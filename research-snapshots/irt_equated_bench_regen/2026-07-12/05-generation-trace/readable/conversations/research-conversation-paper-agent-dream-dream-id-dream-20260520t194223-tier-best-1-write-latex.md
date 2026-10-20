# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T194223 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/4cdb7bff-0186-4287-af6d-80c2435b1cc6.jsonl`
- **Structured JSON:** [`c0d2ad28ad9af67dcb61.json`](../../sessions/c0/c0d2ad28ad9af67dcb61.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T19:58:52.227Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T19:58:52.227Z",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T194223 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：\"Self-healing benchmark\" story完整成立。DIF是唯一经RL训练不退化的contamination信号， 理论论证（group-level ICC vs within-model distribution）获得经验支持。 Ensemble覆盖全effect-size谱，bifactor equating实现psychometrically等价的benchmark再生。 Headline: \"DIF maintains 70-85% TPR where 10 existing methods degrade to random under RL.\" 三条claims均以full strength呈现，ICLR投稿无需调整framing。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T19:58:52.230Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T19:58:52.230Z",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6"
}
```

---

## Round 1

26 recorded events

### User

_source line 3 · 2026-05-20T19:58:52.248Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T194223 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance："Self-healing benchmark" story完整成立。DIF是唯一经RL训练不退化的contamination信号， 理论论证（group-level ICC vs within-model distribution）获得经验支持。 Ensemble覆盖全effect-size谱，bifactor equating实现psychometrically等价的benchmark再生。 Headline: "DIF maintains 70-85% TPR where 10 existing methods degrade to random under RL." 三条claims均以full strength呈现，ICLR投稿无需调整framing。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ed003479-76af-4943-a861-980660b8c55c",
  "type": "user",
  "uuid": "4939862f-7265-4ab9-be23-5ca00d324944",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T19:58:52.247Z_

```json
{
  "parentUuid": "4939862f-7265-4ab9-be23-5ca00d324944",
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
  "uuid": "189399ab-0f7c-421a-89ac-fa0a3792fc42",
  "timestamp": "2026-05-20T19:58:52.247Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T19:58:52.247Z_

```json
{
  "parentUuid": "189399ab-0f7c-421a-89ac-fa0a3792fc42",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7742bd6e-e03f-41f9-8de7-c7fc37c3d273",
  "timestamp": "2026-05-20T19:58:52.247Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6",
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
  "aiTitle": "Generate complete mock research paper",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6"
}
```

---

### Assistant

_source line 7 · 2026-05-20T19:58:55.149Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7742bd6e-e03f-41f9-8de7-c7fc37c3d273",
  "isSidechain": false,
  "requestId": "req_011CbEQuscCTW4krS2BK8u1c",
  "type": "assistant",
  "uuid": "e2e6864f-d4ed-4f11-8f61-028434e0467a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZLizir4dmJQBJFazpmuqf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11331,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11331,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11331
          },
          "type": "message"
        }
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

