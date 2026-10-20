# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T153939 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/5478faf0-d6f0-4310-8fd0-e2717487d58c.jsonl`
- **Structured JSON:** [`b63e0f86b9fcb817afcf.json`](../../sessions/b6/b63e0f86b9fcb817afcf.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T15:56:29.079Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T15:56:29.079Z",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T153939 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260516T153939/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260516T153939/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260516T153939/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260516T153939/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：原始framing完全成立——'Structured error injection is fundamentally destabilizing for embodied planning across architectures'。论文贡献从negative result升级为positive finding about injection stability properties。重点：(1)跨模型SD ratio 4:1证明是structured patterns的内在属性；(2)dose-response inverted-U揭示conflicting signal mechanism；(3)recovery=resilience是对整个error-injection-for-recovery范式的conceptual challenge。无需调整claims强度。\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260516T153939/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T15:56:29.083Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T15:56:29.083Z",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c"
}
```

---

## Round 1

30 recorded events

### User

_source line 3 · 2026-05-16T15:56:29.105Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T153939 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260516T153939/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260516T153939/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260516T153939/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260516T153939/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：原始framing完全成立——'Structured error injection is fundamentally destabilizing for embodied planning across architectures'。论文贡献从negative result升级为positive finding about injection stability properties。重点：(1)跨模型SD ratio 4:1证明是structured patterns的内在属性；(2)dose-response inverted-U揭示conflicting signal mechanism；(3)recovery=resilience是对整个error-injection-for-recovery范式的conceptual challenge。无需调整claims强度。
- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260516T153939/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e9664e84-37e7-4492-8360-bef898696842",
  "type": "user",
  "uuid": "c536fccf-0511-4bdc-8ec1-f7b4b02279bc",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T15:56:29.104Z_

```json
{
  "parentUuid": "c536fccf-0511-4bdc-8ec1-f7b4b02279bc",
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
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
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
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "9f70243a-6a9f-4e8a-8523-3ae19f175a3a",
  "timestamp": "2026-05-16T15:56:29.104Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T15:56:29.104Z_

```json
{
  "parentUuid": "9f70243a-6a9f-4e8a-8523-3ae19f175a3a",
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
  "uuid": "479d897c-a9aa-4114-b0bf-ab264965529f",
  "timestamp": "2026-05-16T15:56:29.104Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-16T15:56:29.104Z_

```json
{
  "parentUuid": "479d897c-a9aa-4114-b0bf-ab264965529f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "6e15ab28-af46-4522-aeb5-36d27b844a0e",
  "timestamp": "2026-05-16T15:56:29.104Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c",
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
  "aiTitle": "Generate simulated research paper from experiment data",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c"
}
```

---

### Assistant

_source line 8 · 2026-05-16T15:56:33.287Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the experiment data and paper framing files to understand what I need to write.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e15ab28-af46-4522-aeb5-36d27b844a0e",
  "isSidechain": false,
  "requestId": "req_011Cb6XCAssrVsW8naDEJ31x",
  "type": "assistant",
  "uuid": "baeb3381-f724-46ed-9cc2-d71fa3301aa8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019cFDEXs9Ycr9zZL43Ghkox",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11585,
      "cache_read_input_tokens": 11447,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 229,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11585
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

_source line 9 · 2026-05-16T15:56:34.269Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LMLBBKh2DE6zVUxvHpYz95`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260516T153939/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "baeb3381-f724-46ed-9cc2-d71fa3301aa8",
  "isSidechain": false,
  "requestId": "req_011Cb6XCAssrVsW8naDEJ31x",
  "type": "assistant",
  "uuid": "348c8ab2-f627-4930-ab67-7f8e48c3cf87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019cFDEXs9Ycr9zZL43Ghkox",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11585,
      "cache_read_input_tokens": 11447,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 229,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11585
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

_source line 10 · 2026-05-16T15:56:34.497Z_

<details open><summary>🔧 Tool call — Read · `toolu_014r6tgtFakSKcEHjfBnwx4c`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260516T153939/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "348c8ab2-f627-4930-ab67-7f8e48c3cf87",
  "isSidechain": false,
  "requestId": "req_011Cb6XCAssrVsW8naDEJ31x",
  "type": "assistant",
  "uuid": "36101591-4682-49a9-8770-f4123ba1cd56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019cFDEXs9Ycr9zZL43Ghkox",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11585,
      "cache_read_input_tokens": 11447,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 229,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11585
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

_source line 11 · 2026-05-16T15:56:34.572Z_

<details><summary>↩ Tool result · `toolu_01LMLBBKh2DE6zVUxvHpYz95`</summary>

```text
1	[
2	  {
3	    "name": "Recovery Eval Multi-Seed (5-seed × 3 conditions)",
4	    "description": "对Vanilla/TaxEI/Random全部5个seed运行recovery eval（injected error条件下47 tasks），验证recovery≈resilience假说跨seed稳健性，并确认per-operator pattern方向一致性",
5	    "results": {
6	      "vanilla_recovery_mean": 66.1,
7	      "vanilla_recovery_sd": 5.4,
8	      "vanilla_recovery_seeds": [
9	        61.7,
10	        68.1,
11	        66.0,
12	        66.0,
13	        74.5
14	      ],
15	      "taxei_recovery_mean": 57.1,
16	      "taxei_recovery_sd": 6.8,
17	      "taxei_recovery_seeds": [
18	        59.6,
19	        46.8,
20	        61.7,
21	        61.7,
22	        57.4
23	      ],
24	      "random_recovery_mean": 57.9,
25	      "random_recovery_sd": 7.2,
26	      "random_recovery_seeds": [
27	        63.8,
28	        55.3,
29	        66.0,
30	        51.1,
31	        53.2
32	      ],
33	      "detection_rate_all": 0.0,
34	      "recovery_vs_clean_gap_vanilla_pp": 1.2,
35	      "recovery_vs_clean_gap_taxei_pp": 1.2,
36	      "recovery_vs_clean_gap_random_pp": 0.4,
37	      "per_operator_C4_advantage_replication": 3,
38	      "per_operator_C4_advantage_out_of": 5,
39	      "cohens_d_vanilla_vs_taxei_recovery": 1.42
40	    },
41	    "tables": [
42	      {
43	        "title": "Table: 5-Seed Recovery Rate vs Clean Success Rate",
44	        "columns": [
45	          "Condition",
46	          "Clean_Mean",
47	          "Recovery_Mean",
48	          "Gap_pp",
49	          "Detection_Rate",
50	          "Recovery_SD"
51	        ],
52	        "rows": [
53	          [
54	            "Vanilla",
55	            67.3,
56	            66.1,
57	            -1.2,
58	            0.0,
59	            5.4
60	          ],
61	          [
62	            "TaxEI",
63	            58.3,
64	            57.1,
65	            -1.2,
66	            0.0,
67	            6.8
68	          ],
69	          [
70	            "Random",
71	            58.3,
72	            57.9,
73	            -0.4,
74	            0.0,
75	            7.2
76	          ]
77	        ]
78	      },
79	      {
80	        "title": "Table: Per-Operator Recovery Advantage (5-seed pooled, 235 episodes)",
81	        "columns": [
82	          "Operator",
83	          "Vanilla_Rate",
84	          "TaxEI_Rate",
85	          "Random_Rate",
86	          "TaxEI_Advantage_pp"
87	        ],
88	        "rows": [
89	          [
90	            "C4_observation_masking",
91	            0.618,
92	            0.655,
93	            0.6,
94	            3.7
95	          ],
96	          [
97	            "P1_step_order_swap",
98	            0.617,
99	            0.6,
100	            0.6,
101	            -1.7
102	          ],
103	          [
104	            "C1_context_truncation",
105	            0.7,
106	            0.633,
107	            0.65,
108	            -6.7
109	          ],
110	          [
111	            "P2_sub_goal_deletion",
112	            0.667,
113	            0.55,
114	            0.583,
115	            -11.7
116	          ]
117	        ]
118	      }
119	    ],
120	    "figures": [],
121	    "analysis": "5-seed recovery data将recovery=resilience从single-seed exploratory observation提升为robust empirical finding。关键统计：paired correlation between clean rate and recovery rate r=0.96 (p<0.001, N=15 seed-condition pairs)。这是对整个error-injection-for-recovery paradigm的conceptual challenge——在embodied planning中，'recovery from errors'根本不存在作为独立能力，它就是task competence本身。Per-operator方向性（C4 local advantage, P2 global disadvantage）在5-seed pooled data中达到suggestive consistency（3/5 seeds方向一致），虽然per-seed仍由±1 task驱动，但pooled N=55-60 per operator使pattern更credible。\n\n在best档位下，recovery=resilience pattern跨seed完全复现。逻辑：如果模型只是passively ignore perturbation而非actively recover，那么recovery rate应该tracking clean eval rate而非独立变化。5-seed数据将使recovery-clean gap压缩到1-2pp以内（在noise范围内），因为每个seed的recovery rate本质上就是该seed对应checkpoint的task completion ability在稍有噪声的eval条件下的测量值。Detection rate保持0%说明没有任何training regime instill error awareness。TaxEI的recovery variance同样高（SD~6.8pp），mirror其clean eval的instability——进一步证明recovery performance完全由base task competence驱动，而非error-specific learning。Vanilla recovery mean（66.1%）vs clean mean（67.3%）gap仅1.2pp，在47-task的McNemar误差范围内。"
122	  },
123	  {
124	    "name": "LLaMA-3.1-8B Cross-Model Replication",
125	    "description": "LLaMA-3.1-8B-Instruct 3-seed完整replication（Vanilla/TaxEI/Random），验证structured injection instability是跨架构通用现象而非Qwen-specific",
126	    "results": {
127	      "llama_vanilla_recovery_mean": 73.1,
128	      "llama_vanilla_recovery_sd": 2.5,
129	      "llama_vanilla_recovery_seeds": [
130	        74.5,
131	        74.5,
132	        70.2
133	      ],
134	      "llama_taxei_recovery_mean": 69.5,
135	      "llama_taxei_recovery_sd": 8.6,
136	      "llama_taxei_recovery_seeds": [
137	        74.5,
138	        74.5,
139	        59.6
140	      ],
141	      "llama_random_recovery_mean": 76.6,
142	      "llama_random_recovery_sd": 2.1,
143	      "llama_random_recovery_seeds": [
144	        74.5,
145	        76.6,
146	        78.7
147	      ],
148	      "llama_vanilla_clean_mean": 72.3,
149	      "llama_vanilla_clean_sd": 0.0,
150	      "llama_taxei_clean_mean": 71.6,
151	      "llama_taxei_clean_sd": 8.6,
152	      "llama_random_clean_mean": 75.9,
153	      "llama_random_clean_sd": 1.2,
154	      "cross_model_taxei_sd_ratio": 4.1,
155	      "catastrophic_seed_fraction_llama": 0.33,
156	      "taxei_vs_random_sd_ratio": 4.1,
157	      "llama_detection_rate_mean": 0.27
158	    },
159	    "tables": [
160	      {
161	        "title": "Table: Cross-Model Comparison — Training Stability",
162	        "columns": [
163	          "Model",
164	          "Condition",
165	          "Mean_Recovery",
166	          "SD",
167	          "Catastrophic_Seeds",
168	          "SD_Ratio_vs_Random"
169	        ],
170	        "rows": [
171	          [
172	            "Qwen3-8B",
173	            "TaxEI",
174	            58.3,
175	            6.5,
176	            "1/5 (20%)",
177	            "0.75×"
178	          ],
179	          [
180	            "Qwen3-8B",
181	            "Random",
182	            58.3,
183	            8.7,
184	            "1/5 (20%)",
185	            "1.0×"
186	          ],
187	          [
188	            "LLaMA-3.1-8B",
189	            "TaxEI",
190	            69.5,
191	            8.6,
192	            "1/3 (33%)",
193	            "4.1×"
194	          ],
195	          [
196	            "LLaMA-3.1-8B",
197	            "Random",
198	            76.6,
199	            2.1,
200	            "0/3 (0%)",
201	            "1.0×"
202	          ]
203	        ]
204	      },
205	      {
206	        "title": "Table: LLaMA Per-Seed Results",
207	        "columns": [
208	          "Seed",
209	          "Vanilla_Recovery",
210	          "TaxEI_Recovery",
211	          "Random_Recovery",
212	          "TaxEI_Δ_vs_Vanilla"
213	        ],
214	        "rows": [
215	          [
216	            "s42",
217	            74.5,
218	            74.5,
219	            76.6,
220	            0.0
221	          ],
222	          [
223	            "s0",
224	            74.5,
225	            74.5,
226	            74.5,
227	            0.0
228	          ],
229	          [
230	            "s123",
231	            70.2,
232	            59.6,
233	            78.7,
234	            -10.6
235	          ]
236	        ]
237	      }
238	    ],
239	    "figures": [],
240	    "analysis": "Cross-model replication是从Borderline Accept升级到Findings Accept的关键evidence。Reviewers最大concern是'maybe it's just Qwen'——3-seed LLaMA data以方向一致性（而非absolute power）回答这个问题。SD ratio 4.1:1在best档下被接受为sufficient evidence because: (1) direction完全一致——两个模型都是TaxEI unstable, Random stable; (2) 具体failure mode不同但可解释——Qwen对structured bias更uniformly susceptible（可能因为较弱的pre-training robustness），LLaMA有stronger base但occasional catastrophic collapse（bimodal response to structured bias）; (3) 3-seed × 2-model = 6 independent TaxEI training runs中2个catastrophic（33%），vs 6 Random runs中0个catastrophic（0%）——这个0-vs-2 pattern本身有practical significance even without formal power。\n\nBest档核心：cross_model_taxei_sd_ratio在[3.5, 4.5]范围内，实际值4.1（TaxEI SD 8.6 / Random SD 2.1）。这个4:1的SD ratio是structured injection创造training instability的直接evidence。为什么会出现：(1) Structured patterns（taxonomy-labeled perturbations）在loss landscape中创造systematic偏移方向，某些seed的初始化恰好与这些bias方向对齐导致catastrophic amplification；(2) Random perturbations平均化为near-zero gradient bias，任何seed都不会被systematically pushed toward failure region。LLaMA s123 collapse（recovery 59.6% vs vanilla 70.2%）mirrors Qwen的consistent degradation pattern但以higher variance形式表现——不同architecture对structured bias的响应mode不同（Qwen: uniform moderate harm; LLaMA: bimodal all-or-nothing），但direction一致。LLaMA的非零detection rate（~27%）是interesting但不影响core story：LLaMA base model本身就有更强的meta-cognitive tendency（可能来自RLHF alignment），这不是training regime effect而是base model property。"
241	  },
242	  {
243	    "name": "Scale-Up Data (500→2500 Trajectories)",
244	    "description": "将训练数据从501 successful trajectories扩展到~2500，测试TaxEI failure是否由数据规模不足导致。3-seed V+T比较。",
245	    "results": {
246	      "collection_success_rate": 0.7,
247	      "total_trajectories_collected": 2487,
248	      "api_cost_usd": 44.5,
249	      "scaled_vanilla_mean": 71.2,
250	      "scaled_vanilla_sd": 3.8,
251	      "scaled_vanilla_seeds": [
252	        69.8,
253	        74.5,
254	        69.4
255	      ],
256	      "scaled_taxei_mean": 62.3,
257	      "scaled_taxei_sd": 7.4,
258	      "scaled_taxei_seeds": [
259	        66.0,
260	        55.3,
261	        65.5
262	      ],
263	      "vanilla_improvement_vs_500": 3.9,
264	      "taxei_improvement_vs_500": 5.6,
265	      "taxei_vanilla_gap_pp": -8.9,
266	      "taxei_sd_still_elevated": true,
267	      "catastrophic_seed_present": true
268	    },
269	    "tables": [
270	      {
271	        "title": "Table: Data Scale Ablation (3-seed)",
272	        "columns": [
273	          "Scale",
274	          "Condition",
275	          "Mean",
276	          "SD",
277	          "Gap_vs_Vanilla",
278	          "Catastrophic_Seeds"
279	        ],
280	        "rows": [
281	          [
282	            "500 traj (baseline)",
283	            "Vanilla",
284	            67.3,
285	            4.7,
286	            "—",
287	            "0/5"
288	          ],
289	          [
290	            "500 traj (baseline)",
291	            "TaxEI",
292	            58.3,
293	            6.5,
294	            -9.0,
295	            "1/5"
296	          ],
297	          [
298	            "2500 traj",
299	            "Vanilla",
300	            71.2,
301	            3.8,
302	            "—",
303	            "0/3"
304	          ],
305	          [
306	            "2500 traj",
307	            "TaxEI",
308	            62.3,
309	            7.4,
310	            -8.9,
311	            "1/3"
312	          ]
313	        ]
314	      }
315	    ],
316	    "figures": [],
317	    "analysis": "Scale ablation在best档下提供clean negative result：more data helps both conditions proportionally但不关闭gap。这strengthens task-structure hypothesis over data-insufficiency explanation。关键framing：'Within ALFWorld's diversity ceiling (~134 unique tasks), 5× data scaling improves absolute performance but does not resolve the structured injection instability, suggesting the failure mechanism is signal-level (conflicting gradients) rather than sample-level (insufficient coverage).' Paper中作为1段Discussion evidence，不需要占main results space。\n\n在best档下，scale-up证明data volume不是瓶颈。逻辑：(1) Vanilla从67.3%→71.2%（+3.9pp），shows正常data scaling behavior——更多clean data mildly improves task completion; (2) TaxEI也改善，从58.3%→62.3%（+5.6pp，slightly larger margin），但gap仍然是~9pp（在[8,10]范围内）且SD仍elevated（7.4pp vs 3.8pp）; (3) 1/3 seed仍然shows catastrophic behavior（55.3%），证明instability is not a small-data artifact。为什么gap维持：ALFWorld只有~134 unique tasks，即使trajectories增加到2500也只是~19/task的重复，无法提供真正的novel task diversity。Structured error patterns在任何data scale下都创造conflicting signals（正确action distribution vs injected error distribution的systematic conflict），不会被averaging out因为taxonomy labels是deterministic not stochastic。这与PALADIN的50K trajectories有qualitative difference：PALADIN的diversity来自thousands of distinct tools/APIs，而ALFWorld diversity ceiling很低。"
318	  },
319	  {
320	    "name": "Scale Ablation (25K-50K Trajectories)",
321	    "description": "假设性的extreme scale experiment——将data规模推到PALADIN级别（25K-50K trajectories）。在best档下，这个experiment如果执行会进一步confirm scale is not the fix。",
322	    "results": {
323	      "trajectories_needed": 25000,
324	      "estimated_api_cost_usd": 250,
325	      "estimated_gpu_hours": 40,
326	      "vanilla_projected_mean": 73.5,
327	      "taxei_projected_mean": 65.2,
328	      "gap_still_present_pp": -8.3,
329	      "taxei_sd_still_elevated": true,
330	      "practical_ceiling_note": "ALFWorld only has 134 unique tasks; beyond ~5K trajectories, marginal returns diminish sharply"
331	    },
332	    "tables": [
333	      {
334	        "title": "Table: Projected Scale-Performance Curve (extrapolation)",
335	        "columns": [
336	          "Scale",
337	          "Vanilla_Proj",
338	          "TaxEI_Proj",
339	          "Gap_pp",
340	          "Diminishing_Returns"
341	        ],
342	        "rows": [
343	          [
344	            500,
345	            67.3,
346	            58.3,
347	            -9.0,
348	            "—"
349	          ],
350	          [
351	            2500,
352	            71.2,
353	            62.3,
354	            -8.9,
355	            "Vanilla +3.9pp"
356	          ],
357	          [
358	            25000,
359	            "~73.5",
360	            "~65.2",
361	            "~-8.3",
362	            "Vanilla +2.3pp (saturation)"
363	          ]
364	        ]
365	      }
366	    ],
367	    "figures": [],
368	    "analysis": "Best档下这个experiment是planned but unnecessary——scale-up-data (2500) already shows the trend is flat for gap closure. Reviewers会accept 'the 9pp gap is maintained at 5× scale with no convergence trend, and ALFWorld's 134-task ceiling makes further scaling uninformative' without requiring the full 25K run. 在paper中放Discussion一段即可。\n\n在best档下，即使25K scale也不会close the gap，因为bottleneck是task diversity（134 unique tasks）而非trajectory count。当每个task有~187个trajectory variants时，model只是在memorize同一task的不同表述，而structured injection的conflicting signal per-task-template不会被additional examples resolve。这是best档而非worst档的预测——reviewers接受'we tested 2500 and the trend is clear, 25K is infeasible given ALFWorld constraints but would not help based on the non-convergence pattern'作为sufficient evidence。不需要actually run这个experiment——scale-up-data已经demonstrate the trend。"
369	  },
370	  {
371	    "name": "Recovery Prompting (Few-Shot In-Context)",
372	    "description": "给模型提供in-context recovery examples（few-shot prompting），测试是否能elicit recovery能力。如果few-shot works但fine-tuning doesn't，说明knowledge exists in the base model但training signal corrupts it。",
373	    "results": {
374	      "vanilla_with_recovery_prompt_rate": 66.0,
375	      "taxei_with_recovery_prompt_rate": 61.7,
376	      "random_with_recovery_prompt_rate": 63.8,
377	      "vanilla_base_recovery_rate": 61.7,
378	      "improvement_from_prompting_vanilla_pp": 4.3,
379	      "improvement_from_prompting_taxei_pp": 2.1,
380	      "improvement_from_prompting_random_pp": 0.0,
381	      "few_shot_detection_rate": 0.12,
382	      "prompt_design": "3 recovery exemplars showing error→detect→recover sequence"
383	    },
384	    "tables": [
385	      {
386	        "title": "Table: Recovery Prompting Ablation (seed=42)",
387	        "columns": [
388	          "Condition",
389	          "Base_Recovery",
390	          "+3-shot Recovery",
391	          "Improvement_pp",
392	          "Detection_Rate"
393	        ],
394	        "rows": [
395	          [
396	            "Vanilla",
397	            61.7,
398	            66.0,
399	            4.3,
400	            0.12
401	          ],
402	          [
403	            "TaxEI",
404	            59.6,
405	            61.7,
406	            2.1,
407	            0.08
408	          ],
409	          [
410	            "Random",
411	            63.8,
412	            63.8,
413	            0.0,
414	            0.04
415	          ]
416	        ]
417	      }
418	    ],
419	    "figures": [],
420	    "analysis": "Recovery prompting在best档下提供complementary evidence for the task-structure hypothesis。Key insight chain: (1) Detection=0% without prompting → no emergent error awareness from training; (2) Detection=12% with prompting → base model has latent capability that training didn't activate; (3) Recovery improvement modest (+4pp max) → error awareness alone insufficient when recovery requires unbounded re-planning; (4) TaxEI benefits least → injection training actively degrades the base model's latent planning ability. 这在paper中是一个clean paragraph supporting 'the failure is structural not methodological'。Priority 3 because it's supplementary——the main story stands without it。\n\n在best档下，few-shot recovery prompting shows modest improvement（+2-4pp）但远不及expected if recovery knowledge were latent。逻辑：(1) Base model（Qwen3-8B）确实有一些在pre-training中获得的generic error tolerance（vanilla本身61.7% recovery despite no injection training），few-shot可以slightly activate这个latent ability; (2) 但improvement modest因为embodied planning的error recovery是unbounded（需要re-plan entire sequence），不像tool-use那样有finite retry space——3个exemplar不能cover combinatorial space; (3) TaxEI-trained model从prompting获益更少（+2.1pp vs +4.3pp for vanilla），因为fine-tuning已经partially corrupted the base model's latent planning ability; (4) Detection rate从0%提升到12%说明explicit prompting can activate some meta-cognition，但这是surface-level mimicry不是true error awareness。这个result在best档下被framed为supplementary evidence：'even explicit in-context guidance cannot overcome the fundamental unbounded-recovery-space problem in embodied planning'。"
421	  },
422	  {
423	    "name": "Per-Operator Deep Dive (Multi-Seed Validation)",
424	    "description": "多seed per-operator recovery分析，验证C4(local) advantage和C1/P2(global) disadvantage的pattern是否robust。",
425	    "results": {
426	      "C4_observation_masking_taxei_advantage_mean_pp": 4.2,
427	      "C4_advantage_direction_consistent_seeds": 4,
428	      "C4_advantage_direction_consistent_out_of": 5,
429	      "P2_sub_goal_deletion_taxei_disadvantage_mean_pp": -9.8,
430	      "P2_disadvantage_direction_consistent_seeds": 4,
431	      "P2_disadvantage_direction_consistent_out_of": 5,
432	      "C1_context_truncation_taxei_disadvantage_mean_pp": -5.4,
433	      "P1_step_order_swap_neutral_mean_pp": -1.2,
434	      "pooled_N_per_operator": 60,
435	      "fisher_exact_C4_p": 0.38,
436	      "fisher_exact_P2_p": 0.18,
437	      "local_vs_global_pattern_consistent": true
438	    },
439	    "tables": [
440	      {
441	        "title": "Table: Per-Operator TaxEI Advantage (5-seed pooled, N=55-60 per operator)",
442	        "columns": [
443	          "Operator",
444	          "Locality",
445	          "Vanilla_Rate",
446	          "TaxEI_Rate",
447	          "Δ_pp",
448	          "Direction_Consistent_Seeds",
449	          "Fisher_p"
450	        ],
451	        "rows": [
452	          [
453	            "C4_observation_masking",
454	            "Local",
455	            0.618,
456	            0.655,
457	            3.7,
458	            "4/5",
459	            0.38
460	          ],
461	          [
462	            "P1_step_order_swap",
463	            "Mixed",
464	            0.617,
465	            0.6,
466	            -1.7,
467	            "3/5",
468	            0.82
469	          ],
470	          [
471	            "C1_context_truncation",
472	            "Global",
473	            0.7,
474	            0.633,
475	            -6.7,
476	            "4/5",
477	            0.24
478	          ],
479	          [
480	            "P2_sub_goal_deletion",
481	            "Global",
482	            0.667,
483	            0.55,
484	            -11.7,
485	            "4/5",
486	            0.18
487	          ]
488	        ]
489	      }
490	    ],
491	    "figures": [],
492	    "analysis": "Per-operator deepdive在best档下被视为论文的conceptual highlight之一——它provides mechanistic explanation for WHY structured injection fails specifically in embodied planning。The local/global gradient is the micro-level instantiation of the macro-level finding (TaxEI fails where errors cascade). Reviewers在best档下appreciate this as 'going beyond reporting negative result to explaining why it's negative'。虽然individual operator tests are NS at any reasonable α, the monotonic gradient across all 4 operators with consistent theoretical motivation (local→positive, global→negative) is accepted as convergent evidence。Paper中作为半页Analysis subsection with 1 figure。\n\n在best档下，per-operator pattern以方向一致性replicate但individual tests仍NS。逻辑：(1) C4 (observation masking) 是最local的perturbation——单个observation被mask，model只需要'ignore missing info and proceed'，这与TaxEI训练中exposure to masked observations的经验对齐，所以TaxEI能show modest advantage (+4.2pp pooled); (2) P2 (sub-goal deletion) 是最global的——删除sub-goal后整个downstream plan invalid，需要full re-planning，TaxEI训练中虽然见过P2 patterns但学到的是'execute corrupted plan'而非'detect missing goal and re-plan'，所以显著disadvantage (-9.8pp pooled); (3) C1 (context truncation) 类似P2——truncated context导致cascading wrong assumptions; (4) P1 (step order swap) 效果neutral因为swapped steps有时accidentally correct（ALFWorld很多task的step order有flexibility），所以injection训练对P1的effect被task structure的flexibility抵消。5-seed pooled到N=60/operator后方向一致但Fisher仍NS because每个operator只有12 tasks/seed，5×12=60仍然underpowered for moderate effect sizes。Best档下reviewers接受这个pattern作为hypothesis-generating evidence配合clear theoretical motivation（local=learnable, global=not learnable）。"
493	  }
494	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "348c8ab2-f627-4930-ab67-7f8e48c3cf87",
  "isSidechain": false,
  "promptId": "e9664e84-37e7-4492-8360-bef898696842",
  "type": "user",
  "uuid": "ba5a2391-50a9-4724-9f6b-158a41f8b4ff",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260516T153939/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Recovery Eval Multi-Seed (5-seed × 3 conditions)\",\n    \"description\": \"对Vanilla/TaxEI/Random全部5个seed运行recovery eval（injected error条件下47 tasks），验证recovery≈resilience假说跨seed稳健性，并确认per-operator pattern方向一致性\",\n    \"results\": {\n      \"vanilla_recovery_mean\": 66.1,\n      \"vanilla_recovery_sd\": 5.4,\n      \"vanilla_recovery_seeds\": [\n        61.7,\n        68.1,\n        66.0,\n        66.0,\n        74.5\n      ],\n      \"taxei_recovery_mean\": 57.1,\n      \"taxei_recovery_sd\": 6.8,\n      \"taxei_recovery_seeds\": [\n        59.6,\n        46.8,\n        61.7,\n        61.7,\n        57.4\n      ],\n      \"random_recovery_mean\": 57.9,\n      \"random_recovery_sd\": 7.2,\n      \"random_recovery_seeds\": [\n        63.8,\n        55.3,\n        66.0,\n        51.1,\n        53.2\n      ],\n      \"detection_rate_all\": 0.0,\n      \"recovery_vs_clean_gap_vanilla_pp\": 1.2,\n      \"recovery_vs_clean_gap_taxei_pp\": 1.2,\n      \"recovery_vs_clean_gap_random_pp\": 0.4,\n      \"per_operator_C4_advantage_replication\": 3,\n      \"per_operator_C4_advantage_out_of\": 5,\n      \"cohens_d_vanilla_vs_taxei_recovery\": 1.42\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: 5-Seed Recovery Rate vs Clean Success Rate\",\n        \"columns\": [\n          \"Condition\",\n          \"Clean_Mean\",\n          \"Recovery_Mean\",\n          \"Gap_pp\",\n          \"Detection_Rate\",\n          \"Recovery_SD\"\n        ],\n        \"rows\": [\n          [\n            \"Vanilla\",\n            67.3,\n            66.1,\n            -1.2,\n            0.0,\n            5.4\n          ],\n          [\n            \"TaxEI\",\n            58.3,\n            57.1,\n            -1.2,\n            0.0,\n            6.8\n          ],\n          [\n            \"Random\",\n            58.3,\n            57.9,\n            -0.4,\n            0.0,\n            7.2\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table: Per-Operator Recovery Advantage (5-seed pooled, 235 episodes)\",\n        \"columns\": [\n          \"Operator\",\n          \"Vanilla_Rate\",\n          \"TaxEI_Rate\",\n          \"Random_Rate\",\n          \"TaxEI_Advantage_pp\"\n        ],\n        \"rows\": [\n          [\n            \"C4_observation_masking\",\n            0.618,\n            0.655,\n            0.6,\n            3.7\n          ],\n          [\n            \"P1_step_order_swap\",\n            0.617,\n            0.6,\n            0.6,\n            -1.7\n          ],\n          [\n            \"C1_context_truncation\",\n            0.7,\n            0.633,\n            0.65,\n            -6.7\n          ],\n          [\n            \"P2_sub_goal_deletion\",\n            0.667,\n            0.55,\n            0.583,\n            -11.7\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"5-seed recovery data将recovery=resilience从single-seed exploratory observation提升为robust empirical finding。关键统计：paired correlation between clean rate and recovery rate r=0.96 (p<0.001, N=15 seed-condition pairs)。这是对整个error-injection-for-recovery paradigm的conceptual challenge——在embodied planning中，'recovery from errors'根本不存在作为独立能力，它就是task competence本身。Per-operator方向性（C4 local advantage, P2 global disadvantage）在5-seed pooled data中达到suggestive consistency（3/5 seeds方向一致），虽然per-seed仍由±1 task驱动，但pooled N=55-60 per operator使pattern更credible。\\n\\n在best档位下，recovery=resilience pattern跨seed完全复现。逻辑：如果模型只是passively ignore perturbation而非actively recover，那么recovery rate应该tracking clean eval rate而非独立变化。5-seed数据将使recovery-clean gap压缩到1-2pp以内（在noise范围内），因为每个seed的recovery rate本质上就是该seed对应checkpoint的task completion ability在稍有噪声的eval条件下的测量值。Detection rate保持0%说明没有任何training regime instill error awareness。TaxEI的recovery variance同样高（SD~6.8pp），mirror其clean eval的instability——进一步证明recovery performance完全由base task competence驱动，而非error-specific learning。Vanilla recovery mean（66.1%）vs clean mean（67.3%）gap仅1.2pp，在47-task的McNemar误差范围内。\"\n  },\n  {\n    \"name\": \"LLaMA-3.1-8B Cross-Model Replication\",\n    \"description\": \"LLaMA-3.1-8B-Instruct 3-seed完整replication（Vanilla/TaxEI/Random），验证structured injection instability是跨架构通用现象而非Qwen-specific\",\n    \"results\": {\n      \"llama_vanilla_recovery_mean\": 73.1,\n      \"llama_vanilla_recovery_sd\": 2.5,\n      \"llama_vanilla_recovery_seeds\": [\n        74.5,\n        74.5,\n        70.2\n      ],\n      \"llama_taxei_recovery_mean\": 69.5,\n      \"llama_taxei_recovery_sd\": 8.6,\n      \"llama_taxei_recovery_seeds\": [\n        74.5,\n        74.5,\n        59.6\n      ],\n      \"llama_random_recovery_mean\": 76.6,\n      \"llama_random_recovery_sd\": 2.1,\n      \"llama_random_recovery_seeds\": [\n        74.5,\n        76.6,\n        78.7\n      ],\n      \"llama_vanilla_clean_mean\": 72.3,\n      \"llama_vanilla_clean_sd\": 0.0,\n      \"llama_taxei_clean_mean\": 71.6,\n      \"llama_taxei_clean_sd\": 8.6,\n      \"llama_random_clean_mean\": 75.9,\n      \"llama_random_clean_sd\": 1.2,\n      \"cross_model_taxei_sd_ratio\": 4.1,\n      \"catastrophic_seed_fraction_llama\": 0.33,\n      \"taxei_vs_random_sd_ratio\": 4.1,\n      \"llama_detection_rate_mean\": 0.27\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Cross-Model Comparison — Training Stability\",\n        \"columns\": [\n          \"Model\",\n          \"Condition\",\n          \"Mean_Recovery\",\n          \"SD\",\n          \"Catastrophic_Seeds\",\n          \"SD_Ratio_vs_Random\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B\",\n            \"TaxEI\",\n            58.3,\n            6.5,\n            \"1/5 (20%)\",\n            \"0.75×\"\n          ],\n          [\n            \"Qwen3-8B\",\n            \"Random\",\n            58.3,\n            8.7,\n            \"1/5 (20%)\",\n            \"1.0×\"\n          ],\n          [\n            \"LLaMA-3.1-8B\",\n            \"TaxEI\",\n            69.5,\n            8.6,\n            \"1/3 (33%)\",\n            \"4.1×\"\n          ],\n          [\n            \"LLaMA-3.1-8B\",\n            \"Random\",\n            76.6,\n            2.1,\n            \"0/3 (0%)\",\n            \"1.0×\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table: LLaMA Per-Seed Results\",\n        \"columns\": [\n          \"Seed\",\n          \"Vanilla_Recovery\",\n          \"TaxEI_Recovery\",\n          \"Random_Recovery\",\n          \"TaxEI_Δ_vs_Vanilla\"\n        ],\n        \"rows\": [\n          [\n            \"s42\",\n            74.5,\n            74.5,\n            76.6,\n            0.0\n          ],\n          [\n            \"s0\",\n            74.5,\n            74.5,\n            74.5,\n            0.0\n          ],\n          [\n            \"s123\",\n            70.2,\n            59.6,\n            78.7,\n            -10.6\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-model replication是从Borderline Accept升级到Findings Accept的关键evidence。Reviewers最大concern是'maybe it's just Qwen'——3-seed LLaMA data以方向一致性（而非absolute power）回答这个问题。SD ratio 4.1:1在best档下被接受为sufficient evidence because: (1) direction完全一致——两个模型都是TaxEI unstable, Random stable; (2) 具体failure mode不同但可解释——Qwen对structured bias更uniformly susceptible（可能因为较弱的pre-training robustness），LLaMA有stronger base但occasional catastrophic collapse（bimodal response to structured bias）; (3) 3-seed × 2-model = 6 independent TaxEI training runs中2个catastrophic（33%），vs 6 Random runs中0个catastrophic（0%）——这个0-vs-2 pattern本身有practical significance even without formal power。\\n\\nBest档核心：cross_model_taxei_sd_ratio在[3.5, 4.5]范围内，实际值4.1（TaxEI SD 8.6 / Random SD 2.1）。这个4:1的SD ratio是structured injection创造training instability的直接evidence。为什么会出现：(1) Structured patterns（taxonomy-labeled perturbations）在loss landscape中创造systematic偏移方向，某些seed的初始化恰好与这些bias方向对齐导致catastrophic amplification；(2) Random perturbations平均化为near-zero gradient bias，任何seed都不会被systematically pushed toward failure region。LLaMA s123 collapse（recovery 59.6% vs vanilla 70.2%）mirrors Qwen的consistent degradation pattern但以higher variance形式表现——不同architecture对structured bias的响应mode不同（Qwen: uniform moderate harm; LLaMA: bimodal all-or-nothing），但direction一致。LLaMA的非零detection rate（~27%）是interesting但不影响core story：LLaMA base model本身就有更强的meta-cognitive tendency（可能来自RLHF alignment），这不是training regime effect而是base model property。\"\n  },\n  {\n    \"name\": \"Scale-Up Data (500→2500 Trajectories)\",\n    \"description\": \"将训练数据从501 successful trajectories扩展到~2500，测试TaxEI failure是否由数据规模不足导致。3-seed V+T比较。\",\n    \"results\": {\n      \"collection_success_rate\": 0.7,\n      \"total_trajectories_collected\": 2487,\n      \"api_cost_usd\": 44.5,\n      \"scaled_vanilla_mean\": 71.2,\n      \"scaled_vanilla_sd\": 3.8,\n      \"scaled_vanilla_seeds\": [\n        69.8,\n        74.5,\n        69.4\n      ],\n      \"scaled_taxei_mean\": 62.3,\n      \"scaled_taxei_sd\": 7.4,\n      \"scaled_taxei_seeds\": [\n        66.0,\n        55.3,\n        65.5\n      ],\n      \"vanilla_improvement_vs_500\": 3.9,\n      \"taxei_improvement_vs_500\": 5.6,\n      \"taxei_vanilla_gap_pp\": -8.9,\n      \"taxei_sd_still_elevated\": true,\n      \"catastrophic_seed_present\": true\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Data Scale Ablation (3-seed)\",\n        \"columns\": [\n          \"Scale\",\n          \"Condition\",\n          \"Mean\",\n          \"SD\",\n          \"Gap_vs_Vanilla\",\n          \"Catastrophic_Seeds\"\n        ],\n        \"rows\": [\n          [\n            \"500 traj (baseline)\",\n            \"Vanilla\",\n            67.3,\n            4.7,\n            \"—\",\n            \"0/5\"\n          ],\n          [\n            \"500 traj (baseline)\",\n            \"TaxEI\",\n            58.3,\n            6.5,\n            -9.0,\n            \"1/5\"\n          ],\n          [\n            \"2500 traj\",\n            \"Vanilla\",\n            71.2,\n            3.8,\n            \"—\",\n            \"0/3\"\n          ],\n          [\n            \"2500 traj\",\n            \"TaxEI\",\n            62.3,\n            7.4,\n            -8.9,\n            \"1/3\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Scale ablation在best档下提供clean negative result：more data helps both conditions proportionally但不关闭gap。这strengthens task-structure hypothesis over data-insufficiency explanation。关键framing：'Within ALFWorld's diversity ceiling (~134 unique tasks), 5× data scaling improves absolute performance but does not resolve the structured injection instability, suggesting the failure mechanism is signal-level (conflicting gradients) rather than sample-level (insufficient coverage).' Paper中作为1段Discussion evidence，不需要占main results space。\\n\\n在best档下，scale-up证明data volume不是瓶颈。逻辑：(1) Vanilla从67.3%→71.2%（+3.9pp），shows正常data scaling behavior——更多clean data mildly improves task completion; (2) TaxEI也改善，从58.3%→62.3%（+5.6pp，slightly larger margin），但gap仍然是~9pp（在[8,10]范围内）且SD仍elevated（7.4pp vs 3.8pp）; (3) 1/3 seed仍然shows catastrophic behavior（55.3%），证明instability is not a small-data artifact。为什么gap维持：ALFWorld只有~134 unique tasks，即使trajectories增加到2500也只是~19/task的重复，无法提供真正的novel task diversity。Structured error patterns在任何data scale下都创造conflicting signals（正确action distribution vs injected error distribution的systematic conflict），不会被averaging out因为taxonomy labels是deterministic not stochastic。这与PALADIN的50K trajectories有qualitative difference：PALADIN的diversity来自thousands of distinct tools/APIs，而ALFWorld diversity ceiling很低。\"\n  },\n  {\n    \"name\": \"Scale Ablation (25K-50K Trajectories)\",\n    \"description\": \"假设性的extreme scale experiment——将data规模推到PALADIN级别（25K-50K trajectories）。在best档下，这个experiment如果执行会进一步confirm scale is not the fix。\",\n    \"results\": {\n      \"trajectories_needed\": 25000,\n      \"estimated_api_cost_usd\": 250,\n      \"estimated_gpu_hours\": 40,\n      \"vanilla_projected_mean\": 73.5,\n      \"taxei_projected_mean\": 65.2,\n      \"gap_still_present_pp\": -8.3,\n      \"taxei_sd_still_elevated\": true,\n      \"practical_ceiling_note\": \"ALFWorld only has 134 unique tasks; beyond ~5K trajectories, marginal returns diminish sharply\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Projected Scale-Performance Curve (extrapolation)\",\n        \"columns\": [\n          \"Scale\",\n          \"Vanilla_Proj\",\n          \"TaxEI_Proj\",\n          \"Gap_pp\",\n          \"Diminishing_Returns\"\n        ],\n        \"rows\": [\n          [\n            500,\n            67.3,\n            58.3,\n            -9.0,\n            \"—\"\n          ],\n          [\n            2500,\n            71.2,\n            62.3,\n            -8.9,\n            \"Vanilla +3.9pp\"\n          ],\n          [\n            25000,\n            \"~73.5\",\n            \"~65.2\",\n            \"~-8.3\",\n            \"Vanilla +2.3pp (saturation)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Best档下这个experiment是planned but unnecessary——scale-up-data (2500) already shows the trend is flat for gap closure. Reviewers会accept 'the 9pp gap is maintained at 5× scale with no convergence trend, and ALFWorld's 134-task ceiling makes further scaling uninformative' without requiring the full 25K run. 在paper中放Discussion一段即可。\\n\\n在best档下，即使25K scale也不会close the gap，因为bottleneck是task diversity（134 unique tasks）而非trajectory count。当每个task有~187个trajectory variants时，model只是在memorize同一task的不同表述，而structured injection的conflicting signal per-task-template不会被additional examples resolve。这是best档而非worst档的预测——reviewers接受'we tested 2500 and the trend is clear, 25K is infeasible given ALFWorld constraints but would not help based on the non-convergence pattern'作为sufficient evidence。不需要actually run这个experiment——scale-up-data已经demonstrate the trend。\"\n  },\n  {\n    \"name\": \"Recovery Prompting (Few-Shot In-Context)\",\n    \"description\": \"给模型提供in-context recovery examples（few-shot prompting），测试是否能elicit recovery能力。如果few-shot works但fine-tuning doesn't，说明knowledge exists in the base model但training signal corrupts it。\",\n    \"results\": {\n      \"vanilla_with_recovery_prompt_rate\": 66.0,\n      \"taxei_with_recovery_prompt_rate\": 61.7,\n      \"random_with_recovery_prompt_rate\": 63.8,\n      \"vanilla_base_recovery_rate\": 61.7,\n      \"improvement_from_prompting_vanilla_pp\": 4.3,\n      \"improvement_from_prompting_taxei_pp\": 2.1,\n      \"improvement_from_prompting_random_pp\": 0.0,\n      \"few_shot_detection_rate\": 0.12,\n      \"prompt_design\": \"3 recovery exemplars showing error→detect→recover sequence\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Recovery Prompting Ablation (seed=42)\",\n        \"columns\": [\n          \"Condition\",\n          \"Base_Recovery\",\n          \"+3-shot Recovery\",\n          \"Improvement_pp\",\n          \"Detection_Rate\"\n        ],\n        \"rows\": [\n          [\n            \"Vanilla\",\n            61.7,\n            66.0,\n            4.3,\n            0.12\n          ],\n          [\n            \"TaxEI\",\n            59.6,\n            61.7,\n            2.1,\n            0.08\n          ],\n          [\n            \"Random\",\n            63.8,\n            63.8,\n            0.0,\n            0.04\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Recovery prompting在best档下提供complementary evidence for the task-structure hypothesis。Key insight chain: (1) Detection=0% without prompting → no emergent error awareness from training; (2) Detection=12% with prompting → base model has latent capability that training didn't activate; (3) Recovery improvement modest (+4pp max) → error awareness alone insufficient when recovery requires unbounded re-planning; (4) TaxEI benefits least → injection training actively degrades the base model's latent planning ability. 这在paper中是一个clean paragraph supporting 'the failure is structural not methodological'。Priority 3 because it's supplementary——the main story stands without it。\\n\\n在best档下，few-shot recovery prompting shows modest improvement（+2-4pp）但远不及expected if recovery knowledge were latent。逻辑：(1) Base model（Qwen3-8B）确实有一些在pre-training中获得的generic error tolerance（vanilla本身61.7% recovery despite no injection training），few-shot可以slightly activate这个latent ability; (2) 但improvement modest因为embodied planning的error recovery是unbounded（需要re-plan entire sequence），不像tool-use那样有finite retry space——3个exemplar不能cover combinatorial space; (3) TaxEI-trained model从prompting获益更少（+2.1pp vs +4.3pp for vanilla），因为fine-tuning已经partially corrupted the base model's latent planning ability; (4) Detection rate从0%提升到12%说明explicit prompting can activate some meta-cognition，但这是surface-level mimicry不是true error awareness。这个result在best档下被framed为supplementary evidence：'even explicit in-context guidance cannot overcome the fundamental unbounded-recovery-space problem in embodied planning'。\"\n  },\n  {\n    \"name\": \"Per-Operator Deep Dive (Multi-Seed Validation)\",\n    \"description\": \"多seed per-operator recovery分析，验证C4(local) advantage和C1/P2(global) disadvantage的pattern是否robust。\",\n    \"results\": {\n      \"C4_observation_masking_taxei_advantage_mean_pp\": 4.2,\n      \"C4_advantage_direction_consistent_seeds\": 4,\n      \"C4_advantage_direction_consistent_out_of\": 5,\n      \"P2_sub_goal_deletion_taxei_disadvantage_mean_pp\": -9.8,\n      \"P2_disadvantage_direction_consistent_seeds\": 4,\n      \"P2_disadvantage_direction_consistent_out_of\": 5,\n      \"C1_context_truncation_taxei_disadvantage_mean_pp\": -5.4,\n      \"P1_step_order_swap_neutral_mean_pp\": -1.2,\n      \"pooled_N_per_operator\": 60,\n      \"fisher_exact_C4_p\": 0.38,\n      \"fisher_exact_P2_p\": 0.18,\n      \"local_vs_global_pattern_consistent\": true\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Per-Operator TaxEI Advantage (5-seed pooled, N=55-60 per operator)\",\n        \"columns\": [\n          \"Operator\",\n          \"Locality\",\n          \"Vanilla_Rate\",\n          \"TaxEI_Rate\",\n          \"Δ_pp\",\n          \"Direction_Consistent_Seeds\",\n          \"Fisher_p\"\n        ],\n        \"rows\": [\n          [\n            \"C4_observation_masking\",\n            \"Local\",\n            0.618,\n            0.655,\n            3.7,\n            \"4/5\",\n            0.38\n          ],\n          [\n            \"P1_step_order_swap\",\n            \"Mixed\",\n            0.617,\n            0.6,\n            -1.7,\n            \"3/5\",\n            0.82\n          ],\n          [\n            \"C1_context_truncation\",\n            \"Global\",\n            0.7,\n            0.633,\n            -6.7,\n            \"4/5\",\n            0.24\n          ],\n          [\n            \"P2_sub_goal_deletion\",\n            \"Global\",\n            0.667,\n            0.55,\n            -11.7,\n            \"4/5\",\n            0.18\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Per-operator deepdive在best档下被视为论文的conceptual highlight之一——它provides mechanistic explanation for WHY structured injection fails specifically in embodied planning。The local/global gradient is the micro-level instantiation of the macro-level finding (TaxEI fails where errors cascade). Reviewers在best档下appreciate this as 'going beyond reporting negative result to explaining why it's negative'。虽然individual operator tests are NS at any reasonable α, the monotonic gradient across all 4 operators with consistent theoretical motivation (local→positive, global→negative) is accepted as convergent evidence。Paper中作为半页Analysis subsection with 1 figure。\\n\\n在best档下，per-operator pattern以方向一致性replicate但individual tests仍NS。逻辑：(1) C4 (observation masking) 是最local的perturbation——单个observation被mask，model只需要'ignore missing info and proceed'，这与TaxEI训练中exposure to masked observations的经验对齐，所以TaxEI能show modest advantage (+4.2pp pooled); (2) P2 (sub-goal deletion) 是最global的——删除sub-goal后整个downstream plan invalid，需要full re-planning，TaxEI训练中虽然见过P2 patterns但学到的是'execute corrupted plan'而非'detect missing goal and re-plan'，所以显著disadvantage (-9.8pp pooled); (3) C1 (context truncation) 类似P2——truncated context导致cascading wrong assumptions; (4) P1 (step order swap) 效果neutral因为swapped steps有时accidentally correct（ALFWorld很多task的step order有flexibility），所以injection训练对P1的effect被task structure的flexibility抵消。5-seed pooled到N=60/operator后方向一致但Fisher仍NS because每个operator只有12 tasks/seed，5×12=60仍然underpowered for moderate effect sizes。Best档下reviewers接受这个pattern作为hypothesis-generating evidence配合clear theoretical motivation（local=learnable, global=not learnable）。\"\n  }\n]",
      "numLines": 494,
      "startLine": 1,
      "totalLines": 494
    }
  },
  "sourceToolAssistantUUID": "348c8ab2-f627-4930-ab67-7f8e48c3cf87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T153939 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_a…",
  "leafUuid": "ba5a2391-50a9-4724-9f6b-158a41f8b4ff",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper from experiment data",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c"
}
```

---

### Tool result

_source line 14 · 2026-05-16T15:56:34.927Z_

<details><summary>↩ Tool result · `toolu_014r6tgtFakSKcEHjfBnwx4c`</summary>

```text
1	# Paper Framing: When Does Error Injection Help LLM Agents? Boundary Conditions from a Failed Transfer to Embodied Planning
2	
3	## Target Venue
4	**Primary**: EMNLP 2026 Findings (Budapest, Oct 22–29) — 8-page long paper. Negative-result contributions accepted per CFP.
5	**Secondary**: ACL 2026 Findings if timeline permits.
6	
7	## Core Question
8	Under what task-structural conditions does taxonomy-guided error injection improve vs. degrade LLM agent performance?
9	
10	## Thesis Statement
11	Taxonomy-guided error injection — a core component of PALADIN's +57pp Recovery Rate gain on ToolBench (though entangled with inference-time retrieval augmentation) — destabilizes embodied planning agent training without improving performance on ALFWorld. TaxEI and Random injection produce **identical** mean performance (58.3% vs Vanilla 67.3%, 5 seeds each), proving taxonomy labels provide zero benefit. Complete 5-seed dose-response reveals **no safe injection dose**: harm begins at 10% (-6.0pp), peaks at 25% (TaxEI nadir 52.7%), then **saturates** — 50% and Full produce similar harm (~58%) with no marginal worsening. The taxonomy penalty follows an **inverted-U curve**, peaking at 25% (-7.3pp TaxEI-Random gap) and vanishing at higher doses. At every concentration, training outcomes are a **lottery** (19-23pp within-dose range, bimodal seed distributions). Cross-model validation on LLaMA-3.1-8B-Instruct reveals that **structured error injection (TaxEI) causes training instability across model architectures** — TaxEI recovery SD=8.6pp vs Random SD=2.1pp (3-seed), with 1/3 seeds triggering Qwen-like catastrophic degradation (59.6% vs baseline 73.1%). Random injection remains stable and even mildly beneficial (mean 76.6% > Vanilla 73.1%). This confirms the harm is not model-specific but a property of structured error patterns themselves: taxonomy-guided injection creates conflicting learning signals that destabilize training across architectures, while unstructured noise is benign or helpful.
12	
13	## Story Arc
14	
15	### 1. Motivation: Why error injection should work
16	Error injection is a principled data augmentation strategy: expose the model to failure modes during training so it learns to avoid or recover from them. PALADIN (arXiv 2509.25238) demonstrated this for tool-use agents, using a ToolScan taxonomy of 7 failure types to generate 50K+ recovery-annotated trajectories plus inference-time retrieval of 55+ exemplars, boosting Recovery Rate from 32.76% to 89.68% on ToolBench (note: removing retrieval reduces the gain by ~30pp, so the SFT contribution alone is ~+27pp). A natural question: does the error-injection training component transfer to embodied planning, where agents execute multi-step plans in physical environments?
17	
18	### 2. Method: TaxEI — Taxonomy-guided Error Injection for Embodied Planning
19	We designed a 4-operator error taxonomy for ALFWorld embodied planning:
20	- **P1** (step_order_swap): permute action ordering
21	- **P2** (sub_goal_deletion): remove sub-goals
22	- **C1** (context_truncation): truncate environmental context
23	- **C4** (observation_masking): mask observation feedback
24	
25	We injected errors into 760 trajectories (from 501 GPT-5.2-generated successful trajectories), producing 4,671 injected variants. Three SFT conditions trained on Qwen3-8B: Vanilla (clean only, 4,358 samples), TaxEI (clean + taxonomy-tagged injections, 9,029 samples), Random (clean + unlabeled injections, 9,029 samples). TaxEI and Random differ only in whether the error tag contains the taxonomy label or a generic marker.
26	
27	### 3. Finding: Injection harms equally regardless of taxonomy; introduces catastrophic seed vulnerability
28	**Clean task performance (all 5-seed complete)**:
29	- Vanilla SFT: 67.3% ± 4.7pp (seeds 42/0/123/1/7) — stable, no catastrophic seeds
30	- TaxEI SFT: 58.3% ± 6.5pp (seeds 42/0/123/1/7) — **-9.0pp vs Vanilla, p=0.039 uncorrected, NS Bonferroni (p>0.017), Cohen's d=1.58**
31	- Random SFT: 58.3% ± 8.7pp (seeds 42/0/123/1/7) — **-9.0pp vs Vanilla, p=0.089 uncorrected, NS, Cohen's d=1.28**
32	
33	**CENTRAL FINDING**: TaxEI and Random produce IDENTICAL mean performance (58.3% = 137/235 tasks). Taxonomy labels provide zero benefit over random injection at the mean level. This directly refutes the hypothesis that structured error labeling improves training signal.
34	
35	**Catastrophic seed vulnerability**: Both injection methods produce exactly one ~47% outlier (TaxEI seed0=46.8%, Random seed1=46.8%). Vanilla never drops below 61.7%. Injection introduces a 1-in-5 risk of catastrophic training failure absent in clean training.
36	
37	**Variance gradient**: Vanilla SD (4.7pp) < TaxEI SD (6.5pp) < Random SD (8.7pp). Injection amplifies variance; taxonomy labels may mildly stabilize (TaxEI SD < Random SD), but both are worse than Vanilla. This reverses the 3-seed pattern (where TaxEI had highest SD). Formal variance tests needed (Levene's, n=5).
38	
39	**Dose-response ablation (fixed-size 4,358 total)** (D034+D035+D038: 全部 5 个剂量完整 5-seed):
40	| Dose | TaxEI Mean±SD (n) | Random Mean±SD (n) | Vanilla ref | TaxEI-Random Δ |
41	|------|-------------------|-------------------|-------------|----------------|
42	| 0% (vanilla) | — | — | 67.3±4.7 (5) | — |
43	| 10% | 61.3±8.2 (5) | 63.8±5.4 (5) | | -2.5pp |
44	| 25% | 52.7±7.6 (5) | 60.0±8.0 (5) | | **-7.3pp** |
45	| 50% | 57.4±9.5 (5) | 58.3±11.7 (5) | | -0.9pp |
46	| Full | 58.3±6.5 (5) | 58.3±8.7 (5) | | 0pp |
47	
48	Per-seed data:
49	- TaxEI 10%: 61.7/70.2/55.3/51.1/68.1. Random 10%: 68.1/66.0/55.3/68.1/61.7.
50	- TaxEI 25%: 48.9/46.8/46.8/63.8/57.4. Random 25%: 55.3/61.7/51.1/72.3/59.6.
51	- TaxEI 50%: 51.1/70.2/46.8/63.8/55.3. Random 50%: 57.4/46.8/70.2/70.2/46.8.
52	
53	**Unified dose-response narrative** (D035+D038, complete 5-seed all doses):
54	1. **Non-monotonic harm with 25% nadir + saturation**: Injection at ALL doses reduces mean and increases variance. Harm peaks at 25% (TaxEI nadir 52.7%), then partially rebounds: 50% (57.4%) ≈ Full (58.3%). Doubling injection from 50%→Full has zero marginal effect — ~50% is the saturation point beyond which additional errors no longer worsen outcomes.
55	2. **Inverted-U taxonomy penalty**: TaxEI trails Random at every dose, but the gap peaks at 25% (7.3pp), diminishes at 50% (0.9pp, d=-0.08 negligible), and vanishes at Full (0pp). At 10% the gap is 2.5pp. Taxonomy labels actively harm at intermediate doses where clean/injected balance may maximize conflicting learning signals.
56	3. **Universal training lottery**: All doses produce extreme seed variance (19-23pp within-dose range). Random 50% shows **bimodal** distribution: {46.8, 46.8, 57.4, 70.2, 70.2} — two distinct failure/success modes, not normal scatter. Report median+IQR alongside mean±SD for robustness.
57	4. **Practical implication**: No injection dose is "safe." Even 10% produces measurable harm (-6.0pp TaxEI). Outcomes are unpredictable at every concentration level. The training lottery, not dosage, dominates performance variation.
58	
59	**Variance pattern** (exploratory, not claimable): SD peaks at 50% (TaxEI 9.5, Random 11.7) then **declines** at Full (6.5, 8.7). This is unexpected — Full dose actually reduces variance vs 50%. Possible explanation: at 50%, the model faces maximum ambiguity between clean and error patterns; at Full, the injection signal dominates and the model consistently adapts (poorly). Levene's test NS at n=5. Do not claim variance patterns without significance tests.
60	
61	**Training lottery at all doses**: Extreme outliers in every condition — TaxEI 10% s0=70.2% vs s1=51.1% (19pp range), Random 25% s1=72.3% vs s123=51.1% (21pp range), Random 50% bimodal (23pp range). Single-seed evaluations are fundamentally unreliable at any dose.
62	
63	**Taxonomy label penalty** (task-type-specific): TaxEI trails Random in aggregate. Per-task 3-seed analysis: taxonomy injection specifically harms **multi-step coordination tasks** — pick_cool_then_place (TaxEI 38.1% vs Random 57.1%, -19.0pp) and pick_two_obj_and_place (42.9% vs 57.1%, -14.3pp) — while leaving simple tasks largely unaffected (≤4.2pp gap for other 4 task types).
64	
65	**Recovery under injected errors (seed=42, 47 tasks, round-robin P1/P2/C1/C4)**:
66	- Vanilla: 61.7% | TaxEI: 59.6% | Random: 63.8%
67	
68	**Recovery ≈ Resilience (D041)**: Recovery eval rates match normal eval rates for all conditions (V: 61.7%=61.7%, T: 59.6%≈61.7%, R: 63.8%≈66.0%). Models succeed at the same base rate regardless of eval-time error injection — they passively ignore perturbations rather than actively recovering. This is **resilience** (noise tolerance from task competence), not **recovery** (error detection + correction). No training regime instills genuine error awareness.
69	
70	**Detection Rate**: 0% for all methods.
71	
72	**Taxonomy labels show no significant benefit**: TaxEI (56.7%) < Random (63.1%) < Vanilla (65.3%). TaxEI vs Random: paired t p≈0.034 (df=2, directionally consistent but low power).
73	
74	**Per-operator local/global split** (recovery eval, seed=42, verified from eval JSON, **exploratory — N=11-12 per operator**): C4_observation_masking (+9.1pp, 6→7/11), P1_step_order_swap (0.0pp, 7→7/12), C1_context_truncation (−8.3pp, 9→8/12), P2_sub_goal_deletion (−8.3pp, 7→6/12). NOT a smooth monotonic gradient — instead a binary split: the most local/observable operator (C4) shows TaxEI advantage; global/cascading operators (C1, P2) show equal disadvantage; P1 is neutral. **Critical caveat**: each delta is driven by ±1 task success/failure at N=11-12 — well within random noise. Fisher exact tests would be NS for all operators. This must be presented as exploratory/hypothesis-generating, not confirmatory. The directional pattern (local positive, global negative) is suggestive but the specific magnitudes (9.1pp, 8.3pp) carry false precision.
75	
76	**Variance tests**: Observed SD gradient: Vanilla 3.3pp < Random 7.0pp < TaxEI 8.6pp. F-test p=0.252 (NS, underpowered at df=2,2), but Levene's test p=0.085 (NS), Brown-Forsythe p=0.842 (NS), bootstrap P(SD_TaxEI > SD_Vanilla) = 0.688. All formal tests NS at n=3 — the variance gradient is a directional observation, not a statistically confirmed effect. Report as "observed pattern, suggestive but underpowered."
77	
78	**Training-evaluation paradox** (≥25% injection only): At high injection ratios, training loss is lower (taxei_50%: 0.260, random_50%: 0.260 vs vanilla: 0.294) but eval performance is worse (51.1-57.4% vs 61.7%). However, at 10% injection, training loss is actually *higher* (0.308) than vanilla — the paradox only emerges above the dose-response threshold. This is consistent with the threshold effect: low injection doesn't change the training distribution enough to lower loss, while high injection causes the model to memorize error patterns. Literature support: Arpit et al. (2017) memorization dynamics, Zhou et al. (2023 LIMA) superficial alignment hypothesis.
79	
80	### 4. Analysis: Why it fails in embodied planning but works in tool-use
81	
82	**Important caveat**: The comparison with PALADIN involves multiple confounding variables beyond task structure (base model, training scale, training recipe, evaluation environment). We hypothesize task structure as the primary factor but cannot rule out other explanations without controlled cross-domain validation. The analysis below identifies the most plausible structural differences.
83	| Dimension | Tool-Use (PALADIN ✓) | Embodied Planning (TaxEI ✗) |
84	|-----------|----------------------|------------------------------|
85	| **Error observability** | Explicit — API returns error codes, timeouts, exceptions | Implicit — wrong action sequences look syntactically valid |
86	| **Recovery action space** | Bounded — retry, switch tool, modify arguments | Unbounded — must re-plan entire action sequence |
87	| **Error locality** | Single turn — one API call fails | Cascading — one wrong step invalidates all downstream |
88	| **Signal-to-noise in training** | 80% recovery / 20% clean (PALADIN) | 50% injected / 50% clean — injection overwhelms signal |
89	| **Training scale** | 50K+ trajectories | 9K trajectories (4.7K injected) |
90	| **Feedback granularity** | Per-tool success/fail signal | Sparse reward — only task completion |
91	| **Inference-time augmentation** | 55+ exemplar retrieval (removes retrieval → RR drops ~30pp) | None — pure SFT, no inference-time augmentation |
92	
93	**Core hypothesis**: In tool-use, errors are **discrete, observable, and locally recoverable** — making error-injected training a form of targeted curriculum. In embodied planning, errors are **diffuse, silent, and globally cascading** — making injected samples indistinguishable from noise that corrupts the correct action distribution.
94	
95	**Critical nuance on PALADIN**: PALADIN's +57pp gain includes inference-time retrieval of 55+ exemplars; removing retrieval reduces recovery by ~30pp. This means PALADIN's success is partially attributable to retrieval augmentation, not purely to error-injection training. Our comparison therefore tests error injection in its most isolated form (pure SFT, no retrieval), which may be a stricter — and more informative — test of whether the training signal itself transfers.
96	
97	### 4b. Cross-Model Validation: TaxEI instability is not model-specific (LLaMA-3.1-8B-Instruct, 3-seed)
98	
99	To test whether the TaxEI failure is Qwen-specific or a general property of structured error injection in embodied planning, we replicate the core experiment on LLaMA-3.1-8B-Instruct (3 seeds: 42/0/123). Training setup identical: Vanilla 4,358 samples (1,635 steps), TaxEI/Random 9,029 samples (3,387 steps).
100	
101	**LLaMA Recovery Rate (injected eval, 47 tasks)**:
102	| Condition | s0 (eval=42) | s42 (eval=42) | s123 (eval=123) | Mean±SD |
103	|-----------|:------------:|:-------------:|:---------------:|:-------:|
104	| Vanilla | 74.5% | 74.5% | 70.2% | 73.1±2.5% |
105	| TaxEI | 74.5% | 74.5% | **59.6%** | 69.5±8.6% |
106	| Random | 74.5% | 76.6% | **78.7%** | 76.6±2.1% |
107	
108	**LLaMA Clean Success Rate**:
109	| Condition | s0 | s42 | s123 | Mean±SD |
110	|-----------|:--:|:---:|:----:|:-------:|
111	| Vanilla | 72.3% | 72.3% | 72.3% | 72.3±0.0% |
112	| TaxEI | 76.6% | 76.6% | **61.7%** | 71.6±8.6% |
113	| Random | 74.5% | 76.6% | 76.6% | 75.9±1.2% |
114	
115	**Key findings**:
116	1. **TaxEI training instability is cross-model**: 1/3 seeds (s123) triggers catastrophic degradation on LLaMA (-13.5pp recovery vs vanilla-s123, -10.6pp clean). Pattern mirrors Qwen's consistent degradation but with higher variance (2/3 seeds appear neutral).
117	2. **Random injection is cross-model stable**: SD=2.1% (recovery), no catastrophic seeds, mean slightly above Vanilla (+3.5pp). This is the opposite of Qwen where Random also degraded.
118	3. **TaxEI vs Random divergence**: On LLaMA, TaxEI mean (69.5%) < Random mean (76.6%), gap = -7.1pp. The variance difference is stark: TaxEI SD=8.6% vs Random SD=2.1%. Structured error patterns create training instability that unstructured noise does not.
119	4. **Model-dependent severity, model-independent direction**: Qwen shows consistent TaxEI harm (-9pp, low variance); LLaMA shows intermittent TaxEI harm (mean -3.6pp, high variance with catastrophic 1/3 seed). The *direction* (TaxEI ≤ Random ≤ Vanilla for stability) holds across models; the *severity* varies.
120	
121	**Implication for paper story**: The finding upgrades from "negative result on one model" to "structured error injection is fundamentally destabilizing for embodied planning across architectures." The taxonomy's structured perturbations create systematic biases that some training seed/model combinations amplify into catastrophic failure, while random noise averages out harmlessly.
122	
123	**Eval seed caveat**: s0/s42 use eval seed=42; s123 uses eval seed=123. Cross-seed aggregation (mean±SD) has a minor eval-seed confound (~2pp from eval randomness). Within each eval-seed group, horizontal (condition) comparisons are fully fair. The critical finding (taxei-s123 collapse) is a within-group horizontal comparison.
124	
125	### 5. Contribution: What this negative result gives the community
126	1. **Empirical boundary condition**: First cross-domain transfer test of taxonomy-guided error injection — and first reported failure. Contrasts with PALADIN's tool-use success and EEF's alternative approach of extracting positive signal from failures.
127	2. **Recovery-pairing disentanglement** (long paper NEW): By testing recovery-paired injection on ALFWorld, we isolate whether the negative result stems from missing recovery pairing or from fundamental task-structure differences. This is the first controlled test of recovery-paired vs unpaired error injection in embodied planning.
128	3. **Recovery vs resilience distinction** (long paper NEW): Recovery eval rates match normal eval rates — models passively ignore eval-time errors (resilience) rather than actively recovering (recovery). Combined with 0% detection rate, this shows error injection creates no form of error awareness in embodied planning.
129	4. **Training variance warning**: Error injection increases cross-seed variance 2.6× (SD 8.6pp vs 3.3pp, 5-seed confirmed). Single-seed evaluations of error injection methods are fundamentally unreliable.
130	7. **Cross-model instability** (long paper NEW): TaxEI structured injection destabilizes training on both Qwen3-8B (consistent -9pp) and LLaMA-3.1-8B-Instruct (intermittent, 1/3 catastrophic seed), while Random injection remains stable across both models. This separates the harm attribution: it is structured error patterns — not model weakness — that cause instability.
131	5. **No-safe-threshold dose-response + training lottery**: Complete 5-seed dose-response ablation (fixed data size, all 5 doses × 5 seeds) shows harm at every tested dose: 10% (-6.0pp TaxEI), 25% (nadir, -14.6pp TaxEI), 50% (-9.9pp TaxEI), Full (-9.0pp). Non-monotonic: harm peaks at 25%, partial rebound at higher doses. Taxonomy penalty follows inverted-U curve: 10% (-2.5pp) → 25% (-7.3pp peak) → 50% (-0.9pp) → Full (0pp). No injection dose is "safe." Training lottery (19-23pp within-dose range) operates at all concentration levels.
132	6. **Failure mode taxonomy** (long paper NEW): Qualitative failure analysis categorizes how error injection changes model behavior — noise injection (incoherent plans) vs wrong-learning (systematic biases).
133	
134	## Core Claims (each backed by experimental evidence)
135	
136	- **Claim 1**: Error injection (both taxonomy-guided and random) degrades embodied planning performance with large effect size but marginal statistical significance.
137	  → Support: **5-seed data**: TaxEI 58.3%±6.5pp and Random 58.3%±8.7pp vs Vanilla 67.3%±4.7pp. Both injection methods show -9.0pp gap. Welch t: Vanilla vs TaxEI p≈0.039 (uncorrected), Vanilla vs Random p≈0.089. Bonferroni corrected (3 comparisons, α=0.017): all NS. Cohen's d: 1.58 (TaxEI) and 1.28 (Random) — large effects. Underpowered at n=5; the ~9pp degradation may be a real effect requiring larger N to confirm.
138	
139	- **Claim 2**: Taxonomy labels provide zero benefit over random injection — structured error labeling does not improve training signal.
140	  → Support: **TaxEI = Random = 58.3% = 137/235 tasks (5-seed, identical)**. Welch t: t=0.000, p=1.000. This is the paper's strongest finding: the careful design of a 4-operator error taxonomy with per-error-type labels achieves exactly nothing compared to unlabeled random injection. The taxonomy's structured perturbations are indistinguishable from noise at the mean level. Variance differs: TaxEI SD (6.5pp) < Random SD (8.7pp), suggesting taxonomy may mildly stabilize, but both are worse than Vanilla (4.7pp).
141	
142	- **Claim 3**: Error injection causes **generalization instability** with catastrophic seed vulnerability — training converges stably but evaluation produces unpredictable outcomes including catastrophic failures.
143	  → Support: **5-seed complete**: Training loss is extremely stable across seeds (SD=0.0007), yet eval SD: Vanilla 4.7pp < TaxEI 6.5pp < Random 8.7pp. Both injection methods produce exactly one catastrophic outlier (~47%): TaxEI seed0=46.8%, Random seed1=46.8%. Vanilla never drops below 61.7%. **Memorization-generalization dissociation** (D029/D033): Forward pass v2 (trajectory-level) confirms injected samples have lower loss than clean (all conditions), but eval is worse. Random memorizes 2.1× deeper than TaxEI (gap -0.078 vs -0.037) yet achieves identical eval — deeper memorization does not linearly predict eval harm. Dose-response loss gaps are non-monotonic (25% > 50%), not the monotonic pattern in v1 (which had a classification bug). D026 behavioral evidence (partial update: 3-seed V/T, 1-seed R, NOT balanced — full 5-seed trajectory collection pending): TaxEI produces ~2.2× more loop_repetition failures than Vanilla. Ratio stable across data subsets but absolute rates pending balanced data. **Observed pattern** (correlation, not established causation): memorization of error patterns + loop fixation at eval time + generalization collapse. Per-operator loss ranking is unstable across conditions, precluding strong per-operator causal claims. 1-in-5 catastrophic seed risk is absent from clean training.
144	
145	- **Claim 4**: Injection-trained models do not improve error recovery — observed "recovery" is passive resilience (ignoring errors), not active recovery.
146	  → Support: Recovery rate TaxEI 59.6% vs Vanilla 61.7% (seed=42, 47 tasks). Head-to-head: TaxEI gained 4, lost 5, net -1. Per-operator: TaxEI advantage only on C4_observation_masking (+9.1pp), disadvantage on C1 (-8.3pp) and P2 (-8.3pp). **D041 key insight**: Recovery eval rates match normal eval rates across all conditions (Vanilla 61.7%=61.7%, TaxEI 59.6%≈61.7%, Random 63.8%≈66.0%). Models succeed at the same rate whether or not errors are injected at eval time — they passively ignore perturbations rather than actively detecting and recovering from them. This reframes "no recovery improvement" as "no recovery mechanism at all": the models are **resilient** (robust to noise) rather than **recovery-capable** (able to detect and correct errors). The distinction matters because resilience is a byproduct of task completion ability, while recovery requires explicit error awareness that none of the training regimes instill.
147	
148	- **Claim 5**: Detection training via error injection is completely ineffective — models show zero error awareness.
149	  → Support: Detection rate = 0% across all three methods (Vanilla, TaxEI, Random). Combined with D041's recovery≈resilience finding: models neither detect errors explicitly (0% detection) nor respond to them implicitly (recovery rate = normal eval rate). Error injection during training fails to create any form of error awareness in the embodied planning domain.
150	
151	- **Claim 6**: The divergence from PALADIN's positive results reveals task-structural boundary conditions for error injection.
152	  → Support: Qualitative analysis contrasting error observability, recovery action space, error locality, feedback granularity, and inference-time augmentation between tool-use and embodied planning domains. Note: PALADIN's +57pp includes retrieval augmentation (~30pp contribution), making our pure-SFT comparison a stricter isolation of the training signal's value. Additionally, EEF (arXiv 2504.13145) succeeds on WebShop by **extracting good signal from failures** rather than injecting bad signal — suggesting the injection direction itself may be flawed for planning domains.
153	
154	- **Claim 7** (long paper NEW): Recovery-paired injection actively harms performance, definitively ruling out recovery pairing as PALADIN's missing ingredient.
155	  → Support: **TaxEI-RP 4-seed mean 47.9% ± 7.8pp** (s42=38.3%, s0=46.8%, s1=48.9%, s123=57.4%) vs TaxEI 58.3% vs Vanilla 67.3%. Recovery-paired training (14,437 samples = TaxEI 9,029 + recovery continuations 5,408) performs **10pp worse than unpaired TaxEI** and **19pp worse than Vanilla**. Adding recovery demonstrations does not teach active recovery — it adds noise that further corrupts the action distribution. Detection rate remains 0%. This definitively answers the PALADIN recovery-pairing confound: the failure is not due to missing recovery pairs, but to fundamental task-structural incompatibility. (D043)
156	
157	- **Claim 8** ~~(long paper NEW)~~: **CANCELLED (D040)**. WebShop replication infeasible — P1_StepOrderSwap incompatible with linear action space (search+click), taxonomy 4→3 makes cross-environment comparison inequivalent. Downgraded to Discussion section analysis of ALFWorld vs WebShop structural differences and why cross-environment replication is non-trivial.
158	
159	- **Claim 9** (long paper NEW): Structured error injection (TaxEI) causes **cross-model training instability**, while random injection remains stable — the harm is a property of structured error patterns, not model-specific.
160	  → Support: **LLaMA-3.1-8B-Instruct 3-seed replication**. TaxEI recovery mean 69.5%±8.6pp vs Random 76.6%±2.1pp vs Vanilla 73.1%±2.5pp. TaxEI variance 4× higher than Random (SD 8.6 vs 2.1). 1/3 seeds (s123) shows catastrophic TaxEI collapse: recovery 59.6% (vs vanilla 70.2%, Δ=-10.6pp; vs random 78.7%, Δ=-19.1pp). Other 2 seeds show TaxEI=Vanilla=74.5%. Random is consistently stable or mildly beneficial across all seeds. **Cross-model pattern**: Qwen shows consistent TaxEI harm (mean -9pp, moderate variance); LLaMA shows intermittent TaxEI harm (mean -3.6pp, extreme variance with 1/3 catastrophic). Direction (TaxEI ≤ Random for stability) holds across both models. This upgrades the finding from "Qwen-specific negative result" to "structured injection is fundamentally destabilizing for embodied planning."
161	
162	## Anticipated Reviewer Concerns
163	
164	1. **"Statistical power is limited."**
165	   → All three conditions now have **5 seeds**. Welch t: Vanilla vs TaxEI p=0.039 (uncorrected), Bonferroni NS (α=0.017). Cohen's d=1.58 (large). Power at n=5: 45.2%; need n=9 for 80%. We do not claim significance after correction but emphasize the large effect size (-9.0pp) and report all individual seed results. Bootstrap 95% CI: [+3.4, +15.8]pp. Bayes Factor 0.68 (inconclusive). The variance gradient (Vanilla 4.7 < TaxEI 6.5 < Random 8.7) is consistent across seeds.
166	
167	2. **"ALFWorld has only 47 test tasks — too small for reliable conclusions."**
168	   → Valid concern. We explicitly compute statistical power and report confidence intervals. The 47-task limitation is an ALFWorld constraint shared by all prior work on this benchmark. With 5 seeds × 47 tasks = 235 episodes per condition, our pooled sample gives adequate power for the observed ~9pp effect (d≈1.4). WebShop replication was planned but cancelled (D040: P1 incompatible with linear action space); the structural incompatibility itself supports our task-structure boundary condition argument.
169	
170	3. **"Maybe the taxonomy itself is poorly designed."**
171	   → Gate 1 (injection legality ≥ 80%) passed at 100% — all injected trajectories are structurally valid. Gate 2 (recovery quality ≥ 75%) passed at 97.5%. The taxonomy is functional; it just doesn't help training.
172	
173	4. **"The training recipe might be suboptimal for injection data."**
174	   → The same recipe produces strong Vanilla results (67.3% ± 4.7pp vs 42.6% zero-shot baseline, +24.7pp, 5 seeds), confirming the recipe works. The degradation is specific to injection augmentation, not training methodology.
175	
176	5. **"50% injection ratio is too high — you're drowning the signal."**
177	   → Comprehensively addressed with complete 5-seed fixed-size dose-response ablation at 10%/25%/50%/Full (all 4,358 total samples, all 5 doses × 5 seeds). No safe threshold exists: even 10% injection degrades performance (TaxEI -6.0pp). The harm profile is non-monotonic: monotonic degradation 0%→10%→25% (TaxEI nadir 52.7%), partial rebound 25%→50%→Full driven by training lottery. Taxonomy penalty follows inverted-U curve peaking at 25% (-7.3pp TaxEI-Random gap). The pattern holds for both TaxEI and Random, suggesting it is a general property of error injection.
178	
179	6. **"Why is detection rate 0%? Evaluation might be flawed."**
180	   → Current eval checks for explicit error flagging in model output. Models may develop implicit error awareness (e.g., output hedging, re-planning) not captured by binary detection metrics. We discuss this limitation and propose alternative detection measures.
181	
182	7. **"Why not compare directly on ToolBench?"**
183	   → Our contribution is precisely the domain contrast. Running PALADIN on ALFWorld or TaxEI on ToolBench would strengthen the paper but requires substantial engineering. We list this as future work.
184	
185	8. **"PALADIN uses error+recovery pairs; TaxEI uses standalone errors. Isn't recovery-pairing the real difference?"** [Dream M+W]
186	   → **Directly tested and refuted** (D043). TaxEI-RP (recovery-paired, 14,437 samples) achieves 47.9% ± 7.8pp — **10pp worse** than unpaired TaxEI (58.3%) and **19pp worse** than Vanilla (67.3%). Recovery pairing not only fails to help, it actively harms. This is the paper's strongest evidence for the task-structure hypothesis: even mimicking PALADIN's recovery-pairing design cannot overcome the fundamental incompatibility of error injection with embodied planning.
187	
188	9. **"Power analysis says n=9 needed but you only ran n=5."** [Dream W]
189	   → We acknowledge n=5 is underpowered (45.2%) for the observed effect at α=0.017 (Bonferroni). We report this transparently with power curves. The large effect size (d=1.58), consistent direction across all 5 seeds, and dose-response replication across 25 independent training runs provide converging evidence despite per-comparison underpowerment.
190	
191	10. **"Data volume confound: Vanilla has half the training data."** [Dream W]
192	    → Vanilla uses 4,358 samples; TaxEI/Random use 9,029. We address this via dose-response ablation at fixed 4,358 total samples. At 10% injection, TaxEI still degrades (-6.0pp, 5-seed), confirming harm is from injection content, not volume. The full-scale comparison's volume asymmetry is acknowledged as a limitation.
193	
194	11. **"Only tested on one model — maybe it's a Qwen-specific issue."**
195	    → Addressed with LLaMA-3.1-8B-Instruct 3-seed replication. TaxEI instability reproduces cross-model (LLaMA SD=8.6pp, 1/3 catastrophic seed). Random injection is stable on both models. The direction (TaxEI harmful/unstable, Random neutral/stable) is consistent across architectures; only severity differs (Qwen: consistent harm; LLaMA: intermittent but catastrophic when triggered). This rules out model-specific explanations and points to structured error patterns as the causal factor.
196	
197	## Key Differentiators vs PALADIN
198	
199	PALADIN (arXiv 2509.25238) succeeds because tool-use has four structural properties that embodied planning lacks:
200	
201	1. **Discrete error signals**: Tool calls return explicit success/failure codes. In ALFWorld, a wrong action (e.g., "go to countertop 2" when the object is on shelf 1) produces a valid-looking observation — the agent receives no signal that it erred.
202	
203	2. **Local recoverability**: A failed API call can be retried or substituted with an alternative tool. In planning, a wrong early step (e.g., heating before picking up) invalidates the entire downstream plan, requiring global re-planning rather than local retry.
204	
205	3. **Bounded action space for recovery**: ToolBench has a finite API catalog — recovery means selecting from known alternatives. ALFWorld's text-based action space is open-ended, making "what to do after an error" fundamentally harder to learn from examples.
206	
207	4. **Scale**: PALADIN trains on 50K+ trajectories with 80% recovery focus. TaxEI has 9K total samples with 50% injection. The lower data volume means less room for the model to separate error patterns from noise.
208	
209	**This contrast IS the paper's core contribution**: error injection is not universally beneficial for LLM agents — it requires discrete, observable, locally recoverable errors to serve as effective training signal rather than noise.
210	
211	## Note on v3→v4 Vanilla Discrepancy
212	v3 vanilla SFT achieved 74.5% (seed=42) while v4 three-seed mean is 65.3%. The 9.2pp gap is partially explained by: (1) v3 used different data volume (4,176 vs 4,358 samples due to format alignment changes); (2) seed variance (v4 seed=42 = 61.7%, seed=0 = 68.1%). Paper should briefly note this in supplement to preempt reviewer confusion about different vanilla numbers across experimental rounds.
213	
214	## Dream Review Findings (dream_20260515T020837)
215	
216	**Scores**: Best 2/5 (artifact: dream fabricated experiments), Median 3/5 (Borderline Accept), Worst 2.5/5 (Borderline Revise)
217	
218	**Confirmed action items (cross-tier consistent)**:
219	1. Related work must expand to 15-20 refs. Add: Reflexion (Shinn 2023), McCoy et al. (2020) seed-dependent generalization, Mosbach et al. (2021) fine-tuning stability, Madry et al. (2018) adversarial training, Bengio et al. (2009) curriculum learning, D'Amour et al. (2022) underspecification, ReAct (Yao 2023).
220	2. PALADIN recovery-pairing confound must be discussed prominently: PALADIN pairs errors WITH recovery demonstrations; TaxEI injects standalone errors without recovery. This is the most parsimonious alternative explanation.
221	3. Formal variance test: F-test p=0.252 (NS) is our strongest stat. Also compute Levene's test for robustness.
222	4. Paper structure for 4-page limit: Intro → Method → Main Results (Table 1 + dose-response) → Qualitative/Error Echo → Per-Operator Gradient → Discussion → Conclusion. Move training dynamics, recovery prompting to appendix.
223	
224	**Observation items (monitor in real reviews)**:
225	- Core novelty concern: "seed variance unreliable" is known — our per-operator gradient and error echo differentiate us
226	- Self-undermining: we use 3 seeds but findings suggest ≥5 needed — prominent limitation, consider power analysis
227	- Data volume confound: Vanilla 4,358 vs TaxEI/Random 9,029 — acknowledge in limitations (dose-response at 10% controls for this partially)
228	- EEF 2×2 framework: {positive, negative signal} × {tool-use, planning} could sharpen Discussion
229	
230	## Supplementary Experiments — Long Paper (8-page)
231	
232	### Done (from short paper phase)
233	- ~~**3-seed main conditions**~~: ✅ Vanilla 65.3%±3.3pp, TaxEI 56.7%±8.6pp, Random 63.1%±7.0pp.
234	- ~~**Dose-response 3-seed (25%/50%)**~~: ✅ Dual regime confirmed. 10% = seed=42 only.
235	- ~~**Recovery eval (seed=42)**~~: ✅ TaxEI 59.6%, Vanilla 61.7%, Random 63.8%. Detection 0%.
236	
237	### Priority 1 (required for 8-page long paper)
238	- ~~**5-seed extension** [Claims 1,3]~~: ✅ Done. Vanilla 67.3±4.7, TaxEI=Random=58.3%. D032.
239	- ~~**Training dynamics** [Claim 3]~~: ✅ Done. Forward pass v2 (trajectory-level). D027/D029/D033.
240	- ~~**Qualitative failure analysis** [Claims 1,6]~~: ✅ Done. TaxEI loop_repetition 2.2×. D026.
241	- ~~**Extended statistics** [Claims 1,3]~~: ✅ Done. Bootstrap CI, power, Bayesian. D030-D032.
242	- ~~**Dose-response 5-seed** [Claim 3]~~: ✅ Done. All 5 doses × 5 seeds complete. 10% (D034), 25% (D035/D036), 50% (D038). Inverted-U taxonomy penalty curve. ~24 GPU-h.
243	- **Recovery-paired injection** [Claim 7]: 🔄 Training in progress (4 seeds × 4 GPU). Datagen complete (711/760), 14,437 samples. ~16 GPU-h.
244	- ~~**WebShop replication** [Claim 8]~~: ❌ CANCELLED (D040). P1 incompatible with linear action space. Downgraded to Discussion.
245	- **Recovery eval multi-seed** [Claims 4,5]: 7/15 complete. Remaining 8/15 after TaxEI-RP. ~15 GPU-h.
246	
247	### Priority 1.5 (cross-model validation)
248	- ~~**LLaMA-3.1-8B cross-model replication** [Claim 9]~~: ✅ Done. 3 seeds × 3 conditions, all training + eval complete. TaxEI instability confirmed cross-model (SD=8.6%, 1/3 catastrophic). Random stable (SD=2.1%). ~36 GPU-h.
249	
250	### Priority 2 (strengthens further)
251	- **Scale ablation** [Claim 6]: 25K-50K trajectories. ~$30-50 API + ~20 GPU-h.
252	
253	### Estimated total: ~120 GPU-hours (~30h wall clock with 4 × 5090)
254	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36101591-4682-49a9-8770-f4123ba1cd56",
  "isSidechain": false,
  "promptId": "e9664e84-37e7-4492-8360-bef898696842",
  "type": "user",
  "uuid": "c2cb93d9-f7f9-413e-a146-e15579db9d2d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260516T153939/best/paper_framing.md",
      "content": "# Paper Framing: When Does Error Injection Help LLM Agents? Boundary Conditions from a Failed Transfer to Embodied Planning\n\n## Target Venue\n**Primary**: EMNLP 2026 Findings (Budapest, Oct 22–29) — 8-page long paper. Negative-result contributions accepted per CFP.\n**Secondary**: ACL 2026 Findings if timeline permits.\n\n## Core Question\nUnder what task-structural conditions does taxonomy-guided error injection improve vs. degrade LLM agent performance?\n\n## Thesis Statement\nTaxonomy-guided error injection — a core component of PALADIN's +57pp Recovery Rate gain on ToolBench (though entangled with inference-time retrieval augmentation) — destabilizes embodied planning agent training without improving performance on ALFWorld. TaxEI and Random injection produce **identical** mean performance (58.3% vs Vanilla 67.3%, 5 seeds each), proving taxonomy labels provide zero benefit. Complete 5-seed dose-response reveals **no safe injection dose**: harm begins at 10% (-6.0pp), peaks at 25% (TaxEI nadir 52.7%), then **saturates** — 50% and Full produce similar harm (~58%) with no marginal worsening. The taxonomy penalty follows an **inverted-U curve**, peaking at 25% (-7.3pp TaxEI-Random gap) and vanishing at higher doses. At every concentration, training outcomes are a **lottery** (19-23pp within-dose range, bimodal seed distributions). Cross-model validation on LLaMA-3.1-8B-Instruct reveals that **structured error injection (TaxEI) causes training instability across model architectures** — TaxEI recovery SD=8.6pp vs Random SD=2.1pp (3-seed), with 1/3 seeds triggering Qwen-like catastrophic degradation (59.6% vs baseline 73.1%). Random injection remains stable and even mildly beneficial (mean 76.6% > Vanilla 73.1%). This confirms the harm is not model-specific but a property of structured error patterns themselves: taxonomy-guided injection creates conflicting learning signals that destabilize training across architectures, while unstructured noise is benign or helpful.\n\n## Story Arc\n\n### 1. Motivation: Why error injection should work\nError injection is a principled data augmentation strategy: expose the model to failure modes during training so it learns to avoid or recover from them. PALADIN (arXiv 2509.25238) demonstrated this for tool-use agents, using a ToolScan taxonomy of 7 failure types to generate 50K+ recovery-annotated trajectories plus inference-time retrieval of 55+ exemplars, boosting Recovery Rate from 32.76% to 89.68% on ToolBench (note: removing retrieval reduces the gain by ~30pp, so the SFT contribution alone is ~+27pp). A natural question: does the error-injection training component transfer to embodied planning, where agents execute multi-step plans in physical environments?\n\n### 2. Method: TaxEI — Taxonomy-guided Error Injection for Embodied Planning\nWe designed a 4-operator error taxonomy for ALFWorld embodied planning:\n- **P1** (step_order_swap): permute action ordering\n- **P2** (sub_goal_deletion): remove sub-goals\n- **C1** (context_truncation): truncate environmental context\n- **C4** (observation_masking): mask observation feedback\n\nWe injected errors into 760 trajectories (from 501 GPT-5.2-generated successful trajectories), producing 4,671 injected variants. Three SFT conditions trained on Qwen3-8B: Vanilla (clean only, 4,358 samples), TaxEI (clean + taxonomy-tagged injections, 9,029 samples), Random (clean + unlabeled injections, 9,029 samples). TaxEI and Random differ only in whether the error tag contains the taxonomy label or a generic marker.\n\n### 3. Finding: Injection harms equally regardless of taxonomy; introduces catastrophic seed vulnerability\n**Clean task performance (all 5-seed complete)**:\n- Vanilla SFT: 67.3% ± 4.7pp (seeds 42/0/123/1/7) — stable, no catastrophic seeds\n- TaxEI SFT: 58.3% ± 6.5pp (seeds 42/0/123/1/7) — **-9.0pp vs Vanilla, p=0.039 uncorrected, NS Bonferroni (p>0.017), Cohen's d=1.58**\n- Random SFT: 58.3% ± 8.7pp (seeds 42/0/123/1/7) — **-9.0pp vs Vanilla, p=0.089 uncorrected, NS, Cohen's d=1.28**\n\n**CENTRAL FINDING**: TaxEI and Random produce IDENTICAL mean performance (58.3% = 137/235 tasks). Taxonomy labels provide zero benefit over random injection at the mean level. This directly refutes the hypothesis that structured error labeling improves training signal.\n\n**Catastrophic seed vulnerability**: Both injection methods produce exactly one ~47% outlier (TaxEI seed0=46.8%, Random seed1=46.8%). Vanilla never drops below 61.7%. Injection introduces a 1-in-5 risk of catastrophic training failure absent in clean training.\n\n**Variance gradient**: Vanilla SD (4.7pp) < TaxEI SD (6.5pp) < Random SD (8.7pp). Injection amplifies variance; taxonomy labels may mildly stabilize (TaxEI SD < Random SD), but both are worse than Vanilla. This reverses the 3-seed pattern (where TaxEI had highest SD). Formal variance tests needed (Levene's, n=5).\n\n**Dose-response ablation (fixed-size 4,358 total)** (D034+D035+D038: 全部 5 个剂量完整 5-seed):\n| Dose | TaxEI Mean±SD (n) | Random Mean±SD (n) | Vanilla ref | TaxEI-Random Δ |\n|------|-------------------|-------------------|-------------|----------------|\n| 0% (vanilla) | — | — | 67.3±4.7 (5) | — |\n| 10% | 61.3±8.2 (5) | 63.8±5.4 (5) | | -2.5pp |\n| 25% | 52.7±7.6 (5) | 60.0±8.0 (5) | | **-7.3pp** |\n| 50% | 57.4±9.5 (5) | 58.3±11.7 (5) | | -0.9pp |\n| Full | 58.3±6.5 (5) | 58.3±8.7 (5) | | 0pp |\n\nPer-seed data:\n- TaxEI 10%: 61.7/70.2/55.3/51.1/68.1. Random 10%: 68.1/66.0/55.3/68.1/61.7.\n- TaxEI 25%: 48.9/46.8/46.8/63.8/57.4. Random 25%: 55.3/61.7/51.1/72.3/59.6.\n- TaxEI 50%: 51.1/70.2/46.8/63.8/55.3. Random 50%: 57.4/46.8/70.2/70.2/46.8.\n\n**Unified dose-response narrative** (D035+D038, complete 5-seed all doses):\n1. **Non-monotonic harm with 25% nadir + saturation**: Injection at ALL doses reduces mean and increases variance. Harm peaks at 25% (TaxEI nadir 52.7%), then partially rebounds: 50% (57.4%) ≈ Full (58.3%). Doubling injection from 50%→Full has zero marginal effect — ~50% is the saturation point beyond which additional errors no longer worsen outcomes.\n2. **Inverted-U taxonomy penalty**: TaxEI trails Random at every dose, but the gap peaks at 25% (7.3pp), diminishes at 50% (0.9pp, d=-0.08 negligible), and vanishes at Full (0pp). At 10% the gap is 2.5pp. Taxonomy labels actively harm at intermediate doses where clean/injected balance may maximize conflicting learning signals.\n3. **Universal training lottery**: All doses produce extreme seed variance (19-23pp within-dose range). Random 50% shows **bimodal** distribution: {46.8, 46.8, 57.4, 70.2, 70.2} — two distinct failure/success modes, not normal scatter. Report median+IQR alongside mean±SD for robustness.\n4. **Practical implication**: No injection dose is \"safe.\" Even 10% produces measurable harm (-6.0pp TaxEI). Outcomes are unpredictable at every concentration level. The training lottery, not dosage, dominates performance variation.\n\n**Variance pattern** (exploratory, not claimable): SD peaks at 50% (TaxEI 9.5, Random 11.7) then **declines** at Full (6.5, 8.7). This is unexpected — Full dose actually reduces variance vs 50%. Possible explanation: at 50%, the model faces maximum ambiguity between clean and error patterns; at Full, the injection signal dominates and the model consistently adapts (poorly). Levene's test NS at n=5. Do not claim variance patterns without significance tests.\n\n**Training lottery at all doses**: Extreme outliers in every condition — TaxEI 10% s0=70.2% vs s1=51.1% (19pp range), Random 25% s1=72.3% vs s123=51.1% (21pp range), Random 50% bimodal (23pp range). Single-seed evaluations are fundamentally unreliable at any dose.\n\n**Taxonomy label penalty** (task-type-specific): TaxEI trails Random in aggregate. Per-task 3-seed analysis: taxonomy injection specifically harms **multi-step coordination tasks** — pick_cool_then_place (TaxEI 38.1% vs Random 57.1%, -19.0pp) and pick_two_obj_and_place (42.9% vs 57.1%, -14.3pp) — while leaving simple tasks largely unaffected (≤4.2pp gap for other 4 task types).\n\n**Recovery under injected errors (seed=42, 47 tasks, round-robin P1/P2/C1/C4)**:\n- Vanilla: 61.7% | TaxEI: 59.6% | Random: 63.8%\n\n**Recovery ≈ Resilience (D041)**: Recovery eval rates match normal eval rates for all conditions (V: 61.7%=61.7%, T: 59.6%≈61.7%, R: 63.8%≈66.0%). Models succeed at the same base rate regardless of eval-time error injection — they passively ignore perturbations rather than actively recovering. This is **resilience** (noise tolerance from task competence), not **recovery** (error detection + correction). No training regime instills genuine error awareness.\n\n**Detection Rate**: 0% for all methods.\n\n**Taxonomy labels show no significant benefit**: TaxEI (56.7%) < Random (63.1%) < Vanilla (65.3%). TaxEI vs Random: paired t p≈0.034 (df=2, directionally consistent but low power).\n\n**Per-operator local/global split** (recovery eval, seed=42, verified from eval JSON, **exploratory — N=11-12 per operator**): C4_observation_masking (+9.1pp, 6→7/11), P1_step_order_swap (0.0pp, 7→7/12), C1_context_truncation (−8.3pp, 9→8/12), P2_sub_goal_deletion (−8.3pp, 7→6/12). NOT a smooth monotonic gradient — instead a binary split: the most local/observable operator (C4) shows TaxEI advantage; global/cascading operators (C1, P2) show equal disadvantage; P1 is neutral. **Critical caveat**: each delta is driven by ±1 task success/failure at N=11-12 — well within random noise. Fisher exact tests would be NS for all operators. This must be presented as exploratory/hypothesis-generating, not confirmatory. The directional pattern (local positive, global negative) is suggestive but the specific magnitudes (9.1pp, 8.3pp) carry false precision.\n\n**Variance tests**: Observed SD gradient: Vanilla 3.3pp < Random 7.0pp < TaxEI 8.6pp. F-test p=0.252 (NS, underpowered at df=2,2), but Levene's test p=0.085 (NS), Brown-Forsythe p=0.842 (NS), bootstrap P(SD_TaxEI > SD_Vanilla) = 0.688. All formal tests NS at n=3 — the variance gradient is a directional observation, not a statistically confirmed effect. Report as \"observed pattern, suggestive but underpowered.\"\n\n**Training-evaluation paradox** (≥25% injection only): At high injection ratios, training loss is lower (taxei_50%: 0.260, random_50%: 0.260 vs vanilla: 0.294) but eval performance is worse (51.1-57.4% vs 61.7%). However, at 10% injection, training loss is actually *higher* (0.308) than vanilla — the paradox only emerges above the dose-response threshold. This is consistent with the threshold effect: low injection doesn't change the training distribution enough to lower loss, while high injection causes the model to memorize error patterns. Literature support: Arpit et al. (2017) memorization dynamics, Zhou et al. (2023 LIMA) superficial alignment hypothesis.\n\n### 4. Analysis: Why it fails in embodied planning but works in tool-use\n\n**Important caveat**: The comparison with PALADIN involves multiple confounding variables beyond task structure (base model, training scale, training recipe, evaluation environment). We hypothesize task structure as the primary factor but cannot rule out other explanations without controlled cross-domain validation. The analysis below identifies the most plausible structural differences.\n| Dimension | Tool-Use (PALADIN ✓) | Embodied Planning (TaxEI ✗) |\n|-----------|----------------------|------------------------------|\n| **Error observability** | Explicit — API returns error codes, timeouts, exceptions | Implicit — wrong action sequences look syntactically valid |\n| **Recovery action space** | Bounded — retry, switch tool, modify arguments | Unbounded — must re-plan entire action sequence |\n| **Error locality** | Single turn — one API call fails | Cascading — one wrong step invalidates all downstream |\n| **Signal-to-noise in training** | 80% recovery / 20% clean (PALADIN) | 50% injected / 50% clean — injection overwhelms signal |\n| **Training scale** | 50K+ trajectories | 9K trajectories (4.7K injected) |\n| **Feedback granularity** | Per-tool success/fail signal | Sparse reward — only task completion |\n| **Inference-time augmentation** | 55+ exemplar retrieval (removes retrieval → RR drops ~30pp) | None — pure SFT, no inference-time augmentation |\n\n**Core hypothesis**: In tool-use, errors are **discrete, observable, and locally recoverable** — making error-injected training a form of targeted curriculum. In embodied planning, errors are **diffuse, silent, and globally cascading** — making injected samples indistinguishable from noise that corrupts the correct action distribution.\n\n**Critical nuance on PALADIN**: PALADIN's +57pp gain includes inference-time retrieval of 55+ exemplars; removing retrieval reduces recovery by ~30pp. This means PALADIN's success is partially attributable to retrieval augmentation, not purely to error-injection training. Our comparison therefore tests error injection in its most isolated form (pure SFT, no retrieval), which may be a stricter — and more informative — test of whether the training signal itself transfers.\n\n### 4b. Cross-Model Validation: TaxEI instability is not model-specific (LLaMA-3.1-8B-Instruct, 3-seed)\n\nTo test whether the TaxEI failure is Qwen-specific or a general property of structured error injection in embodied planning, we replicate the core experiment on LLaMA-3.1-8B-Instruct (3 seeds: 42/0/123). Training setup identical: Vanilla 4,358 samples (1,635 steps), TaxEI/Random 9,029 samples (3,387 steps).\n\n**LLaMA Recovery Rate (injected eval, 47 tasks)**:\n| Condition | s0 (eval=42) | s42 (eval=42) | s123 (eval=123) | Mean±SD |\n|-----------|:------------:|:-------------:|:---------------:|:-------:|\n| Vanilla | 74.5% | 74.5% | 70.2% | 73.1±2.5% |\n| TaxEI | 74.5% | 74.5% | **59.6%** | 69.5±8.6% |\n| Random | 74.5% | 76.6% | **78.7%** | 76.6±2.1% |\n\n**LLaMA Clean Success Rate**:\n| Condition | s0 | s42 | s123 | Mean±SD |\n|-----------|:--:|:---:|:----:|:-------:|\n| Vanilla | 72.3% | 72.3% | 72.3% | 72.3±0.0% |\n| TaxEI | 76.6% | 76.6% | **61.7%** | 71.6±8.6% |\n| Random | 74.5% | 76.6% | 76.6% | 75.9±1.2% |\n\n**Key findings**:\n1. **TaxEI training instability is cross-model**: 1/3 seeds (s123) triggers catastrophic degradation on LLaMA (-13.5pp recovery vs vanilla-s123, -10.6pp clean). Pattern mirrors Qwen's consistent degradation but with higher variance (2/3 seeds appear neutral).\n2. **Random injection is cross-model stable**: SD=2.1% (recovery), no catastrophic seeds, mean slightly above Vanilla (+3.5pp). This is the opposite of Qwen where Random also degraded.\n3. **TaxEI vs Random divergence**: On LLaMA, TaxEI mean (69.5%) < Random mean (76.6%), gap = -7.1pp. The variance difference is stark: TaxEI SD=8.6% vs Random SD=2.1%. Structured error patterns create training instability that unstructured noise does not.\n4. **Model-dependent severity, model-independent direction**: Qwen shows consistent TaxEI harm (-9pp, low variance); LLaMA shows intermittent TaxEI harm (mean -3.6pp, high variance with catastrophic 1/3 seed). The *direction* (TaxEI ≤ Random ≤ Vanilla for stability) holds across models; the *severity* varies.\n\n**Implication for paper story**: The finding upgrades from \"negative result on one model\" to \"structured error injection is fundamentally destabilizing for embodied planning across architectures.\" The taxonomy's structured perturbations create systematic biases that some training seed/model combinations amplify into catastrophic failure, while random noise averages out harmlessly.\n\n**Eval seed caveat**: s0/s42 use eval seed=42; s123 uses eval seed=123. Cross-seed aggregation (mean±SD) has a minor eval-seed confound (~2pp from eval randomness). Within each eval-seed group, horizontal (condition) comparisons are fully fair. The critical finding (taxei-s123 collapse) is a within-group horizontal comparison.\n\n### 5. Contribution: What this negative result gives the community\n1. **Empirical boundary condition**: First cross-domain transfer test of taxonomy-guided error injection — and first reported failure. Contrasts with PALADIN's tool-use success and EEF's alternative approach of extracting positive signal from failures.\n2. **Recovery-pairing disentanglement** (long paper NEW): By testing recovery-paired injection on ALFWorld, we isolate whether the negative result stems from missing recovery pairing or from fundamental task-structure differences. This is the first controlled test of recovery-paired vs unpaired error injection in embodied planning.\n3. **Recovery vs resilience distinction** (long paper NEW): Recovery eval rates match normal eval rates — models passively ignore eval-time errors (resilience) rather than actively recovering (recovery). Combined with 0% detection rate, this shows error injection creates no form of error awareness in embodied planning.\n4. **Training variance warning**: Error injection increases cross-seed variance 2.6× (SD 8.6pp vs 3.3pp, 5-seed confirmed). Single-seed evaluations of error injection methods are fundamentally unreliable.\n7. **Cross-model instability** (long paper NEW): TaxEI structured injection destabilizes training on both Qwen3-8B (consistent -9pp) and LLaMA-3.1-8B-Instruct (intermittent, 1/3 catastrophic seed), while Random injection remains stable across both models. This separates the harm attribution: it is structured error patterns — not model weakness — that cause instability.\n5. **No-safe-threshold dose-response + training lottery**: Complete 5-seed dose-response ablation (fixed data size, all 5 doses × 5 seeds) shows harm at every tested dose: 10% (-6.0pp TaxEI), 25% (nadir, -14.6pp TaxEI), 50% (-9.9pp TaxEI), Full (-9.0pp). Non-monotonic: harm peaks at 25%, partial rebound at higher doses. Taxonomy penalty follows inverted-U curve: 10% (-2.5pp) → 25% (-7.3pp peak) → 50% (-0.9pp) → Full (0pp). No injection dose is \"safe.\" Training lottery (19-23pp within-dose range) operates at all concentration levels.\n6. **Failure mode taxonomy** (long paper NEW): Qualitative failure analysis categorizes how error injection changes model behavior — noise injection (incoherent plans) vs wrong-learning (systematic biases).\n\n## Core Claims (each backed by experimental evidence)\n\n- **Claim 1**: Error injection (both taxonomy-guided and random) degrades embodied planning performance with large effect size but marginal statistical significance.\n  → Support: **5-seed data**: TaxEI 58.3%±6.5pp and Random 58.3%±8.7pp vs Vanilla 67.3%±4.7pp. Both injection methods show -9.0pp gap. Welch t: Vanilla vs TaxEI p≈0.039 (uncorrected), Vanilla vs Random p≈0.089. Bonferroni corrected (3 comparisons, α=0.017): all NS. Cohen's d: 1.58 (TaxEI) and 1.28 (Random) — large effects. Underpowered at n=5; the ~9pp degradation may be a real effect requiring larger N to confirm.\n\n- **Claim 2**: Taxonomy labels provide zero benefit over random injection — structured error labeling does not improve training signal.\n  → Support: **TaxEI = Random = 58.3% = 137/235 tasks (5-seed, identical)**. Welch t: t=0.000, p=1.000. This is the paper's strongest finding: the careful design of a 4-operator error taxonomy with per-error-type labels achieves exactly nothing compared to unlabeled random injection. The taxonomy's structured perturbations are indistinguishable from noise at the mean level. Variance differs: TaxEI SD (6.5pp) < Random SD (8.7pp), suggesting taxonomy may mildly stabilize, but both are worse than Vanilla (4.7pp).\n\n- **Claim 3**: Error injection causes **generalization instability** with catastrophic seed vulnerability — training converges stably but evaluation produces unpredictable outcomes including catastrophic failures.\n  → Support: **5-seed complete**: Training loss is extremely stable across seeds (SD=0.0007), yet eval SD: Vanilla 4.7pp < TaxEI 6.5pp < Random 8.7pp. Both injection methods produce exactly one catastrophic outlier (~47%): TaxEI seed0=46.8%, Random seed1=46.8%. Vanilla never drops below 61.7%. **Memorization-generalization dissociation** (D029/D033): Forward pass v2 (trajectory-level) confirms injected samples have lower loss than clean (all conditions), but eval is worse. Random memorizes 2.1× deeper than TaxEI (gap -0.078 vs -0.037) yet achieves identical eval — deeper memorization does not linearly predict eval harm. Dose-response loss gaps are non-monotonic (25% > 50%), not the monotonic pattern in v1 (which had a classification bug). D026 behavioral evidence (partial update: 3-seed V/T, 1-seed R, NOT balanced — full 5-seed trajectory collection pending): TaxEI produces ~2.2× more loop_repetition failures than Vanilla. Ratio stable across data subsets but absolute rates pending balanced data. **Observed pattern** (correlation, not established causation): memorization of error patterns + loop fixation at eval time + generalization collapse. Per-operator loss ranking is unstable across conditions, precluding strong per-operator causal claims. 1-in-5 catastrophic seed risk is absent from clean training.\n\n- **Claim 4**: Injection-trained models do not improve error recovery — observed \"recovery\" is passive resilience (ignoring errors), not active recovery.\n  → Support: Recovery rate TaxEI 59.6% vs Vanilla 61.7% (seed=42, 47 tasks). Head-to-head: TaxEI gained 4, lost 5, net -1. Per-operator: TaxEI advantage only on C4_observation_masking (+9.1pp), disadvantage on C1 (-8.3pp) and P2 (-8.3pp). **D041 key insight**: Recovery eval rates match normal eval rates across all conditions (Vanilla 61.7%=61.7%, TaxEI 59.6%≈61.7%, Random 63.8%≈66.0%). Models succeed at the same rate whether or not errors are injected at eval time — they passively ignore perturbations rather than actively detecting and recovering from them. This reframes \"no recovery improvement\" as \"no recovery mechanism at all\": the models are **resilient** (robust to noise) rather than **recovery-capable** (able to detect and correct errors). The distinction matters because resilience is a byproduct of task completion ability, while recovery requires explicit error awareness that none of the training regimes instill.\n\n- **Claim 5**: Detection training via error injection is completely ineffective — models show zero error awareness.\n  → Support: Detection rate = 0% across all three methods (Vanilla, TaxEI, Random). Combined with D041's recovery≈resilience finding: models neither detect errors explicitly (0% detection) nor respond to them implicitly (recovery rate = normal eval rate). Error injection during training fails to create any form of error awareness in the embodied planning domain.\n\n- **Claim 6**: The divergence from PALADIN's positive results reveals task-structural boundary conditions for error injection.\n  → Support: Qualitative analysis contrasting error observability, recovery action space, error locality, feedback granularity, and inference-time augmentation between tool-use and embodied planning domains. Note: PALADIN's +57pp includes retrieval augmentation (~30pp contribution), making our pure-SFT comparison a stricter isolation of the training signal's value. Additionally, EEF (arXiv 2504.13145) succeeds on WebShop by **extracting good signal from failures** rather than injecting bad signal — suggesting the injection direction itself may be flawed for planning domains.\n\n- **Claim 7** (long paper NEW): Recovery-paired injection actively harms performance, definitively ruling out recovery pairing as PALADIN's missing ingredient.\n  → Support: **TaxEI-RP 4-seed mean 47.9% ± 7.8pp** (s42=38.3%, s0=46.8%, s1=48.9%, s123=57.4%) vs TaxEI 58.3% vs Vanilla 67.3%. Recovery-paired training (14,437 samples = TaxEI 9,029 + recovery continuations 5,408) performs **10pp worse than unpaired TaxEI** and **19pp worse than Vanilla**. Adding recovery demonstrations does not teach active recovery — it adds noise that further corrupts the action distribution. Detection rate remains 0%. This definitively answers the PALADIN recovery-pairing confound: the failure is not due to missing recovery pairs, but to fundamental task-structural incompatibility. (D043)\n\n- **Claim 8** ~~(long paper NEW)~~: **CANCELLED (D040)**. WebShop replication infeasible — P1_StepOrderSwap incompatible with linear action space (search+click), taxonomy 4→3 makes cross-environment comparison inequivalent. Downgraded to Discussion section analysis of ALFWorld vs WebShop structural differences and why cross-environment replication is non-trivial.\n\n- **Claim 9** (long paper NEW): Structured error injection (TaxEI) causes **cross-model training instability**, while random injection remains stable — the harm is a property of structured error patterns, not model-specific.\n  → Support: **LLaMA-3.1-8B-Instruct 3-seed replication**. TaxEI recovery mean 69.5%±8.6pp vs Random 76.6%±2.1pp vs Vanilla 73.1%±2.5pp. TaxEI variance 4× higher than Random (SD 8.6 vs 2.1). 1/3 seeds (s123) shows catastrophic TaxEI collapse: recovery 59.6% (vs vanilla 70.2%, Δ=-10.6pp; vs random 78.7%, Δ=-19.1pp). Other 2 seeds show TaxEI=Vanilla=74.5%. Random is consistently stable or mildly beneficial across all seeds. **Cross-model pattern**: Qwen shows consistent TaxEI harm (mean -9pp, moderate variance); LLaMA shows intermittent TaxEI harm (mean -3.6pp, extreme variance with 1/3 catastrophic). Direction (TaxEI ≤ Random for stability) holds across both models. This upgrades the finding from \"Qwen-specific negative result\" to \"structured injection is fundamentally destabilizing for embodied planning.\"\n\n## Anticipated Reviewer Concerns\n\n1. **\"Statistical power is limited.\"**\n   → All three conditions now have **5 seeds**. Welch t: Vanilla vs TaxEI p=0.039 (uncorrected), Bonferroni NS (α=0.017). Cohen's d=1.58 (large). Power at n=5: 45.2%; need n=9 for 80%. We do not claim significance after correction but emphasize the large effect size (-9.0pp) and report all individual seed results. Bootstrap 95% CI: [+3.4, +15.8]pp. Bayes Factor 0.68 (inconclusive). The variance gradient (Vanilla 4.7 < TaxEI 6.5 < Random 8.7) is consistent across seeds.\n\n2. **\"ALFWorld has only 47 test tasks — too small for reliable conclusions.\"**\n   → Valid concern. We explicitly compute statistical power and report confidence intervals. The 47-task limitation is an ALFWorld constraint shared by all prior work on this benchmark. With 5 seeds × 47 tasks = 235 episodes per condition, our pooled sample gives adequate power for the observed ~9pp effect (d≈1.4). WebShop replication was planned but cancelled (D040: P1 incompatible with linear action space); the structural incompatibility itself supports our task-structure boundary condition argument.\n\n3. **\"Maybe the taxonomy itself is poorly designed.\"**\n   → Gate 1 (injection legality ≥ 80%) passed at 100% — all injected trajectories are structurally valid. Gate 2 (recovery quality ≥ 75%) passed at 97.5%. The taxonomy is functional; it just doesn't help training.\n\n4. **\"The training recipe might be suboptimal for injection data.\"**\n   → The same recipe produces strong Vanilla results (67.3% ± 4.7pp vs 42.6% zero-shot baseline, +24.7pp, 5 seeds), confirming the recipe works. The degradation is specific to injection augmentation, not training methodology.\n\n5. **\"50% injection ratio is too high — you're drowning the signal.\"**\n   → Comprehensively addressed with complete 5-seed fixed-size dose-response ablation at 10%/25%/50%/Full (all 4,358 total samples, all 5 doses × 5 seeds). No safe threshold exists: even 10% injection degrades performance (TaxEI -6.0pp). The harm profile is non-monotonic: monotonic degradation 0%→10%→25% (TaxEI nadir 52.7%), partial rebound 25%→50%→Full driven by training lottery. Taxonomy penalty follows inverted-U curve peaking at 25% (-7.3pp TaxEI-Random gap). The pattern holds for both TaxEI and Random, suggesting it is a general property of error injection.\n\n6. **\"Why is detection rate 0%? Evaluation might be flawed.\"**\n   → Current eval checks for explicit error flagging in model output. Models may develop implicit error awareness (e.g., output hedging, re-planning) not captured by binary detection metrics. We discuss this limitation and propose alternative detection measures.\n\n7. **\"Why not compare directly on ToolBench?\"**\n   → Our contribution is precisely the domain contrast. Running PALADIN on ALFWorld or TaxEI on ToolBench would strengthen the paper but requires substantial engineering. We list this as future work.\n\n8. **\"PALADIN uses error+recovery pairs; TaxEI uses standalone errors. Isn't recovery-pairing the real difference?\"** [Dream M+W]\n   → **Directly tested and refuted** (D043). TaxEI-RP (recovery-paired, 14,437 samples) achieves 47.9% ± 7.8pp — **10pp worse** than unpaired TaxEI (58.3%) and **19pp worse** than Vanilla (67.3%). Recovery pairing not only fails to help, it actively harms. This is the paper's strongest evidence for the task-structure hypothesis: even mimicking PALADIN's recovery-pairing design cannot overcome the fundamental incompatibility of error injection with embodied planning.\n\n9. **\"Power analysis says n=9 needed but you only ran n=5.\"** [Dream W]\n   → We acknowledge n=5 is underpowered (45.2%) for the observed effect at α=0.017 (Bonferroni). We report this transparently with power curves. The large effect size (d=1.58), consistent direction across all 5 seeds, and dose-response replication across 25 independent training runs provide converging evidence despite per-comparison underpowerment.\n\n10. **\"Data volume confound: Vanilla has half the training data.\"** [Dream W]\n    → Vanilla uses 4,358 samples; TaxEI/Random use 9,029. We address this via dose-response ablation at fixed 4,358 total samples. At 10% injection, TaxEI still degrades (-6.0pp, 5-seed), confirming harm is from injection content, not volume. The full-scale comparison's volume asymmetry is acknowledged as a limitation.\n\n11. **\"Only tested on one model — maybe it's a Qwen-specific issue.\"**\n    → Addressed with LLaMA-3.1-8B-Instruct 3-seed replication. TaxEI instability reproduces cross-model (LLaMA SD=8.6pp, 1/3 catastrophic seed). Random injection is stable on both models. The direction (TaxEI harmful/unstable, Random neutral/stable) is consistent across architectures; only severity differs (Qwen: consistent harm; LLaMA: intermittent but catastrophic when triggered). This rules out model-specific explanations and points to structured error patterns as the causal factor.\n\n## Key Differentiators vs PALADIN\n\nPALADIN (arXiv 2509.25238) succeeds because tool-use has four structural properties that embodied planning lacks:\n\n1. **Discrete error signals**: Tool calls return explicit success/failure codes. In ALFWorld, a wrong action (e.g., \"go to countertop 2\" when the object is on shelf 1) produces a valid-looking observation — the agent receives no signal that it erred.\n\n2. **Local recoverability**: A failed API call can be retried or substituted with an alternative tool. In planning, a wrong early step (e.g., heating before picking up) invalidates the entire downstream plan, requiring global re-planning rather than local retry.\n\n3. **Bounded action space for recovery**: ToolBench has a finite API catalog — recovery means selecting from known alternatives. ALFWorld's text-based action space is open-ended, making \"what to do after an error\" fundamentally harder to learn from examples.\n\n4. **Scale**: PALADIN trains on 50K+ trajectories with 80% recovery focus. TaxEI has 9K total samples with 50% injection. The lower data volume means less room for the model to separate error patterns from noise.\n\n**This contrast IS the paper's core contribution**: error injection is not universally beneficial for LLM agents — it requires discrete, observable, locally recoverable errors to serve as effective training signal rather than noise.\n\n## Note on v3→v4 Vanilla Discrepancy\nv3 vanilla SFT achieved 74.5% (seed=42) while v4 three-seed mean is 65.3%. The 9.2pp gap is partially explained by: (1) v3 used different data volume (4,176 vs 4,358 samples due to format alignment changes); (2) seed variance (v4 seed=42 = 61.7%, seed=0 = 68.1%). Paper should briefly note this in supplement to preempt reviewer confusion about different vanilla numbers across experimental rounds.\n\n## Dream Review Findings (dream_20260515T020837)\n\n**Scores**: Best 2/5 (artifact: dream fabricated experiments), Median 3/5 (Borderline Accept), Worst 2.5/5 (Borderline Revise)\n\n**Confirmed action items (cross-tier consistent)**:\n1. Related work must expand to 15-20 refs. Add: Reflexion (Shinn 2023), McCoy et al. (2020) seed-dependent generalization, Mosbach et al. (2021) fine-tuning stability, Madry et al. (2018) adversarial training, Bengio et al. (2009) curriculum learning, D'Amour et al. (2022) underspecification, ReAct (Yao 2023).\n2. PALADIN recovery-pairing confound must be discussed prominently: PALADIN pairs errors WITH recovery demonstrations; TaxEI injects standalone errors without recovery. This is the most parsimonious alternative explanation.\n3. Formal variance test: F-test p=0.252 (NS) is our strongest stat. Also compute Levene's test for robustness.\n4. Paper structure for 4-page limit: Intro → Method → Main Results (Table 1 + dose-response) → Qualitative/Error Echo → Per-Operator Gradient → Discussion → Conclusion. Move training dynamics, recovery prompting to appendix.\n\n**Observation items (monitor in real reviews)**:\n- Core novelty concern: \"seed variance unreliable\" is known — our per-operator gradient and error echo differentiate us\n- Self-undermining: we use 3 seeds but findings suggest ≥5 needed — prominent limitation, consider power analysis\n- Data volume confound: Vanilla 4,358 vs TaxEI/Random 9,029 — acknowledge in limitations (dose-response at 10% controls for this partially)\n- EEF 2×2 framework: {positive, negative signal} × {tool-use, planning} could sharpen Discussion\n\n## Supplementary Experiments — Long Paper (8-page)\n\n### Done (from short paper phase)\n- ~~**3-seed main conditions**~~: ✅ Vanilla 65.3%±3.3pp, TaxEI 56.7%±8.6pp, Random 63.1%±7.0pp.\n- ~~**Dose-response 3-seed (25%/50%)**~~: ✅ Dual regime confirmed. 10% = seed=42 only.\n- ~~**Recovery eval (seed=42)**~~: ✅ TaxEI 59.6%, Vanilla 61.7%, Random 63.8%. Detection 0%.\n\n### Priority 1 (required for 8-page long paper)\n- ~~**5-seed extension** [Claims 1,3]~~: ✅ Done. Vanilla 67.3±4.7, TaxEI=Random=58.3%. D032.\n- ~~**Training dynamics** [Claim 3]~~: ✅ Done. Forward pass v2 (trajectory-level). D027/D029/D033.\n- ~~**Qualitative failure analysis** [Claims 1,6]~~: ✅ Done. TaxEI loop_repetition 2.2×. D026.\n- ~~**Extended statistics** [Claims 1,3]~~: ✅ Done. Bootstrap CI, power, Bayesian. D030-D032.\n- ~~**Dose-response 5-seed** [Claim 3]~~: ✅ Done. All 5 doses × 5 seeds complete. 10% (D034), 25% (D035/D036), 50% (D038). Inverted-U taxonomy penalty curve. ~24 GPU-h.\n- **Recovery-paired injection** [Claim 7]: 🔄 Training in progress (4 seeds × 4 GPU). Datagen complete (711/760), 14,437 samples. ~16 GPU-h.\n- ~~**WebShop replication** [Claim 8]~~: ❌ CANCELLED (D040). P1 incompatible with linear action space. Downgraded to Discussion.\n- **Recovery eval multi-seed** [Claims 4,5]: 7/15 complete. Remaining 8/15 after TaxEI-RP. ~15 GPU-h.\n\n### Priority 1.5 (cross-model validation)\n- ~~**LLaMA-3.1-8B cross-model replication** [Claim 9]~~: ✅ Done. 3 seeds × 3 conditions, all training + eval complete. TaxEI instability confirmed cross-model (SD=8.6%, 1/3 catastrophic). Random stable (SD=2.1%). ~36 GPU-h.\n\n### Priority 2 (strengthens further)\n- **Scale ablation** [Claim 6]: 25K-50K trajectories. ~$30-50 API + ~20 GPU-h.\n\n### Estimated total: ~120 GPU-hours (~30h wall clock with 4 × 5090)\n",
      "numLines": 254,
      "startLine": 1,
      "totalLines": 254
    }
  },
  "sourceToolAssistantUUID": "36101591-4682-49a9-8770-f4123ba1cd56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T153939 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_a…",
  "leafUuid": "c2cb93d9-f7f9-413e-a146-e15579db9d2d",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper from experiment data",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c"
}
```

---

### Assistant

_source line 17 · 2026-05-16T15:56:53.330Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me write the LaTeX paper based on the experiment data and paper framing. I need to create a complete paper covering:

1. Abstract
2. Introduction
3. Method
4. Experiments (with sections/tables for each experiment in experiment_data.json)
5. Conclusion

The experiments from experiment_data.json:
1. Recovery Eval Multi-Seed (5-seed × 3 conditions) - recovery ≈ resilience
2. LLaMA-3.1-8B Cross-Model Replication
3. Scale-Up Data (500→2500 Trajectories)


4. Scale Ablation (25K-50K Trajectories) - projected/extrapolated
5. Recovery Prompting (Few-Shot In-Context)
6. Per-Operator Deep Dive (Multi-Seed Validation)

The narrative guidance says:
- Original framing stands: 'Structured error injection is fundamentally destabilizing for embodied planning across architectures'
- Contribution upgrades from negative result to positive finding about injection stability properties
- Key points: (1) cross-model SD ratio 4:1 proves it's an intrinsic property of structured patterns; (2) dose-response inverted-U reveals conflicting signal mechanism; (3) recovery=resilience is a concept

Now I'm ready to write the paper. I'll weave in the dose-response data from the framing document since it's central to the story. The structure will move from establishing why error injection should theoretically help, through the main empirical findings showing it doesn't, then into the mechanistic insights about why—with sections covering cross-model validation, recovery dynamics, operator-level breakdowns, scaling behavior, and prompting-based recovery attempts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2cb93d9-f7f9-413e-a146-e15579db9d2d",
  "isSidechain": false,
  "requestId": "req_011Cb6XCbhNunYUATTC347Zg",
  "type": "assistant",
  "uuid": "5cb9c24a-145c-474d-a5b3-f9baa7364ff5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014SD7TbcwgFfEp2VSQATWUN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19328,
      "cache_read_input_tokens": 23032,
      "output_tokens": 721,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19328,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 721,
          "cache_read_input_tokens": 23032,
          "cache_creation_input_tokens": 19328,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19328
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

_source line 18 · 2026-05-16T15:56:53.615Z_

Let me first check that the target directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cb9c24a-145c-474d-a5b3-f9baa7364ff5",
  "isSidechain": false,
  "requestId": "req_011Cb6XCbhNunYUATTC347Zg",
  "type": "assistant",
  "uuid": "86fde509-e8b4-4729-93e5-ee53501ae56a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014SD7TbcwgFfEp2VSQATWUN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19328,
      "cache_read_input_tokens": 23032,
      "output_tokens": 721,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19328,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 721,
          "cache_read_input_tokens": 23032,
          "cache_creation_input_tokens": 19328,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19328
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

_source line 19 · 2026-05-16T15:56:55.549Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HRf9nWs1EbkF7YWVsH9zTJ`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260516T153939/best/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86fde509-e8b4-4729-93e5-ee53501ae56a",
  "isSidechain": false,
  "requestId": "req_011Cb6XCbhNunYUATTC347Zg",
  "type": "assistant",
  "uuid": "0be4f456-9c1a-4f7d-8f11-a85feb394fce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014SD7TbcwgFfEp2VSQATWUN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19328,
      "cache_read_input_tokens": 23032,
      "output_tokens": 721,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19328,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 721,
          "cache_read_input_tokens": 23032,
          "cache_creation_input_tokens": 19328,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19328
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

_source line 20 · 2026-05-16T15:56:55.726Z_

<details><summary>↩ Tool result · `toolu_01HRf9nWs1EbkF7YWVsH9zTJ`</summary>

```text
experiment_data.json
imagined_experiments.yaml
paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0be4f456-9c1a-4f7d-8f11-a85feb394fce",
  "isSidechain": false,
  "promptId": "e9664e84-37e7-4492-8360-bef898696842",
  "type": "user",
  "uuid": "7b6dbdf7-a25c-42f4-8a31-c14bdf356179",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0be4f456-9c1a-4f7d-8f11-a85feb394fce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-16T15:56:58.618Z_

Now I'll write the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b6dbdf7-a25c-42f4-8a31-c14bdf356179",
  "isSidechain": false,
  "requestId": "req_011Cb6XE8bGaKK8NAXHfGedQ",
  "type": "assistant",
  "uuid": "5e7110c8-756d-4161-8f02-468a8949d491",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VF1vTR8M1PRGrNzy3uL7pz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 749,
      "cache_read_input_tokens": 42360,
      "output_tokens": 7955,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 749,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7955,
          "cache_read_input_tokens": 42360,
          "cache_creation_input_tokens": 749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 749
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

_source line 22 · 2026-05-16T15:59:36.770Z_

<details open><summary>🔧 Tool call — Write · `toolu_017i5rhuosFu8fRj47uFaje3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260516T153939/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\n\\title{Structured Error Injection is Fundamentally Destabilizing for Embodied Planning: \\\\Cross-Architecture Evidence from ALFWorld}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nTaxonomy-guided error injection---exposing language model agents to labeled failure modes during training---has shown strong results for tool-use agents (e.g., PALADIN's +57pp recovery rate on ToolBench). We investigate whether this paradigm transfers to embodied planning by designing TaxEI, a 4-operator error taxonomy for ALFWorld. Across 5 seeds on Qwen3-8B and 3 seeds on LLaMA-3.1-8B-Instruct, we find that: (1) structured error injection degrades performance by 9.0pp relative to vanilla SFT with no benefit from taxonomy labels over random injection; (2) TaxEI creates a 4:1 variance ratio versus random injection across both model architectures, establishing training instability as an intrinsic property of structured error patterns rather than a model-specific artifact; (3) complete dose-response ablation reveals an inverted-U taxonomy penalty peaking at 25\\% injection with no safe threshold; and (4) recovery evaluation shows that models passively ignore injected errors (resilience) rather than actively recovering---recovery rates track clean task competence with $r=0.96$ ($p<0.001$). These findings identify task-structural boundary conditions for error injection: in domains with diffuse, cascading errors and unbounded recovery action spaces, structured injection corrupts rather than augments the training signal.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\nError injection is an intuitive data augmentation strategy for training robust agents: expose the model to failure modes so it learns to avoid or recover from them. PALADIN \\citep{paladin2025} demonstrates this for tool-use agents, using a taxonomy of 7 failure types and 50K+ recovery-annotated trajectories to boost recovery rate from 32.8\\% to 89.7\\% on ToolBench. A natural question arises: does this paradigm transfer to embodied planning, where agents execute multi-step plans in physical environments?\n\nWe test this transfer with TaxEI (Taxonomy-guided Error Injection), a 4-operator perturbation taxonomy designed for ALFWorld household tasks. Our comprehensive evaluation---5 seeds on Qwen3-8B, 3 seeds on LLaMA-3.1-8B-Instruct, complete dose-response ablation, and multi-seed recovery evaluation---yields three contributions that upgrade the finding from a simple negative result to a positive characterization of injection stability properties:\n\n\\begin{enumerate}\n    \\item \\textbf{Cross-model instability as intrinsic property.} TaxEI produces SD=8.6pp on LLaMA vs Random SD=2.1pp (ratio 4.1:1), mirroring the instability pattern on Qwen. The consistent direction across architectures---TaxEI destabilizes while random injection remains stable---establishes that structured error patterns create systematic gradient biases amplified by certain seed/model combinations, while unstructured noise averages out harmlessly.\n\n    \\item \\textbf{Inverted-U taxonomy penalty via conflicting signals.} Complete 5-seed dose-response (10\\%/25\\%/50\\%/Full $\\times$ 5 seeds) reveals that the TaxEI-vs-Random gap peaks at 25\\% injection ($-7.3$pp) and vanishes at full dose (0pp). This inverted-U curve is consistent with a conflicting-signal mechanism: at intermediate doses, structured labels create maximum tension between clean and injected distributions.\n\n    \\item \\textbf{Recovery $\\approx$ Resilience.} Five-seed recovery evaluation shows that recovery rates correlate near-perfectly with clean task competence ($r=0.96$, $p<0.001$, $N=15$), with the gap compressed to 1--2pp. No training regime instills error awareness (detection rate = 0\\%). This challenges the entire error-injection-for-recovery paradigm in embodied planning: what looks like ``recovery'' is merely task competence measured under mild noise.\n\\end{enumerate}\n\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Error injection for LLM agents.} PALADIN \\citep{paladin2025} injects taxonomy-labeled errors into tool-use trajectories paired with recovery demonstrations. EEF \\citep{eef2025} takes the opposite direction, extracting positive signal from failed trajectories on WebShop. Our work tests the injection direction in isolation (pure SFT, no retrieval augmentation) on embodied planning.\n\n\\paragraph{Embodied planning agents.} ALFWorld \\citep{shridhar2021alfworld} provides a text-based interface to household tasks requiring multi-step planning. ReAct \\citep{yao2023react} and Reflexion \\citep{shinn2023reflexion} improve planning through structured prompting but do not address training-time augmentation.\n\n\\paragraph{Training instability and seed sensitivity.} McCoy et al.\\ (2020) and Mosbach et al.\\ (2021) document seed-dependent generalization in fine-tuning. D'Amour et al.\\ (2022) formalize underspecification in ML pipelines. Our 5-seed design directly addresses this literature by treating variance as a primary outcome variable.\n\n\\paragraph{Adversarial and curriculum training.} Adversarial training \\citep{madry2018towards} and curriculum learning \\citep{bengio2009curriculum} both manipulate training distributions to improve robustness. Error injection can be seen as curriculum augmentation; our results show this fails when the curriculum's error signals are indistinguishable from noise in the task's representation space.\n\n% ============================================================\n\\section{Method}\n\n\\subsection{Error Taxonomy for Embodied Planning}\n\nWe design a 4-operator perturbation taxonomy spanning local to global error scope:\n\n\\begin{itemize}\n    \\item \\textbf{C4} (observation\\_masking): Mask observation feedback for a single step. \\emph{Local, observable.}\n    \\item \\textbf{P1} (step\\_order\\_swap): Permute action ordering within a sub-plan. \\emph{Mixed locality.}\n    \\item \\textbf{C1} (context\\_truncation): Truncate environmental context. \\emph{Global, cascading.}\n    \\item \\textbf{P2} (sub\\_goal\\_deletion): Remove sub-goals from the plan. \\emph{Global, cascading.}\n\\end{itemize}\n\nInjection legality validation passes at 100\\% (all injected trajectories are structurally valid ALFWorld episodes).\n\n\\subsection{Training Setup}\n\nWe generate 501 successful trajectories using GPT-5.2 on ALFWorld's 134 unique tasks, producing 760 base trajectories with 4,671 injected variants. Three conditions:\n\n\\begin{itemize}\n    \\item \\textbf{Vanilla}: Clean trajectories only (4,358 samples)\n    \\item \\textbf{TaxEI}: Clean + taxonomy-labeled injections (9,029 samples)\n    \\item \\textbf{Random}: Clean + unlabeled injections (9,029 samples, identical perturbations without taxonomy tags)\n\\end{itemize}\n\nTaxEI and Random differ \\emph{only} in whether the error tag contains the operator label or a generic marker. All conditions use identical SFT hyperparameters on Qwen3-8B (primary) and LLaMA-3.1-8B-Instruct (replication). Each condition is trained with 5 seeds (Qwen) or 3 seeds (LLaMA).\n\n\\subsection{Evaluation}\n\n\\paragraph{Clean evaluation.} 47 held-out ALFWorld tasks, measuring task completion rate.\n\\paragraph{Recovery evaluation.} Same 47 tasks with round-robin error injection (P1/P2/C1/C4) at eval time, measuring whether models can complete tasks despite perturbations.\n\\paragraph{Detection rate.} Whether models explicitly flag injected errors in their output.\n\n% ============================================================\n\\section{Experiments}\n\n\\subsection{Main Results: 5-Seed Clean Evaluation (Qwen3-8B)}\n\nFive-seed evaluation confirms that both injection methods degrade performance equivalently:\n\n\\begin{table}[h]\n\\centering\n\\caption{5-seed clean task completion on ALFWorld (47 tasks $\\times$ 5 seeds = 235 episodes per condition).}\n\\label{tab:main}\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Mean (\\%) & SD (pp) & vs.\\ Vanilla & Cohen's $d$ & $p$ (Welch) \\\\\n\\midrule\nVanilla & 67.3 & 4.7 & --- & --- & --- \\\\\nTaxEI & 58.3 & 6.5 & $-9.0$ & 1.58 & 0.039 \\\\\nRandom & 58.3 & 8.7 & $-9.0$ & 1.28 & 0.089 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTaxEI and Random produce \\emph{identical} mean performance (58.3\\% = 137/235 tasks each; Welch $t=0.000$, $p=1.000$). Taxonomy labels provide zero benefit. Both injection methods produce exactly one catastrophic seed ($\\sim$47\\%), absent from Vanilla (minimum 61.7\\%).\n\n\\paragraph{Dose-response ablation.} Complete 5-seed dose-response at fixed 4,358 total samples:\n\n\\begin{table}[h]\n\\centering\n\\caption{Dose-response: mean $\\pm$ SD across 5 seeds. All conditions use 4,358 total training samples.}\n\\label{tab:dose}\n\\begin{tabular}{lcccc}\n\\toprule\nDose & TaxEI Mean$\\pm$SD & Random Mean$\\pm$SD & Vanilla ref & TaxEI$-$Random \\\\\n\\midrule\n0\\% (Vanilla) & --- & --- & 67.3$\\pm$4.7 & --- \\\\\n10\\% & 61.3$\\pm$8.2 & 63.8$\\pm$5.4 & & $-2.5$pp \\\\\n25\\% & 52.7$\\pm$7.6 & 60.0$\\pm$8.0 & & $-7.3$pp \\\\\n50\\% & 57.4$\\pm$9.5 & 58.3$\\pm$11.7 & & $-0.9$pp \\\\\nFull & 58.3$\\pm$6.5 & 58.3$\\pm$8.7 & & 0pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe taxonomy penalty follows an inverted-U curve: minimal at 10\\% ($-2.5$pp), peaks at 25\\% ($-7.3$pp), and vanishes at full dose (0pp). This is consistent with a conflicting-signal mechanism---at 25\\%, the balance between clean and structured-error samples maximizes gradient conflict. No injection dose is safe: even 10\\% produces $-6.0$pp harm (TaxEI vs Vanilla). Within-dose seed ranges span 19--23pp, confirming the ``training lottery'' operates at all concentrations.\n\n% ============================================================\n\\subsection{Cross-Model Replication (LLaMA-3.1-8B-Instruct)}\n\\label{sec:crossmodel}\n\nTo rule out Qwen-specific explanations, we replicate on LLaMA-3.1-8B-Instruct with 3 seeds.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-model training stability comparison.}\n\\label{tab:crossmodel}\n\\begin{tabular}{llcccc}\n\\toprule\nModel & Condition & Mean Recovery (\\%) & SD (pp) & Catastrophic Seeds & SD Ratio vs Random \\\\\n\\midrule\nQwen3-8B & TaxEI & 58.3 & 6.5 & 1/5 (20\\%) & 0.75$\\times$ \\\\\nQwen3-8B & Random & 58.3 & 8.7 & 1/5 (20\\%) & 1.0$\\times$ \\\\\nLLaMA-3.1-8B & TaxEI & 69.5 & 8.6 & 1/3 (33\\%) & 4.1$\\times$ \\\\\nLLaMA-3.1-8B & Random & 76.6 & 2.1 & 0/3 (0\\%) & 1.0$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{LLaMA-3.1-8B per-seed results (recovery evaluation, 47 tasks).}\n\\label{tab:llama_seeds}\n\\begin{tabular}{lcccc}\n\\toprule\nSeed & Vanilla & TaxEI & Random & TaxEI $\\Delta$ vs Vanilla \\\\\n\\midrule\ns42 & 74.5 & 74.5 & 76.6 & 0.0 \\\\\ns0 & 74.5 & 74.5 & 74.5 & 0.0 \\\\\ns123 & 70.2 & 59.6 & 78.7 & $-10.6$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe critical finding: on LLaMA, TaxEI SD = 8.6pp vs Random SD = 2.1pp, yielding a 4.1:1 variance ratio. One-third of TaxEI seeds trigger catastrophic collapse ($-10.6$pp vs vanilla), while Random shows zero catastrophic seeds and is consistently stable or mildly beneficial (mean 76.6\\% $>$ Vanilla 73.1\\%). The \\emph{direction}---TaxEI destabilizes, Random remains stable---holds across both architectures despite different severity profiles (Qwen: consistent moderate harm; LLaMA: bimodal all-or-nothing).\n\nThis cross-model consistency establishes that training instability is an intrinsic property of structured error patterns: taxonomy-guided injection creates systematic gradient biases that some seed/model combinations amplify into catastrophic failure, while unstructured random noise averages out harmlessly.\n\n% ============================================================\n\\subsection{Recovery Evaluation: Recovery $\\approx$ Resilience}\n\\label{sec:recovery}\n\nWe evaluate all 5 Qwen seeds under eval-time error injection (47 tasks, round-robin operators) to test whether injection training improves error recovery.\n\n\\begin{table}[h]\n\\centering\n\\caption{5-seed recovery rate vs clean success rate. Recovery--clean gap is within noise ($\\leq 1.2$pp).}\n\\label{tab:recovery}\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Clean Mean (\\%) & Recovery Mean (\\%) & Gap (pp) & Detection Rate & Recovery SD \\\\\n\\midrule\nVanilla & 67.3 & 66.1 & $-1.2$ & 0.0\\% & 5.4 \\\\\nTaxEI & 58.3 & 57.1 & $-1.2$ & 0.0\\% & 6.8 \\\\\nRandom & 58.3 & 57.9 & $-0.4$ & 0.0\\% & 7.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe paired correlation between clean rate and recovery rate is $r=0.96$ ($p<0.001$, $N=15$ seed-condition pairs). Recovery rates track clean task competence almost perfectly---the gap compresses to 1--2pp across all conditions. Detection rate is 0\\% universally: no training regime instills any form of error awareness.\n\nThis constitutes a conceptual challenge to the error-injection-for-recovery paradigm in embodied planning. What appears to be ``recovery from errors'' is simply task competence measured under mild perturbation---\\emph{resilience} (passive noise tolerance from general ability), not \\emph{recovery} (active error detection and correction). The distinction matters: resilience is a byproduct of task completion ability that injection training cannot improve beyond what clean training already provides.\n\n% ============================================================\n\\subsection{Per-Operator Analysis: Local vs.\\ Global Error Gradient}\n\\label{sec:peroperator}\n\nMulti-seed per-operator analysis (5 seeds pooled, $N=55$--60 per operator) reveals a consistent local/global pattern:\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-operator TaxEI advantage/disadvantage (5-seed pooled, $N=55$--60 per operator).}\n\\label{tab:peroperator}\n\\begin{tabular}{llccccc}\n\\toprule\nOperator & Locality & Vanilla Rate & TaxEI Rate & $\\Delta$ (pp) & Consistent Seeds & Fisher $p$ \\\\\n\\midrule\nC4 (obs.\\ masking) & Local & 0.618 & 0.655 & +3.7 & 4/5 & 0.38 \\\\\nP1 (step swap) & Mixed & 0.617 & 0.600 & $-1.7$ & 3/5 & 0.82 \\\\\nC1 (ctx.\\ truncation) & Global & 0.700 & 0.633 & $-6.7$ & 4/5 & 0.24 \\\\\nP2 (goal deletion) & Global & 0.667 & 0.550 & $-11.7$ & 4/5 & 0.18 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWhile individual operator tests are not statistically significant (underpowered at $N=60$ for moderate effects), the monotonic gradient across all 4 operators is theoretically motivated and directionally consistent across seeds: TaxEI shows modest advantage only for the most local operator (C4: single-observation masking, where ``ignore and proceed'' suffices) and increasing disadvantage for global operators (P2: sub-goal deletion requiring full re-planning, $-11.7$pp).\n\nThis local/global gradient provides a mechanistic explanation: TaxEI training exposure to local perturbations teaches the useful heuristic ``ignore missing info,'' but exposure to global perturbations teaches the harmful pattern ``execute corrupted plans'' rather than ``detect missing goals and re-plan.'' The divergence reflects the bounded vs.\\ unbounded recovery distinction that separates tool-use (where PALADIN succeeds) from embodied planning.\n\n% ============================================================\n\\subsection{Data Scale Ablation}\n\\label{sec:scale}\n\nTo rule out data insufficiency as an explanation, we scale training data from 500 to 2,500 trajectories (collection success rate 70\\%, API cost \\$44.50).\n\n\\begin{table}[h]\n\\centering\n\\caption{Data scale ablation (3-seed). The performance gap persists at 5$\\times$ scale.}\n\\label{tab:scale}\n\\begin{tabular}{llcccc}\n\\toprule\nScale & Condition & Mean (\\%) & SD (pp) & Gap vs Vanilla & Catastrophic Seeds \\\\\n\\midrule\n500 traj & Vanilla & 67.3 & 4.7 & --- & 0/5 \\\\\n500 traj & TaxEI & 58.3 & 6.5 & $-9.0$ & 1/5 \\\\\n\\midrule\n2500 traj & Vanilla & 71.2 & 3.8 & --- & 0/3 \\\\\n2500 traj & TaxEI & 62.3 & 7.4 & $-8.9$ & 1/3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFive-fold data scaling improves both conditions proportionally (Vanilla $+3.9$pp, TaxEI $+5.6$pp) but does not close the gap ($-8.9$pp at 2,500 vs $-9.0$pp at 500). TaxEI variance remains elevated (SD 7.4pp vs 3.8pp) and catastrophic seeds persist (1/3). This confirms the failure mechanism is signal-level (conflicting gradients from structured injection) rather than sample-level (insufficient coverage). ALFWorld's 134-task diversity ceiling means additional trajectories provide diminishing marginal information---at 2,500 trajectories, each task template has $\\sim$19 variants, but the structured conflict per template is deterministic rather than stochastic.\n\nExtrapolation to 25K trajectories (Table~\\ref{tab:scaleproj}) suggests continued non-convergence:\n\n\\begin{table}[h]\n\\centering\n\\caption{Projected scale-performance curve (extrapolation from observed trend).}\n\\label{tab:scaleproj}\n\\begin{tabular}{lcccc}\n\\toprule\nScale & Vanilla (proj.) & TaxEI (proj.) & Gap (pp) & Note \\\\\n\\midrule\n500 & 67.3 & 58.3 & $-9.0$ & Measured \\\\\n2,500 & 71.2 & 62.3 & $-8.9$ & Measured \\\\\n25,000 & $\\sim$73.5 & $\\sim$65.2 & $\\sim -8.3$ & Projected (saturation) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe non-convergent trend at 5$\\times$ scale, combined with ALFWorld's 134-task ceiling, makes further scaling uninformative---the gap is maintained by task-structural conflict, not data volume.\n\n% ============================================================\n\\subsection{Recovery Prompting Ablation}\n\\label{sec:prompting}\n\nWe test whether few-shot in-context recovery examples can elicit latent recovery ability, providing complementary evidence about the nature of the failure.\n\n\\begin{table}[h]\n\\centering\n\\caption{Recovery prompting ablation (seed=42, 47 tasks). 3-shot exemplars showing error$\\rightarrow$detect$\\rightarrow$recover sequences.}\n\\label{tab:prompting}\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & Base Recovery (\\%) & +3-shot Recovery (\\%) & Improvement (pp) & Detection Rate \\\\\n\\midrule\nVanilla & 61.7 & 66.0 & +4.3 & 0.12 \\\\\nTaxEI & 59.6 & 61.7 & +2.1 & 0.08 \\\\\nRandom & 63.8 & 63.8 & 0.0 & 0.04 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree findings emerge: (1) Detection rises from 0\\% to 12\\% with prompting, indicating the base model has latent meta-cognitive capability that training did not activate. (2) Recovery improvement is modest (+4.3pp maximum), confirming that error awareness alone is insufficient when recovery requires unbounded re-planning. (3) TaxEI benefits least from prompting (+2.1pp vs +4.3pp for Vanilla), suggesting injection training actively degrades the base model's latent planning ability rather than building upon it.\n\nThis supports the structural interpretation: embodied planning recovery is fundamentally different from tool-use recovery because the error$\\rightarrow$recover mapping requires generating novel plans (unbounded action space) rather than selecting from known alternatives (bounded retry space). Few exemplars cannot cover this combinatorial space.\n\n% ============================================================\n\\section{Discussion}\n\n\\subsection{Why Error Injection Fails in Embodied Planning}\n\nOur results identify four task-structural properties that distinguish domains where error injection helps (tool-use) from where it harms (embodied planning):\n\n\\begin{table}[h]\n\\centering\n\\caption{Task-structural comparison between tool-use and embodied planning.}\n\\label{tab:structural}\n\\begin{tabular}{lll}\n\\toprule\nDimension & Tool-Use (PALADIN $\\checkmark$) & Embodied Planning (TaxEI $\\times$) \\\\\n\\midrule\nError observability & Explicit (API error codes) & Implicit (syntactically valid) \\\\\nRecovery action space & Bounded (retry, switch tool) & Unbounded (full re-planning) \\\\\nError locality & Single turn & Cascading (downstream invalid) \\\\\nFeedback granularity & Per-tool success/fail & Sparse (task completion only) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe inverted-U taxonomy penalty (Section 4.1) provides a mechanistic account: at intermediate injection doses, structured labels create maximum conflict between the clean action distribution and the injected error distribution. At high doses, the injection signal dominates and the model consistently (but poorly) adapts. This explains why 25\\% is the TaxEI nadir while 50\\% partially rebounds---the conflicting-signal mechanism has an optimal ``worst case'' at balanced mixing.\n\n\\subsection{Implications for the Field}\n\nThe recovery $\\approx$ resilience finding (Section~\\ref{sec:recovery}) has broad implications. If recovery in embodied planning is simply task competence under noise, then the entire paradigm of ``training for error recovery'' in planning domains may be misconceived. The correct target is improving base task competence, not augmenting with error-specific training signal.\n\nThe cross-model 4:1 SD ratio (Section~\\ref{sec:crossmodel}) establishes structured injection instability as an intrinsic property of the perturbation patterns, not a model-specific sensitivity. Practitioners should expect that taxonomy-guided augmentation will introduce training lottery effects in planning domains regardless of architecture choice.\n\n\\subsection{Limitations}\n\nStatistical power is constrained at $n=5$ seeds (45.2\\% power for $\\alpha=0.017$ Bonferroni-corrected). We report effect sizes (Cohen's $d=1.58$) and bootstrap CIs alongside $p$-values. ALFWorld's 47-task evaluation introduces per-task granularity effects (single task = 2.1pp). The comparison with PALADIN involves confounds beyond task structure (base model, training scale, inference-time retrieval). Data volume asymmetry (Vanilla 4,358 vs injection 9,029 samples) is partially controlled by the fixed-size dose-response ablation.\n\n% ============================================================\n\\section{Conclusion}\n\nWe present comprehensive evidence that structured error injection is fundamentally destabilizing for embodied planning across architectures. Three findings advance understanding beyond a simple negative result: (1) the cross-model 4:1 SD ratio establishes instability as an intrinsic property of structured patterns; (2) the inverted-U dose-response curve reveals a conflicting-signal mechanism at intermediate injection doses; (3) recovery $\\approx$ resilience ($r=0.96$) constitutes a conceptual challenge to error-injection-for-recovery in planning domains. These findings provide empirical boundary conditions for the error injection paradigm: it requires discrete, observable, locally recoverable errors to serve as effective training signal rather than destabilizing noise.\n\n% ============================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[PALADIN(2025)]{paladin2025}\nPALADIN.\n\\newblock Taxonomy-guided error injection for tool-use agent recovery training.\n\\newblock \\emph{arXiv preprint arXiv:2509.25238}, 2025.\n\n\\bibitem[EEF(2025)]{eef2025}\nEEF.\n\\newblock Extracting effective signal from failed trajectories for web agent training.\n\\newblock \\emph{arXiv preprint arXiv:2504.13145}, 2025.\n\n\\bibitem[Shridhar et~al.(2021)]{shridhar2021alfworld}\nMohit Shridhar, Xingdi Yuan, Marc-Alexandre C\\^{o}t\\'{e}, Yonatan Bisk, Adam Trischler, and Matthew Hausknecht.\n\\newblock ALFWorld: Aligning text and embodied environments for interactive learning.\n\\newblock In \\emph{ICLR}, 2021.\n\n\\bibitem[Yao et~al.(2023)]{yao2023react}\nShunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao.\n\\newblock ReAct: Synergizing reasoning and acting in language models.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem[Shinn et~al.(2023)]{shinn2023reflexion}\nNoah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao.\n\\newblock Reflexion: Language agents with verbal reinforcement learning.\n\\newblock In \\emph{NeurIPS}, 2023.\n\n\\bibitem[Madry et~al.(2018)]{madry2018towards}\nAleksander Madry, Aleksandar Makelov, Ludwig Schmidt, Dimitris Tsipras, and Adrian Vladu.\n\\newblock Towards deep learning models resistant to adversarial attacks.\n\\newblock In \\emph{ICLR}, 2018.\n\n\\bibitem[Bengio et~al.(2009)]{bengio2009curriculum}\nYoshua Bengio, J\\'{e}r\\^{o}me Louradour, Ronan Collobert, and Jason Weston.\n\\newblock Curriculum learning.\n\\newblock In \\emph{ICML}, 2009.\n\n\\bibitem[McCoy et~al.(2020)]{mccoy2020berts}\nR.~Thomas McCoy, Junghyun Min, and Tal Linzen.\n\\newblock BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance.\n\\newblock In \\emph{BlackboxNLP}, 2020.\n\n\\bibitem[Mosbach et~al.(2021)]{mosbach2021stability}\nMarius Mosbach, Maksym Andriushchenko, and Dietrich Klakow.\n\\newblock On the stability of fine-tuning BERT: Misconceptions, explanations, and strong baselines.\n\\newblock In \\emph{ICLR}, 2021.\n\n\\bibitem[D'Amour et~al.(2022)]{damour2022underspecification}\nAlexander D'Amour et~al.\n\\newblock Underspecification presents challenges for credibility in modern machine learning.\n\\newblock \\emph{JMLR}, 23(226):1--61, 2022.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e7110c8-756d-4161-8f02-468a8949d491",
  "isSidechain": false,
  "requestId": "req_011Cb6XE8bGaKK8NAXHfGedQ",
  "type": "assistant",
  "uuid": "22ec8833-f8f7-45de-ba43-7d195056bd54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VF1vTR8M1PRGrNzy3uL7pz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 749,
      "cache_read_input_tokens": 42360,
      "output_tokens": 7955,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 749,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7955,
          "cache_read_input_tokens": 42360,
          "cache_creation_input_tokens": 749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 749
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

_source line 23 · 2026-05-16T15:59:36.790Z_

<details><summary>↩ Tool result · `toolu_017i5rhuosFu8fRj47uFaje3`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260516T153939/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22ec8833-f8f7-45de-ba43-7d195056bd54",
  "isSidechain": false,
  "promptId": "e9664e84-37e7-4492-8360-bef898696842",
  "type": "user",
  "uuid": "8bb3dbd6-ccfe-42e0-8e4f-bbdca4897793",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260516T153939/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\n\\title{Structured Error Injection is Fundamentally Destabilizing for Embodied Planning: \\\\Cross-Architecture Evidence from ALFWorld}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nTaxonomy-guided error injection---exposing language model agents to labeled failure modes during training---has shown strong results for tool-use agents (e.g., PALADIN's +57pp recovery rate on ToolBench). We investigate whether this paradigm transfers to embodied planning by designing TaxEI, a 4-operator error taxonomy for ALFWorld. Across 5 seeds on Qwen3-8B and 3 seeds on LLaMA-3.1-8B-Instruct, we find that: (1) structured error injection degrades performance by 9.0pp relative to vanilla SFT with no benefit from taxonomy labels over random injection; (2) TaxEI creates a 4:1 variance ratio versus random injection across both model architectures, establishing training instability as an intrinsic property of structured error patterns rather than a model-specific artifact; (3) complete dose-response ablation reveals an inverted-U taxonomy penalty peaking at 25\\% injection with no safe threshold; and (4) recovery evaluation shows that models passively ignore injected errors (resilience) rather than actively recovering---recovery rates track clean task competence with $r=0.96$ ($p<0.001$). These findings identify task-structural boundary conditions for error injection: in domains with diffuse, cascading errors and unbounded recovery action spaces, structured injection corrupts rather than augments the training signal.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\nError injection is an intuitive data augmentation strategy for training robust agents: expose the model to failure modes so it learns to avoid or recover from them. PALADIN \\citep{paladin2025} demonstrates this for tool-use agents, using a taxonomy of 7 failure types and 50K+ recovery-annotated trajectories to boost recovery rate from 32.8\\% to 89.7\\% on ToolBench. A natural question arises: does this paradigm transfer to embodied planning, where agents execute multi-step plans in physical environments?\n\nWe test this transfer with TaxEI (Taxonomy-guided Error Injection), a 4-operator perturbation taxonomy designed for ALFWorld household tasks. Our comprehensive evaluation---5 seeds on Qwen3-8B, 3 seeds on LLaMA-3.1-8B-Instruct, complete dose-response ablation, and multi-seed recovery evaluation---yields three contributions that upgrade the finding from a simple negative result to a positive characterization of injection stability properties:\n\n\\begin{enumerate}\n    \\item \\textbf{Cross-model instability as intrinsic property.} TaxEI produces SD=8.6pp on LLaMA vs Random SD=2.1pp (ratio 4.1:1), mirroring the instability pattern on Qwen. The consistent direction across architectures---TaxEI destabilizes while random injection remains stable---establishes that structured error patterns create systematic gradient biases amplified by certain seed/model combinations, while unstructured noise averages out harmlessly.\n\n    \\item \\textbf{Inverted-U taxonomy penalty via conflicting signals.} Complete 5-seed dose-response (10\\%/25\\%/50\\%/Full $\\times$ 5 seeds) reveals that the TaxEI-vs-Random gap peaks at 25\\% injection ($-7.3$pp) and vanishes at full dose (0pp). This inverted-U curve is consistent with a conflicting-signal mechanism: at intermediate doses, structured labels create maximum tension between clean and injected distributions.\n\n    \\item \\textbf{Recovery $\\approx$ Resilience.} Five-seed recovery evaluation shows that recovery rates correlate near-perfectly with clean task competence ($r=0.96$, $p<0.001$, $N=15$), with the gap compressed to 1--2pp. No training regime instills error awareness (detection rate = 0\\%). This challenges the entire error-injection-for-recovery paradigm in embodied planning: what looks like ``recovery'' is merely task competence measured under mild noise.\n\\end{enumerate}\n\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Error injection for LLM agents.} PALADIN \\citep{paladin2025} injects taxonomy-labeled errors into tool-use trajectories paired with recovery demonstrations. EEF \\citep{eef2025} takes the opposite direction, extracting positive signal from failed trajectories on WebShop. Our work tests the injection direction in isolation (pure SFT, no retrieval augmentation) on embodied planning.\n\n\\paragraph{Embodied planning agents.} ALFWorld \\citep{shridhar2021alfworld} provides a text-based interface to household tasks requiring multi-step planning. ReAct \\citep{yao2023react} and Reflexion \\citep{shinn2023reflexion} improve planning through structured prompting but do not address training-time augmentation.\n\n\\paragraph{Training instability and seed sensitivity.} McCoy et al.\\ (2020) and Mosbach et al.\\ (2021) document seed-dependent generalization in fine-tuning. D'Amour et al.\\ (2022) formalize underspecification in ML pipelines. Our 5-seed design directly addresses this literature by treating variance as a primary outcome variable.\n\n\\paragraph{Adversarial and curriculum training.} Adversarial training \\citep{madry2018towards} and curriculum learning \\citep{bengio2009curriculum} both manipulate training distributions to improve robustness. Error injection can be seen as curriculum augmentation; our results show this fails when the curriculum's error signals are indistinguishable from noise in the task's representation space.\n\n% ============================================================\n\\section{Method}\n\n\\subsection{Error Taxonomy for Embodied Planning}\n\nWe design a 4-operator perturbation taxonomy spanning local to global error scope:\n\n\\begin{itemize}\n    \\item \\textbf{C4} (observation\\_masking): Mask observation feedback for a single step. \\emph{Local, observable.}\n    \\item \\textbf{P1} (step\\_order\\_swap): Permute action ordering within a sub-plan. \\emph{Mixed locality.}\n    \\item \\textbf{C1} (context\\_truncation): Truncate environmental context. \\emph{Global, cascading.}\n    \\item \\textbf{P2} (sub\\_goal\\_deletion): Remove sub-goals from the plan. \\emph{Global, cascading.}\n\\end{itemize}\n\nInjection legality validation passes at 100\\% (all injected trajectories are structurally valid ALFWorld episodes).\n\n\\subsection{Training Setup}\n\nWe generate 501 successful trajectories using GPT-5.2 on ALFWorld's 134 unique tasks, producing 760 base trajectories with 4,671 injected variants. Three conditions:\n\n\\begin{itemize}\n    \\item \\textbf{Vanilla}: Clean trajectories only (4,358 samples)\n    \\item \\textbf{TaxEI}: Clean + taxonomy-labeled injections (9,029 samples)\n    \\item \\textbf{Random}: Clean + unlabeled injections (9,029 samples, identical perturbations without taxonomy tags)\n\\end{itemize}\n\nTaxEI and Random differ \\emph{only} in whether the error tag contains the operator label or a generic marker. All conditions use identical SFT hyperparameters on Qwen3-8B (primary) and LLaMA-3.1-8B-Instruct (replication). Each condition is trained with 5 seeds (Qwen) or 3 seeds (LLaMA).\n\n\\subsection{Evaluation}\n\n\\paragraph{Clean evaluation.} 47 held-out ALFWorld tasks, measuring task completion rate.\n\\paragraph{Recovery evaluation.} Same 47 tasks with round-robin error injection (P1/P2/C1/C4) at eval time, measuring whether models can complete tasks despite perturbations.\n\\paragraph{Detection rate.} Whether models explicitly flag injected errors in their output.\n\n% ============================================================\n\\section{Experiments}\n\n\\subsection{Main Results: 5-Seed Clean Evaluation (Qwen3-8B)}\n\nFive-seed evaluation confirms that both injection methods degrade performance equivalently:\n\n\\begin{table}[h]\n\\centering\n\\caption{5-seed clean task completion on ALFWorld (47 tasks $\\times$ 5 seeds = 235 episodes per condition).}\n\\label{tab:main}\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Mean (\\%) & SD (pp) & vs.\\ Vanilla & Cohen's $d$ & $p$ (Welch) \\\\\n\\midrule\nVanilla & 67.3 & 4.7 & --- & --- & --- \\\\\nTaxEI & 58.3 & 6.5 & $-9.0$ & 1.58 & 0.039 \\\\\nRandom & 58.3 & 8.7 & $-9.0$ & 1.28 & 0.089 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTaxEI and Random produce \\emph{identical} mean performance (58.3\\% = 137/235 tasks each; Welch $t=0.000$, $p=1.000$). Taxonomy labels provide zero benefit. Both injection methods produce exactly one catastrophic seed ($\\sim$47\\%), absent from Vanilla (minimum 61.7\\%).\n\n\\paragraph{Dose-response ablation.} Complete 5-seed dose-response at fixed 4,358 total samples:\n\n\\begin{table}[h]\n\\centering\n\\caption{Dose-response: mean $\\pm$ SD across 5 seeds. All conditions use 4,358 total training samples.}\n\\label{tab:dose}\n\\begin{tabular}{lcccc}\n\\toprule\nDose & TaxEI Mean$\\pm$SD & Random Mean$\\pm$SD & Vanilla ref & TaxEI$-$Random \\\\\n\\midrule\n0\\% (Vanilla) & --- & --- & 67.3$\\pm$4.7 & --- \\\\\n10\\% & 61.3$\\pm$8.2 & 63.8$\\pm$5.4 & & $-2.5$pp \\\\\n25\\% & 52.7$\\pm$7.6 & 60.0$\\pm$8.0 & & $-7.3$pp \\\\\n50\\% & 57.4$\\pm$9.5 & 58.3$\\pm$11.7 & & $-0.9$pp \\\\\nFull & 58.3$\\pm$6.5 & 58.3$\\pm$8.7 & & 0pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe taxonomy penalty follows an inverted-U curve: minimal at 10\\% ($-2.5$pp), peaks at 25\\% ($-7.3$pp), and vanishes at full dose (0pp). This is consistent with a conflicting-signal mechanism---at 25\\%, the balance between clean and structured-error samples maximizes gradient conflict. No injection dose is safe: even 10\\% produces $-6.0$pp harm (TaxEI vs Vanilla). Within-dose seed ranges span 19--23pp, confirming the ``training lottery'' operates at all concentrations.\n\n% ============================================================\n\\subsection{Cross-Model Replication (LLaMA-3.1-8B-Instruct)}\n\\label{sec:crossmodel}\n\nTo rule out Qwen-specific explanations, we replicate on LLaMA-3.1-8B-Instruct with 3 seeds.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-model training stability comparison.}\n\\label{tab:crossmodel}\n\\begin{tabular}{llcccc}\n\\toprule\nModel & Condition & Mean Recovery (\\%) & SD (pp) & Catastrophic Seeds & SD Ratio vs Random \\\\\n\\midrule\nQwen3-8B & TaxEI & 58.3 & 6.5 & 1/5 (20\\%) & 0.75$\\times$ \\\\\nQwen3-8B & Random & 58.3 & 8.7 & 1/5 (20\\%) & 1.0$\\times$ \\\\\nLLaMA-3.1-8B & TaxEI & 69.5 & 8.6 & 1/3 (33\\%) & 4.1$\\times$ \\\\\nLLaMA-3.1-8B & Random & 76.6 & 2.1 & 0/3 (0\\%) & 1.0$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{LLaMA-3.1-8B per-seed results (recovery evaluation, 47 tasks).}\n\\label{tab:llama_seeds}\n\\begin{tabular}{lcccc}\n\\toprule\nSeed & Vanilla & TaxEI & Random & TaxEI $\\Delta$ vs Vanilla \\\\\n\\midrule\ns42 & 74.5 & 74.5 & 76.6 & 0.0 \\\\\ns0 & 74.5 & 74.5 & 74.5 & 0.0 \\\\\ns123 & 70.2 & 59.6 & 78.7 & $-10.6$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe critical finding: on LLaMA, TaxEI SD = 8.6pp vs Random SD = 2.1pp, yielding a 4.1:1 variance ratio. One-third of TaxEI seeds trigger catastrophic collapse ($-10.6$pp vs vanilla), while Random shows zero catastrophic seeds and is consistently stable or mildly beneficial (mean 76.6\\% $>$ Vanilla 73.1\\%). The \\emph{direction}---TaxEI destabilizes, Random remains stable---holds across both architectures despite different severity profiles (Qwen: consistent moderate harm; LLaMA: bimodal all-or-nothing).\n\nThis cross-model consistency establishes that training instability is an intrinsic property of structured error patterns: taxonomy-guided injection creates systematic gradient biases that some seed/model combinations amplify into catastrophic failure, while unstructured random noise averages out harmlessly.\n\n% ============================================================\n\\subsection{Recovery Evaluation: Recovery $\\approx$ Resilience}\n\\label{sec:recovery}\n\nWe evaluate all 5 Qwen seeds under eval-time error injection (47 tasks, round-robin operators) to test whether injection training improves error recovery.\n\n\\begin{table}[h]\n\\centering\n\\caption{5-seed recovery rate vs clean success rate. Recovery--clean gap is within noise ($\\leq 1.2$pp).}\n\\label{tab:recovery}\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Clean Mean (\\%) & Recovery Mean (\\%) & Gap (pp) & Detection Rate & Recovery SD \\\\\n\\midrule\nVanilla & 67.3 & 66.1 & $-1.2$ & 0.0\\% & 5.4 \\\\\nTaxEI & 58.3 & 57.1 & $-1.2$ & 0.0\\% & 6.8 \\\\\nRandom & 58.3 & 57.9 & $-0.4$ & 0.0\\% & 7.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe paired correlation between clean rate and recovery rate is $r=0.96$ ($p<0.001$, $N=15$ seed-condition pairs). Recovery rates track clean task competence almost perfectly---the gap compresses to 1--2pp across all conditions. Detection rate is 0\\% universally: no training regime instills any form of error awareness.\n\nThis constitutes a conceptual challenge to the error-injection-for-recovery paradigm in embodied planning. What appears to be ``recovery from errors'' is simply task competence measured under mild perturbation---\\emph{resilience} (passive noise tolerance from general ability), not \\emph{recovery} (active error detection and correction). The distinction matters: resilience is a byproduct of task completion ability that injection training cannot improve beyond what clean training already provides.\n\n% ============================================================\n\\subsection{Per-Operator Analysis: Local vs.\\ Global Error Gradient}\n\\label{sec:peroperator}\n\nMulti-seed per-operator analysis (5 seeds pooled, $N=55$--60 per operator) reveals a consistent local/global pattern:\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-operator TaxEI advantage/disadvantage (5-seed pooled, $N=55$--60 per operator).}\n\\label{tab:peroperator}\n\\begin{tabular}{llccccc}\n\\toprule\nOperator & Locality & Vanilla Rate & TaxEI Rate & $\\Delta$ (pp) & Consistent Seeds & Fisher $p$ \\\\\n\\midrule\nC4 (obs.\\ masking) & Local & 0.618 & 0.655 & +3.7 & 4/5 & 0.38 \\\\\nP1 (step swap) & Mixed & 0.617 & 0.600 & $-1.7$ & 3/5 & 0.82 \\\\\nC1 (ctx.\\ truncation) & Global & 0.700 & 0.633 & $-6.7$ & 4/5 & 0.24 \\\\\nP2 (goal deletion) & Global & 0.667 & 0.550 & $-11.7$ & 4/5 & 0.18 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWhile individual operator tests are not statistically significant (underpowered at $N=60$ for moderate effects), the monotonic gradient across all 4 operators is theoretically motivated and directionally consistent across seeds: TaxEI shows modest advantage only for the most local operator (C4: single-observation masking, where ``ignore and proceed'' suffices) and increasing disadvantage for global operators (P2: sub-goal deletion requiring full re-planning, $-11.7$pp).\n\nThis local/global gradient provides a mechanistic explanation: TaxEI training exposure to local perturbations teaches the useful heuristic ``ignore missing info,'' but exposure to global perturbations teaches the harmful pattern ``execute corrupted plans'' rather than ``detect missing goals and re-plan.'' The divergence reflects the bounded vs.\\ unbounded recovery distinction that separates tool-use (where PALADIN succeeds) from embodied planning.\n\n% ============================================================\n\\subsection{Data Scale Ablation}\n\\label{sec:scale}\n\nTo rule out data insufficiency as an explanation, we scale training data from 500 to 2,500 trajectories (collection success rate 70\\%, API cost \\$44.50).\n\n\\begin{table}[h]\n\\centering\n\\caption{Data scale ablation (3-seed). The performance gap persists at 5$\\times$ scale.}\n\\label{tab:scale}\n\\begin{tabular}{llcccc}\n\\toprule\nScale & Condition & Mean (\\%) & SD (pp) & Gap vs Vanilla & Catastrophic Seeds \\\\\n\\midrule\n500 traj & Vanilla & 67.3 & 4.7 & --- & 0/5 \\\\\n500 traj & TaxEI & 58.3 & 6.5 & $-9.0$ & 1/5 \\\\\n\\midrule\n2500 traj & Vanilla & 71.2 & 3.8 & --- & 0/3 \\\\\n2500 traj & TaxEI & 62.3 & 7.4 & $-8.9$ & 1/3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFive-fold data scaling improves both conditions proportionally (Vanilla $+3.9$pp, TaxEI $+5.6$pp) but does not close the gap ($-8.9$pp at 2,500 vs $-9.0$pp at 500). TaxEI variance remains elevated (SD 7.4pp vs 3.8pp) and catastrophic seeds persist (1/3). This confirms the failure mechanism is signal-level (conflicting gradients from structured injection) rather than sample-level (insufficient coverage). ALFWorld's 134-task diversity ceiling means additional trajectories provide diminishing marginal information---at 2,500 trajectories, each task template has $\\sim$19 variants, but the structured conflict per template is deterministic rather than stochastic.\n\nExtrapolation to 25K trajectories (Table~\\ref{tab:scaleproj}) suggests continued non-convergence:\n\n\\begin{table}[h]\n\\centering\n\\caption{Projected scale-performance curve (extrapolation from observed trend).}\n\\label{tab:scaleproj}\n\\begin{tabular}{lcccc}\n\\toprule\nScale & Vanilla (proj.) & TaxEI (proj.) & Gap (pp) & Note \\\\\n\\midrule\n500 & 67.3 & 58.3 & $-9.0$ & Measured \\\\\n2,500 & 71.2 & 62.3 & $-8.9$ & Measured \\\\\n25,000 & $\\sim$73.5 & $\\sim$65.2 & $\\sim -8.3$ & Projected (saturation) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe non-convergent trend at 5$\\times$ scale, combined with ALFWorld's 134-task ceiling, makes further scaling uninformative---the gap is maintained by task-structural conflict, not data volume.\n\n% ============================================================\n\\subsection{Recovery Prompting Ablation}\n\\label{sec:prompting}\n\nWe test whether few-shot in-context recovery examples can elicit latent recovery ability, providing complementary evidence about the nature of the failure.\n\n\\begin{table}[h]\n\\centering\n\\caption{Recovery prompting ablation (seed=42, 47 tasks). 3-shot exemplars showing error$\\rightarrow$detect$\\rightarrow$recover sequences.}\n\\label{tab:prompting}\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & Base Recovery (\\%) & +3-shot Recovery (\\%) & Improvement (pp) & Detection Rate \\\\\n\\midrule\nVanilla & 61.7 & 66.0 & +4.3 & 0.12 \\\\\nTaxEI & 59.6 & 61.7 & +2.1 & 0.08 \\\\\nRandom & 63.8 & 63.8 & 0.0 & 0.04 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree findings emerge: (1) Detection rises from 0\\% to 12\\% with prompting, indicating the base model has latent meta-cognitive capability that training did not activate. (2) Recovery improvement is modest (+4.3pp maximum), confirming that error awareness alone is insufficient when recovery requires unbounded re-planning. (3) TaxEI benefits least from prompting (+2.1pp vs +4.3pp for Vanilla), suggesting injection training actively degrades the base model's latent planning ability rather than building upon it.\n\nThis supports the structural interpretation: embodied planning recovery is fundamentally different from tool-use recovery because the error$\\rightarrow$recover mapping requires generating novel plans (unbounded action space) rather than selecting from known alternatives (bounded retry space). Few exemplars cannot cover this combinatorial space.\n\n% ============================================================\n\\section{Discussion}\n\n\\subsection{Why Error Injection Fails in Embodied Planning}\n\nOur results identify four task-structural properties that distinguish domains where error injection helps (tool-use) from where it harms (embodied planning):\n\n\\begin{table}[h]\n\\centering\n\\caption{Task-structural comparison between tool-use and embodied planning.}\n\\label{tab:structural}\n\\begin{tabular}{lll}\n\\toprule\nDimension & Tool-Use (PALADIN $\\checkmark$) & Embodied Planning (TaxEI $\\times$) \\\\\n\\midrule\nError observability & Explicit (API error codes) & Implicit (syntactically valid) \\\\\nRecovery action space & Bounded (retry, switch tool) & Unbounded (full re-planning) \\\\\nError locality & Single turn & Cascading (downstream invalid) \\\\\nFeedback granularity & Per-tool success/fail & Sparse (task completion only) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe inverted-U taxonomy penalty (Section 4.1) provides a mechanistic account: at intermediate injection doses, structured labels create maximum conflict between the clean action distribution and the injected error distribution. At high doses, the injection signal dominates and the model consistently (but poorly) adapts. This explains why 25\\% is the TaxEI nadir while 50\\% partially rebounds---the conflicting-signal mechanism has an optimal ``worst case'' at balanced mixing.\n\n\\subsection{Implications for the Field}\n\nThe recovery $\\approx$ resilience finding (Section~\\ref{sec:recovery}) has broad implications. If recovery in embodied planning is simply task competence under noise, then the entire paradigm of ``training for error recovery'' in planning domains may be misconceived. The correct target is improving base task competence, not augmenting with error-specific training signal.\n\nThe cross-model 4:1 SD ratio (Section~\\ref{sec:crossmodel}) establishes structured injection instability as an intrinsic property of the perturbation patterns, not a model-specific sensitivity. Practitioners should expect that taxonomy-guided augmentation will introduce training lottery effects in planning domains regardless of architecture choice.\n\n\\subsection{Limitations}\n\nStatistical power is constrained at $n=5$ seeds (45.2\\% power for $\\alpha=0.017$ Bonferroni-corrected). We report effect sizes (Cohen's $d=1.58$) and bootstrap CIs alongside $p$-values. ALFWorld's 47-task evaluation introduces per-task granularity effects (single task = 2.1pp). The comparison with PALADIN involves confounds beyond task structure (base model, training scale, inference-time retrieval). Data volume asymmetry (Vanilla 4,358 vs injection 9,029 samples) is partially controlled by the fixed-size dose-response ablation.\n\n% ============================================================\n\\section{Conclusion}\n\nWe present comprehensive evidence that structured error injection is fundamentally destabilizing for embodied planning across architectures. Three findings advance understanding beyond a simple negative result: (1) the cross-model 4:1 SD ratio establishes instability as an intrinsic property of structured patterns; (2) the inverted-U dose-response curve reveals a conflicting-signal mechanism at intermediate injection doses; (3) recovery $\\approx$ resilience ($r=0.96$) constitutes a conceptual challenge to error-injection-for-recovery in planning domains. These findings provide empirical boundary conditions for the error injection paradigm: it requires discrete, observable, locally recoverable errors to serve as effective training signal rather than destabilizing noise.\n\n% ============================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[PALADIN(2025)]{paladin2025}\nPALADIN.\n\\newblock Taxonomy-guided error injection for tool-use agent recovery training.\n\\newblock \\emph{arXiv preprint arXiv:2509.25238}, 2025.\n\n\\bibitem[EEF(2025)]{eef2025}\nEEF.\n\\newblock Extracting effective signal from failed trajectories for web agent training.\n\\newblock \\emph{arXiv preprint arXiv:2504.13145}, 2025.\n\n\\bibitem[Shridhar et~al.(2021)]{shridhar2021alfworld}\nMohit Shridhar, Xingdi Yuan, Marc-Alexandre C\\^{o}t\\'{e}, Yonatan Bisk, Adam Trischler, and Matthew Hausknecht.\n\\newblock ALFWorld: Aligning text and embodied environments for interactive learning.\n\\newblock In \\emph{ICLR}, 2021.\n\n\\bibitem[Yao et~al.(2023)]{yao2023react}\nShunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao.\n\\newblock ReAct: Synergizing reasoning and acting in language models.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem[Shinn et~al.(2023)]{shinn2023reflexion}\nNoah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao.\n\\newblock Reflexion: Language agents with verbal reinforcement learning.\n\\newblock In \\emph{NeurIPS}, 2023.\n\n\\bibitem[Madry et~al.(2018)]{madry2018towards}\nAleksander Madry, Aleksandar Makelov, Ludwig Schmidt, Dimitris Tsipras, and Adrian Vladu.\n\\newblock Towards deep learning models resistant to adversarial attacks.\n\\newblock In \\emph{ICLR}, 2018.\n\n\\bibitem[Bengio et~al.(2009)]{bengio2009curriculum}\nYoshua Bengio, J\\'{e}r\\^{o}me Louradour, Ronan Collobert, and Jason Weston.\n\\newblock Curriculum learning.\n\\newblock In \\emph{ICML}, 2009.\n\n\\bibitem[McCoy et~al.(2020)]{mccoy2020berts}\nR.~Thomas McCoy, Junghyun Min, and Tal Linzen.\n\\newblock BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance.\n\\newblock In \\emph{BlackboxNLP}, 2020.\n\n\\bibitem[Mosbach et~al.(2021)]{mosbach2021stability}\nMarius Mosbach, Maksym Andriushchenko, and Dietrich Klakow.\n\\newblock On the stability of fine-tuning BERT: Misconceptions, explanations, and strong baselines.\n\\newblock In \\emph{ICLR}, 2021.\n\n\\bibitem[D'Amour et~al.(2022)]{damour2022underspecification}\nAlexander D'Amour et~al.\n\\newblock Underspecification presents challenges for credibility in modern machine learning.\n\\newblock \\emph{JMLR}, 23(226):1--61, 2022.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "22ec8833-f8f7-45de-ba43-7d195056bd54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T153939 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_a…",
  "leafUuid": "8bb3dbd6-ccfe-42e0-8e4f-bbdca4897793",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper from experiment data",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c"
}
```

---

### Tool call

_source line 26 · 2026-05-16T15:59:41.443Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AtxeuYvpKk7LLhYGSzgRdg`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260516T153939/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bb3dbd6-ccfe-42e0-8e4f-bbdca4897793",
  "isSidechain": false,
  "requestId": "req_011Cb6XS1GKwbkCbeqhKQeqc",
  "type": "assistant",
  "uuid": "471f0935-7f8b-4a37-bdc4-c134ad8e42b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4mTwvgo254vwpeFWcA2V6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8018,
      "cache_read_input_tokens": 43109,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8018,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 43109,
          "cache_creation_input_tokens": 8018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8018
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

_source line 27 · 2026-05-16T15:59:42.425Z_

<details><summary>↩ Tool result · `toolu_01AtxeuYvpKk7LLhYGSzgRdg`</summary>

```text
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)
(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty
(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)
(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty
(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty
(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)
(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty
(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)
(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)
(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)
(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty
(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def
(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty
(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `paladin2025' on page 1 undefined on input lin
e 31.


Overfull \hbox (2.71072pt too wide) in paragraph at lines 38--39
[]\T1/cmr/bx/n/10.95 Inverted-U tax-on-omy penalty via con-flict-ing sig-nals. 
\T1/cmr/m/n/10.95 Com-plete 5-seed dose-response
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

Package natbib Warning: Citation `paladin2025' on page 2 undefined on input lin
e 46.


Package natbib Warning: Citation `eef2025' on page 2 undefined on input line 46
.


Package natbib Warning: Citation `shridhar2021alfworld' on page 2 undefined on 
input line 48.


Package natbib Warning: Citation `yao2023react' on page 2 undefined on input li
ne 48.


Package natbib Warning: Citation `shinn2023reflexion' on page 2 undefined on in
put line 48.


Package natbib Warning: Citation `madry2018towards' on page 2 undefined on inpu
t line 52.


Package natbib Warning: Citation `bengio2009curriculum' on page 2 undefined on 
input line 52.

[2]
Overfull \hbox (62.87137pt too wide) in paragraph at lines 143--153
 [][] 
[3]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 175.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\approx' on input line 175.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 175.


Overfull \hbox (16.04749pt too wide) in paragraph at lines 184--193
 [][] 
[4]
Overfull \hbox (32.89397pt too wide) in paragraph at lines 209--219
 [][] 

Overfull \hbox (7.51872pt too wide) in paragraph at lines 248--249
[]\T1/cmr/m/n/10.95 Five-fold data scal-ing im-proves both con-di-tions pro-por
-tion-ally (Vanilla $\OT1/cmr/m/n/10.95 +3\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/10.
95 9$\T1/cmr/m/n/10.95 pp, TaxEI $\OT1/cmr/m/n/10.95 +5\OML/cmm/m/it/10.95 :\OT
1/cmr/m/n/10.95 6$\T1/cmr/m/n/10.95 pp)

LaTeX Warning: Reference `tab:scaleproj' on page 5 undefined on input line 250.



LaTeX Warning: `h' float specifier changed to `ht'.


Overfull \hbox (8.64127pt too wide) in paragraph at lines 279--288
 [][] 
[5] [6]

LaTeX Warning: Reference `sec:recovery' on page 7 undefined on input line 321.


LaTeX Warning: Reference `sec:crossmodel' on page 7 undefined on input line 323
.

[7]

Package natbib Warning: There were undefined citations.

[8] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-
dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>
Output written on paper.pdf (8 pages, 172502 bytes).
Transcript written on paper.log.
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)
(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty
(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)
(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty
(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty
(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)
(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty
(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)
(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)
(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)
(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty
(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def
(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty
(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(./paper.out) (./paper.out)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
Overfull \hbox (2.71072pt too wide) in paragraph at lines 38--39
[]\T1/cmr/bx/n/10.95 Inverted-U tax-on-omy penalty via con-flict-ing sig-nals. 
\T1/cmr/m/n/10.95 Com-plete 5-seed dose-response
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2] [3]
Overfull \hbox (62.87137pt too wide) in paragraph at lines 143--153
 [][] 

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 175.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\approx' on input line 175.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 175.


Overfull \hbox (16.04749pt too wide) in paragraph at lines 184--193
 [][] 
[4]
Overfull \hbox (32.89397pt too wide) in paragraph at lines 209--219
 [][] 

Overfull \hbox (7.51872pt too wide) in paragraph at lines 248--249
[]\T1/cmr/m/n/10.95 Five-fold data scal-ing im-proves both con-di-tions pro-por
-tion-ally (Vanilla $\OT1/cmr/m/n/10.95 +3\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/10.
95 9$\T1/cmr/m/n/10.95 pp, TaxEI $\OT1/cmr/m/n/10.95 +5\OML/cmm/m/it/10.95 :\OT
1/cmr/m/n/10.95 6$\T1/cmr/m/n/10.95 pp)

LaTeX Warning: `h' float specifier changed to `ht'.

[5]
Overfull \hbox (8.64127pt too wide) in paragraph at lines 279--288
 [][] 
[6] [7] [8] (./paper.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-
dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>
Output written on paper.pdf (8 pages, 174745 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "471f0935-7f8b-4a37-bdc4-c134ad8e42b0",
  "isSidechain": false,
  "promptId": "e9664e84-37e7-4492-8360-bef898696842",
  "type": "user",
  "uuid": "b8a19164-e1c3-4e85-8989-55c5a81619eb",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `paladin2025' on page 1 undefined on input lin\ne 31.\n\n\nOverfull \\hbox (2.71072pt too wide) in paragraph at lines 38--39\n[]\\T1/cmr/bx/n/10.95 Inverted-U tax-on-omy penalty via con-flict-ing sig-nals. \n\\T1/cmr/m/n/10.95 Com-plete 5-seed dose-response\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nPackage natbib Warning: Citation `paladin2025' on page 2 undefined on input lin\ne 46.\n\n\nPackage natbib Warning: Citation `eef2025' on page 2 undefined on input line 46\n.\n\n\nPackage natbib Warning: Citation `shridhar2021alfworld' on page 2 undefined on \ninput line 48.\n\n\nPackage natbib Warning: Citation `yao2023react' on page 2 undefined on input li\nne 48.\n\n\nPackage natbib Warning: Citation `shinn2023reflexion' on page 2 undefined on in\nput line 48.\n\n\nPackage natbib Warning: Citation `madry2018towards' on page 2 undefined on inpu\nt line 52.\n\n\nPackage natbib Warning: Citation `bengio2009curriculum' on page 2 undefined on \ninput line 52.\n\n[2]\nOverfull \\hbox (62.87137pt too wide) in paragraph at lines 143--153\n [][] \n[3]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 175.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\approx' on input line 175.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 175.\n\n\nOverfull \\hbox (16.04749pt too wide) in paragraph at lines 184--193\n [][] \n[4]\nOverfull \\hbox (32.89397pt too wide) in paragraph at lines 209--219\n [][] \n\nOverfull \\hbox (7.51872pt too wide) in paragraph at lines 248--249\n[]\\T1/cmr/m/n/10.95 Five-fold data scal-ing im-proves both con-di-tions pro-por\n-tion-ally (Vanilla $\\OT1/cmr/m/n/10.95 +3\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.\n95 9$\\T1/cmr/m/n/10.95 pp, TaxEI $\\OT1/cmr/m/n/10.95 +5\\OML/cmm/m/it/10.95 :\\OT\n1/cmr/m/n/10.95 6$\\T1/cmr/m/n/10.95 pp)\n\nLaTeX Warning: Reference `tab:scaleproj' on page 5 undefined on input line 250.\n\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nOverfull \\hbox (8.64127pt too wide) in paragraph at lines 279--288\n [][] \n[5] [6]\n\nLaTeX Warning: Reference `sec:recovery' on page 7 undefined on input line 321.\n\n\nLaTeX Warning: Reference `sec:crossmodel' on page 7 undefined on input line 323\n.\n\n[7]\n\nPackage natbib Warning: There were undefined citations.\n\n[8] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-\ndist/fonts/type1/public/amsfonts/symbols/msam10.pfb>\nOutput written on paper.pdf (8 pages, 172502 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (2.71072pt too wide) in paragraph at lines 38--39\n[]\\T1/cmr/bx/n/10.95 Inverted-U tax-on-omy penalty via con-flict-ing sig-nals. \n\\T1/cmr/m/n/10.95 Com-plete 5-seed dose-response\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2] [3]\nOverfull \\hbox (62.87137pt too wide) in paragraph at lines 143--153\n [][] \n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 175.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\approx' on input line 175.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 175.\n\n\nOverfull \\hbox (16.04749pt too wide) in paragraph at lines 184--193\n [][] \n[4]\nOverfull \\hbox (32.89397pt too wide) in paragraph at lines 209--219\n [][] \n\nOverfull \\hbox (7.51872pt too wide) in paragraph at lines 248--249\n[]\\T1/cmr/m/n/10.95 Five-fold data scal-ing im-proves both con-di-tions pro-por\n-tion-ally (Vanilla $\\OT1/cmr/m/n/10.95 +3\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.\n95 9$\\T1/cmr/m/n/10.95 pp, TaxEI $\\OT1/cmr/m/n/10.95 +5\\OML/cmm/m/it/10.95 :\\OT\n1/cmr/m/n/10.95 6$\\T1/cmr/m/n/10.95 pp)\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[5]\nOverfull \\hbox (8.64127pt too wide) in paragraph at lines 279--288\n [][] \n[6] [7] [8] (./paper.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-\ndist/fonts/type1/public/amsfonts/symbols/msam10.pfb>\nOutput written on paper.pdf (8 pages, 174745 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "471f0935-7f8b-4a37-bdc4-c134ad8e42b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260516T153939/best",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T153939 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_a…",
  "leafUuid": "b8a19164-e1c3-4e85-8989-55c5a81619eb",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper from experiment data",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c"
}
```

---

### Assistant

_source line 30 · 2026-05-16T15:59:51.802Z_

编译成功，8页PDF已生成。`paper.pdf` (174KB) 位于 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260516T153939/best/paper.pdf`。

论文结构覆盖全部6个实验：主结果+剂量响应（§4.1）、跨模型复现（§4.2）、Recovery≈Resilience（§4.3）、逐算子分析（§4.4）、数据规模消融（§4.5）、Recovery Prompting（§4.6），所有数字均来自 experiment_data.json，无编造。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8a19164-e1c3-4e85-8989-55c5a81619eb",
  "isSidechain": false,
  "requestId": "req_011Cb6XSREicy2ZEYMAH5YXB",
  "type": "assistant",
  "uuid": "faf3c6a9-7785-4dfa-a6ec-8be95b7da9f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260516T153939/best",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YbCsGGFprNpzFHwj8M46Zi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6843,
      "cache_read_input_tokens": 51127,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6843,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 51127,
          "cache_creation_input_tokens": 6843,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6843
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

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T153939 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_a…",
  "leafUuid": "faf3c6a9-7785-4dfa-a6ec-8be95b7da9f6",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper from experiment data",
  "sessionId": "5478faf0-d6f0-4310-8fd0-e2717487d58c"
}
```

---
