# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T041217 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/33606c3c-2a96-439f-ad7e-5dfed492ad57.jsonl`
- **Structured JSON:** [`8563520a27c4dece8e8e.json`](../../sessions/85/8563520a27c4dece8e8e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T04:42:39.427Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T04:42:39.427Z",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T041217 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：Reframe: joint estimation is methodologically principled AND provides unique diagnostic value, even when ranking improvement is modest. Claim 1 softened to \"confounding exists and is detectable\" (mechanism, not magnitude). Claim 3 softened to \"comparable or better rankings PLUS interpretable diagnostics no baseline provides.\" Elevate per-model c_n, per-judge d_j, per-item e_i as co-primary contribution. Lead with \"unified diagnostic framework\" angle. Add subset analysis: show G-MFRM advantage is concentrated on high-contamination models (top quartile c_n). AAAI positioning viable but needs strong writing; ARR backup advisable.\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-22T04:42:39.431Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T04:42:39.431Z",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57"
}
```

---

## Round 1

33 recorded events

### User

_source line 3 · 2026-05-22T04:42:39.452Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T041217 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：Reframe: joint estimation is methodologically principled AND provides unique diagnostic value, even when ranking improvement is modest. Claim 1 softened to "confounding exists and is detectable" (mechanism, not magnitude). Claim 3 softened to "comparable or better rankings PLUS interpretable diagnostics no baseline provides." Elevate per-model c_n, per-judge d_j, per-item e_i as co-primary contribution. Lead with "unified diagnostic framework" angle. Add subset analysis: show G-MFRM advantage is concentrated on high-contamination models (top quartile c_n). AAAI positioning viable but needs strong writing; ARR backup advisable.

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "207a7a17-59d3-4278-abf7-5d52712c6cbf",
  "type": "user",
  "uuid": "4aeb5102-bbee-4f84-8c25-3733370fc7f1",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T04:42:39.451Z_

```json
{
  "parentUuid": "4aeb5102-bbee-4f84-8c25-3733370fc7f1",
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
  "uuid": "baf18582-713c-4acf-9291-7ee60e131416",
  "timestamp": "2026-05-22T04:42:39.451Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T04:42:39.451Z_

```json
{
  "parentUuid": "baf18582-713c-4acf-9291-7ee60e131416",
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
  "uuid": "653840ab-d638-4baf-957f-8885a9e2c3f0",
  "timestamp": "2026-05-22T04:42:39.451Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-22T04:42:39.451Z_

```json
{
  "parentUuid": "653840ab-d638-4baf-957f-8885a9e2c3f0",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4625620f-efec-4fc7-959a-3b4af08413c5",
  "timestamp": "2026-05-22T04:42:39.451Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
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
  "aiTitle": "Generate simulated research paper for dream_20260522T041217",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57"
}
```

---

### Assistant

_source line 8 · 2026-05-22T04:42:44.093Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the experiment data and paper framing files to understand what I need to write.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4625620f-efec-4fc7-959a-3b4af08413c5",
  "isSidechain": false,
  "requestId": "req_011CbGzfRY82ESoFoxuNdJck",
  "type": "assistant",
  "uuid": "c73a30c2-c964-4fc9-ae30-592d09fbc40e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178324edfKzEnmySEfmTcBH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12353,
      "cache_read_input_tokens": 11447,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12353,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 223,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12353,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12353
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

_source line 9 · 2026-05-22T04:42:45.701Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HwzVVwpGMB6tYaaFXihvsh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c73a30c2-c964-4fc9-ae30-592d09fbc40e",
  "isSidechain": false,
  "requestId": "req_011CbGzfRY82ESoFoxuNdJck",
  "type": "assistant",
  "uuid": "a1d76f64-1516-4f94-9262-69cb6b43e684",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178324edfKzEnmySEfmTcBH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12353,
      "cache_read_input_tokens": 11447,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12353,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 223,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12353,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12353
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

_source line 10 · 2026-05-22T04:42:45.993Z_

<details><summary>↩ Tool result · `toolu_01HwzVVwpGMB6tYaaFXihvsh`</summary>

```text
1	[
2	  {
3	    "name": "multi_judge_data_collection",
4	    "description": "Collect multi-judge evaluation data on MT-Bench (80 items × 2 turns) and Arena-Hard (500 items) using 8 judges, evaluating 22 target models with position swap.\n",
5	    "results": {
6	      "total_judges": 8,
7	      "judge_list": "GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Qwen3-235B-A22B, Qwen3.6-27B, Llama-4-Maverick, Gemini-2.5-Pro",
8	      "total_target_models": 22,
9	      "mt_bench_items": 160,
10	      "arena_hard_items": 500,
11	      "total_judgments_planned": 232320,
12	      "total_judgments_collected": 219874,
13	      "collection_completion_rate": 0.9464,
14	      "api_failure_rate": 0.031,
15	      "refusal_rate": 0.023,
16	      "position_swap_agreement": 0.72,
17	      "inter_judge_fleiss_kappa": 0.38,
18	      "pairwise_judge_agreement_mean": 0.64,
19	      "pairwise_judge_agreement_std": 0.09,
20	      "uda_response_collection_rate": 0.98,
21	      "api_cost_usd": 847,
22	      "vllm_gpu_hours": 118,
23	      "total_wall_clock_days": 11
24	    },
25	    "tables": [
26	      {
27	        "name": "judge_coverage_matrix",
28	        "caption": "Judge × Benchmark coverage (fraction of completed evaluations)",
29	        "columns": [
30	          "Judge",
31	          "MT-Bench",
32	          "Arena-Hard",
33	          "Overall"
34	        ],
35	        "rows": [
36	          [
37	            "GPT-5.5",
38	            "0.99",
39	            "0.98",
40	            "0.984"
41	          ],
42	          [
43	            "Claude Opus 4.7",
44	            "0.98",
45	            "0.97",
46	            "0.974"
47	          ],
48	          [
49	            "Claude Sonnet 4.6",
50	            "0.99",
51	            "0.98",
52	            "0.984"
53	          ],
54	          [
55	            "DeepSeek-V4-Pro",
56	            "0.97",
57	            "0.95",
58	            "0.958"
59	          ],
60	          [
61	            "Qwen3-235B-A22B",
62	            "0.96",
63	            "0.93",
64	            "0.942"
65	          ],
66	          [
67	            "Qwen3.6-27B",
68	            "0.94",
69	            "0.91",
70	            "0.922"
71	          ],
72	          [
73	            "Llama-4-Maverick",
74	            "0.95",
75	            "0.92",
76	            "0.932"
77	          ],
78	          [
79	            "Gemini-2.5-Pro",
80	            "0.98",
81	            "0.96",
82	            "0.968"
83	          ]
84	        ]
85	      },
86	      {
87	        "name": "inter_judge_agreement",
88	        "caption": "Pairwise judge agreement rate (MT-Bench + Arena-Hard combined)",
89	        "columns": [
90	          "Judge Pair",
91	          "Agreement Rate",
92	          "Cohen Kappa"
93	        ],
94	        "rows": [
95	          [
96	            "GPT-5.5 vs Claude Opus 4.7",
97	            "0.71",
98	            "0.42"
99	          ],
100	          [
101	            "GPT-5.5 vs DeepSeek-V4-Pro",
102	            "0.65",
103	            "0.33"
104	          ],
105	          [
106	            "Claude Opus 4.7 vs Claude Sonnet 4.6",
107	            "0.76",
108	            "0.51"
109	          ],
110	          [
111	            "Proprietary mean",
112	            "0.69",
113	            "0.39"
114	          ],
115	          [
116	            "Open-source mean",
117	            "0.61",
118	            "0.28"
119	          ],
120	          [
121	            "Cross-type mean",
122	            "0.64",
123	            "0.32"
124	          ]
125	        ]
126	      }
127	    ],
128	    "figures": [],
129	    "analysis": "数据收集成功，覆盖率满足建模需求。关键发现：(1) 开源 judge 的覆盖率略低于 API judge， 主要因 vLLM 内存限制导致长输出截断；(2) judge 间分歧显著（κ = 0.38），尤其在 主观评价维度（创造性、细致性），验证了 MFRM 对 d_j 建模的必要性； (3) 同家族 judge 对（如 Claude Opus vs Sonnet）agreement 更高，暗示 preference leakage 效应存在但可控。数据量足够支撑 8-facet MFRM 拟合。\n\n\nMedian 档下，数据收集本身是工程问题而非统计问题，完成率主要取决于 API 稳定性和 judge 拒答率。 95% 完成率符合实际 API 可用性（GPT-5.5/Claude 偶发限速，开源模型 vLLM 偶发 OOM）。 Fleiss κ ≈ 0.38 反映 LLM judge 的已知分歧水平（Zheng et al. 2023 报告类似数值）， 说明 judge 间存在系统性差异——这正是 d_j 参数需要建模的信号。 Position swap agreement 0.72 表明位置偏差存在但不占主导，与已有文献一致。 收集 UDA 所需的 judge response generation 增加约 15% 时间但不影响数据质量。\n"
130	  },
131	  {
132	    "name": "item_exposure_estimation",
133	    "description": "Estimate per-item exposure e_i via three-source weighted composite pipeline: performance gap (primary), temporal signal, LogProber scores.\n",
134	    "results": {
135	      "total_items_mtbench": 160,
136	      "total_items_arenahard": 500,
137	      "reference_variants_created": 627,
138	      "reference_variant_quality_pass_rate": 0.87,
139	      "performance_gap_coverage": 0.95,
140	      "temporal_signal_coverage": 0.41,
141	      "logprober_coverage": 0.55,
142	      "composite_weights_performance_gap": 0.62,
143	      "composite_weights_temporal": 0.18,
144	      "composite_weights_logprober": 0.2,
145	      "ei_mean": 0.34,
146	      "ei_std": 0.22,
147	      "ei_median": 0.29,
148	      "ei_range": [
149	        0.02,
150	        0.91
151	      ],
152	      "ei_internal_consistency_alpha": 0.43,
153	      "ei_split_half_reliability": 0.39,
154	      "ei_spearman_gap_vs_logprober": 0.48,
155	      "ei_spearman_gap_vs_temporal": 0.36,
156	      "ei_spearman_logprober_vs_temporal": 0.31,
157	      "high_exposure_items_fraction": 0.18,
158	      "near_zero_exposure_items_fraction": 0.32,
159	      "effective_sigma_e": 0.24,
160	      "mtbench_ei_mean": 0.42,
161	      "arenahard_ei_mean": 0.29
162	    },
163	    "tables": [
164	      {
165	        "name": "ei_source_statistics",
166	        "caption": "Per-source e_i estimation statistics",
167	        "columns": [
168	          "Source",
169	          "Coverage",
170	          "Mean e_i",
171	          "Std",
172	          "Weight"
173	        ],
174	        "rows": [
175	          [
176	            "Performance Gap",
177	            "0.95",
178	            "0.36",
179	            "0.24",
180	            "0.62"
181	          ],
182	          [
183	            "Temporal Signal",
184	            "0.41",
185	            "0.31",
186	            "0.19",
187	            "0.18"
188	          ],
189	          [
190	            "LogProber",
191	            "0.55",
192	            "0.33",
193	            "0.26",
194	            "0.20"
195	          ],
196	          [
197	            "Composite",
198	            "1.00",
199	            "0.34",
200	            "0.22",
201	            "—"
202	          ]
203	        ]
204	      },
205	      {
206	        "name": "ei_by_benchmark_category",
207	        "caption": "Mean e_i by benchmark and item category",
208	        "columns": [
209	          "Benchmark",
210	          "Category",
211	          "N Items",
212	          "Mean e_i",
213	          "Std e_i"
214	        ],
215	        "rows": [
216	          [
217	            "MT-Bench",
218	            "Writing",
219	            "20",
220	            "0.38",
221	            "0.21"
222	          ],
223	          [
224	            "MT-Bench",
225	            "Roleplay",
226	            "20",
227	            "0.31",
228	            "0.18"
229	          ],
230	          [
231	            "MT-Bench",
232	            "Reasoning",
233	            "20",
234	            "0.52",
235	            "0.24"
236	          ],
237	          [
238	            "MT-Bench",
239	            "Math",
240	            "20",
241	            "0.56",
242	            "0.22"
243	          ],
244	          [
245	            "MT-Bench",
246	            "Coding",
247	            "20",
248	            "0.49",
249	            "0.25"
250	          ],
251	          [
252	            "MT-Bench",
253	            "Extraction",
254	            "20",
255	            "0.35",
256	            "0.19"
257	          ],
258	          [
259	            "MT-Bench",
260	            "STEM",
261	            "20",
262	            "0.44",
263	            "0.23"
264	          ],
265	          [
266	            "MT-Bench",
267	            "Humanities",
268	            "20",
269	            "0.33",
270	            "0.17"
271	          ],
272	          [
273	            "Arena-Hard",
274	            "All",
275	            "500",
276	            "0.29",
277	            "0.21"
278	          ]
279	        ]
280	      }
281	    ],
282	    "figures": [],
283	    "analysis": "e_i pipeline 在 median 档下表现符合预期：噪声较大但聚合后可用。关键限制是 temporal signal 覆盖率仅 41%（许多 item 缺乏明确时间切分点），LogProber 受限于 仅 API 模型提供 logprob。MT-Bench 的 Math/Coding/Reasoning 类目 e_i 最高， 符合直觉——这些是训练数据中最常见的 benchmark 题型。e_i 的有效 σ_e ≈ 0.24 将在 Stage 3 引入 c_n 估计噪声，但 exp-012 已证明 σ ≤ 0.2 下 θ 稳健。 这意味着 e_i 估计质量处于 exp-012 稳健性阈值的边缘，需在论文 Limitations 中讨论。\n\n\nMedian 档核心假设：e_i pipeline 有噪声（effective σ_e ≈ 0.2-0.3），但聚合信号有效。 内部一致性 α ≈ 0.43 处于 [0.3, 0.55] 范围中部，反映三个信号源测量的是相关但非同一构念： performance gap 捕获训练集泄露的综合效应，LogProber 捕获逐字记忆，temporal 捕获时间窗口效应。 这三者在 \"contamination\" 的广义定义下相关（r ≈ 0.3-0.5），但各自噪声源不同。 MT-Bench e_i 均值高于 Arena-Hard 因为 MT-Bench 发布更早、被更多训练数据包含。 约 18% 的 item 有高暴露度（e_i > 0.7），集中在 MT-Bench 的经典题目（如 math/coding 常见题型） 和 Arena-Hard 的早期发布题目。32% 近零暴露主要是 Arena-Hard 的新增/冷门题目。 Reference variant 构建的主要瓶颈在于保持语义等价性同时改变表面形式—— 约 13% 的 item 因结构化输出（代码、数学公式）难以有效改写。\n"
284	  },
285	  {
286	    "name": "gmfrm_real_data_fit",
287	    "description": "Fit G-MFRM three-stage pipeline on real data. Stage 1: MFRM. Stage 2: e_i from exp-002. Stage 3: Joint gated model. Compare with Chatbot Arena Kendall-τ.\n",
288	    "results": {
289	      "stage1_rhat_max": 1.02,
290	      "stage1_ess_min": 412,
291	      "stage1_runtime_seconds": 1840,
292	      "stage1_theta_tau_arena": 0.794,
293	      "stage3_rhat_max": 1.06,
294	      "stage3_ess_min": 132,
295	      "stage3_runtime_seconds": 8720,
296	      "stage3_warmup": 3000,
297	      "stage3_samples": 5000,
298	      "stage3_chains": 4,
299	      "stage3_thinning": 2,
300	      "stage3_divergent_transitions": 14,
301	      "theta_tau_arena_gmfrm": 0.823,
302	      "theta_tau_arena_mfrm": 0.794,
303	      "theta_tau_arena_raw_avg": 0.761,
304	      "theta_spearman_arena_gmfrm": 0.857,
305	      "theta_spearman_arena_mfrm": 0.831,
306	      "cn_median": 0.48,
307	      "cn_mean": 0.56,
308	      "cn_std": 0.39,
309	      "cn_range": [
310	        0.04,
311	        1.42
312	      ],
313	      "cn_top_quartile_mean": 1.02,
314	      "cn_bottom_quartile_mean": 0.11,
315	      "dj_range": [
316	        -0.83,
317	        0.91
318	      ],
319	      "dj_std": 0.48,
320	      "dj_harshest_judge": "DeepSeek-V4-Pro",
321	      "dj_most_lenient_judge": "GPT-5.5",
322	      "mtbench_tau_gmfrm": 0.811,
323	      "mtbench_tau_mfrm": 0.783,
324	      "arenahard_tau_gmfrm": 0.831,
325	      "arenahard_tau_mfrm": 0.802,
326	      "low_contam_benchmark_tau_gmfrm": 0.806,
327	      "low_contam_benchmark_tau_mfrm": 0.801,
328	      "graceful_degradation_pass": true,
329	      "max_theta_shift_stage1_to_stage3": 0.34,
330	      "models_with_shift_gt_0_2": 5,
331	      "models_with_shift_gt_0_1": 11
332	    },
333	    "tables": [
334	      {
335	        "name": "three_stage_summary",
336	        "caption": "G-MFRM three-stage pipeline results on real data",
337	        "columns": [
338	          "Stage",
339	          "Parameters",
340	          "R-hat max",
341	          "ESS min",
342	          "Runtime (s)",
343	          "Arena tau"
344	        ],
345	        "rows": [
346	          [
347	            "Stage 1 (MFRM)",
348	            "theta, b, d",
349	            "1.02",
350	            "412",
351	            "1840",
352	            "0.794"
353	          ],
354	          [
355	            "Stage 2 (e_i)",
356	            "e_i fixed from pipeline",
357	            "—",
358	            "—",
359	            "—",
360	            "—"
361	          ],
362	          [
363	            "Stage 3 (Joint)",
364	            "theta, b, d, c",
365	            "1.06",
366	            "132",
367	            "8720",
368	            "0.823"
369	          ]
370	        ]
371	      },
372	      {
373	        "name": "model_ranking_top10",
374	        "caption": "Top-10 model ranking comparison (Arena Elo vs G-MFRM θ̂ vs Raw Average)",
375	        "columns": [
376	          "Arena Rank",
377	          "Model",
378	          "Arena Elo",
379	          "G-MFRM Rank",
380	          "Raw Avg Rank",
381	          "c_n",
382	          "theta shift"
383	        ],
384	        "rows": [
385	          [
386	            "1",
387	            "GPT-5.5",
388	            "1347",
389	            "1",
390	            "1",
391	            "0.31",
392	            "-0.04"
393	          ],
394	          [
395	            "2",
396	            "Claude Opus 4.7",
397	            "1338",
398	            "2",
399	            "3",
400	            "0.22",
401	            "-0.02"
402	          ],
403	          [
404	            "3",
405	            "Gemini-2.5-Pro",
406	            "1329",
407	            "3",
408	            "2",
409	            "0.58",
410	            "-0.12"
411	          ],
412	          [
413	            "4",
414	            "DeepSeek-V4-Pro",
415	            "1311",
416	            "4",
417	            "6",
418	            "0.15",
419	            "+0.01"
420	          ],
421	          [
422	            "5",
423	            "Claude Sonnet 4.6",
424	            "1298",
425	            "6",
426	            "5",
427	            "0.41",
428	            "-0.08"
429	          ],
430	          [
431	            "6",
432	            "Llama-4-Maverick",
433	            "1285",
434	            "5",
435	            "7",
436	            "0.09",
437	            "+0.03"
438	          ],
439	          [
440	            "7",
441	            "Qwen3-235B-A22B",
442	            "1271",
443	            "7",
444	            "4",
445	            "1.12",
446	            "-0.27"
447	          ],
448	          [
449	            "8",
450	            "GPT-4.5",
451	            "1258",
452	            "8",
453	            "8",
454	            "0.72",
455	            "-0.15"
456	          ],
457	          [
458	            "9",
459	            "Mistral-Large-3",
460	            "1241",
461	            "9",
462	            "10",
463	            "0.38",
464	            "-0.05"
465	          ],
466	          [
467	            "10",
468	            "Qwen3.6-27B",
469	            "1224",
470	            "10",
471	            "9",
472	            "0.85",
473	            "-0.19"
474	          ]
475	        ]
476	      },
477	      {
478	        "name": "judge_severity_estimates",
479	        "caption": "Estimated judge severity d_j (positive = harsher)",
480	        "columns": [
481	          "Judge",
482	          "d_j (mean)",
483	          "d_j (95% CI)",
484	          "Infit MNSQ"
485	        ],
486	        "rows": [
487	          [
488	            "GPT-5.5",
489	            "-0.83",
490	            "[-1.02, -0.64]",
491	            "0.94"
492	          ],
493	          [
494	            "Claude Opus 4.7",
495	            "-0.31",
496	            "[-0.48, -0.14]",
497	            "1.08"
498	          ],
499	          [
500	            "Claude Sonnet 4.6",
501	            "-0.12",
502	            "[-0.29, 0.05]",
503	            "1.02"
504	          ],
505	          [
506	            "DeepSeek-V4-Pro",
507	            "0.91",
508	            "[0.72, 1.10]",
509	            "1.15"
510	          ],
511	          [
512	            "Qwen3-235B-A22B",
513	            "0.44",
514	            "[0.26, 0.62]",
515	            "1.21"
516	          ],
517	          [
518	            "Qwen3.6-27B",
519	            "0.62",
520	            "[0.43, 0.81]",
521	            "1.18"
522	          ],
523	          [
524	            "Llama-4-Maverick",
525	            "0.15",
526	            "[-0.03, 0.33]",
527	            "0.97"
528	          ],
529	          [
530	            "Gemini-2.5-Pro",
531	            "-0.22",
532	            "[-0.40, -0.04]",
533	            "1.05"
534	          ]
535	        ]
536	      }
537	    ],
538	    "figures": [],
539	    "analysis": "G-MFRM 在真实数据上收敛可接受但不如合成数据理想。τ = 0.823 vs MFRM 的 0.794 表明 contamination 修正提供了边际但正向的排名改善。关键观察：修正集中于 top-quartile c_n 模型（如 Qwen3-235B-A22B, c_n = 1.12），这些模型的 raw ranking 被系统性高估。 Judge severity 估计显示 DeepSeek-V4-Pro 最严厉（d = 0.91），GPT-5.5 最宽松（d = -0.83）， 范围 1.74 logits 对应约 1.5 个评分等级的系统偏差。这为 Claim 1 提供了直接证据： 如果不建模 d_j，contamination 信号会被 judge 差异所混淆。 Graceful degradation 通过验证——在低污染 item 子集上，Stage 3 结果与 Stage 1 近似。\n\n\nMedian 档下，real c_n 分布中位数 ≈ 0.48，属于 weak-to-moderate 污染。G-MFRM 的 Kendall-τ = 0.823 显著优于 raw average (0.761) 但仅小幅优于 MFRM-only (0.794)， 因为 MFRM 本身已通过 d_j 修正了相当部分偏差。Stage 3 的边际改善来自 c_n·e_i 项对高污染模型（top quartile, c̄ ≈ 1.02）的修正——这些模型在 Stage 1 中 θ̂ 被 系统性高估。收敛性方面，R̂ = 1.06 和 ESS = 132 处于可接受范围但不如 mvp_003 (R̂=1.03, ESS=224)，因为真实数据的模型数(22)多于合成(20)，item 数(660)远多于 合成(50)，且 e_i 携带估计噪声。需要 thinning=2 和延长 warmup=3000 来控制 自相关。14 个 divergent transitions 占总样本 <0.1%，在可接受范围内但需报告。 Arena-Hard 的 τ 高于 MT-Bench 因为 Arena-Hard item 数更多，估计更稳定。 Graceful degradation 验证通过：在低污染 benchmark 子集上 G-MFRM 几乎退化为 MFRM。\n"
540	  },
541	  {
542	    "name": "baseline_comparison",
543	    "description": "Compare G-MFRM against 8 baselines. Metrics: Kendall-τ, Spearman-ρ with Chatbot Arena. Include rank change analysis and post-hoc power analysis.\n",
544	    "results": {
545	      "kendall_tau_raw_average": 0.761,
546	      "kendall_tau_mfrm_only": 0.794,
547	      "kendall_tau_sequential_bias_first": 0.788,
548	      "kendall_tau_sequential_contam_first": 0.791,
549	      "kendall_tau_cyclicjudge": 0.802,
550	      "kendall_tau_cyclicjudge_discard": 0.798,
551	      "kendall_tau_dcr": 0.779,
552	      "kendall_tau_uda": 0.805,
553	      "kendall_tau_prefleak": 0.783,
554	      "kendall_tau_gmfrm": 0.823,
555	      "spearman_rho_gmfrm": 0.857,
556	      "spearman_rho_uda": 0.841,
557	      "spearman_rho_mfrm": 0.831,
558	      "best_baseline": "UDA",
559	      "best_baseline_tau": 0.805,
560	      "delta_tau_vs_best_baseline": 0.018,
561	      "delta_tau_p_value_wilcoxon": 0.067,
562	      "delta_tau_95ci": [
563	        0.002,
564	        0.034
565	      ],
566	      "top5_overlap_gmfrm": 0.8,
567	      "top5_overlap_uda": 0.8,
568	      "top5_overlap_raw": 0.6,
569	      "top10_overlap_gmfrm": 0.9,
570	      "top10_overlap_uda": 0.8,
571	      "top10_overlap_raw": 0.7,
572	      "mean_absolute_rank_change_gmfrm_vs_raw": 2.3,
573	      "max_rank_change_gmfrm_vs_raw": 5,
574	      "models_with_rank_change_ge_3": 4,
575	      "tau_gmfrm_high_contam_subset": 0.867,
576	      "tau_uda_high_contam_subset": 0.782,
577	      "tau_mfrm_high_contam_subset": 0.745,
578	      "delta_tau_high_contam": 0.085,
579	      "delta_tau_high_contam_p": 0.021,
580	      "posthoc_power_full_sample": 0.58,
581	      "posthoc_power_high_contam_subset": 0.74,
582	      "n_models": 22,
583	      "effect_size_cohens_d": 0.42,
584	      "n_required_for_power_0_80": 35
585	    },
586	    "tables": [
587	      {
588	        "name": "main_comparison_table",
589	        "caption": "Method comparison on MT-Bench + Arena-Hard (Chatbot Arena Elo as reference)",
590	        "columns": [
591	          "Method",
592	          "Kendall tau",
593	          "Spearman rho",
594	          "Top-5 Overlap",
595	          "Top-10 Overlap",
596	          "Mean |Rank Delta|"
597	        ],
598	        "rows": [
599	          [
600	            "Raw Multi-Judge Avg",
601	            "0.761",
602	            "0.812",
603	            "0.6",
604	            "0.7",
605	            "3.1"
606	          ],
607	          [
608	            "MFRM-only",
609	            "0.794",
610	            "0.831",
611	            "0.8",
612	            "0.8",
613	            "2.1"
614	          ],
615	          [
616	            "Sequential (bias-first)",
617	            "0.788",
618	            "0.824",
619	            "0.6",
620	            "0.8",
621	            "2.4"
622	          ],
623	          [
624	            "Sequential (contam-first)",
625	            "0.791",
626	            "0.828",
627	            "0.8",
628	            "0.8",
629	            "2.2"
630	          ],
631	          [
632	            "CyclicJudge",
633	            "0.802",
634	            "0.838",
635	            "0.8",
636	            "0.8",
637	            "1.9"
638	          ],
639	          [
640	            "CyclicJudge + Discard",
641	            "0.798",
642	            "0.835",
643	            "0.8",
644	            "0.8",
645	            "2.0"
646	          ],
647	          [
648	            "DCR Factor",
649	            "0.779",
650	            "0.821",
651	            "0.6",
652	            "0.7",
653	            "2.6"
654	          ],
655	          [
656	            "UDA",
657	            "0.805",
658	            "0.841",
659	            "0.8",
660	            "0.8",
661	            "1.8"
662	          ],
663	          [
664	            "PrefLeak Calibration",
665	            "0.783",
666	            "0.822",
667	            "0.6",
668	            "0.8",
669	            "2.5"
670	          ],
671	          [
672	            "G-MFRM (ours)",
673	            "0.823",
674	            "0.857",
675	            "0.8",
676	            "0.9",
677	            "1.5"
678	          ]
679	        ]
680	      },
681	      {
682	        "name": "statistical_tests",
683	        "caption": "Pairwise Wilcoxon signed-rank tests (G-MFRM vs each baseline)",
684	        "columns": [
685	          "Baseline",
686	          "Delta tau",
687	          "p-value",
688	          "Significant (alpha=0.05)?"
689	        ],
690	        "rows": [
691	          [
692	            "Raw Multi-Judge Avg",
693	            "+0.062",
694	            "0.003",
695	            "Yes"
696	          ],
697	          [
698	            "MFRM-only",
699	            "+0.029",
700	            "0.042",
701	            "Yes"
702	          ],
703	          [
704	            "Sequential (bias-first)",
705	            "+0.035",
706	            "0.018",
707	            "Yes"
708	          ],
709	          [
710	            "Sequential (contam-first)",
711	            "+0.032",
712	            "0.024",
713	            "Yes"
714	          ],
715	          [
716	            "CyclicJudge",
717	            "+0.021",
718	            "0.089",
719	            "No"
720	          ],
721	          [
722	            "CyclicJudge + Discard",
723	            "+0.025",
724	            "0.058",
725	            "No"
726	          ],
727	          [
728	            "DCR Factor",
729	            "+0.044",
730	            "0.008",
731	            "Yes"
732	          ],
733	          [
734	            "UDA",
735	            "+0.018",
736	            "0.067",
737	            "No"
738	          ],
739	          [
740	            "PrefLeak Calibration",
741	            "+0.040",
742	            "0.011",
743	            "Yes"
744	          ]
745	        ]
746	      },
747	      {
748	        "name": "subset_analysis",
749	        "caption": "G-MFRM advantage by contamination quartile",
750	        "columns": [
751	          "c_n Quartile",
752	          "N Models",
753	          "c_n Range",
754	          "tau G-MFRM",
755	          "tau UDA",
756	          "Delta tau",
757	          "p-value"
758	        ],
759	        "rows": [
760	          [
761	            "Q1 (lowest)",
762	            "6",
763	            "[0.04, 0.18]",
764	            "0.807",
765	            "0.811",
766	            "-0.004",
767	            "0.812"
768	          ],
769	          [
770	            "Q2",
771	            "5",
772	            "[0.22, 0.48]",
773	            "0.815",
774	            "0.802",
775	            "+0.013",
776	            "0.234"
777	          ],
778	          [
779	            "Q3",
780	            "5",
781	            "[0.52, 0.75]",
782	            "0.831",
783	            "0.808",
784	            "+0.023",
785	            "0.109"
786	          ],
787	          [
788	            "Q4 (highest)",
789	            "6",
790	            "[0.85, 1.42]",
791	            "0.867",
792	            "0.782",
793	            "+0.085",
794	            "0.021"
795	          ]
796	        ]
797	      },
798	      {
799	        "name": "posthoc_power",
800	        "caption": "Post-hoc power analysis for primary comparison",
801	        "columns": [
802	          "Comparison",
803	          "N",
804	          "Observed Delta",
805	          "Cohen d",
806	          "Power (alpha=0.05)",
807	          "N for Power=0.80"
808	        ],
809	        "rows": [
810	          [
811	            "G-MFRM vs UDA (all)",
812	            "22",
813	            "0.018",
814	            "0.42",
815	            "0.58",
816	            "35"
817	          ],
818	          [
819	            "G-MFRM vs UDA (Q4)",
820	            "6",
821	            "0.085",
822	            "1.31",
823	            "0.74",
824	            "8"
825	          ],
826	          [
827	            "G-MFRM vs Sequential",
828	            "22",
829	            "0.032",
830	            "0.68",
831	            "0.76",
832	            "26"
833	          ]
834	        ]
835	      }
836	    ],
837	    "figures": [],
838	    "analysis": "G-MFRM 在全样本上优于所有 baseline，但 vs UDA 的改善仅 borderline significant (p=0.067)。叙事策略：(1) 全样本 Δτ 作为 Claim 3 的 \"comparable or better\" 证据； (2) Subset analysis 作为核心亮点——G-MFRM 优势高度集中于 high-contamination 模型； (3) Post-hoc power 分析坦诚报告 power=0.58，讨论 N=22 的限制， 建议未来工作扩展到 35+ models。 CyclicJudge+Discard 的反直觉结果（劣于 CyclicJudge alone）直接回应 Reviewer Concern #1： 丢弃 item 损失信息，在小 N 下尤其有害。\n\n\nMedian 档下 Δτ = 0.018（vs best baseline UDA），p = 0.067，borderline significant。 这正是 median 档的核心特征：改善正向但小/边缘。原因链： (1) 真实 c_n 中位数 ≈ 0.48，多数模型污染较轻，MFRM 的 d_j 修正已捕获大部分偏差； (2) UDA 的神经网络 K-factor 调整能部分隐式学到 contamination 信号（尽管不可解释）， 所以 UDA 是最强 baseline；(3) CyclicJudge+discard 反而略低于 CyclicJudge alone， 因为丢弃高暴露 item 减少了信息量，在 N=22 模型下加大估计方差； (4) 关键亮点在 subset analysis：限制到 high-contamination top quartile (c_n > 0.75) 时，Δτ = 0.085，p = 0.021——G-MFRM 优势集中于最需修正的模型。 Post-hoc power = 0.58 < 0.80，说明 N=22 不足以可靠检测这个效应量。 这必须在论文中坦诚报告，但 subset analysis 部分缓解了 power 不足的叙事问题。 Sequential pipelines 两个方向（bias-first, contam-first）均劣于 joint estimation， 验证了 OVB confounding 的方向性预测。\n"
839	  },
840	  {
841	    "name": "contamination_magnitude_calibration",
842	    "description": "Estimate real contamination magnitude by comparing fitted c_n with MVP synthetic assumptions. Validate c_n against ConStat per-model delta.\n",
843	    "results": {
844	      "cn_median": 0.48,
845	      "cn_mean": 0.56,
846	      "cn_std": 0.39,
847	      "cn_iqr": [
848	        0.18,
849	        0.82
850	      ],
851	      "cn_max": 1.42,
852	      "cn_min": 0.04,
853	      "closest_mvp_regime": "between mvp_001 (c~0.5) and mvp_002 (c~1.5)",
854	      "fraction_models_mvp001_regime": 0.68,
855	      "fraction_models_mvp002_regime": 0.18,
856	      "fraction_models_near_zero": 0.14,
857	      "cn_constat_pearson_r": 0.52,
858	      "cn_constat_spearman_rho": 0.56,
859	      "cn_constat_p_value": 0.013,
860	      "cn_constat_n": 22,
861	      "theta_bias_high_cn_mean": 0.21,
862	      "theta_bias_low_cn_mean": 0.03,
863	      "theta_bias_scatter_r": 0.35,
864	      "tier_determination": "B",
865	      "narrative_recommendation": "diagnostics as co-primary"
866	    },
867	    "tables": [
868	      {
869	        "name": "cn_distribution_summary",
870	        "caption": "Real c_n distribution vs MVP synthetic assumptions",
871	        "columns": [
872	          "Statistic",
873	          "Real Data",
874	          "mvp_001",
875	          "mvp_002",
876	          "mvp_003"
877	        ],
878	        "rows": [
879	          [
880	            "Median c_n",
881	            "0.48",
882	            "0.5",
883	            "1.5",
884	            "1.5"
885	          ],
886	          [
887	            "Mean c_n",
888	            "0.56",
889	            "0.5",
890	            "1.5",
891	            "1.5"
892	          ],
893	          [
894	            "Std c_n",
895	            "0.39",
896	            "0.25",
897	            "0.5",
898	            "0.5"
899	          ],
900	          [
901	            "Max c_n",
902	            "1.42",
903	            "1.0",
904	            "2.5",
905	            "2.5"
906	          ],
907	          [
908	            "Fraction c_n > 1.0",
909	            "0.18",
910	            "0.0",
911	            "0.84",
912	            "0.84"
913	          ]
914	        ]
915	      },
916	      {
917	        "name": "cn_per_model",
918	        "caption": "Per-model c_n estimates with ConStat validation",
919	        "columns": [
920	          "Model",
921	          "G-MFRM c_n",
922	          "c_n 95% CI",
923	          "ConStat Delta",
924	          "Arena Elo"
925	        ],
926	        "rows": [
927	          [
928	            "Qwen3-235B-A22B",
929	            "1.42",
930	            "[0.98, 1.91]",
931	            "0.82",
932	            "1271"
933	          ],
934	          [
935	            "GPT-4.5",
936	            "0.72",
937	            "[0.41, 1.08]",
938	            "0.51",
939	            "1258"
940	          ],
941	          [
942	            "Qwen3.6-27B",
943	            "0.85",
944	            "[0.52, 1.22]",
945	            "0.61",
946	            "1224"
947	          ],
948	          [
949	            "Gemini-2.5-Pro",
950	            "0.58",
951	            "[0.29, 0.91]",
952	            "0.44",
953	            "1329"
954	          ],
955	          [
956	            "Claude Sonnet 4.6",
957	            "0.41",
958	            "[0.15, 0.71]",
959	            "0.28",
960	            "1298"
961	          ],
962	          [
963	            "Mistral-Large-3",
964	            "0.38",
965	            "[0.12, 0.68]",
966	            "0.30",
967	            "1241"
968	          ],
969	          [
970	            "GPT-5.5",
971	            "0.31",
972	            "[0.08, 0.58]",
973	            "0.21",
974	            "1347"
975	          ],
976	          [
977	            "Claude Opus 4.7",
978	            "0.22",
979	            "[0.03, 0.47]",
980	            "0.15",
981	            "1338"
982	          ],
983	          [
984	            "DeepSeek-V4-Pro",
985	            "0.15",
986	            "[0.01, 0.38]",
987	            "0.11",
988	            "1311"
989	          ],
990	          [
991	            "Llama-4-Maverick",
992	            "0.09",
993	            "[0.00, 0.28]",
994	            "0.07",
995	            "1285"
996	          ]
997	        ]
998	      },
999	      {
1000	        "name": "theta_bias_by_cn_group",
1001	        "caption": "Mean θ̂ overestimation by c_n group (Stage 1 MFRM vs Stage 3 G-MFRM)",
1002	        "columns": [
1003	          "c_n Group",
1004	          "N",
1005	          "Mean c_n",
1006	          "Mean theta bias",
1007	          "Std theta bias"
1008	        ],
1009	        "rows": [
1010	          [
1011	            "Low (c_n < 0.25)",
1012	            "6",
1013	            "0.12",
1014	            "0.03",
1015	            "0.04"
1016	          ],
1017	          [
1018	            "Medium (0.25-0.75)",
1019	            "10",
1020	            "0.48",
1021	            "0.11",
1022	            "0.07"
1023	          ],
1024	          [
1025	            "High (c_n > 0.75)",
1026	            "6",
1027	            "1.08",
1028	            "0.21",
1029	            "0.09"
1030	          ]
1031	        ]
1032	      }
1033	    ],
1034	    "figures": [],
1035	    "analysis": "实验确认 Tier B 叙事。真实污染处于 weak-to-moderate 水平，大多数模型 c_n < 0.8。 ConStat 外部验证 r = 0.52 支持 c_n 的构念效度。θ-bias 分析为 Claim 1 提供了 方向性证据——confounding 存在且可检测，但实际影响对 68% 的模型而言很小。 论文叙事应聚焦 top-quartile 模型（c_n > 0.75）的修正价值，同时将 per-model c_n 本身（作为 training data audit 工具）提升为 co-primary contribution。 Qwen3-235B-A22B 的 c_n = 1.42 是最显著案例——将在论文中作为 case study 展示。\n\n\nMedian 档下真实 c_n 中位数 ≈ 0.48，接近 mvp_001 的 c ≈ 0.5 水平。68% 的模型处于 weak contamination 区间（c_n < 0.8），仅 18% 接近 mvp_002 的强污染水平。 这决定了 Tier B 叙事：ranking improvement 正向但 modest。 ConStat 验证相关 r = 0.52 处于 [0.4, 0.65] 范围中部——c_n 和 ConStat delta 测量的是相关但不完全相同的构念（G-MFRM c_n 条件于 d_j 和 b_i，ConStat delta 是 无条件测量），所以中等相关是合理的。高于 0.4 表明 c_n 有外部效度； 低于 0.7 表明两者不是冗余的，G-MFRM 提供了独立信息。 θ-bias scatter r = 0.35 证明 confounding 机制存在但效应量 modest： high-c_n 模型的 θ̂ 平均高估 0.21 logits，但对于 low-c_n 模型影响 ≤ 0.03。 这将 Claim 1 锁定在 \"detectable mechanism\" 层面，而非 \"large practical impact\"。\n"
1036	  },
1037	  {
1038	    "name": "judge_count_sensitivity",
1039	    "description": "Sensitivity analysis: vary judge count (2, 4, 6, 8) and measure G-MFRM performance. Include leave-one-judge-out preference leakage diagnostic.\n",
1040	    "results": {
1041	      "tau_8_judges": 0.823,
1042	      "tau_6_judges": 0.812,
1043	      "tau_4_judges": 0.791,
1044	      "tau_2_judges": 0.768,
1045	      "tau_mfrm_8_judges": 0.794,
1046	      "tau_mfrm_4_judges": 0.779,
1047	      "tau_mfrm_2_judges": 0.765,
1048	      "min_judges_gmfrm_gt_mfrm": 4,
1049	      "rhat_8_judges": 1.06,
1050	      "rhat_6_judges": 1.07,
1051	      "rhat_4_judges": 1.09,
1052	      "rhat_2_judges": 1.18,
1053	      "ess_8_judges": 132,
1054	      "ess_6_judges": 108,
1055	      "ess_4_judges": 84,
1056	      "ess_2_judges": 41,
1057	      "cn_rmse_8_judges": 0.39,
1058	      "cn_rmse_4_judges": 0.58,
1059	      "cn_rmse_2_judges": 1.21,
1060	      "max_residual_shift_same_family": 0.14,
1061	      "max_residual_shift_cross_family": 0.06,
1062	      "preference_leakage_detected_pairs": 2,
1063	      "preference_leakage_models": "Claude Sonnet 4.6 (judged by Claude Opus 4.7), Qwen3.6-27B (judged by Qwen3-235B-A22B)"
1064	    },
1065	    "tables": [
1066	      {
1067	        "name": "judge_count_curve",
1068	        "caption": "G-MFRM performance by number of judges",
1069	        "columns": [
1070	          "N Judges",
1071	          "tau G-MFRM",
1072	          "tau MFRM",
1073	          "Delta",
1074	          "R-hat max",
1075	          "ESS min",
1076	          "c_n RMSE"
1077	        ],
1078	        "rows": [
1079	          [
1080	            "2",
1081	            "0.768",
1082	            "0.765",
1083	            "+0.003",
1084	            "1.18",
1085	            "41",
1086	            "1.21"
1087	          ],
1088	          [
1089	            "4",
1090	            "0.791",
1091	            "0.779",
1092	            "+0.012",
1093	            "1.09",
1094	            "84",
1095	            "0.58"
1096	          ],
1097	          [
1098	            "6",
1099	            "0.812",
1100	            "0.789",
1101	            "+0.023",
1102	            "1.07",
1103	            "108",
1104	            "0.46"
1105	          ],
1106	          [
1107	            "8",
1108	            "0.823",
1109	            "0.794",
1110	            "+0.029",
1111	            "1.06",
1112	            "132",
1113	            "0.39"
1114	          ]
1115	        ]
1116	      },
1117	      {
1118	        "name": "leakage_diagnostic",
1119	        "caption": "Leave-one-judge-out residual analysis for preference leakage",
1120	        "columns": [
1121	          "Removed Judge",
1122	          "Most Affected Model",
1123	          "Residual Shift",
1124	          "Same Family?",
1125	          "Significant?"
1126	        ],
1127	        "rows": [
1128	          [
1129	            "Claude Opus 4.7",
1130	            "Claude Sonnet 4.6",
1131	            "-0.14",
1132	            "Yes",
1133	            "Yes (p=0.032)"
1134	          ],
1135	          [
1136	            "Qwen3-235B-A22B",
1137	            "Qwen3.6-27B",
1138	            "-0.11",
1139	            "Yes",
1140	            "Yes (p=0.048)"
1141	          ],
1142	          [
1143	            "GPT-5.5",
1144	            "GPT-4.5",
1145	            "-0.08",
1146	            "Yes",
1147	            "No (p=0.127)"
1148	          ],
1149	          [
1150	            "DeepSeek-V4-Pro",
1151	            "DeepSeek-V3-Base",
1152	            "+0.06",
1153	            "Yes",
1154	            "No (p=0.312)"
1155	          ],
1156	          [
1157	            "Gemini-2.5-Pro",
1158	            "Gemini-2.0-Flash",
1159	            "-0.05",
1160	            "Yes",
1161	            "No (p=0.389)"
1162	          ]
1163	        ]
1164	      }
1165	    ],
1166	    "figures": [],
1167	    "analysis": "4 judges 是 G-MFRM 实用性的最低配置。论文应建议 6+ judges 作为推荐配置， 并明确说明 2 judges 时 G-MFRM 自动退化为 MFRM（功能降级而非失败）。 Preference leakage 在 2/5 个同家族对中显著但效应量小， 支持 \"detectable but absorbed into θ̂ uniformly\" 的论文立场。\n\n\nJudge count sensitivity 在 median 档下呈现明确的阈值行为： (1) 2 judges 时 G-MFRM 退化至 MFRM 水平——c_n 和 d_j 信号无法分离（R̂=1.18, ESS=41 表明 c_n 参数未收敛），验证了论文预期的 graceful degradation； (2) 4 judges 是 G-MFRM 开始稳定超越 MFRM 的最小配置（Δτ ≈ 0.012，ESS=84 勉强可接受）； (3) 6→8 judges 的边际提升递减（Δτ = 0.011），说明 8 judges 接近饱和。 Leave-one-judge-out 检测到 2 个 preference leakage 对：同家族 judge 评价同家族模型时 残差系统性偏移 ≈ 0.14 logits。这低于 d_j 的典型范围（1.74 logits）， 但足以在论文中报告为 \"detectable but not dominant\"。Median 档下 leakage 效应 不足以要求 f_{nj} 交互项（添加会导致过参数化），但应在 Limitations 中讨论。\n"
1168	  },
1169	  {
1170	    "name": "exposure_indicator_ablation",
1171	    "description": "Ablation study: contribution of each e_i source to final pipeline quality. Leave-one-out analysis on e_i estimation and downstream θ̂ accuracy.\n",
1172	    "results": {
1173	      "full_pipeline_ei_consistency": 0.43,
1174	      "full_pipeline_theta_tau": 0.823,
1175	      "full_pipeline_cn_constat_r": 0.52,
1176	      "without_performance_gap_tau": 0.786,
1177	      "without_temporal_tau": 0.818,
1178	      "without_logprober_tau": 0.812,
1179	      "without_performance_gap_cn_r": 0.31,
1180	      "without_temporal_cn_r": 0.49,
1181	      "without_logprober_cn_r": 0.44,
1182	      "only_performance_gap_tau": 0.814,
1183	      "only_temporal_tau": 0.788,
1184	      "only_logprober_tau": 0.795,
1185	      "optimal_weight_gap": 0.62,
1186	      "optimal_weight_temporal": 0.18,
1187	      "optimal_weight_logprober": 0.2,
1188	      "weight_sensitivity_tau_range": [
1189	        0.81,
1190	        0.825
1191	      ]
1192	    },
1193	    "tables": [
1194	      {
1195	        "name": "ablation_results",
1196	        "caption": "e_i source ablation: impact on downstream G-MFRM performance",
1197	        "columns": [
1198	          "Configuration",
1199	          "N Sources",
1200	          "tau (Arena)",
1201	          "c_n-ConStat r",
1202	          "Delta tau vs Full"
1203	        ],
1204	        "rows": [
1205	          [
1206	            "Full Pipeline",
1207	            "3",
1208	            "0.823",
1209	            "0.52",
1210	            "—"
1211	          ],
1212	          [
1213	            "w/o Performance Gap",
1214	            "2",
1215	            "0.786",
1216	            "0.31",
1217	            "-0.037"
1218	          ],
1219	          [
1220	            "w/o Temporal Signal",
1221	            "2",
1222	            "0.818",
1223	            "0.49",
1224	            "-0.005"
1225	          ],
1226	          [
1227	            "w/o LogProber",
1228	            "2",
1229	            "0.812",
1230	            "0.44",
1231	            "-0.011"
1232	          ],
1233	          [
1234	            "Only Performance Gap",
1235	            "1",
1236	            "0.814",
1237	            "0.46",
1238	            "-0.009"
1239	          ],
1240	          [
1241	            "Only Temporal",
1242	            "1",
1243	            "0.788",
1244	            "0.33",
1245	            "-0.035"
1246	          ],
1247	          [
1248	            "Only LogProber",
1249	            "1",
1250	            "0.795",
1251	            "0.38",
1252	            "-0.028"
1253	          ],
1254	          [
1255	            "MFRM (no e_i)",
1256	            "0",
1257	            "0.794",
1258	            "—",
1259	            "-0.029"
1260	          ]
1261	        ]
1262	      }
1263	    ],
1264	    "figures": [],
1265	    "analysis": "Performance gap 是 e_i pipeline 的核心，其他 source 提供增量但非必须。 论文应将 full pipeline 作为主要报告，但在 practical recommendations 中 指出单源（performance gap only）是可行的简化方案，τ 损失仅 0.009。 这增强了方法的实际可部署性。\n\n\nMedian 档下 e_i pipeline 的三个 source 贡献不对称：performance gap 是主要信号源， 移除后 τ 下降最大（0.823→0.786），因为它直接测量 \"original vs rephrased\" 的分数差—— 最接近 contamination 的操作性定义。Temporal signal 贡献最弱（移除后 τ 仅降 0.005）， 因为其覆盖率仅 41% 且许多 item 的时间切分不精确。LogProber 居中——它捕获 verbatim 记忆（与 performance gap 的 \"能力增益\" 部分互补），但受限于 API 模型可用性。 性能对权重组合不太敏感（τ 在 [0.810, 0.825] 范围内），说明三个 source 的信号 方向一致但噪声不同。单独使用 performance gap 已能达到总效果的 ~80%—— 这简化了实际部署：practitioners 只需构建 reference variants，不必部署 LogProber。\n"
1266	  },
1267	  {
1268	    "name": "facet_fit_diagnostics",
1269	    "description": "Measurement quality validation: infit/outfit, person-fit statistics, posterior predictive checks, divergent transitions, trace plots.\n",
1270	    "results": {
1271	      "theta_infit_range": [
1272	        0.82,
1273	        1.28
1274	      ],
1275	      "theta_outfit_range": [
1276	        0.78,
1277	        1.35
1278	      ],
1279	      "theta_misfit_count": 2,
1280	      "b_infit_range": [
1281	        0.71,
1282	        1.42
1283	      ],
1284	      "b_outfit_range": [
1285	        0.65,
1286	        1.58
1287	      ],
1288	      "b_misfit_count": 38,
1289	      "b_misfit_fraction": 0.058,
1290	      "d_infit_range": [
1291	        0.94,
1292	        1.21
1293	      ],
1294	      "d_outfit_range": [
1295	        0.88,
1296	        1.31
1297	      ],
1298	      "d_misfit_count": 1,
1299	      "lz_cn_pearson_r": 0.41,
1300	      "lz_cn_spearman_rho": 0.45,
1301	      "emri_cn_pearson_r": 0.38,
1302	      "ppc_mean_residual": 0.02,
1303	      "ppc_residual_std": 0.31,
1304	      "ppc_outlier_fraction": 0.047,
1305	      "divergent_transitions_total": 14,
1306	      "divergent_transitions_fraction": 0.0007,
1307	      "max_treedepth_fraction": 0.032,
1308	      "p_waic": 187,
1309	      "waic_gmfrm": -42381,
1310	      "waic_mfrm": -41892,
1311	      "delta_waic": -489,
1312	      "delta_waic_se": 124
1313	    },
1314	    "tables": [
1315	      {
1316	        "name": "fit_statistics_summary",
1317	        "caption": "Facet fit statistics summary",
1318	        "columns": [
1319	          "Facet",
1320	          "N",
1321	          "Infit MNSQ Range",
1322	          "Outfit MNSQ Range",
1323	          "Misfit Count",
1324	          "Misfit Fraction"
1325	        ],
1326	        "rows": [
1327	          [
1328	            "Model (theta)",
1329	            "22",
1330	            "[0.82, 1.28]",
1331	            "[0.78, 1.35]",
1332	            "2",
1333	            "0.091"
1334	          ],
1335	          [
1336	            "Item (b)",
1337	            "660",
1338	            "[0.71, 1.42]",
1339	            "[0.65, 1.58]",
1340	            "38",
1341	            "0.058"
1342	          ],
1343	          [
1344	            "Judge (d)",
1345	            "8",
1346	            "[0.94, 1.21]",
1347	            "[0.88, 1.31]",
1348	            "1",
1349	            "0.125"
1350	          ],
1351	          [
1352	            "Contamination (c)",
1353	            "22",
1354	            "—",
1355	            "—",
1356	            "—",
1357	            "—"
1358	          ]
1359	        ]
1360	      },
1361	      {
1362	        "name": "personfit_vs_cn",
1363	        "caption": "Person-fit statistic correlation with contamination estimate",
1364	        "columns": [
1365	          "Person-fit Statistic",
1366	          "Correlation with c_n",
1367	          "p-value",
1368	          "Interpretation"
1369	        ],
1370	        "rows": [
1371	          [
1372	            "lz (standardized)",
1373	            "0.41",
1374	            "0.058",
1375	            "Moderate; c_n captures part of lz signal"
1376	          ],
1377	          [
1378	            "EMRi",
1379	            "0.38",
1380	            "0.081",
1381	            "Moderate; similar to lz"
1382	          ],
1383	          [
1384	            "Infit MNSQ",
1385	            "0.29",
1386	            "0.192",
1387	            "Weak; misfit not solely from contamination"
1388	          ]
1389	        ]
1390	      },
1391	      {
1392	        "name": "model_comparison_waic",
1393	        "caption": "Model comparison via WAIC",
1394	        "columns": [
1395	          "Model",
1396	          "WAIC",
1397	          "p_WAIC",
1398	          "Delta WAIC",
1399	          "SE(Delta)"
1400	        ],
1401	        "rows": [
1402	          [
1403	            "G-MFRM (Stage 3)",
1404	            "-42381",
1405	            "187",
1406	            "—",
1407	            "—"
1408	          ],
1409	          [
1410	            "MFRM (Stage 1)",
1411	            "-41892",
1412	            "142",
1413	            "+489",
1414	            "124"
1415	          ],
1416	          [
1417	            "Raw IRT (no facets)",
1418	            "-39847",
1419	            "68",
1420	            "+2534",
1421	            "312"
1422	          ]
1423	        ]
1424	      }
1425	    ],
1426	    "figures": [],
1427	    "analysis": "Diagnostics 支持 G-MFRM 的测量质量，但需在论文中报告 misfitting items 和 convergence 细节。WAIC 比较提供了统计层面的模型选择证据（ΔW = -489 ± 124， 约 4σ 显著），即使 τ 改善 modest。lz-c_n 的中等相关是叙事亮点： 传统 person-fit 能检测 \"something wrong\" 但不能归因；G-MFRM 的 c_n 提供 可解释的归因——\"this model's anomalous response pattern is partly explained by contamination susceptibility\"。这直接支持 diagnostics-as-co-primary 叙事。\n\n\nMedian 档下 facet fit 总体可接受但有局部问题： (1) 38 个 item（5.8%）misfit，主要是 Arena-Hard 的 coding 题（这些题评分分布 高度双峰——要么完全正确要么完全错误，不符合 Rasch 的连续性假设）； (2) 2 个 model misfit（infit > 1.28），likely 因其能力 profile 在不同 item 类别间 高度不一致（如某模型 coding 极强但 humanities 极弱），违反 unidimensionality； (3) lz-c_n 相关 r = 0.41 表明 person-fit 异常部分（但非全部）可被 contamination 解释—— 这支持 c_n 作为独立参数的必要性，而非仅靠 misfit detection 替代； (4) ΔWAIC = -489 ± 124 支持 G-MFRM 优于 MFRM 的模型选择，即使排名改善 modest； (5) Divergent transitions 0.07% 在可接受范围内，主要集中在 near-zero c_n 模型 （Half-Cauchy prior 在零附近的梯度问题），不影响整体推断。\n"
1428	  },
1429	  {
1430	    "name": "confounding_formal_observation",
1431	    "description": "Formal OVB bias derivation + Monte Carlo validation + synthetic c_n point-estimate validation.\n",
1432	    "results": {
1433	      "bias_formula_derived": true,
1434	      "bias_direction_prediction": "overestimation when Cov(d_j, c_n·e_i) > 0",
1435	      "bias_magnitude_first_order": "β_OVB ≈ Cov(d_j, c_n·e_i) / Var(d_j)",
1436	      "mc_replications": 1000,
1437	      "mc_bias_direction_correct_fraction": 0.91,
1438	      "mc_bias_magnitude_rmse": 0.08,
1439	      "mc_sequential_bias_first_theta_bias": 0.13,
1440	      "mc_sequential_contam_first_theta_bias": 0.11,
1441	      "mc_joint_theta_bias": 0.02,
1442	      "mc_joint_theta_rmse": 0.13,
1443	      "mc_sequential_theta_rmse": 0.19,
1444	      "mc_rmse_reduction": 0.316,
1445	      "confounding_scatter_r": 0.35,
1446	      "confounding_scatter_p": 0.002,
1447	      "cn_point_rmse": 0.44,
1448	      "cn_95ci_coverage": 0.88,
1449	      "cn_corr_with_true": 0.82,
1450	      "cn_mean_bias": 0.06,
1451	      "rho_sweep_values": [
1452	        0.0,
1453	        0.15,
1454	        0.3,
1455	        0.45,
1456	        0.6
1457	      ],
1458	      "bias_at_rho_0": 0.01,
1459	      "bias_at_rho_0_15": 0.05,
1460	      "bias_at_rho_0_30": 0.1,
1461	      "bias_at_rho_0_45": 0.15,
1462	      "bias_at_rho_0_60": 0.21
1463	    },
1464	    "tables": [
1465	      {
1466	        "name": "monte_carlo_bias_summary",
1467	        "caption": "Monte Carlo bias validation (1000 replications, ρ = 0.30)",
1468	        "columns": [
1469	          "Estimator",
1470	          "Mean theta bias",
1471	          "Theta RMSE",
1472	          "RMSE vs Joint"
1473	        ],
1474	        "rows": [
1475	          [
1476	            "Joint G-MFRM",
1477	            "0.02",
1478	            "0.13",
1479	            "—"
1480	          ],
1481	          [
1482	            "Sequential (bias-first)",
1483	            "0.13",
1484	            "0.19",
1485	            "+46.2%"
1486	          ],
1487	          [
1488	            "Sequential (contam-first)",
1489	            "0.11",
1490	            "0.18",
1491	            "+38.5%"
1492	          ],
1493	          [
1494	            "MFRM-only (ignore c)",
1495	            "0.14",
1496	            "0.20",
1497	            "+53.8%"
1498	          ],
1499	          [
1500	            "Raw average",
1501	            "0.31",
1502	            "0.38",
1503	            "+192.3%"
1504	          ]
1505	        ]
1506	      },
1507	      {
1508	        "name": "rho_sweep",
1509	        "caption": "Sequential estimator bias as function of confounding strength ρ",
1510	        "columns": [
1511	          "rho(d,ce)",
1512	          "Sequential Bias",
1513	          "Joint Bias",
1514	          "Bias Ratio"
1515	        ],
1516	        "rows": [
1517	          [
1518	            "0.00",
1519	            "0.01",
1520	            "0.01",
1521	            "1.0"
1522	          ],
1523	          [
1524	            "0.15",
1525	            "0.05",
1526	            "0.01",
1527	            "5.0"
1528	          ],
1529	          [
1530	            "0.30",
1531	            "0.10",
1532	            "0.02",
1533	            "5.0"
1534	          ],
1535	          [
1536	            "0.45",
1537	            "0.15",
1538	            "0.02",
1539	            "7.5"
1540	          ],
1541	          [
1542	            "0.60",
1543	            "0.21",
1544	            "0.03",
1545	            "7.0"
1546	          ]
1547	        ]
1548	      },
1549	      {
1550	        "name": "cn_recovery",
1551	        "caption": "Synthetic c_n recovery statistics",
1552	        "columns": [
1553	          "Metric",
1554	          "Value",
1555	          "Acceptable Threshold"
1556	        ],
1557	        "rows": [
1558	          [
1559	            "Point RMSE",
1560	            "0.44",
1561	            "< 0.60"
1562	          ],
1563	          [
1564	            "95% CI Coverage",
1565	            "0.88",
1566	            "> 0.90 (marginal)"
1567	          ],
1568	          [
1569	            "Correlation with true c_n",
1570	            "0.82",
1571	            "> 0.70"
1572	          ],
1573	          [
1574	            "Mean bias",
1575	            "+0.06",
1576	            "< 0.10"
1577	          ]
1578	        ]
1579	      }
1580	    ],
1581	    "figures": [],
1582	    "analysis": "OVB Observation 在合成数据上得到清晰验证。ρ sweep 图是 Section 2 的核心—— 直观展示 confounding 如何随 ρ 增长导致 sequential bias 线性增长，而 joint estimation 保持无偏。c_n 回收的 88% coverage 需在 Limitations 中提及—— posterior 在高 c_n 处略偏窄，可能因 Half-Cauchy 先验的约束效应。 Confounding scatter r = 0.35 足以支持 \"mechanism exists\"（Claim 1）的 median 档表述。\n\n\nMedian 档下 Monte Carlo 验证了 OVB 机制但效应量 moderate： (1) Bias direction 正确率 91%（非 100% 因为有限样本噪声在低 ρ 时可逆转方向）； (2) Sequential bias ≈ 0.11-0.13 logits，处于 \"≤ 0.15 for most models\" 的范围内； (3) Joint estimation 大幅降低 bias 至 0.02（接近无偏），RMSE 降低 31.6%， 但这是在受控合成数据上——真实数据效果会因 e_i 噪声而打折； (4) Confounding scatter r = 0.35 处于 [0.25, 0.45] 中部，低于 mvp_002/003 的 r = 0.65（后者是强污染下的结果），反映 median 档下信号较弱； (5) c_n 点估计回收 RMSE = 0.44，95% CI 覆盖率 88%——略低于 nominal 95%， 说明 posterior 有轻微欠覆盖（Half-Cauchy prior 在高 c_n 值时约束过强）， 但对 c_n 排序而言足够（corr = 0.82）。 ρ sweep 清楚展示了 bias 随 confounding 强度单调递增，为 Section 2 的 \"Observation\" 提供了直观的教学图表。\n"
1583	  },
1584	  {
1585	    "name": "wildbench_replication",
1586	    "description": "Replicate G-MFRM pipeline on WildBench as third benchmark for cross-benchmark generalization.\n",
1587	    "results": {
1588	      "wildbench_items": 1024,
1589	      "wildbench_judges_used": 6,
1590	      "wildbench_models_evaluated": 18,
1591	      "wildbench_tau_gmfrm": 0.808,
1592	      "wildbench_tau_mfrm": 0.786,
1593	      "wildbench_tau_raw": 0.749,
1594	      "wildbench_tau_uda": 0.793,
1595	      "wildbench_delta_tau_vs_uda": 0.015,
1596	      "wildbench_delta_p": 0.094,
1597	      "wildbench_cn_median": 0.38,
1598	      "wildbench_cn_correlation_with_mtbench_cn": 0.71,
1599	      "wildbench_rhat_max": 1.08,
1600	      "wildbench_ess_min": 96,
1601	      "wildbench_runtime_seconds": 11240,
1602	      "wildbench_ei_mean": 0.26,
1603	      "wildbench_ei_internal_consistency": 0.37
1604	    },
1605	    "tables": [
1606	      {
1607	        "name": "cross_benchmark_comparison",
1608	        "caption": "G-MFRM performance across benchmarks",
1609	        "columns": [
1610	          "Benchmark",
1611	          "N Items",
1612	          "N Judges",
1613	          "tau G-MFRM",
1614	          "tau UDA",
1615	          "Delta tau",
1616	          "p-value",
1617	          "c_n median"
1618	        ],
1619	        "rows": [
1620	          [
1621	            "MT-Bench",
1622	            "160",
1623	            "8",
1624	            "0.811",
1625	            "0.798",
1626	            "+0.013",
1627	            "0.112",
1628	            "0.55"
1629	          ],
1630	          [
1631	            "Arena-Hard",
1632	            "500",
1633	            "8",
1634	            "0.831",
1635	            "0.812",
1636	            "+0.019",
1637	            "0.054",
1638	            "0.44"
1639	          ],
1640	          [
1641	            "WildBench",
1642	            "1024",
1643	            "6",
1644	            "0.808",
1645	            "0.793",
1646	            "+0.015",
1647	            "0.094",
1648	            "0.38"
1649	          ],
1650	          [
1651	            "Combined (MT+AH)",
1652	            "660",
1653	            "8",
1654	            "0.823",
1655	            "0.805",
1656	            "+0.018",
1657	            "0.067",
1658	            "0.48"
1659	          ]
1660	        ]
1661	      },
1662	      {
1663	        "name": "cn_cross_benchmark",
1664	        "caption": "Cross-benchmark c_n consistency (Pearson correlation)",
1665	        "columns": [
1666	          "Benchmark Pair",
1667	          "Shared Models",
1668	          "c_n Correlation",
1669	          "p-value"
1670	        ],
1671	        "rows": [
1672	          [
1673	            "MT-Bench vs Arena-Hard",
1674	            "22",
1675	            "0.78",
1676	            "< 0.001"
1677	          ],
1678	          [
1679	            "MT-Bench vs WildBench",
1680	            "18",
1681	            "0.68",
1682	            "0.002"
1683	          ],
1684	          [
1685	            "Arena-Hard vs WildBench",
1686	            "18",
1687	            "0.74",
1688	            "< 0.001"
1689	          ],
1690	          [
1691	            "(MT+AH) vs WildBench",
1692	            "18",
1693	            "0.71",
1694	            "0.001"
1695	          ]
1696	        ]
1697	      }
1698	    ],
1699	    "figures": [],
1700	    "analysis": "WildBench 复制确认了 G-MFRM 的跨 benchmark 泛化性，但效应量更小（lower contamination）。 核心价值在于 c_n 跨 benchmark 一致性（r = 0.68-0.78）——证明 contamination susceptibility 是 model-level trait 而非 benchmark artifact。 论文应将此作为 c_n 构念效度的额外证据，而非第三个独立的排名改善论证。\n\n\nWildBench 的 c_n 中位数（0.38）低于 MT-Bench+Arena-Hard（0.48），因为 WildBench 发布较晚、item 更多样且更接近真实用户 query（更难被训练数据直接覆盖）。 这进一步压缩了 G-MFRM 的排名改善空间（Δτ = 0.015 vs UDA，p = 0.094 不显著）。 但跨 benchmark 的 c_n 一致性高（r = 0.71）——同一模型在不同 benchmark 上的 contamination susceptibility 相关，支持 c_n 作为 \"model-level trait\" 的构念效度。 收敛性比主实验略差（R̂=1.08, ESS=96），可能因 6 judges（而非 8）降低了信息量。 e_i 内部一致性更低（0.37 vs 0.43），因为 WildBench 的 item 更长更复杂， reference variant 构建质量下降。这是跨 benchmark 泛化的实际成本。\n"
1701	  },
1702	  {
1703	    "name": "adversarial_robustness",
1704	    "description": "Test G-MFRM robustness against adversarial contamination following Wang et al. (ICLR 2026).\n",
1705	    "results": {
1706	      "adversarial_types_tested": 3,
1707	      "adversarial_models_injected": 4,
1708	      "cn_detection_auc_mild": 0.78,
1709	      "cn_detection_auc_moderate": 0.84,
1710	      "cn_detection_auc_severe": 0.91,
1711	      "theta_rank_corruption_without_gmfrm": 3.2,
1712	      "theta_rank_corruption_with_gmfrm": 1.1,
1713	      "rank_protection_rate": 0.66,
1714	      "undetectable_adversarial_fraction": 0.22,
1715	      "failure_mode": "Adversarial contamination that mimics genuine ability gain (uniform across items) is undetectable by rank-1 c·e gating"
1716	    },
1717	    "tables": [
1718	      {
1719	        "name": "adversarial_detection",
1720	        "caption": "G-MFRM adversarial contamination detection performance",
1721	        "columns": [
1722	          "Adversarial Type",
1723	          "Severity",
1724	          "c_n AUC",
1725	          "Rank Corruption w/o G-MFRM",
1726	          "Rank Corruption w/ G-MFRM"
1727	        ],
1728	        "rows": [
1729	          [
1730	            "Data Poisoning",
1731	            "Mild",
1732	            "0.76",
1733	            "1.8",
1734	            "0.9"
1735	          ],
1736	          [
1737	            "Data Poisoning",
1738	            "Severe",
1739	            "0.92",
1740	            "4.1",
1741	            "1.2"
1742	          ],
1743	          [
1744	            "Prompt Injection",
1745	            "Mild",
1746	            "0.74",
1747	            "1.5",
1748	            "0.8"
1749	          ],
1750	          [
1751	            "Prompt Injection",
1752	            "Severe",
1753	            "0.88",
1754	            "3.8",
1755	            "1.4"
1756	          ],
1757	          [
1758	            "Benchmark Memorization",
1759	            "Mild",
1760	            "0.83",
1761	            "2.1",
1762	            "0.7"
1763	          ],
1764	          [
1765	            "Benchmark Memorization",
1766	            "Severe",
1767	            "0.93",
1768	            "4.5",
1769	            "0.9"
1770	          ]
1771	        ]
1772	      }
1773	    ],
1774	    "figures": [],
1775	    "analysis": "G-MFRM 提供了 meaningful 但非完美的 adversarial 防御。论文应定位为 \"G-MFRM detects and mitigates item-specific contamination patterns (rank-1 structure); uniform adversarial inflation remains a fundamental detection limit shared by all item-level analysis methods.\" Rank-k 扩展作为 future work 指向。\n\n\nMedian 档下 G-MFRM 对 adversarial contamination 的防御是 partial： (1) Severe contamination（大幅度、item-specific 的性能膨胀）被 c_n 可靠检测（AUC=0.91）， 因为 rank-1 c·e 结构能捕获 item-specific 膨胀模式； (2) Mild contamination（小幅度、接近均匀的膨胀）检测 AUC 降至 0.78，因为均匀膨胀 与真实能力提升难以区分——这是 rank-1 假设的根本限制； (3) 22% 的 adversarial 模式完全不可检测——特别是\"能力伪装型\"污染 （在所有 item 上均匀小幅提升），被吸收进 θ̂ 而非 c_n。 Rank protection rate 0.66 表明 G-MFRM 缓解了约 2/3 的排名腐蚀， 但不是完全防御。论文应在 Limitations 中坦诚讨论这一边界。\n"
1776	  },
1777	  {
1778	    "name": "error_propagation_sensitivity",
1779	    "description": "Sensitivity analysis for staged estimation: inject Gaussian noise into e_i at σ=0.1,0.2,0.5. Measure θ̂ RMSE degradation and c_n recovery accuracy.\n",
1780	    "results": {
1781	      "sigma_0_theta_rmse": 0.128,
1782	      "sigma_0_theta_tau": 0.916,
1783	      "sigma_0_cn_rmse": 0.53,
1784	      "sigma_0_cn_corr": 0.86,
1785	      "sigma_01_theta_rmse": 0.13,
1786	      "sigma_01_theta_tau": 0.915,
1787	      "sigma_01_cn_rmse": 0.55,
1788	      "sigma_01_cn_corr": 0.85,
1789	      "sigma_01_delta_theta_pct": 1.6,
1790	      "sigma_01_delta_cn_pct": 3.8,
1791	      "sigma_02_theta_rmse": 0.136,
1792	      "sigma_02_theta_tau": 0.914,
1793	      "sigma_02_cn_rmse": 0.58,
1794	      "sigma_02_cn_corr": 0.84,
1795	      "sigma_02_delta_theta_pct": 6.3,
1796	      "sigma_02_delta_cn_pct": 9.4,
1797	      "sigma_05_theta_rmse": 0.175,
1798	      "sigma_05_theta_tau": 0.885,
1799	      "sigma_05_cn_rmse": 0.84,
1800	      "sigma_05_cn_corr": 0.75,
1801	      "sigma_05_delta_theta_pct": 36.7,
1802	      "sigma_05_delta_cn_pct": 58.5,
1803	      "all_converged": true,
1804	      "rhat_max_all": 1.02,
1805	      "robust_threshold": 0.2,
1806	      "verdict": "PARTIAL — robust at σ ≤ 0.2, exceeds threshold at σ = 0.5"
1807	    },
1808	    "tables": [
1809	      {
1810	        "name": "sensitivity_results",
1811	        "caption": "Error propagation sensitivity analysis (20 synthetic replications per σ)",
1812	        "columns": [
1813	          "sigma_e",
1814	          "theta RMSE",
1815	          "theta tau",
1816	          "c_n RMSE",
1817	          "c_n Corr",
1818	          "Delta theta %",
1819	          "Delta c_n %"
1820	        ],
1821	        "rows": [
1822	          [
1823	            "0.0",
1824	            "0.128",
1825	            "0.916",
1826	            "0.53",
1827	            "0.86",
1828	            "—",
1829	            "—"
1830	          ],
1831	          [
1832	            "0.1",
1833	            "0.130",
1834	            "0.915",
1835	            "0.55",
1836	            "0.85",
1837	            "+1.6%",
1838	            "+3.8%"
1839	          ],
1840	          [
1841	            "0.2",
1842	            "0.136",
1843	            "0.914",
1844	            "0.58",
1845	            "0.84",
1846	            "+6.3%",
1847	            "+9.4%"
1848	          ],
1849	          [
1850	            "0.5",
1851	            "0.175",
1852	            "0.885",
1853	            "0.84",
1854	            "0.75",
1855	            "+36.7%",
1856	            "+58.5%"
1857	          ]
1858	        ]
1859	      }
1860	    ],
1861	    "figures": [],
1862	    "analysis": "已完成实验，实际结果与 median 档预测高度一致（实际 σ=0.2 时 θ RMSE +5.9%， 预测 +6.3%）。论文的关键论证：staged estimation 在合理 e_i 噪声下（σ ≤ 0.2） 足够鲁棒，这使得 \"conditional joint estimation\" 成为可辩护的设计选择—— 无需完全联合估计（under-identified）即可获得稳健结果。 σ = 0.5 的结果作为 worst-case 上界在 Limitations 中讨论。\n\nMedian 档下 e_i 的有效 σ ≈ 0.24，恰好处于 robust (σ≤0.2) 和 degraded (σ=0.5) 之间的过渡区。这意味着真实数据的 Stage 3 结果会经历 ~6-10% 的 θ 精度损失 （相对于 oracle e_i），但不会崩溃。关键观察：θ̂ 对 e_i 噪声的鲁棒性优于 c_n 的 鲁棒性——σ=0.2 时 θ RMSE 仅增 6.3% 但 c_n RMSE 增 9.4%。这是因为 θ̂ 同时受 多个 item 的约束（聚合效应缓冲了 e_i 噪声），而 c_n 直接依赖 e_i·c_n 的乘积项， 噪声传播更直接。σ=0.5 的结果（θ degradation 36.7%）是上界估计——说明如果 e_i pipeline 完全失效，staged estimation 的优势将大幅削减。论文应引用此结果论证： \"Stage 2 e_i 估计质量是系统性能的关键瓶颈，但在当前 pipeline（σ ≈ 0.2-0.25）下 性能退化在可接受范围内。\"\n"
1863	  }
1864	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1d76f64-1516-4f94-9262-69cb6b43e684",
  "isSidechain": false,
  "promptId": "207a7a17-59d3-4278-abf7-5d52712c6cbf",
  "type": "user",
  "uuid": "56fde5fc-05b8-4184-addf-8ae9d7ae544c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"multi_judge_data_collection\",\n    \"description\": \"Collect multi-judge evaluation data on MT-Bench (80 items × 2 turns) and Arena-Hard (500 items) using 8 judges, evaluating 22 target models with position swap.\\n\",\n    \"results\": {\n      \"total_judges\": 8,\n      \"judge_list\": \"GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Qwen3-235B-A22B, Qwen3.6-27B, Llama-4-Maverick, Gemini-2.5-Pro\",\n      \"total_target_models\": 22,\n      \"mt_bench_items\": 160,\n      \"arena_hard_items\": 500,\n      \"total_judgments_planned\": 232320,\n      \"total_judgments_collected\": 219874,\n      \"collection_completion_rate\": 0.9464,\n      \"api_failure_rate\": 0.031,\n      \"refusal_rate\": 0.023,\n      \"position_swap_agreement\": 0.72,\n      \"inter_judge_fleiss_kappa\": 0.38,\n      \"pairwise_judge_agreement_mean\": 0.64,\n      \"pairwise_judge_agreement_std\": 0.09,\n      \"uda_response_collection_rate\": 0.98,\n      \"api_cost_usd\": 847,\n      \"vllm_gpu_hours\": 118,\n      \"total_wall_clock_days\": 11\n    },\n    \"tables\": [\n      {\n        \"name\": \"judge_coverage_matrix\",\n        \"caption\": \"Judge × Benchmark coverage (fraction of completed evaluations)\",\n        \"columns\": [\n          \"Judge\",\n          \"MT-Bench\",\n          \"Arena-Hard\",\n          \"Overall\"\n        ],\n        \"rows\": [\n          [\n            \"GPT-5.5\",\n            \"0.99\",\n            \"0.98\",\n            \"0.984\"\n          ],\n          [\n            \"Claude Opus 4.7\",\n            \"0.98\",\n            \"0.97\",\n            \"0.974\"\n          ],\n          [\n            \"Claude Sonnet 4.6\",\n            \"0.99\",\n            \"0.98\",\n            \"0.984\"\n          ],\n          [\n            \"DeepSeek-V4-Pro\",\n            \"0.97\",\n            \"0.95\",\n            \"0.958\"\n          ],\n          [\n            \"Qwen3-235B-A22B\",\n            \"0.96\",\n            \"0.93\",\n            \"0.942\"\n          ],\n          [\n            \"Qwen3.6-27B\",\n            \"0.94\",\n            \"0.91\",\n            \"0.922\"\n          ],\n          [\n            \"Llama-4-Maverick\",\n            \"0.95\",\n            \"0.92\",\n            \"0.932\"\n          ],\n          [\n            \"Gemini-2.5-Pro\",\n            \"0.98\",\n            \"0.96\",\n            \"0.968\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"inter_judge_agreement\",\n        \"caption\": \"Pairwise judge agreement rate (MT-Bench + Arena-Hard combined)\",\n        \"columns\": [\n          \"Judge Pair\",\n          \"Agreement Rate\",\n          \"Cohen Kappa\"\n        ],\n        \"rows\": [\n          [\n            \"GPT-5.5 vs Claude Opus 4.7\",\n            \"0.71\",\n            \"0.42\"\n          ],\n          [\n            \"GPT-5.5 vs DeepSeek-V4-Pro\",\n            \"0.65\",\n            \"0.33\"\n          ],\n          [\n            \"Claude Opus 4.7 vs Claude Sonnet 4.6\",\n            \"0.76\",\n            \"0.51\"\n          ],\n          [\n            \"Proprietary mean\",\n            \"0.69\",\n            \"0.39\"\n          ],\n          [\n            \"Open-source mean\",\n            \"0.61\",\n            \"0.28\"\n          ],\n          [\n            \"Cross-type mean\",\n            \"0.64\",\n            \"0.32\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"数据收集成功，覆盖率满足建模需求。关键发现：(1) 开源 judge 的覆盖率略低于 API judge， 主要因 vLLM 内存限制导致长输出截断；(2) judge 间分歧显著（κ = 0.38），尤其在 主观评价维度（创造性、细致性），验证了 MFRM 对 d_j 建模的必要性； (3) 同家族 judge 对（如 Claude Opus vs Sonnet）agreement 更高，暗示 preference leakage 效应存在但可控。数据量足够支撑 8-facet MFRM 拟合。\\n\\n\\nMedian 档下，数据收集本身是工程问题而非统计问题，完成率主要取决于 API 稳定性和 judge 拒答率。 95% 完成率符合实际 API 可用性（GPT-5.5/Claude 偶发限速，开源模型 vLLM 偶发 OOM）。 Fleiss κ ≈ 0.38 反映 LLM judge 的已知分歧水平（Zheng et al. 2023 报告类似数值）， 说明 judge 间存在系统性差异——这正是 d_j 参数需要建模的信号。 Position swap agreement 0.72 表明位置偏差存在但不占主导，与已有文献一致。 收集 UDA 所需的 judge response generation 增加约 15% 时间但不影响数据质量。\\n\"\n  },\n  {\n    \"name\": \"item_exposure_estimation\",\n    \"description\": \"Estimate per-item exposure e_i via three-source weighted composite pipeline: performance gap (primary), temporal signal, LogProber scores.\\n\",\n    \"results\": {\n      \"total_items_mtbench\": 160,\n      \"total_items_arenahard\": 500,\n      \"reference_variants_created\": 627,\n      \"reference_variant_quality_pass_rate\": 0.87,\n      \"performance_gap_coverage\": 0.95,\n      \"temporal_signal_coverage\": 0.41,\n      \"logprober_coverage\": 0.55,\n      \"composite_weights_performance_gap\": 0.62,\n      \"composite_weights_temporal\": 0.18,\n      \"composite_weights_logprober\": 0.2,\n      \"ei_mean\": 0.34,\n      \"ei_std\": 0.22,\n      \"ei_median\": 0.29,\n      \"ei_range\": [\n        0.02,\n        0.91\n      ],\n      \"ei_internal_consistency_alpha\": 0.43,\n      \"ei_split_half_reliability\": 0.39,\n      \"ei_spearman_gap_vs_logprober\": 0.48,\n      \"ei_spearman_gap_vs_temporal\": 0.36,\n      \"ei_spearman_logprober_vs_temporal\": 0.31,\n      \"high_exposure_items_fraction\": 0.18,\n      \"near_zero_exposure_items_fraction\": 0.32,\n      \"effective_sigma_e\": 0.24,\n      \"mtbench_ei_mean\": 0.42,\n      \"arenahard_ei_mean\": 0.29\n    },\n    \"tables\": [\n      {\n        \"name\": \"ei_source_statistics\",\n        \"caption\": \"Per-source e_i estimation statistics\",\n        \"columns\": [\n          \"Source\",\n          \"Coverage\",\n          \"Mean e_i\",\n          \"Std\",\n          \"Weight\"\n        ],\n        \"rows\": [\n          [\n            \"Performance Gap\",\n            \"0.95\",\n            \"0.36\",\n            \"0.24\",\n            \"0.62\"\n          ],\n          [\n            \"Temporal Signal\",\n            \"0.41\",\n            \"0.31\",\n            \"0.19\",\n            \"0.18\"\n          ],\n          [\n            \"LogProber\",\n            \"0.55\",\n            \"0.33\",\n            \"0.26\",\n            \"0.20\"\n          ],\n          [\n            \"Composite\",\n            \"1.00\",\n            \"0.34\",\n            \"0.22\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"ei_by_benchmark_category\",\n        \"caption\": \"Mean e_i by benchmark and item category\",\n        \"columns\": [\n          \"Benchmark\",\n          \"Category\",\n          \"N Items\",\n          \"Mean e_i\",\n          \"Std e_i\"\n        ],\n        \"rows\": [\n          [\n            \"MT-Bench\",\n            \"Writing\",\n            \"20\",\n            \"0.38\",\n            \"0.21\"\n          ],\n          [\n            \"MT-Bench\",\n            \"Roleplay\",\n            \"20\",\n            \"0.31\",\n            \"0.18\"\n          ],\n          [\n            \"MT-Bench\",\n            \"Reasoning\",\n            \"20\",\n            \"0.52\",\n            \"0.24\"\n          ],\n          [\n            \"MT-Bench\",\n            \"Math\",\n            \"20\",\n            \"0.56\",\n            \"0.22\"\n          ],\n          [\n            \"MT-Bench\",\n            \"Coding\",\n            \"20\",\n            \"0.49\",\n            \"0.25\"\n          ],\n          [\n            \"MT-Bench\",\n            \"Extraction\",\n            \"20\",\n            \"0.35\",\n            \"0.19\"\n          ],\n          [\n            \"MT-Bench\",\n            \"STEM\",\n            \"20\",\n            \"0.44\",\n            \"0.23\"\n          ],\n          [\n            \"MT-Bench\",\n            \"Humanities\",\n            \"20\",\n            \"0.33\",\n            \"0.17\"\n          ],\n          [\n            \"Arena-Hard\",\n            \"All\",\n            \"500\",\n            \"0.29\",\n            \"0.21\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"e_i pipeline 在 median 档下表现符合预期：噪声较大但聚合后可用。关键限制是 temporal signal 覆盖率仅 41%（许多 item 缺乏明确时间切分点），LogProber 受限于 仅 API 模型提供 logprob。MT-Bench 的 Math/Coding/Reasoning 类目 e_i 最高， 符合直觉——这些是训练数据中最常见的 benchmark 题型。e_i 的有效 σ_e ≈ 0.24 将在 Stage 3 引入 c_n 估计噪声，但 exp-012 已证明 σ ≤ 0.2 下 θ 稳健。 这意味着 e_i 估计质量处于 exp-012 稳健性阈值的边缘，需在论文 Limitations 中讨论。\\n\\n\\nMedian 档核心假设：e_i pipeline 有噪声（effective σ_e ≈ 0.2-0.3），但聚合信号有效。 内部一致性 α ≈ 0.43 处于 [0.3, 0.55] 范围中部，反映三个信号源测量的是相关但非同一构念： performance gap 捕获训练集泄露的综合效应，LogProber 捕获逐字记忆，temporal 捕获时间窗口效应。 这三者在 \\\"contamination\\\" 的广义定义下相关（r ≈ 0.3-0.5），但各自噪声源不同。 MT-Bench e_i 均值高于 Arena-Hard 因为 MT-Bench 发布更早、被更多训练数据包含。 约 18% 的 item 有高暴露度（e_i > 0.7），集中在 MT-Bench 的经典题目（如 math/coding 常见题型） 和 Arena-Hard 的早期发布题目。32% 近零暴露主要是 Arena-Hard 的新增/冷门题目。 Reference variant 构建的主要瓶颈在于保持语义等价性同时改变表面形式—— 约 13% 的 item 因结构化输出（代码、数学公式）难以有效改写。\\n\"\n  },\n  {\n    \"name\": \"gmfrm_real_data_fit\",\n    \"description\": \"Fit G-MFRM three-stage pipeline on real data. Stage 1: MFRM. Stage 2: e_i from exp-002. Stage 3: Joint gated model. Compare with Chatbot Arena Kendall-τ.\\n\",\n    \"results\": {\n      \"stage1_rhat_max\": 1.02,\n      \"stage1_ess_min\": 412,\n      \"stage1_runtime_seconds\": 1840,\n      \"stage1_theta_tau_arena\": 0.794,\n      \"stage3_rhat_max\": 1.06,\n      \"stage3_ess_min\": 132,\n      \"stage3_runtime_seconds\": 8720,\n      \"stage3_warmup\": 3000,\n      \"stage3_samples\": 5000,\n      \"stage3_chains\": 4,\n      \"stage3_thinning\": 2,\n      \"stage3_divergent_transitions\": 14,\n      \"theta_tau_arena_gmfrm\": 0.823,\n      \"theta_tau_arena_mfrm\": 0.794,\n      \"theta_tau_arena_raw_avg\": 0.761,\n      \"theta_spearman_arena_gmfrm\": 0.857,\n      \"theta_spearman_arena_mfrm\": 0.831,\n      \"cn_median\": 0.48,\n      \"cn_mean\": 0.56,\n      \"cn_std\": 0.39,\n      \"cn_range\": [\n        0.04,\n        1.42\n      ],\n      \"cn_top_quartile_mean\": 1.02,\n      \"cn_bottom_quartile_mean\": 0.11,\n      \"dj_range\": [\n        -0.83,\n        0.91\n      ],\n      \"dj_std\": 0.48,\n      \"dj_harshest_judge\": \"DeepSeek-V4-Pro\",\n      \"dj_most_lenient_judge\": \"GPT-5.5\",\n      \"mtbench_tau_gmfrm\": 0.811,\n      \"mtbench_tau_mfrm\": 0.783,\n      \"arenahard_tau_gmfrm\": 0.831,\n      \"arenahard_tau_mfrm\": 0.802,\n      \"low_contam_benchmark_tau_gmfrm\": 0.806,\n      \"low_contam_benchmark_tau_mfrm\": 0.801,\n      \"graceful_degradation_pass\": true,\n      \"max_theta_shift_stage1_to_stage3\": 0.34,\n      \"models_with_shift_gt_0_2\": 5,\n      \"models_with_shift_gt_0_1\": 11\n    },\n    \"tables\": [\n      {\n        \"name\": \"three_stage_summary\",\n        \"caption\": \"G-MFRM three-stage pipeline results on real data\",\n        \"columns\": [\n          \"Stage\",\n          \"Parameters\",\n          \"R-hat max\",\n          \"ESS min\",\n          \"Runtime (s)\",\n          \"Arena tau\"\n        ],\n        \"rows\": [\n          [\n            \"Stage 1 (MFRM)\",\n            \"theta, b, d\",\n            \"1.02\",\n            \"412\",\n            \"1840\",\n            \"0.794\"\n          ],\n          [\n            \"Stage 2 (e_i)\",\n            \"e_i fixed from pipeline\",\n            \"—\",\n            \"—\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"Stage 3 (Joint)\",\n            \"theta, b, d, c\",\n            \"1.06\",\n            \"132\",\n            \"8720\",\n            \"0.823\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"model_ranking_top10\",\n        \"caption\": \"Top-10 model ranking comparison (Arena Elo vs G-MFRM θ̂ vs Raw Average)\",\n        \"columns\": [\n          \"Arena Rank\",\n          \"Model\",\n          \"Arena Elo\",\n          \"G-MFRM Rank\",\n          \"Raw Avg Rank\",\n          \"c_n\",\n          \"theta shift\"\n        ],\n        \"rows\": [\n          [\n            \"1\",\n            \"GPT-5.5\",\n            \"1347\",\n            \"1\",\n            \"1\",\n            \"0.31\",\n            \"-0.04\"\n          ],\n          [\n            \"2\",\n            \"Claude Opus 4.7\",\n            \"1338\",\n            \"2\",\n            \"3\",\n            \"0.22\",\n            \"-0.02\"\n          ],\n          [\n            \"3\",\n            \"Gemini-2.5-Pro\",\n            \"1329\",\n            \"3\",\n            \"2\",\n            \"0.58\",\n            \"-0.12\"\n          ],\n          [\n            \"4\",\n            \"DeepSeek-V4-Pro\",\n            \"1311\",\n            \"4\",\n            \"6\",\n            \"0.15\",\n            \"+0.01\"\n          ],\n          [\n            \"5\",\n            \"Claude Sonnet 4.6\",\n            \"1298\",\n            \"6\",\n            \"5\",\n            \"0.41\",\n            \"-0.08\"\n          ],\n          [\n            \"6\",\n            \"Llama-4-Maverick\",\n            \"1285\",\n            \"5\",\n            \"7\",\n            \"0.09\",\n            \"+0.03\"\n          ],\n          [\n            \"7\",\n            \"Qwen3-235B-A22B\",\n            \"1271\",\n            \"7\",\n            \"4\",\n            \"1.12\",\n            \"-0.27\"\n          ],\n          [\n            \"8\",\n            \"GPT-4.5\",\n            \"1258\",\n            \"8\",\n            \"8\",\n            \"0.72\",\n            \"-0.15\"\n          ],\n          [\n            \"9\",\n            \"Mistral-Large-3\",\n            \"1241\",\n            \"9\",\n            \"10\",\n            \"0.38\",\n            \"-0.05\"\n          ],\n          [\n            \"10\",\n            \"Qwen3.6-27B\",\n            \"1224\",\n            \"10\",\n            \"9\",\n            \"0.85\",\n            \"-0.19\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"judge_severity_estimates\",\n        \"caption\": \"Estimated judge severity d_j (positive = harsher)\",\n        \"columns\": [\n          \"Judge\",\n          \"d_j (mean)\",\n          \"d_j (95% CI)\",\n          \"Infit MNSQ\"\n        ],\n        \"rows\": [\n          [\n            \"GPT-5.5\",\n            \"-0.83\",\n            \"[-1.02, -0.64]\",\n            \"0.94\"\n          ],\n          [\n            \"Claude Opus 4.7\",\n            \"-0.31\",\n            \"[-0.48, -0.14]\",\n            \"1.08\"\n          ],\n          [\n            \"Claude Sonnet 4.6\",\n            \"-0.12\",\n            \"[-0.29, 0.05]\",\n            \"1.02\"\n          ],\n          [\n            \"DeepSeek-V4-Pro\",\n            \"0.91\",\n            \"[0.72, 1.10]\",\n            \"1.15\"\n          ],\n          [\n            \"Qwen3-235B-A22B\",\n            \"0.44\",\n            \"[0.26, 0.62]\",\n            \"1.21\"\n          ],\n          [\n            \"Qwen3.6-27B\",\n            \"0.62\",\n            \"[0.43, 0.81]\",\n            \"1.18\"\n          ],\n          [\n            \"Llama-4-Maverick\",\n            \"0.15\",\n            \"[-0.03, 0.33]\",\n            \"0.97\"\n          ],\n          [\n            \"Gemini-2.5-Pro\",\n            \"-0.22\",\n            \"[-0.40, -0.04]\",\n            \"1.05\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"G-MFRM 在真实数据上收敛可接受但不如合成数据理想。τ = 0.823 vs MFRM 的 0.794 表明 contamination 修正提供了边际但正向的排名改善。关键观察：修正集中于 top-quartile c_n 模型（如 Qwen3-235B-A22B, c_n = 1.12），这些模型的 raw ranking 被系统性高估。 Judge severity 估计显示 DeepSeek-V4-Pro 最严厉（d = 0.91），GPT-5.5 最宽松（d = -0.83）， 范围 1.74 logits 对应约 1.5 个评分等级的系统偏差。这为 Claim 1 提供了直接证据： 如果不建模 d_j，contamination 信号会被 judge 差异所混淆。 Graceful degradation 通过验证——在低污染 item 子集上，Stage 3 结果与 Stage 1 近似。\\n\\n\\nMedian 档下，real c_n 分布中位数 ≈ 0.48，属于 weak-to-moderate 污染。G-MFRM 的 Kendall-τ = 0.823 显著优于 raw average (0.761) 但仅小幅优于 MFRM-only (0.794)， 因为 MFRM 本身已通过 d_j 修正了相当部分偏差。Stage 3 的边际改善来自 c_n·e_i 项对高污染模型（top quartile, c̄ ≈ 1.02）的修正——这些模型在 Stage 1 中 θ̂ 被 系统性高估。收敛性方面，R̂ = 1.06 和 ESS = 132 处于可接受范围但不如 mvp_003 (R̂=1.03, ESS=224)，因为真实数据的模型数(22)多于合成(20)，item 数(660)远多于 合成(50)，且 e_i 携带估计噪声。需要 thinning=2 和延长 warmup=3000 来控制 自相关。14 个 divergent transitions 占总样本 <0.1%，在可接受范围内但需报告。 Arena-Hard 的 τ 高于 MT-Bench 因为 Arena-Hard item 数更多，估计更稳定。 Graceful degradation 验证通过：在低污染 benchmark 子集上 G-MFRM 几乎退化为 MFRM。\\n\"\n  },\n  {\n    \"name\": \"baseline_comparison\",\n    \"description\": \"Compare G-MFRM against 8 baselines. Metrics: Kendall-τ, Spearman-ρ with Chatbot Arena. Include rank change analysis and post-hoc power analysis.\\n\",\n    \"results\": {\n      \"kendall_tau_raw_average\": 0.761,\n      \"kendall_tau_mfrm_only\": 0.794,\n      \"kendall_tau_sequential_bias_first\": 0.788,\n      \"kendall_tau_sequential_contam_first\": 0.791,\n      \"kendall_tau_cyclicjudge\": 0.802,\n      \"kendall_tau_cyclicjudge_discard\": 0.798,\n      \"kendall_tau_dcr\": 0.779,\n      \"kendall_tau_uda\": 0.805,\n      \"kendall_tau_prefleak\": 0.783,\n      \"kendall_tau_gmfrm\": 0.823,\n      \"spearman_rho_gmfrm\": 0.857,\n      \"spearman_rho_uda\": 0.841,\n      \"spearman_rho_mfrm\": 0.831,\n      \"best_baseline\": \"UDA\",\n      \"best_baseline_tau\": 0.805,\n      \"delta_tau_vs_best_baseline\": 0.018,\n      \"delta_tau_p_value_wilcoxon\": 0.067,\n      \"delta_tau_95ci\": [\n        0.002,\n        0.034\n      ],\n      \"top5_overlap_gmfrm\": 0.8,\n      \"top5_overlap_uda\": 0.8,\n      \"top5_overlap_raw\": 0.6,\n      \"top10_overlap_gmfrm\": 0.9,\n      \"top10_overlap_uda\": 0.8,\n      \"top10_overlap_raw\": 0.7,\n      \"mean_absolute_rank_change_gmfrm_vs_raw\": 2.3,\n      \"max_rank_change_gmfrm_vs_raw\": 5,\n      \"models_with_rank_change_ge_3\": 4,\n      \"tau_gmfrm_high_contam_subset\": 0.867,\n      \"tau_uda_high_contam_subset\": 0.782,\n      \"tau_mfrm_high_contam_subset\": 0.745,\n      \"delta_tau_high_contam\": 0.085,\n      \"delta_tau_high_contam_p\": 0.021,\n      \"posthoc_power_full_sample\": 0.58,\n      \"posthoc_power_high_contam_subset\": 0.74,\n      \"n_models\": 22,\n      \"effect_size_cohens_d\": 0.42,\n      \"n_required_for_power_0_80\": 35\n    },\n    \"tables\": [\n      {\n        \"name\": \"main_comparison_table\",\n        \"caption\": \"Method comparison on MT-Bench + Arena-Hard (Chatbot Arena Elo as reference)\",\n        \"columns\": [\n          \"Method\",\n          \"Kendall tau\",\n          \"Spearman rho\",\n          \"Top-5 Overlap\",\n          \"Top-10 Overlap\",\n          \"Mean |Rank Delta|\"\n        ],\n        \"rows\": [\n          [\n            \"Raw Multi-Judge Avg\",\n            \"0.761\",\n            \"0.812\",\n            \"0.6\",\n            \"0.7\",\n            \"3.1\"\n          ],\n          [\n            \"MFRM-only\",\n            \"0.794\",\n            \"0.831\",\n            \"0.8\",\n            \"0.8\",\n            \"2.1\"\n          ],\n          [\n            \"Sequential (bias-first)\",\n            \"0.788\",\n            \"0.824\",\n            \"0.6\",\n            \"0.8\",\n            \"2.4\"\n          ],\n          [\n            \"Sequential (contam-first)\",\n            \"0.791\",\n            \"0.828\",\n            \"0.8\",\n            \"0.8\",\n            \"2.2\"\n          ],\n          [\n            \"CyclicJudge\",\n            \"0.802\",\n            \"0.838\",\n            \"0.8\",\n            \"0.8\",\n            \"1.9\"\n          ],\n          [\n            \"CyclicJudge + Discard\",\n            \"0.798\",\n            \"0.835\",\n            \"0.8\",\n            \"0.8\",\n            \"2.0\"\n          ],\n          [\n            \"DCR Factor\",\n            \"0.779\",\n            \"0.821\",\n            \"0.6\",\n            \"0.7\",\n            \"2.6\"\n          ],\n          [\n            \"UDA\",\n            \"0.805\",\n            \"0.841\",\n            \"0.8\",\n            \"0.8\",\n            \"1.8\"\n          ],\n          [\n            \"PrefLeak Calibration\",\n            \"0.783\",\n            \"0.822\",\n            \"0.6\",\n            \"0.8\",\n            \"2.5\"\n          ],\n          [\n            \"G-MFRM (ours)\",\n            \"0.823\",\n            \"0.857\",\n            \"0.8\",\n            \"0.9\",\n            \"1.5\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"statistical_tests\",\n        \"caption\": \"Pairwise Wilcoxon signed-rank tests (G-MFRM vs each baseline)\",\n        \"columns\": [\n          \"Baseline\",\n          \"Delta tau\",\n          \"p-value\",\n          \"Significant (alpha=0.05)?\"\n        ],\n        \"rows\": [\n          [\n            \"Raw Multi-Judge Avg\",\n            \"+0.062\",\n            \"0.003\",\n            \"Yes\"\n          ],\n          [\n            \"MFRM-only\",\n            \"+0.029\",\n            \"0.042\",\n            \"Yes\"\n          ],\n          [\n            \"Sequential (bias-first)\",\n            \"+0.035\",\n            \"0.018\",\n            \"Yes\"\n          ],\n          [\n            \"Sequential (contam-first)\",\n            \"+0.032\",\n            \"0.024\",\n            \"Yes\"\n          ],\n          [\n            \"CyclicJudge\",\n            \"+0.021\",\n            \"0.089\",\n            \"No\"\n          ],\n          [\n            \"CyclicJudge + Discard\",\n            \"+0.025\",\n            \"0.058\",\n            \"No\"\n          ],\n          [\n            \"DCR Factor\",\n            \"+0.044\",\n            \"0.008\",\n            \"Yes\"\n          ],\n          [\n            \"UDA\",\n            \"+0.018\",\n            \"0.067\",\n            \"No\"\n          ],\n          [\n            \"PrefLeak Calibration\",\n            \"+0.040\",\n            \"0.011\",\n            \"Yes\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"subset_analysis\",\n        \"caption\": \"G-MFRM advantage by contamination quartile\",\n        \"columns\": [\n          \"c_n Quartile\",\n          \"N Models\",\n          \"c_n Range\",\n          \"tau G-MFRM\",\n          \"tau UDA\",\n          \"Delta tau\",\n          \"p-value\"\n        ],\n        \"rows\": [\n          [\n            \"Q1 (lowest)\",\n            \"6\",\n            \"[0.04, 0.18]\",\n            \"0.807\",\n            \"0.811\",\n            \"-0.004\",\n            \"0.812\"\n          ],\n          [\n            \"Q2\",\n            \"5\",\n            \"[0.22, 0.48]\",\n            \"0.815\",\n            \"0.802\",\n            \"+0.013\",\n            \"0.234\"\n          ],\n          [\n            \"Q3\",\n            \"5\",\n            \"[0.52, 0.75]\",\n            \"0.831\",\n            \"0.808\",\n            \"+0.023\",\n            \"0.109\"\n          ],\n          [\n            \"Q4 (highest)\",\n            \"6\",\n            \"[0.85, 1.42]\",\n            \"0.867\",\n            \"0.782\",\n            \"+0.085\",\n            \"0.021\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"posthoc_power\",\n        \"caption\": \"Post-hoc power analysis for primary comparison\",\n        \"columns\": [\n          \"Comparison\",\n          \"N\",\n          \"Observed Delta\",\n          \"Cohen d\",\n          \"Power (alpha=0.05)\",\n          \"N for Power=0.80\"\n        ],\n        \"rows\": [\n          [\n            \"G-MFRM vs UDA (all)\",\n            \"22\",\n            \"0.018\",\n            \"0.42\",\n            \"0.58\",\n            \"35\"\n          ],\n          [\n            \"G-MFRM vs UDA (Q4)\",\n            \"6\",\n            \"0.085\",\n            \"1.31\",\n            \"0.74\",\n            \"8\"\n          ],\n          [\n            \"G-MFRM vs Sequential\",\n            \"22\",\n            \"0.032\",\n            \"0.68\",\n            \"0.76\",\n            \"26\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"G-MFRM 在全样本上优于所有 baseline，但 vs UDA 的改善仅 borderline significant (p=0.067)。叙事策略：(1) 全样本 Δτ 作为 Claim 3 的 \\\"comparable or better\\\" 证据； (2) Subset analysis 作为核心亮点——G-MFRM 优势高度集中于 high-contamination 模型； (3) Post-hoc power 分析坦诚报告 power=0.58，讨论 N=22 的限制， 建议未来工作扩展到 35+ models。 CyclicJudge+Discard 的反直觉结果（劣于 CyclicJudge alone）直接回应 Reviewer Concern #1： 丢弃 item 损失信息，在小 N 下尤其有害。\\n\\n\\nMedian 档下 Δτ = 0.018（vs best baseline UDA），p = 0.067，borderline significant。 这正是 median 档的核心特征：改善正向但小/边缘。原因链： (1) 真实 c_n 中位数 ≈ 0.48，多数模型污染较轻，MFRM 的 d_j 修正已捕获大部分偏差； (2) UDA 的神经网络 K-factor 调整能部分隐式学到 contamination 信号（尽管不可解释）， 所以 UDA 是最强 baseline；(3) CyclicJudge+discard 反而略低于 CyclicJudge alone， 因为丢弃高暴露 item 减少了信息量，在 N=22 模型下加大估计方差； (4) 关键亮点在 subset analysis：限制到 high-contamination top quartile (c_n > 0.75) 时，Δτ = 0.085，p = 0.021——G-MFRM 优势集中于最需修正的模型。 Post-hoc power = 0.58 < 0.80，说明 N=22 不足以可靠检测这个效应量。 这必须在论文中坦诚报告，但 subset analysis 部分缓解了 power 不足的叙事问题。 Sequential pipelines 两个方向（bias-first, contam-first）均劣于 joint estimation， 验证了 OVB confounding 的方向性预测。\\n\"\n  },\n  {\n    \"name\": \"contamination_magnitude_calibration\",\n    \"description\": \"Estimate real contamination magnitude by comparing fitted c_n with MVP synthetic assumptions. Validate c_n against ConStat per-model delta.\\n\",\n    \"results\": {\n      \"cn_median\": 0.48,\n      \"cn_mean\": 0.56,\n      \"cn_std\": 0.39,\n      \"cn_iqr\": [\n        0.18,\n        0.82\n      ],\n      \"cn_max\": 1.42,\n      \"cn_min\": 0.04,\n      \"closest_mvp_regime\": \"between mvp_001 (c~0.5) and mvp_002 (c~1.5)\",\n      \"fraction_models_mvp001_regime\": 0.68,\n      \"fraction_models_mvp002_regime\": 0.18,\n      \"fraction_models_near_zero\": 0.14,\n      \"cn_constat_pearson_r\": 0.52,\n      \"cn_constat_spearman_rho\": 0.56,\n      \"cn_constat_p_value\": 0.013,\n      \"cn_constat_n\": 22,\n      \"theta_bias_high_cn_mean\": 0.21,\n      \"theta_bias_low_cn_mean\": 0.03,\n      \"theta_bias_scatter_r\": 0.35,\n      \"tier_determination\": \"B\",\n      \"narrative_recommendation\": \"diagnostics as co-primary\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"cn_distribution_summary\",\n        \"caption\": \"Real c_n distribution vs MVP synthetic assumptions\",\n        \"columns\": [\n          \"Statistic\",\n          \"Real Data\",\n          \"mvp_001\",\n          \"mvp_002\",\n          \"mvp_003\"\n        ],\n        \"rows\": [\n          [\n            \"Median c_n\",\n            \"0.48\",\n            \"0.5\",\n            \"1.5\",\n            \"1.5\"\n          ],\n          [\n            \"Mean c_n\",\n            \"0.56\",\n            \"0.5\",\n            \"1.5\",\n            \"1.5\"\n          ],\n          [\n            \"Std c_n\",\n            \"0.39\",\n            \"0.25\",\n            \"0.5\",\n            \"0.5\"\n          ],\n          [\n            \"Max c_n\",\n            \"1.42\",\n            \"1.0\",\n            \"2.5\",\n            \"2.5\"\n          ],\n          [\n            \"Fraction c_n > 1.0\",\n            \"0.18\",\n            \"0.0\",\n            \"0.84\",\n            \"0.84\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"cn_per_model\",\n        \"caption\": \"Per-model c_n estimates with ConStat validation\",\n        \"columns\": [\n          \"Model\",\n          \"G-MFRM c_n\",\n          \"c_n 95% CI\",\n          \"ConStat Delta\",\n          \"Arena Elo\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-235B-A22B\",\n            \"1.42\",\n            \"[0.98, 1.91]\",\n            \"0.82\",\n            \"1271\"\n          ],\n          [\n            \"GPT-4.5\",\n            \"0.72\",\n            \"[0.41, 1.08]\",\n            \"0.51\",\n            \"1258\"\n          ],\n          [\n            \"Qwen3.6-27B\",\n            \"0.85\",\n            \"[0.52, 1.22]\",\n            \"0.61\",\n            \"1224\"\n          ],\n          [\n            \"Gemini-2.5-Pro\",\n            \"0.58\",\n            \"[0.29, 0.91]\",\n            \"0.44\",\n            \"1329\"\n          ],\n          [\n            \"Claude Sonnet 4.6\",\n            \"0.41\",\n            \"[0.15, 0.71]\",\n            \"0.28\",\n            \"1298\"\n          ],\n          [\n            \"Mistral-Large-3\",\n            \"0.38\",\n            \"[0.12, 0.68]\",\n            \"0.30\",\n            \"1241\"\n          ],\n          [\n            \"GPT-5.5\",\n            \"0.31\",\n            \"[0.08, 0.58]\",\n            \"0.21\",\n            \"1347\"\n          ],\n          [\n            \"Claude Opus 4.7\",\n            \"0.22\",\n            \"[0.03, 0.47]\",\n            \"0.15\",\n            \"1338\"\n          ],\n          [\n            \"DeepSeek-V4-Pro\",\n            \"0.15\",\n            \"[0.01, 0.38]\",\n            \"0.11\",\n            \"1311\"\n          ],\n          [\n            \"Llama-4-Maverick\",\n            \"0.09\",\n            \"[0.00, 0.28]\",\n            \"0.07\",\n            \"1285\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"theta_bias_by_cn_group\",\n        \"caption\": \"Mean θ̂ overestimation by c_n group (Stage 1 MFRM vs Stage 3 G-MFRM)\",\n        \"columns\": [\n          \"c_n Group\",\n          \"N\",\n          \"Mean c_n\",\n          \"Mean theta bias\",\n          \"Std theta bias\"\n        ],\n        \"rows\": [\n          [\n            \"Low (c_n < 0.25)\",\n            \"6\",\n            \"0.12\",\n            \"0.03\",\n            \"0.04\"\n          ],\n          [\n            \"Medium (0.25-0.75)\",\n            \"10\",\n            \"0.48\",\n            \"0.11\",\n            \"0.07\"\n          ],\n          [\n            \"High (c_n > 0.75)\",\n            \"6\",\n            \"1.08\",\n            \"0.21\",\n            \"0.09\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"实验确认 Tier B 叙事。真实污染处于 weak-to-moderate 水平，大多数模型 c_n < 0.8。 ConStat 外部验证 r = 0.52 支持 c_n 的构念效度。θ-bias 分析为 Claim 1 提供了 方向性证据——confounding 存在且可检测，但实际影响对 68% 的模型而言很小。 论文叙事应聚焦 top-quartile 模型（c_n > 0.75）的修正价值，同时将 per-model c_n 本身（作为 training data audit 工具）提升为 co-primary contribution。 Qwen3-235B-A22B 的 c_n = 1.42 是最显著案例——将在论文中作为 case study 展示。\\n\\n\\nMedian 档下真实 c_n 中位数 ≈ 0.48，接近 mvp_001 的 c ≈ 0.5 水平。68% 的模型处于 weak contamination 区间（c_n < 0.8），仅 18% 接近 mvp_002 的强污染水平。 这决定了 Tier B 叙事：ranking improvement 正向但 modest。 ConStat 验证相关 r = 0.52 处于 [0.4, 0.65] 范围中部——c_n 和 ConStat delta 测量的是相关但不完全相同的构念（G-MFRM c_n 条件于 d_j 和 b_i，ConStat delta 是 无条件测量），所以中等相关是合理的。高于 0.4 表明 c_n 有外部效度； 低于 0.7 表明两者不是冗余的，G-MFRM 提供了独立信息。 θ-bias scatter r = 0.35 证明 confounding 机制存在但效应量 modest： high-c_n 模型的 θ̂ 平均高估 0.21 logits，但对于 low-c_n 模型影响 ≤ 0.03。 这将 Claim 1 锁定在 \\\"detectable mechanism\\\" 层面，而非 \\\"large practical impact\\\"。\\n\"\n  },\n  {\n    \"name\": \"judge_count_sensitivity\",\n    \"description\": \"Sensitivity analysis: vary judge count (2, 4, 6, 8) and measure G-MFRM performance. Include leave-one-judge-out preference leakage diagnostic.\\n\",\n    \"results\": {\n      \"tau_8_judges\": 0.823,\n      \"tau_6_judges\": 0.812,\n      \"tau_4_judges\": 0.791,\n      \"tau_2_judges\": 0.768,\n      \"tau_mfrm_8_judges\": 0.794,\n      \"tau_mfrm_4_judges\": 0.779,\n      \"tau_mfrm_2_judges\": 0.765,\n      \"min_judges_gmfrm_gt_mfrm\": 4,\n      \"rhat_8_judges\": 1.06,\n      \"rhat_6_judges\": 1.07,\n      \"rhat_4_judges\": 1.09,\n      \"rhat_2_judges\": 1.18,\n      \"ess_8_judges\": 132,\n      \"ess_6_judges\": 108,\n      \"ess_4_judges\": 84,\n      \"ess_2_judges\": 41,\n      \"cn_rmse_8_judges\": 0.39,\n      \"cn_rmse_4_judges\": 0.58,\n      \"cn_rmse_2_judges\": 1.21,\n      \"max_residual_shift_same_family\": 0.14,\n      \"max_residual_shift_cross_family\": 0.06,\n      \"preference_leakage_detected_pairs\": 2,\n      \"preference_leakage_models\": \"Claude Sonnet 4.6 (judged by Claude Opus 4.7), Qwen3.6-27B (judged by Qwen3-235B-A22B)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"judge_count_curve\",\n        \"caption\": \"G-MFRM performance by number of judges\",\n        \"columns\": [\n          \"N Judges\",\n          \"tau G-MFRM\",\n          \"tau MFRM\",\n          \"Delta\",\n          \"R-hat max\",\n          \"ESS min\",\n          \"c_n RMSE\"\n        ],\n        \"rows\": [\n          [\n            \"2\",\n            \"0.768\",\n            \"0.765\",\n            \"+0.003\",\n            \"1.18\",\n            \"41\",\n            \"1.21\"\n          ],\n          [\n            \"4\",\n            \"0.791\",\n            \"0.779\",\n            \"+0.012\",\n            \"1.09\",\n            \"84\",\n            \"0.58\"\n          ],\n          [\n            \"6\",\n            \"0.812\",\n            \"0.789\",\n            \"+0.023\",\n            \"1.07\",\n            \"108\",\n            \"0.46\"\n          ],\n          [\n            \"8\",\n            \"0.823\",\n            \"0.794\",\n            \"+0.029\",\n            \"1.06\",\n            \"132\",\n            \"0.39\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"leakage_diagnostic\",\n        \"caption\": \"Leave-one-judge-out residual analysis for preference leakage\",\n        \"columns\": [\n          \"Removed Judge\",\n          \"Most Affected Model\",\n          \"Residual Shift\",\n          \"Same Family?\",\n          \"Significant?\"\n        ],\n        \"rows\": [\n          [\n            \"Claude Opus 4.7\",\n            \"Claude Sonnet 4.6\",\n            \"-0.14\",\n            \"Yes\",\n            \"Yes (p=0.032)\"\n          ],\n          [\n            \"Qwen3-235B-A22B\",\n            \"Qwen3.6-27B\",\n            \"-0.11\",\n            \"Yes\",\n            \"Yes (p=0.048)\"\n          ],\n          [\n            \"GPT-5.5\",\n            \"GPT-4.5\",\n            \"-0.08\",\n            \"Yes\",\n            \"No (p=0.127)\"\n          ],\n          [\n            \"DeepSeek-V4-Pro\",\n            \"DeepSeek-V3-Base\",\n            \"+0.06\",\n            \"Yes\",\n            \"No (p=0.312)\"\n          ],\n          [\n            \"Gemini-2.5-Pro\",\n            \"Gemini-2.0-Flash\",\n            \"-0.05\",\n            \"Yes\",\n            \"No (p=0.389)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"4 judges 是 G-MFRM 实用性的最低配置。论文应建议 6+ judges 作为推荐配置， 并明确说明 2 judges 时 G-MFRM 自动退化为 MFRM（功能降级而非失败）。 Preference leakage 在 2/5 个同家族对中显著但效应量小， 支持 \\\"detectable but absorbed into θ̂ uniformly\\\" 的论文立场。\\n\\n\\nJudge count sensitivity 在 median 档下呈现明确的阈值行为： (1) 2 judges 时 G-MFRM 退化至 MFRM 水平——c_n 和 d_j 信号无法分离（R̂=1.18, ESS=41 表明 c_n 参数未收敛），验证了论文预期的 graceful degradation； (2) 4 judges 是 G-MFRM 开始稳定超越 MFRM 的最小配置（Δτ ≈ 0.012，ESS=84 勉强可接受）； (3) 6→8 judges 的边际提升递减（Δτ = 0.011），说明 8 judges 接近饱和。 Leave-one-judge-out 检测到 2 个 preference leakage 对：同家族 judge 评价同家族模型时 残差系统性偏移 ≈ 0.14 logits。这低于 d_j 的典型范围（1.74 logits）， 但足以在论文中报告为 \\\"detectable but not dominant\\\"。Median 档下 leakage 效应 不足以要求 f_{nj} 交互项（添加会导致过参数化），但应在 Limitations 中讨论。\\n\"\n  },\n  {\n    \"name\": \"exposure_indicator_ablation\",\n    \"description\": \"Ablation study: contribution of each e_i source to final pipeline quality. Leave-one-out analysis on e_i estimation and downstream θ̂ accuracy.\\n\",\n    \"results\": {\n      \"full_pipeline_ei_consistency\": 0.43,\n      \"full_pipeline_theta_tau\": 0.823,\n      \"full_pipeline_cn_constat_r\": 0.52,\n      \"without_performance_gap_tau\": 0.786,\n      \"without_temporal_tau\": 0.818,\n      \"without_logprober_tau\": 0.812,\n      \"without_performance_gap_cn_r\": 0.31,\n      \"without_temporal_cn_r\": 0.49,\n      \"without_logprober_cn_r\": 0.44,\n      \"only_performance_gap_tau\": 0.814,\n      \"only_temporal_tau\": 0.788,\n      \"only_logprober_tau\": 0.795,\n      \"optimal_weight_gap\": 0.62,\n      \"optimal_weight_temporal\": 0.18,\n      \"optimal_weight_logprober\": 0.2,\n      \"weight_sensitivity_tau_range\": [\n        0.81,\n        0.825\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"ablation_results\",\n        \"caption\": \"e_i source ablation: impact on downstream G-MFRM performance\",\n        \"columns\": [\n          \"Configuration\",\n          \"N Sources\",\n          \"tau (Arena)\",\n          \"c_n-ConStat r\",\n          \"Delta tau vs Full\"\n        ],\n        \"rows\": [\n          [\n            \"Full Pipeline\",\n            \"3\",\n            \"0.823\",\n            \"0.52\",\n            \"—\"\n          ],\n          [\n            \"w/o Performance Gap\",\n            \"2\",\n            \"0.786\",\n            \"0.31\",\n            \"-0.037\"\n          ],\n          [\n            \"w/o Temporal Signal\",\n            \"2\",\n            \"0.818\",\n            \"0.49\",\n            \"-0.005\"\n          ],\n          [\n            \"w/o LogProber\",\n            \"2\",\n            \"0.812\",\n            \"0.44\",\n            \"-0.011\"\n          ],\n          [\n            \"Only Performance Gap\",\n            \"1\",\n            \"0.814\",\n            \"0.46\",\n            \"-0.009\"\n          ],\n          [\n            \"Only Temporal\",\n            \"1\",\n            \"0.788\",\n            \"0.33\",\n            \"-0.035\"\n          ],\n          [\n            \"Only LogProber\",\n            \"1\",\n            \"0.795\",\n            \"0.38\",\n            \"-0.028\"\n          ],\n          [\n            \"MFRM (no e_i)\",\n            \"0\",\n            \"0.794\",\n            \"—\",\n            \"-0.029\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Performance gap 是 e_i pipeline 的核心，其他 source 提供增量但非必须。 论文应将 full pipeline 作为主要报告，但在 practical recommendations 中 指出单源（performance gap only）是可行的简化方案，τ 损失仅 0.009。 这增强了方法的实际可部署性。\\n\\n\\nMedian 档下 e_i pipeline 的三个 source 贡献不对称：performance gap 是主要信号源， 移除后 τ 下降最大（0.823→0.786），因为它直接测量 \\\"original vs rephrased\\\" 的分数差—— 最接近 contamination 的操作性定义。Temporal signal 贡献最弱（移除后 τ 仅降 0.005）， 因为其覆盖率仅 41% 且许多 item 的时间切分不精确。LogProber 居中——它捕获 verbatim 记忆（与 performance gap 的 \\\"能力增益\\\" 部分互补），但受限于 API 模型可用性。 性能对权重组合不太敏感（τ 在 [0.810, 0.825] 范围内），说明三个 source 的信号 方向一致但噪声不同。单独使用 performance gap 已能达到总效果的 ~80%—— 这简化了实际部署：practitioners 只需构建 reference variants，不必部署 LogProber。\\n\"\n  },\n  {\n    \"name\": \"facet_fit_diagnostics\",\n    \"description\": \"Measurement quality validation: infit/outfit, person-fit statistics, posterior predictive checks, divergent transitions, trace plots.\\n\",\n    \"results\": {\n      \"theta_infit_range\": [\n        0.82,\n        1.28\n      ],\n      \"theta_outfit_range\": [\n        0.78,\n        1.35\n      ],\n      \"theta_misfit_count\": 2,\n      \"b_infit_range\": [\n        0.71,\n        1.42\n      ],\n      \"b_outfit_range\": [\n        0.65,\n        1.58\n      ],\n      \"b_misfit_count\": 38,\n      \"b_misfit_fraction\": 0.058,\n      \"d_infit_range\": [\n        0.94,\n        1.21\n      ],\n      \"d_outfit_range\": [\n        0.88,\n        1.31\n      ],\n      \"d_misfit_count\": 1,\n      \"lz_cn_pearson_r\": 0.41,\n      \"lz_cn_spearman_rho\": 0.45,\n      \"emri_cn_pearson_r\": 0.38,\n      \"ppc_mean_residual\": 0.02,\n      \"ppc_residual_std\": 0.31,\n      \"ppc_outlier_fraction\": 0.047,\n      \"divergent_transitions_total\": 14,\n      \"divergent_transitions_fraction\": 0.0007,\n      \"max_treedepth_fraction\": 0.032,\n      \"p_waic\": 187,\n      \"waic_gmfrm\": -42381,\n      \"waic_mfrm\": -41892,\n      \"delta_waic\": -489,\n      \"delta_waic_se\": 124\n    },\n    \"tables\": [\n      {\n        \"name\": \"fit_statistics_summary\",\n        \"caption\": \"Facet fit statistics summary\",\n        \"columns\": [\n          \"Facet\",\n          \"N\",\n          \"Infit MNSQ Range\",\n          \"Outfit MNSQ Range\",\n          \"Misfit Count\",\n          \"Misfit Fraction\"\n        ],\n        \"rows\": [\n          [\n            \"Model (theta)\",\n            \"22\",\n            \"[0.82, 1.28]\",\n            \"[0.78, 1.35]\",\n            \"2\",\n            \"0.091\"\n          ],\n          [\n            \"Item (b)\",\n            \"660\",\n            \"[0.71, 1.42]\",\n            \"[0.65, 1.58]\",\n            \"38\",\n            \"0.058\"\n          ],\n          [\n            \"Judge (d)\",\n            \"8\",\n            \"[0.94, 1.21]\",\n            \"[0.88, 1.31]\",\n            \"1\",\n            \"0.125\"\n          ],\n          [\n            \"Contamination (c)\",\n            \"22\",\n            \"—\",\n            \"—\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"personfit_vs_cn\",\n        \"caption\": \"Person-fit statistic correlation with contamination estimate\",\n        \"columns\": [\n          \"Person-fit Statistic\",\n          \"Correlation with c_n\",\n          \"p-value\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"lz (standardized)\",\n            \"0.41\",\n            \"0.058\",\n            \"Moderate; c_n captures part of lz signal\"\n          ],\n          [\n            \"EMRi\",\n            \"0.38\",\n            \"0.081\",\n            \"Moderate; similar to lz\"\n          ],\n          [\n            \"Infit MNSQ\",\n            \"0.29\",\n            \"0.192\",\n            \"Weak; misfit not solely from contamination\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"model_comparison_waic\",\n        \"caption\": \"Model comparison via WAIC\",\n        \"columns\": [\n          \"Model\",\n          \"WAIC\",\n          \"p_WAIC\",\n          \"Delta WAIC\",\n          \"SE(Delta)\"\n        ],\n        \"rows\": [\n          [\n            \"G-MFRM (Stage 3)\",\n            \"-42381\",\n            \"187\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"MFRM (Stage 1)\",\n            \"-41892\",\n            \"142\",\n            \"+489\",\n            \"124\"\n          ],\n          [\n            \"Raw IRT (no facets)\",\n            \"-39847\",\n            \"68\",\n            \"+2534\",\n            \"312\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Diagnostics 支持 G-MFRM 的测量质量，但需在论文中报告 misfitting items 和 convergence 细节。WAIC 比较提供了统计层面的模型选择证据（ΔW = -489 ± 124， 约 4σ 显著），即使 τ 改善 modest。lz-c_n 的中等相关是叙事亮点： 传统 person-fit 能检测 \\\"something wrong\\\" 但不能归因；G-MFRM 的 c_n 提供 可解释的归因——\\\"this model's anomalous response pattern is partly explained by contamination susceptibility\\\"。这直接支持 diagnostics-as-co-primary 叙事。\\n\\n\\nMedian 档下 facet fit 总体可接受但有局部问题： (1) 38 个 item（5.8%）misfit，主要是 Arena-Hard 的 coding 题（这些题评分分布 高度双峰——要么完全正确要么完全错误，不符合 Rasch 的连续性假设）； (2) 2 个 model misfit（infit > 1.28），likely 因其能力 profile 在不同 item 类别间 高度不一致（如某模型 coding 极强但 humanities 极弱），违反 unidimensionality； (3) lz-c_n 相关 r = 0.41 表明 person-fit 异常部分（但非全部）可被 contamination 解释—— 这支持 c_n 作为独立参数的必要性，而非仅靠 misfit detection 替代； (4) ΔWAIC = -489 ± 124 支持 G-MFRM 优于 MFRM 的模型选择，即使排名改善 modest； (5) Divergent transitions 0.07% 在可接受范围内，主要集中在 near-zero c_n 模型 （Half-Cauchy prior 在零附近的梯度问题），不影响整体推断。\\n\"\n  },\n  {\n    \"name\": \"confounding_formal_observation\",\n    \"description\": \"Formal OVB bias derivation + Monte Carlo validation + synthetic c_n point-estimate validation.\\n\",\n    \"results\": {\n      \"bias_formula_derived\": true,\n      \"bias_direction_prediction\": \"overestimation when Cov(d_j, c_n·e_i) > 0\",\n      \"bias_magnitude_first_order\": \"β_OVB ≈ Cov(d_j, c_n·e_i) / Var(d_j)\",\n      \"mc_replications\": 1000,\n      \"mc_bias_direction_correct_fraction\": 0.91,\n      \"mc_bias_magnitude_rmse\": 0.08,\n      \"mc_sequential_bias_first_theta_bias\": 0.13,\n      \"mc_sequential_contam_first_theta_bias\": 0.11,\n      \"mc_joint_theta_bias\": 0.02,\n      \"mc_joint_theta_rmse\": 0.13,\n      \"mc_sequential_theta_rmse\": 0.19,\n      \"mc_rmse_reduction\": 0.316,\n      \"confounding_scatter_r\": 0.35,\n      \"confounding_scatter_p\": 0.002,\n      \"cn_point_rmse\": 0.44,\n      \"cn_95ci_coverage\": 0.88,\n      \"cn_corr_with_true\": 0.82,\n      \"cn_mean_bias\": 0.06,\n      \"rho_sweep_values\": [\n        0.0,\n        0.15,\n        0.3,\n        0.45,\n        0.6\n      ],\n      \"bias_at_rho_0\": 0.01,\n      \"bias_at_rho_0_15\": 0.05,\n      \"bias_at_rho_0_30\": 0.1,\n      \"bias_at_rho_0_45\": 0.15,\n      \"bias_at_rho_0_60\": 0.21\n    },\n    \"tables\": [\n      {\n        \"name\": \"monte_carlo_bias_summary\",\n        \"caption\": \"Monte Carlo bias validation (1000 replications, ρ = 0.30)\",\n        \"columns\": [\n          \"Estimator\",\n          \"Mean theta bias\",\n          \"Theta RMSE\",\n          \"RMSE vs Joint\"\n        ],\n        \"rows\": [\n          [\n            \"Joint G-MFRM\",\n            \"0.02\",\n            \"0.13\",\n            \"—\"\n          ],\n          [\n            \"Sequential (bias-first)\",\n            \"0.13\",\n            \"0.19\",\n            \"+46.2%\"\n          ],\n          [\n            \"Sequential (contam-first)\",\n            \"0.11\",\n            \"0.18\",\n            \"+38.5%\"\n          ],\n          [\n            \"MFRM-only (ignore c)\",\n            \"0.14\",\n            \"0.20\",\n            \"+53.8%\"\n          ],\n          [\n            \"Raw average\",\n            \"0.31\",\n            \"0.38\",\n            \"+192.3%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"rho_sweep\",\n        \"caption\": \"Sequential estimator bias as function of confounding strength ρ\",\n        \"columns\": [\n          \"rho(d,ce)\",\n          \"Sequential Bias\",\n          \"Joint Bias\",\n          \"Bias Ratio\"\n        ],\n        \"rows\": [\n          [\n            \"0.00\",\n            \"0.01\",\n            \"0.01\",\n            \"1.0\"\n          ],\n          [\n            \"0.15\",\n            \"0.05\",\n            \"0.01\",\n            \"5.0\"\n          ],\n          [\n            \"0.30\",\n            \"0.10\",\n            \"0.02\",\n            \"5.0\"\n          ],\n          [\n            \"0.45\",\n            \"0.15\",\n            \"0.02\",\n            \"7.5\"\n          ],\n          [\n            \"0.60\",\n            \"0.21\",\n            \"0.03\",\n            \"7.0\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"cn_recovery\",\n        \"caption\": \"Synthetic c_n recovery statistics\",\n        \"columns\": [\n          \"Metric\",\n          \"Value\",\n          \"Acceptable Threshold\"\n        ],\n        \"rows\": [\n          [\n            \"Point RMSE\",\n            \"0.44\",\n            \"< 0.60\"\n          ],\n          [\n            \"95% CI Coverage\",\n            \"0.88\",\n            \"> 0.90 (marginal)\"\n          ],\n          [\n            \"Correlation with true c_n\",\n            \"0.82\",\n            \"> 0.70\"\n          ],\n          [\n            \"Mean bias\",\n            \"+0.06\",\n            \"< 0.10\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"OVB Observation 在合成数据上得到清晰验证。ρ sweep 图是 Section 2 的核心—— 直观展示 confounding 如何随 ρ 增长导致 sequential bias 线性增长，而 joint estimation 保持无偏。c_n 回收的 88% coverage 需在 Limitations 中提及—— posterior 在高 c_n 处略偏窄，可能因 Half-Cauchy 先验的约束效应。 Confounding scatter r = 0.35 足以支持 \\\"mechanism exists\\\"（Claim 1）的 median 档表述。\\n\\n\\nMedian 档下 Monte Carlo 验证了 OVB 机制但效应量 moderate： (1) Bias direction 正确率 91%（非 100% 因为有限样本噪声在低 ρ 时可逆转方向）； (2) Sequential bias ≈ 0.11-0.13 logits，处于 \\\"≤ 0.15 for most models\\\" 的范围内； (3) Joint estimation 大幅降低 bias 至 0.02（接近无偏），RMSE 降低 31.6%， 但这是在受控合成数据上——真实数据效果会因 e_i 噪声而打折； (4) Confounding scatter r = 0.35 处于 [0.25, 0.45] 中部，低于 mvp_002/003 的 r = 0.65（后者是强污染下的结果），反映 median 档下信号较弱； (5) c_n 点估计回收 RMSE = 0.44，95% CI 覆盖率 88%——略低于 nominal 95%， 说明 posterior 有轻微欠覆盖（Half-Cauchy prior 在高 c_n 值时约束过强）， 但对 c_n 排序而言足够（corr = 0.82）。 ρ sweep 清楚展示了 bias 随 confounding 强度单调递增，为 Section 2 的 \\\"Observation\\\" 提供了直观的教学图表。\\n\"\n  },\n  {\n    \"name\": \"wildbench_replication\",\n    \"description\": \"Replicate G-MFRM pipeline on WildBench as third benchmark for cross-benchmark generalization.\\n\",\n    \"results\": {\n      \"wildbench_items\": 1024,\n      \"wildbench_judges_used\": 6,\n      \"wildbench_models_evaluated\": 18,\n      \"wildbench_tau_gmfrm\": 0.808,\n      \"wildbench_tau_mfrm\": 0.786,\n      \"wildbench_tau_raw\": 0.749,\n      \"wildbench_tau_uda\": 0.793,\n      \"wildbench_delta_tau_vs_uda\": 0.015,\n      \"wildbench_delta_p\": 0.094,\n      \"wildbench_cn_median\": 0.38,\n      \"wildbench_cn_correlation_with_mtbench_cn\": 0.71,\n      \"wildbench_rhat_max\": 1.08,\n      \"wildbench_ess_min\": 96,\n      \"wildbench_runtime_seconds\": 11240,\n      \"wildbench_ei_mean\": 0.26,\n      \"wildbench_ei_internal_consistency\": 0.37\n    },\n    \"tables\": [\n      {\n        \"name\": \"cross_benchmark_comparison\",\n        \"caption\": \"G-MFRM performance across benchmarks\",\n        \"columns\": [\n          \"Benchmark\",\n          \"N Items\",\n          \"N Judges\",\n          \"tau G-MFRM\",\n          \"tau UDA\",\n          \"Delta tau\",\n          \"p-value\",\n          \"c_n median\"\n        ],\n        \"rows\": [\n          [\n            \"MT-Bench\",\n            \"160\",\n            \"8\",\n            \"0.811\",\n            \"0.798\",\n            \"+0.013\",\n            \"0.112\",\n            \"0.55\"\n          ],\n          [\n            \"Arena-Hard\",\n            \"500\",\n            \"8\",\n            \"0.831\",\n            \"0.812\",\n            \"+0.019\",\n            \"0.054\",\n            \"0.44\"\n          ],\n          [\n            \"WildBench\",\n            \"1024\",\n            \"6\",\n            \"0.808\",\n            \"0.793\",\n            \"+0.015\",\n            \"0.094\",\n            \"0.38\"\n          ],\n          [\n            \"Combined (MT+AH)\",\n            \"660\",\n            \"8\",\n            \"0.823\",\n            \"0.805\",\n            \"+0.018\",\n            \"0.067\",\n            \"0.48\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"cn_cross_benchmark\",\n        \"caption\": \"Cross-benchmark c_n consistency (Pearson correlation)\",\n        \"columns\": [\n          \"Benchmark Pair\",\n          \"Shared Models\",\n          \"c_n Correlation\",\n          \"p-value\"\n        ],\n        \"rows\": [\n          [\n            \"MT-Bench vs Arena-Hard\",\n            \"22\",\n            \"0.78\",\n            \"< 0.001\"\n          ],\n          [\n            \"MT-Bench vs WildBench\",\n            \"18\",\n            \"0.68\",\n            \"0.002\"\n          ],\n          [\n            \"Arena-Hard vs WildBench\",\n            \"18\",\n            \"0.74\",\n            \"< 0.001\"\n          ],\n          [\n            \"(MT+AH) vs WildBench\",\n            \"18\",\n            \"0.71\",\n            \"0.001\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"WildBench 复制确认了 G-MFRM 的跨 benchmark 泛化性，但效应量更小（lower contamination）。 核心价值在于 c_n 跨 benchmark 一致性（r = 0.68-0.78）——证明 contamination susceptibility 是 model-level trait 而非 benchmark artifact。 论文应将此作为 c_n 构念效度的额外证据，而非第三个独立的排名改善论证。\\n\\n\\nWildBench 的 c_n 中位数（0.38）低于 MT-Bench+Arena-Hard（0.48），因为 WildBench 发布较晚、item 更多样且更接近真实用户 query（更难被训练数据直接覆盖）。 这进一步压缩了 G-MFRM 的排名改善空间（Δτ = 0.015 vs UDA，p = 0.094 不显著）。 但跨 benchmark 的 c_n 一致性高（r = 0.71）——同一模型在不同 benchmark 上的 contamination susceptibility 相关，支持 c_n 作为 \\\"model-level trait\\\" 的构念效度。 收敛性比主实验略差（R̂=1.08, ESS=96），可能因 6 judges（而非 8）降低了信息量。 e_i 内部一致性更低（0.37 vs 0.43），因为 WildBench 的 item 更长更复杂， reference variant 构建质量下降。这是跨 benchmark 泛化的实际成本。\\n\"\n  },\n  {\n    \"name\": \"adversarial_robustness\",\n    \"description\": \"Test G-MFRM robustness against adversarial contamination following Wang et al. (ICLR 2026).\\n\",\n    \"results\": {\n      \"adversarial_types_tested\": 3,\n      \"adversarial_models_injected\": 4,\n      \"cn_detection_auc_mild\": 0.78,\n      \"cn_detection_auc_moderate\": 0.84,\n      \"cn_detection_auc_severe\": 0.91,\n      \"theta_rank_corruption_without_gmfrm\": 3.2,\n      \"theta_rank_corruption_with_gmfrm\": 1.1,\n      \"rank_protection_rate\": 0.66,\n      \"undetectable_adversarial_fraction\": 0.22,\n      \"failure_mode\": \"Adversarial contamination that mimics genuine ability gain (uniform across items) is undetectable by rank-1 c·e gating\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"adversarial_detection\",\n        \"caption\": \"G-MFRM adversarial contamination detection performance\",\n        \"columns\": [\n          \"Adversarial Type\",\n          \"Severity\",\n          \"c_n AUC\",\n          \"Rank Corruption w/o G-MFRM\",\n          \"Rank Corruption w/ G-MFRM\"\n        ],\n        \"rows\": [\n          [\n            \"Data Poisoning\",\n            \"Mild\",\n            \"0.76\",\n            \"1.8\",\n            \"0.9\"\n          ],\n          [\n            \"Data Poisoning\",\n            \"Severe\",\n            \"0.92\",\n            \"4.1\",\n            \"1.2\"\n          ],\n          [\n            \"Prompt Injection\",\n            \"Mild\",\n            \"0.74\",\n            \"1.5\",\n            \"0.8\"\n          ],\n          [\n            \"Prompt Injection\",\n            \"Severe\",\n            \"0.88\",\n            \"3.8\",\n            \"1.4\"\n          ],\n          [\n            \"Benchmark Memorization\",\n            \"Mild\",\n            \"0.83\",\n            \"2.1\",\n            \"0.7\"\n          ],\n          [\n            \"Benchmark Memorization\",\n            \"Severe\",\n            \"0.93\",\n            \"4.5\",\n            \"0.9\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"G-MFRM 提供了 meaningful 但非完美的 adversarial 防御。论文应定位为 \\\"G-MFRM detects and mitigates item-specific contamination patterns (rank-1 structure); uniform adversarial inflation remains a fundamental detection limit shared by all item-level analysis methods.\\\" Rank-k 扩展作为 future work 指向。\\n\\n\\nMedian 档下 G-MFRM 对 adversarial contamination 的防御是 partial： (1) Severe contamination（大幅度、item-specific 的性能膨胀）被 c_n 可靠检测（AUC=0.91）， 因为 rank-1 c·e 结构能捕获 item-specific 膨胀模式； (2) Mild contamination（小幅度、接近均匀的膨胀）检测 AUC 降至 0.78，因为均匀膨胀 与真实能力提升难以区分——这是 rank-1 假设的根本限制； (3) 22% 的 adversarial 模式完全不可检测——特别是\\\"能力伪装型\\\"污染 （在所有 item 上均匀小幅提升），被吸收进 θ̂ 而非 c_n。 Rank protection rate 0.66 表明 G-MFRM 缓解了约 2/3 的排名腐蚀， 但不是完全防御。论文应在 Limitations 中坦诚讨论这一边界。\\n\"\n  },\n  {\n    \"name\": \"error_propagation_sensitivity\",\n    \"description\": \"Sensitivity analysis for staged estimation: inject Gaussian noise into e_i at σ=0.1,0.2,0.5. Measure θ̂ RMSE degradation and c_n recovery accuracy.\\n\",\n    \"results\": {\n      \"sigma_0_theta_rmse\": 0.128,\n      \"sigma_0_theta_tau\": 0.916,\n      \"sigma_0_cn_rmse\": 0.53,\n      \"sigma_0_cn_corr\": 0.86,\n      \"sigma_01_theta_rmse\": 0.13,\n      \"sigma_01_theta_tau\": 0.915,\n      \"sigma_01_cn_rmse\": 0.55,\n      \"sigma_01_cn_corr\": 0.85,\n      \"sigma_01_delta_theta_pct\": 1.6,\n      \"sigma_01_delta_cn_pct\": 3.8,\n      \"sigma_02_theta_rmse\": 0.136,\n      \"sigma_02_theta_tau\": 0.914,\n      \"sigma_02_cn_rmse\": 0.58,\n      \"sigma_02_cn_corr\": 0.84,\n      \"sigma_02_delta_theta_pct\": 6.3,\n      \"sigma_02_delta_cn_pct\": 9.4,\n      \"sigma_05_theta_rmse\": 0.175,\n      \"sigma_05_theta_tau\": 0.885,\n      \"sigma_05_cn_rmse\": 0.84,\n      \"sigma_05_cn_corr\": 0.75,\n      \"sigma_05_delta_theta_pct\": 36.7,\n      \"sigma_05_delta_cn_pct\": 58.5,\n      \"all_converged\": true,\n      \"rhat_max_all\": 1.02,\n      \"robust_threshold\": 0.2,\n      \"verdict\": \"PARTIAL — robust at σ ≤ 0.2, exceeds threshold at σ = 0.5\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"sensitivity_results\",\n        \"caption\": \"Error propagation sensitivity analysis (20 synthetic replications per σ)\",\n        \"columns\": [\n          \"sigma_e\",\n          \"theta RMSE\",\n          \"theta tau\",\n          \"c_n RMSE\",\n          \"c_n Corr\",\n          \"Delta theta %\",\n          \"Delta c_n %\"\n        ],\n        \"rows\": [\n          [\n            \"0.0\",\n            \"0.128\",\n            \"0.916\",\n            \"0.53\",\n            \"0.86\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"0.1\",\n            \"0.130\",\n            \"0.915\",\n            \"0.55\",\n            \"0.85\",\n            \"+1.6%\",\n            \"+3.8%\"\n          ],\n          [\n            \"0.2\",\n            \"0.136\",\n            \"0.914\",\n            \"0.58\",\n            \"0.84\",\n            \"+6.3%\",\n            \"+9.4%\"\n          ],\n          [\n            \"0.5\",\n            \"0.175\",\n            \"0.885\",\n            \"0.84\",\n            \"0.75\",\n            \"+36.7%\",\n            \"+58.5%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"已完成实验，实际结果与 median 档预测高度一致（实际 σ=0.2 时 θ RMSE +5.9%， 预测 +6.3%）。论文的关键论证：staged estimation 在合理 e_i 噪声下（σ ≤ 0.2） 足够鲁棒，这使得 \\\"conditional joint estimation\\\" 成为可辩护的设计选择—— 无需完全联合估计（under-identified）即可获得稳健结果。 σ = 0.5 的结果作为 worst-case 上界在 Limitations 中讨论。\\n\\nMedian 档下 e_i 的有效 σ ≈ 0.24，恰好处于 robust (σ≤0.2) 和 degraded (σ=0.5) 之间的过渡区。这意味着真实数据的 Stage 3 结果会经历 ~6-10% 的 θ 精度损失 （相对于 oracle e_i），但不会崩溃。关键观察：θ̂ 对 e_i 噪声的鲁棒性优于 c_n 的 鲁棒性——σ=0.2 时 θ RMSE 仅增 6.3% 但 c_n RMSE 增 9.4%。这是因为 θ̂ 同时受 多个 item 的约束（聚合效应缓冲了 e_i 噪声），而 c_n 直接依赖 e_i·c_n 的乘积项， 噪声传播更直接。σ=0.5 的结果（θ degradation 36.7%）是上界估计——说明如果 e_i pipeline 完全失效，staged estimation 的优势将大幅削减。论文应引用此结果论证： \\\"Stage 2 e_i 估计质量是系统性能的关键瓶颈，但在当前 pipeline（σ ≈ 0.2-0.25）下 性能退化在可接受范围内。\\\"\\n\"\n  }\n]",
      "numLines": 1864,
      "startLine": 1,
      "totalLines": 1864
    }
  },
  "sourceToolAssistantUUID": "a1d76f64-1516-4f94-9262-69cb6b43e684",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-22T04:42:46.497Z_