_source line 8 · 2026-05-20T19:58:55.634Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XetTVMKRLR5LaEZUWhzmge`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2e6864f-d4ed-4f11-8f61-028434e0467a",
  "isSidechain": false,
  "requestId": "req_011CbEQuscCTW4krS2BK8u1c",
  "type": "assistant",
  "uuid": "3fcfb509-c026-4304-9b0e-27331ebf4752",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZLizir4dmJQBJFazpmuqf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11331,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11331,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11331
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-20T19:58:56.141Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PbbSvJeuUb7crekM14hpk8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fcfb509-c026-4304-9b0e-27331ebf4752",
  "isSidechain": false,
  "requestId": "req_011CbEQuscCTW4krS2BK8u1c",
  "type": "assistant",
  "uuid": "1ead1b3e-64ad-4846-aa79-f94dc2221773",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZLizir4dmJQBJFazpmuqf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11331,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11331,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11331
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-20T19:58:56.148Z_

<details><summary>↩ Tool result · `toolu_01XetTVMKRLR5LaEZUWhzmge`</summary>

```text
1	[
2	  {
3	    "name": "real_data_dif_mmlu",
4	    "description": "对METABENCH MMLU真实响应矩阵（5,055 models × 12,508 items）执行DIF分析。 按release date切temporal cohorts（pre-2024 vs post-2024 + 年度细分）， 运行ETS C检测，用MMLU-CF作为partial ground truth外部验证。\n",
5	    "results": {
6	      "n_models_total": 5055,
7	      "n_models_post_2024": 1820,
8	      "cohort_pre2024_size": 3235,
9	      "cohort_post2024_size": 1820,
10	      "annual_cohort_min_size": 92,
11	      "annual_cohort_max_size": 2100,
12	      "ets_c_items_flagged_C_level": 1340,
13	      "ets_c_items_flagged_B_or_C": 2870,
14	      "ets_c_tpr_delta_ge_1_4": 0.78,
15	      "ets_c_tpr_delta_ge_1_6": 0.83,
16	      "ets_c_fpr": 0.038,
17	      "ets_c_auc_delta_ge_1_4": 0.92,
18	      "mmlu_cf_correlation_with_dif_flags_phi": 0.42,
19	      "mmlu_cf_correlation_with_dif_flags_tetrachoric": 0.48,
20	      "n_mmlu_cf_overlapping_items": 2780,
21	      "dif_flagged_among_cf_modified": 0.61,
22	      "dif_flagged_among_cf_unmodified": 0.07,
23	      "sensitivity_cohort_split_tpr_range": [
24	        0.72,
25	        0.83
26	      ],
27	      "sensitivity_threshold_tpr_range": [
28	        0.68,
29	        0.85
30	      ],
31	      "real_irt_param_a_mean": 1.18,
32	      "real_irt_param_b_mean": -0.79,
33	      "real_irt_param_a_std": 0.42
34	    },
35	    "tables": [
36	      {
37	        "title": "Table 1: DIF Detection Power on METABENCH MMLU Real Data",
38	        "columns": [
39	          "cohort_split",
40	          "N_focal",
41	          "N_ref",
42	          "delta_range",
43	          "TPR",
44	          "FPR",
45	          "AUC"
46	        ],
47	        "rows": [
48	          [
49	            "pre2024_vs_post2024",
50	            1820,
51	            3235,
52	            "≥1.4",
53	            0.78,
54	            0.038,
55	            0.92
56	          ],
57	          [
58	            "pre2024_vs_post2024",
59	            1820,
60	            3235,
61	            "≥1.6",
62	            0.83,
63	            0.038,
64	            0.94
65	          ],
66	          [
67	            "pre2024_vs_post2024",
68	            1820,
69	            3235,
70	            "≥1.0",
71	            0.51,
72	            0.041,
73	            0.83
74	          ],
75	          [
76	            "2022_vs_2024",
77	            920,
78	            2100,
79	            "≥1.4",
80	            0.76,
81	            0.036,
82	            0.91
83	          ],
84	          [
85	            "2023_vs_2025",
86	            680,
87	            1340,
88	            "≥1.4",
89	            0.74,
90	            0.039,
91	            0.9
92	          ],
93	          [
94	            "annual_finest",
95	            92,
96	            2100,
97	            "≥1.4",
98	            0.72,
99	            0.042,
100	            0.88
101	          ]
102	        ]
103	      },
104	      {
105	        "title": "Table 2: MMLU-CF External Validation",
106	        "columns": [
107	          "category",
108	          "n_items",
109	          "dif_flagged_rate",
110	          "description"
111	        ],
112	        "rows": [
113	          [
114	            "CF_modified_items",
115	            2780,
116	            0.61,
117	            "Items significantly changed in MMLU-CF"
118	          ],
119	          [
120	            "CF_unmodified_items",
121	            9728,
122	            0.07,
123	            "Items unchanged in MMLU-CF"
124	          ],
125	          [
126	            "phi_coefficient",
127	            null,
128	            0.42,
129	            "Association between DIF flag and CF modification"
130	          ],
131	          [
132	            "tetrachoric_r",
133	            null,
134	            0.48,
135	            "Latent correlation estimate"
136	          ]
137	        ]
138	      }
139	    ],
140	    "figures": [],
141	    "analysis": "真实数据DIF检测power与Phase 2模拟高度一致，验证了模拟参数设定的生态效度。 关键发现：(1) MMLU上约10.7%的items呈现ETS C级DIF，集中在STEM领域，与contamination through pretraining code data的预期一致；(2) MMLU-CF外部验证提供convergent evidence， phi=0.42虽非完美但在partial ground truth条件下合理——完美相关本身不可信，因为CF的 modification策略与contamination并非一一对应；(3) 敏感性分析显示TPR在不同cohort 定义下稳定在0.72-0.83区间，最弱的annual finest split（N_focal=92）仍达0.72， 正好符合Phase 2模拟在N=80条件下的预测。这一结果直接支持Claim 1的real-data validation。\n\n\nPhase 2模拟已在N=100/δ=1.6条件下达到TPR=0.7966，真实参数（a_mean=1.2, b_mean=-0.84） 与模拟设定高度一致。Best档下真实数据复现模拟power的核心条件是：(1) METABENCH post-2024 cohort达到N≈1820，远超模拟的N=100下限，提供充足统计功效；(2) 真实contamination effect sizes在高频benchmark如MMLU上确实存在δ≥1.4的大效应——GSM1K研究已证实10-13pp 的accuracy gap，对应IRT尺度上δ≈1.5-2.0；(3) ETS C基于effect-size阈值而非p-value， 大样本下不会出现inflation问题，反而因estimation precision提高而TPR略优于模拟。 MMLU-CF验证的phi=0.42反映了partial ground truth的本质局限——CF修改的items与真正 contaminated items有交集但不完全重叠，CF修改了部分未被contaminate的items（降低相关）， 同时未修改一些实际被contaminate的items。但0.42的phi系数在psychometric validation中 已属中等偏强，足以作为convergent validity evidence。FPR=0.038与模拟的0.036-0.042 区间一致，因为false positive rate主要由ETS C的Δ_MH阈值决定，不依赖sample size。\n"
142	  },
143	  {
144	    "name": "rl_robustness_validation",
145	    "description": "经验验证DIF的RL-robustness。构建SFT-only cohort和含RL-trained模型的cohort， 同时运行DIF与传统检测器（Min-K%、ConStat perturbation、DVD），对比RL条件下的退化。\n",
146	    "results": {
147	      "n_rl_models_evaluated": 14,
148	      "n_sft_models_evaluated": 40,
149	      "rl_models_list": "DeepSeek-R1, DeepSeek-R1-Distill-{7B,14B,32B,70B}, Qwen2.5-RL-{7B,72B}, Llama-3.1-Nemotron-Ultra-253B, QwQ-32B, Skywork-OR1-{8B,32B}, K1.5-Chat, Eurus-2-7B-PRIME, OpenThinker-7B\n",
150	      "dif_tpr_sft_cohort_delta_ge_1_4": 0.79,
151	      "dif_tpr_rl_cohort_delta_ge_1_4": 0.76,
152	      "dif_power_retention_ratio": 0.96,
153	      "dif_fpr_sft_cohort": 0.037,
154	      "dif_fpr_rl_cohort": 0.041,
155	      "mink_auroc_sft": 0.72,
156	      "mink_auroc_rl": 0.51,
157	      "mink_degradation_pp": 21,
158	      "constat_auroc_sft": 0.68,
159	      "constat_auroc_rl": 0.53,
160	      "constat_degradation_pp": 15,
161	      "dvd_auroc_sft": 0.65,
162	      "dvd_auroc_rl": 0.54,
163	      "dvd_degradation_pp": 11,
164	      "perplexity_auroc_sft": 0.61,
165	      "perplexity_auroc_rl": 0.5,
166	      "lowercase_auroc_sft": 0.58,
167	      "lowercase_auroc_rl": 0.49,
168	      "traditional_mean_auroc_sft": 0.65,
169	      "traditional_mean_auroc_rl": 0.51,
170	      "p_value_dif_retention_paired_t": 0.62,
171	      "p_value_traditional_degradation_paired_t": 0.0003
172	    },
173	    "tables": [
174	      {
175	        "title": "Table 3: DIF vs Traditional Detectors Under RL Training",
176	        "columns": [
177	          "method",
178	          "auroc_sft_cohort",
179	          "auroc_rl_cohort",
180	          "degradation_pp",
181	          "p_value"
182	        ],
183	        "rows": [
184	          [
185	            "DIF_ETS_C",
186	            0.91,
187	            0.9,
188	            1,
189	            0.62
190	          ],
191	          [
192	            "Min-K%",
193	            0.72,
194	            0.51,
195	            21,
196	            0.0002
197	          ],
198	          [
199	            "ConStat_perturbation",
200	            0.68,
201	            0.53,
202	            15,
203	            0.001
204	          ],
205	          [
206	            "DVD_generation_var",
207	            0.65,
208	            0.54,
209	            11,
210	            0.004
211	          ],
212	          [
213	            "Perplexity",
214	            0.61,
215	            0.5,
216	            11,
217	            0.003
218	          ],
219	          [
220	            "Lowercase",
221	            0.58,
222	            0.49,
223	            9,
224	            0.008
225	          ],
226	          [
227	            "zlib_ratio",
228	            0.6,
229	            0.5,
230	            10,
231	            0.005
232	          ],
233	          [
234	            "Top-K_prob",
235	            0.63,
236	            0.52,
237	            11,
238	            0.003
239	          ],
240	          [
241	            "Ref_model_loss",
242	            0.67,
243	            0.53,
244	            14,
245	            0.002
246	          ],
247	          [
248	            "Neighbor_text",
249	            0.59,
250	            0.5,
251	            9,
252	            0.007
253	          ],
254	          [
255	            "DetectGPT",
256	            0.55,
257	            0.49,
258	            6,
259	            0.04
260	          ]
261	        ]
262	      },
263	      {
264	        "title": "Table 4: DIF Power Retention by RL Training Intensity",
265	        "columns": [
266	          "model_group",
267	          "n_models",
268	          "dif_tpr_delta_ge_1_4",
269	          "dif_fpr",
270	          "retention_vs_sft"
271	        ],
272	        "rows": [
273	          [
274	            "SFT_only",
275	            40,
276	            0.79,
277	            0.037,
278	            1.0
279	          ],
280	          [
281	            "Light_RL_under_500_steps",
282	            6,
283	            0.78,
284	            0.039,
285	            0.99
286	          ],
287	          [
288	            "Heavy_RL_over_500_steps",
289	            8,
290	            0.75,
291	            0.041,
292	            0.95
293	          ],
294	          [
295	            "All_RL",
296	            14,
297	            0.76,
298	            0.041,
299	            0.96
300	          ]
301	        ]
302	      }
303	    ],
304	    "figures": [],
305	    "analysis": "RL-robustness经验验证是论文最核心的卖点。DIF power retention ratio=0.96意味着 RL训练对DIF检测力几乎无影响（paired t-test p=0.62，无统计显著差异），而10种传统 检测器平均退化14pp至near-random（mean AUROC=0.51）。这直接验证了理论预测： DIF操作在group-level behavioral space，RL无法在不放弃contamination benefit的 情况下消除这一信号。Heavy RL（>500 steps）组的轻微衰减（retention=0.95）可归因于 更高general ability导致的effect size estimation compression，而非mechanism failure。 这一结果使headline claim成立：\"DIF maintains 76% TPR where 10 existing methods degrade to random under RL training.\"\n\n\nDIF的RL-robustness源于其检测机制的根本差异。传统检测器（Min-K%、perplexity-based） 依赖within-model output distributions——GRPO/PPO通过policy smoothing将memorized items 的output distribution调整到与clean items相似，消除可检测的distributional anomaly。 Wang et al. (ICLR 2026)已实证证明这种退化：~156 GRPO steps即可将多数检测器降至 near-random。DIF则完全不同：它比较的是group-level Item Characteristic Curves—— \"给定相同latent ability θ，focal group（post-training cohort）在item j上的correct probability是否高于reference group\"。RL训练可以smooth output token distributions， 但无法消除behavioral fact：\"这个模型答对了这道它memorized的题\"。除非RL训练能让模型 在memorized items上故意答错（这会negate contamination的目的），否则group-level behavioral pattern必然保留。Power retention ratio=0.96（而非1.0）的微小衰减来自 RL模型通常具有更高的general ability θ，这略微压缩了DIF effect size的估计——但这是 统计层面的minor attenuation，不是mechanistic failure。传统检测器的AUROC从0.65降至 0.51（mean across methods），与Wang et al.报告的14-20pp退化一致。\n"
306	  },
307	  {
308	    "name": "constat_perturbation_eval",
309	    "description": "独立评估ConStat-style perturbation testing在MMLU上的检测力， 生成200+ items的语义等价改写，比较原始vs改写表现，刻画effect size谱上的检测力。\n",
310	    "results": {
311	      "n_items_reformulated": 240,
312	      "n_models_tested": 35,
313	      "n_reformulations_per_item": 5,
314	      "constat_tpr_non_rl_delta_ge_0_6": 0.68,
315	      "constat_tpr_non_rl_delta_ge_1_0": 0.74,
316	      "constat_tpr_non_rl_delta_ge_1_4": 0.62,
317	      "constat_tpr_rl_delta_ge_0_6": 0.31,
318	      "constat_tpr_rl_delta_ge_1_0": 0.38,
319	      "constat_fpr_non_rl": 0.06,
320	      "constat_fpr_rl": 0.08,
321	      "constat_fdr_controlled_alpha_0_05": 0.048,
322	      "mean_accuracy_drop_contaminated_items": 0.18,
323	      "mean_accuracy_drop_clean_items": 0.03,
324	      "reformulation_semantic_similarity": 0.91
325	    },
326	    "tables": [
327	      {
328	        "title": "Table 5: ConStat Detection Power by Effect Size and Model Type",
329	        "columns": [
330	          "model_type",
331	          "delta_range",
332	          "n_items",
333	          "TPR",
334	          "FPR",
335	          "FDR"
336	        ],
337	        "rows": [
338	          [
339	            "non_RL",
340	            "≥0.6",
341	            142,
342	            0.68,
343	            0.06,
344	            0.048
345	          ],
346	          [
347	            "non_RL",
348	            "≥1.0",
349	            87,
350	            0.74,
351	            0.06,
352	            0.041
353	          ],
354	          [
355	            "non_RL",
356	            "≥1.4",
357	            48,
358	            0.62,
359	            0.06,
360	            0.052
361	          ],
362	          [
363	            "RL",
364	            "≥0.6",
365	            142,
366	            0.31,
367	            0.08,
368	            0.12
369	          ],
370	          [
371	            "RL",
372	            "≥1.0",
373	            87,
374	            0.38,
375	            0.08,
376	            0.1
377	          ],
378	          [
379	            "all_models",
380	            "≥0.6",
381	            142,
382	            0.52,
383	            0.07,
384	            0.07
385	          ]
386	        ]
387	      }
388	    ],
389	    "figures": [],
390	    "analysis": "ConStat在non-RL模型上的medium-effect-size检测力（δ≥0.6: TPR=0.68）验证了其在 ensemble中的角色——填补DIF在small-to-medium effects上的盲区。RL条件下的急剧退化 （TPR从0.68→0.31）与Wang et al.的发现一致，因为perturbation sensitivity本质上仍 依赖于surface-form specific memorization pattern，RL训练将其平滑化。FDR控制在 non-RL条件下有效（0.048 < 0.05），但RL条件下FDR升至0.12，需在ensemble中对RL模型 降低ConStat权重。\n\n\nConStat的检测逻辑是：contaminated models在original items上表现异常好，但在 semantically equivalent reformulations上表现回落——因为memorization是surface-form specific的。在non-RL models上，这一逻辑有效：SFT训练的memorization直接绑定到 token sequences，reformulation打破了这种绑定，导致contaminated items上出现显著 accuracy drop（mean=0.18 vs clean items的0.03）。TPR在δ≥0.6时达0.68，因为即使 中等效应的contamination也会在perturbation下暴露。但在δ≥1.4时TPR反而降到0.62， 因为极大effect size的items通常是extremely easy items（即使不contaminate也正确率高）， reformulation后的drop较小。ConStat在RL模型上急剧退化（TPR从0.68降至0.31），因为 GRPO/PPO的policy optimization使模型学会了更general的answer patterns而非 surface-form memorization——RL模型在reformulated items上的accuracy drop较小， 使perturbation signal模糊化。这正是ConStat在ensemble中的定位：覆盖non-RL models的 medium effect sizes（DIF在δ<1.0时power不足），但在RL场景下需要DIF补位。\n"
391	  },
392	  {
393	    "name": "dvd_generation_variance_eval",
394	    "description": "独立评估DVD generation variance在MMLU上的检测力，对10-15个open-weight模型 每item生成50次response，计算generation variance分数，检测bimodal distributions。\n",
395	    "results": {
396	      "n_models_evaluated": 12,
397	      "n_items_evaluated": 2000,
398	      "responses_per_item": 50,
399	      "temperature_range": [
400	        0.7,
401	        1.0
402	      ],
403	      "dvd_tpr_variant_contamination": 0.65,
404	      "dvd_tpr_verbatim_contamination": 0.38,
405	      "dvd_tpr_all_contamination": 0.52,
406	      "dvd_fpr": 0.07,
407	      "dvd_auroc_variant": 0.78,
408	      "dvd_auroc_verbatim": 0.62,
409	      "dvd_auroc_overall": 0.71,
410	      "bimodal_detection_rate_contaminated": 0.58,
411	      "bimodal_detection_rate_clean": 0.04,
412	      "dvd_tpr_rl_variant": 0.47,
413	      "dvd_tpr_rl_verbatim": 0.29,
414	      "generation_variance_contaminated_mean": 0.31,
415	      "generation_variance_clean_mean": 0.12
416	    },
417	    "tables": [
418	      {
419	        "title": "Table 6: DVD Detection Power by Contamination Type",
420	        "columns": [
421	          "contamination_type",
422	          "model_type",
423	          "n_items",
424	          "TPR",
425	          "FPR",
426	          "AUROC"
427	        ],
428	        "rows": [
429	          [
430	            "variant",
431	            "non_RL",
432	            320,
433	            0.65,
434	            0.07,
435	            0.78
436	          ],
437	          [
438	            "verbatim",
439	            "non_RL",
440	            480,
441	            0.38,
442	            0.07,
443	            0.62
444	          ],
445	          [
446	            "all",
447	            "non_RL",
448	            800,
449	            0.52,
450	            0.07,
451	            0.71
452	          ],
453	          [
454	            "variant",
455	            "RL",
456	            320,
457	            0.47,
458	            0.09,
459	            0.68
460	          ],
461	          [
462	            "verbatim",
463	            "RL",
464	            480,
465	            0.29,
466	            0.09,
467	            0.57
468	          ],
469	          [
470	            "all",
471	            "RL",
472	            800,
473	            0.38,
474	            0.09,
475	            0.63
476	          ]
477	        ]
478	      }
479	    ],
480	    "figures": [],
481	    "analysis": "DVD填补了ensemble中的variant contamination盲区。DIF主要检测verbatim large effects （模型在original item上的behavioral anomaly），ConStat检测non-RL medium effects， DVD则捕获variant contamination——模型见过类似但不完全相同的items，产生partial memorization的generation variance signal。三者的complementary coverage pattern 在best档下清晰呈现，为ensemble fusion提供了solid foundation。\n\n\nDVD的检测逻辑基于generation variance：contaminated models在memorized items上的 generation distribution呈现bimodal pattern——当temperature sampling触发\"recall\" mode时high confidence输出memorized answer，否则回到general reasoning mode。 Variant contamination（模型见过item的变体而非原始形式）下DVD最有效（TPR=0.65）， 因为variant exposure创造了partial memorization——模型\"几乎记得\"答案，导致生成 在confident recall和uncertain reasoning之间振荡，产生高variance和清晰的bimodality。 Verbatim contamination下DVD效果较差（TPR=0.38），因为完全memorized items的生成 variance反而很低（模型每次都确信地输出相同答案），bimodal signal消失。这使DVD与DIF 形成互补：DIF在verbatim large effects上最强，DVD在variant contamination上最强。 RL条件下DVD退化到TPR=0.47（variant），因为GRPO smoothing降低了generation variance 的discriminability，但退化幅度小于ConStat（因为DVD利用的是sampling-level variance 而非perturbation sensitivity，RL对sampling variance的影响弱于对perturbation response的影响）。\n"
482	  },
483	  {
484	    "name": "ensemble_fusion",
485	    "description": "融合DIF + ConStat + DVD为multi-signal ensemble。校准per-signal阈值， 评估majority voting和weighted fusion，展示ensemble coverage覆盖全effect-size谱。\n",
486	    "results": {
487	      "ensemble_tpr_full_spectrum": 0.87,
488	      "ensemble_tpr_delta_ge_1_4": 0.91,
489	      "ensemble_tpr_delta_ge_1_0": 0.85,
490	      "ensemble_tpr_delta_ge_0_6": 0.78,
491	      "ensemble_fpr": 0.08,
492	      "ensemble_auroc": 0.93,
493	      "majority_2of3_tpr": 0.72,
494	      "majority_2of3_fpr": 0.04,
495	      "weighted_fusion_tpr": 0.87,
496	      "weighted_fusion_fpr": 0.08,
497	      "dif_unique_detections_pct": 0.28,
498	      "constat_unique_detections_pct": 0.15,
499	      "dvd_unique_detections_pct": 0.12,
500	      "all_three_overlap_pct": 0.31,
501	      "two_signal_overlap_pct": 0.14,
502	      "ensemble_tpr_rl_models": 0.82,
503	      "ensemble_tpr_non_rl_models": 0.9,
504	      "optimal_weights_dif": 0.45,
505	      "optimal_weights_constat": 0.3,
506	      "optimal_weights_dvd": 0.25
507	    },
508	    "tables": [
509	      {
510	        "title": "Table 7: Ensemble vs Individual Signal Detection Power",
511	        "columns": [
512	          "method",
513	          "tpr_full",
514	          "tpr_ge_1_4",
515	          "tpr_ge_0_6",
516	          "fpr",
517	          "auroc"
518	        ],
519	        "rows": [
520	          [
521	            "DIF_only",
522	            0.58,
523	            0.78,
524	            0.35,
525	            0.038,
526	            0.84
527	          ],
528	          [
529	            "ConStat_only",
530	            0.44,
531	            0.62,
532	            0.68,
533	            0.06,
534	            0.76
535	          ],
536	          [
537	            "DVD_only",
538	            0.38,
539	            0.38,
540	            0.45,
541	            0.07,
542	            0.71
543	          ],
544	          [
545	            "Majority_2of3",
546	            0.72,
547	            0.81,
548	            0.64,
549	            0.04,
550	            0.89
551	          ],
552	          [
553	            "Weighted_fusion",
554	            0.87,
555	            0.91,
556	            0.78,
557	            0.08,
558	            0.93
559	          ]
560	        ]
561	      },
562	      {
563	        "title": "Table 8: Signal Complementarity Analysis",
564	        "columns": [
565	          "detection_source",
566	          "pct_of_total_detections",
567	          "example_regime"
568	        ],
569	        "rows": [
570	          [
571	            "DIF_unique",
572	            0.28,
573	            "Large effect + RL models"
574	          ],
575	          [
576	            "ConStat_unique",
577	            0.15,
578	            "Medium effect + non-RL models"
579	          ],
580	          [
581	            "DVD_unique",
582	            0.12,
583	            "Variant contamination"
584	          ],
585	          [
586	            "DIF_and_ConStat",
587	            0.08,
588	            "Large effect + non-RL"
589	          ],
590	          [
591	            "DIF_and_DVD",
592	            0.04,
593	            "Large variant + RL"
594	          ],
595	          [
596	            "ConStat_and_DVD",
597	            0.02,
598	            "Medium variant + non-RL"
599	          ],
600	          [
601	            "All_three",
602	            0.31,
603	            "Large effect + non-RL + verbatim"
604	          ]
605	        ]
606	      }
607	    ],
608	    "figures": [],
609	    "analysis": "Ensemble coverage分析是Claim 2的核心evidence。三信号互补的清晰pattern—— DIF覆盖RL+large effects，ConStat覆盖non-RL+medium effects，DVD覆盖variant contamination——使full-spectrum TPR从任何单信号的最高0.58提升到0.87。 关键是unique detections分析：每个信号贡献12-28%的独占检测，证明任何单信号都不可替代。 Weighted fusion优于majority voting 15pp，反映了信号互补性超过信号冗余性—— 在most detection regimes下只有1-2个信号active，majority voting的\"2-of-3 agreement\" 要求过于保守。\n\n\nEnsemble的power来源于三信号的systematic complementarity。在best档下，每个信号 覆盖不同的effect-size × model-type区间：DIF覆盖large effects（δ≥1.4）且RL-robust， ConStat覆盖non-RL medium effects（δ≥0.6），DVD覆盖variant contamination。 Weighted fusion（DIF=0.45, ConStat=0.30, DVD=0.25）优于majority voting （TPR 0.87 vs 0.72），因为majority voting要求至少2/3信号agree，而在信号覆盖不 重叠的区间（如RL+large effect只有DIF有效），single-signal detection被majority voting过滤掉。Weighted fusion允许high-confidence single signal触发detection。 Full-spectrum TPR=0.87的构成：δ≥1.4区间DIF主导（TPR=0.91），δ=0.6-1.4区间ConStat 补位（将DIF单独的~0.40 TPR提升到ensemble的0.78），variant contamination区间DVD 补位（unique detections 12%）。FPR=0.08略高于single-signal的0.04-0.07，这是 multi-signal fusion的inherent trade-off——更多信号意味着更多false positive opportunities，但0.08仍在可接受范围内。RL模型上ensemble TPR=0.82（vs non-RL的0.90）， 差距来自ConStat在RL条件下的退化被DIF的RL-robustness部分补偿。\n"
610	  },
611	  {
612	    "name": "cross_benchmark_gsm8k",
613	    "description": "在GSM8K上复制DIF分析，用GSM1K作为contamination ground truth。 收集50+模型的per-item binary responses，运行temporal cohort DIF， 将DIF flags与per-model GSM8K-GSM1K accuracy gap关联。\n",
614	    "results": {
615	      "n_models_gsm8k": 62,
616	      "n_items_gsm8k": 1319,
617	      "n_items_gsm1k": 1250,
618	      "cohort_pre2024_n": 28,
619	      "cohort_post2024_n": 34,
620	      "dif_flagged_items_gsm8k": 178,
621	      "dif_flagged_rate": 0.135,
622	      "dif_tpr_gsm8k_delta_ge_1_4": 0.74,
623	      "dif_fpr_gsm8k": 0.042,
624	      "gsm8k_gsm1k_gap_mean_all_models": 0.068,
625	      "gsm8k_gsm1k_gap_mean_contaminated_models": 0.112,
626	      "gsm8k_gsm1k_gap_mean_clean_models": 0.024,
627	      "gsm8k_gsm1k_gap_dif_correlation_spearman": 0.43,
628	      "gsm8k_gsm1k_gap_dif_correlation_pearson": 0.38,
629	      "per_item_dif_vs_gap_correlation": 0.41,
630	      "gsm8k_dif_auc": 0.88
631	    },
632	    "tables": [
633	      {
634	        "title": "Table 9: DIF Detection on GSM8K with GSM1K Ground Truth",
635	        "columns": [
636	          "metric",
637	          "value"
638	        ],
639	        "rows": [
640	          [
641	            "n_models",
642	            62
643	          ],
644	          [
645	            "n_items",
646	            1319
647	          ],
648	          [
649	            "DIF_flagged_items",
650	            178
651	          ],
652	          [
653	            "DIF_flagged_rate",
654	            0.135
655	          ],
656	          [
657	            "TPR_delta_ge_1_4",
658	            0.74
659	          ],
660	          [
661	            "FPR",
662	            0.042
663	          ],
664	          [
665	            "AUC",
666	            0.88
667	          ],
668	          [
669	            "GSM8K-GSM1K_gap_DIF_corr_spearman",
670	            0.43
671	          ]
672	        ]
673	      },
674	      {
675	        "title": "Table 10: GSM8K-GSM1K Gap by Model Contamination Status",
676	        "columns": [
677	          "model_group",
678	          "n_models",
679	          "mean_gap",
680	          "std_gap",
681	          "median_gap"
682	        ],
683	        "rows": [
684	          [
685	            "DIF_high_contamination",
686	            18,
687	            0.112,
688	            0.034,
689	            0.105
690	          ],
691	          [
692	            "DIF_low_contamination",
693	            22,
694	            0.051,
695	            0.028,
696	            0.047
697	          ],
698	          [
699	            "DIF_clean",
700	            22,
701	            0.024,
702	            0.019,
703	            0.02
704	          ]
705	        ]
706	      }
707	    ],
708	    "figures": [],
709	    "analysis": "跨benchmark验证成功，DIF在GSM8K上的检测力（TPR=0.74）与MMLU结果一致（考虑到 较小样本量下的预期衰减）。GSM8K-GSM1K gap与DIF flags的spearman rho=0.43提供了 独立于MMLU-CF的external validation，使用完全不同的ground truth来源。 13.5%的GSM8K items被flagged，与Mirzadeh et al. (NeurIPS 2024)报告的GSM8K contamination prevalence一致。\n\n\nGSM8K是ideal validation target因为GSM1K提供了independent contamination ground truth—— GSM1K是GSM8K的分布匹配但全新的test set，GSM8K-GSM1K accuracy gap直接反映 contamination benefit。DIF在GSM8K上的TPR=0.74（vs MMLU的0.78）略低，因为： (1) 样本量较小（62 models vs MMLU的5055），cohort sizes（28 vs 34）接近power 下限；(2) GSM8K是math reasoning benchmark，item discrimination更依赖reasoning ability而非factual recall，DIF effect sizes分布略低于MMLU。Spearman rho=0.43 between per-model DIF flag count和GSM8K-GSM1K gap是中等相关，因为DIF flags是 binary item-level indicators而GSM8K-GSM1K gap是continuous model-level metric， 二者在aggregation level上不同——item-level DIF flag到model-level gap的mapping 需要通过contamination load（模型见过的flagged items数量）mediating。直接的 per-item correlation（item的DIF flag vs 该item的across-model gap）达到0.41， 提供convergent evidence。这一跨benchmark验证支持DIF检测的generalizability， 不仅限于MMLU。\n"
710	  },
711	  {
712	    "name": "bifactor_irt_equating_pilot",
713	    "description": "在METABENCH MMLU数据上pilot bifactor IRT equating。拟合bifactor model （general factor + subject-specific factors），选择anchor items， 通过fixed-parameter calibration校准replacement items，验证equated score等价性。\n",
714	    "results": {
715	      "bifactor_model_converged": true,
716	      "n_general_factor_loadings_gt_0_3": 11200,
717	      "n_subject_factors": 57,
718	      "subject_factor_loading_mean": 0.42,
719	      "general_factor_loading_mean": 0.58,
720	      "general_factor_variance_explained": 0.48,
721	      "total_variance_explained": 0.72,
722	      "n_anchor_items_selected": 3100,
723	      "anchor_item_criteria": "No DIF (ETS A), discrimination a>0.8, low missingness",
724	      "anchor_item_stability_rho": 0.98,
725	      "n_replacement_items_calibrated": 500,
726	      "equating_spearman_rho": 0.97,
727	      "equating_pearson_r": 0.96,
728	      "equating_rank_displacement_mean": 1.8,
729	      "equating_rank_displacement_max": 12,
730	      "equating_score_rmse": 0.021,
731	      "equating_classification_agreement": 0.94,
732	      "chi_square_equating_test_p": 0.34,
733	      "anchor_item_dif_free_rate": 0.92,
734	      "replacement_item_factor_loading_corr": 0.88
735	    },
736	    "tables": [
737	      {
738	        "title": "Table 11: Bifactor Model Fit Statistics",
739	        "columns": [
740	          "metric",
741	          "value"
742	        ],
743	        "rows": [
744	          [
745	            "RMSEA",
746	            0.028
747	          ],
748	          [
749	            "CFI",
750	            0.96
751	          ],
752	          [
753	            "TLI",
754	            0.95
755	          ],
756	          [
757	            "General_factor_variance_pct",
758	            0.48
759	          ],
760	          [
761	            "Subject_factors_variance_pct",
762	            0.24
763	          ],
764	          [
765	            "Total_variance_explained",
766	            0.72
767	          ],
768	          [
769	            "N_subjects_factors",
770	            57
771	          ]
772	        ]
773	      },
774	      {
775	        "title": "Table 12: Equating Results — Original vs Replaced Benchmark",
776	        "columns": [
777	          "metric",
778	          "value",
779	          "interpretation"
780	        ],
781	        "rows": [
782	          [
783	            "Spearman_rho",
784	            0.97,
785	            "Rankings nearly identical"
786	          ],
787	          [
788	            "Pearson_r",
789	            0.96,
790	            "Scores linearly related"
791	          ],
792	          [
793	            "RMSE",
794	            0.021,
795	            "Minimal score displacement"
796	          ],
797	          [
798	            "Mean_rank_displacement",
799	            1.8,
800	            "Average 1-2 rank positions"
801	          ],
802	          [
803	            "Max_rank_displacement",
804	            12,
805	            "Worst case still within noise"
806	          ],
807	          [
808	            "Classification_agreement",
809	            0.94,
810	            "94% same performance tier"
811	          ],
812	          [
813	            "Chi_sq_test_p",
814	            0.34,
815	            "Cannot reject equivalence"
816	          ]
817	        ]
818	      }
819	    ],
820	    "figures": [],
821	    "analysis": "Bifactor IRT equating在MMLU上达到psychometric standard（rho=0.97, RMSE=0.021）， 证明了Claim 3的可行性——contaminated items可以被replaced而preserving benchmark comparability。关键支撑是25% anchor items提供了stable calibration bridge， bifactor structure正确捕获了MMLU的multi-subject + general ability structure。 Classification agreement=0.94意味着在实际的model evaluation场景中，equated benchmark与original benchmark在94%的模型对比决策上给出相同结论。\n\n\nBifactor model在MMLU上的良好拟合源于MMLU的psychometric structure：它是multi-subject benchmark，每个subject（57个）构成一个specific factor，同时存在general cognitive ability factor（因为performance across subjects是正相关的——general intelligence drives cross-domain performance）。General factor解释48%方差，与educational testing中的typical bifactor results一致。Anchor items（3100个，~25%）是高稳定性、 无DIF的items——在temporal cohorts间parameter estimates一致，表明未被contaminate。 25%的anchor rate在psychometric equating中是standard practice（Kolen & Brennan 推荐20-30%）。Equating后的Spearman rho=0.97表明模型rankings在original vs replaced benchmark间高度保持——rank displacement mean=1.8意味着平均每个模型只 移动1-2个排名位置。这一精度来自fixed-parameter calibration的mechanics： replacement items的parameters在anchor item scale上calibrate，数学上保证了 score comparability（up to estimation error）。Score RMSE=0.021（在0-1 scale上） 反映estimation uncertainty而非systematic bias。Chi-square equating test p=0.34 表明无法拒绝\"equated scores等价于original scores\"的null hypothesis，即equating 在统计上成功。\n"
822	  },
823	  {
824	    "name": "item_generation_calibration",
825	    "description": "生成replacement items并通过student simulation校准。对比prompt-based difficulty targeting与empirical calibration的精度。在holdout model panel上验证。\n",
826	    "results": {
827	      "n_items_generated": 500,
828	      "n_items_passing_quality_filter": 420,
829	      "quality_filter_pass_rate": 0.84,
830	      "n_student_sim_models": 8,
831	      "student_sim_responses_per_item": 200,
832	      "difficulty_rho_student_sim": 0.78,
833	      "difficulty_rho_prompt_targeting": 0.28,
834	      "difficulty_rmse_student_sim": 0.14,
835	      "difficulty_rmse_prompt_targeting": 0.38,
836	      "discrimination_rho_student_sim": 0.62,
837	      "discrimination_rho_prompt_targeting": 0.15,
838	      "holdout_panel_equating_rho": 0.95,
839	      "construct_validity_factor_loading_corr": 0.85,
840	      "subject_match_accuracy": 0.92,
841	      "cognitive_level_match_accuracy": 0.78,
842	      "item_format_compliance": 0.97
843	    },
844	    "tables": [
845	      {
846	        "title": "Table 13: Calibration Method Comparison",
847	        "columns": [
848	          "method",
849	          "difficulty_rho",
850	          "difficulty_rmse",
851	          "discrimination_rho",
852	          "n_items"
853	        ],
854	        "rows": [
855	          [
856	            "Student_simulation",
857	            0.78,
858	            0.14,
859	            0.62,
860	            420
861	          ],
862	          [
863	            "Prompt_targeting",
864	            0.28,
865	            0.38,
866	            0.15,
867	            420
868	          ],
869	          [
870	            "Random_baseline",
871	            0.05,
872	            0.52,
873	            0.03,
874	            420
875	          ]
876	        ]
877	      },
878	      {
879	        "title": "Table 14: Generated Item Quality Metrics",
880	        "columns": [
881	          "metric",
882	          "value"
883	        ],
884	        "rows": [
885	          [
886	            "Quality_filter_pass_rate",
887	            0.84
888	          ],
889	          [
890	            "Subject_match_accuracy",
891	            0.92
892	          ],
893	          [
894	            "Cognitive_level_match",
895	            0.78
896	          ],
897	          [
898	            "Format_compliance",
899	            0.97
900	          ],
901	          [
902	            "Factor_loading_corr",
903	            0.85
904	          ],
905	          [
906	            "Holdout_equating_rho",
907	            0.95
908	          ]
909	        ]
910	      }
911	    ],
912	    "figures": [],
913	    "analysis": "Student simulation校准是item regeneration pipeline的关键enabler，将difficulty estimation精度从prompt-based的rho=0.28提升到0.78——接近3x improvement。 这一结果支持Claim 3的\"empirically calibrated alternatives\"承诺。Holdout panel equating rho=0.95达到psychometric standard，证明end-to-end pipeline（generation → simulation calibration → equating）可以produce functionally equivalent benchmark items。\n\n\nStudent simulation校准（基于arXiv 2601.09953方法）的核心优势是empirical—— 它通过让diverse student models实际回答generated items来estimate difficulty， 而非依赖LLM的self-report。rho=0.78与原论文报告的r=0.75-0.82一致，因为MMLU 的MCQ format与student simulation的optimal use case对齐（forced-choice items 比open-ended items更适合binary response modeling）。Prompt-based targeting 的rho=0.28与arXiv 2602.06631报告的rho=0.10-0.45一致——LLMs在内省difficulty 时系统性地低估hard items、高估easy items，因为difficulty perception与generation capability不同。Student simulation的优势在于它bypasses这种miscalibration， 直接从behavioral responses estimate difficulty。Discrimination的rho=0.62较低 于difficulty的0.78，因为discrimination是IRT的second-order parameter（item sensitivity to ability differences），inherently harder to control through generation——它依赖item的specific cognitive demands，而这些难以通过prompt engineering精确控制。Construct validity factor loading correlation=0.85表明 generated items load on相同的subject-specific factors，preserving MMLU的 bifactor structure。\n"
914	  },
915	  {
916	    "name": "cumulative_bayesian_dif",
917	    "description": "实现Bayesian累积DIF先验。模拟4次连续benchmark administration， 展示evidence accumulation带来的power提升。\n",
918	    "results": {
919	      "n_administrations_simulated": 4,
920	      "n_models_per_administration": 40,
921	      "admin_1_power_medium_delta_1_0": 0.38,
922	      "admin_2_cumulative_power": 0.55,
923	      "admin_3_cumulative_power": 0.7,
924	      "admin_4_cumulative_power": 0.78,
925	      "power_gain_per_administration": [
926	        0.38,
927	        0.17,
928	        0.15,
929	        0.08
930	      ],
931	      "bayesian_bf_threshold": 3.0,
932	      "false_discovery_rate": 0.04,
933	      "convergence_rate": 0.98,
934	      "prior_posterior_shrinkage": 0.42,
935	      "credible_interval_width_admin1": 0.68,
936	      "credible_interval_width_admin4": 0.31
937	    },
938	    "tables": [
939	      {
940	        "title": "Table 15: Cumulative Bayesian DIF Power Over Administrations",
941	        "columns": [
942	          "administration",
943	          "cumulative_n",
944	          "power_delta_1_0",
945	          "power_delta_1_4",
946	          "CI_width"
947	        ],
948	        "rows": [
949	          [
950	            1,
951	            40,
952	            0.38,
953	            0.62,
954	            0.68
955	          ],
956	          [
957	            2,
958	            80,
959	            0.55,
960	            0.76,
961	            0.48
962	          ],
963	          [
964	            3,
965	            120,
966	            0.7,
967	            0.84,
968	            0.37
969	          ],
970	          [
971	            4,
972	            160,
973	            0.78,
974	            0.88,
975	            0.31
976	          ]
977	        ]
978	      }
979	    ],
980	    "figures": [],
981	    "analysis": "Bayesian累积DIF直接回应reviewer concern #2（sample sizes too small）。 4次累积后medium-effect power从0.38→0.78，使DIF对medium effects也实用化。 这一结果支持论文的\"living benchmark\"叙事——不需要一次性获得大样本， 可以通过temporal accumulation逐步建立detection confidence。\n\n\nBayesian累积先验的power gain来自evidence accumulation的数学性质——每次新的 administration提供independent observations，posterior distribution随data收窄。 从single administration的0.38到4次累积的0.78，power nearly doubles。Gain是 diminishing的（0.17→0.15→0.08），因为posterior precision的improvement是 sub-linear in sample size（~√n scaling）。对medium effects（δ=1.0）这尤其重要， 因为classical DIF在single administration with N=40 per cohort时power不足 （Phase 2模拟显示N=50/δ=1.0时TPR仅0.04-0.07）。Bayesian approach通过 accumulating evidence across time解决了这个sample-size limitation——每次 administration贡献40个models，4次累积相当于effective sample of ~160， 但通过informative priors获得比simple pooling更高的statistical efficiency。 BF threshold=3.0（moderate evidence）对应psychometric practice中的standard decision criterion。FDR=0.04 < 0.05表明error control有效。\n"
982	  },
983	  {
984	    "name": "graceful_degradation_analysis",
985	    "description": "分析benchmark在progressive item replacement下的validity degradation。 定义validity metrics，模拟5%-50% replacement，建立理论bounds。\n",
986	    "results": {
987	      "replacement_rates": [
988	        0.05,
989	        0.1,
990	        0.2,
991	        0.5
992	      ],
993	      "ranking_stability_rho_5pct": 0.99,
994	      "ranking_stability_rho_10pct": 0.97,
995	      "ranking_stability_rho_20pct": 0.95,
996	      "ranking_stability_rho_50pct": 0.89,
997	      "score_reliability_alpha_original": 0.94,
998	      "score_reliability_alpha_5pct": 0.93,
999	      "score_reliability_alpha_10pct": 0.93,
1000	      "score_reliability_alpha_20pct": 0.91,
1001	      "score_reliability_alpha_50pct": 0.87,
1002	      "construct_coverage_jaccard_5pct": 0.98,
1003	      "construct_coverage_jaccard_10pct": 0.96,
1004	      "construct_coverage_jaccard_20pct": 0.92,
1005	      "construct_coverage_jaccard_50pct": 0.83,
1006	      "theoretical_rho_lower_bound_formula": "rho >= 1 - k*replacement_rate*(1-r_replacement)",
1007	      "theoretical_rho_lower_bound_20pct": 0.93,
1008	      "empirical_rho_20pct": 0.95,
1009	      "validity_threshold_replacement_rate": 0.35
1010	    },
1011	    "tables": [
1012	      {
1013	        "title": "Table 16: Validity Metrics Under Progressive Replacement",
1014	        "columns": [
1015	          "replacement_rate",
1016	          "ranking_rho",
1017	          "reliability_alpha",
1018	          "construct_jaccard",
1019	          "score_rmse"
1020	        ],
1021	        "rows": [
1022	          [
1023	            0.0,
1024	            1.0,
1025	            0.94,
1026	            1.0,
1027	            0.0
1028	          ],
1029	          [
1030	            0.05,
1031	            0.99,
1032	            0.93,
1033	            0.98,
1034	            0.008
1035	          ],
1036	          [
1037	            0.1,
1038	            0.97,
1039	            0.93,
1040	            0.96,
1041	            0.015
1042	          ],
1043	          [
1044	            0.2,
1045	            0.95,
1046	            0.91,
1047	            0.92,
1048	            0.025
1049	          ],
1050	          [
1051	            0.35,
1052	            0.92,
1053	            0.89,
1054	            0.87,
1055	            0.038
1056	          ],
1057	          [
1058	            0.5,
1059	            0.89,
1060	            0.87,
1061	            0.83,
1062	            0.052
1063	          ]
1064	        ]
1065	      },
1066	      {
1067	        "title": "Table 17: Theoretical vs Empirical Bounds",
1068	        "columns": [
1069	          "replacement_rate",
1070	          "theoretical_rho_lb",
1071	          "empirical_rho",
1072	          "bound_tight"
1073	        ],
1074	        "rows": [
1075	          [
1076	            0.05,
1077	            0.97,
1078	            0.99,
1079	            false
1080	          ],
1081	          [
1082	            0.1,
1083	            0.95,
1084	            0.97,
1085	            false
1086	          ],
1087	          [
1088	            0.2,
1089	            0.93,
1090	            0.95,
1091	            false
1092	          ],
1093	          [
1094	            0.5,
1095	            0.84,
1096	            0.89,
1097	            false
1098	          ]
1099	        ]
1100	      }
1101	    ],
1102	    "figures": [],
1103	    "analysis": "Graceful degradation分析为benchmark regeneration建立了formal safety guarantees。 20% replacement threshold（rho≥0.95）为实际操作提供了clear guideline—— given MMLU上约10.7% items被DIF flagged（plan_001），单轮replacement在安全范围内。 理论bound的conservativeness（empirical consistently exceeds theoretical by 2-5pp） 提供额外safety margin。这一结果完成了Claim 3从detection → generation → equating → validity guarantee的完整pipeline。\n\n\nGraceful degradation的数学基础是：如果replacement items与original items测量相同 construct（通过bifactor equating保证），且parameter estimation是unbiased的， 那么benchmark score的perturbation仅来自estimation error。Ranking stability (Spearman rho)随replacement rate的下降是approximately linear的：5%→0.99, 10%→0.97, 20%→0.95, 50%→0.89。0.95 threshold（psychometric standard for \"essentially equivalent\"）在~20% replacement rate时hit——这意味着可以替换 最多20%的items（~2500 items on MMLU）while maintaining psychometrically equivalent rankings。50% replacement导致rho=0.89，仍然usable但not equivalent。 Score reliability (Cronbach's alpha)从0.94降至0.91 at 20%，因为replacement items的discrimination estimates有更大variance（calibration uncertainty）， but alpha>0.90在psychometric standards中仍属excellent。Construct coverage (Jaccard similarity of subject factor coverage)在20%时为0.92，因为replacement item generation已constrained to same subject，但minor gaps in specific cognitive sub-skills可能出现。Theoretical lower bound formula provides conservative estimate，empirical results consistently exceed it（0.95 > 0.93 at 20%），validating the bound's correctness。\n"
1104	  },
1105	  {
1106	    "name": "item_focused_trees",
1107	    "description": "实现Item-Focused Trees作为categorical cohort DIF的替代方案。 将model release date作为continuous covariate，比较检测力和灵活性。\n",
1108	    "results": {
1109	      "ift_tpr_delta_ge_1_4": 0.81,
1110	      "ift_tpr_delta_ge_1_0": 0.58,
1111	      "ift_fpr": 0.044,
1112	      "ift_auc": 0.9,
1113	      "ift_vs_ets_c_tpr_improvement": 0.03,
1114	      "ift_vs_ets_c_auc_improvement": -0.02,
1115	      "ift_detected_gradual_contamination": true,
1116	      "n_items_with_changepoint": 890,
1117	      "median_changepoint_date": "2023-06",
1118	      "changepoint_clustering_by_subject": true,
1119	      "ift_computation_time_seconds": 340,
1120	      "ets_c_computation_time_seconds": 28
1121	    },
1122	    "tables": [
1123	      {
1124	        "title": "Table 18: Item-Focused Trees vs ETS C Comparison",
1125	        "columns": [
1126	          "method",
1127	          "tpr_ge_1_4",
1128	          "tpr_ge_1_0",
1129	          "fpr",
1130	          "auc",
1131	          "time_sec"
1132	        ],
1133	        "rows": [
1134	          [
1135	            "ETS_C",
1136	            0.78,
1137	            0.45,
1138	            0.038,
1139	            0.92,
1140	            28
1141	          ],
1142	          [
1143	            "Item_Focused_Trees",
1144	            0.81,
1145	            0.58,
1146	            0.044,
1147	            0.9,
1148	            340
1149	          ],
1150	          [
1151	            "Combined",
1152	            0.84,
1153	            0.6,
1154	            0.048,
1155	            0.93,
1156	            368
1157	          ]
1158	        ]
1159	      },
1160	      {
1161	        "title": "Table 19: Contamination Changepoint Analysis",
1162	        "columns": [
1163	          "subject_group",
1164	          "n_items_with_changepoint",
1165	          "median_changepoint",
1166	          "range"
1167	        ],
1168	        "rows": [
1169	          [
1170	            "STEM",
1171	            520,
1172	            "2023-03",
1173	            "2022-06 to 2024-01"
1174	          ],
1175	          [
1176	            "Humanities",
1177	            210,
1178	            "2023-09",
1179	            "2023-01 to 2024-06"
1180	          ],
1181	          [
1182	            "Social_Sciences",
1183	            160,
1184	            "2023-06",
1185	            "2022-09 to 2024-03"
1186	          ]
1187	        ]
1188	      }
1189	    ],
1190	    "figures": [],
1191	    "analysis": "IFT作为P2实验提供了methodological depth——contamination timing的item-specific 和subject-specific patterns是novel finding，支持论文的temporal dynamics narrative。 Detection power的marginal improvement（+3pp TPR）不足以替代ETS C作为primary method，但combined approach（union of flags）将TPR推到0.84。更重要的是IFT的 changepoint analysis为understanding contamination dynamics提供了unique evidence， 可作为analysis section的secondary contribution。\n\nItem-Focused Trees的优势在于不需要arbitrary cohort splits——它自动发现每个item 的contamination onset point（changepoint）作为tree split。TPR=0.81略优于 ETS C的0.78（+3pp），因为IFT可以为每个item找到optimal focal/reference split 而非使用统一的pre/post cutoff。但AUC=0.90略低于ETS C的0.92，因为IFT在small effects区间的precision较低（tree splitting在low-signal regime容易overfit）。 Changepoint clustering by subject是重要的secondary finding——STEM subjects的 median changepoint早于humanities（2023-03 vs 2023-09），反映code-heavy training data对STEM contamination的earlier onset。890个items有detectable changepoints， 与plan_001的1340 flagged items部分重叠（IFT的threshold更conservative因为tree pruning）。计算成本是ETS C的12x，因为recursive partitioning需要对每个item 搜索所有可能splits，但仍在minutes级别（CPU only），实际可用。IFT的主要paper value 是methodological：它证明contamination timing是item-specific而非cohort-uniform， 支持\"contamination as gradual process\"的narrative。\n"
1192	  }
1193	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3fcfb509-c026-4304-9b0e-27331ebf4752",
  "isSidechain": false,
  "promptId": "ed003479-76af-4943-a861-980660b8c55c",
  "type": "user",
  "uuid": "d1ce2520-a46a-4754-b407-fc4f29b49726",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"real_data_dif_mmlu\",\n    \"description\": \"对METABENCH MMLU真实响应矩阵（5,055 models × 12,508 items）执行DIF分析。 按release date切temporal cohorts（pre-2024 vs post-2024 + 年度细分）， 运行ETS C检测，用MMLU-CF作为partial ground truth外部验证。\\n\",\n    \"results\": {\n      \"n_models_total\": 5055,\n      \"n_models_post_2024\": 1820,\n      \"cohort_pre2024_size\": 3235,\n      \"cohort_post2024_size\": 1820,\n      \"annual_cohort_min_size\": 92,\n      \"annual_cohort_max_size\": 2100,\n      \"ets_c_items_flagged_C_level\": 1340,\n      \"ets_c_items_flagged_B_or_C\": 2870,\n      \"ets_c_tpr_delta_ge_1_4\": 0.78,\n      \"ets_c_tpr_delta_ge_1_6\": 0.83,\n      \"ets_c_fpr\": 0.038,\n      \"ets_c_auc_delta_ge_1_4\": 0.92,\n      \"mmlu_cf_correlation_with_dif_flags_phi\": 0.42,\n      \"mmlu_cf_correlation_with_dif_flags_tetrachoric\": 0.48,\n      \"n_mmlu_cf_overlapping_items\": 2780,\n      \"dif_flagged_among_cf_modified\": 0.61,\n      \"dif_flagged_among_cf_unmodified\": 0.07,\n      \"sensitivity_cohort_split_tpr_range\": [\n        0.72,\n        0.83\n      ],\n      \"sensitivity_threshold_tpr_range\": [\n        0.68,\n        0.85\n      ],\n      \"real_irt_param_a_mean\": 1.18,\n      \"real_irt_param_b_mean\": -0.79,\n      \"real_irt_param_a_std\": 0.42\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 1: DIF Detection Power on METABENCH MMLU Real Data\",\n        \"columns\": [\n          \"cohort_split\",\n          \"N_focal\",\n          \"N_ref\",\n          \"delta_range\",\n          \"TPR\",\n          \"FPR\",\n          \"AUC\"\n        ],\n        \"rows\": [\n          [\n            \"pre2024_vs_post2024\",\n            1820,\n            3235,\n            \"≥1.4\",\n            0.78,\n            0.038,\n            0.92\n          ],\n          [\n            \"pre2024_vs_post2024\",\n            1820,\n            3235,\n            \"≥1.6\",\n            0.83,\n            0.038,\n            0.94\n          ],\n          [\n            \"pre2024_vs_post2024\",\n            1820,\n            3235,\n            \"≥1.0\",\n            0.51,\n            0.041,\n            0.83\n          ],\n          [\n            \"2022_vs_2024\",\n            920,\n            2100,\n            \"≥1.4\",\n            0.76,\n            0.036,\n            0.91\n          ],\n          [\n            \"2023_vs_2025\",\n            680,\n            1340,\n            \"≥1.4\",\n            0.74,\n            0.039,\n            0.9\n          ],\n          [\n            \"annual_finest\",\n            92,\n            2100,\n            \"≥1.4\",\n            0.72,\n            0.042,\n            0.88\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 2: MMLU-CF External Validation\",\n        \"columns\": [\n          \"category\",\n          \"n_items\",\n          \"dif_flagged_rate\",\n          \"description\"\n        ],\n        \"rows\": [\n          [\n            \"CF_modified_items\",\n            2780,\n            0.61,\n            \"Items significantly changed in MMLU-CF\"\n          ],\n          [\n            \"CF_unmodified_items\",\n            9728,\n            0.07,\n            \"Items unchanged in MMLU-CF\"\n          ],\n          [\n            \"phi_coefficient\",\n            null,\n            0.42,\n            \"Association between DIF flag and CF modification\"\n          ],\n          [\n            \"tetrachoric_r\",\n            null,\n            0.48,\n            \"Latent correlation estimate\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"真实数据DIF检测power与Phase 2模拟高度一致，验证了模拟参数设定的生态效度。 关键发现：(1) MMLU上约10.7%的items呈现ETS C级DIF，集中在STEM领域，与contamination through pretraining code data的预期一致；(2) MMLU-CF外部验证提供convergent evidence， phi=0.42虽非完美但在partial ground truth条件下合理——完美相关本身不可信，因为CF的 modification策略与contamination并非一一对应；(3) 敏感性分析显示TPR在不同cohort 定义下稳定在0.72-0.83区间，最弱的annual finest split（N_focal=92）仍达0.72， 正好符合Phase 2模拟在N=80条件下的预测。这一结果直接支持Claim 1的real-data validation。\\n\\n\\nPhase 2模拟已在N=100/δ=1.6条件下达到TPR=0.7966，真实参数（a_mean=1.2, b_mean=-0.84） 与模拟设定高度一致。Best档下真实数据复现模拟power的核心条件是：(1) METABENCH post-2024 cohort达到N≈1820，远超模拟的N=100下限，提供充足统计功效；(2) 真实contamination effect sizes在高频benchmark如MMLU上确实存在δ≥1.4的大效应——GSM1K研究已证实10-13pp 的accuracy gap，对应IRT尺度上δ≈1.5-2.0；(3) ETS C基于effect-size阈值而非p-value， 大样本下不会出现inflation问题，反而因estimation precision提高而TPR略优于模拟。 MMLU-CF验证的phi=0.42反映了partial ground truth的本质局限——CF修改的items与真正 contaminated items有交集但不完全重叠，CF修改了部分未被contaminate的items（降低相关）， 同时未修改一些实际被contaminate的items。但0.42的phi系数在psychometric validation中 已属中等偏强，足以作为convergent validity evidence。FPR=0.038与模拟的0.036-0.042 区间一致，因为false positive rate主要由ETS C的Δ_MH阈值决定，不依赖sample size。\\n\"\n  },\n  {\n    \"name\": \"rl_robustness_validation\",\n    \"description\": \"经验验证DIF的RL-robustness。构建SFT-only cohort和含RL-trained模型的cohort， 同时运行DIF与传统检测器（Min-K%、ConStat perturbation、DVD），对比RL条件下的退化。\\n\",\n    \"results\": {\n      \"n_rl_models_evaluated\": 14,\n      \"n_sft_models_evaluated\": 40,\n      \"rl_models_list\": \"DeepSeek-R1, DeepSeek-R1-Distill-{7B,14B,32B,70B}, Qwen2.5-RL-{7B,72B}, Llama-3.1-Nemotron-Ultra-253B, QwQ-32B, Skywork-OR1-{8B,32B}, K1.5-Chat, Eurus-2-7B-PRIME, OpenThinker-7B\\n\",\n      \"dif_tpr_sft_cohort_delta_ge_1_4\": 0.79,\n      \"dif_tpr_rl_cohort_delta_ge_1_4\": 0.76,\n      \"dif_power_retention_ratio\": 0.96,\n      \"dif_fpr_sft_cohort\": 0.037,\n      \"dif_fpr_rl_cohort\": 0.041,\n      \"mink_auroc_sft\": 0.72,\n      \"mink_auroc_rl\": 0.51,\n      \"mink_degradation_pp\": 21,\n      \"constat_auroc_sft\": 0.68,\n      \"constat_auroc_rl\": 0.53,\n      \"constat_degradation_pp\": 15,\n      \"dvd_auroc_sft\": 0.65,\n      \"dvd_auroc_rl\": 0.54,\n      \"dvd_degradation_pp\": 11,\n      \"perplexity_auroc_sft\": 0.61,\n      \"perplexity_auroc_rl\": 0.5,\n      \"lowercase_auroc_sft\": 0.58,\n      \"lowercase_auroc_rl\": 0.49,\n      \"traditional_mean_auroc_sft\": 0.65,\n      \"traditional_mean_auroc_rl\": 0.51,\n      \"p_value_dif_retention_paired_t\": 0.62,\n      \"p_value_traditional_degradation_paired_t\": 0.0003\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 3: DIF vs Traditional Detectors Under RL Training\",\n        \"columns\": [\n          \"method\",\n          \"auroc_sft_cohort\",\n          \"auroc_rl_cohort\",\n          \"degradation_pp\",\n          \"p_value\"\n        ],\n        \"rows\": [\n          [\n            \"DIF_ETS_C\",\n            0.91,\n            0.9,\n            1,\n            0.62\n          ],\n          [\n            \"Min-K%\",\n            0.72,\n            0.51,\n            21,\n            0.0002\n          ],\n          [\n            \"ConStat_perturbation\",\n            0.68,\n            0.53,\n            15,\n            0.001\n          ],\n          [\n            \"DVD_generation_var\",\n            0.65,\n            0.54,\n            11,\n            0.004\n          ],\n          [\n            \"Perplexity\",\n            0.61,\n            0.5,\n            11,\n            0.003\n          ],\n          [\n            \"Lowercase\",\n            0.58,\n            0.49,\n            9,\n            0.008\n          ],\n          [\n            \"zlib_ratio\",\n            0.6,\n            0.5,\n            10,\n            0.005\n          ],\n          [\n            \"Top-K_prob\",\n            0.63,\n            0.52,\n            11,\n            0.003\n          ],\n          [\n            \"Ref_model_loss\",\n            0.67,\n            0.53,\n            14,\n            0.002\n          ],\n          [\n            \"Neighbor_text\",\n            0.59,\n            0.5,\n            9,\n            0.007\n          ],\n          [\n            \"DetectGPT\",\n            0.55,\n            0.49,\n            6,\n            0.04\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 4: DIF Power Retention by RL Training Intensity\",\n        \"columns\": [\n          \"model_group\",\n          \"n_models\",\n          \"dif_tpr_delta_ge_1_4\",\n          \"dif_fpr\",\n          \"retention_vs_sft\"\n        ],\n        \"rows\": [\n          [\n            \"SFT_only\",\n            40,\n            0.79,\n            0.037,\n            1.0\n          ],\n          [\n            \"Light_RL_under_500_steps\",\n            6,\n            0.78,\n            0.039,\n            0.99\n          ],\n          [\n            \"Heavy_RL_over_500_steps\",\n            8,\n            0.75,\n            0.041,\n            0.95\n          ],\n          [\n            \"All_RL\",\n            14,\n            0.76,\n            0.041,\n            0.96\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"RL-robustness经验验证是论文最核心的卖点。DIF power retention ratio=0.96意味着 RL训练对DIF检测力几乎无影响（paired t-test p=0.62，无统计显著差异），而10种传统 检测器平均退化14pp至near-random（mean AUROC=0.51）。这直接验证了理论预测： DIF操作在group-level behavioral space，RL无法在不放弃contamination benefit的 情况下消除这一信号。Heavy RL（>500 steps）组的轻微衰减（retention=0.95）可归因于 更高general ability导致的effect size estimation compression，而非mechanism failure。 这一结果使headline claim成立：\\\"DIF maintains 76% TPR where 10 existing methods degrade to random under RL training.\\\"\\n\\n\\nDIF的RL-robustness源于其检测机制的根本差异。传统检测器（Min-K%、perplexity-based） 依赖within-model output distributions——GRPO/PPO通过policy smoothing将memorized items 的output distribution调整到与clean items相似，消除可检测的distributional anomaly。 Wang et al. (ICLR 2026)已实证证明这种退化：~156 GRPO steps即可将多数检测器降至 near-random。DIF则完全不同：它比较的是group-level Item Characteristic Curves—— \\\"给定相同latent ability θ，focal group（post-training cohort）在item j上的correct probability是否高于reference group\\\"。RL训练可以smooth output token distributions， 但无法消除behavioral fact：\\\"这个模型答对了这道它memorized的题\\\"。除非RL训练能让模型 在memorized items上故意答错（这会negate contamination的目的），否则group-level behavioral pattern必然保留。Power retention ratio=0.96（而非1.0）的微小衰减来自 RL模型通常具有更高的general ability θ，这略微压缩了DIF effect size的估计——但这是 统计层面的minor attenuation，不是mechanistic failure。传统检测器的AUROC从0.65降至 0.51（mean across methods），与Wang et al.报告的14-20pp退化一致。\\n\"\n  },\n  {\n    \"name\": \"constat_perturbation_eval\",\n    \"description\": \"独立评估ConStat-style perturbation testing在MMLU上的检测力， 生成200+ items的语义等价改写，比较原始vs改写表现，刻画effect size谱上的检测力。\\n\",\n    \"results\": {\n      \"n_items_reformulated\": 240,\n      \"n_models_tested\": 35,\n      \"n_reformulations_per_item\": 5,\n      \"constat_tpr_non_rl_delta_ge_0_6\": 0.68,\n      \"constat_tpr_non_rl_delta_ge_1_0\": 0.74,\n      \"constat_tpr_non_rl_delta_ge_1_4\": 0.62,\n      \"constat_tpr_rl_delta_ge_0_6\": 0.31,\n      \"constat_tpr_rl_delta_ge_1_0\": 0.38,\n      \"constat_fpr_non_rl\": 0.06,\n      \"constat_fpr_rl\": 0.08,\n      \"constat_fdr_controlled_alpha_0_05\": 0.048,\n      \"mean_accuracy_drop_contaminated_items\": 0.18,\n      \"mean_accuracy_drop_clean_items\": 0.03,\n      \"reformulation_semantic_similarity\": 0.91\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 5: ConStat Detection Power by Effect Size and Model Type\",\n        \"columns\": [\n          \"model_type\",\n          \"delta_range\",\n          \"n_items\",\n          \"TPR\",\n          \"FPR\",\n          \"FDR\"\n        ],\n        \"rows\": [\n          [\n            \"non_RL\",\n            \"≥0.6\",\n            142,\n            0.68,\n            0.06,\n            0.048\n          ],\n          [\n            \"non_RL\",\n            \"≥1.0\",\n            87,\n            0.74,\n            0.06,\n            0.041\n          ],\n          [\n            \"non_RL\",\n            \"≥1.4\",\n            48,\n            0.62,\n            0.06,\n            0.052\n          ],\n          [\n            \"RL\",\n            \"≥0.6\",\n            142,\n            0.31,\n            0.08,\n            0.12\n          ],\n          [\n            \"RL\",\n            \"≥1.0\",\n            87,\n            0.38,\n            0.08,\n            0.1\n          ],\n          [\n            \"all_models\",\n            \"≥0.6\",\n            142,\n            0.52,\n            0.07,\n            0.07\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"ConStat在non-RL模型上的medium-effect-size检测力（δ≥0.6: TPR=0.68）验证了其在 ensemble中的角色——填补DIF在small-to-medium effects上的盲区。RL条件下的急剧退化 （TPR从0.68→0.31）与Wang et al.的发现一致，因为perturbation sensitivity本质上仍 依赖于surface-form specific memorization pattern，RL训练将其平滑化。FDR控制在 non-RL条件下有效（0.048 < 0.05），但RL条件下FDR升至0.12，需在ensemble中对RL模型 降低ConStat权重。\\n\\n\\nConStat的检测逻辑是：contaminated models在original items上表现异常好，但在 semantically equivalent reformulations上表现回落——因为memorization是surface-form specific的。在non-RL models上，这一逻辑有效：SFT训练的memorization直接绑定到 token sequences，reformulation打破了这种绑定，导致contaminated items上出现显著 accuracy drop（mean=0.18 vs clean items的0.03）。TPR在δ≥0.6时达0.68，因为即使 中等效应的contamination也会在perturbation下暴露。但在δ≥1.4时TPR反而降到0.62， 因为极大effect size的items通常是extremely easy items（即使不contaminate也正确率高）， reformulation后的drop较小。ConStat在RL模型上急剧退化（TPR从0.68降至0.31），因为 GRPO/PPO的policy optimization使模型学会了更general的answer patterns而非 surface-form memorization——RL模型在reformulated items上的accuracy drop较小， 使perturbation signal模糊化。这正是ConStat在ensemble中的定位：覆盖non-RL models的 medium effect sizes（DIF在δ<1.0时power不足），但在RL场景下需要DIF补位。\\n\"\n  },\n  {\n    \"name\": \"dvd_generation_variance_eval\",\n    \"description\": \"独立评估DVD generation variance在MMLU上的检测力，对10-15个open-weight模型 每item生成50次response，计算generation variance分数，检测bimodal distributions。\\n\",\n    \"results\": {\n      \"n_models_evaluated\": 12,\n      \"n_items_evaluated\": 2000,\n      \"responses_per_item\": 50,\n      \"temperature_range\": [\n        0.7,\n        1.0\n      ],\n      \"dvd_tpr_variant_contamination\": 0.65,\n      \"dvd_tpr_verbatim_contamination\": 0.38,\n      \"dvd_tpr_all_contamination\": 0.52,\n      \"dvd_fpr\": 0.07,\n      \"dvd_auroc_variant\": 0.78,\n      \"dvd_auroc_verbatim\": 0.62,\n      \"dvd_auroc_overall\": 0.71,\n      \"bimodal_detection_rate_contaminated\": 0.58,\n      \"bimodal_detection_rate_clean\": 0.04,\n      \"dvd_tpr_rl_variant\": 0.47,\n      \"dvd_tpr_rl_verbatim\": 0.29,\n      \"generation_variance_contaminated_mean\": 0.31,\n      \"generation_variance_clean_mean\": 0.12\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 6: DVD Detection Power by Contamination Type\",\n        \"columns\": [\n          \"contamination_type\",\n          \"model_type\",\n          \"n_items\",\n          \"TPR\",\n          \"FPR\",\n          \"AUROC\"\n        ],\n        \"rows\": [\n          [\n            \"variant\",\n            \"non_RL\",\n            320,\n            0.65,\n            0.07,\n            0.78\n          ],\n          [\n            \"verbatim\",\n            \"non_RL\",\n            480,\n            0.38,\n            0.07,\n            0.62\n          ],\n          [\n            \"all\",\n            \"non_RL\",\n            800,\n            0.52,\n            0.07,\n            0.71\n          ],\n          [\n            \"variant\",\n            \"RL\",\n            320,\n            0.47,\n            0.09,\n            0.68\n          ],\n          [\n            \"verbatim\",\n            \"RL\",\n            480,\n            0.29,\n            0.09,\n            0.57\n          ],\n          [\n            \"all\",\n            \"RL\",\n            800,\n            0.38,\n            0.09,\n            0.63\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DVD填补了ensemble中的variant contamination盲区。DIF主要检测verbatim large effects （模型在original item上的behavioral anomaly），ConStat检测non-RL medium effects， DVD则捕获variant contamination——模型见过类似但不完全相同的items，产生partial memorization的generation variance signal。三者的complementary coverage pattern 在best档下清晰呈现，为ensemble fusion提供了solid foundation。\\n\\n\\nDVD的检测逻辑基于generation variance：contaminated models在memorized items上的 generation distribution呈现bimodal pattern——当temperature sampling触发\\\"recall\\\" mode时high confidence输出memorized answer，否则回到general reasoning mode。 Variant contamination（模型见过item的变体而非原始形式）下DVD最有效（TPR=0.65）， 因为variant exposure创造了partial memorization——模型\\\"几乎记得\\\"答案，导致生成 在confident recall和uncertain reasoning之间振荡，产生高variance和清晰的bimodality。 Verbatim contamination下DVD效果较差（TPR=0.38），因为完全memorized items的生成 variance反而很低（模型每次都确信地输出相同答案），bimodal signal消失。这使DVD与DIF 形成互补：DIF在verbatim large effects上最强，DVD在variant contamination上最强。 RL条件下DVD退化到TPR=0.47（variant），因为GRPO smoothing降低了generation variance 的discriminability，但退化幅度小于ConStat（因为DVD利用的是sampling-level variance 而非perturbation sensitivity，RL对sampling variance的影响弱于对perturbation response的影响）。\\n\"\n  },\n  {\n    \"name\": \"ensemble_fusion\",\n    \"description\": \"融合DIF + ConStat + DVD为multi-signal ensemble。校准per-signal阈值， 评估majority voting和weighted fusion，展示ensemble coverage覆盖全effect-size谱。\\n\",\n    \"results\": {\n      \"ensemble_tpr_full_spectrum\": 0.87,\n      \"ensemble_tpr_delta_ge_1_4\": 0.91,\n      \"ensemble_tpr_delta_ge_1_0\": 0.85,\n      \"ensemble_tpr_delta_ge_0_6\": 0.78,\n      \"ensemble_fpr\": 0.08,\n      \"ensemble_auroc\": 0.93,\n      \"majority_2of3_tpr\": 0.72,\n      \"majority_2of3_fpr\": 0.04,\n      \"weighted_fusion_tpr\": 0.87,\n      \"weighted_fusion_fpr\": 0.08,\n      \"dif_unique_detections_pct\": 0.28,\n      \"constat_unique_detections_pct\": 0.15,\n      \"dvd_unique_detections_pct\": 0.12,\n      \"all_three_overlap_pct\": 0.31,\n      \"two_signal_overlap_pct\": 0.14,\n      \"ensemble_tpr_rl_models\": 0.82,\n      \"ensemble_tpr_non_rl_models\": 0.9,\n      \"optimal_weights_dif\": 0.45,\n      \"optimal_weights_constat\": 0.3,\n      \"optimal_weights_dvd\": 0.25\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 7: Ensemble vs Individual Signal Detection Power\",\n        \"columns\": [\n          \"method\",\n          \"tpr_full\",\n          \"tpr_ge_1_4\",\n          \"tpr_ge_0_6\",\n          \"fpr\",\n          \"auroc\"\n        ],\n        \"rows\": [\n          [\n            \"DIF_only\",\n            0.58,\n            0.78,\n            0.35,\n            0.038,\n            0.84\n          ],\n          [\n            \"ConStat_only\",\n            0.44,\n            0.62,\n            0.68,\n            0.06,\n            0.76\n          ],\n          [\n            \"DVD_only\",\n            0.38,\n            0.38,\n            0.45,\n            0.07,\n            0.71\n          ],\n          [\n            \"Majority_2of3\",\n            0.72,\n            0.81,\n            0.64,\n            0.04,\n            0.89\n          ],\n          [\n            \"Weighted_fusion\",\n            0.87,\n            0.91,\n            0.78,\n            0.08,\n            0.93\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 8: Signal Complementarity Analysis\",\n        \"columns\": [\n          \"detection_source\",\n          \"pct_of_total_detections\",\n          \"example_regime\"\n        ],\n        \"rows\": [\n          [\n            \"DIF_unique\",\n            0.28,\n            \"Large effect + RL models\"\n          ],\n          [\n            \"ConStat_unique\",\n            0.15,\n            \"Medium effect + non-RL models\"\n          ],\n          [\n            \"DVD_unique\",\n            0.12,\n            \"Variant contamination\"\n          ],\n          [\n            \"DIF_and_ConStat\",\n            0.08,\n            \"Large effect + non-RL\"\n          ],\n          [\n            \"DIF_and_DVD\",\n            0.04,\n            \"Large variant + RL\"\n          ],\n          [\n            \"ConStat_and_DVD\",\n            0.02,\n            \"Medium variant + non-RL\"\n          ],\n          [\n            \"All_three\",\n            0.31,\n            \"Large effect + non-RL + verbatim\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Ensemble coverage分析是Claim 2的核心evidence。三信号互补的清晰pattern—— DIF覆盖RL+large effects，ConStat覆盖non-RL+medium effects，DVD覆盖variant contamination——使full-spectrum TPR从任何单信号的最高0.58提升到0.87。 关键是unique detections分析：每个信号贡献12-28%的独占检测，证明任何单信号都不可替代。 Weighted fusion优于majority voting 15pp，反映了信号互补性超过信号冗余性—— 在most detection regimes下只有1-2个信号active，majority voting的\\\"2-of-3 agreement\\\" 要求过于保守。\\n\\n\\nEnsemble的power来源于三信号的systematic complementarity。在best档下，每个信号 覆盖不同的effect-size × model-type区间：DIF覆盖large effects（δ≥1.4）且RL-robust， ConStat覆盖non-RL medium effects（δ≥0.6），DVD覆盖variant contamination。 Weighted fusion（DIF=0.45, ConStat=0.30, DVD=0.25）优于majority voting （TPR 0.87 vs 0.72），因为majority voting要求至少2/3信号agree，而在信号覆盖不 重叠的区间（如RL+large effect只有DIF有效），single-signal detection被majority voting过滤掉。Weighted fusion允许high-confidence single signal触发detection。 Full-spectrum TPR=0.87的构成：δ≥1.4区间DIF主导（TPR=0.91），δ=0.6-1.4区间ConStat 补位（将DIF单独的~0.40 TPR提升到ensemble的0.78），variant contamination区间DVD 补位（unique detections 12%）。FPR=0.08略高于single-signal的0.04-0.07，这是 multi-signal fusion的inherent trade-off——更多信号意味着更多false positive opportunities，但0.08仍在可接受范围内。RL模型上ensemble TPR=0.82（vs non-RL的0.90）， 差距来自ConStat在RL条件下的退化被DIF的RL-robustness部分补偿。\\n\"\n  },\n  {\n    \"name\": \"cross_benchmark_gsm8k\",\n    \"description\": \"在GSM8K上复制DIF分析，用GSM1K作为contamination ground truth。 收集50+模型的per-item binary responses，运行temporal cohort DIF， 将DIF flags与per-model GSM8K-GSM1K accuracy gap关联。\\n\",\n    \"results\": {\n      \"n_models_gsm8k\": 62,\n      \"n_items_gsm8k\": 1319,\n      \"n_items_gsm1k\": 1250,\n      \"cohort_pre2024_n\": 28,\n      \"cohort_post2024_n\": 34,\n      \"dif_flagged_items_gsm8k\": 178,\n      \"dif_flagged_rate\": 0.135,\n      \"dif_tpr_gsm8k_delta_ge_1_4\": 0.74,\n      \"dif_fpr_gsm8k\": 0.042,\n      \"gsm8k_gsm1k_gap_mean_all_models\": 0.068,\n      \"gsm8k_gsm1k_gap_mean_contaminated_models\": 0.112,\n      \"gsm8k_gsm1k_gap_mean_clean_models\": 0.024,\n      \"gsm8k_gsm1k_gap_dif_correlation_spearman\": 0.43,\n      \"gsm8k_gsm1k_gap_dif_correlation_pearson\": 0.38,\n      \"per_item_dif_vs_gap_correlation\": 0.41,\n      \"gsm8k_dif_auc\": 0.88\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 9: DIF Detection on GSM8K with GSM1K Ground Truth\",\n        \"columns\": [\n          \"metric\",\n          \"value\"\n        ],\n        \"rows\": [\n          [\n            \"n_models\",\n            62\n          ],\n          [\n            \"n_items\",\n            1319\n          ],\n          [\n            \"DIF_flagged_items\",\n            178\n          ],\n          [\n            \"DIF_flagged_rate\",\n            0.135\n          ],\n          [\n            \"TPR_delta_ge_1_4\",\n            0.74\n          ],\n          [\n            \"FPR\",\n            0.042\n          ],\n          [\n            \"AUC\",\n            0.88\n          ],\n          [\n            \"GSM8K-GSM1K_gap_DIF_corr_spearman\",\n            0.43\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 10: GSM8K-GSM1K Gap by Model Contamination Status\",\n        \"columns\": [\n          \"model_group\",\n          \"n_models\",\n          \"mean_gap\",\n          \"std_gap\",\n          \"median_gap\"\n        ],\n        \"rows\": [\n          [\n            \"DIF_high_contamination\",\n            18,\n            0.112,\n            0.034,\n            0.105\n          ],\n          [\n            \"DIF_low_contamination\",\n            22,\n            0.051,\n            0.028,\n            0.047\n          ],\n          [\n            \"DIF_clean\",\n            22,\n            0.024,\n            0.019,\n            0.02\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"跨benchmark验证成功，DIF在GSM8K上的检测力（TPR=0.74）与MMLU结果一致（考虑到 较小样本量下的预期衰减）。GSM8K-GSM1K gap与DIF flags的spearman rho=0.43提供了 独立于MMLU-CF的external validation，使用完全不同的ground truth来源。 13.5%的GSM8K items被flagged，与Mirzadeh et al. (NeurIPS 2024)报告的GSM8K contamination prevalence一致。\\n\\n\\nGSM8K是ideal validation target因为GSM1K提供了independent contamination ground truth—— GSM1K是GSM8K的分布匹配但全新的test set，GSM8K-GSM1K accuracy gap直接反映 contamination benefit。DIF在GSM8K上的TPR=0.74（vs MMLU的0.78）略低，因为： (1) 样本量较小（62 models vs MMLU的5055），cohort sizes（28 vs 34）接近power 下限；(2) GSM8K是math reasoning benchmark，item discrimination更依赖reasoning ability而非factual recall，DIF effect sizes分布略低于MMLU。Spearman rho=0.43 between per-model DIF flag count和GSM8K-GSM1K gap是中等相关，因为DIF flags是 binary item-level indicators而GSM8K-GSM1K gap是continuous model-level metric， 二者在aggregation level上不同——item-level DIF flag到model-level gap的mapping 需要通过contamination load（模型见过的flagged items数量）mediating。直接的 per-item correlation（item的DIF flag vs 该item的across-model gap）达到0.41， 提供convergent evidence。这一跨benchmark验证支持DIF检测的generalizability， 不仅限于MMLU。\\n\"\n  },\n  {\n    \"name\": \"bifactor_irt_equating_pilot\",\n    \"description\": \"在METABENCH MMLU数据上pilot bifactor IRT equating。拟合bifactor model （general factor + subject-specific factors），选择anchor items， 通过fixed-parameter calibration校准replacement items，验证equated score等价性。\\n\",\n    \"results\": {\n      \"bifactor_model_converged\": true,\n      \"n_general_factor_loadings_gt_0_3\": 11200,\n      \"n_subject_factors\": 57,\n      \"subject_factor_loading_mean\": 0.42,\n      \"general_factor_loading_mean\": 0.58,\n      \"general_factor_variance_explained\": 0.48,\n      \"total_variance_explained\": 0.72,\n      \"n_anchor_items_selected\": 3100,\n      \"anchor_item_criteria\": \"No DIF (ETS A), discrimination a>0.8, low missingness\",\n      \"anchor_item_stability_rho\": 0.98,\n      \"n_replacement_items_calibrated\": 500,\n      \"equating_spearman_rho\": 0.97,\n      \"equating_pearson_r\": 0.96,\n      \"equating_rank_displacement_mean\": 1.8,\n      \"equating_rank_displacement_max\": 12,\n      \"equating_score_rmse\": 0.021,\n      \"equating_classification_agreement\": 0.94,\n      \"chi_square_equating_test_p\": 0.34,\n      \"anchor_item_dif_free_rate\": 0.92,\n      \"replacement_item_factor_loading_corr\": 0.88\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 11: Bifactor Model Fit Statistics\",\n        \"columns\": [\n          \"metric\",\n          \"value\"\n        ],\n        \"rows\": [\n          [\n            \"RMSEA\",\n            0.028\n          ],\n          [\n            \"CFI\",\n            0.96\n          ],\n          [\n            \"TLI\",\n            0.95\n          ],\n          [\n            \"General_factor_variance_pct\",\n            0.48\n          ],\n          [\n            \"Subject_factors_variance_pct\",\n            0.24\n          ],\n          [\n            \"Total_variance_explained\",\n            0.72\n          ],\n          [\n            \"N_subjects_factors\",\n            57\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 12: Equating Results — Original vs Replaced Benchmark\",\n        \"columns\": [\n          \"metric\",\n          \"value\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Spearman_rho\",\n            0.97,\n            \"Rankings nearly identical\"\n          ],\n          [\n            \"Pearson_r\",\n            0.96,\n            \"Scores linearly related\"\n          ],\n          [\n            \"RMSE\",\n            0.021,\n            \"Minimal score displacement\"\n          ],\n          [\n            \"Mean_rank_displacement\",\n            1.8,\n            \"Average 1-2 rank positions\"\n          ],\n          [\n            \"Max_rank_displacement\",\n            12,\n            \"Worst case still within noise\"\n          ],\n          [\n            \"Classification_agreement\",\n            0.94,\n            \"94% same performance tier\"\n          ],\n          [\n            \"Chi_sq_test_p\",\n            0.34,\n            \"Cannot reject equivalence\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Bifactor IRT equating在MMLU上达到psychometric standard（rho=0.97, RMSE=0.021）， 证明了Claim 3的可行性——contaminated items可以被replaced而preserving benchmark comparability。关键支撑是25% anchor items提供了stable calibration bridge， bifactor structure正确捕获了MMLU的multi-subject + general ability structure。 Classification agreement=0.94意味着在实际的model evaluation场景中，equated benchmark与original benchmark在94%的模型对比决策上给出相同结论。\\n\\n\\nBifactor model在MMLU上的良好拟合源于MMLU的psychometric structure：它是multi-subject benchmark，每个subject（57个）构成一个specific factor，同时存在general cognitive ability factor（因为performance across subjects是正相关的——general intelligence drives cross-domain performance）。General factor解释48%方差，与educational testing中的typical bifactor results一致。Anchor items（3100个，~25%）是高稳定性、 无DIF的items——在temporal cohorts间parameter estimates一致，表明未被contaminate。 25%的anchor rate在psychometric equating中是standard practice（Kolen & Brennan 推荐20-30%）。Equating后的Spearman rho=0.97表明模型rankings在original vs replaced benchmark间高度保持——rank displacement mean=1.8意味着平均每个模型只 移动1-2个排名位置。这一精度来自fixed-parameter calibration的mechanics： replacement items的parameters在anchor item scale上calibrate，数学上保证了 score comparability（up to estimation error）。Score RMSE=0.021（在0-1 scale上） 反映estimation uncertainty而非systematic bias。Chi-square equating test p=0.34 表明无法拒绝\\\"equated scores等价于original scores\\\"的null hypothesis，即equating 在统计上成功。\\n\"\n  },\n  {\n    \"name\": \"item_generation_calibration\",\n    \"description\": \"生成replacement items并通过student simulation校准。对比prompt-based difficulty targeting与empirical calibration的精度。在holdout model panel上验证。\\n\",\n    \"results\": {\n      \"n_items_generated\": 500,\n      \"n_items_passing_quality_filter\": 420,\n      \"quality_filter_pass_rate\": 0.84,\n      \"n_student_sim_models\": 8,\n      \"student_sim_responses_per_item\": 200,\n      \"difficulty_rho_student_sim\": 0.78,\n      \"difficulty_rho_prompt_targeting\": 0.28,\n      \"difficulty_rmse_student_sim\": 0.14,\n      \"difficulty_rmse_prompt_targeting\": 0.38,\n      \"discrimination_rho_student_sim\": 0.62,\n      \"discrimination_rho_prompt_targeting\": 0.15,\n      \"holdout_panel_equating_rho\": 0.95,\n      \"construct_validity_factor_loading_corr\": 0.85,\n      \"subject_match_accuracy\": 0.92,\n      \"cognitive_level_match_accuracy\": 0.78,\n      \"item_format_compliance\": 0.97\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 13: Calibration Method Comparison\",\n        \"columns\": [\n          \"method\",\n          \"difficulty_rho\",\n          \"difficulty_rmse\",\n          \"discrimination_rho\",\n          \"n_items\"\n        ],\n        \"rows\": [\n          [\n            \"Student_simulation\",\n            0.78,\n            0.14,\n            0.62,\n            420\n          ],\n          [\n            \"Prompt_targeting\",\n            0.28,\n            0.38,\n            0.15,\n            420\n          ],\n          [\n            \"Random_baseline\",\n            0.05,\n            0.52,\n            0.03,\n            420\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 14: Generated Item Quality Metrics\",\n        \"columns\": [\n          \"metric\",\n          \"value\"\n        ],\n        \"rows\": [\n          [\n            \"Quality_filter_pass_rate\",\n            0.84\n          ],\n          [\n            \"Subject_match_accuracy\",\n            0.92\n          ],\n          [\n            \"Cognitive_level_match\",\n            0.78\n          ],\n          [\n            \"Format_compliance\",\n            0.97\n          ],\n          [\n            \"Factor_loading_corr\",\n            0.85\n          ],\n          [\n            \"Holdout_equating_rho\",\n            0.95\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Student simulation校准是item regeneration pipeline的关键enabler，将difficulty estimation精度从prompt-based的rho=0.28提升到0.78——接近3x improvement。 这一结果支持Claim 3的\\\"empirically calibrated alternatives\\\"承诺。Holdout panel equating rho=0.95达到psychometric standard，证明end-to-end pipeline（generation → simulation calibration → equating）可以produce functionally equivalent benchmark items。\\n\\n\\nStudent simulation校准（基于arXiv 2601.09953方法）的核心优势是empirical—— 它通过让diverse student models实际回答generated items来estimate difficulty， 而非依赖LLM的self-report。rho=0.78与原论文报告的r=0.75-0.82一致，因为MMLU 的MCQ format与student simulation的optimal use case对齐（forced-choice items 比open-ended items更适合binary response modeling）。Prompt-based targeting 的rho=0.28与arXiv 2602.06631报告的rho=0.10-0.45一致——LLMs在内省difficulty 时系统性地低估hard items、高估easy items，因为difficulty perception与generation capability不同。Student simulation的优势在于它bypasses这种miscalibration， 直接从behavioral responses estimate difficulty。Discrimination的rho=0.62较低 于difficulty的0.78，因为discrimination是IRT的second-order parameter（item sensitivity to ability differences），inherently harder to control through generation——它依赖item的specific cognitive demands，而这些难以通过prompt engineering精确控制。Construct validity factor loading correlation=0.85表明 generated items load on相同的subject-specific factors，preserving MMLU的 bifactor structure。\\n\"\n  },\n  {\n    \"name\": \"cumulative_bayesian_dif\",\n    \"description\": \"实现Bayesian累积DIF先验。模拟4次连续benchmark administration， 展示evidence accumulation带来的power提升。\\n\",\n    \"results\": {\n      \"n_administrations_simulated\": 4,\n      \"n_models_per_administration\": 40,\n      \"admin_1_power_medium_delta_1_0\": 0.38,\n      \"admin_2_cumulative_power\": 0.55,\n      \"admin_3_cumulative_power\": 0.7,\n      \"admin_4_cumulative_power\": 0.78,\n      \"power_gain_per_administration\": [\n        0.38,\n        0.17,\n        0.15,\n        0.08\n      ],\n      \"bayesian_bf_threshold\": 3.0,\n      \"false_discovery_rate\": 0.04,\n      \"convergence_rate\": 0.98,\n      \"prior_posterior_shrinkage\": 0.42,\n      \"credible_interval_width_admin1\": 0.68,\n      \"credible_interval_width_admin4\": 0.31\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 15: Cumulative Bayesian DIF Power Over Administrations\",\n        \"columns\": [\n          \"administration\",\n          \"cumulative_n\",\n          \"power_delta_1_0\",\n          \"power_delta_1_4\",\n          \"CI_width\"\n        ],\n        \"rows\": [\n          [\n            1,\n            40,\n            0.38,\n            0.62,\n            0.68\n          ],\n          [\n            2,\n            80,\n            0.55,\n            0.76,\n            0.48\n          ],\n          [\n            3,\n            120,\n            0.7,\n            0.84,\n            0.37\n          ],\n          [\n            4,\n            160,\n            0.78,\n            0.88,\n            0.31\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Bayesian累积DIF直接回应reviewer concern #2（sample sizes too small）。 4次累积后medium-effect power从0.38→0.78，使DIF对medium effects也实用化。 这一结果支持论文的\\\"living benchmark\\\"叙事——不需要一次性获得大样本， 可以通过temporal accumulation逐步建立detection confidence。\\n\\n\\nBayesian累积先验的power gain来自evidence accumulation的数学性质——每次新的 administration提供independent observations，posterior distribution随data收窄。 从single administration的0.38到4次累积的0.78，power nearly doubles。Gain是 diminishing的（0.17→0.15→0.08），因为posterior precision的improvement是 sub-linear in sample size（~√n scaling）。对medium effects（δ=1.0）这尤其重要， 因为classical DIF在single administration with N=40 per cohort时power不足 （Phase 2模拟显示N=50/δ=1.0时TPR仅0.04-0.07）。Bayesian approach通过 accumulating evidence across time解决了这个sample-size limitation——每次 administration贡献40个models，4次累积相当于effective sample of ~160， 但通过informative priors获得比simple pooling更高的statistical efficiency。 BF threshold=3.0（moderate evidence）对应psychometric practice中的standard decision criterion。FDR=0.04 < 0.05表明error control有效。\\n\"\n  },\n  {\n    \"name\": \"graceful_degradation_analysis\",\n    \"description\": \"分析benchmark在progressive item replacement下的validity degradation。 定义validity metrics，模拟5%-50% replacement，建立理论bounds。\\n\",\n    \"results\": {\n      \"replacement_rates\": [\n        0.05,\n        0.1,\n        0.2,\n        0.5\n      ],\n      \"ranking_stability_rho_5pct\": 0.99,\n      \"ranking_stability_rho_10pct\": 0.97,\n      \"ranking_stability_rho_20pct\": 0.95,\n      \"ranking_stability_rho_50pct\": 0.89,\n      \"score_reliability_alpha_original\": 0.94,\n      \"score_reliability_alpha_5pct\": 0.93,\n      \"score_reliability_alpha_10pct\": 0.93,\n      \"score_reliability_alpha_20pct\": 0.91,\n      \"score_reliability_alpha_50pct\": 0.87,\n      \"construct_coverage_jaccard_5pct\": 0.98,\n      \"construct_coverage_jaccard_10pct\": 0.96,\n      \"construct_coverage_jaccard_20pct\": 0.92,\n      \"construct_coverage_jaccard_50pct\": 0.83,\n      \"theoretical_rho_lower_bound_formula\": \"rho >= 1 - k*replacement_rate*(1-r_replacement)\",\n      \"theoretical_rho_lower_bound_20pct\": 0.93,\n      \"empirical_rho_20pct\": 0.95,\n      \"validity_threshold_replacement_rate\": 0.35\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 16: Validity Metrics Under Progressive Replacement\",\n        \"columns\": [\n          \"replacement_rate\",\n          \"ranking_rho\",\n          \"reliability_alpha\",\n          \"construct_jaccard\",\n          \"score_rmse\"\n        ],\n        \"rows\": [\n          [\n            0.0,\n            1.0,\n            0.94,\n            1.0,\n            0.0\n          ],\n          [\n            0.05,\n            0.99,\n            0.93,\n            0.98,\n            0.008\n          ],\n          [\n            0.1,\n            0.97,\n            0.93,\n            0.96,\n            0.015\n          ],\n          [\n            0.2,\n            0.95,\n            0.91,\n            0.92,\n            0.025\n          ],\n          [\n            0.35,\n            0.92,\n            0.89,\n            0.87,\n            0.038\n          ],\n          [\n            0.5,\n            0.89,\n            0.87,\n            0.83,\n            0.052\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 17: Theoretical vs Empirical Bounds\",\n        \"columns\": [\n          \"replacement_rate\",\n          \"theoretical_rho_lb\",\n          \"empirical_rho\",\n          \"bound_tight\"\n        ],\n        \"rows\": [\n          [\n            0.05,\n            0.97,\n            0.99,\n            false\n          ],\n          [\n            0.1,\n            0.95,\n            0.97,\n            false\n          ],\n          [\n            0.2,\n            0.93,\n            0.95,\n            false\n          ],\n          [\n            0.5,\n            0.84,\n            0.89,\n            false\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Graceful degradation分析为benchmark regeneration建立了formal safety guarantees。 20% replacement threshold（rho≥0.95）为实际操作提供了clear guideline—— given MMLU上约10.7% items被DIF flagged（plan_001），单轮replacement在安全范围内。 理论bound的conservativeness（empirical consistently exceeds theoretical by 2-5pp） 提供额外safety margin。这一结果完成了Claim 3从detection → generation → equating → validity guarantee的完整pipeline。\\n\\n\\nGraceful degradation的数学基础是：如果replacement items与original items测量相同 construct（通过bifactor equating保证），且parameter estimation是unbiased的， 那么benchmark score的perturbation仅来自estimation error。Ranking stability (Spearman rho)随replacement rate的下降是approximately linear的：5%→0.99, 10%→0.97, 20%→0.95, 50%→0.89。0.95 threshold（psychometric standard for \\\"essentially equivalent\\\"）在~20% replacement rate时hit——这意味着可以替换 最多20%的items（~2500 items on MMLU）while maintaining psychometrically equivalent rankings。50% replacement导致rho=0.89，仍然usable但not equivalent。 Score reliability (Cronbach's alpha)从0.94降至0.91 at 20%，因为replacement items的discrimination estimates有更大variance（calibration uncertainty）， but alpha>0.90在psychometric standards中仍属excellent。Construct coverage (Jaccard similarity of subject factor coverage)在20%时为0.92，因为replacement item generation已constrained to same subject，但minor gaps in specific cognitive sub-skills可能出现。Theoretical lower bound formula provides conservative estimate，empirical results consistently exceed it（0.95 > 0.93 at 20%），validating the bound's correctness。\\n\"\n  },\n  {\n    \"name\": \"item_focused_trees\",\n    \"description\": \"实现Item-Focused Trees作为categorical cohort DIF的替代方案。 将model release date作为continuous covariate，比较检测力和灵活性。\\n\",\n    \"results\": {\n      \"ift_tpr_delta_ge_1_4\": 0.81,\n      \"ift_tpr_delta_ge_1_0\": 0.58,\n      \"ift_fpr\": 0.044,\n      \"ift_auc\": 0.9,\n      \"ift_vs_ets_c_tpr_improvement\": 0.03,\n      \"ift_vs_ets_c_auc_improvement\": -0.02,\n      \"ift_detected_gradual_contamination\": true,\n      \"n_items_with_changepoint\": 890,\n      \"median_changepoint_date\": \"2023-06\",\n      \"changepoint_clustering_by_subject\": true,\n      \"ift_computation_time_seconds\": 340,\n      \"ets_c_computation_time_seconds\": 28\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 18: Item-Focused Trees vs ETS C Comparison\",\n        \"columns\": [\n          \"method\",\n          \"tpr_ge_1_4\",\n          \"tpr_ge_1_0\",\n          \"fpr\",\n          \"auc\",\n          \"time_sec\"\n        ],\n        \"rows\": [\n          [\n            \"ETS_C\",\n            0.78,\n            0.45,\n            0.038,\n            0.92,\n            28\n          ],\n          [\n            \"Item_Focused_Trees\",\n            0.81,\n            0.58,\n            0.044,\n            0.9,\n            340\n          ],\n          [\n            \"Combined\",\n            0.84,\n            0.6,\n            0.048,\n            0.93,\n            368\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 19: Contamination Changepoint Analysis\",\n        \"columns\": [\n          \"subject_group\",\n          \"n_items_with_changepoint\",\n          \"median_changepoint\",\n          \"range\"\n        ],\n        \"rows\": [\n          [\n            \"STEM\",\n            520,\n            \"2023-03\",\n            \"2022-06 to 2024-01\"\n          ],\n          [\n            \"Humanities\",\n            210,\n            \"2023-09\",\n            \"2023-01 to 2024-06\"\n          ],\n          [\n            \"Social_Sciences\",\n            160,\n            \"2023-06\",\n            \"2022-09 to 2024-03\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"IFT作为P2实验提供了methodological depth——contamination timing的item-specific 和subject-specific patterns是novel finding，支持论文的temporal dynamics narrative。 Detection power的marginal improvement（+3pp TPR）不足以替代ETS C作为primary method，但combined approach（union of flags）将TPR推到0.84。更重要的是IFT的 changepoint analysis为understanding contamination dynamics提供了unique evidence， 可作为analysis section的secondary contribution。\\n\\nItem-Focused Trees的优势在于不需要arbitrary cohort splits——它自动发现每个item 的contamination onset point（changepoint）作为tree split。TPR=0.81略优于 ETS C的0.78（+3pp），因为IFT可以为每个item找到optimal focal/reference split 而非使用统一的pre/post cutoff。但AUC=0.90略低于ETS C的0.92，因为IFT在small effects区间的precision较低（tree splitting在low-signal regime容易overfit）。 Changepoint clustering by subject是重要的secondary finding——STEM subjects的 median changepoint早于humanities（2023-03 vs 2023-09），反映code-heavy training data对STEM contamination的earlier onset。890个items有detectable changepoints， 与plan_001的1340 flagged items部分重叠（IFT的threshold更conservative因为tree pruning）。计算成本是ETS C的12x，因为recursive partitioning需要对每个item 搜索所有可能splits，但仍在minutes级别（CPU only），实际可用。IFT的主要paper value 是methodological：它证明contamination timing是item-specific而非cohort-uniform， 支持\\\"contamination as gradual process\\\"的narrative。\\n\"\n  }\n]",
      "numLines": 1193,
      "startLine": 1,
      "totalLines": 1193
    }
  },
  "sourceToolAssistantUUID": "3fcfb509-c026-4304-9b0e-27331ebf4752",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T19:58:56.150Z_

