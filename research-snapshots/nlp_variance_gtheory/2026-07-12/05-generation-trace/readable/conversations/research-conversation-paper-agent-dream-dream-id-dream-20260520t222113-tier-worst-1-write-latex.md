# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T222113 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-3/504e3b83-20e3-4523-8138-37f4c7478640.jsonl`
- **Structured JSON:** [`3586f581e952e4d084aa.json`](../../sessions/35/3586f581e952e4d084aa.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T23:25:30.925Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T23:25:30.925Z",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T222113 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：核心framing从\"cross-benchmark variance gradient\"转向\"方差归因本身不可靠——variance decomposition is a measurement, not a fact\"。\nexp-001b的item重采样不稳定性（CV=33%）成为paper centerpiece。三个Claims全部reframe：\nClaim 1 → \"item dominance估计是sample-unstable的（CV>30%），单次方差分解——包括所有prior work——过度承诺归因确定性\"\nClaim 2 → \"model×item交互（33%）是最大的被忽视项；treating model as fixed系统性误归因方差到item_id；separability在binary scoring下也不完全成立\"\nClaim 3 → \"reproducibility budgets必须包含对budget本身的uncertainty quantification——当前D-study projections跨benchmark收敛（range仅60 items），消灭benchmark-specific budgets贡献，但CI宽度(±190 items)说明budget本身需要error bars\"\nCross-benchmark gradient不成立（spread仅9pp，方向不符合knowledge→reasoning递减预测——GSM8K item_id=42%反而高于MMLU=38%）。\n新hook：\"We set out to build reproducibility budgets for LLM evaluation and discovered that the budget itself is unreliable.\"\nTimeline滑到ACL ARR October以容纳reframing和额外resampling实验。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T23:25:30.928Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T23:25:30.928Z",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640"
}
```

---

## Round 1

32 recorded events

### User

_source line 3 · 2026-05-20T23:25:30.957Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T222113 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：核心framing从"cross-benchmark variance gradient"转向"方差归因本身不可靠——variance decomposition is a measurement, not a fact"。
exp-001b的item重采样不稳定性（CV=33%）成为paper centerpiece。三个Claims全部reframe：
Claim 1 → "item dominance估计是sample-unstable的（CV>30%），单次方差分解——包括所有prior work——过度承诺归因确定性"
Claim 2 → "model×item交互（33%）是最大的被忽视项；treating model as fixed系统性误归因方差到item_id；separability在binary scoring下也不完全成立"
Claim 3 → "reproducibility budgets必须包含对budget本身的uncertainty quantification——当前D-study projections跨benchmark收敛（range仅60 items），消灭benchmark-specific budgets贡献，但CI宽度(±190 items)说明budget本身需要error bars"
Cross-benchmark gradient不成立（spread仅9pp，方向不符合knowledge→reasoning递减预测——GSM8K item_id=42%反而高于MMLU=38%）。
新hook："We set out to build reproducibility budgets for LLM evaluation and discovered that the budget itself is unreliable."
Timeline滑到ACL ARR October以容纳reframing和额外resampling实验。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "373fec7c-0384-4178-9c36-2cd6143072a3",
  "type": "user",
  "uuid": "51871f6e-1d60-40ea-937a-77cd6021c762",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T23:25:30.956Z_

```json
{
  "parentUuid": "51871f6e-1d60-40ea-937a-77cd6021c762",
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
  "uuid": "ccf49c3a-611e-4724-ac55-44d95924acdd",
  "timestamp": "2026-05-20T23:25:30.956Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T23:25:30.956Z_

```json
{
  "parentUuid": "ccf49c3a-611e-4724-ac55-44d95924acdd",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ed2b4f57-e999-4158-b603-d9751183a1be",
  "timestamp": "2026-05-20T23:25:30.956Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640",
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
  "aiTitle": "Generate worst-tier dream paper for NLP variance study",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640"
}
```

---

### Assistant

_source line 7 · 2026-05-20T23:25:33.952Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed2b4f57-e999-4158-b603-d9751183a1be",
  "isSidechain": false,
  "requestId": "req_011CbEgfqEYaRj7NjUmsyDX4",
  "type": "assistant",
  "uuid": "7db28be6-c355-46d3-8d8b-86025a3d0036",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NS9Kr6PXbHYzdC3vznLmm9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11694,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11694,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11694
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

_source line 8 · 2026-05-20T23:25:34.452Z_

<details open><summary>🔧 Tool call — Read · `toolu_01J3Y5gJHt5bH3aoa6KyuWmk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7db28be6-c355-46d3-8d8b-86025a3d0036",
  "isSidechain": false,
  "requestId": "req_011CbEgfqEYaRj7NjUmsyDX4",
  "type": "assistant",
  "uuid": "de0a54b7-77e9-48c6-934a-4e78382fcf59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NS9Kr6PXbHYzdC3vznLmm9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11694,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11694,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11694
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

_source line 9 · 2026-05-20T23:25:34.749Z_

<details><summary>↩ Tool result · `toolu_01J3Y5gJHt5bH3aoa6KyuWmk`</summary>

```text
1	[
2	  {
3	    "name": "Full-scale precision study (confound-fixed, model-as-fixed)",
4	    "description": "4 models × 3 precisions × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items, V0 enforce_eager。Model-as-fixed分析产出point estimates；后续exp-004的model-as-facet reanalysis将彻底改变解读。",
5	    "results": {
6	      "total_records": 172800,
7	      "total_conditions": 1296,
8	      "item_variance_share_pooled": 0.378,
9	      "item_variance_share_qwen3_8b": 0.422,
10	      "item_variance_share_llama31_8b": 0.358,
11	      "item_variance_share_gemma2_9b": 0.401,
12	      "item_variance_share_mistral_7b": 0.303,
13	      "residual_share_pooled": 0.202,
14	      "precision_main_effect": 0.016,
15	      "precision_item_interaction": 0.045,
16	      "prompt_item_interaction": 0.052,
17	      "temperature_item_interaction": 0.058,
18	      "seed_item_interaction": 0.016,
19	      "ordering_item_interaction": 0.012,
20	      "prompt_main_effect": 0.007,
21	      "temperature_main_effect": 0.01,
22	      "seed_main_effect": 0.003,
23	      "ordering_main_effect": 0.002,
24	      "precision_temperature_binary": 0.015,
25	      "infra_x_method_binary_mmlu": 0.015,
26	      "accuracy_fp32": 0.668,
27	      "accuracy_bf16": 0.672,
28	      "accuracy_fp16": 0.67,
29	      "g_coefficient_correct": 0.32,
30	      "cross_model_item_variance_cv": 0.13
31	    },
32	    "tables": [
33	      {
34	        "name": "Table 1: Variance Components (model-as-fixed pooled, MMLU binary)",
35	        "columns": [
36	          "Component",
37	          "Qwen3-8B",
38	          "Llama-3.1-8B",
39	          "Gemma-2-9B",
40	          "Mistral-7B",
41	          "Pooled"
42	        ],
43	        "rows": [
44	          [
45	            "item_id",
46	            "42.2%",
47	            "35.8%",
48	            "40.1%",
49	            "30.3%",
50	            "37.8%"
51	          ],
52	          [
53	            "residual",
54	            "17.4%",
55	            "21.2%",
56	            "18.8%",
57	            "26.1%",
58	            "20.2%"
59	          ],
60	          [
61	            "temperature:item",
62	            "6.3%",
63	            "5.9%",
64	            "5.2%",
65	            "5.8%",
66	            "5.8%"
67	          ],
68	          [
69	            "prompt:item",
70	            "5.8%",
71	            "5.4%",
72	            "4.8%",
73	            "4.2%",
74	            "5.2%"
75	          ],
76	          [
77	            "precision:item",
78	            "4.9%",
79	            "4.6%",
80	            "4.2%",
81	            "3.8%",
82	            "4.5%"
83	          ],
84	          [
85	            "seed:item",
86	            "1.8%",
87	            "1.7%",
88	            "1.4%",
89	            "1.3%",
90	            "1.6%"
91	          ],
92	          [
93	            "ordering:item",
94	            "1.4%",
95	            "1.2%",
96	            "1.1%",
97	            "0.9%",
98	            "1.2%"
99	          ],
100	          [
101	            "precision",
102	            "1.8%",
103	            "1.7%",
104	            "1.5%",
105	            "1.3%",
106	            "1.6%"
107	          ],
108	          [
109	            "temperature",
110	            "1.2%",
111	            "1.0%",
112	            "0.9%",
113	            "0.8%",
114	            "1.0%"
115	          ],
116	          [
117	            "prompt",
118	            "0.8%",
119	            "0.7%",
120	            "0.6%",
121	            "0.5%",
122	            "0.7%"
123	          ],
124	          [
125	            "precision:temperature",
126	            "1.6%",
127	            "1.5%",
128	            "1.4%",
129	            "1.2%",
130	            "1.5%"
131	          ],
132	          [
133	            "all other",
134	            "14.8%",
135	            "19.3%",
136	            "20.0%",
137	            "23.8%",
138	            "18.9%"
139	          ]
140	        ]
141	      },
142	      {
143	        "name": "Table 2: Accuracy by Precision (post-confound-fix)",
144	        "columns": [
145	          "Model",
146	          "FP32",
147	          "BF16",
148	          "FP16",
149	          "Max Δ"
150	        ],
151	        "rows": [
152	          [
153	            "Qwen3-8B",
154	            "0.680",
155	            "0.684",
156	            "0.682",
157	            "0.004"
158	          ],
159	          [
160	            "Llama-3.1-8B",
161	            "0.660",
162	            "0.664",
163	            "0.662",
164	            "0.004"
165	          ],
166	          [
167	            "Gemma-2-9B",
168	            "0.706",
169	            "0.710",
170	            "0.708",
171	            "0.004"
172	          ],
173	          [
174	            "Mistral-7B",
175	            "0.622",
176	            "0.626",
177	            "0.624",
178	            "0.004"
179	          ]
180	        ]
181	      }
182	    ],
183	    "figures": [],
184	    "analysis": "表面支持item dominance（38% pooled），但这是一个unstable point estimate。Cross-model CV=13%暗示model×item问题。exp-001b和exp-004将分别从resampling stability和model-as-facet两个角度瓦解这个数字。Precision×temperature=1.5%开始动摇separability claim但尚未decisive。\n\n\nConfound修复后precision主效应从MVP的夸大水平降至1.6%，三种精度accuracy收敛到66.8-67.2%。Item_id在model-as-fixed分析中仍为最大成分（37.8% pooled），表面上支持Claim 1。但四个模型间item_id的变异（30.3-42.2%，CV=13%）已暗示model×item交互的重要性——Mistral-7B仅30.3%（sliding window attention+不同tokenizer覆盖率改变item-model关系），Qwen3-8B最高42.2%。\nG=0.32反映binary scoring下低reliability：200 items不足以压制item×facet交互。\n关键陷阱：这些point estimates看起来支持item dominance narrative，但exp-001b将显示它们对item selection高度敏感（CV=33%），exp-004将显示model-as-fixed分析系统性膨胀item_id（38%→15%）。此阶段的所有table都是\"misleading precision\"的例证。\ninfra×method binary在MMLU上1.5%——高于MVP的<0.5%但尚未breaks separability。200 items（vs MVP的50）包含更多borderline items，precision差异在这些items上翻转binary outcome。\n"
185	  },
186	  {
187	    "name": "Item resampling stability test (paper centerpiece)",
188	    "description": "3组独立stratified MMLU 200-item samples（seeds 0, 7, 99）× Llama-3.1-8B × 3 precisions × 3 prompts × 3 seeds × 2 orderings = 54 conditions/sample。测试item dominance的抽样稳定性。",
189	    "results": {
190	      "item_variance_sample_seed0": 0.48,
191	      "item_variance_sample_seed7": 0.25,
192	      "item_variance_sample_seed99": 0.41,
193	      "item_variance_mean": 0.38,
194	      "item_variance_sd": 0.12,
195	      "item_resample_cv": 0.33,
196	      "residual_sample_seed0": 0.16,
197	      "residual_sample_seed7": 0.3,
198	      "residual_sample_seed99": 0.19,
199	      "g_coefficient_sample_seed0": 0.28,
200	      "g_coefficient_sample_seed7": 0.38,
201	      "g_coefficient_sample_seed99": 0.31,
202	      "g_coefficient_cv": 0.16,
203	      "variance_component_rank_order_stable": false,
204	      "rank_inversions_across_samples": 3,
205	      "bootstrap_ci_item_id_width": 0.21,
206	      "bootstrap_ci_item_id_lower": 0.27,
207	      "bootstrap_ci_item_id_upper": 0.48,
208	      "conditions_per_sample": 54,
209	      "total_records_per_sample": 10800
210	    },
211	    "tables": [
212	      {
213	        "name": "Table 3: Variance Decomposition Across Item Samples (Llama-3.1-8B, MMLU)",
214	        "columns": [
215	          "Component",
216	          "Sample 0",
217	          "Sample 7",
218	          "Sample 99",
219	          "Mean",
220	          "SD",
221	          "CV"
222	        ],
223	        "rows": [
224	          [
225	            "item_id",
226	            "48.0%",
227	            "25.0%",
228	            "41.0%",
229	            "38.0%",
230	            "12.0%",
231	            "0.33"
232	          ],
233	          [
234	            "residual",
235	            "16.0%",
236	            "30.0%",
237	            "19.0%",
238	            "21.7%",
239	            "7.5%",
240	            "0.35"
241	          ],
242	          [
243	            "temperature:item",
244	            "7.2%",
245	            "9.8%",
246	            "8.1%",
247	            "8.4%",
248	            "1.3%",
249	            "0.16"
250	          ],
251	          [
252	            "prompt:item",
253	            "5.6%",
254	            "8.2%",
255	            "6.4%",
256	            "6.7%",
257	            "1.3%",
258	            "0.20"
259	          ],
260	          [
261	            "precision:item",
262	            "4.8%",
263	            "6.4%",
264	            "5.2%",
265	            "5.5%",
266	            "0.8%",
267	            "0.15"
268	          ],
269	          [
270	            "temperature",
271	            "1.0%",
272	            "2.4%",
273	            "1.4%",
274	            "1.6%",
275	            "0.7%",
276	            "0.46"
277	          ],
278	          [
279	            "prompt",
280	            "0.6%",
281	            "1.8%",
282	            "0.9%",
283	            "1.1%",
284	            "0.6%",
285	            "0.58"
286	          ],
287	          [
288	            "all other",
289	            "16.8%",
290	            "16.4%",
291	            "18.0%",
292	            "17.1%",
293	            "0.8%",
294	            "0.05"
295	          ]
296	        ]
297	      },
298	      {
299	        "name": "Table 4: G-coefficient and Rank Stability Across Item Samples",
300	        "columns": [
301	          "Metric",
302	          "Sample 0",
303	          "Sample 7",
304	          "Sample 99"
305	        ],
306	        "rows": [
307	          [
308	            "G (correct)",
309	            "0.28",
310	            "0.38",
311	            "0.31"
312	          ],
313	          [
314	            "Largest component",
315	            "item_id",
316	            "residual",
317	            "item_id"
318	          ],
319	          [
320	            "2nd largest",
321	            "residual",
322	            "item_id",
323	            "residual"
324	          ],
325	          [
326	            "3rd largest",
327	            "temp:item",
328	            "temp:item",
329	            "temp:item"
330	          ],
331	          [
332	            "Item difficulty SD",
333	            "0.31",
334	            "0.22",
335	            "0.27"
336	          ],
337	          [
338	            "Bimodality index",
339	            "0.71",
340	            "0.38",
341	            "0.58"
342	          ]
343	        ]
344	      }
345	    ],
346	    "figures": [],
347	    "analysis": "Worst档paper的核心发现。Prior work（Mesting 2026、Brittlebench 2026、Bouthillier et al. 2021）都报告单次方差分解的point estimates作为\"findings\"，但从未测试resampling stability。CV=33%说明：如果Mesting用不同的200个items，她的43.8% judge dominance数字可能变成30%或55%。\n新narrative：\"方差分解不是fact而是measurement——和所有measurement一样有自己的measurement error。当前文献忽略了这个error，导致过度自信的归因声明。\"\n\n\n三组不同的200-item stratified samples产出质性不同的方差分解。CV=33%意味着item dominance point estimate在25-48%间波动。\nSample seed 7抽到更多中等难度items（difficulty集中在0.4-0.6），这些items的model responses跨conditions更一致，item_id仅25%；sample seed 0抽到更多极难和极易items（bimodal difficulty），这些items天然有高item-level variance，推高item_id至48%。MMLU的57个subjects有非常不同的difficulty distributions——STEM subjects（abstract algebra, college physics）bimodal，humanities subjects更uniform。200-item stratified sampling在subject层面balanced，但subject内部的item selection对方差结构有质性影响。\n更具破坏性的是：方差component的RANK ORDER在三组samples间不稳定。Sample 7中residual（30%）超过item_id（25%）成为最大成分，产生3次rank inversion。\"Item selection is the largest variance source\"取决于碰巧抽到了哪些items——不是stable empirical finding，而是sample-dependent measurement。\nBootstrap CI=[0.27, 0.48]，width=0.21——足够宽以至于无法区分\"item dominance\"（>40%）和\"item is one of several comparable sources\"（~25%）。\n"
348	  },
349	  {
350	    "name": "Multi-benchmark replication (no systematic gradient)",
351	    "description": "4 models × 2 precisions × 6 prompts × 6 seeds × 2 temperatures × 4 orderings on GSM8K/ARC-Challenge/HellaSwag各200 items。",
352	    "results": {
353	      "item_variance_gsm8k": 0.42,
354	      "item_variance_arc": 0.36,
355	      "item_variance_hellaswag": 0.33,
356	      "item_variance_mmlu_ref": 0.378,
357	      "cross_benchmark_gradient_spread_pp": 9,
358	      "gradient_direction": "non-monotonic",
359	      "gradient_follows_prediction": false,
360	      "residual_gsm8k": 0.22,
361	      "residual_arc": 0.2,
362	      "residual_hellaswag": 0.18,
363	      "temperature_item_gsm8k": 0.08,
364	      "temperature_item_arc": 0.06,
365	      "temperature_item_hellaswag": 0.07,
366	      "seed_item_gsm8k": 0.06,
367	      "seed_item_arc": 0.04,
368	      "seed_item_hellaswag": 0.05,
369	      "prompt_item_gsm8k": 0.05,
370	      "prompt_item_arc": 0.07,
371	      "prompt_item_hellaswag": 0.04,
372	      "infra_x_method_binary_gsm8k": 0.045,
373	      "infra_x_method_binary_arc": 0.02,
374	      "infra_x_method_binary_hellaswag": 0.035,
375	      "g_coefficient_gsm8k": 0.3,
376	      "g_coefficient_arc": 0.35,
377	      "g_coefficient_hellaswag": 0.36,
378	      "benchmarks_with_item_as_largest": 3,
379	      "total_records_per_benchmark": 76800
380	    },
381	    "tables": [
382	      {
383	        "name": "Table 5: Item Dominance Across Benchmarks (model-as-fixed)",
384	        "columns": [
385	          "Benchmark",
386	          "item_id",
387	          "residual",
388	          "temp:item",
389	          "prompt:item",
390	          "seed:item",
391	          "G"
392	        ],
393	        "rows": [
394	          [
395	            "MMLU",
396	            "37.8%",
397	            "20.2%",
398	            "5.8%",
399	            "5.2%",
400	            "1.6%",
401	            "0.32"
402	          ],
403	          [
404	            "GSM8K",
405	            "42.0%",
406	            "22.0%",
407	            "8.0%",
408	            "5.0%",
409	            "6.0%",
410	            "0.30"
411	          ],
412	          [
413	            "ARC-Challenge",
414	            "36.0%",
415	            "20.0%",
416	            "6.0%",
417	            "7.0%",
418	            "4.0%",
419	            "0.35"
420	          ],
421	          [
422	            "HellaSwag",
423	            "33.0%",
424	            "18.0%",
425	            "7.0%",
426	            "4.0%",
427	            "5.0%",
428	            "0.36"
429	          ],
430	          [
431	            "Spread",
432	            "9pp",
433	            "4pp",
434	            "2pp",
435	            "3pp",
436	            "4pp",
437	            "—"
438	          ]
439	        ]
440	      },
441	      {
442	        "name": "Table 6: Separability Test (binary scoring)",
443	        "columns": [
444	          "Benchmark",
445	          "precision×prompt",
446	          "precision×seed",
447	          "precision×temp",
448	          "Total infra×method"
449	        ],
450	        "rows": [
451	          [
452	            "MMLU",
453	            "0.3%",
454	            "0.2%",
455	            "1.0%",
456	            "1.5%"
457	          ],
458	          [
459	            "GSM8K",
460	            "1.2%",
461	            "1.5%",
462	            "1.8%",
463	            "4.5%"
464	          ],
465	          [
466	            "ARC-Challenge",
467	            "0.4%",
468	            "0.3%",
469	            "1.3%",
470	            "2.0%"
471	          ],
472	          [
473	            "HellaSwag",
474	            "0.8%",
475	            "1.0%",
476	            "1.7%",
477	            "3.5%"
478	          ]
479	        ]
480	      },
481	      {
482	        "name": "Table 7: Gradient Prediction vs Observation",
483	        "columns": [
484	          "Predicted",
485	          "Observed",
486	          "Match"
487	        ],
488	        "rows": [
489	          [
490	            "MMLU > ARC > GSM8K (knowledge→reasoning递减)",
491	            "GSM8K > MMLU > ARC > HellaSwag",
492	            "No"
493	          ],
494	          [
495	            "Monotonic decrease with reasoning load",
496	            "Non-monotonic",
497	            "No"
498	          ],
499	          [
500	            "Spread > 15pp for meaningful gradient",
501	            "Spread = 9pp",
502	            "No"
503	          ]
504	        ]
505	      }
506	    ],
507	    "figures": [],
508	    "analysis": "Cross-benchmark gradient是original framing的primary contribution，在worst档下完全不成立：(1) direction错误（GSM8K>MMLU），(2) spread太小（9pp），(3) 叠加resampling instability后spread在noise range内。\n但separability breaking提供新material：binary scoring下infra×method不是universally negligible的。\nReframe：从\"gradient exists\"变为\"gradient doesn't exist, and that's the finding\"——variance structure的benchmark variation不follow任何simple predictive axis，variance attribution depends on item difficulty distribution shape而非task taxonomy。\n\n\nCross-benchmark gradient不成立。GSM8K的item dominance（42%）反而高于MMLU（37.8%），颠覆\"knowledge→reasoning item dominance递减\"预测。原因：GSM8K的200-item sample中difficulty variance极大——从简单单步算术（accuracy>95%）到复杂多步word problems（accuracy<15%），这个bimodal difficulty distribution推高item_id。在8B-class models上，大量GSM8K items要么trivially easy要么完全超出能力，ceiling/floor效应增加item-level variance。\nHellaSwag item dominance最低（33%），不是因为\"reasoning\"（它是commonsense completion），而是其items的difficulty distribution更uniform（大多数items对8B models难度中等），减少了item-level variance。\nSpread=42%-33%=9pp，在[0,12]内。关键：ordering为GSM8K>MMLU>ARC>HellaSwag，不符合任何simple knowledge-reasoning axis。叠加exp-001b的resampling instability（CV>30%），9pp spread完全在noise range内。\nSeparability在binary scoring下breaks on GSM8K（infra×method=4.5%）和HellaSwag（3.5%）。GSM8K因precision差异影响CoT中numerical computation；HellaSwag因completion scoring对token-level probability的precision敏感。\n"
509	  },
510	  {
511	    "name": "Multi-hardware G-study",
512	    "description": "4 models × 2 GPU types × 2 precisions × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。Hardware×methodology interaction核心测试。",
513	    "results": {
514	      "hardware_main_effect": 0.05,
515	      "hardware_item_interaction": 0.06,
516	      "hardware_precision_interaction": 0.035,
517	      "hardware_methodology_interaction": 0.04,
518	      "hardware_seed_interaction": 0.02,
519	      "hardware_temperature_interaction": 0.015,
520	      "total_hardware_related_variance": 0.14,
521	      "infra_x_method_binary_with_hardware": 0.055,
522	      "separability_holds": false,
523	      "accuracy_gpu1_bf16": 0.672,
524	      "accuracy_gpu2_bf16": 0.668,
525	      "accuracy_delta_cross_hardware": 0.004,
526	      "item_id_with_hardware_facet": 0.33,
527	      "g_coefficient_with_hardware": 0.28,
528	      "total_records": 230400
529	    },
530	    "tables": [
531	      {
532	        "name": "Table 8: Hardware-Related Variance Components (MMLU binary)",
533	        "columns": [
534	          "Component",
535	          "Variance Share",
536	          "95% Bootstrap CI"
537	        ],
538	        "rows": [
539	          [
540	            "hardware (main)",
541	            "5.0%",
542	            "[3.2%, 7.1%]"
543	          ],
544	          [
545	            "hardware:item",
546	            "6.0%",
547	            "[4.1%, 8.3%]"
548	          ],
549	          [
550	            "hardware:precision",
551	            "3.5%",
552	            "[2.0%, 5.2%]"
553	          ],
554	          [
555	            "hardware:prompt",
556	            "1.5%",
557	            "[0.8%, 2.4%]"
558	          ],
559	          [
560	            "hardware:seed",
561	            "2.0%",
562	            "[1.2%, 3.1%]"
563	          ],
564	          [
565	            "hardware:temperature",
566	            "1.5%",
567	            "[0.7%, 2.5%]"
568	          ],
569	          [
570	            "item_id (with hardware)",
571	            "33.0%",
572	            "[25.1%, 41.8%]"
573	          ],
574	          [
575	            "residual",
576	            "18.0%",
577	            "[14.2%, 22.5%]"
578	          ]
579	        ]
580	      },
581	      {
582	        "name": "Table 9: Separability With vs Without Hardware",
583	        "columns": [
584	          "Interaction",
585	          "Single-GPU (exp-001)",
586	          "Multi-GPU (exp-003)",
587	          "Separability"
588	        ],
589	        "rows": [
590	          [
591	            "infra×method (binary)",
592	            "1.5%",
593	            "5.5%",
594	            "FAILS (>3%)"
595	          ],
596	          [
597	            "precision×temperature",
598	            "1.5%",
599	            "1.5%",
600	            "marginal"
601	          ],
602	          [
603	            "hardware×methodology",
604	            "N/A",
605	            "4.0%",
606	            "FAILS"
607	          ],
608	          [
609	            "hardware×precision",
610	            "N/A",
611	            "3.5%",
612	            "FAILS"
613	          ]
614	        ]
615	      }
616	    ],
617	    "figures": [],
618	    "analysis": "对Claim 2（separability）致命打击。Hardware crossing不仅没confirm separability反而breaks it——infra×method从1.5%跳到5.5%。\n更深层implication：每增加一个之前被忽略的facet，item_id估计就下降（37.8%→33%），暗示item_id是\"catch-all\"——它吸收所有未建模facet的方差。这与exp-004的model-as-facet发现平行。\n\n\n两种GPU架构在BF16/FP16下产出不同accuracy（Δ=0.4pp），因为不同GPU的tensor core实现、CUDA kernel调度、floating-point rounding behavior不同。Hardware main=5%通过hardware×item（6%）放大：某些items在两块GPU上的correct/incorrect判定不同，这些items的logit margin接近decision boundary，GPU-specific numerical noise翻转outcome。\nHardware×methodology=4%直接breaks Claim 2：methodology因子的效应是hardware-conditional的——同一prompt在GPU1上增加accuracy 2pp，在GPU2上可能降低1pp。Infrastructure和methodology不可分离。\nHardware×precision=3.5%说明precision choice的影响也是GPU-dependent的——BF16在GPU1上比FP16好，GPU2上可能相反。\nTotal hardware-related variance=14%，大于precision-related（~6%），说明hardware是比precision更重要但被忽视的方差来源。Item_id从exp-001的37.8%降至33%——single-GPU design系统性高估item dominance，hardware×item被misattributed to item_id。\n"
619	  },
620	  {
621	    "name": "Comprehensive analysis (model-as-facet + bootstrap + D-study)",
622	    "description": "合并exp-001/001b/002/003数据。Model-as-facet reanalysis、bootstrap CIs、D-study projections、REML sensitivity、ranking stability。",
623	    "results": {
624	      "item_id_model_fixed": 0.378,
625	      "item_id_model_crossed": 0.152,
626	      "model_main_effect": 0.06,
627	      "model_x_item_mmlu": 0.33,
628	      "model_x_prompt": 0.02,
629	      "model_x_temperature": 0.015,
630	      "residual_model_crossed": 0.12,
631	      "bootstrap_ci_item_id_fixed": "[0.27, 0.48]",
632	      "bootstrap_ci_item_id_crossed": "[0.08, 0.23]",
633	      "bootstrap_ci_model_x_item": "[0.24, 0.42]",
634	      "bootstrap_ci_width_item_id": 0.21,
635	      "rank_stability_across_bootstraps": 0.68,
636	      "bootstraps_item_id_largest": 0.45,
637	      "bootstraps_model_x_item_largest": 0.38,
638	      "bootstraps_residual_largest": 0.17,
639	      "dstudy_items_g90_mmlu": 480,
640	      "dstudy_items_g90_gsm8k": 420,
641	      "dstudy_items_g90_arc": 450,
642	      "dstudy_items_g90_hellaswag": 440,
643	      "dstudy_cross_benchmark_range": 60,
644	      "dstudy_ci_width_mmlu": 180,
645	      "dstudy_ci_width_gsm8k": 200,
646	      "reml_henderson_divergence_item_id_pp": 5.7,
647	      "model_ranking_flips": 4
648	    },
649	    "tables": [
650	      {
651	        "name": "Table 10: Model-Fixed vs Model-Crossed (MMLU binary)",
652	        "columns": [
653	          "Component",
654	          "Model-Fixed",
655	          "Model-Crossed",
656	          "Δ",
657	          "Interpretation"
658	        ],
659	        "rows": [
660	          [
661	            "item_id",
662	            "37.8%",
663	            "15.2%",
664	            "-22.6pp",
665	            "misattributed to model×item"
666	          ],
667	          [
668	            "model×item",
669	            "—",
670	            "33.0%",
671	            "+33.0pp",
672	            "largest single component"
673	          ],
674	          [
675	            "model (main)",
676	            "—",
677	            "6.0%",
678	            "+6.0pp",
679	            "between-model differences"
680	          ],
681	          [
682	            "residual",
683	            "20.2%",
684	            "12.0%",
685	            "-8.2pp",
686	            "decomposed into model terms"
687	          ],
688	          [
689	            "temp:item",
690	            "5.8%",
691	            "4.5%",
692	            "-1.3pp",
693	            "slight reallocation"
694	          ],
695	          [
696	            "prompt:item",
697	            "5.2%",
698	            "4.0%",
699	            "-1.2pp",
700	            "slight reallocation"
701	          ],
702	          [
703	            "all other",
704	            "31.0%",
705	            "25.3%",
706	            "-5.7pp",
707	            "redistributed"
708	          ]
709	        ]
710	      },
711	      {
712	        "name": "Table 11: Bootstrap Ranking Stability (1000 resamples)",
713	        "columns": [
714	          "Component",
715	          "Times #1",
716	          "Times #2",
717	          "Times #3",
718	          "Mean Rank"
719	        ],
720	        "rows": [
721	          [
722	            "item_id (model-fixed)",
723	            "450",
724	            "320",
725	            "180",
726	            "1.7"
727	          ],
728	          [
729	            "model×item",
730	            "380",
731	            "350",
732	            "200",
733	            "1.8"
734	          ],
735	          [
736	            "residual",
737	            "170",
738	            "330",
739	            "350",
740	            "2.4"
741	          ]
742	        ]
743	      },
744	      {
745	        "name": "Table 12: D-study Items for G≥0.90",
746	        "columns": [
747	          "Benchmark",
748	          "Point Estimate",
749	          "Bootstrap 95% CI",
750	          "CI Width"
751	        ],
752	        "rows": [
753	          [
754	            "MMLU",
755	            "480",
756	            "[380, 560]",
757	            "180"
758	          ],
759	          [
760	            "GSM8K",
761	            "420",
762	            "[310, 510]",
763	            "200"
764	          ],
765	          [
766	            "ARC",
767	            "450",
768	            "[350, 540]",
769	            "190"
770	          ],
771	          [
772	            "HellaSwag",
773	            "440",
774	            "[340, 530]",
775	            "190"
776	          ],
777	          [
778	            "Cross-benchmark range",
779	            "60",
780	            "—",
781	            "—"
782	          ]
783	        ]
784	      },
785	      {
786	        "name": "Table 13: REML vs Henderson Method I",
787	        "columns": [
788	          "Component",
789	          "Henderson",
790	          "REML",
791	          "Δ"
792	        ],
793	        "rows": [
794	          [
795	            "item_id",
796	            "37.8%",
797	            "32.1%",
798	            "-5.7pp"
799	          ],
800	          [
801	            "model×item",
802	            "33.0%",
803	            "35.2%",
804	            "+2.2pp"
805	          ],
806	          [
807	            "residual",
808	            "20.2%",
809	            "22.8%",
810	            "+2.6pp"
811	          ]
812	        ]
813	      }
814	    ],
815	    "figures": [],
816	    "analysis": "三个Claims全面清算：\nClaim 1：item_id 38%→15%（model-crossed），bootstrap ranking不稳定。\"Item dominance\"是specification artifact。\nClaim 2：separability数据来自exp-001/003，此处model×item的大小说明\"item dominance\"本身不是对separability test的正确framing。\nClaim 3：D-study跨benchmark收敛（range=60 items vs CI width=190 items），消灭benchmark-specific uniqueness。但CIs极宽——budget需要自己的uncertainty quantification，成为新meta-methodological contribution。\n\n\nModel-as-facet reanalysis是worst档的核心打击。Model从fixed变为crossed random facet，item_id从37.8%暴跌至15.2%——差值大部分被model×item interaction（33%）吸收。解读：prior work treating model as fixed，系统性地将model-specific item难度差异misattributed to \"item difficulty\"。一个item在Qwen3上easy但Mistral上hard——这不是item difficulty，而是model×item interaction。Model×item=33%意味着item\"难度\"不是items的intrinsic property，而是item-model pair的joint property，从根本上质疑IRT和G-theory中\"item difficulty is a stable attribute\"的假设。\nBootstrap CIs devastating：item_id (model-fixed) CI=[0.27, 0.48], width=0.21。45%的bootstrap samples中item_id是largest，38%中model×item是largest。Component ranking本身不稳定——无法reliably claim任何single component \"dominates\"。\nD-study projections跨benchmark CONVERGE：G≥0.90需要的items在MMLU(480)、GSM8K(420)、ARC(450)、HellaSwag(440)上差异仅60 items。CI宽度（180-200 items）远大于cross-benchmark range，benchmark间差异statistically indistinguishable。这消灭了\"benchmark-specific budgets\"贡献。\nREML vs Henderson Method I在item_id上分歧5.7pp（REML=32.1%, Henderson=37.8%），estimation method choice也是方差来源，支撑meta-methodological argument。\nModel ranking stability：precision×temperature在4个model-pair comparisons中翻转ranking——即使\"small\" interactions也有practical significance for model comparison。\n"
817	  },
818	  {
819	    "name": "14B model extension",
820	    "description": "Qwen3-14B和DeepSeek-R1-Distill-14B at BF16/FP16。模型规模和architecture对方差结构的影响。",
821	    "results": {
822	      "item_variance_qwen3_14b": 0.32,
823	      "item_variance_deepseek_r1_14b": 0.28,
824	      "residual_qwen3_14b": 0.22,
825	      "residual_deepseek_r1_14b": 0.26,
826	      "model_x_item_with_14b": 0.38,
827	      "model_x_item_increase_vs_8b_only": 0.05,
828	      "temperature_item_deepseek_r1": 0.1,
829	      "seed_item_deepseek_r1": 0.08,
830	      "g_coefficient_pooled_with_14b": 0.28,
831	      "architecture_scale_confounded": true
832	    },
833	    "tables": [
834	      {
835	        "name": "Table 14: 8B vs 14B Variance Structure",
836	        "columns": [
837	          "Component",
838	          "8B Pooled",
839	          "Qwen3-14B",
840	          "DeepSeek-R1-14B",
841	          "All Crossed"
842	        ],
843	        "rows": [
844	          [
845	            "item_id (model-fixed)",
846	            "37.8%",
847	            "32.0%",
848	            "28.0%",
849	            "34.0%"
850	          ],
851	          [
852	            "model×item (crossed)",
853	            "33.0%",
854	            "—",
855	            "—",
856	            "38.0%"
857	          ],
858	          [
859	            "residual",
860	            "20.2%",
861	            "22.0%",
862	            "26.0%",
863	            "16.0%"
864	          ],
865	          [
866	            "temp:item",
867	            "5.8%",
868	            "5.0%",
869	            "10.0%",
870	            "6.5%"
871	          ],
872	          [
873	            "seed:item",
874	            "1.6%",
875	            "1.4%",
876	            "8.0%",
877	            "3.2%"
878	          ]
879	        ]
880	      }
881	    ],
882	    "figures": [],
883	    "analysis": "加剧model×item问题而非缓解。DeepSeek-R1的异常方差结构展示architecture对方差分解的质性影响。作为supplementary evidence，一段话足够。\n\n\n14B模型的item dominance（Qwen3-14B=32%, DeepSeek-R1=28%）低于8B pooled（37.8%），但scale effect与architecture confounded——DeepSeek-R1-Distill是reasoning-distilled模型，lower item dominance可能来自reasoning chain随机性（temp:item=10%, seed:item=8%远高于8B average）而非scale。\n加入14B后model×item从33%增至38%——8B和14B模型在items上difficulty ranking更不一致（14B solve了很多8B无法solve的items），增加model×item方差。进一步支撑\"item difficulty is a model×item property not an item property\"。\n但n=2个14B模型统计力不足，hardware confound未排除。\n"
884	  },
885	  {
886	    "name": "Fine-tuning G-study (RoBERTa)",
887	    "description": "RoBERTa-large on SST-2/MNLI/RTE/COPA。6 seeds × 3 lr × 4 shuffles × 3 GPUs × 2 precisions = 432 runs/task × 4 tasks = 1728 runs。",
888	    "results": {
889	      "item_variance_sst2": 0.14,
890	      "item_variance_mnli": 0.11,
891	      "item_variance_rte": 0.19,
892	      "item_variance_copa": 0.07,
893	      "learning_rate_main_avg": 0.168,
894	      "seed_main_avg": 0.09,
895	      "data_shuffle_main_avg": 0.058,
896	      "precision_main_avg": 0.021,
897	      "gpu_main_avg": 0.03,
898	      "lr_seed_interaction_avg": 0.11,
899	      "lr_item_interaction_avg": 0.075,
900	      "residual_avg": 0.2,
901	      "g_coefficient_sst2": 0.52,
902	      "g_coefficient_rte": 0.45,
903	      "g_coefficient_copa": 0.32,
904	      "inference_training_correlation": 0.18,
905	      "cross_task_stable": false,
906	      "item_id_resampling_cv_finetuning": 0.28
907	    },
908	    "tables": [
909	      {
910	        "name": "Table 15: Fine-tuning Variance Decomposition",
911	        "columns": [
912	          "Component",
913	          "SST-2",
914	          "MNLI",
915	          "RTE",
916	          "COPA",
917	          "Average"
918	        ],
919	        "rows": [
920	          [
921	            "learning_rate",
922	            "15.0%",
923	            "19.0%",
924	            "17.0%",
925	            "16.0%",
926	            "16.8%"
927	          ],
928	          [
929	            "residual",
930	            "18.0%",
931	            "20.0%",
932	            "19.0%",
933	            "23.0%",
934	            "20.0%"
935	          ],
936	          [
937	            "item_id",
938	            "14.0%",
939	            "11.0%",
940	            "19.0%",
941	            "7.0%",
942	            "12.8%"
943	          ],
944	          [
945	            "lr:seed",
946	            "11.0%",
947	            "12.0%",
948	            "10.0%",
949	            "11.0%",
950	            "11.0%"
951	          ],
952	          [
953	            "seed",
954	            "9.0%",
955	            "8.0%",
956	            "10.0%",
957	            "9.0%",
958	            "9.0%"
959	          ],
960	          [
961	            "lr:item",
962	            "8.0%",
963	            "7.0%",
964	            "6.0%",
965	            "9.0%",
966	            "7.5%"
967	          ],
968	          [
969	            "data_shuffle",
970	            "6.0%",
971	            "5.0%",
972	            "5.0%",
973	            "7.0%",
974	            "5.8%"
975	          ],
976	          [
977	            "seed:item",
978	            "5.0%",
979	            "4.0%",
980	            "4.0%",
981	            "6.0%",
982	            "4.8%"
983	          ],
984	          [
985	            "gpu",
986	            "3.0%",
987	            "3.0%",
988	            "3.0%",
989	            "3.0%",
990	            "3.0%"
991	          ],
992	          [
993	            "precision",
994	            "2.0%",
995	            "2.5%",
996	            "1.8%",
997	            "2.2%",
998	            "2.1%"
999	          ],
1000	          [
1001	            "all other",
1002	            "9.0%",
1003	            "8.5%",
1004	            "5.2%",
1005	            "6.8%",
1006	            "7.4%"
1007	          ]
1008	        ]
1009	      },
1010	      {
1011	        "name": "Table 16: Inference vs Fine-tuning",
1012	        "columns": [
1013	          "Metric",
1014	          "Value"
1015	        ],
1016	        "rows": [
1017	          [
1018	            "Pearson r (variance shares)",
1019	            "0.18"
1020	          ],
1021	          [
1022	            "Spearman ρ (component ranks)",
1023	            "0.22"
1024	          ],
1025	          [
1026	            "Largest in inference",
1027	            "item_id (37.8%)"
1028	          ],
1029	          [
1030	            "Largest in fine-tuning",
1031	            "learning_rate (16.8%)"
1032	          ],
1033	          [
1034	            "item_id rank shift",
1035	            "1st → 3rd"
1036	          ]
1037	        ]
1038	      }
1039	    ],
1040	    "figures": [],
1041	    "analysis": "Fine-tuning结果在worst档下ambivalent。Learning rate dominance和inference-training decorrelation是novel。但如果paper的argument是\"variance decomposition is unreliable\"，则fine-tuning也受质疑。\nViable framing：fine-tuning作为ADDITIONAL EVIDENCE for instability——不同analysis contexts产出qualitatively different results。作为supporting evidence有价值，但不是standalone contribution。\n\n\nFine-tuning方差结构与inference fundamentally不同——learning rate dominance（16.8%）取代item dominance。但worst档下fine-tuning也exhibit不稳定性：cross-task structure不consistent（SST-2 item=14% vs COPA item=7%），item_id resampling CV=28%（低于inference的33%但仍substantial）。\nLearning rate dominance expected——不同lr通向不同loss landscape basins，每个basin对每个item有不同prediction。lr:seed=11%说明optimization landscape随机性irreducible。GPU main=3%是novel finding——fine-tuning中GPU difference通过gradient accumulation被amplified（thousands of steps中compound），比inference hardware effect更大。\nInference-training correlation=0.18意味着inference-based reproducibility analysis不能generalize到training。但如果整个variance decomposition methodology的reliability已被质疑（exp-001b/004），fine-tuning results也受同样质疑——这是double-edged的。\n"
1042	  },
1043	  {
1044	    "name": "LayerCast precision mitigation",
1045	    "description": "LayerCast（FP16 storage + FP32 compute）作为第4种precision条件on MMLU。",
1046	    "results": {
1047	      "layercast_accuracy": 0.671,
1048	      "layercast_vs_bf16_delta": 0.001,
1049	      "variance_reduction_vs_fp16": 0.002,
1050	      "precision_component_4level": 0.013,
1051	      "precision_item_4level": 0.04,
1052	      "practical_significance": "negligible"
1053	    },
1054	    "tables": [
1055	      {
1056	        "name": "Table 17: Precision Conditions Including LayerCast",
1057	        "columns": [
1058	          "Condition",
1059	          "Accuracy",
1060	          "Precision Share",
1061	          "Precision:item Share"
1062	        ],
1063	        "rows": [
1064	          [
1065	            "FP32",
1066	            "0.668",
1067	            "—",
1068	            "—"
1069	          ],
1070	          [
1071	            "BF16",
1072	            "0.672",
1073	            "—",
1074	            "—"
1075	          ],
1076	          [
1077	            "FP16",
1078	            "0.670",
1079	            "—",
1080	            "—"
1081	          ],
1082	          [
1083	            "LayerCast",
1084	            "0.671",
1085	            "—",
1086	            "—"
1087	          ],
1088	          [
1089	            "4-level precision",
1090	            "—",
1091	            "1.3%",
1092	            "4.0%"
1093	          ]
1094	        ]
1095	      }
1096	    ],
1097	    "figures": [],
1098	    "analysis": "Null result。一句mention：\"LayerCast addresses <2% of total variance, confirming precision is not a first-order concern once engine confounds are controlled。\"不值得paper space。\n\n\nConfound修复后precision main effect已极小（1.6%），LayerCast额外收益微乎其微。LayerCast accuracy=0.671介于FP16和BF16之间，Δ<0.2pp。在worst档narrative（方差分解本身不可靠）下，precision mitigation targeting一个1.6%的component完全irrelevant——即使完全消除precision variance，其他components的instability仍dominate。\n"
1099	  },
1100	  {
1101	    "name": "MATH benchmark extension",
1102	    "description": "MATH 200 items，测试extreme reasoning task是否延续gradient pattern。",
1103	    "results": {
1104	      "item_variance_math": 0.38,
1105	      "residual_math": 0.24,
1106	      "temperature_item_math": 0.09,
1107	      "seed_item_math": 0.07,
1108	      "temperature_main_math": 0.04,
1109	      "seed_main_math": 0.03,
1110	      "prompt_item_math": 0.04,
1111	      "g_coefficient_math": 0.28,
1112	      "items_needed_g90_math": 520,
1113	      "gradient_with_math": "still non-monotonic",
1114	      "gradient_spread_5bench_pp": 9,
1115	      "difficulty_bimodality_index": 0.7,
1116	      "bimodality_item_id_correlation": 0.95
1117	    },
1118	    "tables": [
1119	      {
1120	        "name": "Table 18: Full 5-Benchmark Spectrum",
1121	        "columns": [
1122	          "Benchmark",
1123	          "Type",
1124	          "item_id",
1125	          "residual",
1126	          "temp:item",
1127	          "seed:item",
1128	          "G",
1129	          "Items G≥0.90"
1130	        ],
1131	        "rows": [
1132	          [
1133	            "MMLU",
1134	            "Knowledge",
1135	            "37.8%",
1136	            "20.2%",
1137	            "5.8%",
1138	            "1.6%",
1139	            "0.32",
1140	            "480"
1141	          ],
1142	          [
1143	            "GSM8K",
1144	            "Math",
1145	            "42.0%",
1146	            "22.0%",
1147	            "8.0%",
1148	            "6.0%",
1149	            "0.30",
1150	            "420"
1151	          ],
1152	          [
1153	            "ARC",
1154	            "Science",
1155	            "36.0%",
1156	            "20.0%",
1157	            "6.0%",
1158	            "4.0%",
1159	            "0.35",
1160	            "450"
1161	          ],
1162	          [
1163	            "HellaSwag",
1164	            "Commonsense",
1165	            "33.0%",
1166	            "18.0%",
1167	            "7.0%",
1168	            "5.0%",
1169	            "0.36",
1170	            "440"
1171	          ],
1172	          [
1173	            "MATH",
1174	            "Hard reasoning",
1175	            "38.0%",
1176	            "24.0%",
1177	            "9.0%",
1178	            "7.0%",
1179	            "0.28",
1180	            "520"
1181	          ]
1182	        ]
1183	      },
1184	      {
1185	        "name": "Table 19: Difficulty Distribution Predicts Item Dominance",
1186	        "columns": [
1187	          "Benchmark",
1188	          "Difficulty SD",
1189	          "Bimodality Index",
1190	          "item_id"
1191	        ],
1192	        "rows": [
1193	          [
1194	            "GSM8K",
1195	            "0.34",
1196	            "0.72",
1197	            "42.0%"
1198	          ],
1199	          [
1200	            "MATH",
1201	            "0.33",
1202	            "0.70",
1203	            "38.0%"
1204	          ],
1205	          [
1206	            "MMLU",
1207	            "0.30",
1208	            "0.65",
1209	            "37.8%"
1210	          ],
1211	          [
1212	            "ARC",
1213	            "0.27",
1214	            "0.52",
1215	            "36.0%"
1216	          ],
1217	          [
1218	            "HellaSwag",
1219	            "0.22",
1220	            "0.38",
1221	            "33.0%"
1222	          ],
1223	          [
1224	            "r with item_id",
1225	            "r=0.92",
1226	            "r=0.95",
1227	            "—"
1228	          ]
1229	        ]
1230	      }
1231	    ],
1232	    "figures": [],
1233	    "analysis": "MATH cements non-gradient finding。但Table 19意外产出positive value：bimodality→item_id的strong correlation是novel mechanistic insight——item dominance is predictable from difficulty distribution shape, not from task taxonomy。在worst档下，这是paper可以claim的少数positive findings之一。\n\nMATH item dominance=38%——与MMLU几乎identical，彻底否定gradient。原因：MATH的200-item sample包含高度bimodal difficulty（Level 1-2: accuracy>80%; Level 4-5: accuracy<10%），extreme bimodality推高item_id，counteracting CoT randomness的预期effect。\n关键insight：item dominance不是task type的function，而是item difficulty distribution shape的function。Bimodal distributions（无论来源——MMLU的subject heterogeneity还是MATH的difficulty levels）inflate item_id；unimodal distributions（HellaSwag）suppress它。5-benchmark ordering: GSM8K(42%)>MMLU=MATH(38%)>ARC(36%)>HellaSwag(33%)，spread=9pp，无systematic pattern。\nBimodality index与item_id的correlation r=0.95是一个strong mechanistic finding——prior work未identify bimodality作为item variance contribution的predictor。这在worst档下是一个positive sub-finding。\nD-study G≥0.90需要520 items，与其他benchmarks（420-480）comparable，进一步支持convergence。\n"
1234	  }
1235	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de0a54b7-77e9-48c6-934a-4e78382fcf59",
  "isSidechain": false,
  "promptId": "373fec7c-0384-4178-9c36-2cd6143072a3",
  "type": "user",
  "uuid": "7989be7e-dc2b-4af5-a648-e08016f5cd6e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Full-scale precision study (confound-fixed, model-as-fixed)\",\n    \"description\": \"4 models × 3 precisions × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items, V0 enforce_eager。Model-as-fixed分析产出point estimates；后续exp-004的model-as-facet reanalysis将彻底改变解读。\",\n    \"results\": {\n      \"total_records\": 172800,\n      \"total_conditions\": 1296,\n      \"item_variance_share_pooled\": 0.378,\n      \"item_variance_share_qwen3_8b\": 0.422,\n      \"item_variance_share_llama31_8b\": 0.358,\n      \"item_variance_share_gemma2_9b\": 0.401,\n      \"item_variance_share_mistral_7b\": 0.303,\n      \"residual_share_pooled\": 0.202,\n      \"precision_main_effect\": 0.016,\n      \"precision_item_interaction\": 0.045,\n      \"prompt_item_interaction\": 0.052,\n      \"temperature_item_interaction\": 0.058,\n      \"seed_item_interaction\": 0.016,\n      \"ordering_item_interaction\": 0.012,\n      \"prompt_main_effect\": 0.007,\n      \"temperature_main_effect\": 0.01,\n      \"seed_main_effect\": 0.003,\n      \"ordering_main_effect\": 0.002,\n      \"precision_temperature_binary\": 0.015,\n      \"infra_x_method_binary_mmlu\": 0.015,\n      \"accuracy_fp32\": 0.668,\n      \"accuracy_bf16\": 0.672,\n      \"accuracy_fp16\": 0.67,\n      \"g_coefficient_correct\": 0.32,\n      \"cross_model_item_variance_cv\": 0.13\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Variance Components (model-as-fixed pooled, MMLU binary)\",\n        \"columns\": [\n          \"Component\",\n          \"Qwen3-8B\",\n          \"Llama-3.1-8B\",\n          \"Gemma-2-9B\",\n          \"Mistral-7B\",\n          \"Pooled\"\n        ],\n        \"rows\": [\n          [\n            \"item_id\",\n            \"42.2%\",\n            \"35.8%\",\n            \"40.1%\",\n            \"30.3%\",\n            \"37.8%\"\n          ],\n          [\n            \"residual\",\n            \"17.4%\",\n            \"21.2%\",\n            \"18.8%\",\n            \"26.1%\",\n            \"20.2%\"\n          ],\n          [\n            \"temperature:item\",\n            \"6.3%\",\n            \"5.9%\",\n            \"5.2%\",\n            \"5.8%\",\n            \"5.8%\"\n          ],\n          [\n            \"prompt:item\",\n            \"5.8%\",\n            \"5.4%\",\n            \"4.8%\",\n            \"4.2%\",\n            \"5.2%\"\n          ],\n          [\n            \"precision:item\",\n            \"4.9%\",\n            \"4.6%\",\n            \"4.2%\",\n            \"3.8%\",\n            \"4.5%\"\n          ],\n          [\n            \"seed:item\",\n            \"1.8%\",\n            \"1.7%\",\n            \"1.4%\",\n            \"1.3%\",\n            \"1.6%\"\n          ],\n          [\n            \"ordering:item\",\n            \"1.4%\",\n            \"1.2%\",\n            \"1.1%\",\n            \"0.9%\",\n            \"1.2%\"\n          ],\n          [\n            \"precision\",\n            \"1.8%\",\n            \"1.7%\",\n            \"1.5%\",\n            \"1.3%\",\n            \"1.6%\"\n          ],\n          [\n            \"temperature\",\n            \"1.2%\",\n            \"1.0%\",\n            \"0.9%\",\n            \"0.8%\",\n            \"1.0%\"\n          ],\n          [\n            \"prompt\",\n            \"0.8%\",\n            \"0.7%\",\n            \"0.6%\",\n            \"0.5%\",\n            \"0.7%\"\n          ],\n          [\n            \"precision:temperature\",\n            \"1.6%\",\n            \"1.5%\",\n            \"1.4%\",\n            \"1.2%\",\n            \"1.5%\"\n          ],\n          [\n            \"all other\",\n            \"14.8%\",\n            \"19.3%\",\n            \"20.0%\",\n            \"23.8%\",\n            \"18.9%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: Accuracy by Precision (post-confound-fix)\",\n        \"columns\": [\n          \"Model\",\n          \"FP32\",\n          \"BF16\",\n          \"FP16\",\n          \"Max Δ\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B\",\n            \"0.680\",\n            \"0.684\",\n            \"0.682\",\n            \"0.004\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            \"0.660\",\n            \"0.664\",\n            \"0.662\",\n            \"0.004\"\n          ],\n          [\n            \"Gemma-2-9B\",\n            \"0.706\",\n            \"0.710\",\n            \"0.708\",\n            \"0.004\"\n          ],\n          [\n            \"Mistral-7B\",\n            \"0.622\",\n            \"0.626\",\n            \"0.624\",\n            \"0.004\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"表面支持item dominance（38% pooled），但这是一个unstable point estimate。Cross-model CV=13%暗示model×item问题。exp-001b和exp-004将分别从resampling stability和model-as-facet两个角度瓦解这个数字。Precision×temperature=1.5%开始动摇separability claim但尚未decisive。\\n\\n\\nConfound修复后precision主效应从MVP的夸大水平降至1.6%，三种精度accuracy收敛到66.8-67.2%。Item_id在model-as-fixed分析中仍为最大成分（37.8% pooled），表面上支持Claim 1。但四个模型间item_id的变异（30.3-42.2%，CV=13%）已暗示model×item交互的重要性——Mistral-7B仅30.3%（sliding window attention+不同tokenizer覆盖率改变item-model关系），Qwen3-8B最高42.2%。\\nG=0.32反映binary scoring下低reliability：200 items不足以压制item×facet交互。\\n关键陷阱：这些point estimates看起来支持item dominance narrative，但exp-001b将显示它们对item selection高度敏感（CV=33%），exp-004将显示model-as-fixed分析系统性膨胀item_id（38%→15%）。此阶段的所有table都是\\\"misleading precision\\\"的例证。\\ninfra×method binary在MMLU上1.5%——高于MVP的<0.5%但尚未breaks separability。200 items（vs MVP的50）包含更多borderline items，precision差异在这些items上翻转binary outcome。\\n\"\n  },\n  {\n    \"name\": \"Item resampling stability test (paper centerpiece)\",\n    \"description\": \"3组独立stratified MMLU 200-item samples（seeds 0, 7, 99）× Llama-3.1-8B × 3 precisions × 3 prompts × 3 seeds × 2 orderings = 54 conditions/sample。测试item dominance的抽样稳定性。\",\n    \"results\": {\n      \"item_variance_sample_seed0\": 0.48,\n      \"item_variance_sample_seed7\": 0.25,\n      \"item_variance_sample_seed99\": 0.41,\n      \"item_variance_mean\": 0.38,\n      \"item_variance_sd\": 0.12,\n      \"item_resample_cv\": 0.33,\n      \"residual_sample_seed0\": 0.16,\n      \"residual_sample_seed7\": 0.3,\n      \"residual_sample_seed99\": 0.19,\n      \"g_coefficient_sample_seed0\": 0.28,\n      \"g_coefficient_sample_seed7\": 0.38,\n      \"g_coefficient_sample_seed99\": 0.31,\n      \"g_coefficient_cv\": 0.16,\n      \"variance_component_rank_order_stable\": false,\n      \"rank_inversions_across_samples\": 3,\n      \"bootstrap_ci_item_id_width\": 0.21,\n      \"bootstrap_ci_item_id_lower\": 0.27,\n      \"bootstrap_ci_item_id_upper\": 0.48,\n      \"conditions_per_sample\": 54,\n      \"total_records_per_sample\": 10800\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Variance Decomposition Across Item Samples (Llama-3.1-8B, MMLU)\",\n        \"columns\": [\n          \"Component\",\n          \"Sample 0\",\n          \"Sample 7\",\n          \"Sample 99\",\n          \"Mean\",\n          \"SD\",\n          \"CV\"\n        ],\n        \"rows\": [\n          [\n            \"item_id\",\n            \"48.0%\",\n            \"25.0%\",\n            \"41.0%\",\n            \"38.0%\",\n            \"12.0%\",\n            \"0.33\"\n          ],\n          [\n            \"residual\",\n            \"16.0%\",\n            \"30.0%\",\n            \"19.0%\",\n            \"21.7%\",\n            \"7.5%\",\n            \"0.35\"\n          ],\n          [\n            \"temperature:item\",\n            \"7.2%\",\n            \"9.8%\",\n            \"8.1%\",\n            \"8.4%\",\n            \"1.3%\",\n            \"0.16\"\n          ],\n          [\n            \"prompt:item\",\n            \"5.6%\",\n            \"8.2%\",\n            \"6.4%\",\n            \"6.7%\",\n            \"1.3%\",\n            \"0.20\"\n          ],\n          [\n            \"precision:item\",\n            \"4.8%\",\n            \"6.4%\",\n            \"5.2%\",\n            \"5.5%\",\n            \"0.8%\",\n            \"0.15\"\n          ],\n          [\n            \"temperature\",\n            \"1.0%\",\n            \"2.4%\",\n            \"1.4%\",\n            \"1.6%\",\n            \"0.7%\",\n            \"0.46\"\n          ],\n          [\n            \"prompt\",\n            \"0.6%\",\n            \"1.8%\",\n            \"0.9%\",\n            \"1.1%\",\n            \"0.6%\",\n            \"0.58\"\n          ],\n          [\n            \"all other\",\n            \"16.8%\",\n            \"16.4%\",\n            \"18.0%\",\n            \"17.1%\",\n            \"0.8%\",\n            \"0.05\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 4: G-coefficient and Rank Stability Across Item Samples\",\n        \"columns\": [\n          \"Metric\",\n          \"Sample 0\",\n          \"Sample 7\",\n          \"Sample 99\"\n        ],\n        \"rows\": [\n          [\n            \"G (correct)\",\n            \"0.28\",\n            \"0.38\",\n            \"0.31\"\n          ],\n          [\n            \"Largest component\",\n            \"item_id\",\n            \"residual\",\n            \"item_id\"\n          ],\n          [\n            \"2nd largest\",\n            \"residual\",\n            \"item_id\",\n            \"residual\"\n          ],\n          [\n            \"3rd largest\",\n            \"temp:item\",\n            \"temp:item\",\n            \"temp:item\"\n          ],\n          [\n            \"Item difficulty SD\",\n            \"0.31\",\n            \"0.22\",\n            \"0.27\"\n          ],\n          [\n            \"Bimodality index\",\n            \"0.71\",\n            \"0.38\",\n            \"0.58\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Worst档paper的核心发现。Prior work（Mesting 2026、Brittlebench 2026、Bouthillier et al. 2021）都报告单次方差分解的point estimates作为\\\"findings\\\"，但从未测试resampling stability。CV=33%说明：如果Mesting用不同的200个items，她的43.8% judge dominance数字可能变成30%或55%。\\n新narrative：\\\"方差分解不是fact而是measurement——和所有measurement一样有自己的measurement error。当前文献忽略了这个error，导致过度自信的归因声明。\\\"\\n\\n\\n三组不同的200-item stratified samples产出质性不同的方差分解。CV=33%意味着item dominance point estimate在25-48%间波动。\\nSample seed 7抽到更多中等难度items（difficulty集中在0.4-0.6），这些items的model responses跨conditions更一致，item_id仅25%；sample seed 0抽到更多极难和极易items（bimodal difficulty），这些items天然有高item-level variance，推高item_id至48%。MMLU的57个subjects有非常不同的difficulty distributions——STEM subjects（abstract algebra, college physics）bimodal，humanities subjects更uniform。200-item stratified sampling在subject层面balanced，但subject内部的item selection对方差结构有质性影响。\\n更具破坏性的是：方差component的RANK ORDER在三组samples间不稳定。Sample 7中residual（30%）超过item_id（25%）成为最大成分，产生3次rank inversion。\\\"Item selection is the largest variance source\\\"取决于碰巧抽到了哪些items——不是stable empirical finding，而是sample-dependent measurement。\\nBootstrap CI=[0.27, 0.48]，width=0.21——足够宽以至于无法区分\\\"item dominance\\\"（>40%）和\\\"item is one of several comparable sources\\\"（~25%）。\\n\"\n  },\n  {\n    \"name\": \"Multi-benchmark replication (no systematic gradient)\",\n    \"description\": \"4 models × 2 precisions × 6 prompts × 6 seeds × 2 temperatures × 4 orderings on GSM8K/ARC-Challenge/HellaSwag各200 items。\",\n    \"results\": {\n      \"item_variance_gsm8k\": 0.42,\n      \"item_variance_arc\": 0.36,\n      \"item_variance_hellaswag\": 0.33,\n      \"item_variance_mmlu_ref\": 0.378,\n      \"cross_benchmark_gradient_spread_pp\": 9,\n      \"gradient_direction\": \"non-monotonic\",\n      \"gradient_follows_prediction\": false,\n      \"residual_gsm8k\": 0.22,\n      \"residual_arc\": 0.2,\n      \"residual_hellaswag\": 0.18,\n      \"temperature_item_gsm8k\": 0.08,\n      \"temperature_item_arc\": 0.06,\n      \"temperature_item_hellaswag\": 0.07,\n      \"seed_item_gsm8k\": 0.06,\n      \"seed_item_arc\": 0.04,\n      \"seed_item_hellaswag\": 0.05,\n      \"prompt_item_gsm8k\": 0.05,\n      \"prompt_item_arc\": 0.07,\n      \"prompt_item_hellaswag\": 0.04,\n      \"infra_x_method_binary_gsm8k\": 0.045,\n      \"infra_x_method_binary_arc\": 0.02,\n      \"infra_x_method_binary_hellaswag\": 0.035,\n      \"g_coefficient_gsm8k\": 0.3,\n      \"g_coefficient_arc\": 0.35,\n      \"g_coefficient_hellaswag\": 0.36,\n      \"benchmarks_with_item_as_largest\": 3,\n      \"total_records_per_benchmark\": 76800\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: Item Dominance Across Benchmarks (model-as-fixed)\",\n        \"columns\": [\n          \"Benchmark\",\n          \"item_id\",\n          \"residual\",\n          \"temp:item\",\n          \"prompt:item\",\n          \"seed:item\",\n          \"G\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            \"37.8%\",\n            \"20.2%\",\n            \"5.8%\",\n            \"5.2%\",\n            \"1.6%\",\n            \"0.32\"\n          ],\n          [\n            \"GSM8K\",\n            \"42.0%\",\n            \"22.0%\",\n            \"8.0%\",\n            \"5.0%\",\n            \"6.0%\",\n            \"0.30\"\n          ],\n          [\n            \"ARC-Challenge\",\n            \"36.0%\",\n            \"20.0%\",\n            \"6.0%\",\n            \"7.0%\",\n            \"4.0%\",\n            \"0.35\"\n          ],\n          [\n            \"HellaSwag\",\n            \"33.0%\",\n            \"18.0%\",\n            \"7.0%\",\n            \"4.0%\",\n            \"5.0%\",\n            \"0.36\"\n          ],\n          [\n            \"Spread\",\n            \"9pp\",\n            \"4pp\",\n            \"2pp\",\n            \"3pp\",\n            \"4pp\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 6: Separability Test (binary scoring)\",\n        \"columns\": [\n          \"Benchmark\",\n          \"precision×prompt\",\n          \"precision×seed\",\n          \"precision×temp\",\n          \"Total infra×method\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            \"0.3%\",\n            \"0.2%\",\n            \"1.0%\",\n            \"1.5%\"\n          ],\n          [\n            \"GSM8K\",\n            \"1.2%\",\n            \"1.5%\",\n            \"1.8%\",\n            \"4.5%\"\n          ],\n          [\n            \"ARC-Challenge\",\n            \"0.4%\",\n            \"0.3%\",\n            \"1.3%\",\n            \"2.0%\"\n          ],\n          [\n            \"HellaSwag\",\n            \"0.8%\",\n            \"1.0%\",\n            \"1.7%\",\n            \"3.5%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 7: Gradient Prediction vs Observation\",\n        \"columns\": [\n          \"Predicted\",\n          \"Observed\",\n          \"Match\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU > ARC > GSM8K (knowledge→reasoning递减)\",\n            \"GSM8K > MMLU > ARC > HellaSwag\",\n            \"No\"\n          ],\n          [\n            \"Monotonic decrease with reasoning load\",\n            \"Non-monotonic\",\n            \"No\"\n          ],\n          [\n            \"Spread > 15pp for meaningful gradient\",\n            \"Spread = 9pp\",\n            \"No\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-benchmark gradient是original framing的primary contribution，在worst档下完全不成立：(1) direction错误（GSM8K>MMLU），(2) spread太小（9pp），(3) 叠加resampling instability后spread在noise range内。\\n但separability breaking提供新material：binary scoring下infra×method不是universally negligible的。\\nReframe：从\\\"gradient exists\\\"变为\\\"gradient doesn't exist, and that's the finding\\\"——variance structure的benchmark variation不follow任何simple predictive axis，variance attribution depends on item difficulty distribution shape而非task taxonomy。\\n\\n\\nCross-benchmark gradient不成立。GSM8K的item dominance（42%）反而高于MMLU（37.8%），颠覆\\\"knowledge→reasoning item dominance递减\\\"预测。原因：GSM8K的200-item sample中difficulty variance极大——从简单单步算术（accuracy>95%）到复杂多步word problems（accuracy<15%），这个bimodal difficulty distribution推高item_id。在8B-class models上，大量GSM8K items要么trivially easy要么完全超出能力，ceiling/floor效应增加item-level variance。\\nHellaSwag item dominance最低（33%），不是因为\\\"reasoning\\\"（它是commonsense completion），而是其items的difficulty distribution更uniform（大多数items对8B models难度中等），减少了item-level variance。\\nSpread=42%-33%=9pp，在[0,12]内。关键：ordering为GSM8K>MMLU>ARC>HellaSwag，不符合任何simple knowledge-reasoning axis。叠加exp-001b的resampling instability（CV>30%），9pp spread完全在noise range内。\\nSeparability在binary scoring下breaks on GSM8K（infra×method=4.5%）和HellaSwag（3.5%）。GSM8K因precision差异影响CoT中numerical computation；HellaSwag因completion scoring对token-level probability的precision敏感。\\n\"\n  },\n  {\n    \"name\": \"Multi-hardware G-study\",\n    \"description\": \"4 models × 2 GPU types × 2 precisions × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。Hardware×methodology interaction核心测试。\",\n    \"results\": {\n      \"hardware_main_effect\": 0.05,\n      \"hardware_item_interaction\": 0.06,\n      \"hardware_precision_interaction\": 0.035,\n      \"hardware_methodology_interaction\": 0.04,\n      \"hardware_seed_interaction\": 0.02,\n      \"hardware_temperature_interaction\": 0.015,\n      \"total_hardware_related_variance\": 0.14,\n      \"infra_x_method_binary_with_hardware\": 0.055,\n      \"separability_holds\": false,\n      \"accuracy_gpu1_bf16\": 0.672,\n      \"accuracy_gpu2_bf16\": 0.668,\n      \"accuracy_delta_cross_hardware\": 0.004,\n      \"item_id_with_hardware_facet\": 0.33,\n      \"g_coefficient_with_hardware\": 0.28,\n      \"total_records\": 230400\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Hardware-Related Variance Components (MMLU binary)\",\n        \"columns\": [\n          \"Component\",\n          \"Variance Share\",\n          \"95% Bootstrap CI\"\n        ],\n        \"rows\": [\n          [\n            \"hardware (main)\",\n            \"5.0%\",\n            \"[3.2%, 7.1%]\"\n          ],\n          [\n            \"hardware:item\",\n            \"6.0%\",\n            \"[4.1%, 8.3%]\"\n          ],\n          [\n            \"hardware:precision\",\n            \"3.5%\",\n            \"[2.0%, 5.2%]\"\n          ],\n          [\n            \"hardware:prompt\",\n            \"1.5%\",\n            \"[0.8%, 2.4%]\"\n          ],\n          [\n            \"hardware:seed\",\n            \"2.0%\",\n            \"[1.2%, 3.1%]\"\n          ],\n          [\n            \"hardware:temperature\",\n            \"1.5%\",\n            \"[0.7%, 2.5%]\"\n          ],\n          [\n            \"item_id (with hardware)\",\n            \"33.0%\",\n            \"[25.1%, 41.8%]\"\n          ],\n          [\n            \"residual\",\n            \"18.0%\",\n            \"[14.2%, 22.5%]\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 9: Separability With vs Without Hardware\",\n        \"columns\": [\n          \"Interaction\",\n          \"Single-GPU (exp-001)\",\n          \"Multi-GPU (exp-003)\",\n          \"Separability\"\n        ],\n        \"rows\": [\n          [\n            \"infra×method (binary)\",\n            \"1.5%\",\n            \"5.5%\",\n            \"FAILS (>3%)\"\n          ],\n          [\n            \"precision×temperature\",\n            \"1.5%\",\n            \"1.5%\",\n            \"marginal\"\n          ],\n          [\n            \"hardware×methodology\",\n            \"N/A\",\n            \"4.0%\",\n            \"FAILS\"\n          ],\n          [\n            \"hardware×precision\",\n            \"N/A\",\n            \"3.5%\",\n            \"FAILS\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"对Claim 2（separability）致命打击。Hardware crossing不仅没confirm separability反而breaks it——infra×method从1.5%跳到5.5%。\\n更深层implication：每增加一个之前被忽略的facet，item_id估计就下降（37.8%→33%），暗示item_id是\\\"catch-all\\\"——它吸收所有未建模facet的方差。这与exp-004的model-as-facet发现平行。\\n\\n\\n两种GPU架构在BF16/FP16下产出不同accuracy（Δ=0.4pp），因为不同GPU的tensor core实现、CUDA kernel调度、floating-point rounding behavior不同。Hardware main=5%通过hardware×item（6%）放大：某些items在两块GPU上的correct/incorrect判定不同，这些items的logit margin接近decision boundary，GPU-specific numerical noise翻转outcome。\\nHardware×methodology=4%直接breaks Claim 2：methodology因子的效应是hardware-conditional的——同一prompt在GPU1上增加accuracy 2pp，在GPU2上可能降低1pp。Infrastructure和methodology不可分离。\\nHardware×precision=3.5%说明precision choice的影响也是GPU-dependent的——BF16在GPU1上比FP16好，GPU2上可能相反。\\nTotal hardware-related variance=14%，大于precision-related（~6%），说明hardware是比precision更重要但被忽视的方差来源。Item_id从exp-001的37.8%降至33%——single-GPU design系统性高估item dominance，hardware×item被misattributed to item_id。\\n\"\n  },\n  {\n    \"name\": \"Comprehensive analysis (model-as-facet + bootstrap + D-study)\",\n    \"description\": \"合并exp-001/001b/002/003数据。Model-as-facet reanalysis、bootstrap CIs、D-study projections、REML sensitivity、ranking stability。\",\n    \"results\": {\n      \"item_id_model_fixed\": 0.378,\n      \"item_id_model_crossed\": 0.152,\n      \"model_main_effect\": 0.06,\n      \"model_x_item_mmlu\": 0.33,\n      \"model_x_prompt\": 0.02,\n      \"model_x_temperature\": 0.015,\n      \"residual_model_crossed\": 0.12,\n      \"bootstrap_ci_item_id_fixed\": \"[0.27, 0.48]\",\n      \"bootstrap_ci_item_id_crossed\": \"[0.08, 0.23]\",\n      \"bootstrap_ci_model_x_item\": \"[0.24, 0.42]\",\n      \"bootstrap_ci_width_item_id\": 0.21,\n      \"rank_stability_across_bootstraps\": 0.68,\n      \"bootstraps_item_id_largest\": 0.45,\n      \"bootstraps_model_x_item_largest\": 0.38,\n      \"bootstraps_residual_largest\": 0.17,\n      \"dstudy_items_g90_mmlu\": 480,\n      \"dstudy_items_g90_gsm8k\": 420,\n      \"dstudy_items_g90_arc\": 450,\n      \"dstudy_items_g90_hellaswag\": 440,\n      \"dstudy_cross_benchmark_range\": 60,\n      \"dstudy_ci_width_mmlu\": 180,\n      \"dstudy_ci_width_gsm8k\": 200,\n      \"reml_henderson_divergence_item_id_pp\": 5.7,\n      \"model_ranking_flips\": 4\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Model-Fixed vs Model-Crossed (MMLU binary)\",\n        \"columns\": [\n          \"Component\",\n          \"Model-Fixed\",\n          \"Model-Crossed\",\n          \"Δ\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"item_id\",\n            \"37.8%\",\n            \"15.2%\",\n            \"-22.6pp\",\n            \"misattributed to model×item\"\n          ],\n          [\n            \"model×item\",\n            \"—\",\n            \"33.0%\",\n            \"+33.0pp\",\n            \"largest single component\"\n          ],\n          [\n            \"model (main)\",\n            \"—\",\n            \"6.0%\",\n            \"+6.0pp\",\n            \"between-model differences\"\n          ],\n          [\n            \"residual\",\n            \"20.2%\",\n            \"12.0%\",\n            \"-8.2pp\",\n            \"decomposed into model terms\"\n          ],\n          [\n            \"temp:item\",\n            \"5.8%\",\n            \"4.5%\",\n            \"-1.3pp\",\n            \"slight reallocation\"\n          ],\n          [\n            \"prompt:item\",\n            \"5.2%\",\n            \"4.0%\",\n            \"-1.2pp\",\n            \"slight reallocation\"\n          ],\n          [\n            \"all other\",\n            \"31.0%\",\n            \"25.3%\",\n            \"-5.7pp\",\n            \"redistributed\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 11: Bootstrap Ranking Stability (1000 resamples)\",\n        \"columns\": [\n          \"Component\",\n          \"Times #1\",\n          \"Times #2\",\n          \"Times #3\",\n          \"Mean Rank\"\n        ],\n        \"rows\": [\n          [\n            \"item_id (model-fixed)\",\n            \"450\",\n            \"320\",\n            \"180\",\n            \"1.7\"\n          ],\n          [\n            \"model×item\",\n            \"380\",\n            \"350\",\n            \"200\",\n            \"1.8\"\n          ],\n          [\n            \"residual\",\n            \"170\",\n            \"330\",\n            \"350\",\n            \"2.4\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 12: D-study Items for G≥0.90\",\n        \"columns\": [\n          \"Benchmark\",\n          \"Point Estimate\",\n          \"Bootstrap 95% CI\",\n          \"CI Width\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            \"480\",\n            \"[380, 560]\",\n            \"180\"\n          ],\n          [\n            \"GSM8K\",\n            \"420\",\n            \"[310, 510]\",\n            \"200\"\n          ],\n          [\n            \"ARC\",\n            \"450\",\n            \"[350, 540]\",\n            \"190\"\n          ],\n          [\n            \"HellaSwag\",\n            \"440\",\n            \"[340, 530]\",\n            \"190\"\n          ],\n          [\n            \"Cross-benchmark range\",\n            \"60\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 13: REML vs Henderson Method I\",\n        \"columns\": [\n          \"Component\",\n          \"Henderson\",\n          \"REML\",\n          \"Δ\"\n        ],\n        \"rows\": [\n          [\n            \"item_id\",\n            \"37.8%\",\n            \"32.1%\",\n            \"-5.7pp\"\n          ],\n          [\n            \"model×item\",\n            \"33.0%\",\n            \"35.2%\",\n            \"+2.2pp\"\n          ],\n          [\n            \"residual\",\n            \"20.2%\",\n            \"22.8%\",\n            \"+2.6pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"三个Claims全面清算：\\nClaim 1：item_id 38%→15%（model-crossed），bootstrap ranking不稳定。\\\"Item dominance\\\"是specification artifact。\\nClaim 2：separability数据来自exp-001/003，此处model×item的大小说明\\\"item dominance\\\"本身不是对separability test的正确framing。\\nClaim 3：D-study跨benchmark收敛（range=60 items vs CI width=190 items），消灭benchmark-specific uniqueness。但CIs极宽——budget需要自己的uncertainty quantification，成为新meta-methodological contribution。\\n\\n\\nModel-as-facet reanalysis是worst档的核心打击。Model从fixed变为crossed random facet，item_id从37.8%暴跌至15.2%——差值大部分被model×item interaction（33%）吸收。解读：prior work treating model as fixed，系统性地将model-specific item难度差异misattributed to \\\"item difficulty\\\"。一个item在Qwen3上easy但Mistral上hard——这不是item difficulty，而是model×item interaction。Model×item=33%意味着item\\\"难度\\\"不是items的intrinsic property，而是item-model pair的joint property，从根本上质疑IRT和G-theory中\\\"item difficulty is a stable attribute\\\"的假设。\\nBootstrap CIs devastating：item_id (model-fixed) CI=[0.27, 0.48], width=0.21。45%的bootstrap samples中item_id是largest，38%中model×item是largest。Component ranking本身不稳定——无法reliably claim任何single component \\\"dominates\\\"。\\nD-study projections跨benchmark CONVERGE：G≥0.90需要的items在MMLU(480)、GSM8K(420)、ARC(450)、HellaSwag(440)上差异仅60 items。CI宽度（180-200 items）远大于cross-benchmark range，benchmark间差异statistically indistinguishable。这消灭了\\\"benchmark-specific budgets\\\"贡献。\\nREML vs Henderson Method I在item_id上分歧5.7pp（REML=32.1%, Henderson=37.8%），estimation method choice也是方差来源，支撑meta-methodological argument。\\nModel ranking stability：precision×temperature在4个model-pair comparisons中翻转ranking——即使\\\"small\\\" interactions也有practical significance for model comparison。\\n\"\n  },\n  {\n    \"name\": \"14B model extension\",\n    \"description\": \"Qwen3-14B和DeepSeek-R1-Distill-14B at BF16/FP16。模型规模和architecture对方差结构的影响。\",\n    \"results\": {\n      \"item_variance_qwen3_14b\": 0.32,\n      \"item_variance_deepseek_r1_14b\": 0.28,\n      \"residual_qwen3_14b\": 0.22,\n      \"residual_deepseek_r1_14b\": 0.26,\n      \"model_x_item_with_14b\": 0.38,\n      \"model_x_item_increase_vs_8b_only\": 0.05,\n      \"temperature_item_deepseek_r1\": 0.1,\n      \"seed_item_deepseek_r1\": 0.08,\n      \"g_coefficient_pooled_with_14b\": 0.28,\n      \"architecture_scale_confounded\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 14: 8B vs 14B Variance Structure\",\n        \"columns\": [\n          \"Component\",\n          \"8B Pooled\",\n          \"Qwen3-14B\",\n          \"DeepSeek-R1-14B\",\n          \"All Crossed\"\n        ],\n        \"rows\": [\n          [\n            \"item_id (model-fixed)\",\n            \"37.8%\",\n            \"32.0%\",\n            \"28.0%\",\n            \"34.0%\"\n          ],\n          [\n            \"model×item (crossed)\",\n            \"33.0%\",\n            \"—\",\n            \"—\",\n            \"38.0%\"\n          ],\n          [\n            \"residual\",\n            \"20.2%\",\n            \"22.0%\",\n            \"26.0%\",\n            \"16.0%\"\n          ],\n          [\n            \"temp:item\",\n            \"5.8%\",\n            \"5.0%\",\n            \"10.0%\",\n            \"6.5%\"\n          ],\n          [\n            \"seed:item\",\n            \"1.6%\",\n            \"1.4%\",\n            \"8.0%\",\n            \"3.2%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"加剧model×item问题而非缓解。DeepSeek-R1的异常方差结构展示architecture对方差分解的质性影响。作为supplementary evidence，一段话足够。\\n\\n\\n14B模型的item dominance（Qwen3-14B=32%, DeepSeek-R1=28%）低于8B pooled（37.8%），但scale effect与architecture confounded——DeepSeek-R1-Distill是reasoning-distilled模型，lower item dominance可能来自reasoning chain随机性（temp:item=10%, seed:item=8%远高于8B average）而非scale。\\n加入14B后model×item从33%增至38%——8B和14B模型在items上difficulty ranking更不一致（14B solve了很多8B无法solve的items），增加model×item方差。进一步支撑\\\"item difficulty is a model×item property not an item property\\\"。\\n但n=2个14B模型统计力不足，hardware confound未排除。\\n\"\n  },\n  {\n    \"name\": \"Fine-tuning G-study (RoBERTa)\",\n    \"description\": \"RoBERTa-large on SST-2/MNLI/RTE/COPA。6 seeds × 3 lr × 4 shuffles × 3 GPUs × 2 precisions = 432 runs/task × 4 tasks = 1728 runs。\",\n    \"results\": {\n      \"item_variance_sst2\": 0.14,\n      \"item_variance_mnli\": 0.11,\n      \"item_variance_rte\": 0.19,\n      \"item_variance_copa\": 0.07,\n      \"learning_rate_main_avg\": 0.168,\n      \"seed_main_avg\": 0.09,\n      \"data_shuffle_main_avg\": 0.058,\n      \"precision_main_avg\": 0.021,\n      \"gpu_main_avg\": 0.03,\n      \"lr_seed_interaction_avg\": 0.11,\n      \"lr_item_interaction_avg\": 0.075,\n      \"residual_avg\": 0.2,\n      \"g_coefficient_sst2\": 0.52,\n      \"g_coefficient_rte\": 0.45,\n      \"g_coefficient_copa\": 0.32,\n      \"inference_training_correlation\": 0.18,\n      \"cross_task_stable\": false,\n      \"item_id_resampling_cv_finetuning\": 0.28\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 15: Fine-tuning Variance Decomposition\",\n        \"columns\": [\n          \"Component\",\n          \"SST-2\",\n          \"MNLI\",\n          \"RTE\",\n          \"COPA\",\n          \"Average\"\n        ],\n        \"rows\": [\n          [\n            \"learning_rate\",\n            \"15.0%\",\n            \"19.0%\",\n            \"17.0%\",\n            \"16.0%\",\n            \"16.8%\"\n          ],\n          [\n            \"residual\",\n            \"18.0%\",\n            \"20.0%\",\n            \"19.0%\",\n            \"23.0%\",\n            \"20.0%\"\n          ],\n          [\n            \"item_id\",\n            \"14.0%\",\n            \"11.0%\",\n            \"19.0%\",\n            \"7.0%\",\n            \"12.8%\"\n          ],\n          [\n            \"lr:seed\",\n            \"11.0%\",\n            \"12.0%\",\n            \"10.0%\",\n            \"11.0%\",\n            \"11.0%\"\n          ],\n          [\n            \"seed\",\n            \"9.0%\",\n            \"8.0%\",\n            \"10.0%\",\n            \"9.0%\",\n            \"9.0%\"\n          ],\n          [\n            \"lr:item\",\n            \"8.0%\",\n            \"7.0%\",\n            \"6.0%\",\n            \"9.0%\",\n            \"7.5%\"\n          ],\n          [\n            \"data_shuffle\",\n            \"6.0%\",\n            \"5.0%\",\n            \"5.0%\",\n            \"7.0%\",\n            \"5.8%\"\n          ],\n          [\n            \"seed:item\",\n            \"5.0%\",\n            \"4.0%\",\n            \"4.0%\",\n            \"6.0%\",\n            \"4.8%\"\n          ],\n          [\n            \"gpu\",\n            \"3.0%\",\n            \"3.0%\",\n            \"3.0%\",\n            \"3.0%\",\n            \"3.0%\"\n          ],\n          [\n            \"precision\",\n            \"2.0%\",\n            \"2.5%\",\n            \"1.8%\",\n            \"2.2%\",\n            \"2.1%\"\n          ],\n          [\n            \"all other\",\n            \"9.0%\",\n            \"8.5%\",\n            \"5.2%\",\n            \"6.8%\",\n            \"7.4%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 16: Inference vs Fine-tuning\",\n        \"columns\": [\n          \"Metric\",\n          \"Value\"\n        ],\n        \"rows\": [\n          [\n            \"Pearson r (variance shares)\",\n            \"0.18\"\n          ],\n          [\n            \"Spearman ρ (component ranks)\",\n            \"0.22\"\n          ],\n          [\n            \"Largest in inference\",\n            \"item_id (37.8%)\"\n          ],\n          [\n            \"Largest in fine-tuning\",\n            \"learning_rate (16.8%)\"\n          ],\n          [\n            \"item_id rank shift\",\n            \"1st → 3rd\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Fine-tuning结果在worst档下ambivalent。Learning rate dominance和inference-training decorrelation是novel。但如果paper的argument是\\\"variance decomposition is unreliable\\\"，则fine-tuning也受质疑。\\nViable framing：fine-tuning作为ADDITIONAL EVIDENCE for instability——不同analysis contexts产出qualitatively different results。作为supporting evidence有价值，但不是standalone contribution。\\n\\n\\nFine-tuning方差结构与inference fundamentally不同——learning rate dominance（16.8%）取代item dominance。但worst档下fine-tuning也exhibit不稳定性：cross-task structure不consistent（SST-2 item=14% vs COPA item=7%），item_id resampling CV=28%（低于inference的33%但仍substantial）。\\nLearning rate dominance expected——不同lr通向不同loss landscape basins，每个basin对每个item有不同prediction。lr:seed=11%说明optimization landscape随机性irreducible。GPU main=3%是novel finding——fine-tuning中GPU difference通过gradient accumulation被amplified（thousands of steps中compound），比inference hardware effect更大。\\nInference-training correlation=0.18意味着inference-based reproducibility analysis不能generalize到training。但如果整个variance decomposition methodology的reliability已被质疑（exp-001b/004），fine-tuning results也受同样质疑——这是double-edged的。\\n\"\n  },\n  {\n    \"name\": \"LayerCast precision mitigation\",\n    \"description\": \"LayerCast（FP16 storage + FP32 compute）作为第4种precision条件on MMLU。\",\n    \"results\": {\n      \"layercast_accuracy\": 0.671,\n      \"layercast_vs_bf16_delta\": 0.001,\n      \"variance_reduction_vs_fp16\": 0.002,\n      \"precision_component_4level\": 0.013,\n      \"precision_item_4level\": 0.04,\n      \"practical_significance\": \"negligible\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 17: Precision Conditions Including LayerCast\",\n        \"columns\": [\n          \"Condition\",\n          \"Accuracy\",\n          \"Precision Share\",\n          \"Precision:item Share\"\n        ],\n        \"rows\": [\n          [\n            \"FP32\",\n            \"0.668\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"BF16\",\n            \"0.672\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"FP16\",\n            \"0.670\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"LayerCast\",\n            \"0.671\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"4-level precision\",\n            \"—\",\n            \"1.3%\",\n            \"4.0%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Null result。一句mention：\\\"LayerCast addresses <2% of total variance, confirming precision is not a first-order concern once engine confounds are controlled。\\\"不值得paper space。\\n\\n\\nConfound修复后precision main effect已极小（1.6%），LayerCast额外收益微乎其微。LayerCast accuracy=0.671介于FP16和BF16之间，Δ<0.2pp。在worst档narrative（方差分解本身不可靠）下，precision mitigation targeting一个1.6%的component完全irrelevant——即使完全消除precision variance，其他components的instability仍dominate。\\n\"\n  },\n  {\n    \"name\": \"MATH benchmark extension\",\n    \"description\": \"MATH 200 items，测试extreme reasoning task是否延续gradient pattern。\",\n    \"results\": {\n      \"item_variance_math\": 0.38,\n      \"residual_math\": 0.24,\n      \"temperature_item_math\": 0.09,\n      \"seed_item_math\": 0.07,\n      \"temperature_main_math\": 0.04,\n      \"seed_main_math\": 0.03,\n      \"prompt_item_math\": 0.04,\n      \"g_coefficient_math\": 0.28,\n      \"items_needed_g90_math\": 520,\n      \"gradient_with_math\": \"still non-monotonic\",\n      \"gradient_spread_5bench_pp\": 9,\n      \"difficulty_bimodality_index\": 0.7,\n      \"bimodality_item_id_correlation\": 0.95\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 18: Full 5-Benchmark Spectrum\",\n        \"columns\": [\n          \"Benchmark\",\n          \"Type\",\n          \"item_id\",\n          \"residual\",\n          \"temp:item\",\n          \"seed:item\",\n          \"G\",\n          \"Items G≥0.90\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            \"Knowledge\",\n            \"37.8%\",\n            \"20.2%\",\n            \"5.8%\",\n            \"1.6%\",\n            \"0.32\",\n            \"480\"\n          ],\n          [\n            \"GSM8K\",\n            \"Math\",\n            \"42.0%\",\n            \"22.0%\",\n            \"8.0%\",\n            \"6.0%\",\n            \"0.30\",\n            \"420\"\n          ],\n          [\n            \"ARC\",\n            \"Science\",\n            \"36.0%\",\n            \"20.0%\",\n            \"6.0%\",\n            \"4.0%\",\n            \"0.35\",\n            \"450\"\n          ],\n          [\n            \"HellaSwag\",\n            \"Commonsense\",\n            \"33.0%\",\n            \"18.0%\",\n            \"7.0%\",\n            \"5.0%\",\n            \"0.36\",\n            \"440\"\n          ],\n          [\n            \"MATH\",\n            \"Hard reasoning\",\n            \"38.0%\",\n            \"24.0%\",\n            \"9.0%\",\n            \"7.0%\",\n            \"0.28\",\n            \"520\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 19: Difficulty Distribution Predicts Item Dominance\",\n        \"columns\": [\n          \"Benchmark\",\n          \"Difficulty SD\",\n          \"Bimodality Index\",\n          \"item_id\"\n        ],\n        \"rows\": [\n          [\n            \"GSM8K\",\n            \"0.34\",\n            \"0.72\",\n            \"42.0%\"\n          ],\n          [\n            \"MATH\",\n            \"0.33\",\n            \"0.70\",\n            \"38.0%\"\n          ],\n          [\n            \"MMLU\",\n            \"0.30\",\n            \"0.65\",\n            \"37.8%\"\n          ],\n          [\n            \"ARC\",\n            \"0.27\",\n            \"0.52\",\n            \"36.0%\"\n          ],\n          [\n            \"HellaSwag\",\n            \"0.22\",\n            \"0.38\",\n            \"33.0%\"\n          ],\n          [\n            \"r with item_id\",\n            \"r=0.92\",\n            \"r=0.95\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"MATH cements non-gradient finding。但Table 19意外产出positive value：bimodality→item_id的strong correlation是novel mechanistic insight——item dominance is predictable from difficulty distribution shape, not from task taxonomy。在worst档下，这是paper可以claim的少数positive findings之一。\\n\\nMATH item dominance=38%——与MMLU几乎identical，彻底否定gradient。原因：MATH的200-item sample包含高度bimodal difficulty（Level 1-2: accuracy>80%; Level 4-5: accuracy<10%），extreme bimodality推高item_id，counteracting CoT randomness的预期effect。\\n关键insight：item dominance不是task type的function，而是item difficulty distribution shape的function。Bimodal distributions（无论来源——MMLU的subject heterogeneity还是MATH的difficulty levels）inflate item_id；unimodal distributions（HellaSwag）suppress它。5-benchmark ordering: GSM8K(42%)>MMLU=MATH(38%)>ARC(36%)>HellaSwag(33%)，spread=9pp，无systematic pattern。\\nBimodality index与item_id的correlation r=0.95是一个strong mechanistic finding——prior work未identify bimodality作为item variance contribution的predictor。这在worst档下是一个positive sub-finding。\\nD-study G≥0.90需要520 items，与其他benchmarks（420-480）comparable，进一步支持convergence。\\n\"\n  }\n]",
      "numLines": 1235,
      "startLine": 1,
      "totalLines": 1235
    }
  },
  "sourceToolAssistantUUID": "de0a54b7-77e9-48c6-934a-4e78382fcf59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T23:25:34.831Z_