<details><summary>↩ Tool result · `toolu_01NnKMxpRJq53PJ4x8KMDgSq`</summary>

```text
1	# Paper Framing — gated_mfrm_judge_bias
2	
3	## Target Venue
4	- Primary: AAAI 2027 (full paper, deadline July 28, 2026)
5	- Backup: ACL 2027 via ARR (submission August 3, 2026)
6	- Timeline: ~68 days from today (2026-05-21)
7	
8	## Core Insight
9	Sequential approaches to judge bias correction and contamination adjustment produce biased model ability estimates due to omitted variable confounding. Joint estimation within a single psychometric calibration framework is methodologically necessary, not merely convenient.
10	
11	## Core Claims (3 条，均可证伪)
12	
13	1. **Confounding Claim**: When judge severity (d_j) and contamination susceptibility (c_n·e_i) are both present but only one is modeled, the unmodeled facet's effect is absorbed into other parameter estimates, producing systematic bias in model ability rankings. Sequential pipelines (bias-first or contamination-first) do not resolve this confounding. (Note: OVB formalization supports this claim as mechanism explanation — "identify and quantify confounding in LLM evaluation" — not as independent theoretical contribution. Cite Angrist & Pischke 2009 as source.)
14	
15	2. **Framework Claim**: The Gated Many-Facet Rasch Model (G-MFRM) — combining MFRM's multi-facet structure with DG-IRT's gating mechanism and externally-anchored exposure indicators — provides a staged joint calibration that estimates model ability, item difficulty, judge severity, and contamination susceptibility, yielding bias-and-contamination-corrected "fair scores." (Note: "staged joint" — e_i is pre-estimated in Stage 2 and fixed in Stage 3; the joint estimation is conditional on e_i. This is a deliberate identifiability choice, not fully simultaneous. Paper must use "staged joint calibration" or "conditional joint estimation," never "fully joint.")
16	
17	3. **Empirical Claim**: G-MFRM fair scores achieve higher agreement with human rankings (Chatbot Arena votes, Kendall-τ) than all baselines: raw multi-judge averages, bias-only correction (CyclicJudge, UDA), contamination-only adjustment (DCR), and naive sequential pipelines.
18	
19	## Story Spine
20	
21	- **Problem**: LLM-as-a-judge evaluation has bifurcated into two correction silos — judge bias and benchmark contamination — that are addressed independently. But judge severity and contamination effects are confounded: bias-only methods absorb contamination inflation into ability estimates; contamination-only methods misattribute judge effects as contamination signals. Sequential correction cannot resolve this because the first stage's estimates are already biased by the unmodeled facet.
22	
23	- **Existing approaches & gaps**: CyclicJudge eliminates average judge bias via round-robin but ignores contamination. UDA uses neural K-factor adjustment (−63.4% inter-judge std) but is black-box and contamination-unaware. DCR/ConStat quantify contamination effects (r²=0.94) but ignore judge variation. In LLM evaluation literature, no existing work jointly models both within a single calibration framework. (Note: educational measurement has MFRM+DIF joint modeling — Eckes 2011, Patz et al. 2002, Fox & Glas 2001, Wind & Peterson 2018 — but these address test fairness, not LLM contamination. G-MFRM is the first to apply continuous-exposure gating within MFRM for LLM evaluation. "First" claim must be precisely scoped to LLM evaluation with continuous exposure.)
24	
25	- **Our framing**: Joint estimation is methodologically necessary. We formalize this as an omitted variable bias problem: under non-orthogonality of d_j and c_n·e_i, sequential estimators are asymptotically biased (direction determined by covariance sign). G-MFRM resolves this by estimating all facets simultaneously, with a three-stage procedure ensuring identifiability: (1) standard MFRM for initial estimates, (2) external per-item exposure estimation via item-level performance gap (original vs reference variants) with difficulty correction, supplemented by temporal signals and LogProber where available, (3) joint gated model with e_i fixed and c_n as latent parameters. ConStat per-model delta serves as external validation of fitted c_n.
26	
27	- **Headline result template**: "On MT-Bench/Arena-Hard with 8 LLM judges, G-MFRM fair scores achieve X% higher Kendall-τ with Chatbot Arena human votes than the best sequential baseline, while simultaneously producing interpretable per-model contamination estimates and per-judge severity profiles."
28	
29	## Narrative Strategy (from distilled writing)
30	
31	- **Type**: "突破局限" (sequential has structural flaw) + "统一框架" (G-MFRM unifies both corrections)
32	- **Opening hook**: Quantitative shock — lead with confounding's θ-RMSE degradation (43.8% in synthetic, to be validated on real data)
33	- **Section 2**: Toy example / formal **observation** (NOT "proposition" — this is standard OVB from Angrist & Pischke 2009 applied to LLM evaluation; cite originals, present as domain-specific instantiation) demonstrating confounding before introducing G-MFRM method
34	- **Figure 1**: Left = sequential pipeline with confounding annotation, Right = joint G-MFRM with gating mechanism highlighted
35	- **Main result table**: rows = methods (7 baselines + G-MFRM), cols = benchmarks × metrics
36	- **Ablation**: Full numbers (not checkmark grid), rows = components on/off
37	
38	## Venue Fit Risks
39	
40	- **AAAI**: Good fit for psychometric methodology applied to AI evaluation. Risk: reviewers may lack MFRM/IRT background — need clear, self-contained exposition with toy examples. Strength: AAAI values formal modeling + practical impact.
41	- **ACL/ARR**: Good fit for LLM evaluation methodology. Risk: may demand stronger NLP-specific contributions beyond the measurement framework. Strength: directly relevant to LLM evaluation community.
42	
43	## Anticipated Reviewer Concerns & Responses
44	
45	1. **"Why not CyclicJudge + discard contaminated items?"** — Item discard wastes information; CyclicJudge doesn't capture item-specific judge effects; neither produces c_n for auditing; G-MFRM degrades gracefully to standard MFRM when contamination ≈ 0.
46	
47	2. **"Is confounding large enough in practice?"** — MVP synthetic: 43.8% RMSE degradation. Real-data calibration (P0 experiment) will establish realistic contamination magnitude. Bias scatter (r=0.65) shows the mechanism exists regardless of magnitude.
48	
49	3. **"Rank-1 assumption (c_n·e_i) too strong"** — Rank-1 is LLTM tradition, good approximation when contamination comes from dominant data source. Person-fit diagnostics (infit/outfit) detect violations. Rank-k extension is future work.
50	
51	4. **"DG-IRT transfer is trivial"** — Three structural differences require non-trivial adaptation: binary→continuous exposure, single-rater→multi-facet, known→unknown exposure status. Stage 2 external anchoring solves a fundamental obstacle (exposure unknown to administrator) absent in educational testing. Error propagation from Stage 2→3 must be discussed in Limitations with sensitivity analysis (vary e_i noise σ=0.1,0.2,0.5).
52	
53	4b. **"Staged estimation ≠ joint estimation"** — Correct: e_i is pre-fixed in Stage 2, so estimation is conditional-joint, not fully simultaneous. Frame as deliberate identifiability choice: true joint estimation of (θ,b,d,c,e) is under-identified without external anchoring. Staged estimation is the principled solution. Compare to two-step estimators in econometrics (Heckman 1979). Error propagation sensitivity analysis shows robustness.
54	
55	5. **"Contamination signal realistic?"** — ConStat validated r²=0.94 with true contamination effects. LogProber provides per-item memorization indicators. Multiple indicators combined via weighted composite. P0 experiment calibrates against real benchmarks.
56	
57	6. **"Chatbot Arena Elo as ground truth — circular reasoning?"** — Arena uses real-time human pairwise comparisons with user-submitted prompts (not fixed benchmark items). Contamination inflates benchmark scores but does not directly improve conversational ability. Arena Elo is the least-contaminated human preference signal available. Acknowledge limitation in paper but argue decoupling is strong.
58	
59	7. **"c_n ≥ 0 assumption too restrictive?"** — Half-Cauchy prior enforces non-negativity, appropriate for the "contamination as unfair advantage" framing. Adversarial contamination (intentional performance degradation) is outside scope. Discuss in Limitations.
60	
61	8. **"≥4 judges needed — too expensive?"** — exp-006 sensitivity analysis shows degradation curve. Discuss in Limitations: at 2 judges, G-MFRM degrades gracefully to MFRM-level (no contamination correction). Cost-benefit analysis for practitioners.
62	
63	9. **"No judge-model interaction term?"** — G-MFRM has d_j (judge-level) and c_n·e_i (model-item), but no f_{nj} (judge-model interaction). Preference Leakage shows same-model PLS≈23.6%, same-family≈8.9%. When GPT-5.5 judges GPT-5.5, this bias distributes uniformly across items and gets absorbed into θ̂_n. Mitigation: (a) exp-006 leave-one-judge-out residual diagnostic detects if specific judges inflate same-family models; (b) Limitations section acknowledges scope boundary; (c) rank-k extension with judge-model interaction is future work.
64	
65	## Two-Tier Narrative (contingent on exp-005 contamination magnitude)
66	
67	**Tier A — Strong contamination (c ≈ 1.0-1.5, matching mvp_002/003)**:
68	- Lead with ranking correction as primary contribution
69	- Claim 3 at full strength: "G-MFRM achieves X% higher Kendall-τ"
70	- Headline: joint estimation dramatically outperforms sequential
71	
72	**Tier B — Weak contamination (c ≈ 0.3-0.5, matching mvp_001)**:
73	- Elevate diagnostic interpretability to co-primary contribution (per IDEA_BRIEF optimization A4)
74	- Reframe: "even when ranking improvement is modest, G-MFRM uniquely provides per-model c_n (training audit), per-item e_i (item retirement), per-judge d_j (judge calibration)"
75	- Bias scatter r=0.65 proves the mechanism exists; practical impact scales with contamination magnitude
76	- Claim 3 softened to "comparable or better rankings PLUS interpretable diagnostic outputs"
77	
78	**Tier B+ — Diagnostics as sole primary (if Claim 1 ρ≈0 AND Claim 3 Δτ non-significant)**:
79	- Diagnostics become the **sole** primary contribution (not co-primary)
80	- Paper becomes "tool paper": G-MFRM as diagnostic framework for LLM evaluation auditing
81	- Contribution: per-model c_n (training data audit), per-item e_i (item retirement), per-judge d_j (judge calibration) — unified diagnostic outputs no existing tool provides
82	- Risk: "tool paper" positioning may be weaker for Main Conference; strong for Findings
83	
84	exp-005 determines which tier. Decision point: after exp-005 results, before paper writing.
85	
86	## Novelty Supplementation Strategy
87	
88	Dream R2 exposed a novelty ceiling: "MFRM + 1 term" + "textbook OVB" = combinatorial novelty. Even with best-case data, Main Conference bar may not be met on novelty alone. Supplement with:
89	
90	1. **Identifiability analysis** (Method section): Prove necessary and sufficient conditions for (θ, b, d, c) identifiability when e_i is fixed. This is a non-trivial technical contribution beyond "adding a term."
91	2. **Formal e_i uncertainty propagation**: Beyond sensitivity analysis (exp-012), provide theoretical treatment of how e_i estimation error propagates to c_n credible intervals. Compare to two-step estimator literature (Heckman 1979, Murphy & Topel 1985).
92	3. **Diagnostic framework formalization**: Frame the four-dimensional output (θ, d_j, c_n, e_i) as a principled measurement framework, not just parameter estimates. Connect to DIF (Differential Item Functioning) tradition.
93	
94	## Bibliography Strategy (Paper Agent input)
95	
96	Required references by positioning role:
97	- **Foundational IRT**: Rasch 1960, Lord & Novick 1968, Fox 2010 (Bayesian IRT)
98	- **MFRM ancestor**: Linacre 1989, Engelhard 2002/2013, Eckes 2011/2015
99	- **DG-IRT ancestor**: Shu et al. 2013 (Psychometrika), Robitzsch 2020
100	- **MFRM+DIF (educational)**: Wind & Peterson 2018, Patz et al. 2002, Fox & Glas 2001
101	- **LLM contamination**: Golchin & Surdeanu 2023, Shi et al. 2023 (Min-K%), ConStat, DCR
102	- **LLM judge bias**: Zheng et al. 2023 (MT-Bench), CyclicJudge, UDA, Preference Leakage
103	- **Benchmarks**: Arena-Hard original, WildBench original, LiveBench
104	- **Econometrics**: Angrist & Pischke 2009 (OVB), Heckman 1979 (two-step)
105	Target: 30-40 references total.
106	
107	## MVP Evidence Summary
108	
109	- mvp_003: Joint RMSE −43.8% vs Sequential (p=1e-6), Kendall-τ +6.3pp, R̂=1.03, ESS=224
110	- Bias scatter: Pearson r=0.65 (sequential systematically overestimates high-c_n models)
111	- Robustness: method effective even under model misspecification (DGP with s_j, model without)
112	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74358fb4-2c62-42d0-a80e-b8b00f1d5187",
  "isSidechain": false,
  "promptId": "207a7a17-59d3-4278-abf7-5d52712c6cbf",
  "type": "user",
  "uuid": "acf293fc-e085-4acb-bdfb-5fc99be890c0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median/paper_framing.md",
      "content": "# Paper Framing — gated_mfrm_judge_bias\n\n## Target Venue\n- Primary: AAAI 2027 (full paper, deadline July 28, 2026)\n- Backup: ACL 2027 via ARR (submission August 3, 2026)\n- Timeline: ~68 days from today (2026-05-21)\n\n## Core Insight\nSequential approaches to judge bias correction and contamination adjustment produce biased model ability estimates due to omitted variable confounding. Joint estimation within a single psychometric calibration framework is methodologically necessary, not merely convenient.\n\n## Core Claims (3 条，均可证伪)\n\n1. **Confounding Claim**: When judge severity (d_j) and contamination susceptibility (c_n·e_i) are both present but only one is modeled, the unmodeled facet's effect is absorbed into other parameter estimates, producing systematic bias in model ability rankings. Sequential pipelines (bias-first or contamination-first) do not resolve this confounding. (Note: OVB formalization supports this claim as mechanism explanation — \"identify and quantify confounding in LLM evaluation\" — not as independent theoretical contribution. Cite Angrist & Pischke 2009 as source.)\n\n2. **Framework Claim**: The Gated Many-Facet Rasch Model (G-MFRM) — combining MFRM's multi-facet structure with DG-IRT's gating mechanism and externally-anchored exposure indicators — provides a staged joint calibration that estimates model ability, item difficulty, judge severity, and contamination susceptibility, yielding bias-and-contamination-corrected \"fair scores.\" (Note: \"staged joint\" — e_i is pre-estimated in Stage 2 and fixed in Stage 3; the joint estimation is conditional on e_i. This is a deliberate identifiability choice, not fully simultaneous. Paper must use \"staged joint calibration\" or \"conditional joint estimation,\" never \"fully joint.\")\n\n3. **Empirical Claim**: G-MFRM fair scores achieve higher agreement with human rankings (Chatbot Arena votes, Kendall-τ) than all baselines: raw multi-judge averages, bias-only correction (CyclicJudge, UDA), contamination-only adjustment (DCR), and naive sequential pipelines.\n\n## Story Spine\n\n- **Problem**: LLM-as-a-judge evaluation has bifurcated into two correction silos — judge bias and benchmark contamination — that are addressed independently. But judge severity and contamination effects are confounded: bias-only methods absorb contamination inflation into ability estimates; contamination-only methods misattribute judge effects as contamination signals. Sequential correction cannot resolve this because the first stage's estimates are already biased by the unmodeled facet.\n\n- **Existing approaches & gaps**: CyclicJudge eliminates average judge bias via round-robin but ignores contamination. UDA uses neural K-factor adjustment (−63.4% inter-judge std) but is black-box and contamination-unaware. DCR/ConStat quantify contamination effects (r²=0.94) but ignore judge variation. In LLM evaluation literature, no existing work jointly models both within a single calibration framework. (Note: educational measurement has MFRM+DIF joint modeling — Eckes 2011, Patz et al. 2002, Fox & Glas 2001, Wind & Peterson 2018 — but these address test fairness, not LLM contamination. G-MFRM is the first to apply continuous-exposure gating within MFRM for LLM evaluation. \"First\" claim must be precisely scoped to LLM evaluation with continuous exposure.)\n\n- **Our framing**: Joint estimation is methodologically necessary. We formalize this as an omitted variable bias problem: under non-orthogonality of d_j and c_n·e_i, sequential estimators are asymptotically biased (direction determined by covariance sign). G-MFRM resolves this by estimating all facets simultaneously, with a three-stage procedure ensuring identifiability: (1) standard MFRM for initial estimates, (2) external per-item exposure estimation via item-level performance gap (original vs reference variants) with difficulty correction, supplemented by temporal signals and LogProber where available, (3) joint gated model with e_i fixed and c_n as latent parameters. ConStat per-model delta serves as external validation of fitted c_n.\n\n- **Headline result template**: \"On MT-Bench/Arena-Hard with 8 LLM judges, G-MFRM fair scores achieve X% higher Kendall-τ with Chatbot Arena human votes than the best sequential baseline, while simultaneously producing interpretable per-model contamination estimates and per-judge severity profiles.\"\n\n## Narrative Strategy (from distilled writing)\n\n- **Type**: \"突破局限\" (sequential has structural flaw) + \"统一框架\" (G-MFRM unifies both corrections)\n- **Opening hook**: Quantitative shock — lead with confounding's θ-RMSE degradation (43.8% in synthetic, to be validated on real data)\n- **Section 2**: Toy example / formal **observation** (NOT \"proposition\" — this is standard OVB from Angrist & Pischke 2009 applied to LLM evaluation; cite originals, present as domain-specific instantiation) demonstrating confounding before introducing G-MFRM method\n- **Figure 1**: Left = sequential pipeline with confounding annotation, Right = joint G-MFRM with gating mechanism highlighted\n- **Main result table**: rows = methods (7 baselines + G-MFRM), cols = benchmarks × metrics\n- **Ablation**: Full numbers (not checkmark grid), rows = components on/off\n\n## Venue Fit Risks\n\n- **AAAI**: Good fit for psychometric methodology applied to AI evaluation. Risk: reviewers may lack MFRM/IRT background — need clear, self-contained exposition with toy examples. Strength: AAAI values formal modeling + practical impact.\n- **ACL/ARR**: Good fit for LLM evaluation methodology. Risk: may demand stronger NLP-specific contributions beyond the measurement framework. Strength: directly relevant to LLM evaluation community.\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"Why not CyclicJudge + discard contaminated items?\"** — Item discard wastes information; CyclicJudge doesn't capture item-specific judge effects; neither produces c_n for auditing; G-MFRM degrades gracefully to standard MFRM when contamination ≈ 0.\n\n2. **\"Is confounding large enough in practice?\"** — MVP synthetic: 43.8% RMSE degradation. Real-data calibration (P0 experiment) will establish realistic contamination magnitude. Bias scatter (r=0.65) shows the mechanism exists regardless of magnitude.\n\n3. **\"Rank-1 assumption (c_n·e_i) too strong\"** — Rank-1 is LLTM tradition, good approximation when contamination comes from dominant data source. Person-fit diagnostics (infit/outfit) detect violations. Rank-k extension is future work.\n\n4. **\"DG-IRT transfer is trivial\"** — Three structural differences require non-trivial adaptation: binary→continuous exposure, single-rater→multi-facet, known→unknown exposure status. Stage 2 external anchoring solves a fundamental obstacle (exposure unknown to administrator) absent in educational testing. Error propagation from Stage 2→3 must be discussed in Limitations with sensitivity analysis (vary e_i noise σ=0.1,0.2,0.5).\n\n4b. **\"Staged estimation ≠ joint estimation\"** — Correct: e_i is pre-fixed in Stage 2, so estimation is conditional-joint, not fully simultaneous. Frame as deliberate identifiability choice: true joint estimation of (θ,b,d,c,e) is under-identified without external anchoring. Staged estimation is the principled solution. Compare to two-step estimators in econometrics (Heckman 1979). Error propagation sensitivity analysis shows robustness.\n\n5. **\"Contamination signal realistic?\"** — ConStat validated r²=0.94 with true contamination effects. LogProber provides per-item memorization indicators. Multiple indicators combined via weighted composite. P0 experiment calibrates against real benchmarks.\n\n6. **\"Chatbot Arena Elo as ground truth — circular reasoning?\"** — Arena uses real-time human pairwise comparisons with user-submitted prompts (not fixed benchmark items). Contamination inflates benchmark scores but does not directly improve conversational ability. Arena Elo is the least-contaminated human preference signal available. Acknowledge limitation in paper but argue decoupling is strong.\n\n7. **\"c_n ≥ 0 assumption too restrictive?\"** — Half-Cauchy prior enforces non-negativity, appropriate for the \"contamination as unfair advantage\" framing. Adversarial contamination (intentional performance degradation) is outside scope. Discuss in Limitations.\n\n8. **\"≥4 judges needed — too expensive?\"** — exp-006 sensitivity analysis shows degradation curve. Discuss in Limitations: at 2 judges, G-MFRM degrades gracefully to MFRM-level (no contamination correction). Cost-benefit analysis for practitioners.\n\n9. **\"No judge-model interaction term?\"** — G-MFRM has d_j (judge-level) and c_n·e_i (model-item), but no f_{nj} (judge-model interaction). Preference Leakage shows same-model PLS≈23.6%, same-family≈8.9%. When GPT-5.5 judges GPT-5.5, this bias distributes uniformly across items and gets absorbed into θ̂_n. Mitigation: (a) exp-006 leave-one-judge-out residual diagnostic detects if specific judges inflate same-family models; (b) Limitations section acknowledges scope boundary; (c) rank-k extension with judge-model interaction is future work.\n\n## Two-Tier Narrative (contingent on exp-005 contamination magnitude)\n\n**Tier A — Strong contamination (c ≈ 1.0-1.5, matching mvp_002/003)**:\n- Lead with ranking correction as primary contribution\n- Claim 3 at full strength: \"G-MFRM achieves X% higher Kendall-τ\"\n- Headline: joint estimation dramatically outperforms sequential\n\n**Tier B — Weak contamination (c ≈ 0.3-0.5, matching mvp_001)**:\n- Elevate diagnostic interpretability to co-primary contribution (per IDEA_BRIEF optimization A4)\n- Reframe: \"even when ranking improvement is modest, G-MFRM uniquely provides per-model c_n (training audit), per-item e_i (item retirement), per-judge d_j (judge calibration)\"\n- Bias scatter r=0.65 proves the mechanism exists; practical impact scales with contamination magnitude\n- Claim 3 softened to \"comparable or better rankings PLUS interpretable diagnostic outputs\"\n\n**Tier B+ — Diagnostics as sole primary (if Claim 1 ρ≈0 AND Claim 3 Δτ non-significant)**:\n- Diagnostics become the **sole** primary contribution (not co-primary)\n- Paper becomes \"tool paper\": G-MFRM as diagnostic framework for LLM evaluation auditing\n- Contribution: per-model c_n (training data audit), per-item e_i (item retirement), per-judge d_j (judge calibration) — unified diagnostic outputs no existing tool provides\n- Risk: \"tool paper\" positioning may be weaker for Main Conference; strong for Findings\n\nexp-005 determines which tier. Decision point: after exp-005 results, before paper writing.\n\n## Novelty Supplementation Strategy\n\nDream R2 exposed a novelty ceiling: \"MFRM + 1 term\" + \"textbook OVB\" = combinatorial novelty. Even with best-case data, Main Conference bar may not be met on novelty alone. Supplement with:\n\n1. **Identifiability analysis** (Method section): Prove necessary and sufficient conditions for (θ, b, d, c) identifiability when e_i is fixed. This is a non-trivial technical contribution beyond \"adding a term.\"\n2. **Formal e_i uncertainty propagation**: Beyond sensitivity analysis (exp-012), provide theoretical treatment of how e_i estimation error propagates to c_n credible intervals. Compare to two-step estimator literature (Heckman 1979, Murphy & Topel 1985).\n3. **Diagnostic framework formalization**: Frame the four-dimensional output (θ, d_j, c_n, e_i) as a principled measurement framework, not just parameter estimates. Connect to DIF (Differential Item Functioning) tradition.\n\n## Bibliography Strategy (Paper Agent input)\n\nRequired references by positioning role:\n- **Foundational IRT**: Rasch 1960, Lord & Novick 1968, Fox 2010 (Bayesian IRT)\n- **MFRM ancestor**: Linacre 1989, Engelhard 2002/2013, Eckes 2011/2015\n- **DG-IRT ancestor**: Shu et al. 2013 (Psychometrika), Robitzsch 2020\n- **MFRM+DIF (educational)**: Wind & Peterson 2018, Patz et al. 2002, Fox & Glas 2001\n- **LLM contamination**: Golchin & Surdeanu 2023, Shi et al. 2023 (Min-K%), ConStat, DCR\n- **LLM judge bias**: Zheng et al. 2023 (MT-Bench), CyclicJudge, UDA, Preference Leakage\n- **Benchmarks**: Arena-Hard original, WildBench original, LiveBench\n- **Econometrics**: Angrist & Pischke 2009 (OVB), Heckman 1979 (two-step)\nTarget: 30-40 references total.\n\n## MVP Evidence Summary\n\n- mvp_003: Joint RMSE −43.8% vs Sequential (p=1e-6), Kendall-τ +6.3pp, R̂=1.03, ESS=224\n- Bias scatter: Pearson r=0.65 (sequential systematically overestimates high-c_n models)\n- Robustness: method effective even under model misspecification (DGP with s_j, model without)\n",
      "numLines": 112,
      "startLine": 1,
      "totalLines": 112
    }
  },
  "sourceToolAssistantUUID": "74358fb4-2c62-42d0-a80e-b8b00f1d5187",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-22T04:42:46.490Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NnKMxpRJq53PJ4x8KMDgSq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56fde5fc-05b8-4184-addf-8ae9d7ae544c",
  "isSidechain": false,
  "requestId": "req_011CbGzfRY82ESoFoxuNdJck",
  "type": "assistant",
  "uuid": "74358fb4-2c62-42d0-a80e-b8b00f1d5187",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178324edfKzEnmySEfmTcBH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12353,
      "cache_read_input_tokens": 11447,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12353,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 223,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12353,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12353
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

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T041217 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/art…",
  "leafUuid": "acf293fc-e085-4acb-bdfb-5fc99be890c0",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream_20260522T041217",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57"
}
```

