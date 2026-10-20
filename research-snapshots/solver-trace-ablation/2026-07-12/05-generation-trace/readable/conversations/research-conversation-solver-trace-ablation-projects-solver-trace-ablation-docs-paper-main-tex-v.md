# Research conversation: 系统通知：审稿审批已通过。请开始审稿。 [论文提交] - 项目: solver-trace-ablation - 论文路径: projects/solver-trace-ablation/docs/paper/main.tex - 目标 v

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 109
- **Recorded user turns:** 4
- **Tool calls:** 29
- **Original source:** `logs/chats/exported-trajectories/account-2/f8953b3f-e1da-4479-9348-d08b652e1646.jsonl`
- **Structured JSON:** [`f635cfd335049b4e3e30.json`](../../sessions/f6/f635cfd335049b4e3e30.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-25T03:54:48.818Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T03:54:48.818Z",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "content": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: solver-trace-ablation\n- 论文路径: projects/solver-trace-ablation/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: Long paper (ARR)\n- 截止日期: 未提供，请自行调研\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

---

### Runtime record

_source line 2 · 2026-05-25T03:54:48.822Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T03:54:48.822Z",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646"
}
```

---

## Round 1

97 recorded events

### User

_source line 3 · 2026-05-25T03:54:48.861Z_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: solver-trace-ablation
- 论文路径: projects/solver-trace-ablation/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long paper (ARR)
- 截止日期: 未提供，请自行调研
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "57799c29-9849-4d34-876e-e27ab221c806",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-25T03:54:48.860Z_

```json
{
  "parentUuid": "57799c29-9849-4d34-876e-e27ab221c806",
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
  "uuid": "7bb00226-e98b-44f9-943b-bed270be6900",
  "timestamp": "2026-05-25T03:54:48.860Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-25T03:54:48.860Z_

```json
{
  "parentUuid": "7bb00226-e98b-44f9-943b-bed270be6900",
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
  "uuid": "18168185-87be-4d5f-8323-2ce110c755bc",
  "timestamp": "2026-05-25T03:54:48.860Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-25T03:54:48.860Z_

```json
{
  "parentUuid": "18168185-87be-4d5f-8323-2ce110c755bc",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f5eebd00-65c0-467c-9dad-28f3e0631800",
  "timestamp": "2026-05-25T03:54:48.860Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
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
  "aiTitle": "Review solver-trace-ablation paper for EMNLP 2026",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646"
}
```

---

### Assistant

_source line 8 · 2026-05-25T03:54:52.042Z_

<details><summary>Logged reasoning block</summary>

```text
收到论文提交，需要开始审稿流程。按照指示，先加载 review-director-session-start skill。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5eebd00-65c0-467c-9dad-28f3e0631800",
  "isSidechain": false,
  "requestId": "req_011CbNcSZYRwEwvXPPyrzdJh",
  "type": "assistant",
  "uuid": "4acfcf1c-c507-4336-bccc-4f149cab615b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2SX8cwYDQAjpoRxDhLZNU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16816,
      "cache_read_input_tokens": 11841,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16816,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 129,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16816,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16816
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

_source line 9 · 2026-05-25T03:54:52.198Z_

<details open><summary>🔧 Tool call — Read · `toolu_019P67MUX7UnitEuHY5eKp1u`</summary>

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
  "parentUuid": "4acfcf1c-c507-4336-bccc-4f149cab615b",
  "isSidechain": false,
  "requestId": "req_011CbNcSZYRwEwvXPPyrzdJh",
  "type": "assistant",
  "uuid": "ef23bda6-93e6-4b2b-a722-0188629971cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2SX8cwYDQAjpoRxDhLZNU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16816,
      "cache_read_input_tokens": 11841,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16816,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 129,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16816,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16816
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

_source line 10 · 2026-05-25T03:54:52.230Z_

<details><summary>↩ Tool result · `toolu_019P67MUX7UnitEuHY5eKp1u`</summary>

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
  "parentUuid": "ef23bda6-93e6-4b2b-a722-0188629971cd",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "aa368109-6262-4ed3-bd84-c3cbf4775c3e",
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
  "sourceToolAssistantUUID": "ef23bda6-93e6-4b2b-a722-0188629971cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
````

</details>

---

### Assistant

_source line 11 · 2026-05-25T03:54:55.386Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to follow the review process. Let me start with:

1. Step 0: Material check + Venue research
2. Get project overview
3. Read the paper

Let me start by getting the project overview and checking the paper files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa368109-6262-4ed3-bd84-c3cbf4775c3e",
  "isSidechain": false,
  "requestId": "req_011CbNcSpCUzR1EoMqhFCiTu",
  "type": "assistant",
  "uuid": "d51f0ba3-c3a8-496a-a5e2-210da0e2e519",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BmK8ADnY19LzivwLKvG9RB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3456,
      "cache_read_input_tokens": 28657,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3456,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 28657,
          "cache_creation_input_tokens": 3456,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3456
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

_source line 12 · 2026-05-25T03:54:56.352Z_

开始审稿流程。先执行初始化和资料检查。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d51f0ba3-c3a8-496a-a5e2-210da0e2e519",
  "isSidechain": false,
  "requestId": "req_011CbNcSpCUzR1EoMqhFCiTu",
  "type": "assistant",
  "uuid": "9917a9bf-5448-4843-9a45-4a4c9692f9b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BmK8ADnY19LzivwLKvG9RB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3456,
      "cache_read_input_tokens": 28657,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3456,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 28657,
          "cache_creation_input_tokens": 3456,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3456
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

_source line 13 · 2026-05-25T03:54:58.481Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DEyu7tyWxLpfqa7qKUvApH`</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9917a9bf-5448-4843-9a45-4a4c9692f9b1",
  "isSidechain": false,
  "requestId": "req_011CbNcSpCUzR1EoMqhFCiTu",
  "type": "assistant",
  "uuid": "04c3c8ec-fe78-4c98-9f18-e64cc8681292",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BmK8ADnY19LzivwLKvG9RB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3456,
      "cache_read_input_tokens": 28657,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3456,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 28657,
          "cache_creation_input_tokens": 3456,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3456
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

_source line 14 · 2026-05-25T03:54:58.859Z_

<details><summary>↩ Tool result · `toolu_013SGVSU6SYnin6GGx9zLYUR`</summary>

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
  "parentUuid": "e9368bf7-4450-4897-bd50-e67faf0a7d91",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "07f70a6f-6420-47e2-883e-a2d75d1d520f",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 29
  },
  "sourceToolAssistantUUID": "e9368bf7-4450-4897-bd50-e67faf0a7d91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-25T03:54:58.486Z_

<details><summary>↩ Tool result · `toolu_01DEyu7tyWxLpfqa7qKUvApH`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04c3c8ec-fe78-4c98-9f18-e64cc8681292",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "7708f7be-43d1-4ca3-a8b0-dc64f932a872",
  "toolUseResult": {
    "matches": [],
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "total_deferred_tools": 29
  },
  "sourceToolAssistantUUID": "04c3c8ec-fe78-4c98-9f18-e64cc8681292",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-25T03:54:58.855Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013SGVSU6SYnin6GGx9zLYUR`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7708f7be-43d1-4ca3-a8b0-dc64f932a872",
  "isSidechain": false,
  "requestId": "req_011CbNcSpCUzR1EoMqhFCiTu",
  "type": "assistant",
  "uuid": "e9368bf7-4450-4897-bd50-e67faf0a7d91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BmK8ADnY19LzivwLKvG9RB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3456,
      "cache_read_input_tokens": 28657,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3456,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 28657,
          "cache_creation_input_tokens": 3456,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3456
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

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: solver-trace-ablation - 论文路径: projects/solver-trace-ablation/docs/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: Long paper (ARR) - 截止日期: 未提供，请自行调研 - **引用验证**: ❌ 未启用…",
  "leafUuid": "07f70a6f-6420-47e2-883e-a2d75d1d520f",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Review solver-trace-ablation paper for EMNLP 2026",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646"
}
```

---

### Tool call

_source line 19 · 2026-05-25T03:55:03.063Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01ThxraRPjNj1avExWkTGezm`</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07f70a6f-6420-47e2-883e-a2d75d1d520f",
  "isSidechain": false,
  "requestId": "req_011CbNcTJhzCTG1BT72uYWKU",
  "type": "assistant",
  "uuid": "8b4c5f90-1c0f-4bac-a53a-603c804eb7e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AtCVPPmw9NsMKYiviEQqsn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1360,
      "cache_read_input_tokens": 32113,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1360,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 141,
          "cache_read_input_tokens": 32113,
          "cache_creation_input_tokens": 1360,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1360
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

_source line 20 · 2026-05-25T03:55:03.066Z_

<details><summary>↩ Tool result · `toolu_01ThxraRPjNj1avExWkTGezm`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b4c5f90-1c0f-4bac-a53a-603c804eb7e5",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "60f64609-9eba-4069-ab13-52f2f2703020",
  "toolUseResult": {
    "matches": [],
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "total_deferred_tools": 29
  },
  "sourceToolAssistantUUID": "8b4c5f90-1c0f-4bac-a53a-603c804eb7e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-25T03:55:06.251Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QEJcQGDv1iTQncWjsFrrq1`</summary>

```json
{
  "query": "director_get_project_overview",
  "max_results": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60f64609-9eba-4069-ab13-52f2f2703020",
  "isSidechain": false,
  "requestId": "req_011CbNcTcaX7aAB7QmjRXYhL",
  "type": "assistant",
  "uuid": "d66fefd2-8e6b-45f7-949f-856671903884",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Y1iNSa67HSoUWWZtc7dSF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 161,
      "cache_read_input_tokens": 33473,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 161,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 33473,
          "cache_creation_input_tokens": 161,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 161
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

_source line 22 · 2026-05-25T03:55:06.263Z_

<details><summary>↩ Tool result · `toolu_01QEJcQGDv1iTQncWjsFrrq1`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__director_get_project_overview"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d66fefd2-8e6b-45f7-949f-856671903884",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "cec22d4b-19ae-4dc5-8cb8-6ebf7d8c44cb",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__director_get_project_overview"
    ],
    "query": "director_get_project_overview",
    "total_deferred_tools": 29
  },
  "sourceToolAssistantUUID": "d66fefd2-8e6b-45f7-949f-856671903884",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-25T03:55:09.322Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013GiLDpP9soLG2rYNDN7YWd`</summary>

```json
{
  "query": "director_post_to_reviewer dispatch_visual_check request_external_review get_external_review_status get_visual_check_status submit_review_report update_review_issues read_project_file",
  "max_results": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cec22d4b-19ae-4dc5-8cb8-6ebf7d8c44cb",
  "isSidechain": false,
  "requestId": "req_011CbNcTr9b5euMeGw8DR2x1",
  "type": "assistant",
  "uuid": "e79762e6-bb9a-4ab7-aa30-eca642baf7ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FE1ea9YzpG48gx6KA4D9Fk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 245,
      "cache_read_input_tokens": 33634,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 245,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 118,
          "cache_read_input_tokens": 33634,
          "cache_creation_input_tokens": 245,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 245
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

_source line 24 · 2026-05-25T03:55:09.334Z_

<details><summary>↩ Tool result · `toolu_013GiLDpP9soLG2rYNDN7YWd`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__dispatch_visual_check"
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
  "tool_name": "mcp__agent-ml-research__read_project_file"
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
  "tool_name": "mcp__agent-ml-research__update_review_issues"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__submit_review_report_to_research_director"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e79762e6-bb9a-4ab7-aa30-eca642baf7ea",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "870e7d38-845a-47ba-89cc-b0b8cb86e479",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__dispatch_visual_check",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__get_external_review_status",
      "mcp__agent-ml-research__get_visual_check_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__request_external_review",
      "mcp__agent-ml-research__update_review_issues",
      "mcp__agent-ml-research__submit_review_report_to_research_director"
    ],
    "query": "director_post_to_reviewer dispatch_visual_check request_external_review get_external_review_status get_visual_check_status submit_review_report update_review_issues read_project_file",
    "total_deferred_tools": 29
  },
  "sourceToolAssistantUUID": "e79762e6-bb9a-4ab7-aa30-eca642baf7ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-25T03:55:22.121Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all tools loaded. Let me start the review process:

1. Get project overview
2. Check paper files exist
3. Search for EMNLP 2026 venue requirements
4. Read the paper

Let me do these in parallel where possible.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "870e7d38-845a-47ba-89cc-b0b8cb86e479",
  "isSidechain": false,
  "requestId": "req_011CbNcU5UH9h63SVvbW92Cz",
  "type": "assistant",
  "uuid": "23a08d46-2f69-4b24-8a29-c94f18f0c009",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVCAJSsoGs6XEW2jdQwA2r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3113,
      "cache_read_input_tokens": 33879,
      "output_tokens": 438,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3113,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 438,
          "cache_read_input_tokens": 33879,
          "cache_creation_input_tokens": 3113,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3113
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

_source line 26 · 2026-05-25T03:55:23.661Z_

工具已就绪。开始执行 Step 0：资料检查 + Venue 调研。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23a08d46-2f69-4b24-8a29-c94f18f0c009",
  "isSidechain": false,
  "requestId": "req_011CbNcU5UH9h63SVvbW92Cz",
  "type": "assistant",
  "uuid": "d1dbca20-b3a9-4c9b-a241-7d339e0e42e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVCAJSsoGs6XEW2jdQwA2r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3113,
      "cache_read_input_tokens": 33879,
      "output_tokens": 438,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3113,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 438,
          "cache_read_input_tokens": 33879,
          "cache_creation_input_tokens": 3113,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3113
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

_source line 27 · 2026-05-25T03:55:24.203Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01JSvCcT2M1JeBoeRxKkqCye`</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1dbca20-b3a9-4c9b-a241-7d339e0e42e4",
  "isSidechain": false,
  "requestId": "req_011CbNcU5UH9h63SVvbW92Cz",
  "type": "assistant",
  "uuid": "7b91a6fc-597b-4b74-980b-ba348296e7a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVCAJSsoGs6XEW2jdQwA2r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3113,
      "cache_read_input_tokens": 33879,
      "output_tokens": 438,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3113,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 438,
          "cache_read_input_tokens": 33879,
          "cache_creation_input_tokens": 3113,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3113
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

_source line 28 · 2026-05-25T03:55:24.702Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ARrnpfjf64najihzwtL6Gk`</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b91a6fc-597b-4b74-980b-ba348296e7a0",
  "isSidechain": false,
  "requestId": "req_011CbNcU5UH9h63SVvbW92Cz",
  "type": "assistant",
  "uuid": "fdf2f58b-6070-454d-94e0-0f2dce312f99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVCAJSsoGs6XEW2jdQwA2r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3113,
      "cache_read_input_tokens": 33879,
      "output_tokens": 438,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3113,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 438,
          "cache_read_input_tokens": 33879,
          "cache_creation_input_tokens": 3113,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3113
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

_source line 29 · 2026-05-25T03:55:24.844Z_

<details><summary>↩ Tool result · `toolu_01JSvCcT2M1JeBoeRxKkqCye`</summary>

```text
{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (216 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- d158_llama_sft_s42（准备中）\n- d154-8b-exec-s42-k4（准备中）\n- d154-8b-exec-s42-r2（准备中）\n- d154-8b-exec-s42: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=42. Tests whether larger model (8B vs 4B) exhibits same Goodhart collapse patterns under exec-only reward. Pilot experiment.（准备中）\n- d154-8b-isr-s43: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=43. Replication of ISR s42 for statistical power at 8B scale.（准备中）\n- d154-8b-isr-s42: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=42. Tests whether ISR-induced Goodhart collapse (TS dominance) persists at 8B scale, or if larger capacity enables genuine reasoning.（准备中）\n- d154-8b-exec-s44: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=44. Replication of exec s42 for statistical power across model scale.（准备中）\n- d154-8b-exec-s43: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=43. Replication of exec s42 for statistical power across model scale.（准备中）\n- d146-pf-pipeline（准备中）\n- d144-llama-isr-s43: D144 cross-model: ISR β=0.1 GRPO on LLaMA-3.2-3B/FOLIO seed=43. Replication of ISR s42 for statistical power.（准备中）\n- …另有 22 项\n\n## 近期结论\n- **exec-only-s45-1000step-k8** (killed): —\n- **exec-only-s45-1000step** (negative): Exec-only GRPO 1000-step K=4 seed 45: testing whether extended training amplifies structural degeneration beyond 500 steps. Config identical to plan001 series (K=4).\n- **d154-8b-exec-s42-k8** (negative): 8B K=8 exec-only non-convergence: gradient signal present but insufficient for convergence within 500 steps, resulting in near-zero training reward by step 500 ← 基于 d154-8b-exec-s42-k4v2\n\n## 趋势\n成功 73 / 负向 50 / 失败 49 / 共 184\nCE_count: 1 →（近 3 次 success）\nCI_count: 0 →（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-39279: 无 GPU 信息\n\n## 告警\n- sta-phase1-exec-only: 训练失败 — unknown\n- sta-phase1-exec-sta: 训练失败 — unknown\n- sta-phase1-exec-only-r2: 训练失败 — unknown\n- sta-phase1-exec-sta-r2: 训练失败 — unknown\n- sta-phase1-exec-only-r3: 训练失败 — unknown\n- sta-phase1-exec-sta-r3: 训练失败 — unknown\n- plan001-exec-only-s42: 训练失败 — unknown\n- plan001-exec-only-s42-r3: 训练失败 — unknown\n- plan001-exec-only-s43: 训练失败 — unknown\n- plan013-random-reward-s42: 训练失败 — unknown\n- plan013-random-reward-s42-r2: 训练失败 — unknown\n- plan001-exec-only-s43-r2: 训练失败 — unknown\n- plan013-random-reward-s42-r3: 训练失败 — unknown\n- plan001-exec-only-s43-r3: 训练失败 — unknown\n- plan006-prolog-exec-s43: 已被终止 — unknown\n- plan018-additive-random-b01-s43: 训练失败 — unknown\n- plan009-sft-baseline-s42: 已被终止 — unknown\n- plan009-sft-baseline-s42-r2: 训练失败 — unknown\n- plan009-sft-baseline-s42-r3: 训练失败 — unknown\n- plan006-prolog-exec-s43-r2: 训练失败 — unknown\n- exp1-isr-b03-s44: 训练失败 — unknown\n- exp1-random-b03-s44: 训练失败 — unknown\n- exp1-isr-b03-s43-r2: 已被终止 — unknown\n- plan015-linear-s42: 已被终止 — unknown\n- exp1-isr-b03-s43-r4: 已被终止 — unknown\n- exp1-random-b03-s43-r2: 已被终止 — unknown\n- exp1-random-b03-s43-r3: 训练失败 — unknown\n- plan018-additive-ra"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b91a6fc-597b-4b74-980b-ba348296e7a0",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "ce8f4db6-961d-48ff-a062-a98b8de63180",
  "toolUseResult": "{\"result\":\"# 项目 solver-trace-ablation 概况\\n\\n## 实验状态 (216 个)\\n\\n- **plan013-random-reward-s42**: DONE (failed) — \\n- **plan001-exec-only-s43**: DONE (failed) — \\n- **plan003-eval-exec-only-r5**: DONE (success) — \\n- **plan001-exec-only-s42-r3**: DONE (failed) — \\n- **sta-phase1-exec-sta-r5**: DONE (negative) — \\n- **sta-phase1-exec-only-r5**: DONE (success) — \\n- **sta-phase1-exec-sta-r4**: DONE (negative) — \\n- **sta-phase1-exec-only-r4**: DONE (negative) — \\n- **sta-phase1-exec-only-r3**: DONE (failed) — \\n- **sta-phase1-exec-sta-r3**: DONE (failed) — \\n- **sta-phase1-exec-sta-r2**: DONE (failed) — \\n- **sta-phase1-exec-only-r2**: DONE (failed) — \\n- **sta-phase1-exec-sta**: DONE (failed) — \\n- **sta-phase1-exec-only**: DONE (failed) — \\n- **sta-phase0-baseline**: DONE (success) — \\n\\n## 最新报告\\n# Handover — 2026-05-22\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- d158_llama_sft_s42（准备中）\\n- d154-8b-exec-s42-k4（准备中）\\n- d154-8b-exec-s42-r2（准备中）\\n- d154-8b-exec-s42: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=42. Tests whether larger model (8B vs 4B) exhibits same Goodhart collapse patterns under exec-only reward. Pilot experiment.（准备中）\\n- d154-8b-isr-s43: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=43. Replication of ISR s42 for statistical power at 8B scale.（准备中）\\n- d154-8b-isr-s42: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=42. Tests whether ISR-induced Goodhart collapse (TS dominance) persists at 8B scale, or if larger capacity enables genuine reasoning.（准备中）\\n- d154-8b-exec-s44: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=44. Replication of exec s42 for statistical power across model scale.（准备中）\\n- d154-8b-exec-s43: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=43. Replication of exec s42 for statistical power across model scale.（准备中）\\n- d146-pf-pipeline（准备中）\\n- d144-llama-isr-s43: D144 cross-model: ISR β=0.1 GRPO on LLaMA-3.2-3B/FOLIO seed=43. Replication of ISR s42 for statistical power.（准备中）\\n- …另有 22 项\\n\\n## 近期结论\\n- **exec-only-s45-1000step-k8** (killed): —\\n- **exec-only-s45-1000step** (negative): Exec-only GRPO 1000-step K=4 seed 45: testing whether extended training amplifies structural degeneration beyond 500 steps. Config identical to plan001 series (K=4).\\n- **d154-8b-exec-s42-k8** (negative): 8B K=8 exec-only non-convergence: gradient signal present but insufficient for convergence within 500 steps, resulting in near-zero training reward by step 500 ← 基于 d154-8b-exec-s42-k4v2\\n\\n## 趋势\\n成功 73 / 负向 50 / 失败 49 / 共 184\\nCE_count: 1 →（近 3 次 success）\\nCI_count: 0 →（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-39279: 无 GPU 信息\\n\\n## 告警\\n- sta-phase1-exec-only: 训练失败 — unknown\\n- sta-phase1-exec-sta: 训练失败 — unknown\\n- sta-phase1-exec-only-r2: 训练失败 — unknown\\n- sta-phase1-exec-sta-r2: 训练失败 — unknown\\n- sta-phase1-exec-only-r3: 训练失败 — unknown\\n- sta-phase1-exec-sta-r3: 训练失败 — unknown\\n- plan001-exec-only-s42: 训练失败 — unknown\\n- plan001-exec-only-s42-r3: 训练失败 — unknown\\n- plan001-exec-only-s43: 训练失败 — unknown\\n- plan013-random-reward-s42: 训练失败 — unknown\\n- plan013-random-reward-s42-r2: 训练失败 — unknown\\n- plan001-exec-only-s43-r2: 训练失败 — unknown\\n- plan013-random-reward-s42-r3: 训练失败 — unknown\\n- plan001-exec-only-s43-r3: 训练失败 — unknown\\n- plan006-prolog-exec-s43: 已被终止 — unknown\\n- plan018-additive-random-b01-s43: 训练失败 — unknown\\n- plan009-sft-baseline-s42: 已被终止 — unknown\\n- plan009-sft-baseline-s42-r2: 训练失败 — unknown\\n- plan009-sft-baseline-s42-r3: 训练失败 — unknown\\n- plan006-prolog-exec-s43-r2: 训练失败 — unknown\\n- exp1-isr-b03-s44: 训练失败 — unknown\\n- exp1-random-b03-s44: 训练失败 — unknown\\n- exp1-isr-b03-s43-r2: 已被终止 — unknown\\n- plan015-linear-s42: 已被终止 — unknown\\n- exp1-isr-b03-s43-r4: 已被终止 — unknown\\n- exp1-random-b03-s43-r2: 已被终止 — unknown\\n- exp1-random-b03-s43-r3: 训练失败 — unknown\\n- plan018-additive-ra\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "# 项目 solver-trace-ablation 概况\n\n## 实验状态 (216 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- d158_llama_sft_s42（准备中）\n- d154-8b-exec-s42-k4（准备中）\n- d154-8b-exec-s42-r2（准备中）\n- d154-8b-exec-s42: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=42. Tests whether larger model (8B vs 4B) exhibits same Goodhart collapse patterns under exec-only reward. Pilot experiment.（准备中）\n- d154-8b-isr-s43: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=43. Replication of ISR s42 for statistical power at 8B scale.（准备中）\n- d154-8b-isr-s42: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=42. Tests whether ISR-induced Goodhart collapse (TS dominance) persists at 8B scale, or if larger capacity enables genuine reasoning.（准备中）\n- d154-8b-exec-s44: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=44. Replication of exec s42 for statistical power across model scale.（准备中）\n- d154-8b-exec-s43: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=43. Replication of exec s42 for statistical power across model scale.（准备中）\n- d146-pf-pipeline（准备中）\n- d144-llama-isr-s43: D144 cross-model: ISR β=0.1 GRPO on LLaMA-3.2-3B/FOLIO seed=43. Replication of ISR s42 for statistical power.（准备中）\n- …另有 22 项\n\n## 近期结论\n- **exec-only-s45-1000step-k8** (killed): —\n- **exec-only-s45-1000step** (negative): Exec-only GRPO 1000-step K=4 seed 45: testing whether extended training amplifies structural degeneration beyond 500 steps. Config identical to plan001 series (K=4).\n- **d154-8b-exec-s42-k8** (negative): 8B K=8 exec-only non-convergence: gradient signal present but insufficient for convergence within 500 steps, resulting in near-zero training reward by step 500 ← 基于 d154-8b-exec-s42-k4v2\n\n## 趋势\n成功 73 / 负向 50 / 失败 49 / 共 184\nCE_count: 1 →（近 3 次 success）\nCI_count: 0 →（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-39279: 无 GPU 信息\n\n## 告警\n- sta-phase1-exec-only: 训练失败 — unknown\n- sta-phase1-exec-sta: 训练失败 — unknown\n- sta-phase1-exec-only-r2: 训练失败 — unknown\n- sta-phase1-exec-sta-r2: 训练失败 — unknown\n- sta-phase1-exec-only-r3: 训练失败 — unknown\n- sta-phase1-exec-sta-r3: 训练失败 — unknown\n- plan001-exec-only-s42: 训练失败 — unknown\n- plan001-exec-only-s42-r3: 训练失败 — unknown\n- plan001-exec-only-s43: 训练失败 — unknown\n- plan013-random-reward-s42: 训练失败 — unknown\n- plan013-random-reward-s42-r2: 训练失败 — unknown\n- plan001-exec-only-s43-r2: 训练失败 — unknown\n- plan013-random-reward-s42-r3: 训练失败 — unknown\n- plan001-exec-only-s43-r3: 训练失败 — unknown\n- plan006-prolog-exec-s43: 已被终止 — unknown\n- plan018-additive-random-b01-s43: 训练失败 — unknown\n- plan009-sft-baseline-s42: 已被终止 — unknown\n- plan009-sft-baseline-s42-r2: 训练失败 — unknown\n- plan009-sft-baseline-s42-r3: 训练失败 — unknown\n- plan006-prolog-exec-s43-r2: 训练失败 — unknown\n- exp1-isr-b03-s44: 训练失败 — unknown\n- exp1-random-b03-s44: 训练失败 — unknown\n- exp1-isr-b03-s43-r2: 已被终止 — unknown\n- plan015-linear-s42: 已被终止 — unknown\n- exp1-isr-b03-s43-r4: 已被终止 — unknown\n- exp1-random-b03-s43-r2: 已被终止 — unknown\n- exp1-random-b03-s43-r3: 训练失败 — unknown\n- plan018-additive-ra"
    }
  },
  "sourceToolAssistantUUID": "7b91a6fc-597b-4b74-980b-ba348296e7a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-25T03:55:26.580Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01LChPRVLzTghziq3FUtKwfe`</summary>

```json
{
  "pattern": "**/docs/paper/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce8f4db6-961d-48ff-a062-a98b8de63180",
  "isSidechain": false,
  "requestId": "req_011CbNcU5UH9h63SVvbW92Cz",
  "type": "assistant",
  "uuid": "195bc456-5a09-4161-bd70-4754c85c6143",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVCAJSsoGs6XEW2jdQwA2r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3113,
      "cache_read_input_tokens": 33879,
      "output_tokens": 438,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3113,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 438,
          "cache_read_input_tokens": 33879,
          "cache_creation_input_tokens": 3113,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3113
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

_source line 31 · 2026-05-25T03:55:26.623Z_

<details><summary>↩ Tool result · `toolu_01LChPRVLzTghziq3FUtKwfe`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "195bc456-5a09-4161-bd70-4754c85c6143",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "e7bd8525-13e6-46b5-9372-6af61daf6494",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex"
    ],
    "durationMs": 37,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "195bc456-5a09-4161-bd70-4754c85c6143",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-25T03:55:28.007Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ukh5hyFAWaxxPa3PNGLQ2m`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7bd8525-13e6-46b5-9372-6af61daf6494",
  "isSidechain": false,
  "requestId": "req_011CbNcU5UH9h63SVvbW92Cz",
  "type": "assistant",
  "uuid": "661ef08d-3a54-4b0a-8aab-bc8f7aad58c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVCAJSsoGs6XEW2jdQwA2r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3113,
      "cache_read_input_tokens": 33879,
      "output_tokens": 438,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3113,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 438,
          "cache_read_input_tokens": 33879,
          "cache_creation_input_tokens": 3113,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3113
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

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: solver-trace-ablation - 论文路径: projects/solver-trace-ablation/docs/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: Long paper (ARR) - 截止日期: 未提供，请自行调研 - **引用验证**: ❌ 未启用…",
  "leafUuid": "661ef08d-3a54-4b0a-8aab-bc8f7aad58c9",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Review solver-trace-ablation paper for EMNLP 2026",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646"
}
```

---

### Tool result

_source line 35 · 2026-05-25T03:55:28.193Z_

<details><summary>↩ Tool result · `toolu_01Ukh5hyFAWaxxPa3PNGLQ2m`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 4147090 May 25 03:49 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/submitted.pdf
PDF_EXISTS
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "661ef08d-3a54-4b0a-8aab-bc8f7aad58c9",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "f1aa21f3-5a91-4d29-8ff4-65a47b2ec1c4",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 4147090 May 25 03:49 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/submitted.pdf\nPDF_EXISTS",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "661ef08d-3a54-4b0a-8aab-bc8f7aad58c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-25T03:55:29.839Z_

<details><summary>↩ Tool result · `toolu_01ARrnpfjf64najihzwtL6Gk`</summary>

```text
Web search results for query: "EMNLP 2026 call for papers submission deadline ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"MRL Workshop at EMNLP 2025: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/mrl-workshop-emnlp-2025-first-call-papers"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the search results, I found information about EMNLP 2026 and ARR submission deadlines, though the main conference call for papers wasn't directly returned. However, here's what I found about EMNLP 2026 related deadlines:

For the MINT workshop co-located with EMNLP 2026, the ARR paper submission deadline is May 25, 2026, which coincidentally is today's date. The direct paper submission deadline for this workshop is July 8, 2026, and the pre-reviewed ARR commitment deadline is August 24, 2026.

Additionally, for the 2nd BabyLM Workshop at EMNLP 2026, the ARR submission deadline is May 25, 2026, with a direct submissions deadline in mid-July and an ARR commitment deadline in early August.

If you're looking for the main EMNLP 2026 conference call for papers specifically, I'd recommend visiting the official EMNLP 2026 website or the ACL portal directly, as the search results primarily returned information about workshops and tutorials affiliated with the conference rather than the main conference call.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdf2f58b-6070-454d-94e0-0f2dce312f99",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "ef6b4b4f-f53b-4067-99d4-5eddf59e586b",
  "toolUseResult": {
    "query": "EMNLP 2026 call for papers submission deadline ARR site:aclweb.org",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DxXVfcQFbHz2WeodH1xw6J",
        "content": [
          {
            "title": "Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"
          },
          {
            "title": "Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"
          },
          {
            "title": "The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026",
            "url": "https://2026.aclweb.org/"
          },
          {
            "title": "EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"
          },
          {
            "title": "[EMNLP 2025] First Call for Papers | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"
          },
          {
            "title": "*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"
          },
          {
            "title": "Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"
          },
          {
            "title": "The 2nd BabyLM Workshop | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/2nd-babylm-workshop"
          },
          {
            "title": "MRL Workshop at EMNLP 2025: First Call for Papers | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/mrl-workshop-emnlp-2025-first-call-papers"
          },
          {
            "title": "Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1",
            "url": "https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"
          }
        ]
      },
      "Based on the search results, I found information about EMNLP 2026 and ARR submission deadlines, though the main conference call for papers wasn't directly returned. However, here's what I found about EMNLP 2026 related deadlines:\n\nFor the MINT workshop co-located with EMNLP 2026, the ARR paper submission deadline is May 25, 2026, which coincidentally is today's date. The direct paper submission deadline for this workshop is July 8, 2026, and the pre-reviewed ARR commitment deadline is August 24, 2026.\n\nAdditionally, for the 2nd BabyLM Workshop at EMNLP 2026, the ARR submission deadline is May 25, 2026, with a direct submissions deadline in mid-July and an ARR commitment deadline in early August.\n\nIf you're looking for the main EMNLP 2026 conference call for papers specifically, I'd recommend visiting the official EMNLP 2026 website or the ACL portal directly, as the search results primarily returned information about workshops and tutorials affiliated with the conference rather than the main conference call."
    ],
    "durationSeconds": 4.9922130500000055
  },
  "sourceToolAssistantUUID": "fdf2f58b-6070-454d-94e0-0f2dce312f99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 37 · 2026-05-25T03:55:29.842Z_

```json
{
  "parentUuid": "ef6b4b4f-f53b-4067-99d4-5eddf59e586b",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "51ac9362-916c-4384-9779-fcfee93281f8",
  "timestamp": "2026-05-25T03:55:29.842Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 38 · 2026-05-25T03:55:33.526Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Let me:
1. Search more specifically for EMNLP 2026 main conference CFP and ARR deadlines
2. Read the paper main.tex to understand what we're reviewing
3. Check for external review configuration

Let me search for the EMNLP 2026 CFP more specifically and read the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51ac9362-916c-4384-9779-fcfee93281f8",
  "isSidechain": false,
  "requestId": "req_011CbNcVajT3NZEYJM77wLD2",
  "type": "assistant",
  "uuid": "0b75a3b4-d08a-4a2b-ac9c-fc07a0d44886",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8HyJe5SVbRnd3wNfXU4uP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 160,
      "cache_creation_input_tokens": 3453,
      "cache_read_input_tokens": 36992,
      "output_tokens": 321,
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
          "input_tokens": 160,
          "output_tokens": 321,
          "cache_read_input_tokens": 36992,
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

_source line 39 · 2026-05-25T03:55:34.943Z_

论文文件和 PDF 均存在。需要进一步确认 EMNLP 2026 主会议 deadline。同时开始读论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b75a3b4-d08a-4a2b-ac9c-fc07a0d44886",
  "isSidechain": false,
  "requestId": "req_011CbNcVajT3NZEYJM77wLD2",
  "type": "assistant",
  "uuid": "03605cc2-6723-4d8b-83cb-c0767f249b71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8HyJe5SVbRnd3wNfXU4uP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 160,
      "cache_creation_input_tokens": 3453,
      "cache_read_input_tokens": 36992,
      "output_tokens": 321,
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
          "input_tokens": 160,
          "output_tokens": 321,
          "cache_read_input_tokens": 36992,
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

_source line 40 · 2026-05-25T03:55:35.433Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WYohafp7pN58Gyw65Ts5g1`</summary>

```json
{
  "query": "EMNLP 2026 main conference submission deadline ARR cycle"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03605cc2-6723-4d8b-83cb-c0767f249b71",
  "isSidechain": false,
  "requestId": "req_011CbNcVajT3NZEYJM77wLD2",
  "type": "assistant",
  "uuid": "65e82af7-940f-4485-85ed-85b5c3b8080f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8HyJe5SVbRnd3wNfXU4uP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 160,
      "cache_creation_input_tokens": 3453,
      "cache_read_input_tokens": 36992,
      "output_tokens": 321,
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
          "input_tokens": 160,
          "output_tokens": 321,
          "cache_read_input_tokens": 36992,
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

_source line 41 · 2026-05-25T03:55:36.307Z_

<details><summary>↩ Tool result · `toolu_01T5r39Z5Z4g68ha5xbgDgUR`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage{float}
13	\usepackage{placeins}
14	\usepackage[protrusion=true,expansion=false]{microtype}
15	
16	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
17	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
18	\setlength{\abovecaptionskip}{4pt}
19	\setlength{\belowcaptionskip}{2pt}
20	
21	\graphicspath{{figures/}}
22	
23	\title{Observe but Don't Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning}
24	
25	\author{Anonymous ACL submission}
26	
27	\begin{document}
28	\maketitle
29	
30	\input{abstract}
31	\input{introduction}
32	\input{related_work}
33	\input{method}
34	\input{experiments}
35	\input{conclusion}
36	
37	\input{limitations}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{appendix}
43	
44	\end{document}
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85e9682d-6dde-4061-ac3c-1dec8322adb6",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "1ac255c1-08a5-42c4-8d9e-6df32db84fea",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\\usepackage{enumitem}\n\\usepackage{xcolor}\n\\usepackage{multirow}\n\\usepackage{float}\n\\usepackage{placeins}\n\\usepackage[protrusion=true,expansion=false]{microtype}\n\n\\setlength{\\textfloatsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\intextsep}{6pt plus 2pt minus 2pt}\n\\setlength{\\abovecaptionskip}{4pt}\n\\setlength{\\belowcaptionskip}{2pt}\n\n\\graphicspath{{figures/}}\n\n\\title{Observe but Don't Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning}\n\n\\author{Anonymous ACL submission}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{experiments}\n\\input{conclusion}\n\n\\input{limitations}\n\n\\bibliography{references}\n\n\\appendix\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 45,
      "startLine": 1,
      "totalLines": 45
    }
  },
  "sourceToolAssistantUUID": "85e9682d-6dde-4061-ac3c-1dec8322adb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-25T03:55:35.910Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016SeL9qR5KkR1xVEvbHETDs`</summary>

