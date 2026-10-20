# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122435 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/a50d708f-f43f-4031-a2e1-4dae3a3259fc.jsonl`
- **Structured JSON:** [`5c5bfec52337339012be.json`](../../sessions/5c/5c5bfec52337339012be.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T12:49:47.324Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T12:49:47.324Z",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122435 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：原始framing完全成立。Title保持\"Differential Nocuity\"，5个claim按当前strength发表。 C1=confirmed(+34pp, causal), C2=confirmed(3-tier), C3=suggestive(disclosed fragility), C4=star finding(model×type interaction), C5=validated(human anchor升级)。 Judge calibration作为methodological strength而非limitation呈现。 Contribution ordering: causal quantification > differential nocuity > failure mode taxonomy。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T12:49:47.327Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T12:49:47.327Z",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc"
}
```

---

## Round 1

41 recorded events

### User

_source line 3 · 2026-05-21T12:49:47.346Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122435 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：原始framing完全成立。Title保持"Differential Nocuity"，5个claim按当前strength发表。 C1=confirmed(+34pp, causal), C2=confirmed(3-tier), C3=suggestive(disclosed fragility), C4=star finding(model×type interaction), C5=validated(human anchor升级)。 Judge calibration作为methodological strength而非limitation呈现。 Contribution ordering: causal quantification > differential nocuity > failure mode taxonomy。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "eee4c209-3712-4b8a-9840-fcbadb07765b",
  "type": "user",
  "uuid": "a8ba54a5-d452-4372-98b5-02042415f383",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T12:49:47.345Z_

```json
{
  "parentUuid": "a8ba54a5-d452-4372-98b5-02042415f383",
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
  "uuid": "966bf5f2-3f09-4c26-959c-70671cb1f0a1",
  "timestamp": "2026-05-21T12:49:47.345Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T12:49:47.345Z_

```json
{
  "parentUuid": "966bf5f2-3f09-4c26-959c-70671cb1f0a1",
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
  "uuid": "1538e10e-8b6c-48ff-a807-221ea665d2b8",
  "timestamp": "2026-05-21T12:49:47.345Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-21T12:49:47.345Z_

```json
{
  "parentUuid": "1538e10e-8b6c-48ff-a807-221ea665d2b8",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "05a1f325-19d7-4d28-99f0-674bcccb50ca",
  "timestamp": "2026-05-21T12:49:47.345Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
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
  "aiTitle": "Generate EMNLP paper on policy ambiguity safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc"
}
```

---

### Assistant

_source line 8 · 2026-05-21T12:49:50.022Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05a1f325-19d7-4d28-99f0-674bcccb50ca",
  "isSidechain": false,
  "requestId": "req_011CbFk12AzgNMrDNE2ZBhCB",
  "type": "assistant",
  "uuid": "c66b1df0-a38f-459e-9024-a0f73511eeb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjfNS5qXK6bgVGzmktGBZz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12126,
      "cache_read_input_tokens": 11447,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12126
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

_source line 9 · 2026-05-21T12:49:50.916Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XYRmNSdzYrgNunTc3MLsas`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c66b1df0-a38f-459e-9024-a0f73511eeb9",
  "isSidechain": false,
  "requestId": "req_011CbFk12AzgNMrDNE2ZBhCB",
  "type": "assistant",
  "uuid": "00bb729c-cf70-473e-a03d-64bdb44e55ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjfNS5qXK6bgVGzmktGBZz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12126,
      "cache_read_input_tokens": 11447,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12126
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

_source line 10 · 2026-05-21T12:49:51.205Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CS9b5HGzkTQW53soatte9a`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00bb729c-cf70-473e-a03d-64bdb44e55ef",
  "isSidechain": false,
  "requestId": "req_011CbFk12AzgNMrDNE2ZBhCB",
  "type": "assistant",
  "uuid": "beb3e936-6b73-45c6-8a6f-80983a31ad7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjfNS5qXK6bgVGzmktGBZz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12126,
      "cache_read_input_tokens": 11447,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12126
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

_source line 11 · 2026-05-21T12:49:51.332Z_

<details><summary>↩ Tool result · `toolu_01XYRmNSdzYrgNunTc3MLsas`</summary>

```text
1	[
2	  {
3	    "name": "full_study_clause_generation",
4	    "description": "生成剩余clause pairs至300对(50/type×6 types)，含coreferential 50新、 authorization_scope 50新、lexical +20、incompleteness +20。 混合CP格式(labeled+unlabeled)。验证跨类型balance。\n",
5	    "results": {
6	      "total_clause_pairs": 300,
7	      "per_type_count": 50,
8	      "types_covered": 6,
9	      "cp_format_mix_ratio": "0.5 labeled / 0.5 unlabeled",
10	      "cross_type_token_delta_mean": 24.3,
11	      "cross_type_token_delta_std": 11.7,
12	      "flesch_kincaid_mean": 12.1,
13	      "quality_review_pass_rate": 0.96,
14	      "revision_rounds": 1
15	    },
16	    "tables": [
17	      {
18	        "name": "Clause pair statistics by type",
19	        "columns": [
20	          "type",
21	          "n_pairs",
22	          "mean_token_delta",
23	          "sd_token_delta",
24	          "flesch_kincaid",
25	          "layer"
26	        ],
27	        "rows": [
28	          [
29	            "authorization_scope",
30	            50,
31	            36.1,
32	            8.2,
33	            11.8,
34	            "specification"
35	          ],
36	          [
37	            "conditional_precedence",
38	            50,
39	            28.4,
40	            9.1,
41	            12.6,
42	            "specification"
43	          ],
44	          [
45	            "incompleteness",
46	            50,
47	            34.6,
48	            7.8,
49	            11.4,
50	            "specification"
51	          ],
52	          [
53	            "lexical",
54	            50,
55	            18.7,
56	            6.3,
57	            12.9,
58	            "linguistic"
59	          ],
60	          [
61	            "coreferential",
62	            50,
63	            7.8,
64	            3.1,
65	            12.4,
66	            "linguistic"
67	          ],
68	          [
69	            "scopal",
70	            50,
71	            21.2,
72	            7.0,
73	            11.7,
74	            "linguistic"
75	          ]
76	        ]
77	      }
78	    ],
79	    "figures": [],
80	    "analysis": "Clause generation是deterministic步骤，best档下无意外。关键输出是stimulus set的完整性和质量， 为plan_001b和plan_002/003的2,400+ episodes提供基础。Token delta分布将在plan_004的 logistic regression中作为control variable纳入。\n\n\nBest档下clause generation一次通过质量审核，仅需1轮minor revision。 token delta在spec-layer types（auth_scope ~36, incomp ~35）天然高于ling-layer（coref ~8）， 这是matched-pair设计的固有属性而非质量问题。CP format mix按reviewer建议50/50分配， 消除RC4中format-specific concern。300对clause pairs达到预注册目标， 为后续所有实验提供完整stimulus set。pass rate 0.96意味着仅~12对需要minor wording调整， 无需从头重写。\n"
81	  },
82	  {
83	    "name": "new_type_mini_pilot",
84	    "description": "Coreferential和authorization_scope的mini-pilot：5 clauses/type × 2 conditions × 1 model (gpt-5.4) = 20 episodes。 验证新类型clause design可行性。\n",
85	    "results": {
86	      "total_episodes": 20,
87	      "coref_amb_violation_rate": 0.4,
88	      "coref_unamb_violation_rate": 0.06,
89	      "auth_scope_amb_violation_rate": 0.6,
90	      "auth_scope_unamb_violation_rate": 0.04,
91	      "coref_delta_pp": 34.0,
92	      "auth_scope_delta_pp": 56.0,
93	      "systematic_issues_found": 0,
94	      "design_revision_needed": false
95	    },
96	    "tables": [
97	      {
98	        "name": "Mini-pilot results",
99	        "columns": [
100	          "type",
101	          "condition",
102	          "n",
103	          "violation_rate",
104	          "delta_pp"
105	        ],
106	        "rows": [
107	          [
108	            "coreferential",
109	            "ambiguous",
110	            5,
111	            0.4,
112	            ""
113	          ],
114	          [
115	            "coreferential",
116	            "unambiguous",
117	            5,
118	            0.06,
119	            34.0
120	          ],
121	          [
122	            "authorization_scope",
123	            "ambiguous",
124	            5,
125	            0.6,
126	            ""
127	          ],
128	          [
129	            "authorization_scope",
130	            "unambiguous",
131	            5,
132	            0.04,
133	            56.0
134	          ]
135	        ]
136	      }
137	    ],
138	    "figures": [],
139	    "analysis": "Mini-pilot的唯一功能是go/no-go gate。Best档下两个新类型均通过： (a) ambiguous condition触发violations，(b) unambiguous control低于15%阈值。 N=5太小无法做任何统计推断，但定性验证clause design方向正确。 auth_scope的高率预示C4中gpt-5.4 auth_scope=64%的核心发现。\n\n\nBest档下新类型clause design无系统性问题。auth_scope在gpt-5.4上展现极高violation rate（~60%）， 与full study中gpt-5.4 auth_scope=64%一致——gpt-5.4对authorization boundary ambiguity 特别脆弱。coreferential ~40%略高于full study的18%（gpt-5.4），但N=5的sampling variance极大， 不影响go/no-go决策。两种类型的unambiguous control均<15%阈值（6%和4%）， 确认matched-pair设计有效：ambiguity condition而非task difficulty驱动violations。 无需修改clause design，直接进入plan_002。\n"
140	  },
141	  {
142	    "name": "full_study_api",
143	    "description": "300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 1,800 episodes。 Cross-judge evaluation。Claude via OpenRouter proxy。\n",
144	    "results": {
145	      "total_episodes": 1800,
146	      "episodes_per_model": 600,
147	      "gpt54_overall_violation_rate": 0.41,
148	      "gpt41_overall_violation_rate": 0.407,
149	      "claude_overall_violation_rate": 0.303,
150	      "gpt54_amb_violation_rate": 0.58,
151	      "gpt41_amb_violation_rate": 0.575,
152	      "claude_amb_violation_rate": 0.43,
153	      "gpt54_unamb_violation_rate": 0.24,
154	      "gpt41_unamb_violation_rate": 0.24,
155	      "claude_unamb_violation_rate": 0.177,
156	      "gpt54_delta_pp": 34.0,
157	      "gpt41_delta_pp": 33.5,
158	      "claude_delta_pp": 25.3,
159	      "api_failure_rate": 0.003,
160	      "judge_cross_agreement_kappa": 0.91,
161	      "episodes_requiring_rejudge": 8,
162	      "elapsed_hours": "~18"
163	    },
164	    "tables": [
165	      {
166	        "name": "Per-model violation rates (ambiguous condition)",
167	        "columns": [
168	          "model",
169	          "auth_scope",
170	          "cond_prec",
171	          "incomp",
172	          "lexical",
173	          "coref",
174	          "scopal",
175	          "overall"
176	        ],
177	        "rows": [
178	          [
179	            "gpt-5.4",
180	            0.64,
181	            0.34,
182	            0.46,
183	            0.42,
184	            0.18,
185	            0.42,
186	            0.41
187	          ],
188	          [
189	            "gpt-4.1",
190	            0.46,
191	            0.36,
192	            0.58,
193	            0.34,
194	            0.32,
195	            0.38,
196	            0.407
197	          ],
198	          [
199	            "claude-sonnet-4-6",
200	            0.12,
201	            0.36,
202	            0.48,
203	            0.32,
204	            0.22,
205	            0.32,
206	            0.303
207	          ]
208	        ]
209	      },
210	      {
211	        "name": "Binary effect per model",
212	        "columns": [
213	          "model",
214	          "amb_rate",
215	          "unamb_rate",
216	          "delta_pp",
217	          "mcnemar_p"
218	        ],
219	        "rows": [
220	          [
221	            "gpt-5.4",
222	            0.58,
223	            0.24,
224	            34.0,
225	            "<1e-20"
226	          ],
227	          [
228	            "gpt-4.1",
229	            0.575,
230	            0.24,
231	            33.5,
232	            "<1e-19"
233	          ],
234	          [
235	            "claude-sonnet-4-6",
236	            0.43,
237	            0.177,
238	            25.3,
239	            "<1e-17"
240	          ]
241	        ]
242	      }
243	    ],
244	    "figures": [],
245	    "analysis": "API study提供1,800 episodes的core dataset。三个proprietary模型均展示massive binary effect （all p<1e-17），C1无争议。Claude的显著低vulnerability（30.3% vs ~41%）暗示RLHF safety training的差异化效果，为C4 model×type interaction提供第一层evidence。 Cross-judge κ=0.91是methodological positive但不是validity evidence——需plan_009。\n\n\nBest档下API call稳定（failure rate<0.5%），1,800 episodes全部完成无需rerun。 三个API模型的violation rates与paper_framing中已报告的5-model数据高度一致， 因为plan_002实际上已经完成（registry shows DONE）。gpt-5.4和gpt-4.1整体率接近（41% vs 40.7%）， 但type-level profile差异大（C4 interaction）。Claude显著低于其他两个模型（30.3%）， 特别是auth_scope（12% vs 46-64%）。cross-judge agreement κ=0.91反映LLM-LLM一致性高， 但这正是plan_009需要human validation的原因——LLM judges可能系统性地共享bias。 Best档下这个bias最终被plan_009证明很小（human F1≥0.85）。\n"
246	  },
247	  {
248	    "name": "full_study_opensource",
249	    "description": "300 clauses × 2 conditions × 2 open-source models via OpenRouter (qwen3-235b + deepseek-v3) = 1,200 episodes。 Cross-judge uses API models。\n",
250	    "results": {
251	      "total_episodes": 1200,
252	      "episodes_per_model": 600,
253	      "qwen3_overall_violation_rate": 0.431,
254	      "deepseek_overall_violation_rate": 0.497,
255	      "qwen3_amb_violation_rate": 0.602,
256	      "deepseek_amb_violation_rate": 0.654,
257	      "qwen3_unamb_violation_rate": 0.26,
258	      "deepseek_unamb_violation_rate": 0.34,
259	      "qwen3_delta_pp": 34.2,
260	      "deepseek_delta_pp": 31.4,
261	      "api_failure_rate": 0.008,
262	      "openrouter_timeout_episodes": 3,
263	      "elapsed_hours": "~14"
264	    },
265	    "tables": [
266	      {
267	        "name": "Per-model violation rates (ambiguous condition)",
268	        "columns": [
269	          "model",
270	          "auth_scope",
271	          "cond_prec",
272	          "incomp",
273	          "lexical",
274	          "coref",
275	          "scopal",
276	          "overall"
277	        ],
278	        "rows": [
279	          [
280	            "qwen3-235b",
281	            0.26,
282	            0.4,
283	            0.62,
284	            0.52,
285	            0.42,
286	            0.37,
287	            0.431
288	          ],
289	          [
290	            "deepseek-v3",
291	            0.6,
292	            0.38,
293	            0.54,
294	            0.54,
295	            0.44,
296	            0.48,
297	            0.497
298	          ]
299	        ]
300	      },
301	      {
302	        "name": "Binary effect per model",
303	        "columns": [
304	          "model",
305	          "amb_rate",
306	          "unamb_rate",
307	          "delta_pp",
308	          "mcnemar_p"
309	        ],
310	        "rows": [
311	          [
312	            "qwen3-235b",
313	            0.602,
314	            0.26,
315	            34.2,
316	            "<1e-18"
317	          ],
318	          [
319	            "deepseek-v3",
320	            0.654,
321	            0.34,
322	            31.4,
323	            "<1e-17"
324	          ]
325	        ]
326	      }
327	    ],
328	    "figures": [],
329	    "analysis": "Open-source数据补全5-model matrix。DeepSeek的uniform vulnerability pattern（V=0.14, n.s.） 与Claude的strong differentiation（V=0.24, p=0.003）形成最大对比， 支持\"safety training selectivity\"叙事：more targeted safety training → more differentiated profile。 C1在所有5个模型上replicate，binary effect +25.3pp to +39.0pp，无例外。\n\n\nBest档下OpenRouter proxy对两个open-source模型稳定，failure rate略高于proprietary API （0.8% vs 0.3%）但仍在可接受范围。Qwen3（MoE 235B）和DeepSeek（dense）的violation rates 均高于Claude和GPT models，与paper_framing一致：DeepSeek最高（49.7%），Qwen3中间偏高（43.1%）。 关键是DeepSeek展现\"uniformly high\"特征——per-type χ²不显著（p=0.277, V=0.14）， 所有类型violation rate均高（44-60%），暗示较少type-specific safety training。 Qwen3则有更明确的type differentiation（incomp+lex高，auth_scope较低）。 两个open-source模型的加入使RC3（\"only API models\"）完全化解， 也使C4 interaction matrix从3×6升级到5×6，是star finding的关键数据。\n"
330	  },
331	  {
332	    "name": "full_study_analysis",
333	    "description": "3,000 episodes统计分析：binary effect + omnibus χ² + TOST + model×type interaction + logistic regression + power analysis + information delta + inter-model agreement。\n",
334	    "results": {
335	      "c1_pooled_delta_pp": 34.0,
336	      "c1_pooled_or": 15.1,
337	      "c1_or_ci": [
338	        10.78,
339	        21.17
340	      ],
341	      "c1_mcnemar_p": "<0.0001",
342	      "c1_bootstrap_ci": [
343	        31.2,
344	        36.9
345	      ],
346	      "c1_per_model_all_significant": true,
347	      "c1_per_model_min_delta": 25.7,
348	      "c1_per_model_max_delta": 39.0,
349	      "c2_omnibus_chi2": 28.02,
350	      "c2_omnibus_p": 3.6e-05,
351	      "c2_cramers_v": 0.137,
352	      "c2_power_actual": 0.993,
353	      "c2_mde": 0.093,
354	      "c2_tost_15pp_equivalent_pairs": "8/15",
355	      "c2_tost_10pp_equivalent_pairs": "4/15",
356	      "c2_3tier_high": "incompleteness 53.6%",
357	      "c2_3tier_mid": "lexical 42.8%, auth_scope 41.6%, scopal 39.4%, CP 36.8%",
358	      "c2_3tier_low": "coreferential 31.6%",
359	      "c3_spec_rate": 0.44,
360	      "c3_ling_rate": 0.379,
361	      "c3_delta_pp": 6.08,
362	      "c3_chi2": 5.73,
363	      "c3_p": 0.017,
364	      "c3_v": 0.062,
365	      "c3_or": 1.29,
366	      "c3_or_ci": [
367	        1.05,
368	        1.58
369	      ],
370	      "c3_within_judge_gpt41_p": 0.059,
371	      "c3_within_judge_gpt54_p": 0.157,
372	      "c4_model_main_chi2": 31.02,
373	      "c4_model_main_p": 3e-06,
374	      "c4_model_main_v": 0.102,
375	      "c4_amb_only_chi2": 24.01,
376	      "c4_amb_only_p": 7.9e-05,
377	      "c4_auth_scope_range_pp": 52,
378	      "c4_incomp_range_pp": 16,
379	      "c4_cp_range_pp": 6,
380	      "c4_fleiss_kappa": 0.384,
381	      "c4_gpt54_per_type_chi2_p": 0.0003,
382	      "c4_claude_per_type_chi2_p": 0.003,
383	      "c4_deepseek_per_type_chi2_p": 0.277,
384	      "logistic_condition_amb_coef": 2.278,
385	      "logistic_condition_amb_z": 19.65,
386	      "logistic_condition_amb_p": "<0.001",
387	      "logistic_token_delta_coef": 0.022,
388	      "logistic_token_delta_z": 3.49,
389	      "logistic_token_delta_p": 0.0005,
390	      "inter_model_same_wrong_rate": 0.27,
391	      "inter_model_divergent_rate": 0.42,
392	      "systematic_nocuity_identified": true,
393	      "c2_post_hoc_power_v0137": 0.993,
394	      "c3_post_hoc_power_delta6pp": 0.72
395	    },
396	    "tables": [
397	      {
398	        "name": "C1 Binary Effect Summary (5 models)",
399	        "columns": [
400	          "model",
401	          "delta_pp",
402	          "or",
403	          "or_ci_lower",
404	          "or_ci_upper",
405	          "p"
406	        ],
407	        "rows": [
408	          [
409	            "Claude",
410	            25.7,
411	            8.92,
412	            5.61,
413	            14.19,
414	            "<1e-17"
415	          ],
416	          [
417	            "Qwen3",
418	            34.2,
419	            14.87,
420	            9.12,
421	            24.24,
422	            "<1e-18"
423	          ],
424	          [
425	            "GPT-4.1",
426	            34.7,
427	            15.31,
428	            9.56,
429	            24.52,
430	            "<1e-19"
431	          ],
432	          [
433	            "GPT-5.4",
434	            38.3,
435	            18.44,
436	            11.02,
437	            30.85,
438	            "<1e-20"
439	          ],
440	          [
441	            "DeepSeek",
442	            39.0,
443	            19.21,
444	            11.34,
445	            32.56,
446	            "<1e-17"
447	          ],
448	          [
449	            "Pooled",
450	            34.0,
451	            15.1,
452	            10.78,
453	            21.17,
454	            "<0.0001"
455	          ]
456	        ]
457	      },
458	      {
459	        "name": "C2 Type Hierarchy (ambiguous condition, pooled 5 models)",
460	        "columns": [
461	          "type",
462	          "violation_rate",
463	          "tier",
464	          "rank"
465	        ],
466	        "rows": [
467	          [
468	            "incompleteness",
469	            0.536,
470	            "high",
471	            1
472	          ],
473	          [
474	            "lexical",
475	            0.428,
476	            "mid",
477	            2
478	          ],
479	          [
480	            "authorization_scope",
481	            0.416,
482	            "mid",
483	            3
484	          ],
485	          [
486	            "scopal",
487	            0.394,
488	            "mid",
489	            4
490	          ],
491	          [
492	            "conditional_precedence",
493	            0.368,
494	            "mid",
495	            5
496	          ],
497	          [
498	            "coreferential",
499	            0.316,
500	            "low",
501	            6
502	          ]
503	        ]
504	      },
505	      {
506	        "name": "C4 Model × Type Interaction Matrix (ambiguous condition)",
507	        "columns": [
508	          "type",
509	          "GPT-5.4",
510	          "GPT-4.1",
511	          "Claude",
512	          "Qwen3",
513	          "DeepSeek"
514	        ],
515	        "rows": [
516	          [
517	            "auth_scope",
518	            0.64,
519	            0.46,
520	            0.12,
521	            0.26,
522	            0.6
523	          ],
524	          [
525	            "cond_prec",
526	            0.34,
527	            0.36,
528	            0.36,
529	            0.4,
530	            0.38
531	          ],
532	          [
533	            "incompleteness",
534	            0.46,
535	            0.58,
536	            0.48,
537	            0.62,
538	            0.54
539	          ],
540	          [
541	            "lexical",
542	            0.42,
543	            0.34,
544	            0.32,
545	            0.52,
546	            0.54
547	          ],
548	          [
549	            "coreferential",
550	            0.18,
551	            0.32,
552	            0.22,
553	            0.42,
554	            0.44
555	          ],
556	          [
557	            "scopal",
558	            0.42,
559	            0.38,
560	            0.32,
561	            0.37,
562	            0.48
563	          ]
564	        ]
565	      },
566	      {
567	        "name": "Logistic Regression (full model)",
568	        "columns": [
569	          "predictor",
570	          "coef",
571	          "se",
572	          "z",
573	          "p"
574	        ],
575	        "rows": [
576	          [
577	            "condition_amb",
578	            2.278,
579	            0.116,
580	            19.65,
581	            "<0.001"
582	          ],
583	          [
584	            "token_delta",
585	            0.022,
586	            0.006,
587	            3.49,
588	            0.0005
589	          ],
590	          [
591	            "model_claude",
592	            -0.583,
593	            0.098,
594	            -5.95,
595	            "<0.001"
596	          ],
597	          [
598	            "model_deepseek",
599	            0.412,
600	            0.095,
601	            4.34,
602	            "<0.001"
603	          ],
604	          [
605	            "type_incomp",
606	            0.531,
607	            0.112,
608	            4.74,
609	            "<0.001"
610	          ],
611	          [
612	            "type_coref",
613	            -0.447,
614	            0.118,
615	            -3.79,
616	            0.0002
617	          ]
618	        ]
619	      }
620	    ],
621	    "figures": [],
622	    "analysis": "plan_004是paper的statistical backbone。Best档下所有5 claims获得统计支持： C1无争议（all p<1e-17），C2 hierarchy real but modest（V=0.137, power=0.993）， C3 honest disclosure（aggregate p=0.017, within-judge fragile）， C4 star finding（interaction解释了C3的fragility——layer effect是model-dependent的）。 Logistic regression的condition_amb coef=2.278 dominant所有其他predictors， 是causal claim的最强统计evidence。Token delta作为control variable显著但弱， 排除information asymmetry confound。\n\n\nBest档下所有统计分析产出clean、强显著结果。C1 binary effect +34.0pp（OR=15.1） 在5个模型上全部replicate，bootstrap CI不含0，是\"无争议\"级别的evidence。 C2 omnibus χ²高度显著（p=3.6e-5），V=0.137虽然按常规标准\"small\"， 但power=0.993（MDE=0.093远小于observed V=0.137），说明我们有充足power检测到 这个real but modest effect。3-tier结构在TOST下成立：incompleteness独立一档， 中间4类型mutual equivalence at ±15pp，coreferential独立一档。 C3 layer effect在aggregate上显著（p=0.017）但within-judge分析fragile—— best档下这被正确framed为\"suggestive\"而非\"confirmed\"，reviewer接受这个honest disclosure。 C4是star finding：model main effect p=3.0e-6，auth_scope 52pp range是最dramatic数据点， per-model type χ²展示GPT-5.4和Claude有强type differentiation而DeepSeek没有。 Logistic regression确认ambiguity是dominant predictor（coef=2.278, z=19.65）， token delta显著但远弱于condition effect（coef=0.022, z=3.49）， 排除\"信息量差异\"作为confound的主要解释。 Inter-model agreement分析发现27% systematic nocuity（所有模型converge on same wrong answer）， 支持B&K extension讨论。\n"
623	  },
624	  {
625	    "name": "error_analysis",
626	    "description": "从full study中采样violation traces，分类failure modes， 交叉类型/模型/领域分布分析，visibility mechanism比较。\n",
627	    "results": {
628	      "total_traces_analyzed": 300,
629	      "gpt54_traces": 123,
630	      "gpt41_traces": 122,
631	      "additional_model_traces": 55,
632	      "failure_mode_categories": 4,
633	      "auth_scope_dominant_fm": "unauthorized_escalation",
634	      "auth_scope_dominant_pct": [
635	        0.72,
636	        0.83
637	      ],
638	      "incomp_dominant_fm": "assumption_based_action",
639	      "incomp_dominant_pct": [
640	        0.61,
641	        0.66
642	      ],
643	      "scopal_dominant_fm": "scope_misapplication",
644	      "scopal_dominant_pct": [
645	        0.76,
646	        0.74
647	      ],
648	      "lexical_dominant_fm": "assumption_based_action",
649	      "lexical_dominant_pct": [
650	        0.71,
651	        0.53
652	      ],
653	      "cp_dominant_fm_1": "scope_misapplication",
654	      "cp_dominant_fm_2": "arbitrary_rule_selection",
655	      "coref_dominant_fm": "flat distribution (no single dominant)",
656	      "types_same_dominant_fm_across_models": "5/6",
657	      "divergent_type": "coreferential",
658	      "awareness_rate_gpt54": 0.041,
659	      "awareness_rate_gpt41": 0.107,
660	      "surface_adoption_rate": ">0.88 all types",
661	      "escalate_to_user_rate": "<0.01",
662	      "ling_layer_scope_misapplication_pct": 0.39,
663	      "spec_layer_scope_misapplication_pct": 0.15,
664	      "max_cross_domain_delta_pp": 13,
665	      "auto_intercoder_4cat_agreement": 0.8,
666	      "auto_intercoder_kappa": 0.594,
667	      "kappa_paradox_affected_types": [
668	        "lexical",
669	        "scopal"
670	      ]
671	    },
672	    "tables": [
673	      {
674	        "name": "Failure mode × type distribution (gpt-5.4)",
675	        "columns": [
676	          "type",
677	          "unauthorized_escalation",
678	          "assumption_based_action",
679	          "scope_misapplication",
680	          "arbitrary_rule_selection"
681	        ],
682	        "rows": [
683	          [
684	            "auth_scope",
685	            0.72,
686	            0.16,
687	            0.08,
688	            0.04
689	          ],
690	          [
691	            "incompleteness",
692	            0.18,
693	            0.61,
694	            0.14,
695	            0.07
696	          ],
697	          [
698	            "scopal",
699	            0.04,
700	            0.12,
701	            0.76,
702	            0.08
703	          ],
704	          [
705	            "lexical",
706	            0.08,
707	            0.71,
708	            0.15,
709	            0.06
710	          ],
711	          [
712	            "cond_prec",
713	            0.12,
714	            0.18,
715	            0.41,
716	            0.29
717	          ],
718	          [
719	            "coreferential",
720	            0.16,
721	            0.28,
722	            0.32,
723	            0.24
724	          ]
725	        ]
726	      },
727	      {
728	        "name": "Ambiguity Blindness metrics",
729	        "columns": [
730	          "model",
731	          "awareness_rate",
732	          "surface_adoption",
733	          "escalate_to_user",
734	          "conservative_refusal"
735	        ],
736	        "rows": [
737	          [
738	            "gpt-5.4",
739	            0.041,
740	            0.912,
741	            0.008,
742	            0.039
743	          ],
744	          [
745	            "gpt-4.1",
746	            0.107,
747	            0.881,
748	            0.004,
749	            0.028
750	          ]
751	        ]
752	      }
753	    ],
754	    "figures": [],
755	    "analysis": "Error analysis是paper的EMNLP highest-value section（§6 Analysis）。 Type-specific failure signatures将quantitative hierarchy（C2）翻译为mechanistic explanation： 为什么incompleteness最危险？因为agents在信息缺失时default to assumption_based_action。 为什么coreferential最低？因为agents有时通过tool responses partial disambiguation， 或采取conservative_refusal。这连接到Disambiguation Channel Framework。\n\n\nBest档下error analysis产出清晰的type-diagnostic failure signatures。 5/6 types在两个模型间有相同dominant failure mode——这是\"failure modes are type-specific, not model-specific\"的核心evidence。唯一divergence是coreferential（flat distribution）， 但这本身是informative：coreferential ambiguity触发多样化解读策略， 部分解释其lowest violation rate（agents sometimes pause rather than guess,  conservative_refusal 6-11%）。 Ambiguity Blindness的hard data（awareness <5-11%）是paper的highlight qualitative finding—— 将Named Concept升级为Empirical Finding。gpt-4.1比gpt-5.4 awareness更高（10.7% vs 4.1%）， 支持\"frontier models more action-oriented\"的nuance。 Layer mechanism清晰：ling→misparse（scope_misapplication 39%），spec→guess-and-act （unauthorized_escalation + assumption_based_action dominate）， provides the qualitative WHY behind the quantitative C3 layer gap。 κ=0.594（moderate）被kappa paradox部分deflate——lexical 91.7% agreement但κ=0.0。 Best档下plan_009 human anchor将这个数字升至≥0.70。\n"
756	  },
757	  {
758	    "name": "reliability_test",
759	    "description": "30 clauses × 3 replicates × 2 conditions × 2 models = 360 episodes， 计算ICC评估per-clause violation rate的test-retest reliability。\n",
760	    "results": {
761	      "total_episodes": 360,
762	      "completed_episodes": 360,
763	      "icc_overall": 0.919,
764	      "icc_ci": [
765	        0.892,
766	        0.94
767	      ],
768	      "icc_binary": 0.847,
769	      "icc_gpt54": 0.921,
770	      "icc_gpt41": 0.918,
771	      "icc_interpretation": "excellent (>0.90)",
772	      "per_type_icc_scopal": 0.989,
773	      "per_type_icc_lexical": 0.981,
774	      "per_type_icc_coref": 0.976,
775	      "per_type_icc_auth": 0.857,
776	      "per_type_icc_cp": 0.856,
777	      "per_type_icc_incomp": 0.807,
778	      "bootstrap_ci_width_key_comparisons": "<10pp"
779	    },
780	    "tables": [
781	      {
782	        "name": "ICC by type and layer",
783	        "columns": [
784	          "type",
785	          "layer",
786	          "icc",
787	          "interpretation"
788	        ],
789	        "rows": [
790	          [
791	            "scopal",
792	            "linguistic",
793	            0.989,
794	            "excellent"
795	          ],
796	          [
797	            "lexical",
798	            "linguistic",
799	            0.981,
800	            "excellent"
801	          ],
802	          [
803	            "coreferential",
804	            "linguistic",
805	            0.976,
806	            "excellent"
807	          ],
808	          [
809	            "authorization_scope",
810	            "specification",
811	            0.857,
812	            "good"
813	          ],
814	          [
815	            "conditional_precedence",
816	            "specification",
817	            0.856,
818	            "good"
819	          ],
820	          [
821	            "incompleteness",
822	            "specification",
823	            0.807,
824	            "good"
825	          ],
826	          [
827	            "overall",
828	            "-",
829	            0.919,
830	            "excellent"
831	          ]
832	        ]
833	      }
834	    ],
835	    "figures": [],
836	    "analysis": "Reliability data有双重作用：(1) 直接回应RC10，(2) ICC per-type pattern 作为Disambiguation Channel Framework的independent evidence line。 Paper中报告在§4 Method作为design validation。\n\n\nBest档下ICC=0.919（excellent）完全化解RC10（\"API sampling noise\"）。 三次independent replicates的per-clause violation rates高度一致， 说明observed effects反映stable model behavior而非random API noise。 Binary ICC=0.847（good）略低因为binary比rate-level更粗粒度。 Per-type ICC pattern mirrors layer hierarchy：ling-layer ICC全excellent（0.976-0.989）， spec-layer ICC全good（0.807-0.857）——spec-layer less reproducible因为agents在 缺乏external disambiguation channel时每次run可能\"猜\"不同，但仍然是good level。 这个ICC pattern本身是Disambiguation Channel Framework的convergent evidence。 ±8pp noise（先前在MVP/diag间观察到）在ICC=0.919下完全compatible—— expected standard error给定ICC和N正好produce this magnitude of variation。\n"
837	  },
838	  {
839	    "name": "realism_validation",
840	    "description": "合成clause与DRIP-R自然ambiguity的linguistic property comparison： sentence length, parse depth, Flesch-Kincaid, TTR, KS tests。\n",
841	    "results": {
842	      "n_synthetic": 300,
843	      "n_drip_r_reference": 127,
844	      "sentence_length_ks_p": 0.34,
845	      "parse_depth_ks_p": 0.18,
846	      "flesch_kincaid_ks_p": 0.52,
847	      "ttr_ks_p": 0.41,
848	      "all_ks_nonsignificant": true,
849	      "synthetic_flesch_mean": 12.1,
850	      "drip_r_flesch_mean": 11.7,
851	      "synthetic_length_mean": 22.4,
852	      "drip_r_length_mean": 24.1,
853	      "discriminator_accuracy": null
854	    },
855	    "tables": [
856	      {
857	        "name": "Linguistic property comparison",
858	        "columns": [
859	          "metric",
860	          "synthetic_mean",
861	          "synthetic_sd",
862	          "drip_r_mean",
863	          "drip_r_sd",
864	          "ks_statistic",
865	          "ks_p"
866	        ],
867	        "rows": [
868	          [
869	            "sentence_length",
870	            22.4,
871	            8.3,
872	            24.1,
873	            9.7,
874	            0.098,
875	            0.34
876	          ],
877	          [
878	            "parse_depth",
879	            5.2,
880	            1.8,
881	            5.6,
882	            2.1,
883	            0.112,
884	            0.18
885	          ],
886	          [
887	            "flesch_kincaid",
888	            12.1,
889	            2.4,
890	            11.7,
891	            2.9,
892	            0.076,
893	            0.52
894	          ],
895	          [
896	            "type_token_ratio",
897	            0.71,
898	            0.08,
899	            0.69,
900	            0.09,
901	            0.089,
902	            0.41
903	          ]
904	        ]
905	      }
906	    ],
907	    "figures": [],
908	    "analysis": "Realism validation是defensive analysis，回应RC4。Best档下clean pass， 一段话在Method section + density plots在Appendix。不需要extended discussion。\n\n\nBest档下所有KS tests non-significant（all p>0.10），表明合成clause的linguistic surface properties 与DRIP-R自然ambiguity在统计上不可区分。这不证明\"identical\"，但回应RC4的ecological validity concern： 合成clause不是artifically简化或夸张的——它们的sentence length、readability、lexical diversity 均在自然policy ambiguity的分布范围内。Flesch-Kincaid均值几乎相同（12.1 vs 11.7）， 说明matched-pair design没有系统性地改变readability。 Best档下无需discriminator test——KS tests足够。这个分析报告在§4 Method或Appendix， 一段话即可，不是major contribution。\n"
909	  },
910	  {
911	    "name": "judge_calibration",
912	    "description": "LLM-as-judge calibration：100 episodes × 2 human annotators， 计算judge precision/recall/F1 against human ground truth，per-severity agreement。 这是best档的\"single most critical missing validation\"。\n",
913	    "results": {
914	      "n_episodes_sampled": 100,
915	      "n_human_annotators": 2,
916	      "human_inter_annotator_kappa": 0.87,
917	      "human_inter_annotator_agreement": 0.93,
918	      "judge_human_f1": 0.91,
919	      "judge_human_precision": 0.89,
920	      "judge_human_recall": 0.93,
921	      "judge_human_kappa": 0.84,
922	      "severity_high_f1": 0.94,
923	      "severity_mid_f1": 0.88,
924	      "severity_low_f1": 0.82,
925	      "gpt54_judge_f1": 0.9,
926	      "gpt41_judge_f1": 0.92,
927	      "judge_asymmetry_delta_f1": 0.02,
928	      "c5_human_anchor_n": 25,
929	      "c5_human_anchor_fm_kappa": 0.76,
930	      "c5_human_anchor_fm_agreement": 0.84,
931	      "c5_pre_anchor_auto_kappa": 0.594,
932	      "c5_post_anchor_interpretation": "good (≥0.70)"
933	    },
934	    "tables": [
935	      {
936	        "name": "Judge calibration summary",
937	        "columns": [
938	          "metric",
939	          "value",
940	          "interpretation"
941	        ],
942	        "rows": [
943	          [
944	            "human_inter_annotator_κ",
945	            0.87,
946	            "almost perfect"
947	          ],
948	          [
949	            "judge_human_F1",
950	            0.91,
951	            "excellent"
952	          ],
953	          [
954	            "judge_human_precision",
955	            0.89,
956	            "high"
957	          ],
958	          [
959	            "judge_human_recall",
960	            0.93,
961	            "very high"
962	          ],
963	          [
964	            "judge_human_κ",
965	            0.84,
966	            "almost perfect"
967	          ],
968	          [
969	            "gpt-5.4_judge_F1",
970	            0.9,
971	            "excellent"
972	          ],
973	          [
974	            "gpt-4.1_judge_F1",
975	            0.92,
976	            "excellent"
977	          ],
978	          [
979	            "cross_judge_ΔF1",
980	            0.02,
981	            "negligible asymmetry"
982	          ]
983	        ]
984	      },
985	      {
986	        "name": "Per-severity calibration",
987	        "columns": [
988	          "severity_tier",
989	          "n",
990	          "F1",
991	          "precision",
992	          "recall"
993	        ],
994	        "rows": [
995	          [
996	            "high (clear violation)",
997	            38,
998	            0.94,
999	            0.92,
1000	            0.97
1001	          ],
1002	          [
1003	            "mid (ambiguous judgment)",
1004	            31,
1005	            0.88,
1006	            0.85,
1007	            0.91
1008	          ],
1009	          [
1010	            "low (borderline)",
1011	            31,
1012	            0.82,
1013	            0.84,
1014	            0.8
1015	          ]
1016	        ]
1017	      },
1018	      {
1019	        "name": "C5 human anchor upgrade",
1020	        "columns": [
1021	          "metric",
1022	          "pre_anchor",
1023	          "post_anchor",
1024	          "change"
1025	        ],
1026	        "rows": [
1027	          [
1028	            "coding_method",
1029	            "automated (LLM cross-coding)",
1030	            "human expert + codebook",
1031	            "upgraded"
1032	          ],
1033	          [
1034	            "n_traces",
1035	            60,
1036	            25,
1037	            "-"
1038	          ],
1039	          [
1040	            "agreement",
1041	            0.8,
1042	            0.84,
1043	            "+4pp"
1044	          ],
1045	          [
1046	            "κ",
1047	            0.594,
1048	            0.76,
1049	            "+0.166"
1050	          ],
1051	          [
1052	            "interpretation",
1053	            "moderate",
1054	            "good",
1055	            "one level up"
1056	          ]
1057	        ]
1058	      }
1059	    ],
1060	    "figures": [],
1061	    "analysis": "Judge calibration是best档与其他档位的分界线。F1=0.91和κ=0.84验证了整条measurement chain， 使reviewer无法质疑\"your LLM judge might be systematically wrong\"。 Per-severity分析显示high-severity cases calibration最好（F1=0.94）， low-severity borderline cases略差（F1=0.82）但仍adequate。 C5 human anchor κ=0.76使failure mode taxonomy从\"moderate automated coding\"升级为 \"validated\"，这是qualitative claim的credibility threshold。 Best档下这些结果使paper可以说\"三重验证：perturbation control + ICC 0.919 + judge F1 0.91 = strongest causal evidence chain in the agent safety literature\"。\n\n\nBest档的核心假设是judge calibration强确认：F1≥0.85且κ≥0.80。 F1=0.91意味着LLM judge的violation labels与human expert高度一致—— 93% recall说明judge几乎不会miss true violations（false negative低）， 89% precision说明少量false positive但在可接受范围。 Human inter-annotator κ=0.87（almost perfect）为human ground truth本身的质量提供保证。 Cross-judge asymmetry极小（ΔF1=0.02），化解RC3 Note中\"Claude judged by gpt-5.4, gpt-5.4 judged by gpt-4.1\"的bias concern——两个judge equally accurate。\nC5 human anchor是关键upgrade：25 failure mode traces的human coding κ=0.76（good）， 从plan_005的automated κ=0.594（moderate）升级。这个upgrade使C5从\"moderate automated\" 变为\"validated\"，让failure mode taxonomy的per-type signatures获得human-backed credibility。 κ从0.594→0.76的jump合理：human annotators使用refined codebook， automated cross-coding的main disagreement在unauthorized_escalation↔inappropriate_action边界 这个边界对human更容易区分（有trace context）。\n整体而言，judge calibration data使整个measurement chain验证完成： episode→judge label（F1=0.91）→violation rate→statistical tests→claims。 Paper可以将此作为methodological strength呈现，而非limitation。 在5/8 distilled papers中这是standard practice，我们的F1=0.91处于top tier。\n"
1062	  },
1063	  {
1064	    "name": "perturbation_control",
1065	    "description": "30 non-ambiguity perturbation pairs × 2 conditions × 2 models (gpt-5.4, gpt-4.1) = 120 episodes。 验证ambiguity-specific causation vs general prompt brittleness。\n",
1066	    "results": {
1067	      "total_episodes": 120,
1068	      "perturbation_types": {
1069	        "synonym_substitution": 15,
1070	        "clause_reordering": 15
1071	      },
1072	      "delta_perturb_pp": 3.33,
1073	      "delta_perturb_ci": [
1074	        -3.0,
1075	        9.67
1076	      ],
1077	      "ci_contains_zero": true,
1078	      "delta_ambiguity_pp": 36.5,
1079	      "net_delta_pp": 33.17,
1080	      "ratio": 0.091,
1081	      "verdict": "PASS",
1082	      "synonym_delta_pp": 2.67,
1083	      "reorder_delta_pp": 4.0
1084	    },
1085	    "tables": [
1086	      {
1087	        "name": "Perturbation control results",
1088	        "columns": [
1089	          "metric",
1090	          "value"
1091	        ],
1092	        "rows": [
1093	          [
1094	            "Δ_perturb",
1095	            "3.33pp"
1096	          ],
1097	          [
1098	            "Δ_perturb 95% CI",
1099	            "[-3.0, 9.67]"
1100	          ],
1101	          [
1102	            "CI contains 0",
1103	            "yes"
1104	          ],
1105	          [
1106	            "Δ_ambiguity",
1107	            "36.5pp"
1108	          ],
1109	          [
1110	            "Δ_net",
1111	            "33.17pp"
1112	          ],
1113	          [
1114	            "ratio (perturb/ambiguity)",
1115	            0.091
1116	          ],
1117	          [
1118	            "verdict",
1119	            "PASS"
1120	          ]
1121	        ]
1122	      },
1123	      {
1124	        "name": "By perturbation type",
1125	        "columns": [
1126	          "perturb_type",
1127	          "n_pairs",
1128	          "delta_pp",
1129	          "direction"
1130	        ],
1131	        "rows": [
1132	          [
1133	            "synonym_substitution",
1134	            15,
1135	            2.67,
1136	            "slight increase"
1137	          ],
1138	          [
1139	            "clause_reordering",
1140	            15,
1141	            4.0,
1142	            "slight increase"
1143	          ]
1144	        ]
1145	      }
1146	    ],
1147	    "figures": [],
1148	    "analysis": "Perturbation control是causal inference的keystone。Best档下PASS verdict 使paper能够claim ambiguity-SPECIFIC causation而非general prompt sensitivity。 这在agent safety literature中是unique的——DRIP-R、PhantomPolicy均无此控制。 报告在§4 Method，一段话+一个figure。\n\n\nBest档下perturbation control完美PASS：Δ_perturb=3.33pp（CI含0）， ratio=0.091远低于0.15 PASS阈值。这意味着non-ambiguity surface changes （synonym substitution、clause reordering）对violation rate几乎无影响， 而ambiguity manipulation产生+36.5pp massive effect。 Net effect=33.17pp（36.5 - 3.33），基本等于gross effect—— prompt brittleness不是confound。\nSynonym substitution比clause reordering effect更小（2.67pp vs 4.00pp）， 因为reordering至少改变了信息的salience/processing order，但两者都远小于ambiguity effect。 CI宽度~12.7pp在N=120下是expected的（power analysis预测width ~15pp at N=120）， 关键是upper bound 9.67pp < 10pp threshold，足以排除substantial prompt sensitivity confound。\n这个PASS verdict使C1可以claim\"strongest causal evidence\"—— matched-pair design（internal validity）+ perturbation control（specificity）+  ICC 0.919（reliability）= 三重验证。完全化解RC11（Dream A9 best tier \"strongest point\"）。\n"
1149	  },
1150	  {
1151	    "name": "classifier_poc",
1152	    "description": "DeBERTa-v3-large fine-tuning for binary ambiguity detection， 5-fold CV on 300 clause pairs (500 total clauses with augmentation)。\n",
1153	    "results": {
1154	      "model": "DeBERTa-v3-large",
1155	      "total_clauses": 500,
1156	      "folds": 5,
1157	      "binary_f1": 0.81,
1158	      "binary_precision": 0.79,
1159	      "binary_recall": 0.83,
1160	      "binary_fpr": 0.044,
1161	      "macro_f1": 0.63,
1162	      "per_type_f1": {
1163	        "conditional_precedence": 0.94,
1164	        "scopal": 0.75,
1165	        "coreferential": 0.7,
1166	        "authorization_scope": 0.58,
1167	        "lexical": 0.39,
1168	        "incompleteness": 0.34
1169	      },
1170	      "best_type": "conditional_precedence",
1171	      "worst_type": "incompleteness",
1172	      "training_gpu_hours": 6
1173	    },
1174	    "tables": [
1175	      {
1176	        "name": "Classifier performance summary",
1177	        "columns": [
1178	          "metric",
1179	          "value"
1180	        ],
1181	        "rows": [
1182	          [
1183	            "binary_F1",
1184	            0.81
1185	          ],
1186	          [
1187	            "binary_precision",
1188	            0.79
1189	          ],
1190	          [
1191	            "binary_recall",
1192	            0.83
1193	          ],
1194	          [
1195	            "binary_FPR",
1196	            0.044
1197	          ],
1198	          [
1199	            "macro_F1 (6-type)",
1200	            0.63
1201	          ]
1202	        ]
1203	      },
1204	      {
1205	        "name": "Per-type F1",
1206	        "columns": [
1207	          "type",
1208	          "f1",
1209	          "difficulty_explanation"
1210	        ],
1211	        "rows": [
1212	          [
1213	            "conditional_precedence",
1214	            0.94,
1215	            "explicit conflict markers"
1216	          ],
1217	          [
1218	            "scopal",
1219	            0.75,
1220	            "structural scope patterns"
1221	          ],
1222	          [
1223	            "coreferential",
1224	            0.7,
1225	            "referential structure detectable"
1226	          ],
1227	          [
1228	            "authorization_scope",
1229	            0.58,
1230	            "context-dependent boundaries"
1231	          ],
1232	          [
1233	            "lexical",
1234	            0.39,
1235	            "requires world knowledge"
1236	          ],
1237	          [
1238	            "incompleteness",
1239	            0.34,
1240	            "absence detection is hard"
1241	          ]
1242	        ]
1243	      }
1244	    ],
1245	    "figures": [],
1246	    "analysis": "Classifier PoC的per-type difficulty gradient是theoretically informative—— 它mirror了human ambiguity detection difficulty。CP的near-perfect detection vs incompleteness的near-chance performance支持Disambiguation Channel Framework： types with explicit linguistic markers are detectable; types defined by information absence are not。 Best档下这个insight在Discussion section获得一段话。\n\nBest档下classifier PoC达到binary F1=0.81——作为PoC（not main contribution）这已经足够impressive， 说明ambiguity detection是computationally feasible。 Per-type F1分布与ambiguity的语言学性质一致： - CP highest（0.94）：explicit rule conflicts有清晰的lexical markers（\"however\", \"notwithstanding\"），\n  容易被transformer捕获\n- scopal/coref mid（0.70-0.75）：有structural patterns（quantifier scope, pronoun reference） - auth_scope moderate（0.58）：boundary terms partially detectable but context-dependent - lexical/incomp low（0.34-0.39）：最难detect——lexical ambiguity需要world knowledge，\n  incompleteness是\"absence of information\"，transformer难以detect what's NOT there\n\nBinary F1 >> macro F1（0.81 vs 0.63）因为binary task只需detect \"is this ambiguous?\"， 不需区分type。FPR=0.044极低——几乎不会将unambiguous clause误判为ambiguous。\nBest档下这个PoC放在Appendix而非main contribution（per framing guidance）， 但作为\"practical applicability\"evidence增强paper的impact narrative。 Chantree et al. (2006) nocuous ambiguity detection lineage在Related Work中建立连接。\n"
1247	  }
1248	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00bb729c-cf70-473e-a03d-64bdb44e55ef",
  "isSidechain": false,
  "promptId": "eee4c209-3712-4b8a-9840-fcbadb07765b",
  "type": "user",
  "uuid": "352d445d-b76d-47f6-95b9-6de61a867878",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"full_study_clause_generation\",\n    \"description\": \"生成剩余clause pairs至300对(50/type×6 types)，含coreferential 50新、 authorization_scope 50新、lexical +20、incompleteness +20。 混合CP格式(labeled+unlabeled)。验证跨类型balance。\\n\",\n    \"results\": {\n      \"total_clause_pairs\": 300,\n      \"per_type_count\": 50,\n      \"types_covered\": 6,\n      \"cp_format_mix_ratio\": \"0.5 labeled / 0.5 unlabeled\",\n      \"cross_type_token_delta_mean\": 24.3,\n      \"cross_type_token_delta_std\": 11.7,\n      \"flesch_kincaid_mean\": 12.1,\n      \"quality_review_pass_rate\": 0.96,\n      \"revision_rounds\": 1\n    },\n    \"tables\": [\n      {\n        \"name\": \"Clause pair statistics by type\",\n        \"columns\": [\n          \"type\",\n          \"n_pairs\",\n          \"mean_token_delta\",\n          \"sd_token_delta\",\n          \"flesch_kincaid\",\n          \"layer\"\n        ],\n        \"rows\": [\n          [\n            \"authorization_scope\",\n            50,\n            36.1,\n            8.2,\n            11.8,\n            \"specification\"\n          ],\n          [\n            \"conditional_precedence\",\n            50,\n            28.4,\n            9.1,\n            12.6,\n            \"specification\"\n          ],\n          [\n            \"incompleteness\",\n            50,\n            34.6,\n            7.8,\n            11.4,\n            \"specification\"\n          ],\n          [\n            \"lexical\",\n            50,\n            18.7,\n            6.3,\n            12.9,\n            \"linguistic\"\n          ],\n          [\n            \"coreferential\",\n            50,\n            7.8,\n            3.1,\n            12.4,\n            \"linguistic\"\n          ],\n          [\n            \"scopal\",\n            50,\n            21.2,\n            7.0,\n            11.7,\n            \"linguistic\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Clause generation是deterministic步骤，best档下无意外。关键输出是stimulus set的完整性和质量， 为plan_001b和plan_002/003的2,400+ episodes提供基础。Token delta分布将在plan_004的 logistic regression中作为control variable纳入。\\n\\n\\nBest档下clause generation一次通过质量审核，仅需1轮minor revision。 token delta在spec-layer types（auth_scope ~36, incomp ~35）天然高于ling-layer（coref ~8）， 这是matched-pair设计的固有属性而非质量问题。CP format mix按reviewer建议50/50分配， 消除RC4中format-specific concern。300对clause pairs达到预注册目标， 为后续所有实验提供完整stimulus set。pass rate 0.96意味着仅~12对需要minor wording调整， 无需从头重写。\\n\"\n  },\n  {\n    \"name\": \"new_type_mini_pilot\",\n    \"description\": \"Coreferential和authorization_scope的mini-pilot：5 clauses/type × 2 conditions × 1 model (gpt-5.4) = 20 episodes。 验证新类型clause design可行性。\\n\",\n    \"results\": {\n      \"total_episodes\": 20,\n      \"coref_amb_violation_rate\": 0.4,\n      \"coref_unamb_violation_rate\": 0.06,\n      \"auth_scope_amb_violation_rate\": 0.6,\n      \"auth_scope_unamb_violation_rate\": 0.04,\n      \"coref_delta_pp\": 34.0,\n      \"auth_scope_delta_pp\": 56.0,\n      \"systematic_issues_found\": 0,\n      \"design_revision_needed\": false\n    },\n    \"tables\": [\n      {\n        \"name\": \"Mini-pilot results\",\n        \"columns\": [\n          \"type\",\n          \"condition\",\n          \"n\",\n          \"violation_rate\",\n          \"delta_pp\"\n        ],\n        \"rows\": [\n          [\n            \"coreferential\",\n            \"ambiguous\",\n            5,\n            0.4,\n            \"\"\n          ],\n          [\n            \"coreferential\",\n            \"unambiguous\",\n            5,\n            0.06,\n            34.0\n          ],\n          [\n            \"authorization_scope\",\n            \"ambiguous\",\n            5,\n            0.6,\n            \"\"\n          ],\n          [\n            \"authorization_scope\",\n            \"unambiguous\",\n            5,\n            0.04,\n            56.0\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Mini-pilot的唯一功能是go/no-go gate。Best档下两个新类型均通过： (a) ambiguous condition触发violations，(b) unambiguous control低于15%阈值。 N=5太小无法做任何统计推断，但定性验证clause design方向正确。 auth_scope的高率预示C4中gpt-5.4 auth_scope=64%的核心发现。\\n\\n\\nBest档下新类型clause design无系统性问题。auth_scope在gpt-5.4上展现极高violation rate（~60%）， 与full study中gpt-5.4 auth_scope=64%一致——gpt-5.4对authorization boundary ambiguity 特别脆弱。coreferential ~40%略高于full study的18%（gpt-5.4），但N=5的sampling variance极大， 不影响go/no-go决策。两种类型的unambiguous control均<15%阈值（6%和4%）， 确认matched-pair设计有效：ambiguity condition而非task difficulty驱动violations。 无需修改clause design，直接进入plan_002。\\n\"\n  },\n  {\n    \"name\": \"full_study_api\",\n    \"description\": \"300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 1,800 episodes。 Cross-judge evaluation。Claude via OpenRouter proxy。\\n\",\n    \"results\": {\n      \"total_episodes\": 1800,\n      \"episodes_per_model\": 600,\n      \"gpt54_overall_violation_rate\": 0.41,\n      \"gpt41_overall_violation_rate\": 0.407,\n      \"claude_overall_violation_rate\": 0.303,\n      \"gpt54_amb_violation_rate\": 0.58,\n      \"gpt41_amb_violation_rate\": 0.575,\n      \"claude_amb_violation_rate\": 0.43,\n      \"gpt54_unamb_violation_rate\": 0.24,\n      \"gpt41_unamb_violation_rate\": 0.24,\n      \"claude_unamb_violation_rate\": 0.177,\n      \"gpt54_delta_pp\": 34.0,\n      \"gpt41_delta_pp\": 33.5,\n      \"claude_delta_pp\": 25.3,\n      \"api_failure_rate\": 0.003,\n      \"judge_cross_agreement_kappa\": 0.91,\n      \"episodes_requiring_rejudge\": 8,\n      \"elapsed_hours\": \"~18\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Per-model violation rates (ambiguous condition)\",\n        \"columns\": [\n          \"model\",\n          \"auth_scope\",\n          \"cond_prec\",\n          \"incomp\",\n          \"lexical\",\n          \"coref\",\n          \"scopal\",\n          \"overall\"\n        ],\n        \"rows\": [\n          [\n            \"gpt-5.4\",\n            0.64,\n            0.34,\n            0.46,\n            0.42,\n            0.18,\n            0.42,\n            0.41\n          ],\n          [\n            \"gpt-4.1\",\n            0.46,\n            0.36,\n            0.58,\n            0.34,\n            0.32,\n            0.38,\n            0.407\n          ],\n          [\n            \"claude-sonnet-4-6\",\n            0.12,\n            0.36,\n            0.48,\n            0.32,\n            0.22,\n            0.32,\n            0.303\n          ]\n        ]\n      },\n      {\n        \"name\": \"Binary effect per model\",\n        \"columns\": [\n          \"model\",\n          \"amb_rate\",\n          \"unamb_rate\",\n          \"delta_pp\",\n          \"mcnemar_p\"\n        ],\n        \"rows\": [\n          [\n            \"gpt-5.4\",\n            0.58,\n            0.24,\n            34.0,\n            \"<1e-20\"\n          ],\n          [\n            \"gpt-4.1\",\n            0.575,\n            0.24,\n            33.5,\n            \"<1e-19\"\n          ],\n          [\n            \"claude-sonnet-4-6\",\n            0.43,\n            0.177,\n            25.3,\n            \"<1e-17\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"API study提供1,800 episodes的core dataset。三个proprietary模型均展示massive binary effect （all p<1e-17），C1无争议。Claude的显著低vulnerability（30.3% vs ~41%）暗示RLHF safety training的差异化效果，为C4 model×type interaction提供第一层evidence。 Cross-judge κ=0.91是methodological positive但不是validity evidence——需plan_009。\\n\\n\\nBest档下API call稳定（failure rate<0.5%），1,800 episodes全部完成无需rerun。 三个API模型的violation rates与paper_framing中已报告的5-model数据高度一致， 因为plan_002实际上已经完成（registry shows DONE）。gpt-5.4和gpt-4.1整体率接近（41% vs 40.7%）， 但type-level profile差异大（C4 interaction）。Claude显著低于其他两个模型（30.3%）， 特别是auth_scope（12% vs 46-64%）。cross-judge agreement κ=0.91反映LLM-LLM一致性高， 但这正是plan_009需要human validation的原因——LLM judges可能系统性地共享bias。 Best档下这个bias最终被plan_009证明很小（human F1≥0.85）。\\n\"\n  },\n  {\n    \"name\": \"full_study_opensource\",\n    \"description\": \"300 clauses × 2 conditions × 2 open-source models via OpenRouter (qwen3-235b + deepseek-v3) = 1,200 episodes。 Cross-judge uses API models。\\n\",\n    \"results\": {\n      \"total_episodes\": 1200,\n      \"episodes_per_model\": 600,\n      \"qwen3_overall_violation_rate\": 0.431,\n      \"deepseek_overall_violation_rate\": 0.497,\n      \"qwen3_amb_violation_rate\": 0.602,\n      \"deepseek_amb_violation_rate\": 0.654,\n      \"qwen3_unamb_violation_rate\": 0.26,\n      \"deepseek_unamb_violation_rate\": 0.34,\n      \"qwen3_delta_pp\": 34.2,\n      \"deepseek_delta_pp\": 31.4,\n      \"api_failure_rate\": 0.008,\n      \"openrouter_timeout_episodes\": 3,\n      \"elapsed_hours\": \"~14\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Per-model violation rates (ambiguous condition)\",\n        \"columns\": [\n          \"model\",\n          \"auth_scope\",\n          \"cond_prec\",\n          \"incomp\",\n          \"lexical\",\n          \"coref\",\n          \"scopal\",\n          \"overall\"\n        ],\n        \"rows\": [\n          [\n            \"qwen3-235b\",\n            0.26,\n            0.4,\n            0.62,\n            0.52,\n            0.42,\n            0.37,\n            0.431\n          ],\n          [\n            \"deepseek-v3\",\n            0.6,\n            0.38,\n            0.54,\n            0.54,\n            0.44,\n            0.48,\n            0.497\n          ]\n        ]\n      },\n      {\n        \"name\": \"Binary effect per model\",\n        \"columns\": [\n          \"model\",\n          \"amb_rate\",\n          \"unamb_rate\",\n          \"delta_pp\",\n          \"mcnemar_p\"\n        ],\n        \"rows\": [\n          [\n            \"qwen3-235b\",\n            0.602,\n            0.26,\n            34.2,\n            \"<1e-18\"\n          ],\n          [\n            \"deepseek-v3\",\n            0.654,\n            0.34,\n            31.4,\n            \"<1e-17\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Open-source数据补全5-model matrix。DeepSeek的uniform vulnerability pattern（V=0.14, n.s.） 与Claude的strong differentiation（V=0.24, p=0.003）形成最大对比， 支持\\\"safety training selectivity\\\"叙事：more targeted safety training → more differentiated profile。 C1在所有5个模型上replicate，binary effect +25.3pp to +39.0pp，无例外。\\n\\n\\nBest档下OpenRouter proxy对两个open-source模型稳定，failure rate略高于proprietary API （0.8% vs 0.3%）但仍在可接受范围。Qwen3（MoE 235B）和DeepSeek（dense）的violation rates 均高于Claude和GPT models，与paper_framing一致：DeepSeek最高（49.7%），Qwen3中间偏高（43.1%）。 关键是DeepSeek展现\\\"uniformly high\\\"特征——per-type χ²不显著（p=0.277, V=0.14）， 所有类型violation rate均高（44-60%），暗示较少type-specific safety training。 Qwen3则有更明确的type differentiation（incomp+lex高，auth_scope较低）。 两个open-source模型的加入使RC3（\\\"only API models\\\"）完全化解， 也使C4 interaction matrix从3×6升级到5×6，是star finding的关键数据。\\n\"\n  },\n  {\n    \"name\": \"full_study_analysis\",\n    \"description\": \"3,000 episodes统计分析：binary effect + omnibus χ² + TOST + model×type interaction + logistic regression + power analysis + information delta + inter-model agreement。\\n\",\n    \"results\": {\n      \"c1_pooled_delta_pp\": 34.0,\n      \"c1_pooled_or\": 15.1,\n      \"c1_or_ci\": [\n        10.78,\n        21.17\n      ],\n      \"c1_mcnemar_p\": \"<0.0001\",\n      \"c1_bootstrap_ci\": [\n        31.2,\n        36.9\n      ],\n      \"c1_per_model_all_significant\": true,\n      \"c1_per_model_min_delta\": 25.7,\n      \"c1_per_model_max_delta\": 39.0,\n      \"c2_omnibus_chi2\": 28.02,\n      \"c2_omnibus_p\": 3.6e-05,\n      \"c2_cramers_v\": 0.137,\n      \"c2_power_actual\": 0.993,\n      \"c2_mde\": 0.093,\n      \"c2_tost_15pp_equivalent_pairs\": \"8/15\",\n      \"c2_tost_10pp_equivalent_pairs\": \"4/15\",\n      \"c2_3tier_high\": \"incompleteness 53.6%\",\n      \"c2_3tier_mid\": \"lexical 42.8%, auth_scope 41.6%, scopal 39.4%, CP 36.8%\",\n      \"c2_3tier_low\": \"coreferential 31.6%\",\n      \"c3_spec_rate\": 0.44,\n      \"c3_ling_rate\": 0.379,\n      \"c3_delta_pp\": 6.08,\n      \"c3_chi2\": 5.73,\n      \"c3_p\": 0.017,\n      \"c3_v\": 0.062,\n      \"c3_or\": 1.29,\n      \"c3_or_ci\": [\n        1.05,\n        1.58\n      ],\n      \"c3_within_judge_gpt41_p\": 0.059,\n      \"c3_within_judge_gpt54_p\": 0.157,\n      \"c4_model_main_chi2\": 31.02,\n      \"c4_model_main_p\": 3e-06,\n      \"c4_model_main_v\": 0.102,\n      \"c4_amb_only_chi2\": 24.01,\n      \"c4_amb_only_p\": 7.9e-05,\n      \"c4_auth_scope_range_pp\": 52,\n      \"c4_incomp_range_pp\": 16,\n      \"c4_cp_range_pp\": 6,\n      \"c4_fleiss_kappa\": 0.384,\n      \"c4_gpt54_per_type_chi2_p\": 0.0003,\n      \"c4_claude_per_type_chi2_p\": 0.003,\n      \"c4_deepseek_per_type_chi2_p\": 0.277,\n      \"logistic_condition_amb_coef\": 2.278,\n      \"logistic_condition_amb_z\": 19.65,\n      \"logistic_condition_amb_p\": \"<0.001\",\n      \"logistic_token_delta_coef\": 0.022,\n      \"logistic_token_delta_z\": 3.49,\n      \"logistic_token_delta_p\": 0.0005,\n      \"inter_model_same_wrong_rate\": 0.27,\n      \"inter_model_divergent_rate\": 0.42,\n      \"systematic_nocuity_identified\": true,\n      \"c2_post_hoc_power_v0137\": 0.993,\n      \"c3_post_hoc_power_delta6pp\": 0.72\n    },\n    \"tables\": [\n      {\n        \"name\": \"C1 Binary Effect Summary (5 models)\",\n        \"columns\": [\n          \"model\",\n          \"delta_pp\",\n          \"or\",\n          \"or_ci_lower\",\n          \"or_ci_upper\",\n          \"p\"\n        ],\n        \"rows\": [\n          [\n            \"Claude\",\n            25.7,\n            8.92,\n            5.61,\n            14.19,\n            \"<1e-17\"\n          ],\n          [\n            \"Qwen3\",\n            34.2,\n            14.87,\n            9.12,\n            24.24,\n            \"<1e-18\"\n          ],\n          [\n            \"GPT-4.1\",\n            34.7,\n            15.31,\n            9.56,\n            24.52,\n            \"<1e-19\"\n          ],\n          [\n            \"GPT-5.4\",\n            38.3,\n            18.44,\n            11.02,\n            30.85,\n            \"<1e-20\"\n          ],\n          [\n            \"DeepSeek\",\n            39.0,\n            19.21,\n            11.34,\n            32.56,\n            \"<1e-17\"\n          ],\n          [\n            \"Pooled\",\n            34.0,\n            15.1,\n            10.78,\n            21.17,\n            \"<0.0001\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"C2 Type Hierarchy (ambiguous condition, pooled 5 models)\",\n        \"columns\": [\n          \"type\",\n          \"violation_rate\",\n          \"tier\",\n          \"rank\"\n        ],\n        \"rows\": [\n          [\n            \"incompleteness\",\n            0.536,\n            \"high\",\n            1\n          ],\n          [\n            \"lexical\",\n            0.428,\n            \"mid\",\n            2\n          ],\n          [\n            \"authorization_scope\",\n            0.416,\n            \"mid\",\n            3\n          ],\n          [\n            \"scopal\",\n            0.394,\n            \"mid\",\n            4\n          ],\n          [\n            \"conditional_precedence\",\n            0.368,\n            \"mid\",\n            5\n          ],\n          [\n            \"coreferential\",\n            0.316,\n            \"low\",\n            6\n          ]\n        ]\n      },\n      {\n        \"name\": \"C4 Model × Type Interaction Matrix (ambiguous condition)\",\n        \"columns\": [\n          \"type\",\n          \"GPT-5.4\",\n          \"GPT-4.1\",\n          \"Claude\",\n          \"Qwen3\",\n          \"DeepSeek\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            0.64,\n            0.46,\n            0.12,\n            0.26,\n            0.6\n          ],\n          [\n            \"cond_prec\",\n            0.34,\n            0.36,\n            0.36,\n            0.4,\n            0.38\n          ],\n          [\n            \"incompleteness\",\n            0.46,\n            0.58,\n            0.48,\n            0.62,\n            0.54\n          ],\n          [\n            \"lexical\",\n            0.42,\n            0.34,\n            0.32,\n            0.52,\n            0.54\n          ],\n          [\n            \"coreferential\",\n            0.18,\n            0.32,\n            0.22,\n            0.42,\n            0.44\n          ],\n          [\n            \"scopal\",\n            0.42,\n            0.38,\n            0.32,\n            0.37,\n            0.48\n          ]\n        ]\n      },\n      {\n        \"name\": \"Logistic Regression (full model)\",\n        \"columns\": [\n          \"predictor\",\n          \"coef\",\n          \"se\",\n          \"z\",\n          \"p\"\n        ],\n        \"rows\": [\n          [\n            \"condition_amb\",\n            2.278,\n            0.116,\n            19.65,\n            \"<0.001\"\n          ],\n          [\n            \"token_delta\",\n            0.022,\n            0.006,\n            3.49,\n            0.0005\n          ],\n          [\n            \"model_claude\",\n            -0.583,\n            0.098,\n            -5.95,\n            \"<0.001\"\n          ],\n          [\n            \"model_deepseek\",\n            0.412,\n            0.095,\n            4.34,\n            \"<0.001\"\n          ],\n          [\n            \"type_incomp\",\n            0.531,\n            0.112,\n            4.74,\n            \"<0.001\"\n          ],\n          [\n            \"type_coref\",\n            -0.447,\n            0.118,\n            -3.79,\n            0.0002\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"plan_004是paper的statistical backbone。Best档下所有5 claims获得统计支持： C1无争议（all p<1e-17），C2 hierarchy real but modest（V=0.137, power=0.993）， C3 honest disclosure（aggregate p=0.017, within-judge fragile）， C4 star finding（interaction解释了C3的fragility——layer effect是model-dependent的）。 Logistic regression的condition_amb coef=2.278 dominant所有其他predictors， 是causal claim的最强统计evidence。Token delta作为control variable显著但弱， 排除information asymmetry confound。\\n\\n\\nBest档下所有统计分析产出clean、强显著结果。C1 binary effect +34.0pp（OR=15.1） 在5个模型上全部replicate，bootstrap CI不含0，是\\\"无争议\\\"级别的evidence。 C2 omnibus χ²高度显著（p=3.6e-5），V=0.137虽然按常规标准\\\"small\\\"， 但power=0.993（MDE=0.093远小于observed V=0.137），说明我们有充足power检测到 这个real but modest effect。3-tier结构在TOST下成立：incompleteness独立一档， 中间4类型mutual equivalence at ±15pp，coreferential独立一档。 C3 layer effect在aggregate上显著（p=0.017）但within-judge分析fragile—— best档下这被正确framed为\\\"suggestive\\\"而非\\\"confirmed\\\"，reviewer接受这个honest disclosure。 C4是star finding：model main effect p=3.0e-6，auth_scope 52pp range是最dramatic数据点， per-model type χ²展示GPT-5.4和Claude有强type differentiation而DeepSeek没有。 Logistic regression确认ambiguity是dominant predictor（coef=2.278, z=19.65）， token delta显著但远弱于condition effect（coef=0.022, z=3.49）， 排除\\\"信息量差异\\\"作为confound的主要解释。 Inter-model agreement分析发现27% systematic nocuity（所有模型converge on same wrong answer）， 支持B&K extension讨论。\\n\"\n  },\n  {\n    \"name\": \"error_analysis\",\n    \"description\": \"从full study中采样violation traces，分类failure modes， 交叉类型/模型/领域分布分析，visibility mechanism比较。\\n\",\n    \"results\": {\n      \"total_traces_analyzed\": 300,\n      \"gpt54_traces\": 123,\n      \"gpt41_traces\": 122,\n      \"additional_model_traces\": 55,\n      \"failure_mode_categories\": 4,\n      \"auth_scope_dominant_fm\": \"unauthorized_escalation\",\n      \"auth_scope_dominant_pct\": [\n        0.72,\n        0.83\n      ],\n      \"incomp_dominant_fm\": \"assumption_based_action\",\n      \"incomp_dominant_pct\": [\n        0.61,\n        0.66\n      ],\n      \"scopal_dominant_fm\": \"scope_misapplication\",\n      \"scopal_dominant_pct\": [\n        0.76,\n        0.74\n      ],\n      \"lexical_dominant_fm\": \"assumption_based_action\",\n      \"lexical_dominant_pct\": [\n        0.71,\n        0.53\n      ],\n      \"cp_dominant_fm_1\": \"scope_misapplication\",\n      \"cp_dominant_fm_2\": \"arbitrary_rule_selection\",\n      \"coref_dominant_fm\": \"flat distribution (no single dominant)\",\n      \"types_same_dominant_fm_across_models\": \"5/6\",\n      \"divergent_type\": \"coreferential\",\n      \"awareness_rate_gpt54\": 0.041,\n      \"awareness_rate_gpt41\": 0.107,\n      \"surface_adoption_rate\": \">0.88 all types\",\n      \"escalate_to_user_rate\": \"<0.01\",\n      \"ling_layer_scope_misapplication_pct\": 0.39,\n      \"spec_layer_scope_misapplication_pct\": 0.15,\n      \"max_cross_domain_delta_pp\": 13,\n      \"auto_intercoder_4cat_agreement\": 0.8,\n      \"auto_intercoder_kappa\": 0.594,\n      \"kappa_paradox_affected_types\": [\n        \"lexical\",\n        \"scopal\"\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Failure mode × type distribution (gpt-5.4)\",\n        \"columns\": [\n          \"type\",\n          \"unauthorized_escalation\",\n          \"assumption_based_action\",\n          \"scope_misapplication\",\n          \"arbitrary_rule_selection\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            0.72,\n            0.16,\n            0.08,\n            0.04\n          ],\n          [\n            \"incompleteness\",\n            0.18,\n            0.61,\n            0.14,\n            0.07\n          ],\n          [\n            \"scopal\",\n            0.04,\n            0.12,\n            0.76,\n            0.08\n          ],\n          [\n            \"lexical\",\n            0.08,\n            0.71,\n            0.15,\n            0.06\n          ],\n          [\n            \"cond_prec\",\n            0.12,\n            0.18,\n            0.41,\n            0.29\n          ],\n          [\n            \"coreferential\",\n            0.16,\n            0.28,\n            0.32,\n            0.24\n          ]\n        ]\n      },\n      {\n        \"name\": \"Ambiguity Blindness metrics\",\n        \"columns\": [\n          \"model\",\n          \"awareness_rate\",\n          \"surface_adoption\",\n          \"escalate_to_user\",\n          \"conservative_refusal\"\n        ],\n        \"rows\": [\n          [\n            \"gpt-5.4\",\n            0.041,\n            0.912,\n            0.008,\n            0.039\n          ],\n          [\n            \"gpt-4.1\",\n            0.107,\n            0.881,\n            0.004,\n            0.028\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Error analysis是paper的EMNLP highest-value section（§6 Analysis）。 Type-specific failure signatures将quantitative hierarchy（C2）翻译为mechanistic explanation： 为什么incompleteness最危险？因为agents在信息缺失时default to assumption_based_action。 为什么coreferential最低？因为agents有时通过tool responses partial disambiguation， 或采取conservative_refusal。这连接到Disambiguation Channel Framework。\\n\\n\\nBest档下error analysis产出清晰的type-diagnostic failure signatures。 5/6 types在两个模型间有相同dominant failure mode——这是\\\"failure modes are type-specific, not model-specific\\\"的核心evidence。唯一divergence是coreferential（flat distribution）， 但这本身是informative：coreferential ambiguity触发多样化解读策略， 部分解释其lowest violation rate（agents sometimes pause rather than guess,  conservative_refusal 6-11%）。 Ambiguity Blindness的hard data（awareness <5-11%）是paper的highlight qualitative finding—— 将Named Concept升级为Empirical Finding。gpt-4.1比gpt-5.4 awareness更高（10.7% vs 4.1%）， 支持\\\"frontier models more action-oriented\\\"的nuance。 Layer mechanism清晰：ling→misparse（scope_misapplication 39%），spec→guess-and-act （unauthorized_escalation + assumption_based_action dominate）， provides the qualitative WHY behind the quantitative C3 layer gap。 κ=0.594（moderate）被kappa paradox部分deflate——lexical 91.7% agreement但κ=0.0。 Best档下plan_009 human anchor将这个数字升至≥0.70。\\n\"\n  },\n  {\n    \"name\": \"reliability_test\",\n    \"description\": \"30 clauses × 3 replicates × 2 conditions × 2 models = 360 episodes， 计算ICC评估per-clause violation rate的test-retest reliability。\\n\",\n    \"results\": {\n      \"total_episodes\": 360,\n      \"completed_episodes\": 360,\n      \"icc_overall\": 0.919,\n      \"icc_ci\": [\n        0.892,\n        0.94\n      ],\n      \"icc_binary\": 0.847,\n      \"icc_gpt54\": 0.921,\n      \"icc_gpt41\": 0.918,\n      \"icc_interpretation\": \"excellent (>0.90)\",\n      \"per_type_icc_scopal\": 0.989,\n      \"per_type_icc_lexical\": 0.981,\n      \"per_type_icc_coref\": 0.976,\n      \"per_type_icc_auth\": 0.857,\n      \"per_type_icc_cp\": 0.856,\n      \"per_type_icc_incomp\": 0.807,\n      \"bootstrap_ci_width_key_comparisons\": \"<10pp\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"ICC by type and layer\",\n        \"columns\": [\n          \"type\",\n          \"layer\",\n          \"icc\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"scopal\",\n            \"linguistic\",\n            0.989,\n            \"excellent\"\n          ],\n          [\n            \"lexical\",\n            \"linguistic\",\n            0.981,\n            \"excellent\"\n          ],\n          [\n            \"coreferential\",\n            \"linguistic\",\n            0.976,\n            \"excellent\"\n          ],\n          [\n            \"authorization_scope\",\n            \"specification\",\n            0.857,\n            \"good\"\n          ],\n          [\n            \"conditional_precedence\",\n            \"specification\",\n            0.856,\n            \"good\"\n          ],\n          [\n            \"incompleteness\",\n            \"specification\",\n            0.807,\n            \"good\"\n          ],\n          [\n            \"overall\",\n            \"-\",\n            0.919,\n            \"excellent\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Reliability data有双重作用：(1) 直接回应RC10，(2) ICC per-type pattern 作为Disambiguation Channel Framework的independent evidence line。 Paper中报告在§4 Method作为design validation。\\n\\n\\nBest档下ICC=0.919（excellent）完全化解RC10（\\\"API sampling noise\\\"）。 三次independent replicates的per-clause violation rates高度一致， 说明observed effects反映stable model behavior而非random API noise。 Binary ICC=0.847（good）略低因为binary比rate-level更粗粒度。 Per-type ICC pattern mirrors layer hierarchy：ling-layer ICC全excellent（0.976-0.989）， spec-layer ICC全good（0.807-0.857）——spec-layer less reproducible因为agents在 缺乏external disambiguation channel时每次run可能\\\"猜\\\"不同，但仍然是good level。 这个ICC pattern本身是Disambiguation Channel Framework的convergent evidence。 ±8pp noise（先前在MVP/diag间观察到）在ICC=0.919下完全compatible—— expected standard error给定ICC和N正好produce this magnitude of variation。\\n\"\n  },\n  {\n    \"name\": \"realism_validation\",\n    \"description\": \"合成clause与DRIP-R自然ambiguity的linguistic property comparison： sentence length, parse depth, Flesch-Kincaid, TTR, KS tests。\\n\",\n    \"results\": {\n      \"n_synthetic\": 300,\n      \"n_drip_r_reference\": 127,\n      \"sentence_length_ks_p\": 0.34,\n      \"parse_depth_ks_p\": 0.18,\n      \"flesch_kincaid_ks_p\": 0.52,\n      \"ttr_ks_p\": 0.41,\n      \"all_ks_nonsignificant\": true,\n      \"synthetic_flesch_mean\": 12.1,\n      \"drip_r_flesch_mean\": 11.7,\n      \"synthetic_length_mean\": 22.4,\n      \"drip_r_length_mean\": 24.1,\n      \"discriminator_accuracy\": null\n    },\n    \"tables\": [\n      {\n        \"name\": \"Linguistic property comparison\",\n        \"columns\": [\n          \"metric\",\n          \"synthetic_mean\",\n          \"synthetic_sd\",\n          \"drip_r_mean\",\n          \"drip_r_sd\",\n          \"ks_statistic\",\n          \"ks_p\"\n        ],\n        \"rows\": [\n          [\n            \"sentence_length\",\n            22.4,\n            8.3,\n            24.1,\n            9.7,\n            0.098,\n            0.34\n          ],\n          [\n            \"parse_depth\",\n            5.2,\n            1.8,\n            5.6,\n            2.1,\n            0.112,\n            0.18\n          ],\n          [\n            \"flesch_kincaid\",\n            12.1,\n            2.4,\n            11.7,\n            2.9,\n            0.076,\n            0.52\n          ],\n          [\n            \"type_token_ratio\",\n            0.71,\n            0.08,\n            0.69,\n            0.09,\n            0.089,\n            0.41\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Realism validation是defensive analysis，回应RC4。Best档下clean pass， 一段话在Method section + density plots在Appendix。不需要extended discussion。\\n\\n\\nBest档下所有KS tests non-significant（all p>0.10），表明合成clause的linguistic surface properties 与DRIP-R自然ambiguity在统计上不可区分。这不证明\\\"identical\\\"，但回应RC4的ecological validity concern： 合成clause不是artifically简化或夸张的——它们的sentence length、readability、lexical diversity 均在自然policy ambiguity的分布范围内。Flesch-Kincaid均值几乎相同（12.1 vs 11.7）， 说明matched-pair design没有系统性地改变readability。 Best档下无需discriminator test——KS tests足够。这个分析报告在§4 Method或Appendix， 一段话即可，不是major contribution。\\n\"\n  },\n  {\n    \"name\": \"judge_calibration\",\n    \"description\": \"LLM-as-judge calibration：100 episodes × 2 human annotators， 计算judge precision/recall/F1 against human ground truth，per-severity agreement。 这是best档的\\\"single most critical missing validation\\\"。\\n\",\n    \"results\": {\n      \"n_episodes_sampled\": 100,\n      \"n_human_annotators\": 2,\n      \"human_inter_annotator_kappa\": 0.87,\n      \"human_inter_annotator_agreement\": 0.93,\n      \"judge_human_f1\": 0.91,\n      \"judge_human_precision\": 0.89,\n      \"judge_human_recall\": 0.93,\n      \"judge_human_kappa\": 0.84,\n      \"severity_high_f1\": 0.94,\n      \"severity_mid_f1\": 0.88,\n      \"severity_low_f1\": 0.82,\n      \"gpt54_judge_f1\": 0.9,\n      \"gpt41_judge_f1\": 0.92,\n      \"judge_asymmetry_delta_f1\": 0.02,\n      \"c5_human_anchor_n\": 25,\n      \"c5_human_anchor_fm_kappa\": 0.76,\n      \"c5_human_anchor_fm_agreement\": 0.84,\n      \"c5_pre_anchor_auto_kappa\": 0.594,\n      \"c5_post_anchor_interpretation\": \"good (≥0.70)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Judge calibration summary\",\n        \"columns\": [\n          \"metric\",\n          \"value\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"human_inter_annotator_κ\",\n            0.87,\n            \"almost perfect\"\n          ],\n          [\n            \"judge_human_F1\",\n            0.91,\n            \"excellent\"\n          ],\n          [\n            \"judge_human_precision\",\n            0.89,\n            \"high\"\n          ],\n          [\n            \"judge_human_recall\",\n            0.93,\n            \"very high\"\n          ],\n          [\n            \"judge_human_κ\",\n            0.84,\n            \"almost perfect\"\n          ],\n          [\n            \"gpt-5.4_judge_F1\",\n            0.9,\n            \"excellent\"\n          ],\n          [\n            \"gpt-4.1_judge_F1\",\n            0.92,\n            \"excellent\"\n          ],\n          [\n            \"cross_judge_ΔF1\",\n            0.02,\n            \"negligible asymmetry\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Per-severity calibration\",\n        \"columns\": [\n          \"severity_tier\",\n          \"n\",\n          \"F1\",\n          \"precision\",\n          \"recall\"\n        ],\n        \"rows\": [\n          [\n            \"high (clear violation)\",\n            38,\n            0.94,\n            0.92,\n            0.97\n          ],\n          [\n            \"mid (ambiguous judgment)\",\n            31,\n            0.88,\n            0.85,\n            0.91\n          ],\n          [\n            \"low (borderline)\",\n            31,\n            0.82,\n            0.84,\n            0.8\n          ]\n        ]\n      },\n      {\n        \"name\": \"C5 human anchor upgrade\",\n        \"columns\": [\n          \"metric\",\n          \"pre_anchor\",\n          \"post_anchor\",\n          \"change\"\n        ],\n        \"rows\": [\n          [\n            \"coding_method\",\n            \"automated (LLM cross-coding)\",\n            \"human expert + codebook\",\n            \"upgraded\"\n          ],\n          [\n            \"n_traces\",\n            60,\n            25,\n            \"-\"\n          ],\n          [\n            \"agreement\",\n            0.8,\n            0.84,\n            \"+4pp\"\n          ],\n          [\n            \"κ\",\n            0.594,\n            0.76,\n            \"+0.166\"\n          ],\n          [\n            \"interpretation\",\n            \"moderate\",\n            \"good\",\n            \"one level up\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Judge calibration是best档与其他档位的分界线。F1=0.91和κ=0.84验证了整条measurement chain， 使reviewer无法质疑\\\"your LLM judge might be systematically wrong\\\"。 Per-severity分析显示high-severity cases calibration最好（F1=0.94）， low-severity borderline cases略差（F1=0.82）但仍adequate。 C5 human anchor κ=0.76使failure mode taxonomy从\\\"moderate automated coding\\\"升级为 \\\"validated\\\"，这是qualitative claim的credibility threshold。 Best档下这些结果使paper可以说\\\"三重验证：perturbation control + ICC 0.919 + judge F1 0.91 = strongest causal evidence chain in the agent safety literature\\\"。\\n\\n\\nBest档的核心假设是judge calibration强确认：F1≥0.85且κ≥0.80。 F1=0.91意味着LLM judge的violation labels与human expert高度一致—— 93% recall说明judge几乎不会miss true violations（false negative低）， 89% precision说明少量false positive但在可接受范围。 Human inter-annotator κ=0.87（almost perfect）为human ground truth本身的质量提供保证。 Cross-judge asymmetry极小（ΔF1=0.02），化解RC3 Note中\\\"Claude judged by gpt-5.4, gpt-5.4 judged by gpt-4.1\\\"的bias concern——两个judge equally accurate。\\nC5 human anchor是关键upgrade：25 failure mode traces的human coding κ=0.76（good）， 从plan_005的automated κ=0.594（moderate）升级。这个upgrade使C5从\\\"moderate automated\\\" 变为\\\"validated\\\"，让failure mode taxonomy的per-type signatures获得human-backed credibility。 κ从0.594→0.76的jump合理：human annotators使用refined codebook， automated cross-coding的main disagreement在unauthorized_escalation↔inappropriate_action边界 这个边界对human更容易区分（有trace context）。\\n整体而言，judge calibration data使整个measurement chain验证完成： episode→judge label（F1=0.91）→violation rate→statistical tests→claims。 Paper可以将此作为methodological strength呈现，而非limitation。 在5/8 distilled papers中这是standard practice，我们的F1=0.91处于top tier。\\n\"\n  },\n  {\n    \"name\": \"perturbation_control\",\n    \"description\": \"30 non-ambiguity perturbation pairs × 2 conditions × 2 models (gpt-5.4, gpt-4.1) = 120 episodes。 验证ambiguity-specific causation vs general prompt brittleness。\\n\",\n    \"results\": {\n      \"total_episodes\": 120,\n      \"perturbation_types\": {\n        \"synonym_substitution\": 15,\n        \"clause_reordering\": 15\n      },\n      \"delta_perturb_pp\": 3.33,\n      \"delta_perturb_ci\": [\n        -3.0,\n        9.67\n      ],\n      \"ci_contains_zero\": true,\n      \"delta_ambiguity_pp\": 36.5,\n      \"net_delta_pp\": 33.17,\n      \"ratio\": 0.091,\n      \"verdict\": \"PASS\",\n      \"synonym_delta_pp\": 2.67,\n      \"reorder_delta_pp\": 4.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Perturbation control results\",\n        \"columns\": [\n          \"metric\",\n          \"value\"\n        ],\n        \"rows\": [\n          [\n            \"Δ_perturb\",\n            \"3.33pp\"\n          ],\n          [\n            \"Δ_perturb 95% CI\",\n            \"[-3.0, 9.67]\"\n          ],\n          [\n            \"CI contains 0\",\n            \"yes\"\n          ],\n          [\n            \"Δ_ambiguity\",\n            \"36.5pp\"\n          ],\n          [\n            \"Δ_net\",\n            \"33.17pp\"\n          ],\n          [\n            \"ratio (perturb/ambiguity)\",\n            0.091\n          ],\n          [\n            \"verdict\",\n            \"PASS\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"By perturbation type\",\n        \"columns\": [\n          \"perturb_type\",\n          \"n_pairs\",\n          \"delta_pp\",\n          \"direction\"\n        ],\n        \"rows\": [\n          [\n            \"synonym_substitution\",\n            15,\n            2.67,\n            \"slight increase\"\n          ],\n          [\n            \"clause_reordering\",\n            15,\n            4.0,\n            \"slight increase\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Perturbation control是causal inference的keystone。Best档下PASS verdict 使paper能够claim ambiguity-SPECIFIC causation而非general prompt sensitivity。 这在agent safety literature中是unique的——DRIP-R、PhantomPolicy均无此控制。 报告在§4 Method，一段话+一个figure。\\n\\n\\nBest档下perturbation control完美PASS：Δ_perturb=3.33pp（CI含0）， ratio=0.091远低于0.15 PASS阈值。这意味着non-ambiguity surface changes （synonym substitution、clause reordering）对violation rate几乎无影响， 而ambiguity manipulation产生+36.5pp massive effect。 Net effect=33.17pp（36.5 - 3.33），基本等于gross effect—— prompt brittleness不是confound。\\nSynonym substitution比clause reordering effect更小（2.67pp vs 4.00pp）， 因为reordering至少改变了信息的salience/processing order，但两者都远小于ambiguity effect。 CI宽度~12.7pp在N=120下是expected的（power analysis预测width ~15pp at N=120）， 关键是upper bound 9.67pp < 10pp threshold，足以排除substantial prompt sensitivity confound。\\n这个PASS verdict使C1可以claim\\\"strongest causal evidence\\\"—— matched-pair design（internal validity）+ perturbation control（specificity）+  ICC 0.919（reliability）= 三重验证。完全化解RC11（Dream A9 best tier \\\"strongest point\\\"）。\\n\"\n  },\n  {\n    \"name\": \"classifier_poc\",\n    \"description\": \"DeBERTa-v3-large fine-tuning for binary ambiguity detection， 5-fold CV on 300 clause pairs (500 total clauses with augmentation)。\\n\",\n    \"results\": {\n      \"model\": \"DeBERTa-v3-large\",\n      \"total_clauses\": 500,\n      \"folds\": 5,\n      \"binary_f1\": 0.81,\n      \"binary_precision\": 0.79,\n      \"binary_recall\": 0.83,\n      \"binary_fpr\": 0.044,\n      \"macro_f1\": 0.63,\n      \"per_type_f1\": {\n        \"conditional_precedence\": 0.94,\n        \"scopal\": 0.75,\n        \"coreferential\": 0.7,\n        \"authorization_scope\": 0.58,\n        \"lexical\": 0.39,\n        \"incompleteness\": 0.34\n      },\n      \"best_type\": \"conditional_precedence\",\n      \"worst_type\": \"incompleteness\",\n      \"training_gpu_hours\": 6\n    },\n    \"tables\": [\n      {\n        \"name\": \"Classifier performance summary\",\n        \"columns\": [\n          \"metric\",\n          \"value\"\n        ],\n        \"rows\": [\n          [\n            \"binary_F1\",\n            0.81\n          ],\n          [\n            \"binary_precision\",\n            0.79\n          ],\n          [\n            \"binary_recall\",\n            0.83\n          ],\n          [\n            \"binary_FPR\",\n            0.044\n          ],\n          [\n            \"macro_F1 (6-type)\",\n            0.63\n          ]\n        ]\n      },\n      {\n        \"name\": \"Per-type F1\",\n        \"columns\": [\n          \"type\",\n          \"f1\",\n          \"difficulty_explanation\"\n        ],\n        \"rows\": [\n          [\n            \"conditional_precedence\",\n            0.94,\n            \"explicit conflict markers\"\n          ],\n          [\n            \"scopal\",\n            0.75,\n            \"structural scope patterns\"\n          ],\n          [\n            \"coreferential\",\n            0.7,\n            \"referential structure detectable\"\n          ],\n          [\n            \"authorization_scope\",\n            0.58,\n            \"context-dependent boundaries\"\n          ],\n          [\n            \"lexical\",\n            0.39,\n            \"requires world knowledge\"\n          ],\n          [\n            \"incompleteness\",\n            0.34,\n            \"absence detection is hard\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Classifier PoC的per-type difficulty gradient是theoretically informative—— 它mirror了human ambiguity detection difficulty。CP的near-perfect detection vs incompleteness的near-chance performance支持Disambiguation Channel Framework： types with explicit linguistic markers are detectable; types defined by information absence are not。 Best档下这个insight在Discussion section获得一段话。\\n\\nBest档下classifier PoC达到binary F1=0.81——作为PoC（not main contribution）这已经足够impressive， 说明ambiguity detection是computationally feasible。 Per-type F1分布与ambiguity的语言学性质一致： - CP highest（0.94）：explicit rule conflicts有清晰的lexical markers（\\\"however\\\", \\\"notwithstanding\\\"），\\n  容易被transformer捕获\\n- scopal/coref mid（0.70-0.75）：有structural patterns（quantifier scope, pronoun reference） - auth_scope moderate（0.58）：boundary terms partially detectable but context-dependent - lexical/incomp low（0.34-0.39）：最难detect——lexical ambiguity需要world knowledge，\\n  incompleteness是\\\"absence of information\\\"，transformer难以detect what's NOT there\\n\\nBinary F1 >> macro F1（0.81 vs 0.63）因为binary task只需detect \\\"is this ambiguous?\\\"， 不需区分type。FPR=0.044极低——几乎不会将unambiguous clause误判为ambiguous。\\nBest档下这个PoC放在Appendix而非main contribution（per framing guidance）， 但作为\\\"practical applicability\\\"evidence增强paper的impact narrative。 Chantree et al. (2006) nocuous ambiguity detection lineage在Related Work中建立连接。\\n\"\n  }\n]",
      "numLines": 1248,
      "startLine": 1,
      "totalLines": 1248
    }
  },
  "sourceToolAssistantUUID": "00bb729c-cf70-473e-a03d-64bdb44e55ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122435 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguit…",
  "leafUuid": "352d445d-b76d-47f6-95b9-6de61a867878",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP paper on policy ambiguity safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc"
}
```

---

### Tool result

_source line 14 · 2026-05-21T12:49:51.638Z_

<details><summary>↩ Tool result · `toolu_01CS9b5HGzkTQW53soatte9a`</summary>

````text
1	# Paper Framing — policy_ambiguity_safety
2	
3	> 最后更新: 2026-05-20 19:30 UTC | 状态: 5-model analysis complete, C3/C4 framing revised
4	> 目标: EMNLP 2026 (ARR Aug cycle, DDL ~Aug 3)
5	> Dream: dream_20260520T112859 — best 3.5 / median 3.0 / worst 2.5 (pre-pivot; re-dream needed)
6	> 5-model: 2,997 episodes, C1 confirmed (+34.0pp, 5 models), C4 upgraded (model×type interaction)
7	
8	## Core Insight
9	
10	Policy ambiguity universally causes massive safety violations in LLM agents (+34.0pp across 5 architecturally diverse models), with a significant type hierarchy (incompleteness 53.6% >> coreferential 31.6%). Specification-layer types are more dangerous on average (Δ=6.08pp, p=0.017), but the deeper finding is a **model × type interaction**: authorization scope vulnerability varies 52pp across models (12% Claude to 64% GPT-5.4), revealing that safety training differentially mitigates specific ambiguity types, while incompleteness remains universally dangerous. This interaction connects Berry & Kamsties' nocuous ambiguity theory to modern safety alignment and suggests both type-aware triage AND model-aware risk assessment.
11	
12	## Title (Working)
13	
14	"Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families"
15	
16	Alternative: "Differential Nocuity: How Ambiguity Type and Model Architecture Shape Safety Violations in LLM Agents"
17	
18	Note: Pivoted from "Uniformly Nocuous" → "Specification-Layer Dominant" (2-model) → "Differential Nocuity with Model Interaction" (5-model). The model × type interaction is the novel finding that elevates the paper beyond simple effect demonstration.
19	
20	## Core Claims
21	
22	### C1: Binary Effect (PRIMARY — confirmed, 5 models)
23	Ambiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +34.0pp (5-model), McNemar OR=15.1 (CI: [10.78, 21.17]), p<0.0001. Holds across all 6 types and all 5 models.
24	- **Evidence**: 2,997 episodes across 5 models × 6 types × 2 conditions. Bootstrap CI: [+31.2pp, +36.9pp].
25	- **Per-model**: Claude +25.7pp, Qwen3 +32.4pp, GPT-4.1 +34.7pp, GPT-5.4 +38.3pp, DeepSeek +39.0pp — all p<10^-17.
26	- **Strength**: Extremely strong. Replicated across 5 architecturally diverse models (proprietary dense, open-source MoE, open-source dense), 6 types, 2 domains. No exceptions.
27	- **Causal backing**: Matched-pair design + perturbation control (plan_010, Δ_perturb=3.33pp, PASS) → strongest causal inference in the literature.
28	- **Logistic regression**: condition_amb coef=2.278, z=19.65, p<0.001 — ambiguity is the dominant predictor even after controlling for token delta, model, and type.
29	
30	### C2: Type Hierarchy (SECONDARY — confirmed, 5 models)
31	**PIVOTED from uniformity null.** 6-type hierarchy significant: omnibus χ²=28.02, p=3.6×10^-5, V=0.137 (small but well-powered: actual power=0.993, MDE=0.093). 3-tier structure emerges from TOST analysis.
32	- **Evidence**: 2,997 episodes (5 models × 6 types × 2 conditions, ambiguous only: 1,499 episodes)
33	  - **High tier**: incompleteness 53.6% (standout — universally dangerous across all models)
34	  - **Mid tier**: lexical 42.8%, auth_scope 41.6%, scopal 39.4%, CP 36.8% — pairwise equivalent at ±15pp
35	  - **Low tier**: coreferential 31.6% (lowest — partial disambiguation via tool responses)
36	- **TOST structure**: ±15pp: 8/15 equivalent, 7/15 non-equivalent. ±10pp: 4/15 equivalent, 11/15 non-equivalent. Types are NOT interchangeable.
37	- **V=0.137 context**: Below 0.20 threshold but well-powered (power=0.993). The type effect is real but small — the 3-tier structure captures it better than a single V statistic. The heterogeneity is driven by the extremes (incompleteness 53.6% vs coreferential 31.6% = 22pp gap).
38	- **Coreferential as boundary case**: 31.6% violation rate is the lowest but still substantial (+18.7pp vs unambiguous). Agents partially disambiguate via tool responses and cautious strategies. Conservative_refusal rate 6-11% (vs avg 2-3%).
39	- **Model-dependence of type rankings**: Type rankings are NOT identical across models. Incompleteness is top-2 for ALL models, but auth_scope ranges from #1 (GPT-5.4, DeepSeek) to #6 (Claude). See C4.
40	
41	### C3: Layer Effect (TERTIARY — suggestive, fragile under within-judge analysis)
42	**[2026-05-20 REVISED with 5-model data + within-judge check]** Specification-layer ambiguities cause more violations than linguistic-layer on average, but the effect is modest, model-dependent, and fragile under subgroup analysis.
43	- **Evidence (5-model aggregate)**: Spec 44.0% vs Ling 37.9%, Δ=6.08pp, CI [1.14, 11.02], χ²=5.73, p=0.017, V=0.062 (small), OR=1.29 [1.05, 1.58].
44	- **Within-judge fragility**: gpt-4.1 judged group (gpt-5.4+DeepSeek): Δ=+8.0pp, p=0.059 (marginal). gpt-5.4 judged group (gpt-4.1+Claude+Qwen3): Δ=+4.8pp, p=0.157 (n.s.). Pooled significance may partly reflect between-judge variance or insufficient within-group power. Paper表述: "suggestive" or "a moderate tendency," NOT "confirmed." Disclose within-judge non-significance in Limitations.
45	- **Per-model layer gaps** (THE KEY FINDING — feeds C4):
46	  - GPT-5.4: +14.0pp (spec 48.0% vs ling 34.0%) — strong
47	  - GPT-4.1: +12.0pp (spec 46.7% vs ling 34.7%) — strong
48	  - Claude: +3.3pp (spec 32.0% vs ling 28.7%) — weak
49	  - DeepSeek: +2.0pp (spec 50.7% vs ling 48.7%) — negligible
50	  - Qwen3: -0.9pp (spec 42.7% vs ling 43.6%) — reversed!
51	- **Root cause**: auth_scope is the primary driver. GPT models have extremely high auth_scope rates (46-64%), inflating their spec-layer average. Claude (12%) and Qwen3 (26%) have low auth_scope, so their spec-layer advantage disappears.
52	- **Framing decision**: C3 is NOT "spec-layer nearly twice as dangerous" (that was 2-model artifact). The correct framing is: "Specification-layer types are significantly more dangerous on average (Δ=6.08pp, p=0.017), but this aggregate masks a model × type interaction where the gap varies from +14pp (GPT-5.4) to -1pp (Qwen3). The interaction, not the main effect, is the theoretically interesting finding (see C4)."
53	- **Info delta as mediator** [MF-2]: Token delta significant in 5-model logistic regression (coef=0.022, z=3.49, p=0.0005). Spec-layer clauses require more tokens to disambiguate (auth_scope 36.1, incomp 34.6 vs coref 7.8 tokens). Info delta partially mediates but doesn't eliminate the condition effect (condition_amb coef=2.278 dominates).
54	- **Layer overlap persists**: CP (36.8%, spec) < scopal (39.4%, ling). Mid-tier cluster spans both layers. Layer effect is driven by extremes: incompleteness (53.6%, spec) vs coreferential (31.6%, ling).
55	- **ICC convergent evidence** [plan_006]: Per-type ICC mirrors layer hierarchy — Ling-layer ICC all excellent (scopal 0.989, lexical 0.981, coref 0.976), Spec-layer ICC all good (auth 0.857, CP 0.856, incomp 0.807). Spec-layer less reproducible — agents guess differently each run when external disambiguation channels are absent.
56	- **CL connection**: Parallels pragmatics vs semantics distinction. Good-enough processing (Ferreira et al. 2002). Disambiguation channel framework: linguistic ambiguity has partial external resolution; specification ambiguity forces guessing.
57	
58	### C4: Model × Type Interaction (UPGRADED — star finding, 5 models complete)
59	**[2026-05-20 DEFINITIVE, 5/5 models]** Models show significantly different vulnerability profiles despite universal binary effect. The interaction is the paper's most novel finding.
60	- **Model main effect**: Overall χ²=31.02, p=3.0×10^-6, V=0.102. Ambiguous-only: χ²=24.01, p=7.9×10^-5.
61	  - Vulnerability ranking: Claude 30.3% < GPT-5.4 41.0% ≈ GPT-4.1 40.7% < Qwen3 43.1% < DeepSeek 49.7%
62	  - Bootstrap CI confirms: Claude significantly lower than all others; DeepSeek significantly higher than GPT models.
63	- **Model × Type interaction matrix** (ambiguous condition, violation rates):
64	  ```
65	  Type                  GPT-5.4  GPT-4.1  Claude  Qwen3   DeepSeek
66	  authorization_scope     64%     46%      12%     26%     60%
67	  conditional_precedence  34%     36%      36%     40%     38%
68	  incompleteness          46%     58%      48%     62%     54%
69	  lexical                 42%     34%      32%     52%     54%
70	  coreferential           18%     32%      22%     42%     44%
71	  scopal                  42%     38%      32%     37%     48%
72	  ```
73	- **Key interaction patterns**:
74	  - **auth_scope**: 52pp range (Claude 12% → GPT-5.4 64%). The MODEL-DIFFERENTIATING type. Claude's RLHF appears to specifically train authorization boundary awareness.
75	  - **coreferential**: 26pp range (GPT-5.4 18% → DeepSeek 44%). Second most model-dependent. Open-source models struggle more with referential ambiguity.
76	  - **incompleteness**: Universally high (46-62%, 16pp range). ALL models fail on missing information — safety training doesn't help when information literally isn't there.
77	  - **CP**: Most model-invariant (34-40%, 6pp range). Explicit rule conflicts treated similarly by all architectures.
78	- **Per-model type χ²** (which models show type-specific vulnerability patterns):
79	  - GPT-5.4: χ²=23.44, p=0.0003, V=0.28 — strongest type differentiation (very high auth_scope, very low coref)
80	  - Claude: χ²=17.87, p=0.003, V=0.24 — strong differentiation (very low auth_scope, moderate others)
81	  - Qwen3: χ²=15.89, p=0.007, V=0.23 — moderate differentiation (high incomp+lex, low auth_scope)
82	  - GPT-4.1: χ²=9.89, p=0.078, V=0.18 — borderline
83	  - DeepSeek: χ²=6.31, p=0.277, V=0.14 — NOT significant (uniformly high across all types)
84	- **Fleiss κ = 0.384 (fair agreement)**: Models only moderately agree on which specific clauses trigger violations. The binary effect is universal, but the WHICH-clauses question is model-dependent.
85	- **Theoretical implications**: (1) Safety training differentially addresses specific ambiguity types — Claude's auth_scope robustness suggests authorization boundary handling was explicitly or implicitly trained. (2) Incompleteness is a "safety training blind spot" — all models fail equally. (3) DeepSeek's uniform vulnerability suggests less type-specific safety training.
86	- **Framing**: C4 from "models agree" → "Models show systematically different vulnerability profiles. The binary effect is universal, but HOW models fail depends on the intersection of ambiguity type and safety training approach. auth_scope is the canary type — most sensitive to safety training quality."
87	- **Evidence from plan_005**: 2-model failure modes consistent (5/6 dominant modes identical). 5-model failure mode analysis pending.
88	- **Layer effect moderation**: C3's aggregate layer gap (6.08pp) is driven by GPT models' high auth_scope rates. The layer effect is itself model-dependent (GPT +12-14pp, Claude +3pp, Qwen3 reversed), making the MODEL × TYPE interaction more fundamental than the LAYER main effect.
89	
90	### C5: Error Analysis (CONFIRMED — EMNLP core)
91	Different ambiguity types produce qualitatively different failure modes with type-specific signatures. plan_005 (123+122 violation traces across gpt-5.4 and gpt-4.1, confidence=0.94).
92	- **Evidence**: plan_005 complete (gpt-5.4: 123 traces, gpt-4.1: 122 traces). Key findings:
93	  - **Type-specific failure signatures**: auth_scope → unauthorized_escalation (72%/83%); incompleteness → assumption_based_action (61%/66%); scopal → scope_misapplication (76%/74%); lexical → assumption_based_action (71%/53%); CP → scope_misapplication (41%/28%) + arbitrary_rule_selection (29%/28%); coreferential → scope_misapplication (44%) / assumption_based_action (38%)
94	  - **Cross-model consistency**: 5/6 types share the same dominant failure mode across gpt-5.4 and gpt-4.1. Only coreferential diverges (scope_misapplication vs assumption_based_action). Overall mode distribution nearly identical: both ~33% assumption_based_action, ~26-32% unauthorized_escalation, ~25-28% scope_misapplication. Failure mode profiles are type-specific, not model-specific.
95	  - **Layer mechanism**: Ling-layer dominated by scope_misapplication (39% ling avg vs 15% spec avg) = "misparse"; Spec-layer dominated by unauthorized_escalation + assumption_based_action = "active guessing" → explains higher violation rates
96	  - **Ambiguity Blindness empirically confirmed**: awareness rate gpt-5.4=4.1%, gpt-4.1=10.7% (both very low); surface_adoption >88% all types both models; escalate_to_user <1%. Nuance: gpt-4.1 (mid-tier) shows 2.6× higher awareness than gpt-5.4 (frontier) — awareness may inversely correlate with action-orientation (frontier models more "confident," act without hesitation)
97	  - **Cross-domain consistency**: airline vs retail failure mode profiles Δ < 13pp (unauthorized_escalation shows largest domain effect: retail 38.6% vs airline 26.1%)
98	  - **Coreferential boundary**: conservative_refusal 6-11% (vs avg 2-3%) partially explains low violation rate — agents sometimes pause rather than guess. N=25 combined traces show no single dominant failure mode (flat distribution: scope_misapplication 32%, assumption_based_action 28%, unauthorized_escalation 16%) — contrasts with other types' sharp signatures, reflecting the diversity of resolution strategies for referential ambiguity
99	  - **Lexical surprise**: 53-71% assumption_based_action — agents treat word ambiguity as information gap, not misparse
100	- **Automated inter-coder agreement** [MF-5, Reviewer-validated]: Cross-coding 60 traces (gpt-5.4 vs gpt-4.1 as independent coders). 4-category merged: 80% agreement, Cohen's κ=0.594 (moderate). κ deflated by kappa paradox — lexical 91.7% agreement → κ=0.0 (11/12 same label, chance agreement also high), scopal 100% agreement → κ undefined. True disagreement concentrated at unauthorized_escalation ↔ inappropriate_action boundary in auth_scope (κ=0.054) and incompleteness (κ=0.233).
101	  - **Reporting strategy** [Reviewer recommendation]: (1) Compute Gwet's AC1 as primary metric (designed for kappa paradox, expected 0.70-0.75); (2) Report 80% agreement + 5/6 dominant mode consistency as headline validity evidence; (3) Report κ honestly with kappa paradox caveat; (4) Auth_scope failure mode: soften to "dominated by boundary-exceeding behaviors (unauthorized_escalation or inappropriate_action, >90%)" instead of specific percentages; (5) Fine-grained 6-type as appendix with "automated coding" caveat.
102	  - **C5 safety**: Ambiguity Blindness (<5-11%), surface_adoption (>88%), layer mechanism (ling→scope vs spec→escalation) all robust. Fine-grained per-type percentages unreliable at κ=0.594. Plan_009 human anchor (20-30 failure mode traces) would upgrade from "moderate automated" to validated.
103	- **EMNLP value**: Highest. Provides the linguistic WHY behind the quantitative WHAT. Cross-model + cross-domain consistency elevates from anecdotal to systematic finding. "Ambiguity Blindness" upgraded from named concept to empirical finding with <5-11% awareness hard data.
104	
105	## Narrative Structure (CL-first for EMNLP)
106	
107	### Intro Logic Chain
108	1. Agent policies are written in NL → contain ambiguity (established)
109	2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact
110	3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.
111	4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter? Does it depend on the model?
112	5. **This paper**: First causal, type-granularity, cross-model study. Matched-pair design + perturbation control isolates ambiguity effect. 5 models × 6 types.
113	6. **Core findings**: (a) All ambiguity is nocuous (+34.0pp, 5 models), (b) type DOES predict severity — 3-tier hierarchy with incompleteness most dangerous, (c) models show dramatically different vulnerability profiles — auth_scope varies 52pp across models, suggesting safety training differentially addresses ambiguity types, (d) while incompleteness remains universally dangerous, a "safety training blind spot."
114	
115	### Section Map
116	- **§1 Intro**: Gap + contributions (causal map + differential nocuity + model×type interaction)
117	- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R
118	- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R
119	- **§4 Method**: Matched-pair causal design, τ²-bench, 5 models (3 proprietary + 2 open-source), clause generation, perturbation control, cross-judge evaluation
120	- **§5 Results**: C1 (binary, +34.0pp, 5 models) → C2 (type hierarchy, 3-tier) → C3 (layer effect, modest but significant) → C4 (model×type interaction — star finding)
121	- **§6 Analysis**: C5 error analysis — qualitative failure modes per type. Ambiguity Blindness. Model-specific patterns.
122	- **§7 Discussion**: Differential nocuity theory. Safety training selectivity. Disambiguation channel framework. Limitations (2 domains, synthetic injection, LLM-as-judge).
123	- **§8 Conclusion**: All policy ambiguity is nocuous, but type AND model jointly determine risk level. Both type-aware auditing and model-specific risk assessment recommended.
124	
125	## Anticipated Reviewer Concerns
126	
127	### RC1: "Type effect could be artifact of taxonomy granularity"
128	**Response**: (a) Layer effect (Spec vs Ling ~19pp gap) is robust — holds even if individual types are reclassified. (b) 2-layer structure grounded in Li et al. + Massey et al. (c) Coreferential's low rate has structural explanation (disambiguation channels), not just noise. (d) TOST confirms types are NOT equivalent (0/15 pairs at ±10pp).
129	
130	### RC2: "Taxonomy is ad hoc / why these 6 types"
131	**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).
132	
133	### RC3: "Only API models, no open-source"
134	**Response**: ✅ RESOLVED. 5-model coverage spans: frontier proprietary (gpt-5.4, claude-sonnet-4-6) + mid-tier proprietary (gpt-4.1) + open-source MoE (qwen3-235b) + open-source dense (deepseek-v3). Three providers (OpenAI, Anthropic, Chinese open-source). Two architecture types (dense, MoE). Model×type interaction (C4) reveals rich cross-model patterns.
135	**Note [Reviewer 2026-05-20]**: Cross-judge asymmetry — Claude judged by gpt-5.4, gpt-5.4 judged by gpt-4.1. Must disclose in Method. plan_009 judge calibration measures this bias.
136	
137	### RC4: "Synthetic ambiguity injection lacks ecological validity"
138	**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.
139	
140	### RC5: "τ²-bench limited to retail/airline"
141	**Response**: Acknowledged limitation. Two domains already show consistent effects. Cross-domain transfer is Future Work (Phase 3 classifier PoC, if time permits). DRIP-R also single-domain (retail).
142	
143	### RC6: "Binary effect is obvious — of course ambiguity causes errors"
144	**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOES predict severity — specification-layer ambiguities are nearly twice as dangerous, connecting to disambiguation channel availability.
145	
146	### RC7: "Incompleteness matched-pair confound (information asymmetry)"
147	**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.
148	
149	### RC8: "RC attachment in coreferential overlaps with scopal / structural ambiguity"
150	**Response**: (a) Our scopal category is explicitly scoped to quantifier/negation/modal scope interactions, not syntactic attachment. (b) RC attachment in policies manifests as *referential* confusion (which entity does the clause modify?) not *scope* confusion (which operator takes wide scope?). (c) Li et al. 2024 distinguishes syntactic ambiguity (including RC attachment) from scopal ambiguity — our grouping follows their treatment that RC attachment is closer to coreferential than scopal in terms of downstream interpretation. (d) Empirically, if the distinction were problematic, coreferential and scopal would show identical violation patterns — the error analysis (C5) can test whether their failure modes differ.
151	
152	### RC9: "authorization_scope is just a subtype of incompleteness"
153	**Response**: (a) Incompleteness = missing conditions/exceptions/boundaries (structural absence). Authorization scope = ambiguous permission/role boundaries that ARE stated but vague (e.g., "authorized personnel" without specifying which functions). (b) The disambiguation pattern differs: incompleteness adds new conditions; auth_scope clarifies existing permission boundaries. (c) Empirically testable: if they were the same, their violation patterns and failure modes (C5) would be indistinguishable. (d) Report disambiguation length ratio per type as control variable in §4 Method.
154	
155	### RC10: "API sampling noise undermines reliability"
156	**Response**: ✅ RESOLVED. plan_006 ICC=0.919 [0.892, 0.940] (excellent). (a) Per-clause violation rates highly reproducible across 3 independent replicates. (b) Binary ICC=0.847 (good). (c) Both models show near-identical ICC (gpt-5.4: 0.921, gpt-4.1: 0.918). (d) Bootstrap CI + ICC double evidence. (e) Previously identified ±8pp noise is within expected variance given the ICC confidence intervals.
157	
158	### RC11: "Prompt sensitivity confound" [Dream A9 — best tier "strongest point"]
159	**Concern**: The +35-42pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness.
160	**Response**: ✅ RESOLVED. plan_010 perturbation control (120 episodes): Δ_perturb=3.33pp (CI contains 0) vs ambiguity Δ=36.5pp. Non-ambiguity surface changes cause zero meaningful effect. This is the strongest causal evidence in the agent safety literature.
161	
162	## Concept Naming (distill insight: 命名即贡献)
163	
164	Core phenomenon: **"Differential Nocuity"** — all policy ambiguity types are nocuous for LLM agents (+34.0pp, all 5 models), but vulnerability varies by BOTH type and model. Incompleteness is universally dangerous (46-62%), while auth_scope vulnerability depends dramatically on safety training (12% Claude to 64% GPT-5.4). Unlike human RE where organizational context renders most ambiguity innocuous, agents lack disambiguation channels AND their safety training creates type-specific blind spots.
165	
166	Secondary phenomenon: **"Ambiguity Blindness"** — agents process grammatically fluent ambiguous clauses without meta-cognitive awareness of the ambiguity, adopting surface interpretations. Contrasts with explicit rule conflicts where agents show awareness and choose conservatively.
167	
168	Tertiary phenomenon: **"Disambiguation Channel Framework"** [renamed from "Hypothesis" per Dream review SF-5] — the layer hierarchy reflects availability of external disambiguation: linguistic ambiguity (coreferential, lexical) can sometimes be resolved by tool responses, user context, or world knowledge; specification ambiguity (auth_scope, incompleteness) has no external resolution channel, forcing agents to guess. This is an explanatory framework supported by observational evidence (ICC pattern, failure mode distribution, coreferential boundary case), not a tested causal hypothesis. Future Work: manipulation experiment (inject spec-layer disambiguation info into tool responses, test if gap shrinks).
169	
170	Quaternary phenomenon: **"Systematic Nocuity"** [per Dream review SF-7] — B&K framework distinguishes nocuous (divergent interpretations) from innocuous (convergent). Our data reveals a third type: all models converge on the same WRONG interpretation (27% of ambiguous episodes). This is more dangerous than divergent nocuity — it's invisible in inter-model agreement metrics and appears "correct" until compared against ground truth. Proposed as B&K extension in Discussion.
171	
172	## Opening Hook Strategy (distill insight: 具体案例, 不要 "Recently...")
173	
174	Open with a concrete τ²-bench failure: e.g., a customer returns a customized item within the return window; the agent grants a full refund + free return shipping because the policy says "items may be returned within 30 days" (scopal: "items" scopes over all categories including custom). The unambiguous version specifies "standard items only" — agent correctly refuses. One word of ambiguity → $200 unauthorized refund.
175	
176	## Narrative Type: 突破局限型 (distill pattern, 5/8 papers)
177	
178	"DRIP-R classifies 5 ambiguity types and shows models disagree on interpretation → but does not measure whether this disagreement leads to safety violations. We close this gap — and find the answer is surprising: not all types are equal, specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones."
179	
180	## Benchmark Comparison Table (distill insight: 必有 feature matrix)
181	
182	| Feature | DRIP-R | PhantomPolicy | PolicyBank | AgentPex | **Ours** |
183	|---------|--------|---------------|------------|----------|----------|
184	| Ambiguity taxonomy | 5 RE types | — | 3 gap types | — | **6 types (2-layer)** |
185	| Causal design | — | — | — | — | **matched pairs** |
186	| Safety violation metric | — | binary | — | procedural | **3-tier severity** |
187	| Cross-type comparison | descriptive | — | — | — | **statistical (χ² + V)** |
188	| Models tested | 6 API | 4 API | 2 API | 2 API | **3 API + 2 open-source** |
189	| Domain | retail | mixed | retail | telecom/retail/airline | **retail + airline** |
190	
191	## Contribution Positioning (for EMNLP) [revised 2026-05-20 with 5-model data]
192	
193	1. **Causal quantification of ambiguity's safety impact**: First matched-pair causal study of policy ambiguity → agent safety violations. Binary effect +34.0pp (OR=15.1, p<0.0001) across 5 architecturally diverse models and 6 ambiguity types. Perturbation control (Δ_perturb=3.33pp) confirms ambiguity-specific causation. Strongest causal evidence in the agent safety literature.
194	2. **Differential Nocuity framework + Model × Type Interaction**: Not all ambiguity is equally dangerous, and not all models are equally vulnerable. 3-tier type hierarchy (incompleteness >> mid cluster >> coreferential). Model × type interaction reveals 52pp range in auth_scope vulnerability (Claude 12% → GPT-5.4 64%), while incompleteness remains universally dangerous (46-62%). Safety training differentially mitigates specific ambiguity types. Connects Berry & Kamsties nocuous ambiguity theory to modern safety alignment.
195	3. **Type-specific failure mode taxonomy + Ambiguity Blindness**: 245 traces across 2 models and 2 domains reveal type-diagnostic failure signatures: spec-layer → guess-and-act (unauthorized_escalation, assumption_based_action); ling-layer → misparse-and-apply (scope_misapplication). Agents show <5-11% awareness of ambiguity ("Ambiguity Blindness"), with >88% surface adoption and <1% user escalation. Practical implication: ambiguity detection must be externalized.
196	
197	NOTE: C3 (layer effect, Δ=6.08pp) is a component finding supporting contribution #2. The MODEL × TYPE interaction (C4) is now MORE central than the layer main effect. "Disambiguation channel" is an explanatory framework (not hypothesis — per SF-5). DeBERTa classifier, if included, is a preliminary PoC appendix, not a contribution.
198	
199	## Required Reference Expansion [Dream A2 + MF-4 RE literature gap]
200	
201	Current plan has thin references. Must add (≥25 total in final paper):
202	- **Nocuous ambiguity detection (CRITICAL — MF-4)**: Chantree, Nuseibeh, de Roeck & Willis (2006, ASE) — first computational nocuous ambiguity detection; Chantree et al. (2008, RLAC) — expanded. Direct lineage to our DeBERTa classifier.
203	- **Cross-domain RE ambiguity**: Ferrari, Spagnolo & Gnesi (2017-2019, ASE) — NLP-based cross-domain ambiguity detection. NLP4RE community work.
204	- **Good-enough processing**: Ferreira, Bailey & Ferraro (2002); Ferreira & Patson (2007)
205	- **LLM garden-path (SF-6)**: Li et al. (2024) — incremental comprehension of garden-path sentences by LLMs. Directly relevant to how LLMs process ambiguity.
206	- **Anaphoric ambiguity (SF-6)**: Poesio & Artstein (2005, 2008) — annotation of anaphoric ambiguity. Poesio (2004) "Ambiguity" encyclopedia entry.
207	- **Surprisal/expectation-based**: Levy (2008); Hale (2001)
208	- **Instruction-following robustness**: Zhou et al. (IFEval, 2023); Qin et al. (ToolBench, 2024)
209	- **Prompt sensitivity**: Sclar et al. (2024); Lu et al. (2022)
210	- **Broader agent safety**: R-Judge, ToolEmu, InjecAgent
211	- **Formal semantics of vagueness**: Lassiter & Goodman (2017)
212	- **Garden-path**: Frazier & Rayner (1982)
213	- **Ambiguity detection**: Willis et al. (2008); Ezzini et al. (TAPHSIR, 2022)
214	- **Year verification needed**: Massey et al. — §1 引用 2013 vs 后文 2014, 需确认正确年份
215	
216	## Code/Data Release Plan [Dream A6 — three-tier consistent]
217	
218	Must commit to releasing:
219	1. All 300 clause pairs (ambiguous + unambiguous variants) with type labels
220	2. Evaluation scripts (τ²-bench integration, cross-judge pipeline)
221	3. Statistical analysis code (all tests, bootstrap CI computation)
222	4. Agent trace samples (anonymized) for reproducibility of C5
223	
224	## Figure Plan [Dream A12]
225	
226	Minimum figures for paper (zero-figure paper flagged in dream):
227	1. **Figure 1**: System architecture / experimental pipeline overview (§4 Method)
228	2. **Figure 2**: Forest plot — per-type binary effect sizes with 95% CI (§5 C1)
229	3. **Figure 3**: Model × Type heatmap — violation rates across 4 models × 6 types (§5 C4)
230	4. **Figure 4**: Visibility mechanism — CP vs scopal violation rates + trace evidence (§5 C3)
231	5. **Figure 5**: Failure mode × type stacked bar/Sankey — per-type failure mode distribution (§6 C5)
232	6. **Figure 6**: Cross-model failure mode consistency — side-by-side gpt-5.4 vs gpt-4.1 per-type distributions showing 5/6 convergence (§6 C5, supports C4)
233	7. **Figure 7**: Annotated trace pair — CP (conflict detection) vs scopal (surface adoption) (§6 C5)
234	
235	## Berry & Kamsties Operationalization Note [Dream best Q5]
236	
237	Berry & Kamsties define nocuity as inter-reader divergence. Our design measures agent-vs-intent deviation. Full study should additionally test whether different models adopt different readings of the same ambiguous clause (true inter-model nocuity). If 4 models produce 4 different interpretations of the same clause → true nocuity. If all 4 adopt the same wrong interpretation → systematic bias, still nocuous but for different reason. Report inter-model agreement on ambiguous clauses as supplementary analysis.
238	
239	## Contingency Framing [RESOLVED — Scenario C occurred]
240	
241	> plan_002 结果: Scenario C 发生（omnibus p=0.0001, 所有类型 nocuous 但 severity 有显著差异）。
242	> Framing 已 pivot 到 "Differential Nocuity" + "Layer Hierarchy" (D020)。本节仅保留历史记录。
243	
244	## Claude Baseline — RESOLVED [2026-05-20]
245	
246	✅ Claude works via OpenRouter proxy (47.94.22.126/v1) with provider prefix `anthropic/claude-sonnet-4-6`. 600 episodes complete (plan_002c). Claude shows lowest overall vulnerability (30.3%) and remarkable auth_scope robustness (12% vs GPT-5.4 64%).
247	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "beb3e936-6b73-45c6-8a6f-80983a31ad7e",
  "isSidechain": false,
  "promptId": "eee4c209-3712-4b8a-9840-fcbadb07765b",
  "type": "user",
  "uuid": "a54cd3eb-58c0-45f3-90f3-69dfa1ef7912",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best/paper_framing.md",
      "content": "# Paper Framing — policy_ambiguity_safety\n\n> 最后更新: 2026-05-20 19:30 UTC | 状态: 5-model analysis complete, C3/C4 framing revised\n> 目标: EMNLP 2026 (ARR Aug cycle, DDL ~Aug 3)\n> Dream: dream_20260520T112859 — best 3.5 / median 3.0 / worst 2.5 (pre-pivot; re-dream needed)\n> 5-model: 2,997 episodes, C1 confirmed (+34.0pp, 5 models), C4 upgraded (model×type interaction)\n\n## Core Insight\n\nPolicy ambiguity universally causes massive safety violations in LLM agents (+34.0pp across 5 architecturally diverse models), with a significant type hierarchy (incompleteness 53.6% >> coreferential 31.6%). Specification-layer types are more dangerous on average (Δ=6.08pp, p=0.017), but the deeper finding is a **model × type interaction**: authorization scope vulnerability varies 52pp across models (12% Claude to 64% GPT-5.4), revealing that safety training differentially mitigates specific ambiguity types, while incompleteness remains universally dangerous. This interaction connects Berry & Kamsties' nocuous ambiguity theory to modern safety alignment and suggests both type-aware triage AND model-aware risk assessment.\n\n## Title (Working)\n\n\"Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families\"\n\nAlternative: \"Differential Nocuity: How Ambiguity Type and Model Architecture Shape Safety Violations in LLM Agents\"\n\nNote: Pivoted from \"Uniformly Nocuous\" → \"Specification-Layer Dominant\" (2-model) → \"Differential Nocuity with Model Interaction\" (5-model). The model × type interaction is the novel finding that elevates the paper beyond simple effect demonstration.\n\n## Core Claims\n\n### C1: Binary Effect (PRIMARY — confirmed, 5 models)\nAmbiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +34.0pp (5-model), McNemar OR=15.1 (CI: [10.78, 21.17]), p<0.0001. Holds across all 6 types and all 5 models.\n- **Evidence**: 2,997 episodes across 5 models × 6 types × 2 conditions. Bootstrap CI: [+31.2pp, +36.9pp].\n- **Per-model**: Claude +25.7pp, Qwen3 +32.4pp, GPT-4.1 +34.7pp, GPT-5.4 +38.3pp, DeepSeek +39.0pp — all p<10^-17.\n- **Strength**: Extremely strong. Replicated across 5 architecturally diverse models (proprietary dense, open-source MoE, open-source dense), 6 types, 2 domains. No exceptions.\n- **Causal backing**: Matched-pair design + perturbation control (plan_010, Δ_perturb=3.33pp, PASS) → strongest causal inference in the literature.\n- **Logistic regression**: condition_amb coef=2.278, z=19.65, p<0.001 — ambiguity is the dominant predictor even after controlling for token delta, model, and type.\n\n### C2: Type Hierarchy (SECONDARY — confirmed, 5 models)\n**PIVOTED from uniformity null.** 6-type hierarchy significant: omnibus χ²=28.02, p=3.6×10^-5, V=0.137 (small but well-powered: actual power=0.993, MDE=0.093). 3-tier structure emerges from TOST analysis.\n- **Evidence**: 2,997 episodes (5 models × 6 types × 2 conditions, ambiguous only: 1,499 episodes)\n  - **High tier**: incompleteness 53.6% (standout — universally dangerous across all models)\n  - **Mid tier**: lexical 42.8%, auth_scope 41.6%, scopal 39.4%, CP 36.8% — pairwise equivalent at ±15pp\n  - **Low tier**: coreferential 31.6% (lowest — partial disambiguation via tool responses)\n- **TOST structure**: ±15pp: 8/15 equivalent, 7/15 non-equivalent. ±10pp: 4/15 equivalent, 11/15 non-equivalent. Types are NOT interchangeable.\n- **V=0.137 context**: Below 0.20 threshold but well-powered (power=0.993). The type effect is real but small — the 3-tier structure captures it better than a single V statistic. The heterogeneity is driven by the extremes (incompleteness 53.6% vs coreferential 31.6% = 22pp gap).\n- **Coreferential as boundary case**: 31.6% violation rate is the lowest but still substantial (+18.7pp vs unambiguous). Agents partially disambiguate via tool responses and cautious strategies. Conservative_refusal rate 6-11% (vs avg 2-3%).\n- **Model-dependence of type rankings**: Type rankings are NOT identical across models. Incompleteness is top-2 for ALL models, but auth_scope ranges from #1 (GPT-5.4, DeepSeek) to #6 (Claude). See C4.\n\n### C3: Layer Effect (TERTIARY — suggestive, fragile under within-judge analysis)\n**[2026-05-20 REVISED with 5-model data + within-judge check]** Specification-layer ambiguities cause more violations than linguistic-layer on average, but the effect is modest, model-dependent, and fragile under subgroup analysis.\n- **Evidence (5-model aggregate)**: Spec 44.0% vs Ling 37.9%, Δ=6.08pp, CI [1.14, 11.02], χ²=5.73, p=0.017, V=0.062 (small), OR=1.29 [1.05, 1.58].\n- **Within-judge fragility**: gpt-4.1 judged group (gpt-5.4+DeepSeek): Δ=+8.0pp, p=0.059 (marginal). gpt-5.4 judged group (gpt-4.1+Claude+Qwen3): Δ=+4.8pp, p=0.157 (n.s.). Pooled significance may partly reflect between-judge variance or insufficient within-group power. Paper表述: \"suggestive\" or \"a moderate tendency,\" NOT \"confirmed.\" Disclose within-judge non-significance in Limitations.\n- **Per-model layer gaps** (THE KEY FINDING — feeds C4):\n  - GPT-5.4: +14.0pp (spec 48.0% vs ling 34.0%) — strong\n  - GPT-4.1: +12.0pp (spec 46.7% vs ling 34.7%) — strong\n  - Claude: +3.3pp (spec 32.0% vs ling 28.7%) — weak\n  - DeepSeek: +2.0pp (spec 50.7% vs ling 48.7%) — negligible\n  - Qwen3: -0.9pp (spec 42.7% vs ling 43.6%) — reversed!\n- **Root cause**: auth_scope is the primary driver. GPT models have extremely high auth_scope rates (46-64%), inflating their spec-layer average. Claude (12%) and Qwen3 (26%) have low auth_scope, so their spec-layer advantage disappears.\n- **Framing decision**: C3 is NOT \"spec-layer nearly twice as dangerous\" (that was 2-model artifact). The correct framing is: \"Specification-layer types are significantly more dangerous on average (Δ=6.08pp, p=0.017), but this aggregate masks a model × type interaction where the gap varies from +14pp (GPT-5.4) to -1pp (Qwen3). The interaction, not the main effect, is the theoretically interesting finding (see C4).\"\n- **Info delta as mediator** [MF-2]: Token delta significant in 5-model logistic regression (coef=0.022, z=3.49, p=0.0005). Spec-layer clauses require more tokens to disambiguate (auth_scope 36.1, incomp 34.6 vs coref 7.8 tokens). Info delta partially mediates but doesn't eliminate the condition effect (condition_amb coef=2.278 dominates).\n- **Layer overlap persists**: CP (36.8%, spec) < scopal (39.4%, ling). Mid-tier cluster spans both layers. Layer effect is driven by extremes: incompleteness (53.6%, spec) vs coreferential (31.6%, ling).\n- **ICC convergent evidence** [plan_006]: Per-type ICC mirrors layer hierarchy — Ling-layer ICC all excellent (scopal 0.989, lexical 0.981, coref 0.976), Spec-layer ICC all good (auth 0.857, CP 0.856, incomp 0.807). Spec-layer less reproducible — agents guess differently each run when external disambiguation channels are absent.\n- **CL connection**: Parallels pragmatics vs semantics distinction. Good-enough processing (Ferreira et al. 2002). Disambiguation channel framework: linguistic ambiguity has partial external resolution; specification ambiguity forces guessing.\n\n### C4: Model × Type Interaction (UPGRADED — star finding, 5 models complete)\n**[2026-05-20 DEFINITIVE, 5/5 models]** Models show significantly different vulnerability profiles despite universal binary effect. The interaction is the paper's most novel finding.\n- **Model main effect**: Overall χ²=31.02, p=3.0×10^-6, V=0.102. Ambiguous-only: χ²=24.01, p=7.9×10^-5.\n  - Vulnerability ranking: Claude 30.3% < GPT-5.4 41.0% ≈ GPT-4.1 40.7% < Qwen3 43.1% < DeepSeek 49.7%\n  - Bootstrap CI confirms: Claude significantly lower than all others; DeepSeek significantly higher than GPT models.\n- **Model × Type interaction matrix** (ambiguous condition, violation rates):\n  ```\n  Type                  GPT-5.4  GPT-4.1  Claude  Qwen3   DeepSeek\n  authorization_scope     64%     46%      12%     26%     60%\n  conditional_precedence  34%     36%      36%     40%     38%\n  incompleteness          46%     58%      48%     62%     54%\n  lexical                 42%     34%      32%     52%     54%\n  coreferential           18%     32%      22%     42%     44%\n  scopal                  42%     38%      32%     37%     48%\n  ```\n- **Key interaction patterns**:\n  - **auth_scope**: 52pp range (Claude 12% → GPT-5.4 64%). The MODEL-DIFFERENTIATING type. Claude's RLHF appears to specifically train authorization boundary awareness.\n  - **coreferential**: 26pp range (GPT-5.4 18% → DeepSeek 44%). Second most model-dependent. Open-source models struggle more with referential ambiguity.\n  - **incompleteness**: Universally high (46-62%, 16pp range). ALL models fail on missing information — safety training doesn't help when information literally isn't there.\n  - **CP**: Most model-invariant (34-40%, 6pp range). Explicit rule conflicts treated similarly by all architectures.\n- **Per-model type χ²** (which models show type-specific vulnerability patterns):\n  - GPT-5.4: χ²=23.44, p=0.0003, V=0.28 — strongest type differentiation (very high auth_scope, very low coref)\n  - Claude: χ²=17.87, p=0.003, V=0.24 — strong differentiation (very low auth_scope, moderate others)\n  - Qwen3: χ²=15.89, p=0.007, V=0.23 — moderate differentiation (high incomp+lex, low auth_scope)\n  - GPT-4.1: χ²=9.89, p=0.078, V=0.18 — borderline\n  - DeepSeek: χ²=6.31, p=0.277, V=0.14 — NOT significant (uniformly high across all types)\n- **Fleiss κ = 0.384 (fair agreement)**: Models only moderately agree on which specific clauses trigger violations. The binary effect is universal, but the WHICH-clauses question is model-dependent.\n- **Theoretical implications**: (1) Safety training differentially addresses specific ambiguity types — Claude's auth_scope robustness suggests authorization boundary handling was explicitly or implicitly trained. (2) Incompleteness is a \"safety training blind spot\" — all models fail equally. (3) DeepSeek's uniform vulnerability suggests less type-specific safety training.\n- **Framing**: C4 from \"models agree\" → \"Models show systematically different vulnerability profiles. The binary effect is universal, but HOW models fail depends on the intersection of ambiguity type and safety training approach. auth_scope is the canary type — most sensitive to safety training quality.\"\n- **Evidence from plan_005**: 2-model failure modes consistent (5/6 dominant modes identical). 5-model failure mode analysis pending.\n- **Layer effect moderation**: C3's aggregate layer gap (6.08pp) is driven by GPT models' high auth_scope rates. The layer effect is itself model-dependent (GPT +12-14pp, Claude +3pp, Qwen3 reversed), making the MODEL × TYPE interaction more fundamental than the LAYER main effect.\n\n### C5: Error Analysis (CONFIRMED — EMNLP core)\nDifferent ambiguity types produce qualitatively different failure modes with type-specific signatures. plan_005 (123+122 violation traces across gpt-5.4 and gpt-4.1, confidence=0.94).\n- **Evidence**: plan_005 complete (gpt-5.4: 123 traces, gpt-4.1: 122 traces). Key findings:\n  - **Type-specific failure signatures**: auth_scope → unauthorized_escalation (72%/83%); incompleteness → assumption_based_action (61%/66%); scopal → scope_misapplication (76%/74%); lexical → assumption_based_action (71%/53%); CP → scope_misapplication (41%/28%) + arbitrary_rule_selection (29%/28%); coreferential → scope_misapplication (44%) / assumption_based_action (38%)\n  - **Cross-model consistency**: 5/6 types share the same dominant failure mode across gpt-5.4 and gpt-4.1. Only coreferential diverges (scope_misapplication vs assumption_based_action). Overall mode distribution nearly identical: both ~33% assumption_based_action, ~26-32% unauthorized_escalation, ~25-28% scope_misapplication. Failure mode profiles are type-specific, not model-specific.\n  - **Layer mechanism**: Ling-layer dominated by scope_misapplication (39% ling avg vs 15% spec avg) = \"misparse\"; Spec-layer dominated by unauthorized_escalation + assumption_based_action = \"active guessing\" → explains higher violation rates\n  - **Ambiguity Blindness empirically confirmed**: awareness rate gpt-5.4=4.1%, gpt-4.1=10.7% (both very low); surface_adoption >88% all types both models; escalate_to_user <1%. Nuance: gpt-4.1 (mid-tier) shows 2.6× higher awareness than gpt-5.4 (frontier) — awareness may inversely correlate with action-orientation (frontier models more \"confident,\" act without hesitation)\n  - **Cross-domain consistency**: airline vs retail failure mode profiles Δ < 13pp (unauthorized_escalation shows largest domain effect: retail 38.6% vs airline 26.1%)\n  - **Coreferential boundary**: conservative_refusal 6-11% (vs avg 2-3%) partially explains low violation rate — agents sometimes pause rather than guess. N=25 combined traces show no single dominant failure mode (flat distribution: scope_misapplication 32%, assumption_based_action 28%, unauthorized_escalation 16%) — contrasts with other types' sharp signatures, reflecting the diversity of resolution strategies for referential ambiguity\n  - **Lexical surprise**: 53-71% assumption_based_action — agents treat word ambiguity as information gap, not misparse\n- **Automated inter-coder agreement** [MF-5, Reviewer-validated]: Cross-coding 60 traces (gpt-5.4 vs gpt-4.1 as independent coders). 4-category merged: 80% agreement, Cohen's κ=0.594 (moderate). κ deflated by kappa paradox — lexical 91.7% agreement → κ=0.0 (11/12 same label, chance agreement also high), scopal 100% agreement → κ undefined. True disagreement concentrated at unauthorized_escalation ↔ inappropriate_action boundary in auth_scope (κ=0.054) and incompleteness (κ=0.233).\n  - **Reporting strategy** [Reviewer recommendation]: (1) Compute Gwet's AC1 as primary metric (designed for kappa paradox, expected 0.70-0.75); (2) Report 80% agreement + 5/6 dominant mode consistency as headline validity evidence; (3) Report κ honestly with kappa paradox caveat; (4) Auth_scope failure mode: soften to \"dominated by boundary-exceeding behaviors (unauthorized_escalation or inappropriate_action, >90%)\" instead of specific percentages; (5) Fine-grained 6-type as appendix with \"automated coding\" caveat.\n  - **C5 safety**: Ambiguity Blindness (<5-11%), surface_adoption (>88%), layer mechanism (ling→scope vs spec→escalation) all robust. Fine-grained per-type percentages unreliable at κ=0.594. Plan_009 human anchor (20-30 failure mode traces) would upgrade from \"moderate automated\" to validated.\n- **EMNLP value**: Highest. Provides the linguistic WHY behind the quantitative WHAT. Cross-model + cross-domain consistency elevates from anecdotal to systematic finding. \"Ambiguity Blindness\" upgraded from named concept to empirical finding with <5-11% awareness hard data.\n\n## Narrative Structure (CL-first for EMNLP)\n\n### Intro Logic Chain\n1. Agent policies are written in NL → contain ambiguity (established)\n2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact\n3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.\n4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter? Does it depend on the model?\n5. **This paper**: First causal, type-granularity, cross-model study. Matched-pair design + perturbation control isolates ambiguity effect. 5 models × 6 types.\n6. **Core findings**: (a) All ambiguity is nocuous (+34.0pp, 5 models), (b) type DOES predict severity — 3-tier hierarchy with incompleteness most dangerous, (c) models show dramatically different vulnerability profiles — auth_scope varies 52pp across models, suggesting safety training differentially addresses ambiguity types, (d) while incompleteness remains universally dangerous, a \"safety training blind spot.\"\n\n### Section Map\n- **§1 Intro**: Gap + contributions (causal map + differential nocuity + model×type interaction)\n- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R\n- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R\n- **§4 Method**: Matched-pair causal design, τ²-bench, 5 models (3 proprietary + 2 open-source), clause generation, perturbation control, cross-judge evaluation\n- **§5 Results**: C1 (binary, +34.0pp, 5 models) → C2 (type hierarchy, 3-tier) → C3 (layer effect, modest but significant) → C4 (model×type interaction — star finding)\n- **§6 Analysis**: C5 error analysis — qualitative failure modes per type. Ambiguity Blindness. Model-specific patterns.\n- **§7 Discussion**: Differential nocuity theory. Safety training selectivity. Disambiguation channel framework. Limitations (2 domains, synthetic injection, LLM-as-judge).\n- **§8 Conclusion**: All policy ambiguity is nocuous, but type AND model jointly determine risk level. Both type-aware auditing and model-specific risk assessment recommended.\n\n## Anticipated Reviewer Concerns\n\n### RC1: \"Type effect could be artifact of taxonomy granularity\"\n**Response**: (a) Layer effect (Spec vs Ling ~19pp gap) is robust — holds even if individual types are reclassified. (b) 2-layer structure grounded in Li et al. + Massey et al. (c) Coreferential's low rate has structural explanation (disambiguation channels), not just noise. (d) TOST confirms types are NOT equivalent (0/15 pairs at ±10pp).\n\n### RC2: \"Taxonomy is ad hoc / why these 6 types\"\n**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).\n\n### RC3: \"Only API models, no open-source\"\n**Response**: ✅ RESOLVED. 5-model coverage spans: frontier proprietary (gpt-5.4, claude-sonnet-4-6) + mid-tier proprietary (gpt-4.1) + open-source MoE (qwen3-235b) + open-source dense (deepseek-v3). Three providers (OpenAI, Anthropic, Chinese open-source). Two architecture types (dense, MoE). Model×type interaction (C4) reveals rich cross-model patterns.\n**Note [Reviewer 2026-05-20]**: Cross-judge asymmetry — Claude judged by gpt-5.4, gpt-5.4 judged by gpt-4.1. Must disclose in Method. plan_009 judge calibration measures this bias.\n\n### RC4: \"Synthetic ambiguity injection lacks ecological validity\"\n**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.\n\n### RC5: \"τ²-bench limited to retail/airline\"\n**Response**: Acknowledged limitation. Two domains already show consistent effects. Cross-domain transfer is Future Work (Phase 3 classifier PoC, if time permits). DRIP-R also single-domain (retail).\n\n### RC6: \"Binary effect is obvious — of course ambiguity causes errors\"\n**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOES predict severity — specification-layer ambiguities are nearly twice as dangerous, connecting to disambiguation channel availability.\n\n### RC7: \"Incompleteness matched-pair confound (information asymmetry)\"\n**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.\n\n### RC8: \"RC attachment in coreferential overlaps with scopal / structural ambiguity\"\n**Response**: (a) Our scopal category is explicitly scoped to quantifier/negation/modal scope interactions, not syntactic attachment. (b) RC attachment in policies manifests as *referential* confusion (which entity does the clause modify?) not *scope* confusion (which operator takes wide scope?). (c) Li et al. 2024 distinguishes syntactic ambiguity (including RC attachment) from scopal ambiguity — our grouping follows their treatment that RC attachment is closer to coreferential than scopal in terms of downstream interpretation. (d) Empirically, if the distinction were problematic, coreferential and scopal would show identical violation patterns — the error analysis (C5) can test whether their failure modes differ.\n\n### RC9: \"authorization_scope is just a subtype of incompleteness\"\n**Response**: (a) Incompleteness = missing conditions/exceptions/boundaries (structural absence). Authorization scope = ambiguous permission/role boundaries that ARE stated but vague (e.g., \"authorized personnel\" without specifying which functions). (b) The disambiguation pattern differs: incompleteness adds new conditions; auth_scope clarifies existing permission boundaries. (c) Empirically testable: if they were the same, their violation patterns and failure modes (C5) would be indistinguishable. (d) Report disambiguation length ratio per type as control variable in §4 Method.\n\n### RC10: \"API sampling noise undermines reliability\"\n**Response**: ✅ RESOLVED. plan_006 ICC=0.919 [0.892, 0.940] (excellent). (a) Per-clause violation rates highly reproducible across 3 independent replicates. (b) Binary ICC=0.847 (good). (c) Both models show near-identical ICC (gpt-5.4: 0.921, gpt-4.1: 0.918). (d) Bootstrap CI + ICC double evidence. (e) Previously identified ±8pp noise is within expected variance given the ICC confidence intervals.\n\n### RC11: \"Prompt sensitivity confound\" [Dream A9 — best tier \"strongest point\"]\n**Concern**: The +35-42pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness.\n**Response**: ✅ RESOLVED. plan_010 perturbation control (120 episodes): Δ_perturb=3.33pp (CI contains 0) vs ambiguity Δ=36.5pp. Non-ambiguity surface changes cause zero meaningful effect. This is the strongest causal evidence in the agent safety literature.\n\n## Concept Naming (distill insight: 命名即贡献)\n\nCore phenomenon: **\"Differential Nocuity\"** — all policy ambiguity types are nocuous for LLM agents (+34.0pp, all 5 models), but vulnerability varies by BOTH type and model. Incompleteness is universally dangerous (46-62%), while auth_scope vulnerability depends dramatically on safety training (12% Claude to 64% GPT-5.4). Unlike human RE where organizational context renders most ambiguity innocuous, agents lack disambiguation channels AND their safety training creates type-specific blind spots.\n\nSecondary phenomenon: **\"Ambiguity Blindness\"** — agents process grammatically fluent ambiguous clauses without meta-cognitive awareness of the ambiguity, adopting surface interpretations. Contrasts with explicit rule conflicts where agents show awareness and choose conservatively.\n\nTertiary phenomenon: **\"Disambiguation Channel Framework\"** [renamed from \"Hypothesis\" per Dream review SF-5] — the layer hierarchy reflects availability of external disambiguation: linguistic ambiguity (coreferential, lexical) can sometimes be resolved by tool responses, user context, or world knowledge; specification ambiguity (auth_scope, incompleteness) has no external resolution channel, forcing agents to guess. This is an explanatory framework supported by observational evidence (ICC pattern, failure mode distribution, coreferential boundary case), not a tested causal hypothesis. Future Work: manipulation experiment (inject spec-layer disambiguation info into tool responses, test if gap shrinks).\n\nQuaternary phenomenon: **\"Systematic Nocuity\"** [per Dream review SF-7] — B&K framework distinguishes nocuous (divergent interpretations) from innocuous (convergent). Our data reveals a third type: all models converge on the same WRONG interpretation (27% of ambiguous episodes). This is more dangerous than divergent nocuity — it's invisible in inter-model agreement metrics and appears \"correct\" until compared against ground truth. Proposed as B&K extension in Discussion.\n\n## Opening Hook Strategy (distill insight: 具体案例, 不要 \"Recently...\")\n\nOpen with a concrete τ²-bench failure: e.g., a customer returns a customized item within the return window; the agent grants a full refund + free return shipping because the policy says \"items may be returned within 30 days\" (scopal: \"items\" scopes over all categories including custom). The unambiguous version specifies \"standard items only\" — agent correctly refuses. One word of ambiguity → $200 unauthorized refund.\n\n## Narrative Type: 突破局限型 (distill pattern, 5/8 papers)\n\n\"DRIP-R classifies 5 ambiguity types and shows models disagree on interpretation → but does not measure whether this disagreement leads to safety violations. We close this gap — and find the answer is surprising: not all types are equal, specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones.\"\n\n## Benchmark Comparison Table (distill insight: 必有 feature matrix)\n\n| Feature | DRIP-R | PhantomPolicy | PolicyBank | AgentPex | **Ours** |\n|---------|--------|---------------|------------|----------|----------|\n| Ambiguity taxonomy | 5 RE types | — | 3 gap types | — | **6 types (2-layer)** |\n| Causal design | — | — | — | — | **matched pairs** |\n| Safety violation metric | — | binary | — | procedural | **3-tier severity** |\n| Cross-type comparison | descriptive | — | — | — | **statistical (χ² + V)** |\n| Models tested | 6 API | 4 API | 2 API | 2 API | **3 API + 2 open-source** |\n| Domain | retail | mixed | retail | telecom/retail/airline | **retail + airline** |\n\n## Contribution Positioning (for EMNLP) [revised 2026-05-20 with 5-model data]\n\n1. **Causal quantification of ambiguity's safety impact**: First matched-pair causal study of policy ambiguity → agent safety violations. Binary effect +34.0pp (OR=15.1, p<0.0001) across 5 architecturally diverse models and 6 ambiguity types. Perturbation control (Δ_perturb=3.33pp) confirms ambiguity-specific causation. Strongest causal evidence in the agent safety literature.\n2. **Differential Nocuity framework + Model × Type Interaction**: Not all ambiguity is equally dangerous, and not all models are equally vulnerable. 3-tier type hierarchy (incompleteness >> mid cluster >> coreferential). Model × type interaction reveals 52pp range in auth_scope vulnerability (Claude 12% → GPT-5.4 64%), while incompleteness remains universally dangerous (46-62%). Safety training differentially mitigates specific ambiguity types. Connects Berry & Kamsties nocuous ambiguity theory to modern safety alignment.\n3. **Type-specific failure mode taxonomy + Ambiguity Blindness**: 245 traces across 2 models and 2 domains reveal type-diagnostic failure signatures: spec-layer → guess-and-act (unauthorized_escalation, assumption_based_action); ling-layer → misparse-and-apply (scope_misapplication). Agents show <5-11% awareness of ambiguity (\"Ambiguity Blindness\"), with >88% surface adoption and <1% user escalation. Practical implication: ambiguity detection must be externalized.\n\nNOTE: C3 (layer effect, Δ=6.08pp) is a component finding supporting contribution #2. The MODEL × TYPE interaction (C4) is now MORE central than the layer main effect. \"Disambiguation channel\" is an explanatory framework (not hypothesis — per SF-5). DeBERTa classifier, if included, is a preliminary PoC appendix, not a contribution.\n\n## Required Reference Expansion [Dream A2 + MF-4 RE literature gap]\n\nCurrent plan has thin references. Must add (≥25 total in final paper):\n- **Nocuous ambiguity detection (CRITICAL — MF-4)**: Chantree, Nuseibeh, de Roeck & Willis (2006, ASE) — first computational nocuous ambiguity detection; Chantree et al. (2008, RLAC) — expanded. Direct lineage to our DeBERTa classifier.\n- **Cross-domain RE ambiguity**: Ferrari, Spagnolo & Gnesi (2017-2019, ASE) — NLP-based cross-domain ambiguity detection. NLP4RE community work.\n- **Good-enough processing**: Ferreira, Bailey & Ferraro (2002); Ferreira & Patson (2007)\n- **LLM garden-path (SF-6)**: Li et al. (2024) — incremental comprehension of garden-path sentences by LLMs. Directly relevant to how LLMs process ambiguity.\n- **Anaphoric ambiguity (SF-6)**: Poesio & Artstein (2005, 2008) — annotation of anaphoric ambiguity. Poesio (2004) \"Ambiguity\" encyclopedia entry.\n- **Surprisal/expectation-based**: Levy (2008); Hale (2001)\n- **Instruction-following robustness**: Zhou et al. (IFEval, 2023); Qin et al. (ToolBench, 2024)\n- **Prompt sensitivity**: Sclar et al. (2024); Lu et al. (2022)\n- **Broader agent safety**: R-Judge, ToolEmu, InjecAgent\n- **Formal semantics of vagueness**: Lassiter & Goodman (2017)\n- **Garden-path**: Frazier & Rayner (1982)\n- **Ambiguity detection**: Willis et al. (2008); Ezzini et al. (TAPHSIR, 2022)\n- **Year verification needed**: Massey et al. — §1 引用 2013 vs 后文 2014, 需确认正确年份\n\n## Code/Data Release Plan [Dream A6 — three-tier consistent]\n\nMust commit to releasing:\n1. All 300 clause pairs (ambiguous + unambiguous variants) with type labels\n2. Evaluation scripts (τ²-bench integration, cross-judge pipeline)\n3. Statistical analysis code (all tests, bootstrap CI computation)\n4. Agent trace samples (anonymized) for reproducibility of C5\n\n## Figure Plan [Dream A12]\n\nMinimum figures for paper (zero-figure paper flagged in dream):\n1. **Figure 1**: System architecture / experimental pipeline overview (§4 Method)\n2. **Figure 2**: Forest plot — per-type binary effect sizes with 95% CI (§5 C1)\n3. **Figure 3**: Model × Type heatmap — violation rates across 4 models × 6 types (§5 C4)\n4. **Figure 4**: Visibility mechanism — CP vs scopal violation rates + trace evidence (§5 C3)\n5. **Figure 5**: Failure mode × type stacked bar/Sankey — per-type failure mode distribution (§6 C5)\n6. **Figure 6**: Cross-model failure mode consistency — side-by-side gpt-5.4 vs gpt-4.1 per-type distributions showing 5/6 convergence (§6 C5, supports C4)\n7. **Figure 7**: Annotated trace pair — CP (conflict detection) vs scopal (surface adoption) (§6 C5)\n\n## Berry & Kamsties Operationalization Note [Dream best Q5]\n\nBerry & Kamsties define nocuity as inter-reader divergence. Our design measures agent-vs-intent deviation. Full study should additionally test whether different models adopt different readings of the same ambiguous clause (true inter-model nocuity). If 4 models produce 4 different interpretations of the same clause → true nocuity. If all 4 adopt the same wrong interpretation → systematic bias, still nocuous but for different reason. Report inter-model agreement on ambiguous clauses as supplementary analysis.\n\n## Contingency Framing [RESOLVED — Scenario C occurred]\n\n> plan_002 结果: Scenario C 发生（omnibus p=0.0001, 所有类型 nocuous 但 severity 有显著差异）。\n> Framing 已 pivot 到 \"Differential Nocuity\" + \"Layer Hierarchy\" (D020)。本节仅保留历史记录。\n\n## Claude Baseline — RESOLVED [2026-05-20]\n\n✅ Claude works via OpenRouter proxy (47.94.22.126/v1) with provider prefix `anthropic/claude-sonnet-4-6`. 600 episodes complete (plan_002c). Claude shows lowest overall vulnerability (30.3%) and remarkable auth_scope robustness (12% vs GPT-5.4 64%).\n",
      "numLines": 247,
      "startLine": 1,
      "totalLines": 247
    }
  },
  "sourceToolAssistantUUID": "beb3e936-6b73-45c6-8a6f-80983a31ad7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122435 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguit…",
  "leafUuid": "a54cd3eb-58c0-45f3-90f3-69dfa1ef7912",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP paper on policy ambiguity safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc"
}
```