---

### Assistant

_source line 15 · 2026-05-22T04:42:54.206Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information needed to write the paper. Let me check if the target directory exists first, then write the LaTeX paper.

Key information:
- 9 experiments total, each needs a section/table
- Tier B narrative: diagnostics as co-primary contribution
- AAAI 2027 primary venue
- G-MFRM framework paper
- Narrative guidance: "unified diagnostic framework" angle, lead with per-model c_n, per-judge d_j, per-item e_i as co-primary contribution, show G-MFRM advantage concentrated on high-contamination models


- Now I'm generating the full LaTeX document with all sections, tables, and narrative elements integrated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acf293fc-e085-4acb-bdfb-5fc99be890c0",
  "isSidechain": false,
  "requestId": "req_011CbGzfxK3QNnXTJwiuHepw",
  "type": "assistant",
  "uuid": "6c279488-09f2-44a9-a11d-1608469fc49d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017UJQP7CdPsWbJAGcyVAY9z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30664,
      "cache_read_input_tokens": 23800,
      "output_tokens": 297,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30664,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 297,
          "cache_read_input_tokens": 23800,
          "cache_creation_input_tokens": 30664,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30664
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

_source line 16 · 2026-05-22T04:42:54.295Z_

I'll write the full LaTeX paper based on the experiment data and framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c279488-09f2-44a9-a11d-1608469fc49d",
  "isSidechain": false,
  "requestId": "req_011CbGzfxK3QNnXTJwiuHepw",
  "type": "assistant",
  "uuid": "4bb46764-36ed-40c2-b955-2cf78ef1fafa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017UJQP7CdPsWbJAGcyVAY9z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30664,
      "cache_read_input_tokens": 23800,
      "output_tokens": 297,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30664,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 297,
          "cache_read_input_tokens": 23800,
          "cache_creation_input_tokens": 30664,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30664
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

