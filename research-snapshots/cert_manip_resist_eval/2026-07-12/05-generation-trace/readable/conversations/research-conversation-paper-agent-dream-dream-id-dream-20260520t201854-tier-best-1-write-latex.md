# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T201854 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/d5955a05-4002-488d-8660-8d47efae1571.jsonl`
- **Structured JSON:** [`61aa4932f09a097d5f60.json`](../../sessions/61/61aa4932f09a097d5f60.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T20:41:59.862Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T20:41:59.862Z",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T201854 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Full method contribution paper (Path A). CaCLR consistency loss provides meaningful gain, confirming distributional matching via MMD helps align capability-specific signals at mid-depth layers. Causal chain complete: Pareto frontier discovered on both architectures with architecture-dependent shape → decomposition explains frontier via difficulty/capability separation → CaCLR shifts frontier by aligning capability-specific components → orthogonality bounds output-based approaches across all languages. CKA provides mechanistic glue linking representation geometry to transfer success. Headline: \"CaCLR-trained correctness probes reduce non-English ECE by 3.5% over temperature scaling with zero target-language labels across 20 languages on Qwen3-235B and Llama 4 Scout.\"\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T20:41:59.867Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T20:41:59.867Z",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571"
}
```

---

## Round 1

42 recorded events

### User

_source line 3 · 2026-05-20T20:41:59.924Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T201854 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Full method contribution paper (Path A). CaCLR consistency loss provides meaningful gain, confirming distributional matching via MMD helps align capability-specific signals at mid-depth layers. Causal chain complete: Pareto frontier discovered on both architectures with architecture-dependent shape → decomposition explains frontier via difficulty/capability separation → CaCLR shifts frontier by aligning capability-specific components → orthogonality bounds output-based approaches across all languages. CKA provides mechanistic glue linking representation geometry to transfer success. Headline: "CaCLR-trained correctness probes reduce non-English ECE by 3.5% over temperature scaling with zero target-language labels across 20 languages on Qwen3-235B and Llama 4 Scout."

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d6812199-51cb-4f3b-a1d1-28a2f25b4592",
  "type": "user",
  "uuid": "4589ed54-80a9-479e-b53e-a28064256482",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T20:41:59.923Z_

```json
{
  "parentUuid": "4589ed54-80a9-479e-b53e-a28064256482",
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
  "uuid": "5c8f53ee-4916-46d7-be15-3089ada1de6e",
  "timestamp": "2026-05-20T20:41:59.923Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T20:41:59.923Z_

```json
{
  "parentUuid": "5c8f53ee-4916-46d7-be15-3089ada1de6e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "17f2aea0-d893-4d5b-8a84-86f361df9098",
  "timestamp": "2026-05-20T20:41:59.923Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate calibration research paper with CaCLR method",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571"
}
```

---

### Assistant

_source line 7 · 2026-05-20T20:42:02.733Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17f2aea0-d893-4d5b-8a84-86f361df9098",
  "isSidechain": false,
  "requestId": "req_011CbEUCd3fdca7w4KVwpDLH",
  "type": "assistant",
  "uuid": "c7eea3e2-a314-4546-add5-f76ef892fbac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115VF35LWoS8nevg8inTo9h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11481,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11481,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11481
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

_source line 8 · 2026-05-20T20:42:03.727Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QpQTp8NaGmcmzCEbrFGCdJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7eea3e2-a314-4546-add5-f76ef892fbac",
  "isSidechain": false,
  "requestId": "req_011CbEUCd3fdca7w4KVwpDLH",
  "type": "assistant",
  "uuid": "e4fa16c5-4b8b-417f-8ca6-264b041a4b4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115VF35LWoS8nevg8inTo9h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11481,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11481,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11481
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

_source line 9 · 2026-05-20T20:42:04.005Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Fb2Nq1eaLMwCxj6ZiKFGKm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4fa16c5-4b8b-417f-8ca6-264b041a4b4e",
  "isSidechain": false,
  "requestId": "req_011CbEUCd3fdca7w4KVwpDLH",
  "type": "assistant",
  "uuid": "cd0d9b5d-2573-48b3-8211-8904077c202b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115VF35LWoS8nevg8inTo9h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11481,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11481,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11481
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

_source line 10 · 2026-05-20T20:42:04.020Z_

<details><summary>↩ Tool result · `toolu_01QpQTp8NaGmcmzCEbrFGCdJ`</summary>

```text
1	[
2	  {
3	    "name": "Full Pareto Frontier — Qwen3-235B-A22B",
4	    "description": "94-layer MoE model, INT8, 24 probed layers (every 4th), 20 languages, 5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR).\n",
5	    "results": {
6	      "en_best_auroc": 0.838,
7	      "en_best_layer": 76,
8	      "en_best_ece_raw": 0.162,
9	      "en_best_ece_tempcal": 0.048,
10	      "temp_scaling_T": 4.83,
11	      "en_auroc_range": [
12	        0.592,
13	        0.838
14	      ],
15	      "optimal_transfer_layer_median": 56,
16	      "zs_transfer_auroc_median_20lang": 0.758,
17	      "zs_transfer_auroc_at_en_optimal_layer76": 0.714,
18	      "zs_transfer_auroc_at_transfer_optimal_layer56": 0.771,
19	      "pareto_rho_global": -0.81,
20	      "pareto_rho_per_lang_median": -0.78,
21	      "pareto_rho_per_lang_iqr": [
22	        -0.84,
23	        -0.71
24	      ],
25	      "zs_langs_above_0p65_out_of_20": 17,
26	      "best_zs_auroc_by_tier": {
27	        "HIGH_zh": 0.793,
28	        "HIGH_es": 0.801,
29	        "HIGH_fr": 0.798,
30	        "HIGH_de": 0.784,
31	        "MID_hi": 0.742,
32	        "MID_ru": 0.769,
33	        "MID_ko": 0.751,
34	        "MID_tr": 0.738,
35	        "LOW_sw": 0.641,
36	        "LOW_bn": 0.633
37	      },
38	      "mean_shift_delta_auroc_median": 0.0,
39	      "linear_proj_delta_auroc_over_zs_median": 0.048,
40	      "fewshot_25_delta_auroc_over_zs_median": 0.032,
41	      "fewshot_100_delta_auroc_over_zs_median": 0.055
42	    },
43	    "tables": [
44	      {
45	        "name": "Table 1: Qwen3-235B Pareto Frontier — EN AUROC vs ZS Transfer AUROC by Layer",
46	        "columns": [
47	          "layer",
48	          "depth_pct",
49	          "en_auroc",
50	          "zs_median_auroc",
51	          "zs_min_auroc",
52	          "zs_max_auroc",
53	          "rho_median"
54	        ],
55	        "rows": [
56	          [
57	            0,
58	            0,
59	            0.592,
60	            0.583,
61	            0.521,
62	            0.601,
63	            null
64	          ],
65	          [
66	            8,
67	            9,
68	            0.631,
69	            0.618,
70	            0.554,
71	            0.639,
72	            null
73	          ],
74	          [
75	            16,
76	            17,
77	            0.672,
78	            0.659,
79	            0.589,
80	            0.678,
81	            null
82	          ],
83	          [
84	            24,
85	            26,
86	            0.711,
87	            0.698,
88	            0.621,
89	            0.719,
90	            null
91	          ],
92	          [
93	            32,
94	            34,
95	            0.738,
96	            0.729,
97	            0.648,
98	            0.751,
99	            null
100	          ],
101	          [
102	            40,
103	            43,
104	            0.762,
105	            0.756,
106	            0.662,
107	            0.778,
108	            null
109	          ],
110	          [
111	            48,
112	            51,
113	            0.781,
114	            0.771,
115	            0.658,
116	            0.793,
117	            null
118	          ],
119	          [
120	            56,
121	            60,
122	            0.798,
123	            0.771,
124	            0.641,
125	            0.801,
126	            null
127	          ],
128	          [
129	            60,
130	            64,
131	            0.808,
132	            0.762,
133	            0.632,
134	            0.796,
135	            null
136	          ],
137	          [
138	            64,
139	            68,
140	            0.816,
141	            0.751,
142	            0.618,
143	            0.788,
144	            null
145	          ],
146	          [
147	            68,
148	            72,
149	            0.824,
150	            0.741,
151	            0.607,
152	            0.779,
153	            null
154	          ],
155	          [
156	            72,
157	            77,
158	            0.831,
159	            0.728,
160	            0.598,
161	            0.768,
162	            null
163	          ],
164	          [
165	            76,
166	            81,
167	            0.838,
168	            0.714,
169	            0.584,
170	            0.756,
171	            null
172	          ],
173	          [
174	            80,
175	            85,
176	            0.835,
177	            0.702,
178	            0.571,
179	            0.742,
180	            null
181	          ],
182	          [
183	            84,
184	            89,
185	            0.829,
186	            0.688,
187	            0.558,
188	            0.729,
189	            null
190	          ],
191	          [
192	            88,
193	            94,
194	            0.818,
195	            0.671,
196	            0.542,
197	            0.712,
198	            null
199	          ],
200	          [
201	            92,
202	            98,
203	            0.801,
204	            0.649,
205	            0.523,
206	            0.694,
207	            null
208	          ]
209	        ]
210	      },
211	      {
212	        "name": "Table 2: Qwen3-235B Transfer Conditions at Fixed Layers (layer 56 + layer 76)",
213	        "columns": [
214	          "condition",
215	          "layer56_median_auroc",
216	          "layer76_median_auroc",
217	          "delta_vs_zs_l56",
218	          "delta_vs_zs_l76"
219	        ],
220	        "rows": [
221	          [
222	            "zero-shot",
223	            0.771,
224	            0.714,
225	            0.0,
226	            0.0
227	          ],
228	          [
229	            "mean-shift",
230	            0.771,
231	            0.714,
232	            0.0,
233	            0.0
234	          ],
235	          [
236	            "linear_proj_50pairs",
237	            0.812,
238	            0.779,
239	            0.041,
240	            0.065
241	          ],
242	          [
243	            "fewshot_25",
244	            0.798,
245	            0.761,
246	            0.027,
247	            0.047
248	          ],
249	          [
250	            "fewshot_100",
251	            0.821,
252	            0.792,
253	            0.05,
254	            0.078
255	          ],
256	          [
257	            "CaCLR_full",
258	            0.828,
259	            0.788,
260	            0.057,
261	            0.074
262	          ]
263	        ]
264	      }
265	    ],
266	    "figures": [],
267	    "analysis": "Pareto frontier 在 Qwen3-235B 上形态清晰。拐点在 layer 56（60% depth）—— 此后EN AUROC继续上升但ZS transfer开始下降。MoE架构的expert routing在深层 更加language-specific是造成Pareto tradeoff的主要机制。High-resource语言 （zh/es/fr/de）的frontier更靠右上方，因为这些语言在pretraining中获得更多 token coverage，deep-layer representation与EN的对齐更好。Low-resource（sw/bn） 即使在最优transfer层也仅达到0.64左右，符合H-divergence理论预测。\n\n\nQwen3-235B-A22B的94层深度和MoE架构产生了强correctness信号。235B参数量使EN AUROC达到0.838， 远超7B MVP的0.754——更大模型的内部表征更丰富、correctness方向更可分离。 Pareto frontier清晰存在：layer 76（81%深度）是EN最优但跨语言transfer在此处下降约5.7pp （从layer 56的0.771降至0.714），因为深层表征越来越language-specific。 MoE架构中expert routing在深层更加language-dependent，强化了这一效应。 Spearman rho中位数-0.78反映depth-transfer反相关在绝大多数语言中一致。 17/20语言ZS AUROC>0.65体现了235B模型强大的multilingual representation—— 仅sw/bn/my三个极低资源语言未达标，符合Ben-David H-divergence理论预测。 Mean-shift ΔAUROC=0.000由rank-invariance定理保证（StandardScaler + logistic regression下 mean-shift仅添加常数偏移，不改变rank order）。 Linear projection作为强baseline（+4.8pp）反映correctness方向在语言间存在可学习的线性映射关系。\n"
268	  },
269	  {
270	    "name": "Full Pareto Frontier — Llama 4 Scout",
271	    "description": "48-layer MoE model, INT8, 12 probed layers (every 4th), 20 languages, 5 transfer conditions.\n",
272	    "results": {
273	      "en_best_auroc": 0.821,
274	      "en_best_layer": 40,
275	      "en_best_ece_raw": 0.171,
276	      "en_best_ece_tempcal": 0.053,
277	      "temp_scaling_T": 5.12,
278	      "en_auroc_range": [
279	        0.604,
280	        0.821
281	      ],
282	      "optimal_transfer_layer_median": 24,
283	      "zs_transfer_auroc_median_20lang": 0.742,
284	      "zs_transfer_auroc_at_en_optimal_layer40": 0.698,
285	      "zs_transfer_auroc_at_transfer_optimal_layer24": 0.756,
286	      "pareto_rho_global": -0.76,
287	      "pareto_rho_per_lang_median": -0.73,
288	      "pareto_rho_per_lang_iqr": [
289	        -0.81,
290	        -0.66
291	      ],
292	      "zs_langs_above_0p65_out_of_20": 16,
293	      "best_zs_auroc_by_tier": {
294	        "HIGH_zh": 0.778,
295	        "HIGH_es": 0.789,
296	        "HIGH_fr": 0.781,
297	        "HIGH_de": 0.772,
298	        "MID_hi": 0.728,
299	        "MID_ru": 0.756,
300	        "MID_ko": 0.739,
301	        "MID_tr": 0.721,
302	        "LOW_sw": 0.628,
303	        "LOW_bn": 0.618
304	      },
305	      "mean_shift_delta_auroc_median": 0.0,
306	      "linear_proj_delta_auroc_over_zs_median": 0.044
307	    },
308	    "tables": [
309	      {
310	        "name": "Table 3: Llama 4 Scout Pareto Frontier",
311	        "columns": [
312	          "layer",
313	          "depth_pct",
314	          "en_auroc",
315	          "zs_median_auroc"
316	        ],
317	        "rows": [
318	          [
319	            0,
320	            0,
321	            0.604,
322	            0.592
323	          ],
324	          [
325	            4,
326	            8,
327	            0.638,
328	            0.624
329	          ],
330	          [
331	            8,
332	            17,
333	            0.674,
334	            0.661
335	          ],
336	          [
337	            12,
338	            25,
339	            0.712,
340	            0.701
341	          ],
342	          [
343	            16,
344	            33,
345	            0.741,
346	            0.738
347	          ],
348	          [
349	            20,
350	            42,
351	            0.768,
352	            0.756
353	          ],
354	          [
355	            24,
356	            50,
357	            0.788,
358	            0.756
359	          ],
360	          [
361	            28,
362	            58,
363	            0.801,
364	            0.742
365	          ],
366	          [
367	            32,
368	            67,
369	            0.811,
370	            0.726
371	          ],
372	          [
373	            36,
374	            75,
375	            0.818,
376	            0.711
377	          ],
378	          [
379	            40,
380	            83,
381	            0.821,
382	            0.698
383	          ],
384	          [
385	            44,
386	            92,
387	            0.814,
388	            0.679
389	          ],
390	          [
391	            48,
392	            100,
393	            0.798,
394	            0.654
395	          ]
396	        ]
397	      }
398	    ],
399	    "figures": [],
400	    "analysis": "两个架构的Pareto frontier在归一化深度上呈现不同形状：Qwen3-235B的拐点在60%深度， Scout在50%深度。这一差异不能由模型大小alone解释（两者都是MoE）， 而是反映了训练数据分布、expert routing策略和层归一化实现的差异。 Scout在每层的language specialization更剧烈，导致frontier更陡峭、拐点更早。 这是论文最核心的发现之一：optimal transfer depth不是universal的，必须per-architecture确定。\n\n\nLlama 4 Scout的48层架构使optimal transfer层在50%深度（layer 24）， 而Qwen3-235B在60%深度（layer 56）——这就是architecture-dependent shape的关键证据。 Scout的层数不到Qwen的一半，deep层的language specialization发生得更快（按比例）。 EN best AUROC=0.821略低于Qwen的0.838，反映Scout虽然是MoE但active参数更少。 ZS median 0.742 vs Qwen的0.758，差距16pp体现了Llama系列multilingual pretraining 数据在低资源语言上的相对弱势。Pareto rho中位数-0.73略弱于Qwen的-0.78， 因为Scout只有12个probed层，frontier采样更粗糙。16/20语言>0.65（vs Qwen 17/20）， sw/bn/my/jv四个低资源语言未达标。Architecture-dependent差异是本文Claim 1的核心发现。\n"
401	  },
402	  {
403	    "name": "CaCLR Implementation and Comparative Evaluation",
404	    "description": "CaCLR (L_BCE + α·L_SB-ECE + β·L_MMD) 训练、超参数sweep、与所有baseline的全面比较。 Path A: β term provides meaningful gain.\n",
405	    "results": {
406	      "caclr_optimal_alpha": 1.0,
407	      "caclr_optimal_beta": 0.1,
408	      "caclr_beta_delta_auroc_over_alpha_only_median": 0.032,
409	      "caclr_beta_delta_auroc_over_alpha_only_range": [
410	        0.018,
411	        0.051
412	      ],
413	      "caclr_full_delta_auroc_over_zeroshot_median": 0.062,
414	      "caclr_full_delta_auroc_over_zeroshot_range": [
415	        0.031,
416	        0.098
417	      ],
418	      "caclr_vs_linear_proj_delta_median": 0.014,
419	      "caclr_vs_fewshot100_delta_median": -0.008,
420	      "ece_reduction_vs_temp_scaling_median": 0.035,
421	      "ece_reduction_vs_temp_scaling_range": [
422	        0.012,
423	        0.061
424	      ],
425	      "beta_sweep_results": {
426	        "beta_0.001": {
427	          "delta_auroc_over_alpha_only": 0.008,
428	          "note": "too weak"
429	        },
430	        "beta_0.01": {
431	          "delta_auroc_over_alpha_only": 0.019,
432	          "note": "marginal"
433	        },
434	        "beta_0.1": {
435	          "delta_auroc_over_alpha_only": 0.032,
436	          "note": "optimal"
437	        },
438	        "beta_1.0": {
439	          "delta_auroc_over_alpha_only": 0.021,
440	          "note": "overfitting to distributional match"
441	        }
442	      },
443	      "alpha_sweep_results": {
444	        "alpha_0.01": {
445	          "en_ece": 0.068,
446	          "transfer_auroc_median": 0.779
447	        },
448	        "alpha_0.1": {
449	          "en_ece": 0.055,
450	          "transfer_auroc_median": 0.793
451	        },
452	        "alpha_1.0": {
453	          "en_ece": 0.041,
454	          "transfer_auroc_median": 0.808
455	        },
456	        "alpha_10.0": {
457	          "en_ece": 0.038,
458	          "transfer_auroc_median": 0.791
459	        }
460	      },
461	      "layer_interaction": {
462	        "mid_depth_beta_gain": 0.041,
463	        "deep_layer_beta_gain": 0.024,
464	        "shallow_layer_beta_gain": 0.018
465	      },
466	      "qwen_results": {
467	        "layer56_caclr_full_median": 0.828,
468	        "layer76_caclr_full_median": 0.788
469	      },
470	      "scout_results": {
471	        "layer24_caclr_full_median": 0.812,
472	        "layer40_caclr_full_median": 0.771
473	      },
474	      "bootstrap_ci_beta_effect": [
475	        0.019,
476	        0.045
477	      ],
478	      "paired_permutation_p_beta": 0.003,
479	      "cohens_d_beta": 0.48
480	    },
481	    "tables": [
482	      {
483	        "name": "Table 4: Transfer Method Comparison (Median AUROC across 20 languages, both models)",
484	        "columns": [
485	          "method",
486	          "labels_needed",
487	          "qwen_layer56",
488	          "qwen_layer76",
489	          "scout_layer24",
490	          "scout_layer40",
491	          "median_all"
492	        ],
493	        "rows": [
494	          [
495	            "zero-shot",
496	            0,
497	            0.771,
498	            0.714,
499	            0.756,
500	            0.698,
501	            0.735
502	          ],
503	          [
504	            "mean-shift",
505	            0,
506	            0.771,
507	            0.714,
508	            0.756,
509	            0.698,
510	            0.735
511	          ],
512	          [
513	            "CaCLR_alpha_only",
514	            "0 (parallel inputs)",
515	            0.798,
516	            0.762,
517	            0.784,
518	            0.745,
519	            0.772
520	          ],
521	          [
522	            "CaCLR_full",
523	            "0 (parallel inputs)",
524	            0.828,
525	            0.788,
526	            0.812,
527	            0.771,
528	            0.8
529	          ],
530	          [
531	            "linear_proj_50",
532	            "50 parallel pairs",
533	            0.812,
534	            0.779,
535	            0.798,
536	            0.758,
537	            0.787
538	          ],
539	          [
540	            "fewshot_25",
541	            25,
542	            0.798,
543	            0.761,
544	            0.781,
545	            0.741,
546	            0.77
547	          ],
548	          [
549	            "fewshot_100",
550	            100,
551	            0.821,
552	            0.792,
553	            0.808,
554	            0.778,
555	            0.8
556	          ]
557	        ]
558	      },
559	      {
560	        "name": "Table 5: β Sensitivity Sweep (Qwen3-235B, layer 56, median across 20 langs)",
561	        "columns": [
562	          "beta",
563	          "delta_auroc_over_alpha_only",
564	          "delta_ece_over_alpha_only",
565	          "note"
566	        ],
567	        "rows": [
568	          [
569	            0.001,
570	            0.008,
571	            -0.003,
572	            "negligible distributional constraint"
573	          ],
574	          [
575	            0.01,
576	            0.019,
577	            -0.008,
578	            "marginal improvement"
579	          ],
580	          [
581	            0.1,
582	            0.032,
583	            -0.014,
584	            "optimal — balances alignment and prediction"
585	          ],
586	          [
587	            1.0,
588	            0.021,
589	            -0.011,
590	            "over-regularized — MMD dominates loss"
591	          ]
592	        ]
593	      }
594	    ],
595	    "figures": [],
596	    "analysis": "CaCLR的consistency loss在mid-depth层效果最好，这与CKA分析（plan_011）一致： mid-depth层的cross-lingual表征相似度足够高让MMD有效对齐，但已经有enough language-specific分化使得对齐产生实际收益。β=0.1的inverted-U曲线说明 distributional matching存在sweet spot——太弱无效，太强则牺牲correctness prediction。 CaCLR vs fewshot_100的near-parity（-0.8pp）是重要结果：CaCLR达到了接近 100-label supervised的性能，但不需要任何target-language correctness labels。 统计显著性（p=0.003, d=0.48）确保β效应不是噪声。\n\n\nCaCLR consistency loss (β term) 提供了有意义的增益（中位数+3.2pp over α-only）， 支持Path A叙事。β=0.1是最优点——更低（0.001-0.01）则MMD约束太弱无法对齐分布， 更高（1.0）则过度约束导致correctness prediction损失。 β增益在mid-depth层（40-60%）最大（+4.1pp），因为这些层的cross-lingual表征 仍有足够的共享结构让MMD可以有效对齐，但已经开始出现分化需要对齐。 在deep层β增益下降到+2.4pp，因为表征的geometric misalignment（非仅distributional shift） 限制了MMD的有效性——但CaCLR仍然比zero-shot好得多。 CaCLR vs linear projection：CaCLR赢1.4pp中位数，因为它同时优化calibration（α项） 和alignment（β项），而linear projection仅做alignment。但CaCLR略输于few-shot 100 （-0.8pp），因为100个标注样本提供了直接的target-language correctness信号。 关键：CaCLR不需要target-language labels，这是实际场景中的核心优势。 ECE reduction vs temp scaling中位数3.5pp，因为CaCLR在训练时直接优化SB-ECE， 而temp scaling仅做post-hoc rescaling无法修复表征层面的miscalibration。 Bootstrap CI [0.019, 0.045]和p=0.003确认β效应统计显著；Cohen's d=0.48为中等效应量。\n"
597	  },
598	  {
599	    "name": "Difficulty-Controlled Decomposition Ablation",
600	    "description": "IRT difficulty probes → project out difficulty → retrain correctness probes → evaluate transfer. 10 languages × 8 layers × 2 models.\n",
601	    "results": {
602	      "decomposition_transfer_delta_after_difficulty_removal_median": 0.031,
603	      "decomposition_transfer_delta_range": [
604	        0.011,
605	        0.052
606	      ],
607	      "difficulty_probe_r2_median": 0.68,
608	      "difficulty_direction_cosine_with_correctness": 0.34,
609	      "capability_specific_transfer_degradation_per_depth": {
610	        "shallow_20pct": 0.008,
611	        "mid_50pct": 0.024,
612	        "deep_80pct": 0.048
613	      },
614	      "random_direction_control_delta": 0.002,
615	      "resource_tier_pattern": {
616	        "HIGH_delta": 0.022,
617	        "MID_delta": 0.033,
618	        "LOW_delta": 0.041
619	      },
620	      "bootstrap_ci_decomposition_delta": [
621	        0.018,
622	        0.044
623	      ],
624	      "paired_permutation_p": 0.006,
625	      "cohens_d": 0.41
626	    },
627	    "tables": [
628	      {
629	        "name": "Table 6: Decomposition Effect by Resource Tier and Depth (ΔAUROC after difficulty removal)",
630	        "columns": [
631	          "depth_pct",
632	          "HIGH_avg",
633	          "MID_avg",
634	          "LOW_avg",
635	          "random_control"
636	        ],
637	        "rows": [
638	          [
639	            20,
640	            0.012,
641	            0.014,
642	            0.019,
643	            0.001
644	          ],
645	          [
646	            35,
647	            0.016,
648	            0.022,
649	            0.028,
650	            0.002
651	          ],
652	          [
653	            50,
654	            0.021,
655	            0.031,
656	            0.038,
657	            0.002
658	          ],
659	          [
660	            60,
661	            0.024,
662	            0.036,
663	            0.043,
664	            0.003
665	          ],
666	          [
667	            70,
668	            0.026,
669	            0.039,
670	            0.046,
671	            0.002
672	          ],
673	          [
674	            80,
675	            0.028,
676	            0.041,
677	            0.048,
678	            0.003
679	          ],
680	          [
681	            85,
682	            0.025,
683	            0.038,
684	            0.044,
685	            0.002
686	          ],
687	          [
688	            90,
689	            0.022,
690	            0.034,
691	            0.041,
692	            0.002
693	          ]
694	        ]
695	      }
696	    ],
697	    "figures": [],
698	    "analysis": "Decomposition结果支持Claim 2：difficulty和capability在correctness方向中可分离， 且分离后capability-specific信号的cross-lingual transfer一致改善。 关键insight是resource tier gradient——低资源语言的difficulty entanglement最严重， 也从decomposition中获益最多。这为CaCLR提供了theoretical motivation： CaCLR的consistency loss本质上在做distributional alignment of capability-specific signals。 Random-direction control（~0pp）是关键的methodological guard rail。\n\n\nDifficulty direction与correctness direction有中等cosine（0.34），说明两者共享 部分信号但不完全重叠。Project out difficulty后，残差中的correctness信号更 \"capability-pure\"——这个信号在高资源语言间更容易transfer（+2.2pp）， 因为capability-specific failures在这些语言间更一致。低资源语言获益最大（+4.1pp）， 因为原始correctness方向中difficulty成分占比更高（低资源语言的difficulty分布 与EN差异更大），去除difficulty后暴露出更可transfer的capability信号。 深层退化更明显（4.8pp）因为深层同时编码了更多language-specific的difficulty信息。 Random-direction control仅+0.2pp，排除了dimensionality reduction artifact—— 是difficulty方向的specific removal而非arbitrary降维带来的改善。 这个分解是prescriptive的：它告诉我们哪些language-layer组合需要capability alignment （高delta = 高difficulty entanglement = 需要CaCLR/projection）。\n"
699	  },
700	  {
701	    "name": "Cross-Lingual Orthogonality Analysis",
702	    "description": "Correctness-confidence cosine similarity across 20 languages × 2 architectures, analyzed by resource tier and language family.\n",
703	    "results": {
704	      "orthogonality_cosine_mean_across_langs": 0.042,
705	      "orthogonality_cosine_max_across_langs": 0.062,
706	      "orthogonality_cosine_min_across_langs": 0.018,
707	      "orthogonality_cosine_std": 0.013,
708	      "cosine_by_tier": {
709	        "HIGH_mean": 0.038,
710	        "MID_mean": 0.043,
711	        "LOW_mean": 0.051
712	      },
713	      "cosine_by_architecture": {
714	        "qwen_mean": 0.039,
715	        "scout_mean": 0.046
716	      },
717	      "cosine_range_qwen_20lang": [
718	        0.018,
719	        0.058
720	      ],
721	      "cosine_range_scout_20lang": [
722	        0.022,
723	        0.062
724	      ],
725	      "all_20_langs_below_0p08": true,
726	      "bootstrap_ci_mean_cosine": [
727	        0.035,
728	        0.049
729	      ]
730	    },
731	    "tables": [
732	      {
733	        "name": "Table 7: Correctness-Confidence Cosine Similarity by Language",
734	        "columns": [
735	          "language",
736	          "tier",
737	          "qwen_cosine",
738	          "scout_cosine",
739	          "mean"
740	        ],
741	        "rows": [
742	          [
743	            "en",
744	            "HIGH",
745	            0.031,
746	            0.037,
747	            0.034
748	          ],
749	          [
750	            "zh",
751	            "HIGH",
752	            0.035,
753	            0.041,
754	            0.038
755	          ],
756	          [
757	            "es",
758	            "HIGH",
759	            0.033,
760	            0.039,
761	            0.036
762	          ],
763	          [
764	            "fr",
765	            "HIGH",
766	            0.034,
767	            0.04,
768	            0.037
769	          ],
770	          [
771	            "de",
772	            "HIGH",
773	            0.036,
774	            0.042,
775	            0.039
776	          ],
777	          [
778	            "hi",
779	            "MID",
780	            0.039,
781	            0.045,
782	            0.042
783	          ],
784	          [
785	            "ru",
786	            "MID",
787	            0.037,
788	            0.043,
789	            0.04
790	          ],
791	          [
792	            "ko",
793	            "MID",
794	            0.041,
795	            0.047,
796	            0.044
797	          ],
798	          [
799	            "tr",
800	            "MID",
801	            0.043,
802	            0.049,
803	            0.046
804	          ],
805	          [
806	            "sw",
807	            "LOW",
808	            0.048,
809	            0.056,
810	            0.052
811	          ],
812	          [
813	            "bn",
814	            "LOW",
815	            0.052,
816	            0.058,
817	            0.055
818	          ]
819	        ]
820	      }
821	    ],
822	    "figures": [],
823	    "analysis": "Cross-lingual orthogonality的universal persistence是论文的bounding contribution。 它回答了\"为什么需要probe-based calibration\"：因为output-based方法在结构上 无法获取correctness信息（cosine<0.08），无论语言。Resource tier gradient 是nuanced finding但不影响main conclusion。\n\n\nOrthogonality在所有20语言 × 2架构上持续存在（max cosine 0.062 < 0.08阈值）， 确认Miao & Ungar (2026)的English-only发现是universal structural property。 Low-resource语言cosine略高（0.051 vs HIGH 0.038），因为这些语言的confidence probe quality更低（更少训练数据→confidence方向估计噪声更大→与correctness的 apparent cosine被噪声inflate）。但即使是最高的0.062也远低于non-orthogonal阈值， 说明output-based calibration在结构上受限不依赖于语言。 Qwen略比Scout更orthogonal（0.039 vs 0.046），可能反映Qwen更大的模型容量 使correctness和confidence能被编码在更分离的子空间中。 这个发现bounds entire output-based calibration approach：无论语言或架构， verbalized confidence不包含correctness信息，motivating probe-based方法。\n"
824	  },
825	  {
826	    "name": "Probe Complexity Comparison",
827	    "description": "Logistic regression vs 2-layer MLP across all probed layers, both models. EN accuracy, cross-lingual transfer degradation, calibration comparison.\n",
828	    "results": {
829	      "lr_en_best_auroc_qwen": 0.838,
830	      "mlp_en_best_auroc_qwen": 0.852,
831	      "lr_en_best_auroc_scout": 0.821,
832	      "mlp_en_best_auroc_scout": 0.834,
833	      "lr_zs_transfer_degradation_median": 0.068,
834	      "mlp_zs_transfer_degradation_median": 0.104,
835	      "lr_transfer_advantage_over_mlp_median": 0.022,
836	      "lr_ece_vs_mlp_ece": [
837	        -0.008,
838	        0.003
839	      ],
840	      "mlp_overfit_indicator_deep_layers": true
841	    },
842	    "tables": [
843	      {
844	        "name": "Table 8: Probe Complexity — EN AUROC vs ZS Transfer (Qwen3-235B, selected layers)",
845	        "columns": [
846	          "layer",
847	          "lr_en",
848	          "mlp_en",
849	          "lr_zs_median",
850	          "mlp_zs_median",
851	          "lr_transfer_advantage"
852	        ],
853	        "rows": [
854	          [
855	            24,
856	            0.711,
857	            0.722,
858	            0.698,
859	            0.691,
860	            0.007
861	          ],
862	          [
863	            40,
864	            0.762,
865	            0.778,
866	            0.756,
867	            0.741,
868	            0.015
869	          ],
870	          [
871	            56,
872	            0.798,
873	            0.814,
874	            0.771,
875	            0.752,
876	            0.019
877	          ],
878	          [
879	            76,
880	            0.838,
881	            0.852,
882	            0.714,
883	            0.686,
884	            0.028
885	          ]
886	        ]
887	      }
888	    ],
889	    "figures": [],
890	    "analysis": "Linear probe是正确的default choice。MLP的EN优势被transfer劣势完全抵消。 这个结果also间接支持correctness direction是线性的——linear probe已经捕获了 大部分信号，MLP额外捕获的主要是noise/language-specific artifact。\n\n\nLinear probes在EN AUROC上略输MLP（~1.4pp），但在cross-lingual transfer上 显著更好（+2.2pp median）。MLP的额外容量捕获了EN-specific patterns导致更多 overfitting to source language——这些patterns在target语言中不泛化。 这与probe complexity literature一致（Hewitt & Liang 2019）：更强的probe 在source domain表现更好但generalization更差。Linear probe的inductive bias （只能学习线性可分方向）恰好与correctness direction的线性结构匹配， 同时限制了对language-specific artifacts的拟合。 在deep层这个差异更大（MLP overfitting更严重），因为deep层表征更language-specific。 这个结果support使用logistic regression作为primary probe的选择。\n"
891	  },
892	  {
893	    "name": "Additional Benchmark Evaluation (Belebele + MMLU-ProX)",
894	    "description": "Best probes + CaCLR在Belebele和MMLU-ProX上的评估，验证beyond-GlobalMMLU泛化。\n",
895	    "results": {
896	      "belebele_zs_auroc_median": 0.731,
897	      "belebele_caclr_auroc_median": 0.789,
898	      "mmlu_prox_zs_auroc_median": 0.748,
899	      "mmlu_prox_caclr_auroc_median": 0.801,
900	      "cross_benchmark_correlation": 0.92,
901	      "belebele_pareto_rho_median": -0.71,
902	      "mmlu_prox_pareto_rho_median": -0.75
903	    },
904	    "tables": [
905	      {
906	        "name": "Table 9: Cross-Benchmark Generalization (Qwen3-235B, optimal transfer layer)",
907	        "columns": [
908	          "benchmark",
909	          "zs_median",
910	          "caclr_median",
911	          "pareto_rho",
912	          "langs_above_0p65"
913	        ],
914	        "rows": [
915	          [
916	            "GlobalMMLU",
917	            0.758,
918	            0.808,
919	            -0.78,
920	            17
921	          ],
922	          [
923	            "Belebele",
924	            0.731,
925	            0.789,
926	            -0.71,
927	            15
928	          ],
929	          [
930	            "MMLU-ProX",
931	            0.748,
932	            0.801,
933	            -0.75,
934	            16
935	          ]
936	        ]
937	      }
938	    ],
939	    "figures": [],
940	    "analysis": "Cross-benchmark泛化confirm findings are not benchmark-specific artifact。 Pareto frontier在三个benchmark上一致存在但shape有细微差异—— Belebele更浅的optimal depth可能反映reading comprehension使用了更浅层的表征。\n\n\nBelebele（reading comprehension）的ZS AUROC略低于GlobalMMLU（0.731 vs 0.758）， 因为不同任务的correctness信号分布不完全一致——但Pareto frontier仍然存在 （rho=-0.71），说明depth-transfer tradeoff是task-general的。 MMLU-ProX与GlobalMMLU最相似（同为knowledge QA），所以结果最接近（0.748 vs 0.758）。 CaCLR在两个benchmark上都提供了consistent improvement（+5.3-5.8pp）， 说明CaCLR学到的alignment不是GlobalMMLU-specific的。 Cross-benchmark correlation 0.92表明per-language transfer difficulty在benchmarks间高度一致—— sw/bn在所有benchmarks上都最难transfer，zh/es在所有benchmarks上都最容易。\n"
941	  },
942	  {
943	    "name": "INT8 Validation Ablation",
944	    "description": "INT8 vs FP16对比，Llama 4 Scout，5 representative layers，5% random subset。\n",
945	    "results": {
946	      "int8_fp16_auroc_max_diff": 0.006,
947	      "int8_fp16_auroc_mean_diff": 0.003,
948	      "int8_fp16_ece_max_diff": 0.008,
949	      "int8_fp16_direction_cosine_min": 0.987,
950	      "all_diffs_within_noise": true
951	    },
952	    "tables": [
953	      {
954	        "name": "Table S1: INT8 vs FP16 Comparison (Llama 4 Scout)",
955	        "columns": [
956	          "layer",
957	          "int8_auroc",
958	          "fp16_auroc",
959	          "diff",
960	          "direction_cosine"
961	        ],
962	        "rows": [
963	          [
964	            8,
965	            0.674,
966	            0.678,
967	            -0.004,
968	            0.991
969	          ],
970	          [
971	            16,
972	            0.741,
973	            0.745,
974	            -0.004,
975	            0.989
976	          ],
977	          [
978	            24,
979	            0.788,
980	            0.791,
981	            -0.003,
982	            0.992
983	          ],
984	          [
985	            32,
986	            0.811,
987	            0.814,
988	            -0.003,
989	            0.99
990	          ],
991	          [
992	            40,
993	            0.821,
994	            0.827,
995	            -0.006,
996	            0.987
997	          ]
998	        ]
999	      }
1000	    ],
1001	    "figures": [],
1002	    "analysis": "INT8量化不distort correctness signals。所有差异在bootstrap noise范围内。 Deep层差异略大（layer 40: 0.6pp）符合预期——深层表征更complex，量化误差累积更多。 但0.6pp远小于实验效应（CaCLR +6pp），不影响任何结论。\n\n\nINT8量化对correctness direction的影响极小（max AUROC差异0.6pp）， 因为correctness信号是高SNR的线性方向——量化噪声主要影响低幅度维度， 而correctness direction在high-variance维度上有强projection。 Direction cosine>0.987说明INT8和FP16下提取的correctness方向几乎相同。 ECE差异稍大（0.8pp）因为calibration对probability scale更敏感，但仍在噪声范围内。 这排除了\"INT8 artifact\"的reviewer concern。\n"
1003	  },
1004	  {
1005	    "name": "CKA Cross-Lingual Representation Similarity",
1006	    "description": "CKA (linear kernel) between EN and each target language at every probed layer, correlated with transfer AUROC. Mechanistic explanation for Pareto frontier.\n",
1007	    "results": {
1008	      "cka_transfer_pearson_r": 0.82,
1009	      "cka_transfer_pearson_r_ci": [
1010	        0.76,
1011	        0.87
1012	      ],
1013	      "cka_transfer_spearman_rho": 0.79,
1014	      "cka_en_zh_by_depth_trend": "monotonically decreasing from 0.92 (shallow) to 0.61 (deep)",
1015	      "cka_en_sw_by_depth_trend": "monotonically decreasing from 0.84 (shallow) to 0.38 (deep)",
1016	      "cka_resource_tier_gradient": {
1017	        "HIGH_mean_cka_at_optimal_depth": 0.78,
1018	        "MID_mean_cka_at_optimal_depth": 0.71,
1019	        "LOW_mean_cka_at_optimal_depth": 0.58
1020	      },
1021	      "geometric_misalignment_evidence": "CKA drop from mid to deep layers exceeds what mean/covariance shift alone predicts. Subspace angle analysis shows correctness direction rotates 15-35° across languages at deep layers vs 5-12° at shallow layers.\n",
1022	      "cka_explains_caclr_beta_limit": "At layers where CKA < 0.55, β term provides diminishing returns because geometric misalignment (rotation) dominates distributional shift.\n"
1023	    },
1024	    "tables": [
1025	      {
1026	        "name": "Table 10: CKA by Depth and Resource Tier (Qwen3-235B)",
1027	        "columns": [
1028	          "depth_pct",
1029	          "HIGH_cka",
1030	          "MID_cka",
1031	          "LOW_cka",
1032	          "zs_auroc_median"
1033	        ],
1034	        "rows": [
1035	          [
1036	            10,
1037	            0.93,
1038	            0.89,
1039	            0.84,
1040	            0.618
1041	          ],
1042	          [
1043	            25,
1044	            0.9,
1045	            0.85,
1046	            0.78,
1047	            0.698
1048	          ],
1049	          [
1050	            40,
1051	            0.86,
1052	            0.79,
1053	            0.69,
1054	            0.756
1055	          ],
1056	          [
1057	            50,
1058	            0.82,
1059	            0.74,
1060	            0.62,
1061	            0.771
1062	          ],
1063	          [
1064	            60,
1065	            0.78,
1066	            0.69,
1067	            0.55,
1068	            0.771
1069	          ],
1070	          [
1071	            70,
1072	            0.73,
1073	            0.63,
1074	            0.47,
1075	            0.741
1076	          ],
1077	          [
1078	            80,
1079	            0.67,
1080	            0.56,
1081	            0.41,
1082	            0.714
1083	          ],
1084	          [
1085	            90,
1086	            0.61,
1087	            0.49,
1088	            0.35,
1089	            0.688
1090	          ]
1091	        ]
1092	      }
1093	    ],
1094	    "figures": [],
1095	    "analysis": "CKA analysis是论文的mechanistic backbone。它将observation（Pareto frontier） 与explanation（representation geometry变化）和method（CaCLR的作用机制与局限） 连接起来。CKA<0.55作为CaCLR β有效性的threshold是一个actionable finding—— 实践者可以用CKA预测CaCLR在哪些layer-language组合上有效。 Geometric vs distributional misalignment的区分是theoretical contribution： 它解释了为什么distributional matching（MMD/CaCLR）在mid-depth有效但在deep层递减， 而geometric alignment（linear projection）在deep层更稳定。\n\n\nCKA与transfer AUROC的高相关（r=0.82）提供了Pareto frontier的mechanistic explanation： cross-lingual表征相似度随depth monotonically下降，直接导致deep层transfer degradation。 这不是trivial的\"深层更specific\"——CKA量化了具体的相似度数值并与transfer成功率 建立了定量关系。High-resource语言在所有depth保持更高CKA（因为pretraining data overlap）， 解释了resource tier gradient。 关键insight：deep层的CKA下降不仅是distributional shift（可被MMD修正）， 还包含geometric misalignment（correctness方向在语言间旋转15-35°）。 这解释了CaCLR β term在deep层效果减弱——MMD对齐分布但不学习旋转， 而linear projection学习旋转所以在deep层更稳定。 Subspace angle analysis区分了distributional vs geometric misalignment， 为Path A narrative提供了theoretical depth：CaCLR works at mid-depth因为 那里的misalignment主要是distributional的。\n"
1096	  },
1097	  {
1098	    "name": "Linear Projection Sensitivity Analysis",
1099	    "description": "Linear projection pair count sweep (10, 20, 50, 100, 200). Both models × 5 layers × 20 languages.\n",
1100	    "results": {
1101	      "linear_proj_min_pairs_for_saturation": 35,
1102	      "saturation_criterion": "95% of 200-pair performance",
1103	      "pairs_sweep": {
1104	        "10": {
1105	          "median_auroc": 0.762,
1106	          "pct_of_200": 0.88
1107	        },
1108	        "20": {
1109	          "median_auroc": 0.778,
1110	          "pct_of_200": 0.94
1111	        },
1112	        "50": {
1113	          "median_auroc": 0.792,
1114	          "pct_of_200": 0.98
1115	        },
1116	        "100": {
1117	          "median_auroc": 0.796,
1118	          "pct_of_200": 0.99
1119	        },
1120	        "200": {
1121	          "median_auroc": 0.798,
1122	          "pct_of_200": 1.0
1123	        }
1124	      },
1125	      "low_resource_saturation_later": true,
1126	      "low_resource_min_pairs": 48,
1127	      "high_resource_min_pairs": 22
1128	    },
1129	    "tables": [
1130	      {
1131	        "name": "Table 11: Linear Projection Data Efficiency (median across 20 langs × 2 models)",
1132	        "columns": [
1133	          "n_pairs",
1134	          "median_auroc",
1135	          "delta_vs_zs",
1136	          "pct_of_200pair",
1137	          "HIGH_auroc",
1138	          "LOW_auroc"
1139	        ],
1140	        "rows": [
1141	          [
1142	            10,
1143	            0.762,
1144	            0.027,
1145	            88,
1146	            0.781,
1147	            0.638
1148	          ],
1149	          [
1150	            20,
1151	            0.778,
1152	            0.043,
1153	            94,
1154	            0.798,
1155	            0.651
1156	          ],
1157	          [
1158	            50,
1159	            0.792,
1160	            0.057,
1161	            98,
1162	            0.814,
1163	            0.664
1164	          ],
1165	          [
1166	            100,
1167	            0.796,
1168	            0.061,
1169	            99,
1170	            0.818,
1171	            0.668
1172	          ],
1173	          [
1174	            200,
1175	            0.798,
1176	            0.063,
1177	            100,
1178	            0.821,
1179	            0.671
1180	          ]
1181	        ]
1182	      }
1183	    ],
1184	    "figures": [],
1185	    "analysis": "Linear projection的data efficiency confirms它作为practical baseline的价值。 50 pairs的saturation point意味着任何有minimal translation capacity的语言 都可以使用这个方法。这也为CaCLR设定了benchmark：CaCLR需要beat 50-pair projection 才能justify its additional complexity（in best tier, CaCLR beats by +1.4pp median）。\n\n\nLinear projection在~35 pairs时达到饱和（95% of 200-pair performance）， 因为correctness方向是低维线性结构——学习一个旋转/缩放矩阵不需要很多样本。 10 pairs已经达到88%性能，说明即使极少数据也能捕获主要的geometric transformation。 50 pairs后几乎无改善（98%→100%），符合线性映射的low sample complexity理论。 Low-resource语言需要slightly more pairs（48 vs 22），因为表征空间中 correctness方向的SNR更低，需要更多样本来robustly估计映射。 整体saturation在20-50范围内，support \"≤50 parallel pairs suffice\"的claim。 这建立了linear projection作为practical baseline的地位—— 50 pairs在任何语言都容易获得（e.g., 翻译50个MCQA items）。\n"
1186	  },
1187	  {
1188	    "name": "Probing Control Tasks (Hewitt & Liang 2019)",
1189	    "description": "Random-label control probes at each layer. Selectivity = probe AUROC - control AUROC. Validates genuine correctness signal.\n",
1190	    "results": {
1191	      "control_task_auroc_range": [
1192	        0.502,
1193	        0.538
1194	      ],
1195	      "selectivity_median": 0.284,
1196	      "selectivity_min": 0.192,
1197	      "selectivity_max": 0.341,
1198	      "control_task_selectivity_min_across_langs": 0.192,
1199	      "selectivity_by_depth": {
1200	        "shallow": 0.218,
1201	        "mid": 0.294,
1202	        "deep": 0.312
1203	      },
1204	      "selectivity_by_tier": {
1205	        "HIGH": 0.301,
1206	        "MID": 0.278,
1207	        "LOW": 0.234
1208	      }
1209	    },
1210	    "tables": [
1211	      {
1212	        "name": "Table S2: Control Task Selectivity (Qwen3-235B, selected layers × languages)",
1213	        "columns": [
1214	          "layer",
1215	          "en_selectivity",
1216	          "zh_selectivity",
1217	          "sw_selectivity",
1218	          "control_auroc"
1219	        ],
1220	        "rows": [
1221	          [
1222	            16,
1223	            0.248,
1224	            0.231,
1225	            0.192,
1226	            0.512
1227	          ],
1228	          [
1229	            32,
1230	            0.281,
1231	            0.268,
1232	            0.218,
1233	            0.519
1234	          ],
1235	          [
1236	            48,
1237	            0.309,
1238	            0.292,
1239	            0.241,
1240	            0.524
1241	          ],
1242	          [
1243	            56,
1244	            0.318,
1245	            0.301,
1246	            0.248,
1247	            0.521
1248	          ],
1249	          [
1250	            76,
1251	            0.341,
1252	            0.324,
1253	            0.262,
1254	            0.538
1255	          ]
1256	        ]
1257	      }
1258	    ],
1259	    "figures": [],
1260	    "analysis": "Control task validation是methodological necessity。Selectivity最小值19.2pp 大幅超过15pp阈值，即使在最challenging的条件（low-resource × shallow layer） 也确认probe是在提取genuine signal。这让reviewer对所有downstream结果 （Pareto frontier, CaCLR, decomposition）更有信心。\n\n\nControl probe AUROC在0.50-0.54范围（near chance），selectivity中位数0.284 远超15pp minimum threshold（min=19.2pp）。这confirm probe AUROC反映 genuine correctness direction而非memorized artifacts或probe capacity。 Selectivity随depth增加（0.218→0.312），因为深层表征包含更丰富的correctness 信号而control仍在chance附近——深层probe的高AUROC不是因为probe容量过大。 Low-resource语言selectivity最低（0.234）但仍远超threshold， 说明即使低资源语言的correctness信号也是genuine的（不是noise fitting）。 这直接回应Hewitt & Liang probing methodology critique—— 我们的probes确实在提取linguistic property而非exploiting high-dimensional capacity。\n"
1261	  },
1262	  {
1263	    "name": "Gemma 4 31B Dense — Camera-Ready Extension",
1264	    "description": "Third architecture (dense, FP16), full Pareto frontier. Dense vs MoE contrast for camera-ready.\n",
1265	    "results": {
1266	      "en_best_auroc": 0.809,
1267	      "en_best_layer": 48,
1268	      "optimal_transfer_layer": 36,
1269	      "zs_transfer_auroc_median": 0.738,
1270	      "pareto_rho_median": -0.69,
1271	      "pareto_shape": "smoother frontier than MoE models — no sharp elbow",
1272	      "dense_vs_moe_key_finding": "Dense architecture shows shallower Pareto slope — transfer degrades more gradually with depth compared to MoE models. Consistent with hypothesis that expert routing accelerates language specialization.\n"
1273	    },
1274	    "tables": [
1275	      {
1276	        "name": "Table S3: Three-Architecture Comparison Summary",
1277	        "columns": [
1278	          "model",
1279	          "type",
1280	          "params",
1281	          "layers",
1282	          "en_best_auroc",
1283	          "zs_median",
1284	          "optimal_transfer_pct",
1285	          "pareto_rho"
1286	        ],
1287	        "rows": [
1288	          [
1289	            "Qwen3-235B-A22B",
1290	            "MoE",
1291	            "235B",
1292	            94,
1293	            0.838,
1294	            0.758,
1295	            60,
1296	            -0.78
1297	          ],
1298	          [
1299	            "Llama 4 Scout",
1300	            "MoE",
1301	            "109B (17B active)",
1302	            48,
1303	            0.821,
1304	            0.742,
1305	            50,
1306	            -0.73
1307	          ],
1308	          [
1309	            "Gemma 4 31B Dense",
1310	            "Dense",
1311	            "31B",
1312	            60,
1313	            0.809,
1314	            0.738,
1315	            75,
1316	            -0.69
1317	          ]
1318	        ]
1319	      }
1320	    ],
1321	    "figures": [],
1322	    "analysis": "Three-architecture comparison is the crown jewel of Claim 1。 Dense vs MoE对比provides causal insight into WHY frontiers differ—— expert routing is the mechanism driving sharp language specialization at depth.\n\n\nGemma 4 31B Dense作为dense对照提供了architectural contrast。 EN AUROC 0.809低于两个MoE模型（0.838, 0.821），反映31B dense参数<235B MoE active参数。 关键发现：dense架构的Pareto frontier更平滑（rho=-0.69 vs MoE -0.73/-0.78）， 没有MoE的sharp elbow。这是因为MoE的expert routing在深层创造了discrete language specialization（某些experts \"负责\"特定语言），而dense模型的specialization是gradual的。 这是architecture-dependent Pareto shape claim的strongest evidence。 Optimal transfer在75%深度（layer 36/48），比Qwen3浅（60%）但比Scout深（50%）， 提供了第三个data point来characterize architecture-depth relationship。\n"
1323	  },
1324	  {
1325	    "name": "Extended Language Coverage — Camera-Ready",
1326	    "description": "Expand from 20 to 50+ languages. Camera-ready extension using GlobalMMLU/Belebele full sets.\n",
1327	    "results": {
1328	      "total_languages": 52,
1329	      "zs_langs_above_0p65": 38,
1330	      "zs_auroc_median_52lang": 0.721,
1331	      "new_low_resource_findings": "Several additional low-resource languages (e.g., Yoruba, Hausa, Malagasy) show ZS AUROC 0.58-0.64, confirming resource-tier gradient extends to tail.\n",
1332	      "pareto_frontier_robust": true,
1333	      "caclr_generalizes": true,
1334	      "caclr_delta_over_zs_52lang_median": 0.058
1335	    },
1336	    "tables": [
1337	      {
1338	        "name": "Table S4: Extended Language Coverage Summary",
1339	        "columns": [
1340	          "resource_tier",
1341	          "n_langs",
1342	          "zs_auroc_median",
1343	          "caclr_median",
1344	          "delta"
1345	        ],
1346	        "rows": [
1347	          [
1348	            "HIGH",
1349	            12,
1350	            0.786,
1351	            0.828,
1352	            0.042
1353	          ],
1354	          [
1355	            "MID",
1356	            18,
1357	            0.741,
1358	            0.798,
1359	            0.057
1360	          ],
1361	          [
1362	            "LOW",
1363	            22,
1364	            0.648,
1365	            0.721,
1366	            0.073
1367	          ]
1368	        ]
1369	      }
1370	    ],
1371	    "figures": [],
1372	    "analysis": "Extended coverage是camera-ready的scale argument。核心findings在52语言上robust。 Low-resource语言从CaCLR获益最多（+7.3pp vs HIGH +4.2pp）， because these languages have the most room for improvement and CaCLR's distributional alignment compensates for sparse pretraining representation.\n\n52语言验证confirms所有findings at broader scale。ZS median从20 langs的0.758 降到52 langs的0.721，因为新增语言主要是低资源的——这是expected的composition effect。 38/52 > 0.65（73%）vs 17/20（85%），比例下降也反映低资源语言的加入。 Pareto frontier和CaCLR在所有语言上consistent，说明findings是language-general的。 Key new finding：Yoruba/Hausa等sub-Saharan African语言的ZS AUROC（0.58-0.62） 与sw/bn相当，但CaCLR对这些语言的improvement更大（+7-9pp）， 可能因为GlobalMMLU translations provide parallel data that partially bridges the representation gap for these extremely low-resource languages.\n"
1373	  }
1374	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4fa16c5-4b8b-417f-8ca6-264b041a4b4e",
  "isSidechain": false,
  "promptId": "d6812199-51cb-4f3b-a1d1-28a2f25b4592",
  "type": "user",
  "uuid": "2d13ea83-06c5-4e69-bda9-65baa37fad4b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Full Pareto Frontier — Qwen3-235B-A22B\",\n    \"description\": \"94-layer MoE model, INT8, 24 probed layers (every 4th), 20 languages, 5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR).\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.838,\n      \"en_best_layer\": 76,\n      \"en_best_ece_raw\": 0.162,\n      \"en_best_ece_tempcal\": 0.048,\n      \"temp_scaling_T\": 4.83,\n      \"en_auroc_range\": [\n        0.592,\n        0.838\n      ],\n      \"optimal_transfer_layer_median\": 56,\n      \"zs_transfer_auroc_median_20lang\": 0.758,\n      \"zs_transfer_auroc_at_en_optimal_layer76\": 0.714,\n      \"zs_transfer_auroc_at_transfer_optimal_layer56\": 0.771,\n      \"pareto_rho_global\": -0.81,\n      \"pareto_rho_per_lang_median\": -0.78,\n      \"pareto_rho_per_lang_iqr\": [\n        -0.84,\n        -0.71\n      ],\n      \"zs_langs_above_0p65_out_of_20\": 17,\n      \"best_zs_auroc_by_tier\": {\n        \"HIGH_zh\": 0.793,\n        \"HIGH_es\": 0.801,\n        \"HIGH_fr\": 0.798,\n        \"HIGH_de\": 0.784,\n        \"MID_hi\": 0.742,\n        \"MID_ru\": 0.769,\n        \"MID_ko\": 0.751,\n        \"MID_tr\": 0.738,\n        \"LOW_sw\": 0.641,\n        \"LOW_bn\": 0.633\n      },\n      \"mean_shift_delta_auroc_median\": 0.0,\n      \"linear_proj_delta_auroc_over_zs_median\": 0.048,\n      \"fewshot_25_delta_auroc_over_zs_median\": 0.032,\n      \"fewshot_100_delta_auroc_over_zs_median\": 0.055\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Qwen3-235B Pareto Frontier — EN AUROC vs ZS Transfer AUROC by Layer\",\n        \"columns\": [\n          \"layer\",\n          \"depth_pct\",\n          \"en_auroc\",\n          \"zs_median_auroc\",\n          \"zs_min_auroc\",\n          \"zs_max_auroc\",\n          \"rho_median\"\n        ],\n        \"rows\": [\n          [\n            0,\n            0,\n            0.592,\n            0.583,\n            0.521,\n            0.601,\n            null\n          ],\n          [\n            8,\n            9,\n            0.631,\n            0.618,\n            0.554,\n            0.639,\n            null\n          ],\n          [\n            16,\n            17,\n            0.672,\n            0.659,\n            0.589,\n            0.678,\n            null\n          ],\n          [\n            24,\n            26,\n            0.711,\n            0.698,\n            0.621,\n            0.719,\n            null\n          ],\n          [\n            32,\n            34,\n            0.738,\n            0.729,\n            0.648,\n            0.751,\n            null\n          ],\n          [\n            40,\n            43,\n            0.762,\n            0.756,\n            0.662,\n            0.778,\n            null\n          ],\n          [\n            48,\n            51,\n            0.781,\n            0.771,\n            0.658,\n            0.793,\n            null\n          ],\n          [\n            56,\n            60,\n            0.798,\n            0.771,\n            0.641,\n            0.801,\n            null\n          ],\n          [\n            60,\n            64,\n            0.808,\n            0.762,\n            0.632,\n            0.796,\n            null\n          ],\n          [\n            64,\n            68,\n            0.816,\n            0.751,\n            0.618,\n            0.788,\n            null\n          ],\n          [\n            68,\n            72,\n            0.824,\n            0.741,\n            0.607,\n            0.779,\n            null\n          ],\n          [\n            72,\n            77,\n            0.831,\n            0.728,\n            0.598,\n            0.768,\n            null\n          ],\n          [\n            76,\n            81,\n            0.838,\n            0.714,\n            0.584,\n            0.756,\n            null\n          ],\n          [\n            80,\n            85,\n            0.835,\n            0.702,\n            0.571,\n            0.742,\n            null\n          ],\n          [\n            84,\n            89,\n            0.829,\n            0.688,\n            0.558,\n            0.729,\n            null\n          ],\n          [\n            88,\n            94,\n            0.818,\n            0.671,\n            0.542,\n            0.712,\n            null\n          ],\n          [\n            92,\n            98,\n            0.801,\n            0.649,\n            0.523,\n            0.694,\n            null\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: Qwen3-235B Transfer Conditions at Fixed Layers (layer 56 + layer 76)\",\n        \"columns\": [\n          \"condition\",\n          \"layer56_median_auroc\",\n          \"layer76_median_auroc\",\n          \"delta_vs_zs_l56\",\n          \"delta_vs_zs_l76\"\n        ],\n        \"rows\": [\n          [\n            \"zero-shot\",\n            0.771,\n            0.714,\n            0.0,\n            0.0\n          ],\n          [\n            \"mean-shift\",\n            0.771,\n            0.714,\n            0.0,\n            0.0\n          ],\n          [\n            \"linear_proj_50pairs\",\n            0.812,\n            0.779,\n            0.041,\n            0.065\n          ],\n          [\n            \"fewshot_25\",\n            0.798,\n            0.761,\n            0.027,\n            0.047\n          ],\n          [\n            \"fewshot_100\",\n            0.821,\n            0.792,\n            0.05,\n            0.078\n          ],\n          [\n            \"CaCLR_full\",\n            0.828,\n            0.788,\n            0.057,\n            0.074\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Pareto frontier 在 Qwen3-235B 上形态清晰。拐点在 layer 56（60% depth）—— 此后EN AUROC继续上升但ZS transfer开始下降。MoE架构的expert routing在深层 更加language-specific是造成Pareto tradeoff的主要机制。High-resource语言 （zh/es/fr/de）的frontier更靠右上方，因为这些语言在pretraining中获得更多 token coverage，deep-layer representation与EN的对齐更好。Low-resource（sw/bn） 即使在最优transfer层也仅达到0.64左右，符合H-divergence理论预测。\\n\\n\\nQwen3-235B-A22B的94层深度和MoE架构产生了强correctness信号。235B参数量使EN AUROC达到0.838， 远超7B MVP的0.754——更大模型的内部表征更丰富、correctness方向更可分离。 Pareto frontier清晰存在：layer 76（81%深度）是EN最优但跨语言transfer在此处下降约5.7pp （从layer 56的0.771降至0.714），因为深层表征越来越language-specific。 MoE架构中expert routing在深层更加language-dependent，强化了这一效应。 Spearman rho中位数-0.78反映depth-transfer反相关在绝大多数语言中一致。 17/20语言ZS AUROC>0.65体现了235B模型强大的multilingual representation—— 仅sw/bn/my三个极低资源语言未达标，符合Ben-David H-divergence理论预测。 Mean-shift ΔAUROC=0.000由rank-invariance定理保证（StandardScaler + logistic regression下 mean-shift仅添加常数偏移，不改变rank order）。 Linear projection作为强baseline（+4.8pp）反映correctness方向在语言间存在可学习的线性映射关系。\\n\"\n  },\n  {\n    \"name\": \"Full Pareto Frontier — Llama 4 Scout\",\n    \"description\": \"48-layer MoE model, INT8, 12 probed layers (every 4th), 20 languages, 5 transfer conditions.\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.821,\n      \"en_best_layer\": 40,\n      \"en_best_ece_raw\": 0.171,\n      \"en_best_ece_tempcal\": 0.053,\n      \"temp_scaling_T\": 5.12,\n      \"en_auroc_range\": [\n        0.604,\n        0.821\n      ],\n      \"optimal_transfer_layer_median\": 24,\n      \"zs_transfer_auroc_median_20lang\": 0.742,\n      \"zs_transfer_auroc_at_en_optimal_layer40\": 0.698,\n      \"zs_transfer_auroc_at_transfer_optimal_layer24\": 0.756,\n      \"pareto_rho_global\": -0.76,\n      \"pareto_rho_per_lang_median\": -0.73,\n      \"pareto_rho_per_lang_iqr\": [\n        -0.81,\n        -0.66\n      ],\n      \"zs_langs_above_0p65_out_of_20\": 16,\n      \"best_zs_auroc_by_tier\": {\n        \"HIGH_zh\": 0.778,\n        \"HIGH_es\": 0.789,\n        \"HIGH_fr\": 0.781,\n        \"HIGH_de\": 0.772,\n        \"MID_hi\": 0.728,\n        \"MID_ru\": 0.756,\n        \"MID_ko\": 0.739,\n        \"MID_tr\": 0.721,\n        \"LOW_sw\": 0.628,\n        \"LOW_bn\": 0.618\n      },\n      \"mean_shift_delta_auroc_median\": 0.0,\n      \"linear_proj_delta_auroc_over_zs_median\": 0.044\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Llama 4 Scout Pareto Frontier\",\n        \"columns\": [\n          \"layer\",\n          \"depth_pct\",\n          \"en_auroc\",\n          \"zs_median_auroc\"\n        ],\n        \"rows\": [\n          [\n            0,\n            0,\n            0.604,\n            0.592\n          ],\n          [\n            4,\n            8,\n            0.638,\n            0.624\n          ],\n          [\n            8,\n            17,\n            0.674,\n            0.661\n          ],\n          [\n            12,\n            25,\n            0.712,\n            0.701\n          ],\n          [\n            16,\n            33,\n            0.741,\n            0.738\n          ],\n          [\n            20,\n            42,\n            0.768,\n            0.756\n          ],\n          [\n            24,\n            50,\n            0.788,\n            0.756\n          ],\n          [\n            28,\n            58,\n            0.801,\n            0.742\n          ],\n          [\n            32,\n            67,\n            0.811,\n            0.726\n          ],\n          [\n            36,\n            75,\n            0.818,\n            0.711\n          ],\n          [\n            40,\n            83,\n            0.821,\n            0.698\n          ],\n          [\n            44,\n            92,\n            0.814,\n            0.679\n          ],\n          [\n            48,\n            100,\n            0.798,\n            0.654\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"两个架构的Pareto frontier在归一化深度上呈现不同形状：Qwen3-235B的拐点在60%深度， Scout在50%深度。这一差异不能由模型大小alone解释（两者都是MoE）， 而是反映了训练数据分布、expert routing策略和层归一化实现的差异。 Scout在每层的language specialization更剧烈，导致frontier更陡峭、拐点更早。 这是论文最核心的发现之一：optimal transfer depth不是universal的，必须per-architecture确定。\\n\\n\\nLlama 4 Scout的48层架构使optimal transfer层在50%深度（layer 24）， 而Qwen3-235B在60%深度（layer 56）——这就是architecture-dependent shape的关键证据。 Scout的层数不到Qwen的一半，deep层的language specialization发生得更快（按比例）。 EN best AUROC=0.821略低于Qwen的0.838，反映Scout虽然是MoE但active参数更少。 ZS median 0.742 vs Qwen的0.758，差距16pp体现了Llama系列multilingual pretraining 数据在低资源语言上的相对弱势。Pareto rho中位数-0.73略弱于Qwen的-0.78， 因为Scout只有12个probed层，frontier采样更粗糙。16/20语言>0.65（vs Qwen 17/20）， sw/bn/my/jv四个低资源语言未达标。Architecture-dependent差异是本文Claim 1的核心发现。\\n\"\n  },\n  {\n    \"name\": \"CaCLR Implementation and Comparative Evaluation\",\n    \"description\": \"CaCLR (L_BCE + α·L_SB-ECE + β·L_MMD) 训练、超参数sweep、与所有baseline的全面比较。 Path A: β term provides meaningful gain.\\n\",\n    \"results\": {\n      \"caclr_optimal_alpha\": 1.0,\n      \"caclr_optimal_beta\": 0.1,\n      \"caclr_beta_delta_auroc_over_alpha_only_median\": 0.032,\n      \"caclr_beta_delta_auroc_over_alpha_only_range\": [\n        0.018,\n        0.051\n      ],\n      \"caclr_full_delta_auroc_over_zeroshot_median\": 0.062,\n      \"caclr_full_delta_auroc_over_zeroshot_range\": [\n        0.031,\n        0.098\n      ],\n      \"caclr_vs_linear_proj_delta_median\": 0.014,\n      \"caclr_vs_fewshot100_delta_median\": -0.008,\n      \"ece_reduction_vs_temp_scaling_median\": 0.035,\n      \"ece_reduction_vs_temp_scaling_range\": [\n        0.012,\n        0.061\n      ],\n      \"beta_sweep_results\": {\n        \"beta_0.001\": {\n          \"delta_auroc_over_alpha_only\": 0.008,\n          \"note\": \"too weak\"\n        },\n        \"beta_0.01\": {\n          \"delta_auroc_over_alpha_only\": 0.019,\n          \"note\": \"marginal\"\n        },\n        \"beta_0.1\": {\n          \"delta_auroc_over_alpha_only\": 0.032,\n          \"note\": \"optimal\"\n        },\n        \"beta_1.0\": {\n          \"delta_auroc_over_alpha_only\": 0.021,\n          \"note\": \"overfitting to distributional match\"\n        }\n      },\n      \"alpha_sweep_results\": {\n        \"alpha_0.01\": {\n          \"en_ece\": 0.068,\n          \"transfer_auroc_median\": 0.779\n        },\n        \"alpha_0.1\": {\n          \"en_ece\": 0.055,\n          \"transfer_auroc_median\": 0.793\n        },\n        \"alpha_1.0\": {\n          \"en_ece\": 0.041,\n          \"transfer_auroc_median\": 0.808\n        },\n        \"alpha_10.0\": {\n          \"en_ece\": 0.038,\n          \"transfer_auroc_median\": 0.791\n        }\n      },\n      \"layer_interaction\": {\n        \"mid_depth_beta_gain\": 0.041,\n        \"deep_layer_beta_gain\": 0.024,\n        \"shallow_layer_beta_gain\": 0.018\n      },\n      \"qwen_results\": {\n        \"layer56_caclr_full_median\": 0.828,\n        \"layer76_caclr_full_median\": 0.788\n      },\n      \"scout_results\": {\n        \"layer24_caclr_full_median\": 0.812,\n        \"layer40_caclr_full_median\": 0.771\n      },\n      \"bootstrap_ci_beta_effect\": [\n        0.019,\n        0.045\n      ],\n      \"paired_permutation_p_beta\": 0.003,\n      \"cohens_d_beta\": 0.48\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: Transfer Method Comparison (Median AUROC across 20 languages, both models)\",\n        \"columns\": [\n          \"method\",\n          \"labels_needed\",\n          \"qwen_layer56\",\n          \"qwen_layer76\",\n          \"scout_layer24\",\n          \"scout_layer40\",\n          \"median_all\"\n        ],\n        \"rows\": [\n          [\n            \"zero-shot\",\n            0,\n            0.771,\n            0.714,\n            0.756,\n            0.698,\n            0.735\n          ],\n          [\n            \"mean-shift\",\n            0,\n            0.771,\n            0.714,\n            0.756,\n            0.698,\n            0.735\n          ],\n          [\n            \"CaCLR_alpha_only\",\n            \"0 (parallel inputs)\",\n            0.798,\n            0.762,\n            0.784,\n            0.745,\n            0.772\n          ],\n          [\n            \"CaCLR_full\",\n            \"0 (parallel inputs)\",\n            0.828,\n            0.788,\n            0.812,\n            0.771,\n            0.8\n          ],\n          [\n            \"linear_proj_50\",\n            \"50 parallel pairs\",\n            0.812,\n            0.779,\n            0.798,\n            0.758,\n            0.787\n          ],\n          [\n            \"fewshot_25\",\n            25,\n            0.798,\n            0.761,\n            0.781,\n            0.741,\n            0.77\n          ],\n          [\n            \"fewshot_100\",\n            100,\n            0.821,\n            0.792,\n            0.808,\n            0.778,\n            0.8\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 5: β Sensitivity Sweep (Qwen3-235B, layer 56, median across 20 langs)\",\n        \"columns\": [\n          \"beta\",\n          \"delta_auroc_over_alpha_only\",\n          \"delta_ece_over_alpha_only\",\n          \"note\"\n        ],\n        \"rows\": [\n          [\n            0.001,\n            0.008,\n            -0.003,\n            \"negligible distributional constraint\"\n          ],\n          [\n            0.01,\n            0.019,\n            -0.008,\n            \"marginal improvement\"\n          ],\n          [\n            0.1,\n            0.032,\n            -0.014,\n            \"optimal — balances alignment and prediction\"\n          ],\n          [\n            1.0,\n            0.021,\n            -0.011,\n            \"over-regularized — MMD dominates loss\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CaCLR的consistency loss在mid-depth层效果最好，这与CKA分析（plan_011）一致： mid-depth层的cross-lingual表征相似度足够高让MMD有效对齐，但已经有enough language-specific分化使得对齐产生实际收益。β=0.1的inverted-U曲线说明 distributional matching存在sweet spot——太弱无效，太强则牺牲correctness prediction。 CaCLR vs fewshot_100的near-parity（-0.8pp）是重要结果：CaCLR达到了接近 100-label supervised的性能，但不需要任何target-language correctness labels。 统计显著性（p=0.003, d=0.48）确保β效应不是噪声。\\n\\n\\nCaCLR consistency loss (β term) 提供了有意义的增益（中位数+3.2pp over α-only）， 支持Path A叙事。β=0.1是最优点——更低（0.001-0.01）则MMD约束太弱无法对齐分布， 更高（1.0）则过度约束导致correctness prediction损失。 β增益在mid-depth层（40-60%）最大（+4.1pp），因为这些层的cross-lingual表征 仍有足够的共享结构让MMD可以有效对齐，但已经开始出现分化需要对齐。 在deep层β增益下降到+2.4pp，因为表征的geometric misalignment（非仅distributional shift） 限制了MMD的有效性——但CaCLR仍然比zero-shot好得多。 CaCLR vs linear projection：CaCLR赢1.4pp中位数，因为它同时优化calibration（α项） 和alignment（β项），而linear projection仅做alignment。但CaCLR略输于few-shot 100 （-0.8pp），因为100个标注样本提供了直接的target-language correctness信号。 关键：CaCLR不需要target-language labels，这是实际场景中的核心优势。 ECE reduction vs temp scaling中位数3.5pp，因为CaCLR在训练时直接优化SB-ECE， 而temp scaling仅做post-hoc rescaling无法修复表征层面的miscalibration。 Bootstrap CI [0.019, 0.045]和p=0.003确认β效应统计显著；Cohen's d=0.48为中等效应量。\\n\"\n  },\n  {\n    \"name\": \"Difficulty-Controlled Decomposition Ablation\",\n    \"description\": \"IRT difficulty probes → project out difficulty → retrain correctness probes → evaluate transfer. 10 languages × 8 layers × 2 models.\\n\",\n    \"results\": {\n      \"decomposition_transfer_delta_after_difficulty_removal_median\": 0.031,\n      \"decomposition_transfer_delta_range\": [\n        0.011,\n        0.052\n      ],\n      \"difficulty_probe_r2_median\": 0.68,\n      \"difficulty_direction_cosine_with_correctness\": 0.34,\n      \"capability_specific_transfer_degradation_per_depth\": {\n        \"shallow_20pct\": 0.008,\n        \"mid_50pct\": 0.024,\n        \"deep_80pct\": 0.048\n      },\n      \"random_direction_control_delta\": 0.002,\n      \"resource_tier_pattern\": {\n        \"HIGH_delta\": 0.022,\n        \"MID_delta\": 0.033,\n        \"LOW_delta\": 0.041\n      },\n      \"bootstrap_ci_decomposition_delta\": [\n        0.018,\n        0.044\n      ],\n      \"paired_permutation_p\": 0.006,\n      \"cohens_d\": 0.41\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: Decomposition Effect by Resource Tier and Depth (ΔAUROC after difficulty removal)\",\n        \"columns\": [\n          \"depth_pct\",\n          \"HIGH_avg\",\n          \"MID_avg\",\n          \"LOW_avg\",\n          \"random_control\"\n        ],\n        \"rows\": [\n          [\n            20,\n            0.012,\n            0.014,\n            0.019,\n            0.001\n          ],\n          [\n            35,\n            0.016,\n            0.022,\n            0.028,\n            0.002\n          ],\n          [\n            50,\n            0.021,\n            0.031,\n            0.038,\n            0.002\n          ],\n          [\n            60,\n            0.024,\n            0.036,\n            0.043,\n            0.003\n          ],\n          [\n            70,\n            0.026,\n            0.039,\n            0.046,\n            0.002\n          ],\n          [\n            80,\n            0.028,\n            0.041,\n            0.048,\n            0.003\n          ],\n          [\n            85,\n            0.025,\n            0.038,\n            0.044,\n            0.002\n          ],\n          [\n            90,\n            0.022,\n            0.034,\n            0.041,\n            0.002\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Decomposition结果支持Claim 2：difficulty和capability在correctness方向中可分离， 且分离后capability-specific信号的cross-lingual transfer一致改善。 关键insight是resource tier gradient——低资源语言的difficulty entanglement最严重， 也从decomposition中获益最多。这为CaCLR提供了theoretical motivation： CaCLR的consistency loss本质上在做distributional alignment of capability-specific signals。 Random-direction control（~0pp）是关键的methodological guard rail。\\n\\n\\nDifficulty direction与correctness direction有中等cosine（0.34），说明两者共享 部分信号但不完全重叠。Project out difficulty后，残差中的correctness信号更 \\\"capability-pure\\\"——这个信号在高资源语言间更容易transfer（+2.2pp）， 因为capability-specific failures在这些语言间更一致。低资源语言获益最大（+4.1pp）， 因为原始correctness方向中difficulty成分占比更高（低资源语言的difficulty分布 与EN差异更大），去除difficulty后暴露出更可transfer的capability信号。 深层退化更明显（4.8pp）因为深层同时编码了更多language-specific的difficulty信息。 Random-direction control仅+0.2pp，排除了dimensionality reduction artifact—— 是difficulty方向的specific removal而非arbitrary降维带来的改善。 这个分解是prescriptive的：它告诉我们哪些language-layer组合需要capability alignment （高delta = 高difficulty entanglement = 需要CaCLR/projection）。\\n\"\n  },\n  {\n    \"name\": \"Cross-Lingual Orthogonality Analysis\",\n    \"description\": \"Correctness-confidence cosine similarity across 20 languages × 2 architectures, analyzed by resource tier and language family.\\n\",\n    \"results\": {\n      \"orthogonality_cosine_mean_across_langs\": 0.042,\n      \"orthogonality_cosine_max_across_langs\": 0.062,\n      \"orthogonality_cosine_min_across_langs\": 0.018,\n      \"orthogonality_cosine_std\": 0.013,\n      \"cosine_by_tier\": {\n        \"HIGH_mean\": 0.038,\n        \"MID_mean\": 0.043,\n        \"LOW_mean\": 0.051\n      },\n      \"cosine_by_architecture\": {\n        \"qwen_mean\": 0.039,\n        \"scout_mean\": 0.046\n      },\n      \"cosine_range_qwen_20lang\": [\n        0.018,\n        0.058\n      ],\n      \"cosine_range_scout_20lang\": [\n        0.022,\n        0.062\n      ],\n      \"all_20_langs_below_0p08\": true,\n      \"bootstrap_ci_mean_cosine\": [\n        0.035,\n        0.049\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Correctness-Confidence Cosine Similarity by Language\",\n        \"columns\": [\n          \"language\",\n          \"tier\",\n          \"qwen_cosine\",\n          \"scout_cosine\",\n          \"mean\"\n        ],\n        \"rows\": [\n          [\n            \"en\",\n            \"HIGH\",\n            0.031,\n            0.037,\n            0.034\n          ],\n          [\n            \"zh\",\n            \"HIGH\",\n            0.035,\n            0.041,\n            0.038\n          ],\n          [\n            \"es\",\n            \"HIGH\",\n            0.033,\n            0.039,\n            0.036\n          ],\n          [\n            \"fr\",\n            \"HIGH\",\n            0.034,\n            0.04,\n            0.037\n          ],\n          [\n            \"de\",\n            \"HIGH\",\n            0.036,\n            0.042,\n            0.039\n          ],\n          [\n            \"hi\",\n            \"MID\",\n            0.039,\n            0.045,\n            0.042\n          ],\n          [\n            \"ru\",\n            \"MID\",\n            0.037,\n            0.043,\n            0.04\n          ],\n          [\n            \"ko\",\n            \"MID\",\n            0.041,\n            0.047,\n            0.044\n          ],\n          [\n            \"tr\",\n            \"MID\",\n            0.043,\n            0.049,\n            0.046\n          ],\n          [\n            \"sw\",\n            \"LOW\",\n            0.048,\n            0.056,\n            0.052\n          ],\n          [\n            \"bn\",\n            \"LOW\",\n            0.052,\n            0.058,\n            0.055\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-lingual orthogonality的universal persistence是论文的bounding contribution。 它回答了\\\"为什么需要probe-based calibration\\\"：因为output-based方法在结构上 无法获取correctness信息（cosine<0.08），无论语言。Resource tier gradient 是nuanced finding但不影响main conclusion。\\n\\n\\nOrthogonality在所有20语言 × 2架构上持续存在（max cosine 0.062 < 0.08阈值）， 确认Miao & Ungar (2026)的English-only发现是universal structural property。 Low-resource语言cosine略高（0.051 vs HIGH 0.038），因为这些语言的confidence probe quality更低（更少训练数据→confidence方向估计噪声更大→与correctness的 apparent cosine被噪声inflate）。但即使是最高的0.062也远低于non-orthogonal阈值， 说明output-based calibration在结构上受限不依赖于语言。 Qwen略比Scout更orthogonal（0.039 vs 0.046），可能反映Qwen更大的模型容量 使correctness和confidence能被编码在更分离的子空间中。 这个发现bounds entire output-based calibration approach：无论语言或架构， verbalized confidence不包含correctness信息，motivating probe-based方法。\\n\"\n  },\n  {\n    \"name\": \"Probe Complexity Comparison\",\n    \"description\": \"Logistic regression vs 2-layer MLP across all probed layers, both models. EN accuracy, cross-lingual transfer degradation, calibration comparison.\\n\",\n    \"results\": {\n      \"lr_en_best_auroc_qwen\": 0.838,\n      \"mlp_en_best_auroc_qwen\": 0.852,\n      \"lr_en_best_auroc_scout\": 0.821,\n      \"mlp_en_best_auroc_scout\": 0.834,\n      \"lr_zs_transfer_degradation_median\": 0.068,\n      \"mlp_zs_transfer_degradation_median\": 0.104,\n      \"lr_transfer_advantage_over_mlp_median\": 0.022,\n      \"lr_ece_vs_mlp_ece\": [\n        -0.008,\n        0.003\n      ],\n      \"mlp_overfit_indicator_deep_layers\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Probe Complexity — EN AUROC vs ZS Transfer (Qwen3-235B, selected layers)\",\n        \"columns\": [\n          \"layer\",\n          \"lr_en\",\n          \"mlp_en\",\n          \"lr_zs_median\",\n          \"mlp_zs_median\",\n          \"lr_transfer_advantage\"\n        ],\n        \"rows\": [\n          [\n            24,\n            0.711,\n            0.722,\n            0.698,\n            0.691,\n            0.007\n          ],\n          [\n            40,\n            0.762,\n            0.778,\n            0.756,\n            0.741,\n            0.015\n          ],\n          [\n            56,\n            0.798,\n            0.814,\n            0.771,\n            0.752,\n            0.019\n          ],\n          [\n            76,\n            0.838,\n            0.852,\n            0.714,\n            0.686,\n            0.028\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Linear probe是正确的default choice。MLP的EN优势被transfer劣势完全抵消。 这个结果also间接支持correctness direction是线性的——linear probe已经捕获了 大部分信号，MLP额外捕获的主要是noise/language-specific artifact。\\n\\n\\nLinear probes在EN AUROC上略输MLP（~1.4pp），但在cross-lingual transfer上 显著更好（+2.2pp median）。MLP的额外容量捕获了EN-specific patterns导致更多 overfitting to source language——这些patterns在target语言中不泛化。 这与probe complexity literature一致（Hewitt & Liang 2019）：更强的probe 在source domain表现更好但generalization更差。Linear probe的inductive bias （只能学习线性可分方向）恰好与correctness direction的线性结构匹配， 同时限制了对language-specific artifacts的拟合。 在deep层这个差异更大（MLP overfitting更严重），因为deep层表征更language-specific。 这个结果support使用logistic regression作为primary probe的选择。\\n\"\n  },\n  {\n    \"name\": \"Additional Benchmark Evaluation (Belebele + MMLU-ProX)\",\n    \"description\": \"Best probes + CaCLR在Belebele和MMLU-ProX上的评估，验证beyond-GlobalMMLU泛化。\\n\",\n    \"results\": {\n      \"belebele_zs_auroc_median\": 0.731,\n      \"belebele_caclr_auroc_median\": 0.789,\n      \"mmlu_prox_zs_auroc_median\": 0.748,\n      \"mmlu_prox_caclr_auroc_median\": 0.801,\n      \"cross_benchmark_correlation\": 0.92,\n      \"belebele_pareto_rho_median\": -0.71,\n      \"mmlu_prox_pareto_rho_median\": -0.75\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: Cross-Benchmark Generalization (Qwen3-235B, optimal transfer layer)\",\n        \"columns\": [\n          \"benchmark\",\n          \"zs_median\",\n          \"caclr_median\",\n          \"pareto_rho\",\n          \"langs_above_0p65\"\n        ],\n        \"rows\": [\n          [\n            \"GlobalMMLU\",\n            0.758,\n            0.808,\n            -0.78,\n            17\n          ],\n          [\n            \"Belebele\",\n            0.731,\n            0.789,\n            -0.71,\n            15\n          ],\n          [\n            \"MMLU-ProX\",\n            0.748,\n            0.801,\n            -0.75,\n            16\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-benchmark泛化confirm findings are not benchmark-specific artifact。 Pareto frontier在三个benchmark上一致存在但shape有细微差异—— Belebele更浅的optimal depth可能反映reading comprehension使用了更浅层的表征。\\n\\n\\nBelebele（reading comprehension）的ZS AUROC略低于GlobalMMLU（0.731 vs 0.758）， 因为不同任务的correctness信号分布不完全一致——但Pareto frontier仍然存在 （rho=-0.71），说明depth-transfer tradeoff是task-general的。 MMLU-ProX与GlobalMMLU最相似（同为knowledge QA），所以结果最接近（0.748 vs 0.758）。 CaCLR在两个benchmark上都提供了consistent improvement（+5.3-5.8pp）， 说明CaCLR学到的alignment不是GlobalMMLU-specific的。 Cross-benchmark correlation 0.92表明per-language transfer difficulty在benchmarks间高度一致—— sw/bn在所有benchmarks上都最难transfer，zh/es在所有benchmarks上都最容易。\\n\"\n  },\n  {\n    \"name\": \"INT8 Validation Ablation\",\n    \"description\": \"INT8 vs FP16对比，Llama 4 Scout，5 representative layers，5% random subset。\\n\",\n    \"results\": {\n      \"int8_fp16_auroc_max_diff\": 0.006,\n      \"int8_fp16_auroc_mean_diff\": 0.003,\n      \"int8_fp16_ece_max_diff\": 0.008,\n      \"int8_fp16_direction_cosine_min\": 0.987,\n      \"all_diffs_within_noise\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S1: INT8 vs FP16 Comparison (Llama 4 Scout)\",\n        \"columns\": [\n          \"layer\",\n          \"int8_auroc\",\n          \"fp16_auroc\",\n          \"diff\",\n          \"direction_cosine\"\n        ],\n        \"rows\": [\n          [\n            8,\n            0.674,\n            0.678,\n            -0.004,\n            0.991\n          ],\n          [\n            16,\n            0.741,\n            0.745,\n            -0.004,\n            0.989\n          ],\n          [\n            24,\n            0.788,\n            0.791,\n            -0.003,\n            0.992\n          ],\n          [\n            32,\n            0.811,\n            0.814,\n            -0.003,\n            0.99\n          ],\n          [\n            40,\n            0.821,\n            0.827,\n            -0.006,\n            0.987\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"INT8量化不distort correctness signals。所有差异在bootstrap noise范围内。 Deep层差异略大（layer 40: 0.6pp）符合预期——深层表征更complex，量化误差累积更多。 但0.6pp远小于实验效应（CaCLR +6pp），不影响任何结论。\\n\\n\\nINT8量化对correctness direction的影响极小（max AUROC差异0.6pp）， 因为correctness信号是高SNR的线性方向——量化噪声主要影响低幅度维度， 而correctness direction在high-variance维度上有强projection。 Direction cosine>0.987说明INT8和FP16下提取的correctness方向几乎相同。 ECE差异稍大（0.8pp）因为calibration对probability scale更敏感，但仍在噪声范围内。 这排除了\\\"INT8 artifact\\\"的reviewer concern。\\n\"\n  },\n  {\n    \"name\": \"CKA Cross-Lingual Representation Similarity\",\n    \"description\": \"CKA (linear kernel) between EN and each target language at every probed layer, correlated with transfer AUROC. Mechanistic explanation for Pareto frontier.\\n\",\n    \"results\": {\n      \"cka_transfer_pearson_r\": 0.82,\n      \"cka_transfer_pearson_r_ci\": [\n        0.76,\n        0.87\n      ],\n      \"cka_transfer_spearman_rho\": 0.79,\n      \"cka_en_zh_by_depth_trend\": \"monotonically decreasing from 0.92 (shallow) to 0.61 (deep)\",\n      \"cka_en_sw_by_depth_trend\": \"monotonically decreasing from 0.84 (shallow) to 0.38 (deep)\",\n      \"cka_resource_tier_gradient\": {\n        \"HIGH_mean_cka_at_optimal_depth\": 0.78,\n        \"MID_mean_cka_at_optimal_depth\": 0.71,\n        \"LOW_mean_cka_at_optimal_depth\": 0.58\n      },\n      \"geometric_misalignment_evidence\": \"CKA drop from mid to deep layers exceeds what mean/covariance shift alone predicts. Subspace angle analysis shows correctness direction rotates 15-35° across languages at deep layers vs 5-12° at shallow layers.\\n\",\n      \"cka_explains_caclr_beta_limit\": \"At layers where CKA < 0.55, β term provides diminishing returns because geometric misalignment (rotation) dominates distributional shift.\\n\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: CKA by Depth and Resource Tier (Qwen3-235B)\",\n        \"columns\": [\n          \"depth_pct\",\n          \"HIGH_cka\",\n          \"MID_cka\",\n          \"LOW_cka\",\n          \"zs_auroc_median\"\n        ],\n        \"rows\": [\n          [\n            10,\n            0.93,\n            0.89,\n            0.84,\n            0.618\n          ],\n          [\n            25,\n            0.9,\n            0.85,\n            0.78,\n            0.698\n          ],\n          [\n            40,\n            0.86,\n            0.79,\n            0.69,\n            0.756\n          ],\n          [\n            50,\n            0.82,\n            0.74,\n            0.62,\n            0.771\n          ],\n          [\n            60,\n            0.78,\n            0.69,\n            0.55,\n            0.771\n          ],\n          [\n            70,\n            0.73,\n            0.63,\n            0.47,\n            0.741\n          ],\n          [\n            80,\n            0.67,\n            0.56,\n            0.41,\n            0.714\n          ],\n          [\n            90,\n            0.61,\n            0.49,\n            0.35,\n            0.688\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CKA analysis是论文的mechanistic backbone。它将observation（Pareto frontier） 与explanation（representation geometry变化）和method（CaCLR的作用机制与局限） 连接起来。CKA<0.55作为CaCLR β有效性的threshold是一个actionable finding—— 实践者可以用CKA预测CaCLR在哪些layer-language组合上有效。 Geometric vs distributional misalignment的区分是theoretical contribution： 它解释了为什么distributional matching（MMD/CaCLR）在mid-depth有效但在deep层递减， 而geometric alignment（linear projection）在deep层更稳定。\\n\\n\\nCKA与transfer AUROC的高相关（r=0.82）提供了Pareto frontier的mechanistic explanation： cross-lingual表征相似度随depth monotonically下降，直接导致deep层transfer degradation。 这不是trivial的\\\"深层更specific\\\"——CKA量化了具体的相似度数值并与transfer成功率 建立了定量关系。High-resource语言在所有depth保持更高CKA（因为pretraining data overlap）， 解释了resource tier gradient。 关键insight：deep层的CKA下降不仅是distributional shift（可被MMD修正）， 还包含geometric misalignment（correctness方向在语言间旋转15-35°）。 这解释了CaCLR β term在deep层效果减弱——MMD对齐分布但不学习旋转， 而linear projection学习旋转所以在deep层更稳定。 Subspace angle analysis区分了distributional vs geometric misalignment， 为Path A narrative提供了theoretical depth：CaCLR works at mid-depth因为 那里的misalignment主要是distributional的。\\n\"\n  },\n  {\n    \"name\": \"Linear Projection Sensitivity Analysis\",\n    \"description\": \"Linear projection pair count sweep (10, 20, 50, 100, 200). Both models × 5 layers × 20 languages.\\n\",\n    \"results\": {\n      \"linear_proj_min_pairs_for_saturation\": 35,\n      \"saturation_criterion\": \"95% of 200-pair performance\",\n      \"pairs_sweep\": {\n        \"10\": {\n          \"median_auroc\": 0.762,\n          \"pct_of_200\": 0.88\n        },\n        \"20\": {\n          \"median_auroc\": 0.778,\n          \"pct_of_200\": 0.94\n        },\n        \"50\": {\n          \"median_auroc\": 0.792,\n          \"pct_of_200\": 0.98\n        },\n        \"100\": {\n          \"median_auroc\": 0.796,\n          \"pct_of_200\": 0.99\n        },\n        \"200\": {\n          \"median_auroc\": 0.798,\n          \"pct_of_200\": 1.0\n        }\n      },\n      \"low_resource_saturation_later\": true,\n      \"low_resource_min_pairs\": 48,\n      \"high_resource_min_pairs\": 22\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: Linear Projection Data Efficiency (median across 20 langs × 2 models)\",\n        \"columns\": [\n          \"n_pairs\",\n          \"median_auroc\",\n          \"delta_vs_zs\",\n          \"pct_of_200pair\",\n          \"HIGH_auroc\",\n          \"LOW_auroc\"\n        ],\n        \"rows\": [\n          [\n            10,\n            0.762,\n            0.027,\n            88,\n            0.781,\n            0.638\n          ],\n          [\n            20,\n            0.778,\n            0.043,\n            94,\n            0.798,\n            0.651\n          ],\n          [\n            50,\n            0.792,\n            0.057,\n            98,\n            0.814,\n            0.664\n          ],\n          [\n            100,\n            0.796,\n            0.061,\n            99,\n            0.818,\n            0.668\n          ],\n          [\n            200,\n            0.798,\n            0.063,\n            100,\n            0.821,\n            0.671\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Linear projection的data efficiency confirms它作为practical baseline的价值。 50 pairs的saturation point意味着任何有minimal translation capacity的语言 都可以使用这个方法。这也为CaCLR设定了benchmark：CaCLR需要beat 50-pair projection 才能justify its additional complexity（in best tier, CaCLR beats by +1.4pp median）。\\n\\n\\nLinear projection在~35 pairs时达到饱和（95% of 200-pair performance）， 因为correctness方向是低维线性结构——学习一个旋转/缩放矩阵不需要很多样本。 10 pairs已经达到88%性能，说明即使极少数据也能捕获主要的geometric transformation。 50 pairs后几乎无改善（98%→100%），符合线性映射的low sample complexity理论。 Low-resource语言需要slightly more pairs（48 vs 22），因为表征空间中 correctness方向的SNR更低，需要更多样本来robustly估计映射。 整体saturation在20-50范围内，support \\\"≤50 parallel pairs suffice\\\"的claim。 这建立了linear projection作为practical baseline的地位—— 50 pairs在任何语言都容易获得（e.g., 翻译50个MCQA items）。\\n\"\n  },\n  {\n    \"name\": \"Probing Control Tasks (Hewitt & Liang 2019)\",\n    \"description\": \"Random-label control probes at each layer. Selectivity = probe AUROC - control AUROC. Validates genuine correctness signal.\\n\",\n    \"results\": {\n      \"control_task_auroc_range\": [\n        0.502,\n        0.538\n      ],\n      \"selectivity_median\": 0.284,\n      \"selectivity_min\": 0.192,\n      \"selectivity_max\": 0.341,\n      \"control_task_selectivity_min_across_langs\": 0.192,\n      \"selectivity_by_depth\": {\n        \"shallow\": 0.218,\n        \"mid\": 0.294,\n        \"deep\": 0.312\n      },\n      \"selectivity_by_tier\": {\n        \"HIGH\": 0.301,\n        \"MID\": 0.278,\n        \"LOW\": 0.234\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S2: Control Task Selectivity (Qwen3-235B, selected layers × languages)\",\n        \"columns\": [\n          \"layer\",\n          \"en_selectivity\",\n          \"zh_selectivity\",\n          \"sw_selectivity\",\n          \"control_auroc\"\n        ],\n        \"rows\": [\n          [\n            16,\n            0.248,\n            0.231,\n            0.192,\n            0.512\n          ],\n          [\n            32,\n            0.281,\n            0.268,\n            0.218,\n            0.519\n          ],\n          [\n            48,\n            0.309,\n            0.292,\n            0.241,\n            0.524\n          ],\n          [\n            56,\n            0.318,\n            0.301,\n            0.248,\n            0.521\n          ],\n          [\n            76,\n            0.341,\n            0.324,\n            0.262,\n            0.538\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Control task validation是methodological necessity。Selectivity最小值19.2pp 大幅超过15pp阈值，即使在最challenging的条件（low-resource × shallow layer） 也确认probe是在提取genuine signal。这让reviewer对所有downstream结果 （Pareto frontier, CaCLR, decomposition）更有信心。\\n\\n\\nControl probe AUROC在0.50-0.54范围（near chance），selectivity中位数0.284 远超15pp minimum threshold（min=19.2pp）。这confirm probe AUROC反映 genuine correctness direction而非memorized artifacts或probe capacity。 Selectivity随depth增加（0.218→0.312），因为深层表征包含更丰富的correctness 信号而control仍在chance附近——深层probe的高AUROC不是因为probe容量过大。 Low-resource语言selectivity最低（0.234）但仍远超threshold， 说明即使低资源语言的correctness信号也是genuine的（不是noise fitting）。 这直接回应Hewitt & Liang probing methodology critique—— 我们的probes确实在提取linguistic property而非exploiting high-dimensional capacity。\\n\"\n  },\n  {\n    \"name\": \"Gemma 4 31B Dense — Camera-Ready Extension\",\n    \"description\": \"Third architecture (dense, FP16), full Pareto frontier. Dense vs MoE contrast for camera-ready.\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.809,\n      \"en_best_layer\": 48,\n      \"optimal_transfer_layer\": 36,\n      \"zs_transfer_auroc_median\": 0.738,\n      \"pareto_rho_median\": -0.69,\n      \"pareto_shape\": \"smoother frontier than MoE models — no sharp elbow\",\n      \"dense_vs_moe_key_finding\": \"Dense architecture shows shallower Pareto slope — transfer degrades more gradually with depth compared to MoE models. Consistent with hypothesis that expert routing accelerates language specialization.\\n\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S3: Three-Architecture Comparison Summary\",\n        \"columns\": [\n          \"model\",\n          \"type\",\n          \"params\",\n          \"layers\",\n          \"en_best_auroc\",\n          \"zs_median\",\n          \"optimal_transfer_pct\",\n          \"pareto_rho\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-235B-A22B\",\n            \"MoE\",\n            \"235B\",\n            94,\n            0.838,\n            0.758,\n            60,\n            -0.78\n          ],\n          [\n            \"Llama 4 Scout\",\n            \"MoE\",\n            \"109B (17B active)\",\n            48,\n            0.821,\n            0.742,\n            50,\n            -0.73\n          ],\n          [\n            \"Gemma 4 31B Dense\",\n            \"Dense\",\n            \"31B\",\n            60,\n            0.809,\n            0.738,\n            75,\n            -0.69\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Three-architecture comparison is the crown jewel of Claim 1。 Dense vs MoE对比provides causal insight into WHY frontiers differ—— expert routing is the mechanism driving sharp language specialization at depth.\\n\\n\\nGemma 4 31B Dense作为dense对照提供了architectural contrast。 EN AUROC 0.809低于两个MoE模型（0.838, 0.821），反映31B dense参数<235B MoE active参数。 关键发现：dense架构的Pareto frontier更平滑（rho=-0.69 vs MoE -0.73/-0.78）， 没有MoE的sharp elbow。这是因为MoE的expert routing在深层创造了discrete language specialization（某些experts \\\"负责\\\"特定语言），而dense模型的specialization是gradual的。 这是architecture-dependent Pareto shape claim的strongest evidence。 Optimal transfer在75%深度（layer 36/48），比Qwen3浅（60%）但比Scout深（50%）， 提供了第三个data point来characterize architecture-depth relationship。\\n\"\n  },\n  {\n    \"name\": \"Extended Language Coverage — Camera-Ready\",\n    \"description\": \"Expand from 20 to 50+ languages. Camera-ready extension using GlobalMMLU/Belebele full sets.\\n\",\n    \"results\": {\n      \"total_languages\": 52,\n      \"zs_langs_above_0p65\": 38,\n      \"zs_auroc_median_52lang\": 0.721,\n      \"new_low_resource_findings\": \"Several additional low-resource languages (e.g., Yoruba, Hausa, Malagasy) show ZS AUROC 0.58-0.64, confirming resource-tier gradient extends to tail.\\n\",\n      \"pareto_frontier_robust\": true,\n      \"caclr_generalizes\": true,\n      \"caclr_delta_over_zs_52lang_median\": 0.058\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S4: Extended Language Coverage Summary\",\n        \"columns\": [\n          \"resource_tier\",\n          \"n_langs\",\n          \"zs_auroc_median\",\n          \"caclr_median\",\n          \"delta\"\n        ],\n        \"rows\": [\n          [\n            \"HIGH\",\n            12,\n            0.786,\n            0.828,\n            0.042\n          ],\n          [\n            \"MID\",\n            18,\n            0.741,\n            0.798,\n            0.057\n          ],\n          [\n            \"LOW\",\n            22,\n            0.648,\n            0.721,\n            0.073\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Extended coverage是camera-ready的scale argument。核心findings在52语言上robust。 Low-resource语言从CaCLR获益最多（+7.3pp vs HIGH +4.2pp）， because these languages have the most room for improvement and CaCLR's distributional alignment compensates for sparse pretraining representation.\\n\\n52语言验证confirms所有findings at broader scale。ZS median从20 langs的0.758 降到52 langs的0.721，因为新增语言主要是低资源的——这是expected的composition effect。 38/52 > 0.65（73%）vs 17/20（85%），比例下降也反映低资源语言的加入。 Pareto frontier和CaCLR在所有语言上consistent，说明findings是language-general的。 Key new finding：Yoruba/Hausa等sub-Saharan African语言的ZS AUROC（0.58-0.62） 与sw/bn相当，但CaCLR对这些语言的improvement更大（+7-9pp）， 可能因为GlobalMMLU translations provide parallel data that partially bridges the representation gap for these extremely low-resource languages.\\n\"\n  }\n]",
      "numLines": 1374,
      "startLine": 1,
      "totalLines": 1374
    }
  },
  "sourceToolAssistantUUID": "e4fa16c5-4b8b-417f-8ca6-264b041a4b4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T20:42:04.015Z_

<details><summary>↩ Tool result · `toolu_01Fb2Nq1eaLMwCxj6ZiKFGKm`</summary>

```text
1	# Paper Framing — xling_calib_direction
2	
3	## Target Venue
4	- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)
5	- Core submission: 2 models × 20 languages × all contributions
6	- Camera-ready extension: Gemma 4 31B Dense + 30+ languages
7	
8	## Core Insight
9	The model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — transfers cross-lingually through intermediate layers, but with a depth-transferability Pareto tradeoff: deeper layers yield better English calibration while shallower layers transfer better. This tradeoff is architecture-dependent and can be shifted by CaCLR, a probe training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without requiring target-language correctness labels.
10	
11	## Core Claims (4, causal chain)
12	
13	### Claim 1 — Pareto Frontier (Discovery)
14	Cross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth is architecture-dependent.
15	- MVP evidence: L27 AUROC=0.754 (EN best) but transfer drops 2-4pp vs L24 on Qwen2.5-7B.
16	- Full evidence: 2 architectures × 20 languages × all layers × 5 transfer conditions.
17	
18	### Claim 2 — Decomposition (Analysis)
19	Cross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.
20	- Evidence: IRT difficulty probes → project out → retrain → compare transfer.
21	
22	### Claim 3 — CaCLR (Method / Diagnostic)
23	CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on parallel activations from GlobalMMLU translated items, train split only) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels.
24	- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.
25	- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that distributional matching fails for correctness probe transfer. CKA analysis provides the theoretical explanation: cross-lingual misalignment at deeper layers is *geometric* (correctness direction rotates/scales across language subspaces), not merely *distributional* (mean/covariance shift). MMD-based alignment cannot correct geometric transformations, which is why linear projection (which learns the rotation) succeeds where distributional matching fails. This closes the distributional-matching path with both empirical evidence and mechanistic explanation.
26	- Parallel activations source: GlobalMMLU train-split translations (not test items). This requires parallel *inputs* but zero target-language *labels* — a weaker requirement than per-language annotation.
27	- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.
28	- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.
29	
30	### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)
31	The correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.
32	- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.
33	
34	## Story Spine
35	- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).
36	- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.
37	- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching approach, and provide mechanistic analysis (CKA) explaining why transfer succeeds or fails at each depth. This is both a field-level viability test and (depending on CaCLR results) a practical method contribution or a principled negative result.
38	- **Headline template (method success)**: "On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels."
39	- **Headline template (negative result)**: "Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines."
40	- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.
41	
42	## Field-Level Significance
43	This paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.
44	
45	## Anticipated Reviewer Concerns & Responses
46	1. **"Xiao et al. already did this"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.
47	2. **"Temperature scaling baseline"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.
48	3. **"Mean-shift too weak / why does it fail?"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.
49	4. **"Difficulty confound"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.
50	5. **"INT8 artifacts"** → Validation ablation comparing INT8 vs FP16 at representative layers.
51	6. **"Only MCQA"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.
52	7. **"Predictable from domain adaptation theory"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.
53	8. **"No statistical tests"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.
54	9. **"Probing methodology concerns"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.
55	10. **"No mechanistic explanation"** → CKA analysis across layers × languages explains WHY transfer fails at deeper layers (cross-lingual representation similarity decreases with depth) and correlates with transfer success.
56	11. **"Why not conformal prediction?"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.
57	12. **"CaCLR parallel activations = test leakage?"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.
58	
59	## Additional Related Work Coverage (Dream-identified gaps)
60	- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. We derive predictions and test them.
61	- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature; CaCLR's failure despite distributional matching is the novel finding.
62	- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — we use CKA to provide mechanistic explanation for the Pareto frontier.
63	- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity.
64	- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.
65	
66	## Differentiation from Closest Prior Work
67	| Paper | Their Focus | Our Difference |
68	|-------|-------------|----------------|
69	| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |
70	| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |
71	| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |
72	| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |
73	| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |
74	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd0d9b5d-2573-48b3-8211-8904077c202b",
  "isSidechain": false,
  "promptId": "d6812199-51cb-4f3b-a1d1-28a2f25b4592",
  "type": "user",
  "uuid": "47ad7a9b-07da-4210-a359-ea8e57313102",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/paper_framing.md",
      "content": "# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — transfers cross-lingually through intermediate layers, but with a depth-transferability Pareto tradeoff: deeper layers yield better English calibration while shallower layers transfer better. This tradeoff is architecture-dependent and can be shifted by CaCLR, a probe training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without requiring target-language correctness labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth is architecture-dependent.\n- MVP evidence: L27 AUROC=0.754 (EN best) but transfer drops 2-4pp vs L24 on Qwen2.5-7B.\n- Full evidence: 2 architectures × 20 languages × all layers × 5 transfer conditions.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on parallel activations from GlobalMMLU translated items, train split only) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels.\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that distributional matching fails for correctness probe transfer. CKA analysis provides the theoretical explanation: cross-lingual misalignment at deeper layers is *geometric* (correctness direction rotates/scales across language subspaces), not merely *distributional* (mean/covariance shift). MMD-based alignment cannot correct geometric transformations, which is why linear projection (which learns the rotation) succeeds where distributional matching fails. This closes the distributional-matching path with both empirical evidence and mechanistic explanation.\n- Parallel activations source: GlobalMMLU train-split translations (not test items). This requires parallel *inputs* but zero target-language *labels* — a weaker requirement than per-language annotation.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching approach, and provide mechanistic analysis (CKA) explaining why transfer succeeds or fails at each depth. This is both a field-level viability test and (depending on CaCLR results) a practical method contribution or a principled negative result.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\"\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA analysis across layers × languages explains WHY transfer fails at deeper layers (cross-lingual representation similarity decreases with depth) and correlates with transfer success.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. We derive predictions and test them.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature; CaCLR's failure despite distributional matching is the novel finding.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — we use CKA to provide mechanistic explanation for the Pareto frontier.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n",
      "numLines": 74,
      "startLine": 1,
      "totalLines": 74
    }
  },
  "sourceToolAssistantUUID": "cd0d9b5d-2573-48b3-8211-8904077c202b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T201854 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direct…",
  "leafUuid": "2d13ea83-06c5-4e69-bda9-65baa37fad4b",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate calibration research paper with CaCLR method",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571"
}
```

---

### Assistant

_source line 14 · 2026-05-20T20:42:09.282Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of both the experiment data and the paper framing. Let me also load the writing skill for guidance on paper writing style.

Let me now write the full LaTeX paper. I need to:

1. Cover all experiments from experiment_data.json
2. Follow the narrative guidance (Path A - CaCLR works)
3. Structure: Abstract, Introduction, Related Work, Method, Experiments, Analysis, Conclusion
4. Make sure every quantitative claim comes from the data

Let me first ensure the output directory exists, then write the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47ad7a9b-07da-4210-a359-ea8e57313102",
  "isSidechain": false,
  "requestId": "req_011CbEUCvYdHoSe9VGJhtJCM",
  "type": "assistant",
  "uuid": "f5e05c20-611a-4222-b7c9-a5425841f960",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JjTNagnC8ZBtLtArTrLxW4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21683,
      "cache_read_input_tokens": 23322,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21683,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 281,
          "cache_read_input_tokens": 23322,
          "cache_creation_input_tokens": 21683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21683
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

_source line 15 · 2026-05-20T20:42:09.710Z_

Now I have all the data. Let me check the output directory and then write the full paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5e05c20-611a-4222-b7c9-a5425841f960",
  "isSidechain": false,
  "requestId": "req_011CbEUCvYdHoSe9VGJhtJCM",
  "type": "assistant",
  "uuid": "304ea1aa-a9c7-4d57-a199-3dd62d8ca4e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JjTNagnC8ZBtLtArTrLxW4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21683,
      "cache_read_input_tokens": 23322,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21683,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 281,
          "cache_read_input_tokens": 23322,
          "cache_creation_input_tokens": 21683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21683
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

_source line 16 · 2026-05-20T20:42:11.980Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Av8QTgQUGPzF26bzfBkdUm`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/",
  "description": "List output directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "304ea1aa-a9c7-4d57-a199-3dd62d8ca4e9",
  "isSidechain": false,
  "requestId": "req_011CbEUCvYdHoSe9VGJhtJCM",
  "type": "assistant",
  "uuid": "bbd53f8f-f30c-4104-8164-e62985e7954b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JjTNagnC8ZBtLtArTrLxW4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21683,
      "cache_read_input_tokens": 23322,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21683,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 281,
          "cache_read_input_tokens": 23322,
          "cache_creation_input_tokens": 21683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21683
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

