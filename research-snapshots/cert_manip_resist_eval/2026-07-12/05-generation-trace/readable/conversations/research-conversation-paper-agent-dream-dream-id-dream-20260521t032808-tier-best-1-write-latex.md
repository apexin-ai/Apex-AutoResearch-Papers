# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032808 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/8a7b9e13-ea8b-4f7a-8439-83707f107d4b.jsonl`
- **Structured JSON:** [`3a6a35c7b7d3e78a4fc4.json`](../../sessions/3a/3a6a35c7b7d3e78a4fc4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T04:03:55.123Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T04:03:55.123Z",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032808 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：CaCLR 是正面方法贡献——β > 0 的 MMD consistency loss 在 probe logits 空间成功\n对齐 correctness subspace，使零标签跨语言校准成为可能。Pareto frontier 在两种\n架构上均 robust：Qwen3-235B 呈强负相关 (ρ ≈ -0.65)，Llama 4 Scout 呈弱但一致\n的负相关 (ρ ≈ -0.33)。CKA partial correlation 控制 depth 后仍显著 (r ≈ 0.42,\np < 0.01)，支撑 geometric analysis framing。四个 claims 均以强形式提出，论文\n以 method + discovery 双重贡献投稿。\nHeadline: \"CaCLR enables zero-label cross-lingual calibration, reducing non-English\nECE by 22% vs temperature scaling across 20 languages on two architectures.\"\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T04:03:55.127Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T04:03:55.127Z",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b"
}
```

---

## Round 1

33 recorded events

### User

_source line 3 · 2026-05-21T04:03:55.157Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032808 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：CaCLR 是正面方法贡献——β > 0 的 MMD consistency loss 在 probe logits 空间成功
对齐 correctness subspace，使零标签跨语言校准成为可能。Pareto frontier 在两种
架构上均 robust：Qwen3-235B 呈强负相关 (ρ ≈ -0.65)，Llama 4 Scout 呈弱但一致
的负相关 (ρ ≈ -0.33)。CKA partial correlation 控制 depth 后仍显著 (r ≈ 0.42,
p < 0.01)，支撑 geometric analysis framing。四个 claims 均以强形式提出，论文
以 method + discovery 双重贡献投稿。
Headline: "CaCLR enables zero-label cross-lingual calibration, reducing non-English
ECE by 22% vs temperature scaling across 20 languages on two architectures."

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "21625223-a819-4abc-b0c5-9519cc481936",
  "type": "user",
  "uuid": "7d21e0c6-0d37-42ac-bb36-46201b59952a",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T04:03:55.156Z_

```json
{
  "parentUuid": "7d21e0c6-0d37-42ac-bb36-46201b59952a",
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
  "uuid": "733098a8-a0ff-4c10-bacd-7b390494dcf3",
  "timestamp": "2026-05-21T04:03:55.156Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T04:03:55.156Z_

```json
{
  "parentUuid": "733098a8-a0ff-4c10-bacd-7b390494dcf3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "82c5740b-fe2b-4f50-97df-f12d5ca569c1",
  "timestamp": "2026-05-21T04:03:55.156Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
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
  "aiTitle": "Generate CaCLR cross-lingual calibration paper",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b"
}
```

---

### Assistant

_source line 7 · 2026-05-21T04:03:58.223Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82c5740b-fe2b-4f50-97df-f12d5ca569c1",
  "isSidechain": false,
  "requestId": "req_011CbF3uAr4csE3wnQQTQsZ2",
  "type": "assistant",
  "uuid": "b2500ff5-d857-4d0a-a049-52db6d9020a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R7CPrwZ5MujbXKzkjVcJzg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11573,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11573,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11573,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11573
          },
          "type": "message"
        }
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

_source line 8 · 2026-05-21T04:03:59.240Z_

<details open><summary>🔧 Tool call — Read · `toolu_014YFstUWjCoyxmj14sWTjia`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2500ff5-d857-4d0a-a049-52db6d9020a8",
  "isSidechain": false,
  "requestId": "req_011CbF3uAr4csE3wnQQTQsZ2",
  "type": "assistant",
  "uuid": "756292b5-6d1e-43ab-be2b-84d00c5b66c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R7CPrwZ5MujbXKzkjVcJzg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11573,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11573,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11573,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11573
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-21T04:03:59.521Z_

<details><summary>↩ Tool result · `toolu_014YFstUWjCoyxmj14sWTjia`</summary>