<details><summary>↩ Tool result · `toolu_01W3NzzcXWMhqWGU1FKK2udF`</summary>

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
  "parentUuid": "e20f1966-4df2-40b8-b5a9-57489cfeef9c",
  "isSidechain": false,
  "promptId": "373fec7c-0384-4178-9c36-2cd6143072a3",
  "type": "user",
  "uuid": "f2200013-9f0d-4ab3-b2f1-a887c901d5e6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/paper_framing.md",
      "content": "# Paper Framing — nlp_variance_gtheory\n\n## Target Venue\n- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)\n- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)\n- Extended: TACL (rolling)\n\n## Title\nReproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics\n\n## Core Claims (3 条，可证伪)\n\n**Claim 1 — Item Dominance (benchmark-conditional)**: Item selection is the single largest variance source in multiple-choice LLM evaluation, but its magnitude is benchmark-dependent: from ~45% on knowledge-retrieval tasks (MMLU) down to ~25% on reasoning tasks (GSM8K/MATH) where temperature and seed interactions increase. Item dominance is expected from measurement theory when item difficulty varies widely (Brennan, 2001); our contribution is in (a) quantifying the precise magnitude across benchmarks and models, (b) demonstrating the systematic benchmark-dependent gradient, and (c) deriving D-study implications specific to LLM evaluation.\n\n**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), \"infrastructure\" is currently limited to the precision facet.\n\n**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent: binary correct scoring yields G=0.357 (item dominance makes G≥0.90 unreachable without massive item expansion), while text-exact-match scoring yields G=0.975 (already adequate). D-study projections show that increasing item sampling is more cost-effective than increasing prompt/seed replication, but the optimal allocation depends critically on both the evaluation metric and the benchmark. Current common practices (1 prompt, 1 seed, ≤200 items, single metric) produce misleading reliability estimates.\n\n## Contributions (3 条，明确区分)\n\n1. **Cross-benchmark variance gradient**: The first multi-benchmark G-theory analysis showing that variance structure systematically shifts from item-dominated (knowledge retrieval) to interaction-dominated (reasoning tasks), explaining why prior single-benchmark studies reached seemingly contradictory conclusions.\n\n2. **Confirmatory separability test**: Infrastructure×methodology interactions are negligible at the aggregate level (<0.5% under binary scoring), providing empirical support for isolated-factor studies — with the caveat that both factors interact with items and the finding is metric-conditional.\n\n3. **Task-specific reproducibility budgets**: D-study projections with bootstrap CIs yield actionable, benchmark-specific item/prompt/seed allocations for achieving target reliability (G≥0.90), contextualized against IRT-based subsampling approaches (tinyBenchmarks, HELM-Lite).\n\n## Story Spine\n\n**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability.\n\n**Existing approaches & gaps**: Bouthillier et al. (2021) decomposed ML benchmark variance across hyperparameters, data splits, and seeds via ANOVA, establishing the template for factorial variance decomposition in ML evaluation. Mesting (2026) adapted G-theory to 5 methodological facets in LLM evaluation but treated infrastructure as fixed. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance on fixed hardware. IRT-based approaches (Lalor et al. 2019; Rodriguez et al. 2021; Polo et al. 2024) have analyzed item-level properties and efficient subsampling, but from a different methodological perspective than G-theory. No study has: (a) crossed infrastructure and methodology in a unified G-theory framework, (b) compared variance structure across multiple benchmarks, or (c) provided metric-conditional reproducibility budgets.\n\n**Our framing**: We conduct a multi-benchmark G-theory study crossing infrastructure (numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors, with model treated as a crossed facet. The infrastructure crossing yields a confirmatory null result: aggregate separability holds, validating the implicit assumption of prior isolated-factor studies. The primary novel finding is the cross-benchmark variance gradient — item dominance systematically weakens as tasks shift from knowledge retrieval to multi-step reasoning — explaining divergent conclusions in the literature. D-study projections provide the first benchmark-specific, metric-conditional reproducibility budgets for LLM evaluation, directly comparable to IRT-based subsampling approaches.\n\n**Headline result template**: \"In a G-study of K conditions across M models and N benchmarks, item selection is the largest single variance source on multiple-choice benchmarks (25-55%, benchmark-dependent), while direct infrastructure×methodology interactions are negligible (<0.5% binary, ≤1.3% text-match). Variance structure shifts systematically from item-dominated (knowledge benchmarks) to interaction-dominated (reasoning benchmarks). D-study reproducibility budgets show that optimal facet allocation is both benchmark-specific and metric-conditional: MMLU needs more items, GSM8K needs more seeds.\"\n\n## Hook (Counter-Intuitive Quantified Claim)\n\"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks — our G-theory analysis across N benchmarks shows the variance structure itself is benchmark-conditional, rendering any 'universal reproducibility recipe' illusory.\"\n\n## Narrative Strategy\n- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Empirical contribution (benchmark-conditional gradient)\n- **Tension**: \"No universal recipe\" — the field seeks standardization but variance structure varies qualitatively across task types\n- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)\n- **Signature visual**: Stacked-bar variance decomposition chart across benchmarks (field idiom from Mesting/Brittlebench)\n- **Figure plan** (4 figures minimum):\n  1. Problem illustration: same model, different benchmark → different dominant variance source\n  2. G-theory facet diagram showing crossed design\n  3. Stacked-bar variance decomposition across benchmarks (signature figure)\n  4. D-study projection curves: G vs item count for different benchmarks\n- **Key framing shifts from Dream feedback**:\n  - Infrastructure crossing framed as **confirmatory** (validates isolated-factor studies), not as primary novelty\n  - Item dominance acknowledged as **psychometrically expected**; contribution is quantification + benchmark gradient\n  - Cross-benchmark gradient is the **primary novel finding**\n  - \"Fully crossed\" language qualified to MMLU exp-001 only; other benchmarks use reduced designs\n\n## Venue Fit Risks\n- AAAI: Strong fit for \"evaluation methodology\" track. Risk: tight 9-week timeline requires overlapping experiments with writing.\n- Reviewer concern 1: \"Only open-weight models, not API models\" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.\n- Reviewer concern 2: \"G-theory is borrowed methodology, not novel\" — Frame as cross-domain transfer. The novelty is the cross-benchmark variance gradient finding, not G-theory itself.\n- Reviewer concern 3: \"Item dominance is obvious from measurement theory\" — Acknowledge explicitly. Contribution is quantification (25-55%), benchmark-dependence, and D-study implications. Contextualize against IRT item analysis literature.\n\n## Anticipated Reviewer Concerns & Planned Responses\n1. **\"Only N GPU types\"** → exp-003 (multi-hardware crossing) addresses this. If blocked, explicitly scope to \"numerical precision\" and frame hardware as future work.\n2. **\"float32 engine confound\"** → exp-001 fixes with V0 enforce_eager for all precisions. Confound discovery itself is a standalone methodological contribution.\n3. **\"Only MMLU\"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag. Cross-benchmark gradient is the core finding.\n4. **\"Small item sample\"** → exp-001 expands from 50 to 200 items. exp-001b tests resampling stability.\n5. **\"No training-time analysis\"** → exp-006 (fine-tuning G-study with RoBERTa). Explicitly qualify as encoder-only classification; decoder fine-tuning is future work.\n6. **\"Missing scale validation\"** → exp-005 (14B models)\n7. **\"G-theory may not be right framework\"** → Compare with ANOVA and regression decomposition as sensitivity analysis. Cite Bouthillier et al. (2021) as ANOVA-based predecessor; show G-theory adds D-study projections.\n8. **\"Separability claim is metric-dependent\"** → This is precisely the point: reproducibility budgets must be metric-qualified. Replace arbitrary threshold with bootstrap CI on interaction term.\n9. **\"FP32 degradation is already known (Yuan 2025)\"** → Position as supporting finding with novel item-level breakdown. Not an independent claim.\n10. **\"Incremental over Mesting (2026)\"** → Infrastructure crossing is confirmatory (valuable as validation, not breakthrough). Primary novelty: cross-benchmark gradient, task-specific budgets, dual-metric analysis, confound fix. Mesting = single benchmark, no infrastructure; we = multi-benchmark, infrastructure confirmation + benchmark gradient.\n11. **\"Model not treated as G-theory facet\"** → exp-004 includes model-as-facet reanalysis of MMLU data. Report model×item interaction separately from residual.\n12. **\"No CIs on variance components\"** → exp-004 includes bootstrap CIs (1000 resamples) on all variance components in all tables.\n13. **\"Missing related work — IRT, tinyBenchmarks, Bouthillier\"** → Comprehensive bibliography (25+ refs). Position D-study budgets against IRT-based subsampling. Cite Bouthillier et al. as ANOVA predecessor.\n14. **\"Diagnostic tool claim unsubstantiated\"** → Release analysis pipeline code (G-theory variance decomposition + D-study projections) as reusable tool. Or reframe as \"empirical analysis + data release.\"\n15. **\"Fine-tuning uses encoder-only RoBERTa\"** → Explicitly qualify. Decoder fine-tuning is a natural extension requiring substantially more compute.\n\n## Design Decisions\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.\n- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.\n- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as \"reduced crossing\" rather than \"fully crossed.\"\n\n## Required Bibliography (minimum 25 references)\nKey references to include beyond current literature_map:\n- Bouthillier et al. (2021, JMLR) — ML variance decomposition via ANOVA\n- Lalor et al. (2019, NAACL) — IRT-based item analysis in NLP\n- Rodriguez et al. (2021, ACL) — IRT evaluation for NLP\n- Polo et al. (2024) — tinyBenchmarks, IRT-based subsampling\n- Perlitz et al. (2023) — Efficient LLM benchmarking\n- Henderson et al. (2018) — Deep RL reproducibility, variance decomposition\n- Shavelson & Webb (1991) — G-theory primer (canonical)\n- Brennan (2001) — G-theory textbook (canonical)\n- Lu et al. (2022) — Option ordering effects in MC evaluation\n- Pezeshkpour & Hruschka (2024) — Option ordering effects\n- Dodge et al. (2020, EMNLP) — Fine-tuning instability (seed, data order)\n- Sellam et al. (2022) — MultiBERTs, multi-seed training\n- Dehghani et al. (2021) — Benchmark Lottery\n- Biderman et al. (2024) — Evaluation reproducibility lessons\n- Vania et al. (2021) — IRT item properties in NLP\n",
      "numLines": 104,
      "startLine": 1,
      "totalLines": 104
    }
  },
  "sourceToolAssistantUUID": "e20f1966-4df2-40b8-b5a9-57489cfeef9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T23:25:34.827Z_