_source line 17 · 2026-05-20T20:42:12.173Z_

<details><summary>↩ Tool result · `toolu_01Av8QTgQUGPzF26bzfBkdUm`</summary>

```text
total 112
drwxr-xr-x 2 ubuntu ubuntu  4096 May 20 20:41 .
drwxr-xr-x 4 ubuntu ubuntu  4096 May 20 20:41 ..
-rw-r--r-- 1 ubuntu ubuntu 46823 May 20 20:41 experiment_data.json
-rw-r--r-- 1 ubuntu ubuntu 44080 May 20 20:41 imagined_experiments.yaml
-rw-r--r-- 1 ubuntu ubuntu 11190 May 20 20:41 paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbd53f8f-f30c-4104-8164-e62985e7954b",
  "isSidechain": false,
  "promptId": "d6812199-51cb-4f3b-a1d1-28a2f25b4592",
  "type": "user",
  "uuid": "5d25cbf1-670e-4513-aad2-f0f95a9a45e7",
  "toolUseResult": {
    "stdout": "total 112\ndrwxr-xr-x 2 ubuntu ubuntu  4096 May 20 20:41 .\ndrwxr-xr-x 4 ubuntu ubuntu  4096 May 20 20:41 ..\n-rw-r--r-- 1 ubuntu ubuntu 46823 May 20 20:41 experiment_data.json\n-rw-r--r-- 1 ubuntu ubuntu 44080 May 20 20:41 imagined_experiments.yaml\n-rw-r--r-- 1 ubuntu ubuntu 11190 May 20 20:41 paper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "bbd53f8f-f30c-4104-8164-e62985e7954b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T20:42:14.954Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TaCK3ZEQcBQFtrNy1beDGv`</summary>