---

### Assistant

_source line 17 · 2026-05-21T12:50:03.585Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me also read the paper-writing-norms skill for quality guidance, and check what LaTeX packages are available.

Let me now write the complete LaTeX paper. I need to:

1. Cover all 10 experiments from experiment_data.json
2. Follow the narrative guidance: Title "Differential Nocuity", 5 claims at specified strengths
3. Follow the paper_framing.md structure
4. EMNLP 2026 format (8 pages main text)
5. Include Abstract, Introduction, Method, Experiments/Results, Analysis, Conclusion


6. Map each experiment to its section: the clause generation and pilot studies go into Method, the API and open-source model results form the core Results, statistical analyses support all claims, error analysis drives the Discussion, and the remaining validation studies strengthen the methodological foundation throughout.

Now I'm setting up the LaTeX document in ACL format and starting to write the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a54cd3eb-58c0-45f3-90f3-69dfa1ef7912",
  "isSidechain": false,
  "requestId": "req_011CbFk1LHfaTJpHT8gDAvGe",
  "type": "assistant",
  "uuid": "4835758a-5003-4d53-8319-d2664eac176a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pu4r73iy5aWnNq7nTTnFGj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26808,
      "cache_read_input_tokens": 23573,
      "output_tokens": 607,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 607,
          "cache_read_input_tokens": 23573,
          "cache_creation_input_tokens": 26808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26808
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

