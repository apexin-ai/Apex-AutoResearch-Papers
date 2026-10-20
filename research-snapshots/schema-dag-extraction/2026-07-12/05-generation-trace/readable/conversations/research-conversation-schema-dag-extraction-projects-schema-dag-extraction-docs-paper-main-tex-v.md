# Research conversation: 系统通知：审稿审批已通过。请开始审稿。 [论文提交] - 项目: schema-dag-extraction - 论文路径: projects/schema-dag-extraction/docs/paper/main.tex - 目标 v

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 95
- **Recorded user turns:** 1
- **Tool calls:** 29
- **Original source:** `logs/chats/exported-trajectories/account-1/b929ddb9-042f-444e-b6a7-4cb35f1bc04a.jsonl`
- **Structured JSON:** [`8836bb95e1286247d327.json`](../../sessions/88/8836bb95e1286247d327.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T14:14:19.860Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T14:14:19.860Z",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "content": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: schema-dag-extraction\n- 论文路径: projects/schema-dag-extraction/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: Main Conference\n- 截止日期: 2026-05-25\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

---

### Runtime record

_source line 2 · 2026-05-17T14:14:19.864Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T14:14:19.864Z",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a"
}
```

---

## Round 1

93 recorded events

### User

_source line 3 · 2026-05-17T14:14:19.906Z_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema-dag-extraction
- 论文路径: projects/schema-dag-extraction/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "8a1ebb7e-0482-48fd-8e94-1c0dad80a9ca",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T14:14:19.906Z_

```json
{
  "parentUuid": "8a1ebb7e-0482-48fd-8e94-1c0dad80a9ca",
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
      "mcp__agent-ml-research__get_external_review_status",
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
      "mcp__agent-ml-research__get_external_review_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__request_external_review",
      "mcp__agent-ml-research__request_study_approval",
      "mcp__agent-ml-research__submit_review_report_to_research_director",
      "mcp__agent-ml-research__update_review_issues"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "be83ea1c-8be0-48c6-8c90-7cadddce8ba4",
  "timestamp": "2026-05-17T14:14:19.906Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T14:14:19.906Z_

```json
{
  "parentUuid": "be83ea1c-8be0-48c6-8c90-7cadddce8ba4",
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
  "uuid": "03f8caa2-a697-4647-b2f5-f4bcd11f1733",
  "timestamp": "2026-05-17T14:14:19.906Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-17T14:14:19.906Z_

```json
{
  "parentUuid": "03f8caa2-a697-4647-b2f5-f4bcd11f1733",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "68b20fbd-928c-4bb2-a76e-d4c0dbbc8bc5",
  "timestamp": "2026-05-17T14:14:19.906Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Review schema-dag-extraction paper for EMNLP 2026",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a"
}
```

---

### Assistant

_source line 8 · 2026-05-17T14:14:23.426Z_

<details><summary>Logged reasoning block</summary>

```text
收到论文提交，需要开始审稿流程。首先按指示读取 review-director-session-start skill 文件。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68b20fbd-928c-4bb2-a76e-d4c0dbbc8bc5",
  "isSidechain": false,
  "requestId": "req_011Cb8HDGuBhNdK5rSSf3VUU",
  "type": "assistant",
  "uuid": "f627655d-fbe7-467c-9aa6-da7cc94e31c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U9tr836tkgRxzodZMBQ3Sr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15684,
      "cache_read_input_tokens": 11841,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15684,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 131,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15684,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15684
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

_source line 9 · 2026-05-17T14:14:23.528Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CWGuAJ1e5pzLtsYgwcbgyF`</summary>

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
  "parentUuid": "f627655d-fbe7-467c-9aa6-da7cc94e31c3",
  "isSidechain": false,
  "requestId": "req_011Cb8HDGuBhNdK5rSSf3VUU",
  "type": "assistant",
  "uuid": "d2efb704-01e6-444e-bc45-80ac9e42976c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U9tr836tkgRxzodZMBQ3Sr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15684,
      "cache_read_input_tokens": 11841,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15684,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 131,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15684,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15684
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

_source line 10 · 2026-05-17T14:14:23.549Z_

<details><summary>↩ Tool result · `toolu_01CWGuAJ1e5pzLtsYgwcbgyF`</summary>

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
70	### Step 1 — Round N：独立审稿
71	
72	携带 Step 0 搜到的 venue 要求，启动所有 Reviewer：
73	
74	```
75	director_post_to_reviewer(reviewer_id="1", round_number=N, text="你负责 {focus}。...")
76	director_post_to_reviewer(reviewer_id="2", round_number=N, text="你负责 {focus}。...")
77	...（按需）
78	```
79	
80	消息中必须包含：
81	- venue 名称和截止日期
82	- 页数限制和模板名称
83	- 匿名规则
84	- 论文文件路径
85	- **该 Reviewer 的审查侧重**（在消息中明确指定）
86	
87	收集所有 Reviewer 的审稿结果。
88	
89	### Step 2 — 交叉分享（原文转发 + 逐条回应）
90	
91	将每位 Reviewer 的**完整审稿原文**转发给其他 Reviewer，要求逐条回应：
92	
93	```
94	director_post_to_reviewer(reviewer_id="2", round_number=N, text="""
95	以下是 Reviewer 1 的完整审稿意见：
96	
97	{Reviewer 1 的原文}
98	
99	请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。
100	""")
101	```
102	
103	对每位 Reviewer 重复此步骤（每人看到其他所有 Reviewer 的原文）。
104	
105	收集所有交叉回应。
106	
107	### Step 3 — 收敛判断
108	
109	分析所有 Reviewer 的意见和交叉回应：
110	
111	- **关键问题已达成共识**（`[AGREE]` 占多数，无未解决的 `[REBUT]` 矛盾）→ 进入 Step 4
112	- **存在重大分歧**（关键 issue 上有 `[REBUT]` 且双方各有道理）→ 回到 Step 1 开始下一轮，附带聚焦问题
113	- **最多 3 轮**：如果第 3 轮仍有分歧，在报告中如实记录各方观点
114	
115	### Step 4 — 汇总报告 & 投递
116	
117	合并所有轮次的发现，形成统一审稿报告：
118	
119	1. 报告结构：
120	   - **Summary**：论文概述（2-3 句）
121	   - **Strengths**：优点（逐条列出）
122	   - **Weaknesses**：缺点（逐条列出，这是重点，必须严格）
123	   - **Reviewer Consensus**：所有 Reviewer 达成共识的关键问题（标注 `[AGREE]`）
124	   - **Reviewer Divergence**：分歧点及各方理由（标注 `[REBUT]`，如有）
125	   - **Questions**：需要作者澄清的问题
126	   - **Missing References**：遗漏的重要相关工作
127	   - **External Review (Stanford Agentic Reviewer)**：如有外部审稿结果，单独列出其 7 维评分、关键发现、以及与内部审稿的差异；如未返回则标注状态
128	   - **Overall Assessment**：总评 + 评分（strong reject / weak reject / borderline / weak accept / strong accept）+ 置信度
129	   - **Detailed Comments**：逐节详细意见
130	2. **同步 Issue Tracker**（投递前必做）：
131	   - 用 `read_local_file("projects/{project}/artifacts/review_issues.yaml")` 读当前 tracker（不存在视为空）
132	   - 对本轮所有 Weakness/Must-Fix/Should-Fix:
133	     - 与已有 issue 匹配（同 category + 相似 summary）→ 在 `mentions` 追加本轮记录,更新 `last_seen_round`
134	     - 新问题 → 创建条目（id=`R{reviewer}-W{n}`,status=`open`,first_raised_round=本轮）
135	   - 对上轮 `open`/`in_progress` 但本轮**未被任何 Reviewer 提及**的:
136	     - 在 `mentions` 追加 `note: "本轮未提及,可能已修复,待 Research Director 确认"`
137	   - 调 `update_review_issues(project, issues_yaml=完整 YAML)` 写回
138	3. 调用 `submit_review_report_to_research_director` 投递报告 → Research Director
139	4. 向用户（Group C）汇报审核完成
140	
141	此流程只在 session 启动时执行一次。
142	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "d2efb704-01e6-444e-bc45-80ac9e42976c",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "9bafd231-5568-4ee8-9542-9dbd72146e7f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md",
      "content": "---\nname: review-director-session-start\ndescription: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。\npriority: 9\nscope: global\ntags:\n- workflow\n- review\n- session\nversion: 3\nroles:\n- review_director\n---\n\n# Review Director Session 启动流程（圆桌会议模式）\n\n## 初始化\n\n1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）\n2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在\n3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）\n4. 向用户简要汇报：\n   - **投稿目标**：venue 和 deadline\n   - **论文状态**：当前草稿位置和版本\n   - **资料完整性**：提交的材料是否齐全\n   - **下一步**：即将开始的圆桌审稿流程\n\n## 评审流程（收到论文提交后执行）\n\n### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）\n\n1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全\n2. 确认目标投稿 venue（从提交消息中获取）\n3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：\n   - `\"&lt;venue name> 2026 call for papers\" site:aclweb.org`\n   - `\"&lt;venue name> 2026 submission deadline\"`\n   - `\"&lt;venue name> 2026 author guidelines\"`\n4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续\n5. 提取当前版本的格式要求：\n   - 页数限制（正文 / 附录 / 参考文献）\n   - 模板（ACL / IEEE / NeurIPS / ICML / ...）\n   - 匿名规则（double-blind / single-blind / open）\n   - 附录规则（是否允许、是否参与审稿）\n   - 引用格式（natbib / biblatex / 特定 .bst）\n6. 将以上信息作为上下文，随任务一起传递给 Reviewer\n\n⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。\n\n### Step 0.5 — 决定 Reviewer 编排\n\n根据 venue 类型和论文特点，决定：\n- 需要几个 Reviewer（1-5 人）\n- 每个 Reviewer 的审查侧重\n\n参考：\n- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）\n- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）\n- **Workshop / 短文**：1 人（全面审查）\n\n向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。\n\n### Step 0.6 — 外部审稿线（与 Step 1 并行）\n\n检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：\n- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片\n- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程\n- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告\n- 如果到 Step 4 时外部结果仍未返回，调用 `get_external_review_status(project)` 确认状态，在报告中标注\n\n### Step 1 — Round N：独立审稿\n\n携带 Step 0 搜到的 venue 要求，启动所有 Reviewer：\n\n```\ndirector_post_to_reviewer(reviewer_id=\"1\", round_number=N, text=\"你负责 {focus}。...\")\ndirector_post_to_reviewer(reviewer_id=\"2\", round_number=N, text=\"你负责 {focus}。...\")\n...（按需）\n```\n\n消息中必须包含：\n- venue 名称和截止日期\n- 页数限制和模板名称\n- 匿名规则\n- 论文文件路径\n- **该 Reviewer 的审查侧重**（在消息中明确指定）\n\n收集所有 Reviewer 的审稿结果。\n\n### Step 2 — 交叉分享（原文转发 + 逐条回应）\n\n将每位 Reviewer 的**完整审稿原文**转发给其他 Reviewer，要求逐条回应：\n\n```\ndirector_post_to_reviewer(reviewer_id=\"2\", round_number=N, text=\"\"\"\n以下是 Reviewer 1 的完整审稿意见：\n\n{Reviewer 1 的原文}\n\n请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\"\"\")\n```\n\n对每位 Reviewer 重复此步骤（每人看到其他所有 Reviewer 的原文）。\n\n收集所有交叉回应。\n\n### Step 3 — 收敛判断\n\n分析所有 Reviewer 的意见和交叉回应：\n\n- **关键问题已达成共识**（`[AGREE]` 占多数，无未解决的 `[REBUT]` 矛盾）→ 进入 Step 4\n- **存在重大分歧**（关键 issue 上有 `[REBUT]` 且双方各有道理）→ 回到 Step 1 开始下一轮，附带聚焦问题\n- **最多 3 轮**：如果第 3 轮仍有分歧，在报告中如实记录各方观点\n\n### Step 4 — 汇总报告 & 投递\n\n合并所有轮次的发现，形成统一审稿报告：\n\n1. 报告结构：\n   - **Summary**：论文概述（2-3 句）\n   - **Strengths**：优点（逐条列出）\n   - **Weaknesses**：缺点（逐条列出，这是重点，必须严格）\n   - **Reviewer Consensus**：所有 Reviewer 达成共识的关键问题（标注 `[AGREE]`）\n   - **Reviewer Divergence**：分歧点及各方理由（标注 `[REBUT]`，如有）\n   - **Questions**：需要作者澄清的问题\n   - **Missing References**：遗漏的重要相关工作\n   - **External Review (Stanford Agentic Reviewer)**：如有外部审稿结果，单独列出其 7 维评分、关键发现、以及与内部审稿的差异；如未返回则标注状态\n   - **Overall Assessment**：总评 + 评分（strong reject / weak reject / borderline / weak accept / strong accept）+ 置信度\n   - **Detailed Comments**：逐节详细意见\n2. **同步 Issue Tracker**（投递前必做）：\n   - 用 `read_local_file(\"projects/{project}/artifacts/review_issues.yaml\")` 读当前 tracker（不存在视为空）\n   - 对本轮所有 Weakness/Must-Fix/Should-Fix:\n     - 与已有 issue 匹配（同 category + 相似 summary）→ 在 `mentions` 追加本轮记录,更新 `last_seen_round`\n     - 新问题 → 创建条目（id=`R{reviewer}-W{n}`,status=`open`,first_raised_round=本轮）\n   - 对上轮 `open`/`in_progress` 但本轮**未被任何 Reviewer 提及**的:\n     - 在 `mentions` 追加 `note: \"本轮未提及,可能已修复,待 Research Director 确认\"`\n   - 调 `update_review_issues(project, issues_yaml=完整 YAML)` 写回\n3. 调用 `submit_review_report_to_research_director` 投递报告 → Research Director\n4. 向用户（Group C）汇报审核完成\n\n此流程只在 session 启动时执行一次。\n",
      "numLines": 142,
      "startLine": 1,
      "totalLines": 142
    }
  },
  "sourceToolAssistantUUID": "d2efb704-01e6-444e-bc45-80ac9e42976c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Assistant

_source line 11 · 2026-05-17T14:14:26.810Z_

开始执行审稿初始化流程。先获取项目概况和论文文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bafd231-5568-4ee8-9542-9dbd72146e7f",
  "isSidechain": false,
  "requestId": "req_011Cb8HDYbkKhakhfZY2ud3q",
  "type": "assistant",
  "uuid": "6fa89119-9156-48b1-b27b-344fbfcf079f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019EQeCtPkFTxhHa6cHRx6rp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2947,
      "cache_read_input_tokens": 27525,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2947,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 231,
          "cache_read_input_tokens": 27525,
          "cache_creation_input_tokens": 2947,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2947
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

_source line 12 · 2026-05-17T14:14:27.820Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FmCpJjZg2hmKqU6FRv7bTn`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fa89119-9156-48b1-b27b-344fbfcf079f",
  "isSidechain": false,
  "requestId": "req_011Cb8HDYbkKhakhfZY2ud3q",
  "type": "assistant",
  "uuid": "f22491d0-4a84-4279-bf75-a06cfcd071a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019EQeCtPkFTxhHa6cHRx6rp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2947,
      "cache_read_input_tokens": 27525,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2947,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 231,
          "cache_read_input_tokens": 27525,
          "cache_creation_input_tokens": 2947,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2947
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

_source line 13 · 2026-05-17T14:14:27.825Z_

<details><summary>↩ Tool result · `toolu_01FmCpJjZg2hmKqU6FRv7bTn`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__director_get_project_overview"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__director_post_to_reviewer"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__request_external_review"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__get_external_review_status"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__submit_review_report_to_research_director"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__update_review_issues"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f22491d0-4a84-4279-bf75-a06cfcd071a4",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "01977ee2-4001-4263-8a8d-913a9ff81758",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__request_external_review",
      "mcp__agent-ml-research__get_external_review_status",
      "mcp__agent-ml-research__submit_review_report_to_research_director",
      "mcp__agent-ml-research__update_review_issues"
    ],
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "total_deferred_tools": 27
  },
  "sourceToolAssistantUUID": "f22491d0-4a84-4279-bf75-a06cfcd071a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-17T14:14:30.636Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_014EkTSTphuKDNMNUhpxQBEt`</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01977ee2-4001-4263-8a8d-913a9ff81758",
  "isSidechain": false,
  "requestId": "req_011Cb8HDroseXztg9Df1goLQ",
  "type": "assistant",
  "uuid": "e0ba5337-a57c-411f-9ec0-e6828eac1dfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WYNkWgQQSto9bKW1dceeAp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2888,
      "cache_read_input_tokens": 30472,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 144,
          "cache_read_input_tokens": 30472,
          "cache_creation_input_tokens": 2888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2888
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

_source line 15 · 2026-05-17T14:14:30.984Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NDMXkrvmV8GE5j9w5Ju9jf`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0ba5337-a57c-411f-9ec0-e6828eac1dfe",
  "isSidechain": false,
  "requestId": "req_011Cb8HDroseXztg9Df1goLQ",
  "type": "assistant",
  "uuid": "7121b12d-db4c-4a0e-9664-3a4583d27f9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WYNkWgQQSto9bKW1dceeAp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2888,
      "cache_read_input_tokens": 30472,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 144,
          "cache_read_input_tokens": 30472,
          "cache_creation_input_tokens": 2888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2888
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

_source line 16 · 2026-05-17T14:14:31.002Z_

<details><summary>↩ Tool result · `toolu_014EkTSTphuKDNMNUhpxQBEt`</summary>

```text
{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (58 个)\n\n- **exp012_llama_8b_r2_exp2**: DONE (negative) — \n- **exp012_llama_8b_r2**: DONE (success) — \n- **exp006_interaction_2x2**: DONE (negative) — \n- **exp012_llama_awq**: DONE (killed) — \n- **exp012_llama_8b_r3**: DONE (failed) — \n- **exp012_llama_8b**: DONE (killed) — \n- **exp_fewrel_40rel_r3**: DONE (failed) — \n- **exp_fewrel_40rel_r2**: DONE (failed) — \n- **exp012_llama_fewnerd_r4**: DONE (failed) — \n- **exp012_llama_8b_fewnerd**: DONE (failed) — \n- **exp_fewrel_40rel**: DONE (failed) — \n- **exp012_llama_fewnerd_r3**: DONE (failed) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- prompt_sensitivity（准备中）\n- prompt_sensitivity_dry4（准备中）\n- prompt_sensitivity_dry3（准备中）\n- prompt_sensitivity_dry2（准备中）\n- prompt_sensitivity_dry（准备中）\n- exp_aggregation_monte_carlo（准备中）\n- exp_scs_name_def_ablation（准备中）\n- exp_fewrel_contamination_check（准备中）\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- …另有 2 项\n\n## 近期结论\n- **exp_fewshot_bcs_v2** (negative): Few-shot demonstrations (1-shot and 5-shot) reduce the BCS-driven confusability effect (high-BCS accuracy penalty) by grounding type boundaries through explicit examples, tested on extreme-BCS batches (low ~0.36, high ~0.80) where 0-shot delta is ~25-31pp. If delta shrinks significantly under few-shot, confusability is addressable via prompting. If delta persists, confusability is a fundamental schema-structural constraint. ← 基于 exp_fewrel_v2_n25\n- **exp_llama70b_cross_model** (success): LLaMA 3.1 70B-Instruct FP8 will replicate the two-dimensional degradation pattern (count-associated recall decline + confusability-associated type confusion) observed on Qwen3-32B, with BCS-accuracy correlation direction preserved despite potential magnitude differences. 70B scale should show stronger Dimension 2 signal than 8B, closing the gap with 32B. ← 基于 exp_prompt_sensitivity\n  [exp_llama70b_cross_model_analysis](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_llama70b_cross_model/report/exp_llama70b_cross_model_analysis.md)\n- **exp_fewshot_bcs_mitigation** (killed): Few-shot demonstrations (1-shot and 5-shot) reduce the BCS-driven confusability effect (high-BCS accuracy penalty) by grounding type boundaries through explicit examples. If the BCS delta (low-high) shrinks significantly under few-shot, confusability is addressable via better prompting. If delta persists, confusability is a fundamental schema-structural constraint even with demonstrations. ← 基于 exp_fewrel_formal_80rel\n\n## 趋势\n成功 25 / 负向 7 / 失败 10 / 共 46\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\ncqa1-38874: 无 GPU 信息\nwestd-24295: 无 GPU 信息\n\n## 告警\n- exp008_sdgd_zero_fewnerd: 训练失败 — unknown\n- exp012_llama_fewnerd: 训练失败 — unknown\n- exp012_llama_fewnerd_r2: 训练失败 — unknown\n- exp012_llama_fewnerd_r3: 训练失败 — unknown\n- exp012_llama_8b: 已被终止 — unknown\n- exp_fewrel_40rel: 训练失败 — unknown\n- exp012_llama_awq: 已被终止 — unknown\n- exp012_llama_fewnerd_r4: 训练失败 — unknown\n- exp012_llama_8b_fewnerd: 训练失败 — unknown\n- exp_fewrel_40rel_r2: 训练失败 — unknown\n- exp_fewrel_40rel_r3: 训练失败 — unknown\n- exp012_llama_8b_r3: 训练失败 — unknown\n- exp_fewrel_16rel_100batch: 已被终止 — unknown\n- exp_fewshot_bcs_mitigation: 已被终止 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0ba5337-a57c-411f-9ec0-e6828eac1dfe",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "fc5f35fe-2219-4272-9633-787a1e79c384",
  "toolUseResult": "{\"result\":\"# 项目 schema-dag-extraction 概况\\n\\n## 实验状态 (58 个)\\n\\n- **exp012_llama_8b_r2_exp2**: DONE (negative) — \\n- **exp012_llama_8b_r2**: DONE (success) — \\n- **exp006_interaction_2x2**: DONE (negative) — \\n- **exp012_llama_awq**: DONE (killed) — \\n- **exp012_llama_8b_r3**: DONE (failed) — \\n- **exp012_llama_8b**: DONE (killed) — \\n- **exp_fewrel_40rel_r3**: DONE (failed) — \\n- **exp_fewrel_40rel_r2**: DONE (failed) — \\n- **exp012_llama_fewnerd_r4**: DONE (failed) — \\n- **exp012_llama_8b_fewnerd**: DONE (failed) — \\n- **exp_fewrel_40rel**: DONE (failed) — \\n- **exp012_llama_fewnerd_r3**: DONE (failed) — \\n- **exp012_llama_fewnerd_r2**: DONE (failed) — \\n- **exp012_llama_fewnerd**: DONE (failed) — \\n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \\n\\n## 最新报告\\n# Handover — 2026-05-17\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- prompt_sensitivity（准备中）\\n- prompt_sensitivity_dry4（准备中）\\n- prompt_sensitivity_dry3（准备中）\\n- prompt_sensitivity_dry2（准备中）\\n- prompt_sensitivity_dry（准备中）\\n- exp_aggregation_monte_carlo（准备中）\\n- exp_scs_name_def_ablation（准备中）\\n- exp_fewrel_contamination_check（准备中）\\n- exp017_gpt4o_mini_fewrel（准备中）\\n- exp_cross_embedding_sensitivity（准备中）\\n- …另有 2 项\\n\\n## 近期结论\\n- **exp_fewshot_bcs_v2** (negative): Few-shot demonstrations (1-shot and 5-shot) reduce the BCS-driven confusability effect (high-BCS accuracy penalty) by grounding type boundaries through explicit examples, tested on extreme-BCS batches (low ~0.36, high ~0.80) where 0-shot delta is ~25-31pp. If delta shrinks significantly under few-shot, confusability is addressable via prompting. If delta persists, confusability is a fundamental schema-structural constraint. ← 基于 exp_fewrel_v2_n25\\n- **exp_llama70b_cross_model** (success): LLaMA 3.1 70B-Instruct FP8 will replicate the two-dimensional degradation pattern (count-associated recall decline + confusability-associated type confusion) observed on Qwen3-32B, with BCS-accuracy correlation direction preserved despite potential magnitude differences. 70B scale should show stronger Dimension 2 signal than 8B, closing the gap with 32B. ← 基于 exp_prompt_sensitivity\\n  [exp_llama70b_cross_model_analysis](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_llama70b_cross_model/report/exp_llama70b_cross_model_analysis.md)\\n- **exp_fewshot_bcs_mitigation** (killed): Few-shot demonstrations (1-shot and 5-shot) reduce the BCS-driven confusability effect (high-BCS accuracy penalty) by grounding type boundaries through explicit examples. If the BCS delta (low-high) shrinks significantly under few-shot, confusability is addressable via better prompting. If delta persists, confusability is a fundamental schema-structural constraint even with demonstrations. ← 基于 exp_fewrel_formal_80rel\\n\\n## 趋势\\n成功 25 / 负向 7 / 失败 10 / 共 46\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ncqa1-38874: 无 GPU 信息\\nwestd-24295: 无 GPU 信息\\n\\n## 告警\\n- exp008_sdgd_zero_fewnerd: 训练失败 — unknown\\n- exp012_llama_fewnerd: 训练失败 — unknown\\n- exp012_llama_fewnerd_r2: 训练失败 — unknown\\n- exp012_llama_fewnerd_r3: 训练失败 — unknown\\n- exp012_llama_8b: 已被终止 — unknown\\n- exp_fewrel_40rel: 训练失败 — unknown\\n- exp012_llama_awq: 已被终止 — unknown\\n- exp012_llama_fewnerd_r4: 训练失败 — unknown\\n- exp012_llama_8b_fewnerd: 训练失败 — unknown\\n- exp_fewrel_40rel_r2: 训练失败 — unknown\\n- exp_fewrel_40rel_r3: 训练失败 — unknown\\n- exp012_llama_8b_r3: 训练失败 — unknown\\n- exp_fewrel_16rel_100batch: 已被终止 — unknown\\n- exp_fewshot_bcs_mitigation: 已被终止 — unknown\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "# 项目 schema-dag-extraction 概况\n\n## 实验状态 (58 个)\n\n- **exp012_llama_8b_r2_exp2**: DONE (negative) — \n- **exp012_llama_8b_r2**: DONE (success) — \n- **exp006_interaction_2x2**: DONE (negative) — \n- **exp012_llama_awq**: DONE (killed) — \n- **exp012_llama_8b_r3**: DONE (failed) — \n- **exp012_llama_8b**: DONE (killed) — \n- **exp_fewrel_40rel_r3**: DONE (failed) — \n- **exp_fewrel_40rel_r2**: DONE (failed) — \n- **exp012_llama_fewnerd_r4**: DONE (failed) — \n- **exp012_llama_8b_fewnerd**: DONE (failed) — \n- **exp_fewrel_40rel**: DONE (failed) — \n- **exp012_llama_fewnerd_r3**: DONE (failed) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- prompt_sensitivity（准备中）\n- prompt_sensitivity_dry4（准备中）\n- prompt_sensitivity_dry3（准备中）\n- prompt_sensitivity_dry2（准备中）\n- prompt_sensitivity_dry（准备中）\n- exp_aggregation_monte_carlo（准备中）\n- exp_scs_name_def_ablation（准备中）\n- exp_fewrel_contamination_check（准备中）\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- …另有 2 项\n\n## 近期结论\n- **exp_fewshot_bcs_v2** (negative): Few-shot demonstrations (1-shot and 5-shot) reduce the BCS-driven confusability effect (high-BCS accuracy penalty) by grounding type boundaries through explicit examples, tested on extreme-BCS batches (low ~0.36, high ~0.80) where 0-shot delta is ~25-31pp. If delta shrinks significantly under few-shot, confusability is addressable via prompting. If delta persists, confusability is a fundamental schema-structural constraint. ← 基于 exp_fewrel_v2_n25\n- **exp_llama70b_cross_model** (success): LLaMA 3.1 70B-Instruct FP8 will replicate the two-dimensional degradation pattern (count-associated recall decline + confusability-associated type confusion) observed on Qwen3-32B, with BCS-accuracy correlation direction preserved despite potential magnitude differences. 70B scale should show stronger Dimension 2 signal than 8B, closing the gap with 32B. ← 基于 exp_prompt_sensitivity\n  [exp_llama70b_cross_model_analysis](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_llama70b_cross_model/report/exp_llama70b_cross_model_analysis.md)\n- **exp_fewshot_bcs_mitigation** (killed): Few-shot demonstrations (1-shot and 5-shot) reduce the BCS-driven confusability effect (high-BCS accuracy penalty) by grounding type boundaries through explicit examples. If the BCS delta (low-high) shrinks significantly under few-shot, confusability is addressable via better prompting. If delta persists, confusability is a fundamental schema-structural constraint even with demonstrations. ← 基于 exp_fewrel_formal_80rel\n\n## 趋势\n成功 25 / 负向 7 / 失败 10 / 共 46\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\ncqa1-38874: 无 GPU 信息\nwestd-24295: 无 GPU 信息\n\n## 告警\n- exp008_sdgd_zero_fewnerd: 训练失败 — unknown\n- exp012_llama_fewnerd: 训练失败 — unknown\n- exp012_llama_fewnerd_r2: 训练失败 — unknown\n- exp012_llama_fewnerd_r3: 训练失败 — unknown\n- exp012_llama_8b: 已被终止 — unknown\n- exp_fewrel_40rel: 训练失败 — unknown\n- exp012_llama_awq: 已被终止 — unknown\n- exp012_llama_fewnerd_r4: 训练失败 — unknown\n- exp012_llama_8b_fewnerd: 训练失败 — unknown\n- exp_fewrel_40rel_r2: 训练失败 — unknown\n- exp_fewrel_40rel_r3: 训练失败 — unknown\n- exp012_llama_8b_r3: 训练失败 — unknown\n- exp_fewrel_16rel_100batch: 已被终止 — unknown\n- exp_fewshot_bcs_mitigation: 已被终止 — unknown"
    }
  },
  "sourceToolAssistantUUID": "e0ba5337-a57c-411f-9ec0-e6828eac1dfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-17T14:14:31.004Z_