```json
{
  "command": "which pdflatex && pdflatex --version | head -2",
  "description": "Check pdflatex availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d25cbf1-670e-4513-aad2-f0f95a9a45e7",
  "isSidechain": false,
  "requestId": "req_011CbEUDXBDnpsX81UQXvHo9",
  "type": "assistant",
  "uuid": "c035fa17-820c-46a4-9ed3-8cbefe70786b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDbXvJcyWv5EsYY5vUFiWj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 446,
      "cache_read_input_tokens": 45005,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 446,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 45005,
          "cache_creation_input_tokens": 446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 446
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

_source line 19 · 2026-05-20T20:42:15.021Z_

<details><summary>↩ Tool result · `toolu_01TaCK3ZEQcBQFtrNy1beDGv`</summary>

```text
/usr/bin/pdflatex
pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)
kpathsea version 6.4.1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c035fa17-820c-46a4-9ed3-8cbefe70786b",
  "isSidechain": false,
  "promptId": "d6812199-51cb-4f3b-a1d1-28a2f25b4592",
  "type": "user",
  "uuid": "f0123ad3-7242-481c-b98a-dfa0e0e75b5f",
  "toolUseResult": {
    "stdout": "/usr/bin/pdflatex\npdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)\nkpathsea version 6.4.1",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "c035fa17-820c-46a4-9ed3-8cbefe70786b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-20T20:42:27.015Z_

<details><summary>Logged reasoning block</summary>

```text
Good, pdflatex is available. Now let me write the full LaTeX paper. I need to carefully structure this based on all the experiment data and the paper framing.

Let me organize the paper:

1. Abstract
2. Introduction
3. Related Work
4. Method (Correctness probes, CaCLR, Decomposition)
5. Experimental Setup
6. Results
   - 6.1 Pareto Frontier (Exp 1 & 2 - Qwen & Scout)
   - 6.2 CaCLR Evaluation (Exp 3)
   - 6.3 Difficulty-Capability Decomposition (Exp 4)
   - 6.4 Cross-Lingual Orthogonality (Exp 5)
   - 6.5 CKA Analysis (Exp 8)
   - 6.6 Additional Analysis (Probe Complexity Exp 6, Benchmarks Exp 7, Linear Proj Exp 9)
7. Discussion
8. Conclusion
Appendix: INT8 validation, control tasks, extended languages, 3-arch comparison

Now I'm pulling together the tables from the experiment data to populate these sections. I need the next thinking content to rewrite. You've provided the current rewritten thinking and the guidelines, but the "next thinking you need to rewrite" section appears to be empty.

Could you please share the next thinking that needs to be rewritten?
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0123ad3-7242-481c-b98a-dfa0e0e75b5f",
  "isSidechain": false,
  "requestId": "req_011CbEUDjeKMXwYn3eHFFtc4",
  "type": "assistant",
  "uuid": "ad51df3e-0315-42b4-a0bb-98803c4cd747",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KP1sAvGznnKiUqYjzpdwDL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 154,
      "cache_read_input_tokens": 45451,
      "output_tokens": 11958,
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
          "output_tokens": 11958,
          "cache_read_input_tokens": 45451,
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

### Assistant

_source line 21 · 2026-05-20T20:42:27.016Z_

Writing the full LaTeX paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad51df3e-0315-42b4-a0bb-98803c4cd747",
  "isSidechain": false,
  "requestId": "req_011CbEUDjeKMXwYn3eHFFtc4",
  "type": "assistant",
  "uuid": "bf5b6fdd-6263-4bec-ab9d-92a96a39d92e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KP1sAvGznnKiUqYjzpdwDL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 154,
      "cache_read_input_tokens": 45451,
      "output_tokens": 11958,
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
          "output_tokens": 11958,
          "cache_read_input_tokens": 45451,
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

### Tool call

_source line 22 · 2026-05-20T20:45:48.811Z_

<details open><summary>🔧 Tool call — Write · `toolu_016xmw3HAUWTDkiXAD9xKVsZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{tabularx}\n\n\\title{Cross-Lingual Calibration via Internal Correctness Directions:\\\\Pareto Frontiers, Decomposition, and Consistency-Aligned Probes}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nMultilingual large language models exhibit substantially worse calibration in non-English languages, yet probe-based calibration methods remain English-only.\nWe present the first systematic study of cross-lingual correctness probe transfer across 20 languages on two MoE architectures (Qwen3-235B-A22B, Llama~4~Scout).\nWe discover a \\emph{depth--transferability Pareto frontier}: deeper layers yield higher English probe AUROC but degrade in zero-shot cross-lingual transfer (Spearman $\\rho=-0.78$/$-0.73$).\nThe frontier shape is architecture-dependent, with the optimal transfer depth at 60\\% for Qwen3 versus 50\\% for Scout.\nWe decompose correctness transfer into difficulty-shared and capability-specific components, showing that removing the difficulty direction improves transfer by 3.1~pp (median), with low-resource languages benefiting most (+4.1~pp).\nWe propose CaCLR, a probe training objective combining binary cross-entropy, sample-binned ECE, and an MMD-based cross-lingual consistency loss on parallel activations.\nCaCLR-trained probes reduce non-English ECE by 3.5\\% over temperature scaling with zero target-language labels, matching few-shot (100-label) supervised performance.\nCKA analysis reveals that cross-lingual representation similarity monotonically decreases with depth ($r=0.82$ with transfer AUROC), mechanistically explaining the Pareto frontier.\nFinally, we confirm that correctness--confidence orthogonality (cosine $<0.062$) persists universally across all 20 languages, bounding output-based calibration regardless of language.\n\\end{abstract}\n\n%---------------------------------------------------------------\n\\section{Introduction}\n\\label{sec:intro}\n%---------------------------------------------------------------\n\nCalibration---the alignment between a model's expressed confidence and its actual accuracy---is critical for deploying language models in high-stakes settings.\nRecent work has shown that multilingual LLMs suffer from substantially worse calibration in non-English languages, with expected calibration error (ECE) up to 5$\\times$ higher than English \\cite{}.\nOutput-based calibration methods such as temperature scaling \\cite{guo2017calibration} and verbalized confidence extraction \\cite{} offer post-hoc corrections but face a structural limitation:\n\\citet{} demonstrated that the internal \\emph{correctness direction} (encoding whether the model will answer correctly) is nearly orthogonal to the \\emph{confidence direction} (encoding verbalized confidence), with cosine similarity below 0.04 in English.\nThis orthogonality means output-based signals are fundamentally uninformative about actual correctness.\n\nProbe-based calibration methods---training linear classifiers on internal representations to predict correctness---offer a principled alternative by directly accessing the correctness direction \\cite{}.\nHowever, all existing probe-based methods (CORAL, CCPS, Confidence Manifold, correctness steering) operate exclusively in English.\nThe question of whether correctness probes transfer cross-lingually---enabling calibration in languages without correctness labels---remains open.\n\nWe present the first systematic study of cross-lingual correctness probe transfer.\nOur contributions form a causal chain:\n\n\\paragraph{(1) Pareto Frontier Discovery.}\nWe reveal a depth--transferability Pareto frontier: deeper layers produce better English probes (AUROC up to 0.838) but degrade in zero-shot cross-lingual transfer.\nThe frontier shape is architecture-dependent---optimal transfer depth is 60\\% for Qwen3-235B versus 50\\% for Llama~4~Scout---with MoE expert routing accelerating deep-layer language specialization.\n\n\\paragraph{(2) Difficulty--Capability Decomposition.}\nWe decompose the correctness signal into a difficulty-shared component (language-agnostic, transferable) and a capability-specific component (language-dependent, driving deep-layer degradation).\nRemoving the difficulty direction improves cross-lingual transfer by 3.1~pp median, with low-resource languages benefiting most (+4.1~pp).\n\n\\paragraph{(3) CaCLR: Calibration-Consistent Cross-Lingual Regularization.}\nWe propose CaCLR, a probe training objective that jointly optimizes correctness prediction ($\\mathcal{L}_\\text{BCE}$), calibration ($\\alpha \\cdot \\mathcal{L}_\\text{SB-ECE}$), and cross-lingual distributional alignment ($\\beta \\cdot \\mathcal{L}_\\text{MMD}$) using parallel activations from translated items.\nCaCLR requires zero target-language correctness labels and reduces non-English ECE by 3.5\\% over temperature scaling across 20 languages.\n\n\\paragraph{(4) Cross-Lingual Orthogonality.}\nWe confirm that correctness--confidence orthogonality persists across all 20 languages and both architectures (max cosine = 0.062), establishing that output-based calibration is structurally limited regardless of language.\n\nCKA representation similarity analysis provides the mechanistic glue: cross-lingual CKA monotonically decreases with depth ($r=0.82$ with transfer AUROC), explaining why deeper layers degrade and why CaCLR's distributional matching is most effective at mid-depth layers where misalignment is distributional rather than geometric.\n\n\n%---------------------------------------------------------------\n\\section{Related Work}\n\\label{sec:related}\n%---------------------------------------------------------------\n\n\\paragraph{LLM Calibration.}\nTemperature scaling \\cite{guo2017calibration} remains the dominant post-hoc calibration method.\nRecent work reveals that multilingual LLMs are substantially worse-calibrated in non-English languages.\nLACE proposes per-language layer ensembles but requires target-language labels.\nMKA uses multi-agent knowledge aggregation at 5$\\times$ inference cost.\n\n\\paragraph{Probe-Based Calibration.}\nCORAL trains cross-task English correctness probes and identifies distribution-shift challenges.\nCCPS uses clustering on correctness probe activations.\nMiao \\& Ungar discover correctness--confidence orthogonality and propose steering-based calibration, but only for English on 7--8B models.\nAll probe-based methods remain monolingual.\n\n\\paragraph{Cross-Lingual Probe Transfer.}\nXiao et al.\\ transfer \\emph{knowledge boundary} probes (input-level answerability) across 8 languages.\nKnowledge boundary is fundamentally different from correctness: answerability is an input property (does the model have relevant knowledge?) while correctness is output-dependent (will the model produce the right answer for this input?).\nTheir success with mean-shift alignment is not expected to transfer to correctness probes, and we formally prove why (Section~\\ref{sec:method:transfer}).\nCivelli et al.\\ study cross-lingual \\emph{difficulty} probes, which we use as a control in our decomposition analysis.\n\n\\paragraph{Domain Adaptation Theory.}\nBen-David et al.'s $\\mathcal{H}$-divergence framework predicts that cross-domain transfer degrades with increasing domain divergence.\nWe derive predictions from this framework and test them: the resource-tier gradient follows theory, but the architecture-dependent Pareto shape and difficulty--capability entanglement are novel findings.\n\n\\paragraph{Representation Similarity.}\nCKA \\cite{kornblith2019similarity} measures representational similarity between network layers.\nWe use CKA to mechanistically explain the Pareto frontier by quantifying cross-lingual representation divergence at each depth.\n\n\\paragraph{Cross-Lingual Alignment.}\nLinear cross-lingual alignment methods (MUSE, VecMap) learn rotation matrices between embedding spaces.\nOur linear projection baseline is conceptually similar; CaCLR's distributional matching via MMD represents the alternative alignment paradigm.\n\n\\paragraph{Conformal Prediction.}\nDistribution-free conformal prediction provides coverage guarantees but requires calibration data per language.\nOur approach targets zero-label transfer, making the two complementary.\n\n\n%---------------------------------------------------------------\n\\section{Method}\n\\label{sec:method}\n%---------------------------------------------------------------\n\n\\subsection{Correctness Probes}\n\\label{sec:method:probes}\n\nGiven a multilingual LLM with $L$ layers, we extract the hidden representation $\\mathbf{h}_\\ell \\in \\mathbb{R}^d$ at layer $\\ell$ for each input.\nA correctness probe $f_\\ell: \\mathbb{R}^d \\to [0,1]$ is a logistic regression classifier trained on English data to predict whether the model's generated answer is correct:\n\\begin{equation}\n    f_\\ell(\\mathbf{h}) = \\sigma(\\mathbf{w}_\\ell^\\top \\mathbf{h} + b_\\ell)\n\\end{equation}\nwhere $\\mathbf{w}_\\ell \\in \\mathbb{R}^d$ defines the \\emph{correctness direction} at layer $\\ell$.\nWe evaluate probes via AUROC (discrimination) and ECE (calibration).\n\n\\subsection{Cross-Lingual Transfer}\n\\label{sec:method:transfer}\n\nWe apply English-trained probes directly to target-language representations (zero-shot transfer).\nWe also evaluate several alignment strategies:\n\n\\paragraph{Mean-Shift.}\nSubtract the English mean and add the target-language mean of representations.\nUnder StandardScaler preprocessing + logistic regression, mean-shift adds a constant offset to all logits.\nSince AUROC is rank-invariant, $\\Delta\\text{AUROC} \\equiv 0$ mathematically---mean-shift cannot improve discrimination under this pipeline.\n\n\\paragraph{Linear Projection.}\nLearn a linear map $\\mathbf{A} \\in \\mathbb{R}^{d \\times d}$ from parallel English--target representation pairs to align the target-language representations to the English correctness subspace.\n\n\\paragraph{Few-Shot.}\nFine-tune probes with 25 or 100 labeled target-language examples.\n\n\\subsection{CaCLR: Calibration-Consistent Cross-Lingual Regularization}\n\\label{sec:method:caclr}\n\nCaCLR trains correctness probes with a composite loss:\n\\begin{equation}\n    \\mathcal{L}_\\text{CaCLR} = \\mathcal{L}_\\text{BCE} + \\alpha \\cdot \\mathcal{L}_\\text{SB-ECE} + \\beta \\cdot \\mathcal{L}_\\text{MMD}\n\\end{equation}\n\n\\noindent where:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item $\\mathcal{L}_\\text{BCE}$: binary cross-entropy on English correctness labels.\n    \\item $\\mathcal{L}_\\text{SB-ECE}$: sample-binned ECE, a differentiable calibration loss.\n    \\item $\\mathcal{L}_\\text{MMD}$: maximum mean discrepancy between English and target-language \\emph{probe activations} on parallel inputs (GlobalMMLU train-split translations). This encourages the probe to produce similar output distributions for semantically equivalent inputs across languages.\n\\end{itemize}\n\nThe MMD term aligns distributional properties (mean, covariance) of probe activations without requiring target-language correctness labels---only parallel inputs.\nWe set $\\alpha=1.0$ and $\\beta=0.1$ based on hyperparameter sweeps (Section~\\ref{sec:exp:caclr}).\n\n\\subsection{Difficulty--Capability Decomposition}\n\\label{sec:method:decomp}\n\nWe hypothesize that the correctness signal mixes two components:\n(1)~a \\emph{difficulty-shared} component reflecting item difficulty (language-agnostic), and\n(2)~a \\emph{capability-specific} component reflecting the model's language-specific ability (drives deep-layer transfer degradation).\n\nWe operationalize this via IRT difficulty probes: train a probe to predict item difficulty (from IRT parameters), extract the difficulty direction $\\mathbf{d}_\\ell$, project it out of representations, and retrain correctness probes on the residual.\nImproved transfer on residual representations confirms that difficulty entanglement degrades cross-lingual transfer.\nA random-direction control validates that the improvement is specific to difficulty removal, not arbitrary dimensionality reduction.\n\n%---------------------------------------------------------------\n\\section{Experimental Setup}\n\\label{sec:setup}\n%---------------------------------------------------------------\n\n\\paragraph{Models.}\nQwen3-235B-A22B (94 layers, MoE, INT8) and Llama~4~Scout (48 layers, MoE, INT8).\nWe probe every 4th layer: 24 layers for Qwen3, 12 for Scout.\n\n\\paragraph{Languages.}\n20 languages spanning three resource tiers: HIGH (en, zh, es, fr, de), MID (hi, ru, ko, tr, and 5 others), LOW (sw, bn, and 8 others).\n\n\\paragraph{Benchmarks.}\nPrimary: GlobalMMLU (multilingual MCQA).\nGeneralization: Belebele (reading comprehension), MMLU-ProX (knowledge QA).\n\n\\paragraph{Probes.}\nLogistic regression with StandardScaler preprocessing.\nWe validate this choice against 2-layer MLPs (Section~\\ref{sec:exp:probe}).\n\n\\paragraph{Evaluation.}\nAUROC for discrimination, ECE for calibration.\nAll comparisons include bootstrap CIs (1000 resamples) and paired permutation tests.\nEffect sizes reported with Cohen's $d$.\n\n\\paragraph{Transfer Conditions.}\nZero-shot, mean-shift, linear projection (50 parallel pairs), few-shot (25/100 labels), and CaCLR.\n\n%---------------------------------------------------------------\n\\section{Results}\n\\label{sec:results}\n%---------------------------------------------------------------\n\n\\subsection{Pareto Frontier Discovery}\n\\label{sec:exp:pareto}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Layer} & \\textbf{Depth} & \\textbf{EN} & \\textbf{ZS Med.} & \\textbf{ZS Min} & \\textbf{ZS Max} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Qwen3-235B-A22B (94 layers)}} \\\\\n\\midrule\n16 & 17\\% & .672 & .659 & .589 & .678 \\\\\n32 & 34\\% & .738 & .729 & .648 & .751 \\\\\n48 & 51\\% & .781 & .771 & .658 & .793 \\\\\n\\textbf{56} & \\textbf{60\\%} & \\textbf{.798} & \\textbf{.771} & \\textbf{.641} & \\textbf{.801} \\\\\n64 & 68\\% & .816 & .751 & .618 & .788 \\\\\n76 & 81\\% & .838 & .714 & .584 & .756 \\\\\n88 & 94\\% & .818 & .671 & .542 & .712 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Llama 4 Scout (48 layers)}} \\\\\n\\midrule\n8  & 17\\% & .674 & .661 & --- & --- \\\\\n16 & 33\\% & .741 & .738 & --- & --- \\\\\n\\textbf{24} & \\textbf{50\\%} & \\textbf{.788} & \\textbf{.756} & --- & --- \\\\\n32 & 67\\% & .811 & .726 & --- & --- \\\\\n40 & 83\\% & .821 & .698 & --- & --- \\\\\n48 & 100\\% & .798 & .654 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pareto frontier across depth for both architectures. Bold rows indicate the optimal zero-shot transfer layer. EN = English AUROC; ZS = zero-shot transfer AUROC (median across 20 languages). Beyond the optimal transfer layer, EN AUROC continues rising while cross-lingual transfer degrades.}\n\\label{tab:pareto}\n\\end{table}\n\nTable~\\ref{tab:pareto} presents the depth--transferability Pareto frontier on both architectures.\nOn Qwen3-235B, English AUROC peaks at 0.838 (layer~76, 81\\% depth), while the optimal zero-shot transfer layer is layer~56 (60\\% depth) with median AUROC 0.771 across 20 languages.\nMoving from the transfer-optimal layer~56 to the English-optimal layer~76, zero-shot transfer drops from 0.771 to 0.714 ($-5.7$~pp) while English AUROC gains only 4.0~pp.\nThe depth--transfer anticorrelation is robust: Spearman $\\rho = -0.78$ (per-language median; IQR $[-0.84, -0.71]$).\n\nOn Llama~4~Scout, the optimal transfer depth shifts to 50\\% (layer~24), with a steeper frontier ($\\rho = -0.73$).\nScout's shallower optimal depth is consistent with MoE expert routing driving faster language specialization in its 48-layer architecture.\n17/20 languages achieve zero-shot AUROC $> 0.65$ on Qwen3 (16/20 on Scout).\n\nThe resource tier strongly modulates transfer quality.\nOn Qwen3 at the optimal layer, high-resource languages (zh: 0.793, es: 0.801) substantially outperform low-resource languages (sw: 0.641, bn: 0.633), consistent with $\\mathcal{H}$-divergence predictions from domain adaptation theory.\n\n\\subsection{CaCLR Evaluation}\n\\label{sec:exp:caclr}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Labels} & \\textbf{Q-56} & \\textbf{Q-76} & \\textbf{S-24} & \\textbf{S-40} \\\\\n\\midrule\nZero-shot & 0 & .771 & .714 & .756 & .698 \\\\\nMean-shift & 0 & .771 & .714 & .756 & .698 \\\\\nCaCLR$_{\\alpha}$ & 0$^*$ & .798 & .762 & .784 & .745 \\\\\n\\textbf{CaCLR} & \\textbf{0$^*$} & \\textbf{.828} & \\textbf{.788} & \\textbf{.812} & \\textbf{.771} \\\\\nLin.\\ proj.\\ (50) & 50 pairs & .812 & .779 & .798 & .758 \\\\\nFew-shot 25 & 25 & .798 & .761 & .781 & .741 \\\\\nFew-shot 100 & 100 & .821 & .792 & .808 & .778 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Transfer method comparison (median AUROC across 20 languages). Q = Qwen3-235B; S = Llama~4~Scout. Numbers after model indicate layer. $^*$Requires parallel inputs but zero target-language correctness labels. CaCLR$_\\alpha$ = $\\beta=0$ (no consistency loss).}\n\\label{tab:transfer}\n\\end{table}\n\nTable~\\ref{tab:transfer} compares all transfer methods.\nCaCLR achieves median AUROC 0.828 at Qwen3 layer~56 and 0.812 at Scout layer~24---surpassing linear projection by +1.4~pp and nearly matching few-shot 100 ($-0.8$~pp), while requiring zero target-language labels.\nMean-shift yields exactly $\\Delta\\text{AUROC} = 0.000$, confirming our theoretical prediction (Section~\\ref{sec:method:transfer}).\n\nThe $\\beta$ term (MMD consistency loss) provides a meaningful gain of +3.2~pp over the $\\alpha$-only ablation (bootstrap CI: [0.019, 0.045]; paired permutation $p = 0.003$; Cohen's $d = 0.48$).\nTable~\\ref{tab:beta} shows the $\\beta$ sensitivity sweep: $\\beta = 0.1$ is optimal, with lower values providing insufficient distributional constraint and $\\beta = 1.0$ over-regularizing.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n$\\beta$ & $\\Delta$AUROC & $\\Delta$ECE & Note \\\\\n\\midrule\n0.001 & +0.008 & $-$0.003 & Negligible \\\\\n0.01  & +0.019 & $-$0.008 & Marginal \\\\\n\\textbf{0.1} & \\textbf{+0.032} & $\\mathbf{-}$\\textbf{0.014} & \\textbf{Optimal} \\\\\n1.0   & +0.021 & $-$0.011 & Over-regularized \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$\\beta$ sensitivity sweep (Qwen3-235B, layer~56, median across 20 languages). Deltas are relative to $\\alpha$-only ($\\beta=0$).}\n\\label{tab:beta}\n\\end{table}\n\nThe $\\beta$ gain is largest at mid-depth layers (+4.1~pp) and diminishes at deep layers (+2.4~pp) and shallow layers (+1.8~pp).\nThis pattern is explained by CKA analysis (Section~\\ref{sec:exp:cka}): mid-depth layers have sufficient cross-lingual structure for MMD alignment to be effective, while deep-layer misalignment is geometric (directional rotation) rather than merely distributional.\n\nCaCLR reduces non-English ECE by a median of 3.5\\% over temperature scaling (range: [1.2\\%, 6.1\\%]).\nTemperature scaling achieves English ECE of 0.048 (Qwen3) and 0.053 (Scout) from raw ECE of 0.162 and 0.171 respectively, but cannot address cross-lingual representation misalignment.\nCaCLR directly optimizes calibration during training via the SB-ECE term.\n\n\\subsection{Difficulty--Capability Decomposition}\n\\label{sec:exp:decomp}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Depth} & \\textbf{HIGH} & \\textbf{MID} & \\textbf{LOW} & \\textbf{Random} \\\\\n\\midrule\n20\\% & +.012 & +.014 & +.019 & +.001 \\\\\n35\\% & +.016 & +.022 & +.028 & +.002 \\\\\n50\\% & +.021 & +.031 & +.038 & +.002 \\\\\n60\\% & +.024 & +.036 & +.043 & +.003 \\\\\n80\\% & +.028 & +.041 & +.048 & +.003 \\\\\n90\\% & +.022 & +.034 & +.041 & +.002 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$\\Delta$AUROC after difficulty direction removal, by resource tier and depth. Random = random direction control. Difficulty removal consistently improves transfer, especially for low-resource languages at deep layers.}\n\\label{tab:decomp}\n\\end{table}\n\nTable~\\ref{tab:decomp} shows the decomposition results.\nRemoving the difficulty direction from representations before training correctness probes improves cross-lingual transfer by a median of 3.1~pp (bootstrap CI: [1.8, 4.4]; $p = 0.006$; $d = 0.41$).\nThe difficulty direction has moderate cosine similarity with the correctness direction (0.34), confirming partial signal overlap without full redundancy.\nThe difficulty probe achieves $R^2 = 0.68$, validating that difficulty is linearly accessible in the representation space.\n\nTwo patterns emerge.\nFirst, a resource-tier gradient: low-resource languages benefit most from decomposition (+4.1~pp) versus high-resource (+2.2~pp), because low-resource languages have greater difficulty distribution mismatch with English.\nSecond, a depth gradient: deep-layer benefit (4.8~pp at 80\\% depth) exceeds shallow-layer benefit (0.8~pp at 20\\%), because deep layers encode more language-specific difficulty information.\nThe random-direction control yields only +0.2~pp, ruling out dimensionality reduction as a confound.\n\n\\subsection{Cross-Lingual Orthogonality}\n\\label{sec:exp:ortho}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\textbf{Qwen3} & \\textbf{Scout} & \\textbf{Mean} \\\\\n\\midrule\nen & HIGH & .031 & .037 & .034 \\\\\nzh & HIGH & .035 & .041 & .038 \\\\\nes & HIGH & .033 & .039 & .036 \\\\\nde & HIGH & .036 & .042 & .039 \\\\\nhi & MID  & .039 & .045 & .042 \\\\\nru & MID  & .037 & .043 & .040 \\\\\nko & MID  & .041 & .047 & .044 \\\\\ntr & MID  & .043 & .049 & .046 \\\\\nsw & LOW  & .048 & .056 & .052 \\\\\nbn & LOW  & .052 & .058 & .055 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Correctness--confidence cosine similarity across languages and architectures. All values remain below 0.062, confirming universal near-orthogonality.}\n\\label{tab:ortho}\n\\end{table}\n\nTable~\\ref{tab:ortho} reports correctness--confidence cosine similarity across languages.\nAll 20 languages on both architectures show cosine similarity below 0.062 (mean = 0.042; bootstrap CI for mean: [0.035, 0.049]).\nThis extends the English-only finding of Miao \\& Ungar to a universal structural property: verbalized confidence is uninformative about correctness regardless of language or architecture.\n\nA mild resource-tier gradient exists: low-resource languages show slightly higher cosine (0.051 vs.\\ 0.038 for high-resource), likely reflecting noisier confidence direction estimates from sparser training data rather than genuine reduction in orthogonality.\nQwen3 exhibits slightly stronger orthogonality than Scout (mean 0.039 vs.\\ 0.046), possibly because its larger capacity encodes correctness and confidence in more separable subspaces.\n\n\\subsection{CKA Representation Similarity Analysis}\n\\label{sec:exp:cka}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Depth} & \\textbf{HIGH} & \\textbf{MID} & \\textbf{LOW} & \\textbf{ZS AUROC} \\\\\n\\midrule\n10\\% & .93 & .89 & .84 & .618 \\\\\n25\\% & .90 & .85 & .78 & .698 \\\\\n40\\% & .86 & .79 & .69 & .756 \\\\\n50\\% & .82 & .74 & .62 & .771 \\\\\n60\\% & .78 & .69 & .55 & .771 \\\\\n70\\% & .73 & .63 & .47 & .741 \\\\\n80\\% & .67 & .56 & .41 & .714 \\\\\n90\\% & .61 & .49 & .35 & .688 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CKA similarity (EN vs.\\ target, Qwen3-235B) by depth and resource tier, alongside zero-shot transfer AUROC. CKA monotonically decreases with depth and correlates strongly with transfer success.}\n\\label{tab:cka}\n\\end{table}\n\nTable~\\ref{tab:cka} presents CKA similarity between English and target-language representations across depth.\nCKA monotonically decreases with depth across all resource tiers, and correlates strongly with zero-shot transfer AUROC (Pearson $r = 0.82$; CI: [0.76, 0.87]; Spearman $\\rho = 0.79$).\nThis provides a mechanistic explanation for the Pareto frontier: deeper layers have progressively less cross-lingual representational overlap, directly causing transfer degradation.\n\nThe resource-tier gradient in CKA mirrors the transfer gradient: high-resource languages maintain CKA $\\geq 0.61$ even at 90\\% depth, while low-resource languages drop to 0.35.\nThis reflects pretraining data overlap---languages with more shared tokens develop more similar deep representations.\n\nCritically, the CKA analysis reveals why CaCLR's $\\beta$ term has depth-dependent effectiveness.\nAt layers where CKA $< 0.55$, the $\\beta$ term provides diminishing returns because misalignment becomes \\emph{geometric} (the correctness direction rotates 15--35$^\\circ$ across languages) rather than merely distributional (mean/covariance shift).\nMMD corrects distributional shift but cannot learn rotations; this explains why linear projection---which explicitly learns a rotation matrix---remains effective at deep layers.\nAt mid-depth layers (CKA $\\approx 0.62$--$0.78$), misalignment is primarily distributional, and CaCLR's MMD term effectively closes the gap.\n\n\\subsection{Probe Complexity}\n\\label{sec:exp:probe}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Layer} & \\textbf{LR-EN} & \\textbf{MLP-EN} & \\textbf{LR-ZS} & \\textbf{MLP-ZS} \\\\\n\\midrule\n24 & .711 & .722 & .698 & .691 \\\\\n40 & .762 & .778 & .756 & .741 \\\\\n56 & .798 & .814 & .771 & .752 \\\\\n76 & .838 & .852 & .714 & .686 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Logistic regression (LR) vs.\\ 2-layer MLP on Qwen3-235B. MLP achieves higher English AUROC but worse zero-shot transfer, with the gap widening at deeper layers.}\n\\label{tab:probe}\n\\end{table}\n\nTable~\\ref{tab:probe} compares logistic regression and 2-layer MLP probes.\nMLPs achieve +1.4~pp higher English AUROC but suffer 3.6~pp worse zero-shot transfer degradation (median), yielding a net transfer advantage of +2.2~pp for logistic regression.\nThe gap widens at deeper layers (LR advantage: +0.7~pp at layer~24 vs.\\ +2.8~pp at layer~76), because deep-layer representations are more language-specific and MLP's extra capacity overfits to English-specific patterns.\nLogistic regression's linear inductive bias matches the linear structure of correctness directions, supporting its use as the default probe.\n\n\\subsection{Cross-Benchmark Generalization}\n\\label{sec:exp:benchmark}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Benchmark} & \\textbf{ZS} & \\textbf{CaCLR} & $\\rho$ & \\textbf{$>$0.65} \\\\\n\\midrule\nGlobalMMLU & .758 & .808 & $-$.78 & 17/20 \\\\\nBelebele & .731 & .789 & $-$.71 & 15/20 \\\\\nMMLU-ProX & .748 & .801 & $-$.75 & 16/20 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-benchmark generalization (Qwen3-235B, optimal transfer layer). ZS = zero-shot median AUROC; $\\rho$ = Pareto Spearman correlation; $>$0.65 = languages above 0.65 AUROC.}\n\\label{tab:benchmark}\n\\end{table}\n\nTable~\\ref{tab:benchmark} shows that all findings generalize across benchmarks.\nThe Pareto frontier persists on Belebele ($\\rho = -0.71$) and MMLU-ProX ($\\rho = -0.75$).\nCaCLR provides consistent improvement on both (+5.8~pp on Belebele, +5.3~pp on MMLU-ProX).\nCross-benchmark per-language correlation is 0.92, indicating that transfer difficulty is language-inherent rather than benchmark-specific.\n\n\\subsection{Linear Projection Data Efficiency}\n\\label{sec:exp:linproj}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Pairs} & \\textbf{Med.} & $\\Delta$\\textbf{ZS} & \\textbf{\\%200} & \\textbf{HIGH} & \\textbf{LOW} \\\\\n\\midrule\n10  & .762 & +.027 & 88\\% & .781 & .638 \\\\\n20  & .778 & +.043 & 94\\% & .798 & .651 \\\\\n50  & .792 & +.057 & 98\\% & .814 & .664 \\\\\n100 & .796 & +.061 & 99\\% & .818 & .668 \\\\\n200 & .798 & +.063 & 100\\% & .821 & .671 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Linear projection data efficiency. Performance saturates at $\\sim$35 pairs (95\\% of 200-pair performance), with low-resource languages requiring slightly more pairs (48 vs.\\ 22 for high-resource).}\n\\label{tab:linproj}\n\\end{table}\n\nLinear projection saturates rapidly: 50 parallel pairs achieve 98\\% of 200-pair performance (Table~\\ref{tab:linproj}).\nThis reflects the low intrinsic dimensionality of the correctness direction---a rotation/scaling matrix between low-dimensional subspaces needs few examples to estimate.\nLow-resource languages saturate later (48 vs.\\ 22 pairs), consistent with noisier correctness direction estimates.\nCaCLR outperforms 50-pair linear projection by +1.4~pp while requiring no paired data beyond parallel inputs.\n\n\n%---------------------------------------------------------------\n\\section{Discussion}\n\\label{sec:discussion}\n%---------------------------------------------------------------\n\n\\paragraph{Why architecture matters.}\nThe architecture-dependent Pareto shape is not predicted by domain adaptation theory alone.\nMoE models exhibit sharper frontiers because expert routing creates discrete language specialization at depth: specific experts become ``responsible'' for specific languages, accelerating representational divergence.\nDense models (Gemma~4~31B; Appendix~\\ref{app:gemma}) show smoother frontiers ($\\rho = -0.69$, optimal transfer at 75\\% depth), confirming that expert routing is the mechanism.\n\n\\paragraph{When CaCLR works and when it does not.}\nCaCLR is most effective at mid-depth layers where cross-lingual misalignment is distributional.\nAt deep layers (CKA $< 0.55$), geometric misalignment dominates and linear projection is preferable.\nThis provides a practical guideline: use CKA to predict which layer--language combinations will benefit from CaCLR versus requiring geometric alignment.\n\n\\paragraph{The role of resource tier.}\nLow-resource languages consistently show (1)~lower zero-shot transfer, (2)~greater benefit from difficulty decomposition, (3)~greater benefit from CaCLR, and (4)~slightly weaker orthogonality.\nAll patterns are consistent with sparser pretraining representation creating larger distributional gaps that alignment methods can partially close.\n\n\\paragraph{Limitations.}\nOur evaluation uses MCQA benchmarks, which enable clean correctness labeling but may not reflect open-ended generation.\nCaCLR requires parallel inputs (translated items), which are readily available for MCQA but less natural for other tasks.\nINT8 quantization introduces small but nonzero perturbations (max $\\Delta$AUROC = 0.6~pp; Appendix~\\ref{app:int8}).\n\n%---------------------------------------------------------------\n\\section{Conclusion}\n\\label{sec:conclusion}\n%---------------------------------------------------------------\n\nWe presented the first systematic study of cross-lingual correctness probe transfer.\nOur findings form a coherent causal chain: (1)~a depth--transferability Pareto frontier exists with architecture-dependent shape; (2)~difficulty--capability decomposition explains the frontier and identifies where alignment is needed; (3)~CaCLR shifts the frontier via distributional alignment, reducing non-English ECE by 3.5\\% over temperature scaling with zero target-language labels across 20 languages; (4)~correctness--confidence orthogonality universally bounds output-based calibration.\nCKA analysis provides the mechanistic glue, linking representation geometry to transfer success and explaining CaCLR's depth-dependent effectiveness.\nThese results establish probe-based calibration as viable for multilingual settings and provide actionable guidelines for practitioners: select layers based on the architecture-specific Pareto frontier, apply CaCLR at mid-depth layers, and use linear projection when geometric misalignment dominates.\n\n%---------------------------------------------------------------\n\n\\appendix\n\n\\section{INT8 Validation}\n\\label{app:int8}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Layer} & \\textbf{INT8} & \\textbf{FP16} & $\\Delta$ & \\textbf{Cos.} \\\\\n\\midrule\n8  & .674 & .678 & $-$.004 & .991 \\\\\n16 & .741 & .745 & $-$.004 & .989 \\\\\n24 & .788 & .791 & $-$.003 & .992 \\\\\n32 & .811 & .814 & $-$.003 & .990 \\\\\n40 & .821 & .827 & $-$.006 & .987 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{INT8 vs.\\ FP16 on Llama~4~Scout. Cos.\\ = cosine similarity between extracted correctness directions. All differences are within bootstrap noise.}\n\\label{tab:int8}\n\\end{table}\n\nINT8 quantization has negligible impact on correctness probes (Table~\\ref{tab:int8}).\nMaximum AUROC difference is 0.6~pp (layer~40), and correctness direction cosine similarity exceeds 0.987 at all layers.\nECE differences are similarly small (max 0.8~pp).\n\n\\section{Probing Control Tasks}\n\\label{app:control}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Layer} & \\textbf{EN Sel.} & \\textbf{ZH Sel.} & \\textbf{SW Sel.} & \\textbf{Ctrl.} \\\\\n\\midrule\n16 & .248 & .231 & .192 & .512 \\\\\n32 & .281 & .268 & .218 & .519 \\\\\n48 & .309 & .292 & .241 & .524 \\\\\n56 & .318 & .301 & .248 & .521 \\\\\n76 & .341 & .324 & .262 & .538 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Selectivity (probe AUROC $-$ control AUROC) on Qwen3-235B. Ctrl.\\ = control task AUROC (random labels). Minimum selectivity is 0.192, well above the 0.15 threshold.}\n\\label{tab:control}\n\\end{table}\n\nFollowing Hewitt \\& Liang (2019), we validate probe selectivity with random-label control tasks (Table~\\ref{tab:control}).\nControl AUROC ranges from 0.502 to 0.538 (near chance).\nSelectivity (probe AUROC minus control AUROC) has a median of 0.284 and minimum of 0.192, well above the 0.15 threshold.\nThis confirms that probes extract genuine correctness signals rather than exploiting high-dimensional capacity.\n\n\\section{Three-Architecture Comparison}\n\\label{app:gemma}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}llccccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Type} & \\textbf{EN} & \\textbf{ZS} & \\textbf{Opt.\\%} & $\\rho$ \\\\\n\\midrule\nQwen3-235B & MoE & .838 & .758 & 60\\% & $-$.78 \\\\\nLlama 4 Scout & MoE & .821 & .742 & 50\\% & $-$.73 \\\\\nGemma 4 31B & Dense & .809 & .738 & 75\\% & $-$.69 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Three-architecture comparison. Dense architecture (Gemma~4) shows a smoother frontier with deeper optimal transfer, consistent with expert routing driving sharper language specialization in MoE models.}\n\\label{tab:arch}\n\\end{table}\n\nAdding Gemma~4~31B Dense as a camera-ready extension confirms that MoE architectures produce sharper Pareto frontiers than dense models (Table~\\ref{tab:arch}).\nGemma's optimal transfer depth is 75\\% (vs.\\ 60\\% and 50\\% for the MoE models), and its Pareto $\\rho = -0.69$ indicates a smoother frontier with no sharp elbow, consistent with gradual rather than discrete language specialization.\n\n\\section{Extended Language Coverage}\n\\label{app:extended}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Tier} & $n$ & \\textbf{ZS} & \\textbf{CaCLR} & $\\Delta$ \\\\\n\\midrule\nHIGH & 12 & .786 & .828 & +.042 \\\\\nMID & 18 & .741 & .798 & +.057 \\\\\nLOW & 22 & .648 & .721 & +.073 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Extended coverage (52 languages). CaCLR benefit increases with decreasing resource tier.}\n\\label{tab:extended}\n\\end{table}\n\nExpanding to 52 languages confirms all findings at scale (Table~\\ref{tab:extended}).\nCaCLR generalizes across the full language set, with low-resource languages benefiting most (+7.3~pp vs.\\ +4.2~pp for high-resource).\n38/52 languages (73\\%) achieve zero-shot AUROC above 0.65; the Pareto frontier and CaCLR improvements remain robust.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf5b6fdd-6263-4bec-ab9d-92a96a39d92e",
  "isSidechain": false,
  "requestId": "req_011CbEUDjeKMXwYn3eHFFtc4",
  "type": "assistant",
  "uuid": "7e7e1abf-ed8f-4a8e-a42d-3ae193d0fe7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KP1sAvGznnKiUqYjzpdwDL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 154,
      "cache_read_input_tokens": 45451,
      "output_tokens": 11958,
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
          "output_tokens": 11958,
          "cache_read_input_tokens": 45451,
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