```text
1	[
2	  {
3	    "name": "Qwen3-235B Full Pareto Frontier",
4	    "description": "94层 MoE (INT4), 24 probed layers (每4层), 20语言, 4 transfer conditions (CaCLR 在 plan_003)",
5	    "results": {
6	      "en_best_auroc": 0.832,
7	      "en_best_layer": 72,
8	      "en_auroc_range": [
9	        0.548,
10	        0.832
11	      ],
12	      "en_best_ece_raw": 0.126,
13	      "zs_transfer_auroc_avg_20lang": 0.713,
14	      "zs_transfer_success_rate": 0.95,
15	      "zs_fail_langs": [
16	        "am"
17	      ],
18	      "pareto_spearman_rho_global": -0.65,
19	      "pareto_spearman_rho_per_lang_range": [
20	        -0.82,
21	        -0.41
22	      ],
23	      "zs_auroc_by_tier": {
24	        "HIGH_avg": 0.773,
25	        "MID_avg": 0.719,
26	        "LOW_avg": 0.635
27	      },
28	      "zs_best_by_lang": {
29	        "zh": {
30	          "auroc": 0.79,
31	          "best_layer": 56
32	        },
33	        "es": {
34	          "auroc": 0.78,
35	          "best_layer": 60
36	        },
37	        "fr": {
38	          "auroc": 0.77,
39	          "best_layer": 56
40	        },
41	        "de": {
42	          "auroc": 0.77,
43	          "best_layer": 60
44	        },
45	        "ja": {
46	          "auroc": 0.75,
47	          "best_layer": 52
48	        },
49	        "pt": {
50	          "auroc": 0.78,
51	          "best_layer": 56
52	        },
53	        "it": {
54	          "auroc": 0.77,
55	          "best_layer": 60
56	        },
57	        "hi": {
58	          "auroc": 0.73,
59	          "best_layer": 48
60	        },
61	        "ru": {
62	          "auroc": 0.74,
63	          "best_layer": 52
64	        },
65	        "ko": {
66	          "auroc": 0.73,
67	          "best_layer": 52
68	        },
69	        "tr": {
70	          "auroc": 0.7,
71	          "best_layer": 44
72	        },
73	        "vi": {
74	          "auroc": 0.71,
75	          "best_layer": 48
76	        },
77	        "ar": {
78	          "auroc": 0.72,
79	          "best_layer": 52
80	        },
81	        "th": {
82	          "auroc": 0.7,
83	          "best_layer": 44
84	        },
85	        "sw": {
86	          "auroc": 0.65,
87	          "best_layer": 40
88	        },
89	        "bn": {
90	          "auroc": 0.66,
91	          "best_layer": 44
92	        },
93	        "yo": {
94	          "auroc": 0.61,
95	          "best_layer": 36
96	        },
97	        "te": {
98	          "auroc": 0.66,
99	          "best_layer": 44
100	        },
101	        "my": {
102	          "auroc": 0.63,
103	          "best_layer": 36
104	        },
105	        "am": {
106	          "auroc": 0.598,
107	          "best_layer": 36
108	        }
109	      },
110	      "depth_transfer_snapshot": {
111	        "en_at_L72": 0.832,
112	        "zs_avg_at_L72": 0.672,
113	        "en_at_L56": 0.812,
114	        "zs_avg_at_L56": 0.728,
115	        "en_at_L40": 0.762,
116	        "zs_avg_at_L40": 0.706
117	      },
118	      "mean_shift_delta_auroc": 0.0,
119	      "linear_proj_50_delta_auroc_avg": 0.062,
120	      "fewshot_25_auroc_avg": 0.738,
121	      "fewshot_100_auroc_avg": 0.768,
122	      "bootstrap_ci_width_auroc": 0.018
123	    },
124	    "tables": [
125	      {
126	        "name": "Table 1: Qwen3-235B Pareto Frontier — Per-Language Summary",
127	        "columns": [
128	          "Language",
129	          "Family",
130	          "Resource",
131	          "Best_ZS_AUROC",
132	          "Best_ZS_Layer",
133	          "EN_AUROC_at_Same_Layer",
134	          "Spearman_rho",
135	          "rho_p"
136	        ],
137	        "representative_rows": [
138	          [
139	            "zh",
140	            "Sinitic",
141	            "HIGH",
142	            0.79,
143	            "L56",
144	            0.812,
145	            -0.58,
146	            0.003
147	          ],
148	          [
149	            "es",
150	            "Romance",
151	            "HIGH",
152	            0.78,
153	            "L60",
154	            0.821,
155	            -0.53,
156	            0.008
157	          ],
158	          [
159	            "ja",
160	            "Japonic",
161	            "HIGH",
162	            0.75,
163	            "L52",
164	            0.802,
165	            -0.62,
166	            0.001
167	          ],
168	          [
169	            "hi",
170	            "Indo-Aryan",
171	            "MID",
172	            0.73,
173	            "L48",
174	            0.789,
175	            -0.67,
176	            "<0.001"
177	          ],
178	          [
179	            "ko",
180	            "Koreanic",
181	            "MID",
182	            0.73,
183	            "L52",
184	            0.802,
185	            -0.61,
186	            0.002
187	          ],
188	          [
189	            "ar",
190	            "Semitic",
191	            "MID",
192	            0.72,
193	            "L52",
194	            0.802,
195	            -0.59,
196	            0.003
197	          ],
198	          [
199	            "sw",
200	            "Bantu",
201	            "LOW",
202	            0.65,
203	            "L40",
204	            0.762,
205	            -0.79,
206	            "<0.001"
207	          ],
208	          [
209	            "yo",
210	            "Volta-Niger",
211	            "LOW",
212	            0.61,
213	            "L36",
214	            0.721,
215	            -0.82,
216	            "<0.001"
217	          ],
218	          [
219	            "am",
220	            "Ethiosemitic",
221	            "LOW",
222	            0.598,
223	            "L36",
224	            0.721,
225	            -0.81,
226	            "<0.001"
227	          ]
228	        ]
229	      },
230	      {
231	        "name": "Table 2: Transfer Conditions Comparison (Qwen3-235B, L56 Pareto Zone)",
232	        "columns": [
233	          "Condition",
234	          "AUROC_Avg_20L",
235	          "AUROC_HIGH",
236	          "AUROC_MID",
237	          "AUROC_LOW",
238	          "ECE_Avg"
239	        ],
240	        "rows": [
241	          [
242	            "Zero-shot",
243	            0.728,
244	            0.773,
245	            0.726,
246	            0.648,
247	            0.165
248	          ],
249	          [
250	            "Mean-shift",
251	            0.728,
252	            0.773,
253	            0.726,
254	            0.648,
255	            0.168
256	          ],
257	          [
258	            "Linear_proj_50",
259	            0.79,
260	            0.821,
261	            0.789,
262	            0.728,
263	            0.139
264	          ],
265	          [
266	            "Few-shot_25",
267	            0.745,
268	            0.789,
269	            0.742,
270	            0.668,
271	            0.152
272	          ],
273	          [
274	            "Few-shot_100",
275	            0.774,
276	            0.811,
277	            0.773,
278	            0.702,
279	            0.136
280	          ]
281	        ]
282	      }
283	    ],
284	    "figures": [],
285	    "analysis": "Qwen3-235B 呈现教科书级 Pareto frontier。关键发现：(1) ρ=-0.65 远强于 MVP\n7B 的约 -0.4，confirming 更大模型 → 更 structured representations → 更清晰\ntradeoff；(2) transfer-optimal zone 在 40-60% depth (L36-L56)，EN-optimal 在\n77% (L72)，gap = 16 层；(3) resource tier gradient: HIGH 0.77 > MID 0.72 > LOW\n0.64，三级分明；(4) 19/20 languages transfer 成功，仅 am 失败。Linear proj\n(50 pairs) 是最强迁移方法 (+6.2pp over ZS)，few-shot 100 紧随 (+4.6pp)。\n\n\n235B MoE 拥有远比 7B 更结构化的内部表征。MVP Qwen2.5-7B EN best AUROC = 0.754;\n235B 的 correctness direction 在中高层 (L48-L72) 线性可分度大幅提升至 0.83，\n与 probing 文献中 \"larger model → more linearly accessible features\" 的规律一致。\n更大模型的多语言预训练数据量级增加约 5-10x，跨语言对齐更强，zero-shot transfer\navg 从 MVP ~0.65 提升至 ~0.71。94 层结构提供精细 depth 分辨率：EN-optimal L72\n(77% depth) 与 transfer-optimal zone L52-56 (55-60% depth) 间有 ~16 层间距，\n产生清晰的强负相关 ρ ≈ -0.65。低资源语言的 ρ 更负 (sw -0.79, yo -0.82)，\n因为这些语言在深层的表征特化最剧烈——模型的 language-specific expert routing\n在深层对高资源语言保持跨语言共享，但对低资源语言已切换至 language-specific pathway。\nMean-shift AUROC delta 严格为零 (数学证明: StandardScaler + LR → 常数偏移 → rank\n不变 → AUROC 不变)。仅 am (Amharic) 以 0.598 未达 0.60 阈值，因为 Qwen3 的\nAmharic 预训练数据极少。\n"
286	  },
287	  {
288	    "name": "Llama 4 Scout Full Pareto Frontier",
289	    "description": "48层 MoE (W4A16), 12 probed layers, 20语言, 4 transfer conditions",
290	    "results": {
291	      "en_best_auroc": 0.811,
292	      "en_best_layer": 40,
293	      "en_auroc_range": [
294	        0.574,
295	        0.811
296	      ],
297	      "en_best_ece_raw": 0.139,
298	      "zs_transfer_auroc_avg_20lang": 0.684,
299	      "zs_transfer_success_rate": 0.85,
300	      "zs_fail_langs": [
301	        "yo",
302	        "my",
303	        "am"
304	      ],
305	      "pareto_spearman_rho_global": -0.33,
306	      "pareto_spearman_rho_per_lang_range": [
307	        -0.68,
308	        0.18
309	      ],
310	      "zs_auroc_by_tier": {
311	        "HIGH_avg": 0.743,
312	        "MID_avg": 0.694,
313	        "LOW_avg": 0.602
314	      },
315	      "zs_best_by_lang": {
316	        "zh": {
317	          "auroc": 0.76,
318	          "best_layer": 36
319	        },
320	        "es": {
321	          "auroc": 0.75,
322	          "best_layer": 36
323	        },
324	        "fr": {
325	          "auroc": 0.74,
326	          "best_layer": 32
327	        },
328	        "de": {
329	          "auroc": 0.74,
330	          "best_layer": 36
331	        },
332	        "ja": {
333	          "auroc": 0.72,
334	          "best_layer": 32
335	        },
336	        "pt": {
337	          "auroc": 0.75,
338	          "best_layer": 36
339	        },
340	        "it": {
341	          "auroc": 0.74,
342	          "best_layer": 36
343	        },
344	        "hi": {
345	          "auroc": 0.7,
346	          "best_layer": 36
347	        },
348	        "ru": {
349	          "auroc": 0.72,
350	          "best_layer": 40
351	        },
352	        "ko": {
353	          "auroc": 0.71,
354	          "best_layer": 40
355	        },
356	        "tr": {
357	          "auroc": 0.67,
358	          "best_layer": 32
359	        },
360	        "vi": {
361	          "auroc": 0.69,
362	          "best_layer": 32
363	        },
364	        "ar": {
365	          "auroc": 0.7,
366	          "best_layer": 40
367	        },
368	        "th": {
369	          "auroc": 0.67,
370	          "best_layer": 28
371	        },
372	        "sw": {
373	          "auroc": 0.62,
374	          "best_layer": 28
375	        },
376	        "bn": {
377	          "auroc": 0.63,
378	          "best_layer": 28
379	        },
380	        "yo": {
381	          "auroc": 0.57,
382	          "best_layer": 24
383	        },
384	        "te": {
385	          "auroc": 0.64,
386	          "best_layer": 28
387	        },
388	        "my": {
389	          "auroc": 0.58,
390	          "best_layer": 24
391	        },
392	        "am": {
393	          "auroc": 0.57,
394	          "best_layer": 24
395	        }
396	      },
397	      "depth_transfer_snapshot": {
398	        "en_at_L40": 0.811,
399	        "zs_avg_at_L40": 0.654,
400	        "en_at_L32": 0.781,
401	        "zs_avg_at_L32": 0.691,
402	        "en_at_L24": 0.732,
403	        "zs_avg_at_L24": 0.682
404	      },
405	      "langs_with_positive_depth_rho": [
406	        "ru",
407	        "ko",
408	        "ar"
409	      ],
410	      "mean_shift_delta_auroc": 0.0,
411	      "linear_proj_50_delta_auroc_avg": 0.058,
412	      "fewshot_25_auroc_avg": 0.706,
413	      "fewshot_100_auroc_avg": 0.741
414	    },
415	    "tables": [
416	      {
417	        "name": "Table 3: Llama 4 Scout Pareto Frontier — Per-Language Summary",
418	        "columns": [
419	          "Language",
420	          "Family",
421	          "Resource",
422	          "Best_ZS_AUROC",
423	          "Best_ZS_Layer",
424	          "Spearman_rho",
425	          "rho_p"
426	        ],
427	        "representative_rows": [
428	          [
429	            "zh",
430	            "Sinitic",
431	            "HIGH",
432	            0.76,
433	            "L36",
434	            -0.45,
435	            0.14
436	          ],
437	          [
438	            "es",
439	            "Romance",
440	            "HIGH",
441	            0.75,
442	            "L36",
443	            -0.41,
444	            0.18
445	          ],
446	          [
447	            "ru",
448	            "Slavic",
449	            "MID",
450	            0.72,
451	            "L40",
452	            0.05,
453	            0.88
454	          ],
455	          [
456	            "ko",
457	            "Koreanic",
458	            "MID",
459	            0.71,
460	            "L40",
461	            0.18,
462	            0.57
463	          ],
464	          [
465	            "ar",
466	            "Semitic",
467	            "MID",
468	            0.7,
469	            "L40",
470	            -0.12,
471	            0.71
472	          ],
473	          [
474	            "sw",
475	            "Bantu",
476	            "LOW",
477	            0.62,
478	            "L28",
479	            -0.62,
480	            0.03
481	          ],
482	          [
483	            "yo",
484	            "Volta-Niger",
485	            "LOW",
486	            0.57,
487	            "L24",
488	            -0.68,
489	            0.02
490	          ],
491	          [
492	            "am",
493	            "Ethiosemitic",
494	            "LOW",
495	            0.57,
496	            "L24",
497	            -0.65,
498	            0.02
499	          ]
500	        ]
501	      }
502	    ],
503	    "figures": [],
504	    "analysis": "Llama 4 Scout 的 Pareto 显著弱于 Qwen3-235B，core finding: architecture\ndetermines tradeoff shape。ρ_Qwen=-0.65 vs ρ_Llama=-0.33, 且 Llama 呈现\nlanguage-specific 异质性 (3 种语言 ρ > 0)。这不是 Pareto 不存在——global ρ\n仍为负——而是 tradeoff 在不同语言上表现不同。论文中框架为 \"strong vs weak\nPareto\" 的架构对比。\n\n\nLlama 4 Scout (17B active × 16 experts, ~109B total) 的 EN AUROC 达到 0.811，\n低于 Qwen3-235B 但显著高于 MVP Llama-3.1-8B (0.728)。Pareto frontier 呈弱\n负相关 ρ ≈ -0.33，延续 MVP 中 Llama 架构的模式：部分语言 (ru, ko, ar) 随\ndepth 增加迁移不退化甚至略微改善 (ρ > 0)，而 sw/yo/am 退化严重 (ρ < -0.60)。\n这种异质性源于 Llama 4 的 16-expert MoE routing：对 ru/ko/ar 等中高资源语言，\n深层 expert routing 倾向于重用与 English 共享的 expert；对低资源语言则分配到\nspecialized expert，导致表征分离。三种低资源语言 (yo 0.57, my 0.58, am 0.57)\n未通过 0.60 阈值，success rate 17/20 = 0.85 达到 best tier 下限。48 层仅\n12 probed layers，depth 分辨率低于 Qwen3 (24 layers)，ρ 估计的统计功效较低\n(n=12 vs n=24)。\n"
505	  },
506	  {
507	    "name": "CaCLR Full Evaluation",
508	    "description": "L_CaCLR = L_BCE + α·L_SB-ECE + β·L_MMD, 两种架构×20语言完整评估",
509	    "results": {
510	      "best_alpha": 1.0,
511	      "best_beta": 0.1,
512	      "alpha_sweep": {
513	        "0.01": {
514	          "auroc": 0.741,
515	          "ece": 0.148
516	        },
517	        "0.1": {
518	          "auroc": 0.749,
519	          "ece": 0.138
520	        },
521	        "1.0": {
522	          "auroc": 0.763,
523	          "ece": 0.121
524	        },
525	        "10.0": {
526	          "auroc": 0.752,
527	          "ece": 0.128
528	        }
529	      },
530	      "beta_sweep": {
531	        "0.0": {
532	          "auroc": 0.724,
533	          "ece": 0.148
534	        },
535	        "0.001": {
536	          "auroc": 0.728,
537	          "ece": 0.145
538	        },
539	        "0.01": {
540	          "auroc": 0.738,
541	          "ece": 0.137
542	        },
543	        "0.1": {
544	          "auroc": 0.763,
545	          "ece": 0.121
546	        },
547	        "1.0": {
548	          "auroc": 0.731,
549	          "ece": 0.141
550	        }
551	      },
552	      "qwen_L56_pareto_zone": {
553	        "caclr_auroc_avg": 0.763,
554	        "zeroshot_auroc_avg": 0.728,
555	        "delta_auroc": 0.035,
556	        "caclr_ece_avg": 0.121,
557	        "tempscaling_ece_avg": 0.155,
558	        "delta_ece_vs_tempscaling": -0.034
559	      },
560	      "qwen_L72_en_optimal": {
561	        "caclr_auroc_avg": 0.728,
562	        "zeroshot_auroc_avg": 0.672,
563	        "delta_auroc": 0.056,
564	        "caclr_ece_avg": 0.132,
565	        "tempscaling_ece_avg": 0.171,
566	        "delta_ece_vs_tempscaling": -0.039
567	      },
568	      "qwen_oracle_per_lang": {
569	        "caclr_auroc_avg": 0.76,
570	        "zeroshot_auroc_avg": 0.713,
571	        "delta_auroc": 0.047
572	      },
573	      "llama_L32_pareto_zone": {
574	        "caclr_auroc_avg": 0.732,
575	        "zeroshot_auroc_avg": 0.691,
576	        "delta_auroc": 0.041,
577	        "caclr_ece_avg": 0.131,
578	        "tempscaling_ece_avg": 0.163,
579	        "delta_ece_vs_tempscaling": -0.032
580	      },
581	      "llama_L40_en_optimal": {
582	        "caclr_auroc_avg": 0.697,
583	        "zeroshot_auroc_avg": 0.654,
584	        "delta_auroc": 0.043,
585	        "caclr_ece_avg": 0.142,
586	        "tempscaling_ece_avg": 0.176,
587	        "delta_ece_vs_tempscaling": -0.034
588	      },
589	      "ablation": {
590	        "bce_only": {
591	          "auroc": 0.728,
592	          "ece": 0.165
593	        },
594	        "bce_sbece": {
595	          "auroc": 0.724,
596	          "ece": 0.148
597	        },
598	        "bce_mmd": {
599	          "auroc": 0.751,
600	          "ece": 0.136
601	        },
602	        "bce_sbece_mmd": {
603	          "auroc": 0.763,
604	          "ece": 0.121
605	        }
606	      },
607	      "beta_vs_zero_paired_permutation_p": 0.003,
608	      "beta_vs_zero_cohens_d": 0.52,
609	      "beta_vs_zero_bootstrap_ci": [
610	        0.024,
611	        0.058
612	      ],
613	      "caclr_delta_by_tier": {
614	        "HIGH": 0.031,
615	        "MID": 0.048,
616	        "LOW": 0.068
617	      },
618	      "pareto_rho_without_caclr": -0.65,
619	      "pareto_rho_with_caclr": -0.51,
620	      "pareto_shift_interpretation": "CaCLR 减弱 Pareto tradeoff (rho 从 -0.65 到 -0.51), 因为深层迁移退化被部分修复",
621	      "mmd_kernel": "Gaussian RBF, bandwidth=median heuristic",
622	      "optimizer": "Adam, lr=1e-3, cosine decay to 1e-5",
623	      "epochs": 50,
624	      "early_stopping": "patience=10, monitor val BCE loss",
625	      "initialization": "warm-start from standard LR solution",
626	      "batch_size": 256,
627	      "mmd_items": "same items as BCE (probe_train portion)",
628	      "parallel_set_size_per_lang_avg": 630,
629	      "parallel_set_size_per_lang_min": 580,
630	      "translation_quality_note": "am/yo/my translations spot-checked, ~8% semantic drift vs high-resource"
631	    },
632	    "tables": [
633	      {
634	        "name": "Table 4: CaCLR vs All Baselines (Fixed Layer, Pareto Zone)",
635	        "columns": [
636	          "Method",
637	          "Qwen3_AUROC",
638	          "Qwen3_ECE",
639	          "Llama4_AUROC",
640	          "Llama4_ECE",
641	          "Labels_Required"
642	        ],
643	        "rows": [
644	          [
645	            "Zero-shot",
646	            0.728,
647	            0.165,
648	            0.691,
649	            0.179,
650	            "EN only"
651	          ],
652	          [
653	            "Mean-shift",
654	            0.728,
655	            0.168,
656	            0.691,
657	            0.183,
658	            "EN only"
659	          ],
660	          [
661	            "Temp scaling",
662	            0.728,
663	            0.155,
664	            0.691,
665	            0.163,
666	            "EN only"
667	          ],
668	          [
669	            "CaCLR (α=1 β=0.1)",
670	            0.763,
671	            0.121,
672	            0.732,
673	            0.131,
674	            "EN only + parallel inputs"
675	          ],
676	          [
677	            "Linear proj (50)",
678	            0.79,
679	            0.139,
680	            0.749,
681	            0.146,
682	            "50 parallel pairs"
683	          ],
684	          [
685	            "Few-shot (25)",
686	            0.745,
687	            0.152,
688	            0.712,
689	            0.159,
690	            "25 target labels"
691	          ],
692	          [
693	            "Few-shot (100)",
694	            0.774,
695	            0.136,
696	            0.745,
697	            0.142,
698	            "100 target labels"
699	          ]
700	        ]
701	      },
702	      {
703	        "name": "Table 5: Component Ablation (Qwen3-235B, L56, Avg 20 Langs)",
704	        "columns": [
705	          "Components",
706	          "AUROC",
707	          "ECE",
708	          "Delta_AUROC_vs_ZS"
709	        ],
710	        "rows": [
711	          [
712	            "BCE only (= zero-shot)",
713	            0.728,
714	            0.165,
715	            "—"
716	          ],
717	          [
718	            "BCE + SB-ECE",
719	            0.724,
720	            0.148,
721	            -0.004
722	          ],
723	          [
724	            "BCE + MMD",
725	            0.751,
726	            0.136,
727	            0.023
728	          ],
729	          [
730	            "BCE + SB-ECE + MMD",
731	            0.763,
732	            0.121,
733	            0.035
734	          ]
735	        ]
736	      },
737	      {
738	        "name": "Table 6: β Sensitivity (α=1.0 fixed, Qwen3 L56)",
739	        "columns": [
740	          "beta",
741	          "AUROC",
742	          "ECE",
743	          "Delta_vs_beta0"
744	        ],
745	        "rows": [
746	          [
747	            0.0,
748	            0.724,
749	            0.148,
750	            "—"
751	          ],
752	          [
753	            0.001,
754	            0.728,
755	            0.145,
756	            0.004
757	          ],
758	          [
759	            0.01,
760	            0.738,
761	            0.137,
762	            0.014
763	          ],
764	          [
765	            0.1,
766	            0.763,
767	            0.121,
768	            0.039
769	          ],
770	          [
771	            1.0,
772	            0.731,
773	            0.141,
774	            0.007
775	          ]
776	        ]
777	      }
778	    ],
779	    "figures": [],
780	    "analysis": "β > 0 统计显著地改善跨语言迁移 (p=0.003, d=0.52)。CaCLR 的核心价值：完全不需要\ntarget-language correctness labels，仅需 parallel inputs (已通过 GlobalMMLU\n翻译存在)。CaCLR 未超过 linear projection (50 pairs): 0.763 vs 0.790，但\nCaCLR 无需 paired correctness labels。Two methods 互补：CaCLR 适用于无 parallel\npairs 的场景，linear projection 在有少量 parallel data 时更优。CaCLR 在深层\n(EN-optimal) 增益更大 (+0.056) 证明它 shifts Pareto frontier，不只是 uniform\nimprovement。ECE reduction 22% vs temp scaling 构成论文 headline。\n\n\nBest tier 核心假设：\"MMD on probe logits 成功对齐 correctness subspace cross-\nlingually\"。为何成立：(1) 235B 模型的 correctness direction 占据低维语言无关\n子空间 (CKA 分析支持)，因此 1D probe logit 的分布差异主要反映 subspace rotation\n而非 intrinsic signal difference；MMD 通过匹配 logit 分布有效纠正这个 rotation。\n(2) β=0.1 是 sweet spot——足以施加对齐压力 (MMD loss ~0.3 量级) 但不 overwhelm\nBCE loss (初始 ~0.65 量级)；β=1.0 过大导致 MMD dominate，probe 为匹配分布而\n牺牲判别力。(3) SB-ECE 单独贡献有限 (+0.006 AUROC)，但与 MMD 叠加有协同：\nSB-ECE 改善 probability calibration 后，MMD 在更好校准的 logit 空间上匹配更\n有效。(4) 低资源语言获益最大 (+0.068)，因为 zero-shot distribution gap 最大，\nMMD 的边际对齐收益最高——与 Ben-David et al. H-divergence 理论一致。(5) 在\nEN-optimal 深层 L72，CaCLR 增益更大 (+0.056 > +0.035)，因为深层迁移退化更\n严重，recovery space 更大——直接证明 \"CaCLR shifts the Pareto frontier\"。\n统计显著性: paired permutation test p=0.003, Cohen's d=0.52 (medium effect),\nbootstrap 95% CI [0.024, 0.058] 不含零。\n"
781	  },
782	  {
783	    "name": "Difficulty-Controlled Decomposition",
784	    "description": "IRT difficulty probe → project out → retrain → transfer delta. 10 langs × 8 layers × 2 models",
785	    "results": {
786	      "difficulty_probe_r2_avg": 0.61,
787	      "difficulty_probe_r2_range": [
788	        0.43,
789	        0.76
790	      ],
791	      "difficulty_probe_r2_by_lang": {
792	        "zh": 0.72,
793	        "es": 0.76,
794	        "de": 0.68,
795	        "fr": 0.71,
796	        "hi": 0.58,
797	        "ru": 0.65,
798	        "ko": 0.63,
799	        "tr": 0.53,
800	        "sw": 0.43,
801	        "bn": 0.47
802	      },
803	      "avg_transfer_delta_after_projection": 0.035,
804	      "delta_by_lang_category": {
805	        "capability_dominated": {
806	          "langs": [
807	            "zh",
808	            "es",
809	            "fr",
810	            "de",
811	            "ru",
812	            "ko"
813	          ],
814	          "delta": 0.042,
815	          "ci": [
816	            0.031,
817	            0.054
818	          ]
819	        },
820	        "difficulty_dominated": {
821	          "langs": [
822	            "hi",
823	            "tr",
824	            "sw",
825	            "bn"
826	          ],
827	          "delta": -0.018,
828	          "ci": [
829	            -0.029,
830	            -0.007
831	          ]
832	        }
833	      },
834	      "random_projection_delta_avg": -0.003,
835	      "random_projection_delta_std": 0.008,
836	      "random_projection_delta_ci": [
837	        -0.011,
838	        0.005
839	      ],
840	      "delta_by_depth": {
841	        "20%": 0.012,
842	        "35%": 0.021,
843	        "50%": 0.035,
844	        "65%": 0.043,
845	        "80%": 0.051,
846	        "90%": 0.048
847	      },
848	      "qwen_avg_delta": 0.038,
849	      "llama_avg_delta": 0.031,
850	      "predicted_vs_actual_alignment_strategy_accuracy": 0.82
851	    },
852	    "tables": [
853	      {
854	        "name": "Table 7: Difficulty Decomposition Effect by Language Category",
855	        "columns": [
856	          "Category",
857	          "Languages",
858	          "N_langs",
859	          "Delta_AUROC",
860	          "CI_95",
861	          "Random_Control"
862	        ],
863	        "rows": [
864	          [
865	            "Capability-dominated",
866	            "zh/es/fr/de/ru/ko",
867	            6,
868	            0.042,
869	            "[0.031, 0.054]",
870	            -0.002
871	          ],
872	          [
873	            "Difficulty-dominated",
874	            "hi/tr/sw/bn",
875	            4,
876	            -0.018,
877	            "[-0.029, -0.007]",
878	            -0.004
879	          ],
880	          [
881	            "Overall",
882	            "all 10",
883	            10,
884	            0.035,
885	            "[0.021, 0.049]",
886	            -0.003
887	          ]
888	        ]
889	      },
890	      {
891	        "name": "Table 8: Depth × Decomposition Interaction",
892	        "columns": [
893	          "Depth_Pct",
894	          "EN_Probe_AUROC",
895	          "ZS_Delta_After_Proj",
896	          "ZS_Delta_Capability_Only",
897	          "ZS_Delta_Difficulty_Only"
898	        ],
899	        "rows": [
900	          [
901	            "20%",
902	            0.65,
903	            0.012,
904	            0.018,
905	            -0.008
906	          ],
907	          [
908	            "50%",
909	            0.78,
910	            0.035,
911	            0.042,
912	            -0.016
913	          ],
914	          [
915	            "80%",
916	            0.82,
917	            0.051,
918	            0.061,
919	            -0.023
920	          ]
921	        ]
922	      }
923	    ],
924	    "figures": [],
925	    "analysis": "Decomposition 成功分离 difficulty/capability，fulfilling Claim 2。Prescriptive\nvalue: 对于 capability-dominated 语言 (baseline ZS > ~0.70)，projecting out\ndifficulty 是 free lunch (+4.2pp)。对于 difficulty-dominated 语言 (baseline ZS\n< ~0.65)，应保留 difficulty 信号。82% prediction accuracy 表明这个规则可\n自动化为 per-language strategy selector。\n\n\nCorrectness signal 是 difficulty (跨语言共享——哪些题目本身更难) 和 capability\n(语言特异性——模型在该语言上的推理能力) 的纠缠。对于 capability-dominated 语言\n(高资源, 模型具备强推理)，difficulty 是共享但无用的噪声维度：projecting out\n移除了对迁移有害的 confound，暴露纯粹的 capability signal，transfer 改善\n+4.2pp。对于 difficulty-dominated 语言 (低资源, 模型 capability 弱)，difficulty\n本身是 correctness 的主要来源 (模型答对题目主要靠题目简单，而非语言能力)——\n移除它丢失了唯一可迁移的信号，transfer 下降 -1.8pp。深层 delta 更大 (80%\ndepth: +5.1pp vs 20%: +1.2pp)，因为 capability 特化在深层更强，difficulty\nconfound 的 relative 权重在深层更大。Random direction control 的 delta ≈ 0\n排除了纯降维的 artifact。IRT difficulty probe R² 呈 resource gradient (zh 0.72\n> sw 0.43)，因为 IRT difficulty scores 基于高资源语言的人类答题数据，低资源\n语言的 difficulty 编码较弱。Prescriptive accuracy 82% 表明 decomposition\n能正确预测 8/10 语言应该用哪种 alignment strategy。\n"
926	  },
927	  {
928	    "name": "Cross-Lingual Orthogonality",
929	    "description": "Correctness vs verbalized confidence direction cosine similarity, 20 langs × 2 archs",
930	    "results": {
931	      "cosine_range": [
932	        0.012,
933	        0.058
934	      ],
935	      "cosine_mean": 0.032,
936	      "cosine_std": 0.013,
937	      "cosine_by_tier": {
938	        "HIGH": 0.027,
939	        "MID": 0.033,
940	        "LOW": 0.04
941	      },
942	      "cosine_by_arch": {
943	        "Qwen3": 0.029,
944	        "Llama4": 0.035
945	      },
946	      "cosine_extremes": {
947	        "min": {
948	          "lang": "es",
949	          "arch": "Qwen3",
950	          "value": 0.012
951	        },
952	        "max": {
953	          "lang": "am",
954	          "arch": "Llama4",
955	          "value": 0.058
956	        }
957	      },
958	      "cosine_per_lang": {
959	        "en": {
960	          "qwen": 0.023,
961	          "llama": 0.03
962	        },
963	        "zh": {
964	          "qwen": 0.021,
965	          "llama": 0.028
966	        },
967	        "es": {
968	          "qwen": 0.012,
969	          "llama": 0.024
970	        },
971	        "hi": {
972	          "qwen": 0.032,
973	          "llama": 0.039
974	        },
975	        "sw": {
976	          "qwen": 0.042,
977	          "llama": 0.049
978	        },
979	        "am": {
980	          "qwen": 0.048,
981	          "llama": 0.058
982	        }
983	      },
984	      "permutation_test_vs_random_p": "<0.001",
985	      "cosine_vs_resource_rho": 0.34,
986	      "cosine_vs_resource_p": 0.042
987	    },
988	    "tables": [
989	      {
990	        "name": "Table 9: Correctness-Confidence Orthogonality Across Languages",
991	        "columns": [
992	          "Language",
993	          "Resource",
994	          "Qwen3_Cosine",
995	          "Llama4_Cosine",
996	          "Average"
997	        ],
998	        "representative_rows": [
999	          [
1000	            "en",
1001	            "—",
1002	            0.023,
1003	            0.03,
1004	            0.027
1005	          ],
1006	          [
1007	            "zh",
1008	            "HIGH",
1009	            0.021,
1010	            0.028,
1011	            0.025
1012	          ],
1013	          [
1014	            "es",
1015	            "HIGH",
1016	            0.012,
1017	            0.024,
1018	            0.018
1019	          ],
1020	          [
1021	            "hi",
1022	            "MID",
1023	            0.032,
1024	            0.039,
1025	            0.036
1026	          ],
1027	          [
1028	            "ko",
1029	            "MID",
1030	            0.028,
1031	            0.035,
1032	            0.032
1033	          ],
1034	          [
1035	            "sw",
1036	            "LOW",
1037	            0.042,
1038	            0.049,
1039	            0.046
1040	          ],
1041	          [
1042	            "am",
1043	            "LOW",
1044	            0.048,
1045	            0.058,
1046	            0.053
1047	          ]
1048	        ]
1049	      }
1050	    ],
1051	    "figures": [],
1052	    "analysis": "Claim 4 完全成立。Output-based calibration 的结构性限制是跨语言普遍的——\n所有 40 个 (language, architecture) 组合的 cosine < 0.06。Resource tier 与\ncosine 弱正相关 (ρ=0.34, p=0.042)，但 effect size 极小 (range 仅 0.013)。\n这进一步 motivate probe-based calibration：output 层面的信息理论限制不随\n语言变化。\n\n\nCorrectness 和 verbalized confidence 的正交性 (cosine < 0.06) 是 transformer\n架构的内在特征：模型学会了在独立的表征子空间中编码 \"我是否答对了\" (correctness)\n和 \"我认为我有多确定\" (confidence)。这不是 English-specific 现象。正交性在\n所有 20 种语言上持续成立，因为两个方向都由模型的参数化决定，不由输入语言决定。\n低资源语言的 cosine 略高 (0.040 vs 0.027) 有两个原因：(1) confidence probe\n在低资源语言上的 SNR 更低，噪声使 cosine 估计偏离零；(2) 低资源语言的表征\n空间利用率低，两个方向在低维子空间中更容易有 spurious overlap。但即使最高\n的 am=0.058 仍远低于表示有意义相关性的阈值 (~0.2)。\n"
1053	  },
1054	  {
1055	    "name": "Probe Complexity Comparison",
1056	    "description": "Logistic regression vs 2-layer MLP: EN accuracy 和 cross-lingual transfer 对比",
1057	    "results": {
1058	      "lr_en_best_auroc": 0.832,
1059	      "mlp_en_best_auroc": 0.851,
1060	      "mlp_en_advantage": 0.019,
1061	      "lr_zs_auroc_avg": 0.713,
1062	      "mlp_zs_auroc_avg": 0.685,
1063	      "lr_zs_advantage": 0.028,
1064	      "lr_relative_degradation": 0.143,
1065	      "mlp_relative_degradation": 0.195,
1066	      "mlp_excess_degradation": 0.052,
1067	      "lr_zs_low": 0.635,
1068	      "mlp_zs_low": 0.581,
1069	      "lr_vs_mlp_gap_low": 0.054,
1070	      "lr_zs_high": 0.773,
1071	      "mlp_zs_high": 0.752,
1072	      "lr_vs_mlp_gap_high": 0.021,
1073	      "lr_ece_avg": 0.165,
1074	      "mlp_ece_avg": 0.184
1075	    },
1076	    "tables": [
1077	      {
1078	        "name": "Table S3: Probe Complexity × Transfer",
1079	        "columns": [
1080	          "Metric",
1081	          "LR",
1082	          "MLP_2layer",
1083	          "Delta"
1084	        ],
1085	        "rows": [
1086	          [
1087	            "EN Best AUROC",
1088	            0.832,
1089	            0.851,
1090	            0.019
1091	          ],
1092	          [
1093	            "ZS Transfer Avg 20L",
1094	            0.713,
1095	            0.685,
1096	            -0.028
1097	          ],
1098	          [
1099	            "Relative Degradation",
1100	            "14.3%",
1101	            "19.5%",
1102	            "+5.2pp"
1103	          ],
1104	          [
1105	            "ZS Low-Resource Avg",
1106	            0.635,
1107	            0.581,
1108	            -0.054
1109	          ],
1110	          [
1111	            "ECE Avg",
1112	            0.165,
1113	            0.184,
1114	            0.019
1115	          ]
1116	        ]
1117	      }
1118	    ],
1119	    "figures": [],
1120	    "analysis": "Linear probe 是跨语言 transfer 的正确选择。MLP 的 +1.9pp English 优势远不足以\n补偿 -2.8pp transfer 劣势。论文中以此证明 LR 作为默认 probe 的合理性。\n\n\nMLP 在 English 上略优 (+1.9pp) 是因为 correctness signal 含有弱非线性成分——\n某些层的 correctness 编码涉及特征交互。但 MLP 同时学到了 English-specific 的\n非线性 pattern (e.g. English-specific token position interactions)，这些 pattern\n在目标语言中不存在，导致 transfer 时引入负迁移。Linear probe 的 inductive bias\n恰好匹配 correctness direction 的跨语言结构：线性投影只能捕获方向性信息，\n而方向性信息正是跨语言共享的 (CKA 子空间分析支持)。差距在低资源语言最大\n(LR +5.4pp vs MLP)，因为低资源表征的线性结构相对于英语更保守 (低维对齐\n更强)，而 MLP 学到的非线性 feature 在低资源语境下完全失效。\n"
1121	  },
1122	  {
1123	    "name": "Additional Benchmarks (Belebele + MMLU-ProX)",
1124	    "description": "最优 probes + CaCLR 在 Belebele 和 MMLU-ProX 上的泛化验证",
1125	    "results": {
1126	      "belebele_qwen_en_auroc": 0.814,
1127	      "belebele_qwen_zs_avg": 0.698,
1128	      "belebele_qwen_caclr_avg": 0.741,
1129	      "belebele_qwen_pareto_rho": -0.61,
1130	      "belebele_llama_en_auroc": 0.793,
1131	      "belebele_llama_zs_avg": 0.671,
1132	      "belebele_llama_caclr_avg": 0.712,
1133	      "mmlupx_qwen_en_auroc": 0.839,
1134	      "mmlupx_qwen_zs_avg": 0.721,
1135	      "mmlupx_qwen_caclr_avg": 0.767,
1136	      "mmlupx_qwen_pareto_rho": -0.67,
1137	      "mmlupx_llama_en_auroc": 0.818,
1138	      "mmlupx_llama_zs_avg": 0.694,
1139	      "mmlupx_llama_caclr_avg": 0.738,
1140	      "per_lang_rank_corr_gmmlu_belebele": 0.89,
1141	      "per_lang_rank_corr_gmmlu_mmlupx": 0.93
1142	    },
1143	    "tables": [
1144	      {
1145	        "name": "Table 10: Cross-Benchmark Generalization (Qwen3-235B)",
1146	        "columns": [
1147	          "Benchmark",
1148	          "Domain",
1149	          "EN_AUROC",
1150	          "ZS_Avg",
1151	          "CaCLR_Avg",
1152	          "Pareto_rho",
1153	          "CaCLR_Delta"
1154	        ],
1155	        "rows": [
1156	          [
1157	            "GlobalMMLU",
1158	            "Knowledge QA",
1159	            0.832,
1160	            0.713,
1161	            0.76,
1162	            -0.65,
1163	            0.047
1164	          ],
1165	          [
1166	            "Belebele",
1167	            "Reading Comp",
1168	            0.814,
1169	            0.698,
1170	            0.741,
1171	            -0.61,
1172	            0.043
1173	          ],
1174	          [
1175	            "MMLU-ProX",
1176	            "Knowledge QA",
1177	            0.839,
1178	            0.721,
1179	            0.767,
1180	            -0.67,
1181	            0.046
1182	          ]
1183	        ]
1184	      }
1185	    ],
1186	    "figures": [],
1187	    "analysis": "三 benchmark 一致性强。Pareto frontier 和 CaCLR gains 跨 domain replicate。\nBelebele 的略低结果 underscores domain dependency 但不 undermine core claims。\n\n\nBelebele 是 reading comprehension，与 GlobalMMLU (knowledge QA) 的 domain 不同。\nCorrectness direction 有轻微 domain dependency：probe 在 knowledge-heavy items\n上学到的 correctness signal 不完全迁移到 comprehension tasks，EN AUROC 略降\n(0.814 vs 0.832)。但 Pareto 结构高度一致 (ρ=-0.61 vs -0.65)，因为 depth-\ntransferability tradeoff 是架构特征而非 task 特征。MMLU-ProX 与 GlobalMMLU\ndomain overlap 大 (同属 knowledge QA)，结果最相似。Per-language ranking 跨\nbenchmark 高度稳定 (ρ=0.89-0.93)——在 GlobalMMLU 上 transfer 好的语言在\nBelebele 上也好。CaCLR 增益在 Belebele 上略小 (+4.3pp vs +4.7pp) 但仍正面。\n"
1188	  },
1189	  {
1190	    "name": "Quantization Validation",
1191	    "description": "W4A16 vs FP16 (Llama) + GPTQ-INT4 vs FP16 (Qwen), 5 layers, 5% subset",
1192	    "results": {
1193	      "llama_w4a16_vs_fp16": {
1194	        "auroc_diff_avg": 0.004,
1195	        "auroc_diff_max": 0.008,
1196	        "auroc_diff_per_layer": {
1197	          "L8": 0.002,
1198	          "L16": 0.003,
1199	          "L24": 0.005,
1200	          "L32": 0.006,
1201	          "L40": 0.008
1202	        },
1203	        "cka_quantized_vs_fp16": 0.987,
1204	        "paired_t_p": 0.31
1205	      },
1206	      "qwen_int4_vs_fp16": {
1207	        "auroc_diff_avg": 0.006,
1208	        "auroc_diff_max": 0.013,
1209	        "auroc_diff_per_layer": {
1210	          "L16": 0.003,
1211	          "L32": 0.005,
1212	          "L48": 0.006,
1213	          "L64": 0.008,
1214	          "L80": 0.013
1215	        },
1216	        "cka_quantized_vs_fp16": 0.981,
1217	        "paired_t_p": 0.18
1218	      }
1219	    },
1220	    "tables": [
1221	      {
1222	        "name": "Table S4: Quantization Validation",
1223	        "columns": [
1224	          "Model",
1225	          "Quantization",
1226	          "Avg_Delta_AUROC",
1227	          "Max_Delta_AUROC",
1228	          "CKA",
1229	          "Paired_t_p"
1230	        ],
1231	        "rows": [
1232	          [
1233	            "Llama 4 Scout",
1234	            "W4A16",
1235	            0.004,
1236	            0.008,
1237	            0.987,
1238	            0.31
1239	          ],
1240	          [
1241	            "Qwen3-235B",
1242	            "GPTQ-INT4",
1243	            0.006,
1244	            0.013,
1245	            0.981,
1246	            0.18
1247	          ]
1248	        ]
1249	      }
1250	    ],
1251	    "figures": [],
1252	    "analysis": "量化不影响核心结论。最大偏差 1.3pp 远小于实验主要效应 (Pareto gap ~6pp,\nCaCLR gain ~4.5pp)。放入 appendix 即可。\n\n\nW4A16 仅压缩权重 (4-bit)，激活保持 16-bit，因此对 correctness direction (线性\nprobe 的目标) 影响极小——probe 训练使用的是 activation vectors，不直接依赖权重\n精度。GPTQ-INT4 的误差略大因为 4-bit 量化是更激进的压缩，且 Qwen3 有 94 层\n导致误差累积更多。最大偏差 1.3pp 出现在最深层 L80 (误差在 94 层中逐层累积)。\n所有差异在 paired t-test 下不显著 (p > 0.15)，CKA > 0.98 表示量化前后表征\n几乎等价。论文中报告此验证可消除 reviewer \"INT4/W4A16 artifacts\" 的顾虑。\n"
1253	  },
1254	  {
1255	    "name": "CKA Cross-Lingual Geometric Analysis",
1256	    "description": "CKA (linear kernel) 20 langs × all layers × 2 archs, partial correlation + subspace angle",
1257	    "results": {
1258	      "cka_partial_corr_controlling_depth": 0.42,
1259	      "cka_partial_corr_p": 0.008,
1260	      "same_layer_corr_by_depth": {
1261	        "25%": {
1262	          "rho": -0.48,
1263	          "p": 0.032
1264	        },
1265	        "50%": {
1266	          "rho": -0.67,
1267	          "p": 0.001
1268	        },
1269	        "75%": {
1270	          "rho": -0.73,
1271	          "p": "<0.001"
1272	        }
1273	      },
1274	      "n_significant_layers": 18,
1275	      "qwen_cka_cliff": {
1276	        "location": "L64 (68% depth)",
1277	        "cka_before": 0.72,
1278	        "cka_after": 0.41,
1279	        "drop_magnitude": 0.31
1280	      },
1281	      "llama_cka_pattern": "gradual decline, no cliff",
1282	      "llama_cka_at_L40": 0.52,
1283	      "llama_cka_at_L24": 0.71,
1284	      "qwen_pooled_rho": -0.58,
1285	      "qwen_pooled_p": "<0.001",
1286	      "llama_pooled_rho": -0.43,
1287	      "llama_pooled_p": 0.002,
1288	      "between_lang_rho_at_50pct_depth": -0.67,
1289	      "between_lang_p_at_50pct_depth": 0.001,
1290	      "between_lang_rho_at_75pct_depth": -0.73,
1291	      "between_lang_p_at_75pct_depth": "<0.001",
1292	      "correctness_subspace_angle_avg_deg": 12.3,
1293	      "correctness_subspace_angle_std_deg": 4.8,
1294	      "global_repr_angle_avg_deg": 38.7,
1295	      "global_repr_angle_std_deg": 9.2,
1296	      "subspace_angle_ratio": 3.15,
1297	      "cka_collapse_threshold": 0.35,
1298	      "langs_below_threshold_at_deepest": [
1299	        "sw",
1300	        "yo",
1301	        "am",
1302	        "my"
1303	      ],
1304	      "per_lang_within_rho_significant": 14,
1305	      "per_lang_within_rho_avg": -0.48
1306	    },
1307	    "tables": [
1308	      {
1309	        "name": "Table 11: CKA Partial Correlation Analysis",
1310	        "columns": [
1311	          "Analysis",
1312	          "Statistic",
1313	          "Value",
1314	          "p_value",
1315	          "Interpretation"
1316	        ],
1317	        "rows": [
1318	          [
1319	            "Raw CKA-degradation pooled",
1320	            "rho",
1321	            -0.64,
1322	            "<0.001",
1323	            "Confounded by depth"
1324	          ],
1325	          [
1326	            "Partial corr controlling depth",
1327	            "r",
1328	            0.42,
1329	            0.008,
1330	            "CKA adds info beyond depth"
1331	          ],
1332	          [
1333	            "Between-lang at 50% depth (n=20)",
1334	            "rho",
1335	            -0.67,
1336	            0.001,
1337	            "Strongest cross-lang test"
1338	          ],
1339	          [
1340	            "Between-lang at 75% depth (n=20)",
1341	            "rho",
1342	            -0.73,
1343	            "<0.001",
1344	            "Even stronger deep"
1345	          ],
1346	          [
1347	            "Within-lang avg (n=24 layers)",
1348	            "rho",
1349	            -0.48,
1350	            "varies",
1351	            "14/20 langs significant"
1352	          ]
1353	        ]
1354	      },
1355	      {
1356	        "name": "Table 12: Subspace Angle Analysis (Quantitative)",
1357	        "columns": [
1358	          "Measure",
1359	          "Qwen3_235B",
1360	          "Llama4_Scout",
1361	          "Interpretation"
1362	        ],
1363	        "rows": [
1364	          [
1365	            "Correctness subspace angle (avg)",
1366	            "11.2°",
1367	            "13.5°",
1368	            "Small — cross-ling shared"
1369	          ],
1370	          [
1371	            "Correctness subspace angle (std)",
1372	            "3.9°",
1373	            "5.7°",
1374	            "More variable in Llama"
1375	          ],
1376	          [
1377	            "Global representation angle (avg)",
1378	            "41.3°",
1379	            "36.1°",
1380	            "Large — language-specific"
1381	          ],
1382	          [
1383	            "Global/correctness ratio",
1384	            3.69,
1385	            2.67,
1386	            "Qwen: correctness 4x more stable"
1387	          ],
1388	          [
1389	            "CKA cliff location",
1390	            "68% depth",
1391	            "no cliff",
1392	            "Architecture difference"
1393	          ],
1394	          [
1395	            "CKA cliff magnitude",
1396	            0.31,
1397	            "N/A",
1398	            "Qwen only"
1399	          ]
1400	        ]
1401	      }
1402	    ],
1403	    "figures": [],
1404	    "analysis": "CKA geometric analysis 成立 (partial r=0.42, p=0.008)，支撑 \"geometric analysis\"\nframing。三层 evidence：(1) partial correlation 证明 CKA 有 depth 以外的解释力；\n(2) between-language correlation (ρ=-0.67) 是最直接证据；(3) subspace angle ratio\n3.15 提供几何直觉。CKA cliff 的有/无解释 Qwen vs Llama Pareto 差异。这是\ndiscovery 级别 finding——连接了 representation geometry 和 practical transfer。\n\n\nBest tier 假设 \"CKA partial correlation 控制 depth 后仍显著\"。Partial r=0.42\n(p=0.008) 表示 CKA 对 transfer degradation 有独立于 depth 的解释力。核心\n机制：correctness direction 占据低维语言无关子空间 (principal angle ~12°)，\n而全局表征差异远大 (~39°)，ratio 3.15。这意味着即使两种语言的全局表征已\n显著分化 (CKA 下降)，correctness 子空间仍可能保持对齐——直到 CKA 跌破临界\n阈值 ~0.35，此时全局分化足够大以至于连低维子空间也被扰动。\nQwen3 的 CKA cliff (L64, 突降 0.31) 解释了为何 Qwen Pareto 清晰：在 cliff\n之前 (L0-L60)，transfer 随 depth 缓慢退化；在 cliff 之后 (L64-L94)，transfer\n急剧崩溃。这产生了强 Pareto (ρ=-0.65) 和清晰的 \"optimal transfer zone\" (L48-L60)。\nLlama4 没有 cliff，CKA 渐降 → Pareto 弱且异质 (ρ=-0.33)。\nBetween-language 分析 (固定层, n=20) 是最强统计检验：在 50% depth，CKA 高的\n语言 (zh 0.82, es 0.79) transfer 好，CKA 低的 (sw 0.48, am 0.42) transfer 差，\nρ=-0.67 (p=0.001)。在 75% depth 更强 (ρ=-0.73)，因为此处 CKA variance 更大。\n20 languages 的密度使 per-language within-lang Spearman 首次有足够统计功效\n(n=24 for Qwen vs MVP 的 n=9)：14/20 显著，avg ρ=-0.48，比 MVP pilot\n(几乎全 n.s.) 大幅改善。\n"
1405	  },
1406	  {
1407	    "name": "Linear Projection Sample Efficiency",
1408	    "description": "Parallel pairs 数量 (10-200) 对 linear projection transfer 的影响",
1409	    "results": {
1410	      "qwen_L56": {
1411	        "pairs_10": {
1412	          "auroc": 0.739,
1413	          "delta": 0.011,
1414	          "ci_width": 0.034
1415	        },
1416	        "pairs_20": {
1417	          "auroc": 0.758,
1418	          "delta": 0.03,
1419	          "ci_width": 0.023
1420	        },
1421	        "pairs_50": {
1422	          "auroc": 0.79,
1423	          "delta": 0.062,
1424	          "ci_width": 0.015
1425	        },
1426	        "pairs_100": {
1427	          "auroc": 0.798,
1428	          "delta": 0.07,
1429	          "ci_width": 0.01
1430	        },
1431	        "pairs_200": {
1432	          "auroc": 0.802,
1433	          "delta": 0.074,
1434	          "ci_width": 0.007
1435	        }
1436	      },
1437	      "llama_L32": {
1438	        "pairs_10": {
1439	          "auroc": 0.712,
1440	          "delta": 0.021,
1441	          "ci_width": 0.031
1442	        },
1443	        "pairs_20": {
1444	          "auroc": 0.729,
1445	          "delta": 0.038,
1446	          "ci_width": 0.022
1447	        },
1448	        "pairs_50": {
1449	          "auroc": 0.749,
1450	          "delta": 0.058,
1451	          "ci_width": 0.014
1452	        },
1453	        "pairs_100": {
1454	          "auroc": 0.757,
1455	          "delta": 0.066,
1456	          "ci_width": 0.009
1457	        },
1458	        "pairs_200": {
1459	          "auroc": 0.761,
1460	          "delta": 0.07,
1461	          "ci_width": 0.006
1462	        }
1463	      },
1464	      "elbow_point": 50,
1465	      "marginal_gain_50_to_100": 0.008,
1466	      "marginal_gain_100_to_200": 0.004,
1467	      "caclr_equivalent_pairs": 35
1468	    },
1469	    "tables": [
1470	      {
1471	        "name": "Table 13: Linear Projection Sample Efficiency (Qwen3, L56)",
1472	        "columns": [
1473	          "Pairs",
1474	          "AUROC_Avg",
1475	          "Delta_vs_ZS",
1476	          "Marginal_Gain",
1477	          "CI_95_Width"
1478	        ],
1479	        "rows": [
1480	          [
1481	            10,
1482	            0.739,
1483	            0.011,
1484	            "—",
1485	            0.034
1486	          ],
1487	          [
1488	            20,
1489	            0.758,
1490	            0.03,
1491	            0.019,
1492	            0.023
1493	          ],
1494	          [
1495	            50,
1496	            0.79,
1497	            0.062,
1498	            0.032,
1499	            0.015
1500	          ],
1501	          [
1502	            100,
1503	            0.798,
1504	            0.07,
1505	            0.008,
1506	            0.01
1507	          ],
1508	          [
1509	            200,
1510	            0.802,
1511	            0.074,
1512	            0.004,
1513	            0.007
1514	          ]
1515	        ]
1516	      }
1517	    ],
1518	    "figures": [],
1519	    "analysis": "50 pairs 是实用甜点。Linear projection 在 50 pairs 时超过 CaCLR (0.790 vs\n0.763)，但需要 parallel pairs with correctness labels。两方法互补：CaCLR\nfor zero-label 场景，linear projection for minimal-data 场景。\n\n\nLinear projection 学习 affine transformation 将 target 语言 correctness subspace\n旋转对齐到 English。Correctness direction 是低维的 (实际是 1D for LR probe)，\n因此旋转矩阵的自由度极低——50 pairs 已充分约束 (条件数稳定)。10 pairs 时 CI\n宽 0.034 (不稳定)，50 pairs CI 收窄至 0.015。超过 50 pairs，marginal gain\n从 +2.2pp/50pairs 骤降至 +0.8pp/50pairs 和 +0.4pp/100pairs。CaCLR (无 parallel\npairs 的 labels) 等效于 ~35-pair linear projection (AUROC 0.763 vs pairs_35\n插值约 0.76)，表明 MMD distributional matching 实现了部分但非完全的子空间\n对齐。50 pairs 的实用意义大：几乎所有 GlobalMMLU 语言都有 600+ parallel items，\n随机选 50 对即可达到 plateau。\n"
1520	  },
1521	  {
1522	    "name": "Full-Scale Probing Control Tasks",
1523	    "description": "Hewitt & Liang control tasks, 20 langs × 2 archs × all layers (扩展 MVP English-only 结果)",
1524	    "results": {
1525	      "selectivity_below_005_fraction": 0.1,
1526	      "low_sel_distribution": {
1527	        "early_layers_pct": 0.72,
1528	        "low_resource_pct": 0.68,
1529	        "overlap_early_AND_low": 0.54
1530	      },
1531	      "qwen_selectivity_avg": 0.178,
1532	      "llama_selectivity_avg": 0.152,
1533	      "control_auroc_avg": 0.491,
1534	      "control_auroc_std": 0.012,
1535	      "control_auroc_max": 0.518,
1536	      "selectivity_grid_qwen": {
1537	        "early_HIGH": 0.045,
1538	        "early_MID": 0.036,
1539	        "early_LOW": 0.019,
1540	        "mid_HIGH": 0.142,
1541	        "mid_MID": 0.118,
1542	        "mid_LOW": 0.078,
1543	        "deep_HIGH": 0.261,
1544	        "deep_MID": 0.242,
1545	        "deep_LOW": 0.188
1546	      },
1547	      "problem_zone_cells": 48,
1548	      "total_cells": 480,
1549	      "problem_zone_pct": 0.1,
1550	      "english_selectivity_deep_layers": 0.255,
1551	      "cross_lingual_selectivity_deep_layers_avg": 0.212,
1552	      "cross_lingual_selectivity_deep_layers_low_resource": 0.168
1553	    },
1554	    "tables": [
1555	      {
1556	        "name": "Table S5: Selectivity by Depth × Resource Tier (Qwen3)",
1557	        "columns": [
1558	          "Depth_Range",
1559	          "HIGH_Resource",
1560	          "MID_Resource",
1561	          "LOW_Resource"
1562	        ],
1563	        "rows": [
1564	          [
1565	            "0-33% (early)",
1566	            0.045,
1567	            0.036,
1568	            0.019
1569	          ],
1570	          [
1571	            "33-67% (mid)",
1572	            0.142,
1573	            0.118,
1574	            0.078
1575	          ],
1576	          [
1577	            "67-100% (deep)",
1578	            0.261,
1579	            0.242,
1580	            0.188
1581	          ]
1582	        ]
1583	      }
1584	    ],
1585	    "figures": [],
1586	    "analysis": "10% capacity artifact rate 在 best tier [0.05, 0.15] 范围内。核心 probing\nresults (中深层 × 中高资源) selectivity > 0.10，genuine signal。Low-resource ×\nearly-layer zone 应在 paper 中标注为 \"interpret with caution\"。\n\n\nControl task AUROC 稳定在 ~0.49 (理论 0.50)，confirming permuted labels 不被\nprobe 学到——probing capacity 有限，不会 memorize random labels。10% 的 grid\ncells 有 selectivity < 0.05，集中在 (early layers, LOW resource) 象限：\n(1) Early layers (L0-L20 Qwen / L0-L12 Llama): correctness signal 尚未形成，\nreal probe 和 control probe 表现接近，selectivity ≈ 0；(2) Low-resource\nlanguages: 较少的预训练数据 → correctness 编码更弱 → real probe 提升有限。\n交叉：54% 的 low-selectivity cells 同时满足 early + low-resource。MVP 的\nEnglish-only plan_013 结果 (selectivity 集中在 L20-L27) 与 full-scale 一致，\n但 cross-lingual extension 揭示了资源维度——英语深层 selectivity 0.255 vs\n低资源深层 0.168。这本身是 methodological contribution：跨语言 probing 中\n~10% 的结果需谨慎解读。\n"
1587	  },
1588	  {
1589	    "name": "Gemma 4 31B Dense — Third Architecture",
1590	    "description": "60层 Dense (FP16), 第三架构提供 dense vs MoE 对比",
1591	    "results": {
1592	      "en_best_auroc": 0.821,
1593	      "en_best_layer": 48,
1594	      "zs_transfer_auroc_avg_20lang": 0.702,
1595	      "zs_transfer_success_rate": 0.9,
1596	      "zs_fail_langs": [
1597	        "yo",
1598	        "am"
1599	      ],
1600	      "pareto_spearman_rho_global": -0.52,
1601	      "cka_pattern": "gradual decline, onset deeper than Llama (no cliff)",
1602	      "cka_correctness_subspace_angle_avg": 13.1,
1603	      "caclr_delta_auroc_avg": 0.039
1604	    },
1605	    "tables": [
1606	      {
1607	        "name": "Table 14: Three-Architecture Comparison",
1608	        "columns": [
1609	          "Architecture",
1610	          "Type",
1611	          "EN_AUROC",
1612	          "ZS_Avg",
1613	          "Pareto_rho",
1614	          "CKA_Pattern",
1615	          "CaCLR_Delta"
1616	        ],
1617	        "rows": [
1618	          [
1619	            "Qwen3-235B",
1620	            "MoE (Int4)",
1621	            0.832,
1622	            0.713,
1623	            -0.65,
1624	            "Cliff at 68%",
1625	            0.047
1626	          ],
1627	          [
1628	            "Gemma4-31B",
1629	            "Dense (FP16)",
1630	            0.821,
1631	            0.702,
1632	            -0.52,
1633	            "Gradual, deep onset",
1634	            0.039
1635	          ],
1636	          [
1637	            "Llama4-Scout",
1638	            "MoE (W4A16)",
1639	            0.811,
1640	            0.684,
1641	            -0.33,
1642	            "Gradual, early onset",
1643	            0.041
1644	          ]
1645	        ]
1646	      }
1647	    ],
1648	    "figures": [],
1649	    "analysis": "第三架构填充了 dense vs MoE 对比。Pareto 强度排序 (Qwen > Gemma > Llama) 与\n架构差异一致：MoE cliff 产生最强 tradeoff，dense 渐降产生中等 tradeoff，\n无 cliff 的 MoE 最弱。Camera-ready 的 n=3 架构虽仍不足以做因果归因 (type,\nscale, layers, training data 均不同)，但三点一致的模式 strengthens \"architecture-\ndependent tradeoff\" 的 observational claim。\n\n\nDense 31B 没有 MoE routing，表征特化更均匀 (无 expert 分配的 language-specific\n路径)，Pareto ρ=-0.52 介于 Qwen3 (ρ=-0.65, 强 MoE cliff) 和 Llama4 (ρ=-0.33,\n弱 MoE) 之间。EN AUROC 0.821 反映 31B dense 的容量低于 235B 但高于 17B active。\nCKA 渐降模式接近 Llama 但 onset 更深——dense model 在中间层保持更强的跨语言\n共享 (无 expert routing 导致的早期分化)。Dense 架构的 Pareto 中等强度提供了\ntheory-consistent 的三点比较：cliff MoE (Qwen) > dense (Gemma) > gradual MoE\n(Llama)。仅 yo/am 失败 (2/20)，success rate 0.90。CaCLR delta +3.9pp 低于\nQwen (+4.7pp) 但高于 Llama (+4.1pp)——dense 的初始 ZS transfer 已较好 (CKA\n更高)，CaCLR 的 marginal room 稍小。\n"
1650	  },
1651	  {
1652	    "name": "Extended Language Coverage (50+)",
1653	    "description": "扩展至 50+ 语言 (GlobalMMLU + Belebele full sets)",
1654	    "results": {
1655	      "total_languages": 53,
1656	      "zs_success_rate": 0.83,
1657	      "n_success": 44,
1658	      "n_fail": 9,
1659	      "fail_langs": [
1660	        "am",
1661	        "my",
1662	        "yo",
1663	        "si",
1664	        "lo",
1665	        "km",
1666	        "gu",
1667	        "or",
1668	        "ne"
1669	      ],
1670	      "pareto_rho_qwen_global_53": -0.62,
1671	      "pareto_rho_llama_global_53": -0.31,
1672	      "resource_tier_gradient_r2": 0.71,
1673	      "new_findings": {
1674	        "dravidian_cluster": "ta/ml/kn 形成 cluster, ZS AUROC 0.64-0.68, transfer 特征接近 MID tier",
1675	        "austronesian_cluster": "id/ms/tl transfer 异常好 (0.72-0.74)，因为与英语的表征对齐度高",
1676	        "uralic_outlier": "fi/hu ZS AUROC 差异大 (fi 0.69 vs hu 0.65)，尽管同为 Uralic"
1677	      },
1678	      "caclr_delta_avg_53": 0.044,
1679	      "caclr_delta_new_langs_avg": 0.041
1680	    },
1681	    "tables": [
1682	      {
1683	        "name": "Table S6: Extended Language Coverage Summary",
1684	        "columns": [
1685	          "Metric",
1686	          "20_Langs",
1687	          "53_Langs"
1688	        ],
1689	        "rows": [
1690	          [
1691	            "ZS Success Rate",
1692	            "95% (Qwen)",
1693	            "83%"
1694	          ],
1695	          [
1696	            "Pareto ρ Qwen",
1697	            -0.65,
1698	            -0.62
1699	          ],
1700	          [
1701	            "Pareto ρ Llama",
1702	            -0.33,
1703	            -0.31
1704	          ],
1705	          [
1706	            "Resource Gradient R²",
1707	            "~0.60",
1708	            0.71
1709	          ],
1710	          [
1711	            "CaCLR Δ AUROC avg",
1712	            0.047,
1713	            0.044
1714	          ]
1715	        ]
1716	      }
1717	    ],
1718	    "figures": [],
1719	    "analysis": "Camera-ready 扩展确认 core findings 跨 50+ 语言成立。9 种 fail 语言均为\nextreme low-resource (预训练 tokens < 100M)，consistent with domain adaptation\ntheory 的 H-divergence 预测。Austronesian cluster 的高 transfer 是 interesting\nsecondary finding。\n\n扩展至 53 语言后，成功率从 ~90% (20 langs) 降至 83% (53 langs)，因为新增\n语言多为 extreme low-resource (si, lo, km 等)。但 Pareto ρ 和主要 patterns\n保持稳定 (Qwen ρ=-0.62 vs -0.65 at 20 langs)，slight reduction 因为新增的\n低资源语言削弱了 global correlation。Resource tier gradient 在更大样本下更\nrobust (R²=0.71, up from ~0.60 at 20 langs)。Austronesian 语言 (id/ms/tl)\ntransfer 异常好，因为这些语言在大模型预训练中常被 grouped with English-heavy\ncorpora (code-switching, romanization)。CaCLR 增益在新增语言上 (+4.1pp) 与\n原 20 语言 (+4.7pp) 相当，confirming method generalizability。\n"
1720	  }
1721	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "756292b5-6d1e-43ab-be2b-84d00c5b66c2",
  "isSidechain": false,
  "promptId": "21625223-a819-4abc-b0c5-9519cc481936",
  "type": "user",
  "uuid": "27e30b50-aa41-4c07-8148-59bb2282c701",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Qwen3-235B Full Pareto Frontier\",\n    \"description\": \"94层 MoE (INT4), 24 probed layers (每4层), 20语言, 4 transfer conditions (CaCLR 在 plan_003)\",\n    \"results\": {\n      \"en_best_auroc\": 0.832,\n      \"en_best_layer\": 72,\n      \"en_auroc_range\": [\n        0.548,\n        0.832\n      ],\n      \"en_best_ece_raw\": 0.126,\n      \"zs_transfer_auroc_avg_20lang\": 0.713,\n      \"zs_transfer_success_rate\": 0.95,\n      \"zs_fail_langs\": [\n        \"am\"\n      ],\n      \"pareto_spearman_rho_global\": -0.65,\n      \"pareto_spearman_rho_per_lang_range\": [\n        -0.82,\n        -0.41\n      ],\n      \"zs_auroc_by_tier\": {\n        \"HIGH_avg\": 0.773,\n        \"MID_avg\": 0.719,\n        \"LOW_avg\": 0.635\n      },\n      \"zs_best_by_lang\": {\n        \"zh\": {\n          \"auroc\": 0.79,\n          \"best_layer\": 56\n        },\n        \"es\": {\n          \"auroc\": 0.78,\n          \"best_layer\": 60\n        },\n        \"fr\": {\n          \"auroc\": 0.77,\n          \"best_layer\": 56\n        },\n        \"de\": {\n          \"auroc\": 0.77,\n          \"best_layer\": 60\n        },\n        \"ja\": {\n          \"auroc\": 0.75,\n          \"best_layer\": 52\n        },\n        \"pt\": {\n          \"auroc\": 0.78,\n          \"best_layer\": 56\n        },\n        \"it\": {\n          \"auroc\": 0.77,\n          \"best_layer\": 60\n        },\n        \"hi\": {\n          \"auroc\": 0.73,\n          \"best_layer\": 48\n        },\n        \"ru\": {\n          \"auroc\": 0.74,\n          \"best_layer\": 52\n        },\n        \"ko\": {\n          \"auroc\": 0.73,\n          \"best_layer\": 52\n        },\n        \"tr\": {\n          \"auroc\": 0.7,\n          \"best_layer\": 44\n        },\n        \"vi\": {\n          \"auroc\": 0.71,\n          \"best_layer\": 48\n        },\n        \"ar\": {\n          \"auroc\": 0.72,\n          \"best_layer\": 52\n        },\n        \"th\": {\n          \"auroc\": 0.7,\n          \"best_layer\": 44\n        },\n        \"sw\": {\n          \"auroc\": 0.65,\n          \"best_layer\": 40\n        },\n        \"bn\": {\n          \"auroc\": 0.66,\n          \"best_layer\": 44\n        },\n        \"yo\": {\n          \"auroc\": 0.61,\n          \"best_layer\": 36\n        },\n        \"te\": {\n          \"auroc\": 0.66,\n          \"best_layer\": 44\n        },\n        \"my\": {\n          \"auroc\": 0.63,\n          \"best_layer\": 36\n        },\n        \"am\": {\n          \"auroc\": 0.598,\n          \"best_layer\": 36\n        }\n      },\n      \"depth_transfer_snapshot\": {\n        \"en_at_L72\": 0.832,\n        \"zs_avg_at_L72\": 0.672,\n        \"en_at_L56\": 0.812,\n        \"zs_avg_at_L56\": 0.728,\n        \"en_at_L40\": 0.762,\n        \"zs_avg_at_L40\": 0.706\n      },\n      \"mean_shift_delta_auroc\": 0.0,\n      \"linear_proj_50_delta_auroc_avg\": 0.062,\n      \"fewshot_25_auroc_avg\": 0.738,\n      \"fewshot_100_auroc_avg\": 0.768,\n      \"bootstrap_ci_width_auroc\": 0.018\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Qwen3-235B Pareto Frontier — Per-Language Summary\",\n        \"columns\": [\n          \"Language\",\n          \"Family\",\n          \"Resource\",\n          \"Best_ZS_AUROC\",\n          \"Best_ZS_Layer\",\n          \"EN_AUROC_at_Same_Layer\",\n          \"Spearman_rho\",\n          \"rho_p\"\n        ],\n        \"representative_rows\": [\n          [\n            \"zh\",\n            \"Sinitic\",\n            \"HIGH\",\n            0.79,\n            \"L56\",\n            0.812,\n            -0.58,\n            0.003\n          ],\n          [\n            \"es\",\n            \"Romance\",\n            \"HIGH\",\n            0.78,\n            \"L60\",\n            0.821,\n            -0.53,\n            0.008\n          ],\n          [\n            \"ja\",\n            \"Japonic\",\n            \"HIGH\",\n            0.75,\n            \"L52\",\n            0.802,\n            -0.62,\n            0.001\n          ],\n          [\n            \"hi\",\n            \"Indo-Aryan\",\n            \"MID\",\n            0.73,\n            \"L48\",\n            0.789,\n            -0.67,\n            \"<0.001\"\n          ],\n          [\n            \"ko\",\n            \"Koreanic\",\n            \"MID\",\n            0.73,\n            \"L52\",\n            0.802,\n            -0.61,\n            0.002\n          ],\n          [\n            \"ar\",\n            \"Semitic\",\n            \"MID\",\n            0.72,\n            \"L52\",\n            0.802,\n            -0.59,\n            0.003\n          ],\n          [\n            \"sw\",\n            \"Bantu\",\n            \"LOW\",\n            0.65,\n            \"L40\",\n            0.762,\n            -0.79,\n            \"<0.001\"\n          ],\n          [\n            \"yo\",\n            \"Volta-Niger\",\n            \"LOW\",\n            0.61,\n            \"L36\",\n            0.721,\n            -0.82,\n            \"<0.001\"\n          ],\n          [\n            \"am\",\n            \"Ethiosemitic\",\n            \"LOW\",\n            0.598,\n            \"L36\",\n            0.721,\n            -0.81,\n            \"<0.001\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: Transfer Conditions Comparison (Qwen3-235B, L56 Pareto Zone)\",\n        \"columns\": [\n          \"Condition\",\n          \"AUROC_Avg_20L\",\n          \"AUROC_HIGH\",\n          \"AUROC_MID\",\n          \"AUROC_LOW\",\n          \"ECE_Avg\"\n        ],\n        \"rows\": [\n          [\n            \"Zero-shot\",\n            0.728,\n            0.773,\n            0.726,\n            0.648,\n            0.165\n          ],\n          [\n            \"Mean-shift\",\n            0.728,\n            0.773,\n            0.726,\n            0.648,\n            0.168\n          ],\n          [\n            \"Linear_proj_50\",\n            0.79,\n            0.821,\n            0.789,\n            0.728,\n            0.139\n          ],\n          [\n            \"Few-shot_25\",\n            0.745,\n            0.789,\n            0.742,\n            0.668,\n            0.152\n          ],\n          [\n            \"Few-shot_100\",\n            0.774,\n            0.811,\n            0.773,\n            0.702,\n            0.136\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Qwen3-235B 呈现教科书级 Pareto frontier。关键发现：(1) ρ=-0.65 远强于 MVP\\n7B 的约 -0.4，confirming 更大模型 → 更 structured representations → 更清晰\\ntradeoff；(2) transfer-optimal zone 在 40-60% depth (L36-L56)，EN-optimal 在\\n77% (L72)，gap = 16 层；(3) resource tier gradient: HIGH 0.77 > MID 0.72 > LOW\\n0.64，三级分明；(4) 19/20 languages transfer 成功，仅 am 失败。Linear proj\\n(50 pairs) 是最强迁移方法 (+6.2pp over ZS)，few-shot 100 紧随 (+4.6pp)。\\n\\n\\n235B MoE 拥有远比 7B 更结构化的内部表征。MVP Qwen2.5-7B EN best AUROC = 0.754;\\n235B 的 correctness direction 在中高层 (L48-L72) 线性可分度大幅提升至 0.83，\\n与 probing 文献中 \\\"larger model → more linearly accessible features\\\" 的规律一致。\\n更大模型的多语言预训练数据量级增加约 5-10x，跨语言对齐更强，zero-shot transfer\\navg 从 MVP ~0.65 提升至 ~0.71。94 层结构提供精细 depth 分辨率：EN-optimal L72\\n(77% depth) 与 transfer-optimal zone L52-56 (55-60% depth) 间有 ~16 层间距，\\n产生清晰的强负相关 ρ ≈ -0.65。低资源语言的 ρ 更负 (sw -0.79, yo -0.82)，\\n因为这些语言在深层的表征特化最剧烈——模型的 language-specific expert routing\\n在深层对高资源语言保持跨语言共享，但对低资源语言已切换至 language-specific pathway。\\nMean-shift AUROC delta 严格为零 (数学证明: StandardScaler + LR → 常数偏移 → rank\\n不变 → AUROC 不变)。仅 am (Amharic) 以 0.598 未达 0.60 阈值，因为 Qwen3 的\\nAmharic 预训练数据极少。\\n\"\n  },\n  {\n    \"name\": \"Llama 4 Scout Full Pareto Frontier\",\n    \"description\": \"48层 MoE (W4A16), 12 probed layers, 20语言, 4 transfer conditions\",\n    \"results\": {\n      \"en_best_auroc\": 0.811,\n      \"en_best_layer\": 40,\n      \"en_auroc_range\": [\n        0.574,\n        0.811\n      ],\n      \"en_best_ece_raw\": 0.139,\n      \"zs_transfer_auroc_avg_20lang\": 0.684,\n      \"zs_transfer_success_rate\": 0.85,\n      \"zs_fail_langs\": [\n        \"yo\",\n        \"my\",\n        \"am\"\n      ],\n      \"pareto_spearman_rho_global\": -0.33,\n      \"pareto_spearman_rho_per_lang_range\": [\n        -0.68,\n        0.18\n      ],\n      \"zs_auroc_by_tier\": {\n        \"HIGH_avg\": 0.743,\n        \"MID_avg\": 0.694,\n        \"LOW_avg\": 0.602\n      },\n      \"zs_best_by_lang\": {\n        \"zh\": {\n          \"auroc\": 0.76,\n          \"best_layer\": 36\n        },\n        \"es\": {\n          \"auroc\": 0.75,\n          \"best_layer\": 36\n        },\n        \"fr\": {\n          \"auroc\": 0.74,\n          \"best_layer\": 32\n        },\n        \"de\": {\n          \"auroc\": 0.74,\n          \"best_layer\": 36\n        },\n        \"ja\": {\n          \"auroc\": 0.72,\n          \"best_layer\": 32\n        },\n        \"pt\": {\n          \"auroc\": 0.75,\n          \"best_layer\": 36\n        },\n        \"it\": {\n          \"auroc\": 0.74,\n          \"best_layer\": 36\n        },\n        \"hi\": {\n          \"auroc\": 0.7,\n          \"best_layer\": 36\n        },\n        \"ru\": {\n          \"auroc\": 0.72,\n          \"best_layer\": 40\n        },\n        \"ko\": {\n          \"auroc\": 0.71,\n          \"best_layer\": 40\n        },\n        \"tr\": {\n          \"auroc\": 0.67,\n          \"best_layer\": 32\n        },\n        \"vi\": {\n          \"auroc\": 0.69,\n          \"best_layer\": 32\n        },\n        \"ar\": {\n          \"auroc\": 0.7,\n          \"best_layer\": 40\n        },\n        \"th\": {\n          \"auroc\": 0.67,\n          \"best_layer\": 28\n        },\n        \"sw\": {\n          \"auroc\": 0.62,\n          \"best_layer\": 28\n        },\n        \"bn\": {\n          \"auroc\": 0.63,\n          \"best_layer\": 28\n        },\n        \"yo\": {\n          \"auroc\": 0.57,\n          \"best_layer\": 24\n        },\n        \"te\": {\n          \"auroc\": 0.64,\n          \"best_layer\": 28\n        },\n        \"my\": {\n          \"auroc\": 0.58,\n          \"best_layer\": 24\n        },\n        \"am\": {\n          \"auroc\": 0.57,\n          \"best_layer\": 24\n        }\n      },\n      \"depth_transfer_snapshot\": {\n        \"en_at_L40\": 0.811,\n        \"zs_avg_at_L40\": 0.654,\n        \"en_at_L32\": 0.781,\n        \"zs_avg_at_L32\": 0.691,\n        \"en_at_L24\": 0.732,\n        \"zs_avg_at_L24\": 0.682\n      },\n      \"langs_with_positive_depth_rho\": [\n        \"ru\",\n        \"ko\",\n        \"ar\"\n      ],\n      \"mean_shift_delta_auroc\": 0.0,\n      \"linear_proj_50_delta_auroc_avg\": 0.058,\n      \"fewshot_25_auroc_avg\": 0.706,\n      \"fewshot_100_auroc_avg\": 0.741\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Llama 4 Scout Pareto Frontier — Per-Language Summary\",\n        \"columns\": [\n          \"Language\",\n          \"Family\",\n          \"Resource\",\n          \"Best_ZS_AUROC\",\n          \"Best_ZS_Layer\",\n          \"Spearman_rho\",\n          \"rho_p\"\n        ],\n        \"representative_rows\": [\n          [\n            \"zh\",\n            \"Sinitic\",\n            \"HIGH\",\n            0.76,\n            \"L36\",\n            -0.45,\n            0.14\n          ],\n          [\n            \"es\",\n            \"Romance\",\n            \"HIGH\",\n            0.75,\n            \"L36\",\n            -0.41,\n            0.18\n          ],\n          [\n            \"ru\",\n            \"Slavic\",\n            \"MID\",\n            0.72,\n            \"L40\",\n            0.05,\n            0.88\n          ],\n          [\n            \"ko\",\n            \"Koreanic\",\n            \"MID\",\n            0.71,\n            \"L40\",\n            0.18,\n            0.57\n          ],\n          [\n            \"ar\",\n            \"Semitic\",\n            \"MID\",\n            0.7,\n            \"L40\",\n            -0.12,\n            0.71\n          ],\n          [\n            \"sw\",\n            \"Bantu\",\n            \"LOW\",\n            0.62,\n            \"L28\",\n            -0.62,\n            0.03\n          ],\n          [\n            \"yo\",\n            \"Volta-Niger\",\n            \"LOW\",\n            0.57,\n            \"L24\",\n            -0.68,\n            0.02\n          ],\n          [\n            \"am\",\n            \"Ethiosemitic\",\n            \"LOW\",\n            0.57,\n            \"L24\",\n            -0.65,\n            0.02\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Llama 4 Scout 的 Pareto 显著弱于 Qwen3-235B，core finding: architecture\\ndetermines tradeoff shape。ρ_Qwen=-0.65 vs ρ_Llama=-0.33, 且 Llama 呈现\\nlanguage-specific 异质性 (3 种语言 ρ > 0)。这不是 Pareto 不存在——global ρ\\n仍为负——而是 tradeoff 在不同语言上表现不同。论文中框架为 \\\"strong vs weak\\nPareto\\\" 的架构对比。\\n\\n\\nLlama 4 Scout (17B active × 16 experts, ~109B total) 的 EN AUROC 达到 0.811，\\n低于 Qwen3-235B 但显著高于 MVP Llama-3.1-8B (0.728)。Pareto frontier 呈弱\\n负相关 ρ ≈ -0.33，延续 MVP 中 Llama 架构的模式：部分语言 (ru, ko, ar) 随\\ndepth 增加迁移不退化甚至略微改善 (ρ > 0)，而 sw/yo/am 退化严重 (ρ < -0.60)。\\n这种异质性源于 Llama 4 的 16-expert MoE routing：对 ru/ko/ar 等中高资源语言，\\n深层 expert routing 倾向于重用与 English 共享的 expert；对低资源语言则分配到\\nspecialized expert，导致表征分离。三种低资源语言 (yo 0.57, my 0.58, am 0.57)\\n未通过 0.60 阈值，success rate 17/20 = 0.85 达到 best tier 下限。48 层仅\\n12 probed layers，depth 分辨率低于 Qwen3 (24 layers)，ρ 估计的统计功效较低\\n(n=12 vs n=24)。\\n\"\n  },\n  {\n    \"name\": \"CaCLR Full Evaluation\",\n    \"description\": \"L_CaCLR = L_BCE + α·L_SB-ECE + β·L_MMD, 两种架构×20语言完整评估\",\n    \"results\": {\n      \"best_alpha\": 1.0,\n      \"best_beta\": 0.1,\n      \"alpha_sweep\": {\n        \"0.01\": {\n          \"auroc\": 0.741,\n          \"ece\": 0.148\n        },\n        \"0.1\": {\n          \"auroc\": 0.749,\n          \"ece\": 0.138\n        },\n        \"1.0\": {\n          \"auroc\": 0.763,\n          \"ece\": 0.121\n        },\n        \"10.0\": {\n          \"auroc\": 0.752,\n          \"ece\": 0.128\n        }\n      },\n      \"beta_sweep\": {\n        \"0.0\": {\n          \"auroc\": 0.724,\n          \"ece\": 0.148\n        },\n        \"0.001\": {\n          \"auroc\": 0.728,\n          \"ece\": 0.145\n        },\n        \"0.01\": {\n          \"auroc\": 0.738,\n          \"ece\": 0.137\n        },\n        \"0.1\": {\n          \"auroc\": 0.763,\n          \"ece\": 0.121\n        },\n        \"1.0\": {\n          \"auroc\": 0.731,\n          \"ece\": 0.141\n        }\n      },\n      \"qwen_L56_pareto_zone\": {\n        \"caclr_auroc_avg\": 0.763,\n        \"zeroshot_auroc_avg\": 0.728,\n        \"delta_auroc\": 0.035,\n        \"caclr_ece_avg\": 0.121,\n        \"tempscaling_ece_avg\": 0.155,\n        \"delta_ece_vs_tempscaling\": -0.034\n      },\n      \"qwen_L72_en_optimal\": {\n        \"caclr_auroc_avg\": 0.728,\n        \"zeroshot_auroc_avg\": 0.672,\n        \"delta_auroc\": 0.056,\n        \"caclr_ece_avg\": 0.132,\n        \"tempscaling_ece_avg\": 0.171,\n        \"delta_ece_vs_tempscaling\": -0.039\n      },\n      \"qwen_oracle_per_lang\": {\n        \"caclr_auroc_avg\": 0.76,\n        \"zeroshot_auroc_avg\": 0.713,\n        \"delta_auroc\": 0.047\n      },\n      \"llama_L32_pareto_zone\": {\n        \"caclr_auroc_avg\": 0.732,\n        \"zeroshot_auroc_avg\": 0.691,\n        \"delta_auroc\": 0.041,\n        \"caclr_ece_avg\": 0.131,\n        \"tempscaling_ece_avg\": 0.163,\n        \"delta_ece_vs_tempscaling\": -0.032\n      },\n      \"llama_L40_en_optimal\": {\n        \"caclr_auroc_avg\": 0.697,\n        \"zeroshot_auroc_avg\": 0.654,\n        \"delta_auroc\": 0.043,\n        \"caclr_ece_avg\": 0.142,\n        \"tempscaling_ece_avg\": 0.176,\n        \"delta_ece_vs_tempscaling\": -0.034\n      },\n      \"ablation\": {\n        \"bce_only\": {\n          \"auroc\": 0.728,\n          \"ece\": 0.165\n        },\n        \"bce_sbece\": {\n          \"auroc\": 0.724,\n          \"ece\": 0.148\n        },\n        \"bce_mmd\": {\n          \"auroc\": 0.751,\n          \"ece\": 0.136\n        },\n        \"bce_sbece_mmd\": {\n          \"auroc\": 0.763,\n          \"ece\": 0.121\n        }\n      },\n      \"beta_vs_zero_paired_permutation_p\": 0.003,\n      \"beta_vs_zero_cohens_d\": 0.52,\n      \"beta_vs_zero_bootstrap_ci\": [\n        0.024,\n        0.058\n      ],\n      \"caclr_delta_by_tier\": {\n        \"HIGH\": 0.031,\n        \"MID\": 0.048,\n        \"LOW\": 0.068\n      },\n      \"pareto_rho_without_caclr\": -0.65,\n      \"pareto_rho_with_caclr\": -0.51,\n      \"pareto_shift_interpretation\": \"CaCLR 减弱 Pareto tradeoff (rho 从 -0.65 到 -0.51), 因为深层迁移退化被部分修复\",\n      \"mmd_kernel\": \"Gaussian RBF, bandwidth=median heuristic\",\n      \"optimizer\": \"Adam, lr=1e-3, cosine decay to 1e-5\",\n      \"epochs\": 50,\n      \"early_stopping\": \"patience=10, monitor val BCE loss\",\n      \"initialization\": \"warm-start from standard LR solution\",\n      \"batch_size\": 256,\n      \"mmd_items\": \"same items as BCE (probe_train portion)\",\n      \"parallel_set_size_per_lang_avg\": 630,\n      \"parallel_set_size_per_lang_min\": 580,\n      \"translation_quality_note\": \"am/yo/my translations spot-checked, ~8% semantic drift vs high-resource\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: CaCLR vs All Baselines (Fixed Layer, Pareto Zone)\",\n        \"columns\": [\n          \"Method\",\n          \"Qwen3_AUROC\",\n          \"Qwen3_ECE\",\n          \"Llama4_AUROC\",\n          \"Llama4_ECE\",\n          \"Labels_Required\"\n        ],\n        \"rows\": [\n          [\n            \"Zero-shot\",\n            0.728,\n            0.165,\n            0.691,\n            0.179,\n            \"EN only\"\n          ],\n          [\n            \"Mean-shift\",\n            0.728,\n            0.168,\n            0.691,\n            0.183,\n            \"EN only\"\n          ],\n          [\n            \"Temp scaling\",\n            0.728,\n            0.155,\n            0.691,\n            0.163,\n            \"EN only\"\n          ],\n          [\n            \"CaCLR (α=1 β=0.1)\",\n            0.763,\n            0.121,\n            0.732,\n            0.131,\n            \"EN only + parallel inputs\"\n          ],\n          [\n            \"Linear proj (50)\",\n            0.79,\n            0.139,\n            0.749,\n            0.146,\n            \"50 parallel pairs\"\n          ],\n          [\n            \"Few-shot (25)\",\n            0.745,\n            0.152,\n            0.712,\n            0.159,\n            \"25 target labels\"\n          ],\n          [\n            \"Few-shot (100)\",\n            0.774,\n            0.136,\n            0.745,\n            0.142,\n            \"100 target labels\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 5: Component Ablation (Qwen3-235B, L56, Avg 20 Langs)\",\n        \"columns\": [\n          \"Components\",\n          \"AUROC\",\n          \"ECE\",\n          \"Delta_AUROC_vs_ZS\"\n        ],\n        \"rows\": [\n          [\n            \"BCE only (= zero-shot)\",\n            0.728,\n            0.165,\n            \"—\"\n          ],\n          [\n            \"BCE + SB-ECE\",\n            0.724,\n            0.148,\n            -0.004\n          ],\n          [\n            \"BCE + MMD\",\n            0.751,\n            0.136,\n            0.023\n          ],\n          [\n            \"BCE + SB-ECE + MMD\",\n            0.763,\n            0.121,\n            0.035\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 6: β Sensitivity (α=1.0 fixed, Qwen3 L56)\",\n        \"columns\": [\n          \"beta\",\n          \"AUROC\",\n          \"ECE\",\n          \"Delta_vs_beta0\"\n        ],\n        \"rows\": [\n          [\n            0.0,\n            0.724,\n            0.148,\n            \"—\"\n          ],\n          [\n            0.001,\n            0.728,\n            0.145,\n            0.004\n          ],\n          [\n            0.01,\n            0.738,\n            0.137,\n            0.014\n          ],\n          [\n            0.1,\n            0.763,\n            0.121,\n            0.039\n          ],\n          [\n            1.0,\n            0.731,\n            0.141,\n            0.007\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"β > 0 统计显著地改善跨语言迁移 (p=0.003, d=0.52)。CaCLR 的核心价值：完全不需要\\ntarget-language correctness labels，仅需 parallel inputs (已通过 GlobalMMLU\\n翻译存在)。CaCLR 未超过 linear projection (50 pairs): 0.763 vs 0.790，但\\nCaCLR 无需 paired correctness labels。Two methods 互补：CaCLR 适用于无 parallel\\npairs 的场景，linear projection 在有少量 parallel data 时更优。CaCLR 在深层\\n(EN-optimal) 增益更大 (+0.056) 证明它 shifts Pareto frontier，不只是 uniform\\nimprovement。ECE reduction 22% vs temp scaling 构成论文 headline。\\n\\n\\nBest tier 核心假设：\\\"MMD on probe logits 成功对齐 correctness subspace cross-\\nlingually\\\"。为何成立：(1) 235B 模型的 correctness direction 占据低维语言无关\\n子空间 (CKA 分析支持)，因此 1D probe logit 的分布差异主要反映 subspace rotation\\n而非 intrinsic signal difference；MMD 通过匹配 logit 分布有效纠正这个 rotation。\\n(2) β=0.1 是 sweet spot——足以施加对齐压力 (MMD loss ~0.3 量级) 但不 overwhelm\\nBCE loss (初始 ~0.65 量级)；β=1.0 过大导致 MMD dominate，probe 为匹配分布而\\n牺牲判别力。(3) SB-ECE 单独贡献有限 (+0.006 AUROC)，但与 MMD 叠加有协同：\\nSB-ECE 改善 probability calibration 后，MMD 在更好校准的 logit 空间上匹配更\\n有效。(4) 低资源语言获益最大 (+0.068)，因为 zero-shot distribution gap 最大，\\nMMD 的边际对齐收益最高——与 Ben-David et al. H-divergence 理论一致。(5) 在\\nEN-optimal 深层 L72，CaCLR 增益更大 (+0.056 > +0.035)，因为深层迁移退化更\\n严重，recovery space 更大——直接证明 \\\"CaCLR shifts the Pareto frontier\\\"。\\n统计显著性: paired permutation test p=0.003, Cohen's d=0.52 (medium effect),\\nbootstrap 95% CI [0.024, 0.058] 不含零。\\n\"\n  },\n  {\n    \"name\": \"Difficulty-Controlled Decomposition\",\n    \"description\": \"IRT difficulty probe → project out → retrain → transfer delta. 10 langs × 8 layers × 2 models\",\n    \"results\": {\n      \"difficulty_probe_r2_avg\": 0.61,\n      \"difficulty_probe_r2_range\": [\n        0.43,\n        0.76\n      ],\n      \"difficulty_probe_r2_by_lang\": {\n        \"zh\": 0.72,\n        \"es\": 0.76,\n        \"de\": 0.68,\n        \"fr\": 0.71,\n        \"hi\": 0.58,\n        \"ru\": 0.65,\n        \"ko\": 0.63,\n        \"tr\": 0.53,\n        \"sw\": 0.43,\n        \"bn\": 0.47\n      },\n      \"avg_transfer_delta_after_projection\": 0.035,\n      \"delta_by_lang_category\": {\n        \"capability_dominated\": {\n          \"langs\": [\n            \"zh\",\n            \"es\",\n            \"fr\",\n            \"de\",\n            \"ru\",\n            \"ko\"\n          ],\n          \"delta\": 0.042,\n          \"ci\": [\n            0.031,\n            0.054\n          ]\n        },\n        \"difficulty_dominated\": {\n          \"langs\": [\n            \"hi\",\n            \"tr\",\n            \"sw\",\n            \"bn\"\n          ],\n          \"delta\": -0.018,\n          \"ci\": [\n            -0.029,\n            -0.007\n          ]\n        }\n      },\n      \"random_projection_delta_avg\": -0.003,\n      \"random_projection_delta_std\": 0.008,\n      \"random_projection_delta_ci\": [\n        -0.011,\n        0.005\n      ],\n      \"delta_by_depth\": {\n        \"20%\": 0.012,\n        \"35%\": 0.021,\n        \"50%\": 0.035,\n        \"65%\": 0.043,\n        \"80%\": 0.051,\n        \"90%\": 0.048\n      },\n      \"qwen_avg_delta\": 0.038,\n      \"llama_avg_delta\": 0.031,\n      \"predicted_vs_actual_alignment_strategy_accuracy\": 0.82\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Difficulty Decomposition Effect by Language Category\",\n        \"columns\": [\n          \"Category\",\n          \"Languages\",\n          \"N_langs\",\n          \"Delta_AUROC\",\n          \"CI_95\",\n          \"Random_Control\"\n        ],\n        \"rows\": [\n          [\n            \"Capability-dominated\",\n            \"zh/es/fr/de/ru/ko\",\n            6,\n            0.042,\n            \"[0.031, 0.054]\",\n            -0.002\n          ],\n          [\n            \"Difficulty-dominated\",\n            \"hi/tr/sw/bn\",\n            4,\n            -0.018,\n            \"[-0.029, -0.007]\",\n            -0.004\n          ],\n          [\n            \"Overall\",\n            \"all 10\",\n            10,\n            0.035,\n            \"[0.021, 0.049]\",\n            -0.003\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 8: Depth × Decomposition Interaction\",\n        \"columns\": [\n          \"Depth_Pct\",\n          \"EN_Probe_AUROC\",\n          \"ZS_Delta_After_Proj\",\n          \"ZS_Delta_Capability_Only\",\n          \"ZS_Delta_Difficulty_Only\"\n        ],\n        \"rows\": [\n          [\n            \"20%\",\n            0.65,\n            0.012,\n            0.018,\n            -0.008\n          ],\n          [\n            \"50%\",\n            0.78,\n            0.035,\n            0.042,\n            -0.016\n          ],\n          [\n            \"80%\",\n            0.82,\n            0.051,\n            0.061,\n            -0.023\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Decomposition 成功分离 difficulty/capability，fulfilling Claim 2。Prescriptive\\nvalue: 对于 capability-dominated 语言 (baseline ZS > ~0.70)，projecting out\\ndifficulty 是 free lunch (+4.2pp)。对于 difficulty-dominated 语言 (baseline ZS\\n< ~0.65)，应保留 difficulty 信号。82% prediction accuracy 表明这个规则可\\n自动化为 per-language strategy selector。\\n\\n\\nCorrectness signal 是 difficulty (跨语言共享——哪些题目本身更难) 和 capability\\n(语言特异性——模型在该语言上的推理能力) 的纠缠。对于 capability-dominated 语言\\n(高资源, 模型具备强推理)，difficulty 是共享但无用的噪声维度：projecting out\\n移除了对迁移有害的 confound，暴露纯粹的 capability signal，transfer 改善\\n+4.2pp。对于 difficulty-dominated 语言 (低资源, 模型 capability 弱)，difficulty\\n本身是 correctness 的主要来源 (模型答对题目主要靠题目简单，而非语言能力)——\\n移除它丢失了唯一可迁移的信号，transfer 下降 -1.8pp。深层 delta 更大 (80%\\ndepth: +5.1pp vs 20%: +1.2pp)，因为 capability 特化在深层更强，difficulty\\nconfound 的 relative 权重在深层更大。Random direction control 的 delta ≈ 0\\n排除了纯降维的 artifact。IRT difficulty probe R² 呈 resource gradient (zh 0.72\\n> sw 0.43)，因为 IRT difficulty scores 基于高资源语言的人类答题数据，低资源\\n语言的 difficulty 编码较弱。Prescriptive accuracy 82% 表明 decomposition\\n能正确预测 8/10 语言应该用哪种 alignment strategy。\\n\"\n  },\n  {\n    \"name\": \"Cross-Lingual Orthogonality\",\n    \"description\": \"Correctness vs verbalized confidence direction cosine similarity, 20 langs × 2 archs\",\n    \"results\": {\n      \"cosine_range\": [\n        0.012,\n        0.058\n      ],\n      \"cosine_mean\": 0.032,\n      \"cosine_std\": 0.013,\n      \"cosine_by_tier\": {\n        \"HIGH\": 0.027,\n        \"MID\": 0.033,\n        \"LOW\": 0.04\n      },\n      \"cosine_by_arch\": {\n        \"Qwen3\": 0.029,\n        \"Llama4\": 0.035\n      },\n      \"cosine_extremes\": {\n        \"min\": {\n          \"lang\": \"es\",\n          \"arch\": \"Qwen3\",\n          \"value\": 0.012\n        },\n        \"max\": {\n          \"lang\": \"am\",\n          \"arch\": \"Llama4\",\n          \"value\": 0.058\n        }\n      },\n      \"cosine_per_lang\": {\n        \"en\": {\n          \"qwen\": 0.023,\n          \"llama\": 0.03\n        },\n        \"zh\": {\n          \"qwen\": 0.021,\n          \"llama\": 0.028\n        },\n        \"es\": {\n          \"qwen\": 0.012,\n          \"llama\": 0.024\n        },\n        \"hi\": {\n          \"qwen\": 0.032,\n          \"llama\": 0.039\n        },\n        \"sw\": {\n          \"qwen\": 0.042,\n          \"llama\": 0.049\n        },\n        \"am\": {\n          \"qwen\": 0.048,\n          \"llama\": 0.058\n        }\n      },\n      \"permutation_test_vs_random_p\": \"<0.001\",\n      \"cosine_vs_resource_rho\": 0.34,\n      \"cosine_vs_resource_p\": 0.042\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: Correctness-Confidence Orthogonality Across Languages\",\n        \"columns\": [\n          \"Language\",\n          \"Resource\",\n          \"Qwen3_Cosine\",\n          \"Llama4_Cosine\",\n          \"Average\"\n        ],\n        \"representative_rows\": [\n          [\n            \"en\",\n            \"—\",\n            0.023,\n            0.03,\n            0.027\n          ],\n          [\n            \"zh\",\n            \"HIGH\",\n            0.021,\n            0.028,\n            0.025\n          ],\n          [\n            \"es\",\n            \"HIGH\",\n            0.012,\n            0.024,\n            0.018\n          ],\n          [\n            \"hi\",\n            \"MID\",\n            0.032,\n            0.039,\n            0.036\n          ],\n          [\n            \"ko\",\n            \"MID\",\n            0.028,\n            0.035,\n            0.032\n          ],\n          [\n            \"sw\",\n            \"LOW\",\n            0.042,\n            0.049,\n            0.046\n          ],\n          [\n            \"am\",\n            \"LOW\",\n            0.048,\n            0.058,\n            0.053\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Claim 4 完全成立。Output-based calibration 的结构性限制是跨语言普遍的——\\n所有 40 个 (language, architecture) 组合的 cosine < 0.06。Resource tier 与\\ncosine 弱正相关 (ρ=0.34, p=0.042)，但 effect size 极小 (range 仅 0.013)。\\n这进一步 motivate probe-based calibration：output 层面的信息理论限制不随\\n语言变化。\\n\\n\\nCorrectness 和 verbalized confidence 的正交性 (cosine < 0.06) 是 transformer\\n架构的内在特征：模型学会了在独立的表征子空间中编码 \\\"我是否答对了\\\" (correctness)\\n和 \\\"我认为我有多确定\\\" (confidence)。这不是 English-specific 现象。正交性在\\n所有 20 种语言上持续成立，因为两个方向都由模型的参数化决定，不由输入语言决定。\\n低资源语言的 cosine 略高 (0.040 vs 0.027) 有两个原因：(1) confidence probe\\n在低资源语言上的 SNR 更低，噪声使 cosine 估计偏离零；(2) 低资源语言的表征\\n空间利用率低，两个方向在低维子空间中更容易有 spurious overlap。但即使最高\\n的 am=0.058 仍远低于表示有意义相关性的阈值 (~0.2)。\\n\"\n  },\n  {\n    \"name\": \"Probe Complexity Comparison\",\n    \"description\": \"Logistic regression vs 2-layer MLP: EN accuracy 和 cross-lingual transfer 对比\",\n    \"results\": {\n      \"lr_en_best_auroc\": 0.832,\n      \"mlp_en_best_auroc\": 0.851,\n      \"mlp_en_advantage\": 0.019,\n      \"lr_zs_auroc_avg\": 0.713,\n      \"mlp_zs_auroc_avg\": 0.685,\n      \"lr_zs_advantage\": 0.028,\n      \"lr_relative_degradation\": 0.143,\n      \"mlp_relative_degradation\": 0.195,\n      \"mlp_excess_degradation\": 0.052,\n      \"lr_zs_low\": 0.635,\n      \"mlp_zs_low\": 0.581,\n      \"lr_vs_mlp_gap_low\": 0.054,\n      \"lr_zs_high\": 0.773,\n      \"mlp_zs_high\": 0.752,\n      \"lr_vs_mlp_gap_high\": 0.021,\n      \"lr_ece_avg\": 0.165,\n      \"mlp_ece_avg\": 0.184\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S3: Probe Complexity × Transfer\",\n        \"columns\": [\n          \"Metric\",\n          \"LR\",\n          \"MLP_2layer\",\n          \"Delta\"\n        ],\n        \"rows\": [\n          [\n            \"EN Best AUROC\",\n            0.832,\n            0.851,\n            0.019\n          ],\n          [\n            \"ZS Transfer Avg 20L\",\n            0.713,\n            0.685,\n            -0.028\n          ],\n          [\n            \"Relative Degradation\",\n            \"14.3%\",\n            \"19.5%\",\n            \"+5.2pp\"\n          ],\n          [\n            \"ZS Low-Resource Avg\",\n            0.635,\n            0.581,\n            -0.054\n          ],\n          [\n            \"ECE Avg\",\n            0.165,\n            0.184,\n            0.019\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Linear probe 是跨语言 transfer 的正确选择。MLP 的 +1.9pp English 优势远不足以\\n补偿 -2.8pp transfer 劣势。论文中以此证明 LR 作为默认 probe 的合理性。\\n\\n\\nMLP 在 English 上略优 (+1.9pp) 是因为 correctness signal 含有弱非线性成分——\\n某些层的 correctness 编码涉及特征交互。但 MLP 同时学到了 English-specific 的\\n非线性 pattern (e.g. English-specific token position interactions)，这些 pattern\\n在目标语言中不存在，导致 transfer 时引入负迁移。Linear probe 的 inductive bias\\n恰好匹配 correctness direction 的跨语言结构：线性投影只能捕获方向性信息，\\n而方向性信息正是跨语言共享的 (CKA 子空间分析支持)。差距在低资源语言最大\\n(LR +5.4pp vs MLP)，因为低资源表征的线性结构相对于英语更保守 (低维对齐\\n更强)，而 MLP 学到的非线性 feature 在低资源语境下完全失效。\\n\"\n  },\n  {\n    \"name\": \"Additional Benchmarks (Belebele + MMLU-ProX)\",\n    \"description\": \"最优 probes + CaCLR 在 Belebele 和 MMLU-ProX 上的泛化验证\",\n    \"results\": {\n      \"belebele_qwen_en_auroc\": 0.814,\n      \"belebele_qwen_zs_avg\": 0.698,\n      \"belebele_qwen_caclr_avg\": 0.741,\n      \"belebele_qwen_pareto_rho\": -0.61,\n      \"belebele_llama_en_auroc\": 0.793,\n      \"belebele_llama_zs_avg\": 0.671,\n      \"belebele_llama_caclr_avg\": 0.712,\n      \"mmlupx_qwen_en_auroc\": 0.839,\n      \"mmlupx_qwen_zs_avg\": 0.721,\n      \"mmlupx_qwen_caclr_avg\": 0.767,\n      \"mmlupx_qwen_pareto_rho\": -0.67,\n      \"mmlupx_llama_en_auroc\": 0.818,\n      \"mmlupx_llama_zs_avg\": 0.694,\n      \"mmlupx_llama_caclr_avg\": 0.738,\n      \"per_lang_rank_corr_gmmlu_belebele\": 0.89,\n      \"per_lang_rank_corr_gmmlu_mmlupx\": 0.93\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Cross-Benchmark Generalization (Qwen3-235B)\",\n        \"columns\": [\n          \"Benchmark\",\n          \"Domain\",\n          \"EN_AUROC\",\n          \"ZS_Avg\",\n          \"CaCLR_Avg\",\n          \"Pareto_rho\",\n          \"CaCLR_Delta\"\n        ],\n        \"rows\": [\n          [\n            \"GlobalMMLU\",\n            \"Knowledge QA\",\n            0.832,\n            0.713,\n            0.76,\n            -0.65,\n            0.047\n          ],\n          [\n            \"Belebele\",\n            \"Reading Comp\",\n            0.814,\n            0.698,\n            0.741,\n            -0.61,\n            0.043\n          ],\n          [\n            \"MMLU-ProX\",\n            \"Knowledge QA\",\n            0.839,\n            0.721,\n            0.767,\n            -0.67,\n            0.046\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"三 benchmark 一致性强。Pareto frontier 和 CaCLR gains 跨 domain replicate。\\nBelebele 的略低结果 underscores domain dependency 但不 undermine core claims。\\n\\n\\nBelebele 是 reading comprehension，与 GlobalMMLU (knowledge QA) 的 domain 不同。\\nCorrectness direction 有轻微 domain dependency：probe 在 knowledge-heavy items\\n上学到的 correctness signal 不完全迁移到 comprehension tasks，EN AUROC 略降\\n(0.814 vs 0.832)。但 Pareto 结构高度一致 (ρ=-0.61 vs -0.65)，因为 depth-\\ntransferability tradeoff 是架构特征而非 task 特征。MMLU-ProX 与 GlobalMMLU\\ndomain overlap 大 (同属 knowledge QA)，结果最相似。Per-language ranking 跨\\nbenchmark 高度稳定 (ρ=0.89-0.93)——在 GlobalMMLU 上 transfer 好的语言在\\nBelebele 上也好。CaCLR 增益在 Belebele 上略小 (+4.3pp vs +4.7pp) 但仍正面。\\n\"\n  },\n  {\n    \"name\": \"Quantization Validation\",\n    \"description\": \"W4A16 vs FP16 (Llama) + GPTQ-INT4 vs FP16 (Qwen), 5 layers, 5% subset\",\n    \"results\": {\n      \"llama_w4a16_vs_fp16\": {\n        \"auroc_diff_avg\": 0.004,\n        \"auroc_diff_max\": 0.008,\n        \"auroc_diff_per_layer\": {\n          \"L8\": 0.002,\n          \"L16\": 0.003,\n          \"L24\": 0.005,\n          \"L32\": 0.006,\n          \"L40\": 0.008\n        },\n        \"cka_quantized_vs_fp16\": 0.987,\n        \"paired_t_p\": 0.31\n      },\n      \"qwen_int4_vs_fp16\": {\n        \"auroc_diff_avg\": 0.006,\n        \"auroc_diff_max\": 0.013,\n        \"auroc_diff_per_layer\": {\n          \"L16\": 0.003,\n          \"L32\": 0.005,\n          \"L48\": 0.006,\n          \"L64\": 0.008,\n          \"L80\": 0.013\n        },\n        \"cka_quantized_vs_fp16\": 0.981,\n        \"paired_t_p\": 0.18\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S4: Quantization Validation\",\n        \"columns\": [\n          \"Model\",\n          \"Quantization\",\n          \"Avg_Delta_AUROC\",\n          \"Max_Delta_AUROC\",\n          \"CKA\",\n          \"Paired_t_p\"\n        ],\n        \"rows\": [\n          [\n            \"Llama 4 Scout\",\n            \"W4A16\",\n            0.004,\n            0.008,\n            0.987,\n            0.31\n          ],\n          [\n            \"Qwen3-235B\",\n            \"GPTQ-INT4\",\n            0.006,\n            0.013,\n            0.981,\n            0.18\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"量化不影响核心结论。最大偏差 1.3pp 远小于实验主要效应 (Pareto gap ~6pp,\\nCaCLR gain ~4.5pp)。放入 appendix 即可。\\n\\n\\nW4A16 仅压缩权重 (4-bit)，激活保持 16-bit，因此对 correctness direction (线性\\nprobe 的目标) 影响极小——probe 训练使用的是 activation vectors，不直接依赖权重\\n精度。GPTQ-INT4 的误差略大因为 4-bit 量化是更激进的压缩，且 Qwen3 有 94 层\\n导致误差累积更多。最大偏差 1.3pp 出现在最深层 L80 (误差在 94 层中逐层累积)。\\n所有差异在 paired t-test 下不显著 (p > 0.15)，CKA > 0.98 表示量化前后表征\\n几乎等价。论文中报告此验证可消除 reviewer \\\"INT4/W4A16 artifacts\\\" 的顾虑。\\n\"\n  },\n  {\n    \"name\": \"CKA Cross-Lingual Geometric Analysis\",\n    \"description\": \"CKA (linear kernel) 20 langs × all layers × 2 archs, partial correlation + subspace angle\",\n    \"results\": {\n      \"cka_partial_corr_controlling_depth\": 0.42,\n      \"cka_partial_corr_p\": 0.008,\n      \"same_layer_corr_by_depth\": {\n        \"25%\": {\n          \"rho\": -0.48,\n          \"p\": 0.032\n        },\n        \"50%\": {\n          \"rho\": -0.67,\n          \"p\": 0.001\n        },\n        \"75%\": {\n          \"rho\": -0.73,\n          \"p\": \"<0.001\"\n        }\n      },\n      \"n_significant_layers\": 18,\n      \"qwen_cka_cliff\": {\n        \"location\": \"L64 (68% depth)\",\n        \"cka_before\": 0.72,\n        \"cka_after\": 0.41,\n        \"drop_magnitude\": 0.31\n      },\n      \"llama_cka_pattern\": \"gradual decline, no cliff\",\n      \"llama_cka_at_L40\": 0.52,\n      \"llama_cka_at_L24\": 0.71,\n      \"qwen_pooled_rho\": -0.58,\n      \"qwen_pooled_p\": \"<0.001\",\n      \"llama_pooled_rho\": -0.43,\n      \"llama_pooled_p\": 0.002,\n      \"between_lang_rho_at_50pct_depth\": -0.67,\n      \"between_lang_p_at_50pct_depth\": 0.001,\n      \"between_lang_rho_at_75pct_depth\": -0.73,\n      \"between_lang_p_at_75pct_depth\": \"<0.001\",\n      \"correctness_subspace_angle_avg_deg\": 12.3,\n      \"correctness_subspace_angle_std_deg\": 4.8,\n      \"global_repr_angle_avg_deg\": 38.7,\n      \"global_repr_angle_std_deg\": 9.2,\n      \"subspace_angle_ratio\": 3.15,\n      \"cka_collapse_threshold\": 0.35,\n      \"langs_below_threshold_at_deepest\": [\n        \"sw\",\n        \"yo\",\n        \"am\",\n        \"my\"\n      ],\n      \"per_lang_within_rho_significant\": 14,\n      \"per_lang_within_rho_avg\": -0.48\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: CKA Partial Correlation Analysis\",\n        \"columns\": [\n          \"Analysis\",\n          \"Statistic\",\n          \"Value\",\n          \"p_value\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Raw CKA-degradation pooled\",\n            \"rho\",\n            -0.64,\n            \"<0.001\",\n            \"Confounded by depth\"\n          ],\n          [\n            \"Partial corr controlling depth\",\n            \"r\",\n            0.42,\n            0.008,\n            \"CKA adds info beyond depth\"\n          ],\n          [\n            \"Between-lang at 50% depth (n=20)\",\n            \"rho\",\n            -0.67,\n            0.001,\n            \"Strongest cross-lang test\"\n          ],\n          [\n            \"Between-lang at 75% depth (n=20)\",\n            \"rho\",\n            -0.73,\n            \"<0.001\",\n            \"Even stronger deep\"\n          ],\n          [\n            \"Within-lang avg (n=24 layers)\",\n            \"rho\",\n            -0.48,\n            \"varies\",\n            \"14/20 langs significant\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 12: Subspace Angle Analysis (Quantitative)\",\n        \"columns\": [\n          \"Measure\",\n          \"Qwen3_235B\",\n          \"Llama4_Scout\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Correctness subspace angle (avg)\",\n            \"11.2°\",\n            \"13.5°\",\n            \"Small — cross-ling shared\"\n          ],\n          [\n            \"Correctness subspace angle (std)\",\n            \"3.9°\",\n            \"5.7°\",\n            \"More variable in Llama\"\n          ],\n          [\n            \"Global representation angle (avg)\",\n            \"41.3°\",\n            \"36.1°\",\n            \"Large — language-specific\"\n          ],\n          [\n            \"Global/correctness ratio\",\n            3.69,\n            2.67,\n            \"Qwen: correctness 4x more stable\"\n          ],\n          [\n            \"CKA cliff location\",\n            \"68% depth\",\n            \"no cliff\",\n            \"Architecture difference\"\n          ],\n          [\n            \"CKA cliff magnitude\",\n            0.31,\n            \"N/A\",\n            \"Qwen only\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CKA geometric analysis 成立 (partial r=0.42, p=0.008)，支撑 \\\"geometric analysis\\\"\\nframing。三层 evidence：(1) partial correlation 证明 CKA 有 depth 以外的解释力；\\n(2) between-language correlation (ρ=-0.67) 是最直接证据；(3) subspace angle ratio\\n3.15 提供几何直觉。CKA cliff 的有/无解释 Qwen vs Llama Pareto 差异。这是\\ndiscovery 级别 finding——连接了 representation geometry 和 practical transfer。\\n\\n\\nBest tier 假设 \\\"CKA partial correlation 控制 depth 后仍显著\\\"。Partial r=0.42\\n(p=0.008) 表示 CKA 对 transfer degradation 有独立于 depth 的解释力。核心\\n机制：correctness direction 占据低维语言无关子空间 (principal angle ~12°)，\\n而全局表征差异远大 (~39°)，ratio 3.15。这意味着即使两种语言的全局表征已\\n显著分化 (CKA 下降)，correctness 子空间仍可能保持对齐——直到 CKA 跌破临界\\n阈值 ~0.35，此时全局分化足够大以至于连低维子空间也被扰动。\\nQwen3 的 CKA cliff (L64, 突降 0.31) 解释了为何 Qwen Pareto 清晰：在 cliff\\n之前 (L0-L60)，transfer 随 depth 缓慢退化；在 cliff 之后 (L64-L94)，transfer\\n急剧崩溃。这产生了强 Pareto (ρ=-0.65) 和清晰的 \\\"optimal transfer zone\\\" (L48-L60)。\\nLlama4 没有 cliff，CKA 渐降 → Pareto 弱且异质 (ρ=-0.33)。\\nBetween-language 分析 (固定层, n=20) 是最强统计检验：在 50% depth，CKA 高的\\n语言 (zh 0.82, es 0.79) transfer 好，CKA 低的 (sw 0.48, am 0.42) transfer 差，\\nρ=-0.67 (p=0.001)。在 75% depth 更强 (ρ=-0.73)，因为此处 CKA variance 更大。\\n20 languages 的密度使 per-language within-lang Spearman 首次有足够统计功效\\n(n=24 for Qwen vs MVP 的 n=9)：14/20 显著，avg ρ=-0.48，比 MVP pilot\\n(几乎全 n.s.) 大幅改善。\\n\"\n  },\n  {\n    \"name\": \"Linear Projection Sample Efficiency\",\n    \"description\": \"Parallel pairs 数量 (10-200) 对 linear projection transfer 的影响\",\n    \"results\": {\n      \"qwen_L56\": {\n        \"pairs_10\": {\n          \"auroc\": 0.739,\n          \"delta\": 0.011,\n          \"ci_width\": 0.034\n        },\n        \"pairs_20\": {\n          \"auroc\": 0.758,\n          \"delta\": 0.03,\n          \"ci_width\": 0.023\n        },\n        \"pairs_50\": {\n          \"auroc\": 0.79,\n          \"delta\": 0.062,\n          \"ci_width\": 0.015\n        },\n        \"pairs_100\": {\n          \"auroc\": 0.798,\n          \"delta\": 0.07,\n          \"ci_width\": 0.01\n        },\n        \"pairs_200\": {\n          \"auroc\": 0.802,\n          \"delta\": 0.074,\n          \"ci_width\": 0.007\n        }\n      },\n      \"llama_L32\": {\n        \"pairs_10\": {\n          \"auroc\": 0.712,\n          \"delta\": 0.021,\n          \"ci_width\": 0.031\n        },\n        \"pairs_20\": {\n          \"auroc\": 0.729,\n          \"delta\": 0.038,\n          \"ci_width\": 0.022\n        },\n        \"pairs_50\": {\n          \"auroc\": 0.749,\n          \"delta\": 0.058,\n          \"ci_width\": 0.014\n        },\n        \"pairs_100\": {\n          \"auroc\": 0.757,\n          \"delta\": 0.066,\n          \"ci_width\": 0.009\n        },\n        \"pairs_200\": {\n          \"auroc\": 0.761,\n          \"delta\": 0.07,\n          \"ci_width\": 0.006\n        }\n      },\n      \"elbow_point\": 50,\n      \"marginal_gain_50_to_100\": 0.008,\n      \"marginal_gain_100_to_200\": 0.004,\n      \"caclr_equivalent_pairs\": 35\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: Linear Projection Sample Efficiency (Qwen3, L56)\",\n        \"columns\": [\n          \"Pairs\",\n          \"AUROC_Avg\",\n          \"Delta_vs_ZS\",\n          \"Marginal_Gain\",\n          \"CI_95_Width\"\n        ],\n        \"rows\": [\n          [\n            10,\n            0.739,\n            0.011,\n            \"—\",\n            0.034\n          ],\n          [\n            20,\n            0.758,\n            0.03,\n            0.019,\n            0.023\n          ],\n          [\n            50,\n            0.79,\n            0.062,\n            0.032,\n            0.015\n          ],\n          [\n            100,\n            0.798,\n            0.07,\n            0.008,\n            0.01\n          ],\n          [\n            200,\n            0.802,\n            0.074,\n            0.004,\n            0.007\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"50 pairs 是实用甜点。Linear projection 在 50 pairs 时超过 CaCLR (0.790 vs\\n0.763)，但需要 parallel pairs with correctness labels。两方法互补：CaCLR\\nfor zero-label 场景，linear projection for minimal-data 场景。\\n\\n\\nLinear projection 学习 affine transformation 将 target 语言 correctness subspace\\n旋转对齐到 English。Correctness direction 是低维的 (实际是 1D for LR probe)，\\n因此旋转矩阵的自由度极低——50 pairs 已充分约束 (条件数稳定)。10 pairs 时 CI\\n宽 0.034 (不稳定)，50 pairs CI 收窄至 0.015。超过 50 pairs，marginal gain\\n从 +2.2pp/50pairs 骤降至 +0.8pp/50pairs 和 +0.4pp/100pairs。CaCLR (无 parallel\\npairs 的 labels) 等效于 ~35-pair linear projection (AUROC 0.763 vs pairs_35\\n插值约 0.76)，表明 MMD distributional matching 实现了部分但非完全的子空间\\n对齐。50 pairs 的实用意义大：几乎所有 GlobalMMLU 语言都有 600+ parallel items，\\n随机选 50 对即可达到 plateau。\\n\"\n  },\n  {\n    \"name\": \"Full-Scale Probing Control Tasks\",\n    \"description\": \"Hewitt & Liang control tasks, 20 langs × 2 archs × all layers (扩展 MVP English-only 结果)\",\n    \"results\": {\n      \"selectivity_below_005_fraction\": 0.1,\n      \"low_sel_distribution\": {\n        \"early_layers_pct\": 0.72,\n        \"low_resource_pct\": 0.68,\n        \"overlap_early_AND_low\": 0.54\n      },\n      \"qwen_selectivity_avg\": 0.178,\n      \"llama_selectivity_avg\": 0.152,\n      \"control_auroc_avg\": 0.491,\n      \"control_auroc_std\": 0.012,\n      \"control_auroc_max\": 0.518,\n      \"selectivity_grid_qwen\": {\n        \"early_HIGH\": 0.045,\n        \"early_MID\": 0.036,\n        \"early_LOW\": 0.019,\n        \"mid_HIGH\": 0.142,\n        \"mid_MID\": 0.118,\n        \"mid_LOW\": 0.078,\n        \"deep_HIGH\": 0.261,\n        \"deep_MID\": 0.242,\n        \"deep_LOW\": 0.188\n      },\n      \"problem_zone_cells\": 48,\n      \"total_cells\": 480,\n      \"problem_zone_pct\": 0.1,\n      \"english_selectivity_deep_layers\": 0.255,\n      \"cross_lingual_selectivity_deep_layers_avg\": 0.212,\n      \"cross_lingual_selectivity_deep_layers_low_resource\": 0.168\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S5: Selectivity by Depth × Resource Tier (Qwen3)\",\n        \"columns\": [\n          \"Depth_Range\",\n          \"HIGH_Resource\",\n          \"MID_Resource\",\n          \"LOW_Resource\"\n        ],\n        \"rows\": [\n          [\n            \"0-33% (early)\",\n            0.045,\n            0.036,\n            0.019\n          ],\n          [\n            \"33-67% (mid)\",\n            0.142,\n            0.118,\n            0.078\n          ],\n          [\n            \"67-100% (deep)\",\n            0.261,\n            0.242,\n            0.188\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"10% capacity artifact rate 在 best tier [0.05, 0.15] 范围内。核心 probing\\nresults (中深层 × 中高资源) selectivity > 0.10，genuine signal。Low-resource ×\\nearly-layer zone 应在 paper 中标注为 \\\"interpret with caution\\\"。\\n\\n\\nControl task AUROC 稳定在 ~0.49 (理论 0.50)，confirming permuted labels 不被\\nprobe 学到——probing capacity 有限，不会 memorize random labels。10% 的 grid\\ncells 有 selectivity < 0.05，集中在 (early layers, LOW resource) 象限：\\n(1) Early layers (L0-L20 Qwen / L0-L12 Llama): correctness signal 尚未形成，\\nreal probe 和 control probe 表现接近，selectivity ≈ 0；(2) Low-resource\\nlanguages: 较少的预训练数据 → correctness 编码更弱 → real probe 提升有限。\\n交叉：54% 的 low-selectivity cells 同时满足 early + low-resource。MVP 的\\nEnglish-only plan_013 结果 (selectivity 集中在 L20-L27) 与 full-scale 一致，\\n但 cross-lingual extension 揭示了资源维度——英语深层 selectivity 0.255 vs\\n低资源深层 0.168。这本身是 methodological contribution：跨语言 probing 中\\n~10% 的结果需谨慎解读。\\n\"\n  },\n  {\n    \"name\": \"Gemma 4 31B Dense — Third Architecture\",\n    \"description\": \"60层 Dense (FP16), 第三架构提供 dense vs MoE 对比\",\n    \"results\": {\n      \"en_best_auroc\": 0.821,\n      \"en_best_layer\": 48,\n      \"zs_transfer_auroc_avg_20lang\": 0.702,\n      \"zs_transfer_success_rate\": 0.9,\n      \"zs_fail_langs\": [\n        \"yo\",\n        \"am\"\n      ],\n      \"pareto_spearman_rho_global\": -0.52,\n      \"cka_pattern\": \"gradual decline, onset deeper than Llama (no cliff)\",\n      \"cka_correctness_subspace_angle_avg\": 13.1,\n      \"caclr_delta_auroc_avg\": 0.039\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 14: Three-Architecture Comparison\",\n        \"columns\": [\n          \"Architecture\",\n          \"Type\",\n          \"EN_AUROC\",\n          \"ZS_Avg\",\n          \"Pareto_rho\",\n          \"CKA_Pattern\",\n          \"CaCLR_Delta\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-235B\",\n            \"MoE (Int4)\",\n            0.832,\n            0.713,\n            -0.65,\n            \"Cliff at 68%\",\n            0.047\n          ],\n          [\n            \"Gemma4-31B\",\n            \"Dense (FP16)\",\n            0.821,\n            0.702,\n            -0.52,\n            \"Gradual, deep onset\",\n            0.039\n          ],\n          [\n            \"Llama4-Scout\",\n            \"MoE (W4A16)\",\n            0.811,\n            0.684,\n            -0.33,\n            \"Gradual, early onset\",\n            0.041\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"第三架构填充了 dense vs MoE 对比。Pareto 强度排序 (Qwen > Gemma > Llama) 与\\n架构差异一致：MoE cliff 产生最强 tradeoff，dense 渐降产生中等 tradeoff，\\n无 cliff 的 MoE 最弱。Camera-ready 的 n=3 架构虽仍不足以做因果归因 (type,\\nscale, layers, training data 均不同)，但三点一致的模式 strengthens \\\"architecture-\\ndependent tradeoff\\\" 的 observational claim。\\n\\n\\nDense 31B 没有 MoE routing，表征特化更均匀 (无 expert 分配的 language-specific\\n路径)，Pareto ρ=-0.52 介于 Qwen3 (ρ=-0.65, 强 MoE cliff) 和 Llama4 (ρ=-0.33,\\n弱 MoE) 之间。EN AUROC 0.821 反映 31B dense 的容量低于 235B 但高于 17B active。\\nCKA 渐降模式接近 Llama 但 onset 更深——dense model 在中间层保持更强的跨语言\\n共享 (无 expert routing 导致的早期分化)。Dense 架构的 Pareto 中等强度提供了\\ntheory-consistent 的三点比较：cliff MoE (Qwen) > dense (Gemma) > gradual MoE\\n(Llama)。仅 yo/am 失败 (2/20)，success rate 0.90。CaCLR delta +3.9pp 低于\\nQwen (+4.7pp) 但高于 Llama (+4.1pp)——dense 的初始 ZS transfer 已较好 (CKA\\n更高)，CaCLR 的 marginal room 稍小。\\n\"\n  },\n  {\n    \"name\": \"Extended Language Coverage (50+)\",\n    \"description\": \"扩展至 50+ 语言 (GlobalMMLU + Belebele full sets)\",\n    \"results\": {\n      \"total_languages\": 53,\n      \"zs_success_rate\": 0.83,\n      \"n_success\": 44,\n      \"n_fail\": 9,\n      \"fail_langs\": [\n        \"am\",\n        \"my\",\n        \"yo\",\n        \"si\",\n        \"lo\",\n        \"km\",\n        \"gu\",\n        \"or\",\n        \"ne\"\n      ],\n      \"pareto_rho_qwen_global_53\": -0.62,\n      \"pareto_rho_llama_global_53\": -0.31,\n      \"resource_tier_gradient_r2\": 0.71,\n      \"new_findings\": {\n        \"dravidian_cluster\": \"ta/ml/kn 形成 cluster, ZS AUROC 0.64-0.68, transfer 特征接近 MID tier\",\n        \"austronesian_cluster\": \"id/ms/tl transfer 异常好 (0.72-0.74)，因为与英语的表征对齐度高\",\n        \"uralic_outlier\": \"fi/hu ZS AUROC 差异大 (fi 0.69 vs hu 0.65)，尽管同为 Uralic\"\n      },\n      \"caclr_delta_avg_53\": 0.044,\n      \"caclr_delta_new_langs_avg\": 0.041\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S6: Extended Language Coverage Summary\",\n        \"columns\": [\n          \"Metric\",\n          \"20_Langs\",\n          \"53_Langs\"\n        ],\n        \"rows\": [\n          [\n            \"ZS Success Rate\",\n            \"95% (Qwen)\",\n            \"83%\"\n          ],\n          [\n            \"Pareto ρ Qwen\",\n            -0.65,\n            -0.62\n          ],\n          [\n            \"Pareto ρ Llama\",\n            -0.33,\n            -0.31\n          ],\n          [\n            \"Resource Gradient R²\",\n            \"~0.60\",\n            0.71\n          ],\n          [\n            \"CaCLR Δ AUROC avg\",\n            0.047,\n            0.044\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Camera-ready 扩展确认 core findings 跨 50+ 语言成立。9 种 fail 语言均为\\nextreme low-resource (预训练 tokens < 100M)，consistent with domain adaptation\\ntheory 的 H-divergence 预测。Austronesian cluster 的高 transfer 是 interesting\\nsecondary finding。\\n\\n扩展至 53 语言后，成功率从 ~90% (20 langs) 降至 83% (53 langs)，因为新增\\n语言多为 extreme low-resource (si, lo, km 等)。但 Pareto ρ 和主要 patterns\\n保持稳定 (Qwen ρ=-0.62 vs -0.65 at 20 langs)，slight reduction 因为新增的\\n低资源语言削弱了 global correlation。Resource tier gradient 在更大样本下更\\nrobust (R²=0.71, up from ~0.60 at 20 langs)。Austronesian 语言 (id/ms/tl)\\ntransfer 异常好，因为这些语言在大模型预训练中常被 grouped with English-heavy\\ncorpora (code-switching, romanization)。CaCLR 增益在新增语言上 (+4.1pp) 与\\n原 20 语言 (+4.7pp) 相当，confirming method generalizability。\\n\"\n  }\n]",
      "numLines": 1721,
      "startLine": 1,
      "totalLines": 1721
    }
  },
  "sourceToolAssistantUUID": "756292b5-6d1e-43ab-be2b-84d00c5b66c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T04:03:59.579Z_

<details><summary>↩ Tool result · `toolu_01G5rFYrsRsLZQkidhye4kgk`</summary>

```text
1	# Paper Framing — xling_calib_direction
2	
3	## Target Venue
4	- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)
5	- Core submission: 2 models × 20 languages × all contributions
6	- Camera-ready extension: Gemma 4 31B Dense + 30+ languages
7	
8	## Core Insight
9	The model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). Cross-lingual transfer degrades only when this subspace itself begins to language-specialize at the deepest layers. The resulting depth-transferability tradeoff varies across architectures (strong on Qwen, weak on Llama); CKA geometric analysis (not mechanistic explanation — correlational, must control for depth) suggests architecture-specific representation divergence rates as a factor. CaCLR tests whether distributional matching can shift this frontier without target-language labels.
10	
11	## Core Claims (4, causal chain)
12	
13	### Claim 1 — Pareto Frontier (Discovery)
14	Cross-lingual correctness probes reveal a depth-transferability tradeoff that varies across architectures: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong tradeoff); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).
15	- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).
16	- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.
17	
18	### Claim 2 — Decomposition (Analysis)
19	Cross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.
20	- Evidence: IRT difficulty probes → project out → retrain → compare transfer.
21	
22	### Claim 3 — CaCLR (Method / Diagnostic)
23	CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space — this is a design limitation worth discussing.
24	- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.
25	- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.
26	- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.
27	- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.
28	- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.
29	- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.
30	
31	### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)
32	The correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.
33	- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.
34	
35	## Story Spine
36	- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).
37	- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.
38	- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the depth-transferability tradeoff, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. A methodological warning: control task analysis reveals that ~28% of low-resource language-layer probing results are capacity artifacts (selectivity below meaningful threshold), challenging uncritical use of cross-lingual probing. This is both a field-level viability test and (depending on CaCLR results) a practical method contribution or a principled negative result.
39	- **Headline template (method success)**: "On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels."
40	- **Headline template (negative result)**: "Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines."
41	- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.
42	
43	## Field-Level Significance
44	This paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.
45	
46	## Anticipated Reviewer Concerns & Responses
47	1. **"Xiao et al. already did this"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.
48	2. **"Temperature scaling baseline"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.
49	3. **"Mean-shift too weak / why does it fail?"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.
50	4. **"Difficulty confound"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.
51	5. **"INT8 artifacts"** → Validation ablation comparing INT8 vs FP16 at representative layers.
52	6. **"Only MCQA"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.
53	7. **"Predictable from domain adaptation theory"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.
54	8. **"No statistical tests"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.
55	9. **"Probing methodology concerns"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.
56	10. **"No mechanistic explanation"** → CKA geometric analysis (framed as correlational, NOT mechanistic) provides two levels of insight: (a) between-language: languages with higher CKA show less transfer degradation; (b) between-architecture: CKA cliff steepness differs. **MUST report partial correlation controlling for normalized depth** — if CKA adds no explanatory power beyond depth, downgrade to "suggestive correlational analysis." Subspace angle analysis (quantitative, not just prose) strengthens geometric narrative.
57	11. **"Why not conformal prediction?"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.
58	12. **"CaCLR parallel activations = test leakage?"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.
59	13. **"CaCLR is your own method — self-debunking is less impactful"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.
60	14. **"CKA is correlational, not mechanistic"** → We agree and frame CKA analysis as geometric/correlational, not mechanistic. We report partial correlation controlling for depth to test whether CKA adds explanatory power beyond the trivial "deeper = worse transfer." If partial correlation is weak, we explicitly state CKA is suggestive only.
61	
62	## Additional Related Work Coverage (Dream-identified gaps)
63	- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) "On learning invariant representations for domain adaptation" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.
64	- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.
65	- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.
66	- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.
67	- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.
68	- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.
69	- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.
70	
71	## Differentiation from Closest Prior Work
72	| Paper | Their Focus | Our Difference |
73	|-------|-------------|----------------|
74	| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |
75	| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |
76	| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |
77	| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |
78	| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |
79	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69711dff-1d5a-4cb8-8537-a16dd4bd1b83",
  "isSidechain": false,
  "promptId": "21625223-a819-4abc-b0c5-9519cc481936",
  "type": "user",
  "uuid": "19e1255c-3354-4356-8f65-b96ad04be5b9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/paper_framing.md",
      "content": "# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). Cross-lingual transfer degrades only when this subspace itself begins to language-specialize at the deepest layers. The resulting depth-transferability tradeoff varies across architectures (strong on Qwen, weak on Llama); CKA geometric analysis (not mechanistic explanation — correlational, must control for depth) suggests architecture-specific representation divergence rates as a factor. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability tradeoff that varies across architectures: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong tradeoff); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\n- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space — this is a design limitation worth discussing.\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the depth-transferability tradeoff, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. A methodological warning: control task analysis reveals that ~28% of low-resource language-layer probing results are capacity artifacts (selectivity below meaningful threshold), challenging uncritical use of cross-lingual probing. This is both a field-level viability test and (depending on CaCLR results) a practical method contribution or a principled negative result.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\"\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA geometric analysis (framed as correlational, NOT mechanistic) provides two levels of insight: (a) between-language: languages with higher CKA show less transfer degradation; (b) between-architecture: CKA cliff steepness differs. **MUST report partial correlation controlling for normalized depth** — if CKA adds no explanatory power beyond depth, downgrade to \"suggestive correlational analysis.\" Subspace angle analysis (quantitative, not just prose) strengthens geometric narrative.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n13. **\"CaCLR is your own method — self-debunking is less impactful\"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.\n14. **\"CKA is correlational, not mechanistic\"** → We agree and frame CKA analysis as geometric/correlational, not mechanistic. We report partial correlation controlling for depth to test whether CKA adds explanatory power beyond the trivial \"deeper = worse transfer.\" If partial correlation is weak, we explicitly state CKA is suggestive only.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) \"On learning invariant representations for domain adaptation\" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.\n- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n",
      "numLines": 79,
      "startLine": 1,
      "totalLines": 79
    }
  },
  "sourceToolAssistantUUID": "69711dff-1d5a-4cb8-8537-a16dd4bd1b83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T04:03:59.569Z_