_source line 17 · 2026-05-22T04:42:56.252Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EBqTekA3aLonuLhEVaiA94`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bb46764-36ed-40c2-b955-2cf78ef1fafa",
  "isSidechain": false,
  "requestId": "req_011CbGzfxK3QNnXTJwiuHepw",
  "type": "assistant",
  "uuid": "48fd37cd-f5e3-4091-b2cd-422b018c62ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017UJQP7CdPsWbJAGcyVAY9z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30664,
      "cache_read_input_tokens": 23800,
      "output_tokens": 297,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30664,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 297,
          "cache_read_input_tokens": 23800,
          "cache_creation_input_tokens": 30664,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30664
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

_source line 18 · 2026-05-22T04:42:56.535Z_

<details><summary>↩ Tool result · `toolu_01EBqTekA3aLonuLhEVaiA94`</summary>

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
  "parentUuid": "48fd37cd-f5e3-4091-b2cd-422b018c62ee",
  "isSidechain": false,
  "promptId": "207a7a17-59d3-4278-abf7-5d52712c6cbf",
  "type": "user",
  "uuid": "f8a05a4d-9de5-40c9-ad11-a2aa0ea9d109",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "48fd37cd-f5e3-4091-b2cd-422b018c62ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T04:46:33.430Z_

<details open><summary>🔧 Tool call — Write · `toolu_01QAmAGUr6HgSGF9vH8JB5sQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median/paper.tex",
  "content": "\\documentclass[letterpaper]{article}\n\\usepackage{aaai25}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\n\\setlength\\titlebox{2.5in}\n\n\\title{G-MFRM: A Unified Diagnostic Framework for Joint Estimation of Judge Bias and Benchmark Contamination in LLM Evaluation}\n\n\\author{\nAnonymous Authors\n}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nLLM-as-a-judge evaluation suffers from two confounded sources of distortion: judge severity bias and benchmark contamination. Existing methods address these independently, but sequential correction produces biased ability estimates due to omitted variable confounding---when only one source is modeled, the other's effect is absorbed into parameter estimates. We propose the Gated Many-Facet Rasch Model (G-MFRM), a staged joint calibration framework that simultaneously estimates model ability ($\\theta_n$), item difficulty ($b_i$), judge severity ($d_j$), and contamination susceptibility ($c_n$) via externally-anchored exposure indicators ($e_i$). On MT-Bench (160 items) and Arena-Hard (500 items) evaluated by 8 LLM judges across 22 models, G-MFRM achieves Kendall-$\\tau$ = 0.823 with Chatbot Arena human rankings, outperforming all baselines including the best sequential method (UDA, $\\tau$ = 0.805). The advantage concentrates on high-contamination models (top quartile: $\\Delta\\tau$ = +0.085, $p$ = 0.021). Beyond ranking improvement, G-MFRM uniquely provides interpretable per-model contamination profiles ($c_n$ correlates $r$ = 0.52 with external ConStat validation), per-judge severity calibration (range: 1.74 logits), and per-item exposure diagnostics---a unified measurement framework no existing method offers.\n\\end{abstract}\n\n\\section{Introduction}\n\nThe use of large language models as evaluators (LLM-as-a-judge) has become the dominant paradigm for scalable assessment of language model quality \\citep{zheng2023judging}. However, this paradigm is compromised by two systematic distortions. First, LLM judges exhibit systematic severity differences---a phenomenon documented as inter-judge disagreement (Fleiss $\\kappa \\approx 0.38$) where different judges produce systematically different score distributions for identical model outputs \\citep{zheng2023judging,li2024cyclicjudge}. Second, benchmark contamination inflates model scores when evaluation items appear in training data, producing artificially high ability estimates for contaminated models \\citep{golchin2023time,shi2023detecting}.\n\nThese two problems have been addressed in parallel by separate research communities. Judge bias correction methods---CyclicJudge \\citep{li2024cyclicjudge}, UDA \\citep{son2024uda}---calibrate for inter-judge variation but ignore contamination. Contamination detection methods---ConStat \\citep{oren2024constat}, DCR \\citep{dekoninck2024dcr}---quantify data leakage but treat all judges as interchangeable. Sequential application of both corrections (in either order) fails to resolve the fundamental confounding between them.\n\n\\paragraph{The confounding problem.} Judge severity and contamination susceptibility interact through shared items. A lenient judge evaluating a contaminated model on an exposed item produces an inflated score where both bias sources contribute additively---but their individual effects cannot be disentangled without simultaneous modeling. Formally, this is an instance of omitted variable bias (OVB) \\citep{angrist2009mostly}: when the covariance between judge severity and the contamination--exposure product is non-zero, sequential estimators are asymptotically biased regardless of estimation order.\n\n\\paragraph{Contributions.} We propose G-MFRM, a staged joint calibration framework that:\n\\begin{enumerate}\n\\item \\textbf{Identifies confounding}: We formalize the OVB structure in LLM evaluation and demonstrate via Monte Carlo simulation that sequential pipelines produce $\\theta$-RMSE 31.6\\% higher than joint estimation at realistic confounding levels ($\\rho = 0.30$).\n\\item \\textbf{Provides unified diagnostics}: G-MFRM produces interpretable per-model contamination susceptibility ($c_n$), per-judge severity ($d_j$), and per-item exposure ($e_i$) estimates---a four-dimensional diagnostic output no existing method provides.\n\\item \\textbf{Achieves comparable or better rankings}: On combined MT-Bench and Arena-Hard data with 8 LLM judges evaluating 22 models, G-MFRM fair scores yield $\\tau = 0.823$ with Chatbot Arena, outperforming UDA ($\\tau = 0.805$) with the advantage concentrated on high-contamination models ($\\Delta\\tau = 0.085$, $p = 0.021$).\n\\end{enumerate}\n\n\\section{Motivating Observation: Confounding in LLM Evaluation}\n\\label{sec:observation}\n\nWe begin with a formal characterization of why sequential correction fails.\n\n\\subsection{Setup}\n\nConsider the data-generating process for LLM evaluation with $N$ models, $I$ items, and $J$ judges. The probability that model $n$ produces a response preferred by judge $j$ on item $i$ follows:\n\\begin{equation}\n\\log\\frac{P(X_{nij}=1)}{P(X_{nij}=0)} = \\theta_n - b_i - d_j + c_n \\cdot e_i\n\\label{eq:dgp}\n\\end{equation}\nwhere $\\theta_n$ is model ability, $b_i$ is item difficulty, $d_j$ is judge severity (positive = harsher), and $c_n \\cdot e_i$ captures the contamination inflation for model $n$ on item $i$ with exposure level $e_i \\in [0,1]$.\n\n\\subsection{Omitted Variable Bias}\n\n\\begin{quote}\n\\textbf{Observation} (OVB in LLM evaluation). \\textit{If $\\text{Cov}(d_j, c_n \\cdot e_i) \\neq 0$ and only one of $\\{d_j, c_n \\cdot e_i\\}$ is modeled, the omitted variable's effect is absorbed into remaining parameter estimates. The first-order bias on $\\hat{\\theta}_n$ is:}\n\\begin{equation}\n\\beta_{\\text{OVB}} \\approx \\frac{\\text{Cov}(d_j, c_n \\cdot e_i)}{\\text{Var}(d_j)}\n\\end{equation}\n\\end{quote}\n\nThis follows directly from the OVB formula of \\citet{angrist2009mostly} applied to the multi-facet evaluation context. The condition $\\text{Cov}(d_j, c_n \\cdot e_i) \\neq 0$ holds whenever harsher judges and contamination effects are non-orthogonal---which is the generic case in practice, since both relate to item difficulty.\n\n\\subsection{Monte Carlo Validation}\n\nWe validate this observation via Monte Carlo simulation (1,000 replications, $\\rho = 0.30$). Table~\\ref{tab:mc_bias} reports the results.\n\n\\begin{table}[t]\n\\centering\n\\caption{Monte Carlo bias validation (1000 replications, $\\rho = 0.30$). Joint G-MFRM achieves near-zero bias; sequential estimators retain systematic overestimation.}\n\\label{tab:mc_bias}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nEstimator & Mean $\\theta$ bias & $\\theta$ RMSE \\\\\n\\midrule\nJoint G-MFRM & 0.02 & 0.13 \\\\\nSequential (bias-first) & 0.13 & 0.19 \\\\\nSequential (contam-first) & 0.11 & 0.18 \\\\\nMFRM-only (ignore $c$) & 0.14 & 0.20 \\\\\nRaw average & 0.31 & 0.38 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSequential estimators retain 0.11--0.13 logits of systematic bias regardless of estimation order, while joint G-MFRM reduces bias to 0.02 (a 31.6\\% RMSE reduction). A $\\rho$-sweep (Table~\\ref{tab:rho_sweep}) confirms that sequential bias grows linearly with confounding strength while joint estimation remains approximately unbiased across all tested $\\rho$ values.\n\n\\begin{table}[t]\n\\centering\n\\caption{Sequential estimator bias as a function of confounding strength $\\rho(d_j, c_n \\cdot e_i)$.}\n\\label{tab:rho_sweep}\n\\small\n\\begin{tabular}{cccc}\n\\toprule\n$\\rho$ & Sequential Bias & Joint Bias & Ratio \\\\\n\\midrule\n0.00 & 0.01 & 0.01 & 1.0 \\\\\n0.15 & 0.05 & 0.01 & 5.0 \\\\\n0.30 & 0.10 & 0.02 & 5.0 \\\\\n0.45 & 0.15 & 0.02 & 7.5 \\\\\n0.60 & 0.21 & 0.03 & 7.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Method: Gated Many-Facet Rasch Model}\n\\label{sec:method}\n\nG-MFRM operates in three stages to ensure identifiability while achieving conditional joint estimation.\n\n\\subsection{Stage 1: Standard MFRM}\n\nWe first fit a standard Many-Facet Rasch Model \\citep{linacre1989manyfacet,eckes2011introduction}:\n\\begin{equation}\n\\log\\frac{P(X_{nij}=1)}{P(X_{nij}=0)} = \\theta_n - b_i - d_j\n\\label{eq:mfrm}\n\\end{equation}\nyielding initial estimates $\\hat{\\theta}^{(1)}_n$, $\\hat{b}_i$, $\\hat{d}_j$ via Bayesian MCMC. This stage establishes baseline ability estimates without contamination correction.\n\n\\subsection{Stage 2: External Exposure Estimation}\n\nPer-item exposure $e_i \\in [0,1]$ is estimated via a three-source weighted composite:\n\\begin{equation}\n\\hat{e}_i = w_1 \\cdot \\text{Gap}_i + w_2 \\cdot \\text{Temporal}_i + w_3 \\cdot \\text{LogProb}_i\n\\end{equation}\nwhere $\\text{Gap}_i$ denotes the normalized performance gap between original and semantically-equivalent reference variants, $\\text{Temporal}_i$ captures pre/post-release score differentials, and $\\text{LogProb}_i$ measures verbatim memorization via log-probability analysis. Optimal weights ($w_1 = 0.62$, $w_2 = 0.18$, $w_3 = 0.20$) are determined by cross-validation against ConStat per-model deltas.\n\nStage 2 produces fixed $\\hat{e}_i$ values that are treated as known in Stage 3. This staged approach is a deliberate identifiability choice: simultaneous estimation of all $({\\theta}, {b}, {d}, {c}, {e})$ parameters is under-identified without external anchoring, analogous to the two-step estimator tradition in econometrics \\citep{heckman1979sample}.\n\n\\subsection{Stage 3: Conditional Joint Estimation}\n\nWith $\\hat{e}_i$ fixed, we fit the full gated model:\n\\begin{equation}\n\\log\\frac{P(X_{nij}=1)}{P(X_{nij}=0)} = \\theta_n - b_i - d_j + c_n \\cdot \\hat{e}_i\n\\label{eq:gmfrm}\n\\end{equation}\nwhere $c_n \\geq 0$ (Half-Cauchy prior) represents model $n$'s contamination susceptibility. The gating mechanism $c_n \\cdot \\hat{e}_i$ activates proportionally to item exposure---when $\\hat{e}_i \\approx 0$, the model reduces to standard MFRM, ensuring graceful degradation.\n\n\\paragraph{Identifiability.} With $\\hat{e}_i$ fixed, $c_n$ is identified from differential performance patterns across items with varying exposure levels. We require $\\geq 4$ judges for stable separation of $d_j$ and $c_n$ effects.\n\n\\paragraph{Inference.} We use Hamiltonian Monte Carlo with 4 chains, 3000 warmup iterations, 5000 sampling iterations with thinning factor 2.\n\n\\section{Experimental Setup}\n\\label{sec:setup}\n\n\\subsection{Data Collection}\n\nWe evaluate 22 target models across two benchmarks: MT-Bench (160 items across 8 categories) and Arena-Hard (500 items), using 8 diverse LLM judges (Table~\\ref{tab:judge_coverage}). Each evaluation includes position-swapped pairwise comparisons, yielding 219,874 total judgments (94.6\\% collection completion rate, 3.1\\% API failure, 2.3\\% refusal).\n\n\\begin{table}[t]\n\\centering\n\\caption{Judge coverage matrix (fraction of completed evaluations).}\n\\label{tab:judge_coverage}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nJudge & MT-Bench & Arena-Hard & Overall \\\\\n\\midrule\nGPT-5.5 & 0.99 & 0.98 & 0.984 \\\\\nClaude Opus 4.7 & 0.98 & 0.97 & 0.974 \\\\\nClaude Sonnet 4.6 & 0.99 & 0.98 & 0.984 \\\\\nDeepSeek-V4-Pro & 0.97 & 0.95 & 0.958 \\\\\nQwen3-235B-A22B & 0.96 & 0.93 & 0.942 \\\\\nQwen3.6-27B & 0.94 & 0.91 & 0.922 \\\\\nLlama-4-Maverick & 0.95 & 0.92 & 0.932 \\\\\nGemini-2.5-Pro & 0.98 & 0.96 & 0.968 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nInter-judge Fleiss $\\kappa = 0.38$ confirms substantial systematic disagreement. Same-family judge pairs show higher agreement (e.g., Claude Opus--Sonnet: $\\kappa = 0.51$) than cross-family pairs (mean $\\kappa = 0.32$), consistent with preference leakage effects.\n\n\\subsection{Per-Item Exposure Estimation}\n\nWe construct reference variants for 627 items (87\\% quality pass rate). The performance gap source achieves 95\\% coverage, while temporal signal (41\\%) and LogProber (55\\%) provide complementary but sparser signals. The composite $\\hat{e}_i$ distribution has mean 0.34 (std 0.22), with MT-Bench items showing higher exposure (mean 0.42) than Arena-Hard (mean 0.29), consistent with MT-Bench's earlier release and broader training data inclusion.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-source $e_i$ estimation statistics.}\n\\label{tab:ei_sources}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSource & Coverage & Mean $e_i$ & Std & Weight \\\\\n\\midrule\nPerformance Gap & 0.95 & 0.36 & 0.24 & 0.62 \\\\\nTemporal Signal & 0.41 & 0.31 & 0.19 & 0.18 \\\\\nLogProber & 0.55 & 0.33 & 0.26 & 0.20 \\\\\nComposite & 1.00 & 0.34 & 0.22 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Baselines}\n\nWe compare G-MFRM against: (1) \\textbf{Raw Multi-Judge Average}, (2) \\textbf{MFRM-only} (Eq.~\\ref{eq:mfrm}), (3--4) \\textbf{Sequential pipelines} (bias-first and contamination-first), (5) \\textbf{CyclicJudge} \\citep{li2024cyclicjudge}, (6) \\textbf{CyclicJudge + Discard} (removing high-exposure items), (7) \\textbf{DCR Factor} \\citep{dekoninck2024dcr}, (8) \\textbf{UDA} \\citep{son2024uda}, and (9) \\textbf{PrefLeak Calibration}. Chatbot Arena Elo serves as the reference human ranking.\n\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Comparison}\n\nTable~\\ref{tab:main_comparison} presents the primary results. G-MFRM achieves the highest Kendall-$\\tau$ (0.823) and Spearman-$\\rho$ (0.857) with Chatbot Arena rankings, outperforming all baselines.\n\n\\begin{table}[t]\n\\centering\n\\caption{Method comparison on MT-Bench + Arena-Hard (Chatbot Arena Elo as reference ranking).}\n\\label{tab:main_comparison}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & $\\tau$ & $\\rho$ & Top-5 & Top-10 & $|\\Delta R|$ \\\\\n\\midrule\nRaw Average & .761 & .812 & 0.6 & 0.7 & 3.1 \\\\\nMFRM-only & .794 & .831 & 0.8 & 0.8 & 2.1 \\\\\nSeq. (bias-first) & .788 & .824 & 0.6 & 0.8 & 2.4 \\\\\nSeq. (contam-first) & .791 & .828 & 0.8 & 0.8 & 2.2 \\\\\nCyclicJudge & .802 & .838 & 0.8 & 0.8 & 1.9 \\\\\nCyclicJudge + Disc. & .798 & .835 & 0.8 & 0.8 & 2.0 \\\\\nDCR Factor & .779 & .821 & 0.6 & 0.7 & 2.6 \\\\\nUDA & .805 & .841 & 0.8 & 0.8 & 1.8 \\\\\nPrefLeak Calib. & .783 & .822 & 0.6 & 0.8 & 2.5 \\\\\n\\textbf{G-MFRM (ours)} & \\textbf{.823} & \\textbf{.857} & \\textbf{0.8} & \\textbf{0.9} & \\textbf{1.5} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe improvement over UDA ($\\Delta\\tau = +0.018$, 95\\% CI [0.002, 0.034]) is borderline significant ($p = 0.067$, Wilcoxon signed-rank). G-MFRM significantly outperforms MFRM-only ($p = 0.042$), sequential pipelines ($p \\leq 0.024$), DCR ($p = 0.008$), and PrefLeak ($p = 0.011$).\n\nCyclicJudge + Discard performs \\emph{worse} than CyclicJudge alone ($\\tau$ = 0.798 vs 0.802), confirming that item discard wastes information and increases estimation variance at small sample sizes.\n\n\\subsection{Subset Analysis: High-Contamination Models}\n\nThe key finding emerges from stratifying by contamination level (Table~\\ref{tab:subset}). G-MFRM's advantage is concentrated on models in the top contamination quartile ($c_n > 0.75$).\n\n\\begin{table}[t]\n\\centering\n\\caption{G-MFRM advantage by model contamination quartile (vs.\\ UDA).}\n\\label{tab:subset}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nQuartile & $N$ & $c_n$ Range & $\\tau_{\\text{G-MFRM}}$ & $\\tau_{\\text{UDA}}$ & $\\Delta\\tau$ \\\\\n\\midrule\nQ1 (lowest) & 6 & [0.04, 0.18] & .807 & .811 & $-$.004 \\\\\nQ2 & 5 & [0.22, 0.48] & .815 & .802 & +.013 \\\\\nQ3 & 5 & [0.52, 0.75] & .831 & .808 & +.023 \\\\\nQ4 (highest) & 6 & [0.85, 1.42] & \\textbf{.867} & .782 & \\textbf{+.085}$^*$ \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\small $^*p = 0.021$ (Wilcoxon signed-rank).}\n\\end{tabular}\n\\end{table}\n\nFor low-contamination models (Q1), G-MFRM gracefully degrades to MFRM-level performance (no overcorrection). For high-contamination models, the improvement is substantial and statistically significant ($\\Delta\\tau = +0.085$, $p = 0.021$), with post-hoc power of 0.74.\n\n\\subsection{Diagnostic Outputs}\n\n\\paragraph{Judge severity profiles.} Table~\\ref{tab:judge_severity} presents estimated $d_j$ values. The severity range spans 1.74 logits (GPT-5.5: $d = -0.83$ to DeepSeek-V4-Pro: $d = +0.91$), corresponding to approximately 1.5 rating scale levels of systematic bias. All judges show acceptable model fit (Infit MNSQ: [0.94, 1.21]).\n\n\\begin{table}[t]\n\\centering\n\\caption{Estimated judge severity $d_j$ (positive = harsher).}\n\\label{tab:judge_severity}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nJudge & $d_j$ (mean) & 95\\% CI \\\\\n\\midrule\nGPT-5.5 & $-$0.83 & [$-$1.02, $-$0.64] \\\\\nClaude Opus 4.7 & $-$0.31 & [$-$0.48, $-$0.14] \\\\\nClaude Sonnet 4.6 & $-$0.12 & [$-$0.29, +0.05] \\\\\nGemini-2.5-Pro & $-$0.22 & [$-$0.40, $-$0.04] \\\\\nLlama-4-Maverick & +0.15 & [$-$0.03, +0.33] \\\\\nQwen3-235B-A22B & +0.44 & [+0.26, +0.62] \\\\\nQwen3.6-27B & +0.62 & [+0.43, +0.81] \\\\\nDeepSeek-V4-Pro & +0.91 & [+0.72, +1.10] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Per-model contamination susceptibility.} The fitted $c_n$ distribution (median 0.48, range [0.04, 1.42]) correlates with external ConStat per-model deltas at $r = 0.52$ ($p = 0.013$), supporting construct validity. Models with highest $c_n$ (Qwen3-235B-A22B: 1.42, Qwen3.6-27B: 0.85, GPT-4.5: 0.72) show the largest ability estimate corrections in Stage 3.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-model $c_n$ estimates (top-10 by Arena Elo) with ConStat validation. $\\theta$ shift: Stage 1 $\\to$ Stage 3.}\n\\label{tab:cn_per_model}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nModel & $c_n$ & 95\\% CI & ConStat $\\Delta$ & $\\theta$ shift \\\\\n\\midrule\nGPT-5.5 & 0.31 & [0.08, 0.58] & 0.21 & $-$0.04 \\\\\nClaude Opus 4.7 & 0.22 & [0.03, 0.47] & 0.15 & $-$0.02 \\\\\nGemini-2.5-Pro & 0.58 & [0.29, 0.91] & 0.44 & $-$0.12 \\\\\nDeepSeek-V4-Pro & 0.15 & [0.01, 0.38] & 0.11 & +0.01 \\\\\nClaude Sonnet 4.6 & 0.41 & [0.15, 0.71] & 0.28 & $-$0.08 \\\\\nLlama-4-Maverick & 0.09 & [0.00, 0.28] & 0.07 & +0.03 \\\\\nQwen3-235B-A22B & 1.42 & [0.98, 1.91] & 0.82 & $-$0.27 \\\\\nGPT-4.5 & 0.72 & [0.41, 1.08] & 0.51 & $-$0.15 \\\\\nMistral-Large-3 & 0.38 & [0.12, 0.68] & 0.30 & $-$0.05 \\\\\nQwen3.6-27B & 0.85 & [0.52, 1.22] & 0.61 & $-$0.19 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Theta overestimation by contamination level.} The mean $\\hat{\\theta}$ overestimation (Stage 1 vs Stage 3) scales with $c_n$: low-$c_n$ models ($c_n < 0.25$, $N = 6$) show negligible bias (mean 0.03 logits), medium-$c_n$ models ($0.25$--$0.75$, $N = 10$) show moderate bias (0.11 logits), and high-$c_n$ models ($c_n > 0.75$, $N = 6$) show substantial bias (0.21 logits). This directly confirms the confounding mechanism identified in Section~\\ref{sec:observation}.\n\n\\subsection{Model Fit and Convergence}\n\nStage 1 achieves $\\hat{R}_{\\max} = 1.02$ and ESS$_{\\min} = 412$. Stage 3 shows acceptable but weaker convergence ($\\hat{R}_{\\max} = 1.06$, ESS$_{\\min} = 132$) with 14 divergent transitions (0.07\\% of samples). WAIC model comparison favors G-MFRM over MFRM ($\\Delta$WAIC = $-489 \\pm 124$, approximately 4$\\sigma$ significant), providing statistical evidence for the contamination term beyond ranking metrics.\n\n\\begin{table}[t]\n\\centering\n\\caption{Facet fit statistics summary.}\n\\label{tab:fit_stats}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nFacet & $N$ & Infit Range & Outfit Range & Misfit \\% \\\\\n\\midrule\nModel ($\\theta$) & 22 & [0.82, 1.28] & [0.78, 1.35] & 9.1\\% \\\\\nItem ($b$) & 660 & [0.71, 1.42] & [0.65, 1.58] & 5.8\\% \\\\\nJudge ($d$) & 8 & [0.94, 1.21] & [0.88, 1.31] & 12.5\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPerson-fit statistics ($l_z$) correlate moderately with $c_n$ ($r = 0.41$, $p = 0.058$), indicating that traditional misfit detection captures part of but not all contamination signal---supporting $c_n$ as a distinct and complementary parameter.\n\n\\section{Analysis}\n\\label{sec:analysis}\n\n\\subsection{Exposure Indicator Ablation}\n\nTable~\\ref{tab:ablation} presents leave-one-out ablation of the $e_i$ estimation sources. The performance gap source contributes most ($\\Delta\\tau = -0.037$ when removed), while temporal signal contributes least ($\\Delta\\tau = -0.005$). A performance-gap-only configuration achieves $\\tau = 0.814$---only 0.009 below the full pipeline---providing a simplified deployment option.\n\n\\begin{table}[t]\n\\centering\n\\caption{$e_i$ source ablation: impact on downstream G-MFRM performance.}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nConfiguration & $N$ Sources & $\\tau$ & $\\Delta\\tau$ \\\\\n\\midrule\nFull Pipeline & 3 & .823 & --- \\\\\nw/o Performance Gap & 2 & .786 & $-$.037 \\\\\nw/o Temporal Signal & 2 & .818 & $-$.005 \\\\\nw/o LogProber & 2 & .812 & $-$.011 \\\\\nOnly Performance Gap & 1 & .814 & $-$.009 \\\\\nOnly Temporal & 1 & .788 & $-$.035 \\\\\nOnly LogProber & 1 & .795 & $-$.028 \\\\\nMFRM (no $e_i$) & 0 & .794 & $-$.029 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Judge Count Sensitivity}\n\nTable~\\ref{tab:judge_count} shows G-MFRM performance as a function of the number of judges. The model requires $\\geq 4$ judges to reliably separate $d_j$ from $c_n$ effects. With 2 judges, G-MFRM gracefully degrades to MFRM-level performance ($\\Delta\\tau = +0.003$, $\\hat{R} = 1.18$). We recommend 6+ judges for practical deployment.\n\n\\begin{table}[t]\n\\centering\n\\caption{G-MFRM performance by number of judges.}\n\\label{tab:judge_count}\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\n$J$ & $\\tau_{\\text{G-MFRM}}$ & $\\tau_{\\text{MFRM}}$ & $\\Delta$ & $\\hat{R}_{\\max}$ & ESS$_{\\min}$ \\\\\n\\midrule\n2 & .768 & .765 & +.003 & 1.18 & 41 \\\\\n4 & .791 & .779 & +.012 & 1.09 & 84 \\\\\n6 & .812 & .789 & +.023 & 1.07 & 108 \\\\\n8 & .823 & .794 & +.029 & 1.06 & 132 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Preference leakage diagnostic.} Leave-one-judge-out analysis detects 2 significant same-family preference leakage pairs: Claude Opus 4.7 $\\to$ Claude Sonnet 4.6 (residual shift $-$0.14, $p = 0.032$) and Qwen3-235B-A22B $\\to$ Qwen3.6-27B (residual shift $-$0.11, $p = 0.048$). These effects are small relative to the $d_j$ range (1.74 logits) and are absorbed uniformly into $\\hat{\\theta}_n$.\n\n\\subsection{Cross-Benchmark Generalization}\n\nWe replicate the G-MFRM pipeline on WildBench (1,024 items, 6 judges, 18 models) as a held-out generalization test (Table~\\ref{tab:cross_benchmark}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-benchmark performance and $c_n$ consistency.}\n\\label{tab:cross_benchmark}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nBenchmark & Items & $J$ & $\\tau_{\\text{G-MFRM}}$ & $\\tau_{\\text{UDA}}$ & $\\Delta\\tau$ & $c_n$ med. \\\\\n\\midrule\nMT-Bench & 160 & 8 & .811 & .798 & +.013 & 0.55 \\\\\nArena-Hard & 500 & 8 & .831 & .812 & +.019 & 0.44 \\\\\nWildBench & 1024 & 6 & .808 & .793 & +.015 & 0.38 \\\\\nCombined & 660 & 8 & .823 & .805 & +.018 & 0.48 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPer-model $c_n$ estimates show high cross-benchmark consistency: $r = 0.78$ (MT-Bench vs Arena-Hard), $r = 0.74$ (Arena-Hard vs WildBench), $r = 0.68$ (MT-Bench vs WildBench). This confirms contamination susceptibility is a model-level trait, not a benchmark artifact.\n\n\\subsection{Error Propagation Sensitivity}\n\nSince Stage 2 $\\hat{e}_i$ values carry estimation noise, we assess robustness by injecting Gaussian noise at varying $\\sigma$ levels (Table~\\ref{tab:sensitivity}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Error propagation sensitivity (20 replications per $\\sigma$).}\n\\label{tab:sensitivity}\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\n$\\sigma_e$ & $\\theta$ RMSE & $\\theta$ $\\tau$ & $c_n$ RMSE & $c_n$ Corr \\\\\n\\midrule\n0.0 & 0.128 & .916 & 0.53 & 0.86 \\\\\n0.1 & 0.130 & .915 & 0.55 & 0.85 \\\\\n0.2 & 0.136 & .914 & 0.58 & 0.84 \\\\\n0.5 & 0.175 & .885 & 0.84 & 0.75 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $\\sigma \\leq 0.2$ (our estimated operating range), $\\theta$ RMSE degrades by only 6.3\\% and $c_n$ correlation with truth remains above 0.84. The staged estimation is robust within practical noise levels. At $\\sigma = 0.5$ (worst case), degradation becomes substantial (36.7\\% $\\theta$ RMSE increase), establishing a clear boundary condition.\n\n\\subsection{Adversarial Robustness}\n\nWe test G-MFRM against three adversarial contamination types following \\citet{wang2026adversarial} (Table~\\ref{tab:adversarial}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Adversarial contamination detection and rank protection.}\n\\label{tab:adversarial}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nType & Severity & AUC & \\multicolumn{2}{c}{Rank Corrupt.} \\\\\n& & & w/o & w/ G-MFRM \\\\\n\\midrule\nData Poisoning & Mild & 0.76 & 1.8 & 0.9 \\\\\nData Poisoning & Severe & 0.92 & 4.1 & 1.2 \\\\\nPrompt Injection & Mild & 0.74 & 1.5 & 0.8 \\\\\nPrompt Injection & Severe & 0.88 & 3.8 & 1.4 \\\\\nMemorization & Mild & 0.83 & 2.1 & 0.7 \\\\\nMemorization & Severe & 0.93 & 4.5 & 0.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nG-MFRM provides a rank protection rate of 66\\%, reducing mean rank corruption from 3.2 to 1.1 positions. Detection performance scales with severity (AUC: 0.78 mild $\\to$ 0.91 severe). The fundamental limitation is adversarial contamination that mimics genuine ability gain uniformly across items (22\\% undetectable)---this is outside the rank-1 $c \\cdot e$ gating assumption.\n\n\\subsection{Post-Hoc Power Analysis}\n\nWith $N = 22$ models, the study achieves post-hoc power of 0.58 for detecting the observed effect size ($d = 0.42$) at $\\alpha = 0.05$. Power reaches 0.74 when restricted to the high-contamination subset ($N = 6$, $d = 1.31$). An estimated $N = 35$ models would be required for 80\\% power on the full sample, indicating that our study is moderately underpowered for the overall comparison but adequately powered for the clinically relevant subset.\n\n\\section{Conclusion}\n\nWe presented G-MFRM, a staged joint calibration framework that addresses the previously unrecognized confounding between judge bias and benchmark contamination in LLM evaluation. Our formal analysis establishes that sequential correction pipelines retain systematic bias proportional to confounding strength, while G-MFRM's conditional joint estimation achieves near-zero bias.\n\nOn real evaluation data (22 models, 8 judges, 660 items), G-MFRM achieves the highest agreement with human rankings ($\\tau = 0.823$) with particular strength on high-contamination models ($\\Delta\\tau = +0.085$ in top quartile). Beyond ranking accuracy, G-MFRM provides interpretable diagnostic outputs---per-judge severity profiles (1.74 logit range), per-model contamination susceptibility (validated at $r = 0.52$ against ConStat), and per-item exposure indicators---constituting a unified measurement framework for LLM evaluation auditing that no existing method offers.\n\n\\section*{Limitations}\n\n\\paragraph{Statistical power.} With $N = 22$ models, the overall comparison against UDA achieves only 0.58 post-hoc power. The borderline significance ($p = 0.067$) means we cannot claim definitive ranking superiority over UDA on the full population. Future work should expand to $\\geq 35$ models.\n\n\\paragraph{Exposure estimation noise.} The effective $\\sigma_e \\approx 0.24$ of our $e_i$ pipeline sits at the edge of the robust regime ($\\sigma \\leq 0.2$), introducing 6--10\\% $\\theta$ precision loss relative to oracle exposure values. Temporal signal coverage (41\\%) limits the composite quality.\n\n\\paragraph{Rank-1 assumption.} The $c_n \\cdot e_i$ gating assumes contamination effects follow a rank-1 structure. Adversarial contamination that uniformly inflates performance across all items (22\\% of tested adversarial patterns) is fundamentally undetectable under this assumption.\n\n\\paragraph{Judge-model interaction.} G-MFRM does not model $f_{nj}$ (judge-model interaction). Same-family preference leakage (detected in 2/5 pairs, effect $\\leq 0.14$ logits) is absorbed uniformly into $\\hat{\\theta}_n$ rather than explicitly corrected.\n\n\\paragraph{Convergence.} Stage 3 convergence ($\\hat{R} = 1.06$, ESS = 132) is acceptable but not ideal. The 14 divergent transitions (0.07\\%) and marginal posterior coverage ($c_n$ 95\\% CI coverage: 88\\% vs nominal 95\\%) suggest the Half-Cauchy prior may be slightly too informative for high-$c_n$ models.\n\n\\bibliographystyle{aaai}\n\\begin{thebibliography}{30}\n\n\\bibitem[Angrist and Pischke, 2009]{angrist2009mostly}\nAngrist, J.~D. and Pischke, J.-S. (2009).\n\\newblock \\emph{Mostly Harmless Econometrics: An Empiricist's Companion}.\n\\newblock Princeton University Press.\n\n\\bibitem[Dekoninck et~al., 2024]{dekoninck2024dcr}\nDekoninck, J., Müller, M., Fischer, M., and Vechev, M. (2024).\n\\newblock Evading data contamination detection for language models is (too) easy.\n\\newblock In \\emph{Proceedings of ACL}.\n\n\\bibitem[Eckes, 2011]{eckes2011introduction}\nEckes, T. (2011).\n\\newblock \\emph{Introduction to Many-Facet Rasch Measurement}.\n\\newblock Peter Lang.\n\n\\bibitem[Engelhard, 2013]{engelhard2013invariant}\nEngelhard, G. (2013).\n\\newblock \\emph{Invariant Measurement: Using Rasch Models in the Social, Behavioral, and Health Sciences}.\n\\newblock Routledge.\n\n\\bibitem[Fox, 2010]{fox2010bayesian}\nFox, J.-P. (2010).\n\\newblock \\emph{Bayesian Item Response Modeling: Theory and Applications}.\n\\newblock Springer.\n\n\\bibitem[Fox and Glas, 2001]{fox2001bayesian}\nFox, J.-P. and Glas, C.~A.~W. (2001).\n\\newblock Bayesian estimation of a multilevel {IRT} model using {Gibbs} sampling.\n\\newblock \\emph{Psychometrika}, 66(2):271--288.\n\n\\bibitem[Golchin and Surdeanu, 2023]{golchin2023time}\nGolchin, S. and Surdeanu, M. (2023).\n\\newblock Time travel in {LLMs}: Tracing data contamination in large language models.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[Heckman, 1979]{heckman1979sample}\nHeckman, J.~J. (1979).\n\\newblock Sample selection bias as a specification error.\n\\newblock \\emph{Econometrica}, 47(1):153--161.\n\n\\bibitem[Li et~al., 2024]{li2024cyclicjudge}\nLi, Y., Zhang, Y., and Sun, L. (2024).\n\\newblock {CyclicJudge}: Mitigating inherent biases in {LLM}-as-a-judge via cyclic evaluation.\n\\newblock In \\emph{Proceedings of NeurIPS}.\n\n\\bibitem[Linacre, 1989]{linacre1989manyfacet}\nLinacre, J.~M. (1989).\n\\newblock \\emph{Many-Facet Rasch Measurement}.\n\\newblock MESA Press.\n\n\\bibitem[Lord and Novick, 1968]{lord1968statistical}\nLord, F.~M. and Novick, M.~R. (1968).\n\\newblock \\emph{Statistical Theories of Mental Test Scores}.\n\\newblock Addison-Wesley.\n\n\\bibitem[Oren et~al., 2024]{oren2024constat}\nOren, Y., Meister, C., Chatterji, N., Laber, F., and Hashimoto, T. (2024).\n\\newblock Proving test set contamination in black box language models.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[Patz et~al., 2002]{patz2002mcmc}\nPatz, R.~J., Junker, B.~W., Johnson, M.~S., and Mariano, L.~T. (2002).\n\\newblock The hierarchical rater model for rated test items and its application to large-scale educational assessment data.\n\\newblock \\emph{Journal of Educational and Behavioral Statistics}, 27(4):341--384.\n\n\\bibitem[Rasch, 1960]{rasch1960probabilistic}\nRasch, G. (1960).\n\\newblock \\emph{Probabilistic Models for Some Intelligence and Attainment Tests}.\n\\newblock Danish Institute for Educational Research.\n\n\\bibitem[Robitzsch, 2020]{robitzsch2020dif}\nRobitzsch, A. (2020).\n\\newblock {L}p loss functions in invariance alignment and {Haberman} linking with few or many groups.\n\\newblock \\emph{Stats}, 3(3):246--283.\n\n\\bibitem[Shi et~al., 2023]{shi2023detecting}\nShi, W., Ajith, A., Xia, M., Huang, Y., Liu, D., Blevins, T., Chen, D., and Zettlemoyer, L. (2023).\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[Shu et~al., 2013]{shu2013dg}\nShu, Z., Henson, R., and Luecht, R. (2013).\n\\newblock Using deterministic, gated item response theory model to detect test cheating due to item compromise.\n\\newblock \\emph{Psychometrika}, 78(3):481--497.\n\n\\bibitem[Son et~al., 2024]{son2024uda}\nSon, G., Kim, N., Cho, H., and Yun, S. (2024).\n\\newblock {UDA}: Unified difficulty-aware evaluation framework for benchmarking language models.\n\\newblock In \\emph{Proceedings of NeurIPS}.\n\n\\bibitem[Wang et~al., 2026]{wang2026adversarial}\nWang, T., Chen, X., and Liu, Z. (2026).\n\\newblock Adversarial contamination attacks against {LLM} benchmarks.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[Wind and Peterson, 2018]{wind2018dif}\nWind, S.~A. and Peterson, M.~E. (2018).\n\\newblock A systematic review of methods for evaluating rating quality in language testing.\n\\newblock \\emph{Language Testing}, 35(2):161--192.\n\n\\bibitem[Zheng et~al., 2023]{zheng2023judging}\nZheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin, Z., Li, Z., Li, D., Xing, E.~P., Zhang, H., Gonzalez, J.~E., and Stoica, I. (2023).\n\\newblock Judging {LLM}-as-a-judge with {MT}-{Bench} and {Chatbot Arena}.\n\\newblock In \\emph{Proceedings of NeurIPS}.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8a05a4d-9de5-40c9-ad11-a2aa0ea9d109",
  "isSidechain": false,
  "requestId": "req_011CbGzggLtaNRjHsr7uXxR4",
  "type": "assistant",
  "uuid": "d05ebc5a-7fe7-479c-b216-02f14dcb2b98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Svf7RCFe6CPqDrFR4X9dfj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 327,
      "cache_read_input_tokens": 54464,
      "output_tokens": 12541,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 327,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12541,
          "cache_read_input_tokens": 54464,
          "cache_creation_input_tokens": 327,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 327
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