<details><summary>↩ Tool result · `toolu_01NDMXkrvmV8GE5j9w5Ju9jf`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7121b12d-db4c-4a0e-9664-3a4583d27f9c",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "0dfcb562-c62d-430c-a45c-cefefee0271b",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "total_deferred_tools": 27
  },
  "sourceToolAssistantUUID": "7121b12d-db4c-4a0e-9664-3a4583d27f9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: schema-dag-extraction - 论文路径: projects/schema-dag-extraction/docs/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: Main Conference - 截止日期: 2026-05-25  请 `Read /home/ubun…",
  "leafUuid": "0dfcb562-c62d-430c-a45c-cefefee0271b",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Review schema-dag-extraction paper for EMNLP 2026",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a"
}
```

---

### Assistant

_source line 20 · 2026-05-17T14:14:34.465Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to:
1. Search for EMNLP 2026 venue requirements (CFP, submission guidelines)
2. Read the paper file
3. Check for existing review_issues.yaml
4. Check external review config

Let me do these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dfcb562-c62d-430c-a45c-cefefee0271b",
  "isSidechain": false,
  "requestId": "req_011Cb8HE6jHEwdn92jDgtZd2",
  "type": "assistant",
  "uuid": "8a419d8c-2113-4dfa-bb4d-59bb1c608e3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8UrPYUfX54aGrJJycweSt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2224,
      "cache_read_input_tokens": 33360,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2224,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 404,
          "cache_read_input_tokens": 33360,
          "cache_creation_input_tokens": 2224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2224
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

_source line 21 · 2026-05-17T14:14:35.515Z_

项目概况已获取。现在执行 Step 0：搜索 EMNLP 2026 CFP 要求 + 读取论文文件 + 检查 issue tracker。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a419d8c-2113-4dfa-bb4d-59bb1c608e3e",
  "isSidechain": false,
  "requestId": "req_011Cb8HE6jHEwdn92jDgtZd2",
  "type": "assistant",
  "uuid": "68cfc633-0957-46ab-a8b9-4094235b276d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8UrPYUfX54aGrJJycweSt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2224,
      "cache_read_input_tokens": 33360,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2224,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 404,
          "cache_read_input_tokens": 33360,
          "cache_creation_input_tokens": 2224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2224
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

_source line 22 · 2026-05-17T14:14:36.978Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017WDvNjGqn9Zp8q73pR9tdU`</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR",
  "allowed_domains": [
    "aclweb.org",
    "2026.emnlp.org",
    "openreview.net"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68cfc633-0957-46ab-a8b9-4094235b276d",
  "isSidechain": false,
  "requestId": "req_011Cb8HE6jHEwdn92jDgtZd2",
  "type": "assistant",
  "uuid": "1cb1385c-2c71-4d4b-a280-c18ea86b3b7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8UrPYUfX54aGrJJycweSt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2224,
      "cache_read_input_tokens": 33360,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2224,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 404,
          "cache_read_input_tokens": 33360,
          "cache_creation_input_tokens": 2224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2224
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

_source line 23 · 2026-05-17T14:14:38.408Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Aps55KRBeenNV5YiaZDHcA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cb1385c-2c71-4d4b-a280-c18ea86b3b7e",
  "isSidechain": false,
  "requestId": "req_011Cb8HE6jHEwdn92jDgtZd2",
  "type": "assistant",
  "uuid": "db6e4808-8f7f-4204-ba4e-ec49911fbe1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8UrPYUfX54aGrJJycweSt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2224,
      "cache_read_input_tokens": 33360,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2224,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 404,
          "cache_read_input_tokens": 33360,
          "cache_creation_input_tokens": 2224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2224
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

_source line 24 · 2026-05-17T14:14:38.774Z_

<details><summary>↩ Tool result · `toolu_01Aps55KRBeenNV5YiaZDHcA`</summary>

```text
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
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B and 70B-Instruct (FP8). Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Dimension~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43	
44	\item \textbf{Factorial interaction tests.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms bounded association ($p_{\text{TOST}} = 0.003$ at $\pm 3$\,pp, interaction = 0.47\,pp; Appendix~\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity. The TOST equivalence test is estimated from BCS-controlled batches (counts 4--40) where BCS variation is sufficient; generalization to broader count ranges requires additional controlled experiments.
45	
46	\item \textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions. For Few-NERD, SCS is computed from the extraction model's own embeddings (Qwen3), creating a shared-representation dependency. MiniLM cross-check yields a conservative but directionally consistent estimate ($r = 0.172$ vs $r = 0.138$; confusion matrix correlation 0.894), suggesting the effect is not an artifact of shared representations.
47	
48	\item \textbf{NER evaluation metric.} Our exact-match NER evaluation conflates boundary errors (partial span overlap) with type errors (correct span, wrong label). Relaxed matching may yield different confusability effect sizes, as boundary ambiguity may correlate with schema complexity independently of type similarity.
49	
50	\item \textbf{RE format specificity.} RE's clean dimension separation may reflect its closed-set classification format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction.
51	
52	\item \textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. The controlled stratification provides evidence consistent with a directional relationship but does not establish interventional causality.
53	
54	\item \textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\%$\to$50.4\%) cannot be explained by uniform contamination, which would elevate all conditions equally. BCS slope consistency across independent and within-pool conditions (permutation $p = 0.60$) provides a robustness check that is difficult to reconcile with non-uniform contamination, which would differentially affect specific type subsets. DocRED (2019) provides a lower-contamination-risk replication with consistent BCS--accuracy slopes ($R^2 = 0.53$). Adding train-origin ratio as a covariate leaves the BCS partial effect unchanged ($p = 0.245$ for origin; Appendix~\ref{app:split-origin}).
55	\end{enumerate}
56	
57	\paragraph{Multiple comparisons.} Cross-dataset comparisons (FewRel, DocRED, Few-NERD, MAVEN) serve as independent replications of the same hypothesis and do not require family-wise correction \citep{rothman-1990}. Within-dataset secondary analyses (e.g., quartile comparisons, slope sensitivity checks) involve multiple looks at the same data; we report individual $p$-values and note that core claims rest on effects reaching $p < 0.001$ \citep{dror-2018-significance}.
58	
59	\input{checklist}
60	
61	\bibliography{references}
62	
63	\appendix
64	
65	\section{Additional Figures}
66	\label{sec:appendix_figures}
67	
68	\begin{table}[h]
69	\centering
70	\small
71	\begin{tabular}{lrr}
72	\toprule
73	\textbf{Count} & \textbf{Llama-3.1-8B} & \textbf{Qwen3-32B} \\
74	\midrule
75	1 & 0.702 & 0.640 \\
76	64 & 0.273 & 0.304 \\
77	\midrule
78	Decline & $-$43\,pp & $-$34\,pp \\
79	\bottomrule
80	\end{tabular}
81	\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\S\ref{sec:model}) for fair cross-model comparison; the count-curve results in \S\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\ 0.64 at count${}\,=\,1$) due to over-prediction under v1.}
82	\label{tab:cross_model}
83	\end{table}
84	
85	\begin{table}[h]
86	\centering
87	\small
88	\resizebox{\columnwidth}{!}{%
89	\begin{tabular}{crrrrrr}
90	\toprule
91	& \multicolumn{3}{c}{\textbf{Llama-3.1-8B}} & \multicolumn{3}{c}{\textbf{Qwen3-32B}} \\
92	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
93	\textbf{Count} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} \\
94	\midrule
95	8 & 78.1\% & 51.0\% & $-$27.1 & 82.3\% & 51.0\% & $-$31.2 \\
96	16 & 75.5\% & 51.6\% & $-$23.9 & 82.8\% & 51.6\% & $-$31.2 \\
97	\bottomrule
98	\end{tabular}}
99	\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\approx$51\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\Delta$, in pp) is 77--87\% as large on Llama-3.1-8B as on Qwen3-32B.}
100	\label{tab:cross_model_bcs}
101	\end{table}
102	
103	\begin{table}[h]
104	\centering
105	\small
106	\resizebox{\columnwidth}{!}{%
107	\begin{tabular}{llrrrrrrr}
108	\toprule
109	 & & \multicolumn{5}{c}{\textbf{BCS Bin}} & & \\
110	\cmidrule(lr){3-7}
111	\textbf{Task} & \textbf{Error} & \textbf{Solo} & \textbf{Low} & \textbf{Mid} & \textbf{High} & \textbf{V.High} & \textbf{$\rho$} & \textbf{$p$} \\
112	\midrule
113	NER & IntraSub & 0\% & 1.6\% & 10.6\% & 49.4\% & --- & 1.000 & ${<}0.001$ \\
114	RE  & IntraSub & 0\% & 4.2\% & 13.0\% & 20.3\% & 32.3\% & 0.954 & ${<}\,0.001$ \\
115	\midrule
116	NER & Missed & --- & 42.8\% & 64.8\% & 49.9\% & --- & --- & --- \\
117	RE  & Missed & --- & 10.4\% & 11.3\% & 13.1\% & 15.7\% & --- & --- \\
118	\bottomrule
119	\end{tabular}}
120	\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}
121	\label{tab:error_taxonomy}
122	\end{table}
123	
124	\section{SDGD Full Protocol and Results}
125	\label{sec:appendix_sdgd}
126	
127	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, the extreme case where each type is extracted in isolation.
128	
129	Single-pass extraction achieves F1\,=\,0.445 (P\,=\,0.563, R\,=\,0.368). SDGD obtains F1\,=\,0.251 (P\,=\,0.210, R\,=\,0.314), a 44\% relative drop. Random batching reaches F1\,=\,0.320 (P\,=\,0.249, R\,=\,0.446), and per-type extraction yields F1\,=\,0.292 (P\,=\,0.194, R\,=\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\ref{tab:sdgd_results}).
130	
131	\begin{table}[h]
132	\centering
133	\small
134	\resizebox{\columnwidth}{!}{%
135	\begin{tabular}{lrccc}
136	\toprule
137	\textbf{Mode} & \textbf{\# Batches} & \textbf{Precision} & \textbf{Recall} & \textbf{F1} \\
138	\midrule
139	single\_pass & 1 & 0.563 & 0.368 & 0.445 \\
140	\midrule
141	sdgd\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\
142	random\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\
143	per\_type & 66 & 0.194 & 0.586 & 0.292 \\
144	\midrule
145	sdgd\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\
146	random\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\
147	\bottomrule
148	\end{tabular}}
149	\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \texttt{min\_batch\_size=8} (reducing 8$\to$4 batches for sdgd\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}
150	\label{tab:sdgd_results}
151	\end{table}
152	
153	Decomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.
154	
155	Our v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\_zero: 0.210$\to$0.324; random\_batch: 0.249$\to$0.331), but at the cost of disproportionate recall loss (0.314$\to$0.191; 0.446$\to$0.276), yielding lower F1 in both modes (sdgd\_zero: 0.251$\to$0.241; random\_batch: 0.320$\to$0.301).
156	
157	\subsection{Practical Routing Strategies on RE}
158	\label{sec:appendix_routing}
159	
160	We evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.
161	
162	\begin{table}[h]
163	\centering
164	\small
165	\begin{tabular}{@{}lrr@{}}
166	\toprule
167	\textbf{Strategy} & \textbf{Accuracy} & \textbf{$\Delta$ vs.\ Single-Pass} \\
168	\midrule
169	Oracle (gold label) & 72.4\% & +22.0\,pp \\
170	\midrule
171	Max-conf (positive only) & 36.5\% & $-$14.0\,pp \\
172	None-aware & 36.5\% & $-$14.0\,pp \\
173	Margin (positive only) & 35.9\% & $-$14.5\,pp \\
174	Max-conf (all) & 27.7\% & $-$22.7\,pp \\
175	Random & 14.7\% & $-$35.7\,pp \\
176	\midrule
177	Single-pass (no decomposition) & 50.4\% & --- \\
178	\bottomrule
179	\end{tabular}
180	\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\%.}
181	\label{tab:routing_strategies}
182	\end{table}
183	
184	\section{Factorial Analysis and Separability Test}
185	\label{sec:appendix_factorial}
186	
187	To formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\sim$ $\log_2$\,count $+$ BCS $+$ count$\times$BCS) across 69 batches from FewRel spanning five count levels ($k \in \{4, 8, 16, 32, 40\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\,pp). A TOST equivalence test with a $\pm 3$\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\text{TOST}} = 0.003$), supporting bounded association between count and confusability effects.
188	
189	A $2 \times 2$ factorial sensitivity check on FewRel (count $\in \{8, 16\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\S\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.
190	
191	\paragraph{Equivalence margin justification.}
192	We set the $\pm 3$\,pp margin based on three converging anchors. \emph{Empirical}: typical random-batch confusability variation produces 2--5\,pp accuracy differences (batch SD $\approx 4.6$\,pp at count 32). \emph{Practical}: a ${<}3$\,pp accuracy difference falls below deployment-relevant thresholds. \emph{Statistical}: 3\,pp $\approx 0.5 \times$ batch SD, equivalent to Cohen's $d \approx 0.5$ (medium effect threshold; \citealt{lakens-2017-equivalence}). A 3\,pp interaction atop the 2.2\,pp confusability main effect would represent ${>}130\%$ amplification, fundamentally changing whether confusability warrants mitigation. At $\pm 2$\,pp (marginally equivalent, $p = 0.047$), interaction remains bounded below the main effect itself.
193	
194	\begin{table}[h]
195	\centering
196	\small
197	\begin{tabular}{crrl}
198	\toprule
199	\textbf{Margin (pp)} & \textbf{$t_{\text{upper}}$} & \textbf{$p_{\text{TOST}}$} & \textbf{Conclusion} \\
200	\midrule
201	$\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\
202	$\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\
203	$\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\
204	$\pm 5$ & $-5.02$ & ${<}\,0.001$ & Equivalent \\
205	\bottomrule
206	\end{tabular}
207	\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\,pp, 90\% CI [$-$1.0, 2.0]\,pp) is bounded below 2\,pp at marginal significance ($p = 0.047$), confirming that the $\pm 3$\,pp choice does not drive the equivalence conclusion. At $\pm 1$\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}
208	\label{tab:tost_sensitivity}
209	\end{table}
210	
211	\paragraph{Logit-scale sensitivity.}
212	Because accuracy near 50\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\pm 3$\,pp margin ($\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\,pp, still within the $\pm 3$\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check.
213	
214	\section{Within-Pool CI Details}
215	\label{sec:appendix_within_pool}
216	
217	The quartile $\Delta$ for 80-pool 16-relation subsets ($-$3.92\,pp, 95\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.
218	
219	\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}
220	\label{sec:appendix_residualized_bcs}
221	
222	Section~\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.
223	
224	\paragraph{Confound identification.}
225	For each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:
226	\begin{itemize}[itemsep=2pt,leftmargin=*]
227	\item \textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.
228	\item \textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.
229	\end{itemize}
230	
231	\paragraph{Partial correlation results.}
232	Table~\ref{tab:residualized_bcs} reports raw Spearman $\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.
233	
234	\begin{table}[h]
235	\centering
236	\small
237	\resizebox{\columnwidth}{!}{%
238	\begin{tabular}{llcccc}
239	\toprule
240	\textbf{Embedding} & \textbf{Control} & \textbf{Raw $\rho$} & \textbf{Raw $p$} & \textbf{Partial $r$} & \textbf{Partial $p$} \\
241	\midrule
242	MiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\
243	MiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\
244	MiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\
245	\midrule
246	Qwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\
247	Qwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\
248	Qwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\
249	\bottomrule
250	\end{tabular}}
251	\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \texttt{exp\_maven\_residualized\_bcs}.}
252	\label{tab:residualized_bcs}
253	\end{table}
254	
255	\paragraph{Interpretation.}
256	The two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.
257	
258	Under joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.
259	
260	\section{Batch Composition Results}
261	\label{sec:appendix_batch_composition}
262	
263	See Table~\ref{tab:batch_composition} and the accompanying discussion in \S\ref{sec:sdgd}.
264	
265	\input{prompt_appendix}
266	
267	\section{Prompt Version Sensitivity Analysis}
268	\label{sec:appendix_prompt_sensitivity}
269	
270	We assess whether the confusability effects reported in \S\ref{sec:bcs_controlled}--\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
271	
272	\paragraph{RE (FewRel).}
273	Under the v1 prompt, the extreme-batch BCS gap (Table~\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; 95\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.
274	
275	\paragraph{NER (Few-NERD).}
276	The batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\text{BCS}, \text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\S\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.
277	
278	\paragraph{Interpretation.}
279	The $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\% vs.\ 82.3\%), but type confusion under high confusability persists (59.7\% vs.\ 51.0\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.
280	
281	\subsection{Cross-Prompt-Variant BCS Correlation}
282	\label{sec:appendix_prompt_variants}
283	
284	To verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.
285	
286	\begin{table}[h]
287	\centering
288	\small
289	\begin{tabular}{llrrrr}
290	\toprule
291	\textbf{Variant} & \textbf{Count} & \textbf{Mean Acc} & \textbf{$r$} & \textbf{$p$} \\
292	\midrule
293	V2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\
294	V2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\
295	Instruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\
296	Instruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\
297	Chain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\
298	Chain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\
299	Minimal & 8 & 0.852 & $-$0.170 & 0.638 \\
300	Minimal & 32 & 0.615 & $-$0.771 & 0.009 \\
301	\bottomrule
302	\end{tabular}
303	\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}
304	\label{tab:prompt_variants}
305	\end{table}
306	
307	At count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.
308	
309	\section{BCS Aggregation Sensitivity}
310	\label{sec:appendix_bcs_sensitivity}
311	
312	We define Batch Confusability Score (BCS) as the \emph{mean} pairwise SCS across all type pairs in a batch (\S\ref{sec:bcs_controlled}). An alternative definition takes the \emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.
313	
314	\begin{table}[h]
315	\centering
316	\small
317	\resizebox{\columnwidth}{!}{%
318	\begin{tabular}{llcccc}
319	\toprule
320	\textbf{Aggregation} & \textbf{Condition} & \textbf{Slope} & \textbf{95\% CI} & \textbf{$r$} & \textbf{$p$} \\
321	\midrule
322	MEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\,0.001$ \\
323	MEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\
324	\midrule
325	MAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\,0.001$ \\
326	MAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\
327	\bottomrule
328	\end{tabular}}
329	\caption{BCS--accuracy regression under mean vs.\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \approx 0.60$; MAX $p \approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}
330	\label{tab:bcs_aggregation}
331	\end{table}
332	
333	MAX aggregation yields stronger correlations ($r = -0.637$ vs.\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.
334	
335	\section{BCS-Controlled Detailed Results}
336	\label{app:bcs-controlled-table}
337	
338	\begin{table}[h]
339	\centering
340	\small
341	\resizebox{\columnwidth}{!}{%
342	\begin{tabular}{lcrrrr}
343	\toprule
344	\textbf{Schema} & \textbf{Count} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
345	\midrule
346	16-rel & 8 & 88.9\% & 79.8\% & $-$9.1 & --- \\
347	80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\
348	80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\
349	\bottomrule
350	\end{tabular}}
351	\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\ref{tab:within_pool}; see \S\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}
352	\label{tab:bcs_controlled}
353	\end{table}
354	
355	\section{Within-Pool Analysis Methodology}
356	\label{app:within-pool-method}
357	
358	A potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.
359	
360	\begin{table}[h]
361	\centering
362	\small
363	\resizebox{\columnwidth}{!}{%
364	\begin{tabular}{lrrrrrrr}
365	\toprule
366	& \multicolumn{4}{c}{\textbf{Regression (BCS $\to$ Accuracy)}} & \multicolumn{2}{c}{\textbf{Quartile $\Delta$}} \\
367	\cmidrule(lr){2-5} \cmidrule(lr){6-7}
368	\textbf{Setting} & \textbf{Slope} & \textbf{95\% CI} & \textbf{$r$} & \textbf{$p$} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
369	\midrule
370	Independent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\
371	80-pool $\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\
372	Full 80-rel ($n{=}25$)$^\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\
373	\midrule
374	\multicolumn{7}{l}{\footnotesize Permutation test (16-rel vs.\ 80-pool slopes): $p \approx 0.60$ (5{,}000 permutations)} \\
375	\multicolumn{7}{l}{\footnotesize $^\dagger$BCS range (IQR\,=\,0.033) insufficient for regression; slope not interpretable.} \\
376	\bottomrule
377	\end{tabular}}
378	\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\ref{sec:appendix_within_pool} for CI interpretation.}
379	\label{tab:within_pool}
380	\end{table}
381	
382	The within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \approx 0.60$). The smaller quartile gap ($-$3.92\,pp vs.\ $-$5.31\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\ref{sec:appendix_within_pool}).
383	
384	In the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.
385	
386	\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}
387	\label{app:scs-ablation}
388	
389	Table~\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.
390	
391	\begin{table}[h]
392	\centering
393	\small
394	\begin{tabular}{lcccc}
395	\toprule
396	Dataset & SCS$_\text{name}$ $r$ & SCS$_\text{def}$ $r$ & $\Delta r$ & Matrix corr. \\
397	\midrule
398	Few-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\
399	MAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\
400	FewRel & 0.178 & 0.193 & +0.015 & 0.848 \\
401	\bottomrule
402	\end{tabular}
403	\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\Delta r$ indicates no systematic benefit from including definitions.}
404	\label{tab:scs-ablation}
405	\end{table}
406	
407	Few-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, making name-only SCS a direct match to model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.
408	
409	\section{Pair-to-Batch Aggregation Simulation}
410	\label{app:aggregation-sim}
411	
412	The following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\S\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.
413	
414	\paragraph{Setup.} We examine whether the pair-level $R^2 \approx 7\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \approx 22\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\rho_\text{SCS} = 0.35$). For batches of $k=8$ types ($\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.
415	
416	\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\sim$3$\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\approx 3.4$, not 28).
417	
418	\paragraph{Unconditional baseline.}
419	When the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ [95\% CI: 0.001--0.151], well below the observed $R^2 = 0.218$. The analytical formula confirms: $\text{SNR} \times \text{EF} / (\text{SNR} \times \text{EF} + 1) = 0.042$ with the same effective factor $\text{EF} = 3.35$. This ${\sim}5\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \emph{active} confusable pairs, not uniform contributions from all pairs.
420	
421	\section{BCS Independence from Type Composition}
422	\label{app:bcs-composition}
423	
424	FewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\% of explained variance), composition unique $R^2 = 0.298$ (42.3\%), and shared $R^2 = 0.147$ (20.9\%). The near-orthogonality of predictors (VIF${}\,=\,1.06$, $r(\text{BCS}, \text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than proxying for type difficulty.
425	
426	\section{Split-Origin Covariate Analysis}
427	\label{app:split-origin}
428	
429	FewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.
430	
431	\paragraph{Method.}  Across 213 multi-type batches ($k \geq 2$) from the batch-composition experiment (\S\ref{sec:sdgd}) and the factorial design (\S\ref{sec:bcs_controlled}), we compute $\texttt{train\_origin\_ratio} = n_{\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, reflecting the 64/80 base rate).  We fit:
432	\[
433	\text{accuracy} = \beta_0 + \beta_{\text{BCS}} \cdot \text{BCS} + \beta_{\text{origin}} \cdot \text{train\_origin\_ratio} + \varepsilon
434	\]
435	
436	\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\beta_{\text{BCS}} = -0.416$, $p < 10^{-16}$ (vs.\ $\beta = -0.412$, $p < 10^{-16}$ without the covariate).  Train-origin ratio is not independently significant ($\beta_{\text{origin}} = -0.057$, $p = 0.245$), and $\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.
437	
438	Pairwise SCS distributions do not differ significantly between train-origin (64 types, mean\,=\,0.880) and val-origin (16 types, mean\,=\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$), confirming that the train/val split does not introduce systematic confusability bias.
439	
440	\section{Cross-Seed Variance Decomposition}
441	\label{app:variance-decomposition}
442	
443	\begin{table}[h]
444	\centering
445	\small
446	\begin{tabular}{rrrr}
447	\toprule
448	\textbf{Count} & \textbf{Batch SD} & \textbf{Seed SD} & \textbf{Ratio} \\
449	\midrule
450	4 & 0.0889 & 0.0122 & 53.5 \\
451	8 & 0.0820 & 0.0098 & 70.0 \\
452	16 & 0.0626 & 0.0270 & 5.4 \\
453	32 & 0.0462 & 0.0091 & 26.0 \\
454	40 & 0.0421 & 0.0019 & 474.4 \\
455	64 & 0.0245 & 0.0022 & 119.8 \\
456	80 & 0.0001 & 0.0088 & $<$0.1 \\
457	\bottomrule
458	\end{tabular}
459	\caption{Variance decomposition on FewRel (3 seeds $\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}
460	\label{tab:variance_decomposition}
461	\end{table}
462	
463	Intra-batch variance dominates inter-seed variance by 5--474$\times$ across count levels 4--64 (mean 125$\times$), confirming that random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\,=\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\,pp, likely attributable to FP8 quantization non-determinism).
464	
465	\section{Cross-Domain Connections}
466	\label{app:cross-domain}
467	
468	The schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.
469	
470	\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}
471	\label{sec:appendix_cross_model_70b}
472	
473	To test whether the two-dimensional degradation pattern generalizes across model families, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\S\ref{sec:count_curves}, \S\ref{sec:bcs_controlled}).
474	
475	\begin{table}[h]
476	\centering
477	\small
478	\begin{tabular}{lrr}
479	\toprule
480	\textbf{Count} & \textbf{LLaMA-70B} & \textbf{Qwen3-32B} \\
481	\midrule
482	\multicolumn{3}{l}{\textit{RE (FewRel, Classification Accuracy)}} \\
483	8  & 0.757 & 0.805 \\
484	16 & 0.685 & 0.719 \\
485	32 & 0.601 & 0.652 \\
486	64 & 0.504 & 0.539 \\
487	80 & 0.450 & 0.504 \\
488	\midrule
489	\multicolumn{3}{l}{\textit{NER (Few-NERD, Text+Type Match Recall)}} \\
490	2  & 0.323 & 0.515 \\
491	6  & 0.300 & 0.399 \\
492	12 & 0.278 & 0.318 \\
493	22 & 0.252 & 0.279 \\
494	44 & 0.297 & 0.309 \\
495	66 & 0.273 & 0.407 \\
496	\bottomrule
497	\end{tabular}
498	\caption{Cross-model count curves for LLaMA-3.1-70B-Instruct (FP8) and Qwen3-32B. RE decline (count 8$\to$80): $-$30.7\,pp (70B) vs.\ $-$30.1\,pp (32B). NER decline (count 2$\to$22): $-$7.1\,pp (70B) vs.\ $-$23.6\,pp (32B); both models exhibit a U-shaped rebound at higher counts. 25 batches per count level, same samples and batch compositions across models (seed 42). All metrics are micro-averaged across batches.}
499	\label{tab:cross_model_70b}
500	\end{table}
501	
502	Table~\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\,pp (70B) versus $-$30.1\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-driven decline) is directionally consistent across architectures for RE.
503	
504	On NER, the count-driven decline direction is consistent across models: both 70B and Qwen3 show a recall decline from count 2 to count 22 (70B: 0.323$\to$0.252, $-$7.1\,pp; Qwen3: 0.515$\to$0.279, $-$23.6\,pp). Both models also exhibit a U-shaped rebound at higher counts (70B: 0.252 at count 22 $\to$ 0.297 at count 44; Qwen3: 0.279 at count 22 $\to$ 0.407 at count 66), which cross-validates the U-shape phenomenon. The magnitude difference reflects a precision-recall tradeoff: 70B operates more conservatively (higher precision, lower recall), while Qwen3 over-predicts (higher recall, lower precision, especially at low counts).
505	
506	For the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\Delta = +10.9$\,pp, 95\% CI: [$+$3.0, $+$20.1]). The confidence interval excludes zero, confirming the confusability effect at the 70B scale.
507	
508	In summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-driven decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.
509	
510	\section{Few-Shot Prompting and Confusability}
511	\label{sec:appendix_fewshot_bcs}
512	
513	To test whether in-context demonstrations mitigate the BCS-driven confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \S\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\approx 0.36$; 25 high-BCS, mean $\approx 0.80$), drawn from the pre-constructed batch pool of \S\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type.
514	
515	\begin{table}[h]
516	\centering
517	\small
518	\resizebox{\columnwidth}{!}{\begin{tabular}{lrrrl}
519	\toprule
520	\textbf{Condition} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
521	\midrule
522	0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\
523	1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\
524	5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\
525	\bottomrule
526	\end{tabular}}
527	\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\,pp over 0-shot) but provide no benefit on high-BCS batches ($-$1.0 to +5.6\,pp). The confusability gap widens from +18.5\,pp (0-shot) to +22.8\,pp (5-shot). All metrics are micro-averaged across batches.}
528	\label{tab:fewshot_bcs}
529	\end{table}
530	
531	Demonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide negligible benefit: the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\,pp from 0-shot to 5-shot), with all three confidence intervals excluding zero. This indicates that BCS-driven type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering.
532	
533	The 0-shot gap (+18.5\,pp) is smaller than the extreme-batch gap reported in \S\ref{sec:bcs_controlled} (+25.5\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.
534	
535	\end{document}
536	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db6e4808-8f7f-4204-ba4e-ec49911fbe1b",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "59f071ac-265a-43ac-9a7d-b6072844ea39",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{How Does Schema Complexity Predict Performance\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B and 70B-Instruct (FP8). Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Dimension~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.\n\n\\item \\textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.\n\n\\item \\textbf{Factorial interaction tests.} Within-dataset count $\\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms bounded association ($p_{\\text{TOST}} = 0.003$ at $\\pm 3$\\,pp, interaction = 0.47\\,pp; Appendix~\\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity. The TOST equivalence test is estimated from BCS-controlled batches (counts 4--40) where BCS variation is sufficient; generalization to broader count ranges requires additional controlled experiments.\n\n\\item \\textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions. For Few-NERD, SCS is computed from the extraction model's own embeddings (Qwen3), creating a shared-representation dependency. MiniLM cross-check yields a conservative but directionally consistent estimate ($r = 0.172$ vs $r = 0.138$; confusion matrix correlation 0.894), suggesting the effect is not an artifact of shared representations.\n\n\\item \\textbf{NER evaluation metric.} Our exact-match NER evaluation conflates boundary errors (partial span overlap) with type errors (correct span, wrong label). Relaxed matching may yield different confusability effect sizes, as boundary ambiguity may correlate with schema complexity independently of type similarity.\n\n\\item \\textbf{RE format specificity.} RE's clean dimension separation may reflect its closed-set classification format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction.\n\n\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. The controlled stratification provides evidence consistent with a directional relationship but does not establish interventional causality.\n\n\\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\\%$\\to$50.4\\%) cannot be explained by uniform contamination, which would elevate all conditions equally. BCS slope consistency across independent and within-pool conditions (permutation $p = 0.60$) provides a robustness check that is difficult to reconcile with non-uniform contamination, which would differentially affect specific type subsets. DocRED (2019) provides a lower-contamination-risk replication with consistent BCS--accuracy slopes ($R^2 = 0.53$). Adding train-origin ratio as a covariate leaves the BCS partial effect unchanged ($p = 0.245$ for origin; Appendix~\\ref{app:split-origin}).\n\\end{enumerate}\n\n\\paragraph{Multiple comparisons.} Cross-dataset comparisons (FewRel, DocRED, Few-NERD, MAVEN) serve as independent replications of the same hypothesis and do not require family-wise correction \\citep{rothman-1990}. Within-dataset secondary analyses (e.g., quartile comparisons, slope sensitivity checks) involve multiple looks at the same data; we report individual $p$-values and note that core claims rest on effects reaching $p < 0.001$ \\citep{dror-2018-significance}.\n\n\\input{checklist}\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$), supporting bounded association between count and confusability effects.\n\nA $2 \\times 2$ factorial sensitivity check on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set the $\\pm 3$\\,pp margin based on three converging anchors. \\emph{Empirical}: typical random-batch confusability variation produces 2--5\\,pp accuracy differences (batch SD $\\approx 4.6$\\,pp at count 32). \\emph{Practical}: a ${<}3$\\,pp accuracy difference falls below deployment-relevant thresholds. \\emph{Statistical}: 3\\,pp $\\approx 0.5 \\times$ batch SD, equivalent to Cohen's $d \\approx 0.5$ (medium effect threshold; \\citealt{lakens-2017-equivalence}). A 3\\,pp interaction atop the 2.2\\,pp confusability main effect would represent ${>}130\\%$ amplification, fundamentally changing whether confusability warrants mitigation. At $\\pm 2$\\,pp (marginally equivalent, $p = 0.047$), interaction remains bounded below the main effect itself.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$), confirming that the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\end{table}\n\n\\paragraph{Logit-scale sensitivity.}\nBecause accuracy near 50\\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\\pm 3$\\,pp margin ($\\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\\,pp, still within the $\\pm 3$\\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nSee Table~\\ref{tab:batch_composition} and the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\\text{BCS}, \\text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \\leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \\citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates no systematic benefit from including definitions.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, making name-only SCS a direct match to model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ [95\\% CI: 0.001--0.151], well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\section{BCS Independence from Type Composition}\n\\label{app:bcs-composition}\n\nFewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\\% of explained variance), composition unique $R^2 = 0.298$ (42.3\\%), and shared $R^2 = 0.147$ (20.9\\%). The near-orthogonality of predictors (VIF${}\\,=\\,1.06$, $r(\\text{BCS}, \\text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than proxying for type difficulty.\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, reflecting the 64/80 base rate).  We fit:\n\\[\n\\text{accuracy} = \\beta_0 + \\beta_{\\text{BCS}} \\cdot \\text{BCS} + \\beta_{\\text{origin}} \\cdot \\text{train\\_origin\\_ratio} + \\varepsilon\n\\]\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 10^{-16}$ (vs.\\ $\\beta = -0.412$, $p < 10^{-16}$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\nPairwise SCS distributions do not differ significantly between train-origin (64 types, mean\\,=\\,0.880) and val-origin (16 types, mean\\,=\\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$), confirming that the train/val split does not introduce systematic confusability bias.\n\n\\section{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition on FewRel (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\end{table}\n\nIntra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$), confirming that random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\\,=\\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\\,pp, likely attributable to FP8 quantization non-determinism).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}\n\\label{sec:appendix_cross_model_70b}\n\nTo test whether the two-dimensional degradation pattern generalizes across model families, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\\S\\ref{sec:count_curves}, \\S\\ref{sec:bcs_controlled}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{LLaMA-70B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{RE (FewRel, Classification Accuracy)}} \\\\\n8  & 0.757 & 0.805 \\\\\n16 & 0.685 & 0.719 \\\\\n32 & 0.601 & 0.652 \\\\\n64 & 0.504 & 0.539 \\\\\n80 & 0.450 & 0.504 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{NER (Few-NERD, Text+Type Match Recall)}} \\\\\n2  & 0.323 & 0.515 \\\\\n6  & 0.300 & 0.399 \\\\\n12 & 0.278 & 0.318 \\\\\n22 & 0.252 & 0.279 \\\\\n44 & 0.297 & 0.309 \\\\\n66 & 0.273 & 0.407 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count curves for LLaMA-3.1-70B-Instruct (FP8) and Qwen3-32B. RE decline (count 8$\\to$80): $-$30.7\\,pp (70B) vs.\\ $-$30.1\\,pp (32B). NER decline (count 2$\\to$22): $-$7.1\\,pp (70B) vs.\\ $-$23.6\\,pp (32B); both models exhibit a U-shaped rebound at higher counts. 25 batches per count level, same samples and batch compositions across models (seed 42). All metrics are micro-averaged across batches.}\n\\label{tab:cross_model_70b}\n\\end{table}\n\nTable~\\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\\,pp (70B) versus $-$30.1\\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-driven decline) is directionally consistent across architectures for RE.\n\nOn NER, the count-driven decline direction is consistent across models: both 70B and Qwen3 show a recall decline from count 2 to count 22 (70B: 0.323$\\to$0.252, $-$7.1\\,pp; Qwen3: 0.515$\\to$0.279, $-$23.6\\,pp). Both models also exhibit a U-shaped rebound at higher counts (70B: 0.252 at count 22 $\\to$ 0.297 at count 44; Qwen3: 0.279 at count 22 $\\to$ 0.407 at count 66), which cross-validates the U-shape phenomenon. The magnitude difference reflects a precision-recall tradeoff: 70B operates more conservatively (higher precision, lower recall), while Qwen3 over-predicts (higher recall, lower precision, especially at low counts).\n\nFor the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\\Delta = +10.9$\\,pp, 95\\% CI: [$+$3.0, $+$20.1]). The confidence interval excludes zero, confirming the confusability effect at the 70B scale.\n\nIn summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-driven decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.\n\n\\section{Few-Shot Prompting and Confusability}\n\\label{sec:appendix_fewshot_bcs}\n\nTo test whether in-context demonstrations mitigate the BCS-driven confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \\S\\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\\approx 0.36$; 25 high-BCS, mean $\\approx 0.80$), drawn from the pre-constructed batch pool of \\S\\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Condition} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\\\\n1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\\\\n5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\\,pp over 0-shot) but provide no benefit on high-BCS batches ($-$1.0 to +5.6\\,pp). The confusability gap widens from +18.5\\,pp (0-shot) to +22.8\\,pp (5-shot). All metrics are micro-averaged across batches.}\n\\label{tab:fewshot_bcs}\n\\end{table}\n\nDemonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide negligible benefit: the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\\,pp from 0-shot to 5-shot), with all three confidence intervals excluding zero. This indicates that BCS-driven type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering.\n\nThe 0-shot gap (+18.5\\,pp) is smaller than the extreme-batch gap reported in \\S\\ref{sec:bcs_controlled} (+25.5\\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.\n\n\\end{document}\n",
      "numLines": 536,
      "startLine": 1,
      "totalLines": 536
    }
  },
  "sourceToolAssistantUUID": "db6e4808-8f7f-4204-ba4e-ec49911fbe1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T14:14:39.230Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WtiwNbmg64EAWpZkk1XTdz`</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "literature_map.yaml",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59f071ac-265a-43ac-9a7d-b6072844ea39",
  "isSidechain": false,
  "requestId": "req_011Cb8HE6jHEwdn92jDgtZd2",
  "type": "assistant",
  "uuid": "ad924de1-2d11-4f6d-a4d0-cfedeb8d1f5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8UrPYUfX54aGrJJycweSt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2224,
      "cache_read_input_tokens": 33360,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2224,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 404,
          "cache_read_input_tokens": 33360,
          "cache_creation_input_tokens": 2224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2224
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

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: schema-dag-extraction - 论文路径: projects/schema-dag-extraction/docs/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: Main Conference - 截止日期: 2026-05-25  请 `Read /home/ubun…",
  "leafUuid": "ad924de1-2d11-4f6d-a4d0-cfedeb8d1f5e",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Review schema-dag-extraction paper for EMNLP 2026",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a"
}
```

---

### Tool result

_source line 28 · 2026-05-17T14:14:45.716Z_

<details><summary>↩ Tool result · `toolu_017WDvNjGqn9Zp8q73pR9tdU`</summary>

```text
Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"}]

I found relevant information about EMNLP 2026 call for papers and submission guidelines related to ARR. Here's what I found:

## EMNLP 2026 Call for Papers - Key Guidelines

**Paper Types and Scope:**
EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

**ARR Submission Process:**
For the ARR 2026 May submission cycle aligned with EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026. Dual submissions are not allowed!

**Review and Commitment:**
Authors commit their reviewed articles to EMNLP 2026, where Senior Area Chairs and Program Chairs make acceptance decisions from ARR reviews and meta-reviews. After a paper has been fully reviewed, authors have the option to commit their paper to a conference, or revise and resubmit for another round of reviews. The reviewing process will continue to be double-blind, and reviewers will not see authors, nor will authors see reviewers and reviews.

**Authorship and Final Submissions:**
During the commitment phase, it is not allowed to modify the author list, though modification of author order is possible. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

**Presentation Requirements:**
All accepted papers must be presented at the conference to appear in the proceedings, and the conference will include both in-person and virtual presentation options.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cb1385c-2c71-4d4b-a280-c18ea86b3b7e",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "91ff7b97-c442-4f11-b3af-560fdbb605bf",
  "toolUseResult": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JouMwzLtW25MVMLQC4yX1M",
        "content": [
          {
            "title": "Call for Main Conference Papers - EMNLP 2026",
            "url": "https://2026.emnlp.org/calls/main_conference_papers/"
          },
          {
            "title": "5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"
          },
          {
            "title": "*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"
          },
          {
            "title": "EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"
          },
          {
            "title": "Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"
          },
          {
            "title": "Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"
          },
          {
            "title": "EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview",
            "url": "https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"
          },
          {
            "title": "Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"
          },
          {
            "title": "[EMNLP 2025] First Call for Papers | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"
          },
          {
            "title": "Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"
          }
        ]
      },
      "I found relevant information about EMNLP 2026 call for papers and submission guidelines related to ARR. Here's what I found:\n\n## EMNLP 2026 Call for Papers - Key Guidelines\n\n**Paper Types and Scope:**\nEMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.\n\n**ARR Submission Process:**\nFor the ARR 2026 May submission cycle aligned with EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026. Dual submissions are not allowed!\n\n**Review and Commitment:**\nAuthors commit their reviewed articles to EMNLP 2026, where Senior Area Chairs and Program Chairs make acceptance decisions from ARR reviews and meta-reviews. After a paper has been fully reviewed, authors have the option to commit their paper to a conference, or revise and resubmit for another round of reviews. The reviewing process will continue to be double-blind, and reviewers will not see authors, nor will authors see reviewers and reviews.\n\n**Authorship and Final Submissions:**\nDuring the commitment phase, it is not allowed to modify the author list, though modification of author order is possible. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.\n\n**Presentation Requirements:**\nAll accepted papers must be presented at the conference to appear in the proceedings, and the conference will include both in-person and virtual presentation options."
    ],
    "durationSeconds": 8.732387115000002
  },
  "sourceToolAssistantUUID": "1cb1385c-2c71-4d4b-a280-c18ea86b3b7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-17T14:14:45.736Z_

<details><summary>↩ Tool result · `toolu_01WtiwNbmg64EAWpZkk1XTdz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml\", \"content\": \"# Literature Map for schema-dag-extraction\\n# Updated: 2026-05-15\\n# Paper: Multi-channel Degradation Model + SDGD Framework for Training-free LLM IE\\n\\n# =============================================================================\\n# DIRECT COMPETITORS — schema decomposition for LLM-based IE\\n# =============================================================================\\n\\n- id: llm-pee-2025\\n  title: \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\"\\n  year: 2025\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2503.02628\\n  role: direct-competitor\\n  relevance_note: >\\n    Similarity-based type recall + type-partitioning prompting for massive event types.\\n    Divides candidate types into partitions to reduce prompt length.\\n    +5.4% event detection, +6.1% argument extraction, +12.9% F1 over mainstream LLMs zero-shot.\\n    KEY DIFF: partitions by similarity-based recall, NOT confusability-aware.\\n    Our DAG decomposition is confusability-driven, not just similarity-driven.\\n\\n- id: parse-2025\\n  title: \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\"\\n  authors: [Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla]\\n  year: 2025\\n  venue: EMNLP 2025 Industry\\n  url: https://arxiv.org/abs/2510.08623\\n  role: direct-competitor\\n  relevance_note: >\\n    ARCHITECT autonomously rewrites JSON schemas for LLM consumption.\\n    SCOPE uses reflection-based extraction with guardrails. +64.7% on SWDE.\\n    Treats schema optimization as black-box LLM rewriting, not principled decomposition.\\n    Does NOT model type confusability explicitly.\\n\\n- id: dee-2024\\n  title: \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\"\\n  year: 2024\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2406.01045\\n  role: direct-competitor\\n  relevance_note: >\\n    Decomposes event extraction into detection + argument extraction.\\n    Dynamic schema-aware RAG for augmented prompts.\\n    KEY DIFF: task-level decomposition (detection vs argument), not schema-level type decomposition.\\n\\n- id: crossagentie-2025\\n  title: \\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot IE\\\"\\n  authors: [Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang]\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://aclanthology.org/2025.findings-acl.718/\\n  role: direct-competitor\\n  relevance_note: >\\n    Multi-agent: intra-group cross-type debate (resolves entity-label conflicts)\\n    + inter-group cross-task debate (NER↔RE mutual refinement).\\n    ⚠️ MODERATE NOVELTY CONCERN: cross-type debate explicitly addresses type confusion.\\n    KEY DIFF: reactive debate to resolve confusion post-hoc vs our proactive decomposition to prevent it.\\n    Must clearly differentiate in paper.\\n\\n- id: dlisc-2025\\n  title: \\\"Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs\\\"\\n  year: 2025\\n  venue: arXiv (May 2025)\\n  url: https://arxiv.org/abs/2505.14992\\n  role: direct-competitor\\n  relevance_note: >\\n    Dual-LoRA with Incremental Schema Caching.\\n    Identification LoRA retrieves relevant schemas, Extraction LoRA performs IE.\\n    Focus on efficiency for on-device LLMs, not confusability analysis.\\n\\n- id: spt-2025\\n  title: \\\"Schema as Parameterized Tools for Universal Information Extraction\\\"\\n  year: 2025\\n  venue: arXiv (June 2025)\\n  url: https://arxiv.org/abs/2506.01276\\n  role: direct-competitor\\n  relevance_note: >\\n    Treats schemas as parameterized tools for LLM tool-calling.\\n    Schema retrieval + generation + infilling. Novel schema-LLM interface.\\n    Does not address type confusability.\\n\\n- id: zeroner-2025\\n  title: \\\"ZeroNER: Fueling Zero-Shot NER via Entity Type Descriptions\\\"\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://aclanthology.org/2025.findings-acl.805/\\n  role: direct-competitor\\n  relevance_note: >\\n    Description-driven: LLM supervision → BERT student for unseen types.\\n    +16% F1 over LLMs on hard zero-shot. Leverages type descriptions.\\n    Related to how schema semantics affect extraction quality.\\n\\n- id: cmas-ner-2025\\n  title: \\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\"\\n  year: 2025\\n  venue: TheWebConf 2025\\n  url: https://dl.acm.org/doi/10.1145/3696410.3714923\\n  role: direct-competitor\\n  relevance_note: >\\n    Multi-agent collective intelligence for zero-shot NER.\\n    Addresses context correlation and indiscriminate demonstration problems.\\n    Outperforms on 6 benchmarks including domain-specific and general-domain.\\n\\n# =============================================================================\\n# METHOD COMPONENTS — techniques we build upon or relate to\\n# =============================================================================\\n\\n- id: uniner-2024\\n  title: \\\"UniversalNER: Targeted Distillation from Large Language Models for Open NER\\\"\\n  authors: [Wenxuan Zhou et al.]\\n  year: 2024\\n  venue: ICLR 2024\\n  url: https://arxiv.org/abs/2308.03279\\n  role: method-component\\n  relevance_note: >\\n    Instruction-tuning on ChatGPT-generated NER data. 43 datasets, 9 domains, 13K+ types.\\n    UniNER-7B outperforms ChatGPT by 7 F1 points.\\n    Important baseline for universal NER and schema-at-scale challenges.\\n\\n- id: gollie-2024\\n  title: \\\"GoLLIE: Annotation Guidelines Following Large Language Model for Information Extraction\\\"\\n  authors: [Oscar Sainz et al.]\\n  year: 2024\\n  venue: ICLR 2024\\n  url: https://hitz-zentroa.github.io/GoLLIE/\\n  role: method-component\\n  relevance_note: >\\n    Code-style schema definitions + annotation guideline following.\\n    Strong zero-shot on unseen IE tasks. Code-Llama based.\\n    Baseline for guideline-driven schema representation.\\n\\n- id: gliner-2024\\n  title: \\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\"\\n  authors: [Urchade Zaratiana et al.]\\n  year: 2024\\n  venue: NAACL 2024\\n  url: https://arxiv.org/abs/2311.08526\\n  role: method-component\\n  relevance_note: >\\n    Compact bidirectional encoder for zero-shot NER with parallel extraction.\\n    Outperforms InstructUIE and larger models. Non-LLM competitive baseline.\\n\\n- id: gliner2-2025\\n  title: \\\"GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface\\\"\\n  authors: [Urchade Zaratiana et al.]\\n  year: 2025\\n  venue: EMNLP 2025 Demo\\n  url: https://arxiv.org/abs/2507.18546\\n  role: method-component\\n  relevance_note: >\\n    Extends GLiNER to multi-task IE (NER+RE+classification). 205M params, CPU-efficient.\\n    Schema-driven interface. Shows schema approach scales to multi-task.\\n\\n- id: kggen-2025\\n  title: \\\"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\\\"\\n  authors: [Mo et al.]\\n  year: 2025\\n  venue: NeurIPS 2025\\n  url: https://arxiv.org/abs/2502.09956\\n  role: method-component\\n  relevance_note: >\\n    Two-stage decomposition: entities first, then relations.\\n    Entity clustering/deduplication to reduce graph sparsity.\\n    Schema decomposition approach for KG construction.\\n\\n- id: code4uie-2024\\n  title: \\\"Retrieval-Augmented Code Generation for Universal Information Extraction\\\"\\n  authors: [Yucan Guo et al.]\\n  year: 2024\\n  venue: NeurIPS 2024 Workshop\\n  url: https://arxiv.org/abs/2311.02962\\n  role: method-component\\n  relevance_note: >\\n    Python class-based schema definitions + RAG for code generation.\\n    Unified code-style schema for all IE tasks.\\n\\n- id: iepile-2024\\n  title: \\\"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\\\"\\n  authors: [Guanzheng Chen et al., ZJU NLP]\\n  year: 2024\\n  venue: ACL 2024\\n  url: https://arxiv.org/abs/2402.14710\\n  role: method-component\\n  relevance_note: >\\n    0.32B token bilingual IE corpus. Hard negative schema construction =\\n    semantically proximate schemas to train type discrimination.\\n    ⚠️ RELATED: hard negatives ≈ confusable schemas, but for TRAINING, not inference-time.\\n    Our contribution is inference-time confusability-aware decomposition (training-free).\\n\\n- id: lost-in-middle-2024\\n  title: \\\"Lost in the Middle: How Language Models Use Long Contexts\\\"\\n  authors: [Nelson F. Liu et al.]\\n  year: 2024\\n  venue: TACL 2024\\n  url: https://arxiv.org/abs/2307.03172\\n  role: method-component\\n  relevance_note: >\\n    LLMs degrade when relevant info is in middle of long contexts (U-shaped attention).\\n    Motivates schema decomposition to reduce prompt length.\\n    No IE-specific follow-up found — opportunity for us to be first to connect this to IE.\\n\\n# =============================================================================\\n# ZERO-SHOT NER / RE BASELINES\\n# =============================================================================\\n\\n- id: self-improve-ner-2024\\n  title: \\\"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\\\"\\n  year: 2024\\n  venue: NAACL 2024\\n  url: https://arxiv.org/abs/2311.08921\\n  role: background\\n  relevance_note: >\\n    Self-improving framework using LLM self-generated examples for zero-shot NER.\\n\\n- id: self-prompting-re-2024\\n  title: \\\"Unleashing the Power of LLMs in Zero-shot Relation Extraction via Self-Prompting\\\"\\n  year: 2024\\n  venue: EMNLP 2024 Findings\\n  url: https://arxiv.org/abs/2410.01154\\n  role: background\\n  relevance_note: >\\n    Three-stage self-prompting for zero-shot RE. Generates synthetic ICL samples.\\n    Training-free RE baseline.\\n\\n- id: reasoning-ner-2025\\n  title: \\\"A Reasoning Paradigm for Named Entity Recognition\\\"\\n  year: 2025\\n  venue: arXiv (Nov 2025)\\n  url: https://arxiv.org/abs/2511.11978\\n  role: background\\n  relevance_note: >\\n    CoT-based reasoning for NER. Outperforms GPT-4 by 12.3 F1 in zero-shot.\\n    Shifts NER from pattern matching to explicit reasoning. Strong zero-shot baseline.\\n\\n- id: nuner-2024\\n  title: \\\"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\\\"\\n  authors: [Sergei Bogdanov et al., NuMind]\\n  year: 2024\\n  venue: EMNLP 2024\\n  url: https://arxiv.org/abs/2402.15343\\n  role: background\\n  relevance_note: >\\n    Contrastive pre-training on LLM-annotated data. Strong few-shot NER foundation model.\\n\\n# =============================================================================\\n# EVALUATION / BENCHMARKING\\n# =============================================================================\\n\\n- id: familiarity-2025\\n  title: \\\"Familiarity: Better Evaluation of Zero-Shot NER by Quantifying Label Shifts in Synthetic Training Data\\\"\\n  year: 2025\\n  venue: NAACL 2025\\n  url: https://arxiv.org/abs/2412.10121\\n  role: evaluation\\n  relevance_note: >\\n    \\\"Familiarity\\\" metric for label shift in synthetic NER data.\\n    Zero-shot NER scores overestimated due to train-eval label overlap.\\n    Quantifies semantic similarity between entity types — related to type confusability.\\n    KEY DIFF: measures evaluation bias, not extraction-time confusability.\\n\\n- id: guidex-2025\\n  title: \\\"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\\\"\\n  authors: [Neil Deshpande et al.]\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://arxiv.org/abs/2506.00649\\n  role: evaluation\\n  relevance_note: >\\n    Auto-generates domain-specific schemas + guidelines + synthetic labels.\\n    SOTA on 7 zero-shot NER benchmarks (+7 F1). Strong baseline.\\n\\n# =============================================================================\\n# SURVEYS\\n# =============================================================================\\n\\n- id: llm4ie-survey-2024\\n  title: \\\"Large Language Models for Generative Information Extraction: A Survey\\\"\\n  authors: [Derong Xu et al.]\\n  year: 2024\\n  venue: Frontiers of Computer Science\\n  url: https://arxiv.org/abs/2312.17617\\n  role: background\\n  relevance_note: >\\n    Comprehensive survey of LLM-based IE covering prompting, fine-tuning, benchmarks.\\n\\n- id: knowcoder-2024\\n  title: \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal IE\\\"\\n  year: 2024\\n  venue: ACL 2024\\n  url: https://arxiv.org/abs/2403.07969\\n  role: background\\n  relevance_note: >\\n    Encodes schema knowledge via code structures into LLM.\\n    Related to code-based schema representation.\\n\\n- id: slot-2025\\n  title: \\\"SLOT: Structuring the Output of Large\\n\\n... [截断: 省略 6972 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 18972, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad924de1-2d11-4f6d-a4d0-cfedeb8d1f5e",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "214588fb-df74-4728-bfcb-2a54a385b4b5",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml\\\", \\\"content\\\": \\\"# Literature Map for schema-dag-extraction\\\\n# Updated: 2026-05-15\\\\n# Paper: Multi-channel Degradation Model + SDGD Framework for Training-free LLM IE\\\\n\\\\n# =============================================================================\\\\n# DIRECT COMPETITORS — schema decomposition for LLM-based IE\\\\n# =============================================================================\\\\n\\\\n- id: llm-pee-2025\\\\n  title: \\\\\\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\\\\\"\\\\n  year: 2025\\\\n  venue: arXiv\\\\n  url: https://arxiv.org/abs/2503.02628\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Similarity-based type recall + type-partitioning prompting for massive event types.\\\\n    Divides candidate types into partitions to reduce prompt length.\\\\n    +5.4% event detection, +6.1% argument extraction, +12.9% F1 over mainstream LLMs zero-shot.\\\\n    KEY DIFF: partitions by similarity-based recall, NOT confusability-aware.\\\\n    Our DAG decomposition is confusability-driven, not just similarity-driven.\\\\n\\\\n- id: parse-2025\\\\n  title: \\\\\\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\\\\\"\\\\n  authors: [Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla]\\\\n  year: 2025\\\\n  venue: EMNLP 2025 Industry\\\\n  url: https://arxiv.org/abs/2510.08623\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    ARCHITECT autonomously rewrites JSON schemas for LLM consumption.\\\\n    SCOPE uses reflection-based extraction with guardrails. +64.7% on SWDE.\\\\n    Treats schema optimization as black-box LLM rewriting, not principled decomposition.\\\\n    Does NOT model type confusability explicitly.\\\\n\\\\n- id: dee-2024\\\\n  title: \\\\\\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\\\\\"\\\\n  year: 2024\\\\n  venue: arXiv\\\\n  url: https://arxiv.org/abs/2406.01045\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Decomposes event extraction into detection + argument extraction.\\\\n    Dynamic schema-aware RAG for augmented prompts.\\\\n    KEY DIFF: task-level decomposition (detection vs argument), not schema-level type decomposition.\\\\n\\\\n- id: crossagentie-2025\\\\n  title: \\\\\\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot IE\\\\\\\"\\\\n  authors: [Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang]\\\\n  year: 2025\\\\n  venue: ACL 2025 Findings\\\\n  url: https://aclanthology.org/2025.findings-acl.718/\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Multi-agent: intra-group cross-type debate (resolves entity-label conflicts)\\\\n    + inter-group cross-task debate (NER↔RE mutual refinement).\\\\n    ⚠️ MODERATE NOVELTY CONCERN: cross-type debate explicitly addresses type confusion.\\\\n    KEY DIFF: reactive debate to resolve confusion post-hoc vs our proactive decomposition to prevent it.\\\\n    Must clearly differentiate in paper.\\\\n\\\\n- id: dlisc-2025\\\\n  title: \\\\\\\"Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs\\\\\\\"\\\\n  year: 2025\\\\n  venue: arXiv (May 2025)\\\\n  url: https://arxiv.org/abs/2505.14992\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Dual-LoRA with Incremental Schema Caching.\\\\n    Identification LoRA retrieves relevant schemas, Extraction LoRA performs IE.\\\\n    Focus on efficiency for on-device LLMs, not confusability analysis.\\\\n\\\\n- id: spt-2025\\\\n  title: \\\\\\\"Schema as Parameterized Tools for Universal Information Extraction\\\\\\\"\\\\n  year: 2025\\\\n  venue: arXiv (June 2025)\\\\n  url: https://arxiv.org/abs/2506.01276\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Treats schemas as parameterized tools for LLM tool-calling.\\\\n    Schema retrieval + generation + infilling. Novel schema-LLM interface.\\\\n    Does not address type confusability.\\\\n\\\\n- id: zeroner-2025\\\\n  title: \\\\\\\"ZeroNER: Fueling Zero-Shot NER via Entity Type Descriptions\\\\\\\"\\\\n  year: 2025\\\\n  venue: ACL 2025 Findings\\\\n  url: https://aclanthology.org/2025.findings-acl.805/\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Description-driven: LLM supervision → BERT student for unseen types.\\\\n    +16% F1 over LLMs on hard zero-shot. Leverages type descriptions.\\\\n    Related to how schema semantics affect extraction quality.\\\\n\\\\n- id: cmas-ner-2025\\\\n  title: \\\\\\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\\\\\"\\\\n  year: 2025\\\\n  venue: TheWebConf 2025\\\\n  url: https://dl.acm.org/doi/10.1145/3696410.3714923\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Multi-agent collective intelligence for zero-shot NER.\\\\n    Addresses context correlation and indiscriminate demonstration problems.\\\\n    Outperforms on 6 benchmarks including domain-specific and general-domain.\\\\n\\\\n# =============================================================================\\\\n# METHOD COMPONENTS — techniques we build upon or relate to\\\\n# =============================================================================\\\\n\\\\n- id: uniner-2024\\\\n  title: \\\\\\\"UniversalNER: Targeted Distillation from Large Language Models for Open NER\\\\\\\"\\\\n  authors: [Wenxuan Zhou et al.]\\\\n  year: 2024\\\\n  venue: ICLR 2024\\\\n  url: https://arxiv.org/abs/2308.03279\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    Instruction-tuning on ChatGPT-generated NER data. 43 datasets, 9 domains, 13K+ types.\\\\n    UniNER-7B outperforms ChatGPT by 7 F1 points.\\\\n    Important baseline for universal NER and schema-at-scale challenges.\\\\n\\\\n- id: gollie-2024\\\\n  title: \\\\\\\"GoLLIE: Annotation Guidelines Following Large Language Model for Information Extraction\\\\\\\"\\\\n  authors: [Oscar Sainz et al.]\\\\n  year: 2024\\\\n  venue: ICLR 2024\\\\n  url: https://hitz-zentroa.github.io/GoLLIE/\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    Code-style schema definitions + annotation guideline following.\\\\n    Strong zero-shot on unseen IE tasks. Code-Llama based.\\\\n    Baseline for guideline-driven schema representation.\\\\n\\\\n- id: gliner-2024\\\\n  title: \\\\\\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\\\\\"\\\\n  authors: [Urchade Zaratiana et al.]\\\\n  year: 2024\\\\n  venue: NAACL 2024\\\\n  url: https://arxiv.org/abs/2311.08526\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    Compact bidirectional encoder for zero-shot NER with parallel extraction.\\\\n    Outperforms InstructUIE and larger models. Non-LLM competitive baseline.\\\\n\\\\n- id: gliner2-2025\\\\n  title: \\\\\\\"GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface\\\\\\\"\\\\n  authors: [Urchade Zaratiana et al.]\\\\n  year: 2025\\\\n  venue: EMNLP 2025 Demo\\\\n  url: https://arxiv.org/abs/2507.18546\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    Extends GLiNER to multi-task IE (NER+RE+classification). 205M params, CPU-efficient.\\\\n    Schema-driven interface. Shows schema approach scales to multi-task.\\\\n\\\\n- id: kggen-2025\\\\n  title: \\\\\\\"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\\\\\\\"\\\\n  authors: [Mo et al.]\\\\n  year: 2025\\\\n  venue: NeurIPS 2025\\\\n  url: https://arxiv.org/abs/2502.09956\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    Two-stage decomposition: entities first, then relations.\\\\n    Entity clustering/deduplication to reduce graph sparsity.\\\\n    Schema decomposition approach for KG construction.\\\\n\\\\n- id: code4uie-2024\\\\n  title: \\\\\\\"Retrieval-Augmented Code Generation for Universal Information Extraction\\\\\\\"\\\\n  authors: [Yucan Guo et al.]\\\\n  year: 2024\\\\n  venue: NeurIPS 2024 Workshop\\\\n  url: https://arxiv.org/abs/2311.02962\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    Python class-based schema definitions + RAG for code generation.\\\\n    Unified code-style schema for all IE tasks.\\\\n\\\\n- id: iepile-2024\\\\n  title: \\\\\\\"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\\\\\\\"\\\\n  authors: [Guanzheng Chen et al., ZJU NLP]\\\\n  year: 2024\\\\n  venue: ACL 2024\\\\n  url: https://arxiv.org/abs/2402.14710\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    0.32B token bilingual IE corpus. Hard negative schema construction =\\\\n    semantically proximate schemas to train type discrimination.\\\\n    ⚠️ RELATED: hard negatives ≈ confusable schemas, but for TRAINING, not inference-time.\\\\n    Our contribution is inference-time confusability-aware decomposition (training-free).\\\\n\\\\n- id: lost-in-middle-2024\\\\n  title: \\\\\\\"Lost in the Middle: How Language Models Use Long Contexts\\\\\\\"\\\\n  authors: [Nelson F. Liu et al.]\\\\n  year: 2024\\\\n  venue: TACL 2024\\\\n  url: https://arxiv.org/abs/2307.03172\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    LLMs degrade when relevant info is in middle of long contexts (U-shaped attention).\\\\n    Motivates schema decomposition to reduce prompt length.\\\\n    No IE-specific follow-up found — opportunity for us to be first to connect this to IE.\\\\n\\\\n# =============================================================================\\\\n# ZERO-SHOT NER / RE BASELINES\\\\n# =============================================================================\\\\n\\\\n- id: self-improve-ner-2024\\\\n  title: \\\\\\\"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\\\\\\\"\\\\n  year: 2024\\\\n  venue: NAACL 2024\\\\n  url: https://arxiv.org/abs/2311.08921\\\\n  role: background\\\\n  relevance_note: >\\\\n    Self-improving framework using LLM self-generated examples for zero-shot NER.\\\\n\\\\n- id: self-prompting-re-2024\\\\n  title: \\\\\\\"Unleashing the Power of LLMs in Zero-shot Relation Extraction via Self-Prompting\\\\\\\"\\\\n  year: 2024\\\\n  venue: EMNLP 2024 Findings\\\\n  url: https://arxiv.org/abs/2410.01154\\\\n  role: background\\\\n  relevance_note: >\\\\n    Three-stage self-prompting for zero-shot RE. Generates synthetic ICL samples.\\\\n    Training-free RE baseline.\\\\n\\\\n- id: reasoning-ner-2025\\\\n  title: \\\\\\\"A Reasoning Paradigm for Named Entity Recognition\\\\\\\"\\\\n  year: 2025\\\\n  venue: arXiv (Nov 2025)\\\\n  url: https://arxiv.org/abs/2511.11978\\\\n  role: background\\\\n  relevance_note: >\\\\n    CoT-based reasoning for NER. Outperforms GPT-4 by 12.3 F1 in zero-shot.\\\\n    Shifts NER from pattern matching to explicit reasoning. Strong zero-shot baseline.\\\\n\\\\n- id: nuner-2024\\\\n  title: \\\\\\\"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\\\\\\\"\\\\n  authors: [Sergei Bogdanov et al., NuMind]\\\\n  year: 2024\\\\n  venue: EMNLP 2024\\\\n  url: https://arxiv.org/abs/2402.15343\\\\n  role: background\\\\n  relevance_note: >\\\\n    Contrastive pre-training on LLM-annotated data. Strong few-shot NER foundation model.\\\\n\\\\n# =============================================================================\\\\n# EVALUATION / BENCHMARKING\\\\n# =============================================================================\\\\n\\\\n- id: familiarity-2025\\\\n  title: \\\\\\\"Familiarity: Better Evaluation of Zero-Shot NER by Quantifying Label Shifts in Synthetic Training Data\\\\\\\"\\\\n  year: 2025\\\\n  venue: NAACL 2025\\\\n  url: https://arxiv.org/abs/2412.10121\\\\n  role: evaluation\\\\n  relevance_note: >\\\\n    \\\\\\\"Familiarity\\\\\\\" metric for label shift in synthetic NER data.\\\\n    Zero-shot NER scores overestimated due to train-eval label overlap.\\\\n    Quantifies semantic similarity between entity types — related to type confusability.\\\\n    KEY DIFF: measures evaluation bias, not extraction-time confusability.\\\\n\\\\n- id: guidex-2025\\\\n  title: \\\\\\\"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\\\\\\\"\\\\n  authors: [Neil Deshpande et al.]\\\\n  year: 2025\\\\n  venue: ACL 2025 Findings\\\\n  url: https://arxiv.org/abs/2506.00649\\\\n  role: evaluation\\\\n  relevance_note: >\\\\n    Auto-generates domain-specific schemas + guidelines + synthetic labels.\\\\n    SOTA on 7 zero-shot NER benchmarks (+7 F1). Strong baseline.\\\\n\\\\n# =============================================================================\\\\n# SURVEYS\\\\n# =============================================================================\\\\n\\\\n- id: llm4ie-survey-2024\\\\n  title: \\\\\\\"Large Language Models for Generative Information Extraction: A Survey\\\\\\\"\\\\n  authors: [Derong Xu et al.]\\\\n  year: 2024\\\\n  venue: Frontiers of Computer Science\\\\n  url: https://arxiv.org/abs/2312.17617\\\\n  role: background\\\\n  relevance_note: >\\\\n    Comprehensive survey of LLM-based IE covering prompting, fine-tuning, benchmarks.\\\\n\\\\n- id: knowcoder-2024\\\\n  title: \\\\\\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal IE\\\\\\\"\\\\n  year: 2024\\\\n  venue: ACL 2024\\\\n  url: https://arxiv.org/abs/2403.07969\\\\n  role: background\\\\n  relevance_note: >\\\\n    Encodes schema knowledge via code structures into LLM.\\\\n    Related to code-based schema representation.\\\\n\\\\n- id: slot-2025\\\\n  title: \\\\\\\"SLOT: Structuring the Output of Large\\\\n\\\\n... [截断: 省略 6972 字符，传 max_chars=0 获取完整内容]\\\", \\\"total_chars\\\": 18972, \\\"truncated\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml\", \"content\": \"# Literature Map for schema-dag-extraction\\n# Updated: 2026-05-15\\n# Paper: Multi-channel Degradation Model + SDGD Framework for Training-free LLM IE\\n\\n# =============================================================================\\n# DIRECT COMPETITORS — schema decomposition for LLM-based IE\\n# =============================================================================\\n\\n- id: llm-pee-2025\\n  title: \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\"\\n  year: 2025\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2503.02628\\n  role: direct-competitor\\n  relevance_note: >\\n    Similarity-based type recall + type-partitioning prompting for massive event types.\\n    Divides candidate types into partitions to reduce prompt length.\\n    +5.4% event detection, +6.1% argument extraction, +12.9% F1 over mainstream LLMs zero-shot.\\n    KEY DIFF: partitions by similarity-based recall, NOT confusability-aware.\\n    Our DAG decomposition is confusability-driven, not just similarity-driven.\\n\\n- id: parse-2025\\n  title: \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\"\\n  authors: [Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla]\\n  year: 2025\\n  venue: EMNLP 2025 Industry\\n  url: https://arxiv.org/abs/2510.08623\\n  role: direct-competitor\\n  relevance_note: >\\n    ARCHITECT autonomously rewrites JSON schemas for LLM consumption.\\n    SCOPE uses reflection-based extraction with guardrails. +64.7% on SWDE.\\n    Treats schema optimization as black-box LLM rewriting, not principled decomposition.\\n    Does NOT model type confusability explicitly.\\n\\n- id: dee-2024\\n  title: \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\"\\n  year: 2024\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2406.01045\\n  role: direct-competitor\\n  relevance_note: >\\n    Decomposes event extraction into detection + argument extraction.\\n    Dynamic schema-aware RAG for augmented prompts.\\n    KEY DIFF: task-level decomposition (detection vs argument), not schema-level type decomposition.\\n\\n- id: crossagentie-2025\\n  title: \\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot IE\\\"\\n  authors: [Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang]\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://aclanthology.org/2025.findings-acl.718/\\n  role: direct-competitor\\n  relevance_note: >\\n    Multi-agent: intra-group cross-type debate (resolves entity-label conflicts)\\n    + inter-group cross-task debate (NER↔RE mutual refinement).\\n    ⚠️ MODERATE NOVELTY CONCERN: cross-type debate explicitly addresses type confusion.\\n    KEY DIFF: reactive debate to resolve confusion post-hoc vs our proactive decomposition to prevent it.\\n    Must clearly differentiate in paper.\\n\\n- id: dlisc-2025\\n  title: \\\"Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs\\\"\\n  year: 2025\\n  venue: arXiv (May 2025)\\n  url: https://arxiv.org/abs/2505.14992\\n  role: direct-competitor\\n  relevance_note: >\\n    Dual-LoRA with Incremental Schema Caching.\\n    Identification LoRA retrieves relevant schemas, Extraction LoRA performs IE.\\n    Focus on efficiency for on-device LLMs, not confusability analysis.\\n\\n- id: spt-2025\\n  title: \\\"Schema as Parameterized Tools for Universal Information Extraction\\\"\\n  year: 2025\\n  venue: arXiv (June 2025)\\n  url: https://arxiv.org/abs/2506.01276\\n  role: direct-competitor\\n  relevance_note: >\\n    Treats schemas as parameterized tools for LLM tool-calling.\\n    Schema retrieval + generation + infilling. Novel schema-LLM interface.\\n    Does not address type confusability.\\n\\n- id: zeroner-2025\\n  title: \\\"ZeroNER: Fueling Zero-Shot NER via Entity Type Descriptions\\\"\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://aclanthology.org/2025.findings-acl.805/\\n  role: direct-competitor\\n  relevance_note: >\\n    Description-driven: LLM supervision → BERT student for unseen types.\\n    +16% F1 over LLMs on hard zero-shot. Leverages type descriptions.\\n    Related to how schema semantics affect extraction quality.\\n\\n- id: cmas-ner-2025\\n  title: \\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\"\\n  year: 2025\\n  venue: TheWebConf 2025\\n  url: https://dl.acm.org/doi/10.1145/3696410.3714923\\n  role: direct-competitor\\n  relevance_note: >\\n    Multi-agent collective intelligence for zero-shot NER.\\n    Addresses context correlation and indiscriminate demonstration problems.\\n    Outperforms on 6 benchmarks including domain-specific and general-domain.\\n\\n# =============================================================================\\n# METHOD COMPONENTS — techniques we build upon or relate to\\n# =============================================================================\\n\\n- id: uniner-2024\\n  title: \\\"UniversalNER: Targeted Distillation from Large Language Models for Open NER\\\"\\n  authors: [Wenxuan Zhou et al.]\\n  year: 2024\\n  venue: ICLR 2024\\n  url: https://arxiv.org/abs/2308.03279\\n  role: method-component\\n  relevance_note: >\\n    Instruction-tuning on ChatGPT-generated NER data. 43 datasets, 9 domains, 13K+ types.\\n    UniNER-7B outperforms ChatGPT by 7 F1 points.\\n    Important baseline for universal NER and schema-at-scale challenges.\\n\\n- id: gollie-2024\\n  title: \\\"GoLLIE: Annotation Guidelines Following Large Language Model for Information Extraction\\\"\\n  authors: [Oscar Sainz et al.]\\n  year: 2024\\n  venue: ICLR 2024\\n  url: https://hitz-zentroa.github.io/GoLLIE/\\n  role: method-component\\n  relevance_note: >\\n    Code-style schema definitions + annotation guideline following.\\n    Strong zero-shot on unseen IE tasks. Code-Llama based.\\n    Baseline for guideline-driven schema representation.\\n\\n- id: gliner-2024\\n  title: \\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\"\\n  authors: [Urchade Zaratiana et al.]\\n  year: 2024\\n  venue: NAACL 2024\\n  url: https://arxiv.org/abs/2311.08526\\n  role: method-component\\n  relevance_note: >\\n    Compact bidirectional encoder for zero-shot NER with parallel extraction.\\n    Outperforms InstructUIE and larger models. Non-LLM competitive baseline.\\n\\n- id: gliner2-2025\\n  title: \\\"GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface\\\"\\n  authors: [Urchade Zaratiana et al.]\\n  year: 2025\\n  venue: EMNLP 2025 Demo\\n  url: https://arxiv.org/abs/2507.18546\\n  role: method-component\\n  relevance_note: >\\n    Extends GLiNER to multi-task IE (NER+RE+classification). 205M params, CPU-efficient.\\n    Schema-driven interface. Shows schema approach scales to multi-task.\\n\\n- id: kggen-2025\\n  title: \\\"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\\\"\\n  authors: [Mo et al.]\\n  year: 2025\\n  venue: NeurIPS 2025\\n  url: https://arxiv.org/abs/2502.09956\\n  role: method-component\\n  relevance_note: >\\n    Two-stage decomposition: entities first, then relations.\\n    Entity clustering/deduplication to reduce graph sparsity.\\n    Schema decomposition approach for KG construction.\\n\\n- id: code4uie-2024\\n  title: \\\"Retrieval-Augmented Code Generation for Universal Information Extraction\\\"\\n  authors: [Yucan Guo et al.]\\n  year: 2024\\n  venue: NeurIPS 2024 Workshop\\n  url: https://arxiv.org/abs/2311.02962\\n  role: method-component\\n  relevance_note: >\\n    Python class-based schema definitions + RAG for code generation.\\n    Unified code-style schema for all IE tasks.\\n\\n- id: iepile-2024\\n  title: \\\"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\\\"\\n  authors: [Guanzheng Chen et al., ZJU NLP]\\n  year: 2024\\n  venue: ACL 2024\\n  url: https://arxiv.org/abs/2402.14710\\n  role: method-component\\n  relevance_note: >\\n    0.32B token bilingual IE corpus. Hard negative schema construction =\\n    semantically proximate schemas to train type discrimination.\\n    ⚠️ RELATED: hard negatives ≈ confusable schemas, but for TRAINING, not inference-time.\\n    Our contribution is inference-time confusability-aware decomposition (training-free).\\n\\n- id: lost-in-middle-2024\\n  title: \\\"Lost in the Middle: How Language Models Use Long Contexts\\\"\\n  authors: [Nelson F. Liu et al.]\\n  year: 2024\\n  venue: TACL 2024\\n  url: https://arxiv.org/abs/2307.03172\\n  role: method-component\\n  relevance_note: >\\n    LLMs degrade when relevant info is in middle of long contexts (U-shaped attention).\\n    Motivates schema decomposition to reduce prompt length.\\n    No IE-specific follow-up found — opportunity for us to be first to connect this to IE.\\n\\n# =============================================================================\\n# ZERO-SHOT NER / RE BASELINES\\n# =============================================================================\\n\\n- id: self-improve-ner-2024\\n  title: \\\"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\\\"\\n  year: 2024\\n  venue: NAACL 2024\\n  url: https://arxiv.org/abs/2311.08921\\n  role: background\\n  relevance_note: >\\n    Self-improving framework using LLM self-generated examples for zero-shot NER.\\n\\n- id: self-prompting-re-2024\\n  title: \\\"Unleashing the Power of LLMs in Zero-shot Relation Extraction via Self-Prompting\\\"\\n  year: 2024\\n  venue: EMNLP 2024 Findings\\n  url: https://arxiv.org/abs/2410.01154\\n  role: background\\n  relevance_note: >\\n    Three-stage self-prompting for zero-shot RE. Generates synthetic ICL samples.\\n    Training-free RE baseline.\\n\\n- id: reasoning-ner-2025\\n  title: \\\"A Reasoning Paradigm for Named Entity Recognition\\\"\\n  year: 2025\\n  venue: arXiv (Nov 2025)\\n  url: https://arxiv.org/abs/2511.11978\\n  role: background\\n  relevance_note: >\\n    CoT-based reasoning for NER. Outperforms GPT-4 by 12.3 F1 in zero-shot.\\n    Shifts NER from pattern matching to explicit reasoning. Strong zero-shot baseline.\\n\\n- id: nuner-2024\\n  title: \\\"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\\\"\\n  authors: [Sergei Bogdanov et al., NuMind]\\n  year: 2024\\n  venue: EMNLP 2024\\n  url: https://arxiv.org/abs/2402.15343\\n  role: background\\n  relevance_note: >\\n    Contrastive pre-training on LLM-annotated data. Strong few-shot NER foundation model.\\n\\n# =============================================================================\\n# EVALUATION / BENCHMARKING\\n# =============================================================================\\n\\n- id: familiarity-2025\\n  title: \\\"Familiarity: Better Evaluation of Zero-Shot NER by Quantifying Label Shifts in Synthetic Training Data\\\"\\n  year: 2025\\n  venue: NAACL 2025\\n  url: https://arxiv.org/abs/2412.10121\\n  role: evaluation\\n  relevance_note: >\\n    \\\"Familiarity\\\" metric for label shift in synthetic NER data.\\n    Zero-shot NER scores overestimated due to train-eval label overlap.\\n    Quantifies semantic similarity between entity types — related to type confusability.\\n    KEY DIFF: measures evaluation bias, not extraction-time confusability.\\n\\n- id: guidex-2025\\n  title: \\\"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\\\"\\n  authors: [Neil Deshpande et al.]\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://arxiv.org/abs/2506.00649\\n  role: evaluation\\n  relevance_note: >\\n    Auto-generates domain-specific schemas + guidelines + synthetic labels.\\n    SOTA on 7 zero-shot NER benchmarks (+7 F1). Strong baseline.\\n\\n# =============================================================================\\n# SURVEYS\\n# =============================================================================\\n\\n- id: llm4ie-survey-2024\\n  title: \\\"Large Language Models for Generative Information Extraction: A Survey\\\"\\n  authors: [Derong Xu et al.]\\n  year: 2024\\n  venue: Frontiers of Computer Science\\n  url: https://arxiv.org/abs/2312.17617\\n  role: background\\n  relevance_note: >\\n    Comprehensive survey of LLM-based IE covering prompting, fine-tuning, benchmarks.\\n\\n- id: knowcoder-2024\\n  title: \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal IE\\\"\\n  year: 2024\\n  venue: ACL 2024\\n  url: https://arxiv.org/abs/2403.07969\\n  role: background\\n  relevance_note: >\\n    Encodes schema knowledge via code structures into LLM.\\n    Related to code-based schema representation.\\n\\n- id: slot-2025\\n  title: \\\"SLOT: Structuring the Output of Large\\n\\n... [截断: 省略 6972 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 18972, \"truncated\": true}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "ad924de1-2d11-4f6d-a4d0-cfedeb8d1f5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: schema-dag-extraction - 论文路径: projects/schema-dag-extraction/docs/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: Main Conference - 截止日期: 2026-05-25  请 `Read /home/ubun…",
  "leafUuid": "214588fb-df74-4728-bfcb-2a54a385b4b5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Review schema-dag-extraction paper for EMNLP 2026",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a"
}
```

---

### Assistant

_source line 32 · 2026-05-17T14:14:55.163Z_

<details><summary>Logged reasoning block</summary>

```text
I have the project overview, the main.tex file (which includes several input files), and the literature map. Now I need to:

1. Read the individual sections of the paper (abstract, introduction, related_work, experimental_setup, results, sdgd_negative, discussion, checklist, prompt_appendix)
2. Search for EMNLP 2026 venue requirements (the web search returned the CFP page)
3. Check for existing review_issues.yaml
4. Check external review config

Let me read the paper sections and do additional web search for more specific EMNLP 2026 requirements. I also need to fetch the external review configuration.


I'll start by reading through the paper sections and running a more targeted search for EMNLP 2026 specifics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "214588fb-df74-4728-bfcb-2a54a385b4b5",
  "isSidechain": false,
  "requestId": "req_011Cb8HFBXHjMe8jtehPehtU",
  "type": "assistant",
  "uuid": "916af529-4163-49e8-8f8d-5a0e92d8fc04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NJw5hmfbB2mgx3NQoiT4o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22336,
      "cache_read_input_tokens": 35584,
      "output_tokens": 947,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 947,
          "cache_read_input_tokens": 35584,
          "cache_creation_input_tokens": 22336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22336
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

_source line 33 · 2026-05-17T14:14:55.719Z_

论文为多文件结构，需要读取各分节。同时搜索更详细的 EMNLP 2026 格式要求。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "916af529-4163-49e8-8f8d-5a0e92d8fc04",
  "isSidechain": false,
  "requestId": "req_011Cb8HFBXHjMe8jtehPehtU",
  "type": "assistant",
  "uuid": "40dfe651-04cb-4e75-9321-bef9b0e442e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NJw5hmfbB2mgx3NQoiT4o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22336,
      "cache_read_input_tokens": 35584,
      "output_tokens": 947,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 947,
          "cache_read_input_tokens": 35584,
          "cache_creation_input_tokens": 22336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22336
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

_source line 34 · 2026-05-17T14:14:57.236Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SBSJYLstFjnbGLYatuftjD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40dfe651-04cb-4e75-9321-bef9b0e442e5",
  "isSidechain": false,
  "requestId": "req_011Cb8HFBXHjMe8jtehPehtU",
  "type": "assistant",
  "uuid": "bfb45b2f-f6d8-4b1f-8e09-7d6e44e10c37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NJw5hmfbB2mgx3NQoiT4o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22336,
      "cache_read_input_tokens": 35584,
      "output_tokens": 947,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 947,
          "cache_read_input_tokens": 35584,
          "cache_creation_input_tokens": 22336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22336
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

_source line 35 · 2026-05-17T14:15:02.313Z_

<details><summary>↩ Tool result · `toolu_01Ls7q1CniJDx3UrEuA4iMoT`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a60cd202-829b-404b-acca-a81af6d176f3",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "668ccd58-bd53-4145-b492-c67105983013",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 30,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "a60cd202-829b-404b-acca-a81af6d176f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-17T14:14:57.246Z_

<details><summary>↩ Tool result · `toolu_01SBSJYLstFjnbGLYatuftjD`</summary>

```text
1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: having more types (count) and having semantically similar types (confusability). We present the first controlled study isolating these factors in zero-shot LLM IE, spanning NER, RE, and event detection across four datasets, and operationalize confusability via the Schema Confusability Score (SCS) and its batch-level aggregation, the Batch Confusability Score (BCS, the mean pairwise embedding similarity within a type batch). Degradation operates along two dimensions: count-related recall decline (up to $-$49\,pp for document-level RE) dominates confusability-related type substitution (${\approx}\,2.2$\,pp in typical batches); at batch level, BCS explains 22--53\% of cross-batch accuracy variance in RE but not in NER, where the signal is absent despite significant pairwise effects. Schema decomposition fails in both tasks due to merge amplification (NER) and routing failure (RE), which points to structural barriers to confusability-aware extraction.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfb45b2f-f6d8-4b1f-8e09-7d6e44e10c37",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "271e00fe-27e5-4e91-a866-df2e294f82bf",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nTraining-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: having more types (count) and having semantically similar types (confusability). We present the first controlled study isolating these factors in zero-shot LLM IE, spanning NER, RE, and event detection across four datasets, and operationalize confusability via the Schema Confusability Score (SCS) and its batch-level aggregation, the Batch Confusability Score (BCS, the mean pairwise embedding similarity within a type batch). Degradation operates along two dimensions: count-related recall decline (up to $-$49\\,pp for document-level RE) dominates confusability-related type substitution (${\\approx}\\,2.2$\\,pp in typical batches); at batch level, BCS explains 22--53\\% of cross-batch accuracy variance in RE but not in NER, where the signal is absent despite significant pairwise effects. Schema decomposition fails in both tasks due to merge amplification (NER) and routing failure (RE), which points to structural barriers to confusability-aware extraction.\n\\end{abstract}\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  },
  "sourceToolAssistantUUID": "bfb45b2f-f6d8-4b1f-8e09-7d6e44e10c37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T14:14:57.667Z_

<details open><summary>🔧 Tool call — Read · `toolu_013AxncxAFrgicActU21qF85`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "271e00fe-27e5-4e91-a866-df2e294f82bf",
  "isSidechain": false,
  "requestId": "req_011Cb8HFBXHjMe8jtehPehtU",
  "type": "assistant",
  "uuid": "8fc6cc75-b80f-4c66-b1fd-914b4816cd4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NJw5hmfbB2mgx3NQoiT4o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22336,
      "cache_read_input_tokens": 35584,
      "output_tokens": 947,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 947,
          "cache_read_input_tokens": 35584,
          "cache_creation_input_tokens": 22336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22336
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

_source line 38 · 2026-05-17T14:14:57.677Z_

<details><summary>↩ Tool result · `toolu_013AxncxAFrgicActU21qF85`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance. Anonymous review materials: \url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 49.5\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.
9	
10	We ask three questions. \textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \textbf{RQ2}: Through what modes do count and confusability each degrade performance? \textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?
11	
12	To our knowledge, we present the first controlled study isolating type confusability from type count via stratified design in zero-shot LLM IE, spanning NER, RE, and event detection (ED). We operationalize confusability via the \emph{Schema Confusability Score} (SCS), defined as pairwise embedding cosine similarity, and its batch-level aggregation, the \emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, and MAVEN \cite{maven-2020} using Qwen3-32B (\S\ref{sec:experimental_setup}).
13	
14	Our experiments yield five findings:
15	(1)~Degradation operates along two dimensions: count-related recall decline (up to $-$49\,pp for document-level RE) and confusability-related type substitution (typical-batch gap ${\approx}\,2.2$\,pp), with count as the dominant factor; the dimensions exhibit bounded association in RE (TOST $p = 0.003$ at $\pm 3$\,pp) but are coupled in NER.
16	(2)~Pairwise SCS predicts type confusion across NER, RE, and ED ($r = 0.112$--$0.129$); at batch level, BCS predicts accuracy in RE ($R^2 = 0.22$--$0.53$) but not in NER (batch-level $r \approx 0$, n.s.).
17	(3)~Effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: $R^2 = 0.53$) and directionally consistent across prompt designs.
18	(4)~Per-type aggregation is confounded by centrality on homogeneous schemas.
19	(5)~Schema decomposition fails due to merge amplification in NER; RE confusability-aware grouping yields no significant improvement over random (+1.4\,pp, $p \approx 0.19$, n.s.) despite oracle routing that recovers +29.8\,pp.
20	
21	Our contributions are:
22	\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]
23	    \item We conduct the first controlled study that isolates count and confusability effects on training-free LLM IE performance across four datasets and three tasks (\S\ref{sec:count_curves}, \S\ref{sec:bcs_controlled}).
24	    \item We validate that embedding-based confusability scores predict type substitution errors and establish an empirical link between schema similarity and extraction accuracy in RE (\S\ref{sec:scs-validation}).
25	    \item We show that count-related recall decline generalizes across tasks, while batch-level confusability effects are specific to RE; NER shows no batch-level BCS signal despite significant pairwise SCS effects (\S\ref{sec:bcs_controlled}, \S\ref{sec:multi_channel}).
26	    \item We report a negative result: schema decomposition fails due to merge amplification in NER and routing failure in RE, and we diagnose structural barriers to confusability-aware extraction (\S\ref{sec:sdgd}).
27	\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fc6cc75-b80f-4c66-b1fd-914b4816cd4b",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "d7d01d92-942a-4cc5-a612-a7b9dd1b4fef",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining-free\\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\\footnote{Code and data will be released upon acceptance. Anonymous review materials: \\url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\\% with one relation to 49.5\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level), near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.\n\nWhat explains this degradation? Prior decomposition strategies \\cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\\S\\ref{sec:related_work}).\n\nThis study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what modes do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\nTo our knowledge, we present the first controlled study isolating type confusability from type count via stratified design in zero-shot LLM IE, spanning NER, RE, and event detection (ED). We operationalize confusability via the \\emph{Schema Confusability Score} (SCS), defined as pairwise embedding cosine similarity, and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, and MAVEN \\cite{maven-2020} using Qwen3-32B (\\S\\ref{sec:experimental_setup}).\n\nOur experiments yield five findings:\n(1)~Degradation operates along two dimensions: count-related recall decline (up to $-$49\\,pp for document-level RE) and confusability-related type substitution (typical-batch gap ${\\approx}\\,2.2$\\,pp), with count as the dominant factor; the dimensions exhibit bounded association in RE (TOST $p = 0.003$ at $\\pm 3$\\,pp) but are coupled in NER.\n(2)~Pairwise SCS predicts type confusion across NER, RE, and ED ($r = 0.112$--$0.129$); at batch level, BCS predicts accuracy in RE ($R^2 = 0.22$--$0.53$) but not in NER (batch-level $r \\approx 0$, n.s.).\n(3)~Effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: $R^2 = 0.53$) and directionally consistent across prompt designs.\n(4)~Per-type aggregation is confounded by centrality on homogeneous schemas.\n(5)~Schema decomposition fails due to merge amplification in NER; RE confusability-aware grouping yields no significant improvement over random (+1.4\\,pp, $p \\approx 0.19$, n.s.) despite oracle routing that recovers +29.8\\,pp.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item We conduct the first controlled study that isolates count and confusability effects on training-free LLM IE performance across four datasets and three tasks (\\S\\ref{sec:count_curves}, \\S\\ref{sec:bcs_controlled}).\n    \\item We validate that embedding-based confusability scores predict type substitution errors and establish an empirical link between schema similarity and extraction accuracy in RE (\\S\\ref{sec:scs-validation}).\n    \\item We show that count-related recall decline generalizes across tasks, while batch-level confusability effects are specific to RE; NER shows no batch-level BCS signal despite significant pairwise SCS effects (\\S\\ref{sec:bcs_controlled}, \\S\\ref{sec:multi_channel}).\n    \\item We report a negative result: schema decomposition fails due to merge amplification in NER and routing failure in RE, and we diagnose structural barriers to confusability-aware extraction (\\S\\ref{sec:sdgd}).\n\\end{enumerate}",
      "numLines": 27,
      "startLine": 1,
      "totalLines": 27
    }
  },
  "sourceToolAssistantUUID": "8fc6cc75-b80f-4c66-b1fd-914b4816cd4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-17T14:14:58.068Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VW23wge835VCQLpt1rvDLd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7d01d92-942a-4cc5-a612-a7b9dd1b4fef",
  "isSidechain": false,
  "requestId": "req_011Cb8HFBXHjMe8jtehPehtU",
  "type": "assistant",
  "uuid": "58946bc9-470c-4738-bbe4-034c6933229f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NJw5hmfbB2mgx3NQoiT4o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22336,
      "cache_read_input_tokens": 35584,
      "output_tokens": 947,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 947,
          "cache_read_input_tokens": 35584,
          "cache_creation_input_tokens": 22336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22336
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

