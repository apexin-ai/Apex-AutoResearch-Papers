# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T222113 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/67977da3-950c-4fc5-98d2-407cc2c60bff.jsonl`
- **Structured JSON:** [`2d9a07b87e45a27efc83.json`](../../sessions/2d/2d9a07b87e45a27efc83.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T23:19:08.607Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T23:19:08.607Z",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T222113 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Soften \"systematic gradient\" to \"benchmark-conditional variance structure\" or \"task-type clustering.\" Cross-benchmark pattern is 2-cluster ({MMLU, ARC} high item dominance vs {GSM8K, HellaSwag} lower), not a clean monotonic 4-point gradient. Item dominance remains dominant on knowledge benchmarks but magnitude is less precise than MVP suggested once model-as-facet is handled and bootstrap CIs computed. Separability holds on knowledge benchmarks but GSM8K shows infra×method ~3% under binary scoring, requiring benchmark+metric qualification on Claim 2. Bootstrap CIs on gradient endpoints overlap partially — directional claims hold, magnitude claims are imprecise. Reframe hook: \"the variance structure itself depends on what you're benchmarking\" rather than a clean ordering. FP32 degradation is real (not engine confound), position as known finding (Yuan 2025) with novel item-level G-theory breakdown. Model-as-facet absorption (21% on MMLU) reframes prior single-model studies as having overestimated pure item dominance — turn this into a feature, not a weakness. Target AAAI with adjusted framing; if exp-008 (MATH) is feasible and strengthens the clustering to 3-tier, include it; otherwise ACL ARR October is a comfortable fallback.\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T23:19:08.610Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T23:19:08.610Z",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff"
}
```

---

## Round 1

35 recorded events

### User

_source line 3 · 2026-05-20T23:19:08.638Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T222113 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Soften "systematic gradient" to "benchmark-conditional variance structure" or "task-type clustering." Cross-benchmark pattern is 2-cluster ({MMLU, ARC} high item dominance vs {GSM8K, HellaSwag} lower), not a clean monotonic 4-point gradient. Item dominance remains dominant on knowledge benchmarks but magnitude is less precise than MVP suggested once model-as-facet is handled and bootstrap CIs computed. Separability holds on knowledge benchmarks but GSM8K shows infra×method ~3% under binary scoring, requiring benchmark+metric qualification on Claim 2. Bootstrap CIs on gradient endpoints overlap partially — directional claims hold, magnitude claims are imprecise. Reframe hook: "the variance structure itself depends on what you're benchmarking" rather than a clean ordering. FP32 degradation is real (not engine confound), position as known finding (Yuan 2025) with novel item-level G-theory breakdown. Model-as-facet absorption (21% on MMLU) reframes prior single-model studies as having overestimated pure item dominance — turn this into a feature, not a weakness. Target AAAI with adjusted framing; if exp-008 (MATH) is feasible and strengthens the clustering to 3-tier, include it; otherwise ACL ARR October is a comfortable fallback.

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "c5460e05-f609-42c9-9ad5-28993b47482a",
  "type": "user",
  "uuid": "d4c214cd-3ec3-4277-aef8-434bab5dbfd1",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T23:19:08.637Z_

```json
{
  "parentUuid": "d4c214cd-3ec3-4277-aef8-434bab5dbfd1",
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
  "uuid": "15a25e6a-48da-435b-a80a-2ba859a8c475",
  "timestamp": "2026-05-20T23:19:08.637Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T23:19:08.638Z_

```json
{
  "parentUuid": "15a25e6a-48da-435b-a80a-2ba859a8c475",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e2ae2bc5-931f-419d-ad06-bf798da4960a",
  "timestamp": "2026-05-20T23:19:08.638Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
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
  "aiTitle": "Generate complete simulation paper for dream_20260520T222113",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff"
}
```

---

### Assistant

_source line 7 · 2026-05-20T23:19:15.196Z_

I'll start by reading the input files to understand the experimental data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2ae2bc5-931f-419d-ad06-bf798da4960a",
  "isSidechain": false,
  "requestId": "req_011CbEgBehkSX4aGpEWWSnk4",
  "type": "assistant",
  "uuid": "ca2510e3-ac45-4474-8eda-38b5ee93c87c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JNUmXNC745qN86wDR1NZ9L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11638,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11638,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11638,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11638
          },
          "type": "message"
        }
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

_source line 8 · 2026-05-20T23:19:15.636Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RPGTPAeXPSAc3jB5qHuKgu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca2510e3-ac45-4474-8eda-38b5ee93c87c",
  "isSidechain": false,
  "requestId": "req_011CbEgBehkSX4aGpEWWSnk4",
  "type": "assistant",
  "uuid": "efabf9ac-c786-4d8d-baae-bf4a4ff7b9d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JNUmXNC745qN86wDR1NZ9L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11638,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11638,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11638,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11638
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-20T23:19:15.984Z_

<details><summary>↩ Tool result · `toolu_01RPGTPAeXPSAc3jB5qHuKgu`</summary>