_source line 23 · 2026-05-20T20:45:48.828Z_

<details><summary>↩ Tool result · `toolu_016xmw3HAUWTDkiXAD9xKVsZ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e7e1abf-ed8f-4a8e-a42d-3ae193d0fe7a",
  "isSidechain": false,
  "promptId": "d6812199-51cb-4f3b-a1d1-28a2f25b4592",
  "type": "user",
  "uuid": "b623439e-1133-4621-bcb5-908f078cf13c",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{tabularx}\n\n\\title{Cross-Lingual Calibration via Internal Correctness Directions:\\\\Pareto Frontiers, Decomposition, and Consistency-Aligned Probes}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nMultilingual large language models exhibit substantially worse calibration in non-English languages, yet probe-based calibration methods remain English-only.\nWe present the first systematic study of cross-lingual correctness probe transfer across 20 languages on two MoE architectures (Qwen3-235B-A22B, Llama~4~Scout).\nWe discover a \\emph{depth--transferability Pareto frontier}: deeper layers yield higher English probe AUROC but degrade in zero-shot cross-lingual transfer (Spearman $\\rho=-0.78$/$-0.73$).\nThe frontier shape is architecture-dependent, with the optimal transfer depth at 60\\% for Qwen3 versus 50\\% for Scout.\nWe decompose correctness transfer into difficulty-shared and capability-specific components, showing that removing the difficulty direction improves transfer by 3.1~pp (median), with low-resource languages benefiting most (+4.1~pp).\nWe propose CaCLR, a probe training objective combining binary cross-entropy, sample-binned ECE, and an MMD-based cross-lingual consistency loss on parallel activations.\nCaCLR-trained probes reduce non-English ECE by 3.5\\% over temperature scaling with zero target-language labels, matching few-shot (100-label) supervised performance.\nCKA analysis reveals that cross-lingual representation similarity monotonically decreases with depth ($r=0.82$ with transfer AUROC), mechanistically explaining the Pareto frontier.\nFinally, we confirm that correctness--confidence orthogonality (cosine $<0.062$) persists universally across all 20 languages, bounding output-based calibration regardless of language.\n\\end{abstract}\n\n%---------------------------------------------------------------\n\\section{Introduction}\n\\label{sec:intro}\n%---------------------------------------------------------------\n\nCalibration---the alignment between a model's expressed confidence and its actual accuracy---is critical for deploying language models in high-stakes settings.\nRecent work has shown that multilingual LLMs suffer from substantially worse calibration in non-English languages, with expected calibration error (ECE) up to 5$\\times$ higher than English \\cite{}.\nOutput-based calibration methods such as temperature scaling \\cite{guo2017calibration} and verbalized confidence extraction \\cite{} offer post-hoc corrections but face a structural limitation:\n\\citet{} demonstrated that the internal \\emph{correctness direction} (encoding whether the model will answer correctly) is nearly orthogonal to the \\emph{confidence direction} (encoding verbalized confidence), with cosine similarity below 0.04 in English.\nThis orthogonality means output-based signals are fundamentally uninformative about actual correctness.\n\nProbe-based calibration methods---training linear classifiers on internal representations to predict correctness---offer a principled alternative by directly accessing the correctness direction \\cite{}.\nHowever, all existing probe-based methods (CORAL, CCPS, Confidence Manifold, correctness steering) operate exclusively in English.\nThe question of whether correctness probes transfer cross-lingually---enabling calibration in languages without correctness labels---remains open.\n\nWe present the first systematic study of cross-lingual correctness probe transfer.\nOur contributions form a causal chain:\n\n\\paragraph{(1) Pareto Frontier Discovery.}\nWe reveal a depth--transferability Pareto frontier: deeper layers produce better English probes (AUROC up to 0.838) but degrade in zero-shot cross-lingual transfer.\nThe frontier shape is architecture-dependent---optimal transfer depth is 60\\% for Qwen3-235B versus 50\\% for Llama~4~Scout---with MoE expert routing accelerating deep-layer language specialization.\n\n\\paragraph{(2) Difficulty--Capability Decomposition.}\nWe decompose the correctness signal into a difficulty-shared component (language-agnostic, transferable) and a capability-specific component (language-dependent, driving deep-layer degradation).\nRemoving the difficulty direction improves cross-lingual transfer by 3.1~pp median, with low-resource languages benefiting most (+4.1~pp).\n\n\\paragraph{(3) CaCLR: Calibration-Consistent Cross-Lingual Regularization.}\nWe propose CaCLR, a probe training objective that jointly optimizes correctness prediction ($\\mathcal{L}_\\text{BCE}$), calibration ($\\alpha \\cdot \\mathcal{L}_\\text{SB-ECE}$), and cross-lingual distributional alignment ($\\beta \\cdot \\mathcal{L}_\\text{MMD}$) using parallel activations from translated items.\nCaCLR requires zero target-language correctness labels and reduces non-English ECE by 3.5\\% over temperature scaling across 20 languages.\n\n\\paragraph{(4) Cross-Lingual Orthogonality.}\nWe confirm that correctness--confidence orthogonality persists across all 20 languages and both architectures (max cosine = 0.062), establishing that output-based calibration is structurally limited regardless of language.\n\nCKA representation similarity analysis provides the mechanistic glue: cross-lingual CKA monotonically decreases with depth ($r=0.82$ with transfer AUROC), explaining why deeper layers degrade and why CaCLR's distributional matching is most effective at mid-depth layers where misalignment is distributional rather than geometric.\n\n\n%---------------------------------------------------------------\n\\section{Related Work}\n\\label{sec:related}\n%---------------------------------------------------------------\n\n\\paragraph{LLM Calibration.}\nTemperature scaling \\cite{guo2017calibration} remains the dominant post-hoc calibration method.\nRecent work reveals that multilingual LLMs are substantially worse-calibrated in non-English languages.\nLACE proposes per-language layer ensembles but requires target-language labels.\nMKA uses multi-agent knowledge aggregation at 5$\\times$ inference cost.\n\n\\paragraph{Probe-Based Calibration.}\nCORAL trains cross-task English correctness probes and identifies distribution-shift challenges.\nCCPS uses clustering on correctness probe activations.\nMiao \\& Ungar discover correctness--confidence orthogonality and propose steering-based calibration, but only for English on 7--8B models.\nAll probe-based methods remain monolingual.\n\n\\paragraph{Cross-Lingual Probe Transfer.}\nXiao et al.\\ transfer \\emph{knowledge boundary} probes (input-level answerability) across 8 languages.\nKnowledge boundary is fundamentally different from correctness: answerability is an input property (does the model have relevant knowledge?) while correctness is output-dependent (will the model produce the right answer for this input?).\nTheir success with mean-shift alignment is not expected to transfer to correctness probes, and we formally prove why (Section~\\ref{sec:method:transfer}).\nCivelli et al.\\ study cross-lingual \\emph{difficulty} probes, which we use as a control in our decomposition analysis.\n\n\\paragraph{Domain Adaptation Theory.}\nBen-David et al.'s $\\mathcal{H}$-divergence framework predicts that cross-domain transfer degrades with increasing domain divergence.\nWe derive predictions from this framework and test them: the resource-tier gradient follows theory, but the architecture-dependent Pareto shape and difficulty--capability entanglement are novel findings.\n\n\\paragraph{Representation Similarity.}\nCKA \\cite{kornblith2019similarity} measures representational similarity between network layers.\nWe use CKA to mechanistically explain the Pareto frontier by quantifying cross-lingual representation divergence at each depth.\n\n\\paragraph{Cross-Lingual Alignment.}\nLinear cross-lingual alignment methods (MUSE, VecMap) learn rotation matrices between embedding spaces.\nOur linear projection baseline is conceptually similar; CaCLR's distributional matching via MMD represents the alternative alignment paradigm.\n\n\\paragraph{Conformal Prediction.}\nDistribution-free conformal prediction provides coverage guarantees but requires calibration data per language.\nOur approach targets zero-label transfer, making the two complementary.\n\n\n%---------------------------------------------------------------\n\\section{Method}\n\\label{sec:method}\n%---------------------------------------------------------------\n\n\\subsection{Correctness Probes}\n\\label{sec:method:probes}\n\nGiven a multilingual LLM with $L$ layers, we extract the hidden representation $\\mathbf{h}_\\ell \\in \\mathbb{R}^d$ at layer $\\ell$ for each input.\nA correctness probe $f_\\ell: \\mathbb{R}^d \\to [0,1]$ is a logistic regression classifier trained on English data to predict whether the model's generated answer is correct:\n\\begin{equation}\n    f_\\ell(\\mathbf{h}) = \\sigma(\\mathbf{w}_\\ell^\\top \\mathbf{h} + b_\\ell)\n\\end{equation}\nwhere $\\mathbf{w}_\\ell \\in \\mathbb{R}^d$ defines the \\emph{correctness direction} at layer $\\ell$.\nWe evaluate probes via AUROC (discrimination) and ECE (calibration).\n\n\\subsection{Cross-Lingual Transfer}\n\\label{sec:method:transfer}\n\nWe apply English-trained probes directly to target-language representations (zero-shot transfer).\nWe also evaluate several alignment strategies:\n\n\\paragraph{Mean-Shift.}\nSubtract the English mean and add the target-language mean of representations.\nUnder StandardScaler preprocessing + logistic regression, mean-shift adds a constant offset to all logits.\nSince AUROC is rank-invariant, $\\Delta\\text{AUROC} \\equiv 0$ mathematically---mean-shift cannot improve discrimination under this pipeline.\n\n\\paragraph{Linear Projection.}\nLearn a linear map $\\mathbf{A} \\in \\mathbb{R}^{d \\times d}$ from parallel English--target representation pairs to align the target-language representations to the English correctness subspace.\n\n\\paragraph{Few-Shot.}\nFine-tune probes with 25 or 100 labeled target-language examples.\n\n\\subsection{CaCLR: Calibration-Consistent Cross-Lingual Regularization}\n\\label{sec:method:caclr}\n\nCaCLR trains correctness probes with a composite loss:\n\\begin{equation}\n    \\mathcal{L}_\\text{CaCLR} = \\mathcal{L}_\\text{BCE} + \\alpha \\cdot \\mathcal{L}_\\text{SB-ECE} + \\beta \\cdot \\mathcal{L}_\\text{MMD}\n\\end{equation}\n\n\\noindent where:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item $\\mathcal{L}_\\text{BCE}$: binary cross-entropy on English correctness labels.\n    \\item $\\mathcal{L}_\\text{SB-ECE}$: sample-binned ECE, a differentiable calibration loss.\n    \\item $\\mathcal{L}_\\text{MMD}$: maximum mean discrepancy between English and target-language \\emph{probe activations} on parallel inputs (GlobalMMLU train-split translations). This encourages the probe to produce similar output distributions for semantically equivalent inputs across languages.\n\\end{itemize}\n\nThe MMD term aligns distributional properties (mean, covariance) of probe activations without requiring target-language correctness labels---only parallel inputs.\nWe set $\\alpha=1.0$ and $\\beta=0.1$ based on hyperparameter sweeps (Section~\\ref{sec:exp:caclr}).\n\n\\subsection{Difficulty--Capability Decomposition}\n\\label{sec:method:decomp}\n\nWe hypothesize that the correctness signal mixes two components:\n(1)~a \\emph{difficulty-shared} component reflecting item difficulty (language-agnostic), and\n(2)~a \\emph{capability-specific} component reflecting the model's language-specific ability (drives deep-layer transfer degradation).\n\nWe operationalize this via IRT difficulty probes: train a probe to predict item difficulty (from IRT parameters), extract the difficulty direction $\\mathbf{d}_\\ell$, project it out of representations, and retrain correctness probes on the residual.\nImproved transfer on residual representations confirms that difficulty entanglement degrades cross-lingual transfer.\nA random-direction control validates that the improvement is specific to difficulty removal, not arbitrary dimensionality reduction.\n\n%---------------------------------------------------------------\n\\section{Experimental Setup}\n\\label{sec:setup}\n%---------------------------------------------------------------\n\n\\paragraph{Models.}\nQwen3-235B-A22B (94 layers, MoE, INT8) and Llama~4~Scout (48 layers, MoE, INT8).\nWe probe every 4th layer: 24 layers for Qwen3, 12 for Scout.\n\n\\paragraph{Languages.}\n20 languages spanning three resource tiers: HIGH (en, zh, es, fr, de), MID (hi, ru, ko, tr, and 5 others), LOW (sw, bn, and 8 others).\n\n\\paragraph{Benchmarks.}\nPrimary: GlobalMMLU (multilingual MCQA).\nGeneralization: Belebele (reading comprehension), MMLU-ProX (knowledge QA).\n\n\\paragraph{Probes.}\nLogistic regression with StandardScaler preprocessing.\nWe validate this choice against 2-layer MLPs (Section~\\ref{sec:exp:probe}).\n\n\\paragraph{Evaluation.}\nAUROC for discrimination, ECE for calibration.\nAll comparisons include bootstrap CIs (1000 resamples) and paired permutation tests.\nEffect sizes reported with Cohen's $d$.\n\n\\paragraph{Transfer Conditions.}\nZero-shot, mean-shift, linear projection (50 parallel pairs), few-shot (25/100 labels), and CaCLR.\n\n%---------------------------------------------------------------\n\\section{Results}\n\\label{sec:results}\n%---------------------------------------------------------------\n\n\\subsection{Pareto Frontier Discovery}\n\\label{sec:exp:pareto}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Layer} & \\textbf{Depth} & \\textbf{EN} & \\textbf{ZS Med.} & \\textbf{ZS Min} & \\textbf{ZS Max} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Qwen3-235B-A22B (94 layers)}} \\\\\n\\midrule\n16 & 17\\% & .672 & .659 & .589 & .678 \\\\\n32 & 34\\% & .738 & .729 & .648 & .751 \\\\\n48 & 51\\% & .781 & .771 & .658 & .793 \\\\\n\\textbf{56} & \\textbf{60\\%} & \\textbf{.798} & \\textbf{.771} & \\textbf{.641} & \\textbf{.801} \\\\\n64 & 68\\% & .816 & .751 & .618 & .788 \\\\\n76 & 81\\% & .838 & .714 & .584 & .756 \\\\\n88 & 94\\% & .818 & .671 & .542 & .712 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Llama 4 Scout (48 layers)}} \\\\\n\\midrule\n8  & 17\\% & .674 & .661 & --- & --- \\\\\n16 & 33\\% & .741 & .738 & --- & --- \\\\\n\\textbf{24} & \\textbf{50\\%} & \\textbf{.788} & \\textbf{.756} & --- & --- \\\\\n32 & 67\\% & .811 & .726 & --- & --- \\\\\n40 & 83\\% & .821 & .698 & --- & --- \\\\\n48 & 100\\% & .798 & .654 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pareto frontier across depth for both architectures. Bold rows indicate the optimal zero-shot transfer layer. EN = English AUROC; ZS = zero-shot transfer AUROC (median across 20 languages). Beyond the optimal transfer layer, EN AUROC continues rising while cross-lingual transfer degrades.}\n\\label{tab:pareto}\n\\end{table}\n\nTable~\\ref{tab:pareto} presents the depth--transferability Pareto frontier on both architectures.\nOn Qwen3-235B, English AUROC peaks at 0.838 (layer~76, 81\\% depth), while the optimal zero-shot transfer layer is layer~56 (60\\% depth) with median AUROC 0.771 across 20 languages.\nMoving from the transfer-optimal layer~56 to the English-optimal layer~76, zero-shot transfer drops from 0.771 to 0.714 ($-5.7$~pp) while English AUROC gains only 4.0~pp.\nThe depth--transfer anticorrelation is robust: Spearman $\\rho = -0.78$ (per-language median; IQR $[-0.84, -0.71]$).\n\nOn Llama~4~Scout, the optimal transfer depth shifts to 50\\% (layer~24), with a steeper frontier ($\\rho = -0.73$).\nScout's shallower optimal depth is consistent with MoE expert routing driving faster language specialization in its 48-layer architecture.\n17/20 languages achieve zero-shot AUROC $> 0.65$ on Qwen3 (16/20 on Scout).\n\nThe resource tier strongly modulates transfer quality.\nOn Qwen3 at the optimal layer, high-resource languages (zh: 0.793, es: 0.801) substantially outperform low-resource languages (sw: 0.641, bn: 0.633), consistent with $\\mathcal{H}$-divergence predictions from domain adaptation theory.\n\n\\subsection{CaCLR Evaluation}\n\\label{sec:exp:caclr}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Labels} & \\textbf{Q-56} & \\textbf{Q-76} & \\textbf{S-24} & \\textbf{S-40} \\\\\n\\midrule\nZero-shot & 0 & .771 & .714 & .756 & .698 \\\\\nMean-shift & 0 & .771 & .714 & .756 & .698 \\\\\nCaCLR$_{\\alpha}$ & 0$^*$ & .798 & .762 & .784 & .745 \\\\\n\\textbf{CaCLR} & \\textbf{0$^*$} & \\textbf{.828} & \\textbf{.788} & \\textbf{.812} & \\textbf{.771} \\\\\nLin.\\ proj.\\ (50) & 50 pairs & .812 & .779 & .798 & .758 \\\\\nFew-shot 25 & 25 & .798 & .761 & .781 & .741 \\\\\nFew-shot 100 & 100 & .821 & .792 & .808 & .778 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Transfer method comparison (median AUROC across 20 languages). Q = Qwen3-235B; S = Llama~4~Scout. Numbers after model indicate layer. $^*$Requires parallel inputs but zero target-language correctness labels. CaCLR$_\\alpha$ = $\\beta=0$ (no consistency loss).}\n\\label{tab:transfer}\n\\end{table}\n\nTable~\\ref{tab:transfer} compares all transfer methods.\nCaCLR achieves median AUROC 0.828 at Qwen3 layer~56 and 0.812 at Scout layer~24---surpassing linear projection by +1.4~pp and nearly matching few-shot 100 ($-0.8$~pp), while requiring zero target-language labels.\nMean-shift yields exactly $\\Delta\\text{AUROC} = 0.000$, confirming our theoretical prediction (Section~\\ref{sec:method:transfer}).\n\nThe $\\beta$ term (MMD consistency loss) provides a meaningful gain of +3.2~pp over the $\\alpha$-only ablation (bootstrap CI: [0.019, 0.045]; paired permutation $p = 0.003$; Cohen's $d = 0.48$).\nTable~\\ref{tab:beta} shows the $\\beta$ sensitivity sweep: $\\beta = 0.1$ is optimal, with lower values providing insufficient distributional constraint and $\\beta = 1.0$ over-regularizing.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n$\\beta$ & $\\Delta$AUROC & $\\Delta$ECE & Note \\\\\n\\midrule\n0.001 & +0.008 & $-$0.003 & Negligible \\\\\n0.01  & +0.019 & $-$0.008 & Marginal \\\\\n\\textbf{0.1} & \\textbf{+0.032} & $\\mathbf{-}$\\textbf{0.014} & \\textbf{Optimal} \\\\\n1.0   & +0.021 & $-$0.011 & Over-regularized \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$\\beta$ sensitivity sweep (Qwen3-235B, layer~56, median across 20 languages). Deltas are relative to $\\alpha$-only ($\\beta=0$).}\n\\label{tab:beta}\n\\end{table}\n\nThe $\\beta$ gain is largest at mid-depth layers (+4.1~pp) and diminishes at deep layers (+2.4~pp) and shallow layers (+1.8~pp).\nThis pattern is explained by CKA analysis (Section~\\ref{sec:exp:cka}): mid-depth layers have sufficient cross-lingual structure for MMD alignment to be effective, while deep-layer misalignment is geometric (directional rotation) rather than merely distributional.\n\nCaCLR reduces non-English ECE by a median of 3.5\\% over temperature scaling (range: [1.2\\%, 6.1\\%]).\nTemperature scaling achieves English ECE of 0.048 (Qwen3) and 0.053 (Scout) from raw ECE of 0.162 and 0.171 respectively, but cannot address cross-lingual representation misalignment.\nCaCLR directly optimizes calibration during training via the SB-ECE term.\n\n\\subsection{Difficulty--Capability Decomposition}\n\\label{sec:exp:decomp}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Depth} & \\textbf{HIGH} & \\textbf{MID} & \\textbf{LOW} & \\textbf{Random} \\\\\n\\midrule\n20\\% & +.012 & +.014 & +.019 & +.001 \\\\\n35\\% & +.016 & +.022 & +.028 & +.002 \\\\\n50\\% & +.021 & +.031 & +.038 & +.002 \\\\\n60\\% & +.024 & +.036 & +.043 & +.003 \\\\\n80\\% & +.028 & +.041 & +.048 & +.003 \\\\\n90\\% & +.022 & +.034 & +.041 & +.002 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$\\Delta$AUROC after difficulty direction removal, by resource tier and depth. Random = random direction control. Difficulty removal consistently improves transfer, especially for low-resource languages at deep layers.}\n\\label{tab:decomp}\n\\end{table}\n\nTable~\\ref{tab:decomp} shows the decomposition results.\nRemoving the difficulty direction from representations before training correctness probes improves cross-lingual transfer by a median of 3.1~pp (bootstrap CI: [1.8, 4.4]; $p = 0.006$; $d = 0.41$).\nThe difficulty direction has moderate cosine similarity with the correctness direction (0.34), confirming partial signal overlap without full redundancy.\nThe difficulty probe achieves $R^2 = 0.68$, validating that difficulty is linearly accessible in the representation space.\n\nTwo patterns emerge.\nFirst, a resource-tier gradient: low-resource languages benefit most from decomposition (+4.1~pp) versus high-resource (+2.2~pp), because low-resource languages have greater difficulty distribution mismatch with English.\nSecond, a depth gradient: deep-layer benefit (4.8~pp at 80\\% depth) exceeds shallow-layer benefit (0.8~pp at 20\\%), because deep layers encode more language-specific difficulty information.\nThe random-direction control yields only +0.2~pp, ruling out dimensionality reduction as a confound.\n\n\\subsection{Cross-Lingual Orthogonality}\n\\label{sec:exp:ortho}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\textbf{Qwen3} & \\textbf{Scout} & \\textbf{Mean} \\\\\n\\midrule\nen & HIGH & .031 & .037 & .034 \\\\\nzh & HIGH & .035 & .041 & .038 \\\\\nes & HIGH & .033 & .039 & .036 \\\\\nde & HIGH & .036 & .042 & .039 \\\\\nhi & MID  & .039 & .045 & .042 \\\\\nru & MID  & .037 & .043 & .040 \\\\\nko & MID  & .041 & .047 & .044 \\\\\ntr & MID  & .043 & .049 & .046 \\\\\nsw & LOW  & .048 & .056 & .052 \\\\\nbn & LOW  & .052 & .058 & .055 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Correctness--confidence cosine similarity across languages and architectures. All values remain below 0.062, confirming universal near-orthogonality.}\n\\label{tab:ortho}\n\\end{table}\n\nTable~\\ref{tab:ortho} reports correctness--confidence cosine similarity across languages.\nAll 20 languages on both architectures show cosine similarity below 0.062 (mean = 0.042; bootstrap CI for mean: [0.035, 0.049]).\nThis extends the English-only finding of Miao \\& Ungar to a universal structural property: verbalized confidence is uninformative about correctness regardless of language or architecture.\n\nA mild resource-tier gradient exists: low-resource languages show slightly higher cosine (0.051 vs.\\ 0.038 for high-resource), likely reflecting noisier confidence direction estimates from sparser training data rather than genuine reduction in orthogonality.\nQwen3 exhibits slightly stronger orthogonality than Scout (mean 0.039 vs.\\ 0.046), possibly because its larger capacity encodes correctness and confidence in more separable subspaces.\n\n\\subsection{CKA Representation Similarity Analysis}\n\\label{sec:exp:cka}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Depth} & \\textbf{HIGH} & \\textbf{MID} & \\textbf{LOW} & \\textbf{ZS AUROC} \\\\\n\\midrule\n10\\% & .93 & .89 & .84 & .618 \\\\\n25\\% & .90 & .85 & .78 & .698 \\\\\n40\\% & .86 & .79 & .69 & .756 \\\\\n50\\% & .82 & .74 & .62 & .771 \\\\\n60\\% & .78 & .69 & .55 & .771 \\\\\n70\\% & .73 & .63 & .47 & .741 \\\\\n80\\% & .67 & .56 & .41 & .714 \\\\\n90\\% & .61 & .49 & .35 & .688 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CKA similarity (EN vs.\\ target, Qwen3-235B) by depth and resource tier, alongside zero-shot transfer AUROC. CKA monotonically decreases with depth and correlates strongly with transfer success.}\n\\label{tab:cka}\n\\end{table}\n\nTable~\\ref{tab:cka} presents CKA similarity between English and target-language representations across depth.\nCKA monotonically decreases with depth across all resource tiers, and correlates strongly with zero-shot transfer AUROC (Pearson $r = 0.82$; CI: [0.76, 0.87]; Spearman $\\rho = 0.79$).\nThis provides a mechanistic explanation for the Pareto frontier: deeper layers have progressively less cross-lingual representational overlap, directly causing transfer degradation.\n\nThe resource-tier gradient in CKA mirrors the transfer gradient: high-resource languages maintain CKA $\\geq 0.61$ even at 90\\% depth, while low-resource languages drop to 0.35.\nThis reflects pretraining data overlap---languages with more shared tokens develop more similar deep representations.\n\nCritically, the CKA analysis reveals why CaCLR's $\\beta$ term has depth-dependent effectiveness.\nAt layers where CKA $< 0.55$, the $\\beta$ term provides diminishing returns because misalignment becomes \\emph{geometric} (the correctness direction rotates 15--35$^\\circ$ across languages) rather than merely distributional (mean/covariance shift).\nMMD corrects distributional shift but cannot learn rotations; this explains why linear projection---which explicitly learns a rotation matrix---remains effective at deep layers.\nAt mid-depth layers (CKA $\\approx 0.62$--$0.78$), misalignment is primarily distributional, and CaCLR's MMD term effectively closes the gap.\n\n\\subsection{Probe Complexity}\n\\label{sec:exp:probe}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Layer} & \\textbf{LR-EN} & \\textbf{MLP-EN} & \\textbf{LR-ZS} & \\textbf{MLP-ZS} \\\\\n\\midrule\n24 & .711 & .722 & .698 & .691 \\\\\n40 & .762 & .778 & .756 & .741 \\\\\n56 & .798 & .814 & .771 & .752 \\\\\n76 & .838 & .852 & .714 & .686 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Logistic regression (LR) vs.\\ 2-layer MLP on Qwen3-235B. MLP achieves higher English AUROC but worse zero-shot transfer, with the gap widening at deeper layers.}\n\\label{tab:probe}\n\\end{table}\n\nTable~\\ref{tab:probe} compares logistic regression and 2-layer MLP probes.\nMLPs achieve +1.4~pp higher English AUROC but suffer 3.6~pp worse zero-shot transfer degradation (median), yielding a net transfer advantage of +2.2~pp for logistic regression.\nThe gap widens at deeper layers (LR advantage: +0.7~pp at layer~24 vs.\\ +2.8~pp at layer~76), because deep-layer representations are more language-specific and MLP's extra capacity overfits to English-specific patterns.\nLogistic regression's linear inductive bias matches the linear structure of correctness directions, supporting its use as the default probe.\n\n\\subsection{Cross-Benchmark Generalization}\n\\label{sec:exp:benchmark}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Benchmark} & \\textbf{ZS} & \\textbf{CaCLR} & $\\rho$ & \\textbf{$>$0.65} \\\\\n\\midrule\nGlobalMMLU & .758 & .808 & $-$.78 & 17/20 \\\\\nBelebele & .731 & .789 & $-$.71 & 15/20 \\\\\nMMLU-ProX & .748 & .801 & $-$.75 & 16/20 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-benchmark generalization (Qwen3-235B, optimal transfer layer). ZS = zero-shot median AUROC; $\\rho$ = Pareto Spearman correlation; $>$0.65 = languages above 0.65 AUROC.}\n\\label{tab:benchmark}\n\\end{table}\n\nTable~\\ref{tab:benchmark} shows that all findings generalize across benchmarks.\nThe Pareto frontier persists on Belebele ($\\rho = -0.71$) and MMLU-ProX ($\\rho = -0.75$).\nCaCLR provides consistent improvement on both (+5.8~pp on Belebele, +5.3~pp on MMLU-ProX).\nCross-benchmark per-language correlation is 0.92, indicating that transfer difficulty is language-inherent rather than benchmark-specific.\n\n\\subsection{Linear Projection Data Efficiency}\n\\label{sec:exp:linproj}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Pairs} & \\textbf{Med.} & $\\Delta$\\textbf{ZS} & \\textbf{\\%200} & \\textbf{HIGH} & \\textbf{LOW} \\\\\n\\midrule\n10  & .762 & +.027 & 88\\% & .781 & .638 \\\\\n20  & .778 & +.043 & 94\\% & .798 & .651 \\\\\n50  & .792 & +.057 & 98\\% & .814 & .664 \\\\\n100 & .796 & +.061 & 99\\% & .818 & .668 \\\\\n200 & .798 & +.063 & 100\\% & .821 & .671 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Linear projection data efficiency. Performance saturates at $\\sim$35 pairs (95\\% of 200-pair performance), with low-resource languages requiring slightly more pairs (48 vs.\\ 22 for high-resource).}\n\\label{tab:linproj}\n\\end{table}\n\nLinear projection saturates rapidly: 50 parallel pairs achieve 98\\% of 200-pair performance (Table~\\ref{tab:linproj}).\nThis reflects the low intrinsic dimensionality of the correctness direction---a rotation/scaling matrix between low-dimensional subspaces needs few examples to estimate.\nLow-resource languages saturate later (48 vs.\\ 22 pairs), consistent with noisier correctness direction estimates.\nCaCLR outperforms 50-pair linear projection by +1.4~pp while requiring no paired data beyond parallel inputs.\n\n\n%---------------------------------------------------------------\n\\section{Discussion}\n\\label{sec:discussion}\n%---------------------------------------------------------------\n\n\\paragraph{Why architecture matters.}\nThe architecture-dependent Pareto shape is not predicted by domain adaptation theory alone.\nMoE models exhibit sharper frontiers because expert routing creates discrete language specialization at depth: specific experts become ``responsible'' for specific languages, accelerating representational divergence.\nDense models (Gemma~4~31B; Appendix~\\ref{app:gemma}) show smoother frontiers ($\\rho = -0.69$, optimal transfer at 75\\% depth), confirming that expert routing is the mechanism.\n\n\\paragraph{When CaCLR works and when it does not.}\nCaCLR is most effective at mid-depth layers where cross-lingual misalignment is distributional.\nAt deep layers (CKA $< 0.55$), geometric misalignment dominates and linear projection is preferable.\nThis provides a practical guideline: use CKA to predict which layer--language combinations will benefit from CaCLR versus requiring geometric alignment.\n\n\\paragraph{The role of resource tier.}\nLow-resource languages consistently show (1)~lower zero-shot transfer, (2)~greater benefit from difficulty decomposition, (3)~greater benefit from CaCLR, and (4)~slightly weaker orthogonality.\nAll patterns are consistent with sparser pretraining representation creating larger distributional gaps that alignment methods can partially close.\n\n\\paragraph{Limitations.}\nOur evaluation uses MCQA benchmarks, which enable clean correctness labeling but may not reflect open-ended generation.\nCaCLR requires parallel inputs (translated items), which are readily available for MCQA but less natural for other tasks.\nINT8 quantization introduces small but nonzero perturbations (max $\\Delta$AUROC = 0.6~pp; Appendix~\\ref{app:int8}).\n\n%---------------------------------------------------------------\n\\section{Conclusion}\n\\label{sec:conclusion}\n%---------------------------------------------------------------\n\nWe presented the first systematic study of cross-lingual correctness probe transfer.\nOur findings form a coherent causal chain: (1)~a depth--transferability Pareto frontier exists with architecture-dependent shape; (2)~difficulty--capability decomposition explains the frontier and identifies where alignment is needed; (3)~CaCLR shifts the frontier via distributional alignment, reducing non-English ECE by 3.5\\% over temperature scaling with zero target-language labels across 20 languages; (4)~correctness--confidence orthogonality universally bounds output-based calibration.\nCKA analysis provides the mechanistic glue, linking representation geometry to transfer success and explaining CaCLR's depth-dependent effectiveness.\nThese results establish probe-based calibration as viable for multilingual settings and provide actionable guidelines for practitioners: select layers based on the architecture-specific Pareto frontier, apply CaCLR at mid-depth layers, and use linear projection when geometric misalignment dominates.\n\n%---------------------------------------------------------------\n\n\\appendix\n\n\\section{INT8 Validation}\n\\label{app:int8}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Layer} & \\textbf{INT8} & \\textbf{FP16} & $\\Delta$ & \\textbf{Cos.} \\\\\n\\midrule\n8  & .674 & .678 & $-$.004 & .991 \\\\\n16 & .741 & .745 & $-$.004 & .989 \\\\\n24 & .788 & .791 & $-$.003 & .992 \\\\\n32 & .811 & .814 & $-$.003 & .990 \\\\\n40 & .821 & .827 & $-$.006 & .987 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{INT8 vs.\\ FP16 on Llama~4~Scout. Cos.\\ = cosine similarity between extracted correctness directions. All differences are within bootstrap noise.}\n\\label{tab:int8}\n\\end{table}\n\nINT8 quantization has negligible impact on correctness probes (Table~\\ref{tab:int8}).\nMaximum AUROC difference is 0.6~pp (layer~40), and correctness direction cosine similarity exceeds 0.987 at all layers.\nECE differences are similarly small (max 0.8~pp).\n\n\\section{Probing Control Tasks}\n\\label{app:control}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Layer} & \\textbf{EN Sel.} & \\textbf{ZH Sel.} & \\textbf{SW Sel.} & \\textbf{Ctrl.} \\\\\n\\midrule\n16 & .248 & .231 & .192 & .512 \\\\\n32 & .281 & .268 & .218 & .519 \\\\\n48 & .309 & .292 & .241 & .524 \\\\\n56 & .318 & .301 & .248 & .521 \\\\\n76 & .341 & .324 & .262 & .538 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Selectivity (probe AUROC $-$ control AUROC) on Qwen3-235B. Ctrl.\\ = control task AUROC (random labels). Minimum selectivity is 0.192, well above the 0.15 threshold.}\n\\label{tab:control}\n\\end{table}\n\nFollowing Hewitt \\& Liang (2019), we validate probe selectivity with random-label control tasks (Table~\\ref{tab:control}).\nControl AUROC ranges from 0.502 to 0.538 (near chance).\nSelectivity (probe AUROC minus control AUROC) has a median of 0.284 and minimum of 0.192, well above the 0.15 threshold.\nThis confirms that probes extract genuine correctness signals rather than exploiting high-dimensional capacity.\n\n\\section{Three-Architecture Comparison}\n\\label{app:gemma}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}llccccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Type} & \\textbf{EN} & \\textbf{ZS} & \\textbf{Opt.\\%} & $\\rho$ \\\\\n\\midrule\nQwen3-235B & MoE & .838 & .758 & 60\\% & $-$.78 \\\\\nLlama 4 Scout & MoE & .821 & .742 & 50\\% & $-$.73 \\\\\nGemma 4 31B & Dense & .809 & .738 & 75\\% & $-$.69 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Three-architecture comparison. Dense architecture (Gemma~4) shows a smoother frontier with deeper optimal transfer, consistent with expert routing driving sharper language specialization in MoE models.}\n\\label{tab:arch}\n\\end{table}\n\nAdding Gemma~4~31B Dense as a camera-ready extension confirms that MoE architectures produce sharper Pareto frontiers than dense models (Table~\\ref{tab:arch}).\nGemma's optimal transfer depth is 75\\% (vs.\\ 60\\% and 50\\% for the MoE models), and its Pareto $\\rho = -0.69$ indicates a smoother frontier with no sharp elbow, consistent with gradual rather than discrete language specialization.\n\n\\section{Extended Language Coverage}\n\\label{app:extended}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Tier} & $n$ & \\textbf{ZS} & \\textbf{CaCLR} & $\\Delta$ \\\\\n\\midrule\nHIGH & 12 & .786 & .828 & +.042 \\\\\nMID & 18 & .741 & .798 & +.057 \\\\\nLOW & 22 & .648 & .721 & +.073 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Extended coverage (52 languages). CaCLR benefit increases with decreasing resource tier.}\n\\label{tab:extended}\n\\end{table}\n\nExpanding to 52 languages confirms all findings at scale (Table~\\ref{tab:extended}).\nCaCLR generalizes across the full language set, with low-resource languages benefiting most (+7.3~pp vs.\\ +4.2~pp for high-resource).\n38/52 languages (73\\%) achieve zero-shot AUROC above 0.65; the Pareto frontier and CaCLR improvements remain robust.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "7e7e1abf-ed8f-4a8e-a42d-3ae193d0fe7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T201854 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direct…",
  "leafUuid": "b623439e-1133-4621-bcb5-908f078cf13c",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate calibration research paper with CaCLR method",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571"
}
```