<details open><summary>🔧 Tool call — Read · `toolu_01W3NzzcXWMhqWGU1FKK2udF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7989be7e-dc2b-4af5-a648-e08016f5cd6e",
  "isSidechain": false,
  "requestId": "req_011CbEgfqEYaRj7NjUmsyDX4",
  "type": "assistant",
  "uuid": "e20f1966-4df2-40b8-b5a9-57489cfeef9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NS9Kr6PXbHYzdC3vznLmm9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11694,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11694,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11694
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T222113 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheor…",
  "leafUuid": "f2200013-9f0d-4ab3-b2f1-a887c901d5e6",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier dream paper for NLP variance study",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640"
}
```

---

### Assistant

_source line 14 · 2026-05-20T23:25:52.283Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me also load the research and writing pattern skills to ensure quality.

Let me now write the paper. The key narrative shift for the "worst" tier is:

1. The cross-benchmark variance gradient doesn't hold (spread only 9pp, wrong direction)
2. The centerpiece is item resampling instability (CV=33%)
3. Core argument: "variance decomposition is a measurement, not a fact"
4. Three reframed claims:
   - Claim 1: item dominance estimates are sample-unstable (CV>30%)
   - Claim 2: model×item interaction (33%) is the largest overlooked component; treating model as fixed systematically misattributes variance
   - Claim 3: reproducibility budgets need their own uncertainty quantification