_source line 40 · 2026-05-17T14:14:58.073Z_

<details><summary>↩ Tool result · `toolu_01VW23wge835VCQLpt1rvDLd`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, and bidirectional encoders \cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. Recent work also explores LLM-based data annotation for NER \cite{bogdanov2024nuner,zhang2023llmaaa} and self-improving zero-shot extraction \cite{xie2024selfimproving}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. Specifically, LLM-PEE employs union merge across sub-schema extractions, which our \S\ref{sec:sdgd} analysis shows is associated with precision collapsing from 0.56 to 0.21 in NER as false positives accumulate across passes; RE avoids this because closed-set classification does not require span reconciliation, explaining why LLM-PEE's decomposition succeeds for relation/event tasks but faces unresolved merge challenges on span-level extraction. Other approaches address schema complexity via hard negative mining \cite{iepile-2024}, schema definition optimization \cite{parse-2025}, multi-agent debate \cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \cite{dee-2024}, and active prompting \cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation factors. Concurrently, \citet{haystack-to-needle-2025} reduces label spaces via iterative LLM filtering, an engineering complement to our analytical approach. Our framework explains \emph{why} such reduction works: it implicitly lowers batch confusability.
9	
10	\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\cite{rastogi2020towards} and SGD-X~\cite{lee2022sgd} document performance degradation with schema linguistic variation. \citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. \citet{volkanovska2025ner} categorize LLM NER errors including type confusion. The relationship between label similarity and classification confusion has precedent in traditional ML: hierarchical classification suffers sibling confusion proportional to inter-class proximity \citep{deng-2010-imagenet}, label confusion matrices improve text classification \citep{guo-2021-label-confusion}, and classification confusion captures semantic similarity \citep{zhou-2025-rethinking}. Hierarchical label sets reduce class confusion in zero-shot image classification \citep{novack-2023-chils}; enriched type descriptions improve zero-shot NER \citep{cocchieri-2025-zeroner}, both orthogonal to our confusability-aware batching.
11	
12	\paragraph{SCS novelty.} SCS shares its formal definition (pairwise cosine similarity of type name embeddings) with the partitioning criterion used in LLM-PEE~\cite{llm-pee-2025} for schema decomposition. Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work. The modest pairwise effect size ($r^2 = 1.3$--$1.7\%$) is consistent with standards for individual-difference predictors in behavioral research \citep{cohen-1988-power}, where such magnitudes are considered ``small but real'' effects that compound at the aggregate level \citep{lakens-2013-effect-size}.
13	
14	\paragraph{Embedding anisotropy.}
15	Our centrality confound (\S\ref{sec:centrality_confound}) connects to representation degeneration: embeddings collapse into narrow cones \cite{gao-repr-degen-2019,ethayarajh-contextual-2019}, but local clusters can be isotropic \cite{cai-isotropy-clusters-2021}, explaining why MAVEN's single-ontology types conflate confusability with centrality.
16	
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58946bc9-470c-4738-bbe4-034c6933229f",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "90ab3bbe-30cc-4589-bdeb-3b3f50001397",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Training-free LLM IE.}\nTraining-free LLM IE spans instruction tuning \\cite{instructuie-2023}, code-style schema encoding \\cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \\cite{gollie-2024,adelie-2024}, schema-driven decoding \\cite{slot-2025,oneke-2025}, and constrained JSON decoding \\cite{json-schema-bench-2025}. For NER, methods include zero-shot decomposition \\cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \\cite{uniner-2024}, and bidirectional encoders \\cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \\cite{relationprompt-2022} and revisits relation extraction in the LLM era \\cite{wadhwa-re-llm-2023}. Recent work also explores LLM-based data annotation for NER \\cite{bogdanov2024nuner,zhang2023llmaaa} and self-improving zero-shot extraction \\cite{xie2024selfimproving}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.\n\n\\paragraph{Schema complexity in IE.}\nThe most directly related work is LLM-PEE \\cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \\emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. Specifically, LLM-PEE employs union merge across sub-schema extractions, which our \\S\\ref{sec:sdgd} analysis shows is associated with precision collapsing from 0.56 to 0.21 in NER as false positives accumulate across passes; RE avoids this because closed-set classification does not require span reconciliation, explaining why LLM-PEE's decomposition succeeds for relation/event tasks but faces unresolved merge challenges on span-level extraction. Other approaches address schema complexity via hard negative mining \\cite{iepile-2024}, schema definition optimization \\cite{parse-2025}, multi-agent debate \\cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \\cite{dee-2024}, and active prompting \\cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation factors. Concurrently, \\citet{haystack-to-needle-2025} reduces label spaces via iterative LLM filtering, an engineering complement to our analytical approach. Our framework explains \\emph{why} such reduction works: it implicitly lowers batch confusability.\n\n\\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\\cite{rastogi2020towards} and SGD-X~\\cite{lee2022sgd} document performance degradation with schema linguistic variation. \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. \\citet{volkanovska2025ner} categorize LLM NER errors including type confusion. The relationship between label similarity and classification confusion has precedent in traditional ML: hierarchical classification suffers sibling confusion proportional to inter-class proximity \\citep{deng-2010-imagenet}, label confusion matrices improve text classification \\citep{guo-2021-label-confusion}, and classification confusion captures semantic similarity \\citep{zhou-2025-rethinking}. Hierarchical label sets reduce class confusion in zero-shot image classification \\citep{novack-2023-chils}; enriched type descriptions improve zero-shot NER \\citep{cocchieri-2025-zeroner}, both orthogonal to our confusability-aware batching.\n\n\\paragraph{SCS novelty.} SCS shares its formal definition (pairwise cosine similarity of type name embeddings) with the partitioning criterion used in LLM-PEE~\\cite{llm-pee-2025} for schema decomposition. Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work. The modest pairwise effect size ($r^2 = 1.3$--$1.7\\%$) is consistent with standards for individual-difference predictors in behavioral research \\citep{cohen-1988-power}, where such magnitudes are considered ``small but real'' effects that compound at the aggregate level \\citep{lakens-2013-effect-size}.\n\n\\paragraph{Embedding anisotropy.}\nOur centrality confound (\\S\\ref{sec:centrality_confound}) connects to representation degeneration: embeddings collapse into narrow cones \\cite{gao-repr-degen-2019,ethayarajh-contextual-2019}, but local clusters can be isotropic \\cite{cai-isotropy-clusters-2021}, explaining why MAVEN's single-ontology types conflate confusability with centrality.\n\n",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
    }
  },
  "sourceToolAssistantUUID": "58946bc9-470c-4738-bbe4-034c6933229f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-17T14:14:59.068Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CnQF831S622oF3SoByZ5LV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90ab3bbe-30cc-4589-bdeb-3b3f50001397",
  "isSidechain": false,
  "requestId": "req_011Cb8HFBXHjMe8jtehPehtU",
  "type": "assistant",
  "uuid": "3a66a8e6-83a3-4f12-ba65-8b7570cf8c1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NJw5hmfbB2mgx3NQoiT4o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22336,
      "cache_read_input_tokens": 35584,
      "output_tokens": 947,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 947,
          "cache_read_input_tokens": 35584,
          "cache_creation_input_tokens": 22336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22336
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