---

### Tool call

_source line 26 · 2026-05-20T20:45:52.451Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QBHM5SDJNGm1B5vjQG8R7s`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best && touch references.bib && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b623439e-1133-4621-bcb5-908f078cf13c",
  "isSidechain": false,
  "requestId": "req_011CbEUVVcAZuMTxoqbtw3S6",
  "type": "assistant",
  "uuid": "2ef4d8ef-76da-4ebc-948a-5b692d9732d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kGzKe4wwsCf5Dev18ueMc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12022,
      "cache_read_input_tokens": 45605,
      "output_tokens": 150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12022,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 150,
          "cache_read_input_tokens": 45605,
          "cache_creation_input_tokens": 12022,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12022
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

_source line 27 · 2026-05-20T20:45:52.621Z_

<details><summary>↩ Tool result · `toolu_01QBHM5SDJNGm1B5vjQG8R7s`</summary>

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

! LaTeX Error: File `acl.sty' not found.

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
  "parentUuid": "2ef4d8ef-76da-4ebc-948a-5b692d9732d3",
  "isSidechain": false,
  "promptId": "d6812199-51cb-4f3b-a1d1-28a2f25b4592",
  "type": "user",
  "uuid": "c0583489-38ba-4876-8789-0e1bf6a1d97e",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "2ef4d8ef-76da-4ebc-948a-5b692d9732d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-20T20:45:55.953Z_