<details><summary>↩ Tool result · `toolu_01PbbSvJeuUb7crekM14hpk8`</summary>

```text
1	# Paper Framing — irt_equated_bench_regen
2	
3	## Target Venue
4	- Primary: ICLR 2027 (expected deadline ~October 2026; 5 months for full pipeline experiments)
5	- Backup: AAAI 2027 (abstract July 21, paper July 28, 2026 — tight, 2 months)
6	- Backup 2: EACL 2027 via ARR August 2026 cycle (August 3, 2026)
7	
8	## Core Claims (3 条, 可证伪)
9	
10	**Claim 1 (Detection)**: DIF analysis across model release cohorts detects benchmark contamination with practical power (ETS C: TPR 0.72-0.85, FPR <0.05 at N≥80, δ≥1.4) and is robust to RL training — because it operates on group-level behavioral response patterns (correct/incorrect conditional on ability), not within-model output distributions that GRPO/PPO smoothing affects.
11	
12	**Claim 2 (Ensemble Coverage)**: A multi-signal contamination sentinel combining DIF (large effects, RL-robust), ConStat-style perturbation testing (non-RL models), and DVD generation variance (variant contamination) achieves detection coverage across the full effect-size spectrum and model-type landscape, with each signal covering the blind spots of the others.
13	
14	**Claim 3 (Regeneration)**: Bifactor IRT equating with anchor items enables psychometrically equivalent benchmark regeneration — flagged items can be replaced with empirically calibrated alternatives that preserve construct validity, difficulty, and discrimination, maintaining benchmark comparability through a formal graceful-degradation framework.
15	
16	## Story Spine
17	
18	**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say "Model B outperforms Model A on MMLU," we presume both scores reflect the same latent ability. Contamination systematically erodes this validity. Critically, RL training (GRPO/PPO) conceals contamination signals: Wang et al. (ICLR 2026) show 14-20pp AUROC degradation for all reference-free detectors after ~156 GRPO steps, reducing most to near-random (~50% AUROC). The model ecosystem is shifting toward RL-trained reasoning models (o1, o3, DeepSeek-R1), making this a growing threat.
19	
20	**Existing approaches & gaps**: LiveBench updates monthly from recent sources but applies no psychometric calibration across updates. ConStat provides FDR-controlled performance-based detection but relies on perturbation sensitivity that RL can mask. DVD detects variant contamination via generation variance but is untested against RL. Growing Pains (arXiv 2026) uses multidimensional IRT for extensible evaluation but addresses score comparability, not contamination. No existing work closes the full loop from RL-robust detection through construct-constrained generation to psychometrically equated regeneration.
21	
22	**Our framing**: Contamination is fundamentally a psychometric problem — it creates Differential Item Functioning (DIF), where contaminated items become differentially easier for exposed model cohorts beyond what general ability gains predict. DIF operates on group-level Item Characteristic Curves conditional on ability, making it orthogonal to within-model output distribution smoothing. This is the one contamination signal RL cannot conceal without negating the purpose of contamination itself: if a model memorized an item, it must answer it correctly, creating a detectable behavioral anomaly at the population level. Combined with a multi-signal ensemble for full effect-size coverage and bifactor IRT equating for calibrated item regeneration, this creates the first self-healing benchmark framework.
23	
24	**Headline result template**: "On MMLU with 5,000+ models spanning 3 years of releases, DIF-based ETS C detection achieves 73-85% TPR with <5% FPR for large contamination effects (δ≥1.4), maintaining power where 10 existing detection methods degrade to near-random under RL training (Wang et al., ICLR 2026)."
25	
26	## Venue Fit Risks
27	
28	- **ICLR**: Strong fit — evaluation methodology, robustness to RL, psychometric theory applied to ML. Risk: reviewers may not be familiar with IRT/DIF methodology. Mitigation: provide self-contained DIF tutorial in appendix, reproducible code, and connection to ML-familiar concepts (DIF ≈ "fairness testing for items").
29	- **Cross-discipline bridge**: IRT/psychometrics vocabulary needs translation for ML audience. Key mappings: "examinees" → "models", "test items" → "benchmark questions", "DIF" → "item-level contamination signal", "equating" → "score comparability across benchmark versions".
30	- **Novelty concern**: DIF itself is not new (1988). Our contribution is the novel application to LLM benchmark contamination + the RL-robustness argument + the integration with regeneration. Need to frame as "bringing mature psychometric tools to solve an urgent ML problem" rather than "inventing new statistics."
31	
32	## Anticipated Reviewer Concerns
33	
34	1. **"DIF power is only sufficient for large effects (δ≥1.4)"**
35	   - Response: Large effects are precisely what threaten benchmark validity most (GSM1K: 10-13% average accuracy drop). Small effects (δ<0.6) have minimal impact on rankings. For medium effects, the ensemble's other signals provide coverage.
36	   - Evidence needed: plan_001 (real-data validation), plan_003 (ensemble)
37	
38	2. **"Model cohort sample sizes are too small for classical DIF"**
39	   - Response: (a) ETS C uses effect-size thresholds, not p-values, reducing sample-size dependence; (b) annual cohorts now reach N=80-100; (c) Cumulative Bayesian priors accumulate power over time; (d) Item-Focused Trees treat release date as continuous covariate.
40	   - Evidence needed: plan_001 (real cohort sizes), plan_008 (Bayesian DIF, P2)
41	
42	3. **"Only validated in simulation"**
43	   - Response: plan_001 uses METABENCH real data (5,055 models). plan_004 cross-validates on GSM8K with GSM1K ground truth.
44	   - Evidence needed: plan_001, plan_004
45	
46	4. **"Item regeneration quality — how do you ensure replacements measure the same construct?"**
47	   - Response: Bifactor IRT equating with anchor items + empirical calibration via student simulation (not prompt-based difficulty targeting). Construct validity verified through factor loading analysis.
48	   - Evidence needed: plan_005, plan_006
49	
50	5. **"RL robustness is only theoretical — where's the empirical evidence?"**
51	   - Response: plan_002 directly evaluates DIF on cohorts including RL-trained models.
52	   - Evidence needed: plan_002
53	
54	6. **"Computational cost of the full pipeline"**
55	   - Response: DIF analysis is lightweight (minutes, CPU only). Main cost is one-time calibration panel. Once calibrated, ongoing monitoring is cheap.
56	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ead1b3e-64ad-4846-aa79-f94dc2221773",
  "isSidechain": false,
  "promptId": "ed003479-76af-4943-a861-980660b8c55c",
  "type": "user",
  "uuid": "a9f7d627-a3b3-4c6e-a7b2-9329a4b015c3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/paper_framing.md",
      "content": "# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: ICLR 2027 (expected deadline ~October 2026; 5 months for full pipeline experiments)\n- Backup: AAAI 2027 (abstract July 21, paper July 28, 2026 — tight, 2 months)\n- Backup 2: EACL 2027 via ARR August 2026 cycle (August 3, 2026)\n\n## Core Claims (3 条, 可证伪)\n\n**Claim 1 (Detection)**: DIF analysis across model release cohorts detects benchmark contamination with practical power (ETS C: TPR 0.72-0.85, FPR <0.05 at N≥80, δ≥1.4) and is robust to RL training — because it operates on group-level behavioral response patterns (correct/incorrect conditional on ability), not within-model output distributions that GRPO/PPO smoothing affects.\n\n**Claim 2 (Ensemble Coverage)**: A multi-signal contamination sentinel combining DIF (large effects, RL-robust), ConStat-style perturbation testing (non-RL models), and DVD generation variance (variant contamination) achieves detection coverage across the full effect-size spectrum and model-type landscape, with each signal covering the blind spots of the others.\n\n**Claim 3 (Regeneration)**: Bifactor IRT equating with anchor items enables psychometrically equivalent benchmark regeneration — flagged items can be replaced with empirically calibrated alternatives that preserve construct validity, difficulty, and discrimination, maintaining benchmark comparability through a formal graceful-degradation framework.\n\n## Story Spine\n\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent ability. Contamination systematically erodes this validity. Critically, RL training (GRPO/PPO) conceals contamination signals: Wang et al. (ICLR 2026) show 14-20pp AUROC degradation for all reference-free detectors after ~156 GRPO steps, reducing most to near-random (~50% AUROC). The model ecosystem is shifting toward RL-trained reasoning models (o1, o3, DeepSeek-R1), making this a growing threat.\n\n**Existing approaches & gaps**: LiveBench updates monthly from recent sources but applies no psychometric calibration across updates. ConStat provides FDR-controlled performance-based detection but relies on perturbation sensitivity that RL can mask. DVD detects variant contamination via generation variance but is untested against RL. Growing Pains (arXiv 2026) uses multidimensional IRT for extensible evaluation but addresses score comparability, not contamination. No existing work closes the full loop from RL-robust detection through construct-constrained generation to psychometrically equated regeneration.\n\n**Our framing**: Contamination is fundamentally a psychometric problem — it creates Differential Item Functioning (DIF), where contaminated items become differentially easier for exposed model cohorts beyond what general ability gains predict. DIF operates on group-level Item Characteristic Curves conditional on ability, making it orthogonal to within-model output distribution smoothing. This is the one contamination signal RL cannot conceal without negating the purpose of contamination itself: if a model memorized an item, it must answer it correctly, creating a detectable behavioral anomaly at the population level. Combined with a multi-signal ensemble for full effect-size coverage and bifactor IRT equating for calibrated item regeneration, this creates the first self-healing benchmark framework.\n\n**Headline result template**: \"On MMLU with 5,000+ models spanning 3 years of releases, DIF-based ETS C detection achieves 73-85% TPR with <5% FPR for large contamination effects (δ≥1.4), maintaining power where 10 existing detection methods degrade to near-random under RL training (Wang et al., ICLR 2026).\"\n\n## Venue Fit Risks\n\n- **ICLR**: Strong fit — evaluation methodology, robustness to RL, psychometric theory applied to ML. Risk: reviewers may not be familiar with IRT/DIF methodology. Mitigation: provide self-contained DIF tutorial in appendix, reproducible code, and connection to ML-familiar concepts (DIF ≈ \"fairness testing for items\").\n- **Cross-discipline bridge**: IRT/psychometrics vocabulary needs translation for ML audience. Key mappings: \"examinees\" → \"models\", \"test items\" → \"benchmark questions\", \"DIF\" → \"item-level contamination signal\", \"equating\" → \"score comparability across benchmark versions\".\n- **Novelty concern**: DIF itself is not new (1988). Our contribution is the novel application to LLM benchmark contamination + the RL-robustness argument + the integration with regeneration. Need to frame as \"bringing mature psychometric tools to solve an urgent ML problem\" rather than \"inventing new statistics.\"\n\n## Anticipated Reviewer Concerns\n\n1. **\"DIF power is only sufficient for large effects (δ≥1.4)\"**\n   - Response: Large effects are precisely what threaten benchmark validity most (GSM1K: 10-13% average accuracy drop). Small effects (δ<0.6) have minimal impact on rankings. For medium effects, the ensemble's other signals provide coverage.\n   - Evidence needed: plan_001 (real-data validation), plan_003 (ensemble)\n\n2. **\"Model cohort sample sizes are too small for classical DIF\"**\n   - Response: (a) ETS C uses effect-size thresholds, not p-values, reducing sample-size dependence; (b) annual cohorts now reach N=80-100; (c) Cumulative Bayesian priors accumulate power over time; (d) Item-Focused Trees treat release date as continuous covariate.\n   - Evidence needed: plan_001 (real cohort sizes), plan_008 (Bayesian DIF, P2)\n\n3. **\"Only validated in simulation\"**\n   - Response: plan_001 uses METABENCH real data (5,055 models). plan_004 cross-validates on GSM8K with GSM1K ground truth.\n   - Evidence needed: plan_001, plan_004\n\n4. **\"Item regeneration quality — how do you ensure replacements measure the same construct?\"**\n   - Response: Bifactor IRT equating with anchor items + empirical calibration via student simulation (not prompt-based difficulty targeting). Construct validity verified through factor loading analysis.\n   - Evidence needed: plan_005, plan_006\n\n5. **\"RL robustness is only theoretical — where's the empirical evidence?\"**\n   - Response: plan_002 directly evaluates DIF on cohorts including RL-trained models.\n   - Evidence needed: plan_002\n\n6. **\"Computational cost of the full pipeline\"**\n   - Response: DIF analysis is lightweight (minutes, CPU only). Main cost is one-time calibration panel. Once calibrated, ongoing monitoring is cheap.\n",
      "numLines": 56,
      "startLine": 1,
      "totalLines": 56
    }
  },
  "sourceToolAssistantUUID": "1ead1b3e-64ad-4846-aa79-f94dc2221773",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T194223 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_…",
  "leafUuid": "a9f7d627-a3b3-4c6e-a7b2-9329a4b015c3",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete mock research paper",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6"
}
```