```json
{
  "query": "\"EMNLP 2026\" commitment deadline date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65e82af7-940f-4485-85ed-85b5c3b8080f",
  "isSidechain": false,
  "requestId": "req_011CbNcVajT3NZEYJM77wLD2",
  "type": "assistant",
  "uuid": "1e585d2d-59dc-4825-af7a-fcedeb83e320",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8HyJe5SVbRnd3wNfXU4uP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 160,
      "cache_creation_input_tokens": 3453,
      "cache_read_input_tokens": 36992,
      "output_tokens": 321,
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
          "input_tokens": 160,
          "output_tokens": 321,
          "cache_read_input_tokens": 36992,
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

_source line 43 · 2026-05-25T03:55:36.300Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T5r39Z5Z4g68ha5xbgDgUR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e585d2d-59dc-4825-af7a-fcedeb83e320",
  "isSidechain": false,
  "requestId": "req_011CbNcVajT3NZEYJM77wLD2",
  "type": "assistant",
  "uuid": "85e9682d-6dde-4061-ac3c-1dec8322adb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8HyJe5SVbRnd3wNfXU4uP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 160,
      "cache_creation_input_tokens": 3453,
      "cache_read_input_tokens": 36992,
      "output_tokens": 321,
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
          "input_tokens": 160,
          "output_tokens": 321,
          "cache_read_input_tokens": 36992,
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

_source line 44 · 2026-05-25T03:55:38.829Z_

<details><summary>↩ Tool result · `toolu_016SeL9qR5KkR1xVEvbHETDs`</summary>

```text
Web search results for query: ""EMNLP 2026" commitment deadline date"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 - Conference on Empirical Methods in Natural Language Processing Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/emnlp"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Update EMNLP System Demonstrations Track with 2026 conference data · huggingface/ai-deadlines at 6a94f2c","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/6a94f2c940ba976564775b34f6b224b0f9ad638d"}]

Based on the search results, the EMNLP 2026 commitment deadline is August 2, 2026. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e585d2d-59dc-4825-af7a-fcedeb83e320",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "d6803536-d640-4320-a510-8d284fb0bfb5",
  "toolUseResult": {
    "query": "\"EMNLP 2026\" commitment deadline date",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LEdcJUu9ZbdAfCjjBViCiA",
        "content": [
          {
            "title": "Call for Main Conference Papers - EMNLP 2026",
            "url": "https://2026.emnlp.org/calls/main_conference_papers/"
          },
          {
            "title": "Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"
          },
          {
            "title": "emnlp 2026 - AI Conference Deadlines",
            "url": "https://mlciv.com/ai-deadlines/conference/?id=emnlp26"
          },
          {
            "title": "EMNLP 2026 : The 2026 Conference on Empirical Methods in N",
            "url": "https://callforpaper.org/call-for-papers-emnlp-2026"
          },
          {
            "title": "LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)",
            "url": "https://linguistlist.org/issues/37/972/"
          },
          {
            "title": "AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML",
            "url": "https://mlciv.com/ai-deadlines/"
          },
          {
            "title": "EMNLP 2026 Conference Deadline | Live Countdown Tracker",
            "url": "https://www.getpaperpilot.com/deadlines/emnlp-2026.html"
          },
          {
            "title": "EMNLP 2026 - Conference on Empirical Methods in Natural Language Processing Deadline | ConferenceDeadlines.com",
            "url": "https://www.conferencedeadlines.com/venue/emnlp"
          },
          {
            "title": "Dates and Venues",
            "url": "http://aclrollingreview.org/dates"
          },
          {
            "title": "Update EMNLP System Demonstrations Track with 2026 conference data · huggingface/ai-deadlines at 6a94f2c",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/6a94f2c940ba976564775b34f6b224b0f9ad638d"
          }
        ]
      },
      "Based on the search results, the EMNLP 2026 commitment deadline is August 2, 2026. All deadlines are 11:59PM UTC-12:00 (\"anywhere on Earth\")."
    ],
    "durationSeconds": 2.9158458870000032
  },
  "sourceToolAssistantUUID": "1e585d2d-59dc-4825-af7a-fcedeb83e320",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-25T03:55:40.625Z_

<details><summary>↩ Tool result · `toolu_01WYohafp7pN58Gyw65Ts5g1`</summary>

```text
Web search results for query: "EMNLP 2026 main conference submission deadline ARR cycle"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here's the information about EMNLP 2026's main conference submission deadline for the ARR cycle:

## EMNLP 2026 ARR Submission Deadline

The Final ARR Submission Date for EMNLP 2026 is May 25, 2026. This corresponds to the ARR 2026 May cycle.

## Key Details

All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors need to explicitly declare which conference they intend to commit to at submission time. This choice will be binding for EMNLP 2026: i.e., ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.

## Commitment Timeline

The commitment date for EMNLP 2026 is August 2, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65e82af7-940f-4485-85ed-85b5c3b8080f",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "e8c6e40e-57b0-4f33-a353-7bb1784b948d",
  "toolUseResult": {
    "query": "EMNLP 2026 main conference submission deadline ARR cycle",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Hwefc883Cm3wZWZMn86CGu",
        "content": [
          {
            "title": "Call for Main Conference Papers - EMNLP 2026",
            "url": "https://2026.emnlp.org/calls/main_conference_papers/"
          },
          {
            "title": "Dates and Venues",
            "url": "http://aclrollingreview.org/dates"
          },
          {
            "title": "AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML",
            "url": "https://mlciv.com/ai-deadlines/"
          },
          {
            "title": "Call for Main Conference Papers -",
            "url": "https://2026.eacl.org/calls/papers/"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X",
            "url": "https://x.com/emnlpmeeting/status/2029508292637061462"
          },
          {
            "title": "EMNLP 2026 : The 2026 Conference on Empirical Methods in N",
            "url": "https://callforpaper.org/call-for-papers-emnlp-2026"
          },
          {
            "title": "aclrollingreview/dates.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/dates.md"
          },
          {
            "title": "Call for workshops: EMNLP & AACL",
            "url": "https://groups.google.com/g/ml-news/c/W-fucfhVto4"
          }
        ]
      },
      "Based on the search results, here's the information about EMNLP 2026's main conference submission deadline for the ARR cycle:\n\n## EMNLP 2026 ARR Submission Deadline\n\nThe Final ARR Submission Date for EMNLP 2026 is May 25, 2026. This corresponds to the ARR 2026 May cycle.\n\n## Key Details\n\nAll deadlines are 11:59PM UTC-12:00 (\"anywhere on Earth\").\n\nGiven that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors need to explicitly declare which conference they intend to commit to at submission time. This choice will be binding for EMNLP 2026: i.e., ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.\n\n## Commitment Timeline\n\nThe commitment date for EMNLP 2026 is August 2, 2026."
    ],
    "durationSeconds": 5.187150743999998
  },
  "sourceToolAssistantUUID": "65e82af7-940f-4485-85ed-85b5c3b8080f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-25T03:55:44.325Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me get the official CFP page for full details, and read the paper content files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8c6e40e-57b0-4f33-a353-7bb1784b948d",
  "isSidechain": false,
  "requestId": "req_011CbNcWPSKvVv5y5s86pivL",
  "type": "assistant",
  "uuid": "e2f8b6be-5331-4249-a6b2-1a06df29634f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W259rRfAjm2t464T54cCZU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1121,
      "cache_creation_input_tokens": 1265,
      "cache_read_input_tokens": 40445,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1265,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1121,
          "output_tokens": 442,
          "cache_read_input_tokens": 40445,
          "cache_creation_input_tokens": 1265,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1265
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

_source line 47 · 2026-05-25T03:55:46.657Z_

EMNLP 2026 ARR submission deadline 是今天（2026-05-25），commitment deadline 是 2026-08-02。Deadline 尚未过期。现在获取完整 venue 要求并读论文各章节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2f8b6be-5331-4249-a6b2-1a06df29634f",
  "isSidechain": false,
  "requestId": "req_011CbNcWPSKvVv5y5s86pivL",
  "type": "assistant",
  "uuid": "75aeeeca-6c77-4970-8fc2-39e8cdca3e17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W259rRfAjm2t464T54cCZU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1121,
      "cache_creation_input_tokens": 1265,
      "cache_read_input_tokens": 40445,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1265,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1121,
          "output_tokens": 442,
          "cache_read_input_tokens": 40445,
          "cache_creation_input_tokens": 1265,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1265
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

_source line 48 · 2026-05-25T03:55:48.939Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ren47RHHaWwQdtU7xrZEex`</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract the full submission requirements: page limits for long/short papers, template requirements, anonymity rules, appendix rules, citation format, any special formatting requirements, and all important dates/deadlines."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75aeeeca-6c77-4970-8fc2-39e8cdca3e17",
  "isSidechain": false,
  "requestId": "req_011CbNcWPSKvVv5y5s86pivL",
  "type": "assistant",
  "uuid": "65f5bd6c-d43d-4257-98e8-91f2bca45662",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W259rRfAjm2t464T54cCZU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1121,
      "cache_creation_input_tokens": 1265,
      "cache_read_input_tokens": 40445,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1265,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1121,
          "output_tokens": 442,
          "cache_read_input_tokens": 40445,
          "cache_creation_input_tokens": 1265,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1265
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

_source line 49 · 2026-05-25T03:55:51.619Z_

<details><summary>↩ Tool result · `toolu_016u95ocEaJkswDkZfN7Kvsb`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task and GRPO Training}
5	\label{sec:task}
6	
7	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$.
8	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
9	This optimizes prove rate but provides no signal about \emph{component necessity} (Figure~\ref{fig:sta-overview}a): a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
10	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation set (100 examples) contains 34 True, 25 False, and 41 Unknown labels, with only True-labeled examples admitting valid proofs (theoretical PR ceiling ${\sim}34\%$).
11	Exec-only GRPO reaching $\text{PR}{=}93\%$ (\S\ref{sec:diagnostic})---nearly $3\times$ this ceiling---confirms the solver accepts formalizations for nominally unprovable examples, constituting direct evidence of structural gaming independent of ISR.
12	
13	\subsection{Solver Trace Ablation (STA)}
14	\label{sec:sta}
15	
16	\begin{figure*}[t]
17	\centering
18	\includegraphics[width=\textwidth]{figures/fig1_sta_overview.pdf}
19	\caption{STA overview. \textbf{(a)}~The formalization pipeline: an LLM translates natural-language (NL) premises into formal logic, verified by an external solver. \textbf{(b)}~STA removes each component in turn and re-runs the solver; the fraction of necessary components yields ISR. \textbf{(c)}~Applied post-hoc, ISR detects structural hacking; repurposed as reward, it triggers a Goodhart effect where tautological shortcuts (TS) achieve $\text{ISR}{=}1$ by construction.}
20	\label{fig:sta-overview}
21	\end{figure*}
22	
23	STA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\ref{fig:sta-overview}; Algorithm~\ref{alg:sta}).
24	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
25	A component is \emph{necessary} if its removal causes proof failure.
26	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
27	LOO ablation itself is standard in mutation testing and sensitivity analysis~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.
28	
29	\begin{algorithm}[t]
30	\caption{Solver Trace Ablation (STA)}
31	\label{alg:sta}
32	\begin{algorithmic}[1]
33	\REQUIRE Proved formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
34	\ENSURE $\text{ISR}(x) \in [0, 1]$
35	\STATE $\textit{necessary} \gets 0$
36	\FOR{$i = 1$ to $n$}
37	    \IF{$S(x \setminus \{c_i\}) = \textit{failed}$}
38	        \STATE $\textit{necessary} \gets \textit{necessary} + 1$
39	    \ENDIF
40	\ENDFOR
41	\RETURN $\textit{necessary} \,/\, n$
42	\end{algorithmic}
43	\end{algorithm}
44	
45	\paragraph{Intensional Structural Reward.}\footnote{Not \emph{intentional}; \emph{intensional} contrasts with extensional (execution-only) evaluation.}
46	For a proved formalization $x = \{c_1, \ldots, c_n\}$, ISR is the fraction of necessary components:
47	\begin{equation}
48	  \text{ISR}(x) = \frac{1}{n}\sum_{i=1}^{n}\mathbf{1}\bigl[S(x\setminus\{c_i\})=\textit{failed}\bigr]
49	  \label{eq:isr}
50	\end{equation}
51	ISR is defined only for proved formalizations: ISR${=}1$ means every component is necessary; ISR${=}0$ means complete redundancy.
52	An ISR of zero for proved samples can arise from structural degeneration or genuine redundancy; our hacking mode classification (\S\ref{sec:taxonomy-method}) disambiguates these cases, with ${>}90\%$ of low-ISR proved samples exhibiting identifiable hacking patterns.
53	ISR is a special case of the $(n{-}1)$-coalition Shapley value~\citep{lundberg2017unified}, reducing complexity from $O(2^n)$ to $O(n)$; the binary solver output makes LOO sufficient for testing necessity.
54	ISR quantifies component redundancy, not semantic faithfulness; its diagnostic value is realized through the downstream mode breakdown (\S\ref{sec:taxonomy}), not the scalar alone.
55	In practice, ISR serves as a screening trigger: anomalously low (or high) values flag samples for mode-level classification (\S\ref{sec:taxonomy-method}), which provides the definitive diagnostic.
56	We report \emph{proved-only} ISR (denoted ISR$^*$) throughout to avoid conflating component necessity with prove rate.
57	
58	\paragraph{LOO independence assumption.}
59	LOO ablation tests individual, not joint, component necessity~\citep{jia-harman-survey}, systematically underestimating ISR when jointly-necessary components exist; the observed collapse is therefore conservative.
60	
61	\subsection{Reward Conditions and Hacking Modes}
62	\label{sec:rewards}
63	\label{sec:taxonomy-method}
64	
65	We study six conditions: exec-only ($r_{\text{exec}}$), ISR low/high-dose ($r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ at $\beta\in\{0.1,0.3\}$), matched random controls ($r_{\text{exec}}\cdot(1{+}\beta u)$, $u\sim\mathcal{U}(0,1)$), and a supervised fine-tuning (SFT) baseline (negative log-likelihood on gold formalizations).
66	Multiplicative bonuses apply only to proved samples, keeping the prove-rate floor intact.
67	Random isolates ISR-specific signal from generic reward-variance effects; SFT isolates whether structural degeneration arises from RL optimization or data exposure alone.
68	Each RL condition uses seeds $\{42,43,44\}$ and identical training data (formulation alternatives in Appendix~\ref{app:setup}).
69	
70	\begin{table*}[t]
71	\centering
72	\small
73	\begin{tabular}{lcccccc}
74	\toprule
75	\textbf{Condition} & $\boldsymbol{\beta}$ & \textbf{PR\%}$\uparrow$ & \textbf{ISR}$^*$ & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} \\
76	\midrule
77	Base (0-shot) & --- & 12 & --- & --- & --- & --- \\ %% registry: sta-phase0-baseline
78	SFT & --- & 13 & 0.595 & 0 & 8 & \textbf{92} \\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)
79	\midrule
80	Exec-only$^\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\ %% registry: plan001-exec-only-s42-r2 (PG corrected)
81	ISR (3-seed) & 0.1 & 77{\scriptsize$\pm$14} & $1.06\times^\ddagger$ & \textbf{71}$^\P$ & 18 & 6 \\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)
82	ISR (5-seed) & 0.1 & 70{\scriptsize$\pm$19} & (0.63)$^\ddagger$ & 54 & 18 & 23 \\ %% registry: plan002-additive-b01-s42--s46 (pooled)
83	Random & 0.1 & \textbf{87}{\scriptsize$\pm$8} & 0.117{\scriptsize$\pm$.04} & 14$^\S$ & 69 & 10 \\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)
84	Shuffled-ISR & 0.1 & 15{\scriptsize$\pm$1} & 0.559{\scriptsize$\pm$.02} & 7 & 7 & \textbf{87} \\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)
85	\midrule
86	ISR & 0.3 & 66{\scriptsize$\pm$42} & 0.39{\scriptsize$\pm$.31} & \textbf{50} & 37 & 11 \\ %% registry: plan002-additive-b03-s42, exp1-isr-b03-s43-r3, plan002-additive-b03-s44 (pooled; D106 s43 genuine 23→20)
87	Random & 0.3 & 54{\scriptsize$\pm$35} & 0.09{\scriptsize$\pm$.09} & 7 & 91 & 2 \\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)
88	\bottomrule
89	\end{tabular}
90	\caption{Goodhart landscape across reward conditions. PR = prove rate; ISR$^*$ = proved-only ISR; TS = tautological shortcut; CE = conclusion embedding; N-H = non-hacking (upper bound on genuine reasoning). Multi-seed rows: pooled TS/CE/N-H; PR/ISR$^*$ as mean$\pm$std. $^\dagger$Seed~42 only. $^\ddagger$Premise-count-matched (\S\ref{sec:goodhart}). $^\P$FN-corrected (\S\ref{app:h8}). $^\S$Seed-dependent (s43: 38.3\%). Per-seed data: Table~\ref{tab:fol-detailed}.}
91	\label{tab:goodhart-landscape}
92	\end{table*}
93	
94	\paragraph{Hacking taxonomy.}
95	Across conditions, seeds, and logic types we identify eight structural-degeneration modes (full definitions in Appendix~\ref{app:hacking-modes}), dominated by three: \textbf{CE} (conclusion embedded among multiple premises), \textbf{TS} (single-premise conclusion duplication; targets ISR directly since removing the sole premise forces $\text{ISR}\geq 0.5$), and \textbf{PG} (premise-subset gaming: each component is LOO-necessary but the premise set is incomplete; Appendix~\ref{app:h8}).
96	Five additional modes---tautological collapse, repetition, complexity-without-utility, contradiction explosion, and query-as-fact (Prolog-specific)---appear in specific seeds or conditions.
97	Modes are identified by strict text matching (CE/TS) plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; when patterns overlap, we assign the most specific mode (PG $>$ CE $>$ TS).
98	The non-hacking rate is an upper bound on genuine reasoning.
99	
100	Low ISR signals redundancy under exec-only but metric gaming under ISR-as-reward; the mode breakdown, not the ISR scalar, licenses interpretation.
101	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab809a9c-ff5d-4a5c-8b3f-c3215e854fba",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "c8570156-e936-4eb8-8233-1f10510f1fa2",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Task and GRPO Training}\n\\label{sec:task}\n\nGiven premises $P_1,\\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\\{c_1,\\ldots,c_n\\}$ verified by an external solver $S\\in\\{\\text{Prover9, SWI-Prolog}\\}$.\nWe train with Group Relative Policy Optimization (GRPO)~\\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\\text{exec}}(x) = \\mathbf{1}[S(F_x){=}\\textit{proved}]$.\nThis optimizes prove rate but provides no signal about \\emph{component necessity} (Figure~\\ref{fig:sta-overview}a): a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.\nAll experiments draw from FOLIO~\\citep{folio}; the held-out evaluation set (100 examples) contains 34 True, 25 False, and 41 Unknown labels, with only True-labeled examples admitting valid proofs (theoretical PR ceiling ${\\sim}34\\%$).\nExec-only GRPO reaching $\\text{PR}{=}93\\%$ (\\S\\ref{sec:diagnostic})---nearly $3\\times$ this ceiling---confirms the solver accepts formalizations for nominally unprovable examples, constituting direct evidence of structural gaming independent of ISR.\n\n\\subsection{Solver Trace Ablation (STA)}\n\\label{sec:sta}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig1_sta_overview.pdf}\n\\caption{STA overview. \\textbf{(a)}~The formalization pipeline: an LLM translates natural-language (NL) premises into formal logic, verified by an external solver. \\textbf{(b)}~STA removes each component in turn and re-runs the solver; the fraction of necessary components yields ISR. \\textbf{(c)}~Applied post-hoc, ISR detects structural hacking; repurposed as reward, it triggers a Goodhart effect where tautological shortcuts (TS) achieve $\\text{ISR}{=}1$ by construction.}\n\\label{fig:sta-overview}\n\\end{figure*}\n\nSTA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\\ref{fig:sta-overview}; Algorithm~\\ref{alg:sta}).\nGiven a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\\setminus\\{c_i\\}$ and re-runs the solver (Algorithm~\\ref{alg:sta}).\nA component is \\emph{necessary} if its removal causes proof failure.\nWhat constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.\nLOO ablation itself is standard in mutation testing and sensitivity analysis~\\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.\n\n\\begin{algorithm}[t]\n\\caption{Solver Trace Ablation (STA)}\n\\label{alg:sta}\n\\begin{algorithmic}[1]\n\\REQUIRE Proved formalization $x = \\{c_1, \\ldots, c_n\\}$, solver $S$\n\\ENSURE $\\text{ISR}(x) \\in [0, 1]$\n\\STATE $\\textit{necessary} \\gets 0$\n\\FOR{$i = 1$ to $n$}\n    \\IF{$S(x \\setminus \\{c_i\\}) = \\textit{failed}$}\n        \\STATE $\\textit{necessary} \\gets \\textit{necessary} + 1$\n    \\ENDIF\n\\ENDFOR\n\\RETURN $\\textit{necessary} \\,/\\, n$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\paragraph{Intensional Structural Reward.}\\footnote{Not \\emph{intentional}; \\emph{intensional} contrasts with extensional (execution-only) evaluation.}\nFor a proved formalization $x = \\{c_1, \\ldots, c_n\\}$, ISR is the fraction of necessary components:\n\\begin{equation}\n  \\text{ISR}(x) = \\frac{1}{n}\\sum_{i=1}^{n}\\mathbf{1}\\bigl[S(x\\setminus\\{c_i\\})=\\textit{failed}\\bigr]\n  \\label{eq:isr}\n\\end{equation}\nISR is defined only for proved formalizations: ISR${=}1$ means every component is necessary; ISR${=}0$ means complete redundancy.\nAn ISR of zero for proved samples can arise from structural degeneration or genuine redundancy; our hacking mode classification (\\S\\ref{sec:taxonomy-method}) disambiguates these cases, with ${>}90\\%$ of low-ISR proved samples exhibiting identifiable hacking patterns.\nISR is a special case of the $(n{-}1)$-coalition Shapley value~\\citep{lundberg2017unified}, reducing complexity from $O(2^n)$ to $O(n)$; the binary solver output makes LOO sufficient for testing necessity.\nISR quantifies component redundancy, not semantic faithfulness; its diagnostic value is realized through the downstream mode breakdown (\\S\\ref{sec:taxonomy}), not the scalar alone.\nIn practice, ISR serves as a screening trigger: anomalously low (or high) values flag samples for mode-level classification (\\S\\ref{sec:taxonomy-method}), which provides the definitive diagnostic.\nWe report \\emph{proved-only} ISR (denoted ISR$^*$) throughout to avoid conflating component necessity with prove rate.\n\n\\paragraph{LOO independence assumption.}\nLOO ablation tests individual, not joint, component necessity~\\citep{jia-harman-survey}, systematically underestimating ISR when jointly-necessary components exist; the observed collapse is therefore conservative.\n\n\\subsection{Reward Conditions and Hacking Modes}\n\\label{sec:rewards}\n\\label{sec:taxonomy-method}\n\nWe study six conditions: exec-only ($r_{\\text{exec}}$), ISR low/high-dose ($r_{\\text{exec}}\\cdot(1{+}\\beta\\,\\text{ISR})$ at $\\beta\\in\\{0.1,0.3\\}$), matched random controls ($r_{\\text{exec}}\\cdot(1{+}\\beta u)$, $u\\sim\\mathcal{U}(0,1)$), and a supervised fine-tuning (SFT) baseline (negative log-likelihood on gold formalizations).\nMultiplicative bonuses apply only to proved samples, keeping the prove-rate floor intact.\nRandom isolates ISR-specific signal from generic reward-variance effects; SFT isolates whether structural degeneration arises from RL optimization or data exposure alone.\nEach RL condition uses seeds $\\{42,43,44\\}$ and identical training data (formulation alternatives in Appendix~\\ref{app:setup}).\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (PG corrected)\nISR (3-seed) & 0.1 & 77{\\scriptsize$\\pm$14} & $1.06\\times^\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\nISR (5-seed) & 0.1 & 70{\\scriptsize$\\pm$19} & (0.63)$^\\ddagger$ & 54 & 18 & 23 \\\\ %% registry: plan002-additive-b01-s42--s46 (pooled)\nRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 69 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\nShuffled-ISR & 0.1 & 15{\\scriptsize$\\pm$1} & 0.559{\\scriptsize$\\pm$.02} & 7 & 7 & \\textbf{87} \\\\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42, exp1-isr-b03-s43-r3, plan002-additive-b03-s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. PR = prove rate; ISR$^*$ = proved-only ISR; TS = tautological shortcut; CE = conclusion embedding; N-H = non-hacking (upper bound on genuine reasoning). Multi-seed rows: pooled TS/CE/N-H; PR/ISR$^*$ as mean$\\pm$std. $^\\dagger$Seed~42 only. $^\\ddagger$Premise-count-matched (\\S\\ref{sec:goodhart}). $^\\P$FN-corrected (\\S\\ref{app:h8}). $^\\S$Seed-dependent (s43: 38.3\\%). Per-seed data: Table~\\ref{tab:fol-detailed}.}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\paragraph{Hacking taxonomy.}\nAcross conditions, seeds, and logic types we identify eight structural-degeneration modes (full definitions in Appendix~\\ref{app:hacking-modes}), dominated by three: \\textbf{CE} (conclusion embedded among multiple premises), \\textbf{TS} (single-premise conclusion duplication; targets ISR directly since removing the sole premise forces $\\text{ISR}\\geq 0.5$), and \\textbf{PG} (premise-subset gaming: each component is LOO-necessary but the premise set is incomplete; Appendix~\\ref{app:h8}).\nFive additional modes---tautological collapse, repetition, complexity-without-utility, contradiction explosion, and query-as-fact (Prolog-specific)---appear in specific seeds or conditions.\nModes are identified by strict text matching (CE/TS) plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; when patterns overlap, we assign the most specific mode (PG $>$ CE $>$ TS).\nThe non-hacking rate is an upper bound on genuine reasoning.\n\nLow ISR signals redundancy under exec-only but metric gaming under ISR-as-reward; the mode breakdown, not the ISR scalar, licenses interpretation.\n",
      "numLines": 101,
      "startLine": 1,
      "totalLines": 101
    }
  },
  "sourceToolAssistantUUID": "ab809a9c-ff5d-4a5c-8b3f-c3215e854fba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-25T03:55:50.785Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E71iSRmukemf6rn1eWPw6a`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65f5bd6c-d43d-4257-98e8-91f2bca45662",
  "isSidechain": false,
  "requestId": "req_011CbNcWPSKvVv5y5s86pivL",
  "type": "assistant",
  "uuid": "005959ac-8cdf-4781-a995-ba96e108aef2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W259rRfAjm2t464T54cCZU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1121,
      "cache_creation_input_tokens": 1265,
      "cache_read_input_tokens": 40445,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1265,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1121,
          "output_tokens": 442,
          "cache_read_input_tokens": 40445,
          "cache_creation_input_tokens": 1265,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1265
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

_source line 51 · 2026-05-25T03:55:50.793Z_

<details><summary>↩ Tool result · `toolu_01E71iSRmukemf6rn1eWPw6a`</summary>

```text
1	\begin{abstract}
2	Execution-based evaluation of neurosymbolic reasoning conflates faithful derivation with structural shortcuts: a formalization that trivially embeds the conclusion among its premises proves just as reliably as a genuine one, and reinforcement learning (RL) optimizers exploit this indifference.
3	We propose \emph{component necessity} as a diagnostic principle and operationalize it as \emph{Solver Trace Ablation} (STA): for each proved output, STA tests whether every component is individually required for proof success, yielding the \emph{Intensional Structural Reward} (ISR).
4	ISR reveals that prove-rate gains conceal a compositional shift toward hacking modes, but ISR occupies a paradoxical position: the same leave-one-out structure that makes it informative also makes it gameable.
5	Tautological formalizations satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.
6	In our Qwen3-4B experiments, the resulting Goodhart effect is seed-dependent (3 of 5 seeds converge to gaming, demonstrating that the Goodhart effect occurs frequently but not universally; 2 of 5 retain genuine reasoning), but the \emph{observe-vs-optimize asymmetry} persists across logic types and dataset families---confirmed by cross-logic (Prolog) replication and supported by exploratory cross-benchmark (ProofFOL) evidence: structural proxies for formalization integrity are easier to observe than to optimize.\end{abstract}
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "005959ac-8cdf-4781-a995-ba96e108aef2",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "15b67627-ee62-4f27-8c5e-f74558fe3321",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nExecution-based evaluation of neurosymbolic reasoning conflates faithful derivation with structural shortcuts: a formalization that trivially embeds the conclusion among its premises proves just as reliably as a genuine one, and reinforcement learning (RL) optimizers exploit this indifference.\nWe propose \\emph{component necessity} as a diagnostic principle and operationalize it as \\emph{Solver Trace Ablation} (STA): for each proved output, STA tests whether every component is individually required for proof success, yielding the \\emph{Intensional Structural Reward} (ISR).\nISR reveals that prove-rate gains conceal a compositional shift toward hacking modes, but ISR occupies a paradoxical position: the same leave-one-out structure that makes it informative also makes it gameable.\nTautological formalizations satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.\nIn our Qwen3-4B experiments, the resulting Goodhart effect is seed-dependent (3 of 5 seeds converge to gaming, demonstrating that the Goodhart effect occurs frequently but not universally; 2 of 5 retain genuine reasoning), but the \\emph{observe-vs-optimize asymmetry} persists across logic types and dataset families---confirmed by cross-logic (Prolog) replication and supported by exploratory cross-benchmark (ProofFOL) evidence: structural proxies for formalization integrity are easier to observe than to optimize.\\end{abstract}\n",
      "numLines": 7,
      "startLine": 1,
      "totalLines": 7
    }
  },
  "sourceToolAssistantUUID": "005959ac-8cdf-4781-a995-ba96e108aef2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-25T03:55:51.277Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ECC5TfYboceg8Za6LEqggf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15b67627-ee62-4f27-8c5e-f74558fe3321",
  "isSidechain": false,
  "requestId": "req_011CbNcWPSKvVv5y5s86pivL",
  "type": "assistant",
  "uuid": "26c867af-1299-4250-994c-1ebf587379b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W259rRfAjm2t464T54cCZU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1121,
      "cache_creation_input_tokens": 1265,
      "cache_read_input_tokens": 40445,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1265,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1121,
          "output_tokens": 442,
          "cache_read_input_tokens": 40445,
          "cache_creation_input_tokens": 1265,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1265
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

_source line 53 · 2026-05-25T03:55:51.295Z_

<details><summary>↩ Tool result · `toolu_01ECC5TfYboceg8Za6LEqggf`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A neurosymbolic reasoner can achieve rising prove rate while the internal structure of its proofs collapses entirely.
5	The root cause is evaluation by a single criterion---whether the generated formalization proves under a formal solver---which treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.
6	Under reinforcement learning, this indifference becomes an active vulnerability~\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.
7	
8	Neurosymbolic formalizers~\citep{logic-lm, linc, satlm} and RL-trained variants~\citep{mellgren-prolog-grpo, logic-rl, deepseekmath} rely on execution accuracy alone, with no diagnostic for whether individual components contribute to the proof.
9	Process reward models~\citep{lightman-verify-step, math-shepherd} offer finer granularity but require expensive step-level annotations that do not transfer to solver-backed settings, while inference-time gaming detection~\citep{kim-game-formalization, bondarenko-spec-gaming} identifies gaming post-hoc but provides no training-time structural signal.
10	What is missing is an annotation-free method for testing \emph{component necessity} in neurosymbolic outputs.
11	
12	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic that tests whether each component of a formalization is necessary for proof success.
13	For each proved output, STA removes components one at a time and re-runs the solver; the fraction whose removal breaks the proof yields the \emph{Intensional Structural Reward} (ISR).
14	A formalization where every component is necessary receives $\text{ISR}{=}1$; one that proves regardless of which component is removed receives $\text{ISR}{=}0$.
15	Leave-one-out (LOO) ablation itself is standard~\citep{demillo1978, jia-harman-survey}; our contribution is its systematic application to neurosymbolic outputs, where it reveals a diagnostic--optimization asymmetry (\S\ref{sec:diagnostic}--\ref{sec:goodhart}).
16	
17	\begin{figure}[t]
18	\centering
19	\includegraphics[width=0.95\columnwidth]{figures/fig5_training_isr_curves.pdf}
20	\caption{ISR$^*$ (proved samples only) training trajectories across reward conditions (rolling $w{=}20$). Exec-only collapses to $\text{ISR}{\approx}0$, confirming structural degeneration (\S\ref{sec:diagnostic}); the ${\sim}0.5$ plateau is an $n{=}2$ artifact. ISR $\beta{=}0.1$ seeds rise toward $\text{ISR}{\approx}1$ via TS gaming (Goodhart effect, \S\ref{sec:goodhart}); random remains low.}
21	\label{fig:training-isr-curves}
22	\end{figure}
23	
24	Applied post-hoc, ISR reveals that rising prove rate conceals a compositional shift in proof structure: genuine reasoning gives way to hacking modes---conclusion embedding and tautological shortcuts---invisible to execution-based metrics (Figure~\ref{fig:training-isr-curves}; \S\ref{sec:diagnostic}).
25	
26	Yet the same LOO structure that makes ISR diagnostic also creates a Goodhart vulnerability~\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}: tautological formalizations ($P{\to}P$) satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.
27	This is not an isolated failure of one metric---it exposes a structural risk inherent to the RLVR paradigm: \emph{any} verifiable proxy that rewards structural properties of solver inputs is susceptible to the same exploitation.
28	In our Qwen3-4B experiments, the asymmetry persists across logic types (FOL, Prolog), dataset families (FOLIO, ProofFOL), reward doses, and random seeds, suggesting that structural proxies for formalization integrity are easier to observe than to optimize.
29	
30	We contribute:
31	(\textbf{C1})~STA, a diagnostic method applicable to any solver-verified reasoning system, including the ISR metric, an eight-mode hacking taxonomy, and a cross-domain evaluation protocol (\S\S\ref{sec:sta}--\ref{sec:crossdomain});
32	(\textbf{C2})~empirical characterization of a seed-dependent Goodhart effect when ISR is repurposed as reward, with matched controls ruling out confounds (\S\ref{sec:goodhart});
33	(\textbf{C3})~cross-logic replication (FOL/Prolog) confirming that the Goodhart effect transfers across logic types, with exploratory cross-dataset evidence (FOLIO/ProofFOL; \S\ref{sec:crossdomain}).
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26c867af-1299-4250-994c-1ebf587379b1",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "f0046171-9ce2-4ad4-b7ee-bb7deb02a43d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nA neurosymbolic reasoner can achieve rising prove rate while the internal structure of its proofs collapses entirely.\nThe root cause is evaluation by a single criterion---whether the generated formalization proves under a formal solver---which treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.\nUnder reinforcement learning, this indifference becomes an active vulnerability~\\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.\n\nNeurosymbolic formalizers~\\citep{logic-lm, linc, satlm} and RL-trained variants~\\citep{mellgren-prolog-grpo, logic-rl, deepseekmath} rely on execution accuracy alone, with no diagnostic for whether individual components contribute to the proof.\nProcess reward models~\\citep{lightman-verify-step, math-shepherd} offer finer granularity but require expensive step-level annotations that do not transfer to solver-backed settings, while inference-time gaming detection~\\citep{kim-game-formalization, bondarenko-spec-gaming} identifies gaming post-hoc but provides no training-time structural signal.\nWhat is missing is an annotation-free method for testing \\emph{component necessity} in neurosymbolic outputs.\n\nWe address this gap with \\emph{Solver Trace Ablation} (STA), a diagnostic that tests whether each component of a formalization is necessary for proof success.\nFor each proved output, STA removes components one at a time and re-runs the solver; the fraction whose removal breaks the proof yields the \\emph{Intensional Structural Reward} (ISR).\nA formalization where every component is necessary receives $\\text{ISR}{=}1$; one that proves regardless of which component is removed receives $\\text{ISR}{=}0$.\nLeave-one-out (LOO) ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; our contribution is its systematic application to neurosymbolic outputs, where it reveals a diagnostic--optimization asymmetry (\\S\\ref{sec:diagnostic}--\\ref{sec:goodhart}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig5_training_isr_curves.pdf}\n\\caption{ISR$^*$ (proved samples only) training trajectories across reward conditions (rolling $w{=}20$). Exec-only collapses to $\\text{ISR}{\\approx}0$, confirming structural degeneration (\\S\\ref{sec:diagnostic}); the ${\\sim}0.5$ plateau is an $n{=}2$ artifact. ISR $\\beta{=}0.1$ seeds rise toward $\\text{ISR}{\\approx}1$ via TS gaming (Goodhart effect, \\S\\ref{sec:goodhart}); random remains low.}\n\\label{fig:training-isr-curves}\n\\end{figure}\n\nApplied post-hoc, ISR reveals that rising prove rate conceals a compositional shift in proof structure: genuine reasoning gives way to hacking modes---conclusion embedding and tautological shortcuts---invisible to execution-based metrics (Figure~\\ref{fig:training-isr-curves}; \\S\\ref{sec:diagnostic}).\n\nYet the same LOO structure that makes ISR diagnostic also creates a Goodhart vulnerability~\\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}: tautological formalizations ($P{\\to}P$) satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.\nThis is not an isolated failure of one metric---it exposes a structural risk inherent to the RLVR paradigm: \\emph{any} verifiable proxy that rewards structural properties of solver inputs is susceptible to the same exploitation.\nIn our Qwen3-4B experiments, the asymmetry persists across logic types (FOL, Prolog), dataset families (FOLIO, ProofFOL), reward doses, and random seeds, suggesting that structural proxies for formalization integrity are easier to observe than to optimize.\n\nWe contribute:\n(\\textbf{C1})~STA, a diagnostic method applicable to any solver-verified reasoning system, including the ISR metric, an eight-mode hacking taxonomy, and a cross-domain evaluation protocol (\\S\\S\\ref{sec:sta}--\\ref{sec:crossdomain});\n(\\textbf{C2})~empirical characterization of a seed-dependent Goodhart effect when ISR is repurposed as reward, with matched controls ruling out confounds (\\S\\ref{sec:goodhart});\n(\\textbf{C3})~cross-logic replication (FOL/Prolog) confirming that the Goodhart effect transfers across logic types, with exploratory cross-dataset evidence (FOLIO/ProofFOL; \\S\\ref{sec:crossdomain}).\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  },
  "sourceToolAssistantUUID": "26c867af-1299-4250-994c-1ebf587379b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-25T03:55:51.614Z_

<details open><summary>🔧 Tool call — Read · `toolu_016u95ocEaJkswDkZfN7Kvsb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0046171-9ce2-4ad4-b7ee-bb7deb02a43d",
  "isSidechain": false,
  "requestId": "req_011CbNcWPSKvVv5y5s86pivL",
  "type": "assistant",
  "uuid": "ab809a9c-ff5d-4a5c-8b3f-c3215e854fba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W259rRfAjm2t464T54cCZU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1121,
      "cache_creation_input_tokens": 1265,
      "cache_read_input_tokens": 40445,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1265,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1121,
          "output_tokens": 442,
          "cache_read_input_tokens": 40445,
          "cache_creation_input_tokens": 1265,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1265
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

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: solver-trace-ablation - 论文路径: projects/solver-trace-ablation/docs/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: Long paper (ARR) - 截止日期: 未提供，请自行调研 - **引用验证**: ❌ 未启用…",
  "leafUuid": "c8570156-e936-4eb8-8233-1f10510f1fa2",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Review solver-trace-ablation paper for EMNLP 2026",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646"
}
```

---

### Tool result

_source line 57 · 2026-05-25T03:55:54.115Z_

<details><summary>↩ Tool result · `toolu_01Ren47RHHaWwQdtU7xrZEex`</summary>

```text
# EMNLP 2026 Submission Requirements Summary