<details open><summary>🔧 Tool call — Read · `toolu_01G5rFYrsRsLZQkidhye4kgk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27e30b50-aa41-4c07-8148-59bb2282c701",
  "isSidechain": false,
  "requestId": "req_011CbF3uAr4csE3wnQQTQsZ2",
  "type": "assistant",
  "uuid": "69711dff-1d5a-4cb8-8537-a16dd4bd1b83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R7CPrwZ5MujbXKzkjVcJzg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11573,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11573,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11573,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11573
          },
          "type": "message"
        }
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

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032808 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direct…",
  "leafUuid": "19e1255c-3354-4356-8f65-b96ad04be5b9",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate CaCLR cross-lingual calibration paper",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b"
}
```

---

### Assistant

_source line 14 · 2026-05-21T04:04:23.119Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the experiment data and paper framing. Let me also load the research and writing skills to inform the paper style.

Actually, let me just write the paper directly. I have all the data I need. Let me craft a complete LaTeX paper based on:

1. **Experiment Data**: 11 experiments covering Pareto frontiers on Qwen3-235B and Llama 4 Scout, CaCLR evaluation, difficulty decomposition, orthogonality analysis, probe complexity, additional benchmarks, quantization validation, CKA analysis, linear projection sample efficiency, control tasks, Gemma 4 31B, and extended language coverage.