_source line 42 · 2026-05-17T14:14:59.073Z_

<details><summary>↩ Tool result · `toolu_01CnQF831S622oF3SoByZ5LV`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound, making it the primary dataset for BCS analysis.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.
17	
18	\paragraph{MAVEN (ED).}
19	MAVEN \cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.
20	
21	Table~\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \S\ref{sec:scs}.
22	
23	\begin{table}[t]
24	\centering
25	\small
26	\resizebox{\columnwidth}{!}{%
27	\begin{tabular}{llrrlll}
28	\toprule
29	\textbf{Dataset} & \textbf{Task} & \textbf{\# Types} & \textbf{\# Eval Units} & \textbf{Domain} & \textbf{BCS Range} & \textbf{Embedding} \\
30	\midrule
31	Few-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\
32	FewRel & RE (sent.) & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\
33	DocRED & RE (doc.) & 96 & 1{,}000 & Cross & 0.53--0.73 & MiniLM \\
34	MAVEN & ED & 168 & 18{,}904\rlap{$^\dagger$} & Same & 0.87--0.97 & MiniLM \\
35	\bottomrule
36	\end{tabular}}
37	\caption{Dataset statistics. BCS Range indicates the min--max Batch Confusability Scores across count-curve batches (Experiment~1). Embedding column indicates the model used for SCS/BCS computation. $^\dagger$Trigger mentions across 8{,}042 sentences in 710 documents.}
38	\label{tab:datasets}
39	\end{table}
40	
41	\subsection{Schema Confusability Score (SCS)}
42	\label{sec:scs}
43	
44	We introduce the Schema Confusability Score to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\text{name}(t)$, an embedding function $\text{embed}(\cdot)$ maps the type name to a vector representation. The \textbf{pairwise SCS} between types $t_i$ and $t_j$ is:
45	{\small
46	\[
47	\text{SCS}(t_i, t_j) = \cos\bigl(\text{embed}(\text{name}(t_i)),\; \text{embed}(\text{name}(t_j))\bigr)
48	\]
49	}
50	
51	For a batch of types $B = \{t_1, \ldots, t_k\}$, the \textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:
52	\[
53	\text{BCS}(B) = \frac{1}{\binom{k}{2}} \sum_{i < j,\; t_i, t_j \in B} \text{SCS}(t_i, t_j)
54	\]
55	
56	We compute SCS with two embedding models: (1)~Qwen3-32B \cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \cite{minilm-2020,sentence-bert-2019}, a 384-dimensional general-purpose sentence encoder. Few-NERD uses Qwen3 embeddings because its 66 fine-grained types include same-category pairs (e.g., ``person-artist'' vs.\ ``person-actor'') that MiniLM's 384-d space does not separate well; a cross-embedding check confirms directional consistency (MiniLM $r = 0.172$, Qwen3 $r = 0.138$; Appendix~\ref{sec:appendix_bcs_sensitivity}). SCS uses name-only embeddings as a practical simplification. We validate this choice empirically: name+definition SCS yields equivalent predictive accuracy ($\Delta r$: $-0.023$ to $+0.035$; Appendix~\ref{app:scs-ablation}), and for MAVEN/FewRel prompts that use type names without definitions, name-only SCS directly matches prompt content. We use MiniLM as the primary embedding for BCS computation because sentence-transformers are specifically trained for semantic similarity \cite{sentence-bert-2019}; a cross-embedding sensitivity check using Qwen3-32B causal-LM hidden states confirms directional consistency but with compressed BCS range (std${}\,=\,0.034$ vs.\ MiniLM std${}\,=\,0.081$), consistent with known autoregressive anisotropy \cite{ethayarajh-contextual-2019}.
57	
58	\paragraph{SCS as a lightweight proxy.}
59	\label{sec:scs-validation}
60	SCS measures embedding-space similarity rather than task-grounded confusion, making it a pre-hoc proxy computable without running extraction experiments. Empirical validation confirms the proxy is informative: pairwise SCS correlates with observed type confusion on both NER and RE datasets (Few-NERD $r = 0.112$, FewRel $r = 0.187$, both $p < 0.001$; Table~\ref{tab:pairwise}). However, SCS is a partial proxy; context, type frequency, mention ambiguity, and definition quality also contribute to confusion (\S\ref{sec:pairwise}). Task-grounded confusion scores derived from empirical error matrices would capture these factors but require running extraction first, forfeiting the predictive utility that makes SCS useful for schema design.
61	
62	\subsection{Experimental Design}
63	\label{sec:exp_design}
64	
65	We conduct two complementary experimental paradigms.
66	
67	\paragraph{Experiment 1: Count Curves.}
68	We vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 25 random type batches for Few-NERD and FewRel (5 for DocRED and MAVEN) and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The remaining count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \{2, 6, 12, 22, 44, 66\} for Few-NERD, \{4, 8, 16, 32, 40, 64, 80\} for FewRel, \{4, 8, 16, 32, 64, 96\} for DocRED, and \{6, 12, 22, 44, 64\} for MAVEN.
69	
70	\paragraph{Experiment 2: BCS-Controlled.}
71	We fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). We evaluate on Few-NERD (count$\,\in\{6, 12\}$), FewRel (count$\,\in\{8, 16\}$, both 16-relation and 80-relation pools), and DocRED (count$\,\in\{16, 32\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\S\ref{sec:centrality_confound}).
72	
73	\subsection{Evaluation Metrics}
74	\label{sec:metrics}
75	
76	\textbf{NER}: text-match F1, where a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \emph{and} the type matches; partial spans count as incorrect. \textbf{RE}: accuracy (exact match of predicted relation label to gold). \textbf{ED}: relaxed F1, where any token overlap between predicted and gold trigger spans, with correct event type.
77	
78	
79	\subsection{Model and Inference}
80	\label{sec:model}
81	
82	We use Qwen3-32B-FP8 \cite{qwen3-2025} served via vLLM v0.20.2 \cite{vllm-2023} on a single NVIDIA RTX PRO 6000 GPU (96\,GB) with greedy decoding (temperature${}\,=\,0$, seed 42). Two NER/ED prompt versions are evaluated: v1 requests character offsets (evaluated via text matching); v2 adds format constraints, doubling precision with minimal recall loss. RE uses a single prompt version throughout. Both versions produce consistent degradation patterns; we report both where applicable to quantify formatting sensitivity \cite{sclar-sensitivity-2024} (templates in Appendix~\ref{sec:appendix_prompts}). Cross-model validation uses Meta-Llama-3.1-70B-Instruct (FP8) and Meta-Llama-3.1-8B-Instruct \cite{llama3-2024}. All experiments use single-seed evaluation with greedy decoding, which substantially reduces model-level randomness (residual SD = 0.88\,pp at count 80 under greedy decoding, likely attributable to FP8 quantization non-determinism); bootstrap CIs capture the remaining sampling variance from batch composition. Pair-level CIs use percentile bootstrap ($B{=}10{,}000$); batch-level CIs use $B{=}1{,}000$.
83	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a66a8e6-83a3-4f12-ba65-8b7570cf8c1d",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "e370f687-6302-4f6b-b86f-ac71d1ea94cb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).\n\n\\subsection{Tasks and Datasets}\n\\label{sec:datasets}\n\n\\paragraph{Few-NERD (NER).}\nFew-NERD \\cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\\binom{66}{2}=2{,}145$ possible pairs.\n\n\\paragraph{FewRel (RE).}\nFewRel \\cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound, making it the primary dataset for BCS analysis.\n\n\\paragraph{DocRED (Document-level RE).}\nDocRED \\cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.\n\n\\paragraph{MAVEN (ED).}\nMAVEN \\cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.\n\nTable~\\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \\S\\ref{sec:scs}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrlll}\n\\toprule\n\\textbf{Dataset} & \\textbf{Task} & \\textbf{\\# Types} & \\textbf{\\# Eval Units} & \\textbf{Domain} & \\textbf{BCS Range} & \\textbf{Embedding} \\\\\n\\midrule\nFew-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\\\\nFewRel & RE (sent.) & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\\\\nDocRED & RE (doc.) & 96 & 1{,}000 & Cross & 0.53--0.73 & MiniLM \\\\\nMAVEN & ED & 168 & 18{,}904\\rlap{$^\\dagger$} & Same & 0.87--0.97 & MiniLM \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Dataset statistics. BCS Range indicates the min--max Batch Confusability Scores across count-curve batches (Experiment~1). Embedding column indicates the model used for SCS/BCS computation. $^\\dagger$Trigger mentions across 8{,}042 sentences in 710 documents.}\n\\label{tab:datasets}\n\\end{table}\n\n\\subsection{Schema Confusability Score (SCS)}\n\\label{sec:scs}\n\nWe introduce the Schema Confusability Score to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\\text{name}(t)$, an embedding function $\\text{embed}(\\cdot)$ maps the type name to a vector representation. The \\textbf{pairwise SCS} between types $t_i$ and $t_j$ is:\n{\\small\n\\[\n\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\text{embed}(\\text{name}(t_i)),\\; \\text{embed}(\\text{name}(t_j))\\bigr)\n\\]\n}\n\nFor a batch of types $B = \\{t_1, \\ldots, t_k\\}$, the \\textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:\n\\[\n\\text{BCS}(B) = \\frac{1}{\\binom{k}{2}} \\sum_{i < j,\\; t_i, t_j \\in B} \\text{SCS}(t_i, t_j)\n\\]\n\nWe compute SCS with two embedding models: (1)~Qwen3-32B \\cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \\cite{minilm-2020,sentence-bert-2019}, a 384-dimensional general-purpose sentence encoder. Few-NERD uses Qwen3 embeddings because its 66 fine-grained types include same-category pairs (e.g., ``person-artist'' vs.\\ ``person-actor'') that MiniLM's 384-d space does not separate well; a cross-embedding check confirms directional consistency (MiniLM $r = 0.172$, Qwen3 $r = 0.138$; Appendix~\\ref{sec:appendix_bcs_sensitivity}). SCS uses name-only embeddings as a practical simplification. We validate this choice empirically: name+definition SCS yields equivalent predictive accuracy ($\\Delta r$: $-0.023$ to $+0.035$; Appendix~\\ref{app:scs-ablation}), and for MAVEN/FewRel prompts that use type names without definitions, name-only SCS directly matches prompt content. We use MiniLM as the primary embedding for BCS computation because sentence-transformers are specifically trained for semantic similarity \\cite{sentence-bert-2019}; a cross-embedding sensitivity check using Qwen3-32B causal-LM hidden states confirms directional consistency but with compressed BCS range (std${}\\,=\\,0.034$ vs.\\ MiniLM std${}\\,=\\,0.081$), consistent with known autoregressive anisotropy \\cite{ethayarajh-contextual-2019}.\n\n\\paragraph{SCS as a lightweight proxy.}\n\\label{sec:scs-validation}\nSCS measures embedding-space similarity rather than task-grounded confusion, making it a pre-hoc proxy computable without running extraction experiments. Empirical validation confirms the proxy is informative: pairwise SCS correlates with observed type confusion on both NER and RE datasets (Few-NERD $r = 0.112$, FewRel $r = 0.187$, both $p < 0.001$; Table~\\ref{tab:pairwise}). However, SCS is a partial proxy; context, type frequency, mention ambiguity, and definition quality also contribute to confusion (\\S\\ref{sec:pairwise}). Task-grounded confusion scores derived from empirical error matrices would capture these factors but require running extraction first, forfeiting the predictive utility that makes SCS useful for schema design.\n\n\\subsection{Experimental Design}\n\\label{sec:exp_design}\n\nWe conduct two complementary experimental paradigms.\n\n\\paragraph{Experiment 1: Count Curves.}\nWe vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 25 random type batches for Few-NERD and FewRel (5 for DocRED and MAVEN) and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The remaining count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \\{2, 6, 12, 22, 44, 66\\} for Few-NERD, \\{4, 8, 16, 32, 40, 64, 80\\} for FewRel, \\{4, 8, 16, 32, 64, 96\\} for DocRED, and \\{6, 12, 22, 44, 64\\} for MAVEN.\n\n\\paragraph{Experiment 2: BCS-Controlled.}\nWe fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). We evaluate on Few-NERD (count$\\,\\in\\{6, 12\\}$), FewRel (count$\\,\\in\\{8, 16\\}$, both 16-relation and 80-relation pools), and DocRED (count$\\,\\in\\{16, 32\\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\\S\\ref{sec:centrality_confound}).\n\n\\subsection{Evaluation Metrics}\n\\label{sec:metrics}\n\n\\textbf{NER}: text-match F1, where a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect. \\textbf{RE}: accuracy (exact match of predicted relation label to gold). \\textbf{ED}: relaxed F1, where any token overlap between predicted and gold trigger spans, with correct event type.\n\n\n\\subsection{Model and Inference}\n\\label{sec:model}\n\nWe use Qwen3-32B-FP8 \\cite{qwen3-2025} served via vLLM v0.20.2 \\cite{vllm-2023} on a single NVIDIA RTX PRO 6000 GPU (96\\,GB) with greedy decoding (temperature${}\\,=\\,0$, seed 42). Two NER/ED prompt versions are evaluated: v1 requests character offsets (evaluated via text matching); v2 adds format constraints, doubling precision with minimal recall loss. RE uses a single prompt version throughout. Both versions produce consistent degradation patterns; we report both where applicable to quantify formatting sensitivity \\cite{sclar-sensitivity-2024} (templates in Appendix~\\ref{sec:appendix_prompts}). Cross-model validation uses Meta-Llama-3.1-70B-Instruct (FP8) and Meta-Llama-3.1-8B-Instruct \\cite{llama3-2024}. All experiments use single-seed evaluation with greedy decoding, which substantially reduces model-level randomness (residual SD = 0.88\\,pp at count 80 under greedy decoding, likely attributable to FP8 quantization non-determinism); bootstrap CIs capture the remaining sampling variance from batch composition. Pair-level CIs use percentile bootstrap ($B{=}10{,}000$); batch-level CIs use $B{=}1{,}000$.\n",
      "numLines": 83,
      "startLine": 1,
      "totalLines": 83
    }
  },
  "sourceToolAssistantUUID": "3a66a8e6-83a3-4f12-ba65-8b7570cf8c1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-17T14:14:59.604Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FFD5nrPfjCxE39wHoTQXkN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e370f687-6302-4f6b-b86f-ac71d1ea94cb",
  "isSidechain": false,
  "requestId": "req_011Cb8HFBXHjMe8jtehPehtU",
  "type": "assistant",
  "uuid": "e6a3c840-26ee-468c-ab59-41d2b6666b97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NJw5hmfbB2mgx3NQoiT4o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22336,
      "cache_read_input_tokens": 35584,
      "output_tokens": 947,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 947,
          "cache_read_input_tokens": 35584,
          "cache_creation_input_tokens": 22336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22336
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