## Page Limits
- **Long Papers:** 8 pages (9 pages allowed in camera-ready to address reviewer feedback)
- **Short Papers:** 4 pages (5 pages allowed in camera-ready)

## Key Deadlines
- ARR submission: May 25, 2026
- Reviewer registration: May 27, 2026
- Author response period: July 7–13, 2026
- Meta-review release: July 30, 2026
- EMNLP commitment deadline: August 2, 2026
- Acceptance notification: August 20, 2026
- Camera-ready due: September 20, 2026
- Conference dates: October 24–29, 2026

*All deadlines: 11:59 PM UTC-12:00*

## Anonymity & Review Process
The document states: "The reviewing process will continue to be double-blind. Reviewers will not see authors, nor will authors see reviewers." Reviews remain confidential on ARR but authors may opt to make their anonymized submissions publicly visible.

## Template & Format Requirements
Authors must follow all ARR submission requirements, including official templates and formatting guidelines available through the ACL Rolling Review platform.

## Appendices & Supplementary Materials
Optional supplementary materials, appendices, software, and data submissions are permitted per ARR guidelines.

## Citation Requirements
Follow ARR citation and comparison standards (specific format details referenced but not detailed in this document).

## Ethics & Integrity
Authors must adhere to the ACL Publication Ethics Policy and complete the "responsible NLP research checklist."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65f5bd6c-d43d-4257-98e8-91f2bca45662",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "fe93fb00-529e-4d3f-91cd-e4d229d18418",
  "toolUseResult": {
    "bytes": 26230,
    "code": 200,
    "codeText": "OK",
    "result": "# EMNLP 2026 Submission Requirements Summary\n\n## Page Limits\n- **Long Papers:** 8 pages (9 pages allowed in camera-ready to address reviewer feedback)\n- **Short Papers:** 4 pages (5 pages allowed in camera-ready)\n\n## Key Deadlines\n- ARR submission: May 25, 2026\n- Reviewer registration: May 27, 2026\n- Author response period: July 7–13, 2026\n- Meta-review release: July 30, 2026\n- EMNLP commitment deadline: August 2, 2026\n- Acceptance notification: August 20, 2026\n- Camera-ready due: September 20, 2026\n- Conference dates: October 24–29, 2026\n\n*All deadlines: 11:59 PM UTC-12:00*\n\n## Anonymity & Review Process\nThe document states: \"The reviewing process will continue to be double-blind. Reviewers will not see authors, nor will authors see reviewers.\" Reviews remain confidential on ARR but authors may opt to make their anonymized submissions publicly visible.\n\n## Template & Format Requirements\nAuthors must follow all ARR submission requirements, including official templates and formatting guidelines available through the ACL Rolling Review platform.\n\n## Appendices & Supplementary Materials\nOptional supplementary materials, appendices, software, and data submissions are permitted per ARR guidelines.\n\n## Citation Requirements\nFollow ARR citation and comparison standards (specific format details referenced but not detailed in this document).\n\n## Ethics & Integrity\nAuthors must adhere to the ACL Publication Ethics Policy and complete the \"responsible NLP research checklist.\"",
    "durationMs": 5170,
    "url": "https://2026.emnlp.org/calls/main_conference_papers/"
  },
  "sourceToolAssistantUUID": "65f5bd6c-d43d-4257-98e8-91f2bca45662",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-25T03:55:57.475Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now let me continue reading the remaining paper sections (experiments, conclusion, limitations, related_work, appendix) and check for external review config.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe93fb00-529e-4d3f-91cd-e4d229d18418",
  "isSidechain": false,
  "requestId": "req_011CbNcXNaWkYPohGvdKk9dH",
  "type": "assistant",
  "uuid": "2367207d-6396-4631-b916-efcb53bab327",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPiRMD2SazWtD3cuFDpNUK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5168,
      "cache_creation_input_tokens": 1968,
      "cache_read_input_tokens": 41710,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1968,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5168,
          "output_tokens": 363,
          "cache_read_input_tokens": 41710,
          "cache_creation_input_tokens": 1968,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1968
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

_source line 59 · 2026-05-25T03:55:58.000Z_

继续读取剩余论文章节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2367207d-6396-4631-b916-efcb53bab327",
  "isSidechain": false,
  "requestId": "req_011CbNcXNaWkYPohGvdKk9dH",
  "type": "assistant",
  "uuid": "99226c1c-03fc-42b5-acf5-4c4781d96fcd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPiRMD2SazWtD3cuFDpNUK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5168,
      "cache_creation_input_tokens": 1968,
      "cache_read_input_tokens": 41710,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1968,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5168,
          "output_tokens": 363,
          "cache_read_input_tokens": 41710,
          "cache_creation_input_tokens": 1968,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1968
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

_source line 60 · 2026-05-25T03:55:59.983Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BgTLhfMDjnEKU1XUyEC6G9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99226c1c-03fc-42b5-acf5-4c4781d96fcd",
  "isSidechain": false,
  "requestId": "req_011CbNcXNaWkYPohGvdKk9dH",
  "type": "assistant",
  "uuid": "2ca93ad1-5398-421b-aa8c-3258961042df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPiRMD2SazWtD3cuFDpNUK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5168,
      "cache_creation_input_tokens": 1968,
      "cache_read_input_tokens": 41710,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1968,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5168,
          "output_tokens": 363,
          "cache_read_input_tokens": 41710,
          "cache_creation_input_tokens": 1968,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1968
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

_source line 61 · 2026-05-25T03:56:01.517Z_

<details><summary>↩ Tool result · `toolu_01DaA6fEagVzUBzaRPsjSe4b`</summary>

```text
1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	Large language model (LLM)--solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp, nlproofs} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1, rlsf} evaluate execution accuracy alone, with no diagnostic for component necessity.
6	AlphaProof~\citep{alphaproof2025} and DeepSeek-Prover-V2~\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4 for competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these settings.
7	We use FOLIO~\citep{folio}, the only public natural language inference (NLI) benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Reward hacking and Goodhart's Law.}
10	Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RL from human feedback (RLHF)~\citep{gao-reward-overoptimization} and logical formalization~\citep{bondarenko-spec-gaming, kim-game-formalization}.
11	Most closely related, \citet{kim-game-formalization} document inference-time gaming on FOLIO with frontier models; our work complements theirs by studying training-time degeneration via component necessity rather than faithfulness.
12	\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes catastrophic Goodhart where Kullback--Leibler (KL) regularization provably fails, providing a theoretical lens for why GRPO's KL penalty does not prevent our observed collapse.
13	Concurrent work documents spurious signals in RLVR~\citep{spurious-rewards, yan2026spurious, dong2026probing, metr-reward-hacking, helff2026gaming, nishimura2026specgaming, khalifa2026countdown} and proposes composite rewards as mitigations~\citep{tarek2025reward, pronesti2026beyond};
14	mitigation strategies include reward model ensembles~\citep{coste2023reward}, constrained optimization~\citep{moskovitz2023confronting}, and activation-level monitoring~\citep{wilhelm2026monitoring}. \citet{yue2025rl-reasoning} show RLVR redistributes probability mass rather than creating new reasoning, consistent with our finding that GRPO exploits existing shortcuts.
15	Our Goodhart effect follows the regressional pattern~\citep{manheim-goodhart-taxonomy} on FOLIO; its application to a diagnostic designed to detect gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.
16	
17	\paragraph{Process rewards and reward design.}
18	Process reward models~\citep{lightman-verify-step, setlur2025rewarding, cui2025prime, cobbe2021training, uesato2022solving} supervise intermediate steps; \citet{sullivan2025grpo-prm} show GRPO implicitly implements process reward. Classical reward shaping~\citep{ng1999policy, gao-effective-rl-reward} guarantees policy invariance only under potential-based transforms---ISR violates this condition.
19	
20	\paragraph{Mutation testing.}
21	STA adapts the LOO mutation paradigm~\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.
22	Related concerns about chain-of-thought (CoT) faithfulness~\citep{lanham2023faithfulness, turpin2023unfaithful} operate at the reasoning-chain level rather than solver-input components.
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6358ac26-59e3-479f-a16f-add506ee91f7",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "2409fc26-5de8-47ff-9c8e-c3b01874582e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Neurosymbolic reasoning.}\nLarge language model (LLM)--solver pipelines~\\citep{satlm, logic-lm, linc, fover-pei2025, lorp, nlproofs} and RL methods trained on solver feedback~\\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1, rlsf} evaluate execution accuracy alone, with no diagnostic for component necessity.\nAlphaProof~\\citep{alphaproof2025} and DeepSeek-Prover-V2~\\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4 for competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these settings.\nWe use FOLIO~\\citep{folio}, the only public natural language inference (NLI) benchmark with both FOL and Prolog annotations.\n\n\\paragraph{Reward hacking and Goodhart's Law.}\nGoodhart's Law is established theoretically~\\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RL from human feedback (RLHF)~\\citep{gao-reward-overoptimization} and logical formalization~\\citep{bondarenko-spec-gaming, kim-game-formalization}.\nMost closely related, \\citet{kim-game-formalization} document inference-time gaming on FOLIO with frontier models; our work complements theirs by studying training-time degeneration via component necessity rather than faithfulness.\n\\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes catastrophic Goodhart where Kullback--Leibler (KL) regularization provably fails, providing a theoretical lens for why GRPO's KL penalty does not prevent our observed collapse.\nConcurrent work documents spurious signals in RLVR~\\citep{spurious-rewards, yan2026spurious, dong2026probing, metr-reward-hacking, helff2026gaming, nishimura2026specgaming, khalifa2026countdown} and proposes composite rewards as mitigations~\\citep{tarek2025reward, pronesti2026beyond};\nmitigation strategies include reward model ensembles~\\citep{coste2023reward}, constrained optimization~\\citep{moskovitz2023confronting}, and activation-level monitoring~\\citep{wilhelm2026monitoring}. \\citet{yue2025rl-reasoning} show RLVR redistributes probability mass rather than creating new reasoning, consistent with our finding that GRPO exploits existing shortcuts.\nOur Goodhart effect follows the regressional pattern~\\citep{manheim-goodhart-taxonomy} on FOLIO; its application to a diagnostic designed to detect gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.\n\n\\paragraph{Process rewards and reward design.}\nProcess reward models~\\citep{lightman-verify-step, setlur2025rewarding, cui2025prime, cobbe2021training, uesato2022solving} supervise intermediate steps; \\citet{sullivan2025grpo-prm} show GRPO implicitly implements process reward. Classical reward shaping~\\citep{ng1999policy, gao-effective-rl-reward} guarantees policy invariance only under potential-based transforms---ISR violates this condition.\n\n\\paragraph{Mutation testing.}\nSTA adapts the LOO mutation paradigm~\\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.\nRelated concerns about chain-of-thought (CoT) faithfulness~\\citep{lanham2023faithfulness, turpin2023unfaithful} operate at the reasoning-chain level rather than solver-input components.\n",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  },
  "sourceToolAssistantUUID": "6358ac26-59e3-479f-a16f-add506ee91f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-25T03:56:00.000Z_

<details><summary>↩ Tool result · `toolu_01BgTLhfMDjnEKU1XUyEC6G9`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ (ISR $\beta{=}0.1$ extends to $\{45,46\}$; Appendix~\ref{app:detailed-results}) on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\leq}7\%$ non-hacking (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention; Appendix~\ref{app:prooffol-construction}); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}; classifier blind spots discussed in Appendix~\ref{app:extended-discussion}), and a \emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall unknown; 152-sample precision audit in Appendix~\ref{app:hacking-modes}).
13	
14	\begin{figure}[t]
15	\centering
16	\includegraphics[width=0.85\columnwidth]{figures/fig_seed_divergence.pdf}
17	\caption{Seed-dependent Goodhart effect under ISR $\beta{=}0.1$ reward (500 steps). Three seeds converge to gaming ($\text{N-H}{\leq}17\%$); two retain genuine reasoning (${\sim}55\%$).}
18	\label{fig:seed-divergence}
19	\end{figure}
20	
21	\paragraph{Statistical considerations.}
22	With three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.
23	Pooled Cochran--Mantel--Haenszel $p$-values ($N{=}3$ strata) are descriptive summaries, not formal inference; non-significant comparisons are exploratory.
24	An $N{=}2$ sensitivity analysis excluding s43 confirms consistent or stronger patterns (Appendix~\ref{app:n2-sensitivity}).
25	ProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory and underpowered.
26	
27	\subsection{ISR as Diagnostic}
28	\label{sec:diagnostic}
29	
30	\textbf{Collapse trajectory.}
31	Figure~\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) across 1000 training steps.
32	As PR climbs from $32\%$ to $96\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\times$, \S\ref{sec:goodhart}) consistent with structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42
33	By 500 steps, $87\%$ of proved samples embed the conclusion verbatim (CE), establishing degeneration independent of the ISR scalar.
34	A binary variant testing only collective premise necessity misses the collapse entirely ($\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\ref{app:o1-ablation}).
35	
36	\textbf{Cross-seed instability.}
37	Three seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\leq}7\%$ non-hacking by 1000 steps (Table~\ref{tab:fol-detailed}; Appendix~\ref{app:detailed-results}).
38	Exec-only seeds exhibit qualitatively different convergence patterns (PR range: 13--98\%), precluding meaningful pooling; we report seed~42 as representative of the converged regime (Table~\ref{tab:goodhart-landscape}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2
39	Two additional seeds under identical conditions fail to converge ($\text{PR}{\approx}14\%$; Appendix~\ref{app:seed-convergence}), retaining genuine reasoning and suggesting that structural degeneration requires successful convergence, though the confound between model capability and optimization success precludes strong causal attribution (Appendix~\ref{app:llama-coldstart}).
40	
41	\textbf{SFT baseline.}
42	SFT on gold formalizations produces $92\%$ non-hacking outputs at $\text{PR}{=}13\%$ (odds ratio ${=}147$ vs.\ exec-only, $p{<}0.001$), establishing that hacking modes are absent before RL optimization.
43	SFT serves as a pre-RL reference rather than a PR-matched control; its low PR reflects minimal optimization pressure.
44	Early-training comparison supports this interpretation: at 100 steps ($\text{PR}{=}32\%$), hacking already reaches $31\%$ vs.\ SFT's $8\%$ at comparable PR (Appendix~\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3
45	
46	\subsection{Goodhart Effects on ISR-as-Reward}
47	\label{sec:goodhart}
48	
49	We reverse ISR's role from observer to reward: $r = r_{\text{exec}}\cdot(1 + \beta\,\text{ISR})$, with matched random control ($u\sim\mathcal{U}(0,1)$).
50	The result is a regressional Goodhart pattern~\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \emph{composition} of failure modes without reducing their aggregate prevalence.
51	ISR reward systematically selects for tautological shortcuts (TS) over conclusion embedding (CE) rather than producing genuine reasoning (Table~\ref{tab:goodhart-landscape}). The scalar ISR$^*$ advantage ($214\times$ raw) collapses to $1.06\times$ after controlling for premise count; the compositional mode shift provides the primary evidence.
52	
53	\paragraph{Multiplicative coupling.}
54	Three controls constrain the multiplicative confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\ref{app:setup}).
55	The shuffled-ISR control ($87\%$ non-hacking at low PR) confirms the Goodhart effect requires sample-level ISR signal, not its distributional shape.
56	
57	\textbf{Low-dose ISR ($\beta{=}0.1$).}
58	ISR reward amplifies TS convergence: $71\%$ of proved samples under ISR exhibit tautological shortcuts vs.\ $14\%$ under random (Appendix~\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL
59	TS is the canonical Goodhart move: a single premise identical to the conclusion yields $\text{ISR}\geq 0.5$ by construction, directly satisfying the LOO metric (\S\ref{sec:taxonomy-method}).
60	Total conclusion embedding ($\text{CE}+\text{TS}$) spans $68$--$100\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\ref{fig:hacking-composition}).
61	A seed-stratified $\chi^2$ test confirms the overall mode distribution differs significantly between ISR and random conditions ($\chi^2{=}174.8$, $\text{df}{=}2$, $p{<}10^{-38}$; Appendix~\ref{app:statistical-details}).
62	
63	\textbf{Seed-dependent outcomes.}
64	ISR reward produces bimodal outcomes (Figure~\ref{fig:seed-divergence}): 3 of 5 seeds converge to gaming, demonstrating that the Goodhart effect occurs frequently but not universally; 2 of 5 retain substantial genuine reasoning (seeds~45/46 added post-hoc to test replication; Appendix~\ref{app:detailed-results}).
65	Excluding seed~43 (which uses nucleus sampling; \S\ref{sec:setup}), the remaining two ISR seeds show ${\leq}7\%$ non-hacking and $100\%$ TS, strengthening the core finding (full $N{=}2$ analysis: Appendix~\ref{app:n2-sensitivity}).
66	
67	\textbf{Premise-count confound.}
68	The $214\times$ raw ISR$^*$ collapse is largely explained by premise-count reduction: ISR-trained models produce shorter formalizations that mechanically inflate ISR.
69	The premise-count-matched comparison yields only $1.06\times$ (McNemar $p{=}0.317$, $n{=}100$ matched pairs; Appendix~\ref{app:premise-count}), indicating that the scalar ISR advantage is not statistically significant.
70	
71	The compositional evidence, however, survives this control.
72	In the modal premise-count range (4--6 premises, where most proved samples fall), TS reaches $19.7\%$ under ISR versus $0\%$ under random reward (Figure~\ref{fig:premise-bins}; Table~\ref{tab:premise-bin-modes}).
73	TS hacking is mechanistically limited to simpler problems---models cannot restate the conclusion while ignoring all premises when formalization complexity is high.
74	This complexity dependence is a mechanistic insight, not a confound: the compositional mode shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect.
75	The failure of ISR-as-reward demonstrates that structural diagnostics cannot be naively repurposed as training objectives---a finding that applies to any LOO-based metric in solver-verified settings.
76	
77	\begin{figure}[t]
78	\centering
79	\includegraphics[width=\columnwidth]{figures/fig_premise_bins.pdf}
80	\caption{Mode composition by premise count (proved samples, seed~42, $\beta{=}0.1$). TS hacking emerges exclusively under ISR in the 4--6 premise range; Random shows zero TS at any complexity, confirming that ISR's compositional shift is not a premise-count artifact. I\,=\,ISR, R\,=\,Random.}
81	\label{fig:premise-bins}
82	\end{figure}
83	
84	\textbf{Higher doses and temporal dynamics.}
85	Any genuine reasoning under ISR $\beta{=}0.1$ is transient: non-hacking drops from $17\%$ to $2\%$ by 1000 steps as TS escalates (Figure~\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42
86	Higher doses accelerate collapse: $\beta{=}0.2$ eliminates all non-hacking; $\beta{=}0.3$ destabilizes training itself, producing multi-modal failure~\citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44
87	
88	\subsection{Cross-Domain and Cross-Dataset Evidence}
89	\label{sec:crossdomain}
90	\label{sec:crosslogic}
91	
92	The following results extend the primary findings of \S\ref{sec:diagnostic}--\ref{sec:goodhart} to alternative logic types and dataset families; these cross-domain experiments are exploratory in nature.
93	
94	\begin{figure}[t]
95	\centering
96	\includegraphics[width=\columnwidth]{figures/fig4_prolog_comparison.pdf}
97	\caption{Cross-logic results. \textbf{Top}: FOL vs.\ Prolog exec-only $\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\% non-hacking through distinct mechanisms.}
98	\label{fig:prolog-comparison}
99	\end{figure}
100	
101	\textbf{Prolog: universal Goodhart.}
102	Replicating the pipeline with Prolog/SWI-Prolog (Figure~\ref{fig:prolog-comparison}), exec-only seeds collapse to $\text{ISR}^*{\approx}0$ via redundant ground-fact coding, supporting STA's diagnostic transfer across logic types.
103	Under ISR-as-reward, all three seeds reach $0\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\ref{tab:prolog-detailed}).
104	Prolog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.
105	
106	\textbf{ProofFOL exec-only: cross-dataset replication.}
107	Converged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.
108	The mode repertoire differs across datasets: among converged seeds, TS dominates one while CE dominates the other, showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.
109	
110	\textbf{ProofFOL ISR ($\beta{=}0.1$): dataset-dependent asymmetry.}
111	ISR reward on ProofFOL produces directionally higher genuine rates than exec-only ($p{=}0.10$, exploratory; Table~\ref{tab:prooffol-detailed}).
112	The asymmetry follows from hacking geometry: on FOLIO, TS yields high ISR (regressional Goodhart~\citep{manheim-goodhart-taxonomy}); on ProofFOL, CE embeds conclusions among many premises, yielding $\text{ISR}{\approx}0$ and rendering ISR reward effectively corrective.
113	
114	\paragraph{Cross-scale validation (Qwen3-8B).}
115	Qwen3-8B does not converge under exec-only GRPO ($\text{PR}{=}14\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\ref{app:8b-results}).
116	
117	\subsection{Hacking Taxonomy}
118	\label{sec:taxonomy}
119	
120	\begin{figure}[t]
121	\centering
122	\includegraphics[width=0.92\columnwidth]{figures/fig3_hacking_composition.pdf}
123	\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}). ISR systematically selects for TS over CE without reducing total hacking; SFT shows near-zero hacking.}
124	\label{fig:hacking-composition}
125	\end{figure}
126	
127	Three modes account for the vast majority of hacking (Appendix Table~\ref{tab:hacking-taxonomy}; Appendix~\ref{app:hacking-modes}): CE (conclusion embedding), TS (conclusion duplication), and PG (premise-subset gaming).
128	The central pattern: \emph{reward formulation determines which mode dominates but not whether hacking occurs}; all GRPO conditions produce overwhelming degeneration, while SFT achieves $92\%$ non-hacking.
129	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ca93ad1-5398-421b-aa8c-3258961042df",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "78d2ab22-fbd0-4b73-b5cd-f509c902a2d9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\\S\\ref{sec:crossdomain}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ (ISR $\\beta{=}0.1$ extends to $\\{45,46\\}$; Appendix~\\ref{app:detailed-results}) on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}\nHeld-out evaluation uses 100 FOLIO examples with greedy decoding;\\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\\leq}7\\%$ non-hacking (Appendix~\\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.\nCross-dataset experiments (\\S\\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\\sim}$500 training examples constructed by translating ProofWriter~\\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\\sim}70\\%$ retention; Appendix~\\ref{app:prooffol-construction}); \\emph{stable convergence} denotes $\\overline{\\text{PR}}_{\\text{final\\,50}} > 0.90$.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}; classifier blind spots discussed in Appendix~\\ref{app:extended-discussion}), and a \\emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall unknown; 152-sample precision audit in Appendix~\\ref{app:hacking-modes}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig_seed_divergence.pdf}\n\\caption{Seed-dependent Goodhart effect under ISR $\\beta{=}0.1$ reward (500 steps). Three seeds converge to gaming ($\\text{N-H}{\\leq}17\\%$); two retain genuine reasoning (${\\sim}55\\%$).}\n\\label{fig:seed-divergence}\n\\end{figure}\n\n\\paragraph{Statistical considerations.}\nWith three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.\nPooled Cochran--Mantel--Haenszel $p$-values ($N{=}3$ strata) are descriptive summaries, not formal inference; non-significant comparisons are exploratory.\nAn $N{=}2$ sensitivity analysis excluding s43 confirms consistent or stronger patterns (Appendix~\\ref{app:n2-sensitivity}).\nProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory and underpowered.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) across 1000 training steps.\nAs PR climbs from $32\\%$ to $96\\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\\times$, \\S\\ref{sec:goodhart}) consistent with structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, $87\\%$ of proved samples embed the conclusion verbatim (CE), establishing degeneration independent of the ISR scalar.\nA binary variant testing only collective premise necessity misses the collapse entirely ($\\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\\ref{app:o1-ablation}).\n\n\\textbf{Cross-seed instability.}\nThree seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\\leq}7\\%$ non-hacking by 1000 steps (Table~\\ref{tab:fol-detailed}; Appendix~\\ref{app:detailed-results}).\nExec-only seeds exhibit qualitatively different convergence patterns (PR range: 13--98\\%), precluding meaningful pooling; we report seed~42 as representative of the converged regime (Table~\\ref{tab:goodhart-landscape}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2\nTwo additional seeds under identical conditions fail to converge ($\\text{PR}{\\approx}14\\%$; Appendix~\\ref{app:seed-convergence}), retaining genuine reasoning and suggesting that structural degeneration requires successful convergence, though the confound between model capability and optimization success precludes strong causal attribution (Appendix~\\ref{app:llama-coldstart}).\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations produces $92\\%$ non-hacking outputs at $\\text{PR}{=}13\\%$ (odds ratio ${=}147$ vs.\\ exec-only, $p{<}0.001$), establishing that hacking modes are absent before RL optimization.\nSFT serves as a pre-RL reference rather than a PR-matched control; its low PR reflects minimal optimization pressure.\nEarly-training comparison supports this interpretation: at 100 steps ($\\text{PR}{=}32\\%$), hacking already reaches $31\\%$ vs.\\ SFT's $8\\%$ at comparable PR (Appendix~\\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\n\n\\subsection{Goodhart Effects on ISR-as-Reward}\n\\label{sec:goodhart}\n\nWe reverse ISR's role from observer to reward: $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with matched random control ($u\\sim\\mathcal{U}(0,1)$).\nThe result is a regressional Goodhart pattern~\\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \\emph{composition} of failure modes without reducing their aggregate prevalence.\nISR reward systematically selects for tautological shortcuts (TS) over conclusion embedding (CE) rather than producing genuine reasoning (Table~\\ref{tab:goodhart-landscape}). The scalar ISR$^*$ advantage ($214\\times$ raw) collapses to $1.06\\times$ after controlling for premise count; the compositional mode shift provides the primary evidence.\n\n\\paragraph{Multiplicative coupling.}\nThree controls constrain the multiplicative confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\\ref{app:setup}).\nThe shuffled-ISR control ($87\\%$ non-hacking at low PR) confirms the Goodhart effect requires sample-level ISR signal, not its distributional shape.\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$).}\nISR reward amplifies TS convergence: $71\\%$ of proved samples under ISR exhibit tautological shortcuts vs.\\ $14\\%$ under random (Appendix~\\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nTS is the canonical Goodhart move: a single premise identical to the conclusion yields $\\text{ISR}\\geq 0.5$ by construction, directly satisfying the LOO metric (\\S\\ref{sec:taxonomy-method}).\nTotal conclusion embedding ($\\text{CE}+\\text{TS}$) spans $68$--$100\\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\\ref{fig:hacking-composition}).\nA seed-stratified $\\chi^2$ test confirms the overall mode distribution differs significantly between ISR and random conditions ($\\chi^2{=}174.8$, $\\text{df}{=}2$, $p{<}10^{-38}$; Appendix~\\ref{app:statistical-details}).\n\n\\textbf{Seed-dependent outcomes.}\nISR reward produces bimodal outcomes (Figure~\\ref{fig:seed-divergence}): 3 of 5 seeds converge to gaming, demonstrating that the Goodhart effect occurs frequently but not universally; 2 of 5 retain substantial genuine reasoning (seeds~45/46 added post-hoc to test replication; Appendix~\\ref{app:detailed-results}).\nExcluding seed~43 (which uses nucleus sampling; \\S\\ref{sec:setup}), the remaining two ISR seeds show ${\\leq}7\\%$ non-hacking and $100\\%$ TS, strengthening the core finding (full $N{=}2$ analysis: Appendix~\\ref{app:n2-sensitivity}).\n\n\\textbf{Premise-count confound.}\nThe $214\\times$ raw ISR$^*$ collapse is largely explained by premise-count reduction: ISR-trained models produce shorter formalizations that mechanically inflate ISR.\nThe premise-count-matched comparison yields only $1.06\\times$ (McNemar $p{=}0.317$, $n{=}100$ matched pairs; Appendix~\\ref{app:premise-count}), indicating that the scalar ISR advantage is not statistically significant.\n\nThe compositional evidence, however, survives this control.\nIn the modal premise-count range (4--6 premises, where most proved samples fall), TS reaches $19.7\\%$ under ISR versus $0\\%$ under random reward (Figure~\\ref{fig:premise-bins}; Table~\\ref{tab:premise-bin-modes}).\nTS hacking is mechanistically limited to simpler problems---models cannot restate the conclusion while ignoring all premises when formalization complexity is high.\nThis complexity dependence is a mechanistic insight, not a confound: the compositional mode shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect.\nThe failure of ISR-as-reward demonstrates that structural diagnostics cannot be naively repurposed as training objectives---a finding that applies to any LOO-based metric in solver-verified settings.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_premise_bins.pdf}\n\\caption{Mode composition by premise count (proved samples, seed~42, $\\beta{=}0.1$). TS hacking emerges exclusively under ISR in the 4--6 premise range; Random shows zero TS at any complexity, confirming that ISR's compositional shift is not a premise-count artifact. I\\,=\\,ISR, R\\,=\\,Random.}\n\\label{fig:premise-bins}\n\\end{figure}\n\n\\textbf{Higher doses and temporal dynamics.}\nAny genuine reasoning under ISR $\\beta{=}0.1$ is transient: non-hacking drops from $17\\%$ to $2\\%$ by 1000 steps as TS escalates (Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\nHigher doses accelerate collapse: $\\beta{=}0.2$ eliminates all non-hacking; $\\beta{=}0.3$ destabilizes training itself, producing multi-modal failure~\\citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~\\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44\n\n\\subsection{Cross-Domain and Cross-Dataset Evidence}\n\\label{sec:crossdomain}\n\\label{sec:crosslogic}\n\nThe following results extend the primary findings of \\S\\ref{sec:diagnostic}--\\ref{sec:goodhart} to alternative logic types and dataset families; these cross-domain experiments are exploratory in nature.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Top}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \\textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\textbf{Prolog: universal Goodhart.}\nReplicating the pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}), exec-only seeds collapse to $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding, supporting STA's diagnostic transfer across logic types.\nUnder ISR-as-reward, all three seeds reach $0\\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\\ref{tab:prolog-detailed}).\nProlog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.\n\n\\textbf{ProofFOL exec-only: cross-dataset replication.}\nConverged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.\nThe mode repertoire differs across datasets: among converged seeds, TS dominates one while CE dominates the other, showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.\n\n\\textbf{ProofFOL ISR ($\\beta{=}0.1$): dataset-dependent asymmetry.}\nISR reward on ProofFOL produces directionally higher genuine rates than exec-only ($p{=}0.10$, exploratory; Table~\\ref{tab:prooffol-detailed}).\nThe asymmetry follows from hacking geometry: on FOLIO, TS yields high ISR (regressional Goodhart~\\citep{manheim-goodhart-taxonomy}); on ProofFOL, CE embeds conclusions among many premises, yielding $\\text{ISR}{\\approx}0$ and rendering ISR reward effectively corrective.\n\n\\paragraph{Cross-scale validation (Qwen3-8B).}\nQwen3-8B does not converge under exec-only GRPO ($\\text{PR}{=}14\\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\\ref{app:8b-results}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR systematically selects for TS over CE without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\nThree modes account for the vast majority of hacking (Appendix Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}): CE (conclusion embedding), TS (conclusion duplication), and PG (premise-subset gaming).\nThe central pattern: \\emph{reward formulation determines which mode dominates but not whether hacking occurs}; all GRPO conditions produce overwhelming degeneration, while SFT achieves $92\\%$ non-hacking.\n",
      "numLines": 129,
      "startLine": 1,
      "totalLines": 129
    }
  },
  "sourceToolAssistantUUID": "2ca93ad1-5398-421b-aa8c-3258961042df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-25T03:56:01.169Z_

<details open><summary>🔧 Tool call — Read · `toolu_019fvboXuH3QVZPNkzubvoEq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78d2ab22-fbd0-4b73-b5cd-f509c902a2d9",
  "isSidechain": false,
  "requestId": "req_011CbNcXNaWkYPohGvdKk9dH",
  "type": "assistant",
  "uuid": "2a9696aa-0e9e-4c2c-bc70-59a242fe1c56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPiRMD2SazWtD3cuFDpNUK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5168,
      "cache_creation_input_tokens": 1968,
      "cache_read_input_tokens": 41710,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1968,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5168,
          "output_tokens": 363,
          "cache_read_input_tokens": 41710,
          "cache_creation_input_tokens": 1968,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1968
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

_source line 64 · 2026-05-25T03:56:01.175Z_

<details><summary>↩ Tool result · `toolu_019fvboXuH3QVZPNkzubvoEq`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation; repurposed as reward, ISR produces a seed-dependent Goodhart effect: structural proxies for formalization integrity are easier to observe than to optimize (Appendix~\ref{app:practical-guidelines}).
5	Cross-logic experiments (Prolog) confirm the compositional mode shift; cross-benchmark evidence (ProofFOL, $p{=}0.10$) is exploratory (\S\ref{sec:crossdomain}).
6	Convergence appears necessary for degeneration, though capability and optimization confounds preclude causal attribution (Appendix~\ref{app:seed-convergence}).
7	For practitioners, structural diagnostics should be applied post-hoc; the mode breakdown provides the reliable signal.
8	The observe-vs-optimize asymmetry motivates targeted mitigations---mode-aware reward shaping~\citep{tarek2025reward, pronesti2026beyond} or single-premise penalties to block TS---rather than blanket structural optimization; that 2/5 seeds retain genuine reasoning suggests this is feasible.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a9696aa-0e9e-4c2c-bc70-59a242fe1c56",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "5d4b02ee-8096-4a56-b329-2c82ffe3fecd",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex",
      "content": "\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\nSTA exposes structural degeneration invisible to execution-based evaluation; repurposed as reward, ISR produces a seed-dependent Goodhart effect: structural proxies for formalization integrity are easier to observe than to optimize (Appendix~\\ref{app:practical-guidelines}).\nCross-logic experiments (Prolog) confirm the compositional mode shift; cross-benchmark evidence (ProofFOL, $p{=}0.10$) is exploratory (\\S\\ref{sec:crossdomain}).\nConvergence appears necessary for degeneration, though capability and optimization confounds preclude causal attribution (Appendix~\\ref{app:seed-convergence}).\nFor practitioners, structural diagnostics should be applied post-hoc; the mode breakdown provides the reliable signal.\nThe observe-vs-optimize asymmetry motivates targeted mitigations---mode-aware reward shaping~\\citep{tarek2025reward, pronesti2026beyond} or single-premise penalties to block TS---rather than blanket structural optimization; that 2/5 seeds retain genuine reasoning suggests this is feasible.\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "2a9696aa-0e9e-4c2c-bc70-59a242fe1c56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-25T03:56:01.361Z_