2. **Paper Framing**: EACL 2027 target with four core claims around Pareto frontiers, decomposition, CaCLR, and cross-lingual orthogonality, centered on a story about probe-based calibration for multilingual LLMs.
3. **Narrative Guidance**: CaCLR is the positive method contribution where the MMD consistency loss with β > 0 successfully aligns the correctness subspace, with the headline result being 22% ECE reduction for non-English across 20 languages on two architectures compared to temperature scaling.

Let me structure the paper...

Now I'm mapping out the full paper structure with sections for abstract through conclusion, making sure each experiment from the data gets its own results table or analysis. I need to verify all numbers come directly from the experimental results and then start building the LaTeX document in standard ACL format. I'm continuing to map out the remaining experiments and deciding which tables belong in the main paper versus the appendix. The key ones like CaCLR results, ablations, and sensitivity analyses will go in the body, while supplementary analyses like control tasks and extended language results can move to the appendix to keep the paper focused.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19e1255c-3354-4356-8f65-b96ad04be5b9",
  "isSidechain": false,
  "requestId": "req_011CbF3uVwGovfzEY2Mg4PnH",
  "type": "assistant",
  "uuid": "ea12c74a-bb9a-49b9-bad8-0ce9de00caee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UcWrddk1HJDDwZprqLkVpv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28963,
      "cache_read_input_tokens": 23414,
      "output_tokens": 1228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28963,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1228,
          "cache_read_input_tokens": 23414,
          "cache_creation_input_tokens": 28963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28963
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-21T04:04:23.230Z_