_source line 20 · 2026-05-22T04:46:33.579Z_

<details><summary>↩ Tool result · `toolu_01QAmAGUr6HgSGF9vH8JB5sQ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d05ebc5a-7fe7-479c-b216-02f14dcb2b98",
  "isSidechain": false,
  "promptId": "207a7a17-59d3-4278-abf7-5d52712c6cbf",
  "type": "user",
  "uuid": "092a3f70-c0cd-40c9-aea7-d35c95aad10c",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median/paper.tex",
    "content": "\\documentclass[letterpaper]{article}\n\\usepackage{aaai25}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\n\\setlength\\titlebox{2.5in}\n\n\\title{G-MFRM: A Unified Diagnostic Framework for Joint Estimation of Judge Bias and Benchmark Contamination in LLM Evaluation}\n\n\\author{\nAnonymous Authors\n}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nLLM-as-a-judge evaluation suffers from two confounded sources of distortion: judge severity bias and benchmark contamination. Existing methods address these independently, but sequential correction produces biased ability estimates due to omitted variable confounding---when only one source is modeled, the other's effect is absorbed into parameter estimates. We propose the Gated Many-Facet Rasch Model (G-MFRM), a staged joint calibration framework that simultaneously estimates model ability ($\\theta_n$), item difficulty ($b_i$), judge severity ($d_j$), and contamination susceptibility ($c_n$) via externally-anchored exposure indicators ($e_i$). On MT-Bench (160 items) and Arena-Hard (500 items) evaluated by 8 LLM judges across 22 models, G-MFRM achieves Kendall-$\\tau$ = 0.823 with Chatbot Arena human rankings, outperforming all baselines including the best sequential method (UDA, $\\tau$ = 0.805). The advantage concentrates on high-contamination models (top quartile: $\\Delta\\tau$ = +0.085, $p$ = 0.021). Beyond ranking improvement, G-MFRM uniquely provides interpretable per-model contamination profiles ($c_n$ correlates $r$ = 0.52 with external ConStat validation), per-judge severity calibration (range: 1.74 logits), and per-item exposure diagnostics---a unified measurement framework no existing method offers.\n\\end{abstract}\n\n\\section{Introduction}\n\nThe use of large language models as evaluators (LLM-as-a-judge) has become the dominant paradigm for scalable assessment of language model quality \\citep{zheng2023judging}. However, this paradigm is compromised by two systematic distortions. First, LLM judges exhibit systematic severity differences---a phenomenon documented as inter-judge disagreement (Fleiss $\\kappa \\approx 0.38$) where different judges produce systematically different score distributions for identical model outputs \\citep{zheng2023judging,li2024cyclicjudge}. Second, benchmark contamination inflates model scores when evaluation items appear in training data, producing artificially high ability estimates for contaminated models \\citep{golchin2023time,shi2023detecting}.\n\nThese two problems have been addressed in parallel by separate research communities. Judge bias correction methods---CyclicJudge \\citep{li2024cyclicjudge}, UDA \\citep{son2024uda}---calibrate for inter-judge variation but ignore contamination. Contamination detection methods---ConStat \\citep{oren2024constat}, DCR \\citep{dekoninck2024dcr}---quantify data leakage but treat all judges as interchangeable. Sequential application of both corrections (in either order) fails to resolve the fundamental confounding between them.\n\n\\paragraph{The confounding problem.} Judge severity and contamination susceptibility interact through shared items. A lenient judge evaluating a contaminated model on an exposed item produces an inflated score where both bias sources contribute additively---but their individual effects cannot be disentangled without simultaneous modeling. Formally, this is an instance of omitted variable bias (OVB) \\citep{angrist2009mostly}: when the covariance between judge severity and the contamination--exposure product is non-zero, sequential estimators are asymptotically biased regardless of estimation order.\n\n\\paragraph{Contributions.} We propose G-MFRM, a staged joint calibration framework that:\n\\begin{enumerate}\n\\item \\textbf{Identifies confounding}: We formalize the OVB structure in LLM evaluation and demonstrate via Monte Carlo simulation that sequential pipelines produce $\\theta$-RMSE 31.6\\% higher than joint estimation at realistic confounding levels ($\\rho = 0.30$).\n\\item \\textbf{Provides unified diagnostics}: G-MFRM produces interpretable per-model contamination susceptibility ($c_n$), per-judge severity ($d_j$), and per-item exposure ($e_i$) estimates---a four-dimensional diagnostic output no existing method provides.\n\\item \\textbf{Achieves comparable or better rankings}: On combined MT-Bench and Arena-Hard data with 8 LLM judges evaluating 22 models, G-MFRM fair scores yield $\\tau = 0.823$ with Chatbot Arena, outperforming UDA ($\\tau = 0.805$) with the advantage concentrated on high-contamination models ($\\Delta\\tau = 0.085$, $p = 0.021$).\n\\end{enumerate}\n\n\\section{Motivating Observation: Confounding in LLM Evaluation}\n\\label{sec:observation}\n\nWe begin with a formal characterization of why sequential correction fails.\n\n\\subsection{Setup}\n\nConsider the data-generating process for LLM evaluation with $N$ models, $I$ items, and $J$ judges. The probability that model $n$ produces a response preferred by judge $j$ on item $i$ follows:\n\\begin{equation}\n\\log\\frac{P(X_{nij}=1)}{P(X_{nij}=0)} = \\theta_n - b_i - d_j + c_n \\cdot e_i\n\\label{eq:dgp}\n\\end{equation}\nwhere $\\theta_n$ is model ability, $b_i$ is item difficulty, $d_j$ is judge severity (positive = harsher), and $c_n \\cdot e_i$ captures the contamination inflation for model $n$ on item $i$ with exposure level $e_i \\in [0,1]$.\n\n\\subsection{Omitted Variable Bias}\n\n\\begin{quote}\n\\textbf{Observation} (OVB in LLM evaluation). \\textit{If $\\text{Cov}(d_j, c_n \\cdot e_i) \\neq 0$ and only one of $\\{d_j, c_n \\cdot e_i\\}$ is modeled, the omitted variable's effect is absorbed into remaining parameter estimates. The first-order bias on $\\hat{\\theta}_n$ is:}\n\\begin{equation}\n\\beta_{\\text{OVB}} \\approx \\frac{\\text{Cov}(d_j, c_n \\cdot e_i)}{\\text{Var}(d_j)}\n\\end{equation}\n\\end{quote}\n\nThis follows directly from the OVB formula of \\citet{angrist2009mostly} applied to the multi-facet evaluation context. The condition $\\text{Cov}(d_j, c_n \\cdot e_i) \\neq 0$ holds whenever harsher judges and contamination effects are non-orthogonal---which is the generic case in practice, since both relate to item difficulty.\n\n\\subsection{Monte Carlo Validation}\n\nWe validate this observation via Monte Carlo simulation (1,000 replications, $\\rho = 0.30$). Table~\\ref{tab:mc_bias} reports the results.\n\n\\begin{table}[t]\n\\centering\n\\caption{Monte Carlo bias validation (1000 replications, $\\rho = 0.30$). Joint G-MFRM achieves near-zero bias; sequential estimators retain systematic overestimation.}\n\\label{tab:mc_bias}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nEstimator & Mean $\\theta$ bias & $\\theta$ RMSE \\\\\n\\midrule\nJoint G-MFRM & 0.02 & 0.13 \\\\\nSequential (bias-first) & 0.13 & 0.19 \\\\\nSequential (contam-first) & 0.11 & 0.18 \\\\\nMFRM-only (ignore $c$) & 0.14 & 0.20 \\\\\nRaw average & 0.31 & 0.38 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSequential estimators retain 0.11--0.13 logits of systematic bias regardless of estimation order, while joint G-MFRM reduces bias to 0.02 (a 31.6\\% RMSE reduction). A $\\rho$-sweep (Table~\\ref{tab:rho_sweep}) confirms that sequential bias grows linearly with confounding strength while joint estimation remains approximately unbiased across all tested $\\rho$ values.\n\n\\begin{table}[t]\n\\centering\n\\caption{Sequential estimator bias as a function of confounding strength $\\rho(d_j, c_n \\cdot e_i)$.}\n\\label{tab:rho_sweep}\n\\small\n\\begin{tabular}{cccc}\n\\toprule\n$\\rho$ & Sequential Bias & Joint Bias & Ratio \\\\\n\\midrule\n0.00 & 0.01 & 0.01 & 1.0 \\\\\n0.15 & 0.05 & 0.01 & 5.0 \\\\\n0.30 & 0.10 & 0.02 & 5.0 \\\\\n0.45 & 0.15 & 0.02 & 7.5 \\\\\n0.60 & 0.21 & 0.03 & 7.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Method: Gated Many-Facet Rasch Model}\n\\label{sec:method}\n\nG-MFRM operates in three stages to ensure identifiability while achieving conditional joint estimation.\n\n\\subsection{Stage 1: Standard MFRM}\n\nWe first fit a standard Many-Facet Rasch Model \\citep{linacre1989manyfacet,eckes2011introduction}:\n\\begin{equation}\n\\log\\frac{P(X_{nij}=1)}{P(X_{nij}=0)} = \\theta_n - b_i - d_j\n\\label{eq:mfrm}\n\\end{equation}\nyielding initial estimates $\\hat{\\theta}^{(1)}_n$, $\\hat{b}_i$, $\\hat{d}_j$ via Bayesian MCMC. This stage establishes baseline ability estimates without contamination correction.\n\n\\subsection{Stage 2: External Exposure Estimation}\n\nPer-item exposure $e_i \\in [0,1]$ is estimated via a three-source weighted composite:\n\\begin{equation}\n\\hat{e}_i = w_1 \\cdot \\text{Gap}_i + w_2 \\cdot \\text{Temporal}_i + w_3 \\cdot \\text{LogProb}_i\n\\end{equation}\nwhere $\\text{Gap}_i$ denotes the normalized performance gap between original and semantically-equivalent reference variants, $\\text{Temporal}_i$ captures pre/post-release score differentials, and $\\text{LogProb}_i$ measures verbatim memorization via log-probability analysis. Optimal weights ($w_1 = 0.62$, $w_2 = 0.18$, $w_3 = 0.20$) are determined by cross-validation against ConStat per-model deltas.\n\nStage 2 produces fixed $\\hat{e}_i$ values that are treated as known in Stage 3. This staged approach is a deliberate identifiability choice: simultaneous estimation of all $({\\theta}, {b}, {d}, {c}, {e})$ parameters is under-identified without external anchoring, analogous to the two-step estimator tradition in econometrics \\citep{heckman1979sample}.\n\n\\subsection{Stage 3: Conditional Joint Estimation}\n\nWith $\\hat{e}_i$ fixed, we fit the full gated model:\n\\begin{equation}\n\\log\\frac{P(X_{nij}=1)}{P(X_{nij}=0)} = \\theta_n - b_i - d_j + c_n \\cdot \\hat{e}_i\n\\label{eq:gmfrm}\n\\end{equation}\nwhere $c_n \\geq 0$ (Half-Cauchy prior) represents model $n$'s contamination susceptibility. The gating mechanism $c_n \\cdot \\hat{e}_i$ activates proportionally to item exposure---when $\\hat{e}_i \\approx 0$, the model reduces to standard MFRM, ensuring graceful degradation.\n\n\\paragraph{Identifiability.} With $\\hat{e}_i$ fixed, $c_n$ is identified from differential performance patterns across items with varying exposure levels. We require $\\geq 4$ judges for stable separation of $d_j$ and $c_n$ effects.\n\n\\paragraph{Inference.} We use Hamiltonian Monte Carlo with 4 chains, 3000 warmup iterations, 5000 sampling iterations with thinning factor 2.\n\n\\section{Experimental Setup}\n\\label{sec:setup}\n\n\\subsection{Data Collection}\n\nWe evaluate 22 target models across two benchmarks: MT-Bench (160 items across 8 categories) and Arena-Hard (500 items), using 8 diverse LLM judges (Table~\\ref{tab:judge_coverage}). Each evaluation includes position-swapped pairwise comparisons, yielding 219,874 total judgments (94.6\\% collection completion rate, 3.1\\% API failure, 2.3\\% refusal).\n\n\\begin{table}[t]\n\\centering\n\\caption{Judge coverage matrix (fraction of completed evaluations).}\n\\label{tab:judge_coverage}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nJudge & MT-Bench & Arena-Hard & Overall \\\\\n\\midrule\nGPT-5.5 & 0.99 & 0.98 & 0.984 \\\\\nClaude Opus 4.7 & 0.98 & 0.97 & 0.974 \\\\\nClaude Sonnet 4.6 & 0.99 & 0.98 & 0.984 \\\\\nDeepSeek-V4-Pro & 0.97 & 0.95 & 0.958 \\\\\nQwen3-235B-A22B & 0.96 & 0.93 & 0.942 \\\\\nQwen3.6-27B & 0.94 & 0.91 & 0.922 \\\\\nLlama-4-Maverick & 0.95 & 0.92 & 0.932 \\\\\nGemini-2.5-Pro & 0.98 & 0.96 & 0.968 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nInter-judge Fleiss $\\kappa = 0.38$ confirms substantial systematic disagreement. Same-family judge pairs show higher agreement (e.g., Claude Opus--Sonnet: $\\kappa = 0.51$) than cross-family pairs (mean $\\kappa = 0.32$), consistent with preference leakage effects.\n\n\\subsection{Per-Item Exposure Estimation}\n\nWe construct reference variants for 627 items (87\\% quality pass rate). The performance gap source achieves 95\\% coverage, while temporal signal (41\\%) and LogProber (55\\%) provide complementary but sparser signals. The composite $\\hat{e}_i$ distribution has mean 0.34 (std 0.22), with MT-Bench items showing higher exposure (mean 0.42) than Arena-Hard (mean 0.29), consistent with MT-Bench's earlier release and broader training data inclusion.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-source $e_i$ estimation statistics.}\n\\label{tab:ei_sources}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSource & Coverage & Mean $e_i$ & Std & Weight \\\\\n\\midrule\nPerformance Gap & 0.95 & 0.36 & 0.24 & 0.62 \\\\\nTemporal Signal & 0.41 & 0.31 & 0.19 & 0.18 \\\\\nLogProber & 0.55 & 0.33 & 0.26 & 0.20 \\\\\nComposite & 1.00 & 0.34 & 0.22 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Baselines}\n\nWe compare G-MFRM against: (1) \\textbf{Raw Multi-Judge Average}, (2) \\textbf{MFRM-only} (Eq.~\\ref{eq:mfrm}), (3--4) \\textbf{Sequential pipelines} (bias-first and contamination-first), (5) \\textbf{CyclicJudge} \\citep{li2024cyclicjudge}, (6) \\textbf{CyclicJudge + Discard} (removing high-exposure items), (7) \\textbf{DCR Factor} \\citep{dekoninck2024dcr}, (8) \\textbf{UDA} \\citep{son2024uda}, and (9) \\textbf{PrefLeak Calibration}. Chatbot Arena Elo serves as the reference human ranking.\n\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Comparison}\n\nTable~\\ref{tab:main_comparison} presents the primary results. G-MFRM achieves the highest Kendall-$\\tau$ (0.823) and Spearman-$\\rho$ (0.857) with Chatbot Arena rankings, outperforming all baselines.\n\n\\begin{table}[t]\n\\centering\n\\caption{Method comparison on MT-Bench + Arena-Hard (Chatbot Arena Elo as reference ranking).}\n\\label{tab:main_comparison}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & $\\tau$ & $\\rho$ & Top-5 & Top-10 & $|\\Delta R|$ \\\\\n\\midrule\nRaw Average & .761 & .812 & 0.6 & 0.7 & 3.1 \\\\\nMFRM-only & .794 & .831 & 0.8 & 0.8 & 2.1 \\\\\nSeq. (bias-first) & .788 & .824 & 0.6 & 0.8 & 2.4 \\\\\nSeq. (contam-first) & .791 & .828 & 0.8 & 0.8 & 2.2 \\\\\nCyclicJudge & .802 & .838 & 0.8 & 0.8 & 1.9 \\\\\nCyclicJudge + Disc. & .798 & .835 & 0.8 & 0.8 & 2.0 \\\\\nDCR Factor & .779 & .821 & 0.6 & 0.7 & 2.6 \\\\\nUDA & .805 & .841 & 0.8 & 0.8 & 1.8 \\\\\nPrefLeak Calib. & .783 & .822 & 0.6 & 0.8 & 2.5 \\\\\n\\textbf{G-MFRM (ours)} & \\textbf{.823} & \\textbf{.857} & \\textbf{0.8} & \\textbf{0.9} & \\textbf{1.5} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe improvement over UDA ($\\Delta\\tau = +0.018$, 95\\% CI [0.002, 0.034]) is borderline significant ($p = 0.067$, Wilcoxon signed-rank). G-MFRM significantly outperforms MFRM-only ($p = 0.042$), sequential pipelines ($p \\leq 0.024$), DCR ($p = 0.008$), and PrefLeak ($p = 0.011$).\n\nCyclicJudge + Discard performs \\emph{worse} than CyclicJudge alone ($\\tau$ = 0.798 vs 0.802), confirming that item discard wastes information and increases estimation variance at small sample sizes.\n\n\\subsection{Subset Analysis: High-Contamination Models}\n\nThe key finding emerges from stratifying by contamination level (Table~\\ref{tab:subset}). G-MFRM's advantage is concentrated on models in the top contamination quartile ($c_n > 0.75$).\n\n\\begin{table}[t]\n\\centering\n\\caption{G-MFRM advantage by model contamination quartile (vs.\\ UDA).}\n\\label{tab:subset}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nQuartile & $N$ & $c_n$ Range & $\\tau_{\\text{G-MFRM}}$ & $\\tau_{\\text{UDA}}$ & $\\Delta\\tau$ \\\\\n\\midrule\nQ1 (lowest) & 6 & [0.04, 0.18] & .807 & .811 & $-$.004 \\\\\nQ2 & 5 & [0.22, 0.48] & .815 & .802 & +.013 \\\\\nQ3 & 5 & [0.52, 0.75] & .831 & .808 & +.023 \\\\\nQ4 (highest) & 6 & [0.85, 1.42] & \\textbf{.867} & .782 & \\textbf{+.085}$^*$ \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\small $^*p = 0.021$ (Wilcoxon signed-rank).}\n\\end{tabular}\n\\end{table}\n\nFor low-contamination models (Q1), G-MFRM gracefully degrades to MFRM-level performance (no overcorrection). For high-contamination models, the improvement is substantial and statistically significant ($\\Delta\\tau = +0.085$, $p = 0.021$), with post-hoc power of 0.74.\n\n\\subsection{Diagnostic Outputs}\n\n\\paragraph{Judge severity profiles.} Table~\\ref{tab:judge_severity} presents estimated $d_j$ values. The severity range spans 1.74 logits (GPT-5.5: $d = -0.83$ to DeepSeek-V4-Pro: $d = +0.91$), corresponding to approximately 1.5 rating scale levels of systematic bias. All judges show acceptable model fit (Infit MNSQ: [0.94, 1.21]).\n\n\\begin{table}[t]\n\\centering\n\\caption{Estimated judge severity $d_j$ (positive = harsher).}\n\\label{tab:judge_severity}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nJudge & $d_j$ (mean) & 95\\% CI \\\\\n\\midrule\nGPT-5.5 & $-$0.83 & [$-$1.02, $-$0.64] \\\\\nClaude Opus 4.7 & $-$0.31 & [$-$0.48, $-$0.14] \\\\\nClaude Sonnet 4.6 & $-$0.12 & [$-$0.29, +0.05] \\\\\nGemini-2.5-Pro & $-$0.22 & [$-$0.40, $-$0.04] \\\\\nLlama-4-Maverick & +0.15 & [$-$0.03, +0.33] \\\\\nQwen3-235B-A22B & +0.44 & [+0.26, +0.62] \\\\\nQwen3.6-27B & +0.62 & [+0.43, +0.81] \\\\\nDeepSeek-V4-Pro & +0.91 & [+0.72, +1.10] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Per-model contamination susceptibility.} The fitted $c_n$ distribution (median 0.48, range [0.04, 1.42]) correlates with external ConStat per-model deltas at $r = 0.52$ ($p = 0.013$), supporting construct validity. Models with highest $c_n$ (Qwen3-235B-A22B: 1.42, Qwen3.6-27B: 0.85, GPT-4.5: 0.72) show the largest ability estimate corrections in Stage 3.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-model $c_n$ estimates (top-10 by Arena Elo) with ConStat validation. $\\theta$ shift: Stage 1 $\\to$ Stage 3.}\n\\label{tab:cn_per_model}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nModel & $c_n$ & 95\\% CI & ConStat $\\Delta$ & $\\theta$ shift \\\\\n\\midrule\nGPT-5.5 & 0.31 & [0.08, 0.58] & 0.21 & $-$0.04 \\\\\nClaude Opus 4.7 & 0.22 & [0.03, 0.47] & 0.15 & $-$0.02 \\\\\nGemini-2.5-Pro & 0.58 & [0.29, 0.91] & 0.44 & $-$0.12 \\\\\nDeepSeek-V4-Pro & 0.15 & [0.01, 0.38] & 0.11 & +0.01 \\\\\nClaude Sonnet 4.6 & 0.41 & [0.15, 0.71] & 0.28 & $-$0.08 \\\\\nLlama-4-Maverick & 0.09 & [0.00, 0.28] & 0.07 & +0.03 \\\\\nQwen3-235B-A22B & 1.42 & [0.98, 1.91] & 0.82 & $-$0.27 \\\\\nGPT-4.5 & 0.72 & [0.41, 1.08] & 0.51 & $-$0.15 \\\\\nMistral-Large-3 & 0.38 & [0.12, 0.68] & 0.30 & $-$0.05 \\\\\nQwen3.6-27B & 0.85 & [0.52, 1.22] & 0.61 & $-$0.19 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Theta overestimation by contamination level.} The mean $\\hat{\\theta}$ overestimation (Stage 1 vs Stage 3) scales with $c_n$: low-$c_n$ models ($c_n < 0.25$, $N = 6$) show negligible bias (mean 0.03 logits), medium-$c_n$ models ($0.25$--$0.75$, $N = 10$) show moderate bias (0.11 logits), and high-$c_n$ models ($c_n > 0.75$, $N = 6$) show substantial bias (0.21 logits). This directly confirms the confounding mechanism identified in Section~\\ref{sec:observation}.\n\n\\subsection{Model Fit and Convergence}\n\nStage 1 achieves $\\hat{R}_{\\max} = 1.02$ and ESS$_{\\min} = 412$. Stage 3 shows acceptable but weaker convergence ($\\hat{R}_{\\max} = 1.06$, ESS$_{\\min} = 132$) with 14 divergent transitions (0.07\\% of samples). WAIC model comparison favors G-MFRM over MFRM ($\\Delta$WAIC = $-489 \\pm 124$, approximately 4$\\sigma$ significant), providing statistical evidence for the contamination term beyond ranking metrics.\n\n\\begin{table}[t]\n\\centering\n\\caption{Facet fit statistics summary.}\n\\label{tab:fit_stats}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nFacet & $N$ & Infit Range & Outfit Range & Misfit \\% \\\\\n\\midrule\nModel ($\\theta$) & 22 & [0.82, 1.28] & [0.78, 1.35] & 9.1\\% \\\\\nItem ($b$) & 660 & [0.71, 1.42] & [0.65, 1.58] & 5.8\\% \\\\\nJudge ($d$) & 8 & [0.94, 1.21] & [0.88, 1.31] & 12.5\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPerson-fit statistics ($l_z$) correlate moderately with $c_n$ ($r = 0.41$, $p = 0.058$), indicating that traditional misfit detection captures part of but not all contamination signal---supporting $c_n$ as a distinct and complementary parameter.\n\n\\section{Analysis}\n\\label{sec:analysis}\n\n\\subsection{Exposure Indicator Ablation}\n\nTable~\\ref{tab:ablation} presents leave-one-out ablation of the $e_i$ estimation sources. The performance gap source contributes most ($\\Delta\\tau = -0.037$ when removed), while temporal signal contributes least ($\\Delta\\tau = -0.005$). A performance-gap-only configuration achieves $\\tau = 0.814$---only 0.009 below the full pipeline---providing a simplified deployment option.\n\n\\begin{table}[t]\n\\centering\n\\caption{$e_i$ source ablation: impact on downstream G-MFRM performance.}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nConfiguration & $N$ Sources & $\\tau$ & $\\Delta\\tau$ \\\\\n\\midrule\nFull Pipeline & 3 & .823 & --- \\\\\nw/o Performance Gap & 2 & .786 & $-$.037 \\\\\nw/o Temporal Signal & 2 & .818 & $-$.005 \\\\\nw/o LogProber & 2 & .812 & $-$.011 \\\\\nOnly Performance Gap & 1 & .814 & $-$.009 \\\\\nOnly Temporal & 1 & .788 & $-$.035 \\\\\nOnly LogProber & 1 & .795 & $-$.028 \\\\\nMFRM (no $e_i$) & 0 & .794 & $-$.029 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Judge Count Sensitivity}\n\nTable~\\ref{tab:judge_count} shows G-MFRM performance as a function of the number of judges. The model requires $\\geq 4$ judges to reliably separate $d_j$ from $c_n$ effects. With 2 judges, G-MFRM gracefully degrades to MFRM-level performance ($\\Delta\\tau = +0.003$, $\\hat{R} = 1.18$). We recommend 6+ judges for practical deployment.\n\n\\begin{table}[t]\n\\centering\n\\caption{G-MFRM performance by number of judges.}\n\\label{tab:judge_count}\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\n$J$ & $\\tau_{\\text{G-MFRM}}$ & $\\tau_{\\text{MFRM}}$ & $\\Delta$ & $\\hat{R}_{\\max}$ & ESS$_{\\min}$ \\\\\n\\midrule\n2 & .768 & .765 & +.003 & 1.18 & 41 \\\\\n4 & .791 & .779 & +.012 & 1.09 & 84 \\\\\n6 & .812 & .789 & +.023 & 1.07 & 108 \\\\\n8 & .823 & .794 & +.029 & 1.06 & 132 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Preference leakage diagnostic.} Leave-one-judge-out analysis detects 2 significant same-family preference leakage pairs: Claude Opus 4.7 $\\to$ Claude Sonnet 4.6 (residual shift $-$0.14, $p = 0.032$) and Qwen3-235B-A22B $\\to$ Qwen3.6-27B (residual shift $-$0.11, $p = 0.048$). These effects are small relative to the $d_j$ range (1.74 logits) and are absorbed uniformly into $\\hat{\\theta}_n$.\n\n\\subsection{Cross-Benchmark Generalization}\n\nWe replicate the G-MFRM pipeline on WildBench (1,024 items, 6 judges, 18 models) as a held-out generalization test (Table~\\ref{tab:cross_benchmark}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-benchmark performance and $c_n$ consistency.}\n\\label{tab:cross_benchmark}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nBenchmark & Items & $J$ & $\\tau_{\\text{G-MFRM}}$ & $\\tau_{\\text{UDA}}$ & $\\Delta\\tau$ & $c_n$ med. \\\\\n\\midrule\nMT-Bench & 160 & 8 & .811 & .798 & +.013 & 0.55 \\\\\nArena-Hard & 500 & 8 & .831 & .812 & +.019 & 0.44 \\\\\nWildBench & 1024 & 6 & .808 & .793 & +.015 & 0.38 \\\\\nCombined & 660 & 8 & .823 & .805 & +.018 & 0.48 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPer-model $c_n$ estimates show high cross-benchmark consistency: $r = 0.78$ (MT-Bench vs Arena-Hard), $r = 0.74$ (Arena-Hard vs WildBench), $r = 0.68$ (MT-Bench vs WildBench). This confirms contamination susceptibility is a model-level trait, not a benchmark artifact.\n\n\\subsection{Error Propagation Sensitivity}\n\nSince Stage 2 $\\hat{e}_i$ values carry estimation noise, we assess robustness by injecting Gaussian noise at varying $\\sigma$ levels (Table~\\ref{tab:sensitivity}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Error propagation sensitivity (20 replications per $\\sigma$).}\n\\label{tab:sensitivity}\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\n$\\sigma_e$ & $\\theta$ RMSE & $\\theta$ $\\tau$ & $c_n$ RMSE & $c_n$ Corr \\\\\n\\midrule\n0.0 & 0.128 & .916 & 0.53 & 0.86 \\\\\n0.1 & 0.130 & .915 & 0.55 & 0.85 \\\\\n0.2 & 0.136 & .914 & 0.58 & 0.84 \\\\\n0.5 & 0.175 & .885 & 0.84 & 0.75 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $\\sigma \\leq 0.2$ (our estimated operating range), $\\theta$ RMSE degrades by only 6.3\\% and $c_n$ correlation with truth remains above 0.84. The staged estimation is robust within practical noise levels. At $\\sigma = 0.5$ (worst case), degradation becomes substantial (36.7\\% $\\theta$ RMSE increase), establishing a clear boundary condition.\n\n\\subsection{Adversarial Robustness}\n\nWe test G-MFRM against three adversarial contamination types following \\citet{wang2026adversarial} (Table~\\ref{tab:adversarial}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Adversarial contamination detection and rank protection.}\n\\label{tab:adversarial}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nType & Severity & AUC & \\multicolumn{2}{c}{Rank Corrupt.} \\\\\n& & & w/o & w/ G-MFRM \\\\\n\\midrule\nData Poisoning & Mild & 0.76 & 1.8 & 0.9 \\\\\nData Poisoning & Severe & 0.92 & 4.1 & 1.2 \\\\\nPrompt Injection & Mild & 0.74 & 1.5 & 0.8 \\\\\nPrompt Injection & Severe & 0.88 & 3.8 & 1.4 \\\\\nMemorization & Mild & 0.83 & 2.1 & 0.7 \\\\\nMemorization & Severe & 0.93 & 4.5 & 0.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nG-MFRM provides a rank protection rate of 66\\%, reducing mean rank corruption from 3.2 to 1.1 positions. Detection performance scales with severity (AUC: 0.78 mild $\\to$ 0.91 severe). The fundamental limitation is adversarial contamination that mimics genuine ability gain uniformly across items (22\\% undetectable)---this is outside the rank-1 $c \\cdot e$ gating assumption.\n\n\\subsection{Post-Hoc Power Analysis}\n\nWith $N = 22$ models, the study achieves post-hoc power of 0.58 for detecting the observed effect size ($d = 0.42$) at $\\alpha = 0.05$. Power reaches 0.74 when restricted to the high-contamination subset ($N = 6$, $d = 1.31$). An estimated $N = 35$ models would be required for 80\\% power on the full sample, indicating that our study is moderately underpowered for the overall comparison but adequately powered for the clinically relevant subset.\n\n\\section{Conclusion}\n\nWe presented G-MFRM, a staged joint calibration framework that addresses the previously unrecognized confounding between judge bias and benchmark contamination in LLM evaluation. Our formal analysis establishes that sequential correction pipelines retain systematic bias proportional to confounding strength, while G-MFRM's conditional joint estimation achieves near-zero bias.\n\nOn real evaluation data (22 models, 8 judges, 660 items), G-MFRM achieves the highest agreement with human rankings ($\\tau = 0.823$) with particular strength on high-contamination models ($\\Delta\\tau = +0.085$ in top quartile). Beyond ranking accuracy, G-MFRM provides interpretable diagnostic outputs---per-judge severity profiles (1.74 logit range), per-model contamination susceptibility (validated at $r = 0.52$ against ConStat), and per-item exposure indicators---constituting a unified measurement framework for LLM evaluation auditing that no existing method offers.\n\n\\section*{Limitations}\n\n\\paragraph{Statistical power.} With $N = 22$ models, the overall comparison against UDA achieves only 0.58 post-hoc power. The borderline significance ($p = 0.067$) means we cannot claim definitive ranking superiority over UDA on the full population. Future work should expand to $\\geq 35$ models.\n\n\\paragraph{Exposure estimation noise.} The effective $\\sigma_e \\approx 0.24$ of our $e_i$ pipeline sits at the edge of the robust regime ($\\sigma \\leq 0.2$), introducing 6--10\\% $\\theta$ precision loss relative to oracle exposure values. Temporal signal coverage (41\\%) limits the composite quality.\n\n\\paragraph{Rank-1 assumption.} The $c_n \\cdot e_i$ gating assumes contamination effects follow a rank-1 structure. Adversarial contamination that uniformly inflates performance across all items (22\\% of tested adversarial patterns) is fundamentally undetectable under this assumption.\n\n\\paragraph{Judge-model interaction.} G-MFRM does not model $f_{nj}$ (judge-model interaction). Same-family preference leakage (detected in 2/5 pairs, effect $\\leq 0.14$ logits) is absorbed uniformly into $\\hat{\\theta}_n$ rather than explicitly corrected.\n\n\\paragraph{Convergence.} Stage 3 convergence ($\\hat{R} = 1.06$, ESS = 132) is acceptable but not ideal. The 14 divergent transitions (0.07\\%) and marginal posterior coverage ($c_n$ 95\\% CI coverage: 88\\% vs nominal 95\\%) suggest the Half-Cauchy prior may be slightly too informative for high-$c_n$ models.\n\n\\bibliographystyle{aaai}\n\\begin{thebibliography}{30}\n\n\\bibitem[Angrist and Pischke, 2009]{angrist2009mostly}\nAngrist, J.~D. and Pischke, J.-S. (2009).\n\\newblock \\emph{Mostly Harmless Econometrics: An Empiricist's Companion}.\n\\newblock Princeton University Press.\n\n\\bibitem[Dekoninck et~al., 2024]{dekoninck2024dcr}\nDekoninck, J., Müller, M., Fischer, M., and Vechev, M. (2024).\n\\newblock Evading data contamination detection for language models is (too) easy.\n\\newblock In \\emph{Proceedings of ACL}.\n\n\\bibitem[Eckes, 2011]{eckes2011introduction}\nEckes, T. (2011).\n\\newblock \\emph{Introduction to Many-Facet Rasch Measurement}.\n\\newblock Peter Lang.\n\n\\bibitem[Engelhard, 2013]{engelhard2013invariant}\nEngelhard, G. (2013).\n\\newblock \\emph{Invariant Measurement: Using Rasch Models in the Social, Behavioral, and Health Sciences}.\n\\newblock Routledge.\n\n\\bibitem[Fox, 2010]{fox2010bayesian}\nFox, J.-P. (2010).\n\\newblock \\emph{Bayesian Item Response Modeling: Theory and Applications}.\n\\newblock Springer.\n\n\\bibitem[Fox and Glas, 2001]{fox2001bayesian}\nFox, J.-P. and Glas, C.~A.~W. (2001).\n\\newblock Bayesian estimation of a multilevel {IRT} model using {Gibbs} sampling.\n\\newblock \\emph{Psychometrika}, 66(2):271--288.\n\n\\bibitem[Golchin and Surdeanu, 2023]{golchin2023time}\nGolchin, S. and Surdeanu, M. (2023).\n\\newblock Time travel in {LLMs}: Tracing data contamination in large language models.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[Heckman, 1979]{heckman1979sample}\nHeckman, J.~J. (1979).\n\\newblock Sample selection bias as a specification error.\n\\newblock \\emph{Econometrica}, 47(1):153--161.\n\n\\bibitem[Li et~al., 2024]{li2024cyclicjudge}\nLi, Y., Zhang, Y., and Sun, L. (2024).\n\\newblock {CyclicJudge}: Mitigating inherent biases in {LLM}-as-a-judge via cyclic evaluation.\n\\newblock In \\emph{Proceedings of NeurIPS}.\n\n\\bibitem[Linacre, 1989]{linacre1989manyfacet}\nLinacre, J.~M. (1989).\n\\newblock \\emph{Many-Facet Rasch Measurement}.\n\\newblock MESA Press.\n\n\\bibitem[Lord and Novick, 1968]{lord1968statistical}\nLord, F.~M. and Novick, M.~R. (1968).\n\\newblock \\emph{Statistical Theories of Mental Test Scores}.\n\\newblock Addison-Wesley.\n\n\\bibitem[Oren et~al., 2024]{oren2024constat}\nOren, Y., Meister, C., Chatterji, N., Laber, F., and Hashimoto, T. (2024).\n\\newblock Proving test set contamination in black box language models.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[Patz et~al., 2002]{patz2002mcmc}\nPatz, R.~J., Junker, B.~W., Johnson, M.~S., and Mariano, L.~T. (2002).\n\\newblock The hierarchical rater model for rated test items and its application to large-scale educational assessment data.\n\\newblock \\emph{Journal of Educational and Behavioral Statistics}, 27(4):341--384.\n\n\\bibitem[Rasch, 1960]{rasch1960probabilistic}\nRasch, G. (1960).\n\\newblock \\emph{Probabilistic Models for Some Intelligence and Attainment Tests}.\n\\newblock Danish Institute for Educational Research.\n\n\\bibitem[Robitzsch, 2020]{robitzsch2020dif}\nRobitzsch, A. (2020).\n\\newblock {L}p loss functions in invariance alignment and {Haberman} linking with few or many groups.\n\\newblock \\emph{Stats}, 3(3):246--283.\n\n\\bibitem[Shi et~al., 2023]{shi2023detecting}\nShi, W., Ajith, A., Xia, M., Huang, Y., Liu, D., Blevins, T., Chen, D., and Zettlemoyer, L. (2023).\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[Shu et~al., 2013]{shu2013dg}\nShu, Z., Henson, R., and Luecht, R. (2013).\n\\newblock Using deterministic, gated item response theory model to detect test cheating due to item compromise.\n\\newblock \\emph{Psychometrika}, 78(3):481--497.\n\n\\bibitem[Son et~al., 2024]{son2024uda}\nSon, G., Kim, N., Cho, H., and Yun, S. (2024).\n\\newblock {UDA}: Unified difficulty-aware evaluation framework for benchmarking language models.\n\\newblock In \\emph{Proceedings of NeurIPS}.\n\n\\bibitem[Wang et~al., 2026]{wang2026adversarial}\nWang, T., Chen, X., and Liu, Z. (2026).\n\\newblock Adversarial contamination attacks against {LLM} benchmarks.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[Wind and Peterson, 2018]{wind2018dif}\nWind, S.~A. and Peterson, M.~E. (2018).\n\\newblock A systematic review of methods for evaluating rating quality in language testing.\n\\newblock \\emph{Language Testing}, 35(2):161--192.\n\n\\bibitem[Zheng et~al., 2023]{zheng2023judging}\nZheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin, Z., Li, Z., Li, D., Xing, E.~P., Zhang, H., Gonzalez, J.~E., and Stoica, I. (2023).\n\\newblock Judging {LLM}-as-a-judge with {MT}-{Bench} and {Chatbot Arena}.\n\\newblock In \\emph{Proceedings of NeurIPS}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "d05ebc5a-7fe7-479c-b216-02f14dcb2b98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T041217 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/art…",
  "leafUuid": "092a3f70-c0cd-40c9-aea7-d35c95aad10c",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream_20260522T041217",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57"
}
```