```text
1	[
2	  {
3	    "name": "Full-scale MMLU precision study (confound-fixed)",
4	    "description": "4 models × 3 precisions (FP32/BF16/FP16, all V0 enforce_eager) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items (stratified). 1,036,800 total observations.\n",
5	    "results": {
6	      "total_observations": 1036800,
7	      "total_conditions": 5184,
8	      "accuracy_fp32": 0.655,
9	      "accuracy_bf16": 0.684,
10	      "accuracy_fp16": 0.681,
11	      "accuracy_gap_fp32_bf16_pp": 2.9,
12	      "accuracy_gap_bf16_fp16_pp": 0.3,
13	      "accuracy_by_model": {
14	        "qwen3_8b": {
15	          "fp32": 0.695,
16	          "bf16": 0.71,
17	          "fp16": 0.706
18	        },
19	        "llama31_8b": {
20	          "fp32": 0.6,
21	          "bf16": 0.672,
22	          "fp16": 0.669
23	        },
24	        "gemma2_9b": {
25	          "fp32": 0.638,
26	          "bf16": 0.66,
27	          "fp16": 0.658
28	        },
29	        "mistral_7b": {
30	          "fp32": 0.688,
31	          "bf16": 0.694,
32	          "fp16": 0.691
33	        }
34	      },
35	      "item_id_variance_binary": 0.52,
36	      "residual_variance_binary": 0.14,
37	      "precision_x_item_binary": 0.05,
38	      "prompt_x_item_binary": 0.058,
39	      "temperature_x_item_binary": 0.055,
40	      "seed_x_item_binary": 0.028,
41	      "precision_main_binary": 0.03,
42	      "temperature_main_binary": 0.015,
43	      "prompt_main_binary": 0.008,
44	      "ordering_main_binary": 0.002,
45	      "precision_x_temperature_binary": 0.002,
46	      "precision_x_prompt_binary": 0.001,
47	      "precision_x_seed_binary": 0.001,
48	      "other_binary": 0.09,
49	      "residual_textmatch": 0.36,
50	      "prompt_x_item_textmatch": 0.33,
51	      "temperature_main_textmatch": 0.14,
52	      "precision_x_item_textmatch": 0.04,
53	      "precision_x_temperature_textmatch": 0.022,
54	      "temperature_x_item_textmatch": 0.03,
55	      "item_id_textmatch": 0.03,
56	      "precision_main_textmatch": 0.025,
57	      "other_textmatch": 0.023,
58	      "g_correct_binary": 0.37,
59	      "g_correct_textmatch": 0.97,
60	      "item_id_rank_corr_across_models": 0.82,
61	      "fp32_gap_model_range_pp": [
62	        1.5,
63	        7.2
64	      ]
65	    },
66	    "tables": [
67	      {
68	        "name": "Table 1: MMLU Variance Decomposition — Binary Correct (Basic, Model Pooled)",
69	        "columns": [
70	          "Source",
71	          "% Total Variance"
72	        ],
73	        "rows": [
74	          [
75	            "item_id",
76	            "52.0%"
77	          ],
78	          [
79	            "residual (includes model effects)",
80	            "14.0%"
81	          ],
82	          [
83	            "prompt:item",
84	            "5.8%"
85	          ],
86	          [
87	            "temperature:item",
88	            "5.5%"
89	          ],
90	          [
91	            "precision:item",
92	            "5.0%"
93	          ],
94	          [
95	            "precision (main)",
96	            "3.0%"
97	          ],
98	          [
99	            "seed:item",
100	            "2.8%"
101	          ],
102	          [
103	            "temperature (main)",
104	            "1.5%"
105	          ],
106	          [
107	            "prompt (main)",
108	            "0.8%"
109	          ],
110	          [
111	            "infra×method (all)",
112	            "0.4%"
113	          ],
114	          [
115	            "ordering",
116	            "0.2%"
117	          ],
118	          [
119	            "other 2-way / 3-way",
120	            "9.0%"
121	          ]
122	        ]
123	      },
124	      {
125	        "name": "Table 2: MMLU Variance Decomposition — Text Exact Match (Basic)",
126	        "columns": [
127	          "Source",
128	          "% Total Variance"
129	        ],
130	        "rows": [
131	          [
132	            "residual",
133	            "36.0%"
134	          ],
135	          [
136	            "prompt:item",
137	            "33.0%"
138	          ],
139	          [
140	            "temperature (main)",
141	            "14.0%"
142	          ],
143	          [
144	            "precision:item",
145	            "4.0%"
146	          ],
147	          [
148	            "temperature:item",
149	            "3.0%"
150	          ],
151	          [
152	            "item_id",
153	            "3.0%"
154	          ],
155	          [
156	            "precision (main)",
157	            "2.5%"
158	          ],
159	          [
160	            "precision×temperature",
161	            "2.2%"
162	          ],
163	          [
164	            "other",
165	            "2.3%"
166	          ]
167	        ]
168	      },
169	      {
170	        "name": "Table 3: Per-Model Accuracy by Precision (V0 enforce_eager)",
171	        "columns": [
172	          "Model",
173	          "FP32",
174	          "BF16",
175	          "FP16",
176	          "FP32-BF16 Gap"
177	        ],
178	        "rows": [
179	          [
180	            "Qwen3-8B-Instruct",
181	            "0.695",
182	            "0.710",
183	            "0.706",
184	            "1.5pp"
185	          ],
186	          [
187	            "Llama-3.1-8B-Instruct",
188	            "0.600",
189	            "0.672",
190	            "0.669",
191	            "7.2pp"
192	          ],
193	          [
194	            "Gemma-2-9B-IT",
195	            "0.638",
196	            "0.660",
197	            "0.658",
198	            "2.2pp"
199	          ],
200	          [
201	            "Mistral-7B-v0.3",
202	            "0.688",
203	            "0.694",
204	            "0.691",
205	            "0.6pp"
206	          ],
207	          [
208	            "Average",
209	            "0.655",
210	            "0.684",
211	            "0.681",
212	            "2.9pp"
213	          ]
214	        ]
215	      }
216	    ],
217	    "figures": [],
218	    "analysis": "Key finding: FP32 degradation is REAL, not an engine confound. The bf16_eager_disentangle result is confirmed at scale — V0 enforce_eager changes nothing substantial. This reframes the contribution: we provide the first item-level G-theory decomposition of precision effects, showing that precision:item (5%) exceeds precision main (3%). The model-dependence of FP32 degradation (1.5-7.2pp) is novel and suggests training-time precision choices affect inference robustness. For the paper: position FP32 degradation as supporting Yuan et al. (2025) with novel item×model granularity, NOT as a primary finding. Separability on MMLU is confirmed: infra×method = 0.4% binary, 2.2% text-match (precision×temperature only). CIs deferred to exp-004.\n\n\nV0 enforce_eager for all precisions eliminates the 0.22pp engine confound (bf16_eager_disentangle) but the FP32 accuracy gap PERSISTS at ~2.9pp average — confirming the disentangle conclusion that 97.4% of the gap was genuine precision effect. FP32 degradation is strongly model-dependent: Llama-3.1-8B shows 7.2pp gap (consistent with MVP's 8.5pp on this model) while Qwen3-8B shows only 1.5pp, likely because Qwen's training used mixed-precision strategies that are more robust to FP32 inference rounding. Precision main effect at 3% is real but dwarfed by item_id at 52%. Precision:item at 5% means certain items (those near decision boundaries) are disproportionately affected — this is the novel item-level breakdown that extends Yuan et al. (2025). Item_id at 52% is lower than MVP's 58.4% because 200 stratified items (vs 50) include more mid-difficulty items that reduce between-item variance, and pooling across 4 models absorbs some item-specific variance into residual. Residual at 14% is inflated because model effects are pooled — exp-004 will decompose this. G=0.37 replicates MVP's 0.357, confirming item dominance makes G≥0.90 unreachable without massive item expansion. Text-match scoring replicates the qualitative shift: prompt:item dominates (33%), precision×temperature at 2.2% (consistent with MVP's 1.3% but larger due to more conditions), driven by floating-point non-associativity in generation.\n"
219	  },
220	  {
221	    "name": "Item resampling stability test",
222	    "description": "3 independent stratified samples of 200 MMLU items (seeds 0, 7, 99) × Llama-3.1-8B × 3 precisions × 3 prompts × 3 seeds × 2 orderings = 54 conditions/sample, 32,400 obs/sample.\n",
223	    "results": {
224	      "item_id_sample_0": 0.49,
225	      "item_id_sample_7": 0.55,
226	      "item_id_sample_99": 0.44,
227	      "item_id_mean": 0.493,
228	      "item_id_sd": 0.055,
229	      "item_id_cv": 0.19,
230	      "g_coeff_sample_0": 0.36,
231	      "g_coeff_sample_7": 0.32,
232	      "g_coeff_sample_99": 0.39,
233	      "accuracy_sample_0": 0.668,
234	      "accuracy_sample_7": 0.641,
235	      "accuracy_sample_99": 0.679,
236	      "mean_item_difficulty_sample_0": 0.5,
237	      "mean_item_difficulty_sample_7": 0.42,
238	      "mean_item_difficulty_sample_99": 0.54,
239	      "sd_item_difficulty_sample_0": 0.28,
240	      "sd_item_difficulty_sample_7": 0.32,
241	      "sd_item_difficulty_sample_99": 0.25,
242	      "rank_order_top3_sources_preserved": true,
243	      "residual_cv": 0.11,
244	      "prompt_item_cv": 0.09
245	    },
246	    "tables": [
247	      {
248	        "name": "Table 4: Resampling Stability of Variance Components",
249	        "columns": [
250	          "Source",
251	          "Sample 0",
252	          "Sample 7",
253	          "Sample 99",
254	          "Mean",
255	          "CV"
256	        ],
257	        "rows": [
258	          [
259	            "item_id",
260	            "49.0%",
261	            "55.0%",
262	            "44.0%",
263	            "49.3%",
264	            "0.19"
265	          ],
266	          [
267	            "residual",
268	            "17.5%",
269	            "15.0%",
270	            "19.5%",
271	            "17.3%",
272	            "0.11"
273	          ],
274	          [
275	            "prompt:item",
276	            "6.5%",
277	            "6.0%",
278	            "7.0%",
279	            "6.5%",
280	            "0.09"
281	          ],
282	          [
283	            "temp:item",
284	            "5.8%",
285	            "5.2%",
286	            "6.5%",
287	            "5.8%",
288	            "0.10"
289	          ],
290	          [
291	            "prec:item",
292	            "5.0%",
293	            "5.5%",
294	            "4.2%",
295	            "4.9%",
296	            "0.12"
297	          ],
298	          [
299	            "precision",
300	            "3.0%",
301	            "3.5%",
302	            "2.8%",
303	            "3.1%",
304	            "0.10"
305	          ],
306	          [
307	            "other",
308	            "13.2%",
309	            "9.8%",
310	            "16.0%",
311	            "13.0%",
312	            "—"
313	          ]
314	        ]
315	      },
316	      {
317	        "name": "Table 5: Per-Sample Summary Statistics",
318	        "columns": [
319	          "Metric",
320	          "Sample 0",
321	          "Sample 7",
322	          "Sample 99"
323	        ],
324	        "rows": [
325	          [
326	            "N items",
327	            "200",
328	            "200",
329	            "200"
330	          ],
331	          [
332	            "Mean item difficulty",
333	            "0.50",
334	            "0.42",
335	            "0.54"
336	          ],
337	          [
338	            "SD item difficulty",
339	            "0.28",
340	            "0.32",
341	            "0.25"
342	          ],
343	          [
344	            "Overall accuracy",
345	            "0.668",
346	            "0.641",
347	            "0.679"
348	          ],
349	          [
350	            "G (binary)",
351	            "0.36",
352	            "0.32",
353	            "0.39"
354	          ],
355	          [
356	            "item_id %",
357	            "49.0%",
358	            "55.0%",
359	            "44.0%"
360	          ]
361	        ]
362	      }
363	    ],
364	    "figures": [],
365	    "analysis": "The 19% CV is the paper's best defense against \"you just got lucky with your items.\" It quantifies the item-sampling uncertainty that plagues every single-draw benchmark study. Rank ordering is robust (item_id always #1) but precise magnitude depends on which items you drew — explaining why Mesting (2026) and Brittlebench (2026) reached different headline numbers on different item sets. For the paper: always report item_id as a range (44-55%) not a point. D-study projections from exp-004 should include CIs that account for this resampling instability.\n\n\nCV of 19% reflects meaningful item-sampling uncertainty. MMLU has 14,042 items across 57 subjects with heterogeneous difficulty; stratified sampling with 200 items (1.4%) leaves substantial sampling variance especially in the tails. Sample 7 draws more hard items (mean difficulty 0.42), inflating between-item variance to 55% because the difficulty spread is wider (SD 0.32). Sample 99 draws more mid-difficulty items (mean 0.54, SD 0.25), compressing item_id to 44% because items cluster around the center. Despite magnitude variation, the qualitative hierarchy is preserved: item_id ranks #1 in all 3 samples, residual #2, prompt:item #3. This stability-in-rank with instability-in-magnitude is the key finding: the headline claim \"item dominance ~50%\" needs error bars, reported as \"44-55% across independent 200-item stratified draws.\" The G-coefficient varies inversely (0.32-0.39) because higher item variance = lower generalizability of the benchmark score. This directly motivates D-study item-count recommendations with CIs, not point estimates — if your headline variance component shifts ±5pp with a different item draw, your optimal resource allocation shifts too.\n"
366	  },
367	  {
368	    "name": "Multi-benchmark replication (GSM8K, ARC, HellaSwag)",
369	    "description": "4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures × 4 orderings × 200 items on GSM8K, ARC-Challenge, HellaSwag. Reduced crossing vs exp-001.\n",
370	    "results": {
371	      "total_observations_per_benchmark": 384000,
372	      "gsm8k_accuracy": 0.575,
373	      "gsm8k_item_id_binary": 0.4,
374	      "gsm8k_residual_binary": 0.15,
375	      "gsm8k_temp_x_item_binary": 0.1,
376	      "gsm8k_seed_x_item_binary": 0.07,
377	      "gsm8k_prompt_x_item_binary": 0.065,
378	      "gsm8k_temperature_binary": 0.04,
379	      "gsm8k_prec_x_temp_binary": 0.022,
380	      "gsm8k_prec_x_seed_binary": 0.005,
381	      "gsm8k_prec_x_prompt_binary": 0.003,
382	      "gsm8k_infra_x_method_total_binary": 0.03,
383	      "gsm8k_precision_main_binary": 0.01,
384	      "gsm8k_prec_x_item_binary": 0.015,
385	      "gsm8k_other_binary": 0.093,
386	      "gsm8k_g_correct_binary": 0.42,
387	      "arc_accuracy": 0.625,
388	      "arc_item_id_binary": 0.5,
389	      "arc_residual_binary": 0.12,
390	      "arc_prompt_x_item_binary": 0.085,
391	      "arc_temp_x_item_binary": 0.055,
392	      "arc_seed_x_item_binary": 0.04,
393	      "arc_prec_x_item_binary": 0.025,
394	      "arc_temperature_binary": 0.025,
395	      "arc_precision_binary": 0.01,
396	      "arc_infra_x_method_total_binary": 0.005,
397	      "arc_other_binary": 0.115,
398	      "arc_g_correct_binary": 0.35,
399	      "hellaswag_accuracy": 0.712,
400	      "hellaswag_item_id_binary": 0.35,
401	      "hellaswag_residual_binary": 0.18,
402	      "hellaswag_temp_x_item_binary": 0.095,
403	      "hellaswag_seed_x_item_binary": 0.085,
404	      "hellaswag_prompt_x_item_binary": 0.075,
405	      "hellaswag_temperature_binary": 0.045,
406	      "hellaswag_prec_x_item_binary": 0.015,
407	      "hellaswag_precision_binary": 0.005,
408	      "hellaswag_infra_x_method_total_binary": 0.003,
409	      "hellaswag_other_binary": 0.127,
410	      "hellaswag_g_correct_binary": 0.48,
411	      "gradient_pattern": "2-cluster: {MMLU 52%, ARC 50%} vs {GSM8K 40%, HellaSwag 35%}",
412	      "gradient_spread_pp": 17,
413	      "within_cluster_ordering_reliable": false,
414	      "gsm8k_prec_x_temp_textmatch": 0.035,
415	      "arc_prec_x_temp_textmatch": 0.022,
416	      "hellaswag_prec_x_temp_textmatch": 0.016,
417	      "infra_x_method_textmatch_max": 0.035
418	    },
419	    "tables": [
420	      {
421	        "name": "Table 6: Cross-Benchmark Variance Decomposition — Binary (Basic, Model Pooled)",
422	        "columns": [
423	          "Source",
424	          "MMLU",
425	          "GSM8K",
426	          "ARC",
427	          "HellaSwag"
428	        ],
429	        "rows": [
430	          [
431	            "item_id",
432	            "52.0%",
433	            "40.0%",
434	            "50.0%",
435	            "35.0%"
436	          ],
437	          [
438	            "residual",
439	            "14.0%",
440	            "15.0%",
441	            "12.0%",
442	            "18.0%"
443	          ],
444	          [
445	            "temp:item",
446	            "5.5%",
447	            "10.0%",
448	            "5.5%",
449	            "9.5%"
450	          ],
451	          [
452	            "seed:item",
453	            "2.8%",
454	            "7.0%",
455	            "4.0%",
456	            "8.5%"
457	          ],
458	          [
459	            "prompt:item",
460	            "5.8%",
461	            "6.5%",
462	            "8.5%",
463	            "7.5%"
464	          ],
465	          [
466	            "prec:item",
467	            "5.0%",
468	            "1.5%",
469	            "2.5%",
470	            "1.5%"
471	          ],
472	          [
473	            "precision (main)",
474	            "3.0%",
475	            "1.0%",
476	            "1.0%",
477	            "0.5%"
478	          ],
479	          [
480	            "temperature (main)",
481	            "1.5%",
482	            "4.0%",
483	            "2.5%",
484	            "4.5%"
485	          ],
486	          [
487	            "infra×method (total)",
488	            "0.4%",
489	            "3.0%",
490	            "0.5%",
491	            "0.3%"
492	          ],
493	          [
494	            "other",
495	            "10.0%",
496	            "12.0%",
497	            "13.5%",
498	            "14.7%"
499	          ]
500	        ]
501	      },
502	      {
503	        "name": "Table 7: Cross-Benchmark Summary (Basic)",
504	        "columns": [
505	          "Benchmark",
506	          "Task Type",
507	          "item_id %",
508	          "G (binary)",
509	          "infra×method",
510	          "Cluster"
511	        ],
512	        "rows": [
513	          [
514	            "MMLU",
515	            "Knowledge",
516	            "52.0%",
517	            "0.37",
518	            "0.4%",
519	            "High"
520	          ],
521	          [
522	            "ARC-Challenge",
523	            "Knowledge/Science",
524	            "50.0%",
525	            "0.35",
526	            "0.5%",
527	            "High"
528	          ],
529	          [
530	            "GSM8K",
531	            "Math reasoning",
532	            "40.0%",
533	            "0.42",
534	            "3.0%",
535	            "Low"
536	          ],
537	          [
538	            "HellaSwag",
539	            "Commonsense",
540	            "35.0%",
541	            "0.48",
542	            "0.3%",
543	            "Low"
544	          ]
545	        ]
546	      },
547	      {
548	        "name": "Table 8: GSM8K Infra×Method Interaction Breakdown (Binary)",
549	        "columns": [
550	          "Interaction",
551	          "% Total Variance",
552	          "95% CI (bootstrap, exp-004)"
553	        ],
554	        "rows": [
555	          [
556	            "precision×temperature",
557	            "2.2%",
558	            "deferred"
559	          ],
560	          [
561	            "precision×seed",
562	            "0.5%",
563	            "deferred"
564	          ],
565	          [
566	            "precision×prompt",
567	            "0.3%",
568	            "deferred"
569	          ],
570	          [
571	            "Total infra×method",
572	            "3.0%",
573	            "deferred"
574	          ]
575	        ],
576	        "note": "Only GSM8K exceeds 1% threshold. MMLU 0.4%, ARC 0.5%, HellaSwag 0.3%."
577	      }
578	    ],
579	    "figures": [],
580	    "analysis": "This is the core finding. The 2-cluster pattern is clear and the direction is robust, but it is NOT the clean monotonic gradient originally hypothesized. ARC clusters with MMLU (not intermediate) — this is actually a stronger finding than a gradient: variance structure tracks cognitive demand, and ARC's \"science reasoning\" label is misleading. The GSM8K infra×method at 3% binary is the median tier's key complication for Claim 2: separability is benchmark-conditional, not universal. The paper must add \"on knowledge-retrieval benchmarks\" or \"when math reasoning is excluded\" to the separability claim. Under text-match, GSM8K reaches 3.5% (within target [1.5%, 4.5%]). Practical implication: practitioners evaluating math reasoning on GSM8K should fix both precision AND temperature to minimize infra×method confounding.\n\n\nThe 2-cluster pattern emerges because variance structure tracks cognitive demand, not benchmark labels. Knowledge-retrieval benchmarks (MMLU, ARC) show high item dominance (50-52% basic) because item difficulty is the primary driver — items test factual knowledge that is either present or absent in the model, and this binary state dominates across conditions. ARC clusters with MMLU despite being labeled \"science reasoning\" because most ARC items are effectively factual recall (what happens when ice melts?) rather than multi-step inference. Reasoning benchmarks (GSM8K, HellaSwag) show lower item dominance (35-40%) because temperature and seed interact strongly with items: multi-step reasoning and commonsense inference have multiple valid processing paths, and sampling randomness determines which path is taken, shifting variance from item_id to interaction terms. GSM8K item dominance at 40% is above the hypothesized 20-30% because even math reasoning has trivially easy items (single-step arithmetic) and impossible items (complex multi-step for 8B models), creating a floor of item-driven variance. The critical median-tier finding: GSM8K shows infra×method = 3.0% under binary scoring (precision×temperature 2.2% + precision×seed 0.5% + precision×prompt 0.3%). This breaks universal separability. The mechanism: math generation produces longer chains-of-thought where BF16 vs FP16 accumulation differences compound; temperature controls how aggressively alternative reasoning paths are explored; the precision×temperature combination can push probability distributions past decision boundaries, flipping the final numerical answer. Binary scoring captures this because the extracted number differs. Other benchmarks show infra×method <0.5% binary — the effect is GSM8K-specific. Under text-match, GSM8K prec×temp reaches 3.5% because exact-string comparison of multi-step outputs amplifies floating-point divergence. The gradient spread of 17pp (MMLU 52% vs HellaSwag 35%, basic) is within the target range [10-24pp]; after model-as-facet correction in exp-004 it will be similar (48% vs 31% = 17pp).\n"
581	  },
582	  {
583	    "name": "Multi-hardware G-study",
584	    "description": "4 models × 2 GPU types (RTX PRO 6000 + second GPU) × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items.\n",
585	    "results": {
586	      "total_observations": 1152000,
587	      "hardware_main_binary": 0.004,
588	      "hardware_x_precision_binary": 0.008,
589	      "hardware_x_temperature_binary": 0.003,
590	      "hardware_x_seed_binary": 0.002,
591	      "hardware_x_prompt_binary": 0.001,
592	      "hardware_x_methodology_total_binary": 0.014,
593	      "hardware_x_item_binary": 0.018,
594	      "total_hardware_related_binary": 0.036,
595	      "hardware_main_textmatch": 0.012,
596	      "hardware_x_precision_textmatch": 0.022,
597	      "hardware_x_methodology_total_textmatch": 0.032,
598	      "hardware_x_item_textmatch": 0.028,
599	      "total_hardware_related_textmatch": 0.072,
600	      "item_id_with_hardware_binary": 0.5,
601	      "g_correct_binary_gpu1": 0.37,
602	      "g_correct_binary_gpu2": 0.36,
603	      "cross_gpu_gap_bf16_mean_pp": 0.12,
604	      "cross_gpu_gap_fp16_mean_pp": 0.75,
605	      "cross_gpu_gap_bf16_max_pp": 0.2,
606	      "cross_gpu_gap_fp16_max_pp": 1.1,
607	      "model_ranking_preserved_across_gpus": true,
608	      "hardware_variance_fp16_subset": 0.022,
609	      "hardware_variance_bf16_subset": 0.003
610	    },
611	    "tables": [
612	      {
613	        "name": "Table 9: Hardware Facet Variance Components",
614	        "columns": [
615	          "Source",
616	          "Binary %",
617	          "Text-match %"
618	        ],
619	        "rows": [
620	          [
621	            "hardware (main)",
622	            "0.4%",
623	            "1.2%"
624	          ],
625	          [
626	            "hardware×precision",
627	            "0.8%",
628	            "2.2%"
629	          ],
630	          [
631	            "hardware×temperature",
632	            "0.3%",
633	            "0.6%"
634	          ],
635	          [
636	            "hardware×seed",
637	            "0.2%",
638	            "0.4%"
639	          ],
640	          [
641	            "hardware×prompt",
642	            "0.1%",
643	            "0.3%"
644	          ],
645	          [
646	            "hardware×item",
647	            "1.8%",
648	            "2.8%"
649	          ],
650	          [
651	            "Total hardware-related",
652	            "3.6%",
653	            "7.5%"
654	          ]
655	        ]
656	      },
657	      {
658	        "name": "Table 10: Cross-GPU Accuracy by Model and Precision",
659	        "columns": [
660	          "Model",
661	          "GPU1-BF16",
662	          "GPU2-BF16",
663	          "Δ(pp)",
664	          "GPU1-FP16",
665	          "GPU2-FP16",
666	          "Δ(pp)"
667	        ],
668	        "rows": [
669	          [
670	            "Qwen3-8B",
671	            "0.710",
672	            "0.709",
673	            "0.1",
674	            "0.706",
675	            "0.700",
676	            "0.6"
677	          ],
678	          [
679	            "Llama-3.1-8B",
680	            "0.672",
681	            "0.672",
682	            "0.0",
683	            "0.669",
684	            "0.661",
685	            "0.8"
686	          ],
687	          [
688	            "Gemma-2-9B",
689	            "0.660",
690	            "0.659",
691	            "0.1",
692	            "0.658",
693	            "0.649",
694	            "0.9"
695	          ],
696	          [
697	            "Mistral-7B",
698	            "0.694",
699	            "0.693",
700	            "0.1",
701	            "0.691",
702	            "0.680",
703	            "1.1"
704	          ]
705	        ]
706	      },
707	      {
708	        "name": "Table 11: Hardware Effect Conditioned on Precision",
709	        "columns": [
710	          "Metric",
711	          "BF16 Only",
712	          "FP16 Only"
713	        ],
714	        "rows": [
715	          [
716	            "Hardware % total variance",
717	            "0.3%",
718	            "2.2%"
719	          ],
720	          [
721	            "Mean cross-GPU gap (pp)",
722	            "0.12",
723	            "0.75"
724	          ],
725	          [
726	            "Max cross-GPU gap (pp)",
727	            "0.2",
728	            "1.1"
729	          ]
730	        ]
731	      }
732	    ],
733	    "figures": [],
734	    "analysis": "Hardware is a manageable confound, not a showstopper. Separability claim (Claim 2) survives with qualification: \"hardware×methodology is ≤1.4% under binary scoring\" — but the FP16 hardware sensitivity (2.2% when conditioned on FP16) warrants a Discussion paragraph. Practical recommendation: prefer BF16 for hardware-independent reproducibility; if FP16 is necessary for memory, acknowledge ~1pp cross-GPU uncertainty. The hardware×item overlap with precision×item suggests a unified \"logit perturbation\" mechanism — items near decision boundaries are vulnerable to both precision and hardware nondeterminism. This is a potential Discussion point but not a formal claim.\n\n\nHardware main effect at 0.4% binary is negligible because both GPUs implement the same IEEE 754 operations; differences arise only from CUDA kernel scheduling nondeterminism and memory subsystem timing. The critical finding is hardware×precision at 0.8% binary: FP16 is more hardware-sensitive than BF16 (cross-GPU gap 0.75pp vs 0.12pp), because FP16's narrower dynamic range (5-bit exponent vs BF16's 8-bit) makes accumulation order hardware-dependent — consistent with Yuan et al. (2025). When subsetting to FP16-only data, hardware explains 2.2% of variance (within median narrative's \"1-3% on one precision\"). Under text-match, hardware effects roughly double (total 7.2%) because different GPU kernel orderings produce different final tokens in long generations, amplified by exact-match scoring. Hardware×item at 1.8% binary means certain items near decision boundaries are hardware-sensitive — the same items that are precision-sensitive (prec:item) are also hardware-sensitive, consistent with a shared mechanism of logit perturbation near thresholds. Model rankings are fully preserved across GPUs (Kendall tau = 1.0 at all condition combinations) — hardware effects are far too small to alter comparative model evaluation. Total hardware-related variance at 3.6% binary is manageable but nonzero, requiring \"approximately separable\" language.\n"
735	  },
736	  {
737	    "name": "Comprehensive combined analysis",
738	    "description": "Reanalysis of all exp-001/001b/002/003 data: (a) model-as-facet G-theory, (b) bootstrap CIs (1000 resamples), (c) D-study projections, (d) REML vs Henderson, (e) logprob scoring, (f) ranking stability, (g) higher-order interactions.\n",
739	    "results": {
740	      "mmlu_item_id_model_facet": 0.48,
741	      "mmlu_model_main": 0.05,
742	      "mmlu_model_x_item": 0.21,
743	      "mmlu_residual_model_facet": 0.08,
744	      "mmlu_prompt_item_model_facet": 0.053,
745	      "mmlu_temp_item_model_facet": 0.048,
746	      "mmlu_prec_item_model_facet": 0.028,
747	      "mmlu_precision_main_model_facet": 0.025,
748	      "mmlu_temperature_main_model_facet": 0.012,
749	      "gsm8k_item_id_model_facet": 0.36,
750	      "gsm8k_model_x_item": 0.18,
751	      "gsm8k_model_main": 0.04,
752	      "arc_item_id_model_facet": 0.46,
753	      "arc_model_x_item": 0.16,
754	      "arc_model_main": 0.04,
755	      "hellaswag_item_id_model_facet": 0.31,
756	      "hellaswag_model_x_item": 0.19,
757	      "hellaswag_model_main": 0.05,
758	      "item_id_reduction_mmlu_pp": 4.0,
759	      "item_id_reduction_gsm8k_pp": 4.0,
760	      "item_id_reduction_arc_pp": 4.0,
761	      "item_id_reduction_hellaswag_pp": 4.0,
762	      "mmlu_item_id_ci": [
763	        0.41,
764	        0.55
765	      ],
766	      "mmlu_item_id_ci_width": 0.14,
767	      "gsm8k_item_id_ci": [
768	        0.29,
769	        0.43
770	      ],
771	      "gsm8k_item_id_ci_width": 0.14,
772	      "arc_item_id_ci": [
773	        0.39,
774	        0.53
775	      ],
776	      "arc_item_id_ci_width": 0.14,
777	      "hellaswag_item_id_ci": [
778	        0.24,
779	        0.38
780	      ],
781	      "hellaswag_item_id_ci_width": 0.14,
782	      "gradient_high_endpoint_ci": [
783	        0.41,
784	        0.55
785	      ],
786	      "gradient_low_endpoint_ci": [
787	        0.24,
788	        0.38
789	      ],
790	      "gradient_endpoint_overlap": true,
791	      "gradient_overlap_range": [
792	        0.38,
793	        0.41
794	      ],
795	      "gradient_direction_p_value": 0.003,
796	      "gsm8k_infra_x_method_ci": [
797	        0.012,
798	        0.048
799	      ],
800	      "mmlu_infra_x_method_ci": [
801	        0.0,
802	        0.012
803	      ],
804	      "mmlu_model_x_item_ci": [
805	        0.16,
806	        0.27
807	      ],
808	      "dstudy_items_g80_mmlu": 220,
809	      "dstudy_items_g90_mmlu": 420,
810	      "dstudy_items_g95_mmlu": 680,
811	      "dstudy_items_g80_gsm8k": 150,
812	      "dstudy_items_g90_gsm8k": 280,
813	      "dstudy_items_g95_gsm8k": 450,
814	      "dstudy_items_g80_arc": 200,
815	      "dstudy_items_g90_arc": 380,
816	      "dstudy_items_g95_arc": 620,
817	      "dstudy_items_g80_hellaswag": 130,
818	      "dstudy_items_g90_hellaswag": 240,
819	      "dstudy_items_g95_hellaswag": 400,
820	      "dstudy_optimal_prompts_mmlu": 3,
821	      "dstudy_optimal_seeds_mmlu": 4,
822	      "dstudy_optimal_prompts_gsm8k": 4,
823	      "dstudy_optimal_seeds_gsm8k": 6,
824	      "dstudy_items_g90_ci_mmlu": [
825	        350,
826	        510
827	      ],
828	      "dstudy_items_g90_ci_gsm8k": [
829	        220,
830	        360
831	      ],
832	      "dstudy_ratio_mmlu_vs_hellaswag": 1.75,
833	      "dstudy_ratio_mmlu_vs_gsm8k": 1.5,
834	      "reml_henderson_max_diff_pp": 2.1,
835	      "reml_henderson_rank_preserved": true,
836	      "mmlu_item_id_logprob": 0.55,
837	      "mmlu_g_logprob": 0.32,
838	      "gsm8k_item_id_logprob": 0.42,
839	      "model_rank_flip_pct_across_conditions": 0.12,
840	      "rank_flip_driver": "temperature=1.0",
841	      "precision_causes_rank_flip": false,
842	      "three_way_interactions_total_mmlu": 0.03,
843	      "three_way_interactions_total_gsm8k": 0.05
844	    },
845	    "tables": [
846	      {
847	        "name": "Table 12: Model-as-Facet Reanalysis — All Benchmarks (Binary)",
848	        "columns": [
849	          "Source",
850	          "MMLU",
851	          "GSM8K",
852	          "ARC",
853	          "HellaSwag"
854	        ],
855	        "rows": [
856	          [
857	            "item_id",
858	            "48.0%",
859	            "36.0%",
860	            "46.0%",
861	            "31.0%"
862	          ],
863	          [
864	            "model×item",
865	            "21.0%",
866	            "18.0%",
867	            "16.0%",
868	            "19.0%"
869	          ],
870	          [
871	            "model (main)",
872	            "5.0%",
873	            "4.0%",
874	            "4.0%",
875	            "5.0%"
876	          ],
877	          [
878	            "residual",
879	            "8.0%",
880	            "10.0%",
881	            "8.0%",
882	            "10.0%"
883	          ],
884	          [
885	            "temp:item",
886	            "4.8%",
887	            "9.0%",
888	            "5.0%",
889	            "8.5%"
890	          ],
891	          [
892	            "seed:item",
893	            "2.0%",
894	            "5.5%",
895	            "3.0%",
896	            "7.0%"
897	          ],
898	          [
899	            "prompt:item",
900	            "5.3%",
901	            "5.5%",
902	            "7.5%",
903	            "6.5%"
904	          ],
905	          [
906	            "prec:item",
907	            "2.8%",
908	            "1.2%",
909	            "2.0%",
910	            "1.2%"
911	          ],
912	          [
913	            "precision (main)",
914	            "2.5%",
915	            "0.8%",
916	            "0.8%",
917	            "0.3%"
918	          ],
919	          [
920	            "temperature (main)",
921	            "1.2%",
922	            "3.5%",
923	            "2.2%",
924	            "4.0%"
925	          ],
926	          [
927	            "infra×method",
928	            "0.4%",
929	            "3.0%",
930	            "0.5%",
931	            "0.3%"
932	          ],
933	          [
934	            "other",
935	            "0.0%",
936	            "3.5%",
937	            "5.0%",
938	            "7.2%"
939	          ]
940	        ],
941	        "note": "Rows may not sum to 100% due to rounding and higher-order terms in 'other.'"
942	      },
943	      {
944	        "name": "Table 13: Bootstrap 95% CIs on Key Variance Components",
945	        "columns": [
946	          "Component",
947	          "MMLU",
948	          "GSM8K",
949	          "ARC",
950	          "HellaSwag"
951	        ],
952	        "rows": [
953	          [
954	            "item_id",
955	            "[0.41, 0.55]",
956	            "[0.29, 0.43]",
957	            "[0.39, 0.53]",
958	            "[0.24, 0.38]"
959	          ],
960	          [
961	            "model×item",
962	            "[0.16, 0.27]",
963	            "[0.13, 0.24]",
964	            "[0.11, 0.22]",
965	            "[0.14, 0.25]"
966	          ],
967	          [
968	            "infra×method",
969	            "[0.00, 0.012]",
970	            "[0.012, 0.048]",
971	            "[0.00, 0.014]",
972	            "[0.00, 0.010]"
973	          ]
974	        ],
975	        "note": "1000 bootstrap resamples (items × conditions). GSM8K infra×method CI excludes 0."
976	      },
977	      {
978	        "name": "Table 14: D-Study — Items Needed for Target G (BF16, optimal prompt/seed)",
979	        "columns": [
980	          "Benchmark",
981	          "G≥0.80",
982	          "G≥0.90",
983	          "G≥0.90 CI",
984	          "G≥0.95",
985	          "Prompts",
986	          "Seeds"
987	        ],
988	        "rows": [
989	          [
990	            "MMLU",
991	            "220",
992	            "420",
993	            "[350, 510]",
994	            "680",
995	            "3",
996	            "4"
997	          ],
998	          [
999	            "ARC",
1000	            "200",
1001	            "380",
1002	            "[310, 470]",
1003	            "620",
1004	            "3",
1005	            "4"
1006	          ],
1007	          [
1008	            "GSM8K",
1009	            "150",
1010	            "280",
1011	            "[220, 360]",
1012	            "450",
1013	            "4",
1014	            "6"
1015	          ],
1016	          [
1017	            "HellaSwag",
1018	            "130",
1019	            "240",
1020	            "[190, 310]",
1021	            "400",
1022	            "4",
1023	            "6"
1024	          ]
1025	        ]
1026	      },
1027	      {
1028	        "name": "Table 15: Scoring Metric Comparison (MMLU, Model-as-Facet)",
1029	        "columns": [
1030	          "Source",
1031	          "Binary",
1032	          "Text-match",
1033	          "Logprob"
1034	        ],
1035	        "rows": [
1036	          [
1037	            "item_id",
1038	            "48.0%",
1039	            "3.0%",
1040	            "55.0%"
1041	          ],
1042	          [
1043	            "model×item",
1044	            "21.0%",
1045	            "1.5%",
1046	            "18.0%"
1047	          ],
1048	          [
1049	            "prompt:item",
1050	            "5.3%",
1051	            "33.0%",
1052	            "4.0%"
1053	          ],
1054	          [
1055	            "residual",
1056	            "8.0%",
1057	            "36.0%",
1058	            "6.0%"
1059	          ],
1060	          [
1061	            "G coefficient",
1062	            "0.37",
1063	            "0.97",
1064	            "0.32"
1065	          ]
1066	        ]
1067	      },
1068	      {
1069	        "name": "Table 16: REML vs Henderson Method I (MMLU, Binary)",
1070	        "columns": [
1071	          "Source",
1072	          "Henderson %",
1073	          "REML %",
1074	          "Diff (pp)"
1075	        ],
1076	        "rows": [
1077	          [
1078	            "item_id",
1079	            "48.0%",
1080	            "49.2%",
1081	            "+1.2"
1082	          ],
1083	          [
1084	            "model×item",
1085	            "21.0%",
1086	            "22.4%",
1087	            "+1.4"
1088	          ],
1089	          [
1090	            "residual",
1091	            "8.0%",
1092	            "6.1%",
1093	            "-1.9"
1094	          ],
1095	          [
1096	            "other sources",
1097	            "23.0%",
1098	            "22.3%",
1099	            "—"
1100	          ]
1101	        ]
1102	      }
1103	    ],
1104	    "figures": [],
1105	    "analysis": "Five key takeaways for the paper. (1) Model-as-facet reduces item_id by ~4pp on ALL benchmarks — prior single-model studies systematically overestimated pure item dominance. Frame as: \"even within the 7-9B parameter range, model-specific knowledge gaps account for 16-21% of variance, meaning item difficulty estimates from single-model studies are inflated.\" (2) Gradient direction is significant (p=0.003) but magnitude CIs overlap at endpoints — use \"10-30pp spread\" in claims. (3) GSM8K infra×method CI [1.2%, 4.8%] excludes zero — this is a statistically robust departure from separability, requiring benchmark qualification on Claim 2. (4) D-study budgets differentiate benchmarks but the ratio (1.5-1.75×, not 3×) means the practical implication is real but less dramatic than hoped. (5) Logprob scoring amplifies item_id to 55% — a third metric perspective that strengthens the metric-conditional narrative.\n\n\nModel-as-facet is the most consequential reanalysis. On MMLU, 21% of total variance is model×item — this is not \"model difficulty\" but model-SPECIFIC item difficulty: items that are hard for Llama but easy for Qwen due to model-specific knowledge gaps and training data overlap. Absorbing this from item_id (52%→48%) and residual (14%→8%) properly attributes variance that prior single-model studies would have assigned to \"item difficulty.\" The 4pp reduction is consistent across all benchmarks, suggesting the model-facet correction is systematic rather than benchmark-specific. Bootstrap CI width of 0.14 on item_id reflects both item-resampling instability (exp-001b CV=19%) and condition-resampling instability. The gradient endpoint CIs overlap narrowly: MMLU lower CI (0.41) exceeds HellaSwag upper CI (0.38) by only 3pp, so the gradient direction is statistically significant (p=0.003 by permutation test) but the magnitude is imprecise — the paper should say \"10-30pp spread\" not \"17pp.\" D-study projections differentiate benchmarks: MMLU needs 420 items for G≥0.90 vs HellaSwag 240, a 1.75× ratio. This is directionally useful but less dramatic than a clean gradient would predict — the practical message is \"50-75% more items for knowledge vs reasoning benchmarks,\" not \"3× more items.\" D-study CIs on MMLU G≥0.90 ([350, 510]) show that even the recommended item count is imprecise. REML and Henderson agree to within 2.1pp — methodological choice doesn't affect qualitative conclusions. Logprob scoring increases item_id to 55% on MMLU because continuous logprobs capture fine-grained difficulty more sensitively than binary 0/1. Model rank flips occur in 12% of condition pairs, driven entirely by temperature=1.0 (high-temperature conditions produce enough noise to flip rankings of close models); precision never causes rank flips. Three-way interactions total 3-5% — most variance is captured by main effects and 2-way terms.\n"
1106	  },
1107	  {
1108	    "name": "14B model scale extension",
1109	    "description": "Qwen3-14B + DeepSeek-R1-Distill-14B at BF16/FP16 × 6 prompts × 6 seeds × 2 temperatures × 4 orderings × 200 MMLU items on datacenter GPUs (≥48GB VRAM).\n",
1110	    "results": {
1111	      "qwen3_14b_accuracy_bf16": 0.745,
1112	      "deepseek_r1_14b_accuracy_bf16": 0.728,
1113	      "item_id_14b_model_facet": 0.44,
1114	      "model_x_item_14b": 0.25,
1115	      "model_main_14b": 0.07,
1116	      "residual_14b": 0.06,
1117	      "temp_x_item_14b": 0.06,
1118	      "prompt_x_item_14b": 0.045,
1119	      "precision_main_14b": 0.003,
1120	      "g_correct_14b_binary": 0.4,
1121	      "deepseek_r1_temp_x_item": 0.085,
1122	      "qwen3_14b_temp_x_item": 0.042,
1123	      "cross_gpu_gap_14b_bf16_pp": 0.1,
1124	      "item_id_8b_vs_14b_diff_pp": 4.0,
1125	      "model_x_item_8b_vs_14b_diff_pp": 4.0,
1126	      "variance_hierarchy_qualitatively_preserved": true
1127	    },
1128	    "tables": [
1129	      {
1130	        "name": "Table 17: 8B vs 14B Variance Decomposition (MMLU, Model-as-Facet)",
1131	        "columns": [
1132	          "Source",
1133	          "8B (4 models)",
1134	          "14B (2 models)",
1135	          "Δ"
1136	        ],
1137	        "rows": [
1138	          [
1139	            "item_id",
1140	            "48.0%",
1141	            "44.0%",
1142	            "-4.0pp"
1143	          ],
1144	          [
1145	            "model×item",
1146	            "21.0%",
1147	            "25.0%",
1148	            "+4.0pp"
1149	          ],
1150	          [
1151	            "model (main)",
1152	            "5.0%",
1153	            "7.0%",
1154	            "+2.0pp"
1155	          ],
1156	          [
1157	            "residual",
1158	            "8.0%",
1159	            "6.0%",
1160	            "-2.0pp"
1161	          ],
1162	          [
1163	            "temp:item",
1164	            "4.8%",
1165	            "6.0%",
1166	            "+1.2pp"
1167	          ],
1168	          [
1169	            "prompt:item",
1170	            "5.3%",
1171	            "4.5%",
1172	            "-0.8pp"
1173	          ],
1174	          [
1175	            "precision (main)",
1176	            "2.5%",
1177	            "0.3%",
1178	            "-2.2pp"
1179	          ],
1180	          [
1181	            "other",
1182	            "5.4%",
1183	            "7.2%",
1184	            "—"
1185	          ]
1186	        ]
1187	      },
1188	      {
1189	        "name": "Table 18: Per-Architecture Temperature Sensitivity (14B)",
1190	        "columns": [
1191	          "Model",
1192	          "Type",
1193	          "temp:item",
1194	          "temp=0.0 Acc",
1195	          "temp=1.0 Acc",
1196	          "Spread"
1197	        ],
1198	        "rows": [
1199	          [
1200	            "Qwen3-14B",
1201	            "Dense",
1202	            "4.2%",
1203	            "0.752",
1204	            "0.738",
1205	            "1.4pp"
1206	          ],
1207	          [
1208	            "DeepSeek-R1-14B",
1209	            "Reasoning-distilled",
1210	            "8.5%",
1211	            "0.740",
1212	            "0.715",
1213	            "2.5pp"
1214	          ]
1215	        ]
1216	      }
1217	    ],
1218	    "figures": [],
1219	    "analysis": "Scale extension confirms qualitative stability: item_id > model×item > residual hierarchy holds at 14B. The 4pp item_id reduction per scale doubling (8B→14B) suggests that at current model sizes, item difficulty remains the dominant variance source — much larger models (70B+) would be needed to substantively alter the hierarchy. The dense-vs-reasoning architecture finding is a useful Discussion point: model×item increases not from more models but from more architecturally diverse models. For the paper: \"variance structure is qualitatively stable across 7-14B but item dominance magnitude is scale- and architecture-dependent.\" Frame as scope validation, not a primary finding. The precision reduction from 2.5% to 0.3% at 14B (both at BF16/FP16 only, no FP32) is because the FP32 degradation source is absent from this experiment.\n\n\n14B models show 44% item_id (vs 48% at 8B) because higher capacity reduces floor effects — items that were impossible for 8B models become solvable at 14B, compressing between-item variance. The 4pp reduction is modest, suggesting item difficulty saturation is far from reached even at 14B. Model×item interaction rises to 25% (from 21%) because the dense-vs-reasoning-distilled architecture difference creates larger model-specific item profiles: DeepSeek-R1-Distill-14B excels on multi-step reasoning items (distilled from R1's reasoning traces) while Qwen3-14B excels on factual knowledge items (larger pre-training corpus). This architecture-driven specialization is larger than the Llama-vs-Qwen difference at 8B. DeepSeek shows elevated temperature×item (8.5% vs Qwen's 4.2%) because reasoning-distilled models produce chain-of-thought that branches more at sampling time — consistent with exp-002's finding that reasoning tasks show higher temperature sensitivity. Model main effect at 7% (vs 5% at 8B) reflects the larger accuracy spread between dense and reasoning-distilled architectures. Precision effect remains negligible (0.3pp) — precision sensitivity does not increase with scale in this range. G-coefficient of 0.40 is slightly higher than 8B (0.37) because reduced item variance improves relative reliability.\n"
1220	  },
1221	  {
1222	    "name": "Fine-tuning G-study (RoBERTa)",
1223	    "description": "RoBERTa-large fine-tuning on SST-2/MNLI/RTE/COPA. 6 seeds × 3 LRs × 4 data shuffles × 3 GPUs × 2 precisions = 432 runs/task × 4 tasks = 1,728 total runs.\n",
1224	    "results": {
1225	      "sst2_accuracy_mean": 0.942,
1226	      "sst2_accuracy_sd": 0.005,
1227	      "sst2_lr_variance": 0.35,
1228	      "sst2_seed_variance": 0.25,
1229	      "sst2_data_shuffle_variance": 0.12,
1230	      "sst2_seed_x_lr_variance": 0.1,
1231	      "sst2_gpu_variance": 0.003,
1232	      "sst2_precision_variance": 0.008,
1233	      "sst2_residual": 0.159,
1234	      "mnli_accuracy_mean": 0.875,
1235	      "mnli_accuracy_sd": 0.008,
1236	      "mnli_lr_variance": 0.3,
1237	      "mnli_seed_variance": 0.22,
1238	      "mnli_data_shuffle_variance": 0.15,
1239	      "mnli_seed_x_lr_variance": 0.12,
1240	      "mnli_gpu_variance": 0.004,
1241	      "mnli_precision_variance": 0.009,
1242	      "mnli_residual": 0.177,
1243	      "rte_accuracy_mean": 0.716,
1244	      "rte_accuracy_sd": 0.032,
1245	      "rte_lr_variance": 0.2,
1246	      "rte_seed_variance": 0.16,
1247	      "rte_data_shuffle_variance": 0.28,
1248	      "rte_seed_x_lr_variance": 0.16,
1249	      "rte_gpu_variance": 0.005,
1250	      "rte_precision_variance": 0.01,
1251	      "rte_residual": 0.175,
1252	      "copa_accuracy_mean": 0.672,
1253	      "copa_accuracy_sd": 0.038,
1254	      "copa_lr_variance": 0.18,
1255	      "copa_seed_variance": 0.2,
1256	      "copa_data_shuffle_variance": 0.3,
1257	      "copa_seed_x_lr_variance": 0.14,
1258	      "copa_gpu_variance": 0.004,
1259	      "copa_precision_variance": 0.012,
1260	      "copa_residual": 0.134,
1261	      "dominant_source_large_data": "learning_rate",
1262	      "dominant_source_small_data": "data_shuffle",
1263	      "gpu_all_tasks_max": 0.005,
1264	      "precision_all_tasks_max": 0.012,
1265	      "hierarchy_differs_from_inference": true,
1266	      "rte_bimodal_seed_lr": true
1267	    },
1268	    "tables": [
1269	      {
1270	        "name": "Table 19: Fine-Tuning Variance Decomposition Across Tasks",
1271	        "columns": [
1272	          "Source",
1273	          "SST-2",
1274	          "MNLI",
1275	          "RTE",
1276	          "COPA"
1277	        ],
1278	        "rows": [
1279	          [
1280	            "learning_rate",
1281	            "35.0%",
1282	            "30.0%",
1283	            "20.0%",
1284	            "18.0%"
1285	          ],
1286	          [
1287	            "seed",
1288	            "25.0%",
1289	            "22.0%",
1290	            "16.0%",
1291	            "20.0%"
1292	          ],
1293	          [
1294	            "data_shuffle",
1295	            "12.0%",
1296	            "15.0%",
1297	            "28.0%",
1298	            "30.0%"
1299	          ],
1300	          [
1301	            "seed×lr",
1302	            "10.0%",
1303	            "12.0%",
1304	            "16.0%",
1305	            "14.0%"
1306	          ],
1307	          [
1308	            "gpu",
1309	            "0.3%",
1310	            "0.4%",
1311	            "0.5%",
1312	            "0.4%"
1313	          ],
1314	          [
1315	            "precision",
1316	            "0.8%",
1317	            "0.9%",
1318	            "1.0%",
1319	            "1.2%"
1320	          ],
1321	          [
1322	            "residual",
1323	            "16.9%",
1324	            "19.7%",
1325	            "18.5%",
1326	            "16.4%"
1327	          ]
1328	        ]
1329	      },
1330	      {
1331	        "name": "Table 20: Inference vs Fine-Tuning Variance Hierarchy",
1332	        "columns": [
1333	          "Rank",
1334	          "Inference (MMLU)",
1335	          "FT — Large (SST-2)",
1336	          "FT — Small (RTE)"
1337	        ],
1338	        "rows": [
1339	          [
1340	            "#1",
1341	            "item_id (48%)",
1342	            "learning_rate (35%)",
1343	            "data_shuffle (28%)"
1344	          ],
1345	          [
1346	            "#2",
1347	            "model×item (21%)",
1348	            "seed (25%)",
1349	            "learning_rate (20%)"
1350	          ],
1351	          [
1352	            "#3",
1353	            "residual (8%)",
1354	            "residual (17%)",
1355	            "seed×lr (16%)"
1356	          ],
1357	          [
1358	            "#4",
1359	            "prompt:item (5%)",
1360	            "data_shuffle (12%)",
1361	            "seed (16%)"
1362	          ],
1363	          [
1364	            "Infra",
1365	            "precision 2.5%",
1366	            "gpu+prec 1.1%",
1367	            "gpu+prec 1.5%"
1368	          ]
1369	        ]
1370	      }
1371	    ],
1372	    "figures": [],
1373	    "analysis": "Fine-tuning results support the paper's broader thesis at a meta-level: variance structure is task-conditional, and this extends beyond benchmarks to evaluation MODES. The LR-dominated (large data) vs shuffle-dominated (small data) pattern in fine-tuning parallels the knowledge-item-dominated vs reasoning-interaction-dominated pattern in inference — in both cases, the dominant source shifts as the task's \"difficulty structure\" changes. Infrastructure effects remain negligible in both settings, providing cross-mode evidence for separability (with the caveat that fine-tuning doesn't test the temperature/seed × precision interactions that drive GSM8K's infra×method departure). For the paper: position as Discussion material showing G-theory generality. Explicit caveat: encoder-only fine-tuning (RoBERTa) may not generalize to decoder fine-tuning where generation-related variance sources (temperature, seed) would re-enter.\n\n\nFine-tuning variance structure is qualitatively different from inference: hyperparameters (LR, seed, data shuffle) dominate instead of items. On large datasets (SST-2, MNLI), learning rate dominates (30-35%) because the optimization landscape is well-defined and LR determines the convergence basin — too high overshoots, too low underfits, and the sensitivity is amplified by RoBERTa's sharp loss surface near the optimum (Dodge et al., 2020). On small datasets (RTE, COPA), data shuffle dominates (28-30%) because mini-batch composition has outsized influence with fewer training examples — a single misplaced hard example in early batches can steer the model into a different loss basin. Seed is substantial everywhere (16-25%) because weight initialization and dropout mask jointly determine the optimization trajectory. The seed×LR interaction (10-16%) is the fine-tuning analog of item×temperature in inference: certain seed-LR combinations land in qualitatively different loss basins, producing bimodal accuracy distributions on RTE (two clusters separated by ~4pp accuracy, one basin near 72% and one near 68%). GPU and precision effects remain negligible (<1.2%) across all tasks — the variance hierarchy for infrastructure factors is consistent between fine-tuning and inference, even though the methodology-factor hierarchy differs completely. This validates the G-theory framework's generality while showing that reproducibility budgets cannot be transferred between evaluation modes.\n"
1374	  },
1375	  {
1376	    "name": "LayerCast precision mitigation",
1377	    "description": "LayerCast (FP16 storage + FP32 compute) as additional precision condition on MMLU. Same 4 models × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 items.\n",
1378	    "results": {
1379	      "layercast_accuracy_mean": 0.682,
1380	      "layercast_vs_bf16_gap_pp": 0.2,
1381	      "layercast_vs_fp16_gap_pp": 0.1,
1382	      "layercast_vs_fp32_gap_pp": 2.7,
1383	      "layercast_item_id_binary": 0.515,
1384	      "layercast_prec_x_item_reduction_vs_fp16_pct": 40,
1385	      "layercast_g_correct_binary": 0.37,
1386	      "layercast_inference_overhead_pct": 18,
1387	      "layercast_prec_x_temp_binary": 0.001,
1388	      "layercast_prec_x_temp_textmatch": 0.008
1389	    },
1390	    "tables": [
1391	      {
1392	        "name": "Table 21: LayerCast Comparison Across Precision Modes",
1393	        "columns": [
1394	          "Metric",
1395	          "FP32",
1396	          "BF16",
1397	          "FP16",
1398	          "LayerCast"
1399	        ],
1400	        "rows": [
1401	          [
1402	            "Accuracy",
1403	            "0.655",
1404	            "0.684",
1405	            "0.681",
1406	            "0.682"
1407	          ],
1408	          [
1409	            "item_id %",
1410	            "50.5%",
1411	            "52.0%",
1412	            "51.8%",
1413	            "51.5%"
1414	          ],
1415	          [
1416	            "prec:item %",
1417	            "5.8%",
1418	            "4.5%",
1419	            "5.0%",
1420	            "3.0%"
1421	          ],
1422	          [
1423	            "prec×temp (binary)",
1424	            "0.3%",
1425	            "0.1%",
1426	            "0.2%",
1427	            "0.1%"
1428	          ],
1429	          [
1430	            "prec×temp (text)",
1431	            "2.5%",
1432	            "1.8%",
1433	            "2.2%",
1434	            "0.8%"
1435	          ],
1436	          [
1437	            "G (binary)",
1438	            "0.36",
1439	            "0.37",
1440	            "0.37",
1441	            "0.37"
1442	          ],
1443	          [
1444	            "Inference cost (rel.)",
1445	            "1.35×",
1446	            "1.00×",
1447	            "1.00×",
1448	            "1.18×"
1449	          ]
1450	        ]
1451	      }
1452	    ],
1453	    "figures": [],
1454	    "analysis": "LayerCast is a footnote finding. Precision effects are already small post-confound analysis (precision main 2.5-3% of total, infra×method <0.5% on knowledge benchmarks). Mitigating them further with LayerCast provides diminishing returns at 18% inference cost. Include as 1-2 paragraphs in Discussion or as appendix material. Practical recommendation: use BF16 — it has no overhead and minimal precision artifacts. LayerCast is only worth mentioning to preempt reviewer questions about mitigation strategies.\n\n\nLayerCast reduces precision:item interaction by ~40% vs FP16 because the FP32 compute path eliminates mid-layer accumulation errors that flip items near decision boundaries. However, the practical benefit is marginal: FP16 precision:item was already only 5% of total variance, so a 40% reduction brings it to ~3% — still dwarfed by item_id at 51.5%. Accuracy (0.682) falls between BF16 (0.684) and FP16 (0.681), essentially equivalent to both. The precision×temperature interaction drops to 0.1% binary (from FP16's ~0.2%) because FP32 compute stabilizes the logit computation at each sampling step. The 18% inference overhead comes from FP16→FP32 upcasting at each transformer layer. G-coefficient is unchanged (0.37) because the dominant item_id component is unaffected by precision mitigation. Given that BF16 already shows negligible precision effects and has no inference overhead, LayerCast is only relevant for the specific case where FP16 memory savings are required AND cross-hardware reproducibility matters.\n"
1455	  },
1456	  {
1457	    "name": "MATH benchmark extension",
1458	    "description": "MATH (200 items) with 4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures × 4 orderings. Tests chain-of-thought reasoning variance.\n",
1459	    "results": {
1460	      "math_accuracy_mean": 0.38,
1461	      "math_accuracy_sd_across_conditions": 0.045,
1462	      "math_item_id_basic": 0.32,
1463	      "math_residual_basic": 0.17,
1464	      "math_temp_x_item_basic": 0.14,
1465	      "math_seed_x_item_basic": 0.11,
1466	      "math_prompt_x_item_basic": 0.08,
1467	      "math_temperature_main_basic": 0.06,
1468	      "math_precision_main_basic": 0.005,
1469	      "math_infra_x_method_binary": 0.025,
1470	      "math_other_basic": 0.09,
1471	      "math_item_id_model_facet": 0.28,
1472	      "math_model_x_item": 0.22,
1473	      "math_model_main": 0.06,
1474	      "math_residual_model_facet": 0.07,
1475	      "math_g_correct_binary": 0.52,
1476	      "five_benchmark_item_id_range": [
1477	        0.28,
1478	        0.48
1479	      ],
1480	      "five_benchmark_spread_pp": 20,
1481	      "five_benchmark_pattern": "{MMLU 48%, ARC 46%} > {GSM8K 36%, HellaSwag 31%} ≥ {MATH 28%}",
1482	      "three_tier_structure": true,
1483	      "math_infra_x_method_textmatch": 0.042
1484	    },
1485	    "tables": [
1486	      {
1487	        "name": "Table 22: MATH Variance Decomposition (Binary, Model-as-Facet)",
1488	        "columns": [
1489	          "Source",
1490	          "MATH",
1491	          "GSM8K (ref)",
1492	          "MMLU (ref)"
1493	        ],
1494	        "rows": [
1495	          [
1496	            "item_id",
1497	            "28.0%",
1498	            "36.0%",
1499	            "48.0%"
1500	          ],
1501	          [
1502	            "model×item",
1503	            "22.0%",
1504	            "18.0%",
1505	            "21.0%"
1506	          ],
1507	          [
1508	            "temp:item",
1509	            "14.0%",
1510	            "9.0%",
1511	            "4.8%"
1512	          ],
1513	          [
1514	            "seed:item",
1515	            "11.0%",
1516	            "5.5%",
1517	            "2.0%"
1518	          ],
1519	          [
1520	            "prompt:item",
1521	            "6.5%",
1522	            "5.5%",
1523	            "5.3%"
1524	          ],
1525	          [
1526	            "model (main)",
1527	            "6.0%",
1528	            "4.0%",
1529	            "5.0%"
1530	          ],
1531	          [
1532	            "residual",
1533	            "7.0%",
1534	            "10.0%",
1535	            "8.0%"
1536	          ],
1537	          [
1538	            "temperature",
1539	            "4.5%",
1540	            "3.5%",
1541	            "1.2%"
1542	          ],
1543	          [
1544	            "infra×method",
1545	            "2.5%",
1546	            "3.0%",
1547	            "0.4%"
1548	          ],
1549	          [
1550	            "other",
1551	            "-1.5%",
1552	            "5.5%",
1553	            "4.3%"
1554	          ]
1555	        ],
1556	        "note": "Negative 'other' due to rounding and minor negative Henderson estimates on near-zero terms."
1557	      },
1558	      {
1559	        "name": "Table 23: Updated 5-Benchmark Summary (Model-as-Facet)",
1560	        "columns": [
1561	          "Benchmark",
1562	          "Type",
1563	          "item_id",
1564	          "G (binary)",
1565	          "infra×method",
1566	          "Tier"
1567	        ],
1568	        "rows": [
1569	          [
1570	            "MMLU",
1571	            "Knowledge",
1572	            "48.0%",
1573	            "0.37",
1574	            "0.4%",
1575	            "High"
1576	          ],
1577	          [
1578	            "ARC",
1579	            "Knowledge",
1580	            "46.0%",
1581	            "0.35",
1582	            "0.5%",
1583	            "High"
1584	          ],
1585	          [
1586	            "GSM8K",
1587	            "Arithmetic reasoning",
1588	            "36.0%",
1589	            "0.42",
1590	            "3.0%",
1591	            "Mid"
1592	          ],
1593	          [
1594	            "HellaSwag",
1595	            "Commonsense",
1596	            "31.0%",
1597	            "0.48",
1598	            "0.3%",
1599	            "Mid"
1600	          ],
1601	          [
1602	            "MATH",
1603	            "Proof reasoning",
1604	            "28.0%",
1605	            "0.52",
1606	            "2.5%",
1607	            "Low"
1608	          ]
1609	        ]
1610	      }
1611	    ],
1612	    "figures": [],
1613	    "analysis": "MATH is the median tier's upgrade path. With 5 benchmarks and 20pp spread, the narrative strengthens from \"2-cluster\" to \"task-complexity gradient with 3 tiers\": knowledge benchmarks (MMLU, ARC) → arithmetic/commonsense reasoning (GSM8K, HellaSwag) → proof reasoning (MATH). HellaSwag's position (31%, in \"mid\" tier despite being commonsense rather than math) adds nuance — the gradient tracks multi-step reasoning demand more than domain. MATH also reinforces the GSM8K infra×method finding: both math-heavy benchmarks show 2.5-3% infra×method binary, while knowledge and commonsense benchmarks show <0.5%. This transforms the separability exception from \"one benchmark\" to \"math-generation benchmarks\" — a more principled category that strengthens the paper. If AAAI timeline permits exp-008 (50 GPU hours, dependent on exp-002), include it and claim the 3-tier gradient. If not, the 4-benchmark 2-cluster story is publishable with softened framing, and MATH can be added for camera-ready or the ACL submission.\n\nMATH shows the lowest item dominance (28% model-as-facet) because multi-step mathematical proofs introduce maximal chain-of-thought variance. Unlike GSM8K's mostly arithmetic word problems, MATH items require proof strategies (induction, construction, algebraic manipulation) with multiple valid approaches — temperature and seed determine which strategy the model attempts, making temp:item (14%) and seed:item (11%) jointly exceed item_id. The 38% overall accuracy (8B models on MATH) creates strong floor effects: ~40% of items are never solved regardless of conditions (zero variance), ~20% are always solved (zero variance), and the remaining ~40% of \"mid-difficulty\" items carry nearly all the variance — and on these items, condition sensitivity is extreme. G-coefficient at 0.52 (highest of all benchmarks) is counterintuitive but correct: the items that 8B models CAN solve are consistently solved (low relative error), so the universe score is reliable despite high absolute variance. Model×item at 22% is the highest across benchmarks because dense vs reasoning-distilled architectures diverge most on proof items: DeepSeek-R1-Distill can solve certain proof items that no other 8B model touches, creating large model-specific item effects. Adding MATH extends the 2-cluster gradient to a potential 3-tier structure with 20pp total spread (48-28%), strengthening the cognitive-complexity narrative. Infra×method at 2.5% binary confirms the GSM8K pattern: math-heavy generation shows detectable precision×methodology interaction. Under text-match, MATH prec×temp reaches 4.2% (the highest single infra×method interaction) because proof-format outputs are extremely sensitive to token-level differences.\n"
1614	  }
1615	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "efabf9ac-c786-4d8d-baae-bf4a4ff7b9d8",
  "isSidechain": false,
  "promptId": "c5460e05-f609-42c9-9ad5-28993b47482a",
  "type": "user",
  "uuid": "2df83229-fdc6-43a5-a495-16e283858fd4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Full-scale MMLU precision study (confound-fixed)\",\n    \"description\": \"4 models × 3 precisions (FP32/BF16/FP16, all V0 enforce_eager) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items (stratified). 1,036,800 total observations.\\n\",\n    \"results\": {\n      \"total_observations\": 1036800,\n      \"total_conditions\": 5184,\n      \"accuracy_fp32\": 0.655,\n      \"accuracy_bf16\": 0.684,\n      \"accuracy_fp16\": 0.681,\n      \"accuracy_gap_fp32_bf16_pp\": 2.9,\n      \"accuracy_gap_bf16_fp16_pp\": 0.3,\n      \"accuracy_by_model\": {\n        \"qwen3_8b\": {\n          \"fp32\": 0.695,\n          \"bf16\": 0.71,\n          \"fp16\": 0.706\n        },\n        \"llama31_8b\": {\n          \"fp32\": 0.6,\n          \"bf16\": 0.672,\n          \"fp16\": 0.669\n        },\n        \"gemma2_9b\": {\n          \"fp32\": 0.638,\n          \"bf16\": 0.66,\n          \"fp16\": 0.658\n        },\n        \"mistral_7b\": {\n          \"fp32\": 0.688,\n          \"bf16\": 0.694,\n          \"fp16\": 0.691\n        }\n      },\n      \"item_id_variance_binary\": 0.52,\n      \"residual_variance_binary\": 0.14,\n      \"precision_x_item_binary\": 0.05,\n      \"prompt_x_item_binary\": 0.058,\n      \"temperature_x_item_binary\": 0.055,\n      \"seed_x_item_binary\": 0.028,\n      \"precision_main_binary\": 0.03,\n      \"temperature_main_binary\": 0.015,\n      \"prompt_main_binary\": 0.008,\n      \"ordering_main_binary\": 0.002,\n      \"precision_x_temperature_binary\": 0.002,\n      \"precision_x_prompt_binary\": 0.001,\n      \"precision_x_seed_binary\": 0.001,\n      \"other_binary\": 0.09,\n      \"residual_textmatch\": 0.36,\n      \"prompt_x_item_textmatch\": 0.33,\n      \"temperature_main_textmatch\": 0.14,\n      \"precision_x_item_textmatch\": 0.04,\n      \"precision_x_temperature_textmatch\": 0.022,\n      \"temperature_x_item_textmatch\": 0.03,\n      \"item_id_textmatch\": 0.03,\n      \"precision_main_textmatch\": 0.025,\n      \"other_textmatch\": 0.023,\n      \"g_correct_binary\": 0.37,\n      \"g_correct_textmatch\": 0.97,\n      \"item_id_rank_corr_across_models\": 0.82,\n      \"fp32_gap_model_range_pp\": [\n        1.5,\n        7.2\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: MMLU Variance Decomposition — Binary Correct (Basic, Model Pooled)\",\n        \"columns\": [\n          \"Source\",\n          \"% Total Variance\"\n        ],\n        \"rows\": [\n          [\n            \"item_id\",\n            \"52.0%\"\n          ],\n          [\n            \"residual (includes model effects)\",\n            \"14.0%\"\n          ],\n          [\n            \"prompt:item\",\n            \"5.8%\"\n          ],\n          [\n            \"temperature:item\",\n            \"5.5%\"\n          ],\n          [\n            \"precision:item\",\n            \"5.0%\"\n          ],\n          [\n            \"precision (main)\",\n            \"3.0%\"\n          ],\n          [\n            \"seed:item\",\n            \"2.8%\"\n          ],\n          [\n            \"temperature (main)\",\n            \"1.5%\"\n          ],\n          [\n            \"prompt (main)\",\n            \"0.8%\"\n          ],\n          [\n            \"infra×method (all)\",\n            \"0.4%\"\n          ],\n          [\n            \"ordering\",\n            \"0.2%\"\n          ],\n          [\n            \"other 2-way / 3-way\",\n            \"9.0%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: MMLU Variance Decomposition — Text Exact Match (Basic)\",\n        \"columns\": [\n          \"Source\",\n          \"% Total Variance\"\n        ],\n        \"rows\": [\n          [\n            \"residual\",\n            \"36.0%\"\n          ],\n          [\n            \"prompt:item\",\n            \"33.0%\"\n          ],\n          [\n            \"temperature (main)\",\n            \"14.0%\"\n          ],\n          [\n            \"precision:item\",\n            \"4.0%\"\n          ],\n          [\n            \"temperature:item\",\n            \"3.0%\"\n          ],\n          [\n            \"item_id\",\n            \"3.0%\"\n          ],\n          [\n            \"precision (main)\",\n            \"2.5%\"\n          ],\n          [\n            \"precision×temperature\",\n            \"2.2%\"\n          ],\n          [\n            \"other\",\n            \"2.3%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 3: Per-Model Accuracy by Precision (V0 enforce_eager)\",\n        \"columns\": [\n          \"Model\",\n          \"FP32\",\n          \"BF16\",\n          \"FP16\",\n          \"FP32-BF16 Gap\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B-Instruct\",\n            \"0.695\",\n            \"0.710\",\n            \"0.706\",\n            \"1.5pp\"\n          ],\n          [\n            \"Llama-3.1-8B-Instruct\",\n            \"0.600\",\n            \"0.672\",\n            \"0.669\",\n            \"7.2pp\"\n          ],\n          [\n            \"Gemma-2-9B-IT\",\n            \"0.638\",\n            \"0.660\",\n            \"0.658\",\n            \"2.2pp\"\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            \"0.688\",\n            \"0.694\",\n            \"0.691\",\n            \"0.6pp\"\n          ],\n          [\n            \"Average\",\n            \"0.655\",\n            \"0.684\",\n            \"0.681\",\n            \"2.9pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Key finding: FP32 degradation is REAL, not an engine confound. The bf16_eager_disentangle result is confirmed at scale — V0 enforce_eager changes nothing substantial. This reframes the contribution: we provide the first item-level G-theory decomposition of precision effects, showing that precision:item (5%) exceeds precision main (3%). The model-dependence of FP32 degradation (1.5-7.2pp) is novel and suggests training-time precision choices affect inference robustness. For the paper: position FP32 degradation as supporting Yuan et al. (2025) with novel item×model granularity, NOT as a primary finding. Separability on MMLU is confirmed: infra×method = 0.4% binary, 2.2% text-match (precision×temperature only). CIs deferred to exp-004.\\n\\n\\nV0 enforce_eager for all precisions eliminates the 0.22pp engine confound (bf16_eager_disentangle) but the FP32 accuracy gap PERSISTS at ~2.9pp average — confirming the disentangle conclusion that 97.4% of the gap was genuine precision effect. FP32 degradation is strongly model-dependent: Llama-3.1-8B shows 7.2pp gap (consistent with MVP's 8.5pp on this model) while Qwen3-8B shows only 1.5pp, likely because Qwen's training used mixed-precision strategies that are more robust to FP32 inference rounding. Precision main effect at 3% is real but dwarfed by item_id at 52%. Precision:item at 5% means certain items (those near decision boundaries) are disproportionately affected — this is the novel item-level breakdown that extends Yuan et al. (2025). Item_id at 52% is lower than MVP's 58.4% because 200 stratified items (vs 50) include more mid-difficulty items that reduce between-item variance, and pooling across 4 models absorbs some item-specific variance into residual. Residual at 14% is inflated because model effects are pooled — exp-004 will decompose this. G=0.37 replicates MVP's 0.357, confirming item dominance makes G≥0.90 unreachable without massive item expansion. Text-match scoring replicates the qualitative shift: prompt:item dominates (33%), precision×temperature at 2.2% (consistent with MVP's 1.3% but larger due to more conditions), driven by floating-point non-associativity in generation.\\n\"\n  },\n  {\n    \"name\": \"Item resampling stability test\",\n    \"description\": \"3 independent stratified samples of 200 MMLU items (seeds 0, 7, 99) × Llama-3.1-8B × 3 precisions × 3 prompts × 3 seeds × 2 orderings = 54 conditions/sample, 32,400 obs/sample.\\n\",\n    \"results\": {\n      \"item_id_sample_0\": 0.49,\n      \"item_id_sample_7\": 0.55,\n      \"item_id_sample_99\": 0.44,\n      \"item_id_mean\": 0.493,\n      \"item_id_sd\": 0.055,\n      \"item_id_cv\": 0.19,\n      \"g_coeff_sample_0\": 0.36,\n      \"g_coeff_sample_7\": 0.32,\n      \"g_coeff_sample_99\": 0.39,\n      \"accuracy_sample_0\": 0.668,\n      \"accuracy_sample_7\": 0.641,\n      \"accuracy_sample_99\": 0.679,\n      \"mean_item_difficulty_sample_0\": 0.5,\n      \"mean_item_difficulty_sample_7\": 0.42,\n      \"mean_item_difficulty_sample_99\": 0.54,\n      \"sd_item_difficulty_sample_0\": 0.28,\n      \"sd_item_difficulty_sample_7\": 0.32,\n      \"sd_item_difficulty_sample_99\": 0.25,\n      \"rank_order_top3_sources_preserved\": true,\n      \"residual_cv\": 0.11,\n      \"prompt_item_cv\": 0.09\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: Resampling Stability of Variance Components\",\n        \"columns\": [\n          \"Source\",\n          \"Sample 0\",\n          \"Sample 7\",\n          \"Sample 99\",\n          \"Mean\",\n          \"CV\"\n        ],\n        \"rows\": [\n          [\n            \"item_id\",\n            \"49.0%\",\n            \"55.0%\",\n            \"44.0%\",\n            \"49.3%\",\n            \"0.19\"\n          ],\n          [\n            \"residual\",\n            \"17.5%\",\n            \"15.0%\",\n            \"19.5%\",\n            \"17.3%\",\n            \"0.11\"\n          ],\n          [\n            \"prompt:item\",\n            \"6.5%\",\n            \"6.0%\",\n            \"7.0%\",\n            \"6.5%\",\n            \"0.09\"\n          ],\n          [\n            \"temp:item\",\n            \"5.8%\",\n            \"5.2%\",\n            \"6.5%\",\n            \"5.8%\",\n            \"0.10\"\n          ],\n          [\n            \"prec:item\",\n            \"5.0%\",\n            \"5.5%\",\n            \"4.2%\",\n            \"4.9%\",\n            \"0.12\"\n          ],\n          [\n            \"precision\",\n            \"3.0%\",\n            \"3.5%\",\n            \"2.8%\",\n            \"3.1%\",\n            \"0.10\"\n          ],\n          [\n            \"other\",\n            \"13.2%\",\n            \"9.8%\",\n            \"16.0%\",\n            \"13.0%\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 5: Per-Sample Summary Statistics\",\n        \"columns\": [\n          \"Metric\",\n          \"Sample 0\",\n          \"Sample 7\",\n          \"Sample 99\"\n        ],\n        \"rows\": [\n          [\n            \"N items\",\n            \"200\",\n            \"200\",\n            \"200\"\n          ],\n          [\n            \"Mean item difficulty\",\n            \"0.50\",\n            \"0.42\",\n            \"0.54\"\n          ],\n          [\n            \"SD item difficulty\",\n            \"0.28\",\n            \"0.32\",\n            \"0.25\"\n          ],\n          [\n            \"Overall accuracy\",\n            \"0.668\",\n            \"0.641\",\n            \"0.679\"\n          ],\n          [\n            \"G (binary)\",\n            \"0.36\",\n            \"0.32\",\n            \"0.39\"\n          ],\n          [\n            \"item_id %\",\n            \"49.0%\",\n            \"55.0%\",\n            \"44.0%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The 19% CV is the paper's best defense against \\\"you just got lucky with your items.\\\" It quantifies the item-sampling uncertainty that plagues every single-draw benchmark study. Rank ordering is robust (item_id always #1) but precise magnitude depends on which items you drew — explaining why Mesting (2026) and Brittlebench (2026) reached different headline numbers on different item sets. For the paper: always report item_id as a range (44-55%) not a point. D-study projections from exp-004 should include CIs that account for this resampling instability.\\n\\n\\nCV of 19% reflects meaningful item-sampling uncertainty. MMLU has 14,042 items across 57 subjects with heterogeneous difficulty; stratified sampling with 200 items (1.4%) leaves substantial sampling variance especially in the tails. Sample 7 draws more hard items (mean difficulty 0.42), inflating between-item variance to 55% because the difficulty spread is wider (SD 0.32). Sample 99 draws more mid-difficulty items (mean 0.54, SD 0.25), compressing item_id to 44% because items cluster around the center. Despite magnitude variation, the qualitative hierarchy is preserved: item_id ranks #1 in all 3 samples, residual #2, prompt:item #3. This stability-in-rank with instability-in-magnitude is the key finding: the headline claim \\\"item dominance ~50%\\\" needs error bars, reported as \\\"44-55% across independent 200-item stratified draws.\\\" The G-coefficient varies inversely (0.32-0.39) because higher item variance = lower generalizability of the benchmark score. This directly motivates D-study item-count recommendations with CIs, not point estimates — if your headline variance component shifts ±5pp with a different item draw, your optimal resource allocation shifts too.\\n\"\n  },\n  {\n    \"name\": \"Multi-benchmark replication (GSM8K, ARC, HellaSwag)\",\n    \"description\": \"4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures × 4 orderings × 200 items on GSM8K, ARC-Challenge, HellaSwag. Reduced crossing vs exp-001.\\n\",\n    \"results\": {\n      \"total_observations_per_benchmark\": 384000,\n      \"gsm8k_accuracy\": 0.575,\n      \"gsm8k_item_id_binary\": 0.4,\n      \"gsm8k_residual_binary\": 0.15,\n      \"gsm8k_temp_x_item_binary\": 0.1,\n      \"gsm8k_seed_x_item_binary\": 0.07,\n      \"gsm8k_prompt_x_item_binary\": 0.065,\n      \"gsm8k_temperature_binary\": 0.04,\n      \"gsm8k_prec_x_temp_binary\": 0.022,\n      \"gsm8k_prec_x_seed_binary\": 0.005,\n      \"gsm8k_prec_x_prompt_binary\": 0.003,\n      \"gsm8k_infra_x_method_total_binary\": 0.03,\n      \"gsm8k_precision_main_binary\": 0.01,\n      \"gsm8k_prec_x_item_binary\": 0.015,\n      \"gsm8k_other_binary\": 0.093,\n      \"gsm8k_g_correct_binary\": 0.42,\n      \"arc_accuracy\": 0.625,\n      \"arc_item_id_binary\": 0.5,\n      \"arc_residual_binary\": 0.12,\n      \"arc_prompt_x_item_binary\": 0.085,\n      \"arc_temp_x_item_binary\": 0.055,\n      \"arc_seed_x_item_binary\": 0.04,\n      \"arc_prec_x_item_binary\": 0.025,\n      \"arc_temperature_binary\": 0.025,\n      \"arc_precision_binary\": 0.01,\n      \"arc_infra_x_method_total_binary\": 0.005,\n      \"arc_other_binary\": 0.115,\n      \"arc_g_correct_binary\": 0.35,\n      \"hellaswag_accuracy\": 0.712,\n      \"hellaswag_item_id_binary\": 0.35,\n      \"hellaswag_residual_binary\": 0.18,\n      \"hellaswag_temp_x_item_binary\": 0.095,\n      \"hellaswag_seed_x_item_binary\": 0.085,\n      \"hellaswag_prompt_x_item_binary\": 0.075,\n      \"hellaswag_temperature_binary\": 0.045,\n      \"hellaswag_prec_x_item_binary\": 0.015,\n      \"hellaswag_precision_binary\": 0.005,\n      \"hellaswag_infra_x_method_total_binary\": 0.003,\n      \"hellaswag_other_binary\": 0.127,\n      \"hellaswag_g_correct_binary\": 0.48,\n      \"gradient_pattern\": \"2-cluster: {MMLU 52%, ARC 50%} vs {GSM8K 40%, HellaSwag 35%}\",\n      \"gradient_spread_pp\": 17,\n      \"within_cluster_ordering_reliable\": false,\n      \"gsm8k_prec_x_temp_textmatch\": 0.035,\n      \"arc_prec_x_temp_textmatch\": 0.022,\n      \"hellaswag_prec_x_temp_textmatch\": 0.016,\n      \"infra_x_method_textmatch_max\": 0.035\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: Cross-Benchmark Variance Decomposition — Binary (Basic, Model Pooled)\",\n        \"columns\": [\n          \"Source\",\n          \"MMLU\",\n          \"GSM8K\",\n          \"ARC\",\n          \"HellaSwag\"\n        ],\n        \"rows\": [\n          [\n            \"item_id\",\n            \"52.0%\",\n            \"40.0%\",\n            \"50.0%\",\n            \"35.0%\"\n          ],\n          [\n            \"residual\",\n            \"14.0%\",\n            \"15.0%\",\n            \"12.0%\",\n            \"18.0%\"\n          ],\n          [\n            \"temp:item\",\n            \"5.5%\",\n            \"10.0%\",\n            \"5.5%\",\n            \"9.5%\"\n          ],\n          [\n            \"seed:item\",\n            \"2.8%\",\n            \"7.0%\",\n            \"4.0%\",\n            \"8.5%\"\n          ],\n          [\n            \"prompt:item\",\n            \"5.8%\",\n            \"6.5%\",\n            \"8.5%\",\n            \"7.5%\"\n          ],\n          [\n            \"prec:item\",\n            \"5.0%\",\n            \"1.5%\",\n            \"2.5%\",\n            \"1.5%\"\n          ],\n          [\n            \"precision (main)\",\n            \"3.0%\",\n            \"1.0%\",\n            \"1.0%\",\n            \"0.5%\"\n          ],\n          [\n            \"temperature (main)\",\n            \"1.5%\",\n            \"4.0%\",\n            \"2.5%\",\n            \"4.5%\"\n          ],\n          [\n            \"infra×method (total)\",\n            \"0.4%\",\n            \"3.0%\",\n            \"0.5%\",\n            \"0.3%\"\n          ],\n          [\n            \"other\",\n            \"10.0%\",\n            \"12.0%\",\n            \"13.5%\",\n            \"14.7%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 7: Cross-Benchmark Summary (Basic)\",\n        \"columns\": [\n          \"Benchmark\",\n          \"Task Type\",\n          \"item_id %\",\n          \"G (binary)\",\n          \"infra×method\",\n          \"Cluster\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            \"Knowledge\",\n            \"52.0%\",\n            \"0.37\",\n            \"0.4%\",\n            \"High\"\n          ],\n          [\n            \"ARC-Challenge\",\n            \"Knowledge/Science\",\n            \"50.0%\",\n            \"0.35\",\n            \"0.5%\",\n            \"High\"\n          ],\n          [\n            \"GSM8K\",\n            \"Math reasoning\",\n            \"40.0%\",\n            \"0.42\",\n            \"3.0%\",\n            \"Low\"\n          ],\n          [\n            \"HellaSwag\",\n            \"Commonsense\",\n            \"35.0%\",\n            \"0.48\",\n            \"0.3%\",\n            \"Low\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 8: GSM8K Infra×Method Interaction Breakdown (Binary)\",\n        \"columns\": [\n          \"Interaction\",\n          \"% Total Variance\",\n          \"95% CI (bootstrap, exp-004)\"\n        ],\n        \"rows\": [\n          [\n            \"precision×temperature\",\n            \"2.2%\",\n            \"deferred\"\n          ],\n          [\n            \"precision×seed\",\n            \"0.5%\",\n            \"deferred\"\n          ],\n          [\n            \"precision×prompt\",\n            \"0.3%\",\n            \"deferred\"\n          ],\n          [\n            \"Total infra×method\",\n            \"3.0%\",\n            \"deferred\"\n          ]\n        ],\n        \"note\": \"Only GSM8K exceeds 1% threshold. MMLU 0.4%, ARC 0.5%, HellaSwag 0.3%.\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"This is the core finding. The 2-cluster pattern is clear and the direction is robust, but it is NOT the clean monotonic gradient originally hypothesized. ARC clusters with MMLU (not intermediate) — this is actually a stronger finding than a gradient: variance structure tracks cognitive demand, and ARC's \\\"science reasoning\\\" label is misleading. The GSM8K infra×method at 3% binary is the median tier's key complication for Claim 2: separability is benchmark-conditional, not universal. The paper must add \\\"on knowledge-retrieval benchmarks\\\" or \\\"when math reasoning is excluded\\\" to the separability claim. Under text-match, GSM8K reaches 3.5% (within target [1.5%, 4.5%]). Practical implication: practitioners evaluating math reasoning on GSM8K should fix both precision AND temperature to minimize infra×method confounding.\\n\\n\\nThe 2-cluster pattern emerges because variance structure tracks cognitive demand, not benchmark labels. Knowledge-retrieval benchmarks (MMLU, ARC) show high item dominance (50-52% basic) because item difficulty is the primary driver — items test factual knowledge that is either present or absent in the model, and this binary state dominates across conditions. ARC clusters with MMLU despite being labeled \\\"science reasoning\\\" because most ARC items are effectively factual recall (what happens when ice melts?) rather than multi-step inference. Reasoning benchmarks (GSM8K, HellaSwag) show lower item dominance (35-40%) because temperature and seed interact strongly with items: multi-step reasoning and commonsense inference have multiple valid processing paths, and sampling randomness determines which path is taken, shifting variance from item_id to interaction terms. GSM8K item dominance at 40% is above the hypothesized 20-30% because even math reasoning has trivially easy items (single-step arithmetic) and impossible items (complex multi-step for 8B models), creating a floor of item-driven variance. The critical median-tier finding: GSM8K shows infra×method = 3.0% under binary scoring (precision×temperature 2.2% + precision×seed 0.5% + precision×prompt 0.3%). This breaks universal separability. The mechanism: math generation produces longer chains-of-thought where BF16 vs FP16 accumulation differences compound; temperature controls how aggressively alternative reasoning paths are explored; the precision×temperature combination can push probability distributions past decision boundaries, flipping the final numerical answer. Binary scoring captures this because the extracted number differs. Other benchmarks show infra×method <0.5% binary — the effect is GSM8K-specific. Under text-match, GSM8K prec×temp reaches 3.5% because exact-string comparison of multi-step outputs amplifies floating-point divergence. The gradient spread of 17pp (MMLU 52% vs HellaSwag 35%, basic) is within the target range [10-24pp]; after model-as-facet correction in exp-004 it will be similar (48% vs 31% = 17pp).\\n\"\n  },\n  {\n    \"name\": \"Multi-hardware G-study\",\n    \"description\": \"4 models × 2 GPU types (RTX PRO 6000 + second GPU) × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items.\\n\",\n    \"results\": {\n      \"total_observations\": 1152000,\n      \"hardware_main_binary\": 0.004,\n      \"hardware_x_precision_binary\": 0.008,\n      \"hardware_x_temperature_binary\": 0.003,\n      \"hardware_x_seed_binary\": 0.002,\n      \"hardware_x_prompt_binary\": 0.001,\n      \"hardware_x_methodology_total_binary\": 0.014,\n      \"hardware_x_item_binary\": 0.018,\n      \"total_hardware_related_binary\": 0.036,\n      \"hardware_main_textmatch\": 0.012,\n      \"hardware_x_precision_textmatch\": 0.022,\n      \"hardware_x_methodology_total_textmatch\": 0.032,\n      \"hardware_x_item_textmatch\": 0.028,\n      \"total_hardware_related_textmatch\": 0.072,\n      \"item_id_with_hardware_binary\": 0.5,\n      \"g_correct_binary_gpu1\": 0.37,\n      \"g_correct_binary_gpu2\": 0.36,\n      \"cross_gpu_gap_bf16_mean_pp\": 0.12,\n      \"cross_gpu_gap_fp16_mean_pp\": 0.75,\n      \"cross_gpu_gap_bf16_max_pp\": 0.2,\n      \"cross_gpu_gap_fp16_max_pp\": 1.1,\n      \"model_ranking_preserved_across_gpus\": true,\n      \"hardware_variance_fp16_subset\": 0.022,\n      \"hardware_variance_bf16_subset\": 0.003\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: Hardware Facet Variance Components\",\n        \"columns\": [\n          \"Source\",\n          \"Binary %\",\n          \"Text-match %\"\n        ],\n        \"rows\": [\n          [\n            \"hardware (main)\",\n            \"0.4%\",\n            \"1.2%\"\n          ],\n          [\n            \"hardware×precision\",\n            \"0.8%\",\n            \"2.2%\"\n          ],\n          [\n            \"hardware×temperature\",\n            \"0.3%\",\n            \"0.6%\"\n          ],\n          [\n            \"hardware×seed\",\n            \"0.2%\",\n            \"0.4%\"\n          ],\n          [\n            \"hardware×prompt\",\n            \"0.1%\",\n            \"0.3%\"\n          ],\n          [\n            \"hardware×item\",\n            \"1.8%\",\n            \"2.8%\"\n          ],\n          [\n            \"Total hardware-related\",\n            \"3.6%\",\n            \"7.5%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 10: Cross-GPU Accuracy by Model and Precision\",\n        \"columns\": [\n          \"Model\",\n          \"GPU1-BF16\",\n          \"GPU2-BF16\",\n          \"Δ(pp)\",\n          \"GPU1-FP16\",\n          \"GPU2-FP16\",\n          \"Δ(pp)\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B\",\n            \"0.710\",\n            \"0.709\",\n            \"0.1\",\n            \"0.706\",\n            \"0.700\",\n            \"0.6\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            \"0.672\",\n            \"0.672\",\n            \"0.0\",\n            \"0.669\",\n            \"0.661\",\n            \"0.8\"\n          ],\n          [\n            \"Gemma-2-9B\",\n            \"0.660\",\n            \"0.659\",\n            \"0.1\",\n            \"0.658\",\n            \"0.649\",\n            \"0.9\"\n          ],\n          [\n            \"Mistral-7B\",\n            \"0.694\",\n            \"0.693\",\n            \"0.1\",\n            \"0.691\",\n            \"0.680\",\n            \"1.1\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 11: Hardware Effect Conditioned on Precision\",\n        \"columns\": [\n          \"Metric\",\n          \"BF16 Only\",\n          \"FP16 Only\"\n        ],\n        \"rows\": [\n          [\n            \"Hardware % total variance\",\n            \"0.3%\",\n            \"2.2%\"\n          ],\n          [\n            \"Mean cross-GPU gap (pp)\",\n            \"0.12\",\n            \"0.75\"\n          ],\n          [\n            \"Max cross-GPU gap (pp)\",\n            \"0.2\",\n            \"1.1\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Hardware is a manageable confound, not a showstopper. Separability claim (Claim 2) survives with qualification: \\\"hardware×methodology is ≤1.4% under binary scoring\\\" — but the FP16 hardware sensitivity (2.2% when conditioned on FP16) warrants a Discussion paragraph. Practical recommendation: prefer BF16 for hardware-independent reproducibility; if FP16 is necessary for memory, acknowledge ~1pp cross-GPU uncertainty. The hardware×item overlap with precision×item suggests a unified \\\"logit perturbation\\\" mechanism — items near decision boundaries are vulnerable to both precision and hardware nondeterminism. This is a potential Discussion point but not a formal claim.\\n\\n\\nHardware main effect at 0.4% binary is negligible because both GPUs implement the same IEEE 754 operations; differences arise only from CUDA kernel scheduling nondeterminism and memory subsystem timing. The critical finding is hardware×precision at 0.8% binary: FP16 is more hardware-sensitive than BF16 (cross-GPU gap 0.75pp vs 0.12pp), because FP16's narrower dynamic range (5-bit exponent vs BF16's 8-bit) makes accumulation order hardware-dependent — consistent with Yuan et al. (2025). When subsetting to FP16-only data, hardware explains 2.2% of variance (within median narrative's \\\"1-3% on one precision\\\"). Under text-match, hardware effects roughly double (total 7.2%) because different GPU kernel orderings produce different final tokens in long generations, amplified by exact-match scoring. Hardware×item at 1.8% binary means certain items near decision boundaries are hardware-sensitive — the same items that are precision-sensitive (prec:item) are also hardware-sensitive, consistent with a shared mechanism of logit perturbation near thresholds. Model rankings are fully preserved across GPUs (Kendall tau = 1.0 at all condition combinations) — hardware effects are far too small to alter comparative model evaluation. Total hardware-related variance at 3.6% binary is manageable but nonzero, requiring \\\"approximately separable\\\" language.\\n\"\n  },\n  {\n    \"name\": \"Comprehensive combined analysis\",\n    \"description\": \"Reanalysis of all exp-001/001b/002/003 data: (a) model-as-facet G-theory, (b) bootstrap CIs (1000 resamples), (c) D-study projections, (d) REML vs Henderson, (e) logprob scoring, (f) ranking stability, (g) higher-order interactions.\\n\",\n    \"results\": {\n      \"mmlu_item_id_model_facet\": 0.48,\n      \"mmlu_model_main\": 0.05,\n      \"mmlu_model_x_item\": 0.21,\n      \"mmlu_residual_model_facet\": 0.08,\n      \"mmlu_prompt_item_model_facet\": 0.053,\n      \"mmlu_temp_item_model_facet\": 0.048,\n      \"mmlu_prec_item_model_facet\": 0.028,\n      \"mmlu_precision_main_model_facet\": 0.025,\n      \"mmlu_temperature_main_model_facet\": 0.012,\n      \"gsm8k_item_id_model_facet\": 0.36,\n      \"gsm8k_model_x_item\": 0.18,\n      \"gsm8k_model_main\": 0.04,\n      \"arc_item_id_model_facet\": 0.46,\n      \"arc_model_x_item\": 0.16,\n      \"arc_model_main\": 0.04,\n      \"hellaswag_item_id_model_facet\": 0.31,\n      \"hellaswag_model_x_item\": 0.19,\n      \"hellaswag_model_main\": 0.05,\n      \"item_id_reduction_mmlu_pp\": 4.0,\n      \"item_id_reduction_gsm8k_pp\": 4.0,\n      \"item_id_reduction_arc_pp\": 4.0,\n      \"item_id_reduction_hellaswag_pp\": 4.0,\n      \"mmlu_item_id_ci\": [\n        0.41,\n        0.55\n      ],\n      \"mmlu_item_id_ci_width\": 0.14,\n      \"gsm8k_item_id_ci\": [\n        0.29,\n        0.43\n      ],\n      \"gsm8k_item_id_ci_width\": 0.14,\n      \"arc_item_id_ci\": [\n        0.39,\n        0.53\n      ],\n      \"arc_item_id_ci_width\": 0.14,\n      \"hellaswag_item_id_ci\": [\n        0.24,\n        0.38\n      ],\n      \"hellaswag_item_id_ci_width\": 0.14,\n      \"gradient_high_endpoint_ci\": [\n        0.41,\n        0.55\n      ],\n      \"gradient_low_endpoint_ci\": [\n        0.24,\n        0.38\n      ],\n      \"gradient_endpoint_overlap\": true,\n      \"gradient_overlap_range\": [\n        0.38,\n        0.41\n      ],\n      \"gradient_direction_p_value\": 0.003,\n      \"gsm8k_infra_x_method_ci\": [\n        0.012,\n        0.048\n      ],\n      \"mmlu_infra_x_method_ci\": [\n        0.0,\n        0.012\n      ],\n      \"mmlu_model_x_item_ci\": [\n        0.16,\n        0.27\n      ],\n      \"dstudy_items_g80_mmlu\": 220,\n      \"dstudy_items_g90_mmlu\": 420,\n      \"dstudy_items_g95_mmlu\": 680,\n      \"dstudy_items_g80_gsm8k\": 150,\n      \"dstudy_items_g90_gsm8k\": 280,\n      \"dstudy_items_g95_gsm8k\": 450,\n      \"dstudy_items_g80_arc\": 200,\n      \"dstudy_items_g90_arc\": 380,\n      \"dstudy_items_g95_arc\": 620,\n      \"dstudy_items_g80_hellaswag\": 130,\n      \"dstudy_items_g90_hellaswag\": 240,\n      \"dstudy_items_g95_hellaswag\": 400,\n      \"dstudy_optimal_prompts_mmlu\": 3,\n      \"dstudy_optimal_seeds_mmlu\": 4,\n      \"dstudy_optimal_prompts_gsm8k\": 4,\n      \"dstudy_optimal_seeds_gsm8k\": 6,\n      \"dstudy_items_g90_ci_mmlu\": [\n        350,\n        510\n      ],\n      \"dstudy_items_g90_ci_gsm8k\": [\n        220,\n        360\n      ],\n      \"dstudy_ratio_mmlu_vs_hellaswag\": 1.75,\n      \"dstudy_ratio_mmlu_vs_gsm8k\": 1.5,\n      \"reml_henderson_max_diff_pp\": 2.1,\n      \"reml_henderson_rank_preserved\": true,\n      \"mmlu_item_id_logprob\": 0.55,\n      \"mmlu_g_logprob\": 0.32,\n      \"gsm8k_item_id_logprob\": 0.42,\n      \"model_rank_flip_pct_across_conditions\": 0.12,\n      \"rank_flip_driver\": \"temperature=1.0\",\n      \"precision_causes_rank_flip\": false,\n      \"three_way_interactions_total_mmlu\": 0.03,\n      \"three_way_interactions_total_gsm8k\": 0.05\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 12: Model-as-Facet Reanalysis — All Benchmarks (Binary)\",\n        \"columns\": [\n          \"Source\",\n          \"MMLU\",\n          \"GSM8K\",\n          \"ARC\",\n          \"HellaSwag\"\n        ],\n        \"rows\": [\n          [\n            \"item_id\",\n            \"48.0%\",\n            \"36.0%\",\n            \"46.0%\",\n            \"31.0%\"\n          ],\n          [\n            \"model×item\",\n            \"21.0%\",\n            \"18.0%\",\n            \"16.0%\",\n            \"19.0%\"\n          ],\n          [\n            \"model (main)\",\n            \"5.0%\",\n            \"4.0%\",\n            \"4.0%\",\n            \"5.0%\"\n          ],\n          [\n            \"residual\",\n            \"8.0%\",\n            \"10.0%\",\n            \"8.0%\",\n            \"10.0%\"\n          ],\n          [\n            \"temp:item\",\n            \"4.8%\",\n            \"9.0%\",\n            \"5.0%\",\n            \"8.5%\"\n          ],\n          [\n            \"seed:item\",\n            \"2.0%\",\n            \"5.5%\",\n            \"3.0%\",\n            \"7.0%\"\n          ],\n          [\n            \"prompt:item\",\n            \"5.3%\",\n            \"5.5%\",\n            \"7.5%\",\n            \"6.5%\"\n          ],\n          [\n            \"prec:item\",\n            \"2.8%\",\n            \"1.2%\",\n            \"2.0%\",\n            \"1.2%\"\n          ],\n          [\n            \"precision (main)\",\n            \"2.5%\",\n            \"0.8%\",\n            \"0.8%\",\n            \"0.3%\"\n          ],\n          [\n            \"temperature (main)\",\n            \"1.2%\",\n            \"3.5%\",\n            \"2.2%\",\n            \"4.0%\"\n          ],\n          [\n            \"infra×method\",\n            \"0.4%\",\n            \"3.0%\",\n            \"0.5%\",\n            \"0.3%\"\n          ],\n          [\n            \"other\",\n            \"0.0%\",\n            \"3.5%\",\n            \"5.0%\",\n            \"7.2%\"\n          ]\n        ],\n        \"note\": \"Rows may not sum to 100% due to rounding and higher-order terms in 'other.'\"\n      },\n      {\n        \"name\": \"Table 13: Bootstrap 95% CIs on Key Variance Components\",\n        \"columns\": [\n          \"Component\",\n          \"MMLU\",\n          \"GSM8K\",\n          \"ARC\",\n          \"HellaSwag\"\n        ],\n        \"rows\": [\n          [\n            \"item_id\",\n            \"[0.41, 0.55]\",\n            \"[0.29, 0.43]\",\n            \"[0.39, 0.53]\",\n            \"[0.24, 0.38]\"\n          ],\n          [\n            \"model×item\",\n            \"[0.16, 0.27]\",\n            \"[0.13, 0.24]\",\n            \"[0.11, 0.22]\",\n            \"[0.14, 0.25]\"\n          ],\n          [\n            \"infra×method\",\n            \"[0.00, 0.012]\",\n            \"[0.012, 0.048]\",\n            \"[0.00, 0.014]\",\n            \"[0.00, 0.010]\"\n          ]\n        ],\n        \"note\": \"1000 bootstrap resamples (items × conditions). GSM8K infra×method CI excludes 0.\"\n      },\n      {\n        \"name\": \"Table 14: D-Study — Items Needed for Target G (BF16, optimal prompt/seed)\",\n        \"columns\": [\n          \"Benchmark\",\n          \"G≥0.80\",\n          \"G≥0.90\",\n          \"G≥0.90 CI\",\n          \"G≥0.95\",\n          \"Prompts\",\n          \"Seeds\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            \"220\",\n            \"420\",\n            \"[350, 510]\",\n            \"680\",\n            \"3\",\n            \"4\"\n          ],\n          [\n            \"ARC\",\n            \"200\",\n            \"380\",\n            \"[310, 470]\",\n            \"620\",\n            \"3\",\n            \"4\"\n          ],\n          [\n            \"GSM8K\",\n            \"150\",\n            \"280\",\n            \"[220, 360]\",\n            \"450\",\n            \"4\",\n            \"6\"\n          ],\n          [\n            \"HellaSwag\",\n            \"130\",\n            \"240\",\n            \"[190, 310]\",\n            \"400\",\n            \"4\",\n            \"6\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 15: Scoring Metric Comparison (MMLU, Model-as-Facet)\",\n        \"columns\": [\n          \"Source\",\n          \"Binary\",\n          \"Text-match\",\n          \"Logprob\"\n        ],\n        \"rows\": [\n          [\n            \"item_id\",\n            \"48.0%\",\n            \"3.0%\",\n            \"55.0%\"\n          ],\n          [\n            \"model×item\",\n            \"21.0%\",\n            \"1.5%\",\n            \"18.0%\"\n          ],\n          [\n            \"prompt:item\",\n            \"5.3%\",\n            \"33.0%\",\n            \"4.0%\"\n          ],\n          [\n            \"residual\",\n            \"8.0%\",\n            \"36.0%\",\n            \"6.0%\"\n          ],\n          [\n            \"G coefficient\",\n            \"0.37\",\n            \"0.97\",\n            \"0.32\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 16: REML vs Henderson Method I (MMLU, Binary)\",\n        \"columns\": [\n          \"Source\",\n          \"Henderson %\",\n          \"REML %\",\n          \"Diff (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"item_id\",\n            \"48.0%\",\n            \"49.2%\",\n            \"+1.2\"\n          ],\n          [\n            \"model×item\",\n            \"21.0%\",\n            \"22.4%\",\n            \"+1.4\"\n          ],\n          [\n            \"residual\",\n            \"8.0%\",\n            \"6.1%\",\n            \"-1.9\"\n          ],\n          [\n            \"other sources\",\n            \"23.0%\",\n            \"22.3%\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Five key takeaways for the paper. (1) Model-as-facet reduces item_id by ~4pp on ALL benchmarks — prior single-model studies systematically overestimated pure item dominance. Frame as: \\\"even within the 7-9B parameter range, model-specific knowledge gaps account for 16-21% of variance, meaning item difficulty estimates from single-model studies are inflated.\\\" (2) Gradient direction is significant (p=0.003) but magnitude CIs overlap at endpoints — use \\\"10-30pp spread\\\" in claims. (3) GSM8K infra×method CI [1.2%, 4.8%] excludes zero — this is a statistically robust departure from separability, requiring benchmark qualification on Claim 2. (4) D-study budgets differentiate benchmarks but the ratio (1.5-1.75×, not 3×) means the practical implication is real but less dramatic than hoped. (5) Logprob scoring amplifies item_id to 55% — a third metric perspective that strengthens the metric-conditional narrative.\\n\\n\\nModel-as-facet is the most consequential reanalysis. On MMLU, 21% of total variance is model×item — this is not \\\"model difficulty\\\" but model-SPECIFIC item difficulty: items that are hard for Llama but easy for Qwen due to model-specific knowledge gaps and training data overlap. Absorbing this from item_id (52%→48%) and residual (14%→8%) properly attributes variance that prior single-model studies would have assigned to \\\"item difficulty.\\\" The 4pp reduction is consistent across all benchmarks, suggesting the model-facet correction is systematic rather than benchmark-specific. Bootstrap CI width of 0.14 on item_id reflects both item-resampling instability (exp-001b CV=19%) and condition-resampling instability. The gradient endpoint CIs overlap narrowly: MMLU lower CI (0.41) exceeds HellaSwag upper CI (0.38) by only 3pp, so the gradient direction is statistically significant (p=0.003 by permutation test) but the magnitude is imprecise — the paper should say \\\"10-30pp spread\\\" not \\\"17pp.\\\" D-study projections differentiate benchmarks: MMLU needs 420 items for G≥0.90 vs HellaSwag 240, a 1.75× ratio. This is directionally useful but less dramatic than a clean gradient would predict — the practical message is \\\"50-75% more items for knowledge vs reasoning benchmarks,\\\" not \\\"3× more items.\\\" D-study CIs on MMLU G≥0.90 ([350, 510]) show that even the recommended item count is imprecise. REML and Henderson agree to within 2.1pp — methodological choice doesn't affect qualitative conclusions. Logprob scoring increases item_id to 55% on MMLU because continuous logprobs capture fine-grained difficulty more sensitively than binary 0/1. Model rank flips occur in 12% of condition pairs, driven entirely by temperature=1.0 (high-temperature conditions produce enough noise to flip rankings of close models); precision never causes rank flips. Three-way interactions total 3-5% — most variance is captured by main effects and 2-way terms.\\n\"\n  },\n  {\n    \"name\": \"14B model scale extension\",\n    \"description\": \"Qwen3-14B + DeepSeek-R1-Distill-14B at BF16/FP16 × 6 prompts × 6 seeds × 2 temperatures × 4 orderings × 200 MMLU items on datacenter GPUs (≥48GB VRAM).\\n\",\n    \"results\": {\n      \"qwen3_14b_accuracy_bf16\": 0.745,\n      \"deepseek_r1_14b_accuracy_bf16\": 0.728,\n      \"item_id_14b_model_facet\": 0.44,\n      \"model_x_item_14b\": 0.25,\n      \"model_main_14b\": 0.07,\n      \"residual_14b\": 0.06,\n      \"temp_x_item_14b\": 0.06,\n      \"prompt_x_item_14b\": 0.045,\n      \"precision_main_14b\": 0.003,\n      \"g_correct_14b_binary\": 0.4,\n      \"deepseek_r1_temp_x_item\": 0.085,\n      \"qwen3_14b_temp_x_item\": 0.042,\n      \"cross_gpu_gap_14b_bf16_pp\": 0.1,\n      \"item_id_8b_vs_14b_diff_pp\": 4.0,\n      \"model_x_item_8b_vs_14b_diff_pp\": 4.0,\n      \"variance_hierarchy_qualitatively_preserved\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 17: 8B vs 14B Variance Decomposition (MMLU, Model-as-Facet)\",\n        \"columns\": [\n          \"Source\",\n          \"8B (4 models)\",\n          \"14B (2 models)\",\n          \"Δ\"\n        ],\n        \"rows\": [\n          [\n            \"item_id\",\n            \"48.0%\",\n            \"44.0%\",\n            \"-4.0pp\"\n          ],\n          [\n            \"model×item\",\n            \"21.0%\",\n            \"25.0%\",\n            \"+4.0pp\"\n          ],\n          [\n            \"model (main)\",\n            \"5.0%\",\n            \"7.0%\",\n            \"+2.0pp\"\n          ],\n          [\n            \"residual\",\n            \"8.0%\",\n            \"6.0%\",\n            \"-2.0pp\"\n          ],\n          [\n            \"temp:item\",\n            \"4.8%\",\n            \"6.0%\",\n            \"+1.2pp\"\n          ],\n          [\n            \"prompt:item\",\n            \"5.3%\",\n            \"4.5%\",\n            \"-0.8pp\"\n          ],\n          [\n            \"precision (main)\",\n            \"2.5%\",\n            \"0.3%\",\n            \"-2.2pp\"\n          ],\n          [\n            \"other\",\n            \"5.4%\",\n            \"7.2%\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 18: Per-Architecture Temperature Sensitivity (14B)\",\n        \"columns\": [\n          \"Model\",\n          \"Type\",\n          \"temp:item\",\n          \"temp=0.0 Acc\",\n          \"temp=1.0 Acc\",\n          \"Spread\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-14B\",\n            \"Dense\",\n            \"4.2%\",\n            \"0.752\",\n            \"0.738\",\n            \"1.4pp\"\n          ],\n          [\n            \"DeepSeek-R1-14B\",\n            \"Reasoning-distilled\",\n            \"8.5%\",\n            \"0.740\",\n            \"0.715\",\n            \"2.5pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Scale extension confirms qualitative stability: item_id > model×item > residual hierarchy holds at 14B. The 4pp item_id reduction per scale doubling (8B→14B) suggests that at current model sizes, item difficulty remains the dominant variance source — much larger models (70B+) would be needed to substantively alter the hierarchy. The dense-vs-reasoning architecture finding is a useful Discussion point: model×item increases not from more models but from more architecturally diverse models. For the paper: \\\"variance structure is qualitatively stable across 7-14B but item dominance magnitude is scale- and architecture-dependent.\\\" Frame as scope validation, not a primary finding. The precision reduction from 2.5% to 0.3% at 14B (both at BF16/FP16 only, no FP32) is because the FP32 degradation source is absent from this experiment.\\n\\n\\n14B models show 44% item_id (vs 48% at 8B) because higher capacity reduces floor effects — items that were impossible for 8B models become solvable at 14B, compressing between-item variance. The 4pp reduction is modest, suggesting item difficulty saturation is far from reached even at 14B. Model×item interaction rises to 25% (from 21%) because the dense-vs-reasoning-distilled architecture difference creates larger model-specific item profiles: DeepSeek-R1-Distill-14B excels on multi-step reasoning items (distilled from R1's reasoning traces) while Qwen3-14B excels on factual knowledge items (larger pre-training corpus). This architecture-driven specialization is larger than the Llama-vs-Qwen difference at 8B. DeepSeek shows elevated temperature×item (8.5% vs Qwen's 4.2%) because reasoning-distilled models produce chain-of-thought that branches more at sampling time — consistent with exp-002's finding that reasoning tasks show higher temperature sensitivity. Model main effect at 7% (vs 5% at 8B) reflects the larger accuracy spread between dense and reasoning-distilled architectures. Precision effect remains negligible (0.3pp) — precision sensitivity does not increase with scale in this range. G-coefficient of 0.40 is slightly higher than 8B (0.37) because reduced item variance improves relative reliability.\\n\"\n  },\n  {\n    \"name\": \"Fine-tuning G-study (RoBERTa)\",\n    \"description\": \"RoBERTa-large fine-tuning on SST-2/MNLI/RTE/COPA. 6 seeds × 3 LRs × 4 data shuffles × 3 GPUs × 2 precisions = 432 runs/task × 4 tasks = 1,728 total runs.\\n\",\n    \"results\": {\n      \"sst2_accuracy_mean\": 0.942,\n      \"sst2_accuracy_sd\": 0.005,\n      \"sst2_lr_variance\": 0.35,\n      \"sst2_seed_variance\": 0.25,\n      \"sst2_data_shuffle_variance\": 0.12,\n      \"sst2_seed_x_lr_variance\": 0.1,\n      \"sst2_gpu_variance\": 0.003,\n      \"sst2_precision_variance\": 0.008,\n      \"sst2_residual\": 0.159,\n      \"mnli_accuracy_mean\": 0.875,\n      \"mnli_accuracy_sd\": 0.008,\n      \"mnli_lr_variance\": 0.3,\n      \"mnli_seed_variance\": 0.22,\n      \"mnli_data_shuffle_variance\": 0.15,\n      \"mnli_seed_x_lr_variance\": 0.12,\n      \"mnli_gpu_variance\": 0.004,\n      \"mnli_precision_variance\": 0.009,\n      \"mnli_residual\": 0.177,\n      \"rte_accuracy_mean\": 0.716,\n      \"rte_accuracy_sd\": 0.032,\n      \"rte_lr_variance\": 0.2,\n      \"rte_seed_variance\": 0.16,\n      \"rte_data_shuffle_variance\": 0.28,\n      \"rte_seed_x_lr_variance\": 0.16,\n      \"rte_gpu_variance\": 0.005,\n      \"rte_precision_variance\": 0.01,\n      \"rte_residual\": 0.175,\n      \"copa_accuracy_mean\": 0.672,\n      \"copa_accuracy_sd\": 0.038,\n      \"copa_lr_variance\": 0.18,\n      \"copa_seed_variance\": 0.2,\n      \"copa_data_shuffle_variance\": 0.3,\n      \"copa_seed_x_lr_variance\": 0.14,\n      \"copa_gpu_variance\": 0.004,\n      \"copa_precision_variance\": 0.012,\n      \"copa_residual\": 0.134,\n      \"dominant_source_large_data\": \"learning_rate\",\n      \"dominant_source_small_data\": \"data_shuffle\",\n      \"gpu_all_tasks_max\": 0.005,\n      \"precision_all_tasks_max\": 0.012,\n      \"hierarchy_differs_from_inference\": true,\n      \"rte_bimodal_seed_lr\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 19: Fine-Tuning Variance Decomposition Across Tasks\",\n        \"columns\": [\n          \"Source\",\n          \"SST-2\",\n          \"MNLI\",\n          \"RTE\",\n          \"COPA\"\n        ],\n        \"rows\": [\n          [\n            \"learning_rate\",\n            \"35.0%\",\n            \"30.0%\",\n            \"20.0%\",\n            \"18.0%\"\n          ],\n          [\n            \"seed\",\n            \"25.0%\",\n            \"22.0%\",\n            \"16.0%\",\n            \"20.0%\"\n          ],\n          [\n            \"data_shuffle\",\n            \"12.0%\",\n            \"15.0%\",\n            \"28.0%\",\n            \"30.0%\"\n          ],\n          [\n            \"seed×lr\",\n            \"10.0%\",\n            \"12.0%\",\n            \"16.0%\",\n            \"14.0%\"\n          ],\n          [\n            \"gpu\",\n            \"0.3%\",\n            \"0.4%\",\n            \"0.5%\",\n            \"0.4%\"\n          ],\n          [\n            \"precision\",\n            \"0.8%\",\n            \"0.9%\",\n            \"1.0%\",\n            \"1.2%\"\n          ],\n          [\n            \"residual\",\n            \"16.9%\",\n            \"19.7%\",\n            \"18.5%\",\n            \"16.4%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 20: Inference vs Fine-Tuning Variance Hierarchy\",\n        \"columns\": [\n          \"Rank\",\n          \"Inference (MMLU)\",\n          \"FT — Large (SST-2)\",\n          \"FT — Small (RTE)\"\n        ],\n        \"rows\": [\n          [\n            \"#1\",\n            \"item_id (48%)\",\n            \"learning_rate (35%)\",\n            \"data_shuffle (28%)\"\n          ],\n          [\n            \"#2\",\n            \"model×item (21%)\",\n            \"seed (25%)\",\n            \"learning_rate (20%)\"\n          ],\n          [\n            \"#3\",\n            \"residual (8%)\",\n            \"residual (17%)\",\n            \"seed×lr (16%)\"\n          ],\n          [\n            \"#4\",\n            \"prompt:item (5%)\",\n            \"data_shuffle (12%)\",\n            \"seed (16%)\"\n          ],\n          [\n            \"Infra\",\n            \"precision 2.5%\",\n            \"gpu+prec 1.1%\",\n            \"gpu+prec 1.5%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Fine-tuning results support the paper's broader thesis at a meta-level: variance structure is task-conditional, and this extends beyond benchmarks to evaluation MODES. The LR-dominated (large data) vs shuffle-dominated (small data) pattern in fine-tuning parallels the knowledge-item-dominated vs reasoning-interaction-dominated pattern in inference — in both cases, the dominant source shifts as the task's \\\"difficulty structure\\\" changes. Infrastructure effects remain negligible in both settings, providing cross-mode evidence for separability (with the caveat that fine-tuning doesn't test the temperature/seed × precision interactions that drive GSM8K's infra×method departure). For the paper: position as Discussion material showing G-theory generality. Explicit caveat: encoder-only fine-tuning (RoBERTa) may not generalize to decoder fine-tuning where generation-related variance sources (temperature, seed) would re-enter.\\n\\n\\nFine-tuning variance structure is qualitatively different from inference: hyperparameters (LR, seed, data shuffle) dominate instead of items. On large datasets (SST-2, MNLI), learning rate dominates (30-35%) because the optimization landscape is well-defined and LR determines the convergence basin — too high overshoots, too low underfits, and the sensitivity is amplified by RoBERTa's sharp loss surface near the optimum (Dodge et al., 2020). On small datasets (RTE, COPA), data shuffle dominates (28-30%) because mini-batch composition has outsized influence with fewer training examples — a single misplaced hard example in early batches can steer the model into a different loss basin. Seed is substantial everywhere (16-25%) because weight initialization and dropout mask jointly determine the optimization trajectory. The seed×LR interaction (10-16%) is the fine-tuning analog of item×temperature in inference: certain seed-LR combinations land in qualitatively different loss basins, producing bimodal accuracy distributions on RTE (two clusters separated by ~4pp accuracy, one basin near 72% and one near 68%). GPU and precision effects remain negligible (<1.2%) across all tasks — the variance hierarchy for infrastructure factors is consistent between fine-tuning and inference, even though the methodology-factor hierarchy differs completely. This validates the G-theory framework's generality while showing that reproducibility budgets cannot be transferred between evaluation modes.\\n\"\n  },\n  {\n    \"name\": \"LayerCast precision mitigation\",\n    \"description\": \"LayerCast (FP16 storage + FP32 compute) as additional precision condition on MMLU. Same 4 models × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 items.\\n\",\n    \"results\": {\n      \"layercast_accuracy_mean\": 0.682,\n      \"layercast_vs_bf16_gap_pp\": 0.2,\n      \"layercast_vs_fp16_gap_pp\": 0.1,\n      \"layercast_vs_fp32_gap_pp\": 2.7,\n      \"layercast_item_id_binary\": 0.515,\n      \"layercast_prec_x_item_reduction_vs_fp16_pct\": 40,\n      \"layercast_g_correct_binary\": 0.37,\n      \"layercast_inference_overhead_pct\": 18,\n      \"layercast_prec_x_temp_binary\": 0.001,\n      \"layercast_prec_x_temp_textmatch\": 0.008\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 21: LayerCast Comparison Across Precision Modes\",\n        \"columns\": [\n          \"Metric\",\n          \"FP32\",\n          \"BF16\",\n          \"FP16\",\n          \"LayerCast\"\n        ],\n        \"rows\": [\n          [\n            \"Accuracy\",\n            \"0.655\",\n            \"0.684\",\n            \"0.681\",\n            \"0.682\"\n          ],\n          [\n            \"item_id %\",\n            \"50.5%\",\n            \"52.0%\",\n            \"51.8%\",\n            \"51.5%\"\n          ],\n          [\n            \"prec:item %\",\n            \"5.8%\",\n            \"4.5%\",\n            \"5.0%\",\n            \"3.0%\"\n          ],\n          [\n            \"prec×temp (binary)\",\n            \"0.3%\",\n            \"0.1%\",\n            \"0.2%\",\n            \"0.1%\"\n          ],\n          [\n            \"prec×temp (text)\",\n            \"2.5%\",\n            \"1.8%\",\n            \"2.2%\",\n            \"0.8%\"\n          ],\n          [\n            \"G (binary)\",\n            \"0.36\",\n            \"0.37\",\n            \"0.37\",\n            \"0.37\"\n          ],\n          [\n            \"Inference cost (rel.)\",\n            \"1.35×\",\n            \"1.00×\",\n            \"1.00×\",\n            \"1.18×\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"LayerCast is a footnote finding. Precision effects are already small post-confound analysis (precision main 2.5-3% of total, infra×method <0.5% on knowledge benchmarks). Mitigating them further with LayerCast provides diminishing returns at 18% inference cost. Include as 1-2 paragraphs in Discussion or as appendix material. Practical recommendation: use BF16 — it has no overhead and minimal precision artifacts. LayerCast is only worth mentioning to preempt reviewer questions about mitigation strategies.\\n\\n\\nLayerCast reduces precision:item interaction by ~40% vs FP16 because the FP32 compute path eliminates mid-layer accumulation errors that flip items near decision boundaries. However, the practical benefit is marginal: FP16 precision:item was already only 5% of total variance, so a 40% reduction brings it to ~3% — still dwarfed by item_id at 51.5%. Accuracy (0.682) falls between BF16 (0.684) and FP16 (0.681), essentially equivalent to both. The precision×temperature interaction drops to 0.1% binary (from FP16's ~0.2%) because FP32 compute stabilizes the logit computation at each sampling step. The 18% inference overhead comes from FP16→FP32 upcasting at each transformer layer. G-coefficient is unchanged (0.37) because the dominant item_id component is unaffected by precision mitigation. Given that BF16 already shows negligible precision effects and has no inference overhead, LayerCast is only relevant for the specific case where FP16 memory savings are required AND cross-hardware reproducibility matters.\\n\"\n  },\n  {\n    \"name\": \"MATH benchmark extension\",\n    \"description\": \"MATH (200 items) with 4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures × 4 orderings. Tests chain-of-thought reasoning variance.\\n\",\n    \"results\": {\n      \"math_accuracy_mean\": 0.38,\n      \"math_accuracy_sd_across_conditions\": 0.045,\n      \"math_item_id_basic\": 0.32,\n      \"math_residual_basic\": 0.17,\n      \"math_temp_x_item_basic\": 0.14,\n      \"math_seed_x_item_basic\": 0.11,\n      \"math_prompt_x_item_basic\": 0.08,\n      \"math_temperature_main_basic\": 0.06,\n      \"math_precision_main_basic\": 0.005,\n      \"math_infra_x_method_binary\": 0.025,\n      \"math_other_basic\": 0.09,\n      \"math_item_id_model_facet\": 0.28,\n      \"math_model_x_item\": 0.22,\n      \"math_model_main\": 0.06,\n      \"math_residual_model_facet\": 0.07,\n      \"math_g_correct_binary\": 0.52,\n      \"five_benchmark_item_id_range\": [\n        0.28,\n        0.48\n      ],\n      \"five_benchmark_spread_pp\": 20,\n      \"five_benchmark_pattern\": \"{MMLU 48%, ARC 46%} > {GSM8K 36%, HellaSwag 31%} ≥ {MATH 28%}\",\n      \"three_tier_structure\": true,\n      \"math_infra_x_method_textmatch\": 0.042\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 22: MATH Variance Decomposition (Binary, Model-as-Facet)\",\n        \"columns\": [\n          \"Source\",\n          \"MATH\",\n          \"GSM8K (ref)\",\n          \"MMLU (ref)\"\n        ],\n        \"rows\": [\n          [\n            \"item_id\",\n            \"28.0%\",\n            \"36.0%\",\n            \"48.0%\"\n          ],\n          [\n            \"model×item\",\n            \"22.0%\",\n            \"18.0%\",\n            \"21.0%\"\n          ],\n          [\n            \"temp:item\",\n            \"14.0%\",\n            \"9.0%\",\n            \"4.8%\"\n          ],\n          [\n            \"seed:item\",\n            \"11.0%\",\n            \"5.5%\",\n            \"2.0%\"\n          ],\n          [\n            \"prompt:item\",\n            \"6.5%\",\n            \"5.5%\",\n            \"5.3%\"\n          ],\n          [\n            \"model (main)\",\n            \"6.0%\",\n            \"4.0%\",\n            \"5.0%\"\n          ],\n          [\n            \"residual\",\n            \"7.0%\",\n            \"10.0%\",\n            \"8.0%\"\n          ],\n          [\n            \"temperature\",\n            \"4.5%\",\n            \"3.5%\",\n            \"1.2%\"\n          ],\n          [\n            \"infra×method\",\n            \"2.5%\",\n            \"3.0%\",\n            \"0.4%\"\n          ],\n          [\n            \"other\",\n            \"-1.5%\",\n            \"5.5%\",\n            \"4.3%\"\n          ]\n        ],\n        \"note\": \"Negative 'other' due to rounding and minor negative Henderson estimates on near-zero terms.\"\n      },\n      {\n        \"name\": \"Table 23: Updated 5-Benchmark Summary (Model-as-Facet)\",\n        \"columns\": [\n          \"Benchmark\",\n          \"Type\",\n          \"item_id\",\n          \"G (binary)\",\n          \"infra×method\",\n          \"Tier\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            \"Knowledge\",\n            \"48.0%\",\n            \"0.37\",\n            \"0.4%\",\n            \"High\"\n          ],\n          [\n            \"ARC\",\n            \"Knowledge\",\n            \"46.0%\",\n            \"0.35\",\n            \"0.5%\",\n            \"High\"\n          ],\n          [\n            \"GSM8K\",\n            \"Arithmetic reasoning\",\n            \"36.0%\",\n            \"0.42\",\n            \"3.0%\",\n            \"Mid\"\n          ],\n          [\n            \"HellaSwag\",\n            \"Commonsense\",\n            \"31.0%\",\n            \"0.48\",\n            \"0.3%\",\n            \"Mid\"\n          ],\n          [\n            \"MATH\",\n            \"Proof reasoning\",\n            \"28.0%\",\n            \"0.52\",\n            \"2.5%\",\n            \"Low\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"MATH is the median tier's upgrade path. With 5 benchmarks and 20pp spread, the narrative strengthens from \\\"2-cluster\\\" to \\\"task-complexity gradient with 3 tiers\\\": knowledge benchmarks (MMLU, ARC) → arithmetic/commonsense reasoning (GSM8K, HellaSwag) → proof reasoning (MATH). HellaSwag's position (31%, in \\\"mid\\\" tier despite being commonsense rather than math) adds nuance — the gradient tracks multi-step reasoning demand more than domain. MATH also reinforces the GSM8K infra×method finding: both math-heavy benchmarks show 2.5-3% infra×method binary, while knowledge and commonsense benchmarks show <0.5%. This transforms the separability exception from \\\"one benchmark\\\" to \\\"math-generation benchmarks\\\" — a more principled category that strengthens the paper. If AAAI timeline permits exp-008 (50 GPU hours, dependent on exp-002), include it and claim the 3-tier gradient. If not, the 4-benchmark 2-cluster story is publishable with softened framing, and MATH can be added for camera-ready or the ACL submission.\\n\\nMATH shows the lowest item dominance (28% model-as-facet) because multi-step mathematical proofs introduce maximal chain-of-thought variance. Unlike GSM8K's mostly arithmetic word problems, MATH items require proof strategies (induction, construction, algebraic manipulation) with multiple valid approaches — temperature and seed determine which strategy the model attempts, making temp:item (14%) and seed:item (11%) jointly exceed item_id. The 38% overall accuracy (8B models on MATH) creates strong floor effects: ~40% of items are never solved regardless of conditions (zero variance), ~20% are always solved (zero variance), and the remaining ~40% of \\\"mid-difficulty\\\" items carry nearly all the variance — and on these items, condition sensitivity is extreme. G-coefficient at 0.52 (highest of all benchmarks) is counterintuitive but correct: the items that 8B models CAN solve are consistently solved (low relative error), so the universe score is reliable despite high absolute variance. Model×item at 22% is the highest across benchmarks because dense vs reasoning-distilled architectures diverge most on proof items: DeepSeek-R1-Distill can solve certain proof items that no other 8B model touches, creating large model-specific item effects. Adding MATH extends the 2-cluster gradient to a potential 3-tier structure with 20pp total spread (48-28%), strengthening the cognitive-complexity narrative. Infra×method at 2.5% binary confirms the GSM8K pattern: math-heavy generation shows detectable precision×methodology interaction. Under text-match, MATH prec×temp reaches 4.2% (the highest single infra×method interaction) because proof-format outputs are extremely sensitive to token-level differences.\\n\"\n  }\n]",
      "numLines": 1615,
      "startLine": 1,
      "totalLines": 1615
    }
  },
  "sourceToolAssistantUUID": "efabf9ac-c786-4d8d-baae-bf4a4ff7b9d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T23:19:16.071Z_

<details><summary>↩ Tool result · `toolu_01RVcfTmDn3B9qKDzEcYiy1Q`</summary>

```text
1	# Paper Framing — nlp_variance_gtheory
2	
3	## Target Venue
4	- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)
5	- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)
6	- Extended: TACL (rolling)
7	
8	## Title
9	Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics
10	
11	## Core Claims (3 条，可证伪)
12	
13	**Claim 1 — Item Dominance (benchmark-conditional)**: Item selection is the single largest variance source in multiple-choice LLM evaluation, but its magnitude is benchmark-dependent: from ~45% on knowledge-retrieval tasks (MMLU) down to ~25% on reasoning tasks (GSM8K/MATH) where temperature and seed interactions increase. Item dominance is expected from measurement theory when item difficulty varies widely (Brennan, 2001); our contribution is in (a) quantifying the precise magnitude across benchmarks and models, (b) demonstrating the systematic benchmark-dependent gradient, and (c) deriving D-study implications specific to LLM evaluation.
14	
15	**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), "infrastructure" is currently limited to the precision facet.
16	
17	**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent: binary correct scoring yields G=0.357 (item dominance makes G≥0.90 unreachable without massive item expansion), while text-exact-match scoring yields G=0.975 (already adequate). D-study projections show that increasing item sampling is more cost-effective than increasing prompt/seed replication, but the optimal allocation depends critically on both the evaluation metric and the benchmark. Current common practices (1 prompt, 1 seed, ≤200 items, single metric) produce misleading reliability estimates.
18	
19	## Contributions (3 条，明确区分)
20	
21	1. **Cross-benchmark variance gradient**: The first multi-benchmark G-theory analysis showing that variance structure systematically shifts from item-dominated (knowledge retrieval) to interaction-dominated (reasoning tasks), explaining why prior single-benchmark studies reached seemingly contradictory conclusions.
22	
23	2. **Confirmatory separability test**: Infrastructure×methodology interactions are negligible at the aggregate level (<0.5% under binary scoring), providing empirical support for isolated-factor studies — with the caveat that both factors interact with items and the finding is metric-conditional.
24	
25	3. **Task-specific reproducibility budgets**: D-study projections with bootstrap CIs yield actionable, benchmark-specific item/prompt/seed allocations for achieving target reliability (G≥0.90), contextualized against IRT-based subsampling approaches (tinyBenchmarks, HELM-Lite).
26	
27	## Story Spine
28	
29	**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability.
30	
31	**Existing approaches & gaps**: Bouthillier et al. (2021) decomposed ML benchmark variance across hyperparameters, data splits, and seeds via ANOVA, establishing the template for factorial variance decomposition in ML evaluation. Mesting (2026) adapted G-theory to 5 methodological facets in LLM evaluation but treated infrastructure as fixed. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance on fixed hardware. IRT-based approaches (Lalor et al. 2019; Rodriguez et al. 2021; Polo et al. 2024) have analyzed item-level properties and efficient subsampling, but from a different methodological perspective than G-theory. No study has: (a) crossed infrastructure and methodology in a unified G-theory framework, (b) compared variance structure across multiple benchmarks, or (c) provided metric-conditional reproducibility budgets.
32	
33	**Our framing**: We conduct a multi-benchmark G-theory study crossing infrastructure (numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors, with model treated as a crossed facet. The infrastructure crossing yields a confirmatory null result: aggregate separability holds, validating the implicit assumption of prior isolated-factor studies. The primary novel finding is the cross-benchmark variance gradient — item dominance systematically weakens as tasks shift from knowledge retrieval to multi-step reasoning — explaining divergent conclusions in the literature. D-study projections provide the first benchmark-specific, metric-conditional reproducibility budgets for LLM evaluation, directly comparable to IRT-based subsampling approaches.
34	
35	**Headline result template**: "In a G-study of K conditions across M models and N benchmarks, item selection is the largest single variance source on multiple-choice benchmarks (25-55%, benchmark-dependent), while direct infrastructure×methodology interactions are negligible (<0.5% binary, ≤1.3% text-match). Variance structure shifts systematically from item-dominated (knowledge benchmarks) to interaction-dominated (reasoning benchmarks). D-study reproducibility budgets show that optimal facet allocation is both benchmark-specific and metric-conditional: MMLU needs more items, GSM8K needs more seeds."
36	
37	## Hook (Counter-Intuitive Quantified Claim)
38	"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks — our G-theory analysis across N benchmarks shows the variance structure itself is benchmark-conditional, rendering any 'universal reproducibility recipe' illusory."
39	
40	## Narrative Strategy
41	- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Empirical contribution (benchmark-conditional gradient)
42	- **Tension**: "No universal recipe" — the field seeks standardization but variance structure varies qualitatively across task types
43	- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)
44	- **Signature visual**: Stacked-bar variance decomposition chart across benchmarks (field idiom from Mesting/Brittlebench)
45	- **Figure plan** (4 figures minimum):
46	  1. Problem illustration: same model, different benchmark → different dominant variance source
47	  2. G-theory facet diagram showing crossed design
48	  3. Stacked-bar variance decomposition across benchmarks (signature figure)
49	  4. D-study projection curves: G vs item count for different benchmarks
50	- **Key framing shifts from Dream feedback**:
51	  - Infrastructure crossing framed as **confirmatory** (validates isolated-factor studies), not as primary novelty
52	  - Item dominance acknowledged as **psychometrically expected**; contribution is quantification + benchmark gradient
53	  - Cross-benchmark gradient is the **primary novel finding**
54	  - "Fully crossed" language qualified to MMLU exp-001 only; other benchmarks use reduced designs
55	
56	## Venue Fit Risks
57	- AAAI: Strong fit for "evaluation methodology" track. Risk: tight 9-week timeline requires overlapping experiments with writing.
58	- Reviewer concern 1: "Only open-weight models, not API models" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.
59	- Reviewer concern 2: "G-theory is borrowed methodology, not novel" — Frame as cross-domain transfer. The novelty is the cross-benchmark variance gradient finding, not G-theory itself.
60	- Reviewer concern 3: "Item dominance is obvious from measurement theory" — Acknowledge explicitly. Contribution is quantification (25-55%), benchmark-dependence, and D-study implications. Contextualize against IRT item analysis literature.
61	
62	## Anticipated Reviewer Concerns & Planned Responses
63	1. **"Only N GPU types"** → exp-003 (multi-hardware crossing) addresses this. If blocked, explicitly scope to "numerical precision" and frame hardware as future work.
64	2. **"float32 engine confound"** → exp-001 fixes with V0 enforce_eager for all precisions. Confound discovery itself is a standalone methodological contribution.
65	3. **"Only MMLU"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag. Cross-benchmark gradient is the core finding.
66	4. **"Small item sample"** → exp-001 expands from 50 to 200 items. exp-001b tests resampling stability.
67	5. **"No training-time analysis"** → exp-006 (fine-tuning G-study with RoBERTa). Explicitly qualify as encoder-only classification; decoder fine-tuning is future work.
68	6. **"Missing scale validation"** → exp-005 (14B models)
69	7. **"G-theory may not be right framework"** → Compare with ANOVA and regression decomposition as sensitivity analysis. Cite Bouthillier et al. (2021) as ANOVA-based predecessor; show G-theory adds D-study projections.
70	8. **"Separability claim is metric-dependent"** → This is precisely the point: reproducibility budgets must be metric-qualified. Replace arbitrary threshold with bootstrap CI on interaction term.
71	9. **"FP32 degradation is already known (Yuan 2025)"** → Position as supporting finding with novel item-level breakdown. Not an independent claim.
72	10. **"Incremental over Mesting (2026)"** → Infrastructure crossing is confirmatory (valuable as validation, not breakthrough). Primary novelty: cross-benchmark gradient, task-specific budgets, dual-metric analysis, confound fix. Mesting = single benchmark, no infrastructure; we = multi-benchmark, infrastructure confirmation + benchmark gradient.
73	11. **"Model not treated as G-theory facet"** → exp-004 includes model-as-facet reanalysis of MMLU data. Report model×item interaction separately from residual.
74	12. **"No CIs on variance components"** → exp-004 includes bootstrap CIs (1000 resamples) on all variance components in all tables.
75	13. **"Missing related work — IRT, tinyBenchmarks, Bouthillier"** → Comprehensive bibliography (25+ refs). Position D-study budgets against IRT-based subsampling. Cite Bouthillier et al. as ANOVA predecessor.
76	14. **"Diagnostic tool claim unsubstantiated"** → Release analysis pipeline code (G-theory variance decomposition + D-study projections) as reusable tool. Or reframe as "empirical analysis + data release."
77	15. **"Fine-tuning uses encoder-only RoBERTa"** → Explicitly qualify. Decoder fine-tuning is a natural extension requiring substantially more compute.
78	
79	## Design Decisions
80	- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.
81	- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.
82	- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.
83	- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.
84	- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.
85	- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as "reduced crossing" rather than "fully crossed."
86	
87	## Required Bibliography (minimum 25 references)
88	Key references to include beyond current literature_map:
89	- Bouthillier et al. (2021, JMLR) — ML variance decomposition via ANOVA
90	- Lalor et al. (2019, NAACL) — IRT-based item analysis in NLP
91	- Rodriguez et al. (2021, ACL) — IRT evaluation for NLP
92	- Polo et al. (2024) — tinyBenchmarks, IRT-based subsampling
93	- Perlitz et al. (2023) — Efficient LLM benchmarking
94	- Henderson et al. (2018) — Deep RL reproducibility, variance decomposition
95	- Shavelson & Webb (1991) — G-theory primer (canonical)
96	- Brennan (2001) — G-theory textbook (canonical)
97	- Lu et al. (2022) — Option ordering effects in MC evaluation
98	- Pezeshkpour & Hruschka (2024) — Option ordering effects
99	- Dodge et al. (2020, EMNLP) — Fine-tuning instability (seed, data order)
100	- Sellam et al. (2022) — MultiBERTs, multi-seed training
101	- Dehghani et al. (2021) — Benchmark Lottery
102	- Biderman et al. (2024) — Evaluation reproducibility lessons
103	- Vania et al. (2021) — IRT item properties in NLP
104	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf556517-fcf7-4e00-9ac8-74b6a29c727e",
  "isSidechain": false,
  "promptId": "c5460e05-f609-42c9-9ad5-28993b47482a",
  "type": "user",
  "uuid": "a7eda911-7ae9-4e02-af6b-4e4d53909f6c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median/paper_framing.md",
      "content": "# Paper Framing — nlp_variance_gtheory\n\n## Target Venue\n- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)\n- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)\n- Extended: TACL (rolling)\n\n## Title\nReproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics\n\n## Core Claims (3 条，可证伪)\n\n**Claim 1 — Item Dominance (benchmark-conditional)**: Item selection is the single largest variance source in multiple-choice LLM evaluation, but its magnitude is benchmark-dependent: from ~45% on knowledge-retrieval tasks (MMLU) down to ~25% on reasoning tasks (GSM8K/MATH) where temperature and seed interactions increase. Item dominance is expected from measurement theory when item difficulty varies widely (Brennan, 2001); our contribution is in (a) quantifying the precise magnitude across benchmarks and models, (b) demonstrating the systematic benchmark-dependent gradient, and (c) deriving D-study implications specific to LLM evaluation.\n\n**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), \"infrastructure\" is currently limited to the precision facet.\n\n**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent: binary correct scoring yields G=0.357 (item dominance makes G≥0.90 unreachable without massive item expansion), while text-exact-match scoring yields G=0.975 (already adequate). D-study projections show that increasing item sampling is more cost-effective than increasing prompt/seed replication, but the optimal allocation depends critically on both the evaluation metric and the benchmark. Current common practices (1 prompt, 1 seed, ≤200 items, single metric) produce misleading reliability estimates.\n\n## Contributions (3 条，明确区分)\n\n1. **Cross-benchmark variance gradient**: The first multi-benchmark G-theory analysis showing that variance structure systematically shifts from item-dominated (knowledge retrieval) to interaction-dominated (reasoning tasks), explaining why prior single-benchmark studies reached seemingly contradictory conclusions.\n\n2. **Confirmatory separability test**: Infrastructure×methodology interactions are negligible at the aggregate level (<0.5% under binary scoring), providing empirical support for isolated-factor studies — with the caveat that both factors interact with items and the finding is metric-conditional.\n\n3. **Task-specific reproducibility budgets**: D-study projections with bootstrap CIs yield actionable, benchmark-specific item/prompt/seed allocations for achieving target reliability (G≥0.90), contextualized against IRT-based subsampling approaches (tinyBenchmarks, HELM-Lite).\n\n## Story Spine\n\n**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability.\n\n**Existing approaches & gaps**: Bouthillier et al. (2021) decomposed ML benchmark variance across hyperparameters, data splits, and seeds via ANOVA, establishing the template for factorial variance decomposition in ML evaluation. Mesting (2026) adapted G-theory to 5 methodological facets in LLM evaluation but treated infrastructure as fixed. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance on fixed hardware. IRT-based approaches (Lalor et al. 2019; Rodriguez et al. 2021; Polo et al. 2024) have analyzed item-level properties and efficient subsampling, but from a different methodological perspective than G-theory. No study has: (a) crossed infrastructure and methodology in a unified G-theory framework, (b) compared variance structure across multiple benchmarks, or (c) provided metric-conditional reproducibility budgets.\n\n**Our framing**: We conduct a multi-benchmark G-theory study crossing infrastructure (numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors, with model treated as a crossed facet. The infrastructure crossing yields a confirmatory null result: aggregate separability holds, validating the implicit assumption of prior isolated-factor studies. The primary novel finding is the cross-benchmark variance gradient — item dominance systematically weakens as tasks shift from knowledge retrieval to multi-step reasoning — explaining divergent conclusions in the literature. D-study projections provide the first benchmark-specific, metric-conditional reproducibility budgets for LLM evaluation, directly comparable to IRT-based subsampling approaches.\n\n**Headline result template**: \"In a G-study of K conditions across M models and N benchmarks, item selection is the largest single variance source on multiple-choice benchmarks (25-55%, benchmark-dependent), while direct infrastructure×methodology interactions are negligible (<0.5% binary, ≤1.3% text-match). Variance structure shifts systematically from item-dominated (knowledge benchmarks) to interaction-dominated (reasoning benchmarks). D-study reproducibility budgets show that optimal facet allocation is both benchmark-specific and metric-conditional: MMLU needs more items, GSM8K needs more seeds.\"\n\n## Hook (Counter-Intuitive Quantified Claim)\n\"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks — our G-theory analysis across N benchmarks shows the variance structure itself is benchmark-conditional, rendering any 'universal reproducibility recipe' illusory.\"\n\n## Narrative Strategy\n- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Empirical contribution (benchmark-conditional gradient)\n- **Tension**: \"No universal recipe\" — the field seeks standardization but variance structure varies qualitatively across task types\n- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)\n- **Signature visual**: Stacked-bar variance decomposition chart across benchmarks (field idiom from Mesting/Brittlebench)\n- **Figure plan** (4 figures minimum):\n  1. Problem illustration: same model, different benchmark → different dominant variance source\n  2. G-theory facet diagram showing crossed design\n  3. Stacked-bar variance decomposition across benchmarks (signature figure)\n  4. D-study projection curves: G vs item count for different benchmarks\n- **Key framing shifts from Dream feedback**:\n  - Infrastructure crossing framed as **confirmatory** (validates isolated-factor studies), not as primary novelty\n  - Item dominance acknowledged as **psychometrically expected**; contribution is quantification + benchmark gradient\n  - Cross-benchmark gradient is the **primary novel finding**\n  - \"Fully crossed\" language qualified to MMLU exp-001 only; other benchmarks use reduced designs\n\n## Venue Fit Risks\n- AAAI: Strong fit for \"evaluation methodology\" track. Risk: tight 9-week timeline requires overlapping experiments with writing.\n- Reviewer concern 1: \"Only open-weight models, not API models\" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.\n- Reviewer concern 2: \"G-theory is borrowed methodology, not novel\" — Frame as cross-domain transfer. The novelty is the cross-benchmark variance gradient finding, not G-theory itself.\n- Reviewer concern 3: \"Item dominance is obvious from measurement theory\" — Acknowledge explicitly. Contribution is quantification (25-55%), benchmark-dependence, and D-study implications. Contextualize against IRT item analysis literature.\n\n## Anticipated Reviewer Concerns & Planned Responses\n1. **\"Only N GPU types\"** → exp-003 (multi-hardware crossing) addresses this. If blocked, explicitly scope to \"numerical precision\" and frame hardware as future work.\n2. **\"float32 engine confound\"** → exp-001 fixes with V0 enforce_eager for all precisions. Confound discovery itself is a standalone methodological contribution.\n3. **\"Only MMLU\"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag. Cross-benchmark gradient is the core finding.\n4. **\"Small item sample\"** → exp-001 expands from 50 to 200 items. exp-001b tests resampling stability.\n5. **\"No training-time analysis\"** → exp-006 (fine-tuning G-study with RoBERTa). Explicitly qualify as encoder-only classification; decoder fine-tuning is future work.\n6. **\"Missing scale validation\"** → exp-005 (14B models)\n7. **\"G-theory may not be right framework\"** → Compare with ANOVA and regression decomposition as sensitivity analysis. Cite Bouthillier et al. (2021) as ANOVA-based predecessor; show G-theory adds D-study projections.\n8. **\"Separability claim is metric-dependent\"** → This is precisely the point: reproducibility budgets must be metric-qualified. Replace arbitrary threshold with bootstrap CI on interaction term.\n9. **\"FP32 degradation is already known (Yuan 2025)\"** → Position as supporting finding with novel item-level breakdown. Not an independent claim.\n10. **\"Incremental over Mesting (2026)\"** → Infrastructure crossing is confirmatory (valuable as validation, not breakthrough). Primary novelty: cross-benchmark gradient, task-specific budgets, dual-metric analysis, confound fix. Mesting = single benchmark, no infrastructure; we = multi-benchmark, infrastructure confirmation + benchmark gradient.\n11. **\"Model not treated as G-theory facet\"** → exp-004 includes model-as-facet reanalysis of MMLU data. Report model×item interaction separately from residual.\n12. **\"No CIs on variance components\"** → exp-004 includes bootstrap CIs (1000 resamples) on all variance components in all tables.\n13. **\"Missing related work — IRT, tinyBenchmarks, Bouthillier\"** → Comprehensive bibliography (25+ refs). Position D-study budgets against IRT-based subsampling. Cite Bouthillier et al. as ANOVA predecessor.\n14. **\"Diagnostic tool claim unsubstantiated\"** → Release analysis pipeline code (G-theory variance decomposition + D-study projections) as reusable tool. Or reframe as \"empirical analysis + data release.\"\n15. **\"Fine-tuning uses encoder-only RoBERTa\"** → Explicitly qualify. Decoder fine-tuning is a natural extension requiring substantially more compute.\n\n## Design Decisions\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.\n- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.\n- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as \"reduced crossing\" rather than \"fully crossed.\"\n\n## Required Bibliography (minimum 25 references)\nKey references to include beyond current literature_map:\n- Bouthillier et al. (2021, JMLR) — ML variance decomposition via ANOVA\n- Lalor et al. (2019, NAACL) — IRT-based item analysis in NLP\n- Rodriguez et al. (2021, ACL) — IRT evaluation for NLP\n- Polo et al. (2024) — tinyBenchmarks, IRT-based subsampling\n- Perlitz et al. (2023) — Efficient LLM benchmarking\n- Henderson et al. (2018) — Deep RL reproducibility, variance decomposition\n- Shavelson & Webb (1991) — G-theory primer (canonical)\n- Brennan (2001) — G-theory textbook (canonical)\n- Lu et al. (2022) — Option ordering effects in MC evaluation\n- Pezeshkpour & Hruschka (2024) — Option ordering effects\n- Dodge et al. (2020, EMNLP) — Fine-tuning instability (seed, data order)\n- Sellam et al. (2022) — MultiBERTs, multi-seed training\n- Dehghani et al. (2021) — Benchmark Lottery\n- Biderman et al. (2024) — Evaluation reproducibility lessons\n- Vania et al. (2021) — IRT item properties in NLP\n",
      "numLines": 104,
      "startLine": 1,
      "totalLines": 104
    }
  },
  "sourceToolAssistantUUID": "bf556517-fcf7-4e00-9ac8-74b6a29c727e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T23:19:16.067Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RVcfTmDn3B9qKDzEcYiy1Q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2df83229-fdc6-43a5-a495-16e283858fd4",
  "isSidechain": false,
  "requestId": "req_011CbEgBehkSX4aGpEWWSnk4",
  "type": "assistant",
  "uuid": "bf556517-fcf7-4e00-9ac8-74b6a29c727e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JNUmXNC745qN86wDR1NZ9L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11638,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11638,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11638,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11638
          },
          "type": "message"
        }
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T222113 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheo…",
  "leafUuid": "a7eda911-7ae9-4e02-af6b-4e4d53909f6c",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulation paper for dream_20260520T222113",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff"
}
```

---

### Assistant

_source line 14 · 2026-05-20T23:19:34.894Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me also read the distilled research and writing skills to inform the paper style.

Actually, I have enough context to write the paper. Let me now compose a complete LaTeX paper based on:

1. The experiment data JSON with 7 experiments
2. The paper framing document

Let me organize the paper structure:
- Abstract
- Introduction (4 paragraphs + 3 contributions)
- Related Work
- Method (G-theory background, experimental design)
- Experiments (one section per experiment, with tables)
- Discussion


- Conclusion

I need to weave in the key narrative points: reframing the systematic gradient as benchmark-conditional variance structure, showing how the 2-cluster pattern shifts to 3-tier with MATH, emphasizing that item dominance persists on knowledge tasks, and positioning the FP32 degradation as a known finding with novel item-level breakdown. The model-as-facet absorption on MMLU reframes what prior single-model studies missed, and I should target an AA audience throughout.

Now I'm planning the full paper structure across all seven experimental components—the MMLU precision study, item resampling stability, multi-benchmark replication, combined analysis with bootstrap CIs and D-study, 14B model extension, fine-tuning G-study, LayerCast mitigation, and MATH extension. That's a substantial set of tables, so I need to prioritize the most critical ones for the main narrative while referencing the rest, keeping in mind what the submission guidelines actually require.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7eda911-7ae9-4e02-af6b-4e4d53909f6c",
  "isSidechain": false,
  "requestId": "req_011CbEgCCZfVZdfyGpjXpHH3",
  "type": "assistant",
  "uuid": "17c2fd00-4a24-4264-855f-2dcea46e7188",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQH75rGDwELprYdS8E3bPX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27039,
      "cache_read_input_tokens": 23479,
      "output_tokens": 696,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27039,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 696,
          "cache_read_input_tokens": 23479,
          "cache_creation_input_tokens": 27039,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27039
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-20T23:19:35.053Z_

Now let me check the target directory and pdflatex availability.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17c2fd00-4a24-4264-855f-2dcea46e7188",
  "isSidechain": false,
  "requestId": "req_011CbEgCCZfVZdfyGpjXpHH3",
  "type": "assistant",
  "uuid": "0c1c1a1e-6051-40e2-9df9-f07c68224ac2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQH75rGDwELprYdS8E3bPX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27039,
      "cache_read_input_tokens": 23479,
      "output_tokens": 696,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27039,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 696,
          "cache_read_input_tokens": 23479,
          "cache_creation_input_tokens": 27039,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27039
          },
          "type": "message"
        }
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

_source line 16 · 2026-05-20T23:19:37.391Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0117paREZpEBukPNhx8dgPRb`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median/ && which pdflatex",
  "description": "Check target directory and pdflatex availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c1c1a1e-6051-40e2-9df9-f07c68224ac2",
  "isSidechain": false,
  "requestId": "req_011CbEgCCZfVZdfyGpjXpHH3",
  "type": "assistant",
  "uuid": "9ed1001d-df54-4229-b7d1-3be8dd1fafd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQH75rGDwELprYdS8E3bPX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27039,
      "cache_read_input_tokens": 23479,
      "output_tokens": 696,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27039,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 696,
          "cache_read_input_tokens": 23479,
          "cache_creation_input_tokens": 27039,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27039
          },
          "type": "message"
        }
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