Now let me check the output directory and write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea12c74a-bb9a-49b9-bad8-0ce9de00caee",
  "isSidechain": false,
  "requestId": "req_011CbF3uVwGovfzEY2Mg4PnH",
  "type": "assistant",
  "uuid": "13d2d006-84d9-4d66-b002-a3cdc3894e0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UcWrddk1HJDDwZprqLkVpv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28963,
      "cache_read_input_tokens": 23414,
      "output_tokens": 1228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28963,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1228,
          "cache_read_input_tokens": 23414,
          "cache_creation_input_tokens": 28963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28963
          },
          "type": "message"
        }
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

_source line 16 · 2026-05-21T04:04:25.377Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01U1Aw9aQLgeNgkJF3BiDvbs`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/",
  "description": "List output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13d2d006-84d9-4d66-b002-a3cdc3894e0a",
  "isSidechain": false,
  "requestId": "req_011CbF3uVwGovfzEY2Mg4PnH",
  "type": "assistant",
  "uuid": "8568faad-ddf8-432e-9478-ceefd4c092da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UcWrddk1HJDDwZprqLkVpv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28963,
      "cache_read_input_tokens": 23414,
      "output_tokens": 1228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28963,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1228,
          "cache_read_input_tokens": 23414,
          "cache_creation_input_tokens": 28963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28963
          },
          "type": "message"
        }
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

_source line 17 · 2026-05-21T04:04:25.555Z_

<details><summary>↩ Tool result · `toolu_01U1Aw9aQLgeNgkJF3BiDvbs`</summary>

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
  "parentUuid": "8568faad-ddf8-432e-9478-ceefd4c092da",
  "isSidechain": false,
  "promptId": "21625223-a819-4abc-b0c5-9519cc481936",
  "type": "user",
  "uuid": "68667987-0759-43c5-9865-d143d921ed12",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "8568faad-ddf8-432e-9478-ceefd4c092da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-21T04:04:28.580Z_

Writing the full LaTeX paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68667987-0759-43c5-9865-d143d921ed12",
  "isSidechain": false,
  "requestId": "req_011CbF3wRXRGXTSd3hMEeJrz",
  "type": "assistant",
  "uuid": "8bef94fe-8b65-4abf-9ace-bc6b48b1a1de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GT14icroaom49vSrpmT1Ex",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1256,
      "cache_read_input_tokens": 52377,
      "output_tokens": 15165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1256,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15165,
          "cache_read_input_tokens": 52377,
          "cache_creation_input_tokens": 1256,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1256
          },
          "type": "message"
        }
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

_source line 19 · 2026-05-21T04:08:35.414Z_

<details open><summary>🔧 Tool call — Write · `toolu_01K8GFYmiftL8v9hoRRb44A7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{array}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{adjustbox}\n\n\\title{CaCLR: Zero-Label Cross-Lingual Calibration via\\\\Correctness-Direction Alignment in Large Language Models}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nNon-English languages suffer substantially worse calibration in multilingual large language models, yet all existing probe-based calibration methods operate exclusively in English.\nWe present the first systematic study of cross-lingual correctness-probe transfer across 20 languages on two large-scale architectures (Qwen3-235B-A22B and Llama~4 Scout 109B).\nWe discover an architecture-dependent \\emph{depth--transferability Pareto frontier}: English-optimal probe layers consistently degrade in cross-lingual transfer on Qwen3 ($\\rho \\approx -0.65$) but show a weaker, language-heterogeneous tradeoff on Llama~4 ($\\rho \\approx -0.33$).\nWe propose \\textbf{CaCLR} (Calibration via Cross-Lingual Regularization), a training objective that combines binary cross-entropy, sample-binned ECE, and an MMD consistency loss on probe logits from parallel inputs---requiring zero target-language correctness labels.\nCaCLR reduces non-English ECE by 22\\% relative to temperature scaling across 20 languages on two architectures, while improving AUROC by 3.5--5.6 percentage points over zero-shot transfer.\nA difficulty-controlled decomposition separates transfer into shared-difficulty and language-specific capability components, providing prescriptive per-language alignment guidance.\nCKA geometric analysis reveals that the correctness direction occupies a low-dimensional language-agnostic subspace (principal angle $\\sim$12\\textdegree) even as global representations diverge ($\\sim$39\\textdegree), with a partial correlation $r=0.42$ ($p<0.01$) after controlling for depth.\nWe validate all findings on a third architecture (Gemma~4 31B Dense), two additional benchmarks, and 53 languages.\n\\end{abstract}\n\n%% ============================================================\n%% 1. INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nLarge language models exhibit poor calibration in non-English languages, with expected calibration error (ECE) often 3--5$\\times$ worse than in English~\\citep{huang2023look}.\nProbe-based calibration---training linear probes on internal representations to predict answer correctness---offers a promising alternative to output-based methods, as it accesses richer signal than verbalized confidence~\\citep{miao2026correctness}.\nHowever, the entire probe-based calibration research line has been developed and evaluated exclusively in English.\n\nThis paper asks: \\emph{does probe-based calibration work across languages?}\nIf correctness probes trained on English internal representations can transfer to other languages without target-language labels, this would unlock scalable multilingual calibration.\nIf not, understanding \\emph{why} transfer fails---and under what conditions---charts a path forward.\n\nWe make four contributions:\n\n\\paragraph{(1) Pareto Frontier Discovery.}\nWe reveal an architecture-dependent depth--transferability tradeoff across 20 languages on Qwen3-235B and Llama~4 Scout.\nDeeper layers yield better English probes but degrade cross-lingual transfer; the tradeoff is strong on Qwen3 (Spearman $\\rho = -0.65$) and weaker on Llama~4 ($\\rho = -0.33$), with a third architecture (Gemma~4 31B, $\\rho = -0.52$) confirming the pattern.\n\n\\paragraph{(2) Difficulty--Capability Decomposition.}\nWe decompose cross-lingual correctness transfer into a shared difficulty component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer degradation).\nThis decomposition is prescriptive: it predicts the optimal alignment strategy per language with 82\\% accuracy.\n\n\\paragraph{(3) CaCLR Method.}\nWe propose CaCLR ($\\mathcal{L} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{MMD}}$), which aligns the correctness subspace across languages via MMD on probe logits from parallel inputs.\nCaCLR requires zero target-language correctness labels and reduces non-English ECE by 22\\% versus temperature scaling (0.121 vs.\\ 0.155 on Qwen3, 0.131 vs.\\ 0.163 on Llama~4).\n\n\\paragraph{(4) Cross-Lingual Orthogonality.}\nWe establish that the correctness--confidence orthogonality~\\citep{miao2026correctness} persists across all 20 languages and both architectures (cosine similarity $<0.06$ everywhere), establishing output-based calibration as structurally limited regardless of language.\n\n\n%% ============================================================\n%% 2. RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\paragraph{Probe-based calibration.}\nRecent work has shown that internal representations encode correctness signals that are orthogonal to verbalized confidence~\\citep{miao2026correctness}.\nCORAL~\\citep{miao2026coral} extends correctness probes across tasks but remains English-only.\nLACE~\\citep{zhou2024lace} uses per-language layer ensembles but requires target-language labels.\nWe extend this research line to multilingual settings with zero target-language labels.\n\n\\paragraph{Cross-lingual probing.}\n\\citet{xiao2025crosslingual} transfer knowledge-boundary probes across 8 languages, but knowledge boundaries (input-level answerability) differ fundamentally from correctness (output-dependent accuracy).\nThey measure probing accuracy rather than calibration and do not discover the Pareto frontier.\n\\citet{civelli2025difficulty} transfer difficulty probes cross-lingually; difficulty is their target, whereas it is a confound we control for.\n\n\\paragraph{Domain adaptation theory.}\nThe H-divergence framework~\\citep{bendavid2010theory} predicts that cross-lingual transfer degrades with representation divergence.\n\\citet{zhao2019learning} show that marginal distribution matching fails when conditional distributions differ---directly relevant to understanding CaCLR's mechanism.\n\n\\paragraph{Cross-lingual alignment.}\nLinear projection methods (MUSE~\\citep{conneau2018word}, VecMap~\\citep{artetxe2018robust}) align cross-lingual word embeddings via linear maps.\nOur linear projection baseline applies this principle at the sentence-level correctness representation.\n\n\\paragraph{Representation similarity.}\nCKA~\\citep{kornblith2019similarity} measures representational similarity between neural network layers.\nWe use CKA to analyze the geometric structure of correctness subspaces across languages and depths.\n\n\\paragraph{Conformal prediction.}\nDistribution-free conformal methods~\\citep{angelopoulos2023conformal} provide coverage guarantees but require per-language calibration data.\nOur approach targets zero-label transfer and is complementary.\n\n\n%% ============================================================\n%% 3. METHOD\n%% ============================================================\n\\section{Method}\n\n\\subsection{Correctness Probing}\n\nGiven an LLM processing a multiple-choice question, we extract the hidden state $\\mathbf{h}_l \\in \\mathbb{R}^d$ at layer $l$ from the last token position.\nA logistic regression probe $f_l(\\mathbf{h}) = \\sigma(\\mathbf{w}_l^\\top \\mathbf{h} + b_l)$ is trained on English data to predict binary correctness.\nThe probe defines a \\emph{correctness direction} $\\mathbf{w}_l / \\|\\mathbf{w}_l\\|$ in representation space.\n\n\\paragraph{Cross-lingual transfer.}\nWe apply the English-trained probe directly to target-language representations (zero-shot transfer).\nTransfer quality is measured by AUROC and ECE on held-out target-language data.\n\n\\paragraph{Why linear probes?}\nWe compare logistic regression against 2-layer MLPs and find that linear probes transfer better cross-lingually (Section~\\ref{sec:probe_complexity}), consistent with the correctness direction's linear structure.\n\n\\subsection{Depth--Transferability Pareto Frontier}\n\nWe probe every $k$-th layer ($k=4$ for 94-layer Qwen3, $k=4$ for 48-layer Llama~4) and measure both English AUROC and zero-shot cross-lingual AUROC.\nThe Pareto frontier is quantified per language via Spearman's $\\rho$ between English AUROC and zero-shot transfer AUROC across layers.\nNegative $\\rho$ indicates a tradeoff: layers optimal for English are suboptimal for transfer.\n\n\\subsection{CaCLR: Calibration via Cross-Lingual Regularization}\n\\label{sec:caclr_method}\n\nCaCLR jointly optimizes three objectives:\n\\begin{equation}\n\\mathcal{L}_{\\text{CaCLR}} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{MMD}}\n\\end{equation}\nwhere $\\mathcal{L}_{\\text{BCE}}$ is the binary cross-entropy on English correctness labels, $\\mathcal{L}_{\\text{SB-ECE}}$ is a sample-binned ECE penalty for calibration, and $\\mathcal{L}_{\\text{MMD}}$ is the maximum mean discrepancy between English and target-language probe logits computed from parallel inputs.\n\n\\paragraph{MMD on probe logits.}\nGiven parallel inputs $\\{(x_i^{\\text{en}}, x_i^{\\text{tgt}})\\}_{i=1}^N$ (the same GlobalMMLU item in two languages), we compute probe logits $z_i^{\\text{en}} = \\mathbf{w}^\\top \\mathbf{h}(x_i^{\\text{en}}) + b$ and $z_i^{\\text{tgt}} = \\mathbf{w}^\\top \\mathbf{h}(x_i^{\\text{tgt}}) + b$.\nThe MMD with Gaussian RBF kernel (bandwidth via median heuristic) operates on these 1-D logits:\n\\begin{equation}\n\\mathcal{L}_{\\text{MMD}} = \\text{MMD}^2\\!\\left(\\{z_i^{\\text{en}}\\}, \\{z_i^{\\text{tgt}}\\}\\right)\n\\end{equation}\nOperating on probe logits (not raw activations) ensures gradient flow to probe parameters and focuses the alignment on the correctness-relevant subspace.\n\n\\paragraph{Training details.}\nOptimizer: Adam with learning rate $10^{-3}$ and cosine decay to $10^{-5}$.\n50 epochs with early stopping (patience 10, monitoring validation BCE loss).\nBatch size 256.\nWarm-started from the standard logistic regression solution.\nParallel set size averages 630 items per language (minimum 580).\n\n\\paragraph{Data protocol.}\nEnglish BCE labels and parallel activations for MMD both come from a 70\\% stratified train split of GlobalMMLU test items.\nEvaluation uses the held-out 30\\%.\nNo target-language correctness labels are used at any stage.\n\n\\subsection{Difficulty--Capability Decomposition}\n\nWe train an IRT difficulty probe to predict item difficulty (estimated from high-resource human response data) from representations.\nThe difficulty direction is projected out, and the correctness probe is retrained on the residual.\nIf transfer \\emph{improves} after projection, the language is \\emph{capability-dominated} (difficulty was a confound).\nIf transfer \\emph{degrades}, the language is \\emph{difficulty-dominated} (difficulty was the transferable signal).\nA random-direction projection control validates that effects are specific to the difficulty direction.\n\n\n%% ============================================================\n%% 4. EXPERIMENTS\n%% ============================================================\n\\section{Experiments}\n\n\\subsection{Setup}\n\n\\paragraph{Models.}\nQwen3-235B-A22B (94 layers, MoE, GPTQ-INT4), Llama~4 Scout 109B (48 layers, MoE, W4A16), and Gemma~4 31B Dense (60 layers, FP16).\nQuantization validation confirms negligible impact on probing results (Appendix~\\ref{app:quantization}).\n\n\\paragraph{Languages.}\n20 languages spanning three resource tiers: HIGH (zh, es, fr, de, ja, pt, it), MID (hi, ru, ko, tr, vi, ar, th), and LOW (sw, bn, yo, te, my, am).\nExtended evaluation covers 53 languages.\n\n\\paragraph{Benchmarks.}\nPrimary: GlobalMMLU (knowledge QA).\nAdditional: Belebele (reading comprehension), MMLU-ProX (knowledge QA).\n\n\\paragraph{Metrics.}\nAUROC for discrimination, ECE for calibration.\nAll comparisons include bootstrap 95\\% CIs (1000 resamples) and paired permutation tests.\n\n%% ------ 4.2 Pareto Frontier ------\n\\subsection{Pareto Frontier: Depth--Transferability Tradeoff}\n\\label{sec:pareto}\n\n\\paragraph{Qwen3-235B.}\nTable~\\ref{tab:qwen_pareto} summarizes the per-language Pareto frontier.\nEnglish-optimal probing occurs at layer 72 (77\\% depth, AUROC 0.832), while the transfer-optimal zone lies at layers 48--56 (51--60\\% depth).\nThe global Spearman $\\rho = -0.65$ indicates a strong negative tradeoff, with per-language $\\rho$ ranging from $-0.82$ (yo) to $-0.41$.\nA clear resource-tier gradient emerges: HIGH 0.773, MID 0.719, LOW 0.635.\n19 of 20 languages transfer successfully (AUROC $>$ 0.60); only Amharic (0.598) falls below threshold.\n\n\\begin{table}[t]\n\\centering\n\\caption{Qwen3-235B Pareto Frontier: representative languages by resource tier.}\n\\label{tab:qwen_pareto}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Lang} & \\textbf{Family} & \\textbf{Tier} & \\textbf{ZS AUROC} & \\textbf{Best Layer} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nzh & Sinitic    & HIGH & 0.790 & L56 & $-0.58$ & .003 \\\\\nes & Romance    & HIGH & 0.780 & L60 & $-0.53$ & .008 \\\\\nja & Japonic    & HIGH & 0.750 & L52 & $-0.62$ & .001 \\\\\nhi & Indo-Aryan & MID  & 0.730 & L48 & $-0.67$ & $<$.001 \\\\\nko & Koreanic   & MID  & 0.730 & L52 & $-0.61$ & .002 \\\\\nar & Semitic    & MID  & 0.720 & L52 & $-0.59$ & .003 \\\\\nsw & Bantu      & LOW  & 0.650 & L40 & $-0.79$ & $<$.001 \\\\\nyo & Volta-Niger& LOW  & 0.610 & L36 & $-0.82$ & $<$.001 \\\\\nam & Ethiosemit.& LOW  & 0.598 & L36 & $-0.81$ & $<$.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Depth--transfer snapshot.}\nThe tradeoff is concrete: at English-optimal L72, English AUROC is 0.832 but cross-lingual average drops to 0.672.\nAt the transfer-optimal L56, English AUROC decreases to 0.812 while cross-lingual average rises to 0.728---a 5.6 percentage-point (pp) cross-lingual gain for a 2.0~pp English cost.\n\n\\paragraph{Transfer conditions (Qwen3).}\nTable~\\ref{tab:transfer_conditions} compares five transfer methods at the Pareto-optimal layer (L56).\nMean-shift produces exactly zero AUROC change (proven: under StandardScaler + LR, mean-shift adds a constant offset to logits, preserving ranks).\nLinear projection with 50 parallel pairs achieves the highest AUROC (0.790) but requires paired correctness labels.\nCaCLR (Section~\\ref{sec:caclr_results}) bridges the gap without target-language labels.\n\n\\begin{table}[t]\n\\centering\n\\caption{Transfer conditions at Pareto zone (Qwen3-235B, L56). Avg over 20 languages.}\n\\label{tab:transfer_conditions}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{AUROC} & \\textbf{ECE} & \\textbf{Labels Required} \\\\\n\\midrule\nZero-shot        & 0.728 & 0.165 & EN only \\\\\nMean-shift       & 0.728 & 0.168 & EN only \\\\\nLinear proj (50) & 0.790 & 0.139 & 50 parallel pairs \\\\\nFew-shot (25)    & 0.745 & 0.152 & 25 target labels \\\\\nFew-shot (100)   & 0.774 & 0.136 & 100 target labels \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Llama~4 Scout.}\nTable~\\ref{tab:llama_pareto} shows the Llama~4 Pareto frontier.\nThe global $\\rho = -0.33$ is significantly weaker than Qwen3's $-0.65$.\nCritically, three languages (ru, ko, ar) show \\emph{positive} depth--transfer correlations: deeper layers do not degrade transfer for these languages.\nLow-resource languages still show strong negative $\\rho$ (sw: $-0.62$, yo: $-0.68$, am: $-0.65$).\nThree languages (yo, my, am) fail the 0.60 transfer threshold, yielding an 85\\% success rate.\n\n\\begin{table}[t]\n\\centering\n\\caption{Llama~4 Scout Pareto Frontier: representative languages.}\n\\label{tab:llama_pareto}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Lang} & \\textbf{Family} & \\textbf{Tier} & \\textbf{ZS AUROC} & \\textbf{Best Layer} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nzh & Sinitic    & HIGH & 0.760 & L36 & $-0.45$ & .14 \\\\\nes & Romance    & HIGH & 0.750 & L36 & $-0.41$ & .18 \\\\\nru & Slavic     & MID  & 0.720 & L40 & $+0.05$ & .88 \\\\\nko & Koreanic   & MID  & 0.710 & L40 & $+0.18$ & .57 \\\\\nar & Semitic    & MID  & 0.700 & L40 & $-0.12$ & .71 \\\\\nsw & Bantu      & LOW  & 0.620 & L28 & $-0.62$ & .03 \\\\\nyo & Volta-Niger& LOW  & 0.570 & L24 & $-0.68$ & .02 \\\\\nam & Ethiosemit.& LOW  & 0.570 & L24 & $-0.65$ & .02 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ------ 4.3 CaCLR ------\n\\subsection{CaCLR: Cross-Lingual Regularization Results}\n\\label{sec:caclr_results}\n\n\\paragraph{Main results.}\nTable~\\ref{tab:caclr_main} compares CaCLR against all baselines at the Pareto-optimal layers.\nCaCLR ($\\alpha = 1.0, \\beta = 0.1$) achieves 0.763 AUROC and 0.121 ECE on Qwen3 (vs.\\ 0.728/0.165 zero-shot and 0.728/0.155 temperature scaling), representing a 22\\% ECE reduction versus temperature scaling.\nOn Llama~4, CaCLR achieves 0.732/0.131 (vs.\\ 0.691/0.163 temperature scaling), a 20\\% ECE reduction.\nThe improvement over zero-shot is statistically significant (paired permutation $p = 0.003$, Cohen's $d = 0.52$, bootstrap 95\\% CI $[0.024, 0.058]$).\n\n\\begin{table}[t]\n\\centering\n\\caption{CaCLR vs baselines at Pareto-optimal layers.}\n\\label{tab:caclr_main}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Qwen3} & \\textbf{Qwen3} & \\textbf{Llama4} & \\textbf{Llama4} & \\textbf{Labels} \\\\\n & \\textbf{AUROC} & \\textbf{ECE} & \\textbf{AUROC} & \\textbf{ECE} & \\\\\n\\midrule\nZero-shot      & 0.728 & 0.165 & 0.691 & 0.179 & EN only \\\\\nMean-shift     & 0.728 & 0.168 & 0.691 & 0.183 & EN only \\\\\nTemp scaling   & 0.728 & 0.155 & 0.691 & 0.163 & EN only \\\\\n\\textbf{CaCLR} & \\textbf{0.763} & \\textbf{0.121} & \\textbf{0.732} & \\textbf{0.131} & EN + parallel \\\\\nLinear proj (50)& 0.790 & 0.139 & 0.749 & 0.146 & 50 pairs \\\\\nFew-shot (25)  & 0.745 & 0.152 & 0.712 & 0.159 & 25 tgt labels \\\\\nFew-shot (100) & 0.774 & 0.136 & 0.745 & 0.142 & 100 tgt labels \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{CaCLR at English-optimal depth.}\nCaCLR's benefit is even larger at the English-optimal layer (L72 on Qwen3): $+5.6$~pp AUROC over zero-shot (0.728 vs.\\ 0.672), with ECE 0.132 vs.\\ 0.171 for temperature scaling.\nThis directly demonstrates that CaCLR shifts the Pareto frontier, partially recovering deep-layer transfer degradation.\n\n\\paragraph{Resource-tier benefit.}\nCaCLR's improvement scales inversely with resource level: HIGH $+3.1$~pp, MID $+4.8$~pp, LOW $+6.8$~pp AUROC.\nLow-resource languages benefit most because the zero-shot distribution gap is largest, giving MMD the greatest marginal alignment gain.\n\n\\paragraph{Pareto shift.}\nCaCLR weakens the Pareto tradeoff: Spearman $\\rho$ shifts from $-0.65$ to $-0.51$ on Qwen3, as deep-layer transfer degradation is partially repaired.\n\n\\paragraph{Component ablation.}\nTable~\\ref{tab:ablation} isolates each component's contribution.\nBCE alone gives the zero-shot baseline (0.728 AUROC, 0.165 ECE).\nAdding SB-ECE alone slightly \\emph{decreases} AUROC ($-0.4$~pp) while improving ECE to 0.148.\nAdding MMD alone yields the largest AUROC gain ($+2.3$~pp) and strong ECE improvement (0.136).\nThe full CaCLR (BCE + SB-ECE + MMD) achieves the best result (0.763/0.121), with synergy between SB-ECE and MMD: SB-ECE improves probability calibration, enabling MMD to match logit distributions more effectively.\n\n\\begin{table}[t]\n\\centering\n\\caption{Component ablation (Qwen3-235B, L56, avg 20 languages).}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Components} & \\textbf{AUROC} & \\textbf{ECE} & \\textbf{$\\Delta$ AUROC} \\\\\n\\midrule\nBCE only (= zero-shot) & 0.728 & 0.165 & --- \\\\\nBCE + SB-ECE           & 0.724 & 0.148 & $-0.004$ \\\\\nBCE + MMD              & 0.751 & 0.136 & $+0.023$ \\\\\nBCE + SB-ECE + MMD     & \\textbf{0.763} & \\textbf{0.121} & $+0.035$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{$\\beta$ sensitivity.}\nTable~\\ref{tab:beta} shows the sensitivity to the MMD weight $\\beta$ (with $\\alpha = 1.0$ fixed).\n$\\beta = 0.1$ is the sweet spot: sufficient alignment pressure without overwhelming the BCE loss.\n$\\beta = 1.0$ degrades performance as MMD dominates, forcing the probe to sacrifice discriminative power for distributional matching.\n\n\\begin{table}[t]\n\\centering\n\\caption{$\\beta$ sensitivity ($\\alpha = 1.0$, Qwen3 L56).}\n\\label{tab:beta}\n\\small\n\\begin{tabular}{cccc}\n\\toprule\n\\textbf{$\\beta$} & \\textbf{AUROC} & \\textbf{ECE} & \\textbf{$\\Delta$ vs $\\beta\\!=\\!0$} \\\\\n\\midrule\n0.0    & 0.724 & 0.148 & --- \\\\\n0.001  & 0.728 & 0.145 & $+0.004$ \\\\\n0.01   & 0.738 & 0.137 & $+0.014$ \\\\\n\\textbf{0.1} & \\textbf{0.763} & \\textbf{0.121} & $+0.039$ \\\\\n1.0    & 0.731 & 0.141 & $+0.007$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ------ 4.4 Decomposition ------\n\\subsection{Difficulty--Capability Decomposition}\n\\label{sec:decomposition}\n\nTable~\\ref{tab:decomp} presents the decomposition results across 10 languages $\\times$ 8 layers $\\times$ 2 architectures.\nFor \\emph{capability-dominated} languages (zh, es, fr, de, ru, ko; typically HIGH/MID resource with baseline ZS AUROC $> 0.70$), projecting out the difficulty direction \\emph{improves} transfer by $+4.2$~pp (95\\% CI $[0.031, 0.054]$).\nFor \\emph{difficulty-dominated} languages (hi, tr, sw, bn; typically lower-resource), projection \\emph{degrades} transfer by $-1.8$~pp (CI $[-0.029, -0.007]$).\n\nThe IRT difficulty probe achieves $R^2 = 0.61$ on average, with a resource gradient (zh: 0.72, sw: 0.43).\nA random-direction projection control yields $\\Delta \\approx -0.003$ ($\\pm 0.008$), confirming specificity.\nThe decomposition correctly predicts the optimal alignment strategy for 82\\% of language--layer combinations.\n\n\\begin{table}[t]\n\\centering\n\\caption{Difficulty decomposition by language category.}\n\\label{tab:decomp}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Category} & \\textbf{Languages} & \\textbf{$\\Delta$ AUROC} & \\textbf{95\\% CI} & \\textbf{Random} \\\\\n\\midrule\nCapability-dom. & zh/es/fr/de/ru/ko & $+0.042$ & $[.031, .054]$ & $-0.002$ \\\\\nDifficulty-dom. & hi/tr/sw/bn       & $-0.018$ & $[-.029, -.007]$ & $-0.004$ \\\\\nOverall         & all 10            & $+0.035$ & $[.021, .049]$ & $-0.003$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Depth interaction.}\nThe decomposition effect amplifies with depth.\nAt 20\\% depth, the capability-only delta is $+1.8$~pp; at 80\\%, it reaches $+6.1$~pp (Table~\\ref{tab:depth_decomp}).\nThis is expected: capability specialization intensifies in deeper layers, making the difficulty confound relatively larger.\n\n\\begin{table}[t]\n\\centering\n\\caption{Depth $\\times$ decomposition interaction.}\n\\label{tab:depth_decomp}\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\n\\textbf{Depth} & \\textbf{EN AUROC} & \\textbf{$\\Delta$ Overall} & \\textbf{$\\Delta$ Cap.} & \\textbf{$\\Delta$ Diff.} \\\\\n\\midrule\n20\\% & 0.650 & $+0.012$ & $+0.018$ & $-0.008$ \\\\\n50\\% & 0.780 & $+0.035$ & $+0.042$ & $-0.016$ \\\\\n80\\% & 0.820 & $+0.051$ & $+0.061$ & $-0.023$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n%% ------ 4.5 CKA Geometric Analysis ------\n\\subsection{CKA Geometric Analysis}\n\\label{sec:cka}\n\n\\paragraph{Partial correlation.}\nTable~\\ref{tab:cka} reports the CKA analysis.\nThe raw correlation between CKA and transfer degradation is $\\rho = -0.64$ ($p < 0.001$), but this is confounded by depth.\nAfter controlling for normalized depth, the partial correlation remains significant ($r = 0.42$, $p = 0.008$), confirming that CKA adds explanatory power beyond depth.\nBetween-language correlations at fixed depth provide the strongest test: at 50\\% depth ($n = 20$ languages), $\\rho = -0.67$ ($p = 0.001$); at 75\\% depth, $\\rho = -0.73$ ($p < 0.001$).\n\n\\begin{table}[t]\n\\centering\n\\caption{CKA partial correlation analysis.}\n\\label{tab:cka}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Analysis} & \\textbf{Statistic} & \\textbf{Value} & \\textbf{$p$} \\\\\n\\midrule\nRaw pooled                & $\\rho$ & $-0.64$ & $<.001$ \\\\\nPartial (ctrl depth)      & $r$    & $0.42$  & .008 \\\\\nBetween-lang, 50\\% depth  & $\\rho$ & $-0.67$ & .001 \\\\\nBetween-lang, 75\\% depth  & $\\rho$ & $-0.73$ & $<.001$ \\\\\nWithin-lang avg (24 layers)& $\\rho$ & $-0.48$ & varies \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Subspace angle analysis.}\nTable~\\ref{tab:subspace} reveals a striking geometric asymmetry.\nThe correctness subspace angle between languages averages 12.3\\textdegree\\ ($\\pm$4.8\\textdegree), while the global representation angle averages 38.7\\textdegree\\ ($\\pm$9.2\\textdegree)---a ratio of 3.15$\\times$.\nThe correctness direction occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge.\n\n\\begin{table}[t]\n\\centering\n\\caption{Subspace angle analysis: correctness direction vs.\\ global representations.}\n\\label{tab:subspace}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Measure} & \\textbf{Qwen3} & \\textbf{Llama4} & \\textbf{Interp.} \\\\\n\\midrule\nCorrect.\\ angle (avg) & 11.2\\textdegree & 13.5\\textdegree & Cross-ling shared \\\\\nCorrect.\\ angle (std) & 3.9\\textdegree  & 5.7\\textdegree  & More variable in Llama \\\\\nGlobal repr.\\ angle    & 41.3\\textdegree & 36.1\\textdegree & Language-specific \\\\\nGlobal/correct.\\ ratio & 3.69 & 2.67 & Qwen: 4$\\times$ more stable \\\\\nCKA cliff location     & 68\\% depth & no cliff & Architecture difference \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{CKA cliff.}\nQwen3-235B exhibits a sharp CKA cliff at L64 (68\\% depth): CKA drops from 0.72 to 0.41 (magnitude 0.31).\nThis explains Qwen3's strong Pareto: before the cliff (L0--L60), transfer degrades slowly; after it (L64--L94), transfer collapses.\nLlama~4 shows no cliff---CKA declines gradually---producing a weaker, more heterogeneous tradeoff.\n\n\n%% ------ 4.6 Orthogonality ------\n\\subsection{Cross-Lingual Orthogonality}\n\\label{sec:orthogonality}\n\nTable~\\ref{tab:orthogonality} shows that the correctness--confidence cosine similarity remains below 0.06 across all 40 (language, architecture) combinations.\nThe mean cosine is 0.032 ($\\pm 0.013$), with a weak positive correlation with resource tier ($\\rho = 0.34$, $p = 0.042$) but negligible effect size (range: 0.027 HIGH vs.\\ 0.040 LOW).\nA permutation test against random directions yields $p < 0.001$, confirming the near-orthogonality is non-trivial.\n\nThis result establishes that the structural limitation of output-based calibration---that models encode ``whether I am correct'' and ``how confident I sound'' in independent subspaces---is a universal architectural property, not an English-specific phenomenon.\n\n\\begin{table}[t]\n\\centering\n\\caption{Correctness--confidence cosine similarity across languages.}\n\\label{tab:orthogonality}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\textbf{Qwen3} & \\textbf{Llama4} & \\textbf{Avg} \\\\\n\\midrule\nen & ---  & 0.023 & 0.030 & 0.027 \\\\\nzh & HIGH & 0.021 & 0.028 & 0.025 \\\\\nes & HIGH & 0.012 & 0.024 & 0.018 \\\\\nhi & MID  & 0.032 & 0.039 & 0.036 \\\\\nko & MID  & 0.028 & 0.035 & 0.032 \\\\\nsw & LOW  & 0.042 & 0.049 & 0.046 \\\\\nam & LOW  & 0.048 & 0.058 & 0.053 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ------ 4.7 Three Architectures ------\n\\subsection{Third Architecture: Gemma~4 31B Dense}\n\\label{sec:gemma}\n\nTable~\\ref{tab:three_arch} summarizes the three-architecture comparison.\nGemma~4 31B Dense ($\\rho = -0.52$) falls between Qwen3 ($-0.65$) and Llama~4 ($-0.33$), consistent with the hypothesis that MoE routing sharpens the Pareto tradeoff.\nGemma's gradual CKA decline (no cliff) resembles Llama~4 but with a deeper onset---dense models maintain cross-lingual sharing longer in the absence of expert routing.\nCaCLR provides $+3.9$~pp AUROC gain, confirming generalization across architectures.\n\n\\begin{table}[t]\n\\centering\n\\caption{Three-architecture comparison.}\n\\label{tab:three_arch}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Architecture} & \\textbf{Type} & \\textbf{EN} & \\textbf{ZS} & \\textbf{$\\rho$} & \\textbf{CKA} & \\textbf{CaCLR} \\\\\n & & \\textbf{AUROC} & \\textbf{Avg} & & \\textbf{Pattern} & \\textbf{$\\Delta$} \\\\\n\\midrule\nQwen3-235B  & MoE (Int4)  & 0.832 & 0.713 & $-0.65$ & Cliff 68\\% & $+0.047$ \\\\\nGemma4-31B  & Dense (FP16)& 0.821 & 0.702 & $-0.52$ & Gradual, deep & $+0.039$ \\\\\nLlama4-Scout& MoE (W4A16) & 0.811 & 0.684 & $-0.33$ & Gradual, early & $+0.041$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n%% ------ 4.8 Cross-Benchmark ------\n\\subsection{Cross-Benchmark Generalization}\n\\label{sec:benchmarks}\n\nTable~\\ref{tab:benchmarks} shows that the Pareto frontier and CaCLR gains replicate across three benchmarks.\nBelebele (reading comprehension) shows slightly lower performance than GlobalMMLU (knowledge QA), reflecting mild domain dependency, but the Pareto structure is highly consistent ($\\rho = -0.61$ vs.\\ $-0.65$).\nMMLU-ProX closely matches GlobalMMLU ($\\rho = -0.67$).\nPer-language rankings are stable across benchmarks (rank correlation $\\rho = 0.89$--$0.93$).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-benchmark generalization (Qwen3-235B).}\n\\label{tab:benchmarks}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Benchmark} & \\textbf{Domain} & \\textbf{EN} & \\textbf{ZS Avg} & \\textbf{$\\rho$} & \\textbf{CaCLR $\\Delta$} \\\\\n\\midrule\nGlobalMMLU & Knowledge QA & 0.832 & 0.713 & $-0.65$ & $+0.047$ \\\\\nBelebele   & Reading comp.& 0.814 & 0.698 & $-0.61$ & $+0.043$ \\\\\nMMLU-ProX  & Knowledge QA & 0.839 & 0.721 & $-0.67$ & $+0.046$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n%% ------ 4.9 Probe Complexity ------\n\\subsection{Probe Complexity}\n\\label{sec:probe_complexity}\n\nComparing logistic regression (LR) against a 2-layer MLP on Qwen3-235B: the MLP achieves slightly higher English AUROC (0.851 vs.\\ 0.832, $+1.9$~pp) but substantially worse zero-shot transfer (0.685 vs.\\ 0.713, $-2.8$~pp).\nThe gap widens for low-resource languages: LR 0.635 vs.\\ MLP 0.581 ($-5.4$~pp).\nRelative degradation from English to cross-lingual is 14.3\\% for LR vs.\\ 19.5\\% for MLP.\nThe MLP's nonlinear capacity captures English-specific patterns that fail to transfer, validating linear probes as the correct choice for cross-lingual calibration.\n\n\n%% ------ 4.10 Linear Projection ------\n\\subsection{Linear Projection Sample Efficiency}\n\\label{sec:linear_proj}\n\nTable~\\ref{tab:linproj} characterizes the sample efficiency of linear projection.\nThe elbow occurs at 50 parallel pairs (AUROC 0.790), beyond which marginal gains diminish sharply ($+0.8$~pp from 50 to 100, $+0.4$~pp from 100 to 200).\nCaCLR (0.763) is equivalent to approximately 35 parallel pairs of linear projection, demonstrating that MMD-based distributional matching achieves partial but not complete subspace alignment.\nThe two methods are complementary: CaCLR for zero-label settings, linear projection when even modest parallel data with labels is available.\n\n\\begin{table}[t]\n\\centering\n\\caption{Linear projection sample efficiency (Qwen3-235B, L56).}\n\\label{tab:linproj}\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\n\\textbf{Pairs} & \\textbf{AUROC} & \\textbf{$\\Delta$ vs ZS} & \\textbf{Marginal} & \\textbf{CI Width} \\\\\n\\midrule\n10  & 0.739 & $+0.011$ & --- & 0.034 \\\\\n20  & 0.758 & $+0.030$ & $+0.019$ & 0.023 \\\\\n50  & 0.790 & $+0.062$ & $+0.032$ & 0.015 \\\\\n100 & 0.798 & $+0.070$ & $+0.008$ & 0.010 \\\\\n200 & 0.802 & $+0.074$ & $+0.004$ & 0.007 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n%% ============================================================\n%% 5. CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe presented the first systematic study of cross-lingual correctness-probe calibration, revealing four key findings.\nFirst, an architecture-dependent depth--transferability Pareto frontier: strong on Qwen3 ($\\rho = -0.65$), weak on Llama~4 ($\\rho = -0.33$), intermediate on Gemma~4 ($\\rho = -0.52$).\nSecond, correctness transfer decomposes into difficulty-shared and capability-specific components, enabling prescriptive per-language alignment selection (82\\% accuracy).\nThird, CaCLR enables zero-label cross-lingual calibration, reducing non-English ECE by 22\\% versus temperature scaling across 20 languages on two architectures, with low-resource languages benefiting most ($+6.8$~pp AUROC).\nFourth, correctness--confidence orthogonality is universal (cosine $< 0.06$ across all 40 language--architecture pairs), establishing structural limits on output-based calibration regardless of language.\n\nCKA geometric analysis provides the connecting thread: the correctness direction occupies a language-agnostic low-dimensional subspace (angle $\\sim$12\\textdegree) even as global representations diverge ($\\sim$39\\textdegree), and CKA predicts transfer success beyond what depth alone explains ($r = 0.42$, $p < 0.01$).\nAll findings replicate across three architectures, three benchmarks, and 53 languages.\n\n\\paragraph{Limitations.}\nOur evaluation is limited to MCQA formats.\nThe three-architecture comparison, while consistent, does not support causal attribution to specific architectural features (type, scale, and training data co-vary).\nControl task analysis reveals that $\\sim$10\\% of low-resource, early-layer probing results are capacity artifacts; such results should be interpreted with caution.\nCaCLR's MMD operates in 1-D logit space for linear probes, which limits its alignment capacity compared to higher-dimensional approaches.\n\n\n%% ============================================================\n%% REFERENCES\n%% ============================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{20}\n\n\\bibitem[Angelopoulos \\& Bates(2023)]{angelopoulos2023conformal}\nAngelopoulos, A.~N. \\& Bates, S. (2023).\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock {\\em Foundations and Trends in Machine Learning}.\n\n\\bibitem[Artetxe et~al.(2018)]{artetxe2018robust}\nArtetxe, M., Labaka, G., \\& Agirre, E. (2018).\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In {\\em Proc.\\ ACL}.\n\n\\bibitem[Ben-David et~al.(2010)]{bendavid2010theory}\nBen-David, S., Blitzer, J., Crammer, K., Kulesza, A., Pereira, F., \\& Vaughan, J.~W. (2010).\n\\newblock A theory of learning from different domains.\n\\newblock {\\em Machine Learning}, 79(1--2):151--175.\n\n\\bibitem[Civelli et~al.(2025)]{civelli2025difficulty}\nCivelli, L., et~al. (2025).\n\\newblock Cross-lingual difficulty probe transfer in multilingual models.\n\\newblock In {\\em Proc.\\ NAACL}.\n\n\\bibitem[Conneau et~al.(2018)]{conneau2018word}\nConneau, A., Lample, G., Ranzato, M., Denoyer, L., \\& J\\'{e}gou, H. (2018).\n\\newblock Word translation without parallel data.\n\\newblock In {\\em Proc.\\ ICLR}.\n\n\\bibitem[Hewitt \\& Liang(2019)]{hewitt2019control}\nHewitt, J. \\& Liang, P. (2019).\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In {\\em Proc.\\ EMNLP}.\n\n\\bibitem[Huang et~al.(2023)]{huang2023look}\nHuang, Y., et~al. (2023).\n\\newblock Look before you leap: An exploratory study of uncertainty measurement for large language models.\n\\newblock {\\em arXiv preprint arXiv:2307.10236}.\n\n\\bibitem[Kornblith et~al.(2019)]{kornblith2019similarity}\nKornblith, S., Norouzi, M., Lee, H., \\& Hinton, G. (2019).\n\\newblock Similarity of neural network representations revisited.\n\\newblock In {\\em Proc.\\ ICML}.\n\n\\bibitem[Miao et~al.(2026a)]{miao2026coral}\nMiao, N., et~al. (2026a).\n\\newblock CORAL: Cross-task correctness probes for LLM calibration.\n\\newblock In {\\em Proc.\\ ICLR}.\n\n\\bibitem[Miao \\& Ungar(2026)]{miao2026correctness}\nMiao, N. \\& Ungar, L. (2026).\n\\newblock Correctness--confidence orthogonality in large language models.\n\\newblock In {\\em Proc.\\ ACL}.\n\n\\bibitem[Pires et~al.(2019)]{pires2019multilingual}\nPires, T., Schlinger, E., \\& Garrette, D. (2019).\n\\newblock How multilingual is multilingual {BERT}?\n\\newblock In {\\em Proc.\\ ACL}.\n\n\\bibitem[Raghu et~al.(2017)]{raghu2017svcca}\nRaghu, M., Gilmer, J., Yosinski, J., \\& Sohl-Dickstein, J. (2017).\n\\newblock {SVCCA}: Singular vector canonical correlation analysis for deep learning dynamics and interpretability.\n\\newblock In {\\em Proc.\\ NeurIPS}.\n\n\\bibitem[Voita \\& Titov(2020)]{voita2020mdl}\nVoita, E. \\& Titov, I. (2020).\n\\newblock Information-theoretic probing with minimum description length.\n\\newblock In {\\em Proc.\\ EMNLP}.\n\n\\bibitem[Wu \\& Dredze(2019)]{wu2019beto}\nWu, S. \\& Dredze, M. (2019).\n\\newblock Beto, bentz, becas: The surprising cross-lingual effectiveness of {BERT}.\n\\newblock In {\\em Proc.\\ EMNLP}.\n\n\\bibitem[Xiao et~al.(2025)]{xiao2025crosslingual}\nXiao, Y., et~al. (2025).\n\\newblock Cross-lingual knowledge boundary probe transfer.\n\\newblock In {\\em Proc.\\ ACL}.\n\n\\bibitem[Zhao et~al.(2019)]{zhao2019learning}\nZhao, H., et~al. (2019).\n\\newblock On learning invariant representations for domain adaptation.\n\\newblock In {\\em Proc.\\ ICML}.\n\n\\bibitem[Zhou et~al.(2024)]{zhou2024lace}\nZhou, K., et~al. (2024).\n\\newblock {LACE}: Language-aware calibration ensembles for multilingual {LLMs}.\n\\newblock In {\\em Proc.\\ EMNLP}.\n\n\\end{thebibliography}\n\n\n%% ============================================================\n%% APPENDIX\n%% ============================================================\n\\appendix\n\n\\section{Quantization Validation}\n\\label{app:quantization}\n\nTable~\\ref{tab:quant} validates that INT4/W4A16 quantization does not meaningfully affect probing results.\nAverage AUROC differences are 0.004 (Llama~4) and 0.006 (Qwen3), with CKA between quantized and FP16 representations exceeding 0.98.\nNo differences reach statistical significance.\n\n\\begin{table}[h]\n\\centering\n\\caption{Quantization validation: INT4/W4A16 vs FP16.}\n\\label{tab:quant}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Quant} & \\textbf{Avg $\\Delta$AUROC} & \\textbf{Max $\\Delta$} & \\textbf{CKA} \\\\\n\\midrule\nLlama~4 Scout & W4A16     & 0.004 & 0.008 & 0.987 \\\\\nQwen3-235B    & GPTQ-INT4 & 0.006 & 0.013 & 0.981 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Probe Complexity: LR vs MLP}\n\\label{app:probe_complexity}\n\n\\begin{table}[h]\n\\centering\n\\caption{Probe complexity $\\times$ cross-lingual transfer (Qwen3-235B).}\n\\label{tab:probe_detail}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{LR} & \\textbf{MLP (2-layer)} & \\textbf{$\\Delta$} \\\\\n\\midrule\nEN Best AUROC         & 0.832  & 0.851  & $+0.019$ \\\\\nZS Transfer Avg (20L) & 0.713  & 0.685  & $-0.028$ \\\\\nRelative Degradation   & 14.3\\% & 19.5\\% & $+5.2$pp \\\\\nZS Low-Resource Avg   & 0.635  & 0.581  & $-0.054$ \\\\\nECE Avg               & 0.165  & 0.184  & $+0.019$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Control Task Validation}\n\\label{app:control}\n\nTable~\\ref{tab:control} reports selectivity (real AUROC $-$ control AUROC) by depth and resource tier on Qwen3-235B.\nControl task AUROC averages 0.491 ($\\pm 0.012$, max 0.518), confirming probes cannot memorize random labels.\nOf 480 total grid cells (20 languages $\\times$ 24 layers), 48 (10\\%) have selectivity $<$ 0.05, concentrated in early layers and low-resource languages (54\\% overlap).\nCore results (mid/deep layers, mid/high-resource) maintain selectivity $>$ 0.10.\n\n\\begin{table}[h]\n\\centering\n\\caption{Selectivity by depth $\\times$ resource tier (Qwen3-235B).}\n\\label{tab:control}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Depth} & \\textbf{HIGH} & \\textbf{MID} & \\textbf{LOW} \\\\\n\\midrule\n0--33\\% (early)  & 0.045 & 0.036 & 0.019 \\\\\n33--67\\% (mid)   & 0.142 & 0.118 & 0.078 \\\\\n67--100\\% (deep) & 0.261 & 0.242 & 0.188 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Extended Language Coverage}\n\\label{app:extended}\n\nExtending to 53 languages, zero-shot success rate drops to 83\\% (44/53 succeed, 9 fail---all extreme low-resource: am, my, yo, si, lo, km, gu, or, ne).\nPareto $\\rho$ remains stable: Qwen3 $-0.62$ (vs.\\ $-0.65$ at 20 languages), Llama~4 $-0.31$ (vs.\\ $-0.33$).\nResource-tier gradient strengthens ($R^2 = 0.71$, up from $\\sim$0.60).\nCaCLR gains on new languages average $+4.1$~pp, comparable to the original $+4.7$~pp.\n\n\\begin{table}[h]\n\\centering\n\\caption{Extended language coverage summary.}\n\\label{tab:extended}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{20 Langs} & \\textbf{53 Langs} \\\\\n\\midrule\nZS Success Rate    & 95\\% (Qwen) & 83\\% \\\\\nPareto $\\rho$ Qwen & $-0.65$ & $-0.62$ \\\\\nPareto $\\rho$ Llama& $-0.33$ & $-0.31$ \\\\\nResource Gradient $R^2$ & $\\sim$0.60 & 0.71 \\\\\nCaCLR $\\Delta$ AUROC    & $+0.047$ & $+0.044$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Linear Projection Sample Efficiency: Llama~4}\n\\label{app:linproj_llama}\n\n\\begin{table}[h]\n\\centering\n\\caption{Linear projection sample efficiency (Llama~4 Scout, L32).}\n\\label{tab:linproj_llama}\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\n\\textbf{Pairs} & \\textbf{AUROC} & \\textbf{$\\Delta$ vs ZS} & \\textbf{Marginal} & \\textbf{CI Width} \\\\\n\\midrule\n10  & 0.712 & $+0.021$ & --- & 0.031 \\\\\n20  & 0.729 & $+0.038$ & $+0.017$ & 0.022 \\\\\n50  & 0.749 & $+0.058$ & $+0.020$ & 0.014 \\\\\n100 & 0.757 & $+0.066$ & $+0.008$ & 0.009 \\\\\n200 & 0.761 & $+0.070$ & $+0.004$ & 0.006 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bef94fe-8b65-4abf-9ace-bc6b48b1a1de",
  "isSidechain": false,
  "requestId": "req_011CbF3wRXRGXTSd3hMEeJrz",
  "type": "assistant",
  "uuid": "f5258b16-ba4f-4952-bbd3-a24d4795314c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GT14icroaom49vSrpmT1Ex",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1256,
      "cache_read_input_tokens": 52377,
      "output_tokens": 15165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1256,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15165,
          "cache_read_input_tokens": 52377,
          "cache_creation_input_tokens": 1256,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1256
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-21T04:08:35.431Z_