<details><summary>Logged reasoning block</summary>

```text
The ACL style file isn't available. Let me switch to a standard article class format instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0583489-38ba-4876-8789-0e1bf6a1d97e",
  "isSidechain": false,
  "requestId": "req_011CbEUVmd5JioaxE4Ex47m9",
  "type": "assistant",
  "uuid": "d627e88b-ac81-47af-aa5d-06578fc3e998",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XAVLu9HUG3K8LmQbLRRvoC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 431,
      "cache_read_input_tokens": 57627,
      "output_tokens": 530,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 530,
          "cache_read_input_tokens": 57627,
          "cache_creation_input_tokens": 431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 431
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

_source line 29 · 2026-05-20T20:45:56.451Z_

ACL style file not available. Switching to standard article class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d627e88b-ac81-47af-aa5d-06578fc3e998",
  "isSidechain": false,
  "requestId": "req_011CbEUVmd5JioaxE4Ex47m9",
  "type": "assistant",
  "uuid": "0fffa140-c41c-43fa-a6ed-9ffc2525aea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XAVLu9HUG3K8LmQbLRRvoC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 431,
      "cache_read_input_tokens": 57627,
      "output_tokens": 530,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 530,
          "cache_read_input_tokens": 57627,
          "cache_creation_input_tokens": 431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 431
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

_source line 30 · 2026-05-20T20:46:00.501Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01BY5svoFrQU2eKZKteESsy8`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{tabularx}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{tabularx}\n\\usepackage{natbib}\n\\usepackage[colorlinks,citecolor=blue,urlcolor=blue]{hyperref}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fffa140-c41c-43fa-a6ed-9ffc2525aea2",
  "isSidechain": false,
  "requestId": "req_011CbEUVmd5JioaxE4Ex47m9",
  "type": "assistant",
  "uuid": "5aafef72-99a1-453a-9690-65fb53240a66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XAVLu9HUG3K8LmQbLRRvoC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 431,
      "cache_read_input_tokens": 57627,
      "output_tokens": 530,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 530,
          "cache_read_input_tokens": 57627,
          "cache_creation_input_tokens": 431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 431
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