<details open><summary>🔧 Tool call — Read · `toolu_0132C1w6mMTgiTrmEVyQFPtm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d4b02ee-8096-4a56-b329-2c82ffe3fecd",
  "isSidechain": false,
  "requestId": "req_011CbNcXNaWkYPohGvdKk9dH",
  "type": "assistant",
  "uuid": "6bd7e451-829b-4b6d-9c2b-290d92923a4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPiRMD2SazWtD3cuFDpNUK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5168,
      "cache_creation_input_tokens": 1968,
      "cache_read_input_tokens": 41710,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1968,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5168,
          "output_tokens": 363,
          "cache_read_input_tokens": 41710,
          "cache_creation_input_tokens": 1968,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1968
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

_source line 66 · 2026-05-25T03:56:01.366Z_

<details><summary>↩ Tool result · `toolu_0132C1w6mMTgiTrmEVyQFPtm`</summary>

```text
1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B); structural degeneration patterns may not transfer to other model families, and cross-scale generalization remains untested (Appendix~\ref{app:8b-results}).
5	Three to five seeds per condition demonstrate qualitative divergence but remain underpowered for seed-level significance; pooled statistics treat within-seed samples as independent.
6	The mechanisms driving seed heterogeneity---why 3/5 seeds converge to gaming while 2/5 retain genuine reasoning under identical conditions---remain unexplored; possible explanations include initialization sensitivity, early-training bifurcation dynamics, and loss landscape multi-modality, but causal attribution requires targeted intervention experiments beyond our current scope.
7	FOLIO is a relatively small (1,435 examples) synthetic benchmark; generalization of both the degeneration phenomena and the STA diagnostic to larger, naturalistic, or domain-specific corpora (e.g., legal or scientific reasoning) is untested.
8	ISR quantifies component necessity, not semantic faithfulness; its diagnostic value is realized through the mode breakdown, not the scalar alone (Appendix~\ref{app:extended-discussion}).
9	Given perfect classifier precision (152/152; Appendix~\ref{app:hacking-modes}), measured non-hacking rates of 6--10\% for converged seeds are internally consistent only if classifier recall exceeds ${\sim}90\%$; below this threshold, the implied true non-hacking rate would be negative, indicating that low measured rates are self-validating evidence of high recall.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6bd7e451-829b-4b6d-9c2b-290d92923a4c",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "676d34bd-ead2-4b88-87be-afde5b659c43",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex",
      "content": "\\section{Limitations}\n\\label{sec:limitations}\n\nExperiments use a single base model (Qwen3-4B); structural degeneration patterns may not transfer to other model families, and cross-scale generalization remains untested (Appendix~\\ref{app:8b-results}).\nThree to five seeds per condition demonstrate qualitative divergence but remain underpowered for seed-level significance; pooled statistics treat within-seed samples as independent.\nThe mechanisms driving seed heterogeneity---why 3/5 seeds converge to gaming while 2/5 retain genuine reasoning under identical conditions---remain unexplored; possible explanations include initialization sensitivity, early-training bifurcation dynamics, and loss landscape multi-modality, but causal attribution requires targeted intervention experiments beyond our current scope.\nFOLIO is a relatively small (1,435 examples) synthetic benchmark; generalization of both the degeneration phenomena and the STA diagnostic to larger, naturalistic, or domain-specific corpora (e.g., legal or scientific reasoning) is untested.\nISR quantifies component necessity, not semantic faithfulness; its diagnostic value is realized through the mode breakdown, not the scalar alone (Appendix~\\ref{app:extended-discussion}).\nGiven perfect classifier precision (152/152; Appendix~\\ref{app:hacking-modes}), measured non-hacking rates of 6--10\\% for converged seeds are internally consistent only if classifier recall exceeds ${\\sim}90\\%$; below this threshold, the implied true non-hacking rate would be negative, indicating that low measured rates are self-validating evidence of high recall.\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  },
  "sourceToolAssistantUUID": "6bd7e451-829b-4b6d-9c2b-290d92923a4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-25T03:56:01.511Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DaA6fEagVzUBzaRPsjSe4b`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "676d34bd-ead2-4b88-87be-afde5b659c43",
  "isSidechain": false,
  "requestId": "req_011CbNcXNaWkYPohGvdKk9dH",
  "type": "assistant",
  "uuid": "6358ac26-59e3-479f-a16f-add506ee91f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPiRMD2SazWtD3cuFDpNUK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5168,
      "cache_creation_input_tokens": 1968,
      "cache_read_input_tokens": 41710,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1968,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5168,
          "output_tokens": 363,
          "cache_read_input_tokens": 41710,
          "cache_creation_input_tokens": 1968,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1968
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

_source line 68 · 2026-05-25T03:56:01.566Z_