---

### Assistant

_source line 14 · 2026-05-20T19:59:06.328Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me write a comprehensive LaTeX paper. I need to organize this into:

1. Abstract
2. Introduction
3. Related Work
4. Method (DIF detection, ensemble, bifactor IRT equating/regeneration)
5. Experiments (covering all 9 experiments)
6. Conclusion

Let me make sure I have all the experiments:
1. real_data_dif_mmlu - Tables 1, 2
2. rl_robustness_validation - Tables 3, 4


3. constat_perturbation_eval - Table 5
4. dvd_generation_variance_eval - Table 6
5. ensemble_fusion - Tables 7, 8
6. cross_benchmark_gsm8k - Tables 9, 10
7. bifactor_irt_equating_pilot - Tables 11, 12
8. item_generation_calibration - Tables 13, 14
9. cumulative_bayesian_dif - Table 15
10. graceful_degradation_analysis - Tables 16, 17
11. item_focused_trees - Tables 18, 19

That's 11 experiments with 19 tables total. Now I'll start writing the paper.

Writing LaTeX structure...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9f7d627-a3b3-4c6e-a7b2-9329a4b015c3",
  "isSidechain": false,
  "requestId": "req_011CbEQvAcPoAuM2wCpZQeqG",
  "type": "assistant",
  "uuid": "58b0bfee-6620-47ac-8a30-1c0b55b646ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ReQa1CpkBvSwyWMBtZ75iZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20311,
      "cache_read_input_tokens": 23172,
      "output_tokens": 480,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20311,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 480,
          "cache_read_input_tokens": 23172,
          "cache_creation_input_tokens": 20311,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20311
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-20T19:59:06.330Z_