---

### Tool call

_source line 23 · 2026-05-22T04:46:38.187Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NBAbnd8haqVVXMva7DevBG`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "092a3f70-c0cd-40c9-aea7-d35c95aad10c",
  "isSidechain": false,
  "requestId": "req_011CbGzxgHMxmHFRBzCzuki1",
  "type": "assistant",
  "uuid": "5caef64b-b7f8-4db2-9a72-cd7b17a1986f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019eY1hKZ612jmtNsWveA4Yy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12605,
      "cache_read_input_tokens": 54791,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12605,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 54791,
          "cache_creation_input_tokens": 12605,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12605
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

_source line 24 · 2026-05-22T04:46:38.445Z_

<details><summary>↩ Tool result · reported error · `toolu_01NBAbnd8haqVVXMva7DevBG`</summary>

```text
Exit code 1
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))

! LaTeX Error: File `aaai25.sty' not found.

Type X to quit or &lt;RETURN> to proceed,
or enter new name. (Default extension: sty)

Enter file name: 
! Emergency stop.
&lt;read *> 
         
l.3 \usepackage
               {times}^^M
!  ==> Fatal error occurred, no output PDF file produced!
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5caef64b-b7f8-4db2-9a72-cd7b17a1986f",
  "isSidechain": false,
  "promptId": "207a7a17-59d3-4278-abf7-5d52712c6cbf",
  "type": "user",
  "uuid": "89e3c020-ff33-48cc-945e-6d89490a8010",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n\n! LaTeX Error: File `aaai25.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "5caef64b-b7f8-4db2-9a72-cd7b17a1986f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-22T04:46:44.655Z_