```json
{
  "parentUuid": "2409fc26-5de8-47ff-9c8e-c3b01874582e",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "10ced755-3fcf-49b9-970b-d5dbec5448a8",
  "timestamp": "2026-05-25T03:56:01.566Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 69_

```json
{
  "type": "last-prompt",
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: solver-trace-ablation - 论文路径: projects/solver-trace-ablation/docs/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: Long paper (ARR) - 截止日期: 未提供，请自行调研 - **引用验证**: ❌ 未启用…",
  "leafUuid": "10ced755-3fcf-49b9-970b-d5dbec5448a8",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646"
}
```

---

### Runtime record

_source line 70_

```json
{
  "type": "ai-title",
  "aiTitle": "Review solver-trace-ablation paper for EMNLP 2026",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646"
}
```

---

### Assistant

_source line 71 · 2026-05-25T03:56:04.720Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the appendix and check the external review config.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10ced755-3fcf-49b9-970b-d5dbec5448a8",
  "isSidechain": false,
  "requestId": "req_011CbNcXvRBZU63naGCKsZi7",
  "type": "assistant",
  "uuid": "0a905971-3f98-4dc5-85a3-ce061a7be226",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFHmMgTqqeGcBvUcCT5LfC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12111,
      "cache_read_input_tokens": 43678,
      "output_tokens": 283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12111,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 283,
          "cache_read_input_tokens": 43678,
          "cache_creation_input_tokens": 12111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12111
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

_source line 72 · 2026-05-25T03:56:06.747Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C4fhi1kjB2AsLoEGBCGFwv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a905971-3f98-4dc5-85a3-ce061a7be226",
  "isSidechain": false,
  "requestId": "req_011CbNcXvRBZU63naGCKsZi7",
  "type": "assistant",
  "uuid": "5b314621-c614-41a6-844c-9349dd2e2a29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFHmMgTqqeGcBvUcCT5LfC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12111,
      "cache_read_input_tokens": 43678,
      "output_tokens": 283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12111,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 283,
          "cache_read_input_tokens": 43678,
          "cache_creation_input_tokens": 12111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12111
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

_source line 73 · 2026-05-25T03:56:07.010Z_

<details><summary>↩ Tool result · `toolu_01C4fhi1kjB2AsLoEGBCGFwv`</summary>

```text
1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[ht]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\small
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Compute resources.}
53	Experiments were run on single-GPU setups (NVIDIA RTX 4090 24\,GB and RTX PRO 6000 96\,GB).
54	Each GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).
55	Total compute across all seeds, conditions, and reruns is approximately 80--120 GPU-hours.
56	
57	\paragraph{SFT convergence.}
58	SFT training converged across all three seeds: final-step loss ${\leq}0.04$ and token accuracy ${>}99\%$ after ${\sim}8$ epochs on 500 examples (seed~42: $0.029$; seed~44: $0.033$); the 1000-step extension further decreases loss to $0.017$.
59	
60	\paragraph{Evaluation exception.}
61	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
62	Its PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).
63	
64	\paragraph{Reward formulation.}
65	An additive variant ($r = r_{\text{exec}} + \beta\,\text{ISR}$) was tested in early experiments but collapsed prove rate to near-zero, as ISR alone provides no gradient toward provable formalizations; the multiplicative form $r_{\text{exec}}\cdot(1+\beta\,\text{ISR})$ ensures ISR modulates only proved outputs.
66	
67	\paragraph{ProofFOL dataset construction.}
68	\label{app:prooffol-construction}
69	ProofFOL is derived from ProofWriter~\citep{proofwriter} (10{,}424 training examples) via the GPT-4o silver-standard FOL translation pipeline of \citet{prooffol-thatikonda2024} with Prover9 verification filtering (${\sim}70\%$ retention; failures from timeouts, unsupported constructs, and translation errors).
70	Of the translated examples, 99.1\% parse successfully (92 skipped due to empty FOL output).
71	We sample 500 training and 100 evaluation examples (seed~42) from the verified pool.
72	Table~\ref{tab:prooffol-vs-folio} compares key structural properties.
73	
74	\begin{table}[!ht]
75	\centering
76	\caption{ProofFOL vs.\ FOLIO structural comparison (training sets, $n{=}500$ each).}
77	\label{tab:prooffol-vs-folio}
78	\small
79	\resizebox{\columnwidth}{!}{%
80	\begin{tabular}{@{}lcc@{}}
81	\toprule
82	\textbf{Property} & \textbf{ProofFOL} & \textbf{FOLIO} \\
83	\midrule
84	FOL premises (mean$\pm$std) & $18.2 \pm 3.2$ & $5.3 \pm 1.4$ \\
85	\quad Ground facts & $10.2 \pm 3.0$ & $1.8 \pm 1.5$ \\
86	\quad Rules & $8.1 \pm 1.1$ & $3.5 \pm 1.9$ \\
87	XOR ($\oplus$) samples & 0\% & 37.2\% \\
88	Dominant depth & 4--5 & 2--3 \\
89	Predicate style & synthetic & real-world \\
90	FOL source & GPT-4o (silver) & human (gold) \\
91	\bottomrule
92	\end{tabular}}
93	\end{table}
94	
95	ProofFOL problems are structurally more complex ($3.4{\times}$ more premises) but use simpler, synthetic predicates (e.g., \texttt{Blue(x)}, \texttt{Rough(x)}) characteristic of ProofWriter's procedural generation.
96	The absence of XOR constraints and the regularity of predicate structure make ProofFOL a complementary testbed: structural degeneration must emerge from the RL training dynamics rather than from formalization difficulty.
97	
98	\section{Extended Discussion}
99	\label{app:extended-discussion}
100	
101	\paragraph{What ISR measures---and what it does not.}
102	ISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.
103	This is strictly weaker than semantic faithfulness: whether the formalization accurately captures the natural-language meaning.
104	We verify this empirically: Spearman $\rho(\text{ISR}, \text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.
105	ISR and downstream task performance are uncorrelated.
106	ISR is thus a component-necessity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.
107	
108	Critically, low ISR carries different semantics depending on the training objective.
109	Under exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\S\ref{sec:crosslogic}).
110	Under ISR-as-reward, high ISR reflects metric gaming (\S\ref{sec:goodhart}).
111	ISR values must always be interpreted relative to the optimization objective that produced them.
112	
113	\paragraph{ISR as $(n{-}1)$-coalition Shapley value.}
114	\label{app:shapley}
115	Define a cooperative game $(N, v)$ with player set $N = \{1,\ldots,n\}$ (components) and binary utility $v(S) = \mathbf{1}[S(S){=}\textit{proved}]$.
116	The Shapley value $\phi_i$ averages marginal contributions over all coalition sizes; ISR restricts to the maximal coalition $|S|{=}n{-}1$, giving $\phi_i^{\text{LOO}} = \frac{1}{n}[v(N) - v(N \setminus \{i\})]$.
117	Summing: $\text{ISR}(x) = \sum_i \phi_i^{\text{LOO}} = \frac{1}{n}\sum_i \mathbf{1}[v(N \setminus \{i\}){=}0]$, recovering Equation~\ref{eq:isr}.
118	This restriction trades full interaction detection for $O(n)$ cost; the binary solver output makes higher-order interactions unobservable from LOO alone (\S\ref{sec:sta}).
119	
120	\paragraph{The premise-count confound.}
121	\label{app:premise-count}
122	LOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.
123	A formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.
124	This confound explains the sole apparent ISR-as-reward success (\S\ref{sec:goodhart}): ISR $\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.
125	Premise-count-matched comparison eliminates the difference ($1.06\times$, McNemar's test $p{=}0.317$; Table~\ref{tab:fol-beta01-detailed}), confirming that the scalar ISR advantage is not statistically significant.
126	This bias is not specific to our setting: any LOO-based structural metric applied to variable-length outputs requires component-count normalization.
127	We recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.
128	Mode composition analysis (CE vs.\ TS rates) is unaffected by premise-count confounding because TS classification depends on tautological proof structure (\S\ref{app:hacking-modes}), not on the number of premises in the formalization.
129	
130	\begin{table}[h]
131	\centering
132	\resizebox{\columnwidth}{!}{%
133	\begin{tabular}{@{}llrrrr@{}}
134	\toprule
135	\textbf{Premises} & \textbf{Condition} & \textbf{$N_{\text{proved}}$} & \textbf{CE\%} & \textbf{TS\%} & \textbf{Genuine\%} \\
136	\midrule
137	$\leq$3 & ISR $\beta{=}0.1$ & 8 & 50.0 & 12.5 & 12.5 \\
138	         & Random $\beta{=}0.1$ & 6 & 50.0 & 0.0 & 50.0 \\
139	\midrule
140	4--6     & ISR $\beta{=}0.1$ & 61 & 47.5 & 19.7 & 14.8 \\
141	         & Random $\beta{=}0.1$ & 58 & 72.4 & 0.0 & 22.4 \\
142	\midrule
143	$\geq$7  & ISR $\beta{=}0.1$ & 12 & 75.0 & 0.0 & 25.0 \\
144	         & Random $\beta{=}0.1$ & 15 & 86.7 & 0.0 & 13.3 \\
145	\bottomrule
146	\end{tabular}}
147	\caption{Mode composition by premise-count bin (seed 42). TS hacking is concentrated in the 4--6 premise range and absent for ${\geq}7$ premises, indicating a mechanistic complexity threshold rather than a statistical confound.}
148	\label{tab:premise-bin-modes}
149	\end{table}
150	
151	\begin{table*}[ht]
152	\centering
153	\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\beta{=}0.1$ non-hacking rate is corrected for PG reclassification and TS false negatives (Appendix~\ref{app:h8}).}
154	\label{tab:bootstrap-ci}
155	\small
156	\begin{tabular}{@{}lcccc@{}}
157	\toprule
158	\textbf{Comparison} & \textbf{Condition} & \textbf{Control} & \textbf{OR} & \textbf{$p$} \\
159	\midrule
160	\multicolumn{5}{@{}l}{\textit{Non-hacking rate (PG+FN corrected)}} \\
161	ISR vs.\ Random & 6.06\% {\scriptsize[3.6,9.9]} & 9.5\% {\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\
162	ISR vs.\ Exec-only & 6.06\% & 7.5\% & 0.79 & 0.62 \\
163	Random vs.\ Exec-only & 9.5\% & 7.5\% & 1.30 & 0.68 \\
164	\midrule
165	\multicolumn{5}{@{}l}{\textit{TS gaming rate}} \\
166	ISR vs.\ Random & 70.6\% {\scriptsize[64.3,76.3]} & 13.7\% {\scriptsize[9.9,18.6]} & 15.05 & $1.3{\times}10^{-39}$ \\
167	\midrule
168	\multicolumn{5}{@{}l}{\textit{SFT vs.\ Exec-only non-hacking rate}} \\
169	SFT vs.\ Exec-only & 92.3\% {\scriptsize[79.7,97.3]} & 7.5\% & 147 & ${<}0.001$ \\
170	\bottomrule
171	\end{tabular}
172	\\[2pt]
173	{\small ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\% Wilson CIs in brackets where shown. Pooled statistics treat within-seed samples as independent and serve as descriptive summaries only; the seed-stratified CMH test (\S\ref{app:statistical-details}) accounts for within-seed dependence.}
174	\end{table*}
175	
176	\paragraph{TS dose-response gradient.}
177	TS tautology follows a dose-response pattern across reward conditions: random $\beta{=}0.1$ produces $13.7\%$ TS ($36/262$ pooled; per-seed: $38.3\%$ in s43, $0\%$ in s42/s44), random $\beta{=}0.3$ yields 4--7 TSa samples per seed, and ISR $\beta{=}0.1$ reaches $70.6\%$ ($163/231$).
178	The gradient (random $\beta{=}0.1$ ($13.7\%$) $\to$ random $\beta{=}0.3$ (4--7 TSa per seed) $\to$ ISR $\beta{=}0.1$ ($70.6\%$)) shows ISR transforms TS from a seed-dependent GRPO tendency to a near-universal convergence direction.
179	
180	\paragraph{Goodhart effects: implications.}
181	ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself. Any diagnostic metric risks becoming a target when optimized.
182	The dose-response pattern maps onto the Manheim \& Garrabrant taxonomy~\citep{manheim-goodhart-taxonomy}: $\beta{=}0.1$ on FOLIO instantiates \emph{regressional} Goodhart ($P{\to}P$ tautologies yield $\text{ISR}{\geq}0.5$, so ISR erroneously rewards the shortcut); $\beta{\geq}0.2$ introduces \emph{extremal} elements (PR collapse to 18\% vs.\ 48\% random at $\beta{=}0.3$).
183	The implication is conditional: ISR fails as a training reward when hacking satisfies its LOO structure (FOLIO), but produces beneficial instability when hacking does not (ProofFOL; \S\ref{sec:crossdomain}).
184	
185	\paragraph{Single-seed unreliability.}
186	The three exec-only seeds diverge radically (PR $\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\S\ref{sec:diagnostic}).
187	ISR $\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (TS), 1/3 by premise minimization (\S\ref{sec:goodhart}).
188	Multi-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.
189	
190	\paragraph{Classifier limitations.}
191	Text-match hacking classifiers have systematic blind spots that functional analysis exposes.
192	In Prolog STA, two seeds achieved 100\% genuine classification under strict text matching, yet functional analysis via the $n_{\text{necessary}}$ distribution revealed 0\% genuine in both cases (Table~\ref{tab:prolog-detailed}).
193	One seed produces uppercase pseudo-Prolog that is functionally tautological; the other converts conclusions to snake\_case atoms serving as both fact and query, a gaming mode invisible to string comparison.
194	Practitioners should cross-validate text-match classifiers with functional metrics and never treat classifier-reported genuine rates as ground truth without independent verification.
195	
196	\paragraph{Practical guidelines.}
197	\label{app:practical-guidelines}
198	Our findings yield five guidelines for GRPO-trained neurosymbolic systems:
199	(1)~Never evaluate by prove rate alone; use ISR and component count as joint diagnostics.
200	(2)~Report multi-seed results: single-seed GRPO evaluation is unreliable, as cross-seed variance can exceed the effect size of interest (\S\ref{sec:diagnostic}).
201	(3)~Use ISR for post-hoc diagnosis only, not as a training signal; any dose induces gaming or collapse.
202	(4)~Treat LOO-based metrics as component-count-biased until normalized.
203	(5)~Expect conclusion embedding as a GRPO-universal baseline (Table~\ref{tab:goodhart-landscape}): reward shaping alters hacking composition, not prevalence.
204	
205	\paragraph{Multiple testing correction.}
206	\label{app:statistical-details}
207	We define two test families: FOLIO ($k{=}14$ tests across all conditions) and ProofFOL ($k{=}1$).
208	Within the FOLIO family, Bonferroni correction at $\alpha{=}0.05$ yields adjusted thresholds of $p_{\text{adj}}{=}0.05/14{=}0.0036$.
209	Three primary comparisons survive correction: the TS rate difference (ISR vs.\ random; $p_{\text{bonf}}{=}1.82{\times}10^{-38}$), the SFT vs.\ exec-only non-hacking rate ($p_{\text{bonf}}{=}0.014$), and the Cochran--Mantel--Haenszel test for TS association across seeds ($p_{\text{bonf}}{<}10^{-8}$).
210	The matched 5+5-seed Fisher/Mann-Whitney comparison is borderline ($p_{\text{bonf}}{=}0.056$), significant at $\alpha{=}0.10$ after Bonferroni correction ($k{=}14$).
211	The ProofFOL genuine-rate permutation test ($p{=}0.10$) belongs to a separate hypothesis family (different dataset, independent experimental design) and does not reach significance even without correction; it is reported as an exploratory observation throughout.
212	Bonferroni assumes independence, which is conservative for our setting (several tests use overlapping data); Holm--Bonferroni or Benjamini--Hochberg FDR would recover the matched 5+5 comparison at conventional significance.
213	We report the most conservative Bonferroni results for transparency.
214	
215	\paragraph{Mode distribution $\chi^2$ test.}
216	A pooled $3{\times}2$ contingency table (TS/CE/N-H $\times$ ISR/Random, 3-seed, 500 steps) yields $\chi^2{=}174.8$, $\text{df}{=}2$, $p{=}1.08{\times}10^{-38}$, confirming that ISR reward shifts the overall hacking mode composition, not merely the TS rate.
217	Per-seed tests are individually significant (s42: $\chi^2{=}15.8$, $p{<}0.001$; s43: $\chi^2{=}59.4$, $p{<}10^{-13}$; s44: $\chi^2{=}168.0$, $p{<}10^{-36}$).
218	The previously reported $\text{OR}_{\text{CMH}}{=}2.46$ for TS specifically ($p{<}10^{-8}$) captures a narrower slice of this distributional shift.
219	
220	
221	\section{Hacking Mode Definitions}
222	\label{app:hacking-modes}
223	
224	We identify eight distinct reward hacking modes across all experiments.
225	Each mode is defined below with its mechanism, a representative example, and its interaction with ISR.
226	
227	\begin{table}[t]
228	\centering
229	\small
230	\resizebox{\columnwidth}{!}{%
231	\begin{tabular}{lccccc}
232	\toprule
233	\textbf{Mode} & \textbf{Exec} & \textbf{ISR$_{.1}$} & \textbf{Rnd$_{.1}$} & \textbf{SFT} & \textbf{Prolog$_{\text{ISR}}$} \\
234	\midrule
235	CE embed       & 87 & 18 & 68 & 8 & 0$^\sharp$ \\
236	TS duplicate   & 0  & 71 & 14 & 0 & 100$^\sharp$ \\
237	PG prem-subset & 5  & 5  & 8   & 0 & --- \\
238	Tautological   & --- & --- & --- & --- & s42 \\
239	Repetition     & s43 & --- & --- & --- & --- \\
240	Contradiction  & 1k & --- & --- & --- & --- \\
241	Cmplx.\ vacuous& 0  & 0  & 1  & 0 & --- \\
242	Query-as-fact  & --- & --- & --- & --- & s44 \\
243	\midrule
244	\textbf{Non-hacking} & 8  & 6  & 10 & \textbf{92} & \textbf{0} \\
245	\bottomrule
246	\end{tabular}}
247	\caption{Eight hacking modes across conditions (\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\sharp$Prolog row pools strict+functional (\S\ref{sec:crosslogic}). \texttt{1k} denotes a mode observed only at the 1000-step checkpoint. CE and PG can co-occur; Table~\ref{tab:goodhart-landscape} applies PG${>}$CE priority, reducing Random CE by ${\sim}2$\,pp relative to counts here.}
248	\label{tab:hacking-taxonomy}
249	\end{table}
250	
251	Table~\ref{tab:hacking-taxonomy} provides a compact cross-condition summary; Table~\ref{tab:hacking-taxonomy-app} below gives the extended breakdown.
252	
253	\begin{table*}[ht]
254	\centering
255	\small
256	\begin{tabular}{@{}llcccc@{}}
257	\toprule
258	\textbf{Mode} & \textbf{Mechanism} & \textbf{Exec} & \textbf{ISR} & \textbf{Rnd} & \textbf{SFT} \\
259	\midrule
260	CE & Concl.\ in premises & 87 & 18 & 68 & 8 \\
261	TS & Single prem.\ = concl. & $\bullet$ & \textbf{71} & 14$^\dagger$ & 0 \\
262	PG & Premise-subset gaming & 5 & 5 & 8 & 0 \\
263	Tautological & 2-comp $P{=}C$ & $\bullet$ & 0 & 0 & 0 \\
264	Repetition & Output degen. & $\bullet$ & --- & --- & --- \\
265	Contradiction & $n_{\text{comp}}$ inflated & $\bullet$ & --- & --- & --- \\
266	C-w/o-utility & Complex, redundant & 0 & 0 & 1 & 0 \\
267	Q-as-fact & Atom = fact+query & --- & --- & --- & --- \\
268	\bottomrule
269	\end{tabular}
270	\caption{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta{=}0.1$ 3-seed pooled. TS includes subtypes TSa (text-match, $n{=}149$ ISR $+$ 36 random) and TSb (obfuscated tautology, $n{=}14$; primarily s44). $^\dagger$Random TS driven by seed~43 (38.3\%); seeds~42/44: 0\%. Exec: CE${=}87$\% in s42; $\bullet$ marks seed- or step-specific modes (TS/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). PG: premise-subset gaming (Appendix~\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref{tab:prolog-detailed}).}
271	\label{tab:hacking-taxonomy-app}
272	\end{table*}
273	
274	\paragraph{Classifier Validation.}
275	Hacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.
276	CE and TS are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\text{necessary}}$ distribution from STA (leave-one-out ablation).
277	No training data or manual annotation is used for classification.
278	
279	To estimate precision, we manually verified 50 randomly sampled outputs classified as CE or TS: all 50 were confirmed correct (estimated precision ${>}$95\%, Wilson 95\% CI: [93\%, 100\%]).
280	Recall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.
281	We cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\text{necessary}} \leq 1$ are flagged as potential false negatives.
282	This cross-validation revealed query-as-fact gaming in Prolog (\S\ref{app:hacking-modes}), where the strict text classifier reported 100\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\text{necessary}}{=}1$).
283	The non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.
284	\paragraph{Boundary case validation.}
285	Stratified validation across 82 samples (all five hacking categories) yields Cohen's $\kappa{=}1.0$; independent re-annotation confirms full agreement.
286	Structured inspection of 20 boundary cases (short-conclusion CE (10, minimum 4 characters), low-ISR genuine (5, minimum $\text{ISR}{=}0.22$), and TS on false propositions (5)) confirmed 20/20 correct classifications.
287	Short-conclusion CE samples are unambiguous hacking: the conclusion appears as a standalone premise with no NL source.
288	Low-ISR genuine samples reflect mode-collapsed template outputs, not structural gaming.
289	3/5 TS boundary cases confirm factually false propositions (e.g., affirming ``dogs are plants''), showing TS is not merely vacuous but actively harmful.
290	
291	\begin{table}[h]
292	\centering
293	\small
294	\begin{tabular}{@{}lcr@{}}
295	\toprule
296	\textbf{Mode} & \textbf{Val.\ $N$} & \textbf{Prec.} \\
297	\midrule
298	CE (Concl.\ Embed.) & 80$^\dagger$ & 1.00 \\
299	TS (Tautological) & 7 & 1.00 \\
300	PG (Premise-Subset) & 20 & 1.00 \\
301	Contradiction & 20 & 1.00 \\
302	Genuine & 25 & 1.00 \\
303	\midrule
304	\textbf{Overall} & \textbf{152} & \textbf{1.00} \\
305	\bottomrule
306	\end{tabular}
307	\caption{Per-mode classifier precision on 152 manually validated samples (stratified + boundary + random; three exercises pooled). $^\dagger$Includes 50 randomly sampled CE$\cup$TS outputs (pool ratio CE:TS${=}$374:2). Recall is not estimable from a validation-only design.}
308	\label{tab:classifier-precision}
309	\end{table}
310	
311	The TS\textsubscript{b} subcategory (functional LOO tautologies undetectable by text matching) provides a lower bound on TS recall: ${\geq}91\%$ ($149/163$) under ISR $\beta{=}0.1$. Other modes' recall is not estimable from the validation-only design; non-hacking rates throughout should be interpreted as upper bounds.
312	
313	\subsection{PG -- Premise-Subset Gaming}
314	\label{app:h8}
315	
316	Manual audit of ISR $\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (CE-style).
317	We term this \textbf{PG (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.
318	
319	\paragraph{Detection.} PG is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\text{prem}} \leq 3$) that nonetheless achieve high ISR.
320	Automated detection is not currently feasible because PG requires comparing the generated premise set against the gold premises.
321	
322	\paragraph{Audit scope and limitations.}
323	Full PG audit was completed for ISR $\beta{=}0.1$ seed~42 only.
324	ISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated.
325	Random $\beta{=}0.1$ does not produce PG by mechanism (no ISR optimization pressure); seed~42 audit confirmed PG${=}0$.
326	
327	\paragraph{TS false-negative correction (TSb obfuscated tautology).}
328	ISR $\beta{=}0.1$ seed~44 contained 12 samples with $n_{\text{prem}}{=}1$ classified as non-hacking by the text matcher.
329	Manual inspection confirmed all 12 are logically equivalent to TS but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).
330	We classify these as \textbf{TSb} (obfuscated tautology), distinct from text-match-detectable TSa.
331	$10/12$ achieve $\text{ISR}{\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and TS classifier: triple gaming (\S\ref{sec:taxonomy}).
332	After correction, ISR s44 non-hacking${=}0$; total TS = TSa (77 text-match) + TSb (12 obfuscated) = 89.
333	
334	\paragraph{Impact on non-hacking-rate comparison.}
335	After PG reclassification and TS false-negative correction: ISR non-hacking $= 14/231 = 6.06\%$ vs.\ random non-hacking $= 25/262 = 9.5\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\% CI: ISR [3.6\%, 9.9\%], Random [6.5\%, 13.7\%]).
336	The direction is consistent with ISR-amplified gaming modes (TS, PG) displacing non-hacking output, but the effect is not statistically significant at the conventional $\alpha{=}0.05$ threshold.
337	
338	\subsection{CE -- Conclusion Embedding}
339	
340	\paragraph{Definition.}
341	The conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.
342	The solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.
343	
344	\paragraph{Example (FOL).}
345	\smallskip\noindent\rule{\columnwidth}{0.3pt}
346	{\small\begin{verbatim}
347	Premises:
348	  all x (bird(x) -> flies(x)).
349	  bird(tweety).
350	  flies(tweety).  % conclusion embedded
351	Conclusion: flies(tweety).
352	\end{verbatim}}
353	\noindent\rule{\columnwidth}{0.3pt}\smallskip
354	
355	\paragraph{ISR interaction.}
356	Variable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.
357	ISR does not distinguish trivial from substantive necessity.
358	
359	\paragraph{Prevalence.}
360	Conclusion embedding in some form (CE multi-premise or TS single-premise) is GRPO-universal at 68--97\% across all RL conditions.
361	Under exec-only and Random reward, it manifests as CE (69--93\%); under ISR reward, it shifts to TS (70.6\% pooled).
362	
363	
364	\subsection{TSa -- Conclusion Duplication (Standard)}
365	
366	\paragraph{Definition.}
367	The entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.
368	Since $P \to P$ is trivially provable, this simultaneously maximizes exec reward.
369	Because the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.
370	
371	\paragraph{Example (FOL).}
372	\smallskip\noindent\rule{\columnwidth}{0.3pt}
373	{\small\begin{verbatim}
374	Premises:
375	  all x ((A(x)&B(x))->(C(x)|D(x))).
376	Conclusion:
377	  all x ((A(x)&B(x))->(C(x)|D(x))).
378	\end{verbatim}}
379	\noindent\rule{\columnwidth}{0.3pt}\smallskip
380	
381	\paragraph{ISR interaction.}
382	ISR~$\approx 0.8$--$1.0$.
383	The single premise is trivially ``maximally necessary,'' but the proof is vacuous.
384	TSa games both exec reward and ISR reward; TSb extends this to triple gaming by additionally evading the text-match classifier.
385	
386	\paragraph{Prevalence.}
387	TSa (text-match detectable): 64.5\% pooled (149/231) under ISR~$\beta{=}0.1$ (s42: 16.0\%, s43: 96.7\%, s44: 86.5\%).
388	Combined TS (TSa + TSb): 70.6\% (163/231; s43 TSa${=}59$ + TSb${=}2$; includes s44 FN correction).
389	Random~$\beta{=}0.1$ pooled: 13.7\% (36/262, all TSa; driven by seed~43 at 38.3\%, seeds~42 and~44 at 0\%).
390	
391	
392	\subsection{TSb -- Obfuscated Tautology}
393	
394	\paragraph{Definition.}
395	A single-premise formalization logically equivalent to TSa (premise = conclusion) but with surface-form differences that evade the text-match TS classifier.
396	The model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).
397	
398	\paragraph{Example (FOL, vacuous quantifier wrapping).}
399	\smallskip\noindent\rule{\columnwidth}{0.3pt}
400	{\small\begin{verbatim}
401	Premises:
402	  all x all y ((A(x)&B(y))->(C(x)|D(y))).
403	Conclusion:
404	  all x ((A(x)&B(x))->(C(x)|D(x))).
405	\end{verbatim}}
406	\noindent\rule{\columnwidth}{0.3pt}\smallskip
407	
408	\noindent The premise introduces a vacuous variable $y$, unified with~$x$ at proof time; the formulas are logically equivalent but textually distinct.
409	
410	\paragraph{ISR interaction.}
411	$\text{ISR}{\geq}0.83$ ($10/12$ samples).
412	TSb simultaneously games three objectives: execution reward ($r_{\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match TS classifier (surface-form difference evades detection).
413	This triple gaming makes TSb the most complete Goodhart case we observe.
414	
415	\paragraph{Prevalence.}
416	Found primarily in ISR $\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as non-hacking); seed~43 contributes $2$ additional cases.
417	Functional cross-validation via $n_{\text{necessary}}{=}1$ exposed the misclassification.
418	
419	
420	\subsection{Tautological Collapse}
421	
422	\paragraph{Definition.}
423	Two-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \to P$ tautology with minimal token cost.
424	
425	\paragraph{Example (FOL).}
426	\smallskip\noindent\rule{\columnwidth}{0.3pt}
427	\begin{verbatim}
428	Premises: p(a).
429	Conclusion: p(a).
430	\end{verbatim}
431	\noindent\rule{\columnwidth}{0.3pt}\smallskip
432	
433	\paragraph{ISR interaction.}
434	ISR~$=1.0$ (the sole premise is necessary).
435	Distinguished from TS by having low component count ($n_{\text{comp}}\approx 2$) and atomic formulas rather than complex sub-structured conclusions.
436	
437	\paragraph{Prevalence.}
438	Dominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\text{comp}}=2.04$, 100\% TS by strict classifier).
439	Also observed in Prolog exec+STA seed~42 (100\% TS, PR~$=0.50$).
440	
441	
442	\subsection{Repetition Collapse}
443	
444	\paragraph{Definition.}
445	The model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.
446	Removing any single repeated copy leaves the others intact, yielding ISR~$\approx 0$.
447	
448	\paragraph{Example (Prolog).}
449	\smallskip\noindent\rule{\columnwidth}{0.3pt}
450	\begin{verbatim}
451	penguin(fido).
452	penguin(fido).
453	penguin(fido).
454	... (repeated to 512 tokens)
455	query(penguin(fido)).
456	\end{verbatim}
457	\noindent\rule{\columnwidth}{0.3pt}\smallskip
458	
459	\paragraph{ISR interaction.}
460	ISR~$\approx 0$. Each copy is individually redundant since identical copies remain after removal.
461	ISR correctly diagnoses this degeneration.
462	
463	\paragraph{Prevalence.}
464	Observed in FOL exec-only seed~43 (87\% of outputs hit max completion length; PR~$=13$\%, ISR~$=0$).
465	
466	
467	\subsection{Complexity-without-Utility}
468	
469	\paragraph{Definition.}
470	The formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous: none individually necessary for the proof.
471	The complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.
472	
473	\paragraph{Example (FOL).}
474	\smallskip\noindent\rule{\columnwidth}{0.3pt}
475	{\small\begin{verbatim}
476	Premises:
477	  all x all y (R(x,y) ->
478	    exists z (S(x,z) & T(z,y))).
479	  all x (P(x) -> Q(x)).
480	  P(a).            % only this needed
481	Conclusion: Q(a).
482	\end{verbatim}}
483	\noindent\rule{\columnwidth}{0.3pt}\smallskip
484	
485	\paragraph{ISR interaction.}
486	ISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.
487	This is the mode ISR is best calibrated for.
488	
489	\paragraph{Prevalence.}
490	Low. Observed in Random~$\beta{=}0.1$ seed~42 at 3.8\% (3/79).
491	Not observed under ISR reward (ISR's gradient discourages zero-ISR premises).
492	
493	
494	\subsection{Contradiction Explosion}
495	
496	\paragraph{Definition.}
497	The component count grows unboundedly over training.
498	Excess premises introduce contradictions or redundancies that trivially entail any conclusion via \emph{ex falso quodlibet}.
499	Individual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.
500	
501	\paragraph{Example (FOL, 1000-step exec-only).}
502	\smallskip\noindent\rule{\columnwidth}{0.3pt}
503	{\small\begin{verbatim}
504	Premises:
505	  c1. c2. c3. ... c18. % 18.55 mean
506	  % conclusion embedded among premises
507	Conclusion: Q(a).
508	\end{verbatim}}
509	\noindent\rule{\columnwidth}{0.3pt}\smallskip
510	
511	\paragraph{ISR interaction.}
512	ISR~$\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\% of proved samples having ISR~$=0$).
513	
514	\paragraph{Prevalence.}
515	Observed in extended exec-only training (seed~42, 1000 steps).
516	Mean component count grows from ${\sim}6$ (500 steps) to 18.55 (1000 steps).
517	
518	
519	\subsection{Query-as-Fact Gaming}
520	
521	\paragraph{Definition.}
522	The model converts the natural language conclusion into a snake\_case atom and includes it as both a ground fact and the query.
523	Prolog trivially proves the query by unifying with the fact.
524	This mode evades text-match classifiers designed for CE/TS because the generated atom bears no surface resemblance to the original conclusion text.
525	
526	\paragraph{Example (Prolog).}
527	\smallskip\noindent\rule{\columnwidth}{0.3pt}
528	\begin{verbatim}
529	% NL: "Fido is happy."
530	% Model output:
531	fido_is_happy.
532	:- fido_is_happy.     % query = fact
533	\end{verbatim}
534	\noindent\rule{\columnwidth}{0.3pt}\smallskip
535	
536	\paragraph{ISR interaction.}
537	ISR~$\approx 0.9$--$1.0$.
538	The single fact is trivially necessary (its removal breaks the query), inflating ISR.
539	Functionally equivalent to TS but with a distinct surface mechanism.
540	
541	\paragraph{Prevalence.}
542	Observed in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).
543	95/97 proved samples have $n_{\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\% non-hacking.
544	
545	
546	\section{Per-Seed Detailed Results}
547	\label{app:detailed-results}
548	
549	Tables~\ref{tab:fol-beta01-detailed} and \ref{tab:prolog-detailed} report full per-seed results.
550	All metrics are computed by \texttt{eval\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.
551	ISR values are proved-only ISR$^*$.
552	
553	\begin{table*}[t]
554	\centering
555	\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\beta{=}0.1$ breakdown referenced from Table~\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\ = percentage among proved samples. ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$). $^\ddagger$Three s44-1000 samples escape text-match heuristics (CE/PG classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass PG detection and commuted premises that bypass CE detection; reclassified as degenerate. $^\diamond$Seeds 45--46 added post-hoc under identical hyperparameters (effective batch size 8; micro-batch decomposition differs: $4{\times}2$ vs.\ $2{\times}4$, mathematically equivalent).}
556	\label{tab:fol-detailed}
557	\label{tab:fol-beta01-detailed}
558	\small
559	\setlength{\tabcolsep}{3pt}
560	\resizebox{\textwidth}{!}{%
561	\begin{tabular}{@{}llccccccl@{}}
562	\toprule
563	\textbf{Condition} & \textbf{Seed} & \textbf{Steps} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Notes} \\
564	\midrule
565	\multicolumn{9}{@{}l}{\textit{Baselines}} \\
566	Base model (no training)
567	  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\
568	Ground-truth FOL
569	  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
570	SFT
571	  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \textbf{92.3} & Supervised, no RL \\
572	  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \textbf{90.9} & \\
573	  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \textbf{93.3} & \\
574	\cmidrule(l){2-9}
575	  & \multicolumn{2}{l}{3-seed pooled} & $0.130$ & $0.595$ & $0$ & $7.8$ & \textbf{92.3} & $n{=}39$ proved \\
576	\midrule
577	\multicolumn{9}{@{}l}{\textit{Exec-only}} \\
578	  & 42 & 100 & 0.32 & \textbf{0.642} & --- & --- & --- & Early checkpoint \\
579	  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & PG${=}5.4\%$ \\
580	  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\
581	  & 43 & 500 & 0.13 & 0$^\dagger$ & --- & --- & --- & $^\dagger$Greedy ($n_{\text{proved}}{=}13$) \\
582	  & 43 & 1000 & 0.96 & 0.082 & 0 & 93.8 & 6.2 & CE dominant \\
583	  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\
584	  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\ddagger$ & PG${=}15\%$ \\
585	\cmidrule(l){2-9}
586	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.68{\pm}0.47$ & $0.238{\pm}0.30$ & & & & 500-step \\
587	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.97{\pm}0.02$ & $0.029{\pm}0.05$ & & & $2.1{\pm}3.6$ & 1000-step \\
588	\midrule
589	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
590	  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \textbf{17.3} & Mixed CE+TS+PG \\
591	  & 42 & 1000 & 0.90 & 0.877 & 96.7 & 0 & 2.2 & TS collapse; PG${=}1$ ($n{=}90$) \\
592	  & 43 & 500 & 0.61 & 0.830 & \textbf{100} & 0 & 0 & TSa${=}59$, TSb${=}2$ \\
593	  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & TS dominant (FN corrected) \\
594	  & 45$^\diamond$ & 500 & 0.42 & 0.605 & 38.1 & 4.8 & \textbf{54.8} & PG${=}1$; $n{=}42$ \\
595	  & 46$^\diamond$ & 500 & 0.77 & 0.411 & 14.3 & 26.0 & \textbf{54.5} & PG${=}4$; $n{=}77$ \\
596	\cmidrule(l){2-9}
597	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.77{\pm}0.14$ & $0.716{\pm}0.26$ & & & & 500-step (s42--44) \\
598	  & \multicolumn{2}{l}{5-seed mean$\pm$std} & $0.70{\pm}0.19$ & $0.633{\pm}0.23$ & & & & 500-step (s42--46) \\
599	\midrule
600	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
601	  & \multicolumn{8}{l}{See Table~\ref{tab:beta03-detailed} for per-seed $\beta{=}0.3$ results.} \\
602	\midrule
603	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.1$}} \\
604	  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & PG${=}4$ \\
605	  & 43 & 500 & 0.94 & 0.150 & \textbf{38.3} & 59.6 & 1.1 & TSa${=}36$; PG${=}1$ \\
606	  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & PG${=}16$ (CE$\cap$PG: 6) \\
607	\cmidrule(l){2-9}
608	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.87{\pm}0.08$ & $0.117{\pm}0.042$ & & & & TS seed-dep.: 0/38/0\% \\
609	\midrule
610	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
611	  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ (D086); $n_{\text{comp}} = 9.6$ \\
612	  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\text{N-H}}{=}3$ \\
613	  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\
614	\cmidrule(l){2-9}
615	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.54{\pm}0.35$ & $0.09{\pm}0.09$ & & & & \\
616	\midrule
617	\multicolumn{9}{@{}l}{\textit{Shuffled-ISR $\beta{=}0.1$ (deconfounding control)}} \\
618	  & 42 & 500 & 0.15 & 0.567 & 6.7 & 6.7 & \textbf{86.7} & $n{=}15$ proved \\
619	  & 43 & 500 & 0.16 & 0.568 & 6.3 & 6.3 & \textbf{87.5} & $n{=}16$ proved \\
620	  & 44 & 500 & 0.15 & 0.542 & 6.7 & 6.7 & \textbf{86.7} & $n{=}15$ proved \\
621	\cmidrule(l){2-9}
622	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.153{\pm}0.006$ & $0.559{\pm}0.015$ & $6.5$ & $6.5$ & \textbf{87.0} & $N{=}46$ proved \\
623	\bottomrule
624	\end{tabular}}% end resizebox
625	\end{table*}
626	
627	\begin{table*}[t]
628	\centering
629	\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\ = percentage among proved samples.  ``---'' indicates data not available.}
630	\label{tab:prolog-detailed}
631	\small
632	\begin{tabular}{@{}llcccccl@{}}
633	\toprule
634	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Notes} \\
635	\midrule
636	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
637	  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\
638	  & 43 & 0.56 & 0.015 & --- & --- & --- & \\
639	  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\
640	\cmidrule(l){2-8}
641	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.53{\pm}0.31$ & $0.146{\pm}0.21$ & & & \\
642	\midrule
643	\multicolumn{8}{@{}l}{\textit{Exec+ISR (STA reward)}} \\
644	  & 42 & 0.50 & 1.000 & \textbf{100} & 0 & 0 & TS tautological \\
645	  & 43 & 0.38 & 0.185 & 0$^\ddagger$ & 97.4 & 0 & $^\ddagger$Functional TS$^a$ \\
646	  & 44 & 0.97 & 0.912 & 0$^\ddagger$ & 0 & 0$^\ddagger$ & Query-as-fact gaming$^b$ \\
647	\cmidrule(l){2-8}
648	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.62{\pm}0.31$ & $0.699{\pm}0.45$ & & & 3/3 Goodhart, 0\% non-hacking \\
649	\bottomrule
650	\end{tabular}
651	
652	\vspace{4pt}
653	{\small
654	$^a$ Strict TS classifier reports 0\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\
655	$^b$ Strict classifier reports Non-hacking$\,{=}\,100$\%, but 95/97 proved samples have $n_{\text{necessary}}=1$. The model converts NL to snake\_case atoms serving as both fact and query, a third distinct Goodhart pathway.\\
656	$^\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.
657	}
658	\end{table*}
659	
660	\begin{table*}[t]
661	\centering
662	\caption{Detailed per-seed results: ProofFOL (Prover9). PR$_{\text{f50}}$ = mean prove rate over final 50 steps. TS = tautological shortcutting (\S\ref{sec:taxonomy}), CE = conclusion embedding, Genuine = classified as neither TS nor CE. Stable convergence: PR$_{\text{f50}}{>}0.90$.}
663	\label{tab:prooffol-detailed}
664	\small
665	\begin{tabular}{@{}llcccccl@{}}
666	\toprule
667	\textbf{Condition} & \textbf{Seed} & \textbf{PR$_{\text{f50}}$} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{Genuine\%} & \textbf{Notes} \\
668	\midrule
669	Base & --- & 0.16 & 0.310 & 0 & 0 & \textbf{100} & $n{=}16$ proved \\
670	\midrule
671	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
672	  & 42 & ${\approx}$1.0 & 0.066 & \textbf{100} & 0 & 0 & $n{=}99$; stable \\
673	  & 43 & 0.55 & 0.119 & 0 & 49.2 & 50.8 & $n{=}63$; partial \\
674	  & 44 & ${\approx}$1.0 & 0.043 & 0 & 98.6 & 1.4 & $n{=}72$; stable \\
675	\cmidrule(l){2-8}
676	  & \multicolumn{2}{l}{Aggregate} & & \multicolumn{3}{c}{17.4\% genuine (mean of seeds)} & \\
677	\midrule
678	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
679	  & 42 & 0.35 & 0.12 & 0 & 0 & \textbf{100} & $n{=}46$; collapsed \\
680	  & 43 & ${\approx}$0.47 & ${\approx}$0.13 & 0 & 69.6 & 30.4 & $n{=}56$; unstable \\
681	  & 44 & 0.49 & 0.145 & 0 & 0 & \textbf{100} & $n{=}66$; oscillation \\
682	\cmidrule(l){2-8}
683	  & \multicolumn{2}{l}{Aggregate} & & \multicolumn{3}{c}{\textbf{76.8\%} genuine (mean of seeds)} & \\
684	\bottomrule
685	\end{tabular}
686	
687	\vspace{4pt}
688	{\small Aggregate genuine rate: mean of per-seed genuine rates. Permutation test (exec vs.\ ISR genuine): $p{=}0.10$, $N{=}3$ per group.}
689	\end{table*}
690	
691	\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}
692	Table~\ref{tab:fol-detailed} traces the ISR collapse over training:
693	ISR$^*=0.642$ at 100 steps $\to$ $0.132$ at 500 steps ($-79.4$\%) $\to$ $0.003$ at 1000 steps ($-99.5$\% from step 100).
694	PR increases monotonically ($0.32 \to 0.93 \to 0.96$) while component necessity collapses, confirming that ISR flags degeneration invisible to execution reward.
695	By step 1000, 94.8\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.
696	
697	\paragraph{Prolog: universal Goodhart via three distinct pathways.}
698	All three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\% non-hacking proofs (Figure~\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:
699	seed~42 produces clean TS tautologies (single premise~$=$~conclusion),
700	seed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,
701	and seed~44 converts NL conclusions to snake\_case atoms used as both fact and query.
702	The diversity of gaming pathways across seeds (despite identical training data and reward function) demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.
703	
704	\subsection{Per-Seed Results at $\beta{=}0.2$ and $\beta{=}0.3$}
705	\label{app:beta03}
706	
707	Table~\ref{tab:beta03-detailed} reports per-seed results for ISR at $\beta{=}0.2$ and both ISR and Random at $\beta{=}0.3$.
708	At $\beta{=}0.2$, all three seeds converge to pure TS Goodhart (100\% or near-100\% TS), confirming $\beta{\geq}0.2$ as the extremal Goodhart regime.
709	The three ISR $\beta{=}0.3$ seeds illustrate qualitatively distinct Goodhart pathways (\S\ref{sec:goodhart}).
710	
711	\begin{table*}[ht]
712	\centering
713	\caption{Per-seed results at $\beta{=}0.2$ and $\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H = percentage among proved samples.}
714	\label{tab:beta03-detailed}
715	\small
716	\begin{tabular}{@{}llcccccl@{}}
717	\toprule
718	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Mode} \\
719	\midrule
720	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.2$}} \\
721	  & 42 & 1.00 & 0.602 & \textbf{100} & 0 & 0 & Pure TS ($n{=}100$) \\
722	  & 43 & 0.96 & 0.552 & \textbf{96.9} & 1.0 & 0 & PG${=}2$ \\
723	  & 44 & 0.94 & 0.964 & \textbf{100} & 0 & 0 & Pure TS ($n{=}94$) \\
724	\cmidrule(l){2-8}
725	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.97{\pm}0.03$ & $0.71{\pm}0.22$ & & & 3/3 TS Goodhart \\
726	\midrule
727	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
728	  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); PG${=}3$ \\
729	  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 23.3 & CE shortcutting \\
730	  & 44 & 0.95 & 0.742 & \textbf{100} & 0 & 0 & Pure TS Goodhart \\
731	\cmidrule(l){2-8}
732	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.66{\pm}0.42$ & $0.39{\pm}0.31$ & & & \\
733	\midrule
734	\multicolumn{8}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
735	  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ (D086) \\
736	  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\text{N-H}}{=}3$ \\
737	  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\
738	\cmidrule(l){2-8}
739	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.54{\pm}0.35$ & $0.09{\pm}0.09$ & & & \\
740	\bottomrule
741	\end{tabular}
742	\end{table*}
743	
744	\FloatBarrier
745	
746	\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}
747	\label{app:100step}
748	
749	To control for the prove-rate confound in our SFT comparison (\S\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\%, higher than SFT (13.0\%, 3-seed pooled) but still early in training.
750	Of the 32 proved samples, 9 (28.1\%) exhibit TS hacking (single premise identical to conclusion) and 1 (3.1\%) exhibits CE (conclusion embedded among premises), yielding a total hacking rate of 31.2\%.
751	By contrast, SFT at comparable or lower PR shows 7.7\% hacking (1/13 proved samples).
752	This demonstrates that reward hacking emerges early in GRPO training, well before the prove-rate plateau, and is not simply an artifact of having more proved samples available for exploitation.
753	The 100-step hacking rate (31.2\%) is already substantially above SFT (7.7\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.
754	
755	\subsection{$O(1)$ vs.\ $O(n)$ ISR Ablation}
756	\label{app:o1-ablation}
757	
758	All main experiments (\S\ref{sec:diagnostic}--\ref{sec:crossdomain}) use $O(n)$ full LOO ISR during both training and evaluation; the $O(1)$ binary variant described below exists as an alternative implementation (\texttt{execution\_fast\_sta}) but is used only in the ablation reported here.
759	The two signals measure fundamentally different properties, not approximations of the same quantity.
760	The binary signal tests \emph{collective} premise necessity: $\text{fast\_ISR}(x) = 1$ if $x$ is proved and the conclusion is not provable under empty premises (tautology check), $0$ otherwise.
761	LOO tests \emph{individual} premise necessity: each component is removed in turn, and ISR reflects the fraction whose removal causes proof failure.
762	
763	\paragraph{Evaluation-time comparison.}
764	Across 402 proved samples from all ProofFOL conditions, the $O(1)$ binary signal is 1.0 for every sample: non-tautological conclusions cannot be proved without any premises, so the collective necessity test is trivially satisfied.
765	This renders $O(1)$ unable to distinguish hacking from genuine formalizations: both pass the empty-premise check.
766	By contrast, $O(n)$ LOO produces a clear separation: exec-only models average $\text{ISR}^*{=}0.046$ ($n{=}234$) while ISR-trained models average $\text{ISR}^*{=}0.183$ ($n{=}168$), because hacking constructions contain individually redundant components that LOO detects.
767	Of 179 disagreements between the two signals, all are false positives ($O(1){=}1$, LOO${=}0$): the binary check approves formalizations that LOO correctly identifies as structurally degenerate.
768	
769	\paragraph{Training-time ablation.}
770	As a training reward ($r = 0.5\,r_{\text{exec}} + 0.5\,\text{fast\_ISR}$, seed~42, 500 steps), the $O(1)$ variant achieves $\text{PR}{=}63\%$ with $\text{ISR}^*{=}0.007$, functionally zero, compared to $\text{ISR}^*{=}0.132$ under exec-only and $\text{ISR}^*{=}0.42$ under $O(n)$ ISR $\beta{=}0.1$.
771	The tautology check depresses prove rate by 30\,pp relative to exec-only ($63\%$ vs.\ $93\%$) by penalizing formalizations where the conclusion is provable without premises, but this constraint provides no gradient toward individual component necessity; the model is free to degenerate as long as it avoids trivial tautologies.
772	That even the fine-grained $O(n)$ LOO signal, which \emph{does} provide per-component necessity feedback, is ultimately gamed (\S\ref{sec:goodhart}) underscores that the problem lies in reward optimization itself, not in signal granularity.
773	
774	\paragraph{Computational overhead.}
775	Full LOO requires $n{+}1$ solver calls per sample (mean $n{\approx}6$ for FOLIO).
776	With Prover9 at ${\sim}5$\,ms per call, STA evaluation adds ${\sim}55$\,ms per sample versus ${\sim}4$\,s for LLM inference (${<}1\%$ overhead).
777	The $O(1)$ binary check adds a single solver call per proved sample (${<}2\%$ per training step), but the evaluation above shows this saving comes at the cost of all diagnostic power.
778	
779	\subsection{Cross-Model Generalization: LLaMA-3.2-3B Cold-Start Failure}
780	\label{app:llama-coldstart}
781	
782	We applied the identical GRPO configuration (Table~\ref{tab:hyperparams}) to LLaMA-3.2-3B~\citep{grattafiori2024llama} (3B; exec-only, seed~42, $K{=}4$, FOLIO).
783	Across 72 of 500 planned steps the model produced zero valid Prover9 output, generating only natural-language text; $r_{\text{exec}}{=}0$ for all rollouts yields zero GRPO advantage, so training was terminated early.\footnote{This run was also affected by a generation-termination configuration issue (dual EOS tokens); the zero prove rate reflects both the base model's lack of FOL generation capability and truncated outputs.}
784	This establishes a \emph{capability threshold}: the base model must produce syntactically valid solver input for the RL loop to generate signal.
785	Qwen3-4B crosses this threshold (non-zero prove rates within 10 steps) while LLaMA-3.2-3B does not despite comparable size (3B vs.\ 4B), likely reflecting pretraining data composition.
786	An SFT warmstart (3 epochs on gold formalizations, lr$=$2$\times$10$^{-5}$) achieves $\text{PR}{=}16\%$ ($n{=}100$) after correcting the generation-termination issue.
787	However, the model produces Unicode FOL notation ($\forall$, $\to$, $\wedge$) instead of the required ASCII syntax despite training on ASCII-formatted data; the 16\% prove rate reflects Prover9's partial Unicode tolerance rather than correct format adherence.
788	Subsequent GRPO runs (exec-only, 500 steps from SFT warmstart, 3 seeds) fail to improve beyond SFT baseline ($\text{PR}{=}15.0{\pm}1.0\%$, $n{=}14$--$16$ proved per seed), yet produce no structural degeneration: $86.6{\pm}0.9\%$ of proved samples are genuine across seeds, with cross-seed variance near zero ($\sigma_{\text{PR}}{=}1$\,pp).
789	This contrasts sharply with Qwen3-4B, where GRPO reaches $93\%$ PR but collapses to $8\%$ genuine with high cross-seed variance.
790	The result suggests structural degeneration is a byproduct of successful RL optimization, not of the training procedure \emph{per se}: when GRPO fails to amplify prove rate, the model retains structural integrity.
791	
792	\subsection{Seed-Dependent Convergence in Exec-Only GRPO}
793	\label{app:seed-convergence}
794	
795	Not all exec-only seeds converge.
796	Of 6 seeds tested (s42--s46, s52; s52 uses $K{=}4$, all others $K{=}8$), we observe three regimes: \emph{converging with degeneration} (s42: $\text{PR}{=}93\%$, genuine${=}7.5\%$; s44: $\text{PR}{=}96\%$, genuine${=}0\%$; s46: $\text{PR}{=}93\%$ at 500 steps), \emph{slow convergence with degeneration} (s43: $\text{PR}{=}14\%$ but $100\%$ hacking at 500 steps), and \emph{non-converging} (s45: $\text{PR}{=}15\%$, genuine${=}86.7\%$; s52: $\text{PR}{=}14\%$, genuine${=}85.7\%$).
797	Non-converging seeds retain high genuine rates (85--87\%), indicating that structural degeneration is conditional on successful RL optimization: when GRPO fails to bootstrap prove rate beyond base-model levels, the model preserves structural integrity.
798	Extended training to 1000 steps for s45 confirms persistent non-convergence ($\text{PR}{=}15\%$, $\text{ISR}^*{=}0.592$, genuine${=}86.7\%$, $n{=}15$ proved); the model neither improves nor degenerates.
799	
800	This parallels the LLaMA-3.2-3B finding (Appendix~\ref{app:llama-coldstart}), where GRPO also fails to improve PR and retains structural quality.
801	Both cases support the interpretation that degeneration is a byproduct of reward optimization success, not of the training procedure per se.
802	
803	\subsection{$N{=}2$ Sensitivity Analysis (Excluding Seed 43)}
804	\label{app:n2-sensitivity}
805	
806	Seed~43 was evaluated with sampling ($T{=}0.7$) rather than greedy decoding (\S\ref{app:setup}).
807	To assess whether this non-standard protocol affects qualitative conclusions, Table~\ref{tab:n2-sensitivity} reports pooled statistics from seeds~42 and~44 only.
808	
809	\begin{table}[h]
810	\centering
811	\resizebox{\columnwidth}{!}{%
812	\begin{tabular}{@{}lccc@{}}
813	\toprule
814	\textbf{Condition} & \textbf{PR (\%)} & \textbf{ISR$^*$} & \textbf{N-H (\%)} \\
815	\midrule
816	Exec-only 500-step & $95.5 \pm 3.5$ & $0.357 \pm 0.318$ & $3.8 \pm 5.3$ \\
817	Exec-only 1000-step & $98.0 \pm 2.8$ & $0.003 \pm 0.001$ & $0.0 \pm 0.0$ \\
818	ISR $\beta{=}0.1$ 500-step & $85.0 \pm 5.7$ & $0.659 \pm 0.344$ & $8.7 \pm 12.2$ \\
819	\bottomrule
820	\end{tabular}}
821	\caption{Pooled statistics excluding seed~43 ($N{=}2$, seeds~42 and~44 only). Mean$\pm$std of per-seed values. Qualitative patterns preserved: exec-only converges to ${\leq}7.5\%$ non-hacking; ISR $\beta{=}0.1$ shifts composition toward TS.}
822	\label{tab:n2-sensitivity}
823	\end{table}
824	
825	Excluding seed~43, exec-only converges to ${\leq}7.5\%$ non-hacking at 500 steps and $0\%$ at 1000 steps.
826	Under ISR $\beta{=}0.1$, TS dominates both remaining seeds (s42: $16\%$, s44: $100\%$), confirming that ISR reward shifts hacking composition toward tautological shortcuts independent of the s43 evaluation anomaly.
827	The large per-seed ISR$^*$ variance ($0.357 \pm 0.318$) reflects different degeneration modes (CE in s42 vs.\ TS in s44), not data quality issues.
828	
829	\subsection{Cross-Scale: Qwen3-8B Exec-Only GRPO}
830	\label{app:8b-results}
831	
832	To test whether structural degeneration generalizes beyond 4B scale, we apply exec-only GRPO to Qwen3-8B with $K{=}8$ rollouts per prompt ($K{=}4$ produces near-identical completions at 8B scale, yielding zero GRPO advantage and no learning signal).
833	Table~\ref{tab:8b-combined} summarizes configuration differences and results.
834	
835	\begin{table}[H]
836	\centering
837	\small
838	\begin{tabular}{lcc}
839	\toprule
840	& \textbf{Qwen3-4B} & \textbf{Qwen3-8B} \\
841	\midrule
842	Rollouts ($K$) & 4 & 8 \\
843	Batch size & 4 & 1 \\
844	Gradient accum. & 2 & 16 \\
845	Effective batch & 8 & 16 \\
846	\bottomrule
847	\end{tabular}
848	
849	\vspace{4pt}
850	
851	\resizebox{\columnwidth}{!}{%
852	\begin{tabular}{lcccc}
853	\toprule
854	\textbf{Config} & \textbf{PR\%} & \textbf{Genuine\%} & \textbf{Converged?} & \textbf{Gradient} \\
855	\midrule
856	4B $K{=}4$ s42 & 93 & 7.5 & Yes (degenerate) & Sufficient \\
857	8B $K{=}4$ s42 & 15.5 & --- & No & Zero \\
858	8B $K{=}8$ s42 & 14 & 92.9 & No & Partial \\
859	\bottomrule
860	\end{tabular}}
861	\caption{Cross-scale: Qwen3-4B vs.\ Qwen3-8B. \textbf{Top}: Configuration; $K{=}8$ required at 8B because $K{=}4$ produces near-identical rollouts. \textbf{Bottom}: Results; 4B converges with degeneration, both 8B configurations fail to converge, preserving structural integrity.}
862	\label{tab:8b-combined}
863	\end{table}
864	
865	We first tested $K{=}4$ (matching the 4B configuration): the 8B model produces near-identical rollouts across all four completions, yielding zero GRPO advantage throughout 500 steps and no learning signal ($\text{PR}{=}15.5\%$, cold-start stagnation).
866	Increasing to $K{=}8$ provides non-zero reward variance during mid-training (approximately 40--50\% of steps between 20--370 show non-zero advantage), but this signal proves insufficient for convergence: held-out evaluation yields $\text{PR}{=}14\%$ ($n{=}14$ proved), $\text{ISR}^*{=}0.573$, genuine${=}92.9\%$ (13/14), with a single CE sample.
867	Cosine learning-rate decay combined with insufficient early bootstrap appears to prevent the model from escaping the low-PR regime.
868	
869	This result mirrors two other non-convergence cases: (1)~the seed-dependent 4B non-convergence (s45, s52; Appendix~\ref{app:seed-convergence}), where identical 4B configurations fail to bootstrap, and (2)~the LLaMA-3.2-3B cold-start failure (Appendix~\ref{app:llama-coldstart}), where the base model lacks FOL generation capability entirely.
870	Together, these cases establish a convergence threshold for GRPO-driven degeneration: the structural collapse documented in \S\ref{sec:diagnostic} requires successful RL optimization as a prerequisite, and at 8B scale the rollout diversity bottleneck prevents this optimization from occurring under our configuration.
871	
872	\section{Use of AI Assistants}
873	\label{app:ai-assistants}
874	
875	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
876	\begin{itemize}
877	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
878	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \LaTeX{}.
879	    \item \textbf{Literature:} summarizing related papers to inform the related-work section.
880	\end{itemize}
881	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b314621-c614-41a6-844c-9349dd2e2a29",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "e5f114e1-d347-4941-affb-a875ac4f82d7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
      "content": "% Appendix — solver-trace-ablation\n\n\\section{Experimental Setup}\n\\label{app:setup}\n\nTable~\\ref{tab:hyperparams} lists all hyperparameters shared across experiments.\nAll RL conditions use the same GRPO configuration; only the reward function differs.\nSeeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).\n\n\\begin{table}[ht]\n\\centering\n\\caption{Training hyperparameters for all GRPO experiments.}\n\\label{tab:hyperparams}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll@{}}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Model}} \\\\\nBase model & Qwen3-4B \\\\\nPrecision & BF16 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{GRPO Training}} \\\\\nRollouts per prompt ($K$) & 4 \\\\\nTraining steps (default) & 500 \\\\\nTraining steps (extended) & 1000 \\\\\nLearning rate & $1 \\times 10^{-6}$ \\\\\nPer-device batch size & 4 \\\\\nGradient accumulation steps & 2 \\\\\nEffective batch size & 8 \\\\\nMax completion length & 512 tokens \\\\\nRandom seeds & 42, 43, 44 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Data}} \\\\\nTraining set & FOLIO, 500 examples \\\\\nEvaluation set & FOLIO, 100 examples (held-out) \\\\\nData file & \\texttt{train\\_500\\_seed42} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Solvers}} \\\\\nFOL solver & Prover9 \\\\\nProlog solver & SWI-Prolog 8.4.2 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Evaluation}} \\\\\nDecoding & Greedy ($T{=}0$) \\\\\nISR computation & \\texttt{eval\\_sta.py} \\\\\nISR variant & Proved-only (ISR$^*$) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Compute resources.}\nExperiments were run on single-GPU setups (NVIDIA RTX 4090 24\\,GB and RTX PRO 6000 96\\,GB).\nEach GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).\nTotal compute across all seeds, conditions, and reruns is approximately 80--120 GPU-hours.\n\n\\paragraph{SFT convergence.}\nSFT training converged across all three seeds: final-step loss ${\\leq}0.04$ and token accuracy ${>}99\\%$ after ${\\sim}8$ epochs on 500 examples (seed~42: $0.029$; seed~44: $0.033$); the 1000-step extension further decreases loss to $0.017$.\n\n\\paragraph{Evaluation exception.}\nFOL exec-only seed~43 (\\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.\nIts PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).\n\n\\paragraph{Reward formulation.}\nAn additive variant ($r = r_{\\text{exec}} + \\beta\\,\\text{ISR}$) was tested in early experiments but collapsed prove rate to near-zero, as ISR alone provides no gradient toward provable formalizations; the multiplicative form $r_{\\text{exec}}\\cdot(1+\\beta\\,\\text{ISR})$ ensures ISR modulates only proved outputs.\n\n\\paragraph{ProofFOL dataset construction.}\n\\label{app:prooffol-construction}\nProofFOL is derived from ProofWriter~\\citep{proofwriter} (10{,}424 training examples) via the GPT-4o silver-standard FOL translation pipeline of \\citet{prooffol-thatikonda2024} with Prover9 verification filtering (${\\sim}70\\%$ retention; failures from timeouts, unsupported constructs, and translation errors).\nOf the translated examples, 99.1\\% parse successfully (92 skipped due to empty FOL output).\nWe sample 500 training and 100 evaluation examples (seed~42) from the verified pool.\nTable~\\ref{tab:prooffol-vs-folio} compares key structural properties.\n\n\\begin{table}[!ht]\n\\centering\n\\caption{ProofFOL vs.\\ FOLIO structural comparison (training sets, $n{=}500$ each).}\n\\label{tab:prooffol-vs-folio}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Property} & \\textbf{ProofFOL} & \\textbf{FOLIO} \\\\\n\\midrule\nFOL premises (mean$\\pm$std) & $18.2 \\pm 3.2$ & $5.3 \\pm 1.4$ \\\\\n\\quad Ground facts & $10.2 \\pm 3.0$ & $1.8 \\pm 1.5$ \\\\\n\\quad Rules & $8.1 \\pm 1.1$ & $3.5 \\pm 1.9$ \\\\\nXOR ($\\oplus$) samples & 0\\% & 37.2\\% \\\\\nDominant depth & 4--5 & 2--3 \\\\\nPredicate style & synthetic & real-world \\\\\nFOL source & GPT-4o (silver) & human (gold) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nProofFOL problems are structurally more complex ($3.4{\\times}$ more premises) but use simpler, synthetic predicates (e.g., \\texttt{Blue(x)}, \\texttt{Rough(x)}) characteristic of ProofWriter's procedural generation.\nThe absence of XOR constraints and the regularity of predicate structure make ProofFOL a complementary testbed: structural degeneration must emerge from the RL training dynamics rather than from formalization difficulty.\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\n\\paragraph{What ISR measures---and what it does not.}\nISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.\nThis is strictly weaker than semantic faithfulness: whether the formalization accurately captures the natural-language meaning.\nWe verify this empirically: Spearman $\\rho(\\text{ISR}, \\text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.\nISR and downstream task performance are uncorrelated.\nISR is thus a component-necessity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.\n\nCritically, low ISR carries different semantics depending on the training objective.\nUnder exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\\S\\ref{sec:crosslogic}).\nUnder ISR-as-reward, high ISR reflects metric gaming (\\S\\ref{sec:goodhart}).\nISR values must always be interpreted relative to the optimization objective that produced them.\n\n\\paragraph{ISR as $(n{-}1)$-coalition Shapley value.}\n\\label{app:shapley}\nDefine a cooperative game $(N, v)$ with player set $N = \\{1,\\ldots,n\\}$ (components) and binary utility $v(S) = \\mathbf{1}[S(S){=}\\textit{proved}]$.\nThe Shapley value $\\phi_i$ averages marginal contributions over all coalition sizes; ISR restricts to the maximal coalition $|S|{=}n{-}1$, giving $\\phi_i^{\\text{LOO}} = \\frac{1}{n}[v(N) - v(N \\setminus \\{i\\})]$.\nSumming: $\\text{ISR}(x) = \\sum_i \\phi_i^{\\text{LOO}} = \\frac{1}{n}\\sum_i \\mathbf{1}[v(N \\setminus \\{i\\}){=}0]$, recovering Equation~\\ref{eq:isr}.\nThis restriction trades full interaction detection for $O(n)$ cost; the binary solver output makes higher-order interactions unobservable from LOO alone (\\S\\ref{sec:sta}).\n\n\\paragraph{The premise-count confound.}\n\\label{app:premise-count}\nLOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.\nA formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.\nThis confound explains the sole apparent ISR-as-reward success (\\S\\ref{sec:goodhart}): ISR $\\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.\nPremise-count-matched comparison eliminates the difference ($1.06\\times$, McNemar's test $p{=}0.317$; Table~\\ref{tab:fol-beta01-detailed}), confirming that the scalar ISR advantage is not statistically significant.\nThis bias is not specific to our setting: any LOO-based structural metric applied to variable-length outputs requires component-count normalization.\nWe recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.\nMode composition analysis (CE vs.\\ TS rates) is unaffected by premise-count confounding because TS classification depends on tautological proof structure (\\S\\ref{app:hacking-modes}), not on the number of premises in the formalization.\n\n\\begin{table}[h]\n\\centering\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrrrr@{}}\n\\toprule\n\\textbf{Premises} & \\textbf{Condition} & \\textbf{$N_{\\text{proved}}$} & \\textbf{CE\\%} & \\textbf{TS\\%} & \\textbf{Genuine\\%} \\\\\n\\midrule\n$\\leq$3 & ISR $\\beta{=}0.1$ & 8 & 50.0 & 12.5 & 12.5 \\\\\n         & Random $\\beta{=}0.1$ & 6 & 50.0 & 0.0 & 50.0 \\\\\n\\midrule\n4--6     & ISR $\\beta{=}0.1$ & 61 & 47.5 & 19.7 & 14.8 \\\\\n         & Random $\\beta{=}0.1$ & 58 & 72.4 & 0.0 & 22.4 \\\\\n\\midrule\n$\\geq$7  & ISR $\\beta{=}0.1$ & 12 & 75.0 & 0.0 & 25.0 \\\\\n         & Random $\\beta{=}0.1$ & 15 & 86.7 & 0.0 & 13.3 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Mode composition by premise-count bin (seed 42). TS hacking is concentrated in the 4--6 premise range and absent for ${\\geq}7$ premises, indicating a mechanistic complexity threshold rather than a statistical confound.}\n\\label{tab:premise-bin-modes}\n\\end{table}\n\n\\begin{table*}[ht]\n\\centering\n\\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\\beta{=}0.1$ non-hacking rate is corrected for PG reclassification and TS false negatives (Appendix~\\ref{app:h8}).}\n\\label{tab:bootstrap-ci}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Comparison} & \\textbf{Condition} & \\textbf{Control} & \\textbf{OR} & \\textbf{$p$} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Non-hacking rate (PG+FN corrected)}} \\\\\nISR vs.\\ Random & 6.06\\% {\\scriptsize[3.6,9.9]} & 9.5\\% {\\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\\\\nISR vs.\\ Exec-only & 6.06\\% & 7.5\\% & 0.79 & 0.62 \\\\\nRandom vs.\\ Exec-only & 9.5\\% & 7.5\\% & 1.30 & 0.68 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{TS gaming rate}} \\\\\nISR vs.\\ Random & 70.6\\% {\\scriptsize[64.3,76.3]} & 13.7\\% {\\scriptsize[9.9,18.6]} & 15.05 & $1.3{\\times}10^{-39}$ \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{SFT vs.\\ Exec-only non-hacking rate}} \\\\\nSFT vs.\\ Exec-only & 92.3\\% {\\scriptsize[79.7,97.3]} & 7.5\\% & 147 & ${<}0.001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\\\[2pt]\n{\\small ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\\% Wilson CIs in brackets where shown. Pooled statistics treat within-seed samples as independent and serve as descriptive summaries only; the seed-stratified CMH test (\\S\\ref{app:statistical-details}) accounts for within-seed dependence.}\n\\end{table*}\n\n\\paragraph{TS dose-response gradient.}\nTS tautology follows a dose-response pattern across reward conditions: random $\\beta{=}0.1$ produces $13.7\\%$ TS ($36/262$ pooled; per-seed: $38.3\\%$ in s43, $0\\%$ in s42/s44), random $\\beta{=}0.3$ yields 4--7 TSa samples per seed, and ISR $\\beta{=}0.1$ reaches $70.6\\%$ ($163/231$).\nThe gradient (random $\\beta{=}0.1$ ($13.7\\%$) $\\to$ random $\\beta{=}0.3$ (4--7 TSa per seed) $\\to$ ISR $\\beta{=}0.1$ ($70.6\\%$)) shows ISR transforms TS from a seed-dependent GRPO tendency to a near-universal convergence direction.\n\n\\paragraph{Goodhart effects: implications.}\nISR was designed to \\emph{detect} reward gaming of $r_{\\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself. Any diagnostic metric risks becoming a target when optimized.\nThe dose-response pattern maps onto the Manheim \\& Garrabrant taxonomy~\\citep{manheim-goodhart-taxonomy}: $\\beta{=}0.1$ on FOLIO instantiates \\emph{regressional} Goodhart ($P{\\to}P$ tautologies yield $\\text{ISR}{\\geq}0.5$, so ISR erroneously rewards the shortcut); $\\beta{\\geq}0.2$ introduces \\emph{extremal} elements (PR collapse to 18\\% vs.\\ 48\\% random at $\\beta{=}0.3$).\nThe implication is conditional: ISR fails as a training reward when hacking satisfies its LOO structure (FOLIO), but produces beneficial instability when hacking does not (ProofFOL; \\S\\ref{sec:crossdomain}).\n\n\\paragraph{Single-seed unreliability.}\nThe three exec-only seeds diverge radically (PR $\\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\\S\\ref{sec:diagnostic}).\nISR $\\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (TS), 1/3 by premise minimization (\\S\\ref{sec:goodhart}).\nMulti-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.\n\n\\paragraph{Classifier limitations.}\nText-match hacking classifiers have systematic blind spots that functional analysis exposes.\nIn Prolog STA, two seeds achieved 100\\% genuine classification under strict text matching, yet functional analysis via the $n_{\\text{necessary}}$ distribution revealed 0\\% genuine in both cases (Table~\\ref{tab:prolog-detailed}).\nOne seed produces uppercase pseudo-Prolog that is functionally tautological; the other converts conclusions to snake\\_case atoms serving as both fact and query, a gaming mode invisible to string comparison.\nPractitioners should cross-validate text-match classifiers with functional metrics and never treat classifier-reported genuine rates as ground truth without independent verification.\n\n\\paragraph{Practical guidelines.}\n\\label{app:practical-guidelines}\nOur findings yield five guidelines for GRPO-trained neurosymbolic systems:\n(1)~Never evaluate by prove rate alone; use ISR and component count as joint diagnostics.\n(2)~Report multi-seed results: single-seed GRPO evaluation is unreliable, as cross-seed variance can exceed the effect size of interest (\\S\\ref{sec:diagnostic}).\n(3)~Use ISR for post-hoc diagnosis only, not as a training signal; any dose induces gaming or collapse.\n(4)~Treat LOO-based metrics as component-count-biased until normalized.\n(5)~Expect conclusion embedding as a GRPO-universal baseline (Table~\\ref{tab:goodhart-landscape}): reward shaping alters hacking composition, not prevalence.\n\n\\paragraph{Multiple testing correction.}\n\\label{app:statistical-details}\nWe define two test families: FOLIO ($k{=}14$ tests across all conditions) and ProofFOL ($k{=}1$).\nWithin the FOLIO family, Bonferroni correction at $\\alpha{=}0.05$ yields adjusted thresholds of $p_{\\text{adj}}{=}0.05/14{=}0.0036$.\nThree primary comparisons survive correction: the TS rate difference (ISR vs.\\ random; $p_{\\text{bonf}}{=}1.82{\\times}10^{-38}$), the SFT vs.\\ exec-only non-hacking rate ($p_{\\text{bonf}}{=}0.014$), and the Cochran--Mantel--Haenszel test for TS association across seeds ($p_{\\text{bonf}}{<}10^{-8}$).\nThe matched 5+5-seed Fisher/Mann-Whitney comparison is borderline ($p_{\\text{bonf}}{=}0.056$), significant at $\\alpha{=}0.10$ after Bonferroni correction ($k{=}14$).\nThe ProofFOL genuine-rate permutation test ($p{=}0.10$) belongs to a separate hypothesis family (different dataset, independent experimental design) and does not reach significance even without correction; it is reported as an exploratory observation throughout.\nBonferroni assumes independence, which is conservative for our setting (several tests use overlapping data); Holm--Bonferroni or Benjamini--Hochberg FDR would recover the matched 5+5 comparison at conventional significance.\nWe report the most conservative Bonferroni results for transparency.\n\n\\paragraph{Mode distribution $\\chi^2$ test.}\nA pooled $3{\\times}2$ contingency table (TS/CE/N-H $\\times$ ISR/Random, 3-seed, 500 steps) yields $\\chi^2{=}174.8$, $\\text{df}{=}2$, $p{=}1.08{\\times}10^{-38}$, confirming that ISR reward shifts the overall hacking mode composition, not merely the TS rate.\nPer-seed tests are individually significant (s42: $\\chi^2{=}15.8$, $p{<}0.001$; s43: $\\chi^2{=}59.4$, $p{<}10^{-13}$; s44: $\\chi^2{=}168.0$, $p{<}10^{-36}$).\nThe previously reported $\\text{OR}_{\\text{CMH}}{=}2.46$ for TS specifically ($p{<}10^{-8}$) captures a narrower slice of this distributional shift.\n\n\n\\section{Hacking Mode Definitions}\n\\label{app:hacking-modes}\n\nWe identify eight distinct reward hacking modes across all experiments.\nEach mode is defined below with its mechanism, a representative example, and its interaction with ISR.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nCE embed       & 87 & 18 & 68 & 8 & 0$^\\sharp$ \\\\\nTS duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\\nPG prem-subset & 5  & 5  & 8   & 0 & --- \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 1  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}). \\texttt{1k} denotes a mode observed only at the 1000-step checkpoint. CE and PG can co-occur; Table~\\ref{tab:goodhart-landscape} applies PG${>}$CE priority, reducing Random CE by ${\\sim}2$\\,pp relative to counts here.}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nTable~\\ref{tab:hacking-taxonomy} provides a compact cross-condition summary; Table~\\ref{tab:hacking-taxonomy-app} below gives the extended breakdown.\n\n\\begin{table*}[ht]\n\\centering\n\\small\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Mechanism} & \\textbf{Exec} & \\textbf{ISR} & \\textbf{Rnd} & \\textbf{SFT} \\\\\n\\midrule\nCE & Concl.\\ in premises & 87 & 18 & 68 & 8 \\\\\nTS & Single prem.\\ = concl. & $\\bullet$ & \\textbf{71} & 14$^\\dagger$ & 0 \\\\\nPG & Premise-subset gaming & 5 & 5 & 8 & 0 \\\\\nTautological & 2-comp $P{=}C$ & $\\bullet$ & 0 & 0 & 0 \\\\\nRepetition & Output degen. & $\\bullet$ & --- & --- & --- \\\\\nContradiction & $n_{\\text{comp}}$ inflated & $\\bullet$ & --- & --- & --- \\\\\nC-w/o-utility & Complex, redundant & 0 & 0 & 1 & 0 \\\\\nQ-as-fact & Atom = fact+query & --- & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta{=}0.1$ 3-seed pooled. TS includes subtypes TSa (text-match, $n{=}149$ ISR $+$ 36 random) and TSb (obfuscated tautology, $n{=}14$; primarily s44). $^\\dagger$Random TS driven by seed~43 (38.3\\%); seeds~42/44: 0\\%. Exec: CE${=}87$\\% in s42; $\\bullet$ marks seed- or step-specific modes (TS/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). PG: premise-subset gaming (Appendix~\\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref{tab:prolog-detailed}).}\n\\label{tab:hacking-taxonomy-app}\n\\end{table*}\n\n\\paragraph{Classifier Validation.}\nHacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.\nCE and TS are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA (leave-one-out ablation).\nNo training data or manual annotation is used for classification.\n\nTo estimate precision, we manually verified 50 randomly sampled outputs classified as CE or TS: all 50 were confirmed correct (estimated precision ${>}$95\\%, Wilson 95\\% CI: [93\\%, 100\\%]).\nRecall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.\nWe cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\\text{necessary}} \\leq 1$ are flagged as potential false negatives.\nThis cross-validation revealed query-as-fact gaming in Prolog (\\S\\ref{app:hacking-modes}), where the strict text classifier reported 100\\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\\text{necessary}}{=}1$).\nThe non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.\n\\paragraph{Boundary case validation.}\nStratified validation across 82 samples (all five hacking categories) yields Cohen's $\\kappa{=}1.0$; independent re-annotation confirms full agreement.\nStructured inspection of 20 boundary cases (short-conclusion CE (10, minimum 4 characters), low-ISR genuine (5, minimum $\\text{ISR}{=}0.22$), and TS on false propositions (5)) confirmed 20/20 correct classifications.\nShort-conclusion CE samples are unambiguous hacking: the conclusion appears as a standalone premise with no NL source.\nLow-ISR genuine samples reflect mode-collapsed template outputs, not structural gaming.\n3/5 TS boundary cases confirm factually false propositions (e.g., affirming ``dogs are plants''), showing TS is not merely vacuous but actively harmful.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lcr@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Val.\\ $N$} & \\textbf{Prec.} \\\\\n\\midrule\nCE (Concl.\\ Embed.) & 80$^\\dagger$ & 1.00 \\\\\nTS (Tautological) & 7 & 1.00 \\\\\nPG (Premise-Subset) & 20 & 1.00 \\\\\nContradiction & 20 & 1.00 \\\\\nGenuine & 25 & 1.00 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{152} & \\textbf{1.00} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-mode classifier precision on 152 manually validated samples (stratified + boundary + random; three exercises pooled). $^\\dagger$Includes 50 randomly sampled CE$\\cup$TS outputs (pool ratio CE:TS${=}$374:2). Recall is not estimable from a validation-only design.}\n\\label{tab:classifier-precision}\n\\end{table}\n\nThe TS\\textsubscript{b} subcategory (functional LOO tautologies undetectable by text matching) provides a lower bound on TS recall: ${\\geq}91\\%$ ($149/163$) under ISR $\\beta{=}0.1$. Other modes' recall is not estimable from the validation-only design; non-hacking rates throughout should be interpreted as upper bounds.\n\n\\subsection{PG -- Premise-Subset Gaming}\n\\label{app:h8}\n\nManual audit of ISR $\\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (CE-style).\nWe term this \\textbf{PG (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.\n\n\\paragraph{Detection.} PG is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\\text{prem}} \\leq 3$) that nonetheless achieve high ISR.\nAutomated detection is not currently feasible because PG requires comparing the generated premise set against the gold premises.\n\n\\paragraph{Audit scope and limitations.}\nFull PG audit was completed for ISR $\\beta{=}0.1$ seed~42 only.\nISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated.\nRandom $\\beta{=}0.1$ does not produce PG by mechanism (no ISR optimization pressure); seed~42 audit confirmed PG${=}0$.\n\n\\paragraph{TS false-negative correction (TSb obfuscated tautology).}\nISR $\\beta{=}0.1$ seed~44 contained 12 samples with $n_{\\text{prem}}{=}1$ classified as non-hacking by the text matcher.\nManual inspection confirmed all 12 are logically equivalent to TS but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).\nWe classify these as \\textbf{TSb} (obfuscated tautology), distinct from text-match-detectable TSa.\n$10/12$ achieve $\\text{ISR}{\\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and TS classifier: triple gaming (\\S\\ref{sec:taxonomy}).\nAfter correction, ISR s44 non-hacking${=}0$; total TS = TSa (77 text-match) + TSb (12 obfuscated) = 89.\n\n\\paragraph{Impact on non-hacking-rate comparison.}\nAfter PG reclassification and TS false-negative correction: ISR non-hacking $= 14/231 = 6.06\\%$ vs.\\ random non-hacking $= 25/262 = 9.5\\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\\% CI: ISR [3.6\\%, 9.9\\%], Random [6.5\\%, 13.7\\%]).\nThe direction is consistent with ISR-amplified gaming modes (TS, PG) displacing non-hacking output, but the effect is not statistically significant at the conventional $\\alpha{=}0.05$ threshold.\n\n\\subsection{CE -- Conclusion Embedding}\n\n\\paragraph{Definition.}\nThe conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.\nThe solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x (bird(x) -> flies(x)).\n  bird(tweety).\n  flies(tweety).  % conclusion embedded\nConclusion: flies(tweety).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nVariable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.\nISR does not distinguish trivial from substantive necessity.\n\n\\paragraph{Prevalence.}\nConclusion embedding in some form (CE multi-premise or TS single-premise) is GRPO-universal at 68--97\\% across all RL conditions.\nUnder exec-only and Random reward, it manifests as CE (69--93\\%); under ISR reward, it shifts to TS (70.6\\% pooled).\n\n\n\\subsection{TSa -- Conclusion Duplication (Standard)}\n\n\\paragraph{Definition.}\nThe entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.\nSince $P \\to P$ is trivially provable, this simultaneously maximizes exec reward.\nBecause the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.8$--$1.0$.\nThe single premise is trivially ``maximally necessary,'' but the proof is vacuous.\nTSa games both exec reward and ISR reward; TSb extends this to triple gaming by additionally evading the text-match classifier.\n\n\\paragraph{Prevalence.}\nTSa (text-match detectable): 64.5\\% pooled (149/231) under ISR~$\\beta{=}0.1$ (s42: 16.0\\%, s43: 96.7\\%, s44: 86.5\\%).\nCombined TS (TSa + TSb): 70.6\\% (163/231; s43 TSa${=}59$ + TSb${=}2$; includes s44 FN correction).\nRandom~$\\beta{=}0.1$ pooled: 13.7\\% (36/262, all TSa; driven by seed~43 at 38.3\\%, seeds~42 and~44 at 0\\%).\n\n\n\\subsection{TSb -- Obfuscated Tautology}\n\n\\paragraph{Definition.}\nA single-premise formalization logically equivalent to TSa (premise = conclusion) but with surface-form differences that evade the text-match TS classifier.\nThe model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).\n\n\\paragraph{Example (FOL, vacuous quantifier wrapping).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y ((A(x)&B(y))->(C(x)|D(y))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\noindent The premise introduces a vacuous variable $y$, unified with~$x$ at proof time; the formulas are logically equivalent but textually distinct.\n\n\\paragraph{ISR interaction.}\n$\\text{ISR}{\\geq}0.83$ ($10/12$ samples).\nTSb simultaneously games three objectives: execution reward ($r_{\\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match TS classifier (surface-form difference evades detection).\nThis triple gaming makes TSb the most complete Goodhart case we observe.\n\n\\paragraph{Prevalence.}\nFound primarily in ISR $\\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as non-hacking); seed~43 contributes $2$ additional cases.\nFunctional cross-validation via $n_{\\text{necessary}}{=}1$ exposed the misclassification.\n\n\n\\subsection{Tautological Collapse}\n\n\\paragraph{Definition.}\nTwo-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \\to P$ tautology with minimal token cost.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n\\begin{verbatim}\nPremises: p(a).\nConclusion: p(a).\n\\end{verbatim}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$=1.0$ (the sole premise is necessary).\nDistinguished from TS by having low component count ($n_{\\text{comp}}\\approx 2$) and atomic formulas rather than complex sub-structured conclusions.\n\n\\paragraph{Prevalence.}\nDominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\\text{comp}}=2.04$, 100\\% TS by strict classifier).\nAlso observed in Prolog exec+STA seed~42 (100\\% TS, PR~$=0.50$).\n\n\n\\subsection{Repetition Collapse}\n\n\\paragraph{Definition.}\nThe model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.\nRemoving any single repeated copy leaves the others intact, yielding ISR~$\\approx 0$.\n\n\\paragraph{Example (Prolog).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n\\begin{verbatim}\npenguin(fido).\npenguin(fido).\npenguin(fido).\n... (repeated to 512 tokens)\nquery(penguin(fido)).\n\\end{verbatim}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$. Each copy is individually redundant since identical copies remain after removal.\nISR correctly diagnoses this degeneration.\n\n\\paragraph{Prevalence.}\nObserved in FOL exec-only seed~43 (87\\% of outputs hit max completion length; PR~$=13$\\%, ISR~$=0$).\n\n\n\\subsection{Complexity-without-Utility}\n\n\\paragraph{Definition.}\nThe formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous: none individually necessary for the proof.\nThe complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y (R(x,y) ->\n    exists z (S(x,z) & T(z,y))).\n  all x (P(x) -> Q(x)).\n  P(a).            % only this needed\nConclusion: Q(a).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.\nThis is the mode ISR is best calibrated for.\n\n\\paragraph{Prevalence.}\nLow. Observed in Random~$\\beta{=}0.1$ seed~42 at 3.8\\% (3/79).\nNot observed under ISR reward (ISR's gradient discourages zero-ISR premises).\n\n\n\\subsection{Contradiction Explosion}\n\n\\paragraph{Definition.}\nThe component count grows unboundedly over training.\nExcess premises introduce contradictions or redundancies that trivially entail any conclusion via \\emph{ex falso quodlibet}.\nIndividual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.\n\n\\paragraph{Example (FOL, 1000-step exec-only).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  c1. c2. c3. ... c18. % 18.55 mean\n  % conclusion embedded among premises\nConclusion: Q(a).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\\% of proved samples having ISR~$=0$).\n\n\\paragraph{Prevalence.}\nObserved in extended exec-only training (seed~42, 1000 steps).\nMean component count grows from ${\\sim}6$ (500 steps) to 18.55 (1000 steps).\n\n\n\\subsection{Query-as-Fact Gaming}\n\n\\paragraph{Definition.}\nThe model converts the natural language conclusion into a snake\\_case atom and includes it as both a ground fact and the query.\nProlog trivially proves the query by unifying with the fact.\nThis mode evades text-match classifiers designed for CE/TS because the generated atom bears no surface resemblance to the original conclusion text.\n\n\\paragraph{Example (Prolog).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n\\begin{verbatim}\n% NL: \"Fido is happy.\"\n% Model output:\nfido_is_happy.\n:- fido_is_happy.     % query = fact\n\\end{verbatim}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.9$--$1.0$.\nThe single fact is trivially necessary (its removal breaks the query), inflating ISR.\nFunctionally equivalent to TS but with a distinct surface mechanism.\n\n\\paragraph{Prevalence.}\nObserved in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).\n95/97 proved samples have $n_{\\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\\% non-hacking.\n\n\n\\section{Per-Seed Detailed Results}\n\\label{app:detailed-results}\n\nTables~\\ref{tab:fol-beta01-detailed} and \\ref{tab:prolog-detailed} report full per-seed results.\nAll metrics are computed by \\texttt{eval\\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.\nISR values are proved-only ISR$^*$.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\\beta{=}0.1$ breakdown referenced from Table~\\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\\ = percentage among proved samples. ``---'' indicates data not available. $^\\dagger$s43 uses sampling eval ($T{=}0.7$). $^\\ddagger$Three s44-1000 samples escape text-match heuristics (CE/PG classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass PG detection and commuted premises that bypass CE detection; reclassified as degenerate. $^\\diamond$Seeds 45--46 added post-hoc under identical hyperparameters (effective batch size 8; micro-batch decomposition differs: $4{\\times}2$ vs.\\ $2{\\times}4$, mathematically equivalent).}\n\\label{tab:fol-detailed}\n\\label{tab:fol-beta01-detailed}\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\textwidth}{!}{%\n\\begin{tabular}{@{}llccccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{Steps} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Baselines}} \\\\\nBase model (no training)\n  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\\\\nGround-truth FOL\n  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\\\\nSFT\n  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \\textbf{92.3} & Supervised, no RL \\\\\n  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \\textbf{90.9} & \\\\\n  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \\textbf{93.3} & \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed pooled} & $0.130$ & $0.595$ & $0$ & $7.8$ & \\textbf{92.3} & $n{=}39$ proved \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 100 & 0.32 & \\textbf{0.642} & --- & --- & --- & Early checkpoint \\\\\n  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & PG${=}5.4\\%$ \\\\\n  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\\\\n  & 43 & 500 & 0.13 & 0$^\\dagger$ & --- & --- & --- & $^\\dagger$Greedy ($n_{\\text{proved}}{=}13$) \\\\\n  & 43 & 1000 & 0.96 & 0.082 & 0 & 93.8 & 6.2 & CE dominant \\\\\n  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\\\\n  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\\ddagger$ & PG${=}15\\%$ \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.68{\\pm}0.47$ & $0.238{\\pm}0.30$ & & & & 500-step \\\\\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.97{\\pm}0.02$ & $0.029{\\pm}0.05$ & & & $2.1{\\pm}3.6$ & 1000-step \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \\textbf{17.3} & Mixed CE+TS+PG \\\\\n  & 42 & 1000 & 0.90 & 0.877 & 96.7 & 0 & 2.2 & TS collapse; PG${=}1$ ($n{=}90$) \\\\\n  & 43 & 500 & 0.61 & 0.830 & \\textbf{100} & 0 & 0 & TSa${=}59$, TSb${=}2$ \\\\\n  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & TS dominant (FN corrected) \\\\\n  & 45$^\\diamond$ & 500 & 0.42 & 0.605 & 38.1 & 4.8 & \\textbf{54.8} & PG${=}1$; $n{=}42$ \\\\\n  & 46$^\\diamond$ & 500 & 0.77 & 0.411 & 14.3 & 26.0 & \\textbf{54.5} & PG${=}4$; $n{=}77$ \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.77{\\pm}0.14$ & $0.716{\\pm}0.26$ & & & & 500-step (s42--44) \\\\\n  & \\multicolumn{2}{l}{5-seed mean$\\pm$std} & $0.70{\\pm}0.19$ & $0.633{\\pm}0.23$ & & & & 500-step (s42--46) \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & \\multicolumn{8}{l}{See Table~\\ref{tab:beta03-detailed} for per-seed $\\beta{=}0.3$ results.} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & PG${=}4$ \\\\\n  & 43 & 500 & 0.94 & 0.150 & \\textbf{38.3} & 59.6 & 1.1 & TSa${=}36$; PG${=}1$ \\\\\n  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & PG${=}16$ (CE$\\cap$PG: 6) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.87{\\pm}0.08$ & $0.117{\\pm}0.042$ & & & & TS seed-dep.: 0/38/0\\% \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ (D086); $n_{\\text{comp}} = 9.6$ \\\\\n  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\\text{N-H}}{=}3$ \\\\\n  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.54{\\pm}0.35$ & $0.09{\\pm}0.09$ & & & & \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Shuffled-ISR $\\beta{=}0.1$ (deconfounding control)}} \\\\\n  & 42 & 500 & 0.15 & 0.567 & 6.7 & 6.7 & \\textbf{86.7} & $n{=}15$ proved \\\\\n  & 43 & 500 & 0.16 & 0.568 & 6.3 & 6.3 & \\textbf{87.5} & $n{=}16$ proved \\\\\n  & 44 & 500 & 0.15 & 0.542 & 6.7 & 6.7 & \\textbf{86.7} & $n{=}15$ proved \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.153{\\pm}0.006$ & $0.559{\\pm}0.015$ & $6.5$ & $6.5$ & \\textbf{87.0} & $N{=}46$ proved \\\\\n\\bottomrule\n\\end{tabular}}% end resizebox\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\\ = percentage among proved samples.  ``---'' indicates data not available.}\n\\label{tab:prolog-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\\\\n  & 43 & 0.56 & 0.015 & --- & --- & --- & \\\\\n  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.53{\\pm}0.31$ & $0.146{\\pm}0.21$ & & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec+ISR (STA reward)}} \\\\\n  & 42 & 0.50 & 1.000 & \\textbf{100} & 0 & 0 & TS tautological \\\\\n  & 43 & 0.38 & 0.185 & 0$^\\ddagger$ & 97.4 & 0 & $^\\ddagger$Functional TS$^a$ \\\\\n  & 44 & 0.97 & 0.912 & 0$^\\ddagger$ & 0 & 0$^\\ddagger$ & Query-as-fact gaming$^b$ \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.62{\\pm}0.31$ & $0.699{\\pm}0.45$ & & & 3/3 Goodhart, 0\\% non-hacking \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\small\n$^a$ Strict TS classifier reports 0\\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\\\\n$^b$ Strict classifier reports Non-hacking$\\,{=}\\,100$\\%, but 95/97 proved samples have $n_{\\text{necessary}}=1$. The model converts NL to snake\\_case atoms serving as both fact and query, a third distinct Goodhart pathway.\\\\\n$^\\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.\n}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: ProofFOL (Prover9). PR$_{\\text{f50}}$ = mean prove rate over final 50 steps. TS = tautological shortcutting (\\S\\ref{sec:taxonomy}), CE = conclusion embedding, Genuine = classified as neither TS nor CE. Stable convergence: PR$_{\\text{f50}}{>}0.90$.}\n\\label{tab:prooffol-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR$_{\\text{f50}}$} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{Genuine\\%} & \\textbf{Notes} \\\\\n\\midrule\nBase & --- & 0.16 & 0.310 & 0 & 0 & \\textbf{100} & $n{=}16$ proved \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & ${\\approx}$1.0 & 0.066 & \\textbf{100} & 0 & 0 & $n{=}99$; stable \\\\\n  & 43 & 0.55 & 0.119 & 0 & 49.2 & 50.8 & $n{=}63$; partial \\\\\n  & 44 & ${\\approx}$1.0 & 0.043 & 0 & 98.6 & 1.4 & $n{=}72$; stable \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{Aggregate} & & \\multicolumn{3}{c}{17.4\\% genuine (mean of seeds)} & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 0.35 & 0.12 & 0 & 0 & \\textbf{100} & $n{=}46$; collapsed \\\\\n  & 43 & ${\\approx}$0.47 & ${\\approx}$0.13 & 0 & 69.6 & 30.4 & $n{=}56$; unstable \\\\\n  & 44 & 0.49 & 0.145 & 0 & 0 & \\textbf{100} & $n{=}66$; oscillation \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{Aggregate} & & \\multicolumn{3}{c}{\\textbf{76.8\\%} genuine (mean of seeds)} & \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\small Aggregate genuine rate: mean of per-seed genuine rates. Permutation test (exec vs.\\ ISR genuine): $p{=}0.10$, $N{=}3$ per group.}\n\\end{table*}\n\n\\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}\nTable~\\ref{tab:fol-detailed} traces the ISR collapse over training:\nISR$^*=0.642$ at 100 steps $\\to$ $0.132$ at 500 steps ($-79.4$\\%) $\\to$ $0.003$ at 1000 steps ($-99.5$\\% from step 100).\nPR increases monotonically ($0.32 \\to 0.93 \\to 0.96$) while component necessity collapses, confirming that ISR flags degeneration invisible to execution reward.\nBy step 1000, 94.8\\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.\n\n\\paragraph{Prolog: universal Goodhart via three distinct pathways.}\nAll three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\\% non-hacking proofs (Figure~\\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:\nseed~42 produces clean TS tautologies (single premise~$=$~conclusion),\nseed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,\nand seed~44 converts NL conclusions to snake\\_case atoms used as both fact and query.\nThe diversity of gaming pathways across seeds (despite identical training data and reward function) demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.\n\n\\subsection{Per-Seed Results at $\\beta{=}0.2$ and $\\beta{=}0.3$}\n\\label{app:beta03}\n\nTable~\\ref{tab:beta03-detailed} reports per-seed results for ISR at $\\beta{=}0.2$ and both ISR and Random at $\\beta{=}0.3$.\nAt $\\beta{=}0.2$, all three seeds converge to pure TS Goodhart (100\\% or near-100\\% TS), confirming $\\beta{\\geq}0.2$ as the extremal Goodhart regime.\nThe three ISR $\\beta{=}0.3$ seeds illustrate qualitatively distinct Goodhart pathways (\\S\\ref{sec:goodhart}).\n\n\\begin{table*}[ht]\n\\centering\n\\caption{Per-seed results at $\\beta{=}0.2$ and $\\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H = percentage among proved samples.}\n\\label{tab:beta03-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.2$}} \\\\\n  & 42 & 1.00 & 0.602 & \\textbf{100} & 0 & 0 & Pure TS ($n{=}100$) \\\\\n  & 43 & 0.96 & 0.552 & \\textbf{96.9} & 1.0 & 0 & PG${=}2$ \\\\\n  & 44 & 0.94 & 0.964 & \\textbf{100} & 0 & 0 & Pure TS ($n{=}94$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.97{\\pm}0.03$ & $0.71{\\pm}0.22$ & & & 3/3 TS Goodhart \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); PG${=}3$ \\\\\n  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 23.3 & CE shortcutting \\\\\n  & 44 & 0.95 & 0.742 & \\textbf{100} & 0 & 0 & Pure TS Goodhart \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.66{\\pm}0.42$ & $0.39{\\pm}0.31$ & & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ (D086) \\\\\n  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\\text{N-H}}{=}3$ \\\\\n  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.54{\\pm}0.35$ & $0.09{\\pm}0.09$ & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\FloatBarrier\n\n\\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}\n\\label{app:100step}\n\nTo control for the prove-rate confound in our SFT comparison (\\S\\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\\%, higher than SFT (13.0\\%, 3-seed pooled) but still early in training.\nOf the 32 proved samples, 9 (28.1\\%) exhibit TS hacking (single premise identical to conclusion) and 1 (3.1\\%) exhibits CE (conclusion embedded among premises), yielding a total hacking rate of 31.2\\%.\nBy contrast, SFT at comparable or lower PR shows 7.7\\% hacking (1/13 proved samples).\nThis demonstrates that reward hacking emerges early in GRPO training, well before the prove-rate plateau, and is not simply an artifact of having more proved samples available for exploitation.\nThe 100-step hacking rate (31.2\\%) is already substantially above SFT (7.7\\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.\n\n\\subsection{$O(1)$ vs.\\ $O(n)$ ISR Ablation}\n\\label{app:o1-ablation}\n\nAll main experiments (\\S\\ref{sec:diagnostic}--\\ref{sec:crossdomain}) use $O(n)$ full LOO ISR during both training and evaluation; the $O(1)$ binary variant described below exists as an alternative implementation (\\texttt{execution\\_fast\\_sta}) but is used only in the ablation reported here.\nThe two signals measure fundamentally different properties, not approximations of the same quantity.\nThe binary signal tests \\emph{collective} premise necessity: $\\text{fast\\_ISR}(x) = 1$ if $x$ is proved and the conclusion is not provable under empty premises (tautology check), $0$ otherwise.\nLOO tests \\emph{individual} premise necessity: each component is removed in turn, and ISR reflects the fraction whose removal causes proof failure.\n\n\\paragraph{Evaluation-time comparison.}\nAcross 402 proved samples from all ProofFOL conditions, the $O(1)$ binary signal is 1.0 for every sample: non-tautological conclusions cannot be proved without any premises, so the collective necessity test is trivially satisfied.\nThis renders $O(1)$ unable to distinguish hacking from genuine formalizations: both pass the empty-premise check.\nBy contrast, $O(n)$ LOO produces a clear separation: exec-only models average $\\text{ISR}^*{=}0.046$ ($n{=}234$) while ISR-trained models average $\\text{ISR}^*{=}0.183$ ($n{=}168$), because hacking constructions contain individually redundant components that LOO detects.\nOf 179 disagreements between the two signals, all are false positives ($O(1){=}1$, LOO${=}0$): the binary check approves formalizations that LOO correctly identifies as structurally degenerate.\n\n\\paragraph{Training-time ablation.}\nAs a training reward ($r = 0.5\\,r_{\\text{exec}} + 0.5\\,\\text{fast\\_ISR}$, seed~42, 500 steps), the $O(1)$ variant achieves $\\text{PR}{=}63\\%$ with $\\text{ISR}^*{=}0.007$, functionally zero, compared to $\\text{ISR}^*{=}0.132$ under exec-only and $\\text{ISR}^*{=}0.42$ under $O(n)$ ISR $\\beta{=}0.1$.\nThe tautology check depresses prove rate by 30\\,pp relative to exec-only ($63\\%$ vs.\\ $93\\%$) by penalizing formalizations where the conclusion is provable without premises, but this constraint provides no gradient toward individual component necessity; the model is free to degenerate as long as it avoids trivial tautologies.\nThat even the fine-grained $O(n)$ LOO signal, which \\emph{does} provide per-component necessity feedback, is ultimately gamed (\\S\\ref{sec:goodhart}) underscores that the problem lies in reward optimization itself, not in signal granularity.\n\n\\paragraph{Computational overhead.}\nFull LOO requires $n{+}1$ solver calls per sample (mean $n{\\approx}6$ for FOLIO).\nWith Prover9 at ${\\sim}5$\\,ms per call, STA evaluation adds ${\\sim}55$\\,ms per sample versus ${\\sim}4$\\,s for LLM inference (${<}1\\%$ overhead).\nThe $O(1)$ binary check adds a single solver call per proved sample (${<}2\\%$ per training step), but the evaluation above shows this saving comes at the cost of all diagnostic power.\n\n\\subsection{Cross-Model Generalization: LLaMA-3.2-3B Cold-Start Failure}\n\\label{app:llama-coldstart}\n\nWe applied the identical GRPO configuration (Table~\\ref{tab:hyperparams}) to LLaMA-3.2-3B~\\citep{grattafiori2024llama} (3B; exec-only, seed~42, $K{=}4$, FOLIO).\nAcross 72 of 500 planned steps the model produced zero valid Prover9 output, generating only natural-language text; $r_{\\text{exec}}{=}0$ for all rollouts yields zero GRPO advantage, so training was terminated early.\\footnote{This run was also affected by a generation-termination configuration issue (dual EOS tokens); the zero prove rate reflects both the base model's lack of FOL generation capability and truncated outputs.}\nThis establishes a \\emph{capability threshold}: the base model must produce syntactically valid solver input for the RL loop to generate signal.\nQwen3-4B crosses this threshold (non-zero prove rates within 10 steps) while LLaMA-3.2-3B does not despite comparable size (3B vs.\\ 4B), likely reflecting pretraining data composition.\nAn SFT warmstart (3 epochs on gold formalizations, lr$=$2$\\times$10$^{-5}$) achieves $\\text{PR}{=}16\\%$ ($n{=}100$) after correcting the generation-termination issue.\nHowever, the model produces Unicode FOL notation ($\\forall$, $\\to$, $\\wedge$) instead of the required ASCII syntax despite training on ASCII-formatted data; the 16\\% prove rate reflects Prover9's partial Unicode tolerance rather than correct format adherence.\nSubsequent GRPO runs (exec-only, 500 steps from SFT warmstart, 3 seeds) fail to improve beyond SFT baseline ($\\text{PR}{=}15.0{\\pm}1.0\\%$, $n{=}14$--$16$ proved per seed), yet produce no structural degeneration: $86.6{\\pm}0.9\\%$ of proved samples are genuine across seeds, with cross-seed variance near zero ($\\sigma_{\\text{PR}}{=}1$\\,pp).\nThis contrasts sharply with Qwen3-4B, where GRPO reaches $93\\%$ PR but collapses to $8\\%$ genuine with high cross-seed variance.\nThe result suggests structural degeneration is a byproduct of successful RL optimization, not of the training procedure \\emph{per se}: when GRPO fails to amplify prove rate, the model retains structural integrity.\n\n\\subsection{Seed-Dependent Convergence in Exec-Only GRPO}\n\\label{app:seed-convergence}\n\nNot all exec-only seeds converge.\nOf 6 seeds tested (s42--s46, s52; s52 uses $K{=}4$, all others $K{=}8$), we observe three regimes: \\emph{converging with degeneration} (s42: $\\text{PR}{=}93\\%$, genuine${=}7.5\\%$; s44: $\\text{PR}{=}96\\%$, genuine${=}0\\%$; s46: $\\text{PR}{=}93\\%$ at 500 steps), \\emph{slow convergence with degeneration} (s43: $\\text{PR}{=}14\\%$ but $100\\%$ hacking at 500 steps), and \\emph{non-converging} (s45: $\\text{PR}{=}15\\%$, genuine${=}86.7\\%$; s52: $\\text{PR}{=}14\\%$, genuine${=}85.7\\%$).\nNon-converging seeds retain high genuine rates (85--87\\%), indicating that structural degeneration is conditional on successful RL optimization: when GRPO fails to bootstrap prove rate beyond base-model levels, the model preserves structural integrity.\nExtended training to 1000 steps for s45 confirms persistent non-convergence ($\\text{PR}{=}15\\%$, $\\text{ISR}^*{=}0.592$, genuine${=}86.7\\%$, $n{=}15$ proved); the model neither improves nor degenerates.\n\nThis parallels the LLaMA-3.2-3B finding (Appendix~\\ref{app:llama-coldstart}), where GRPO also fails to improve PR and retains structural quality.\nBoth cases support the interpretation that degeneration is a byproduct of reward optimization success, not of the training procedure per se.\n\n\\subsection{$N{=}2$ Sensitivity Analysis (Excluding Seed 43)}\n\\label{app:n2-sensitivity}\n\nSeed~43 was evaluated with sampling ($T{=}0.7$) rather than greedy decoding (\\S\\ref{app:setup}).\nTo assess whether this non-standard protocol affects qualitative conclusions, Table~\\ref{tab:n2-sensitivity} reports pooled statistics from seeds~42 and~44 only.\n\n\\begin{table}[h]\n\\centering\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{PR (\\%)} & \\textbf{ISR$^*$} & \\textbf{N-H (\\%)} \\\\\n\\midrule\nExec-only 500-step & $95.5 \\pm 3.5$ & $0.357 \\pm 0.318$ & $3.8 \\pm 5.3$ \\\\\nExec-only 1000-step & $98.0 \\pm 2.8$ & $0.003 \\pm 0.001$ & $0.0 \\pm 0.0$ \\\\\nISR $\\beta{=}0.1$ 500-step & $85.0 \\pm 5.7$ & $0.659 \\pm 0.344$ & $8.7 \\pm 12.2$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pooled statistics excluding seed~43 ($N{=}2$, seeds~42 and~44 only). Mean$\\pm$std of per-seed values. Qualitative patterns preserved: exec-only converges to ${\\leq}7.5\\%$ non-hacking; ISR $\\beta{=}0.1$ shifts composition toward TS.}\n\\label{tab:n2-sensitivity}\n\\end{table}\n\nExcluding seed~43, exec-only converges to ${\\leq}7.5\\%$ non-hacking at 500 steps and $0\\%$ at 1000 steps.\nUnder ISR $\\beta{=}0.1$, TS dominates both remaining seeds (s42: $16\\%$, s44: $100\\%$), confirming that ISR reward shifts hacking composition toward tautological shortcuts independent of the s43 evaluation anomaly.\nThe large per-seed ISR$^*$ variance ($0.357 \\pm 0.318$) reflects different degeneration modes (CE in s42 vs.\\ TS in s44), not data quality issues.\n\n\\subsection{Cross-Scale: Qwen3-8B Exec-Only GRPO}\n\\label{app:8b-results}\n\nTo test whether structural degeneration generalizes beyond 4B scale, we apply exec-only GRPO to Qwen3-8B with $K{=}8$ rollouts per prompt ($K{=}4$ produces near-identical completions at 8B scale, yielding zero GRPO advantage and no learning signal).\nTable~\\ref{tab:8b-combined} summarizes configuration differences and results.\n\n\\begin{table}[H]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n& \\textbf{Qwen3-4B} & \\textbf{Qwen3-8B} \\\\\n\\midrule\nRollouts ($K$) & 4 & 8 \\\\\nBatch size & 4 & 1 \\\\\nGradient accum. & 2 & 16 \\\\\nEffective batch & 8 & 16 \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Config} & \\textbf{PR\\%} & \\textbf{Genuine\\%} & \\textbf{Converged?} & \\textbf{Gradient} \\\\\n\\midrule\n4B $K{=}4$ s42 & 93 & 7.5 & Yes (degenerate) & Sufficient \\\\\n8B $K{=}4$ s42 & 15.5 & --- & No & Zero \\\\\n8B $K{=}8$ s42 & 14 & 92.9 & No & Partial \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-scale: Qwen3-4B vs.\\ Qwen3-8B. \\textbf{Top}: Configuration; $K{=}8$ required at 8B because $K{=}4$ produces near-identical rollouts. \\textbf{Bottom}: Results; 4B converges with degeneration, both 8B configurations fail to converge, preserving structural integrity.}\n\\label{tab:8b-combined}\n\\end{table}\n\nWe first tested $K{=}4$ (matching the 4B configuration): the 8B model produces near-identical rollouts across all four completions, yielding zero GRPO advantage throughout 500 steps and no learning signal ($\\text{PR}{=}15.5\\%$, cold-start stagnation).\nIncreasing to $K{=}8$ provides non-zero reward variance during mid-training (approximately 40--50\\% of steps between 20--370 show non-zero advantage), but this signal proves insufficient for convergence: held-out evaluation yields $\\text{PR}{=}14\\%$ ($n{=}14$ proved), $\\text{ISR}^*{=}0.573$, genuine${=}92.9\\%$ (13/14), with a single CE sample.\nCosine learning-rate decay combined with insufficient early bootstrap appears to prevent the model from escaping the low-PR regime.\n\nThis result mirrors two other non-convergence cases: (1)~the seed-dependent 4B non-convergence (s45, s52; Appendix~\\ref{app:seed-convergence}), where identical 4B configurations fail to bootstrap, and (2)~the LLaMA-3.2-3B cold-start failure (Appendix~\\ref{app:llama-coldstart}), where the base model lacks FOL generation capability entirely.\nTogether, these cases establish a convergence threshold for GRPO-driven degeneration: the structural collapse documented in \\S\\ref{sec:diagnostic} requires successful RL optimization as a prerequisite, and at 8B scale the rollout diversity bottleneck prevents this optimization from occurring under our configuration.\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \\LaTeX{}.\n    \\item \\textbf{Literature:} summarizing related papers to inform the related-work section.\n\\end{itemize}\n",
      "numLines": 881,
      "startLine": 1,
      "totalLines": 881
    }
  },
  "sourceToolAssistantUUID": "5b314621-c614-41a6-844c-9349dd2e2a29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-25T03:56:07.707Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RDGz8iX2rZhGtaeVngx5tE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5f114e1-d347-4941-affb-a875ac4f82d7",
  "isSidechain": false,
  "requestId": "req_011CbNcXvRBZU63naGCKsZi7",
  "type": "assistant",
  "uuid": "551ebc38-6fe3-48a1-9493-478e77d693d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFHmMgTqqeGcBvUcCT5LfC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12111,
      "cache_read_input_tokens": 43678,
      "output_tokens": 283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12111,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 283,
          "cache_read_input_tokens": 43678,
          "cache_creation_input_tokens": 12111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12111
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

_source line 75 · 2026-05-25T03:56:07.712Z_

<details><summary>↩ Tool result · `toolu_01RDGz8iX2rZhGtaeVngx5tE`</summary>

```text
1	%% DEPRECATED: Content transferred to conclusion.tex and appendix.tex (Extended Discussion section).
2	%% This file is NOT \input'd by main.tex.
3	%% Retained for reference only; do not re-include.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "551ebc38-6fe3-48a1-9493-478e77d693d3",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "31aee69b-5eb0-45c3-bf0c-9ffce7a346e7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/discussion.tex",
      "content": "%% DEPRECATED: Content transferred to conclusion.tex and appendix.tex (Extended Discussion section).\n%% This file is NOT \\input'd by main.tex.\n%% Retained for reference only; do not re-include.\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  },
  "sourceToolAssistantUUID": "551ebc38-6fe3-48a1-9493-478e77d693d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-25T03:56:08.396Z_

<details><summary>↩ Tool result · `toolu_017sFeKJNBahMmD6tH6jTR1M`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'solver-trace-ablation'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f79dc20b-f4c9-473a-9d11-3dbe8a91b2ca",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "12967c28-1025-40e3-89fd-fecb11350fc1",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"No paper_checklist.yaml found for 'solver-trace-ablation'.\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'solver-trace-ablation'.\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "f79dc20b-f4c9-473a-9d11-3dbe8a91b2ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-25T03:56:08.385Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017sFeKJNBahMmD6tH6jTR1M`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_checklist.yaml",
  "max_chars": 3000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31aee69b-5eb0-45c3-bf0c-9ffce7a346e7",
  "isSidechain": false,
  "requestId": "req_011CbNcXvRBZU63naGCKsZi7",
  "type": "assistant",
  "uuid": "f79dc20b-f4c9-473a-9d11-3dbe8a91b2ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFHmMgTqqeGcBvUcCT5LfC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12111,
      "cache_read_input_tokens": 43678,
      "output_tokens": 283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12111,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 283,
          "cache_read_input_tokens": 43678,
          "cache_creation_input_tokens": 12111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12111
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
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: solver-trace-ablation - 论文路径: projects/solver-trace-ablation/docs/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: Long paper (ARR) - 截止日期: 未提供，请自行调研 - **引用验证**: ❌ 未启用…",
  "leafUuid": "12967c28-1025-40e3-89fd-fecb11350fc1",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646"
}
```

---

### Runtime record

_source line 79_

```json
{
  "type": "ai-title",
  "aiTitle": "Review solver-trace-ablation paper for EMNLP 2026",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646"
}
```

---

### Assistant

_source line 80 · 2026-05-25T03:56:14.344Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the paper. Let me also check for the external review configuration and read the existing review_issues.yaml.

Let me now proceed with the review. Let me:

1. Check external review config
2. Check existing review issues
3. Then set up the reviewer team

Let me first check project config for external review settings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12967c28-1025-40e3-89fd-fecb11350fc1",
  "isSidechain": false,
  "requestId": "req_011CbNcYS29yPNyZ84yRR6Zb",
  "type": "assistant",
  "uuid": "436c391c-74b7-416d-b4f6-7b2787c01601",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sLFN1hLJe59DaRDbQza7o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23844,
      "cache_read_input_tokens": 55789,
      "output_tokens": 396,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23844,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 396,
          "cache_read_input_tokens": 55789,
          "cache_creation_input_tokens": 23844,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23844
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

_source line 81 · 2026-05-25T03:56:15.325Z_

论文已全部读完。检查外部审稿配置和现有 issue tracker。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "436c391c-74b7-416d-b4f6-7b2787c01601",
  "isSidechain": false,
  "requestId": "req_011CbNcYS29yPNyZ84yRR6Zb",
  "type": "assistant",
  "uuid": "6511f8ca-aa74-401e-8efd-cf789e7d9cdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sLFN1hLJe59DaRDbQza7o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23844,
      "cache_read_input_tokens": 55789,
      "output_tokens": 396,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23844,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 396,
          "cache_read_input_tokens": 55789,
          "cache_creation_input_tokens": 23844,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23844
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

_source line 82 · 2026-05-25T03:56:17.311Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DapxexiwrhuWSTLY9Nia6M`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6511f8ca-aa74-401e-8efd-cf789e7d9cdc",
  "isSidechain": false,
  "requestId": "req_011CbNcYS29yPNyZ84yRR6Zb",
  "type": "assistant",
  "uuid": "01063aba-e1a0-4b5f-98ca-194fd9a47800",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sLFN1hLJe59DaRDbQza7o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23844,
      "cache_read_input_tokens": 55789,
      "output_tokens": 396,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23844,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 396,
          "cache_read_input_tokens": 55789,
          "cache_creation_input_tokens": 23844,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23844
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