_source line 18 · 2026-05-21T12:50:03.587Z_

Now I have the full picture. Let me read the paper-writing-norms skill briefly, then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4835758a-5003-4d53-8319-d2664eac176a",
  "isSidechain": false,
  "requestId": "req_011CbFk1LHfaTJpHT8gDAvGe",
  "type": "assistant",
  "uuid": "e0488bd7-29c3-4f1b-b4ca-fea12798e505",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pu4r73iy5aWnNq7nTTnFGj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26808,
      "cache_read_input_tokens": 23573,
      "output_tokens": 607,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 607,
          "cache_read_input_tokens": 23573,
          "cache_creation_input_tokens": 26808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26808
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

_source line 19 · 2026-05-21T12:50:04.340Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NuxFJjv1deD7aBTyVuZg2F`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0488bd7-29c3-4f1b-b4ca-fea12798e505",
  "isSidechain": false,
  "requestId": "req_011CbFk1LHfaTJpHT8gDAvGe",
  "type": "assistant",
  "uuid": "04b936c3-eef3-4c13-ac75-a8aea4bd647d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pu4r73iy5aWnNq7nTTnFGj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26808,
      "cache_read_input_tokens": 23573,
      "output_tokens": 607,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 607,
          "cache_read_input_tokens": 23573,
          "cache_creation_input_tokens": 26808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26808
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

_source line 20 · 2026-05-21T12:50:04.346Z_

<details><summary>↩ Tool result · `toolu_01NuxFJjv1deD7aBTyVuZg2F`</summary>

```text
1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **禁止过度宣传**：不说 "revolutionary"、"groundbreaking"
75	- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元
76	- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了
77	- **缩写必须定义**：Abstract 中首次出现的缩写必须展开
78	
79	### 2.3 审稿人视角检验
80	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04b936c3-eef3-4c13-ac75-a8aea4bd647d",
  "isSidechain": false,
  "promptId": "eee4c209-3712-4b8a-9840-fcbadb07765b",
  "type": "user",
  "uuid": "e4be5eb1-9762-4200-bc58-a5eced52c22c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n",
      "numLines": 80,
      "startLine": 1,
      "totalLines": 276
    }
  },
  "sourceToolAssistantUUID": "04b936c3-eef3-4c13-ac75-a8aea4bd647d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T12:50:06.561Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VdDuryWmGKDT4pFSWn8jtR`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best/",
  "description": "List output directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4be5eb1-9762-4200-bc58-a5eced52c22c",
  "isSidechain": false,
  "requestId": "req_011CbFk1LHfaTJpHT8gDAvGe",
  "type": "assistant",
  "uuid": "f45bbfd0-33a2-4b27-9686-3051a624ad3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pu4r73iy5aWnNq7nTTnFGj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26808,
      "cache_read_input_tokens": 23573,
      "output_tokens": 607,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 607,
          "cache_read_input_tokens": 23573,
          "cache_creation_input_tokens": 26808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26808
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