Now I have all the data. Let me write the full LaTeX paper covering all 9 experiments with 19 tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58b0bfee-6620-47ac-8a30-1c0b55b646ff",
  "isSidechain": false,
  "requestId": "req_011CbEQvAcPoAuM2wCpZQeqG",
  "type": "assistant",
  "uuid": "b4f1cc43-2758-45d0-9abe-1dbc71a77ee0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ReQa1CpkBvSwyWMBtZ75iZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20311,
      "cache_read_input_tokens": 23172,
      "output_tokens": 480,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20311,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 480,
          "cache_read_input_tokens": 23172,
          "cache_creation_input_tokens": 20311,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20311
          },
          "type": "message"
        }
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

_source line 16 · 2026-05-20T19:59:08.750Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BVrb1mjwwbkew3hq36DsXi`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4f1cc43-2758-45d0-9abe-1dbc71a77ee0",
  "isSidechain": false,
  "requestId": "req_011CbEQvAcPoAuM2wCpZQeqG",
  "type": "assistant",
  "uuid": "a2e97e84-9324-46b6-9269-e11a21717f3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ReQa1CpkBvSwyWMBtZ75iZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20311,
      "cache_read_input_tokens": 23172,
      "output_tokens": 480,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20311,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 480,
          "cache_read_input_tokens": 23172,
          "cache_creation_input_tokens": 20311,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20311
          },
          "type": "message"
        }
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

_source line 17 · 2026-05-20T19:59:08.919Z_

<details><summary>↩ Tool result · `toolu_01BVrb1mjwwbkew3hq36DsXi`</summary>

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
  "parentUuid": "a2e97e84-9324-46b6-9269-e11a21717f3e",
  "isSidechain": false,
  "promptId": "ed003479-76af-4943-a861-980660b8c55c",
  "type": "user",
  "uuid": "1724a7e3-3519-41ee-a010-15d3e8814081",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a2e97e84-9324-46b6-9269-e11a21717f3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T20:02:49.340Z_

<details open><summary>🔧 Tool call — Write · `toolu_01QqGAEHnp8yoUTWKi6dECn3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/paper.tex",
  "content": "\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{caption}\n\n\\title{Self-Healing Benchmarks: RL-Robust Contamination Detection via Differential Item Functioning and Psychometrically Equated Benchmark Regeneration}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%======================================================================\n\\begin{abstract}\nLLM benchmark scores are only meaningful if they reflect genuine ability rather than memorization of test items.\nExisting contamination detectors rely on within-model output distributions (perplexity, token probabilities, generation variance) that reinforcement learning (RL) training smooths away---Wang et al.\\ (ICLR 2026) report 14--20 percentage-point AUROC degradation after $\\sim$156 GRPO steps, reducing most methods to near-random.\nWe reframe contamination as a psychometric phenomenon---Differential Item Functioning (DIF)---where contaminated items become differentially easier for exposed model cohorts beyond what latent ability predicts.\nBecause DIF operates on group-level behavioral patterns (correct/incorrect conditional on ability), it is orthogonal to the within-model distribution smoothing that RL performs.\nOn METABENCH MMLU (5,055 models $\\times$ 12,508 items), DIF-based ETS~C detection achieves 78--83\\% TPR at $<$5\\% FPR for large contamination effects ($\\delta \\ge 1.4$), maintaining 96\\% power retention where 10 existing methods degrade to random under RL training.\nWe further propose a multi-signal ensemble combining DIF, ConStat-style perturbation testing, and DVD generation variance that achieves 87\\% TPR across the full effect-size spectrum.\nFinally, we demonstrate that bifactor IRT equating enables psychometrically equivalent benchmark regeneration: replacing flagged items with empirically calibrated alternatives preserves model rankings ($\\rho = 0.97$) and score reliability ($\\alpha > 0.91$) at up to 20\\% replacement rate.\nTogether, these components constitute the first \\emph{self-healing benchmark} framework.\n\\end{abstract}\n\n%======================================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nWhen we say ``Model B outperforms Model A on MMLU,'' we implicitly assume temporal score comparability---that both scores reflect the same latent ability measured under equivalent conditions.\nBenchmark contamination systematically violates this assumption: models trained on benchmark items receive inflated scores that no longer reflect genuine capability.\n\nThe problem is worsening.\nThe shift toward RL-trained reasoning models (o1, o3, DeepSeek-R1) introduces a new challenge: RL training conceals contamination signals.\nWang et al.\\ (ICLR 2026) demonstrate that $\\sim$156 GRPO steps reduce 10 reference-free contamination detectors to near-random performance ($\\sim$50\\% AUROC), because policy optimization smooths the within-model output distributions these methods rely on.\nAs the model ecosystem moves toward RL, existing detection approaches face obsolescence.\n\nWe observe that contamination is fundamentally a \\emph{psychometric} problem.\nIn educational testing, when a test item functions differently for groups of examinees \\emph{after controlling for overall ability}, the item exhibits Differential Item Functioning (DIF).\nBenchmark contamination creates exactly this pattern: a model cohort trained after a benchmark leaked into training data will find contaminated items differentially easier than their latent ability predicts.\nCrucially, DIF operates on \\emph{group-level Item Characteristic Curves} conditional on ability---not on within-model token distributions.\nRL training cannot eliminate this signal without negating the purpose of contamination itself: a model that memorized an item must still answer it correctly, preserving the behavioral anomaly at the population level.\n\nThis paper makes three contributions:\n\n\\begin{enumerate}\n    \\item \\textbf{RL-Robust Detection} (\\S\\ref{sec:exp_dif}--\\ref{sec:exp_rl}): DIF-based ETS~C detection achieves 78--83\\% TPR with $<$5\\% FPR on METABENCH MMLU real data, maintaining 96\\% power retention under RL training where 10 traditional detectors degrade by 6--21 percentage points to near-random.\n\n    \\item \\textbf{Full-Spectrum Ensemble} (\\S\\ref{sec:exp_ensemble}): A multi-signal sentinel combining DIF (large effects, RL-robust), ConStat perturbation testing (non-RL medium effects), and DVD generation variance (variant contamination) achieves 87\\% TPR and 0.93 AUROC across the full effect-size and model-type landscape.\n\n    \\item \\textbf{Psychometrically Equated Regeneration} (\\S\\ref{sec:exp_equating}--\\ref{sec:exp_degradation}): Bifactor IRT equating with anchor items enables benchmark regeneration that preserves model rankings ($\\rho = 0.97$), score reliability ($\\alpha > 0.91$), and construct validity through a formal graceful-degradation framework.\n\\end{enumerate}\n\n%======================================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Contamination Detection.}\nReference-free methods detect contamination from model outputs alone.\nMin-K\\% Prob identifies memorized text via low-probability token ratios.\nPerplexity-based and compression-based methods (zlib ratio) flag suspiciously fluent outputs.\nDetectGPT uses curvature in log-probability space.\nReference-model approaches compare target model loss against a clean reference.\nThese methods share a common vulnerability: they operate on within-model output distributions that RL training smooths.\nConStat (Dekoninck et al., 2024) tests whether model performance degrades under semantically equivalent reformulations, providing FDR-controlled detection but relying on surface-form-specific memorization patterns vulnerable to RL.\nDVD (Dong et al., 2024) detects variant contamination via generation variance and bimodal response distributions.\n\n\\paragraph{Benchmark Evolution.}\nLiveBench updates monthly from recent sources but applies no psychometric calibration across updates, making temporal comparisons unreliable.\nGrowing Pains (arXiv 2026) uses multidimensional IRT for extensible evaluation but addresses score comparability across tasks, not contamination.\nNo existing work closes the full loop from RL-robust detection through construct-constrained generation to psychometrically equated regeneration.\n\n\\paragraph{Psychometrics in NLP Evaluation.}\nItem Response Theory has been applied to NLP evaluation for ability estimation and item analysis.\nBifactor models have been used in educational testing to separate general from domain-specific factors.\nDIF analysis is a standard tool in educational measurement for detecting item bias.\nOur contribution is the novel application of DIF to LLM benchmark contamination, the theoretical and empirical demonstration of its RL-robustness, and integration with bifactor equating for benchmark regeneration.\n\n%======================================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{DIF-Based Contamination Detection}\n\\label{sec:method_dif}\n\nLet $U_{ij} \\in \\{0, 1\\}$ denote the binary response of model $i$ on item $j$.\nUnder a 2PL IRT model, the probability of a correct response is:\n\\begin{equation}\n    P(U_{ij} = 1 \\mid \\theta_i) = \\frac{1}{1 + \\exp(-a_j(\\theta_i - b_j))}\n\\end{equation}\nwhere $\\theta_i$ is the latent ability of model $i$, $a_j$ is the item discrimination, and $b_j$ is the item difficulty.\n\nDIF occurs when the Item Characteristic Curve (ICC) differs between a \\emph{reference group} (e.g., models released before a benchmark was widely available) and a \\emph{focal group} (e.g., models released after):\n\\begin{equation}\n    P(U_{ij} = 1 \\mid \\theta, G = \\text{focal}) \\neq P(U_{ij} = 1 \\mid \\theta, G = \\text{ref})\n\\end{equation}\nfor some $\\theta$ values, after controlling for overall ability.\n\nWe use the ETS classification system based on the Mantel-Haenszel $\\Delta_\\text{MH}$ statistic:\n\\begin{itemize}\n    \\item \\textbf{A} (negligible): $|\\Delta_\\text{MH}| < 1.0$\n    \\item \\textbf{B} (moderate): $1.0 \\leq |\\Delta_\\text{MH}| < 1.5$\n    \\item \\textbf{C} (large): $|\\Delta_\\text{MH}| \\geq 1.5$\n\\end{itemize}\n\nItems classified as ETS~C are flagged as contaminated. This effect-size-based criterion, rather than p-value-based testing, reduces sensitivity to sample size and focuses on practically meaningful contamination.\n\n\\paragraph{Why DIF is RL-robust.}\nTraditional detectors operate on within-model output distributions (token probabilities, generation variance).\nRL training (GRPO/PPO) optimizes the policy to smooth these distributions, eliminating detectable anomalies.\nDIF, by contrast, compares \\emph{group-level behavioral patterns}: ``given the same latent ability $\\theta$, does the focal group have higher probability of answering item $j$ correctly?''\nRL can smooth output token distributions but cannot eliminate the behavioral fact that a model answers a memorized item correctly.\nThe only way to defeat DIF would be for the model to deliberately answer memorized items \\emph{incorrectly}---which negates the purpose of contamination.\n\n\\subsection{Multi-Signal Ensemble}\n\\label{sec:method_ensemble}\n\nNo single signal covers the full contamination landscape. We combine three complementary detectors:\n\n\\begin{enumerate}\n    \\item \\textbf{DIF (ETS~C)}: Strongest for large effects ($\\delta \\geq 1.4$) and RL-trained models.\n    \\item \\textbf{ConStat perturbation}: Effective for medium effects ($\\delta \\geq 0.6$) on non-RL models, where surface-form memorization creates detectable performance drops under semantic reformulation.\n    \\item \\textbf{DVD generation variance}: Targets variant contamination (partial memorization from exposure to item variants), where bimodal generation distributions emerge.\n\\end{enumerate}\n\nWe evaluate two fusion strategies: (a) \\emph{majority voting} ($\\geq$2/3 signals agree) and (b) \\emph{weighted fusion} with per-signal weights optimized on a calibration set. Weighted fusion with weights $w_\\text{DIF} = 0.45$, $w_\\text{ConStat} = 0.30$, $w_\\text{DVD} = 0.25$ allows high-confidence single-signal detections to trigger flags, avoiding the over-conservatism of majority voting in regimes where only one signal is active.\n\n\\subsection{Bifactor IRT Equating for Benchmark Regeneration}\n\\label{sec:method_equating}\n\nGiven a set of contaminated items, we regenerate the benchmark through three steps:\n\n\\paragraph{Step 1: Bifactor Model Fitting.}\nMMLU has a natural bifactor structure: a general cognitive ability factor $g$ plus subject-specific factors $s_k$ ($k = 1, \\ldots, K$). We fit a bifactor IRT model:\n\\begin{equation}\n    P(U_{ij} = 1 \\mid \\theta_{ig}, \\theta_{is_k}) = \\frac{1}{1 + \\exp(-[a_{jg}\\theta_{ig} + a_{js_k}\\theta_{is_k} - d_j])}\n\\end{equation}\nwhere $a_{jg}$ and $a_{js_k}$ are the general and specific factor loadings.\n\n\\paragraph{Step 2: Anchor Item Selection.}\nWe select DIF-free items (ETS~A classification, discrimination $a > 0.8$, low missingness) as anchor items. These provide the calibration bridge between original and regenerated benchmark versions.\n\n\\paragraph{Step 3: Fixed-Parameter Calibration.}\nReplacement items are generated via LLM and calibrated through student simulation (using a panel of diverse models as simulated examinees). Item parameters are estimated on the anchor item scale through fixed-parameter calibration, ensuring score comparability.\n\n\\subsection{Cumulative Bayesian DIF}\n\\label{sec:method_bayesian}\n\nFor medium-effect contamination ($\\delta \\approx 1.0$) where single-administration power is limited, we implement a Bayesian framework that accumulates evidence across successive model cohorts. The posterior from administration $t$ serves as the prior for administration $t+1$:\n\\begin{equation}\n    p(\\Delta_j \\mid \\mathbf{D}_{1:t}) \\propto p(\\mathbf{D}_t \\mid \\Delta_j) \\cdot p(\\Delta_j \\mid \\mathbf{D}_{1:t-1})\n\\end{equation}\nwhere $\\Delta_j$ is the DIF effect size for item $j$ and $\\mathbf{D}_{1:t}$ denotes data from all administrations up to $t$. A Bayes factor threshold of $\\text{BF} \\geq 3.0$ triggers flagging.\n\n%======================================================================\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{DIF Detection on METABENCH MMLU Real Data}\n\\label{sec:exp_dif}\n\nWe apply DIF analysis to the METABENCH MMLU response matrix comprising 5,055 models and 12,508 items. Models are split into temporal cohorts: a reference group of 3,235 pre-2024 models and a focal group of 1,820 post-2024 models. We also evaluate finer annual cohort splits.\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF Detection Power on METABENCH MMLU Real Data}\n\\label{tab:dif_mmlu}\n\\small\n\\begin{tabular}{lrrcrcc}\n\\toprule\nCohort Split & $N_\\text{focal}$ & $N_\\text{ref}$ & $\\delta$ range & TPR & FPR & AUC \\\\\n\\midrule\npre2024 vs post2024 & 1,820 & 3,235 & $\\geq 1.4$ & 0.78 & 0.038 & 0.92 \\\\\npre2024 vs post2024 & 1,820 & 3,235 & $\\geq 1.6$ & 0.83 & 0.038 & 0.94 \\\\\npre2024 vs post2024 & 1,820 & 3,235 & $\\geq 1.0$ & 0.51 & 0.041 & 0.83 \\\\\n2022 vs 2024 & 920 & 2,100 & $\\geq 1.4$ & 0.76 & 0.036 & 0.91 \\\\\n2023 vs 2025 & 680 & 1,340 & $\\geq 1.4$ & 0.74 & 0.039 & 0.90 \\\\\nAnnual (finest) & 92 & 2,100 & $\\geq 1.4$ & 0.72 & 0.042 & 0.88 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nETS~C flags 1,340 items at the C level (10.7\\% of MMLU), concentrated in STEM subjects.\nTPR ranges from 72\\% to 83\\% depending on cohort granularity and effect-size threshold, while FPR remains consistently below 5\\%.\nEven the finest annual split ($N_\\text{focal} = 92$) achieves TPR = 0.72, consistent with simulation predictions at this sample size.\nReal IRT parameters (mean $a = 1.18$, mean $b = -0.79$) closely match our simulation settings, validating ecological validity.\n\n\\paragraph{External Validation with MMLU-CF.}\nWe use MMLU-CF as partial ground truth. Among 2,780 items that MMLU-CF modified (indicating suspected contamination vulnerability), 61\\% are DIF-flagged. Among 9,728 unmodified items, only 7\\% are flagged ($\\phi = 0.42$, tetrachoric $r = 0.48$).\n\n\\begin{table}[h]\n\\centering\n\\caption{MMLU-CF External Validation}\n\\label{tab:mmlu_cf}\n\\small\n\\begin{tabular}{lrcl}\n\\toprule\nCategory & $n$ items & DIF flagged rate & Description \\\\\n\\midrule\nCF-modified items & 2,780 & 0.61 & Items changed in MMLU-CF \\\\\nCF-unmodified items & 9,728 & 0.07 & Items unchanged in MMLU-CF \\\\\n\\midrule\n$\\phi$ coefficient & --- & 0.42 & Association between DIF flag \\& CF modification \\\\\nTetrachoric $r$ & --- & 0.48 & Latent correlation estimate \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe moderate-to-strong association ($\\phi = 0.42$) reflects the partial nature of this ground truth: MMLU-CF's modification strategy does not correspond one-to-one with contamination, making perfect correlation neither expected nor credible.\n\n\\subsection{RL-Robustness Validation}\n\\label{sec:exp_rl}\n\nWe evaluate DIF alongside 10 traditional detectors on cohorts including 14 RL-trained models (DeepSeek-R1, QwQ-32B, Skywork-OR1, Eurus-2-PRIME, and others) and 40 SFT-only models.\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF vs Traditional Detectors Under RL Training}\n\\label{tab:rl_robustness}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & AUROC (SFT) & AUROC (RL) & Degradation (pp) & $p$-value \\\\\n\\midrule\nDIF (ETS~C) & 0.91 & 0.90 & 1 & 0.62 \\\\\n\\midrule\nMin-K\\% & 0.72 & 0.51 & 21 & 0.0002 \\\\\nConStat (perturbation) & 0.68 & 0.53 & 15 & 0.001 \\\\\nDVD (gen.\\ variance) & 0.65 & 0.54 & 11 & 0.004 \\\\\nPerplexity & 0.61 & 0.50 & 11 & 0.003 \\\\\nLowercase & 0.58 & 0.49 & 9 & 0.008 \\\\\nzlib ratio & 0.60 & 0.50 & 10 & 0.005 \\\\\nTop-K prob & 0.63 & 0.52 & 11 & 0.003 \\\\\nRef-model loss & 0.67 & 0.53 & 14 & 0.002 \\\\\nNeighbor text & 0.59 & 0.50 & 9 & 0.007 \\\\\nDetectGPT & 0.55 & 0.49 & 6 & 0.040 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDIF exhibits 1~pp AUROC degradation ($p = 0.62$, not significant), while traditional methods degrade by 6--21~pp to near-random performance (mean AUROC = 0.51). The power retention ratio of DIF is 0.96 ($p = 0.62$ for paired $t$-test of SFT vs RL cohort TPRs), compared to statistically significant degradation for all traditional methods ($p < 0.01$).\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF Power Retention by RL Training Intensity}\n\\label{tab:rl_intensity}\n\\small\n\\begin{tabular}{lcccr}\n\\toprule\nModel Group & $n$ & TPR ($\\delta \\geq 1.4$) & FPR & Retention \\\\\n\\midrule\nSFT only & 40 & 0.79 & 0.037 & 1.00 \\\\\nLight RL ($<$500 steps) & 6 & 0.78 & 0.039 & 0.99 \\\\\nHeavy RL ($>$500 steps) & 8 & 0.75 & 0.041 & 0.95 \\\\\nAll RL & 14 & 0.76 & 0.041 & 0.96 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEven heavy RL training ($>$500 optimization steps) reduces DIF power by only 5\\% (retention = 0.95), attributable to higher general ability compressing effect-size estimates rather than mechanistic failure.\n\n\\subsection{ConStat Perturbation Evaluation}\n\\label{sec:exp_constat}\n\nWe independently evaluate ConStat-style perturbation testing by generating 5 semantically equivalent reformulations (semantic similarity 0.91) for each of 240 MMLU items across 35 models.\n\n\\begin{table}[h]\n\\centering\n\\caption{ConStat Detection Power by Effect Size and Model Type}\n\\label{tab:constat}\n\\small\n\\begin{tabular}{llrccc}\n\\toprule\nModel Type & $\\delta$ range & $n$ items & TPR & FPR & FDR \\\\\n\\midrule\nnon-RL & $\\geq 0.6$ & 142 & 0.68 & 0.06 & 0.048 \\\\\nnon-RL & $\\geq 1.0$ & 87 & 0.74 & 0.06 & 0.041 \\\\\nnon-RL & $\\geq 1.4$ & 48 & 0.62 & 0.06 & 0.052 \\\\\nRL & $\\geq 0.6$ & 142 & 0.31 & 0.08 & 0.120 \\\\\nRL & $\\geq 1.0$ & 87 & 0.38 & 0.08 & 0.100 \\\\\nAll models & $\\geq 0.6$ & 142 & 0.52 & 0.07 & 0.070 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nConStat achieves TPR = 0.68 on non-RL models at $\\delta \\geq 0.6$, filling DIF's blind spot in the medium-effect regime.\nUnder RL training, TPR drops to 0.31, consistent with RL smoothing of surface-form memorization.\nMean accuracy drop on contaminated items is 0.18 vs 0.03 on clean items under reformulation, confirming the perturbation mechanism.\nThe inverted pattern at $\\delta \\geq 1.4$ (TPR = 0.62, lower than at $\\delta \\geq 1.0$) reflects that extremely contaminated items are often intrinsically easy, reducing the reformulation-induced accuracy drop.\n\n\\subsection{DVD Generation Variance Evaluation}\n\\label{sec:exp_dvd}\n\nWe evaluate DVD on 12 open-weight models, generating 50 responses per item at temperatures 0.7--1.0 across 2,000 MMLU items.\n\n\\begin{table}[h]\n\\centering\n\\caption{DVD Detection Power by Contamination Type}\n\\label{tab:dvd}\n\\small\n\\begin{tabular}{llrccc}\n\\toprule\nContamination Type & Model Type & $n$ items & TPR & FPR & AUROC \\\\\n\\midrule\nVariant & non-RL & 320 & 0.65 & 0.07 & 0.78 \\\\\nVerbatim & non-RL & 480 & 0.38 & 0.07 & 0.62 \\\\\nAll & non-RL & 800 & 0.52 & 0.07 & 0.71 \\\\\nVariant & RL & 320 & 0.47 & 0.09 & 0.68 \\\\\nVerbatim & RL & 480 & 0.29 & 0.09 & 0.57 \\\\\nAll & RL & 800 & 0.38 & 0.09 & 0.63 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDVD is most effective for variant contamination on non-RL models (TPR = 0.65), where partial memorization creates bimodal generation patterns (bimodal detection rate: 0.58 for contaminated vs 0.04 for clean items).\nIts lower performance on verbatim contamination (TPR = 0.38) is expected: fully memorized items produce consistently confident outputs with low generation variance, eliminating the bimodal signal.\nThis complementarity with DIF (strongest on verbatim large effects) motivates the ensemble design.\n\n\\subsection{Ensemble Fusion}\n\\label{sec:exp_ensemble}\n\nWe fuse DIF, ConStat, and DVD signals using both majority voting and weighted fusion strategies.\n\n\\begin{table}[h]\n\\centering\n\\caption{Ensemble vs Individual Signal Detection Power}\n\\label{tab:ensemble}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & TPR (full) & TPR ($\\geq$1.4) & TPR ($\\geq$0.6) & FPR & AUROC \\\\\n\\midrule\nDIF only & 0.58 & 0.78 & 0.35 & 0.038 & 0.84 \\\\\nConStat only & 0.44 & 0.62 & 0.68 & 0.060 & 0.76 \\\\\nDVD only & 0.38 & 0.38 & 0.45 & 0.070 & 0.71 \\\\\nMajority (2/3) & 0.72 & 0.81 & 0.64 & 0.040 & 0.89 \\\\\nWeighted fusion & \\textbf{0.87} & \\textbf{0.91} & \\textbf{0.78} & 0.080 & \\textbf{0.93} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWeighted fusion achieves 87\\% TPR across the full effect-size spectrum---a 29~pp improvement over the best individual signal (DIF at 0.58 full-spectrum).\nThe 15~pp advantage over majority voting reflects the systematic complementarity: in most detection regimes, only 1--2 signals are active, and the 2-of-3 agreement requirement of majority voting filters out valid single-signal detections.\n\n\\begin{table}[h]\n\\centering\n\\caption{Signal Complementarity Analysis}\n\\label{tab:complementarity}\n\\small\n\\begin{tabular}{lcl}\n\\toprule\nDetection Source & \\% of Total & Primary Regime \\\\\n\\midrule\nDIF unique & 28\\% & Large effect + RL models \\\\\nConStat unique & 15\\% & Medium effect + non-RL \\\\\nDVD unique & 12\\% & Variant contamination \\\\\nDIF $\\cap$ ConStat & 8\\% & Large effect + non-RL \\\\\nDIF $\\cap$ DVD & 4\\% & Large variant + RL \\\\\nConStat $\\cap$ DVD & 2\\% & Medium variant + non-RL \\\\\nAll three & 31\\% & Large effect + non-RL + verbatim \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEach signal contributes 12--28\\% unique detections that no other signal captures, confirming that no individual signal is dispensable.\nOn RL models, ensemble TPR reaches 0.82 (vs 0.90 on non-RL), with DIF's RL-robustness partially compensating for ConStat's RL-induced degradation.\n\n\\subsection{Cross-Benchmark Validation on GSM8K}\n\\label{sec:exp_gsm8k}\n\nTo test generalizability, we replicate DIF analysis on GSM8K (1,319 items, 62 models), using GSM1K---a distribution-matched but entirely novel test set---as independent ground truth.\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF Detection on GSM8K with GSM1K Ground Truth}\n\\label{tab:gsm8k}\n\\small\n\\begin{tabular}{lr}\n\\toprule\nMetric & Value \\\\\n\\midrule\nModels evaluated & 62 \\\\\nItems evaluated & 1,319 \\\\\nDIF-flagged items & 178 (13.5\\%) \\\\\nTPR ($\\delta \\geq 1.4$) & 0.74 \\\\\nFPR & 0.042 \\\\\nAUC & 0.88 \\\\\nGSM8K--GSM1K gap $\\times$ DIF (Spearman $\\rho$) & 0.43 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDIF achieves TPR = 0.74 on GSM8K, consistent with MMLU results accounting for smaller sample sizes (28 vs 34 models per cohort).\nThe 13.5\\% flagged rate aligns with prior reports of GSM8K contamination prevalence.\nDIF flags correlate with the GSM8K--GSM1K accuracy gap (Spearman $\\rho = 0.43$), providing convergent validation from an entirely independent ground truth source.\n\n\\begin{table}[h]\n\\centering\n\\caption{GSM8K--GSM1K Gap by Model Contamination Status}\n\\label{tab:gsm8k_gap}\n\\small\n\\begin{tabular}{lrccc}\n\\toprule\nModel Group & $n$ & Mean Gap & Std & Median Gap \\\\\n\\midrule\nDIF high contamination & 18 & 0.112 & 0.034 & 0.105 \\\\\nDIF low contamination & 22 & 0.051 & 0.028 & 0.047 \\\\\nDIF clean & 22 & 0.024 & 0.019 & 0.020 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nModels classified as high-contamination by DIF show 4.7$\\times$ larger GSM8K--GSM1K gaps than clean models (0.112 vs 0.024), with a monotonic relationship across contamination levels.\n\n\\subsection{Bifactor IRT Equating}\n\\label{sec:exp_equating}\n\nWe pilot bifactor IRT equating on METABENCH MMLU. The bifactor model captures a general factor ($g$, explaining 48\\% of variance) and 57 subject-specific factors (24\\% of variance), with good fit statistics.\n\n\\begin{table}[h]\n\\centering\n\\caption{Bifactor Model Fit Statistics}\n\\label{tab:bifactor_fit}\n\\small\n\\begin{tabular}{lr}\n\\toprule\nMetric & Value \\\\\n\\midrule\nRMSEA & 0.028 \\\\\nCFI & 0.96 \\\\\nTLI & 0.95 \\\\\nGeneral factor variance & 48\\% \\\\\nSubject factors variance & 24\\% \\\\\nTotal variance explained & 72\\% \\\\\nNumber of subject factors & 57 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe select 3,100 anchor items ($\\sim$25\\%, meeting criteria: ETS~A classification, $a > 0.8$, low missingness; DIF-free rate 92\\%, stability $\\rho = 0.98$) and calibrate 500 replacement items through fixed-parameter calibration on the anchor scale.\n\n\\begin{table}[h]\n\\centering\n\\caption{Equating Results: Original vs Replaced Benchmark}\n\\label{tab:equating}\n\\small\n\\begin{tabular}{lrl}\n\\toprule\nMetric & Value & Interpretation \\\\\n\\midrule\nSpearman $\\rho$ & 0.97 & Rankings nearly identical \\\\\nPearson $r$ & 0.96 & Scores linearly related \\\\\nRMSE & 0.021 & Minimal score displacement \\\\\nMean rank displacement & 1.8 & Average 1--2 rank positions \\\\\nMax rank displacement & 12 & Worst case within noise \\\\\nClassification agreement & 0.94 & 94\\% same performance tier \\\\\n$\\chi^2$ test $p$-value & 0.34 & Cannot reject equivalence \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe equated benchmark achieves Spearman $\\rho = 0.97$ with the original, meaning models shift an average of 1.8 rank positions.\nClassification agreement of 94\\% indicates that in practical model evaluation scenarios, the equated benchmark yields the same comparative conclusions in 94\\% of cases.\nThe $\\chi^2$ equating test ($p = 0.34$) fails to reject the null hypothesis of score equivalence.\n\n\\subsection{Item Generation and Calibration}\n\\label{sec:exp_generation}\n\nWe generate 500 replacement items via LLM and evaluate two calibration approaches: student simulation (using 8 diverse models as simulated examinees with 200 responses per item) and prompt-based difficulty targeting.\n\n\\begin{table}[h]\n\\centering\n\\caption{Calibration Method Comparison}\n\\label{tab:calibration}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Difficulty $\\rho$ & Difficulty RMSE & Discrimination $\\rho$ & $n$ items \\\\\n\\midrule\nStudent simulation & 0.78 & 0.14 & 0.62 & 420 \\\\\nPrompt targeting & 0.28 & 0.38 & 0.15 & 420 \\\\\nRandom baseline & 0.05 & 0.52 & 0.03 & 420 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nStudent simulation achieves difficulty correlation $\\rho = 0.78$---nearly $3\\times$ the precision of prompt-based targeting ($\\rho = 0.28$).\nPrompt-based methods systematically underestimate hard items and overestimate easy items, because difficulty perception diverges from generation capability.\nDiscrimination correlation ($\\rho = 0.62$) is lower, as discrimination is a second-order parameter inherently harder to control through generation.\n\n\\begin{table}[h]\n\\centering\n\\caption{Generated Item Quality Metrics}\n\\label{tab:item_quality}\n\\small\n\\begin{tabular}{lr}\n\\toprule\nMetric & Value \\\\\n\\midrule\nQuality filter pass rate & 0.84 \\\\\nSubject match accuracy & 0.92 \\\\\nCognitive level match & 0.78 \\\\\nFormat compliance & 0.97 \\\\\nFactor loading correlation & 0.85 \\\\\nHoldout equating $\\rho$ & 0.95 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFactor loading correlation of 0.85 confirms that generated items load on the same subject-specific factors, preserving bifactor structure.\nEnd-to-end holdout validation ($\\rho = 0.95$) demonstrates that the full pipeline (generation $\\to$ simulation calibration $\\to$ equating) produces functionally equivalent items.\n\n\\subsection{Cumulative Bayesian DIF}\n\\label{sec:exp_bayesian}\n\nFor medium-effect contamination where single-administration power is limited, we simulate 4 successive administrations of 40 models each and evaluate cumulative Bayesian DIF.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cumulative Bayesian DIF Power Over Administrations}\n\\label{tab:bayesian}\n\\small\n\\begin{tabular}{rrccc}\n\\toprule\nAdmin. & Cumulative $N$ & Power ($\\delta = 1.0$) & Power ($\\delta = 1.4$) & CI Width \\\\\n\\midrule\n1 & 40 & 0.38 & 0.62 & 0.68 \\\\\n2 & 80 & 0.55 & 0.76 & 0.48 \\\\\n3 & 120 & 0.70 & 0.84 & 0.37 \\\\\n4 & 160 & 0.78 & 0.88 & 0.31 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCumulative evidence accumulation doubles medium-effect power from 0.38 to 0.78 over 4 administrations, with diminishing gains per round ($\\sim\\sqrt{n}$ scaling).\nCredible interval width shrinks from 0.68 to 0.31, enabling more precise effect-size estimation.\nFDR remains controlled at 0.04 with BF threshold 3.0.\nThis supports the ``living benchmark'' paradigm: detection confidence improves over time without requiring large initial cohorts.\n\n\\subsection{Graceful Degradation Under Progressive Replacement}\n\\label{sec:exp_degradation}\n\nWe analyze benchmark validity under 5--50\\% item replacement rates, establishing a formal graceful-degradation framework.\n\n\\begin{table}[h]\n\\centering\n\\caption{Validity Metrics Under Progressive Replacement}\n\\label{tab:degradation}\n\\small\n\\begin{tabular}{rcccc}\n\\toprule\nReplacement Rate & Ranking $\\rho$ & Reliability $\\alpha$ & Construct Jaccard & Score RMSE \\\\\n\\midrule\n0\\% (original) & 1.00 & 0.94 & 1.00 & 0.000 \\\\\n5\\% & 0.99 & 0.93 & 0.98 & 0.008 \\\\\n10\\% & 0.97 & 0.93 & 0.96 & 0.015 \\\\\n20\\% & 0.95 & 0.91 & 0.92 & 0.025 \\\\\n35\\% & 0.92 & 0.89 & 0.87 & 0.038 \\\\\n50\\% & 0.89 & 0.87 & 0.83 & 0.052 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe psychometric equivalence threshold ($\\rho \\geq 0.95$) is met at up to 20\\% replacement, providing a clear operational guideline.\nGiven that MMLU has $\\sim$10.7\\% items flagged, a single regeneration round operates well within this safety margin.\nScore reliability remains excellent ($\\alpha > 0.91$) through 20\\% replacement, and construct coverage (Jaccard similarity of subject-factor coverage) exceeds 0.92.\n\n\\begin{table}[h]\n\\centering\n\\caption{Theoretical vs Empirical Bounds}\n\\label{tab:bounds}\n\\small\n\\begin{tabular}{rccc}\n\\toprule\nReplacement Rate & Theoretical $\\rho$ LB & Empirical $\\rho$ & Bound Tight? \\\\\n\\midrule\n5\\% & 0.97 & 0.99 & No \\\\\n10\\% & 0.95 & 0.97 & No \\\\\n20\\% & 0.93 & 0.95 & No \\\\\n50\\% & 0.84 & 0.89 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTheoretical lower bounds are consistently conservative (empirical $\\rho$ exceeds theoretical by 2--5~pp), providing additional safety margins for practitioners.\n\n\\subsection{Item-Focused Trees}\n\\label{sec:exp_ift}\n\nAs an alternative to categorical cohort DIF, we implement Item-Focused Trees (IFT) that treat model release date as a continuous covariate, automatically discovering per-item contamination changepoints.\n\n\\begin{table}[h]\n\\centering\n\\caption{Item-Focused Trees vs ETS~C Comparison}\n\\label{tab:ift}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & TPR ($\\geq$1.4) & TPR ($\\geq$1.0) & FPR & AUC & Time (s) \\\\\n\\midrule\nETS~C & 0.78 & 0.45 & 0.038 & 0.92 & 28 \\\\\nItem-Focused Trees & 0.81 & 0.58 & 0.044 & 0.90 & 340 \\\\\nCombined (union) & 0.84 & 0.60 & 0.048 & 0.93 & 368 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIFT achieves marginal TPR improvement (+3~pp at $\\delta \\geq 1.4$) by finding item-specific optimal splits rather than using a uniform cohort boundary.\nThe combined approach (union of ETS~C and IFT flags) reaches TPR = 0.84 at $\\delta \\geq 1.4$.\nIFT's greater advantage at $\\delta \\geq 1.0$ (+13~pp over ETS~C) reflects its ability to detect gradual contamination onset that fixed cohort boundaries miss.\n\n\\begin{table}[h]\n\\centering\n\\caption{Contamination Changepoint Analysis by Subject}\n\\label{tab:changepoint}\n\\small\n\\begin{tabular}{lrcl}\n\\toprule\nSubject Group & Items with Changepoint & Median Changepoint & Range \\\\\n\\midrule\nSTEM & 520 & 2023-03 & 2022-06 to 2024-01 \\\\\nHumanities & 210 & 2023-09 & 2023-01 to 2024-06 \\\\\nSocial Sciences & 160 & 2023-06 & 2022-09 to 2024-03 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe changepoint analysis reveals that STEM contamination onset precedes humanities by $\\sim$6 months (median: 2023-03 vs 2023-09), consistent with code-heavy training data exposing STEM items earlier.\nThis subject-specific temporal pattern is a novel finding that supports understanding contamination as a gradual, domain-dependent process.\n\n%======================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Limitations.}\nDIF requires sufficient model cohort sizes ($N \\geq 80$ for large effects); the Bayesian extension addresses this for medium effects but requires multiple administrations.\nThe ensemble's FPR (0.08) is higher than individual signals; practitioners should consider the FPR-TPR trade-off for their use case.\nItem generation quality depends on the generator model; as models improve, generated item quality should improve correspondingly, but this also raises the risk of generating items similar to existing training data.\nOur evaluation is limited to multiple-choice benchmarks (MMLU, GSM8K); extension to open-ended evaluation requires adapted DIF methodology.\n\n\\paragraph{Broader Impact.}\nSelf-healing benchmarks enable continued meaningful evaluation of LLMs despite pervasive contamination.\nBy publishing the detection and regeneration methodology, we aim to shift the incentive structure: if contamination is reliably detectable and correctable, the returns to training on benchmark data diminish.\nHowever, publishing detection methodology also enables adversarial adaptation; we argue that the psychometric foundation of DIF (requiring deliberate performance suppression to evade) provides a more durable defense than distribution-based methods.\n\n%======================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented a self-healing benchmark framework comprising three components: (1) DIF-based contamination detection that maintains 78--83\\% TPR with $<$5\\% FPR and 96\\% power retention under RL training, where 10 existing methods degrade to near-random; (2) a multi-signal ensemble achieving 87\\% TPR across the full effect-size spectrum; and (3) bifactor IRT equating enabling psychometrically equivalent benchmark regeneration ($\\rho = 0.97$, $\\alpha > 0.91$) at up to 20\\% item replacement.\nCross-benchmark validation on GSM8K with GSM1K ground truth confirms generalizability.\nCumulative Bayesian DIF and Item-Focused Trees extend detection to medium effects and continuous temporal modeling.\nTogether, these results establish that LLM benchmarks can be maintained as living instruments that detect, diagnose, and heal contamination while preserving psychometric validity.\n\n\\bibliographystyle{plainnat}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1724a7e3-3519-41ee-a010-15d3e8814081",
  "isSidechain": false,
  "requestId": "req_011CbEQw6baP2qWFvyKtc2cd",
  "type": "assistant",
  "uuid": "03c5ebbc-dd34-483e-ad04-81d4f724ae10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DWwTTjFKMVNnWDHRsdV7fS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 508,
      "cache_read_input_tokens": 43483,
      "output_tokens": 11625,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 508,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11625,
          "cache_read_input_tokens": 43483,
          "cache_creation_input_tokens": 508,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 508
          },
          "type": "message"
        }
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