_source line 44 · 2026-05-17T14:14:59.610Z_

<details><summary>↩ Tool result · `toolu_01FFD5nrPfjCxE39wHoTQXkN`</summary>

```text
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
20	\caption{\textbf{(a)} Count-degradation curves for NER and RE. Error bars show $\pm 1$\,SD across 3 seeds (42, 123, 456) $\times$ 25 batches per seed. RE accuracy declines monotonically with count; NER recall exhibits a U-shaped pattern with minimum at intermediate counts. Full-schema points (rightmost, hollow markers) represent the complete type inventory with no batch sampling variance. \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}), indicating schema configuration rather than model-specific factors predicts difficulty. The pattern replicates across three seeds (42, 123, 456; max $\Delta = 10.7$\,pp, within 1\,SD); intra-batch variance exceeds inter-seed variance by ${>}$5$\times$ at every count level (Appendix~\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $J = 109{,}707$, $p < 0.001$, pooled across three seeds). Count curves (25 batches per level) establish trend direction with error bars; magnitude estimation relies on the higher-powered BCS-controlled experiments (\S\ref{sec:bcs_controlled}).
25	
26	\subsection{Pairwise Confusability and Type Confusion}
27	\label{sec:pairwise}
28	
29	We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\% CIs.
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\resizebox{\columnwidth}{!}{%
35	\begin{tabular}{llrrrrr}
36	\toprule
37	\textbf{Dataset} & \textbf{Embed.} & \textbf{$n$ pairs} & \textbf{$r$} & \textbf{$r^2$} & \textbf{95\% CI} & \textbf{$p$} \\
38	\midrule
39	Few-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\,0.001$ \\
40	MAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\,0.001$ \\
41	\bottomrule
42	\end{tabular}}
43	\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models (both $p \ll 0.001$). Confusion rate for each ordered pair $(t_i, t_j)$ is computed as the total bidirectional confusion count $C(t_i{\to}t_j) + C(t_j{\to}t_i)$ divided by the sum of gold frequencies, aggregated over all count conditions; CIs are pair-level percentile bootstrap ($B{=}10{,}000$). FewRel ($r = 0.187$; \S\ref{sec:scs-validation}) is excluded as RE's per-instance format precludes direct comparison of confusion rates. Type-level cluster bootstrap CIs: Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]; both exclude zero, confirming robustness to within-type correlation.}
44	\label{tab:pairwise}
45	\end{table}
46	
47	The correlations are statistically significant but modest: $r^2 \approx 1.3\text{--}1.7\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Both datasets show significant positive correlations between pairwise SCS and type confusion rates. Spearman correlations corroborate: $\rho = 0.144\text{--}0.227$ across all pairs, strengthening to $\rho = 0.27\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).
48	
49	The remaining variance likely reflects entity frequency, prompt position \cite{lost-in-middle-2024}, mention ambiguity, and definition quality. Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\,pp under typical batching (\S\ref{sec:practical_magnitude}). Notably, the independent MiniLM embedding yields a \emph{stronger} SCS--confusion correlation on Few-NERD ($r = 0.172$ vs.\ Qwen3 $r = 0.138$; Appendix), suggesting that shared-representation bias is conservative rather than inflationary.
50	
51	\subsection{BCS-Controlled Experiments}
52	\label{sec:bcs_controlled}
53	
54	We fix type count and vary BCS. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound; the within-pool analysis (\S\ref{sec:within_pool}) controls for pool composition.
55	
56	In BCS-controlled FewRel subsets, the high-BCS quartile shows $\Delta=-5.3$\,pp lower accuracy than low-BCS (quartile comparison; full data in Appendix~\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\,pp (CI: [17.7, 42.7]), stable across count levels. An intermediate count${}\,=\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\,pp at count 8, $-$31.8\,pp at count 16), confirming monotonic decline.
57	
58	\paragraph{Document-level RE (DocRED).}
59	The effect replicates on DocRED's 96-relation schema: BCS gap $-$23.3\,pp at count 16 (slope $= -0.713$, $\rho = -0.661$, $p < 0.001$) and $-$17.6\,pp at count 32 (slope $= -0.690$, $\rho = -0.509$, $p = 0.002$). BCS explains 44--53\% of cross-batch variance ($R^2 = 0.525$ at count 16), substantially higher than FewRel ($R^2 = 0.218$), possibly reflecting a wider confusability range in the DocRED schema, though document-level context may also provide richer cues for type confusion. Across all RE settings, BCS slopes range from $-$0.40 to $-$0.71, significant in all conditions with sufficient BCS range.
60	
61	\paragraph{Within-pool controlled comparison.}
62	\label{sec:within_pool}
63	Within-pool analysis confirms slope consistency across pools (permutation $p \approx 0.60$; Appendix~\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\S\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.
64	
65	\paragraph{Practical magnitude.}
66	\label{sec:practical_magnitude}
67	Direct regression on 100 random 16-type batches from the 80-relation pool shows BCS explains 22\% of cross-batch accuracy variance ($R^2 = 0.218$, $p < 0.001$), scaling to 53\% at DocRED 96-rel. The typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\,pp (95\% CI: [0.4, 4.0]), roughly 7\% of the extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\% vs.\ 78.9\% for top-quartile ($\Delta = 3.9$\,pp). High mean-BCS batches contain more active confusable pairs, concentrating degradation. A post-hoc Monte Carlo simulation reproducing the observed ${\sim}3\times$ pair-to-batch amplification (conditional $R^2 \approx 7\%$ among non-zero confusion pairs to batch $R^2 \approx 22\%$; Appendix~\ref{app:aggregation-sim}) confirms this aggregation pattern.
68	
69	\paragraph{Cross-model validation.}
70	The effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\,pp (count 8) and $-$23.9\,pp (count 16), reaching 77--87\% of Qwen3-32B's gap. Both models converge to $\approx$51\% under high confusability regardless of count, while divergence is confined to the low-BCS regime, suggesting a task-inherent difficulty floor under high confusability (Table~\ref{tab:cross_model_bcs}). Dimension~1 replicates fully on Llama-3.1-8B (\S\ref{sec:count_curves}); Dimension~2 replicates on RE but shows floor effects on 8B NER (Limitations, item~1). Additional validation on Llama-3.1-70B-Instruct (FP8) confirms directional consistency across model scales (Appendix~\ref{sec:appendix_cross_model_70b}).
71	
72	\paragraph{Prompt sensitivity.}
73	Under the v2 prompt, the extreme-batch BCS gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; $n{=}25$; $r = -0.919$; $p < 0.001$), modestly attenuated from v1's extreme-batch gap but highly significant. NER shows no significant batch-level BCS--F1 correlation under either prompt version ($r \approx 0$, $n = 450$; \S\ref{sec:multi_channel}). Prompt design modulates magnitude but does not eliminate the RE effect (Appendix~\ref{sec:appendix_prompt_sensitivity}). The BCS--accuracy correlation holds across four structurally distinct prompt variants at count 32 (all $r \leq -0.47$; Appendix~\ref{sec:appendix_prompt_variants}), confirming that the confusability effect is not an artifact of prompt design.
74	
75	\subsection{Multi-Dimensional Degradation}
76	\label{sec:multi_channel}
77	
78	\begin{figure}[t]
79	\centering
80	\includegraphics[width=\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}
81	\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\%), but NER missed rates are substantially higher (43--65\%) and non-monotonic.}
82	\label{fig:error_taxonomy}
83	\end{figure}
84	
85	Error taxonomy decomposition (Table~\ref{tab:error_taxonomy} and Figure~\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\rho = 1.0$ ($p < 0.001$) for NER and $\rho = 0.954$ ($p < 0.001$) for RE. Under closed-set classification, non-\texttt{none} errors are necessarily intra-batch; the more informative finding is that IntraSub confusion frequency correlates with pairwise SCS ($\rho{=}0.954$, $p{<}0.001$). In NER, missed rates are higher (43--65\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\text{--}27.5\times$ more confusion than low-BCS batches.
86	
87	These results establish two dimensions: \textbf{Dimension~1} (count predicts recall decline) and \textbf{Dimension~2} (confusability predicts type confusion), consistent with bounded association in RE but coupled in NER where type ambiguity and boundary ambiguity interact. The full-range regression ($n = 69$, five count levels) serves as the primary separability test; the $2 \times 2$ factorial ($n = 54$) as a sensitivity check. Two One-Sided Tests (TOST) equivalence testing \citep{lakens-2017-equivalence} with a $\pm 3$\,pp margin ($p_{\text{TOST}} = 0.003$) confirms bounded association; sensitivity analysis at $\pm 2$\,pp and on the logit scale is reported in Appendix~\ref{sec:appendix_factorial}.
88	
89	\subsection{Centrality Confound on Homogeneous Schemas}
90	\label{sec:centrality_confound}
91	
92	Per-type analysis on MAVEN reveals an anomalous \emph{positive} BCS--F1 correlation (Qwen3 $\rho = +0.184$, $p = 0.025$; MiniLM $\rho = +0.208$, $p = 0.011$). This traces to same-domain embedding collapse \cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly, so mean BCS conflates confusability with centrality: high-BCS types are semantically central and easy to extract. Controlling for log frequency and degree centrality, the positive correlation vanishes ($p > 0.2$; Appendix~\ref{sec:appendix_residualized_bcs}). The pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$; Table~\ref{tab:pairwise}); the problem is per-type aggregation, not the underlying relationship. Few-NERD's cross-domain schema does not exhibit this confound ($\rho = -0.293$, $p = 0.02$). Mean BCS is thus reliable only for cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6a3c840-26ee-468c-ab59-41d2b6666b97",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "f85e9a28-df52-44e1-96ad-61073b2611d4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves for NER and RE. Error bars show $\\pm 1$\\,SD across 3 seeds (42, 123, 456) $\\times$ 25 batches per seed. RE accuracy declines monotonically with count; NER recall exhibits a U-shaped pattern with minimum at intermediate counts. Full-schema points (rightmost, hollow markers) represent the complete type inventory with no batch sampling variance. \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nFigure~\\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\\%$\\to$38.7\\%, $-$56\\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\\S\\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\\,pp on Few-NERD; per-batch $r = 0.725$; Table~\\ref{tab:cross_model}), indicating schema configuration rather than model-specific factors predicts difficulty. The pattern replicates across three seeds (42, 123, 456; max $\\Delta = 10.7$\\,pp, within 1\\,SD); intra-batch variance exceeds inter-seed variance by ${>}$5$\\times$ at every count level (Appendix~\\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $J = 109{,}707$, $p < 0.001$, pooled across three seeds). Count curves (25 batches per level) establish trend direction with error bars; magnitude estimation relies on the higher-powered BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\\,0.001$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\\,0.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models (both $p \\ll 0.001$). Confusion rate for each ordered pair $(t_i, t_j)$ is computed as the total bidirectional confusion count $C(t_i{\\to}t_j) + C(t_j{\\to}t_i)$ divided by the sum of gold frequencies, aggregated over all count conditions; CIs are pair-level percentile bootstrap ($B{=}10{,}000$). FewRel ($r = 0.187$; \\S\\ref{sec:scs-validation}) is excluded as RE's per-instance format precludes direct comparison of confusion rates. Type-level cluster bootstrap CIs: Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]; both exclude zero, confirming robustness to within-type correlation.}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Both datasets show significant positive correlations between pairwise SCS and type confusion rates. Spearman correlations corroborate: $\\rho = 0.144\\text{--}0.227$ across all pairs, strengthening to $\\rho = 0.27\\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).\n\nThe remaining variance likely reflects entity frequency, prompt position \\cite{lost-in-middle-2024}, mention ambiguity, and definition quality. Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\\,pp under typical batching (\\S\\ref{sec:practical_magnitude}). Notably, the independent MiniLM embedding yields a \\emph{stronger} SCS--confusion correlation on Few-NERD ($r = 0.172$ vs.\\ Qwen3 $r = 0.138$; Appendix), suggesting that shared-representation bias is conservative rather than inflationary.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nWe fix type count and vary BCS. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound; the within-pool analysis (\\S\\ref{sec:within_pool}) controls for pool composition.\n\nIn BCS-controlled FewRel subsets, the high-BCS quartile shows $\\Delta=-5.3$\\,pp lower accuracy than low-BCS (quartile comparison; full data in Appendix~\\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\\,pp (CI: [17.7, 42.7]), stable across count levels. An intermediate count${}\\,=\\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\\,pp at count 8, $-$31.8\\,pp at count 16), confirming monotonic decline.\n\n\\paragraph{Document-level RE (DocRED).}\nThe effect replicates on DocRED's 96-relation schema: BCS gap $-$23.3\\,pp at count 16 (slope $= -0.713$, $\\rho = -0.661$, $p < 0.001$) and $-$17.6\\,pp at count 32 (slope $= -0.690$, $\\rho = -0.509$, $p = 0.002$). BCS explains 44--53\\% of cross-batch variance ($R^2 = 0.525$ at count 16), substantially higher than FewRel ($R^2 = 0.218$), possibly reflecting a wider confusability range in the DocRED schema, though document-level context may also provide richer cues for type confusion. Across all RE settings, BCS slopes range from $-$0.40 to $-$0.71, significant in all conditions with sufficient BCS range.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nWithin-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\\S\\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nDirect regression on 100 random 16-type batches from the 80-relation pool shows BCS explains 22\\% of cross-batch accuracy variance ($R^2 = 0.218$, $p < 0.001$), scaling to 53\\% at DocRED 96-rel. The typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). High mean-BCS batches contain more active confusable pairs, concentrating degradation. A post-hoc Monte Carlo simulation reproducing the observed ${\\sim}3\\times$ pair-to-batch amplification (conditional $R^2 \\approx 7\\%$ among non-zero confusion pairs to batch $R^2 \\approx 22\\%$; Appendix~\\ref{app:aggregation-sim}) confirms this aggregation pattern.\n\n\\paragraph{Cross-model validation.}\nThe effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\\,pp (count 8) and $-$23.9\\,pp (count 16), reaching 77--87\\% of Qwen3-32B's gap. Both models converge to $\\approx$51\\% under high confusability regardless of count, while divergence is confined to the low-BCS regime, suggesting a task-inherent difficulty floor under high confusability (Table~\\ref{tab:cross_model_bcs}). Dimension~1 replicates fully on Llama-3.1-8B (\\S\\ref{sec:count_curves}); Dimension~2 replicates on RE but shows floor effects on 8B NER (Limitations, item~1). Additional validation on Llama-3.1-70B-Instruct (FP8) confirms directional consistency across model scales (Appendix~\\ref{sec:appendix_cross_model_70b}).\n\n\\paragraph{Prompt sensitivity.}\nUnder the v2 prompt, the extreme-batch BCS gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; $n{=}25$; $r = -0.919$; $p < 0.001$), modestly attenuated from v1's extreme-batch gap but highly significant. NER shows no significant batch-level BCS--F1 correlation under either prompt version ($r \\approx 0$, $n = 450$; \\S\\ref{sec:multi_channel}). Prompt design modulates magnitude but does not eliminate the RE effect (Appendix~\\ref{sec:appendix_prompt_sensitivity}). The BCS--accuracy correlation holds across four structurally distinct prompt variants at count 32 (all $r \\leq -0.47$; Appendix~\\ref{sec:appendix_prompt_variants}), confirming that the confusability effect is not an artifact of prompt design.\n\n\\subsection{Multi-Dimensional Degradation}\n\\label{sec:multi_channel}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure}\n\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\\rho = 1.0$ ($p < 0.001$) for NER and $\\rho = 0.954$ ($p < 0.001$) for RE. Under closed-set classification, non-\\texttt{none} errors are necessarily intra-batch; the more informative finding is that IntraSub confusion frequency correlates with pairwise SCS ($\\rho{=}0.954$, $p{<}0.001$). In NER, missed rates are higher (43--65\\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches.\n\nThese results establish two dimensions: \\textbf{Dimension~1} (count predicts recall decline) and \\textbf{Dimension~2} (confusability predicts type confusion), consistent with bounded association in RE but coupled in NER where type ambiguity and boundary ambiguity interact. The full-range regression ($n = 69$, five count levels) serves as the primary separability test; the $2 \\times 2$ factorial ($n = 54$) as a sensitivity check. Two One-Sided Tests (TOST) equivalence testing \\citep{lakens-2017-equivalence} with a $\\pm 3$\\,pp margin ($p_{\\text{TOST}} = 0.003$) confirms bounded association; sensitivity analysis at $\\pm 2$\\,pp and on the logit scale is reported in Appendix~\\ref{sec:appendix_factorial}.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--F1 correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$). This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly, so mean BCS conflates confusability with centrality: high-BCS types are semantically central and easy to extract. Controlling for log frequency and degree centrality, the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). The pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}); the problem is per-type aggregation, not the underlying relationship. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$). Mean BCS is thus reliable only for cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment.",
      "numLines": 92,
      "startLine": 1,
      "totalLines": 92
    }
  },
  "sourceToolAssistantUUID": "e6a3c840-26ee-468c-ab59-41d2b6666b97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-17T14:15:00.091Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MhETt6DFhEBDEB7MegNeJP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f85e9a28-df52-44e1-96ad-61073b2611d4",
  "isSidechain": false,
  "requestId": "req_011Cb8HFBXHjMe8jtehPehtU",
  "type": "assistant",
  "uuid": "af09864d-76ab-4bfb-aa77-338ffadf623c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NJw5hmfbB2mgx3NQoiT4o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22336,
      "cache_read_input_tokens": 35584,
      "output_tokens": 947,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 947,
          "cache_read_input_tokens": 35584,
          "cache_creation_input_tokens": 22336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22336
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

_source line 46 · 2026-05-17T14:15:00.096Z_

<details><summary>↩ Tool result · `toolu_01MhETt6DFhEBDEB7MegNeJP`</summary>

```text
1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-related degradation is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
5	
6	\paragraph{NER: merge amplification.}
7	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320, per-type 0.292 (Appendix~\ref{sec:appendix_sdgd}). The core failure is \emph{merge amplification}: presenting text to the model $k$ times with different type subsets is associated with precision collapsing (0.563$\to$0.210--0.249) as false positives scale with $k$, while true positives remain bounded. Confidence gating does not recover net F1. RE avoids this failure because closed-set classification requires no span reconciliation across passes.
8	
9	\paragraph{RE: oracle routing.}
10	Oracle routing achieves 0.802 accuracy versus 0.504 single-pass on FewRel 80-relation RE (+29.8\,pp; Table~\ref{tab:batch_composition}), confirming that type separation recovers performance absent merge amplification. Confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.); all practical routing strategies fall below the single-pass baseline because constrained decoding forces confident predictions in every sub-schema (Appendix~\ref{sec:appendix_routing}).
11	
12	\paragraph{Future directions.}
13	Three avenues may address these bottlenecks: (1)~coarse-to-fine pipelines that screen with the full schema then refine with targeted sub-schemas; (2)~retrieval-based routing using document retrieval rather than LLM confidence for sub-schema assignment; (3)~calibrated generation to recover confidence signals eliminated by constrained decoding.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{@{}lcc@{}}
20	\toprule
21	\textbf{Condition} & \textbf{Accuracy} & \textbf{Mean BCS} \\
22	\midrule
23	Single-pass (80 types) & 0.504 & 0.557 \\
24	Random batching (15 seeds)$^\dagger$ & 0.788\,$\pm$\,0.018 & 0.559 \\
25	Confus.-aware (graph coloring) & \textbf{0.802} & 0.552 \\
26	\bottomrule
27	\end{tabular}}
28	\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\dagger$Mean $\pm$ SD across 15 random seeds.}
29	\label{tab:batch_composition}
30	\end{table}
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af09864d-76ab-4bfb-aa77-338ffadf623c",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "c7a35d28-98ce-4d5e-9182-e3239c011586",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
      "content": "\\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}\n\\label{sec:sdgd}\n\nA natural intervention against confusability-related degradation is to partition the schema so confusable types never co-occur. We test this with \\textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.\n\n\\paragraph{NER: merge amplification.}\nAll decomposition modes fall below the single-pass NER baseline (F1\\,=\\,0.445): SDGD obtains 0.251, random batching 0.320, per-type 0.292 (Appendix~\\ref{sec:appendix_sdgd}). The core failure is \\emph{merge amplification}: presenting text to the model $k$ times with different type subsets is associated with precision collapsing (0.563$\\to$0.210--0.249) as false positives scale with $k$, while true positives remain bounded. Confidence gating does not recover net F1. RE avoids this failure because closed-set classification requires no span reconciliation across passes.\n\n\\paragraph{RE: oracle routing.}\nOracle routing achieves 0.802 accuracy versus 0.504 single-pass on FewRel 80-relation RE (+29.8\\,pp; Table~\\ref{tab:batch_composition}), confirming that type separation recovers performance absent merge amplification. Confusability-aware grouping yields only +1.4\\,pp over random ($p \\approx 0.19$, n.s.); all practical routing strategies fall below the single-pass baseline because constrained decoding forces confident predictions in every sub-schema (Appendix~\\ref{sec:appendix_routing}).\n\n\\paragraph{Future directions.}\nThree avenues may address these bottlenecks: (1)~coarse-to-fine pipelines that screen with the full schema then refine with targeted sub-schemas; (2)~retrieval-based routing using document retrieval rather than LLM confidence for sub-schema assignment; (3)~calibrated generation to recover confidence signals eliminated by constrained decoding.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds.}\n\\label{tab:batch_composition}\n\\end{table}\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  },
  "sourceToolAssistantUUID": "af09864d-76ab-4bfb-aa77-338ffadf623c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-17T14:15:00.549Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EnGcFzW9bopiRPW39NVhKq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7a35d28-98ce-4d5e-9182-e3239c011586",
  "isSidechain": false,
  "requestId": "req_011Cb8HFBXHjMe8jtehPehtU",
  "type": "assistant",
  "uuid": "93f345a6-cb8c-4398-9f2a-f5c29765e55f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NJw5hmfbB2mgx3NQoiT4o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22336,
      "cache_read_input_tokens": 35584,
      "output_tokens": 947,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 947,
          "cache_read_input_tokens": 35584,
          "cache_creation_input_tokens": 22336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22336
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