<details><summary>↩ Tool result · `toolu_01K8GFYmiftL8v9hoRRb44A7`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5258b16-ba4f-4952-bbd3-a24d4795314c",
  "isSidechain": false,
  "promptId": "21625223-a819-4abc-b0c5-9519cc481936",
  "type": "user",
  "uuid": "74c4dc23-97ab-480a-836b-83d954f8201e",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{array}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{adjustbox}\n\n\\title{CaCLR: Zero-Label Cross-Lingual Calibration via\\\\Correctness-Direction Alignment in Large Language Models}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nNon-English languages suffer substantially worse calibration in multilingual large language models, yet all existing probe-based calibration methods operate exclusively in English.\nWe present the first systematic study of cross-lingual correctness-probe transfer across 20 languages on two large-scale architectures (Qwen3-235B-A22B and Llama~4 Scout 109B).\nWe discover an architecture-dependent \\emph{depth--transferability Pareto frontier}: English-optimal probe layers consistently degrade in cross-lingual transfer on Qwen3 ($\\rho \\approx -0.65$) but show a weaker, language-heterogeneous tradeoff on Llama~4 ($\\rho \\approx -0.33$).\nWe propose \\textbf{CaCLR} (Calibration via Cross-Lingual Regularization), a training objective that combines binary cross-entropy, sample-binned ECE, and an MMD consistency loss on probe logits from parallel inputs---requiring zero target-language correctness labels.\nCaCLR reduces non-English ECE by 22\\% relative to temperature scaling across 20 languages on two architectures, while improving AUROC by 3.5--5.6 percentage points over zero-shot transfer.\nA difficulty-controlled decomposition separates transfer into shared-difficulty and language-specific capability components, providing prescriptive per-language alignment guidance.\nCKA geometric analysis reveals that the correctness direction occupies a low-dimensional language-agnostic subspace (principal angle $\\sim$12\\textdegree) even as global representations diverge ($\\sim$39\\textdegree), with a partial correlation $r=0.42$ ($p<0.01$) after controlling for depth.\nWe validate all findings on a third architecture (Gemma~4 31B Dense), two additional benchmarks, and 53 languages.\n\\end{abstract}\n\n%% ============================================================\n%% 1. INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nLarge language models exhibit poor calibration in non-English languages, with expected calibration error (ECE) often 3--5$\\times$ worse than in English~\\citep{huang2023look}.\nProbe-based calibration---training linear probes on internal representations to predict answer correctness---offers a promising alternative to output-based methods, as it accesses richer signal than verbalized confidence~\\citep{miao2026correctness}.\nHowever, the entire probe-based calibration research line has been developed and evaluated exclusively in English.\n\nThis paper asks: \\emph{does probe-based calibration work across languages?}\nIf correctness probes trained on English internal representations can transfer to other languages without target-language labels, this would unlock scalable multilingual calibration.\nIf not, understanding \\emph{why} transfer fails---and under what conditions---charts a path forward.\n\nWe make four contributions:\n\n\\paragraph{(1) Pareto Frontier Discovery.}\nWe reveal an architecture-dependent depth--transferability tradeoff across 20 languages on Qwen3-235B and Llama~4 Scout.\nDeeper layers yield better English probes but degrade cross-lingual transfer; the tradeoff is strong on Qwen3 (Spearman $\\rho = -0.65$) and weaker on Llama~4 ($\\rho = -0.33$), with a third architecture (Gemma~4 31B, $\\rho = -0.52$) confirming the pattern.\n\n\\paragraph{(2) Difficulty--Capability Decomposition.}\nWe decompose cross-lingual correctness transfer into a shared difficulty component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer degradation).\nThis decomposition is prescriptive: it predicts the optimal alignment strategy per language with 82\\% accuracy.\n\n\\paragraph{(3) CaCLR Method.}\nWe propose CaCLR ($\\mathcal{L} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{MMD}}$), which aligns the correctness subspace across languages via MMD on probe logits from parallel inputs.\nCaCLR requires zero target-language correctness labels and reduces non-English ECE by 22\\% versus temperature scaling (0.121 vs.\\ 0.155 on Qwen3, 0.131 vs.\\ 0.163 on Llama~4).\n\n\\paragraph{(4) Cross-Lingual Orthogonality.}\nWe establish that the correctness--confidence orthogonality~\\citep{miao2026correctness} persists across all 20 languages and both architectures (cosine similarity $<0.06$ everywhere), establishing output-based calibration as structurally limited regardless of language.\n\n\n%% ============================================================\n%% 2. RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\paragraph{Probe-based calibration.}\nRecent work has shown that internal representations encode correctness signals that are orthogonal to verbalized confidence~\\citep{miao2026correctness}.\nCORAL~\\citep{miao2026coral} extends correctness probes across tasks but remains English-only.\nLACE~\\citep{zhou2024lace} uses per-language layer ensembles but requires target-language labels.\nWe extend this research line to multilingual settings with zero target-language labels.\n\n\\paragraph{Cross-lingual probing.}\n\\citet{xiao2025crosslingual} transfer knowledge-boundary probes across 8 languages, but knowledge boundaries (input-level answerability) differ fundamentally from correctness (output-dependent accuracy).\nThey measure probing accuracy rather than calibration and do not discover the Pareto frontier.\n\\citet{civelli2025difficulty} transfer difficulty probes cross-lingually; difficulty is their target, whereas it is a confound we control for.\n\n\\paragraph{Domain adaptation theory.}\nThe H-divergence framework~\\citep{bendavid2010theory} predicts that cross-lingual transfer degrades with representation divergence.\n\\citet{zhao2019learning} show that marginal distribution matching fails when conditional distributions differ---directly relevant to understanding CaCLR's mechanism.\n\n\\paragraph{Cross-lingual alignment.}\nLinear projection methods (MUSE~\\citep{conneau2018word}, VecMap~\\citep{artetxe2018robust}) align cross-lingual word embeddings via linear maps.\nOur linear projection baseline applies this principle at the sentence-level correctness representation.\n\n\\paragraph{Representation similarity.}\nCKA~\\citep{kornblith2019similarity} measures representational similarity between neural network layers.\nWe use CKA to analyze the geometric structure of correctness subspaces across languages and depths.\n\n\\paragraph{Conformal prediction.}\nDistribution-free conformal methods~\\citep{angelopoulos2023conformal} provide coverage guarantees but require per-language calibration data.\nOur approach targets zero-label transfer and is complementary.\n\n\n%% ============================================================\n%% 3. METHOD\n%% ============================================================\n\\section{Method}\n\n\\subsection{Correctness Probing}\n\nGiven an LLM processing a multiple-choice question, we extract the hidden state $\\mathbf{h}_l \\in \\mathbb{R}^d$ at layer $l$ from the last token position.\nA logistic regression probe $f_l(\\mathbf{h}) = \\sigma(\\mathbf{w}_l^\\top \\mathbf{h} + b_l)$ is trained on English data to predict binary correctness.\nThe probe defines a \\emph{correctness direction} $\\mathbf{w}_l / \\|\\mathbf{w}_l\\|$ in representation space.\n\n\\paragraph{Cross-lingual transfer.}\nWe apply the English-trained probe directly to target-language representations (zero-shot transfer).\nTransfer quality is measured by AUROC and ECE on held-out target-language data.\n\n\\paragraph{Why linear probes?}\nWe compare logistic regression against 2-layer MLPs and find that linear probes transfer better cross-lingually (Section~\\ref{sec:probe_complexity}), consistent with the correctness direction's linear structure.\n\n\\subsection{Depth--Transferability Pareto Frontier}\n\nWe probe every $k$-th layer ($k=4$ for 94-layer Qwen3, $k=4$ for 48-layer Llama~4) and measure both English AUROC and zero-shot cross-lingual AUROC.\nThe Pareto frontier is quantified per language via Spearman's $\\rho$ between English AUROC and zero-shot transfer AUROC across layers.\nNegative $\\rho$ indicates a tradeoff: layers optimal for English are suboptimal for transfer.\n\n\\subsection{CaCLR: Calibration via Cross-Lingual Regularization}\n\\label{sec:caclr_method}\n\nCaCLR jointly optimizes three objectives:\n\\begin{equation}\n\\mathcal{L}_{\\text{CaCLR}} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{MMD}}\n\\end{equation}\nwhere $\\mathcal{L}_{\\text{BCE}}$ is the binary cross-entropy on English correctness labels, $\\mathcal{L}_{\\text{SB-ECE}}$ is a sample-binned ECE penalty for calibration, and $\\mathcal{L}_{\\text{MMD}}$ is the maximum mean discrepancy between English and target-language probe logits computed from parallel inputs.\n\n\\paragraph{MMD on probe logits.}\nGiven parallel inputs $\\{(x_i^{\\text{en}}, x_i^{\\text{tgt}})\\}_{i=1}^N$ (the same GlobalMMLU item in two languages), we compute probe logits $z_i^{\\text{en}} = \\mathbf{w}^\\top \\mathbf{h}(x_i^{\\text{en}}) + b$ and $z_i^{\\text{tgt}} = \\mathbf{w}^\\top \\mathbf{h}(x_i^{\\text{tgt}}) + b$.\nThe MMD with Gaussian RBF kernel (bandwidth via median heuristic) operates on these 1-D logits:\n\\begin{equation}\n\\mathcal{L}_{\\text{MMD}} = \\text{MMD}^2\\!\\left(\\{z_i^{\\text{en}}\\}, \\{z_i^{\\text{tgt}}\\}\\right)\n\\end{equation}\nOperating on probe logits (not raw activations) ensures gradient flow to probe parameters and focuses the alignment on the correctness-relevant subspace.\n\n\\paragraph{Training details.}\nOptimizer: Adam with learning rate $10^{-3}$ and cosine decay to $10^{-5}$.\n50 epochs with early stopping (patience 10, monitoring validation BCE loss).\nBatch size 256.\nWarm-started from the standard logistic regression solution.\nParallel set size averages 630 items per language (minimum 580).\n\n\\paragraph{Data protocol.}\nEnglish BCE labels and parallel activations for MMD both come from a 70\\% stratified train split of GlobalMMLU test items.\nEvaluation uses the held-out 30\\%.\nNo target-language correctness labels are used at any stage.\n\n\\subsection{Difficulty--Capability Decomposition}\n\nWe train an IRT difficulty probe to predict item difficulty (estimated from high-resource human response data) from representations.\nThe difficulty direction is projected out, and the correctness probe is retrained on the residual.\nIf transfer \\emph{improves} after projection, the language is \\emph{capability-dominated} (difficulty was a confound).\nIf transfer \\emph{degrades}, the language is \\emph{difficulty-dominated} (difficulty was the transferable signal).\nA random-direction projection control validates that effects are specific to the difficulty direction.\n\n\n%% ============================================================\n%% 4. EXPERIMENTS\n%% ============================================================\n\\section{Experiments}\n\n\\subsection{Setup}\n\n\\paragraph{Models.}\nQwen3-235B-A22B (94 layers, MoE, GPTQ-INT4), Llama~4 Scout 109B (48 layers, MoE, W4A16), and Gemma~4 31B Dense (60 layers, FP16).\nQuantization validation confirms negligible impact on probing results (Appendix~\\ref{app:quantization}).\n\n\\paragraph{Languages.}\n20 languages spanning three resource tiers: HIGH (zh, es, fr, de, ja, pt, it), MID (hi, ru, ko, tr, vi, ar, th), and LOW (sw, bn, yo, te, my, am).\nExtended evaluation covers 53 languages.\n\n\\paragraph{Benchmarks.}\nPrimary: GlobalMMLU (knowledge QA).\nAdditional: Belebele (reading comprehension), MMLU-ProX (knowledge QA).\n\n\\paragraph{Metrics.}\nAUROC for discrimination, ECE for calibration.\nAll comparisons include bootstrap 95\\% CIs (1000 resamples) and paired permutation tests.\n\n%% ------ 4.2 Pareto Frontier ------\n\\subsection{Pareto Frontier: Depth--Transferability Tradeoff}\n\\label{sec:pareto}\n\n\\paragraph{Qwen3-235B.}\nTable~\\ref{tab:qwen_pareto} summarizes the per-language Pareto frontier.\nEnglish-optimal probing occurs at layer 72 (77\\% depth, AUROC 0.832), while the transfer-optimal zone lies at layers 48--56 (51--60\\% depth).\nThe global Spearman $\\rho = -0.65$ indicates a strong negative tradeoff, with per-language $\\rho$ ranging from $-0.82$ (yo) to $-0.41$.\nA clear resource-tier gradient emerges: HIGH 0.773, MID 0.719, LOW 0.635.\n19 of 20 languages transfer successfully (AUROC $>$ 0.60); only Amharic (0.598) falls below threshold.\n\n\\begin{table}[t]\n\\centering\n\\caption{Qwen3-235B Pareto Frontier: representative languages by resource tier.}\n\\label{tab:qwen_pareto}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Lang} & \\textbf{Family} & \\textbf{Tier} & \\textbf{ZS AUROC} & \\textbf{Best Layer} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nzh & Sinitic    & HIGH & 0.790 & L56 & $-0.58$ & .003 \\\\\nes & Romance    & HIGH & 0.780 & L60 & $-0.53$ & .008 \\\\\nja & Japonic    & HIGH & 0.750 & L52 & $-0.62$ & .001 \\\\\nhi & Indo-Aryan & MID  & 0.730 & L48 & $-0.67$ & $<$.001 \\\\\nko & Koreanic   & MID  & 0.730 & L52 & $-0.61$ & .002 \\\\\nar & Semitic    & MID  & 0.720 & L52 & $-0.59$ & .003 \\\\\nsw & Bantu      & LOW  & 0.650 & L40 & $-0.79$ & $<$.001 \\\\\nyo & Volta-Niger& LOW  & 0.610 & L36 & $-0.82$ & $<$.001 \\\\\nam & Ethiosemit.& LOW  & 0.598 & L36 & $-0.81$ & $<$.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Depth--transfer snapshot.}\nThe tradeoff is concrete: at English-optimal L72, English AUROC is 0.832 but cross-lingual average drops to 0.672.\nAt the transfer-optimal L56, English AUROC decreases to 0.812 while cross-lingual average rises to 0.728---a 5.6 percentage-point (pp) cross-lingual gain for a 2.0~pp English cost.\n\n\\paragraph{Transfer conditions (Qwen3).}\nTable~\\ref{tab:transfer_conditions} compares five transfer methods at the Pareto-optimal layer (L56).\nMean-shift produces exactly zero AUROC change (proven: under StandardScaler + LR, mean-shift adds a constant offset to logits, preserving ranks).\nLinear projection with 50 parallel pairs achieves the highest AUROC (0.790) but requires paired correctness labels.\nCaCLR (Section~\\ref{sec:caclr_results}) bridges the gap without target-language labels.\n\n\\begin{table}[t]\n\\centering\n\\caption{Transfer conditions at Pareto zone (Qwen3-235B, L56). Avg over 20 languages.}\n\\label{tab:transfer_conditions}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{AUROC} & \\textbf{ECE} & \\textbf{Labels Required} \\\\\n\\midrule\nZero-shot        & 0.728 & 0.165 & EN only \\\\\nMean-shift       & 0.728 & 0.168 & EN only \\\\\nLinear proj (50) & 0.790 & 0.139 & 50 parallel pairs \\\\\nFew-shot (25)    & 0.745 & 0.152 & 25 target labels \\\\\nFew-shot (100)   & 0.774 & 0.136 & 100 target labels \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Llama~4 Scout.}\nTable~\\ref{tab:llama_pareto} shows the Llama~4 Pareto frontier.\nThe global $\\rho = -0.33$ is significantly weaker than Qwen3's $-0.65$.\nCritically, three languages (ru, ko, ar) show \\emph{positive} depth--transfer correlations: deeper layers do not degrade transfer for these languages.\nLow-resource languages still show strong negative $\\rho$ (sw: $-0.62$, yo: $-0.68$, am: $-0.65$).\nThree languages (yo, my, am) fail the 0.60 transfer threshold, yielding an 85\\% success rate.\n\n\\begin{table}[t]\n\\centering\n\\caption{Llama~4 Scout Pareto Frontier: representative languages.}\n\\label{tab:llama_pareto}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Lang} & \\textbf{Family} & \\textbf{Tier} & \\textbf{ZS AUROC} & \\textbf{Best Layer} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nzh & Sinitic    & HIGH & 0.760 & L36 & $-0.45$ & .14 \\\\\nes & Romance    & HIGH & 0.750 & L36 & $-0.41$ & .18 \\\\\nru & Slavic     & MID  & 0.720 & L40 & $+0.05$ & .88 \\\\\nko & Koreanic   & MID  & 0.710 & L40 & $+0.18$ & .57 \\\\\nar & Semitic    & MID  & 0.700 & L40 & $-0.12$ & .71 \\\\\nsw & Bantu      & LOW  & 0.620 & L28 & $-0.62$ & .03 \\\\\nyo & Volta-Niger& LOW  & 0.570 & L24 & $-0.68$ & .02 \\\\\nam & Ethiosemit.& LOW  & 0.570 & L24 & $-0.65$ & .02 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ------ 4.3 CaCLR ------\n\\subsection{CaCLR: Cross-Lingual Regularization Results}\n\\label{sec:caclr_results}\n\n\\paragraph{Main results.}\nTable~\\ref{tab:caclr_main} compares CaCLR against all baselines at the Pareto-optimal layers.\nCaCLR ($\\alpha = 1.0, \\beta = 0.1$) achieves 0.763 AUROC and 0.121 ECE on Qwen3 (vs.\\ 0.728/0.165 zero-shot and 0.728/0.155 temperature scaling), representing a 22\\% ECE reduction versus temperature scaling.\nOn Llama~4, CaCLR achieves 0.732/0.131 (vs.\\ 0.691/0.163 temperature scaling), a 20\\% ECE reduction.\nThe improvement over zero-shot is statistically significant (paired permutation $p = 0.003$, Cohen's $d = 0.52$, bootstrap 95\\% CI $[0.024, 0.058]$).\n\n\\begin{table}[t]\n\\centering\n\\caption{CaCLR vs baselines at Pareto-optimal layers.}\n\\label{tab:caclr_main}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Qwen3} & \\textbf{Qwen3} & \\textbf{Llama4} & \\textbf{Llama4} & \\textbf{Labels} \\\\\n & \\textbf{AUROC} & \\textbf{ECE} & \\textbf{AUROC} & \\textbf{ECE} & \\\\\n\\midrule\nZero-shot      & 0.728 & 0.165 & 0.691 & 0.179 & EN only \\\\\nMean-shift     & 0.728 & 0.168 & 0.691 & 0.183 & EN only \\\\\nTemp scaling   & 0.728 & 0.155 & 0.691 & 0.163 & EN only \\\\\n\\textbf{CaCLR} & \\textbf{0.763} & \\textbf{0.121} & \\textbf{0.732} & \\textbf{0.131} & EN + parallel \\\\\nLinear proj (50)& 0.790 & 0.139 & 0.749 & 0.146 & 50 pairs \\\\\nFew-shot (25)  & 0.745 & 0.152 & 0.712 & 0.159 & 25 tgt labels \\\\\nFew-shot (100) & 0.774 & 0.136 & 0.745 & 0.142 & 100 tgt labels \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{CaCLR at English-optimal depth.}\nCaCLR's benefit is even larger at the English-optimal layer (L72 on Qwen3): $+5.6$~pp AUROC over zero-shot (0.728 vs.\\ 0.672), with ECE 0.132 vs.\\ 0.171 for temperature scaling.\nThis directly demonstrates that CaCLR shifts the Pareto frontier, partially recovering deep-layer transfer degradation.\n\n\\paragraph{Resource-tier benefit.}\nCaCLR's improvement scales inversely with resource level: HIGH $+3.1$~pp, MID $+4.8$~pp, LOW $+6.8$~pp AUROC.\nLow-resource languages benefit most because the zero-shot distribution gap is largest, giving MMD the greatest marginal alignment gain.\n\n\\paragraph{Pareto shift.}\nCaCLR weakens the Pareto tradeoff: Spearman $\\rho$ shifts from $-0.65$ to $-0.51$ on Qwen3, as deep-layer transfer degradation is partially repaired.\n\n\\paragraph{Component ablation.}\nTable~\\ref{tab:ablation} isolates each component's contribution.\nBCE alone gives the zero-shot baseline (0.728 AUROC, 0.165 ECE).\nAdding SB-ECE alone slightly \\emph{decreases} AUROC ($-0.4$~pp) while improving ECE to 0.148.\nAdding MMD alone yields the largest AUROC gain ($+2.3$~pp) and strong ECE improvement (0.136).\nThe full CaCLR (BCE + SB-ECE + MMD) achieves the best result (0.763/0.121), with synergy between SB-ECE and MMD: SB-ECE improves probability calibration, enabling MMD to match logit distributions more effectively.\n\n\\begin{table}[t]\n\\centering\n\\caption{Component ablation (Qwen3-235B, L56, avg 20 languages).}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Components} & \\textbf{AUROC} & \\textbf{ECE} & \\textbf{$\\Delta$ AUROC} \\\\\n\\midrule\nBCE only (= zero-shot) & 0.728 & 0.165 & --- \\\\\nBCE + SB-ECE           & 0.724 & 0.148 & $-0.004$ \\\\\nBCE + MMD              & 0.751 & 0.136 & $+0.023$ \\\\\nBCE + SB-ECE + MMD     & \\textbf{0.763} & \\textbf{0.121} & $+0.035$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{$\\beta$ sensitivity.}\nTable~\\ref{tab:beta} shows the sensitivity to the MMD weight $\\beta$ (with $\\alpha = 1.0$ fixed).\n$\\beta = 0.1$ is the sweet spot: sufficient alignment pressure without overwhelming the BCE loss.\n$\\beta = 1.0$ degrades performance as MMD dominates, forcing the probe to sacrifice discriminative power for distributional matching.\n\n\\begin{table}[t]\n\\centering\n\\caption{$\\beta$ sensitivity ($\\alpha = 1.0$, Qwen3 L56).}\n\\label{tab:beta}\n\\small\n\\begin{tabular}{cccc}\n\\toprule\n\\textbf{$\\beta$} & \\textbf{AUROC} & \\textbf{ECE} & \\textbf{$\\Delta$ vs $\\beta\\!=\\!0$} \\\\\n\\midrule\n0.0    & 0.724 & 0.148 & --- \\\\\n0.001  & 0.728 & 0.145 & $+0.004$ \\\\\n0.01   & 0.738 & 0.137 & $+0.014$ \\\\\n\\textbf{0.1} & \\textbf{0.763} & \\textbf{0.121} & $+0.039$ \\\\\n1.0    & 0.731 & 0.141 & $+0.007$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ------ 4.4 Decomposition ------\n\\subsection{Difficulty--Capability Decomposition}\n\\label{sec:decomposition}\n\nTable~\\ref{tab:decomp} presents the decomposition results across 10 languages $\\times$ 8 layers $\\times$ 2 architectures.\nFor \\emph{capability-dominated} languages (zh, es, fr, de, ru, ko; typically HIGH/MID resource with baseline ZS AUROC $> 0.70$), projecting out the difficulty direction \\emph{improves} transfer by $+4.2$~pp (95\\% CI $[0.031, 0.054]$).\nFor \\emph{difficulty-dominated} languages (hi, tr, sw, bn; typically lower-resource), projection \\emph{degrades} transfer by $-1.8$~pp (CI $[-0.029, -0.007]$).\n\nThe IRT difficulty probe achieves $R^2 = 0.61$ on average, with a resource gradient (zh: 0.72, sw: 0.43).\nA random-direction projection control yields $\\Delta \\approx -0.003$ ($\\pm 0.008$), confirming specificity.\nThe decomposition correctly predicts the optimal alignment strategy for 82\\% of language--layer combinations.\n\n\\begin{table}[t]\n\\centering\n\\caption{Difficulty decomposition by language category.}\n\\label{tab:decomp}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Category} & \\textbf{Languages} & \\textbf{$\\Delta$ AUROC} & \\textbf{95\\% CI} & \\textbf{Random} \\\\\n\\midrule\nCapability-dom. & zh/es/fr/de/ru/ko & $+0.042$ & $[.031, .054]$ & $-0.002$ \\\\\nDifficulty-dom. & hi/tr/sw/bn       & $-0.018$ & $[-.029, -.007]$ & $-0.004$ \\\\\nOverall         & all 10            & $+0.035$ & $[.021, .049]$ & $-0.003$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Depth interaction.}\nThe decomposition effect amplifies with depth.\nAt 20\\% depth, the capability-only delta is $+1.8$~pp; at 80\\%, it reaches $+6.1$~pp (Table~\\ref{tab:depth_decomp}).\nThis is expected: capability specialization intensifies in deeper layers, making the difficulty confound relatively larger.\n\n\\begin{table}[t]\n\\centering\n\\caption{Depth $\\times$ decomposition interaction.}\n\\label{tab:depth_decomp}\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\n\\textbf{Depth} & \\textbf{EN AUROC} & \\textbf{$\\Delta$ Overall} & \\textbf{$\\Delta$ Cap.} & \\textbf{$\\Delta$ Diff.} \\\\\n\\midrule\n20\\% & 0.650 & $+0.012$ & $+0.018$ & $-0.008$ \\\\\n50\\% & 0.780 & $+0.035$ & $+0.042$ & $-0.016$ \\\\\n80\\% & 0.820 & $+0.051$ & $+0.061$ & $-0.023$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n%% ------ 4.5 CKA Geometric Analysis ------\n\\subsection{CKA Geometric Analysis}\n\\label{sec:cka}\n\n\\paragraph{Partial correlation.}\nTable~\\ref{tab:cka} reports the CKA analysis.\nThe raw correlation between CKA and transfer degradation is $\\rho = -0.64$ ($p < 0.001$), but this is confounded by depth.\nAfter controlling for normalized depth, the partial correlation remains significant ($r = 0.42$, $p = 0.008$), confirming that CKA adds explanatory power beyond depth.\nBetween-language correlations at fixed depth provide the strongest test: at 50\\% depth ($n = 20$ languages), $\\rho = -0.67$ ($p = 0.001$); at 75\\% depth, $\\rho = -0.73$ ($p < 0.001$).\n\n\\begin{table}[t]\n\\centering\n\\caption{CKA partial correlation analysis.}\n\\label{tab:cka}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Analysis} & \\textbf{Statistic} & \\textbf{Value} & \\textbf{$p$} \\\\\n\\midrule\nRaw pooled                & $\\rho$ & $-0.64$ & $<.001$ \\\\\nPartial (ctrl depth)      & $r$    & $0.42$  & .008 \\\\\nBetween-lang, 50\\% depth  & $\\rho$ & $-0.67$ & .001 \\\\\nBetween-lang, 75\\% depth  & $\\rho$ & $-0.73$ & $<.001$ \\\\\nWithin-lang avg (24 layers)& $\\rho$ & $-0.48$ & varies \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Subspace angle analysis.}\nTable~\\ref{tab:subspace} reveals a striking geometric asymmetry.\nThe correctness subspace angle between languages averages 12.3\\textdegree\\ ($\\pm$4.8\\textdegree), while the global representation angle averages 38.7\\textdegree\\ ($\\pm$9.2\\textdegree)---a ratio of 3.15$\\times$.\nThe correctness direction occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge.\n\n\\begin{table}[t]\n\\centering\n\\caption{Subspace angle analysis: correctness direction vs.\\ global representations.}\n\\label{tab:subspace}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Measure} & \\textbf{Qwen3} & \\textbf{Llama4} & \\textbf{Interp.} \\\\\n\\midrule\nCorrect.\\ angle (avg) & 11.2\\textdegree & 13.5\\textdegree & Cross-ling shared \\\\\nCorrect.\\ angle (std) & 3.9\\textdegree  & 5.7\\textdegree  & More variable in Llama \\\\\nGlobal repr.\\ angle    & 41.3\\textdegree & 36.1\\textdegree & Language-specific \\\\\nGlobal/correct.\\ ratio & 3.69 & 2.67 & Qwen: 4$\\times$ more stable \\\\\nCKA cliff location     & 68\\% depth & no cliff & Architecture difference \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{CKA cliff.}\nQwen3-235B exhibits a sharp CKA cliff at L64 (68\\% depth): CKA drops from 0.72 to 0.41 (magnitude 0.31).\nThis explains Qwen3's strong Pareto: before the cliff (L0--L60), transfer degrades slowly; after it (L64--L94), transfer collapses.\nLlama~4 shows no cliff---CKA declines gradually---producing a weaker, more heterogeneous tradeoff.\n\n\n%% ------ 4.6 Orthogonality ------\n\\subsection{Cross-Lingual Orthogonality}\n\\label{sec:orthogonality}\n\nTable~\\ref{tab:orthogonality} shows that the correctness--confidence cosine similarity remains below 0.06 across all 40 (language, architecture) combinations.\nThe mean cosine is 0.032 ($\\pm 0.013$), with a weak positive correlation with resource tier ($\\rho = 0.34$, $p = 0.042$) but negligible effect size (range: 0.027 HIGH vs.\\ 0.040 LOW).\nA permutation test against random directions yields $p < 0.001$, confirming the near-orthogonality is non-trivial.\n\nThis result establishes that the structural limitation of output-based calibration---that models encode ``whether I am correct'' and ``how confident I sound'' in independent subspaces---is a universal architectural property, not an English-specific phenomenon.\n\n\\begin{table}[t]\n\\centering\n\\caption{Correctness--confidence cosine similarity across languages.}\n\\label{tab:orthogonality}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\textbf{Qwen3} & \\textbf{Llama4} & \\textbf{Avg} \\\\\n\\midrule\nen & ---  & 0.023 & 0.030 & 0.027 \\\\\nzh & HIGH & 0.021 & 0.028 & 0.025 \\\\\nes & HIGH & 0.012 & 0.024 & 0.018 \\\\\nhi & MID  & 0.032 & 0.039 & 0.036 \\\\\nko & MID  & 0.028 & 0.035 & 0.032 \\\\\nsw & LOW  & 0.042 & 0.049 & 0.046 \\\\\nam & LOW  & 0.048 & 0.058 & 0.053 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ------ 4.7 Three Architectures ------\n\\subsection{Third Architecture: Gemma~4 31B Dense}\n\\label{sec:gemma}\n\nTable~\\ref{tab:three_arch} summarizes the three-architecture comparison.\nGemma~4 31B Dense ($\\rho = -0.52$) falls between Qwen3 ($-0.65$) and Llama~4 ($-0.33$), consistent with the hypothesis that MoE routing sharpens the Pareto tradeoff.\nGemma's gradual CKA decline (no cliff) resembles Llama~4 but with a deeper onset---dense models maintain cross-lingual sharing longer in the absence of expert routing.\nCaCLR provides $+3.9$~pp AUROC gain, confirming generalization across architectures.\n\n\\begin{table}[t]\n\\centering\n\\caption{Three-architecture comparison.}\n\\label{tab:three_arch}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Architecture} & \\textbf{Type} & \\textbf{EN} & \\textbf{ZS} & \\textbf{$\\rho$} & \\textbf{CKA} & \\textbf{CaCLR} \\\\\n & & \\textbf{AUROC} & \\textbf{Avg} & & \\textbf{Pattern} & \\textbf{$\\Delta$} \\\\\n\\midrule\nQwen3-235B  & MoE (Int4)  & 0.832 & 0.713 & $-0.65$ & Cliff 68\\% & $+0.047$ \\\\\nGemma4-31B  & Dense (FP16)& 0.821 & 0.702 & $-0.52$ & Gradual, deep & $+0.039$ \\\\\nLlama4-Scout& MoE (W4A16) & 0.811 & 0.684 & $-0.33$ & Gradual, early & $+0.041$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n%% ------ 4.8 Cross-Benchmark ------\n\\subsection{Cross-Benchmark Generalization}\n\\label{sec:benchmarks}\n\nTable~\\ref{tab:benchmarks} shows that the Pareto frontier and CaCLR gains replicate across three benchmarks.\nBelebele (reading comprehension) shows slightly lower performance than GlobalMMLU (knowledge QA), reflecting mild domain dependency, but the Pareto structure is highly consistent ($\\rho = -0.61$ vs.\\ $-0.65$).\nMMLU-ProX closely matches GlobalMMLU ($\\rho = -0.67$).\nPer-language rankings are stable across benchmarks (rank correlation $\\rho = 0.89$--$0.93$).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-benchmark generalization (Qwen3-235B).}\n\\label{tab:benchmarks}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Benchmark} & \\textbf{Domain} & \\textbf{EN} & \\textbf{ZS Avg} & \\textbf{$\\rho$} & \\textbf{CaCLR $\\Delta$} \\\\\n\\midrule\nGlobalMMLU & Knowledge QA & 0.832 & 0.713 & $-0.65$ & $+0.047$ \\\\\nBelebele   & Reading comp.& 0.814 & 0.698 & $-0.61$ & $+0.043$ \\\\\nMMLU-ProX  & Knowledge QA & 0.839 & 0.721 & $-0.67$ & $+0.046$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n%% ------ 4.9 Probe Complexity ------\n\\subsection{Probe Complexity}\n\\label{sec:probe_complexity}\n\nComparing logistic regression (LR) against a 2-layer MLP on Qwen3-235B: the MLP achieves slightly higher English AUROC (0.851 vs.\\ 0.832, $+1.9$~pp) but substantially worse zero-shot transfer (0.685 vs.\\ 0.713, $-2.8$~pp).\nThe gap widens for low-resource languages: LR 0.635 vs.\\ MLP 0.581 ($-5.4$~pp).\nRelative degradation from English to cross-lingual is 14.3\\% for LR vs.\\ 19.5\\% for MLP.\nThe MLP's nonlinear capacity captures English-specific patterns that fail to transfer, validating linear probes as the correct choice for cross-lingual calibration.\n\n\n%% ------ 4.10 Linear Projection ------\n\\subsection{Linear Projection Sample Efficiency}\n\\label{sec:linear_proj}\n\nTable~\\ref{tab:linproj} characterizes the sample efficiency of linear projection.\nThe elbow occurs at 50 parallel pairs (AUROC 0.790), beyond which marginal gains diminish sharply ($+0.8$~pp from 50 to 100, $+0.4$~pp from 100 to 200).\nCaCLR (0.763) is equivalent to approximately 35 parallel pairs of linear projection, demonstrating that MMD-based distributional matching achieves partial but not complete subspace alignment.\nThe two methods are complementary: CaCLR for zero-label settings, linear projection when even modest parallel data with labels is available.\n\n\\begin{table}[t]\n\\centering\n\\caption{Linear projection sample efficiency (Qwen3-235B, L56).}\n\\label{tab:linproj}\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\n\\textbf{Pairs} & \\textbf{AUROC} & \\textbf{$\\Delta$ vs ZS} & \\textbf{Marginal} & \\textbf{CI Width} \\\\\n\\midrule\n10  & 0.739 & $+0.011$ & --- & 0.034 \\\\\n20  & 0.758 & $+0.030$ & $+0.019$ & 0.023 \\\\\n50  & 0.790 & $+0.062$ & $+0.032$ & 0.015 \\\\\n100 & 0.798 & $+0.070$ & $+0.008$ & 0.010 \\\\\n200 & 0.802 & $+0.074$ & $+0.004$ & 0.007 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n%% ============================================================\n%% 5. CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe presented the first systematic study of cross-lingual correctness-probe calibration, revealing four key findings.\nFirst, an architecture-dependent depth--transferability Pareto frontier: strong on Qwen3 ($\\rho = -0.65$), weak on Llama~4 ($\\rho = -0.33$), intermediate on Gemma~4 ($\\rho = -0.52$).\nSecond, correctness transfer decomposes into difficulty-shared and capability-specific components, enabling prescriptive per-language alignment selection (82\\% accuracy).\nThird, CaCLR enables zero-label cross-lingual calibration, reducing non-English ECE by 22\\% versus temperature scaling across 20 languages on two architectures, with low-resource languages benefiting most ($+6.8$~pp AUROC).\nFourth, correctness--confidence orthogonality is universal (cosine $< 0.06$ across all 40 language--architecture pairs), establishing structural limits on output-based calibration regardless of language.\n\nCKA geometric analysis provides the connecting thread: the correctness direction occupies a language-agnostic low-dimensional subspace (angle $\\sim$12\\textdegree) even as global representations diverge ($\\sim$39\\textdegree), and CKA predicts transfer success beyond what depth alone explains ($r = 0.42$, $p < 0.01$).\nAll findings replicate across three architectures, three benchmarks, and 53 languages.\n\n\\paragraph{Limitations.}\nOur evaluation is limited to MCQA formats.\nThe three-architecture comparison, while consistent, does not support causal attribution to specific architectural features (type, scale, and training data co-vary).\nControl task analysis reveals that $\\sim$10\\% of low-resource, early-layer probing results are capacity artifacts; such results should be interpreted with caution.\nCaCLR's MMD operates in 1-D logit space for linear probes, which limits its alignment capacity compared to higher-dimensional approaches.\n\n\n%% ============================================================\n%% REFERENCES\n%% ============================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{20}\n\n\\bibitem[Angelopoulos \\& Bates(2023)]{angelopoulos2023conformal}\nAngelopoulos, A.~N. \\& Bates, S. (2023).\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock {\\em Foundations and Trends in Machine Learning}.\n\n\\bibitem[Artetxe et~al.(2018)]{artetxe2018robust}\nArtetxe, M., Labaka, G., \\& Agirre, E. (2018).\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In {\\em Proc.\\ ACL}.\n\n\\bibitem[Ben-David et~al.(2010)]{bendavid2010theory}\nBen-David, S., Blitzer, J., Crammer, K., Kulesza, A., Pereira, F., \\& Vaughan, J.~W. (2010).\n\\newblock A theory of learning from different domains.\n\\newblock {\\em Machine Learning}, 79(1--2):151--175.\n\n\\bibitem[Civelli et~al.(2025)]{civelli2025difficulty}\nCivelli, L., et~al. (2025).\n\\newblock Cross-lingual difficulty probe transfer in multilingual models.\n\\newblock In {\\em Proc.\\ NAACL}.\n\n\\bibitem[Conneau et~al.(2018)]{conneau2018word}\nConneau, A., Lample, G., Ranzato, M., Denoyer, L., \\& J\\'{e}gou, H. (2018).\n\\newblock Word translation without parallel data.\n\\newblock In {\\em Proc.\\ ICLR}.\n\n\\bibitem[Hewitt \\& Liang(2019)]{hewitt2019control}\nHewitt, J. \\& Liang, P. (2019).\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In {\\em Proc.\\ EMNLP}.\n\n\\bibitem[Huang et~al.(2023)]{huang2023look}\nHuang, Y., et~al. (2023).\n\\newblock Look before you leap: An exploratory study of uncertainty measurement for large language models.\n\\newblock {\\em arXiv preprint arXiv:2307.10236}.\n\n\\bibitem[Kornblith et~al.(2019)]{kornblith2019similarity}\nKornblith, S., Norouzi, M., Lee, H., \\& Hinton, G. (2019).\n\\newblock Similarity of neural network representations revisited.\n\\newblock In {\\em Proc.\\ ICML}.\n\n\\bibitem[Miao et~al.(2026a)]{miao2026coral}\nMiao, N., et~al. (2026a).\n\\newblock CORAL: Cross-task correctness probes for LLM calibration.\n\\newblock In {\\em Proc.\\ ICLR}.\n\n\\bibitem[Miao \\& Ungar(2026)]{miao2026correctness}\nMiao, N. \\& Ungar, L. (2026).\n\\newblock Correctness--confidence orthogonality in large language models.\n\\newblock In {\\em Proc.\\ ACL}.\n\n\\bibitem[Pires et~al.(2019)]{pires2019multilingual}\nPires, T., Schlinger, E., \\& Garrette, D. (2019).\n\\newblock How multilingual is multilingual {BERT}?\n\\newblock In {\\em Proc.\\ ACL}.\n\n\\bibitem[Raghu et~al.(2017)]{raghu2017svcca}\nRaghu, M., Gilmer, J., Yosinski, J., \\& Sohl-Dickstein, J. (2017).\n\\newblock {SVCCA}: Singular vector canonical correlation analysis for deep learning dynamics and interpretability.\n\\newblock In {\\em Proc.\\ NeurIPS}.\n\n\\bibitem[Voita \\& Titov(2020)]{voita2020mdl}\nVoita, E. \\& Titov, I. (2020).\n\\newblock Information-theoretic probing with minimum description length.\n\\newblock In {\\em Proc.\\ EMNLP}.\n\n\\bibitem[Wu \\& Dredze(2019)]{wu2019beto}\nWu, S. \\& Dredze, M. (2019).\n\\newblock Beto, bentz, becas: The surprising cross-lingual effectiveness of {BERT}.\n\\newblock In {\\em Proc.\\ EMNLP}.\n\n\\bibitem[Xiao et~al.(2025)]{xiao2025crosslingual}\nXiao, Y., et~al. (2025).\n\\newblock Cross-lingual knowledge boundary probe transfer.\n\\newblock In {\\em Proc.\\ ACL}.\n\n\\bibitem[Zhao et~al.(2019)]{zhao2019learning}\nZhao, H., et~al. (2019).\n\\newblock On learning invariant representations for domain adaptation.\n\\newblock In {\\em Proc.\\ ICML}.\n\n\\bibitem[Zhou et~al.(2024)]{zhou2024lace}\nZhou, K., et~al. (2024).\n\\newblock {LACE}: Language-aware calibration ensembles for multilingual {LLMs}.\n\\newblock In {\\em Proc.\\ EMNLP}.\n\n\\end{thebibliography}\n\n\n%% ============================================================\n%% APPENDIX\n%% ============================================================\n\\appendix\n\n\\section{Quantization Validation}\n\\label{app:quantization}\n\nTable~\\ref{tab:quant} validates that INT4/W4A16 quantization does not meaningfully affect probing results.\nAverage AUROC differences are 0.004 (Llama~4) and 0.006 (Qwen3), with CKA between quantized and FP16 representations exceeding 0.98.\nNo differences reach statistical significance.\n\n\\begin{table}[h]\n\\centering\n\\caption{Quantization validation: INT4/W4A16 vs FP16.}\n\\label{tab:quant}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Quant} & \\textbf{Avg $\\Delta$AUROC} & \\textbf{Max $\\Delta$} & \\textbf{CKA} \\\\\n\\midrule\nLlama~4 Scout & W4A16     & 0.004 & 0.008 & 0.987 \\\\\nQwen3-235B    & GPTQ-INT4 & 0.006 & 0.013 & 0.981 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Probe Complexity: LR vs MLP}\n\\label{app:probe_complexity}\n\n\\begin{table}[h]\n\\centering\n\\caption{Probe complexity $\\times$ cross-lingual transfer (Qwen3-235B).}\n\\label{tab:probe_detail}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{LR} & \\textbf{MLP (2-layer)} & \\textbf{$\\Delta$} \\\\\n\\midrule\nEN Best AUROC         & 0.832  & 0.851  & $+0.019$ \\\\\nZS Transfer Avg (20L) & 0.713  & 0.685  & $-0.028$ \\\\\nRelative Degradation   & 14.3\\% & 19.5\\% & $+5.2$pp \\\\\nZS Low-Resource Avg   & 0.635  & 0.581  & $-0.054$ \\\\\nECE Avg               & 0.165  & 0.184  & $+0.019$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Control Task Validation}\n\\label{app:control}\n\nTable~\\ref{tab:control} reports selectivity (real AUROC $-$ control AUROC) by depth and resource tier on Qwen3-235B.\nControl task AUROC averages 0.491 ($\\pm 0.012$, max 0.518), confirming probes cannot memorize random labels.\nOf 480 total grid cells (20 languages $\\times$ 24 layers), 48 (10\\%) have selectivity $<$ 0.05, concentrated in early layers and low-resource languages (54\\% overlap).\nCore results (mid/deep layers, mid/high-resource) maintain selectivity $>$ 0.10.\n\n\\begin{table}[h]\n\\centering\n\\caption{Selectivity by depth $\\times$ resource tier (Qwen3-235B).}\n\\label{tab:control}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Depth} & \\textbf{HIGH} & \\textbf{MID} & \\textbf{LOW} \\\\\n\\midrule\n0--33\\% (early)  & 0.045 & 0.036 & 0.019 \\\\\n33--67\\% (mid)   & 0.142 & 0.118 & 0.078 \\\\\n67--100\\% (deep) & 0.261 & 0.242 & 0.188 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Extended Language Coverage}\n\\label{app:extended}\n\nExtending to 53 languages, zero-shot success rate drops to 83\\% (44/53 succeed, 9 fail---all extreme low-resource: am, my, yo, si, lo, km, gu, or, ne).\nPareto $\\rho$ remains stable: Qwen3 $-0.62$ (vs.\\ $-0.65$ at 20 languages), Llama~4 $-0.31$ (vs.\\ $-0.33$).\nResource-tier gradient strengthens ($R^2 = 0.71$, up from $\\sim$0.60).\nCaCLR gains on new languages average $+4.1$~pp, comparable to the original $+4.7$~pp.\n\n\\begin{table}[h]\n\\centering\n\\caption{Extended language coverage summary.}\n\\label{tab:extended}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{20 Langs} & \\textbf{53 Langs} \\\\\n\\midrule\nZS Success Rate    & 95\\% (Qwen) & 83\\% \\\\\nPareto $\\rho$ Qwen & $-0.65$ & $-0.62$ \\\\\nPareto $\\rho$ Llama& $-0.33$ & $-0.31$ \\\\\nResource Gradient $R^2$ & $\\sim$0.60 & 0.71 \\\\\nCaCLR $\\Delta$ AUROC    & $+0.047$ & $+0.044$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Linear Projection Sample Efficiency: Llama~4}\n\\label{app:linproj_llama}\n\n\\begin{table}[h]\n\\centering\n\\caption{Linear projection sample efficiency (Llama~4 Scout, L32).}\n\\label{tab:linproj_llama}\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\n\\textbf{Pairs} & \\textbf{AUROC} & \\textbf{$\\Delta$ vs ZS} & \\textbf{Marginal} & \\textbf{CI Width} \\\\\n\\midrule\n10  & 0.712 & $+0.021$ & --- & 0.031 \\\\\n20  & 0.729 & $+0.038$ & $+0.017$ & 0.022 \\\\\n50  & 0.749 & $+0.058$ & $+0.020$ & 0.014 \\\\\n100 & 0.757 & $+0.066$ & $+0.008$ & 0.009 \\\\\n200 & 0.761 & $+0.070$ & $+0.004$ & 0.006 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "f5258b16-ba4f-4952-bbd3-a24d4795314c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032808 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direct…",
  "leafUuid": "74c4dc23-97ab-480a-836b-83d954f8201e",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate CaCLR cross-lingual calibration paper",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b"
}
```

---

### Tool call

_source line 23 · 2026-05-21T04:08:38.913Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014eRch91NbukAgXdprD5gDk`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74c4dc23-97ab-480a-836b-83d954f8201e",
  "isSidechain": false,
  "requestId": "req_011CbF4FqESCkwcQqoSLCqVb",
  "type": "assistant",
  "uuid": "d9fb77b0-0f6b-4ea7-afea-d0083d8f4fe0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQf5RMQqgnR3t2y8cRNTti",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15232,
      "cache_read_input_tokens": 53633,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15232,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 53633,
          "cache_creation_input_tokens": 15232,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15232
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-21T04:08:47.191Z_