_source line 19 · 2026-05-20T20:02:49.375Z_

<details><summary>↩ Tool result · `toolu_01QqGAEHnp8yoUTWKi6dECn3`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03c5ebbc-dd34-483e-ad04-81d4f724ae10",
  "isSidechain": false,
  "promptId": "ed003479-76af-4943-a861-980660b8c55c",
  "type": "user",
  "uuid": "489c2501-4a18-418b-b45e-806c6b238a46",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/paper.tex",
    "content": "\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{caption}\n\n\\title{Self-Healing Benchmarks: RL-Robust Contamination Detection via Differential Item Functioning and Psychometrically Equated Benchmark Regeneration}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%======================================================================\n\\begin{abstract}\nLLM benchmark scores are only meaningful if they reflect genuine ability rather than memorization of test items.\nExisting contamination detectors rely on within-model output distributions (perplexity, token probabilities, generation variance) that reinforcement learning (RL) training smooths away---Wang et al.\\ (ICLR 2026) report 14--20 percentage-point AUROC degradation after $\\sim$156 GRPO steps, reducing most methods to near-random.\nWe reframe contamination as a psychometric phenomenon---Differential Item Functioning (DIF)---where contaminated items become differentially easier for exposed model cohorts beyond what latent ability predicts.\nBecause DIF operates on group-level behavioral patterns (correct/incorrect conditional on ability), it is orthogonal to the within-model distribution smoothing that RL performs.\nOn METABENCH MMLU (5,055 models $\\times$ 12,508 items), DIF-based ETS~C detection achieves 78--83\\% TPR at $<$5\\% FPR for large contamination effects ($\\delta \\ge 1.4$), maintaining 96\\% power retention where 10 existing methods degrade to random under RL training.\nWe further propose a multi-signal ensemble combining DIF, ConStat-style perturbation testing, and DVD generation variance that achieves 87\\% TPR across the full effect-size spectrum.\nFinally, we demonstrate that bifactor IRT equating enables psychometrically equivalent benchmark regeneration: replacing flagged items with empirically calibrated alternatives preserves model rankings ($\\rho = 0.97$) and score reliability ($\\alpha > 0.91$) at up to 20\\% replacement rate.\nTogether, these components constitute the first \\emph{self-healing benchmark} framework.\n\\end{abstract}\n\n%======================================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nWhen we say ``Model B outperforms Model A on MMLU,'' we implicitly assume temporal score comparability---that both scores reflect the same latent ability measured under equivalent conditions.\nBenchmark contamination systematically violates this assumption: models trained on benchmark items receive inflated scores that no longer reflect genuine capability.\n\nThe problem is worsening.\nThe shift toward RL-trained reasoning models (o1, o3, DeepSeek-R1) introduces a new challenge: RL training conceals contamination signals.\nWang et al.\\ (ICLR 2026) demonstrate that $\\sim$156 GRPO steps reduce 10 reference-free contamination detectors to near-random performance ($\\sim$50\\% AUROC), because policy optimization smooths the within-model output distributions these methods rely on.\nAs the model ecosystem moves toward RL, existing detection approaches face obsolescence.\n\nWe observe that contamination is fundamentally a \\emph{psychometric} problem.\nIn educational testing, when a test item functions differently for groups of examinees \\emph{after controlling for overall ability}, the item exhibits Differential Item Functioning (DIF).\nBenchmark contamination creates exactly this pattern: a model cohort trained after a benchmark leaked into training data will find contaminated items differentially easier than their latent ability predicts.\nCrucially, DIF operates on \\emph{group-level Item Characteristic Curves} conditional on ability---not on within-model token distributions.\nRL training cannot eliminate this signal without negating the purpose of contamination itself: a model that memorized an item must still answer it correctly, preserving the behavioral anomaly at the population level.\n\nThis paper makes three contributions:\n\n\\begin{enumerate}\n    \\item \\textbf{RL-Robust Detection} (\\S\\ref{sec:exp_dif}--\\ref{sec:exp_rl}): DIF-based ETS~C detection achieves 78--83\\% TPR with $<$5\\% FPR on METABENCH MMLU real data, maintaining 96\\% power retention under RL training where 10 traditional detectors degrade by 6--21 percentage points to near-random.\n\n    \\item \\textbf{Full-Spectrum Ensemble} (\\S\\ref{sec:exp_ensemble}): A multi-signal sentinel combining DIF (large effects, RL-robust), ConStat perturbation testing (non-RL medium effects), and DVD generation variance (variant contamination) achieves 87\\% TPR and 0.93 AUROC across the full effect-size and model-type landscape.\n\n    \\item \\textbf{Psychometrically Equated Regeneration} (\\S\\ref{sec:exp_equating}--\\ref{sec:exp_degradation}): Bifactor IRT equating with anchor items enables benchmark regeneration that preserves model rankings ($\\rho = 0.97$), score reliability ($\\alpha > 0.91$), and construct validity through a formal graceful-degradation framework.\n\\end{enumerate}\n\n%======================================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Contamination Detection.}\nReference-free methods detect contamination from model outputs alone.\nMin-K\\% Prob identifies memorized text via low-probability token ratios.\nPerplexity-based and compression-based methods (zlib ratio) flag suspiciously fluent outputs.\nDetectGPT uses curvature in log-probability space.\nReference-model approaches compare target model loss against a clean reference.\nThese methods share a common vulnerability: they operate on within-model output distributions that RL training smooths.\nConStat (Dekoninck et al., 2024) tests whether model performance degrades under semantically equivalent reformulations, providing FDR-controlled detection but relying on surface-form-specific memorization patterns vulnerable to RL.\nDVD (Dong et al., 2024) detects variant contamination via generation variance and bimodal response distributions.\n\n\\paragraph{Benchmark Evolution.}\nLiveBench updates monthly from recent sources but applies no psychometric calibration across updates, making temporal comparisons unreliable.\nGrowing Pains (arXiv 2026) uses multidimensional IRT for extensible evaluation but addresses score comparability across tasks, not contamination.\nNo existing work closes the full loop from RL-robust detection through construct-constrained generation to psychometrically equated regeneration.\n\n\\paragraph{Psychometrics in NLP Evaluation.}\nItem Response Theory has been applied to NLP evaluation for ability estimation and item analysis.\nBifactor models have been used in educational testing to separate general from domain-specific factors.\nDIF analysis is a standard tool in educational measurement for detecting item bias.\nOur contribution is the novel application of DIF to LLM benchmark contamination, the theoretical and empirical demonstration of its RL-robustness, and integration with bifactor equating for benchmark regeneration.\n\n%======================================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{DIF-Based Contamination Detection}\n\\label{sec:method_dif}\n\nLet $U_{ij} \\in \\{0, 1\\}$ denote the binary response of model $i$ on item $j$.\nUnder a 2PL IRT model, the probability of a correct response is:\n\\begin{equation}\n    P(U_{ij} = 1 \\mid \\theta_i) = \\frac{1}{1 + \\exp(-a_j(\\theta_i - b_j))}\n\\end{equation}\nwhere $\\theta_i$ is the latent ability of model $i$, $a_j$ is the item discrimination, and $b_j$ is the item difficulty.\n\nDIF occurs when the Item Characteristic Curve (ICC) differs between a \\emph{reference group} (e.g., models released before a benchmark was widely available) and a \\emph{focal group} (e.g., models released after):\n\\begin{equation}\n    P(U_{ij} = 1 \\mid \\theta, G = \\text{focal}) \\neq P(U_{ij} = 1 \\mid \\theta, G = \\text{ref})\n\\end{equation}\nfor some $\\theta$ values, after controlling for overall ability.\n\nWe use the ETS classification system based on the Mantel-Haenszel $\\Delta_\\text{MH}$ statistic:\n\\begin{itemize}\n    \\item \\textbf{A} (negligible): $|\\Delta_\\text{MH}| < 1.0$\n    \\item \\textbf{B} (moderate): $1.0 \\leq |\\Delta_\\text{MH}| < 1.5$\n    \\item \\textbf{C} (large): $|\\Delta_\\text{MH}| \\geq 1.5$\n\\end{itemize}\n\nItems classified as ETS~C are flagged as contaminated. This effect-size-based criterion, rather than p-value-based testing, reduces sensitivity to sample size and focuses on practically meaningful contamination.\n\n\\paragraph{Why DIF is RL-robust.}\nTraditional detectors operate on within-model output distributions (token probabilities, generation variance).\nRL training (GRPO/PPO) optimizes the policy to smooth these distributions, eliminating detectable anomalies.\nDIF, by contrast, compares \\emph{group-level behavioral patterns}: ``given the same latent ability $\\theta$, does the focal group have higher probability of answering item $j$ correctly?''\nRL can smooth output token distributions but cannot eliminate the behavioral fact that a model answers a memorized item correctly.\nThe only way to defeat DIF would be for the model to deliberately answer memorized items \\emph{incorrectly}---which negates the purpose of contamination.\n\n\\subsection{Multi-Signal Ensemble}\n\\label{sec:method_ensemble}\n\nNo single signal covers the full contamination landscape. We combine three complementary detectors:\n\n\\begin{enumerate}\n    \\item \\textbf{DIF (ETS~C)}: Strongest for large effects ($\\delta \\geq 1.4$) and RL-trained models.\n    \\item \\textbf{ConStat perturbation}: Effective for medium effects ($\\delta \\geq 0.6$) on non-RL models, where surface-form memorization creates detectable performance drops under semantic reformulation.\n    \\item \\textbf{DVD generation variance}: Targets variant contamination (partial memorization from exposure to item variants), where bimodal generation distributions emerge.\n\\end{enumerate}\n\nWe evaluate two fusion strategies: (a) \\emph{majority voting} ($\\geq$2/3 signals agree) and (b) \\emph{weighted fusion} with per-signal weights optimized on a calibration set. Weighted fusion with weights $w_\\text{DIF} = 0.45$, $w_\\text{ConStat} = 0.30$, $w_\\text{DVD} = 0.25$ allows high-confidence single-signal detections to trigger flags, avoiding the over-conservatism of majority voting in regimes where only one signal is active.\n\n\\subsection{Bifactor IRT Equating for Benchmark Regeneration}\n\\label{sec:method_equating}\n\nGiven a set of contaminated items, we regenerate the benchmark through three steps:\n\n\\paragraph{Step 1: Bifactor Model Fitting.}\nMMLU has a natural bifactor structure: a general cognitive ability factor $g$ plus subject-specific factors $s_k$ ($k = 1, \\ldots, K$). We fit a bifactor IRT model:\n\\begin{equation}\n    P(U_{ij} = 1 \\mid \\theta_{ig}, \\theta_{is_k}) = \\frac{1}{1 + \\exp(-[a_{jg}\\theta_{ig} + a_{js_k}\\theta_{is_k} - d_j])}\n\\end{equation}\nwhere $a_{jg}$ and $a_{js_k}$ are the general and specific factor loadings.\n\n\\paragraph{Step 2: Anchor Item Selection.}\nWe select DIF-free items (ETS~A classification, discrimination $a > 0.8$, low missingness) as anchor items. These provide the calibration bridge between original and regenerated benchmark versions.\n\n\\paragraph{Step 3: Fixed-Parameter Calibration.}\nReplacement items are generated via LLM and calibrated through student simulation (using a panel of diverse models as simulated examinees). Item parameters are estimated on the anchor item scale through fixed-parameter calibration, ensuring score comparability.\n\n\\subsection{Cumulative Bayesian DIF}\n\\label{sec:method_bayesian}\n\nFor medium-effect contamination ($\\delta \\approx 1.0$) where single-administration power is limited, we implement a Bayesian framework that accumulates evidence across successive model cohorts. The posterior from administration $t$ serves as the prior for administration $t+1$:\n\\begin{equation}\n    p(\\Delta_j \\mid \\mathbf{D}_{1:t}) \\propto p(\\mathbf{D}_t \\mid \\Delta_j) \\cdot p(\\Delta_j \\mid \\mathbf{D}_{1:t-1})\n\\end{equation}\nwhere $\\Delta_j$ is the DIF effect size for item $j$ and $\\mathbf{D}_{1:t}$ denotes data from all administrations up to $t$. A Bayes factor threshold of $\\text{BF} \\geq 3.0$ triggers flagging.\n\n%======================================================================\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{DIF Detection on METABENCH MMLU Real Data}\n\\label{sec:exp_dif}\n\nWe apply DIF analysis to the METABENCH MMLU response matrix comprising 5,055 models and 12,508 items. Models are split into temporal cohorts: a reference group of 3,235 pre-2024 models and a focal group of 1,820 post-2024 models. We also evaluate finer annual cohort splits.\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF Detection Power on METABENCH MMLU Real Data}\n\\label{tab:dif_mmlu}\n\\small\n\\begin{tabular}{lrrcrcc}\n\\toprule\nCohort Split & $N_\\text{focal}$ & $N_\\text{ref}$ & $\\delta$ range & TPR & FPR & AUC \\\\\n\\midrule\npre2024 vs post2024 & 1,820 & 3,235 & $\\geq 1.4$ & 0.78 & 0.038 & 0.92 \\\\\npre2024 vs post2024 & 1,820 & 3,235 & $\\geq 1.6$ & 0.83 & 0.038 & 0.94 \\\\\npre2024 vs post2024 & 1,820 & 3,235 & $\\geq 1.0$ & 0.51 & 0.041 & 0.83 \\\\\n2022 vs 2024 & 920 & 2,100 & $\\geq 1.4$ & 0.76 & 0.036 & 0.91 \\\\\n2023 vs 2025 & 680 & 1,340 & $\\geq 1.4$ & 0.74 & 0.039 & 0.90 \\\\\nAnnual (finest) & 92 & 2,100 & $\\geq 1.4$ & 0.72 & 0.042 & 0.88 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nETS~C flags 1,340 items at the C level (10.7\\% of MMLU), concentrated in STEM subjects.\nTPR ranges from 72\\% to 83\\% depending on cohort granularity and effect-size threshold, while FPR remains consistently below 5\\%.\nEven the finest annual split ($N_\\text{focal} = 92$) achieves TPR = 0.72, consistent with simulation predictions at this sample size.\nReal IRT parameters (mean $a = 1.18$, mean $b = -0.79$) closely match our simulation settings, validating ecological validity.\n\n\\paragraph{External Validation with MMLU-CF.}\nWe use MMLU-CF as partial ground truth. Among 2,780 items that MMLU-CF modified (indicating suspected contamination vulnerability), 61\\% are DIF-flagged. Among 9,728 unmodified items, only 7\\% are flagged ($\\phi = 0.42$, tetrachoric $r = 0.48$).\n\n\\begin{table}[h]\n\\centering\n\\caption{MMLU-CF External Validation}\n\\label{tab:mmlu_cf}\n\\small\n\\begin{tabular}{lrcl}\n\\toprule\nCategory & $n$ items & DIF flagged rate & Description \\\\\n\\midrule\nCF-modified items & 2,780 & 0.61 & Items changed in MMLU-CF \\\\\nCF-unmodified items & 9,728 & 0.07 & Items unchanged in MMLU-CF \\\\\n\\midrule\n$\\phi$ coefficient & --- & 0.42 & Association between DIF flag \\& CF modification \\\\\nTetrachoric $r$ & --- & 0.48 & Latent correlation estimate \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe moderate-to-strong association ($\\phi = 0.42$) reflects the partial nature of this ground truth: MMLU-CF's modification strategy does not correspond one-to-one with contamination, making perfect correlation neither expected nor credible.\n\n\\subsection{RL-Robustness Validation}\n\\label{sec:exp_rl}\n\nWe evaluate DIF alongside 10 traditional detectors on cohorts including 14 RL-trained models (DeepSeek-R1, QwQ-32B, Skywork-OR1, Eurus-2-PRIME, and others) and 40 SFT-only models.\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF vs Traditional Detectors Under RL Training}\n\\label{tab:rl_robustness}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & AUROC (SFT) & AUROC (RL) & Degradation (pp) & $p$-value \\\\\n\\midrule\nDIF (ETS~C) & 0.91 & 0.90 & 1 & 0.62 \\\\\n\\midrule\nMin-K\\% & 0.72 & 0.51 & 21 & 0.0002 \\\\\nConStat (perturbation) & 0.68 & 0.53 & 15 & 0.001 \\\\\nDVD (gen.\\ variance) & 0.65 & 0.54 & 11 & 0.004 \\\\\nPerplexity & 0.61 & 0.50 & 11 & 0.003 \\\\\nLowercase & 0.58 & 0.49 & 9 & 0.008 \\\\\nzlib ratio & 0.60 & 0.50 & 10 & 0.005 \\\\\nTop-K prob & 0.63 & 0.52 & 11 & 0.003 \\\\\nRef-model loss & 0.67 & 0.53 & 14 & 0.002 \\\\\nNeighbor text & 0.59 & 0.50 & 9 & 0.007 \\\\\nDetectGPT & 0.55 & 0.49 & 6 & 0.040 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDIF exhibits 1~pp AUROC degradation ($p = 0.62$, not significant), while traditional methods degrade by 6--21~pp to near-random performance (mean AUROC = 0.51). The power retention ratio of DIF is 0.96 ($p = 0.62$ for paired $t$-test of SFT vs RL cohort TPRs), compared to statistically significant degradation for all traditional methods ($p < 0.01$).\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF Power Retention by RL Training Intensity}\n\\label{tab:rl_intensity}\n\\small\n\\begin{tabular}{lcccr}\n\\toprule\nModel Group & $n$ & TPR ($\\delta \\geq 1.4$) & FPR & Retention \\\\\n\\midrule\nSFT only & 40 & 0.79 & 0.037 & 1.00 \\\\\nLight RL ($<$500 steps) & 6 & 0.78 & 0.039 & 0.99 \\\\\nHeavy RL ($>$500 steps) & 8 & 0.75 & 0.041 & 0.95 \\\\\nAll RL & 14 & 0.76 & 0.041 & 0.96 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEven heavy RL training ($>$500 optimization steps) reduces DIF power by only 5\\% (retention = 0.95), attributable to higher general ability compressing effect-size estimates rather than mechanistic failure.\n\n\\subsection{ConStat Perturbation Evaluation}\n\\label{sec:exp_constat}\n\nWe independently evaluate ConStat-style perturbation testing by generating 5 semantically equivalent reformulations (semantic similarity 0.91) for each of 240 MMLU items across 35 models.\n\n\\begin{table}[h]\n\\centering\n\\caption{ConStat Detection Power by Effect Size and Model Type}\n\\label{tab:constat}\n\\small\n\\begin{tabular}{llrccc}\n\\toprule\nModel Type & $\\delta$ range & $n$ items & TPR & FPR & FDR \\\\\n\\midrule\nnon-RL & $\\geq 0.6$ & 142 & 0.68 & 0.06 & 0.048 \\\\\nnon-RL & $\\geq 1.0$ & 87 & 0.74 & 0.06 & 0.041 \\\\\nnon-RL & $\\geq 1.4$ & 48 & 0.62 & 0.06 & 0.052 \\\\\nRL & $\\geq 0.6$ & 142 & 0.31 & 0.08 & 0.120 \\\\\nRL & $\\geq 1.0$ & 87 & 0.38 & 0.08 & 0.100 \\\\\nAll models & $\\geq 0.6$ & 142 & 0.52 & 0.07 & 0.070 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nConStat achieves TPR = 0.68 on non-RL models at $\\delta \\geq 0.6$, filling DIF's blind spot in the medium-effect regime.\nUnder RL training, TPR drops to 0.31, consistent with RL smoothing of surface-form memorization.\nMean accuracy drop on contaminated items is 0.18 vs 0.03 on clean items under reformulation, confirming the perturbation mechanism.\nThe inverted pattern at $\\delta \\geq 1.4$ (TPR = 0.62, lower than at $\\delta \\geq 1.0$) reflects that extremely contaminated items are often intrinsically easy, reducing the reformulation-induced accuracy drop.\n\n\\subsection{DVD Generation Variance Evaluation}\n\\label{sec:exp_dvd}\n\nWe evaluate DVD on 12 open-weight models, generating 50 responses per item at temperatures 0.7--1.0 across 2,000 MMLU items.\n\n\\begin{table}[h]\n\\centering\n\\caption{DVD Detection Power by Contamination Type}\n\\label{tab:dvd}\n\\small\n\\begin{tabular}{llrccc}\n\\toprule\nContamination Type & Model Type & $n$ items & TPR & FPR & AUROC \\\\\n\\midrule\nVariant & non-RL & 320 & 0.65 & 0.07 & 0.78 \\\\\nVerbatim & non-RL & 480 & 0.38 & 0.07 & 0.62 \\\\\nAll & non-RL & 800 & 0.52 & 0.07 & 0.71 \\\\\nVariant & RL & 320 & 0.47 & 0.09 & 0.68 \\\\\nVerbatim & RL & 480 & 0.29 & 0.09 & 0.57 \\\\\nAll & RL & 800 & 0.38 & 0.09 & 0.63 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDVD is most effective for variant contamination on non-RL models (TPR = 0.65), where partial memorization creates bimodal generation patterns (bimodal detection rate: 0.58 for contaminated vs 0.04 for clean items).\nIts lower performance on verbatim contamination (TPR = 0.38) is expected: fully memorized items produce consistently confident outputs with low generation variance, eliminating the bimodal signal.\nThis complementarity with DIF (strongest on verbatim large effects) motivates the ensemble design.\n\n\\subsection{Ensemble Fusion}\n\\label{sec:exp_ensemble}\n\nWe fuse DIF, ConStat, and DVD signals using both majority voting and weighted fusion strategies.\n\n\\begin{table}[h]\n\\centering\n\\caption{Ensemble vs Individual Signal Detection Power}\n\\label{tab:ensemble}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & TPR (full) & TPR ($\\geq$1.4) & TPR ($\\geq$0.6) & FPR & AUROC \\\\\n\\midrule\nDIF only & 0.58 & 0.78 & 0.35 & 0.038 & 0.84 \\\\\nConStat only & 0.44 & 0.62 & 0.68 & 0.060 & 0.76 \\\\\nDVD only & 0.38 & 0.38 & 0.45 & 0.070 & 0.71 \\\\\nMajority (2/3) & 0.72 & 0.81 & 0.64 & 0.040 & 0.89 \\\\\nWeighted fusion & \\textbf{0.87} & \\textbf{0.91} & \\textbf{0.78} & 0.080 & \\textbf{0.93} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWeighted fusion achieves 87\\% TPR across the full effect-size spectrum---a 29~pp improvement over the best individual signal (DIF at 0.58 full-spectrum).\nThe 15~pp advantage over majority voting reflects the systematic complementarity: in most detection regimes, only 1--2 signals are active, and the 2-of-3 agreement requirement of majority voting filters out valid single-signal detections.\n\n\\begin{table}[h]\n\\centering\n\\caption{Signal Complementarity Analysis}\n\\label{tab:complementarity}\n\\small\n\\begin{tabular}{lcl}\n\\toprule\nDetection Source & \\% of Total & Primary Regime \\\\\n\\midrule\nDIF unique & 28\\% & Large effect + RL models \\\\\nConStat unique & 15\\% & Medium effect + non-RL \\\\\nDVD unique & 12\\% & Variant contamination \\\\\nDIF $\\cap$ ConStat & 8\\% & Large effect + non-RL \\\\\nDIF $\\cap$ DVD & 4\\% & Large variant + RL \\\\\nConStat $\\cap$ DVD & 2\\% & Medium variant + non-RL \\\\\nAll three & 31\\% & Large effect + non-RL + verbatim \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEach signal contributes 12--28\\% unique detections that no other signal captures, confirming that no individual signal is dispensable.\nOn RL models, ensemble TPR reaches 0.82 (vs 0.90 on non-RL), with DIF's RL-robustness partially compensating for ConStat's RL-induced degradation.\n\n\\subsection{Cross-Benchmark Validation on GSM8K}\n\\label{sec:exp_gsm8k}\n\nTo test generalizability, we replicate DIF analysis on GSM8K (1,319 items, 62 models), using GSM1K---a distribution-matched but entirely novel test set---as independent ground truth.\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF Detection on GSM8K with GSM1K Ground Truth}\n\\label{tab:gsm8k}\n\\small\n\\begin{tabular}{lr}\n\\toprule\nMetric & Value \\\\\n\\midrule\nModels evaluated & 62 \\\\\nItems evaluated & 1,319 \\\\\nDIF-flagged items & 178 (13.5\\%) \\\\\nTPR ($\\delta \\geq 1.4$) & 0.74 \\\\\nFPR & 0.042 \\\\\nAUC & 0.88 \\\\\nGSM8K--GSM1K gap $\\times$ DIF (Spearman $\\rho$) & 0.43 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDIF achieves TPR = 0.74 on GSM8K, consistent with MMLU results accounting for smaller sample sizes (28 vs 34 models per cohort).\nThe 13.5\\% flagged rate aligns with prior reports of GSM8K contamination prevalence.\nDIF flags correlate with the GSM8K--GSM1K accuracy gap (Spearman $\\rho = 0.43$), providing convergent validation from an entirely independent ground truth source.\n\n\\begin{table}[h]\n\\centering\n\\caption{GSM8K--GSM1K Gap by Model Contamination Status}\n\\label{tab:gsm8k_gap}\n\\small\n\\begin{tabular}{lrccc}\n\\toprule\nModel Group & $n$ & Mean Gap & Std & Median Gap \\\\\n\\midrule\nDIF high contamination & 18 & 0.112 & 0.034 & 0.105 \\\\\nDIF low contamination & 22 & 0.051 & 0.028 & 0.047 \\\\\nDIF clean & 22 & 0.024 & 0.019 & 0.020 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nModels classified as high-contamination by DIF show 4.7$\\times$ larger GSM8K--GSM1K gaps than clean models (0.112 vs 0.024), with a monotonic relationship across contamination levels.\n\n\\subsection{Bifactor IRT Equating}\n\\label{sec:exp_equating}\n\nWe pilot bifactor IRT equating on METABENCH MMLU. The bifactor model captures a general factor ($g$, explaining 48\\% of variance) and 57 subject-specific factors (24\\% of variance), with good fit statistics.\n\n\\begin{table}[h]\n\\centering\n\\caption{Bifactor Model Fit Statistics}\n\\label{tab:bifactor_fit}\n\\small\n\\begin{tabular}{lr}\n\\toprule\nMetric & Value \\\\\n\\midrule\nRMSEA & 0.028 \\\\\nCFI & 0.96 \\\\\nTLI & 0.95 \\\\\nGeneral factor variance & 48\\% \\\\\nSubject factors variance & 24\\% \\\\\nTotal variance explained & 72\\% \\\\\nNumber of subject factors & 57 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe select 3,100 anchor items ($\\sim$25\\%, meeting criteria: ETS~A classification, $a > 0.8$, low missingness; DIF-free rate 92\\%, stability $\\rho = 0.98$) and calibrate 500 replacement items through fixed-parameter calibration on the anchor scale.\n\n\\begin{table}[h]\n\\centering\n\\caption{Equating Results: Original vs Replaced Benchmark}\n\\label{tab:equating}\n\\small\n\\begin{tabular}{lrl}\n\\toprule\nMetric & Value & Interpretation \\\\\n\\midrule\nSpearman $\\rho$ & 0.97 & Rankings nearly identical \\\\\nPearson $r$ & 0.96 & Scores linearly related \\\\\nRMSE & 0.021 & Minimal score displacement \\\\\nMean rank displacement & 1.8 & Average 1--2 rank positions \\\\\nMax rank displacement & 12 & Worst case within noise \\\\\nClassification agreement & 0.94 & 94\\% same performance tier \\\\\n$\\chi^2$ test $p$-value & 0.34 & Cannot reject equivalence \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe equated benchmark achieves Spearman $\\rho = 0.97$ with the original, meaning models shift an average of 1.8 rank positions.\nClassification agreement of 94\\% indicates that in practical model evaluation scenarios, the equated benchmark yields the same comparative conclusions in 94\\% of cases.\nThe $\\chi^2$ equating test ($p = 0.34$) fails to reject the null hypothesis of score equivalence.\n\n\\subsection{Item Generation and Calibration}\n\\label{sec:exp_generation}\n\nWe generate 500 replacement items via LLM and evaluate two calibration approaches: student simulation (using 8 diverse models as simulated examinees with 200 responses per item) and prompt-based difficulty targeting.\n\n\\begin{table}[h]\n\\centering\n\\caption{Calibration Method Comparison}\n\\label{tab:calibration}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Difficulty $\\rho$ & Difficulty RMSE & Discrimination $\\rho$ & $n$ items \\\\\n\\midrule\nStudent simulation & 0.78 & 0.14 & 0.62 & 420 \\\\\nPrompt targeting & 0.28 & 0.38 & 0.15 & 420 \\\\\nRandom baseline & 0.05 & 0.52 & 0.03 & 420 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nStudent simulation achieves difficulty correlation $\\rho = 0.78$---nearly $3\\times$ the precision of prompt-based targeting ($\\rho = 0.28$).\nPrompt-based methods systematically underestimate hard items and overestimate easy items, because difficulty perception diverges from generation capability.\nDiscrimination correlation ($\\rho = 0.62$) is lower, as discrimination is a second-order parameter inherently harder to control through generation.\n\n\\begin{table}[h]\n\\centering\n\\caption{Generated Item Quality Metrics}\n\\label{tab:item_quality}\n\\small\n\\begin{tabular}{lr}\n\\toprule\nMetric & Value \\\\\n\\midrule\nQuality filter pass rate & 0.84 \\\\\nSubject match accuracy & 0.92 \\\\\nCognitive level match & 0.78 \\\\\nFormat compliance & 0.97 \\\\\nFactor loading correlation & 0.85 \\\\\nHoldout equating $\\rho$ & 0.95 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFactor loading correlation of 0.85 confirms that generated items load on the same subject-specific factors, preserving bifactor structure.\nEnd-to-end holdout validation ($\\rho = 0.95$) demonstrates that the full pipeline (generation $\\to$ simulation calibration $\\to$ equating) produces functionally equivalent items.\n\n\\subsection{Cumulative Bayesian DIF}\n\\label{sec:exp_bayesian}\n\nFor medium-effect contamination where single-administration power is limited, we simulate 4 successive administrations of 40 models each and evaluate cumulative Bayesian DIF.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cumulative Bayesian DIF Power Over Administrations}\n\\label{tab:bayesian}\n\\small\n\\begin{tabular}{rrccc}\n\\toprule\nAdmin. & Cumulative $N$ & Power ($\\delta = 1.0$) & Power ($\\delta = 1.4$) & CI Width \\\\\n\\midrule\n1 & 40 & 0.38 & 0.62 & 0.68 \\\\\n2 & 80 & 0.55 & 0.76 & 0.48 \\\\\n3 & 120 & 0.70 & 0.84 & 0.37 \\\\\n4 & 160 & 0.78 & 0.88 & 0.31 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCumulative evidence accumulation doubles medium-effect power from 0.38 to 0.78 over 4 administrations, with diminishing gains per round ($\\sim\\sqrt{n}$ scaling).\nCredible interval width shrinks from 0.68 to 0.31, enabling more precise effect-size estimation.\nFDR remains controlled at 0.04 with BF threshold 3.0.\nThis supports the ``living benchmark'' paradigm: detection confidence improves over time without requiring large initial cohorts.\n\n\\subsection{Graceful Degradation Under Progressive Replacement}\n\\label{sec:exp_degradation}\n\nWe analyze benchmark validity under 5--50\\% item replacement rates, establishing a formal graceful-degradation framework.\n\n\\begin{table}[h]\n\\centering\n\\caption{Validity Metrics Under Progressive Replacement}\n\\label{tab:degradation}\n\\small\n\\begin{tabular}{rcccc}\n\\toprule\nReplacement Rate & Ranking $\\rho$ & Reliability $\\alpha$ & Construct Jaccard & Score RMSE \\\\\n\\midrule\n0\\% (original) & 1.00 & 0.94 & 1.00 & 0.000 \\\\\n5\\% & 0.99 & 0.93 & 0.98 & 0.008 \\\\\n10\\% & 0.97 & 0.93 & 0.96 & 0.015 \\\\\n20\\% & 0.95 & 0.91 & 0.92 & 0.025 \\\\\n35\\% & 0.92 & 0.89 & 0.87 & 0.038 \\\\\n50\\% & 0.89 & 0.87 & 0.83 & 0.052 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe psychometric equivalence threshold ($\\rho \\geq 0.95$) is met at up to 20\\% replacement, providing a clear operational guideline.\nGiven that MMLU has $\\sim$10.7\\% items flagged, a single regeneration round operates well within this safety margin.\nScore reliability remains excellent ($\\alpha > 0.91$) through 20\\% replacement, and construct coverage (Jaccard similarity of subject-factor coverage) exceeds 0.92.\n\n\\begin{table}[h]\n\\centering\n\\caption{Theoretical vs Empirical Bounds}\n\\label{tab:bounds}\n\\small\n\\begin{tabular}{rccc}\n\\toprule\nReplacement Rate & Theoretical $\\rho$ LB & Empirical $\\rho$ & Bound Tight? \\\\\n\\midrule\n5\\% & 0.97 & 0.99 & No \\\\\n10\\% & 0.95 & 0.97 & No \\\\\n20\\% & 0.93 & 0.95 & No \\\\\n50\\% & 0.84 & 0.89 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTheoretical lower bounds are consistently conservative (empirical $\\rho$ exceeds theoretical by 2--5~pp), providing additional safety margins for practitioners.\n\n\\subsection{Item-Focused Trees}\n\\label{sec:exp_ift}\n\nAs an alternative to categorical cohort DIF, we implement Item-Focused Trees (IFT) that treat model release date as a continuous covariate, automatically discovering per-item contamination changepoints.\n\n\\begin{table}[h]\n\\centering\n\\caption{Item-Focused Trees vs ETS~C Comparison}\n\\label{tab:ift}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & TPR ($\\geq$1.4) & TPR ($\\geq$1.0) & FPR & AUC & Time (s) \\\\\n\\midrule\nETS~C & 0.78 & 0.45 & 0.038 & 0.92 & 28 \\\\\nItem-Focused Trees & 0.81 & 0.58 & 0.044 & 0.90 & 340 \\\\\nCombined (union) & 0.84 & 0.60 & 0.048 & 0.93 & 368 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIFT achieves marginal TPR improvement (+3~pp at $\\delta \\geq 1.4$) by finding item-specific optimal splits rather than using a uniform cohort boundary.\nThe combined approach (union of ETS~C and IFT flags) reaches TPR = 0.84 at $\\delta \\geq 1.4$.\nIFT's greater advantage at $\\delta \\geq 1.0$ (+13~pp over ETS~C) reflects its ability to detect gradual contamination onset that fixed cohort boundaries miss.\n\n\\begin{table}[h]\n\\centering\n\\caption{Contamination Changepoint Analysis by Subject}\n\\label{tab:changepoint}\n\\small\n\\begin{tabular}{lrcl}\n\\toprule\nSubject Group & Items with Changepoint & Median Changepoint & Range \\\\\n\\midrule\nSTEM & 520 & 2023-03 & 2022-06 to 2024-01 \\\\\nHumanities & 210 & 2023-09 & 2023-01 to 2024-06 \\\\\nSocial Sciences & 160 & 2023-06 & 2022-09 to 2024-03 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe changepoint analysis reveals that STEM contamination onset precedes humanities by $\\sim$6 months (median: 2023-03 vs 2023-09), consistent with code-heavy training data exposing STEM items earlier.\nThis subject-specific temporal pattern is a novel finding that supports understanding contamination as a gradual, domain-dependent process.\n\n%======================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Limitations.}\nDIF requires sufficient model cohort sizes ($N \\geq 80$ for large effects); the Bayesian extension addresses this for medium effects but requires multiple administrations.\nThe ensemble's FPR (0.08) is higher than individual signals; practitioners should consider the FPR-TPR trade-off for their use case.\nItem generation quality depends on the generator model; as models improve, generated item quality should improve correspondingly, but this also raises the risk of generating items similar to existing training data.\nOur evaluation is limited to multiple-choice benchmarks (MMLU, GSM8K); extension to open-ended evaluation requires adapted DIF methodology.\n\n\\paragraph{Broader Impact.}\nSelf-healing benchmarks enable continued meaningful evaluation of LLMs despite pervasive contamination.\nBy publishing the detection and regeneration methodology, we aim to shift the incentive structure: if contamination is reliably detectable and correctable, the returns to training on benchmark data diminish.\nHowever, publishing detection methodology also enables adversarial adaptation; we argue that the psychometric foundation of DIF (requiring deliberate performance suppression to evade) provides a more durable defense than distribution-based methods.\n\n%======================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented a self-healing benchmark framework comprising three components: (1) DIF-based contamination detection that maintains 78--83\\% TPR with $<$5\\% FPR and 96\\% power retention under RL training, where 10 existing methods degrade to near-random; (2) a multi-signal ensemble achieving 87\\% TPR across the full effect-size spectrum; and (3) bifactor IRT equating enabling psychometrically equivalent benchmark regeneration ($\\rho = 0.97$, $\\alpha > 0.91$) at up to 20\\% item replacement.\nCross-benchmark validation on GSM8K with GSM1K ground truth confirms generalizability.\nCumulative Bayesian DIF and Item-Focused Trees extend detection to medium effects and continuous temporal modeling.\nTogether, these results establish that LLM benchmarks can be maintained as living instruments that detect, diagnose, and heal contamination while preserving psychometric validity.\n\n\\bibliographystyle{plainnat}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "03c5ebbc-dd34-483e-ad04-81d4f724ae10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T194223 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_…",
  "leafUuid": "489c2501-4a18-418b-b45e-806c6b238a46",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete mock research paper",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6"
}
```

---

### Tool call

_source line 22 · 2026-05-20T20:02:53.364Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UsQTJau8LQTsrvnYh93Upe`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "489c2501-4a18-418b-b45e-806c6b238a46",
  "isSidechain": false,
  "requestId": "req_011CbERDMGZqy4QxLpqnB7PN",
  "type": "assistant",
  "uuid": "de194ee3-f9cf-46f3-ae16-41e3bdf2f61a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5RbSua5w3XS4JRixD6gyg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11695,
      "cache_read_input_tokens": 43991,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11695,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 149,
          "cache_read_input_tokens": 43991,
          "cache_creation_input_tokens": 11695,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11695
          },
          "type": "message"
        }
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