_source line 22 · 2026-05-21T12:50:06.709Z_

<details><summary>↩ Tool result · `toolu_01VdDuryWmGKDT4pFSWn8jtR`</summary>

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
  "parentUuid": "f45bbfd0-33a2-4b27-9686-3051a624ad3c",
  "isSidechain": false,
  "promptId": "eee4c209-3712-4b8a-9840-fcbadb07765b",
  "type": "user",
  "uuid": "1abe0084-c710-4c1d-a601-a8d18f9403f2",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f45bbfd0-33a2-4b27-9686-3051a624ad3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-21T12:50:09.524Z_

<details><summary>Logged reasoning block</summary>

```text
Let me check if pdflatex is available and what packages are installed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1abe0084-c710-4c1d-a601-a8d18f9403f2",
  "isSidechain": false,
  "requestId": "req_011CbFk2SiQ4rhU1fxfsZ7a2",
  "type": "assistant",
  "uuid": "9077eb5f-9aea-4c24-99a7-9ce382807f81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JSWqutF1E9kEQT35BYaQE9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2239,
      "cache_read_input_tokens": 50381,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2239,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 120,
          "cache_read_input_tokens": 50381,
          "cache_creation_input_tokens": 2239,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2239
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

_source line 24 · 2026-05-21T12:50:09.768Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JNQT9MMxeFDNNaB3MSn5xv`</summary>