I'm structuring a comprehensive LaTeX paper that pulls data from all eight experiments without fabricating numbers, following the narrative guidance about the unreliability of the budget itself. The paper will move through abstract, introduction with the core hook, related work, the G-theory framework, and experimental sections that demonstrate how variance decomposition reveals measurement instability rather than ground truth.

Writing the paper structure...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2200013-9f0d-4ab3-b2f1-a887c901d5e6",
  "isSidechain": false,
  "requestId": "req_011CbEgg7y7jkvFU4q1CziLu",
  "type": "assistant",
  "uuid": "12900eeb-4570-405d-b214-b2387007e9cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuJS6PbfegHAbkmx1WYQ2X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20230,
      "cache_read_input_tokens": 23535,
      "output_tokens": 468,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20230,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 468,
          "cache_read_input_tokens": 23535,
          "cache_creation_input_tokens": 20230,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20230
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

_source line 15 · 2026-05-20T23:25:52.286Z_

Now let me check the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12900eeb-4570-405d-b214-b2387007e9cd",
  "isSidechain": false,
  "requestId": "req_011CbEgg7y7jkvFU4q1CziLu",
  "type": "assistant",
  "uuid": "4367f7ba-3ef1-4f43-8561-df98bc934b93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuJS6PbfegHAbkmx1WYQ2X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20230,
      "cache_read_input_tokens": 23535,
      "output_tokens": 468,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20230,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 468,
          "cache_read_input_tokens": 23535,
          "cache_creation_input_tokens": 20230,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20230
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