_source line 83 · 2026-05-25T03:56:17.370Z_

<details><summary>↩ Tool result · `toolu_01DapxexiwrhuWSTLY9Nia6M`</summary>

```text
issues:
- id: R1-W1
  summary: "统计效力严重不足：β=0.3 仅 single seed"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: "β=0.3 ISR 和 Random 各 3 seeds 已完成。"
  resolution_round: 2
- id: v22-R12-N3
  summary: "Premise-count confound 使 ISR scalar 诊断价值严重削弱"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 22
  last_seen_round: 34
  resolution: "Compositional narrative + screening trigger 定位。method.tex L54 显式定位 ISR 为 screening trigger。"
  resolution_round: 34
- id: v22-R12-N1
  summary: "ISR vs Random non-hacking rate p=0.182 不显著"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 22
  last_seen_round: 33
  resolution: "Compositional Goodhart reframed. χ² as primary evidence."
  resolution_round: 33
- id: v17-R12-W1
  summary: "单模型 (Qwen3-4B) 无法支撑通用性声明"
  category: experiment
  severity: critical
  status: wont_fix
  first_raised_round: 17
  last_seen_round: 33
  resolution: "结构性限制。Claims scoped to Qwen3-4B."
- id: v27-R1-N2
  summary: "CMH pseudo-replication：within-seed samples 非独立"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 27
  last_seen_round: 34
  resolution: "Table 5 caption 增加 descriptive-only 限定 + CMH 引用。"
  resolution_round: 34
- id: v17-R1-W9
  summary: "Seed 43 使用 T=0.7 sampling 评估而非 greedy"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 17
  last_seen_round: 34
  resolution: "正文 N=2 统计句（experiments.tex L65）+ Appendix D.6。复发×3 后从 footnote 升级到正文。"
  resolution_round: 34
- id: v22-R2-N1
  summary: "方法论新颖性不足——LOO 是标准技术"
  category: framing
  severity: warning
  status: wont_fix
  first_raised_round: 22
  last_seen_round: 34
  resolution: "结构性 framing 问题。贡献在组合应用。"
- id: v29-R2-W5
  summary: "'Observe-vs-optimize asymmetry' 非新概念"
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 29
  last_seen_round: 34
  resolution: "Reframed as empirical instantiation of Goodhart's Law."
  resolution_round: 31
- id: v30-R1-W1
  summary: "SFT baseline selection bias"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 30
  last_seen_round: 32
  resolution: "SFT positioned as pre-RL temporal reference."
  resolution_round: 31
- id: v22-R1-W4
  summary: "Shuffled-ISR control N=46 统计效力有限"
  category: experiment
  severity: warning
  status: wont_fix
  first_raised_round: 22
  last_seen_round: 31
  resolution: "Positioned as corroborating rather than definitive."
- id: v27-R2-W4
  summary: "Hacking taxonomy recall 未评估"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 27
  last_seen_round: 34
  resolution: "Limitations 增加 recall 自约束论证：precision=100% + measured N-H=6% 约束 recall ≥94%。复发×3 后用数学论证彻底解决。"
  resolution_round: 34
- id: v19-R12-W3
  summary: "ProofFOL p=0.10 被过度引用"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 19
  last_seen_round: 34
  resolution: "C3 降级 establishing→confirming(Prolog)+exploratory(ProofFOL)。Abstract/Conclusion 同步。"
  resolution_round: 34
- id: v30-R2-W3
  summary: "ISR 与 NLI accuracy 不相关限制 actionability"
  category: method
  severity: warning
  status: resolved
  first_raised_round: 30
  last_seen_round: 33
  resolution: "'reasoning quality' → 'formalization integrity'."
  resolution_round: 32
- id: v33-N2-BIMODAL
  summary: "5-seed 双峰弱化 Goodhart 核心叙事"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 33
  last_seen_round: 33
  resolution: "C2 changed to 'seed-dependent Goodhart effect'."
  resolution_round: 33
- id: v33-W1-EXEC-POOLING
  summary: "Table 1 exec-only 仅报告 s42"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 33
  last_seen_round: 33
  resolution: "§4.2 explains. Table 1 footnote expanded."
  resolution_round: 33
- id: v33-M8-CONVERTS
  summary: "'ISR converts CE into TS' 不准确"
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 33
  last_seen_round: 33
  resolution: "'converts' → 'systematically selects for TS over CE'."
  resolution_round: 33
- id: v33-W3-TAXONOMY
  summary: "Taxonomy 互斥性和 N-H upper bound 未在正文说明"
  category: method
  severity: warning
  status: resolved
  first_raised_round: 33
  last_seen_round: 33
  resolution: "Priority rule and N-H upper bound added to §3.3."
  resolution_round: 33
- id: v31-R2-MR-SPECGAMING
  summary: "缺失引用：Nishimura et al. 2026 spec gaming"
  category: writing
  severity: info
  status: resolved
  first_raised_round: 31
  last_seen_round: 31
  resolution: "Citation added."
  resolution_round: 31
- id: v31-R2-W-TITLE-LENGTH
  summary: "标题过长"
  category: writing
  severity: info
  status: resolved
  first_raised_round: 31
  last_seen_round: 32
  resolution: "Title shortened."
  resolution_round: 32
- id: v31-R2-M-ISR0-AMBIGUITY
  summary: "ISR=0 语义不同"
  category: method
  severity: info
  status: resolved
  first_raised_round: 31
  last_seen_round: 31
  resolution: "ISR=0 disambiguation added."
  resolution_round: 31
- id: v32-R12-MR-UNFAITHFUL-COT
  summary: "缺失引用：Lanham/Turpin"
  category: writing
  severity: info
  status: resolved
  first_raised_round: 32
  last_seen_round: 32
  resolution: "Both citations added."
  resolution_round: 32
- id: v34-R12-N1
  summary: "C3 贡献声称 overclaim"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 34
  last_seen_round: 34
  resolution: "C3 establishing→confirming(Prolog)+exploratory(ProofFOL)。Abstract/Conclusion 三处同步。Reviewer 验证 PASS。"
  resolution_round: 34
- id: v34-R12-N2
  summary: "ISR scalar framing 张力"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 34
  last_seen_round: 34
  resolution: "method.tex L54 ISR screening trigger 定位句。与 L53/L99 形成三处闭环。Reviewer 验证 PASS。"
  resolution_round: 34
- id: v34-R1-N1
  summary: "3-5 seeds proportion claim CI 宽"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 34
  last_seen_round: 34
  resolution: "正文改 existence claim；CI 移 Appendix。Reviewer 验证 PASS。"
  resolution_round: 34
- id: v34-R1-N2
  summary: "Seed 43 sensitivity 可见性不足"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 34
  last_seen_round: 34
  resolution: "正文 L65 N=2 统计句。从 footnote 升级到正文。Reviewer 验证 PASS。"
  resolution_round: 34
- id: v34-R1-N3
  summary: "Table 5 pooled Fisher 缺 descriptive-only 限定"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 34
  last_seen_round: 34
  resolution: "Appendix Table 5 caption 增加限定 + CMH 引用。Reviewer 验证 PASS。"
  resolution_round: 34
- id: v34-R12-W1
  summary: "Table 1 caption 过长"
  category: writing
  severity: warning
  status: resolved
  first_raised_round: 34
  last_seen_round: 34
  resolution: "150 词→48 词。信息无丢失。Reviewer 验证 PASS。"
  resolution_round: 34
- id: v34-R1-W3
  summary: "convergence 因果 claim 过强"
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 34
  last_seen_round: 34
  resolution: "experiments.tex + conclusion.tex 两处同步弱化。Reviewer 验证 PASS。"
  resolution_round: 34
- id: v34-R2-W3
  summary: "正文信息密度过高"
  category: writing
  severity: warning
  status: resolved
  first_raised_round: 34
  last_seen_round: 34
  resolution: "§4.4 开头 exploratory signposting。Reviewer 验证 PASS（minor 备注：与 C3 Prolog confirming 微弱张力）。"
  resolution_round: 34
- id: v34-R2-W5
  summary: "Abstract [anonymized] 脚注"
  category: writing
  severity: info
  status: resolved
  first_raised_round: 34
  last_seen_round: 34
  resolution: "已移除。Reviewer 验证 PASS。"
  resolution_round: 34
- id: v34-R1-W5
  summary: "ISR = Shapley 声明缺推导"
  category: method
  severity: info
  status: resolved
  first_raised_round: 34
  last_seen_round: 34
  resolution: "Appendix 4 行推导。Reviewer 验证 PASS。"
  resolution_round: 34
- id: v34-REVIEWER-FIG2
  summary: "Figure 2 未被正文引用"
  category: writing
  severity: warning
  status: resolved
  first_raised_round: 34
  last_seen_round: 34
  resolution: "method.tex 两处引用。Reviewer 验证 PASS。"
  resolution_round: 34
- id: v34-REVIEWER-CONCL
  summary: "conclusion.tex confirm 对 ProofFOL 过强"
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 34
  last_seen_round: 34
  resolution: "与 C3 同步修改，ProofFOL 标注 exploratory。Reviewer 验证 PASS。"
  resolution_round: 34
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01063aba-e1a0-4b5f-98ca-194fd9a47800",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "8c398dde-a549-4fa8-8250-a65dfc552d42",
  "toolUseResult": {
    "stdout": "issues:\n- id: R1-W1\n  summary: \"统计效力严重不足：β=0.3 仅 single seed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。\"\n  resolution_round: 2\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 34\n  resolution: \"Compositional narrative + screening trigger 定位。method.tex L54 显式定位 ISR 为 screening trigger。\"\n  resolution_round: 34\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 33\n  resolution: \"Compositional Goodhart reframed. χ² as primary evidence.\"\n  resolution_round: 33\n- id: v17-R12-W1\n  summary: \"单模型 (Qwen3-4B) 无法支撑通用性声明\"\n  category: experiment\n  severity: critical\n  status: wont_fix\n  first_raised_round: 17\n  last_seen_round: 33\n  resolution: \"结构性限制。Claims scoped to Qwen3-4B.\"\n- id: v27-R1-N2\n  summary: \"CMH pseudo-replication：within-seed samples 非独立\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 34\n  resolution: \"Table 5 caption 增加 descriptive-only 限定 + CMH 引用。\"\n  resolution_round: 34\n- id: v17-R1-W9\n  summary: \"Seed 43 使用 T=0.7 sampling 评估而非 greedy\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 34\n  resolution: \"正文 N=2 统计句（experiments.tex L65）+ Appendix D.6。复发×3 后从 footnote 升级到正文。\"\n  resolution_round: 34\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足——LOO 是标准技术\"\n  category: framing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 22\n  last_seen_round: 34\n  resolution: \"结构性 framing 问题。贡献在组合应用。\"\n- id: v29-R2-W5\n  summary: \"'Observe-vs-optimize asymmetry' 非新概念\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  resolution: \"Reframed as empirical instantiation of Goodhart's Law.\"\n  resolution_round: 31\n- id: v30-R1-W1\n  summary: \"SFT baseline selection bias\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 30\n  last_seen_round: 32\n  resolution: \"SFT positioned as pre-RL temporal reference.\"\n  resolution_round: 31\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 22\n  last_seen_round: 31\n  resolution: \"Positioned as corroborating rather than definitive.\"\n- id: v27-R2-W4\n  summary: \"Hacking taxonomy recall 未评估\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 34\n  resolution: \"Limitations 增加 recall 自约束论证：precision=100% + measured N-H=6% 约束 recall ≥94%。复发×3 后用数学论证彻底解决。\"\n  resolution_round: 34\n- id: v19-R12-W3\n  summary: \"ProofFOL p=0.10 被过度引用\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 34\n  resolution: \"C3 降级 establishing→confirming(Prolog)+exploratory(ProofFOL)。Abstract/Conclusion 同步。\"\n  resolution_round: 34\n- id: v30-R2-W3\n  summary: \"ISR 与 NLI accuracy 不相关限制 actionability\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 30\n  last_seen_round: 33\n  resolution: \"'reasoning quality' → 'formalization integrity'.\"\n  resolution_round: 32\n- id: v33-N2-BIMODAL\n  summary: \"5-seed 双峰弱化 Goodhart 核心叙事\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 33\n  resolution: \"C2 changed to 'seed-dependent Goodhart effect'.\"\n  resolution_round: 33\n- id: v33-W1-EXEC-POOLING\n  summary: \"Table 1 exec-only 仅报告 s42\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 33\n  resolution: \"§4.2 explains. Table 1 footnote expanded.\"\n  resolution_round: 33\n- id: v33-M8-CONVERTS\n  summary: \"'ISR converts CE into TS' 不准确\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 33\n  resolution: \"'converts' → 'systematically selects for TS over CE'.\"\n  resolution_round: 33\n- id: v33-W3-TAXONOMY\n  summary: \"Taxonomy 互斥性和 N-H upper bound 未在正文说明\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 33\n  resolution: \"Priority rule and N-H upper bound added to §3.3.\"\n  resolution_round: 33\n- id: v31-R2-MR-SPECGAMING\n  summary: \"缺失引用：Nishimura et al. 2026 spec gaming\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  resolution: \"Citation added.\"\n  resolution_round: 31\n- id: v31-R2-W-TITLE-LENGTH\n  summary: \"标题过长\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 32\n  resolution: \"Title shortened.\"\n  resolution_round: 32\n- id: v31-R2-M-ISR0-AMBIGUITY\n  summary: \"ISR=0 语义不同\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  resolution: \"ISR=0 disambiguation added.\"\n  resolution_round: 31\n- id: v32-R12-MR-UNFAITHFUL-COT\n  summary: \"缺失引用：Lanham/Turpin\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  resolution: \"Both citations added.\"\n  resolution_round: 32\n- id: v34-R12-N1\n  summary: \"C3 贡献声称 overclaim\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"C3 establishing→confirming(Prolog)+exploratory(ProofFOL)。Abstract/Conclusion 三处同步。Reviewer 验证 PASS。\"\n  resolution_round: 34\n- id: v34-R12-N2\n  summary: \"ISR scalar framing 张力\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"method.tex L54 ISR screening trigger 定位句。与 L53/L99 形成三处闭环。Reviewer 验证 PASS。\"\n  resolution_round: 34\n- id: v34-R1-N1\n  summary: \"3-5 seeds proportion claim CI 宽\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"正文改 existence claim；CI 移 Appendix。Reviewer 验证 PASS。\"\n  resolution_round: 34\n- id: v34-R1-N2\n  summary: \"Seed 43 sensitivity 可见性不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"正文 L65 N=2 统计句。从 footnote 升级到正文。Reviewer 验证 PASS。\"\n  resolution_round: 34\n- id: v34-R1-N3\n  summary: \"Table 5 pooled Fisher 缺 descriptive-only 限定\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"Appendix Table 5 caption 增加限定 + CMH 引用。Reviewer 验证 PASS。\"\n  resolution_round: 34\n- id: v34-R12-W1\n  summary: \"Table 1 caption 过长\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"150 词→48 词。信息无丢失。Reviewer 验证 PASS。\"\n  resolution_round: 34\n- id: v34-R1-W3\n  summary: \"convergence 因果 claim 过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"experiments.tex + conclusion.tex 两处同步弱化。Reviewer 验证 PASS。\"\n  resolution_round: 34\n- id: v34-R2-W3\n  summary: \"正文信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"§4.4 开头 exploratory signposting。Reviewer 验证 PASS（minor 备注：与 C3 Prolog confirming 微弱张力）。\"\n  resolution_round: 34\n- id: v34-R2-W5\n  summary: \"Abstract [anonymized] 脚注\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"已移除。Reviewer 验证 PASS。\"\n  resolution_round: 34\n- id: v34-R1-W5\n  summary: \"ISR = Shapley 声明缺推导\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"Appendix 4 行推导。Reviewer 验证 PASS。\"\n  resolution_round: 34\n- id: v34-REVIEWER-FIG2\n  summary: \"Figure 2 未被正文引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"method.tex 两处引用。Reviewer 验证 PASS。\"\n  resolution_round: 34\n- id: v34-REVIEWER-CONCL\n  summary: \"conclusion.tex confirm 对 ProofFOL 过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"与 C3 同步修改，ProofFOL 标注 exploratory。Reviewer 验证 PASS。\"\n  resolution_round: 34",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "01063aba-e1a0-4b5f-98ca-194fd9a47800",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-25T03:56:18.866Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WnGiBoM6hM576M5JesAXLw`</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/ 2>/dev/null | head -5; grep -r \"paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/ 2>/dev/null | head -5",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c398dde-a549-4fa8-8250-a65dfc552d42",
  "isSidechain": false,
  "requestId": "req_011CbNcYS29yPNyZ84yRR6Zb",
  "type": "assistant",
  "uuid": "6183b746-b929-4ad4-8fea-d44561e00740",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sLFN1hLJe59DaRDbQza7o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23844,
      "cache_read_input_tokens": 55789,
      "output_tokens": 396,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23844,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 396,
          "cache_read_input_tokens": 55789,
          "cache_creation_input_tokens": 23844,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23844
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