_source line 17 · 2026-05-20T23:19:37.529Z_

<details><summary>↩ Tool result · `toolu_0117paREZpEBukPNhx8dgPRb`</summary>

```text
experiment_data.json
imagined_experiments.yaml
paper_framing.md
/usr/bin/pdflatex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ed1001d-df54-4229-b7d1-3be8dd1fafd0",
  "isSidechain": false,
  "promptId": "c5460e05-f609-42c9-9ad5-28993b47482a",
  "type": "user",
  "uuid": "a36256d5-bfc1-4571-a986-eefdcd675b08",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md\n/usr/bin/pdflatex",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "9ed1001d-df54-4229-b7d1-3be8dd1fafd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-20T23:20:06.917Z_

<details><summary>Logged reasoning block</summary>

```text
Good, the directory exists and pdflatex is available. Now let me write the complete paper.

I need to map each experiment to paper sections:

1. Full-scale MMLU precision study → Section 4.1 (MMLU G-Study)
2. Item resampling stability test → Section 4.2 (Resampling Stability)
3. Multi-benchmark replication → Section 4.3 (Cross-Benchmark Analysis)
4. Multi-hardware G-study → Section 4.4 (Hardware Facet)


5. Comprehensive combined analysis → Section 4.5 (Model-as-Facet Reanalysis, Bootstrap CIs, D-Study)
6. 14B model scale extension → Section 4.6 (Scale Extension)
7. Fine-tuning G-study → Section 4.7 (Fine-Tuning Variance)
8. LayerCast precision mitigation → Section 4.8 or Discussion
9. MATH benchmark extension → Section 4.3 (extend cross-benchmark) or separate section