_source line 31 · 2026-05-20T20:46:00.522Z_

<details><summary>↩ Tool result · `toolu_01BY5svoFrQU2eKZKteESsy8`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5aafef72-99a1-453a-9690-65fb53240a66",
  "isSidechain": false,
  "promptId": "d6812199-51cb-4f3b-a1d1-28a2f25b4592",
  "type": "user",
  "uuid": "d4a4a854-4ac7-472e-9b7b-fea90ccf35b7",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{tabularx}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{tabularx}\n\\usepackage{natbib}\n\\usepackage[colorlinks,citecolor=blue,urlcolor=blue]{hyperref}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " \\documentclass[11pt,a4paper]{article}",
          "-\\usepackage[hyperref]{acl}",
          "+\\usepackage[margin=1in]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{graphicx}"
        ]
      },
      {
        "oldStart": 13,
        "oldLines": 6,
        "newStart": 13,
        "newLines": 8,
        "lines": [
          " \\usepackage[utf8]{inputenc}",
          " \\usepackage{microtype}",
          " \\usepackage{tabularx}",
          "+\\usepackage{natbib}",
          "+\\usepackage[colorlinks,citecolor=blue,urlcolor=blue]{hyperref}",
          " ",
          " \\title{Cross-Lingual Calibration via Internal Correctness Directions:\\\\Pareto Frontiers, Decomposition, and Consistency-Aligned Probes}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "5aafef72-99a1-453a-9690-65fb53240a66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-20T20:46:00.550Z_

```json
{
  "parentUuid": "d4a4a854-4ac7-472e-9b7b-fea90ccf35b7",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "edfe9394-163b-4e05-8fdc-f3e224ba79e8",
  "timestamp": "2026-05-20T20:46:00.550Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 33 · 2026-05-20T20:46:03.951Z_

<details open><summary>🔧 Tool call — Edit · `toolu_011T9rJPSC7tt7suaGzLnuqa`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/paper.tex",
  "old_string": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
  "new_string": "\\bibliographystyle{plainnat}\n\\bibliography{references}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edfe9394-163b-4e05-8fdc-f3e224ba79e8",
  "isSidechain": false,
  "requestId": "req_011CbEUWMWn5toPZexuKK7eZ",
  "type": "assistant",
  "uuid": "6712cca3-ebad-4432-b2ad-eb877fad47ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tH7mpEpvvGfBDq491YzLj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 721,
      "cache_read_input_tokens": 58058,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 721,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 58058,
          "cache_creation_input_tokens": 721,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 721
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

_source line 34 · 2026-05-20T20:46:03.965Z_

<details><summary>↩ Tool result · `toolu_011T9rJPSC7tt7suaGzLnuqa`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6712cca3-ebad-4432-b2ad-eb877fad47ec",
  "isSidechain": false,
  "promptId": "d6812199-51cb-4f3b-a1d1-28a2f25b4592",
  "type": "user",
  "uuid": "ce18388d-2f6e-4ba0-9067-c92ad3db3945",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/paper.tex",
    "oldString": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
    "newString": "\\bibliographystyle{plainnat}\n\\bibliography{references}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 617,
        "oldLines": 7,
        "newStart": 617,
        "newLines": 7,
        "lines": [
          " CaCLR generalizes across the full language set, with low-resource languages benefiting most (+7.3~pp vs.\\ +4.2~pp for high-resource).",
          " 38/52 languages (73\\%) achieve zero-shot AUROC above 0.65; the Pareto frontier and CaCLR improvements remain robust.",
          " ",
          "+\\bibliographystyle{plainnat}",
          " \\bibliography{references}",
          "-\\bibliographystyle{acl_natbib}",
          " ",
          " \\end{document}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "6712cca3-ebad-4432-b2ad-eb877fad47ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T20:46:07.132Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HAZkgn5TjWp77DKXXoQcFC`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce18388d-2f6e-4ba0-9067-c92ad3db3945",
  "isSidechain": false,
  "requestId": "req_011CbEUWcL1XztdtwbGtxa8E",
  "type": "assistant",
  "uuid": "f3166217-ede6-46a5-be9a-27095c2f1220",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013dupNKXY9Eymmx7evEXBri",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 257,
      "cache_read_input_tokens": 58779,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 58779,
          "cache_creation_input_tokens": 257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 257
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

_source line 36 · 2026-05-20T20:46:07.806Z_

<details><summary>↩ Tool result · `toolu_01HAZkgn5TjWp77DKXXoQcFC`</summary>

```text
Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/urw/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 175415 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3166217-ede6-46a5-be9a-27095c2f1220",
  "isSidechain": false,
  "promptId": "d6812199-51cb-4f3b-a1d1-28a2f25b4592",
  "type": "user",
  "uuid": "e4aaf9e8-53d1-425b-bc20-5de62c89b5dc",
  "toolUseResult": {
    "stdout": "Package rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 175415 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f3166217-ede6-46a5-be9a-27095c2f1220",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T20:46:10.795Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019FsAsaySpwwfYra2iNyvF4`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Second pdflatex pass for references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4aaf9e8-53d1-425b-bc20-5de62c89b5dc",
  "isSidechain": false,
  "requestId": "req_011CbEUWtYaQwHFMSdXuBPSE",
  "type": "assistant",
  "uuid": "dbba83ce-ea90-4ee1-b220-6e4cd97b704e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01272XSASjtuNBaCbtcQRcmr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 666,
      "cache_read_input_tokens": 59036,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 666,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 59036,
          "cache_creation_input_tokens": 666,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 666
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

_source line 38 · 2026-05-20T20:46:11.438Z_

<details><summary>↩ Tool result · `toolu_019FsAsaySpwwfYra2iNyvF4`</summary>

```text
e/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/urw/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 177980 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dbba83ce-ea90-4ee1-b220-6e4cd97b704e",
  "isSidechain": false,
  "promptId": "d6812199-51cb-4f3b-a1d1-28a2f25b4592",
  "type": "user",
  "uuid": "a214783d-e6fd-49d1-aa99-a8b9d44c3844",
  "toolUseResult": {
    "stdout": "e/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 177980 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "dbba83ce-ea90-4ee1-b220-6e4cd97b704e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-20T20:46:14.011Z_

PDF compiled successfully — 10 pages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a214783d-e6fd-49d1-aa99-a8b9d44c3844",
  "isSidechain": false,
  "requestId": "req_011CbEUXAsqhKXzK9Yt6biiq",
  "type": "assistant",
  "uuid": "92114dfa-6f94-4f91-9548-9eea8794042a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qhit9SVurFaRurBh2khiJH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 236,
      "cache_read_input_tokens": 59702,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 135,
          "cache_read_input_tokens": 59702,
          "cache_creation_input_tokens": 236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 236
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

_source line 40 · 2026-05-20T20:46:14.812Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Vish1k81NFXGvGPSsQyjxm`</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/paper.pdf",
  "description": "Verify PDF output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92114dfa-6f94-4f91-9548-9eea8794042a",
  "isSidechain": false,
  "requestId": "req_011CbEUXAsqhKXzK9Yt6biiq",
  "type": "assistant",
  "uuid": "e35d250e-35b3-4aa3-b420-bcd59b8ae4f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qhit9SVurFaRurBh2khiJH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 236,
      "cache_read_input_tokens": 59702,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 135,
          "cache_read_input_tokens": 59702,
          "cache_creation_input_tokens": 236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 236
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

_source line 41 · 2026-05-20T20:46:14.862Z_

<details><summary>↩ Tool result · `toolu_01Vish1k81NFXGvGPSsQyjxm`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 174K May 20 20:46 /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e35d250e-35b3-4aa3-b420-bcd59b8ae4f9",
  "isSidechain": false,
  "promptId": "d6812199-51cb-4f3b-a1d1-28a2f25b4592",
  "type": "user",
  "uuid": "29e2cc5f-1d1e-4a4b-bb2d-d8d4086a4166",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 174K May 20 20:46 /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/paper.pdf",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "e35d250e-35b3-4aa3-b420-bcd59b8ae4f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-20T20:46:23.363Z_

论文已生成：10页PDF，包含所有11个实验对应的表格和分析。

结构：Abstract → Introduction (4 claims) → Related Work (7段) → Method (correctness probes, transfer, CaCLR, decomposition) → Experiments (Pareto frontier, CaCLR, decomposition, orthogonality, CKA, probe complexity, cross-benchmark, linear projection) → Discussion → Conclusion → Appendix (INT8 validation, control tasks, Gemma 4 dense, 52-language extension)。

所有定量数据均来自 `experiment_data.json`，无编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29e2cc5f-1d1e-4a4b-bb2d-d8d4086a4166",
  "isSidechain": false,
  "requestId": "req_011CbEUXR5cWRmKbK3oxz6bJ",
  "type": "assistant",
  "uuid": "4c59cc91-0d1b-40bb-80a5-282f5616667a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RTjv4AJJYPhVfNz5M85vbg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 221,
      "cache_read_input_tokens": 59938,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 221,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 59938,
          "cache_creation_input_tokens": 221,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 221
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

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T201854 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direct…",
  "leafUuid": "4c59cc91-0d1b-40bb-80a5-282f5616667a",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate calibration research paper with CaCLR method",
  "sessionId": "d5955a05-4002-488d-8660-8d47efae1571"
}
```

---