_source line 48 · 2026-05-17T14:15:00.560Z_

<details><summary>↩ Tool result · `toolu_01EnGcFzW9bopiRPW39NVhKq`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% across models, suggesting a difficulty ceiling. RE's separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\,pp; Appendix~\ref{sec:appendix_prompt_sensitivity}). Cross-scale evidence (32B vs.\ 8B) shows Dimension~1 replicates fully while Dimension~2 attenuates on smaller models, dropping to near-zero $R^2$ for NER on Llama-3.1-8B (Tables~\ref{tab:cross_model}--\ref{tab:cross_model_bcs}). Count-related degradation may partly reflect prompt length (per-type recall 0.586 vs.\ single-pass 0.368, consistent with lost-in-middle effects; \citealt{lost-in-middle-2024}; \citealt{levy-2024-same-task}).
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	SCS captures semantic proximity in LLMs' type-resolution space. The unconditional pair-level effect is modest ($r^2 = 1.3$--$1.7\%$, as ${\sim}89\%$ of pairs never produce mutual confusion); among active-confusion pairs, $R^2 \approx 7\%$ amplifies ${\sim}3\times$ at batch level (Appendix~\ref{app:aggregation-sim}), yielding $R^2$ of 22--53\%. For individual type pairs, SCS is therefore a weak predictor; other factors such as frequency, context diversity, and definition quality dominate. At the batch level, however, these pair-level effects aggregate to produce the observed $R^2$ of 22--53\% in RE, sufficient for practical schema-level screening. We hypothesize that the NER U-shape (\S\ref{sec:count_curves}) reflects a dual-task burden absent in RE: partial schemas require simultaneous span detection and type-membership filtering; at full-schema, filtering becomes vacuous and recall recovers, confirming task-specific pathways.
9	
10	\paragraph{Task-dependent batch-level effects.}
11	While pairwise SCS predicts type confusion in both NER and RE, the batch-level BCS--performance relationship is RE-specific: BCS explains 22--53\% of cross-batch accuracy variance in RE but shows no significant correlation with NER F1 ($r \approx 0$, $n = 450$). We hypothesize this reflects the different error structures: RE errors are dominated by type substitution (IntraSub scales with BCS; \S\ref{sec:multi_channel}), so batch-level confusability directly predicts accuracy. NER errors are dominated by missed entities (43--65\% of errors), which correlate with count rather than confusability; pairwise SCS captures individual type confusion but this signal is diluted at the batch level by the overwhelming contribution of boundary detection failures. This task dependence has practical implications: BCS is a useful pre-hoc screening tool for RE schema design but not for NER, where count reduction is the primary lever.
12	
13	\paragraph{Practical implications.}
14	The bounded count$\times$confusability interaction (0.47\,pp, TOST $p = 0.003$) is itself an actionable finding: practitioners who scale schema size need not additionally worry about confusability amplification of count-related degradation. For RE deployment with cross-domain schemas, BCS provides a lightweight pre-hoc screen: schemas that exceed the top-quartile BCS threshold (mean pairwise SCS $> 0.59$) can expect 3--5\,pp lower accuracy, which can inform decisions about few-shot augmentation or schema redesign. For NER, count is the dominant predictor, and the primary mitigation strategy is to reduce schema size per prompt. Even few-shot demonstrations do not mitigate the confusability gap: under 5-shot prompting, the BCS penalty persists and slightly widens (+4.3\,pp over 0-shot), suggesting confusability is a structural property of the schema rather than a prompt engineering problem (Appendix~\ref{sec:appendix_fewshot_bcs}). These results apply to the training-free setting; fine-tuned models may learn type boundaries that reduce confusability effects.
15	
16	\section{Conclusion}
17	\label{sec:conclusion}
18	
19	Schema-induced degradation in training-free LLM extraction operates along two dimensions (count-related recall decline, confusability-related type confusion) with bounded association in RE but coupling in NER. Dimension~1 replicates across scales; Dimension~2 attenuates on smaller models. BCS enables pre-hoc screening.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93f345a6-cb8c-4398-9f2a-f5c29765e55f",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "736d5119-e4ad-460d-bed1-5aa80cea9647",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Boundary conditions.}\nThe decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across models, suggesting a difficulty ceiling. RE's separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp; Appendix~\\ref{sec:appendix_prompt_sensitivity}). Cross-scale evidence (32B vs.\\ 8B) shows Dimension~1 replicates fully while Dimension~2 attenuates on smaller models, dropping to near-zero $R^2$ for NER on Llama-3.1-8B (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}). Count-related degradation may partly reflect prompt length (per-type recall 0.586 vs.\\ single-pass 0.368, consistent with lost-in-middle effects; \\citealt{lost-in-middle-2024}; \\citealt{levy-2024-same-task}).\n\n\\paragraph{Why does embedding similarity predict LLM confusion?}\nSCS captures semantic proximity in LLMs' type-resolution space. The unconditional pair-level effect is modest ($r^2 = 1.3$--$1.7\\%$, as ${\\sim}89\\%$ of pairs never produce mutual confusion); among active-confusion pairs, $R^2 \\approx 7\\%$ amplifies ${\\sim}3\\times$ at batch level (Appendix~\\ref{app:aggregation-sim}), yielding $R^2$ of 22--53\\%. For individual type pairs, SCS is therefore a weak predictor; other factors such as frequency, context diversity, and definition quality dominate. At the batch level, however, these pair-level effects aggregate to produce the observed $R^2$ of 22--53\\% in RE, sufficient for practical schema-level screening. We hypothesize that the NER U-shape (\\S\\ref{sec:count_curves}) reflects a dual-task burden absent in RE: partial schemas require simultaneous span detection and type-membership filtering; at full-schema, filtering becomes vacuous and recall recovers, confirming task-specific pathways.\n\n\\paragraph{Task-dependent batch-level effects.}\nWhile pairwise SCS predicts type confusion in both NER and RE, the batch-level BCS--performance relationship is RE-specific: BCS explains 22--53\\% of cross-batch accuracy variance in RE but shows no significant correlation with NER F1 ($r \\approx 0$, $n = 450$). We hypothesize this reflects the different error structures: RE errors are dominated by type substitution (IntraSub scales with BCS; \\S\\ref{sec:multi_channel}), so batch-level confusability directly predicts accuracy. NER errors are dominated by missed entities (43--65\\% of errors), which correlate with count rather than confusability; pairwise SCS captures individual type confusion but this signal is diluted at the batch level by the overwhelming contribution of boundary detection failures. This task dependence has practical implications: BCS is a useful pre-hoc screening tool for RE schema design but not for NER, where count reduction is the primary lever.\n\n\\paragraph{Practical implications.}\nThe bounded count$\\times$confusability interaction (0.47\\,pp, TOST $p = 0.003$) is itself an actionable finding: practitioners who scale schema size need not additionally worry about confusability amplification of count-related degradation. For RE deployment with cross-domain schemas, BCS provides a lightweight pre-hoc screen: schemas that exceed the top-quartile BCS threshold (mean pairwise SCS $> 0.59$) can expect 3--5\\,pp lower accuracy, which can inform decisions about few-shot augmentation or schema redesign. For NER, count is the dominant predictor, and the primary mitigation strategy is to reduce schema size per prompt. Even few-shot demonstrations do not mitigate the confusability gap: under 5-shot prompting, the BCS penalty persists and slightly widens (+4.3\\,pp over 0-shot), suggesting confusability is a structural property of the schema rather than a prompt engineering problem (Appendix~\\ref{sec:appendix_fewshot_bcs}). These results apply to the training-free setting; fine-tuned models may learn type boundaries that reduce confusability effects.\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nSchema-induced degradation in training-free LLM extraction operates along two dimensions (count-related recall decline, confusability-related type confusion) with bounded association in RE but coupling in NER. Dimension~1 replicates across scales; Dimension~2 attenuates on smaller models. BCS enables pre-hoc screening.\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  },
  "sourceToolAssistantUUID": "93f345a6-cb8c-4398-9f2a-f5c29765e55f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-17T14:15:00.982Z_

<details open><summary>🔧 Tool call — Read · `toolu_011m3PEuUMFnijAxbT3yVoVJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "736d5119-e4ad-460d-bed1-5aa80cea9647",
  "isSidechain": false,
  "requestId": "req_011Cb8HFBXHjMe8jtehPehtU",
  "type": "assistant",
  "uuid": "3342c80f-aa61-47a4-81ab-0b34d5a08e26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NJw5hmfbB2mgx3NQoiT4o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22336,
      "cache_read_input_tokens": 35584,
      "output_tokens": 947,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 947,
          "cache_read_input_tokens": 35584,
          "cache_creation_input_tokens": 22336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22336
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

_source line 50 · 2026-05-17T14:15:00.991Z_

<details><summary>↩ Tool result · `toolu_011m3PEuUMFnijAxbT3yVoVJ`</summary>

```text
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
11	Yes. The Limitations section (after \S\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, factorial interaction tests with TOST equivalence, decomposition scope, and metric scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	N/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-dimensional degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. We used Claude (Anthropic) for writing assistance and experimental code development. All scientific claims, experimental designs, and analyses were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and Meta-Llama-3.1-8B-Instruct \cite{llama3-2024}, vLLM \cite{vllm-2023}, and all-MiniLM-L6-v2 \cite{minilm-2020} are cited in \S\ref{sec:datasets} and \S\ref{sec:model}.
34	
35	\item \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}
36	
37	Yes. All four datasets are publicly available research benchmarks. Few-NERD is released under CC-BY-SA 4.0; FewRel, DocRED, and MAVEN are publicly released for research use. Models are used under their respective open-weight licenses.
38	
39	\item \textbf{Did you discuss if your use of existing artifacts is consistent with their intended use?}
40	
41	Yes. All datasets are used for their intended purpose (IE evaluation). No data is used outside the scope specified by the dataset creators.
42	
43	\item \textbf{Did you discuss whether the data contains personally identifiable information or offensive content?}
44	
45	N/A. We use established benchmarks that have been vetted by the research community. No new data collection or annotation was performed.
46	
47	\item \textbf{Did you provide documentation of the artifacts, e.g., coverage of languages, coverage of domains, etc.?}
48	
49	Yes. Table~\ref{tab:datasets} reports type counts, evaluation unit counts, domain characteristics, and BCS ranges for each dataset. \S\ref{sec:datasets} describes dataset provenance and sampling procedures.
50	
51	\item \textbf{Did you report relevant statistics for your dataset(s)?}
52	
53	Yes. \S\ref{sec:datasets} and Table~\ref{tab:datasets} report evaluation set sizes, type counts, and sampling methodology. Count levels and batch sizes are specified in \S\ref{sec:exp_design}.
54	
55	\end{enumerate}
56	
57	\subsection*{C \quad Computational Experiments}
58	
59	\begin{enumerate}[label=\textbf{C\arabic*.},leftmargin=*,itemsep=4pt]
60	
61	\item \textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?}
62	
63	Yes. \S\ref{sec:model}: Qwen3-32B (32B parameters, FP8), Meta-Llama-3.1-70B-Instruct (70B parameters, FP8), and Meta-Llama-3.1-8B-Instruct (8B parameters). Inference was conducted on NVIDIA RTX PRO 6000 GPUs (96\,GB) served via vLLM. Total compute was approximately 72 GPU-hours of inference (no training).
64	
65	\item \textbf{Did you discuss the experimental setup, including hyperparameter search and best-found values?}
66	
67	Yes. \S\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \S\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions. No hyperparameter search was conducted as this is a zero-shot evaluation study.
68	
69	\item \textbf{Did you report descriptive statistics about your results?}
70	
71	Yes. All key metrics include 95\% bootstrap confidence intervals (10{,}000 resamples, percentile method) as stated in \S\ref{sec:model}. Spearman correlations are reported with $p$-values throughout \S\ref{sec:count_curves}--\ref{sec:centrality_confound}. Permutation tests are used for slope comparisons.
72	
73	\item \textbf{Did you report implementation details, e.g., versions of packages?}
74	
75	Yes. \S\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\S\ref{sec:scs}). Code and scripts will be released upon acceptance.
76	
77	\end{enumerate}
78	
79	\subsection*{D \quad Human Annotators or Crowdworkers}
80	
81	\begin{enumerate}[label=\textbf{D\arabic*.},leftmargin=*,itemsep=4pt]
82	
83	\item \textbf{Did you report the full text of instructions given to participants?}
84	
85	N/A. No human annotation or crowdsourcing was conducted.
86	
87	\item \textbf{Did you report information about how you recruited and paid participants?}
88	
89	N/A.
90	
91	\item \textbf{Did you discuss whether and how consent was obtained?}
92	
93	N/A.
94	
95	\item \textbf{Did you report whether the data collection was approved by an institutional review board (IRB)?}
96	
97	N/A.
98	
99	\item \textbf{Did you report the basic demographic and geographic characteristics of the annotator population?}
100	
101	N/A.
102	
103	\end{enumerate}
104	
105	\subsection*{E \quad AI-Assisted Research}
106	
107	\begin{enumerate}[label=\textbf{E\arabic*.},leftmargin=*,itemsep=4pt]
108	
109	\item \textbf{Did you report the use of AI assistants?}
110	
111	Yes. See A4 above. AI assistants were used for code development and document formatting. The research design, execution, and interpretation are the authors' own work.
112	
113	\end{enumerate}
114	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3342c80f-aa61-47a4-81ab-0b34d5a08e26",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "4eae0676-e200-4083-84af-137f7467cc49",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex",
      "content": "\\section*{Responsible NLP Research Checklist}\n\nFor each question, the answer is \\textbf{Yes}, \\textbf{No}, or \\textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.\n\n\\subsection*{A \\quad For Every Submission}\n\n\\begin{enumerate}[label=\\textbf{A\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you describe the limitations of your work?}\n\nYes. The Limitations section (after \\S\\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, factorial interaction tests with TOST equivalence, decomposition scope, and metric scope.\n\n\\item \\textbf{Did you discuss any potential risks of your work?}\n\nN/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.\n\n\\item \\textbf{Do the abstract and introduction summarize the paper's main claims?}\n\nYes. The abstract and \\S\\ref{sec:introduction} state the two-dimensional degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.\n\n\\item \\textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}\n\nYes. We used Claude (Anthropic) for writing assistance and experimental code development. All scientific claims, experimental designs, and analyses were conducted by the authors.\n\n\\end{enumerate}\n\n\\subsection*{B \\quad Scientific Artifacts}\n\n\\begin{enumerate}[label=\\textbf{B\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you cite the creators of artifacts you used?}\n\nYes. Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, MAVEN \\cite{maven-2020}, Qwen3-32B \\cite{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and Meta-Llama-3.1-8B-Instruct \\cite{llama3-2024}, vLLM \\cite{vllm-2023}, and all-MiniLM-L6-v2 \\cite{minilm-2020} are cited in \\S\\ref{sec:datasets} and \\S\\ref{sec:model}.\n\n\\item \\textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}\n\nYes. All four datasets are publicly available research benchmarks. Few-NERD is released under CC-BY-SA 4.0; FewRel, DocRED, and MAVEN are publicly released for research use. Models are used under their respective open-weight licenses.\n\n\\item \\textbf{Did you discuss if your use of existing artifacts is consistent with their intended use?}\n\nYes. All datasets are used for their intended purpose (IE evaluation). No data is used outside the scope specified by the dataset creators.\n\n\\item \\textbf{Did you discuss whether the data contains personally identifiable information or offensive content?}\n\nN/A. We use established benchmarks that have been vetted by the research community. No new data collection or annotation was performed.\n\n\\item \\textbf{Did you provide documentation of the artifacts, e.g., coverage of languages, coverage of domains, etc.?}\n\nYes. Table~\\ref{tab:datasets} reports type counts, evaluation unit counts, domain characteristics, and BCS ranges for each dataset. \\S\\ref{sec:datasets} describes dataset provenance and sampling procedures.\n\n\\item \\textbf{Did you report relevant statistics for your dataset(s)?}\n\nYes. \\S\\ref{sec:datasets} and Table~\\ref{tab:datasets} report evaluation set sizes, type counts, and sampling methodology. Count levels and batch sizes are specified in \\S\\ref{sec:exp_design}.\n\n\\end{enumerate}\n\n\\subsection*{C \\quad Computational Experiments}\n\n\\begin{enumerate}[label=\\textbf{C\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?}\n\nYes. \\S\\ref{sec:model}: Qwen3-32B (32B parameters, FP8), Meta-Llama-3.1-70B-Instruct (70B parameters, FP8), and Meta-Llama-3.1-8B-Instruct (8B parameters). Inference was conducted on NVIDIA RTX PRO 6000 GPUs (96\\,GB) served via vLLM. Total compute was approximately 72 GPU-hours of inference (no training).\n\n\\item \\textbf{Did you discuss the experimental setup, including hyperparameter search and best-found values?}\n\nYes. \\S\\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \\S\\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions. No hyperparameter search was conducted as this is a zero-shot evaluation study.\n\n\\item \\textbf{Did you report descriptive statistics about your results?}\n\nYes. All key metrics include 95\\% bootstrap confidence intervals (10{,}000 resamples, percentile method) as stated in \\S\\ref{sec:model}. Spearman correlations are reported with $p$-values throughout \\S\\ref{sec:count_curves}--\\ref{sec:centrality_confound}. Permutation tests are used for slope comparisons.\n\n\\item \\textbf{Did you report implementation details, e.g., versions of packages?}\n\nYes. \\S\\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\\S\\ref{sec:scs}). Code and scripts will be released upon acceptance.\n\n\\end{enumerate}\n\n\\subsection*{D \\quad Human Annotators or Crowdworkers}\n\n\\begin{enumerate}[label=\\textbf{D\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the full text of instructions given to participants?}\n\nN/A. No human annotation or crowdsourcing was conducted.\n\n\\item \\textbf{Did you report information about how you recruited and paid participants?}\n\nN/A.\n\n\\item \\textbf{Did you discuss whether and how consent was obtained?}\n\nN/A.\n\n\\item \\textbf{Did you report whether the data collection was approved by an institutional review board (IRB)?}\n\nN/A.\n\n\\item \\textbf{Did you report the basic demographic and geographic characteristics of the annotator population?}\n\nN/A.\n\n\\end{enumerate}\n\n\\subsection*{E \\quad AI-Assisted Research}\n\n\\begin{enumerate}[label=\\textbf{E\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the use of AI assistants?}\n\nYes. See A4 above. AI assistants were used for code development and document formatting. The research design, execution, and interpretation are the authors' own work.\n\n\\end{enumerate}\n",
      "numLines": 114,
      "startLine": 1,
      "totalLines": 114
    }
  },
  "sourceToolAssistantUUID": "3342c80f-aa61-47a4-81ab-0b34d5a08e26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-17T14:15:01.922Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MR5TpSXrU6ghFnVfEYwdtt`</summary>

```json
{
  "query": "EMNLP 2026 ARR submission format page limit long short paper guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4eae0676-e200-4083-84af-137f7467cc49",
  "isSidechain": false,
  "requestId": "req_011Cb8HFBXHjMe8jtehPehtU",
  "type": "assistant",
  "uuid": "b858599d-bb39-494f-9735-ec4e87265f43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NJw5hmfbB2mgx3NQoiT4o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22336,
      "cache_read_input_tokens": 35584,
      "output_tokens": 947,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 947,
          "cache_read_input_tokens": 35584,
          "cache_creation_input_tokens": 22336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22336
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

_source line 52 · 2026-05-17T14:15:02.277Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Ls7q1CniJDx3UrEuA4iMoT`</summary>