Let me recount the experiments to make sure I have them all accounted for correctly. I'm recounting the experiments in the JSON structure more carefully. Looking at each entry systematically, I can see there are actually 9 distinct experiments listed, including the LayerCast precision mitigation and MATH benchmark extension at the end.

Now I'm organizing the paper structure to accommodate all nine experiments, grouping related results together—like combining the cross-benchmark variance analysis with the MATH extension, and consolidating the model-as-facet reanalysis under a single results section. I'm consolidating the results sections further to keep the paper compact—combining the D-study reproducibility budgets with fine-tuning and precision work into just a couple of subsections. Now I'm shifting to actually writing the LaTeX document in a conference-style format, using a simple two-column layout rather than strict AAAI formatting, and I'll renumber the experiment tables to maintain a clean sequence throughout the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a36256d5-bfc1-4571-a986-eefdcd675b08",
  "isSidechain": false,
  "requestId": "req_011CbEgDn73o9MLzykrA9hbL",
  "type": "assistant",
  "uuid": "4165d75c-04e9-41f5-8105-82e0ad1de2e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYe4q2AwqQwXKXM5jMJJBX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 735,
      "cache_read_input_tokens": 50518,
      "output_tokens": 1690,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 735,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1690,
          "cache_read_input_tokens": 50518,
          "cache_creation_input_tokens": 735,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 735
          },
          "type": "message"
        }
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

