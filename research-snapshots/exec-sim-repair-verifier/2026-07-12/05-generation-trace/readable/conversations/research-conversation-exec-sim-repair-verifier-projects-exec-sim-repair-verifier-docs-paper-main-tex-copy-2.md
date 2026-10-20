# Research conversation: 系统通知：审稿审批已通过。请开始审稿。 [论文提交] - 项目: exec-sim-repair-verifier - 论文路径: projects/exec-sim-repair-verifier/docs/paper/main.tex 

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 92
- **Recorded user turns:** 1
- **Tool calls:** 28
- **Original source:** `logs/chats/exported-trajectories/account-1/21e91d71-aa56-45c2-8945-1101b3d4f69e.jsonl`
- **Structured JSON:** [`61d7b7550ba374a78835.json`](../../sessions/61/61d7b7550ba374a78835.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-25T21:14:18.662Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T21:14:18.662Z",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "content": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: exec-sim-repair-verifier\n- 论文路径: projects/exec-sim-repair-verifier/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR (Main/Findings unified)\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

---

### Runtime record

_source line 2 · 2026-05-25T21:14:18.665Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T21:14:18.665Z",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e"
}
```

---

## Round 1

90 recorded events

### User

_source line 3 · 2026-05-25T21:14:18.700Z_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: exec-sim-repair-verifier
- 论文路径: projects/exec-sim-repair-verifier/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR (Main/Findings unified)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "ec052adb-6e0d-4847-91db-f31e83046c73",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-25T21:14:18.700Z_

```json
{
  "parentUuid": "ec052adb-6e0d-4847-91db-f31e83046c73",
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
  "uuid": "cc83d254-6a60-4bfa-aea3-39f2b90fdf05",
  "timestamp": "2026-05-25T21:14:18.700Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-25T21:14:18.700Z_

```json
{
  "parentUuid": "cc83d254-6a60-4bfa-aea3-39f2b90fdf05",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "3b9d0e2f-9613-4883-9b92-30c669ccfca9",
  "timestamp": "2026-05-25T21:14:18.700Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-25T21:14:18.700Z_

```json
{
  "parentUuid": "3b9d0e2f-9613-4883-9b92-30c669ccfca9",
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
  "uuid": "8b724835-1cf7-4211-b970-7a55d5d3840c",
  "timestamp": "2026-05-25T21:14:18.700Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 7 · 2026-05-25T21:14:18.700Z_

```json
{
  "parentUuid": "8b724835-1cf7-4211-b970-7a55d5d3840c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "302b6e4f-dc46-4e60-a2c5-29af922409a2",
  "timestamp": "2026-05-25T21:14:18.700Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper submission for EMNLP 2026",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e"
}
```

---

### Assistant

_source line 9 · 2026-05-25T21:14:21.409Z_

<details><summary>Logged reasoning block</summary>

```text
The user is asking me to start a review process. Let me first read the review-director-session-start skill file to understand the full review workflow.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "302b6e4f-dc46-4e60-a2c5-29af922409a2",
  "isSidechain": false,
  "requestId": "req_011CbPyi7RwnHvjKJE7oYtjs",
  "type": "assistant",
  "uuid": "9461adc6-00e7-45c0-b22e-32a98cfd9125",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015uZhrbu2d4yrxVHZeQA3hp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16703,
      "cache_read_input_tokens": 11447,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 126,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 16703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16703
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

_source line 10 · 2026-05-25T21:14:21.545Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FJv5GwG2GLBYaS1KWrnDkD`</summary>

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
  "parentUuid": "9461adc6-00e7-45c0-b22e-32a98cfd9125",
  "isSidechain": false,
  "requestId": "req_011CbPyi7RwnHvjKJE7oYtjs",
  "type": "assistant",
  "uuid": "b7dc0cd4-a6a5-464d-889c-77ed668a0de5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015uZhrbu2d4yrxVHZeQA3hp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16703,
      "cache_read_input_tokens": 11447,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 126,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 16703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16703
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

_source line 11 · 2026-05-25T21:14:21.562Z_

<details><summary>↩ Tool result · `toolu_01FJv5GwG2GLBYaS1KWrnDkD`</summary>

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
  "parentUuid": "b7dc0cd4-a6a5-464d-889c-77ed668a0de5",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "5e5de30b-c50e-4ef5-8f22-ef1a8ffe22c5",
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
  "sourceToolAssistantUUID": "b7dc0cd4-a6a5-464d-889c-77ed668a0de5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
````

</details>

---

### Assistant

_source line 12 · 2026-05-25T21:14:27.276Z_

<details><summary>Logged reasoning block</summary>

```text
Now I understand the full review workflow. Let me follow it step by step:

1. Step 0: Resource check + Venue research
2. Step 0.5: Decide Reviewer arrangement
3. Step 0.6: External review (if enabled)
4. Step 0.7: Visual check dispatch
5. Step 1: Independent review
6. Step 2: Cross-sharing
7. Step 3: Convergence check
8. Step 4: Summary report

Let me start with initialization:
1. Get project overview
2. Check paper file status
3. Process the paper submission


4. Begin the workflow
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e5de30b-c50e-4ef5-8f22-ef1a8ffe22c5",
  "isSidechain": false,
  "requestId": "req_011CbPyiKnLaf7okwHh2An1S",
  "type": "assistant",
  "uuid": "3641bafc-c90e-4a4a-a396-c526d1063aac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALpk4yMaJmbSxTM4T3Cagc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3453,
      "cache_read_input_tokens": 28150,
      "output_tokens": 402,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3453,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 402,
          "cache_read_input_tokens": 28150,
          "cache_creation_input_tokens": 3453,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3453
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

_source line 13 · 2026-05-25T21:14:27.505Z_

开始审稿流程初始化。先获取项目概况和论文文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3641bafc-c90e-4a4a-a396-c526d1063aac",
  "isSidechain": false,
  "requestId": "req_011CbPyiKnLaf7okwHh2An1S",
  "type": "assistant",
  "uuid": "9a23ad7e-ea0c-4363-bc75-9f8835203911",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALpk4yMaJmbSxTM4T3Cagc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3453,
      "cache_read_input_tokens": 28150,
      "output_tokens": 402,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3453,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 402,
          "cache_read_input_tokens": 28150,
          "cache_creation_input_tokens": 3453,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3453
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

_source line 14 · 2026-05-25T21:14:29.899Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FkZq9XYz4tVrVz4tDffTJw`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a23ad7e-ea0c-4363-bc75-9f8835203911",
  "isSidechain": false,
  "requestId": "req_011CbPyiKnLaf7okwHh2An1S",
  "type": "assistant",
  "uuid": "ee79214f-55bd-4421-aaa5-e73ad0ad4ad7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALpk4yMaJmbSxTM4T3Cagc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3453,
      "cache_read_input_tokens": 28150,
      "output_tokens": 402,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3453,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 402,
          "cache_read_input_tokens": 28150,
          "cache_creation_input_tokens": 3453,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3453
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

_source line 15 · 2026-05-25T21:14:29.903Z_

<details><summary>↩ Tool result · `toolu_01FkZq9XYz4tVrVz4tDffTJw`</summary>

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
  "tool_name": "mcp__agent-ml-research__dispatch_visual_check"
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
  "tool_name": "mcp__agent-ml-research__get_visual_check_status"
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
  "parentUuid": "ee79214f-55bd-4421-aaa5-e73ad0ad4ad7",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "c8c48f1b-6a34-407c-8d37-461b7049f9fb",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__dispatch_visual_check",
      "mcp__agent-ml-research__request_external_review",
      "mcp__agent-ml-research__get_external_review_status",
      "mcp__agent-ml-research__get_visual_check_status",
      "mcp__agent-ml-research__submit_review_report_to_research_director",
      "mcp__agent-ml-research__update_review_issues"
    ],
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "total_deferred_tools": 29
  },
  "sourceToolAssistantUUID": "ee79214f-55bd-4421-aaa5-e73ad0ad4ad7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: exec-sim-repair-verifier - 论文路径: projects/exec-sim-repair-verifier/docs/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: ARR (Main/Findings unified) - 截止日期: 2026-05-25 -…",
  "leafUuid": "c8c48f1b-6a34-407c-8d37-461b7049f9fb",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper submission for EMNLP 2026",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e"
}
```

---

### Tool call

_source line 18 · 2026-05-25T21:14:33.252Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_018TXRPN5qbrjuLjkksGRrRc`</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8c48f1b-6a34-407c-8d37-461b7049f9fb",
  "isSidechain": false,
  "requestId": "req_011CbPyiwZ9VzEEeoC7UcJT7",
  "type": "assistant",
  "uuid": "61a3b3a7-bfd3-454d-8a47-2333a1b02838",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmFeKkntBRGGquF1ekSYez",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3536,
      "cache_read_input_tokens": 31603,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3536,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 164,
          "cache_read_input_tokens": 31603,
          "cache_creation_input_tokens": 3536,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3536
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

_source line 19 · 2026-05-25T21:14:33.991Z_

<details><summary>↩ Tool result · `toolu_018TXRPN5qbrjuLjkksGRrRc`</summary>

```text
{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (267 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- deepseek-cls-repo-resume: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633（已分配 ? GPU:?，等待提交）\n- cls14b-func-s42-v2-bf16-eval: CLS 14B bf16 eval should yield higher accuracy than NF4 eval (89.47%), eliminating quantization confound. If bf16 accuracy > 89.47%, the CLS 8B→14B regression is an NF4 artifact; if bf16 ≈ 89.47%, the regression is real.（准备中）\n- qwen_cwm_s456_resume2（准备中）\n- qwen_cwm_s456_resume（准备中）\n- deepseek-cwm-repo-s42-e3-seq4096-eval（准备中）\n- exp-downsample-cls-func-v3-eval-v2: Eval downsample CLS (Qwen3-4B, ~8K训练数据) on repo-level test set. 如果 accuracy 接近全量训练的 CLS (83.63%), 则证明 CLS formulation 优势不来自数据量（准备中）\n- exp-e-qwen3-3shot-baseline: Qwen3-8B 3-shot few-shot CLS baseline 在 repo-level 表现差于 fine-tuned models，与 DeepSeek 3-shot 一致，证明 fine-tuning 的必要性跨模型成立（准备中）\n- D131-cwm-s42-epoch3-seq2048（准备中）\n- D133-cwm-s42-e2-seq2048-home-resume（准备中）\n- deepseek-cwm-repo-s42-epoch2-eval: Eval CWM s42 epoch 2 checkpoint 解耦过拟合 vs seed 差异：如果 epoch 2 accuracy >> epoch 3 (56.7%)，则 CWM repo-level 在 epoch 3 过拟合（准备中）\n- …另有 9 项\n\n## 近期结论\n- **cls-downsample-400-s42** (success): CLS function-level trained on ~447 samples (matching TRAJ variant count) should reveal whether TRAJ's lower accuracy (86.30% vs CLS 88.43%) is due to data volume disparity (34×) or formulation difference. If CLS@447 ≈ TRAJ → data volume is main confound; if CLS@447 > TRAJ → formulation effect independent of data volume.\n- **deepseek-cwm-repo-s456-train-v2** (success): DeepSeek CWM repo-level s456-v2：第 3 seed，与 s42/s123-v2 对齐（train_unified.py + --train_file swebench_full/swebench_train.jsonl, 70748 行）。组成完整 3-seed coverage (42/123/456)。使用 epoch 3 final checkpoint 评估。 ← 基于 deepseek-cwm-repo-s456-train\n- **traj14b-func-s456** (success): TRAJ 14B (seed 456) 补完 Table 2 的 14B TRAJ 行。与 CLS/CWM 14B 对比验证三公式在 14B 的 scaling 趋势。4B→8B TRAJ scaling +2.13pp，14B 应保持或扩大趋势。\n\n## 趋势\n成功 149 / 负向 7 / 失败 60 / 共 248\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nseetacloud-westd-4x5090: 无 GPU 信息\n\n## 告警\n- trace-then-judge: 训练失败 — unknown\n- repo-level-cls: 训练失败 — unknown\n- repo-level-cwm: 训练失败 — unknown\n- repo-level-cls-v2: 训练失败 — unknown\n- repo-level-cwm-v2: 训练失败 — unknown\n- repo-level-cls-v3: 训练失败 — unknown\n- repo-level-cwm-v3: 训练失败 — unknown\n- repo-level-cls-home: 训练失败 — unknown\n- repo-level-cwm-v4: 已被终止 — unknown\n- repo-level-cwm-v5: 训练失败 — unknown\n- repo-level-cwm-v6: 训练失败 — unknown\n- repo-level-cwm-v7: 训练失败 — unknown\n- repo-level-cwm-v8: 训练失败 — unknown\n- repo-level-cwm-v9: 训练失败 — unknown\n- repo-level-cls-seed123: 已被终止 — unknown\n- repo-level-cwm-seed123: 已被终止 — unknown\n- repo-level-cwm-v11: 已被终止 — unknown\n- repo-level-cls-8b: 已被终止 — unknown\n- repo-level-cwm-v12: 已被终止 — unknown\n- repo-level-cwm-seed123-conda: 已被终止 — unknown\n- repo-level-cwm-8b-conda: 训练失败 — unknown\n- repo-level-cls-8b-seed123-conda: 训练失败 — unknown\n- repo-level-cwm-8b-conda-v2: 训练失败 — unknown\n- repo-level-cls-8b-seed123-conda-v2: 训练失败 — "}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61a3b3a7-bfd3-454d-8a47-2333a1b02838",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "dda71d32-d4f4-4516-82cb-6445eeeecaea",
  "toolUseResult": "{\"result\":\"# 项目 exec-sim-repair-verifier 概况\\n\\n## 实验状态 (267 个)\\n\\n- **per-test-majority-voting**: DONE (negative) — \\n- **block-corr-empirical**: DONE (success) — \\n- **model-size-scaling-cwm8b**: DONE (success) — \\n- **model-size-scaling-cls8b**: DONE (success) — \\n- **llm-judge-32b-zeroshot**: DONE (success) — \\n- **llm-judge-8b-zeroshot**: DONE (success) — \\n- **traj-level-seed123**: DONE (success) — \\n- **oracle-f2p-stratified**: DONE (success) — \\n- **trace-then-judge**: DONE (failed) — \\n- **mvp-b-train**: DONE (success) — \\n- **multi-seed-core**: DONE (success) — \\n- **cwm-baseline**: DONE (negative) — \\n- **mvp-a-oracle-sim**: DONE (success) — \\n- **p2p-regression-rate**: DONE (negative) — \\n- **mvp-b-data-prep**: DONE (success) — \\n\\n## 最新报告\\n# Handover — 2026-05-23\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- deepseek-cls-repo-resume: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633（已分配 ? GPU:?，等待提交）\\n- cls14b-func-s42-v2-bf16-eval: CLS 14B bf16 eval should yield higher accuracy than NF4 eval (89.47%), eliminating quantization confound. If bf16 accuracy > 89.47%, the CLS 8B→14B regression is an NF4 artifact; if bf16 ≈ 89.47%, the regression is real.（准备中）\\n- qwen_cwm_s456_resume2（准备中）\\n- qwen_cwm_s456_resume（准备中）\\n- deepseek-cwm-repo-s42-e3-seq4096-eval（准备中）\\n- exp-downsample-cls-func-v3-eval-v2: Eval downsample CLS (Qwen3-4B, ~8K训练数据) on repo-level test set. 如果 accuracy 接近全量训练的 CLS (83.63%), 则证明 CLS formulation 优势不来自数据量（准备中）\\n- exp-e-qwen3-3shot-baseline: Qwen3-8B 3-shot few-shot CLS baseline 在 repo-level 表现差于 fine-tuned models，与 DeepSeek 3-shot 一致，证明 fine-tuning 的必要性跨模型成立（准备中）\\n- D131-cwm-s42-epoch3-seq2048（准备中）\\n- D133-cwm-s42-e2-seq2048-home-resume（准备中）\\n- deepseek-cwm-repo-s42-epoch2-eval: Eval CWM s42 epoch 2 checkpoint 解耦过拟合 vs seed 差异：如果 epoch 2 accuracy >> epoch 3 (56.7%)，则 CWM repo-level 在 epoch 3 过拟合（准备中）\\n- …另有 9 项\\n\\n## 近期结论\\n- **cls-downsample-400-s42** (success): CLS function-level trained on ~447 samples (matching TRAJ variant count) should reveal whether TRAJ's lower accuracy (86.30% vs CLS 88.43%) is due to data volume disparity (34×) or formulation difference. If CLS@447 ≈ TRAJ → data volume is main confound; if CLS@447 > TRAJ → formulation effect independent of data volume.\\n- **deepseek-cwm-repo-s456-train-v2** (success): DeepSeek CWM repo-level s456-v2：第 3 seed，与 s42/s123-v2 对齐（train_unified.py + --train_file swebench_full/swebench_train.jsonl, 70748 行）。组成完整 3-seed coverage (42/123/456)。使用 epoch 3 final checkpoint 评估。 ← 基于 deepseek-cwm-repo-s456-train\\n- **traj14b-func-s456** (success): TRAJ 14B (seed 456) 补完 Table 2 的 14B TRAJ 行。与 CLS/CWM 14B 对比验证三公式在 14B 的 scaling 趋势。4B→8B TRAJ scaling +2.13pp，14B 应保持或扩大趋势。\\n\\n## 趋势\\n成功 149 / 负向 7 / 失败 60 / 共 248\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nseetacloud-westd-4x5090: 无 GPU 信息\\n\\n## 告警\\n- trace-then-judge: 训练失败 — unknown\\n- repo-level-cls: 训练失败 — unknown\\n- repo-level-cwm: 训练失败 — unknown\\n- repo-level-cls-v2: 训练失败 — unknown\\n- repo-level-cwm-v2: 训练失败 — unknown\\n- repo-level-cls-v3: 训练失败 — unknown\\n- repo-level-cwm-v3: 训练失败 — unknown\\n- repo-level-cls-home: 训练失败 — unknown\\n- repo-level-cwm-v4: 已被终止 — unknown\\n- repo-level-cwm-v5: 训练失败 — unknown\\n- repo-level-cwm-v6: 训练失败 — unknown\\n- repo-level-cwm-v7: 训练失败 — unknown\\n- repo-level-cwm-v8: 训练失败 — unknown\\n- repo-level-cwm-v9: 训练失败 — unknown\\n- repo-level-cls-seed123: 已被终止 — unknown\\n- repo-level-cwm-seed123: 已被终止 — unknown\\n- repo-level-cwm-v11: 已被终止 — unknown\\n- repo-level-cls-8b: 已被终止 — unknown\\n- repo-level-cwm-v12: 已被终止 — unknown\\n- repo-level-cwm-seed123-conda: 已被终止 — unknown\\n- repo-level-cwm-8b-conda: 训练失败 — unknown\\n- repo-level-cls-8b-seed123-conda: 训练失败 — unknown\\n- repo-level-cwm-8b-conda-v2: 训练失败 — unknown\\n- repo-level-cls-8b-seed123-conda-v2: 训练失败 — \"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (267 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- deepseek-cls-repo-resume: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633（已分配 ? GPU:?，等待提交）\n- cls14b-func-s42-v2-bf16-eval: CLS 14B bf16 eval should yield higher accuracy than NF4 eval (89.47%), eliminating quantization confound. If bf16 accuracy > 89.47%, the CLS 8B→14B regression is an NF4 artifact; if bf16 ≈ 89.47%, the regression is real.（准备中）\n- qwen_cwm_s456_resume2（准备中）\n- qwen_cwm_s456_resume（准备中）\n- deepseek-cwm-repo-s42-e3-seq4096-eval（准备中）\n- exp-downsample-cls-func-v3-eval-v2: Eval downsample CLS (Qwen3-4B, ~8K训练数据) on repo-level test set. 如果 accuracy 接近全量训练的 CLS (83.63%), 则证明 CLS formulation 优势不来自数据量（准备中）\n- exp-e-qwen3-3shot-baseline: Qwen3-8B 3-shot few-shot CLS baseline 在 repo-level 表现差于 fine-tuned models，与 DeepSeek 3-shot 一致，证明 fine-tuning 的必要性跨模型成立（准备中）\n- D131-cwm-s42-epoch3-seq2048（准备中）\n- D133-cwm-s42-e2-seq2048-home-resume（准备中）\n- deepseek-cwm-repo-s42-epoch2-eval: Eval CWM s42 epoch 2 checkpoint 解耦过拟合 vs seed 差异：如果 epoch 2 accuracy >> epoch 3 (56.7%)，则 CWM repo-level 在 epoch 3 过拟合（准备中）\n- …另有 9 项\n\n## 近期结论\n- **cls-downsample-400-s42** (success): CLS function-level trained on ~447 samples (matching TRAJ variant count) should reveal whether TRAJ's lower accuracy (86.30% vs CLS 88.43%) is due to data volume disparity (34×) or formulation difference. If CLS@447 ≈ TRAJ → data volume is main confound; if CLS@447 > TRAJ → formulation effect independent of data volume.\n- **deepseek-cwm-repo-s456-train-v2** (success): DeepSeek CWM repo-level s456-v2：第 3 seed，与 s42/s123-v2 对齐（train_unified.py + --train_file swebench_full/swebench_train.jsonl, 70748 行）。组成完整 3-seed coverage (42/123/456)。使用 epoch 3 final checkpoint 评估。 ← 基于 deepseek-cwm-repo-s456-train\n- **traj14b-func-s456** (success): TRAJ 14B (seed 456) 补完 Table 2 的 14B TRAJ 行。与 CLS/CWM 14B 对比验证三公式在 14B 的 scaling 趋势。4B→8B TRAJ scaling +2.13pp，14B 应保持或扩大趋势。\n\n## 趋势\n成功 149 / 负向 7 / 失败 60 / 共 248\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nseetacloud-westd-4x5090: 无 GPU 信息\n\n## 告警\n- trace-then-judge: 训练失败 — unknown\n- repo-level-cls: 训练失败 — unknown\n- repo-level-cwm: 训练失败 — unknown\n- repo-level-cls-v2: 训练失败 — unknown\n- repo-level-cwm-v2: 训练失败 — unknown\n- repo-level-cls-v3: 训练失败 — unknown\n- repo-level-cwm-v3: 训练失败 — unknown\n- repo-level-cls-home: 训练失败 — unknown\n- repo-level-cwm-v4: 已被终止 — unknown\n- repo-level-cwm-v5: 训练失败 — unknown\n- repo-level-cwm-v6: 训练失败 — unknown\n- repo-level-cwm-v7: 训练失败 — unknown\n- repo-level-cwm-v8: 训练失败 — unknown\n- repo-level-cwm-v9: 训练失败 — unknown\n- repo-level-cls-seed123: 已被终止 — unknown\n- repo-level-cwm-seed123: 已被终止 — unknown\n- repo-level-cwm-v11: 已被终止 — unknown\n- repo-level-cls-8b: 已被终止 — unknown\n- repo-level-cwm-v12: 已被终止 — unknown\n- repo-level-cwm-seed123-conda: 已被终止 — unknown\n- repo-level-cwm-8b-conda: 训练失败 — unknown\n- repo-level-cls-8b-seed123-conda: 训练失败 — unknown\n- repo-level-cwm-8b-conda-v2: 训练失败 — unknown\n- repo-level-cls-8b-seed123-conda-v2: 训练失败 — "
    }
  },
  "sourceToolAssistantUUID": "61a3b3a7-bfd3-454d-8a47-2333a1b02838",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-25T21:14:34.801Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ABP2NprmfrxGBVhRDcQYqW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dda71d32-d4f4-4516-82cb-6445eeeecaea",
  "isSidechain": false,
  "requestId": "req_011CbPyiwZ9VzEEeoC7UcJT7",
  "type": "assistant",
  "uuid": "a8ed637a-759e-4c78-938d-e725a1496385",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmFeKkntBRGGquF1ekSYez",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3536,
      "cache_read_input_tokens": 31603,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3536,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 164,
          "cache_read_input_tokens": 31603,
          "cache_creation_input_tokens": 3536,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3536
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

_source line 21 · 2026-05-25T21:14:34.808Z_

<details><summary>↩ Tool result · `toolu_01ABP2NprmfrxGBVhRDcQYqW`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	% ACL style (review mode for anonymous ARR submission)
4	\usepackage[review]{acl}
5	
6	% Standard packages from official ACL template
7	\usepackage{times}
8	\usepackage{latexsym}
9	\usepackage[T1]{fontenc}
10	\usepackage[utf8]{inputenc}
11	\usepackage{microtype}
12	\usepackage{inconsolata}
13	
14	% Math
15	\usepackage{amsmath}
16	\usepackage{amssymb}
17	
18	% Tables
19	\usepackage{booktabs}
20	\usepackage{multirow}
21	\usepackage{tabularx}
22	
23	% Graphics (xcolor loaded by acl.sty)
24	\usepackage{graphicx}
25	\graphicspath{{../../artifacts/}}
26	
27	% Lists
28	\usepackage{enumitem}
29	
30	% Custom commands
31	\newcommand{\cls}{\textsc{Cls}}
32	\newcommand{\cwm}{\textsc{Cwm}}
33	\newcommand{\traj}{\textsc{Traj}}
34	\newcommand{\fone}{F\textsubscript{1}}
35	\newcommand{\pp}{\,\text{pp}}
36	\newcommand{\tbd}{\textsc{tbd}}
37	\newcommand{\placeholder}[1]{{\color{red}\texttt{[#1]}}}
38	
39	\title{A Systematic Comparison of Execution-Free Verification Formulations for Code Repair}
40	\author{Anonymous}
41	
42	\begin{document}
43	\maketitle
44	
45	\input{abstract}
46	
47	\input{introduction}
48	
49	\begin{figure*}[t]
50	\centering
51	\includegraphics[width=\textwidth]{figures/paper/fig1_reformulation.pdf}
52	\caption{Three verification formulations. \textbf{Left:} \cls{} predicts binary pass/fail per test (1 output token). \textbf{Center:} \cwm{} generates execution output, derives verdict by exact match ($O(L)$ tokens). \textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved (1 token, no per-test signal). Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost.}
53	\label{fig:reformulation}
54	\end{figure*}
55	
56	\input{related_work}
57	
58	\input{method}
59	
60	\input{experiments}
61	
62	\input{conclusion}
63	
64	\bibliography{references}
65	
66	% ARR checklist is filled in OpenReview submission form, not in PDF
67	% \input{checklist}
68	
69	\input{appendix}
70	
71	\end{document}
72	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8ed637a-759e-4c78-938d-e725a1496385",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "51d454a7-7e4f-486b-a883-5214cccae966",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n% ACL style (review mode for anonymous ARR submission)\n\\usepackage[review]{acl}\n\n% Standard packages from official ACL template\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\n% Math\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n% Tables\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{tabularx}\n\n% Graphics (xcolor loaded by acl.sty)\n\\usepackage{graphicx}\n\\graphicspath{{../../artifacts/}}\n\n% Lists\n\\usepackage{enumitem}\n\n% Custom commands\n\\newcommand{\\cls}{\\textsc{Cls}}\n\\newcommand{\\cwm}{\\textsc{Cwm}}\n\\newcommand{\\traj}{\\textsc{Traj}}\n\\newcommand{\\fone}{F\\textsubscript{1}}\n\\newcommand{\\pp}{\\,\\text{pp}}\n\\newcommand{\\tbd}{\\textsc{tbd}}\n\\newcommand{\\placeholder}[1]{{\\color{red}\\texttt{[#1]}}}\n\n\\title{A Systematic Comparison of Execution-Free Verification Formulations for Code Repair}\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig1_reformulation.pdf}\n\\caption{Three verification formulations. \\textbf{Left:} \\cls{} predicts binary pass/fail per test (1 output token). \\textbf{Center:} \\cwm{} generates execution output, derives verdict by exact match ($O(L)$ tokens). \\textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved (1 token, no per-test signal). Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost.}\n\\label{fig:reformulation}\n\\end{figure*}\n\n\\input{related_work}\n\n\\input{method}\n\n\\input{experiments}\n\n\\input{conclusion}\n\n\\bibliography{references}\n\n% ARR checklist is filled in OpenReview submission form, not in PDF\n% \\input{checklist}\n\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 72,
      "startLine": 1,
      "totalLines": 72
    }
  },
  "sourceToolAssistantUUID": "a8ed637a-759e-4c78-938d-e725a1496385",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-25T21:14:46.237Z_

<details><summary>Logged reasoning block</summary>

```text
Good. I have the project overview and the main.tex file structure. Now I need to:

1. Read the full paper to understand its content
2. Search for EMNLP 2026 venue requirements (using web_search)
3. Check if external review is enabled in project config

Let me read the paper sections and search for venue requirements. Let me read the key sections of the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51d454a7-7e4f-486b-a883-5214cccae966",
  "isSidechain": false,
  "requestId": "req_011CbPyjJFbXiP572yeM8mVa",
  "type": "assistant",
  "uuid": "06641d1b-c988-48f1-b097-6710c300de54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaM23BQDFXe5A2ztbfTa1m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2976,
      "cache_read_input_tokens": 35139,
      "output_tokens": 742,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2976,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 742,
          "cache_read_input_tokens": 35139,
          "cache_creation_input_tokens": 2976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2976
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

_source line 23 · 2026-05-25T21:14:46.256Z_

论文文件存在，结构完整。现在执行 Step 0：读取论文各章节 + 搜索 EMNLP 2026 venue 要求。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06641d1b-c988-48f1-b097-6710c300de54",
  "isSidechain": false,
  "requestId": "req_011CbPyjJFbXiP572yeM8mVa",
  "type": "assistant",
  "uuid": "f2292ec4-2aa9-49ec-84e0-bfc3de5a7daa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaM23BQDFXe5A2ztbfTa1m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2976,
      "cache_read_input_tokens": 35139,
      "output_tokens": 742,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2976,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 742,
          "cache_read_input_tokens": 35139,
          "cache_creation_input_tokens": 2976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2976
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

_source line 24 · 2026-05-25T21:14:46.285Z_

<details open><summary>🔧 Tool call — Read · `toolu_018eMBRJ87guLjzXEsm2AkRS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2292ec4-2aa9-49ec-84e0-bfc3de5a7daa",
  "isSidechain": false,
  "requestId": "req_011CbPyjJFbXiP572yeM8mVa",
  "type": "assistant",
  "uuid": "6710a636-ec78-49fd-ace5-8a2bccd8866b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaM23BQDFXe5A2ztbfTa1m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2976,
      "cache_read_input_tokens": 35139,
      "output_tokens": 742,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2976,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 742,
          "cache_read_input_tokens": 35139,
          "cache_creation_input_tokens": 2976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2976
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

_source line 25 · 2026-05-25T21:14:50.279Z_

<details><summary>↩ Tool result · `toolu_01E7cXgVAoH6CdevEYSdB4Z5`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We systematically compare \cls{}, \cwm{}, and \traj{} across two representative code LLM families, two complexity levels, and multiple seeds to characterize the formulation landscape for neural code verification.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench}; runs with NaN validation loss (due to truncated targets exceeding 2,048-token limits) default to the final epoch checkpoint (Appendix~\ref{app:hyperparams}). Qwen3 \cwm{} runs show early overfitting (best at ${\sim}$6\% of training); checkpoint details in Appendix~\ref{app:hyperparams}.
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with LoRA~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds (3 bfloat16, 2 NF4~\cite{dettmers2024qlora}). DeepSeek-Coder-6.7B~\cite{guo2024deepseekcoder} serves as a cross-model check (2 seeds). Our \cwm{} baseline uses LoRA fine-tuning for matched comparison, not the 32B CWM~\cite{meta2025cwm}. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4). Full hyperparameters in Appendix~\ref{app:hyperparams}; prompts in Appendix~\ref{app:prompts}.
15	
16	\paragraph{Statistics.}
17	Equivalence uses Two One-Sided Tests (TOST)~\cite{schuirmann1987tost} with $\pm$2\pp{} margin; seed-level paired analysis (df${=}$4 for 5-seed, df${=}$2 for 3-seed) treats each training seed as the unit of replication. Holm-Bonferroni correction~\cite{holm1979} controls family-wise error across the five primary comparisons (Table~\ref{tab:holm}). Confidence intervals use clustered bootstrap~\cite{davison1997bootstrap} (114 problem clusters, 10K resamples); intraclass correlation coefficient (ICC)~\cite{shrout1979icc} quantifies within-problem correlation. Bayesian ROPE and mixed-effects regression supplement these tests. Full statistical power analysis in Appendix~\ref{app:power}.
18	
19	
20	\subsection{Function-Level Results}
21	\label{sec:func_results}
22	
23	Table~\ref{tab:main_results} reports function-level results across formulations and model families.
24	
25	\begin{table}[t]
26	\centering
27	\small
28	\caption{Function-level per-test accuracy on HumanEval+MBPP ($n{=}1{,}890$). Mean $\pm$ std over 5 seeds (Qwen3) or 2 seeds (DeepSeek). Seeds 42/123/456: bfloat16; 789/0: NF4. DeepSeek: $n{=}2$ seeds; std reported for descriptive comparison, not inferential. \traj{}\textsuperscript{$\star$} evaluated on 1,032-sample subset (447 matched variants). All prompting baselines use NF4 4-bit quantization. \textsuperscript{$\star$}Training configuration differs (\S\ref{sec:repo}).}
29	\label{tab:main_results}
30	\resizebox{\columnwidth}{!}{%
31	\setlength{\tabcolsep}{4pt}
32	\begin{tabular}{llcc}
33	\toprule
34	\textbf{Method} & \textbf{Model} & \textbf{Seeds} & \textbf{Accuracy (\%)} \\
35	\midrule
36	\multicolumn{4}{l}{\emph{Qwen3 (primary)}} \\
37	\cls{} (fine-tuned) & 4B & 5 & \textbf{88.43 $\pm$ 0.78} \\
38	\cwm{} (fine-tuned) & 4B & 5 & \underline{87.19 $\pm$ 0.37} \\
39	\traj{}\textsuperscript{$\star$} (fine-tuned) & 4B & 5 & 86.30 $\pm$ 0.97 \\
40	\midrule
41	\multicolumn{4}{l}{\emph{DeepSeek-Coder (cross-model consistency check)}} \\
42	\cls{} (fine-tuned) & 6.7B & 2 & \textbf{86.85 $\pm$ 0.11} \\
43	\cwm{} (fine-tuned) & 6.7B & 2 & \underline{86.83 $\pm$ 1.49} \\
44	\traj{}\textsuperscript{$\star$} (fine-tuned) & 6.7B & 2 & 84.16 $\pm$ 1.30 \\
45	\midrule
46	\multicolumn{4}{l}{\emph{Prompting baselines}} \\
47	0-shot & 8B (Qwen3) & 1 & 60.53 \\
48	0-shot & 14B (Qwen3) & 1 & 66.24 \\
49	0-shot & 6.7B (DeepSeek) & 1 & 63.02 \\
50	ZS LLM-as-judge & 8B (Qwen3) & 1 & 64.40 \\
51	ZS LLM-as-judge & 6.7B (DeepSeek) & 1 & 56.56 \\
52	ZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\
53	3-shot ICL & 8B (Qwen3) & 1 & 60.42 \\
54	3-shot ICL & 14B (Qwen3) & 1 & 73.12 \\
55	3-shot ICL & 6.7B (DeepSeek) & 1 & 59.95 \\
56	\midrule
57	Majority (pass) & --- & --- & 51.75 \\
58	\bottomrule
59	\end{tabular}}
60	\end{table}
61	
62	All three formulations achieve comparable accuracy on Qwen3-4B: \cls{} 88.43\%, \cwm{} 87.19\%, \traj{} 86.30\% (Table~\ref{tab:main_results}). The \cls{}--\cwm{} gap (0.02--1.24\pp{}) is within seed noise across both families; the \cls{}--\traj{} gap (2.13--2.69\pp{}) exceeds the $\pm$2\pp{} equivalence margin on DeepSeek-Coder (\S\ref{sec:equivalence}). Zero-shot baselines confirm that repo-level verification requires fine-tuning (35--36\pp{} gains) and that formulation choice matters only at repo level (\cls{} outperforms \cwm{} by 18--26\pp{}).
63	
64	
65	\subsection{Scaling Behavior}
66	\label{sec:scaling}
67	
68	Beyond overall accuracy, we examine whether formulation ranking is stable across model sizes. Table~\ref{tab:scaling} compares all three formulations at 4B, 8B, and 14B. The 4B and 8B rows use seeds 42 and 123; the 14B row uses seeds 42, 123, and 456. All rows use bfloat16 inference.
69	
70	\begin{figure}[t]
71	\centering
72	\includegraphics[width=\columnwidth]{figures/paper/figure2_v3.pdf}
73	\caption{Function-level accuracy scaling (4B--14B). CLS and CWM accuracy with shaded gap region; $y$-axis does not start at zero. The \cls{}--\cwm{} gap shows a non-monotonic pattern: 1.32\pp{} at 4B, widening to 2.62\pp{} at 8B, then narrowing to 0.43\pp{} at 14B (3 seeds).}
74	\label{fig:scaling_gap}
75	\end{figure}
76	
77	\cls{} and \traj{} both scale positively from 4B to 8B (+1.27\pp{} and +2.13\pp{} respectively), while \cwm{} remains flat ($-$0.03\pp{}). At 8B, the ranking is \cls{} (89.94) $>$ \traj{} (87.70) $>$ \cwm{} (87.33). The \cls{}--\cwm{} gap widens from 1.32\pp{} at 4B to 2.62\pp{} at 8B (Figure~\ref{fig:scaling_gap}); clustered bootstrap on the 3-seed superset (42, 123, 456 for \cls{}/\cwm{}) yields $p = 0.0066$ (95\% CI $[1.80, 2.71]$), which confirms the widening is not a sampling artifact.
78	
79	At 14B (3 seeds), all three formulations converge in point estimates: \cls{} 89.93$\pm$0.80\%, \cwm{} 89.50$\pm$0.67\%, \traj{} 88.86$\pm$0.77\%. The maximum pairwise gap (\cls{}--\traj{}) narrows from 3.11\pp{} at 4B to 1.07\pp{} at 14B, within the $\pm$2\pp{} equivalence margin. Seed-level TOST (df${=}$2) is inconclusive for equivalence in both pairs ($p{=}0.076$ for \cls{}--\cwm{}, $p{=}0.187$ for \cls{}--\traj{}), reflecting the low power inherent in 3-seed comparisons; Bayesian ROPE provides moderate support ($P(\text{ROPE}){=}0.887$ and $0.780$ respectively; Appendix~\ref{app:bayesian_rope}). \cwm{}'s delayed scaling onset (flat from 4B to 8B, then +2.17\pp{} at 14B) and \traj{}'s decelerating convergence (+2.13\pp{} at 8B, +1.16\pp{} at 14B) are both consistent with capacity-dependent convergence at function level.
80	
81	\paragraph{Baseline scaling.} Prompting baselines remain well below fine-tuning: the best result (14B 3-shot, 73.12\%) is 16.82\pp{} below fine-tuned \cls{} at 8B. Only \cls{} scales positively across both complexity levels; \traj{} shows negligible repo-level scaling (72.92\% at 4B, 73.61\% at 8B).
82	
83	
84	\subsection{Function-Level Equivalence}
85	\label{sec:equivalence}
86	
87	We test pairwise equivalence on 523 variant-level instances across five seeds.\footnote{Seeds 789/0 use NF4 inference; the remaining three use bfloat16. Restricting to bfloat16 only: \cls{}--\cwm{} remains significant ($p{<}0.05$); \cls{}--\traj{} yields $p{=}0.128$.} Our Smallest Effect Size of Interest (SESOI) threshold of $\pm$2\pp{}~\cite{lakens2017,wellek2010} is domain-motivated but not pre-registered: at 85--88\% accuracy, 2\pp{} corresponds to ${\sim}$2--3 problems out of 114, below practitioner-relevant differences, and is consistent with between-seed variation (0.37--0.97\pp{} std). Within-problem predictions are correlated (ICC $= 0.191$, design effect [DEFF] $= 3.97$~\cite{moulton1990}); confidence intervals use clustered bootstrap (\S\ref{sec:setup}). Sensitivity analysis shows \cls{}--\cwm{} equivalence is robust across margins down to $\pm$1.63\pp{} (Table~\ref{tab:tost_sensitivity}); \cls{}--\traj{} equivalence is margin-sensitive ($\pm$1.5\pp{}: $p{=}0.068$).
88	
89	\begin{figure}[t]
90	\centering
91	\includegraphics[width=\columnwidth]{figures/paper/fig_tost_sensitivity.pdf}
92	\caption{TOST $p$-value as a function of equivalence margin. \cls{}--\cwm{} achieves equivalence at $\pm$1.63\pp{}; \cls{}--\traj{} crosses $\alpha{=}0.05$ near $\pm$1.8\pp{} but does not survive Holm correction. Log scale.}
93	\label{fig:tost_sensitivity}
94	\end{figure}
95	
96	\paragraph{\cls{}--\cwm{} equivalence.} The pooled gap is 1.24\pp{} (88.43\%--87.19\%); TOST confirms equivalence at $p = 0.007$ ($\pm$2\pp{} margin), surviving Holm-Bonferroni correction ($k{=}5$, adjusted $p{=}0.028$; Table~\ref{tab:holm}). Equivalence holds at margins as tight as $\pm$1.63\pp{} (Figure~\ref{fig:tost_sensitivity}). On DeepSeek-Coder, the \cls{}--\cwm{} gap of 0.02\pp{} is consistent with equivalence but underpowered (2 seeds).
97	
98	\paragraph{\cls{}--\traj{} equivalence.} The pooled gap is $-$0.45\pp{} (95\% CI [$-$1.71, +0.84]); TOST yields $p = 0.025$ ($\pm$2\pp{}), nominally significant but not surviving Holm-Bonferroni correction ($k{=}5$, adjusted $p{=}0.075$; Table~\ref{tab:holm}). The DeepSeek \cls{}--\traj{} gap (2.69\pp{}) exceeds the $\pm$2\pp{} margin; \traj{} parity is model-dependent. This holds under different training recipes (data volume and label granularity; \S\ref{sec:repo}). Per-test classification provides diagnostic information at no accuracy cost, paralleling process supervision~\cite{lightman2023letsverify}.
99	
100	\begin{table}[t]
101	\centering
102	\small
103	\caption{Model-size scaling: accuracy (\%) at 4B, 8B, and 14B (Qwen3). Seeds 42/123 (4B/8B), seeds 42/123/456 (14B). All bfloat16 inference. $\Delta$: change from previous size. \cwm{} and \traj{}\textsuperscript{$\star$} use $n{=}2$ seeds (4B/8B) and $n{=}3$ seeds (14B). \traj{}\textsuperscript{$\star$} evaluated on 1{,}032-sample subset; \cls{}/\cwm{} use the full 1{,}890-sample set. \textsuperscript{$\star$}Training configuration differs (\S\ref{sec:repo}).}
104	\label{tab:scaling}
105	\setlength{\tabcolsep}{3pt}
106	\begin{tabular}{llccccc}
107	\toprule
108	\textbf{Method} & \textbf{Size} & \textbf{s42} & \textbf{s123} & \textbf{s456} & \textbf{Mean} & \textbf{$\Delta$} \\
109	\midrule
110	\multirow{3}{*}{\cls{}} & 4B & 87.83 & 89.52 & --- & \textbf{88.68} & --- \\
111	 & 8B & \textbf{90.48} & 89.40 & --- & \textbf{89.94} & +1.27 \\
112	 & 14B & 89.21 & \textbf{90.79} & 89.79 & \textbf{89.93 $\pm$ 0.80} & $-$0.01 \\
113	\midrule
114	\multirow{3}{*}{\cwm{}} & 4B & 87.51 & 87.20 & --- & \underline{87.36} & --- \\
115	 & 8B & 87.67 & 86.98 & --- & 87.33 & $-$0.03 \\
116	 & 14B & 89.26 & 88.99 & 90.26 & \underline{89.50 $\pm$ 0.67} & +2.17 \\
117	\midrule
118	\multirow{3}{*}{\traj{}} & 4B & 85.66 & 85.47 & --- & 85.57 & --- \\
119	 & 8B & 87.60 & 87.79 & --- & \underline{87.70} & +2.13 \\
120	 & 14B & 89.73 & 88.57 & 88.28 & 88.86 $\pm$ 0.77 & +1.16 \\
121	\bottomrule
122	\end{tabular}
123	\end{table}
124	
125	\paragraph{Statistical power.} With $n_{\text{eff}} \approx 86$ after clustering, TOST power is ${\sim}$0.3~\cite{cohen1988}. The \cls{}--\cwm{} equivalence ($p{=}0.007$) is robust; the \cls{}--\traj{} inconclusive result (adjusted $p{=}0.075$) may reflect insufficient power ($n_{\text{eff}} \approx 350$ needed for ${\geq}$0.8 power). Bayesian ROPE corroborates: $P(\text{ROPE}){=}0.975$ for \cls{}--\cwm{}; \cls{}--\traj{} $P(\text{ROPE}){=}0.970$ at variant level but 0.542 at per-test level (Appendix~\ref{app:bayesian_rope}).
126	
127	
128	\subsection{Repo-Level: Complexity-Dependent Divergence}
129	\label{sec:repo}
130	
131	Table~\ref{tab:repo_level} compares formulations at repository-level complexity. The following results are established under ${\leq}$8B LoRA; preliminary 14B evidence (\S\ref{sec:scaling}) suggests these gaps may narrow at larger scales. Variant-level comparisons ($n{=}48$) are exploratory due to limited seed coverage; the per-test interaction effect is statistically confirmed (see below). Checkpoints are val-selected where validation loss is computable (\S\ref{sec:setup}); the test set has zero problem overlap with validation.
132	
133	\begin{table}[t]
134	\centering
135	\small
136	\caption{Repo-level cross-formulation comparison on SWE-bench Verified test set. Qwen3-8B \cls{}/\traj{}: mean $\pm$ std over 3 seeds; DeepSeek \cls{}: 2 seeds\textsuperscript{$\ddagger$}; DeepSeek \traj{}: 3 seeds; Qwen3-4B: seed 42. \cwm{}: 3 seeds (42/123/456).}
137	\label{tab:repo_level}
138	\resizebox{\columnwidth}{!}{%
139	\setlength{\tabcolsep}{4pt}
140	\begin{tabular}{lcccc}
141	\toprule
142	\textbf{Model} & \textbf{\cls{} (\%)} & \textbf{\cls{} Var.\ (\%)} & \textbf{\cwm{} (\%)} & \textbf{\traj{} Var.\ (\%)\textsuperscript{$\diamond$}} \\
143	\midrule
144	Qwen3-4B & 83.63 & 64.58 & 58.04 & 72.92 \\
145	Qwen3-8B & \textbf{84.83 $\pm$ 0.67} & 72.92 / 81.25\textsuperscript{$\dagger$} & 66.48 $\pm$ 1.14 & 73.61 $\pm$ 3.18 \\
146	DeepSeek-6.7B & 84.38 $\pm$ 2.50\textsuperscript{$\ddagger$} & 81.25\textsuperscript{$\dagger$} & 58.30 $\pm$ 2.82 & 77.08 $\pm$ 3.61 \\
147	\midrule
148	0-shot (Qwen3-8B) & 49.90 & --- & --- & --- \\
149	0-shot (DeepSeek) & 48.54 & --- & --- & --- \\
150	Majority & 72.96 & 54.17 & 72.96 & 54.17 \\
151	\bottomrule
152	\end{tabular}}
153	
154	\vspace{2pt}
155	{\footnotesize
156	\textsuperscript{$\dagger$}Individual-seed variant accuracy.\\
157	\textsuperscript{$\ddagger$}One seed excluded: truncate preprocessing$\to$NaN val loss, decision collapse (Table~\ref{tab:taxonomy}); mean over two matched seeds.\\
158	\textsuperscript{$\diamond$}Var.\ columns: variant-level accuracy ($n{=}48$); \cls{} aggregated via all-pass rule; \traj{} by design. Per-test: $n{=}9{,}784$. \cwm{} unparseable: 54\% (4B); default to pass; parseable-only 38--43\%, below majority. Eval seq\_length differs across models (Appendix~\ref{app:threats}). \cwm{} uses final-epoch checkpoint (step 6633) for s123/s456; s42 uses an earlier checkpoint (step 400) from a prior training configuration. Val loss is undefined for DeepSeek \cwm{} runs (Qwen3 \cwm{} has valid val loss; see \S\ref{sec:setup}). Checkpoint sensitivity analysis in Appendix~\ref{app:cwm_convergence}.}
159	\end{table}
160	
161	Few-shot prompting (3-shot ICL) collapses to an always-predict-unresolved baseline (variant accuracy 45.83\%, below majority 54.17\%; Appendix~\ref{app:few_shot}); execution-free verification requires task-specific fine-tuning regardless of formulation. Fine-tuning yields 35--36\pp{} gains (Table~\ref{tab:repo_level}), a prerequisite before formulation choice becomes relevant.
162	
163	\paragraph{Formulation divergence.} Under our 4--8B LoRA protocol, \cls{} and \cwm{} diverge: the gap is 25.59\pp{} at 4B and 18.35\pp{} at 8B (Table~\ref{tab:repo_level}), with \cwm{} falling below majority baseline at both scales. Limited seed coverage and multiple confounds (\S\ref{sec:threats}) limit causal attribution.
164	
165	\paragraph{Cross-model consistency.} DeepSeek-Coder shows the same direction (\cls{} $>$ \cwm{}) across all seeds; gap variation across families (20\pp{} Qwen3 vs.\ 23--28\pp{} DeepSeek) narrows to ${\sim}$2\pp{} under matched checkpoints (Appendix~\ref{app:threats}). All six \cwm{} repo-level seeds exhibit format collapse ($>$50\% unparseable), ruling out seed-specific artifacts.
166	
167	\paragraph{Failure mode taxonomy.} Variant-level analysis ($n{=}48$) identifies three failure modes (Table~\ref{tab:taxonomy}; full variant-level and per-mutation breakdowns in Appendices~\ref{app:variant_level} and~\ref{app:repo_mutation}): format collapse (\cwm{}, 53--74\% unparseable), decision collapse (\cls{} under truncate preprocessing, fail recall ${\sim}$14\%), and aggregation penalty (\cls{} under drop preprocessing, fail recall 38--57\%). Decision collapse is configuration-dependent, not model-inherent. \traj{} avoids aggregation penalty by predicting variant outcomes directly (72.92--77.08\%). Downsampling \cls{} to match \traj{}'s data volume still yields 80.74\% (+7.82\pp{} above \traj{}; Appendix~\ref{app:downsample}). The CLS--TRAJ repo-level comparison remains exploratory: downsample ablation controls data volume but not label granularity (per-test vs.\ variant-level), a formulation-inherent confound that cannot be experimentally resolved.
168	
169	\paragraph{Default assignment artifact.} The apparent \cwm{} accuracy increase from 4B to 8B is an artifact of rising unparseable rate (53.7\%$\to$73.8\%), inflating accuracy via majority-class default while parseable-only accuracy decreases (42.88\%$\to$38.52\%); cross-seed evidence confirms the pattern (Appendix~\ref{app:parseable_bias}).
170	
171	\paragraph{Complexity as moderator.} The \cls{}--\cwm{} gap widens from 1--3\pp{} (function) to 18--26\pp{} (repo) under our protocol; a matched-context ablation confirms input disparity explains $<$3\% of this gap (Appendix~\ref{app:ablations}). While the directional advantage of lower-complexity output formulations may be anticipated from \S\ref{sec:failure-modes}, the magnitude of this gap, the function-level equivalence, and the specific failure mechanisms (Table~\ref{tab:taxonomy}) were not predictable a priori.
172	
173	\paragraph{Formulation$\times$complexity interaction.} A mixed-effects linear probability model (LPM) ($n{=}56{,}480$, 139 clusters, DeepSeek-Coder) confirms: \cwm{} effect at function level is negligible ($\hat{\beta}{=}-0.002$, $p{=}0.805$), but the formulation$\times$complexity interaction is highly significant ($z{=}-23.7$, $p{<}0.001$). A cross-model LPM confirms formulation dominates ($\hat{\beta}{=}-0.22$ vs.\ model $\hat{\beta}{=}+0.011$); model identity significance is estimator-dependent (LPM $p{=}0.002$; generalized estimating equations [GEE] $p{=}0.449$), consistent with limited clusters ($k{=}25 < 40$; Appendix~\ref{app:interaction}).
174	
175	\begin{table}[t]
176	\centering
177	\small
178	\caption{Repo-level failure mode taxonomy. Variant-level majority baseline: 54.17\%.}
179	\label{tab:taxonomy}
180	\setlength{\tabcolsep}{3pt}
181	\resizebox{\columnwidth}{!}{%
182	\begin{tabular}{llcc}
183	\toprule
184	\textbf{Failure Mode} & \textbf{Representative} & \textbf{Fail Recall} & \textbf{Variant Acc} \\
185	\midrule
186	Format collapse & \cwm{} (all) & N/A & 48--52\% \\
187	Decision collapse & \cls{} (DeepSeek, s123) & ${\sim}$14\% & 56\% \\
188	Aggr.\ penalty & \cls{} (Qwen3-8B) & 51--57\% & 73--81\% \\
189	Aggr.\ penalty & \cls{} (DeepSeek, s42) & 38--51\% & 79--81\% \\
190	\bottomrule
191	\end{tabular}}
192	\end{table}
193	
194	\subsection{Analysis}
195	\label{sec:analysis}
196	
197	\paragraph{Aggregation penalty.} The aggregation penalty ranges from 1.36\pp{} to 19\pp{}, negligible at function level ($\bar{T} \approx 2.3$) but substantial at repo level ($\bar{T} \gg 10$; Appendix~\ref{app:extended_analysis}(a)).
198	
199	\begin{figure}[t]
200	\centering
201	\includegraphics[width=\columnwidth]{figures/paper/fig_cwm_unparseable.pdf}
202	\caption{\cwm{} unparseable rate by complexity level. Function-level outputs (${\sim}$5--15 tokens) yield 1.4\% unparseable; repo-level outputs (${\sim}$477 tokens) reach 53.7\% (4B) and 73.8\% (8B). Parseable-only accuracy (inside bars) decreases from 4B to 8B despite rising overall accuracy---evidence of default-assignment inflation.}
203	\label{fig:cwm_unparseable}
204	\end{figure}
205	
206	\paragraph{Why does generation degrade at repo level?} Output complexity increases nonlinearly: function-level outputs average ${\sim}$5--15 tokens; repo-level outputs average ${\sim}$477 tokens (Figure~\ref{fig:cwm_unparseable}), leading to format collapse (53--74\% unparseable; Appendix~\ref{app:qualitative}). Even parseable outputs achieve only 38--43\%, below majority; a model accidentally trained on CLS-format data achieves 86.05\% with 0\% unparseable; this confirms that degradation stems from output format complexity, not task difficulty (Appendix~\ref{app:extended_analysis}(c)). Four targeted interventions all fail to close this gap (Appendix~\ref{app:extended_analysis}(g)). \cls{} achieves 217$\times$ higher throughput (1 vs.\ avg 477 output tokens).
207	
208	\begin{figure}[t]
209	\centering
210	\includegraphics[width=\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}
211	\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\% of instances) and concentrates at $T{=}2$ (19.1\%, contributing 55.3\% of total advantage).}
212	\label{fig:oracle_stratified}
213	\end{figure}
214	
215	\paragraph{Error complementarity.} \cls{} and \cwm{} make partially complementary errors. An oracle combination achieves 90.63\% (+2.80\pp{}; 95\% CI [89.3\%, 91.9\%]; single-seed) at function level and 95.83\% (+14.58\pp{}; $n{=}48$) at repo level (Figure~\ref{fig:oracle_stratified}). Simple routing heuristics capture $<$0.4\pp{} of the oracle gap; the complementarity is instance-specific, so simple heuristics are insufficient. Whether a learned router can capture this advantage remains open (Appendix~\ref{app:oracle}).
216	
217	\subsection{Threats to Validity}
218	\label{sec:threats}
219	
220	We identify five potential confounds (Appendix~\ref{app:threats}): checkpoint selection ($<$1\pp{}), evaluation sequence length (${\sim}$1.5\pp{}), preprocessing (${\sim}$8\pp{}; val-test distribution shift in Appendix~\ref{app:mutation_distribution}), \traj{} training regime, and \cwm{} scale/pretraining (primary limitation). Preprocessing and checkpoint interact, accounting for up to 7.68\pp{} variation within one model (Appendix~\ref{app:threats}). The 18--26\pp{} gap exceeds any single confound, but correlated confounds and limited seeds preclude definitive causal attribution. Holm-Bonferroni ($k{=}5$) confirms the two core claims (adjusted $p{=}0.015$ and $p{=}0.028$; Table~\ref{tab:holm}).
221	
222	\begin{table}[t]
223	\centering
224	\small
225	\caption{Holm-Bonferroni correction for primary comparisons ($k{=}5$). Comparisons ranked by raw $p$-value; each tested against $\alpha / (k - \text{rank} + 1)$.}
226	\label{tab:holm}
227	\setlength{\tabcolsep}{3pt}
228	\resizebox{\columnwidth}{!}{%
229	\begin{tabular}{clcccc}
230	\toprule
231	\textbf{Rank} & \textbf{Comparison} & \textbf{Raw $p$} & \textbf{Factor} & \textbf{Adj $p$} & \textbf{Sig.?} \\
232	\midrule
233	1 & Repo: \cls{} vs \cwm{} & 0.003 & $\times$5 & 0.015 & \checkmark \\
234	2 & Func: \cls{} vs \cwm{} (TOST $\pm$2\pp{}) & 0.007 & $\times$4 & 0.028 & \checkmark \\
235	3 & Func: \cls{} vs \traj{} (TOST $\pm$2\pp{}) & 0.025 & $\times$3 & 0.075 & --- \\
236	4 & Repo: \cwm{} vs \traj{} & 0.039 & $\times$2 & 0.078 & --- \\
237	5 & Repo: \cls{} vs \traj{} & 0.385 & $\times$1 & 0.385 & --- \\
238	\bottomrule
239	\end{tabular}}
240	\end{table}
241	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4d85d50-898b-4256-a14a-b3e3d1a6f8d5",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "5956fbf3-5b8b-4e63-8b30-82d2db879937",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe systematically compare \\cls{}, \\cwm{}, and \\traj{} across two representative code LLM families, two complexity levels, and multiple seeds to characterize the formulation landscape for neural code verification.\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\n\\emph{Function-level}: mutated variants from HumanEval~\\cite{chen2021humaneval} and MBPP~\\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\\approx$ 52:48, majority baseline 51.75\\%).\n\\emph{Repo-level}: per-test instances from SWE-bench Verified~\\cite{chowdhury2024swebenchverified} mutants. ${\\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\\%). Val-based checkpoint selection follows standard practice~\\cite{jimenez2024swebench}; runs with NaN validation loss (due to truncated targets exceeding 2,048-token limits) default to the final epoch checkpoint (Appendix~\\ref{app:hyperparams}). Qwen3 \\cwm{} runs show early overfitting (best at ${\\sim}$6\\% of training); checkpoint details in Appendix~\\ref{app:hyperparams}.\n\n\\paragraph{Models and training.}\nWe fine-tune Qwen3-4B and Qwen3-8B~\\cite{qwen2025qwen3} with LoRA~\\cite{hu2022lora} (rank 16, 3 epochs) across five seeds (3 bfloat16, 2 NF4~\\cite{dettmers2024qlora}). DeepSeek-Coder-6.7B~\\cite{guo2024deepseekcoder} serves as a cross-model check (2 seeds). Our \\cwm{} baseline uses LoRA fine-tuning for matched comparison, not the 32B CWM~\\cite{meta2025cwm}. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4). Full hyperparameters in Appendix~\\ref{app:hyperparams}; prompts in Appendix~\\ref{app:prompts}.\n\n\\paragraph{Statistics.}\nEquivalence uses Two One-Sided Tests (TOST)~\\cite{schuirmann1987tost} with $\\pm$2\\pp{} margin; seed-level paired analysis (df${=}$4 for 5-seed, df${=}$2 for 3-seed) treats each training seed as the unit of replication. Holm-Bonferroni correction~\\cite{holm1979} controls family-wise error across the five primary comparisons (Table~\\ref{tab:holm}). Confidence intervals use clustered bootstrap~\\cite{davison1997bootstrap} (114 problem clusters, 10K resamples); intraclass correlation coefficient (ICC)~\\cite{shrout1979icc} quantifies within-problem correlation. Bayesian ROPE and mixed-effects regression supplement these tests. Full statistical power analysis in Appendix~\\ref{app:power}.\n\n\n\\subsection{Function-Level Results}\n\\label{sec:func_results}\n\nTable~\\ref{tab:main_results} reports function-level results across formulations and model families.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Function-level per-test accuracy on HumanEval+MBPP ($n{=}1{,}890$). Mean $\\pm$ std over 5 seeds (Qwen3) or 2 seeds (DeepSeek). Seeds 42/123/456: bfloat16; 789/0: NF4. DeepSeek: $n{=}2$ seeds; std reported for descriptive comparison, not inferential. \\traj{}\\textsuperscript{$\\star$} evaluated on 1,032-sample subset (447 matched variants). All prompting baselines use NF4 4-bit quantization. \\textsuperscript{$\\star$}Training configuration differs (\\S\\ref{sec:repo}).}\n\\label{tab:main_results}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Method} & \\textbf{Model} & \\textbf{Seeds} & \\textbf{Accuracy (\\%)} \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Qwen3 (primary)}} \\\\\n\\cls{} (fine-tuned) & 4B & 5 & \\textbf{88.43 $\\pm$ 0.78} \\\\\n\\cwm{} (fine-tuned) & 4B & 5 & \\underline{87.19 $\\pm$ 0.37} \\\\\n\\traj{}\\textsuperscript{$\\star$} (fine-tuned) & 4B & 5 & 86.30 $\\pm$ 0.97 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{DeepSeek-Coder (cross-model consistency check)}} \\\\\n\\cls{} (fine-tuned) & 6.7B & 2 & \\textbf{86.85 $\\pm$ 0.11} \\\\\n\\cwm{} (fine-tuned) & 6.7B & 2 & \\underline{86.83 $\\pm$ 1.49} \\\\\n\\traj{}\\textsuperscript{$\\star$} (fine-tuned) & 6.7B & 2 & 84.16 $\\pm$ 1.30 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Prompting baselines}} \\\\\n0-shot & 8B (Qwen3) & 1 & 60.53 \\\\\n0-shot & 14B (Qwen3) & 1 & 66.24 \\\\\n0-shot & 6.7B (DeepSeek) & 1 & 63.02 \\\\\nZS LLM-as-judge & 8B (Qwen3) & 1 & 64.40 \\\\\nZS LLM-as-judge & 6.7B (DeepSeek) & 1 & 56.56 \\\\\nZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\\\\n3-shot ICL & 8B (Qwen3) & 1 & 60.42 \\\\\n3-shot ICL & 14B (Qwen3) & 1 & 73.12 \\\\\n3-shot ICL & 6.7B (DeepSeek) & 1 & 59.95 \\\\\n\\midrule\nMajority (pass) & --- & --- & 51.75 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAll three formulations achieve comparable accuracy on Qwen3-4B: \\cls{} 88.43\\%, \\cwm{} 87.19\\%, \\traj{} 86.30\\% (Table~\\ref{tab:main_results}). The \\cls{}--\\cwm{} gap (0.02--1.24\\pp{}) is within seed noise across both families; the \\cls{}--\\traj{} gap (2.13--2.69\\pp{}) exceeds the $\\pm$2\\pp{} equivalence margin on DeepSeek-Coder (\\S\\ref{sec:equivalence}). Zero-shot baselines confirm that repo-level verification requires fine-tuning (35--36\\pp{} gains) and that formulation choice matters only at repo level (\\cls{} outperforms \\cwm{} by 18--26\\pp{}).\n\n\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nBeyond overall accuracy, we examine whether formulation ranking is stable across model sizes. Table~\\ref{tab:scaling} compares all three formulations at 4B, 8B, and 14B. The 4B and 8B rows use seeds 42 and 123; the 14B row uses seeds 42, 123, and 456. All rows use bfloat16 inference.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/figure2_v3.pdf}\n\\caption{Function-level accuracy scaling (4B--14B). CLS and CWM accuracy with shaded gap region; $y$-axis does not start at zero. The \\cls{}--\\cwm{} gap shows a non-monotonic pattern: 1.32\\pp{} at 4B, widening to 2.62\\pp{} at 8B, then narrowing to 0.43\\pp{} at 14B (3 seeds).}\n\\label{fig:scaling_gap}\n\\end{figure}\n\n\\cls{} and \\traj{} both scale positively from 4B to 8B (+1.27\\pp{} and +2.13\\pp{} respectively), while \\cwm{} remains flat ($-$0.03\\pp{}). At 8B, the ranking is \\cls{} (89.94) $>$ \\traj{} (87.70) $>$ \\cwm{} (87.33). The \\cls{}--\\cwm{} gap widens from 1.32\\pp{} at 4B to 2.62\\pp{} at 8B (Figure~\\ref{fig:scaling_gap}); clustered bootstrap on the 3-seed superset (42, 123, 456 for \\cls{}/\\cwm{}) yields $p = 0.0066$ (95\\% CI $[1.80, 2.71]$), which confirms the widening is not a sampling artifact.\n\nAt 14B (3 seeds), all three formulations converge in point estimates: \\cls{} 89.93$\\pm$0.80\\%, \\cwm{} 89.50$\\pm$0.67\\%, \\traj{} 88.86$\\pm$0.77\\%. The maximum pairwise gap (\\cls{}--\\traj{}) narrows from 3.11\\pp{} at 4B to 1.07\\pp{} at 14B, within the $\\pm$2\\pp{} equivalence margin. Seed-level TOST (df${=}$2) is inconclusive for equivalence in both pairs ($p{=}0.076$ for \\cls{}--\\cwm{}, $p{=}0.187$ for \\cls{}--\\traj{}), reflecting the low power inherent in 3-seed comparisons; Bayesian ROPE provides moderate support ($P(\\text{ROPE}){=}0.887$ and $0.780$ respectively; Appendix~\\ref{app:bayesian_rope}). \\cwm{}'s delayed scaling onset (flat from 4B to 8B, then +2.17\\pp{} at 14B) and \\traj{}'s decelerating convergence (+2.13\\pp{} at 8B, +1.16\\pp{} at 14B) are both consistent with capacity-dependent convergence at function level.\n\n\\paragraph{Baseline scaling.} Prompting baselines remain well below fine-tuning: the best result (14B 3-shot, 73.12\\%) is 16.82\\pp{} below fine-tuned \\cls{} at 8B. Only \\cls{} scales positively across both complexity levels; \\traj{} shows negligible repo-level scaling (72.92\\% at 4B, 73.61\\% at 8B).\n\n\n\\subsection{Function-Level Equivalence}\n\\label{sec:equivalence}\n\nWe test pairwise equivalence on 523 variant-level instances across five seeds.\\footnote{Seeds 789/0 use NF4 inference; the remaining three use bfloat16. Restricting to bfloat16 only: \\cls{}--\\cwm{} remains significant ($p{<}0.05$); \\cls{}--\\traj{} yields $p{=}0.128$.} Our Smallest Effect Size of Interest (SESOI) threshold of $\\pm$2\\pp{}~\\cite{lakens2017,wellek2010} is domain-motivated but not pre-registered: at 85--88\\% accuracy, 2\\pp{} corresponds to ${\\sim}$2--3 problems out of 114, below practitioner-relevant differences, and is consistent with between-seed variation (0.37--0.97\\pp{} std). Within-problem predictions are correlated (ICC $= 0.191$, design effect [DEFF] $= 3.97$~\\cite{moulton1990}); confidence intervals use clustered bootstrap (\\S\\ref{sec:setup}). Sensitivity analysis shows \\cls{}--\\cwm{} equivalence is robust across margins down to $\\pm$1.63\\pp{} (Table~\\ref{tab:tost_sensitivity}); \\cls{}--\\traj{} equivalence is margin-sensitive ($\\pm$1.5\\pp{}: $p{=}0.068$).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig_tost_sensitivity.pdf}\n\\caption{TOST $p$-value as a function of equivalence margin. \\cls{}--\\cwm{} achieves equivalence at $\\pm$1.63\\pp{}; \\cls{}--\\traj{} crosses $\\alpha{=}0.05$ near $\\pm$1.8\\pp{} but does not survive Holm correction. Log scale.}\n\\label{fig:tost_sensitivity}\n\\end{figure}\n\n\\paragraph{\\cls{}--\\cwm{} equivalence.} The pooled gap is 1.24\\pp{} (88.43\\%--87.19\\%); TOST confirms equivalence at $p = 0.007$ ($\\pm$2\\pp{} margin), surviving Holm-Bonferroni correction ($k{=}5$, adjusted $p{=}0.028$; Table~\\ref{tab:holm}). Equivalence holds at margins as tight as $\\pm$1.63\\pp{} (Figure~\\ref{fig:tost_sensitivity}). On DeepSeek-Coder, the \\cls{}--\\cwm{} gap of 0.02\\pp{} is consistent with equivalence but underpowered (2 seeds).\n\n\\paragraph{\\cls{}--\\traj{} equivalence.} The pooled gap is $-$0.45\\pp{} (95\\% CI [$-$1.71, +0.84]); TOST yields $p = 0.025$ ($\\pm$2\\pp{}), nominally significant but not surviving Holm-Bonferroni correction ($k{=}5$, adjusted $p{=}0.075$; Table~\\ref{tab:holm}). The DeepSeek \\cls{}--\\traj{} gap (2.69\\pp{}) exceeds the $\\pm$2\\pp{} margin; \\traj{} parity is model-dependent. This holds under different training recipes (data volume and label granularity; \\S\\ref{sec:repo}). Per-test classification provides diagnostic information at no accuracy cost, paralleling process supervision~\\cite{lightman2023letsverify}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Model-size scaling: accuracy (\\%) at 4B, 8B, and 14B (Qwen3). Seeds 42/123 (4B/8B), seeds 42/123/456 (14B). All bfloat16 inference. $\\Delta$: change from previous size. \\cwm{} and \\traj{}\\textsuperscript{$\\star$} use $n{=}2$ seeds (4B/8B) and $n{=}3$ seeds (14B). \\traj{}\\textsuperscript{$\\star$} evaluated on 1{,}032-sample subset; \\cls{}/\\cwm{} use the full 1{,}890-sample set. \\textsuperscript{$\\star$}Training configuration differs (\\S\\ref{sec:repo}).}\n\\label{tab:scaling}\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Size} & \\textbf{s42} & \\textbf{s123} & \\textbf{s456} & \\textbf{Mean} & \\textbf{$\\Delta$} \\\\\n\\midrule\n\\multirow{3}{*}{\\cls{}} & 4B & 87.83 & 89.52 & --- & \\textbf{88.68} & --- \\\\\n & 8B & \\textbf{90.48} & 89.40 & --- & \\textbf{89.94} & +1.27 \\\\\n & 14B & 89.21 & \\textbf{90.79} & 89.79 & \\textbf{89.93 $\\pm$ 0.80} & $-$0.01 \\\\\n\\midrule\n\\multirow{3}{*}{\\cwm{}} & 4B & 87.51 & 87.20 & --- & \\underline{87.36} & --- \\\\\n & 8B & 87.67 & 86.98 & --- & 87.33 & $-$0.03 \\\\\n & 14B & 89.26 & 88.99 & 90.26 & \\underline{89.50 $\\pm$ 0.67} & +2.17 \\\\\n\\midrule\n\\multirow{3}{*}{\\traj{}} & 4B & 85.66 & 85.47 & --- & 85.57 & --- \\\\\n & 8B & 87.60 & 87.79 & --- & \\underline{87.70} & +2.13 \\\\\n & 14B & 89.73 & 88.57 & 88.28 & 88.86 $\\pm$ 0.77 & +1.16 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Statistical power.} With $n_{\\text{eff}} \\approx 86$ after clustering, TOST power is ${\\sim}$0.3~\\cite{cohen1988}. The \\cls{}--\\cwm{} equivalence ($p{=}0.007$) is robust; the \\cls{}--\\traj{} inconclusive result (adjusted $p{=}0.075$) may reflect insufficient power ($n_{\\text{eff}} \\approx 350$ needed for ${\\geq}$0.8 power). Bayesian ROPE corroborates: $P(\\text{ROPE}){=}0.975$ for \\cls{}--\\cwm{}; \\cls{}--\\traj{} $P(\\text{ROPE}){=}0.970$ at variant level but 0.542 at per-test level (Appendix~\\ref{app:bayesian_rope}).\n\n\n\\subsection{Repo-Level: Complexity-Dependent Divergence}\n\\label{sec:repo}\n\nTable~\\ref{tab:repo_level} compares formulations at repository-level complexity. The following results are established under ${\\leq}$8B LoRA; preliminary 14B evidence (\\S\\ref{sec:scaling}) suggests these gaps may narrow at larger scales. Variant-level comparisons ($n{=}48$) are exploratory due to limited seed coverage; the per-test interaction effect is statistically confirmed (see below). Checkpoints are val-selected where validation loss is computable (\\S\\ref{sec:setup}); the test set has zero problem overlap with validation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Repo-level cross-formulation comparison on SWE-bench Verified test set. Qwen3-8B \\cls{}/\\traj{}: mean $\\pm$ std over 3 seeds; DeepSeek \\cls{}: 2 seeds\\textsuperscript{$\\ddagger$}; DeepSeek \\traj{}: 3 seeds; Qwen3-4B: seed 42. \\cwm{}: 3 seeds (42/123/456).}\n\\label{tab:repo_level}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{\\cls{} (\\%)} & \\textbf{\\cls{} Var.\\ (\\%)} & \\textbf{\\cwm{} (\\%)} & \\textbf{\\traj{} Var.\\ (\\%)\\textsuperscript{$\\diamond$}} \\\\\n\\midrule\nQwen3-4B & 83.63 & 64.58 & 58.04 & 72.92 \\\\\nQwen3-8B & \\textbf{84.83 $\\pm$ 0.67} & 72.92 / 81.25\\textsuperscript{$\\dagger$} & 66.48 $\\pm$ 1.14 & 73.61 $\\pm$ 3.18 \\\\\nDeepSeek-6.7B & 84.38 $\\pm$ 2.50\\textsuperscript{$\\ddagger$} & 81.25\\textsuperscript{$\\dagger$} & 58.30 $\\pm$ 2.82 & 77.08 $\\pm$ 3.61 \\\\\n\\midrule\n0-shot (Qwen3-8B) & 49.90 & --- & --- & --- \\\\\n0-shot (DeepSeek) & 48.54 & --- & --- & --- \\\\\nMajority & 72.96 & 54.17 & 72.96 & 54.17 \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{2pt}\n{\\footnotesize\n\\textsuperscript{$\\dagger$}Individual-seed variant accuracy.\\\\\n\\textsuperscript{$\\ddagger$}One seed excluded: truncate preprocessing$\\to$NaN val loss, decision collapse (Table~\\ref{tab:taxonomy}); mean over two matched seeds.\\\\\n\\textsuperscript{$\\diamond$}Var.\\ columns: variant-level accuracy ($n{=}48$); \\cls{} aggregated via all-pass rule; \\traj{} by design. Per-test: $n{=}9{,}784$. \\cwm{} unparseable: 54\\% (4B); default to pass; parseable-only 38--43\\%, below majority. Eval seq\\_length differs across models (Appendix~\\ref{app:threats}). \\cwm{} uses final-epoch checkpoint (step 6633) for s123/s456; s42 uses an earlier checkpoint (step 400) from a prior training configuration. Val loss is undefined for DeepSeek \\cwm{} runs (Qwen3 \\cwm{} has valid val loss; see \\S\\ref{sec:setup}). Checkpoint sensitivity analysis in Appendix~\\ref{app:cwm_convergence}.}\n\\end{table}\n\nFew-shot prompting (3-shot ICL) collapses to an always-predict-unresolved baseline (variant accuracy 45.83\\%, below majority 54.17\\%; Appendix~\\ref{app:few_shot}); execution-free verification requires task-specific fine-tuning regardless of formulation. Fine-tuning yields 35--36\\pp{} gains (Table~\\ref{tab:repo_level}), a prerequisite before formulation choice becomes relevant.\n\n\\paragraph{Formulation divergence.} Under our 4--8B LoRA protocol, \\cls{} and \\cwm{} diverge: the gap is 25.59\\pp{} at 4B and 18.35\\pp{} at 8B (Table~\\ref{tab:repo_level}), with \\cwm{} falling below majority baseline at both scales. Limited seed coverage and multiple confounds (\\S\\ref{sec:threats}) limit causal attribution.\n\n\\paragraph{Cross-model consistency.} DeepSeek-Coder shows the same direction (\\cls{} $>$ \\cwm{}) across all seeds; gap variation across families (20\\pp{} Qwen3 vs.\\ 23--28\\pp{} DeepSeek) narrows to ${\\sim}$2\\pp{} under matched checkpoints (Appendix~\\ref{app:threats}). All six \\cwm{} repo-level seeds exhibit format collapse ($>$50\\% unparseable), ruling out seed-specific artifacts.\n\n\\paragraph{Failure mode taxonomy.} Variant-level analysis ($n{=}48$) identifies three failure modes (Table~\\ref{tab:taxonomy}; full variant-level and per-mutation breakdowns in Appendices~\\ref{app:variant_level} and~\\ref{app:repo_mutation}): format collapse (\\cwm{}, 53--74\\% unparseable), decision collapse (\\cls{} under truncate preprocessing, fail recall ${\\sim}$14\\%), and aggregation penalty (\\cls{} under drop preprocessing, fail recall 38--57\\%). Decision collapse is configuration-dependent, not model-inherent. \\traj{} avoids aggregation penalty by predicting variant outcomes directly (72.92--77.08\\%). Downsampling \\cls{} to match \\traj{}'s data volume still yields 80.74\\% (+7.82\\pp{} above \\traj{}; Appendix~\\ref{app:downsample}). The CLS--TRAJ repo-level comparison remains exploratory: downsample ablation controls data volume but not label granularity (per-test vs.\\ variant-level), a formulation-inherent confound that cannot be experimentally resolved.\n\n\\paragraph{Default assignment artifact.} The apparent \\cwm{} accuracy increase from 4B to 8B is an artifact of rising unparseable rate (53.7\\%$\\to$73.8\\%), inflating accuracy via majority-class default while parseable-only accuracy decreases (42.88\\%$\\to$38.52\\%); cross-seed evidence confirms the pattern (Appendix~\\ref{app:parseable_bias}).\n\n\\paragraph{Complexity as moderator.} The \\cls{}--\\cwm{} gap widens from 1--3\\pp{} (function) to 18--26\\pp{} (repo) under our protocol; a matched-context ablation confirms input disparity explains $<$3\\% of this gap (Appendix~\\ref{app:ablations}). While the directional advantage of lower-complexity output formulations may be anticipated from \\S\\ref{sec:failure-modes}, the magnitude of this gap, the function-level equivalence, and the specific failure mechanisms (Table~\\ref{tab:taxonomy}) were not predictable a priori.\n\n\\paragraph{Formulation$\\times$complexity interaction.} A mixed-effects linear probability model (LPM) ($n{=}56{,}480$, 139 clusters, DeepSeek-Coder) confirms: \\cwm{} effect at function level is negligible ($\\hat{\\beta}{=}-0.002$, $p{=}0.805$), but the formulation$\\times$complexity interaction is highly significant ($z{=}-23.7$, $p{<}0.001$). A cross-model LPM confirms formulation dominates ($\\hat{\\beta}{=}-0.22$ vs.\\ model $\\hat{\\beta}{=}+0.011$); model identity significance is estimator-dependent (LPM $p{=}0.002$; generalized estimating equations [GEE] $p{=}0.449$), consistent with limited clusters ($k{=}25 < 40$; Appendix~\\ref{app:interaction}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Repo-level failure mode taxonomy. Variant-level majority baseline: 54.17\\%.}\n\\label{tab:taxonomy}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Failure Mode} & \\textbf{Representative} & \\textbf{Fail Recall} & \\textbf{Variant Acc} \\\\\n\\midrule\nFormat collapse & \\cwm{} (all) & N/A & 48--52\\% \\\\\nDecision collapse & \\cls{} (DeepSeek, s123) & ${\\sim}$14\\% & 56\\% \\\\\nAggr.\\ penalty & \\cls{} (Qwen3-8B) & 51--57\\% & 73--81\\% \\\\\nAggr.\\ penalty & \\cls{} (DeepSeek, s42) & 38--51\\% & 79--81\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Analysis}\n\\label{sec:analysis}\n\n\\paragraph{Aggregation penalty.} The aggregation penalty ranges from 1.36\\pp{} to 19\\pp{}, negligible at function level ($\\bar{T} \\approx 2.3$) but substantial at repo level ($\\bar{T} \\gg 10$; Appendix~\\ref{app:extended_analysis}(a)).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig_cwm_unparseable.pdf}\n\\caption{\\cwm{} unparseable rate by complexity level. Function-level outputs (${\\sim}$5--15 tokens) yield 1.4\\% unparseable; repo-level outputs (${\\sim}$477 tokens) reach 53.7\\% (4B) and 73.8\\% (8B). Parseable-only accuracy (inside bars) decreases from 4B to 8B despite rising overall accuracy---evidence of default-assignment inflation.}\n\\label{fig:cwm_unparseable}\n\\end{figure}\n\n\\paragraph{Why does generation degrade at repo level?} Output complexity increases nonlinearly: function-level outputs average ${\\sim}$5--15 tokens; repo-level outputs average ${\\sim}$477 tokens (Figure~\\ref{fig:cwm_unparseable}), leading to format collapse (53--74\\% unparseable; Appendix~\\ref{app:qualitative}). Even parseable outputs achieve only 38--43\\%, below majority; a model accidentally trained on CLS-format data achieves 86.05\\% with 0\\% unparseable; this confirms that degradation stems from output format complexity, not task difficulty (Appendix~\\ref{app:extended_analysis}(c)). Four targeted interventions all fail to close this gap (Appendix~\\ref{app:extended_analysis}(g)). \\cls{} achieves 217$\\times$ higher throughput (1 vs.\\ avg 477 output tokens).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}\n\\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\\% of instances) and concentrates at $T{=}2$ (19.1\\%, contributing 55.3\\% of total advantage).}\n\\label{fig:oracle_stratified}\n\\end{figure}\n\n\\paragraph{Error complementarity.} \\cls{} and \\cwm{} make partially complementary errors. An oracle combination achieves 90.63\\% (+2.80\\pp{}; 95\\% CI [89.3\\%, 91.9\\%]; single-seed) at function level and 95.83\\% (+14.58\\pp{}; $n{=}48$) at repo level (Figure~\\ref{fig:oracle_stratified}). Simple routing heuristics capture $<$0.4\\pp{} of the oracle gap; the complementarity is instance-specific, so simple heuristics are insufficient. Whether a learned router can capture this advantage remains open (Appendix~\\ref{app:oracle}).\n\n\\subsection{Threats to Validity}\n\\label{sec:threats}\n\nWe identify five potential confounds (Appendix~\\ref{app:threats}): checkpoint selection ($<$1\\pp{}), evaluation sequence length (${\\sim}$1.5\\pp{}), preprocessing (${\\sim}$8\\pp{}; val-test distribution shift in Appendix~\\ref{app:mutation_distribution}), \\traj{} training regime, and \\cwm{} scale/pretraining (primary limitation). Preprocessing and checkpoint interact, accounting for up to 7.68\\pp{} variation within one model (Appendix~\\ref{app:threats}). The 18--26\\pp{} gap exceeds any single confound, but correlated confounds and limited seeds preclude definitive causal attribution. Holm-Bonferroni ($k{=}5$) confirms the two core claims (adjusted $p{=}0.015$ and $p{=}0.028$; Table~\\ref{tab:holm}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Holm-Bonferroni correction for primary comparisons ($k{=}5$). Comparisons ranked by raw $p$-value; each tested against $\\alpha / (k - \\text{rank} + 1)$.}\n\\label{tab:holm}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{clcccc}\n\\toprule\n\\textbf{Rank} & \\textbf{Comparison} & \\textbf{Raw $p$} & \\textbf{Factor} & \\textbf{Adj $p$} & \\textbf{Sig.?} \\\\\n\\midrule\n1 & Repo: \\cls{} vs \\cwm{} & 0.003 & $\\times$5 & 0.015 & \\checkmark \\\\\n2 & Func: \\cls{} vs \\cwm{} (TOST $\\pm$2\\pp{}) & 0.007 & $\\times$4 & 0.028 & \\checkmark \\\\\n3 & Func: \\cls{} vs \\traj{} (TOST $\\pm$2\\pp{}) & 0.025 & $\\times$3 & 0.075 & --- \\\\\n4 & Repo: \\cwm{} vs \\traj{} & 0.039 & $\\times$2 & 0.078 & --- \\\\\n5 & Repo: \\cls{} vs \\traj{} & 0.385 & $\\times$1 & 0.385 & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n",
      "numLines": 241,
      "startLine": 1,
      "totalLines": 241
    }
  },
  "sourceToolAssistantUUID": "cd777723-bf4a-4232-8290-f31e26319ba9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-25T21:14:46.287Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Lt69mp4jW5FJgVMbWD7yAX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6710a636-ec78-49fd-ace5-8a2bccd8866b",
  "isSidechain": false,
  "requestId": "req_011CbPyjJFbXiP572yeM8mVa",
  "type": "assistant",
  "uuid": "57079b09-4731-4ee4-9bf9-34f72f65b21b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaM23BQDFXe5A2ztbfTa1m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2976,
      "cache_read_input_tokens": 35139,
      "output_tokens": 742,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2976,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 742,
          "cache_read_input_tokens": 35139,
          "cache_creation_input_tokens": 2976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2976
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

_source line 27 · 2026-05-25T21:14:46.292Z_

<details><summary>↩ Tool result · `toolu_018eMBRJ87guLjzXEsm2AkRS`</summary>

```text
1	\begin{abstract}
2	Execution-free verification promises to replace costly test execution in Large Language Model (LLM)-based program repair, yet practitioners must choose among three fundamentally different formulations with no controlled comparison to guide the decision: per-test classification (\cls{}), execution output generation (\cwm{}), and trajectory-level scoring (\traj{}). We present the first systematic comparison, controlling for model capacity, training data, and evaluation protocol across two code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple random seeds under ${\leq}$8B Low-Rank Adaptation (LoRA) fine-tuning. Our central finding is that \emph{code complexity moderates the classification--generation tradeoff}. When outputs are short (function-level verification), classification and generation achieve statistically equivalent accuracy; trajectory-level parity is model-dependent. When outputs grow longer and more structured (repository-level verification), this equivalence breaks down: generation-based verification suffers format collapse, falling well below classification. At 14B, function-level gaps narrow to approximately one percentage point, but whether the repo-level divergence is capacity-contingent remains open. A failure mode taxonomy and error complementarity analysis provide actionable guidance for formulation selection and motivate complexity-aware routing as a key open direction\footnote{Code and data are available at \url{https://anonymous.4open.science/r/exec-sim-repair-verifier-102B/}.}.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6710a636-ec78-49fd-ace5-8a2bccd8866b",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "748eb3a7-17e3-41fe-8426-d4d4f4b8f6a8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nExecution-free verification promises to replace costly test execution in Large Language Model (LLM)-based program repair, yet practitioners must choose among three fundamentally different formulations with no controlled comparison to guide the decision: per-test classification (\\cls{}), execution output generation (\\cwm{}), and trajectory-level scoring (\\traj{}). We present the first systematic comparison, controlling for model capacity, training data, and evaluation protocol across two code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple random seeds under ${\\leq}$8B Low-Rank Adaptation (LoRA) fine-tuning. Our central finding is that \\emph{code complexity moderates the classification--generation tradeoff}. When outputs are short (function-level verification), classification and generation achieve statistically equivalent accuracy; trajectory-level parity is model-dependent. When outputs grow longer and more structured (repository-level verification), this equivalence breaks down: generation-based verification suffers format collapse, falling well below classification. At 14B, function-level gaps narrow to approximately one percentage point, but whether the repo-level divergence is capacity-contingent remains open. A failure mode taxonomy and error complementarity analysis provide actionable guidance for formulation selection and motivate complexity-aware routing as a key open direction\\footnote{Code and data are available at \\url{https://anonymous.4open.science/r/exec-sim-repair-verifier-102B/}.}.\n\\end{abstract}\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  },
  "sourceToolAssistantUUID": "6710a636-ec78-49fd-ace5-8a2bccd8866b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-25T21:14:46.294Z_

<details><summary>↩ Tool result · `toolu_01Lt69mp4jW5FJgVMbWD7yAX`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\cite{snell2024scaling}. Full execution verification is reliable but expensive (\$1--3 per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}), which has driven demand for execution-free alternatives. Three distinct formulations have emerged for this task: \textbf{generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \textbf{trajectory-level scoring}~\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \textbf{per-test classification}~\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.
5	
6	Despite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. This connects to a broader pattern in NLP: task formulation (classification vs.\ generation vs.\ span extraction) systematically affects performance~\cite{raffel2020t5}, but the conditions under which each wins remain task-dependent and empirically unresolved. Recent evidence that generation-based verification outperforms classification in mathematical reasoning~\cite{hosseini2025genrm} raises a further question: does this advantage transfer to code verification, where outputs are longer and format-constrained? A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?
7	
8	We present the first systematic comparison across two code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds under ${\leq}$8B LoRA fine-tuning. By controlling model capacity, training data, and evaluation protocol, we isolate the effect of formulation choice itself. Our central finding is that \emph{code complexity moderates the classification--generation tradeoff}: at function level, all formulations achieve comparable accuracy; at repository level, this equivalence breaks down as generation-based verification suffers format collapse. Figure~\ref{fig:reformulation} illustrates the three formulations.
9	
10	We make the following contributions:
11	
12	\begin{itemize}[leftmargin=*,itemsep=2pt]
13	\item \textbf{Complexity-moderated equivalence and divergence.} At function level, classification and generation are statistically equivalent; at repository level, generation accuracy drops sharply due to output format complexity, while classification and trajectory scoring remain competitive (\S\ref{sec:equivalence}, \S\ref{sec:repo}).
14	
15	\item \textbf{Scaling evidence.} At 14B, function-level gaps narrow to ${\sim}$1\pp{} across all formulations, but whether the repo-level divergence is capacity-contingent or formulation-inherent remains open (\S\ref{sec:scaling}).
16	
17	\item \textbf{Error complementarity.} An oracle analysis shows that formulations make partially complementary errors, with upper bounds substantially above individual formulations, providing quantitative motivation for complexity-aware routing (\S\ref{sec:analysis}).
18	
19	\item \textbf{Failure mode taxonomy.} We identify three distinct failure modes at repository level---format collapse, decision collapse, and aggregation penalty---each tied to specific formulation--complexity interactions and amenable to targeted mitigation (\S\ref{sec:repo}).
20	\end{itemize}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57079b09-4731-4ee4-9bf9-34f72f65b21b",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "15636d18-e5ed-45e9-bade-5b53ee2e00b5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\\cite{snell2024scaling}. Full execution verification is reliable but expensive (\\$1--3 per candidate at repository scale\\footnote{Based on per-instance costs reported by \\citet{yang2024sweagent} and \\citet{xia2024agentless}.}), which has driven demand for execution-free alternatives. Three distinct formulations have emerged for this task: \\textbf{generation-based simulation}~\\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \\textbf{trajectory-level scoring}~\\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \\textbf{per-test classification}~\\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.\n\nDespite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. This connects to a broader pattern in NLP: task formulation (classification vs.\\ generation vs.\\ span extraction) systematically affects performance~\\cite{raffel2020t5}, but the conditions under which each wins remain task-dependent and empirically unresolved. Recent evidence that generation-based verification outperforms classification in mathematical reasoning~\\cite{hosseini2025genrm} raises a further question: does this advantage transfer to code verification, where outputs are longer and format-constrained? A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?\n\nWe present the first systematic comparison across two code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds under ${\\leq}$8B LoRA fine-tuning. By controlling model capacity, training data, and evaluation protocol, we isolate the effect of formulation choice itself. Our central finding is that \\emph{code complexity moderates the classification--generation tradeoff}: at function level, all formulations achieve comparable accuracy; at repository level, this equivalence breaks down as generation-based verification suffers format collapse. Figure~\\ref{fig:reformulation} illustrates the three formulations.\n\nWe make the following contributions:\n\n\\begin{itemize}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Complexity-moderated equivalence and divergence.} At function level, classification and generation are statistically equivalent; at repository level, generation accuracy drops sharply due to output format complexity, while classification and trajectory scoring remain competitive (\\S\\ref{sec:equivalence}, \\S\\ref{sec:repo}).\n\n\\item \\textbf{Scaling evidence.} At 14B, function-level gaps narrow to ${\\sim}$1\\pp{} across all formulations, but whether the repo-level divergence is capacity-contingent or formulation-inherent remains open (\\S\\ref{sec:scaling}).\n\n\\item \\textbf{Error complementarity.} An oracle analysis shows that formulations make partially complementary errors, with upper bounds substantially above individual formulations, providing quantitative motivation for complexity-aware routing (\\S\\ref{sec:analysis}).\n\n\\item \\textbf{Failure mode taxonomy.} We identify three distinct failure modes at repository level---format collapse, decision collapse, and aggregation penalty---each tied to specific formulation--complexity interactions and amenable to targeted mitigation (\\S\\ref{sec:repo}).\n\\end{itemize}\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  },
  "sourceToolAssistantUUID": "57079b09-4731-4ee4-9bf9-34f72f65b21b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-25T21:14:46.372Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XbQwKS7HqGHUzFKFoghxrs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15636d18-e5ed-45e9-bade-5b53ee2e00b5",
  "isSidechain": false,
  "requestId": "req_011CbPyjJFbXiP572yeM8mVa",
  "type": "assistant",
  "uuid": "2e26c799-a6c1-42e3-aae2-f20c1d80898c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaM23BQDFXe5A2ztbfTa1m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2976,
      "cache_read_input_tokens": 35139,
      "output_tokens": 742,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2976,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 742,
          "cache_read_input_tokens": 35139,
          "cache_creation_input_tokens": 2976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2976
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

_source line 30 · 2026-05-25T21:14:46.376Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EuFU27hzmqJtnJmgd2B6VG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e26c799-a6c1-42e3-aae2-f20c1d80898c",
  "isSidechain": false,
  "requestId": "req_011CbPyjJFbXiP572yeM8mVa",
  "type": "assistant",
  "uuid": "183f447b-d081-4ab9-ab36-95fc950d952c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaM23BQDFXe5A2ztbfTa1m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2976,
      "cache_read_input_tokens": 35139,
      "output_tokens": 742,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2976,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 742,
          "cache_read_input_tokens": 35139,
          "cache_creation_input_tokens": 2976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2976
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

_source line 31 · 2026-05-25T21:14:46.379Z_

<details><summary>↩ Tool result · `toolu_01XbQwKS7HqGHUzFKFoghxrs`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation and Verification.}
5	Execution trace generation improves code reasoning~\cite{nye2021scratchpad}, with extensions to output prediction~\cite{meta2025cwm,maimon2026selfexecution,liu2024codemind,liu2023codeexecutor,lee2026solidcoder}, failure analysis~\cite{abdollahi2025demystifying}, and error detection~\cite{li2024redo}. CRUXEval~\citep{gu2024cruxeval} benchmarks code execution prediction at function level; RepoExec~\citep{nam2025repoexec} evaluates repo-level code generation with execution-based correctness checks. Our work extends execution prediction to repo-level repair verification. Verification formulations span trajectory-level reward~\cite{shum2025swerm}, process-level feedback~\cite{li2025codeprm,xu2025patchreasoner}, per-test classification~\cite{ni2023lever,chen2023codet}, learned metrics~\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}, and RL with execution-based rewards~\cite{wang2026verpo,tang2026execverify}. Aletheia~\cite{venkatkrishna2026aletheia} compares training recipes; we compare \emph{formulations}. Test-time scaling~\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\cite{wang2023selfconsistency} demonstrate verification value; none compare formulations at matched capacity.
6	
7	\paragraph{Process vs.\ Outcome Supervision.}
8	PRMs outperform ORMs for math reasoning~\cite{lightman2023letsverify,uesato2022solving}, with code-specific extensions~\cite{ye2025prlcoder,zhang2026funprm,jiang2025coderlplus,li2025codeprm}. GenRM~\cite{hosseini2025genrm} and GenPRM~\cite{zhao2026genprm} show generative verifiers outperform discriminative ones for math; our results reveal a domain difference---in code, the generative formulation does not outperform classification, which points to domain-specific tradeoffs (Appendix~\ref{app:threats}). In reward modeling terms, \cls{} maps to PRM, \traj{} to ORM, and \cwm{} to generative verification~\cite{hosseini2025genrm}; we also vary output format.
9	
10	\paragraph{Repair, Mutation Testing, and Task Framing.}
11	CodeRL~\cite{le2022coderl}, AlphaCode~\cite{li2022alphacode,alphacode2023team}, and Reflexion~\cite{shinn2023reflexion} use execution feedback for repair. SWE-bench~\cite{jimenez2024swebench,chowdhury2024swebenchverified} benchmarks and SWE-agent~\cite{yang2024sweagent}/Agentless~\cite{xia2024agentless} demonstrate pipelines where verification is a bottleneck~\cite{yang2025aprsurvey}. Predictive mutation testing~\cite{tufano2019predictive,kim2022predictive,wang2024llmmutation,jain2023contextual} shares our per-test structure. \citet{raffel2020t5} showed that task framing affects NLP performance; we find that complexity moderates the classification--generation tradeoff in code verification.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e26c799-a6c1-42e3-aae2-f20c1d80898c",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "76dd7d8b-9e70-4cbb-af52-71f0b1bb6f25",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Execution Simulation and Verification.}\nExecution trace generation improves code reasoning~\\cite{nye2021scratchpad}, with extensions to output prediction~\\cite{meta2025cwm,maimon2026selfexecution,liu2024codemind,liu2023codeexecutor,lee2026solidcoder}, failure analysis~\\cite{abdollahi2025demystifying}, and error detection~\\cite{li2024redo}. CRUXEval~\\citep{gu2024cruxeval} benchmarks code execution prediction at function level; RepoExec~\\citep{nam2025repoexec} evaluates repo-level code generation with execution-based correctness checks. Our work extends execution prediction to repo-level repair verification. Verification formulations span trajectory-level reward~\\cite{shum2025swerm}, process-level feedback~\\cite{li2025codeprm,xu2025patchreasoner}, per-test classification~\\cite{ni2023lever,chen2023codet}, learned metrics~\\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}, and RL with execution-based rewards~\\cite{wang2026verpo,tang2026execverify}. Aletheia~\\cite{venkatkrishna2026aletheia} compares training recipes; we compare \\emph{formulations}. Test-time scaling~\\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\\cite{wang2023selfconsistency} demonstrate verification value; none compare formulations at matched capacity.\n\n\\paragraph{Process vs.\\ Outcome Supervision.}\nPRMs outperform ORMs for math reasoning~\\cite{lightman2023letsverify,uesato2022solving}, with code-specific extensions~\\cite{ye2025prlcoder,zhang2026funprm,jiang2025coderlplus,li2025codeprm}. GenRM~\\cite{hosseini2025genrm} and GenPRM~\\cite{zhao2026genprm} show generative verifiers outperform discriminative ones for math; our results reveal a domain difference---in code, the generative formulation does not outperform classification, which points to domain-specific tradeoffs (Appendix~\\ref{app:threats}). In reward modeling terms, \\cls{} maps to PRM, \\traj{} to ORM, and \\cwm{} to generative verification~\\cite{hosseini2025genrm}; we also vary output format.\n\n\\paragraph{Repair, Mutation Testing, and Task Framing.}\nCodeRL~\\cite{le2022coderl}, AlphaCode~\\cite{li2022alphacode,alphacode2023team}, and Reflexion~\\cite{shinn2023reflexion} use execution feedback for repair. SWE-bench~\\cite{jimenez2024swebench,chowdhury2024swebenchverified} benchmarks and SWE-agent~\\cite{yang2024sweagent}/Agentless~\\cite{xia2024agentless} demonstrate pipelines where verification is a bottleneck~\\cite{yang2025aprsurvey}. Predictive mutation testing~\\cite{tufano2019predictive,kim2022predictive,wang2024llmmutation,jain2023contextual} shares our per-test structure. \\citet{raffel2020t5} showed that task framing affects NLP performance; we find that complexity moderates the classification--generation tradeoff in code verification.\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  },
  "sourceToolAssistantUUID": "2e26c799-a6c1-42e3-aae2-f20c1d80898c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-25T21:14:46.381Z_

<details><summary>↩ Tool result · `toolu_01EuFU27hzmqJtnJmgd2B6VG`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	Let $p$ denote a candidate patch and $T = \{t_1, \ldots, t_n\}$ its test suite, where each $t_i$ has label $y_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ from execution. Tests decompose into \emph{fail-to-pass} ($T_{\text{f2p}}$) and \emph{pass-to-pass} ($T_{\text{p2p}}$) subsets; a patch is correct iff $\forall\, t_i{:}\ y_i = \text{\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.
5	
6	\subsection{Verification Formulations}
7	\label{sec:formulations}
8	
9	Let $c_p$ denote the code context (unified diff) of patch $p$.
10	
11	\paragraph{\cls{} (per-test classification).} $f(c_p, t_i) \rightarrow \hat{y}_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\hat{y}_p = \bigwedge_{i} [\hat{y}_i = \text{\textsc{Pass}}]$. Output cost: one token per test.
12	
13	\paragraph{\cwm{} (output generation).}\footnote{We use ``code world model'' following \citet{meta2025cwm} to denote execution output prediction, distinct from world models in model-based reinforcement learning.} $g(c_p, t_i) \rightarrow \hat{o}_i \in \Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\hat{y}_i = \text{\textsc{Pass}}$ iff $\hat{o}_i = o_i^*$.\footnote{Exact string matching is conservative, consistent with \citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Output cost: $\sum_i |\hat{o}_i|$ tokens.
14	
15	\paragraph{\traj{} (trajectory-level).} $h(c_p, T) \rightarrow \hat{y}_p \in \{\text{\textsc{Resolved}}, \text{\textsc{Unresolved}}\}$ predicts a single patch verdict from all tests and provides no per-test signal. \traj{} serves as a granularity control: \cls{}--\traj{} differences isolate the value of per-test decomposition independent of the classification formulation itself.
16	
17	\subsection{Expected Failure Modes}
18	\label{sec:failure-modes}
19	
20	Each formulation has characteristic failure modes that differ in their sensitivity to code complexity:
21	
22	\paragraph{Generation failure modes (\cwm{}).} The open-ended output space introduces three failure modes: (1)~\emph{token-budget exhaustion}, where $|o_i^*| > B$ guarantees exact-match failure; (2)~\emph{string-value prediction errors}, where semantically equivalent outputs differing in surface form produce false negatives; and (3)~\emph{format compliance collapse}, where the model fails to produce structured predictions at high complexity. A token sequence of length $L$ with per-token accuracy $q$ has correct-sequence probability $q^L$; long outputs are exponentially harder to predict exactly. We adopt exact string matching following \citet{meta2025cwm}; unparseable predictions default to the majority-class label (\textsc{Pass}).
23	
24	\paragraph{Classification failure modes (\cls{}).} The single-token output eliminates format and truncation failures but constrains reasoning to internal representations. \cls{} errors manifest as false positives or false negatives; at function level, a mild FP bias (56.5\%) emerges.
25	
26	\paragraph{Trajectory-level failure modes (\traj{}).} By collapsing per-test information into a single verdict, \traj{} discards diagnostic granularity but avoids per-test aggregation errors.
27	
28	\paragraph{Complexity dependence.} When outputs are short (function level), generation modes (1)--(2) are rarely triggered and all formulations should perform comparably. As output complexity increases (repository level), generation-specific failures may compound. Whether this divergence is formulation-inherent or capacity-contingent is an empirical question (\S\ref{sec:experiments}).
29	
30	\subsection{Oracle Accuracy-Utility Framework}
31	\label{sec:oracle}
32	
33	For a buggy patch with $k = |T_{\text{f2p}}|$ fail-to-pass tests, a per-test verifier with recall $r$ detects the bug if it identifies at least one failing test: $P_{\text{detect}}(k) = 1 - (1 - r)^{k_{\text{eff}}}$, where $k_{\text{eff}} = k / (1 + (k-1)\rho)$ accounts for within-patch correlation via intraclass correlation coefficient (ICC) $\rho$~\citep{shrout1979icc}. The per-test advantage over a trajectory-level baseline ($a_h$) is $\Delta(k) = P_{\text{detect}}(k) - a_h$, with population expectation $\mathbb{E}[\Delta] = \sum_{k} P(|T_{\text{f2p}}| = k) \cdot \Delta(k)$. This predicts that per-test advantage concentrates in multi-F2P-test instances and vanishes at $k{=}1$, validated in \S\ref{sec:experiments} and Appendix~\ref{app:oracle}.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "183f447b-d081-4ab9-ab36-95fc950d952c",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "96a680b3-1c4f-44c6-895c-6cdf00f0d8ec",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nLet $p$ denote a candidate patch and $T = \\{t_1, \\ldots, t_n\\}$ its test suite, where each $t_i$ has label $y_i \\in \\{\\text{\\textsc{Pass}}, \\text{\\textsc{Fail}}\\}$ from execution. Tests decompose into \\emph{fail-to-pass} ($T_{\\text{f2p}}$) and \\emph{pass-to-pass} ($T_{\\text{p2p}}$) subsets; a patch is correct iff $\\forall\\, t_i{:}\\ y_i = \\text{\\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.\n\n\\subsection{Verification Formulations}\n\\label{sec:formulations}\n\nLet $c_p$ denote the code context (unified diff) of patch $p$.\n\n\\paragraph{\\cls{} (per-test classification).} $f(c_p, t_i) \\rightarrow \\hat{y}_i \\in \\{\\text{\\textsc{Pass}}, \\text{\\textsc{Fail}}\\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\\hat{y}_p = \\bigwedge_{i} [\\hat{y}_i = \\text{\\textsc{Pass}}]$. Output cost: one token per test.\n\n\\paragraph{\\cwm{} (output generation).}\\footnote{We use ``code world model'' following \\citet{meta2025cwm} to denote execution output prediction, distinct from world models in model-based reinforcement learning.} $g(c_p, t_i) \\rightarrow \\hat{o}_i \\in \\Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\\hat{y}_i = \\text{\\textsc{Pass}}$ iff $\\hat{o}_i = o_i^*$.\\footnote{Exact string matching is conservative, consistent with \\citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Output cost: $\\sum_i |\\hat{o}_i|$ tokens.\n\n\\paragraph{\\traj{} (trajectory-level).} $h(c_p, T) \\rightarrow \\hat{y}_p \\in \\{\\text{\\textsc{Resolved}}, \\text{\\textsc{Unresolved}}\\}$ predicts a single patch verdict from all tests and provides no per-test signal. \\traj{} serves as a granularity control: \\cls{}--\\traj{} differences isolate the value of per-test decomposition independent of the classification formulation itself.\n\n\\subsection{Expected Failure Modes}\n\\label{sec:failure-modes}\n\nEach formulation has characteristic failure modes that differ in their sensitivity to code complexity:\n\n\\paragraph{Generation failure modes (\\cwm{}).} The open-ended output space introduces three failure modes: (1)~\\emph{token-budget exhaustion}, where $|o_i^*| > B$ guarantees exact-match failure; (2)~\\emph{string-value prediction errors}, where semantically equivalent outputs differing in surface form produce false negatives; and (3)~\\emph{format compliance collapse}, where the model fails to produce structured predictions at high complexity. A token sequence of length $L$ with per-token accuracy $q$ has correct-sequence probability $q^L$; long outputs are exponentially harder to predict exactly. We adopt exact string matching following \\citet{meta2025cwm}; unparseable predictions default to the majority-class label (\\textsc{Pass}).\n\n\\paragraph{Classification failure modes (\\cls{}).} The single-token output eliminates format and truncation failures but constrains reasoning to internal representations. \\cls{} errors manifest as false positives or false negatives; at function level, a mild FP bias (56.5\\%) emerges.\n\n\\paragraph{Trajectory-level failure modes (\\traj{}).} By collapsing per-test information into a single verdict, \\traj{} discards diagnostic granularity but avoids per-test aggregation errors.\n\n\\paragraph{Complexity dependence.} When outputs are short (function level), generation modes (1)--(2) are rarely triggered and all formulations should perform comparably. As output complexity increases (repository level), generation-specific failures may compound. Whether this divergence is formulation-inherent or capacity-contingent is an empirical question (\\S\\ref{sec:experiments}).\n\n\\subsection{Oracle Accuracy-Utility Framework}\n\\label{sec:oracle}\n\nFor a buggy patch with $k = |T_{\\text{f2p}}|$ fail-to-pass tests, a per-test verifier with recall $r$ detects the bug if it identifies at least one failing test: $P_{\\text{detect}}(k) = 1 - (1 - r)^{k_{\\text{eff}}}$, where $k_{\\text{eff}} = k / (1 + (k-1)\\rho)$ accounts for within-patch correlation via intraclass correlation coefficient (ICC) $\\rho$~\\citep{shrout1979icc}. The per-test advantage over a trajectory-level baseline ($a_h$) is $\\Delta(k) = P_{\\text{detect}}(k) - a_h$, with population expectation $\\mathbb{E}[\\Delta] = \\sum_{k} P(|T_{\\text{f2p}}| = k) \\cdot \\Delta(k)$. This predicts that per-test advantage concentrates in multi-F2P-test instances and vanishes at $k{=}1$, validated in \\S\\ref{sec:experiments} and Appendix~\\ref{app:oracle}.\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  },
  "sourceToolAssistantUUID": "183f447b-d081-4ab9-ab36-95fc950d952c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-25T21:14:50.254Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E7cXgVAoH6CdevEYSdB4Z5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96a680b3-1c4f-44c6-895c-6cdf00f0d8ec",
  "isSidechain": false,
  "requestId": "req_011CbPyjJFbXiP572yeM8mVa",
  "type": "assistant",
  "uuid": "cd777723-bf4a-4232-8290-f31e26319ba9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaM23BQDFXe5A2ztbfTa1m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2976,
      "cache_read_input_tokens": 35139,
      "output_tokens": 742,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2976,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 742,
          "cache_read_input_tokens": 35139,
          "cache_creation_input_tokens": 2976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2976
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

_source line 34 · 2026-05-25T21:14:50.281Z_

<details><summary>↩ Tool result · `toolu_01CdT4G11PhgKt8kNknq3NnX`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic comparison of three execution-free verification formulations (\cls{}, \cwm{}, \traj{}) under ${\leq}$8B LoRA fine-tuning. At function level, \cls{} and \cwm{} are statistically equivalent (TOST $p{=}0.007$, 5 seeds); \traj{} equivalence is inconclusive after Holm correction. At repository level, divergence reaches 18--26\pp{} via three failure modes; the formulation$\times$complexity interaction is highly significant ($z{=}-23.7$, $p{<}0.001$), consistent across families. 14B results narrow function-level gaps to ${\sim}$1\pp{}; whether repo-level divergence is formulation-inherent or capacity-contingent remains open. Scaling to 32B+~\cite{meta2025cwm} and complexity-aware routing are key open questions.
5	
6	\section*{Limitations}
7	
8	Primary findings use ${\leq}$8B LoRA fine-tuning with multi-seed replication; 14B results use a single model family with 3 seeds; cross-family replication at 32B+ is needed. The repo-level gap may diminish with scale or execution-trace pretraining~\cite{meta2025cwm}. All evaluation uses Python-only benchmarks; training data uses synthetic mutation operators~\cite{andrews2005mutation,just2014mutants} with untested transfer to real faults (Appendix~\ref{app:limitations}). Constrained decoding~\cite{poesia2022synchromesh,dong2024xgrammar,willard2023outlines} may mitigate \cwm{}'s format collapse but was not evaluated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5956fbf3-5b8b-4e63-8b30-82d2db879937",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "fd199199-0495-4f45-b324-7bbac415ca81",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented the first systematic comparison of three execution-free verification formulations (\\cls{}, \\cwm{}, \\traj{}) under ${\\leq}$8B LoRA fine-tuning. At function level, \\cls{} and \\cwm{} are statistically equivalent (TOST $p{=}0.007$, 5 seeds); \\traj{} equivalence is inconclusive after Holm correction. At repository level, divergence reaches 18--26\\pp{} via three failure modes; the formulation$\\times$complexity interaction is highly significant ($z{=}-23.7$, $p{<}0.001$), consistent across families. 14B results narrow function-level gaps to ${\\sim}$1\\pp{}; whether repo-level divergence is formulation-inherent or capacity-contingent remains open. Scaling to 32B+~\\cite{meta2025cwm} and complexity-aware routing are key open questions.\n\n\\section*{Limitations}\n\nPrimary findings use ${\\leq}$8B LoRA fine-tuning with multi-seed replication; 14B results use a single model family with 3 seeds; cross-family replication at 32B+ is needed. The repo-level gap may diminish with scale or execution-trace pretraining~\\cite{meta2025cwm}. All evaluation uses Python-only benchmarks; training data uses synthetic mutation operators~\\cite{andrews2005mutation,just2014mutants} with untested transfer to real faults (Appendix~\\ref{app:limitations}). Constrained decoding~\\cite{poesia2022synchromesh,dong2024xgrammar,willard2023outlines} may mitigate \\cwm{}'s format collapse but was not evaluated.",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  },
  "sourceToolAssistantUUID": "7e24216a-444e-40a3-bac0-8cd7e47f5602",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-25T21:14:50.262Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CdT4G11PhgKt8kNknq3NnX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd777723-bf4a-4232-8290-f31e26319ba9",
  "isSidechain": false,
  "requestId": "req_011CbPyjJFbXiP572yeM8mVa",
  "type": "assistant",
  "uuid": "7e24216a-444e-40a3-bac0-8cd7e47f5602",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaM23BQDFXe5A2ztbfTa1m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2976,
      "cache_read_input_tokens": 35139,
      "output_tokens": 742,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2976,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 742,
          "cache_read_input_tokens": 35139,
          "cache_creation_input_tokens": 2976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2976
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

_source line 36 · 2026-05-25T21:14:50.267Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TUedrLfZmpu5Y4RyJEeshA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e24216a-444e-40a3-bac0-8cd7e47f5602",
  "isSidechain": false,
  "requestId": "req_011CbPyjJFbXiP572yeM8mVa",
  "type": "assistant",
  "uuid": "771bad3f-f358-4157-b30e-b4eb7b70497e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaM23BQDFXe5A2ztbfTa1m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2976,
      "cache_read_input_tokens": 35139,
      "output_tokens": 742,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2976,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 742,
          "cache_read_input_tokens": 35139,
          "cache_creation_input_tokens": 2976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2976
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

_source line 37 · 2026-05-25T21:14:50.270Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UUVqDhgdntGYcseW6Fz5bE`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "771bad3f-f358-4157-b30e-b4eb7b70497e",
  "isSidechain": false,
  "requestId": "req_011CbPyjJFbXiP572yeM8mVa",
  "type": "assistant",
  "uuid": "e4d85d50-898b-4256-a14a-b3e3d1a6f8d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaM23BQDFXe5A2ztbfTa1m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2976,
      "cache_read_input_tokens": 35139,
      "output_tokens": 742,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2976,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 742,
          "cache_read_input_tokens": 35139,
          "cache_creation_input_tokens": 2976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2976
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

_source line 38 · 2026-05-25T21:14:50.276Z_

<details><summary>↩ Tool result · `toolu_01UUVqDhgdntGYcseW6Fz5bE`</summary>

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
  "parentUuid": "e4d85d50-898b-4256-a14a-b3e3d1a6f8d5",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "378dc1d0-8ddf-4002-b6f1-dcd3cb705fa0",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 29
  },
  "sourceToolAssistantUUID": "e4d85d50-898b-4256-a14a-b3e3d1a6f8d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: exec-sim-repair-verifier - 论文路径: projects/exec-sim-repair-verifier/docs/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: ARR (Main/Findings unified) - 截止日期: 2026-05-25 -…",
  "leafUuid": "fd199199-0495-4f45-b324-7bbac415ca81",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper submission for EMNLP 2026",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e"
}
```

---

### Tool result

_source line 41 · 2026-05-25T21:14:50.609Z_

<details><summary>↩ Tool result · `toolu_01TUedrLfZmpu5Y4RyJEeshA`</summary>

```text
1	\appendix
2	
3	\noindent\textbf{Appendix overview.} A: Oracle analysis. B: Ablations. C: Per-mutation breakdown. D: Variant-level accuracy. E: Hyperparameters. F: Prompt templates. G: Mutation distribution. H: Qualitative errors. I: Extended analysis (I.a--I.k). J: TOST sensitivity (J.1: Bayesian ROPE). K: Effect sizes. L: Holm-Bonferroni. M: Mixed-effects regression. N: Parseable bias. O: Threats (O.1: CWM convergence; O.2: Extended validity). P: AI assistants.
4	
5	\section{Oracle Accuracy-Utility Analysis}
6	\label{app:oracle}
7	
8	We stratify SWE-bench Verified instances by Fail-to-Pass (F2P) test count $T$, comparing per-test vs.\ trajectory-level oracle resolve rates under i.i.d.\ and block-correlated error models (ICC $= 0.191$, from function-level analysis; \S\ref{sec:equivalence}).
9	
10	\begin{table}[h]
11	\centering
12	\small
13	\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses function-level ICC $= 0.191$ (from function-level analysis, \S\ref{sec:equivalence}). Pass-to-Pass (P2P) regression rate: 1.04\% mean, 0\% median.}
14	\label{tab:oracle}
15	\resizebox{\columnwidth}{!}{%
16	\setlength{\tabcolsep}{3pt}
17	\begin{tabular}{lcccc}
18	\toprule
19	\textbf{$T$} & \textbf{Inst.\%} & \textbf{i.i.d.\ (\pp{})} & \textbf{Block (\pp{})} & \textbf{Contrib.\%} \\
20	\midrule
21	$1$ & 68.7 & $-$0.04 & $-$0.09 & $\approx$0 \\
22	$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\
23	$3$--$5$ & 7.1 & 25.00 & 40.74 & $\approx$26 \\
24	$\geq 6$ & 5.1 & 30.00 & 40.06 & $\approx$19 \\
25	\midrule
26	\textbf{All} & 100.0 & --- & \textbf{10.93} & 100.0 \\
27	\bottomrule
28	\end{tabular}}
29	\end{table}
30	
31	Figure~\ref{fig:oracle_stratified} (main text) shows the oracle per-test advantage by F2P test count.
32	
33	Table~\ref{tab:oracle} and Figure~\ref{fig:oracle_stratified} reveal a sharp concentration: at $T = 1$ (68.7\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T = 2$ (19.1\%), where block-correlated advantage reaches 31.69\pp{} (55.3\% of total). The overall block-correlated advantage is 10.93\pp{}, driven by the $T \geq 2$ minority. Block correlation amplifies relative to i.i.d.: at $T = 2$, 31.69\pp{} vs.\ 18.49\pp{} (1.7$\times$). P2P regression is negligible (1.04\% mean, 0\% median); the practical value concentrates in F2P discrimination.
34	
35	\paragraph{Sensitivity to ICC estimate.}
36	The analysis above uses ICC $= 0.191$ from function-level analysis (\S\ref{sec:equivalence}), where mean cluster size $\bar{k} \approx 16.5$ yields DEFF $= 3.97$. At repository level, within-problem correlation is substantially stronger: ICC $= 0.3146$ with DEFF $= 114.4$ (\S\ref{sec:repo}), yielding an effective sample size of $n_{\text{eff}} \approx 9{,}784 / 114.4 \approx 86$ independent observations~\cite{moulton1990}, still sufficient for regression but limiting precision of variance component estimates. This is a consequence of the larger and more heterogeneous test suites in SWE-bench Verified problems. Under higher ICC, within-problem errors cluster more tightly and amplify the block-correlated per-test advantage at each $T$ stratum; the correction from i.i.d.\ to block-correlated grows monotonically with ICC. The function-level ICC $= 0.191$ used in Table~\ref{tab:oracle} thus provides a conservative lower bound on the per-test advantage. The repo-level correlation structure would yield an even larger gap between per-test and trajectory-level oracle resolve rates, which strengthens the case for per-test granularity at repository-level complexity.
37	
38	\section{Ablation Studies}
39	\label{app:ablations}
40	
41	\paragraph{LoRA rank sensitivity.}
42	All \cwm{} experiments use LoRA rank $r{=}16$. To test whether this capacity constraint handicaps \cwm{}, we train rank-32 variants (seed 42), doubling adapter parameters.
43	
44	\begin{table}[h]
45	\centering
46	\small
47	\caption{LoRA rank ablation for \cwm{} 4B (seed 42, 3 epochs, lr $= 2{\times}10^{-4}$). Rank-16 seed variance: 0.53\pp{} (seeds 42 vs.\ 456).}
48	\label{tab:rank_ablation}
49	\setlength{\tabcolsep}{4pt}
50	\begin{tabular}{lccccc}
51	\toprule
52	\textbf{Config} & \textbf{$\alpha/r$} & \textbf{Acc (\%)} & \textbf{Fail \fone{}} & \textbf{Pass \fone{}} & \textbf{$\Delta$} \\
53	\midrule
54	$r{=}16$, $\alpha{=}32$ & 2 & \textbf{87.51} & --- & --- & --- \\
55	$r{=}32$, $\alpha{=}32$ & 1 & 87.00 & 87.1 & 86.9 & $-$0.51 \\
56	$r{=}32$, $\alpha{=}64$ & 2 & 87.04 & 87.27 & 86.79 & $-$0.47 \\
57	\bottomrule
58	\end{tabular}
59	\end{table}
60	
61	Both rank-32 variants fall within the 2-seed variance of the rank-16 baseline (0.53\pp{} between seeds 42 and 456; Table~\ref{tab:rank_ablation}). The $\alpha{=}64$ variant (matching the baseline $\alpha/r{=}2$ ratio) rules out the confound that the $\alpha{=}32$ result might reflect reduced effective scaling rather than rank insensitivity. This is consistent with \cwm{}'s function-level performance being bounded by output-format constraints rather than adapter capacity.
62	
63	\paragraph{Majority voting.}
64	Majority voting ($K{=}3$) decreases accuracy from 87.51\% to 86.83\% ($-$0.68\pp{}): errors are systematic rather than stochastic, so sampling-based ensembles do not help.
65	
66	\paragraph{Sequence-length ablation details.}
67	Both formulations are trained with \texttt{max\_seq\_length}$=$2,048. At inference, \cwm{} reserves \texttt{max\_new\_tokens}$=$512, leaving ${\sim}$1,536 effective input tokens; \cls{} allocates nearly all context to input (5,120--8,192 tokens). A matched-context ablation (\cls{} 8B at 2,048 tokens) achieves 83.04\%, only 1.44\pp{} below the 8,192-token evaluation (84.48\%), though truncation introduces 136 unparseable outputs (1.39\% of test samples). The matched-context gap (\cls{}@2,048 vs.\ \cwm{}@2,048) is 25.00\pp{} (98\% of the full 25.59\pp{} gap), confirming that input context disparity explains at most 3\% of the difference.
68	
69	\paragraph{Training data size control.}
70	\label{app:downsample}
71	To control for the training set size asymmetry between \cls{} (${\sim}$70K instances) and \traj{} (386 variant-level instances, ${\sim}$8K per-test equivalents, at repo level), we downsample \cls{} training data to match \traj{} in data volume. Downsampled \cls{} (Qwen3-4B, seed 42) achieves 80.74\% repo-level per-test accuracy, only 2.89\pp{} below the full-data \cls{} (83.63\%) and still 7.82\pp{} above \traj{} (72.92\%). The \cls{} formulation advantage is not attributable to training data volume.
72	
73	At function level, the relationship reverses: \traj{} uses 8,052 variant-level instances (2.24$\times$ more unique variants than \cls{}/\cwm{}'s 3,596 from 15,290 per-test instances). \cls{} nonetheless outperforms \traj{} by 2.13\pp{} (88.43\% vs.\ 86.30\%, Qwen3-4B), ruling out data volume as the explanation. An extreme downsample ablation (CLS trained on 447 per-test instances, ${\sim}$105 unique variants) achieves 78.57 $\pm$ 0.78\%, confirming that per-test classification maintains reasonable performance under severe data reduction, though it falls below \traj{} (86.30\%) given the 20$\times$ data disadvantage.
74	
75	\paragraph{Few-shot prompting baselines.}
76	\label{app:few_shot}
77	We evaluate 3-shot in-context learning at repo level to test whether prompting strategy closes the gap to fine-tuned models. Table~\ref{tab:few_shot} reports both per-test and variant-level accuracy.
78	
79	\begin{table}[h]
80	\centering
81	\small
82	\caption{Repo-level prompting baselines (per-test $n{=}9{,}784$; variant-level $n{=}48$). Majority baseline: 72.96\% per-test, 54.17\% variant-level.}
83	\label{tab:few_shot}
84	\setlength{\tabcolsep}{4pt}
85	\resizebox{\columnwidth}{!}{%
86	\begin{tabular}{lcccc}
87	\toprule
88	\textbf{Model} & \textbf{0-shot (per-test)} & \textbf{3-shot (per-test)} & \textbf{3-shot (variant)} \\
89	\midrule
90	Qwen3-8B & 49.90\% & 71.61\% & 45.83\%\textsuperscript{$\ast$} \\
91	DeepSeek-6.7B & 48.54\% & 46.28\% & 45.83\%\textsuperscript{$\ast$} \\
92	\bottomrule
93	\end{tabular}}
94	
95	\vspace{2pt}
96	{\footnotesize \textsuperscript{$\ast$}Both models achieve 45.83\% by correctly classifying all 22 unresolved variants and zero resolved variants (22/48 = 45.83\%), equivalent to an always-predict-unresolved baseline. The 100\% overlap in variant-level predictions confirms complete degradation at task-relevant granularity.}
97	\end{table}
98	
99	Both models converge to exactly 45.83\% variant-level accuracy under 3-shot prompting, below majority baseline (54.17\%). Variant-level analysis reveals this is not a coincidence: both models correctly classify all 22 unresolved variants and zero resolved variants, equivalent to an always-predict-unresolved baseline with 100\% prediction overlap. Per-test accuracy diverges sharply (Qwen3-8B 71.61\% vs.\ DeepSeek 46.28\%), but this divergence is entirely superficial: Qwen3-8B predicts pass on nearly all tests, inflating per-test accuracy on a pass-heavy dataset (72.96\% pass rate) without genuine discriminative ability. Per-test metrics can thus severely misrepresent baseline capability; variant-level evaluation is necessary to detect complete degradation. Neither 0-shot nor few-shot prompting approaches fine-tuned performance (82--84\% per-test); fine-tuning is a necessary condition for repo-level verification.
100	
101	\section{Repo-Level Per-Mutation Breakdown}
102	\label{app:repo_mutation}
103	
104	Table~\ref{tab:mutation_breakdown} compares per-mutation accuracy at repo level. \cls{} produces 0\% unparseable outputs; all values are direct classification accuracy. \cwm{} overall accuracy includes default-pass assignment for unparseable outputs (see \S\ref{sec:repo}).
105	
106	\begin{table}[h]
107	\centering
108	\small
109	\caption{Per-mutation test accuracy (\%) at repo level (SWE-bench Verified, $n{=}9{,}784$). \cls{} 8B reports two seeds; $\Delta$ is mean 4B$\to$8B gain for \cls{}. \cwm{} 4B per-mutation overall accuracy omitted for non-gold mutations due to low parse rates (4.4--56.9\%, Table~\ref{tab:cwm_mutation_parse}); gold overall accuracy derived from parse rate 43.5\% and parseable accuracy 23.5\%.}
110	\label{tab:mutation_breakdown}
111	\resizebox{\columnwidth}{!}{%
112	\setlength{\tabcolsep}{3pt}
113	\begin{tabular}{lccccccc}
114	\toprule
115	\textbf{Mutation} & \textbf{$n$} & \textbf{CLS 4B} & \textbf{CLS 8B s42} & \textbf{CLS 8B s123} & \textbf{CWM 4B} & \textbf{CWM 8B} & \textbf{$\Delta$ CLS} \\
116	\midrule
117	gold & 4,633 & 98.25 & 96.24 & 99.60 & 66.72 & 80.06 & $-$0.33 \\
118	operator\_swap & 3,357 & 78.91 & 81.38 & 82.60 & --- & 54.57 & +3.08 \\
119	off\_by\_one & 183 & 58.47 & 86.89 & 79.20 & --- & 63.39 & \textbf{+24.58} \\
120	return\_value & 562 & 67.97 & 75.44 & 66.40 & --- & 49.11 & +2.95 \\
121	boundary\_removal & 1,049 & 46.90 & 46.90 & 44.90 & --- & 42.23 & $-$1.00 \\
122	\bottomrule
123	\end{tabular}}
124	\end{table}
125	
126	Figure~\ref{fig:mutation_heatmap} visualises the per-mutation accuracy contrast between \cls{} and \cwm{} at repo level.
127	
128	\begin{figure}[h]
129	\centering
130	\includegraphics[width=\columnwidth]{figures/paper/fig_mutation_heatmap.pdf}
131	\caption{Per-mutation repo-level accuracy heatmap. \cls{} 8B values are seed-averaged (s42/s123). \cwm{} 8B includes default-pass for unparseable outputs. \texttt{boundary\_removal} is a scale-invariant difficulty ceiling (${\sim}$45\%) for both formulations.}
132	\label{fig:mutation_heatmap}
133	\end{figure}
134	
135	Table~\ref{tab:cwm_mutation_parse} shows that \cwm{} generation quality degrades from 4B to 8B across all mutation types.
136	
137	\begin{table}[h]
138	\centering
139	\small
140	\caption{\cwm{} parse rates and parseable-only accuracy per mutation type (seed 42). Parse rate decreases uniformly from 4B to 8B; parseable-only accuracy is below random binary chance (50\%) for gold at both scales.}
141	\label{tab:cwm_mutation_parse}
142	\setlength{\tabcolsep}{4pt}
143	\begin{tabular}{lcccc}
144	\toprule
145	& \multicolumn{2}{c}{\textbf{Parse Rate (\%)}} & \multicolumn{2}{c}{\textbf{Parse Acc (\%)}} \\
146	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
147	\textbf{Mutation} & \textbf{4B} & \textbf{8B} & \textbf{4B} & \textbf{8B} \\
148	\midrule
149	gold & 43.5 & 23.9 & 23.5 & 16.5 \\
150	operator\_swap & 56.9 & 21.2 & 63.1 & 58.8 \\
151	off\_by\_one & 4.4 & 27.3 & 0.0 & 38.0 \\
152	return\_value & 48.8 & 26.9 & 27.0 & 56.9 \\
153	boundary\_removal & 30.6 & 51.8 & 59.2 & 51.8 \\
154	\bottomrule
155	\end{tabular}
156	\end{table}
157	
158	Key findings: (1)~Gold parse rate collapses from 43.5\% to 23.9\% at 8B; the simplest generation target (unmodified code, where all tests pass) degrades most, consistent with a fundamental generation bottleneck rather than task difficulty. (2)~Among parseable outputs, gold accuracy is 16.5--23.5\%: the model generates outputs that fail exact-match even for correct code. (3)~\texttt{off\_by\_one} is an anomaly: parse rate \emph{increases} from 4.4\% to 27.3\%, but this is from an extremely low base ($n{=}8$ parseable at 4B), making both directions unreliable for this category.
159	
160	\section{Variant-Level Accuracy}
161	\label{app:variant_level}
162	
163	Table~\ref{tab:variant_level} reports variant-level accuracy ($n{=}48$) alongside per-test accuracy for all repo-level configurations. For \cls{}, the aggregation penalty (per-test $\to$ variant-level drop) ranges from 1\pp{} to 19\pp{} and is largest for models with low fail recall under the all-pass rule. \cwm{} variant-level accuracy (48--52\%) falls at or below the majority baseline, consistent with format collapse as the dominant failure mode.
164	
165	\begin{table}[h]
166	\centering
167	\small
168	\caption{Repo-level per-test vs.\ variant-level accuracy ($n{=}48$ variants). Penalty = per-test $-$ variant-level. \traj{} predicts variant outcomes directly (no aggregation). Variant-level majority baseline: 54.17\% (26/48).}
169	\label{tab:variant_level}
170	\setlength{\tabcolsep}{3pt}
171	\resizebox{\columnwidth}{!}{%
172	\begin{tabular}{llcccc}
173	\toprule
174	\textbf{Model} & \textbf{Seed} & \textbf{Per-test (\%)} & \textbf{Variant (\%)} & \textbf{Penalty (\pp{})} & \textbf{Fail Recall (\%)} \\
175	\midrule
176	\multicolumn{6}{l}{\emph{\cls{}}} \\
177	Qwen3-8B & s42 & 84.48 & 72.92 & 11.56 & 56.76 \\
178	Qwen3-8B & s123 & 85.60 & 81.25 & 4.35 & 51.44 \\
179	Qwen3-4B & s42 & 83.63 & 64.58 & 19.05 & 48.72 \\
180	DeepSeek-6.7B & s42 (e1) & 82.61 & 81.25 & 1.36 & 51.02 \\
181	DeepSeek-6.7B & s42 (e3) & 82.51 & 79.17 & 3.34 & 38.47 \\
182	DeepSeek-6.7B & s123 & 74.93 & 56.25 & 18.68 & ${\sim}$13.72 \\
183	\midrule
184	\multicolumn{6}{l}{\emph{\cwm{}}} \\
185	Qwen3-8B & s42 & 65.17 & 52.08 & 13.09 & --- \\
186	DeepSeek-6.7B$^\dagger$ & s123 & --- & 47.92 & --- & --- \\
187	\midrule
188	\multicolumn{6}{l}{\emph{\traj{}}} \\
189	Qwen3-4B & s42 & --- & 72.92 & --- & --- \\
190	Qwen3-8B & s42 & --- & 70.83 & --- & --- \\
191	DeepSeek-6.7B & 3-seed & --- & 77.08 $\pm$ 3.61 & --- & --- \\
192	\midrule
193	Majority & --- & 72.96 & 54.17 & --- & --- \\
194	\bottomrule
195	\end{tabular}}
196	\vspace{2pt}
197	
198	{\footnotesize $^\dagger$Evaluated on ${\sim}$75\% of test instances (7210--7668 of 9784). DeepSeek \traj{} Table~\ref{tab:repo_level} reports 3 seeds (42/123/456) for alignment with \cls{}/\cwm{} seed coverage; three supplementary seeds (0/789/999) yield 75.0\%, 66.7\%, 79.2\% respectively (6-seed mean 75.35 $\pm$ 5.00\%), consistent in direction.}
199	\end{table}
200	
201	\section{Training Hyperparameters}
202	\label{app:hyperparams}
203	
204	Table~\ref{tab:hyperparams} lists all hyperparameters used for fine-tuning. Both \cls{} and \cwm{} share the same LoRA configuration, optimizer, and training schedule; the only differences are per-device batch size, gradient accumulation steps (adjusted to maintain identical effective batch size of 32 across model sizes), and learning rate (DeepSeek-Coder uses $2{\times}10^{-4}$ vs.\ $5{\times}10^{-5}$ for Qwen3, selected via grid search over $\{5{\times}10^{-5}, 1{\times}10^{-4}, 2{\times}10^{-4}\}$ on held-out validation loss).
205	
206	\begin{table}[h]
207	\centering
208	\small
209	\caption{Training hyperparameters for \cls{}/\cwm{} configurations. \traj{} models use lr $= 2{\times}10^{-4}$ due to the smaller training set (${\sim}$8K function-level instances vs.\ ${\sim}$70K for \cls{}/\cwm{}); other hyperparameters are shared.}
210	\label{tab:hyperparams}
211	\resizebox{\columnwidth}{!}{%
212	\begin{tabular}{ll}
213	\toprule
214	\multicolumn{2}{l}{\textbf{Shared across all configurations}} \\
215	\midrule
216	LoRA rank / alpha / dropout & 16 / 32 / 0.05 \\
217	LoRA targets & \texttt{q/k/v/o\_proj} \\
218	Optimizer & AdamW ($\beta_1{=}0.9$, $\beta_2{=}0.999$) \\
219	LR scheduler & Linear \\
220	Effective batch size & 32 \\
221	Max sequence length & 2,048 \\
222	Epochs & 3 \\
223	Precision & bf16 \\
224	Gradient checkpointing & \checkmark \\
225	Seeds (function) & \{42, 123, 456, 789, 0\}\textsuperscript{$b$} \\
226	Seeds (repo) & \{42, 123, 456\}\textsuperscript{$c$} \\
227	\bottomrule
228	\end{tabular}}
229	
230	\vspace{6pt}
231	
232	\resizebox{\columnwidth}{!}{%
233	\begin{tabular}{lccc}
234	\toprule
235	\multicolumn{4}{l}{\textbf{Model-family--specific parameters}} \\
236	\midrule
237	& \textbf{Qwen3-4B} & \textbf{Qwen3-8B} & \textbf{DS-6.7B} \\
238	\midrule
239	Learning rate & 5e-5 & 5e-5 & 2e-4 \\
240	Weight decay & 0.01 & 0.01 & 0.0 \\
241	Warmup ratio & 0.05 & 0.05 & 0.1 \\
242	Batch / grad.\ accum.\ (\cls{}) & 2 / 16 & 1 / 32 & 2 / 16 \\
243	Batch / grad.\ accum.\ (\cwm{}) & 1 / 32 & 1 / 32 & 1 / 32 \\
244	Training samples & 70,748 & 70,748 & 67,343--70,748\textsuperscript{$a$} \\
245	\bottomrule
246	\end{tabular}}
247	
248	\vspace{2pt}
249	{\footnotesize $^a$DeepSeek \cls{} canonical run (s42) uses drop preprocessing, which excludes 3,405 sequences exceeding max length (67,343 of 70,748). The s123 run uses truncate preprocessing (70,748 samples) but produces NaN validation loss. See \S\ref{sec:setup}. $^b$Seeds 789 and 0 use NF4 quantization; others use bf16. $^c$Repo-level seed coverage varies by configuration; see Table~\ref{tab:repo_level} caption for per-model counts.}
250	\end{table}
251	
252	\paragraph{Data processing.} DeepSeek CWM seeds use \texttt{train\_unified.py}, which drops samples exceeding \texttt{max\_seq\_length} (3{,}405 of 70{,}748 samples, 4.8\%). Qwen CWM seeds use \texttt{train\_repo\_cwm.py}, which truncates and retains all samples. This difference affects total training steps (${\sim}$12{,}627 vs.\ ${\sim}$13{,}266 for DeepSeek, ${\sim}$6{,}633 for Qwen) but not the training data distribution, as dropped samples are uniformly distributed across labels.
253	
254	\paragraph{Prompt templates.} Prompt templates for all formulations (\cls{}, \cwm{}, \traj{}) are provided in the code repository. \cls{} uses a binary classification template (``Does this test pass or fail?''); \cwm{} uses an execution simulation template (``What is the output of this test?''); \traj{} uses a variant-level verdict template (``Is this patch resolved or unresolved?'').
255	
256	\paragraph{Mutation operators.} We use five mutation types: (1)~\emph{gold}: unmodified code (all tests pass); (2)~\emph{operator\_swap}: replaces comparison or arithmetic operators (e.g., \texttt{<} $\to$ \texttt{<=}); (3)~\emph{off\_by\_one}: shifts loop bounds or array indices by $\pm$1; (4)~\emph{return\_value}: modifies return statements (e.g., negating a boolean, changing a constant); (5)~\emph{boundary\_removal}: removes conditional guards or boundary checks. Mutation operators were applied using AST-level transformation; variants that did not alter any test outcome were discarded.
257	
258	\paragraph{Compute budget.}
259	All experiments were conducted on NVIDIA RTX 5090 GPUs. Training time is approximately 1.5 hours per run for 4B models and 2 hours for 8B models. Total compute budget: ${\sim}$370 GPU-hours across 223 completed runs (135 successful, 88 failed/killed; ${\sim}$46 unique configurations including seeds, formulations, model sizes, and ablations).
260	
261	\section{Prompt Templates}
262	\label{app:prompts}
263	
264	We show representative prompt examples for each formulation. All examples use the same input instance for comparability.
265	
266	\paragraph{CLS (per-test classification).}
267	{\footnotesize\begin{verbatim}
268	System: You are a code verifier.
269	Given a code patch and a test name,
270	predict whether the test will pass
271	or fail when run against the
272	patched code.
273	
274	User:
275	## Patch (git diff)
276	&lt;patch content> [... truncated]
277	## Test
278	test_boundary_check
279	Will this test pass or fail?
280	
281	Target: pass
282	\end{verbatim}}
283	
284	\paragraph{CWM (execution simulation).}
285	{\footnotesize\begin{verbatim}
286	System: You are a code execution
287	simulator. Given a code snippet and
288	a test case, predict the execution
289	result.
290	
291	User:
292	## Code
293	&lt;code content> [... truncated]
294	## Test
295	test_boundary_check
296	What is the execution result?
297	
298	Target: PASS: test completed
299	successfully
300	\end{verbatim}}
301	
302	\paragraph{TRAJ (trajectory scoring).}
303	{\footnotesize\begin{verbatim}
304	System: You are a code repair
305	verifier. Given the code patch and
306	test summary, predict whether all
307	tests pass (resolved) or any test
308	fails (unresolved).
309	
310	User:
311	[Code]
312	&lt;patch content> [... truncated]
313	[Test Summary]
314	&lt;all test names and descriptions>
315	
316	Target: resolved
317	\end{verbatim}}
318	
319	\cls{} and \cwm{} share the same input format (one code--test pair per instance); \cls{} produces a single token (\texttt{pass}/\texttt{fail}), while \cwm{} generates a variable-length execution trace. \traj{} receives all tests concatenated and produces a single token (\texttt{resolved}/\texttt{unresolved}).
320	
321	
322	\section{Val-Test Mutation Type Distribution}
323	\label{app:mutation_distribution}
324	
325	Table~\ref{tab:mutation_distribution} reports the mutation type composition of the repo-level validation and test sets. The most notable shift is \texttt{operator\_swap}, which nearly doubles from val (19.1\%) to test (34.3\%), while \texttt{off\_by\_one} shrinks from 10.0\% to 1.9\%.
326	
327	\begin{table}[h]
328	\centering
329	\small
330	\caption{Repo-level mutation type distribution: validation vs.\ test set, with per-type \cls{} accuracy at two model sizes (seed 42). Shift = test\% $-$ val\%.}
331	\label{tab:mutation_distribution}
332	\setlength{\tabcolsep}{3pt}
333	\resizebox{\columnwidth}{!}{%
334	\begin{tabular}{lccccc}
335	\toprule
336	\textbf{Mutation Type} & \textbf{Val (\%)} & \textbf{Test (\%)} & \textbf{Shift} & \textbf{\cls{} 4B} & \textbf{\cls{} 8B} \\
337	\midrule
338	gold & 45.2 & 47.4 & +2.2 & 98.3 & 96.2 \\
339	operator\_swap & 19.1 & 34.3 & +15.2 & 78.9 & 81.4 \\
340	boundary\_removal & 15.0 & 10.7 & $-$4.3 & 46.9 & 46.9 \\
341	return\_value & 10.7 & 5.7 & $-$5.0 & 68.0 & 75.4 \\
342	off\_by\_one & 10.0 & 1.9 & $-$8.1 & 58.5 & 86.9 \\
343	\bottomrule
344	\end{tabular}}
345	\end{table}
346	
347	The \texttt{operator\_swap} shift is the primary source of val-test distribution mismatch. Since \cls{} achieves moderate accuracy on this type (78.9--81.4\%), the over-representation in the test set does not systematically bias overall accuracy estimates in either direction. Two boundary observations are notable: (1)~\texttt{boundary\_removal} represents a scale-invariant difficulty ceiling at ${\sim}$47\% across both model sizes: this mutation type resists capacity scaling; (2)~\texttt{off\_by\_one} shows the largest scaling gain (+28.4\pp{}, 58.5\%$\to$86.9\%) but its small test share (1.9\%) limits its contribution to overall accuracy differences across scales.
348	
349	\section{Qualitative Error Analysis}
350	\label{app:qualitative}
351	
352	To complement the quantitative divergence reported in \S\ref{sec:repo}, we examine representative errors from each formulation at repository level.
353	
354	\paragraph{\cwm{} failure modes.}
355	Two patterns account for the majority of unparseable \cwm{} outputs on Qwen3. (1)~\emph{Task misunderstanding}: the model generates a complete simulated test runner log (test names, timing, summary lines) rather than a pass/fail verdict. For instance, on \texttt{django\_\_django-14315}, the model outputs a fabricated 1,248-token Django test execution trace with hallucinated test names that do not exist in the target file. The model confuses ``predict test outcome'' with ``simulate test execution environment.'' (2)~\emph{Autoregressive degeneration}: the model enters a repetitive loop (e.g., repeating \texttt{from \_pytest.config import \_parse\_pytest\_args} until truncation at 4,542 tokens). Both patterns produce zero usable signal and default to the majority-class label. This explains why unparseable predictions carry higher accuracy than parseable ones (\S\ref{sec:repo}).
356	
357	\paragraph{\cls{} failure modes.}
358	\cls{} errors concentrate in two categories requiring multi-step reasoning. False positives arise from \emph{cross-concern value propagation}: a boundary removal mutation in \texttt{pytest} converts a guarded attribute access (\texttt{if xfailed and not xfailed.run}) to \texttt{if True:}, causing a NoneType error on tests exercising unrelated skip marks. The model fails to trace the None path through the pytest hook lifecycle. False negatives arise from \emph{mathematical equivalence}: on \texttt{HumanEval/130} (Tribonacci variant), the model predicts failure for correct code because verifying the self-referential recurrence requires algebraic substitution rather than syntactic inspection. This single problem accounts for 17\% of all function-level false negatives.
359	
360	\paragraph{Complementarity.}
361	These failure patterns operate at different levels: \cwm{} fails at the format level (producing no usable signal), while \cls{} fails at the reasoning level (producing a confident but incorrect binary verdict). Both formulations are FP-dominant (over-predict failure), but \cwm{}'s higher FP rate (70.3\% vs.\ 56.5\%) means it over-predicts failure on instances \cls{} correctly classifies, producing partial complementarity (oracle combination: 90.63\%; \S\ref{app:extended_analysis}, paragraph a).
362	
363	\section{Extended Analysis}
364	\label{app:extended_analysis}
365	
366	\paragraph{Function-level CWM metric robustness.}
367	At function level, \cwm{} outputs are short status strings (mean ${\sim}$5--15 tokens). The unparseable rate is only 1.39\%, and default-to-pass bias is $<$1\pp{}, well below the SESOI threshold. Exact string matching is appropriate for these short, structured outputs; semantic-but-format-different matches are rare given the constrained output space.
368	
369	\paragraph{(a) Error complementarity.}
370	\cls{} and \cwm{} are both FP-dominant at function level but at different rates, producing partial complementarity. Among \cls{} errors (seed 42), 56.5\% are false positives (PASS $\to$ FAIL); among \cwm{} errors, 70.3\% are false positives. Both formulations over-predict failure, but \cwm{}'s stronger FP bias means it incorrectly rejects passing tests that \cls{} correctly accepts. An oracle combination achieves 90.63\% accuracy (1713/1890 correct, 177 both-wrong; +2.80\pp{} over the best single formulation, \cls{} 87.83\%; single-seed estimate, seed 42). The complementarity arises from different \emph{degrees} of fail-bias rather than opposite error directions: \cwm{}'s generation bottleneck produces aggressive failure predictions, while \cls{}'s single-token output is more calibrated. Ensemble approaches exploiting this degree difference are a natural direction.
371	
372	\paragraph{(b) CWM error mode breakdown.}
373	Among unparseable \cwm{} outputs (Qwen3, repo-level), 76.9\% contain no execution keywords; 22.9\% contain ambiguous co-occurring pass/fail keywords. Format compliance varies sharply across repositories (scikit-learn: near-zero unparseable; sphinx: 100\%); repository-specific code patterns interact with the model's generation capabilities in complex ways. This per-repository variation is consistent with a model/tokenizer-specific failure rather than a formulation-level one.
374	
375	\paragraph{(c) Relaxed matching does not rescue \cwm{}.}
376	Relaxed matching (tolerating format deviations, L0--L4) \emph{decreases} \cwm{} accuracy: 58.04\%$\to$56.98\% (seed 42) and 59.09\%$\to$55.91\% (seed 123). Unparseable predictions default to the majority class (pass, 72.96\%), which outperforms the model's own parseable predictions (38--43\%). The divergence widens from 26\pp{} to 27\pp{} under relaxed matching. This rules out the hypothesis that parsing strictness inflates the observed gap. Constrained decoding~\cite{willard2023outlines} could enforce format compliance but would not address the semantic accuracy deficit among parseable outputs. An accidental training artifact provides further evidence: a \cwm{} model inadvertently trained on function-level (\cls{}-format) data achieved 86.05\% accuracy with 0\% unparseable outputs at repo level, recovering \cls{}-level performance. This confirms that the repo-level \cwm{} degradation stems entirely from trace generation complexity, not from the underlying verification task.
377	
378	\paragraph{(d) Variance compression.}
379	\cwm{}'s 5-seed standard deviation (0.37\pp{}) is lower than \cls{} (0.78\pp{}) and \traj{} (0.97\pp{}) at function level. If \cwm{} performance is capped by output-format constraints at a given complexity level, seed-to-seed variability is compressed relative to formulations whose performance depends more on learned representations.
380	
381	\paragraph{(e) Per-test precision and recall.}
382	\cls{} achieves fail \fone{} 87.59\% (precision 86.20\%, recall 89.04\%) at seed 42.% derived from overlap analysis (error_overlap_matched_seed.json); FP=130, FN=100, TP=848, TN=812
383	Multi-F2P instances (6--10 tests) reach 96.3\% accuracy, consistent with the oracle finding that per-test granularity is most valuable for complex instances.
384	
385	\paragraph{(f) Block correlation.}
386	Within-problem errors are correlated (ICC $= 0.191$, DEFF $= 3.97$, 2.81$\times$ more all-correct problems than i.i.d.\ expectation). All statistical tests use clustered bootstrap accordingly.
387	
388	\paragraph{(g) Failed interventions.}
389	We systematically tested four interventions targeting different hypothesized causes of \cwm{} repo-level degradation; all failed:
390	
391	\begin{itemize}[leftmargin=*,itemsep=1pt,topsep=2pt]
392	\item \textbf{Capacity (rank 32, $\alpha{=}64$):} $-$0.47\pp{}, within seed variance (\S\ref{app:ablations}).
393	\item \textbf{Majority voting ($K{=}3$):} $-$0.68\pp{}; 93.3\% unanimous, net flips negative (\S\ref{app:ablations}).
394	\item \textbf{Relaxed matching (L0--L4):} $-$1.06\pp{}; default-pass outperforms parseable predictions (paragraph~(c) above).
395	\item \textbf{Model scaling (4B$\to$8B):} parseable accuracy decreases (42.88\%$\to$38.52\%) while unparseable rate rises (53.7\%$\to$73.8\%); gain is a default-assignment artifact (\S\ref{sec:repo}).
396	\end{itemize}
397	
398	\noindent Each intervention targets a distinct alternative explanation (insufficient capacity, random noise, parsing strictness, model scale); the uniform failure across all four confirms the bottleneck is formulation-level: output space complexity at repo level exceeds what ${\leq}$8B generation models can handle, independent of these surface-level factors.
399	
400	\paragraph{(h) Per-mutation scaling patterns.}
401	Scaling benefits are highly non-uniform across mutation types (Table~\ref{tab:mutation_breakdown}). \texttt{off\_by\_one} shows the largest \cls{} scaling gain: 58.5\% (4B) to 86.9\% (8B, $+$28.4\pp{}). In contrast, \texttt{boundary\_removal} is scale-invariant at ${\sim}$47\% across both sizes, which marks an intrinsic difficulty ceiling. For \cwm{}, gold mutation parse rate collapses from 43.5\% (4B) to 23.9\% (8B) despite being the simplest target: generation capability degrades even for trivially correct code at larger scale within Qwen3. The val-test mutation type distribution differs notably (\texttt{operator\_swap} shifts from 19.1\% to 34.3\%; Table~\ref{tab:mutation_distribution}), but this shift does not systematically bias overall accuracy because \cls{} performance on \texttt{operator\_swap} (78.9--81.4\%) is close to the overall mean.
402	
403	\paragraph{(i) Inference efficiency.}
404	\cls{} achieves 217$\times$ higher throughput than \cwm{} at repo level (853 vs.\ 3.9 inferences/min; Qwen3-4B, RTX 5090, 100 samples, avg ${\sim}$1,040 input tokens). The speedup derives directly from the formulation: classification requires a single output token, whereas \cwm{} generates an average of 477 tokens per inference. Median latency is 48ms (\cls{}) vs.\ 16.3s (\cwm{}). At the observed unparseable rate of 73.8\% (8B), the majority of \cwm{}'s generation budget produces tokens that cannot yield a valid verdict. This \cls{}--\cwm{} efficiency gap is an inherent property of the formulation difference (1 vs.\ $O(L)$ output tokens) and should generalize across models, unlike the accuracy divergence which may be model-contingent.
405	
406	The \cls{}--\traj{} efficiency comparison is more nuanced, because \cls{} makes one call per test while \traj{} makes one call per instance. Per-call, \cls{} is 20--138$\times$ faster (depending on input length: 47ms for short contexts vs.\ 2,632ms for \traj{}). However, the per-instance effective speedup depends on test count $|T|$: at function level ($|T| \approx 2.3$), \cls{} is ${\sim}$24$\times$ faster (108ms vs.\ 2,632ms per instance); at repo level ($|T| \approx 12.3$, ${\sim}$70ms/call with longer inputs), \cls{} is ${\sim}$3$\times$ faster (861ms vs.\ 2,631ms). A crossover exists at $|T| \approx 50$ tests, beyond which \traj{}'s single-call amortization dominates. This boundary condition is informative for deployment: \cls{} is strongly preferred for function-level and moderate repo-level test suites, while extremely large test suites ($>$50 tests per instance) favor trajectory-level efficiency despite its coarser diagnostic signal.
407	
408	\paragraph{(j) Re-repair pilot.}
409	We tested whether per-test diagnostic feedback improves downstream repair. A Qwen3-8B repair agent received either per-test diagnostic signals (which specific tests failed and why) or binary accept/reject feedback, evaluated on 44 SWE-bench Verified instances. The diagnostic condition achieved accuracy no higher than the binary baseline ($A_1 = 52.3\%$, $p = 0.42$, effect size $\approx 0$). Per-test diagnostic information does not automatically translate to repair improvements at this scale. The negative result may reflect insufficient agent capability to exploit fine-grained feedback, insufficient sample size (at $n = 44$, statistical power is ${\sim}$0.3 for a medium effect size), or a genuine limitation of the diagnostic-to-repair translation.
410	
411	\paragraph{(k) Relationship to chain-of-thought verification.}
412	\cwm{} is structurally a chain-of-thought verifier: the model generates an execution trace token by token and derives its PASS/FAIL verdict from the final trace state. If intermediate reasoning improved verification, \cwm{} should outperform the reasoning-free \cls{} baseline. At function level, no such advantage materialises: \cwm{} and \cls{} are statistically equivalent (TOST $p{=}0.007$, $\pm$2\pp{} margin; \S\ref{sec:equivalence}), indicating that the additional trace generation provides no accuracy benefit over direct binary classification. At repo level, the chain-of-thought mechanism actively \emph{hurts}: trace generation triggers format collapse (53--74\% unparseable), and even parseable traces yield accuracy below the majority baseline (38--43\% vs.\ 72.96\%; paragraph~(c)). Four targeted interventions fail to rescue the generation pathway (paragraph~(g)). Within the ${\leq}$8B LoRA regime, chain-of-thought--style verification does not outperform direct classification for execution prediction. Whether execution-trace pretraining at larger scale~\cite{meta2025cwm} changes this conclusion remains the primary open question (\S\ref{sec:threats}).
413	
414	\section{TOST Margin Sensitivity}
415	\label{app:tost_sensitivity}
416	
417	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence $p$-value as a function of the equivalence margin, computed on the 5-seed variant-level \cls{}--\cwm{} comparison (gap $= 1.24$\pp{}, 523 variants, 114 clusters, clustered bootstrap).
418	
419	\begin{table}[h]
420	\centering
421	\small
422	\caption{TOST margin sensitivity for \cls{}--\cwm{} equivalence (seed-level paired, 5 seeds, df${=}$4). The smallest margin achieving equivalence at $\alpha = 0.05$ is $\pm$1.63\pp{}.}
423	\label{tab:tost_sensitivity}
424	\setlength{\tabcolsep}{4pt}
425	\begin{tabular}{ccc}
426	\toprule
427	\textbf{Margin ($\pm$\pp{})} & \textbf{$p$-value} & \textbf{Equivalent ($\alpha{=}0.05$)?} \\
428	\midrule
429	1.0 & 0.871 & No \\
430	1.5 & 0.113 & No \\
431	\textbf{1.63} & ${\sim}$\textbf{0.05} & \textbf{Smallest margin} \\
432	2.0 & 0.007 & Yes \\
433	3.0 & $3.2{\times}10^{-4}$ & Yes \\
434	5.0 & $1.6{\times}10^{-5}$ & Yes \\
435	\bottomrule
436	\end{tabular}
437	\end{table}
438	
439	Figure~\ref{fig:tost_sensitivity} (main text) visualises the margin--$p$-value relationship for both comparisons.
440	
441	The minimum equivalence margin is $\pm$1.63\pp{}, 0.37\pp{} below our pre-specified $\pm$2\pp{} threshold. The $\pm$2\pp{} threshold was set based on deployment relevance rather than observed data: at function-level accuracy (85--88\%), a 2\pp{} per-test difference corresponds to ${\sim}$38 additional errors across 1,890 tests (${\sim}$2--3 problems out of 114), comparable in magnitude to between-seed standard deviation (0.37--0.97\pp{}) and checkpoint selection noise ($<$1\pp{}). Differences within this range do not reliably distinguish formulations from training noise in pipeline selection decisions. For \cls{}--\traj{}, the TOST at $\pm$2\pp{} yields $p{=}0.025$, nominally significant but not surviving Holm-Bonferroni correction at $k{=}5$ (adjusted $p{=}0.075$; Table~\ref{tab:holm}). The one-sided decomposition reveals the binding constraint: $p_{\text{upper}}{=}0.005$ ($\Delta < {+}2$\pp{} is well-confirmed) while $p_{\text{lower}}{=}0.025$ ($\Delta > {-}2$\pp{}) limits the overall TOST, consistent with \cls{} having mildly higher accuracy.
442	
443	\paragraph{Robustness: seed-level vs.\ clustered bootstrap TOST.}
444	The primary TOST $p$-values use seed-level paired analysis (df${=}$4), treating each training seed as the unit of replication (\S\ref{sec:setup}). Under problem-level clustered bootstrap (resampling 114 problem clusters, 10K iterations), the \cls{}--\traj{} raw TOST $p$ decreases to ${\sim}$0.007 (Holm-adjusted $p{\approx}0.021$), which would confirm equivalence. We report the more conservative seed-level result ($p{=}0.025$, adjusted $p{=}0.075$) as primary, since training seeds are the true unit of replication; problem-level bootstrap pools within-seed observations and may understate between-seed uncertainty. For \cls{}--\cwm{}, both methods confirm equivalence ($p \leq 0.010$), so the choice does not affect conclusions.
445	
446	\subsection{Bayesian ROPE Analysis}
447	\label{app:bayesian_rope}
448	To complement the frequentist TOST, we conduct a Bayesian equivalence analysis using a paired $t$-test with Jeffreys prior~\cite{kruschke2013bayesian,kruschke2018rejecting}. The marginal posterior for the mean accuracy difference follows a $t$-distribution with $n{-}1$ degrees of freedom. For \cls{}--\cwm{}, the posterior probability within the $\pm$2\pp{} ROPE is $P(\text{ROPE}) = 0.975$, and the 95\% highest density interval (HDI $= [{+}0.10, {+}2.00]$\,pp) falls entirely inside the ROPE, confirming equivalence under both continuous and HDI-based decision criteria. For \cls{}--\traj{} at per-test level, $P(\text{ROPE}) = 0.542$ (inconclusive; 95\% HDI $= [{+}0.35, {+}3.52]$\,pp extends beyond the ROPE), consistent with the TOST inconclusive result after Holm correction ($p_{\text{adj}} = 0.075$). At variant level, \cls{}--\traj{} equivalence is supported by the Bayesian criterion ($P(\text{ROPE}) = 0.970$, HDI $= [{-}2.00, {+}1.03]$\,pp), but the frequentist TOST remains inconclusive after Holm-Bonferroni correction ($p_{\text{adj}} = 0.075$; Table~\ref{tab:holm}). This discrepancy reflects differing treatments of multiplicity: Bayesian ROPE evaluates each comparison independently, while Holm correction penalizes across all $k{=}5$ primary tests. For \cls{}--\cwm{}, both frameworks agree (TOST $p_{\text{adj}}{=}0.028$, $P(\text{ROPE}){=}0.975$); for \cls{}--\traj{} per-test, both are inconclusive. We conservatively follow the Holm-corrected TOST in the main text and report \cls{}--\traj{} equivalence as inconclusive.
449	
450	\paragraph{14B scaling evidence.} At 14B (3 seeds), the \cls{}--\cwm{} gap narrows to 0.43\pp{} and the \cls{}--\traj{} gap to 1.07\pp{}, both within the $\pm$2\pp{} margin. Seed-level TOST (df${=}$2) is inconclusive for equivalence in both pairs ($p{=}0.076$ for \cls{}--\cwm{}, $p{=}0.187$ for \cls{}--\traj{}), reflecting the severe power limitation of 3-seed comparisons (power ${\sim}$0.08 at $\pm$2\pp{} margin with df${=}$2). Bayesian ROPE provides moderate support: $P(\text{ROPE}){=}0.887$ for \cls{}--\cwm{} and $P(\text{ROPE}){=}0.780$ for \cls{}--\traj{}. Under problem-level clustered bootstrap, both comparisons reach significance ($p{=}0.0006$ and $p{=}0.043$ respectively), but this analysis treats within-seed observations as exchangeable, potentially understating between-seed uncertainty. The monotonic gap reduction (3.11\pp{} at 4B $\to$ 2.24\pp{} at 8B $\to$ 1.07\pp{} at 14B) favors a capacity-dependent convergence interpretation, though formal confirmation at seed level requires more training seeds.
451	
452	
453	\section{Variant-Level Effect Sizes}
454	\label{app:power}
455	
456	Table~\ref{tab:variant_power} reports variant-level bootstrap confidence intervals for the repo-level formulation comparisons ($n{=}48$ variants). Following Hoenig and Heisey~\cite{hoenig2001}, we report minimum detectable effect (MDE) rather than post-hoc observed power.
457	
458	\begin{table}[h]
459	\centering
460	\small
461	\caption{Variant-level bootstrap analysis ($n{=}48$). \cls{}--\cwm{} uses paired bootstrap (same variants, same seed); \cls{}--\traj{} uses unpaired bootstrap (per-variant \traj{} predictions not archived for pairing). MDE at $n{=}48$: ${\sim}$25\pp{}.}
462	\label{tab:variant_power}
463	\setlength{\tabcolsep}{3pt}
464	\resizebox{\columnwidth}{!}{%
465	\begin{tabular}{llccc}
466	\toprule
467	\textbf{Comparison} & \textbf{Config} & \textbf{$\Delta$ (\pp{})} & \textbf{95\% CI} & \textbf{$p$} \\
468	\midrule
469	\multicolumn{5}{l}{\emph{\cls{} vs.\ \cwm{} (paired)}} \\
470	& Qwen3-8B & +29.17 & [10.42, 47.92] & 0.003 \\
471	& DeepSeek-6.7B & +35.42 & [18.75, 50.05] & ${<}$0.001 \\
472	\midrule
473	\multicolumn{5}{l}{\emph{\cls{} vs.\ \traj{} (unpaired)}} \\
474	& Qwen3-4B & $-$4.17 & wide & 0.740 \\
475	& Qwen3-8B & +8.33 & wide & 0.385 \\
476	& DeepSeek-6.7B & 0.00 & wide & 1.000 \\
477	\bottomrule
478	\end{tabular}}
479	\end{table}
480	
481	At $n{=}48$, the MDE is ${\sim}$25\pp{}. The \cls{}--\cwm{} gap (29--35\pp{}) exceeds this threshold, confirming that $n{=}48$ is sufficient to detect the observed divergence. The \cls{}--\traj{} gaps ($<$10\pp{}) fall well below the MDE: any true difference is too small to detect at this sample size, consistent with the function-level TOST equivalence (\S\ref{sec:equivalence}).
482	
483	The \cls{}--\traj{} unpaired bootstrap produces wider confidence intervals than paired analysis would; \traj{} per-variant predictions were not archived in a format that permits pairing. The \cls{}--\cwm{} paired comparison uses \cls{} s123 vs.\ \cwm{} s42 (different seeds), but the CI lower bound of 10.42\pp{} far exceeds the seed noise observed in function-level experiments ($<$2\pp{}).
484	
485	
486	\section{Multiple Comparison Correction}
487	\label{app:holm}
488	
489	Table~\ref{tab:holm} (main text) applies Holm-Bonferroni correction~\cite{holm1979} to the five primary statistical comparisons across this study ($k{=}5$, family-wise $\alpha{=}0.05$).
490	
491	The two core claims survive correction: the repo-level \cls{}--\cwm{} divergence (adjusted $p{=}0.015$) and function-level \cls{}--\cwm{} equivalence (adjusted $p{=}0.028$). The function-level \cls{}--\traj{} equivalence does not survive correction (adjusted $p{=}0.075$). Under problem-level clustered bootstrap, the raw TOST $p$ decreases to ${\sim}$0.007 (adjusted $p{\approx}0.021$), which would confirm equivalence; we report the more conservative seed-level result ($p{=}0.025$) as primary, since training seeds are the true unit of replication.
492	
493	\section{Mixed-Effects Regression}
494	\label{app:interaction}
495	
496	We fit mixed-effects linear probability models (LPM) with heteroskedasticity-robust standard errors (HC1) to test the formulation$\times$complexity interaction formally~\cite{moulton1990}. We choose LPM because coefficients are directly interpretable as probability differences (percentage points), consistent with the reporting units in the main text; at these sample sizes ($n{\approx}56$K cross-complexity, repo-level pooled cross-model) and base rate range (0.6--0.9), LPM and logistic regression yield concordant conclusions for all primary effects~\cite{angrist2009mostly} (confirmed below).
497	
498	\paragraph{Cross-complexity model (DeepSeek-Coder).} \texttt{correct $\sim$ formulation $\times$ complexity + (1|problem\_id)}, $n{=}56{,}480$ observations (\cls{} + \cwm{} $\times$ function + repo), 139 problem clusters. The \cwm{} main effect at function level is non-significant ($\hat{\beta}{=}-0.002$, $z{=}-0.25$, $p{=}0.805$); the \cwm{}$\times$repo interaction is highly significant ($\hat{\beta}{=}-0.219$, $z{=}-23.7$, $p{<}0.001$). \cwm{} and \cls{} are statistically indistinguishable at function level ($\Delta{=}-0.2$\pp{}, $p{=}0.805$) but diverge by 22\pp{} at repo level, confirming the complexity-dependent divergence is not an artifact of aggregation.
499	
500	\paragraph{Repo-level cross-model model.} \texttt{correct $\sim$ formulation $\times$ model + (1|problem\_id)}, both model families, repo level only. \cwm{} deficit: $\hat{\beta}{=}-0.22$ ($-$22\pp{}, $z{=}-64.4$, $p{<}0.001$). Model effect: +1.1\pp{} for Qwen3 ($z{=}3.1$, $p{=}0.002$ in LPM; not significant under GEE, $p{=}0.449$). Formulation$\times$model interaction: +1.6\pp{} less \cwm{} degradation on Qwen3 ($z{=}2.8$, $p{=}0.006$ in LPM; not significant under GEE, $p{=}0.860$). Formulation dominates the predictable variance; model identity is directionally positive but specification-dependent. The 25-cluster random intercept structure limits effective degrees of freedom for the random effects; inferences on fixed effects (formulation, complexity) are robust as they pool across the full observation count.
501	
502	\paragraph{Logistic regression robustness check.} To verify that LPM conclusions are not artifacts of the linear link function, we fit GEE logistic regression (binomial family, exchangeable working correlation, robust sandwich standard errors) to the same data. For the cross-complexity model, the \cwm{} main effect at function level has OR$=$0.98 (95\% CI [0.86, 1.12], $p{=}0.771$) and the \cwm{}$\times$repo interaction has OR$=$0.31 ([0.15, 0.65], $p{=}0.002$). Average marginal effects are $-$0.2\pp{} (function) and $-$21.6\pp{} (repo), matching LPM coefficients within 0.3\pp{}. For the cross-model model, the \cwm{} deficit has OR$=$0.30 ([0.15, 0.63], $p{=}0.001$, AME$=$\,$-$21.1\pp{}). Direction, magnitude, and significance of all primary effects are concordant between LPM and logistic regression; minor discrepancies in secondary effects (model identity, formulation$\times$model interaction: $p{=}0.449$ and $p{=}0.860$ under GEE vs.\ $p{=}0.002$ and $p{=}0.006$ under LPM) reflect the GEE's more conservative cluster-robust inference with $k{=}25$ clusters. The discrepancy in secondary effects reflects cluster count: the cross-complexity model ($k{=}139$) yields reliable sandwich SEs, while the cross-model model ($k{=}25$) falls below the $k{\geq}40$ threshold recommended for stable cluster-robust inference~\cite{cameron2008bootstrap}.
503	
504	\section{CWM Parseable Bias Analysis}
505	\label{app:parseable_bias}
506	
507	Figure~\ref{fig:cwm_unparseable} (main text) summarises the unparseable rate contrast across complexity levels.
508	
509	The default-to-pass assignment for unparseable \cwm{} outputs is not random with respect to instance difficulty. Unparseable instances have significantly higher pass rates than parseable ones (74.6\% vs.\ 68.3\%, $\chi^2$ $p = 5.9 \times 10^{-10}$), and \cls{} models achieve higher accuracy on unparseable instances (86.4\% vs.\ 79.1\%, $p = 3.3 \times 10^{-18}$). This indicates that \cwm{}'s parsing failures concentrate on simpler, pass-heavy instances where the majority-class default happens to be correct more often. Cross-model Jaccard overlap of unparseable instance sets is 0.46, confirming this pattern is instance-driven (specific inputs consistently cause parsing failure across models) rather than stochastic. The net effect is that \cwm{}'s reported accuracy is inflated by default-correct assignments on easy instances, while its effective discriminative accuracy on harder instances is substantially lower than the aggregate figure suggests.
510	
511	
512	\section{Threats to Validity (Full Analysis)}
513	\label{app:threats}
514	
515	We identify five potential confounds and assess their impact on our conclusions.
516	
517	\paragraph{Checkpoint selection.} Val-based selection is unavailable for runs with NaN validation loss (DeepSeek \cwm{} repo-level runs, DeepSeek \cls{} s123), which default to the final epoch checkpoint. A checkpoint ablation on Qwen3-8B \cls{} s42 quantifies this confound: epoch~1 (ckpt-2200) achieves 85.34\%, val-selected (ckpt-3600) 84.48\%, and final epoch (ckpt-6633) 85.29\%, a $<$1\pp{} range. The val-selected checkpoint is the lowest, indicating no upward bias from checkpoint selection. The Qwen3-8B \traj{} comparison (epoch 2: 72.92\% vs.\ epoch 3: 70.83\%) shows a slightly larger ${\sim}$2\pp{} shift. For \cwm{}, the convergence analysis (Appendix~\ref{app:cwm_convergence}) shows eval loss at the final epoch is 1.8$\times$ its minimum; however, early-stopped checkpoints retain high unparseable rates, leaving the qualitative ranking unchanged.
518	
519	\paragraph{\cwm{} convergence analysis.}
520	\label{app:cwm_convergence}
521	Qwen3-8B \cwm{} repo-level eval loss reaches its minimum within ${\sim}$5\% of training (step 300--400 of 6{,}633) and increases monotonically thereafter, with no plateau or recovery (Table~\ref{tab:cwm_convergence}). This pattern is consistent across all three seeds, confirming systematic overfitting to trace generation rather than stochastic variation. The final-epoch eval loss is ${\sim}$1.8$\times$ the optimal value. By contrast, function-level \cwm{} achieves \cls{}-equivalent accuracy (TOST $p{=}0.007$) with the same training recipe, indicating that the overfit is specific to repo-level output complexity. Cross-model validation: a DeepSeek-Coder early-stopped checkpoint (s123, epoch~1) achieves 75.45\% versus 57.31\% at epoch~3 (s123; +18.14\pp{}), but retains 66.4\% unparseable rate, confirming that format collapse emerges early and is not a late-training artifact. No epoch-level checkpoint is available for Qwen3 CWM (only step-level checkpoints at steps 300/400 and late steps ${\geq}$5800; continuous epoch checkpointing was not enabled for this training run). The convergence analysis (Table~\ref{tab:cwm_convergence}) shows eval loss minimum at step 300--400 across all three Qwen3 seeds, consistent with DeepSeek-Coder's epoch-1 improvement, providing cross-model evidence that the overtraining pattern generalizes. An early checkpoint (step 400, ${\sim}$6.5\% of training, s42) yields 65.17\% repo-level accuracy with 63.7\% unparseable rate, comparable to or below final-epoch performance (66.93--67.33\% accuracy, 60.4--63.9\% unparseable; s123/s456 at step 6633). This rules out late-training format degradation: collapse is present from early training, and the optimal eval-loss checkpoint does not recover repo-level accuracy. A later checkpoint (step 6100, s42, seq8192) achieves 69.50\% test accuracy despite substantially higher validation loss than val-best ckpt-400 (64.36\%), suggesting that validation loss may not be a reliable proxy for test-set performance in \cwm{} repo-level evaluation.
522	
523	\begin{table}[h]
524	\centering
525	\small
526	\caption{\cwm{} repo-level eval loss across training (Qwen3-8B, 3 seeds). Minimum is reached at step 300--400 (${\sim}$5\% of training); subsequent training monotonically increases loss.}
527	\label{tab:cwm_convergence}
528	\begin{tabular}{lccc}
529	\toprule
530	Step & s42 & s123 & s456 \\
531	\midrule
532	300 & 0.291 & \textbf{0.288} & \textbf{0.277} \\
533	400 & \textbf{0.286} & 0.306 & 0.283 \\
534	1000 & 0.333 & 0.336 & 0.351 \\
535	3000 & 0.445 & 0.453 & 0.435 \\
536	6600 & 0.521 & 0.517 & 0.507 \\
537	\bottomrule
538	\end{tabular}
539	\end{table}
540	
541	\paragraph{Evaluation sequence length.} \cwm{} accuracy varies by ${\sim}$9\pp{} across evaluation sequence lengths for the same checkpoint (seq2048: ${\sim}$65\% vs.\ seq4096: ${\sim}$56\%), driven by unparseable-rate differences that propagate through majority-class default assignment. \cls{} is invariant to this parameter. Cross-model \cwm{} comparisons use different eval lengths (Qwen3: 8192, DeepSeek: 4096) and are not directly comparable in absolute terms. A matched-sequence evaluation shows ${\sim}$1.5\pp{} difference for \cls{} (Appendix~\ref{app:ablations}), insufficient to explain the 18--26\pp{} gap. Furthermore, increasing Qwen3-8B \cwm{} evaluation from seq4096 to seq8192 \emph{raises} the unparseable rate (63.7\%$\to$73.8\%) while changing accuracy by only 0.81\pp{} (64.36\%$\to$65.17\%); giving the model more generation budget worsens format compliance rather than improving it, confirming that format collapse is a structural bottleneck rather than a truncation artifact. Practitioners must standardize evaluation sequence length for generation-based formulations.
542	
543	\paragraph{Preprocessing.} DeepSeek \cls{} accuracy ranges from 82.61\% (s42, drop preprocessing) to 74.93\% (s123, truncate preprocessing), a 7.68\pp{} spread that conflates preprocessing strategy, checkpoint selection method, and seed. The two strategies produce different effective training sets (67,343 vs.\ 70,748 samples) and different checkpoint selection regimes. The qualitative ranking \cls{} $>$ \cwm{} holds under both strategies (Table~\ref{tab:taxonomy}).
544	
545	\paragraph{\traj{} training regime.} \traj{} uses a different training configuration: smaller training set (${\sim}$400 repo-level variants vs.\ ${\sim}$70K per-test instances), higher learning rate ($2{\times}10^{-4}$ vs.\ $5{\times}10^{-5}$), and variant-level labels. This asymmetry is inherent to the formulation (trajectory-level labels are only available at variant granularity), but precludes training-data-controlled comparison at repo level. The downsample ablation confirms the \cls{} formulation advantage persists at matched data volume (80.74\% vs.\ 72.92\%; Appendix~\ref{app:downsample}), though it controls for training volume but not label granularity (per-test vs.\ variant-level). Crucially, \traj{} achieves statistical equivalence with \cls{} at function level (${\leq}$1.3\pp{}, \S\ref{sec:func_results}), demonstrating the formulation itself is viable; the repo-level gap attribution remains uncertain: data volume (${\sim}$400 variants vs.\ ${\sim}$70K per-test instances) and label granularity (variant-level vs.\ per-test) are both plausible confounds that cannot be separately controlled.
546	
547	\paragraph{\cwm{} scale and pretraining.} Our \cwm{} baseline uses 4--8B LoRA fine-tuning without execution trace pretraining. The original Code World Model~\cite{meta2025cwm} uses 32B parameters with mid-training on execution traces, a fundamentally different training regime. At larger scale or with execution-trace pretraining, the generation bottleneck observed here may diminish: larger models produce more coherent long-form outputs, and execution trace exposure may improve output format compliance. This is the primary limitation: all repo-level \cwm{} conclusions are conditional on the ${\leq}$8B LoRA regime.
548	
549	Despite these confounds, the repo-level \cls{}--\cwm{} gap (18--26\pp{}) exceeds any single assessed confound. Even under worst-case compounding (${\sim}$11.5\pp{}), the gap retains ${\geq}$7.5\pp{} margin; confounds predominantly disadvantage \cwm{}. However, correlated confounds and limited seed coverage mean definitive causal attribution requires multi-seed replication. At $n{=}48$, the minimum detectable effect (MDE) is ${\sim}$25\pp{}~\cite{hoenig2001}; the \cls{}--\cwm{} gap (29--35\pp{}) exceeds this threshold, while the \cls{}--\traj{} gap ($<$10\pp{}) falls below it, consistent with our TOST equivalence finding. Holm-Bonferroni correction across the five primary comparisons ($k{=}5$; Table~\ref{tab:holm}) confirms the \cls{}--\cwm{} gap (adjusted $p{=}0.015$) and function-level \cls{}--\cwm{} equivalence (adjusted $p{=}0.028$); function-level \cls{}--\traj{} equivalence does not survive correction (adjusted $p{=}0.075$), nor does the repo-level \cwm{}--\traj{} comparison (adjusted $p{=}0.078$). The consistent direction across both model families and all tested configurations supports a formulation-level explanation, though definitive causal attribution requires future experiments addressing each confound individually.
550	
551	
552	\paragraph{Extended validity discussion.}
553	\label{app:limitations}
554	The same-size 4B comparison uses a single seed; \cls{} 4B seed 123 (val-best ckpt-800) achieves only 75.33\% test accuracy (+2.4\pp{} above majority baseline); val-best selection at an early checkpoint (step 800) amplifies the val-test distribution shift observed across all configurations. The \cwm{} 8B comparison uses 3 seeds per model. The validation and test sets have zero problem overlap but differ in mutation type composition (Table~\ref{tab:mutation_distribution}): \texttt{operator\_swap} shifts from 19.1\% (val) to 34.3\% (test), the largest single-type distribution mismatch (+15.2\pp{}). All repo-level results use val-selected checkpoints, and checkpoint selection variance could contribute to observed differences. Our training data is synthetically constructed from mutation operators rather than real developer patches. While mutation testing literature establishes that mutants are reasonable proxies for real faults in test effectiveness studies~\cite{andrews2005mutation,just2014mutants}, these findings concern mutation \emph{adequacy} (whether tests that kill mutants also detect real faults), not whether verifiers trained on mutants transfer to real patches. However, the coupling effect underlying these results supports \emph{relative ranking} validity: a domain shift from synthetic mutations to real bugs may affect absolute accuracy levels, but our core finding (that formulation choice matters at repo level but not function level) concerns relative performance ordering, which is expected to be preserved under distributional shifts that affect all formulations equally. The synthetic-to-real transfer gap for absolute accuracy remains untested. The \traj{} training configuration differs from \cls{}/\cwm{}: smaller training set (${\sim}$400 vs.\ ${\sim}$70K instances), different learning rate ($2{\times}10^{-4}$ vs.\ $5{\times}10^{-5}$), and variant-level evaluation ($n{=}48$ vs.\ per-test $n{=}9{,}784$). The function-level \cls{}--\traj{} TOST equivalence ($p = 0.025$, seed-level paired, $\pm$2\pp{}) is computed on 523 matched variant-level instances across 5 seeds; 2 of 5 seeds use NF4 quantization. Restricting to three bfloat16 seeds yields a comparable mean gap ($-$0.45\pp{}) but wider confidence interval (df${=}$2); the TOST $p$-value increases to 0.128, which reflects reduced statistical power rather than a shift in the point estimate. The NF4 seeds contribute precision (narrowing the CI) without shifting the mean, consistent with precision being comparable across both quantization levels at function level. Repo-level \cls{}--\traj{} comparison should be interpreted with caution due to configuration and granularity differences.
555	
556	\paragraph{Domain contrast with generative verification in math reasoning.}
557	GenRM~\cite{hosseini2025genrm} demonstrates that generative verifiers outperform discriminative ones for math reasoning. Our results reveal a domain-specific divergence: in code repair verification, the generative formulation (\cwm{}) does not outperform the discriminative one (\cls{}), and degrades sharply at repository level. The key difference is output space structure: math reasoning generates natural-language solution traces with flexible formatting, whereas code execution output requires exact syntactic compliance (specific variable values, error messages, stack traces). This structural constraint makes format collapse, absent in math verification, the dominant failure mode for code \cwm{} at repo level (53--74\% unparseable). The domain contrast suggests that the generative verification advantage is contingent on output space complexity rather than being a universal property of verifier architecture.
558	
559	\paragraph{Use of AI assistants.}
560	\label{app:ai-assistants}
561	Claude (Anthropic) assisted with code, writing, and literature review.
562	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "771bad3f-f358-4157-b30e-b4eb7b70497e",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "ed2fa61f-bccf-42c9-98ff-40fb378f5a67",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
      "content": "\\appendix\n\n\\noindent\\textbf{Appendix overview.} A: Oracle analysis. B: Ablations. C: Per-mutation breakdown. D: Variant-level accuracy. E: Hyperparameters. F: Prompt templates. G: Mutation distribution. H: Qualitative errors. I: Extended analysis (I.a--I.k). J: TOST sensitivity (J.1: Bayesian ROPE). K: Effect sizes. L: Holm-Bonferroni. M: Mixed-effects regression. N: Parseable bias. O: Threats (O.1: CWM convergence; O.2: Extended validity). P: AI assistants.\n\n\\section{Oracle Accuracy-Utility Analysis}\n\\label{app:oracle}\n\nWe stratify SWE-bench Verified instances by Fail-to-Pass (F2P) test count $T$, comparing per-test vs.\\ trajectory-level oracle resolve rates under i.i.d.\\ and block-correlated error models (ICC $= 0.191$, from function-level analysis; \\S\\ref{sec:equivalence}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses function-level ICC $= 0.191$ (from function-level analysis, \\S\\ref{sec:equivalence}). Pass-to-Pass (P2P) regression rate: 1.04\\% mean, 0\\% median.}\n\\label{tab:oracle}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{$T$} & \\textbf{Inst.\\%} & \\textbf{i.i.d.\\ (\\pp{})} & \\textbf{Block (\\pp{})} & \\textbf{Contrib.\\%} \\\\\n\\midrule\n$1$ & 68.7 & $-$0.04 & $-$0.09 & $\\approx$0 \\\\\n$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\\\\n$3$--$5$ & 7.1 & 25.00 & 40.74 & $\\approx$26 \\\\\n$\\geq 6$ & 5.1 & 30.00 & 40.06 & $\\approx$19 \\\\\n\\midrule\n\\textbf{All} & 100.0 & --- & \\textbf{10.93} & 100.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFigure~\\ref{fig:oracle_stratified} (main text) shows the oracle per-test advantage by F2P test count.\n\nTable~\\ref{tab:oracle} and Figure~\\ref{fig:oracle_stratified} reveal a sharp concentration: at $T = 1$ (68.7\\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T = 2$ (19.1\\%), where block-correlated advantage reaches 31.69\\pp{} (55.3\\% of total). The overall block-correlated advantage is 10.93\\pp{}, driven by the $T \\geq 2$ minority. Block correlation amplifies relative to i.i.d.: at $T = 2$, 31.69\\pp{} vs.\\ 18.49\\pp{} (1.7$\\times$). P2P regression is negligible (1.04\\% mean, 0\\% median); the practical value concentrates in F2P discrimination.\n\n\\paragraph{Sensitivity to ICC estimate.}\nThe analysis above uses ICC $= 0.191$ from function-level analysis (\\S\\ref{sec:equivalence}), where mean cluster size $\\bar{k} \\approx 16.5$ yields DEFF $= 3.97$. At repository level, within-problem correlation is substantially stronger: ICC $= 0.3146$ with DEFF $= 114.4$ (\\S\\ref{sec:repo}), yielding an effective sample size of $n_{\\text{eff}} \\approx 9{,}784 / 114.4 \\approx 86$ independent observations~\\cite{moulton1990}, still sufficient for regression but limiting precision of variance component estimates. This is a consequence of the larger and more heterogeneous test suites in SWE-bench Verified problems. Under higher ICC, within-problem errors cluster more tightly and amplify the block-correlated per-test advantage at each $T$ stratum; the correction from i.i.d.\\ to block-correlated grows monotonically with ICC. The function-level ICC $= 0.191$ used in Table~\\ref{tab:oracle} thus provides a conservative lower bound on the per-test advantage. The repo-level correlation structure would yield an even larger gap between per-test and trajectory-level oracle resolve rates, which strengthens the case for per-test granularity at repository-level complexity.\n\n\\section{Ablation Studies}\n\\label{app:ablations}\n\n\\paragraph{LoRA rank sensitivity.}\nAll \\cwm{} experiments use LoRA rank $r{=}16$. To test whether this capacity constraint handicaps \\cwm{}, we train rank-32 variants (seed 42), doubling adapter parameters.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{LoRA rank ablation for \\cwm{} 4B (seed 42, 3 epochs, lr $= 2{\\times}10^{-4}$). Rank-16 seed variance: 0.53\\pp{} (seeds 42 vs.\\ 456).}\n\\label{tab:rank_ablation}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Config} & \\textbf{$\\alpha/r$} & \\textbf{Acc (\\%)} & \\textbf{Fail \\fone{}} & \\textbf{Pass \\fone{}} & \\textbf{$\\Delta$} \\\\\n\\midrule\n$r{=}16$, $\\alpha{=}32$ & 2 & \\textbf{87.51} & --- & --- & --- \\\\\n$r{=}32$, $\\alpha{=}32$ & 1 & 87.00 & 87.1 & 86.9 & $-$0.51 \\\\\n$r{=}32$, $\\alpha{=}64$ & 2 & 87.04 & 87.27 & 86.79 & $-$0.47 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth rank-32 variants fall within the 2-seed variance of the rank-16 baseline (0.53\\pp{} between seeds 42 and 456; Table~\\ref{tab:rank_ablation}). The $\\alpha{=}64$ variant (matching the baseline $\\alpha/r{=}2$ ratio) rules out the confound that the $\\alpha{=}32$ result might reflect reduced effective scaling rather than rank insensitivity. This is consistent with \\cwm{}'s function-level performance being bounded by output-format constraints rather than adapter capacity.\n\n\\paragraph{Majority voting.}\nMajority voting ($K{=}3$) decreases accuracy from 87.51\\% to 86.83\\% ($-$0.68\\pp{}): errors are systematic rather than stochastic, so sampling-based ensembles do not help.\n\n\\paragraph{Sequence-length ablation details.}\nBoth formulations are trained with \\texttt{max\\_seq\\_length}$=$2,048. At inference, \\cwm{} reserves \\texttt{max\\_new\\_tokens}$=$512, leaving ${\\sim}$1,536 effective input tokens; \\cls{} allocates nearly all context to input (5,120--8,192 tokens). A matched-context ablation (\\cls{} 8B at 2,048 tokens) achieves 83.04\\%, only 1.44\\pp{} below the 8,192-token evaluation (84.48\\%), though truncation introduces 136 unparseable outputs (1.39\\% of test samples). The matched-context gap (\\cls{}@2,048 vs.\\ \\cwm{}@2,048) is 25.00\\pp{} (98\\% of the full 25.59\\pp{} gap), confirming that input context disparity explains at most 3\\% of the difference.\n\n\\paragraph{Training data size control.}\n\\label{app:downsample}\nTo control for the training set size asymmetry between \\cls{} (${\\sim}$70K instances) and \\traj{} (386 variant-level instances, ${\\sim}$8K per-test equivalents, at repo level), we downsample \\cls{} training data to match \\traj{} in data volume. Downsampled \\cls{} (Qwen3-4B, seed 42) achieves 80.74\\% repo-level per-test accuracy, only 2.89\\pp{} below the full-data \\cls{} (83.63\\%) and still 7.82\\pp{} above \\traj{} (72.92\\%). The \\cls{} formulation advantage is not attributable to training data volume.\n\nAt function level, the relationship reverses: \\traj{} uses 8,052 variant-level instances (2.24$\\times$ more unique variants than \\cls{}/\\cwm{}'s 3,596 from 15,290 per-test instances). \\cls{} nonetheless outperforms \\traj{} by 2.13\\pp{} (88.43\\% vs.\\ 86.30\\%, Qwen3-4B), ruling out data volume as the explanation. An extreme downsample ablation (CLS trained on 447 per-test instances, ${\\sim}$105 unique variants) achieves 78.57 $\\pm$ 0.78\\%, confirming that per-test classification maintains reasonable performance under severe data reduction, though it falls below \\traj{} (86.30\\%) given the 20$\\times$ data disadvantage.\n\n\\paragraph{Few-shot prompting baselines.}\n\\label{app:few_shot}\nWe evaluate 3-shot in-context learning at repo level to test whether prompting strategy closes the gap to fine-tuned models. Table~\\ref{tab:few_shot} reports both per-test and variant-level accuracy.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Repo-level prompting baselines (per-test $n{=}9{,}784$; variant-level $n{=}48$). Majority baseline: 72.96\\% per-test, 54.17\\% variant-level.}\n\\label{tab:few_shot}\n\\setlength{\\tabcolsep}{4pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{0-shot (per-test)} & \\textbf{3-shot (per-test)} & \\textbf{3-shot (variant)} \\\\\n\\midrule\nQwen3-8B & 49.90\\% & 71.61\\% & 45.83\\%\\textsuperscript{$\\ast$} \\\\\nDeepSeek-6.7B & 48.54\\% & 46.28\\% & 45.83\\%\\textsuperscript{$\\ast$} \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{2pt}\n{\\footnotesize \\textsuperscript{$\\ast$}Both models achieve 45.83\\% by correctly classifying all 22 unresolved variants and zero resolved variants (22/48 = 45.83\\%), equivalent to an always-predict-unresolved baseline. The 100\\% overlap in variant-level predictions confirms complete degradation at task-relevant granularity.}\n\\end{table}\n\nBoth models converge to exactly 45.83\\% variant-level accuracy under 3-shot prompting, below majority baseline (54.17\\%). Variant-level analysis reveals this is not a coincidence: both models correctly classify all 22 unresolved variants and zero resolved variants, equivalent to an always-predict-unresolved baseline with 100\\% prediction overlap. Per-test accuracy diverges sharply (Qwen3-8B 71.61\\% vs.\\ DeepSeek 46.28\\%), but this divergence is entirely superficial: Qwen3-8B predicts pass on nearly all tests, inflating per-test accuracy on a pass-heavy dataset (72.96\\% pass rate) without genuine discriminative ability. Per-test metrics can thus severely misrepresent baseline capability; variant-level evaluation is necessary to detect complete degradation. Neither 0-shot nor few-shot prompting approaches fine-tuned performance (82--84\\% per-test); fine-tuning is a necessary condition for repo-level verification.\n\n\\section{Repo-Level Per-Mutation Breakdown}\n\\label{app:repo_mutation}\n\nTable~\\ref{tab:mutation_breakdown} compares per-mutation accuracy at repo level. \\cls{} produces 0\\% unparseable outputs; all values are direct classification accuracy. \\cwm{} overall accuracy includes default-pass assignment for unparseable outputs (see \\S\\ref{sec:repo}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-mutation test accuracy (\\%) at repo level (SWE-bench Verified, $n{=}9{,}784$). \\cls{} 8B reports two seeds; $\\Delta$ is mean 4B$\\to$8B gain for \\cls{}. \\cwm{} 4B per-mutation overall accuracy omitted for non-gold mutations due to low parse rates (4.4--56.9\\%, Table~\\ref{tab:cwm_mutation_parse}); gold overall accuracy derived from parse rate 43.5\\% and parseable accuracy 23.5\\%.}\n\\label{tab:mutation_breakdown}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lccccccc}\n\\toprule\n\\textbf{Mutation} & \\textbf{$n$} & \\textbf{CLS 4B} & \\textbf{CLS 8B s42} & \\textbf{CLS 8B s123} & \\textbf{CWM 4B} & \\textbf{CWM 8B} & \\textbf{$\\Delta$ CLS} \\\\\n\\midrule\ngold & 4,633 & 98.25 & 96.24 & 99.60 & 66.72 & 80.06 & $-$0.33 \\\\\noperator\\_swap & 3,357 & 78.91 & 81.38 & 82.60 & --- & 54.57 & +3.08 \\\\\noff\\_by\\_one & 183 & 58.47 & 86.89 & 79.20 & --- & 63.39 & \\textbf{+24.58} \\\\\nreturn\\_value & 562 & 67.97 & 75.44 & 66.40 & --- & 49.11 & +2.95 \\\\\nboundary\\_removal & 1,049 & 46.90 & 46.90 & 44.90 & --- & 42.23 & $-$1.00 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFigure~\\ref{fig:mutation_heatmap} visualises the per-mutation accuracy contrast between \\cls{} and \\cwm{} at repo level.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig_mutation_heatmap.pdf}\n\\caption{Per-mutation repo-level accuracy heatmap. \\cls{} 8B values are seed-averaged (s42/s123). \\cwm{} 8B includes default-pass for unparseable outputs. \\texttt{boundary\\_removal} is a scale-invariant difficulty ceiling (${\\sim}$45\\%) for both formulations.}\n\\label{fig:mutation_heatmap}\n\\end{figure}\n\nTable~\\ref{tab:cwm_mutation_parse} shows that \\cwm{} generation quality degrades from 4B to 8B across all mutation types.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{\\cwm{} parse rates and parseable-only accuracy per mutation type (seed 42). Parse rate decreases uniformly from 4B to 8B; parseable-only accuracy is below random binary chance (50\\%) for gold at both scales.}\n\\label{tab:cwm_mutation_parse}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{Parse Rate (\\%)}} & \\multicolumn{2}{c}{\\textbf{Parse Acc (\\%)}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n\\textbf{Mutation} & \\textbf{4B} & \\textbf{8B} & \\textbf{4B} & \\textbf{8B} \\\\\n\\midrule\ngold & 43.5 & 23.9 & 23.5 & 16.5 \\\\\noperator\\_swap & 56.9 & 21.2 & 63.1 & 58.8 \\\\\noff\\_by\\_one & 4.4 & 27.3 & 0.0 & 38.0 \\\\\nreturn\\_value & 48.8 & 26.9 & 27.0 & 56.9 \\\\\nboundary\\_removal & 30.6 & 51.8 & 59.2 & 51.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKey findings: (1)~Gold parse rate collapses from 43.5\\% to 23.9\\% at 8B; the simplest generation target (unmodified code, where all tests pass) degrades most, consistent with a fundamental generation bottleneck rather than task difficulty. (2)~Among parseable outputs, gold accuracy is 16.5--23.5\\%: the model generates outputs that fail exact-match even for correct code. (3)~\\texttt{off\\_by\\_one} is an anomaly: parse rate \\emph{increases} from 4.4\\% to 27.3\\%, but this is from an extremely low base ($n{=}8$ parseable at 4B), making both directions unreliable for this category.\n\n\\section{Variant-Level Accuracy}\n\\label{app:variant_level}\n\nTable~\\ref{tab:variant_level} reports variant-level accuracy ($n{=}48$) alongside per-test accuracy for all repo-level configurations. For \\cls{}, the aggregation penalty (per-test $\\to$ variant-level drop) ranges from 1\\pp{} to 19\\pp{} and is largest for models with low fail recall under the all-pass rule. \\cwm{} variant-level accuracy (48--52\\%) falls at or below the majority baseline, consistent with format collapse as the dominant failure mode.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Repo-level per-test vs.\\ variant-level accuracy ($n{=}48$ variants). Penalty = per-test $-$ variant-level. \\traj{} predicts variant outcomes directly (no aggregation). Variant-level majority baseline: 54.17\\% (26/48).}\n\\label{tab:variant_level}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Seed} & \\textbf{Per-test (\\%)} & \\textbf{Variant (\\%)} & \\textbf{Penalty (\\pp{})} & \\textbf{Fail Recall (\\%)} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{\\cls{}}} \\\\\nQwen3-8B & s42 & 84.48 & 72.92 & 11.56 & 56.76 \\\\\nQwen3-8B & s123 & 85.60 & 81.25 & 4.35 & 51.44 \\\\\nQwen3-4B & s42 & 83.63 & 64.58 & 19.05 & 48.72 \\\\\nDeepSeek-6.7B & s42 (e1) & 82.61 & 81.25 & 1.36 & 51.02 \\\\\nDeepSeek-6.7B & s42 (e3) & 82.51 & 79.17 & 3.34 & 38.47 \\\\\nDeepSeek-6.7B & s123 & 74.93 & 56.25 & 18.68 & ${\\sim}$13.72 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{\\cwm{}}} \\\\\nQwen3-8B & s42 & 65.17 & 52.08 & 13.09 & --- \\\\\nDeepSeek-6.7B$^\\dagger$ & s123 & --- & 47.92 & --- & --- \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{\\traj{}}} \\\\\nQwen3-4B & s42 & --- & 72.92 & --- & --- \\\\\nQwen3-8B & s42 & --- & 70.83 & --- & --- \\\\\nDeepSeek-6.7B & 3-seed & --- & 77.08 $\\pm$ 3.61 & --- & --- \\\\\n\\midrule\nMajority & --- & 72.96 & 54.17 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{2pt}\n\n{\\footnotesize $^\\dagger$Evaluated on ${\\sim}$75\\% of test instances (7210--7668 of 9784). DeepSeek \\traj{} Table~\\ref{tab:repo_level} reports 3 seeds (42/123/456) for alignment with \\cls{}/\\cwm{} seed coverage; three supplementary seeds (0/789/999) yield 75.0\\%, 66.7\\%, 79.2\\% respectively (6-seed mean 75.35 $\\pm$ 5.00\\%), consistent in direction.}\n\\end{table}\n\n\\section{Training Hyperparameters}\n\\label{app:hyperparams}\n\nTable~\\ref{tab:hyperparams} lists all hyperparameters used for fine-tuning. Both \\cls{} and \\cwm{} share the same LoRA configuration, optimizer, and training schedule; the only differences are per-device batch size, gradient accumulation steps (adjusted to maintain identical effective batch size of 32 across model sizes), and learning rate (DeepSeek-Coder uses $2{\\times}10^{-4}$ vs.\\ $5{\\times}10^{-5}$ for Qwen3, selected via grid search over $\\{5{\\times}10^{-5}, 1{\\times}10^{-4}, 2{\\times}10^{-4}\\}$ on held-out validation loss).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Training hyperparameters for \\cls{}/\\cwm{} configurations. \\traj{} models use lr $= 2{\\times}10^{-4}$ due to the smaller training set (${\\sim}$8K function-level instances vs.\\ ${\\sim}$70K for \\cls{}/\\cwm{}); other hyperparameters are shared.}\n\\label{tab:hyperparams}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll}\n\\toprule\n\\multicolumn{2}{l}{\\textbf{Shared across all configurations}} \\\\\n\\midrule\nLoRA rank / alpha / dropout & 16 / 32 / 0.05 \\\\\nLoRA targets & \\texttt{q/k/v/o\\_proj} \\\\\nOptimizer & AdamW ($\\beta_1{=}0.9$, $\\beta_2{=}0.999$) \\\\\nLR scheduler & Linear \\\\\nEffective batch size & 32 \\\\\nMax sequence length & 2,048 \\\\\nEpochs & 3 \\\\\nPrecision & bf16 \\\\\nGradient checkpointing & \\checkmark \\\\\nSeeds (function) & \\{42, 123, 456, 789, 0\\}\\textsuperscript{$b$} \\\\\nSeeds (repo) & \\{42, 123, 456\\}\\textsuperscript{$c$} \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{6pt}\n\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\multicolumn{4}{l}{\\textbf{Model-family--specific parameters}} \\\\\n\\midrule\n& \\textbf{Qwen3-4B} & \\textbf{Qwen3-8B} & \\textbf{DS-6.7B} \\\\\n\\midrule\nLearning rate & 5e-5 & 5e-5 & 2e-4 \\\\\nWeight decay & 0.01 & 0.01 & 0.0 \\\\\nWarmup ratio & 0.05 & 0.05 & 0.1 \\\\\nBatch / grad.\\ accum.\\ (\\cls{}) & 2 / 16 & 1 / 32 & 2 / 16 \\\\\nBatch / grad.\\ accum.\\ (\\cwm{}) & 1 / 32 & 1 / 32 & 1 / 32 \\\\\nTraining samples & 70,748 & 70,748 & 67,343--70,748\\textsuperscript{$a$} \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{2pt}\n{\\footnotesize $^a$DeepSeek \\cls{} canonical run (s42) uses drop preprocessing, which excludes 3,405 sequences exceeding max length (67,343 of 70,748). The s123 run uses truncate preprocessing (70,748 samples) but produces NaN validation loss. See \\S\\ref{sec:setup}. $^b$Seeds 789 and 0 use NF4 quantization; others use bf16. $^c$Repo-level seed coverage varies by configuration; see Table~\\ref{tab:repo_level} caption for per-model counts.}\n\\end{table}\n\n\\paragraph{Data processing.} DeepSeek CWM seeds use \\texttt{train\\_unified.py}, which drops samples exceeding \\texttt{max\\_seq\\_length} (3{,}405 of 70{,}748 samples, 4.8\\%). Qwen CWM seeds use \\texttt{train\\_repo\\_cwm.py}, which truncates and retains all samples. This difference affects total training steps (${\\sim}$12{,}627 vs.\\ ${\\sim}$13{,}266 for DeepSeek, ${\\sim}$6{,}633 for Qwen) but not the training data distribution, as dropped samples are uniformly distributed across labels.\n\n\\paragraph{Prompt templates.} Prompt templates for all formulations (\\cls{}, \\cwm{}, \\traj{}) are provided in the code repository. \\cls{} uses a binary classification template (``Does this test pass or fail?''); \\cwm{} uses an execution simulation template (``What is the output of this test?''); \\traj{} uses a variant-level verdict template (``Is this patch resolved or unresolved?'').\n\n\\paragraph{Mutation operators.} We use five mutation types: (1)~\\emph{gold}: unmodified code (all tests pass); (2)~\\emph{operator\\_swap}: replaces comparison or arithmetic operators (e.g., \\texttt{<} $\\to$ \\texttt{<=}); (3)~\\emph{off\\_by\\_one}: shifts loop bounds or array indices by $\\pm$1; (4)~\\emph{return\\_value}: modifies return statements (e.g., negating a boolean, changing a constant); (5)~\\emph{boundary\\_removal}: removes conditional guards or boundary checks. Mutation operators were applied using AST-level transformation; variants that did not alter any test outcome were discarded.\n\n\\paragraph{Compute budget.}\nAll experiments were conducted on NVIDIA RTX 5090 GPUs. Training time is approximately 1.5 hours per run for 4B models and 2 hours for 8B models. Total compute budget: ${\\sim}$370 GPU-hours across 223 completed runs (135 successful, 88 failed/killed; ${\\sim}$46 unique configurations including seeds, formulations, model sizes, and ablations).\n\n\\section{Prompt Templates}\n\\label{app:prompts}\n\nWe show representative prompt examples for each formulation. All examples use the same input instance for comparability.\n\n\\paragraph{CLS (per-test classification).}\n{\\footnotesize\\begin{verbatim}\nSystem: You are a code verifier.\nGiven a code patch and a test name,\npredict whether the test will pass\nor fail when run against the\npatched code.\n\nUser:\n## Patch (git diff)\n&lt;patch content> [... truncated]\n## Test\ntest_boundary_check\nWill this test pass or fail?\n\nTarget: pass\n\\end{verbatim}}\n\n\\paragraph{CWM (execution simulation).}\n{\\footnotesize\\begin{verbatim}\nSystem: You are a code execution\nsimulator. Given a code snippet and\na test case, predict the execution\nresult.\n\nUser:\n## Code\n&lt;code content> [... truncated]\n## Test\ntest_boundary_check\nWhat is the execution result?\n\nTarget: PASS: test completed\nsuccessfully\n\\end{verbatim}}\n\n\\paragraph{TRAJ (trajectory scoring).}\n{\\footnotesize\\begin{verbatim}\nSystem: You are a code repair\nverifier. Given the code patch and\ntest summary, predict whether all\ntests pass (resolved) or any test\nfails (unresolved).\n\nUser:\n[Code]\n&lt;patch content> [... truncated]\n[Test Summary]\n&lt;all test names and descriptions>\n\nTarget: resolved\n\\end{verbatim}}\n\n\\cls{} and \\cwm{} share the same input format (one code--test pair per instance); \\cls{} produces a single token (\\texttt{pass}/\\texttt{fail}), while \\cwm{} generates a variable-length execution trace. \\traj{} receives all tests concatenated and produces a single token (\\texttt{resolved}/\\texttt{unresolved}).\n\n\n\\section{Val-Test Mutation Type Distribution}\n\\label{app:mutation_distribution}\n\nTable~\\ref{tab:mutation_distribution} reports the mutation type composition of the repo-level validation and test sets. The most notable shift is \\texttt{operator\\_swap}, which nearly doubles from val (19.1\\%) to test (34.3\\%), while \\texttt{off\\_by\\_one} shrinks from 10.0\\% to 1.9\\%.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Repo-level mutation type distribution: validation vs.\\ test set, with per-type \\cls{} accuracy at two model sizes (seed 42). Shift = test\\% $-$ val\\%.}\n\\label{tab:mutation_distribution}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mutation Type} & \\textbf{Val (\\%)} & \\textbf{Test (\\%)} & \\textbf{Shift} & \\textbf{\\cls{} 4B} & \\textbf{\\cls{} 8B} \\\\\n\\midrule\ngold & 45.2 & 47.4 & +2.2 & 98.3 & 96.2 \\\\\noperator\\_swap & 19.1 & 34.3 & +15.2 & 78.9 & 81.4 \\\\\nboundary\\_removal & 15.0 & 10.7 & $-$4.3 & 46.9 & 46.9 \\\\\nreturn\\_value & 10.7 & 5.7 & $-$5.0 & 68.0 & 75.4 \\\\\noff\\_by\\_one & 10.0 & 1.9 & $-$8.1 & 58.5 & 86.9 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe \\texttt{operator\\_swap} shift is the primary source of val-test distribution mismatch. Since \\cls{} achieves moderate accuracy on this type (78.9--81.4\\%), the over-representation in the test set does not systematically bias overall accuracy estimates in either direction. Two boundary observations are notable: (1)~\\texttt{boundary\\_removal} represents a scale-invariant difficulty ceiling at ${\\sim}$47\\% across both model sizes: this mutation type resists capacity scaling; (2)~\\texttt{off\\_by\\_one} shows the largest scaling gain (+28.4\\pp{}, 58.5\\%$\\to$86.9\\%) but its small test share (1.9\\%) limits its contribution to overall accuracy differences across scales.\n\n\\section{Qualitative Error Analysis}\n\\label{app:qualitative}\n\nTo complement the quantitative divergence reported in \\S\\ref{sec:repo}, we examine representative errors from each formulation at repository level.\n\n\\paragraph{\\cwm{} failure modes.}\nTwo patterns account for the majority of unparseable \\cwm{} outputs on Qwen3. (1)~\\emph{Task misunderstanding}: the model generates a complete simulated test runner log (test names, timing, summary lines) rather than a pass/fail verdict. For instance, on \\texttt{django\\_\\_django-14315}, the model outputs a fabricated 1,248-token Django test execution trace with hallucinated test names that do not exist in the target file. The model confuses ``predict test outcome'' with ``simulate test execution environment.'' (2)~\\emph{Autoregressive degeneration}: the model enters a repetitive loop (e.g., repeating \\texttt{from \\_pytest.config import \\_parse\\_pytest\\_args} until truncation at 4,542 tokens). Both patterns produce zero usable signal and default to the majority-class label. This explains why unparseable predictions carry higher accuracy than parseable ones (\\S\\ref{sec:repo}).\n\n\\paragraph{\\cls{} failure modes.}\n\\cls{} errors concentrate in two categories requiring multi-step reasoning. False positives arise from \\emph{cross-concern value propagation}: a boundary removal mutation in \\texttt{pytest} converts a guarded attribute access (\\texttt{if xfailed and not xfailed.run}) to \\texttt{if True:}, causing a NoneType error on tests exercising unrelated skip marks. The model fails to trace the None path through the pytest hook lifecycle. False negatives arise from \\emph{mathematical equivalence}: on \\texttt{HumanEval/130} (Tribonacci variant), the model predicts failure for correct code because verifying the self-referential recurrence requires algebraic substitution rather than syntactic inspection. This single problem accounts for 17\\% of all function-level false negatives.\n\n\\paragraph{Complementarity.}\nThese failure patterns operate at different levels: \\cwm{} fails at the format level (producing no usable signal), while \\cls{} fails at the reasoning level (producing a confident but incorrect binary verdict). Both formulations are FP-dominant (over-predict failure), but \\cwm{}'s higher FP rate (70.3\\% vs.\\ 56.5\\%) means it over-predicts failure on instances \\cls{} correctly classifies, producing partial complementarity (oracle combination: 90.63\\%; \\S\\ref{app:extended_analysis}, paragraph a).\n\n\\section{Extended Analysis}\n\\label{app:extended_analysis}\n\n\\paragraph{Function-level CWM metric robustness.}\nAt function level, \\cwm{} outputs are short status strings (mean ${\\sim}$5--15 tokens). The unparseable rate is only 1.39\\%, and default-to-pass bias is $<$1\\pp{}, well below the SESOI threshold. Exact string matching is appropriate for these short, structured outputs; semantic-but-format-different matches are rare given the constrained output space.\n\n\\paragraph{(a) Error complementarity.}\n\\cls{} and \\cwm{} are both FP-dominant at function level but at different rates, producing partial complementarity. Among \\cls{} errors (seed 42), 56.5\\% are false positives (PASS $\\to$ FAIL); among \\cwm{} errors, 70.3\\% are false positives. Both formulations over-predict failure, but \\cwm{}'s stronger FP bias means it incorrectly rejects passing tests that \\cls{} correctly accepts. An oracle combination achieves 90.63\\% accuracy (1713/1890 correct, 177 both-wrong; +2.80\\pp{} over the best single formulation, \\cls{} 87.83\\%; single-seed estimate, seed 42). The complementarity arises from different \\emph{degrees} of fail-bias rather than opposite error directions: \\cwm{}'s generation bottleneck produces aggressive failure predictions, while \\cls{}'s single-token output is more calibrated. Ensemble approaches exploiting this degree difference are a natural direction.\n\n\\paragraph{(b) CWM error mode breakdown.}\nAmong unparseable \\cwm{} outputs (Qwen3, repo-level), 76.9\\% contain no execution keywords; 22.9\\% contain ambiguous co-occurring pass/fail keywords. Format compliance varies sharply across repositories (scikit-learn: near-zero unparseable; sphinx: 100\\%); repository-specific code patterns interact with the model's generation capabilities in complex ways. This per-repository variation is consistent with a model/tokenizer-specific failure rather than a formulation-level one.\n\n\\paragraph{(c) Relaxed matching does not rescue \\cwm{}.}\nRelaxed matching (tolerating format deviations, L0--L4) \\emph{decreases} \\cwm{} accuracy: 58.04\\%$\\to$56.98\\% (seed 42) and 59.09\\%$\\to$55.91\\% (seed 123). Unparseable predictions default to the majority class (pass, 72.96\\%), which outperforms the model's own parseable predictions (38--43\\%). The divergence widens from 26\\pp{} to 27\\pp{} under relaxed matching. This rules out the hypothesis that parsing strictness inflates the observed gap. Constrained decoding~\\cite{willard2023outlines} could enforce format compliance but would not address the semantic accuracy deficit among parseable outputs. An accidental training artifact provides further evidence: a \\cwm{} model inadvertently trained on function-level (\\cls{}-format) data achieved 86.05\\% accuracy with 0\\% unparseable outputs at repo level, recovering \\cls{}-level performance. This confirms that the repo-level \\cwm{} degradation stems entirely from trace generation complexity, not from the underlying verification task.\n\n\\paragraph{(d) Variance compression.}\n\\cwm{}'s 5-seed standard deviation (0.37\\pp{}) is lower than \\cls{} (0.78\\pp{}) and \\traj{} (0.97\\pp{}) at function level. If \\cwm{} performance is capped by output-format constraints at a given complexity level, seed-to-seed variability is compressed relative to formulations whose performance depends more on learned representations.\n\n\\paragraph{(e) Per-test precision and recall.}\n\\cls{} achieves fail \\fone{} 87.59\\% (precision 86.20\\%, recall 89.04\\%) at seed 42.% derived from overlap analysis (error_overlap_matched_seed.json); FP=130, FN=100, TP=848, TN=812\nMulti-F2P instances (6--10 tests) reach 96.3\\% accuracy, consistent with the oracle finding that per-test granularity is most valuable for complex instances.\n\n\\paragraph{(f) Block correlation.}\nWithin-problem errors are correlated (ICC $= 0.191$, DEFF $= 3.97$, 2.81$\\times$ more all-correct problems than i.i.d.\\ expectation). All statistical tests use clustered bootstrap accordingly.\n\n\\paragraph{(g) Failed interventions.}\nWe systematically tested four interventions targeting different hypothesized causes of \\cwm{} repo-level degradation; all failed:\n\n\\begin{itemize}[leftmargin=*,itemsep=1pt,topsep=2pt]\n\\item \\textbf{Capacity (rank 32, $\\alpha{=}64$):} $-$0.47\\pp{}, within seed variance (\\S\\ref{app:ablations}).\n\\item \\textbf{Majority voting ($K{=}3$):} $-$0.68\\pp{}; 93.3\\% unanimous, net flips negative (\\S\\ref{app:ablations}).\n\\item \\textbf{Relaxed matching (L0--L4):} $-$1.06\\pp{}; default-pass outperforms parseable predictions (paragraph~(c) above).\n\\item \\textbf{Model scaling (4B$\\to$8B):} parseable accuracy decreases (42.88\\%$\\to$38.52\\%) while unparseable rate rises (53.7\\%$\\to$73.8\\%); gain is a default-assignment artifact (\\S\\ref{sec:repo}).\n\\end{itemize}\n\n\\noindent Each intervention targets a distinct alternative explanation (insufficient capacity, random noise, parsing strictness, model scale); the uniform failure across all four confirms the bottleneck is formulation-level: output space complexity at repo level exceeds what ${\\leq}$8B generation models can handle, independent of these surface-level factors.\n\n\\paragraph{(h) Per-mutation scaling patterns.}\nScaling benefits are highly non-uniform across mutation types (Table~\\ref{tab:mutation_breakdown}). \\texttt{off\\_by\\_one} shows the largest \\cls{} scaling gain: 58.5\\% (4B) to 86.9\\% (8B, $+$28.4\\pp{}). In contrast, \\texttt{boundary\\_removal} is scale-invariant at ${\\sim}$47\\% across both sizes, which marks an intrinsic difficulty ceiling. For \\cwm{}, gold mutation parse rate collapses from 43.5\\% (4B) to 23.9\\% (8B) despite being the simplest target: generation capability degrades even for trivially correct code at larger scale within Qwen3. The val-test mutation type distribution differs notably (\\texttt{operator\\_swap} shifts from 19.1\\% to 34.3\\%; Table~\\ref{tab:mutation_distribution}), but this shift does not systematically bias overall accuracy because \\cls{} performance on \\texttt{operator\\_swap} (78.9--81.4\\%) is close to the overall mean.\n\n\\paragraph{(i) Inference efficiency.}\n\\cls{} achieves 217$\\times$ higher throughput than \\cwm{} at repo level (853 vs.\\ 3.9 inferences/min; Qwen3-4B, RTX 5090, 100 samples, avg ${\\sim}$1,040 input tokens). The speedup derives directly from the formulation: classification requires a single output token, whereas \\cwm{} generates an average of 477 tokens per inference. Median latency is 48ms (\\cls{}) vs.\\ 16.3s (\\cwm{}). At the observed unparseable rate of 73.8\\% (8B), the majority of \\cwm{}'s generation budget produces tokens that cannot yield a valid verdict. This \\cls{}--\\cwm{} efficiency gap is an inherent property of the formulation difference (1 vs.\\ $O(L)$ output tokens) and should generalize across models, unlike the accuracy divergence which may be model-contingent.\n\nThe \\cls{}--\\traj{} efficiency comparison is more nuanced, because \\cls{} makes one call per test while \\traj{} makes one call per instance. Per-call, \\cls{} is 20--138$\\times$ faster (depending on input length: 47ms for short contexts vs.\\ 2,632ms for \\traj{}). However, the per-instance effective speedup depends on test count $|T|$: at function level ($|T| \\approx 2.3$), \\cls{} is ${\\sim}$24$\\times$ faster (108ms vs.\\ 2,632ms per instance); at repo level ($|T| \\approx 12.3$, ${\\sim}$70ms/call with longer inputs), \\cls{} is ${\\sim}$3$\\times$ faster (861ms vs.\\ 2,631ms). A crossover exists at $|T| \\approx 50$ tests, beyond which \\traj{}'s single-call amortization dominates. This boundary condition is informative for deployment: \\cls{} is strongly preferred for function-level and moderate repo-level test suites, while extremely large test suites ($>$50 tests per instance) favor trajectory-level efficiency despite its coarser diagnostic signal.\n\n\\paragraph{(j) Re-repair pilot.}\nWe tested whether per-test diagnostic feedback improves downstream repair. A Qwen3-8B repair agent received either per-test diagnostic signals (which specific tests failed and why) or binary accept/reject feedback, evaluated on 44 SWE-bench Verified instances. The diagnostic condition achieved accuracy no higher than the binary baseline ($A_1 = 52.3\\%$, $p = 0.42$, effect size $\\approx 0$). Per-test diagnostic information does not automatically translate to repair improvements at this scale. The negative result may reflect insufficient agent capability to exploit fine-grained feedback, insufficient sample size (at $n = 44$, statistical power is ${\\sim}$0.3 for a medium effect size), or a genuine limitation of the diagnostic-to-repair translation.\n\n\\paragraph{(k) Relationship to chain-of-thought verification.}\n\\cwm{} is structurally a chain-of-thought verifier: the model generates an execution trace token by token and derives its PASS/FAIL verdict from the final trace state. If intermediate reasoning improved verification, \\cwm{} should outperform the reasoning-free \\cls{} baseline. At function level, no such advantage materialises: \\cwm{} and \\cls{} are statistically equivalent (TOST $p{=}0.007$, $\\pm$2\\pp{} margin; \\S\\ref{sec:equivalence}), indicating that the additional trace generation provides no accuracy benefit over direct binary classification. At repo level, the chain-of-thought mechanism actively \\emph{hurts}: trace generation triggers format collapse (53--74\\% unparseable), and even parseable traces yield accuracy below the majority baseline (38--43\\% vs.\\ 72.96\\%; paragraph~(c)). Four targeted interventions fail to rescue the generation pathway (paragraph~(g)). Within the ${\\leq}$8B LoRA regime, chain-of-thought--style verification does not outperform direct classification for execution prediction. Whether execution-trace pretraining at larger scale~\\cite{meta2025cwm} changes this conclusion remains the primary open question (\\S\\ref{sec:threats}).\n\n\\section{TOST Margin Sensitivity}\n\\label{app:tost_sensitivity}\n\nTable~\\ref{tab:tost_sensitivity} reports the TOST equivalence $p$-value as a function of the equivalence margin, computed on the 5-seed variant-level \\cls{}--\\cwm{} comparison (gap $= 1.24$\\pp{}, 523 variants, 114 clusters, clustered bootstrap).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{TOST margin sensitivity for \\cls{}--\\cwm{} equivalence (seed-level paired, 5 seeds, df${=}$4). The smallest margin achieving equivalence at $\\alpha = 0.05$ is $\\pm$1.63\\pp{}.}\n\\label{tab:tost_sensitivity}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{ccc}\n\\toprule\n\\textbf{Margin ($\\pm$\\pp{})} & \\textbf{$p$-value} & \\textbf{Equivalent ($\\alpha{=}0.05$)?} \\\\\n\\midrule\n1.0 & 0.871 & No \\\\\n1.5 & 0.113 & No \\\\\n\\textbf{1.63} & ${\\sim}$\\textbf{0.05} & \\textbf{Smallest margin} \\\\\n2.0 & 0.007 & Yes \\\\\n3.0 & $3.2{\\times}10^{-4}$ & Yes \\\\\n5.0 & $1.6{\\times}10^{-5}$ & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFigure~\\ref{fig:tost_sensitivity} (main text) visualises the margin--$p$-value relationship for both comparisons.\n\nThe minimum equivalence margin is $\\pm$1.63\\pp{}, 0.37\\pp{} below our pre-specified $\\pm$2\\pp{} threshold. The $\\pm$2\\pp{} threshold was set based on deployment relevance rather than observed data: at function-level accuracy (85--88\\%), a 2\\pp{} per-test difference corresponds to ${\\sim}$38 additional errors across 1,890 tests (${\\sim}$2--3 problems out of 114), comparable in magnitude to between-seed standard deviation (0.37--0.97\\pp{}) and checkpoint selection noise ($<$1\\pp{}). Differences within this range do not reliably distinguish formulations from training noise in pipeline selection decisions. For \\cls{}--\\traj{}, the TOST at $\\pm$2\\pp{} yields $p{=}0.025$, nominally significant but not surviving Holm-Bonferroni correction at $k{=}5$ (adjusted $p{=}0.075$; Table~\\ref{tab:holm}). The one-sided decomposition reveals the binding constraint: $p_{\\text{upper}}{=}0.005$ ($\\Delta < {+}2$\\pp{} is well-confirmed) while $p_{\\text{lower}}{=}0.025$ ($\\Delta > {-}2$\\pp{}) limits the overall TOST, consistent with \\cls{} having mildly higher accuracy.\n\n\\paragraph{Robustness: seed-level vs.\\ clustered bootstrap TOST.}\nThe primary TOST $p$-values use seed-level paired analysis (df${=}$4), treating each training seed as the unit of replication (\\S\\ref{sec:setup}). Under problem-level clustered bootstrap (resampling 114 problem clusters, 10K iterations), the \\cls{}--\\traj{} raw TOST $p$ decreases to ${\\sim}$0.007 (Holm-adjusted $p{\\approx}0.021$), which would confirm equivalence. We report the more conservative seed-level result ($p{=}0.025$, adjusted $p{=}0.075$) as primary, since training seeds are the true unit of replication; problem-level bootstrap pools within-seed observations and may understate between-seed uncertainty. For \\cls{}--\\cwm{}, both methods confirm equivalence ($p \\leq 0.010$), so the choice does not affect conclusions.\n\n\\subsection{Bayesian ROPE Analysis}\n\\label{app:bayesian_rope}\nTo complement the frequentist TOST, we conduct a Bayesian equivalence analysis using a paired $t$-test with Jeffreys prior~\\cite{kruschke2013bayesian,kruschke2018rejecting}. The marginal posterior for the mean accuracy difference follows a $t$-distribution with $n{-}1$ degrees of freedom. For \\cls{}--\\cwm{}, the posterior probability within the $\\pm$2\\pp{} ROPE is $P(\\text{ROPE}) = 0.975$, and the 95\\% highest density interval (HDI $= [{+}0.10, {+}2.00]$\\,pp) falls entirely inside the ROPE, confirming equivalence under both continuous and HDI-based decision criteria. For \\cls{}--\\traj{} at per-test level, $P(\\text{ROPE}) = 0.542$ (inconclusive; 95\\% HDI $= [{+}0.35, {+}3.52]$\\,pp extends beyond the ROPE), consistent with the TOST inconclusive result after Holm correction ($p_{\\text{adj}} = 0.075$). At variant level, \\cls{}--\\traj{} equivalence is supported by the Bayesian criterion ($P(\\text{ROPE}) = 0.970$, HDI $= [{-}2.00, {+}1.03]$\\,pp), but the frequentist TOST remains inconclusive after Holm-Bonferroni correction ($p_{\\text{adj}} = 0.075$; Table~\\ref{tab:holm}). This discrepancy reflects differing treatments of multiplicity: Bayesian ROPE evaluates each comparison independently, while Holm correction penalizes across all $k{=}5$ primary tests. For \\cls{}--\\cwm{}, both frameworks agree (TOST $p_{\\text{adj}}{=}0.028$, $P(\\text{ROPE}){=}0.975$); for \\cls{}--\\traj{} per-test, both are inconclusive. We conservatively follow the Holm-corrected TOST in the main text and report \\cls{}--\\traj{} equivalence as inconclusive.\n\n\\paragraph{14B scaling evidence.} At 14B (3 seeds), the \\cls{}--\\cwm{} gap narrows to 0.43\\pp{} and the \\cls{}--\\traj{} gap to 1.07\\pp{}, both within the $\\pm$2\\pp{} margin. Seed-level TOST (df${=}$2) is inconclusive for equivalence in both pairs ($p{=}0.076$ for \\cls{}--\\cwm{}, $p{=}0.187$ for \\cls{}--\\traj{}), reflecting the severe power limitation of 3-seed comparisons (power ${\\sim}$0.08 at $\\pm$2\\pp{} margin with df${=}$2). Bayesian ROPE provides moderate support: $P(\\text{ROPE}){=}0.887$ for \\cls{}--\\cwm{} and $P(\\text{ROPE}){=}0.780$ for \\cls{}--\\traj{}. Under problem-level clustered bootstrap, both comparisons reach significance ($p{=}0.0006$ and $p{=}0.043$ respectively), but this analysis treats within-seed observations as exchangeable, potentially understating between-seed uncertainty. The monotonic gap reduction (3.11\\pp{} at 4B $\\to$ 2.24\\pp{} at 8B $\\to$ 1.07\\pp{} at 14B) favors a capacity-dependent convergence interpretation, though formal confirmation at seed level requires more training seeds.\n\n\n\\section{Variant-Level Effect Sizes}\n\\label{app:power}\n\nTable~\\ref{tab:variant_power} reports variant-level bootstrap confidence intervals for the repo-level formulation comparisons ($n{=}48$ variants). Following Hoenig and Heisey~\\cite{hoenig2001}, we report minimum detectable effect (MDE) rather than post-hoc observed power.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Variant-level bootstrap analysis ($n{=}48$). \\cls{}--\\cwm{} uses paired bootstrap (same variants, same seed); \\cls{}--\\traj{} uses unpaired bootstrap (per-variant \\traj{} predictions not archived for pairing). MDE at $n{=}48$: ${\\sim}$25\\pp{}.}\n\\label{tab:variant_power}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Comparison} & \\textbf{Config} & \\textbf{$\\Delta$ (\\pp{})} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{\\cls{} vs.\\ \\cwm{} (paired)}} \\\\\n& Qwen3-8B & +29.17 & [10.42, 47.92] & 0.003 \\\\\n& DeepSeek-6.7B & +35.42 & [18.75, 50.05] & ${<}$0.001 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{\\cls{} vs.\\ \\traj{} (unpaired)}} \\\\\n& Qwen3-4B & $-$4.17 & wide & 0.740 \\\\\n& Qwen3-8B & +8.33 & wide & 0.385 \\\\\n& DeepSeek-6.7B & 0.00 & wide & 1.000 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAt $n{=}48$, the MDE is ${\\sim}$25\\pp{}. The \\cls{}--\\cwm{} gap (29--35\\pp{}) exceeds this threshold, confirming that $n{=}48$ is sufficient to detect the observed divergence. The \\cls{}--\\traj{} gaps ($<$10\\pp{}) fall well below the MDE: any true difference is too small to detect at this sample size, consistent with the function-level TOST equivalence (\\S\\ref{sec:equivalence}).\n\nThe \\cls{}--\\traj{} unpaired bootstrap produces wider confidence intervals than paired analysis would; \\traj{} per-variant predictions were not archived in a format that permits pairing. The \\cls{}--\\cwm{} paired comparison uses \\cls{} s123 vs.\\ \\cwm{} s42 (different seeds), but the CI lower bound of 10.42\\pp{} far exceeds the seed noise observed in function-level experiments ($<$2\\pp{}).\n\n\n\\section{Multiple Comparison Correction}\n\\label{app:holm}\n\nTable~\\ref{tab:holm} (main text) applies Holm-Bonferroni correction~\\cite{holm1979} to the five primary statistical comparisons across this study ($k{=}5$, family-wise $\\alpha{=}0.05$).\n\nThe two core claims survive correction: the repo-level \\cls{}--\\cwm{} divergence (adjusted $p{=}0.015$) and function-level \\cls{}--\\cwm{} equivalence (adjusted $p{=}0.028$). The function-level \\cls{}--\\traj{} equivalence does not survive correction (adjusted $p{=}0.075$). Under problem-level clustered bootstrap, the raw TOST $p$ decreases to ${\\sim}$0.007 (adjusted $p{\\approx}0.021$), which would confirm equivalence; we report the more conservative seed-level result ($p{=}0.025$) as primary, since training seeds are the true unit of replication.\n\n\\section{Mixed-Effects Regression}\n\\label{app:interaction}\n\nWe fit mixed-effects linear probability models (LPM) with heteroskedasticity-robust standard errors (HC1) to test the formulation$\\times$complexity interaction formally~\\cite{moulton1990}. We choose LPM because coefficients are directly interpretable as probability differences (percentage points), consistent with the reporting units in the main text; at these sample sizes ($n{\\approx}56$K cross-complexity, repo-level pooled cross-model) and base rate range (0.6--0.9), LPM and logistic regression yield concordant conclusions for all primary effects~\\cite{angrist2009mostly} (confirmed below).\n\n\\paragraph{Cross-complexity model (DeepSeek-Coder).} \\texttt{correct $\\sim$ formulation $\\times$ complexity + (1|problem\\_id)}, $n{=}56{,}480$ observations (\\cls{} + \\cwm{} $\\times$ function + repo), 139 problem clusters. The \\cwm{} main effect at function level is non-significant ($\\hat{\\beta}{=}-0.002$, $z{=}-0.25$, $p{=}0.805$); the \\cwm{}$\\times$repo interaction is highly significant ($\\hat{\\beta}{=}-0.219$, $z{=}-23.7$, $p{<}0.001$). \\cwm{} and \\cls{} are statistically indistinguishable at function level ($\\Delta{=}-0.2$\\pp{}, $p{=}0.805$) but diverge by 22\\pp{} at repo level, confirming the complexity-dependent divergence is not an artifact of aggregation.\n\n\\paragraph{Repo-level cross-model model.} \\texttt{correct $\\sim$ formulation $\\times$ model + (1|problem\\_id)}, both model families, repo level only. \\cwm{} deficit: $\\hat{\\beta}{=}-0.22$ ($-$22\\pp{}, $z{=}-64.4$, $p{<}0.001$). Model effect: +1.1\\pp{} for Qwen3 ($z{=}3.1$, $p{=}0.002$ in LPM; not significant under GEE, $p{=}0.449$). Formulation$\\times$model interaction: +1.6\\pp{} less \\cwm{} degradation on Qwen3 ($z{=}2.8$, $p{=}0.006$ in LPM; not significant under GEE, $p{=}0.860$). Formulation dominates the predictable variance; model identity is directionally positive but specification-dependent. The 25-cluster random intercept structure limits effective degrees of freedom for the random effects; inferences on fixed effects (formulation, complexity) are robust as they pool across the full observation count.\n\n\\paragraph{Logistic regression robustness check.} To verify that LPM conclusions are not artifacts of the linear link function, we fit GEE logistic regression (binomial family, exchangeable working correlation, robust sandwich standard errors) to the same data. For the cross-complexity model, the \\cwm{} main effect at function level has OR$=$0.98 (95\\% CI [0.86, 1.12], $p{=}0.771$) and the \\cwm{}$\\times$repo interaction has OR$=$0.31 ([0.15, 0.65], $p{=}0.002$). Average marginal effects are $-$0.2\\pp{} (function) and $-$21.6\\pp{} (repo), matching LPM coefficients within 0.3\\pp{}. For the cross-model model, the \\cwm{} deficit has OR$=$0.30 ([0.15, 0.63], $p{=}0.001$, AME$=$\\,$-$21.1\\pp{}). Direction, magnitude, and significance of all primary effects are concordant between LPM and logistic regression; minor discrepancies in secondary effects (model identity, formulation$\\times$model interaction: $p{=}0.449$ and $p{=}0.860$ under GEE vs.\\ $p{=}0.002$ and $p{=}0.006$ under LPM) reflect the GEE's more conservative cluster-robust inference with $k{=}25$ clusters. The discrepancy in secondary effects reflects cluster count: the cross-complexity model ($k{=}139$) yields reliable sandwich SEs, while the cross-model model ($k{=}25$) falls below the $k{\\geq}40$ threshold recommended for stable cluster-robust inference~\\cite{cameron2008bootstrap}.\n\n\\section{CWM Parseable Bias Analysis}\n\\label{app:parseable_bias}\n\nFigure~\\ref{fig:cwm_unparseable} (main text) summarises the unparseable rate contrast across complexity levels.\n\nThe default-to-pass assignment for unparseable \\cwm{} outputs is not random with respect to instance difficulty. Unparseable instances have significantly higher pass rates than parseable ones (74.6\\% vs.\\ 68.3\\%, $\\chi^2$ $p = 5.9 \\times 10^{-10}$), and \\cls{} models achieve higher accuracy on unparseable instances (86.4\\% vs.\\ 79.1\\%, $p = 3.3 \\times 10^{-18}$). This indicates that \\cwm{}'s parsing failures concentrate on simpler, pass-heavy instances where the majority-class default happens to be correct more often. Cross-model Jaccard overlap of unparseable instance sets is 0.46, confirming this pattern is instance-driven (specific inputs consistently cause parsing failure across models) rather than stochastic. The net effect is that \\cwm{}'s reported accuracy is inflated by default-correct assignments on easy instances, while its effective discriminative accuracy on harder instances is substantially lower than the aggregate figure suggests.\n\n\n\\section{Threats to Validity (Full Analysis)}\n\\label{app:threats}\n\nWe identify five potential confounds and assess their impact on our conclusions.\n\n\\paragraph{Checkpoint selection.} Val-based selection is unavailable for runs with NaN validation loss (DeepSeek \\cwm{} repo-level runs, DeepSeek \\cls{} s123), which default to the final epoch checkpoint. A checkpoint ablation on Qwen3-8B \\cls{} s42 quantifies this confound: epoch~1 (ckpt-2200) achieves 85.34\\%, val-selected (ckpt-3600) 84.48\\%, and final epoch (ckpt-6633) 85.29\\%, a $<$1\\pp{} range. The val-selected checkpoint is the lowest, indicating no upward bias from checkpoint selection. The Qwen3-8B \\traj{} comparison (epoch 2: 72.92\\% vs.\\ epoch 3: 70.83\\%) shows a slightly larger ${\\sim}$2\\pp{} shift. For \\cwm{}, the convergence analysis (Appendix~\\ref{app:cwm_convergence}) shows eval loss at the final epoch is 1.8$\\times$ its minimum; however, early-stopped checkpoints retain high unparseable rates, leaving the qualitative ranking unchanged.\n\n\\paragraph{\\cwm{} convergence analysis.}\n\\label{app:cwm_convergence}\nQwen3-8B \\cwm{} repo-level eval loss reaches its minimum within ${\\sim}$5\\% of training (step 300--400 of 6{,}633) and increases monotonically thereafter, with no plateau or recovery (Table~\\ref{tab:cwm_convergence}). This pattern is consistent across all three seeds, confirming systematic overfitting to trace generation rather than stochastic variation. The final-epoch eval loss is ${\\sim}$1.8$\\times$ the optimal value. By contrast, function-level \\cwm{} achieves \\cls{}-equivalent accuracy (TOST $p{=}0.007$) with the same training recipe, indicating that the overfit is specific to repo-level output complexity. Cross-model validation: a DeepSeek-Coder early-stopped checkpoint (s123, epoch~1) achieves 75.45\\% versus 57.31\\% at epoch~3 (s123; +18.14\\pp{}), but retains 66.4\\% unparseable rate, confirming that format collapse emerges early and is not a late-training artifact. No epoch-level checkpoint is available for Qwen3 CWM (only step-level checkpoints at steps 300/400 and late steps ${\\geq}$5800; continuous epoch checkpointing was not enabled for this training run). The convergence analysis (Table~\\ref{tab:cwm_convergence}) shows eval loss minimum at step 300--400 across all three Qwen3 seeds, consistent with DeepSeek-Coder's epoch-1 improvement, providing cross-model evidence that the overtraining pattern generalizes. An early checkpoint (step 400, ${\\sim}$6.5\\% of training, s42) yields 65.17\\% repo-level accuracy with 63.7\\% unparseable rate, comparable to or below final-epoch performance (66.93--67.33\\% accuracy, 60.4--63.9\\% unparseable; s123/s456 at step 6633). This rules out late-training format degradation: collapse is present from early training, and the optimal eval-loss checkpoint does not recover repo-level accuracy. A later checkpoint (step 6100, s42, seq8192) achieves 69.50\\% test accuracy despite substantially higher validation loss than val-best ckpt-400 (64.36\\%), suggesting that validation loss may not be a reliable proxy for test-set performance in \\cwm{} repo-level evaluation.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{\\cwm{} repo-level eval loss across training (Qwen3-8B, 3 seeds). Minimum is reached at step 300--400 (${\\sim}$5\\% of training); subsequent training monotonically increases loss.}\n\\label{tab:cwm_convergence}\n\\begin{tabular}{lccc}\n\\toprule\nStep & s42 & s123 & s456 \\\\\n\\midrule\n300 & 0.291 & \\textbf{0.288} & \\textbf{0.277} \\\\\n400 & \\textbf{0.286} & 0.306 & 0.283 \\\\\n1000 & 0.333 & 0.336 & 0.351 \\\\\n3000 & 0.445 & 0.453 & 0.435 \\\\\n6600 & 0.521 & 0.517 & 0.507 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Evaluation sequence length.} \\cwm{} accuracy varies by ${\\sim}$9\\pp{} across evaluation sequence lengths for the same checkpoint (seq2048: ${\\sim}$65\\% vs.\\ seq4096: ${\\sim}$56\\%), driven by unparseable-rate differences that propagate through majority-class default assignment. \\cls{} is invariant to this parameter. Cross-model \\cwm{} comparisons use different eval lengths (Qwen3: 8192, DeepSeek: 4096) and are not directly comparable in absolute terms. A matched-sequence evaluation shows ${\\sim}$1.5\\pp{} difference for \\cls{} (Appendix~\\ref{app:ablations}), insufficient to explain the 18--26\\pp{} gap. Furthermore, increasing Qwen3-8B \\cwm{} evaluation from seq4096 to seq8192 \\emph{raises} the unparseable rate (63.7\\%$\\to$73.8\\%) while changing accuracy by only 0.81\\pp{} (64.36\\%$\\to$65.17\\%); giving the model more generation budget worsens format compliance rather than improving it, confirming that format collapse is a structural bottleneck rather than a truncation artifact. Practitioners must standardize evaluation sequence length for generation-based formulations.\n\n\\paragraph{Preprocessing.} DeepSeek \\cls{} accuracy ranges from 82.61\\% (s42, drop preprocessing) to 74.93\\% (s123, truncate preprocessing), a 7.68\\pp{} spread that conflates preprocessing strategy, checkpoint selection method, and seed. The two strategies produce different effective training sets (67,343 vs.\\ 70,748 samples) and different checkpoint selection regimes. The qualitative ranking \\cls{} $>$ \\cwm{} holds under both strategies (Table~\\ref{tab:taxonomy}).\n\n\\paragraph{\\traj{} training regime.} \\traj{} uses a different training configuration: smaller training set (${\\sim}$400 repo-level variants vs.\\ ${\\sim}$70K per-test instances), higher learning rate ($2{\\times}10^{-4}$ vs.\\ $5{\\times}10^{-5}$), and variant-level labels. This asymmetry is inherent to the formulation (trajectory-level labels are only available at variant granularity), but precludes training-data-controlled comparison at repo level. The downsample ablation confirms the \\cls{} formulation advantage persists at matched data volume (80.74\\% vs.\\ 72.92\\%; Appendix~\\ref{app:downsample}), though it controls for training volume but not label granularity (per-test vs.\\ variant-level). Crucially, \\traj{} achieves statistical equivalence with \\cls{} at function level (${\\leq}$1.3\\pp{}, \\S\\ref{sec:func_results}), demonstrating the formulation itself is viable; the repo-level gap attribution remains uncertain: data volume (${\\sim}$400 variants vs.\\ ${\\sim}$70K per-test instances) and label granularity (variant-level vs.\\ per-test) are both plausible confounds that cannot be separately controlled.\n\n\\paragraph{\\cwm{} scale and pretraining.} Our \\cwm{} baseline uses 4--8B LoRA fine-tuning without execution trace pretraining. The original Code World Model~\\cite{meta2025cwm} uses 32B parameters with mid-training on execution traces, a fundamentally different training regime. At larger scale or with execution-trace pretraining, the generation bottleneck observed here may diminish: larger models produce more coherent long-form outputs, and execution trace exposure may improve output format compliance. This is the primary limitation: all repo-level \\cwm{} conclusions are conditional on the ${\\leq}$8B LoRA regime.\n\nDespite these confounds, the repo-level \\cls{}--\\cwm{} gap (18--26\\pp{}) exceeds any single assessed confound. Even under worst-case compounding (${\\sim}$11.5\\pp{}), the gap retains ${\\geq}$7.5\\pp{} margin; confounds predominantly disadvantage \\cwm{}. However, correlated confounds and limited seed coverage mean definitive causal attribution requires multi-seed replication. At $n{=}48$, the minimum detectable effect (MDE) is ${\\sim}$25\\pp{}~\\cite{hoenig2001}; the \\cls{}--\\cwm{} gap (29--35\\pp{}) exceeds this threshold, while the \\cls{}--\\traj{} gap ($<$10\\pp{}) falls below it, consistent with our TOST equivalence finding. Holm-Bonferroni correction across the five primary comparisons ($k{=}5$; Table~\\ref{tab:holm}) confirms the \\cls{}--\\cwm{} gap (adjusted $p{=}0.015$) and function-level \\cls{}--\\cwm{} equivalence (adjusted $p{=}0.028$); function-level \\cls{}--\\traj{} equivalence does not survive correction (adjusted $p{=}0.075$), nor does the repo-level \\cwm{}--\\traj{} comparison (adjusted $p{=}0.078$). The consistent direction across both model families and all tested configurations supports a formulation-level explanation, though definitive causal attribution requires future experiments addressing each confound individually.\n\n\n\\paragraph{Extended validity discussion.}\n\\label{app:limitations}\nThe same-size 4B comparison uses a single seed; \\cls{} 4B seed 123 (val-best ckpt-800) achieves only 75.33\\% test accuracy (+2.4\\pp{} above majority baseline); val-best selection at an early checkpoint (step 800) amplifies the val-test distribution shift observed across all configurations. The \\cwm{} 8B comparison uses 3 seeds per model. The validation and test sets have zero problem overlap but differ in mutation type composition (Table~\\ref{tab:mutation_distribution}): \\texttt{operator\\_swap} shifts from 19.1\\% (val) to 34.3\\% (test), the largest single-type distribution mismatch (+15.2\\pp{}). All repo-level results use val-selected checkpoints, and checkpoint selection variance could contribute to observed differences. Our training data is synthetically constructed from mutation operators rather than real developer patches. While mutation testing literature establishes that mutants are reasonable proxies for real faults in test effectiveness studies~\\cite{andrews2005mutation,just2014mutants}, these findings concern mutation \\emph{adequacy} (whether tests that kill mutants also detect real faults), not whether verifiers trained on mutants transfer to real patches. However, the coupling effect underlying these results supports \\emph{relative ranking} validity: a domain shift from synthetic mutations to real bugs may affect absolute accuracy levels, but our core finding (that formulation choice matters at repo level but not function level) concerns relative performance ordering, which is expected to be preserved under distributional shifts that affect all formulations equally. The synthetic-to-real transfer gap for absolute accuracy remains untested. The \\traj{} training configuration differs from \\cls{}/\\cwm{}: smaller training set (${\\sim}$400 vs.\\ ${\\sim}$70K instances), different learning rate ($2{\\times}10^{-4}$ vs.\\ $5{\\times}10^{-5}$), and variant-level evaluation ($n{=}48$ vs.\\ per-test $n{=}9{,}784$). The function-level \\cls{}--\\traj{} TOST equivalence ($p = 0.025$, seed-level paired, $\\pm$2\\pp{}) is computed on 523 matched variant-level instances across 5 seeds; 2 of 5 seeds use NF4 quantization. Restricting to three bfloat16 seeds yields a comparable mean gap ($-$0.45\\pp{}) but wider confidence interval (df${=}$2); the TOST $p$-value increases to 0.128, which reflects reduced statistical power rather than a shift in the point estimate. The NF4 seeds contribute precision (narrowing the CI) without shifting the mean, consistent with precision being comparable across both quantization levels at function level. Repo-level \\cls{}--\\traj{} comparison should be interpreted with caution due to configuration and granularity differences.\n\n\\paragraph{Domain contrast with generative verification in math reasoning.}\nGenRM~\\cite{hosseini2025genrm} demonstrates that generative verifiers outperform discriminative ones for math reasoning. Our results reveal a domain-specific divergence: in code repair verification, the generative formulation (\\cwm{}) does not outperform the discriminative one (\\cls{}), and degrades sharply at repository level. The key difference is output space structure: math reasoning generates natural-language solution traces with flexible formatting, whereas code execution output requires exact syntactic compliance (specific variable values, error messages, stack traces). This structural constraint makes format collapse, absent in math verification, the dominant failure mode for code \\cwm{} at repo level (53--74\\% unparseable). The domain contrast suggests that the generative verification advantage is contingent on output space complexity rather than being a universal property of verifier architecture.\n\n\\paragraph{Use of AI assistants.}\n\\label{app:ai-assistants}\nClaude (Anthropic) assisted with code, writing, and literature review.\n",
      "numLines": 562,
      "startLine": 1,
      "totalLines": 562
    }
  },
  "sourceToolAssistantUUID": "771bad3f-f358-4157-b30e-b4eb7b70497e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 42 · 2026-05-25T21:14:50.616Z_

```json
{
  "parentUuid": "ed2fa61f-bccf-42c9-98ff-40fb378f5a67",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "af0b7274-ee46-4271-8f27-2068874703b1",
  "timestamp": "2026-05-25T21:14:50.616Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: exec-sim-repair-verifier - 论文路径: projects/exec-sim-repair-verifier/docs/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: ARR (Main/Findings unified) - 截止日期: 2026-05-25 -…",
  "leafUuid": "af0b7274-ee46-4271-8f27-2068874703b1",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper submission for EMNLP 2026",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e"
}
```

---

### Assistant

_source line 45 · 2026-05-25T21:14:55.401Z_

<details><summary>Logged reasoning block</summary>

```text
I've now read the full paper. Let me proceed with the review workflow:

1. Step 0: Search for EMNLP 2026 venue requirements (must use web search, not training knowledge)
2. Check external review config
3. Then proceed with reviewer assignment

Let me search for EMNLP 2026 CFP and check the project config for external review settings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af0b7274-ee46-4271-8f27-2068874703b1",
  "isSidechain": false,
  "requestId": "req_011CbPykTxH4c61yUDgNDGFM",
  "type": "assistant",
  "uuid": "6eef88e3-d69b-469a-ac14-cacf05f29f79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A6vjiULBm8mFZXPC4DSeR5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 36182,
      "cache_read_input_tokens": 38115,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36182,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 345,
          "cache_read_input_tokens": 38115,
          "cache_creation_input_tokens": 36182,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36182
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

_source line 46 · 2026-05-25T21:14:56.540Z_

论文已完整读取。现在搜索 EMNLP 2026 CFP 确认 venue 要求。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6eef88e3-d69b-469a-ac14-cacf05f29f79",
  "isSidechain": false,
  "requestId": "req_011CbPykTxH4c61yUDgNDGFM",
  "type": "assistant",
  "uuid": "a7eb20de-760f-45c4-a9bd-7bc3459ebb8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A6vjiULBm8mFZXPC4DSeR5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 36182,
      "cache_read_input_tokens": 38115,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36182,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 345,
          "cache_read_input_tokens": 38115,
          "cache_creation_input_tokens": 36182,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36182
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

_source line 47 · 2026-05-25T21:14:57.975Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WSpE1vRm7r1yddGd9KxieN`</summary>

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
  "parentUuid": "a7eb20de-760f-45c4-a9bd-7bc3459ebb8a",
  "isSidechain": false,
  "requestId": "req_011CbPykTxH4c61yUDgNDGFM",
  "type": "assistant",
  "uuid": "084e1cd2-1abd-452d-9562-0ddcb18b1c56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A6vjiULBm8mFZXPC4DSeR5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 36182,
      "cache_read_input_tokens": 38115,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36182,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 345,
          "cache_read_input_tokens": 38115,
          "cache_creation_input_tokens": 36182,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36182
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

_source line 48 · 2026-05-25T21:14:58.971Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Dw9osvi2PCsTWvU8H8UZNa`</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "paper_checklist.yaml",
  "max_chars": 3000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "084e1cd2-1abd-452d-9562-0ddcb18b1c56",
  "isSidechain": false,
  "requestId": "req_011CbPykTxH4c61yUDgNDGFM",
  "type": "assistant",
  "uuid": "4ac080a6-2e9a-4908-b02f-bd2f685d4508",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A6vjiULBm8mFZXPC4DSeR5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 36182,
      "cache_read_input_tokens": 38115,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36182,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 345,
          "cache_read_input_tokens": 38115,
          "cache_creation_input_tokens": 36182,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36182
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

_source line 49 · 2026-05-25T21:15:04.616Z_

<details><summary>↩ Tool result · `toolu_01WSpE1vRm7r1yddGd9KxieN`</summary>

```text
Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"}]

Based on the search results, here are the key EMNLP 2026 call for papers submission guidelines related to ARR:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## Important ARR Policy

Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026.

## General Requirements

All accepted papers must be presented at the conference to appear in the proceedings. The conference will include both in-person and virtual presentation options. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

Following the ACL and ARR policies, there is no anonymity period requirement.

For more detailed information, you can visit the official EMNLP 2026 Call for Main Conference Papers at https://2026.emnlp.org/calls/main_conference_papers/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "084e1cd2-1abd-452d-9562-0ddcb18b1c56",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "f38a67ad-9aaa-4abe-bf45-d6b445f5d505",
  "toolUseResult": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TxEVxo9CyssAgAQwQptamz",
        "content": [
          {
            "title": "Call for Main Conference Papers - EMNLP 2026",
            "url": "https://2026.emnlp.org/calls/main_conference_papers/"
          },
          {
            "title": "Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"
          },
          {
            "title": "*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"
          },
          {
            "title": "Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"
          },
          {
            "title": "EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"
          },
          {
            "title": "EACL 2026: First Call for Papers | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"
          }
        ]
      },
      "Based on the search results, here are the key EMNLP 2026 call for papers submission guidelines related to ARR:\n\n## Paper Types and Scope\n\nEMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.\n\n## Important ARR Policy\n\nGiven that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026.\n\n## General Requirements\n\nAll accepted papers must be presented at the conference to appear in the proceedings. The conference will include both in-person and virtual presentation options. All deadlines are 11:59PM UTC-12:00 (\"anywhere on Earth\").\n\nFollowing the ACL and ARR policies, there is no anonymity period requirement.\n\nFor more detailed information, you can visit the official EMNLP 2026 Call for Main Conference Papers at https://2026.emnlp.org/calls/main_conference_papers/"
    ],
    "durationSeconds": 6.636241707000001
  },
  "sourceToolAssistantUUID": "084e1cd2-1abd-452d-9562-0ddcb18b1c56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-25T21:15:04.634Z_

<details><summary>↩ Tool result · `toolu_01Dw9osvi2PCsTWvU8H8UZNa`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'exec-sim-repair-verifier'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ac080a6-2e9a-4908-b02f-bd2f685d4508",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "a1a756af-5125-45d6-a476-1ad5e8c53612",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"No paper_checklist.yaml found for 'exec-sim-repair-verifier'.\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'exec-sim-repair-verifier'.\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "4ac080a6-2e9a-4908-b02f-bd2f685d4508",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-25T21:15:07.513Z_

<details><summary>Logged reasoning block</summary>

```text
Let me get more specific information about EMNLP 2026 submission guidelines - page limits, formatting, etc. Let me also check the project config for external review settings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1a756af-5125-45d6-a476-1ad5e8c53612",
  "isSidechain": false,
  "requestId": "req_011CbPymVngtXCZ7traFEqFN",
  "type": "assistant",
  "uuid": "b5926112-7e69-44f9-8901-dd0619e12f5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0134PpzW9aLpNNSGdsp7scBH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1207,
      "cache_read_input_tokens": 74297,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1207,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 74297,
          "cache_creation_input_tokens": 1207,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1207
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

_source line 52 · 2026-05-25T21:15:08.511Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UrDXB4VPhvow8tSvG9ZXmv`</summary>

```json
{
  "query": "EMNLP 2026 page limit format template double blind anonymity ARR submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5926112-7e69-44f9-8901-dd0619e12f5e",
  "isSidechain": false,
  "requestId": "req_011CbPymVngtXCZ7traFEqFN",
  "type": "assistant",
  "uuid": "72b26601-d9a1-4342-93fb-2634bedbc8e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0134PpzW9aLpNNSGdsp7scBH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1207,
      "cache_read_input_tokens": 74297,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1207,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 74297,
          "cache_creation_input_tokens": 1207,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1207
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

_source line 53 · 2026-05-25T21:15:09.020Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Mqa662TftwdMko6E3UmKYg`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72b26601-d9a1-4342-93fb-2634bedbc8e5",
  "isSidechain": false,
  "requestId": "req_011CbPymVngtXCZ7traFEqFN",
  "type": "assistant",
  "uuid": "f7650e6d-dd96-4e32-b2eb-f13dce1691f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0134PpzW9aLpNNSGdsp7scBH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1207,
      "cache_read_input_tokens": 74297,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1207,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 74297,
          "cache_creation_input_tokens": 1207,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1207
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

_source line 54 · 2026-05-25T21:15:09.023Z_

<details><summary>↩ Tool result · `toolu_01Mqa662TftwdMko6E3UmKYg`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7650e6d-dd96-4e32-b2eb-f13dce1691f0",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "c5e4d195-1e60-4aac-8c89-bb247a5afde0",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 29
  },
  "sourceToolAssistantUUID": "f7650e6d-dd96-4e32-b2eb-f13dce1691f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-25T21:15:15.050Z_

<details><summary>↩ Tool result · `toolu_01UrDXB4VPhvow8tSvG9ZXmv`</summary>

```text
Web search results for query: "EMNLP 2026 page limit format template double blind anonymity ARR submission"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"ACL Policies for Review and Citation - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Policies_for_Review_and_Citation"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"}]

Based on the search results, here's the information about EMNLP 2026 submission requirements:

## Page Limits and Format

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences. EMNLP uses the ACL style files available at github.com/acl-org/acl-style-files.

## Double-Blind Review

The reviewing process will continue to be double-blind. Reviewers will not see authors, nor will authors see reviewers and reviews on ARR will not be made publicly visible.

## Anonymity Requirements

Papers must not include authors' names and affiliations. Furthermore, self-references that reveal the authors' identities, e.g., "We previously showed (Smith, 1991)…" must be avoided.

## Anonymity Period Policy

Following the ACL and ARR policies, there is no anonymity period requirement. However, the new policy incentivizes anonymous submissions by special paper awards and priority in acceptance decisions for borderline papers.

## ARR Submission

All submissions go through ACL Rolling Review (ARR), with the ARR submission deadline of May 25, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72b26601-d9a1-4342-93fb-2634bedbc8e5",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "14a7bd5b-e1a6-4034-b4f1-22ac54e4c697",
  "toolUseResult": {
    "query": "EMNLP 2026 page limit format template double blind anonymity ARR submission",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ha2FWswc7jpEnShXXh2Aue",
        "content": [
          {
            "title": "Call for Main Conference Papers - EMNLP 2026",
            "url": "https://2026.emnlp.org/calls/main_conference_papers/"
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
            "title": "Confs: 2026 Conference on Empirical Methods in Natural ...",
            "url": "https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"
          },
          {
            "title": "Submissions | Transactions of the Association for Computational Linguistics",
            "url": "https://transacl.org/index.php/tacl/about/submissions"
          },
          {
            "title": "ACL Policies for Review and Citation - Admin Wiki",
            "url": "https://www.aclweb.org/adminwiki/index.php/ACL_Policies_for_Review_and_Citation"
          },
          {
            "title": "EMNLP 2026 Conference | OpenReview",
            "url": "https://openreview.net/group?id=EMNLP%2F2026%2FConference"
          }
        ]
      },
      "Based on the search results, here's the information about EMNLP 2026 submission requirements:\n\n## Page Limits and Format\n\nThe format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences. EMNLP uses the ACL style files available at github.com/acl-org/acl-style-files.\n\n## Double-Blind Review\n\nThe reviewing process will continue to be double-blind. Reviewers will not see authors, nor will authors see reviewers and reviews on ARR will not be made publicly visible.\n\n## Anonymity Requirements\n\nPapers must not include authors' names and affiliations. Furthermore, self-references that reveal the authors' identities, e.g., \"We previously showed (Smith, 1991)…\" must be avoided.\n\n## Anonymity Period Policy\n\nFollowing the ACL and ARR policies, there is no anonymity period requirement. However, the new policy incentivizes anonymous submissions by special paper awards and priority in acceptance decisions for borderline papers.\n\n## ARR Submission\n\nAll submissions go through ACL Rolling Review (ARR), with the ARR submission deadline of May 25, 2026."
    ],
    "durationSeconds": 6.516841508999998
  },
  "sourceToolAssistantUUID": "72b26601-d9a1-4342-93fb-2634bedbc8e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-25T21:15:17.872Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the venue requirements. Let me also check the project config for external review settings. Let me read the project config to check external_review settings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14a7bd5b-e1a6-4034-b4f1-22ac54e4c697",
  "isSidechain": false,
  "requestId": "req_011CbPynGJ71Up5eQVyrxj2E",
  "type": "assistant",
  "uuid": "b0921e32-253b-4625-88fd-822040e1a0ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019E2LPQWnYXBSGTeAJSifMH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1324,
      "cache_read_input_tokens": 75504,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1324,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 135,
          "cache_read_input_tokens": 75504,
          "cache_creation_input_tokens": 1324,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1324
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

_source line 57 · 2026-05-25T21:15:18.742Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Pog6LTFFqkgW7qVFvnoFnc`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0921e32-253b-4625-88fd-822040e1a0ca",
  "isSidechain": false,
  "requestId": "req_011CbPynGJ71Up5eQVyrxj2E",
  "type": "assistant",
  "uuid": "060a3fcd-5336-4545-8e9a-7947101e2513",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019E2LPQWnYXBSGTeAJSifMH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1324,
      "cache_read_input_tokens": 75504,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1324,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 135,
          "cache_read_input_tokens": 75504,
          "cache_creation_input_tokens": 1324,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1324
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

_source line 58 · 2026-05-25T21:15:18.751Z_

<details><summary>↩ Tool result · `toolu_01Pog6LTFFqkgW7qVFvnoFnc`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "060a3fcd-5336-4545-8e9a-7947101e2513",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "46616044-c765-438f-911f-a3f1009d83d1",
  "toolUseResult": {
    "matches": [],
    "query": "select:mcp__agent-ml-research__read_local_file",
    "total_deferred_tools": 29
  },
  "sourceToolAssistantUUID": "060a3fcd-5336-4545-8e9a-7947101e2513",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-25T21:15:23.874Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01L5c1h8bb5QU5AtrsSPFwm9`</summary>

```json
{
  "pattern": "**/exec-sim-repair-verifier/**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46616044-c765-438f-911f-a3f1009d83d1",
  "isSidechain": false,
  "requestId": "req_011CbPynYNz8PHfcHdnUcZSy",
  "type": "assistant",
  "uuid": "e0cbdde8-f05e-4c76-8ce8-61aa56626471",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014gPUirUvBbezhyY5q7UyuT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 154,
      "cache_read_input_tokens": 76828,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 154,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 101,
          "cache_read_input_tokens": 76828,
          "cache_creation_input_tokens": 154,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 154
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

_source line 60 · 2026-05-25T21:15:23.925Z_

<details><summary>↩ Tool result · `toolu_01L5c1h8bb5QU5AtrsSPFwm9`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0cbdde8-f05e-4c76-8ce8-61aa56626471",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "e81e8a7e-067d-421e-87ef-b82e377604df",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 45,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "e0cbdde8-f05e-4c76-8ce8-61aa56626471",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-25T21:15:26.165Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018SbwaoBQqZLK7cBh5XW7fm`</summary>

```json
{
  "pattern": "**/exec-sim-repair-verifier/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e81e8a7e-067d-421e-87ef-b82e377604df",
  "isSidechain": false,
  "requestId": "req_011CbPynvHrgMuqcMUHJyjEk",
  "type": "assistant",
  "uuid": "c9f00c3e-3609-4b15-a520-764d7ab558d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKwRjSmmy2DSxe3GTHQVyu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 116,
      "cache_read_input_tokens": 76982,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 116,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 100,
          "cache_read_input_tokens": 76982,
          "cache_creation_input_tokens": 116,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 116
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

_source line 62 · 2026-05-25T21:15:26.207Z_

<details><summary>↩ Tool result · `toolu_018SbwaoBQqZLK7cBh5XW7fm`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/decisions.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9f00c3e-3609-4b15-a520-764d7ab558d2",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "c6bdb12d-d07c-4a73-b658-fc04218311ce",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/experiment_plan.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/literature_map.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/writing_plan.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/dream_registry.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/paper_provenance.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/mistakes.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/registry.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/decisions.yaml"
    ],
    "durationMs": 39,
    "numFiles": 8,
    "truncated": false
  },
  "sourceToolAssistantUUID": "c9f00c3e-3609-4b15-a520-764d7ab558d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 63_

```json
{
  "type": "last-prompt",
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: exec-sim-repair-verifier - 论文路径: projects/exec-sim-repair-verifier/docs/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: ARR (Main/Findings unified) - 截止日期: 2026-05-25 -…",
  "leafUuid": "c6bdb12d-d07c-4a73-b658-fc04218311ce",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e"
}
```

---

### Runtime record

_source line 64_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper submission for EMNLP 2026",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e"
}
```

---

### Tool call

_source line 65 · 2026-05-25T21:15:29.718Z_

<details open><summary>🔧 Tool call — Grep · `toolu_016nQV65eWfeg3ieuYVgWj5g`</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "glob": "*.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6bdb12d-d07c-4a73-b658-fc04218311ce",
  "isSidechain": false,
  "requestId": "req_011CbPyo64jJSnmrc1hefNUA",
  "type": "assistant",
  "uuid": "f0578a98-2326-40ff-9f46-70a3b54694af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKkjKKJgh4MBGeZm2qqWkT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 77098,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 401,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 130,
          "cache_read_input_tokens": 77098,
          "cache_creation_input_tokens": 401,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 401
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

_source line 66 · 2026-05-25T21:15:29.737Z_

<details><summary>↩ Tool result · `toolu_016nQV65eWfeg3ieuYVgWj5g`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0578a98-2326-40ff-9f46-70a3b54694af",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "9f8f2c90-bd6c-4128-a3ca-9ce8f754cbbf",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "f0578a98-2326-40ff-9f46-70a3b54694af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-25T21:15:32.983Z_

<details open><summary>🔧 Tool call — Grep · `toolu_0193KrUZMfh36HtrVFrqoDzz`</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "glob": "*.{yaml,yml,json,toml}",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f8f2c90-bd6c-4128-a3ca-9ce8f754cbbf",
  "isSidechain": false,
  "requestId": "req_011CbPyoMKkTKmkjMKkGsqhB",
  "type": "assistant",
  "uuid": "ee34ebf8-5db1-4c16-bde3-60bc06560100",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EZtwRmqBzb6mxpehSB4wf5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 145,
      "cache_read_input_tokens": 77499,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 145,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 77499,
          "cache_creation_input_tokens": 145,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 145
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

_source line 68 · 2026-05-25T21:15:33.073Z_

<details><summary>↩ Tool result · `toolu_0193KrUZMfh36HtrVFrqoDzz`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee34ebf8-5db1-4c16-bde3-60bc06560100",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "d47d447a-5ccc-401a-b998-359b27866a6e",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "ee34ebf8-5db1-4c16-bde3-60bc06560100",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 69 · 2026-05-25T21:15:33.076Z_

```json
{
  "parentUuid": "d47d447a-5ccc-401a-b998-359b27866a6e",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6a3881d4-29d5-4242-aa1d-4e89e5ab18b1",
  "timestamp": "2026-05-25T21:15:33.076Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 70 · 2026-05-25T21:16:00.834Z_

<details><summary>Logged reasoning block</summary>

```text
External review is not configured (no `external_review.paperreview_ai.enabled` found in project config). So I'll skip Step 0.6.

Now let me also check if there's an existing review_issues.yaml file.

Let me also check the PDF exists.

Now let me summarize what I know:

**Venue requirements (EMNLP 2026 via ARR):**
- Long paper: 8-page limit for main text
- Short paper: 4-page limit
- Unlimited references
- ACL style template
- Double-blind review
- No anonymity period requirement


- ARR submission deadline: May 25, 2026 (today!)
- Main/Findings unified (not separate tracks)

**Paper status:**
- Title: "A Systematic Comparison of Execution-Free Verification Formulations for Code Repair"
- Authors: Anonymous (correct for double-blind)
- Uses ACL review style (`\usepackage[review]{acl}`)
- Has abstract, intro, related work, method, experiments, conclusion, limitations, appendix
- References via `references.bib`

Now I'm checking the review arrangement for EMNLP... level → 2 Reviewers:
- Reviewer 1: 方法严谨性 + 实验设计
- Reviewer 2: 新颖性 + 完整性 + 写作质量

Now let me check:
1. Review issues tracker
2. PDF exists
3. Then dispatch visual check + assign reviewers

Let me proceed with the review. First let me check word count of abstract (should be ≤200 words per EMNLP rules).

The abstract describes a systematic comparison of three different approaches to execution-free verification in LLM-based program repair, testing across multiple model families and complexity levels. The key finding is that code complexity determines whether classification and generation methods perform equivalently—they do for shorter outputs but diverge significantly when dealing with longer, more structured code at the repository level. The analysis includes failure modes and error patterns to guide practitioners on which formulation to use, with open questions remaining about whether capacity differences affect the repository-level performance gap.

I'm checking the word count and verifying the PDF location, then I'll proceed with assigning reviewers based on their expertise areas.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a3881d4-29d5-4242-aa1d-4e89e5ab18b1",
  "isSidechain": false,
  "requestId": "req_011CbPyobMcCiRXTEiXrdwur",
  "type": "assistant",
  "uuid": "aa8c9feb-4a7e-4b68-b01e-db9b63eba4b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T63icej2nYZ7h5acEFp3yF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 256,
      "cache_read_input_tokens": 77644,
      "output_tokens": 1209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 256,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1209,
          "cache_read_input_tokens": 77644,
          "cache_creation_input_tokens": 256,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 256
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

_source line 71 · 2026-05-25T21:16:00.836Z_

外部审稿未配置，跳过 Step 0.6。现在检查现有 issue tracker 和 PDF，然后开始编排 Reviewer。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa8c9feb-4a7e-4b68-b01e-db9b63eba4b0",
  "isSidechain": false,
  "requestId": "req_011CbPyobMcCiRXTEiXrdwur",
  "type": "assistant",
  "uuid": "0ac50029-7f4b-4f59-a670-c4e0029165d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T63icej2nYZ7h5acEFp3yF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 256,
      "cache_read_input_tokens": 77644,
      "output_tokens": 1209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 256,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1209,
          "cache_read_input_tokens": 77644,
          "cache_creation_input_tokens": 256,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 256
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

_source line 72 · 2026-05-25T21:16:01.857Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01LWRv4Bc6vFyG1N9boJuM1A`</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ac50029-7f4b-4f59-a670-c4e0029165d1",
  "isSidechain": false,
  "requestId": "req_011CbPyobMcCiRXTEiXrdwur",
  "type": "assistant",
  "uuid": "d0db9de0-e574-476a-9755-11c74b471b56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T63icej2nYZ7h5acEFp3yF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 256,
      "cache_read_input_tokens": 77644,
      "output_tokens": 1209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 256,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1209,
          "cache_read_input_tokens": 77644,
          "cache_creation_input_tokens": 256,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 256
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

_source line 73 · 2026-05-25T21:16:03.557Z_

<details><summary>↩ Tool result · `toolu_01QRuwhugmejS8DDGW3C4Li5`</summary>

```text
1	% === Statistical Methods ===
2	
3	@article{cameron2008bootstrap,
4	  author    = {A. Colin Cameron and Jonah B. Gelbach and Douglas L. Miller},
5	  title     = {Bootstrap-Based Improvements for Inference with Clustered Errors},
6	  journal   = {Review of Economics and Statistics},
7	  volume    = {90},
8	  number    = {3},
9	  pages     = {414--427},
10	  year      = {2008},
11	}
12	
13	@book{wellek2010,
14	  author    = {Stefan Wellek},
15	  title     = {Testing Statistical Hypotheses of Equivalence and Noninferiority},
16	  publisher = {Chapman and Hall/CRC},
17	  edition   = {2nd},
18	  year      = {2010},
19	}
20	
21	@article{moulton1990,
22	  author  = {Brent R. Moulton},
23	  title   = {An Illustration of a Pitfall in Estimating the Effects of Aggregate Variables on Micro Units},
24	  journal = {The Review of Economics and Statistics},
25	  volume  = {72},
26	  number  = {2},
27	  pages   = {334--338},
28	  year    = {1990},
29	}
30	
31	@book{cohen1988,
32	  author    = {Cohen, Jacob},
33	  title     = {Statistical Power Analysis for the Behavioral Sciences},
34	  edition   = {2nd},
35	  publisher = {Lawrence Erlbaum Associates},
36	  year      = {1988}
37	}
38	
39	@article{kruschke2013bayesian,
40	  title={Bayesian estimation supersedes the t test},
41	  author={Kruschke, John K},
42	  journal={Journal of Experimental Psychology: General},
43	  volume={142},
44	  number={2},
45	  pages={573--603},
46	  year={2013},
47	  publisher={American Psychological Association}
48	}
49	
50	@article{kruschke2018rejecting,
51	  title={Rejecting or accepting parameter values in {B}ayesian estimation},
52	  author={Kruschke, John K},
53	  journal={Advances in Methods and Practices in Psychological Science},
54	  volume={1},
55	  number={2},
56	  pages={270--280},
57	  year={2018},
58	  publisher={SAGE Publications}
59	}
60	
61	% === Execution Simulation ===
62	
63	@inproceedings{gu2024cruxeval,
64	  title={{CRUXEval}: A Benchmark for Code Reasoning, Understanding and Execution},
65	  author={Gu, Alex and Rozi{\`e}re, Baptiste and Leather, Hugh and Solar-Lezama, Armando and Synnaeve, Gabriel and Wang, Sida I.},
66	  booktitle={Proceedings of the 41st International Conference on Machine Learning},
67	  pages={16568--16621},
68	  year={2024}
69	}
70	
71	@inproceedings{nam2025repoexec,
72	  title={{REPOEXEC}: Evaluate Code Generation with a Repository-Level Executable Benchmark},
73	  author={Nam, Hai and Dau, Thang and Bui, Nhat and Nguyen, Nghi D. Q.},
74	  booktitle={NAACL},
75	  year={2025}
76	}
77	
78	@inproceedings{zhao2026genprm,
79	  title={{GenPRM}: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning},
80	  author={Zhao, Mingyang and Liu, Yang and Yang, Lei and Chen, Liang and Li, Zhongyuan},
81	  booktitle={AAAI},
82	  year={2026}
83	}
84	
85	@inproceedings{hosseini2025genrm,
86	  title={Generative Verifiers: Reward Modeling as Next-Token Prediction},
87	  author={Hosseini, Arian and Yuan, Xingdi and Malkin, Nikolay and Courville, Aaron and Sordoni, Alessandro and Agarwal, Rishabh},
88	  booktitle={ICLR},
89	  year={2025}
90	}
91	
92	@article{maimon2026selfexecution,
93	  title={Self-Execution Simulation Improves Coding Models},
94	  author={Maimon, Gallil and Yoran, Ori and Kreuk, Felix and Hassid, Michael and Cohen, Gal and Chambon, Pierre and Adi, Yossi},
95	  journal={arXiv preprint arXiv:2604.03253},
96	  year={2026}
97	}
98	
99	@article{meta2025cwm,
100	  title={{CWM}: An Open-Weights {LLM} for Research on Code Generation with World Models},
101	  author={{FAIR CodeGen team} and Copet, Jade and Carbonneaux, Quentin and Cohen, Gal and Gehring, Jonas and Kahn, Jacob and Kossen, Jannik and Kreuk, Felix and McMilin, Emily and Meyer, Michel and Wei, Yuxiang and Zhang, David and Zheng, Kunhao and others},
102	  journal={arXiv preprint arXiv:2510.02387},
103	  year={2025}
104	}
105	
106	@article{liu2024codemind,
107	  title={{CodeMind}: A Framework to Challenge Large Language Models for Code Reasoning},
108	  author={Liu, Changshu and Zhang, Shizhuo Dylan and Ibrahimzada, Ali Reza and Jabbarvand, Reyhaneh},
109	  journal={arXiv preprint arXiv:2402.09664},
110	  year={2024}
111	}
112	
113	@article{abdollahi2025demystifying,
114	  title={Demystifying Errors in {LLM} Reasoning Traces: An Empirical Study of Code Execution Simulation},
115	  author={Abdollahi, Mohammad and Tasnia, Khandaker Rifah and Saha, Soumit Kanti and Yang, Jinqiu and Wang, Song and Hemmati, Hadi},
116	  journal={arXiv preprint arXiv:2512.00215},
117	  year={2025}
118	}
119	
120	@article{venkatkrishna2026aletheia,
121	  title={Aletheia: What Makes {RLVR} For Code Verifiers Tick?},
122	  author={Venkatkrishna, Vatsal and Paul, Indraneil and Gurevych, Iryna},
123	  journal={arXiv preprint arXiv:2601.12186},
124	  year={2026}
125	}
126	
127	@article{lee2026solidcoder,
128	  title={{SolidCoder}: Bridging the Mental-Reality Gap in {LLM} Code Generation through Concrete Execution},
129	  author={Lee, Woojin and Huang, Jin-Xia},
130	  journal={arXiv preprint arXiv:2604.19825},
131	  year={2026}
132	}
133	
134	@article{nye2021scratchpad,
135	  title={Show Your Work: Scratchpads for Intermediate Computation with Language Models},
136	  author={Nye, Maxwell and Andreassen, Anders Johan and Gur-Ari, Guy and Michalewski, Henryk and Austin, Jacob and Biber, David and Dohan, David and Lewkowycz, Aitor and Bosma, Maarten and Luan, David and Sutton, Charles and Odena, Augustus},
137	  journal={arXiv preprint arXiv:2112.00114},
138	  year={2021}
139	}
140	
141	@inproceedings{liu2023codeexecutor,
142	  title={Code Execution with Pre-trained Language Models},
143	  author={Liu, Chenxiao and Lu, Shuai and Chen, Weizhu and Jiang, Daxin and Svyatkovskiy, Alexey and Fu, Shengyu and Sundaresan, Neel and Duan, Nan},
144	  booktitle={Findings of the Association for Computational Linguistics: ACL 2023},
145	  year={2023}
146	}
147	
148	@article{li2024redo,
149	  title={{REDO}: Execution-Free Runtime Error Detection for Coding Agents},
150	  author={Li, Shou and Kan, Andrey and Callot, Laurent and Bhasker, Bhavana and Rashid, Muhammad Shihab and Esler, Timothy B},
151	  journal={arXiv preprint arXiv:2410.09117},
152	  year={2024}
153	}
154	
155	% === LLM Verification for Code ===
156	
157	@article{shum2025swerm,
158	  title={{SWE-RM}: Execution-free Feedback for Software Engineering Agents},
159	  author={Shum, KaShun and Hui, Binyuan and Chen, Jiawei and Zhang, Lei and Yang, Jiaxi and Huang, Yuzhen and Lin, Junyang and He, Junxian},
160	  journal={arXiv preprint arXiv:2512.21919},
161	  year={2025}
162	}
163	
164	@article{xu2025patchreasoner,
165	  title={Scalable Supervising Software Agents with Patch Reasoner},
166	  author={Xu, Junjielong and Tan, Boyin and Liu, Xiaoyuan and Peng, Chao and Gao, Pengfei and He, Pinjia},
167	  journal={arXiv preprint arXiv:2510.22775},
168	  year={2025}
169	}
170	
171	@inproceedings{chen2025vgsearch,
172	  title={Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling},
173	  author={Chen, Hao Mark and Lu, Guanxi and Okoshi, Yasuyuki and Mo, Zhiwen and Motomura, Masato and Fan, Hongxiang},
174	  booktitle={NeurIPS},
175	  year={2025}
176	}
177	
178	@inproceedings{snell2024scaling,
179	  title={Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},
180	  author={Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},
181	  booktitle={ICLR},
182	  year={2025},
183	  note={Oral}
184	}
185	
186	@inproceedings{li2025sstar,
187	  title={S*: Test Time Scaling for Code Generation},
188	  author={Li, Dacheng and Cao, Shiyi and Cao, Chengkun and Li, Xiuyu and Tan, Shangyin and Keutzer, Kurt and Xing, Jiarong and Gonzalez, Joseph E. and Stoica, Ion},
189	  booktitle={Findings of EMNLP},
190	  year={2025}
191	}
192	
193	% === APR and SWE-bench ===
194	
195	@inproceedings{jimenez2024swebench,
196	  title={{SWE-bench}: Can Language Models Resolve Real-world {GitHub} Issues?},
197	  author={Jimenez, Carlos E and Yang, John and Wettig, Alexander and Yao, Shunyu and Pei, Kexin and Press, Ofir and Narasimhan, Karthik},
198	  booktitle={ICLR},
199	  year={2024}
200	}
201	
202	@misc{chowdhury2024swebenchverified,
203	  title={Introducing {SWE-bench} Verified},
204	  author={Chowdhury, Neil and Aung, James and Shern, Chan Jun and Jaffe, Oliver and Sherburn, Dane and Starace, Giulio and Mays, Evan and Dias, Rachel and Aljubeh, Marwan and Glaese, Mia and Jimenez, Carlos E. and Yang, John and Ho, Leyton and Patwardhan, Tejal and Liu, Kevin and Madry, Aleksander},
205	  year={2024},
206	  url={https://openai.com/index/introducing-swe-bench-verified/}
207	}
208	
209	@inproceedings{yang2024sweagent,
210	  title={{SWE-agent}: Agent-Computer Interfaces Enable Automated Software Engineering},
211	  author={Yang, John and Jimenez, Carlos E and Wettig, Alexander and Lieret, Kilian and Yao, Shunyu and Narasimhan, Karthik and Press, Ofir},
212	  booktitle={NeurIPS},
213	  year={2024}
214	}
215	
216	@inproceedings{xia2024agentless,
217	  title={Agentless: Demystifying {LLM}-based Software Engineering Agents},
218	  author={Xia, Chunqiu Steven and Deng, Yinlin and Dunn, Soren and Zhang, Lingming},
219	  booktitle={FSE},
220	  year={2025},
221	  note={Distinguished Paper}
222	}
223	
224	@article{yang2025aprsurvey,
225	  title={A Survey of {LLM}-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications},
226	  author={Yang, Boyang and Cai, Zijian and Liu, Fengling and Le, Bach and Zhang, Lingming and Bissyand{\'e}, Tegawend{\'e} F. and Liu, Yang and Tian, Haoye},
227	  journal={arXiv preprint arXiv:2506.23749},
228	  year={2025}
229	}
230	
231	% === Code LLMs and Benchmarks ===
232	
233	@article{qwen2025qwen3,
234	  title={{Qwen3} Technical Report},
235	  author={Yang, An and Li, Anfeng and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and others},
236	  journal={arXiv preprint arXiv:2505.09388},
237	  year={2025}
238	}
239	
240	@article{chen2021humaneval,
241	  title={Evaluating Large Language Models Trained on Code},
242	  author={Chen, Mark and Tworek, Jerry and Jun, Heewoo and others},
243	  journal={arXiv preprint arXiv:2107.03374},
244	  year={2021}
245	}
246	
247	@article{austin2021mbpp,
248	  title={Program Synthesis with Large Language Models},
249	  author={Austin, Jacob and Odena, Augustus and Nye, Maxwell and others},
250	  journal={arXiv preprint arXiv:2108.07732},
251	  year={2021}
252	}
253	
254	@inproceedings{hu2022lora,
255	  title={{LoRA}: Low-Rank Adaptation of Large Language Models},
256	  author={Hu, Edward J and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
257	  booktitle={ICLR},
258	  year={2022}
259	}
260	
261	@inproceedings{dettmers2024qlora,
262	  title={{QLoRA}: Efficient Finetuning of Quantized {LLMs}},
263	  author={Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},
264	  booktitle={NeurIPS},
265	  year={2023}
266	}
267	
268	@article{guo2024deepseekcoder,
269	  title={{DeepSeek-Coder}: When the Large Language Model Meets Programming -- The Rise of Code Intelligence},
270	  author={Guo, Daya and Zhu, Qihao and Yang, Dejian and Xie, Zhenda and Dong, Kai and Zhang, Wentao and Chen, Guanting and Bi, Xiao and Wu, Y. and Li, Y.K. and Luo, Fuli and Xiong, Yun and Liang, Wenfeng},
271	  journal={arXiv preprint arXiv:2401.14196},
272	  year={2024}
273	}
274	
275	% === Code Verification ===
276	
277	@inproceedings{ni2023lever,
278	  title={{LEVER}: Learning to Verify Language-to-Code Generation with Execution},
279	  author={Ni, Ansong and Iyer, Srini and Radev, Dragomir and Stoyanov, Veselin and Yih, Wen-tau and Wang, Sida I. and Lin, Xi Victoria},
280	  booktitle={ICML},
281	  year={2023}
282	}
283	
284	@inproceedings{chen2023codet,
285	  title={{CodeT}: Code Generation with Generated Tests},
286	  author={Chen, Bei and Zhang, Fengji and Nguyen, Anh and Zan, Daoguang and Lin, Zeqi and Lou, Jian-Guang and Chen, Weizhu},
287	  booktitle={ICLR},
288	  year={2023}
289	}
290	
291	% === Process vs Outcome Supervision ===
292	
293	@article{lightman2023letsverify,
294	  title={Let's Verify Step by Step},
295	  author={Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},
296	  journal={arXiv preprint arXiv:2305.20050},
297	  year={2023}
298	}
299	
300	@article{uesato2022solving,
301	  title={Solving Math Word Problems with Process- and Outcome-Based Feedback},
302	  author={Uesato, Jonathan and Kushman, Nate and Kumar, Ramana and Song, Francis and Siegel, Noah and Wang, Lisa and Creswell, Antonia and Irving, Geoffrey and Higgins, Irina},
303	  journal={arXiv preprint arXiv:2211.14275},
304	  year={2022}
305	}
306	
307	@inproceedings{wang2024mathshepherd,
308	  title={Math-Shepherd: Verify and Reinforce {LLMs} Step-by-step without Human Annotations},
309	  author={Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, Yifei and Chen, Deli and Wu, Yu and Sui, Zhifang},
310	  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL)},
311	  year={2024}
312	}
313	
314	@article{luo2024omegaprm,
315	  title={Improve Mathematical Reasoning in Language Models by Automated Process Supervision},
316	  author={Luo, Liangchen and Liu, Yinxiao and Liu, Rosanne and Phatale, Samrat and Lara, Harsh and Li, Yunxuan and Shu, Lei and Zhu, Yun and Meng, Lei and Sun, Jiao and Rastogi, Abhinav},
317	  journal={arXiv preprint arXiv:2406.06592},
318	  year={2024}
319	}
320	
321	% === Verification-in-the-Loop ===
322	
323	@article{wang2026verpo,
324	  title={{VeRPO}: Verifiable Dense Reward Policy Optimization for Code Generation},
325	  author={Wang, Longwen and Wu, Xuan'er and Hu, Xiaohui and Liu, Yirui and Fan, Yuankai and Yu, Kaidong and Weng, Qizhen and Xi, Wei and Li, Xuelong},
326	  journal={arXiv preprint arXiv:2601.03525},
327	  year={2026}
328	}
329	
330	@article{tang2026execverify,
331	  title={{ExecVerify}: White-Box {RL} with Verifiable Stepwise Rewards for Code Execution Reasoning},
332	  author={Tang, Lingxiao and Ye, He and Chu, Zhaoyang and Ye, Muyang and Liu, Zhongxin and Ren, Xiaoxue and Bao, Lingfeng},
333	  journal={arXiv preprint arXiv:2603.11226},
334	  year={2026}
335	}
336	
337	@inproceedings{le2022coderl,
338	  title={{CodeRL}: Mastering Code Generation through Pretrained Models and Deep Reinforcement Learning},
339	  author={Le, Hung and Wang, Yue and Gotmare, Akhilesh Deepak and Savarese, Silvio and Hoi, Steven C.H.},
340	  booktitle={NeurIPS},
341	  year={2022}
342	}
343	
344	@article{li2022alphacode,
345	  title={Competition-Level Code Generation with {AlphaCode}},
346	  author={Li, Yujia and Choi, David and Chung, Junyoung and Kushman, Nate and Schrittwieser, Julian and others},
347	  journal={Science},
348	  volume={378},
349	  number={6624},
350	  pages={1092--1097},
351	  year={2022}
352	}
353	
354	@article{shinn2023reflexion,
355	  title={Reflexion: Language Agents with Verbal Reinforcement Learning},
356	  author={Shinn, Noah and Cassano, Federico and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},
357	  journal={NeurIPS},
358	  year={2023}
359	}
360	
361	% === Predictive Mutation Testing ===
362	
363	@inproceedings{tufano2019predictive,
364	  title={Learning How to Mutate Source Code from Bug-Fixes},
365	  author={Tufano, Michele and Watson, Cody and Bavota, Gabriele and Di Penta, Massimiliano and White, Martin and Poshyvanyk, Denys},
366	  booktitle={ISSTA},
367	  year={2019}
368	}
369	
370	@article{kim2022predictive,
371	  title={Predictive Mutation Testing via Natural Language Channel},
372	  author={Kim, Jinhan and Ju, Juyoung and Tao, Robert and Hu, Nhat-Tan and Baik, Shin Yoo Juyeon},
373	  journal={IEEE TSE},
374	  year={2022}
375	}
376	
377	% === Task Reformulation NLP ===
378	
379	@article{raffel2020t5,
380	  title={Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},
381	  author={Raffel, Colin and Shazeer, Noam and Roberts, Adam and Lee, Katherine and Narang, Sharan and Matena, Michael and Zhou, Yanqi and Li, Wei and Liu, Peter J},
382	  journal={JMLR},
383	  volume={21},
384	  number={140},
385	  pages={1--67},
386	  year={2020}
387	}
388	
389	% === Mutation Testing Validity ===
390	
391	@inproceedings{andrews2005mutation,
392	  title={Is Mutation an Adequate Substitute for Real Faults?},
393	  author={Andrews, James H and Briand, Lionel C and Labiche, Yvan},
394	  booktitle={ICSE},
395	  pages={313--322},
396	  year={2005}
397	}
398	
399	@inproceedings{just2014mutants,
400	  title={Are Mutants a Valid Substitute for Real Faults in Software Testing?},
401	  author={Just, Ren{\'e} and Jalali, Darioush and Inozemtseva, Laura and Ernst, Michael D and Holmes, Reid and Fraser, Gordon},
402	  booktitle={FSE},
403	  pages={654--665},
404	  year={2014}
405	}
406	
407	% === Sampling and Consistency ===
408	
409	@inproceedings{wang2023selfconsistency,
410	  title={Self-Consistency Improves Chain of Thought Reasoning in Language Models},
411	  author={Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},
412	  booktitle={ICLR},
413	  year={2023}
414	}
415	
416	% === Statistical Methods ===
417	
418	@book{angrist2009mostly,
419	  title={Mostly Harmless Econometrics: An Empiricist's Companion},
420	  author={Angrist, Joshua D. and Pischke, J{\"o}rn-Steffen},
421	  year={2009},
422	  publisher={Princeton University Press}
423	}
424	
425	@article{schuirmann1987tost,
426	  title={A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},
427	  author={Schuirmann, Donald J},
428	  journal={Journal of Pharmacokinetics and Biopharmaceutics},
429	  volume={15},
430	  number={6},
431	  pages={657--680},
432	  year={1987}
433	}
434	
435	@book{davison1997bootstrap,
436	  title={Bootstrap Methods and their Application},
437	  author={Davison, Anthony C and Hinkley, David V},
438	  publisher={Cambridge University Press},
439	  year={1997}
440	}
441	
442	@article{shrout1979icc,
443	  title={Intraclass Correlations: Uses in Assessing Rater Reliability},
444	  author={Shrout, Patrick E and Fleiss, Joseph L},
445	  journal={Psychological Bulletin},
446	  volume={86},
447	  number={2},
448	  pages={420--428},
449	  year={1979},
450	  doi={10.1037/0033-2909.86.2.420}
451	}
452	
453	@article{holm1979,
454	  title={A Simple Sequentially Rejective Multiple Test Procedure},
455	  author={Holm, Sture},
456	  journal={Scandinavian Journal of Statistics},
457	  volume={6},
458	  number={2},
459	  pages={65--70},
460	  year={1979}
461	}
462	
463	@article{lakens2017,
464	  title={Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses},
465	  author={Lakens, Dani{\"e}l},
466	  journal={Social Psychological and Personality Science},
467	  volume={8},
468	  number={4},
469	  pages={355--362},
470	  year={2017}
471	}
472	
473	@article{hoenig2001,
474	  title={The Abuse of Power: The Pervasive Fallacy of Power Calculations for Data Analysis},
475	  author={Hoenig, John M. and Heisey, Dennis M.},
476	  journal={The American Statistician},
477	  volume={55},
478	  number={1},
479	  pages={19--24},
480	  year={2001}
481	}
482	
483	% === Code Evaluation Metrics ===
484	
485	@inproceedings{zhuo2024icescore,
486	  title={{ICE-Score}: Instructing Large Language Models to Evaluate Code},
487	  author={Zhuo, Terry Yue},
488	  booktitle={Findings of EACL},
489	  year={2024}
490	}
491	
492	@article{dong2024codescore,
493	  title={{CodeScore}: Evaluating Code Generation by Learning Code Execution},
494	  author={Dong, Yihong and Ding, Jiazheng and Jiang, Xue and Li, Ge and Li, Zhuo and Jin, Zhi},
495	  journal={ACM Transactions on Software Engineering and Methodology},
496	  volume={33},
497	  number={8},
498	  year={2024}
499	}
500	
501	@inproceedings{zhou2023codebertscore,
502	  title={{CodeBERTScore}: Evaluating Code Generation with Pretrained Models of Code},
503	  author={Zhou, Shuyan and Alon, Uri and Agarwal, Sumit and Neubig, Graham},
504	  booktitle={EMNLP},
505	  year={2023}
506	}
507	
508	% === Constrained Decoding ===
509	
510	@article{willard2023outlines,
511	  title={Efficient Guided Generation for Large Language Models},
512	  author={Willard, Brandon T. and Louf, R{\'e}mi},
513	  journal={arXiv preprint arXiv:2307.09702},
514	  year={2023}
515	}
516	
517	@inproceedings{poesia2022synchromesh,
518	  author    = {Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares, Gustavo and Meek, Christopher and Gulwani, Sumit},
519	  title     = {Synchromesh: Reliable Code Generation by Retrieving and Transforming},
520	  booktitle = {ICLR},
521	  year      = {2022}
522	}
523	
524	@inproceedings{dong2024xgrammar,
525	  author    = {Dong, Yixin and Huang, Charlie F. and Chen, Tianqi},
526	  title     = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},
527	  booktitle = {MLSys},
528	  year      = {2025}
529	}
530	
531	@inproceedings{ma2025coderm,
532	  author    = {Ma, Zeyao and Zhang, Xiaokang and Zhang, Jing and Yu, Jifan and Tang, Jie},
533	  title     = {Dynamic Scaling of Unit Tests for Code Reward Modeling},
534	  booktitle = {Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},
535	  pages     = {6917--6935},
536	  year      = {2025}
537	}
538	
539	% === Code Reward Models ===
540	
541	@article{zhu2026codescaler,
542	  title={{CodeScaler}: Scaling Code {LLM} Training and Test-Time Inference via Execution-Free Reward Models},
543	  author={Zhu, Xiao and Zhou, Xinyu and Zhu, Boyu and Hu, Hanxu and Du, Mingzhe and Zhang, Haotian and Wang, Huiming and Guo, Zhijiang},
544	  journal={arXiv preprint arXiv:2602.17684},
545	  year={2026}
546	}
547	
548	@inproceedings{li2025codeprm,
549	  title={{CodePRM}: Execution Feedback-enhanced Process Reward Model for Code Generation},
550	  author={Li, Qingyao and Dai, Xinyi and Li, Xiangyang and Zhang, Weinan and Wang, Yasheng and Tang, Ruiming and Yu, Yong},
551	  booktitle={Findings of ACL},
552	  pages={8169--8182},
553	  year={2025}
554	}
555	
556	@article{zhang2026funprm,
557	  title={{FunPRM}: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation},
558	  author={Zhang, Ruiyi and Qin, Peijia and Cao, Qi and Xue, Eric and Xie, Pengtao},
559	  journal={arXiv preprint arXiv:2601.22249},
560	  year={2026}
561	}
562	
563	@article{jiang2025coderlplus,
564	  title={{CodeRL+}: Improving Code Generation via Reinforcement with Execution Semantics Alignment},
565	  author={Jiang, Xue and Dong, Yihong and Liu, Mengyang and Deng, Hongyi and Wang, Tian and Tao, Yongding and Cao, Rongyu and Li, Binhua and Jin, Zhi and Jiao, Wenpin and Huang, Fei and Li, Yongbin and Li, Ge},
566	  journal={arXiv preprint arXiv:2510.18471},
567	  year={2025}
568	}
569	
570	@inproceedings{ye2025prlcoder,
571	  title={Process-Supervised Reinforcement Learning for Code Generation},
572	  author={Ye, Yufan and Zhang, Ting and Jiang, Wenbin and Huang, Hua},
573	  booktitle={EMNLP},
574	  year={2025}
575	}
576	
577	@article{dreamprm2025code,
578	  title={{DreamPRM-Code}: Function-as-Step Process Reward Model with Label Correction for {LLM} Coding},
579	  author={Zhang, Ruiyi and Qin, Peijia and Cao, Qi and Xie, Pengtao},
580	  journal={arXiv preprint arXiv:2512.15000},
581	  year={2025}
582	}
583	
584	% === Mutation Testing ===
585	
586	@inproceedings{jain2023contextual,
587	  title={Contextual Predictive Mutation Testing},
588	  author={Jain, Kush and Barik, Ristimoy and Le Goues, Claire},
589	  booktitle={ESEC/FSE},
590	  year={2023}
591	}
592	
593	@article{wang2024llmmutation,
594	  title={A Comprehensive Study on Large Language Models for Mutation Testing},
595	  author={Wang, Bo and Chen, Mingda and Deng, Ming and Lin, Youfang and Harman, Mark and Papadakis, Mike and Zhang, Jie M.},
596	  journal={ACM Transactions on Software Engineering and Methodology},
597	  year={2025}
598	}
599	
600	% === Code Generation Systems ===
601	
602	@techreport{alphacode2023team,
603	  title={{AlphaCode} 2 Technical Report},
604	  author={{AlphaCode Team}},
605	  institution={Google DeepMind},
606	  year={2023},
607	  url={https://storage.googleapis.com/deepmind-media/AlphaCode2/AlphaCode2_Tech_Report.pdf}
608	}
609	
610	
611	@article{wei2022emergent,
612	  author    = {Jason Wei and Yi Tay and Rishi Bommasani and Colin Raffel and Barret Zoph and Sebastian Borgeaud and Dani Yogatama and Maarten Bosma and Denny Zhou and Donald Metzler and Ed H. Chi and Tatsunori Hashimoto and Oriol Vinyals and Percy Liang and Jeff Dean and William Fedus},
613	  title     = {Emergent Abilities of Large Language Models},
614	  journal   = {Transactions on Machine Learning Research (TMLR)},
615	  year      = {2022}
616	}
617	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09311c21-3150-4808-a271-3dff225e9559",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "009275db-8d49-4f4a-bb86-9d60f29911a6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib",
      "content": "% === Statistical Methods ===\n\n@article{cameron2008bootstrap,\n  author    = {A. Colin Cameron and Jonah B. Gelbach and Douglas L. Miller},\n  title     = {Bootstrap-Based Improvements for Inference with Clustered Errors},\n  journal   = {Review of Economics and Statistics},\n  volume    = {90},\n  number    = {3},\n  pages     = {414--427},\n  year      = {2008},\n}\n\n@book{wellek2010,\n  author    = {Stefan Wellek},\n  title     = {Testing Statistical Hypotheses of Equivalence and Noninferiority},\n  publisher = {Chapman and Hall/CRC},\n  edition   = {2nd},\n  year      = {2010},\n}\n\n@article{moulton1990,\n  author  = {Brent R. Moulton},\n  title   = {An Illustration of a Pitfall in Estimating the Effects of Aggregate Variables on Micro Units},\n  journal = {The Review of Economics and Statistics},\n  volume  = {72},\n  number  = {2},\n  pages   = {334--338},\n  year    = {1990},\n}\n\n@book{cohen1988,\n  author    = {Cohen, Jacob},\n  title     = {Statistical Power Analysis for the Behavioral Sciences},\n  edition   = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1988}\n}\n\n@article{kruschke2013bayesian,\n  title={Bayesian estimation supersedes the t test},\n  author={Kruschke, John K},\n  journal={Journal of Experimental Psychology: General},\n  volume={142},\n  number={2},\n  pages={573--603},\n  year={2013},\n  publisher={American Psychological Association}\n}\n\n@article{kruschke2018rejecting,\n  title={Rejecting or accepting parameter values in {B}ayesian estimation},\n  author={Kruschke, John K},\n  journal={Advances in Methods and Practices in Psychological Science},\n  volume={1},\n  number={2},\n  pages={270--280},\n  year={2018},\n  publisher={SAGE Publications}\n}\n\n% === Execution Simulation ===\n\n@inproceedings{gu2024cruxeval,\n  title={{CRUXEval}: A Benchmark for Code Reasoning, Understanding and Execution},\n  author={Gu, Alex and Rozi{\\`e}re, Baptiste and Leather, Hugh and Solar-Lezama, Armando and Synnaeve, Gabriel and Wang, Sida I.},\n  booktitle={Proceedings of the 41st International Conference on Machine Learning},\n  pages={16568--16621},\n  year={2024}\n}\n\n@inproceedings{nam2025repoexec,\n  title={{REPOEXEC}: Evaluate Code Generation with a Repository-Level Executable Benchmark},\n  author={Nam, Hai and Dau, Thang and Bui, Nhat and Nguyen, Nghi D. Q.},\n  booktitle={NAACL},\n  year={2025}\n}\n\n@inproceedings{zhao2026genprm,\n  title={{GenPRM}: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning},\n  author={Zhao, Mingyang and Liu, Yang and Yang, Lei and Chen, Liang and Li, Zhongyuan},\n  booktitle={AAAI},\n  year={2026}\n}\n\n@inproceedings{hosseini2025genrm,\n  title={Generative Verifiers: Reward Modeling as Next-Token Prediction},\n  author={Hosseini, Arian and Yuan, Xingdi and Malkin, Nikolay and Courville, Aaron and Sordoni, Alessandro and Agarwal, Rishabh},\n  booktitle={ICLR},\n  year={2025}\n}\n\n@article{maimon2026selfexecution,\n  title={Self-Execution Simulation Improves Coding Models},\n  author={Maimon, Gallil and Yoran, Ori and Kreuk, Felix and Hassid, Michael and Cohen, Gal and Chambon, Pierre and Adi, Yossi},\n  journal={arXiv preprint arXiv:2604.03253},\n  year={2026}\n}\n\n@article{meta2025cwm,\n  title={{CWM}: An Open-Weights {LLM} for Research on Code Generation with World Models},\n  author={{FAIR CodeGen team} and Copet, Jade and Carbonneaux, Quentin and Cohen, Gal and Gehring, Jonas and Kahn, Jacob and Kossen, Jannik and Kreuk, Felix and McMilin, Emily and Meyer, Michel and Wei, Yuxiang and Zhang, David and Zheng, Kunhao and others},\n  journal={arXiv preprint arXiv:2510.02387},\n  year={2025}\n}\n\n@article{liu2024codemind,\n  title={{CodeMind}: A Framework to Challenge Large Language Models for Code Reasoning},\n  author={Liu, Changshu and Zhang, Shizhuo Dylan and Ibrahimzada, Ali Reza and Jabbarvand, Reyhaneh},\n  journal={arXiv preprint arXiv:2402.09664},\n  year={2024}\n}\n\n@article{abdollahi2025demystifying,\n  title={Demystifying Errors in {LLM} Reasoning Traces: An Empirical Study of Code Execution Simulation},\n  author={Abdollahi, Mohammad and Tasnia, Khandaker Rifah and Saha, Soumit Kanti and Yang, Jinqiu and Wang, Song and Hemmati, Hadi},\n  journal={arXiv preprint arXiv:2512.00215},\n  year={2025}\n}\n\n@article{venkatkrishna2026aletheia,\n  title={Aletheia: What Makes {RLVR} For Code Verifiers Tick?},\n  author={Venkatkrishna, Vatsal and Paul, Indraneil and Gurevych, Iryna},\n  journal={arXiv preprint arXiv:2601.12186},\n  year={2026}\n}\n\n@article{lee2026solidcoder,\n  title={{SolidCoder}: Bridging the Mental-Reality Gap in {LLM} Code Generation through Concrete Execution},\n  author={Lee, Woojin and Huang, Jin-Xia},\n  journal={arXiv preprint arXiv:2604.19825},\n  year={2026}\n}\n\n@article{nye2021scratchpad,\n  title={Show Your Work: Scratchpads for Intermediate Computation with Language Models},\n  author={Nye, Maxwell and Andreassen, Anders Johan and Gur-Ari, Guy and Michalewski, Henryk and Austin, Jacob and Biber, David and Dohan, David and Lewkowycz, Aitor and Bosma, Maarten and Luan, David and Sutton, Charles and Odena, Augustus},\n  journal={arXiv preprint arXiv:2112.00114},\n  year={2021}\n}\n\n@inproceedings{liu2023codeexecutor,\n  title={Code Execution with Pre-trained Language Models},\n  author={Liu, Chenxiao and Lu, Shuai and Chen, Weizhu and Jiang, Daxin and Svyatkovskiy, Alexey and Fu, Shengyu and Sundaresan, Neel and Duan, Nan},\n  booktitle={Findings of the Association for Computational Linguistics: ACL 2023},\n  year={2023}\n}\n\n@article{li2024redo,\n  title={{REDO}: Execution-Free Runtime Error Detection for Coding Agents},\n  author={Li, Shou and Kan, Andrey and Callot, Laurent and Bhasker, Bhavana and Rashid, Muhammad Shihab and Esler, Timothy B},\n  journal={arXiv preprint arXiv:2410.09117},\n  year={2024}\n}\n\n% === LLM Verification for Code ===\n\n@article{shum2025swerm,\n  title={{SWE-RM}: Execution-free Feedback for Software Engineering Agents},\n  author={Shum, KaShun and Hui, Binyuan and Chen, Jiawei and Zhang, Lei and Yang, Jiaxi and Huang, Yuzhen and Lin, Junyang and He, Junxian},\n  journal={arXiv preprint arXiv:2512.21919},\n  year={2025}\n}\n\n@article{xu2025patchreasoner,\n  title={Scalable Supervising Software Agents with Patch Reasoner},\n  author={Xu, Junjielong and Tan, Boyin and Liu, Xiaoyuan and Peng, Chao and Gao, Pengfei and He, Pinjia},\n  journal={arXiv preprint arXiv:2510.22775},\n  year={2025}\n}\n\n@inproceedings{chen2025vgsearch,\n  title={Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling},\n  author={Chen, Hao Mark and Lu, Guanxi and Okoshi, Yasuyuki and Mo, Zhiwen and Motomura, Masato and Fan, Hongxiang},\n  booktitle={NeurIPS},\n  year={2025}\n}\n\n@inproceedings{snell2024scaling,\n  title={Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author={Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle={ICLR},\n  year={2025},\n  note={Oral}\n}\n\n@inproceedings{li2025sstar,\n  title={S*: Test Time Scaling for Code Generation},\n  author={Li, Dacheng and Cao, Shiyi and Cao, Chengkun and Li, Xiuyu and Tan, Shangyin and Keutzer, Kurt and Xing, Jiarong and Gonzalez, Joseph E. and Stoica, Ion},\n  booktitle={Findings of EMNLP},\n  year={2025}\n}\n\n% === APR and SWE-bench ===\n\n@inproceedings{jimenez2024swebench,\n  title={{SWE-bench}: Can Language Models Resolve Real-world {GitHub} Issues?},\n  author={Jimenez, Carlos E and Yang, John and Wettig, Alexander and Yao, Shunyu and Pei, Kexin and Press, Ofir and Narasimhan, Karthik},\n  booktitle={ICLR},\n  year={2024}\n}\n\n@misc{chowdhury2024swebenchverified,\n  title={Introducing {SWE-bench} Verified},\n  author={Chowdhury, Neil and Aung, James and Shern, Chan Jun and Jaffe, Oliver and Sherburn, Dane and Starace, Giulio and Mays, Evan and Dias, Rachel and Aljubeh, Marwan and Glaese, Mia and Jimenez, Carlos E. and Yang, John and Ho, Leyton and Patwardhan, Tejal and Liu, Kevin and Madry, Aleksander},\n  year={2024},\n  url={https://openai.com/index/introducing-swe-bench-verified/}\n}\n\n@inproceedings{yang2024sweagent,\n  title={{SWE-agent}: Agent-Computer Interfaces Enable Automated Software Engineering},\n  author={Yang, John and Jimenez, Carlos E and Wettig, Alexander and Lieret, Kilian and Yao, Shunyu and Narasimhan, Karthik and Press, Ofir},\n  booktitle={NeurIPS},\n  year={2024}\n}\n\n@inproceedings{xia2024agentless,\n  title={Agentless: Demystifying {LLM}-based Software Engineering Agents},\n  author={Xia, Chunqiu Steven and Deng, Yinlin and Dunn, Soren and Zhang, Lingming},\n  booktitle={FSE},\n  year={2025},\n  note={Distinguished Paper}\n}\n\n@article{yang2025aprsurvey,\n  title={A Survey of {LLM}-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications},\n  author={Yang, Boyang and Cai, Zijian and Liu, Fengling and Le, Bach and Zhang, Lingming and Bissyand{\\'e}, Tegawend{\\'e} F. and Liu, Yang and Tian, Haoye},\n  journal={arXiv preprint arXiv:2506.23749},\n  year={2025}\n}\n\n% === Code LLMs and Benchmarks ===\n\n@article{qwen2025qwen3,\n  title={{Qwen3} Technical Report},\n  author={Yang, An and Li, Anfeng and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and others},\n  journal={arXiv preprint arXiv:2505.09388},\n  year={2025}\n}\n\n@article{chen2021humaneval,\n  title={Evaluating Large Language Models Trained on Code},\n  author={Chen, Mark and Tworek, Jerry and Jun, Heewoo and others},\n  journal={arXiv preprint arXiv:2107.03374},\n  year={2021}\n}\n\n@article{austin2021mbpp,\n  title={Program Synthesis with Large Language Models},\n  author={Austin, Jacob and Odena, Augustus and Nye, Maxwell and others},\n  journal={arXiv preprint arXiv:2108.07732},\n  year={2021}\n}\n\n@inproceedings{hu2022lora,\n  title={{LoRA}: Low-Rank Adaptation of Large Language Models},\n  author={Hu, Edward J and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},\n  booktitle={ICLR},\n  year={2022}\n}\n\n@inproceedings{dettmers2024qlora,\n  title={{QLoRA}: Efficient Finetuning of Quantized {LLMs}},\n  author={Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},\n  booktitle={NeurIPS},\n  year={2023}\n}\n\n@article{guo2024deepseekcoder,\n  title={{DeepSeek-Coder}: When the Large Language Model Meets Programming -- The Rise of Code Intelligence},\n  author={Guo, Daya and Zhu, Qihao and Yang, Dejian and Xie, Zhenda and Dong, Kai and Zhang, Wentao and Chen, Guanting and Bi, Xiao and Wu, Y. and Li, Y.K. and Luo, Fuli and Xiong, Yun and Liang, Wenfeng},\n  journal={arXiv preprint arXiv:2401.14196},\n  year={2024}\n}\n\n% === Code Verification ===\n\n@inproceedings{ni2023lever,\n  title={{LEVER}: Learning to Verify Language-to-Code Generation with Execution},\n  author={Ni, Ansong and Iyer, Srini and Radev, Dragomir and Stoyanov, Veselin and Yih, Wen-tau and Wang, Sida I. and Lin, Xi Victoria},\n  booktitle={ICML},\n  year={2023}\n}\n\n@inproceedings{chen2023codet,\n  title={{CodeT}: Code Generation with Generated Tests},\n  author={Chen, Bei and Zhang, Fengji and Nguyen, Anh and Zan, Daoguang and Lin, Zeqi and Lou, Jian-Guang and Chen, Weizhu},\n  booktitle={ICLR},\n  year={2023}\n}\n\n% === Process vs Outcome Supervision ===\n\n@article{lightman2023letsverify,\n  title={Let's Verify Step by Step},\n  author={Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  journal={arXiv preprint arXiv:2305.20050},\n  year={2023}\n}\n\n@article{uesato2022solving,\n  title={Solving Math Word Problems with Process- and Outcome-Based Feedback},\n  author={Uesato, Jonathan and Kushman, Nate and Kumar, Ramana and Song, Francis and Siegel, Noah and Wang, Lisa and Creswell, Antonia and Irving, Geoffrey and Higgins, Irina},\n  journal={arXiv preprint arXiv:2211.14275},\n  year={2022}\n}\n\n@inproceedings{wang2024mathshepherd,\n  title={Math-Shepherd: Verify and Reinforce {LLMs} Step-by-step without Human Annotations},\n  author={Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, Yifei and Chen, Deli and Wu, Yu and Sui, Zhifang},\n  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2024}\n}\n\n@article{luo2024omegaprm,\n  title={Improve Mathematical Reasoning in Language Models by Automated Process Supervision},\n  author={Luo, Liangchen and Liu, Yinxiao and Liu, Rosanne and Phatale, Samrat and Lara, Harsh and Li, Yunxuan and Shu, Lei and Zhu, Yun and Meng, Lei and Sun, Jiao and Rastogi, Abhinav},\n  journal={arXiv preprint arXiv:2406.06592},\n  year={2024}\n}\n\n% === Verification-in-the-Loop ===\n\n@article{wang2026verpo,\n  title={{VeRPO}: Verifiable Dense Reward Policy Optimization for Code Generation},\n  author={Wang, Longwen and Wu, Xuan'er and Hu, Xiaohui and Liu, Yirui and Fan, Yuankai and Yu, Kaidong and Weng, Qizhen and Xi, Wei and Li, Xuelong},\n  journal={arXiv preprint arXiv:2601.03525},\n  year={2026}\n}\n\n@article{tang2026execverify,\n  title={{ExecVerify}: White-Box {RL} with Verifiable Stepwise Rewards for Code Execution Reasoning},\n  author={Tang, Lingxiao and Ye, He and Chu, Zhaoyang and Ye, Muyang and Liu, Zhongxin and Ren, Xiaoxue and Bao, Lingfeng},\n  journal={arXiv preprint arXiv:2603.11226},\n  year={2026}\n}\n\n@inproceedings{le2022coderl,\n  title={{CodeRL}: Mastering Code Generation through Pretrained Models and Deep Reinforcement Learning},\n  author={Le, Hung and Wang, Yue and Gotmare, Akhilesh Deepak and Savarese, Silvio and Hoi, Steven C.H.},\n  booktitle={NeurIPS},\n  year={2022}\n}\n\n@article{li2022alphacode,\n  title={Competition-Level Code Generation with {AlphaCode}},\n  author={Li, Yujia and Choi, David and Chung, Junyoung and Kushman, Nate and Schrittwieser, Julian and others},\n  journal={Science},\n  volume={378},\n  number={6624},\n  pages={1092--1097},\n  year={2022}\n}\n\n@article{shinn2023reflexion,\n  title={Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author={Shinn, Noah and Cassano, Federico and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},\n  journal={NeurIPS},\n  year={2023}\n}\n\n% === Predictive Mutation Testing ===\n\n@inproceedings{tufano2019predictive,\n  title={Learning How to Mutate Source Code from Bug-Fixes},\n  author={Tufano, Michele and Watson, Cody and Bavota, Gabriele and Di Penta, Massimiliano and White, Martin and Poshyvanyk, Denys},\n  booktitle={ISSTA},\n  year={2019}\n}\n\n@article{kim2022predictive,\n  title={Predictive Mutation Testing via Natural Language Channel},\n  author={Kim, Jinhan and Ju, Juyoung and Tao, Robert and Hu, Nhat-Tan and Baik, Shin Yoo Juyeon},\n  journal={IEEE TSE},\n  year={2022}\n}\n\n% === Task Reformulation NLP ===\n\n@article{raffel2020t5,\n  title={Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},\n  author={Raffel, Colin and Shazeer, Noam and Roberts, Adam and Lee, Katherine and Narang, Sharan and Matena, Michael and Zhou, Yanqi and Li, Wei and Liu, Peter J},\n  journal={JMLR},\n  volume={21},\n  number={140},\n  pages={1--67},\n  year={2020}\n}\n\n% === Mutation Testing Validity ===\n\n@inproceedings{andrews2005mutation,\n  title={Is Mutation an Adequate Substitute for Real Faults?},\n  author={Andrews, James H and Briand, Lionel C and Labiche, Yvan},\n  booktitle={ICSE},\n  pages={313--322},\n  year={2005}\n}\n\n@inproceedings{just2014mutants,\n  title={Are Mutants a Valid Substitute for Real Faults in Software Testing?},\n  author={Just, Ren{\\'e} and Jalali, Darioush and Inozemtseva, Laura and Ernst, Michael D and Holmes, Reid and Fraser, Gordon},\n  booktitle={FSE},\n  pages={654--665},\n  year={2014}\n}\n\n% === Sampling and Consistency ===\n\n@inproceedings{wang2023selfconsistency,\n  title={Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author={Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle={ICLR},\n  year={2023}\n}\n\n% === Statistical Methods ===\n\n@book{angrist2009mostly,\n  title={Mostly Harmless Econometrics: An Empiricist's Companion},\n  author={Angrist, Joshua D. and Pischke, J{\\\"o}rn-Steffen},\n  year={2009},\n  publisher={Princeton University Press}\n}\n\n@article{schuirmann1987tost,\n  title={A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},\n  author={Schuirmann, Donald J},\n  journal={Journal of Pharmacokinetics and Biopharmaceutics},\n  volume={15},\n  number={6},\n  pages={657--680},\n  year={1987}\n}\n\n@book{davison1997bootstrap,\n  title={Bootstrap Methods and their Application},\n  author={Davison, Anthony C and Hinkley, David V},\n  publisher={Cambridge University Press},\n  year={1997}\n}\n\n@article{shrout1979icc,\n  title={Intraclass Correlations: Uses in Assessing Rater Reliability},\n  author={Shrout, Patrick E and Fleiss, Joseph L},\n  journal={Psychological Bulletin},\n  volume={86},\n  number={2},\n  pages={420--428},\n  year={1979},\n  doi={10.1037/0033-2909.86.2.420}\n}\n\n@article{holm1979,\n  title={A Simple Sequentially Rejective Multiple Test Procedure},\n  author={Holm, Sture},\n  journal={Scandinavian Journal of Statistics},\n  volume={6},\n  number={2},\n  pages={65--70},\n  year={1979}\n}\n\n@article{lakens2017,\n  title={Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses},\n  author={Lakens, Dani{\\\"e}l},\n  journal={Social Psychological and Personality Science},\n  volume={8},\n  number={4},\n  pages={355--362},\n  year={2017}\n}\n\n@article{hoenig2001,\n  title={The Abuse of Power: The Pervasive Fallacy of Power Calculations for Data Analysis},\n  author={Hoenig, John M. and Heisey, Dennis M.},\n  journal={The American Statistician},\n  volume={55},\n  number={1},\n  pages={19--24},\n  year={2001}\n}\n\n% === Code Evaluation Metrics ===\n\n@inproceedings{zhuo2024icescore,\n  title={{ICE-Score}: Instructing Large Language Models to Evaluate Code},\n  author={Zhuo, Terry Yue},\n  booktitle={Findings of EACL},\n  year={2024}\n}\n\n@article{dong2024codescore,\n  title={{CodeScore}: Evaluating Code Generation by Learning Code Execution},\n  author={Dong, Yihong and Ding, Jiazheng and Jiang, Xue and Li, Ge and Li, Zhuo and Jin, Zhi},\n  journal={ACM Transactions on Software Engineering and Methodology},\n  volume={33},\n  number={8},\n  year={2024}\n}\n\n@inproceedings{zhou2023codebertscore,\n  title={{CodeBERTScore}: Evaluating Code Generation with Pretrained Models of Code},\n  author={Zhou, Shuyan and Alon, Uri and Agarwal, Sumit and Neubig, Graham},\n  booktitle={EMNLP},\n  year={2023}\n}\n\n% === Constrained Decoding ===\n\n@article{willard2023outlines,\n  title={Efficient Guided Generation for Large Language Models},\n  author={Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal={arXiv preprint arXiv:2307.09702},\n  year={2023}\n}\n\n@inproceedings{poesia2022synchromesh,\n  author    = {Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares, Gustavo and Meek, Christopher and Gulwani, Sumit},\n  title     = {Synchromesh: Reliable Code Generation by Retrieving and Transforming},\n  booktitle = {ICLR},\n  year      = {2022}\n}\n\n@inproceedings{dong2024xgrammar,\n  author    = {Dong, Yixin and Huang, Charlie F. and Chen, Tianqi},\n  title     = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},\n  booktitle = {MLSys},\n  year      = {2025}\n}\n\n@inproceedings{ma2025coderm,\n  author    = {Ma, Zeyao and Zhang, Xiaokang and Zhang, Jing and Yu, Jifan and Tang, Jie},\n  title     = {Dynamic Scaling of Unit Tests for Code Reward Modeling},\n  booktitle = {Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages     = {6917--6935},\n  year      = {2025}\n}\n\n% === Code Reward Models ===\n\n@article{zhu2026codescaler,\n  title={{CodeScaler}: Scaling Code {LLM} Training and Test-Time Inference via Execution-Free Reward Models},\n  author={Zhu, Xiao and Zhou, Xinyu and Zhu, Boyu and Hu, Hanxu and Du, Mingzhe and Zhang, Haotian and Wang, Huiming and Guo, Zhijiang},\n  journal={arXiv preprint arXiv:2602.17684},\n  year={2026}\n}\n\n@inproceedings{li2025codeprm,\n  title={{CodePRM}: Execution Feedback-enhanced Process Reward Model for Code Generation},\n  author={Li, Qingyao and Dai, Xinyi and Li, Xiangyang and Zhang, Weinan and Wang, Yasheng and Tang, Ruiming and Yu, Yong},\n  booktitle={Findings of ACL},\n  pages={8169--8182},\n  year={2025}\n}\n\n@article{zhang2026funprm,\n  title={{FunPRM}: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation},\n  author={Zhang, Ruiyi and Qin, Peijia and Cao, Qi and Xue, Eric and Xie, Pengtao},\n  journal={arXiv preprint arXiv:2601.22249},\n  year={2026}\n}\n\n@article{jiang2025coderlplus,\n  title={{CodeRL+}: Improving Code Generation via Reinforcement with Execution Semantics Alignment},\n  author={Jiang, Xue and Dong, Yihong and Liu, Mengyang and Deng, Hongyi and Wang, Tian and Tao, Yongding and Cao, Rongyu and Li, Binhua and Jin, Zhi and Jiao, Wenpin and Huang, Fei and Li, Yongbin and Li, Ge},\n  journal={arXiv preprint arXiv:2510.18471},\n  year={2025}\n}\n\n@inproceedings{ye2025prlcoder,\n  title={Process-Supervised Reinforcement Learning for Code Generation},\n  author={Ye, Yufan and Zhang, Ting and Jiang, Wenbin and Huang, Hua},\n  booktitle={EMNLP},\n  year={2025}\n}\n\n@article{dreamprm2025code,\n  title={{DreamPRM-Code}: Function-as-Step Process Reward Model with Label Correction for {LLM} Coding},\n  author={Zhang, Ruiyi and Qin, Peijia and Cao, Qi and Xie, Pengtao},\n  journal={arXiv preprint arXiv:2512.15000},\n  year={2025}\n}\n\n% === Mutation Testing ===\n\n@inproceedings{jain2023contextual,\n  title={Contextual Predictive Mutation Testing},\n  author={Jain, Kush and Barik, Ristimoy and Le Goues, Claire},\n  booktitle={ESEC/FSE},\n  year={2023}\n}\n\n@article{wang2024llmmutation,\n  title={A Comprehensive Study on Large Language Models for Mutation Testing},\n  author={Wang, Bo and Chen, Mingda and Deng, Ming and Lin, Youfang and Harman, Mark and Papadakis, Mike and Zhang, Jie M.},\n  journal={ACM Transactions on Software Engineering and Methodology},\n  year={2025}\n}\n\n% === Code Generation Systems ===\n\n@techreport{alphacode2023team,\n  title={{AlphaCode} 2 Technical Report},\n  author={{AlphaCode Team}},\n  institution={Google DeepMind},\n  year={2023},\n  url={https://storage.googleapis.com/deepmind-media/AlphaCode2/AlphaCode2_Tech_Report.pdf}\n}\n\n\n@article{wei2022emergent,\n  author    = {Jason Wei and Yi Tay and Rishi Bommasani and Colin Raffel and Barret Zoph and Sebastian Borgeaud and Dani Yogatama and Maarten Bosma and Denny Zhou and Donald Metzler and Ed H. Chi and Tatsunori Hashimoto and Oriol Vinyals and Percy Liang and Jeff Dean and William Fedus},\n  title     = {Emergent Abilities of Large Language Models},\n  journal   = {Transactions on Machine Learning Research (TMLR)},\n  year      = {2022}\n}\n",
      "numLines": 617,
      "startLine": 1,
      "totalLines": 617
    }
  },
  "sourceToolAssistantUUID": "09311c21-3150-4808-a271-3dff225e9559",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-25T21:16:01.916Z_

<details><summary>↩ Tool result · `toolu_01LWRv4Bc6vFyG1N9boJuM1A`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0db9de0-e574-476a-9755-11c74b471b56",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "1eff071c-bdae-4d60-8227-9518b897dc04",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
    ],
    "durationMs": 52,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "d0db9de0-e574-476a-9755-11c74b471b56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-25T21:16:02.918Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GFbtBgsNHv8HLUa8bcgb5h`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_18/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1eff071c-bdae-4d60-8227-9518b897dc04",
  "isSidechain": false,
  "requestId": "req_011CbPyobMcCiRXTEiXrdwur",
  "type": "assistant",
  "uuid": "d7197b0d-00d2-454b-9dcd-daa6748061c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T63icej2nYZ7h5acEFp3yF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 256,
      "cache_read_input_tokens": 77644,
      "output_tokens": 1209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 256,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1209,
          "cache_read_input_tokens": 77644,
          "cache_creation_input_tokens": 256,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 256
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

_source line 76 · 2026-05-25T21:16:03.072Z_

<details><summary>↩ Tool result · `toolu_01GFbtBgsNHv8HLUa8bcgb5h`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 782286 May 25 21:11 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_18/submitted.pdf
PDF_EXISTS
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7197b0d-00d2-454b-9dcd-daa6748061c0",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "29cbe6df-0445-4768-a90c-cabb92919e0a",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 782286 May 25 21:11 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_18/submitted.pdf\nPDF_EXISTS",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d7197b0d-00d2-454b-9dcd-daa6748061c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-25T21:16:03.541Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QRuwhugmejS8DDGW3C4Li5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29cbe6df-0445-4768-a90c-cabb92919e0a",
  "isSidechain": false,
  "requestId": "req_011CbPyobMcCiRXTEiXrdwur",
  "type": "assistant",
  "uuid": "09311c21-3150-4808-a271-3dff225e9559",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T63icej2nYZ7h5acEFp3yF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 256,
      "cache_read_input_tokens": 77644,
      "output_tokens": 1209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 256,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1209,
          "cache_read_input_tokens": 77644,
          "cache_creation_input_tokens": 256,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 256
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

_source line 78_

```json
{
  "type": "last-prompt",
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: exec-sim-repair-verifier - 论文路径: projects/exec-sim-repair-verifier/docs/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: ARR (Main/Findings unified) - 截止日期: 2026-05-25 -…",
  "leafUuid": "009275db-8d49-4f4a-bb86-9d60f29911a6",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e"
}
```

---

### Runtime record

_source line 79_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper submission for EMNLP 2026",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e"
}
```

---

### Assistant

_source line 80 · 2026-05-25T21:16:06.950Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me also read the existing review_issues.yaml to understand prior issues.

Let me now read the existing review issues.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "009275db-8d49-4f4a-bb86-9d60f29911a6",
  "isSidechain": false,
  "requestId": "req_011CbPyqqxk3SQQ5ZPgy1EKj",
  "type": "assistant",
  "uuid": "24f99be9-1782-4fa0-8b6e-1ab77fa6aefa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018dmqWriyP56QtQChWbVsUa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11182,
      "cache_read_input_tokens": 77900,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11182,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 77900,
          "cache_creation_input_tokens": 11182,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11182
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

_source line 81 · 2026-05-25T21:16:08.660Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AtdrXAQqkT5zne98Th53NE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24f99be9-1782-4fa0-8b6e-1ab77fa6aefa",
  "isSidechain": false,
  "requestId": "req_011CbPyqqxk3SQQ5ZPgy1EKj",
  "type": "assistant",
  "uuid": "71831459-17d3-47f3-9ce4-f86fe1fbc408",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018dmqWriyP56QtQChWbVsUa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11182,
      "cache_read_input_tokens": 77900,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11182,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 77900,
          "cache_creation_input_tokens": 11182,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11182
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

_source line 82 · 2026-05-25T21:16:08.938Z_

<details><summary>↩ Tool result · `toolu_01AtdrXAQqkT5zne98Th53NE`</summary>

```text
1	# === Round 6 Issues (Original) ===
2	
3	# --- Round 6 Must-Fix (Consensus Critical) ---
4	
5	- id: "R6-N1"
6	  summary: "Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当"
7	  category: experiment
8	  severity: critical
9	  status: resolved
10	  first_raised_round: 6
11	  last_seen_round: 19
12	  mentions:
13	    - round: 6
14	      reviewers: [1, 2]
15	      note: "两人独立提出，最高共识。"
16	    - round: 7
17	      reviewers: [pre-review]
18	      note: "CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress."
19	    - round: 8
20	      reviewers: [1, 2]
21	      note: "Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp."
22	    - round: 9
23	      reviewers: [1, 2]
24	      note: "Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported."
25	    - round: 10
26	      reviewers: [1, 2]
27	      note: "Fresh review. R1-W2 re-raises seed coverage (2-3 seeds for repo-level). R2 agrees. Repo-level variance > function-level, claims read as definitive but only 2-3 observations."
28	    - round: 11
29	      reviewers: [1, 2]
30	      note: "Continue review. Both RESOLVED. §3.5 has explicit 'exploratory due to limited seed coverage' label. Failure mode taxonomy uses descriptive language. §3.7 reinforces 'definitive causal attribution requires multi-seed replication'. No causal claims in variant-level discussion."
31	    - round: 13
32	      reviewers: [1]
33	      note: "Fresh review R13. R1-W3 re-raises repo-level seed sparsity (some configs n=2). §3.5 exploratory label present. Director: resolved status maintained; R13 concern is about prominence of labeling, not missing disclosure."
34	    - round: 14
35	      reviewers: [1, 2]
36	      note: "Fresh review R14. R1-N2 re-raises. R2 REBUT 指出 R1 混淆两个统计模型。Director：resolved 维持。"
37	    - round: 15
38	      reviewers: [1, 2]
39	      note: "Fresh review R15. R1-W2 re-raises low power (~0.3, n_eff≈86). R2 AGREE 但补充论文已用 TOST+Bayesian ROPE+14B scaling 三重互补验证。Resolved 维持。"
40	    - round: 16
41	      reviewers: [1]
42	      note: "Fresh review R16. R1-N2 re-raises：2-3 seeds 无法支撑 18-26pp gap 的 formulation 归因。R2 隐含 AGREE（N2 scope 限制）。论文 §3.5 'exploratory' 标注仍在。"
43	    - round: 18
44	      reviewers: [1, 2]
45	      note: "Fresh review R18. R1-W1 re-raises：18-26pp 点估计但 CI 宽（~5pp 到 ~40pp），建议报告 CI 范围。R2 同意（N2）。论文 §3.5 exploratory 标注仍在。Resolved 维持。"
46	    - round: 19
47	      reviewers: [1, 2]
48	      note: "Fresh review R19. 两人共识 repo-level 2-3 seeds CI 宽度与点估计精度不匹配。§3.5 exploratory 标注到位。Resolved 维持。"
49	  action_items:
50	    - round: 6
51	      action: "补充至少 2-3 seeds repo-level 实验并报告 CI"
52	      assigned_to: "paper"
53	      status: resolved
54	    - round: 9
55	      action: "正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive"
56	      assigned_to: "paper"
57	      status: resolved
58	  resolution: "§3.5 开头标注 'Variant-level comparisons (n=48) are exploratory due to limited seed coverage'。后续讨论使用描述性语言，避免 causal claims。§3.7 强调 multi-seed replication needed。R11 两位 Reviewer 一致确认 RESOLVED。R13-R19 反复提及但无新增要求。"
59	  resolution_round: 11
60	
61	- id: "R6-N2"
62	  summary: "Checkpoint selection 系统性偏向 CLS"
63	  category: method
64	  severity: critical
65	  status: resolved
66	  first_raised_round: 6
67	  last_seen_round: 18
68	  mentions:
69	    - round: 6
70	      reviewers: [1, 2]
71	      note: "系统性偏差方向与 observed effect 一致。"
72	    - round: 7
73	      reviewers: [pre-review]
74	      note: "Reviewer 确认修复充分。"
75	    - round: 9
76	      reviewers: [1]
77	      note: "R1-W3 re-raises checkpoint inconsistency."
78	    - round: 10
79	      reviewers: [1]
80	      note: "R1 再次标为 CRITICAL。R2 REBUT。Director 降为 Should-Fix。"
81	    - round: 12
82	      reviewers: [1, 2]
83	      note: "R1-N2 升级为 critical。R2 完全 AGREE。"
84	    - round: 13
85	      reviewers: [1]
86	      note: "R1-W4 re-raises。R2 AGREE。Director resolved 维持。"
87	    - round: 14
88	      reviewers: [2]
89	      note: "R2-W1 re-raises s42 vs s123/s456 配置异质性。R1 AGREE。Director resolved 维持。"
90	    - round: 15
91	      reviewers: [1]
92	      note: "R1-W7 re-raises CWM checkpoint ablation 范围。R2 REBUT。Director resolved 维持。"
93	    - round: 18
94	      reviewers: [1, 2]
95	      note: "R18. R1-W2 re-raises NaN val-loss runs 用 final epoch 而 CLS 用 val-selected。R2 AGREE。已有 Appendix O 讨论。Resolved 维持。"
96	  action_items:
97	    - round: 6
98	      action: "CLS epoch ablation + matched epoch-3 解释"
99	      assigned_to: "paper"
100	      status: resolved
101	    - round: 9
102	      action: "解释 CWM NaN val loss 原因"
103	      assigned_to: "paper"
104	      status: resolved
105	    - round: 12
106	      action: "评估 Qwen3 CWM step 300-400 checkpoints 的 repo-level accuracy"
107	      assigned_to: "experiment"
108	      status: wont_fix
109	  resolution: "Step 300-400 checkpoints 未保存，但已找到现有 step-400 eval 数据（s42: 64.36%, 63.7% unparseable）。Format collapse 从训练早期即存在。"
110	  resolution_round: 12
111	
112	- id: "R6-N3"
113	  summary: "Oracle ensemble accuracy 数值矛盾"
114	  category: experiment
115	  severity: critical
116	  status: resolved
117	  first_raised_round: 6
118	  last_seen_round: 6
119	  resolution: "Oracle 90.63% 验证正确。96.03% 已删除。"
120	  resolution_round: 7
121	
122	- id: "R6-N4"
123	  summary: "Novelty 有限：核心贡献为比较已有 formulations，excitement 不足 main conference"
124	  category: framing
125	  severity: critical
126	  status: wont_fix
127	  first_raised_round: 6
128	  last_seen_round: 19
129	  mentions:
130	    - round: 6
131	      reviewers: [1, 2]
132	      note: "R1 建议 function-level equivalence 作为 headline。"
133	    - round: 10
134	      reviewers: [1, 2]
135	      note: "两人共识：Findings 合适，Main 不够。"
136	    - round: 12
137	      reviewers: [1, 2]
138	      note: "R2 Excitement 2/5, R1 Excitement 3/5。"
139	    - round: 13
140	      reviewers: [1, 2]
141	      note: "两人 Excitement 均为 3/5。"
142	    - round: 15
143	      reviewers: [1, 2]
144	      note: "R1 Excitement 3/5, R2 Excitement 2.5/5。"
145	    - round: 16
146	      reviewers: [1, 2]
147	      note: "Fresh review R16. R1 Excitement 3/5, R2 Excitement 3/5。核心发现可预测性限制新颖性。wont_fix 维持。"
148	    - round: 17
149	      reviewers: [1, 2]
150	      note: "Fresh review R17. R1 Excitement 3/5, R2 Excitement 2.5/5。R2 明确判定 Findings 而非 main conference。wont_fix 维持。"
151	    - round: 18
152	      reviewers: [1, 2]
153	      note: "Fresh review R18. R1 Excitement 3/5, R2 Excitement 2.5/5。R1 反驳'直观可预期'但同意缺少干预闭环。R2 维持 Findings 判定。分歧在于 empirical comparison paper 的 novelty 标准。wont_fix 维持。"
154	    - round: 19
155	      reviewers: [1, 2]
156	      note: "Fresh review R19. R1 3.5 vs R2 3.0——分歧仍在 novelty 标准。R2 认为核心发现方向可预测，R1 认为 rigorous methodology + failure taxonomy 有独立价值。两人共识 Findings 区间。wont_fix 维持。"
157	  resolution: "Excitement 稳定在 2.5-3.0/5，核心贡献类型（empirical comparison）无法通过修改改变。"
158	  resolution_round: 11
159	
160	# --- Round 6 Should-Fix ---
161	
162	- id: "R6-W1"
163	  summary: "SESOI ±2pp 的 a priori 属性值得商榷"
164	  category: method
165	  severity: warning
166	  status: resolved
167	  first_raised_round: 6
168	  last_seen_round: 18
169	  mentions:
170	    - round: 9
171	      reviewers: [1, 2]
172	      note: "两人独立 re-raise。"
173	    - round: 12
174	      reviewers: [1, 2]
175	      note: "R1-W1 re-raises：无 pre-registration。"
176	    - round: 15
177	      reviewers: [1, 2]
178	      note: "R1-W1 标 Must-Fix。R2 AGREE 部分。共识：Table 13 应移入正文。Resolved 维持。"
179	    - round: 16
180	      reviewers: [1]
181	      note: "R1-W1 re-raises：缺乏正式论证。但论文已诚实披露 post-hoc 状态并提供 sensitivity analysis。Resolved 维持。"
182	    - round: 17
183	      reviewers: [1, 2]
184	      note: "R1-W4 re-raises：SESOI 应基于 downstream 实践意义（repair@K 影响），论文未提供此分析。R2 AGREE with nuance——±2pp 是合理 convention 但增加实践论证更好。Resolved 维持。"
185	    - round: 18
186	      reviewers: []
187	      note: "R18 未单独提及。Resolved 维持。"
188	  resolution: "§3.4 已改为 'motivated by domain considerations but was not pre-registered'；Bayesian ROPE 提供独立佐证。"
189	  resolution_round: 12
190	
191	- id: "R6-W2"
192	  summary: "CWM regime qualifier 不充分——Abstract/Conclusion 缺少 ≤8B LoRA 限定"
193	  category: framing
194	  severity: warning
195	  status: resolved
196	  first_raised_round: 6
197	  last_seen_round: 19
198	  mentions:
199	    - round: 10
200	      reviewers: [1, 2]
201	      note: "Abstract 已有 '≤8B LoRA protocol'，Conclusion 加入限定。"
202	    - round: 16
203	      reviewers: [1, 2]
204	      note: "Fresh review R16. R2-N2 re-raises：标题仍暗示通用性。R1 AGREE 但程度略轻。Abstract 已有限定词但标题无。建议标题加 scope 限定。"
205	    - round: 18
206	      reviewers: [1, 2]
207	      note: "R18. R1 反驳'严重限制'但同意标题可限定。R2 维持。Abstract/Conclusion 限定已到位。Resolved 维持。"
208	    - round: 19
209	      reviewers: [1, 2]
210	      note: "R19. R2 持续关注标题泛化。R1 反驳：2 families 已超出同类论文，systematic 指方法论。Abstract/Conclusion 限定到位。Resolved 维持。"
211	  resolution: "Abstract + Conclusion 均已加入 ≤8B LoRA 限定。标题是否需要修改由 Research Director 决定。"
212	  resolution_round: 10
213	
214	- id: "R6-W3"
215	  summary: "Re-repair δ=0 与 diagnostic granularity 矛盾"
216	  category: framing
217	  severity: warning
218	  status: resolved
219	  first_raised_round: 6
220	  last_seen_round: 7
221	  resolution: "Contributions 4→3, diagnostic granularity 降级为 pending validation."
222	  resolution_round: 7
223	
224	- id: "R6-W4"
225	  summary: "TRAJ 训练配置差异——label granularity + data composition 混淆"
226	  category: experiment
227	  severity: warning
228	  status: resolved
229	  first_raised_round: 6
230	  last_seen_round: 19
231	  mentions:
232	    - round: 12
233	      reviewers: [1, 2]
234	      note: "downsample 控制了 volume 但未控制 label granularity。"
235	    - round: 14
236	      reviewers: [1, 2]
237	      note: "Director 裁定 Should-Fix（降级）。"
238	    - round: 15
239	      reviewers: [1, 2]
240	      note: "Abstract 已有 'the TRAJ comparison is inherently confounded'。"
241	    - round: 16
242	      reviewers: [1, 2]
243	      note: "R2-W1 re-raises TRAJ 与 CLS/CWM 比较性质不同。R1 AGREE：应视觉区分 controlled vs observational comparison。Resolved 维持——Abstract 和 §3.5 均有 confound 标注。"
244	    - round: 17
245	      reviewers: [1, 2]
246	      note: "R1-N1 升级为 Must-Fix。原以为 175× data volume asymmetry，实际核实后 function-level TRAJ 有 8,052 训练 variants（CLS 仅 3,596 unique variants）——TRAJ 反而有 2.24× 更多 unique variants。Repo-level: ~70K vs 386 variants 仍有显著不对称。Confound 重新定性为 label granularity（非 data volume）。CLS@400 极端下采样实验进行中。"
247	    - round: 18
248	      reviewers: [1, 2]
249	      note: "R18. R1-N2 标 Must-Fix（100x 数据量 + 4x 学习率 + label granularity）。R2 部分同意但降为 Should-Fix——downsample ablation 和 function-level 近等价已部分缓解。建议补充 TRAJ@5e-5 消融。Resolved 维持——Abstract 'inherently confounded' + §3.1 显式配置说明 + §3.5 confound 讨论均已到位。"
250	    - round: 19
251	      reviewers: [1, 2]
252	      note: "R19. R1 标 Must-Fix（R1-N1），R2 同意问题存在但降为 Should-Fix。~100× 数据量 + 4× 学习率 + label granularity 差异使 CLS-TRAJ 属 observational comparison。缓解：downsample ablation + function-level 等价 + Abstract 'inherently confounded'。Director 采纳 Should-Fix。Resolved 维持。"
253	  resolution: "§3.1 增加 M1 显式句子（8,052 vs 15,290, 2.24× more unique variants, confounded by label granularity and data composition）。§3.5 repo-level confound 讨论保留。Abstract 'inherently confounded' 保留。"
254	  resolution_round: 17
255	
256	- id: "R6-W5"
257	  summary: "Interaction 未做统计检验"
258	  category: method
259	  severity: warning
260	  status: resolved
261	  first_raised_round: 6
262	  last_seen_round: 8
263	  resolution: "Interaction test z=-23.7 完成。"
264	  resolution_round: 9
265	
266	- id: "R6-W6"
267	  summary: "合成 mutation 外部效度"
268	  category: experiment
269	  severity: warning
270	  status: resolved
271	  first_raised_round: 6
272	  last_seen_round: 18
273	  mentions:
274	    - round: 16
275	      reviewers: [1]
276	      note: "R1-W5 re-raises：synthetic mutation vs real developer patch 分布差异。Limitations 已提及但讨论不深。Resolved 维持。"
277	    - round: 17
278	      reviewers: [1, 2]
279	      note: "R1-W1 + R2-W3 re-raises。单基准(SWE-bench)/单语言(Python)/合成 mutation 限制泛化性。R1 补充：mutation data 可能系统性偏向特定 formulation——CLS 对 mutation 类型更 robust，CWM 在合成 mutation 简单输出上表现可能被高估。此方向性 confound 论文未讨论。Resolved 维持——Limitations 已提及。"
280	    - round: 18
281	      reviewers: [2]
282	      note: "R2-Q4 问为何不使用其他 repo-level benchmark。论文使用 SWE-bench Verified 是领域标准。Resolved 维持。"
283	  resolution: "Appendix Extended Validity Discussion 讨论充分。Limitations 已提及 Python-only 和 codegen 限制。"
284	  resolution_round: 7
285	
286	- id: "R6-W7"
287	  summary: "Abstract 偏短 (~120-130 词)"
288	  category: writing
289	  severity: warning
290	  status: resolved
291	  first_raised_round: 6
292	  last_seen_round: 7
293	  resolution: "~185 词，合规。"
294	  resolution_round: 7
295	
296	- id: "R6-W8"
297	  summary: "遗漏近期相关工作"
298	  category: writing
299	  severity: warning
300	  status: resolved
301	  first_raised_round: 6
302	  last_seen_round: 10
303	  resolution: "CodeRM, CodeScaler, GenPRM 等均已加入 Related Work。"
304	  resolution_round: 10
305	
306	# --- Round 6 Minor ---
307	
308	- id: "R6-M1"
309	  summary: "Tables 缺少次优下划线"
310	  category: format
311	  severity: info
312	  status: resolved
313	  first_raised_round: 6
314	  last_seen_round: 18
315	  mentions:
316	    - round: 18
317	      reviewers: [1]
318	      note: "R1-M1 re-raises Table 1/2 缺乏 bold/underline 标注最优 formulation。但论文 Table 1/2 已有 bold 和 underline（检查确认）。Resolved 维持。"
319	  resolution: "Tables 1-3 bold+underline 完成。"
320	  resolution_round: 7
321	
322	- id: "R6-M2"
323	  summary: "Checklist C4 version numbers"
324	  category: format
325	  severity: info
326	  status: resolved
327	  first_raised_round: 6
328	  last_seen_round: 7
329	  resolution: "C4 已列出版本号。"
330	  resolution_round: 7
331	
332	- id: "R6-M3"
333	  summary: "Figure 2 信息密度偏低 / y-axis 截断"
334	  category: format
335	  severity: info
336	  status: resolved
337	  first_raised_round: 6
338	  last_seen_round: 19
339	  mentions:
340	    - round: 18
341	      reviewers: [1]
342	      note: "R1-M2 re-raises y-axis 截断可能夸大视觉差异。论文 caption 已标注 'y-axis does not start at zero'。Resolved 维持。"
343	    - round: 19
344	      reviewers: [1]
345	      note: "R19 提及。Caption disclosure 到位。Resolved 维持。"
346	  resolution: "Figure 2 caption 标注 'y-axis does not start at zero'。"
347	  resolution_round: 11
348	
349	# === Round 8 Issues ===
350	
351	- id: "R8-C1"
352	  summary: "TOST p=0.007 归属混淆"
353	  category: experiment
354	  severity: critical
355	  status: resolved
356	  first_raised_round: 8
357	  last_seen_round: 10
358	  resolution: "§3.4 分开呈现。"
359	  resolution_round: 10
360	
361	- id: "R8-C2"
362	  summary: "Abstract 对 repo-level CWM 结论缺少 regime qualifier + z=-23.7 缺 model 标注"
363	  category: framing
364	  severity: critical
365	  status: resolved
366	  first_raised_round: 8
367	  last_seen_round: 10
368	  resolution: "Abstract qualifier 和 model 标注已加入。"
369	  resolution_round: 10
370	
371	- id: "R8-W1"
372	  summary: "n=48 variant 样本量导致 TOST 统计功效不足"
373	  category: experiment
374	  severity: warning
375	  status: resolved
376	  first_raised_round: 8
377	  last_seen_round: 19
378	  mentions:
379	    - round: 10
380	      reviewers: [1, 2]
381	      note: "R1-N2 标 CRITICAL：TOST power ~0.3。"
382	    - round: 11
383	      reviewers: [1, 2]
384	      note: "Both RESOLVED."
385	    - round: 12
386	      reviewers: [1, 2]
387	      note: "R1-N3 re-raises."
388	    - round: 15
389	      reviewers: [1, 2]
390	      note: "R1-W2 标 Must-Fix。R2 AGREE 但补充 Bayesian ROPE 不受 power 限制。Resolved 维持。"
391	    - round: 16
392	      reviewers: [1, 2]
393	      note: "R1-N1 标 Critical：CLS-TRAJ power ~0.3 使该比较 uninformative，Abstract 'not confirmed' 可能 mislead。R2-W1 AGREE。论文 §3.4 已有 power paragraph + 'at current power (~0.3)' 限定。Resolved 维持。"
394	    - round: 17
395	      reviewers: [1, 2]
396	      note: "R1-N2 升级为 Must-Fix。power ~0.3 使 CLS-TRAJ 比较 inconclusive（非 directional evidence）。R2 完全 AGREE 并建议 'not confirmed' 改为 'inconclusive'。建议增加 MDE 表格。Repo-level 2-3 seeds 功效更低。Resolved 维持——§3.4 已有 power paragraph。"
397	    - round: 18
398	      reviewers: [1]
399	      note: "R18. R1-W1 re-raises repo-level 2-3 seeds power 不足。与 R6-N1 一致。Resolved 维持。"
400	    - round: 19
401	      reviewers: [1, 2]
402	      note: "R19. 隐含于 SF3（seed coverage）。§3.4 power paragraph + 'inconclusive' 术语 + Bayesian ROPE 均到位。Resolved 维持。"
403	  resolution: "§3.4 已扩写 power paragraph，14B TOST 完成。Abstract 已加 'at current power (~0.3)' 限定。"
404	  resolution_round: 12
405	
406	- id: "R8-W2"
407	  summary: "Oracle 互补性估计为单种子、无置信区间"
408	  category: experiment
409	  severity: warning
410	  status: resolved
411	  first_raised_round: 8
412	  last_seen_round: 10
413	  resolution: "Cross-seed oracle 已加入正文。"
414	  resolution_round: 10
415	
416	- id: "R8-W3"
417	  summary: "CWM checkpoint 消融不对称——Qwen3 缺 early-stopping 评估"
418	  category: experiment
419	  severity: warning
420	  status: resolved
421	  first_raised_round: 8
422	  last_seen_round: 10
423	  resolution: "Appendix 已讨论。"
424	  resolution_round: 10
425	
426	- id: "R8-W4"
427	  summary: "z=-23.7 interaction 仅基于 DeepSeek-Coder"
428	  category: framing
429	  severity: warning
430	  status: resolved
431	  first_raised_round: 8
432	  last_seen_round: 10
433	  resolution: "Abstract 已标注 model。"
434	  resolution_round: 10
435	
436	- id: "R8-W5"
437	  summary: "遗漏 GenRM / RepoExec"
438	  category: writing
439	  severity: warning
440	  status: resolved
441	  first_raised_round: 8
442	  last_seen_round: 10
443	  resolution: "GenRM, CodeScaler, GenPRM 已加入。"
444	  resolution_round: 10
445	
446	- id: "R8-W6"
447	  summary: "CWM baseline 偏弱 (≤8B LoRA vs 原始 32B)"
448	  category: method
449	  severity: warning
450	  status: resolved
451	  first_raised_round: 8
452	  last_seen_round: 19
453	  mentions:
454	    - round: 10
455	      reviewers: [1, 2]
456	      note: "R2-N2 标 CRITICAL。"
457	    - round: 14
458	      reviewers: [1, 2]
459	      note: "Director 裁定 Should-Fix（降级）。"
460	    - round: 15
461	      reviewers: [1, 2]
462	      note: "R2-N2 标 Must-Fix。R1 REBUT matched design 方法论价值。Resolved 维持。"
463	    - round: 16
464	      reviewers: [1, 2]
465	      note: "R2-N2 re-raises scope limitation。R1 AGREE 标题应加限定。Resolved 维持——所有 qualifier 已到位。"
466	    - round: 18
467	      reviewers: [1, 2]
468	      note: "R18. R2-N2 re-raises 实验规模限制。R1 反驳——2 families 已超出同类论文常规。Resolved 维持。"
469	    - round: 19
470	      reviewers: [1, 2]
471	      note: "R19. 隐含于 SF6（scope limitation）。R1 反驳 2 families 超出常规。Resolved 维持。"
472	  resolution: "Abstract + Conclusion 均已加入 ≤8B LoRA 限定。14B 验证实验完成。"
473	  resolution_round: 10
474	
475	- id: "R8-W7"
476	  summary: "Novelty 是否足够 Conference 水平"
477	  category: framing
478	  severity: warning
479	  status: wont_fix
480	  first_raised_round: 8
481	  last_seen_round: 13
482	  resolution: "合并至 R6-N4。Inherent limitation。"
483	  resolution_round: 11
484	
485	# --- Round 8 Minor ---
486	
487	- id: "R8-M1"
488	  summary: "混合精度 (bfloat16/NF4) 对 TOST 的影响"
489	  category: method
490	  severity: info
491	  status: resolved
492	  first_raised_round: 8
493	  last_seen_round: 10
494	  resolution: "§3.4 footnote 充分讨论。"
495	  resolution_round: 10
496	
497	- id: "R8-M2"
498	  summary: "LPM 未报告 robust SEs; prompt templates 未展示"
499	  category: format
500	  severity: info
501	  status: resolved
502	  first_raised_round: 8
503	  last_seen_round: 16
504	  mentions:
505	    - round: 16
506	      reviewers: [1]
507	      note: "R1-W6 re-raises LPM vs GEE 不一致（model identity p=0.002 vs p=0.449）。论文 Appendix M 已有 estimator-dependent 标注和 cluster 数限制讨论。Resolved 维持。"
508	  resolution: "Appendix M 补充 GEE logistic regression + estimator-dependent 标注。"
509	  resolution_round: 11
510	
511	# === Round 9-12 Issues (all resolved, abbreviated) ===
512	
513	- id: "R9-C1"
514	  summary: "'Design space' framing 过度"
515	  category: framing
516	  severity: critical
517	  status: resolved
518	  first_raised_round: 9
519	  last_seen_round: 10
520	  resolution: "标题已改为 Systematic Comparison。"
521	  resolution_round: 10
522	
523	- id: "R9-W1"
524	  summary: "CWM 评估指标非对称性"
525	  category: method
526	  severity: warning
527	  status: resolved
528	  first_raised_round: 9
529	  last_seen_round: 10
530	  resolution: "R2 REBUT 成功：relaxed matching 扩大 gap。"
531	  resolution_round: 10
532	
533	- id: "R9-W2"
534	  summary: "DeepSeek 仅 2 seeds 却声称 'model-dependent'"
535	  category: framing
536	  severity: warning
537	  status: resolved
538	  first_raised_round: 9
539	  last_seen_round: 16
540	  mentions:
541	    - round: 16
542	      reviewers: [1]
543	      note: "R1-W3 re-raises DeepSeek 仅 2 seeds，跨模型比较可信度降低。Resolved 维持——§3.4 已有 caveat。"
544	  resolution: "Abstract 改为更审慎措辞。"
545	  resolution_round: 10
546	
547	- id: "R12-N1"
548	  summary: "CWM baseline 生态效度：≤8B LoRA vs 原始 CWM 32B"
549	  category: method
550	  severity: critical
551	  status: resolved
552	  first_raised_round: 12
553	  last_seen_round: 15
554	  resolution: "Introduction §1 已加 'under our ≤8B LoRA protocol' 限定。14B function-level 收敛提供间接支持。"
555	  resolution_round: 12
556	
557	- id: "R12-N3"
558	  summary: "CLS-TRAJ 等价性不对称结论可能是 power ~0.3 artifact"
559	  category: method
560	  severity: critical
561	  status: resolved
562	  first_raised_round: 12
563	  last_seen_round: 13
564	  resolution: "§3.4 power paragraph 扩写，14B TOST 完成。"
565	  resolution_round: 12
566	
567	- id: "R12-W2"
568	  summary: "GenRM 对比发现未充分讨论"
569	  category: framing
570	  severity: warning
571	  status: resolved
572	  first_raised_round: 12
573	  last_seen_round: 19
574	  mentions:
575	    - round: 16
576	      reviewers: [1, 2]
577	      note: "R2-W4 re-raises：跨领域 code vs math GenRM 比较分析浅薄。R1 AGREE 但认为超出本文 scope。Resolved 维持——Conclusion 已有 GenRM 段落。"
578	    - round: 18
579	      reviewers: [1, 2]
580	      note: "R18. R1-M4 + R2-W4：GenRM domain contrast 是最有 novelty 潜力的观点但仅 Conclusion 一句话。双方共识应展开讨论。Resolved 维持但建议 rebuttal 展开。"
581	    - round: 19
582	      reviewers: [1, 2]
583	      note: "R19. 两人强烈共识 GenRM domain contrast 被严重低估（SF4）。Code domain 的 exact match 严格性和 output space 结构化程度等机制未展开。Conclusion 仍仅一句话。Resolved 维持但作为最有影响力的改进方向。"
584	  resolution: "Conclusion 新增 GenRM domain-specificity 段落。"
585	  resolution_round: 12
586	
587	- id: "R13-N1"
588	  summary: "Appendix 'P: Limitations' 标题可能违反 EMNLP 格式规则"
589	  category: format
590	  severity: critical
591	  status: resolved
592	  first_raised_round: 13
593	  last_seen_round: 13
594	  resolution: "Appendix P 重命名为 'Extended validity discussion'。"
595	  resolution_round: 13
596	
597	- id: "R13-W1"
598	  summary: "Abstract/Conclusion 中 TRAJ 'not confirmed' 措辞在 power ~0.3 下 over-stated"
599	  category: framing
600	  severity: warning
601	  status: resolved
602	  first_raised_round: 13
603	  last_seen_round: 18
604	  mentions:
605	    - round: 18
606	      reviewers: [1, 2]
607	      note: "R18. R1 同意 Abstract 中 'all three formulations achieve comparable accuracy' 表述过强。建议改为 'CLS and CWM achieve statistical equivalence; TRAJ parity is model-dependent'。"
608	  resolution: "Abstract 加入 'at current power (~0.3)' 限定语。R17 将 'not confirmed' 改为 'inconclusive'。"
609	  resolution_round: 13
610	
611	- id: "R13-W2"
612	  summary: "Oracle 互补性应重新框定为 negative result + motivation，而非独立正面贡献"
613	  category: framing
614	  severity: warning
615	  status: resolved
616	  first_raised_round: 13
617	  last_seen_round: 19
618	  mentions:
619	    - round: 16
620	      reviewers: [1, 2]
621	      note: "R2-W2 re-raises：error complementarity 被高估。R1 AGREE 应降级为 exploratory finding。论文 §1 Contribution 2 已重写为 negative result framing。Resolved 维持。"
622	    - round: 17
623	      reviewers: [1, 2]
624	      note: "R1-W3 + R2-W2 re-raises。Oracle gap 大但 heuristic <0.4pp，Conclusion routing 方向过于乐观。§1 Contribution 2 权重过大。R2 补充：互补性存在有价值但不应列为主要贡献。Resolved 维持。"
625	    - round: 18
626	      reviewers: [1, 2]
627	      note: "R18. R1 同意 complementarity overclaim——oracle 90.63% 但 simple heuristics <0.4pp，oracle-to-achievable gap 过大。R2 同意。§1 已合并为 Contribution #1 子句。Resolved 维持。"
628	    - round: 19
629	      reviewers: [1, 2]
630	      note: "R19. 两人共识 oracle-to-achievable gap 过大（SF5）。§3.6 和 Conclusion routing 表述仍偏乐观。Resolved 维持。"
631	  resolution: "Introduction Contribution 2 重写为 negative result framing。R17 合并为 Contribution #1 子句。"
632	  resolution_round: 13
633	
634	- id: "R13-W3"
635	  summary: "14B 'capacity-dependent convergence' claim 证据不足——仅 1 model family, 3 seeds"
636	  category: experiment
637	  severity: warning
638	  status: resolved
639	  first_raised_round: 13
640	  last_seen_round: 17
641	  resolution: "Abstract 和 Conclusion 已有 'preliminary observation' + 'single family' 限定。"
642	  resolution_round: 13
643	
644	- id: "R13-W4"
645	  summary: "GenRM 领域特异性对比分析不充分"
646	  category: framing
647	  severity: warning
648	  status: resolved
649	  first_raised_round: 13
650	  last_seen_round: 19
651	  mentions:
652	    - round: 16
653	      reviewers: [1, 2]
654	      note: "R2-W4 re-raises。R1 AGREE 但认为超出 scope。Resolved 维持。"
655	    - round: 18
656	      reviewers: [1, 2]
657	      note: "R18. 双方共识 GenRM domain contrast 应展开——code domain 的 exact match 严格性和 output space 结构化程度可能是关键差异。建议 Conclusion 或 §4 增加讨论。"
658	    - round: 19
659	      reviewers: [1, 2]
660	      note: "R19. 与 R12-W2 一致。强烈共识应展开。"
661	  resolution: "Conclusion 扩展 GenRM 对比。"
662	  resolution_round: 13
663	
664	# === Round 16 New Issues ===
665	
666	- id: "R16-N1"
667	  summary: "Complexity-dependent 核心叙事存在 complexity 与 output format/length 的未解耦混淆"
668	  category: framing
669	  severity: critical
670	  status: resolved
671	  first_raised_round: 16
672	  last_seen_round: 16
673	  mentions:
674	    - round: 16
675	      reviewers: [1, 2]
676	      note: "R2-N1 提出，R1 完全 AGREE。论文将 function→repo 分歧归因于 'code complexity'，但 format collapse（53-74% unparseable）更直接指向 output format/length 效应。四种 intervention 均未攻击 output length 本身（如 constrained decoding）。核心 narrative 框架需修正。两位 Reviewer 共识。"
677	  action_items:
678	    - round: 16
679	      action: "Introduction 核心 claim 增加 mechanistic pathway：'formulation choice is moderated by code complexity, operating through output format'，明确 function ~5-15 tokens vs repo ~477 tokens 的 output length 差异是直接机制"
680	      assigned_to: "paper"
681	      status: resolved
682	  resolution: "Introduction §1 核心 claim 增加 mechanistic pathway 解释。"
683	  resolution_round: 16
684	
685	- id: "R16-N2"
686	  summary: "≤8B LoRA 范围限制下标题和 abstract 泛化声明过广"
687	  category: framing
688	  severity: critical
689	  status: wont_fix
690	  first_raised_round: 16
691	  last_seen_round: 19
692	  mentions:
693	    - round: 16
694	      reviewers: [1, 2]
695	      note: "R2-N2 提出，R1 AGREE。标题 'A Systematic Comparison...' 暗示通用性，但实际仅覆盖 2 families × ≤8B × LoRA。"
696	    - round: 17
697	      reviewers: [1, 2]
698	      note: "R2-N1 re-raises。R1 AGREE with nuance——'systematic' 可指方法论系统性而非穷举性。wont_fix 维持。"
699	    - round: 18
700	      reviewers: [1, 2]
701	      note: "R18. R2-N2 re-raises。R1 反驳'严重限制'——2 families 已超出同类论文，LoRA-only 是合理控制变量选择。但同意标题可略加限定。wont_fix 维持——Abstract 限定已到位。"
702	    - round: 19
703	      reviewers: [1, 2]
704	      note: "R19. SF6——R2 持续关注，R1 部分同意。Abstract 限定到位。wont_fix 维持。"
705	  resolution: "Rebuttal material。Abstract 已有 '≤8B LoRA fine-tuning' 限定。标题修改由 Research Director 决定。"
706	  resolution_round: 16
707	
708	- id: "R16-W1"
709	  summary: "统计方法多样但主次层次不清"
710	  category: method
711	  severity: warning
712	  status: resolved
713	  first_raised_round: 16
714	  last_seen_round: 16
715	  resolution: "§3.1 Statistics 段落增加统计层次声明。"
716	  resolution_round: 16
717	
718	- id: "R16-W2"
719	  summary: "CWM format collapse 的定性归因不清：inherent formulation limitation vs engineering artifact"
720	  category: method
721	  severity: warning
722	  status: resolved
723	  first_raised_round: 16
724	  last_seen_round: 19
725	  mentions:
726	    - round: 16
727	      reviewers: [1]
728	      note: "R1-W4 提出。53-74% unparseable + default to majority class。四种 interventions 失败但未测试 constrained decoding。"
729	    - round: 17
730	      reviewers: [1, 2]
731	      note: "R1-W2 re-raises。14B gap 收窄到 1.07pp 与 'inherent limitation' 归因存在叙事张力。R2 AGREE。Resolved 维持。"
732	    - round: 18
733	      reviewers: [1, 2]
734	      note: "R18. R1-N1 标 Must-Fix——constrained decoding 未测试使 'formulation-inherent' 归因不稳固。R2 REBUT——Appendix (c) 的间接证据（CWM 误训 CLS-format 数据 → 86.05% + 0% unparseable; parseable CWM 仅 38-43%）已证明 format compliance ≠ semantic accuracy，constrained decoding 即使消除 format collapse 也不改变核心结论。但 R2 同意 Appendix (c) 证据应提升到正文。Director 裁定 Should-Fix：间接证据充分但正文可见度不足。"
735	    - round: 19
736	      reviewers: [1, 2]
737	      note: "R19. SF2——两人共识 constrained decoding 未测试是明确 gap。Appendix (c) 间接证据到位，Limitations 已引用 Synchromesh/XGrammar/Outlines（R18 修复），§3.6 提及 Appendix (c)。但正文可见度仍不足——关键证据仍在 Appendix。Resolved 维持。"
738	  action_items:
739	    - round: 18
740	      action: "将 Appendix (c) 的 CWM 误训实验和 parseable-only accuracy 证据提升到 §3.5 或 §3.6 正文"
741	      assigned_to: "paper"
742	      status: resolved
743	  resolution: "Limitations §8 已有 constrained decoding 讨论。N1 mechanistic pathway 修复间接回应了归因问题。R18 建议将 Appendix (c) 关键证据提升到正文。Limitations 已引用 3 篇 constrained decoding 文献。"
744	  resolution_round: 16
745	
746	- id: "R16-M1"
747	  summary: "'pp' 缩写首次使用未定义"
748	  category: writing
749	  severity: info
750	  status: resolved
751	  first_raised_round: 16
752	  last_seen_round: 16
753	  resolution: "Introduction §1 首次出现处改为 'percentage points (pp)'。"
754	  resolution_round: 16
755	
756	- id: "R16-M2"
757	  summary: "DeepSeek-Coder 2 seeds 的 CI/std 在 Table 1 中未报告"
758	  category: format
759	  severity: info
760	  status: wont_fix
761	  first_raised_round: 16
762	  last_seen_round: 16
763	  resolution: "Table 1 caption 已改为显式注明 seed 数量。"
764	  resolution_round: 16
765	
766	- id: "R16-M3"
767	  summary: "Figure 1 字体偏小，接近可读性下限"
768	  category: format
769	  severity: info
770	  status: wont_fix
771	  first_raised_round: 16
772	  last_seen_round: 16
773	  resolution: "当前字体大小在 ACL 论文中属正常范围。"
774	  resolution_round: 16
775	
776	# === Round 17 New Issues ===
777	
778	- id: "R17-W1"
779	  summary: "核心发现可预测性未被讨论——complexity moderates formulation choice 方向直觉可预期"
780	  category: framing
781	  severity: warning
782	  status: resolved
783	  first_raised_round: 17
784	  last_seen_round: 19
785	  mentions:
786	    - round: 18
787	      reviewers: [1, 2]
788	      note: "R18. R2-N1 re-raises 核心发现可预测性。R1 反驳——TRAJ 等价是反直觉的，failure taxonomy 不可先验推导。但 R1 同意缺少干预闭环。§3.5 已增加 predictability sentence。Resolved 维持。"
789	    - round: 19
790	      reviewers: [1, 2]
791	      note: "R19. 两人共识核心发现方向可预测（Reviewer Consensus #7）。R1 辩护 TRAJ 等价和 failure taxonomy 细节不可先验推导。分歧在 novelty 评估。Resolved 维持。"
792	  resolution: "§3.5 增加 predictability discussion。"
793	  resolution_round: 17
794	
795	- id: "R17-W2"
796	  summary: "Conclusion scope 未标注 ≤8B LoRA 限定"
797	  category: framing
798	  severity: warning
799	  status: resolved
800	  first_raised_round: 17
801	  last_seen_round: 17
802	  resolution: "Conclusion 首句改为 '...under ≤8B LoRA fine-tuning'。"
803	  resolution_round: 17
804	
805	- id: "R17-W3"
806	  summary: "Format collapse 描述缺少 training regime 限定"
807	  category: framing
808	  severity: warning
809	  status: resolved
810	  first_raised_round: 17
811	  last_seen_round: 17
812	  resolution: "§3.6 改为 '...under our ≤8B LoRA protocol'。"
813	  resolution_round: 17
814	
815	- id: "R17-W4"
816	  summary: "Contribution #2 (Error complementarity) 权重过大，应合并入 Contribution #1"
817	  category: framing
818	  severity: warning
819	  status: resolved
820	  first_raised_round: 17
821	  last_seen_round: 17
822	  resolution: "Introduction Contribution #2 合并入 #1 作为子句。"
823	  resolution_round: 17
824	
825	- id: "R17-N2-write"
826	  summary: "'not confirmed' 应改为 'inconclusive'——TOST 标准术语"
827	  category: writing
828	  severity: warning
829	  status: resolved
830	  first_raised_round: 17
831	  last_seen_round: 17
832	  resolution: "全文替换为 'inconclusive'。"
833	  resolution_round: 17
834	
835	- id: "R17-N3-write"
836	  summary: "14B 在 abstract/conclusion 叙事权重与 3 seeds/单家族证据不匹配"
837	  category: framing
838	  severity: warning
839	  status: resolved
840	  first_raised_round: 17
841	  last_seen_round: 17
842	  resolution: "Abstract 改为 'Preliminary 14B results (3 seeds, single family) suggest the gap may narrow at larger scale'。"
843	  resolution_round: 17
844	
845	- id: "R17-M1"
846	  summary: "TRAJ 训练配置差异仅在 table footnote 中说明，应为显式句子"
847	  category: writing
848	  severity: info
849	  status: resolved
850	  first_raised_round: 17
851	  last_seen_round: 17
852	  resolution: "§3.1 增加 TRAJ 配置显式说明。"
853	  resolution_round: 17
854	
855	- id: "R17-M3"
856	  summary: "CWM 术语与 RL world models 混淆——缺少辨析脚注"
857	  category: writing
858	  severity: info
859	  status: resolved
860	  first_raised_round: 17
861	  last_seen_round: 17
862	  resolution: "§2.1 CWM 段增加辨析脚注。"
863	  resolution_round: 17
864	
865	- id: "R17-M4"
866	  summary: "DreamPRM/CodePRM 仅列举引用，未展开讨论差异"
867	  category: writing
868	  severity: info
869	  status: resolved
870	  first_raised_round: 17
871	  last_seen_round: 17
872	  resolution: "Related Work 展开 DreamPRM/CodePRM 讨论。"
873	  resolution_round: 17
874	
875	# === Round 18 New Issues ===
876	
877	- id: "R18-W1"
878	  summary: "Re-repair 实验样本量不一致（n=44 vs n=14）且结论过强"
879	  category: experiment
880	  severity: warning
881	  status: resolved
882	  first_raised_round: 18
883	  last_seen_round: 18
884	  mentions:
885	    - round: 18
886	      reviewers: [1]
887	      note: "R1-W3 提出。Appendix I(j) 说 n=44 但后文出现 n=14。power ~0.3 不支撑 'does not translate' 结论。R2 部分同意。"
888	  action_items:
889	    - round: 18
890	      action: "澄清 n=44 vs n=14 不一致；将结论弱化为 'we found no evidence of benefit, but the study was underpowered'"
891	      assigned_to: "paper"
892	      status: resolved
893	  resolution: "n=14 经调查不存在于论文中（审稿人误读）。Appendix (j) 重写为 n=44 全样本 + power ~0.3 caveat。"
894	  resolution_round: 18
895	
896	- id: "R18-W2"
897	  summary: "Abstract 中 'all three formulations achieve comparable accuracy' 表述过强——TRAJ 未通过等价检验"
898	  category: framing
899	  severity: warning
900	  status: resolved
901	  first_raised_round: 18
902	  last_seen_round: 18
903	  mentions:
904	    - round: 18
905	      reviewers: [1, 2]
906	      note: "R1 交叉回应中明确提出：CLS-TRAJ 在 Holm-Bonferroni 校正后 inconclusive (p_adj=0.075)，Abstract 不应声称 'all three comparable'。建议改为 'CLS and CWM achieve statistical equivalence; TRAJ parity is model-dependent'。R2 W1 亦提及。"
907	  action_items:
908	    - round: 18
909	      action: "Abstract 表述修正，区分 CLS-CWM（confirmed equivalence）和 CLS-TRAJ（inconclusive）"
910	      assigned_to: "paper"
911	      status: resolved
912	  resolution: "Abstract 已有正确区分：CLS-CWM (TOST p=0.007) 和 TRAJ (inconclusive after correction)。加入 p=0.007 与 §3.4/Conclusion 三处统一。"
913	  resolution_round: 18
914	
915	- id: "R18-W3"
916	  summary: "Constrained decoding 相关文献缺失（Synchromesh / XGrammar）"
917	  category: writing
918	  severity: warning
919	  status: resolved
920	  first_raised_round: 18
921	  last_seen_round: 18
922	  mentions:
923	    - round: 18
924	      reviewers: [1, 2]
925	      note: "R1 missing refs + R2 missing refs 均提到。Appendix (c) 已引用 Willard & Louf 2023 但正文 §3.7 讨论 constrained decoding 时未引用。建议正文增加引用。"
926	  action_items:
927	    - round: 18
928	      action: "§3.7 或 Limitations 中增加 Synchromesh / XGrammar 引用"
929	      assigned_to: "paper"
930	      status: resolved
931	  resolution: "Limitations 中 constrained decoding 句引用扩展为 3 篇：Synchromesh (Poesia 2022), XGrammar (Dong 2025), Outlines (Willard 2023)。"
932	  resolution_round: 18
933	
934	- id: "R18-M1"
935	  summary: "CWM exact string matching 未讨论 near-match 敏感性"
936	  category: method
937	  severity: info
938	  status: open
939	  first_raised_round: 18
940	  last_seen_round: 19
941	  mentions:
942	    - round: 18
943	      reviewers: [1]
944	      note: "R1-M3 提出。§2.1 定义了 exact match 并引用 CWM 原文，但未讨论 near-match 情况（如浮点数差异）的敏感性。Appendix (c) relaxed matching 实验部分回应但未在正文展开。"
945	    - round: 19
946	      reviewers: [1]
947	      note: "R19. M1 re-raises。Appendix (c) relaxed matching 部分回应。低优先级。"
948	
949	- id: "R19-M3"
950	  summary: "Figure 2 axis labels 和 legend 字号偏小（~正文 60-65%）"
951	  category: format
952	  severity: info
953	  status: wont_fix
954	  first_raised_round: 19
955	  last_seen_round: 19
956	  mentions:
957	    - round: 19
958	      reviewers: [1, 2]
959	      note: "R19 视觉审查。150dpi 下辨识困难。但在 ACL 论文正常范围内。"
960	  resolution: "ACL 论文正常范围，camera-ready 可微调。"
961	  resolution_round: 19
962	
963	# R17-N1 (TRAJ confound) tracked under R6-W4 with R17/R18/R19 mention.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71831459-17d3-47f3-9ce4-f86fe1fbc408",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "bfb5a8cc-af4e-4d3f-9ea2-13266b27d289",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
      "content": "# === Round 6 Issues (Original) ===\n\n# --- Round 6 Must-Fix (Consensus Critical) ---\n\n- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 19\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两人独立提出，最高共识。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W2 re-raises seed coverage (2-3 seeds for repo-level). R2 agrees. Repo-level variance > function-level, claims read as definitive but only 2-3 observations.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. §3.5 has explicit 'exploratory due to limited seed coverage' label. Failure mode taxonomy uses descriptive language. §3.7 reinforces 'definitive causal attribution requires multi-seed replication'. No causal claims in variant-level discussion.\"\n    - round: 13\n      reviewers: [1]\n      note: \"Fresh review R13. R1-W3 re-raises repo-level seed sparsity (some configs n=2). §3.5 exploratory label present. Director: resolved status maintained; R13 concern is about prominence of labeling, not missing disclosure.\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Fresh review R14. R1-N2 re-raises. R2 REBUT 指出 R1 混淆两个统计模型。Director：resolved 维持。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Fresh review R15. R1-W2 re-raises low power (~0.3, n_eff≈86). R2 AGREE 但补充论文已用 TOST+Bayesian ROPE+14B scaling 三重互补验证。Resolved 维持。\"\n    - round: 16\n      reviewers: [1]\n      note: \"Fresh review R16. R1-N2 re-raises：2-3 seeds 无法支撑 18-26pp gap 的 formulation 归因。R2 隐含 AGREE（N2 scope 限制）。论文 §3.5 'exploratory' 标注仍在。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"Fresh review R18. R1-W1 re-raises：18-26pp 点估计但 CI 宽（~5pp 到 ~40pp），建议报告 CI 范围。R2 同意（N2）。论文 §3.5 exploratory 标注仍在。Resolved 维持。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"Fresh review R19. 两人共识 repo-level 2-3 seeds CI 宽度与点估计精度不匹配。§3.5 exploratory 标注到位。Resolved 维持。\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 开头标注 'Variant-level comparisons (n=48) are exploratory due to limited seed coverage'。后续讨论使用描述性语言，避免 causal claims。§3.7 强调 multi-seed replication needed。R11 两位 Reviewer 一致确认 RESOLVED。R13-R19 反复提及但无新增要求。\"\n  resolution_round: 11\n\n- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 18\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"系统性偏差方向与 observed effect 一致。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"Reviewer 确认修复充分。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W3 re-raises checkpoint inconsistency.\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1 再次标为 CRITICAL。R2 REBUT。Director 降为 Should-Fix。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N2 升级为 critical。R2 完全 AGREE。\"\n    - round: 13\n      reviewers: [1]\n      note: \"R1-W4 re-raises。R2 AGREE。Director resolved 维持。\"\n    - round: 14\n      reviewers: [2]\n      note: \"R2-W1 re-raises s42 vs s123/s456 配置异质性。R1 AGREE。Director resolved 维持。\"\n    - round: 15\n      reviewers: [1]\n      note: \"R1-W7 re-raises CWM checkpoint ablation 范围。R2 REBUT。Director resolved 维持。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18. R1-W2 re-raises NaN val-loss runs 用 final epoch 而 CLS 用 val-selected。R2 AGREE。已有 Appendix O 讨论。Resolved 维持。\"\n  action_items:\n    - round: 6\n      action: \"CLS epoch ablation + matched epoch-3 解释\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"解释 CWM NaN val loss 原因\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 12\n      action: \"评估 Qwen3 CWM step 300-400 checkpoints 的 repo-level accuracy\"\n      assigned_to: \"experiment\"\n      status: wont_fix\n  resolution: \"Step 300-400 checkpoints 未保存，但已找到现有 step-400 eval 数据（s42: 64.36%, 63.7% unparseable）。Format collapse 从训练早期即存在。\"\n  resolution_round: 12\n\n- id: \"R6-N3\"\n  summary: \"Oracle ensemble accuracy 数值矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Oracle 90.63% 验证正确。96.03% 已删除。\"\n  resolution_round: 7\n\n- id: \"R6-N4\"\n  summary: \"Novelty 有限：核心贡献为比较已有 formulations，excitement 不足 main conference\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 19\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 建议 function-level equivalence 作为 headline。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"两人共识：Findings 合适，Main 不够。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2 Excitement 2/5, R1 Excitement 3/5。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"两人 Excitement 均为 3/5。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3/5, R2 Excitement 2.5/5。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"Fresh review R16. R1 Excitement 3/5, R2 Excitement 3/5。核心发现可预测性限制新颖性。wont_fix 维持。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"Fresh review R17. R1 Excitement 3/5, R2 Excitement 2.5/5。R2 明确判定 Findings 而非 main conference。wont_fix 维持。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"Fresh review R18. R1 Excitement 3/5, R2 Excitement 2.5/5。R1 反驳'直观可预期'但同意缺少干预闭环。R2 维持 Findings 判定。分歧在于 empirical comparison paper 的 novelty 标准。wont_fix 维持。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"Fresh review R19. R1 3.5 vs R2 3.0——分歧仍在 novelty 标准。R2 认为核心发现方向可预测，R1 认为 rigorous methodology + failure taxonomy 有独立价值。两人共识 Findings 区间。wont_fix 维持。\"\n  resolution: \"Excitement 稳定在 2.5-3.0/5，核心贡献类型（empirical comparison）无法通过修改改变。\"\n  resolution_round: 11\n\n# --- Round 6 Should-Fix ---\n\n- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 的 a priori 属性值得商榷\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 18\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人独立 re-raise。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises：无 pre-registration。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-W1 标 Must-Fix。R2 AGREE 部分。共识：Table 13 应移入正文。Resolved 维持。\"\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W1 re-raises：缺乏正式论证。但论文已诚实披露 post-hoc 状态并提供 sensitivity analysis。Resolved 维持。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W4 re-raises：SESOI 应基于 downstream 实践意义（repair@K 影响），论文未提供此分析。R2 AGREE with nuance——±2pp 是合理 convention 但增加实践论证更好。Resolved 维持。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未单独提及。Resolved 维持。\"\n  resolution: \"§3.4 已改为 'motivated by domain considerations but was not pre-registered'；Bayesian ROPE 提供独立佐证。\"\n  resolution_round: 12\n\n- id: \"R6-W2\"\n  summary: \"CWM regime qualifier 不充分——Abstract/Conclusion 缺少 ≤8B LoRA 限定\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 19\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Abstract 已有 '≤8B LoRA protocol'，Conclusion 加入限定。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"Fresh review R16. R2-N2 re-raises：标题仍暗示通用性。R1 AGREE 但程度略轻。Abstract 已有限定词但标题无。建议标题加 scope 限定。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18. R1 反驳'严重限制'但同意标题可限定。R2 维持。Abstract/Conclusion 限定已到位。Resolved 维持。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19. R2 持续关注标题泛化。R1 反驳：2 families 已超出同类论文，systematic 指方法论。Abstract/Conclusion 限定到位。Resolved 维持。\"\n  resolution: \"Abstract + Conclusion 均已加入 ≤8B LoRA 限定。标题是否需要修改由 Research Director 决定。\"\n  resolution_round: 10\n\n- id: \"R6-W3\"\n  summary: \"Re-repair δ=0 与 diagnostic granularity 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Contributions 4→3, diagnostic granularity 降级为 pending validation.\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异——label granularity + data composition 混淆\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 19\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"downsample 控制了 volume 但未控制 label granularity。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Director 裁定 Should-Fix（降级）。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"Abstract 已有 'the TRAJ comparison is inherently confounded'。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W1 re-raises TRAJ 与 CLS/CWM 比较性质不同。R1 AGREE：应视觉区分 controlled vs observational comparison。Resolved 维持——Abstract 和 §3.5 均有 confound 标注。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-N1 升级为 Must-Fix。原以为 175× data volume asymmetry，实际核实后 function-level TRAJ 有 8,052 训练 variants（CLS 仅 3,596 unique variants）——TRAJ 反而有 2.24× 更多 unique variants。Repo-level: ~70K vs 386 variants 仍有显著不对称。Confound 重新定性为 label granularity（非 data volume）。CLS@400 极端下采样实验进行中。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18. R1-N2 标 Must-Fix（100x 数据量 + 4x 学习率 + label granularity）。R2 部分同意但降为 Should-Fix——downsample ablation 和 function-level 近等价已部分缓解。建议补充 TRAJ@5e-5 消融。Resolved 维持——Abstract 'inherently confounded' + §3.1 显式配置说明 + §3.5 confound 讨论均已到位。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19. R1 标 Must-Fix（R1-N1），R2 同意问题存在但降为 Should-Fix。~100× 数据量 + 4× 学习率 + label granularity 差异使 CLS-TRAJ 属 observational comparison。缓解：downsample ablation + function-level 等价 + Abstract 'inherently confounded'。Director 采纳 Should-Fix。Resolved 维持。\"\n  resolution: \"§3.1 增加 M1 显式句子（8,052 vs 15,290, 2.24× more unique variants, confounded by label granularity and data composition）。§3.5 repo-level confound 讨论保留。Abstract 'inherently confounded' 保留。\"\n  resolution_round: 17\n\n- id: \"R6-W5\"\n  summary: \"Interaction 未做统计检验\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Interaction test z=-23.7 完成。\"\n  resolution_round: 9\n\n- id: \"R6-W6\"\n  summary: \"合成 mutation 外部效度\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W5 re-raises：synthetic mutation vs real developer patch 分布差异。Limitations 已提及但讨论不深。Resolved 维持。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2-W3 re-raises。单基准(SWE-bench)/单语言(Python)/合成 mutation 限制泛化性。R1 补充：mutation data 可能系统性偏向特定 formulation——CLS 对 mutation 类型更 robust，CWM 在合成 mutation 简单输出上表现可能被高估。此方向性 confound 论文未讨论。Resolved 维持——Limitations 已提及。\"\n    - round: 18\n      reviewers: [2]\n      note: \"R2-Q4 问为何不使用其他 repo-level benchmark。论文使用 SWE-bench Verified 是领域标准。Resolved 维持。\"\n  resolution: \"Appendix Extended Validity Discussion 讨论充分。Limitations 已提及 Python-only 和 codegen 限制。\"\n  resolution_round: 7\n\n- id: \"R6-W7\"\n  summary: \"Abstract 偏短 (~120-130 词)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"~185 词，合规。\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"遗漏近期相关工作\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  resolution: \"CodeRM, CodeScaler, GenPRM 等均已加入 Related Work。\"\n  resolution_round: 10\n\n# --- Round 6 Minor ---\n\n- id: \"R6-M1\"\n  summary: \"Tables 缺少次优下划线\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1]\n      note: \"R1-M1 re-raises Table 1/2 缺乏 bold/underline 标注最优 formulation。但论文 Table 1/2 已有 bold 和 underline（检查确认）。Resolved 维持。\"\n  resolution: \"Tables 1-3 bold+underline 完成。\"\n  resolution_round: 7\n\n- id: \"R6-M2\"\n  summary: \"Checklist C4 version numbers\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"C4 已列出版本号。\"\n  resolution_round: 7\n\n- id: \"R6-M3\"\n  summary: \"Figure 2 信息密度偏低 / y-axis 截断\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [1]\n      note: \"R1-M2 re-raises y-axis 截断可能夸大视觉差异。论文 caption 已标注 'y-axis does not start at zero'。Resolved 维持。\"\n    - round: 19\n      reviewers: [1]\n      note: \"R19 提及。Caption disclosure 到位。Resolved 维持。\"\n  resolution: \"Figure 2 caption 标注 'y-axis does not start at zero'。\"\n  resolution_round: 11\n\n# === Round 8 Issues ===\n\n- id: \"R8-C1\"\n  summary: \"TOST p=0.007 归属混淆\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 分开呈现。\"\n  resolution_round: 10\n\n- id: \"R8-C2\"\n  summary: \"Abstract 对 repo-level CWM 结论缺少 regime qualifier + z=-23.7 缺 model 标注\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract qualifier 和 model 标注已加入。\"\n  resolution_round: 10\n\n- id: \"R8-W1\"\n  summary: \"n=48 variant 样本量导致 TOST 统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 19\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-N2 标 CRITICAL：TOST power ~0.3。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Both RESOLVED.\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N3 re-raises.\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-W2 标 Must-Fix。R2 AGREE 但补充 Bayesian ROPE 不受 power 限制。Resolved 维持。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R1-N1 标 Critical：CLS-TRAJ power ~0.3 使该比较 uninformative，Abstract 'not confirmed' 可能 mislead。R2-W1 AGREE。论文 §3.4 已有 power paragraph + 'at current power (~0.3)' 限定。Resolved 维持。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-N2 升级为 Must-Fix。power ~0.3 使 CLS-TRAJ 比较 inconclusive（非 directional evidence）。R2 完全 AGREE 并建议 'not confirmed' 改为 'inconclusive'。建议增加 MDE 表格。Repo-level 2-3 seeds 功效更低。Resolved 维持——§3.4 已有 power paragraph。\"\n    - round: 18\n      reviewers: [1]\n      note: \"R18. R1-W1 re-raises repo-level 2-3 seeds power 不足。与 R6-N1 一致。Resolved 维持。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19. 隐含于 SF3（seed coverage）。§3.4 power paragraph + 'inconclusive' 术语 + Bayesian ROPE 均到位。Resolved 维持。\"\n  resolution: \"§3.4 已扩写 power paragraph，14B TOST 完成。Abstract 已加 'at current power (~0.3)' 限定。\"\n  resolution_round: 12\n\n- id: \"R8-W2\"\n  summary: \"Oracle 互补性估计为单种子、无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Cross-seed oracle 已加入正文。\"\n  resolution_round: 10\n\n- id: \"R8-W3\"\n  summary: \"CWM checkpoint 消融不对称——Qwen3 缺 early-stopping 评估\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Appendix 已讨论。\"\n  resolution_round: 10\n\n- id: \"R8-W4\"\n  summary: \"z=-23.7 interaction 仅基于 DeepSeek-Coder\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract 已标注 model。\"\n  resolution_round: 10\n\n- id: \"R8-W5\"\n  summary: \"遗漏 GenRM / RepoExec\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"GenRM, CodeScaler, GenPRM 已加入。\"\n  resolution_round: 10\n\n- id: \"R8-W6\"\n  summary: \"CWM baseline 偏弱 (≤8B LoRA vs 原始 32B)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 19\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N2 标 CRITICAL。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Director 裁定 Should-Fix（降级）。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R2-N2 标 Must-Fix。R1 REBUT matched design 方法论价值。Resolved 维持。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-N2 re-raises scope limitation。R1 AGREE 标题应加限定。Resolved 维持——所有 qualifier 已到位。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18. R2-N2 re-raises 实验规模限制。R1 反驳——2 families 已超出同类论文常规。Resolved 维持。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19. 隐含于 SF6（scope limitation）。R1 反驳 2 families 超出常规。Resolved 维持。\"\n  resolution: \"Abstract + Conclusion 均已加入 ≤8B LoRA 限定。14B 验证实验完成。\"\n  resolution_round: 10\n\n- id: \"R8-W7\"\n  summary: \"Novelty 是否足够 Conference 水平\"\n  category: framing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 8\n  last_seen_round: 13\n  resolution: \"合并至 R6-N4。Inherent limitation。\"\n  resolution_round: 11\n\n# --- Round 8 Minor ---\n\n- id: \"R8-M1\"\n  summary: \"混合精度 (bfloat16/NF4) 对 TOST 的影响\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 footnote 充分讨论。\"\n  resolution_round: 10\n\n- id: \"R8-M2\"\n  summary: \"LPM 未报告 robust SEs; prompt templates 未展示\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W6 re-raises LPM vs GEE 不一致（model identity p=0.002 vs p=0.449）。论文 Appendix M 已有 estimator-dependent 标注和 cluster 数限制讨论。Resolved 维持。\"\n  resolution: \"Appendix M 补充 GEE logistic regression + estimator-dependent 标注。\"\n  resolution_round: 11\n\n# === Round 9-12 Issues (all resolved, abbreviated) ===\n\n- id: \"R9-C1\"\n  summary: \"'Design space' framing 过度\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"标题已改为 Systematic Comparison。\"\n  resolution_round: 10\n\n- id: \"R9-W1\"\n  summary: \"CWM 评估指标非对称性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"R2 REBUT 成功：relaxed matching 扩大 gap。\"\n  resolution_round: 10\n\n- id: \"R9-W2\"\n  summary: \"DeepSeek 仅 2 seeds 却声称 'model-dependent'\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W3 re-raises DeepSeek 仅 2 seeds，跨模型比较可信度降低。Resolved 维持——§3.4 已有 caveat。\"\n  resolution: \"Abstract 改为更审慎措辞。\"\n  resolution_round: 10\n\n- id: \"R12-N1\"\n  summary: \"CWM baseline 生态效度：≤8B LoRA vs 原始 CWM 32B\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 15\n  resolution: \"Introduction §1 已加 'under our ≤8B LoRA protocol' 限定。14B function-level 收敛提供间接支持。\"\n  resolution_round: 12\n\n- id: \"R12-N3\"\n  summary: \"CLS-TRAJ 等价性不对称结论可能是 power ~0.3 artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"§3.4 power paragraph 扩写，14B TOST 完成。\"\n  resolution_round: 12\n\n- id: \"R12-W2\"\n  summary: \"GenRM 对比发现未充分讨论\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W4 re-raises：跨领域 code vs math GenRM 比较分析浅薄。R1 AGREE 但认为超出本文 scope。Resolved 维持——Conclusion 已有 GenRM 段落。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18. R1-M4 + R2-W4：GenRM domain contrast 是最有 novelty 潜力的观点但仅 Conclusion 一句话。双方共识应展开讨论。Resolved 维持但建议 rebuttal 展开。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19. 两人强烈共识 GenRM domain contrast 被严重低估（SF4）。Code domain 的 exact match 严格性和 output space 结构化程度等机制未展开。Conclusion 仍仅一句话。Resolved 维持但作为最有影响力的改进方向。\"\n  resolution: \"Conclusion 新增 GenRM domain-specificity 段落。\"\n  resolution_round: 12\n\n- id: \"R13-N1\"\n  summary: \"Appendix 'P: Limitations' 标题可能违反 EMNLP 格式规则\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Appendix P 重命名为 'Extended validity discussion'。\"\n  resolution_round: 13\n\n- id: \"R13-W1\"\n  summary: \"Abstract/Conclusion 中 TRAJ 'not confirmed' 措辞在 power ~0.3 下 over-stated\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18. R1 同意 Abstract 中 'all three formulations achieve comparable accuracy' 表述过强。建议改为 'CLS and CWM achieve statistical equivalence; TRAJ parity is model-dependent'。\"\n  resolution: \"Abstract 加入 'at current power (~0.3)' 限定语。R17 将 'not confirmed' 改为 'inconclusive'。\"\n  resolution_round: 13\n\n- id: \"R13-W2\"\n  summary: \"Oracle 互补性应重新框定为 negative result + motivation，而非独立正面贡献\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W2 re-raises：error complementarity 被高估。R1 AGREE 应降级为 exploratory finding。论文 §1 Contribution 2 已重写为 negative result framing。Resolved 维持。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W3 + R2-W2 re-raises。Oracle gap 大但 heuristic <0.4pp，Conclusion routing 方向过于乐观。§1 Contribution 2 权重过大。R2 补充：互补性存在有价值但不应列为主要贡献。Resolved 维持。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18. R1 同意 complementarity overclaim——oracle 90.63% 但 simple heuristics <0.4pp，oracle-to-achievable gap 过大。R2 同意。§1 已合并为 Contribution #1 子句。Resolved 维持。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19. 两人共识 oracle-to-achievable gap 过大（SF5）。§3.6 和 Conclusion routing 表述仍偏乐观。Resolved 维持。\"\n  resolution: \"Introduction Contribution 2 重写为 negative result framing。R17 合并为 Contribution #1 子句。\"\n  resolution_round: 13\n\n- id: \"R13-W3\"\n  summary: \"14B 'capacity-dependent convergence' claim 证据不足——仅 1 model family, 3 seeds\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 17\n  resolution: \"Abstract 和 Conclusion 已有 'preliminary observation' + 'single family' 限定。\"\n  resolution_round: 13\n\n- id: \"R13-W4\"\n  summary: \"GenRM 领域特异性对比分析不充分\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W4 re-raises。R1 AGREE 但认为超出 scope。Resolved 维持。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18. 双方共识 GenRM domain contrast 应展开——code domain 的 exact match 严格性和 output space 结构化程度可能是关键差异。建议 Conclusion 或 §4 增加讨论。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19. 与 R12-W2 一致。强烈共识应展开。\"\n  resolution: \"Conclusion 扩展 GenRM 对比。\"\n  resolution_round: 13\n\n# === Round 16 New Issues ===\n\n- id: \"R16-N1\"\n  summary: \"Complexity-dependent 核心叙事存在 complexity 与 output format/length 的未解耦混淆\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-N1 提出，R1 完全 AGREE。论文将 function→repo 分歧归因于 'code complexity'，但 format collapse（53-74% unparseable）更直接指向 output format/length 效应。四种 intervention 均未攻击 output length 本身（如 constrained decoding）。核心 narrative 框架需修正。两位 Reviewer 共识。\"\n  action_items:\n    - round: 16\n      action: \"Introduction 核心 claim 增加 mechanistic pathway：'formulation choice is moderated by code complexity, operating through output format'，明确 function ~5-15 tokens vs repo ~477 tokens 的 output length 差异是直接机制\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Introduction §1 核心 claim 增加 mechanistic pathway 解释。\"\n  resolution_round: 16\n\n- id: \"R16-N2\"\n  summary: \"≤8B LoRA 范围限制下标题和 abstract 泛化声明过广\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-N2 提出，R1 AGREE。标题 'A Systematic Comparison...' 暗示通用性，但实际仅覆盖 2 families × ≤8B × LoRA。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R2-N1 re-raises。R1 AGREE with nuance——'systematic' 可指方法论系统性而非穷举性。wont_fix 维持。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18. R2-N2 re-raises。R1 反驳'严重限制'——2 families 已超出同类论文，LoRA-only 是合理控制变量选择。但同意标题可略加限定。wont_fix 维持——Abstract 限定已到位。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19. SF6——R2 持续关注，R1 部分同意。Abstract 限定到位。wont_fix 维持。\"\n  resolution: \"Rebuttal material。Abstract 已有 '≤8B LoRA fine-tuning' 限定。标题修改由 Research Director 决定。\"\n  resolution_round: 16\n\n- id: \"R16-W1\"\n  summary: \"统计方法多样但主次层次不清\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"§3.1 Statistics 段落增加统计层次声明。\"\n  resolution_round: 16\n\n- id: \"R16-W2\"\n  summary: \"CWM format collapse 的定性归因不清：inherent formulation limitation vs engineering artifact\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W4 提出。53-74% unparseable + default to majority class。四种 interventions 失败但未测试 constrained decoding。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W2 re-raises。14B gap 收窄到 1.07pp 与 'inherent limitation' 归因存在叙事张力。R2 AGREE。Resolved 维持。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18. R1-N1 标 Must-Fix——constrained decoding 未测试使 'formulation-inherent' 归因不稳固。R2 REBUT——Appendix (c) 的间接证据（CWM 误训 CLS-format 数据 → 86.05% + 0% unparseable; parseable CWM 仅 38-43%）已证明 format compliance ≠ semantic accuracy，constrained decoding 即使消除 format collapse 也不改变核心结论。但 R2 同意 Appendix (c) 证据应提升到正文。Director 裁定 Should-Fix：间接证据充分但正文可见度不足。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19. SF2——两人共识 constrained decoding 未测试是明确 gap。Appendix (c) 间接证据到位，Limitations 已引用 Synchromesh/XGrammar/Outlines（R18 修复），§3.6 提及 Appendix (c)。但正文可见度仍不足——关键证据仍在 Appendix。Resolved 维持。\"\n  action_items:\n    - round: 18\n      action: \"将 Appendix (c) 的 CWM 误训实验和 parseable-only accuracy 证据提升到 §3.5 或 §3.6 正文\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Limitations §8 已有 constrained decoding 讨论。N1 mechanistic pathway 修复间接回应了归因问题。R18 建议将 Appendix (c) 关键证据提升到正文。Limitations 已引用 3 篇 constrained decoding 文献。\"\n  resolution_round: 16\n\n- id: \"R16-M1\"\n  summary: \"'pp' 缩写首次使用未定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"Introduction §1 首次出现处改为 'percentage points (pp)'。\"\n  resolution_round: 16\n\n- id: \"R16-M2\"\n  summary: \"DeepSeek-Coder 2 seeds 的 CI/std 在 Table 1 中未报告\"\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"Table 1 caption 已改为显式注明 seed 数量。\"\n  resolution_round: 16\n\n- id: \"R16-M3\"\n  summary: \"Figure 1 字体偏小，接近可读性下限\"\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"当前字体大小在 ACL 论文中属正常范围。\"\n  resolution_round: 16\n\n# === Round 17 New Issues ===\n\n- id: \"R17-W1\"\n  summary: \"核心发现可预测性未被讨论——complexity moderates formulation choice 方向直觉可预期\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18. R2-N1 re-raises 核心发现可预测性。R1 反驳——TRAJ 等价是反直觉的，failure taxonomy 不可先验推导。但 R1 同意缺少干预闭环。§3.5 已增加 predictability sentence。Resolved 维持。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19. 两人共识核心发现方向可预测（Reviewer Consensus #7）。R1 辩护 TRAJ 等价和 failure taxonomy 细节不可先验推导。分歧在 novelty 评估。Resolved 维持。\"\n  resolution: \"§3.5 增加 predictability discussion。\"\n  resolution_round: 17\n\n- id: \"R17-W2\"\n  summary: \"Conclusion scope 未标注 ≤8B LoRA 限定\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"Conclusion 首句改为 '...under ≤8B LoRA fine-tuning'。\"\n  resolution_round: 17\n\n- id: \"R17-W3\"\n  summary: \"Format collapse 描述缺少 training regime 限定\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§3.6 改为 '...under our ≤8B LoRA protocol'。\"\n  resolution_round: 17\n\n- id: \"R17-W4\"\n  summary: \"Contribution #2 (Error complementarity) 权重过大，应合并入 Contribution #1\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"Introduction Contribution #2 合并入 #1 作为子句。\"\n  resolution_round: 17\n\n- id: \"R17-N2-write\"\n  summary: \"'not confirmed' 应改为 'inconclusive'——TOST 标准术语\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"全文替换为 'inconclusive'。\"\n  resolution_round: 17\n\n- id: \"R17-N3-write\"\n  summary: \"14B 在 abstract/conclusion 叙事权重与 3 seeds/单家族证据不匹配\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"Abstract 改为 'Preliminary 14B results (3 seeds, single family) suggest the gap may narrow at larger scale'。\"\n  resolution_round: 17\n\n- id: \"R17-M1\"\n  summary: \"TRAJ 训练配置差异仅在 table footnote 中说明，应为显式句子\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§3.1 增加 TRAJ 配置显式说明。\"\n  resolution_round: 17\n\n- id: \"R17-M3\"\n  summary: \"CWM 术语与 RL world models 混淆——缺少辨析脚注\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§2.1 CWM 段增加辨析脚注。\"\n  resolution_round: 17\n\n- id: \"R17-M4\"\n  summary: \"DreamPRM/CodePRM 仅列举引用，未展开讨论差异\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"Related Work 展开 DreamPRM/CodePRM 讨论。\"\n  resolution_round: 17\n\n# === Round 18 New Issues ===\n\n- id: \"R18-W1\"\n  summary: \"Re-repair 实验样本量不一致（n=44 vs n=14）且结论过强\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1]\n      note: \"R1-W3 提出。Appendix I(j) 说 n=44 但后文出现 n=14。power ~0.3 不支撑 'does not translate' 结论。R2 部分同意。\"\n  action_items:\n    - round: 18\n      action: \"澄清 n=44 vs n=14 不一致；将结论弱化为 'we found no evidence of benefit, but the study was underpowered'\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"n=14 经调查不存在于论文中（审稿人误读）。Appendix (j) 重写为 n=44 全样本 + power ~0.3 caveat。\"\n  resolution_round: 18\n\n- id: \"R18-W2\"\n  summary: \"Abstract 中 'all three formulations achieve comparable accuracy' 表述过强——TRAJ 未通过等价检验\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R1 交叉回应中明确提出：CLS-TRAJ 在 Holm-Bonferroni 校正后 inconclusive (p_adj=0.075)，Abstract 不应声称 'all three comparable'。建议改为 'CLS and CWM achieve statistical equivalence; TRAJ parity is model-dependent'。R2 W1 亦提及。\"\n  action_items:\n    - round: 18\n      action: \"Abstract 表述修正，区分 CLS-CWM（confirmed equivalence）和 CLS-TRAJ（inconclusive）\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Abstract 已有正确区分：CLS-CWM (TOST p=0.007) 和 TRAJ (inconclusive after correction)。加入 p=0.007 与 §3.4/Conclusion 三处统一。\"\n  resolution_round: 18\n\n- id: \"R18-W3\"\n  summary: \"Constrained decoding 相关文献缺失（Synchromesh / XGrammar）\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R1 missing refs + R2 missing refs 均提到。Appendix (c) 已引用 Willard & Louf 2023 但正文 §3.7 讨论 constrained decoding 时未引用。建议正文增加引用。\"\n  action_items:\n    - round: 18\n      action: \"§3.7 或 Limitations 中增加 Synchromesh / XGrammar 引用\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Limitations 中 constrained decoding 句引用扩展为 3 篇：Synchromesh (Poesia 2022), XGrammar (Dong 2025), Outlines (Willard 2023)。\"\n  resolution_round: 18\n\n- id: \"R18-M1\"\n  summary: \"CWM exact string matching 未讨论 near-match 敏感性\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [1]\n      note: \"R1-M3 提出。§2.1 定义了 exact match 并引用 CWM 原文，但未讨论 near-match 情况（如浮点数差异）的敏感性。Appendix (c) relaxed matching 实验部分回应但未在正文展开。\"\n    - round: 19\n      reviewers: [1]\n      note: \"R19. M1 re-raises。Appendix (c) relaxed matching 部分回应。低优先级。\"\n\n- id: \"R19-M3\"\n  summary: \"Figure 2 axis labels 和 legend 字号偏小（~正文 60-65%）\"\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19 视觉审查。150dpi 下辨识困难。但在 ACL 论文正常范围内。\"\n  resolution: \"ACL 论文正常范围，camera-ready 可微调。\"\n  resolution_round: 19\n\n# R17-N1 (TRAJ confound) tracked under R6-W4 with R17/R18/R19 mention.",
      "numLines": 963,
      "startLine": 1,
      "totalLines": 963
    }
  },
  "sourceToolAssistantUUID": "71831459-17d3-47f3-9ce4-f86fe1fbc408",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 83_

```json
{
  "type": "last-prompt",
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: exec-sim-repair-verifier - 论文路径: projects/exec-sim-repair-verifier/docs/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: ARR (Main/Findings unified) - 截止日期: 2026-05-25 -…",
  "leafUuid": "bfb5a8cc-af4e-4d3f-9ea2-13266b27d289",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e"
}
```

---

### Runtime record

_source line 84_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper submission for EMNLP 2026",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e"
}
```

---

### Assistant

_source line 85 · 2026-05-25T21:16:23.500Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent. I now have a complete picture of the paper and the review history. This is a fresh review (Round 20, since the last round in the tracker was 19). Let me now:

1. Dispatch visual check
2. Assign 2 Reviewers

For EMNLP 2026 (一般会议):
- Reviewer 1: 方法严谨性 + 实验设计
- Reviewer 2: 新颖性 + 完整性 + 写作质量

Let me compose the review tasks with venue info.


Now I'm gathering the key submission details—EMNLP 2026 through ARR with an 8-page limit for the main text, unlimited references, ACL style formatting, and double-blind review. The deadline is today, May 25, 2026. I need to draft reviewer messages that include the venue requirements, page limits, anonymity guidelines, the paper location, and each reviewer's specific evaluation focus.

I have the paper PDF and main LaTeX file paths ready. Since this is a fresh submission, I'll skip any reference to previous feedback and launch the visual check along with both reviewer assignments simultaneously.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfb5a8cc-af4e-4d3f-9ea2-13266b27d289",
  "isSidechain": false,
  "requestId": "req_011CbPyrEhUWDgSdAtcWth7J",
  "type": "assistant",
  "uuid": "54a39f9e-f6f7-4e95-a04a-b1d76c623e33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zhya6W7nJ5SnjVGcxaF7r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17001,
      "cache_read_input_tokens": 89082,
      "output_tokens": 2648,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17001,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2648,
          "cache_read_input_tokens": 89082,
          "cache_creation_input_tokens": 17001,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17001
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

_source line 86 · 2026-05-25T21:16:29.675Z_

资料检查完成：
- **论文 PDF**：存在（782KB，2026-05-25 更新）
- **LaTeX 源文件**：完整（abstract/intro/related_work/method/experiments/conclusion/appendix）
- **引用文件**：47 篇引用，格式完整
- **Issue Tracker**：存在，含 R6-R19 历史记录

**Venue 确认（EMNLP 2026 via ARR）**：
- 正文 ≤8 页（long paper），参考文献不限
- ACL 模板，double-blind 审稿
- ARR 提交截止：2026-05-25
- Limitations 必须写在正文，不计入页数
- ARR Checklist 在 OpenReview 表单填写，不在 PDF 中

**Reviewer 编排**：EMNLP 为一般会议级别，安排 2 名 Reviewer：
- **Reviewer 1**：方法严谨性 + 实验设计 + 统计分析
- **Reviewer 2**：新颖性 + 完整性 + 写作质量 + 相关工作

开始 Round 1 独立审稿，同时派发视觉审查。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54a39f9e-f6f7-4e95-a04a-b1d76c623e33",
  "isSidechain": false,
  "requestId": "req_011CbPyrEhUWDgSdAtcWth7J",
  "type": "assistant",
  "uuid": "f182d724-fac5-4031-9fe8-ac8b61ce1589",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zhya6W7nJ5SnjVGcxaF7r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17001,
      "cache_read_input_tokens": 89082,
      "output_tokens": 2648,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17001,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2648,
          "cache_read_input_tokens": 89082,
          "cache_creation_input_tokens": 17001,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17001
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

_source line 87 · 2026-05-25T21:16:32.171Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check · `toolu_01KzRC2ZMorJXm87CWmbRrY5`</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f182d724-fac5-4031-9fe8-ac8b61ce1589",
  "isSidechain": false,
  "requestId": "req_011CbPyrEhUWDgSdAtcWth7J",
  "type": "assistant",
  "uuid": "4b186d60-c390-425d-909d-b2bdaca0fcd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zhya6W7nJ5SnjVGcxaF7r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17001,
      "cache_read_input_tokens": 89082,
      "output_tokens": 2648,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17001,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2648,
          "cache_read_input_tokens": 89082,
          "cache_creation_input_tokens": 17001,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17001
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

_source line 88 · 2026-05-25T21:16:39.303Z_

<details><summary>↩ Tool result · `toolu_01KzRC2ZMorJXm87CWmbRrY5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b186d60-c390-425d-909d-b2bdaca0fcd5",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "a2d43509-9533-49e9-a7b4-591a4d6356ef",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"status\\\": \\\"started\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "4b186d60-c390-425d-909d-b2bdaca0fcd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-25T21:16:49.486Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer · `toolu_01TWJzLCeby9JDraACErxCrF`</summary>

```json
{
  "reviewer_id": "1",
  "round_number": 1,
  "text": "你是 Reviewer 1，负责审查以下论文的**方法严谨性、实验设计和统计分析**。\n\n## 论文信息\n- 标题: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n- LaTeX 源文件: projects/exec-sim-repair-verifier/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_18/submitted.pdf\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- 截止日期: 2026-05-25\n- Long paper: 正文 ≤8 页，参考文献不限\n- ACL 模板，double-blind 审稿\n- Limitations 必须在正文，不计入页数限制\n- ARR Checklist 在 OpenReview 表单填写，不在 PDF 中\n- Overall Assessment 评分标准: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n请重点关注以下方面：\n1. **实验设计**：控制变量是否充分？seed 数量和模型覆盖是否支撑结论？confound 是否充分讨论？\n2. **统计方法**：TOST 等价检验、Holm-Bonferroni 校正、clustered bootstrap、Bayesian ROPE、mixed-effects LPM 等统计方法的使用是否正确、合理？\n3. **Checkpoint selection 和 evaluation protocol**：不同 formulation 之间的 checkpoint 选择是否公平？eval sequence length 差异是否充分控制？\n4. **Repo-level 结论强度**：18-26pp gap 的 causal attribution 是否与 2-3 seeds 的证据强度匹配？\n5. **CWM baseline 公平性**：≤8B LoRA vs 原始 32B CWM 的比较是否充分限定？\n6. **TRAJ 训练配置差异**：label granularity + data volume + learning rate 差异是否使 CLS-TRAJ 比较有效？\n\n请按以下格式输出审稿意见：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 Must-Fix / Should-Fix / Minor)\n- Questions\n- Missing References\n- Soundness (1-5)\n- Excitement (1-5)\n- Overall Assessment (使用 EMNLP 2026 评分标准)\n- Confidence (1-5)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2d43509-9533-49e9-a7b4-591a4d6356ef",
  "isSidechain": false,
  "requestId": "req_011CbPyrEhUWDgSdAtcWth7J",
  "type": "assistant",
  "uuid": "9adec863-936e-4e1d-9825-bffa2888b30e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zhya6W7nJ5SnjVGcxaF7r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17001,
      "cache_read_input_tokens": 89082,
      "output_tokens": 2648,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17001,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2648,
          "cache_read_input_tokens": 89082,
          "cache_creation_input_tokens": 17001,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17001
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

_source line 90 · 2026-05-25T21:16:50.836Z_

<details><summary>↩ Tool result · `toolu_01TWJzLCeby9JDraACErxCrF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9adec863-936e-4e1d-9825-bffa2888b30e",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "0eddc6d0-064f-4e40-9753-563230d27539",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reviewer_key\\\": \\\"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "9adec863-936e-4e1d-9825-bffa2888b30e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-25T21:17:00.580Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer · `toolu_01J5FAyrNkH3pGeHrUsqjz6d`</summary>

```json
{
  "reviewer_id": "2",
  "round_number": 1,
  "text": "你是 Reviewer 2，负责审查以下论文的**新颖性、完整性、写作质量和相关工作**。\n\n## 论文信息\n- 标题: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n- LaTeX 源文件: projects/exec-sim-repair-verifier/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_18/submitted.pdf\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- 截止日期: 2026-05-25\n- Long paper: 正文 ≤8 页，参考文献不限\n- ACL 模板，double-blind 审稿\n- Limitations 必须在正文，不计入页数限制\n- ARR Checklist 在 OpenReview 表单填写，不在 PDF 中\n- Overall Assessment 评分标准: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n请重点关注以下方面：\n1. **新颖性**：核心贡献（formulation comparison）是否有足够 novelty？结论是否可预测？failure mode taxonomy 和 error complementarity 是否提供了新洞察？\n2. **完整性**：实验是否覆盖了充分的 baseline？消融实验是否完整？是否有重要的缺失实验？\n3. **写作质量**：叙事结构是否清晰？Abstract/Intro/Conclusion 的 claim 强度是否与证据匹配？术语使用是否一致？\n4. **相关工作**：是否遗漏重要参考文献？与 GenRM、CWM 原文、SWE-RM 等的定位是否清晰？\n5. **标题和 Framing**：标题是否暗示了过广的泛化性？≤8B LoRA 范围限制是否在关键位置充分标注？\n6. **贡献陈述**：4 个 contribution 的权重是否合理？oracle complementarity 是否被过度强调？\n7. **GenRM 对比**：code vs math domain 的 generative verifier 对比分析是否充分？\n\n请按以下格式输出审稿意见：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 Must-Fix / Should-Fix / Minor)\n- Questions\n- Missing References\n- Soundness (1-5)\n- Excitement (1-5)\n- Overall Assessment (使用 EMNLP 2026 评分标准)\n- Confidence (1-5)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0eddc6d0-064f-4e40-9753-563230d27539",
  "isSidechain": false,
  "requestId": "req_011CbPyrEhUWDgSdAtcWth7J",
  "type": "assistant",
  "uuid": "e0407e57-98d9-443f-b84a-070e56f91a53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zhya6W7nJ5SnjVGcxaF7r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17001,
      "cache_read_input_tokens": 89082,
      "output_tokens": 2648,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17001,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2648,
          "cache_read_input_tokens": 89082,
          "cache_creation_input_tokens": 17001,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17001
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

_source line 92 · 2026-05-25T21:17:01.997Z_

<details><summary>↩ Tool result · `toolu_01J5FAyrNkH3pGeHrUsqjz6d`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0407e57-98d9-443f-b84a-070e56f91a53",
  "isSidechain": false,
  "promptId": "f4fab3ed-c54e-4c23-8001-777667b98a53",
  "type": "user",
  "uuid": "67f0d7d0-49d0-4c22-93d6-cb077a2f9a8a",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reviewer_key\\\": \\\"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "e0407e57-98d9-443f-b84a-070e56f91a53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3",
  "sessionId": "21e91d71-aa56-45c2-8945-1101b3d4f69e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---