<details><summary>↩ Tool result · `toolu_014eRch91NbukAgXdprD5gDk`</summary>

```text
&lt;persisted-output>
Output too large (59KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-xling-calib-direction/8a7b9e13-ea8b-4f7a-8439-83707f107d4b/tool-results/bdsb4e9l1.txt

Preview (first 2KB):
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
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9fb77b0-0f6b-4ea7-afea-d0083d8f4fe0",
  "isSidechain": false,
  "promptId": "21625223-a819-4abc-b0c5-9519cc481936",
  "type": "user",
  "uuid": "4cea6343-9caa-4531-b141-242497f47c93",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/adjustbox.sty\n(/usr/share/texlive/texmf-dist/tex/latex/xkeyval/xkeyval.sty\n(/usr/share/texlive/texmf-dist/tex/generic/xkeyval/xkeyval.tex\n(/usr/share/texlive/texmf-dist/tex/generic/xkeyval/xkvutils.tex)))\n(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/adjcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/trimclip.sty\n(/usr/share/texlive/texmf-dist/tex/latex/collectbox/collectbox.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/tc-pdftex.def))\n(/usr/share/texlive/texmf-dist/tex/latex/ifoddpage/ifoddpage.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/varwidth/varwidth.sty)\n==> First Aid for varwidth.sty applied!\n) (/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `huang2023look' on page 1 undefined on input l\nine 44.\n\n\nPackage natbib Warning: Citation `miao2026correctness' on page 1 undefined on i\nnput line 45.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nPackage natbib Warning: Citation `miao2026correctness' on page 2 undefined on i\nnput line 67.\n\n\nPackage natbib Warning: Citation `miao2026correctness' on page 2 undefined on i\nnput line 76.\n\n\nPackage natbib Warning: Citation `miao2026coral' on page 2 undefined on input l\nine 77.\n\n\nPackage natbib Warning: Citation `zhou2024lace' on page 2 undefined on input li\nne 78.\n\n\nPackage natbib Warning: Citation `xiao2025crosslingual' on page 2 undefined on \ninput line 82.\n\n\nPackage natbib Warning: Citation `civelli2025difficulty' on page 2 undefined on\n input line 84.\n\n\nOverfull \\hbox (0.83939pt too wide) in paragraph at lines 82--85\n []\\T1/cmr/bx/n/10.95 Cross-lingual prob-ing.[] ? \\T1/cmr/m/n/10.95 trans-fer k\nnowledge-boundary probes across 8 lan-guages, but knowl-\n\nOverfull \\hbox (14.13182pt too wide) in paragraph at lines 82--85\n\\T1/cmr/m/n/10.95 edge bound-aries (input-level an-swer-abil-ity) dif-fer fun-d\na-men-tally from cor-rect-ness (output-dependent\n\nPackage natbib Warning: Citation `bendavid2010theory' on page 2 undefined on in\nput line 87.\n\n\nPackage natbib Warning: Citation `zhao2019learning' on page 2 undefined on inpu\nt line 88.\n\n\nPackage natbib Warning: Citation `conneau2018word' on page 2 undefined on input\n line 91.\n\n\nPackage natbib Warning: Citation `artetxe2018robust' on page 2 undefined on inp\nut line 91.\n\n\nPackage natbib Warning: Citation `kornblith2019similarity' on page 2 undefined \non input line 95.\n\n\nPackage natbib Warning: Citation `angelopoulos2023conformal' on page 2 undefine\nd on input line 99.\n\n[2]\n\nLaTeX Warning: Reference `sec:probe_complexity' on page 3 undefined on input li\nne 119.\n\n\nLaTeX Warning: Reference `app:quantization' on page 3 undefined on input line 1\n74.\n\n[3]\n\nLaTeX Warning: Reference `tab:qwen_pareto' on page 4 undefined on input line 19\n3.\n\n\nLaTeX Warning: Reference `tab:transfer_conditions' on page 4 undefined on input\n line 226.\n\n\nLaTeX Warning: Reference `sec:caclr_results' on page 4 undefined on input line \n229.\n\n\nLaTeX Warning: Reference `tab:llama_pareto' on page 4 undefined on input line 2\n50.\n\n[4]\n\nLaTeX Warning: Reference `tab:caclr_main' on page 5 undefined on input line 282\n.\n\n\nLaTeX Warning: Reference `tab:ablation' on page 5 undefined on input line 320.\n\n[5]\n\nLaTeX Warning: Reference `tab:beta' on page 6 undefined on input line 344.\n\n\nLaTeX Warning: Reference `tab:decomp' on page 6 undefined on input line 370.\n\n\nLaTeX Warning: Reference `tab:depth_decomp' on page 6 undefined on input line 3\n96.\n\n\nLaTeX Warning: Reference `tab:cka' on page 6 undefined on input line 421.\n\n[6]\n\nLaTeX Warning: Reference `tab:subspace' on page 7 undefined on input line 445.\n\n\nLaTeX Warning: Reference `tab:orthogonality' on page 7 undefined on input line \n477.\n\n\nLaTeX Warning: Reference `tab:three_arch' on page 7 undefined on input line 507\n.\n\n\nLaTeX Warning: Reference `tab:benchmarks' on page 7 undefined on input line 534\n.\n\n[7]\n\nLaTeX Warning: Reference `tab:linproj' on page 8 undefined on input line 570.\n\n[8] [9]\n\nLaTeX Warning: Reference `tab:quant' on page 10 undefined on input line 717.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:control' on page 10 undefined on input line 762.\n\n[10]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nPackage natbib Warning: There were undefined citations.\n\n[11] [12] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 tcrm1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input tcrm1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymb.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [27] [29])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txgen.mf\n Ok [100] [109] [98] [99] [108])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymbol.mf\n Ok [13] [18] [21] [22] [23] [24] [25] [26] [28] [31] [32] [36] [39] [44]\n[45] [46] [42] [47] [60] [61] [62] [77] [79] [87] [110] [91] [93] [94] [95]\n[96] [126] [127] [128] [129] [130] [131] [132] [133] [134] [135] [136] [137]\n[138] [139] [140] [141] [142] [143] [144] [145] [146] [147] [148] [149]\n[150] [151] [152] [153] [154] [155] [156] [157] [158] [159] [160] [161]\n[162] [163] [164] [165] [166] [167] [168] [169] [171] [172] [173] [174]\n[175] [177] [176] [180] [181] [182] [183] [184] [187] [191] [214] [246])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txromod.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrsuper.mf\n Ok [185] [178] [179] [170] [186])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrfract.mf\n Ok [188] [189] [190]) ) ) )\n(some charht values had to be adjusted by as much as 0.06952pt)\nFont metrics written on tcrm1095.tfm.\nOutput written on tcrm1095.600gf (128 characters, 25592 bytes).\nTranscript written on tcrm1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk: successfully generated.\n\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecbx1200\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecbx1200\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx1200.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\nFont metrics written on ecbx1200.tfm.\nOutput written on ecbx1200.600gf (256 characters, 59220 bytes).\nTranscript written on ecbx1200.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk: successfully generated.\n &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm0800\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm0800\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm0800.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.06445pt)\nFont metrics written on ecrm0800.tfm.\nOutput written on ecrm0800.600gf (256 characters, 41732 bytes).\nTranscript written on ecrm0800.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk: successfully generated.\n &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecti1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecti1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecti1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecti.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/extextit.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exileast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilig.mf\n Ok [25] [26] [27] [28] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exitalp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exillett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exidigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exiligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.06808pt)\nFont metrics written on ecti1095.tfm.\nOutput written on ecti1095.600gf (256 characters, 57920 bytes).\nTranscript written on ecti1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk: successfully generated.\n &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecbx1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecbx1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\nFont metrics written on ecbx1095.tfm.\nOutput written on ecbx1095.600gf (256 characters, 54848 bytes).\nTranscript written on ecbx1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk: successfully generated.\n &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.07599pt)\nFont metrics written on ecrm1095.tfm.\nOutput written on ecrm1095.600gf (256 characters, 55424 bytes).\nTranscript written on ecrm1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk: successfully generated.\n &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecbx1440\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecbx1440\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx1440.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-xling-calib-direction/8a7b9e13-ea8b-4f7a-8439-83707f107d4b/tool-results/bdsb4e9l1.txt",
    "persistedOutputSize": 60424
  },
  "sourceToolAssistantUUID": "d9fb77b0-0f6b-4ea7-afea-d0083d8f4fe0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032808 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direct…",
  "leafUuid": "4cea6343-9caa-4531-b141-242497f47c93",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate CaCLR cross-lingual calibration paper",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b"
}
```

---

### Tool call

_source line 27 · 2026-05-21T04:08:50.381Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DCC7LMMNEj9Leuy27Zq9LZ`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/paper.pdf 2>/dev/null && echo \"PDF EXISTS\" || echo \"PDF MISSING\"",
  "description": "Check if PDF was generated"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cea6343-9caa-4531-b141-242497f47c93",
  "isSidechain": false,
  "requestId": "req_011CbF4GhKTrGbU9NgvPpTxY",
  "type": "assistant",
  "uuid": "3258d67d-ab73-4b31-873f-0381d1656f06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018e5LE4bWhSBmMV1FpW5gRg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1195,
      "cache_read_input_tokens": 68865,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1195,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 68865,
          "cache_creation_input_tokens": 1195,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1195
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-21T04:08:50.436Z_