_source line 19 · 2026-05-20T23:20:06.940Z_

Now I'll write the complete paper. This is a substantial document covering all 9 experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4165d75c-04e9-41f5-8105-82e0ad1de2e2",
  "isSidechain": false,
  "requestId": "req_011CbEgDn73o9MLzykrA9hbL",
  "type": "assistant",
  "uuid": "66a676d8-3005-43c6-a5a4-37c7154d4066",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYe4q2AwqQwXKXM5jMJJBX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 735,
      "cache_read_input_tokens": 50518,
      "output_tokens": 1690,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 735,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1690,
          "cache_read_input_tokens": 50518,
          "cache_creation_input_tokens": 735,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 735
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-20T23:20:07.756Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017kq88wbtCqGwfjNWRBGNSK`</summary>

```json
{
  "command": "kpsewhich aaai.sty 2>/dev/null; kpsewhich acmart.cls 2>/dev/null; kpsewhich article.cls",
  "description": "Check available LaTeX document classes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66a676d8-3005-43c6-a5a4-37c7154d4066",
  "isSidechain": false,
  "requestId": "req_011CbEgDn73o9MLzykrA9hbL",
  "type": "assistant",
  "uuid": "a50edbfe-8c43-49d8-a715-7dbf12a95da3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYe4q2AwqQwXKXM5jMJJBX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 735,
      "cache_read_input_tokens": 50518,
      "output_tokens": 1690,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 735,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1690,
          "cache_read_input_tokens": 50518,
          "cache_creation_input_tokens": 735,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 735
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-20T23:20:07.858Z_

<details><summary>↩ Tool result · `toolu_017kq88wbtCqGwfjNWRBGNSK`</summary>

```text
/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a50edbfe-8c43-49d8-a715-7dbf12a95da3",
  "isSidechain": false,
  "promptId": "c5460e05-f609-42c9-9ad5-28993b47482a",
  "type": "user",
  "uuid": "d8de644f-392a-4358-b7fc-4cecdea01e25",
  "toolUseResult": {
    "stdout": "/usr/share/texlive/texmf-dist/tex/latex/base/article.cls",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a50edbfe-8c43-49d8-a715-7dbf12a95da3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-20T23:20:38.474Z_

<details><summary>Logged reasoning block</summary>

```text
No AAAI style available, I'll use article class with appropriate formatting. Let me write the complete paper now.

Let me carefully organize all the data points and write a comprehensive paper. I'll use a compact format.

For tables, I need to cover all 9 experiments. Let me map them:

Experiment 1 (MMLU precision) → Tables 1, 2, 3 in data → Paper Tables 1, 2
Experiment 2 (Resampling) → Tables 4, 5 → Paper Table 3
Experiment 3 (Cross-benchmark) → Tables 6, 7, 8 → Paper Tables 4, 5


Experiment 4 (Hardware) → Tables 9, 10, 11 → Paper Table 6
Experiment 5 (Combined analysis) → Tables 12-16 → Paper Tables 7, 8, 9, 10
Experiment 6 (14B scale) → Tables 17, 18 → Paper Table 11
Experiment 7 (Fine-tuning) → Tables 19, 20 → Paper Table 12
Experiment 8 (LayerCast) → Table 21 → Paper Table 13
Experiment 9 (MATH) → Tables 22, 23 → Paper Table 14

That gives me 14 tables total for the paper.

I should consolidate this down to around 10-12 tables instead. Let me identify the most critical ones to keep: the MMLU binary variance decomposition, per-model accuracy by precision, resampling stability results, the cross-benchmark variance table since that's the signature finding, cross-benchmark summary, hardware facet results, and the model-as-facet analysis across all benchmarks. I can fold some of the other data into the text or combine related tables to reduce the overall count. I'm folding some of the smaller tables into text descriptions and organizing the results section by analysis type. Each section will have a dedicated table showing the key findings, with MATH results integrated into the cross-benchmark analysis rather than kept separate.

I'm reconsidering the table density—for a paper like this, fewer but more comprehensive tables will actually improve clarity and ensure every experiment gets proper coverage. I'll aim for around 12-15 tables total and make sure the narrative softens claims appropriately with benchmark-conditional language throughout.

Now I'm ready to start writing the paper itself, keeping the bibliography references from the framing document in mind.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8de644f-392a-4358-b7fc-4cecdea01e25",
  "isSidechain": false,
  "requestId": "req_011CbEgG24jxzYGNppHAVjWf",
  "type": "assistant",
  "uuid": "cfb693e2-04cc-485b-b442-1f06226827e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EdZGwfDuDV4CepNasuPC8t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1723,
      "cache_read_input_tokens": 51253,
      "output_tokens": 14642,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1723,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14642,
          "cache_read_input_tokens": 51253,
          "cache_creation_input_tokens": 1723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1723
          },
          "type": "message"
        }
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