_source line 16 · 2026-05-20T23:25:52.438Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01LjyChjuSV4T8SPRZPKYvSz`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/",
  "description": "List output directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4367f7ba-3ef1-4f43-8561-df98bc934b93",
  "isSidechain": false,
  "requestId": "req_011CbEgg7y7jkvFU4q1CziLu",
  "type": "assistant",
  "uuid": "e6f64b4f-a86b-47f8-9299-5102f85b627a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuJS6PbfegHAbkmx1WYQ2X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20230,
      "cache_read_input_tokens": 23535,
      "output_tokens": 468,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20230,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 468,
          "cache_read_input_tokens": 23535,
          "cache_creation_input_tokens": 20230,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20230
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

_source line 17 · 2026-05-20T23:25:52.561Z_

<details><summary>↩ Tool result · `toolu_01LjyChjuSV4T8SPRZPKYvSz`</summary>

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
  "parentUuid": "e6f64b4f-a86b-47f8-9299-5102f85b627a",
  "isSidechain": false,
  "promptId": "373fec7c-0384-4178-9c36-2cd6143072a3",
  "type": "user",
  "uuid": "514b6401-bc21-44ea-96bb-6ff1bdef45cd",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "e6f64b4f-a86b-47f8-9299-5102f85b627a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-20T23:25:54.638Z_

Writing the full LaTeX paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "514b6401-bc21-44ea-96bb-6ff1bdef45cd",
  "isSidechain": false,
  "requestId": "req_011CbEghRX5j4yV73YKrVGVV",
  "type": "assistant",
  "uuid": "c1b9053f-a0bf-48e0-9be8-2b6900dfd446",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PPHhyJzQNqEmUKTSGrQJ9e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 496,
      "cache_read_input_tokens": 43765,
      "output_tokens": 14676,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 496,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14676,
          "cache_read_input_tokens": 43765,
          "cache_creation_input_tokens": 496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 496
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

_source line 19 · 2026-05-20T23:30:20.730Z_

<details open><summary>🔧 Tool call — Write · `toolu_012A7hrgXPEqhfvijd4SHETb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{adjustbox}\n\n\\title{Variance Decomposition Is a Measurement, Not a Fact:\\\\\nOn the Instability of Reproducibility Budgets for LLM Evaluation}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nWe set out to build reproducibility budgets for LLM evaluation using Generalizability Theory (G-theory) and discovered that the budget itself is unreliable.\nIn a multi-benchmark G-study crossing infrastructure (numerical precision, hardware) $\\times$ methodology (prompt, seed, temperature, ordering) $\\times$ measurement (item) factors across four models and five benchmarks (172{,}800--230{,}400 observations per experiment), we find three results that challenge current variance-attribution practices.\nFirst, item dominance estimates are sample-unstable: resampling 200 MMLU items with different stratified seeds yields item variance shares ranging from 25\\% to 48\\% (CV\\,=\\,0.33), meaning prior single-decomposition studies---including all existing G-theory analyses of LLM evaluation---over-commit to attribution certainty.\nSecond, treating model as fixed (the standard practice) systematically inflates item variance from 37.8\\% to an apparent dominance; a model-as-facet reanalysis reveals that model$\\times$item interaction (33\\%) is the single largest component, reducing pure item variance to 15.2\\%.\nThird, D-study reproducibility budgets converge across benchmarks (range = 60 items for $G \\geq 0.90$) but carry bootstrap confidence intervals of $\\pm$190 items, rendering benchmark-specific budget recommendations statistically indistinguishable and demanding that budgets themselves report uncertainty.\nThese findings reframe variance decomposition from a factual attribution to a measurement with its own error, requiring uncertainty quantification before actionable conclusions can be drawn.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nWhen LLM evaluation results fail to replicate, the natural response is to identify the culprit: was it the prompt, the random seed, the GPU, the numerical precision, or the item selection?\nA growing body of work has pursued this question by decomposing evaluation variance into attributable sources \\citep{bouthillier2021accounting, mesting2026generalizability, brittlebench2026}.\nThese studies report point estimates of variance shares---``item selection accounts for 43.8\\% of variance'' \\citep{mesting2026generalizability}, ``prompt sensitivity explains 50\\% of score variation'' \\citep{brittlebench2026}---and derive practical recommendations from them.\n\nWe conducted a large-scale G-theory study with the same goal: cross infrastructure and methodology factors in a unified framework, measure variance components across five benchmarks, and produce reproducibility budgets telling practitioners how many items, prompts, and seeds they need.\nWhat we found instead is that \\emph{the variance decomposition itself is unstable}.\nThree independent item samples of 200 MMLU questions yield item dominance estimates of 48\\%, 25\\%, and 41\\%---a coefficient of variation of 33\\%.\nWhich items happen to be sampled determines not just the magnitude but the \\emph{rank order} of variance components: in one sample, the residual exceeds item variance as the largest component.\nEvery prior study that reports a single variance decomposition without resampling stability analysis has, in effect, presented one draw from a high-variance distribution as a finding.\n\nThis instability compounds with a second problem: model specification.\nStandard practice treats model as fixed and pools across models or analyzes each separately.\nWhen we instead treat model as a crossed random facet, item variance drops from 37.8\\% to 15.2\\%, with the difference absorbed by a model$\\times$item interaction of 33\\%---the largest single component in the crossed design.\nItem ``difficulty'' is not an intrinsic property of items but a joint property of item--model pairs, a conclusion that fundamentally challenges the premise of item-dominated variance attribution.\n\nA third discovery concerns reproducibility budgets themselves.\nD-study projections for $G \\geq 0.90$ converge across benchmarks (420--520 items, range = 60), which would seem to simplify practical recommendations.\nBut the bootstrap 95\\% confidence intervals span $\\pm$190 items---wider than the cross-benchmark range---meaning any specific budget recommendation is statistically indistinguishable from its neighbors.\nReproducibility budgets require their own error bars.\n\nOur contributions are:\n\\begin{enumerate}\n\\item Evidence that variance component estimates in LLM evaluation are sample-unstable (item resampling CV\\,=\\,0.33, component rank inversions across samples), establishing that single-run decompositions over-commit to attribution certainty.\n\\item A model-as-facet reanalysis showing that model$\\times$item interaction (33\\%) is the largest overlooked variance source, and that treating model as fixed inflates item dominance by $>$22 percentage points.\n\\item A demonstration that D-study reproducibility budgets require uncertainty quantification: cross-benchmark budget convergence (range = 60 items) is dominated by within-benchmark CI width ($\\pm$190 items), rendering benchmark-specific recommendations unreliable.\n\\end{enumerate}\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Variance decomposition in ML evaluation.}\n\\citet{bouthillier2021accounting} introduced factorial variance decomposition to ML benchmarking via ANOVA, decomposing performance variation across hyperparameters, data splits, and random seeds.\n\\citet{henderson2018deep} applied similar methods to deep reinforcement learning, finding that implementation details dominate reported improvements.\n\\citet{dodge2020fine} and \\citet{sellam2022multiBERTs} documented fine-tuning instability from seed and data order in BERT-scale models.\nThese studies establish the paradigm we build on but do not address LLM inference evaluation or apply G-theory's D-study projections.\n\n\\paragraph{G-theory in LLM evaluation.}\n\\citet{mesting2026generalizability} adapted Generalizability Theory to LLM-as-judge evaluation, decomposing variance across five methodological facets.\nTheir study treats model and infrastructure as fixed, reports single-run point estimates without resampling stability analysis, and covers one benchmark.\n\\citet{brittlebench2026} quantified prompt sensitivity at up to 50\\% of score variation on fixed hardware.\nNeither study crosses infrastructure with methodology or tests the stability of their decomposition.\n\n\\paragraph{Item-level analysis and IRT.}\nItem Response Theory has been applied to NLP evaluation for item analysis \\citep{lalor2019learning, rodriguez2021evaluation, vania2021comparing}, efficient subsampling \\citep{polo2024tinybenchmarks, perlitz2023efficient}, and the Benchmark Lottery phenomenon \\citep{dehghani2021benchmark}.\nThese approaches model item properties but do not decompose evaluation variance into infrastructure vs.\\ methodology sources.\n\n\\paragraph{Reproducibility factors.}\n\\citet{yuan2025llm} documented up to 9\\% accuracy variation from hardware and numerical precision without factorial attribution.\n\\citet{lu2022fantastically, pezeshkpour2024large} studied option ordering effects in multiple-choice evaluation.\n\\citet{biderman2024lessons} surveyed evaluation reproducibility challenges.\nEach isolates at most two factors, implicitly assuming separability.\n\n% ============================================================\n% 3. METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{Generalizability Theory Framework}\n\nGeneralizability Theory (G-theory; \\citealp{shavelson1991generalizability, brennan2001generalizability}) decomposes observed score variance into components attributable to facets (e.g., items, prompts, seeds) and their interactions.\nFor a fully crossed design with $k$ facets, a person's observed score $X_{p}$ is:\n\\begin{equation}\nX_{pijk\\ldots} = \\mu + \\alpha_p + \\beta_i + \\gamma_j + \\delta_k + (\\alpha\\beta)_{pi} + (\\alpha\\gamma)_{pj} + \\cdots + \\epsilon_{pijk\\ldots}\n\\end{equation}\nwhere each Greek letter represents the effect of a facet or interaction and $\\epsilon$ is residual error.\nThe G-coefficient summarizes measurement dependability:\n\\begin{equation}\nG = \\frac{\\sigma^2_p}{\\sigma^2_p + \\sigma^2_{\\text{relative error}}}\n\\end{equation}\nD-studies project $G$ under hypothetical facet sample sizes, enabling reproducibility budget planning.\n\n\\subsection{Experimental Design}\n\nWe conduct a series of experiments with increasing scope.\nAll experiments use generation-based evaluation (following \\citealp{hua2025emnlp}) with vLLM 0.9.2 and \\texttt{enforce\\_eager} mode to eliminate engine-level confounds.\n\n\\paragraph{Experiment 1: Full-scale precision study.}\n4 models (Qwen3-8B, Llama-3.1-8B, Gemma-2-9B, Mistral-7B) $\\times$ 3 precisions (FP32, BF16, FP16) $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 3 temperatures $\\times$ 4 orderings $\\times$ 200 MMLU items = 172{,}800 observations.\nModel is initially treated as fixed (analyzed per-model and pooled); Experiment 4 reanalyzes with model as a crossed facet.\n\n\\paragraph{Experiment 1b: Item resampling stability.}\n3 independent stratified 200-item MMLU samples (seeds 0, 7, 99) $\\times$ Llama-3.1-8B $\\times$ 3 precisions $\\times$ 3 prompts $\\times$ 3 seeds $\\times$ 2 orderings = 54 conditions per sample, 10{,}800 observations per sample.\n\n\\paragraph{Experiment 2: Multi-benchmark replication.}\n4 models $\\times$ 2 precisions $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 2 temperatures $\\times$ 4 orderings on GSM8K, ARC-Challenge, and HellaSwag (200 items each), 76{,}800 observations per benchmark.\n\n\\paragraph{Experiment 3: Multi-hardware G-study.}\n4 models $\\times$ 2 GPU types $\\times$ 2 precisions $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 3 temperatures $\\times$ 4 orderings $\\times$ 200 MMLU items = 230{,}400 observations.\n\n\\paragraph{Experiment 4: Comprehensive reanalysis.}\nMerged data from Experiments 1--3. Model-as-facet reanalysis, 1{,}000-replicate bootstrap CIs on all variance components, D-study projections with uncertainty quantification, and REML sensitivity analysis.\n\n\\paragraph{Experiment 5: Scale extension.}\nQwen3-14B and DeepSeek-R1-Distill-14B at BF16/FP16, testing whether 14B models alter variance structure.\n\n\\paragraph{Experiment 6: Fine-tuning G-study.}\nRoBERTa-large on SST-2, MNLI, RTE, COPA. 6 seeds $\\times$ 3 learning rates $\\times$ 4 data shuffles $\\times$ 3 GPUs $\\times$ 2 precisions = 432 runs per task, 1{,}728 total.\n\n\\paragraph{Experiment 7: LayerCast precision mitigation.}\nFP16 storage + FP32 compute as a fourth precision condition on MMLU.\n\n\\paragraph{Experiment 8: MATH benchmark extension.}\n200 MATH items under the same multi-benchmark protocol, completing a 5-benchmark spectrum.\n\n% ============================================================\n% 4. EXPERIMENTS AND RESULTS\n% ============================================================\n\\section{Experiments and Results}\n\n\\subsection{Experiment 1: Variance Decomposition Under Model-as-Fixed Analysis}\n\\label{sec:exp1}\n\nTable~\\ref{tab:exp1_variance} presents the variance decomposition from the full-scale MMLU study with model treated as fixed.\nAt face value, item selection is the largest component (37.8\\% pooled), with substantial variation across models: Qwen3-8B shows the highest item dominance (42.2\\%) while Mistral-7B shows the lowest (30.3\\%, CV across models = 0.13).\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance components under model-as-fixed analysis (MMLU, binary scoring, 200 items). These point estimates are subsequently shown to be unstable (Sec.~\\ref{sec:exp1b}) and inflated (Sec.~\\ref{sec:exp4}).}\n\\label{tab:exp1_variance}\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{lccccc}\n\\toprule\nComponent & Qwen3-8B & Llama-3.1-8B & Gemma-2-9B & Mistral-7B & Pooled \\\\\n\\midrule\nitem\\_id         & 42.2\\% & 35.8\\% & 40.1\\% & 30.3\\% & 37.8\\% \\\\\nresidual         & 17.4\\% & 21.2\\% & 18.8\\% & 26.1\\% & 20.2\\% \\\\\ntemperature:item & 6.3\\%  & 5.9\\%  & 5.2\\%  & 5.8\\%  & 5.8\\%  \\\\\nprompt:item      & 5.8\\%  & 5.4\\%  & 4.8\\%  & 4.2\\%  & 5.2\\%  \\\\\nprecision:item   & 4.9\\%  & 4.6\\%  & 4.2\\%  & 3.8\\%  & 4.5\\%  \\\\\nseed:item        & 1.8\\%  & 1.7\\%  & 1.4\\%  & 1.3\\%  & 1.6\\%  \\\\\nordering:item    & 1.4\\%  & 1.2\\%  & 1.1\\%  & 0.9\\%  & 1.2\\%  \\\\\nprecision        & 1.8\\%  & 1.7\\%  & 1.5\\%  & 1.3\\%  & 1.6\\%  \\\\\ntemperature      & 1.2\\%  & 1.0\\%  & 0.9\\%  & 0.8\\%  & 1.0\\%  \\\\\nprompt           & 0.8\\%  & 0.7\\%  & 0.6\\%  & 0.5\\%  & 0.7\\%  \\\\\nprec.:temp.      & 1.6\\%  & 1.5\\%  & 1.4\\%  & 1.2\\%  & 1.5\\%  \\\\\nall other        & 14.8\\% & 19.3\\% & 20.0\\% & 23.8\\% & 18.9\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\nPrecision main effects are small after confound correction (1.6\\% pooled), and accuracy differences across FP32 (0.668), BF16 (0.672), and FP16 (0.670) are negligible ($\\Delta_{\\max}$ = 0.004 for each model).\nThe $G$-coefficient under binary scoring is 0.32, reflecting the inherent low reliability of binary item scoring with 200 items.\nThe precision$\\times$temperature interaction (1.5\\%) is non-negligible but does not by itself break separability.\n\nThese results appear to support an item-dominance narrative.\nHowever, as we show next, this narrative is an artifact of two methodological choices: a single item sample and a fixed-model specification.\n\n\\subsection{Experiment 1b: Item Resampling Instability}\n\\label{sec:exp1b}\n\nTable~\\ref{tab:resample} presents the variance decomposition under three independent stratified 200-item MMLU samples.\nThe item variance share ranges from 25.0\\% (Sample~7) to 48.0\\% (Sample~0), yielding a coefficient of variation of 0.33.\nThis instability is not merely quantitative: in Sample~7, the residual (30.0\\%) exceeds item variance (25.0\\%) as the largest component, producing a qualitatively different decomposition.\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance decomposition across three independent item samples (Llama-3.1-8B, MMLU). Item dominance is sample-dependent, with rank inversions across samples.}\n\\label{tab:resample}\n\\begin{tabular}{lcccccc}\n\\toprule\nComponent & Sample 0 & Sample 7 & Sample 99 & Mean & SD & CV \\\\\n\\midrule\nitem\\_id        & 48.0\\% & 25.0\\% & 41.0\\% & 38.0\\% & 12.0\\% & 0.33 \\\\\nresidual        & 16.0\\% & 30.0\\% & 19.0\\% & 21.7\\% & 7.5\\%  & 0.35 \\\\\ntemperature:item& 7.2\\%  & 9.8\\%  & 8.1\\%  & 8.4\\%  & 1.3\\%  & 0.16 \\\\\nprompt:item     & 5.6\\%  & 8.2\\%  & 6.4\\%  & 6.7\\%  & 1.3\\%  & 0.20 \\\\\nprecision:item  & 4.8\\%  & 6.4\\%  & 5.2\\%  & 5.5\\%  & 0.8\\%  & 0.15 \\\\\ntemperature     & 1.0\\%  & 2.4\\%  & 1.4\\%  & 1.6\\%  & 0.7\\%  & 0.46 \\\\\nprompt          & 0.6\\%  & 1.8\\%  & 0.9\\%  & 1.1\\%  & 0.6\\%  & 0.58 \\\\\nall other       & 16.8\\% & 16.4\\% & 18.0\\% & 17.1\\% & 0.8\\%  & 0.05 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:resample_stability} shows that the $G$-coefficient itself varies from 0.28 to 0.38 across samples (CV\\,=\\,0.16), and the largest-component identity is not stable.\nThe bootstrap 95\\% CI on item variance is [0.27, 0.48] (width = 0.21), wide enough that it cannot distinguish between ``item dominance'' ($>$40\\%) and ``item is one of several comparable sources'' ($\\sim$25\\%).\n\n\\begin{table}[t]\n\\centering\n\\caption{$G$-coefficient and rank stability across item samples. The rank order of variance components is not stable: Sample~7 reverses the top two components.}\n\\label{tab:resample_stability}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Sample 0 & Sample 7 & Sample 99 \\\\\n\\midrule\n$G$ (correct)       & 0.28     & 0.38     & 0.31 \\\\\nLargest component    & item\\_id & residual & item\\_id \\\\\n2nd largest          & residual & item\\_id & residual \\\\\n3rd largest          & temp:item& temp:item& temp:item \\\\\nItem difficulty SD   & 0.31     & 0.22     & 0.27 \\\\\nBimodality index     & 0.71     & 0.38     & 0.58 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe mechanism is traceable: Sample~0 draws more items with extreme difficulty (bimodality index = 0.71), which naturally produce high item-level variance; Sample~7 draws items with more uniform difficulty (bimodality index = 0.38), compressing item variance.\nMMLU's 57 subjects have heterogeneous difficulty distributions---STEM subjects tend bimodal, humanities more uniform---and 200-item stratified sampling balances at the subject level but not within subjects.\n\nThis result is the centerpiece of the paper.\nPrior work reports single variance decompositions as findings \\citep{mesting2026generalizability, brittlebench2026, bouthillier2021accounting}.\nA CV of 33\\% means that if \\citet{mesting2026generalizability} had used different items, her 43.8\\% judge-dominance estimate might have been 30\\% or 55\\%.\nVariance decomposition is a measurement with its own measurement error, and that error has been systematically ignored.\n\n\\subsection{Experiment 2: Multi-Benchmark Replication}\n\\label{sec:exp2}\n\nTable~\\ref{tab:multi_bench} extends the analysis to four benchmarks.\nItem variance ranges from 33.0\\% (HellaSwag) to 42.0\\% (GSM8K), a spread of only 9 percentage points.\nThe ordering is GSM8K $>$ MMLU $>$ ARC $>$ HellaSwag, which does not follow the predicted knowledge$\\to$reasoning gradient (Table~\\ref{tab:gradient_test}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Item dominance across benchmarks (model-as-fixed). No systematic gradient exists; spread = 9pp.}\n\\label{tab:multi_bench}\n\\begin{tabular}{lcccccc}\n\\toprule\nBenchmark & item\\_id & residual & temp:item & prompt:item & seed:item & $G$ \\\\\n\\midrule\nMMLU         & 37.8\\% & 20.2\\% & 5.8\\% & 5.2\\% & 1.6\\% & 0.32 \\\\\nGSM8K        & 42.0\\% & 22.0\\% & 8.0\\% & 5.0\\% & 6.0\\% & 0.30 \\\\\nARC-Challenge& 36.0\\% & 20.0\\% & 6.0\\% & 7.0\\% & 4.0\\% & 0.35 \\\\\nHellaSwag    & 33.0\\% & 18.0\\% & 7.0\\% & 4.0\\% & 5.0\\% & 0.36 \\\\\n\\midrule\nSpread       & 9pp    & 4pp    & 2pp   & 3pp   & 4pp   & ---  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{The predicted cross-benchmark gradient does not match observations.}\n\\label{tab:gradient_test}\n\\begin{tabular}{lll}\n\\toprule\nPredicted & Observed & Match \\\\\n\\midrule\nMMLU $>$ ARC $>$ GSM8K & GSM8K $>$ MMLU $>$ ARC $>$ HellaSwag & No \\\\\nMonotonic decrease with reasoning & Non-monotonic & No \\\\\nSpread $>$ 15pp for meaningful gradient & Spread = 9pp & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGSM8K's high item dominance (42\\%) despite being a reasoning benchmark is explained by its bimodal difficulty distribution: items range from trivial single-step arithmetic (accuracy $>$95\\%) to complex multi-step problems (accuracy $<$15\\%) for 8B-class models, and this bimodality inflates item-level variance.\nHellaSwag shows the lowest item dominance (33\\%) not because of task type but because its items have more uniform difficulty for these models.\n\nSuperimposed on the resampling instability from Experiment~1b (CV $>$ 30\\%), the 9pp spread falls within the noise range.\nThere is no evidence for a systematic cross-benchmark variance gradient.\n\n\\paragraph{Separability under binary scoring.}\nTable~\\ref{tab:separability} shows infrastructure$\\times$methodology interactions across benchmarks.\nOn MMLU, the total infra$\\times$method interaction is small (1.5\\%), but on GSM8K it reaches 4.5\\%, driven by precision$\\times$seed (1.5\\%) and precision$\\times$temperature (1.8\\%) interactions.\nSeparability does not hold uniformly across benchmarks under binary scoring.\n\n\\begin{table}[t]\n\\centering\n\\caption{Separability test (binary scoring). Infrastructure$\\times$methodology interactions exceed 3\\% on GSM8K and HellaSwag.}\n\\label{tab:separability}\n\\begin{tabular}{lcccc}\n\\toprule\nBenchmark & prec.$\\times$prompt & prec.$\\times$seed & prec.$\\times$temp & Total infra$\\times$method \\\\\n\\midrule\nMMLU         & 0.3\\% & 0.2\\% & 1.0\\% & 1.5\\% \\\\\nGSM8K        & 1.2\\% & 1.5\\% & 1.8\\% & 4.5\\% \\\\\nARC-Challenge& 0.4\\% & 0.3\\% & 1.3\\% & 2.0\\% \\\\\nHellaSwag    & 0.8\\% & 1.0\\% & 1.7\\% & 3.5\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Experiment 3: Multi-Hardware G-Study}\n\\label{sec:exp3}\n\nAdding a second GPU type reveals that hardware is a substantial variance source (Table~\\ref{tab:hardware}).\nTotal hardware-related variance is 14.0\\%, exceeding precision-related variance ($\\sim$6\\%).\nThe hardware$\\times$item interaction (6.0\\%) indicates that specific items flip between correct and incorrect across GPU architectures due to differences in tensor core implementations and floating-point rounding.\n\n\\begin{table}[t]\n\\centering\n\\caption{Hardware-related variance components (MMLU, binary scoring).}\n\\label{tab:hardware}\n\\begin{tabular}{lcc}\n\\toprule\nComponent & Variance Share & 95\\% Bootstrap CI \\\\\n\\midrule\nhardware (main)       & 5.0\\% & [3.2\\%, 7.1\\%] \\\\\nhardware:item         & 6.0\\% & [4.1\\%, 8.3\\%] \\\\\nhardware:precision    & 3.5\\% & [2.0\\%, 5.2\\%] \\\\\nhardware:prompt       & 1.5\\% & [0.8\\%, 2.4\\%] \\\\\nhardware:seed         & 2.0\\% & [1.2\\%, 3.1\\%] \\\\\nhardware:temperature  & 1.5\\% & [0.7\\%, 2.5\\%] \\\\\nitem\\_id (with hardware) & 33.0\\% & [25.1\\%, 41.8\\%] \\\\\nresidual              & 18.0\\% & [14.2\\%, 22.5\\%] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCritically, item variance drops from 37.8\\% (single-GPU, Experiment~1) to 33.0\\% when hardware is included as a facet.\nThis demonstrates that item variance in single-hardware designs is inflated by unmodeled hardware$\\times$item interactions---the item component acts as a catch-all for variance from omitted facets.\n\nSeparability fails decisively with hardware in the design (Table~\\ref{tab:sep_hardware}).\nThe total infra$\\times$method interaction increases from 1.5\\% (single-GPU) to 5.5\\% (multi-GPU), and hardware$\\times$methodology accounts for 4.0\\%.\n\n\\begin{table}[t]\n\\centering\n\\caption{Separability with vs.\\ without hardware. Adding hardware breaks separability.}\n\\label{tab:sep_hardware}\n\\begin{tabular}{lccc}\n\\toprule\nInteraction & Single-GPU & Multi-GPU & Separability \\\\\n\\midrule\ninfra$\\times$method (binary) & 1.5\\% & 5.5\\% & Fails ($>$3\\%) \\\\\nprecision$\\times$temperature & 1.5\\% & 1.5\\% & Marginal \\\\\nhardware$\\times$methodology  & N/A   & 4.0\\% & Fails \\\\\nhardware$\\times$precision    & N/A   & 3.5\\% & Fails \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Experiment 4: Model-as-Facet Reanalysis and D-Study Projections}\n\\label{sec:exp4}\n\nTable~\\ref{tab:model_crossed} presents the central methodological finding.\nWhen model is treated as a crossed random facet rather than fixed, item variance drops from 37.8\\% to 15.2\\% ($-$22.6pp), while model$\\times$item interaction emerges at 33.0\\%---the largest single component.\nThis means that what the model-as-fixed analysis attributes to ``item difficulty'' is largely the differential difficulty of items \\emph{across models}: an item that is easy for Qwen3-8B may be hard for Mistral-7B, and this interaction is misattributed to item variance when model is fixed.\n\n\\begin{table}[t]\n\\centering\n\\caption{Model-fixed vs.\\ model-crossed variance decomposition (MMLU, binary scoring). Treating model as fixed inflates item variance by 22.6pp.}\n\\label{tab:model_crossed}\n\\begin{tabular}{lcccc}\n\\toprule\nComponent & Model-Fixed & Model-Crossed & $\\Delta$ & Interpretation \\\\\n\\midrule\nitem\\_id        & 37.8\\% & 15.2\\% & $-$22.6pp & Misattributed to model$\\times$item \\\\\nmodel$\\times$item & ---  & 33.0\\% & +33.0pp  & Largest single component \\\\\nmodel (main)    & ---    & 6.0\\%  & +6.0pp   & Between-model differences \\\\\nresidual        & 20.2\\% & 12.0\\% & $-$8.2pp & Decomposed into model terms \\\\\ntemp:item       & 5.8\\%  & 4.5\\%  & $-$1.3pp & Slight reallocation \\\\\nprompt:item     & 5.2\\%  & 4.0\\%  & $-$1.2pp & Slight reallocation \\\\\nall other       & 31.0\\% & 25.3\\% & $-$5.7pp & Redistributed \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Bootstrap ranking stability.}\nTable~\\ref{tab:bootstrap_rank} shows that across 1{,}000 bootstrap resamples, no single component is consistently the largest.\nItem variance (model-fixed) is ranked first in only 45\\% of resamples; model$\\times$item is first in 38\\%.\nThe rank stability across bootstraps is 0.68---substantially below the level needed for confident attribution claims.\n\n\\begin{table}[t]\n\\centering\n\\caption{Bootstrap ranking stability (1{,}000 resamples). No component is reliably the largest.}\n\\label{tab:bootstrap_rank}\n\\begin{tabular}{lcccc}\n\\toprule\nComponent & Times \\#1 & Times \\#2 & Times \\#3 & Mean Rank \\\\\n\\midrule\nitem\\_id (model-fixed)   & 450 & 320 & 180 & 1.7 \\\\\nmodel$\\times$item        & 380 & 350 & 200 & 1.8 \\\\\nresidual                  & 170 & 330 & 350 & 2.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{D-study reproducibility budgets.}\nTable~\\ref{tab:dstudy} presents D-study projections for achieving $G \\geq 0.90$.\nPoint estimates converge across benchmarks (420--520 items, range = 60), but the 95\\% bootstrap CIs are wide (180--200 items).\nThe cross-benchmark range (60 items) is smaller than any single benchmark's CI width, meaning benchmark-specific budget differences are statistically indistinguishable.\n\n\\begin{table}[t]\n\\centering\n\\caption{D-study: items required for $G \\geq 0.90$. CI widths exceed the cross-benchmark range.}\n\\label{tab:dstudy}\n\\begin{tabular}{lccc}\n\\toprule\nBenchmark & Point Estimate & Bootstrap 95\\% CI & CI Width \\\\\n\\midrule\nMMLU      & 480 & [380, 560] & 180 \\\\\nGSM8K     & 420 & [310, 510] & 200 \\\\\nARC       & 450 & [350, 540] & 190 \\\\\nHellaSwag & 440 & [340, 530] & 190 \\\\\n\\midrule\nCross-benchmark range & 60 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Estimation method sensitivity.}\nThe choice between Henderson Method~I and REML estimation produces a 5.7pp divergence on item variance (37.8\\% vs.\\ 32.1\\%; Table~\\ref{tab:reml}), adding a further source of instability: the ``finding'' depends on which estimation method is used.\n\n\\begin{table}[t]\n\\centering\n\\caption{REML vs.\\ Henderson Method~I. Estimation method choice alters conclusions.}\n\\label{tab:reml}\n\\begin{tabular}{lccc}\n\\toprule\nComponent & Henderson & REML & $\\Delta$ \\\\\n\\midrule\nitem\\_id          & 37.8\\% & 32.1\\% & $-$5.7pp \\\\\nmodel$\\times$item & 33.0\\% & 35.2\\% & +2.2pp \\\\\nresidual          & 20.2\\% & 22.8\\% & +2.6pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Experiment 5: 14B Model Extension}\n\\label{sec:exp5}\n\nAdding 14B models (Table~\\ref{tab:14b}) reduces per-model item dominance (Qwen3-14B: 32.0\\%, DeepSeek-R1-14B: 28.0\\%) relative to 8B models (37.8\\% pooled) and increases model$\\times$item interaction from 33.0\\% to 38.0\\%.\nDeepSeek-R1-Distill-14B exhibits unusually high temperature:item (10.0\\%) and seed:item (8.0\\%) interactions, likely due to its reasoning-distilled architecture amplifying chain-of-thought stochasticity.\nScale and architecture effects are confounded with $n$=2 models and cannot be separated.\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance structure: 8B pooled vs.\\ 14B models vs.\\ all crossed.}\n\\label{tab:14b}\n\\begin{tabular}{lcccc}\n\\toprule\nComponent & 8B Pooled & Qwen3-14B & DeepSeek-R1-14B & All Crossed \\\\\n\\midrule\nitem\\_id (model-fixed) & 37.8\\% & 32.0\\% & 28.0\\% & 34.0\\% \\\\\nmodel$\\times$item (crossed) & 33.0\\% & --- & --- & 38.0\\% \\\\\nresidual                & 20.2\\% & 22.0\\% & 26.0\\% & 16.0\\% \\\\\ntemp:item               & 5.8\\%  & 5.0\\%  & 10.0\\% & 6.5\\%  \\\\\nseed:item               & 1.6\\%  & 1.4\\%  & 8.0\\%  & 3.2\\%  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Experiment 6: Fine-Tuning G-Study}\n\\label{sec:exp6}\n\nTable~\\ref{tab:finetune} presents the fine-tuning variance decomposition.\nThe variance structure differs qualitatively from inference: learning rate (16.8\\% average) replaces item selection as the dominant component, and the lr$\\times$seed interaction (11.0\\%) reflects irreducible optimization landscape stochasticity.\nItem variance in fine-tuning is modest (12.8\\% average) and cross-task unstable (SST-2: 14.0\\%, COPA: 7.0\\%).\nItem resampling CV in fine-tuning is 0.28---lower than inference (0.33) but still substantial.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fine-tuning variance decomposition (RoBERTa-large).}\n\\label{tab:finetune}\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{lccccc}\n\\toprule\nComponent & SST-2 & MNLI & RTE & COPA & Average \\\\\n\\midrule\nlearning\\_rate  & 15.0\\% & 19.0\\% & 17.0\\% & 16.0\\% & 16.8\\% \\\\\nresidual        & 18.0\\% & 20.0\\% & 19.0\\% & 23.0\\% & 20.0\\% \\\\\nitem\\_id        & 14.0\\% & 11.0\\% & 19.0\\% & 7.0\\%  & 12.8\\% \\\\\nlr:seed         & 11.0\\% & 12.0\\% & 10.0\\% & 11.0\\% & 11.0\\% \\\\\nseed            & 9.0\\%  & 8.0\\%  & 10.0\\% & 9.0\\%  & 9.0\\%  \\\\\nlr:item         & 8.0\\%  & 7.0\\%  & 6.0\\%  & 9.0\\%  & 7.5\\%  \\\\\ndata\\_shuffle   & 6.0\\%  & 5.0\\%  & 5.0\\%  & 7.0\\%  & 5.8\\%  \\\\\nseed:item       & 5.0\\%  & 4.0\\%  & 4.0\\%  & 6.0\\%  & 4.8\\%  \\\\\ngpu             & 3.0\\%  & 3.0\\%  & 3.0\\%  & 3.0\\%  & 3.0\\%  \\\\\nprecision       & 2.0\\%  & 2.5\\%  & 1.8\\%  & 2.2\\%  & 2.1\\%  \\\\\nall other       & 9.0\\%  & 8.5\\%  & 5.2\\%  & 6.8\\%  & 7.4\\%  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\nThe correlation between inference and fine-tuning variance shares is low (Pearson $r$ = 0.18, Spearman $\\rho$ = 0.22; Table~\\ref{tab:inf_ft_corr}).\nThis means that reproducibility analyses conducted on inference cannot predict the variance structure of fine-tuning, and vice versa.\n\n\\begin{table}[t]\n\\centering\n\\caption{Inference vs.\\ fine-tuning variance structure comparison.}\n\\label{tab:inf_ft_corr}\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nPearson $r$ (variance shares) & 0.18 \\\\\nSpearman $\\rho$ (component ranks) & 0.22 \\\\\nLargest in inference    & item\\_id (37.8\\%) \\\\\nLargest in fine-tuning  & learning\\_rate (16.8\\%) \\\\\nitem\\_id rank shift     & 1st $\\to$ 3rd \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Experiment 7: LayerCast Precision Mitigation}\n\nLayerCast (FP16 storage + FP32 compute) achieves accuracy of 0.671, between FP16 (0.670) and BF16 (0.672).\nWith four precision levels, precision accounts for 1.3\\% and precision:item for 4.0\\% of total variance.\nLayerCast addresses $<$2\\% of total variance, confirming that precision is not a first-order concern once engine confounds are controlled.\n\n\\begin{table}[t]\n\\centering\n\\caption{Precision conditions including LayerCast (MMLU, pooled across models).}\n\\label{tab:layercast}\n\\begin{tabular}{lccc}\n\\toprule\nCondition & Accuracy & \\multicolumn{2}{c}{4-level decomposition} \\\\\n\\cmidrule(lr){3-4}\n & & Precision & Precision:item \\\\\n\\midrule\nFP32      & 0.668 & \\multirow{4}{*}{1.3\\%} & \\multirow{4}{*}{4.0\\%} \\\\\nBF16      & 0.672 & & \\\\\nFP16      & 0.670 & & \\\\\nLayerCast & 0.671 & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Experiment 8: MATH Benchmark Extension}\n\\label{sec:exp8}\n\nAdding MATH completes a 5-benchmark spectrum (Table~\\ref{tab:5bench}).\nMATH item dominance is 38.0\\%---nearly identical to MMLU (37.8\\%)---definitively ruling out a systematic gradient linked to task type.\nThe 5-benchmark spread remains 9pp (33\\%--42\\%), and the ordering (GSM8K $>$ MATH $\\approx$ MMLU $>$ ARC $>$ HellaSwag) is non-monotonic with respect to any simple knowledge--reasoning axis.\n\n\\begin{table}[t]\n\\centering\n\\caption{Full 5-benchmark spectrum. No systematic gradient; item dominance is predicted by difficulty distribution shape, not task type.}\n\\label{tab:5bench}\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{llcccccc}\n\\toprule\nBenchmark & Type & item\\_id & residual & temp:item & seed:item & $G$ & Items $G{\\geq}0.90$ \\\\\n\\midrule\nMMLU      & Knowledge      & 37.8\\% & 20.2\\% & 5.8\\% & 1.6\\% & 0.32 & 480 \\\\\nGSM8K     & Math           & 42.0\\% & 22.0\\% & 8.0\\% & 6.0\\% & 0.30 & 420 \\\\\nARC       & Science        & 36.0\\% & 20.0\\% & 6.0\\% & 4.0\\% & 0.35 & 450 \\\\\nHellaSwag & Commonsense    & 33.0\\% & 18.0\\% & 7.0\\% & 5.0\\% & 0.36 & 440 \\\\\nMATH      & Hard reasoning & 38.0\\% & 24.0\\% & 9.0\\% & 7.0\\% & 0.28 & 520 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\nTable~\\ref{tab:bimodality} reveals a strong mechanistic predictor: item difficulty bimodality.\nThe correlation between bimodality index and item variance share is $r = 0.95$.\nBenchmarks with bimodal difficulty distributions (items that are either very easy or very hard for 8B models) produce higher item variance, regardless of whether they test knowledge or reasoning.\n\n\\begin{table}[t]\n\\centering\n\\caption{Difficulty distribution shape predicts item dominance ($r = 0.95$).}\n\\label{tab:bimodality}\n\\begin{tabular}{lccc}\n\\toprule\nBenchmark & Difficulty SD & Bimodality Index & item\\_id \\\\\n\\midrule\nGSM8K     & 0.34 & 0.72 & 42.0\\% \\\\\nMATH      & 0.33 & 0.70 & 38.0\\% \\\\\nMMLU      & 0.30 & 0.65 & 37.8\\% \\\\\nARC       & 0.27 & 0.52 & 36.0\\% \\\\\nHellaSwag & 0.22 & 0.38 & 33.0\\% \\\\\n\\midrule\n$r$ with item\\_id & $r$=0.92 & $r$=0.95 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n% 5. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Variance decomposition as measurement.}\nThe central message of this work is epistemological: a variance decomposition is a measurement, and like all measurements, it has its own error.\nThe field has treated variance component estimates as factual attributions---``item selection accounts for $X$\\% of variance''---without acknowledging that $X$ depends on which items were sampled (CV = 33\\%), which model specification was chosen (37.8\\% vs.\\ 15.2\\%), which estimation method was applied (Henderson vs.\\ REML: $\\Delta$ = 5.7pp), and which facets were included in the design (adding hardware drops item variance by 4.8pp).\nEvery single one of these analyst degrees of freedom shifts the decomposition qualitatively.\n\n\\paragraph{The model$\\times$item interaction.}\nAt 33\\% of total variance under the crossed design, model$\\times$item interaction is the single largest component and has been entirely overlooked.\nThis component represents differential item functioning across models: items that are easy for one architecture may be hard for another, due to differences in tokenization, attention mechanisms, and training data.\nTreating model as fixed---the universal practice in prior work---absorbs this interaction into item variance, producing the misleading impression that items have stable intrinsic difficulty.\nThis finding challenges a core assumption shared by both G-theory and IRT approaches to evaluation: that item difficulty is a property of items rather than of item--model pairs.\n\n\\paragraph{The non-gradient.}\nWe found no systematic cross-benchmark variance gradient.\nThe 9pp spread in item dominance across five benchmarks is non-monotonic and falls within the noise range established by resampling instability.\nItem dominance is predicted not by task taxonomy (knowledge vs.\\ reasoning) but by item difficulty distribution shape (bimodality index $r = 0.95$ with item variance).\nThis has practical implications: benchmark designers can predict whether their item pool will produce item-dominated variance by examining the difficulty distribution, without running a full G-study.\n\n\\paragraph{Budgets need error bars.}\nD-study projections converge across benchmarks (420--520 items for $G \\geq 0.90$, range = 60), eliminating the hoped-for contribution of benchmark-specific budgets.\nMore importantly, the bootstrap CIs ($\\pm$190 items) dwarf this range.\nA recommendation of ``use 480 items for reliable MMLU evaluation'' is more honestly stated as ``use somewhere between 380 and 560 items''---not actionable without further qualification.\nReproducibility budgets must themselves report uncertainty, a meta-methodological requirement that no prior work has identified.\n\n\\paragraph{Separability depends on scope.}\nSeparability of infrastructure and methodology factors holds approximately on MMLU under single-GPU binary scoring (1.5\\%), but fails on GSM8K (4.5\\%), fails when hardware is added to the design (5.5\\%), and fails when model is treated as a facet.\nThe apparent separability in prior isolated-factor studies may be an artifact of restricted experimental scope.\n\n\\paragraph{Limitations.}\nOur study uses open-weight models only; API models with opaque infrastructure may exhibit different variance structures.\nThe 14B extension ($n$=2 models) confounds scale with architecture.\nFine-tuning analysis uses encoder-only RoBERTa; decoder fine-tuning is substantially more expensive.\nItem resampling stability was tested on one model (Llama-3.1-8B) and one benchmark (MMLU); the CV may differ for other configurations.\n\n% ============================================================\n% 6. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe conducted a multi-benchmark G-theory analysis of LLM evaluation variance with the goal of producing reproducibility budgets.\nInstead, we discovered that the variance decomposition underlying such budgets is itself unreliable: item dominance estimates have a CV of 33\\% across item samples, the model$\\times$item interaction (33\\%) is systematically hidden by standard model-as-fixed analyses, and D-study budget projections carry $\\pm$190-item confidence intervals that render benchmark-specific recommendations statistically meaningless.\n\nThese findings do not invalidate G-theory as a framework for evaluation analysis.\nThey do establish that single-run variance decompositions---the current standard---are insufficient for reliable attribution.\nWe recommend that future variance decomposition studies (1) report resampling stability via bootstrap or jackknife CIs, (2) treat model as a crossed facet rather than fixed, and (3) accompany D-study budget recommendations with uncertainty intervals.\n\nVariance decomposition is a powerful lens for understanding evaluation variability.\nBut a lens with unmeasured distortion misleads more than it illuminates.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[Biderman et~al.(2024)]{biderman2024lessons}\nS.~Biderman, et~al.\n\\newblock Lessons from the trenches on reproducible evaluation of language models.\n\\newblock \\emph{arXiv preprint arXiv:2405.14782}, 2024.\n\n\\bibitem[Bouthillier et~al.(2021)]{bouthillier2021accounting}\nX.~Bouthillier, P.~Delaunay, M.~Bronzi, et~al.\n\\newblock Accounting for variance in machine learning benchmarks.\n\\newblock \\emph{Proceedings of Machine Learning and Systems}, 3, 2021.\n\n\\bibitem[Brennan(2001)]{brennan2001generalizability}\nR.~L. Brennan.\n\\newblock \\emph{Generalizability Theory}.\n\\newblock Springer, 2001.\n\n\\bibitem[Brittlebench(2026)]{brittlebench2026}\nBrittlebench Team.\n\\newblock Brittlebench: How fragile are LLM evaluations?\n\\newblock \\emph{arXiv preprint}, 2026.\n\n\\bibitem[Dehghani et~al.(2021)]{dehghani2021benchmark}\nM.~Dehghani, Y.~Tay, A.~A. Gritsenko, et~al.\n\\newblock The benchmark lottery.\n\\newblock \\emph{arXiv preprint arXiv:2107.07002}, 2021.\n\n\\bibitem[Dodge et~al.(2020)]{dodge2020fine}\nJ.~Dodge, G.~Ilharco, R.~Schwartz, et~al.\n\\newblock Fine-tuning pretrained language models: Weight initializations, data orders, and early stopping.\n\\newblock \\emph{arXiv preprint arXiv:2002.06305}, 2020.\n\n\\bibitem[Henderson et~al.(2018)]{henderson2018deep}\nP.~Henderson, R.~Islam, P.~Bachman, et~al.\n\\newblock Deep reinforcement learning that matters.\n\\newblock In \\emph{Proceedings of AAAI}, 2018.\n\n\\bibitem[Hua et~al.(2025)]{hua2025emnlp}\nH.~Hua, et~al.\n\\newblock Generation-based evaluation eliminates scoring artifacts in LLM benchmarks.\n\\newblock In \\emph{Proceedings of EMNLP}, 2025.\n\n\\bibitem[Lalor et~al.(2019)]{lalor2019learning}\nJ.~P. Lalor, H.~Wu, H.~Yu.\n\\newblock Learning latent parameters without human response patterns: Item response theory with artificial crowds.\n\\newblock In \\emph{Proceedings of NAACL-HLT}, 2019.\n\n\\bibitem[Lu et~al.(2022)]{lu2022fantastically}\nY.~Lu, M.~Bartolo, A.~Moore, et~al.\n\\newblock Fantastically ordered prompts and where to find them: Overcoming few-shot prompt order sensitivity.\n\\newblock In \\emph{Proceedings of ACL}, 2022.\n\n\\bibitem[Mesting(2026)]{mesting2026generalizability}\nB.~Mesting.\n\\newblock A generalizability theory analysis of LLM-as-judge evaluation.\n\\newblock \\emph{arXiv preprint}, 2026.\n\n\\bibitem[Messina \\& Scotta(2026)]{messina2026floating}\nP.~Messina and M.~Scotta.\n\\newblock Floating-point non-associativity in neural network inference.\n\\newblock \\emph{arXiv preprint}, 2026.\n\n\\bibitem[Perlitz et~al.(2023)]{perlitz2023efficient}\nY.~Perlitz, E.~Bandel, et~al.\n\\newblock Efficient benchmarking of language models.\n\\newblock \\emph{arXiv preprint arXiv:2308.11696}, 2023.\n\n\\bibitem[Pezeshkpour \\& Hruschka(2024)]{pezeshkpour2024large}\nP.~Pezeshkpour and E.~Hruschka.\n\\newblock Large language models sensitivity to the order of options in multiple-choice questions.\n\\newblock \\emph{arXiv preprint arXiv:2308.11483}, 2024.\n\n\\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}\nF.~M. Polo, L.~Weber, L.~Choshen, et~al.\n\\newblock tinybenchmarks: Evaluating LLMs with fewer examples.\n\\newblock \\emph{arXiv preprint arXiv:2402.14992}, 2024.\n\n\\bibitem[Rodriguez et~al.(2021)]{rodriguez2021evaluation}\nP.~Rodriguez, J.~Barrow, A.~M. Hoyle, et~al.\n\\newblock Evaluation examples are not equally informative: How should that change NLP leaderboards?\n\\newblock In \\emph{Proceedings of ACL}, 2021.\n\n\\bibitem[Sellam et~al.(2022)]{sellam2022multiBERTs}\nT.~Sellam, S.~Yadlowsky, I.~Tenney, et~al.\n\\newblock The MultiBERTs: BERT reproductions for robustness analysis.\n\\newblock In \\emph{Proceedings of ICLR}, 2022.\n\n\\bibitem[Shavelson \\& Webb(1991)]{shavelson1991generalizability}\nR.~J. Shavelson and N.~M. Webb.\n\\newblock \\emph{Generalizability Theory: A Primer}.\n\\newblock SAGE Publications, 1991.\n\n\\bibitem[Vania et~al.(2021)]{vania2021comparing}\nC.~Vania, et~al.\n\\newblock Comparing test sets with item response theory.\n\\newblock In \\emph{Proceedings of ACL}, 2021.\n\n\\bibitem[Yuan et~al.(2025)]{yuan2025llm}\nZ.~Yuan, et~al.\n\\newblock Do LLM evaluations converge across hardware? Up to 9\\% accuracy variation from GPU and precision choices.\n\\newblock \\emph{arXiv preprint}, 2025.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1b9053f-a0bf-48e0-9be8-2b6900dfd446",
  "isSidechain": false,
  "requestId": "req_011CbEghRX5j4yV73YKrVGVV",
  "type": "assistant",
  "uuid": "308d83ce-fc19-45ae-8321-ef9c29b68a7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PPHhyJzQNqEmUKTSGrQJ9e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 496,
      "cache_read_input_tokens": 43765,
      "output_tokens": 14676,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 496,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14676,
          "cache_read_input_tokens": 43765,
          "cache_creation_input_tokens": 496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 496
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

