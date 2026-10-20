# Research conversation: 系统通知：审稿审批已通过。请开始审稿。 [论文提交] - 项目: causal_annot_error_attrib - 论文路径: /home/ubuntu/.agent-ml-research-prod_0510/projects/ca

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 141
- **Recorded user turns:** 12
- **Tool calls:** 28
- **Original source:** `logs/chats/exported-trajectories/account-1/c928a4cc-3e3f-4de1-bdfb-f994449906a4.jsonl`
- **Structured JSON:** [`e1c5c307a9d6d7f46713.json`](../../sessions/e1/e1c5c307a9d6d7f46713.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T13:40:35.331Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T13:40:35.331Z",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "content": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: causal_annot_error_attrib\n- 论文路径: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: Long Paper (via ARR)\n- 截止日期: 未提供，请自行调研\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

---

### Runtime record

_source line 2 · 2026-05-22T13:40:35.335Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T13:40:35.335Z",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

## Round 1

66 recorded events

### User

_source line 3 · 2026-05-22T13:40:35.374Z_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_annot_error_attrib
- 论文路径: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (via ARR)
- 截止日期: 未提供，请自行调研
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e832977f-06f5-437f-9468-12b340b28a19",
  "type": "user",
  "uuid": "3e35545b-eca1-45e6-a5ac-e3d12d8b5ce0",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T13:40:35.373Z_

```json
{
  "parentUuid": "3e35545b-eca1-45e6-a5ac-e3d12d8b5ce0",
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
  "uuid": "4df43c96-ced2-4362-b208-57df446f83d3",
  "timestamp": "2026-05-22T13:40:35.373Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T13:40:35.373Z_

```json
{
  "parentUuid": "4df43c96-ced2-4362-b208-57df446f83d3",
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
  "uuid": "5d57a55e-6d43-4d68-afbd-f0e27c2e547c",
  "timestamp": "2026-05-22T13:40:35.373Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-22T13:40:35.373Z_

```json
{
  "parentUuid": "5d57a55e-6d43-4d68-afbd-f0e27c2e547c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f07ca7aa-528f-47c5-b518-6a515505f920",
  "timestamp": "2026-05-22T13:40:35.373Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
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
  "aiTitle": "Review causal annotation error attribution paper",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Assistant

_source line 8 · 2026-05-22T13:40:38.147Z_

<details><summary>Logged reasoning block</summary>

```text
The user is asking me to start a review process for a paper submission. Let me follow the instructions and first read the review-director-session-start skill file to get the full review process.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f07ca7aa-528f-47c5-b518-6a515505f920",
  "isSidechain": false,
  "requestId": "req_011CbHhgcobD5vpdzXYWUnyu",
  "type": "assistant",
  "uuid": "0413a01f-0f07-428b-aea3-a0bb11ac1fcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012VZYQNZMG1k4DrkJTGRJR9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16932,
      "cache_read_input_tokens": 11841,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16932,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 134,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16932
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

_source line 9 · 2026-05-22T13:40:38.386Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ra9XNtPZM9UKobgHSvn2Fc`</summary>

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
  "parentUuid": "0413a01f-0f07-428b-aea3-a0bb11ac1fcf",
  "isSidechain": false,
  "requestId": "req_011CbHhgcobD5vpdzXYWUnyu",
  "type": "assistant",
  "uuid": "b2e1117f-bf13-44a9-8b84-ea6955abf12c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012VZYQNZMG1k4DrkJTGRJR9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16932,
      "cache_read_input_tokens": 11841,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16932,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 134,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16932
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

_source line 10 · 2026-05-22T13:40:38.405Z_

<details><summary>↩ Tool result · `toolu_01Ra9XNtPZM9UKobgHSvn2Fc`</summary>

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
  "parentUuid": "b2e1117f-bf13-44a9-8b84-ea6955abf12c",
  "isSidechain": false,
  "promptId": "e832977f-06f5-437f-9468-12b340b28a19",
  "type": "user",
  "uuid": "2875338e-9b4c-4759-b19a-64b78f679eaa",
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
  "sourceToolAssistantUUID": "b2e1117f-bf13-44a9-8b84-ea6955abf12c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
````

</details>

---

### Assistant

_source line 11 · 2026-05-22T13:40:42.592Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to follow the steps outlined in the skill file. Let me start with:

1. Step 0 — Resource check + Venue research
2. Get project overview
3. Check paper files

Let me do these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2875338e-9b4c-4759-b19a-64b78f679eaa",
  "isSidechain": false,
  "requestId": "req_011CbHhgqqAp6PBQ3PzqXsNF",
  "type": "assistant",
  "uuid": "2b26a21f-8fe4-4fca-920a-d9ba6d6bb637",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rrtc18Ld3KgPNmchApcTit",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3461,
      "cache_read_input_tokens": 28773,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3461,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 309,
          "cache_read_input_tokens": 28773,
          "cache_creation_input_tokens": 3461,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3461
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

_source line 12 · 2026-05-22T13:40:43.546Z_

开始审稿流程。先执行初始化和资料检查。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b26a21f-8fe4-4fca-920a-d9ba6d6bb637",
  "isSidechain": false,
  "requestId": "req_011CbHhgqqAp6PBQ3PzqXsNF",
  "type": "assistant",
  "uuid": "c08e8c39-f9cb-489e-8dd3-df1cae794396",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rrtc18Ld3KgPNmchApcTit",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3461,
      "cache_read_input_tokens": 28773,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3461,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 309,
          "cache_read_input_tokens": 28773,
          "cache_creation_input_tokens": 3461,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3461
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

_source line 13 · 2026-05-22T13:40:46.188Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GAfgrqQMtMV8xePbbYMjnL`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c08e8c39-f9cb-489e-8dd3-df1cae794396",
  "isSidechain": false,
  "requestId": "req_011CbHhgqqAp6PBQ3PzqXsNF",
  "type": "assistant",
  "uuid": "0b048441-0c9a-44f7-b9ce-d7cc151414c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rrtc18Ld3KgPNmchApcTit",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3461,
      "cache_read_input_tokens": 28773,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3461,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 309,
          "cache_read_input_tokens": 28773,
          "cache_creation_input_tokens": 3461,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3461
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

_source line 14 · 2026-05-22T13:40:46.193Z_

<details><summary>↩ Tool result · `toolu_01GAfgrqQMtMV8xePbbYMjnL`</summary>

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
  "parentUuid": "0b048441-0c9a-44f7-b9ce-d7cc151414c1",
  "isSidechain": false,
  "promptId": "e832977f-06f5-437f-9468-12b340b28a19",
  "type": "user",
  "uuid": "bf4ee2c7-93f3-4309-a1e2-b411d17d4e11",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__dispatch_visual_check",
      "mcp__agent-ml-research__get_external_review_status",
      "mcp__agent-ml-research__get_visual_check_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__request_external_review",
      "mcp__agent-ml-research__submit_review_report_to_research_director",
      "mcp__agent-ml-research__update_review_issues"
    ],
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "total_deferred_tools": 29
  },
  "sourceToolAssistantUUID": "0b048441-0c9a-44f7-b9ce-d7cc151414c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
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
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: causal_annot_error_attrib - 论文路径: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: Long…",
  "leafUuid": "bf4ee2c7-93f3-4309-a1e2-b411d17d4e11",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Review causal annotation error attribution paper",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Assistant

_source line 17 · 2026-05-22T13:40:49.773Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the tools loaded. Let me start the initialization process:

1. Get project overview
2. Check paper files exist
3. Search for EMNLP 2026 venue requirements

Let me do these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf4ee2c7-93f3-4309-a1e2-b411d17d4e11",
  "isSidechain": false,
  "requestId": "req_011CbHhhR1Cm6v9qLYGfARTp",
  "type": "assistant",
  "uuid": "837c67b8-9c4d-4482-9548-97933965ba79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GdZLz7Y9D5jadiNvFUAYcT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3440,
      "cache_read_input_tokens": 32234,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3440,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 288,
          "cache_read_input_tokens": 32234,
          "cache_creation_input_tokens": 3440,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3440
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

_source line 18 · 2026-05-22T13:40:50.301Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01DH11cMh4rZFjhmTH162HGz`</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "837c67b8-9c4d-4482-9548-97933965ba79",
  "isSidechain": false,
  "requestId": "req_011CbHhhR1Cm6v9qLYGfARTp",
  "type": "assistant",
  "uuid": "91317526-e1ba-40cd-a57a-a6ae33b1c7a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GdZLz7Y9D5jadiNvFUAYcT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3440,
      "cache_read_input_tokens": 32234,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3440,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 288,
          "cache_read_input_tokens": 32234,
          "cache_creation_input_tokens": 3440,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3440
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

_source line 19 · 2026-05-22T13:40:50.390Z_

<details><summary>↩ Tool result · `toolu_01DH11cMh4rZFjhmTH162HGz`</summary>

```text
{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91317526-e1ba-40cd-a57a-a6ae33b1c7a5",
  "isSidechain": false,
  "promptId": "e832977f-06f5-437f-9468-12b340b28a19",
  "type": "user",
  "uuid": "f0a4089c-f1ee-4782-9727-2c8cad497bae",
  "toolUseResult": "{\"result\":\"# 项目 causal_annot_error_attrib 概况\\n\\n## 实验状态 (14 个)\\n\\n- **plan006_asv_empirical**: DONE (success) — \\n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \\n- **plan003_empirical_confusion_matrices**: DONE (failed) — \\n- **plan007_correction_guidance**: DONE (success) — \\n- **plan009_pathological_matrices**: DONE (success) — \\n- **plan005_asv_extended**: DONE (success) — \\n- **plan002_k57_extension**: DONE (success) — \\n- **plan001_dag_taxonomy**: DONE (success) — \\n- **plan004_asv_framework**: DONE (success) — \\n- **plan_004_asv_v3_fixed**: DONE (success) — \\n- **plan008_binarization_collapse**: DONE (success) — \\n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \\n- **mvp_exposure_dag**: DONE (success) — \\n- **mvp_confounding_dag**: DONE (success) — \\n\\n## 最新报告\\n# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\\n\\n## 趋势\\n成功 13 / 负向 0 / 失败 1 / 共 14\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nhome-1x5090: 无 GPU 信息\\n\\n## 告警\\n- plan003_empirical_confusion_matrices: 训练失败 — unknown\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"
    }
  },
  "sourceToolAssistantUUID": "91317526-e1ba-40cd-a57a-a6ae33b1c7a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T13:40:52.516Z_

<details><summary>↩ Tool result · `toolu_01Ggm5yeX9rBsNU4mE7mKjvU`</summary>

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
  "parentUuid": "af456273-aa2f-4a85-b9f0-acf6ed1bfc49",
  "isSidechain": false,
  "promptId": "e832977f-06f5-437f-9468-12b340b28a19",
  "type": "user",
  "uuid": "2895b59f-5e70-432f-89d7-e920a361ba91",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 29
  },
  "sourceToolAssistantUUID": "af456273-aa2f-4a85-b9f0-acf6ed1bfc49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T13:40:52.259Z_

<details open><summary>🔧 Tool call — Read · `toolu_014kKoGgy4vtczLoUjAV2cvz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0a4089c-f1ee-4782-9727-2c8cad497bae",
  "isSidechain": false,
  "requestId": "req_011CbHhhR1Cm6v9qLYGfARTp",
  "type": "assistant",
  "uuid": "fd8c067e-4dc0-46e2-ac98-30c983ec1a76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GdZLz7Y9D5jadiNvFUAYcT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3440,
      "cache_read_input_tokens": 32234,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3440,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 288,
          "cache_read_input_tokens": 32234,
          "cache_creation_input_tokens": 3440,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3440
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

_source line 22 · 2026-05-22T13:40:52.264Z_

<details><summary>↩ Tool result · `toolu_014kKoGgy4vtczLoUjAV2cvz`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{graphicx}
5	\usepackage{algorithm}
6	\usepackage{algorithmic}
7	
8	\usepackage{amsmath,amssymb,amsthm}
9	\usepackage{booktabs}
10	\usepackage{pifont}
11	\usepackage{multirow}
12	
13	\newtheorem{definition}{Definition}
14	\newtheorem{proposition}{Proposition}
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{lemma}{Lemma}
17	\newtheorem{conjecture}{Conjecture}
18	
19	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
20	\setlength{\dbltextfloatsep}{8pt plus 2pt minus 4pt}
21	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
22	\setlength{\dblfloatsep}{8pt plus 2pt minus 4pt}
23	\graphicspath{{../../figures/paper/}}
24	
25	\title{Multi-Class Annotation Errors in Causal Inference:\\Topology-Dependent Bias, Sensitivity, and Correction}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	\input{abstract}
33	
34	\input{introduction}
35	
36	\input{related_work}
37	
38	\input{method}
39	
40	% ── Figures ──
41	
42	\begin{figure*}[t]
43	\centering
44	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig1_dag_taxonomy.pdf}
45	\vspace{-6pt}
46	\caption{Seven canonical DAG topologies with starred-node annotation. $A$ (latent) connects to $A^*$ (observed) via a dashed measurement edge; the causal role of $A$ varies across topologies.}
47	\label{fig:dag_taxonomy}
48	\end{figure*}
49	
50	\begin{figure*}[t]
51	\centering
52	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig2_bias_distribution.pdf}
53	\vspace{-6pt}
54	\caption{Bias distributions under 100{,}000 random $K{=}3$ confusion matrices. Red = sign reversal. Exposure: 83.4\% sign reversal; IV: 52.6\%.}
55	\label{fig:bias_distribution}
56	\end{figure*}
57	
58	\input{experiments}
59	
60	\input{conclusion}
61	
62	\bibliography{references}
63	
64	\appendix
65	\input{appendix_proofs}
66	
67	\end{document}
68	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd8c067e-4dc0-46e2-ac98-30c983ec1a76",
  "isSidechain": false,
  "promptId": "e832977f-06f5-437f-9468-12b340b28a19",
  "type": "user",
  "uuid": "cf4f42cb-df9a-4f01-80b6-00aae11ef961",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\n\\usepackage{graphicx}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\n\\usepackage{amsmath,amssymb,amsthm}\n\\usepackage{booktabs}\n\\usepackage{pifont}\n\\usepackage{multirow}\n\n\\newtheorem{definition}{Definition}\n\\newtheorem{proposition}{Proposition}\n\\newtheorem{theorem}{Theorem}\n\\newtheorem{lemma}{Lemma}\n\\newtheorem{conjecture}{Conjecture}\n\n\\setlength{\\textfloatsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\dbltextfloatsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\floatsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\dblfloatsep}{8pt plus 2pt minus 4pt}\n\\graphicspath{{../../figures/paper/}}\n\n\\title{Multi-Class Annotation Errors in Causal Inference:\\\\Topology-Dependent Bias, Sensitivity, and Correction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{method}\n\n% ── Figures ──\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.92\\textwidth,height=0.18\\textheight,keepaspectratio]{fig1_dag_taxonomy.pdf}\n\\vspace{-6pt}\n\\caption{Seven canonical DAG topologies with starred-node annotation. $A$ (latent) connects to $A^*$ (observed) via a dashed measurement edge; the causal role of $A$ varies across topologies.}\n\\label{fig:dag_taxonomy}\n\\end{figure*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.92\\textwidth,height=0.18\\textheight,keepaspectratio]{fig2_bias_distribution.pdf}\n\\vspace{-6pt}\n\\caption{Bias distributions under 100{,}000 random $K{=}3$ confusion matrices. Red = sign reversal. Exposure: 83.4\\% sign reversal; IV: 52.6\\%.}\n\\label{fig:bias_distribution}\n\\end{figure*}\n\n\\input{experiments}\n\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\appendix\n\\input{appendix_proofs}\n\n\\end{document}\n",
      "numLines": 68,
      "startLine": 1,
      "totalLines": 68
    }
  },
  "sourceToolAssistantUUID": "fd8c067e-4dc0-46e2-ac98-30c983ec1a76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T13:40:52.513Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Ggm5yeX9rBsNU4mE7mKjvU`</summary>

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
  "parentUuid": "cf4f42cb-df9a-4f01-80b6-00aae11ef961",
  "isSidechain": false,
  "requestId": "req_011CbHhhR1Cm6v9qLYGfARTp",
  "type": "assistant",
  "uuid": "af456273-aa2f-4a85-b9f0-acf6ed1bfc49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GdZLz7Y9D5jadiNvFUAYcT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3440,
      "cache_read_input_tokens": 32234,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3440,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 288,
          "cache_read_input_tokens": 32234,
          "cache_creation_input_tokens": 3440,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3440
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

_source line 24 · 2026-05-22T13:41:00.108Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the project overview, the main.tex file, and the WebSearch tool loaded. Now let me:

1. Search for EMNLP 2026 / ARR venue requirements
2. Read the paper sections to understand the content
3. Check if the PDF exists

Let me do the venue search and read paper sections in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2895b59f-5e70-432f-89d7-e920a361ba91",
  "isSidechain": false,
  "requestId": "req_011CbHhhuVDJbJGqxsQjHX9V",
  "type": "assistant",
  "uuid": "9f90ba10-963c-4f01-ba5f-84e893b0bd34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1SFgPbwipYimAhth6sbrq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2591,
      "cache_read_input_tokens": 35674,
      "output_tokens": 397,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2591,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 397,
          "cache_read_input_tokens": 35674,
          "cache_creation_input_tokens": 2591,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2591
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

_source line 25 · 2026-05-22T13:41:01.224Z_

论文文件已确认存在，使用 ACL review 模板。现在搜索 EMNLP 2026 / ARR 投稿要求。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f90ba10-963c-4f01-ba5f-84e893b0bd34",
  "isSidechain": false,
  "requestId": "req_011CbHhhuVDJbJGqxsQjHX9V",
  "type": "assistant",
  "uuid": "86bef6ca-97c7-4bbd-9bc4-e0dc3510df9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1SFgPbwipYimAhth6sbrq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2591,
      "cache_read_input_tokens": 35674,
      "output_tokens": 397,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2591,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 397,
          "cache_read_input_tokens": 35674,
          "cache_creation_input_tokens": 2591,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2591
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

_source line 26 · 2026-05-22T13:41:01.737Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BkScUt9SNQAjQzsyrz9Gxj`</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission deadline author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86bef6ca-97c7-4bbd-9bc4-e0dc3510df9b",
  "isSidechain": false,
  "requestId": "req_011CbHhhuVDJbJGqxsQjHX9V",
  "type": "assistant",
  "uuid": "facbf15e-aaab-4395-82ef-04f64c9641dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1SFgPbwipYimAhth6sbrq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2591,
      "cache_read_input_tokens": 35674,
      "output_tokens": 397,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2591,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 397,
          "cache_read_input_tokens": 35674,
          "cache_creation_input_tokens": 2591,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2591
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

_source line 27 · 2026-05-22T13:41:04.759Z_

<details><summary>↩ Tool result · `toolu_012EtDoLWTgFuuPbTDaBzeF4`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models; these errors are highly correlated across models (60\% agreement when both err)~\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference.
5	
6	The consequences can be catastrophic. Even under realistic classifier accuracy (diagonal $\geq 0.7$), 13.7\% of $K{=}3$ confusion matrices produce violations of the classical binary guarantee, with 2.1\% causing outright \emph{sign reversal} of the estimated treatment effect. Across the full Dirichlet$(1,1,1)$ parameter space, sign reversal reaches 83.4\%, establishing that it is the majority outcome under uniform priors, not a pathological edge case. This failure breaks the classical binary guarantee that non-differential misclassification biases estimates ``toward the null''~\cite{brenner1993}, a guarantee that many applied researchers implicitly rely upon. Moreover, standard classification metrics do not predict downstream causal risk: within a narrow $F_1$ range of 0.614--0.690 across three frontier LLMs, relative bias varies by an order of magnitude across topologies (from 4.1\% to 42.1\%), illustrating that \emph{topology}, not annotator quality, determines downstream risk.
7	
8	The mechanism is algebraic, and the transition at $K {\geq} 3$ is a qualitative break, not a gradual degradation. For $K{=}2$, the stochastic constraint forces any confusion matrix with $C_{kk} {>} 0.5$ to preserve coefficient signs---an algebraic property of the $2{\times}2$ matrix dimension, not of a specific error rate. This guarantee \emph{vanishes} at $K {\geq} 3$: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients, enabling sign reversal even when every diagonal entry exceeds $0.5$~\cite{veirod_laake2001}. This fundamental asymmetry has received limited systematic treatment. \citet{brenner1993} identified the possibility of polytomous reversal but did not characterize it across causal designs. \citet{lee_wood_doughty2024} extended classifier error analysis to categorical variables and LLM classifiers, but covered only one DAG topology (unobserved confounding). No existing framework addresses how the same confusion matrix produces qualitatively different bias across different causal identification strategies.
9	
10	We address these gaps with three contributions:
11	
12	\begin{enumerate}
13	\item \textbf{Multi-class bias taxonomy.} We derive bias expressions for seven canonical DAG topologies (Figure~\ref{fig:dag_taxonomy}) under $K$-class non-differential misclassification and establish that five topologies maintain a structural sign-flip guarantee while exposure and IV can produce sign reversal. Binarization amplifies the gap: collapsing $K{=}3$ to binary introduces additional bias varying 154$\times$ across topologies.
14	
15	\item \textbf{Annotation Sensitivity Values (ASVs).} We propose three complementary sensitivity measures---magnitude, significance, and sign-flip ASV---revealing a vulnerability spectrum from IV (maximally fragile, 52.6\% sign reversal) to M-bias (immune, ASV $= \infty$).
16	
17	\item \textbf{Topology-aware correction guidance.} We evaluate five correction methods and show that matrix-based corrections achieve exactly 0\% bias reduction for four topologies due to Frisch--Waugh--Lovell invariance. PPI++ achieves 47.0\% RMSE reduction but requires gold labels and is harmful for M-bias ($-$88\%).
18	\end{enumerate}
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0620e978-0b75-4662-92d8-b80cec734d69",
  "isSidechain": false,
  "promptId": "e832977f-06f5-437f-9468-12b340b28a19",
  "type": "user",
  "uuid": "9ff27b9b-8fdb-4f75-bdb9-9b6f2c40e8b3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLarge language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\\cite{egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \\citet{baumann2025} demonstrate that across 37 annotation tasks, 31\\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\\% for smaller models; these errors are highly correlated across models (60\\% agreement when both err)~\\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \\emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference.\n\nThe consequences can be catastrophic. Even under realistic classifier accuracy (diagonal $\\geq 0.7$), 13.7\\% of $K{=}3$ confusion matrices produce violations of the classical binary guarantee, with 2.1\\% causing outright \\emph{sign reversal} of the estimated treatment effect. Across the full Dirichlet$(1,1,1)$ parameter space, sign reversal reaches 83.4\\%, establishing that it is the majority outcome under uniform priors, not a pathological edge case. This failure breaks the classical binary guarantee that non-differential misclassification biases estimates ``toward the null''~\\cite{brenner1993}, a guarantee that many applied researchers implicitly rely upon. Moreover, standard classification metrics do not predict downstream causal risk: within a narrow $F_1$ range of 0.614--0.690 across three frontier LLMs, relative bias varies by an order of magnitude across topologies (from 4.1\\% to 42.1\\%), illustrating that \\emph{topology}, not annotator quality, determines downstream risk.\n\nThe mechanism is algebraic, and the transition at $K {\\geq} 3$ is a qualitative break, not a gradual degradation. For $K{=}2$, the stochastic constraint forces any confusion matrix with $C_{kk} {>} 0.5$ to preserve coefficient signs---an algebraic property of the $2{\\times}2$ matrix dimension, not of a specific error rate. This guarantee \\emph{vanishes} at $K {\\geq} 3$: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients, enabling sign reversal even when every diagonal entry exceeds $0.5$~\\cite{veirod_laake2001}. This fundamental asymmetry has received limited systematic treatment. \\citet{brenner1993} identified the possibility of polytomous reversal but did not characterize it across causal designs. \\citet{lee_wood_doughty2024} extended classifier error analysis to categorical variables and LLM classifiers, but covered only one DAG topology (unobserved confounding). No existing framework addresses how the same confusion matrix produces qualitatively different bias across different causal identification strategies.\n\nWe address these gaps with three contributions:\n\n\\begin{enumerate}\n\\item \\textbf{Multi-class bias taxonomy.} We derive bias expressions for seven canonical DAG topologies (Figure~\\ref{fig:dag_taxonomy}) under $K$-class non-differential misclassification and establish that five topologies maintain a structural sign-flip guarantee while exposure and IV can produce sign reversal. Binarization amplifies the gap: collapsing $K{=}3$ to binary introduces additional bias varying 154$\\times$ across topologies.\n\n\\item \\textbf{Annotation Sensitivity Values (ASVs).} We propose three complementary sensitivity measures---magnitude, significance, and sign-flip ASV---revealing a vulnerability spectrum from IV (maximally fragile, 52.6\\% sign reversal) to M-bias (immune, ASV $= \\infty$).\n\n\\item \\textbf{Topology-aware correction guidance.} We evaluate five correction methods and show that matrix-based corrections achieve exactly 0\\% bias reduction for four topologies due to Frisch--Waugh--Lovell invariance. PPI++ achieves 47.0\\% RMSE reduction but requires gold labels and is harmful for M-bias ($-$88\\%).\n\\end{enumerate}\n",
      "numLines": 19,
      "startLine": 1,
      "totalLines": 19
    }
  },
  "sourceToolAssistantUUID": "0620e978-0b75-4662-92d8-b80cec734d69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-22T13:41:02.799Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LDoQWFbhHGxX1WZRTLP125`</summary>

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
  "parentUuid": "facbf15e-aaab-4395-82ef-04f64c9641dd",
  "isSidechain": false,
  "requestId": "req_011CbHhhuVDJbJGqxsQjHX9V",
  "type": "assistant",
  "uuid": "ce3f4f6b-365b-4385-81c8-6578e7395a0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1SFgPbwipYimAhth6sbrq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2591,
      "cache_read_input_tokens": 35674,
      "output_tokens": 397,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2591,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 397,
          "cache_read_input_tokens": 35674,
          "cache_creation_input_tokens": 2591,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2591
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

_source line 29 · 2026-05-22T13:41:04.573Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Eb4N94T9G4Gx3uyZqZ8fMp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce3f4f6b-365b-4385-81c8-6578e7395a0b",
  "isSidechain": false,
  "requestId": "req_011CbHhhuVDJbJGqxsQjHX9V",
  "type": "assistant",
  "uuid": "4b6b0b5b-2120-4b2f-a266-27ea1163c381",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1SFgPbwipYimAhth6sbrq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2591,
      "cache_read_input_tokens": 35674,
      "output_tokens": 397,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2591,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 397,
          "cache_read_input_tokens": 35674,
          "cache_creation_input_tokens": 2591,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2591
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

_source line 30 · 2026-05-22T13:41:04.579Z_

<details><summary>↩ Tool result · `toolu_01Eb4N94T9G4Gx3uyZqZ8fMp`</summary>

```text
1	\begin{abstract}
2	Large language models (LLMs) are increasingly used as annotators in computational social science, yet annotation errors propagate into downstream causal estimates in ways that binary measurement error theory cannot predict. We present a systematic framework characterizing how $K$-class confusion matrix structure interacts with DAG topology to determine bias direction and magnitude. We derive bias expressions for seven canonical DAG topologies under multi-class non-differential misclassification and establish that five topologies show no sign reversal across extensive numerical verification (proven analytically for confounding and collider via sufficient conditions; Appendix~A), while exposure and instrumental variable topologies can produce sign reversal---under realistic classifier accuracy (diagonal $\geq 0.7$), the violation rate is 13.7\% with 2.1\% sign reversal; across the full Dirichlet$(1,1,1)$ parameter space, the rate reaches 83.4\%. We introduce Annotation Sensitivity Values (ASVs) with three complementary measures revealing a topology-dependent vulnerability spectrum from IV (maximally fragile, 52.6\% sign reversal) to M-bias (immune). We evaluate five correction methods and prove a Frisch--Waugh--Lovell invariance result: matrix-based corrections achieve 0\% bias reduction for four topologies, while PPI++ achieves 47.0\% RMSE reduction but requires gold labels and is harmful for M-bias ($-$88\%). Empirical validation on three tasks ($K{=}2,3,10$) with four LLMs confirms structural predictions: zero sign reversals across five guaranteed topologies, while 61\% of exposure configurations exhibit coefficient-level sign reversal in secondary coefficients. Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b6b0b5b-2120-4b2f-a266-27ea1163c381",
  "isSidechain": false,
  "promptId": "e832977f-06f5-437f-9468-12b340b28a19",
  "type": "user",
  "uuid": "0df448a8-81b3-4385-bc04-e81e03c984d5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nLarge language models (LLMs) are increasingly used as annotators in computational social science, yet annotation errors propagate into downstream causal estimates in ways that binary measurement error theory cannot predict. We present a systematic framework characterizing how $K$-class confusion matrix structure interacts with DAG topology to determine bias direction and magnitude. We derive bias expressions for seven canonical DAG topologies under multi-class non-differential misclassification and establish that five topologies show no sign reversal across extensive numerical verification (proven analytically for confounding and collider via sufficient conditions; Appendix~A), while exposure and instrumental variable topologies can produce sign reversal---under realistic classifier accuracy (diagonal $\\geq 0.7$), the violation rate is 13.7\\% with 2.1\\% sign reversal; across the full Dirichlet$(1,1,1)$ parameter space, the rate reaches 83.4\\%. We introduce Annotation Sensitivity Values (ASVs) with three complementary measures revealing a topology-dependent vulnerability spectrum from IV (maximally fragile, 52.6\\% sign reversal) to M-bias (immune). We evaluate five correction methods and prove a Frisch--Waugh--Lovell invariance result: matrix-based corrections achieve 0\\% bias reduction for four topologies, while PPI++ achieves 47.0\\% RMSE reduction but requires gold labels and is harmful for M-bias ($-$88\\%). Empirical validation on three tasks ($K{=}2,3,10$) with four LLMs confirms structural predictions: zero sign reversals across five guaranteed topologies, while 61\\% of exposure configurations exhibit coefficient-level sign reversal in secondary coefficients. Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations.\n\\end{abstract}\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  },
  "sourceToolAssistantUUID": "4b6b0b5b-2120-4b2f-a266-27ea1163c381",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T13:41:04.749Z_

<details open><summary>🔧 Tool call — Read · `toolu_012EtDoLWTgFuuPbTDaBzeF4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0df448a8-81b3-4385-bc04-e81e03c984d5",
  "isSidechain": false,
  "requestId": "req_011CbHhhuVDJbJGqxsQjHX9V",
  "type": "assistant",
  "uuid": "0620e978-0b75-4662-92d8-b80cec734d69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1SFgPbwipYimAhth6sbrq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2591,
      "cache_read_input_tokens": 35674,
      "output_tokens": 397,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2591,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 397,
          "cache_read_input_tokens": 35674,
          "cache_creation_input_tokens": 2591,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2591
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

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: causal_annot_error_attrib - 论文路径: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: Long…",
  "leafUuid": "9ff27b9b-8fdb-4f75-bdb9-9b6f2c40e8b3",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Review causal annotation error attribution paper",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Tool result

_source line 34 · 2026-05-22T13:41:09.085Z_

<details><summary>↩ Tool result · `toolu_01LDoQWFbhHGxX1WZRTLP125`</summary>

```text
Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results for ACL Rolling Review 2026 submission guidelines, here are the key page limit and format requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Upon acceptance, final versions of long papers will be given one additional page – up to nine (9) pages of content plus unlimited pages for acknowledgments and references.

Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references. Final versions of short papers may have up to five (5) pages, plus unlimited pages for acknowledgments and references.

## Format Requirements

For both long and short papers, all figures and tables that are part of the main text must fit within these page limits.

The paper must have a section titled "Limitations" and can only include the discussion of limitations; strictly no new experiments, figures or analysis. It does not count towards the page limit.

The paper should follow ACL formatting. There is an official Overleaf template, and this template has a [review] setting that must be on for the submission.

Papers must not include authors' names and affiliations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce3f4f6b-365b-4385-81c8-6578e7395a0b",
  "isSidechain": false,
  "promptId": "e832977f-06f5-437f-9468-12b340b28a19",
  "type": "user",
  "uuid": "59355038-7b98-459a-80b1-367db79e4a29",
  "toolUseResult": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements",
    "results": [
      {
        "tool_use_id": "srvtoolu_01M49Zk3FkJ1WABMLqV1RmY8",
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
            "title": "Paper formatting guidelines - ACLPUB",
            "url": "https://acl-org.github.io/ACLPUB/formatting.html"
          },
          {
            "title": "Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authorchecklist"
          },
          {
            "title": "Call for Main Conference Papers -",
            "url": "https://2026.eacl.org/calls/papers/"
          },
          {
            "title": "Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/submissionform"
          },
          {
            "title": "ACL Rolling Review | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/acl-rolling-review"
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
      "Based on the search results for ACL Rolling Review 2026 submission guidelines, here are the key page limit and format requirements:\n\n## Page Limits\n\nReview versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Upon acceptance, final versions of long papers will be given one additional page – up to nine (9) pages of content plus unlimited pages for acknowledgments and references.\n\nReview versions of short papers may have up to four (4) pages of content, plus unlimited pages for references. Final versions of short papers may have up to five (5) pages, plus unlimited pages for acknowledgments and references.\n\n## Format Requirements\n\nFor both long and short papers, all figures and tables that are part of the main text must fit within these page limits.\n\nThe paper must have a section titled \"Limitations\" and can only include the discussion of limitations; strictly no new experiments, figures or analysis. It does not count towards the page limit.\n\nThe paper should follow ACL formatting. There is an official Overleaf template, and this template has a [review] setting that must be on for the submission.\n\nPapers must not include authors' names and affiliations."
    ],
    "durationSeconds": 6.283077568
  },
  "sourceToolAssistantUUID": "ce3f4f6b-365b-4385-81c8-6578e7395a0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-22T13:41:15.654Z_

<details><summary>↩ Tool result · `toolu_01BkScUt9SNQAjQzsyrz9Gxj`</summary>

```text
Web search results for query: "EMNLP 2026 ARR call for papers submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Now let me search for the author guidelines specifically:

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Submission Checklist for Original, First Time Submissions | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/OriginalSubmissionChecklist"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"LaTeLL_26_template - Overleaf, Online LaTeX Editor","url":"https://www.overleaf.com/latex/templates/latell-26-template/kfcvbgxmccvb"},{"title":"EMNLP: Empirical Methods in Natural Language Processing Template - ACM Conference","url":"https://scispace.com/formats/acm-conference/emnlp-empirical-methods-in-natural-language-processing/9660af2f47424125a400febdfef4f76f"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on my search results, here's the comprehensive information about EMNLP 2026 ARR call for papers:

## EMNLP 2026 ARR Call for Papers - Key Information

### Submission Deadline
The ARR submission deadline is May 25, 2026.

### Important Dates
- Reviewer registration deadline for ALL authors: May 27, 2026
- Author response and author-reviewer discussion: July 7 - July 13, 2026
- Meta review released: July 30, 2026
- EMNLP commitment deadline: August 2, 2026
- Notification of acceptance (long & short papers): August 20, 2026
- Camera-ready papers due: September 20, 2026

### Submission Types
EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

### Author Guidelines & Format Requirements
The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. The mandatory Limitations section is required, placed after the conclusion.

EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences, available at github.com/acl-org/acl-style-files.

### Special Policy for EMNLP 2026
Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time. This choice will be binding for EMNLP 2026: ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.

### Mandatory Reviewer Registration
After submission, all authors must complete the author registration form by May 27, 2026 EoD AoE.

For the complete and official details, visit the EMNLP 2026 call for papers page at https://2026.emnlp.org/calls/main_conference_papers/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "facbf15e-aaab-4395-82ef-04f64c9641dd",
  "isSidechain": false,
  "promptId": "e832977f-06f5-437f-9468-12b340b28a19",
  "type": "user",
  "uuid": "5e7c2fcb-f27a-4902-8594-48ea606955e6",
  "toolUseResult": {
    "query": "EMNLP 2026 ARR call for papers submission deadline author guidelines",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SfuXBSLSHR5i3hVewV6WSy",
        "content": [
          {
            "title": "Call for Main Conference Papers - EMNLP 2026",
            "url": "https://2026.emnlp.org/calls/main_conference_papers/"
          },
          {
            "title": "EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X",
            "url": "https://x.com/emnlpmeeting/status/2029508292637061462"
          },
          {
            "title": "Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/dates"
          },
          {
            "title": "EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X",
            "url": "https://x.com/emnlpmeeting/status/2047754845919031450"
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
            "title": "CALL FOR PAPERS – ACL Rolling Review",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "Call for workshops: EMNLP & AACL",
            "url": "https://groups.google.com/g/ml-news/c/W-fucfhVto4"
          },
          {
            "title": "EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot",
            "url": "https://www.getpaperpilot.com/deadlines/emnlp-2026.html"
          },
          {
            "title": "AI Conference Deadlines",
            "url": "https://mlciv.com/ai-deadlines/"
          }
        ]
      },
      "Now let me search for the author guidelines specifically:",
      {
        "tool_use_id": "srvtoolu_01NcLca82Zw3DSQH4zFwMEog",
        "content": [
          {
            "title": "Call for Main Conference Papers - EMNLP 2026",
            "url": "https://2026.emnlp.org/calls/main_conference_papers/"
          },
          {
            "title": "Submission Guide",
            "url": "https://nlp4climate.github.io/submissionguide/"
          },
          {
            "title": "EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf",
            "url": "https://www.underleaf.ai/templates/emnlp"
          },
          {
            "title": "Submission Checklist for Original, First Time Submissions | Computational Linguistics",
            "url": "https://submissions.cljournal.org/index.php/cljournal/OriginalSubmissionChecklist"
          },
          {
            "title": "LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)",
            "url": "https://linguistlist.org/issues/37/972/"
          },
          {
            "title": "EMNLP 2026 : The 2026 Conference on Empirical Methods in N",
            "url": "https://callforpaper.org/call-for-papers-emnlp-2026"
          },
          {
            "title": "Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"
          },
          {
            "title": "LaTeLL_26_template - Overleaf, Online LaTeX Editor",
            "url": "https://www.overleaf.com/latex/templates/latell-26-template/kfcvbgxmccvb"
          },
          {
            "title": "EMNLP: Empirical Methods in Natural Language Processing Template - ACM Conference",
            "url": "https://scispace.com/formats/acm-conference/emnlp-empirical-methods-in-natural-language-processing/9660af2f47424125a400febdfef4f76f"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review",
            "url": "http://aclrollingreview.org/cfp"
          }
        ]
      },
      "Based on my search results, here's the comprehensive information about EMNLP 2026 ARR call for papers:\n\n## EMNLP 2026 ARR Call for Papers - Key Information\n\n### Submission Deadline\nThe ARR submission deadline is May 25, 2026.\n\n### Important Dates\n- Reviewer registration deadline for ALL authors: May 27, 2026\n- Author response and author-reviewer discussion: July 7 - July 13, 2026\n- Meta review released: July 30, 2026\n- EMNLP commitment deadline: August 2, 2026\n- Notification of acceptance (long & short papers): August 20, 2026\n- Camera-ready papers due: September 20, 2026\n\n### Submission Types\nEMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.\n\n### Author Guidelines & Format Requirements\nThe format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. The mandatory Limitations section is required, placed after the conclusion.\n\nEMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences, available at github.com/acl-org/acl-style-files.\n\n### Special Policy for EMNLP 2026\nGiven that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time. This choice will be binding for EMNLP 2026: ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.\n\n### Mandatory Reviewer Registration\nAfter submission, all authors must complete the author registration form by May 27, 2026 EoD AoE.\n\nFor the complete and official details, visit the EMNLP 2026 call for papers page at https://2026.emnlp.org/calls/main_conference_papers/."
    ],
    "durationSeconds": 13.910535483999997
  },
  "sourceToolAssistantUUID": "facbf15e-aaab-4395-82ef-04f64c9641dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-22T13:41:15.661Z_

```json
{
  "parentUuid": "5e7c2fcb-f27a-4902-8594-48ea606955e6",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1afb50f6-37eb-439f-9928-2b14cd3db052",
  "timestamp": "2026-05-22T13:41:15.661Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 37 · 2026-05-22T13:41:25.205Z_

<details><summary>Logged reasoning block</summary>

```text
Great, I now have:

1. Project overview - 14 experiments, 13 successful, 1 failed
2. Paper main.tex - ACL review template, long paper format
3. EMNLP 2026 venue requirements:
   - ARR submission deadline: May 25, 2026
   - Long paper: 8 pages content + unlimited references
   - Double-blind (anonymous)
   - Mandatory Limitations section (doesn't count toward page limit)
   - ACL style template with [review] option
4. Abstract and Introduction read

Now I need to:


Read through the remaining sections of the paper, verify the PDF output exists, check the project configuration for external review settings, and see if there's an existing review issues file to work from.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1afb50f6-37eb-439f-9928-2b14cd3db052",
  "isSidechain": false,
  "requestId": "req_011CbHhjawZAWLgmCx6xMRHN",
  "type": "assistant",
  "uuid": "6fa91351-bb5f-436b-87d8-123a6ab8276d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y4dsySXmb6d31aQhSGZ6LP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2311,
      "cache_creation_input_tokens": 2246,
      "cache_read_input_tokens": 38265,
      "output_tokens": 893,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2246,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2311,
          "output_tokens": 893,
          "cache_read_input_tokens": 38265,
          "cache_creation_input_tokens": 2246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2246
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

_source line 38 · 2026-05-22T13:41:25.483Z_

Venue 信息已确认：EMNLP 2026 via ARR，截止日期 2026-05-25（距今 3 天）。继续读取论文各章节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fa91351-bb5f-436b-87d8-123a6ab8276d",
  "isSidechain": false,
  "requestId": "req_011CbHhjawZAWLgmCx6xMRHN",
  "type": "assistant",
  "uuid": "46683a5a-48c7-49be-a258-8b0a78ae6c24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y4dsySXmb6d31aQhSGZ6LP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2311,
      "cache_creation_input_tokens": 2246,
      "cache_read_input_tokens": 38265,
      "output_tokens": 893,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2246,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2311,
          "output_tokens": 893,
          "cache_read_input_tokens": 38265,
          "cache_creation_input_tokens": 2246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2246
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

_source line 39 · 2026-05-22T13:41:28.016Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PpRin86dNyr1vN1xVev3DK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46683a5a-48c7-49be-a258-8b0a78ae6c24",
  "isSidechain": false,
  "requestId": "req_011CbHhjawZAWLgmCx6xMRHN",
  "type": "assistant",
  "uuid": "8334918c-e844-4162-b737-d48cf65d2e29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y4dsySXmb6d31aQhSGZ6LP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2311,
      "cache_creation_input_tokens": 2246,
      "cache_read_input_tokens": 38265,
      "output_tokens": 893,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2246,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2311,
          "output_tokens": 893,
          "cache_read_input_tokens": 38265,
          "cache_creation_input_tokens": 2246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2246
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

_source line 40 · 2026-05-22T13:41:28.023Z_

<details><summary>↩ Tool result · `toolu_01PpRin86dNyr1vN1xVev3DK`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Measurement error in causal inference.}
5	The statistical foundations are established in \citet{carroll2006} and \citet{gustafson2004}, with starred-node DAGs formalized by \citet{hernan_cole2009}. For binary variables, non-differential misclassification biases toward the null~\cite{brenner1993, ogburn_vanderweele2012}, but \citet{dosemeci1990} and \citet{jurek2005} showed this fails for polytomous exposures. \citet{veirod_laake2001} derived multi-category bias expressions for Poisson regression, and \citet{edwards_lessler_naimi2021} showed dependent misclassification can bias in either direction. All of these works analyze a single DAG topology; our taxonomy is the first to characterize how the \emph{same} confusion matrix produces qualitatively different bias across seven topologies.
6	
7	\paragraph{Text classifiers and LLM annotation.}
8	\citet{grimmer2022} provide the foundation for text-as-data; \citet{feder_etal2022} offer a comprehensive taxonomy of causal inference in NLP, categorizing text-as-treatment and text-as-confounder paradigms. \citet{wood_doughty2018} first applied DAG reasoning to classifier error. \citet{teblunthuis2024} gave the most complete binary treatment (four DAG scenarios, $K{=}2$), and \citet{lee_wood_doughty2024} extended to categorical LLM classifiers but covered only confounding. On annotation quality, \citet{baumann2025} found 31\% incorrect conclusions with LLM labels, \citet{cheng_mayya_sedoc2024} propose structured approaches to reduce LLM measurement error, and \citet{kim_garg2025} showed 60\% error correlation across models. \citet{audinet2025} benchmark debiasing methods for LLM-generated parameter estimates; \citet{keith_jensen_oconnor2020} survey the broader text-and-causal-inference landscape. These works either restrict to binary labels, cover a single topology, or diagnose quality without connecting it to causal validity. Our framework provides the missing link.
9	
10	\paragraph{Sensitivity analysis and correction methods.}
11	Our ASV framework draws on E-values for unmeasured confounding~\cite{vanderweele_ding2017} and probabilistic bias analysis~\cite{lash2009}. Unlike E-values, ASVs comprise three types (magnitude, significance, sign-flip) because failure modes are topology-dependent; unlike PBA, ASVs provide monotonicity guarantees over $K{\times}K$ matrices. For correction, PPI++~\cite{angelopoulos2023} and DSL~\cite{egami_hinck_stewart_wei2023} are designed as topology-agnostic; \citet{zrnic_candes2024} extend PPI to gold-free cross-prediction settings, and \citet{gligoric2025} leverage LLM confidence scores for inference. Our contribution reveals that this agnosticism is costly: correction effectiveness is itself topology-dependent, with matrix-based methods provably ineffective for four topologies.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8334918c-e844-4162-b737-d48cf65d2e29",
  "isSidechain": false,
  "promptId": "e832977f-06f5-437f-9468-12b340b28a19",
  "type": "user",
  "uuid": "88907bed-a330-41c9-bc62-897d5a90dc64",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Measurement error in causal inference.}\nThe statistical foundations are established in \\citet{carroll2006} and \\citet{gustafson2004}, with starred-node DAGs formalized by \\citet{hernan_cole2009}. For binary variables, non-differential misclassification biases toward the null~\\cite{brenner1993, ogburn_vanderweele2012}, but \\citet{dosemeci1990} and \\citet{jurek2005} showed this fails for polytomous exposures. \\citet{veirod_laake2001} derived multi-category bias expressions for Poisson regression, and \\citet{edwards_lessler_naimi2021} showed dependent misclassification can bias in either direction. All of these works analyze a single DAG topology; our taxonomy is the first to characterize how the \\emph{same} confusion matrix produces qualitatively different bias across seven topologies.\n\n\\paragraph{Text classifiers and LLM annotation.}\n\\citet{grimmer2022} provide the foundation for text-as-data; \\citet{feder_etal2022} offer a comprehensive taxonomy of causal inference in NLP, categorizing text-as-treatment and text-as-confounder paradigms. \\citet{wood_doughty2018} first applied DAG reasoning to classifier error. \\citet{teblunthuis2024} gave the most complete binary treatment (four DAG scenarios, $K{=}2$), and \\citet{lee_wood_doughty2024} extended to categorical LLM classifiers but covered only confounding. On annotation quality, \\citet{baumann2025} found 31\\% incorrect conclusions with LLM labels, \\citet{cheng_mayya_sedoc2024} propose structured approaches to reduce LLM measurement error, and \\citet{kim_garg2025} showed 60\\% error correlation across models. \\citet{audinet2025} benchmark debiasing methods for LLM-generated parameter estimates; \\citet{keith_jensen_oconnor2020} survey the broader text-and-causal-inference landscape. These works either restrict to binary labels, cover a single topology, or diagnose quality without connecting it to causal validity. Our framework provides the missing link.\n\n\\paragraph{Sensitivity analysis and correction methods.}\nOur ASV framework draws on E-values for unmeasured confounding~\\cite{vanderweele_ding2017} and probabilistic bias analysis~\\cite{lash2009}. Unlike E-values, ASVs comprise three types (magnitude, significance, sign-flip) because failure modes are topology-dependent; unlike PBA, ASVs provide monotonicity guarantees over $K{\\times}K$ matrices. For correction, PPI++~\\cite{angelopoulos2023} and DSL~\\cite{egami_hinck_stewart_wei2023} are designed as topology-agnostic; \\citet{zrnic_candes2024} extend PPI to gold-free cross-prediction settings, and \\citet{gligoric2025} leverage LLM confidence scores for inference. Our contribution reveals that this agnosticism is costly: correction effectiveness is itself topology-dependent, with matrix-based methods provably ineffective for four topologies.\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  },
  "sourceToolAssistantUUID": "8334918c-e844-4162-b737-d48cf65d2e29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-22T13:41:28.048Z_

<details open><summary>🔧 Tool call — Read · `toolu_01K67whditGtUSwdxFVaQa72`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88907bed-a330-41c9-bc62-897d5a90dc64",
  "isSidechain": false,
  "requestId": "req_011CbHhjawZAWLgmCx6xMRHN",
  "type": "assistant",
  "uuid": "58b89507-fb9d-428d-9e36-141ab083199b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y4dsySXmb6d31aQhSGZ6LP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2311,
      "cache_creation_input_tokens": 2246,
      "cache_read_input_tokens": 38265,
      "output_tokens": 893,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2246,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2311,
          "output_tokens": 893,
          "cache_read_input_tokens": 38265,
          "cache_creation_input_tokens": 2246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2246
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

_source line 42 · 2026-05-22T13:41:28.053Z_

<details><summary>↩ Tool result · `toolu_01K67whditGtUSwdxFVaQa72`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one. Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\begin{definition}[Non-differential misclassification]
10	\label{def:nondiff}
11	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
12	\end{definition}
13	
14	We study seven canonical DAG topologies (Figure~\ref{fig:dag_taxonomy})~\cite{pearl2009} in which $A$ occupies structurally distinct causal roles: confounder, exposure, mediator, collider, M-bias variable, front-door mediator, and instrument. Each role induces a different functional relationship between $C$ and the probability limit of the standard causal estimator, yielding topology-dependent bias.
15	
16	\subsection{Multi-Class Bias Expressions}
17	\label{sec:bias_expressions}
18	
19	For each topology, we derive the probability limit of the naive estimator that substitutes $A^*$ for $A$. Let $\tau$ denote the target causal parameter and $\hat{\tau}(A^*)$ the estimator using misclassified annotations.
20	
21	\paragraph{Confounding ($A$ = confounder).}
22	When $A$ confounds the $X{\to}Y$ relationship, the OLS estimator controlling for $A^*$ has probability limit
23	\begin{equation}
24	\label{eq:confounding}
25	\text{plim}\;\hat{\tau}(A^*) = \bigl(\mathbb{E}[Z^{\prime}Z]\bigr)^{-1}\mathbb{E}[Z^{\prime}X]\,\boldsymbol{\beta},
26	\end{equation}
27	where $Z = [X, \text{dummies}(A^*)]$, $\boldsymbol{\beta}$ contains the true coefficients, and the target parameter $\tau$ is the coefficient on $X$. Misclassification produces residual confounding that monotonically approaches the omitted variable bias, but the sign of $\hat{\tau}$ is preserved: $\tau_{\text{sign\_flip}} = 0$ structurally.\footnote{This result is consistent with \citet{brenner1993}, who showed that the adjusted estimate with misclassified polytomous confounders can be biased toward or away from the null. Both findings hold simultaneously: misclassification degrades confounding control, producing residual bias whose magnitude can exceed the correctly adjusted estimate (amplification), but the treatment effect sign is never reversed. The distinction is between \emph{sign reversal} ($\text{sign}(\hat{\tau}) \neq \text{sign}(\tau)$, which we show never occurs) and \emph{amplification} ($|\hat{\tau}| > |\tau|$, which occurs universally in this topology).}
28	
29	\paragraph{Exposure ($A$ = treatment variable).}
30	When $A$ is the exposure of interest, the biased coefficient for category $j$ becomes a weighted combination of true coefficients:
31	\begin{equation}
32	\label{eq:exposure}
33	\text{plim}\;\hat{\beta}_j(A^*) = \sum_{k=1}^{K} w_{jk}\,\beta_k,
34	\end{equation}
35	where $w_{jk}$ depends on the confusion matrix $C$ and the marginal distribution of $A$. Unlike the binary case, where non-differential misclassification guarantees attenuation toward the null~\cite{brenner1993}, the $K{\geq}3$ case permits $w_{jk}$ to assign negative weight to categories with opposite-sign coefficients, producing \emph{sign reversal}. A near-permutation confusion matrix effectively swaps category labels, making sign reversal the dominant outcome (83.4\% under uniform Dirichlet prior). This failure mode is structurally impossible at $K{=}2$ because a $2{\times}2$ stochastic matrix with positive diagonal cannot reverse the sign of a single coefficient.
36	
37	\paragraph{Mediation ($A$ = mediator).}
38	When $A$ mediates the $X{\to}Y$ relationship, the direct effect estimator controlling for $A^*$ has probability limit
39	\begin{equation}
40	\label{eq:mediation}
41	\text{plim}\;\hat{\tau}_{\text{direct}}(A^*) = \tau_{\text{direct}} + \bigl(1 - \lambda(C)\bigr)\,\tau_{\text{indirect}},
42	\end{equation}
43	where $\lambda(C) \in [0,1]$ summarizes attenuation (Appendix~\ref{app:proof}, Proposition~3), with $\lambda(I) = 1$ under perfect classification. Misclassification ($\lambda < 1$) causes the residual indirect effect to be absorbed into the direct path estimate, producing upward bias in $|\hat{\tau}_{\text{direct}}|$ but preserving the sign ($\tau_{\text{sign\_flip}} = 0$).
44	
45	\paragraph{Collider ($A$ = collider, conditioned on $A^*$).}
46	Conditioning on a collider $A$ of $X$ and $Y$ opens a spurious path. When we condition on $A^*$ instead, misclassification attenuates this spurious association because $A^*$ is a noisy proxy for $A$. The collider topology thus exhibits a \emph{protective} property: annotation error reduces rather than amplifies the bias from collider stratification, with $\tau_{\text{sign\_flip}} = 0$.
47	
48	\paragraph{M-bias ($A$ = intermediate collider).}
49	In the M-shaped DAG ($U_1 \to X$, $U_1 \to A$, $U_2 \to A$, $U_2 \to Y$, $X \to Y$), adjusting for $A$ introduces a small spurious association via the M-bias path~\cite{greenland2003}. Misclassifying $A$ weakens this adjustment, reducing the M-bias. This topology is \emph{immune}: $\hat{\tau}(A^*)$ is closer to $\tau$ than $\hat{\tau}(A)$ for all non-trivial confusion matrices, yielding $\text{ASV} = \infty$.
50	
51	\paragraph{Front-door ($A$ = front-door mediator).}
52	In the front-door DAG ($X \to A \to Y$ with unmeasured $U \to X$, $U \to Y$), the front-door estimator~\cite{bellemare_bloem2024} uses $A$ to identify effects despite unmeasured confounding. Misclassification attenuates both $X \to A$ and $A \to Y$ relationships, producing moderate bias with $\tau_{\text{sign\_flip}} = 0$.
53	
54	\paragraph{Instrumental variable ($A$ = instrument).}
55	The Wald estimator~\cite{angrist_imbens1995} $\hat{\tau}_{\text{IV}} = \hat{\text{cov}}(A^*, Y) / \hat{\text{cov}}(A^*, X)$ has $C$ in the denominator. Misclassification can drive first-stage coefficients toward zero or reverse their sign, causing the ratio estimator to diverge or flip. Under random Dirichlet matrices, 52.6\% produce sign reversal, making IV the most fragile topology.
56	
57	\paragraph{Structural sign-flip guarantee.}
58	\begin{proposition}[Sign preservation---analytic results]
59	\label{prop:signflip}
60	Under non-differential misclassification with $C_{kk} > 0$ for all $k$:
61	\emph{(a)}~Confounding preserves sign when $\operatorname{sign}(\tau) = \operatorname{sign}(\tau {+} B_{\mathrm{OV}})$, where $B_{\mathrm{OV}} {=} \operatorname{Cov}(g(A),f(A))/\operatorname{Var}(T)$ is the omitted-variable bias (Cauchy--Schwarz; Appendix~\ref{app:confounding}).
62	\emph{(b)}~Collider preserves sign when $|\tau| > \sqrt{\operatorname{Var}(g)\operatorname{Var}(h)}/\mathbb{E}[\operatorname{Var}(T{\mid}A)]$ (Berkson attenuation; Appendix~\ref{app:collider}).
63	\emph{(c)}~Exposure can produce sign reversal for $K {\geq} 3$, even with $C_{kk} {>} 0.5$ (counterexample in Appendix~\ref{app:exposure}).
64	\end{proposition}
65	
66	\paragraph{Empirical Finding 1} (Mediation, M-bias, front-door).
67	Sign preservation holds under topology-specific conditions: mediation requires $\operatorname{sign}(\tau_{\mathrm{dir}}) {=} \operatorname{sign}(\tau_{\mathrm{total}})$; front-door requires $\operatorname{sign}(\lambda\alpha_U) {=} \operatorname{sign}(\lambda\alpha_U {+} \operatorname{Cov}(T,f(A)))$; M-bias is attenuating for all $C$. Verified across 100{,}000 random matrices with zero violations (Appendix~\ref{app:conditions}); analytic proofs for general $K$ remain open.
68	
69	These conditions involve true DGP parameters, which in practice must be estimated. The ASV framework (§\ref{sec:asv}) provides a complementary assessment that does not require knowledge of the exact sufficient conditions.
70	
71	\subsection{Annotation Sensitivity Values}
72	\label{sec:asv}
73	
74	We introduce Annotation Sensitivity Values (ASVs) as a unified sensitivity analysis framework, analogous to E-values for unmeasured confounding~\cite{vanderweele_ding2017} but designed for annotation-induced bias.
75	
76	\paragraph{Parameterization.}
77	We parameterize the confusion matrix as $C(\delta) = (1{-}\delta)I + \delta C_0$, where $C_0$ is a reference confusion matrix (e.g., estimated from a validation set) and $\delta \geq 0$ controls the severity of misclassification. At $\delta{=}0$, classification is perfect; at $\delta{=}1$, classification matches $C_0$. Non-negativity of $C(\delta)$ requires $\delta \leq \delta_{\max} = \min_j \frac{1}{1 - (C_0)_{jj}}$. Since $(C_0)_{jj} \in [0,1]$, we have $\delta_{\max} \geq 1$ for all valid $C_0$, ensuring the full range $[0,1]$ is always feasible; all ASV computations are constrained to $[0, \delta_{\max}]$. In practice, $C_0$ is estimated from a finite validation set and subject to sampling uncertainty; we recommend bootstrapping $C_0$ and reporting ASV confidence intervals.
78	
79	\paragraph{Three ASV types.}
80	We define three complementary measures: (1)~\textbf{Magnitude ASV} $\delta^*_{\text{mag}} = \min\{\delta : |\text{plim}\;\hat{\tau}(C(\delta)) - \tau| > \epsilon\}$---analogous to E-values; (2)~\textbf{Significance ASV} $\delta^*_{\text{sig}} = \min\{\delta : |\text{plim}\;\hat{\tau}(C(\delta))| < z_{\alpha/2} \cdot SE(N)\}$---relevant for attenuating topologies; (3)~\textbf{Sign-flip ASV} $\delta^*_{\text{sf}} = \min\{\delta : \text{sign}(\hat{\tau}) \neq \text{sign}(\tau)\}$---exposure and IV only. The significance ASV depends on $N$ through $SE(N)$, exhibiting a sharp phase transition at a critical $N^*$ below which all rejections are blocked.
81	
82	\begin{theorem}[Envelope monotonicity---confounding, proportional effects]
83	\label{thm:monotone}
84	For the confounding topology with proportional effects ($f = \lambda g$ for some scalar $\lambda$) under $C(\delta) = (1{-}\delta)I + \delta C_0$, $|B(C(\delta))|$ is monotonically non-decreasing in $\delta \in [0, \delta_{\max}]$.
85	\end{theorem}
86	
87	\emph{Proof sketch.} $B(C(\delta)) {=} \lambda V_W(\delta)/(V_W(\delta) {+} \sigma_T^2)$ where $V_W(\delta) {=} \operatorname{Var}(g) {-} \operatorname{Var}(\mathbb{E}[g{\mid}A^*_\delta])$. As $\delta$ increases, $A^*$ becomes a noisier channel for $A$, so $\operatorname{Var}(\mathbb{E}[g{\mid}A^*_\delta])$ decreases by the data processing inequality, increasing $V_W$. Since $x/(x{+}c)$ is increasing for $c{>}0$, $|B|$ is non-decreasing (full proof in Appendix~\ref{app:monotonicity_proof}). For general (non-proportional) effects, numerical verification across 10{,}000 random matrices confirms $\varepsilon$-approximate monotonicity with $\varepsilon < 0.02$ (Appendix~\ref{app:monotonicity_proof}).
88	
89	\begin{conjecture}[$\varepsilon$-approximate envelope monotonicity]
90	\label{conj:monotone}
91	For the six non-IV topologies under $C(\delta) = (1{-}\delta)I + \delta C_0$: exposure, mediation, and front-door are $\varepsilon$-approximately non-decreasing in $\delta$, and collider and M-bias (protective topologies) are $\varepsilon$-approximately non-increasing in $\delta$, with $\varepsilon < 0.06$ ($<$6\% of $\tau$). Verified across 10{,}000 random matrices per topology and $K \in \{3,5,7\}$ using analytic probability limits (Appendix~\ref{sec:conjecture_verify}).
92	\end{conjecture}
93	
94	The instrumental variable topology is excluded from Conjecture~\ref{conj:monotone}: the Wald estimator $\hat{\tau} = \hat{\gamma}_{Y{\sim}A^*} / \hat{\gamma}_{T{\sim}A^*}$ exhibits singularities when the first-stage coefficient passes through zero as $\delta$ increases, producing unbounded deviations ($>10^6$). This is a property of the Wald estimator itself, not of the ASV framework; magnitude ASV remains well-defined for IV away from first-stage singularities.
95	
96	Binarization of $K{=}3$ annotations introduces additional topology-dependent bias (Appendix~\ref{app:binarization}).
97	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58b89507-fb9d-428d-9e36-141ab083199b",
  "isSidechain": false,
  "promptId": "e832977f-06f5-437f-9468-12b340b28a19",
  "type": "user",
  "uuid": "aca91a35-ab36-4da8-aa4a-0bcbae3ad833",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Setup and Notation}\n\\label{sec:notation}\n\nLet $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \\mid A{=}k)$, where each column sums to one. Following \\citet{hernan_cole2009}, we represent this measurement process using \\emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.\n\n\\begin{definition}[Non-differential misclassification]\n\\label{def:nondiff}\nMisclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\\mathbf{Z}$ if $P(A^*{=}j \\mid A{=}k, Y, \\mathbf{Z}) = P(A^*{=}j \\mid A{=}k) = C_{jk}$ for all $j,k$.\n\\end{definition}\n\nWe study seven canonical DAG topologies (Figure~\\ref{fig:dag_taxonomy})~\\cite{pearl2009} in which $A$ occupies structurally distinct causal roles: confounder, exposure, mediator, collider, M-bias variable, front-door mediator, and instrument. Each role induces a different functional relationship between $C$ and the probability limit of the standard causal estimator, yielding topology-dependent bias.\n\n\\subsection{Multi-Class Bias Expressions}\n\\label{sec:bias_expressions}\n\nFor each topology, we derive the probability limit of the naive estimator that substitutes $A^*$ for $A$. Let $\\tau$ denote the target causal parameter and $\\hat{\\tau}(A^*)$ the estimator using misclassified annotations.\n\n\\paragraph{Confounding ($A$ = confounder).}\nWhen $A$ confounds the $X{\\to}Y$ relationship, the OLS estimator controlling for $A^*$ has probability limit\n\\begin{equation}\n\\label{eq:confounding}\n\\text{plim}\\;\\hat{\\tau}(A^*) = \\bigl(\\mathbb{E}[Z^{\\prime}Z]\\bigr)^{-1}\\mathbb{E}[Z^{\\prime}X]\\,\\boldsymbol{\\beta},\n\\end{equation}\nwhere $Z = [X, \\text{dummies}(A^*)]$, $\\boldsymbol{\\beta}$ contains the true coefficients, and the target parameter $\\tau$ is the coefficient on $X$. Misclassification produces residual confounding that monotonically approaches the omitted variable bias, but the sign of $\\hat{\\tau}$ is preserved: $\\tau_{\\text{sign\\_flip}} = 0$ structurally.\\footnote{This result is consistent with \\citet{brenner1993}, who showed that the adjusted estimate with misclassified polytomous confounders can be biased toward or away from the null. Both findings hold simultaneously: misclassification degrades confounding control, producing residual bias whose magnitude can exceed the correctly adjusted estimate (amplification), but the treatment effect sign is never reversed. The distinction is between \\emph{sign reversal} ($\\text{sign}(\\hat{\\tau}) \\neq \\text{sign}(\\tau)$, which we show never occurs) and \\emph{amplification} ($|\\hat{\\tau}| > |\\tau|$, which occurs universally in this topology).}\n\n\\paragraph{Exposure ($A$ = treatment variable).}\nWhen $A$ is the exposure of interest, the biased coefficient for category $j$ becomes a weighted combination of true coefficients:\n\\begin{equation}\n\\label{eq:exposure}\n\\text{plim}\\;\\hat{\\beta}_j(A^*) = \\sum_{k=1}^{K} w_{jk}\\,\\beta_k,\n\\end{equation}\nwhere $w_{jk}$ depends on the confusion matrix $C$ and the marginal distribution of $A$. Unlike the binary case, where non-differential misclassification guarantees attenuation toward the null~\\cite{brenner1993}, the $K{\\geq}3$ case permits $w_{jk}$ to assign negative weight to categories with opposite-sign coefficients, producing \\emph{sign reversal}. A near-permutation confusion matrix effectively swaps category labels, making sign reversal the dominant outcome (83.4\\% under uniform Dirichlet prior). This failure mode is structurally impossible at $K{=}2$ because a $2{\\times}2$ stochastic matrix with positive diagonal cannot reverse the sign of a single coefficient.\n\n\\paragraph{Mediation ($A$ = mediator).}\nWhen $A$ mediates the $X{\\to}Y$ relationship, the direct effect estimator controlling for $A^*$ has probability limit\n\\begin{equation}\n\\label{eq:mediation}\n\\text{plim}\\;\\hat{\\tau}_{\\text{direct}}(A^*) = \\tau_{\\text{direct}} + \\bigl(1 - \\lambda(C)\\bigr)\\,\\tau_{\\text{indirect}},\n\\end{equation}\nwhere $\\lambda(C) \\in [0,1]$ summarizes attenuation (Appendix~\\ref{app:proof}, Proposition~3), with $\\lambda(I) = 1$ under perfect classification. Misclassification ($\\lambda < 1$) causes the residual indirect effect to be absorbed into the direct path estimate, producing upward bias in $|\\hat{\\tau}_{\\text{direct}}|$ but preserving the sign ($\\tau_{\\text{sign\\_flip}} = 0$).\n\n\\paragraph{Collider ($A$ = collider, conditioned on $A^*$).}\nConditioning on a collider $A$ of $X$ and $Y$ opens a spurious path. When we condition on $A^*$ instead, misclassification attenuates this spurious association because $A^*$ is a noisy proxy for $A$. The collider topology thus exhibits a \\emph{protective} property: annotation error reduces rather than amplifies the bias from collider stratification, with $\\tau_{\\text{sign\\_flip}} = 0$.\n\n\\paragraph{M-bias ($A$ = intermediate collider).}\nIn the M-shaped DAG ($U_1 \\to X$, $U_1 \\to A$, $U_2 \\to A$, $U_2 \\to Y$, $X \\to Y$), adjusting for $A$ introduces a small spurious association via the M-bias path~\\cite{greenland2003}. Misclassifying $A$ weakens this adjustment, reducing the M-bias. This topology is \\emph{immune}: $\\hat{\\tau}(A^*)$ is closer to $\\tau$ than $\\hat{\\tau}(A)$ for all non-trivial confusion matrices, yielding $\\text{ASV} = \\infty$.\n\n\\paragraph{Front-door ($A$ = front-door mediator).}\nIn the front-door DAG ($X \\to A \\to Y$ with unmeasured $U \\to X$, $U \\to Y$), the front-door estimator~\\cite{bellemare_bloem2024} uses $A$ to identify effects despite unmeasured confounding. Misclassification attenuates both $X \\to A$ and $A \\to Y$ relationships, producing moderate bias with $\\tau_{\\text{sign\\_flip}} = 0$.\n\n\\paragraph{Instrumental variable ($A$ = instrument).}\nThe Wald estimator~\\cite{angrist_imbens1995} $\\hat{\\tau}_{\\text{IV}} = \\hat{\\text{cov}}(A^*, Y) / \\hat{\\text{cov}}(A^*, X)$ has $C$ in the denominator. Misclassification can drive first-stage coefficients toward zero or reverse their sign, causing the ratio estimator to diverge or flip. Under random Dirichlet matrices, 52.6\\% produce sign reversal, making IV the most fragile topology.\n\n\\paragraph{Structural sign-flip guarantee.}\n\\begin{proposition}[Sign preservation---analytic results]\n\\label{prop:signflip}\nUnder non-differential misclassification with $C_{kk} > 0$ for all $k$:\n\\emph{(a)}~Confounding preserves sign when $\\operatorname{sign}(\\tau) = \\operatorname{sign}(\\tau {+} B_{\\mathrm{OV}})$, where $B_{\\mathrm{OV}} {=} \\operatorname{Cov}(g(A),f(A))/\\operatorname{Var}(T)$ is the omitted-variable bias (Cauchy--Schwarz; Appendix~\\ref{app:confounding}).\n\\emph{(b)}~Collider preserves sign when $|\\tau| > \\sqrt{\\operatorname{Var}(g)\\operatorname{Var}(h)}/\\mathbb{E}[\\operatorname{Var}(T{\\mid}A)]$ (Berkson attenuation; Appendix~\\ref{app:collider}).\n\\emph{(c)}~Exposure can produce sign reversal for $K {\\geq} 3$, even with $C_{kk} {>} 0.5$ (counterexample in Appendix~\\ref{app:exposure}).\n\\end{proposition}\n\n\\paragraph{Empirical Finding 1} (Mediation, M-bias, front-door).\nSign preservation holds under topology-specific conditions: mediation requires $\\operatorname{sign}(\\tau_{\\mathrm{dir}}) {=} \\operatorname{sign}(\\tau_{\\mathrm{total}})$; front-door requires $\\operatorname{sign}(\\lambda\\alpha_U) {=} \\operatorname{sign}(\\lambda\\alpha_U {+} \\operatorname{Cov}(T,f(A)))$; M-bias is attenuating for all $C$. Verified across 100{,}000 random matrices with zero violations (Appendix~\\ref{app:conditions}); analytic proofs for general $K$ remain open.\n\nThese conditions involve true DGP parameters, which in practice must be estimated. The ASV framework (§\\ref{sec:asv}) provides a complementary assessment that does not require knowledge of the exact sufficient conditions.\n\n\\subsection{Annotation Sensitivity Values}\n\\label{sec:asv}\n\nWe introduce Annotation Sensitivity Values (ASVs) as a unified sensitivity analysis framework, analogous to E-values for unmeasured confounding~\\cite{vanderweele_ding2017} but designed for annotation-induced bias.\n\n\\paragraph{Parameterization.}\nWe parameterize the confusion matrix as $C(\\delta) = (1{-}\\delta)I + \\delta C_0$, where $C_0$ is a reference confusion matrix (e.g., estimated from a validation set) and $\\delta \\geq 0$ controls the severity of misclassification. At $\\delta{=}0$, classification is perfect; at $\\delta{=}1$, classification matches $C_0$. Non-negativity of $C(\\delta)$ requires $\\delta \\leq \\delta_{\\max} = \\min_j \\frac{1}{1 - (C_0)_{jj}}$. Since $(C_0)_{jj} \\in [0,1]$, we have $\\delta_{\\max} \\geq 1$ for all valid $C_0$, ensuring the full range $[0,1]$ is always feasible; all ASV computations are constrained to $[0, \\delta_{\\max}]$. In practice, $C_0$ is estimated from a finite validation set and subject to sampling uncertainty; we recommend bootstrapping $C_0$ and reporting ASV confidence intervals.\n\n\\paragraph{Three ASV types.}\nWe define three complementary measures: (1)~\\textbf{Magnitude ASV} $\\delta^*_{\\text{mag}} = \\min\\{\\delta : |\\text{plim}\\;\\hat{\\tau}(C(\\delta)) - \\tau| > \\epsilon\\}$---analogous to E-values; (2)~\\textbf{Significance ASV} $\\delta^*_{\\text{sig}} = \\min\\{\\delta : |\\text{plim}\\;\\hat{\\tau}(C(\\delta))| < z_{\\alpha/2} \\cdot SE(N)\\}$---relevant for attenuating topologies; (3)~\\textbf{Sign-flip ASV} $\\delta^*_{\\text{sf}} = \\min\\{\\delta : \\text{sign}(\\hat{\\tau}) \\neq \\text{sign}(\\tau)\\}$---exposure and IV only. The significance ASV depends on $N$ through $SE(N)$, exhibiting a sharp phase transition at a critical $N^*$ below which all rejections are blocked.\n\n\\begin{theorem}[Envelope monotonicity---confounding, proportional effects]\n\\label{thm:monotone}\nFor the confounding topology with proportional effects ($f = \\lambda g$ for some scalar $\\lambda$) under $C(\\delta) = (1{-}\\delta)I + \\delta C_0$, $|B(C(\\delta))|$ is monotonically non-decreasing in $\\delta \\in [0, \\delta_{\\max}]$.\n\\end{theorem}\n\n\\emph{Proof sketch.} $B(C(\\delta)) {=} \\lambda V_W(\\delta)/(V_W(\\delta) {+} \\sigma_T^2)$ where $V_W(\\delta) {=} \\operatorname{Var}(g) {-} \\operatorname{Var}(\\mathbb{E}[g{\\mid}A^*_\\delta])$. As $\\delta$ increases, $A^*$ becomes a noisier channel for $A$, so $\\operatorname{Var}(\\mathbb{E}[g{\\mid}A^*_\\delta])$ decreases by the data processing inequality, increasing $V_W$. Since $x/(x{+}c)$ is increasing for $c{>}0$, $|B|$ is non-decreasing (full proof in Appendix~\\ref{app:monotonicity_proof}). For general (non-proportional) effects, numerical verification across 10{,}000 random matrices confirms $\\varepsilon$-approximate monotonicity with $\\varepsilon < 0.02$ (Appendix~\\ref{app:monotonicity_proof}).\n\n\\begin{conjecture}[$\\varepsilon$-approximate envelope monotonicity]\n\\label{conj:monotone}\nFor the six non-IV topologies under $C(\\delta) = (1{-}\\delta)I + \\delta C_0$: exposure, mediation, and front-door are $\\varepsilon$-approximately non-decreasing in $\\delta$, and collider and M-bias (protective topologies) are $\\varepsilon$-approximately non-increasing in $\\delta$, with $\\varepsilon < 0.06$ ($<$6\\% of $\\tau$). Verified across 10{,}000 random matrices per topology and $K \\in \\{3,5,7\\}$ using analytic probability limits (Appendix~\\ref{sec:conjecture_verify}).\n\\end{conjecture}\n\nThe instrumental variable topology is excluded from Conjecture~\\ref{conj:monotone}: the Wald estimator $\\hat{\\tau} = \\hat{\\gamma}_{Y{\\sim}A^*} / \\hat{\\gamma}_{T{\\sim}A^*}$ exhibits singularities when the first-stage coefficient passes through zero as $\\delta$ increases, producing unbounded deviations ($>10^6$). This is a property of the Wald estimator itself, not of the ASV framework; magnitude ASV remains well-defined for IV away from first-stage singularities.\n\nBinarization of $K{=}3$ annotations introduces additional topology-dependent bias (Appendix~\\ref{app:binarization}).\n",
      "numLines": 97,
      "startLine": 1,
      "totalLines": 97
    }
  },
  "sourceToolAssistantUUID": "58b89507-fb9d-428d-9e36-141ab083199b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-22T13:41:28.423Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Sj5g23XXCzpLpWEksCLqfA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aca91a35-ab36-4da8-aa4a-0bcbae3ad833",
  "isSidechain": false,
  "requestId": "req_011CbHhjawZAWLgmCx6xMRHN",
  "type": "assistant",
  "uuid": "0b40e1db-e711-46be-9e50-33ac692d6413",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y4dsySXmb6d31aQhSGZ6LP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2311,
      "cache_creation_input_tokens": 2246,
      "cache_read_input_tokens": 38265,
      "output_tokens": 893,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2246,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2311,
          "output_tokens": 893,
          "cache_read_input_tokens": 38265,
          "cache_creation_input_tokens": 2246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2246
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

_source line 44 · 2026-05-22T13:41:28.439Z_

<details><summary>↩ Tool result · `toolu_01Sj5g23XXCzpLpWEksCLqfA`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We validate the bias taxonomy and ASV framework through analytical derivations and Monte Carlo simulation across seven DAG topologies under $K{=}3$ non-differential misclassification.
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	For each of the seven topologies (confounding, exposure, mediation, collider, M-bias, front-door, IV), we sample 100{,}000 confusion matrices from a Dirichlet$(1,1,1)$ prior, compute the analytical probability limit of the causal estimator, and validate against Monte Carlo simulation ($N{=}10{,}000$). ASV experiments use $C(\delta) = (1{-}\delta)I + \delta C_0$.
10	
11	\subsection{Bias Taxonomy}
12	\label{sec:taxonomy_results}
13	
14	\paragraph{Theory-MC agreement.}
15	Analytical probability limits match Monte Carlo estimates with grand MAPE of 2.0\% across 126 scenarios (18 LLM configurations $\times$ 7 topologies, $N{=}10{,}000$). Per-topology MAPE ranges from 0.5\% (confounding) to 5.5\% (IV); the IV maximum reflects the Wald estimator's small-denominator variance amplification.
16	
17	\paragraph{Exposure DAG: catastrophic sign reversal.}
18	Under the full Dirichlet$(1,1,1)$ prior, 85\% of $K{=}3$ confusion matrices produce bias that violates the binary ``toward-null'' guarantee. More critically, 83.4\% of matrices cause \emph{sign reversal} of at least one coefficient. The two failure modes are distinct: for a coefficient with true value $\beta_1{=}1.0$, a near-permutation $C$ produces $\hat{\gamma}_1{=}{-}0.84$ (sign reversal, magnitude $0.84{\times}$); for $\beta_2{=}{-}0.5$, the same $C$ yields $\hat{\gamma}_2{=}{-}1.41$ (same-sign amplification, $2.83{\times}$).
19	
20	This finding persists in practically relevant subspaces. When restricting to confusion matrices with diagonal entries $\geq 0.7$ (typical of current LLM classifiers achieving $F_1 > 0.8$), the violation rate remains 13.7\% with 2.1\% sign reversal and 11.7\% amplification. Even at diagonal $\geq 0.9$, violation persists at 11.9\%. In contrast, the $K{=}2$ control confirms that all six tested binary confusion matrices maintain the classical bias-toward-null guarantee~\cite{brenner1993}, establishing that the multi-class failure is structurally distinct from the binary case.
21	
22	\paragraph{Structural guarantee for non-exposure topologies.}
23	Five of seven topologies exhibit zero sign-flip rate across all sampled matrices (Table~\ref{tab:taxonomy}). Confounding, mediation, and front-door show 100\% violation and amplification but never reverse the sign.\footnote{Consistent with \citet{brenner1993} and \citet{dosemeci1990}: polytomous misclassification can bias \emph{away} from the null (amplification), but our sign-flip metric confirms the effect sign is preserved.} Collider misclassification attenuates the spurious association (protective): the 100\% violation and amplification rates in Table~\ref{tab:taxonomy} reflect the comparison against the unconditional $\tau$, but $|B(C)|$ is approximately \emph{non-increasing} in misclassification severity (worst-case deviation $<$0.005)---conditioning on noisy $A^*$ induces \emph{less} collider bias than conditioning on perfect $A$ (Conjecture~\ref{conj:monotone}). M-bias shows the weakest sensitivity (53.2\% violation, 10.4\% amplification) because error on a collider variable reduces the spurious M-bias path.
24	
25	\paragraph{IV: Wald estimator instability.}
26	The instrumental variable topology is the sole exception among non-exposure DAGs. The Wald estimator's first stage involves $C$ directly in the denominator, and 52.6\% of random confusion matrices cause the denominator to change sign, producing $\tau$-specific sign reversal. This rate remains stable across $K{=}3,5,7$, indicating that IV fragility is a structural property of the Wald estimator rather than a finite-$K$ artifact. Diagonal-dominance subspace analysis (Appendix~\ref{sec:iv_dirichlet_subspace}) reveals that IV sign reversal vanishes at diagonal $\geq 0.5$, but unlike exposure, the violation rate remains at 100\% (pure amplification) even at diagonal $\geq 0.9$.
27	
28	\paragraph{Cross-$K$ robustness.}
29	All structural patterns persist at $K{=}5,7$ (100{,}000 matrices each): sign-flip guarantees hold for the same five topologies, and IV sign-flip rates remain within 51--53\%.
30	
31	\begin{table}[t]
32	\centering
33	\caption{Bias characteristics of $K{=}3$ non-differential misclassification across 7 DAG topologies. Violation: $|\hat{\tau}| > |\tau|$ (bias exceeds true effect); Sign flip: $\text{sign}(\hat{\tau}) \neq \text{sign}(\tau)$; Amplification: $|\hat{\tau}| > |\tau|$ with same sign; $\tau_{\text{sf}}{=}0$?: structural sign-flip guarantee holds (\checkmark) or not (\ding{55}). Rates over 100{,}000 Dirichlet$(1,1,1)$ random confusion matrices.}
34	\label{tab:taxonomy}
35	\small
36	\begin{tabular}{lcccc}
37	\toprule
38	\textbf{Topology} & \textbf{Violation} & \textbf{Sign Flip} & \textbf{Amplif.} & $\tau_{\text{sf}}{=}0$? \\
39	\midrule
40	Confounding & 100\% & 0\% & 100\% & \checkmark \\
41	Exposure & 85\% & 83.4\% & 14.1\% & \ding{55} \\
42	Mediation & 100\% & 0\% & 100\% & \checkmark \\
43	Front-door & 100\% & 0\% & 100\% & \checkmark \\
44	Collider & 100\% & 0\% & 100\% & \checkmark \\
45	M-bias & 53.2\% & 0\% & 10.4\% & \checkmark \\
46	IV & 100\% & 52.6\% & 100\% & \ding{55} \\
47	\bottomrule
48	\end{tabular}
49	\end{table}
50	
51	The bias distributions across topologies are visualized in Figure~\ref{fig:bias_distribution}, where the exposure panel's dominant red region (sign reversal) contrasts with the symmetric attenuation patterns of other topologies.
52	
53	\subsection{ASV Framework Validation}
54	\label{sec:asv_results}
55	
56	\paragraph{Envelope monotonicity.}
57	The ASV envelope (bias magnitude as a function of $\delta$) is $\varepsilon$-approximately monotonic for all six non-IV topologies, with worst-case step deviations below 0.06 ($<$6\% of $\tau$), confirmed by analytic probability limits with zero sampling noise (Appendix~\ref{sec:conjecture_verify}). IV is excluded from Conjecture~\ref{conj:monotone}: the Wald estimator exhibits singularities when the first-stage coefficient passes through zero, producing unbounded deviations. These bounded deviations for non-IV topologies confirm that $\delta$ serves as a meaningful ``dial'' controlling annotation error severity.
58	
59	\paragraph{Magnitude ASV.}
60	Table~\ref{tab:asv_grid} reports magnitude ASV ranges at $\tau{=}0.5$ with a 10\% bias threshold. The ranking from most fragile to most robust is: front-door (0.064--0.387) $<$ mediation (0.076--0.454) $<$ confounding (0.081--0.487) $<$ IV (0.101--0.607) $<$ collider (0.338--2.028) $<$ M-bias ($\infty$). The collider's high ASV reflects its protective nature: misclassification attenuates the spurious association rather than amplifying it. M-bias achieves infinite ASV because annotation error on the collider variable $A$ only reduces the already-small bias from the M-shaped confounding path.
61	
62	\paragraph{Significance and sign-flip ASV.}
63	At $\tau{=}0.05$, significance ASV achieves 100\% power for confounding, front-door, and M-bias, but 0\% for mediation, collider, and IV (correct behavior for attenuating topologies; Type~I error is 0\%). For sign-flip ASV, 83.4\% of exposure reference matrices yield $\tau_{\text{sign\_flip}} < 1$ (catastrophic sensitivity); IV sign-flip ASV ranges 1.1--6.7 (moderate-to-high). The complete ranking (Figure~\ref{fig:asv_ranking}, Table~\ref{tab:asv_grid}, Appendix~\ref{app:supplementary}) confirms IV as maximally fragile and M-bias as immune (ASV $= \infty$).
64	
65	\paragraph{$N$-sensitivity.}
66	The significance ASV exhibits a sharp phase transition at a critical sample size $N^* \approx 6{,}000$--$10{,}000$ (analytically computable per topology), below which all rejections are blocked. Complete ASV values across all topologies and error structures are reported in Appendix~\ref{app:supplementary}.
67	Bootstrap resampling of the confusion matrix ($B{=}1{,}000$; Appendix~\ref{sec:bootstrap_asv}) yields 95\% CIs for magnitude ASV: $\delta^* = 0.94\,[0.60, 1.36]$ (exposure) and $0.75\,[0.44, 1.29]$ (IV), indicating practitioners should account for CM estimation uncertainty.
68	Confounding ASV is consistently the most robust across DGP parameters, but exposure vs.\ IV relative fragility depends on coefficient sign structure (Appendix~\ref{sec:asv_stability}).
69	
70	\subsection{Empirical Validation}
71	\label{sec:empirical}
72	
73	We validate using real LLM confusion matrices from three tasks: HumAID~\cite{alam2021humaid} ($K{=}10$), VAST ($K{=}3$), and CivilComments ($K{=}2$). Four LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat, Qwen2.5-7B-Instruct) produce 23 configurations across the three datasets under zero-shot and few-shot prompting, yielding 161 bias scenarios ($23 \times 7$ topologies).
74	
75	\paragraph{HumAID ($K{=}10$): theory--practice alignment.}
76	The empirical bias ranking matches predictions: IV (12.4--42.1\%), exposure (9.0--17.4\%), mediation/front-door (10.7--14.8\%), while collider, confounding, and M-bias remain below 10\%---consistent with the ASV vulnerability spectrum.
77	
78	\paragraph{Cross-$K$ comparison.}
79	Bias varies substantially across settings: VAST ($K{=}3$) produces 62.8\% mean bias with IV reaching 326\%, versus 12.2\% for HumAID ($K{=}10$) and 32.4\% for CivilComments ($K{=}2$). Even CivilComments configurations with $F_1{=}0.82$ (Qwen3-235B) produce 62--92\% IV bias, confirming that classification accuracy does not predict downstream causal risk (Figure~\ref{fig:f1_vs_bias}).\footnote{VAST's near-degenerate confusion matrices (Neutral-class recall 3.6--16.1\%) drive its extreme IV bias via the Wald estimator's small-denominator amplification.}
80	
81	Checking all $K{-}1$ exposure coefficients, 14 of 23 configurations (61\%) exhibit sign reversal in at least one coefficient---all in the exposure topology, confirming that exposure vulnerability persists at the coefficient level even for diagonally-dominant matrices. For HumAID ($K{=}10$), 7 of 8 configurations reverse a secondary coefficient ($|\beta| \leq 0.2$); for VAST ($K{=}3$), 7 of 8 reverse $\beta_2{=}{-}0.50$. The primary coefficient ($\beta_1$, largest magnitude) never reverses across any empirical configuration; sign flips occur exclusively in secondary coefficients corresponding to rare categories with small $|\beta|$. Sign reversal requires the DGP to contain opposite-sign treatment effects across categories (Equation~\ref{eq:exposure}); when all $\beta_k$ share the same sign, misclassification produces only attenuation. Zero sign reversals occur across 138 non-exposure scenarios ($23 {\times} 6$ topologies), validating the structural guarantee $K$-invariantly. CivilComments ($K{=}2$) confirms the binary algebraic protection. The 7B-to-frontier bias ratio is 1.89, indicating topology rather than model scale determines downstream bias.
82	
83	\paragraph{ASV diagnostic results.}
84	For HumAID ($K{=}10$, 56 scenarios), 55.4\% are flagged as magnitude-ASV-unsafe---IV, mediation, front-door, and exposure all trigger, while confounding, collider, and M-bias remain below 10\% bias (Figure~\ref{fig:asv_heatmap}). For CivilComments ($K{=}2$), 100\% of scenarios are ASV-unsafe despite $F_1$ ranging from $0.69$ (7B) to $0.82$ (frontier).
85	
86	Overlaying all 23 empirical matrices onto the theoretical Dirichlet violation-rate curves (Figure~\ref{fig:dirichlet_overlay}, Appendix~\ref{app:supplementary}) confirms placement: VAST in the danger zone, HumAID mid-range, CivilComments approaching safe for exposure but still in IV amplification.
87	A logistic DGP simulation (Appendix~\ref{sec:logistic_dgp}) confirms that sign-flip patterns are qualitatively preserved under nonlinear models for three representative topologies (confounding, exposure, IV), with treatment-effect sign-flip rate differences $< 2$ percentage points.
88	
89	\begin{figure}[t]
90	\centering
91	\includegraphics[width=\columnwidth]{fig5_f1_vs_bias.pdf}
92	\caption{Topology determines downstream causal bias, not $F_1$. HumAID $K{=}10$ (56 points): within $F_1$ range 0.614--0.690, bias varies $10{\times}$ (IV 42.1\% vs.\ collider $<$5.6\%).}
93	\label{fig:f1_vs_bias}
94	\end{figure}
95	
96	
97	\subsection{Correction Guidance}
98	\label{sec:correction}
99	
100	We evaluate five correction methods (naive plug-in, MLA, DSL~\cite{egami_hinck_stewart_wei2023}, MC-SIMEX, PPI++~\cite{angelopoulos2023}) across all seven topologies under six error structures (210 configurations; full results in Table~\ref{tab:correction}, Appendix~\ref{app:supplementary}).
101	
102	\paragraph{FWL invariance.}
103	For four topologies where $A$ enters as a covariate (confounding, mediation, collider, M-bias), the Frisch--Waugh--Lovell theorem implies that applying $C^{-1}$ to the dummy variables cannot change the $T$ coefficient. Naive plug-in and MLA achieve exactly 0.0\% bias reduction across these four topologies.
104	
105	\paragraph{Method ranking.}
106	Measuring RMSE reduction ($1 - \text{RMSE}_{\text{corr}} / \text{RMSE}_{\text{uncorr}}$), PPI++ achieves the highest grand-mean reduction (47.0\%) but requires gold labels and is catastrophically harmful for M-bias ($-$88.0\%). MC-SIMEX provides gold-free correction (13.3\% grand mean, best for IV at 59.4\%) but harms front-door ($-$62.4\%). DSL corrects confounding (48.0\%) and mediation (52.9\%) but amplifies M-bias ($-$267\%) and IV ($-$206\%). No single method dominates: correction effectiveness is itself topology-dependent. Cross-PPI~\cite{zrnic_candes2024} eliminates the gold-label requirement by using two independent LLM annotators whose predictions serve as mutual references, yielding valid confidence intervals under an annotator-independence assumption. Because it operates on estimator outputs rather than on $C$ directly, Cross-PPI is not subject to FWL invariance and can potentially correct all seven topologies. Methods that bypass FWL through a different route---such as EM imputation of latent true labels and Bayesian measurement error models---offer further alternatives for the four FWL-invariant topologies.
107	
108	Empirical validation on HumAID ($K{=}10$, 30 MC replicates) confirms topology-dependent method superiority: MC-SIMEX outperforms PPI++ in 4 of 7 topologies and reverses from harmful ($K{=}3$) to beneficial ($K{=}10$). A retrospective case study applying the full framework to \citet{lee_wood_doughty2024} is in Appendix~\ref{app:case_study}.
109	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b40e1db-e711-46be-9e50-33ac692d6413",
  "isSidechain": false,
  "promptId": "e832977f-06f5-437f-9468-12b340b28a19",
  "type": "user",
  "uuid": "1464eb78-476c-4bad-8274-828b0708bfc9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe validate the bias taxonomy and ASV framework through analytical derivations and Monte Carlo simulation across seven DAG topologies under $K{=}3$ non-differential misclassification.\n\n\\subsection{Setup}\n\\label{sec:setup}\n\nFor each of the seven topologies (confounding, exposure, mediation, collider, M-bias, front-door, IV), we sample 100{,}000 confusion matrices from a Dirichlet$(1,1,1)$ prior, compute the analytical probability limit of the causal estimator, and validate against Monte Carlo simulation ($N{=}10{,}000$). ASV experiments use $C(\\delta) = (1{-}\\delta)I + \\delta C_0$.\n\n\\subsection{Bias Taxonomy}\n\\label{sec:taxonomy_results}\n\n\\paragraph{Theory-MC agreement.}\nAnalytical probability limits match Monte Carlo estimates with grand MAPE of 2.0\\% across 126 scenarios (18 LLM configurations $\\times$ 7 topologies, $N{=}10{,}000$). Per-topology MAPE ranges from 0.5\\% (confounding) to 5.5\\% (IV); the IV maximum reflects the Wald estimator's small-denominator variance amplification.\n\n\\paragraph{Exposure DAG: catastrophic sign reversal.}\nUnder the full Dirichlet$(1,1,1)$ prior, 85\\% of $K{=}3$ confusion matrices produce bias that violates the binary ``toward-null'' guarantee. More critically, 83.4\\% of matrices cause \\emph{sign reversal} of at least one coefficient. The two failure modes are distinct: for a coefficient with true value $\\beta_1{=}1.0$, a near-permutation $C$ produces $\\hat{\\gamma}_1{=}{-}0.84$ (sign reversal, magnitude $0.84{\\times}$); for $\\beta_2{=}{-}0.5$, the same $C$ yields $\\hat{\\gamma}_2{=}{-}1.41$ (same-sign amplification, $2.83{\\times}$).\n\nThis finding persists in practically relevant subspaces. When restricting to confusion matrices with diagonal entries $\\geq 0.7$ (typical of current LLM classifiers achieving $F_1 > 0.8$), the violation rate remains 13.7\\% with 2.1\\% sign reversal and 11.7\\% amplification. Even at diagonal $\\geq 0.9$, violation persists at 11.9\\%. In contrast, the $K{=}2$ control confirms that all six tested binary confusion matrices maintain the classical bias-toward-null guarantee~\\cite{brenner1993}, establishing that the multi-class failure is structurally distinct from the binary case.\n\n\\paragraph{Structural guarantee for non-exposure topologies.}\nFive of seven topologies exhibit zero sign-flip rate across all sampled matrices (Table~\\ref{tab:taxonomy}). Confounding, mediation, and front-door show 100\\% violation and amplification but never reverse the sign.\\footnote{Consistent with \\citet{brenner1993} and \\citet{dosemeci1990}: polytomous misclassification can bias \\emph{away} from the null (amplification), but our sign-flip metric confirms the effect sign is preserved.} Collider misclassification attenuates the spurious association (protective): the 100\\% violation and amplification rates in Table~\\ref{tab:taxonomy} reflect the comparison against the unconditional $\\tau$, but $|B(C)|$ is approximately \\emph{non-increasing} in misclassification severity (worst-case deviation $<$0.005)---conditioning on noisy $A^*$ induces \\emph{less} collider bias than conditioning on perfect $A$ (Conjecture~\\ref{conj:monotone}). M-bias shows the weakest sensitivity (53.2\\% violation, 10.4\\% amplification) because error on a collider variable reduces the spurious M-bias path.\n\n\\paragraph{IV: Wald estimator instability.}\nThe instrumental variable topology is the sole exception among non-exposure DAGs. The Wald estimator's first stage involves $C$ directly in the denominator, and 52.6\\% of random confusion matrices cause the denominator to change sign, producing $\\tau$-specific sign reversal. This rate remains stable across $K{=}3,5,7$, indicating that IV fragility is a structural property of the Wald estimator rather than a finite-$K$ artifact. Diagonal-dominance subspace analysis (Appendix~\\ref{sec:iv_dirichlet_subspace}) reveals that IV sign reversal vanishes at diagonal $\\geq 0.5$, but unlike exposure, the violation rate remains at 100\\% (pure amplification) even at diagonal $\\geq 0.9$.\n\n\\paragraph{Cross-$K$ robustness.}\nAll structural patterns persist at $K{=}5,7$ (100{,}000 matrices each): sign-flip guarantees hold for the same five topologies, and IV sign-flip rates remain within 51--53\\%.\n\n\\begin{table}[t]\n\\centering\n\\caption{Bias characteristics of $K{=}3$ non-differential misclassification across 7 DAG topologies. Violation: $|\\hat{\\tau}| > |\\tau|$ (bias exceeds true effect); Sign flip: $\\text{sign}(\\hat{\\tau}) \\neq \\text{sign}(\\tau)$; Amplification: $|\\hat{\\tau}| > |\\tau|$ with same sign; $\\tau_{\\text{sf}}{=}0$?: structural sign-flip guarantee holds (\\checkmark) or not (\\ding{55}). Rates over 100{,}000 Dirichlet$(1,1,1)$ random confusion matrices.}\n\\label{tab:taxonomy}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Topology} & \\textbf{Violation} & \\textbf{Sign Flip} & \\textbf{Amplif.} & $\\tau_{\\text{sf}}{=}0$? \\\\\n\\midrule\nConfounding & 100\\% & 0\\% & 100\\% & \\checkmark \\\\\nExposure & 85\\% & 83.4\\% & 14.1\\% & \\ding{55} \\\\\nMediation & 100\\% & 0\\% & 100\\% & \\checkmark \\\\\nFront-door & 100\\% & 0\\% & 100\\% & \\checkmark \\\\\nCollider & 100\\% & 0\\% & 100\\% & \\checkmark \\\\\nM-bias & 53.2\\% & 0\\% & 10.4\\% & \\checkmark \\\\\nIV & 100\\% & 52.6\\% & 100\\% & \\ding{55} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe bias distributions across topologies are visualized in Figure~\\ref{fig:bias_distribution}, where the exposure panel's dominant red region (sign reversal) contrasts with the symmetric attenuation patterns of other topologies.\n\n\\subsection{ASV Framework Validation}\n\\label{sec:asv_results}\n\n\\paragraph{Envelope monotonicity.}\nThe ASV envelope (bias magnitude as a function of $\\delta$) is $\\varepsilon$-approximately monotonic for all six non-IV topologies, with worst-case step deviations below 0.06 ($<$6\\% of $\\tau$), confirmed by analytic probability limits with zero sampling noise (Appendix~\\ref{sec:conjecture_verify}). IV is excluded from Conjecture~\\ref{conj:monotone}: the Wald estimator exhibits singularities when the first-stage coefficient passes through zero, producing unbounded deviations. These bounded deviations for non-IV topologies confirm that $\\delta$ serves as a meaningful ``dial'' controlling annotation error severity.\n\n\\paragraph{Magnitude ASV.}\nTable~\\ref{tab:asv_grid} reports magnitude ASV ranges at $\\tau{=}0.5$ with a 10\\% bias threshold. The ranking from most fragile to most robust is: front-door (0.064--0.387) $<$ mediation (0.076--0.454) $<$ confounding (0.081--0.487) $<$ IV (0.101--0.607) $<$ collider (0.338--2.028) $<$ M-bias ($\\infty$). The collider's high ASV reflects its protective nature: misclassification attenuates the spurious association rather than amplifying it. M-bias achieves infinite ASV because annotation error on the collider variable $A$ only reduces the already-small bias from the M-shaped confounding path.\n\n\\paragraph{Significance and sign-flip ASV.}\nAt $\\tau{=}0.05$, significance ASV achieves 100\\% power for confounding, front-door, and M-bias, but 0\\% for mediation, collider, and IV (correct behavior for attenuating topologies; Type~I error is 0\\%). For sign-flip ASV, 83.4\\% of exposure reference matrices yield $\\tau_{\\text{sign\\_flip}} < 1$ (catastrophic sensitivity); IV sign-flip ASV ranges 1.1--6.7 (moderate-to-high). The complete ranking (Figure~\\ref{fig:asv_ranking}, Table~\\ref{tab:asv_grid}, Appendix~\\ref{app:supplementary}) confirms IV as maximally fragile and M-bias as immune (ASV $= \\infty$).\n\n\\paragraph{$N$-sensitivity.}\nThe significance ASV exhibits a sharp phase transition at a critical sample size $N^* \\approx 6{,}000$--$10{,}000$ (analytically computable per topology), below which all rejections are blocked. Complete ASV values across all topologies and error structures are reported in Appendix~\\ref{app:supplementary}.\nBootstrap resampling of the confusion matrix ($B{=}1{,}000$; Appendix~\\ref{sec:bootstrap_asv}) yields 95\\% CIs for magnitude ASV: $\\delta^* = 0.94\\,[0.60, 1.36]$ (exposure) and $0.75\\,[0.44, 1.29]$ (IV), indicating practitioners should account for CM estimation uncertainty.\nConfounding ASV is consistently the most robust across DGP parameters, but exposure vs.\\ IV relative fragility depends on coefficient sign structure (Appendix~\\ref{sec:asv_stability}).\n\n\\subsection{Empirical Validation}\n\\label{sec:empirical}\n\nWe validate using real LLM confusion matrices from three tasks: HumAID~\\cite{alam2021humaid} ($K{=}10$), VAST ($K{=}3$), and CivilComments ($K{=}2$). Four LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat, Qwen2.5-7B-Instruct) produce 23 configurations across the three datasets under zero-shot and few-shot prompting, yielding 161 bias scenarios ($23 \\times 7$ topologies).\n\n\\paragraph{HumAID ($K{=}10$): theory--practice alignment.}\nThe empirical bias ranking matches predictions: IV (12.4--42.1\\%), exposure (9.0--17.4\\%), mediation/front-door (10.7--14.8\\%), while collider, confounding, and M-bias remain below 10\\%---consistent with the ASV vulnerability spectrum.\n\n\\paragraph{Cross-$K$ comparison.}\nBias varies substantially across settings: VAST ($K{=}3$) produces 62.8\\% mean bias with IV reaching 326\\%, versus 12.2\\% for HumAID ($K{=}10$) and 32.4\\% for CivilComments ($K{=}2$). Even CivilComments configurations with $F_1{=}0.82$ (Qwen3-235B) produce 62--92\\% IV bias, confirming that classification accuracy does not predict downstream causal risk (Figure~\\ref{fig:f1_vs_bias}).\\footnote{VAST's near-degenerate confusion matrices (Neutral-class recall 3.6--16.1\\%) drive its extreme IV bias via the Wald estimator's small-denominator amplification.}\n\nChecking all $K{-}1$ exposure coefficients, 14 of 23 configurations (61\\%) exhibit sign reversal in at least one coefficient---all in the exposure topology, confirming that exposure vulnerability persists at the coefficient level even for diagonally-dominant matrices. For HumAID ($K{=}10$), 7 of 8 configurations reverse a secondary coefficient ($|\\beta| \\leq 0.2$); for VAST ($K{=}3$), 7 of 8 reverse $\\beta_2{=}{-}0.50$. The primary coefficient ($\\beta_1$, largest magnitude) never reverses across any empirical configuration; sign flips occur exclusively in secondary coefficients corresponding to rare categories with small $|\\beta|$. Sign reversal requires the DGP to contain opposite-sign treatment effects across categories (Equation~\\ref{eq:exposure}); when all $\\beta_k$ share the same sign, misclassification produces only attenuation. Zero sign reversals occur across 138 non-exposure scenarios ($23 {\\times} 6$ topologies), validating the structural guarantee $K$-invariantly. CivilComments ($K{=}2$) confirms the binary algebraic protection. The 7B-to-frontier bias ratio is 1.89, indicating topology rather than model scale determines downstream bias.\n\n\\paragraph{ASV diagnostic results.}\nFor HumAID ($K{=}10$, 56 scenarios), 55.4\\% are flagged as magnitude-ASV-unsafe---IV, mediation, front-door, and exposure all trigger, while confounding, collider, and M-bias remain below 10\\% bias (Figure~\\ref{fig:asv_heatmap}). For CivilComments ($K{=}2$), 100\\% of scenarios are ASV-unsafe despite $F_1$ ranging from $0.69$ (7B) to $0.82$ (frontier).\n\nOverlaying all 23 empirical matrices onto the theoretical Dirichlet violation-rate curves (Figure~\\ref{fig:dirichlet_overlay}, Appendix~\\ref{app:supplementary}) confirms placement: VAST in the danger zone, HumAID mid-range, CivilComments approaching safe for exposure but still in IV amplification.\nA logistic DGP simulation (Appendix~\\ref{sec:logistic_dgp}) confirms that sign-flip patterns are qualitatively preserved under nonlinear models for three representative topologies (confounding, exposure, IV), with treatment-effect sign-flip rate differences $< 2$ percentage points.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig5_f1_vs_bias.pdf}\n\\caption{Topology determines downstream causal bias, not $F_1$. HumAID $K{=}10$ (56 points): within $F_1$ range 0.614--0.690, bias varies $10{\\times}$ (IV 42.1\\% vs.\\ collider $<$5.6\\%).}\n\\label{fig:f1_vs_bias}\n\\end{figure}\n\n\n\\subsection{Correction Guidance}\n\\label{sec:correction}\n\nWe evaluate five correction methods (naive plug-in, MLA, DSL~\\cite{egami_hinck_stewart_wei2023}, MC-SIMEX, PPI++~\\cite{angelopoulos2023}) across all seven topologies under six error structures (210 configurations; full results in Table~\\ref{tab:correction}, Appendix~\\ref{app:supplementary}).\n\n\\paragraph{FWL invariance.}\nFor four topologies where $A$ enters as a covariate (confounding, mediation, collider, M-bias), the Frisch--Waugh--Lovell theorem implies that applying $C^{-1}$ to the dummy variables cannot change the $T$ coefficient. Naive plug-in and MLA achieve exactly 0.0\\% bias reduction across these four topologies.\n\n\\paragraph{Method ranking.}\nMeasuring RMSE reduction ($1 - \\text{RMSE}_{\\text{corr}} / \\text{RMSE}_{\\text{uncorr}}$), PPI++ achieves the highest grand-mean reduction (47.0\\%) but requires gold labels and is catastrophically harmful for M-bias ($-$88.0\\%). MC-SIMEX provides gold-free correction (13.3\\% grand mean, best for IV at 59.4\\%) but harms front-door ($-$62.4\\%). DSL corrects confounding (48.0\\%) and mediation (52.9\\%) but amplifies M-bias ($-$267\\%) and IV ($-$206\\%). No single method dominates: correction effectiveness is itself topology-dependent. Cross-PPI~\\cite{zrnic_candes2024} eliminates the gold-label requirement by using two independent LLM annotators whose predictions serve as mutual references, yielding valid confidence intervals under an annotator-independence assumption. Because it operates on estimator outputs rather than on $C$ directly, Cross-PPI is not subject to FWL invariance and can potentially correct all seven topologies. Methods that bypass FWL through a different route---such as EM imputation of latent true labels and Bayesian measurement error models---offer further alternatives for the four FWL-invariant topologies.\n\nEmpirical validation on HumAID ($K{=}10$, 30 MC replicates) confirms topology-dependent method superiority: MC-SIMEX outperforms PPI++ in 4 of 7 topologies and reverses from harmful ($K{=}3$) to beneficial ($K{=}10$). A retrospective case study applying the full framework to \\citet{lee_wood_doughty2024} is in Appendix~\\ref{app:case_study}.\n",
      "numLines": 109,
      "startLine": 1,
      "totalLines": 109
    }
  },
  "sourceToolAssistantUUID": "0b40e1db-e711-46be-9e50-33ac692d6413",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-22T13:41:28.901Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ct4Zb2rCPh21nV8gwe1oFc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1464eb78-476c-4bad-8274-828b0708bfc9",
  "isSidechain": false,
  "requestId": "req_011CbHhjawZAWLgmCx6xMRHN",
  "type": "assistant",
  "uuid": "809cdef4-dcb2-41b1-a337-f904690bc829",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y4dsySXmb6d31aQhSGZ6LP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2311,
      "cache_creation_input_tokens": 2246,
      "cache_read_input_tokens": 38265,
      "output_tokens": 893,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2246,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2311,
          "output_tokens": 893,
          "cache_read_input_tokens": 38265,
          "cache_creation_input_tokens": 2246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2246
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

_source line 46 · 2026-05-22T13:41:28.909Z_

<details><summary>↩ Tool result · `toolu_01Ct4Zb2rCPh21nV8gwe1oFc`</summary>

```text
1	\enlargethispage{1\baselineskip}
2	\section{Conclusion}
3	\label{sec:conclusion}
4	
5	We characterized how multi-class annotation errors interact with causal DAG topology, analyzing bias direction, sensitivity, and correction across seven canonical topologies. The classical binary guarantee breaks at $K \geq 3$: exposure and IV topologies produce sign reversal (83.4\% and 52.6\%), while five topologies maintain a structural guarantee. Three core contributions---the $K{\geq}3$ algebraic break, the five-topology sign-preservation guarantee, and FWL invariance---are DGP-independent structural results that hold for arbitrary parameter values under stated sufficient conditions. Empirical validation with real LLM confusion matrices confirms this vulnerability: 61\% of exposure configurations exhibit coefficient-level sign reversal despite diagonal dominance. The ASV framework reveals a vulnerability spectrum from IV (maximally fragile) to M-bias (immune), and correction effectiveness is itself topology-dependent, with matrix-based methods provably ineffective for four topologies. Differential misclassification and correlated multi-LLM errors are natural extensions.
6	
7	\section*{Limitations}
8	
9	Our framework assumes non-differential misclassification ($P(A^*|A, Y, \mathbf{Z}) = P(A^*|A)$), which holds when the LLM has no access to $Y$ but may be violated with outcome-conditional prompting. A stress test across 96 configurations (Appendix~\ref{sec:nondiff_stress}) shows moderate robustness: $\varepsilon{=}0.05$ increases violations by $<$3pp; at $K{=}10$, zero sign flips across all $\varepsilon$. Closed-form expressions are derived for $K{=}3$ and verified at $K{=}5,7$; arbitrary $K$ remains open. The framework assumes a single annotator; correlated multi-annotator settings~\cite{kim_garg2025} are future work. Frontier-model coverage for VAST and CivilComments is partial (15 of 18 planned configurations completed); cross-tier comparisons should be interpreted with this caveat. All derivations assume linear structural equations; the FWL invariance result does not hold for logistic regression, and bias patterns under nonlinear models may differ.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "809cdef4-dcb2-41b1-a337-f904690bc829",
  "isSidechain": false,
  "promptId": "e832977f-06f5-437f-9468-12b340b28a19",
  "type": "user",
  "uuid": "caa58958-e920-49b7-a3b6-4d5cb24ea170",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex",
      "content": "\\enlargethispage{1\\baselineskip}\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe characterized how multi-class annotation errors interact with causal DAG topology, analyzing bias direction, sensitivity, and correction across seven canonical topologies. The classical binary guarantee breaks at $K \\geq 3$: exposure and IV topologies produce sign reversal (83.4\\% and 52.6\\%), while five topologies maintain a structural guarantee. Three core contributions---the $K{\\geq}3$ algebraic break, the five-topology sign-preservation guarantee, and FWL invariance---are DGP-independent structural results that hold for arbitrary parameter values under stated sufficient conditions. Empirical validation with real LLM confusion matrices confirms this vulnerability: 61\\% of exposure configurations exhibit coefficient-level sign reversal despite diagonal dominance. The ASV framework reveals a vulnerability spectrum from IV (maximally fragile) to M-bias (immune), and correction effectiveness is itself topology-dependent, with matrix-based methods provably ineffective for four topologies. Differential misclassification and correlated multi-LLM errors are natural extensions.\n\n\\section*{Limitations}\n\nOur framework assumes non-differential misclassification ($P(A^*|A, Y, \\mathbf{Z}) = P(A^*|A)$), which holds when the LLM has no access to $Y$ but may be violated with outcome-conditional prompting. A stress test across 96 configurations (Appendix~\\ref{sec:nondiff_stress}) shows moderate robustness: $\\varepsilon{=}0.05$ increases violations by $<$3pp; at $K{=}10$, zero sign flips across all $\\varepsilon$. Closed-form expressions are derived for $K{=}3$ and verified at $K{=}5,7$; arbitrary $K$ remains open. The framework assumes a single annotator; correlated multi-annotator settings~\\cite{kim_garg2025} are future work. Frontier-model coverage for VAST and CivilComments is partial (15 of 18 planned configurations completed); cross-tier comparisons should be interpreted with this caveat. All derivations assume linear structural equations; the FWL invariance result does not hold for logistic regression, and bias patterns under nonlinear models may differ.\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  },
  "sourceToolAssistantUUID": "809cdef4-dcb2-41b1-a337-f904690bc829",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-22T13:41:29.808Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E33sd1hWfLY6iQMpCQRmvP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "caa58958-e920-49b7-a3b6-4d5cb24ea170",
  "isSidechain": false,
  "requestId": "req_011CbHhjawZAWLgmCx6xMRHN",
  "type": "assistant",
  "uuid": "76905a48-91dc-4eaa-b1fd-2e91eed5bf2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y4dsySXmb6d31aQhSGZ6LP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2311,
      "cache_creation_input_tokens": 2246,
      "cache_read_input_tokens": 38265,
      "output_tokens": 893,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2246,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2311,
          "output_tokens": 893,
          "cache_read_input_tokens": 38265,
          "cache_creation_input_tokens": 2246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2246
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

_source line 48 · 2026-05-22T13:41:30.070Z_

<details><summary>↩ Tool result · `toolu_01E33sd1hWfLY6iQMpCQRmvP`</summary>

```text
1	\section{Proofs of Proposition~\ref{prop:signflip} and Theorem~\ref{thm:monotone}}
2	\label{app:proof}
3	
4	We provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Empirical Finding~1), and the monotonicity proof for confounding (Theorem~\ref{thm:monotone}).
5	Throughout, $A\in\{0,1,\dots,K{-}1\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\mid A{=}k)$.
6	We use category~0 as the reference and let $D_j=\mathbf{1}(A{=}j)$, $D_j^*=\mathbf{1}(A^*{=}j)$ for $j=1,\dots,K{-}1$.
7	
8	\subsection{Notation and Key Identities}
9	\label{app:notation}
10	
11	Under non-differential misclassification, the misclassified moments factor linearly through $C$.
12	Define the population vectors:
13	\begin{align}
14	  q_j &= P(A^*{=}j) = \textstyle\sum_k C_{jk}\,p_k, \label{eq:q}\\
15	  \mathrm{ct}_j &= \mathbb{E}[T\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[T\cdot D_k], \label{eq:ct}\\
16	  \mathrm{cy}_j &= \mathbb{E}[Y\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[Y\cdot D_k]. \label{eq:cy}
17	\end{align}
18	Write $q = Cp$, $\mathrm{ct} = C\,\mathbb{E}[T\cdot D]$, and $\mathrm{cy} = C\,\mathbb{E}[Y\cdot D]$, where $D=(D_0,\dots,D_{K-1})^\top$.
19	
20	\subsection{Frisch--Waugh--Lovell Decomposition}
21	\label{app:fwl}
22	
23	For topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\dots,D_{K-1}^*)$.
24	By the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:
25	\begin{equation}
26	  \operatorname{plim}\hat{\tau}(C)
27	  = \frac{\mathbb{E}[\tilde{T}\,\tilde{Y}]}{\mathbb{E}[\tilde{T}^2]},
28	  \label{eq:fwl}
29	\end{equation}
30	where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$ and $\tilde{Y}=Y-\mathbb{E}[Y\mid A^*]$ are residuals from projecting onto $(1,D_1^*,\dots,D_{K-1}^*)$.
31	
32	\begin{lemma}[Bias decomposition]
33	\label{lem:bias_decomp}
34	Suppose $Y = \tau T + f(A) + \varepsilon_Y$ with $\varepsilon_Y \perp (T, A, A^*)$.
35	Then
36	\begin{equation}
37	  \operatorname{plim}\hat\tau(C) = \tau + \frac{R(C)}{D(C)},
38	  \label{eq:bias_decomp}
39	\end{equation}
40	where
41	\begin{align}
42	  R(C) &= \mathbb{E}\bigl[\operatorname{Cov}(T,\,f(A)\mid A^*)\bigr], \label{eq:R}\\
43	  D(C) &= \mathbb{E}\bigl[\operatorname{Var}(T\mid A^*)\bigr] > 0. \label{eq:D}
44	\end{align}
45	\end{lemma}
46	
47	\begin{proof}
48	Expand $\tilde{Y}$ using $Y=\tau T + f(A) + \varepsilon_Y$:
49	\[
50	  \tilde{Y} = \tau\,\tilde{T} + \bigl(f(A) - \mathbb{E}[f(A)\mid A^*]\bigr) + \varepsilon_Y.
51	\]
52	Since $\tilde{T}$ is measurable w.r.t.\ $(T,A^*)$ and $\varepsilon_Y\perp(T,A,A^*)$:
53	\[
54	  \mathbb{E}[\tilde{T}\,\tilde{Y}]
55	  = \tau\,\mathbb{E}[\tilde{T}^2]
56	  + \mathbb{E}\bigl[\tilde{T}\,\bigl(f(A)-\mathbb{E}[f(A)\mid A^*]\bigr)\bigr].
57	\]
58	The numerator residual is $R(C) = \mathbb{E}[\tilde{T}(f(A)-\mathbb{E}[f(A)\mid A^*])]$, and the denominator is $D(C) = \mathbb{E}[\tilde{T}^2]$.
59	
60	By the law of total covariance:
61	\[
62	  R(C) = \sum_{j=0}^{K-1} q_j\,\operatorname{Cov}(T,\,f(A)\mid A^*{=}j)
63	  = \mathbb{E}[\operatorname{Cov}(T,f(A)\mid A^*)].
64	\]
65	For $D(C)>0$: decompose $T = g(A) + \varepsilon_T$ where $g(A)=\mathbb{E}[T\mid A]$ (for confounding) or simply note that $T$ has exogenous variation independent of $A^*$ (for mediation).
66	In both cases, $\tilde{T}=\bigl(g(A)-\mathbb{E}[g(A)\mid A^*]\bigr)+\varepsilon_T'$, where $\varepsilon_T'$ is the component of $T$ independent of $(A,A^*)$.
67	Hence $D(C)\geq\operatorname{Var}(\varepsilon_T')>0$.
68	\end{proof}
69	
70	\subsection{Confounding Topology ($A$ = Confounder)}
71	\label{app:confounding}
72	
73	\paragraph{Data-generating process.}
74	$A\to T$, $A\to Y$, $T\to Y$.
75	Using dummy coding with category 0 as reference:
76	\begin{align*}
77	  T &= \sum_{j=1}^{K-1}\alpha_j D_j + \varepsilon_T,\quad
78	  \varepsilon_T\sim\mathcal{N}(0,\sigma_T^2),\;\varepsilon_T\perp A,\\
79	  Y &= \tau\, T + \sum_{j=1}^{K-1}\beta_j^{(A)} D_j + \varepsilon_Y,\quad
80	  \varepsilon_Y\sim\mathcal{N}(0,1),\;\varepsilon_Y\perp(T,A).
81	\end{align*}
82	Define $g(k)=\sum_{j}\alpha_j\mathbf{1}(k{=}j)$ and $f(k)=\sum_{j}\beta_j^{(A)}\mathbf{1}(k{=}j)$, so $g(0)=f(0)=0$.
83	
84	\paragraph{Closed-form plim.}
85	Using the FWL decomposition, the coefficient on $T$ is:
86	\begin{equation}
87	  \operatorname{plim}\hat\tau(C)
88	  = \frac{\mu_{TY} - \sum_{j=0}^{K-1}\frac{\mathrm{ct}_j\,\mathrm{cy}_j}{q_j}}
89	  {s_T - \sum_{j=0}^{K-1}\frac{\mathrm{ct}_j^2}{q_j}},
90	  \label{eq:plim_conf}
91	\end{equation}
92	where $s_T=\mathbb{E}[T^2]$, $\mu_{TY}=\mathbb{E}[TY]$, and $\mathrm{ct}_j$, $\mathrm{cy}_j$, $q_j$ are defined in~\eqref{eq:q}--\eqref{eq:cy}.
93	
94	\begin{proof}[Derivation]
95	By FWL, $\operatorname{plim}\hat\tau = \mathbb{E}[\tilde{T}Y]/\mathbb{E}[\tilde{T}^2]$ where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$.
96	Since $\mathbb{E}[T\mid A^*{=}j]=\mathrm{ct}_j/q_j$:
97	\begin{align*}
98	  \mathbb{E}[\tilde{T}^2]
99	  &= \mathbb{E}[T^2] - \sum_j q_j\bigl(\mathrm{ct}_j/q_j\bigr)^2
100	  = s_T - \sum_j \mathrm{ct}_j^2/q_j,\\
101	  \mathbb{E}[\tilde{T}\,Y]
102	  &= \mathbb{E}[TY] - \sum_j \bigl(\mathrm{ct}_j/q_j\bigr)\,\mathbb{E}[Y\cdot D_j^*]
103	  = \mu_{TY} - \sum_j \mathrm{ct}_j\,\mathrm{cy}_j/q_j.
104	\end{align*}
105	\end{proof}
106	
107	\paragraph{Verification at $C=I$.}
108	When $C=I$: $q_j=p_j$, $\mathrm{ct}_j=\mathbb{E}[T D_j]=\alpha_j p_j$, $\mathrm{cy}_j=\mathbb{E}[Y D_j]=p_j(\tau\alpha_j+\beta_j^{(A)})$.
109	Direct substitution yields numerator $= \tau\sigma_T^2$ and denominator $= \sigma_T^2$, giving $\operatorname{plim}\hat\tau = \tau$.
110	
111	\paragraph{Bias structure.}
112	By Lemma~\ref{lem:bias_decomp}:
113	\begin{equation}
114	  \operatorname{plim}\hat\tau(C) = \tau + B(C),\quad
115	  B(C) = \frac{\mathbb{E}[\operatorname{Cov}(g(A),\,f(A)\mid A^*)]}{D(C)}.
116	  \label{eq:bias_conf}
117	\end{equation}
118	By the law of total covariance:
119	\begin{equation}
120	  \mathbb{E}[\operatorname{Cov}(g,f\mid A^*)]
121	  = \operatorname{Cov}(g(A),f(A))
122	  - \operatorname{Cov}\bigl(\mathbb{E}[g(A)\mid A^*],\;\mathbb{E}[f(A)\mid A^*]\bigr).
123	  \label{eq:lotc}
124	\end{equation}
125	
126	At $C=I$: $\mathbb{E}[g\mid A^*]=g(A)$, so the between-group covariance equals $\operatorname{Cov}(g,f)$ and $B(I)=0$.
127	
128	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ (uniform, $A^*\perp A$): $\mathbb{E}[g\mid A^*]$ is constant, so the between-group covariance is zero and
129	\begin{equation}
130	  B_{\mathrm{OV}} \;\equiv\; B\bigl(\tfrac{1}{K}\mathbf{1}\mathbf{1}^\top\bigr)
131	  = \frac{\operatorname{Cov}(g(A),\,f(A))}{\operatorname{Var}(T)},
132	  \label{eq:bov}
133	\end{equation}
134	which equals the classical omitted-variable bias (no control for $A$).
135	
136	\paragraph{Sign preservation condition.}
137	Since $D(C)>0$, sign$(\operatorname{plim}\hat\tau) = $ sign$(\tau\cdot D(C) + R(C))$.
138	For sign preservation, it suffices that $R(C)$ does not overwhelm $\tau\cdot D(C)$.
139	
140	\begin{proposition}[Confounding sign preservation --- proportional case]
141	\label{prop:conf_prop}
142	If $f(A) = \lambda\,g(A)$ for some constant $\lambda$ (i.e., the confounder effects on $T$ and $Y$ are proportional), then
143	\begin{equation}
144	  B(C) = \bigl(1-\eta(C)\bigr)\,B_{\mathrm{OV}},
145	  \label{eq:convex}
146	\end{equation}
147	where
148	\[
149	  \eta(C) = \frac{\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])\;\sigma_T^2}
150	  {\operatorname{Var}(g(A))\bigl(\operatorname{Var}(g(A))-\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])+\sigma_T^2\bigr)}
151	  \;\in\;[0,1].
152	\]
153	Consequently, $B(C)$ lies between $0$ and $B_{\mathrm{OV}}$, and $\operatorname{sign}(\operatorname{plim}\hat\tau)=\operatorname{sign}(\tau)$ whenever $\operatorname{sign}(\tau)=\operatorname{sign}(\tau+B_{\mathrm{OV}})$.
154	\end{proposition}
155	
156	\begin{proof}
157	When $f=\lambda g$: the between-group covariance in~\eqref{eq:lotc} becomes $\lambda\,\operatorname{Var}(\mathbb{E}[g\mid A^*])$, and $\operatorname{Cov}(g,f)=\lambda\,\operatorname{Var}(g)$.
158	So $R(C)=\lambda\bigl(\operatorname{Var}(g)-\operatorname{Var}(\mathbb{E}[g\mid A^*])\bigr)=\lambda\,V_W$, where $V_W=\operatorname{Var}(g)-V_B$ with $V_B=\operatorname{Var}(\mathbb{E}[g\mid A^*])$.
159	Similarly, $D(C)=V_W+\sigma_T^2$.
160	Hence
161	\[
162	  B(C) = \frac{\lambda\,V_W}{V_W+\sigma_T^2},\qquad
163	  B_{\mathrm{OV}} = \frac{\lambda\,V}{V+\sigma_T^2},
164	\]
165	where $V=\operatorname{Var}(g)=V_B+V_W$.
166	The ratio
167	\[
168	  \frac{B(C)}{B_{\mathrm{OV}}} = \frac{V_W(V+\sigma_T^2)}{V(V_W+\sigma_T^2)} = 1 - \eta(C)
169	\]
170	is a decreasing function of $V_B\in[0,V]$.
171	At $V_B=0$ (no classification, $C$ uniform): $\eta=0$, $B=B_{\mathrm{OV}}$.
172	At $V_B=V$ (perfect classification, $C=I$): $\eta=1$, $B=0$.
173	Since $0\leq V_B\leq V$, we have $\eta\in[0,1]$ and $B(C)\in[0,B_{\mathrm{OV}}]$ (with the sign of $B_{\mathrm{OV}}$).
174	\end{proof}
175	
176	\begin{proposition}[Confounding sign preservation --- general case]
177	\label{prop:conf_gen}
178	For general $g$ and $f$ (not necessarily proportional), define the worst-case bias bound
179	\begin{equation}
180	  \bar{B} \;=\; \frac{\sqrt{\operatorname{Var}(g(A))\,\operatorname{Var}(f(A))}}{\sigma_T^2}.
181	  \label{eq:bbar}
182	\end{equation}
183	If $|\tau| > \bar{B}$, then $\operatorname{sign}(\operatorname{plim}\hat\tau(C))=\operatorname{sign}(\tau)$ for \emph{all} column-stochastic $C$.
184	\end{proposition}
185	
186	\begin{proof}
187	We need $\operatorname{sign}(\tau\cdot D(C)+R(C))=\operatorname{sign}(\tau)$, which holds if $|R(C)|<|\tau|\cdot D(C)$.
188	Since $D(C)\geq\sigma_T^2$ (shown in Lemma~\ref{lem:bias_decomp}), it suffices to show $|R(C)|<|\tau|\,\sigma_T^2$.
189	
190	\emph{Step 1: Bound $|R(C)|$.}
191	$R(C)=\mathbb{E}[\operatorname{Cov}(g(A),f(A)\mid A^*)]$.
192	By the Cauchy--Schwarz inequality applied to each within-group covariance:
193	\[
194	  |\operatorname{Cov}(g,f\mid A^*{=}j)|
195	  \leq \sqrt{\operatorname{Var}(g\mid A^*{=}j)\,\operatorname{Var}(f\mid A^*{=}j)}.
196	\]
197	Taking expectations and applying Cauchy--Schwarz again:
198	\begin{align*}
199	  |R(C)|
200	  &\leq \mathbb{E}\bigl[\sqrt{\operatorname{Var}(g\mid A^*)\,\operatorname{Var}(f\mid A^*)}\bigr]\\
201	  &\leq \sqrt{\mathbb{E}[\operatorname{Var}(g\mid A^*)]\;\mathbb{E}[\operatorname{Var}(f\mid A^*)]}\\
202	  &\leq \sqrt{\operatorname{Var}(g(A))\;\operatorname{Var}(f(A))},
203	\end{align*}
204	where the last step uses $\mathbb{E}[\operatorname{Var}(X\mid Y)]\leq\operatorname{Var}(X)$ (law of total variance).
205	
206	\emph{Step 2: Conclude.}
207	The bias satisfies
208	\[
209	  |B(C)| = \frac{|R(C)|}{D(C)} \leq \frac{\sqrt{\operatorname{Var}(g)\,\operatorname{Var}(f)}}{\sigma_T^2} = \bar{B}.
210	\]
211	When $|\tau|>\bar{B}$, the bias cannot cancel $\tau$, so $\operatorname{sign}(\operatorname{plim}\hat\tau)=\operatorname{sign}(\tau)$ for all $C$.
212	\end{proof}
213	
214	\paragraph{Relationship to the omitted-variable condition.}
215	A weaker (necessary) condition for sign preservation is $\operatorname{sign}(\tau)=\operatorname{sign}(\tau_{\mathrm{OV}})$ where $\tau_{\mathrm{OV}}=\tau+\operatorname{Cov}(g,f)/\operatorname{Var}(T)$.
216	If this fails, then $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ (uniform noise) already flips the sign.
217	The rigorous sufficient condition $|\tau|>\bar{B}$ implies the weaker condition, since $|B_{\mathrm{OV}}|=|\operatorname{Cov}(g,f)|/\operatorname{Var}(T)\leq\bar{B}$ by Cauchy--Schwarz and $\operatorname{Var}(T)\geq\sigma_T^2$.
218	
219	\paragraph{Verification for paper parameters ($K{=}3$).}
220	With $\tau{=}2.0$, $\boldsymbol{\alpha}{=}(1.5,{-}1.0)$, $\boldsymbol{\beta}^{(A)}{=}(1.0,{-}0.5)$, $\sigma_T{=}1.0$, $\mathbf{p}{=}(0.40,0.35,0.25)$:
221	\begin{align*}
222	  \operatorname{Var}(g) &= \sum_k p_k\alpha_k^2 - \bigl(\textstyle\sum_k p_k\alpha_k\bigr)^2 = 0.962,\\
223	  \operatorname{Var}(f) &= \sum_k p_k(\beta_k^{(A)})^2 - \bigl(\textstyle\sum_k p_k\beta_k^{(A)}\bigr)^2 = 0.362,\\
224	  \bar{B} &= \sqrt{0.962\times 0.362}\;/\;1.0^2 = 0.590.
225	\end{align*}
226	Since $|\tau|{=}2.0 > \bar{B}{=}0.590$, sign preservation is guaranteed for \emph{all} column-stochastic $C$ by Proposition~\ref{prop:conf_gen}.
227	Additionally, $B_{\mathrm{OV}}=\operatorname{Cov}(g,f)/\operatorname{Var}(T)=0.588/1.962={+}0.300$, giving $\tau_{\mathrm{OV}}{=}2.300>0$, confirming that both the necessary and sufficient conditions are satisfied.
228	
229	\paragraph{Extension to $K > 3$.}
230	For $K{>}3$, treatment effect coefficients are drawn from a fixed pool with alternating signs and decreasing magnitudes: $\boldsymbol{\beta} = (0, 1.0, {-}0.5, 0.7, {-}0.3, 0.5, {-}0.2, 0.4, {-}0.15, 0.3, \ldots)$, truncated to $K$ entries. The category distribution uses $p_k \propto 1/(k{+}1)$, normalized to sum to 1. Other topology-specific parameters (confounding strengths, mediator effects, etc.) follow analogous alternating-sign pools. For $K{=}10$, $\boldsymbol{\beta} = (0, 1.0, {-}0.5, 0.7, {-}0.3, 0.5, {-}0.2, 0.4, {-}0.15, 0.3)$.
231	
232	\subsection{Proof of Theorem~\ref{thm:monotone} (Confounding Monotonicity)}
233	\label{app:monotonicity_proof}
234	
235	Under the interpolation $C(\delta)=(1{-}\delta)I+\delta C_0$, we prove $|B(C(\delta))|$ is non-decreasing in $\delta$ for proportional effects ($f=\lambda g$) and provide numerical verification for the general case.
236	
237	\paragraph{Proportional case ($f=\lambda g$).}
238	From Proposition~\ref{prop:conf_prop}, $B(C)=\lambda V_W/(V_W+\sigma_T^2)$ where $V_W=\operatorname{Var}(g)-V_B$ and $V_B(\delta)=\operatorname{Var}(\mathbb{E}[g(A)\mid A^*_\delta])$.
239	
240	\emph{Step 1: $V_B(\delta)$ is non-increasing.}
241	The conditional expectation $\mathbb{E}[g(A)\mid A^*_\delta]$ is a linear function of the posterior $P(A\mid A^*_\delta)$, which in turn depends on $C(\delta)$.
242	As $\delta$ increases, $C(\delta)$ becomes a noisier channel: the mutual information $I(A;A^*_\delta)$ decreases.
243	While the exact degradation factorization $C(\delta_2)=M\cdot C(\delta_1)$ for a stochastic $M$ is non-trivial for the linear interpolation family, the monotonic decrease of $V_B(\delta)$ can be verified directly: for $K{=}2$ symmetric $C_0$, $dV_B/d\delta < 0$ follows by differentiation; for general $K$, we verify $V_B(\delta_2)\leq V_B(\delta_1)$ numerically across all test configurations with zero violations.
244	
245	\emph{Step 2: $|B(\delta)|$ is non-decreasing.}
246	$V_W(\delta)=\operatorname{Var}(g)-V_B(\delta)$ is non-decreasing (Step~1).
247	The function $h(x)=|\lambda|\,x/(x+\sigma_T^2)$ is strictly increasing for $x\geq 0$ and $\sigma_T^2>0$.
248	Hence $|B(\delta)|=h(V_W(\delta))$ is non-decreasing.
249	
250	\paragraph{General case.}
251	$|B(C(\delta))|\leq\bar{B}(\delta)$ where $\bar{B}(\delta)=\sqrt{\mathbb{E}[\operatorname{Var}(g\mid A^*_\delta)]\,\mathbb{E}[\operatorname{Var}(f\mid A^*_\delta)]}\,/\,D(\delta)$ (Proposition~\ref{prop:conf_gen}).
252	By the same data processing argument, each $\mathbb{E}[\operatorname{Var}(\cdot\mid A^*_\delta)]$ is non-decreasing in $\delta$, and $D(\delta)=\mathbb{E}[\operatorname{Var}(T\mid A^*_\delta)]$ is non-decreasing.
253	The numerator grows at least as fast as the denominator (since $D(\delta)\leq\operatorname{Var}(T)$), maintaining monotonicity of the bound.
254	Extended verification (10{,}000 random $C_0$ matrices, $K \in \{3,5,7\}$) reveals worst-case step deviations of 0.011 (confounding), confirming approximate tightness; a strict monotonicity proof for the general case remains open.
255	
256	\subsection{Mediation Topology ($A$ = Mediator)}
257	\label{app:mediation}
258	
259	\paragraph{Data-generating process.}
260	$T\to A\to Y$, $T\to Y$.
261	\begin{align*}
262	  T &\sim \operatorname{Bernoulli}(0.5),\\
263	  A\mid T &\sim \operatorname{Categorical}\bigl(\operatorname{softmax}(\boldsymbol{\gamma}+\boldsymbol{\delta}\,T)\bigr),\\
264	  Y &= \tau_{\mathrm{dir}}\,T + f(A) + \varepsilon_Y.
265	\end{align*}
266	
267	\paragraph{Bias decomposition.}
268	By Lemma~\ref{lem:bias_decomp}, the direct-effect estimator satisfies:
269	\begin{equation}
270	  \operatorname{plim}\hat\tau_{\mathrm{dir}}(C) = \tau_{\mathrm{dir}} + \frac{\mathbb{E}[\operatorname{Cov}(T,\,f(A)\mid A^*)]}{D(C)}.
271	  \label{eq:med_bias}
272	\end{equation}
273	
274	The key structural difference from confounding: $T$ \emph{causes} $A$, so the residual covariance $\operatorname{Cov}(T,f(A)\mid A^*)$ captures the indirect effect of $T$ on $Y$ through $A$ that is not absorbed by conditioning on $A^*$.
275	
276	\paragraph{Endpoint analysis.}
277	
278	At $C=I$ ($A^*{=}A$): conditioning on $A$ blocks the mediated path $T\to A\to Y$, so $\operatorname{Cov}(T,f(A)\mid A)=0$ and $\operatorname{plim}\hat\tau=\tau_{\mathrm{dir}}$.
279	
280	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ ($A^*\perp A$): no information about $A$ is used, and
281	\begin{align*}
282	  \mathbb{E}[\operatorname{Cov}(T,f(A)\mid A^*)] &= \operatorname{Cov}(T,f(A)),\\
283	  D(C) &= \operatorname{Var}(T) = 0.25.
284	\end{align*}
285	The indirect effect is $\tau_{\mathrm{ind}}=\mathbb{E}[f(A)\mid T{=}1]-\mathbb{E}[f(A)\mid T{=}0]$, and
286	\[
287	  \operatorname{Cov}(T,f(A)) = 0.25\,\tau_{\mathrm{ind}}.
288	\]
289	Hence at $C$ uniform: $\operatorname{plim}\hat\tau = \tau_{\mathrm{dir}}+\tau_{\mathrm{ind}} = \tau_{\mathrm{total}}$.
290	
291	\paragraph{Empirical Finding (Mediation sign preservation).}
292	\label{find:med_sign}
293	$\operatorname{sign}(\operatorname{plim}\hat\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{dir}})$ whenever $\operatorname{sign}(\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{total}})$, where $\tau_{\mathrm{total}}=\tau_{\mathrm{dir}}+\tau_{\mathrm{ind}}$.
294	This result is verified numerically for $100{,}000$ independently sampled column-stochastic matrices $C$; a closed-form proof for general $K$ remains open.
295	
296	\begin{proof}
297	Let $R(C)=\mathbb{E}[\operatorname{Cov}(T,f(A)\mid A^*)]$ and $D(C)=\mathbb{E}[\operatorname{Var}(T\mid A^*)]>0$.
298	
299	\emph{Endpoints.}
300	At $C{=}I$: $f(A)$ is constant given $A{=}A^*$, so $R(I)=0$ and $B(I)=0$.
301	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$: $R=\operatorname{Cov}(T,f(A))=0.25\,\tau_{\mathrm{ind}}$ and $D=\operatorname{Var}(T)=0.25$, giving $B=\tau_{\mathrm{ind}}$.
302	
303	\emph{Within-group structure for binary $T$.}
304	Since $T\in\{0,1\}$, the within-$A^*$-group bias admits a revealing decomposition.
305	Let $p_j=P(T{=}1\mid A^*{=}j)$.
306	Then $\operatorname{Var}(T\mid A^*{=}j)=p_j(1{-}p_j)$ and
307	\[
308	  \operatorname{Cov}(T,f(A)\mid A^*{=}j)
309	  = p_j(1{-}p_j)\bigl[\mathbb{E}[f(A)\mid T{=}1,A^*{=}j]-\mathbb{E}[f(A)\mid T{=}0,A^*{=}j]\bigr].
310	\]
311	Define $\delta_j=\mathbb{E}[f(A)\mid T{=}1,A^*{=}j]-\mathbb{E}[f(A)\mid T{=}0,A^*{=}j]$ as the \emph{conditional indirect effect} in the $A^*{=}j$ subpopulation.
312	Then
313	\[
314	  B(C)=\frac{R(C)}{D(C)}
315	  =\frac{\sum_j q_j\,p_j(1{-}p_j)\,\delta_j}{\sum_j q_j\,p_j(1{-}p_j)}
316	  =\sum_j w_j\,\delta_j,
317	\]
318	a weighted average of the conditional indirect effects, with weights $w_j=q_j p_j(1{-}p_j)/\sum_\ell q_\ell p_\ell(1{-}p_\ell)\geq 0$ summing to 1.
319	
320	At $C{=}I$: each $A^*{=}j$ group has $A{=}j$ a.s., so $\delta_j=f(j)-f(j)=0$ and $B=0$.
321	At $C$ uniform: $\delta_j=\tau_{\mathrm{ind}}$ for all $j$ and $B=\tau_{\mathrm{ind}}$.
322	
323	\emph{Sign preservation.}
324	When $\operatorname{Cov}(g(A),f(A))>0$ (the indirect effect reinforces the direct effect, i.e., $\tau_{\mathrm{dir}}$ and $\tau_{\mathrm{ind}}$ have the same sign), the bias $B(C)\geq 0$ cannot oppose $\tau_{\mathrm{dir}}$, so sign is preserved trivially.
325	
326	When $\tau_{\mathrm{dir}}$ and $\tau_{\mathrm{ind}}$ have opposite signs but $|\tau_{\mathrm{ind}}|<|\tau_{\mathrm{dir}}|$ (i.e., $\operatorname{sign}(\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{total}})$), sign reversal requires some $|\delta_j|>|\tau_{\mathrm{dir}}|$ with the opposing sign.
327	Since each $\delta_j$ is a difference of weighted averages of $f$ values (with weights $P(A{=}k\mid T{=}t,A^*{=}j)$), and $B(C)$ is a convex combination of $\delta_j$, the bound $|B(C)|\leq\max_j|\delta_j|$ holds.
328	We verify numerically that $\max_j|\delta_j|\leq|\tau_{\mathrm{ind}}|$ for all 100{,}000 random $C$ matrices in our experiments, confirming sign preservation.
329	\end{proof}
330	
331	\paragraph{Verification for paper parameters ($K{=}3$).}
332	With $\tau_{\mathrm{dir}}{=}0.5$, $\boldsymbol{\gamma}{=}(0,0,0)$, $\boldsymbol{\delta}{=}(0,0.8,{-}0.6)$, $\boldsymbol{\beta}{=}(0,1.0,{-}0.5)$:
333	
334	$\tau_{\mathrm{ind}}=\mathbb{E}[f(A)\mid T{=}1]-\mathbb{E}[f(A)\mid T{=}0]=0.351$ (computed from the softmax class probabilities).
335	$\tau_{\mathrm{total}}=0.5+0.351=0.851>0$.
336	Since $\tau_{\mathrm{dir}}{>}0$ and $\tau_{\mathrm{total}}{>}0$, sign preservation holds for all $C$.
337	
338	\subsection{Collider Topology ($A$ = Collider)}
339	\label{app:collider}
340	
341	\paragraph{Data-generating process.}
342	$T\to A\leftarrow Y$, $T\to Y$.
343	The treatment effect is unconfounded:
344	\begin{align*}
345	  T &\sim \mathcal{N}(0,1),\quad
346	  Y = \tau\,T + \varepsilon_Y,\quad \varepsilon_Y\sim\mathcal{N}(0,1),\;\varepsilon_Y\perp T,\\
347	  A\mid T,Y &\sim \operatorname{Categorical}\bigl(\operatorname{softmax}(\boldsymbol{\delta}_T\,T + \boldsymbol{\delta}_Y\,Y)\bigr).
348	\end{align*}
349	The collider $A$ is a common \emph{effect} of $T$ and $Y$.
350	The no-control estimator (regressing $Y$ on $T$ alone) is consistent: $\operatorname{plim}\hat\tau_{\mathrm{nc}}=\tau$.
351	The researcher erroneously controls for $A^*$, inducing Berkson's bias.
352	
353	\paragraph{Bias decomposition.}
354	Unlike confounding, $\varepsilon_Y$ is not independent of $A$ (since $A$ depends on $Y=\tau T+\varepsilon_Y$), so Lemma~\ref{lem:bias_decomp} does not apply directly.
355	Instead, we derive the bias from the FWL identity~\eqref{eq:fwl}.
356	Writing $\tilde{Y}=\tau\tilde{T}+(\varepsilon_Y-\mathbb{E}[\varepsilon_Y\mid A^*])$ and noting that $\mathbb{E}[\tilde{T}\,\varepsilon_Y]=\mathbb{E}[\operatorname{Cov}(T,\varepsilon_Y\mid A^*)]$ (since $T\perp\varepsilon_Y$ unconditionally):
357	\begin{equation}
358	  \operatorname{plim}\hat\tau(C) = \tau + B(C),\quad
359	  B(C) = \frac{\mathbb{E}[\operatorname{Cov}(T,\,\varepsilon_Y\mid A^*)]}{\mathbb{E}[\operatorname{Var}(T\mid A^*)]}.
360	  \label{eq:bias_col}
361	\end{equation}
362	Under non-differential misclassification ($A^*\perp(T,\varepsilon_Y)\mid A$), define $g(k)=\mathbb{E}[T\mid A{=}k]$ and $h(k)=\mathbb{E}[\varepsilon_Y\mid A{=}k]$.
363	By the tower property, $\mathbb{E}[T\mid A^*]=\mathbb{E}[g(A)\mid A^*]$ and $\mathbb{E}[\varepsilon_Y\mid A^*]=\mathbb{E}[h(A)\mid A^*]$.
364	Since $\operatorname{Cov}(T,\varepsilon_Y)=0$, the law of total covariance gives:
365	\[
366	  B(C) = \frac{-\operatorname{Cov}\bigl(\mathbb{E}[g(A)\mid A^*],\;\mathbb{E}[h(A)\mid A^*]\bigr)}{\mathbb{E}[\operatorname{Var}(T\mid A^*)]}.
367	\]
368	
369	\paragraph{Endpoint analysis.}
370	At $C=I$ ($A^*{=}A$):
371	$B(I) = -\operatorname{Cov}(g(A),h(A))\,/\,\mathbb{E}[\operatorname{Var}(T\mid A)] = B_{\mathrm{Berkson}}$,
372	the full Berkson's bias from conditioning on the collider.
373	
374	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ ($A^*\perp A$):
375	$\mathbb{E}[g(A)\mid A^*]$ and $\mathbb{E}[h(A)\mid A^*]$ are constant, so $B=0$ and $\operatorname{plim}\hat\tau=\tau$.
376	
377	This is the structural reverse of confounding: misclassification attenuates the collider-induced bias toward zero, rather than growing bias from zero toward $B_{\mathrm{OV}}$.
378	
379	\begin{proposition}[Collider sign preservation --- proportional case]
380	\label{prop:col_prop}
381	If $h(A)=\lambda\,g(A)$ for some constant $\lambda$, then $|B(C)|\leq|B(I)|$ for all column-stochastic $C$, and $B(C)$ has the same sign as $B(I)$.
382	Consequently, $\operatorname{sign}(\operatorname{plim}\hat\tau)=\operatorname{sign}(\tau)$ whenever $\operatorname{sign}(\tau)=\operatorname{sign}(\tau+B_{\mathrm{Berkson}})$.
383	\end{proposition}
384	
385	\begin{proof}
386	When $h=\lambda g$, the numerator becomes $-\lambda\,\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])$ and the denominator is $\operatorname{Var}(T)-\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])$.
387	Let $V^*=\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])\in[0,V_g]$ where $V_g=\operatorname{Var}(g(A))$.
388	Then
389	\[
390	  |B(C)| = |\lambda|\,\frac{V^*}{\operatorname{Var}(T)-V^*}.
391	\]
392	The function $x\mapsto x/(a-x)$ is increasing on $[0,a)$.
393	With $a=\operatorname{Var}(T)>V_g\geq V^*$:
394	$|B(C)|\leq|\lambda|\,V_g/(\operatorname{Var}(T)-V_g)=|B(I)|$.
395	At $V^*{=}0$ (uniform $C$): $B{=}0$.  At $V^*{=}V_g$ ($C{=}I$): $B{=}B(I)$.
396	\end{proof}
397	
398	\begin{proposition}[Collider sign preservation --- general case]
399	\label{prop:col_gen}
400	Define
401	\begin{equation}
402	  \bar{B}_{\mathrm{col}} = \frac{\sqrt{\operatorname{Var}(g(A))\,\operatorname{Var}(h(A))}}{\mathbb{E}[\operatorname{Var}(T\mid A)]}.
403	  \label{eq:bbar_col}
404	\end{equation}
405	If $|\tau|>\bar{B}_{\mathrm{col}}$, then $\operatorname{sign}(\operatorname{plim}\hat\tau(C))=\operatorname{sign}(\tau)$ for all column-stochastic $C$.
406	\end{proposition}
407	
408	\begin{proof}
409	\emph{Step~1: Bound the numerator.}
410	By Cauchy--Schwarz:
411	$|\operatorname{Cov}(\mathbb{E}[g\mid A^*],\mathbb{E}[h\mid A^*])|\leq\sqrt{\operatorname{Var}(\mathbb{E}[g\mid A^*])\,\operatorname{Var}(\mathbb{E}[h\mid A^*])}$.
412	Since conditional expectation reduces variance: $\operatorname{Var}(\mathbb{E}[g\mid A^*])\leq\operatorname{Var}(g(A))$ and likewise for $h$.
413	
414	\emph{Step~2: Bound the denominator.}
415	$\mathbb{E}[\operatorname{Var}(T\mid A^*)]=\operatorname{Var}(T)-\operatorname{Var}(\mathbb{E}[T\mid A^*])\geq\operatorname{Var}(T)-\operatorname{Var}(g(A))=\mathbb{E}[\operatorname{Var}(T\mid A)]$.
416	
417	\emph{Step~3: Conclude.}
418	$|B(C)|\leq\sqrt{\operatorname{Var}(g)\,\operatorname{Var}(h)}\,/\,\mathbb{E}[\operatorname{Var}(T\mid A)]=\bar{B}_{\mathrm{col}}$.
419	When $|\tau|>\bar{B}_{\mathrm{col}}$, the bias cannot overwhelm $\tau$.
420	\end{proof}
421	
422	\paragraph{Verification for paper parameters ($K{=}3$).}
423	With $\tau{=}1.0$, $\boldsymbol{\delta}_T{=}(0,\,0.5,\,{-}0.3)$, $\boldsymbol{\delta}_Y{=}(0,\,0.8,\,0.6)$, from $5{\times}10^6$-sample Monte Carlo:
424	\begin{align*}
425	  \operatorname{Var}(g(A)) &= 0.187,\quad
426	  \operatorname{Var}(h(A)) = 0.076,\quad
427	  \mathbb{E}[\operatorname{Var}(T\mid A)] = 0.813,\\
428	  \bar{B}_{\mathrm{col}} &= \sqrt{0.187\times 0.076}\;/\;0.813 = 0.147.
429	\end{align*}
430	Since $|\tau|{=}1.0\gg\bar{B}_{\mathrm{col}}{=}0.147$, Proposition~\ref{prop:col_gen} guarantees sign preservation.
431	Additionally, $B_{\mathrm{Berkson}}{=}{-}0.114$, giving $\tau+B_{\mathrm{Berkson}}{=}0.886{>}0$.
432	Verified across $100{,}000$ random column-stochastic $C$: $\tau_{\mathrm{sign\,flip}}{=}0\%$, and $|B(C)|\leq|B_{\mathrm{Berkson}}|$ in all cases.
433	
434	\subsection{Front-door Topology ($A$ = Mediator under Confounding)}
435	\label{app:frontdoor}
436	
437	\paragraph{Data-generating process.}
438	$T\to A\to Y$, $U\to T$, $U\to Y$.
439	An unobserved confounder $U$ affects both treatment and outcome:
440	\begin{align*}
441	  U &\sim \mathcal{N}(0,1),\quad
442	  T = \alpha_U\,U + \eta,\quad \eta\sim\mathcal{N}(0,1),\;\eta\perp U,\\
443	  A\mid T &\sim \operatorname{Categorical}\bigl(\operatorname{softmax}(\boldsymbol{\gamma}+\boldsymbol{\delta}\,T)\bigr),\\
444	  Y &= f(A) + \lambda\,U + \varepsilon_Y,\quad \varepsilon_Y\perp(T,A,U).
445	\end{align*}
446	There is no direct $T{\to}Y$ edge; the causal effect of $T$ on $Y$ operates entirely through $A$.
447	The researcher controls for $A^*$ in $Y\sim 1+T+D_1^*+\cdots+D_{K-1}^*$.
448	
449	\paragraph{Bias decomposition.}
450	Since the direct effect is zero, the FWL coefficient on $T$ captures only bias:
451	\[
452	  \operatorname{plim}\hat\tau(C) = \frac{\mathbb{E}[\operatorname{Cov}(T,\,Y\mid A^*)]}{\mathbb{E}[\operatorname{Var}(T\mid A^*)]}.
453	\]
454	Substituting $Y=f(A)+\lambda U+\varepsilon_Y$ and using $\varepsilon_Y\perp(T,A,A^*)$:
455	\begin{equation}
456	  \operatorname{plim}\hat\tau(C)
457	  = \underbrace{\frac{\lambda\,\alpha_U}{\operatorname{Var}(T)}}_{\text{confounding (constant)}}
458	  \;+\; \underbrace{\frac{\mathbb{E}[\operatorname{Cov}(T,\,f(A)\mid A^*)]}{D(C)}}_{\displaystyle B_{\mathrm{med}}(C)},
459	  \label{eq:fd_decomp}
460	\end{equation}
461	where $D(C)=\mathbb{E}[\operatorname{Var}(T\mid A^*)]$.
462	
463	\begin{proof}[Derivation of~\eqref{eq:fd_decomp}]
464	Expand the numerator as
465	$\mathbb{E}[\operatorname{Cov}(T,f(A)\mid A^*)] + \lambda\,\mathbb{E}[\operatorname{Cov}(T,U\mid A^*)]$.
466	For the confounding term: since $T=\alpha_U U+\eta$ with $(U,\eta)$ jointly Gaussian, the regression residual $\xi=U-\frac{\alpha_U}{\operatorname{Var}(T)}T$ satisfies $\xi\perp T$.
467	Because $A$ is a function of $T$ (plus independent softmax noise) and $A^*$ is a function of $A$ (plus independent misclassification noise), $\xi\perp(T,A,A^*)$.
468	Therefore
469	\[
470	  \operatorname{Cov}(T,U\mid A^*{=}j)
471	  = \frac{\alpha_U}{\operatorname{Var}(T)}\,\operatorname{Var}(T\mid A^*{=}j)
472	  \quad\forall\;j,
473	\]
474	and $\lambda\,\mathbb{E}[\operatorname{Cov}(T,U\mid A^*)]=\frac{\lambda\alpha_U}{\operatorname{Var}(T)}\,D(C)$, yielding the constant first term after division by $D(C)$.
475	\end{proof}
476	
477	This decomposition reveals that \emph{misclassification does not affect the confounding component}.
478	The confusion matrix $C$ modulates only the mediation-type leakage $B_{\mathrm{med}}(C)$, which has the same structure as in~§\ref{app:mediation}.
479	
480	\paragraph{Endpoint analysis.}
481	At $C=I$: $B_{\mathrm{med}}(I)=0$ (controlling $A$ blocks the $T\to A\to Y$ path), and $\operatorname{plim}\hat\tau(I)=\lambda\alpha_U/\operatorname{Var}(T)$ (pure confounding residual).
482	
483	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$: $B_{\mathrm{med}}=\operatorname{Cov}(T,f(A))/\operatorname{Var}(T)$, and $\operatorname{plim}\hat\tau_{\mathrm{nc}}=[\operatorname{Cov}(T,f(A))+\lambda\alpha_U]/\operatorname{Var}(T)$, the naive regression coefficient with no controls.
484	
485	\paragraph{Empirical Finding (Front-door sign preservation).}
486	\label{find:fd_sign}
487	Since $B_{\mathrm{med}}(C)$ has the same structure as the mediation bias (§\ref{app:mediation})---interpolating between $0$ at $C{=}I$ and $\operatorname{Cov}(T,f(A))/\operatorname{Var}(T)$ at $C$ uniform---sign preservation holds whenever the two endpoints have the same sign:
488	\[
489	  \operatorname{sign}\!\bigl(\lambda\alpha_U\bigr)
490	  = \operatorname{sign}\!\bigl(\lambda\alpha_U + \operatorname{Cov}(T,f(A))\bigr).
491	\]
492	This result is verified numerically for $100{,}000$ independently sampled column-stochastic matrices $C$.
493	
494	\paragraph{Verification for paper parameters ($K{=}3$).}
495	With $\alpha_U{=}1.0$, $\lambda{=}1.0$, $\boldsymbol{\beta}{=}(0,1.0,{-}0.5)$, $\boldsymbol{\gamma}{=}(0,0.5,{-}0.3)$, $\boldsymbol{\delta}{=}(0,1.0,{-}0.8)$:
496	\begin{align*}
497	  \lambda\alpha_U/\operatorname{Var}(T) &= 1.0\times 1.0\,/\,2.0 = 0.500,\\
498	  \operatorname{Cov}(T,f(A))/\operatorname{Var}(T) &= 0.594\,/\,2.0 = 0.297.
499	\end{align*}
500	Both components are positive, so $\operatorname{plim}\hat\tau(C)\in[0.500,\,0.797]>0$ for all $C$.
501	
502	\subsection{Exposure Topology: Sign Reversal Counterexample}
503	\label{app:exposure}
504	
505	\begin{proposition}[Exposure sign reversal]
506	\label{prop:exp_counter}
507	For $K{=}3$ with $A$ as the treatment variable, there exist a marginal distribution $\mathbf{p}$, treatment effects $\boldsymbol{\beta}$, and a column-stochastic $C$ with $C_{kk}>0.5$ for all $k$, such that $\operatorname{sign}(\operatorname{plim}\hat\beta_1)\neq\operatorname{sign}(\beta_1)$.
508	\end{proposition}
509	
510	\begin{proof}[Construction]
511	Consider the exposure DGP $Y = \beta_1 D_1 + \beta_2 D_2 + \varepsilon_Y$ with:
512	\begin{itemize}
513	  \item Uniform prior: $\mathbf{p}=(1/3,\,1/3,\,1/3)$.
514	  \item True effects: $\beta_1=1$,\; $\beta_2=-10$.
515	\end{itemize}
516	Choose the confusion matrix
517	\[
518	  C = \begin{pmatrix}
519	    0.60 & 0.10 & 0.10\\
520	    0.10 & 0.60 & 0.39\\
521	    0.30 & 0.30 & 0.51
522	  \end{pmatrix},\qquad
523	  C_{kk}\in\{0.60,\,0.60,\,0.51\},\;\text{all}>0.5.
524	\]
525	Column sums are $1$ (verifiable by inspection).
526	
527	The OLS estimator regresses $Y$ on $(1,D_1^*,D_2^*)$.
528	The plim of $\hat\beta_j$ equals $\mathbb{E}[Y\mid A^*{=}j]-\mathbb{E}[Y\mid A^*{=}0]$, where
529	\[
530	  \mathbb{E}[Y\mid A^*{=}j] = \sum_{k=0}^{2} P(A{=}k\mid A^*{=}j)\,\beta_k
531	  = \sum_{k=1}^{2}\frac{C_{jk}\,p_k}{q_j}\,\beta_k.
532	\]
533	
534	\emph{Marginal distribution of $A^*$:}
535	\begin{align*}
536	  q_0 &= \tfrac{1}{3}(0.60+0.10+0.10)=0.267,\\
537	  q_1 &= \tfrac{1}{3}(0.10+0.60+0.39)=0.363,\\
538	  q_2 &= \tfrac{1}{3}(0.30+0.30+0.51)=0.370.
539	\end{align*}
540	
541	\emph{Conditional means:}
542	\begin{align*}
543	  \mathbb{E}[Y\mid A^*{=}0]
544	  &= \frac{0.10\times\tfrac{1}{3}\times 1 + 0.10\times\tfrac{1}{3}\times({-}10)}{0.267}
545	  = \frac{0.0333-0.3333}{0.267} = -1.125,\\[4pt]
546	  \mathbb{E}[Y\mid A^*{=}1]
547	  &= \frac{0.60\times\tfrac{1}{3}\times 1 + 0.39\times\tfrac{1}{3}\times({-}10)}{0.363}
548	  = \frac{0.200-1.300}{0.363} = -3.028,\\[4pt]
549	  \mathbb{E}[Y\mid A^*{=}2]
550	  &= \frac{0.30\times\tfrac{1}{3}\times 1 + 0.51\times\tfrac{1}{3}\times({-}10)}{0.370}
551	  = \frac{0.100-1.700}{0.370} = -4.324.
552	\end{align*}
553	
554	\emph{Estimated coefficient:}
555	\[
556	  \operatorname{plim}\hat\beta_1 = \mathbb{E}[Y\mid A^*{=}1]-\mathbb{E}[Y\mid A^*{=}0]
557	  = -3.028-(-1.125) = \mathbf{-1.903}.
558	\]
559	The true $\beta_1=+1>0$ but $\operatorname{plim}\hat\beta_1=-1.903<0$: \textbf{sign reversal}.
560	
561	\emph{Mechanism.}
562	The large off-diagonal entry $C_{12}=0.39$ (probability of classifying true category~2 as $A^*{=}1$) routes substantial probability mass from category~2 ($\beta_2=-10$) into the $A^*{=}1$ bin.
563	Despite $C_{11}=0.60>0.5$, the contamination from the strongly negative $\beta_2$ overwhelms the positive $\beta_1$, reversing the sign of the estimated effect for category~1.
564	This failure mode is structurally impossible at $K{=}2$: a $2{\times}2$ column-stochastic matrix with $C_{kk}>0.5$ has the form $C=\bigl(\begin{smallmatrix}a&1{-}b\\1{-}a&b\end{smallmatrix}\bigr)$ with $a,b>0.5$, and the single coefficient $\hat\beta_1$ is a positive-weighted average of $\beta_1$, preserving sign.
565	For $K{\geq}3$, the additional degrees of freedom in $C$ permit cross-contamination between categories with opposite-sign effects.
566	\end{proof}
567	
568	\subsection{Summary of Conditions}
569	\label{app:conditions}
570	
571	\begin{table}[h]
572	\centering
573	\small
574	\begin{tabular}{lccc}
575	\toprule
576	\textbf{Topology} & \textbf{Sufficient condition} & \textbf{Status} & \textbf{Paper DGP} \\
577	\midrule
578	Confounding & $\operatorname{sign}(\tau)=\operatorname{sign}(\tau{+}B_{\mathrm{OV}})$ & Proved & $\checkmark$ ($2.0$ vs $2.3$)\\
579	Collider & $|\tau|>\bar{B}_{\mathrm{col}}$ (Prop.~\ref{prop:col_gen}) & Proved & $\checkmark$ ($1.0$ vs $0.15$)\\
580	\midrule
581	Mediation & $\operatorname{sign}(\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{total}})$ & Empirical & $\checkmark$ ($0.5$ vs $0.85$)\\
582	M-bias & Bias is attenuating (toward $\tau$) & Empirical & $\checkmark$ \\
583	Front-door & $\operatorname{sign}(\lambda\alpha_U)=\operatorname{sign}(\lambda\alpha_U{+}\operatorname{Cov}(T,f))$ & Empirical & $\checkmark$ ($0.50$ vs $0.80$)\\
584	\midrule
585	Exposure & Not guaranteed for $K\geq 3$ & Counterex. & See §\ref{app:exposure} \\
586	IV & Not guaranteed (denominator instability) & --- & --- \\
587	\bottomrule
588	\end{tabular}
589	\caption{Sufficient conditions for sign preservation under non-differential misclassification.
590	``Proved'' = algebraic proof via Cauchy--Schwarz (confounding) or Berkson attenuation (collider).
591	``Empirical'' = verified across 100{,}000 random column-stochastic matrices with zero violations; analytic proof for general $K$ remains open.
592	All conditions are on DGP parameters (not on $C$): once satisfied, sign preservation holds for all column-stochastic $C$ with $C_{kk}>0$.}
593	\label{tab:sign_conditions}
594	\end{table}
595	
596	\paragraph{Structural argument for M-bias topology.}
597	\emph{M-bias:} The M-structure creates a backdoor path through two latent common causes.
598	Misclassification of $A$ weakens the statistical association along this backdoor path, reducing the spurious correlation rather than amplifying it.
599	The bias therefore interpolates between the full M-bias (perfect classification, $\delta{=}0$) and zero (no classification information, $\delta{\to}\delta_{\max}$), monotonically non-increasing in $\delta$.
600	
601	\paragraph{Remark.}
602	The sign preservation conditions for confounding, mediation, collider, and front-door are conditions on the DGP parameters (the relative strength of the causal effect versus the confounding, indirect, or collider-induced bias), not on the confusion matrix $C$.
603	Once the condition is satisfied, sign preservation holds for \emph{all} column-stochastic $C$ with $C_{kk}>0$---no diagonal-dominance restriction is needed.
604	Conversely, if the condition fails (i.e., the omitted-variable or total-effect estimate has the opposite sign from $\tau$), then there exist confusion matrices that produce sign reversal.
605	For the DGP parameters used throughout our experiments, the conditions are comfortably satisfied.
606	The sign-alignment condition is violated when the confounder has opposing effects on treatment and outcome (e.g., $\gamma_A > 0$ on $T$ but $\gamma_A < 0$ on $Y$), producing $\operatorname{sign}(\tau) \neq \operatorname{sign}(\tau_{\mathrm{OV}})$. In applied settings, such opposing effects are uncommon when the analyst adjusts for $A$ precisely because they believe it confounds the $T$--$Y$ relationship in a consistent direction. When the condition fails, sign reversal becomes possible under sufficient misclassification, though this represents a pathological DGP where adjustment itself may be questionable.
607	
608	\section{Supplementary Tables, Figures, and Algorithm}
609	\label{app:supplementary}
610	
611	\subsection{Binarization Collapse}
612	\label{app:binarization}
613	
614	Collapsing $K$-class annotations to binary before analysis discards multi-class error structure. We quantify ``binarization collapse'' as $\Delta = |\text{bias}_{K} - \text{bias}_{K \to 2}|$.
615	
616	For $K{=}3$, binarization introduces additional bias varying 154$\times$ across topologies: from $\bar{\Delta}{=}0.006$ (M-bias) to $\bar{\Delta}{=}0.926$ (IV). Exposure and IV also introduce sign flips during binarization (14\% and 17.5\%), a phenomenon absent in the other topologies (Figure~\ref{fig:binarization}).
617	
618	\begin{figure*}[h]
619	\centering
620	\includegraphics[width=\textwidth]{fig3_asv_ranking.pdf}
621	\caption{ASV sensitivity ranking across topologies. Three ASV types (magnitude, significance, sign-flip) reveal a topology-dependent vulnerability spectrum from IV (maximally fragile, 52.6\% sign reversal; sign-flip ASV $= 1.1$--$6.7$) to M-bias (immune, ASV $= \infty$).}
622	\label{fig:asv_ranking}
623	\end{figure*}
624	
625	\begin{table}[h]
626	\centering
627	\caption{ASV type applicability and sensitivity across DAG topologies. Magnitude ASV at $\tau{=}0.5$, 10\% threshold. Power at $\tau{=}0.05$ significance filter. ---: not applicable.}
628	\label{tab:asv_grid}
629	\small
630	\begin{tabular}{lcccl}
631	\toprule
632	\textbf{Topology} & \textbf{Mag. ASV} & \textbf{Signif.} & \textbf{Sign-flip} & \textbf{Rank} \\
633	\midrule
634	IV & 0.101--0.607 & 0\% & 1.1--6.7 & 1 (fragile) \\
635	Front-door & 0.064--0.387 & 100\% & --- & 2 \\
636	Confounding & 0.081--0.487 & 100\% & --- & 3 \\
637	Mediation & 0.076--0.454 & 0\% & --- & 4 \\
638	Collider & 0.338--2.028 & 0\% & --- & 5 \\
639	M-bias & $\infty$ & 96--100\% & --- & 6 (immune) \\
640	Exposure & --- & --- & 83.4\%$^*$ & --- \\
641	\bottomrule
642	\multicolumn{5}{l}{\scriptsize $^*$Fraction of $C_0$ with $\tau_{\text{sign\_flip}} < 1$. Exposure uses sign-flip ASV exclusively.}
643	\end{tabular}
644	\end{table}
645	
646	\begin{figure}[h]
647	\centering
648	\includegraphics[width=\columnwidth]{fig7_dirichlet_overlay.pdf}
649	\caption{Empirical LLM confusion matrices overlaid on theoretical violation-rate curves (exposure, left; IV, right). Theoretical curves are derived from $K{=}3$ Dirichlet random matrices; empirical points are positioned at their minimum diagonal entry. Markers denote datasets (circles: HumAID $K{=}10$; squares: VAST $K{=}3$; triangles: CivilComments $K{=}2$).}
650	\label{fig:dirichlet_overlay}
651	\end{figure}
652	
653	\begin{figure}[h]
654	\centering
655	\includegraphics[width=\columnwidth]{fig4_binarization.pdf}
656	\caption{Binarization collapse $\Delta$ across topologies. Collapsing $K{=}3$ annotations to binary introduces additional bias varying 154$\times$ from M-bias (0.006) to IV (0.926).}
657	\label{fig:binarization}
658	\end{figure}
659	
660	\begin{figure}[h]
661	\centering
662	\includegraphics[width=\columnwidth]{fig6_asv_heatmap.pdf}
663	\caption{ASV magnitude ranges across topologies for HumAID ($K{=}10$). Left: magnitude ASV ($\delta^*$) range across 8 LLM configurations; lower values indicate greater fragility. ``Safe'' topologies never exceed the 10\% bias threshold. Right: percentage of configurations flagged as ASV-unsafe.}
664	\label{fig:asv_heatmap}
665	\end{figure}
666	
667	\begin{table}[h]
668	\centering
669	\caption{RMSE reduction (\%) by correction method and DAG topology (mean across 6 error structures, $N_{\text{sim}}{=}1{,}000$). Positive = reduced RMSE; negative = increased RMSE. Naive/MLA show 0.0\% for FWL-invariant topologies because $C^{-1}$ cannot change the $T$ coefficient. \textbf{Bold}: best method per topology; \underline{underline}: best gold-free method.}
670	\label{tab:correction}
671	\small
672	\begin{tabular}{lccccc}
673	\toprule
674	\textbf{Topology} & \textbf{Naive} & \textbf{MLA} & \textbf{DSL} & \textbf{SIMEX} & \textbf{PPI++} \\
675	\midrule
676	Confounding & 0.0 & 0.0 & \underline{48.0} & 35.1 & \textbf{83.2} \\
677	Mediation & 0.0 & 0.0 & \underline{52.9} & 39.1 & \textbf{54.1} \\
678	Collider & 0.0 & 0.0 & $-$92.6 & \underline{31.8} & \textbf{50.5} \\
679	M-bias & 0.0 & 0.0 & $-$267 & \textbf{\underline{0.1}} & $-$88.0 \\
680	\midrule
681	Front-door & $-$52.7 & $-$111.5 & \underline{$-$29.0} & $-$62.4 & \textbf{74.1} \\
682	Exposure & $-$44.8 & $-$89.0 & $-$59.5 & \underline{$-$9.8} & \textbf{75.5} \\
683	IV & $-$40.4 & $-$58.7 & $-$206.1 & \underline{59.4} & \textbf{79.4} \\
684	\midrule
685	Grand mean & $-$19.7 & $-$37.0 & $-$79.0 & 13.3 & \textbf{47.0} \\
686	\bottomrule
687	\end{tabular}
688	\end{table}
689	
690	\paragraph{Error structures used in correction experiments.}
691	The six confusion matrix structures used for Table~\ref{tab:correction} are:
692	(1)~\emph{Diagonal-dominant}: $C_{kk}{=}0.7$, off-diagonal uniform;
693	(2)~\emph{Moderate noise}: $C_{kk}{=}0.5$, off-diagonal uniform;
694	(3)~\emph{Near-permutation}: $C_{kk}{=}0.4$, largest off-diagonal 0.5;
695	(4)~\emph{Asymmetric}: $C_{kk}$ varies (0.8, 0.5, 0.3);
696	(5)~\emph{Block confusion}: two classes confused ($C_{12}{=}C_{21}{=}0.4$), third clean;
697	(6)~\emph{Heavy noise}: $C_{kk}{=}0.4$, off-diagonal uniform.
698	All are column-stochastic with $K{=}3$. Results are averaged across all six structures.
699	
700	\begin{algorithm}[h]
701	\caption{Correction method selection for LLM-annotated causal inference.}
702	\label{alg:correction}
703	\small
704	\begin{algorithmic}[1]
705	\REQUIRE DAG topology $\mathcal{T}$, gold-label availability $G \in \{\textsc{yes}, \textsc{no}\}$
706	\ENSURE Recommended method $M$, risk level $R$
707	\STATE
708	\STATE \textbf{Step 1: Assess risk level}
709	\IF{$\mathcal{T} \in \{\text{M-bias}\}$}
710	    \STATE $R \gets \textsc{Low}$ \COMMENT{$|\text{bias}| < 0.04$ for all $C$}
711	\ELSIF{$\mathcal{T} \in \{\text{Conf., Med., Coll., Front-door}\}$}
712	    \STATE $R \gets \textsc{Medium}$ \COMMENT{bounded bias, no sign reversal}
713	\ELSE
714	    \STATE $R \gets \textsc{High}$ \COMMENT{Exposure, IV: sign reversal 83.4\% / 52.6\%}
715	\ENDIF
716	\STATE
717	\STATE \textbf{Step 2: Select correction method}
718	\IF{$G = \textsc{yes}$}
719	    \IF{$\mathcal{T} = \text{M-bias}$}
720	        \STATE $M \gets \textsc{None}$ \COMMENT{PPI++ RMSE red.\ $-$88.0\%; no correction preferred}
721	    \ELSE
722	        \STATE $M \gets \text{PPI++}$ \COMMENT{47.0\% RMSE red., 96.8\% coverage}
723	    \ENDIF
724	\ELSE
725	    \STATE \COMMENT{no gold labels}
726	    \IF{$\mathcal{T} \in \{\text{Confounding, Mediation}\}$}
727	        \STATE $M \gets \text{DSL}$ \COMMENT{48.0\% / 52.9\% RMSE reduction}
728	    \ELSIF{$\mathcal{T} = \text{IV}$}
729	        \STATE $M \gets \text{MC-SIMEX}$ \COMMENT{59.4\% RMSE reduction}
730	    \ELSIF{$\mathcal{T} \in \{\text{Collider, M-bias}\}$}
731	        \STATE $M \gets \text{MC-SIMEX}$ \COMMENT{31.8\% / 0.1\% RMSE reduction}
732	    \ELSE
733	        \STATE $M \gets \emptyset$; flag: acquire gold labels \COMMENT{no reliable gold-free method}
734	    \ENDIF
735	\ENDIF
736	\STATE
737	\STATE \textbf{Step 3: FWL invariance warning}
738	\IF{$\mathcal{T} \in \{\text{Conf., Med., Coll., M-bias}\}$}
739	    \STATE Skip Naive plug-in and MLA \COMMENT{0\% bias red.\ on $T$ coeff.}
740	\ENDIF
741	\RETURN $(M, R)$
742	\end{algorithmic}
743	\end{algorithm}
744	
745	\subsection{Applied Illustration: ClinicalBERT Case Study}
746	\label{app:case_study}
747	
748	To demonstrate the framework's end-to-end utility, we apply it retrospectively to \citet{lee_wood_doughty2024}, who use ClinicalBERT to classify patient smoking status ($K{=}4$: never, past, current, unknown) from clinical notes and control for this predicted confounder when estimating the causal effect of echocardiography on mortality in 4{,}735 MIMIC-III sepsis patients.
749	Our taxonomy identifies this as a \emph{confounding topology}: the annotated variable enters as a confounder between treatment and outcome.
750	Three conclusions follow directly.
751	First, the zero sign-flip guarantee for confounding (Table~\ref{tab:taxonomy}) ensures that the estimated protective effect (OR~$= 0.89$) cannot reverse direction due to annotation error---a reassurance unavailable without topology-specific analysis.
752	Second, the FWL invariance result implies that any correction reducing to $C^{-1}$ applied to the dummy-coded confounder achieves exactly 0\% bias reduction for the treatment coefficient; naive plug-in is provably futile here.
753	Third, our correction guidance ranks PPI++ (83.2\% RMSE reduction for confounding) above MC-SIMEX (35.1\%) when gold labels are available---a concrete recommendation the original study lacked.
754	This example illustrates the intended workflow: DAG identification $\to$ topology-specific guarantees $\to$ correction method selection.
755	
756	\subsection{IV Wald Estimator: Diagonal-Dominance Subspaces}
757	\label{sec:iv_dirichlet_subspace}
758	
759	Section~\ref{sec:taxonomy_results} reports a 52.6\% Wald sign-flip rate
760	over the full Dirichlet$(1,1,1)$ prior. Because realistic LLM confusion
761	matrices are diagonal-dominant, we replicate the exposure-DAG stratification
762	for the IV topology, restricting the sample
763	space to $\{C : \min_k C_{kk} \geq d\}$ for $d \in \{0, 0.5, 0.7, 0.9\}$
764	(100{,}000 random matrices per threshold).
765	
766	\begin{table}[h]
767	\centering
768	\caption{IV Wald estimator bias by minimum-diagonal subspace ($K{=}3$, $\tau_{\text{true}}{=}1.41$).
769	Rates over 100{,}000 Dirichlet-truncated random $C$ per threshold.}
770	\label{tab:iv_dirichlet_subspace}
771	\small
772	\begin{tabular}{lcccc}
773	\toprule
774	\textbf{Subspace} & \textbf{Violation} & \textbf{Sign Flip} & \textbf{Amplif.} & \textbf{Worst} \\
775	\midrule
776	Full           & 100.0\% & 51.7\% & 48.3\% & $10^{5}\!\times$ \\
777	$d \geq 0.5$   & 100.0\% & 0.0\%  & 100.0\% & $28.6\times$ \\
778	$d \geq 0.7$   & 100.0\% & 0.0\%  & 100.0\% & $2.4\times$ \\
779	$d \geq 0.9$   & 100.0\% & 0.0\%  & 100.0\% & $1.2\times$ \\
780	\bottomrule
781	\end{tabular}
782	\end{table}
783	
784	The contrast with exposure is instructive: at $d{\geq}0.7$, exposure violation drops to 13.7\% (sign reversal 2.1\%, amplification 11.7\%), while IV maintains 100\% violation with pure amplification. IV sign reversal is entirely driven by pathological (near-random) confusion matrices where the Wald denominator crosses zero; diagonal dominance prevents this crossing but cannot prevent amplification. Even at $d{\geq}0.9$, the Wald estimator inflates $|\tau|$ by up to $1.24\times$ with probability~1.
785	
786	\subsection{Non-Differential Assumption Stress Test}
787	\label{sec:nondiff_stress}
788	
789	Our main analysis assumes non-differential misclassification: the confusion matrix $C$ does not depend on the outcome $Y$. To assess sensitivity to violations of this assumption, we conduct a stress test on the exposure topology ($K{=}3$, $\min_k C_{kk} \geq 0.7$, 10{,}000 random matrices per $\varepsilon$). For each base matrix $C_0$, observations with $Y > \text{median}(Y)$ are misclassified using a perturbed matrix $\tilde{C} = \text{renormalize}(C_0 + \varepsilon \cdot \Delta)$ where $\Delta_{jk} \sim \text{Uniform}(-1,1)$ for $j \neq k$, while observations with $Y \leq \text{median}(Y)$ retain $C_0$.
790	
791	\begin{table}[h]
792	\centering
793	\small
794	\caption{Effect of differential misclassification on bias violation rates (exposure DAG, $K{=}3$, $\min_k C_{kk} \geq 0.7$, $N{=}50{,}000$ MC samples per trial).}
795	\label{tab:nondiff_stress}
796	\begin{tabular}{cccc}
797	\toprule
798	$\varepsilon$ & Sign-Flip (\%) & Amplification (\%) & Any Violation (\%) \\
799	\midrule
800	0.00 & 2.0 & 11.5 & 13.3 \\
801	0.01 & 2.4 & 12.4 & 14.7 \\
802	0.05 & 2.8 & 13.0 & 15.7 \\
803	0.10 & 4.5 & 16.7 & 20.9 \\
804	\bottomrule
805	\end{tabular}
806	\end{table}
807	
808	The $\varepsilon{=}0$ baseline (13.3\% violation) closely matches the analytical result (13.7\%) from Section~\ref{sec:taxonomy_results}. Even at $\varepsilon{=}0.10$---a substantial departure from non-differential error---the violation rate increases by only 7.6 percentage points. Small departures ($\varepsilon \leq 0.05$) change rates by fewer than 3 percentage points, suggesting that our main results are moderately robust to mild violations of the non-differential assumption.
809	
810	\paragraph{Extended stress test.}
811	An extended stress test across 96 configurations (4 topologies $\times$ 2 $K$ $\times$ 3 CM qualities $\times$ 4 $\varepsilon$, 100 MC replications each; Table~\ref{tab:stress-test}) confirms these patterns broadly: at $\varepsilon{=}0$, sign-flip rates are zero for all configurations; at $\varepsilon{=}0.10$, the maximum sign-flip rate is 7\% (IV, low-quality $C_{kk}{=}0.4$, $K{=}3$). At $K{=}10$, sign-flip rates remain zero for all topologies and $\varepsilon$ values, suggesting that higher $K$ provides additional robustness to differential misclassification.
812	
813	\input{exp_a_stress_test_table.tex}
814	
815	\subsection{Robustness to Nonlinear DGP}
816	\label{sec:logistic_dgp}
817	
818	We replace the linear structural equations with $Y \sim \text{Bernoulli}(\sigma(\mathbf{x}^\top\boldsymbol{\beta}))$ and estimate via logistic regression (control function for IV) for three representative topologies, using $K{=}3$, six real VAST confusion matrices, 500 MC replications, and $N{=}10{,}000$. Mean sign-flip rates across the six CMs:
819	
820	\begin{center}
821	\small
822	\begin{tabular}{lcccc}
823	\toprule
824	Topology & Linear SF$_\tau$ & Logistic SF$_\tau$ & Linear SF$_\text{any}$ & Logistic SF$_\text{any}$ \\
825	\midrule
826	Confounding & 0.000 & 0.000 & 0.573 & 0.559 \\
827	Exposure & --- & --- & 0.577 & 0.574 \\
828	IV & 0.071 & 0.065 & 0.071 & 0.565 \\
829	\bottomrule
830	\end{tabular}
831	\end{center}
832	
833	Treatment-effect sign-flip rates (SF$_\tau$) differ by $< 0.01$ across all topologies. The SF$_\text{any}$ discrepancy for IV reflects estimator dimensionality: the control function includes a residual coefficient prone to sign noise; the core comparison is SF$_\tau$, where both estimators agree ($\approx 7\%$). Linear and logistic DGPs produce virtually identical sign-flip patterns ($|\Delta\,\text{SF}_\tau| < 0.02$).
834	
835	\subsection{Bootstrap Uncertainty of ASV}
836	\label{sec:bootstrap_asv}
837	
838	We assess confusion-matrix estimation uncertainty by bootstrapping label pairs from HumAID DeepSeek zero-shot ($K{=}10$, $n{=}1{,}500$): resample with replacement $B{=}1{,}000$ times, re-estimate $C_0$, and recompute magnitude ASV $\delta^*$ at a 10\% bias threshold.
839	
840	\begin{center}
841	\small
842	\begin{tabular}{lccc}
843	\toprule
844	Topology & $\delta^*$ (point) & 95\% CI & Valid / 1000 \\
845	\midrule
846	Confounding & --- & --- & 0 \\
847	Exposure & 0.937 & [0.602, 1.363] & 907 \\
848	IV & 0.754 & [0.435, 1.290] & 902 \\
849	\bottomrule
850	\end{tabular}
851	\end{center}
852	
853	Confounding never reaches the 10\% threshold across all 1{,}000 bootstraps, confirming robustness. For IV, the 95\% CI spans a $3{\times}$ range (0.435 to 1.290); practitioners should bootstrap $C_0$ rather than rely on a point estimate when ASV is near the decision boundary.
854	
855	\begin{figure}[h]
856	\centering
857	\includegraphics[width=0.9\columnwidth]{exp_c_bootstrap_figure.pdf}
858	\caption{Bootstrap distribution of magnitude ASV $\delta^*$ ($B{=}1{,}000$) for HumAID DeepSeek zero-shot ($K{=}10$). Dashed line: point estimate; shaded: 95\% CI.}
859	\label{fig:bootstrap_asv}
860	\end{figure}
861	
862	\subsection{ASV Stability Across DGP Parameters}
863	\label{sec:asv_stability}
864	
865	We test whether ASV rankings are stable across different data-generating process (DGP) configurations by varying the treatment-effect vector $\boldsymbol{\beta}$ across three settings: alternating-large ($\boldsymbol{\beta}=[0,\,1.0,\,-0.5]$), same-sign ($\boldsymbol{\beta}=[0,\,0.5,\,0.3]$), and alternating-small ($\boldsymbol{\beta}=[0,\,0.2,\,-0.1]$), with $K{=}3$, $\tau{=}0.5$, and five $C_0$ diagonal values $\in\{0.5,0.6,0.7,0.8,0.9\}$.
866	
867	\input{exp_e_asv_stability_table.tex}
868	
869	Three patterns emerge (Table~\ref{tab:asv_stability}). First, IV magnitude ASV is identical across all three DGPs ($\delta^*{=}0.203$). This is a mathematical identity, not an empirical finding: the Wald estimator $\hat{\tau}_{\text{IV}} = \text{RF}/\text{FS}$ has $\boldsymbol{\beta}$ in both numerator and denominator, and the ratio depends only on $C$ and the first-stage structure, making ASV invariant to $\boldsymbol{\beta}$ by construction. Second, exposure ASV depends on the coefficient ratio structure: alternating-large ($\beta_2/\beta_1 = -0.5$) and alternating-small ($\beta_2/\beta_1 = -0.5$) share the same ratio and yield identical $\delta^*{=}0.090$, while same-sign ($\beta_2/\beta_1 = 0.6$) gives $\delta^*{=}0.223$---thus the experiment provides two distinct sign-structure conditions, not three. Third, confounding ASV depends on effect magnitudes: only alternating-large triggers the 10\% threshold ($\delta^*{=}0.348$); smaller effects never reach 10\% bias.
870	
871	Confounding is consistently the most robust topology (highest ASV or no violation), and M-bias remains immune (not shown). However, the relative fragility of exposure vs.\ IV inverts with coefficient sign structure: under alternating signs, exposure is most fragile ($0.090 < 0.203$); under same-sign effects, IV is most fragile ($0.203 < 0.223$). Practitioners should compute ASV with their specific DGP rather than relying on generic rankings.
872	
873	\subsection{Extended Conjecture Verification}
874	\label{sec:conjecture_verify}
875	
876	We test envelope monotonicity (Conjecture~\ref{conj:monotone}) by sampling 10{,}000 random $C_0$ matrices from Dirichlet$(1,\dots,1)$ per topology for $K \in \{3,5,7\}$ (210{,}000 total), sweeping $\delta$ in steps of 0.01, and counting matrices with at least one non-monotonic step exceeding tolerance $10^{-12}$. Bias at each $\delta$ is computed via analytic probability limits using Gauss--Hermite quadrature (100 points), eliminating sampling noise entirely.
877	
878	\begin{table}[h]
879	\centering
880	\small
881	\caption{Envelope monotonicity violations per 10{,}000 random $C_0$ matrices. ``Worst mag.''\ is the largest single-step deviation $|B(\delta_{i+1})|-|B(\delta_i)|$ in the non-monotonic direction.}
882	\label{tab:conjecture_verify}
883	\begin{tabular}{lccccc}
884	\toprule
885	\textbf{Topology} & $K{=}3$ & $K{=}5$ & $K{=}7$ & \textbf{Worst mag.} & \textbf{Direction} \\
886	\midrule
887	Confounding & 8467 & 8063 & 7892 & 0.011 & non-dec \\
888	Mediation   & 8236 & 7905 & 7893 & 0.013 & non-dec \\
889	Collider    & 8683 & 7669 & 7570 & 0.005 & non-inc \\
890	Exposure    & 485  & 205  & 77   & 0.056 & non-dec \\
891	M-bias      & 9791 & 7783 & 7399 & 0.002 & non-inc \\
892	IV          & 7433 & 6015 & 5711 & $>10^6$ & non-dec \\
893	Front-door  & 8429 & 8079 & 7899 & 0.013 & non-dec \\
894	\bottomrule
895	\end{tabular}
896	\end{table}
897	
898	Violation counts are high (60--97\% of matrices), but magnitudes are negligible for non-IV topologies: all worst-case deviations fall below 0.06 ($<$6\% of the respective $\tau$). These results are computed from analytic probability limits with zero sampling noise, confirming the violations are structural properties of multi-class confusion matrices rather than numerical artifacts. IV deviations reflect Wald estimator singularities when the first-stage coefficient passes near zero---this is a property of the Wald estimator, not of the ASV parameterization. Adversarial search (500 restarts per configuration, $K \in \{3,5\}$) finds genuine counterexamples for all topologies except IV $K{=}3$, confirming that strict monotonicity does not hold universally. The bias envelope is $\varepsilon$-approximately monotonic with $\varepsilon < 0.06$ for all six non-IV topologies, supporting the practical validity of ASV as a sensitivity tool at any meaningful bias threshold.
899	
900	\section{Notation}
901	\label{app:notation_table}
902	
903	\begin{table}[h]
904	\centering
905	\small
906	\caption{Key notation used throughout the paper.}
907	\label{tab:notation}
908	\begin{tabular}{cl}
909	\toprule
910	\textbf{Symbol} & \textbf{Description} \\
911	\midrule
912	$K$ & Number of annotation categories \\
913	$C$ & Column-stochastic confusion matrix, $C_{jk} = P(A^*{=}j \mid A{=}k)$ \\
914	$A$, $A^*$ & True and observed (misclassified) annotation \\
915	$T$ & Treatment variable \\
916	$Y$ & Outcome variable \\
917	$\tau$ & Causal effect of interest \\
918	$\delta$ & ASV perturbation parameter, $C(\delta) = (1{-}\delta)I + \delta C_0$ \\
919	$\delta^*$ & Critical ASV value (magnitude/significance/sign-flip) \\
920	$B(C)$ & Bias function, $= \operatorname{plim}(\hat{\tau}) - \tau$ \\
921	$\beta_k$ & Treatment effect coefficient for category $k$ \\
922	$D_k$ & Dummy variable for category $k$ \\
923	\bottomrule
924	\end{tabular}
925	\end{table}
926	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76905a48-91dc-4eaa-b1fd-2e91eed5bf2a",
  "isSidechain": false,
  "promptId": "e832977f-06f5-437f-9468-12b340b28a19",
  "type": "user",
  "uuid": "33e7e5ed-3edf-4b51-820e-1043379010fb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
      "content": "\\section{Proofs of Proposition~\\ref{prop:signflip} and Theorem~\\ref{thm:monotone}}\n\\label{app:proof}\n\nWe provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Empirical Finding~1), and the monotonicity proof for confounding (Theorem~\\ref{thm:monotone}).\nThroughout, $A\\in\\{0,1,\\dots,K{-}1\\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\\mid A{=}k)$.\nWe use category~0 as the reference and let $D_j=\\mathbf{1}(A{=}j)$, $D_j^*=\\mathbf{1}(A^*{=}j)$ for $j=1,\\dots,K{-}1$.\n\n\\subsection{Notation and Key Identities}\n\\label{app:notation}\n\nUnder non-differential misclassification, the misclassified moments factor linearly through $C$.\nDefine the population vectors:\n\\begin{align}\n  q_j &= P(A^*{=}j) = \\textstyle\\sum_k C_{jk}\\,p_k, \\label{eq:q}\\\\\n  \\mathrm{ct}_j &= \\mathbb{E}[T\\cdot D_j^*] = \\textstyle\\sum_k C_{jk}\\,\\mathbb{E}[T\\cdot D_k], \\label{eq:ct}\\\\\n  \\mathrm{cy}_j &= \\mathbb{E}[Y\\cdot D_j^*] = \\textstyle\\sum_k C_{jk}\\,\\mathbb{E}[Y\\cdot D_k]. \\label{eq:cy}\n\\end{align}\nWrite $q = Cp$, $\\mathrm{ct} = C\\,\\mathbb{E}[T\\cdot D]$, and $\\mathrm{cy} = C\\,\\mathbb{E}[Y\\cdot D]$, where $D=(D_0,\\dots,D_{K-1})^\\top$.\n\n\\subsection{Frisch--Waugh--Lovell Decomposition}\n\\label{app:fwl}\n\nFor topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\\dots,D_{K-1}^*)$.\nBy the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:\n\\begin{equation}\n  \\operatorname{plim}\\hat{\\tau}(C)\n  = \\frac{\\mathbb{E}[\\tilde{T}\\,\\tilde{Y}]}{\\mathbb{E}[\\tilde{T}^2]},\n  \\label{eq:fwl}\n\\end{equation}\nwhere $\\tilde{T}=T-\\mathbb{E}[T\\mid A^*]$ and $\\tilde{Y}=Y-\\mathbb{E}[Y\\mid A^*]$ are residuals from projecting onto $(1,D_1^*,\\dots,D_{K-1}^*)$.\n\n\\begin{lemma}[Bias decomposition]\n\\label{lem:bias_decomp}\nSuppose $Y = \\tau T + f(A) + \\varepsilon_Y$ with $\\varepsilon_Y \\perp (T, A, A^*)$.\nThen\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau(C) = \\tau + \\frac{R(C)}{D(C)},\n  \\label{eq:bias_decomp}\n\\end{equation}\nwhere\n\\begin{align}\n  R(C) &= \\mathbb{E}\\bigl[\\operatorname{Cov}(T,\\,f(A)\\mid A^*)\\bigr], \\label{eq:R}\\\\\n  D(C) &= \\mathbb{E}\\bigl[\\operatorname{Var}(T\\mid A^*)\\bigr] > 0. \\label{eq:D}\n\\end{align}\n\\end{lemma}\n\n\\begin{proof}\nExpand $\\tilde{Y}$ using $Y=\\tau T + f(A) + \\varepsilon_Y$:\n\\[\n  \\tilde{Y} = \\tau\\,\\tilde{T} + \\bigl(f(A) - \\mathbb{E}[f(A)\\mid A^*]\\bigr) + \\varepsilon_Y.\n\\]\nSince $\\tilde{T}$ is measurable w.r.t.\\ $(T,A^*)$ and $\\varepsilon_Y\\perp(T,A,A^*)$:\n\\[\n  \\mathbb{E}[\\tilde{T}\\,\\tilde{Y}]\n  = \\tau\\,\\mathbb{E}[\\tilde{T}^2]\n  + \\mathbb{E}\\bigl[\\tilde{T}\\,\\bigl(f(A)-\\mathbb{E}[f(A)\\mid A^*]\\bigr)\\bigr].\n\\]\nThe numerator residual is $R(C) = \\mathbb{E}[\\tilde{T}(f(A)-\\mathbb{E}[f(A)\\mid A^*])]$, and the denominator is $D(C) = \\mathbb{E}[\\tilde{T}^2]$.\n\nBy the law of total covariance:\n\\[\n  R(C) = \\sum_{j=0}^{K-1} q_j\\,\\operatorname{Cov}(T,\\,f(A)\\mid A^*{=}j)\n  = \\mathbb{E}[\\operatorname{Cov}(T,f(A)\\mid A^*)].\n\\]\nFor $D(C)>0$: decompose $T = g(A) + \\varepsilon_T$ where $g(A)=\\mathbb{E}[T\\mid A]$ (for confounding) or simply note that $T$ has exogenous variation independent of $A^*$ (for mediation).\nIn both cases, $\\tilde{T}=\\bigl(g(A)-\\mathbb{E}[g(A)\\mid A^*]\\bigr)+\\varepsilon_T'$, where $\\varepsilon_T'$ is the component of $T$ independent of $(A,A^*)$.\nHence $D(C)\\geq\\operatorname{Var}(\\varepsilon_T')>0$.\n\\end{proof}\n\n\\subsection{Confounding Topology ($A$ = Confounder)}\n\\label{app:confounding}\n\n\\paragraph{Data-generating process.}\n$A\\to T$, $A\\to Y$, $T\\to Y$.\nUsing dummy coding with category 0 as reference:\n\\begin{align*}\n  T &= \\sum_{j=1}^{K-1}\\alpha_j D_j + \\varepsilon_T,\\quad\n  \\varepsilon_T\\sim\\mathcal{N}(0,\\sigma_T^2),\\;\\varepsilon_T\\perp A,\\\\\n  Y &= \\tau\\, T + \\sum_{j=1}^{K-1}\\beta_j^{(A)} D_j + \\varepsilon_Y,\\quad\n  \\varepsilon_Y\\sim\\mathcal{N}(0,1),\\;\\varepsilon_Y\\perp(T,A).\n\\end{align*}\nDefine $g(k)=\\sum_{j}\\alpha_j\\mathbf{1}(k{=}j)$ and $f(k)=\\sum_{j}\\beta_j^{(A)}\\mathbf{1}(k{=}j)$, so $g(0)=f(0)=0$.\n\n\\paragraph{Closed-form plim.}\nUsing the FWL decomposition, the coefficient on $T$ is:\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau(C)\n  = \\frac{\\mu_{TY} - \\sum_{j=0}^{K-1}\\frac{\\mathrm{ct}_j\\,\\mathrm{cy}_j}{q_j}}\n  {s_T - \\sum_{j=0}^{K-1}\\frac{\\mathrm{ct}_j^2}{q_j}},\n  \\label{eq:plim_conf}\n\\end{equation}\nwhere $s_T=\\mathbb{E}[T^2]$, $\\mu_{TY}=\\mathbb{E}[TY]$, and $\\mathrm{ct}_j$, $\\mathrm{cy}_j$, $q_j$ are defined in~\\eqref{eq:q}--\\eqref{eq:cy}.\n\n\\begin{proof}[Derivation]\nBy FWL, $\\operatorname{plim}\\hat\\tau = \\mathbb{E}[\\tilde{T}Y]/\\mathbb{E}[\\tilde{T}^2]$ where $\\tilde{T}=T-\\mathbb{E}[T\\mid A^*]$.\nSince $\\mathbb{E}[T\\mid A^*{=}j]=\\mathrm{ct}_j/q_j$:\n\\begin{align*}\n  \\mathbb{E}[\\tilde{T}^2]\n  &= \\mathbb{E}[T^2] - \\sum_j q_j\\bigl(\\mathrm{ct}_j/q_j\\bigr)^2\n  = s_T - \\sum_j \\mathrm{ct}_j^2/q_j,\\\\\n  \\mathbb{E}[\\tilde{T}\\,Y]\n  &= \\mathbb{E}[TY] - \\sum_j \\bigl(\\mathrm{ct}_j/q_j\\bigr)\\,\\mathbb{E}[Y\\cdot D_j^*]\n  = \\mu_{TY} - \\sum_j \\mathrm{ct}_j\\,\\mathrm{cy}_j/q_j.\n\\end{align*}\n\\end{proof}\n\n\\paragraph{Verification at $C=I$.}\nWhen $C=I$: $q_j=p_j$, $\\mathrm{ct}_j=\\mathbb{E}[T D_j]=\\alpha_j p_j$, $\\mathrm{cy}_j=\\mathbb{E}[Y D_j]=p_j(\\tau\\alpha_j+\\beta_j^{(A)})$.\nDirect substitution yields numerator $= \\tau\\sigma_T^2$ and denominator $= \\sigma_T^2$, giving $\\operatorname{plim}\\hat\\tau = \\tau$.\n\n\\paragraph{Bias structure.}\nBy Lemma~\\ref{lem:bias_decomp}:\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau(C) = \\tau + B(C),\\quad\n  B(C) = \\frac{\\mathbb{E}[\\operatorname{Cov}(g(A),\\,f(A)\\mid A^*)]}{D(C)}.\n  \\label{eq:bias_conf}\n\\end{equation}\nBy the law of total covariance:\n\\begin{equation}\n  \\mathbb{E}[\\operatorname{Cov}(g,f\\mid A^*)]\n  = \\operatorname{Cov}(g(A),f(A))\n  - \\operatorname{Cov}\\bigl(\\mathbb{E}[g(A)\\mid A^*],\\;\\mathbb{E}[f(A)\\mid A^*]\\bigr).\n  \\label{eq:lotc}\n\\end{equation}\n\nAt $C=I$: $\\mathbb{E}[g\\mid A^*]=g(A)$, so the between-group covariance equals $\\operatorname{Cov}(g,f)$ and $B(I)=0$.\n\nAt $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$ (uniform, $A^*\\perp A$): $\\mathbb{E}[g\\mid A^*]$ is constant, so the between-group covariance is zero and\n\\begin{equation}\n  B_{\\mathrm{OV}} \\;\\equiv\\; B\\bigl(\\tfrac{1}{K}\\mathbf{1}\\mathbf{1}^\\top\\bigr)\n  = \\frac{\\operatorname{Cov}(g(A),\\,f(A))}{\\operatorname{Var}(T)},\n  \\label{eq:bov}\n\\end{equation}\nwhich equals the classical omitted-variable bias (no control for $A$).\n\n\\paragraph{Sign preservation condition.}\nSince $D(C)>0$, sign$(\\operatorname{plim}\\hat\\tau) = $ sign$(\\tau\\cdot D(C) + R(C))$.\nFor sign preservation, it suffices that $R(C)$ does not overwhelm $\\tau\\cdot D(C)$.\n\n\\begin{proposition}[Confounding sign preservation --- proportional case]\n\\label{prop:conf_prop}\nIf $f(A) = \\lambda\\,g(A)$ for some constant $\\lambda$ (i.e., the confounder effects on $T$ and $Y$ are proportional), then\n\\begin{equation}\n  B(C) = \\bigl(1-\\eta(C)\\bigr)\\,B_{\\mathrm{OV}},\n  \\label{eq:convex}\n\\end{equation}\nwhere\n\\[\n  \\eta(C) = \\frac{\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*])\\;\\sigma_T^2}\n  {\\operatorname{Var}(g(A))\\bigl(\\operatorname{Var}(g(A))-\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*])+\\sigma_T^2\\bigr)}\n  \\;\\in\\;[0,1].\n\\]\nConsequently, $B(C)$ lies between $0$ and $B_{\\mathrm{OV}}$, and $\\operatorname{sign}(\\operatorname{plim}\\hat\\tau)=\\operatorname{sign}(\\tau)$ whenever $\\operatorname{sign}(\\tau)=\\operatorname{sign}(\\tau+B_{\\mathrm{OV}})$.\n\\end{proposition}\n\n\\begin{proof}\nWhen $f=\\lambda g$: the between-group covariance in~\\eqref{eq:lotc} becomes $\\lambda\\,\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])$, and $\\operatorname{Cov}(g,f)=\\lambda\\,\\operatorname{Var}(g)$.\nSo $R(C)=\\lambda\\bigl(\\operatorname{Var}(g)-\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])\\bigr)=\\lambda\\,V_W$, where $V_W=\\operatorname{Var}(g)-V_B$ with $V_B=\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])$.\nSimilarly, $D(C)=V_W+\\sigma_T^2$.\nHence\n\\[\n  B(C) = \\frac{\\lambda\\,V_W}{V_W+\\sigma_T^2},\\qquad\n  B_{\\mathrm{OV}} = \\frac{\\lambda\\,V}{V+\\sigma_T^2},\n\\]\nwhere $V=\\operatorname{Var}(g)=V_B+V_W$.\nThe ratio\n\\[\n  \\frac{B(C)}{B_{\\mathrm{OV}}} = \\frac{V_W(V+\\sigma_T^2)}{V(V_W+\\sigma_T^2)} = 1 - \\eta(C)\n\\]\nis a decreasing function of $V_B\\in[0,V]$.\nAt $V_B=0$ (no classification, $C$ uniform): $\\eta=0$, $B=B_{\\mathrm{OV}}$.\nAt $V_B=V$ (perfect classification, $C=I$): $\\eta=1$, $B=0$.\nSince $0\\leq V_B\\leq V$, we have $\\eta\\in[0,1]$ and $B(C)\\in[0,B_{\\mathrm{OV}}]$ (with the sign of $B_{\\mathrm{OV}}$).\n\\end{proof}\n\n\\begin{proposition}[Confounding sign preservation --- general case]\n\\label{prop:conf_gen}\nFor general $g$ and $f$ (not necessarily proportional), define the worst-case bias bound\n\\begin{equation}\n  \\bar{B} \\;=\\; \\frac{\\sqrt{\\operatorname{Var}(g(A))\\,\\operatorname{Var}(f(A))}}{\\sigma_T^2}.\n  \\label{eq:bbar}\n\\end{equation}\nIf $|\\tau| > \\bar{B}$, then $\\operatorname{sign}(\\operatorname{plim}\\hat\\tau(C))=\\operatorname{sign}(\\tau)$ for \\emph{all} column-stochastic $C$.\n\\end{proposition}\n\n\\begin{proof}\nWe need $\\operatorname{sign}(\\tau\\cdot D(C)+R(C))=\\operatorname{sign}(\\tau)$, which holds if $|R(C)|<|\\tau|\\cdot D(C)$.\nSince $D(C)\\geq\\sigma_T^2$ (shown in Lemma~\\ref{lem:bias_decomp}), it suffices to show $|R(C)|<|\\tau|\\,\\sigma_T^2$.\n\n\\emph{Step 1: Bound $|R(C)|$.}\n$R(C)=\\mathbb{E}[\\operatorname{Cov}(g(A),f(A)\\mid A^*)]$.\nBy the Cauchy--Schwarz inequality applied to each within-group covariance:\n\\[\n  |\\operatorname{Cov}(g,f\\mid A^*{=}j)|\n  \\leq \\sqrt{\\operatorname{Var}(g\\mid A^*{=}j)\\,\\operatorname{Var}(f\\mid A^*{=}j)}.\n\\]\nTaking expectations and applying Cauchy--Schwarz again:\n\\begin{align*}\n  |R(C)|\n  &\\leq \\mathbb{E}\\bigl[\\sqrt{\\operatorname{Var}(g\\mid A^*)\\,\\operatorname{Var}(f\\mid A^*)}\\bigr]\\\\\n  &\\leq \\sqrt{\\mathbb{E}[\\operatorname{Var}(g\\mid A^*)]\\;\\mathbb{E}[\\operatorname{Var}(f\\mid A^*)]}\\\\\n  &\\leq \\sqrt{\\operatorname{Var}(g(A))\\;\\operatorname{Var}(f(A))},\n\\end{align*}\nwhere the last step uses $\\mathbb{E}[\\operatorname{Var}(X\\mid Y)]\\leq\\operatorname{Var}(X)$ (law of total variance).\n\n\\emph{Step 2: Conclude.}\nThe bias satisfies\n\\[\n  |B(C)| = \\frac{|R(C)|}{D(C)} \\leq \\frac{\\sqrt{\\operatorname{Var}(g)\\,\\operatorname{Var}(f)}}{\\sigma_T^2} = \\bar{B}.\n\\]\nWhen $|\\tau|>\\bar{B}$, the bias cannot cancel $\\tau$, so $\\operatorname{sign}(\\operatorname{plim}\\hat\\tau)=\\operatorname{sign}(\\tau)$ for all $C$.\n\\end{proof}\n\n\\paragraph{Relationship to the omitted-variable condition.}\nA weaker (necessary) condition for sign preservation is $\\operatorname{sign}(\\tau)=\\operatorname{sign}(\\tau_{\\mathrm{OV}})$ where $\\tau_{\\mathrm{OV}}=\\tau+\\operatorname{Cov}(g,f)/\\operatorname{Var}(T)$.\nIf this fails, then $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$ (uniform noise) already flips the sign.\nThe rigorous sufficient condition $|\\tau|>\\bar{B}$ implies the weaker condition, since $|B_{\\mathrm{OV}}|=|\\operatorname{Cov}(g,f)|/\\operatorname{Var}(T)\\leq\\bar{B}$ by Cauchy--Schwarz and $\\operatorname{Var}(T)\\geq\\sigma_T^2$.\n\n\\paragraph{Verification for paper parameters ($K{=}3$).}\nWith $\\tau{=}2.0$, $\\boldsymbol{\\alpha}{=}(1.5,{-}1.0)$, $\\boldsymbol{\\beta}^{(A)}{=}(1.0,{-}0.5)$, $\\sigma_T{=}1.0$, $\\mathbf{p}{=}(0.40,0.35,0.25)$:\n\\begin{align*}\n  \\operatorname{Var}(g) &= \\sum_k p_k\\alpha_k^2 - \\bigl(\\textstyle\\sum_k p_k\\alpha_k\\bigr)^2 = 0.962,\\\\\n  \\operatorname{Var}(f) &= \\sum_k p_k(\\beta_k^{(A)})^2 - \\bigl(\\textstyle\\sum_k p_k\\beta_k^{(A)}\\bigr)^2 = 0.362,\\\\\n  \\bar{B} &= \\sqrt{0.962\\times 0.362}\\;/\\;1.0^2 = 0.590.\n\\end{align*}\nSince $|\\tau|{=}2.0 > \\bar{B}{=}0.590$, sign preservation is guaranteed for \\emph{all} column-stochastic $C$ by Proposition~\\ref{prop:conf_gen}.\nAdditionally, $B_{\\mathrm{OV}}=\\operatorname{Cov}(g,f)/\\operatorname{Var}(T)=0.588/1.962={+}0.300$, giving $\\tau_{\\mathrm{OV}}{=}2.300>0$, confirming that both the necessary and sufficient conditions are satisfied.\n\n\\paragraph{Extension to $K > 3$.}\nFor $K{>}3$, treatment effect coefficients are drawn from a fixed pool with alternating signs and decreasing magnitudes: $\\boldsymbol{\\beta} = (0, 1.0, {-}0.5, 0.7, {-}0.3, 0.5, {-}0.2, 0.4, {-}0.15, 0.3, \\ldots)$, truncated to $K$ entries. The category distribution uses $p_k \\propto 1/(k{+}1)$, normalized to sum to 1. Other topology-specific parameters (confounding strengths, mediator effects, etc.) follow analogous alternating-sign pools. For $K{=}10$, $\\boldsymbol{\\beta} = (0, 1.0, {-}0.5, 0.7, {-}0.3, 0.5, {-}0.2, 0.4, {-}0.15, 0.3)$.\n\n\\subsection{Proof of Theorem~\\ref{thm:monotone} (Confounding Monotonicity)}\n\\label{app:monotonicity_proof}\n\nUnder the interpolation $C(\\delta)=(1{-}\\delta)I+\\delta C_0$, we prove $|B(C(\\delta))|$ is non-decreasing in $\\delta$ for proportional effects ($f=\\lambda g$) and provide numerical verification for the general case.\n\n\\paragraph{Proportional case ($f=\\lambda g$).}\nFrom Proposition~\\ref{prop:conf_prop}, $B(C)=\\lambda V_W/(V_W+\\sigma_T^2)$ where $V_W=\\operatorname{Var}(g)-V_B$ and $V_B(\\delta)=\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*_\\delta])$.\n\n\\emph{Step 1: $V_B(\\delta)$ is non-increasing.}\nThe conditional expectation $\\mathbb{E}[g(A)\\mid A^*_\\delta]$ is a linear function of the posterior $P(A\\mid A^*_\\delta)$, which in turn depends on $C(\\delta)$.\nAs $\\delta$ increases, $C(\\delta)$ becomes a noisier channel: the mutual information $I(A;A^*_\\delta)$ decreases.\nWhile the exact degradation factorization $C(\\delta_2)=M\\cdot C(\\delta_1)$ for a stochastic $M$ is non-trivial for the linear interpolation family, the monotonic decrease of $V_B(\\delta)$ can be verified directly: for $K{=}2$ symmetric $C_0$, $dV_B/d\\delta < 0$ follows by differentiation; for general $K$, we verify $V_B(\\delta_2)\\leq V_B(\\delta_1)$ numerically across all test configurations with zero violations.\n\n\\emph{Step 2: $|B(\\delta)|$ is non-decreasing.}\n$V_W(\\delta)=\\operatorname{Var}(g)-V_B(\\delta)$ is non-decreasing (Step~1).\nThe function $h(x)=|\\lambda|\\,x/(x+\\sigma_T^2)$ is strictly increasing for $x\\geq 0$ and $\\sigma_T^2>0$.\nHence $|B(\\delta)|=h(V_W(\\delta))$ is non-decreasing.\n\n\\paragraph{General case.}\n$|B(C(\\delta))|\\leq\\bar{B}(\\delta)$ where $\\bar{B}(\\delta)=\\sqrt{\\mathbb{E}[\\operatorname{Var}(g\\mid A^*_\\delta)]\\,\\mathbb{E}[\\operatorname{Var}(f\\mid A^*_\\delta)]}\\,/\\,D(\\delta)$ (Proposition~\\ref{prop:conf_gen}).\nBy the same data processing argument, each $\\mathbb{E}[\\operatorname{Var}(\\cdot\\mid A^*_\\delta)]$ is non-decreasing in $\\delta$, and $D(\\delta)=\\mathbb{E}[\\operatorname{Var}(T\\mid A^*_\\delta)]$ is non-decreasing.\nThe numerator grows at least as fast as the denominator (since $D(\\delta)\\leq\\operatorname{Var}(T)$), maintaining monotonicity of the bound.\nExtended verification (10{,}000 random $C_0$ matrices, $K \\in \\{3,5,7\\}$) reveals worst-case step deviations of 0.011 (confounding), confirming approximate tightness; a strict monotonicity proof for the general case remains open.\n\n\\subsection{Mediation Topology ($A$ = Mediator)}\n\\label{app:mediation}\n\n\\paragraph{Data-generating process.}\n$T\\to A\\to Y$, $T\\to Y$.\n\\begin{align*}\n  T &\\sim \\operatorname{Bernoulli}(0.5),\\\\\n  A\\mid T &\\sim \\operatorname{Categorical}\\bigl(\\operatorname{softmax}(\\boldsymbol{\\gamma}+\\boldsymbol{\\delta}\\,T)\\bigr),\\\\\n  Y &= \\tau_{\\mathrm{dir}}\\,T + f(A) + \\varepsilon_Y.\n\\end{align*}\n\n\\paragraph{Bias decomposition.}\nBy Lemma~\\ref{lem:bias_decomp}, the direct-effect estimator satisfies:\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau_{\\mathrm{dir}}(C) = \\tau_{\\mathrm{dir}} + \\frac{\\mathbb{E}[\\operatorname{Cov}(T,\\,f(A)\\mid A^*)]}{D(C)}.\n  \\label{eq:med_bias}\n\\end{equation}\n\nThe key structural difference from confounding: $T$ \\emph{causes} $A$, so the residual covariance $\\operatorname{Cov}(T,f(A)\\mid A^*)$ captures the indirect effect of $T$ on $Y$ through $A$ that is not absorbed by conditioning on $A^*$.\n\n\\paragraph{Endpoint analysis.}\n\nAt $C=I$ ($A^*{=}A$): conditioning on $A$ blocks the mediated path $T\\to A\\to Y$, so $\\operatorname{Cov}(T,f(A)\\mid A)=0$ and $\\operatorname{plim}\\hat\\tau=\\tau_{\\mathrm{dir}}$.\n\nAt $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$ ($A^*\\perp A$): no information about $A$ is used, and\n\\begin{align*}\n  \\mathbb{E}[\\operatorname{Cov}(T,f(A)\\mid A^*)] &= \\operatorname{Cov}(T,f(A)),\\\\\n  D(C) &= \\operatorname{Var}(T) = 0.25.\n\\end{align*}\nThe indirect effect is $\\tau_{\\mathrm{ind}}=\\mathbb{E}[f(A)\\mid T{=}1]-\\mathbb{E}[f(A)\\mid T{=}0]$, and\n\\[\n  \\operatorname{Cov}(T,f(A)) = 0.25\\,\\tau_{\\mathrm{ind}}.\n\\]\nHence at $C$ uniform: $\\operatorname{plim}\\hat\\tau = \\tau_{\\mathrm{dir}}+\\tau_{\\mathrm{ind}} = \\tau_{\\mathrm{total}}$.\n\n\\paragraph{Empirical Finding (Mediation sign preservation).}\n\\label{find:med_sign}\n$\\operatorname{sign}(\\operatorname{plim}\\hat\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{dir}})$ whenever $\\operatorname{sign}(\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{total}})$, where $\\tau_{\\mathrm{total}}=\\tau_{\\mathrm{dir}}+\\tau_{\\mathrm{ind}}$.\nThis result is verified numerically for $100{,}000$ independently sampled column-stochastic matrices $C$; a closed-form proof for general $K$ remains open.\n\n\\begin{proof}\nLet $R(C)=\\mathbb{E}[\\operatorname{Cov}(T,f(A)\\mid A^*)]$ and $D(C)=\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]>0$.\n\n\\emph{Endpoints.}\nAt $C{=}I$: $f(A)$ is constant given $A{=}A^*$, so $R(I)=0$ and $B(I)=0$.\nAt $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$: $R=\\operatorname{Cov}(T,f(A))=0.25\\,\\tau_{\\mathrm{ind}}$ and $D=\\operatorname{Var}(T)=0.25$, giving $B=\\tau_{\\mathrm{ind}}$.\n\n\\emph{Within-group structure for binary $T$.}\nSince $T\\in\\{0,1\\}$, the within-$A^*$-group bias admits a revealing decomposition.\nLet $p_j=P(T{=}1\\mid A^*{=}j)$.\nThen $\\operatorname{Var}(T\\mid A^*{=}j)=p_j(1{-}p_j)$ and\n\\[\n  \\operatorname{Cov}(T,f(A)\\mid A^*{=}j)\n  = p_j(1{-}p_j)\\bigl[\\mathbb{E}[f(A)\\mid T{=}1,A^*{=}j]-\\mathbb{E}[f(A)\\mid T{=}0,A^*{=}j]\\bigr].\n\\]\nDefine $\\delta_j=\\mathbb{E}[f(A)\\mid T{=}1,A^*{=}j]-\\mathbb{E}[f(A)\\mid T{=}0,A^*{=}j]$ as the \\emph{conditional indirect effect} in the $A^*{=}j$ subpopulation.\nThen\n\\[\n  B(C)=\\frac{R(C)}{D(C)}\n  =\\frac{\\sum_j q_j\\,p_j(1{-}p_j)\\,\\delta_j}{\\sum_j q_j\\,p_j(1{-}p_j)}\n  =\\sum_j w_j\\,\\delta_j,\n\\]\na weighted average of the conditional indirect effects, with weights $w_j=q_j p_j(1{-}p_j)/\\sum_\\ell q_\\ell p_\\ell(1{-}p_\\ell)\\geq 0$ summing to 1.\n\nAt $C{=}I$: each $A^*{=}j$ group has $A{=}j$ a.s., so $\\delta_j=f(j)-f(j)=0$ and $B=0$.\nAt $C$ uniform: $\\delta_j=\\tau_{\\mathrm{ind}}$ for all $j$ and $B=\\tau_{\\mathrm{ind}}$.\n\n\\emph{Sign preservation.}\nWhen $\\operatorname{Cov}(g(A),f(A))>0$ (the indirect effect reinforces the direct effect, i.e., $\\tau_{\\mathrm{dir}}$ and $\\tau_{\\mathrm{ind}}$ have the same sign), the bias $B(C)\\geq 0$ cannot oppose $\\tau_{\\mathrm{dir}}$, so sign is preserved trivially.\n\nWhen $\\tau_{\\mathrm{dir}}$ and $\\tau_{\\mathrm{ind}}$ have opposite signs but $|\\tau_{\\mathrm{ind}}|<|\\tau_{\\mathrm{dir}}|$ (i.e., $\\operatorname{sign}(\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{total}})$), sign reversal requires some $|\\delta_j|>|\\tau_{\\mathrm{dir}}|$ with the opposing sign.\nSince each $\\delta_j$ is a difference of weighted averages of $f$ values (with weights $P(A{=}k\\mid T{=}t,A^*{=}j)$), and $B(C)$ is a convex combination of $\\delta_j$, the bound $|B(C)|\\leq\\max_j|\\delta_j|$ holds.\nWe verify numerically that $\\max_j|\\delta_j|\\leq|\\tau_{\\mathrm{ind}}|$ for all 100{,}000 random $C$ matrices in our experiments, confirming sign preservation.\n\\end{proof}\n\n\\paragraph{Verification for paper parameters ($K{=}3$).}\nWith $\\tau_{\\mathrm{dir}}{=}0.5$, $\\boldsymbol{\\gamma}{=}(0,0,0)$, $\\boldsymbol{\\delta}{=}(0,0.8,{-}0.6)$, $\\boldsymbol{\\beta}{=}(0,1.0,{-}0.5)$:\n\n$\\tau_{\\mathrm{ind}}=\\mathbb{E}[f(A)\\mid T{=}1]-\\mathbb{E}[f(A)\\mid T{=}0]=0.351$ (computed from the softmax class probabilities).\n$\\tau_{\\mathrm{total}}=0.5+0.351=0.851>0$.\nSince $\\tau_{\\mathrm{dir}}{>}0$ and $\\tau_{\\mathrm{total}}{>}0$, sign preservation holds for all $C$.\n\n\\subsection{Collider Topology ($A$ = Collider)}\n\\label{app:collider}\n\n\\paragraph{Data-generating process.}\n$T\\to A\\leftarrow Y$, $T\\to Y$.\nThe treatment effect is unconfounded:\n\\begin{align*}\n  T &\\sim \\mathcal{N}(0,1),\\quad\n  Y = \\tau\\,T + \\varepsilon_Y,\\quad \\varepsilon_Y\\sim\\mathcal{N}(0,1),\\;\\varepsilon_Y\\perp T,\\\\\n  A\\mid T,Y &\\sim \\operatorname{Categorical}\\bigl(\\operatorname{softmax}(\\boldsymbol{\\delta}_T\\,T + \\boldsymbol{\\delta}_Y\\,Y)\\bigr).\n\\end{align*}\nThe collider $A$ is a common \\emph{effect} of $T$ and $Y$.\nThe no-control estimator (regressing $Y$ on $T$ alone) is consistent: $\\operatorname{plim}\\hat\\tau_{\\mathrm{nc}}=\\tau$.\nThe researcher erroneously controls for $A^*$, inducing Berkson's bias.\n\n\\paragraph{Bias decomposition.}\nUnlike confounding, $\\varepsilon_Y$ is not independent of $A$ (since $A$ depends on $Y=\\tau T+\\varepsilon_Y$), so Lemma~\\ref{lem:bias_decomp} does not apply directly.\nInstead, we derive the bias from the FWL identity~\\eqref{eq:fwl}.\nWriting $\\tilde{Y}=\\tau\\tilde{T}+(\\varepsilon_Y-\\mathbb{E}[\\varepsilon_Y\\mid A^*])$ and noting that $\\mathbb{E}[\\tilde{T}\\,\\varepsilon_Y]=\\mathbb{E}[\\operatorname{Cov}(T,\\varepsilon_Y\\mid A^*)]$ (since $T\\perp\\varepsilon_Y$ unconditionally):\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau(C) = \\tau + B(C),\\quad\n  B(C) = \\frac{\\mathbb{E}[\\operatorname{Cov}(T,\\,\\varepsilon_Y\\mid A^*)]}{\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]}.\n  \\label{eq:bias_col}\n\\end{equation}\nUnder non-differential misclassification ($A^*\\perp(T,\\varepsilon_Y)\\mid A$), define $g(k)=\\mathbb{E}[T\\mid A{=}k]$ and $h(k)=\\mathbb{E}[\\varepsilon_Y\\mid A{=}k]$.\nBy the tower property, $\\mathbb{E}[T\\mid A^*]=\\mathbb{E}[g(A)\\mid A^*]$ and $\\mathbb{E}[\\varepsilon_Y\\mid A^*]=\\mathbb{E}[h(A)\\mid A^*]$.\nSince $\\operatorname{Cov}(T,\\varepsilon_Y)=0$, the law of total covariance gives:\n\\[\n  B(C) = \\frac{-\\operatorname{Cov}\\bigl(\\mathbb{E}[g(A)\\mid A^*],\\;\\mathbb{E}[h(A)\\mid A^*]\\bigr)}{\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]}.\n\\]\n\n\\paragraph{Endpoint analysis.}\nAt $C=I$ ($A^*{=}A$):\n$B(I) = -\\operatorname{Cov}(g(A),h(A))\\,/\\,\\mathbb{E}[\\operatorname{Var}(T\\mid A)] = B_{\\mathrm{Berkson}}$,\nthe full Berkson's bias from conditioning on the collider.\n\nAt $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$ ($A^*\\perp A$):\n$\\mathbb{E}[g(A)\\mid A^*]$ and $\\mathbb{E}[h(A)\\mid A^*]$ are constant, so $B=0$ and $\\operatorname{plim}\\hat\\tau=\\tau$.\n\nThis is the structural reverse of confounding: misclassification attenuates the collider-induced bias toward zero, rather than growing bias from zero toward $B_{\\mathrm{OV}}$.\n\n\\begin{proposition}[Collider sign preservation --- proportional case]\n\\label{prop:col_prop}\nIf $h(A)=\\lambda\\,g(A)$ for some constant $\\lambda$, then $|B(C)|\\leq|B(I)|$ for all column-stochastic $C$, and $B(C)$ has the same sign as $B(I)$.\nConsequently, $\\operatorname{sign}(\\operatorname{plim}\\hat\\tau)=\\operatorname{sign}(\\tau)$ whenever $\\operatorname{sign}(\\tau)=\\operatorname{sign}(\\tau+B_{\\mathrm{Berkson}})$.\n\\end{proposition}\n\n\\begin{proof}\nWhen $h=\\lambda g$, the numerator becomes $-\\lambda\\,\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*])$ and the denominator is $\\operatorname{Var}(T)-\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*])$.\nLet $V^*=\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*])\\in[0,V_g]$ where $V_g=\\operatorname{Var}(g(A))$.\nThen\n\\[\n  |B(C)| = |\\lambda|\\,\\frac{V^*}{\\operatorname{Var}(T)-V^*}.\n\\]\nThe function $x\\mapsto x/(a-x)$ is increasing on $[0,a)$.\nWith $a=\\operatorname{Var}(T)>V_g\\geq V^*$:\n$|B(C)|\\leq|\\lambda|\\,V_g/(\\operatorname{Var}(T)-V_g)=|B(I)|$.\nAt $V^*{=}0$ (uniform $C$): $B{=}0$.  At $V^*{=}V_g$ ($C{=}I$): $B{=}B(I)$.\n\\end{proof}\n\n\\begin{proposition}[Collider sign preservation --- general case]\n\\label{prop:col_gen}\nDefine\n\\begin{equation}\n  \\bar{B}_{\\mathrm{col}} = \\frac{\\sqrt{\\operatorname{Var}(g(A))\\,\\operatorname{Var}(h(A))}}{\\mathbb{E}[\\operatorname{Var}(T\\mid A)]}.\n  \\label{eq:bbar_col}\n\\end{equation}\nIf $|\\tau|>\\bar{B}_{\\mathrm{col}}$, then $\\operatorname{sign}(\\operatorname{plim}\\hat\\tau(C))=\\operatorname{sign}(\\tau)$ for all column-stochastic $C$.\n\\end{proposition}\n\n\\begin{proof}\n\\emph{Step~1: Bound the numerator.}\nBy Cauchy--Schwarz:\n$|\\operatorname{Cov}(\\mathbb{E}[g\\mid A^*],\\mathbb{E}[h\\mid A^*])|\\leq\\sqrt{\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])\\,\\operatorname{Var}(\\mathbb{E}[h\\mid A^*])}$.\nSince conditional expectation reduces variance: $\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])\\leq\\operatorname{Var}(g(A))$ and likewise for $h$.\n\n\\emph{Step~2: Bound the denominator.}\n$\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]=\\operatorname{Var}(T)-\\operatorname{Var}(\\mathbb{E}[T\\mid A^*])\\geq\\operatorname{Var}(T)-\\operatorname{Var}(g(A))=\\mathbb{E}[\\operatorname{Var}(T\\mid A)]$.\n\n\\emph{Step~3: Conclude.}\n$|B(C)|\\leq\\sqrt{\\operatorname{Var}(g)\\,\\operatorname{Var}(h)}\\,/\\,\\mathbb{E}[\\operatorname{Var}(T\\mid A)]=\\bar{B}_{\\mathrm{col}}$.\nWhen $|\\tau|>\\bar{B}_{\\mathrm{col}}$, the bias cannot overwhelm $\\tau$.\n\\end{proof}\n\n\\paragraph{Verification for paper parameters ($K{=}3$).}\nWith $\\tau{=}1.0$, $\\boldsymbol{\\delta}_T{=}(0,\\,0.5,\\,{-}0.3)$, $\\boldsymbol{\\delta}_Y{=}(0,\\,0.8,\\,0.6)$, from $5{\\times}10^6$-sample Monte Carlo:\n\\begin{align*}\n  \\operatorname{Var}(g(A)) &= 0.187,\\quad\n  \\operatorname{Var}(h(A)) = 0.076,\\quad\n  \\mathbb{E}[\\operatorname{Var}(T\\mid A)] = 0.813,\\\\\n  \\bar{B}_{\\mathrm{col}} &= \\sqrt{0.187\\times 0.076}\\;/\\;0.813 = 0.147.\n\\end{align*}\nSince $|\\tau|{=}1.0\\gg\\bar{B}_{\\mathrm{col}}{=}0.147$, Proposition~\\ref{prop:col_gen} guarantees sign preservation.\nAdditionally, $B_{\\mathrm{Berkson}}{=}{-}0.114$, giving $\\tau+B_{\\mathrm{Berkson}}{=}0.886{>}0$.\nVerified across $100{,}000$ random column-stochastic $C$: $\\tau_{\\mathrm{sign\\,flip}}{=}0\\%$, and $|B(C)|\\leq|B_{\\mathrm{Berkson}}|$ in all cases.\n\n\\subsection{Front-door Topology ($A$ = Mediator under Confounding)}\n\\label{app:frontdoor}\n\n\\paragraph{Data-generating process.}\n$T\\to A\\to Y$, $U\\to T$, $U\\to Y$.\nAn unobserved confounder $U$ affects both treatment and outcome:\n\\begin{align*}\n  U &\\sim \\mathcal{N}(0,1),\\quad\n  T = \\alpha_U\\,U + \\eta,\\quad \\eta\\sim\\mathcal{N}(0,1),\\;\\eta\\perp U,\\\\\n  A\\mid T &\\sim \\operatorname{Categorical}\\bigl(\\operatorname{softmax}(\\boldsymbol{\\gamma}+\\boldsymbol{\\delta}\\,T)\\bigr),\\\\\n  Y &= f(A) + \\lambda\\,U + \\varepsilon_Y,\\quad \\varepsilon_Y\\perp(T,A,U).\n\\end{align*}\nThere is no direct $T{\\to}Y$ edge; the causal effect of $T$ on $Y$ operates entirely through $A$.\nThe researcher controls for $A^*$ in $Y\\sim 1+T+D_1^*+\\cdots+D_{K-1}^*$.\n\n\\paragraph{Bias decomposition.}\nSince the direct effect is zero, the FWL coefficient on $T$ captures only bias:\n\\[\n  \\operatorname{plim}\\hat\\tau(C) = \\frac{\\mathbb{E}[\\operatorname{Cov}(T,\\,Y\\mid A^*)]}{\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]}.\n\\]\nSubstituting $Y=f(A)+\\lambda U+\\varepsilon_Y$ and using $\\varepsilon_Y\\perp(T,A,A^*)$:\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau(C)\n  = \\underbrace{\\frac{\\lambda\\,\\alpha_U}{\\operatorname{Var}(T)}}_{\\text{confounding (constant)}}\n  \\;+\\; \\underbrace{\\frac{\\mathbb{E}[\\operatorname{Cov}(T,\\,f(A)\\mid A^*)]}{D(C)}}_{\\displaystyle B_{\\mathrm{med}}(C)},\n  \\label{eq:fd_decomp}\n\\end{equation}\nwhere $D(C)=\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]$.\n\n\\begin{proof}[Derivation of~\\eqref{eq:fd_decomp}]\nExpand the numerator as\n$\\mathbb{E}[\\operatorname{Cov}(T,f(A)\\mid A^*)] + \\lambda\\,\\mathbb{E}[\\operatorname{Cov}(T,U\\mid A^*)]$.\nFor the confounding term: since $T=\\alpha_U U+\\eta$ with $(U,\\eta)$ jointly Gaussian, the regression residual $\\xi=U-\\frac{\\alpha_U}{\\operatorname{Var}(T)}T$ satisfies $\\xi\\perp T$.\nBecause $A$ is a function of $T$ (plus independent softmax noise) and $A^*$ is a function of $A$ (plus independent misclassification noise), $\\xi\\perp(T,A,A^*)$.\nTherefore\n\\[\n  \\operatorname{Cov}(T,U\\mid A^*{=}j)\n  = \\frac{\\alpha_U}{\\operatorname{Var}(T)}\\,\\operatorname{Var}(T\\mid A^*{=}j)\n  \\quad\\forall\\;j,\n\\]\nand $\\lambda\\,\\mathbb{E}[\\operatorname{Cov}(T,U\\mid A^*)]=\\frac{\\lambda\\alpha_U}{\\operatorname{Var}(T)}\\,D(C)$, yielding the constant first term after division by $D(C)$.\n\\end{proof}\n\nThis decomposition reveals that \\emph{misclassification does not affect the confounding component}.\nThe confusion matrix $C$ modulates only the mediation-type leakage $B_{\\mathrm{med}}(C)$, which has the same structure as in~§\\ref{app:mediation}.\n\n\\paragraph{Endpoint analysis.}\nAt $C=I$: $B_{\\mathrm{med}}(I)=0$ (controlling $A$ blocks the $T\\to A\\to Y$ path), and $\\operatorname{plim}\\hat\\tau(I)=\\lambda\\alpha_U/\\operatorname{Var}(T)$ (pure confounding residual).\n\nAt $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$: $B_{\\mathrm{med}}=\\operatorname{Cov}(T,f(A))/\\operatorname{Var}(T)$, and $\\operatorname{plim}\\hat\\tau_{\\mathrm{nc}}=[\\operatorname{Cov}(T,f(A))+\\lambda\\alpha_U]/\\operatorname{Var}(T)$, the naive regression coefficient with no controls.\n\n\\paragraph{Empirical Finding (Front-door sign preservation).}\n\\label{find:fd_sign}\nSince $B_{\\mathrm{med}}(C)$ has the same structure as the mediation bias (§\\ref{app:mediation})---interpolating between $0$ at $C{=}I$ and $\\operatorname{Cov}(T,f(A))/\\operatorname{Var}(T)$ at $C$ uniform---sign preservation holds whenever the two endpoints have the same sign:\n\\[\n  \\operatorname{sign}\\!\\bigl(\\lambda\\alpha_U\\bigr)\n  = \\operatorname{sign}\\!\\bigl(\\lambda\\alpha_U + \\operatorname{Cov}(T,f(A))\\bigr).\n\\]\nThis result is verified numerically for $100{,}000$ independently sampled column-stochastic matrices $C$.\n\n\\paragraph{Verification for paper parameters ($K{=}3$).}\nWith $\\alpha_U{=}1.0$, $\\lambda{=}1.0$, $\\boldsymbol{\\beta}{=}(0,1.0,{-}0.5)$, $\\boldsymbol{\\gamma}{=}(0,0.5,{-}0.3)$, $\\boldsymbol{\\delta}{=}(0,1.0,{-}0.8)$:\n\\begin{align*}\n  \\lambda\\alpha_U/\\operatorname{Var}(T) &= 1.0\\times 1.0\\,/\\,2.0 = 0.500,\\\\\n  \\operatorname{Cov}(T,f(A))/\\operatorname{Var}(T) &= 0.594\\,/\\,2.0 = 0.297.\n\\end{align*}\nBoth components are positive, so $\\operatorname{plim}\\hat\\tau(C)\\in[0.500,\\,0.797]>0$ for all $C$.\n\n\\subsection{Exposure Topology: Sign Reversal Counterexample}\n\\label{app:exposure}\n\n\\begin{proposition}[Exposure sign reversal]\n\\label{prop:exp_counter}\nFor $K{=}3$ with $A$ as the treatment variable, there exist a marginal distribution $\\mathbf{p}$, treatment effects $\\boldsymbol{\\beta}$, and a column-stochastic $C$ with $C_{kk}>0.5$ for all $k$, such that $\\operatorname{sign}(\\operatorname{plim}\\hat\\beta_1)\\neq\\operatorname{sign}(\\beta_1)$.\n\\end{proposition}\n\n\\begin{proof}[Construction]\nConsider the exposure DGP $Y = \\beta_1 D_1 + \\beta_2 D_2 + \\varepsilon_Y$ with:\n\\begin{itemize}\n  \\item Uniform prior: $\\mathbf{p}=(1/3,\\,1/3,\\,1/3)$.\n  \\item True effects: $\\beta_1=1$,\\; $\\beta_2=-10$.\n\\end{itemize}\nChoose the confusion matrix\n\\[\n  C = \\begin{pmatrix}\n    0.60 & 0.10 & 0.10\\\\\n    0.10 & 0.60 & 0.39\\\\\n    0.30 & 0.30 & 0.51\n  \\end{pmatrix},\\qquad\n  C_{kk}\\in\\{0.60,\\,0.60,\\,0.51\\},\\;\\text{all}>0.5.\n\\]\nColumn sums are $1$ (verifiable by inspection).\n\nThe OLS estimator regresses $Y$ on $(1,D_1^*,D_2^*)$.\nThe plim of $\\hat\\beta_j$ equals $\\mathbb{E}[Y\\mid A^*{=}j]-\\mathbb{E}[Y\\mid A^*{=}0]$, where\n\\[\n  \\mathbb{E}[Y\\mid A^*{=}j] = \\sum_{k=0}^{2} P(A{=}k\\mid A^*{=}j)\\,\\beta_k\n  = \\sum_{k=1}^{2}\\frac{C_{jk}\\,p_k}{q_j}\\,\\beta_k.\n\\]\n\n\\emph{Marginal distribution of $A^*$:}\n\\begin{align*}\n  q_0 &= \\tfrac{1}{3}(0.60+0.10+0.10)=0.267,\\\\\n  q_1 &= \\tfrac{1}{3}(0.10+0.60+0.39)=0.363,\\\\\n  q_2 &= \\tfrac{1}{3}(0.30+0.30+0.51)=0.370.\n\\end{align*}\n\n\\emph{Conditional means:}\n\\begin{align*}\n  \\mathbb{E}[Y\\mid A^*{=}0]\n  &= \\frac{0.10\\times\\tfrac{1}{3}\\times 1 + 0.10\\times\\tfrac{1}{3}\\times({-}10)}{0.267}\n  = \\frac{0.0333-0.3333}{0.267} = -1.125,\\\\[4pt]\n  \\mathbb{E}[Y\\mid A^*{=}1]\n  &= \\frac{0.60\\times\\tfrac{1}{3}\\times 1 + 0.39\\times\\tfrac{1}{3}\\times({-}10)}{0.363}\n  = \\frac{0.200-1.300}{0.363} = -3.028,\\\\[4pt]\n  \\mathbb{E}[Y\\mid A^*{=}2]\n  &= \\frac{0.30\\times\\tfrac{1}{3}\\times 1 + 0.51\\times\\tfrac{1}{3}\\times({-}10)}{0.370}\n  = \\frac{0.100-1.700}{0.370} = -4.324.\n\\end{align*}\n\n\\emph{Estimated coefficient:}\n\\[\n  \\operatorname{plim}\\hat\\beta_1 = \\mathbb{E}[Y\\mid A^*{=}1]-\\mathbb{E}[Y\\mid A^*{=}0]\n  = -3.028-(-1.125) = \\mathbf{-1.903}.\n\\]\nThe true $\\beta_1=+1>0$ but $\\operatorname{plim}\\hat\\beta_1=-1.903<0$: \\textbf{sign reversal}.\n\n\\emph{Mechanism.}\nThe large off-diagonal entry $C_{12}=0.39$ (probability of classifying true category~2 as $A^*{=}1$) routes substantial probability mass from category~2 ($\\beta_2=-10$) into the $A^*{=}1$ bin.\nDespite $C_{11}=0.60>0.5$, the contamination from the strongly negative $\\beta_2$ overwhelms the positive $\\beta_1$, reversing the sign of the estimated effect for category~1.\nThis failure mode is structurally impossible at $K{=}2$: a $2{\\times}2$ column-stochastic matrix with $C_{kk}>0.5$ has the form $C=\\bigl(\\begin{smallmatrix}a&1{-}b\\\\1{-}a&b\\end{smallmatrix}\\bigr)$ with $a,b>0.5$, and the single coefficient $\\hat\\beta_1$ is a positive-weighted average of $\\beta_1$, preserving sign.\nFor $K{\\geq}3$, the additional degrees of freedom in $C$ permit cross-contamination between categories with opposite-sign effects.\n\\end{proof}\n\n\\subsection{Summary of Conditions}\n\\label{app:conditions}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Topology} & \\textbf{Sufficient condition} & \\textbf{Status} & \\textbf{Paper DGP} \\\\\n\\midrule\nConfounding & $\\operatorname{sign}(\\tau)=\\operatorname{sign}(\\tau{+}B_{\\mathrm{OV}})$ & Proved & $\\checkmark$ ($2.0$ vs $2.3$)\\\\\nCollider & $|\\tau|>\\bar{B}_{\\mathrm{col}}$ (Prop.~\\ref{prop:col_gen}) & Proved & $\\checkmark$ ($1.0$ vs $0.15$)\\\\\n\\midrule\nMediation & $\\operatorname{sign}(\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{total}})$ & Empirical & $\\checkmark$ ($0.5$ vs $0.85$)\\\\\nM-bias & Bias is attenuating (toward $\\tau$) & Empirical & $\\checkmark$ \\\\\nFront-door & $\\operatorname{sign}(\\lambda\\alpha_U)=\\operatorname{sign}(\\lambda\\alpha_U{+}\\operatorname{Cov}(T,f))$ & Empirical & $\\checkmark$ ($0.50$ vs $0.80$)\\\\\n\\midrule\nExposure & Not guaranteed for $K\\geq 3$ & Counterex. & See §\\ref{app:exposure} \\\\\nIV & Not guaranteed (denominator instability) & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Sufficient conditions for sign preservation under non-differential misclassification.\n``Proved'' = algebraic proof via Cauchy--Schwarz (confounding) or Berkson attenuation (collider).\n``Empirical'' = verified across 100{,}000 random column-stochastic matrices with zero violations; analytic proof for general $K$ remains open.\nAll conditions are on DGP parameters (not on $C$): once satisfied, sign preservation holds for all column-stochastic $C$ with $C_{kk}>0$.}\n\\label{tab:sign_conditions}\n\\end{table}\n\n\\paragraph{Structural argument for M-bias topology.}\n\\emph{M-bias:} The M-structure creates a backdoor path through two latent common causes.\nMisclassification of $A$ weakens the statistical association along this backdoor path, reducing the spurious correlation rather than amplifying it.\nThe bias therefore interpolates between the full M-bias (perfect classification, $\\delta{=}0$) and zero (no classification information, $\\delta{\\to}\\delta_{\\max}$), monotonically non-increasing in $\\delta$.\n\n\\paragraph{Remark.}\nThe sign preservation conditions for confounding, mediation, collider, and front-door are conditions on the DGP parameters (the relative strength of the causal effect versus the confounding, indirect, or collider-induced bias), not on the confusion matrix $C$.\nOnce the condition is satisfied, sign preservation holds for \\emph{all} column-stochastic $C$ with $C_{kk}>0$---no diagonal-dominance restriction is needed.\nConversely, if the condition fails (i.e., the omitted-variable or total-effect estimate has the opposite sign from $\\tau$), then there exist confusion matrices that produce sign reversal.\nFor the DGP parameters used throughout our experiments, the conditions are comfortably satisfied.\nThe sign-alignment condition is violated when the confounder has opposing effects on treatment and outcome (e.g., $\\gamma_A > 0$ on $T$ but $\\gamma_A < 0$ on $Y$), producing $\\operatorname{sign}(\\tau) \\neq \\operatorname{sign}(\\tau_{\\mathrm{OV}})$. In applied settings, such opposing effects are uncommon when the analyst adjusts for $A$ precisely because they believe it confounds the $T$--$Y$ relationship in a consistent direction. When the condition fails, sign reversal becomes possible under sufficient misclassification, though this represents a pathological DGP where adjustment itself may be questionable.\n\n\\section{Supplementary Tables, Figures, and Algorithm}\n\\label{app:supplementary}\n\n\\subsection{Binarization Collapse}\n\\label{app:binarization}\n\nCollapsing $K$-class annotations to binary before analysis discards multi-class error structure. We quantify ``binarization collapse'' as $\\Delta = |\\text{bias}_{K} - \\text{bias}_{K \\to 2}|$.\n\nFor $K{=}3$, binarization introduces additional bias varying 154$\\times$ across topologies: from $\\bar{\\Delta}{=}0.006$ (M-bias) to $\\bar{\\Delta}{=}0.926$ (IV). Exposure and IV also introduce sign flips during binarization (14\\% and 17.5\\%), a phenomenon absent in the other topologies (Figure~\\ref{fig:binarization}).\n\n\\begin{figure*}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{fig3_asv_ranking.pdf}\n\\caption{ASV sensitivity ranking across topologies. Three ASV types (magnitude, significance, sign-flip) reveal a topology-dependent vulnerability spectrum from IV (maximally fragile, 52.6\\% sign reversal; sign-flip ASV $= 1.1$--$6.7$) to M-bias (immune, ASV $= \\infty$).}\n\\label{fig:asv_ranking}\n\\end{figure*}\n\n\\begin{table}[h]\n\\centering\n\\caption{ASV type applicability and sensitivity across DAG topologies. Magnitude ASV at $\\tau{=}0.5$, 10\\% threshold. Power at $\\tau{=}0.05$ significance filter. ---: not applicable.}\n\\label{tab:asv_grid}\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Topology} & \\textbf{Mag. ASV} & \\textbf{Signif.} & \\textbf{Sign-flip} & \\textbf{Rank} \\\\\n\\midrule\nIV & 0.101--0.607 & 0\\% & 1.1--6.7 & 1 (fragile) \\\\\nFront-door & 0.064--0.387 & 100\\% & --- & 2 \\\\\nConfounding & 0.081--0.487 & 100\\% & --- & 3 \\\\\nMediation & 0.076--0.454 & 0\\% & --- & 4 \\\\\nCollider & 0.338--2.028 & 0\\% & --- & 5 \\\\\nM-bias & $\\infty$ & 96--100\\% & --- & 6 (immune) \\\\\nExposure & --- & --- & 83.4\\%$^*$ & --- \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\scriptsize $^*$Fraction of $C_0$ with $\\tau_{\\text{sign\\_flip}} < 1$. Exposure uses sign-flip ASV exclusively.}\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig7_dirichlet_overlay.pdf}\n\\caption{Empirical LLM confusion matrices overlaid on theoretical violation-rate curves (exposure, left; IV, right). Theoretical curves are derived from $K{=}3$ Dirichlet random matrices; empirical points are positioned at their minimum diagonal entry. Markers denote datasets (circles: HumAID $K{=}10$; squares: VAST $K{=}3$; triangles: CivilComments $K{=}2$).}\n\\label{fig:dirichlet_overlay}\n\\end{figure}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig4_binarization.pdf}\n\\caption{Binarization collapse $\\Delta$ across topologies. Collapsing $K{=}3$ annotations to binary introduces additional bias varying 154$\\times$ from M-bias (0.006) to IV (0.926).}\n\\label{fig:binarization}\n\\end{figure}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig6_asv_heatmap.pdf}\n\\caption{ASV magnitude ranges across topologies for HumAID ($K{=}10$). Left: magnitude ASV ($\\delta^*$) range across 8 LLM configurations; lower values indicate greater fragility. ``Safe'' topologies never exceed the 10\\% bias threshold. Right: percentage of configurations flagged as ASV-unsafe.}\n\\label{fig:asv_heatmap}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{RMSE reduction (\\%) by correction method and DAG topology (mean across 6 error structures, $N_{\\text{sim}}{=}1{,}000$). Positive = reduced RMSE; negative = increased RMSE. Naive/MLA show 0.0\\% for FWL-invariant topologies because $C^{-1}$ cannot change the $T$ coefficient. \\textbf{Bold}: best method per topology; \\underline{underline}: best gold-free method.}\n\\label{tab:correction}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Topology} & \\textbf{Naive} & \\textbf{MLA} & \\textbf{DSL} & \\textbf{SIMEX} & \\textbf{PPI++} \\\\\n\\midrule\nConfounding & 0.0 & 0.0 & \\underline{48.0} & 35.1 & \\textbf{83.2} \\\\\nMediation & 0.0 & 0.0 & \\underline{52.9} & 39.1 & \\textbf{54.1} \\\\\nCollider & 0.0 & 0.0 & $-$92.6 & \\underline{31.8} & \\textbf{50.5} \\\\\nM-bias & 0.0 & 0.0 & $-$267 & \\textbf{\\underline{0.1}} & $-$88.0 \\\\\n\\midrule\nFront-door & $-$52.7 & $-$111.5 & \\underline{$-$29.0} & $-$62.4 & \\textbf{74.1} \\\\\nExposure & $-$44.8 & $-$89.0 & $-$59.5 & \\underline{$-$9.8} & \\textbf{75.5} \\\\\nIV & $-$40.4 & $-$58.7 & $-$206.1 & \\underline{59.4} & \\textbf{79.4} \\\\\n\\midrule\nGrand mean & $-$19.7 & $-$37.0 & $-$79.0 & 13.3 & \\textbf{47.0} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Error structures used in correction experiments.}\nThe six confusion matrix structures used for Table~\\ref{tab:correction} are:\n(1)~\\emph{Diagonal-dominant}: $C_{kk}{=}0.7$, off-diagonal uniform;\n(2)~\\emph{Moderate noise}: $C_{kk}{=}0.5$, off-diagonal uniform;\n(3)~\\emph{Near-permutation}: $C_{kk}{=}0.4$, largest off-diagonal 0.5;\n(4)~\\emph{Asymmetric}: $C_{kk}$ varies (0.8, 0.5, 0.3);\n(5)~\\emph{Block confusion}: two classes confused ($C_{12}{=}C_{21}{=}0.4$), third clean;\n(6)~\\emph{Heavy noise}: $C_{kk}{=}0.4$, off-diagonal uniform.\nAll are column-stochastic with $K{=}3$. Results are averaged across all six structures.\n\n\\begin{algorithm}[h]\n\\caption{Correction method selection for LLM-annotated causal inference.}\n\\label{alg:correction}\n\\small\n\\begin{algorithmic}[1]\n\\REQUIRE DAG topology $\\mathcal{T}$, gold-label availability $G \\in \\{\\textsc{yes}, \\textsc{no}\\}$\n\\ENSURE Recommended method $M$, risk level $R$\n\\STATE\n\\STATE \\textbf{Step 1: Assess risk level}\n\\IF{$\\mathcal{T} \\in \\{\\text{M-bias}\\}$}\n    \\STATE $R \\gets \\textsc{Low}$ \\COMMENT{$|\\text{bias}| < 0.04$ for all $C$}\n\\ELSIF{$\\mathcal{T} \\in \\{\\text{Conf., Med., Coll., Front-door}\\}$}\n    \\STATE $R \\gets \\textsc{Medium}$ \\COMMENT{bounded bias, no sign reversal}\n\\ELSE\n    \\STATE $R \\gets \\textsc{High}$ \\COMMENT{Exposure, IV: sign reversal 83.4\\% / 52.6\\%}\n\\ENDIF\n\\STATE\n\\STATE \\textbf{Step 2: Select correction method}\n\\IF{$G = \\textsc{yes}$}\n    \\IF{$\\mathcal{T} = \\text{M-bias}$}\n        \\STATE $M \\gets \\textsc{None}$ \\COMMENT{PPI++ RMSE red.\\ $-$88.0\\%; no correction preferred}\n    \\ELSE\n        \\STATE $M \\gets \\text{PPI++}$ \\COMMENT{47.0\\% RMSE red., 96.8\\% coverage}\n    \\ENDIF\n\\ELSE\n    \\STATE \\COMMENT{no gold labels}\n    \\IF{$\\mathcal{T} \\in \\{\\text{Confounding, Mediation}\\}$}\n        \\STATE $M \\gets \\text{DSL}$ \\COMMENT{48.0\\% / 52.9\\% RMSE reduction}\n    \\ELSIF{$\\mathcal{T} = \\text{IV}$}\n        \\STATE $M \\gets \\text{MC-SIMEX}$ \\COMMENT{59.4\\% RMSE reduction}\n    \\ELSIF{$\\mathcal{T} \\in \\{\\text{Collider, M-bias}\\}$}\n        \\STATE $M \\gets \\text{MC-SIMEX}$ \\COMMENT{31.8\\% / 0.1\\% RMSE reduction}\n    \\ELSE\n        \\STATE $M \\gets \\emptyset$; flag: acquire gold labels \\COMMENT{no reliable gold-free method}\n    \\ENDIF\n\\ENDIF\n\\STATE\n\\STATE \\textbf{Step 3: FWL invariance warning}\n\\IF{$\\mathcal{T} \\in \\{\\text{Conf., Med., Coll., M-bias}\\}$}\n    \\STATE Skip Naive plug-in and MLA \\COMMENT{0\\% bias red.\\ on $T$ coeff.}\n\\ENDIF\n\\RETURN $(M, R)$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\subsection{Applied Illustration: ClinicalBERT Case Study}\n\\label{app:case_study}\n\nTo demonstrate the framework's end-to-end utility, we apply it retrospectively to \\citet{lee_wood_doughty2024}, who use ClinicalBERT to classify patient smoking status ($K{=}4$: never, past, current, unknown) from clinical notes and control for this predicted confounder when estimating the causal effect of echocardiography on mortality in 4{,}735 MIMIC-III sepsis patients.\nOur taxonomy identifies this as a \\emph{confounding topology}: the annotated variable enters as a confounder between treatment and outcome.\nThree conclusions follow directly.\nFirst, the zero sign-flip guarantee for confounding (Table~\\ref{tab:taxonomy}) ensures that the estimated protective effect (OR~$= 0.89$) cannot reverse direction due to annotation error---a reassurance unavailable without topology-specific analysis.\nSecond, the FWL invariance result implies that any correction reducing to $C^{-1}$ applied to the dummy-coded confounder achieves exactly 0\\% bias reduction for the treatment coefficient; naive plug-in is provably futile here.\nThird, our correction guidance ranks PPI++ (83.2\\% RMSE reduction for confounding) above MC-SIMEX (35.1\\%) when gold labels are available---a concrete recommendation the original study lacked.\nThis example illustrates the intended workflow: DAG identification $\\to$ topology-specific guarantees $\\to$ correction method selection.\n\n\\subsection{IV Wald Estimator: Diagonal-Dominance Subspaces}\n\\label{sec:iv_dirichlet_subspace}\n\nSection~\\ref{sec:taxonomy_results} reports a 52.6\\% Wald sign-flip rate\nover the full Dirichlet$(1,1,1)$ prior. Because realistic LLM confusion\nmatrices are diagonal-dominant, we replicate the exposure-DAG stratification\nfor the IV topology, restricting the sample\nspace to $\\{C : \\min_k C_{kk} \\geq d\\}$ for $d \\in \\{0, 0.5, 0.7, 0.9\\}$\n(100{,}000 random matrices per threshold).\n\n\\begin{table}[h]\n\\centering\n\\caption{IV Wald estimator bias by minimum-diagonal subspace ($K{=}3$, $\\tau_{\\text{true}}{=}1.41$).\nRates over 100{,}000 Dirichlet-truncated random $C$ per threshold.}\n\\label{tab:iv_dirichlet_subspace}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Subspace} & \\textbf{Violation} & \\textbf{Sign Flip} & \\textbf{Amplif.} & \\textbf{Worst} \\\\\n\\midrule\nFull           & 100.0\\% & 51.7\\% & 48.3\\% & $10^{5}\\!\\times$ \\\\\n$d \\geq 0.5$   & 100.0\\% & 0.0\\%  & 100.0\\% & $28.6\\times$ \\\\\n$d \\geq 0.7$   & 100.0\\% & 0.0\\%  & 100.0\\% & $2.4\\times$ \\\\\n$d \\geq 0.9$   & 100.0\\% & 0.0\\%  & 100.0\\% & $1.2\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe contrast with exposure is instructive: at $d{\\geq}0.7$, exposure violation drops to 13.7\\% (sign reversal 2.1\\%, amplification 11.7\\%), while IV maintains 100\\% violation with pure amplification. IV sign reversal is entirely driven by pathological (near-random) confusion matrices where the Wald denominator crosses zero; diagonal dominance prevents this crossing but cannot prevent amplification. Even at $d{\\geq}0.9$, the Wald estimator inflates $|\\tau|$ by up to $1.24\\times$ with probability~1.\n\n\\subsection{Non-Differential Assumption Stress Test}\n\\label{sec:nondiff_stress}\n\nOur main analysis assumes non-differential misclassification: the confusion matrix $C$ does not depend on the outcome $Y$. To assess sensitivity to violations of this assumption, we conduct a stress test on the exposure topology ($K{=}3$, $\\min_k C_{kk} \\geq 0.7$, 10{,}000 random matrices per $\\varepsilon$). For each base matrix $C_0$, observations with $Y > \\text{median}(Y)$ are misclassified using a perturbed matrix $\\tilde{C} = \\text{renormalize}(C_0 + \\varepsilon \\cdot \\Delta)$ where $\\Delta_{jk} \\sim \\text{Uniform}(-1,1)$ for $j \\neq k$, while observations with $Y \\leq \\text{median}(Y)$ retain $C_0$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Effect of differential misclassification on bias violation rates (exposure DAG, $K{=}3$, $\\min_k C_{kk} \\geq 0.7$, $N{=}50{,}000$ MC samples per trial).}\n\\label{tab:nondiff_stress}\n\\begin{tabular}{cccc}\n\\toprule\n$\\varepsilon$ & Sign-Flip (\\%) & Amplification (\\%) & Any Violation (\\%) \\\\\n\\midrule\n0.00 & 2.0 & 11.5 & 13.3 \\\\\n0.01 & 2.4 & 12.4 & 14.7 \\\\\n0.05 & 2.8 & 13.0 & 15.7 \\\\\n0.10 & 4.5 & 16.7 & 20.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $\\varepsilon{=}0$ baseline (13.3\\% violation) closely matches the analytical result (13.7\\%) from Section~\\ref{sec:taxonomy_results}. Even at $\\varepsilon{=}0.10$---a substantial departure from non-differential error---the violation rate increases by only 7.6 percentage points. Small departures ($\\varepsilon \\leq 0.05$) change rates by fewer than 3 percentage points, suggesting that our main results are moderately robust to mild violations of the non-differential assumption.\n\n\\paragraph{Extended stress test.}\nAn extended stress test across 96 configurations (4 topologies $\\times$ 2 $K$ $\\times$ 3 CM qualities $\\times$ 4 $\\varepsilon$, 100 MC replications each; Table~\\ref{tab:stress-test}) confirms these patterns broadly: at $\\varepsilon{=}0$, sign-flip rates are zero for all configurations; at $\\varepsilon{=}0.10$, the maximum sign-flip rate is 7\\% (IV, low-quality $C_{kk}{=}0.4$, $K{=}3$). At $K{=}10$, sign-flip rates remain zero for all topologies and $\\varepsilon$ values, suggesting that higher $K$ provides additional robustness to differential misclassification.\n\n\\input{exp_a_stress_test_table.tex}\n\n\\subsection{Robustness to Nonlinear DGP}\n\\label{sec:logistic_dgp}\n\nWe replace the linear structural equations with $Y \\sim \\text{Bernoulli}(\\sigma(\\mathbf{x}^\\top\\boldsymbol{\\beta}))$ and estimate via logistic regression (control function for IV) for three representative topologies, using $K{=}3$, six real VAST confusion matrices, 500 MC replications, and $N{=}10{,}000$. Mean sign-flip rates across the six CMs:\n\n\\begin{center}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTopology & Linear SF$_\\tau$ & Logistic SF$_\\tau$ & Linear SF$_\\text{any}$ & Logistic SF$_\\text{any}$ \\\\\n\\midrule\nConfounding & 0.000 & 0.000 & 0.573 & 0.559 \\\\\nExposure & --- & --- & 0.577 & 0.574 \\\\\nIV & 0.071 & 0.065 & 0.071 & 0.565 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{center}\n\nTreatment-effect sign-flip rates (SF$_\\tau$) differ by $< 0.01$ across all topologies. The SF$_\\text{any}$ discrepancy for IV reflects estimator dimensionality: the control function includes a residual coefficient prone to sign noise; the core comparison is SF$_\\tau$, where both estimators agree ($\\approx 7\\%$). Linear and logistic DGPs produce virtually identical sign-flip patterns ($|\\Delta\\,\\text{SF}_\\tau| < 0.02$).\n\n\\subsection{Bootstrap Uncertainty of ASV}\n\\label{sec:bootstrap_asv}\n\nWe assess confusion-matrix estimation uncertainty by bootstrapping label pairs from HumAID DeepSeek zero-shot ($K{=}10$, $n{=}1{,}500$): resample with replacement $B{=}1{,}000$ times, re-estimate $C_0$, and recompute magnitude ASV $\\delta^*$ at a 10\\% bias threshold.\n\n\\begin{center}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nTopology & $\\delta^*$ (point) & 95\\% CI & Valid / 1000 \\\\\n\\midrule\nConfounding & --- & --- & 0 \\\\\nExposure & 0.937 & [0.602, 1.363] & 907 \\\\\nIV & 0.754 & [0.435, 1.290] & 902 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{center}\n\nConfounding never reaches the 10\\% threshold across all 1{,}000 bootstraps, confirming robustness. For IV, the 95\\% CI spans a $3{\\times}$ range (0.435 to 1.290); practitioners should bootstrap $C_0$ rather than rely on a point estimate when ASV is near the decision boundary.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.9\\columnwidth]{exp_c_bootstrap_figure.pdf}\n\\caption{Bootstrap distribution of magnitude ASV $\\delta^*$ ($B{=}1{,}000$) for HumAID DeepSeek zero-shot ($K{=}10$). Dashed line: point estimate; shaded: 95\\% CI.}\n\\label{fig:bootstrap_asv}\n\\end{figure}\n\n\\subsection{ASV Stability Across DGP Parameters}\n\\label{sec:asv_stability}\n\nWe test whether ASV rankings are stable across different data-generating process (DGP) configurations by varying the treatment-effect vector $\\boldsymbol{\\beta}$ across three settings: alternating-large ($\\boldsymbol{\\beta}=[0,\\,1.0,\\,-0.5]$), same-sign ($\\boldsymbol{\\beta}=[0,\\,0.5,\\,0.3]$), and alternating-small ($\\boldsymbol{\\beta}=[0,\\,0.2,\\,-0.1]$), with $K{=}3$, $\\tau{=}0.5$, and five $C_0$ diagonal values $\\in\\{0.5,0.6,0.7,0.8,0.9\\}$.\n\n\\input{exp_e_asv_stability_table.tex}\n\nThree patterns emerge (Table~\\ref{tab:asv_stability}). First, IV magnitude ASV is identical across all three DGPs ($\\delta^*{=}0.203$). This is a mathematical identity, not an empirical finding: the Wald estimator $\\hat{\\tau}_{\\text{IV}} = \\text{RF}/\\text{FS}$ has $\\boldsymbol{\\beta}$ in both numerator and denominator, and the ratio depends only on $C$ and the first-stage structure, making ASV invariant to $\\boldsymbol{\\beta}$ by construction. Second, exposure ASV depends on the coefficient ratio structure: alternating-large ($\\beta_2/\\beta_1 = -0.5$) and alternating-small ($\\beta_2/\\beta_1 = -0.5$) share the same ratio and yield identical $\\delta^*{=}0.090$, while same-sign ($\\beta_2/\\beta_1 = 0.6$) gives $\\delta^*{=}0.223$---thus the experiment provides two distinct sign-structure conditions, not three. Third, confounding ASV depends on effect magnitudes: only alternating-large triggers the 10\\% threshold ($\\delta^*{=}0.348$); smaller effects never reach 10\\% bias.\n\nConfounding is consistently the most robust topology (highest ASV or no violation), and M-bias remains immune (not shown). However, the relative fragility of exposure vs.\\ IV inverts with coefficient sign structure: under alternating signs, exposure is most fragile ($0.090 < 0.203$); under same-sign effects, IV is most fragile ($0.203 < 0.223$). Practitioners should compute ASV with their specific DGP rather than relying on generic rankings.\n\n\\subsection{Extended Conjecture Verification}\n\\label{sec:conjecture_verify}\n\nWe test envelope monotonicity (Conjecture~\\ref{conj:monotone}) by sampling 10{,}000 random $C_0$ matrices from Dirichlet$(1,\\dots,1)$ per topology for $K \\in \\{3,5,7\\}$ (210{,}000 total), sweeping $\\delta$ in steps of 0.01, and counting matrices with at least one non-monotonic step exceeding tolerance $10^{-12}$. Bias at each $\\delta$ is computed via analytic probability limits using Gauss--Hermite quadrature (100 points), eliminating sampling noise entirely.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Envelope monotonicity violations per 10{,}000 random $C_0$ matrices. ``Worst mag.''\\ is the largest single-step deviation $|B(\\delta_{i+1})|-|B(\\delta_i)|$ in the non-monotonic direction.}\n\\label{tab:conjecture_verify}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Topology} & $K{=}3$ & $K{=}5$ & $K{=}7$ & \\textbf{Worst mag.} & \\textbf{Direction} \\\\\n\\midrule\nConfounding & 8467 & 8063 & 7892 & 0.011 & non-dec \\\\\nMediation   & 8236 & 7905 & 7893 & 0.013 & non-dec \\\\\nCollider    & 8683 & 7669 & 7570 & 0.005 & non-inc \\\\\nExposure    & 485  & 205  & 77   & 0.056 & non-dec \\\\\nM-bias      & 9791 & 7783 & 7399 & 0.002 & non-inc \\\\\nIV          & 7433 & 6015 & 5711 & $>10^6$ & non-dec \\\\\nFront-door  & 8429 & 8079 & 7899 & 0.013 & non-dec \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nViolation counts are high (60--97\\% of matrices), but magnitudes are negligible for non-IV topologies: all worst-case deviations fall below 0.06 ($<$6\\% of the respective $\\tau$). These results are computed from analytic probability limits with zero sampling noise, confirming the violations are structural properties of multi-class confusion matrices rather than numerical artifacts. IV deviations reflect Wald estimator singularities when the first-stage coefficient passes near zero---this is a property of the Wald estimator, not of the ASV parameterization. Adversarial search (500 restarts per configuration, $K \\in \\{3,5\\}$) finds genuine counterexamples for all topologies except IV $K{=}3$, confirming that strict monotonicity does not hold universally. The bias envelope is $\\varepsilon$-approximately monotonic with $\\varepsilon < 0.06$ for all six non-IV topologies, supporting the practical validity of ASV as a sensitivity tool at any meaningful bias threshold.\n\n\\section{Notation}\n\\label{app:notation_table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Key notation used throughout the paper.}\n\\label{tab:notation}\n\\begin{tabular}{cl}\n\\toprule\n\\textbf{Symbol} & \\textbf{Description} \\\\\n\\midrule\n$K$ & Number of annotation categories \\\\\n$C$ & Column-stochastic confusion matrix, $C_{jk} = P(A^*{=}j \\mid A{=}k)$ \\\\\n$A$, $A^*$ & True and observed (misclassified) annotation \\\\\n$T$ & Treatment variable \\\\\n$Y$ & Outcome variable \\\\\n$\\tau$ & Causal effect of interest \\\\\n$\\delta$ & ASV perturbation parameter, $C(\\delta) = (1{-}\\delta)I + \\delta C_0$ \\\\\n$\\delta^*$ & Critical ASV value (magnitude/significance/sign-flip) \\\\\n$B(C)$ & Bias function, $= \\operatorname{plim}(\\hat{\\tau}) - \\tau$ \\\\\n$\\beta_k$ & Treatment effect coefficient for category $k$ \\\\\n$D_k$ & Dummy variable for category $k$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 926,
      "startLine": 1,
      "totalLines": 926
    }
  },
  "sourceToolAssistantUUID": "76905a48-91dc-4eaa-b1fd-2e91eed5bf2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-22T13:41:31.344Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VrjcyEdQpunkkUnAENJ4WC`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_3/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33e7e5ed-3edf-4b51-820e-1043379010fb",
  "isSidechain": false,
  "requestId": "req_011CbHhjawZAWLgmCx6xMRHN",
  "type": "assistant",
  "uuid": "3582b1b2-887b-4da4-9828-a71c3c305a99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y4dsySXmb6d31aQhSGZ6LP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2311,
      "cache_creation_input_tokens": 2246,
      "cache_read_input_tokens": 38265,
      "output_tokens": 893,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2246,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2311,
          "output_tokens": 893,
          "cache_read_input_tokens": 38265,
          "cache_creation_input_tokens": 2246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2246
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

_source line 50 · 2026-05-22T13:41:31.508Z_

<details><summary>↩ Tool result · `toolu_01VrjcyEdQpunkkUnAENJ4WC`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 844506 May 22 13:38 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_3/submitted.pdf
PDF_EXISTS
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3582b1b2-887b-4da4-9828-a71c3c305a99",
  "isSidechain": false,
  "promptId": "e832977f-06f5-437f-9468-12b340b28a19",
  "type": "user",
  "uuid": "11f75c97-2956-4974-a70f-61b865641ea4",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 844506 May 22 13:38 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_3/submitted.pdf\nPDF_EXISTS",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3582b1b2-887b-4da4-9828-a71c3c305a99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-22T13:41:32.042Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VrYkERxVbz1E3KRybu1W67`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11f75c97-2956-4974-a70f-61b865641ea4",
  "isSidechain": false,
  "requestId": "req_011CbHhjawZAWLgmCx6xMRHN",
  "type": "assistant",
  "uuid": "9ddda5fc-e994-4d5d-a8b5-9d9b3d207ce6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y4dsySXmb6d31aQhSGZ6LP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2311,
      "cache_creation_input_tokens": 2246,
      "cache_read_input_tokens": 38265,
      "output_tokens": 893,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2246,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2311,
          "output_tokens": 893,
          "cache_read_input_tokens": 38265,
          "cache_creation_input_tokens": 2246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2246
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

_source line 52 · 2026-05-22T13:41:32.108Z_

<details><summary>↩ Tool result · `toolu_01VrYkERxVbz1E3KRybu1W67`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 15026 May 22 11:12 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml
EXISTS
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ddda5fc-e994-4d5d-a8b5-9d9b3d207ce6",
  "isSidechain": false,
  "promptId": "e832977f-06f5-437f-9468-12b340b28a19",
  "type": "user",
  "uuid": "c666f4f5-9554-499d-919e-dc48cc25a1eb",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 15026 May 22 11:12 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\nEXISTS",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "9ddda5fc-e994-4d5d-a8b5-9d9b3d207ce6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 53_

```json
{
  "type": "last-prompt",
  "lastPrompt": "系统通知：审稿审批已通过。请开始审稿。  [论文提交] - 项目: causal_annot_error_attrib - 论文路径: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex - 目标 venue: EMNLP 2026 - 投稿类别: Long…",
  "leafUuid": "c666f4f5-9554-499d-919e-dc48cc25a1eb",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "Review causal annotation error attribution paper",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Assistant

_source line 55 · 2026-05-22T13:42:11.393Z_

<details><summary>Logged reasoning block</summary>

```text
Great, I now have:

1. All paper sections read
2. PDF exists (844KB, dated May 22 13:38)
3. review_issues.yaml exists from prior rounds
4. EMNLP 2026 venue info confirmed

Since this is a "fresh" review mode (重新审稿), I should treat this as a first-time review. But I should still read the review_issues.yaml to understand the history, as it's persistent. Actually, wait - the CLAUDE.md says:

"**重新审稿模式（fresh）** —— 收到 "🚀 审稿阶段已启动" 的 kick-off 消息时（无论是首次还是 Round N 重新审稿），你**没有任何上一轮的记忆或痕迹**：session 已 reset、外部审稿状态已清空、CLAUDE.md 锁定本轮论文路径。

But actually the review_issues.yaml is a persistent file that I should still read for context. And the review-director-session-start skill says in Step 4: "用 `read_local_file("projects/{project}/artifacts/review_issues.yaml")` 读当前 tracker"

Let me continue with the process. I need to check the external review config, then decide on reviewer assignment and dispatch the visual check before assigning reviewers.

For EMNLP 2026, the guideline calls for 2 reviewers given it's a general conference. This paper has substantial theoretical content with multi-class bias expressions across DAG topologies, an ASV sensitivity framework, correction methods, and extensive empirical validation with real LLM confusion matrices. I'll split the assignments: one reviewer focusing on method rigor and experimental design, another on novelty, related work coverage, writing quality, and format compliance. Let me check if external review is configured. I'm checking the external review status and dispatching a visual check in parallel, then I'll assign the two reviewers based on EMNLP 2026's requirements—which calls for an ARR unified review, 8-page main text with unlimited references, a mandatory Limitations section, and double-blind review by May 25, 2026.

For the first reviewer, I'm focusing on mathematical rigor and experimental validity—checking whether the seven topology bias expressions are correct, whether Theorem 1's proof holds up, and whether the experimental design and results are convincing. The second reviewer will assess novelty relative to recent work like Teblunthuis 2024 and Lee et al. 2024, verify that important references aren't missing, evaluate writing quality, and confirm compliance with the 8-page format requirement.

Now I'm composing the reviewer assignment messages and dispatching everything in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c666f4f5-9554-499d-919e-dc48cc25a1eb",
  "isSidechain": false,
  "requestId": "req_011CbHhkoF16pVxVSLb91GuR",
  "type": "assistant",
  "uuid": "ec1ce9b8-efa3-4dab-95f0-d745f87f289e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6wn1cmuEbLW8a2HBbUk6w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39918,
      "cache_read_input_tokens": 40511,
      "output_tokens": 4069,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 39918,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4069,
          "cache_read_input_tokens": 40511,
          "cache_creation_input_tokens": 39918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 39918
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

_source line 56 · 2026-05-22T13:42:15.879Z_

论文全文已读完。这是一篇方法论密集的长文，覆盖 7 种 DAG 拓扑下多分类标注误差的偏差分析、ASV 敏感性框架、5 种校正方法评估，以及真实 LLM confusion matrix 的实证验证。

**审稿编排决定**：EMNLP 2026（一般会议），分配 **2 名 Reviewer**：
- **Reviewer 1**：方法严谨性——数学推导正确性、证明完备性、实验设计与统计方法
- **Reviewer 2**：新颖性与完整性——创新贡献评估、相关工作覆盖、写作质量、格式合规

现在并行派发视觉审查 + 外部审稿检查 + 分配 Reviewer。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec1ce9b8-efa3-4dab-95f0-d745f87f289e",
  "isSidechain": false,
  "requestId": "req_011CbHhkoF16pVxVSLb91GuR",
  "type": "assistant",
  "uuid": "96a079ca-fd28-4f41-89b5-cefcd8146d4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6wn1cmuEbLW8a2HBbUk6w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39918,
      "cache_read_input_tokens": 40511,
      "output_tokens": 4069,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 39918,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4069,
          "cache_read_input_tokens": 40511,
          "cache_creation_input_tokens": 39918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 39918
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

_source line 57 · 2026-05-22T13:42:17.719Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check · `toolu_014maVdfvWcrYzxAFjuxkHoq`</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96a079ca-fd28-4f41-89b5-cefcd8146d4f",
  "isSidechain": false,
  "requestId": "req_011CbHhkoF16pVxVSLb91GuR",
  "type": "assistant",
  "uuid": "8a11801a-2f9c-41c5-9e26-809b13271a2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6wn1cmuEbLW8a2HBbUk6w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39918,
      "cache_read_input_tokens": 40511,
      "output_tokens": 4069,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 39918,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4069,
          "cache_read_input_tokens": 40511,
          "cache_creation_input_tokens": 39918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 39918
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

_source line 58 · 2026-05-22T13:42:18.245Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status · `toolu_01Voy6uGL9dBSL98tkv3GJ7i`</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a11801a-2f9c-41c5-9e26-809b13271a2c",
  "isSidechain": false,
  "requestId": "req_011CbHhkoF16pVxVSLb91GuR",
  "type": "assistant",
  "uuid": "3b6271fc-930a-4bd4-8611-18b7c6f5d79a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6wn1cmuEbLW8a2HBbUk6w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39918,
      "cache_read_input_tokens": 40511,
      "output_tokens": 4069,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 39918,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4069,
          "cache_read_input_tokens": 40511,
          "cache_creation_input_tokens": 39918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 39918
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

_source line 59 · 2026-05-22T13:42:21.653Z_

<details><summary>↩ Tool result · `toolu_014maVdfvWcrYzxAFjuxkHoq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a11801a-2f9c-41c5-9e26-809b13271a2c",
  "isSidechain": false,
  "promptId": "e832977f-06f5-437f-9468-12b340b28a19",
  "type": "user",
  "uuid": "68143fea-d08c-4ebf-978d-4e1a4fad14f8",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"status\\\": \\\"started\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "8a11801a-2f9c-41c5-9e26-809b13271a2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-22T13:42:21.667Z_

<details><summary>↩ Tool result · `toolu_01Voy6uGL9dBSL98tkv3GJ7i`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b6271fc-930a-4bd4-8611-18b7c6f5d79a",
  "isSidechain": false,
  "promptId": "e832977f-06f5-437f-9468-12b340b28a19",
  "type": "user",
  "uuid": "62f18390-3ea9-4868-a3b2-7006533f8588",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"status\\\": \\\"not_requested\\\", \\\"message\\\": \\\"No external review requested.\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "3b6271fc-930a-4bd4-8611-18b7c6f5d79a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-22T13:42:42.258Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer · `toolu_01XutV6jPpee7yth3Ai5GThJ`</summary>

```json
{
  "reviewer_id": "1",
  "round_number": 1,
  "text": "## 审稿任务分配 — Reviewer 1（方法严谨性）\n\n### 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_3/submitted.pdf`\n- **目标 venue**: EMNLP 2026 (via ARR)\n- **投稿类别**: Long Paper\n\n### Venue 要求\n- ARR 统一审稿，截止日期 2026-05-25\n- 正文 8 页限制 + 无限参考文献页\n- 强制 Limitations 章节（不计入页数）\n- ACL 模板，\\usepackage[review]{acl}\n- Double-blind（匿名）\n- Overall Assessment 评分标准：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 你的审查侧重：方法严谨性 + 实验设计\n\n请重点审查以下方面：\n\n1. **数学推导正确性**：\n   - 7 种 DAG 拓扑的 bias 表达式（Eq. 1-6）是否正确推导\n   - Proposition 1 的三个子结论（confounding/collider 的 sign preservation，exposure 的 sign reversal）是否成立\n   - Theorem 1（envelope monotonicity for confounding, proportional effects）的证明是否严密\n   - Conjecture 1（ε-approximate monotonicity for 6 topologies）的数值验证是否充分\n   - 附录中 Lemma 1（Bias decomposition）和各 Proposition 的证明链是否完整\n\n2. **ASV 框架的理论基础**：\n   - 三类 ASV（magnitude/significance/sign-flip）的定义是否清晰、互补\n   - δ 参数化 C(δ) = (1-δ)I + δC₀ 的选择是否合理、是否有已知替代方案\n   - significance ASV 的 N-sensitivity 相变现象是否有理论解释\n   - 与 E-value 的类比是否恰当\n\n3. **实验设计与统计方法**：\n   - 100,000 Dirichlet(1,1,1) 随机矩阵采样是否足够，是否有采样偏差\n   - Monte Carlo 验证（N=10,000）的 MAPE 2.0% 是否在合理范围\n   - 经验验证使用 3 个任务/4 个 LLM 的覆盖面是否充分\n   - 校正方法实验（210 configurations）的设计是否公平\n   - Bootstrap ASV 的样本量（n=1,500, B=1,000）是否足够\n\n4. **FWL 不变性结论**：\n   - 对 4 种拓扑 matrix-based 校正 0% bias reduction 的论证是否严密\n   - 是否有遗漏的 bypass 途径\n\n5. **潜在技术问题**：\n   - non-differential misclassification 假设在实践中的合理性\n   - 线性 SEM 假设的限制\n   - Conjecture 未证明是否构成方法论缺陷\n\n请按 ARR 标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses、Questions、Overall Assessment（使用上述评分标准）和 Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62f18390-3ea9-4868-a3b2-7006533f8588",
  "isSidechain": false,
  "requestId": "req_011CbHhkoF16pVxVSLb91GuR",
  "type": "assistant",
  "uuid": "3a7a0765-1d16-420d-afe7-20cdfec7ff92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6wn1cmuEbLW8a2HBbUk6w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39918,
      "cache_read_input_tokens": 40511,
      "output_tokens": 4069,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 39918,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4069,
          "cache_read_input_tokens": 40511,
          "cache_creation_input_tokens": 39918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 39918
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

_source line 62 · 2026-05-22T13:42:43.719Z_

<details><summary>↩ Tool result · `toolu_01XutV6jPpee7yth3Ai5GThJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a7a0765-1d16-420d-afe7-20cdfec7ff92",
  "isSidechain": false,
  "promptId": "e832977f-06f5-437f-9468-12b340b28a19",
  "type": "user",
  "uuid": "26fc2c7e-2e61-426a-bdfa-46f50de18964",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reviewer_key\\\": \\\"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "3a7a0765-1d16-420d-afe7-20cdfec7ff92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-22T13:43:00.838Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer · `toolu_01XTMLxJodqWWsL5cSzb5pPW`</summary>

```json
{
  "reviewer_id": "2",
  "round_number": 1,
  "text": "## 审稿任务分配 — Reviewer 2（新颖性与完整性）\n\n### 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_3/submitted.pdf`\n- **目标 venue**: EMNLP 2026 (via ARR)\n- **投稿类别**: Long Paper\n\n### Venue 要求\n- ARR 统一审稿，截止日期 2026-05-25\n- 正文 8 页限制 + 无限参考文献页\n- 强制 Limitations 章节（不计入页数）\n- ACL 模板，\\usepackage[review]{acl}\n- Double-blind（匿名）\n- Overall Assessment 评分标准：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 你的审查侧重：新颖性 + 完整性 + 写作 + 格式\n\n请重点审查以下方面：\n\n1. **新颖性评估**：\n   - 相对于 Teblunthuis (2024)（binary, 4 DAG scenarios）和 Lee, Wood-Doughty (2024)（categorical LLM classifiers, confounding only）的增量贡献是否足够\n   - ASV 框架相对于 E-values (VanderWeele & Ding 2017) 和概率偏差分析 (Lash 2009) 的技术创新程度\n   - FWL 不变性是否是已知结论的直接推论\n   - \"topology-dependent\" 视角是否构成足够的概念创新\n\n2. **相关工作覆盖**：\n   - 测量误差文献是否有重要遗漏（Carroll 2006, Gustafson 2004 已引用）\n   - NLP 因果推断文献是否完整（Feder et al. 2022, Keith et al. 2020 已引用）\n   - LLM annotation 质量文献是否有新发表的遗漏\n   - PPI++ / Cross-PPI 文献线是否完整\n   - 是否有因果推断领域的重要 sensitivity analysis 方法未被讨论\n\n3. **写作质量**：\n   - 论文结构是否合理（Abstract → Intro → Related Work → Method → Experiments → Conclusion）\n   - 符号体系是否一致\n   - 图表质量和信息密度\n   - 是否有过度 claim 或不当 hedging\n   - Abstract 是否准确反映论文内容和贡献\n\n4. **格式合规**：\n   - 正文是否在 8 页以内（不含参考文献和 Limitations）\n   - Limitations 章节是否存在且内容合适（不含新实验/分析）\n   - 是否使用 \\usepackage[review]{acl}\n   - 是否匿名（无作者信息泄露）\n   - 附录是否合理使用（是否有本应在正文的关键信息放在了附录）\n\n5. **论文的 broader impact 和定位**：\n   - 对 CL/NLP 社区的实际价值\n   - 是否适合 EMNLP 的主题范围（empirical methods for NLP）\n   - 论文的受众是谁——是否对 NLP 实践者有可操作性\n\n请按 ARR 标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses、Questions、Missing References、Overall Assessment（使用上述评分标准）和 Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26fc2c7e-2e61-426a-bdfa-46f50de18964",
  "isSidechain": false,
  "requestId": "req_011CbHhkoF16pVxVSLb91GuR",
  "type": "assistant",
  "uuid": "b31c9428-4720-4071-b726-a0d72dd30520",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6wn1cmuEbLW8a2HBbUk6w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39918,
      "cache_read_input_tokens": 40511,
      "output_tokens": 4069,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 39918,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4069,
          "cache_read_input_tokens": 40511,
          "cache_creation_input_tokens": 39918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 39918
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

_source line 64 · 2026-05-22T13:43:02.389Z_

<details><summary>↩ Tool result · `toolu_01XTMLxJodqWWsL5cSzb5pPW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b31c9428-4720-4071-b726-a0d72dd30520",
  "isSidechain": false,
  "promptId": "e832977f-06f5-437f-9468-12b340b28a19",
  "type": "user",
  "uuid": "b4a57b00-f9d5-4882-b28f-54f92acbcc23",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reviewer_key\\\": \\\"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "b31c9428-4720-4071-b726-a0d72dd30520",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 65 · 2026-05-22T13:43:02.394Z_

```json
{
  "parentUuid": "b4a57b00-f9d5-4882-b28f-54f92acbcc23",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "5bea0e04-2d0d-44d1-a255-df724f484192",
  "timestamp": "2026-05-22T13:43:02.394Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 66_

```json
{
  "type": "ai-title",
  "aiTitle": "Review causal annotation error attribution paper",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Runtime record

_source line 67 · 2026-05-22T13:49:17.665Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T13:49:17.665Z",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "content": "[Reviewer 2 审稿意见]:\n## Reviewer 2 审稿意见 — Round 1（新颖性 + 完整性 + 写作 + 格式）\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (via ARR), Long Paper\n\n---\n\n## 总体评分\n**Overall**: 3.5 — Borderline Conference\n**一句话总结**: 系统性地刻画了多分类标注误差在七种因果 DAG 拓扑下的传播差异，填补了文献空白；但理论深度中等，对 sign reversal 严重性的表述存在过度声称，且正文超页。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 核心 bias 表达式正确，5 拓扑的 sign preservation 中 2 个有解析证明（confounding/collider）、3 个仅有数值验证（Empirical Finding 1）；Conjecture 1 未证明；non-differential 假设的 stress test 范围有限 |\n| **Excitement** | 3/5 | \"topology-dependent\" 视角新颖且实用，ASV 工具可操作，FWL invariance 结果被忽视但重要；但 bias 表达式推导直接，ASV 是 E-value 的自然类比，K≥3 break 已被 Dosemeci (1990) 和 Veierød & Laake (2001) 指出 |\n| **Reproducibility** | 4/5 | 数学公式清晰，DGP 参数详细，仿真设置可复现；但未提及代码/数据公开 |\n| **Confidence** | 4/5 | 熟悉因果推断方法论和测量误差理论，逐页仔细阅读含附录 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 正文超出 8 页限制\n- 具体位置：Page 9（Section 4.5 尾段 + Section 5 Conclusion 在第 9 页）\n- 问题：EMNLP 2026 Long Paper 正文限 8 页（不含 References 和 Limitations）。Section 4.5 的最后若干段和 Section 5 (Conclusion) 溢出到第 9 页。即使 Limitations 不计入页数，Section 5 属于正文，目前大约超出 0.5 页。`main.tex` 中已使用 `\\enlargethispage{1\\baselineskip}` 和压缩 `\\floatsep` 等手段，说明作者已在挤压空间但仍未达标。\n- 为什么影响接收：ARR desk rejection 条件之一。即使不被 desk reject，reviewer 也应标记。\n- 建议修改方向：压缩 Section 4（如将 Cross-K robustness 段和 ASV diagnostic results 段移至附录）；Figure 1+2 占满整页，考虑缩小或合并。\n\n**N2** [critical] Sign reversal 的实际严重性被过度声称\n- 具体位置：Abstract（\"83.4% sign reversal\"）、Section 1 第 2 段（\"catastrophic\"）、Section 4.4（\"61% of exposure configurations exhibit coefficient-level sign reversal\"）\n- 问题：Abstract 和 Introduction 大量引用 83.4% sign reversal 数据，但这来自均匀 Dirichlet(1,1,1) 先验——一个包含大量非对角占优矩阵的不现实分布。在实际 LLM 分类器精度下（diagonal ≥ 0.7），sign reversal 降至 2.1%（Section 4.2 第 2 段）。更重要的是，Section 4.4 的实证结果显示 sign reversal **仅发生在 secondary coefficients**（\"corresponding to rare categories with small |β|\"），primary coefficient（最大|β|）在所有 23 个配置中从未反转。这与 abstract 中\"catastrophic\"的框架存在重大落差。\n- 为什么影响接收：Reviewer 最敏感的问题之一是 overclaiming。83.4% 数字在 abstract/intro/conclusion 中反复出现，给读者留下\"多数情况下因果估计方向错误\"的印象，但实际只在极端参数空间和次要系数上成立。\n- 建议修改方向：(1) Abstract 中先报告 realistic regime（diagonal ≥ 0.7）的 2.1% sign reversal，再提 Dirichlet prior 的 83.4% 作为理论上界；(2) 明确说明 empirical sign reversal 限于 secondary coefficients；(3) 用 \"structurally possible\" 替代 \"catastrophic\" 等极端措辞。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Sign preservation 的 3/5 拓扑缺乏解析证明\n- 具体位置：Section 3.2 Empirical Finding 1（mediation, M-bias, front-door）\n- 问题：论文声称\"五个拓扑维持 structural sign-flip guarantee\"，但 Proposition 1 只覆盖 confounding 和 collider（解析证明）。Mediation、M-bias、front-door 三个拓扑的 sign preservation 标记为 \"Empirical Finding\"，基于 100,000 随机矩阵的数值验证而非解析证明。论文在 Empirical Finding 1 中承认\"analytic proofs for general K remain open\"，但在 abstract 和 conclusion 中说\"establish that five topologies show no sign reversal\"，\"establish\" 一词暗示证明而非数值验证。\n- 建议：在 abstract/conclusion 中区分\"proven\"（2 个）和\"numerically verified\"（3 个），或者用\"show\"替代\"establish\"。\n\n**W2** [warning] Conjecture 1（ε-approximate monotonicity）支撑 ASV 有效性，但未证明\n- 具体位置：Section 3.3 Conjecture 1、Theorem 1\n- 问题：Theorem 1 只对 confounding topology 在 proportional effects 假设下证明了单调性。其余 5 个 non-IV 拓扑的 ASV 单调性依赖 Conjecture 1，且 ε < 0.06 的 bound 来自数值模拟。如果单调性不成立，δ 作为\"annotation error severity dial\"的解释就不成立，ASV 的排序意义也受影响。\n- 建议：(1) 更明确地讨论 Conjecture 1 失败时的后果；(2) 考虑证明 mediation 和 collider 等较简单拓扑的单调性。\n\n**W3** [warning] Non-differential misclassification 假设对 LLM 的适用性讨论不足\n- 具体位置：Definition 1 (Section 3.1)、Limitations\n- 问题：LLM annotator 处理包含 Y 和 Z 信息的文本，P(A*|A,Y,Z) = P(A*|A) 在文本分类场景中很可能不成立。Appendix B.4 的 stress test 仅检验 ε=0.05 的微小偏离，且只覆盖 exposure 拓扑。对于一个以\"LLM annotation\"为卖点的框架，这个基础假设需要更充分的讨论和更强的鲁棒性分析。\n- 建议：(1) 在正文 Method 部分讨论何时 LLM 满足 non-differential 条件（如 LLM 未见 outcome 文本时）；(2) stress test 扩展到更多拓扑和更大 ε。\n\n**W4** [warning] 缺少 outcome misclassification 的讨论\n- 具体位置：Section 3（整个 Method 部分）\n- 问题：许多 NLP 因果研究中 Y 也是 LLM 标注的（如 sentiment → political engagement）。当 A 和 Y 同时被误分类时，bias 的传播更为复杂。论文完全未讨论这一场景，Related Work 中也未提及。\n- 建议：至少在 Limitations 或 Related Work 中讨论 outcome misclassification 的影响和扩展方向。\n\n**W5** [warning] Abstract 信息过载\n- 具体位置：Abstract（整段）\n- 问题：Abstract 约 200 词中塞入了 15+ 个数字（83.4%, 52.6%, 13.7%, 2.1%, 47.0%, 88%, 61%, 0.7 等），读起来像是 results summary 而非 motivated preview。ARR reviewer 通常在 abstract 阶段形成第一印象。\n- 建议：Abstract 保留 3-4 个最关键数字，其余移至正文。重点是 \"what's new and why it matters\"，而非所有数字的罗列。\n\n**W6** [warning] 未提及代码/数据公开\n- 具体位置：全文\n- 问题：方法论论文的可复现性很大程度依赖代码。论文包含大量仿真实验（100,000 矩阵 × 7 拓扑 × 多 K 值），但未提及代码是否会公开。ASV 计算工具如果作为 package 发布，实用价值会大幅提升。\n- 建议：承诺公开代码，或在 supplementary 中提供。\n\n---\n\n## 小问题（不影响接收）\n\n- Section 4.2 第 1 段：\"grand MAPE of 2.0% across 126 scenarios (18 LLM configurations × 7 topologies)\" — 18×7=126 的推导依赖 empirical validation 的具体设置，但这里还在 Monte Carlo 验证部分，126 的解释容易混淆。\n- Table 1 caption 很长（约 4 行），可以精简。\n- Figure 2 中标签文字较小，在打印版中可能难以辨认。\n- Section 3.3 中 ASV 的 parameterization C(δ) = (1-δ)I + δC₀ 在 δ=0 时给出完美分类，这意味着 ASV 衡量的是\"从完美到 C₀ 的退化路径上\"的敏感性——如果实际 confusion matrix 不在这条路径上呢？这个局限性未讨论。\n- references.bib 中 `messing2026`（Hidden Measurement Error in LLM Pipelines）已引入但在正文中未看到引用，可能是 orphan entry。\n\n---\n\n## 新颖性专项评估\n\n### 相对于 Teblunthuis (2024) 的增量\n**充分**。Teblunthuis 限于 binary (K=2) 和 4 个 DAG。本文扩展到 K≥3 并证明了质的变化（sign reversal 可能性），覆盖 7 个拓扑且包含敏感性分析框架（ASV）和校正指南。增量不仅是数量上的（更多拓扑），更是性质上的（K≥3 的代数 break）。\n\n### 相对于 Lee & Wood-Doughty (2024) 的增量\n**充分**。Lee & Wood-Doughty 仅覆盖 confounding topology。本文证明了同一 confusion matrix 在不同拓扑下产生质的不同 bias，这是 Lee & Wood-Doughty 无法得出的结论。\n\n### ASV 相对于 E-values 和 PBA 的技术创新\n**中等**。ASV 的 parameterization C(δ) 是 E-value 思路的自然类比，三种 ASV 类型（magnitude/significance/sign-flip）的动机来自拓扑依赖的失败模式。Theorem 1 的单调性证明有技术贡献但限于 proportional effects。创新程度 adequate 但不 exciting。\n\n### FWL 不变性\n**重要但技术上直接**。这是一个被文献忽视的实用观察——矩阵校正方法在 4/7 拓扑上 provably 无效。技术上是 FWL 定理的直接推论，但对实践者意义重大。\n\n### \"Topology-dependent\" 视角\n**足够的概念创新**。虽然测量误差在不同位置的效果已有零散讨论，但系统性的 7 拓扑对比是第一次。这个视角将碎片化的知识统一到一个框架中。\n\n---\n\n## 相关工作覆盖评估\n\n### 已覆盖（关键引用）\n- 测量误差核心：Carroll (2006) ✓, Gustafson (2004) ✓, Hernán & Cole (2009) ✓\n- NLP 因果推断：Feder et al. (2022) ✓, Keith et al. (2020) ✓, Wood-Doughty (2018) ✓\n- LLM 标注质量：Baumann et al. (2025) ✓, Kim & Garg (2025) ✓, Cheng et al. (2024) ✓\n- 校正方法：PPI++ ✓, Cross-PPI ✓, DSL ✓, Gligoric et al. (2025) ✓\n- 敏感性分析：E-values ✓, PBA (Lash 2009) ✓, Rosenbaum (2002) ✓\n\n### 可能的遗漏\n1. **Cinelli & Hazlett (2020)** \"Making Sense of Sensitivity: Extending Omitted Variable Bias\" — 提出了 modern sensitivity analysis 的 robustness value 框架，与 ASV 有直接可比性，应在 Section 2 或 3.3 中讨论对比。\n2. **Gilardi et al. (2023)** \"ChatGPT Outperforms Crowd-Workers for Text-Annotation Tasks\" — LLM 标注的标志性论文，虽非因果推断方向但经常被引用在 LLM annotation 文献综述中。\n3. **Ziems et al. (2024)** \"Can Large Language Models Transform Computational Social Science?\" — 综合性 survey 覆盖 LLM 在社会科学中的标注应用，与论文的 motivation 直接相关。\n4. **Bound, Brown & Mathiowetz (2001)** 关于 survey data 中 measurement error 的经典综述，虽然是 survey 领域但多分类误分类的讨论与本文相关。\n5. 论文未讨论 **Bayesian measurement error models**（如 Gustafson 2004 中的方法）作为 FWL-invariant 拓扑的校正替代方案，Section 4.5 中仅一笔带过\"Bayesian measurement error models\"但未引用具体工作。\n\n### PPI++ / Cross-PPI 文献线\n**基本完整**。引用了 Angelopoulos et al. (2023), Zrnic & Candes (2024), Gligoric et al. (2025)。缺少 Angelopoulos et al. (2023b) \"PPI++: When Is Prediction-Powered Inference Worth It?\" 如果存在的话。\n\n---\n\n## 格式合规检查\n\n| 检查项 | 状态 | 备注 |\n|--------|------|------|\n| `\\usepackage[review]{acl}` | ✓ | main.tex line 2 |\n| 匿名 | ✓ | `\\author{Anonymous}` |\n| 正文 ≤ 8 页 | **✗** | 正文延伸至第 9 页（Section 4.5 尾段 + Section 5 Conclusion），超约 0.5 页 |\n| Limitations 存在 | ✓ | 在 conclusion.tex 中，\\section*{Limitations}，约 1 段 |\n| Limitations 无新实验 | ✓ | 仅讨论假设局限和未来方向 |\n| 附录合理使用 | ✓ | 证明、补充表格、stress test、case study 均适合附录 |\n| 关键信息是否在正文 | 基本 ✓ | 核心结果在正文；但 sign preservation 的 sufficient conditions 汇总（Table 2, Appendix A.9）对理解 Proposition 1 很重要，可考虑在正文中简述 |\n\n---\n\n## 主要优势\n\n1. **系统性的 taxonomy**：首次在统一框架下对比 7 种 DAG 拓扑的多分类误分类效应，概念贡献清晰。\n2. **K≥3 代数 break 的刻画**：证明 K=2 的 sign preservation 在 K≥3 时结构性崩塌，这是一个非平凡的 qualitative 结果。\n3. **FWL invariance 的实用洞察**：证明矩阵校正方法对 4/7 拓扑无效，对实践者直接可操作，文献中被忽视。\n4. **ASV 框架**：提供了一个 parameterized 的敏感性分析工具，类比 E-values 但针对 annotation error，有实际应用价值。\n5. **丰富的实证验证**：100,000 矩阵的仿真 + 4 个 LLM × 3 数据集的 empirical validation + logistic DGP robustness check + case study，验证覆盖面广。\n6. **写作结构清晰**：Abstract → Intro → Related Work → Method → Experiments → Conclusion 的组织合理，符号体系一致。\n\n---\n\n## 关于论文定位和受众\n\n**EMNLP 适配性**：高。论文直接回答\"NLP 社区用 LLM 做标注时因果推断可靠吗\"这一实际问题，符合 EMNLP \"empirical methods for NLP\" 的主题。\n\n**目标受众**：(1) 用 LLM 标注做因果推断的计算社会科学家；(2) text-as-data 方法论研究者；(3) 对测量误差感兴趣的统计学家。\n\n**可操作性**：中等偏高。论文的 taxonomy（Table 1）和 correction guidance（Section 4.5）直接可用。但 ASV 的实际使用需要估计 confusion matrix C₀，而论文未提供工具或 package。\n\n---\n\n## Questions to Authors\n\n1. 在 realistic regime（diagonal ≥ 0.7）下，sign reversal rate 仅 2.1%。请作者解释为何 abstract 和 introduction 选择以 83.4%（Dirichlet prior）作为主要数字而非 2.1%？\n2. Empirical Finding 1（mediation, M-bias, front-door 的 sign preservation）是否有证明进展？如果这 3 个拓扑的保证只是 conjectural，论文的核心 claim \"five topologies maintain structural guarantee\" 的可信度如何评估？\n3. 论文是否计划公开代码？ASV 计算工具如果作为 Python package 发布，对论文影响力会有实质提升。\n4. C(δ) = (1-δ)I + δC₀ 的线性路径是否是唯一合理的 parameterization？如果实际退化路径不在这条线上（如 off-diagonal 结构随 δ 变化），ASV 的意义如何？"
}
```

---

### Runtime record

_source line 68 · 2026-05-22T13:49:17.665Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T13:49:17.665Z",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

## Round 2

2 recorded events

### User

_source line 69 · 2026-05-22T13:49:17.654Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5bea0e04-2d0d-44d1-a255-df724f484192",
  "isSidechain": false,
  "promptId": "76316ba6-c864-45f0-936b-195158a85937",
  "type": "user",
  "isMeta": true,
  "uuid": "ec0bea9c-1563-413e-bd39-3ad98a55bb37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 70 · 2026-05-22T13:49:17.654Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec0bea9c-1563-413e-bd39-3ad98a55bb37",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "aa842995-5600-426e-8fe5-e0d41283b706",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "id": "b916b447-e16a-4448-bab2-abb9ddd36103",
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

_source line 71 · 2026-05-22T13:49:17.782Z_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见 — Round 1（新颖性 + 完整性 + 写作 + 格式）

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 (via ARR), Long Paper

---

## 总体评分
**Overall**: 3.5 — Borderline Conference
**一句话总结**: 系统性地刻画了多分类标注误差在七种因果 DAG 拓扑下的传播差异，填补了文献空白；但理论深度中等，对 sign reversal 严重性的表述存在过度声称，且正文超页。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 核心 bias 表达式正确，5 拓扑的 sign preservation 中 2 个有解析证明（confounding/collider）、3 个仅有数值验证（Empirical Finding 1）；Conjecture 1 未证明；non-differential 假设的 stress test 范围有限 |
| **Excitement** | 3/5 | "topology-dependent" 视角新颖且实用，ASV 工具可操作，FWL invariance 结果被忽视但重要；但 bias 表达式推导直接，ASV 是 E-value 的自然类比，K≥3 break 已被 Dosemeci (1990) 和 Veierød & Laake (2001) 指出 |
| **Reproducibility** | 4/5 | 数学公式清晰，DGP 参数详细，仿真设置可复现；但未提及代码/数据公开 |
| **Confidence** | 4/5 | 熟悉因果推断方法论和测量误差理论，逐页仔细阅读含附录 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 正文超出 8 页限制
- 具体位置：Page 9（Section 4.5 尾段 + Section 5 Conclusion 在第 9 页）
- 问题：EMNLP 2026 Long Paper 正文限 8 页（不含 References 和 Limitations）。Section 4.5 的最后若干段和 Section 5 (Conclusion) 溢出到第 9 页。即使 Limitations 不计入页数，Section 5 属于正文，目前大约超出 0.5 页。`main.tex` 中已使用 `\enlargethispage{1\baselineskip}` 和压缩 `\floatsep` 等手段，说明作者已在挤压空间但仍未达标。
- 为什么影响接收：ARR desk rejection 条件之一。即使不被 desk reject，reviewer 也应标记。
- 建议修改方向：压缩 Section 4（如将 Cross-K robustness 段和 ASV diagnostic results 段移至附录）；Figure 1+2 占满整页，考虑缩小或合并。

**N2** [critical] Sign reversal 的实际严重性被过度声称
- 具体位置：Abstract（"83.4% sign reversal"）、Section 1 第 2 段（"catastrophic"）、Section 4.4（"61% of exposure configurations exhibit coefficient-level sign reversal"）
- 问题：Abstract 和 Introduction 大量引用 83.4% sign reversal 数据，但这来自均匀 Dirichlet(1,1,1) 先验——一个包含大量非对角占优矩阵的不现实分布。在实际 LLM 分类器精度下（diagonal ≥ 0.7），sign reversal 降至 2.1%（Section 4.2 第 2 段）。更重要的是，Section 4.4 的实证结果显示 sign reversal **仅发生在 secondary coefficients**（"corresponding to rare categories with small |β|"），primary coefficient（最大|β|）在所有 23 个配置中从未反转。这与 abstract 中"catastrophic"的框架存在重大落差。
- 为什么影响接收：Reviewer 最敏感的问题之一是 overclaiming。83.4% 数字在 abstract/intro/conclusion 中反复出现，给读者留下"多数情况下因果估计方向错误"的印象，但实际只在极端参数空间和次要系数上成立。
- 建议修改方向：(1) Abstract 中先报告 realistic regime（diagonal ≥ 0.7）的 2.1% sign reversal，再提 Dirichlet prior 的 83.4% 作为理论上界；(2) 明确说明 empirical sign reversal 限于 secondary coefficients；(3) 用 "structurally possible" 替代 "catastrophic" 等极端措辞。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Sign preservation 的 3/5 拓扑缺乏解析证明
- 具体位置：Section 3.2 Empirical Finding 1（mediation, M-bias, front-door）
- 问题：论文声称"五个拓扑维持 structural sign-flip guarantee"，但 Proposition 1 只覆盖 confounding 和 collider（解析证明）。Mediation、M-bias、front-door 三个拓扑的 sign preservation 标记为 "Empirical Finding"，基于 100,000 随机矩阵的数值验证而非解析证明。论文在 Empirical Finding 1 中承认"analytic proofs for general K remain open"，但在 abstract 和 conclusion 中说"establish that five topologies show no sign reversal"，"establish" 一词暗示证明而非数值验证。
- 建议：在 abstract/conclusion 中区分"proven"（2 个）和"numerically verified"（3 个），或者用"show"替代"establish"。

**W2** [warning] Conjecture 1（ε-approximate monotonicity）支撑 ASV 有效性，但未证明
- 具体位置：Section 3.3 Conjecture 1、Theorem 1
- 问题：Theorem 1 只对 confounding topology 在 proportional effects 假设下证明了单调性。其余 5 个 non-IV 拓扑的 ASV 单调性依赖 Conjecture 1，且 ε < 0.06 的 bound 来自数值模拟。如果单调性不成立，δ 作为"annotation error severity dial"的解释就不成立，ASV 的排序意义也受影响。
- 建议：(1) 更明确地讨论 Conjecture 1 失败时的后果；(2) 考虑证明 mediation 和 collider 等较简单拓扑的单调性。

**W3** [warning] Non-differential misclassification 假设对 LLM 的适用性讨论不足
- 具体位置：Definition 1 (Section 3.1)、Limitations
- 问题：LLM annotator 处理包含 Y 和 Z 信息的文本，P(A*|A,Y,Z) = P(A*|A) 在文本分类场景中很可能不成立。Appendix B.4 的 stress test 仅检验 ε=0.05 的微小偏离，且只覆盖 exposure 拓扑。对于一个以"LLM annotation"为卖点的框架，这个基础假设需要更充分的讨论和更强的鲁棒性分析。
- 建议：(1) 在正文 Method 部分讨论何时 LLM 满足 non-differential 条件（如 LLM 未见 outcome 文本时）；(2) stress test 扩展到更多拓扑和更大 ε。

**W4** [warning] 缺少 outcome misclassification 的讨论
- 具体位置：Section 3（整个 Method 部分）
- 问题：许多 NLP 因果研究中 Y 也是 LLM 标注的（如 sentiment → political engagement）。当 A 和 Y 同时被误分类时，bias 的传播更为复杂。论文完全未讨论这一场景，Related Work 中也未提及。
- 建议：至少在 Limitations 或 Related Work 中讨论 outcome misclassification 的影响和扩展方向。

**W5** [warning] Abstract 信息过载
- 具体位置：Abstract（整段）
- 问题：Abstract 约 200 词中塞入了 15+ 个数字（83.4%, 52.6%, 13.7%, 2.1%, 47.0%, 88%, 61%, 0.7 等），读起来像是 results summary 而非 motivated preview。ARR reviewer 通常在 abstract 阶段形成第一印象。
- 建议：Abstract 保留 3-4 个最关键数字，其余移至正文。重点是 "what's new and why it matters"，而非所有数字的罗列。

**W6** [warning] 未提及代码/数据公开
- 具体位置：全文
- 问题：方法论论文的可复现性很大程度依赖代码。论文包含大量仿真实验（100,000 矩阵 × 7 拓扑 × 多 K 值），但未提及代码是否会公开。ASV 计算工具如果作为 package 发布，实用价值会大幅提升。
- 建议：承诺公开代码，或在 supplementary 中提供。

---

## 小问题（不影响接收）

- Section 4.2 第 1 段："grand MAPE of 2.0% across 126 scenarios (18 LLM configurations × 7 topologies)" — 18×7=126 的推导依赖 empirical validation 的具体设置，但这里还在 Monte Carlo 验证部分，126 的解释容易混淆。
- Table 1 caption 很长（约 4 行），可以精简。
- Figure 2 中标签文字较小，在打印版中可能难以辨认。
- Section 3.3 中 ASV 的 parameterization C(δ) = (1-δ)I + δC₀ 在 δ=0 时给出完美分类，这意味着 ASV 衡量的是"从完美到 C₀ 的退化路径上"的敏感性——如果实际 confusion matrix 不在这条路径上呢？这个局限性未讨论。
- references.bib 中 `messing2026`（Hidden Measurement Error in LLM Pipelines）已引入但在正文中未看到引用，可能是 orphan entry。

---

## 新颖性专项评估

### 相对于 Teblunthuis (2024) 的增量
**充分**。Teblunthuis 限于 binary (K=2) 和 4 个 DAG。本文扩展到 K≥3 并证明了质的变化（sign reversal 可能性），覆盖 7 个拓扑且包含敏感性分析框架（ASV）和校正指南。增量不仅是数量上的（更多拓扑），更是性质上的（K≥3 的代数 break）。

### 相对于 Lee & Wood-Doughty (2024) 的增量
**充分**。Lee & Wood-Doughty 仅覆盖 confounding topology。本文证明了同一 confusion matrix 在不同拓扑下产生质的不同 bias，这是 Lee & Wood-Doughty 无法得出的结论。

### ASV 相对于 E-values 和 PBA 的技术创新
**中等**。ASV 的 parameterization C(δ) 是 E-value 思路的自然类比，三种 ASV 类型（magnitude/significance/sign-flip）的动机来自拓扑依赖的失败模式。Theorem 1 的单调性证明有技术贡献但限于 proportional effects。创新程度 adequate 但不 exciting。

### FWL 不变性
**重要但技术上直接**。这是一个被文献忽视的实用观察——矩阵校正方法在 4/7 拓扑上 provably 无效。技术上是 FWL 定理的直接推论，但对实践者意义重大。

### "Topology-dependent" 视角
**足够的概念创新**。虽然测量误差在不同位置的效果已有零散讨论，但系统性的 7 拓扑对比是第一次。这个视角将碎片化的知识统一到一个框架中。

---

## 相关工作覆盖评估

### 已覆盖（关键引用）
- 测量误差核心：Carroll (2006) ✓, Gustafson (2004) ✓, Hernán & Cole (2009) ✓
- NLP 因果推断：Feder et al. (2022) ✓, Keith et al. (2020) ✓, Wood-Doughty (2018) ✓
- LLM 标注质量：Baumann et al. (2025) ✓, Kim & Garg (2025) ✓, Cheng et al. (2024) ✓
- 校正方法：PPI++ ✓, Cross-PPI ✓, DSL ✓, Gligoric et al. (2025) ✓
- 敏感性分析：E-values ✓, PBA (Lash 2009) ✓, Rosenbaum (2002) ✓

### 可能的遗漏
1. **Cinelli & Hazlett (2020)** "Making Sense of Sensitivity: Extending Omitted Variable Bias" — 提出了 modern sensitivity analysis 的 robustness value 框架，与 ASV 有直接可比性，应在 Section 2 或 3.3 中讨论对比。
2. **Gilardi et al. (2023)** "ChatGPT Outperforms Crowd-Workers for Text-Annotation Tasks" — LLM 标注的标志性论文，虽非因果推断方向但经常被引用在 LLM annotation 文献综述中。
3. **Ziems et al. (2024)** "Can Large Language Models Transform Computational Social Science?" — 综合性 survey 覆盖 LLM 在社会科学中的标注应用，与论文的 motivation 直接相关。
4. **Bound, Brown & Mathiowetz (2001)** 关于 survey data 中 measurement error 的经典综述，虽然是 survey 领域但多分类误分类的讨论与本文相关。
5. 论文未讨论 **Bayesian measurement error models**（如 Gustafson 2004 中的方法）作为 FWL-invariant 拓扑的校正替代方案，Section 4.5 中仅一笔带过"Bayesian measurement error models"但未引用具体工作。

### PPI++ / Cross-PPI 文献线
**基本完整**。引用了 Angelopoulos et al. (2023), Zrnic & Candes (2024), Gligoric et al. (2025)。缺少 Angelopoulos et al. (2023b) "PPI++: When Is Prediction-Powered Inference Worth It?" 如果存在的话。

---

## 格式合规检查

| 检查项 | 状态 | 备注 |
|--------|------|------|
| `\usepackage[review]{acl}` | ✓ | main.tex line 2 |
| 匿名 | ✓ | `\author{Anonymous}` |
| 正文 ≤ 8 页 | **✗** | 正文延伸至第 9 页（Section 4.5 尾段 + Section 5 Conclusion），超约 0.5 页 |
| Limitations 存在 | ✓ | 在 conclusion.tex 中，\section*{Limitations}，约 1 段 |
| Limitations 无新实验 | ✓ | 仅讨论假设局限和未来方向 |
| 附录合理使用 | ✓ | 证明、补充表格、stress test、case study 均适合附录 |
| 关键信息是否在正文 | 基本 ✓ | 核心结果在正文；但 sign preservation 的 sufficient conditions 汇总（Table 2, Appendix A.9）对理解 Proposition 1 很重要，可考虑在正文中简述 |

---

## 主要优势

1. **系统性的 taxonomy**：首次在统一框架下对比 7 种 DAG 拓扑的多分类误分类效应，概念贡献清晰。
2. **K≥3 代数 break 的刻画**：证明 K=2 的 sign preservation 在 K≥3 时结构性崩塌，这是一个非平凡的 qualitative 结果。
3. **FWL invariance 的实用洞察**：证明矩阵校正方法对 4/7 拓扑无效，对实践者直接可操作，文献中被忽视。
4. **ASV 框架**：提供了一个 parameterized 的敏感性分析工具，类比 E-values 但针对 annotation error，有实际应用价值。
5. **丰富的实证验证**：100,000 矩阵的仿真 + 4 个 LLM × 3 数据集的 empirical validation + logistic DGP robustness check + case study，验证覆盖面广。
6. **写作结构清晰**：Abstract → Intro → Related Work → Method → Experiments → Conclusion 的组织合理，符号体系一致。

---

## 关于论文定位和受众

**EMNLP 适配性**：高。论文直接回答"NLP 社区用 LLM 做标注时因果推断可靠吗"这一实际问题，符合 EMNLP "empirical methods for NLP" 的主题。

**目标受众**：(1) 用 LLM 标注做因果推断的计算社会科学家；(2) text-as-data 方法论研究者；(3) 对测量误差感兴趣的统计学家。

**可操作性**：中等偏高。论文的 taxonomy（Table 1）和 correction guidance（Section 4.5）直接可用。但 ASV 的实际使用需要估计 confusion matrix C₀，而论文未提供工具或 package。

---

## Questions to Authors

1. 在 realistic regime（diagonal ≥ 0.7）下，sign reversal rate 仅 2.1%。请作者解释为何 abstract 和 introduction 选择以 83.4%（Dirichlet prior）作为主要数字而非 2.1%？
2. Empirical Finding 1（mediation, M-bias, front-door 的 sign preservation）是否有证明进展？如果这 3 个拓扑的保证只是 conjectural，论文的核心 claim "five topologies maintain structural guarantee" 的可信度如何评估？
3. 论文是否计划公开代码？ASV 计算工具如果作为 Python package 发布，对论文影响力会有实质提升。
4. C(δ) = (1-δ)I + δC₀ 的线性路径是否是唯一合理的 parameterization？如果实际退化路径不在这条线上（如 off-diagonal 结构随 δ 变化），ASV 的意义如何？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa842995-5600-426e-8fe5-e0d41283b706",
  "isSidechain": false,
  "promptId": "76316ba6-c864-45f0-936b-195158a85937",
  "type": "user",
  "uuid": "bf25b7a3-3b30-4841-9720-31ac646aa583",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 72_

```json
{
  "type": "ai-title",
  "aiTitle": "Review causal annotation error attribution paper",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Runtime record

_source line 73 · 2026-05-22T13:49:37.787Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T13:49:37.787Z",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "content": "[Reviewer 2 审稿结果]:\nReviewer 2 审稿完成。主要结论：\n\n- **Overall 3.5（Borderline Conference）**\n- **2 个 Must-Fix**：正文超 8 页限制（约 0.5 页）；sign reversal 严重性被过度声称（83.4% 来自不现实的 Dirichlet prior，实际 LLM 矩阵下仅影响 secondary coefficients）\n- **6 个 Should-Fix**：3/5 sign preservation 拓扑缺解析证明、Conjecture 1 未证明、non-differential 假设讨论不足、缺少 outcome misclassification 讨论、abstract 数字过载、未承诺代码公开\n- **新颖性评估**：相对 Teblunthuis (2024) 和 Lee & Wood-Doughty (2024) 的增量充分；ASV 创新中等（E-value 自然类比）；FWL invariance 技术直接但实用价值高；topology-dependent 视角是足够的概念创新"
}
```

---

### Runtime record

_source line 74 · 2026-05-22T13:49:37.787Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T13:49:37.787Z",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Assistant

_source line 75 · 2026-05-22T13:49:37.776Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf25b7a3-3b30-4841-9720-31ac646aa583",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "bd54b3ba-36b3-40a9-8b76-eb2e7884d4e9",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "id": "81b9024e-9470-4dc6-823f-f54efb63c556",
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

_source line 76 · 2026-05-22T13:49:37.901Z_

[Reviewer 2 审稿结果]:
Reviewer 2 审稿完成。主要结论：

- **Overall 3.5（Borderline Conference）**
- **2 个 Must-Fix**：正文超 8 页限制（约 0.5 页）；sign reversal 严重性被过度声称（83.4% 来自不现实的 Dirichlet prior，实际 LLM 矩阵下仅影响 secondary coefficients）
- **6 个 Should-Fix**：3/5 sign preservation 拓扑缺解析证明、Conjecture 1 未证明、non-differential 假设讨论不足、缺少 outcome misclassification 讨论、abstract 数字过载、未承诺代码公开
- **新颖性评估**：相对 Teblunthuis (2024) 和 Lee & Wood-Doughty (2024) 的增量充分；ASV 创新中等（E-value 自然类比）；FWL invariance 技术直接但实用价值高；topology-dependent 视角是足够的概念创新

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd54b3ba-36b3-40a9-8b76-eb2e7884d4e9",
  "isSidechain": false,
  "promptId": "3b9f8a19-fa14-4e2d-ab07-208ce168f954",
  "type": "user",
  "uuid": "3bade6e0-bce2-487d-a73f-a28aaa45765f",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 77_

```json
{
  "type": "ai-title",
  "aiTitle": "Review causal annotation error attribution paper",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Runtime record

_source line 78 · 2026-05-22T13:53:53.021Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T13:53:53.021Z",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "content": "[Reviewer 1 审稿意见]:\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 理论框架新颖且重要（K≥3 break point, ASV, FWL invariance），但核心单调性结果仅为 Conjecture，线性 SEM 限制实际适用性，且正文可能超出 8 页限制。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 已有证明（Theorem 1, Propositions 1-5）正确，但核心单调性结果仅覆盖 confounding+proportional effects，其余 6 拓扑为 Conjecture；线性 SEM 假设限制了结论的普适性 |\n| Excitement | 3.5/5 | 首个系统研究多类标注误差×因果推断的框架，K≥3 algebraic break 和 FWL invariance 发现有实际指导价值，但线性假设和非差异误分类假设限制了 NLP 社区的直接适用性 |\n| Reproducibility | 4/5 | 分析推导详尽（12页附录），实验参数完整（Dirichlet 采样、MC 样本量、Bootstrap 配置均有报告），代码未提供但可从方程重现 |\n| Confidence | 4/5 | 熟悉测量误差理论和因果推断文献，仔细阅读了全部证明和附录 |\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Theorem 1 适用范围过窄，Conjecture 1 缺乏证明\n- 具体位置：Section 3.3 (p.5), Theorem 1 & Conjecture 1; Appendix C, Table 9 (p.22)\n- 问题：论文唯一被证明的单调性结果（Theorem 1）仅覆盖 confounding 拓扑 + proportional effects（β = λα）这一特殊条件。其余 6 个非 IV 拓扑的单调性依赖 Conjecture 1，而 Table 9 显示 60-97% 的随机矩阵违反严格单调性。虽然违反幅度小（worst-case < 0.06），但高频违反意味着 ASV vulnerability spectrum 的理论基础不够坚实。\n- 为什么影响接收：ASV 框架的核心价值依赖于 |bias| 随 δ 单调变化——如果不成立，\"临界 δ 阈值\"的语义变得模糊，ASV 不再是一个 well-defined 的 sensitivity measure。对于一篇强调理论贡献的论文，核心结果是 numerically-verified conjecture 而非 theorem，是显著弱点。\n- 建议修改方向：(1) 至少再证明一个拓扑（如 mediation，其 indirect effect 结构较简洁，可能可推导出解析证明）；(2) 给出 ε 关于 K 和 DGP 参数的 formal bound，而非仅依赖经验验证；(3) 如果完整证明不可行，应明确讨论 Conjecture 失败时 ASV 的 interpretation 如何 degrade。\n\n**N2** [critical] 正文疑似超出 8 页限制\n- 具体位置：Sections 1-5, pages 1-9\n- 问题：Section 5 (Conclusion) 在第 9 页开始，意味着正文（不含 Limitations 和 References）约为 8.3 页。EMNLP 2026 long paper 限制为严格 8 页。\n- 为什么影响接收：可能导致 desk rejection。\n- 建议修改方向：压缩 Section 2 (Related Work) 和 Section 4.2 (Bias Taxonomy 的实验细节，部分可移入附录) 以控制在 8 页内。\n\n**N3** [critical] FWL invariance 结论缺乏严格证明\n- 具体位置：Section 4.5 (p.8-9), Appendix B.3 (p.19), Algorithm 1 (p.19)\n- 问题：论文声称\"matrix-based corrections achieve exactly 0% bias reduction\"对 4 个 FWL 拓扑成立，但这一 quantitative claim 主要依赖实验结果（Table 4），而非 formal proof。三个关键问题未澄清：\n  (a) \"matrix-based correction\" 的精确定义是什么？MLA 调整的是群体级分布，SIMEX 通过模拟额外噪声并外推来修正——两者的操作机制截然不同，为何都导致 0% reduction？\n  (b) SIMEX 在 individual level 工作（模拟额外误分类后外推至零误差），其外推函数的形式假设（线性/二次）是否适用于分类误差设定？Theorem 1 表明 confounding bias 关于 δ 确实是单调的，理论上 SIMEX 的外推应能工作——那么 0% reduction 的结果是否说明 SIMEX 实现中存在问题？\n  (c) 这一发现与测量误差文献中已知的\"controlling for a mismeasured confounder leaves residual confounding\"结果（Carroll et al., 2006; Ogburn & VanderWeele, 2012）的关系是什么？\n- 为什么影响接收：没有 formal proof，读者无法区分这是一个深刻的理论洞察还是实验设置的 artifact。\n- 建议修改方向：添加一个 formal proposition 证明 FWL invariance，明确指出对每种 correction method 为何成立（或不成立）。\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 非差异误分类假设对 LLM 标注者可能不成立\n- 具体位置：Definition 1 (p.3), Appendix B.4 (p.20)\n- 问题：假设 P(A*|A,T,Y) = P(A*|A) 要求 LLM 标注误差在给定真实标签后独立于处理和结果。但在 NLP 中，文本内容同时决定 LLM 分类、处理变量和结果变量，自然产生依赖。Appendix B.4 的 stress test 仅测试 ε ≤ 0.10 的轻微偏离，且 ε = 0.10 时 bias violation rate 已增加 7.4 个百分点。\n- 建议：(1) 讨论非差异假设在哪些具体 NLP 场景下成立/失败（如情感分析 vs. 政治立场检测）；(2) 至少为 exposure 和 confounding 拓扑推导 differential misclassification 下的 bias 表达式骨架。\n\n**W2** [warning] 线性 SEM 假设限制实际适用性\n- 具体位置：Section 3.1 (p.3), Limitations (p.9), Appendix B.6 (p.20)\n- 问题：所有结果基于线性结构方程，但 NLP 因果推断通常使用 logistic/nonlinear 模型。Appendix B.6 仅对 3 个拓扑（K=3, logistic DGP）做了有限的 robustness check。论文自身承认\"FWL invariance result does not hold for logistic regressions\"——这意味着最重要的实践指导之一（Algorithm 1 中 FWL 拓扑的分流）在 nonlinear 设定下可能失效。\n- 建议：(1) 扩展 Appendix B.6 至全部 7 拓扑并包含更多 nonlinear DGP 变体；(2) 或在 Algorithm 1 中明确标注\"仅适用于线性模型\"的局限。\n\n**W3** [warning] Dirichlet(1,1,1) headline 数字具有误导性\n- 具体位置：Abstract, Section 4.2 (p.5)\n- 问题：Abstract 和 Introduction 以 Dirichlet(1,1,1) 全参数空间统计量（\"83.4% violation rate\", \"52.6% sign reversal\"）为主导，但该分布包含随机分类器（平均准确率 1/K）。更具实践参考价值的数字——C_kk ≥ 0.7 时 13.7% violation rate, 2.1% sign reversal——出现在后文且着墨较少。LLM 分类器通常达到 70-99% 准确率。\n- 建议：以 restricted parameter space 结果为主线叙事，Dirichlet(1,1,1) 结果作为理论完备性补充。\n\n**W4** [warning] 相对于测量误差文献的新颖性定位不清\n- 具体位置：Section 2 (p.2-3), throughout\n- 问题：几个结果在已有文献中有直接先例：(1) 多类变量的 attenuation with possible sign reversal 在 Carroll et al. (2006) 和 Gustafson (2004) 中有讨论；(2) 对 mismeasured confounder 的 residual confounding 在 Greenland (2003) 和 Ogburn & VanderWeele (2012) 中有分析。论文引用了这些工作但未明确界定\"哪些是已知结果在 LLM 语境的应用\"vs.\"哪些是真正新的贡献\"。\n- 建议：在 Related Work 或 Contribution 段落中添加一段明确的 novelty delineation：\"以下结果已在 binary misclassification 下被建立：... 我们的贡献将其扩展至 K≥3 并新证明了：...\"\n\n**W5** [warning] 经验验证使用模拟 DGP 而非真实因果数据\n- 具体位置：Section 4.4 (p.7-8)\n- 问题：\"Empirical validation\"使用真实 LLM confusion matrices 但应用于模拟 DGP（线性 SEM），而非使用已知因果效应的真实数据集。这验证的是理论推导的正确性（对线性 SEM 来说 trivially true），而非框架在实践中的指导价值。ClinicalBERT case study (Appendix B.2) 是回顾性应用，不是 prospective validation。\n- 建议：增加至少一个 semi-synthetic 实验——使用已知因果效应的数据集（如 RCT 数据），引入 LLM 标注误差，验证框架能否正确识别 topology-specific risk 并指导 correction 选择。\n\n## 小问题（不影响接收）\n- 记号在 τ 和 β_T 之间交替使用，缺少明确消歧\n- 正文 Proposition 1(a,b,c) 对应附录 Propositions 2, 3, 5 等不同编号——建议添加交叉引用帮助读者导航\n- Figure 2 (p.6) 的 y 轴标签在 PDF 中较小，影响可读性\n- Table 2 (p.17) conditions 列混合了 DGP 参数和形式化记号，风格不一致\n\n## 主要优势\n1. **重要且及时的问题**：LLM 标注质量与因果推断方法假设之间的差距日益严重，本文提供了首个系统性框架。\n2. **清晰的理论贡献**：K≥3 algebraic break point（K=2 始终 attenuate；K≥3 可 sign reverse）是一个优雅且对实践者有直接指导意义的结果。\n3. **实用性**：Algorithm 1 提供了 topology-aware correction 决策流程，ASV 框架给出了可量化的 sensitivity analysis 工具。\n4. **系统覆盖**：7 DAG 拓扑 × 5 correction methods × 多种验证方式的组合覆盖面全面。\n5. **附录质量高**：12 页证明和补充实验，Lemma-Proposition 证明链基本完整。\n6. **Cross-PPI 和 FWL bypass 方法的讨论**：不仅诊断问题（FWL invariance），还提供了替代方案，增加了论文的实践指导价值。\n"
}
```

---

### Runtime record

_source line 79 · 2026-05-22T13:53:53.021Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T13:53:53.021Z",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Assistant

_source line 80 · 2026-05-22T13:53:53.010Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3bade6e0-bce2-487d-a73f-a28aaa45765f",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "a81d6fa3-467a-419a-b760-f9bb677328a8",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "id": "791f8aa9-ac10-43cc-9e28-f99690301cc5",
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

11 recorded events

### User

_source line 81 · 2026-05-22T13:53:53.128Z_

[Reviewer 1 审稿意见]:

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 理论框架新颖且重要（K≥3 break point, ASV, FWL invariance），但核心单调性结果仅为 Conjecture，线性 SEM 限制实际适用性，且正文可能超出 8 页限制。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 已有证明（Theorem 1, Propositions 1-5）正确，但核心单调性结果仅覆盖 confounding+proportional effects，其余 6 拓扑为 Conjecture；线性 SEM 假设限制了结论的普适性 |
| Excitement | 3.5/5 | 首个系统研究多类标注误差×因果推断的框架，K≥3 algebraic break 和 FWL invariance 发现有实际指导价值，但线性假设和非差异误分类假设限制了 NLP 社区的直接适用性 |
| Reproducibility | 4/5 | 分析推导详尽（12页附录），实验参数完整（Dirichlet 采样、MC 样本量、Bootstrap 配置均有报告），代码未提供但可从方程重现 |
| Confidence | 4/5 | 熟悉测量误差理论和因果推断文献，仔细阅读了全部证明和附录 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] Theorem 1 适用范围过窄，Conjecture 1 缺乏证明
- 具体位置：Section 3.3 (p.5), Theorem 1 & Conjecture 1; Appendix C, Table 9 (p.22)
- 问题：论文唯一被证明的单调性结果（Theorem 1）仅覆盖 confounding 拓扑 + proportional effects（β = λα）这一特殊条件。其余 6 个非 IV 拓扑的单调性依赖 Conjecture 1，而 Table 9 显示 60-97% 的随机矩阵违反严格单调性。虽然违反幅度小（worst-case < 0.06），但高频违反意味着 ASV vulnerability spectrum 的理论基础不够坚实。
- 为什么影响接收：ASV 框架的核心价值依赖于 |bias| 随 δ 单调变化——如果不成立，"临界 δ 阈值"的语义变得模糊，ASV 不再是一个 well-defined 的 sensitivity measure。对于一篇强调理论贡献的论文，核心结果是 numerically-verified conjecture 而非 theorem，是显著弱点。
- 建议修改方向：(1) 至少再证明一个拓扑（如 mediation，其 indirect effect 结构较简洁，可能可推导出解析证明）；(2) 给出 ε 关于 K 和 DGP 参数的 formal bound，而非仅依赖经验验证；(3) 如果完整证明不可行，应明确讨论 Conjecture 失败时 ASV 的 interpretation 如何 degrade。

**N2** [critical] 正文疑似超出 8 页限制
- 具体位置：Sections 1-5, pages 1-9
- 问题：Section 5 (Conclusion) 在第 9 页开始，意味着正文（不含 Limitations 和 References）约为 8.3 页。EMNLP 2026 long paper 限制为严格 8 页。
- 为什么影响接收：可能导致 desk rejection。
- 建议修改方向：压缩 Section 2 (Related Work) 和 Section 4.2 (Bias Taxonomy 的实验细节，部分可移入附录) 以控制在 8 页内。

**N3** [critical] FWL invariance 结论缺乏严格证明
- 具体位置：Section 4.5 (p.8-9), Appendix B.3 (p.19), Algorithm 1 (p.19)
- 问题：论文声称"matrix-based corrections achieve exactly 0% bias reduction"对 4 个 FWL 拓扑成立，但这一 quantitative claim 主要依赖实验结果（Table 4），而非 formal proof。三个关键问题未澄清：
  (a) "matrix-based correction" 的精确定义是什么？MLA 调整的是群体级分布，SIMEX 通过模拟额外噪声并外推来修正——两者的操作机制截然不同，为何都导致 0% reduction？
  (b) SIMEX 在 individual level 工作（模拟额外误分类后外推至零误差），其外推函数的形式假设（线性/二次）是否适用于分类误差设定？Theorem 1 表明 confounding bias 关于 δ 确实是单调的，理论上 SIMEX 的外推应能工作——那么 0% reduction 的结果是否说明 SIMEX 实现中存在问题？
  (c) 这一发现与测量误差文献中已知的"controlling for a mismeasured confounder leaves residual confounding"结果（Carroll et al., 2006; Ogburn & VanderWeele, 2012）的关系是什么？
- 为什么影响接收：没有 formal proof，读者无法区分这是一个深刻的理论洞察还是实验设置的 artifact。
- 建议修改方向：添加一个 formal proposition 证明 FWL invariance，明确指出对每种 correction method 为何成立（或不成立）。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 非差异误分类假设对 LLM 标注者可能不成立
- 具体位置：Definition 1 (p.3), Appendix B.4 (p.20)
- 问题：假设 P(A*|A,T,Y) = P(A*|A) 要求 LLM 标注误差在给定真实标签后独立于处理和结果。但在 NLP 中，文本内容同时决定 LLM 分类、处理变量和结果变量，自然产生依赖。Appendix B.4 的 stress test 仅测试 ε ≤ 0.10 的轻微偏离，且 ε = 0.10 时 bias violation rate 已增加 7.4 个百分点。
- 建议：(1) 讨论非差异假设在哪些具体 NLP 场景下成立/失败（如情感分析 vs. 政治立场检测）；(2) 至少为 exposure 和 confounding 拓扑推导 differential misclassification 下的 bias 表达式骨架。

**W2** [warning] 线性 SEM 假设限制实际适用性
- 具体位置：Section 3.1 (p.3), Limitations (p.9), Appendix B.6 (p.20)
- 问题：所有结果基于线性结构方程，但 NLP 因果推断通常使用 logistic/nonlinear 模型。Appendix B.6 仅对 3 个拓扑（K=3, logistic DGP）做了有限的 robustness check。论文自身承认"FWL invariance result does not hold for logistic regressions"——这意味着最重要的实践指导之一（Algorithm 1 中 FWL 拓扑的分流）在 nonlinear 设定下可能失效。
- 建议：(1) 扩展 Appendix B.6 至全部 7 拓扑并包含更多 nonlinear DGP 变体；(2) 或在 Algorithm 1 中明确标注"仅适用于线性模型"的局限。

**W3** [warning] Dirichlet(1,1,1) headline 数字具有误导性
- 具体位置：Abstract, Section 4.2 (p.5)
- 问题：Abstract 和 Introduction 以 Dirichlet(1,1,1) 全参数空间统计量（"83.4% violation rate", "52.6% sign reversal"）为主导，但该分布包含随机分类器（平均准确率 1/K）。更具实践参考价值的数字——C_kk ≥ 0.7 时 13.7% violation rate, 2.1% sign reversal——出现在后文且着墨较少。LLM 分类器通常达到 70-99% 准确率。
- 建议：以 restricted parameter space 结果为主线叙事，Dirichlet(1,1,1) 结果作为理论完备性补充。

**W4** [warning] 相对于测量误差文献的新颖性定位不清
- 具体位置：Section 2 (p.2-3), throughout
- 问题：几个结果在已有文献中有直接先例：(1) 多类变量的 attenuation with possible sign reversal 在 Carroll et al. (2006) 和 Gustafson (2004) 中有讨论；(2) 对 mismeasured confounder 的 residual confounding 在 Greenland (2003) 和 Ogburn & VanderWeele (2012) 中有分析。论文引用了这些工作但未明确界定"哪些是已知结果在 LLM 语境的应用"vs."哪些是真正新的贡献"。
- 建议：在 Related Work 或 Contribution 段落中添加一段明确的 novelty delineation："以下结果已在 binary misclassification 下被建立：... 我们的贡献将其扩展至 K≥3 并新证明了：..."

**W5** [warning] 经验验证使用模拟 DGP 而非真实因果数据
- 具体位置：Section 4.4 (p.7-8)
- 问题："Empirical validation"使用真实 LLM confusion matrices 但应用于模拟 DGP（线性 SEM），而非使用已知因果效应的真实数据集。这验证的是理论推导的正确性（对线性 SEM 来说 trivially true），而非框架在实践中的指导价值。ClinicalBERT case study (Appendix B.2) 是回顾性应用，不是 prospective validation。
- 建议：增加至少一个 semi-synthetic 实验——使用已知因果效应的数据集（如 RCT 数据），引入 LLM 标注误差，验证框架能否正确识别 topology-specific risk 并指导 correction 选择。

## 小问题（不影响接收）
- 记号在 τ 和 β_T 之间交替使用，缺少明确消歧
- 正文 Proposition 1(a,b,c) 对应附录 Propositions 2, 3, 5 等不同编号——建议添加交叉引用帮助读者导航
- Figure 2 (p.6) 的 y 轴标签在 PDF 中较小，影响可读性
- Table 2 (p.17) conditions 列混合了 DGP 参数和形式化记号，风格不一致

## 主要优势
1. **重要且及时的问题**：LLM 标注质量与因果推断方法假设之间的差距日益严重，本文提供了首个系统性框架。
2. **清晰的理论贡献**：K≥3 algebraic break point（K=2 始终 attenuate；K≥3 可 sign reverse）是一个优雅且对实践者有直接指导意义的结果。
3. **实用性**：Algorithm 1 提供了 topology-aware correction 决策流程，ASV 框架给出了可量化的 sensitivity analysis 工具。
4. **系统覆盖**：7 DAG 拓扑 × 5 correction methods × 多种验证方式的组合覆盖面全面。
5. **附录质量高**：12 页证明和补充实验，Lemma-Proposition 证明链基本完整。
6. **Cross-PPI 和 FWL bypass 方法的讨论**：不仅诊断问题（FWL invariance），还提供了替代方案，增加了论文的实践指导价值。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a81d6fa3-467a-419a-b760-f9bb677328a8",
  "isSidechain": false,
  "promptId": "128d9f67-cbf3-40b6-8b31-60cfc4dfab75",
  "type": "user",
  "uuid": "34a1b5fd-821f-4c2a-93ac-4d2658d4c69c",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 82 · 2026-05-22T13:54:09.272Z_

Reviewer 1 审稿已收到。两位 Reviewer 均给出 3.5（Borderline Conference），且在多个关键问题上有重叠。现在进入 **Step 2：交叉分享**，将双方完整审稿意见互相转发，要求逐条 `[AGREE]`/`[REBUT]` 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34a1b5fd-821f-4c2a-93ac-4d2658d4c69c",
  "isSidechain": false,
  "requestId": "req_011CbHihRVbBEZSBsJSc2tki",
  "type": "assistant",
  "uuid": "01d4ad69-5ab7-494a-aa49-3a203b454d1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmYm3qPaaSQWnwCBbSGV4o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 3630,
      "cache_read_input_tokens": 90938,
      "output_tokens": 2584,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3630,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2584,
          "cache_read_input_tokens": 90938,
          "cache_creation_input_tokens": 3630,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3630
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

_source line 83 · 2026-05-22T13:54:39.000Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer · `toolu_01X6VK1K32fCbZzPAdAjgbBy`</summary>

```json
{
  "reviewer_id": "1",
  "round_number": 1,
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n**Overall**: 3.5 — Borderline Conference\n\n### Must-Fix 问题\n\n**N1** [critical] 正文超出 8 页限制\n- Section 4.5 尾段 + Section 5 (Conclusion) 溢出到第 9 页，超约 0.5 页。已使用 `\\enlargethispage` 和压缩 `\\floatsep` 等手段但仍未达标。ARR desk rejection 条件之一。\n\n**N2** [critical] Sign reversal 的实际严重性被过度声称\n- Abstract 和 Introduction 大量引用 83.4% sign reversal（来自 Dirichlet(1,1,1) 先验——包含大量不现实矩阵），在 diagonal ≥ 0.7 下降至 2.1%。更重要的是，empirical sign reversal **仅发生在 secondary coefficients**（small |β|），primary coefficient 从未反转。与 abstract 中\"catastrophic\"框架存在重大落差。建议先报告 realistic regime 的 2.1%，再提 Dirichlet 的 83.4% 作为理论上界。\n\n### Should-Fix 问题\n\n**W1** Sign preservation 的 3/5 拓扑缺乏解析证明（mediation, M-bias, front-door 标为\"Empirical Finding\"，但 abstract/conclusion 用\"establish\"暗示已证明）\n\n**W2** Conjecture 1（ε-approximate monotonicity）支撑 ASV 有效性但未证明\n\n**W3** Non-differential misclassification 假设对 LLM 的适用性讨论不足（stress test 仅覆盖 exposure 拓扑、ε≤0.10）\n\n**W4** 缺少 outcome misclassification 的讨论（Y 也可能是 LLM 标注的）\n\n**W5** Abstract 信息过载（15+ 个数字）\n\n**W6** 未提及代码/数据公开\n\n### 新颖性评估\n- 相对 Teblunthuis (2024) 和 Lee & Wood-Doughty (2024) 增量充分\n- ASV 创新中等（E-value 自然类比）\n- FWL invariance 技术直接但实用价值高\n- \"Topology-dependent\" 视角是足够的概念创新\n\n### 相关工作可能遗漏\n1. Cinelli & Hazlett (2020) \"Making Sense of Sensitivity\" — 与 ASV 有直接可比性\n2. Gilardi et al. (2023) \"ChatGPT Outperforms Crowd-Workers\"\n3. Ziems et al. (2024) \"Can Large Language Models Transform Computational Social Science?\"\n4. Bound, Brown & Mathiowetz (2001) 关于 survey data 中 measurement error\n5. Bayesian measurement error models 作为 FWL-invariant 拓扑的校正替代方案未引用具体工作\n\n### Questions\n1. 为何 abstract 选择 83.4% 而非 2.1% 作为主要数字？\n2. Empirical Finding 1 是否有证明进展？\n3. 是否计划公开代码？\n4. C(δ) 线性路径是否是唯一合理的 parameterization？\n\n---\n\n请逐条回应上述所有 Must-Fix、Should-Fix、新颖性评估、相关工作遗漏和 Questions。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01d4ad69-5ab7-494a-aa49-3a203b454d1f",
  "isSidechain": false,
  "requestId": "req_011CbHihRVbBEZSBsJSc2tki",
  "type": "assistant",
  "uuid": "f5d712b6-89b2-468e-be8b-1f18382ee869",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmYm3qPaaSQWnwCBbSGV4o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 3630,
      "cache_read_input_tokens": 90938,
      "output_tokens": 2584,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3630,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2584,
          "cache_read_input_tokens": 90938,
          "cache_creation_input_tokens": 3630,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3630
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

_source line 84 · 2026-05-22T13:54:42.981Z_

<details><summary>↩ Tool result · `toolu_01X6VK1K32fCbZzPAdAjgbBy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5d712b6-89b2-468e-be8b-1f18382ee869",
  "isSidechain": false,
  "promptId": "128d9f67-cbf3-40b6-8b31-60cfc4dfab75",
  "type": "user",
  "uuid": "0f59bad4-8d6b-4003-b762-d7bb4cb6e676",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reviewer_key\\\": \\\"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "f5d712b6-89b2-468e-be8b-1f18382ee869",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-22T13:55:02.526Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer · `toolu_01KmCkniMuhPMsN6v2uKUwwX`</summary>

```json
{
  "reviewer_id": "2",
  "round_number": 1,
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] Theorem 1 适用范围过窄，Conjecture 1 缺乏证明\n- Theorem 1 仅覆盖 confounding + proportional effects。其余 6 个 non-IV 拓扑的单调性依赖 Conjecture 1，而 Table 9 显示 60-97% 的随机矩阵违反严格单调性。虽然违反幅度小（< 0.06），但高频违反意味着 ASV vulnerability spectrum 的理论基础不够坚实。如果单调性不成立，\"临界 δ 阈值\"的语义变得模糊。建议至少再证明一个拓扑（如 mediation），或给出 ε 关于 K 和 DGP 参数的 formal bound。\n\n**N2** [critical] 正文疑似超出 8 页限制\n- Section 5 (Conclusion) 在第 9 页开始，正文约 8.3 页。\n\n**N3** [critical] FWL invariance 结论缺乏严格证明\n- 三个关键问题：(a) \"matrix-based correction\"的精确定义是什么？(b) SIMEX 在 individual level 工作，其外推函数形式假设是否适用于分类误差设定？Theorem 1 表明 confounding bias 关于 δ 单调——SIMEX 理论上应能工作，0% reduction 是否说明实现问题？(c) 与测量误差文献中已知的\"controlling for mismeasured confounder leaves residual confounding\"的关系？\n\n### Should-Fix 问题\n\n**W1** 非差异误分类假设对 LLM 标注者可能不成立（stress test 仅测 ε≤0.10 的轻微偏离）\n\n**W2** 线性 SEM 假设限制实际适用性（FWL invariance 在 logistic 下不成立——Algorithm 1 的分流建议可能失效）\n\n**W3** Dirichlet(1,1,1) headline 数字具有误导性（83.4% vs realistic 2.1%）\n\n**W4** 相对于测量误差文献的新颖性定位不清（哪些是已知结果在 LLM 语境的应用 vs 真正新贡献未明确界定）\n\n**W5** 经验验证使用模拟 DGP 而非真实因果数据（\"Empirical validation\"用真实 CM 但应用于模拟 DGP，验证的是理论推导正确性而非实践指导价值）\n\n### 主要优势\n1. 重要且及时的问题\n2. 清晰的理论贡献：K≥3 algebraic break point\n3. 实用性：Algorithm 1 + ASV 框架\n4. 系统覆盖：7 DAG × 5 correction methods\n5. 附录质量高（12 页证明）\n6. Cross-PPI 和 FWL bypass 方法讨论\n\n### 小问题\n- τ 和 β_T 记号交替使用\n- Proposition 编号在正文与附录不一致\n- Figure 2 y 轴标签较小\n- Table 2 conditions 列风格不一致\n\n---\n\n请逐条回应上述所有 Must-Fix、Should-Fix、主要优势和小问题。特别关注：\n1. 你是否同意 R1-N3（FWL invariance 需要 formal proof）？你的审稿中也提到了 FWL invariance 但评价为\"技术上直接\"——两位对此的严重性评估是否一致？\n2. R1-W5（经验验证用模拟 DGP 而非真实因果数据）——你如何看待这一批评？\n3. R1-W4（新颖性定位不清）与你的新颖性评估是否矛盾？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f59bad4-8d6b-4003-b762-d7bb4cb6e676",
  "isSidechain": false,
  "requestId": "req_011CbHihRVbBEZSBsJSc2tki",
  "type": "assistant",
  "uuid": "92a762d8-be12-4890-bc2c-edb24b9becb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmYm3qPaaSQWnwCBbSGV4o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 3630,
      "cache_read_input_tokens": 90938,
      "output_tokens": 2584,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3630,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2584,
          "cache_read_input_tokens": 90938,
          "cache_creation_input_tokens": 3630,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3630
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

_source line 86 · 2026-05-22T13:55:04.070Z_

<details><summary>↩ Tool result · `toolu_01KmCkniMuhPMsN6v2uKUwwX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92a762d8-be12-4890-bc2c-edb24b9becb2",
  "isSidechain": false,
  "promptId": "128d9f67-cbf3-40b6-8b31-60cfc4dfab75",
  "type": "user",
  "uuid": "63f5dff3-0c1a-404c-ba14-bd6bafa8ed3b",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reviewer_key\\\": \\\"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "92a762d8-be12-4890-bc2c-edb24b9becb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 87_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Reviewer 1 审稿意见]:  ## 总体评分 **Overall**: 3.5 (Borderline Conference) **一句话总结**: 理论框架新颖且重要（K≥3 break point, ASV, FWL invariance），但核心单调性结果仅为 Conjecture，线性 SEM 限制实际适用性，且正文可能超出 8 页限制。  ## 官方维度打分（ACL ARR R…",
  "leafUuid": "63f5dff3-0c1a-404c-ba14-bd6bafa8ed3b",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Runtime record

_source line 88_

```json
{
  "type": "ai-title",
  "aiTitle": "Review causal annotation error attribution paper",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Runtime record

_source line 89_

```json
{
  "type": "ai-title",
  "aiTitle": "Review causal annotation error attribution paper",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Runtime record

_source line 90 · 2026-05-22T13:55:12.320Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T13:55:12.320Z",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "content": "[Reviewer 1 审稿结果]:\n清理完成。审稿任务已结束。"
}
```

---

### Runtime record

_source line 91 · 2026-05-22T13:55:12.320Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T13:55:12.320Z",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

## Round 6

2 recorded events

### User

_source line 92 · 2026-05-22T13:55:12.309Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63f5dff3-0c1a-404c-ba14-bd6bafa8ed3b",
  "isSidechain": false,
  "promptId": "6fb152a4-c3a6-4b3c-a465-6494e24f2989",
  "type": "user",
  "isMeta": true,
  "uuid": "efd816bd-758a-4cbe-9bfe-6d762511bd49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 93 · 2026-05-22T13:55:12.309Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efd816bd-758a-4cbe-9bfe-6d762511bd49",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "e6eebd89-d0d5-4482-a20b-0daa7ff43b1c",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "id": "0af1bc80-a946-4087-abbb-d6f02fc72203",
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

_source line 94 · 2026-05-22T13:55:12.418Z_

[Reviewer 1 审稿结果]:
清理完成。审稿任务已结束。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6eebd89-d0d5-4482-a20b-0daa7ff43b1c",
  "isSidechain": false,
  "promptId": "6fb152a4-c3a6-4b3c-a465-6494e24f2989",
  "type": "user",
  "uuid": "c3f7b633-f5b5-4348-b382-53523c64e3cf",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 95_

```json
{
  "type": "ai-title",
  "aiTitle": "Review causal annotation error attribution paper",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Runtime record

_source line 96 · 2026-05-22T13:56:59.102Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T13:56:59.102Z",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "content": "[Reviewer 1 审稿意见]:\n\n## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 正文超出 8 页限制**\n与我的 N2 一致。Section 5 (Conclusion) 确实在第 9 页开始，正文约 8.3 页。ARR 对 long paper 8 页限制执行严格，这是 desk rejection 风险。无异议。\n\n**[AGREE] R2-N2: Sign reversal 实际严重性被过度声称**\n与我的 W3 部分重叠，但 R2 提出了一个我未充分强调的关键观察：论文自身在 Section 4.4 (p.8) 明确写道 *\"The primary coefficient (β₁, largest magnitude) never reverses across any empirical configuration; sign flips occur exclusively in secondary coefficients corresponding to rare categories with small |β|\"*。这与 Abstract 的 \"catastrophic\" 框架形成重大落差。\n\n补充证据：(1) 在 C_kk ≥ 0.7 的现实区间，sign reversal 仅 2.1%，且全部发生在 secondary coefficients；(2) 论文 Section 4.2 (p.5) 的 \"catastrophic sign reversal\" 小标题与 Section 4.4 的实证结果自相矛盾。\n\n不过我认为 R2 的严重性定级可以稍作调整：理论上任何系数都 CAN reverse（给定足够差的 confusion matrix），这一理论贡献本身是有价值的。建议将呈现方式从 \"catastrophic failure is the norm\" 调整为 \"sign reversal is theoretically possible for K≥3, practically rare for primary coefficients under realistic classifiers, but non-negligible for secondary coefficients\"。这比完全弱化声称更准确。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: 3/5 拓扑缺乏解析证明但用词暗示已证明**\n论文 Abstract 用 \"establish\" 描述五拓扑 sign preservation，但查看附录：\n- Confounding: Proposition 2 (Appendix A.3, p.12) — **已证明** ✓\n- Collider: Propositions 3-5 (Appendix A.6, p.14-15) — **已证明** ✓\n- Mediation: Appendix A.5 (p.13-14) — \"a closed-form proof for general K remains open\"，仅 **数值验证** ✗\n- M-bias: Appendix A.7 (p.15) — 类似，**数值验证** ✗\n- Front-door: Appendix A.7 (p.15-16) — **数值验证** ✗\n\nAbstract 的 \"establish\" 对只有 empirical verification 的 3 个拓扑而言确实 overclaim。建议改为 \"prove for confounding and collider, and verify numerically for mediation, M-bias, and front-door\"。\n\n**[AGREE, 但我认为应升级为 Must-Fix] R2-W2: Conjecture 1 支撑 ASV 但未证明**\n我在自己的审稿中将此列为 **N1 (critical)**，而 R2 列为 Should-Fix。我认为应升级。理由：\n- ASV 的 vulnerability spectrum（IV fragile → M-bias immune）的语义 *依赖* 单调性——如果 |bias| 不随 δ 单调变化，\"critical δ threshold\" 的解释就失去了理论基础\n- Table 9 (Appendix C, p.22) 显示 60-97% 的矩阵违反严格单调性，虽然幅度小 (< 0.06)，但这意味着对于相当大比例的 confusion matrices，ASV 可能给出误导性的 sensitivity ranking\n- 对于一篇以理论贡献为核心卖点的论文，其最重要的实用工具（ASV）缺乏理论保障，这比 presentation 问题更严重\n\n**[AGREE] R2-W3: Non-differential misclassification 假设讨论不足**\n与我的 W1 一致。补充：R2 指出 stress test \"仅覆盖 exposure 拓扑\"——这一点我之前漏掉了。确实，Appendix B.4 (p.20) 的 stress test 只在 exposure DAG 上做了非差异假设的敏感性分析，对其他 6 个拓扑的 differential misclassification robustness 完全缺失。对于 confounding 拓扑（LLM 误差可能与混淆因子相关），这是一个更严重的遗漏。\n\n**[AGREE] R2-W4: 缺少 outcome misclassification 的讨论**\n这是一个我未提出的有效观点。在许多 NLP 因果推断场景中，Y（结果变量）也可能由 LLM 标注（如标注\"是否包含仇恨言论\"作为结果）。Outcome misclassification 在 OLS 中通常不导致系数偏倚（仅增加方差），但在 nonlinear models（如 logistic regression）中会导致偏倚。鉴于论文已在 Limitations 中承认 nonlinear 是重要扩展方向，outcome misclassification 至少值得一段讨论。\n\n**[AGREE] R2-W5: Abstract 信息过载**\n同意。Abstract 中包含 15+ 个具体数字（83.4%, 52.6%, 13.7%, 2.1%, 47.0%, 210 configurations, 100,000 matrices, etc.），影响可读性。建议保留 3-5 个最关键的数字，其余移入正文。\n\n**[AGREE] R2-W6: 未提及代码/数据公开**\n同意。对于 reproducibility 维度，代码公开是 ARR 评审的标准预期。\n\n---\n\n### 新颖性评估\n\n**[AGREE] R2 的新颖性评估基本准确**\n补充两点：\n1. R2 说 \"ASV 创新中等（E-value 自然类比）\"——我同意 ASV 是 E-value 的自然多类扩展，但增加的是 **topology-dependent** 维度（不同拓扑的 ASV ranking 不同），这超越了简单类比。\n2. R2 说 \"FWL invariance 技术直接但实用价值高\"——我同意实用价值，但正如我在 N3 中指出的，这一结论本身缺乏 formal proof（仅有实验验证），削弱了其作为\"established result\"的可信度。\n\n---\n\n### 相关工作遗漏\n\n**[AGREE] R2-Ref1: Cinelli & Hazlett (2020) \"Making Sense of Sensitivity\"**\n这是最重要的遗漏。Cinelli & Hazlett 的 sensitivity analysis framework（robustness value, partial R²-based bounds）与 ASV 框架有直接可比性——两者都通过参数化 confounding/measurement error 的强度来评估估计量的稳健性。论文应明确讨论 ASV 与 Cinelli & Hazlett framework 的异同：ASV 针对的是 misclassification-specific 的 C(δ) 参数化，而 Cinelli & Hazlett 针对的是 omitted variable 的 partial R²。\n\n**[AGREE] R2-Ref2: Gilardi et al. (2023)**\n同意，作为 LLM annotation quality 的 seminal reference 应被引用，特别是论文 Introduction 讨论 LLM annotation 在社会科学中的应用时。\n\n**[AGREE] R2-Ref3: Ziems et al. (2024)**\n同意，作为 LLM in CSS 的综合 survey 应被引用以支撑 motivation。\n\n**[AGREE] R2-Ref4: Bound, Brown & Mathiowetz (2001)**\n同意。这与我的 W4 (novelty delineation) 相关——survey methodology 中对 categorical measurement error 的研究是 ASV 和 bias taxonomy 的重要先例。\n\n**[AGREE] R2-Ref5: Bayesian measurement error models 缺具体引用**\n论文 Section 4.5 (p.8) 提到 \"Bayesian measurement error models\" 作为 FWL bypass 方案，但未引用具体工作（如 Richardson & Gilks 1993, Gustafson 2004 的具体 Bayesian 方法章节）。\n\n---\n\n### Questions 回应\n\n**[AGREE] R2-Q1: 为何 abstract 选择 83.4% 而非 2.1%？**\n与我的 W3 和 R2-N2 一致。83.4% 来自 Dirichlet(1,1,1) 全参数空间（含随机分类器），2.1% 来自 C_kk ≥ 0.7 的现实区间。论文应以后者为主线。\n\n**[AGREE] R2-Q2: Empirical Finding 1 是否有证明进展？**\n与我的 N1 相关。3/5 拓扑的 sign preservation 和 Conjecture 1 的 monotonicity 都缺乏解析证明。\n\n**[AGREE] R2-Q3: 代码公开计划？**\n标准 reproducibility 要求。\n\n**[REBUT] R2-Q4: C(δ) 线性路径是否是唯一合理的 parameterization？**\nR2 的问题隐含质疑 C(δ) = (1-δ)I + δC₀ 的唯一性。我认为这一 parameterization 是合理且自然的，理由：\n1. 它是 identity matrix（完美分类）到目标 confusion matrix C₀ 的最短路径（在 Frobenius 范数下的线性插值）\n2. δ 有清晰的语义解释：从 0（无误差）到 1（达到 C₀ 的误差水平）\n3. 与 E-value 文献中的 sensitivity parameter 类似（单参数索引的 monotone family）\n4. 论文 Section 3.3 (p.4-5) 讨论了 non-negativity constraint（δ ≤ δ_max = min_{j,k} C₀_{jk}/(1-C₀_{jk})），说明对 boundary behavior 有考虑\n\n不过，论文确实应该讨论替代参数化（如 matrix exponential path、Dirichlet-based interpolation）及其对 ASV 值的潜在影响，即使最终选择线性路径。\n\n---\n\n### 总体评价差异\n\nR2 给出 Overall 3.5，与我的 3.5 一致。我们的主要分歧在于：\n1. **Conjecture 1 的严重性**：我列为 Must-Fix (N1)，R2 列为 Should-Fix (W2)。我坚持认为应升级——ASV 框架是论文的核心实用贡献，其理论基础不应仅依赖 numerical verification。\n2. **FWL invariance 证明**：我列为 Must-Fix (N3)，R2 未专门讨论。我认为 \"exactly 0%\" 这一定量声称需要 formal justification。\n3. **Sign reversal framing**：R2 列为 Must-Fix (N2)，我原列为 Should-Fix (W3)。R2 关于 \"primary coefficient never reverses\" 的观察让我认为这确实应升级——abstract/conclusion 的声称与实证结果之间的 gap 比我最初评估的更大。\n"
}
```

---

### Runtime record

_source line 97 · 2026-05-22T13:56:59.103Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T13:56:59.103Z",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Assistant

_source line 98 · 2026-05-22T13:56:59.091Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3f7b633-f5b5-4348-b382-53523c64e3cf",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "8f1db8f1-6f55-4d26-97ae-bbe44a3480a7",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "id": "81b49cd3-eb7c-4ae0-97a6-c45f3f47549d",
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

5 recorded events

### User

_source line 99 · 2026-05-22T13:56:59.209Z_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: 正文超出 8 页限制**
与我的 N2 一致。Section 5 (Conclusion) 确实在第 9 页开始，正文约 8.3 页。ARR 对 long paper 8 页限制执行严格，这是 desk rejection 风险。无异议。

**[AGREE] R2-N2: Sign reversal 实际严重性被过度声称**
与我的 W3 部分重叠，但 R2 提出了一个我未充分强调的关键观察：论文自身在 Section 4.4 (p.8) 明确写道 *"The primary coefficient (β₁, largest magnitude) never reverses across any empirical configuration; sign flips occur exclusively in secondary coefficients corresponding to rare categories with small |β|"*。这与 Abstract 的 "catastrophic" 框架形成重大落差。

补充证据：(1) 在 C_kk ≥ 0.7 的现实区间，sign reversal 仅 2.1%，且全部发生在 secondary coefficients；(2) 论文 Section 4.2 (p.5) 的 "catastrophic sign reversal" 小标题与 Section 4.4 的实证结果自相矛盾。

不过我认为 R2 的严重性定级可以稍作调整：理论上任何系数都 CAN reverse（给定足够差的 confusion matrix），这一理论贡献本身是有价值的。建议将呈现方式从 "catastrophic failure is the norm" 调整为 "sign reversal is theoretically possible for K≥3, practically rare for primary coefficients under realistic classifiers, but non-negligible for secondary coefficients"。这比完全弱化声称更准确。

---

### Should-Fix 问题

**[AGREE] R2-W1: 3/5 拓扑缺乏解析证明但用词暗示已证明**
论文 Abstract 用 "establish" 描述五拓扑 sign preservation，但查看附录：
- Confounding: Proposition 2 (Appendix A.3, p.12) — **已证明** ✓
- Collider: Propositions 3-5 (Appendix A.6, p.14-15) — **已证明** ✓
- Mediation: Appendix A.5 (p.13-14) — "a closed-form proof for general K remains open"，仅 **数值验证** ✗
- M-bias: Appendix A.7 (p.15) — 类似，**数值验证** ✗
- Front-door: Appendix A.7 (p.15-16) — **数值验证** ✗

Abstract 的 "establish" 对只有 empirical verification 的 3 个拓扑而言确实 overclaim。建议改为 "prove for confounding and collider, and verify numerically for mediation, M-bias, and front-door"。

**[AGREE, 但我认为应升级为 Must-Fix] R2-W2: Conjecture 1 支撑 ASV 但未证明**
我在自己的审稿中将此列为 **N1 (critical)**，而 R2 列为 Should-Fix。我认为应升级。理由：
- ASV 的 vulnerability spectrum（IV fragile → M-bias immune）的语义 *依赖* 单调性——如果 |bias| 不随 δ 单调变化，"critical δ threshold" 的解释就失去了理论基础
- Table 9 (Appendix C, p.22) 显示 60-97% 的矩阵违反严格单调性，虽然幅度小 (< 0.06)，但这意味着对于相当大比例的 confusion matrices，ASV 可能给出误导性的 sensitivity ranking
- 对于一篇以理论贡献为核心卖点的论文，其最重要的实用工具（ASV）缺乏理论保障，这比 presentation 问题更严重

**[AGREE] R2-W3: Non-differential misclassification 假设讨论不足**
与我的 W1 一致。补充：R2 指出 stress test "仅覆盖 exposure 拓扑"——这一点我之前漏掉了。确实，Appendix B.4 (p.20) 的 stress test 只在 exposure DAG 上做了非差异假设的敏感性分析，对其他 6 个拓扑的 differential misclassification robustness 完全缺失。对于 confounding 拓扑（LLM 误差可能与混淆因子相关），这是一个更严重的遗漏。

**[AGREE] R2-W4: 缺少 outcome misclassification 的讨论**
这是一个我未提出的有效观点。在许多 NLP 因果推断场景中，Y（结果变量）也可能由 LLM 标注（如标注"是否包含仇恨言论"作为结果）。Outcome misclassification 在 OLS 中通常不导致系数偏倚（仅增加方差），但在 nonlinear models（如 logistic regression）中会导致偏倚。鉴于论文已在 Limitations 中承认 nonlinear 是重要扩展方向，outcome misclassification 至少值得一段讨论。

**[AGREE] R2-W5: Abstract 信息过载**
同意。Abstract 中包含 15+ 个具体数字（83.4%, 52.6%, 13.7%, 2.1%, 47.0%, 210 configurations, 100,000 matrices, etc.），影响可读性。建议保留 3-5 个最关键的数字，其余移入正文。

**[AGREE] R2-W6: 未提及代码/数据公开**
同意。对于 reproducibility 维度，代码公开是 ARR 评审的标准预期。

---

### 新颖性评估

**[AGREE] R2 的新颖性评估基本准确**
补充两点：
1. R2 说 "ASV 创新中等（E-value 自然类比）"——我同意 ASV 是 E-value 的自然多类扩展，但增加的是 **topology-dependent** 维度（不同拓扑的 ASV ranking 不同），这超越了简单类比。
2. R2 说 "FWL invariance 技术直接但实用价值高"——我同意实用价值，但正如我在 N3 中指出的，这一结论本身缺乏 formal proof（仅有实验验证），削弱了其作为"established result"的可信度。

---

### 相关工作遗漏

**[AGREE] R2-Ref1: Cinelli & Hazlett (2020) "Making Sense of Sensitivity"**
这是最重要的遗漏。Cinelli & Hazlett 的 sensitivity analysis framework（robustness value, partial R²-based bounds）与 ASV 框架有直接可比性——两者都通过参数化 confounding/measurement error 的强度来评估估计量的稳健性。论文应明确讨论 ASV 与 Cinelli & Hazlett framework 的异同：ASV 针对的是 misclassification-specific 的 C(δ) 参数化，而 Cinelli & Hazlett 针对的是 omitted variable 的 partial R²。

**[AGREE] R2-Ref2: Gilardi et al. (2023)**
同意，作为 LLM annotation quality 的 seminal reference 应被引用，特别是论文 Introduction 讨论 LLM annotation 在社会科学中的应用时。

**[AGREE] R2-Ref3: Ziems et al. (2024)**
同意，作为 LLM in CSS 的综合 survey 应被引用以支撑 motivation。

**[AGREE] R2-Ref4: Bound, Brown & Mathiowetz (2001)**
同意。这与我的 W4 (novelty delineation) 相关——survey methodology 中对 categorical measurement error 的研究是 ASV 和 bias taxonomy 的重要先例。

**[AGREE] R2-Ref5: Bayesian measurement error models 缺具体引用**
论文 Section 4.5 (p.8) 提到 "Bayesian measurement error models" 作为 FWL bypass 方案，但未引用具体工作（如 Richardson & Gilks 1993, Gustafson 2004 的具体 Bayesian 方法章节）。

---

### Questions 回应

**[AGREE] R2-Q1: 为何 abstract 选择 83.4% 而非 2.1%？**
与我的 W3 和 R2-N2 一致。83.4% 来自 Dirichlet(1,1,1) 全参数空间（含随机分类器），2.1% 来自 C_kk ≥ 0.7 的现实区间。论文应以后者为主线。

**[AGREE] R2-Q2: Empirical Finding 1 是否有证明进展？**
与我的 N1 相关。3/5 拓扑的 sign preservation 和 Conjecture 1 的 monotonicity 都缺乏解析证明。

**[AGREE] R2-Q3: 代码公开计划？**
标准 reproducibility 要求。

**[REBUT] R2-Q4: C(δ) 线性路径是否是唯一合理的 parameterization？**
R2 的问题隐含质疑 C(δ) = (1-δ)I + δC₀ 的唯一性。我认为这一 parameterization 是合理且自然的，理由：
1. 它是 identity matrix（完美分类）到目标 confusion matrix C₀ 的最短路径（在 Frobenius 范数下的线性插值）
2. δ 有清晰的语义解释：从 0（无误差）到 1（达到 C₀ 的误差水平）
3. 与 E-value 文献中的 sensitivity parameter 类似（单参数索引的 monotone family）
4. 论文 Section 3.3 (p.4-5) 讨论了 non-negativity constraint（δ ≤ δ_max = min_{j,k} C₀_{jk}/(1-C₀_{jk})），说明对 boundary behavior 有考虑

不过，论文确实应该讨论替代参数化（如 matrix exponential path、Dirichlet-based interpolation）及其对 ASV 值的潜在影响，即使最终选择线性路径。

---

### 总体评价差异

R2 给出 Overall 3.5，与我的 3.5 一致。我们的主要分歧在于：
1. **Conjecture 1 的严重性**：我列为 Must-Fix (N1)，R2 列为 Should-Fix (W2)。我坚持认为应升级——ASV 框架是论文的核心实用贡献，其理论基础不应仅依赖 numerical verification。
2. **FWL invariance 证明**：我列为 Must-Fix (N3)，R2 未专门讨论。我认为 "exactly 0%" 这一定量声称需要 formal justification。
3. **Sign reversal framing**：R2 列为 Must-Fix (N2)，我原列为 Should-Fix (W3)。R2 关于 "primary coefficient never reverses" 的观察让我认为这确实应升级——abstract/conclusion 的声称与实证结果之间的 gap 比我最初评估的更大。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f1db8f1-6f55-4d26-97ae-bbe44a3480a7",
  "isSidechain": false,
  "promptId": "d029e2df-210e-40c5-a131-2a5ac992fd3d",
  "type": "user",
  "uuid": "f4eadd66-ab9d-4b56-9fce-ce2f1dd9a1a6",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 100_

```json
{
  "type": "ai-title",
  "aiTitle": "Review causal annotation error attribution paper",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Runtime record

_source line 101 · 2026-05-22T13:57:15.399Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T13:57:15.399Z",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "content": "[Reviewer 1 审稿结果]:\n交叉回应已提交。\n\n核心结论：与 R2 在大多数问题上达成一致（12 个 AGREE，1 个 REBUT），主要分歧在于严重性定级：\n- 我认为 **Conjecture 1 (R2-W2) 应升级为 Must-Fix**——ASV 框架的理论基础不应仅依赖 numerical verification\n- 我认为 **FWL invariance 缺乏 formal proof** 是 R2 未充分讨论的 Must-Fix 问题\n- R2 关于 \"primary coefficient never reverses\" 的观察让我同意将 **sign reversal framing 升级为 Must-Fix**\n- 唯一 REBUT：C(δ) 线性参数化是合理的自然选择，但应讨论替代方案"
}
```

---

### Runtime record

_source line 102 · 2026-05-22T13:57:15.399Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T13:57:15.399Z",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Assistant

_source line 103 · 2026-05-22T13:57:15.388Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4eadd66-ab9d-4b56-9fce-ce2f1dd9a1a6",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "5aaadf15-1b01-44b9-bcf8-f51230fbbdef",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "id": "0669a24a-32fc-4291-99e5-66a87cf17822",
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

## Round 9

5 recorded events

### User

_source line 104 · 2026-05-22T13:57:15.507Z_

[Reviewer 1 审稿结果]:
交叉回应已提交。

核心结论：与 R2 在大多数问题上达成一致（12 个 AGREE，1 个 REBUT），主要分歧在于严重性定级：
- 我认为 **Conjecture 1 (R2-W2) 应升级为 Must-Fix**——ASV 框架的理论基础不应仅依赖 numerical verification
- 我认为 **FWL invariance 缺乏 formal proof** 是 R2 未充分讨论的 Must-Fix 问题
- R2 关于 "primary coefficient never reverses" 的观察让我同意将 **sign reversal framing 升级为 Must-Fix**
- 唯一 REBUT：C(δ) 线性参数化是合理的自然选择，但应讨论替代方案

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5aaadf15-1b01-44b9-bcf8-f51230fbbdef",
  "isSidechain": false,
  "promptId": "c7bc2ad6-6b7f-4ae8-8be3-b5126e39eae9",
  "type": "user",
  "uuid": "07b51e30-c72e-4ad9-8168-0b8641867dd7",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 105_

```json
{
  "type": "ai-title",
  "aiTitle": "Review causal annotation error attribution paper",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Runtime record

_source line 106 · 2026-05-22T13:57:31.925Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T13:57:31.925Z",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "content": "[Reviewer 2 审稿意见]:\n## Reviewer 2 交叉回应 — 逐条回应 Reviewer 1 审稿意见\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: Theorem 1 适用范围过窄，Conjecture 1 缺乏证明**\n\n同意这是一个实质性问题。我在自己的审稿中将其列为 W2（should-fix），但 R1 将其提升到 critical 也有道理。具体而言：\n\n- Theorem 1 限于 confounding + proportional effects（Section 3.3），这是一个很强的假设。\n- Conjecture 1 的数值验证虽然覆盖广（10,000 矩阵 × 7 拓扑 × K∈{3,5,7}），但 ε < 0.06 是 empirical bound，不是 formal bound。\n- R1 指出 Table 9 显示 60-97% 的随机矩阵违反严格单调性——这个数字我在审稿中未单独指出，但它确实让\"monotonicity\"这个词的使用变得微妙。论文用了\"ε-approximate monotonicity\"来 hedge，但如果多数矩阵都违反严格单调性，\"ASV 单调递增/递减\"的直觉描述就不准确。\n\n不过我对严重性的评估略低于 R1：ASV 的核心价值在于 **ranking topologies**（IV 最脆弱、M-bias 最安全），这个排序在所有数值实验中都成立，不完全依赖严格单调性。即使 ε-approximate，只要 ε 足够小（< 6%），排序结论不受影响。因此我维持 should-fix 而非 must-fix 的评级，但建议作者：(1) 在正文中更诚实地讨论\"多数矩阵违反严格单调\"这一事实；(2) 至少再证明 mediation 的单调性（其 bias 表达式 Eq.3 结构较简单）。\n\n---\n\n**[AGREE] R1-N2: 正文超出 8 页限制**\n\n完全同意。我也将此列为 N1（critical）。Section 5 (Conclusion) 在第 9 页，正文约超 0.5 页。这是 ARR desk rejection 风险。\n\n---\n\n**[REBUT] R1-N3: FWL invariance 结论缺乏严格证明**\n\n我部分不同意 R1 将此列为 critical。逐点回应：\n\n**(a) \"matrix-based correction\"的精确定义**：R1 的要求合理。论文确实未给出 formal definition。但从 Section 4.5 和 Appendix 的上下文可以推断，\"matrix-based correction\"指的是对 dummy 变量施加 C⁻¹ 变换（naive plug-in 和 MLA 都属此类）。建议作者添加一个 precise definition，但这属于 writing clarity 问题，不影响结论正确性。\n\n**(b) SIMEX 的 0% reduction 问题**：R1 质疑\"SIMEX 理论上应能工作\"。但我认为恰恰相反——SIMEX 对 covariate misclassification 的 0% reduction 正是 FWL invariance 的正确推论。SIMEX 通过向 A* 添加额外噪声再外推回去，但 FWL 定理保证了 T 的系数不受 A* column space 内任何变换的影响。因此 SIMEX 的 measurement error function 是常数函数——外推结果等于原始估计。这不是实现问题，而是 FWL 的必然结果。论文可以更清楚地解释这一点。\n\n**(c) 与已知 \"residual confounding\" 结果的关系**：R1 问的是 \"controlling for mismeasured confounder leaves residual confounding\" 这一已知事实和 FWL invariance 的关系。这两者是互补而非矛盾的：(i) residual confounding 说的是 bias 的存在（T coefficient 有偏），这在论文的 Eq.1 confounding bias 表达式中已体现；(ii) FWL invariance 说的是 correction 的无效性——即使你知道真实 C，施加 C⁻¹ 也不能消除 T 的 bias，因为 bias 来自 T 与 A residual 的相关性而非 A 的编码方式。这个区分（bias 存在 vs. 校正无效）是论文的实质贡献，虽然技术上直接但在文献中确实被忽视。\n\n**我的评估**：FWL invariance 的结论是正确的且可从 FWL 定理直接推出，不需要额外 formal proof——它本身就是 FWL 定理的 corollary。R1 要求\"严格证明\"的合理性在于论文表述不够 precise，但这是 writing issue 不是 correctness issue。我将此从 R1 的 critical 降为 should-fix：建议添加 precise definition + 一段 FWL 推导（3-4 行公式），但不认为这影响接收决定。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Non-differential 假设对 LLM 不成立**\n\n同意。我在 W3 中提出了完全相同的关切。LLM 处理包含 Y 和 Z 信息的文本，P(A*|A,Y,Z) = P(A*|A) 在许多场景中不成立。Appendix B.4 的 stress test 仅测 ε≤0.10 且主要覆盖 exposure 拓扑，不足以支撑框架的一般性声称。\n\n---\n\n**[AGREE] R1-W2: 线性 SEM 假设限制适用性**\n\n同意且认为 R1 指出了一个我在审稿中未充分强调的具体后果：**Algorithm 1 的分流建议可能在 logistic 模型下失效**。论文 Appendix B.3 的 logistic DGP 检验显示 sign-flip patterns 保持，但 FWL invariance 本身在非线性模型下不成立——这意味着 Algorithm 1 中\"topology ∈ {confounding, mediation, collider, M-bias} → matrix-based correction ineffective\"的分支在 logistic regression 中可能不正确。论文在 Limitations 中提到了这一点（\"FWL invariance result does not hold for logistic regression\"），但 Algorithm 1 本身没有加此 caveat。这是一个有实际影响的问题。\n\n---\n\n**[AGREE] R1-W3: Dirichlet(1,1,1) headline 数字误导性**\n\n强烈同意。这与我的 N2 (critical) 一致。我甚至将其严重性评估高于 R1（R1 列为 W3 should-fix，我列为 N2 must-fix）。83.4% 在 abstract 第一段出现，但这是 Dirichlet(1,1,1) 均匀先验的结果——realistic regime（diagonal ≥ 0.7）下 sign reversal 仅 2.1%。更重要的是，empirical validation 显示 sign reversal 仅影响 secondary coefficients（Section 4.4）。Abstract 和 Introduction 的\"catastrophic\"框架与实际 severity 的落差是 overclaiming 问题。\n\n---\n\n**[PARTIALLY AGREE] R1-W4: 新颖性定位不清**\n\n部分同意。R1 要求更清晰地界定\"已知结果在 LLM 语境的应用 vs 真正新贡献\"，这个要求合理。具体而言：\n\n- **已知**：K≥3 polytomous misclassification 可导致 sign reversal（Dosemeci 1990, Veierød & Laake 2001）；non-differential misclassification of binary confounder 的 attenuation 性质（Brenner 1993, Ogburn & VanderWeele 2012）\n- **新贡献**：(1) 系统性 7 拓扑对比（从未有人在统一框架下比较）；(2) ASV 框架（E-value 类比应用于 annotation error 是新的）；(3) FWL invariance 对 correction methods 的影响（文献中从未被指出）；(4) 在 NLP/LLM annotation 语境中的实证验证\n\n但我不认为这构成 rejection 理由。论文在 Related Work（Section 2）中已经 cite 了 Dosemeci (1990) 和 Veierød & Laake (2001)，并明确说\"our taxonomy is the first to characterize how the same confusion matrix produces qualitatively different bias across seven topologies\"。问题是 **程度**——论文应更明确地用一两句话说\"K≥3 sign reversal possibility 本身是已知的（Dosemeci 1990），我们的新贡献是 topology-dependent 的系统刻画\"。这是 framing 改进而非 novelty 不足。\n\n---\n\n**[PARTIALLY AGREE] R1-W5: 经验验证用模拟 DGP 而非真实因果数据**\n\nR1 的批评技术上正确但我认为过于严苛。理由如下：\n\n1. **这是方法论论文的标准做法**。验证理论框架需要 known ground truth，只有模拟 DGP 能提供。E-value 原始论文（VanderWeele & Ding 2017）、PPI++（Angelopoulos et al. 2023）等方法论工作也采用类似策略。\n2. **论文用了 real LLM confusion matrices**。这比纯模拟高一个层次——confusion matrices 来自 4 个真实 LLM 在 3 个真实数据集上的表现（HumAID, VAST, CivilComments），不是 fabricated 的。\n3. **Appendix B.2 有 retrospective case study**。虽然在附录，但确实应用了框架到 Lee & Wood-Doughty (2024) 的真实因果分析。\n\n但我也同意 R1 的核心关切：论文的 practical guidance value 没有被充分验证。如果作者能在 camera-ready 中加入一个更完整的 real-world case study（如在 HumAID 数据上执行完整因果分析并展示 ASV 如何改变分析决策），说服力会大幅提升。\n\n---\n\n### 主要优势\n\n**[AGREE] 所有 6 条优势**\n\nR1 列出的优势与我的评估高度一致：\n- \"重要且及时的问题\" — 同意，LLM annotation 在 CL/NLP 社区快速普及，downstream causal validity 是紧迫问题。\n- \"K≥3 algebraic break point\" — 同意，这是论文最核心的 insight。\n- \"Algorithm 1 + ASV 框架的实用性\" — 同意，可操作性是论文的主要卖点。\n- \"7 DAG × 5 correction methods 的系统覆盖\" — 同意，覆盖面是竞争优势。\n- \"附录质量高\" — 同意，12 页附录包含详细证明、stress test、case study，质量高于多数投稿。\n- \"Cross-PPI 和 FWL bypass 方法讨论\" — 同意，Section 4.5 最后一段的 Cross-PPI 和 EM imputation 讨论虽然只是提及未评估，但展示了对 correction 方向的全面思考。\n\n---\n\n### 小问题\n\n**[AGREE] τ 和 β_T 记号交替使用**\n确认存在。Section 3.2 用 τ 表示 target causal parameter，但 exposure 部分用 β_j，confounding 部分用 τ（T 的系数）。虽然语义可从上下文推断，但 notation 一致性应改进。\n\n**[AGREE] Proposition 编号在正文与附录不一致**\n未独立验证此问题，但如果存在，应在 camera-ready 修复。\n\n**[AGREE] Figure 2 y 轴标签较小**\n同意。我在小问题中也提到了 Figure 2 标签文字在打印版中可能难以辨认。\n\n**[AGREE] Table 2 conditions 列风格不一致**\n未独立验证（Table 2 在 Appendix A.9），但 R1 对附录阅读的仔细程度值得肯定。\n\n---\n\n### 对 Director 提出的三个具体问题的回应\n\n**Q1: FWL invariance 严重性评估是否一致？**\n\n不完全一致，但分歧不大。R1 将 FWL invariance 列为 N3 (critical)，要求 formal proof；我在审稿中将其列为优势（\"技术上直接但实践重要\"）。核心分歧在于：**R1 认为 FWL invariance 需要被 prove**，而我认为它是 FWL 定理的 direct corollary，不需要额外证明——需要改进的是 **表述精度**而非 **证明**。\n\n具体来说：FWL 定理说 OLS 中 T 的系数等于对 T 和 Y 分别投影掉 A* dummies 后的简单回归系数。对 A* dummies 施加 C⁻¹ 变换不改变其 column space（C⁻¹ 可逆），因此 projection matrix M_{A*} 不变，T 系数不变。这个推导不到 3 行。论文应该把这 3 行写出来，但说它\"缺乏严格证明\"我认为过度了。\n\n我建议将此定性为 **should-fix (writing clarity)**，而非 **must-fix (missing proof)**。\n\n**Q2: 如何看待 R1-W5（模拟 DGP 而非真实因果数据）？**\n\n如上所述，我认为这是有效但不严重的批评。方法论论文用模拟 DGP + real parameters 是标准做法。论文的贡献在于理论框架，不在于某个具体因果分析。但我同意 R1 的建议方向——一个完整的 real-world case study 会大幅增强论文说服力，建议在 camera-ready 中将 Appendix B.2 的 case study 扩展并移入正文（如果页数允许）。\n\n**Q3: R1-W4（新颖性定位）与我的新颖性评估是否矛盾？**\n\n不矛盾，高度一致。R1 说\"新颖性定位不清\"，我在新颖性专项评估中说\"ASV 相对于 E-values 的技术创新中等\"、\"K≥3 break 已被 Dosemeci (1990) 指出\"。我们都认为：\n- 论文的系统性 7 拓扑对比是 **genuinely new**\n- K≥3 sign reversal 本身是 **known but under-explored**\n- ASV 是 E-value 的 **natural adaptation**，不是 breakthrough\n\n差异在于表述：R1 要求论文更明确界定已知 vs 新，我在审稿中已经做了这个区分。建议作者在 Introduction 最后一段添加 1-2 句：\"The possibility of polytomous sign reversal was noted by Dosemeci et al. (1990); our contribution is the first systematic characterization across multiple DAG topologies and the ASV framework for quantifying this vulnerability.\"\n\n---\n\n### 综合评估\n\n两位 reviewer 的评估高度一致：\n\n| 维度 | R1 | R2（我） | 共识 |\n|------|----|----|------|\n| Overall | 3.5 | 3.5 | 一致 |\n| 页数超限 | N2 critical | N1 critical | 一致 |\n| Conjecture 1 未证明 | N1 critical | W2 warning | R1 更严格，但方向一致 |\n| 83.4% overclaiming | W3 warning | N2 critical | 我更严格 |\n| Non-differential 假设 | W1 warning | W3 warning | 一致 |\n| FWL invariance | N3 critical | 列为优势 | 分歧最大——我认为 should-fix writing 即可 |\n| 模拟 DGP | W5 warning | 未单独列出 | R1 更关注，我认为 acceptable |\n\n**两位 reviewer 的核心共识**：这是一篇重要且及时的工作，系统性 taxonomy 和 ASV 框架有实用价值，但 (1) 理论深度中等（Conjecture 未证明、部分 sign preservation 仅数值验证），(2) framing 存在 overclaiming，(3) 格式需修复。Borderline Conference 的评分反映了贡献与不足的平衡。"
}
```

---

### Runtime record

_source line 107 · 2026-05-22T13:57:31.926Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T13:57:31.926Z",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Assistant

_source line 108 · 2026-05-22T13:57:31.913Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07b51e30-c72e-4ad9-8168-0b8641867dd7",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "949a55ed-98a3-4510-a05e-37aae69ad518",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "id": "854464c0-5142-46e6-8880-46dda1e1e892",
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

## Round 10

29 recorded events

### User

_source line 109 · 2026-05-22T13:57:32.037Z_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 逐条回应 Reviewer 1 审稿意见

---

### Must-Fix 问题

**[AGREE] R1-N1: Theorem 1 适用范围过窄，Conjecture 1 缺乏证明**

同意这是一个实质性问题。我在自己的审稿中将其列为 W2（should-fix），但 R1 将其提升到 critical 也有道理。具体而言：

- Theorem 1 限于 confounding + proportional effects（Section 3.3），这是一个很强的假设。
- Conjecture 1 的数值验证虽然覆盖广（10,000 矩阵 × 7 拓扑 × K∈{3,5,7}），但 ε < 0.06 是 empirical bound，不是 formal bound。
- R1 指出 Table 9 显示 60-97% 的随机矩阵违反严格单调性——这个数字我在审稿中未单独指出，但它确实让"monotonicity"这个词的使用变得微妙。论文用了"ε-approximate monotonicity"来 hedge，但如果多数矩阵都违反严格单调性，"ASV 单调递增/递减"的直觉描述就不准确。

不过我对严重性的评估略低于 R1：ASV 的核心价值在于 **ranking topologies**（IV 最脆弱、M-bias 最安全），这个排序在所有数值实验中都成立，不完全依赖严格单调性。即使 ε-approximate，只要 ε 足够小（< 6%），排序结论不受影响。因此我维持 should-fix 而非 must-fix 的评级，但建议作者：(1) 在正文中更诚实地讨论"多数矩阵违反严格单调"这一事实；(2) 至少再证明 mediation 的单调性（其 bias 表达式 Eq.3 结构较简单）。

---

**[AGREE] R1-N2: 正文超出 8 页限制**

完全同意。我也将此列为 N1（critical）。Section 5 (Conclusion) 在第 9 页，正文约超 0.5 页。这是 ARR desk rejection 风险。

---

**[REBUT] R1-N3: FWL invariance 结论缺乏严格证明**

我部分不同意 R1 将此列为 critical。逐点回应：

**(a) "matrix-based correction"的精确定义**：R1 的要求合理。论文确实未给出 formal definition。但从 Section 4.5 和 Appendix 的上下文可以推断，"matrix-based correction"指的是对 dummy 变量施加 C⁻¹ 变换（naive plug-in 和 MLA 都属此类）。建议作者添加一个 precise definition，但这属于 writing clarity 问题，不影响结论正确性。

**(b) SIMEX 的 0% reduction 问题**：R1 质疑"SIMEX 理论上应能工作"。但我认为恰恰相反——SIMEX 对 covariate misclassification 的 0% reduction 正是 FWL invariance 的正确推论。SIMEX 通过向 A* 添加额外噪声再外推回去，但 FWL 定理保证了 T 的系数不受 A* column space 内任何变换的影响。因此 SIMEX 的 measurement error function 是常数函数——外推结果等于原始估计。这不是实现问题，而是 FWL 的必然结果。论文可以更清楚地解释这一点。

**(c) 与已知 "residual confounding" 结果的关系**：R1 问的是 "controlling for mismeasured confounder leaves residual confounding" 这一已知事实和 FWL invariance 的关系。这两者是互补而非矛盾的：(i) residual confounding 说的是 bias 的存在（T coefficient 有偏），这在论文的 Eq.1 confounding bias 表达式中已体现；(ii) FWL invariance 说的是 correction 的无效性——即使你知道真实 C，施加 C⁻¹ 也不能消除 T 的 bias，因为 bias 来自 T 与 A residual 的相关性而非 A 的编码方式。这个区分（bias 存在 vs. 校正无效）是论文的实质贡献，虽然技术上直接但在文献中确实被忽视。

**我的评估**：FWL invariance 的结论是正确的且可从 FWL 定理直接推出，不需要额外 formal proof——它本身就是 FWL 定理的 corollary。R1 要求"严格证明"的合理性在于论文表述不够 precise，但这是 writing issue 不是 correctness issue。我将此从 R1 的 critical 降为 should-fix：建议添加 precise definition + 一段 FWL 推导（3-4 行公式），但不认为这影响接收决定。

---

### Should-Fix 问题

**[AGREE] R1-W1: Non-differential 假设对 LLM 不成立**

同意。我在 W3 中提出了完全相同的关切。LLM 处理包含 Y 和 Z 信息的文本，P(A*|A,Y,Z) = P(A*|A) 在许多场景中不成立。Appendix B.4 的 stress test 仅测 ε≤0.10 且主要覆盖 exposure 拓扑，不足以支撑框架的一般性声称。

---

**[AGREE] R1-W2: 线性 SEM 假设限制适用性**

同意且认为 R1 指出了一个我在审稿中未充分强调的具体后果：**Algorithm 1 的分流建议可能在 logistic 模型下失效**。论文 Appendix B.3 的 logistic DGP 检验显示 sign-flip patterns 保持，但 FWL invariance 本身在非线性模型下不成立——这意味着 Algorithm 1 中"topology ∈ {confounding, mediation, collider, M-bias} → matrix-based correction ineffective"的分支在 logistic regression 中可能不正确。论文在 Limitations 中提到了这一点（"FWL invariance result does not hold for logistic regression"），但 Algorithm 1 本身没有加此 caveat。这是一个有实际影响的问题。

---

**[AGREE] R1-W3: Dirichlet(1,1,1) headline 数字误导性**

强烈同意。这与我的 N2 (critical) 一致。我甚至将其严重性评估高于 R1（R1 列为 W3 should-fix，我列为 N2 must-fix）。83.4% 在 abstract 第一段出现，但这是 Dirichlet(1,1,1) 均匀先验的结果——realistic regime（diagonal ≥ 0.7）下 sign reversal 仅 2.1%。更重要的是，empirical validation 显示 sign reversal 仅影响 secondary coefficients（Section 4.4）。Abstract 和 Introduction 的"catastrophic"框架与实际 severity 的落差是 overclaiming 问题。

---

**[PARTIALLY AGREE] R1-W4: 新颖性定位不清**

部分同意。R1 要求更清晰地界定"已知结果在 LLM 语境的应用 vs 真正新贡献"，这个要求合理。具体而言：

- **已知**：K≥3 polytomous misclassification 可导致 sign reversal（Dosemeci 1990, Veierød & Laake 2001）；non-differential misclassification of binary confounder 的 attenuation 性质（Brenner 1993, Ogburn & VanderWeele 2012）
- **新贡献**：(1) 系统性 7 拓扑对比（从未有人在统一框架下比较）；(2) ASV 框架（E-value 类比应用于 annotation error 是新的）；(3) FWL invariance 对 correction methods 的影响（文献中从未被指出）；(4) 在 NLP/LLM annotation 语境中的实证验证

但我不认为这构成 rejection 理由。论文在 Related Work（Section 2）中已经 cite 了 Dosemeci (1990) 和 Veierød & Laake (2001)，并明确说"our taxonomy is the first to characterize how the same confusion matrix produces qualitatively different bias across seven topologies"。问题是 **程度**——论文应更明确地用一两句话说"K≥3 sign reversal possibility 本身是已知的（Dosemeci 1990），我们的新贡献是 topology-dependent 的系统刻画"。这是 framing 改进而非 novelty 不足。

---

**[PARTIALLY AGREE] R1-W5: 经验验证用模拟 DGP 而非真实因果数据**

R1 的批评技术上正确但我认为过于严苛。理由如下：

1. **这是方法论论文的标准做法**。验证理论框架需要 known ground truth，只有模拟 DGP 能提供。E-value 原始论文（VanderWeele & Ding 2017）、PPI++（Angelopoulos et al. 2023）等方法论工作也采用类似策略。
2. **论文用了 real LLM confusion matrices**。这比纯模拟高一个层次——confusion matrices 来自 4 个真实 LLM 在 3 个真实数据集上的表现（HumAID, VAST, CivilComments），不是 fabricated 的。
3. **Appendix B.2 有 retrospective case study**。虽然在附录，但确实应用了框架到 Lee & Wood-Doughty (2024) 的真实因果分析。

但我也同意 R1 的核心关切：论文的 practical guidance value 没有被充分验证。如果作者能在 camera-ready 中加入一个更完整的 real-world case study（如在 HumAID 数据上执行完整因果分析并展示 ASV 如何改变分析决策），说服力会大幅提升。

---

### 主要优势

**[AGREE] 所有 6 条优势**

R1 列出的优势与我的评估高度一致：
- "重要且及时的问题" — 同意，LLM annotation 在 CL/NLP 社区快速普及，downstream causal validity 是紧迫问题。
- "K≥3 algebraic break point" — 同意，这是论文最核心的 insight。
- "Algorithm 1 + ASV 框架的实用性" — 同意，可操作性是论文的主要卖点。
- "7 DAG × 5 correction methods 的系统覆盖" — 同意，覆盖面是竞争优势。
- "附录质量高" — 同意，12 页附录包含详细证明、stress test、case study，质量高于多数投稿。
- "Cross-PPI 和 FWL bypass 方法讨论" — 同意，Section 4.5 最后一段的 Cross-PPI 和 EM imputation 讨论虽然只是提及未评估，但展示了对 correction 方向的全面思考。

---

### 小问题

**[AGREE] τ 和 β_T 记号交替使用**
确认存在。Section 3.2 用 τ 表示 target causal parameter，但 exposure 部分用 β_j，confounding 部分用 τ（T 的系数）。虽然语义可从上下文推断，但 notation 一致性应改进。

**[AGREE] Proposition 编号在正文与附录不一致**
未独立验证此问题，但如果存在，应在 camera-ready 修复。

**[AGREE] Figure 2 y 轴标签较小**
同意。我在小问题中也提到了 Figure 2 标签文字在打印版中可能难以辨认。

**[AGREE] Table 2 conditions 列风格不一致**
未独立验证（Table 2 在 Appendix A.9），但 R1 对附录阅读的仔细程度值得肯定。

---

### 对 Director 提出的三个具体问题的回应

**Q1: FWL invariance 严重性评估是否一致？**

不完全一致，但分歧不大。R1 将 FWL invariance 列为 N3 (critical)，要求 formal proof；我在审稿中将其列为优势（"技术上直接但实践重要"）。核心分歧在于：**R1 认为 FWL invariance 需要被 prove**，而我认为它是 FWL 定理的 direct corollary，不需要额外证明——需要改进的是 **表述精度**而非 **证明**。

具体来说：FWL 定理说 OLS 中 T 的系数等于对 T 和 Y 分别投影掉 A* dummies 后的简单回归系数。对 A* dummies 施加 C⁻¹ 变换不改变其 column space（C⁻¹ 可逆），因此 projection matrix M_{A*} 不变，T 系数不变。这个推导不到 3 行。论文应该把这 3 行写出来，但说它"缺乏严格证明"我认为过度了。

我建议将此定性为 **should-fix (writing clarity)**，而非 **must-fix (missing proof)**。

**Q2: 如何看待 R1-W5（模拟 DGP 而非真实因果数据）？**

如上所述，我认为这是有效但不严重的批评。方法论论文用模拟 DGP + real parameters 是标准做法。论文的贡献在于理论框架，不在于某个具体因果分析。但我同意 R1 的建议方向——一个完整的 real-world case study 会大幅增强论文说服力，建议在 camera-ready 中将 Appendix B.2 的 case study 扩展并移入正文（如果页数允许）。

**Q3: R1-W4（新颖性定位）与我的新颖性评估是否矛盾？**

不矛盾，高度一致。R1 说"新颖性定位不清"，我在新颖性专项评估中说"ASV 相对于 E-values 的技术创新中等"、"K≥3 break 已被 Dosemeci (1990) 指出"。我们都认为：
- 论文的系统性 7 拓扑对比是 **genuinely new**
- K≥3 sign reversal 本身是 **known but under-explored**
- ASV 是 E-value 的 **natural adaptation**，不是 breakthrough

差异在于表述：R1 要求论文更明确界定已知 vs 新，我在审稿中已经做了这个区分。建议作者在 Introduction 最后一段添加 1-2 句："The possibility of polytomous sign reversal was noted by Dosemeci et al. (1990); our contribution is the first systematic characterization across multiple DAG topologies and the ASV framework for quantifying this vulnerability."

---

### 综合评估

两位 reviewer 的评估高度一致：

| 维度 | R1 | R2（我） | 共识 |
|------|----|----|------|
| Overall | 3.5 | 3.5 | 一致 |
| 页数超限 | N2 critical | N1 critical | 一致 |
| Conjecture 1 未证明 | N1 critical | W2 warning | R1 更严格，但方向一致 |
| 83.4% overclaiming | W3 warning | N2 critical | 我更严格 |
| Non-differential 假设 | W1 warning | W3 warning | 一致 |
| FWL invariance | N3 critical | 列为优势 | 分歧最大——我认为 should-fix writing 即可 |
| 模拟 DGP | W5 warning | 未单独列出 | R1 更关注，我认为 acceptable |

**两位 reviewer 的核心共识**：这是一篇重要且及时的工作，系统性 taxonomy 和 ASV 框架有实用价值，但 (1) 理论深度中等（Conjecture 未证明、部分 sign preservation 仅数值验证），(2) framing 存在 overclaiming，(3) 格式需修复。Borderline Conference 的评分反映了贡献与不足的平衡。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "949a55ed-98a3-4510-a05e-37aae69ad518",
  "isSidechain": false,
  "promptId": "35007fc4-a558-4c2b-a533-ce1f9088b4a3",
  "type": "user",
  "uuid": "58cdf0d8-72ba-42a4-9626-99510d71f643",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 110 · 2026-05-22T13:57:32.036Z_

```json
{
  "parentUuid": "58cdf0d8-72ba-42a4-9626-99510d71f643",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f6d4a055-87cf-4c47-a9e1-dcc2b1f32621",
  "timestamp": "2026-05-22T13:57:32.036Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 111 · 2026-05-22T13:57:48.264Z_

<details><summary>Logged reasoning block</summary>

```text
Both Reviewers have completed their cross-responses. Let me analyze the convergence:

**Convergence achieved:**
- Both reviewers agree on Overall 3.5 (Borderline Conference)
- Both agree on page limit issue (critical)
- Both agree on overclaiming of 83.4% sign reversal (both think it's important, R2 rates it critical, R1 upgraded to agree)
- Both agree on non-differential assumption concern
- Both agree on all 6 strengths
- Both agree on most should-fix items


- Three key disagreements remain on severity levels: whether Conjecture 1's monotonicity requirement is truly critical versus a technical concern that doesn't undermine the ASV ranking, whether the FWL invariance proof is a missing proof or just needs clarification as a direct corollary, and how important the simulated DGP validation is.

Now I'm moving to synthesize everything by checking the existing review issues file, confirming the visual check and external review status, and pulling together the final report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6d4a055-87cf-4c47-a9e1-dcc2b1f32621",
  "isSidechain": false,
  "requestId": "req_011CbHiyZUkeydr87qaPbzpi",
  "type": "assistant",
  "uuid": "2fbf1c09-9ea4-4448-ac2c-06ae113f3af5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WqoLVCt61ov4ydaW7xwrTW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4989,
      "cache_read_input_tokens": 100999,
      "output_tokens": 702,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4989,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 702,
          "cache_read_input_tokens": 100999,
          "cache_creation_input_tokens": 4989,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4989
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

_source line 112 · 2026-05-22T13:57:50.289Z_

Reviewer 2 交叉回应已收到。两位 Reviewer 的意见高度收敛（12+ AGREE），分歧明确且已充分论证。关键共识已达成，无需进入第 2 轮。进入 **Step 4：合成报告**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fbf1c09-9ea4-4448-ac2c-06ae113f3af5",
  "isSidechain": false,
  "requestId": "req_011CbHiyZUkeydr87qaPbzpi",
  "type": "assistant",
  "uuid": "3888f02e-894e-470b-bc9f-c6980bd54e83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WqoLVCt61ov4ydaW7xwrTW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4989,
      "cache_read_input_tokens": 100999,
      "output_tokens": 702,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4989,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 702,
          "cache_read_input_tokens": 100999,
          "cache_creation_input_tokens": 4989,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4989
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

_source line 113 · 2026-05-22T13:57:50.594Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status · `toolu_01JCjD7X58sawuHuP3hKp8qy`</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3888f02e-894e-470b-bc9f-c6980bd54e83",
  "isSidechain": false,
  "requestId": "req_011CbHiyZUkeydr87qaPbzpi",
  "type": "assistant",
  "uuid": "d9257be3-40fd-40b4-b181-ab7b22ef82eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WqoLVCt61ov4ydaW7xwrTW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4989,
      "cache_read_input_tokens": 100999,
      "output_tokens": 702,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4989,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 702,
          "cache_read_input_tokens": 100999,
          "cache_creation_input_tokens": 4989,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4989
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

_source line 114 · 2026-05-22T13:57:50.635Z_

<details><summary>↩ Tool result · `toolu_01JCjD7X58sawuHuP3hKp8qy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T13:42:21.430890+00:00\", \"completed_at\": \"2026-05-22T13:42:25.019969+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets May 23, 4pm (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9257be3-40fd-40b4-b181-ab7b22ef82eb",
  "isSidechain": false,
  "promptId": "35007fc4-a558-4c2b-a533-ce1f9088b4a3",
  "type": "user",
  "uuid": "0001c75a-29ce-4209-a8d2-82ca404bc6c3",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"status\\\": \\\"done\\\", \\\"started_at\\\": \\\"2026-05-22T13:42:21.430890+00:00\\\", \\\"completed_at\\\": \\\"2026-05-22T13:42:25.019969+00:00\\\", \\\"findings\\\": [{\\\"severity\\\": \\\"info\\\", \\\"dimension\\\": \\\"agent_error\\\", \\\"message\\\": \\\"[ERROR] Agent exited 1: You've hit your limit · resets May 23, 4pm (UTC)\\\"}], \\\"counts\\\": {\\\"critical\\\": 0, \\\"warning\\\": 0, \\\"info\\\": 1}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T13:42:21.430890+00:00\", \"completed_at\": \"2026-05-22T13:42:25.019969+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets May 23, 4pm (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "d9257be3-40fd-40b4-b181-ab7b22ef82eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-22T13:57:51.164Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status · `toolu_01Hc1K1XUsnYzWCTVc6F4MhB`</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0001c75a-29ce-4209-a8d2-82ca404bc6c3",
  "isSidechain": false,
  "requestId": "req_011CbHiyZUkeydr87qaPbzpi",
  "type": "assistant",
  "uuid": "4993b4e6-291d-437c-b3c1-f848892e5dea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WqoLVCt61ov4ydaW7xwrTW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4989,
      "cache_read_input_tokens": 100999,
      "output_tokens": 702,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4989,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 702,
          "cache_read_input_tokens": 100999,
          "cache_creation_input_tokens": 4989,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4989
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

_source line 116 · 2026-05-22T13:57:53.116Z_

<details><summary>↩ Tool result · `toolu_01XT3rwHt3AZPiJ5oEyxg6wo`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6391f330-222c-4223-b2cf-45cb79d1669d",
  "isSidechain": false,
  "promptId": "35007fc4-a558-4c2b-a533-ce1f9088b4a3",
  "type": "user",
  "uuid": "172d8030-7fb3-4342-b92f-74c8912646a5",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "6391f330-222c-4223-b2cf-45cb79d1669d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-22T13:57:51.178Z_

<details><summary>↩ Tool result · `toolu_01Hc1K1XUsnYzWCTVc6F4MhB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4993b4e6-291d-437c-b3c1-f848892e5dea",
  "isSidechain": false,
  "promptId": "35007fc4-a558-4c2b-a533-ce1f9088b4a3",
  "type": "user",
  "uuid": "60435f5b-2300-417a-a4ab-2fd57c5a7e96",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"status\\\": \\\"not_requested\\\", \\\"message\\\": \\\"No external review requested.\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "4993b4e6-291d-437c-b3c1-f848892e5dea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-22T13:57:53.103Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XT3rwHt3AZPiJ5oEyxg6wo`</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "review_issues.yaml",
  "max_chars": 20000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60435f5b-2300-417a-a4ab-2fd57c5a7e96",
  "isSidechain": false,
  "requestId": "req_011CbHiyZUkeydr87qaPbzpi",
  "type": "assistant",
  "uuid": "6391f330-222c-4223-b2cf-45cb79d1669d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WqoLVCt61ov4ydaW7xwrTW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4989,
      "cache_read_input_tokens": 100999,
      "output_tokens": 702,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4989,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 702,
          "cache_read_input_tokens": 100999,
          "cache_creation_input_tokens": 4989,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4989
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

_source line 119_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Reviewer 2 审稿意见]: ## Reviewer 2 交叉回应 — 逐条回应 Reviewer 1 审稿意见  ---  ### Must-Fix 问题  **[AGREE] R1-N1: Theorem 1 适用范围过窄，Conjecture 1 缺乏证明**  同意这是一个实质性问题。我在自己的审稿中将其列为 W2（should-fix），但 R1 将其提升到 critical 也…",
  "leafUuid": "172d8030-7fb3-4342-b92f-74c8912646a5",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Runtime record

_source line 120_

```json
{
  "type": "ai-title",
  "aiTitle": "Review causal annotation error attribution paper",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Assistant

_source line 121 · 2026-05-22T13:57:56.753Z_

<details><summary>Logged reasoning block</summary>

```text
The read_project_file doesn't support review_issues.yaml. Let me read it directly using Read tool. Also, the visual check failed due to rate limit, and external review was not requested.

Let me read the review_issues.yaml directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "172d8030-7fb3-4342-b92f-74c8912646a5",
  "isSidechain": false,
  "requestId": "req_011CbHj183cGojPjcRX8cj9C",
  "type": "assistant",
  "uuid": "68d65efc-43be-4607-9292-43d5c64ec9c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RzVcDi6xV5CdVvrNEEVwPz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1205,
      "cache_read_input_tokens": 105988,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 157,
          "cache_read_input_tokens": 105988,
          "cache_creation_input_tokens": 1205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1205
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

_source line 122 · 2026-05-22T13:57:57.797Z_

<details open><summary>🔧 Tool call — Read · `toolu_012oHAYHg2N49FoTfXup3uwe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68d65efc-43be-4607-9292-43d5c64ec9c4",
  "isSidechain": false,
  "requestId": "req_011CbHj183cGojPjcRX8cj9C",
  "type": "assistant",
  "uuid": "f73301a3-e9d2-4d54-8679-84f9eb8ee164",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RzVcDi6xV5CdVvrNEEVwPz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1205,
      "cache_read_input_tokens": 105988,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 157,
          "cache_read_input_tokens": 105988,
          "cache_creation_input_tokens": 1205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1205
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

_source line 123 · 2026-05-22T13:57:57.809Z_

<details><summary>↩ Tool result · `toolu_012oHAYHg2N49FoTfXup3uwe`</summary>

```text
1	issues:
2	  # === Round 1 issues — status updates for Round 2 ===
3	
4	  - id: R1-N1
5	    category: soundness
6	    severity: must-fix
7	    summary: "Theorem 1 一般情形证明不完整：Cauchy-Schwarz 界的单调性 ≠ |B(C(δ))| 本身的单调性"
8	    status: in_progress
9	    first_raised_round: 1
10	    last_seen_round: 2
11	    mentions:
12	      - round: 1
13	        reviewers: [R1, R2]
14	        note: "R1 首发，R2 AGREE。Reviewer 确认 bias 是 δ 的有理函数（非线性），需正确的有理函数单调性证明。"
15	      - round: 2
16	        reviewers: [R1, R2]
17	        note: "双方再次独立提出。R1 明确指出上界单调 ≠ 函数单调（Cauchy-Schwarz gap）。R2 AGREE 并补充 ASV δ* 唯一性依赖。比例情形 (f=λg) 证明完整，一般情形仅 500 组数值验证。建议：一般情形降级为 Conjecture 或 Empirical Finding。"
18	    action_items:
19	      - round: 1
20	        action: "Confounding case 补解析证明（有理函数单调性，非线性），其余降级为 Conjecture"
21	        assigned_to: agent
22	        status: in_progress
23	      - round: 2
24	        action: "一般情形降级为 Empirical Finding，保留比例情形 (f=λg) 的解析证明"
25	        assigned_to: agent
26	        status: in_progress
27	    resolution: ""
28	    resolution_round: null
29	
30	  - id: R1-N2
31	    category: soundness
32	    severity: must-fix
33	    summary: "3/5 安全拓扑的符号保持仅有数值验证，缺乏解析证明"
34	    status: in_progress
35	    first_raised_round: 1
36	    last_seen_round: 2
37	    mentions:
38	      - round: 1
39	        reviewers: [R1, R2]
40	        note: "R1 首发，R2 AGREE 并建议拆分。"
41	      - round: 2
42	        reviewers: [R1, R2]
43	        note: "双方再次一致。摘要 'five topologies never produce sign reversal' 中 'never' 是全称量词，但 mediation/M-bias/front-door 仅有 Empirical Finding。R2 建议改为 'show no sign reversal in extensive numerical verification'。R1 补充 6D 空间 100k 采样密度论证。"
44	    action_items:
45	      - round: 1
46	        action: "拆分 Proposition 1 → 已证(confounding/collider/exposure反例) vs Empirical Finding(mediation/M-bias/front-door)；替换 'standard DGP' 为显式充分条件"
47	        assigned_to: agent
48	        status: in_progress
49	      - round: 2
50	        action: "Abstract 'never' → 'show no sign reversal... (proven analytically for confounding and collider via sufficient conditions)'"
51	        assigned_to: agent
52	        status: in_progress
53	    resolution: ""
54	    resolution_round: null
55	
56	  - id: R1-N3
57	    category: soundness
58	    severity: must-fix
59	    summary: "ASV C(δ) 定义域错误：δ∈[0,∞) 实际有限"
60	    status: resolved
61	    first_raised_round: 1
62	    last_seen_round: 1
63	    mentions:
64	      - round: 1
65	        reviewers: [R1, R2]
66	        note: "δ_max = min_j 1/(1-(C₀)_{jj})。sign-flip ASV 6.7 可能超出有效域。超出 δ_max 的 ASV 应标为 ∞（实际强化结论）。"
67	      - round: 2
68	        reviewers: []
69	        note: "本轮未被任何 Reviewer 提及。论文 Section 3.3 已引入 δ_max 约束并明确 ASV 限制在 [0, δ_max]。已修复。"
70	    action_items:
71	      - round: 1
72	        action: "引入 δ_max 约束，写脚本重新计算所有 ASV 值，超出 δ_max 标为 ∞，更新 method.tex + experiments.tex"
73	        assigned_to: agent
74	        status: resolved
75	    resolution: "Section 3.3 已引入 δ_max 约束，ASV 限制在 [0, δ_max]。Round 2 未再提及。"
76	    resolution_round: 2
77	
78	  - id: R2-N1
79	    category: presentation
80	    severity: should-fix
81	    summary: "83.4% headline framing 需调整叙事重心"
82	    status: open
83	    first_raised_round: 1
84	    last_seen_round: 2
85	    mentions:
86	      - round: 1
87	        reviewers: [R1, R2]
88	        note: "R2 首发，R1 AGREE。"
89	      - round: 2
90	        reviewers: [R1, R2]
91	        note: "R2 再次标为 CRITICAL。R1 REBUT：论文 Abstract 已同时报告 83.4%（Dirichlet prior）和 2.1%（realistic accuracy），条件透明。Dirichlet(1,1,1) 用于参数空间刻画有方法论正当性。R1 建议降级为 WARNING。R2 未反驳 REBUT。综合判断：降级为 should-fix。"
92	    action_items:
93	      - round: 1
94	        action: "Abstract/Intro 同时呈现 full prior (83.4%) 和 realistic regime (2.1% sign reversal at diagonal≥0.7)"
95	        assigned_to: agent
96	        status: pending
97	      - round: 2
98	        action: "调整叙事重心：以 realistic accuracy 为主叙事，Dirichlet(1,1,1) 作为参数空间刻画的补充"
99	        assigned_to: agent
100	        status: pending
101	    resolution: ""
102	    resolution_round: null
103	
104	  - id: R2-N2
105	    category: novelty
106	    severity: should-fix
107	    summary: "'first systematic framework' 过度声明"
108	    status: resolved
109	    first_raised_round: 1
110	    last_seen_round: 1
111	    mentions:
112	      - round: 1
113	        reviewers: [R1, R2]
114	        note: "R2 must-fix，R1 rebut 认为 K≥3 是质变。降级 should-fix。"
115	      - round: 2
116	        reviewers: []
117	        note: "本轮未被提及。当前 Abstract 使用 'We present a systematic framework'（非 'the first'），已修复。"
118	    action_items:
119	      - round: 1
120	        action: "Abstract/Intro 'the first systematic framework' → 'a systematic framework'；保留 'first to jointly characterize' 在有依据处"
121	        assigned_to: agent
122	        status: resolved
123	    resolution: "Abstract 已改为 'We present a systematic framework'。Round 2 未再提及。"
124	    resolution_round: 2
125	
126	  - id: R2-N3
127	    category: related_work
128	    severity: must-fix
129	    summary: "4 篇关键相关工作未引用"
130	    status: resolved
131	    first_raised_round: 1
132	    last_seen_round: 1
133	    mentions:
134	      - round: 1
135	        reviewers: [R1, R2]
136	        note: "4 篇已在 references.bib 中，page fitting 时从 .tex 移除。需恢复 \\cite 并补讨论。"
137	      - round: 2
138	        reviewers: []
139	        note: "本轮未被提及。当前 Related Work 已包含 audinet2025, zrnic_candes2024, gligoric2025, keith_jensen_oconnor2020 的引用，已修复。Round 2 新增了 2 篇遗漏引用（见 NEW-2）。"
140	    action_items:
141	      - round: 1
142	        action: "恢复 audinet2025, zrnic_candes2024, gligoric2025, keith_jensen_oconnor2020 引用；Related Work 补讨论"
143	        assigned_to: agent
144	        status: resolved
145	    resolution: "4 篇引用已全部恢复到 Related Work。Round 2 未再提及这 4 篇，但新增了 2 篇遗漏（NEW-2）。"
146	    resolution_round: 2
147	
148	  - id: R1-W2
149	    category: clarity
150	    severity: should-fix
151	    summary: "Sign preservation 的 DGP 条件在实践中难以事前验证"
152	    status: in_progress
153	    first_raised_round: 1
154	    last_seen_round: 2
155	    mentions:
156	      - round: 1
157	        reviewers: [R1, R2]
158	        note: "双方 AGREE。"
159	      - round: 2
160	        reviewers: [R1, R2]
161	        note: "双方再次一致。Table 2 充分条件涉及未知 DGP 参数。论文 p4 承认但未讨论满足频率或可诊断性。建议添加模拟或 domain knowledge 讨论。"
162	    action_items:
163	      - round: 1
164	        action: "Method 加 1-2 句讨论条件循环性 + ASV 作为不依赖精确条件的替代"
165	        assigned_to: agent
166	        status: in_progress
167	      - round: 2
168	        action: "添加 DGP 条件可验证性讨论 + 数值 demo 表格"
169	        assigned_to: agent
170	        status: in_progress
171	    resolution: ""
172	    resolution_round: null
173	
174	  - id: R1-W3
175	    category: experiments
176	    severity: should-fix
177	    summary: "实证验证不完整：22/38 配置完成，无商业 LLM"
178	    status: in_progress
179	    first_raised_round: 1
180	    last_seen_round: 2
181	    mentions:
182	      - round: 1
183	        reviewers: [R1, R2]
184	        note: "R1 首发，R2 部分 AGREE。"
185	      - round: 2
186	        reviewers: [R1, R2]
187	        note: "双方再次一致。R2 纠正数字为 14/38（非 14/28），完成率仅 36.8%。R1 补充缺少商业 LLM（GPT-4, Claude）对比。注：已扩展至 22 configs。"
188	    action_items:
189	      - round: 1
190	        action: "Limitations 强化 model asymmetry caveat"
191	        assigned_to: agent
192	        status: in_progress
193	      - round: 2
194	        action: "Limitations 讨论开源 vs 商业 LLM 误差模式差异，更新覆盖率数字"
195	        assigned_to: agent
196	        status: in_progress
197	    resolution: ""
198	    resolution_round: null
199	
200	  - id: R2-W2
201	    category: presentation
202	    severity: should-fix
203	    summary: "98 场景 zero sign reversals 与 sign reversal narrative 的 tension"
204	    status: resolved
205	    first_raised_round: 1
206	    last_seen_round: 1
207	    mentions:
208	      - round: 1
209	        reviewers: [R1, R2]
210	        note: "R2 首发，R1 rebut 但同意调整 framing。"
211	      - round: 2
212	        reviewers: []
213	        note: "本轮未被提及。Experiments 已用 triple verification narrative 区分：132 non-exposure scenarios 0 flips vs 13/22 exposure configs 59% flip rate。已改善。"
214	    action_items:
215	      - round: 1
216	        action: "Experiments 明确区分理论风险（Dirichlet prior）vs 实践观测（empirical matrices）"
217	        assigned_to: agent
218	        status: resolved
219	    resolution: "Triple verification narrative 已解决 tension：safe topologies 0 flips vs exposure 59% flips，区分清晰。Round 2 未再提及。"
220	    resolution_round: 2
221	
222	  - id: R2-W3
223	    category: method
224	    severity: should-fix
225	    summary: "ASV 对 C₀ 估计不确定性的敏感性未展示"
226	    status: in_progress
227	    first_raised_round: 1
228	    last_seen_round: 2
229	    mentions:
230	      - round: 1
231	        reviewers: [R1, R2]
232	        note: "R2 首发，R1 AGREE。"
233	      - round: 2
234	        reviewers: [R1, R2]
235	        note: "双方再次一致。论文 p4 提到 'we recommend bootstrapping C₀ and reporting ASV confidence intervals' 但未展示实际 bootstrap 结果。R1 要求示例。R2 追问不同 C₀ 是否导致 safe/unsafe 判断翻转。"
236	    action_items:
237	      - round: 1
238	        action: "Method 或 Limitations 加 bootstrap C₀ uncertainty 讨论"
239	        assigned_to: agent
240	        status: in_progress
241	      - round: 2
242	        action: "展示至少一个 C₀ bootstrap 示例（HumAID deepseek_zs, B=1000），分析 δ* 的 95% CI"
243	        assigned_to: agent
244	        status: in_progress
245	    resolution: ""
246	    resolution_round: null
247	
248	  - id: R2-W4
249	    category: scope
250	    severity: should-fix
251	    summary: "线性 SEM 假设限制对 NLP 受众的实用性"
252	    status: in_progress
253	    first_raised_round: 1
254	    last_seen_round: 2
255	    mentions:
256	      - round: 1
257	        reviewers: [R1, R2]
258	        note: "R2 首发，R1 AGREE。FWL 对 logistic regression 不成立。"
259	      - round: 2
260	        reviewers: [R1, R2]
261	        note: "双方再次完全一致。Limitations 仅一句提及。建议至少一个 logistic DGP 模拟验证 sign-flip 是否定性保持。"
262	    action_items:
263	      - round: 1
264	        action: "Limitations 加线性模型假设 + FWL 不推广到非线性的说明"
265	        assigned_to: agent
266	        status: in_progress
267	      - round: 2
268	        action: "添加 K=3 logistic regression 模拟实验验证核心发现的定性保持"
269	        assigned_to: agent
270	        status: in_progress
271	    resolution: ""
272	    resolution_round: null
273	
274	  - id: R1-W4
275	    category: experiments
276	    severity: should-fix
277	    summary: "MC MAPE 报告不充分，掩盖 per-topology 差异"
278	    status: resolved
279	    first_raised_round: 1
280	    last_seen_round: 1
281	    mentions:
282	      - round: 1
283	        reviewers: [R1, R2]
284	        note: "R1 首发，R2 AGREE。"
285	      - round: 2
286	        reviewers: []
287	        note: "本轮未被提及。论文已报告 per-topology range (0.5%-5.5%)。"
288	    action_items:
289	      - round: 1
290	        action: "已有 per-topology range (0.5%-5.5%)，考虑加 median 或更详细报告"
291	        assigned_to: agent
292	        status: resolved
293	    resolution: "Per-topology MAPE range 已在论文中报告。Round 2 未再提及。"
294	    resolution_round: 2
295	
296	  - id: MISC-1
297	    category: presentation
298	    severity: minor
299	    summary: "符号不统一、命名歧义、Table caption 不完整"
300	    status: in_progress
301	    first_raised_round: 1
302	    last_seen_round: 2
303	    mentions:
304	      - round: 1
305	        reviewers: [R1, R2]
306	        note: "双方 AGREE。"
307	      - round: 2
308	        reviewers: [R2]
309	        note: "R2 在小问题中提到符号系统多套（τ, τ̂, f(A*), β）建议符号表。"
310	    action_items:
311	      - round: 1
312	        action: "统一符号，修正命名，补 Table caption 定义"
313	        assigned_to: agent
314	        status: in_progress
315	      - round: 2
316	        action: "添加 Appendix 符号表"
317	        assigned_to: agent
318	        status: in_progress
319	    resolution: ""
320	    resolution_round: null
321	
322	  # === Round 2 新增 issues ===
323	
324	  - id: NEW-1
325	    category: soundness
326	    severity: must-fix
327	    summary: "Non-differential misclassification stress test 仅覆盖单一拓扑(exposure)、单一 K 值(K=3)、ε≤0.10"
328	    status: in_progress
329	    first_raised_round: 2
330	    last_seen_round: 2
331	    mentions:
332	      - round: 2
333	        reviewers: [R1, R2]
334	        note: "R1 标为 MAJOR。R2 AGREE with nuance：non-differential 是标准假设（Carroll 2006），且 Table 6 显示小偏离下 sign-flip 仅从 2.0% 升至 4.5%，但覆盖面确实过窄。建议扩展至 confounding/mediation + K=10。"
335	    action_items:
336	      - round: 2
337	        action: "Exp-A: 扩展 stress test 至 confounding+mediation+exposure+IV × K=3,10 × ε=0,0.01,0.05,0.10"
338	        assigned_to: agent
339	        status: in_progress
340	    resolution: ""
341	    resolution_round: null
342	
343	  - id: NEW-2
344	    category: related_work
345	    severity: should-fix
346	    summary: "缺少 2 篇高度相关引用：Feder et al. (2022) TACL 综述, Cheng et al. (2024) LLM 误差分解"
347	    status: in_progress
348	    first_raised_round: 2
349	    last_seen_round: 2
350	    mentions:
351	      - round: 2
352	        reviewers: [R1, R2]
353	        note: "R2 提出，R1 AGREE（Feder 完全同意，Cheng 条件性同意）。Feder et al. 是 NLP+因果推断最重要综述（TACL，400+ 引用），投 EMNLP 必引。Cheng et al. 分解 LLM 标注误差上游来源，与本文下游传播分析互补。"
354	    action_items:
355	      - round: 2
356	        action: "SF2: Related Work 补充 Feder et al. (2022) TACL 和 Cheng et al. (2024) 引用"
357	        assigned_to: agent
358	        status: in_progress
359	    resolution: ""
360	    resolution_round: null
361	
362	  - id: NEW-3
363	    category: soundness
364	    severity: should-fix
365	    summary: "Conjecture 1 数值验证仅 500 scenarios，远少于 Empirical Finding 1 的 100,000"
366	    status: in_progress
367	    first_raised_round: 2
368	    last_seen_round: 2
369	    mentions:
370	      - round: 2
371	        reviewers: [R1, R2]
372	        note: "R1 首发，R2 AGREE。200 倍的采样量差异缺乏解释。Conjecture 1 是 ASV 框架的理论基础，重要性不亚于 Empirical Finding 1。"
373	    action_items:
374	      - round: 2
375	        action: "Exp-D: 增加 Conjecture 1 验证到 10,000 random + 100-start adversarial search per topology"
376	        assigned_to: agent
377	        status: in_progress
378	    resolution: ""
379	    resolution_round: null
380	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f73301a3-e9d2-4d54-8679-84f9eb8ee164",
  "isSidechain": false,
  "promptId": "35007fc4-a558-4c2b-a533-ce1f9088b4a3",
  "type": "user",
  "uuid": "2b5f8c30-6ef1-47a3-a50f-1375ade95ad9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
      "content": "issues:\n  # === Round 1 issues — status updates for Round 2 ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 一般情形证明不完整：Cauchy-Schwarz 界的单调性 ≠ |B(C(δ))| 本身的单调性\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE。Reviewer 确认 bias 是 δ 的有理函数（非线性），需正确的有理函数单调性证明。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次独立提出。R1 明确指出上界单调 ≠ 函数单调（Cauchy-Schwarz gap）。R2 AGREE 并补充 ASV δ* 唯一性依赖。比例情形 (f=λg) 证明完整，一般情形仅 500 组数值验证。建议：一般情形降级为 Conjecture 或 Empirical Finding。\"\n    action_items:\n      - round: 1\n        action: \"Confounding case 补解析证明（有理函数单调性，非线性），其余降级为 Conjecture\"\n        assigned_to: agent\n        status: in_progress\n      - round: 2\n        action: \"一般情形降级为 Empirical Finding，保留比例情形 (f=λg) 的解析证明\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N2\n    category: soundness\n    severity: must-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，缺乏解析证明\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE 并建议拆分。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次一致。摘要 'five topologies never produce sign reversal' 中 'never' 是全称量词，但 mediation/M-bias/front-door 仅有 Empirical Finding。R2 建议改为 'show no sign reversal in extensive numerical verification'。R1 补充 6D 空间 100k 采样密度论证。\"\n    action_items:\n      - round: 1\n        action: \"拆分 Proposition 1 → 已证(confounding/collider/exposure反例) vs Empirical Finding(mediation/M-bias/front-door)；替换 'standard DGP' 为显式充分条件\"\n        assigned_to: agent\n        status: in_progress\n      - round: 2\n        action: \"Abstract 'never' → 'show no sign reversal... (proven analytically for confounding and collider via sufficient conditions)'\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误：δ∈[0,∞) 实际有限\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"δ_max = min_j 1/(1-(C₀)_{jj})。sign-flip ASV 6.7 可能超出有效域。超出 δ_max 的 ASV 应标为 ∞（实际强化结论）。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未被任何 Reviewer 提及。论文 Section 3.3 已引入 δ_max 约束并明确 ASV 限制在 [0, δ_max]。已修复。\"\n    action_items:\n      - round: 1\n        action: \"引入 δ_max 约束，写脚本重新计算所有 ASV 值，超出 δ_max 标为 ∞，更新 method.tex + experiments.tex\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Section 3.3 已引入 δ_max 约束，ASV 限制在 [0, δ_max]。Round 2 未再提及。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: should-fix\n    summary: \"83.4% headline framing 需调整叙事重心\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"R2 再次标为 CRITICAL。R1 REBUT：论文 Abstract 已同时报告 83.4%（Dirichlet prior）和 2.1%（realistic accuracy），条件透明。Dirichlet(1,1,1) 用于参数空间刻画有方法论正当性。R1 建议降级为 WARNING。R2 未反驳 REBUT。综合判断：降级为 should-fix。\"\n    action_items:\n      - round: 1\n        action: \"Abstract/Intro 同时呈现 full prior (83.4%) 和 realistic regime (2.1% sign reversal at diagonal≥0.7)\"\n        assigned_to: agent\n        status: pending\n      - round: 2\n        action: \"调整叙事重心：以 realistic accuracy 为主叙事，Dirichlet(1,1,1) 作为参数空间刻画的补充\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 must-fix，R1 rebut 认为 K≥3 是质变。降级 should-fix。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未被提及。当前 Abstract 使用 'We present a systematic framework'（非 'the first'），已修复。\"\n    action_items:\n      - round: 1\n        action: \"Abstract/Intro 'the first systematic framework' → 'a systematic framework'；保留 'first to jointly characterize' 在有依据处\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Abstract 已改为 'We present a systematic framework'。Round 2 未再提及。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"4 篇已在 references.bib 中，page fitting 时从 .tex 移除。需恢复 \\\\cite 并补讨论。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未被提及。当前 Related Work 已包含 audinet2025, zrnic_candes2024, gligoric2025, keith_jensen_oconnor2020 的引用，已修复。Round 2 新增了 2 篇遗漏引用（见 NEW-2）。\"\n    action_items:\n      - round: 1\n        action: \"恢复 audinet2025, zrnic_candes2024, gligoric2025, keith_jensen_oconnor2020 引用；Related Work 补讨论\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"4 篇引用已全部恢复到 Related Work。Round 2 未再提及这 4 篇，但新增了 2 篇遗漏（NEW-2）。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"双方 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次一致。Table 2 充分条件涉及未知 DGP 参数。论文 p4 承认但未讨论满足频率或可诊断性。建议添加模拟或 domain knowledge 讨论。\"\n    action_items:\n      - round: 1\n        action: \"Method 加 1-2 句讨论条件循环性 + ASV 作为不依赖精确条件的替代\"\n        assigned_to: agent\n        status: in_progress\n      - round: 2\n        action: \"添加 DGP 条件可验证性讨论 + 数值 demo 表格\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：22/38 配置完成，无商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 部分 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次一致。R2 纠正数字为 14/38（非 14/28），完成率仅 36.8%。R1 补充缺少商业 LLM（GPT-4, Claude）对比。注：已扩展至 22 configs。\"\n    action_items:\n      - round: 1\n        action: \"Limitations 强化 model asymmetry caveat\"\n        assigned_to: agent\n        status: in_progress\n      - round: 2\n        action: \"Limitations 讨论开源 vs 商业 LLM 误差模式差异，更新覆盖率数字\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 rebut 但同意调整 framing。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未被提及。Experiments 已用 triple verification narrative 区分：132 non-exposure scenarios 0 flips vs 13/22 exposure configs 59% flip rate。已改善。\"\n    action_items:\n      - round: 1\n        action: \"Experiments 明确区分理论风险（Dirichlet prior）vs 实践观测（empirical matrices）\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Triple verification narrative 已解决 tension：safe topologies 0 flips vs exposure 59% flips，区分清晰。Round 2 未再提及。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性未展示\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次一致。论文 p4 提到 'we recommend bootstrapping C₀ and reporting ASV confidence intervals' 但未展示实际 bootstrap 结果。R1 要求示例。R2 追问不同 C₀ 是否导致 safe/unsafe 判断翻转。\"\n    action_items:\n      - round: 1\n        action: \"Method 或 Limitations 加 bootstrap C₀ uncertainty 讨论\"\n        assigned_to: agent\n        status: in_progress\n      - round: 2\n        action: \"展示至少一个 C₀ bootstrap 示例（HumAID deepseek_zs, B=1000），分析 δ* 的 95% CI\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制对 NLP 受众的实用性\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 AGREE。FWL 对 logistic regression 不成立。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次完全一致。Limitations 仅一句提及。建议至少一个 logistic DGP 模拟验证 sign-flip 是否定性保持。\"\n    action_items:\n      - round: 1\n        action: \"Limitations 加线性模型假设 + FWL 不推广到非线性的说明\"\n        assigned_to: agent\n        status: in_progress\n      - round: 2\n        action: \"添加 K=3 logistic regression 模拟实验验证核心发现的定性保持\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分，掩盖 per-topology 差异\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未被提及。论文已报告 per-topology range (0.5%-5.5%)。\"\n    action_items:\n      - round: 1\n        action: \"已有 per-topology range (0.5%-5.5%)，考虑加 median 或更详细报告\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Per-topology MAPE range 已在论文中报告。Round 2 未再提及。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一、命名歧义、Table caption 不完整\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"双方 AGREE。\"\n      - round: 2\n        reviewers: [R2]\n        note: \"R2 在小问题中提到符号系统多套（τ, τ̂, f(A*), β）建议符号表。\"\n    action_items:\n      - round: 1\n        action: \"统一符号，修正命名，补 Table caption 定义\"\n        assigned_to: agent\n        status: in_progress\n      - round: 2\n        action: \"添加 Appendix 符号表\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 2 新增 issues ===\n\n  - id: NEW-1\n    category: soundness\n    severity: must-fix\n    summary: \"Non-differential misclassification stress test 仅覆盖单一拓扑(exposure)、单一 K 值(K=3)、ε≤0.10\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"R1 标为 MAJOR。R2 AGREE with nuance：non-differential 是标准假设（Carroll 2006），且 Table 6 显示小偏离下 sign-flip 仅从 2.0% 升至 4.5%，但覆盖面确实过窄。建议扩展至 confounding/mediation + K=10。\"\n    action_items:\n      - round: 2\n        action: \"Exp-A: 扩展 stress test 至 confounding+mediation+exposure+IV × K=3,10 × ε=0,0.01,0.05,0.10\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 2 篇高度相关引用：Feder et al. (2022) TACL 综述, Cheng et al. (2024) LLM 误差分解\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"R2 提出，R1 AGREE（Feder 完全同意，Cheng 条件性同意）。Feder et al. 是 NLP+因果推断最重要综述（TACL，400+ 引用），投 EMNLP 必引。Cheng et al. 分解 LLM 标注误差上游来源，与本文下游传播分析互补。\"\n    action_items:\n      - round: 2\n        action: \"SF2: Related Work 补充 Feder et al. (2022) TACL 和 Cheng et al. (2024) 引用\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证仅 500 scenarios，远少于 Empirical Finding 1 的 100,000\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE。200 倍的采样量差异缺乏解释。Conjecture 1 是 ASV 框架的理论基础，重要性不亚于 Empirical Finding 1。\"\n    action_items:\n      - round: 2\n        action: \"Exp-D: 增加 Conjecture 1 验证到 10,000 random + 100-start adversarial search per topology\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n",
      "numLines": 380,
      "startLine": 1,
      "totalLines": 380
    }
  },
  "sourceToolAssistantUUID": "f73301a3-e9d2-4d54-8679-84f9eb8ee164",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 124_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Reviewer 2 审稿意见]: ## Reviewer 2 交叉回应 — 逐条回应 Reviewer 1 审稿意见  ---  ### Must-Fix 问题  **[AGREE] R1-N1: Theorem 1 适用范围过窄，Conjecture 1 缺乏证明**  同意这是一个实质性问题。我在自己的审稿中将其列为 W2（should-fix），但 R1 将其提升到 critical 也…",
  "leafUuid": "2b5f8c30-6ef1-47a3-a50f-1375ade95ad9",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Runtime record

_source line 125_

```json
{
  "type": "ai-title",
  "aiTitle": "Review causal annotation error attribution paper",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Assistant

_source line 126 · 2026-05-22T13:59:10.857Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture. Let me synthesize the report.

Key observations from the review_issues.yaml:
- This is Round 3. There are issues from Round 1 and Round 2.
- Several issues from prior rounds are resolved (R1-N3, R2-N2, R2-N3, R2-W2, R1-W4)
- Several issues remain in_progress or open

Now let me map the current Round 3 findings to the existing issues:

**Round 3 findings that map to existing issues:**

1. **Page limit (R1-N2, R2-N1 both critical)** → This is a NEW issue not in the tracker! The prior rounds didn't flag page limit. Let me add it.


2. **Conjecture 1 未证明 / Theorem 1 适用范围窄 (R1-N1 critical, R2-W2 warning)** → Maps to existing **R1-N1** (Theorem 1 一般情形证明不完整). The issue persists across rounds — Conjecture 1 remains unproven, though it's now explicitly framed as a Conjecture rather than a Theorem.
3. **Sign reversal overclaiming (R2-N2 critical, R1-W3 warning)** → Maps to existing **R2-N1** (83.4% headline framing). The problem has deepened: R2 identifies that empirical sign reversals only affect secondary coefficients, widening the disconnect between what's claimed and what the evidence supports.
4. **3/5 sign preservation 缺解析证明 (R2-W1 warning)** → Maps to existing **R1-N2**. The Proposition was split as suggested, but the abstract still uses language like "establish" that overstates the scope of what's actually proven.
5. **Non-differential assumption (R1-W1, R2-W3 warning)** → Maps to existing **NEW-1** from Round 2. The stress test expanded to 96 configurations per Appendix B.4, but R2 points out the core issue remains unresolved.
6. **Linear SEM limitation (R1-W2 warning)** → Maps to existing **R2-W4**. A logistic DGP robustness check was added in Appendix B.6 covering 3 topologies, though FWL invariance breaks down in the nonlinear case.
7. **FWL invariance lacks formal proof (R1-N3 critical)** → R2 argues this follows directly from the FWL theorem, but the claim still needs explicit derivation.
8. **Outcome misclassification not discussed (R2-W4 warning)** → This is a new gap that hasn't been addressed.
9. **Abstract info overload (R2-W5 warning)** → Another new concern about presentation density.
10. **Code/data not promised** → Still unresolved.
11. **Novelty delineation unclear (R1-W4 warning)** → The boundary between this work and prior results needs clarification.
12. **Empirical validation uses simulated DGP (R1-W5 warning)** → Relying on simulations rather than real data is a limitation worth noting.
13. **Missing references** → Several key papers need to be cited, including recent work on causal inference and measurement error.

Now I'm stepping back to reconcile the issues tracker with what's actually been resolved versus what remains open, particularly looking at how R1 and R2 comments map to the current status.

The Theorem 1 proof issue has evolved—the general case was appropriately downgraded to a conjecture, but the conjecture itself remains unproven, so this is still in progress. The sign preservation finding across 3 out of 5 specifications is still numerical-only without formal establishment. The 83.4% framing concern persists and has expanded to include questions about secondary coefficients. The stress test coverage has grown to 96 configurations, which partially addresses earlier concerns but leaves the scope question still open.

Looking at the expanded stress test more carefully—the paper now includes Appendix B.4 with the full 96-configuration matrix across topologies, K values, and quality metrics, which does seem to respond to the earlier feedback. The bootstrap uncertainty analysis for ASV also appears resolved with Appendix B.5 showing 1,000 bootstrap samples, and neither reviewer flagged this as missing in Round 3. I'm checking what remains unaddressed from the previous rounds. R1-W2 about DGP verifiability wasn't explicitly flagged again in Round 3, though it relates to the "Empirical Finding" wording concern. The empirical validation has expanded to cover 161 scenarios across multiple topologies, addressing the earlier incompleteness issue. Most other weaknesses from prior rounds appear resolved and weren't re-raised, except for notation which remains in progress.

Now I'm compiling the Round 3 issues and organizing them by priority. The page limit is a critical concern both reviewers flagged, and the sign reversal framing—particularly the 83.4% statistic and "catastrophic" language—needs significant revision, especially since R2 marked it critical and R1 has agreed to escalate it.

Conjecture 1 and Theorem 1 remain contentious: R1 sees them as critical gaps, while R2 acknowledges the scope limitation but doesn't view it as a blocker. The FWL invariance proof is another divergence—R1 wants formal rigor, R2 thinks the writing just needs clarification.

For the should-fix category, I'm tracking the sign preservation wording across those three results, the non-differential assumption discussion that's only partially addressed, and the linear SEM limitation that needs more explicit caveating in Algorithm 1.

Beyond that, there's outcome misclassification that hasn't been discussed, abstract information overload, the missing code and data availability statement, how novelty is positioned relative to prior work, and the fact that empirical validation relies on simulated data rather than real-world examples. On novelty and empirical validation, the reviewers partially agree but with some nuance.

Missing references are straightforward consensus items: Cinelli & Hazlett, Gilardi et al., Ziems et al., Bound et al., and the Bayesian measurement error citations all need to be added.

Both reviewers landed on 3.5, so I'm looking at a borderline decision.

The core issue is that while this tackles an important and timely problem with a systematic approach, the theoretical contributions are moderate—mostly conjectures rather than formal theorems—and there's overclaiming in how the work is framed. The page limit constraint is particularly problematic and could trigger a desk rejection. I need to write up the full consolidated report now, covering summary, strengths, weaknesses, consensus and divergence points, questions, missing references, and the overall assessment, then update the review issues file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b5f8c30-6ef1-47a3-a50f-1375ade95ad9",
  "isSidechain": false,
  "requestId": "req_011CbHj1U2tEQhXrYD2FLHH7",
  "type": "assistant",
  "uuid": "5f16aeb4-ed7c-419a-91e1-d383d4d912c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiPRiKXjZyd12EVcbxD3Fe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6431,
      "cache_read_input_tokens": 107193,
      "output_tokens": 11002,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11002,
          "cache_read_input_tokens": 107193,
          "cache_creation_input_tokens": 6431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6431
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

_source line 127 · 2026-05-22T13:59:11.101Z_

视觉审查因 Agent 配额耗尽失败，外部审稿未请求。现在基于两位 Reviewer 的完整意见和交叉回应合成最终报告。

先整理 issue tracker，然后提交报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f16aeb4-ed7c-419a-91e1-d383d4d912c2",
  "isSidechain": false,
  "requestId": "req_011CbHj1U2tEQhXrYD2FLHH7",
  "type": "assistant",
  "uuid": "c40ed250-ffaa-418b-addb-15f4f0d6d790",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiPRiKXjZyd12EVcbxD3Fe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6431,
      "cache_read_input_tokens": 107193,
      "output_tokens": 11002,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11002,
          "cache_read_input_tokens": 107193,
          "cache_creation_input_tokens": 6431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6431
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

_source line 128 · 2026-05-22T14:01:31.918Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues · `toolu_01VU6tgZeXxQbLZ5ov7vMz1g`</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "issues_yaml": "issues:\n  # === Round 1 issues — status updates through Round 3 ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），Conjecture 1 未证明\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE。Reviewer 确认 bias 是 δ 的有理函数（非线性），需正确的有理函数单调性证明。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次独立提出。R1 明确指出上界单调 ≠ 函数单调（Cauchy-Schwarz gap）。R2 AGREE 并补充 ASV δ* 唯一性依赖。比例情形 (f=λg) 证明完整，一般情形仅 500 组数值验证。建议：一般情形降级为 Conjecture 或 Empirical Finding。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1 列为 N1 critical：Table 9 显示 60-97% 随机矩阵违反严格单调性，ASV 的 well-defined sensitivity measure 语义依赖单调性。R2 列为 W2 should-fix：ASV 核心价值在于 topology ranking，ranking 在所有实验中成立，不完全依赖严格单调性。R2 建议至少证明 mediation。双方方向一致，严重性分歧（R1 must-fix vs R2 should-fix）。\"\n    action_items:\n      - round: 1\n        action: \"Confounding case 补解析证明（有理函数单调性，非线性），其余降级为 Conjecture\"\n        assigned_to: agent\n        status: in_progress\n      - round: 2\n        action: \"一般情形降级为 Empirical Finding，保留比例情形 (f=λg) 的解析证明\"\n        assigned_to: agent\n        status: done\n      - round: 3\n        action: \"至少证明 mediation 的单调性；正文讨论 Conjecture 失败时 ASV interpretation 如何 degrade；给出 ε 关于 K 和 DGP 参数的 formal bound\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE 并建议拆分。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次一致。Abstract 改为 'establish...proven analytically for confounding and collider via sufficient conditions; Appendix A'。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R2-W1: Abstract 仍用 'establish that five topologies show no sign reversal'，'establish' 对仅有 empirical verification 的 3 拓扑是 overclaim。R1 AGREE。建议用 'prove for confounding and collider, verify numerically for mediation, M-bias, and front-door'。\"\n    action_items:\n      - round: 2\n        action: \"Abstract 'never' → 'show no sign reversal... (proven analytically for confounding and collider via sufficient conditions)'\"\n        assigned_to: agent\n        status: done\n      - round: 3\n        action: \"Abstract/Conclusion 中区分 'proven'(2) vs 'numerically verified'(3)，或用 'show' 替代 'establish'\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误：δ∈[0,∞) 实际有限\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"δ_max = min_j 1/(1-(C₀)_{jj})。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未被提及。Section 3.3 已引入 δ_max 约束。已修复。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被提及。确认已修复。\"\n    action_items:\n      - round: 1\n        action: \"引入 δ_max 约束\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Section 3.3 已引入 δ_max 约束，ASV 限制在 [0, δ_max]。Round 2-3 未再提及。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称；empirical sign reversal 仅影响 secondary coefficients\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"R2 再次标为 CRITICAL。R1 REBUT 认为 Dirichlet 有方法论正当性。降级为 should-fix。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R2 再次列为 N2 critical：(1) 83.4% 来自不现实的 Dirichlet(1,1,1) prior，realistic regime 仅 2.1%；(2) 新发现——Section 4.4 明确写道 primary coefficient never reverses，sign flips exclusively in secondary coefficients with small |β|，与 Abstract 'catastrophic' 框架严重不符。R1 AGREE 并升级：'Section 4.2 catastrophic sign reversal 小标题与 Section 4.4 实证结果自相矛盾'。建议：先报告 2.1%（realistic），再提 83.4%（theoretical）；用 'structurally possible' 替代 'catastrophic'。\"\n    action_items:\n      - round: 2\n        action: \"调整叙事重心：以 realistic accuracy 为主叙事\"\n        assigned_to: agent\n        status: pending\n      - round: 3\n        action: \"(1) Abstract 先报告 realistic regime (diagonal≥0.7, 2.1% sign reversal)，再提 Dirichlet 83.4% 作为理论上界；(2) 明确说明 empirical sign reversal 限于 secondary coefficients；(3) 替换 'catastrophic' 措辞\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 must-fix，R1 rebut。降级 should-fix。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被提及。Abstract 已改为 'We present a systematic framework'。确认已修复。\"\n    action_items:\n      - round: 1\n        action: \"Abstract 'the first' → 'a systematic framework'\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Abstract 已改为 'We present a systematic framework'。Round 2-3 未再提及。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"4 篇已恢复引用。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被提及。确认已修复。但 Round 3 发现新的遗漏引用（见 R3-NEW-5）。\"\n    action_items:\n      - round: 1\n        action: \"恢复 audinet2025, zrnic_candes2024, gligoric2025, keith_jensen_oconnor2020 引用\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"4 篇引用已全部恢复。Round 2-3 未再提及。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"双方 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次一致。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被明确提及。论文 Section 3.2 最后一段添加了 ASV 作为不依赖精确条件的替代讨论。可能已部分改善。\"\n    action_items:\n      - round: 2\n        action: \"添加 DGP 条件可验证性讨论 + ASV 作为替代\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 部分 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"已扩展至 23 configs（4 LLM × 3 数据集）。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未明确提及。Section 4.4 报告 23 configurations，但均为开源 LLM（Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat, Qwen2.5-7B-Instruct），Limitations 提到 '15 of 18 planned configurations completed'。\"\n    action_items:\n      - round: 2\n        action: \"Limitations 讨论开源 vs 商业 LLM 误差模式差异\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 rebut。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被提及。叙事已改善。\"\n    action_items:\n      - round: 1\n        action: \"区分理论风险 vs 实践观测\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Triple verification narrative 已解决。Round 2-3 未再提及。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"建议展示 bootstrap 示例。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被提及。Appendix B.5 现包含 B=1,000 bootstrap，95% CI for magnitude ASV。Section 3.3 建议 bootstrapping。Section 4.3 报告 bootstrap CI。已修复。\"\n    action_items:\n      - round: 2\n        action: \"展示 bootstrap C₀ uncertainty 示例\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Appendix B.5 + Section 4.3 已包含 bootstrap ASV 分析。Round 3 未再提及。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制对 NLP 受众的实用性；FWL 对 logistic 不成立\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"建议至少一个 logistic DGP 模拟验证。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1-W2: Appendix B.6 仅覆盖 3 拓扑（confounding, exposure, IV）的 logistic DGP，sign-flip rate 差异 <2pp，但 FWL invariance 在非线性下不成立。R2 AGREE 并补充：Algorithm 1 中 FWL 分流在 logistic 下可能失效，但 Algorithm 1 未加 caveat。\"\n    action_items:\n      - round: 2\n        action: \"添加 logistic DGP 模拟实验\"\n        assigned_to: agent\n        status: done\n      - round: 3\n        action: \"(1) Algorithm 1 添加 'linear models only' caveat；(2) 扩展 Appendix B.6 至全部 7 拓扑\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被提及。Per-topology MAPE range (0.5%-5.5%) 已报告。确认已修复。\"\n    action_items:\n      - round: 1\n        action: \"报告 per-topology MAPE range\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Per-topology MAPE range 已在论文中报告。Round 2-3 未再提及。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号正文-附录不一致\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"双方 AGREE。\"\n      - round: 2\n        reviewers: [R2]\n        note: \"R2 建议符号表。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1 小问题：τ 和 β_T 交替使用，Proposition 编号不一致。R2 AGREE。Appendix D 现有 notation table (Table 8) 但正文仍有不一致。\"\n    action_items:\n      - round: 3\n        action: \"统一正文 τ/β_T 记号；添加正文-附录 Proposition 交叉引用\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 2 issues — status updates for Round 3 ===\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification stress test 覆盖面\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"建议扩展至 confounding+mediation+exposure+IV × K=3,10。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1-W1/R2-W3: Appendix B.4 已扩展至 96 configurations (4 topologies × 2K × 3 CM × 4 ε)，但正文 Definition 1 的实践讨论仍不足——何时 LLM 满足 non-differential？R2 补充 stress test 基础版仅 exposure 拓扑不够。R1 建议讨论具体 NLP 场景（sentiment vs stance detection）。\"\n    action_items:\n      - round: 2\n        action: \"扩展 stress test\"\n        assigned_to: agent\n        status: done\n      - round: 3\n        action: \"(1) 正文 Method 或 Related Work 讨论 non-differential 假设成立/失败的具体 NLP 场景；(2) Stress test 覆盖更多拓扑\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) TACL 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"R2 提出，R1 AGREE。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被提及。Related Work 已引用 feder_etal2022 和 cheng_mayya_sedoc2024。确认已修复。\"\n    action_items:\n      - round: 2\n        action: \"补充 Feder et al. (2022) 和 Cheng et al. (2024) 引用\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Related Work 已包含两篇引用。Round 3 未再提及。\"\n    resolution_round: 3\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"仅 500 scenarios 远少于 Empirical Finding 1 的 100,000。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被提及。Appendix C (Table 9) 现报告 10,000 random C₀ per topology per K ∈ {3,5,7} + 500-restart adversarial search。规模已充分。确认已修复。\"\n    action_items:\n      - round: 2\n        action: \"增加 Conjecture 1 验证到 10,000 random + adversarial search\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Appendix C 现包含 210,000 total matrices (10,000 × 7 topologies × 3 K values) + adversarial search。Round 3 未再提及。\"\n    resolution_round: 3\n\n  # === Round 3 新增 issues ===\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制约 0.5 页\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"双方均列为 critical。Section 5 (Conclusion) 在第 9 页开始。main.tex 已使用 \\\\enlargethispage 和压缩 \\\\floatsep 但仍超限。ARR desk rejection 风险。建议压缩 Section 4（Cross-K robustness 和 ASV diagnostic 移至附录）或缩小 Figure 1+2。\"\n    action_items:\n      - round: 3\n        action: \"压缩正文至 8 页以内：(1) Section 4 部分段落移至附录；(2) Figure 1+2 缩小或合并；(3) Section 2 Related Work 精简\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1 列为 N3 critical：'matrix-based correction' 精确定义缺失，SIMEX 0% reduction 需解释，与 Carroll et al. (2006) 关系需澄清。R2 REBUT 降为 should-fix：FWL invariance 是 FWL 定理的 direct corollary（3 行推导），C⁻¹ 不改变 column space，projection matrix 不变，T 系数不变。分歧：R1 要求 formal proof，R2 认为 writing clarity 即可。\"\n    action_items:\n      - round: 3\n        action: \"(1) 添加 'matrix-based correction' 的 precise definition；(2) 写出 3-4 行 FWL 推导；(3) 解释 SIMEX 0% reduction 为何不矛盾；(4) 讨论与 Carroll et al. (2006) residual confounding 的关系\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R2-W4 首发，R1 AGREE。NLP 因果研究中 Y 也可能是 LLM 标注的。OLS 下 outcome misclassification 仅增加方差，但非线性模型下会产生偏倚。至少在 Limitations 中讨论。\"\n    action_items:\n      - round: 3\n        action: \"Limitations 添加 outcome misclassification 段落\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 信息过载（15+ 数字）\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R2-W5 首发，R1 AGREE。Abstract 包含 83.4%, 52.6%, 13.7%, 2.1%, 47.0%, 88%, 61% 等 15+ 数字，读起来像 results dump 而非 motivated preview。建议保留 3-5 个最关键数字。\"\n    action_items:\n      - round: 3\n        action: \"Abstract 精简至 3-5 个核心数字，其余移入正文\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"双方 AGREE 缺少：(1) Cinelli & Hazlett (2020) 'Making Sense of Sensitivity'——与 ASV 直接可比；(2) Gilardi et al. (2023) ChatGPT annotation；(3) Ziems et al. (2024) LLM+CSS survey；(4) Bound, Brown & Mathiowetz (2001) survey measurement error；(5) Bayesian ME model 具体引用（Gustafson 2004 具体章节或 Richardson & Gilks 1993）。\"\n    action_items:\n      - round: 3\n        action: \"Related Work 补充 5 篇引用并讨论与本文关系\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R2-W6 首发，R1 AGREE。方法论论文含大量仿真实验，代码公开是 ARR 评审标准预期。ASV 计算工具作为 package 发布可大幅提升实用价值。\"\n    action_items:\n      - round: 3\n        action: \"论文中承诺公开代码，或在 supplementary 中提供\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1-W4 首发，R2 partially agrees。K≥3 sign reversal 已被 Dosemeci (1990) 和 Veierød & Laake (2001) 指出；residual confounding 在 Greenland (2003) 和 Ogburn & VanderWeele (2012) 中已分析。论文应明确：'以下已知：...。我们的新贡献：(1) 系统性 7 拓扑对比；(2) ASV 框架；(3) FWL invariance 对 correction 的影响'。R2 认为这是 framing 改进而非 novelty 不足。\"\n    action_items:\n      - round: 3\n        action: \"Introduction 或 Related Work 添加 1-2 句明确的 novelty delineation\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1-W5 首发，R2 partially agrees。'Empirical validation' 用真实 CM 但应用于模拟 DGP（线性 SEM），验证的是推导正确性而非实践指导价值。ClinicalBERT case study (Appendix B.2) 是回顾性应用。R2 认为这是方法论论文标准做法，但同意完整 real-world case study 会增强说服力。\"\n    action_items:\n      - round: 3\n        action: \"考虑将 Appendix B.2 case study 扩展并移入正文；或增加 semi-synthetic 实验\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c40ed250-ffaa-418b-addb-15f4f0d6d790",
  "isSidechain": false,
  "requestId": "req_011CbHj1U2tEQhXrYD2FLHH7",
  "type": "assistant",
  "uuid": "e5cb9e4d-4fb6-4464-b2f2-5e102c59faba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiPRiKXjZyd12EVcbxD3Fe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6431,
      "cache_read_input_tokens": 107193,
      "output_tokens": 11002,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11002,
          "cache_read_input_tokens": 107193,
          "cache_creation_input_tokens": 6431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6431
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

_source line 129 · 2026-05-22T14:01:32.021Z_

<details><summary>↩ Tool result · `toolu_01VU6tgZeXxQbLZ5ov7vMz1g`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\", \"bytes\": 18772}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5cb9e4d-4fb6-4464-b2f2-5e102c59faba",
  "isSidechain": false,
  "promptId": "35007fc4-a558-4c2b-a533-ce1f9088b4a3",
  "type": "user",
  "uuid": "894d3a15-6be9-4271-bd27-47c959349c20",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\\\", \\\"bytes\\\": 18772}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\", \"bytes\": 18772}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "e5cb9e4d-4fb6-4464-b2f2-5e102c59faba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 130_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Reviewer 2 审稿意见]: ## Reviewer 2 交叉回应 — 逐条回应 Reviewer 1 审稿意见  ---  ### Must-Fix 问题  **[AGREE] R1-N1: Theorem 1 适用范围过窄，Conjecture 1 缺乏证明**  同意这是一个实质性问题。我在自己的审稿中将其列为 W2（should-fix），但 R1 将其提升到 critical 也…",
  "leafUuid": "894d3a15-6be9-4271-bd27-47c959349c20",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Runtime record

_source line 131_

```json
{
  "type": "ai-title",
  "aiTitle": "Review causal annotation error attribution paper",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Assistant

_source line 132 · 2026-05-22T14:01:35.630Z_

Issue tracker 已更新。现在提交合并审稿报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "894d3a15-6be9-4271-bd27-47c959349c20",
  "isSidechain": false,
  "requestId": "req_011CbHjHFWGLwbubMZzZ7gmP",
  "type": "assistant",
  "uuid": "94ebe7d5-593d-4ceb-b6c1-199b6dc56311",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PsEsLVPAn6CzEZL4y8wJjS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11076,
      "cache_read_input_tokens": 113624,
      "output_tokens": 6818,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11076,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6818,
          "cache_read_input_tokens": 113624,
          "cache_creation_input_tokens": 11076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11076
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

_source line 133 · 2026-05-22T14:04:11.042Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director · `toolu_01MVUmuDtqRfnAVSXcMy27PY`</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "reviewer_ids_acknowledged": [
    1,
    2
  ],
  "cross_response_reviewer_ids": [
    1,
    2
  ],
  "overall_score": "3.5 - Borderline Conference",
  "report": "# Round 3 合并审稿报告\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (via ARR), Long Paper\n**Reviewers**: R1（方法严谨性）, R2（新颖性+完整性+写作+格式）\n**审稿模式**: Fresh（重新审稿）\n\n---\n\n## Summary\n\n本文系统研究了 K 类（K≥3）非差异误分类在七种典型因果 DAG 拓扑下的偏差传播。核心发现：(1) K=2 时二分类变量的 attenuation-toward-null 保证在 K≥3 时结构性崩塌——exposure 和 IV 拓扑可产生符号反转；(2) 其余五种拓扑维持符号保持（confounding 和 collider 有解析证明，mediation/M-bias/front-door 有数值验证）；(3) 提出 Annotation Sensitivity Values (ASV) 框架量化各拓扑的脆弱性光谱；(4) 证明 Frisch-Waugh-Lovell 不变性导致矩阵校正方法对 4/7 拓扑无效；(5) 通过真实 LLM confusion matrix 的经验验证确认理论预测。\n\n---\n\n## Strengths\n\n**S1** [共识] **重要且及时的问题**。LLM 标注在计算社会科学中快速普及，标注误差对因果推断的影响是紧迫问题。本文提供了首个系统性框架。\n\n**S2** [共识] **K≥3 代数断点的刻画**。证明 K=2 的符号保持保证在 K≥3 时因混淆矩阵高维自由度而结构性崩塌，这是一个非平凡的定性结果，对实践者有直接指导意义。\n\n**S3** [共识] **FWL 不变性的实用洞察**。揭示矩阵校正方法（naive plug-in, MLA）对 4/7 拓扑 provably 无效，文献中长期被忽视，对实践者直接可操作。\n\n**S4** [共识] **ASV 框架的可操作性**。提供参数化的敏感性分析工具，类比 E-values 但针对标注误差，包含三种互补度量（magnitude/significance/sign-flip），实用价值明确。\n\n**S5** [共识] **系统覆盖面**。7 DAG 拓扑 × 5 校正方法 × 多种验证方式（100,000 随机矩阵 + 4 LLM × 3 数据集 + logistic DGP + case study），覆盖面全面。\n\n**S6** [共识] **附录质量高**。12 页附录包含详细 Lemma-Proposition 证明链、stress test、bootstrap ASV 分析、case study，质量高于多数投稿。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [共识, critical] **正文超出 8 页限制约 0.5 页**\nSection 5 (Conclusion) 在第 9 页开始，正文约 8.3 页。EMNLP 2026 Long Paper 严格限制 8 页正文（不含 References 和 Limitations）。main.tex 已使用 `\\enlargethispage` 和压缩 `\\floatsep` 等手段但仍超限。这是 ARR desk rejection 条件之一。\n- *建议*：压缩 Section 4（Cross-K robustness 段和 ASV diagnostic results 段可移至附录）；Figure 1+2 占满整页，考虑缩小或合并；精简 Section 2 Related Work。\n\n**N2** [共识, critical] **Sign reversal 严重性被过度声称**\nAbstract 和 Introduction 以 Dirichlet(1,1,1) 全参数空间的 83.4% sign reversal 为主导叙事，辅以 \"catastrophic\" 等极端措辞。但：(1) Dirichlet(1,1,1) 包含大量不现实的非对角占优矩阵（平均准确率 1/K）；(2) 在实际 LLM 分类器精度下（diagonal ≥ 0.7），sign reversal 降至 2.1%；(3) 论文 Section 4.4 自身明确写道 \"The primary coefficient (β₁, largest magnitude) never reverses across any empirical configuration; sign flips occur exclusively in secondary coefficients corresponding to rare categories with small |β|\"。Section 4.2 的 \"catastrophic sign reversal\" 小标题与 Section 4.4 的实证结果自相矛盾。\n- R1 补充：理论上任何系数 CAN reverse 的结论本身有价值，建议调整为 \"sign reversal is theoretically possible for K≥3, practically rare for primary coefficients under realistic classifiers, but non-negligible for secondary coefficients\"\n- *建议*：(1) Abstract 先报告 realistic regime (diagonal ≥ 0.7, 2.1% sign reversal)，再提 Dirichlet 83.4% 作为理论上界；(2) 明确说明 empirical sign reversal 限于 secondary coefficients；(3) 用 \"structurally possible\" 替代 \"catastrophic\"\n\n**N3** [R1 critical, R2 should-fix, 分歧] **Theorem 1 适用范围过窄，Conjecture 1 未证明**\nTheorem 1 仅覆盖 confounding + proportional effects（f = λg）。其余 6 个非 IV 拓扑的 ASV 单调性依赖 Conjecture 1，而 Table 9 显示 60-97% 的随机矩阵违反严格单调性（虽然违反幅度 < 0.06）。如果单调性不成立，ASV 的 \"临界 δ 阈值\" 语义变得模糊。\n- R1 立场：ASV 是论文核心实用贡献，其理论基础不应仅依赖 numerical verification → must-fix\n- R2 立场：ASV 核心价值在于 topology ranking，ranking 在所有实验中成立，不完全依赖严格单调性；ε < 0.06 足够小 → should-fix\n- *建议*：(1) 至少证明 mediation 的单调性（Eq.3 结构较简单）；(2) 给出 ε 关于 K 和 DGP 参数的 formal bound；(3) 明确讨论 Conjecture 失败时 ASV interpretation 如何 degrade\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [共识] **3/5 sign preservation 拓扑 \"establish\" 措辞过度**\nAbstract 用 \"establish that five topologies show no sign reversal\"，但 mediation/M-bias/front-door 仅有 100,000 随机矩阵的数值验证（Empirical Finding 1），附录明确写 \"analytic proofs for general K remain open\"。\"Establish\" 暗示证明而非验证。\n- *建议*：改为 \"prove for confounding and collider, and verify numerically for mediation, M-bias, and front-door\"\n\n**W2** [R1 critical, R2 should-fix, 分歧] **FWL invariance 结论缺乏 precise statement**\n论文声称 \"matrix-based corrections achieve exactly 0% bias reduction\" 对 4 个 FWL 拓扑成立，但：(a) \"matrix-based correction\" 无精确定义；(b) SIMEX 的 0% reduction 与其理论上应能外推的预期矛盾，需解释；(c) 与 Carroll et al. (2006) 已知 residual confounding 结果的关系未澄清。\n- R1 立场：缺 formal proof，无法区分深刻洞察 vs 实验 artifact → must-fix\n- R2 立场：FWL invariance 是 FWL 定理的 direct corollary（C⁻¹ 不改变 column space → projection matrix 不变 → T 系数不变），3 行推导即可，是 writing clarity 问题 → should-fix\n- *建议*：添加 precise definition + 3-4 行 FWL 推导 + SIMEX 解释 + Carroll (2006) 关系讨论\n\n**W3** [共识] **Non-differential misclassification 假设讨论不足**\nLLM 处理包含 Y 和 Z 信息的文本，P(A*|A,Y,Z) = P(A*|A) 在许多场景中不成立。Appendix B.4 的 extended stress test 覆盖 96 configurations（4 topologies × 2K × 3 CM × 4ε），但正文 Method 部分未讨论何时 LLM 满足此假设（如 LLM 未见 outcome 文本时）。\n- *建议*：(1) 正文讨论具体 NLP 场景（sentiment vs. stance detection）；(2) stress test 进一步覆盖 confounding 拓扑\n\n**W4** [共识] **线性 SEM 假设限制实用性**\n所有结果基于线性结构方程。论文自身承认 \"FWL invariance result does not hold for logistic regression\"——Algorithm 1 的 FWL 分流建议在非线性设定下可能失效，但 Algorithm 1 未标注此 caveat。Appendix B.6 的 logistic DGP robustness check 仅覆盖 3/7 拓扑。\n- *建议*：(1) Algorithm 1 标注 \"linear models only\"；(2) 扩展 Appendix B.6 至全部 7 拓扑\n\n**W5** [共识] **缺少 outcome misclassification 讨论**\n许多 NLP 因果研究中 Y 也由 LLM 标注。至少在 Limitations 中讨论 outcome misclassification 的影响和扩展方向。\n\n**W6** [共识] **Abstract 信息过载**\nAbstract 包含 15+ 个具体数字（83.4%, 52.6%, 13.7%, 2.1%, 47.0% 等），影响可读性。\n- *建议*：保留 3-5 个最关键数字，其余移入正文\n\n**W7** [共识] **未承诺代码/数据公开**\n方法论论文含大量仿真实验，代码公开是 ARR 标准预期。ASV 计算工具作为 package 发布可大幅提升实用价值。\n\n**W8** [R1 warning, R2 partially agrees] **新颖性定位不清**\nK≥3 sign reversal 已被 Dosemeci (1990) 和 Veierød & Laake (2001) 指出；residual confounding 在 Greenland (2003) 和 Ogburn & VanderWeele (2012) 中已分析。论文应明确界定 \"已知结果在 LLM 语境的应用\" vs \"真正新贡献\"。R2 认为这是 framing 改进而非 novelty 不足。\n\n**W9** [R1 warning, R2 partially agrees] **经验验证使用模拟 DGP 而非真实因果数据**\n\"Empirical validation\" 用真实 LLM confusion matrices 但应用于模拟 DGP（线性 SEM），验证的是推导正确性而非实践指导价值。R2 认为这是方法论论文标准做法，但同意完整 real-world case study 会增强说服力。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上达成共识：\n1. **[AGREE]** 正文超 8 页限制 — 双方 critical\n2. **[AGREE]** Sign reversal 83.4% framing overclaiming — 双方同意需调整叙事（R2 critical, R1 upgraded after cross-sharing）\n3. **[AGREE]** Non-differential 假设讨论不足 — 双方 warning\n4. **[AGREE]** 线性 SEM 限制 + Algorithm 1 缺 caveat — 双方 warning\n5. **[AGREE]** Abstract 信息过载 — 双方 warning\n6. **[AGREE]** 代码公开 — 双方 warning\n7. **[AGREE]** 3/5 拓扑 \"establish\" 措辞过度 — 双方 warning\n8. **[AGREE]** Outcome misclassification 缺讨论 — 双方 warning\n9. **[AGREE]** 所有 6 条优势 — 双方一致\n10. **[AGREE]** 新颖性评估：相对 Teblunthuis (2024) 和 Lee & Wood-Doughty (2024) 增量充分；ASV 创新中等；FWL invariance 实用价值高；topology-dependent 视角足够\n11. **[AGREE]** 缺少 Cinelli & Hazlett (2020)、Gilardi et al. (2023)、Ziems et al. (2024) 等引用\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 分歧性质 |\n|------|----|----|----------|\n| Conjecture 1 严重性 | N1 must-fix | W2 should-fix | 严重性分歧：R1 认为 ASV 理论基础需保障，R2 认为 ranking 结论不受影响 |\n| FWL invariance 证明 | N3 must-fix | Should-fix (writing) | 定性分歧：R1 要求 formal proof，R2 认为是 FWL 的 direct corollary 仅需改善表述 |\n| 模拟 DGP 验证 | W5 warning | Partially agrees | R1 要求 semi-synthetic 实验，R2 认为方法论论文标准做法 |\n| C(δ) 参数化唯一性 | — | Q4 (question) | R1 rebut：线性路径是自然选择但应讨论替代方案（唯一 REBUT 点） |\n\n---\n\n## Questions（需要作者澄清）\n\n1. 在 realistic regime（diagonal ≥ 0.7）下 sign reversal rate 仅 2.1%，为何 abstract 选择以 83.4% 作为主要数字？\n2. Empirical Finding 1（mediation, M-bias, front-door 的 sign preservation）是否有解析证明进展？如果这 3 个拓扑的保证只是 conjectural，论文核心 claim \"five topologies maintain structural guarantee\" 的可信度如何评估？\n3. 论文是否计划公开代码和 ASV 计算工具？\n4. Algorithm 1 在非线性模型（如 logistic regression）下是否仍然有效？FWL 分流分支的适用范围应如何界定？\n5. C(δ) = (1-δ)I + δC₀ 线性参数化的选择理由是什么？如果实际退化路径不在此线上，ASV 的意义如何？\n\n---\n\n## Missing References\n\n1. **Cinelli & Hazlett (2020)** \"Making Sense of Sensitivity: Extending Omitted Variable Bias\" — 与 ASV 框架有直接可比性（robustness value vs ASV），应在 Section 2 或 3.3 中讨论对比 [双方 AGREE]\n2. **Gilardi et al. (2023)** \"ChatGPT Outperforms Crowd-Workers for Text-Annotation Tasks\" — LLM 标注的标志性论文 [双方 AGREE]\n3. **Ziems et al. (2024)** \"Can Large Language Models Transform Computational Social Science?\" — 综合 survey，与论文 motivation 直接相关 [双方 AGREE]\n4. **Bound, Brown & Mathiowetz (2001)** — Survey data 中 measurement error 经典综述 [双方 AGREE]\n5. **Bayesian measurement error models 具体引用**（如 Richardson & Gilks 1993, Gustafson 2004 具体章节）— Section 4.5 提及但未引用具体工作 [双方 AGREE]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 因配额限制（rate limit）执行失败，未产出排版审查结果。建议用户可手动触发重试。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference**\n\n**Soundness: 3.5/5** — 核心 bias 表达式和已有证明（Theorem 1, Propositions for confounding/collider）正确；但 Conjecture 1 未证明、3/5 sign preservation 仅有数值验证、FWL invariance 表述不够 precise。\n\n**Excitement: 3.25/5** — Topology-dependent 视角是足够的概念创新，ASV 框架可操作，FWL invariance 被忽视但重要；但理论深度中等（Conjecture 而非 Theorem），ASV 是 E-value 的自然类比，K≥3 break 本身已被 Dosemeci (1990) 指出。\n\n**Reproducibility: 4/5** — 数学公式清晰，DGP 参数详细，附录证明完整；但未承诺代码公开。\n\n**Confidence: 4/5** — 两位 Reviewer 均熟悉测量误差理论和因果推断文献，逐页仔细阅读含附录。\n\n**总体判断**：这是一篇重要且及时的方法论工作，系统性 taxonomy 和 ASV 框架有明确的实用价值。主要不足在于：(1) 格式问题（超页，desk rejection 风险）；(2) framing 过度声称（83.4% vs 2.1%，\"catastrophic\" vs secondary coefficients only）；(3) 理论完备性中等（Conjecture 未证明，部分 sign preservation 仅数值验证）。如果格式和 framing 问题能在修订中解决，论文有潜力达到 Conference (4.0) 水平；如果 Conjecture 1 能至少部分证明，理论贡献将显著增强。当前版本处于 Borderline Conference / Findings 交界。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"catastrophic\" 措辞与 Section 4.4 实证结果不符——primary coefficient 从未反转\n- 建议添加 1-2 句 novelty delineation：\"The possibility of polytomous sign reversal was noted by Dosemeci et al. (1990); our contribution is the first systematic characterization across multiple DAG topologies and the ASV framework for quantifying this vulnerability.\"\n\n### Section 2 (Related Work)\n- 缺少 Cinelli & Hazlett (2020) 与 ASV 的对比讨论\n- 缺少 Gilardi et al. (2023) 和 Ziems et al. (2024) 作为 LLM annotation 动机引用\n- 可精简以节省页面空间\n\n### Section 3.2 (Bias Expressions)\n- Proposition 1 中 \"establish\" 措辞对 mediation/M-bias/front-door 过度——应区分 \"proven\" vs \"numerically verified\"\n- Empirical Finding 1 的条件涉及未知 DGP 参数，实践中难以事前验证——论文已提 ASV 作为替代，但可进一步讨论\n\n### Section 3.3 (ASV Framework)\n- Theorem 1 限于 proportional effects——应讨论此假设何时成立/失败\n- Conjecture 1：60-97% 矩阵违反严格单调性但幅度 < 0.06——应更诚实地讨论\n- C(δ) 线性参数化的选择应讨论替代方案（matrix exponential, Dirichlet-based）\n\n### Section 4 (Experiments)\n- Section 4.2 \"catastrophic sign reversal\" 小标题与 Section 4.4 结果矛盾\n- Cross-K robustness 和 ASV diagnostic 段可移至附录以节省空间\n- \"grand MAPE of 2.0% across 126 scenarios (18 LLM configurations × 7 topologies)\" 的 126 = 18×7 推导出现在 Monte Carlo 验证段，容易与 empirical validation 混淆\n\n### Section 4.5 (Correction Guidance)\n- \"matrix-based correction\" 需 precise definition\n- FWL invariance 需 3-4 行推导而非仅引用实验结果\n- SIMEX 对 FWL 拓扑的 0% reduction 需解释为何不矛盾\n- Algorithm 1 需标注 \"linear models only\" caveat\n- Bayesian ME models 作为 FWL bypass 方案需引用具体工作\n\n### Section 5 (Conclusion)\n- 溢出到第 9 页——压缩或部分合入 Limitations\n\n### Limitations\n- 应增加 outcome misclassification 讨论\n- Non-differential 假设的适用场景应更具体\n\n### 附录\n- 符号表（Table 8）存在但正文 τ/β_T 仍不一致\n- Proposition 编号在正文与附录间缺乏交叉引用\n- Figure 2 y 轴标签偏小，影响打印可读性\n\n### 跨轮次 Issue 追踪\n本轮为 Round 3 fresh 审稿。以下先前 issue 已确认修复：\n- R1-N3 (ASV δ 定义域) — Section 3.3 引入 δ_max 约束 ✓\n- R2-N2 ('first systematic framework' overclaim) — Abstract 已改为 'a systematic framework' ✓\n- R2-N3 (4 篇缺失引用) — Related Work 已恢复 ✓\n- R2-W2 (zero reversals vs narrative tension) — Triple verification narrative 已改善 ✓\n- R2-W3 (ASV bootstrap uncertainty) — Appendix B.5 已包含 B=1,000 bootstrap 分析 ✓\n- NEW-2 (Feder et al. 2022, Cheng et al. 2024) — Related Work 已引用 ✓\n- NEW-3 (Conjecture 1 验证规模) — Appendix C 已扩展至 210,000 matrices ✓\n\n以下 issue 持续存在或新增：\n- R1-N1 (Theorem 1/Conjecture 1) — 持续 open（Round 1-3）\n- R1-N2 (3/5 拓扑 \"establish\" 措辞) — 持续 open（Round 1-3）\n- R2-N1 (83.4% framing) — 持续 open 且新增 secondary coefficient 维度（Round 1-3）\n- R3-NEW-1 ~ R3-NEW-8 — 本轮新增 8 个 issue\n\n完整 issue tracker 见 `artifacts/review_issues.yaml`。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94ebe7d5-593d-4ceb-b6c1-199b6dc56311",
  "isSidechain": false,
  "requestId": "req_011CbHjHFWGLwbubMZzZ7gmP",
  "type": "assistant",
  "uuid": "dece7f42-46f8-4f8a-8d02-9fd3f85cbfe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PsEsLVPAn6CzEZL4y8wJjS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11076,
      "cache_read_input_tokens": 113624,
      "output_tokens": 6818,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11076,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6818,
          "cache_read_input_tokens": 113624,
          "cache_creation_input_tokens": 11076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11076
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

_source line 134 · 2026-05-22T14:04:15.297Z_

<details><summary>↩ Tool result · `toolu_01MVUmuDtqRfnAVSXcMy27PY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dece7f42-46f8-4f8a-8d02-9fd3f85cbfe3",
  "isSidechain": false,
  "promptId": "35007fc4-a558-4c2b-a533-ce1f9088b4a3",
  "type": "user",
  "uuid": "0b53f258-41a0-4c0a-b180-db9568ab253e",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"research_director_key\\\": \\\"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "dece7f42-46f8-4f8a-8d02-9fd3f85cbfe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 135_

```json
{
  "type": "ai-title",
  "aiTitle": "Review causal annotation error attribution paper",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

### Runtime record

_source line 136 · 2026-05-22T14:04:34.492Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T14:04:34.492Z",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "content": "[Reviewer 2 审稿结果]:\n交叉回应已提交。两位 reviewer 在 Overall 3.5、页数超限、overclaiming 等核心问题上高度一致，主要分歧在 FWL invariance 的严重性评估（R1 视为 critical missing proof，我视为 writing clarity issue）。"
}
```

---

### Runtime record

_source line 137 · 2026-05-22T14:04:34.492Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T14:04:34.492Z",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4"
}
```

---

## Round 11

2 recorded events

### User

_source line 138 · 2026-05-22T14:04:34.481Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b53f258-41a0-4c0a-b180-db9568ab253e",
  "isSidechain": false,
  "promptId": "e7e4107a-3229-4b01-9fbf-cae6fcee49d9",
  "type": "user",
  "isMeta": true,
  "uuid": "d6551108-1f87-4be8-a0fe-1bddda7caaf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 139 · 2026-05-22T14:04:34.481Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6551108-1f87-4be8-a0fe-1bddda7caaf4",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "8c4bfbe4-f095-4697-bcba-1b6fb2ef1dee",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "id": "e31c3bf6-197d-4e06-aec5-92fa0ee3b8b0",
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

## Round 12

2 recorded events

### User

_source line 140 · 2026-05-22T14:04:34.597Z_

[Reviewer 2 审稿结果]:
交叉回应已提交。两位 reviewer 在 Overall 3.5、页数超限、overclaiming 等核心问题上高度一致，主要分歧在 FWL invariance 的严重性评估（R1 视为 critical missing proof，我视为 writing clarity issue）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c4bfbe4-f095-4697-bcba-1b6fb2ef1dee",
  "isSidechain": false,
  "promptId": "e7e4107a-3229-4b01-9fbf-cae6fcee49d9",
  "type": "user",
  "uuid": "d441e1ce-a3b7-4ed8-bc5b-fbe1fbe7dfcc",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 141 · 2026-05-22T14:04:34.596Z_

```json
{
  "parentUuid": "d441e1ce-a3b7-4ed8-bc5b-fbe1fbe7dfcc",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "752fc6a5-15d4-41e3-9428-e32126b7f07f",
  "timestamp": "2026-05-22T14:04:34.596Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be",
  "sessionId": "c928a4cc-3e3f-4de1-bdfb-f994449906a4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---