_source line 23 · 2026-05-20T23:24:52.081Z_

<details open><summary>🔧 Tool call — Write · `toolu_01KBMfpHbDgqp5981enZ9m8c`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median/paper.tex",
  "content": "\\documentclass[11pt,twocolumn]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\usepackage{enumitem}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{caption}\n\n\\setlength{\\columnsep}{0.3in}\n\\captionsetup{font=small}\n\n\\title{Reproducibility Budgets for LLM Evaluation:\\\\A Generalizability Theory Analysis of Variance Sources\\\\Across Benchmarks, Models, and Evaluation Metrics}\n\n\\author{\nAnonymous Authors\n}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nWhen LLM benchmark results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, numerical precision, temperature, or item selection---let alone how these factors interact. We conduct a multi-benchmark Generalizability Theory (G-theory) study crossing infrastructure (numerical precision, hardware) with methodology (prompt template, seed, temperature, answer ordering) and measurement (item selection) facets across five benchmarks (MMLU, ARC-Challenge, GSM8K, HellaSwag, MATH), four 7--9B models, two 14B models, and two GPU architectures, totaling over 3 million evaluation observations. Three findings emerge. First, item selection is the single largest variance source, but its magnitude is benchmark-conditional: 48\\% on knowledge-retrieval tasks (MMLU) versus 28\\% on proof-reasoning tasks (MATH) under model-as-facet analysis, forming a task-type clustering from knowledge-dominated to interaction-dominated variance structures. Second, infrastructure and methodology factors are approximately separable on knowledge benchmarks (infra$\\times$method $<$0.5\\% binary), but this separability breaks down on math-generation benchmarks where precision$\\times$temperature reaches 3\\% under binary scoring. Third, reproducibility budgets are fundamentally metric-dependent: binary scoring yields $G=0.37$ while text-exact-match yields $G=0.97$, and optimal facet allocation differs by benchmark---MMLU requires 420 items for $G\\geq0.90$ versus 240 for HellaSwag. We release variance decomposition tables and D-study projection code to enable task-specific reproducibility planning.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nThe reliability of LLM evaluation has become a first-order concern as benchmark scores drive model selection, funding decisions, and public perception. Recent studies have documented substantial score variation from individual factors: up to 9 percentage points from numerical precision alone \\citep{yuan2025}, 50\\% variance from prompt template choice on fixed hardware \\citep{mizrahi2024}, and significant sensitivity to random seeds and answer ordering \\citep{lu2022,pezeshkpour2024}. Yet each study isolates at most two sources, implicitly assuming that infrastructure factors (precision, hardware) and methodology factors (prompt, seed, temperature) contribute independently. Whether this separability assumption holds---and whether findings from one benchmark generalize to another---remains untested.\n\nGeneralizability Theory (G-theory) provides a principled framework for simultaneously decomposing variance across multiple facets and their interactions \\citep{shavelson1991,brennan2001}. Unlike ANOVA, G-theory distinguishes the universe score from error variance and supports Decision studies (D-studies) that project reliability under alternative resource allocations. \\citet{bouthillier2021} demonstrated the value of factorial variance decomposition for ML benchmarks via ANOVA, and \\citet{mesting2026} adapted G-theory to five methodology facets in LLM evaluation. However, neither study crossed infrastructure with methodology in a unified design, and both analyzed a single benchmark---leaving the question of cross-benchmark generalization unanswered.\n\nWe conduct the first multi-benchmark G-theory analysis of LLM evaluation variance, crossing infrastructure (numerical precision across two GPU architectures) with methodology (prompt template, seed, temperature, answer ordering) and measurement (item selection) facets. Our design spans five benchmarks (MMLU, ARC-Challenge, GSM8K, HellaSwag, MATH), four 7--9B models with model treated as a crossed random facet, and over 3 million total observations. The key insight is that \\emph{the variance structure itself depends on what you are benchmarking}: knowledge-retrieval benchmarks exhibit high item dominance with negligible cross-factor interaction, while reasoning benchmarks show reduced item dominance with detectable infrastructure$\\times$methodology coupling. This benchmark-conditional structure renders any ``universal reproducibility recipe'' illusory.\n\nOur contributions are: (1) a cross-benchmark variance gradient showing that item dominance shifts from 48\\% (knowledge) to 28\\% (proof reasoning) under model-as-facet analysis, with a three-tier task-type clustering; (2) a confirmatory separability test showing infrastructure$\\times$methodology interactions $<$0.5\\% on knowledge benchmarks but reaching 3\\% on math-generation benchmarks; and (3) task-specific reproducibility budgets via D-study projections with bootstrap confidence intervals, showing that optimal facet allocation is both benchmark-specific and metric-conditional.\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Variance sources in LLM evaluation.}\n\\citet{yuan2025} documented up to 9\\% accuracy variation from hardware and numerical precision without factorial attribution. \\citet{mizrahi2024} (Brittlebench) quantified prompt sensitivity at approximately 50\\% of evaluation variance on fixed hardware. \\citet{lu2022} and \\citet{pezeshkpour2024} demonstrated significant option-ordering effects in multiple-choice evaluation. \\citet{biderman2024} summarized reproducibility lessons across evaluation frameworks. These studies isolate individual factors; our work crosses them in a unified factorial design.\n\n\\paragraph{Generalizability Theory in NLP.}\nG-theory \\citep{shavelson1991,brennan2001} has been applied extensively in educational and psychological measurement. \\citet{bouthillier2021} adapted ANOVA-based variance decomposition to ML benchmarks, decomposing variance across hyperparameters, data splits, and seeds. \\citet{mesting2026} applied G-theory to LLM evaluation with five methodology facets but treated infrastructure as fixed and analyzed only MMLU. Our work extends this to infrastructure$\\times$methodology crossing across multiple benchmarks.\n\n\\paragraph{Item-level analysis and efficient benchmarking.}\nItem Response Theory (IRT) provides a complementary perspective on item properties \\citep{lalor2019,rodriguez2021,vania2021}. \\citet{polo2024} used IRT for efficient subsampling (tinyBenchmarks), and \\citet{perlitz2023} developed HELM-Lite for efficient benchmarking. Our D-study projections offer a G-theory-based alternative to IRT subsampling, with the advantage of jointly optimizing across multiple facets.\n\n\\paragraph{Training instability and reproducibility.}\n\\citet{dodge2020} documented fine-tuning instability from seeds and data order. \\citet{sellam2022} (MultiBERTs) trained multiple BERT copies to quantify training variance. \\citet{henderson2018} highlighted variance in deep RL evaluation. \\citet{dehghani2021} (Benchmark Lottery) showed that model ranking depends on benchmark selection. Our fine-tuning G-study (Section~\\ref{sec:finetuning}) extends this line by decomposing fine-tuning variance with G-theory.\n\n% ============================================================\n% 3. FRAMEWORK AND METHOD\n% ============================================================\n\\section{Framework and Method}\n\n\\subsection{Generalizability Theory}\n\nIn G-theory, the observed score for person $p$ (here: item $i$) under condition $c$ is decomposed as:\n\\begin{equation}\nX_{ic} = \\mu + \\alpha_i + \\beta_c + (\\alpha\\beta)_{ic} + \\epsilon_{ic}\n\\end{equation}\nwhere $\\alpha_i$ captures item difficulty, $\\beta_c$ captures condition effects (prompt, seed, temperature, precision, ordering), $(\\alpha\\beta)_{ic}$ captures item$\\times$condition interactions, and $\\epsilon_{ic}$ is residual error. G-theory estimates variance components $\\hat{\\sigma}^2$ for each source, which partition total variance. The \\emph{generalizability coefficient} $G$ quantifies the reliability of the benchmark score as a function of the number of items and conditions:\n\\begin{equation}\nG = \\frac{\\hat{\\sigma}^2_i}{\\hat{\\sigma}^2_i + \\sum_c \\hat{\\sigma}^2_{ic}/n_c + \\hat{\\sigma}^2_\\epsilon / (n_c \\cdot n_i)}\n\\end{equation}\n\nA \\emph{Decision study} (D-study) projects $G$ under hypothetical resource allocations (e.g., more items, fewer prompts), enabling cost-effective evaluation design.\n\n\\subsection{Experimental Design}\n\nWe conduct a series of G-studies with increasing scope:\n\n\\paragraph{Experiment 1: Full-scale MMLU G-study.} 4 models $\\times$ 3 precisions (FP32, BF16, FP16; all vLLM V0 enforce\\_eager) $\\times$ 6 prompt templates $\\times$ 6 seeds $\\times$ 3 temperatures $\\times$ 4 answer orderings $\\times$ 200 MMLU items (stratified across 57 subjects). Total: 1,036,800 observations across 5,184 conditions. The V0 enforce\\_eager configuration eliminates a previously identified engine confound where BF16 defaults to a different execution path.\n\n\\paragraph{Experiment 2: Item resampling stability.} Three independent stratified samples of 200 MMLU items (seeds 0, 7, 99) $\\times$ Llama-3.1-8B $\\times$ reduced crossing (3 precisions $\\times$ 3 prompts $\\times$ 3 seeds $\\times$ 2 orderings). 32,400 observations per sample.\n\n\\paragraph{Experiment 3: Multi-benchmark replication.} GSM8K, ARC-Challenge, and HellaSwag with 4 models $\\times$ 2 precisions (BF16, FP16) $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 2 temperatures $\\times$ 4 orderings $\\times$ 200 items. 384,000 observations per benchmark (reduced crossing vs.\\ Experiment 1).\n\n\\paragraph{Experiment 4: Multi-hardware G-study.} 4 models $\\times$ 2 GPU types $\\times$ 2 precisions $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 3 temperatures $\\times$ 4 orderings $\\times$ 200 MMLU items. 1,152,000 observations.\n\n\\paragraph{Experiment 5: Combined analysis.} Reanalysis of all preceding data with: (a) model treated as a crossed random facet; (b) bootstrap confidence intervals (1,000 resamples); (c) D-study projections; (d) REML vs.\\ Henderson Method I comparison; (e) log-probability scoring; (f) ranking stability analysis.\n\n\\paragraph{Experiment 6: 14B scale extension.} Qwen3-14B and DeepSeek-R1-Distill-14B at BF16/FP16 $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 2 temperatures $\\times$ 4 orderings $\\times$ 200 MMLU items.\n\n\\paragraph{Experiment 7: Fine-tuning G-study.} RoBERTa-large fine-tuned on SST-2, MNLI, RTE, and COPA with 6 seeds $\\times$ 3 learning rates $\\times$ 4 data shuffles $\\times$ 3 GPUs $\\times$ 2 precisions = 432 runs per task, 1,728 total.\n\n\\paragraph{Experiment 8: LayerCast mitigation.} LayerCast (FP16 storage + FP32 compute) as an additional precision condition on MMLU with the same 4 models and full facet crossing.\n\n\\paragraph{Experiment 9: MATH extension.} 200 MATH items $\\times$ 4 models $\\times$ 2 precisions $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 2 temperatures $\\times$ 4 orderings.\n\n\\subsection{Models and Infrastructure}\n\nWe use four 7--9B instruction-tuned models: Qwen3-8B-Instruct, Llama-3.1-8B-Instruct, Gemma-2-9B-IT, and Mistral-7B-v0.3. Scale extension uses Qwen3-14B and DeepSeek-R1-Distill-14B. All inference uses vLLM 0.9.2 with default settings (without batch-invariant kernels) to reflect realistic practitioner conditions. Variance components are estimated via Henderson Method I with REML sensitivity checks.\n\n\\subsection{Scoring Metrics}\n\nWe employ three scoring metrics: \\emph{binary correct} (1 if the extracted answer matches the gold label), \\emph{text exact match} (1 if the full generated text exactly matches a reference), and \\emph{log-probability} (continuous log-prob of the correct option). Each metric captures different variance structure.\n\n% ============================================================\n% 4. RESULTS\n% ============================================================\n\\section{Results}\n\n\\subsection{MMLU Variance Decomposition}\n\\label{sec:mmlu}\n\nTable~\\ref{tab:mmlu_binary} presents the variance decomposition for MMLU under binary correct scoring with models pooled. Item selection dominates at 52.0\\% of total variance, consistent with the psychometric expectation that item difficulty is the primary driver when difficulty varies widely \\citep{brennan2001}. The next-largest sources are all item interactions: prompt$\\times$item (5.8\\%), temperature$\\times$item (5.5\\%), and precision$\\times$item (5.0\\%). Infrastructure$\\times$methodology interactions (all direct cross-factor terms) total only 0.4\\%, supporting approximate separability at the aggregate level.\n\n\\begin{table}[t]\n\\centering\n\\caption{MMLU variance decomposition (binary correct, model pooled, $N$=1,036,800).}\n\\label{tab:mmlu_binary}\n\\small\n\\begin{tabular}{@{}lr@{}}\n\\toprule\nSource & \\% Variance \\\\\n\\midrule\nitem\\_id & 52.0 \\\\\nresidual (incl.\\ model) & 14.0 \\\\\nprompt$\\times$item & 5.8 \\\\\ntemperature$\\times$item & 5.5 \\\\\nprecision$\\times$item & 5.0 \\\\\nprecision (main) & 3.0 \\\\\nseed$\\times$item & 2.8 \\\\\ntemperature (main) & 1.5 \\\\\nprompt (main) & 0.8 \\\\\ninfra$\\times$method (all) & 0.4 \\\\\nordering & 0.2 \\\\\nother 2-way/3-way & 9.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder text-exact-match scoring, the variance structure shifts qualitatively: prompt$\\times$item rises to 33.0\\%, residual accounts for 36.0\\%, and item\\_id drops to 3.0\\%. The generalizability coefficient reflects this: $G=0.37$ under binary scoring versus $G=0.97$ under text-match. This metric dependence is a central finding.\n\n\\paragraph{FP32 degradation.} Table~\\ref{tab:precision_accuracy} shows that FP32 inference degrades accuracy by 2.9 percentage points (pp) on average relative to BF16, with strong model dependence (1.5--7.2pp). This effect persists under V0 enforce\\_eager, confirming it is a genuine precision artifact rather than an engine confound, consistent with \\citet{yuan2025}. The novel contribution is the item-level breakdown: precision$\\times$item (5.0\\%) exceeds the precision main effect (3.0\\%), indicating that items near decision boundaries are disproportionately affected.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-model MMLU accuracy by precision (V0 enforce\\_eager). All models show FP32 degradation.}\n\\label{tab:precision_accuracy}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & FP32 & BF16 & FP16 & Gap \\\\\n\\midrule\nQwen3-8B & .695 & .710 & .706 & 1.5pp \\\\\nLlama-3.1-8B & .600 & .672 & .669 & 7.2pp \\\\\nGemma-2-9B & .638 & .660 & .658 & 2.2pp \\\\\nMistral-7B & .688 & .694 & .691 & 0.6pp \\\\\n\\midrule\nAverage & .655 & .684 & .681 & 2.9pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Item Resampling Stability}\n\\label{sec:resampling}\n\nA single draw of 200 items from MMLU's 14,042 items introduces meaningful sampling uncertainty. Table~\\ref{tab:resampling} shows variance components across three independent stratified draws. Item dominance ranges from 44\\% to 55\\% (CV=0.19), and the G-coefficient varies from 0.32 to 0.39. Crucially, the \\emph{rank ordering} of variance sources is preserved across all draws (item\\_id always ranks first), but point estimates of magnitude are unstable. This explains why prior studies using different item sets reached different headline numbers.\n\n\\begin{table}[t]\n\\centering\n\\caption{Resampling stability of key variance components across three independent 200-item stratified MMLU samples (Llama-3.1-8B).}\n\\label{tab:resampling}\n\\small\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nSource & S0 & S7 & S99 & Mean & CV \\\\\n\\midrule\nitem\\_id & 49.0 & 55.0 & 44.0 & 49.3 & .19 \\\\\nresidual & 17.5 & 15.0 & 19.5 & 17.3 & .11 \\\\\nprompt:item & 6.5 & 6.0 & 7.0 & 6.5 & .09 \\\\\ntemp:item & 5.8 & 5.2 & 6.5 & 5.8 & .10 \\\\\nprec:item & 5.0 & 5.5 & 4.2 & 4.9 & .12 \\\\\nprecision & 3.0 & 3.5 & 2.8 & 3.1 & .10 \\\\\n\\midrule\n$G$ (binary) & .36 & .32 & .39 & .36 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Benchmark Variance Structure}\n\\label{sec:crossbenchmark}\n\nTable~\\ref{tab:crossbench} presents the variance decomposition across all five benchmarks under binary scoring with models pooled. The data reveal a task-type clustering rather than a clean monotonic gradient. Knowledge-retrieval benchmarks (MMLU, ARC) show high item dominance (50--52\\%), while reasoning benchmarks show progressively lower item dominance: GSM8K (40\\%), HellaSwag (35\\%), and MATH (32\\%). The 20pp spread across benchmarks is statistically significant (permutation $p=0.003$) but the endpoints' bootstrap CIs overlap partially (Section~\\ref{sec:modelasfacet}), requiring directional rather than magnitude claims.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-benchmark variance decomposition (binary correct, model pooled). Benchmarks sorted by item dominance. 384,000 obs/benchmark (GSM8K, ARC, HellaSwag); 1,036,800 (MMLU).}\n\\label{tab:crossbench}\n\\small\n\\begin{tabular}{@{}lrrrrr@{}}\n\\toprule\nSource & MMLU & ARC & GSM & Hella & MATH \\\\\n\\midrule\nitem\\_id & 52.0 & 50.0 & 40.0 & 35.0 & 32.0 \\\\\nresidual & 14.0 & 12.0 & 15.0 & 18.0 & 17.0 \\\\\ntemp:item & 5.5 & 5.5 & 10.0 & 9.5 & 14.0 \\\\\nseed:item & 2.8 & 4.0 & 7.0 & 8.5 & 11.0 \\\\\nprompt:item & 5.8 & 8.5 & 6.5 & 7.5 & 8.0 \\\\\nprec:item & 5.0 & 2.5 & 1.5 & 1.5 & 1.5 \\\\\nprecision & 3.0 & 1.0 & 1.0 & 0.5 & 0.5 \\\\\ntemperature & 1.5 & 2.5 & 4.0 & 4.5 & 6.0 \\\\\ninfra$\\times$meth & 0.4 & 0.5 & 3.0 & 0.3 & 2.5 \\\\\nother & 10.0 & 13.5 & 12.0 & 14.7 & 7.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe critical finding for separability is benchmark-conditional: on knowledge benchmarks (MMLU, ARC), infra$\\times$method totals $<$0.5\\%, but on GSM8K it reaches 3.0\\% (precision$\\times$temperature 2.2\\% + precision$\\times$seed 0.5\\% + precision$\\times$prompt 0.3\\%). Table~\\ref{tab:gsm8k_infra} breaks down the GSM8K interaction. Under text-match scoring, GSM8K infra$\\times$method reaches 3.5\\%. This benchmark-specific departure means that separability claims require qualification: ``on knowledge-retrieval benchmarks'' or ``excluding math-generation tasks.''\n\n\\begin{table}[t]\n\\centering\n\\caption{GSM8K infra$\\times$method interaction breakdown (binary). Only GSM8K and MATH exceed 1\\%; MMLU 0.4\\%, ARC 0.5\\%, HellaSwag 0.3\\%.}\n\\label{tab:gsm8k_infra}\n\\small\n\\begin{tabular}{@{}lr@{}}\n\\toprule\nInteraction & \\% Variance \\\\\n\\midrule\nprecision$\\times$temperature & 2.2 \\\\\nprecision$\\times$seed & 0.5 \\\\\nprecision$\\times$prompt & 0.3 \\\\\n\\midrule\nTotal infra$\\times$method & 3.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWith MATH included, the pattern extends from a two-cluster to a three-tier structure: \\{MMLU 52\\%, ARC 50\\%\\} $>$ \\{GSM8K 40\\%, HellaSwag 35\\%\\} $\\geq$ \\{MATH 32\\%\\}. MATH exhibits the highest temperature$\\times$item (14\\%) and seed$\\times$item (11\\%) among all benchmarks, consistent with the multi-step proof reasoning that introduces maximal chain-of-thought variance.\n\n\\subsection{Model-as-Facet Reanalysis}\n\\label{sec:modelasfacet}\n\nTable~\\ref{tab:model_facet} presents the reanalysis with model treated as a crossed random facet. This absorbs model$\\times$item interaction---previously conflated with item\\_id and residual---into an explicit component. On MMLU, model$\\times$item accounts for 21\\% of total variance, reducing item\\_id from 52\\% to 48\\% and residual from 14\\% to 8\\%. The 4pp reduction is consistent across all benchmarks, suggesting that prior single-model studies systematically overestimated pure item dominance.\n\n\\begin{table}[t]\n\\centering\n\\caption{Model-as-facet variance decomposition (binary correct) across five benchmarks. Model$\\times$item captures model-specific item difficulty profiles.}\n\\label{tab:model_facet}\n\\small\n\\begin{tabular}{@{}lrrrrr@{}}\n\\toprule\nSource & MMLU & ARC & GSM & Hella & MATH \\\\\n\\midrule\nitem\\_id & 48.0 & 46.0 & 36.0 & 31.0 & 28.0 \\\\\nmodel$\\times$item & 21.0 & 16.0 & 18.0 & 19.0 & 22.0 \\\\\nmodel (main) & 5.0 & 4.0 & 4.0 & 5.0 & 6.0 \\\\\nresidual & 8.0 & 8.0 & 10.0 & 10.0 & 7.0 \\\\\ntemp:item & 4.8 & 5.0 & 9.0 & 8.5 & 14.0 \\\\\nseed:item & 2.0 & 3.0 & 5.5 & 7.0 & 11.0 \\\\\nprompt:item & 5.3 & 7.5 & 5.5 & 6.5 & 6.5 \\\\\nprec:item & 2.8 & 2.0 & 1.2 & 1.2 & --- \\\\\nprecision & 2.5 & 0.8 & 0.8 & 0.3 & --- \\\\\ntemperature & 1.2 & 2.2 & 3.5 & 4.0 & 4.5 \\\\\ninfra$\\times$meth & 0.4 & 0.5 & 3.0 & 0.3 & 2.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe benchmark-conditional structure persists after model-as-facet correction, with a 20pp spread from MMLU (48\\%) to MATH (28\\%). The three-tier clustering is preserved: knowledge benchmarks (\\{MMLU, ARC\\}: 46--48\\%), arithmetic/commonsense reasoning (\\{GSM8K, HellaSwag\\}: 31--36\\%), and proof reasoning (\\{MATH\\}: 28\\%).\n\n\\paragraph{Bootstrap confidence intervals.} Table~\\ref{tab:bootstrap_ci} reports 95\\% bootstrap CIs (1,000 item$\\times$condition resamples) on key variance components. The item\\_id CIs are wide (width $\\approx$0.14), reflecting both item-sampling instability (Section~\\ref{sec:resampling}) and condition-resampling uncertainty. The gradient direction is statistically significant ($p=0.003$): MMLU item\\_id $[0.41, 0.55]$ vs.\\ HellaSwag $[0.24, 0.38]$, with partial overlap only at the margins ($[0.38, 0.41]$). GSM8K infra$\\times$method CI $[0.012, 0.048]$ excludes zero, confirming a statistically robust departure from separability.\n\n\\begin{table}[t]\n\\centering\n\\caption{Bootstrap 95\\% CIs on key variance components (model-as-facet, 1,000 resamples).}\n\\label{tab:bootstrap_ci}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n & MMLU & GSM & ARC & Hella \\\\\n\\midrule\nitem & [.41,.55] & [.29,.43] & [.39,.53] & [.24,.38] \\\\\nm$\\times$i & [.16,.27] & [.13,.24] & [.11,.22] & [.14,.25] \\\\\ninf$\\times$m & [.00,.01] & [.01,.05] & [.00,.01] & [.00,.01] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Hardware Facet Analysis}\n\\label{sec:hardware}\n\nTable~\\ref{tab:hardware} presents variance components from the multi-hardware G-study on MMLU. Total hardware-related variance is 3.6\\% under binary scoring and 7.5\\% under text-match. The largest component is hardware$\\times$item (1.8\\% binary), indicating that items near decision boundaries are sensitive to GPU-specific kernel scheduling differences.\n\n\\begin{table}[t]\n\\centering\n\\caption{Hardware facet variance components (MMLU, 1,152,000 obs, 2 GPU types).}\n\\label{tab:hardware}\n\\small\n\\begin{tabular}{@{}lrr@{}}\n\\toprule\nSource & Binary \\% & Text \\% \\\\\n\\midrule\nhardware (main) & 0.4 & 1.2 \\\\\nhardware$\\times$precision & 0.8 & 2.2 \\\\\nhardware$\\times$temperature & 0.3 & 0.6 \\\\\nhardware$\\times$seed & 0.2 & 0.4 \\\\\nhardware$\\times$prompt & 0.1 & 0.3 \\\\\nhardware$\\times$item & 1.8 & 2.8 \\\\\n\\midrule\nTotal hardware & 3.6 & 7.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHardware sensitivity is precision-conditional: when restricted to FP16 data, hardware explains 2.2\\% of variance with cross-GPU accuracy gaps up to 1.1pp. Under BF16, hardware accounts for only 0.3\\% with gaps $\\leq$0.2pp. This asymmetry arises because FP16's narrower dynamic range (5-bit exponent) makes accumulation order hardware-dependent. Model rankings are fully preserved across GPUs---hardware effects are too small to alter comparative model evaluation. Practical recommendation: use BF16 for hardware-independent reproducibility.\n\n\\subsection{D-Study Reproducibility Budgets}\n\\label{sec:dstudy}\n\nTable~\\ref{tab:dstudy} presents D-study projections for the number of items needed to achieve target generalizability coefficients, assuming BF16 precision and optimal prompt/seed allocation. The projections differentiate benchmarks: MMLU requires 420 items for $G\\geq0.90$ versus 240 for HellaSwag (ratio 1.75$\\times$). The practical implication is that knowledge-retrieval benchmarks need 50--75\\% more items than reasoning benchmarks to achieve equivalent reliability, because higher item dominance requires more items to stabilize the universe score estimate.\n\n\\begin{table}[t]\n\\centering\n\\caption{D-study projections: items needed for target $G$ (BF16, optimal prompt/seed). CIs from bootstrap.}\n\\label{tab:dstudy}\n\\small\n\\begin{tabular}{@{}lrrccc@{}}\n\\toprule\nBench & $G$\\scriptsize{$\\geq$.80} & $G$\\scriptsize{$\\geq$.90} & CI\\scriptsize{$_{.90}$} & $G$\\scriptsize{$\\geq$.95} & P/S \\\\\n\\midrule\nMMLU & 220 & 420 & [350,510] & 680 & 3/4 \\\\\nARC & 200 & 380 & [310,470] & 620 & 3/4 \\\\\nGSM8K & 150 & 280 & [220,360] & 450 & 4/6 \\\\\nHella & 130 & 240 & [190,310] & 400 & 4/6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nD-study CIs on the $G\\geq0.90$ threshold span $\\pm$80 items (MMLU: $[350, 510]$), reflecting uncertainty that practitioners should acknowledge when setting evaluation budgets. GSM8K and HellaSwag require more prompts (4 vs.\\ 3) and seeds (6 vs.\\ 4) due to their higher interaction variance.\n\n\\subsection{Scoring Metric Sensitivity}\n\\label{sec:metrics}\n\nTable~\\ref{tab:scoring} demonstrates that the variance hierarchy is fundamentally metric-dependent. Under binary scoring, item\\_id dominates (48\\%); under text-match, prompt$\\times$item (33\\%) and residual (36\\%) dominate while item\\_id drops to 3\\%. Log-probability scoring amplifies item dominance to 55\\% because continuous log-probs capture fine-grained difficulty more sensitively than binary 0/1. The $G$-coefficient ranges from 0.32 (logprob) to 0.97 (text-match)---a practitioner choosing text-match scoring would conclude the benchmark is already reliable, while binary scoring reveals substantial unreliability.\n\n\\begin{table}[t]\n\\centering\n\\caption{Scoring metric comparison (MMLU, model-as-facet). Variance hierarchy depends qualitatively on the evaluation metric.}\n\\label{tab:scoring}\n\\small\n\\begin{tabular}{@{}lrrr@{}}\n\\toprule\nSource & Binary & Text & Logprob \\\\\n\\midrule\nitem\\_id & 48.0 & 3.0 & 55.0 \\\\\nmodel$\\times$item & 21.0 & 1.5 & 18.0 \\\\\nprompt:item & 5.3 & 33.0 & 4.0 \\\\\nresidual & 8.0 & 36.0 & 6.0 \\\\\n\\midrule\n$G$ & 0.37 & 0.97 & 0.32 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Estimation Method Sensitivity}\n\nREML and Henderson Method I estimates agree to within 2.1pp on all variance components (Table~\\ref{tab:reml}). Rank ordering is fully preserved. This methodological choice does not affect qualitative conclusions.\n\n\\begin{table}[t]\n\\centering\n\\caption{REML vs.\\ Henderson Method I (MMLU, binary).}\n\\label{tab:reml}\n\\small\n\\begin{tabular}{@{}lrrr@{}}\n\\toprule\nSource & Henderson & REML & $\\Delta$ \\\\\n\\midrule\nitem\\_id & 48.0\\% & 49.2\\% & +1.2 \\\\\nmodel$\\times$item & 21.0\\% & 22.4\\% & +1.4 \\\\\nresidual & 8.0\\% & 6.1\\% & $-$1.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{14B Scale Extension}\n\\label{sec:scale}\n\nTable~\\ref{tab:scale} compares variance decomposition at 8B (4 models) and 14B (2 models: Qwen3-14B, DeepSeek-R1-Distill-14B) on MMLU. Item dominance decreases by 4pp (48\\%$\\to$44\\%) as higher capacity reduces floor effects. Model$\\times$item increases by 4pp (21\\%$\\to$25\\%) because the dense-versus-reasoning-distilled architecture difference creates larger model-specific item profiles: DeepSeek-R1-Distill-14B excels on multi-step reasoning items while Qwen3-14B excels on factual knowledge items.\n\n\\begin{table}[t]\n\\centering\n\\caption{8B vs.\\ 14B variance decomposition (MMLU, model-as-facet, binary).}\n\\label{tab:scale}\n\\small\n\\begin{tabular}{@{}lrrc@{}}\n\\toprule\nSource & 8B & 14B & $\\Delta$ \\\\\n\\midrule\nitem\\_id & 48.0 & 44.0 & $-$4.0 \\\\\nmodel$\\times$item & 21.0 & 25.0 & +4.0 \\\\\nmodel (main) & 5.0 & 7.0 & +2.0 \\\\\nresidual & 8.0 & 6.0 & $-$2.0 \\\\\ntemp:item & 4.8 & 6.0 & +1.2 \\\\\nprompt:item & 5.3 & 4.5 & $-$0.8 \\\\\nprecision & 2.5 & 0.3 & $-$2.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDeepSeek-R1-Distill-14B shows elevated temperature$\\times$item interaction (8.5\\% vs.\\ 4.2\\% for Qwen3-14B) because reasoning-distilled models produce chain-of-thought that branches more at sampling time. The variance hierarchy is qualitatively preserved at 14B (item\\_id $>$ model$\\times$item $>$ residual), suggesting that the framework's findings are not an artifact of a narrow model-size range.\n\n\\subsection{Fine-Tuning Variance Decomposition}\n\\label{sec:finetuning}\n\nTable~\\ref{tab:finetune} presents variance decomposition for RoBERTa-large fine-tuning across four classification tasks. The variance hierarchy is qualitatively different from inference: hyperparameters dominate instead of items. On large datasets (SST-2, MNLI), learning rate is the primary source (30--35\\%). On small datasets (RTE, COPA), data shuffle dominates (28--30\\%) because mini-batch composition has outsized influence with fewer training examples.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fine-tuning variance decomposition (RoBERTa-large, 432 runs/task).}\n\\label{tab:finetune}\n\\small\n\\begin{tabular}{@{}lrrrr@{}}\n\\toprule\nSource & SST-2 & MNLI & RTE & COPA \\\\\n\\midrule\nlearning\\_rate & 35.0 & 30.0 & 20.0 & 18.0 \\\\\nseed & 25.0 & 22.0 & 16.0 & 20.0 \\\\\ndata\\_shuffle & 12.0 & 15.0 & 28.0 & 30.0 \\\\\nseed$\\times$lr & 10.0 & 12.0 & 16.0 & 14.0 \\\\\ngpu & 0.3 & 0.4 & 0.5 & 0.4 \\\\\nprecision & 0.8 & 0.9 & 1.0 & 1.2 \\\\\nresidual & 16.9 & 19.7 & 18.5 & 16.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nInfrastructure effects (GPU + precision) remain $<$1.5\\% across all tasks, consistent with the inference experiments. The seed$\\times$lr interaction (10--16\\%) is the fine-tuning analogue of item$\\times$temperature in inference: certain seed-LR combinations land in qualitatively different loss basins, producing bimodal accuracy distributions on RTE. This parallel---methodology interactions dominate, infrastructure is negligible---validates the G-theory framework's generality while confirming that reproducibility budgets cannot transfer between evaluation modes.\n\n\\subsection{Precision Mitigation: LayerCast}\n\\label{sec:layercast}\n\nTable~\\ref{tab:layercast} evaluates LayerCast (FP16 storage + FP32 compute) as a precision mitigation strategy. LayerCast reduces precision$\\times$item interaction by $\\sim$40\\% relative to FP16 and achieves accuracy (0.682) essentially equivalent to BF16 (0.684). However, the practical benefit is marginal: precision effects are already small post-confound analysis (precision main 2.5\\% of total), and the 18\\% inference overhead makes LayerCast cost-ineffective relative to simply using BF16.\n\n\\begin{table}[t]\n\\centering\n\\caption{LayerCast comparison across precision modes (MMLU, binary).}\n\\label{tab:layercast}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nMetric & FP32 & BF16 & FP16 & LC \\\\\n\\midrule\nAccuracy & .655 & .684 & .681 & .682 \\\\\nitem\\_id \\% & 50.5 & 52.0 & 51.8 & 51.5 \\\\\nprec:item \\% & 5.8 & 4.5 & 5.0 & 3.0 \\\\\np$\\times$t (binary) & 0.3 & 0.1 & 0.2 & 0.1 \\\\\np$\\times$t (text) & 2.5 & 1.8 & 2.2 & 0.8 \\\\\n$G$ (binary) & .36 & .37 & .37 & .37 \\\\\nCost (rel.) & 1.35 & 1.00 & 1.00 & 1.18 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Five-Benchmark Summary}\n\nTable~\\ref{tab:summary} synthesizes the benchmark-conditional findings under model-as-facet analysis. The three-tier structure tracks cognitive demand: knowledge benchmarks exhibit high item dominance with negligible infra$\\times$method coupling, while reasoning benchmarks show redistributed variance toward temperature and seed interactions, with math-generation benchmarks additionally showing detectable infrastructure$\\times$methodology interaction.\n\n\\begin{table}[t]\n\\centering\n\\caption{Five-benchmark summary (model-as-facet, binary).}\n\\label{tab:summary}\n\\small\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nBench & Type & $i$ \\% & $G$ & i$\\times$m & Tier \\\\\n\\midrule\nMMLU & Know. & 48 & .37 & 0.4 & High \\\\\nARC & Know. & 46 & .35 & 0.5 & High \\\\\nGSM8K & Arith. & 36 & .42 & 3.0 & Mid \\\\\nHella & C.sense & 31 & .48 & 0.3 & Mid \\\\\nMATH & Proof & 28 & .52 & 2.5 & Low \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n% 5. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{The variance structure is benchmark-conditional.}\nOur central finding is that no single variance decomposition characterizes ``LLM evaluation.'' Knowledge-retrieval benchmarks (MMLU, ARC) are item-dominated with separable infrastructure and methodology effects, while reasoning benchmarks (GSM8K, MATH) show reduced item dominance, elevated sampling interactions, and detectable infrastructure$\\times$methodology coupling. This benchmark-conditional structure explains why prior studies---each analyzing a single benchmark---reached seemingly contradictory conclusions about which factors matter most.\n\n\\paragraph{Model-as-facet reframes prior work.}\nTreating model as a crossed random facet reveals that 16--22\\% of total variance is model$\\times$item interaction: items that are hard for one model architecture may be easy for another. Prior single-model studies attributed this variance to item difficulty, inflating item dominance by approximately 4pp. This correction applies systematically across benchmarks and should be standard practice in G-theory analyses of LLM evaluation.\n\n\\paragraph{Separability requires qualification.}\nOn knowledge benchmarks, infrastructure$\\times$methodology interactions are negligible ($<$0.5\\% binary), validating the implicit assumption of prior isolated-factor studies. On math-generation benchmarks, precision$\\times$temperature reaches 2--3\\%, driven by floating-point non-associativity in long chain-of-thought generation. Practitioners evaluating on math-reasoning benchmarks should fix both precision and temperature to avoid confounding.\n\n\\paragraph{Hardware is manageable.}\nTotal hardware-related variance is 3.6\\% (binary), predominantly from hardware$\\times$item (1.8\\%)---the same items sensitive to precision changes are also hardware-sensitive, suggesting a shared mechanism of logit perturbation near decision boundaries. BF16 reduces hardware sensitivity to 0.3\\%, providing a practical path to hardware-independent evaluation. Model rankings are preserved across GPUs.\n\n\\paragraph{Metric dependence as a feature.}\nThe dramatic shift in variance structure between binary ($G=0.37$) and text-match ($G=0.97$) scoring is not a methodological weakness but an important empirical result: the choice of evaluation metric determines which variance sources are visible. Text-match scoring inflates apparent reliability by averaging over generation-level variation that binary scoring correctly captures.\n\n\\paragraph{Limitations.}\nOur infrastructure facet is limited to numerical precision and two GPU architectures; quantization, batching strategies, and API-based inference are not covered. The model sample spans 7--14B open-weight models; API models with opaque infrastructure and models at 70B+ scale may exhibit different variance structures. The fine-tuning analysis uses encoder-only RoBERTa; decoder fine-tuning introduces generation-related variance sources. Item samples of 200 per benchmark leave meaningful sampling uncertainty (CV$\\approx$0.19).\n\n% ============================================================\n% 6. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe presented the first multi-benchmark Generalizability Theory analysis of LLM evaluation, crossing infrastructure, methodology, and measurement facets across five benchmarks, six model architectures, and two GPU types. The variance structure is benchmark-conditional: item dominance ranges from 48\\% (knowledge retrieval) to 28\\% (proof reasoning), and infrastructure$\\times$methodology separability holds on knowledge benchmarks but breaks down on math-generation tasks. Model-as-facet analysis reveals 16--22\\% model$\\times$item interaction, correcting systematic overestimation in prior single-model studies. D-study projections provide benchmark-specific reproducibility budgets: MMLU requires 420 items and 3 prompts for $G\\geq0.90$, while HellaSwag requires only 240 items but 4 prompts and 6 seeds. These findings establish that no universal reproducibility recipe exists---evaluation reliability must be planned task by task, metric by metric.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[Biderman et~al.(2024)]{biderman2024}\nBiderman, S., et~al. (2024).\n\\newblock Lessons from the trenches on reproducible evaluation of language models.\n\\newblock \\emph{arXiv preprint arXiv:2405.14782}.\n\n\\bibitem[Bouthillier et~al.(2021)]{bouthillier2021}\nBouthillier, X., et~al. (2021).\n\\newblock Accounting for variance in machine learning benchmarks.\n\\newblock \\emph{Machine Learning and Systems (MLSys)}.\n\n\\bibitem[Brennan(2001)]{brennan2001}\nBrennan, R.~L. (2001).\n\\newblock \\emph{Generalizability Theory}.\n\\newblock Springer-Verlag.\n\n\\bibitem[Dehghani et~al.(2021)]{dehghani2021}\nDehghani, M., et~al. (2021).\n\\newblock The benchmark lottery.\n\\newblock \\emph{arXiv preprint arXiv:2107.07002}.\n\n\\bibitem[Dodge et~al.(2020)]{dodge2020}\nDodge, J., Ilharco, G., Schwartz, R., Farhadi, A., Hajishirzi, H., and Smith, N.~A. (2020).\n\\newblock Fine-tuning pretrained language models: Weight initializations, data orders, and early stopping.\n\\newblock \\emph{arXiv preprint arXiv:2002.06305}.\n\n\\bibitem[Henderson et~al.(2018)]{henderson2018}\nHenderson, P., et~al. (2018).\n\\newblock Deep reinforcement learning that matters.\n\\newblock \\emph{AAAI}.\n\n\\bibitem[Lalor et~al.(2019)]{lalor2019}\nLalor, J.~P., Wu, H., and Yu, H. (2019).\n\\newblock Learning latent parameters without human response patterns: Item response theory with artificial crowds.\n\\newblock \\emph{EMNLP}.\n\n\\bibitem[Lu et~al.(2022)]{lu2022}\nLu, Y., et~al. (2022).\n\\newblock Are emergent abilities in large language models just in-context learning?\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Mesting(2026)]{mesting2026}\nMesting, F. (2026).\n\\newblock A generalizability theory analysis of LLM evaluation variance.\n\\newblock \\emph{ACL}.\n\n\\bibitem[Mizrahi et~al.(2024)]{mizrahi2024}\nMizrahi, M., et~al. (2024).\n\\newblock State of what art? A call for multi-prompt LLM evaluation.\n\\newblock \\emph{TACL}.\n\n\\bibitem[Perlitz et~al.(2023)]{perlitz2023}\nPerlitz, Y., et~al. (2023).\n\\newblock Efficient benchmarking (of language models).\n\\newblock \\emph{arXiv preprint arXiv:2308.11696}.\n\n\\bibitem[Pezeshkpour and Hruschka(2024)]{pezeshkpour2024}\nPezeshkpour, P. and Hruschka, E. (2024).\n\\newblock Large language models sensitivity to the order of options in multiple-choice questions.\n\\newblock \\emph{Findings of ACL}.\n\n\\bibitem[Polo et~al.(2024)]{polo2024}\nPolo, F.~M., et~al. (2024).\n\\newblock tinyBenchmarks: Evaluating LLMs with fewer examples.\n\\newblock \\emph{ICML}.\n\n\\bibitem[Rodriguez et~al.(2021)]{rodriguez2021}\nRodriguez, P., Barrow, J., Hoyle, A.~M., Lalor, J.~P., Jia, R., and Boyd-Graber, J. (2021).\n\\newblock Evaluation examples are not equally informative: How should that change NLP leaderboards?\n\\newblock \\emph{ACL}.\n\n\\bibitem[Sellam et~al.(2022)]{sellam2022}\nSellam, T., et~al. (2022).\n\\newblock MultiBERTs: BERT reproductions for robustness analysis.\n\\newblock \\emph{ICLR}.\n\n\\bibitem[Shavelson and Webb(1991)]{shavelson1991}\nShavelson, R.~J. and Webb, N.~M. (1991).\n\\newblock \\emph{Generalizability Theory: A Primer}.\n\\newblock Sage.\n\n\\bibitem[Vania et~al.(2021)]{vania2021}\nVania, C., et~al. (2021).\n\\newblock Comparing test sets with item response theory.\n\\newblock \\emph{ACL}.\n\n\\bibitem[Yuan et~al.(2025)]{yuan2025}\nYuan, Z., et~al. (2025).\n\\newblock Numerical precision matters: Hardware-induced variance in LLM evaluation.\n\\newblock \\emph{NeurIPS}.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfb693e2-04cc-485b-b442-1f06226827e9",
  "isSidechain": false,
  "requestId": "req_011CbEgG24jxzYGNppHAVjWf",
  "type": "assistant",
  "uuid": "7b280557-60c0-40d9-b971-ea2f9220cee1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EdZGwfDuDV4CepNasuPC8t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1723,
      "cache_read_input_tokens": 51253,
      "output_tokens": 14642,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1723,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14642,
          "cache_read_input_tokens": 51253,
          "cache_creation_input_tokens": 1723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1723
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-20T23:24:52.097Z_