_source line 20 · 2026-05-20T23:30:20.777Z_

<details><summary>↩ Tool result · `toolu_012A7hrgXPEqhfvijd4SHETb`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "308d83ce-fc19-45ae-8321-ef9c29b68a7d",
  "isSidechain": false,
  "promptId": "373fec7c-0384-4178-9c36-2cd6143072a3",
  "type": "user",
  "uuid": "36531159-512c-4461-b810-bdc9a9bdf43c",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{adjustbox}\n\n\\title{Variance Decomposition Is a Measurement, Not a Fact:\\\\\nOn the Instability of Reproducibility Budgets for LLM Evaluation}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nWe set out to build reproducibility budgets for LLM evaluation using Generalizability Theory (G-theory) and discovered that the budget itself is unreliable.\nIn a multi-benchmark G-study crossing infrastructure (numerical precision, hardware) $\\times$ methodology (prompt, seed, temperature, ordering) $\\times$ measurement (item) factors across four models and five benchmarks (172{,}800--230{,}400 observations per experiment), we find three results that challenge current variance-attribution practices.\nFirst, item dominance estimates are sample-unstable: resampling 200 MMLU items with different stratified seeds yields item variance shares ranging from 25\\% to 48\\% (CV\\,=\\,0.33), meaning prior single-decomposition studies---including all existing G-theory analyses of LLM evaluation---over-commit to attribution certainty.\nSecond, treating model as fixed (the standard practice) systematically inflates item variance from 37.8\\% to an apparent dominance; a model-as-facet reanalysis reveals that model$\\times$item interaction (33\\%) is the single largest component, reducing pure item variance to 15.2\\%.\nThird, D-study reproducibility budgets converge across benchmarks (range = 60 items for $G \\geq 0.90$) but carry bootstrap confidence intervals of $\\pm$190 items, rendering benchmark-specific budget recommendations statistically indistinguishable and demanding that budgets themselves report uncertainty.\nThese findings reframe variance decomposition from a factual attribution to a measurement with its own error, requiring uncertainty quantification before actionable conclusions can be drawn.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nWhen LLM evaluation results fail to replicate, the natural response is to identify the culprit: was it the prompt, the random seed, the GPU, the numerical precision, or the item selection?\nA growing body of work has pursued this question by decomposing evaluation variance into attributable sources \\citep{bouthillier2021accounting, mesting2026generalizability, brittlebench2026}.\nThese studies report point estimates of variance shares---``item selection accounts for 43.8\\% of variance'' \\citep{mesting2026generalizability}, ``prompt sensitivity explains 50\\% of score variation'' \\citep{brittlebench2026}---and derive practical recommendations from them.\n\nWe conducted a large-scale G-theory study with the same goal: cross infrastructure and methodology factors in a unified framework, measure variance components across five benchmarks, and produce reproducibility budgets telling practitioners how many items, prompts, and seeds they need.\nWhat we found instead is that \\emph{the variance decomposition itself is unstable}.\nThree independent item samples of 200 MMLU questions yield item dominance estimates of 48\\%, 25\\%, and 41\\%---a coefficient of variation of 33\\%.\nWhich items happen to be sampled determines not just the magnitude but the \\emph{rank order} of variance components: in one sample, the residual exceeds item variance as the largest component.\nEvery prior study that reports a single variance decomposition without resampling stability analysis has, in effect, presented one draw from a high-variance distribution as a finding.\n\nThis instability compounds with a second problem: model specification.\nStandard practice treats model as fixed and pools across models or analyzes each separately.\nWhen we instead treat model as a crossed random facet, item variance drops from 37.8\\% to 15.2\\%, with the difference absorbed by a model$\\times$item interaction of 33\\%---the largest single component in the crossed design.\nItem ``difficulty'' is not an intrinsic property of items but a joint property of item--model pairs, a conclusion that fundamentally challenges the premise of item-dominated variance attribution.\n\nA third discovery concerns reproducibility budgets themselves.\nD-study projections for $G \\geq 0.90$ converge across benchmarks (420--520 items, range = 60), which would seem to simplify practical recommendations.\nBut the bootstrap 95\\% confidence intervals span $\\pm$190 items---wider than the cross-benchmark range---meaning any specific budget recommendation is statistically indistinguishable from its neighbors.\nReproducibility budgets require their own error bars.\n\nOur contributions are:\n\\begin{enumerate}\n\\item Evidence that variance component estimates in LLM evaluation are sample-unstable (item resampling CV\\,=\\,0.33, component rank inversions across samples), establishing that single-run decompositions over-commit to attribution certainty.\n\\item A model-as-facet reanalysis showing that model$\\times$item interaction (33\\%) is the largest overlooked variance source, and that treating model as fixed inflates item dominance by $>$22 percentage points.\n\\item A demonstration that D-study reproducibility budgets require uncertainty quantification: cross-benchmark budget convergence (range = 60 items) is dominated by within-benchmark CI width ($\\pm$190 items), rendering benchmark-specific recommendations unreliable.\n\\end{enumerate}\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Variance decomposition in ML evaluation.}\n\\citet{bouthillier2021accounting} introduced factorial variance decomposition to ML benchmarking via ANOVA, decomposing performance variation across hyperparameters, data splits, and random seeds.\n\\citet{henderson2018deep} applied similar methods to deep reinforcement learning, finding that implementation details dominate reported improvements.\n\\citet{dodge2020fine} and \\citet{sellam2022multiBERTs} documented fine-tuning instability from seed and data order in BERT-scale models.\nThese studies establish the paradigm we build on but do not address LLM inference evaluation or apply G-theory's D-study projections.\n\n\\paragraph{G-theory in LLM evaluation.}\n\\citet{mesting2026generalizability} adapted Generalizability Theory to LLM-as-judge evaluation, decomposing variance across five methodological facets.\nTheir study treats model and infrastructure as fixed, reports single-run point estimates without resampling stability analysis, and covers one benchmark.\n\\citet{brittlebench2026} quantified prompt sensitivity at up to 50\\% of score variation on fixed hardware.\nNeither study crosses infrastructure with methodology or tests the stability of their decomposition.\n\n\\paragraph{Item-level analysis and IRT.}\nItem Response Theory has been applied to NLP evaluation for item analysis \\citep{lalor2019learning, rodriguez2021evaluation, vania2021comparing}, efficient subsampling \\citep{polo2024tinybenchmarks, perlitz2023efficient}, and the Benchmark Lottery phenomenon \\citep{dehghani2021benchmark}.\nThese approaches model item properties but do not decompose evaluation variance into infrastructure vs.\\ methodology sources.\n\n\\paragraph{Reproducibility factors.}\n\\citet{yuan2025llm} documented up to 9\\% accuracy variation from hardware and numerical precision without factorial attribution.\n\\citet{lu2022fantastically, pezeshkpour2024large} studied option ordering effects in multiple-choice evaluation.\n\\citet{biderman2024lessons} surveyed evaluation reproducibility challenges.\nEach isolates at most two factors, implicitly assuming separability.\n\n% ============================================================\n% 3. METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{Generalizability Theory Framework}\n\nGeneralizability Theory (G-theory; \\citealp{shavelson1991generalizability, brennan2001generalizability}) decomposes observed score variance into components attributable to facets (e.g., items, prompts, seeds) and their interactions.\nFor a fully crossed design with $k$ facets, a person's observed score $X_{p}$ is:\n\\begin{equation}\nX_{pijk\\ldots} = \\mu + \\alpha_p + \\beta_i + \\gamma_j + \\delta_k + (\\alpha\\beta)_{pi} + (\\alpha\\gamma)_{pj} + \\cdots + \\epsilon_{pijk\\ldots}\n\\end{equation}\nwhere each Greek letter represents the effect of a facet or interaction and $\\epsilon$ is residual error.\nThe G-coefficient summarizes measurement dependability:\n\\begin{equation}\nG = \\frac{\\sigma^2_p}{\\sigma^2_p + \\sigma^2_{\\text{relative error}}}\n\\end{equation}\nD-studies project $G$ under hypothetical facet sample sizes, enabling reproducibility budget planning.\n\n\\subsection{Experimental Design}\n\nWe conduct a series of experiments with increasing scope.\nAll experiments use generation-based evaluation (following \\citealp{hua2025emnlp}) with vLLM 0.9.2 and \\texttt{enforce\\_eager} mode to eliminate engine-level confounds.\n\n\\paragraph{Experiment 1: Full-scale precision study.}\n4 models (Qwen3-8B, Llama-3.1-8B, Gemma-2-9B, Mistral-7B) $\\times$ 3 precisions (FP32, BF16, FP16) $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 3 temperatures $\\times$ 4 orderings $\\times$ 200 MMLU items = 172{,}800 observations.\nModel is initially treated as fixed (analyzed per-model and pooled); Experiment 4 reanalyzes with model as a crossed facet.\n\n\\paragraph{Experiment 1b: Item resampling stability.}\n3 independent stratified 200-item MMLU samples (seeds 0, 7, 99) $\\times$ Llama-3.1-8B $\\times$ 3 precisions $\\times$ 3 prompts $\\times$ 3 seeds $\\times$ 2 orderings = 54 conditions per sample, 10{,}800 observations per sample.\n\n\\paragraph{Experiment 2: Multi-benchmark replication.}\n4 models $\\times$ 2 precisions $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 2 temperatures $\\times$ 4 orderings on GSM8K, ARC-Challenge, and HellaSwag (200 items each), 76{,}800 observations per benchmark.\n\n\\paragraph{Experiment 3: Multi-hardware G-study.}\n4 models $\\times$ 2 GPU types $\\times$ 2 precisions $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 3 temperatures $\\times$ 4 orderings $\\times$ 200 MMLU items = 230{,}400 observations.\n\n\\paragraph{Experiment 4: Comprehensive reanalysis.}\nMerged data from Experiments 1--3. Model-as-facet reanalysis, 1{,}000-replicate bootstrap CIs on all variance components, D-study projections with uncertainty quantification, and REML sensitivity analysis.\n\n\\paragraph{Experiment 5: Scale extension.}\nQwen3-14B and DeepSeek-R1-Distill-14B at BF16/FP16, testing whether 14B models alter variance structure.\n\n\\paragraph{Experiment 6: Fine-tuning G-study.}\nRoBERTa-large on SST-2, MNLI, RTE, COPA. 6 seeds $\\times$ 3 learning rates $\\times$ 4 data shuffles $\\times$ 3 GPUs $\\times$ 2 precisions = 432 runs per task, 1{,}728 total.\n\n\\paragraph{Experiment 7: LayerCast precision mitigation.}\nFP16 storage + FP32 compute as a fourth precision condition on MMLU.\n\n\\paragraph{Experiment 8: MATH benchmark extension.}\n200 MATH items under the same multi-benchmark protocol, completing a 5-benchmark spectrum.\n\n% ============================================================\n% 4. EXPERIMENTS AND RESULTS\n% ============================================================\n\\section{Experiments and Results}\n\n\\subsection{Experiment 1: Variance Decomposition Under Model-as-Fixed Analysis}\n\\label{sec:exp1}\n\nTable~\\ref{tab:exp1_variance} presents the variance decomposition from the full-scale MMLU study with model treated as fixed.\nAt face value, item selection is the largest component (37.8\\% pooled), with substantial variation across models: Qwen3-8B shows the highest item dominance (42.2\\%) while Mistral-7B shows the lowest (30.3\\%, CV across models = 0.13).\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance components under model-as-fixed analysis (MMLU, binary scoring, 200 items). These point estimates are subsequently shown to be unstable (Sec.~\\ref{sec:exp1b}) and inflated (Sec.~\\ref{sec:exp4}).}\n\\label{tab:exp1_variance}\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{lccccc}\n\\toprule\nComponent & Qwen3-8B & Llama-3.1-8B & Gemma-2-9B & Mistral-7B & Pooled \\\\\n\\midrule\nitem\\_id         & 42.2\\% & 35.8\\% & 40.1\\% & 30.3\\% & 37.8\\% \\\\\nresidual         & 17.4\\% & 21.2\\% & 18.8\\% & 26.1\\% & 20.2\\% \\\\\ntemperature:item & 6.3\\%  & 5.9\\%  & 5.2\\%  & 5.8\\%  & 5.8\\%  \\\\\nprompt:item      & 5.8\\%  & 5.4\\%  & 4.8\\%  & 4.2\\%  & 5.2\\%  \\\\\nprecision:item   & 4.9\\%  & 4.6\\%  & 4.2\\%  & 3.8\\%  & 4.5\\%  \\\\\nseed:item        & 1.8\\%  & 1.7\\%  & 1.4\\%  & 1.3\\%  & 1.6\\%  \\\\\nordering:item    & 1.4\\%  & 1.2\\%  & 1.1\\%  & 0.9\\%  & 1.2\\%  \\\\\nprecision        & 1.8\\%  & 1.7\\%  & 1.5\\%  & 1.3\\%  & 1.6\\%  \\\\\ntemperature      & 1.2\\%  & 1.0\\%  & 0.9\\%  & 0.8\\%  & 1.0\\%  \\\\\nprompt           & 0.8\\%  & 0.7\\%  & 0.6\\%  & 0.5\\%  & 0.7\\%  \\\\\nprec.:temp.      & 1.6\\%  & 1.5\\%  & 1.4\\%  & 1.2\\%  & 1.5\\%  \\\\\nall other        & 14.8\\% & 19.3\\% & 20.0\\% & 23.8\\% & 18.9\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\nPrecision main effects are small after confound correction (1.6\\% pooled), and accuracy differences across FP32 (0.668), BF16 (0.672), and FP16 (0.670) are negligible ($\\Delta_{\\max}$ = 0.004 for each model).\nThe $G$-coefficient under binary scoring is 0.32, reflecting the inherent low reliability of binary item scoring with 200 items.\nThe precision$\\times$temperature interaction (1.5\\%) is non-negligible but does not by itself break separability.\n\nThese results appear to support an item-dominance narrative.\nHowever, as we show next, this narrative is an artifact of two methodological choices: a single item sample and a fixed-model specification.\n\n\\subsection{Experiment 1b: Item Resampling Instability}\n\\label{sec:exp1b}\n\nTable~\\ref{tab:resample} presents the variance decomposition under three independent stratified 200-item MMLU samples.\nThe item variance share ranges from 25.0\\% (Sample~7) to 48.0\\% (Sample~0), yielding a coefficient of variation of 0.33.\nThis instability is not merely quantitative: in Sample~7, the residual (30.0\\%) exceeds item variance (25.0\\%) as the largest component, producing a qualitatively different decomposition.\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance decomposition across three independent item samples (Llama-3.1-8B, MMLU). Item dominance is sample-dependent, with rank inversions across samples.}\n\\label{tab:resample}\n\\begin{tabular}{lcccccc}\n\\toprule\nComponent & Sample 0 & Sample 7 & Sample 99 & Mean & SD & CV \\\\\n\\midrule\nitem\\_id        & 48.0\\% & 25.0\\% & 41.0\\% & 38.0\\% & 12.0\\% & 0.33 \\\\\nresidual        & 16.0\\% & 30.0\\% & 19.0\\% & 21.7\\% & 7.5\\%  & 0.35 \\\\\ntemperature:item& 7.2\\%  & 9.8\\%  & 8.1\\%  & 8.4\\%  & 1.3\\%  & 0.16 \\\\\nprompt:item     & 5.6\\%  & 8.2\\%  & 6.4\\%  & 6.7\\%  & 1.3\\%  & 0.20 \\\\\nprecision:item  & 4.8\\%  & 6.4\\%  & 5.2\\%  & 5.5\\%  & 0.8\\%  & 0.15 \\\\\ntemperature     & 1.0\\%  & 2.4\\%  & 1.4\\%  & 1.6\\%  & 0.7\\%  & 0.46 \\\\\nprompt          & 0.6\\%  & 1.8\\%  & 0.9\\%  & 1.1\\%  & 0.6\\%  & 0.58 \\\\\nall other       & 16.8\\% & 16.4\\% & 18.0\\% & 17.1\\% & 0.8\\%  & 0.05 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:resample_stability} shows that the $G$-coefficient itself varies from 0.28 to 0.38 across samples (CV\\,=\\,0.16), and the largest-component identity is not stable.\nThe bootstrap 95\\% CI on item variance is [0.27, 0.48] (width = 0.21), wide enough that it cannot distinguish between ``item dominance'' ($>$40\\%) and ``item is one of several comparable sources'' ($\\sim$25\\%).\n\n\\begin{table}[t]\n\\centering\n\\caption{$G$-coefficient and rank stability across item samples. The rank order of variance components is not stable: Sample~7 reverses the top two components.}\n\\label{tab:resample_stability}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Sample 0 & Sample 7 & Sample 99 \\\\\n\\midrule\n$G$ (correct)       & 0.28     & 0.38     & 0.31 \\\\\nLargest component    & item\\_id & residual & item\\_id \\\\\n2nd largest          & residual & item\\_id & residual \\\\\n3rd largest          & temp:item& temp:item& temp:item \\\\\nItem difficulty SD   & 0.31     & 0.22     & 0.27 \\\\\nBimodality index     & 0.71     & 0.38     & 0.58 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe mechanism is traceable: Sample~0 draws more items with extreme difficulty (bimodality index = 0.71), which naturally produce high item-level variance; Sample~7 draws items with more uniform difficulty (bimodality index = 0.38), compressing item variance.\nMMLU's 57 subjects have heterogeneous difficulty distributions---STEM subjects tend bimodal, humanities more uniform---and 200-item stratified sampling balances at the subject level but not within subjects.\n\nThis result is the centerpiece of the paper.\nPrior work reports single variance decompositions as findings \\citep{mesting2026generalizability, brittlebench2026, bouthillier2021accounting}.\nA CV of 33\\% means that if \\citet{mesting2026generalizability} had used different items, her 43.8\\% judge-dominance estimate might have been 30\\% or 55\\%.\nVariance decomposition is a measurement with its own measurement error, and that error has been systematically ignored.\n\n\\subsection{Experiment 2: Multi-Benchmark Replication}\n\\label{sec:exp2}\n\nTable~\\ref{tab:multi_bench} extends the analysis to four benchmarks.\nItem variance ranges from 33.0\\% (HellaSwag) to 42.0\\% (GSM8K), a spread of only 9 percentage points.\nThe ordering is GSM8K $>$ MMLU $>$ ARC $>$ HellaSwag, which does not follow the predicted knowledge$\\to$reasoning gradient (Table~\\ref{tab:gradient_test}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Item dominance across benchmarks (model-as-fixed). No systematic gradient exists; spread = 9pp.}\n\\label{tab:multi_bench}\n\\begin{tabular}{lcccccc}\n\\toprule\nBenchmark & item\\_id & residual & temp:item & prompt:item & seed:item & $G$ \\\\\n\\midrule\nMMLU         & 37.8\\% & 20.2\\% & 5.8\\% & 5.2\\% & 1.6\\% & 0.32 \\\\\nGSM8K        & 42.0\\% & 22.0\\% & 8.0\\% & 5.0\\% & 6.0\\% & 0.30 \\\\\nARC-Challenge& 36.0\\% & 20.0\\% & 6.0\\% & 7.0\\% & 4.0\\% & 0.35 \\\\\nHellaSwag    & 33.0\\% & 18.0\\% & 7.0\\% & 4.0\\% & 5.0\\% & 0.36 \\\\\n\\midrule\nSpread       & 9pp    & 4pp    & 2pp   & 3pp   & 4pp   & ---  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{The predicted cross-benchmark gradient does not match observations.}\n\\label{tab:gradient_test}\n\\begin{tabular}{lll}\n\\toprule\nPredicted & Observed & Match \\\\\n\\midrule\nMMLU $>$ ARC $>$ GSM8K & GSM8K $>$ MMLU $>$ ARC $>$ HellaSwag & No \\\\\nMonotonic decrease with reasoning & Non-monotonic & No \\\\\nSpread $>$ 15pp for meaningful gradient & Spread = 9pp & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGSM8K's high item dominance (42\\%) despite being a reasoning benchmark is explained by its bimodal difficulty distribution: items range from trivial single-step arithmetic (accuracy $>$95\\%) to complex multi-step problems (accuracy $<$15\\%) for 8B-class models, and this bimodality inflates item-level variance.\nHellaSwag shows the lowest item dominance (33\\%) not because of task type but because its items have more uniform difficulty for these models.\n\nSuperimposed on the resampling instability from Experiment~1b (CV $>$ 30\\%), the 9pp spread falls within the noise range.\nThere is no evidence for a systematic cross-benchmark variance gradient.\n\n\\paragraph{Separability under binary scoring.}\nTable~\\ref{tab:separability} shows infrastructure$\\times$methodology interactions across benchmarks.\nOn MMLU, the total infra$\\times$method interaction is small (1.5\\%), but on GSM8K it reaches 4.5\\%, driven by precision$\\times$seed (1.5\\%) and precision$\\times$temperature (1.8\\%) interactions.\nSeparability does not hold uniformly across benchmarks under binary scoring.\n\n\\begin{table}[t]\n\\centering\n\\caption{Separability test (binary scoring). Infrastructure$\\times$methodology interactions exceed 3\\% on GSM8K and HellaSwag.}\n\\label{tab:separability}\n\\begin{tabular}{lcccc}\n\\toprule\nBenchmark & prec.$\\times$prompt & prec.$\\times$seed & prec.$\\times$temp & Total infra$\\times$method \\\\\n\\midrule\nMMLU         & 0.3\\% & 0.2\\% & 1.0\\% & 1.5\\% \\\\\nGSM8K        & 1.2\\% & 1.5\\% & 1.8\\% & 4.5\\% \\\\\nARC-Challenge& 0.4\\% & 0.3\\% & 1.3\\% & 2.0\\% \\\\\nHellaSwag    & 0.8\\% & 1.0\\% & 1.7\\% & 3.5\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Experiment 3: Multi-Hardware G-Study}\n\\label{sec:exp3}\n\nAdding a second GPU type reveals that hardware is a substantial variance source (Table~\\ref{tab:hardware}).\nTotal hardware-related variance is 14.0\\%, exceeding precision-related variance ($\\sim$6\\%).\nThe hardware$\\times$item interaction (6.0\\%) indicates that specific items flip between correct and incorrect across GPU architectures due to differences in tensor core implementations and floating-point rounding.\n\n\\begin{table}[t]\n\\centering\n\\caption{Hardware-related variance components (MMLU, binary scoring).}\n\\label{tab:hardware}\n\\begin{tabular}{lcc}\n\\toprule\nComponent & Variance Share & 95\\% Bootstrap CI \\\\\n\\midrule\nhardware (main)       & 5.0\\% & [3.2\\%, 7.1\\%] \\\\\nhardware:item         & 6.0\\% & [4.1\\%, 8.3\\%] \\\\\nhardware:precision    & 3.5\\% & [2.0\\%, 5.2\\%] \\\\\nhardware:prompt       & 1.5\\% & [0.8\\%, 2.4\\%] \\\\\nhardware:seed         & 2.0\\% & [1.2\\%, 3.1\\%] \\\\\nhardware:temperature  & 1.5\\% & [0.7\\%, 2.5\\%] \\\\\nitem\\_id (with hardware) & 33.0\\% & [25.1\\%, 41.8\\%] \\\\\nresidual              & 18.0\\% & [14.2\\%, 22.5\\%] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCritically, item variance drops from 37.8\\% (single-GPU, Experiment~1) to 33.0\\% when hardware is included as a facet.\nThis demonstrates that item variance in single-hardware designs is inflated by unmodeled hardware$\\times$item interactions---the item component acts as a catch-all for variance from omitted facets.\n\nSeparability fails decisively with hardware in the design (Table~\\ref{tab:sep_hardware}).\nThe total infra$\\times$method interaction increases from 1.5\\% (single-GPU) to 5.5\\% (multi-GPU), and hardware$\\times$methodology accounts for 4.0\\%.\n\n\\begin{table}[t]\n\\centering\n\\caption{Separability with vs.\\ without hardware. Adding hardware breaks separability.}\n\\label{tab:sep_hardware}\n\\begin{tabular}{lccc}\n\\toprule\nInteraction & Single-GPU & Multi-GPU & Separability \\\\\n\\midrule\ninfra$\\times$method (binary) & 1.5\\% & 5.5\\% & Fails ($>$3\\%) \\\\\nprecision$\\times$temperature & 1.5\\% & 1.5\\% & Marginal \\\\\nhardware$\\times$methodology  & N/A   & 4.0\\% & Fails \\\\\nhardware$\\times$precision    & N/A   & 3.5\\% & Fails \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Experiment 4: Model-as-Facet Reanalysis and D-Study Projections}\n\\label{sec:exp4}\n\nTable~\\ref{tab:model_crossed} presents the central methodological finding.\nWhen model is treated as a crossed random facet rather than fixed, item variance drops from 37.8\\% to 15.2\\% ($-$22.6pp), while model$\\times$item interaction emerges at 33.0\\%---the largest single component.\nThis means that what the model-as-fixed analysis attributes to ``item difficulty'' is largely the differential difficulty of items \\emph{across models}: an item that is easy for Qwen3-8B may be hard for Mistral-7B, and this interaction is misattributed to item variance when model is fixed.\n\n\\begin{table}[t]\n\\centering\n\\caption{Model-fixed vs.\\ model-crossed variance decomposition (MMLU, binary scoring). Treating model as fixed inflates item variance by 22.6pp.}\n\\label{tab:model_crossed}\n\\begin{tabular}{lcccc}\n\\toprule\nComponent & Model-Fixed & Model-Crossed & $\\Delta$ & Interpretation \\\\\n\\midrule\nitem\\_id        & 37.8\\% & 15.2\\% & $-$22.6pp & Misattributed to model$\\times$item \\\\\nmodel$\\times$item & ---  & 33.0\\% & +33.0pp  & Largest single component \\\\\nmodel (main)    & ---    & 6.0\\%  & +6.0pp   & Between-model differences \\\\\nresidual        & 20.2\\% & 12.0\\% & $-$8.2pp & Decomposed into model terms \\\\\ntemp:item       & 5.8\\%  & 4.5\\%  & $-$1.3pp & Slight reallocation \\\\\nprompt:item     & 5.2\\%  & 4.0\\%  & $-$1.2pp & Slight reallocation \\\\\nall other       & 31.0\\% & 25.3\\% & $-$5.7pp & Redistributed \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Bootstrap ranking stability.}\nTable~\\ref{tab:bootstrap_rank} shows that across 1{,}000 bootstrap resamples, no single component is consistently the largest.\nItem variance (model-fixed) is ranked first in only 45\\% of resamples; model$\\times$item is first in 38\\%.\nThe rank stability across bootstraps is 0.68---substantially below the level needed for confident attribution claims.\n\n\\begin{table}[t]\n\\centering\n\\caption{Bootstrap ranking stability (1{,}000 resamples). No component is reliably the largest.}\n\\label{tab:bootstrap_rank}\n\\begin{tabular}{lcccc}\n\\toprule\nComponent & Times \\#1 & Times \\#2 & Times \\#3 & Mean Rank \\\\\n\\midrule\nitem\\_id (model-fixed)   & 450 & 320 & 180 & 1.7 \\\\\nmodel$\\times$item        & 380 & 350 & 200 & 1.8 \\\\\nresidual                  & 170 & 330 & 350 & 2.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{D-study reproducibility budgets.}\nTable~\\ref{tab:dstudy} presents D-study projections for achieving $G \\geq 0.90$.\nPoint estimates converge across benchmarks (420--520 items, range = 60), but the 95\\% bootstrap CIs are wide (180--200 items).\nThe cross-benchmark range (60 items) is smaller than any single benchmark's CI width, meaning benchmark-specific budget differences are statistically indistinguishable.\n\n\\begin{table}[t]\n\\centering\n\\caption{D-study: items required for $G \\geq 0.90$. CI widths exceed the cross-benchmark range.}\n\\label{tab:dstudy}\n\\begin{tabular}{lccc}\n\\toprule\nBenchmark & Point Estimate & Bootstrap 95\\% CI & CI Width \\\\\n\\midrule\nMMLU      & 480 & [380, 560] & 180 \\\\\nGSM8K     & 420 & [310, 510] & 200 \\\\\nARC       & 450 & [350, 540] & 190 \\\\\nHellaSwag & 440 & [340, 530] & 190 \\\\\n\\midrule\nCross-benchmark range & 60 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Estimation method sensitivity.}\nThe choice between Henderson Method~I and REML estimation produces a 5.7pp divergence on item variance (37.8\\% vs.\\ 32.1\\%; Table~\\ref{tab:reml}), adding a further source of instability: the ``finding'' depends on which estimation method is used.\n\n\\begin{table}[t]\n\\centering\n\\caption{REML vs.\\ Henderson Method~I. Estimation method choice alters conclusions.}\n\\label{tab:reml}\n\\begin{tabular}{lccc}\n\\toprule\nComponent & Henderson & REML & $\\Delta$ \\\\\n\\midrule\nitem\\_id          & 37.8\\% & 32.1\\% & $-$5.7pp \\\\\nmodel$\\times$item & 33.0\\% & 35.2\\% & +2.2pp \\\\\nresidual          & 20.2\\% & 22.8\\% & +2.6pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Experiment 5: 14B Model Extension}\n\\label{sec:exp5}\n\nAdding 14B models (Table~\\ref{tab:14b}) reduces per-model item dominance (Qwen3-14B: 32.0\\%, DeepSeek-R1-14B: 28.0\\%) relative to 8B models (37.8\\% pooled) and increases model$\\times$item interaction from 33.0\\% to 38.0\\%.\nDeepSeek-R1-Distill-14B exhibits unusually high temperature:item (10.0\\%) and seed:item (8.0\\%) interactions, likely due to its reasoning-distilled architecture amplifying chain-of-thought stochasticity.\nScale and architecture effects are confounded with $n$=2 models and cannot be separated.\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance structure: 8B pooled vs.\\ 14B models vs.\\ all crossed.}\n\\label{tab:14b}\n\\begin{tabular}{lcccc}\n\\toprule\nComponent & 8B Pooled & Qwen3-14B & DeepSeek-R1-14B & All Crossed \\\\\n\\midrule\nitem\\_id (model-fixed) & 37.8\\% & 32.0\\% & 28.0\\% & 34.0\\% \\\\\nmodel$\\times$item (crossed) & 33.0\\% & --- & --- & 38.0\\% \\\\\nresidual                & 20.2\\% & 22.0\\% & 26.0\\% & 16.0\\% \\\\\ntemp:item               & 5.8\\%  & 5.0\\%  & 10.0\\% & 6.5\\%  \\\\\nseed:item               & 1.6\\%  & 1.4\\%  & 8.0\\%  & 3.2\\%  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Experiment 6: Fine-Tuning G-Study}\n\\label{sec:exp6}\n\nTable~\\ref{tab:finetune} presents the fine-tuning variance decomposition.\nThe variance structure differs qualitatively from inference: learning rate (16.8\\% average) replaces item selection as the dominant component, and the lr$\\times$seed interaction (11.0\\%) reflects irreducible optimization landscape stochasticity.\nItem variance in fine-tuning is modest (12.8\\% average) and cross-task unstable (SST-2: 14.0\\%, COPA: 7.0\\%).\nItem resampling CV in fine-tuning is 0.28---lower than inference (0.33) but still substantial.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fine-tuning variance decomposition (RoBERTa-large).}\n\\label{tab:finetune}\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{lccccc}\n\\toprule\nComponent & SST-2 & MNLI & RTE & COPA & Average \\\\\n\\midrule\nlearning\\_rate  & 15.0\\% & 19.0\\% & 17.0\\% & 16.0\\% & 16.8\\% \\\\\nresidual        & 18.0\\% & 20.0\\% & 19.0\\% & 23.0\\% & 20.0\\% \\\\\nitem\\_id        & 14.0\\% & 11.0\\% & 19.0\\% & 7.0\\%  & 12.8\\% \\\\\nlr:seed         & 11.0\\% & 12.0\\% & 10.0\\% & 11.0\\% & 11.0\\% \\\\\nseed            & 9.0\\%  & 8.0\\%  & 10.0\\% & 9.0\\%  & 9.0\\%  \\\\\nlr:item         & 8.0\\%  & 7.0\\%  & 6.0\\%  & 9.0\\%  & 7.5\\%  \\\\\ndata\\_shuffle   & 6.0\\%  & 5.0\\%  & 5.0\\%  & 7.0\\%  & 5.8\\%  \\\\\nseed:item       & 5.0\\%  & 4.0\\%  & 4.0\\%  & 6.0\\%  & 4.8\\%  \\\\\ngpu             & 3.0\\%  & 3.0\\%  & 3.0\\%  & 3.0\\%  & 3.0\\%  \\\\\nprecision       & 2.0\\%  & 2.5\\%  & 1.8\\%  & 2.2\\%  & 2.1\\%  \\\\\nall other       & 9.0\\%  & 8.5\\%  & 5.2\\%  & 6.8\\%  & 7.4\\%  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\nThe correlation between inference and fine-tuning variance shares is low (Pearson $r$ = 0.18, Spearman $\\rho$ = 0.22; Table~\\ref{tab:inf_ft_corr}).\nThis means that reproducibility analyses conducted on inference cannot predict the variance structure of fine-tuning, and vice versa.\n\n\\begin{table}[t]\n\\centering\n\\caption{Inference vs.\\ fine-tuning variance structure comparison.}\n\\label{tab:inf_ft_corr}\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nPearson $r$ (variance shares) & 0.18 \\\\\nSpearman $\\rho$ (component ranks) & 0.22 \\\\\nLargest in inference    & item\\_id (37.8\\%) \\\\\nLargest in fine-tuning  & learning\\_rate (16.8\\%) \\\\\nitem\\_id rank shift     & 1st $\\to$ 3rd \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Experiment 7: LayerCast Precision Mitigation}\n\nLayerCast (FP16 storage + FP32 compute) achieves accuracy of 0.671, between FP16 (0.670) and BF16 (0.672).\nWith four precision levels, precision accounts for 1.3\\% and precision:item for 4.0\\% of total variance.\nLayerCast addresses $<$2\\% of total variance, confirming that precision is not a first-order concern once engine confounds are controlled.\n\n\\begin{table}[t]\n\\centering\n\\caption{Precision conditions including LayerCast (MMLU, pooled across models).}\n\\label{tab:layercast}\n\\begin{tabular}{lccc}\n\\toprule\nCondition & Accuracy & \\multicolumn{2}{c}{4-level decomposition} \\\\\n\\cmidrule(lr){3-4}\n & & Precision & Precision:item \\\\\n\\midrule\nFP32      & 0.668 & \\multirow{4}{*}{1.3\\%} & \\multirow{4}{*}{4.0\\%} \\\\\nBF16      & 0.672 & & \\\\\nFP16      & 0.670 & & \\\\\nLayerCast & 0.671 & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Experiment 8: MATH Benchmark Extension}\n\\label{sec:exp8}\n\nAdding MATH completes a 5-benchmark spectrum (Table~\\ref{tab:5bench}).\nMATH item dominance is 38.0\\%---nearly identical to MMLU (37.8\\%)---definitively ruling out a systematic gradient linked to task type.\nThe 5-benchmark spread remains 9pp (33\\%--42\\%), and the ordering (GSM8K $>$ MATH $\\approx$ MMLU $>$ ARC $>$ HellaSwag) is non-monotonic with respect to any simple knowledge--reasoning axis.\n\n\\begin{table}[t]\n\\centering\n\\caption{Full 5-benchmark spectrum. No systematic gradient; item dominance is predicted by difficulty distribution shape, not task type.}\n\\label{tab:5bench}\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{llcccccc}\n\\toprule\nBenchmark & Type & item\\_id & residual & temp:item & seed:item & $G$ & Items $G{\\geq}0.90$ \\\\\n\\midrule\nMMLU      & Knowledge      & 37.8\\% & 20.2\\% & 5.8\\% & 1.6\\% & 0.32 & 480 \\\\\nGSM8K     & Math           & 42.0\\% & 22.0\\% & 8.0\\% & 6.0\\% & 0.30 & 420 \\\\\nARC       & Science        & 36.0\\% & 20.0\\% & 6.0\\% & 4.0\\% & 0.35 & 450 \\\\\nHellaSwag & Commonsense    & 33.0\\% & 18.0\\% & 7.0\\% & 5.0\\% & 0.36 & 440 \\\\\nMATH      & Hard reasoning & 38.0\\% & 24.0\\% & 9.0\\% & 7.0\\% & 0.28 & 520 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\nTable~\\ref{tab:bimodality} reveals a strong mechanistic predictor: item difficulty bimodality.\nThe correlation between bimodality index and item variance share is $r = 0.95$.\nBenchmarks with bimodal difficulty distributions (items that are either very easy or very hard for 8B models) produce higher item variance, regardless of whether they test knowledge or reasoning.\n\n\\begin{table}[t]\n\\centering\n\\caption{Difficulty distribution shape predicts item dominance ($r = 0.95$).}\n\\label{tab:bimodality}\n\\begin{tabular}{lccc}\n\\toprule\nBenchmark & Difficulty SD & Bimodality Index & item\\_id \\\\\n\\midrule\nGSM8K     & 0.34 & 0.72 & 42.0\\% \\\\\nMATH      & 0.33 & 0.70 & 38.0\\% \\\\\nMMLU      & 0.30 & 0.65 & 37.8\\% \\\\\nARC       & 0.27 & 0.52 & 36.0\\% \\\\\nHellaSwag & 0.22 & 0.38 & 33.0\\% \\\\\n\\midrule\n$r$ with item\\_id & $r$=0.92 & $r$=0.95 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n% 5. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Variance decomposition as measurement.}\nThe central message of this work is epistemological: a variance decomposition is a measurement, and like all measurements, it has its own error.\nThe field has treated variance component estimates as factual attributions---``item selection accounts for $X$\\% of variance''---without acknowledging that $X$ depends on which items were sampled (CV = 33\\%), which model specification was chosen (37.8\\% vs.\\ 15.2\\%), which estimation method was applied (Henderson vs.\\ REML: $\\Delta$ = 5.7pp), and which facets were included in the design (adding hardware drops item variance by 4.8pp).\nEvery single one of these analyst degrees of freedom shifts the decomposition qualitatively.\n\n\\paragraph{The model$\\times$item interaction.}\nAt 33\\% of total variance under the crossed design, model$\\times$item interaction is the single largest component and has been entirely overlooked.\nThis component represents differential item functioning across models: items that are easy for one architecture may be hard for another, due to differences in tokenization, attention mechanisms, and training data.\nTreating model as fixed---the universal practice in prior work---absorbs this interaction into item variance, producing the misleading impression that items have stable intrinsic difficulty.\nThis finding challenges a core assumption shared by both G-theory and IRT approaches to evaluation: that item difficulty is a property of items rather than of item--model pairs.\n\n\\paragraph{The non-gradient.}\nWe found no systematic cross-benchmark variance gradient.\nThe 9pp spread in item dominance across five benchmarks is non-monotonic and falls within the noise range established by resampling instability.\nItem dominance is predicted not by task taxonomy (knowledge vs.\\ reasoning) but by item difficulty distribution shape (bimodality index $r = 0.95$ with item variance).\nThis has practical implications: benchmark designers can predict whether their item pool will produce item-dominated variance by examining the difficulty distribution, without running a full G-study.\n\n\\paragraph{Budgets need error bars.}\nD-study projections converge across benchmarks (420--520 items for $G \\geq 0.90$, range = 60), eliminating the hoped-for contribution of benchmark-specific budgets.\nMore importantly, the bootstrap CIs ($\\pm$190 items) dwarf this range.\nA recommendation of ``use 480 items for reliable MMLU evaluation'' is more honestly stated as ``use somewhere between 380 and 560 items''---not actionable without further qualification.\nReproducibility budgets must themselves report uncertainty, a meta-methodological requirement that no prior work has identified.\n\n\\paragraph{Separability depends on scope.}\nSeparability of infrastructure and methodology factors holds approximately on MMLU under single-GPU binary scoring (1.5\\%), but fails on GSM8K (4.5\\%), fails when hardware is added to the design (5.5\\%), and fails when model is treated as a facet.\nThe apparent separability in prior isolated-factor studies may be an artifact of restricted experimental scope.\n\n\\paragraph{Limitations.}\nOur study uses open-weight models only; API models with opaque infrastructure may exhibit different variance structures.\nThe 14B extension ($n$=2 models) confounds scale with architecture.\nFine-tuning analysis uses encoder-only RoBERTa; decoder fine-tuning is substantially more expensive.\nItem resampling stability was tested on one model (Llama-3.1-8B) and one benchmark (MMLU); the CV may differ for other configurations.\n\n% ============================================================\n% 6. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe conducted a multi-benchmark G-theory analysis of LLM evaluation variance with the goal of producing reproducibility budgets.\nInstead, we discovered that the variance decomposition underlying such budgets is itself unreliable: item dominance estimates have a CV of 33\\% across item samples, the model$\\times$item interaction (33\\%) is systematically hidden by standard model-as-fixed analyses, and D-study budget projections carry $\\pm$190-item confidence intervals that render benchmark-specific recommendations statistically meaningless.\n\nThese findings do not invalidate G-theory as a framework for evaluation analysis.\nThey do establish that single-run variance decompositions---the current standard---are insufficient for reliable attribution.\nWe recommend that future variance decomposition studies (1) report resampling stability via bootstrap or jackknife CIs, (2) treat model as a crossed facet rather than fixed, and (3) accompany D-study budget recommendations with uncertainty intervals.\n\nVariance decomposition is a powerful lens for understanding evaluation variability.\nBut a lens with unmeasured distortion misleads more than it illuminates.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[Biderman et~al.(2024)]{biderman2024lessons}\nS.~Biderman, et~al.\n\\newblock Lessons from the trenches on reproducible evaluation of language models.\n\\newblock \\emph{arXiv preprint arXiv:2405.14782}, 2024.\n\n\\bibitem[Bouthillier et~al.(2021)]{bouthillier2021accounting}\nX.~Bouthillier, P.~Delaunay, M.~Bronzi, et~al.\n\\newblock Accounting for variance in machine learning benchmarks.\n\\newblock \\emph{Proceedings of Machine Learning and Systems}, 3, 2021.\n\n\\bibitem[Brennan(2001)]{brennan2001generalizability}\nR.~L. Brennan.\n\\newblock \\emph{Generalizability Theory}.\n\\newblock Springer, 2001.\n\n\\bibitem[Brittlebench(2026)]{brittlebench2026}\nBrittlebench Team.\n\\newblock Brittlebench: How fragile are LLM evaluations?\n\\newblock \\emph{arXiv preprint}, 2026.\n\n\\bibitem[Dehghani et~al.(2021)]{dehghani2021benchmark}\nM.~Dehghani, Y.~Tay, A.~A. Gritsenko, et~al.\n\\newblock The benchmark lottery.\n\\newblock \\emph{arXiv preprint arXiv:2107.07002}, 2021.\n\n\\bibitem[Dodge et~al.(2020)]{dodge2020fine}\nJ.~Dodge, G.~Ilharco, R.~Schwartz, et~al.\n\\newblock Fine-tuning pretrained language models: Weight initializations, data orders, and early stopping.\n\\newblock \\emph{arXiv preprint arXiv:2002.06305}, 2020.\n\n\\bibitem[Henderson et~al.(2018)]{henderson2018deep}\nP.~Henderson, R.~Islam, P.~Bachman, et~al.\n\\newblock Deep reinforcement learning that matters.\n\\newblock In \\emph{Proceedings of AAAI}, 2018.\n\n\\bibitem[Hua et~al.(2025)]{hua2025emnlp}\nH.~Hua, et~al.\n\\newblock Generation-based evaluation eliminates scoring artifacts in LLM benchmarks.\n\\newblock In \\emph{Proceedings of EMNLP}, 2025.\n\n\\bibitem[Lalor et~al.(2019)]{lalor2019learning}\nJ.~P. Lalor, H.~Wu, H.~Yu.\n\\newblock Learning latent parameters without human response patterns: Item response theory with artificial crowds.\n\\newblock In \\emph{Proceedings of NAACL-HLT}, 2019.\n\n\\bibitem[Lu et~al.(2022)]{lu2022fantastically}\nY.~Lu, M.~Bartolo, A.~Moore, et~al.\n\\newblock Fantastically ordered prompts and where to find them: Overcoming few-shot prompt order sensitivity.\n\\newblock In \\emph{Proceedings of ACL}, 2022.\n\n\\bibitem[Mesting(2026)]{mesting2026generalizability}\nB.~Mesting.\n\\newblock A generalizability theory analysis of LLM-as-judge evaluation.\n\\newblock \\emph{arXiv preprint}, 2026.\n\n\\bibitem[Messina \\& Scotta(2026)]{messina2026floating}\nP.~Messina and M.~Scotta.\n\\newblock Floating-point non-associativity in neural network inference.\n\\newblock \\emph{arXiv preprint}, 2026.\n\n\\bibitem[Perlitz et~al.(2023)]{perlitz2023efficient}\nY.~Perlitz, E.~Bandel, et~al.\n\\newblock Efficient benchmarking of language models.\n\\newblock \\emph{arXiv preprint arXiv:2308.11696}, 2023.\n\n\\bibitem[Pezeshkpour \\& Hruschka(2024)]{pezeshkpour2024large}\nP.~Pezeshkpour and E.~Hruschka.\n\\newblock Large language models sensitivity to the order of options in multiple-choice questions.\n\\newblock \\emph{arXiv preprint arXiv:2308.11483}, 2024.\n\n\\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}\nF.~M. Polo, L.~Weber, L.~Choshen, et~al.\n\\newblock tinybenchmarks: Evaluating LLMs with fewer examples.\n\\newblock \\emph{arXiv preprint arXiv:2402.14992}, 2024.\n\n\\bibitem[Rodriguez et~al.(2021)]{rodriguez2021evaluation}\nP.~Rodriguez, J.~Barrow, A.~M. Hoyle, et~al.\n\\newblock Evaluation examples are not equally informative: How should that change NLP leaderboards?\n\\newblock In \\emph{Proceedings of ACL}, 2021.\n\n\\bibitem[Sellam et~al.(2022)]{sellam2022multiBERTs}\nT.~Sellam, S.~Yadlowsky, I.~Tenney, et~al.\n\\newblock The MultiBERTs: BERT reproductions for robustness analysis.\n\\newblock In \\emph{Proceedings of ICLR}, 2022.\n\n\\bibitem[Shavelson \\& Webb(1991)]{shavelson1991generalizability}\nR.~J. Shavelson and N.~M. Webb.\n\\newblock \\emph{Generalizability Theory: A Primer}.\n\\newblock SAGE Publications, 1991.\n\n\\bibitem[Vania et~al.(2021)]{vania2021comparing}\nC.~Vania, et~al.\n\\newblock Comparing test sets with item response theory.\n\\newblock In \\emph{Proceedings of ACL}, 2021.\n\n\\bibitem[Yuan et~al.(2025)]{yuan2025llm}\nZ.~Yuan, et~al.\n\\newblock Do LLM evaluations converge across hardware? Up to 9\\% accuracy variation from GPU and precision choices.\n\\newblock \\emph{arXiv preprint}, 2025.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "308d83ce-fc19-45ae-8321-ef9c29b68a7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T222113 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheor…",
  "leafUuid": "36531159-512c-4461-b810-bdc9a9bdf43c",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier dream paper for NLP variance study",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640"
}
```

---

### Assistant

_source line 23 · 2026-05-20T23:30:23.628Z_

Compiling the LaTeX.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36531159-512c-4461-b810-bdc9a9bdf43c",
  "isSidechain": false,
  "requestId": "req_011CbEh3CGRM4VGeu1Rx1fjd",
  "type": "assistant",
  "uuid": "83a4b3ae-3f93-4cbb-b1dd-7e4c9babf480",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Mucbp7yoCZK4LVZhe2SQx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14742,
      "cache_read_input_tokens": 44261,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14742,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 44261,
          "cache_creation_input_tokens": 14742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14742
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

_source line 24 · 2026-05-20T23:30:28.449Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EfTZ4cm4iR7QNM9aijGv9W`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83a4b3ae-3f93-4cbb-b1dd-7e4c9babf480",
  "isSidechain": false,
  "requestId": "req_011CbEh3CGRM4VGeu1Rx1fjd",
  "type": "assistant",
  "uuid": "54bde776-ec4d-43f7-8938-bee8eeb4091d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Mucbp7yoCZK4LVZhe2SQx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14742,
      "cache_read_input_tokens": 44261,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14742,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 44261,
          "cache_creation_input_tokens": 14742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14742
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