<details><summary>↩ Tool result · `toolu_01DCC7LMMNEj9Leuy27Zq9LZ`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 275554 May 21 04:08 /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/paper.pdf
PDF EXISTS
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3258d67d-ab73-4b31-873f-0381d1656f06",
  "isSidechain": false,
  "promptId": "21625223-a819-4abc-b0c5-9519cc481936",
  "type": "user",
  "uuid": "5bb070b0-41f9-4d1d-b81f-e2cec7793b81",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 275554 May 21 04:08 /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/paper.pdf\nPDF EXISTS",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3258d67d-ab73-4b31-873f-0381d1656f06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-21T04:08:53.688Z_

PDF compiled successfully (276KB). Let me verify there are no critical LaTeX errors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bb070b0-41f9-4d1d-b81f-e2cec7793b81",
  "isSidechain": false,
  "requestId": "req_011CbF4GwCPZNm7ixZTYwN8A",
  "type": "assistant",
  "uuid": "5197fe3b-fa17-40e0-b2a7-8436a4fdb8db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGT3HnzZUzUm7HexWcBUkC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 70060,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 217,
          "cache_read_input_tokens": 70060,
          "cache_creation_input_tokens": 234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 234
          },
          "type": "message"
        }
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

_source line 30 · 2026-05-21T04:08:55.199Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017qfHKZ3mVp1dSHpayDHgMD`</summary>

```json
{
  "command": "grep -c \"^!\" /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/paper.log 2>/dev/null; grep \"Output written\" /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/paper.log | tail -1",
  "description": "Check LaTeX log for errors and output confirmation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5197fe3b-fa17-40e0-b2a7-8436a4fdb8db",
  "isSidechain": false,
  "requestId": "req_011CbF4GwCPZNm7ixZTYwN8A",
  "type": "assistant",
  "uuid": "c84e918d-1dbf-407d-bfc9-c97d2b48754b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGT3HnzZUzUm7HexWcBUkC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 70060,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 217,
          "cache_read_input_tokens": 70060,
          "cache_creation_input_tokens": 234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 234
          },
          "type": "message"
        }
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

_source line 31 · 2026-05-21T04:08:55.271Z_

<details><summary>↩ Tool result · `toolu_017qfHKZ3mVp1dSHpayDHgMD`</summary>

```text
0
Output written on paper.pdf (12 pages, 275554 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c84e918d-1dbf-407d-bfc9-c97d2b48754b",
  "isSidechain": false,
  "promptId": "21625223-a819-4abc-b0c5-9519cc481936",
  "type": "user",
  "uuid": "057a8024-6d1e-40b1-ba5a-d8394d6b9693",
  "toolUseResult": {
    "stdout": "0\nOutput written on paper.pdf (12 pages, 275554 bytes).",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "c84e918d-1dbf-407d-bfc9-c97d2b48754b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-21T04:08:55.276Z_

```json
{
  "parentUuid": "057a8024-6d1e-40b1-ba5a-d8394d6b9693",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6208477c-e7a9-4f99-8c3d-8548fd6d166d",
  "timestamp": "2026-05-21T04:08:55.276Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 33 · 2026-05-21T04:09:04.394Z_

论文已生成：12 页 PDF，0 个 LaTeX 错误。

文件位置：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/paper.pdf`

覆盖了 experiment_data.json 中全部 11 个实验：
- **主文**：Qwen3/Llama4 Pareto frontier (Tables 1-3)、CaCLR 主结果+消融+β敏感度 (Tables 4-6)、Difficulty decomposition (Tables 7-8)、CKA geometric analysis (Tables 9-10)、Orthogonality (Table 11)、三架构对比 (Table 12)、跨 benchmark 泛化 (Table 13)、Probe complexity、Linear projection sample efficiency (Table 14)
- **Appendix**：Quantization validation、Control tasks、Extended 53 languages、Llama4 linear projection

所有定量数字均来自 experiment_data.json，无编造。Headline claim: CaCLR reduces non-English ECE by 22% vs temperature scaling (0.121 vs 0.155)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6208477c-e7a9-4f99-8c3d-8548fd6d166d",
  "isSidechain": false,
  "requestId": "req_011CbF4HJ1HMtDKfbjq2tZxg",
  "type": "assistant",
  "uuid": "ac970919-ce96-4b4a-b3d5-920993965ca8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R8eV4WpEiMbtziEsqZcZhX",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 351,
      "cache_read_input_tokens": 70294,
      "output_tokens": 320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 351,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 320,
          "cache_read_input_tokens": 70294,
          "cache_creation_input_tokens": 351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 351
          },
          "type": "message"
        }
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032808 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direct…",
  "leafUuid": "ac970919-ce96-4b4a-b3d5-920993965ca8",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate CaCLR cross-lingual calibration paper",
  "sessionId": "8a7b9e13-ea8b-4f7a-8439-83707f107d4b"
}
```

---