<details><summary>↩ Tool result · `toolu_01KBMfpHbDgqp5981enZ9m8c`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b280557-60c0-40d9-b971-ea2f9220cee1",
  "isSidechain": false,
  "promptId": "c5460e05-f609-42c9-9ad5-28993b47482a",
  "type": "user",
  "uuid": "ce1efae8-9a07-4fb1-adad-1c48e86d3fbd",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median/paper.tex",
    "content": "\\documentclass[11pt,twocolumn]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\usepackage{enumitem}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{caption}\n\n\\setlength{\\columnsep}{0.3in}\n\\captionsetup{font=small}\n\n\\title{Reproducibility Budgets for LLM Evaluation:\\\\A Generalizability Theory Analysis of Variance Sources\\\\Across Benchmarks, Models, and Evaluation Metrics}\n\n\\author{\nAnonymous Authors\n}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nWhen LLM benchmark results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, numerical precision, temperature, or item selection---let alone how these factors interact. We conduct a multi-benchmark Generalizability Theory (G-theory) study crossing infrastructure (numerical precision, hardware) with methodology (prompt template, seed, temperature, answer ordering) and measurement (item selection) facets across five benchmarks (MMLU, ARC-Challenge, GSM8K, HellaSwag, MATH), four 7--9B models, two 14B models, and two GPU architectures, totaling over 3 million evaluation observations. Three findings emerge. First, item selection is the single largest variance source, but its magnitude is benchmark-conditional: 48\\% on knowledge-retrieval tasks (MMLU) versus 28\\% on proof-reasoning tasks (MATH) under model-as-facet analysis, forming a task-type clustering from knowledge-dominated to interaction-dominated variance structures. Second, infrastructure and methodology factors are approximately separable on knowledge benchmarks (infra$\\times$method $<$0.5\\% binary), but this separability breaks down on math-generation benchmarks where precision$\\times$temperature reaches 3\\% under binary scoring. Third, reproducibility budgets are fundamentally metric-dependent: binary scoring yields $G=0.37$ while text-exact-match yields $G=0.97$, and optimal facet allocation differs by benchmark---MMLU requires 420 items for $G\\geq0.90$ versus 240 for HellaSwag. We release variance decomposition tables and D-study projection code to enable task-specific reproducibility planning.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nThe reliability of LLM evaluation has become a first-order concern as benchmark scores drive model selection, funding decisions, and public perception. Recent studies have documented substantial score variation from individual factors: up to 9 percentage points from numerical precision alone \\citep{yuan2025}, 50\\% variance from prompt template choice on fixed hardware \\citep{mizrahi2024}, and significant sensitivity to random seeds and answer ordering \\citep{lu2022,pezeshkpour2024}. Yet each study isolates at most two sources, implicitly assuming that infrastructure factors (precision, hardware) and methodology factors (prompt, seed, temperature) contribute independently. Whether this separability assumption holds---and whether findings from one benchmark generalize to another---remains untested.\n\nGeneralizability Theory (G-theory) provides a principled framework for simultaneously decomposing variance across multiple facets and their interactions \\citep{shavelson1991,brennan2001}. Unlike ANOVA, G-theory distinguishes the universe score from error variance and supports Decision studies (D-studies) that project reliability under alternative resource allocations. \\citet{bouthillier2021} demonstrated the value of factorial variance decomposition for ML benchmarks via ANOVA, and \\citet{mesting2026} adapted G-theory to five methodology facets in LLM evaluation. However, neither study crossed infrastructure with methodology in a unified design, and both analyzed a single benchmark---leaving the question of cross-benchmark generalization unanswered.\n\nWe conduct the first multi-benchmark G-theory analysis of LLM evaluation variance, crossing infrastructure (numerical precision across two GPU architectures) with methodology (prompt template, seed, temperature, answer ordering) and measurement (item selection) facets. Our design spans five benchmarks (MMLU, ARC-Challenge, GSM8K, HellaSwag, MATH), four 7--9B models with model treated as a crossed random facet, and over 3 million total observations. The key insight is that \\emph{the variance structure itself depends on what you are benchmarking}: knowledge-retrieval benchmarks exhibit high item dominance with negligible cross-factor interaction, while reasoning benchmarks show reduced item dominance with detectable infrastructure$\\times$methodology coupling. This benchmark-conditional structure renders any ``universal reproducibility recipe'' illusory.\n\nOur contributions are: (1) a cross-benchmark variance gradient showing that item dominance shifts from 48\\% (knowledge) to 28\\% (proof reasoning) under model-as-facet analysis, with a three-tier task-type clustering; (2) a confirmatory separability test showing infrastructure$\\times$methodology interactions $<$0.5\\% on knowledge benchmarks but reaching 3\\% on math-generation benchmarks; and (3) task-specific reproducibility budgets via D-study projections with bootstrap confidence intervals, showing that optimal facet allocation is both benchmark-specific and metric-conditional.\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Variance sources in LLM evaluation.}\n\\citet{yuan2025} documented up to 9\\% accuracy variation from hardware and numerical precision without factorial attribution. \\citet{mizrahi2024} (Brittlebench) quantified prompt sensitivity at approximately 50\\% of evaluation variance on fixed hardware. \\citet{lu2022} and \\citet{pezeshkpour2024} demonstrated significant option-ordering effects in multiple-choice evaluation. \\citet{biderman2024} summarized reproducibility lessons across evaluation frameworks. These studies isolate individual factors; our work crosses them in a unified factorial design.\n\n\\paragraph{Generalizability Theory in NLP.}\nG-theory \\citep{shavelson1991,brennan2001} has been applied extensively in educational and psychological measurement. \\citet{bouthillier2021} adapted ANOVA-based variance decomposition to ML benchmarks, decomposing variance across hyperparameters, data splits, and seeds. \\citet{mesting2026} applied G-theory to LLM evaluation with five methodology facets but treated infrastructure as fixed and analyzed only MMLU. Our work extends this to infrastructure$\\times$methodology crossing across multiple benchmarks.\n\n\\paragraph{Item-level analysis and efficient benchmarking.}\nItem Response Theory (IRT) provides a complementary perspective on item properties \\citep{lalor2019,rodriguez2021,vania2021}. \\citet{polo2024} used IRT for efficient subsampling (tinyBenchmarks), and \\citet{perlitz2023} developed HELM-Lite for efficient benchmarking. Our D-study projections offer a G-theory-based alternative to IRT subsampling, with the advantage of jointly optimizing across multiple facets.\n\n\\paragraph{Training instability and reproducibility.}\n\\citet{dodge2020} documented fine-tuning instability from seeds and data order. \\citet{sellam2022} (MultiBERTs) trained multiple BERT copies to quantify training variance. \\citet{henderson2018} highlighted variance in deep RL evaluation. \\citet{dehghani2021} (Benchmark Lottery) showed that model ranking depends on benchmark selection. Our fine-tuning G-study (Section~\\ref{sec:finetuning}) extends this line by decomposing fine-tuning variance with G-theory.\n\n% ============================================================\n% 3. FRAMEWORK AND METHOD\n% ============================================================\n\\section{Framework and Method}\n\n\\subsection{Generalizability Theory}\n\nIn G-theory, the observed score for person $p$ (here: item $i$) under condition $c$ is decomposed as:\n\\begin{equation}\nX_{ic} = \\mu + \\alpha_i + \\beta_c + (\\alpha\\beta)_{ic} + \\epsilon_{ic}\n\\end{equation}\nwhere $\\alpha_i$ captures item difficulty, $\\beta_c$ captures condition effects (prompt, seed, temperature, precision, ordering), $(\\alpha\\beta)_{ic}$ captures item$\\times$condition interactions, and $\\epsilon_{ic}$ is residual error. G-theory estimates variance components $\\hat{\\sigma}^2$ for each source, which partition total variance. The \\emph{generalizability coefficient} $G$ quantifies the reliability of the benchmark score as a function of the number of items and conditions:\n\\begin{equation}\nG = \\frac{\\hat{\\sigma}^2_i}{\\hat{\\sigma}^2_i + \\sum_c \\hat{\\sigma}^2_{ic}/n_c + \\hat{\\sigma}^2_\\epsilon / (n_c \\cdot n_i)}\n\\end{equation}\n\nA \\emph{Decision study} (D-study) projects $G$ under hypothetical resource allocations (e.g., more items, fewer prompts), enabling cost-effective evaluation design.\n\n\\subsection{Experimental Design}\n\nWe conduct a series of G-studies with increasing scope:\n\n\\paragraph{Experiment 1: Full-scale MMLU G-study.} 4 models $\\times$ 3 precisions (FP32, BF16, FP16; all vLLM V0 enforce\\_eager) $\\times$ 6 prompt templates $\\times$ 6 seeds $\\times$ 3 temperatures $\\times$ 4 answer orderings $\\times$ 200 MMLU items (stratified across 57 subjects). Total: 1,036,800 observations across 5,184 conditions. The V0 enforce\\_eager configuration eliminates a previously identified engine confound where BF16 defaults to a different execution path.\n\n\\paragraph{Experiment 2: Item resampling stability.} Three independent stratified samples of 200 MMLU items (seeds 0, 7, 99) $\\times$ Llama-3.1-8B $\\times$ reduced crossing (3 precisions $\\times$ 3 prompts $\\times$ 3 seeds $\\times$ 2 orderings). 32,400 observations per sample.\n\n\\paragraph{Experiment 3: Multi-benchmark replication.} GSM8K, ARC-Challenge, and HellaSwag with 4 models $\\times$ 2 precisions (BF16, FP16) $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 2 temperatures $\\times$ 4 orderings $\\times$ 200 items. 384,000 observations per benchmark (reduced crossing vs.\\ Experiment 1).\n\n\\paragraph{Experiment 4: Multi-hardware G-study.} 4 models $\\times$ 2 GPU types $\\times$ 2 precisions $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 3 temperatures $\\times$ 4 orderings $\\times$ 200 MMLU items. 1,152,000 observations.\n\n\\paragraph{Experiment 5: Combined analysis.} Reanalysis of all preceding data with: (a) model treated as a crossed random facet; (b) bootstrap confidence intervals (1,000 resamples); (c) D-study projections; (d) REML vs.\\ Henderson Method I comparison; (e) log-probability scoring; (f) ranking stability analysis.\n\n\\paragraph{Experiment 6: 14B scale extension.} Qwen3-14B and DeepSeek-R1-Distill-14B at BF16/FP16 $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 2 temperatures $\\times$ 4 orderings $\\times$ 200 MMLU items.\n\n\\paragraph{Experiment 7: Fine-tuning G-study.} RoBERTa-large fine-tuned on SST-2, MNLI, RTE, and COPA with 6 seeds $\\times$ 3 learning rates $\\times$ 4 data shuffles $\\times$ 3 GPUs $\\times$ 2 precisions = 432 runs per task, 1,728 total.\n\n\\paragraph{Experiment 8: LayerCast mitigation.} LayerCast (FP16 storage + FP32 compute) as an additional precision condition on MMLU with the same 4 models and full facet crossing.\n\n\\paragraph{Experiment 9: MATH extension.} 200 MATH items $\\times$ 4 models $\\times$ 2 precisions $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 2 temperatures $\\times$ 4 orderings.\n\n\\subsection{Models and Infrastructure}\n\nWe use four 7--9B instruction-tuned models: Qwen3-8B-Instruct, Llama-3.1-8B-Instruct, Gemma-2-9B-IT, and Mistral-7B-v0.3. Scale extension uses Qwen3-14B and DeepSeek-R1-Distill-14B. All inference uses vLLM 0.9.2 with default settings (without batch-invariant kernels) to reflect realistic practitioner conditions. Variance components are estimated via Henderson Method I with REML sensitivity checks.\n\n\\subsection{Scoring Metrics}\n\nWe employ three scoring metrics: \\emph{binary correct} (1 if the extracted answer matches the gold label), \\emph{text exact match} (1 if the full generated text exactly matches a reference), and \\emph{log-probability} (continuous log-prob of the correct option). Each metric captures different variance structure.\n\n% ============================================================\n% 4. RESULTS\n% ============================================================\n\\section{Results}\n\n\\subsection{MMLU Variance Decomposition}\n\\label{sec:mmlu}\n\nTable~\\ref{tab:mmlu_binary} presents the variance decomposition for MMLU under binary correct scoring with models pooled. Item selection dominates at 52.0\\% of total variance, consistent with the psychometric expectation that item difficulty is the primary driver when difficulty varies widely \\citep{brennan2001}. The next-largest sources are all item interactions: prompt$\\times$item (5.8\\%), temperature$\\times$item (5.5\\%), and precision$\\times$item (5.0\\%). Infrastructure$\\times$methodology interactions (all direct cross-factor terms) total only 0.4\\%, supporting approximate separability at the aggregate level.\n\n\\begin{table}[t]\n\\centering\n\\caption{MMLU variance decomposition (binary correct, model pooled, $N$=1,036,800).}\n\\label{tab:mmlu_binary}\n\\small\n\\begin{tabular}{@{}lr@{}}\n\\toprule\nSource & \\% Variance \\\\\n\\midrule\nitem\\_id & 52.0 \\\\\nresidual (incl.\\ model) & 14.0 \\\\\nprompt$\\times$item & 5.8 \\\\\ntemperature$\\times$item & 5.5 \\\\\nprecision$\\times$item & 5.0 \\\\\nprecision (main) & 3.0 \\\\\nseed$\\times$item & 2.8 \\\\\ntemperature (main) & 1.5 \\\\\nprompt (main) & 0.8 \\\\\ninfra$\\times$method (all) & 0.4 \\\\\nordering & 0.2 \\\\\nother 2-way/3-way & 9.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder text-exact-match scoring, the variance structure shifts qualitatively: prompt$\\times$item rises to 33.0\\%, residual accounts for 36.0\\%, and item\\_id drops to 3.0\\%. The generalizability coefficient reflects this: $G=0.37$ under binary scoring versus $G=0.97$ under text-match. This metric dependence is a central finding.\n\n\\paragraph{FP32 degradation.} Table~\\ref{tab:precision_accuracy} shows that FP32 inference degrades accuracy by 2.9 percentage points (pp) on average relative to BF16, with strong model dependence (1.5--7.2pp). This effect persists under V0 enforce\\_eager, confirming it is a genuine precision artifact rather than an engine confound, consistent with \\citet{yuan2025}. The novel contribution is the item-level breakdown: precision$\\times$item (5.0\\%) exceeds the precision main effect (3.0\\%), indicating that items near decision boundaries are disproportionately affected.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-model MMLU accuracy by precision (V0 enforce\\_eager). All models show FP32 degradation.}\n\\label{tab:precision_accuracy}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & FP32 & BF16 & FP16 & Gap \\\\\n\\midrule\nQwen3-8B & .695 & .710 & .706 & 1.5pp \\\\\nLlama-3.1-8B & .600 & .672 & .669 & 7.2pp \\\\\nGemma-2-9B & .638 & .660 & .658 & 2.2pp \\\\\nMistral-7B & .688 & .694 & .691 & 0.6pp \\\\\n\\midrule\nAverage & .655 & .684 & .681 & 2.9pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Item Resampling Stability}\n\\label{sec:resampling}\n\nA single draw of 200 items from MMLU's 14,042 items introduces meaningful sampling uncertainty. Table~\\ref{tab:resampling} shows variance components across three independent stratified draws. Item dominance ranges from 44\\% to 55\\% (CV=0.19), and the G-coefficient varies from 0.32 to 0.39. Crucially, the \\emph{rank ordering} of variance sources is preserved across all draws (item\\_id always ranks first), but point estimates of magnitude are unstable. This explains why prior studies using different item sets reached different headline numbers.\n\n\\begin{table}[t]\n\\centering\n\\caption{Resampling stability of key variance components across three independent 200-item stratified MMLU samples (Llama-3.1-8B).}\n\\label{tab:resampling}\n\\small\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nSource & S0 & S7 & S99 & Mean & CV \\\\\n\\midrule\nitem\\_id & 49.0 & 55.0 & 44.0 & 49.3 & .19 \\\\\nresidual & 17.5 & 15.0 & 19.5 & 17.3 & .11 \\\\\nprompt:item & 6.5 & 6.0 & 7.0 & 6.5 & .09 \\\\\ntemp:item & 5.8 & 5.2 & 6.5 & 5.8 & .10 \\\\\nprec:item & 5.0 & 5.5 & 4.2 & 4.9 & .12 \\\\\nprecision & 3.0 & 3.5 & 2.8 & 3.1 & .10 \\\\\n\\midrule\n$G$ (binary) & .36 & .32 & .39 & .36 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Benchmark Variance Structure}\n\\label{sec:crossbenchmark}\n\nTable~\\ref{tab:crossbench} presents the variance decomposition across all five benchmarks under binary scoring with models pooled. The data reveal a task-type clustering rather than a clean monotonic gradient. Knowledge-retrieval benchmarks (MMLU, ARC) show high item dominance (50--52\\%), while reasoning benchmarks show progressively lower item dominance: GSM8K (40\\%), HellaSwag (35\\%), and MATH (32\\%). The 20pp spread across benchmarks is statistically significant (permutation $p=0.003$) but the endpoints' bootstrap CIs overlap partially (Section~\\ref{sec:modelasfacet}), requiring directional rather than magnitude claims.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-benchmark variance decomposition (binary correct, model pooled). Benchmarks sorted by item dominance. 384,000 obs/benchmark (GSM8K, ARC, HellaSwag); 1,036,800 (MMLU).}\n\\label{tab:crossbench}\n\\small\n\\begin{tabular}{@{}lrrrrr@{}}\n\\toprule\nSource & MMLU & ARC & GSM & Hella & MATH \\\\\n\\midrule\nitem\\_id & 52.0 & 50.0 & 40.0 & 35.0 & 32.0 \\\\\nresidual & 14.0 & 12.0 & 15.0 & 18.0 & 17.0 \\\\\ntemp:item & 5.5 & 5.5 & 10.0 & 9.5 & 14.0 \\\\\nseed:item & 2.8 & 4.0 & 7.0 & 8.5 & 11.0 \\\\\nprompt:item & 5.8 & 8.5 & 6.5 & 7.5 & 8.0 \\\\\nprec:item & 5.0 & 2.5 & 1.5 & 1.5 & 1.5 \\\\\nprecision & 3.0 & 1.0 & 1.0 & 0.5 & 0.5 \\\\\ntemperature & 1.5 & 2.5 & 4.0 & 4.5 & 6.0 \\\\\ninfra$\\times$meth & 0.4 & 0.5 & 3.0 & 0.3 & 2.5 \\\\\nother & 10.0 & 13.5 & 12.0 & 14.7 & 7.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe critical finding for separability is benchmark-conditional: on knowledge benchmarks (MMLU, ARC), infra$\\times$method totals $<$0.5\\%, but on GSM8K it reaches 3.0\\% (precision$\\times$temperature 2.2\\% + precision$\\times$seed 0.5\\% + precision$\\times$prompt 0.3\\%). Table~\\ref{tab:gsm8k_infra} breaks down the GSM8K interaction. Under text-match scoring, GSM8K infra$\\times$method reaches 3.5\\%. This benchmark-specific departure means that separability claims require qualification: ``on knowledge-retrieval benchmarks'' or ``excluding math-generation tasks.''\n\n\\begin{table}[t]\n\\centering\n\\caption{GSM8K infra$\\times$method interaction breakdown (binary). Only GSM8K and MATH exceed 1\\%; MMLU 0.4\\%, ARC 0.5\\%, HellaSwag 0.3\\%.}\n\\label{tab:gsm8k_infra}\n\\small\n\\begin{tabular}{@{}lr@{}}\n\\toprule\nInteraction & \\% Variance \\\\\n\\midrule\nprecision$\\times$temperature & 2.2 \\\\\nprecision$\\times$seed & 0.5 \\\\\nprecision$\\times$prompt & 0.3 \\\\\n\\midrule\nTotal infra$\\times$method & 3.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWith MATH included, the pattern extends from a two-cluster to a three-tier structure: \\{MMLU 52\\%, ARC 50\\%\\} $>$ \\{GSM8K 40\\%, HellaSwag 35\\%\\} $\\geq$ \\{MATH 32\\%\\}. MATH exhibits the highest temperature$\\times$item (14\\%) and seed$\\times$item (11\\%) among all benchmarks, consistent with the multi-step proof reasoning that introduces maximal chain-of-thought variance.\n\n\\subsection{Model-as-Facet Reanalysis}\n\\label{sec:modelasfacet}\n\nTable~\\ref{tab:model_facet} presents the reanalysis with model treated as a crossed random facet. This absorbs model$\\times$item interaction---previously conflated with item\\_id and residual---into an explicit component. On MMLU, model$\\times$item accounts for 21\\% of total variance, reducing item\\_id from 52\\% to 48\\% and residual from 14\\% to 8\\%. The 4pp reduction is consistent across all benchmarks, suggesting that prior single-model studies systematically overestimated pure item dominance.\n\n\\begin{table}[t]\n\\centering\n\\caption{Model-as-facet variance decomposition (binary correct) across five benchmarks. Model$\\times$item captures model-specific item difficulty profiles.}\n\\label{tab:model_facet}\n\\small\n\\begin{tabular}{@{}lrrrrr@{}}\n\\toprule\nSource & MMLU & ARC & GSM & Hella & MATH \\\\\n\\midrule\nitem\\_id & 48.0 & 46.0 & 36.0 & 31.0 & 28.0 \\\\\nmodel$\\times$item & 21.0 & 16.0 & 18.0 & 19.0 & 22.0 \\\\\nmodel (main) & 5.0 & 4.0 & 4.0 & 5.0 & 6.0 \\\\\nresidual & 8.0 & 8.0 & 10.0 & 10.0 & 7.0 \\\\\ntemp:item & 4.8 & 5.0 & 9.0 & 8.5 & 14.0 \\\\\nseed:item & 2.0 & 3.0 & 5.5 & 7.0 & 11.0 \\\\\nprompt:item & 5.3 & 7.5 & 5.5 & 6.5 & 6.5 \\\\\nprec:item & 2.8 & 2.0 & 1.2 & 1.2 & --- \\\\\nprecision & 2.5 & 0.8 & 0.8 & 0.3 & --- \\\\\ntemperature & 1.2 & 2.2 & 3.5 & 4.0 & 4.5 \\\\\ninfra$\\times$meth & 0.4 & 0.5 & 3.0 & 0.3 & 2.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe benchmark-conditional structure persists after model-as-facet correction, with a 20pp spread from MMLU (48\\%) to MATH (28\\%). The three-tier clustering is preserved: knowledge benchmarks (\\{MMLU, ARC\\}: 46--48\\%), arithmetic/commonsense reasoning (\\{GSM8K, HellaSwag\\}: 31--36\\%), and proof reasoning (\\{MATH\\}: 28\\%).\n\n\\paragraph{Bootstrap confidence intervals.} Table~\\ref{tab:bootstrap_ci} reports 95\\% bootstrap CIs (1,000 item$\\times$condition resamples) on key variance components. The item\\_id CIs are wide (width $\\approx$0.14), reflecting both item-sampling instability (Section~\\ref{sec:resampling}) and condition-resampling uncertainty. The gradient direction is statistically significant ($p=0.003$): MMLU item\\_id $[0.41, 0.55]$ vs.\\ HellaSwag $[0.24, 0.38]$, with partial overlap only at the margins ($[0.38, 0.41]$). GSM8K infra$\\times$method CI $[0.012, 0.048]$ excludes zero, confirming a statistically robust departure from separability.\n\n\\begin{table}[t]\n\\centering\n\\caption{Bootstrap 95\\% CIs on key variance components (model-as-facet, 1,000 resamples).}\n\\label{tab:bootstrap_ci}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n & MMLU & GSM & ARC & Hella \\\\\n\\midrule\nitem & [.41,.55] & [.29,.43] & [.39,.53] & [.24,.38] \\\\\nm$\\times$i & [.16,.27] & [.13,.24] & [.11,.22] & [.14,.25] \\\\\ninf$\\times$m & [.00,.01] & [.01,.05] & [.00,.01] & [.00,.01] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Hardware Facet Analysis}\n\\label{sec:hardware}\n\nTable~\\ref{tab:hardware} presents variance components from the multi-hardware G-study on MMLU. Total hardware-related variance is 3.6\\% under binary scoring and 7.5\\% under text-match. The largest component is hardware$\\times$item (1.8\\% binary), indicating that items near decision boundaries are sensitive to GPU-specific kernel scheduling differences.\n\n\\begin{table}[t]\n\\centering\n\\caption{Hardware facet variance components (MMLU, 1,152,000 obs, 2 GPU types).}\n\\label{tab:hardware}\n\\small\n\\begin{tabular}{@{}lrr@{}}\n\\toprule\nSource & Binary \\% & Text \\% \\\\\n\\midrule\nhardware (main) & 0.4 & 1.2 \\\\\nhardware$\\times$precision & 0.8 & 2.2 \\\\\nhardware$\\times$temperature & 0.3 & 0.6 \\\\\nhardware$\\times$seed & 0.2 & 0.4 \\\\\nhardware$\\times$prompt & 0.1 & 0.3 \\\\\nhardware$\\times$item & 1.8 & 2.8 \\\\\n\\midrule\nTotal hardware & 3.6 & 7.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHardware sensitivity is precision-conditional: when restricted to FP16 data, hardware explains 2.2\\% of variance with cross-GPU accuracy gaps up to 1.1pp. Under BF16, hardware accounts for only 0.3\\% with gaps $\\leq$0.2pp. This asymmetry arises because FP16's narrower dynamic range (5-bit exponent) makes accumulation order hardware-dependent. Model rankings are fully preserved across GPUs---hardware effects are too small to alter comparative model evaluation. Practical recommendation: use BF16 for hardware-independent reproducibility.\n\n\\subsection{D-Study Reproducibility Budgets}\n\\label{sec:dstudy}\n\nTable~\\ref{tab:dstudy} presents D-study projections for the number of items needed to achieve target generalizability coefficients, assuming BF16 precision and optimal prompt/seed allocation. The projections differentiate benchmarks: MMLU requires 420 items for $G\\geq0.90$ versus 240 for HellaSwag (ratio 1.75$\\times$). The practical implication is that knowledge-retrieval benchmarks need 50--75\\% more items than reasoning benchmarks to achieve equivalent reliability, because higher item dominance requires more items to stabilize the universe score estimate.\n\n\\begin{table}[t]\n\\centering\n\\caption{D-study projections: items needed for target $G$ (BF16, optimal prompt/seed). CIs from bootstrap.}\n\\label{tab:dstudy}\n\\small\n\\begin{tabular}{@{}lrrccc@{}}\n\\toprule\nBench & $G$\\scriptsize{$\\geq$.80} & $G$\\scriptsize{$\\geq$.90} & CI\\scriptsize{$_{.90}$} & $G$\\scriptsize{$\\geq$.95} & P/S \\\\\n\\midrule\nMMLU & 220 & 420 & [350,510] & 680 & 3/4 \\\\\nARC & 200 & 380 & [310,470] & 620 & 3/4 \\\\\nGSM8K & 150 & 280 & [220,360] & 450 & 4/6 \\\\\nHella & 130 & 240 & [190,310] & 400 & 4/6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nD-study CIs on the $G\\geq0.90$ threshold span $\\pm$80 items (MMLU: $[350, 510]$), reflecting uncertainty that practitioners should acknowledge when setting evaluation budgets. GSM8K and HellaSwag require more prompts (4 vs.\\ 3) and seeds (6 vs.\\ 4) due to their higher interaction variance.\n\n\\subsection{Scoring Metric Sensitivity}\n\\label{sec:metrics}\n\nTable~\\ref{tab:scoring} demonstrates that the variance hierarchy is fundamentally metric-dependent. Under binary scoring, item\\_id dominates (48\\%); under text-match, prompt$\\times$item (33\\%) and residual (36\\%) dominate while item\\_id drops to 3\\%. Log-probability scoring amplifies item dominance to 55\\% because continuous log-probs capture fine-grained difficulty more sensitively than binary 0/1. The $G$-coefficient ranges from 0.32 (logprob) to 0.97 (text-match)---a practitioner choosing text-match scoring would conclude the benchmark is already reliable, while binary scoring reveals substantial unreliability.\n\n\\begin{table}[t]\n\\centering\n\\caption{Scoring metric comparison (MMLU, model-as-facet). Variance hierarchy depends qualitatively on the evaluation metric.}\n\\label{tab:scoring}\n\\small\n\\begin{tabular}{@{}lrrr@{}}\n\\toprule\nSource & Binary & Text & Logprob \\\\\n\\midrule\nitem\\_id & 48.0 & 3.0 & 55.0 \\\\\nmodel$\\times$item & 21.0 & 1.5 & 18.0 \\\\\nprompt:item & 5.3 & 33.0 & 4.0 \\\\\nresidual & 8.0 & 36.0 & 6.0 \\\\\n\\midrule\n$G$ & 0.37 & 0.97 & 0.32 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Estimation Method Sensitivity}\n\nREML and Henderson Method I estimates agree to within 2.1pp on all variance components (Table~\\ref{tab:reml}). Rank ordering is fully preserved. This methodological choice does not affect qualitative conclusions.\n\n\\begin{table}[t]\n\\centering\n\\caption{REML vs.\\ Henderson Method I (MMLU, binary).}\n\\label{tab:reml}\n\\small\n\\begin{tabular}{@{}lrrr@{}}\n\\toprule\nSource & Henderson & REML & $\\Delta$ \\\\\n\\midrule\nitem\\_id & 48.0\\% & 49.2\\% & +1.2 \\\\\nmodel$\\times$item & 21.0\\% & 22.4\\% & +1.4 \\\\\nresidual & 8.0\\% & 6.1\\% & $-$1.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{14B Scale Extension}\n\\label{sec:scale}\n\nTable~\\ref{tab:scale} compares variance decomposition at 8B (4 models) and 14B (2 models: Qwen3-14B, DeepSeek-R1-Distill-14B) on MMLU. Item dominance decreases by 4pp (48\\%$\\to$44\\%) as higher capacity reduces floor effects. Model$\\times$item increases by 4pp (21\\%$\\to$25\\%) because the dense-versus-reasoning-distilled architecture difference creates larger model-specific item profiles: DeepSeek-R1-Distill-14B excels on multi-step reasoning items while Qwen3-14B excels on factual knowledge items.\n\n\\begin{table}[t]\n\\centering\n\\caption{8B vs.\\ 14B variance decomposition (MMLU, model-as-facet, binary).}\n\\label{tab:scale}\n\\small\n\\begin{tabular}{@{}lrrc@{}}\n\\toprule\nSource & 8B & 14B & $\\Delta$ \\\\\n\\midrule\nitem\\_id & 48.0 & 44.0 & $-$4.0 \\\\\nmodel$\\times$item & 21.0 & 25.0 & +4.0 \\\\\nmodel (main) & 5.0 & 7.0 & +2.0 \\\\\nresidual & 8.0 & 6.0 & $-$2.0 \\\\\ntemp:item & 4.8 & 6.0 & +1.2 \\\\\nprompt:item & 5.3 & 4.5 & $-$0.8 \\\\\nprecision & 2.5 & 0.3 & $-$2.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDeepSeek-R1-Distill-14B shows elevated temperature$\\times$item interaction (8.5\\% vs.\\ 4.2\\% for Qwen3-14B) because reasoning-distilled models produce chain-of-thought that branches more at sampling time. The variance hierarchy is qualitatively preserved at 14B (item\\_id $>$ model$\\times$item $>$ residual), suggesting that the framework's findings are not an artifact of a narrow model-size range.\n\n\\subsection{Fine-Tuning Variance Decomposition}\n\\label{sec:finetuning}\n\nTable~\\ref{tab:finetune} presents variance decomposition for RoBERTa-large fine-tuning across four classification tasks. The variance hierarchy is qualitatively different from inference: hyperparameters dominate instead of items. On large datasets (SST-2, MNLI), learning rate is the primary source (30--35\\%). On small datasets (RTE, COPA), data shuffle dominates (28--30\\%) because mini-batch composition has outsized influence with fewer training examples.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fine-tuning variance decomposition (RoBERTa-large, 432 runs/task).}\n\\label{tab:finetune}\n\\small\n\\begin{tabular}{@{}lrrrr@{}}\n\\toprule\nSource & SST-2 & MNLI & RTE & COPA \\\\\n\\midrule\nlearning\\_rate & 35.0 & 30.0 & 20.0 & 18.0 \\\\\nseed & 25.0 & 22.0 & 16.0 & 20.0 \\\\\ndata\\_shuffle & 12.0 & 15.0 & 28.0 & 30.0 \\\\\nseed$\\times$lr & 10.0 & 12.0 & 16.0 & 14.0 \\\\\ngpu & 0.3 & 0.4 & 0.5 & 0.4 \\\\\nprecision & 0.8 & 0.9 & 1.0 & 1.2 \\\\\nresidual & 16.9 & 19.7 & 18.5 & 16.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nInfrastructure effects (GPU + precision) remain $<$1.5\\% across all tasks, consistent with the inference experiments. The seed$\\times$lr interaction (10--16\\%) is the fine-tuning analogue of item$\\times$temperature in inference: certain seed-LR combinations land in qualitatively different loss basins, producing bimodal accuracy distributions on RTE. This parallel---methodology interactions dominate, infrastructure is negligible---validates the G-theory framework's generality while confirming that reproducibility budgets cannot transfer between evaluation modes.\n\n\\subsection{Precision Mitigation: LayerCast}\n\\label{sec:layercast}\n\nTable~\\ref{tab:layercast} evaluates LayerCast (FP16 storage + FP32 compute) as a precision mitigation strategy. LayerCast reduces precision$\\times$item interaction by $\\sim$40\\% relative to FP16 and achieves accuracy (0.682) essentially equivalent to BF16 (0.684). However, the practical benefit is marginal: precision effects are already small post-confound analysis (precision main 2.5\\% of total), and the 18\\% inference overhead makes LayerCast cost-ineffective relative to simply using BF16.\n\n\\begin{table}[t]\n\\centering\n\\caption{LayerCast comparison across precision modes (MMLU, binary).}\n\\label{tab:layercast}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nMetric & FP32 & BF16 & FP16 & LC \\\\\n\\midrule\nAccuracy & .655 & .684 & .681 & .682 \\\\\nitem\\_id \\% & 50.5 & 52.0 & 51.8 & 51.5 \\\\\nprec:item \\% & 5.8 & 4.5 & 5.0 & 3.0 \\\\\np$\\times$t (binary) & 0.3 & 0.1 & 0.2 & 0.1 \\\\\np$\\times$t (text) & 2.5 & 1.8 & 2.2 & 0.8 \\\\\n$G$ (binary) & .36 & .37 & .37 & .37 \\\\\nCost (rel.) & 1.35 & 1.00 & 1.00 & 1.18 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Five-Benchmark Summary}\n\nTable~\\ref{tab:summary} synthesizes the benchmark-conditional findings under model-as-facet analysis. The three-tier structure tracks cognitive demand: knowledge benchmarks exhibit high item dominance with negligible infra$\\times$method coupling, while reasoning benchmarks show redistributed variance toward temperature and seed interactions, with math-generation benchmarks additionally showing detectable infrastructure$\\times$methodology interaction.\n\n\\begin{table}[t]\n\\centering\n\\caption{Five-benchmark summary (model-as-facet, binary).}\n\\label{tab:summary}\n\\small\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nBench & Type & $i$ \\% & $G$ & i$\\times$m & Tier \\\\\n\\midrule\nMMLU & Know. & 48 & .37 & 0.4 & High \\\\\nARC & Know. & 46 & .35 & 0.5 & High \\\\\nGSM8K & Arith. & 36 & .42 & 3.0 & Mid \\\\\nHella & C.sense & 31 & .48 & 0.3 & Mid \\\\\nMATH & Proof & 28 & .52 & 2.5 & Low \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n% 5. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{The variance structure is benchmark-conditional.}\nOur central finding is that no single variance decomposition characterizes ``LLM evaluation.'' Knowledge-retrieval benchmarks (MMLU, ARC) are item-dominated with separable infrastructure and methodology effects, while reasoning benchmarks (GSM8K, MATH) show reduced item dominance, elevated sampling interactions, and detectable infrastructure$\\times$methodology coupling. This benchmark-conditional structure explains why prior studies---each analyzing a single benchmark---reached seemingly contradictory conclusions about which factors matter most.\n\n\\paragraph{Model-as-facet reframes prior work.}\nTreating model as a crossed random facet reveals that 16--22\\% of total variance is model$\\times$item interaction: items that are hard for one model architecture may be easy for another. Prior single-model studies attributed this variance to item difficulty, inflating item dominance by approximately 4pp. This correction applies systematically across benchmarks and should be standard practice in G-theory analyses of LLM evaluation.\n\n\\paragraph{Separability requires qualification.}\nOn knowledge benchmarks, infrastructure$\\times$methodology interactions are negligible ($<$0.5\\% binary), validating the implicit assumption of prior isolated-factor studies. On math-generation benchmarks, precision$\\times$temperature reaches 2--3\\%, driven by floating-point non-associativity in long chain-of-thought generation. Practitioners evaluating on math-reasoning benchmarks should fix both precision and temperature to avoid confounding.\n\n\\paragraph{Hardware is manageable.}\nTotal hardware-related variance is 3.6\\% (binary), predominantly from hardware$\\times$item (1.8\\%)---the same items sensitive to precision changes are also hardware-sensitive, suggesting a shared mechanism of logit perturbation near decision boundaries. BF16 reduces hardware sensitivity to 0.3\\%, providing a practical path to hardware-independent evaluation. Model rankings are preserved across GPUs.\n\n\\paragraph{Metric dependence as a feature.}\nThe dramatic shift in variance structure between binary ($G=0.37$) and text-match ($G=0.97$) scoring is not a methodological weakness but an important empirical result: the choice of evaluation metric determines which variance sources are visible. Text-match scoring inflates apparent reliability by averaging over generation-level variation that binary scoring correctly captures.\n\n\\paragraph{Limitations.}\nOur infrastructure facet is limited to numerical precision and two GPU architectures; quantization, batching strategies, and API-based inference are not covered. The model sample spans 7--14B open-weight models; API models with opaque infrastructure and models at 70B+ scale may exhibit different variance structures. The fine-tuning analysis uses encoder-only RoBERTa; decoder fine-tuning introduces generation-related variance sources. Item samples of 200 per benchmark leave meaningful sampling uncertainty (CV$\\approx$0.19).\n\n% ============================================================\n% 6. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe presented the first multi-benchmark Generalizability Theory analysis of LLM evaluation, crossing infrastructure, methodology, and measurement facets across five benchmarks, six model architectures, and two GPU types. The variance structure is benchmark-conditional: item dominance ranges from 48\\% (knowledge retrieval) to 28\\% (proof reasoning), and infrastructure$\\times$methodology separability holds on knowledge benchmarks but breaks down on math-generation tasks. Model-as-facet analysis reveals 16--22\\% model$\\times$item interaction, correcting systematic overestimation in prior single-model studies. D-study projections provide benchmark-specific reproducibility budgets: MMLU requires 420 items and 3 prompts for $G\\geq0.90$, while HellaSwag requires only 240 items but 4 prompts and 6 seeds. These findings establish that no universal reproducibility recipe exists---evaluation reliability must be planned task by task, metric by metric.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[Biderman et~al.(2024)]{biderman2024}\nBiderman, S., et~al. (2024).\n\\newblock Lessons from the trenches on reproducible evaluation of language models.\n\\newblock \\emph{arXiv preprint arXiv:2405.14782}.\n\n\\bibitem[Bouthillier et~al.(2021)]{bouthillier2021}\nBouthillier, X., et~al. (2021).\n\\newblock Accounting for variance in machine learning benchmarks.\n\\newblock \\emph{Machine Learning and Systems (MLSys)}.\n\n\\bibitem[Brennan(2001)]{brennan2001}\nBrennan, R.~L. (2001).\n\\newblock \\emph{Generalizability Theory}.\n\\newblock Springer-Verlag.\n\n\\bibitem[Dehghani et~al.(2021)]{dehghani2021}\nDehghani, M., et~al. (2021).\n\\newblock The benchmark lottery.\n\\newblock \\emph{arXiv preprint arXiv:2107.07002}.\n\n\\bibitem[Dodge et~al.(2020)]{dodge2020}\nDodge, J., Ilharco, G., Schwartz, R., Farhadi, A., Hajishirzi, H., and Smith, N.~A. (2020).\n\\newblock Fine-tuning pretrained language models: Weight initializations, data orders, and early stopping.\n\\newblock \\emph{arXiv preprint arXiv:2002.06305}.\n\n\\bibitem[Henderson et~al.(2018)]{henderson2018}\nHenderson, P., et~al. (2018).\n\\newblock Deep reinforcement learning that matters.\n\\newblock \\emph{AAAI}.\n\n\\bibitem[Lalor et~al.(2019)]{lalor2019}\nLalor, J.~P., Wu, H., and Yu, H. (2019).\n\\newblock Learning latent parameters without human response patterns: Item response theory with artificial crowds.\n\\newblock \\emph{EMNLP}.\n\n\\bibitem[Lu et~al.(2022)]{lu2022}\nLu, Y., et~al. (2022).\n\\newblock Are emergent abilities in large language models just in-context learning?\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Mesting(2026)]{mesting2026}\nMesting, F. (2026).\n\\newblock A generalizability theory analysis of LLM evaluation variance.\n\\newblock \\emph{ACL}.\n\n\\bibitem[Mizrahi et~al.(2024)]{mizrahi2024}\nMizrahi, M., et~al. (2024).\n\\newblock State of what art? A call for multi-prompt LLM evaluation.\n\\newblock \\emph{TACL}.\n\n\\bibitem[Perlitz et~al.(2023)]{perlitz2023}\nPerlitz, Y., et~al. (2023).\n\\newblock Efficient benchmarking (of language models).\n\\newblock \\emph{arXiv preprint arXiv:2308.11696}.\n\n\\bibitem[Pezeshkpour and Hruschka(2024)]{pezeshkpour2024}\nPezeshkpour, P. and Hruschka, E. (2024).\n\\newblock Large language models sensitivity to the order of options in multiple-choice questions.\n\\newblock \\emph{Findings of ACL}.\n\n\\bibitem[Polo et~al.(2024)]{polo2024}\nPolo, F.~M., et~al. (2024).\n\\newblock tinyBenchmarks: Evaluating LLMs with fewer examples.\n\\newblock \\emph{ICML}.\n\n\\bibitem[Rodriguez et~al.(2021)]{rodriguez2021}\nRodriguez, P., Barrow, J., Hoyle, A.~M., Lalor, J.~P., Jia, R., and Boyd-Graber, J. (2021).\n\\newblock Evaluation examples are not equally informative: How should that change NLP leaderboards?\n\\newblock \\emph{ACL}.\n\n\\bibitem[Sellam et~al.(2022)]{sellam2022}\nSellam, T., et~al. (2022).\n\\newblock MultiBERTs: BERT reproductions for robustness analysis.\n\\newblock \\emph{ICLR}.\n\n\\bibitem[Shavelson and Webb(1991)]{shavelson1991}\nShavelson, R.~J. and Webb, N.~M. (1991).\n\\newblock \\emph{Generalizability Theory: A Primer}.\n\\newblock Sage.\n\n\\bibitem[Vania et~al.(2021)]{vania2021}\nVania, C., et~al. (2021).\n\\newblock Comparing test sets with item response theory.\n\\newblock \\emph{ACL}.\n\n\\bibitem[Yuan et~al.(2025)]{yuan2025}\nYuan, Z., et~al. (2025).\n\\newblock Numerical precision matters: Hardware-induced variance in LLM evaluation.\n\\newblock \\emph{NeurIPS}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "7b280557-60c0-40d9-b971-ea2f9220cee1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T222113 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheo…",
  "leafUuid": "ce1efae8-9a07-4fb1-adad-1c48e86d3fbd",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulation paper for dream_20260520T222113",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff"
}
```

---

### Assistant

_source line 27 · 2026-05-20T23:24:56.170Z_

Now compiling.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce1efae8-9a07-4fb1-adad-1c48e86d3fbd",
  "isSidechain": false,
  "requestId": "req_011CbEgcyGQfDSpTtrtFuPkj",
  "type": "assistant",
  "uuid": "c8195c16-c3e6-4b57-9731-aabbf8e2cdba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F1KCxL7DjjsFYJWapTqV8J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14702,
      "cache_read_input_tokens": 52976,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14702,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 52976,
          "cache_creation_input_tokens": 14702,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14702
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-20T23:24:57.427Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WDe9K44VjXHmStpGXX1nVu`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8195c16-c3e6-4b57-9731-aabbf8e2cdba",
  "isSidechain": false,
  "requestId": "req_011CbEgcyGQfDSpTtrtFuPkj",
  "type": "assistant",
  "uuid": "cd491f03-ac9e-4431-b669-5aa0c512267f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F1KCxL7DjjsFYJWapTqV8J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14702,
      "cache_read_input_tokens": 52976,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14702,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 52976,
          "cache_creation_input_tokens": 14702,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14702
          },
          "type": "message"
        }
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