_source line 25 · 2026-05-20T23:30:30.400Z_

<details><summary>↩ Tool result · `toolu_01EfTZ4cm4iR7QNM9aijGv9W`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/adjustbox.sty
(/usr/share/texlive/texmf-dist/tex/latex/xkeyval/xkeyval.sty
(/usr/share/texlive/texmf-dist/tex/generic/xkeyval/xkeyval.tex
(/usr/share/texlive/texmf-dist/tex/generic/xkeyval/xkvutils.tex)))
(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/adjcalc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/trimclip.sty
(/usr/share/texlive/texmf-dist/tex/latex/collectbox/collectbox.sty)
(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/tc-pdftex.def))
(/usr/share/texlive/texmf-dist/tex/latex/ifoddpage/ifoddpage.sty)
(/usr/share/texlive/texmf-dist/tex/latex/varwidth/varwidth.sty)
==> First Aid for varwidth.sty applied!
) (/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `bouthillier2021accounting' on page 1 undefine
d on input line 43.


Package natbib Warning: Citation `mesting2026generalizability' on page 1 undefi
ned on input line 43.


Package natbib Warning: Citation `brittlebench2026' on page 1 undefined on inpu
t line 43.


Package natbib Warning: Citation `mesting2026generalizability' on page 1 undefi
ned on input line 44.


Package natbib Warning: Citation `brittlebench2026' on page 1 undefined on inpu
t line 44.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

Package natbib Warning: Citation `bouthillier2021accounting' on page 2 undefine
d on input line 75.


Package natbib Warning: Citation `henderson2018deep' on page 2 undefined on inp
ut line 76.


Package natbib Warning: Citation `dodge2020fine' on page 2 undefined on input l
ine 77.


Package natbib Warning: Citation `sellam2022multiBERTs' on page 2 undefined on 
input line 77.


Package natbib Warning: Citation `mesting2026generalizability' on page 2 undefi
ned on input line 81.


Package natbib Warning: Citation `brittlebench2026' on page 2 undefined on inpu
t line 83.


Package natbib Warning: Citation `lalor2019learning' on page 2 undefined on inp
ut line 87.


Package natbib Warning: Citation `rodriguez2021evaluation' on page 2 undefined 
on input line 87.


Package natbib Warning: Citation `vania2021comparing' on page 2 undefined on in
put line 87.


Package natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o
n input line 87.


Package natbib Warning: Citation `perlitz2023efficient' on page 2 undefined on 
input line 87.


Package natbib Warning: Citation `dehghani2021benchmark' on page 2 undefined on
 input line 87.


Package natbib Warning: Citation `yuan2025llm' on page 2 undefined on input lin
e 91.


Package natbib Warning: Citation `lu2022fantastically' on page 2 undefined on i
nput line 92.


Package natbib Warning: Citation `pezeshkpour2024large' on page 2 undefined on 
input line 92.


Package natbib Warning: Citation `biderman2024lessons' on page 2 undefined on i
nput line 93.


Package natbib Warning: Citation `shavelson1991generalizability' on page 2 unde
fined on input line 103.


Package natbib Warning: Citation `brennan2001generalizability' on page 2 undefi
ned on input line 103.

[2]

Package natbib Warning: Citation `hua2025emnlp' on page 3 undefined on input li
ne 118.

[3]

LaTeX Warning: Reference `tab:exp1_variance' on page 4 undefined on input line 
156.


LaTeX Warning: Reference `sec:exp1b' on page 4 undefined on input line 161.


LaTeX Warning: Reference `sec:exp4' on page 4 undefined on input line 161.


LaTeX Warning: Reference `sec:exp1b' on page 4 undefined on input line 161.


LaTeX Warning: Reference `sec:exp4' on page 4 undefined on input line 161.


LaTeX Warning: Reference `tab:resample' on page 4 undefined on input line 195.


LaTeX Warning: Reference `tab:resample_stability' on page 4 undefined on input 
line 219.

[4]

Package natbib Warning: Citation `mesting2026generalizability' on page 5 undefi
ned on input line 244.


Package natbib Warning: Citation `brittlebench2026' on page 5 undefined on inpu
t line 244.


Package natbib Warning: Citation `bouthillier2021accounting' on page 5 undefine
d on input line 244.


Package natbib Warning: Citation `mesting2026generalizability' on page 5 undefi
ned on input line 245.


LaTeX Warning: Reference `tab:multi_bench' on page 5 undefined on input line 25
1.


LaTeX Warning: Reference `tab:gradient_test' on page 5 undefined on input line 
253.

[5]

LaTeX Warning: Reference `tab:separability' on page 6 undefined on input line 2
95.


LaTeX Warning: Reference `tab:hardware' on page 6 undefined on input line 318.


Overfull \hbox (1.85022pt too wide) in paragraph at lines 318--321
\T1/cmr/m/n/10.95 hardware-related vari-ance is 14.0%, ex-ceed-ing precision-re
lated vari-ance ($\OMS/cmsy/m/n/10.95 ^^X$\T1/cmr/m/n/10.95 6%). The hardware$\
OMS/cmsy/m/n/10.95 ^^B$\T1/cmr/m/n/10.95 item

LaTeX Warning: Reference `tab:sep_hardware' on page 6 undefined on input line 3
45.


LaTeX Warning: Reference `tab:model_crossed' on page 6 undefined on input line 
367.

[6]

LaTeX Warning: Reference `tab:bootstrap_rank' on page 7 undefined on input line
 391.


LaTeX Warning: Reference `tab:dstudy' on page 7 undefined on input line 411.


LaTeX Warning: Reference `tab:reml' on page 7 undefined on input line 434.


LaTeX Warning: Reference `tab:14b' on page 7 undefined on input line 454.

[7]

LaTeX Warning: Reference `tab:finetune' on page 8 undefined on input line 478.


LaTeX Warning: Reference `tab:inf_ft_corr' on page 8 undefined on input line 50
8.


LaTeX Warning: Reference `tab:5bench' on page 8 undefined on input line 555.


LaTeX Warning: Reference `tab:bimodality' on page 8 undefined on input line 578
.

[8] [9] [10] [11] [12]

Package natbib Warning: There were undefined citations.

[13] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ectt1095
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input ectt1095
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ectt1095.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ectt.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf
 Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf
 Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]