<details><summary>Logged reasoning block</summary>

```text
The aaai25.sty is not available. Let me switch to a standard article class or find what's available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89e3c020-ff33-48cc-945e-6d89490a8010",
  "isSidechain": false,
  "requestId": "req_011CbGzy39ECQeKP6V5pQ47e",
  "type": "assistant",
  "uuid": "933c5df0-bb12-49d8-b1f3-25d2e187eef4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018xmNL2kFvfLv77TdMpZApM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 463,
      "cache_read_input_tokens": 67396,
      "output_tokens": 474,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 463,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 474,
          "cache_read_input_tokens": 67396,
          "cache_creation_input_tokens": 463,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 463
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

_source line 26 · 2026-05-22T04:46:45.210Z_

AAAI style not available. I'll switch to a standard article class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "933c5df0-bb12-49d8-b1f3-25d2e187eef4",
  "isSidechain": false,
  "requestId": "req_011CbGzy39ECQeKP6V5pQ47e",
  "type": "assistant",
  "uuid": "73d9d0a4-069e-4627-bedd-bbdafac61dc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018xmNL2kFvfLv77TdMpZApM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 463,
      "cache_read_input_tokens": 67396,
      "output_tokens": 474,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 463,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 474,
          "cache_read_input_tokens": 67396,
          "cache_creation_input_tokens": 463,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 463
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

_source line 27 · 2026-05-22T04:46:49.757Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01NpcfyyRX5LgMFSXNKun819`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median/paper.tex",
  "old_string": "\\documentclass[letterpaper]{article}\n\\usepackage{aaai25}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\n\\setlength\\titlebox{2.5in}",
  "new_string": "\\documentclass[letterpaper,11pt]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73d9d0a4-069e-4627-bedd-bbdafac61dc2",
  "isSidechain": false,
  "requestId": "req_011CbGzy39ECQeKP6V5pQ47e",
  "type": "assistant",
  "uuid": "e7dc507f-fddf-44c9-b5ee-0c51c4c1a002",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018xmNL2kFvfLv77TdMpZApM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 463,
      "cache_read_input_tokens": 67396,
      "output_tokens": 474,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 463,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 474,
          "cache_read_input_tokens": 67396,
          "cache_creation_input_tokens": 463,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 463
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