```json
{
  "pattern": "projects/schema-dag-extraction/artifacts/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b858599d-bb39-494f-9735-ec4e87265f43",
  "isSidechain": false,
  "requestId": "req_011Cb8HFBXHjMe8jtehPehtU",
  "type": "assistant",
  "uuid": "a60cd202-829b-404b-acca-a81af6d176f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NJw5hmfbB2mgx3NQoiT4o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22336,
      "cache_read_input_tokens": 35584,
      "output_tokens": 947,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 947,
          "cache_read_input_tokens": 35584,
          "cache_creation_input_tokens": 22336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22336
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

_source line 53_

```json
{
  "type": "last-prompt",
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: schema-dag-extraction - 论文路径: projects/schema-dag-extraction/docs/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: Main Conference - 截止日期: 2026-05-25  请 `Read /home/ubun…",
  "leafUuid": "668ccd58-bd53-4145-b492-c67105983013",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "Review schema-dag-extraction paper for EMNLP 2026",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a"
}
```

---

### Tool result

_source line 55 · 2026-05-17T14:15:13.851Z_

<details><summary>↩ Tool result · `toolu_01MR5TpSXrU6ghFnVfEYwdtt`</summary>

```text
Web search results for query: "EMNLP 2026 ARR submission format page limit long short paper guidelines"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"}]

Based on the search results, here's what I found about EMNLP 2026 ARR submission format guidelines:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

## Submission Format

EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences.

## Limitations Section

The mandatory Limitations section is required, placed after the conclusion. Submissions that exceed the length requirements, or are missing a limitations section, will be desk rejected.

## Anonymization

Papers must not include authors' names and affiliations.

## Key Deadline

All submissions go through ACL Rolling Review (ARR), with the ARR submission deadline of May 25, 2026.

For more detailed information about submission guidelines and requirements, you can visit the official EMNLP 2026 main conference papers call at https://2026.emnlp.org/calls/main_conference_papers/ or the ARR Call for Papers at http://aclrollingreview.org/cfp.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b858599d-bb39-494f-9735-ec4e87265f43",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "872ad9a7-7427-455a-a603-40cb17808229",
  "toolUseResult": {
    "query": "EMNLP 2026 ARR submission format page limit long short paper guidelines",
    "results": [
      {
        "tool_use_id": "srvtoolu_016yZq4NCPeZUYwMkmtVMNjV",
        "content": [
          {
            "title": "Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026",
            "url": "https://2026.emnlp.org/calls/industry_track/"
          },
          {
            "title": "EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf",
            "url": "https://www.underleaf.ai/templates/emnlp"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "Call for Main Conference Papers -",
            "url": "https://2026.eacl.org/calls/papers/"
          },
          {
            "title": "Authors Guidelines",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "Call for workshops: EMNLP & AACL",
            "url": "https://groups.google.com/g/ml-news/c/W-fucfhVto4"
          },
          {
            "title": "Submission Guide",
            "url": "https://nlp4climate.github.io/submissionguide/"
          },
          {
            "title": "EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X",
            "url": "https://x.com/emnlpmeeting/status/2029508292637061462"
          },
          {
            "title": "Dates and Venues",
            "url": "http://aclrollingreview.org/dates"
          },
          {
            "title": "EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...",
            "url": "http://www.wikicfp.com/cfp/program?id=883"
          }
        ]
      },
      "Based on the search results, here's what I found about EMNLP 2026 ARR submission format guidelines:\n\n## Page Limits\n\nThe format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.\n\n## Submission Format\n\nEMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences.\n\n## Limitations Section\n\nThe mandatory Limitations section is required, placed after the conclusion. Submissions that exceed the length requirements, or are missing a limitations section, will be desk rejected.\n\n## Anonymization\n\nPapers must not include authors' names and affiliations.\n\n## Key Deadline\n\nAll submissions go through ACL Rolling Review (ARR), with the ARR submission deadline of May 25, 2026.\n\nFor more detailed information about submission guidelines and requirements, you can visit the official EMNLP 2026 main conference papers call at https://2026.emnlp.org/calls/main_conference_papers/ or the ARR Call for Papers at http://aclrollingreview.org/cfp."
    ],
    "durationSeconds": 11.924888133999993
  },
  "sourceToolAssistantUUID": "b858599d-bb39-494f-9735-ec4e87265f43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 56 · 2026-05-17T14:15:13.856Z_

```json
{
  "parentUuid": "872ad9a7-7427-455a-a603-40cb17808229",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1f709067-a3a0-4ec2-977e-b0f4ef4a4d46",
  "timestamp": "2026-05-17T14:15:13.856Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 57 · 2026-05-17T14:15:25.856Z_

<details><summary>Logged reasoning block</summary>

```text
Let me also read the prompt_appendix.tex and references.bib. I also need to check for external review configuration. Let me also search for the ARR CFP page to get more specific requirements.

Let me now check:
1. The prompt_appendix file
2. The references file
3. The external review config
4. More specific ARR/EMNLP requirements

Actually, I have enough information to proceed. Let me summarize what I know:

**EMNLP 2026 venue requirements:**
- Through ARR (ACL Rolling Review)
- ARR submission deadline: May 25, 2026


- Long papers are 8 pages plus unlimited references and appendix, short papers are 4 pages, with double-blind review using the ACL style template, a mandatory Limitations section, and two-column format.

**Paper status:**
- The paper exists at the given path with multiple tex files covering abstract through checklist sections, uses the correct review package configuration, has anonymous authorship properly set, includes both a Limitations section and the Responsible NLP Research Checklist.

Now I'm checking the external review configuration to set up reviewer assignments. For EMNLP 2026, I'll assign two reviewers—one focused on method rigor and experimental validity, the other on novelty, completeness, and writing quality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f709067-a3a0-4ec2-977e-b0f4ef4a4d46",
  "isSidechain": false,
  "requestId": "req_011Cb8HHFYBs584aLmm4KqMT",
  "type": "assistant",
  "uuid": "88d07414-c127-4081-b424-0b8c2f0c6bfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQZ4ABfcgTVRJB8tfrYeUY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 34,
      "cache_creation_input_tokens": 16692,
      "cache_read_input_tokens": 57920,
      "output_tokens": 673,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 34,
          "output_tokens": 673,
          "cache_read_input_tokens": 57920,
          "cache_creation_input_tokens": 16692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16692
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

_source line 58 · 2026-05-17T14:15:25.858Z_

需要检查外部审稿配置和论文引用文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88d07414-c127-4081-b424-0b8c2f0c6bfe",
  "isSidechain": false,
  "requestId": "req_011Cb8HHFYBs584aLmm4KqMT",
  "type": "assistant",
  "uuid": "b109e7ee-fc8c-47d9-813c-78a2e06a389e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQZ4ABfcgTVRJB8tfrYeUY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 34,
      "cache_creation_input_tokens": 16692,
      "cache_read_input_tokens": 57920,
      "output_tokens": 673,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 34,
          "output_tokens": 673,
          "cache_read_input_tokens": 57920,
          "cache_creation_input_tokens": 16692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16692
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

_source line 59 · 2026-05-17T14:15:27.244Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017TRRF3FaKmn6mRoHNcQugD`</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "paper_checklist.yaml",
  "max_chars": 5000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b109e7ee-fc8c-47d9-813c-78a2e06a389e",
  "isSidechain": false,
  "requestId": "req_011Cb8HHFYBs584aLmm4KqMT",
  "type": "assistant",
  "uuid": "21cfb3de-0705-4754-a88f-9e25ab1b6857",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQZ4ABfcgTVRJB8tfrYeUY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 34,
      "cache_creation_input_tokens": 16692,
      "cache_read_input_tokens": 57920,
      "output_tokens": 673,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 34,
          "output_tokens": 673,
          "cache_read_input_tokens": 57920,
          "cache_creation_input_tokens": 16692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16692
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

_source line 60 · 2026-05-17T14:15:27.265Z_

<details><summary>↩ Tool result · `toolu_017TRRF3FaKmn6mRoHNcQugD`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema-dag-extraction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21cfb3de-0705-4754-a88f-9e25ab1b6857",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "04cb566c-1314-4966-ab9a-4cd5bd7f0d91",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"No paper_checklist.yaml found for 'schema-dag-extraction'.\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema-dag-extraction'.\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "21cfb3de-0705-4754-a88f-9e25ab1b6857",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-17T14:15:28.769Z_

<details open><summary>🔧 Tool call — Read · `toolu_016FXB9kCoakrQ7gpiArbeSo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04cb566c-1314-4966-ab9a-4cd5bd7f0d91",
  "isSidechain": false,
  "requestId": "req_011Cb8HHFYBs584aLmm4KqMT",
  "type": "assistant",
  "uuid": "b2fd9176-1850-469a-8218-2198ae6f1c49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQZ4ABfcgTVRJB8tfrYeUY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 34,
      "cache_creation_input_tokens": 16692,
      "cache_read_input_tokens": 57920,
      "output_tokens": 673,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 34,
          "output_tokens": 673,
          "cache_read_input_tokens": 57920,
          "cache_creation_input_tokens": 16692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16692
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

_source line 62 · 2026-05-17T14:15:28.776Z_

<details><summary>↩ Tool result · `toolu_016FXB9kCoakrQ7gpiArbeSo`</summary>

```text
1	\lstset{
2	  basicstyle=\ttfamily\small,
3	  breaklines=true,
4	  breakatwhitespace=true,
5	  columns=fullflexible
6	}
7	
8	\section{Prompt Templates}
9	\label{sec:appendix_prompts}
10	
11	This appendix reproduces the complete prompt templates used for all three extraction tasks.
12	All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
13	Both versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \emph{not} included in the natural-language prompt itself.
14	We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout.
15	
16	\medskip\noindent
17	\textbf{Notation.}
18	Placeholders are shown in \texttt{\{braces\}}.
19	Text \textbf{added in v2} (relative to v1) is marked with $\triangleright$.
20	Text \textbf{removed in v2} is marked with \sout{strikethrough}.
21	
22	\subsection{Named Entity Recognition (Few-NERD)}
23	
24	\paragraph{v1 prompt (with character offsets).}
25	
26	\begin{small}
27	\begin{lstlisting}
28	Extract all named entities from the following text.
29	Only extract entities of the following types:
30	- {type_1}: {definition_1}
31	- {type_2}: {definition_2}
32	  ...
33	
34	Text: {input_text}
35	
36	Output as JSON: [{"text": "...", "type": "...",
37	                  "start": ..., "end": ...}]
38	\end{lstlisting}
39	\end{small}
40	
41	\noindent
42	\textbf{v1 constrained-decoding schema:}
43	\begin{small}
44	\begin{lstlisting}
45	{"type": "array",
46	 "items": {"type": "object",
47	   "properties": {
48	     "text":  {"type": "string"},
49	     "type":  {"type": "string",
50	               "enum": [&lt;sorted_types>]},
51	     "start": {"type": "integer"},
52	     "end":   {"type": "integer"}},
53	   "required": ["text","type","start","end"]}}
54	\end{lstlisting}
55	\end{small}
56	
57	\paragraph{v2 prompt (text+type only).}
58	
59	\begin{small}
60	\begin{lstlisting}
61	Extract all named entities from the following text.
62	Only extract entities of the following types:
63	- {type_1}: {definition_1}
64	- {type_2}: {definition_2}
65	  ...
66	
67	Text: {input_text}
68	\end{lstlisting}
69	\end{small}
70	\vspace{-0.5em}
71	\noindent$\triangleright$~\textbf{Added in v2:}
72	\begin{small}
73	\begin{lstlisting}
74	Only extract entities that clearly match one of the
75	given types. If no entities of these types exist in
76	the text, output an empty list [].
77	\end{lstlisting}
78	\end{small}
79	\vspace{-0.5em}
80	\begin{small}
81	\begin{lstlisting}
82	Output as JSON: [{"text": "...", "type": "..."}]
83	\end{lstlisting}
84	\end{small}
85	
86	\noindent
87	\textbf{v2 constrained-decoding schema:}
88	\begin{small}
89	\begin{lstlisting}
90	{"type": "array",
91	 "items": {"type": "object",
92	   "properties": {
93	     "text": {"type": "string"},
94	     "type": {"type": "string",
95	              "enum": [&lt;sorted_types>]}},
96	   "required": ["text","type"]}}
97	\end{lstlisting}
98	\end{small}
99	
100	\paragraph{v1 $\to$ v2 differences (NER).}
101	\begin{enumerate}[leftmargin=*,itemsep=2pt]
102	\item \textbf{Offset fields removed.} The \texttt{start}/\texttt{end} integer fields are dropped from both the natural-language instruction and the JSON schema. In v1, 96.5\% of predicted offsets were hallucinated (\S\ref{sec:model}).
103	\item \textbf{Format constraints added.} Two sentences are appended: (a)~``Only extract entities that clearly match one of the given types'' suppresses spurious predictions; (b)~``If no entities \ldots output an empty list~\texttt{[]}'' provides an explicit empty-output path.
104	\end{enumerate}
105	
106	\subsection{Event Detection (MAVEN)}
107	
108	\paragraph{v1 prompt (with character offsets).}
109	
110	\begin{small}
111	\begin{lstlisting}
112	Extract all event triggers from the following text.
113	A trigger is the word or phrase that most clearly
114	expresses the event occurrence. Only extract triggers
115	of the following event types:
116	- {type_1}: {definition_1}
117	- {type_2}: {definition_2}
118	  ...
119	
120	Text: {input_text}
121	
122	Output as JSON: [{"text": "...", "type": "...",
123	                  "start": ..., "end": ...}]
124	\end{lstlisting}
125	\end{small}
126	
127	\paragraph{v2 prompt (text+type only).}
128	
129	\begin{small}
130	\begin{lstlisting}
131	Extract all event triggers from the following text.
132	A trigger is the word or phrase that most clearly
133	expresses the event occurrence. Only extract triggers
134	of the following event types:
135	- {type_1}: {definition_1}
136	- {type_2}: {definition_2}
137	  ...
138	
139	Text: {input_text}
140	\end{lstlisting}
141	\end{small}
142	\vspace{-0.5em}
143	\noindent$\triangleright$~\textbf{Added in v2:}
144	\begin{small}
145	\begin{lstlisting}
146	Only extract triggers that clearly match one of the
147	given event types. If no events of these types exist
148	in the text, output an empty list [].
149	\end{lstlisting}
150	\end{small}
151	\vspace{-0.5em}
152	\begin{small}
153	\begin{lstlisting}
154	Output as JSON: [{"text": "...", "type": "..."}]
155	\end{lstlisting}
156	\end{small}
157	
158	\noindent The JSON schemas for ED are identical to the NER schemas above; only the natural-language framing differs (``event triggers'' instead of ``named entities'').
159	
160	\paragraph{v1 $\to$ v2 differences (ED).}
161	Same two changes as NER: offset fields removed, format constraints added.
162	
163	\subsection{Relation Extraction (FewRel)}
164	
165	RE uses only a v2-style prompt (no offset fields are applicable to classification).
166	
167	\paragraph{Prompt.}
168	
169	\begin{small}
170	\begin{lstlisting}
171	Given the following sentence and two entities,
172	classify the relation between them.
173	
174	Sentence: "{sentence}"
175	Head entity: "{head_entity}"
176	Tail entity: "{tail_entity}"
177	
178	Candidate relations: {type_1}, {type_2}, ...
179	
180	Output a single JSON object:
181	  {"relation": "&lt;relation_type>"}
182	If none of the candidate relations apply, output:
183	  {"relation": "none"}
184	\end{lstlisting}
185	\end{small}
186	
187	\noindent
188	\textbf{Constrained-decoding schema:}
189	\begin{small}
190	\begin{lstlisting}
191	{"type": "object",
192	 "properties": {
193	   "relation": {"type": "string",
194	     "enum": [&lt;sorted_types>, "none"]}},
195	 "required": ["relation"]}
196	\end{lstlisting}
197	\end{small}
198	
199	\subsection{Type Definitions}
200	\label{sec:appendix_type_defs}
201	
202	All prompts include per-type natural-language definitions sourced from the respective dataset documentation:
203	\begin{itemize}[leftmargin=*,itemsep=2pt]
204	\item \textbf{Few-NERD:} 66 fine-grained entity types with definitions derived from the Few-NERD type ontology \cite{fewnerd-2021}.
205	\item \textbf{MAVEN:} 168 event types with FrameNet-based definitions \cite{maven-2020}.
206	\item \textbf{FewRel:} 80 relation types with Wikidata property descriptions \cite{fewrel-2018}.
207	\end{itemize}
208	
209	\noindent Type definitions are injected as ``\texttt{- \{type\_name\}: \{definition\}}'' lines in alphabetical order. The number of types per prompt varies by experimental condition (count${}= 1$ to full schema; \S\ref{sec:exp_design}).
210	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2fd9176-1850-469a-8218-2198ae6f1c49",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "15875020-6c14-490c-b785-8e52208d0880",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex",
      "content": "\\lstset{\n  basicstyle=\\ttfamily\\small,\n  breaklines=true,\n  breakatwhitespace=true,\n  columns=fullflexible\n}\n\n\\section{Prompt Templates}\n\\label{sec:appendix_prompts}\n\nThis appendix reproduces the complete prompt templates used for all three extraction tasks.\nAll prompts are injected into a single \\texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.\nBoth versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \\emph{not} included in the natural-language prompt itself.\nWe use greedy decoding (\\texttt{temperature=0}, \\texttt{seed=42}) throughout.\n\n\\medskip\\noindent\n\\textbf{Notation.}\nPlaceholders are shown in \\texttt{\\{braces\\}}.\nText \\textbf{added in v2} (relative to v1) is marked with $\\triangleright$.\nText \\textbf{removed in v2} is marked with \\sout{strikethrough}.\n\n\\subsection{Named Entity Recognition (Few-NERD)}\n\n\\paragraph{v1 prompt (with character offsets).}\n\n\\begin{small}\n\\begin{lstlisting}\nExtract all named entities from the following text.\nOnly extract entities of the following types:\n- {type_1}: {definition_1}\n- {type_2}: {definition_2}\n  ...\n\nText: {input_text}\n\nOutput as JSON: [{\"text\": \"...\", \"type\": \"...\",\n                  \"start\": ..., \"end\": ...}]\n\\end{lstlisting}\n\\end{small}\n\n\\noindent\n\\textbf{v1 constrained-decoding schema:}\n\\begin{small}\n\\begin{lstlisting}\n{\"type\": \"array\",\n \"items\": {\"type\": \"object\",\n   \"properties\": {\n     \"text\":  {\"type\": \"string\"},\n     \"type\":  {\"type\": \"string\",\n               \"enum\": [&lt;sorted_types>]},\n     \"start\": {\"type\": \"integer\"},\n     \"end\":   {\"type\": \"integer\"}},\n   \"required\": [\"text\",\"type\",\"start\",\"end\"]}}\n\\end{lstlisting}\n\\end{small}\n\n\\paragraph{v2 prompt (text+type only).}\n\n\\begin{small}\n\\begin{lstlisting}\nExtract all named entities from the following text.\nOnly extract entities of the following types:\n- {type_1}: {definition_1}\n- {type_2}: {definition_2}\n  ...\n\nText: {input_text}\n\\end{lstlisting}\n\\end{small}\n\\vspace{-0.5em}\n\\noindent$\\triangleright$~\\textbf{Added in v2:}\n\\begin{small}\n\\begin{lstlisting}\nOnly extract entities that clearly match one of the\ngiven types. If no entities of these types exist in\nthe text, output an empty list [].\n\\end{lstlisting}\n\\end{small}\n\\vspace{-0.5em}\n\\begin{small}\n\\begin{lstlisting}\nOutput as JSON: [{\"text\": \"...\", \"type\": \"...\"}]\n\\end{lstlisting}\n\\end{small}\n\n\\noindent\n\\textbf{v2 constrained-decoding schema:}\n\\begin{small}\n\\begin{lstlisting}\n{\"type\": \"array\",\n \"items\": {\"type\": \"object\",\n   \"properties\": {\n     \"text\": {\"type\": \"string\"},\n     \"type\": {\"type\": \"string\",\n              \"enum\": [&lt;sorted_types>]}},\n   \"required\": [\"text\",\"type\"]}}\n\\end{lstlisting}\n\\end{small}\n\n\\paragraph{v1 $\\to$ v2 differences (NER).}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Offset fields removed.} The \\texttt{start}/\\texttt{end} integer fields are dropped from both the natural-language instruction and the JSON schema. In v1, 96.5\\% of predicted offsets were hallucinated (\\S\\ref{sec:model}).\n\\item \\textbf{Format constraints added.} Two sentences are appended: (a)~``Only extract entities that clearly match one of the given types'' suppresses spurious predictions; (b)~``If no entities \\ldots output an empty list~\\texttt{[]}'' provides an explicit empty-output path.\n\\end{enumerate}\n\n\\subsection{Event Detection (MAVEN)}\n\n\\paragraph{v1 prompt (with character offsets).}\n\n\\begin{small}\n\\begin{lstlisting}\nExtract all event triggers from the following text.\nA trigger is the word or phrase that most clearly\nexpresses the event occurrence. Only extract triggers\nof the following event types:\n- {type_1}: {definition_1}\n- {type_2}: {definition_2}\n  ...\n\nText: {input_text}\n\nOutput as JSON: [{\"text\": \"...\", \"type\": \"...\",\n                  \"start\": ..., \"end\": ...}]\n\\end{lstlisting}\n\\end{small}\n\n\\paragraph{v2 prompt (text+type only).}\n\n\\begin{small}\n\\begin{lstlisting}\nExtract all event triggers from the following text.\nA trigger is the word or phrase that most clearly\nexpresses the event occurrence. Only extract triggers\nof the following event types:\n- {type_1}: {definition_1}\n- {type_2}: {definition_2}\n  ...\n\nText: {input_text}\n\\end{lstlisting}\n\\end{small}\n\\vspace{-0.5em}\n\\noindent$\\triangleright$~\\textbf{Added in v2:}\n\\begin{small}\n\\begin{lstlisting}\nOnly extract triggers that clearly match one of the\ngiven event types. If no events of these types exist\nin the text, output an empty list [].\n\\end{lstlisting}\n\\end{small}\n\\vspace{-0.5em}\n\\begin{small}\n\\begin{lstlisting}\nOutput as JSON: [{\"text\": \"...\", \"type\": \"...\"}]\n\\end{lstlisting}\n\\end{small}\n\n\\noindent The JSON schemas for ED are identical to the NER schemas above; only the natural-language framing differs (``event triggers'' instead of ``named entities'').\n\n\\paragraph{v1 $\\to$ v2 differences (ED).}\nSame two changes as NER: offset fields removed, format constraints added.\n\n\\subsection{Relation Extraction (FewRel)}\n\nRE uses only a v2-style prompt (no offset fields are applicable to classification).\n\n\\paragraph{Prompt.}\n\n\\begin{small}\n\\begin{lstlisting}\nGiven the following sentence and two entities,\nclassify the relation between them.\n\nSentence: \"{sentence}\"\nHead entity: \"{head_entity}\"\nTail entity: \"{tail_entity}\"\n\nCandidate relations: {type_1}, {type_2}, ...\n\nOutput a single JSON object:\n  {\"relation\": \"&lt;relation_type>\"}\nIf none of the candidate relations apply, output:\n  {\"relation\": \"none\"}\n\\end{lstlisting}\n\\end{small}\n\n\\noindent\n\\textbf{Constrained-decoding schema:}\n\\begin{small}\n\\begin{lstlisting}\n{\"type\": \"object\",\n \"properties\": {\n   \"relation\": {\"type\": \"string\",\n     \"enum\": [&lt;sorted_types>, \"none\"]}},\n \"required\": [\"relation\"]}\n\\end{lstlisting}\n\\end{small}\n\n\\subsection{Type Definitions}\n\\label{sec:appendix_type_defs}\n\nAll prompts include per-type natural-language definitions sourced from the respective dataset documentation:\n\\begin{itemize}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Few-NERD:} 66 fine-grained entity types with definitions derived from the Few-NERD type ontology \\cite{fewnerd-2021}.\n\\item \\textbf{MAVEN:} 168 event types with FrameNet-based definitions \\cite{maven-2020}.\n\\item \\textbf{FewRel:} 80 relation types with Wikidata property descriptions \\cite{fewrel-2018}.\n\\end{itemize}\n\n\\noindent Type definitions are injected as ``\\texttt{- \\{type\\_name\\}: \\{definition\\}}'' lines in alphabetical order. The number of types per prompt varies by experimental condition (count${}= 1$ to full schema; \\S\\ref{sec:exp_design}).\n",
      "numLines": 210,
      "startLine": 1,
      "totalLines": 210
    }
  },
  "sourceToolAssistantUUID": "b2fd9176-1850-469a-8218-2198ae6f1c49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-17T14:15:29.305Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HDCxp9o426z76iLFXJVsRA`</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines page limits appendix ethics review checklist",
  "allowed_domains": [
    "aclrollingreview.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15875020-6c14-490c-b785-8e52208d0880",
  "isSidechain": false,
  "requestId": "req_011Cb8HHFYBs584aLmm4KqMT",
  "type": "assistant",
  "uuid": "b5b0e6d0-8940-47db-b26c-64632ec5eaf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQZ4ABfcgTVRJB8tfrYeUY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 34,
      "cache_creation_input_tokens": 16692,
      "cache_read_input_tokens": 57920,
      "output_tokens": 673,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 34,
          "output_tokens": 673,
          "cache_read_input_tokens": 57920,
          "cache_creation_input_tokens": 16692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16692
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

_source line 64_

```json
{
  "type": "last-prompt",
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: schema-dag-extraction - 论文路径: projects/schema-dag-extraction/docs/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: Main Conference - 截止日期: 2026-05-25  请 `Read /home/ubun…",
  "leafUuid": "b5b0e6d0-8940-47db-b26c-64632ec5eaf7",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a"
}
```

---

### Runtime record

_source line 65_

```json
{
  "type": "ai-title",
  "aiTitle": "Review schema-dag-extraction paper for EMNLP 2026",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a"
}
```

---

### Tool result

_source line 66 · 2026-05-17T14:15:38.112Z_

<details><summary>↩ Tool result · `toolu_01HDCxp9o426z76iLFXJVsRA`</summary>

```text
Web search results for query: "ACL Rolling Review 2026 author guidelines page limits appendix ethics review checklist"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Let me search for more specific information about page limits and the ethics review checklist.

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Discontinuation of the MS Word Template – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/discontinuation-word-template"}]

Links: [{"title":"ARR Responsible NLP Research checklist","url":"http://aclrollingreview.org/responsibleNLPresearch/"},{"title":"Responsible NLP Research Checklist","url":"https://aclrollingreview.org/static/responsibleNLPresearch.pdf"},{"title":"Guidelines for Ethics Reviewing","url":"http://aclrollingreview.org/ethicsreviewertutorial"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2025 to include Responsible NLP Checklists as Paper Appendices – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/responsible-nlp-checklist-appendices"},{"title":"ACL ARR Ethics Review Flagging Guidelines","url":"http://aclrollingreview.org/ethics-flagging-guidelines/"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Arr Changes December – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/ARR-changes-December/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on my web search results, I've found comprehensive information about ACL Rolling Review 2026 author guidelines. Here's what I found:

## Page Limits

Short papers have a maximum of 4 content pages, while long papers have a maximum of 8 content pages. Sections on ethical considerations and limitations do not count towards the page limit.

## Appendix Guidelines

Appendices should come after the references in the submitted PDF and do not count towards the page limit. Appendices should follow the official double-column format, with exceptions covered by the ACLPUB guidelines. Additionally, starting from July 2025, papers with appendices not following the double column format (except if covered by the approved exceptions) will be desk rejected.

## Ethics Review Checklist (Responsible NLP Research Checklist)

The submission form includes the responsible NLP research checklist with detailed explanations of all its questions available. Starting from December 2024, inappropriately filled checklist can be considered grounds for desk rejection. Checklists do not count against page limits and are included as an appendix.

Common issues with the checklist include just saying 'yes' for all questions, even those not relevant for your paper, and failing to provide section numbers, justifications or extra information when needed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5b0e6d0-8940-47db-b26c-64632ec5eaf7",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "78f74dd4-e438-48f8-8d4d-aa4e438345af",
  "toolUseResult": {
    "query": "ACL Rolling Review 2026 author guidelines page limits appendix ethics review checklist",
    "results": [
      {
        "tool_use_id": "srvtoolu_013ktybsW7YTjgNnLghidL8r",
        "content": [
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewerguidelines"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authorchecklist"
          },
          {
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/"
          },
          {
            "title": "Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/submissionform"
          },
          {
            "title": "ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/acguidelines"
          },
          {
            "title": "How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewing"
          },
          {
            "title": "ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/changelog"
          },
          {
            "title": "Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/incentives2026"
          }
        ]
      },
      "Let me search for more specific information about page limits and the ethics review checklist.",
      {
        "tool_use_id": "srvtoolu_01N4gbXNd87L29b3tr7AW9Q1",
        "content": [
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authorchecklist"
          },
          {
            "title": "ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/acguidelines"
          },
          {
            "title": "How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewing"
          },
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/changelog"
          },
          {
            "title": "Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/submissionform"
          },
          {
            "title": "ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewerguidelines"
          },
          {
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/"
          },
          {
            "title": "Discontinuation of the MS Word Template – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/discontinuation-word-template"
          }
        ]
      },
      {
        "tool_use_id": "srvtoolu_018g5fGXw6xFv9gwRwkzeoo2",
        "content": [
          {
            "title": "ARR Responsible NLP Research checklist",
            "url": "http://aclrollingreview.org/responsibleNLPresearch/"
          },
          {
            "title": "Responsible NLP Research Checklist",
            "url": "https://aclrollingreview.org/static/responsibleNLPresearch.pdf"
          },
          {
            "title": "Guidelines for Ethics Reviewing",
            "url": "http://aclrollingreview.org/ethicsreviewertutorial"
          },
          {
            "title": "Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authorchecklist"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "EMNLP 2025 to include Responsible NLP Checklists as Paper Appendices – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/responsible-nlp-checklist-appendices"
          },
          {
            "title": "ACL ARR Ethics Review Flagging Guidelines",
            "url": "http://aclrollingreview.org/ethics-flagging-guidelines/"
          },
          {
            "title": "ARR Reviewer Guidelines",
            "url": "http://aclrollingreview.org/reviewerguidelines"
          },
          {
            "title": "Arr Changes December – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/ARR-changes-December/"
          },
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          }
        ]
      },
      "Based on my web search results, I've found comprehensive information about ACL Rolling Review 2026 author guidelines. Here's what I found:\n\n## Page Limits\n\nShort papers have a maximum of 4 content pages, while long papers have a maximum of 8 content pages. Sections on ethical considerations and limitations do not count towards the page limit.\n\n## Appendix Guidelines\n\nAppendices should come after the references in the submitted PDF and do not count towards the page limit. Appendices should follow the official double-column format, with exceptions covered by the ACLPUB guidelines. Additionally, starting from July 2025, papers with appendices not following the double column format (except if covered by the approved exceptions) will be desk rejected.\n\n## Ethics Review Checklist (Responsible NLP Research Checklist)\n\nThe submission form includes the responsible NLP research checklist with detailed explanations of all its questions available. Starting from December 2024, inappropriately filled checklist can be considered grounds for desk rejection. Checklists do not count against page limits and are included as an appendix.\n\nCommon issues with the checklist include just saying 'yes' for all questions, even those not relevant for your paper, and failing to provide section numbers, justifications or extra information when needed."
    ],
    "durationSeconds": 8.803116766999999
  },
  "sourceToolAssistantUUID": "b5b0e6d0-8940-47db-b26c-64632ec5eaf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-17T14:15:41.211Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me also check external review configuration.

Let me now check the project config for external review settings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78f74dd4-e438-48f8-8d4d-aa4e438345af",
  "isSidechain": false,
  "requestId": "req_011Cb8HK3HYz1yjku9kUbXt5",
  "type": "assistant",
  "uuid": "a06386db-c022-4ca3-b535-da62d5aa67af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XuFcHWbzfDJQwn9m5Uv84T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5073,
      "cache_read_input_tokens": 74612,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5073,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 74612,
          "cache_creation_input_tokens": 5073,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5073
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

_source line 68 · 2026-05-17T14:15:42.218Z_

检查外部审稿配置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a06386db-c022-4ca3-b535-da62d5aa67af",
  "isSidechain": false,
  "requestId": "req_011Cb8HK3HYz1yjku9kUbXt5",
  "type": "assistant",
  "uuid": "dd88ffff-faf4-47ca-86ca-de1c733ce77d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XuFcHWbzfDJQwn9m5Uv84T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5073,
      "cache_read_input_tokens": 74612,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5073,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 74612,
          "cache_creation_input_tokens": 5073,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5073
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

_source line 69 · 2026-05-17T14:15:43.234Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PHUASBcNXhoLH6Jg3xAbWp`</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "decisions.yaml",
  "max_chars": 5000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd88ffff-faf4-47ca-86ca-de1c733ce77d",
  "isSidechain": false,
  "requestId": "req_011Cb8HK3HYz1yjku9kUbXt5",
  "type": "assistant",
  "uuid": "36f01463-04ac-4e3e-885b-b5fef23a1ce2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XuFcHWbzfDJQwn9m5Uv84T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5073,
      "cache_read_input_tokens": 74612,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5073,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 74612,
          "cache_creation_input_tokens": 5073,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5073
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

_source line 70 · 2026-05-17T14:15:43.250Z_

<details><summary>↩ Tool result · `toolu_01PHUASBcNXhoLH6Jg3xAbWp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/decisions.yaml\", \"content\": \"_next_id: 57\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 16:10 UTC\\n  summary: 项目立项，MVP 验证方案：Experiment 2 (Confusability Controlled) 为核心验证实验\\n  rationale: 'IDEA_BRIEF 的核心假设是 type confusability 独立于 type count 驱动 LLM IE 质量下降。Experiment\\n    2（固定 count 变 BCS）是最直接的假设检验。Pass 标准: |r|≥0.3 且 p<0.05。ACE05 RE + Few-NERD 双数据集验证。ARR\\n    May 25 DDL（11天），MVP 需 1-2 天完成。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 16:15 UTC\\n  summary: 修正 MVP 统计设计：random samples 从 10 增至 25/档，加入 per-type solo baseline 控制变量，核心指标改为\\n    Δ(solo_F1 - batch_F1)\\n  rationale: Reviewer 指出 n=12 下 |r|=0.3 对应 p≈0.34，无法同时满足 |r|≥0.3 且 p<0.05。增至 25 random\\n    batches/档 → n≈54，|r|≥0.27 即可达 p<0.05。同时加入 solo F1 控制 type 固有难度，避免将\\\"类型本身难抽取\\\"误归因于\\\"confusability\\n    效应\\\"。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 23:11 UTC\\n  summary: MVP 分析方法从 Δ(solo-batch) 切换到 within-count Pearson r(F1, BCS)，pass 标准更新为\\n    |r|≥0.3 at fixed count\\n  rationale: Exp 1 发现 count curve 方向反转（F1 随 count 上升），根因是低 count 时模型过度 hallucinate（pred/gold=8x\\n    at count=1）。solo baseline 处于极端行为模式，Δ 被跨 count 行为差异污染。改为 within-count 对比更干净：同一\\n    count 下比较不同 BCS 的 F1，直接检验 confusability 独立效应。\\n  related_experiments:\\n  - exp_id: exp001_count_baseline\\n    role: evidence\\n    result: count curve reversed, hallucination at low count\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 23:31 UTC\\n  summary: MVP 主指标更新为 within-count r(recall, BCS)，F1 因 over-prediction confound 降为补充指标\\n  rationale: Exp 1 text-match 重评估发现：recall 单调下降（0.72→0.42，符合预期），precision 单调上升（0.11→0.52，over-prediction\\n    减少），F1 受 precision 主导而反转。within-count 分析中 precision confound 在同一 count 下近似恒定，F1\\n    仍可用；但 recall 更干净且直接反映 type confusion。WrongType 错误（text 正确但 type 错标）随 count 从 0\\n    升至 2434，直接支持 confusability 假设。\\n  related_experiments:\\n  - exp_id: exp001_count_baseline\\n    role: evidence\\n    result: recall monotonically decreases with count; WrongType errors increase;\\n      over-prediction confounds F1\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-15 02:34 UTC\\n  summary: 'MVP PASS（refined mechanism）: confusability 通过 type confusion 通道驱动降级，选择\\n    Narrative A (multi-channel degradation model)'\\n  rationale: Exp 2 结果：recall vs BCS 不显著（r=0.25, p=0.066），但 F1 vs BCS 在 count_12 显著（r=0.50,\\n    p=0.008），偏相关 r=0.30 p=0.026 达到 pass 标准。Confusion rate high-BCS vs low-BCS 差异 30-40x（p=0.043）。机制清晰：confusability\\n    不导致遗漏，而是导致错标。选 Narrative A（multi-channel）因为：(1) 用上所有数据（exp1 count→recall + exp2\\n    BCS→confusion）(2) 两个正交机制 story 更丰富 (3) SDGD 框架天然需要同时处理 count 和 confusability。\\n  related_experiments:\\n  - exp_id: exp001_count_baseline\\n    role: evidence\\n    result: count drives recall decline 0.72→0.42\\n  - exp_id: exp002_confusability_controlled\\n    role: evidence\\n    result: BCS drives type confusion 30-40x, F1 partial r=0.30 p=0.026\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-15 04:04 UTC\\n  summary: 跳过 Dream 模拟，直接批准 P0 实验\\n  rationale: 'Dream 模拟因基础设施 bug 崩溃（TypeError: _run_dream_pipeline() got unexpected\\n    keyword argument ''operational_chat_id''），P0 实验已被阻塞 9+ 小时。这是平台问题不是项目问题，不应阻塞研究进度。paper_framing.md\\n    和 experiment_plan.yaml 已完成，方向清晰，可直接推进。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D007\\n  date: 2026-05-15 04:16 UTC\\n  summary: RE 第三任务需先做 BCS pilot 验证，不直接 commit\\n  rationale: Reviewer 指出 RE 的 confusability 机制与 NER/ED 可能不同——RE type confusion 取决于\\n    entity pair 语义角色而非 relation label embedding 相似度。如果 BCS 在 RE 上不 work，反而削弱 task-agnostic\\n    claim。策略：先花 1h 做 FewRel type 的 BCS 矩阵 + 小规模 pilot（5 batches），确认信号存在再 commit P0；信号不存在则\\n    claim 缩窄为 span-level IE，在 limitation 中承认。\\n  related_experiments: []\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-15 05:10 UTC\\n  summary: 重构证据层级：pairwise 分析升为主要证据，batch-level 需控制 type frequency\\n  rationale: exp003a v2 Reviewer 独立核实发现 within-count BCS-F1 正相关（高 BCS→高 F1），与假设方向相反。根因：type\\n    frequency 混淆变量（高频类型既有高 BCS 又被模型更好提取）。pairwise 分析（r=0.156, p=4.6e-12）不受此影响，仍成立。需要：(1)\\n    pairwise 升为 Channel 1 主要证据 (2) 新增 per-type F1 分析控制频率 (3) batch-level 正相关在论文中透明报告并解释混淆变量。\\n  related_experiments:\\n  - exp_id: exp003a\\n    role: trigger\\n    result: within-count r>0 contradicts hypothesis direction\\n  depends_on:\\n  - D006\\n- id: D009\\n  date: 2026-05-15 07:21 UTC\\n  summary: 'Paper story reframe: BCS proxy task-specific → SDGD-cal empirical calibration\\n    成为核心贡献'\\n  rationale: MAVEN per-type 分析显示 BCS 与 F1 正相关（ρ=+0.184, p=0.025），与 Few-NERD 方向相反且已排除\\n    frequency confound。说明 embedding-based BCS 是 task-specific proxy：对 NER 有效（type\\n    name 相似度驱动 confusion），对 ED 无效（trigger word 歧义驱动 confusion，非 type name embedding\\n    距离）。Reframe 方向：BCS proxy 有局限 → 需要 empirical confusability（从 actual confusion matrix\\n    推导）→ SDGD-cal 用 empirical calibration 解决跨任务泛化。这让 SDGD-cal 成为比 SDGD-zero 更核心的贡献。\\n  related_experiments:\\n  - exp_id: exp004_maven_bcs\\n    role: trigger\\n    result: MAVEN per-type ρ=+0.184 contradicts hypothesis\\n  - exp_id: exp003a_prompt_v2_rerun\\n    role: baseline\\n    result: Few-NERD per-type ρ=-0.293 supports hypothesis\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-15 07:37 UTC\\n\\n\\n... [截断: 省略 31307 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 36307, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36f01463-04ac-4e3e-885b-b5fef23a1ce2",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "cf444e64-5418-4a9e-9853-9c7b11baeb92",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/decisions.yaml\\\", \\\"content\\\": \\\"_next_id: 57\\\\ndecisions:\\\\n- id: D001\\\\n  date: 2026-05-14 16:10 UTC\\\\n  summary: 项目立项，MVP 验证方案：Experiment 2 (Confusability Controlled) 为核心验证实验\\\\n  rationale: 'IDEA_BRIEF 的核心假设是 type confusability 独立于 type count 驱动 LLM IE 质量下降。Experiment\\\\n    2（固定 count 变 BCS）是最直接的假设检验。Pass 标准: |r|≥0.3 且 p<0.05。ACE05 RE + Few-NERD 双数据集验证。ARR\\\\n    May 25 DDL（11天），MVP 需 1-2 天完成。'\\\\n  related_experiments: []\\\\n  depends_on: []\\\\n- id: D002\\\\n  date: 2026-05-14 16:15 UTC\\\\n  summary: 修正 MVP 统计设计：random samples 从 10 增至 25/档，加入 per-type solo baseline 控制变量，核心指标改为\\\\n    Δ(solo_F1 - batch_F1)\\\\n  rationale: Reviewer 指出 n=12 下 |r|=0.3 对应 p≈0.34，无法同时满足 |r|≥0.3 且 p<0.05。增至 25 random\\\\n    batches/档 → n≈54，|r|≥0.27 即可达 p<0.05。同时加入 solo F1 控制 type 固有难度，避免将\\\\\\\"类型本身难抽取\\\\\\\"误归因于\\\\\\\"confusability\\\\n    效应\\\\\\\"。\\\\n  related_experiments: []\\\\n  depends_on:\\\\n  - D001\\\\n- id: D003\\\\n  date: 2026-05-14 23:11 UTC\\\\n  summary: MVP 分析方法从 Δ(solo-batch) 切换到 within-count Pearson r(F1, BCS)，pass 标准更新为\\\\n    |r|≥0.3 at fixed count\\\\n  rationale: Exp 1 发现 count curve 方向反转（F1 随 count 上升），根因是低 count 时模型过度 hallucinate（pred/gold=8x\\\\n    at count=1）。solo baseline 处于极端行为模式，Δ 被跨 count 行为差异污染。改为 within-count 对比更干净：同一\\\\n    count 下比较不同 BCS 的 F1，直接检验 confusability 独立效应。\\\\n  related_experiments:\\\\n  - exp_id: exp001_count_baseline\\\\n    role: evidence\\\\n    result: count curve reversed, hallucination at low count\\\\n  depends_on:\\\\n  - D002\\\\n- id: D004\\\\n  date: 2026-05-14 23:31 UTC\\\\n  summary: MVP 主指标更新为 within-count r(recall, BCS)，F1 因 over-prediction confound 降为补充指标\\\\n  rationale: Exp 1 text-match 重评估发现：recall 单调下降（0.72→0.42，符合预期），precision 单调上升（0.11→0.52，over-prediction\\\\n    减少），F1 受 precision 主导而反转。within-count 分析中 precision confound 在同一 count 下近似恒定，F1\\\\n    仍可用；但 recall 更干净且直接反映 type confusion。WrongType 错误（text 正确但 type 错标）随 count 从 0\\\\n    升至 2434，直接支持 confusability 假设。\\\\n  related_experiments:\\\\n  - exp_id: exp001_count_baseline\\\\n    role: evidence\\\\n    result: recall monotonically decreases with count; WrongType errors increase;\\\\n      over-prediction confounds F1\\\\n  depends_on:\\\\n  - D003\\\\n- id: D005\\\\n  date: 2026-05-15 02:34 UTC\\\\n  summary: 'MVP PASS（refined mechanism）: confusability 通过 type confusion 通道驱动降级，选择\\\\n    Narrative A (multi-channel degradation model)'\\\\n  rationale: Exp 2 结果：recall vs BCS 不显著（r=0.25, p=0.066），但 F1 vs BCS 在 count_12 显著（r=0.50,\\\\n    p=0.008），偏相关 r=0.30 p=0.026 达到 pass 标准。Confusion rate high-BCS vs low-BCS 差异 30-40x（p=0.043）。机制清晰：confusability\\\\n    不导致遗漏，而是导致错标。选 Narrative A（multi-channel）因为：(1) 用上所有数据（exp1 count→recall + exp2\\\\n    BCS→confusion）(2) 两个正交机制 story 更丰富 (3) SDGD 框架天然需要同时处理 count 和 confusability。\\\\n  related_experiments:\\\\n  - exp_id: exp001_count_baseline\\\\n    role: evidence\\\\n    result: count drives recall decline 0.72→0.42\\\\n  - exp_id: exp002_confusability_controlled\\\\n    role: evidence\\\\n    result: BCS drives type confusion 30-40x, F1 partial r=0.30 p=0.026\\\\n  depends_on:\\\\n  - D004\\\\n- id: D006\\\\n  date: 2026-05-15 04:04 UTC\\\\n  summary: 跳过 Dream 模拟，直接批准 P0 实验\\\\n  rationale: 'Dream 模拟因基础设施 bug 崩溃（TypeError: _run_dream_pipeline() got unexpected\\\\n    keyword argument ''operational_chat_id''），P0 实验已被阻塞 9+ 小时。这是平台问题不是项目问题，不应阻塞研究进度。paper_framing.md\\\\n    和 experiment_plan.yaml 已完成，方向清晰，可直接推进。'\\\\n  related_experiments: []\\\\n  depends_on: []\\\\n- id: D007\\\\n  date: 2026-05-15 04:16 UTC\\\\n  summary: RE 第三任务需先做 BCS pilot 验证，不直接 commit\\\\n  rationale: Reviewer 指出 RE 的 confusability 机制与 NER/ED 可能不同——RE type confusion 取决于\\\\n    entity pair 语义角色而非 relation label embedding 相似度。如果 BCS 在 RE 上不 work，反而削弱 task-agnostic\\\\n    claim。策略：先花 1h 做 FewRel type 的 BCS 矩阵 + 小规模 pilot（5 batches），确认信号存在再 commit P0；信号不存在则\\\\n    claim 缩窄为 span-level IE，在 limitation 中承认。\\\\n  related_experiments: []\\\\n  depends_on:\\\\n  - D006\\\\n- id: D008\\\\n  date: 2026-05-15 05:10 UTC\\\\n  summary: 重构证据层级：pairwise 分析升为主要证据，batch-level 需控制 type frequency\\\\n  rationale: exp003a v2 Reviewer 独立核实发现 within-count BCS-F1 正相关（高 BCS→高 F1），与假设方向相反。根因：type\\\\n    frequency 混淆变量（高频类型既有高 BCS 又被模型更好提取）。pairwise 分析（r=0.156, p=4.6e-12）不受此影响，仍成立。需要：(1)\\\\n    pairwise 升为 Channel 1 主要证据 (2) 新增 per-type F1 分析控制频率 (3) batch-level 正相关在论文中透明报告并解释混淆变量。\\\\n  related_experiments:\\\\n  - exp_id: exp003a\\\\n    role: trigger\\\\n    result: within-count r>0 contradicts hypothesis direction\\\\n  depends_on:\\\\n  - D006\\\\n- id: D009\\\\n  date: 2026-05-15 07:21 UTC\\\\n  summary: 'Paper story reframe: BCS proxy task-specific → SDGD-cal empirical calibration\\\\n    成为核心贡献'\\\\n  rationale: MAVEN per-type 分析显示 BCS 与 F1 正相关（ρ=+0.184, p=0.025），与 Few-NERD 方向相反且已排除\\\\n    frequency confound。说明 embedding-based BCS 是 task-specific proxy：对 NER 有效（type\\\\n    name 相似度驱动 confusion），对 ED 无效（trigger word 歧义驱动 confusion，非 type name embedding\\\\n    距离）。Reframe 方向：BCS proxy 有局限 → 需要 empirical confusability（从 actual confusion matrix\\\\n    推导）→ SDGD-cal 用 empirical calibration 解决跨任务泛化。这让 SDGD-cal 成为比 SDGD-zero 更核心的贡献。\\\\n  related_experiments:\\\\n  - exp_id: exp004_maven_bcs\\\\n    role: trigger\\\\n    result: MAVEN per-type ρ=+0.184 contradicts hypothesis\\\\n  - exp_id: exp003a_prompt_v2_rerun\\\\n    role: baseline\\\\n    result: Few-NERD per-type ρ=-0.293 supports hypothesis\\\\n  depends_on:\\\\n  - D008\\\\n- id: D010\\\\n  date: 2026-05-15 07:37 UTC\\\\n\\\\n\\\\n... [截断: 省略 31307 字符，传 max_chars=0 获取完整内容]\\\", \\\"total_chars\\\": 36307, \\\"truncated\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/decisions.yaml\", \"content\": \"_next_id: 57\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 16:10 UTC\\n  summary: 项目立项，MVP 验证方案：Experiment 2 (Confusability Controlled) 为核心验证实验\\n  rationale: 'IDEA_BRIEF 的核心假设是 type confusability 独立于 type count 驱动 LLM IE 质量下降。Experiment\\n    2（固定 count 变 BCS）是最直接的假设检验。Pass 标准: |r|≥0.3 且 p<0.05。ACE05 RE + Few-NERD 双数据集验证。ARR\\n    May 25 DDL（11天），MVP 需 1-2 天完成。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 16:15 UTC\\n  summary: 修正 MVP 统计设计：random samples 从 10 增至 25/档，加入 per-type solo baseline 控制变量，核心指标改为\\n    Δ(solo_F1 - batch_F1)\\n  rationale: Reviewer 指出 n=12 下 |r|=0.3 对应 p≈0.34，无法同时满足 |r|≥0.3 且 p<0.05。增至 25 random\\n    batches/档 → n≈54，|r|≥0.27 即可达 p<0.05。同时加入 solo F1 控制 type 固有难度，避免将\\\"类型本身难抽取\\\"误归因于\\\"confusability\\n    效应\\\"。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 23:11 UTC\\n  summary: MVP 分析方法从 Δ(solo-batch) 切换到 within-count Pearson r(F1, BCS)，pass 标准更新为\\n    |r|≥0.3 at fixed count\\n  rationale: Exp 1 发现 count curve 方向反转（F1 随 count 上升），根因是低 count 时模型过度 hallucinate（pred/gold=8x\\n    at count=1）。solo baseline 处于极端行为模式，Δ 被跨 count 行为差异污染。改为 within-count 对比更干净：同一\\n    count 下比较不同 BCS 的 F1，直接检验 confusability 独立效应。\\n  related_experiments:\\n  - exp_id: exp001_count_baseline\\n    role: evidence\\n    result: count curve reversed, hallucination at low count\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 23:31 UTC\\n  summary: MVP 主指标更新为 within-count r(recall, BCS)，F1 因 over-prediction confound 降为补充指标\\n  rationale: Exp 1 text-match 重评估发现：recall 单调下降（0.72→0.42，符合预期），precision 单调上升（0.11→0.52，over-prediction\\n    减少），F1 受 precision 主导而反转。within-count 分析中 precision confound 在同一 count 下近似恒定，F1\\n    仍可用；但 recall 更干净且直接反映 type confusion。WrongType 错误（text 正确但 type 错标）随 count 从 0\\n    升至 2434，直接支持 confusability 假设。\\n  related_experiments:\\n  - exp_id: exp001_count_baseline\\n    role: evidence\\n    result: recall monotonically decreases with count; WrongType errors increase;\\n      over-prediction confounds F1\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-15 02:34 UTC\\n  summary: 'MVP PASS（refined mechanism）: confusability 通过 type confusion 通道驱动降级，选择\\n    Narrative A (multi-channel degradation model)'\\n  rationale: Exp 2 结果：recall vs BCS 不显著（r=0.25, p=0.066），但 F1 vs BCS 在 count_12 显著（r=0.50,\\n    p=0.008），偏相关 r=0.30 p=0.026 达到 pass 标准。Confusion rate high-BCS vs low-BCS 差异 30-40x（p=0.043）。机制清晰：confusability\\n    不导致遗漏，而是导致错标。选 Narrative A（multi-channel）因为：(1) 用上所有数据（exp1 count→recall + exp2\\n    BCS→confusion）(2) 两个正交机制 story 更丰富 (3) SDGD 框架天然需要同时处理 count 和 confusability。\\n  related_experiments:\\n  - exp_id: exp001_count_baseline\\n    role: evidence\\n    result: count drives recall decline 0.72→0.42\\n  - exp_id: exp002_confusability_controlled\\n    role: evidence\\n    result: BCS drives type confusion 30-40x, F1 partial r=0.30 p=0.026\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-15 04:04 UTC\\n  summary: 跳过 Dream 模拟，直接批准 P0 实验\\n  rationale: 'Dream 模拟因基础设施 bug 崩溃（TypeError: _run_dream_pipeline() got unexpected\\n    keyword argument ''operational_chat_id''），P0 实验已被阻塞 9+ 小时。这是平台问题不是项目问题，不应阻塞研究进度。paper_framing.md\\n    和 experiment_plan.yaml 已完成，方向清晰，可直接推进。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D007\\n  date: 2026-05-15 04:16 UTC\\n  summary: RE 第三任务需先做 BCS pilot 验证，不直接 commit\\n  rationale: Reviewer 指出 RE 的 confusability 机制与 NER/ED 可能不同——RE type confusion 取决于\\n    entity pair 语义角色而非 relation label embedding 相似度。如果 BCS 在 RE 上不 work，反而削弱 task-agnostic\\n    claim。策略：先花 1h 做 FewRel type 的 BCS 矩阵 + 小规模 pilot（5 batches），确认信号存在再 commit P0；信号不存在则\\n    claim 缩窄为 span-level IE，在 limitation 中承认。\\n  related_experiments: []\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-15 05:10 UTC\\n  summary: 重构证据层级：pairwise 分析升为主要证据，batch-level 需控制 type frequency\\n  rationale: exp003a v2 Reviewer 独立核实发现 within-count BCS-F1 正相关（高 BCS→高 F1），与假设方向相反。根因：type\\n    frequency 混淆变量（高频类型既有高 BCS 又被模型更好提取）。pairwise 分析（r=0.156, p=4.6e-12）不受此影响，仍成立。需要：(1)\\n    pairwise 升为 Channel 1 主要证据 (2) 新增 per-type F1 分析控制频率 (3) batch-level 正相关在论文中透明报告并解释混淆变量。\\n  related_experiments:\\n  - exp_id: exp003a\\n    role: trigger\\n    result: within-count r>0 contradicts hypothesis direction\\n  depends_on:\\n  - D006\\n- id: D009\\n  date: 2026-05-15 07:21 UTC\\n  summary: 'Paper story reframe: BCS proxy task-specific → SDGD-cal empirical calibration\\n    成为核心贡献'\\n  rationale: MAVEN per-type 分析显示 BCS 与 F1 正相关（ρ=+0.184, p=0.025），与 Few-NERD 方向相反且已排除\\n    frequency confound。说明 embedding-based BCS 是 task-specific proxy：对 NER 有效（type\\n    name 相似度驱动 confusion），对 ED 无效（trigger word 歧义驱动 confusion，非 type name embedding\\n    距离）。Reframe 方向：BCS proxy 有局限 → 需要 empirical confusability（从 actual confusion matrix\\n    推导）→ SDGD-cal 用 empirical calibration 解决跨任务泛化。这让 SDGD-cal 成为比 SDGD-zero 更核心的贡献。\\n  related_experiments:\\n  - exp_id: exp004_maven_bcs\\n    role: trigger\\n    result: MAVEN per-type ρ=+0.184 contradicts hypothesis\\n  - exp_id: exp003a_prompt_v2_rerun\\n    role: baseline\\n    result: Few-NERD per-type ρ=-0.293 supports hypothesis\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-15 07:37 UTC\\n\\n\\n... [截断: 省略 31307 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 36307, \"truncated\": true}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "36f01463-04ac-4e3e-885b-b5fef23a1ce2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-17T14:15:43.403Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status · `toolu_01MYSFQJQNaQpvM4ipMoQFMs`</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf444e64-5418-4a9e-9853-9c7b11baeb92",
  "isSidechain": false,
  "requestId": "req_011Cb8HK3HYz1yjku9kUbXt5",
  "type": "assistant",
  "uuid": "16b9cc85-300d-4bd2-b203-eddc6f38e58d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XuFcHWbzfDJQwn9m5Uv84T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5073,
      "cache_read_input_tokens": 74612,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5073,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 74612,
          "cache_creation_input_tokens": 5073,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5073
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