_source line 29 · 2026-05-20T23:25:02.412Z_

<details><summary>↩ Tool result · `toolu_01WDe9K44VjXHmStpGXX1nVu`</summary>

```text
 Ok [38] [63] [190])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf
 Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]
[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf
 Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]
[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]
[121] [122])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf
 Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf
 Ok) ) ) )
(some charht values had to be adjusted by as much as 0.0972pt)
Font metrics written on ecrm1728.tfm.
Output written on ecrm1728.600gf (256 characters, 84608 bytes).
Transcript written on ecrm1728.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk: successfully generated.
 &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
sy8.pfb>
Output written on paper.pdf (10 pages, 241255 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd491f03-ac9e-4431-b669-5aa0c512267f",
  "isSidechain": false,
  "promptId": "c5460e05-f609-42c9-9ad5-28993b47482a",
  "type": "user",
  "uuid": "8837aa9e-ee08-4149-bead-96af332e02cc",
  "toolUseResult": {
    "stdout": " Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.0972pt)\nFont metrics written on ecrm1728.tfm.\nOutput written on ecrm1728.600gf (256 characters, 84608 bytes).\nTranscript written on ecrm1728.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk: successfully generated.\n &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nsy8.pfb>\nOutput written on paper.pdf (10 pages, 241255 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "cd491f03-ac9e-4431-b669-5aa0c512267f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-20T23:25:02.415Z_

```json
{
  "parentUuid": "8837aa9e-ee08-4149-bead-96af332e02cc",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "fa9c6493-3b5a-4849-8c1d-249f8b8897b1",
  "timestamp": "2026-05-20T23:25:02.415Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-20T23:25:07.355Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01ADbouJWtuzVPuPyWmY7yra`</summary>

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
  "parentUuid": "fa9c6493-3b5a-4849-8c1d-249f8b8897b1",
  "isSidechain": false,
  "requestId": "req_011CbEgdj7PeyMZAbKXykhwt",
  "type": "assistant",
  "uuid": "7c63eaff-de47-4ebc-8337-4308a28289c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bpqdycg5ariTbcNaNZFKoT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 67678,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1130,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 67678,
          "cache_creation_input_tokens": 1130,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1130
          },
          "type": "message"
        }
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

_source line 32 · 2026-05-20T23:25:07.869Z_

<details><summary>↩ Tool result · `toolu_01ADbouJWtuzVPuPyWmY7yra`</summary>

```text
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
sy8.pfb>
Output written on paper.pdf (10 pages, 245985 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c63eaff-de47-4ebc-8337-4308a28289c3",
  "isSidechain": false,
  "promptId": "c5460e05-f609-42c9-9ad5-28993b47482a",
  "type": "user",
  "uuid": "cc4f3b88-1d3f-4fca-a38c-b0defcaf7fed",
  "toolUseResult": {
    "stdout": "live/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nsy8.pfb>\nOutput written on paper.pdf (10 pages, 245985 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7c63eaff-de47-4ebc-8337-4308a28289c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T23:25:12.936Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WRYZ7gLjF6ZEV4Nagstx1u`</summary>

```json
{
  "command": "grep -c \"Warning\" /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median/paper.log | head -1; grep \"Error\" /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median/paper.log | head -5",
  "description": "Check for LaTeX errors/warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc4f3b88-1d3f-4fca-a38c-b0defcaf7fed",
  "isSidechain": false,
  "requestId": "req_011CbEge8SLnw7drExU8szDH",
  "type": "assistant",
  "uuid": "8fb83162-121c-4480-a9d7-3d9e515b8163",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FwJrRCsj9LPcgKVQuAkG2D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 422,
      "cache_read_input_tokens": 68808,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 422,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 191,
          "cache_read_input_tokens": 68808,
          "cache_creation_input_tokens": 422,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 422
          },
          "type": "message"
        }
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

_source line 34 · 2026-05-20T23:25:13.002Z_

<details><summary>↩ Tool result · `toolu_01WRYZ7gLjF6ZEV4Nagstx1u`</summary>

```text
1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fb83162-121c-4480-a9d7-3d9e515b8163",
  "isSidechain": false,
  "promptId": "c5460e05-f609-42c9-9ad5-28993b47482a",
  "type": "user",
  "uuid": "3fe01888-e9c8-407f-b2fb-b2cc50b0881d",
  "toolUseResult": {
    "stdout": "1",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "8fb83162-121c-4480-a9d7-3d9e515b8163",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-20T23:25:29.174Z_

编译成功，无错误。`paper.pdf` 为 10 页，245KB，包含：

- **Abstract** + **Introduction**（4段 + 3贡献）
- **Related Work**（4段，覆盖方差源文献、G-theory、IRT、训练不稳定性）
- **Framework and Method**（G-theory公式、9个实验设计、模型/基础设施/评分指标说明）
- **Results**（10个子节，覆盖全部9个实验）：
  - 4.1 MMLU方差分解（Tables 1-2）
  - 4.2 Item重采样稳定性（Table 3）
  - 4.3 跨基准方差结构 + MATH扩展（Tables 4-5）
  - 4.4 Model-as-Facet重分析 + Bootstrap CI（Tables 6-7）
  - 4.5 硬件面分析（Table 8）
  - 4.6 D-Study可复现性预算（Table 9）
  - 4.7 评分指标敏感性（Table 10）
  - 4.8 估计方法敏感性（Table 11）
  - 4.9 14B规模扩展（Table 12）
  - 4.10 Fine-tuning方差（Table 13）
  - 4.11 LayerCast精度缓解（Table 14）
  - 5-Benchmark汇总表（Table 15）
- **Discussion**（5段 + Limitations）
- **Conclusion** + 18条参考文献

所有定量数据来自 `experiment_data.json`，按 narrative guidance 使用 "benchmark-conditional variance structure" 和 "task-type clustering" 而非 "systematic gradient"。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fe01888-e9c8-407f-b2fb-b2cc50b0881d",
  "isSidechain": false,
  "requestId": "req_011CbEgeWNwjmGUgdLnamr9B",
  "type": "assistant",
  "uuid": "2a190aa9-cc39-46d1-a050-20551a5e19aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CyQaMpuoPqiZdUpF3B7Z5i",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 204,
      "cache_read_input_tokens": 69230,
      "output_tokens": 485,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 485,
          "cache_read_input_tokens": 69230,
          "cache_creation_input_tokens": 204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 204
          },
          "type": "message"
        }
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

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T222113 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheo…",
  "leafUuid": "2a190aa9-cc39-46d1-a050-20551a5e19aa",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulation paper for dream_20260520T222113",
  "sessionId": "67977da3-950c-4fc5-98d2-407cc2c60bff"
}
```

---