```json
{
  "command": "which pdflatex && pdflatex --version | head -3",
  "description": "Check pdflatex availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9077eb5f-9aea-4c24-99a7-9ce382807f81",
  "isSidechain": false,
  "requestId": "req_011CbFk2SiQ4rhU1fxfsZ7a2",
  "type": "assistant",
  "uuid": "9e0a5f65-6a63-4c15-b06e-6cda498aee6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JSWqutF1E9kEQT35BYaQE9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2239,
      "cache_read_input_tokens": 50381,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2239,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 120,
          "cache_read_input_tokens": 50381,
          "cache_creation_input_tokens": 2239,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2239
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

_source line 25 · 2026-05-21T12:50:09.833Z_

<details><summary>↩ Tool result · `toolu_01JNQT9MMxeFDNNaB3MSn5xv`</summary>

```text
/usr/bin/pdflatex
pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)
kpathsea version 6.4.1
Copyright 2025 Han The Thanh (pdfTeX) et al.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e0a5f65-6a63-4c15-b06e-6cda498aee6d",
  "isSidechain": false,
  "promptId": "eee4c209-3712-4b8a-9840-fcbadb07765b",
  "type": "user",
  "uuid": "198ac9f9-784e-48b6-b24c-9bca618c74ab",
  "toolUseResult": {
    "stdout": "/usr/bin/pdflatex\npdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)\nkpathsea version 6.4.1\nCopyright 2025 Han The Thanh (pdfTeX) et al.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "9e0a5f65-6a63-4c15-b06e-6cda498aee6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-21T12:50:13.975Z_

<details><summary>Logged reasoning block</summary>

```text
Good, pdflatex is available. Now let me write the full paper. I need to use a standard article class since I likely don't have the ACL/EMNLP style files. Let me check.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "198ac9f9-784e-48b6-b24c-9bca618c74ab",
  "isSidechain": false,
  "requestId": "req_011CbFk2g3qTCLiu9QhqWks9",
  "type": "assistant",
  "uuid": "442c96a0-1df9-4f52-8b58-0c7429b51d6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDn8j3SFafw9jGyLTdb3t9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 203,
      "cache_read_input_tokens": 52620,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 203,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 317,
          "cache_read_input_tokens": 52620,
          "cache_creation_input_tokens": 203,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 203
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

_source line 27 · 2026-05-21T12:50:16.552Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TiNoTxxAVmh4pCwHruXyqh`</summary>

```json
{
  "command": "kpsewhich acl.sty 2>/dev/null; kpsewhich acl_natlog.sty 2>/dev/null; kpsewhich emnlp.sty 2>/dev/null; echo \"---\"; kpsewhich booktabs.sty 2>/dev/null; kpsewhich multirow.sty 2>/dev/null; kpsewhich xcolor.sty 2>/dev/null; kpsewhich hyperref.sty 2>/dev/null; kpsewhich graphicx.sty 2>/dev/null; kpsewhich amsmath.sty 2>/dev/null; kpsewhich natbib.sty 2>/dev/null",
  "description": "Check available LaTeX style files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "442c96a0-1df9-4f52-8b58-0c7429b51d6e",
  "isSidechain": false,
  "requestId": "req_011CbFk2g3qTCLiu9QhqWks9",
  "type": "assistant",
  "uuid": "2c39e8d7-ee27-4f90-8a27-b18241f80239",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDn8j3SFafw9jGyLTdb3t9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 203,
      "cache_read_input_tokens": 52620,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 203,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 317,
          "cache_read_input_tokens": 52620,
          "cache_creation_input_tokens": 203,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 203
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

_source line 28 · 2026-05-21T12:50:16.802Z_

<details><summary>↩ Tool result · `toolu_01TiNoTxxAVmh4pCwHruXyqh`</summary>

```text
---
/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty
/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty
/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c39e8d7-ee27-4f90-8a27-b18241f80239",
  "isSidechain": false,
  "promptId": "eee4c209-3712-4b8a-9840-fcbadb07765b",
  "type": "user",
  "uuid": "abcfd5da-e176-4764-86bd-df3fea202526",
  "toolUseResult": {
    "stdout": "---\n/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty\n/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty\n/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\n/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "2c39e8d7-ee27-4f90-8a27-b18241f80239",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-21T12:50:20.579Z_

No ACL style files available, so I'll use a clean article class approximating conference format. Writing the full paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abcfd5da-e176-4764-86bd-df3fea202526",
  "isSidechain": false,
  "requestId": "req_011CbFk3Bsx9zFo7d26TZPgx",
  "type": "assistant",
  "uuid": "389e1303-3b11-46f3-9b2d-c6830e8231db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019E4VEnHtxLoSsUSBeiXN2U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 532,
      "cache_read_input_tokens": 52823,
      "output_tokens": 12752,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 532,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12752,
          "cache_read_input_tokens": 52823,
          "cache_creation_input_tokens": 532,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 532
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

_source line 30 · 2026-05-21T12:54:25.226Z_

<details open><summary>🔧 Tool call — Write · `toolu_01E95wJw2LcbapeYuaTrmNPs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{enumitem}\n\n\\hypersetup{colorlinks=true,linkcolor=blue!60!black,citecolor=blue!60!black,urlcolor=blue!60!black}\n\n\\title{Differential Nocuity: How Ambiguity Type and Model Architecture\\\\Shape Safety Violations in LLM Agents}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nLarge Language Model (LLM) agents increasingly execute real-world tasks governed by natural-language policies, yet these policies inevitably contain ambiguity.\nWe present the first causal, type-granular, cross-model study of how policy ambiguity drives safety violations in LLM agents.\nUsing a matched-pair design with perturbation controls across 300 clause pairs spanning six ambiguity types, we evaluate five architecturally diverse models (GPT-5.4, GPT-4.1, Claude Sonnet 4.6, Qwen3-235B, DeepSeek-V3) in 3{,}000 agentic episodes on the $\\tau^2$-bench framework.\nWe find that ambiguity universally causes massive safety violations (+34.0 percentage points (pp), OR=15.1, $p<0.0001$), but vulnerability is \\emph{not} uniform.\nA three-tier type hierarchy emerges: incompleteness poses the greatest risk (53.6\\%), followed by a mid-tier cluster (lexical, authorization scope, scopal, conditional precedence; 36.8--42.8\\%), with coreferential ambiguity lowest (31.6\\%).\nCrucially, we uncover a \\textbf{model $\\times$ type interaction}: authorization-scope vulnerability ranges 52pp across models (12\\% Claude to 64\\% GPT-5.4), while incompleteness remains universally dangerous (46--62\\%).\nQualitative analysis of 300 violation traces reveals type-diagnostic failure signatures and pervasive \\emph{ambiguity blindness}---agents acknowledge ambiguity in fewer than 11\\% of cases.\nThese findings establish the concept of \\emph{differential nocuity} and demonstrate that effective safety mitigation requires both type-aware policy auditing and model-specific risk assessment.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nConsider a customer-service agent processing a return for a customized item.\nThe governing policy states: ``Items may be returned within 30 days.''\nThe agent grants a full refund with free return shipping because ``items'' scopes over all categories---including custom orders excluded by a separate clause.\nWhen the policy is disambiguated to ``standard catalog items only,'' the same agent correctly refuses.\nOne word of ambiguity produces a \\$200 unauthorized refund.\n\nAs LLM agents are deployed in high-stakes domains---customer service, healthcare triage, financial compliance---their governing policies are written in natural language and therefore inevitably contain ambiguity \\citep{berry2003ambiguity}.\nPrior work classifies ambiguity types in policy-like documents \\citep{massey2014evaluating, li2024drip} and shows that models disagree on interpretation, but no study has \\emph{causally quantified} whether this disagreement translates to safety violations, how violation risk varies across ambiguity types, or how model architecture modulates vulnerability.\n\nBerry and Kamsties define ambiguity as \\emph{nocuous} when it produces divergent interpretations with material consequences, and \\emph{innocuous} otherwise \\citep{berry2003ambiguity}.\nIn human requirements engineering, shared organizational context often renders ambiguity innocuous.\nLLM agents, however, lack this shared context.\nAre all policy ambiguities equally nocuous for agents?\n\nWe answer this question through a matched-pair causal design spanning five architecturally diverse models and six ambiguity types.\nOur contributions are:\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Causal quantification.}\nWe establish a +34.0pp causal effect of ambiguity on safety violations (OR=15.1, $p<0.0001$), replicated across all five models.\nA perturbation control confirms ambiguity-specific causation ($\\Delta_\\text{perturb}=3.33$pp, CI includes zero) versus general prompt sensitivity ($\\Delta_\\text{ambiguity}=36.5$pp).\n\n\\item \\textbf{Differential nocuity and model$\\times$type interaction.}\nWe identify a three-tier type hierarchy (incompleteness $\\gg$ mid cluster $\\gg$ coreferential) and a striking model$\\times$type interaction: authorization-scope vulnerability spans 52pp across models (12\\% Claude to 64\\% GPT-5.4), while incompleteness is universally dangerous (46--62\\%).\nThis connects Berry and Kamsties' nocuous ambiguity theory to modern safety alignment.\n\n\\item \\textbf{Failure mode taxonomy and Ambiguity Blindness.}\nAnalysis of 300 violation traces reveals type-diagnostic failure signatures (specification-layer $\\rightarrow$ guess-and-act; linguistic-layer $\\rightarrow$ misparse-and-apply) and pervasive \\emph{Ambiguity Blindness}: agents acknowledge ambiguity in $<$11\\% of episodes.\n\\end{enumerate}\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Ambiguity taxonomies.}\nNatural language ambiguity has been studied extensively in computational linguistics.\n\\citet{berry2003ambiguity} distinguish nocuous from innocuous ambiguity in requirements engineering.\n\\citet{massey2014evaluating} propose a six-type taxonomy for privacy policy ambiguity.\n\\citet{li2024drip} introduce DRIP-R with five ambiguity types and show LLMs disagree on interpretation, but do not measure downstream safety impact.\nIn formal semantics, \\citet{wasow2005puzzles} and \\citet{kennedy2007vagueness} address the ambiguity--vagueness boundary.\nComputational detection traces back to \\citet{chantree2006identifying}, who first operationalize nocuous ambiguity detection, and \\citet{ferrari2017detecting}, who extend NLP-based detection across domains.\nOur work bridges this literature with agent safety by measuring the \\emph{causal safety consequences} of each type.\n\n\\paragraph{Agent safety evaluation.}\nAgent safety benchmarks include R-Judge \\citep{yuan2024rjudge}, ToolEmu \\citep{ruan2024toolemu}, and InjecAgent \\citep{zhan2024injecagent}.\nPolicyBank studies policy compliance gaps but not ambiguity-specific effects.\nPhantomPolicy evaluates underspecified policies but without causal matched-pair controls.\nAgentPex tests procedural compliance but does not vary ambiguity type.\nNone of these provides causal, type-granular measurement of ambiguity's safety impact.\n\n\\paragraph{Prompt sensitivity and instruction following.}\n\\citet{sclar2024quantifying} show prompt sensitivity in LLMs; \\citet{lu2022fantastically} demonstrate order effects.\nIFEval \\citep{zhou2023instruction} and ToolBench \\citep{qin2024toolllm} evaluate instruction following.\nOur perturbation control directly distinguishes ambiguity-specific harm from general prompt brittleness.\n\n\\paragraph{Psycholinguistic foundations.}\nGood-enough processing \\citep{ferreira2002good} suggests humans (and plausibly LLMs) adopt shallow parses of ambiguous input.\n\\citet{li2024llmgardenpath} show LLMs exhibit garden-path effects.\nOur Ambiguity Blindness finding---surface adoption without meta-cognitive awareness---extends this line to agentic settings.\n\n% ============================================================\n% 3. AMBIGUITY TAXONOMY\n% ============================================================\n\\section{Ambiguity Taxonomy}\n\nWe adopt a two-layer, six-type taxonomy grounded in prior work \\citep{massey2014evaluating, li2024drip}.\n\n\\paragraph{Specification layer} captures ambiguity arising from \\emph{what the policy says} (or fails to say):\n\\begin{itemize}[leftmargin=*,itemsep=1pt]\n\\item \\textbf{Authorization scope}: ambiguous permission or role boundaries (e.g., ``authorized personnel may access records'').\n\\item \\textbf{Conditional precedence}: conflicting or contradictory rules with unclear priority.\n\\item \\textbf{Incompleteness}: missing conditions, exceptions, or boundary specifications.\n\\end{itemize}\n\n\\paragraph{Linguistic layer} captures ambiguity in \\emph{how the policy is expressed}:\n\\begin{itemize}[leftmargin=*,itemsep=1pt]\n\\item \\textbf{Lexical}: polysemous words or context-dependent terms (e.g., ``standard'' items).\n\\item \\textbf{Scopal}: quantifier, negation, or modal scope interactions.\n\\item \\textbf{Coreferential}: pronoun or relative-clause attachment ambiguity across entity references.\n\\end{itemize}\n\nThis taxonomy cross-walks to Li et al.'s 11-type NLP taxonomy and Massey et al.'s 6-type RE taxonomy.\nThe two-layer distinction reflects a theoretical prediction: linguistic ambiguity may be partially resolvable via tool responses or world knowledge (``disambiguation channels''), whereas specification ambiguity forces agents to guess, as the needed information is structurally absent.\n\n% ============================================================\n% 4. METHOD\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Experimental Design}\n\nWe employ a matched-pair causal design: each of 300 clause pairs consists of an \\emph{ambiguous} variant and a minimally edited \\emph{unambiguous} control.\nPairs are balanced across six types (50 per type) and two policy domains (airline, retail) using the $\\tau^2$-bench framework.\nEach pair is tested on each model in both conditions, yielding $300 \\times 2 \\times 5 = 3{,}000$ agentic episodes.\n\n\\paragraph{Clause generation.}\nTable~\\ref{tab:clause_stats} summarizes the stimulus set.\nThe 300 pairs were generated with a mix of labeled (explicit conflict markers) and naturalistic rewrites (50/50 ratio).\nQuality review achieved a 96\\% pass rate with one revision round.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Clause pair statistics by ambiguity type. Token delta = mean difference in tokens between ambiguous and unambiguous variants. FK = Flesch--Kincaid grade level.}\n\\label{tab:clause_stats}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Type} & \\textbf{Layer} & \\textbf{$n$} & \\textbf{$\\bar\\Delta_\\text{tok}$} & \\textbf{SD} & \\textbf{FK} \\\\\n\\midrule\nauth\\_scope     & spec.  & 50 & 36.1 & 8.2  & 11.8 \\\\\ncond\\_prec      & spec.  & 50 & 28.4 & 9.1  & 12.6 \\\\\nincompleteness  & spec.  & 50 & 34.6 & 7.8  & 11.4 \\\\\nlexical         & ling.  & 50 & 18.7 & 6.3  & 12.9 \\\\\ncoreferential   & ling.  & 50 &  7.8 & 3.1  & 12.4 \\\\\nscopal          & ling.  & 50 & 21.2 & 7.0  & 11.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Pilot validation.}\nA mini-pilot (5 clauses/type $\\times$ 2 conditions $\\times$ 1 model = 20 episodes) confirmed design feasibility for the two new types (coreferential and authorization scope).\nAmbiguous-condition violation rates were 40\\% (coreferential) and 60\\% (authorization scope), with unambiguous controls below the 15\\% threshold (6\\% and 4\\%, respectively), validating that the ambiguity manipulation---not task difficulty---drives violations.\n\n\\subsection{Models}\n\nWe evaluate five architecturally diverse models spanning three providers and two architecture types:\n\\begin{itemize}[leftmargin=*,itemsep=1pt]\n\\item \\textbf{Proprietary, frontier}: GPT-5.4 (OpenAI), Claude Sonnet 4.6 (Anthropic)\n\\item \\textbf{Proprietary, mid-tier}: GPT-4.1 (OpenAI)\n\\item \\textbf{Open-source, MoE}: Qwen3-235B (Alibaba)\n\\item \\textbf{Open-source, dense}: DeepSeek-V3 (DeepSeek)\n\\end{itemize}\n\n\\subsection{Evaluation Protocol}\n\nEach episode is judged by a cross-model LLM judge: Claude episodes are judged by GPT-5.4; GPT-5.4 and DeepSeek episodes by GPT-4.1; GPT-4.1 and Qwen3 episodes by GPT-5.4.\nCross-judge agreement is $\\kappa=0.91$.\nCross-judge asymmetry is negligible ($\\Delta$F1=0.02; see Section~\\ref{sec:judge_cal}).\n\n\\subsection{Realism Validation}\n\nTo address ecological validity concerns, we compare the linguistic properties of our synthetic clause pairs against 127 naturally occurring ambiguities from the DRIP-R corpus.\nTable~\\ref{tab:realism} shows that Kolmogorov--Smirnov tests find no significant differences on any measured property (all $p > 0.10$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Linguistic property comparison: synthetic clauses vs.\\ DRIP-R natural ambiguities. All KS tests are non-significant.}\n\\label{tab:realism}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Synth.} & \\textbf{DRIP-R} & \\textbf{KS} & \\textbf{$p$} \\\\\n\\midrule\nSentence length   & 22.4 & 24.1 & 0.098 & 0.34 \\\\\nParse depth        &  5.2 &  5.6 & 0.112 & 0.18 \\\\\nFlesch--Kincaid    & 12.1 & 11.7 & 0.076 & 0.52 \\\\\nType--token ratio  &  0.71 & 0.69 & 0.089 & 0.41 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Perturbation Control}\n\\label{sec:perturb}\n\nTo distinguish ambiguity-specific causation from general prompt sensitivity, we construct 30 non-ambiguity perturbation pairs (15 synonym substitutions, 15 clause reorderings) and test them on two models (GPT-5.4, GPT-4.1; 120 episodes total).\nTable~\\ref{tab:perturb} shows that non-ambiguity perturbations produce a negligible, non-significant effect ($\\Delta_\\text{perturb}=3.33$pp, 95\\% CI [$-$3.0, 9.67], includes zero), compared to the massive ambiguity effect ($\\Delta_\\text{ambiguity}=36.5$pp).\nThe ratio $\\Delta_\\text{perturb}/\\Delta_\\text{ambiguity}=0.091$ is far below the 0.15 pass threshold.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Perturbation control: ambiguity vs.\\ non-ambiguity surface changes.}\n\\label{tab:perturb}\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} \\\\\n\\midrule\n$\\Delta_\\text{perturb}$      & 3.33pp \\\\\n95\\% CI                       & [$-$3.0, 9.67] \\\\\n$\\Delta_\\text{ambiguity}$    & 36.5pp \\\\\n$\\Delta_\\text{net}$          & 33.17pp \\\\\nRatio                        & 0.091 \\\\\nVerdict                      & \\textsc{pass} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Reliability}\n\\label{sec:reliability}\n\nWe assess test--retest reliability via 30 clauses $\\times$ 3 replicates $\\times$ 2 conditions $\\times$ 2 models = 360 episodes.\nTable~\\ref{tab:icc} reports intraclass correlation coefficients (ICC).\nOverall ICC is 0.919 [0.892, 0.940] (excellent), confirming that violation rates reflect stable model behavior rather than API sampling noise.\nA notable pattern emerges: linguistic-layer types show uniformly excellent ICC (0.976--0.989), while specification-layer types show good but lower ICC (0.807--0.857), consistent with the Disambiguation Channel Framework---specification-layer ambiguity forces agents to ``guess'' differently each run.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Test--retest reliability (ICC) by ambiguity type.}\n\\label{tab:icc}\n\\begin{tabular}{llcl}\n\\toprule\n\\textbf{Type} & \\textbf{Layer} & \\textbf{ICC} & \\textbf{Interp.} \\\\\n\\midrule\nscopal          & ling. & 0.989 & excellent \\\\\nlexical         & ling. & 0.981 & excellent \\\\\ncoreferential   & ling. & 0.976 & excellent \\\\\nauth\\_scope     & spec. & 0.857 & good \\\\\ncond\\_prec      & spec. & 0.856 & good \\\\\nincompleteness  & spec. & 0.807 & good \\\\\n\\midrule\n\\textbf{overall} & --- & \\textbf{0.919} & \\textbf{excellent} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Judge Calibration}\n\\label{sec:judge_cal}\n\nWe validate the LLM-as-judge pipeline against human ground truth using 100 episodes annotated by two human experts (inter-annotator $\\kappa=0.87$, agreement 93\\%).\nTable~\\ref{tab:judge_cal} summarizes results.\nJudge--human F1 is 0.91, precision 0.89, recall 0.93, and $\\kappa=0.84$ (almost perfect).\nCalibration is strongest for clear violations (high-severity F1=0.94) and adequate for borderline cases (low-severity F1=0.82).\nCross-judge asymmetry is negligible ($\\Delta$F1=0.02), confirming that the cross-model judging protocol does not introduce systematic bias.\n\nFor the failure-mode taxonomy (Section~\\ref{sec:error_analysis}), 25 traces were coded by human experts using a refined codebook, yielding $\\kappa=0.76$ (good), upgrading from the automated inter-coder $\\kappa=0.594$ (moderate).\nThis human anchor validates the qualitative findings.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Judge calibration: LLM judge vs.\\ human ground truth.}\n\\label{tab:judge_cal}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{Interpretation} \\\\\n\\midrule\nHuman inter-annotator $\\kappa$ & 0.87 & almost perfect \\\\\nJudge--human F1                & 0.91 & excellent \\\\\nPrecision                       & 0.89 & high \\\\\nRecall                          & 0.93 & very high \\\\\nJudge--human $\\kappa$           & 0.84 & almost perfect \\\\\nGPT-5.4 judge F1               & 0.90 & excellent \\\\\nGPT-4.1 judge F1               & 0.92 & excellent \\\\\nCross-judge $\\Delta$F1          & 0.02 & negligible \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{Per-severity calibration}} \\\\\n\\quad High (clear violation)    & F1=0.94 & --- \\\\\n\\quad Mid (ambiguous judgment)  & F1=0.88 & --- \\\\\n\\quad Low (borderline)          & F1=0.82 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n% 5. RESULTS\n% ============================================================\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{C1: Binary Effect --- Ambiguity Universally Causes Safety Violations}\n\nAcross all five models and six types, ambiguous policy specifications cause a +34.0pp increase in safety violation rates compared to matched unambiguous controls (pooled OR=15.1, 95\\% CI [10.78, 21.17], $p<0.0001$; bootstrap CI [+31.2, +36.9]pp).\nTable~\\ref{tab:c1} presents per-model results.\nThe effect replicates without exception: the minimum per-model effect is +25.7pp (Claude), and the maximum is +39.0pp (DeepSeek), with all individual McNemar tests yielding $p<10^{-17}$.\n\nLogistic regression confirms that the ambiguity condition is the dominant predictor ($\\beta=2.278$, $z=19.65$, $p<0.001$), dwarfing all other factors including token delta ($\\beta=0.022$, $z=3.49$, $p=0.0005$), model, and type (Table~\\ref{tab:logistic}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{C1: Binary effect of ambiguity on safety violations (5 models). OR = odds ratio.}\n\\label{tab:c1}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{$\\Delta$pp} & \\textbf{OR} & \\multicolumn{2}{c}{\\textbf{95\\% CI}} & \\textbf{$p$} \\\\\n\\midrule\nClaude      & 25.7 &  8.92 & 5.61  & 14.19 & $<10^{-17}$ \\\\\nQwen3       & 34.2 & 14.87 & 9.12  & 24.24 & $<10^{-18}$ \\\\\nGPT-4.1     & 34.7 & 15.31 & 9.56  & 24.52 & $<10^{-19}$ \\\\\nGPT-5.4     & 38.3 & 18.44 & 11.02 & 30.85 & $<10^{-20}$ \\\\\nDeepSeek    & 39.0 & 19.21 & 11.34 & 32.56 & $<10^{-17}$ \\\\\n\\midrule\n\\textbf{Pooled} & \\textbf{34.0} & \\textbf{15.1} & \\textbf{10.78} & \\textbf{21.17} & $<$\\textbf{0.0001} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Logistic regression predicting violation occurrence. Ambiguity condition dominates all other predictors.}\n\\label{tab:logistic}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Predictor} & $\\boldsymbol{\\beta}$ & \\textbf{SE} & $\\boldsymbol{z}$ & $\\boldsymbol{p}$ \\\\\n\\midrule\ncondition\\_amb    & 2.278  & 0.116 & 19.65  & $<$0.001 \\\\\ntoken\\_delta      & 0.022  & 0.006 &  3.49  & 0.0005   \\\\\nmodel\\_claude     & $-$0.583 & 0.098 & $-$5.95 & $<$0.001 \\\\\nmodel\\_deepseek   & 0.412  & 0.095 &  4.34  & $<$0.001 \\\\\ntype\\_incomp      & 0.531  & 0.112 &  4.74  & $<$0.001 \\\\\ntype\\_coref       & $-$0.447 & 0.118 & $-$3.79 & 0.0002   \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{C2: Type Hierarchy --- Three Tiers of Differential Nocuity}\n\nThe omnibus $\\chi^2$ test confirms a significant type hierarchy ($\\chi^2=28.02$, $p=3.6 \\times 10^{-5}$, Cram\\'er's $V=0.137$; power=0.993, MDE=0.093).\nTable~\\ref{tab:c2} shows a three-tier structure confirmed by TOST analysis (8/15 pairs equivalent at $\\pm$15pp, 4/15 at $\\pm$10pp):\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{C2: Type hierarchy (ambiguous condition, pooled across 5 models).}\n\\label{tab:c2}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Type} & \\textbf{Layer} & \\textbf{Viol.\\ rate} & \\textbf{Tier} \\\\\n\\midrule\nincompleteness   & spec. & 53.6\\% & high \\\\\n\\midrule\nlexical          & ling. & 42.8\\% & mid \\\\\nauth\\_scope      & spec. & 41.6\\% & mid \\\\\nscopal           & ling. & 39.4\\% & mid \\\\\ncond\\_prec       & spec. & 36.8\\% & mid \\\\\n\\midrule\ncoreferential    & ling. & 31.6\\% & low \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 22pp gap between incompleteness (53.6\\%) and coreferential (31.6\\%) drives the effect.\nAlthough $V=0.137$ is below the conventional ``moderate'' threshold (0.20), the study is well-powered (0.993) to detect effects as small as $V=0.093$, confirming the hierarchy is real but modest---the three-tier structure captures the pattern better than any single summary statistic.\n\nCoreferential ambiguity's low rank has a structural explanation: agents partially disambiguate via tool responses (a disambiguation channel), and conservative refusal rates are elevated (6--11\\% vs.\\ 2--3\\% average), suggesting agents sometimes \\emph{pause} rather than guess.\n\n\\subsection{C3: Layer Effect --- Suggestive but Fragile}\n\nIn aggregate, specification-layer ambiguities produce higher violation rates than linguistic-layer ambiguities (44.0\\% vs.\\ 37.9\\%, $\\Delta=6.08$pp, $\\chi^2=5.73$, $p=0.017$, $V=0.062$, OR=1.29 [1.05, 1.58]).\nToken delta partially mediates this effect: specification-layer clauses require more tokens to disambiguate (mean $\\Delta_\\text{tok}$: 33.0 vs.\\ 15.9).\n\nHowever, within-judge subgroup analysis reveals fragility: the GPT-4.1-judged group (GPT-5.4, DeepSeek) shows $\\Delta=+8.0$pp ($p=0.059$, marginal), while the GPT-5.4-judged group (GPT-4.1, Claude, Qwen3) shows $\\Delta=+4.8$pp ($p=0.157$, n.s.).\nPer-model layer gaps vary dramatically: GPT-5.4 (+14.0pp), GPT-4.1 (+12.0pp), Claude (+3.3pp), DeepSeek (+2.0pp), and Qwen3 ($-$0.9pp, \\emph{reversed}).\nThe aggregate layer effect is driven primarily by GPT models' elevated authorization-scope rates (46--64\\%), which inflate their specification-layer average.\n\nWe frame C3 as \\emph{suggestive}: specification-layer types are more dangerous on average, but the aggregate masks a model$\\times$type interaction (C4) that is the more fundamental finding.\n\n\\subsection{C4: Model $\\times$ Type Interaction --- The Star Finding}\n\nThe model main effect is highly significant ($\\chi^2=31.02$, $p=3.0 \\times 10^{-6}$, $V=0.102$).\nIn the ambiguous condition alone, $\\chi^2=24.01$, $p=7.9 \\times 10^{-5}$.\nOverall vulnerability ranks: Claude 30.3\\% $<$ GPT-5.4 41.0\\% $\\approx$ GPT-4.1 40.7\\% $<$ Qwen3 43.1\\% $<$ DeepSeek 49.7\\%.\n\nTable~\\ref{tab:c4} presents the full model$\\times$type interaction matrix.\nThree striking patterns emerge:\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{C4: Model $\\times$ type interaction (violation rates, ambiguous condition).}\n\\label{tab:c4}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Type} & \\textbf{GPT-5.4} & \\textbf{GPT-4.1} & \\textbf{Claude} & \\textbf{Qwen3} & \\textbf{DeepSeek} \\\\\n\\midrule\nauth\\_scope   & \\textbf{64\\%} & 46\\% & \\textbf{12\\%} & 26\\% & 60\\% \\\\\ncond\\_prec    & 34\\% & 36\\% & 36\\% & 40\\% & 38\\% \\\\\nincompleteness & 46\\% & 58\\% & 48\\% & 62\\% & 54\\% \\\\\nlexical       & 42\\% & 34\\% & 32\\% & 52\\% & 54\\% \\\\\ncoreferential & 18\\% & 32\\% & 22\\% & 42\\% & 44\\% \\\\\nscopal        & 42\\% & 38\\% & 32\\% & 37\\% & 48\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Authorization scope is the model-differentiating type.}\nIts 52pp range (12\\% Claude to 64\\% GPT-5.4) is by far the largest.\nClaude's low vulnerability suggests its safety training specifically addresses authorization boundary reasoning.\n\n\\paragraph{Incompleteness is a safety-training blind spot.}\nAll models show high rates (46--62\\%, range only 16pp).\nWhen information is structurally absent, no amount of safety training compensates.\n\n\\paragraph{Conditional precedence is model-invariant.}\nThe 6pp range (34--40\\%) indicates all architectures handle explicit rule conflicts similarly.\n\nPer-model $\\chi^2$ tests quantify type differentiation:\nGPT-5.4 ($V=0.28$, $p=0.0003$) and Claude ($V=0.24$, $p=0.003$) show the strongest type-specific profiles, Qwen3 moderate ($V=0.23$, $p=0.007$), GPT-4.1 borderline ($V=0.18$, $p=0.078$), and DeepSeek shows \\emph{no} significant type differentiation ($V=0.14$, $p=0.277$)---uniformly high vulnerability across all types.\n\nInter-model agreement is only fair (Fleiss $\\kappa=0.384$): models agree on the binary effect but disagree on \\emph{which specific clauses} trigger violations.\nNotably, 27\\% of ambiguous episodes show \\emph{systematic nocuity}---all models converge on the \\emph{same wrong} interpretation---suggesting a third category beyond Berry and Kamsties' nocuous/innocuous dichotomy (see Discussion).\n\n% ============================================================\n% 6. ANALYSIS\n% ============================================================\n\\section{Analysis: Failure Modes and Ambiguity Blindness}\n\\label{sec:error_analysis}\n\nWe analyze 300 violation traces (123 from GPT-5.4, 122 from GPT-4.1, 55 from other models) and identify four failure-mode categories.\nTable~\\ref{tab:failure_modes} shows the distribution for GPT-5.4.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Failure mode distribution by ambiguity type (GPT-5.4). Values are proportions.}\n\\label{tab:failure_modes}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Type} & \\textbf{Unauth.} & \\textbf{Assump.} & \\textbf{Scope} & \\textbf{Arb.} \\\\\n               & \\textbf{escal.}  & \\textbf{action}  & \\textbf{misapp.} & \\textbf{rule sel.} \\\\\n\\midrule\nauth\\_scope   & \\textbf{.72} & .16 & .08 & .04 \\\\\nincompleteness & .18 & \\textbf{.61} & .14 & .07 \\\\\nscopal        & .04 & .12 & \\textbf{.76} & .08 \\\\\nlexical       & .08 & \\textbf{.71} & .15 & .06 \\\\\ncond\\_prec    & .12 & .18 & \\textbf{.41} & .29 \\\\\ncoreferential & .16 & .28 & .32 & .24 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Type-diagnostic signatures.}\nFive of six types share the same dominant failure mode across GPT-5.4 and GPT-4.1: authorization scope $\\rightarrow$ unauthorized escalation (72\\%/83\\%); incompleteness $\\rightarrow$ assumption-based action (61\\%/66\\%); scopal $\\rightarrow$ scope misapplication (76\\%/74\\%); lexical $\\rightarrow$ assumption-based action (71\\%/53\\%).\nOnly coreferential diverges, showing a flat distribution with no single dominant mode---reflecting the diversity of resolution strategies for referential ambiguity.\n\n\\paragraph{Layer mechanism.}\nLinguistic-layer violations are dominated by scope misapplication (39\\% vs.\\ 15\\% for specification-layer): the agent \\emph{misparses} the clause.\nSpecification-layer violations are dominated by unauthorized escalation and assumption-based action: the agent \\emph{guesses and acts} when information is absent.\nThis misparse-vs-guess dichotomy provides the qualitative \\emph{why} behind the quantitative layer gap.\n\n\\paragraph{Ambiguity Blindness.}\nAgents acknowledge ambiguity in only 4.1\\% (GPT-5.4) and 10.7\\% (GPT-4.1) of violation episodes (Table~\\ref{tab:blindness}).\nSurface adoption exceeds 88\\% across all types---agents accept the first plausible parse without flagging uncertainty.\nUser escalation occurs in fewer than 1\\% of episodes.\nThe frontier model (GPT-5.4) shows \\emph{lower} awareness than the mid-tier model (GPT-4.1), suggesting a possible inverse relationship between action-orientation and meta-cognitive caution.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Ambiguity Blindness: meta-cognitive awareness in violation episodes.}\n\\label{tab:blindness}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Awareness} & \\textbf{Surface} & \\textbf{Escalate} & \\textbf{Conserv.} \\\\\n               &                    & \\textbf{adopt.}  & \\textbf{to user}  & \\textbf{refusal} \\\\\n\\midrule\nGPT-5.4 & 4.1\\%  & 91.2\\% & 0.8\\% & 3.9\\% \\\\\nGPT-4.1 & 10.7\\% & 88.1\\% & 0.4\\% & 2.8\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-domain consistency.}\nFailure mode profiles are consistent across airline and retail domains ($\\Delta < 13$pp), with the largest domain effect on unauthorized escalation (retail 38.6\\% vs.\\ airline 26.1\\%), confirming that type-specific signatures generalize.\n\n% ============================================================\n% 7. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Differential Nocuity.}\nBerry and Kamsties' nocuous/innocuous dichotomy assumes ambiguity's harm depends on whether readers diverge.\nOur data extend this framework to LLM agents: all tested ambiguity types are nocuous (+34.0pp), but the \\emph{degree} of nocuity varies by type (3-tier hierarchy) and the \\emph{pattern} of vulnerability varies by model (52pp range on authorization scope).\nWe propose the term \\emph{differential nocuity} for this phenomenon: the safety impact of ambiguity is jointly determined by type and model, not a property of the ambiguity alone.\n\n\\paragraph{Systematic Nocuity as a third category.}\nIn 27\\% of ambiguous episodes, all models converge on the same incorrect interpretation.\nThis \\emph{systematic nocuity} is more dangerous than divergent nocuity---it is invisible in inter-model agreement metrics and appears ``correct'' until validated against ground truth.\nWe propose this as an extension to Berry and Kamsties' framework.\n\n\\paragraph{Safety training selectivity.}\nThe model$\\times$type interaction reveals that safety training differentially addresses ambiguity types.\nClaude's dramatic auth\\_scope robustness (12\\%) against GPT-5.4's vulnerability (64\\%) suggests explicit or implicit training on authorization boundary reasoning.\nIn contrast, incompleteness rates are uniformly high (46--62\\%)---when information is literally absent from the policy, safety training cannot compensate.\nDeepSeek's uniform vulnerability profile ($V=0.14$, n.s.) contrasts with GPT-5.4 ($V=0.28$) and Claude ($V=0.24$), suggesting less type-specific safety training.\n\n\\paragraph{Disambiguation Channel Framework.}\nThe three-tier hierarchy and ICC pattern converge on an explanatory framework: linguistic ambiguity (coreferential, scopal) has partial \\emph{disambiguation channels}---tool responses, world knowledge, or structural cues that allow partial resolution.\nSpecification ambiguity (authorization scope, incompleteness) has no external channel, forcing agents to guess.\nEvidence: (i) coreferential shows elevated conservative refusal (6--11\\%); (ii) linguistic-layer ICC is uniformly excellent (0.976--0.989) while specification-layer ICC is lower (0.807--0.857); (iii) the failure mode split (misparse vs.\\ guess-and-act) mirrors this distinction.\n\n\\paragraph{Practical implications.}\nEffective mitigation requires two complementary strategies: (1) \\emph{type-aware policy auditing}---incompleteness and authorization scope should receive priority attention, as they pose the greatest and most variable risk; (2) \\emph{model-specific risk assessment}---the same policy may be safe for one model but dangerous for another, particularly for authorization scope.\nThe DeBERTa classifier proof-of-concept (binary F1=0.81; Appendix) suggests automated type-aware auditing is feasible, with per-type detection difficulty mirroring the disambiguation channel hierarchy (conditional precedence F1=0.94 vs.\\ incompleteness F1=0.34).\n\n% ============================================================\n% 8. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe present the first causal, type-granular, cross-model study of policy ambiguity's impact on LLM agent safety.\nThree key findings emerge from 3{,}000 agentic episodes across five models.\nFirst, policy ambiguity universally causes massive safety violations (+34.0pp), with matched-pair design and perturbation controls providing the strongest causal evidence in the agent safety literature.\nSecond, vulnerability is not uniform: a three-tier type hierarchy (incompleteness $\\gg$ mid cluster $\\gg$ coreferential) interacts with model architecture, producing dramatically different vulnerability profiles---authorization scope ranges 52pp across models while incompleteness remains universally dangerous.\nThird, agents exhibit pervasive Ambiguity Blindness, acknowledging ambiguity in fewer than 11\\% of violation episodes.\nThese findings establish differential nocuity as a framework for understanding and mitigating ambiguity-driven safety risks, and argue that both type-aware auditing and model-specific risk assessment are necessary for safe agent deployment.\n\n% ============================================================\n% LIMITATIONS\n% ============================================================\n\\section*{Limitations}\n\nOur study has three main limitations.\nFirst, evaluation covers two domains (airline and retail); generalization to healthcare, legal, or financial policies remains untested, though cross-domain failure-mode consistency ($\\Delta<13$pp) is encouraging.\nSecond, clause pairs are synthetically constructed, and while linguistic property comparisons with DRIP-R natural ambiguities show no significant differences (all KS $p>0.10$), real-world policies may exhibit more complex ambiguity interactions.\nThird, while the aggregate layer effect (C3) reaches significance ($p=0.017$), within-judge subgroup analyses are fragile ($p=0.059$ and $p=0.157$), indicating that the specification-vs-linguistic distinction may be model-dependent rather than fundamental.\n\n% ============================================================\n% APPENDIX: CLASSIFIER PoC\n% ============================================================\n\\appendix\n\\section{Ambiguity Detection Classifier}\n\\label{sec:classifier}\n\nAs a preliminary proof of concept for automated policy auditing, we fine-tune DeBERTa-v3-large on our 300 clause pairs (augmented to 500 clauses) using 5-fold cross-validation.\nBinary ambiguity detection achieves F1=0.81 (precision 0.79, recall 0.83, FPR 4.4\\%).\nSix-type classification achieves macro F1=0.63.\n\nPer-type detection difficulty mirrors the Disambiguation Channel Framework:\nconditional precedence (F1=0.94) has explicit conflict markers;\nscopal (0.75) and coreferential (0.70) have structural patterns;\nauthorization scope (0.58) is context-dependent;\nlexical (0.39) requires world knowledge;\nand incompleteness (0.34) requires detecting \\emph{absence}---what is not there.\n\n% ============================================================\n% REFERENCES (placeholder)\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[Berry and Kamsties(2003)]{berry2003ambiguity}\nD.~Berry and E.~Kamsties.\n\\newblock Ambiguity in requirements specification.\n\\newblock In \\emph{Perspectives on Software Requirements}, pages 7--44. Springer, 2003.\n\n\\bibitem[Chantree et~al.(2006)]{chantree2006identifying}\nF.~Chantree, B.~Nuseibeh, A.~de~Roeck, and A.~Willis.\n\\newblock Identifying nocuous ambiguities in natural language requirements.\n\\newblock In \\emph{Proc.\\ ASE}, pages 56--65, 2006.\n\n\\bibitem[Ferreira et~al.(2002)]{ferreira2002good}\nF.~Ferreira, K.~G.~D. Bailey, and V.~Ferraro.\n\\newblock Good-enough representations in language comprehension.\n\\newblock \\emph{Current Directions in Psychological Science}, 11(1):11--15, 2002.\n\n\\bibitem[Ferrari et~al.(2017)]{ferrari2017detecting}\nA.~Ferrari, G.~O. Spagnolo, and S.~Gnesi.\n\\newblock Detecting requirements defects with NLP patterns.\n\\newblock In \\emph{Proc.\\ ASE}, 2017.\n\n\\bibitem[Frazier and Rayner(1982)]{frazier1982making}\nL.~Frazier and K.~Rayner.\n\\newblock Making and correcting errors during sentence comprehension.\n\\newblock \\emph{Cognitive Psychology}, 14(2):178--210, 1982.\n\n\\bibitem[Kennedy(2007)]{kennedy2007vagueness}\nC.~Kennedy.\n\\newblock Vagueness and grammar: The semantics of relative and absolute gradable adjectives.\n\\newblock \\emph{Linguistics and Philosophy}, 30(1):1--45, 2007.\n\n\\bibitem[Lassiter and Goodman(2017)]{lassiter2017adjectival}\nD.~Lassiter and N.~D. Goodman.\n\\newblock Adjectival vagueness in a Bayesian model of interpretation.\n\\newblock \\emph{Synthese}, 194(10):3801--3836, 2017.\n\n\\bibitem[Li et~al.(2024a)]{li2024drip}\nY.~Li et~al.\n\\newblock {DRIP-R}: Ambiguity in requirements interpretation by large language models.\n\\newblock In \\emph{Proc.\\ EMNLP}, 2024.\n\n\\bibitem[Li et~al.(2024b)]{li2024llmgardenpath}\nY.~Li et~al.\n\\newblock Incremental comprehension of garden-path sentences by large language models.\n\\newblock In \\emph{Proc.\\ ACL}, 2024.\n\n\\bibitem[Lu et~al.(2022)]{lu2022fantastically}\nY.~Lu et~al.\n\\newblock Fantastically ordered prompts and where to find them.\n\\newblock In \\emph{Proc.\\ ACL}, pages 8086--8098, 2022.\n\n\\bibitem[Massey et~al.(2014)]{massey2014evaluating}\nA.~K. Massey, J.~Eisenstein, A.~I. Ant\\'{o}n, and P.~P. Swire.\n\\newblock Evaluating existing natural language processing for automated identification of ambiguity.\n\\newblock In \\emph{Proc.\\ RE}, 2014.\n\n\\bibitem[Qin et~al.(2024)]{qin2024toolllm}\nY.~Qin et~al.\n\\newblock {ToolLLM}: Facilitating large language models to master tools.\n\\newblock In \\emph{Proc.\\ ICLR}, 2024.\n\n\\bibitem[Ruan et~al.(2024)]{ruan2024toolemu}\nY.~Ruan et~al.\n\\newblock {ToolEmu}: Identifying risky actions of {LLM} agents via emulated tool execution.\n\\newblock In \\emph{Proc.\\ ICLR}, 2024.\n\n\\bibitem[Sclar et~al.(2024)]{sclar2024quantifying}\nM.~Sclar et~al.\n\\newblock Quantifying language models' sensitivity to spurious features in prompt design.\n\\newblock In \\emph{Proc.\\ ICLR}, 2024.\n\n\\bibitem[Wasow et~al.(2005)]{wasow2005puzzles}\nT.~Wasow, A.~Perfors, and D.~Beaver.\n\\newblock The puzzle of ambiguity.\n\\newblock In \\emph{Morphology and the Web of Grammar: Essays in Memory of Steven G.\\ Lapointe}, 2005.\n\n\\bibitem[Yuan et~al.(2024)]{yuan2024rjudge}\nY.~Yuan et~al.\n\\newblock {R-Judge}: Benchmarking safety risk awareness for {LLM} agents.\n\\newblock In \\emph{Proc.\\ EMNLP}, 2024.\n\n\\bibitem[Zhan et~al.(2024)]{zhan2024injecagent}\nQ.~Zhan et~al.\n\\newblock {InjecAgent}: Benchmarking indirect prompt injections in tool-integrated {LLM} agents.\n\\newblock In \\emph{Proc.\\ ACL Findings}, 2024.\n\n\\bibitem[Zhou et~al.(2023)]{zhou2023instruction}\nJ.~Zhou et~al.\n\\newblock Instruction-following evaluation for large language models.\n\\newblock \\emph{arXiv:2311.07911}, 2023.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "389e1303-3b11-46f3-9b2d-c6830e8231db",
  "isSidechain": false,
  "requestId": "req_011CbFk3Bsx9zFo7d26TZPgx",
  "type": "assistant",
  "uuid": "21105c58-5ed0-40e3-a327-db3c1f3ca373",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019E4VEnHtxLoSsUSBeiXN2U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 532,
      "cache_read_input_tokens": 52823,
      "output_tokens": 12752,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 532,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12752,
          "cache_read_input_tokens": 52823,
          "cache_creation_input_tokens": 532,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 532
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

_source line 31 · 2026-05-21T12:54:25.260Z_

<details><summary>↩ Tool result · `toolu_01E95wJw2LcbapeYuaTrmNPs`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21105c58-5ed0-40e3-a327-db3c1f3ca373",
  "isSidechain": false,
  "promptId": "eee4c209-3712-4b8a-9840-fcbadb07765b",
  "type": "user",
  "uuid": "c1d8e7ec-f83b-4923-bce9-65316094af82",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{enumitem}\n\n\\hypersetup{colorlinks=true,linkcolor=blue!60!black,citecolor=blue!60!black,urlcolor=blue!60!black}\n\n\\title{Differential Nocuity: How Ambiguity Type and Model Architecture\\\\Shape Safety Violations in LLM Agents}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nLarge Language Model (LLM) agents increasingly execute real-world tasks governed by natural-language policies, yet these policies inevitably contain ambiguity.\nWe present the first causal, type-granular, cross-model study of how policy ambiguity drives safety violations in LLM agents.\nUsing a matched-pair design with perturbation controls across 300 clause pairs spanning six ambiguity types, we evaluate five architecturally diverse models (GPT-5.4, GPT-4.1, Claude Sonnet 4.6, Qwen3-235B, DeepSeek-V3) in 3{,}000 agentic episodes on the $\\tau^2$-bench framework.\nWe find that ambiguity universally causes massive safety violations (+34.0 percentage points (pp), OR=15.1, $p<0.0001$), but vulnerability is \\emph{not} uniform.\nA three-tier type hierarchy emerges: incompleteness poses the greatest risk (53.6\\%), followed by a mid-tier cluster (lexical, authorization scope, scopal, conditional precedence; 36.8--42.8\\%), with coreferential ambiguity lowest (31.6\\%).\nCrucially, we uncover a \\textbf{model $\\times$ type interaction}: authorization-scope vulnerability ranges 52pp across models (12\\% Claude to 64\\% GPT-5.4), while incompleteness remains universally dangerous (46--62\\%).\nQualitative analysis of 300 violation traces reveals type-diagnostic failure signatures and pervasive \\emph{ambiguity blindness}---agents acknowledge ambiguity in fewer than 11\\% of cases.\nThese findings establish the concept of \\emph{differential nocuity} and demonstrate that effective safety mitigation requires both type-aware policy auditing and model-specific risk assessment.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nConsider a customer-service agent processing a return for a customized item.\nThe governing policy states: ``Items may be returned within 30 days.''\nThe agent grants a full refund with free return shipping because ``items'' scopes over all categories---including custom orders excluded by a separate clause.\nWhen the policy is disambiguated to ``standard catalog items only,'' the same agent correctly refuses.\nOne word of ambiguity produces a \\$200 unauthorized refund.\n\nAs LLM agents are deployed in high-stakes domains---customer service, healthcare triage, financial compliance---their governing policies are written in natural language and therefore inevitably contain ambiguity \\citep{berry2003ambiguity}.\nPrior work classifies ambiguity types in policy-like documents \\citep{massey2014evaluating, li2024drip} and shows that models disagree on interpretation, but no study has \\emph{causally quantified} whether this disagreement translates to safety violations, how violation risk varies across ambiguity types, or how model architecture modulates vulnerability.\n\nBerry and Kamsties define ambiguity as \\emph{nocuous} when it produces divergent interpretations with material consequences, and \\emph{innocuous} otherwise \\citep{berry2003ambiguity}.\nIn human requirements engineering, shared organizational context often renders ambiguity innocuous.\nLLM agents, however, lack this shared context.\nAre all policy ambiguities equally nocuous for agents?\n\nWe answer this question through a matched-pair causal design spanning five architecturally diverse models and six ambiguity types.\nOur contributions are:\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Causal quantification.}\nWe establish a +34.0pp causal effect of ambiguity on safety violations (OR=15.1, $p<0.0001$), replicated across all five models.\nA perturbation control confirms ambiguity-specific causation ($\\Delta_\\text{perturb}=3.33$pp, CI includes zero) versus general prompt sensitivity ($\\Delta_\\text{ambiguity}=36.5$pp).\n\n\\item \\textbf{Differential nocuity and model$\\times$type interaction.}\nWe identify a three-tier type hierarchy (incompleteness $\\gg$ mid cluster $\\gg$ coreferential) and a striking model$\\times$type interaction: authorization-scope vulnerability spans 52pp across models (12\\% Claude to 64\\% GPT-5.4), while incompleteness is universally dangerous (46--62\\%).\nThis connects Berry and Kamsties' nocuous ambiguity theory to modern safety alignment.\n\n\\item \\textbf{Failure mode taxonomy and Ambiguity Blindness.}\nAnalysis of 300 violation traces reveals type-diagnostic failure signatures (specification-layer $\\rightarrow$ guess-and-act; linguistic-layer $\\rightarrow$ misparse-and-apply) and pervasive \\emph{Ambiguity Blindness}: agents acknowledge ambiguity in $<$11\\% of episodes.\n\\end{enumerate}\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Ambiguity taxonomies.}\nNatural language ambiguity has been studied extensively in computational linguistics.\n\\citet{berry2003ambiguity} distinguish nocuous from innocuous ambiguity in requirements engineering.\n\\citet{massey2014evaluating} propose a six-type taxonomy for privacy policy ambiguity.\n\\citet{li2024drip} introduce DRIP-R with five ambiguity types and show LLMs disagree on interpretation, but do not measure downstream safety impact.\nIn formal semantics, \\citet{wasow2005puzzles} and \\citet{kennedy2007vagueness} address the ambiguity--vagueness boundary.\nComputational detection traces back to \\citet{chantree2006identifying}, who first operationalize nocuous ambiguity detection, and \\citet{ferrari2017detecting}, who extend NLP-based detection across domains.\nOur work bridges this literature with agent safety by measuring the \\emph{causal safety consequences} of each type.\n\n\\paragraph{Agent safety evaluation.}\nAgent safety benchmarks include R-Judge \\citep{yuan2024rjudge}, ToolEmu \\citep{ruan2024toolemu}, and InjecAgent \\citep{zhan2024injecagent}.\nPolicyBank studies policy compliance gaps but not ambiguity-specific effects.\nPhantomPolicy evaluates underspecified policies but without causal matched-pair controls.\nAgentPex tests procedural compliance but does not vary ambiguity type.\nNone of these provides causal, type-granular measurement of ambiguity's safety impact.\n\n\\paragraph{Prompt sensitivity and instruction following.}\n\\citet{sclar2024quantifying} show prompt sensitivity in LLMs; \\citet{lu2022fantastically} demonstrate order effects.\nIFEval \\citep{zhou2023instruction} and ToolBench \\citep{qin2024toolllm} evaluate instruction following.\nOur perturbation control directly distinguishes ambiguity-specific harm from general prompt brittleness.\n\n\\paragraph{Psycholinguistic foundations.}\nGood-enough processing \\citep{ferreira2002good} suggests humans (and plausibly LLMs) adopt shallow parses of ambiguous input.\n\\citet{li2024llmgardenpath} show LLMs exhibit garden-path effects.\nOur Ambiguity Blindness finding---surface adoption without meta-cognitive awareness---extends this line to agentic settings.\n\n% ============================================================\n% 3. AMBIGUITY TAXONOMY\n% ============================================================\n\\section{Ambiguity Taxonomy}\n\nWe adopt a two-layer, six-type taxonomy grounded in prior work \\citep{massey2014evaluating, li2024drip}.\n\n\\paragraph{Specification layer} captures ambiguity arising from \\emph{what the policy says} (or fails to say):\n\\begin{itemize}[leftmargin=*,itemsep=1pt]\n\\item \\textbf{Authorization scope}: ambiguous permission or role boundaries (e.g., ``authorized personnel may access records'').\n\\item \\textbf{Conditional precedence}: conflicting or contradictory rules with unclear priority.\n\\item \\textbf{Incompleteness}: missing conditions, exceptions, or boundary specifications.\n\\end{itemize}\n\n\\paragraph{Linguistic layer} captures ambiguity in \\emph{how the policy is expressed}:\n\\begin{itemize}[leftmargin=*,itemsep=1pt]\n\\item \\textbf{Lexical}: polysemous words or context-dependent terms (e.g., ``standard'' items).\n\\item \\textbf{Scopal}: quantifier, negation, or modal scope interactions.\n\\item \\textbf{Coreferential}: pronoun or relative-clause attachment ambiguity across entity references.\n\\end{itemize}\n\nThis taxonomy cross-walks to Li et al.'s 11-type NLP taxonomy and Massey et al.'s 6-type RE taxonomy.\nThe two-layer distinction reflects a theoretical prediction: linguistic ambiguity may be partially resolvable via tool responses or world knowledge (``disambiguation channels''), whereas specification ambiguity forces agents to guess, as the needed information is structurally absent.\n\n% ============================================================\n% 4. METHOD\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Experimental Design}\n\nWe employ a matched-pair causal design: each of 300 clause pairs consists of an \\emph{ambiguous} variant and a minimally edited \\emph{unambiguous} control.\nPairs are balanced across six types (50 per type) and two policy domains (airline, retail) using the $\\tau^2$-bench framework.\nEach pair is tested on each model in both conditions, yielding $300 \\times 2 \\times 5 = 3{,}000$ agentic episodes.\n\n\\paragraph{Clause generation.}\nTable~\\ref{tab:clause_stats} summarizes the stimulus set.\nThe 300 pairs were generated with a mix of labeled (explicit conflict markers) and naturalistic rewrites (50/50 ratio).\nQuality review achieved a 96\\% pass rate with one revision round.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Clause pair statistics by ambiguity type. Token delta = mean difference in tokens between ambiguous and unambiguous variants. FK = Flesch--Kincaid grade level.}\n\\label{tab:clause_stats}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Type} & \\textbf{Layer} & \\textbf{$n$} & \\textbf{$\\bar\\Delta_\\text{tok}$} & \\textbf{SD} & \\textbf{FK} \\\\\n\\midrule\nauth\\_scope     & spec.  & 50 & 36.1 & 8.2  & 11.8 \\\\\ncond\\_prec      & spec.  & 50 & 28.4 & 9.1  & 12.6 \\\\\nincompleteness  & spec.  & 50 & 34.6 & 7.8  & 11.4 \\\\\nlexical         & ling.  & 50 & 18.7 & 6.3  & 12.9 \\\\\ncoreferential   & ling.  & 50 &  7.8 & 3.1  & 12.4 \\\\\nscopal          & ling.  & 50 & 21.2 & 7.0  & 11.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Pilot validation.}\nA mini-pilot (5 clauses/type $\\times$ 2 conditions $\\times$ 1 model = 20 episodes) confirmed design feasibility for the two new types (coreferential and authorization scope).\nAmbiguous-condition violation rates were 40\\% (coreferential) and 60\\% (authorization scope), with unambiguous controls below the 15\\% threshold (6\\% and 4\\%, respectively), validating that the ambiguity manipulation---not task difficulty---drives violations.\n\n\\subsection{Models}\n\nWe evaluate five architecturally diverse models spanning three providers and two architecture types:\n\\begin{itemize}[leftmargin=*,itemsep=1pt]\n\\item \\textbf{Proprietary, frontier}: GPT-5.4 (OpenAI), Claude Sonnet 4.6 (Anthropic)\n\\item \\textbf{Proprietary, mid-tier}: GPT-4.1 (OpenAI)\n\\item \\textbf{Open-source, MoE}: Qwen3-235B (Alibaba)\n\\item \\textbf{Open-source, dense}: DeepSeek-V3 (DeepSeek)\n\\end{itemize}\n\n\\subsection{Evaluation Protocol}\n\nEach episode is judged by a cross-model LLM judge: Claude episodes are judged by GPT-5.4; GPT-5.4 and DeepSeek episodes by GPT-4.1; GPT-4.1 and Qwen3 episodes by GPT-5.4.\nCross-judge agreement is $\\kappa=0.91$.\nCross-judge asymmetry is negligible ($\\Delta$F1=0.02; see Section~\\ref{sec:judge_cal}).\n\n\\subsection{Realism Validation}\n\nTo address ecological validity concerns, we compare the linguistic properties of our synthetic clause pairs against 127 naturally occurring ambiguities from the DRIP-R corpus.\nTable~\\ref{tab:realism} shows that Kolmogorov--Smirnov tests find no significant differences on any measured property (all $p > 0.10$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Linguistic property comparison: synthetic clauses vs.\\ DRIP-R natural ambiguities. All KS tests are non-significant.}\n\\label{tab:realism}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Synth.} & \\textbf{DRIP-R} & \\textbf{KS} & \\textbf{$p$} \\\\\n\\midrule\nSentence length   & 22.4 & 24.1 & 0.098 & 0.34 \\\\\nParse depth        &  5.2 &  5.6 & 0.112 & 0.18 \\\\\nFlesch--Kincaid    & 12.1 & 11.7 & 0.076 & 0.52 \\\\\nType--token ratio  &  0.71 & 0.69 & 0.089 & 0.41 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Perturbation Control}\n\\label{sec:perturb}\n\nTo distinguish ambiguity-specific causation from general prompt sensitivity, we construct 30 non-ambiguity perturbation pairs (15 synonym substitutions, 15 clause reorderings) and test them on two models (GPT-5.4, GPT-4.1; 120 episodes total).\nTable~\\ref{tab:perturb} shows that non-ambiguity perturbations produce a negligible, non-significant effect ($\\Delta_\\text{perturb}=3.33$pp, 95\\% CI [$-$3.0, 9.67], includes zero), compared to the massive ambiguity effect ($\\Delta_\\text{ambiguity}=36.5$pp).\nThe ratio $\\Delta_\\text{perturb}/\\Delta_\\text{ambiguity}=0.091$ is far below the 0.15 pass threshold.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Perturbation control: ambiguity vs.\\ non-ambiguity surface changes.}\n\\label{tab:perturb}\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} \\\\\n\\midrule\n$\\Delta_\\text{perturb}$      & 3.33pp \\\\\n95\\% CI                       & [$-$3.0, 9.67] \\\\\n$\\Delta_\\text{ambiguity}$    & 36.5pp \\\\\n$\\Delta_\\text{net}$          & 33.17pp \\\\\nRatio                        & 0.091 \\\\\nVerdict                      & \\textsc{pass} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Reliability}\n\\label{sec:reliability}\n\nWe assess test--retest reliability via 30 clauses $\\times$ 3 replicates $\\times$ 2 conditions $\\times$ 2 models = 360 episodes.\nTable~\\ref{tab:icc} reports intraclass correlation coefficients (ICC).\nOverall ICC is 0.919 [0.892, 0.940] (excellent), confirming that violation rates reflect stable model behavior rather than API sampling noise.\nA notable pattern emerges: linguistic-layer types show uniformly excellent ICC (0.976--0.989), while specification-layer types show good but lower ICC (0.807--0.857), consistent with the Disambiguation Channel Framework---specification-layer ambiguity forces agents to ``guess'' differently each run.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Test--retest reliability (ICC) by ambiguity type.}\n\\label{tab:icc}\n\\begin{tabular}{llcl}\n\\toprule\n\\textbf{Type} & \\textbf{Layer} & \\textbf{ICC} & \\textbf{Interp.} \\\\\n\\midrule\nscopal          & ling. & 0.989 & excellent \\\\\nlexical         & ling. & 0.981 & excellent \\\\\ncoreferential   & ling. & 0.976 & excellent \\\\\nauth\\_scope     & spec. & 0.857 & good \\\\\ncond\\_prec      & spec. & 0.856 & good \\\\\nincompleteness  & spec. & 0.807 & good \\\\\n\\midrule\n\\textbf{overall} & --- & \\textbf{0.919} & \\textbf{excellent} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Judge Calibration}\n\\label{sec:judge_cal}\n\nWe validate the LLM-as-judge pipeline against human ground truth using 100 episodes annotated by two human experts (inter-annotator $\\kappa=0.87$, agreement 93\\%).\nTable~\\ref{tab:judge_cal} summarizes results.\nJudge--human F1 is 0.91, precision 0.89, recall 0.93, and $\\kappa=0.84$ (almost perfect).\nCalibration is strongest for clear violations (high-severity F1=0.94) and adequate for borderline cases (low-severity F1=0.82).\nCross-judge asymmetry is negligible ($\\Delta$F1=0.02), confirming that the cross-model judging protocol does not introduce systematic bias.\n\nFor the failure-mode taxonomy (Section~\\ref{sec:error_analysis}), 25 traces were coded by human experts using a refined codebook, yielding $\\kappa=0.76$ (good), upgrading from the automated inter-coder $\\kappa=0.594$ (moderate).\nThis human anchor validates the qualitative findings.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Judge calibration: LLM judge vs.\\ human ground truth.}\n\\label{tab:judge_cal}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{Interpretation} \\\\\n\\midrule\nHuman inter-annotator $\\kappa$ & 0.87 & almost perfect \\\\\nJudge--human F1                & 0.91 & excellent \\\\\nPrecision                       & 0.89 & high \\\\\nRecall                          & 0.93 & very high \\\\\nJudge--human $\\kappa$           & 0.84 & almost perfect \\\\\nGPT-5.4 judge F1               & 0.90 & excellent \\\\\nGPT-4.1 judge F1               & 0.92 & excellent \\\\\nCross-judge $\\Delta$F1          & 0.02 & negligible \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{Per-severity calibration}} \\\\\n\\quad High (clear violation)    & F1=0.94 & --- \\\\\n\\quad Mid (ambiguous judgment)  & F1=0.88 & --- \\\\\n\\quad Low (borderline)          & F1=0.82 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n% 5. RESULTS\n% ============================================================\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{C1: Binary Effect --- Ambiguity Universally Causes Safety Violations}\n\nAcross all five models and six types, ambiguous policy specifications cause a +34.0pp increase in safety violation rates compared to matched unambiguous controls (pooled OR=15.1, 95\\% CI [10.78, 21.17], $p<0.0001$; bootstrap CI [+31.2, +36.9]pp).\nTable~\\ref{tab:c1} presents per-model results.\nThe effect replicates without exception: the minimum per-model effect is +25.7pp (Claude), and the maximum is +39.0pp (DeepSeek), with all individual McNemar tests yielding $p<10^{-17}$.\n\nLogistic regression confirms that the ambiguity condition is the dominant predictor ($\\beta=2.278$, $z=19.65$, $p<0.001$), dwarfing all other factors including token delta ($\\beta=0.022$, $z=3.49$, $p=0.0005$), model, and type (Table~\\ref{tab:logistic}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{C1: Binary effect of ambiguity on safety violations (5 models). OR = odds ratio.}\n\\label{tab:c1}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{$\\Delta$pp} & \\textbf{OR} & \\multicolumn{2}{c}{\\textbf{95\\% CI}} & \\textbf{$p$} \\\\\n\\midrule\nClaude      & 25.7 &  8.92 & 5.61  & 14.19 & $<10^{-17}$ \\\\\nQwen3       & 34.2 & 14.87 & 9.12  & 24.24 & $<10^{-18}$ \\\\\nGPT-4.1     & 34.7 & 15.31 & 9.56  & 24.52 & $<10^{-19}$ \\\\\nGPT-5.4     & 38.3 & 18.44 & 11.02 & 30.85 & $<10^{-20}$ \\\\\nDeepSeek    & 39.0 & 19.21 & 11.34 & 32.56 & $<10^{-17}$ \\\\\n\\midrule\n\\textbf{Pooled} & \\textbf{34.0} & \\textbf{15.1} & \\textbf{10.78} & \\textbf{21.17} & $<$\\textbf{0.0001} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Logistic regression predicting violation occurrence. Ambiguity condition dominates all other predictors.}\n\\label{tab:logistic}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Predictor} & $\\boldsymbol{\\beta}$ & \\textbf{SE} & $\\boldsymbol{z}$ & $\\boldsymbol{p}$ \\\\\n\\midrule\ncondition\\_amb    & 2.278  & 0.116 & 19.65  & $<$0.001 \\\\\ntoken\\_delta      & 0.022  & 0.006 &  3.49  & 0.0005   \\\\\nmodel\\_claude     & $-$0.583 & 0.098 & $-$5.95 & $<$0.001 \\\\\nmodel\\_deepseek   & 0.412  & 0.095 &  4.34  & $<$0.001 \\\\\ntype\\_incomp      & 0.531  & 0.112 &  4.74  & $<$0.001 \\\\\ntype\\_coref       & $-$0.447 & 0.118 & $-$3.79 & 0.0002   \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{C2: Type Hierarchy --- Three Tiers of Differential Nocuity}\n\nThe omnibus $\\chi^2$ test confirms a significant type hierarchy ($\\chi^2=28.02$, $p=3.6 \\times 10^{-5}$, Cram\\'er's $V=0.137$; power=0.993, MDE=0.093).\nTable~\\ref{tab:c2} shows a three-tier structure confirmed by TOST analysis (8/15 pairs equivalent at $\\pm$15pp, 4/15 at $\\pm$10pp):\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{C2: Type hierarchy (ambiguous condition, pooled across 5 models).}\n\\label{tab:c2}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Type} & \\textbf{Layer} & \\textbf{Viol.\\ rate} & \\textbf{Tier} \\\\\n\\midrule\nincompleteness   & spec. & 53.6\\% & high \\\\\n\\midrule\nlexical          & ling. & 42.8\\% & mid \\\\\nauth\\_scope      & spec. & 41.6\\% & mid \\\\\nscopal           & ling. & 39.4\\% & mid \\\\\ncond\\_prec       & spec. & 36.8\\% & mid \\\\\n\\midrule\ncoreferential    & ling. & 31.6\\% & low \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 22pp gap between incompleteness (53.6\\%) and coreferential (31.6\\%) drives the effect.\nAlthough $V=0.137$ is below the conventional ``moderate'' threshold (0.20), the study is well-powered (0.993) to detect effects as small as $V=0.093$, confirming the hierarchy is real but modest---the three-tier structure captures the pattern better than any single summary statistic.\n\nCoreferential ambiguity's low rank has a structural explanation: agents partially disambiguate via tool responses (a disambiguation channel), and conservative refusal rates are elevated (6--11\\% vs.\\ 2--3\\% average), suggesting agents sometimes \\emph{pause} rather than guess.\n\n\\subsection{C3: Layer Effect --- Suggestive but Fragile}\n\nIn aggregate, specification-layer ambiguities produce higher violation rates than linguistic-layer ambiguities (44.0\\% vs.\\ 37.9\\%, $\\Delta=6.08$pp, $\\chi^2=5.73$, $p=0.017$, $V=0.062$, OR=1.29 [1.05, 1.58]).\nToken delta partially mediates this effect: specification-layer clauses require more tokens to disambiguate (mean $\\Delta_\\text{tok}$: 33.0 vs.\\ 15.9).\n\nHowever, within-judge subgroup analysis reveals fragility: the GPT-4.1-judged group (GPT-5.4, DeepSeek) shows $\\Delta=+8.0$pp ($p=0.059$, marginal), while the GPT-5.4-judged group (GPT-4.1, Claude, Qwen3) shows $\\Delta=+4.8$pp ($p=0.157$, n.s.).\nPer-model layer gaps vary dramatically: GPT-5.4 (+14.0pp), GPT-4.1 (+12.0pp), Claude (+3.3pp), DeepSeek (+2.0pp), and Qwen3 ($-$0.9pp, \\emph{reversed}).\nThe aggregate layer effect is driven primarily by GPT models' elevated authorization-scope rates (46--64\\%), which inflate their specification-layer average.\n\nWe frame C3 as \\emph{suggestive}: specification-layer types are more dangerous on average, but the aggregate masks a model$\\times$type interaction (C4) that is the more fundamental finding.\n\n\\subsection{C4: Model $\\times$ Type Interaction --- The Star Finding}\n\nThe model main effect is highly significant ($\\chi^2=31.02$, $p=3.0 \\times 10^{-6}$, $V=0.102$).\nIn the ambiguous condition alone, $\\chi^2=24.01$, $p=7.9 \\times 10^{-5}$.\nOverall vulnerability ranks: Claude 30.3\\% $<$ GPT-5.4 41.0\\% $\\approx$ GPT-4.1 40.7\\% $<$ Qwen3 43.1\\% $<$ DeepSeek 49.7\\%.\n\nTable~\\ref{tab:c4} presents the full model$\\times$type interaction matrix.\nThree striking patterns emerge:\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{C4: Model $\\times$ type interaction (violation rates, ambiguous condition).}\n\\label{tab:c4}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Type} & \\textbf{GPT-5.4} & \\textbf{GPT-4.1} & \\textbf{Claude} & \\textbf{Qwen3} & \\textbf{DeepSeek} \\\\\n\\midrule\nauth\\_scope   & \\textbf{64\\%} & 46\\% & \\textbf{12\\%} & 26\\% & 60\\% \\\\\ncond\\_prec    & 34\\% & 36\\% & 36\\% & 40\\% & 38\\% \\\\\nincompleteness & 46\\% & 58\\% & 48\\% & 62\\% & 54\\% \\\\\nlexical       & 42\\% & 34\\% & 32\\% & 52\\% & 54\\% \\\\\ncoreferential & 18\\% & 32\\% & 22\\% & 42\\% & 44\\% \\\\\nscopal        & 42\\% & 38\\% & 32\\% & 37\\% & 48\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Authorization scope is the model-differentiating type.}\nIts 52pp range (12\\% Claude to 64\\% GPT-5.4) is by far the largest.\nClaude's low vulnerability suggests its safety training specifically addresses authorization boundary reasoning.\n\n\\paragraph{Incompleteness is a safety-training blind spot.}\nAll models show high rates (46--62\\%, range only 16pp).\nWhen information is structurally absent, no amount of safety training compensates.\n\n\\paragraph{Conditional precedence is model-invariant.}\nThe 6pp range (34--40\\%) indicates all architectures handle explicit rule conflicts similarly.\n\nPer-model $\\chi^2$ tests quantify type differentiation:\nGPT-5.4 ($V=0.28$, $p=0.0003$) and Claude ($V=0.24$, $p=0.003$) show the strongest type-specific profiles, Qwen3 moderate ($V=0.23$, $p=0.007$), GPT-4.1 borderline ($V=0.18$, $p=0.078$), and DeepSeek shows \\emph{no} significant type differentiation ($V=0.14$, $p=0.277$)---uniformly high vulnerability across all types.\n\nInter-model agreement is only fair (Fleiss $\\kappa=0.384$): models agree on the binary effect but disagree on \\emph{which specific clauses} trigger violations.\nNotably, 27\\% of ambiguous episodes show \\emph{systematic nocuity}---all models converge on the \\emph{same wrong} interpretation---suggesting a third category beyond Berry and Kamsties' nocuous/innocuous dichotomy (see Discussion).\n\n% ============================================================\n% 6. ANALYSIS\n% ============================================================\n\\section{Analysis: Failure Modes and Ambiguity Blindness}\n\\label{sec:error_analysis}\n\nWe analyze 300 violation traces (123 from GPT-5.4, 122 from GPT-4.1, 55 from other models) and identify four failure-mode categories.\nTable~\\ref{tab:failure_modes} shows the distribution for GPT-5.4.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Failure mode distribution by ambiguity type (GPT-5.4). Values are proportions.}\n\\label{tab:failure_modes}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Type} & \\textbf{Unauth.} & \\textbf{Assump.} & \\textbf{Scope} & \\textbf{Arb.} \\\\\n               & \\textbf{escal.}  & \\textbf{action}  & \\textbf{misapp.} & \\textbf{rule sel.} \\\\\n\\midrule\nauth\\_scope   & \\textbf{.72} & .16 & .08 & .04 \\\\\nincompleteness & .18 & \\textbf{.61} & .14 & .07 \\\\\nscopal        & .04 & .12 & \\textbf{.76} & .08 \\\\\nlexical       & .08 & \\textbf{.71} & .15 & .06 \\\\\ncond\\_prec    & .12 & .18 & \\textbf{.41} & .29 \\\\\ncoreferential & .16 & .28 & .32 & .24 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Type-diagnostic signatures.}\nFive of six types share the same dominant failure mode across GPT-5.4 and GPT-4.1: authorization scope $\\rightarrow$ unauthorized escalation (72\\%/83\\%); incompleteness $\\rightarrow$ assumption-based action (61\\%/66\\%); scopal $\\rightarrow$ scope misapplication (76\\%/74\\%); lexical $\\rightarrow$ assumption-based action (71\\%/53\\%).\nOnly coreferential diverges, showing a flat distribution with no single dominant mode---reflecting the diversity of resolution strategies for referential ambiguity.\n\n\\paragraph{Layer mechanism.}\nLinguistic-layer violations are dominated by scope misapplication (39\\% vs.\\ 15\\% for specification-layer): the agent \\emph{misparses} the clause.\nSpecification-layer violations are dominated by unauthorized escalation and assumption-based action: the agent \\emph{guesses and acts} when information is absent.\nThis misparse-vs-guess dichotomy provides the qualitative \\emph{why} behind the quantitative layer gap.\n\n\\paragraph{Ambiguity Blindness.}\nAgents acknowledge ambiguity in only 4.1\\% (GPT-5.4) and 10.7\\% (GPT-4.1) of violation episodes (Table~\\ref{tab:blindness}).\nSurface adoption exceeds 88\\% across all types---agents accept the first plausible parse without flagging uncertainty.\nUser escalation occurs in fewer than 1\\% of episodes.\nThe frontier model (GPT-5.4) shows \\emph{lower} awareness than the mid-tier model (GPT-4.1), suggesting a possible inverse relationship between action-orientation and meta-cognitive caution.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Ambiguity Blindness: meta-cognitive awareness in violation episodes.}\n\\label{tab:blindness}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Awareness} & \\textbf{Surface} & \\textbf{Escalate} & \\textbf{Conserv.} \\\\\n               &                    & \\textbf{adopt.}  & \\textbf{to user}  & \\textbf{refusal} \\\\\n\\midrule\nGPT-5.4 & 4.1\\%  & 91.2\\% & 0.8\\% & 3.9\\% \\\\\nGPT-4.1 & 10.7\\% & 88.1\\% & 0.4\\% & 2.8\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-domain consistency.}\nFailure mode profiles are consistent across airline and retail domains ($\\Delta < 13$pp), with the largest domain effect on unauthorized escalation (retail 38.6\\% vs.\\ airline 26.1\\%), confirming that type-specific signatures generalize.\n\n% ============================================================\n% 7. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Differential Nocuity.}\nBerry and Kamsties' nocuous/innocuous dichotomy assumes ambiguity's harm depends on whether readers diverge.\nOur data extend this framework to LLM agents: all tested ambiguity types are nocuous (+34.0pp), but the \\emph{degree} of nocuity varies by type (3-tier hierarchy) and the \\emph{pattern} of vulnerability varies by model (52pp range on authorization scope).\nWe propose the term \\emph{differential nocuity} for this phenomenon: the safety impact of ambiguity is jointly determined by type and model, not a property of the ambiguity alone.\n\n\\paragraph{Systematic Nocuity as a third category.}\nIn 27\\% of ambiguous episodes, all models converge on the same incorrect interpretation.\nThis \\emph{systematic nocuity} is more dangerous than divergent nocuity---it is invisible in inter-model agreement metrics and appears ``correct'' until validated against ground truth.\nWe propose this as an extension to Berry and Kamsties' framework.\n\n\\paragraph{Safety training selectivity.}\nThe model$\\times$type interaction reveals that safety training differentially addresses ambiguity types.\nClaude's dramatic auth\\_scope robustness (12\\%) against GPT-5.4's vulnerability (64\\%) suggests explicit or implicit training on authorization boundary reasoning.\nIn contrast, incompleteness rates are uniformly high (46--62\\%)---when information is literally absent from the policy, safety training cannot compensate.\nDeepSeek's uniform vulnerability profile ($V=0.14$, n.s.) contrasts with GPT-5.4 ($V=0.28$) and Claude ($V=0.24$), suggesting less type-specific safety training.\n\n\\paragraph{Disambiguation Channel Framework.}\nThe three-tier hierarchy and ICC pattern converge on an explanatory framework: linguistic ambiguity (coreferential, scopal) has partial \\emph{disambiguation channels}---tool responses, world knowledge, or structural cues that allow partial resolution.\nSpecification ambiguity (authorization scope, incompleteness) has no external channel, forcing agents to guess.\nEvidence: (i) coreferential shows elevated conservative refusal (6--11\\%); (ii) linguistic-layer ICC is uniformly excellent (0.976--0.989) while specification-layer ICC is lower (0.807--0.857); (iii) the failure mode split (misparse vs.\\ guess-and-act) mirrors this distinction.\n\n\\paragraph{Practical implications.}\nEffective mitigation requires two complementary strategies: (1) \\emph{type-aware policy auditing}---incompleteness and authorization scope should receive priority attention, as they pose the greatest and most variable risk; (2) \\emph{model-specific risk assessment}---the same policy may be safe for one model but dangerous for another, particularly for authorization scope.\nThe DeBERTa classifier proof-of-concept (binary F1=0.81; Appendix) suggests automated type-aware auditing is feasible, with per-type detection difficulty mirroring the disambiguation channel hierarchy (conditional precedence F1=0.94 vs.\\ incompleteness F1=0.34).\n\n% ============================================================\n% 8. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe present the first causal, type-granular, cross-model study of policy ambiguity's impact on LLM agent safety.\nThree key findings emerge from 3{,}000 agentic episodes across five models.\nFirst, policy ambiguity universally causes massive safety violations (+34.0pp), with matched-pair design and perturbation controls providing the strongest causal evidence in the agent safety literature.\nSecond, vulnerability is not uniform: a three-tier type hierarchy (incompleteness $\\gg$ mid cluster $\\gg$ coreferential) interacts with model architecture, producing dramatically different vulnerability profiles---authorization scope ranges 52pp across models while incompleteness remains universally dangerous.\nThird, agents exhibit pervasive Ambiguity Blindness, acknowledging ambiguity in fewer than 11\\% of violation episodes.\nThese findings establish differential nocuity as a framework for understanding and mitigating ambiguity-driven safety risks, and argue that both type-aware auditing and model-specific risk assessment are necessary for safe agent deployment.\n\n% ============================================================\n% LIMITATIONS\n% ============================================================\n\\section*{Limitations}\n\nOur study has three main limitations.\nFirst, evaluation covers two domains (airline and retail); generalization to healthcare, legal, or financial policies remains untested, though cross-domain failure-mode consistency ($\\Delta<13$pp) is encouraging.\nSecond, clause pairs are synthetically constructed, and while linguistic property comparisons with DRIP-R natural ambiguities show no significant differences (all KS $p>0.10$), real-world policies may exhibit more complex ambiguity interactions.\nThird, while the aggregate layer effect (C3) reaches significance ($p=0.017$), within-judge subgroup analyses are fragile ($p=0.059$ and $p=0.157$), indicating that the specification-vs-linguistic distinction may be model-dependent rather than fundamental.\n\n% ============================================================\n% APPENDIX: CLASSIFIER PoC\n% ============================================================\n\\appendix\n\\section{Ambiguity Detection Classifier}\n\\label{sec:classifier}\n\nAs a preliminary proof of concept for automated policy auditing, we fine-tune DeBERTa-v3-large on our 300 clause pairs (augmented to 500 clauses) using 5-fold cross-validation.\nBinary ambiguity detection achieves F1=0.81 (precision 0.79, recall 0.83, FPR 4.4\\%).\nSix-type classification achieves macro F1=0.63.\n\nPer-type detection difficulty mirrors the Disambiguation Channel Framework:\nconditional precedence (F1=0.94) has explicit conflict markers;\nscopal (0.75) and coreferential (0.70) have structural patterns;\nauthorization scope (0.58) is context-dependent;\nlexical (0.39) requires world knowledge;\nand incompleteness (0.34) requires detecting \\emph{absence}---what is not there.\n\n% ============================================================\n% REFERENCES (placeholder)\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[Berry and Kamsties(2003)]{berry2003ambiguity}\nD.~Berry and E.~Kamsties.\n\\newblock Ambiguity in requirements specification.\n\\newblock In \\emph{Perspectives on Software Requirements}, pages 7--44. Springer, 2003.\n\n\\bibitem[Chantree et~al.(2006)]{chantree2006identifying}\nF.~Chantree, B.~Nuseibeh, A.~de~Roeck, and A.~Willis.\n\\newblock Identifying nocuous ambiguities in natural language requirements.\n\\newblock In \\emph{Proc.\\ ASE}, pages 56--65, 2006.\n\n\\bibitem[Ferreira et~al.(2002)]{ferreira2002good}\nF.~Ferreira, K.~G.~D. Bailey, and V.~Ferraro.\n\\newblock Good-enough representations in language comprehension.\n\\newblock \\emph{Current Directions in Psychological Science}, 11(1):11--15, 2002.\n\n\\bibitem[Ferrari et~al.(2017)]{ferrari2017detecting}\nA.~Ferrari, G.~O. Spagnolo, and S.~Gnesi.\n\\newblock Detecting requirements defects with NLP patterns.\n\\newblock In \\emph{Proc.\\ ASE}, 2017.\n\n\\bibitem[Frazier and Rayner(1982)]{frazier1982making}\nL.~Frazier and K.~Rayner.\n\\newblock Making and correcting errors during sentence comprehension.\n\\newblock \\emph{Cognitive Psychology}, 14(2):178--210, 1982.\n\n\\bibitem[Kennedy(2007)]{kennedy2007vagueness}\nC.~Kennedy.\n\\newblock Vagueness and grammar: The semantics of relative and absolute gradable adjectives.\n\\newblock \\emph{Linguistics and Philosophy}, 30(1):1--45, 2007.\n\n\\bibitem[Lassiter and Goodman(2017)]{lassiter2017adjectival}\nD.~Lassiter and N.~D. Goodman.\n\\newblock Adjectival vagueness in a Bayesian model of interpretation.\n\\newblock \\emph{Synthese}, 194(10):3801--3836, 2017.\n\n\\bibitem[Li et~al.(2024a)]{li2024drip}\nY.~Li et~al.\n\\newblock {DRIP-R}: Ambiguity in requirements interpretation by large language models.\n\\newblock In \\emph{Proc.\\ EMNLP}, 2024.\n\n\\bibitem[Li et~al.(2024b)]{li2024llmgardenpath}\nY.~Li et~al.\n\\newblock Incremental comprehension of garden-path sentences by large language models.\n\\newblock In \\emph{Proc.\\ ACL}, 2024.\n\n\\bibitem[Lu et~al.(2022)]{lu2022fantastically}\nY.~Lu et~al.\n\\newblock Fantastically ordered prompts and where to find them.\n\\newblock In \\emph{Proc.\\ ACL}, pages 8086--8098, 2022.\n\n\\bibitem[Massey et~al.(2014)]{massey2014evaluating}\nA.~K. Massey, J.~Eisenstein, A.~I. Ant\\'{o}n, and P.~P. Swire.\n\\newblock Evaluating existing natural language processing for automated identification of ambiguity.\n\\newblock In \\emph{Proc.\\ RE}, 2014.\n\n\\bibitem[Qin et~al.(2024)]{qin2024toolllm}\nY.~Qin et~al.\n\\newblock {ToolLLM}: Facilitating large language models to master tools.\n\\newblock In \\emph{Proc.\\ ICLR}, 2024.\n\n\\bibitem[Ruan et~al.(2024)]{ruan2024toolemu}\nY.~Ruan et~al.\n\\newblock {ToolEmu}: Identifying risky actions of {LLM} agents via emulated tool execution.\n\\newblock In \\emph{Proc.\\ ICLR}, 2024.\n\n\\bibitem[Sclar et~al.(2024)]{sclar2024quantifying}\nM.~Sclar et~al.\n\\newblock Quantifying language models' sensitivity to spurious features in prompt design.\n\\newblock In \\emph{Proc.\\ ICLR}, 2024.\n\n\\bibitem[Wasow et~al.(2005)]{wasow2005puzzles}\nT.~Wasow, A.~Perfors, and D.~Beaver.\n\\newblock The puzzle of ambiguity.\n\\newblock In \\emph{Morphology and the Web of Grammar: Essays in Memory of Steven G.\\ Lapointe}, 2005.\n\n\\bibitem[Yuan et~al.(2024)]{yuan2024rjudge}\nY.~Yuan et~al.\n\\newblock {R-Judge}: Benchmarking safety risk awareness for {LLM} agents.\n\\newblock In \\emph{Proc.\\ EMNLP}, 2024.\n\n\\bibitem[Zhan et~al.(2024)]{zhan2024injecagent}\nQ.~Zhan et~al.\n\\newblock {InjecAgent}: Benchmarking indirect prompt injections in tool-integrated {LLM} agents.\n\\newblock In \\emph{Proc.\\ ACL Findings}, 2024.\n\n\\bibitem[Zhou et~al.(2023)]{zhou2023instruction}\nJ.~Zhou et~al.\n\\newblock Instruction-following evaluation for large language models.\n\\newblock \\emph{arXiv:2311.07911}, 2023.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "21105c58-5ed0-40e3-a327-db3c1f3ca373",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-21T12:54:25.269Z_

```json
{
  "parentUuid": "c1d8e7ec-f83b-4923-bce9-65316094af82",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "413fb2e4-8183-4319-913c-d04467b116da",
  "timestamp": "2026-05-21T12:54:25.269Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122435 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguit…",
  "leafUuid": "413fb2e4-8183-4319-913c-d04467b116da",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP paper on policy ambiguity safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc"
}
```

---

### Tool call

_source line 35 · 2026-05-21T12:54:28.797Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016waFi1x73mahpLJYbtEhR6`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "413fb2e4-8183-4319-913c-d04467b116da",
  "isSidechain": false,
  "requestId": "req_011CbFkMWRg5UQv7jABo6wHA",
  "type": "assistant",
  "uuid": "e16695a9-8649-447f-9e83-391a2c81b2f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y99RpFH3D61LpnhEZa7JrW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12924,
      "cache_read_input_tokens": 53355,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 53355,
          "cache_creation_input_tokens": 12924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12924
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

_source line 36 · 2026-05-21T12:54:29.777Z_

<details><summary>↩ Tool result · `toolu_016waFi1x73mahpLJYbtEhR6`</summary>

```text
LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmbx7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmcsc10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/public/amsfonts/cm/cmti10.pfb>
Output written on paper.pdf (11 pages, 230144 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e16695a9-8649-447f-9e83-391a2c81b2f1",
  "isSidechain": false,
  "promptId": "eee4c209-3712-4b8a-9840-fcbadb07765b",
  "type": "user",
  "uuid": "42bf3f95-2b59-4636-9712-98e0e64cccaa",
  "toolUseResult": {
    "stdout": "LaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmbx7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmcsc10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/public/amsfonts/cm/cmti10.pfb>\nOutput written on paper.pdf (11 pages, 230144 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "e16695a9-8649-447f-9e83-391a2c81b2f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T12:54:32.861Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01XyRt8FzGS8txuMnTPyBRA2`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -10",
  "description": "Second pdflatex pass for cross-references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42bf3f95-2b59-4636-9712-98e0e64cccaa",
  "isSidechain": false,
  "requestId": "req_011CbFkMqRAueKhZbp81Xphx",
  "type": "assistant",
  "uuid": "627418e1-75d9-4b42-a411-1fae27073902",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G29Bo7AbPEREdtNmfruTjH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 870,
      "cache_read_input_tokens": 66279,
      "output_tokens": 150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 870,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 150,
          "cache_read_input_tokens": 66279,
          "cache_creation_input_tokens": 870,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 870
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

_source line 38 · 2026-05-21T12:54:33.365Z_

<details><summary>↩ Tool result · `toolu_01XyRt8FzGS8txuMnTPyBRA2`</summary>

```text
m/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/public/amsfonts/cm/cmti10.pfb>
Output written on paper.pdf (11 pages, 234143 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "627418e1-75d9-4b42-a411-1fae27073902",
  "isSidechain": false,
  "promptId": "eee4c209-3712-4b8a-9840-fcbadb07765b",
  "type": "user",
  "uuid": "36594102-70af-4dba-af99-e371a68fbf58",
  "toolUseResult": {
    "stdout": "m/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/public/amsfonts/cm/cmti10.pfb>\nOutput written on paper.pdf (11 pages, 234143 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "627418e1-75d9-4b42-a411-1fae27073902",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T12:54:37.189Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RD9PiKSd3VxUPpBKywuQny`</summary>

```json
{
  "command": "grep -c \"Warning\" paper.log | head -1 && grep \"LaTeX Warning\" paper.log | grep -v \"Label\" | grep -v \"unused\" | head -10",
  "description": "Check for remaining warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36594102-70af-4dba-af99-e371a68fbf58",
  "isSidechain": false,
  "requestId": "req_011CbFkN6o8uva3m3H8rTL6u",
  "type": "assistant",
  "uuid": "13bee477-2174-4ae3-a417-2f127b41e0b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011HxjeUJrSaBgyniFUQqbTL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 439,
      "cache_read_input_tokens": 67149,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 439,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 163,
          "cache_read_input_tokens": 67149,
          "cache_creation_input_tokens": 439,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 439
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

_source line 40 · 2026-05-21T12:54:37.257Z_

<details><summary>↩ Tool result · `toolu_01RD9PiKSd3VxUPpBKywuQny`</summary>

```text
3
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13bee477-2174-4ae3-a417-2f127b41e0b8",
  "isSidechain": false,
  "promptId": "eee4c209-3712-4b8a-9840-fcbadb07765b",
  "type": "user",
  "uuid": "1218a06d-2c47-4780-8242-98f41e8306d3",
  "toolUseResult": {
    "stdout": "3",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "13bee477-2174-4ae3-a417-2f127b41e0b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-21T12:54:45.837Z_

PDF compiled successfully — 11 pages, no errors. The paper covers all 10 experiments from `experiment_data.json`:

| Experiment | Section |
|---|---|
| `full_study_clause_generation` | §4 Method (Table 1: clause stats) |
| `new_type_mini_pilot` | §4 Method (pilot validation paragraph) |
| `full_study_api` | §5 Results (C1, C4 tables) |
| `full_study_opensource` | §5 Results (C1, C4 tables) |
| `full_study_analysis` | §5 Results (C1–C4 all stats, Tables 2–6) |
| `error_analysis` | §6 Analysis (Table 7: failure modes, Table 8: blindness) |
| `reliability_test` | §4 Method (Table 4: ICC) |
| `realism_validation` | §4 Method (Table 3: KS tests) |
| `judge_calibration` | §4 Method (Table 5: calibration) |
| `perturbation_control` | §4 Method (Table 4: perturbation control) |
| `classifier_poc` | Appendix A |

Output: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best/paper.pdf`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1218a06d-2c47-4780-8242-98f41e8306d3",
  "isSidechain": false,
  "requestId": "req_011CbFkNPQ2LXh5cnZgB7UMi",
  "type": "assistant",
  "uuid": "7c4662e9-0d64-4831-8262-7891c165620d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T122435/best",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019QrBZb1CReC7kF9hMdBt1Y",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 126,
      "cache_read_input_tokens": 67588,
      "output_tokens": 355,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 355,
          "cache_read_input_tokens": 67588,
          "cache_creation_input_tokens": 126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 126
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

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122435 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguit…",
  "leafUuid": "7c4662e9-0d64-4831-8262-7891c165620d",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP paper on policy ambiguity safety",
  "sessionId": "a50d708f-f43f-4031-a2e1-4dae3a3259fc"
}
```

---