_source line 72 · 2026-05-17T14:15:43.425Z_

<details><summary>↩ Tool result · `toolu_01MYSFQJQNaQpvM4ipMoQFMs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16b9cc85-300d-4bd2-b203-eddc6f38e58d",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "c151889b-ab40-457c-8275-dc0661193d1a",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"status\\\": \\\"not_requested\\\", \\\"message\\\": \\\"No external review requested.\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "16b9cc85-300d-4bd2-b203-eddc6f38e58d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 73_

```json
{
  "type": "last-prompt",
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: schema-dag-extraction - 论文路径: projects/schema-dag-extraction/docs/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: Main Conference - 截止日期: 2026-05-25  请 `Read /home/ubun…",
  "leafUuid": "c151889b-ab40-457c-8275-dc0661193d1a",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a"
}
```

---

### Runtime record

_source line 74_

```json
{
  "type": "ai-title",
  "aiTitle": "Review schema-dag-extraction paper for EMNLP 2026",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a"
}
```

---

### Assistant

_source line 75 · 2026-05-17T14:15:53.696Z_

<details><summary>Logged reasoning block</summary>

```text
External review status is "not_requested" and I need to check if the project config has external review enabled. Let me check the project config.

Actually, I think I should just check whether external review is enabled in the project config. Let me look for the project config.

But actually, I have enough information to proceed. Let me now set up the review process:

1. Venue info gathered: EMNLP 2026, through ARR, May 25 deadline, 8 pages long / 4 pages short, double-blind, ACL template, mandatory Limitations section
2. Paper exists and is readable - multi-file LaTeX


3. No existing review_issues.yaml

For EMNLP 2026, I'll assign two reviewers with complementary expertise: one focused on methodological rigor and experimental validity, the other on novelty, completeness, and presentation quality. Let me check the project config to see if external review is enabled before proceeding.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c151889b-ab40-457c-8275-dc0661193d1a",
  "isSidechain": false,
  "requestId": "req_011Cb8HKSERwE31gLYYUJqEm",
  "type": "assistant",
  "uuid": "e67eeb64-d3fa-42f2-8f9f-0cc1cb45fe37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKJpfLr9zhFvwcGwnGvYPD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3153,
      "cache_read_input_tokens": 79685,
      "output_tokens": 437,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3153,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 437,
          "cache_read_input_tokens": 79685,
          "cache_creation_input_tokens": 3153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3153
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

_source line 76 · 2026-05-17T14:15:53.696Z_

检查项目外部审稿配置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e67eeb64-d3fa-42f2-8f9f-0cc1cb45fe37",
  "isSidechain": false,
  "requestId": "req_011Cb8HKSERwE31gLYYUJqEm",
  "type": "assistant",
  "uuid": "5c51ce37-a02b-46e2-ae56-00f034f3b305",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKJpfLr9zhFvwcGwnGvYPD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3153,
      "cache_read_input_tokens": 79685,
      "output_tokens": 437,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3153,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 437,
          "cache_read_input_tokens": 79685,
          "cache_creation_input_tokens": 3153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3153
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

_source line 77 · 2026-05-17T14:15:53.750Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01V1VKyr1okDXecBJ8uZ1eX6`</summary>

```json
{
  "pattern": "projects/schema-dag-extraction/**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c51ce37-a02b-46e2-ae56-00f034f3b305",
  "isSidechain": false,
  "requestId": "req_011Cb8HKSERwE31gLYYUJqEm",
  "type": "assistant",
  "uuid": "e3325b7b-a5d9-4d72-9ac9-c83e5e01b0a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKJpfLr9zhFvwcGwnGvYPD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3153,
      "cache_read_input_tokens": 79685,
      "output_tokens": 437,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3153,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 437,
          "cache_read_input_tokens": 79685,
          "cache_creation_input_tokens": 3153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3153
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

_source line 78 · 2026-05-17T14:15:53.786Z_

<details><summary>↩ Tool result · `toolu_01V1VKyr1okDXecBJ8uZ1eX6`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3325b7b-a5d9-4d72-9ac9-c83e5e01b0a3",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "daf11913-cb56-4536-a434-1be56792249f",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 31,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "e3325b7b-a5d9-4d72-9ac9-c83e5e01b0a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-17T14:15:57.609Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01XEzChrfaCHgZCjNih3Fimo`</summary>

```json
{
  "pattern": "projects/schema-dag-extraction/**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "daf11913-cb56-4536-a434-1be56792249f",
  "isSidechain": false,
  "requestId": "req_011Cb8HLCuGj1kkHwrs6z9mt",
  "type": "assistant",
  "uuid": "6a455012-eea6-4b19-b3de-0b6fe22a921f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgpYdWYtt8WpU6bM9Sfmn8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 452,
      "cache_read_input_tokens": 82838,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 452,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 96,
          "cache_read_input_tokens": 82838,
          "cache_creation_input_tokens": 452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 452
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

_source line 80 · 2026-05-17T14:15:57.642Z_

<details><summary>↩ Tool result · `toolu_01XEzChrfaCHgZCjNih3Fimo`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a455012-eea6-4b19-b3de-0b6fe22a921f",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "5e15c694-10af-4bad-a489-ee92715ddd62",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 24,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "6a455012-eea6-4b19-b3de-0b6fe22a921f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 81 · 2026-05-17T14:15:57.675Z_

```json
{
  "parentUuid": "5e15c694-10af-4bad-a489-ee92715ddd62",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "eebad962-4fec-4e0c-9d69-2ecf3d63b20d",
  "timestamp": "2026-05-17T14:15:57.675Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 82 · 2026-05-17T14:16:03.666Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011VHaVHPuhbRhSiVUXVxn26`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
  "description": "Find YAML config files in project directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eebad962-4fec-4e0c-9d69-2ecf3d63b20d",
  "isSidechain": false,
  "requestId": "req_011Cb8HLUrDbHhD8CtXcTadD",
  "type": "assistant",
  "uuid": "f31f37f6-e39a-4a91-a685-6d2dd212f776",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012UxcSza4wJtKttk1mmoXsD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 214,
      "cache_read_input_tokens": 83290,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 214,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 127,
          "cache_read_input_tokens": 83290,
          "cache_creation_input_tokens": 214,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 214
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

_source line 83 · 2026-05-17T14:16:04.002Z_

<details><summary>↩ Tool result · `toolu_011VHaVHPuhbRhSiVUXVxn26`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f31f37f6-e39a-4a91-a685-6d2dd212f776",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "28ccdd97-a63b-4344-9e39-a4996687e85f",
  "toolUseResult": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/dream_registry.yaml\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/writing_plan.yaml\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/registry.yaml\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/constraints.yaml\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/mistakes.yaml\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/review_context.yaml\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/imagined_experiments.yaml\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/review_context.yaml\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/imagined_experiments.yaml\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/meta.yaml\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/best/review_context.yaml\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/best/imagined_experiments.yaml\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/review_context.yaml\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/imagined_experiments.yaml\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/worst/review_context.yaml\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/worst/imagined_experiments.yaml\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/meta.yaml\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/review_context.yaml",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f31f37f6-e39a-4a91-a685-6d2dd212f776",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-17T14:16:07.303Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01F5aD8bawejtdT7cvmZE74X`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -maxdepth 2 -name \"config*.yaml\" -o -name \"project_config*\" -o -name \"settings.yaml\" 2>/dev/null | head -10",
  "description": "Find project config files at top level"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28ccdd97-a63b-4344-9e39-a4996687e85f",
  "isSidechain": false,
  "requestId": "req_011Cb8HLwzcMtt2pp5CuJksY",
  "type": "assistant",
  "uuid": "eb847498-822e-4f80-9a7f-f110142971a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DwYTmzvJkGunTaFp4j3ukE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1030,
      "cache_read_input_tokens": 83504,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1030,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 83504,
          "cache_creation_input_tokens": 1030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1030
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

_source line 85 · 2026-05-17T14:16:07.380Z_

<details><summary>↩ Tool result · `toolu_01F5aD8bawejtdT7cvmZE74X`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb847498-822e-4f80-9a7f-f110142971a8",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "8f76dd5a-502b-40ca-b2bf-e98344cfca05",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "eb847498-822e-4f80-9a7f-f110142971a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-17T14:16:10.929Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Q5UWEey4Y3jUkNqTDjvPZA`</summary>

```json
{
  "command": "grep -rl \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" --include=\"*.toml\" 2>/dev/null | head -5",
  "description": "Search for external_review configuration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f76dd5a-502b-40ca-b2bf-e98344cfca05",
  "isSidechain": false,
  "requestId": "req_011Cb8HMCQ3LgQii8iAByk1L",
  "type": "assistant",
  "uuid": "c3b89b79-3b11-4c66-9e51-d182bd5d5831",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Bm6b4t4qRrvxnomNGmXG4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 157,
      "cache_read_input_tokens": 84534,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 157,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 84534,
          "cache_creation_input_tokens": 157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 157
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

_source line 87 · 2026-05-17T14:16:11.077Z_

<details><summary>↩ Tool result · `toolu_01Q5UWEey4Y3jUkNqTDjvPZA`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3b89b79-3b11-4c66-9e51-d182bd5d5831",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "d8365e72-aca1-477f-a294-491f8fcc7522",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "c3b89b79-3b11-4c66-9e51-d182bd5d5831",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 88 · 2026-05-17T14:16:27.407Z_

<details><summary>Logged reasoning block</summary>

```text
No external review config found. So external review is not enabled. Let me proceed with the internal review only.

Now I have all the information needed. Let me summarize:

**Venue Requirements (EMNLP 2026 through ARR):**
- Deadline: May 25, 2026 (today is May 17, deadline has NOT passed)
- Long paper: 8 pages content + unlimited references + appendix
- Short paper: 4 pages content + unlimited references + appendix
- Template: ACL style (`\usepackage[review]{acl}`) ✓
- Double-blind review ✓ (author listed as "Anonymous")


- Mandatory Limitations section and Responsible NLP Research Checklist required ✓
- Appendix must be double-column format

**Paper Structure:**
- Title: "How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?"
- Main sections: Abstract, Introduction, Related Work, Experimental Setup, Results, Schema Decomposition (negative result), Discussion + Conclusion, Limitations, Checklist
- Appendices covering Additional Figures, SDGD Protocol, Factorial Analysis, Within-Pool CI, MAVEN Centrality, Batch Composition, Prompt Templates, Prompt Sensitivity, BCS Aggregation, and BCS-Controlled Details

, plus Within-Pool Method, SCS Ablation, Aggregation Simulation, BCS Independence, Split-Origin, Variance Decomposition, Cross-Domain, Cross-Model 70B, and Few-Shot BCS

**Reviewer Assignment (EMNLP 2026):**
- Reviewer 1 focuses on methodological rigor, experimental design, and statistical analysis
- Reviewer 2 evaluates novelty, narrative coherence, writing quality, and citation coverage

I'm preparing to dispatch the reviewers with venue information included in the messages. Given the extensive appendices and comprehensive main sections, this is clearly a long paper format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8365e72-aca1-477f-a294-491f8fcc7522",
  "isSidechain": false,
  "requestId": "req_011Cb8HMUDYcJPGeYHDX6W4s",
  "type": "assistant",
  "uuid": "5625382f-a301-455b-9f0a-3f3b5d904279",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUiCRMKkZauCvQPzJDjrQ8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 155,
      "cache_read_input_tokens": 84691,
      "output_tokens": 3262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 155,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3262,
          "cache_read_input_tokens": 84691,
          "cache_creation_input_tokens": 155,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 155
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

_source line 89 · 2026-05-17T14:16:34.053Z_

所有资料检查完毕。汇报审稿启动状态，然后分配 Reviewer。

---

**圆桌审稿启动 — Round 1**

| 项目 | 内容 |
|---|---|
| **投稿目标** | EMNLP 2026 Main Conference (通过 ARR May cycle) |
| **截止日期** | 2026-05-25（距今 8 天，未过期） |
| **论文路径** | `projects/schema-dag-extraction/docs/paper/main.tex`（多文件结构，含 11 个 appendix section） |
| **格式** | Long paper, ACL `[review]` 模板, double-blind, 8 页正文 + 无限参考文献 + 附录 |
| **资料完整性** | LaTeX 源文件完整（abstract/intro/related_work/experimental_setup/results/sdgd_negative/discussion/checklist/prompt_appendix），有 Limitations section，有 Responsible NLP Checklist |
| **外部审稿** | 未启用（配置中无 `external_review.paperreview_ai.enabled`） |

**Reviewer 编排**（EMNLP = 一般会议级别，2 人）：
- **Reviewer 1**：方法严谨性 + 实验设计 + 统计分析
- **Reviewer 2**：新颖性 + 叙事完整性 + 写作质量 + 引用覆盖

现在分配任务。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5625382f-a301-455b-9f0a-3f3b5d904279",
  "isSidechain": false,
  "requestId": "req_011Cb8HMUDYcJPGeYHDX6W4s",
  "type": "assistant",
  "uuid": "a94c0277-bc2b-49c8-a649-7e2596499f85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUiCRMKkZauCvQPzJDjrQ8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 155,
      "cache_read_input_tokens": 84691,
      "output_tokens": 3262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 155,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3262,
          "cache_read_input_tokens": 84691,
          "cache_creation_input_tokens": 155,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 155
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

_source line 90 · 2026-05-17T14:16:53.585Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer · `toolu_01JasfnmVpGboHCTxLUrrThC`</summary>

```json
{
  "reviewer_id": "1",
  "round_number": 1,
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的侧重**：方法严谨性 + 实验设计 + 统计分析\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: Long paper, 8 页正文, ACL `[review]` 模板, double-blind\n- **附录**: 不计入页数限制，但必须双栏格式\n- **必须包含**: Limitations section + Responsible NLP Research Checklist\n\n### 论文路径\n`projects/schema-dag-extraction/docs/paper/main.tex`（多文件结构，需读取 abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex, prompt_appendix.tex）\n\n### 论文概要\n标题: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n研究 training-free LLM IE 中 schema complexity 的两个维度（type count vs type confusability）如何独立预测性能下降。提出 SCS/BCS 指标量化 type confusability。实验横跨 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）和 3 个任务（NER, RE, ED）。包含一个重要负面结果：schema decomposition (SDGD) 在 NER 和 RE 上均失败。\n\n### 审查重点\n请重点审查以下方面，给出详细评估：\n\n1. **实验设计严谨性**\n   - BCS-controlled 实验的 confound control 是否充分？type frequency 混淆变量是否被充分处理？\n   - Count curve 和 BCS-controlled 两个实验范式的互补性是否合理？\n   - 数据集选择（4个）和任务覆盖（NER/RE/ED）是否充分支撑 claim？\n\n2. **统计方法**\n   - TOST 等价性检验的 margin 选择（±3pp）是否合理？\n   - Bootstrap CI 的使用是否恰当？\n   - 多重比较问题的处理（引用 Rothman 1990 作为不需要校正的理由）是否充分？\n   - Pairwise $r^2$ = 1.3-1.7% 的效应量是否足以支撑论文的核心 claim？\n\n3. **结论与证据匹配**\n   - \"Two dimensions\" claim 的证据是否充分？NER 上 batch-level BCS 无显著效果，这如何影响 claim？\n   - SDGD 负面结果的诊断（merge amplification, routing failure）是否有说服力？\n   - Cross-model validation（Llama 8B/70B）的证据力度如何？\n\n4. **可重现性**\n   - 实验细节是否足够重现？\n   - 单 seed 评估 + greedy decoding 的正当性\n\n5. **格式合规**\n   - 正文是否在 8 页以内？\n   - 引用格式是否正确？\n   - 图表是否清晰可读？\n\n请按照标准审稿报告格式输出：Summary → Strengths → Weaknesses → Questions → Missing References → Detailed Comments",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a94c0277-bc2b-49c8-a649-7e2596499f85",
  "isSidechain": false,
  "requestId": "req_011Cb8HMUDYcJPGeYHDX6W4s",
  "type": "assistant",
  "uuid": "3d28f13c-ad88-4926-a408-583da3415910",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUiCRMKkZauCvQPzJDjrQ8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 155,
      "cache_read_input_tokens": 84691,
      "output_tokens": 3262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 155,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3262,
          "cache_read_input_tokens": 84691,
          "cache_creation_input_tokens": 155,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 155
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

_source line 91 · 2026-05-17T14:16:58.790Z_

<details><summary>↩ Tool result · `toolu_01JasfnmVpGboHCTxLUrrThC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d28f13c-ad88-4926-a408-583da3415910",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "1053cbcf-7674-4a8b-a32b-e9fd5d686df0",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reviewer_key\\\": \\\"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "3d28f13c-ad88-4926-a408-583da3415910",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-17T14:17:11.099Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer · `toolu_01PTksC51znvn2sFizVThpxR`</summary>

```json
{
  "reviewer_id": "2",
  "round_number": 1,
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的侧重**：新颖性 + 叙事完整性 + 写作质量 + 引用覆盖\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: Long paper, 8 页正文, ACL `[review]` 模板, double-blind\n- **附录**: 不计入页数限制，但必须双栏格式\n- **必须包含**: Limitations section + Responsible NLP Research Checklist\n\n### 论文路径\n`projects/schema-dag-extraction/docs/paper/main.tex`（多文件结构，需读取 abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex, prompt_appendix.tex）\n\n### 论文概要\n标题: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n这是一篇分析性论文，不提出新方法/新模型，而是通过控制实验揭示 training-free LLM IE 中 schema complexity 如何驱动性能下降。核心指标为 SCS（pairwise embedding similarity）和 BCS（batch-level aggregation）。包含跨 4 个数据集、3 个任务、3 个模型的广泛实验。负面结果：SDGD schema decomposition 失败。\n\n### 审查重点\n请重点审查以下方面，给出详细评估：\n\n1. **新颖性评估**\n   - SCS/BCS 本质上是 pairwise cosine similarity 的简单聚合——这是否有足够的新颖性？论文自身承认 SCS 与 LLM-PEE 的 partitioning criterion 形式相同。\n   - \"Controlled study isolating count from confusability\" 的分析范式新颖性如何？\n   - 负面结果（SDGD 失败）的贡献度如何？是否足以作为独立贡献点？\n   - 对 EMNLP 2026 的贡献门槛评估：这篇论文更适合 Main 还是 Findings？\n\n2. **叙事完整性**\n   - Abstract → Introduction → Method → Results → Discussion 的故事线是否连贯？\n   - \"Two dimensions\" framing 是否准确？NER 上 batch-level 无效果这一事实是否削弱了框架的普适性？\n   - 论文的 contribution claim（Introduction 末尾的 4 条）是否都有充分支撑？\n   - RQ1/RQ2/RQ3 的回答是否清晰且令人信服？\n\n3. **写作质量**\n   - 是否存在 AI 写作痕迹（em-dash、-ing phrases、过度分段等）？\n   - 术语定义是否清晰？首次出现是否有解释？\n   - 段落过渡是否自然？\n   - Abstract 是否在 150-250 words 内完成四个必答问题？\n\n4. **Related Work 和引用覆盖**\n   - Related Work 是否充分 positioning？与直接竞争者（LLM-PEE, PARSE, CrossAgentIE, DEE）的区分是否清晰？\n   - 是否遗漏重要相关工作？特别关注 2025-2026 年的最新工作\n   - 引用密度是否达到 EMNLP 标准？\n   - SCS novelty paragraph 是否有效地回应了潜在的新颖性质疑？\n\n5. **图表质量**\n   - 图表信息密度是否足够？\n   - Caption 是否自包含？\n   - 数值精度是否统一？\n\n请按照标准审稿报告格式输出：Summary → Strengths → Weaknesses → Questions → Missing References → Detailed Comments",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1053cbcf-7674-4a8b-a32b-e9fd5d686df0",
  "isSidechain": false,
  "requestId": "req_011Cb8HMUDYcJPGeYHDX6W4s",
  "type": "assistant",
  "uuid": "05798911-e862-4c7d-aa61-be49f884a7e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUiCRMKkZauCvQPzJDjrQ8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 155,
      "cache_read_input_tokens": 84691,
      "output_tokens": 3262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 155,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3262,
          "cache_read_input_tokens": 84691,
          "cache_creation_input_tokens": 155,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 155
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

_source line 93_

```json
{
  "type": "last-prompt",
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: schema-dag-extraction - 论文路径: projects/schema-dag-extraction/docs/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: Main Conference - 截止日期: 2026-05-25  请 `Read /home/ubun…",
  "leafUuid": "05798911-e862-4c7d-aa61-be49f884a7e3",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a"
}
```

---

### Runtime record

_source line 94_

```json
{
  "type": "ai-title",
  "aiTitle": "Review schema-dag-extraction paper for EMNLP 2026",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a"
}
```

---

### Tool result

_source line 95 · 2026-05-17T14:17:12.579Z_

<details><summary>↩ Tool result · `toolu_01PTksC51znvn2sFizVThpxR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05798911-e862-4c7d-aa61-be49f884a7e3",
  "isSidechain": false,
  "promptId": "de06f297-455f-476c-9fc8-b305d7d2f534",
  "type": "user",
  "uuid": "a17885b8-8a76-433f-b3a8-f7c1df43f1b4",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reviewer_key\\\": \\\"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "05798911-e862-4c7d-aa61-be49f884a7e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5",
  "sessionId": "b929ddb9-042f-444e-b6a7-4cb35f1bc04a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