_source line 28 · 2026-05-22T04:46:49.806Z_

<details><summary>↩ Tool result · `toolu_01NpcfyyRX5LgMFSXNKun819`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7dc507f-fddf-44c9-b5ee-0c51c4c1a002",
  "isSidechain": false,
  "promptId": "207a7a17-59d3-4278-abf7-5d52712c6cbf",
  "type": "user",
  "uuid": "8a01444d-2a83-458e-a832-7ec0d6808f7c",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median/paper.tex",
    "oldString": "\\documentclass[letterpaper]{article}\n\\usepackage{aaai25}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\n\\setlength\\titlebox{2.5in}",
    "newString": "\\documentclass[letterpaper,11pt]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 8,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          "-\\documentclass[letterpaper]{article}",
          "-\\usepackage{aaai25}",
          "+\\documentclass[letterpaper,11pt]{article}",
          "+\\usepackage[margin=1in]{geometry}",
          " \\usepackage{times}",
          "-\\usepackage{helvet}",
          "-\\usepackage{courier}",
          " \\usepackage{graphicx}",
          " \\usepackage{amsmath,amssymb,amsfonts}",
          " \\usepackage{booktabs}"
        ]
      },
      {
        "oldStart": 13,
        "oldLines": 8,
        "newStart": 11,
        "newLines": 6,
        "lines": [
          " \\usepackage{algorithm}",
          " \\usepackage{algorithmic}",
          " ",
          "-\\setlength\\titlebox{2.5in}",
          "-",
          " \\title{G-MFRM: A Unified Diagnostic Framework for Joint Estimation of Judge Bias and Benchmark Contamination in LLM Evaluation}",
          " ",
          " \\author{"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "e7dc507f-fddf-44c9-b5ee-0c51c4c1a002",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T04:46:58.354Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01S9RKPqdy2LNeiPB5o7DCdS`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a01444d-2a83-458e-a832-7ec0d6808f7c",
  "isSidechain": false,
  "requestId": "req_011CbGzysgVJC1NUbbm5KxeR",
  "type": "assistant",
  "uuid": "7e13b62b-a68e-4945-a8fc-9039a08ccaeb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rskvsq7sJ1rhAt92w2aC91",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 558,
      "cache_read_input_tokens": 67859,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 558,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 165,
          "cache_read_input_tokens": 67859,
          "cache_creation_input_tokens": 558,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 558
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

_source line 30 · 2026-05-22T04:46:59.852Z_

<details><summary>↩ Tool result · `toolu_01S9RKPqdy2LNeiPB5o7DCdS`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
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
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/algorithms/algorithm.sty
(/usr/share/texlive/texmf-dist/tex/latex/float/float.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/algorithms/algorithmic.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `zheng2023judging' on page 1 undefined on inpu
t line 29.


Package natbib Warning: Citation `zheng2023judging' on page 1 undefined on inpu
t line 29.


Package natbib Warning: Citation `li2024cyclicjudge' on page 1 undefined on inp
ut line 29.


Package natbib Warning: Citation `golchin2023time' on page 1 undefined on input
 line 29.


Package natbib Warning: Citation `shi2023detecting' on page 1 undefined on inpu
t line 29.


Package natbib Warning: Citation `li2024cyclicjudge' on page 1 undefined on inp
ut line 31.


Package natbib Warning: Citation `son2024uda' on page 1 undefined on input line
 31.


Package natbib Warning: Citation `oren2024constat' on page 1 undefined on input
 line 31.


Package natbib Warning: Citation `dekoninck2024dcr' on page 1 undefined on inpu
t line 31.


Package natbib Warning: Citation `angrist2009mostly' on page 1 undefined on inp
ut line 33.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]

Package natbib Warning: Citation `angrist2009mostly' on page 2 undefined on inp
ut line 65.


LaTeX Warning: Reference `tab:mc_bias' on page 2 undefined on input line 69.


LaTeX Warning: Reference `tab:rho_sweep' on page 2 undefined on input line 89.

[2]

Package natbib Warning: Citation `linacre1989manyfacet' on page 3 undefined on 
input line 116.


Package natbib Warning: Citation `eckes2011introduction' on page 3 undefined on
 input line 116.


Package natbib Warning: Citation `heckman1979sample' on page 3 undefined on inp
ut line 131.

[3
pdfTeX warning (ext4): destination with the same identifier (name{table.1}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.139 \end{equation}
                    
pdfTeX warning (ext4): destination with the same identifier (name{table.2}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.139 \end{equation}
                    ]

LaTeX Warning: Reference `tab:judge_coverage' on page 4 undefined on input line
 151.


LaTeX Warning: Reference `eq:mfrm' on page 4 undefined on input line 199.


Package natbib Warning: Citation `li2024cyclicjudge' on page 4 undefined on inp
ut line 199.


Package natbib Warning: Citation `dekoninck2024dcr' on page 4 undefined on inpu
t line 199.


Package natbib Warning: Citation `son2024uda' on page 4 undefined on input line
 199.

[4
pdfTeX warning (ext4): destination with the same identifier (name{table.3}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.200 
      ]

LaTeX Warning: Reference `tab:main_comparison' on page 5 undefined on input lin
e 206.


LaTeX Warning: Reference `tab:subset' on page 5 undefined on input line 237.


LaTeX Warning: Reference `tab:judge_severity' on page 5 undefined on input line
 261.

[5
pdfTeX warning (ext4): destination with the same identifier (name{table.4}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.262 
      
pdfTeX warning (ext4): destination with the same identifier (name{table.5}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.262 
      ]

LaTeX Warning: Reference `sec:observation' on page 6 undefined on input line 30
9.


LaTeX Warning: Reference `tab:ablation' on page 6 undefined on input line 338.

[6
pdfTeX warning (ext4): destination with the same identifier (name{table.6}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.339 
      
pdfTeX warning (ext4): destination with the same identifier (name{table.7}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.339 
      ]

LaTeX Warning: Reference `tab:judge_count' on page 7 undefined on input line 36
3.


LaTeX Warning: Reference `tab:cross_benchmark' on page 7 undefined on input lin
e 386.


LaTeX Warning: Reference `tab:sensitivity' on page 7 undefined on input line 40
9.

[7
pdfTeX warning (ext4): destination with the same identifier (name{table.8}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.426 \end{table}
                 
pdfTeX warning (ext4): destination with the same identifier (name{table.9}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.426 \end{table}
                 ]

Package natbib Warning: Citation `wang2026adversarial' on page 8 undefined on i
nput line 432.


LaTeX Warning: Reference `tab:adversarial' on page 8 undefined on input line 43
2.

[8
pdfTeX warning (ext4): destination with the same identifier (name{table.10}) ha
s been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.464 O
       n real evaluation data (22 models, 8 judges, 660 items), G-MFRM achie...

pdfTeX warning (ext4): destination with the same identifier (name{table.11}) ha
s been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.464 O
       n real evaluation data (22 models, 8 judges, 660 items), G-MFRM achie...
] [9
pdfTeX warning (ext4): destination with the same identifier (name{table.12}) ha
s been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.486 ...Dekoninck et~al., 2024]{dekoninck2024dcr}
                                                  
pdfTeX warning (ext4): destination with the same identifier (name{table.13}) ha
s been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.486 ...Dekoninck et~al., 2024]{dekoninck2024dcr}
                                                  ] [10
pdfTeX warning (ext4): destination with the same identifier (name{table.14}) ha
s been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.561 \bibitem[Shu et~al., 2013]{shu2013dg}
                                           ]

Package natbib Warning: There were undefined citations.

[11] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive
/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 166269 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
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
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/algorithms/algorithm.sty
(/usr/share/texlive/texmf-dist/tex/latex/float/float.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/algorithms/algorithmic.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(./paper.out) (./paper.out)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}] [2] [3
pdfTeX warning (ext4): destination with the same identifier (name{table.1}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.139 \end{equation}
                    
pdfTeX warning (ext4): destination with the same identifier (name{table.2}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.139 \end{equation}
                    ] [4
pdfTeX warning (ext4): destination with the same identifier (name{table.3}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.200 
      ] [5
pdfTeX warning (ext4): destination with the same identifier (name{table.4}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.262 
      
pdfTeX warning (ext4): destination with the same identifier (name{table.5}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.262 
      ] [6
pdfTeX warning (ext4): destination with the same identifier (name{table.6}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.339 
      
pdfTeX warning (ext4): destination with the same identifier (name{table.7}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.339 
      ] [7
pdfTeX warning (ext4): destination with the same identifier (name{table.8}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.426 \end{table}
                 
pdfTeX warning (ext4): destination with the same identifier (name{table.9}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.426 \end{table}
                 ] [8
pdfTeX warning (ext4): destination with the same identifier (name{table.10}) ha
s been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.464 O
       n real evaluation data (22 models, 8 judges, 660 items), G-MFRM achie...

pdfTeX warning (ext4): destination with the same identifier (name{table.11}) ha
s been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.464 O
       n real evaluation data (22 models, 8 judges, 660 items), G-MFRM achie...
] [9
pdfTeX warning (ext4): destination with the same identifier (name{table.12}) ha
s been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.486 ...Dekoninck et~al., 2024]{dekoninck2024dcr}
                                                  
pdfTeX warning (ext4): destination with the same identifier (name{table.13}) ha
s been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.486 ...Dekoninck et~al., 2024]{dekoninck2024dcr}
                                                  ] [10
pdfTeX warning (ext4): destination with the same identifier (name{table.14}) ha
s been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.561 \bibitem[Shu et~al., 2013]{shu2013dg}
                                           ] [11] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive
/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 169917 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e13b62b-a68e-4945-a8fc-9039a08ccaeb",
  "isSidechain": false,
  "promptId": "207a7a17-59d3-4278-abf7-5d52712c6cbf",
  "type": "user",
  "uuid": "f2517c0d-58c1-47cb-88ed-31d876e268bd",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/algorithms/algorithm.sty\n(/usr/share/texlive/texmf-dist/tex/latex/float/float.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/algorithms/algorithmic.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `zheng2023judging' on page 1 undefined on inpu\nt line 29.\n\n\nPackage natbib Warning: Citation `zheng2023judging' on page 1 undefined on inpu\nt line 29.\n\n\nPackage natbib Warning: Citation `li2024cyclicjudge' on page 1 undefined on inp\nut line 29.\n\n\nPackage natbib Warning: Citation `golchin2023time' on page 1 undefined on input\n line 29.\n\n\nPackage natbib Warning: Citation `shi2023detecting' on page 1 undefined on inpu\nt line 29.\n\n\nPackage natbib Warning: Citation `li2024cyclicjudge' on page 1 undefined on inp\nut line 31.\n\n\nPackage natbib Warning: Citation `son2024uda' on page 1 undefined on input line\n 31.\n\n\nPackage natbib Warning: Citation `oren2024constat' on page 1 undefined on input\n line 31.\n\n\nPackage natbib Warning: Citation `dekoninck2024dcr' on page 1 undefined on inpu\nt line 31.\n\n\nPackage natbib Warning: Citation `angrist2009mostly' on page 1 undefined on inp\nut line 33.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n\nPackage natbib Warning: Citation `angrist2009mostly' on page 2 undefined on inp\nut line 65.\n\n\nLaTeX Warning: Reference `tab:mc_bias' on page 2 undefined on input line 69.\n\n\nLaTeX Warning: Reference `tab:rho_sweep' on page 2 undefined on input line 89.\n\n[2]\n\nPackage natbib Warning: Citation `linacre1989manyfacet' on page 3 undefined on \ninput line 116.\n\n\nPackage natbib Warning: Citation `eckes2011introduction' on page 3 undefined on\n input line 116.\n\n\nPackage natbib Warning: Citation `heckman1979sample' on page 3 undefined on inp\nut line 131.\n\n[3\npdfTeX warning (ext4): destination with the same identifier (name{table.1}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.139 \\end{equation}\n                    \npdfTeX warning (ext4): destination with the same identifier (name{table.2}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.139 \\end{equation}\n                    ]\n\nLaTeX Warning: Reference `tab:judge_coverage' on page 4 undefined on input line\n 151.\n\n\nLaTeX Warning: Reference `eq:mfrm' on page 4 undefined on input line 199.\n\n\nPackage natbib Warning: Citation `li2024cyclicjudge' on page 4 undefined on inp\nut line 199.\n\n\nPackage natbib Warning: Citation `dekoninck2024dcr' on page 4 undefined on inpu\nt line 199.\n\n\nPackage natbib Warning: Citation `son2024uda' on page 4 undefined on input line\n 199.\n\n[4\npdfTeX warning (ext4): destination with the same identifier (name{table.3}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.200 \n      ]\n\nLaTeX Warning: Reference `tab:main_comparison' on page 5 undefined on input lin\ne 206.\n\n\nLaTeX Warning: Reference `tab:subset' on page 5 undefined on input line 237.\n\n\nLaTeX Warning: Reference `tab:judge_severity' on page 5 undefined on input line\n 261.\n\n[5\npdfTeX warning (ext4): destination with the same identifier (name{table.4}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.262 \n      \npdfTeX warning (ext4): destination with the same identifier (name{table.5}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.262 \n      ]\n\nLaTeX Warning: Reference `sec:observation' on page 6 undefined on input line 30\n9.\n\n\nLaTeX Warning: Reference `tab:ablation' on page 6 undefined on input line 338.\n\n[6\npdfTeX warning (ext4): destination with the same identifier (name{table.6}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.339 \n      \npdfTeX warning (ext4): destination with the same identifier (name{table.7}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.339 \n      ]\n\nLaTeX Warning: Reference `tab:judge_count' on page 7 undefined on input line 36\n3.\n\n\nLaTeX Warning: Reference `tab:cross_benchmark' on page 7 undefined on input lin\ne 386.\n\n\nLaTeX Warning: Reference `tab:sensitivity' on page 7 undefined on input line 40\n9.\n\n[7\npdfTeX warning (ext4): destination with the same identifier (name{table.8}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.426 \\end{table}\n                 \npdfTeX warning (ext4): destination with the same identifier (name{table.9}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.426 \\end{table}\n                 ]\n\nPackage natbib Warning: Citation `wang2026adversarial' on page 8 undefined on i\nnput line 432.\n\n\nLaTeX Warning: Reference `tab:adversarial' on page 8 undefined on input line 43\n2.\n\n[8\npdfTeX warning (ext4): destination with the same identifier (name{table.10}) ha\ns been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.464 O\n       n real evaluation data (22 models, 8 judges, 660 items), G-MFRM achie...\n\npdfTeX warning (ext4): destination with the same identifier (name{table.11}) ha\ns been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.464 O\n       n real evaluation data (22 models, 8 judges, 660 items), G-MFRM achie...\n] [9\npdfTeX warning (ext4): destination with the same identifier (name{table.12}) ha\ns been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.486 ...Dekoninck et~al., 2024]{dekoninck2024dcr}\n                                                  \npdfTeX warning (ext4): destination with the same identifier (name{table.13}) ha\ns been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.486 ...Dekoninck et~al., 2024]{dekoninck2024dcr}\n                                                  ] [10\npdfTeX warning (ext4): destination with the same identifier (name{table.14}) ha\ns been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.561 \\bibitem[Shu et~al., 2013]{shu2013dg}\n                                           ]\n\nPackage natbib Warning: There were undefined citations.\n\n[11] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\nonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive\n/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 166269 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/algorithms/algorithm.sty\n(/usr/share/texlive/texmf-dist/tex/latex/float/float.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/algorithms/algorithmic.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}] [2] [3\npdfTeX warning (ext4): destination with the same identifier (name{table.1}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.139 \\end{equation}\n                    \npdfTeX warning (ext4): destination with the same identifier (name{table.2}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.139 \\end{equation}\n                    ] [4\npdfTeX warning (ext4): destination with the same identifier (name{table.3}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.200 \n      ] [5\npdfTeX warning (ext4): destination with the same identifier (name{table.4}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.262 \n      \npdfTeX warning (ext4): destination with the same identifier (name{table.5}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.262 \n      ] [6\npdfTeX warning (ext4): destination with the same identifier (name{table.6}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.339 \n      \npdfTeX warning (ext4): destination with the same identifier (name{table.7}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.339 \n      ] [7\npdfTeX warning (ext4): destination with the same identifier (name{table.8}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.426 \\end{table}\n                 \npdfTeX warning (ext4): destination with the same identifier (name{table.9}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.426 \\end{table}\n                 ] [8\npdfTeX warning (ext4): destination with the same identifier (name{table.10}) ha\ns been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.464 O\n       n real evaluation data (22 models, 8 judges, 660 items), G-MFRM achie...\n\npdfTeX warning (ext4): destination with the same identifier (name{table.11}) ha\ns been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.464 O\n       n real evaluation data (22 models, 8 judges, 660 items), G-MFRM achie...\n] [9\npdfTeX warning (ext4): destination with the same identifier (name{table.12}) ha\ns been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.486 ...Dekoninck et~al., 2024]{dekoninck2024dcr}\n                                                  \npdfTeX warning (ext4): destination with the same identifier (name{table.13}) ha\ns been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.486 ...Dekoninck et~al., 2024]{dekoninck2024dcr}\n                                                  ] [10\npdfTeX warning (ext4): destination with the same identifier (name{table.14}) ha\ns been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.561 \\bibitem[Shu et~al., 2013]{shu2013dg}\n                                           ] [11] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\nonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive\n/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 169917 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7e13b62b-a68e-4945-a8fc-9039a08ccaeb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T041217 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/art…",
  "leafUuid": "f2517c0d-58c1-47cb-88ed-31d876e268bd",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream_20260522T041217",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57"
}
```

---

### Assistant

_source line 33 · 2026-05-22T04:47:13.472Z_

PDF 编译成功（11 页，无致命错误，仅 duplicate destination warnings 因为多个 float 出现在同一页）。

产出：`/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median/paper.pdf`

论文覆盖了全部 9 个实验：
1. **multi_judge_data_collection** → §4.1 + Table 1 (judge coverage)
2. **item_exposure_estimation** → §4.2 + Table 3 (e_i sources)
3. **gmfrm_real_data_fit** → §5.3 (fit diagnostics) + Tables 6-7 (judge severity, c_n per model)
4. **baseline_comparison** → §5.1 + Table 4 (main comparison) + Table 5 (subset analysis)
5. **contamination_magnitude_calibration** → §5.3 (θ overestimation by c_n group)
6. **judge_count_sensitivity** → §6.2 + Table 9 (judge count curve) + leakage diagnostic
7. **exposure_indicator_ablation** → §6.1 + Table 8 (ablation)
8. **facet_fit_diagnostics** → §5.4 + Table 8 (fit stats) + WAIC comparison
9. **confounding_formal_observation** → §2 + Tables 1-2 (MC bias, ρ-sweep)
10. **wildbench_replication** → §6.3 + Table 10 (cross-benchmark)
11. **adversarial_robustness** → §6.4 + Table 11
12. **error_propagation_sensitivity** → §6.4 + Table 12 (sensitivity)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2517c0d-58c1-47cb-88ed-31d876e268bd",
  "isSidechain": false,
  "requestId": "req_011CbGzzcYgkz3Ubjmnz6j1o",
  "type": "assistant",
  "uuid": "c8a844da-1218-4a73-8b12-63df1b117588",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260522T041217/median",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M7UySPJeXL5Y1byRvFshRZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8632,
      "cache_read_input_tokens": 68417,
      "output_tokens": 466,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8632,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 466,
          "cache_read_input_tokens": 68417,
          "cache_creation_input_tokens": 8632,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8632
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

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T041217 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/art…",
  "leafUuid": "c8a844da-1218-4a73-8b12-63df1b117588",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream_20260522T041217",
  "sessionId": "33606c3c-2a96-439f-ad7e-5dfed492ad57"
}
```

---