_source line 23 · 2026-05-20T20:02:55.087Z_

<details><summary>↩ Tool result · `toolu_01UsQTJau8LQTsrvnYh93Upe`</summary>

```text
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
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
Overfull \hbox (7.04921pt too wide) in paragraph at lines 39--41
\OT1/cmr/m/n/10 When we say ``Model B out-per-forms Model A on MMLU,'' we im-pl
ic-itly as-sume tem-po-ral score comparability---

LaTeX Warning: Reference `sec:exp_dif' on page 1 undefined on input line 56.


LaTeX Warning: Reference `sec:exp_rl' on page 1 undefined on input line 56.


LaTeX Warning: Reference `sec:exp_ensemble' on page 1 undefined on input line 5
8.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

LaTeX Warning: Reference `sec:exp_equating' on page 2 undefined on input line 6
0.


LaTeX Warning: Reference `sec:exp_degradation' on page 2 undefined on input lin
e 60.

[2] [3]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[4]

LaTeX Warning: `h' float specifier changed to `ht'.

[5]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[6]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[7]

LaTeX Warning: `h' float specifier changed to `ht'.


Overfull \hbox (6.94037pt too wide) in paragraph at lines 552--553
\OT1/cmr/m/n/10 We an-a-lyze bench-mark va-lid-ity un-der 5--50% item re-place-
ment rates, es-tab-lish-ing a for-mal graceful-degradation

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[8]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[9] [10] [11] (./paper.aux)
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 tcrm1000
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input tcrm1000
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm1000.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymb.mf
 Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf
 Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [27] [29])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txgen.mf
 Ok [100] [109] [98] [99] [108])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymbol.mf
 Ok [13] [18] [21] [22] [23] [24] [25] [26] [28] [31] [32] [36] [39] [44]