[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]
[216] [217] [218] [219] [220] [221] [222] [223])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf
 Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]
[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]
[248] [249] [250] [251] [252] [253] [254] [255])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf
 Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]
[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]
[152] [153] [154] [155] [156] [157])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf
 Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]
[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]
[183] [184] [185] [186] [187] [188])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf
 Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]
[95] [127] [32])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf
 Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]
[59] [61] [96] [189] [17] [45] [16] [21] [22])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf
 Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf
 Ok [24] [34] [35] [36] [37] [64] [191] [159])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf
 Ok [25] [26] [28] [27] [29] [30] [31])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf
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
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exmligtb.mf
 Ok) ) ) )
Font metrics written on ectt1095.tfm.
Output written on ectt1095.600gf (256 characters, 47796 bytes).
Transcript written on ectt1095.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk: successfully generated.


LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk>
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecbx1000
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input ecbx1000
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx1000.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf
 Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf
 Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]
[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]
[216] [217] [218] [219] [220] [221] [222] [223])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf
 Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]
[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]
[248] [249] [250] [251] [252] [253] [254] [255])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf
 Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]
[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]
[152] [153] [154] [155] [156] [157])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf
 Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]
[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]
[183] [184] [185] [186] [187] [188])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf
 Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]
[95] [127] [32])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf
 Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]
[59] [61] [96] [189] [17] [45] [16] [21] [22])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf
 Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf
 Ok [24] [34] [35] [36] [37] [64] [191] [159])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf
 Ok [25] [26] [28] [27] [29] [30] [31])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf
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
Font metrics written on ecbx1000.tfm.
Output written on ecbx1000.600gf (256 characters, 49864 bytes).
Transcript written on ecbx1000.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk: successfully generated.
 &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmsy10.pfb>
Output written on paper.pdf (13 pages, 205940 bytes).
Transcript written on paper.log.
 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmsy10.pfb>
Output written on paper.pdf (13 pages, 210161 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54bde776-ec4d-43f7-8938-bee8eeb4091d",
  "isSidechain": false,
  "promptId": "373fec7c-0384-4178-9c36-2cd6143072a3",
  "type": "user",
  "uuid": "a90bbf48-b81b-4246-80df-ad8b21309f61",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/adjustbox.sty\n(/usr/share/texlive/texmf-dist/tex/latex/xkeyval/xkeyval.sty\n(/usr/share/texlive/texmf-dist/tex/generic/xkeyval/xkeyval.tex\n(/usr/share/texlive/texmf-dist/tex/generic/xkeyval/xkvutils.tex)))\n(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/adjcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/trimclip.sty\n(/usr/share/texlive/texmf-dist/tex/latex/collectbox/collectbox.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/tc-pdftex.def))\n(/usr/share/texlive/texmf-dist/tex/latex/ifoddpage/ifoddpage.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/varwidth/varwidth.sty)\n==> First Aid for varwidth.sty applied!\n) (/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `bouthillier2021accounting' on page 1 undefine\nd on input line 43.\n\n\nPackage natbib Warning: Citation `mesting2026generalizability' on page 1 undefi\nned on input line 43.\n\n\nPackage natbib Warning: Citation `brittlebench2026' on page 1 undefined on inpu\nt line 43.\n\n\nPackage natbib Warning: Citation `mesting2026generalizability' on page 1 undefi\nned on input line 44.\n\n\nPackage natbib Warning: Citation `brittlebench2026' on page 1 undefined on inpu\nt line 44.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nPackage natbib Warning: Citation `bouthillier2021accounting' on page 2 undefine\nd on input line 75.\n\n\nPackage natbib Warning: Citation `henderson2018deep' on page 2 undefined on inp\nut line 76.\n\n\nPackage natbib Warning: Citation `dodge2020fine' on page 2 undefined on input l\nine 77.\n\n\nPackage natbib Warning: Citation `sellam2022multiBERTs' on page 2 undefined on \ninput line 77.\n\n\nPackage natbib Warning: Citation `mesting2026generalizability' on page 2 undefi\nned on input line 81.\n\n\nPackage natbib Warning: Citation `brittlebench2026' on page 2 undefined on inpu\nt line 83.\n\n\nPackage natbib Warning: Citation `lalor2019learning' on page 2 undefined on inp\nut line 87.\n\n\nPackage natbib Warning: Citation `rodriguez2021evaluation' on page 2 undefined \non input line 87.\n\n\nPackage natbib Warning: Citation `vania2021comparing' on page 2 undefined on in\nput line 87.\n\n\nPackage natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o\nn input line 87.\n\n\nPackage natbib Warning: Citation `perlitz2023efficient' on page 2 undefined on \ninput line 87.\n\n\nPackage natbib Warning: Citation `dehghani2021benchmark' on page 2 undefined on\n input line 87.\n\n\nPackage natbib Warning: Citation `yuan2025llm' on page 2 undefined on input lin\ne 91.\n\n\nPackage natbib Warning: Citation `lu2022fantastically' on page 2 undefined on i\nnput line 92.\n\n\nPackage natbib Warning: Citation `pezeshkpour2024large' on page 2 undefined on \ninput line 92.\n\n\nPackage natbib Warning: Citation `biderman2024lessons' on page 2 undefined on i\nnput line 93.\n\n\nPackage natbib Warning: Citation `shavelson1991generalizability' on page 2 unde\nfined on input line 103.\n\n\nPackage natbib Warning: Citation `brennan2001generalizability' on page 2 undefi\nned on input line 103.\n\n[2]\n\nPackage natbib Warning: Citation `hua2025emnlp' on page 3 undefined on input li\nne 118.\n\n[3]\n\nLaTeX Warning: Reference `tab:exp1_variance' on page 4 undefined on input line \n156.\n\n\nLaTeX Warning: Reference `sec:exp1b' on page 4 undefined on input line 161.\n\n\nLaTeX Warning: Reference `sec:exp4' on page 4 undefined on input line 161.\n\n\nLaTeX Warning: Reference `sec:exp1b' on page 4 undefined on input line 161.\n\n\nLaTeX Warning: Reference `sec:exp4' on page 4 undefined on input line 161.\n\n\nLaTeX Warning: Reference `tab:resample' on page 4 undefined on input line 195.\n\n\nLaTeX Warning: Reference `tab:resample_stability' on page 4 undefined on input \nline 219.\n\n[4]\n\nPackage natbib Warning: Citation `mesting2026generalizability' on page 5 undefi\nned on input line 244.\n\n\nPackage natbib Warning: Citation `brittlebench2026' on page 5 undefined on inpu\nt line 244.\n\n\nPackage natbib Warning: Citation `bouthillier2021accounting' on page 5 undefine\nd on input line 244.\n\n\nPackage natbib Warning: Citation `mesting2026generalizability' on page 5 undefi\nned on input line 245.\n\n\nLaTeX Warning: Reference `tab:multi_bench' on page 5 undefined on input line 25\n1.\n\n\nLaTeX Warning: Reference `tab:gradient_test' on page 5 undefined on input line \n253.\n\n[5]\n\nLaTeX Warning: Reference `tab:separability' on page 6 undefined on input line 2\n95.\n\n\nLaTeX Warning: Reference `tab:hardware' on page 6 undefined on input line 318.\n\n\nOverfull \\hbox (1.85022pt too wide) in paragraph at lines 318--321\n\\T1/cmr/m/n/10.95 hardware-related vari-ance is 14.0%, ex-ceed-ing precision-re\nlated vari-ance ($\\OMS/cmsy/m/n/10.95 ^^X$\\T1/cmr/m/n/10.95 6%). The hardware$\\\nOMS/cmsy/m/n/10.95 ^^B$\\T1/cmr/m/n/10.95 item\n\nLaTeX Warning: Reference `tab:sep_hardware' on page 6 undefined on input line 3\n45.\n\n\nLaTeX Warning: Reference `tab:model_crossed' on page 6 undefined on input line \n367.\n\n[6]\n\nLaTeX Warning: Reference `tab:bootstrap_rank' on page 7 undefined on input line\n 391.\n\n\nLaTeX Warning: Reference `tab:dstudy' on page 7 undefined on input line 411.\n\n\nLaTeX Warning: Reference `tab:reml' on page 7 undefined on input line 434.\n\n\nLaTeX Warning: Reference `tab:14b' on page 7 undefined on input line 454.\n\n[7]\n\nLaTeX Warning: Reference `tab:finetune' on page 8 undefined on input line 478.\n\n\nLaTeX Warning: Reference `tab:inf_ft_corr' on page 8 undefined on input line 50\n8.\n\n\nLaTeX Warning: Reference `tab:5bench' on page 8 undefined on input line 555.\n\n\nLaTeX Warning: Reference `tab:bimodality' on page 8 undefined on input line 578\n.\n\n[8] [9] [10] [11] [12]\n\nPackage natbib Warning: There were undefined citations.\n\n[13] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ectt1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ectt1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ectt1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ectt.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exmligtb.mf\n Ok) ) ) )\nFont metrics written on ectt1095.tfm.\nOutput written on ectt1095.600gf (256 characters, 47796 bytes).\nTranscript written on ectt1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk: successfully generated.\n\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecbx1000\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecbx1000\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx1000.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\nFont metrics written on ecbx1000.tfm.\nOutput written on ecbx1000.600gf (256 characters, 49864 bytes).\nTranscript written on ecbx1000.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk: successfully generated.\n &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmsy10.pfb>\nOutput written on paper.pdf (13 pages, 205940 bytes).\nTranscript written on paper.log.\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmsy10.pfb>\nOutput written on paper.pdf (13 pages, 210161 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "54bde776-ec4d-43f7-8938-bee8eeb4091d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T222113 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheor…",
  "leafUuid": "a90bbf48-b81b-4246-80df-ad8b21309f61",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier dream paper for NLP variance study",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640"
}
```

---

### Assistant

_source line 28 · 2026-05-20T23:30:35.712Z_

PDF compiled successfully (13 pages). Let me verify the output.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a90bbf48-b81b-4246-80df-ad8b21309f61",
  "isSidechain": false,
  "requestId": "req_011CbEh3uQBQ6pj9SFkaZdUM",
  "type": "assistant",
  "uuid": "1064920b-e484-431f-8b80-ab5d7b6facfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXMNaggqHobqV412K7EyRN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8937,
      "cache_read_input_tokens": 59003,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8937,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 59003,
          "cache_creation_input_tokens": 8937,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8937
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

_source line 29 · 2026-05-20T23:30:37.886Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UNN8eWewR2LShnfPLAgsvo`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/paper.pdf",
  "description": "Verify PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1064920b-e484-431f-8b80-ab5d7b6facfc",
  "isSidechain": false,
  "requestId": "req_011CbEh3uQBQ6pj9SFkaZdUM",
  "type": "assistant",
  "uuid": "970c8e64-ea79-4a2d-9c60-a659597dc063",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXMNaggqHobqV412K7EyRN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8937,
      "cache_read_input_tokens": 59003,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8937,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 59003,
          "cache_creation_input_tokens": 8937,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8937
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

_source line 30 · 2026-05-20T23:30:37.923Z_

<details><summary>↩ Tool result · `toolu_01UNN8eWewR2LShnfPLAgsvo`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 210161 May 20 23:30 /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "970c8e64-ea79-4a2d-9c60-a659597dc063",
  "isSidechain": false,
  "promptId": "373fec7c-0384-4178-9c36-2cd6143072a3",
  "type": "user",
  "uuid": "f2371a7b-bfef-4c80-8fbe-40900098351d",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 210161 May 20 23:30 /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/paper.pdf",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "970c8e64-ea79-4a2d-9c60-a659597dc063",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-20T23:30:37.940Z_

```json
{
  "parentUuid": "f2371a7b-bfef-4c80-8fbe-40900098351d",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "d1aa6c32-c35e-4aa5-b39f-e5460d6aaecc",
  "timestamp": "2026-05-20T23:30:37.940Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-20T23:30:46.688Z_

论文已生成并编译成功。

- **文件**: `worst/paper.tex` (LaTeX 源码) + `worst/paper.pdf` (13 页)
- **标题**: *Variance Decomposition Is a Measurement, Not a Fact: On the Instability of Reproducibility Budgets for LLM Evaluation*
- **覆盖全部 8 个实验**，每个实验对应独立的 subsection 和 table（共 19 个表格）
- **三个核心 claim** 按 narrative guidance 重构：item resampling instability (CV=33%) 为 centerpiece，model×item interaction (33%) 为最大被忽视项，D-study budget CI (±190 items) 要求 budget 本身需要 error bars
- 所有数字直接取自 `experiment_data.json`，无编造

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1aa6c32-c35e-4aa5-b39f-e5460d6aaecc",
  "isSidechain": false,
  "requestId": "req_011CbEh4TcBYijV91SqgpPEf",
  "type": "assistant",
  "uuid": "6a69c224-d147-471a-ad80-8aad311f90d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HbauL9gZfqejDrUV58TDtD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 327,
      "cache_read_input_tokens": 67940,
      "output_tokens": 230,
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
          "output_tokens": 230,
          "cache_read_input_tokens": 67940,
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

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T222113 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheor…",
  "leafUuid": "6a69c224-d147-471a-ad80-8aad311f90d7",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier dream paper for NLP variance study",
  "sessionId": "504e3b83-20e3-4523-8138-37f4c7478640"
}
```

---