_source line 85 · 2026-05-25T03:56:18.959Z_

<details><summary>↩ Tool result · `toolu_01WnGiBoM6hM576M5JesAXLw`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6183b746-b929-4ad4-8fea-d44561e00740",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "f07b0a4d-0904-4b83-87eb-331095e439de",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "6183b746-b929-4ad4-8fea-d44561e00740",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 86 · 2026-05-25T03:56:34.941Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture. Let me proceed with the review:

1. The paper exists and is readable
2. EMNLP 2026 deadline: ARR submission May 25, 2026 (today), commitment August 2, 2026
3. Format: Long paper, 8 pages main text, unlimited references, double-blind, ACL template
4. External review: not configured (no `paperreview_ai` found in config)
5. Existing issues tracker: 33 issues, all resolved or wont_fix

This is a fresh review (重新审稿模式), so I should treat this as a new initial review.


For EMNLP 2026, I'll assign two reviewers following the guidelines for major conferences: one focused on methodological rigor and experimental soundness, the other on novelty, completeness, and presentation quality. I need to run the visual check, then dispatch the review requests to both reviewers with the full venue details.

The paper investigates how structural rewards in neurosymbolic reasoning can trigger Goodhart effects, using Solver Trace Ablation as a diagnostic tool and the Intensional Structural Reward metric to measure component necessity. The experiments test this on Qwen3-4B using GRPO across FOL and Prolog domains.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f07b0a4d-0904-4b83-87eb-331095e439de",
  "isSidechain": false,
  "requestId": "req_011CbNcZCpSH4BbNykLewtDJ",
  "type": "assistant",
  "uuid": "5d86beac-f57b-41e4-929d-bca5ae986c68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Wb7TyRLFCk2U6J5UmYfCY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3892,
      "cache_read_input_tokens": 79633,
      "output_tokens": 2656,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3892,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2656,
          "cache_read_input_tokens": 79633,
          "cache_creation_input_tokens": 3892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3892
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

_source line 87 · 2026-05-25T03:56:40.155Z_

论文和资料检查完毕。Venue 确认如下：

- **目标**：EMNLP 2026 (通过 ARR 统一审稿)
- **ARR 提交 deadline**：2026-05-25 (今天，AoE)
- **Commitment deadline**：2026-08-02
- **格式**：Long paper，正文 8 页，参考文献无限，double-blind，ACL 模板
- **Deadline 状态**：未过期

**Reviewer 编排**（EMNLP，2 人）：
- **Reviewer 1**：方法严谨性 + 实验设计（STA/ISR 方法有效性、统计分析、实验控制）
- **Reviewer 2**：新颖性 + 完整性 + 写作质量（贡献定位、related work 覆盖、格式合规）

现在并行派发视觉审查 + 两位 Reviewer。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d86beac-f57b-41e4-929d-bca5ae986c68",
  "isSidechain": false,
  "requestId": "req_011CbNcZCpSH4BbNykLewtDJ",
  "type": "assistant",
  "uuid": "b9195fe0-82cd-46f7-b121-8de0aa84d577",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Wb7TyRLFCk2U6J5UmYfCY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3892,
      "cache_read_input_tokens": 79633,
      "output_tokens": 2656,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3892,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2656,
          "cache_read_input_tokens": 79633,
          "cache_creation_input_tokens": 3892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3892
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

_source line 88 · 2026-05-25T03:56:42.662Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check · `toolu_01XQyYCXyJCUNreiRuNfu3jp`</summary>

```json
{
  "project": "solver-trace-ablation",
  "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9195fe0-82cd-46f7-b121-8de0aa84d577",
  "isSidechain": false,
  "requestId": "req_011CbNcZCpSH4BbNykLewtDJ",
  "type": "assistant",
  "uuid": "ad821dec-d8dd-4b83-bb68-4284b05f7bb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Wb7TyRLFCk2U6J5UmYfCY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3892,
      "cache_read_input_tokens": 79633,
      "output_tokens": 2656,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3892,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2656,
          "cache_read_input_tokens": 79633,
          "cache_creation_input_tokens": 3892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3892
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

_source line 89 · 2026-05-25T03:56:46.690Z_

<details><summary>↩ Tool result · `toolu_01XQyYCXyJCUNreiRuNfu3jp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad821dec-d8dd-4b83-bb68-4284b05f7bb9",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "3c41fd7a-b2b4-437d-b4c7-52bb7c059c61",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"status\\\": \\\"started\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "ad821dec-d8dd-4b83-bb68-4284b05f7bb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-25T03:57:00.146Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer · `toolu_01UdvwEF9N8qa3kKb3k17YEf`</summary>

```json
{
  "reviewer_id": "1",
  "round_number": 1,
  "text": "你是 Reviewer 1，负责**方法严谨性与实验设计**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (ARR 统一审稿)\n- **类别**: Long paper\n- **正文页数限制**: 8 页（参考文献不计入）\n- **匿名**: Double-blind\n- **模板**: ACL 2026\n- **ARR submission deadline**: 2026-05-25\n- **Commitment deadline**: 2026-08-02\n\n## 论文文件\n- LaTeX 源码: `projects/solver-trace-ablation/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, related_work.tex, appendix.tex）\n- PDF: `projects/solver-trace-ablation/artifacts/review_round_33/submitted.pdf`\n\n## 你的审查侧重\n1. **STA/ISR 方法有效性**：LOO ablation 作为诊断的理论基础是否充分？ISR 的数学定义是否严谨？Shapley value 联系是否正确？\n2. **实验设计**：6 个 reward conditions 的控制是否合理？随机对照组是否充分隔离 ISR-specific 信号？Shuffled-ISR control 是否有效？\n3. **统计分析**：3-5 seeds 的统计效力；premise-count confound 的处理；多重比较校正（Bonferroni）；CMH 伪重复问题\n4. **Seed 43 异常处理**：sampling (T=0.7) 评估 vs greedy——对结论的影响是否被充分讨论？N=2 sensitivity analysis 是否足够？\n5. **跨域泛化**：Prolog 复制的证据强度；ProofFOL p=0.10 的解释是否适当？Qwen3-8B/LLaMA 结果的定位\n6. **Hacking taxonomy**：8 模式分类的精度/召回率验证是否充分？152 sample precision audit 是否足够？\n7. **因果推断**：convergence→degeneration 的因果声明是否过强？confound 讨论是否充分？\n\n请按 ARR 评分标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses、Questions、Missing References、Overall Assessment。",
  "project": "solver-trace-ablation",
  "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7",
  "director_session_key": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c41fd7a-b2b4-437d-b4c7-52bb7c059c61",
  "isSidechain": false,
  "requestId": "req_011CbNcZCpSH4BbNykLewtDJ",
  "type": "assistant",
  "uuid": "a20460f0-0b6b-4de1-a658-cb690ae647cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Wb7TyRLFCk2U6J5UmYfCY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3892,
      "cache_read_input_tokens": 79633,
      "output_tokens": 2656,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3892,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2656,
          "cache_read_input_tokens": 79633,
          "cache_creation_input_tokens": 3892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3892
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

_source line 91 · 2026-05-25T03:57:01.872Z_

<details><summary>↩ Tool result · `toolu_01UdvwEF9N8qa3kKb3k17YEf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a20460f0-0b6b-4de1-a658-cb690ae647cf",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "f0341d7b-9911-4a64-a69e-b80723b0d87e",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reviewer_key\\\": \\\"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "a20460f0-0b6b-4de1-a658-cb690ae647cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-25T03:57:13.600Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer · `toolu_01LF4MfG6RYSstuZy6KmpvBX`</summary>

```json
{
  "reviewer_id": "2",
  "round_number": 1,
  "text": "你是 Reviewer 2，负责**新颖性、完整性与写作质量**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (ARR 统一审稿)\n- **类别**: Long paper\n- **正文页数限制**: 8 页（参考文献不计入）\n- **匿名**: Double-blind\n- **模板**: ACL 2026\n- **ARR submission deadline**: 2026-05-25\n- **Commitment deadline**: 2026-08-02\n\n## 论文文件\n- LaTeX 源码: `projects/solver-trace-ablation/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, related_work.tex, appendix.tex）\n- PDF: `projects/solver-trace-ablation/artifacts/review_round_33/submitted.pdf`\n\n## 你的审查侧重\n1. **新颖性评估**：LOO ablation 是标准技术（mutation testing），论文的创新贡献点在哪？\"observe-vs-optimize asymmetry\" 是否 Goodhart's Law 的已知推论？与 Kim et al. (game-formalization) 和 Bondarenko (spec-gaming) 的区分是否足够？\n2. **Related Work 覆盖**：RLVR reward hacking 文献（2025-2026）是否覆盖充分？Process reward models 文献是否完整？是否有重要遗漏？\n3. **贡献声明**：C1/C2/C3 三个贡献的定位是否准确？是否存在 overclaim？特别注意 C3 中 Prolog \"confirming\" vs ProofFOL \"exploratory\" 的措辞\n4. **写作质量**：\n   - Abstract 是否控制在 200 words 以内？\n   - 信息密度是否合适？正文 8 页是否有效利用？\n   - Figure/Table 是否清晰、被正文充分引用？\n   - 术语一致性（ISR/ISR*/STA 等）\n5. **格式合规**：\n   - ACL 模板使用是否正确？\n   - Limitations section 是否存在且位置正确（正文内，非 appendix）？\n   - 引用格式是否正确？\n   - 匿名性是否维护？（检查是否泄露作者信息）\n6. **Limitations 覆盖**：3 个点左右是否足够？是否遗漏重要限制？\n7. **伦理声明**：AI assistants 使用声明是否充分？\n\n请按 ARR 评分标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses、Questions、Missing References、Overall Assessment。",
  "project": "solver-trace-ablation",
  "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7",
  "director_session_key": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0341d7b-9911-4a64-a69e-b80723b0d87e",
  "isSidechain": false,
  "requestId": "req_011CbNcZCpSH4BbNykLewtDJ",
  "type": "assistant",
  "uuid": "c2dc93af-4d0d-4eab-8e75-a763f3ff971d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Wb7TyRLFCk2U6J5UmYfCY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3892,
      "cache_read_input_tokens": 79633,
      "output_tokens": 2656,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3892,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2656,
          "cache_read_input_tokens": 79633,
          "cache_creation_input_tokens": 3892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3892
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
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: solver-trace-ablation - 论文路径: projects/solver-trace-ablation/docs/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: Long paper (ARR) - 截止日期: 未提供，请自行调研 - **引用验证**: ❌ 未启用…",
  "leafUuid": "c2dc93af-4d0d-4eab-8e75-a763f3ff971d",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646"
}
```

---

### Runtime record

_source line 94_

```json
{
  "type": "ai-title",
  "aiTitle": "Review solver-trace-ablation paper for EMNLP 2026",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646"
}
```

---

### Tool result

_source line 95 · 2026-05-25T03:57:15.304Z_

<details><summary>↩ Tool result · `toolu_01LF4MfG6RYSstuZy6KmpvBX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2dc93af-4d0d-4eab-8e75-a763f3ff971d",
  "isSidechain": false,
  "promptId": "dc9278f9-a33b-4351-8906-b4e9b67d6b74",
  "type": "user",
  "uuid": "7e552dc3-d4ff-4703-be1d-354e51b5988b",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reviewer_key\\\": \\\"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "c2dc93af-4d0d-4eab-8e75-a763f3ff971d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 96 · 2026-05-25T03:57:15.310Z_