[45] [46] [42] [47] [60] [61] [62] [77] [79] [87] [110] [91] [93] [94] [95]
[96] [126] [127] [128] [129] [130] [131] [132] [133] [134] [135] [136] [137]
[138] [139] [140] [141] [142] [143] [144] [145] [146] [147] [148] [149]
[150] [151] [152] [153] [154] [155] [156] [157] [158] [159] [160] [161]
[162] [163] [164] [165] [166] [167] [168] [169] [171] [172] [173] [174]
[175] [177] [176] [180] [181] [182] [183] [184] [187] [191] [214] [246])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txromod.mf
 Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrsuper.mf
 Ok [185] [178] [179] [170] [186])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrfract.mf
 Ok [188] [189] [190]) ) ) )
(some charht values had to be adjusted by as much as 0.06943pt)
Font metrics written on tcrm1000.tfm.
Output written on tcrm1000.600gf (128 characters, 23548 bytes).
Transcript written on tcrm1000.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk: successfully generated.


LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
mi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mti9.pfb>
Output written on paper.pdf (11 pages, 270101 bytes).
Transcript written on paper.log.
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
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
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
Overfull \hbox (7.04921pt too wide) in paragraph at lines 39--41
\OT1/cmr/m/n/10 When we say ``Model B out-per-forms Model A on MMLU,'' we im-pl
ic-itly as-sume tem-po-ral score comparability---
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2] [3]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[4]

LaTeX Warning: `h' float specifier changed to `ht'.

[5]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[6]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[7]

LaTeX Warning: `h' float specifier changed to `ht'.


Overfull \hbox (6.94037pt too wide) in paragraph at lines 552--553
\OT1/cmr/m/n/10 We an-a-lyze bench-mark va-lid-ity un-der 5--50% item re-place-
ment rates, es-tab-lish-ing a for-mal graceful-degradation

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[8]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[9] [10] [11] (./paper.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
mi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mti9.pfb>
Output written on paper.pdf (11 pages, 271721 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de194ee3-f9cf-46f3-ae16-41e3bdf2f61a",
  "isSidechain": false,
  "promptId": "ed003479-76af-4943-a861-980660b8c55c",
  "type": "user",
  "uuid": "f097a090-47e3-4ddd-9200-1d5b06b83a20",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (7.04921pt too wide) in paragraph at lines 39--41\n\\OT1/cmr/m/n/10 When we say ``Model B out-per-forms Model A on MMLU,'' we im-pl\nic-itly as-sume tem-po-ral score comparability---\n\nLaTeX Warning: Reference `sec:exp_dif' on page 1 undefined on input line 56.\n\n\nLaTeX Warning: Reference `sec:exp_rl' on page 1 undefined on input line 56.\n\n\nLaTeX Warning: Reference `sec:exp_ensemble' on page 1 undefined on input line 5\n8.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nLaTeX Warning: Reference `sec:exp_equating' on page 2 undefined on input line 6\n0.\n\n\nLaTeX Warning: Reference `sec:exp_degradation' on page 2 undefined on input lin\ne 60.\n\n[2] [3]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[4]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[5]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[6]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[7]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nOverfull \\hbox (6.94037pt too wide) in paragraph at lines 552--553\n\\OT1/cmr/m/n/10 We an-a-lyze bench-mark va-lid-ity un-der 5--50% item re-place-\nment rates, es-tab-lish-ing a for-mal graceful-degradation\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[8]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[9] [10] [11] (./paper.aux)\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 tcrm1000\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input tcrm1000\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm1000.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymb.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [27] [29])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txgen.mf\n Ok [100] [109] [98] [99] [108])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymbol.mf\n Ok [13] [18] [21] [22] [23] [24] [25] [26] [28] [31] [32] [36] [39] [44]\n[45] [46] [42] [47] [60] [61] [62] [77] [79] [87] [110] [91] [93] [94] [95]\n[96] [126] [127] [128] [129] [130] [131] [132] [133] [134] [135] [136] [137]\n[138] [139] [140] [141] [142] [143] [144] [145] [146] [147] [148] [149]\n[150] [151] [152] [153] [154] [155] [156] [157] [158] [159] [160] [161]\n[162] [163] [164] [165] [166] [167] [168] [169] [171] [172] [173] [174]\n[175] [177] [176] [180] [181] [182] [183] [184] [187] [191] [214] [246])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txromod.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrsuper.mf\n Ok [185] [178] [179] [170] [186])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrfract.mf\n Ok [188] [189] [190]) ) ) )\n(some charht values had to be adjusted by as much as 0.06943pt)\nFont metrics written on tcrm1000.tfm.\nOutput written on tcrm1000.600gf (128 characters, 23548 bytes).\nTranscript written on tcrm1000.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk: successfully generated.\n\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmti9.pfb>\nOutput written on paper.pdf (11 pages, 270101 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (7.04921pt too wide) in paragraph at lines 39--41\n\\OT1/cmr/m/n/10 When we say ``Model B out-per-forms Model A on MMLU,'' we im-pl\nic-itly as-sume tem-po-ral score comparability---\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2] [3]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[4]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[5]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[6]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[7]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nOverfull \\hbox (6.94037pt too wide) in paragraph at lines 552--553\n\\OT1/cmr/m/n/10 We an-a-lyze bench-mark va-lid-ity un-der 5--50% item re-place-\nment rates, es-tab-lish-ing a for-mal graceful-degradation\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[8]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[9] [10] [11] (./paper.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmti9.pfb>\nOutput written on paper.pdf (11 pages, 271721 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "de194ee3-f9cf-46f3-ae16-41e3bdf2f61a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T194223 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_…",
  "leafUuid": "f097a090-47e3-4ddd-9200-1d5b06b83a20",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete mock research paper",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6"
}
```

---

### Assistant

_source line 26 · 2026-05-20T20:03:00.352Z_

编译成功，无错误。PDF 生成 11 页，包含全部 19 张表格，覆盖所有 9 个实验。产出路径：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/paper.pdf`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f097a090-47e3-4ddd-9200-1d5b06b83a20",
  "isSidechain": false,
  "requestId": "req_011CbERDmcHys4hDpS6aAm8D",
  "type": "assistant",
  "uuid": "70f1903b-fd07-4d18-b84e-218f140a47a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018pVL7V5kvmAqLN4ko9DcS6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7660,
      "cache_read_input_tokens": 55686,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7660,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 105,
          "cache_read_input_tokens": 55686,
          "cache_creation_input_tokens": 7660,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7660
          },
          "type": "message"
        }
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T194223 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_…",
  "leafUuid": "70f1903b-fd07-4d18-b84e-218f140a47a9",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete mock research paper",
  "sessionId": "4cdb7bff-0186-4287-af6d-80c2435b1cc6"
}
```

---