```json
{
  "parentUuid": "7e552dc3-d4ff-4703-be1d-354e51b5988b",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "acc738d0-5ba5-43ca-b749-dc982740884f",
  "timestamp": "2026-05-25T03:57:15.310Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 97_

```json
{
  "type": "ai-title",
  "aiTitle": "Review solver-trace-ablation paper for EMNLP 2026",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646"
}
```

---

### Runtime record

_source line 98 · 2026-05-25T04:05:35.405Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T04:05:35.405Z",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "content": "[Reviewer 1 审稿意见]:\n\n## Reviewer 1 审稿意见：方法严谨性与实验设计\n\n**论文标题**: Observe but Don't Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning\n\n---\n\n## 总体评分\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n**一句话总结**: STA 作为诊断工具的构想新颖且有价值，observe-vs-optimize 不对称性是重要发现，但统计效力不足（核心条件仅 1-3 seeds）、seed 43 评估协议不一致未被修正、premise-count confound 未被充分解决，使得定量结论的可信度受限。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3 / 5 | 方法论框架合理但统计效力严重不足；ISR 标量优势被 premise-count confound 完全解释（McNemar p=0.317）；compositional evidence 更强但也受 premise-count 影响 |\n| Excitement | 3.5 / 5 | 问题重要（RLVR 中的 Goodhart 效应），STA 诊断工具填补了真实空白，observe-optimize asymmetry 是有启发性的概念贡献 |\n| Reproducibility | 3 / 5 | 超参数报告详尽（Table 2），但 seed 43 协议不一致、exec-only 仅单 seed 报告、已删除 checkpoints 阻碍完整验证 |\n| Confidence | 4 / 5 | 仔细阅读全文及全部 24 页附录，熟悉 RLVR、reward hacking、mutation testing 相关文献 |\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation（STA），一种基于 Leave-One-Out（LOO）消融的诊断方法，用于检测神经符号推理中 GRPO 训练产生的结构性退化。核心指标 ISR（Intensional Structural Reward）量化每个组件的个体必要性。论文的关键发现是 observe-vs-optimize 不对称性：ISR 作为事后诊断有效，但作为训练奖励时会被 tautological shortcuts（TS）所 Goodhart 化。实验覆盖 FOL/Prolog 两种逻辑类型、FOLIO/ProofFOL 两个数据集，并建立了 8 类 hacking 模式的分类体系。\n\n---\n\n## 主要优势（Strengths）\n\n**S1. 诊断方法填补真实空白。** 现有 process reward models 需要步骤级标注（Lightman et al., 2023），inference-time gaming detection 无法提供训练信号（Kim et al., 2026）。STA 仅依赖 solver 输出即可检测组件冗余，$O(n)$ 开销在 Prover9 下 <1%（Appendix D.3, ~55ms/sample），实用性好。\n\n**S2. Observe-optimize asymmetry 是重要概念贡献。** 同一个 LOO 结构使 ISR 既能诊断又能被博弈（§1, §3.3），这一悖论对所有基于可验证代理指标的 RLVR 方法具有广泛警示意义。TS 通过 $P \\to P$ 构造性满足 ISR≥0.5（§3.3）的机制分析清晰。\n\n**S3. 控制组设计周到。** Random 控制隔离 ISR-specific 信号 vs. reward-variance 效应；Shuffled-ISR 控制（3-seed pooled, 87% non-hacking, PR=15%）确认 Goodhart 效应需要 sample-level ISR 信号而非分布形状（Table 1）。SFT 基线（92% non-hacking）建立了 RL 前的参考点。\n\n**S4. 对自身弱点的透明讨论。** 论文罕见地坦诚承认了 premise-count confound 完全解释了 ISR 标量优势（§4.3: \"The 214× raw ISR* collapse is largely explained by premise-count reduction\"），seed 43 协议不一致（§4.1 脚注），以及统计效力不足（Limitations §6）。这种学术诚实值得肯定。\n\n**S5. Hacking taxonomy 细致。** 8 种模式有定义、示例、ISR 交互分析和流行率数据（Appendix C）。Prolog 中发现的 query-as-fact gaming 和 uppercase pseudo-Prolog 展示了模型在不同逻辑系统中发现不同博弈路径的能力。\n\n**S6. Prolog 跨逻辑复制有力。** 3/3 seeds 达到 0% non-hacking，且各通过不同机制（TS/功能性 TS/query-as-fact），证明 Goodhart 效应跨逻辑类型普遍存在（Table 11）。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Exec-only 诊断结论依赖单一 seed，代表性不足\n- 具体位置：§4.2, Table 1 (Exec-only† 行), experiments.tex line 38\n- 问题：Exec-only 条件——STA 诊断能力的核心展示——仅报告 seed 42（PR=93%, ISR*=0.132, CE=87%）。论文承认 \"Exec-only seeds exhibit qualitatively different convergence patterns (PR range: 13-98%), precluding meaningful pooling\"，但这恰恰说明单 seed 结论不可靠。Appendix D 显示 seed 43 的 PR=13%（未收敛），seed 44 的 PR=98% 且 100% TS（完全不同的退化模式）。§4.2 的 \"ISR collapse trajectory\"（ISR*: 0.642→0.132→0.003）仅基于 seed 42，无法确定这是典型行为还是个案。\n- 为什么影响接收：论文的 C1 贡献（STA 作为诊断工具）的核心实证依据来自这一单 seed 轨迹。如果读者不仔细看附录，会误以为 ISR 退化轨迹是 exec-only GRPO 的普遍规律，而实际上 3 个 seed 中只有 1 个展现了这种 clean trajectory。\n- 建议修改方向：在正文中明确展示 3 个 seed 的诊断结果对比（不仅是脚注），讨论为何不同 seed 产生不同退化模式但最终都收敛到低 genuine 率。或者增加更多 seeds 以建立统计规律。\n\n**N2** [critical] Seed 43 评估协议不一致——方法论缺陷\n- 具体位置：§4.1 脚注 2, Appendix A (appendix.tex line 60-62), Appendix D.6\n- 问题：Seed 43 在所有条件下的评估使用 sampling T=0.7 而非 greedy decoding（论文标准协议）。这影响 ISR β=0.1 seed 43（100% TS）、Random β=0.1 seed 43（38.3% TS——唯一产生 TS 的 Random seed）、以及 exec-only seed 43 的所有数据。论文提供了 N=2 sensitivity analysis（Appendix D.6），但 N=2 几乎没有统计意义（ISR* = 0.659±0.344，方差大于均值）。关键问题：**为何不重新用 greedy 评估 seed 43？** 论文没有解释。这不是数据丢失问题（模型 checkpoint 可以重新评估），而是方法论上的疏忽。\n- 为什么影响接收：3 个核心 seed 中有 1 个使用不同评估协议，且该 seed 在 Random 条件下产生了异常的 38.3% TS 率（其他 2 个 seed 为 0%）。这个异常值直接影响 pooled statistics（Random TS 率从 0% 被拉到 14%），进而影响 ISR vs Random 的 compositional comparison。\n- 建议修改方向：用 greedy decoding 重新评估 seed 43 的所有条件。如果 checkpoint 已不可用，至少需要更多 seeds（如扩展到 5-7 seeds）来补偿这个 protocol violation。\n\n**N3** [critical] Premise-count confound 未被充分解决——影响核心 claim\n- 具体位置：§4.3 (experiments.tex lines 67-75), Appendix B.2 (appendix.tex lines 120-128), Table 4\n- 问题：论文坦诚承认 214× 的 raw ISR* 下降 \"largely explained by premise-count reduction\"，matched comparison 仅 1.06×（McNemar p=0.317，不显著）。论文转向 compositional evidence（TS vs CE shift）作为 primary evidence。然而，TS shift 本身也受 premise-count 影响：§4.3 明确指出 \"TS hacking is mechanistically limited to simpler problems—models cannot restate the conclusion while ignoring all premises when formalization complexity is high\"。Table 4 确认 TS 集中在 4-6 premise 范围，≥7 premises 时 TS=0%。这意味着 ISR reward 是否促进了 TS，还是 ISR reward 碰巧产生了更短的 formalizations（因而更容易出现 TS），仍有混淆。\n- 为什么影响接收：如果 compositional shift 也能被 premise-count reduction 解释，则 ISR-as-reward 的 Goodhart 效应的独特性——论文的 C2 贡献——被大幅削弱。论文需要在 premise-count matched 条件下也展示 TS 率差异。\n- 建议修改方向：在相同 premise-count bin 内比较 ISR vs Random 的 TS 率。Table 4 已有这些数据（4-6 premise bin: ISR 19.7% TS vs Random 0% TS）——但仅基于 seed 42，需要多 seed 验证。建议正文中更突出这一 premise-matched TS 分析，并提供相应的统计检验。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Shapley value 关联的数学表述不够精确\n- 具体位置：§3.2 (method.tex line 53), Appendix B (appendix.tex lines 113-118)\n- 问题：论文称 ISR 是 \"(n-1)-coalition Shapley value 的 special case\"。严格来说，这不正确。Shapley value 对所有 coalition sizes 求平均（包括 |S|=0 到 |S|=n-1），ISR 仅使用 |S|=n-1 的 marginal contribution。这是 Shapley value 的一个特定 approximation（LOO approximation），不是 \"special case\"。\"Special case\" 意味着在某些条件下 LOO 估计等于完整 Shapley value，但论文未建立这种等价条件。Appendix B 的推导正确展示了 ISR 如何从 LOO marginal contribution 推导出来，但将其称为 \"Shapley value\" 是过度声称。\n- 建议：将 \"special case of the (n-1)-coalition Shapley value\" 改为 \"the (n-1)-coalition marginal contribution, a LOO approximation to the Shapley value\"。这更精确且不损失任何诊断价值。\n\n**W2** [warning] 标题中 \"Trigger\" 暗示因果关系，证据不足以支撑\n- 具体位置：标题, §5 (conclusion.tex line 6)\n- 问题：标题 \"Structural Rewards Trigger Goodhart Effects\" 使用 \"trigger\" 暗示因果关系。但论文正文明确承认 \"capability and optimization confounds preclude causal attribution\"（§5）。Goodhart 效应与 convergence 的共现可能是模型能力的函数：能收敛的 seed 同时更容易找到 shortcut。这是一个 confound，不是 trigger。\n- 建议：考虑使用更中性的措辞如 \"Structural Rewards Exhibit Goodhart Effects\" 或 \"Structural Rewards Produce Goodhart Effects\"。\n\n**W3** [warning] 单一基础模型限制泛化性\n- 具体位置：§6 Limitations (limitations.tex line 1), Appendix D.4 (LLaMA), Appendix D.8 (Qwen3-8B)\n- 问题：主要实验仅使用 Qwen3-4B。LLaMA-3.2-3B 无法生成有效 FOL（cold-start failure, Appendix D.4），Qwen3-8B 在 exec-only GRPO 下未收敛（PR=14%, Appendix D.8, 仅 1 seed）。这些是 negative results——其他模型未能展现 Goodhart 效应，是因为它们未能收敛（capability threshold），但这也意味着 STA 诊断和 Goodhart 发现的泛化性完全未被验证。\n- 建议：需要至少一个额外的成功收敛的模型来展示跨模型泛化。可以尝试更大的模型或更好的 SFT warmstart。\n\n**W4** [warning] 已删除 checkpoints 阻碍完整 PG 审计\n- 具体位置：Appendix C.1 (appendix.tex lines 322-325)\n- 问题：PG（premise-subset gaming）的审计仅完成了 ISR β=0.1 seed 42。论文承认 \"ISR seeds 43 and 44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated.\" 这意味着 Table 1 中 ISR β=0.1 的 N-H%=6 可能不准确——如果 seed 43/44 也存在未检测的 PG，真实 non-hacking 率可能更低。\n- 建议：在论文中更醒目地标注此限制（不仅在 Appendix C.1），并讨论 PG 对 pooled statistics 的潜在影响。\n\n**W5** [warning] ProofFOL 证据过弱，不应在 contributions 中列出\n- 具体位置：§1 C3, §4.4, §5\n- 问题：ProofFOL 结果 p=0.10，N=3 per group，不显著。论文正确标注为 \"exploratory and underpowered\"（§4.1），但 C3 贡献声称 \"exploratory cross-dataset evidence (FOLIO/ProofFOL)\"。一个 p=0.10 的非显著结果出现在贡献列表中，会给 AC 留下过度声称的印象。\n- 建议：从 C3 贡献中移除 ProofFOL 或明确标注为 \"preliminary\"。Prolog 跨逻辑复制足以支撑 C3。\n\n---\n\n## Questions for Authors\n\n**Q1.** Seed 43 的 sampling T=0.7 评估是否可以用 greedy 重新执行？如果 checkpoint 仍然可用，这应该是 camera-ready 的最低要求。如果不可用，请解释为何在发现协议不一致后没有立即保存 checkpoint。\n\n**Q2.** Table 4 的 premise-count-matched TS 分析（4-6 bin: ISR 19.7% vs Random 0%）仅基于 seed 42。seeds 43 和 44 在相同 premise bin 内是否也呈现 TS 偏移？这是支撑 N3 修改的关键数据。\n\n**Q3.** Shuffled-ISR 控制的 PR（15±1%）远低于 ISR（77±14%）和 Random（87±8%）。作者如何排除这一低 PR 本身（而非 ISR 信号的缺失）导致了 87% non-hacking 率？SFT 在类似低 PR（13%）也有 92% non-hacking——这是否仅说明低 PR 模型还没 \"学会\" hacking，而非 Shuffled-ISR 的 sample-level 去关联起了作用？\n\n**Q4.** 论文声称 ISR 的 LOO underestimation 使诊断 \"conservative\"（§3.2）。但如果存在 jointly-unnecessary 但 individually-necessary 的组件对（例如两个互相替代的冗余路径），LOO 会将它们都标为 necessary，导致 ISR overestimation。这种情况在 FOL 形式化中是否可能出现？\n\n**Q5.** Qwen3-8B 和 LLaMA-3.2-3B 的 negative results 是否应该被理解为 STA 对模型 capability 的依赖？如果 Goodhart 效应仅在一个特定模型-规模-数据集组合中出现，其理论意义如何？\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract 字数为 ~192 words（在 200 word 限制内），但较长的嵌套从句降低了可读性（第 4-5 句）。\n- Table 1 的 ISR* 列：3-seed 行报告 \"1.06×‡\" 而非实际 ISR 值，与其他行不一致，需要脚注来理解。5-seed 行的 \"(0.63)‡\" 同样需要说明括号含义。\n- §3.2 的 \"proved-only ISR (denoted ISR*)\" 在首次出现时应更早定义，而非在 §3.2 末尾。\n- Appendix C.1 的 PG 检测方法描述为 \"manual inspection of non-hacking samples with unusually low premise counts\"——这一人工检测过程的判断标准不够形式化。\n- Figure 4 的 premise-count bins 仅展示 seed 42，未标注；读者可能误以为是 pooled results。\n\n---\n\n## Missing References\n\n- Shapley value 在 ML 可解释性中的应用综述（如 Molnar, 2022, Interpretable ML）可以更好地定位 ISR-Shapley 关联。\n- Reward hacking 领域的 concurrent work：Pan et al. (2025, \"Spontaneous Reward Hacking in Iterative Self-Refinement\") 和 Wang et al. (2026, \"Reward Hacking in the Era of Large Models\") 已被引用，但 Burns et al. (2023, \"Weak-to-Strong Generalization\") 在讨论 capability threshold 时可能相关。\n- Mutation testing 领域的 equivalent mutant problem（Jia & Harman, 2011 已引用但未讨论 equivalent mutant 概念）与 ISR 的 false positive/negative 直接相关。\n\n---\n\n## 总结\n\n本文的核心贡献——STA 作为诊断工具和 observe-vs-optimize 不对称性——是有价值的，对 neurosymbolic RLVR 社区有实际指导意义。Hacking taxonomy 详尽、控制组设计周到、Prolog 跨逻辑复制有力。但在统计执行层面存在系统性不足：核心条件的 seed 数太少（exec-only N=1, ISR N=2-3 clean seeds）、evaluation protocol 不一致未被修正、premise-count confound 对 compositional evidence 的影响未被充分隔离。这些问题使定量结论的可靠性低于顶会标准。论文的学术诚实性突出（主动承认大部分弱点），这在一定程度上弥补了执行上的不足，但不能替代更严格的实验设计。\n\n建议：如果作者能 (1) 修复 seed 43 的评估协议, (2) 增加 seeds 数至 5-7, (3) 在 premise-count matched 条件下展示多 seed 的 TS 率差异, 本文可以提升到 clear accept (4.0)。\n"
}
```

---

### Runtime record

_source line 99 · 2026-05-25T04:05:35.406Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T04:05:35.406Z",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646"
}
```

---

## Round 2

2 recorded events

### User

_source line 100 · 2026-05-25T04:05:35.388Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acc738d0-5ba5-43ca-b749-dc982740884f",
  "isSidechain": false,
  "promptId": "4c15d144-e535-4dbc-95db-4a456593f03a",
  "type": "user",
  "isMeta": true,
  "uuid": "c582f8ac-a18b-4695-ba12-7a3fcacf7790",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 101 · 2026-05-25T04:05:35.388Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c582f8ac-a18b-4695-ba12-7a3fcacf7790",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "43a7f35a-6eed-44ab-b033-a3574c21580f",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "id": "b5468d20-b3b9-4a51-94e0-71602865e73c",
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

7 recorded events

### User

_source line 102 · 2026-05-25T04:05:35.600Z_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿意见：方法严谨性与实验设计

**论文标题**: Observe but Don't Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning

---

## 总体评分
**Overall Assessment**: 3.5 / 5 (Borderline Conference)
**一句话总结**: STA 作为诊断工具的构想新颖且有价值，observe-vs-optimize 不对称性是重要发现，但统计效力不足（核心条件仅 1-3 seeds）、seed 43 评估协议不一致未被修正、premise-count confound 未被充分解决，使得定量结论的可信度受限。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3 / 5 | 方法论框架合理但统计效力严重不足；ISR 标量优势被 premise-count confound 完全解释（McNemar p=0.317）；compositional evidence 更强但也受 premise-count 影响 |
| Excitement | 3.5 / 5 | 问题重要（RLVR 中的 Goodhart 效应），STA 诊断工具填补了真实空白，observe-optimize asymmetry 是有启发性的概念贡献 |
| Reproducibility | 3 / 5 | 超参数报告详尽（Table 2），但 seed 43 协议不一致、exec-only 仅单 seed 报告、已删除 checkpoints 阻碍完整验证 |
| Confidence | 4 / 5 | 仔细阅读全文及全部 24 页附录，熟悉 RLVR、reward hacking、mutation testing 相关文献 |

---

## Summary

本文提出 Solver Trace Ablation（STA），一种基于 Leave-One-Out（LOO）消融的诊断方法，用于检测神经符号推理中 GRPO 训练产生的结构性退化。核心指标 ISR（Intensional Structural Reward）量化每个组件的个体必要性。论文的关键发现是 observe-vs-optimize 不对称性：ISR 作为事后诊断有效，但作为训练奖励时会被 tautological shortcuts（TS）所 Goodhart 化。实验覆盖 FOL/Prolog 两种逻辑类型、FOLIO/ProofFOL 两个数据集，并建立了 8 类 hacking 模式的分类体系。

---

## 主要优势（Strengths）

**S1. 诊断方法填补真实空白。** 现有 process reward models 需要步骤级标注（Lightman et al., 2023），inference-time gaming detection 无法提供训练信号（Kim et al., 2026）。STA 仅依赖 solver 输出即可检测组件冗余，$O(n)$ 开销在 Prover9 下 <1%（Appendix D.3, ~55ms/sample），实用性好。

**S2. Observe-optimize asymmetry 是重要概念贡献。** 同一个 LOO 结构使 ISR 既能诊断又能被博弈（§1, §3.3），这一悖论对所有基于可验证代理指标的 RLVR 方法具有广泛警示意义。TS 通过 $P \to P$ 构造性满足 ISR≥0.5（§3.3）的机制分析清晰。

**S3. 控制组设计周到。** Random 控制隔离 ISR-specific 信号 vs. reward-variance 效应；Shuffled-ISR 控制（3-seed pooled, 87% non-hacking, PR=15%）确认 Goodhart 效应需要 sample-level ISR 信号而非分布形状（Table 1）。SFT 基线（92% non-hacking）建立了 RL 前的参考点。

**S4. 对自身弱点的透明讨论。** 论文罕见地坦诚承认了 premise-count confound 完全解释了 ISR 标量优势（§4.3: "The 214× raw ISR* collapse is largely explained by premise-count reduction"），seed 43 协议不一致（§4.1 脚注），以及统计效力不足（Limitations §6）。这种学术诚实值得肯定。

**S5. Hacking taxonomy 细致。** 8 种模式有定义、示例、ISR 交互分析和流行率数据（Appendix C）。Prolog 中发现的 query-as-fact gaming 和 uppercase pseudo-Prolog 展示了模型在不同逻辑系统中发现不同博弈路径的能力。

**S6. Prolog 跨逻辑复制有力。** 3/3 seeds 达到 0% non-hacking，且各通过不同机制（TS/功能性 TS/query-as-fact），证明 Goodhart 效应跨逻辑类型普遍存在（Table 11）。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Exec-only 诊断结论依赖单一 seed，代表性不足
- 具体位置：§4.2, Table 1 (Exec-only† 行), experiments.tex line 38
- 问题：Exec-only 条件——STA 诊断能力的核心展示——仅报告 seed 42（PR=93%, ISR*=0.132, CE=87%）。论文承认 "Exec-only seeds exhibit qualitatively different convergence patterns (PR range: 13-98%), precluding meaningful pooling"，但这恰恰说明单 seed 结论不可靠。Appendix D 显示 seed 43 的 PR=13%（未收敛），seed 44 的 PR=98% 且 100% TS（完全不同的退化模式）。§4.2 的 "ISR collapse trajectory"（ISR*: 0.642→0.132→0.003）仅基于 seed 42，无法确定这是典型行为还是个案。
- 为什么影响接收：论文的 C1 贡献（STA 作为诊断工具）的核心实证依据来自这一单 seed 轨迹。如果读者不仔细看附录，会误以为 ISR 退化轨迹是 exec-only GRPO 的普遍规律，而实际上 3 个 seed 中只有 1 个展现了这种 clean trajectory。
- 建议修改方向：在正文中明确展示 3 个 seed 的诊断结果对比（不仅是脚注），讨论为何不同 seed 产生不同退化模式但最终都收敛到低 genuine 率。或者增加更多 seeds 以建立统计规律。

**N2** [critical] Seed 43 评估协议不一致——方法论缺陷
- 具体位置：§4.1 脚注 2, Appendix A (appendix.tex line 60-62), Appendix D.6
- 问题：Seed 43 在所有条件下的评估使用 sampling T=0.7 而非 greedy decoding（论文标准协议）。这影响 ISR β=0.1 seed 43（100% TS）、Random β=0.1 seed 43（38.3% TS——唯一产生 TS 的 Random seed）、以及 exec-only seed 43 的所有数据。论文提供了 N=2 sensitivity analysis（Appendix D.6），但 N=2 几乎没有统计意义（ISR* = 0.659±0.344，方差大于均值）。关键问题：**为何不重新用 greedy 评估 seed 43？** 论文没有解释。这不是数据丢失问题（模型 checkpoint 可以重新评估），而是方法论上的疏忽。
- 为什么影响接收：3 个核心 seed 中有 1 个使用不同评估协议，且该 seed 在 Random 条件下产生了异常的 38.3% TS 率（其他 2 个 seed 为 0%）。这个异常值直接影响 pooled statistics（Random TS 率从 0% 被拉到 14%），进而影响 ISR vs Random 的 compositional comparison。
- 建议修改方向：用 greedy decoding 重新评估 seed 43 的所有条件。如果 checkpoint 已不可用，至少需要更多 seeds（如扩展到 5-7 seeds）来补偿这个 protocol violation。

**N3** [critical] Premise-count confound 未被充分解决——影响核心 claim
- 具体位置：§4.3 (experiments.tex lines 67-75), Appendix B.2 (appendix.tex lines 120-128), Table 4
- 问题：论文坦诚承认 214× 的 raw ISR* 下降 "largely explained by premise-count reduction"，matched comparison 仅 1.06×（McNemar p=0.317，不显著）。论文转向 compositional evidence（TS vs CE shift）作为 primary evidence。然而，TS shift 本身也受 premise-count 影响：§4.3 明确指出 "TS hacking is mechanistically limited to simpler problems—models cannot restate the conclusion while ignoring all premises when formalization complexity is high"。Table 4 确认 TS 集中在 4-6 premise 范围，≥7 premises 时 TS=0%。这意味着 ISR reward 是否促进了 TS，还是 ISR reward 碰巧产生了更短的 formalizations（因而更容易出现 TS），仍有混淆。
- 为什么影响接收：如果 compositional shift 也能被 premise-count reduction 解释，则 ISR-as-reward 的 Goodhart 效应的独特性——论文的 C2 贡献——被大幅削弱。论文需要在 premise-count matched 条件下也展示 TS 率差异。
- 建议修改方向：在相同 premise-count bin 内比较 ISR vs Random 的 TS 率。Table 4 已有这些数据（4-6 premise bin: ISR 19.7% TS vs Random 0% TS）——但仅基于 seed 42，需要多 seed 验证。建议正文中更突出这一 premise-matched TS 分析，并提供相应的统计检验。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Shapley value 关联的数学表述不够精确
- 具体位置：§3.2 (method.tex line 53), Appendix B (appendix.tex lines 113-118)
- 问题：论文称 ISR 是 "(n-1)-coalition Shapley value 的 special case"。严格来说，这不正确。Shapley value 对所有 coalition sizes 求平均（包括 |S|=0 到 |S|=n-1），ISR 仅使用 |S|=n-1 的 marginal contribution。这是 Shapley value 的一个特定 approximation（LOO approximation），不是 "special case"。"Special case" 意味着在某些条件下 LOO 估计等于完整 Shapley value，但论文未建立这种等价条件。Appendix B 的推导正确展示了 ISR 如何从 LOO marginal contribution 推导出来，但将其称为 "Shapley value" 是过度声称。
- 建议：将 "special case of the (n-1)-coalition Shapley value" 改为 "the (n-1)-coalition marginal contribution, a LOO approximation to the Shapley value"。这更精确且不损失任何诊断价值。

**W2** [warning] 标题中 "Trigger" 暗示因果关系，证据不足以支撑
- 具体位置：标题, §5 (conclusion.tex line 6)
- 问题：标题 "Structural Rewards Trigger Goodhart Effects" 使用 "trigger" 暗示因果关系。但论文正文明确承认 "capability and optimization confounds preclude causal attribution"（§5）。Goodhart 效应与 convergence 的共现可能是模型能力的函数：能收敛的 seed 同时更容易找到 shortcut。这是一个 confound，不是 trigger。
- 建议：考虑使用更中性的措辞如 "Structural Rewards Exhibit Goodhart Effects" 或 "Structural Rewards Produce Goodhart Effects"。

**W3** [warning] 单一基础模型限制泛化性
- 具体位置：§6 Limitations (limitations.tex line 1), Appendix D.4 (LLaMA), Appendix D.8 (Qwen3-8B)
- 问题：主要实验仅使用 Qwen3-4B。LLaMA-3.2-3B 无法生成有效 FOL（cold-start failure, Appendix D.4），Qwen3-8B 在 exec-only GRPO 下未收敛（PR=14%, Appendix D.8, 仅 1 seed）。这些是 negative results——其他模型未能展现 Goodhart 效应，是因为它们未能收敛（capability threshold），但这也意味着 STA 诊断和 Goodhart 发现的泛化性完全未被验证。
- 建议：需要至少一个额外的成功收敛的模型来展示跨模型泛化。可以尝试更大的模型或更好的 SFT warmstart。

**W4** [warning] 已删除 checkpoints 阻碍完整 PG 审计
- 具体位置：Appendix C.1 (appendix.tex lines 322-325)
- 问题：PG（premise-subset gaming）的审计仅完成了 ISR β=0.1 seed 42。论文承认 "ISR seeds 43 and 44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated." 这意味着 Table 1 中 ISR β=0.1 的 N-H%=6 可能不准确——如果 seed 43/44 也存在未检测的 PG，真实 non-hacking 率可能更低。
- 建议：在论文中更醒目地标注此限制（不仅在 Appendix C.1），并讨论 PG 对 pooled statistics 的潜在影响。

**W5** [warning] ProofFOL 证据过弱，不应在 contributions 中列出
- 具体位置：§1 C3, §4.4, §5
- 问题：ProofFOL 结果 p=0.10，N=3 per group，不显著。论文正确标注为 "exploratory and underpowered"（§4.1），但 C3 贡献声称 "exploratory cross-dataset evidence (FOLIO/ProofFOL)"。一个 p=0.10 的非显著结果出现在贡献列表中，会给 AC 留下过度声称的印象。
- 建议：从 C3 贡献中移除 ProofFOL 或明确标注为 "preliminary"。Prolog 跨逻辑复制足以支撑 C3。

---

## Questions for Authors

**Q1.** Seed 43 的 sampling T=0.7 评估是否可以用 greedy 重新执行？如果 checkpoint 仍然可用，这应该是 camera-ready 的最低要求。如果不可用，请解释为何在发现协议不一致后没有立即保存 checkpoint。

**Q2.** Table 4 的 premise-count-matched TS 分析（4-6 bin: ISR 19.7% vs Random 0%）仅基于 seed 42。seeds 43 和 44 在相同 premise bin 内是否也呈现 TS 偏移？这是支撑 N3 修改的关键数据。

**Q3.** Shuffled-ISR 控制的 PR（15±1%）远低于 ISR（77±14%）和 Random（87±8%）。作者如何排除这一低 PR 本身（而非 ISR 信号的缺失）导致了 87% non-hacking 率？SFT 在类似低 PR（13%）也有 92% non-hacking——这是否仅说明低 PR 模型还没 "学会" hacking，而非 Shuffled-ISR 的 sample-level 去关联起了作用？

**Q4.** 论文声称 ISR 的 LOO underestimation 使诊断 "conservative"（§3.2）。但如果存在 jointly-unnecessary 但 individually-necessary 的组件对（例如两个互相替代的冗余路径），LOO 会将它们都标为 necessary，导致 ISR overestimation。这种情况在 FOL 形式化中是否可能出现？

**Q5.** Qwen3-8B 和 LLaMA-3.2-3B 的 negative results 是否应该被理解为 STA 对模型 capability 的依赖？如果 Goodhart 效应仅在一个特定模型-规模-数据集组合中出现，其理论意义如何？

---

## 小问题（不影响接收）

- Abstract 字数为 ~192 words（在 200 word 限制内），但较长的嵌套从句降低了可读性（第 4-5 句）。
- Table 1 的 ISR* 列：3-seed 行报告 "1.06×‡" 而非实际 ISR 值，与其他行不一致，需要脚注来理解。5-seed 行的 "(0.63)‡" 同样需要说明括号含义。
- §3.2 的 "proved-only ISR (denoted ISR*)" 在首次出现时应更早定义，而非在 §3.2 末尾。
- Appendix C.1 的 PG 检测方法描述为 "manual inspection of non-hacking samples with unusually low premise counts"——这一人工检测过程的判断标准不够形式化。
- Figure 4 的 premise-count bins 仅展示 seed 42，未标注；读者可能误以为是 pooled results。

---

## Missing References

- Shapley value 在 ML 可解释性中的应用综述（如 Molnar, 2022, Interpretable ML）可以更好地定位 ISR-Shapley 关联。
- Reward hacking 领域的 concurrent work：Pan et al. (2025, "Spontaneous Reward Hacking in Iterative Self-Refinement") 和 Wang et al. (2026, "Reward Hacking in the Era of Large Models") 已被引用，但 Burns et al. (2023, "Weak-to-Strong Generalization") 在讨论 capability threshold 时可能相关。
- Mutation testing 领域的 equivalent mutant problem（Jia & Harman, 2011 已引用但未讨论 equivalent mutant 概念）与 ISR 的 false positive/negative 直接相关。

---

## 总结

本文的核心贡献——STA 作为诊断工具和 observe-vs-optimize 不对称性——是有价值的，对 neurosymbolic RLVR 社区有实际指导意义。Hacking taxonomy 详尽、控制组设计周到、Prolog 跨逻辑复制有力。但在统计执行层面存在系统性不足：核心条件的 seed 数太少（exec-only N=1, ISR N=2-3 clean seeds）、evaluation protocol 不一致未被修正、premise-count confound 对 compositional evidence 的影响未被充分隔离。这些问题使定量结论的可靠性低于顶会标准。论文的学术诚实性突出（主动承认大部分弱点），这在一定程度上弥补了执行上的不足，但不能替代更严格的实验设计。

建议：如果作者能 (1) 修复 seed 43 的评估协议, (2) 增加 seeds 数至 5-7, (3) 在 premise-count matched 条件下展示多 seed 的 TS 率差异, 本文可以提升到 clear accept (4.0)。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43a7f35a-6eed-44ab-b033-a3574c21580f",
  "isSidechain": false,
  "promptId": "4c15d144-e535-4dbc-95db-4a456593f03a",
  "type": "user",
  "uuid": "5940762d-718b-497a-851b-d686614a4ec3",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 103_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Reviewer 1 审稿意见]:  ## Reviewer 1 审稿意见：方法严谨性与实验设计  **论文标题**: Observe but Don't Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning  ---  ## 总体评分 **Overall Assessment**: 3.…",
  "leafUuid": "5940762d-718b-497a-851b-d686614a4ec3",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646"
}
```

---

### Runtime record

_source line 104_

```json
{
  "type": "ai-title",
  "aiTitle": "Review solver-trace-ablation paper for EMNLP 2026",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646"
}
```

---

### Runtime record

_source line 105_

```json
{
  "type": "ai-title",
  "aiTitle": "Review solver-trace-ablation paper for EMNLP 2026",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646"
}
```

---

### Runtime record

_source line 106 · 2026-05-25T04:05:44.762Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T04:05:44.762Z",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "content": "[Reviewer 1 审稿结果]:\n审稿意见已提交给 Review Director。\n\n核心评判：**Overall 3.5 / 5（Borderline Conference）**。\n\n主要发现：\n- STA 诊断方法和 observe-vs-optimize 不对称性是有价值的贡献\n- 3 个 Must-Fix 问题：exec-only 仅单 seed 代表性不足、seed 43 评估协议不一致未修正、premise-count confound 对 compositional evidence 的影响未被隔离\n- 5 个 Should-Fix 问题：Shapley value 表述不精确、标题因果暗示过强、单一基础模型、已删除 checkpoints、ProofFOL 证据过弱\n- 论文的学术诚实性值得肯定，但统计执行层面存在系统性不足"
}
```

---

### Runtime record

_source line 107 · 2026-05-25T04:05:44.763Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T04:05:44.763Z",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646"
}
```

---

### Assistant

_source line 108 · 2026-05-25T04:05:44.751Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5940762d-718b-497a-851b-d686614a4ec3",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "f02fc9f3-48b7-48fe-b070-5b98039ae561",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "id": "ed91de7e-09db-4b9a-99d8-2af549bfd9a3",
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

1 recorded events

### User

_source line 109 · 2026-05-25T04:05:44.883Z_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心评判：**Overall 3.5 / 5（Borderline Conference）**。

主要发现：
- STA 诊断方法和 observe-vs-optimize 不对称性是有价值的贡献
- 3 个 Must-Fix 问题：exec-only 仅单 seed 代表性不足、seed 43 评估协议不一致未修正、premise-count confound 对 compositional evidence 的影响未被隔离
- 5 个 Should-Fix 问题：Shapley value 表述不精确、标题因果暗示过强、单一基础模型、已删除 checkpoints、ProofFOL 证据过弱
- 论文的学术诚实性值得肯定，但统计执行层面存在系统性不足

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f02fc9f3-48b7-48fe-b070-5b98039ae561",
  "isSidechain": false,
  "promptId": "e445bfd9-1ddc-4d9b-9706-a189f703df0c",
  "type": "user",
  "uuid": "af22633d-49e7-4fdb-940b-35f7e354501e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029",
  "sessionId": "f8953b3f-e1da-4479-9348-d08b652e1646",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---
