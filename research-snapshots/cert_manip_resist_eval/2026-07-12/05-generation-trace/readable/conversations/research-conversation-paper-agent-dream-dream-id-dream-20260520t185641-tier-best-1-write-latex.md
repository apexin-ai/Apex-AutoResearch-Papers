# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T185641 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/30326c6e-1574-480d-ae02-912541994f75.jsonl`
- **Structured JSON:** [`22966877e6b0e3b310f8.json`](../../sessions/22/22966877e6b0e3b310f8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T19:23:21.412Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T19:23:21.412Z",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T185641 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Original framing stands: \"CaCLR shifts the cross-lingual calibration Pareto frontier.\" All 4 claims form an unbroken causal chain — discovery → analysis → method → mechanism. Headline: CaCLR reduces non-EN ECE by 30-50% over temp scaling with zero target-language labels. Pareto frontier is the organizing principle, CaCLR is the actionable contribution, decomposition explains why it works, orthogonality explains why output-based methods can't.\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T19:23:21.415Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T19:23:21.415Z",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75"
}
```

---

## Round 1

36 recorded events

### User

_source line 3 · 2026-05-20T19:23:21.451Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T185641 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Original framing stands: "CaCLR shifts the cross-lingual calibration Pareto frontier." All 4 claims form an unbroken causal chain — discovery → analysis → method → mechanism. Headline: CaCLR reduces non-EN ECE by 30-50% over temp scaling with zero target-language labels. Pareto frontier is the organizing principle, CaCLR is the actionable contribution, decomposition explains why it works, orthogonality explains why output-based methods can't.

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "907ecca9-b4a5-4dd2-af0b-6dcee3e5aad0",
  "type": "user",
  "uuid": "a1978b7d-800a-4aed-8caf-147602a17daf",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T19:23:21.450Z_

```json
{
  "parentUuid": "a1978b7d-800a-4aed-8caf-147602a17daf",
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
  "uuid": "c67020c2-ccd6-4292-9bb1-19cd7adc673b",
  "timestamp": "2026-05-20T19:23:21.450Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T19:23:21.450Z_

```json
{
  "parentUuid": "c67020c2-ccd6-4292-9bb1-19cd7adc673b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ea370554-8151-4e61-8bd7-b31382c7ead7",
  "timestamp": "2026-05-20T19:23:21.450Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
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
  "aiTitle": "Generate complete research paper for dream session",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75"
}
```

---

### Assistant

_source line 7 · 2026-05-20T19:23:23.791Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea370554-8151-4e61-8bd7-b31382c7ead7",
  "isSidechain": false,
  "requestId": "req_011CbENCoLLtHzQp3tNu1igi",
  "type": "assistant",
  "uuid": "b4ed5bcb-d41d-4fb4-94a5-91973e093784",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014FXxE7P9kh3hpEhHdrmmq1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11424,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11424
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

_source line 8 · 2026-05-20T19:23:24.783Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JWYQeETSsNjA2gMjBaktsV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4ed5bcb-d41d-4fb4-94a5-91973e093784",
  "isSidechain": false,
  "requestId": "req_011CbENCoLLtHzQp3tNu1igi",
  "type": "assistant",
  "uuid": "bbc758a5-91f3-4b5d-b4b1-dd90569ab86a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014FXxE7P9kh3hpEhHdrmmq1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11424,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11424
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

_source line 9 · 2026-05-20T19:23:25.082Z_

<details><summary>↩ Tool result · `toolu_01JWYQeETSsNjA2gMjBaktsV`</summary>

```text
1	[
2	  {
3	    "name": "Full Pareto Frontier — Qwen3-235B-A22B",
4	    "description": "Extract activations at every 4th layer (24 probed layers out of 94), 20 languages, train English correctness probes (logistic regression + 2-layer MLP), evaluate 5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR).\n",
5	    "results": {
6	      "en_auroc_best_layer": 0.843,
7	      "en_best_layer_idx": 72,
8	      "en_auroc_range": [
9	        0.621,
10	        0.843
11	      ],
12	      "en_ece_raw_best": 0.162,
13	      "en_ece_tempcal_best": 0.054,
14	      "temp_scaling_T": 4.87,
15	      "zs_transfer_auroc_mean_19lang_best_transfer_layer": 0.762,
16	      "zs_best_transfer_layer_idx": 56,
17	      "zs_transfer_drop_from_en_mean_pp": 8.1,
18	      "zs_auroc_by_tier": {
19	        "high_resource_mean": 0.791,
20	        "mid_resource_mean": 0.754,
21	        "low_resource_mean": 0.683
22	      },
23	      "zs_auroc_by_lang": {
24	        "en": 0.843,
25	        "zh": 0.802,
26	        "de": 0.796,
27	        "fr": 0.793,
28	        "es": 0.789,
29	        "ja": 0.785,
30	        "ru": 0.782,
31	        "pt": 0.788,
32	        "it": 0.786,
33	        "ar": 0.768,
34	        "hi": 0.761,
35	        "ko": 0.755,
36	        "vi": 0.749,
37	        "th": 0.743,
38	        "bn": 0.738,
39	        "tr": 0.756,
40	        "nl": 0.79,
41	        "sw": 0.695,
42	        "yo": 0.672,
43	        "ig": 0.681
44	      },
45	      "mean_shift_improvement_count": 2,
46	      "mean_shift_delta_ece_mean": 1.41,
47	      "linproj_auroc_mean_19lang": 0.724,
48	      "fewshot_25_auroc_mean_19lang": 0.748,
49	      "fewshot_100_auroc_mean_19lang": 0.771,
50	      "pareto_depth_transfer_rank_corr": 0.88,
51	      "pareto_frontier_layers": [
52	        40,
53	        44,
54	        48,
55	        52,
56	        56,
57	        60
58	      ],
59	      "layers_above_0p5_auroc_count": 22
60	    },
61	    "tables": [
62	      {
63	        "name": "Table 1: Qwen3-235B Pareto Frontier — EN AUROC vs ZS Transfer AUROC by Layer",
64	        "columns": [
65	          "layer_idx",
66	          "layer_depth_pct",
67	          "en_auroc",
68	          "zs_mean_auroc_19",
69	          "zs_drop_pp",
70	          "on_pareto"
71	        ],
72	        "rows": [
73	          [
74	            4,
75	            4,
76	            0.621,
77	            0.608,
78	            1.3,
79	            false
80	          ],
81	          [
82	            8,
83	            9,
84	            0.648,
85	            0.637,
86	            1.1,
87	            false
88	          ],
89	          [
90	            12,
91	            13,
92	            0.689,
93	            0.671,
94	            1.8,
95	            false
96	          ],
97	          [
98	            16,
99	            17,
100	            0.712,
101	            0.698,
102	            1.4,
103	            false
104	          ],
105	          [
106	            20,
107	            21,
108	            0.738,
109	            0.724,
110	            1.4,
111	            false
112	          ],
113	          [
114	            24,
115	            26,
116	            0.756,
117	            0.742,
118	            1.4,
119	            false
120	          ],
121	          [
122	            28,
123	            30,
124	            0.771,
125	            0.755,
126	            1.6,
127	            false
128	          ],
129	          [
130	            32,
131	            34,
132	            0.784,
133	            0.764,
134	            2.0,
135	            false
136	          ],
137	          [
138	            36,
139	            38,
140	            0.795,
141	            0.771,
142	            2.4,
143	            false
144	          ],
145	          [
146	            40,
147	            43,
148	            0.803,
149	            0.776,
150	            2.7,
151	            true
152	          ],
153	          [
154	            44,
155	            47,
156	            0.81,
157	            0.774,
158	            3.6,
159	            true
160	          ],
161	          [
162	            48,
163	            51,
164	            0.816,
165	            0.77,
166	            4.6,
167	            true
168	          ],
169	          [
170	            52,
171	            55,
172	            0.822,
173	            0.765,
174	            5.7,
175	            true
176	          ],
177	          [
178	            56,
179	            60,
180	            0.827,
181	            0.762,
182	            6.5,
183	            true
184	          ],
185	          [
186	            60,
187	            64,
188	            0.831,
189	            0.753,
190	            7.8,
191	            true
192	          ],
193	          [
194	            64,
195	            68,
196	            0.835,
197	            0.741,
198	            9.4,
199	            false
200	          ],
201	          [
202	            68,
203	            72,
204	            0.839,
205	            0.728,
206	            11.1,
207	            false
208	          ],
209	          [
210	            72,
211	            77,
212	            0.843,
213	            0.712,
214	            13.1,
215	            false
216	          ],
217	          [
218	            76,
219	            81,
220	            0.841,
221	            0.694,
222	            14.7,
223	            false
224	          ],
225	          [
226	            80,
227	            85,
228	            0.838,
229	            0.671,
230	            16.7,
231	            false
232	          ],
233	          [
234	            84,
235	            89,
236	            0.832,
237	            0.643,
238	            18.9,
239	            false
240	          ],
241	          [
242	            88,
243	            94,
244	            0.819,
245	            0.611,
246	            20.8,
247	            false
248	          ],
249	          [
250	            92,
251	            98,
252	            0.791,
253	            0.574,
254	            21.7,
255	            false
256	          ],
257	          [
258	            94,
259	            100,
260	            0.762,
261	            0.541,
262	            22.1,
263	            false
264	          ]
265	        ]
266	      },
267	      {
268	        "name": "Table 2: Transfer Condition Comparison (at best-transfer layer L56)",
269	        "columns": [
270	          "condition",
271	          "auroc_mean_19",
272	          "ece_mean_19",
273	          "ece_reduction_vs_tempcal_pct"
274	        ],
275	        "rows": [
276	          [
277	            "zero-shot",
278	            0.762,
279	            0.098,
280	            0
281	          ],
282	          [
283	            "mean-shift",
284	            0.758,
285	            0.101,
286	            -3.1
287	          ],
288	          [
289	            "linear_projection",
290	            0.781,
291	            0.082,
292	            16.3
293	          ],
294	          [
295	            "few-shot-25",
296	            0.748,
297	            0.089,
298	            9.2
299	          ],
300	          [
301	            "few-shot-100",
302	            0.771,
303	            0.079,
304	            19.4
305	          ],
306	          [
307	            "CaCLR",
308	            0.814,
309	            0.058,
310	            40.8
311	          ]
312	        ]
313	      }
314	    ],
315	    "figures": [],
316	    "analysis": "The Pareto frontier is crisp and monotonic: 6 layers form the efficient frontier between L40-L60. The rank correlation (Spearman) between layer depth and transfer degradation is ρ=0.88 (p<0.001). The frontier's shape confirms that the depth- transferability tradeoff is not an artifact of small models — it amplifies at scale. The 16pp gap between best-EN layer (L72) and best-transfer layer (L56) is larger than MVP's ~3-layer gap, consistent with deeper models having more room for language-specific specialization. All high-resource languages pass AUROC > 0.75 at the best-transfer layer; all low-resource languages exceed 0.65.\n\n\nQwen3-235B-A22B is a 94-layer MoE with massive representation capacity. The jump from MVP's 7B (en AUROC 0.754) to 235B is expected to yield ~9pp AUROC gain, consistent with prior probing literature showing log-linear scaling of linear probe accuracy with model parameters (Burns et al., Marks et al.). The MoE architecture concentrates expert representations, producing cleaner correctness signals in intermediate layers. The Pareto frontier emerges because deeper layers (L72+) specialize for English-dominant pretraining data distribution — the model's language-specific processing intensifies past ~75% depth, degrading cross-lingual invariance. The best transfer layer (L56, ~60% depth) sits in the \"universal reasoning\" zone before language-specific heads activate. Low-resource languages (sw, yo, ig) still transfer above 0.65 AUROC because GlobalMMLU questions share structural patterns that even underrepresented languages partially align with in middle layers. Mean-shift continues to mostly fail because correctness directions are not simply mean-offset between languages — they require rotation, not translation, which linear projection and CaCLR address.\n"
317	  },
318	  {
319	    "name": "Full Pareto Frontier — Llama 4 Scout",
320	    "description": "Extract activations at every 4th layer (12 probed layers out of 48), 20 languages, 5 transfer conditions. INT8 weight quantization.\n",
321	    "results": {
322	      "en_auroc_best_layer": 0.821,
323	      "en_best_layer_idx": 36,
324	      "en_auroc_range": [
325	        0.634,
326	        0.821
327	      ],
328	      "en_ece_raw_best": 0.174,
329	      "en_ece_tempcal_best": 0.061,
330	      "temp_scaling_T": 5.34,
331	      "zs_transfer_auroc_mean_19lang_best_transfer_layer": 0.741,
332	      "zs_best_transfer_layer_idx": 28,
333	      "zs_transfer_drop_from_en_mean_pp": 8.0,
334	      "zs_auroc_by_tier": {
335	        "high_resource_mean": 0.771,
336	        "mid_resource_mean": 0.733,
337	        "low_resource_mean": 0.661
338	      },
339	      "zs_auroc_by_lang": {
340	        "en": 0.821,
341	        "zh": 0.784,
342	        "de": 0.778,
343	        "fr": 0.775,
344	        "es": 0.771,
345	        "ja": 0.766,
346	        "ru": 0.762,
347	        "pt": 0.77,
348	        "it": 0.768,
349	        "ar": 0.748,
350	        "hi": 0.741,
351	        "ko": 0.735,
352	        "vi": 0.729,
353	        "th": 0.722,
354	        "bn": 0.718,
355	        "tr": 0.737,
356	        "nl": 0.772,
357	        "sw": 0.674,
358	        "yo": 0.641,
359	        "ig": 0.667
360	      },
361	      "mean_shift_improvement_count": 1,
362	      "linproj_auroc_mean_19lang": 0.706,
363	      "fewshot_25_auroc_mean_19lang": 0.728,
364	      "fewshot_100_auroc_mean_19lang": 0.752,
365	      "pareto_depth_transfer_rank_corr": 0.82,
366	      "pareto_frontier_layers": [
367	        20,
368	        24,
369	        28,
370	        32
371	      ]
372	    },
373	    "tables": [
374	      {
375	        "name": "Table 3: Llama 4 Scout Pareto Frontier",
376	        "columns": [
377	          "layer_idx",
378	          "layer_depth_pct",
379	          "en_auroc",
380	          "zs_mean_auroc_19",
381	          "zs_drop_pp",
382	          "on_pareto"
383	        ],
384	        "rows": [
385	          [
386	            4,
387	            8,
388	            0.634,
389	            0.624,
390	            1.0,
391	            false
392	          ],
393	          [
394	            8,
395	            17,
396	            0.672,
397	            0.659,
398	            1.3,
399	            false
400	          ],
401	          [
402	            12,
403	            25,
404	            0.714,
405	            0.699,
406	            1.5,
407	            false
408	          ],
409	          [
410	            16,
411	            33,
412	            0.745,
413	            0.729,
414	            1.6,
415	            false
416	          ],
417	          [
418	            20,
419	            42,
420	            0.768,
421	            0.748,
422	            2.0,
423	            true
424	          ],
425	          [
426	            24,
427	            50,
428	            0.786,
429	            0.745,
430	            4.1,
431	            true
432	          ],
433	          [
434	            28,
435	            58,
436	            0.798,
437	            0.741,
438	            5.7,
439	            true
440	          ],
441	          [
442	            32,
443	            67,
444	            0.81,
445	            0.732,
446	            7.8,
447	            true
448	          ],
449	          [
450	            36,
451	            75,
452	            0.821,
453	            0.714,
454	            10.7,
455	            false
456	          ],
457	          [
458	            40,
459	            83,
460	            0.818,
461	            0.689,
462	            12.9,
463	            false
464	          ],
465	          [
466	            44,
467	            92,
468	            0.804,
469	            0.651,
470	            15.3,
471	            false
472	          ],
473	          [
474	            48,
475	            100,
476	            0.771,
477	            0.608,
478	            16.3,
479	            false
480	          ]
481	        ]
482	      },
483	      {
484	        "name": "Table 4: Cross-Architecture Pareto Frontier Agreement",
485	        "columns": [
486	          "metric",
487	          "qwen3_235b",
488	          "llama4_scout",
489	          "agreement"
490	        ],
491	        "rows": [
492	          [
493	            "best_en_layer_depth_pct",
494	            77,
495	            75,
496	            "within 2pp"
497	          ],
498	          [
499	            "best_transfer_layer_depth_pct",
500	            60,
501	            58,
502	            "within 2pp"
503	          ],
504	          [
505	            "pareto_zone_depth_range_pct",
506	            "43-64",
507	            "42-67",
508	            "overlapping"
509	          ],
510	          [
511	            "depth_transfer_rank_corr",
512	            0.88,
513	            0.82,
514	            "both >0.75"
515	          ],
516	          [
517	            "frontier_shape",
518	            "convex monotonic",
519	            "convex monotonic",
520	            "consistent"
521	          ]
522	        ]
523	      }
524	    ],
525	    "figures": [],
526	    "analysis": "Cross-architecture agreement is high: both models show best transfer at ~59% depth, the Pareto frontier occupies the 42-67% depth band, and the rank correlation between depth and transfer degradation exceeds 0.75 in both. The frontier shape is architecture-invariant — it's the depth-normalized position, not absolute layer count, that determines the tradeoff. This validates Claim 1 at scale.\n\n\nLlama 4 Scout has 48 layers (fewer than Qwen3's 94) and a different MoE routing strategy (16 experts, top-2). With roughly 109B total / ~17B active params, its active compute is smaller than Qwen3-235B's ~22B active. This yields ~2pp lower EN AUROC and ~2pp lower transfer AUROC. The Pareto frontier has fewer points (4 vs 6) due to coarser layer sampling (every 4th of 48 = 12 points), but the monotonic depth-transfer tradeoff still holds clearly. Llama 4 Scout's best transfer layer sits at ~58% depth (L28), remarkably close to Qwen3's 60%, suggesting a universal \"mid-depth transfer zone\" across architectures. The rank correlation is slightly lower (0.82 vs 0.88) due to fewer data points but still highly significant. Low-resource languages are slightly weaker because Meta's multilingual pretraining mix underrepresents African languages compared to Qwen3.\n"
527	  },
528	  {
529	    "name": "CaCLR Implementation and Comparative Evaluation",
530	    "description": "CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) implementation. Train on English labels + unlabeled parallel activations. Compare vs all 5 conditions across full Pareto frontier, both models × 20 languages. Hyperparameter tuning (α, β).\n",
531	    "results": {
532	      "best_alpha": 0.15,
533	      "best_beta": 0.08,
534	      "qwen3_caclr_auroc_mean_19lang": 0.814,
535	      "qwen3_caclr_ece_mean_19lang": 0.058,
536	      "qwen3_caclr_vs_linproj_auroc_delta_pp": 3.3,
537	      "qwen3_caclr_vs_zeroshot_auroc_delta_pp": 5.2,
538	      "qwen3_caclr_ece_reduction_vs_tempcal_pct": 40.8,
539	      "qwen3_caclr_best_operating_layer": 64,
540	      "llama4_caclr_auroc_mean_19lang": 0.793,
541	      "llama4_caclr_ece_mean_19lang": 0.064,
542	      "llama4_caclr_vs_linproj_auroc_delta_pp": 3.1,
543	      "llama4_caclr_vs_zeroshot_auroc_delta_pp": 5.2,
544	      "llama4_caclr_ece_reduction_vs_tempcal_pct": 38.5,
545	      "llama4_caclr_best_operating_layer": 32,
546	      "caclr_vs_linproj_auroc_delta_pp_mean": 3.2,
547	      "caclr_ece_reduction_vs_tempcal_pct_mean": 39.7,
548	      "caclr_improvement_pass_rate": 0.92,
549	      "caclr_pareto_shift_layers": 2,
550	      "low_resource_caclr_auroc": {
551	        "sw_qwen3": 0.731,
552	        "yo_qwen3": 0.709,
553	        "ig_qwen3": 0.718,
554	        "sw_llama4": 0.712,
555	        "yo_llama4": 0.681,
556	        "ig_llama4": 0.698
557	      },
558	      "low_resource_zs_pass_rate": 1.0
559	    },
560	    "tables": [
561	      {
562	        "name": "Table 5: CaCLR vs Baselines — Full Comparison (averaged across both architectures)",
563	        "columns": [
564	          "method",
565	          "auroc_mean_19",
566	          "ece_mean_19",
567	          "requires_target_labels",
568	          "params_overhead"
569	        ],
570	        "rows": [
571	          [
572	            "zero-shot",
573	            0.752,
574	            0.098,
575	            "no",
576	            "0"
577	          ],
578	          [
579	            "mean-shift",
580	            0.747,
581	            0.102,
582	            "no",
583	            "0"
584	          ],
585	          [
586	            "linear_projection",
587	            0.77,
588	            0.082,
589	            "no",
590	            "d×d matrix"
591	          ],
592	          [
593	            "few-shot-25",
594	            0.738,
595	            0.089,
596	            "yes (25)",
597	            "0"
598	          ],
599	          [
600	            "few-shot-100",
601	            0.762,
602	            0.079,
603	            "yes (100)",
604	            "0"
605	          ],
606	          [
607	            "CaCLR",
608	            0.804,
609	            0.061,
610	            "no",
611	            "~1% probe params"
612	          ]
613	        ]
614	      },
615	      {
616	        "name": "Table 6: CaCLR Ablation — Loss Component Contributions",
617	        "columns": [
618	          "configuration",
619	          "auroc_mean_19",
620	          "ece_mean_19",
621	          "delta_vs_full_auroc_pp"
622	        ],
623	        "rows": [
624	          [
625	            "L_BCE_only (= zero-shot probe)",
626	            0.752,
627	            0.098,
628	            -5.2
629	          ],
630	          [
631	            "L_BCE + L_SB-ECE",
632	            0.768,
633	            0.072,
634	            -3.6
635	          ],
636	          [
637	            "L_BCE + L_consistency",
638	            0.793,
639	            0.078,
640	            -1.1
641	          ],
642	          [
643	            "L_BCE + L_SB-ECE + L_consistency (full CaCLR)",
644	            0.804,
645	            0.061,
646	            0.0
647	          ]
648	        ]
649	      },
650	      {
651	        "name": "Table 7: CaCLR Pareto Frontier Shift (Qwen3-235B)",
652	        "columns": [
653	          "layer_idx",
654	          "zs_auroc_19",
655	          "caclr_auroc_19",
656	          "shift_pp",
657	          "on_shifted_pareto"
658	        ],
659	        "rows": [
660	          [
661	            40,
662	            0.776,
663	            0.798,
664	            2.2,
665	            false
666	          ],
667	          [
668	            44,
669	            0.774,
670	            0.8,
671	            2.6,
672	            false
673	          ],
674	          [
675	            48,
676	            0.77,
677	            0.803,
678	            3.3,
679	            true
680	          ],
681	          [
682	            52,
683	            0.765,
684	            0.806,
685	            4.1,
686	            true
687	          ],
688	          [
689	            56,
690	            0.762,
691	            0.81,
692	            4.8,
693	            true
694	          ],
695	          [
696	            60,
697	            0.753,
698	            0.814,
699	            6.1,
700	            true
701	          ],
702	          [
703	            64,
704	            0.741,
705	            0.814,
706	            7.3,
707	            true
708	          ],
709	          [
710	            68,
711	            0.728,
712	            0.808,
713	            8.0,
714	            true
715	          ],
716	          [
717	            72,
718	            0.712,
719	            0.796,
720	            8.4,
721	            false
722	          ]
723	        ]
724	      }
725	    ],
726	    "figures": [],
727	    "analysis": "CaCLR decisively outperforms all baselines. The ablation shows both loss terms contribute: L_consistency provides the bulk of AUROC improvement (+4.1pp alone), while L_SB-ECE provides calibration refinement (ECE drops from 0.078 to 0.061 when added). The interaction is synergistic — joint optimization yields better results than either term alone. The Pareto shift is the headline result: at the same EN calibration quality (L64, AUROC 0.835), CaCLR achieves 0.814 transfer vs 0.741 zero-shot — a 7.3pp improvement. This shifts the practical recommendation from \"use shallower layers for transfer\" to \"use CaCLR and operate at deeper, better-calibrated layers.\" The improvement pass rate of 92% (35/38 model-lang pairs) demonstrates consistency. The 3 non-improving pairs are high-resource languages (fr, nl, de on Llama 4 Scout) where zero-shot transfer is already excellent and the consistency loss has minimal signal to exploit.\n\n\nCaCLR's consistency loss (β·L_consistency) directly penalizes divergence between EN and non-EN probe outputs on parallel/comparable activations, forcing the probe to learn language-invariant features. This is strictly more informative than linear projection (which only aligns means and covariances post-hoc) because it shapes the learned representation during training. The 3.2pp AUROC gain over linear projection reflects the value of end-to-end optimization: linear projection corrects first-order distributional mismatch but not the nonlinear feature interactions that L_consistency captures. The SB-ECE term (α·L_SB-ECE) provides calibration-aware training that temperature scaling cannot — it directly optimizes the calibration objective rather than post-hoc rescaling. The 40% ECE reduction over temperature scaling arises because CaCLR addresses the root cause (representation misalignment) rather than the symptom (miscalibrated probabilities). The Pareto frontier shift is the key result: CaCLR allows operating 2 layers deeper than the ZS-optimal point while maintaining equivalent or better transfer — it literally pushes the Pareto frontier outward. Low-resource languages benefit most from L_consistency because their activation distributions are most misaligned from EN; the consistency term provides the strongest gradient signal precisely where the gap is largest.\n"
728	  },
729	  {
730	    "name": "Difficulty-Controlled Ablation",
731	    "description": "IRT difficulty probes (Ridge regression), project out difficulty direction, retrain correctness probes on residuals, evaluate transfer. 10 languages × 8 layers per model.\n",
732	    "results": {
733	      "difficulty_probe_r2_mean": 0.72,
734	      "difficulty_var_explained_pct_mean": 68.4,
735	      "difficulty_var_explained_pct_range": [
736	        58.2,
737	        79.1
738	      ],
739	      "residual_en_auroc_drop_pp": 4.2,
740	      "residual_zs_transfer_drop_pp": 1.1,
741	      "capability_specific_var_pct": 31.6,
742	      "capability_specific_transfer_degradation_pct": 87,
743	      "difficulty_component_transfer_degradation_pct": 13,
744	      "decomp_prescriptive_accuracy": 0.81,
745	      "difficulty_var_by_depth": {
746	        "shallow_20pct": 0.74,
747	        "mid_50pct": 0.69,
748	        "deep_80pct": 0.62
749	      },
750	      "capability_transfer_drop_by_depth": {
751	        "shallow_20pct": 0.8,
752	        "mid_50pct": 3.4,
753	        "deep_80pct": 9.7
754	      }
755	    },
756	    "tables": [
757	      {
758	        "name": "Table 8: Decomposition Results — Difficulty vs Capability Components",
759	        "columns": [
760	          "component",
761	          "var_explained_pct",
762	          "transfer_auroc_mean",
763	          "transfer_drop_from_en_pp",
764	          "share_of_total_transfer_drop_pct"
765	        ],
766	        "rows": [
767	          [
768	            "full_correctness",
769	            100,
770	            0.752,
771	            8.1,
772	            100
773	          ],
774	          [
775	            "difficulty_shared",
776	            68.4,
777	            0.738,
778	            1.1,
779	            13
780	          ],
781	          [
782	            "capability_specific",
783	            31.6,
784	            0.614,
785	            14.2,
786	            87
787	          ]
788	        ]
789	      },
790	      {
791	        "name": "Table 9: Capability-Specific Transfer Drop by Depth",
792	        "columns": [
793	          "depth_band",
794	          "difficulty_transfer_drop_pp",
795	          "capability_transfer_drop_pp",
796	          "ratio"
797	        ],
798	        "rows": [
799	          [
800	            "0-30%",
801	            0.3,
802	            0.8,
803	            "2.7×"
804	          ],
805	          [
806	            "30-60%",
807	            0.8,
808	            3.4,
809	            "4.3×"
810	          ],
811	          [
812	            "60-90%",
813	            1.6,
814	            9.7,
815	            "6.1×"
816	          ]
817	        ]
818	      }
819	    ],
820	    "figures": [],
821	    "analysis": "The decomposition cleanly separates: difficulty-shared signal is the majority (68%) of correctness variance and transfers near-perfectly across languages and depths. The capability-specific residual (32%) drives nearly all transfer degradation (87%), and this degradation accelerates exponentially with depth. This explains the Pareto frontier mechanistically: deeper layers have stronger capability-specific signals that improve EN calibration but impede transfer. CaCLR works because its consistency loss specifically targets the capability-specific component — forcing alignment of the non-difficulty residual across languages. The prescriptive value (81% accuracy in predicting when CaCLR is needed) confirms this is a load-bearing decomposition, not a post-hoc narrative.\n\n\nIRT difficulty is a strong, language-agnostic property — harder questions are harder everywhere. Ridge regression captures this cleanly (R²=0.72) because difficulty is linearly encoded in intermediate representations (Civelli et al. confirmed this). The difficulty component accounts for 68% of explained variance because GlobalMMLU correctness is heavily driven by item difficulty: a model gets easy questions right in all languages and hard questions wrong in all languages. After projecting out difficulty, the residual correctness signal is \"capability-specific\" — it captures language-dependent competence differences. This residual transfers poorly at deep layers (9.7pp drop at 80% depth vs 0.8pp at 20% depth) because deep layers encode language-specific processing that makes capability assessments non-transferable. The difficulty component transfers well at all depths (only 13% of total transfer degradation) because it's language-invariant by construction. This decomposition is prescriptive: when difficulty explains most of a language's correctness variance, simple zero-shot transfer suffices; when the capability residual is large, CaCLR is needed. The 81% prescriptive accuracy validates the decomposition as more than descriptive.\n"
822	  },
823	  {
824	    "name": "Cross-Lingual Orthogonality Analysis",
825	    "description": "Extract verbalized confidence direction via prompted confidence scores, compute cosine similarity with correctness direction across 20 languages × 2 architectures. Analyze by resource tier and language family.\n",
826	    "results": {
827	      "orthogonality_cosine_mean_overall": 0.052,
828	      "orthogonality_cosine_range": [
829	        0.018,
830	        0.094
831	      ],
832	      "orthogonality_cosine_en": 0.034,
833	      "qwen3_cosine_mean": 0.048,
834	      "llama4_cosine_mean": 0.057,
835	      "high_resource_cosine_mean": 0.041,
836	      "mid_resource_cosine_mean": 0.054,
837	      "low_resource_cosine_mean": 0.074,
838	      "cosine_by_lang": {
839	        "en": 0.034,
840	        "zh": 0.038,
841	        "de": 0.036,
842	        "fr": 0.039,
843	        "es": 0.041,
844	        "ja": 0.044,
845	        "ru": 0.043,
846	        "pt": 0.04,
847	        "it": 0.042,
848	        "ar": 0.051,
849	        "hi": 0.055,
850	        "ko": 0.049,
851	        "vi": 0.058,
852	        "th": 0.061,
853	        "bn": 0.056,
854	        "tr": 0.052,
855	        "nl": 0.037,
856	        "sw": 0.078,
857	        "yo": 0.094,
858	        "ig": 0.082
859	      },
860	      "all_langs_below_0p1": true,
861	      "cosine_resource_tier_correlation": -0.68
862	    },
863	    "tables": [
864	      {
865	        "name": "Table 10: Correctness-Confidence Cosine Similarity by Language and Architecture",
866	        "columns": [
867	          "language",
868	          "resource_tier",
869	          "qwen3_cosine",
870	          "llama4_cosine",
871	          "mean_cosine"
872	        ],
873	        "rows": [
874	          [
875	            "en",
876	            "high",
877	            0.031,
878	            0.037,
879	            0.034
880	          ],
881	          [
882	            "zh",
883	            "high",
884	            0.035,
885	            0.041,
886	            0.038
887	          ],
888	          [
889	            "de",
890	            "high",
891	            0.033,
892	            0.039,
893	            0.036
894	          ],
895	          [
896	            "fr",
897	            "high",
898	            0.036,
899	            0.042,
900	            0.039
901	          ],
902	          [
903	            "es",
904	            "high",
905	            0.038,
906	            0.044,
907	            0.041
908	          ],
909	          [
910	            "ja",
911	            "high",
912	            0.041,
913	            0.047,
914	            0.044
915	          ],
916	          [
917	            "ru",
918	            "high",
919	            0.04,
920	            0.046,
921	            0.043
922	          ],
923	          [
924	            "pt",
925	            "high",
926	            0.037,
927	            0.043,
928	            0.04
929	          ],
930	          [
931	            "it",
932	            "high",
933	            0.039,
934	            0.045,
935	            0.042
936	          ],
937	          [
938	            "nl",
939	            "high",
940	            0.034,
941	            0.04,
942	            0.037
943	          ],
944	          [
945	            "ar",
946	            "mid",
947	            0.047,
948	            0.055,
949	            0.051
950	          ],
951	          [
952	            "hi",
953	            "mid",
954	            0.051,
955	            0.059,
956	            0.055
957	          ],
958	          [
959	            "ko",
960	            "mid",
961	            0.045,
962	            0.053,
963	            0.049
964	          ],
965	          [
966	            "vi",
967	            "mid",
968	            0.054,
969	            0.062,
970	            0.058
971	          ],
972	          [
973	            "th",
974	            "mid",
975	            0.057,
976	            0.065,
977	            0.061
978	          ],
979	          [
980	            "bn",
981	            "mid",
982	            0.052,
983	            0.06,
984	            0.056
985	          ],
986	          [
987	            "tr",
988	            "mid",
989	            0.048,
990	            0.056,
991	            0.052
992	          ],
993	          [
994	            "sw",
995	            "low",
996	            0.073,
997	            0.083,
998	            0.078
999	          ],
1000	          [
1001	            "yo",
1002	            "low",
1003	            0.089,
1004	            0.099,
1005	            0.094
1006	          ],
1007	          [
1008	            "ig",
1009	            "low",
1010	            0.077,
1011	            0.087,
1012	            0.082
1013	          ]
1014	        ]
1015	      },
1016	      {
1017	        "name": "Table 11: Orthogonality Summary Statistics",
1018	        "columns": [
1019	          "statistic",
1020	          "qwen3_235b",
1021	          "llama4_scout",
1022	          "both_models"
1023	        ],
1024	        "rows": [
1025	          [
1026	            "cosine_mean",
1027	            0.048,
1028	            0.057,
1029	            0.052
1030	          ],
1031	          [
1032	            "cosine_std",
1033	            0.015,
1034	            0.017,
1035	            0.016
1036	          ],
1037	          [
1038	            "cosine_max",
1039	            0.089,
1040	            0.099,
1041	            0.094
1042	          ],
1043	          [
1044	            "cosine_min",
1045	            0.031,
1046	            0.037,
1047	            0.018
1048	          ],
1049	          [
1050	            "all_below_0.1",
1051	            "yes (20/20)",
1052	            "yes (19/20)",
1053	            "39/40"
1054	          ],
1055	          [
1056	            "resource_tier_corr",
1057	            -0.71,
1058	            -0.65,
1059	            -0.68
1060	          ]
1061	        ]
1062	      }
1063	    ],
1064	    "figures": [],
1065	    "analysis": "Orthogonality generalizes comprehensively. The mean cosine of 0.052 across all 40 language-architecture pairs is well within the \"near-orthogonal\" regime (< 0.1). The resource-tier gradient is the novel finding: it suggests that output-based calibration methods are not just structurally limited but are *more* limited for well-resourced languages where the orthogonality is strongest. This strengthens the motivation for probe-based approaches universally and for CaCLR specifically in multilingual settings. Yoruba's 0.094 is the only value approaching the 0.1 threshold (on Llama4 it hits 0.099), which is worth noting but does not break the claim.\n\n\nMiao & Ungar (2026) established correctness-confidence orthogonality (cosine < 0.04) for English on 7-8B models. We extend to 20 languages on larger models. The orthogonality persists universally (all < 0.1) because it reflects a fundamental architectural property: verbalized confidence is generated by the language modeling head from surface-level token probabilities, while correctness is encoded in intermediate representation geometry. These are structurally decoupled in transformer architectures. The slight increase in cosine for low-resource languages (0.074 mean vs 0.041 for high-resource) occurs because low-resource languages have noisier confidence elicitation — the model's verbalized confidence in Yoruba is less well-calibrated and leaks some correctness signal, producing weak correlation. The resource-tier gradient (ρ=-0.68) suggests that better multilingual training data produces cleaner separation between correctness and confidence representations. The cross-architecture consistency (Qwen3: 0.048, Llama4: 0.057) confirms this is not architecture-specific. Llama 4's slightly higher cosines may reflect its less aggressive multilingual pretraining compared to Qwen3.\n"
1066	  },
1067	  {
1068	    "name": "Probe Complexity Comparison",
1069	    "description": "Logistic regression vs 2-layer MLP at each probed layer, both models. Compare English accuracy, cross-lingual transfer degradation, calibration quality.\n",
1070	    "results": {
1071	      "logreg_en_auroc_best": 0.843,
1072	      "mlp_en_auroc_best": 0.856,
1073	      "mlp_en_auroc_gain_pp": 1.3,
1074	      "logreg_zs_transfer_drop_mean_pp": 8.1,
1075	      "mlp_zs_transfer_drop_mean_pp": 12.4,
1076	      "transfer_degradation_ratio": 1.53,
1077	      "logreg_ece_mean": 0.054,
1078	      "mlp_ece_mean": 0.068,
1079	      "logreg_transfer_advantage_shallow_pp": 2.1,
1080	      "logreg_transfer_advantage_deep_pp": 6.8
1081	    },
1082	    "tables": [
1083	      {
1084	        "name": "Table 12: Probe Complexity Comparison",
1085	        "columns": [
1086	          "probe_type",
1087	          "en_auroc_best",
1088	          "zs_auroc_mean_19",
1089	          "zs_drop_pp",
1090	          "ece_mean_19"
1091	        ],
1092	        "rows": [
1093	          [
1094	            "logistic_regression",
1095	            0.843,
1096	            0.762,
1097	            8.1,
1098	            0.054
1099	          ],
1100	          [
1101	            "mlp_2layer",
1102	            0.856,
1103	            0.733,
1104	            12.4,
1105	            0.068
1106	          ]
1107	        ]
1108	      }
1109	    ],
1110	    "figures": [],
1111	    "analysis": "Linear probes are the correct choice for cross-lingual transfer: they sacrifice 1.3pp EN AUROC but gain 4.3pp average transfer. The depth interaction effect is notable — the logreg advantage grows from 2.1pp at shallow layers to 6.8pp at deep layers, confirming that deep-layer transfer degradation is driven by nonlinear, language- specific features. CaCLR + logreg is thus the optimal configuration.\n\n\nLinear probes transfer better because they learn a single hyperplane in activation space — the hyperplane generalizes across languages when the underlying geometry is approximately shared (as it is in mid-depth layers). MLPs learn nonlinear decision boundaries that fit English-specific feature interactions, gaining ~1.3pp EN AUROC but losing ~4.3pp in transfer. The transfer gap widens at deeper layers (6.8pp advantage for logreg) because deep layers have more language-specific nonlinear structure that MLPs exploit but logreg ignores. This justifies our choice of linear probes for the main results and supports the geometric interpretation of the Pareto frontier: it's about linear subspace alignment, not complex feature interactions.\n"
1112	  },
1113	  {
1114	    "name": "Additional Benchmark Evaluation (Belebele + MMLU-ProX)",
1115	    "description": "Evaluate best probes + CaCLR on Belebele (20 languages) and MMLU-ProX (20 languages).\n",
1116	    "results": {
1117	      "belebele_zs_auroc_mean_19": 0.738,
1118	      "belebele_caclr_auroc_mean_19": 0.789,
1119	      "belebele_caclr_vs_zs_pp": 5.1,
1120	      "belebele_ece_reduction_vs_tempcal_pct": 36.2,
1121	      "mmlupx_zs_auroc_mean_19": 0.722,
1122	      "mmlupx_caclr_auroc_mean_19": 0.774,
1123	      "mmlupx_caclr_vs_zs_pp": 5.2,
1124	      "mmlupx_ece_reduction_vs_tempcal_pct": 33.8,
1125	      "caclr_benefit_cross_benchmark_cv": 0.08
1126	    },
1127	    "tables": [
1128	      {
1129	        "name": "Table 13: Cross-Benchmark Generalization",
1130	        "columns": [
1131	          "benchmark",
1132	          "zs_auroc_mean_19",
1133	          "caclr_auroc_mean_19",
1134	          "caclr_gain_pp",
1135	          "ece_reduction_pct"
1136	        ],
1137	        "rows": [
1138	          [
1139	            "GlobalMMLU",
1140	            0.752,
1141	            0.804,
1142	            5.2,
1143	            39.7
1144	          ],
1145	          [
1146	            "Belebele",
1147	            0.738,
1148	            0.789,
1149	            5.1,
1150	            36.2
1151	          ],
1152	          [
1153	            "MMLU-ProX",
1154	            0.722,
1155	            0.774,
1156	            5.2,
1157	            33.8
1158	          ]
1159	        ]
1160	      }
1161	    ],
1162	    "figures": [],
1163	    "analysis": "CaCLR generalizes cleanly across benchmarks. The improvement magnitude is remarkably stable (5.1-5.2pp AUROC, 33-40% ECE reduction), suggesting the method addresses a fundamental representation alignment issue rather than overfitting to GlobalMMLU- specific patterns. This is critical for reviewer confidence.\n\n\nBelebele tests reading comprehension (vs GlobalMMLU's factual knowledge), providing domain generalization evidence. Transfer AUROC is slightly lower (0.738 vs 0.762) because Belebele's passage-dependent questions have weaker difficulty-shared signal — comprehension difficulty is more language-dependent than factual difficulty. CaCLR still provides ~5pp improvement, confirming the consistency loss generalizes beyond factual MCQA. MMLU-ProX has harder questions that compress the AUROC distribution (lower base rate of correctness), yielding slightly lower absolute numbers but comparable CaCLR benefit. The cross-benchmark CV of 0.08 for CaCLR improvement confirms the method is robust to evaluation domain.\n"
1164	  },
1165	  {
1166	    "name": "INT8 Validation Ablation",
1167	    "description": "Compare INT8 vs FP16 probing results at 5 representative layers for Llama 4 Scout on 5% random subset.\n",
1168	    "results": {
1169	      "int8_fp16_auroc_diff_mean_pp": 0.3,
1170	      "int8_fp16_auroc_diff_max_pp": 0.7,
1171	      "int8_fp16_ece_diff_mean_pp": 0.2,
1172	      "int8_fp16_transfer_drop_diff_pp": 0.4,
1173	      "int8_fp16_rank_correlation": 0.997,
1174	      "conclusion": "INT8 quantization introduces negligible distortion"
1175	    },
1176	    "tables": [
1177	      {
1178	        "name": "Table S1: INT8 vs FP16 Comparison (Llama 4 Scout, 5% subset)",
1179	        "columns": [
1180	          "layer_idx",
1181	          "fp16_auroc",
1182	          "int8_auroc",
1183	          "diff_pp",
1184	          "fp16_zs_auroc_5lang",
1185	          "int8_zs_auroc_5lang",
1186	          "transfer_diff_pp"
1187	        ],
1188	        "rows": [
1189	          [
1190	            8,
1191	            0.674,
1192	            0.672,
1193	            0.2,
1194	            0.661,
1195	            0.658,
1196	            0.3
1197	          ],
1198	          [
1199	            16,
1200	            0.747,
1201	            0.745,
1202	            0.2,
1203	            0.731,
1204	            0.728,
1205	            0.3
1206	          ],
1207	          [
1208	            24,
1209	            0.788,
1210	            0.786,
1211	            0.2,
1212	            0.747,
1213	            0.744,
1214	            0.3
1215	          ],
1216	          [
1217	            32,
1218	            0.812,
1219	            0.81,
1220	            0.2,
1221	            0.734,
1222	            0.731,
1223	            0.3
1224	          ],
1225	          [
1226	            40,
1227	            0.82,
1228	            0.817,
1229	            0.3,
1230	            0.691,
1231	            0.687,
1232	            0.4
1233	          ]
1234	        ]
1235	      }
1236	    ],
1237	    "figures": [],
1238	    "analysis": "INT8 quantization is validated as safe for our experimental setup. The maximum observed difference (0.7pp at a single layer-language combination) is well within the noise floor of probing experiments. The Pareto frontier ordering is perfectly preserved (rank correlation 0.997). This ablation preempts reviewer concern #5.\n\n\nINT8 weight-only quantization preserves the 8 most significant bits of each weight, introducing per-channel quantization noise of ~0.4% relative magnitude. Correctness probing relies on the geometry of activation space (direction of correctness signal), not absolute magnitudes. The quantization noise is approximately isotropic and thus preserves angular relationships between directions. The 0.3pp mean AUROC difference is within random seed variance, and the rank correlation of 0.997 between INT8 and FP16 layer rankings confirms that the Pareto frontier shape is unaffected. This result is expected given prior work showing that probing results are robust to quantization down to INT4 (Gao et al., 2024).\n"
1239	  },
1240	  {
1241	    "name": "Gemma 4 31B Dense — Third Architecture (Camera-Ready)",
1242	    "description": "Full Pareto frontier on Gemma 4 31B Dense (60 layers), 20+ languages. Provides dense vs MoE architectural contrast.\n",
1243	    "results": {
1244	      "en_auroc_best_layer": 0.812,
1245	      "en_best_layer_idx": 45,
1246	      "zs_transfer_auroc_mean_19lang": 0.734,
1247	      "zs_best_transfer_layer_idx": 36,
1248	      "zs_transfer_drop_mean_pp": 7.8,
1249	      "pareto_depth_transfer_rank_corr": 0.86,
1250	      "caclr_auroc_mean_19lang": 0.786,
1251	      "caclr_vs_linproj_auroc_delta_pp": 2.9,
1252	      "dense_vs_moe_transfer_comparison": "comparable within 2pp",
1253	      "pareto_shape": "convex monotonic, consistent with MoE models"
1254	    },
1255	    "tables": [
1256	      {
1257	        "name": "Table 14: Three-Architecture Summary",
1258	        "columns": [
1259	          "model",
1260	          "type",
1261	          "layers",
1262	          "en_auroc_best",
1263	          "zs_auroc_mean_19",
1264	          "best_transfer_depth_pct",
1265	          "pareto_rank_corr",
1266	          "caclr_gain_pp"
1267	        ],
1268	        "rows": [
1269	          [
1270	            "Qwen3-235B-A22B",
1271	            "MoE",
1272	            94,
1273	            0.843,
1274	            0.762,
1275	            60,
1276	            0.88,
1277	            3.3
1278	          ],
1279	          [
1280	            "Llama 4 Scout",
1281	            "MoE",
1282	            48,
1283	            0.821,
1284	            0.741,
1285	            58,
1286	            0.82,
1287	            3.1
1288	          ],
1289	          [
1290	            "Gemma 4 31B Dense",
1291	            "Dense",
1292	            60,
1293	            0.812,
1294	            0.734,
1295	            60,
1296	            0.86,
1297	            2.9
1298	          ]
1299	        ]
1300	      }
1301	    ],
1302	    "figures": [],
1303	    "analysis": "The three-architecture comparison is the strongest evidence for the universality of the depth-transferability tradeoff. The best-transfer depth converges to 58-60% across dense and MoE architectures with 48-94 layers, CaCLR provides consistent 2.9-3.3pp improvement, and the Pareto rank correlation is 0.82-0.88 in all cases. Dense vs MoE makes minimal difference — the phenomenon is a property of transformer depth, not routing architecture.\n\n\nGemma 4 31B Dense has fewer total parameters than the MoE models but all are active, yielding comparable per-token compute. As a dense model, its representations are more uniformly distributed across layers (no expert routing), producing slightly smoother Pareto frontiers. The best-transfer depth (~60%) matches both MoE models, confirming this is a universal property of transformer depth, not MoE-specific. EN AUROC is slightly lower (0.812 vs 0.843/0.821) because 31B active params < 22B active with MoE routing benefits. CaCLR improvement is slightly lower (2.9pp) on the dense model because the absence of expert routing means less language-specific feature fragmentation to correct. This is the ideal third data point: different architecture family, consistent findings.\n"
1304	  },
1305	  {
1306	    "name": "Extended Language Coverage (Camera-Ready)",
1307	    "description": "Expand from 20 to 50+ languages for camera-ready, leveraging GlobalMMLU/Belebele full language sets.\n",
1308	    "results": {
1309	      "total_languages": 52,
1310	      "new_languages_added": 32,
1311	      "zs_auroc_above_0p60_count": 48,
1312	      "zs_auroc_below_0p55_count": 2,
1313	      "caclr_improvement_positive_count": 49,
1314	      "mean_zs_auroc_51lang": 0.72,
1315	      "mean_caclr_auroc_51lang": 0.77,
1316	      "pareto_frontier_holds_all_langs": true,
1317	      "new_language_families_covered": [
1318	        "Austronesian",
1319	        "Dravidian",
1320	        "Niger-Congo B",
1321	        "Uralic",
1322	        "Kartvelian"
1323	      ]
1324	    },
1325	    "tables": [
1326	      {
1327	        "name": "Table 15: Extended Language Coverage Summary by Resource Tier",
1328	        "columns": [
1329	          "tier",
1330	          "n_langs",
1331	          "zs_auroc_mean",
1332	          "caclr_auroc_mean",
1333	          "caclr_gain_pp",
1334	          "pct_above_0p60"
1335	        ],
1336	        "rows": [
1337	          [
1338	            "high",
1339	            12,
1340	            0.782,
1341	            0.812,
1342	            3.0,
1343	            100
1344	          ],
1345	          [
1346	            "mid",
1347	            25,
1348	            0.738,
1349	            0.784,
1350	            4.6,
1351	            100
1352	          ],
1353	          [
1354	            "low",
1355	            10,
1356	            0.661,
1357	            0.712,
1358	            5.1,
1359	            90
1360	          ],
1361	          [
1362	            "very_low",
1363	            4,
1364	            0.582,
1365	            0.638,
1366	            5.6,
1367	            50
1368	          ]
1369	        ]
1370	      }
1371	    ],
1372	    "figures": [],
1373	    "analysis": "The extension to 52 languages confirms all findings at broader scale. The resource-tier gradient is smooth and predictable — no language family shows anomalous behavior. CaCLR's benefit is inversely correlated with resource level (3.0pp for high-resource to 5.6pp for very-low-resource), confirming that the consistency loss provides most value where representation misalignment is worst. The 48/51 pass rate (>0.60 AUROC) for zero-shot CaCLR transfer with no target-language labels is the practical headline for camera-ready: usable cross-lingual calibration for the vast majority of languages.\n\nExpanding to 50+ languages primarily adds mid-resource languages (Indonesian, Malay, Finnish, Georgian, Tamil, Telugu, etc.) where the model has moderate pretraining exposure. Most new languages fall in the 0.65-0.78 AUROC range, consistent with the mid-resource tier from the 20-language set. A handful of extremely low-resource languages (e.g., Amharic script languages with minimal pretraining data) may fall below 0.55, but these represent edge cases rather than systematic failures. CaCLR continues to improve 96% of languages because the consistency loss mechanism is language-agnostic — it aligns activation distributions without requiring any language-specific knowledge. The Pareto frontier structure is preserved across all 52 languages, confirming it's a depth property, not a language-set artifact.\n"
1374	  }
1375	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbc758a5-91f3-4b5d-b4b1-dd90569ab86a",
  "isSidechain": false,
  "promptId": "907ecca9-b4a5-4dd2-af0b-6dcee3e5aad0",
  "type": "user",
  "uuid": "5a87d5e0-5937-4a17-bf39-e45a06d58e68",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Full Pareto Frontier — Qwen3-235B-A22B\",\n    \"description\": \"Extract activations at every 4th layer (24 probed layers out of 94), 20 languages, train English correctness probes (logistic regression + 2-layer MLP), evaluate 5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR).\\n\",\n    \"results\": {\n      \"en_auroc_best_layer\": 0.843,\n      \"en_best_layer_idx\": 72,\n      \"en_auroc_range\": [\n        0.621,\n        0.843\n      ],\n      \"en_ece_raw_best\": 0.162,\n      \"en_ece_tempcal_best\": 0.054,\n      \"temp_scaling_T\": 4.87,\n      \"zs_transfer_auroc_mean_19lang_best_transfer_layer\": 0.762,\n      \"zs_best_transfer_layer_idx\": 56,\n      \"zs_transfer_drop_from_en_mean_pp\": 8.1,\n      \"zs_auroc_by_tier\": {\n        \"high_resource_mean\": 0.791,\n        \"mid_resource_mean\": 0.754,\n        \"low_resource_mean\": 0.683\n      },\n      \"zs_auroc_by_lang\": {\n        \"en\": 0.843,\n        \"zh\": 0.802,\n        \"de\": 0.796,\n        \"fr\": 0.793,\n        \"es\": 0.789,\n        \"ja\": 0.785,\n        \"ru\": 0.782,\n        \"pt\": 0.788,\n        \"it\": 0.786,\n        \"ar\": 0.768,\n        \"hi\": 0.761,\n        \"ko\": 0.755,\n        \"vi\": 0.749,\n        \"th\": 0.743,\n        \"bn\": 0.738,\n        \"tr\": 0.756,\n        \"nl\": 0.79,\n        \"sw\": 0.695,\n        \"yo\": 0.672,\n        \"ig\": 0.681\n      },\n      \"mean_shift_improvement_count\": 2,\n      \"mean_shift_delta_ece_mean\": 1.41,\n      \"linproj_auroc_mean_19lang\": 0.724,\n      \"fewshot_25_auroc_mean_19lang\": 0.748,\n      \"fewshot_100_auroc_mean_19lang\": 0.771,\n      \"pareto_depth_transfer_rank_corr\": 0.88,\n      \"pareto_frontier_layers\": [\n        40,\n        44,\n        48,\n        52,\n        56,\n        60\n      ],\n      \"layers_above_0p5_auroc_count\": 22\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Qwen3-235B Pareto Frontier — EN AUROC vs ZS Transfer AUROC by Layer\",\n        \"columns\": [\n          \"layer_idx\",\n          \"layer_depth_pct\",\n          \"en_auroc\",\n          \"zs_mean_auroc_19\",\n          \"zs_drop_pp\",\n          \"on_pareto\"\n        ],\n        \"rows\": [\n          [\n            4,\n            4,\n            0.621,\n            0.608,\n            1.3,\n            false\n          ],\n          [\n            8,\n            9,\n            0.648,\n            0.637,\n            1.1,\n            false\n          ],\n          [\n            12,\n            13,\n            0.689,\n            0.671,\n            1.8,\n            false\n          ],\n          [\n            16,\n            17,\n            0.712,\n            0.698,\n            1.4,\n            false\n          ],\n          [\n            20,\n            21,\n            0.738,\n            0.724,\n            1.4,\n            false\n          ],\n          [\n            24,\n            26,\n            0.756,\n            0.742,\n            1.4,\n            false\n          ],\n          [\n            28,\n            30,\n            0.771,\n            0.755,\n            1.6,\n            false\n          ],\n          [\n            32,\n            34,\n            0.784,\n            0.764,\n            2.0,\n            false\n          ],\n          [\n            36,\n            38,\n            0.795,\n            0.771,\n            2.4,\n            false\n          ],\n          [\n            40,\n            43,\n            0.803,\n            0.776,\n            2.7,\n            true\n          ],\n          [\n            44,\n            47,\n            0.81,\n            0.774,\n            3.6,\n            true\n          ],\n          [\n            48,\n            51,\n            0.816,\n            0.77,\n            4.6,\n            true\n          ],\n          [\n            52,\n            55,\n            0.822,\n            0.765,\n            5.7,\n            true\n          ],\n          [\n            56,\n            60,\n            0.827,\n            0.762,\n            6.5,\n            true\n          ],\n          [\n            60,\n            64,\n            0.831,\n            0.753,\n            7.8,\n            true\n          ],\n          [\n            64,\n            68,\n            0.835,\n            0.741,\n            9.4,\n            false\n          ],\n          [\n            68,\n            72,\n            0.839,\n            0.728,\n            11.1,\n            false\n          ],\n          [\n            72,\n            77,\n            0.843,\n            0.712,\n            13.1,\n            false\n          ],\n          [\n            76,\n            81,\n            0.841,\n            0.694,\n            14.7,\n            false\n          ],\n          [\n            80,\n            85,\n            0.838,\n            0.671,\n            16.7,\n            false\n          ],\n          [\n            84,\n            89,\n            0.832,\n            0.643,\n            18.9,\n            false\n          ],\n          [\n            88,\n            94,\n            0.819,\n            0.611,\n            20.8,\n            false\n          ],\n          [\n            92,\n            98,\n            0.791,\n            0.574,\n            21.7,\n            false\n          ],\n          [\n            94,\n            100,\n            0.762,\n            0.541,\n            22.1,\n            false\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: Transfer Condition Comparison (at best-transfer layer L56)\",\n        \"columns\": [\n          \"condition\",\n          \"auroc_mean_19\",\n          \"ece_mean_19\",\n          \"ece_reduction_vs_tempcal_pct\"\n        ],\n        \"rows\": [\n          [\n            \"zero-shot\",\n            0.762,\n            0.098,\n            0\n          ],\n          [\n            \"mean-shift\",\n            0.758,\n            0.101,\n            -3.1\n          ],\n          [\n            \"linear_projection\",\n            0.781,\n            0.082,\n            16.3\n          ],\n          [\n            \"few-shot-25\",\n            0.748,\n            0.089,\n            9.2\n          ],\n          [\n            \"few-shot-100\",\n            0.771,\n            0.079,\n            19.4\n          ],\n          [\n            \"CaCLR\",\n            0.814,\n            0.058,\n            40.8\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The Pareto frontier is crisp and monotonic: 6 layers form the efficient frontier between L40-L60. The rank correlation (Spearman) between layer depth and transfer degradation is ρ=0.88 (p<0.001). The frontier's shape confirms that the depth- transferability tradeoff is not an artifact of small models — it amplifies at scale. The 16pp gap between best-EN layer (L72) and best-transfer layer (L56) is larger than MVP's ~3-layer gap, consistent with deeper models having more room for language-specific specialization. All high-resource languages pass AUROC > 0.75 at the best-transfer layer; all low-resource languages exceed 0.65.\\n\\n\\nQwen3-235B-A22B is a 94-layer MoE with massive representation capacity. The jump from MVP's 7B (en AUROC 0.754) to 235B is expected to yield ~9pp AUROC gain, consistent with prior probing literature showing log-linear scaling of linear probe accuracy with model parameters (Burns et al., Marks et al.). The MoE architecture concentrates expert representations, producing cleaner correctness signals in intermediate layers. The Pareto frontier emerges because deeper layers (L72+) specialize for English-dominant pretraining data distribution — the model's language-specific processing intensifies past ~75% depth, degrading cross-lingual invariance. The best transfer layer (L56, ~60% depth) sits in the \\\"universal reasoning\\\" zone before language-specific heads activate. Low-resource languages (sw, yo, ig) still transfer above 0.65 AUROC because GlobalMMLU questions share structural patterns that even underrepresented languages partially align with in middle layers. Mean-shift continues to mostly fail because correctness directions are not simply mean-offset between languages — they require rotation, not translation, which linear projection and CaCLR address.\\n\"\n  },\n  {\n    \"name\": \"Full Pareto Frontier — Llama 4 Scout\",\n    \"description\": \"Extract activations at every 4th layer (12 probed layers out of 48), 20 languages, 5 transfer conditions. INT8 weight quantization.\\n\",\n    \"results\": {\n      \"en_auroc_best_layer\": 0.821,\n      \"en_best_layer_idx\": 36,\n      \"en_auroc_range\": [\n        0.634,\n        0.821\n      ],\n      \"en_ece_raw_best\": 0.174,\n      \"en_ece_tempcal_best\": 0.061,\n      \"temp_scaling_T\": 5.34,\n      \"zs_transfer_auroc_mean_19lang_best_transfer_layer\": 0.741,\n      \"zs_best_transfer_layer_idx\": 28,\n      \"zs_transfer_drop_from_en_mean_pp\": 8.0,\n      \"zs_auroc_by_tier\": {\n        \"high_resource_mean\": 0.771,\n        \"mid_resource_mean\": 0.733,\n        \"low_resource_mean\": 0.661\n      },\n      \"zs_auroc_by_lang\": {\n        \"en\": 0.821,\n        \"zh\": 0.784,\n        \"de\": 0.778,\n        \"fr\": 0.775,\n        \"es\": 0.771,\n        \"ja\": 0.766,\n        \"ru\": 0.762,\n        \"pt\": 0.77,\n        \"it\": 0.768,\n        \"ar\": 0.748,\n        \"hi\": 0.741,\n        \"ko\": 0.735,\n        \"vi\": 0.729,\n        \"th\": 0.722,\n        \"bn\": 0.718,\n        \"tr\": 0.737,\n        \"nl\": 0.772,\n        \"sw\": 0.674,\n        \"yo\": 0.641,\n        \"ig\": 0.667\n      },\n      \"mean_shift_improvement_count\": 1,\n      \"linproj_auroc_mean_19lang\": 0.706,\n      \"fewshot_25_auroc_mean_19lang\": 0.728,\n      \"fewshot_100_auroc_mean_19lang\": 0.752,\n      \"pareto_depth_transfer_rank_corr\": 0.82,\n      \"pareto_frontier_layers\": [\n        20,\n        24,\n        28,\n        32\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Llama 4 Scout Pareto Frontier\",\n        \"columns\": [\n          \"layer_idx\",\n          \"layer_depth_pct\",\n          \"en_auroc\",\n          \"zs_mean_auroc_19\",\n          \"zs_drop_pp\",\n          \"on_pareto\"\n        ],\n        \"rows\": [\n          [\n            4,\n            8,\n            0.634,\n            0.624,\n            1.0,\n            false\n          ],\n          [\n            8,\n            17,\n            0.672,\n            0.659,\n            1.3,\n            false\n          ],\n          [\n            12,\n            25,\n            0.714,\n            0.699,\n            1.5,\n            false\n          ],\n          [\n            16,\n            33,\n            0.745,\n            0.729,\n            1.6,\n            false\n          ],\n          [\n            20,\n            42,\n            0.768,\n            0.748,\n            2.0,\n            true\n          ],\n          [\n            24,\n            50,\n            0.786,\n            0.745,\n            4.1,\n            true\n          ],\n          [\n            28,\n            58,\n            0.798,\n            0.741,\n            5.7,\n            true\n          ],\n          [\n            32,\n            67,\n            0.81,\n            0.732,\n            7.8,\n            true\n          ],\n          [\n            36,\n            75,\n            0.821,\n            0.714,\n            10.7,\n            false\n          ],\n          [\n            40,\n            83,\n            0.818,\n            0.689,\n            12.9,\n            false\n          ],\n          [\n            44,\n            92,\n            0.804,\n            0.651,\n            15.3,\n            false\n          ],\n          [\n            48,\n            100,\n            0.771,\n            0.608,\n            16.3,\n            false\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 4: Cross-Architecture Pareto Frontier Agreement\",\n        \"columns\": [\n          \"metric\",\n          \"qwen3_235b\",\n          \"llama4_scout\",\n          \"agreement\"\n        ],\n        \"rows\": [\n          [\n            \"best_en_layer_depth_pct\",\n            77,\n            75,\n            \"within 2pp\"\n          ],\n          [\n            \"best_transfer_layer_depth_pct\",\n            60,\n            58,\n            \"within 2pp\"\n          ],\n          [\n            \"pareto_zone_depth_range_pct\",\n            \"43-64\",\n            \"42-67\",\n            \"overlapping\"\n          ],\n          [\n            \"depth_transfer_rank_corr\",\n            0.88,\n            0.82,\n            \"both >0.75\"\n          ],\n          [\n            \"frontier_shape\",\n            \"convex monotonic\",\n            \"convex monotonic\",\n            \"consistent\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-architecture agreement is high: both models show best transfer at ~59% depth, the Pareto frontier occupies the 42-67% depth band, and the rank correlation between depth and transfer degradation exceeds 0.75 in both. The frontier shape is architecture-invariant — it's the depth-normalized position, not absolute layer count, that determines the tradeoff. This validates Claim 1 at scale.\\n\\n\\nLlama 4 Scout has 48 layers (fewer than Qwen3's 94) and a different MoE routing strategy (16 experts, top-2). With roughly 109B total / ~17B active params, its active compute is smaller than Qwen3-235B's ~22B active. This yields ~2pp lower EN AUROC and ~2pp lower transfer AUROC. The Pareto frontier has fewer points (4 vs 6) due to coarser layer sampling (every 4th of 48 = 12 points), but the monotonic depth-transfer tradeoff still holds clearly. Llama 4 Scout's best transfer layer sits at ~58% depth (L28), remarkably close to Qwen3's 60%, suggesting a universal \\\"mid-depth transfer zone\\\" across architectures. The rank correlation is slightly lower (0.82 vs 0.88) due to fewer data points but still highly significant. Low-resource languages are slightly weaker because Meta's multilingual pretraining mix underrepresents African languages compared to Qwen3.\\n\"\n  },\n  {\n    \"name\": \"CaCLR Implementation and Comparative Evaluation\",\n    \"description\": \"CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) implementation. Train on English labels + unlabeled parallel activations. Compare vs all 5 conditions across full Pareto frontier, both models × 20 languages. Hyperparameter tuning (α, β).\\n\",\n    \"results\": {\n      \"best_alpha\": 0.15,\n      \"best_beta\": 0.08,\n      \"qwen3_caclr_auroc_mean_19lang\": 0.814,\n      \"qwen3_caclr_ece_mean_19lang\": 0.058,\n      \"qwen3_caclr_vs_linproj_auroc_delta_pp\": 3.3,\n      \"qwen3_caclr_vs_zeroshot_auroc_delta_pp\": 5.2,\n      \"qwen3_caclr_ece_reduction_vs_tempcal_pct\": 40.8,\n      \"qwen3_caclr_best_operating_layer\": 64,\n      \"llama4_caclr_auroc_mean_19lang\": 0.793,\n      \"llama4_caclr_ece_mean_19lang\": 0.064,\n      \"llama4_caclr_vs_linproj_auroc_delta_pp\": 3.1,\n      \"llama4_caclr_vs_zeroshot_auroc_delta_pp\": 5.2,\n      \"llama4_caclr_ece_reduction_vs_tempcal_pct\": 38.5,\n      \"llama4_caclr_best_operating_layer\": 32,\n      \"caclr_vs_linproj_auroc_delta_pp_mean\": 3.2,\n      \"caclr_ece_reduction_vs_tempcal_pct_mean\": 39.7,\n      \"caclr_improvement_pass_rate\": 0.92,\n      \"caclr_pareto_shift_layers\": 2,\n      \"low_resource_caclr_auroc\": {\n        \"sw_qwen3\": 0.731,\n        \"yo_qwen3\": 0.709,\n        \"ig_qwen3\": 0.718,\n        \"sw_llama4\": 0.712,\n        \"yo_llama4\": 0.681,\n        \"ig_llama4\": 0.698\n      },\n      \"low_resource_zs_pass_rate\": 1.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: CaCLR vs Baselines — Full Comparison (averaged across both architectures)\",\n        \"columns\": [\n          \"method\",\n          \"auroc_mean_19\",\n          \"ece_mean_19\",\n          \"requires_target_labels\",\n          \"params_overhead\"\n        ],\n        \"rows\": [\n          [\n            \"zero-shot\",\n            0.752,\n            0.098,\n            \"no\",\n            \"0\"\n          ],\n          [\n            \"mean-shift\",\n            0.747,\n            0.102,\n            \"no\",\n            \"0\"\n          ],\n          [\n            \"linear_projection\",\n            0.77,\n            0.082,\n            \"no\",\n            \"d×d matrix\"\n          ],\n          [\n            \"few-shot-25\",\n            0.738,\n            0.089,\n            \"yes (25)\",\n            \"0\"\n          ],\n          [\n            \"few-shot-100\",\n            0.762,\n            0.079,\n            \"yes (100)\",\n            \"0\"\n          ],\n          [\n            \"CaCLR\",\n            0.804,\n            0.061,\n            \"no\",\n            \"~1% probe params\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 6: CaCLR Ablation — Loss Component Contributions\",\n        \"columns\": [\n          \"configuration\",\n          \"auroc_mean_19\",\n          \"ece_mean_19\",\n          \"delta_vs_full_auroc_pp\"\n        ],\n        \"rows\": [\n          [\n            \"L_BCE_only (= zero-shot probe)\",\n            0.752,\n            0.098,\n            -5.2\n          ],\n          [\n            \"L_BCE + L_SB-ECE\",\n            0.768,\n            0.072,\n            -3.6\n          ],\n          [\n            \"L_BCE + L_consistency\",\n            0.793,\n            0.078,\n            -1.1\n          ],\n          [\n            \"L_BCE + L_SB-ECE + L_consistency (full CaCLR)\",\n            0.804,\n            0.061,\n            0.0\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 7: CaCLR Pareto Frontier Shift (Qwen3-235B)\",\n        \"columns\": [\n          \"layer_idx\",\n          \"zs_auroc_19\",\n          \"caclr_auroc_19\",\n          \"shift_pp\",\n          \"on_shifted_pareto\"\n        ],\n        \"rows\": [\n          [\n            40,\n            0.776,\n            0.798,\n            2.2,\n            false\n          ],\n          [\n            44,\n            0.774,\n            0.8,\n            2.6,\n            false\n          ],\n          [\n            48,\n            0.77,\n            0.803,\n            3.3,\n            true\n          ],\n          [\n            52,\n            0.765,\n            0.806,\n            4.1,\n            true\n          ],\n          [\n            56,\n            0.762,\n            0.81,\n            4.8,\n            true\n          ],\n          [\n            60,\n            0.753,\n            0.814,\n            6.1,\n            true\n          ],\n          [\n            64,\n            0.741,\n            0.814,\n            7.3,\n            true\n          ],\n          [\n            68,\n            0.728,\n            0.808,\n            8.0,\n            true\n          ],\n          [\n            72,\n            0.712,\n            0.796,\n            8.4,\n            false\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CaCLR decisively outperforms all baselines. The ablation shows both loss terms contribute: L_consistency provides the bulk of AUROC improvement (+4.1pp alone), while L_SB-ECE provides calibration refinement (ECE drops from 0.078 to 0.061 when added). The interaction is synergistic — joint optimization yields better results than either term alone. The Pareto shift is the headline result: at the same EN calibration quality (L64, AUROC 0.835), CaCLR achieves 0.814 transfer vs 0.741 zero-shot — a 7.3pp improvement. This shifts the practical recommendation from \\\"use shallower layers for transfer\\\" to \\\"use CaCLR and operate at deeper, better-calibrated layers.\\\" The improvement pass rate of 92% (35/38 model-lang pairs) demonstrates consistency. The 3 non-improving pairs are high-resource languages (fr, nl, de on Llama 4 Scout) where zero-shot transfer is already excellent and the consistency loss has minimal signal to exploit.\\n\\n\\nCaCLR's consistency loss (β·L_consistency) directly penalizes divergence between EN and non-EN probe outputs on parallel/comparable activations, forcing the probe to learn language-invariant features. This is strictly more informative than linear projection (which only aligns means and covariances post-hoc) because it shapes the learned representation during training. The 3.2pp AUROC gain over linear projection reflects the value of end-to-end optimization: linear projection corrects first-order distributional mismatch but not the nonlinear feature interactions that L_consistency captures. The SB-ECE term (α·L_SB-ECE) provides calibration-aware training that temperature scaling cannot — it directly optimizes the calibration objective rather than post-hoc rescaling. The 40% ECE reduction over temperature scaling arises because CaCLR addresses the root cause (representation misalignment) rather than the symptom (miscalibrated probabilities). The Pareto frontier shift is the key result: CaCLR allows operating 2 layers deeper than the ZS-optimal point while maintaining equivalent or better transfer — it literally pushes the Pareto frontier outward. Low-resource languages benefit most from L_consistency because their activation distributions are most misaligned from EN; the consistency term provides the strongest gradient signal precisely where the gap is largest.\\n\"\n  },\n  {\n    \"name\": \"Difficulty-Controlled Ablation\",\n    \"description\": \"IRT difficulty probes (Ridge regression), project out difficulty direction, retrain correctness probes on residuals, evaluate transfer. 10 languages × 8 layers per model.\\n\",\n    \"results\": {\n      \"difficulty_probe_r2_mean\": 0.72,\n      \"difficulty_var_explained_pct_mean\": 68.4,\n      \"difficulty_var_explained_pct_range\": [\n        58.2,\n        79.1\n      ],\n      \"residual_en_auroc_drop_pp\": 4.2,\n      \"residual_zs_transfer_drop_pp\": 1.1,\n      \"capability_specific_var_pct\": 31.6,\n      \"capability_specific_transfer_degradation_pct\": 87,\n      \"difficulty_component_transfer_degradation_pct\": 13,\n      \"decomp_prescriptive_accuracy\": 0.81,\n      \"difficulty_var_by_depth\": {\n        \"shallow_20pct\": 0.74,\n        \"mid_50pct\": 0.69,\n        \"deep_80pct\": 0.62\n      },\n      \"capability_transfer_drop_by_depth\": {\n        \"shallow_20pct\": 0.8,\n        \"mid_50pct\": 3.4,\n        \"deep_80pct\": 9.7\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Decomposition Results — Difficulty vs Capability Components\",\n        \"columns\": [\n          \"component\",\n          \"var_explained_pct\",\n          \"transfer_auroc_mean\",\n          \"transfer_drop_from_en_pp\",\n          \"share_of_total_transfer_drop_pct\"\n        ],\n        \"rows\": [\n          [\n            \"full_correctness\",\n            100,\n            0.752,\n            8.1,\n            100\n          ],\n          [\n            \"difficulty_shared\",\n            68.4,\n            0.738,\n            1.1,\n            13\n          ],\n          [\n            \"capability_specific\",\n            31.6,\n            0.614,\n            14.2,\n            87\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 9: Capability-Specific Transfer Drop by Depth\",\n        \"columns\": [\n          \"depth_band\",\n          \"difficulty_transfer_drop_pp\",\n          \"capability_transfer_drop_pp\",\n          \"ratio\"\n        ],\n        \"rows\": [\n          [\n            \"0-30%\",\n            0.3,\n            0.8,\n            \"2.7×\"\n          ],\n          [\n            \"30-60%\",\n            0.8,\n            3.4,\n            \"4.3×\"\n          ],\n          [\n            \"60-90%\",\n            1.6,\n            9.7,\n            \"6.1×\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The decomposition cleanly separates: difficulty-shared signal is the majority (68%) of correctness variance and transfers near-perfectly across languages and depths. The capability-specific residual (32%) drives nearly all transfer degradation (87%), and this degradation accelerates exponentially with depth. This explains the Pareto frontier mechanistically: deeper layers have stronger capability-specific signals that improve EN calibration but impede transfer. CaCLR works because its consistency loss specifically targets the capability-specific component — forcing alignment of the non-difficulty residual across languages. The prescriptive value (81% accuracy in predicting when CaCLR is needed) confirms this is a load-bearing decomposition, not a post-hoc narrative.\\n\\n\\nIRT difficulty is a strong, language-agnostic property — harder questions are harder everywhere. Ridge regression captures this cleanly (R²=0.72) because difficulty is linearly encoded in intermediate representations (Civelli et al. confirmed this). The difficulty component accounts for 68% of explained variance because GlobalMMLU correctness is heavily driven by item difficulty: a model gets easy questions right in all languages and hard questions wrong in all languages. After projecting out difficulty, the residual correctness signal is \\\"capability-specific\\\" — it captures language-dependent competence differences. This residual transfers poorly at deep layers (9.7pp drop at 80% depth vs 0.8pp at 20% depth) because deep layers encode language-specific processing that makes capability assessments non-transferable. The difficulty component transfers well at all depths (only 13% of total transfer degradation) because it's language-invariant by construction. This decomposition is prescriptive: when difficulty explains most of a language's correctness variance, simple zero-shot transfer suffices; when the capability residual is large, CaCLR is needed. The 81% prescriptive accuracy validates the decomposition as more than descriptive.\\n\"\n  },\n  {\n    \"name\": \"Cross-Lingual Orthogonality Analysis\",\n    \"description\": \"Extract verbalized confidence direction via prompted confidence scores, compute cosine similarity with correctness direction across 20 languages × 2 architectures. Analyze by resource tier and language family.\\n\",\n    \"results\": {\n      \"orthogonality_cosine_mean_overall\": 0.052,\n      \"orthogonality_cosine_range\": [\n        0.018,\n        0.094\n      ],\n      \"orthogonality_cosine_en\": 0.034,\n      \"qwen3_cosine_mean\": 0.048,\n      \"llama4_cosine_mean\": 0.057,\n      \"high_resource_cosine_mean\": 0.041,\n      \"mid_resource_cosine_mean\": 0.054,\n      \"low_resource_cosine_mean\": 0.074,\n      \"cosine_by_lang\": {\n        \"en\": 0.034,\n        \"zh\": 0.038,\n        \"de\": 0.036,\n        \"fr\": 0.039,\n        \"es\": 0.041,\n        \"ja\": 0.044,\n        \"ru\": 0.043,\n        \"pt\": 0.04,\n        \"it\": 0.042,\n        \"ar\": 0.051,\n        \"hi\": 0.055,\n        \"ko\": 0.049,\n        \"vi\": 0.058,\n        \"th\": 0.061,\n        \"bn\": 0.056,\n        \"tr\": 0.052,\n        \"nl\": 0.037,\n        \"sw\": 0.078,\n        \"yo\": 0.094,\n        \"ig\": 0.082\n      },\n      \"all_langs_below_0p1\": true,\n      \"cosine_resource_tier_correlation\": -0.68\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Correctness-Confidence Cosine Similarity by Language and Architecture\",\n        \"columns\": [\n          \"language\",\n          \"resource_tier\",\n          \"qwen3_cosine\",\n          \"llama4_cosine\",\n          \"mean_cosine\"\n        ],\n        \"rows\": [\n          [\n            \"en\",\n            \"high\",\n            0.031,\n            0.037,\n            0.034\n          ],\n          [\n            \"zh\",\n            \"high\",\n            0.035,\n            0.041,\n            0.038\n          ],\n          [\n            \"de\",\n            \"high\",\n            0.033,\n            0.039,\n            0.036\n          ],\n          [\n            \"fr\",\n            \"high\",\n            0.036,\n            0.042,\n            0.039\n          ],\n          [\n            \"es\",\n            \"high\",\n            0.038,\n            0.044,\n            0.041\n          ],\n          [\n            \"ja\",\n            \"high\",\n            0.041,\n            0.047,\n            0.044\n          ],\n          [\n            \"ru\",\n            \"high\",\n            0.04,\n            0.046,\n            0.043\n          ],\n          [\n            \"pt\",\n            \"high\",\n            0.037,\n            0.043,\n            0.04\n          ],\n          [\n            \"it\",\n            \"high\",\n            0.039,\n            0.045,\n            0.042\n          ],\n          [\n            \"nl\",\n            \"high\",\n            0.034,\n            0.04,\n            0.037\n          ],\n          [\n            \"ar\",\n            \"mid\",\n            0.047,\n            0.055,\n            0.051\n          ],\n          [\n            \"hi\",\n            \"mid\",\n            0.051,\n            0.059,\n            0.055\n          ],\n          [\n            \"ko\",\n            \"mid\",\n            0.045,\n            0.053,\n            0.049\n          ],\n          [\n            \"vi\",\n            \"mid\",\n            0.054,\n            0.062,\n            0.058\n          ],\n          [\n            \"th\",\n            \"mid\",\n            0.057,\n            0.065,\n            0.061\n          ],\n          [\n            \"bn\",\n            \"mid\",\n            0.052,\n            0.06,\n            0.056\n          ],\n          [\n            \"tr\",\n            \"mid\",\n            0.048,\n            0.056,\n            0.052\n          ],\n          [\n            \"sw\",\n            \"low\",\n            0.073,\n            0.083,\n            0.078\n          ],\n          [\n            \"yo\",\n            \"low\",\n            0.089,\n            0.099,\n            0.094\n          ],\n          [\n            \"ig\",\n            \"low\",\n            0.077,\n            0.087,\n            0.082\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 11: Orthogonality Summary Statistics\",\n        \"columns\": [\n          \"statistic\",\n          \"qwen3_235b\",\n          \"llama4_scout\",\n          \"both_models\"\n        ],\n        \"rows\": [\n          [\n            \"cosine_mean\",\n            0.048,\n            0.057,\n            0.052\n          ],\n          [\n            \"cosine_std\",\n            0.015,\n            0.017,\n            0.016\n          ],\n          [\n            \"cosine_max\",\n            0.089,\n            0.099,\n            0.094\n          ],\n          [\n            \"cosine_min\",\n            0.031,\n            0.037,\n            0.018\n          ],\n          [\n            \"all_below_0.1\",\n            \"yes (20/20)\",\n            \"yes (19/20)\",\n            \"39/40\"\n          ],\n          [\n            \"resource_tier_corr\",\n            -0.71,\n            -0.65,\n            -0.68\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Orthogonality generalizes comprehensively. The mean cosine of 0.052 across all 40 language-architecture pairs is well within the \\\"near-orthogonal\\\" regime (< 0.1). The resource-tier gradient is the novel finding: it suggests that output-based calibration methods are not just structurally limited but are *more* limited for well-resourced languages where the orthogonality is strongest. This strengthens the motivation for probe-based approaches universally and for CaCLR specifically in multilingual settings. Yoruba's 0.094 is the only value approaching the 0.1 threshold (on Llama4 it hits 0.099), which is worth noting but does not break the claim.\\n\\n\\nMiao & Ungar (2026) established correctness-confidence orthogonality (cosine < 0.04) for English on 7-8B models. We extend to 20 languages on larger models. The orthogonality persists universally (all < 0.1) because it reflects a fundamental architectural property: verbalized confidence is generated by the language modeling head from surface-level token probabilities, while correctness is encoded in intermediate representation geometry. These are structurally decoupled in transformer architectures. The slight increase in cosine for low-resource languages (0.074 mean vs 0.041 for high-resource) occurs because low-resource languages have noisier confidence elicitation — the model's verbalized confidence in Yoruba is less well-calibrated and leaks some correctness signal, producing weak correlation. The resource-tier gradient (ρ=-0.68) suggests that better multilingual training data produces cleaner separation between correctness and confidence representations. The cross-architecture consistency (Qwen3: 0.048, Llama4: 0.057) confirms this is not architecture-specific. Llama 4's slightly higher cosines may reflect its less aggressive multilingual pretraining compared to Qwen3.\\n\"\n  },\n  {\n    \"name\": \"Probe Complexity Comparison\",\n    \"description\": \"Logistic regression vs 2-layer MLP at each probed layer, both models. Compare English accuracy, cross-lingual transfer degradation, calibration quality.\\n\",\n    \"results\": {\n      \"logreg_en_auroc_best\": 0.843,\n      \"mlp_en_auroc_best\": 0.856,\n      \"mlp_en_auroc_gain_pp\": 1.3,\n      \"logreg_zs_transfer_drop_mean_pp\": 8.1,\n      \"mlp_zs_transfer_drop_mean_pp\": 12.4,\n      \"transfer_degradation_ratio\": 1.53,\n      \"logreg_ece_mean\": 0.054,\n      \"mlp_ece_mean\": 0.068,\n      \"logreg_transfer_advantage_shallow_pp\": 2.1,\n      \"logreg_transfer_advantage_deep_pp\": 6.8\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 12: Probe Complexity Comparison\",\n        \"columns\": [\n          \"probe_type\",\n          \"en_auroc_best\",\n          \"zs_auroc_mean_19\",\n          \"zs_drop_pp\",\n          \"ece_mean_19\"\n        ],\n        \"rows\": [\n          [\n            \"logistic_regression\",\n            0.843,\n            0.762,\n            8.1,\n            0.054\n          ],\n          [\n            \"mlp_2layer\",\n            0.856,\n            0.733,\n            12.4,\n            0.068\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Linear probes are the correct choice for cross-lingual transfer: they sacrifice 1.3pp EN AUROC but gain 4.3pp average transfer. The depth interaction effect is notable — the logreg advantage grows from 2.1pp at shallow layers to 6.8pp at deep layers, confirming that deep-layer transfer degradation is driven by nonlinear, language- specific features. CaCLR + logreg is thus the optimal configuration.\\n\\n\\nLinear probes transfer better because they learn a single hyperplane in activation space — the hyperplane generalizes across languages when the underlying geometry is approximately shared (as it is in mid-depth layers). MLPs learn nonlinear decision boundaries that fit English-specific feature interactions, gaining ~1.3pp EN AUROC but losing ~4.3pp in transfer. The transfer gap widens at deeper layers (6.8pp advantage for logreg) because deep layers have more language-specific nonlinear structure that MLPs exploit but logreg ignores. This justifies our choice of linear probes for the main results and supports the geometric interpretation of the Pareto frontier: it's about linear subspace alignment, not complex feature interactions.\\n\"\n  },\n  {\n    \"name\": \"Additional Benchmark Evaluation (Belebele + MMLU-ProX)\",\n    \"description\": \"Evaluate best probes + CaCLR on Belebele (20 languages) and MMLU-ProX (20 languages).\\n\",\n    \"results\": {\n      \"belebele_zs_auroc_mean_19\": 0.738,\n      \"belebele_caclr_auroc_mean_19\": 0.789,\n      \"belebele_caclr_vs_zs_pp\": 5.1,\n      \"belebele_ece_reduction_vs_tempcal_pct\": 36.2,\n      \"mmlupx_zs_auroc_mean_19\": 0.722,\n      \"mmlupx_caclr_auroc_mean_19\": 0.774,\n      \"mmlupx_caclr_vs_zs_pp\": 5.2,\n      \"mmlupx_ece_reduction_vs_tempcal_pct\": 33.8,\n      \"caclr_benefit_cross_benchmark_cv\": 0.08\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: Cross-Benchmark Generalization\",\n        \"columns\": [\n          \"benchmark\",\n          \"zs_auroc_mean_19\",\n          \"caclr_auroc_mean_19\",\n          \"caclr_gain_pp\",\n          \"ece_reduction_pct\"\n        ],\n        \"rows\": [\n          [\n            \"GlobalMMLU\",\n            0.752,\n            0.804,\n            5.2,\n            39.7\n          ],\n          [\n            \"Belebele\",\n            0.738,\n            0.789,\n            5.1,\n            36.2\n          ],\n          [\n            \"MMLU-ProX\",\n            0.722,\n            0.774,\n            5.2,\n            33.8\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CaCLR generalizes cleanly across benchmarks. The improvement magnitude is remarkably stable (5.1-5.2pp AUROC, 33-40% ECE reduction), suggesting the method addresses a fundamental representation alignment issue rather than overfitting to GlobalMMLU- specific patterns. This is critical for reviewer confidence.\\n\\n\\nBelebele tests reading comprehension (vs GlobalMMLU's factual knowledge), providing domain generalization evidence. Transfer AUROC is slightly lower (0.738 vs 0.762) because Belebele's passage-dependent questions have weaker difficulty-shared signal — comprehension difficulty is more language-dependent than factual difficulty. CaCLR still provides ~5pp improvement, confirming the consistency loss generalizes beyond factual MCQA. MMLU-ProX has harder questions that compress the AUROC distribution (lower base rate of correctness), yielding slightly lower absolute numbers but comparable CaCLR benefit. The cross-benchmark CV of 0.08 for CaCLR improvement confirms the method is robust to evaluation domain.\\n\"\n  },\n  {\n    \"name\": \"INT8 Validation Ablation\",\n    \"description\": \"Compare INT8 vs FP16 probing results at 5 representative layers for Llama 4 Scout on 5% random subset.\\n\",\n    \"results\": {\n      \"int8_fp16_auroc_diff_mean_pp\": 0.3,\n      \"int8_fp16_auroc_diff_max_pp\": 0.7,\n      \"int8_fp16_ece_diff_mean_pp\": 0.2,\n      \"int8_fp16_transfer_drop_diff_pp\": 0.4,\n      \"int8_fp16_rank_correlation\": 0.997,\n      \"conclusion\": \"INT8 quantization introduces negligible distortion\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S1: INT8 vs FP16 Comparison (Llama 4 Scout, 5% subset)\",\n        \"columns\": [\n          \"layer_idx\",\n          \"fp16_auroc\",\n          \"int8_auroc\",\n          \"diff_pp\",\n          \"fp16_zs_auroc_5lang\",\n          \"int8_zs_auroc_5lang\",\n          \"transfer_diff_pp\"\n        ],\n        \"rows\": [\n          [\n            8,\n            0.674,\n            0.672,\n            0.2,\n            0.661,\n            0.658,\n            0.3\n          ],\n          [\n            16,\n            0.747,\n            0.745,\n            0.2,\n            0.731,\n            0.728,\n            0.3\n          ],\n          [\n            24,\n            0.788,\n            0.786,\n            0.2,\n            0.747,\n            0.744,\n            0.3\n          ],\n          [\n            32,\n            0.812,\n            0.81,\n            0.2,\n            0.734,\n            0.731,\n            0.3\n          ],\n          [\n            40,\n            0.82,\n            0.817,\n            0.3,\n            0.691,\n            0.687,\n            0.4\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"INT8 quantization is validated as safe for our experimental setup. The maximum observed difference (0.7pp at a single layer-language combination) is well within the noise floor of probing experiments. The Pareto frontier ordering is perfectly preserved (rank correlation 0.997). This ablation preempts reviewer concern #5.\\n\\n\\nINT8 weight-only quantization preserves the 8 most significant bits of each weight, introducing per-channel quantization noise of ~0.4% relative magnitude. Correctness probing relies on the geometry of activation space (direction of correctness signal), not absolute magnitudes. The quantization noise is approximately isotropic and thus preserves angular relationships between directions. The 0.3pp mean AUROC difference is within random seed variance, and the rank correlation of 0.997 between INT8 and FP16 layer rankings confirms that the Pareto frontier shape is unaffected. This result is expected given prior work showing that probing results are robust to quantization down to INT4 (Gao et al., 2024).\\n\"\n  },\n  {\n    \"name\": \"Gemma 4 31B Dense — Third Architecture (Camera-Ready)\",\n    \"description\": \"Full Pareto frontier on Gemma 4 31B Dense (60 layers), 20+ languages. Provides dense vs MoE architectural contrast.\\n\",\n    \"results\": {\n      \"en_auroc_best_layer\": 0.812,\n      \"en_best_layer_idx\": 45,\n      \"zs_transfer_auroc_mean_19lang\": 0.734,\n      \"zs_best_transfer_layer_idx\": 36,\n      \"zs_transfer_drop_mean_pp\": 7.8,\n      \"pareto_depth_transfer_rank_corr\": 0.86,\n      \"caclr_auroc_mean_19lang\": 0.786,\n      \"caclr_vs_linproj_auroc_delta_pp\": 2.9,\n      \"dense_vs_moe_transfer_comparison\": \"comparable within 2pp\",\n      \"pareto_shape\": \"convex monotonic, consistent with MoE models\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 14: Three-Architecture Summary\",\n        \"columns\": [\n          \"model\",\n          \"type\",\n          \"layers\",\n          \"en_auroc_best\",\n          \"zs_auroc_mean_19\",\n          \"best_transfer_depth_pct\",\n          \"pareto_rank_corr\",\n          \"caclr_gain_pp\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-235B-A22B\",\n            \"MoE\",\n            94,\n            0.843,\n            0.762,\n            60,\n            0.88,\n            3.3\n          ],\n          [\n            \"Llama 4 Scout\",\n            \"MoE\",\n            48,\n            0.821,\n            0.741,\n            58,\n            0.82,\n            3.1\n          ],\n          [\n            \"Gemma 4 31B Dense\",\n            \"Dense\",\n            60,\n            0.812,\n            0.734,\n            60,\n            0.86,\n            2.9\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The three-architecture comparison is the strongest evidence for the universality of the depth-transferability tradeoff. The best-transfer depth converges to 58-60% across dense and MoE architectures with 48-94 layers, CaCLR provides consistent 2.9-3.3pp improvement, and the Pareto rank correlation is 0.82-0.88 in all cases. Dense vs MoE makes minimal difference — the phenomenon is a property of transformer depth, not routing architecture.\\n\\n\\nGemma 4 31B Dense has fewer total parameters than the MoE models but all are active, yielding comparable per-token compute. As a dense model, its representations are more uniformly distributed across layers (no expert routing), producing slightly smoother Pareto frontiers. The best-transfer depth (~60%) matches both MoE models, confirming this is a universal property of transformer depth, not MoE-specific. EN AUROC is slightly lower (0.812 vs 0.843/0.821) because 31B active params < 22B active with MoE routing benefits. CaCLR improvement is slightly lower (2.9pp) on the dense model because the absence of expert routing means less language-specific feature fragmentation to correct. This is the ideal third data point: different architecture family, consistent findings.\\n\"\n  },\n  {\n    \"name\": \"Extended Language Coverage (Camera-Ready)\",\n    \"description\": \"Expand from 20 to 50+ languages for camera-ready, leveraging GlobalMMLU/Belebele full language sets.\\n\",\n    \"results\": {\n      \"total_languages\": 52,\n      \"new_languages_added\": 32,\n      \"zs_auroc_above_0p60_count\": 48,\n      \"zs_auroc_below_0p55_count\": 2,\n      \"caclr_improvement_positive_count\": 49,\n      \"mean_zs_auroc_51lang\": 0.72,\n      \"mean_caclr_auroc_51lang\": 0.77,\n      \"pareto_frontier_holds_all_langs\": true,\n      \"new_language_families_covered\": [\n        \"Austronesian\",\n        \"Dravidian\",\n        \"Niger-Congo B\",\n        \"Uralic\",\n        \"Kartvelian\"\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 15: Extended Language Coverage Summary by Resource Tier\",\n        \"columns\": [\n          \"tier\",\n          \"n_langs\",\n          \"zs_auroc_mean\",\n          \"caclr_auroc_mean\",\n          \"caclr_gain_pp\",\n          \"pct_above_0p60\"\n        ],\n        \"rows\": [\n          [\n            \"high\",\n            12,\n            0.782,\n            0.812,\n            3.0,\n            100\n          ],\n          [\n            \"mid\",\n            25,\n            0.738,\n            0.784,\n            4.6,\n            100\n          ],\n          [\n            \"low\",\n            10,\n            0.661,\n            0.712,\n            5.1,\n            90\n          ],\n          [\n            \"very_low\",\n            4,\n            0.582,\n            0.638,\n            5.6,\n            50\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The extension to 52 languages confirms all findings at broader scale. The resource-tier gradient is smooth and predictable — no language family shows anomalous behavior. CaCLR's benefit is inversely correlated with resource level (3.0pp for high-resource to 5.6pp for very-low-resource), confirming that the consistency loss provides most value where representation misalignment is worst. The 48/51 pass rate (>0.60 AUROC) for zero-shot CaCLR transfer with no target-language labels is the practical headline for camera-ready: usable cross-lingual calibration for the vast majority of languages.\\n\\nExpanding to 50+ languages primarily adds mid-resource languages (Indonesian, Malay, Finnish, Georgian, Tamil, Telugu, etc.) where the model has moderate pretraining exposure. Most new languages fall in the 0.65-0.78 AUROC range, consistent with the mid-resource tier from the 20-language set. A handful of extremely low-resource languages (e.g., Amharic script languages with minimal pretraining data) may fall below 0.55, but these represent edge cases rather than systematic failures. CaCLR continues to improve 96% of languages because the consistency loss mechanism is language-agnostic — it aligns activation distributions without requiring any language-specific knowledge. The Pareto frontier structure is preserved across all 52 languages, confirming it's a depth property, not a language-set artifact.\\n\"\n  }\n]",
      "numLines": 1375,
      "startLine": 1,
      "totalLines": 1375
    }
  },
  "sourceToolAssistantUUID": "bbc758a5-91f3-4b5d-b4b1-dd90569ab86a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T19:23:25.139Z_

<details><summary>↩ Tool result · `toolu_0175VqenJQ6bmmaFmhBRKaZ1`</summary>

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
22	### Claim 3 — CaCLR (Method)
23	CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) shifts the Pareto frontier by jointly optimizing calibration and cross-lingual invariance, enabling effective probe transfer at deeper, better-calibrated layers without target-language correctness labels.
24	- MVP evidence: Mean-shift fails entirely (0/5 languages improved) — motivates principled approach.
25	- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier.
26	
27	### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)
28	The correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.
29	- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.
30	
31	## Story Spine
32	- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).
33	- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.
34	- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, and propose CaCLR to shift the frontier. This is both a field-level viability test and a practical method contribution.
35	- **Headline template**: "On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels."
36	
37	## Field-Level Significance
38	This paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.
39	
40	## Anticipated Reviewer Concerns & Responses
41	1. **"Xiao et al. already did this"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier.
42	2. **"Temperature scaling baseline"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.
43	3. **"Mean-shift too weak"** → 5 transfer conditions tested. Mean-shift failure (MVP-confirmed) motivates CaCLR. Mean-shift works for Xiao et al.'s knowledge boundary but fails for correctness — important finding.
44	4. **"Difficulty confound"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.
45	5. **"INT8 artifacts"** → Validation ablation comparing INT8 vs FP16 at representative layers.
46	6. **"Only MCQA"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.
47	
48	## Differentiation from Closest Prior Work
49	| Paper | Their Focus | Our Difference |
50	|-------|-------------|----------------|
51	| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier |
52	| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |
53	| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |
54	| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |
55	| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |
56	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4197565b-2cae-410d-9ff7-69bcde3fce0a",
  "isSidechain": false,
  "promptId": "907ecca9-b4a5-4dd2-af0b-6dcee3e5aad0",
  "type": "user",
  "uuid": "abe03133-b53a-4463-a28c-4572fdb04ec3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper_framing.md",
      "content": "# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — transfers cross-lingually through intermediate layers, but with a depth-transferability Pareto tradeoff: deeper layers yield better English calibration while shallower layers transfer better. This tradeoff is architecture-dependent and can be shifted by CaCLR, a probe training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without requiring target-language correctness labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth is architecture-dependent.\n- MVP evidence: L27 AUROC=0.754 (EN best) but transfer drops 2-4pp vs L24 on Qwen2.5-7B.\n- Full evidence: 2 architectures × 20 languages × all layers × 5 transfer conditions.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) shifts the Pareto frontier by jointly optimizing calibration and cross-lingual invariance, enabling effective probe transfer at deeper, better-calibrated layers without target-language correctness labels.\n- MVP evidence: Mean-shift fails entirely (0/5 languages improved) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier.\n\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, and propose CaCLR to shift the frontier. This is both a field-level viability test and a practical method contribution.\n- **Headline template**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak\"** → 5 transfer conditions tested. Mean-shift failure (MVP-confirmed) motivates CaCLR. Mean-shift works for Xiao et al.'s knowledge boundary but fails for correctness — important finding.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n",
      "numLines": 56,
      "startLine": 1,
      "totalLines": 56
    }
  },
  "sourceToolAssistantUUID": "4197565b-2cae-410d-9ff7-69bcde3fce0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T19:23:25.129Z_

<details open><summary>🔧 Tool call — Read · `toolu_0175VqenJQ6bmmaFmhBRKaZ1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a87d5e0-5937-4a17-bf39-e45a06d58e68",
  "isSidechain": false,
  "requestId": "req_011CbENCoLLtHzQp3tNu1igi",
  "type": "assistant",
  "uuid": "4197565b-2cae-410d-9ff7-69bcde3fce0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014FXxE7P9kh3hpEhHdrmmq1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11424,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11424
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T185641 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direct…",
  "leafUuid": "abe03133-b53a-4463-a28c-4572fdb04ec3",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete research paper for dream session",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75"
}
```

---

### Assistant

_source line 14 · 2026-05-20T19:23:37.562Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the experiment data and paper framing. Let me also load the research and writing skills to inform the paper quality.

Actually, I have enough context. Let me write the full LaTeX paper now. I need to:

1. Cover all 8 experiments with corresponding sections/tables
2. Follow the narrative guidance: CaCLR shifts the Pareto frontier, 4 claims form a causal chain
3. All numbers from experiment_data.json, no fabrication
4. Quality: "够审" level - reviewable but not submission quality

Let me structure the paper:
- Abstract
- Introduction (problem, gaps, contributions)


- Related Work
- Method (Pareto frontier analysis, decomposition, CaCLR)
- Experiments section covering the full pipeline: starting with the Pareto frontier analysis on Qwen3-235B, then cross-architecture validation with Llama 4 Scout, the core CaCLR results, difficulty decomposition analysis, orthogonality studies, probe complexity investigation, and cross-benchmark evaluation.
- Additional experiments examining three-architecture comparisons, extended language support, and INT8 quantization validation in the appendix
- Conclusion
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abe03133-b53a-4463-a28c-4572fdb04ec3",
  "isSidechain": false,
  "requestId": "req_011CbEND5GoFRnS8Hpr8LuDW",
  "type": "assistant",
  "uuid": "6461a537-adfa-49ab-b40d-a7172d32915c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ivWUQtfwMTtHxEq2hK84N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18701,
      "cache_read_input_tokens": 23265,
      "output_tokens": 602,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18701,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 602,
          "cache_read_input_tokens": 23265,
          "cache_creation_input_tokens": 18701,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18701
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

_source line 15 · 2026-05-20T19:23:37.562Z_

Now let me check if the output directory exists and if pdflatex is available.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6461a537-adfa-49ab-b40d-a7172d32915c",
  "isSidechain": false,
  "requestId": "req_011CbEND5GoFRnS8Hpr8LuDW",
  "type": "assistant",
  "uuid": "634d062e-30da-4163-a729-5a5e057346a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ivWUQtfwMTtHxEq2hK84N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18701,
      "cache_read_input_tokens": 23265,
      "output_tokens": 602,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18701,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 602,
          "cache_read_input_tokens": 23265,
          "cache_creation_input_tokens": 18701,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18701
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

_source line 16 · 2026-05-20T19:23:39.185Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FaKwkWih6BJxx476Gs6vZJ`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/ && which pdflatex",
  "description": "Check output directory and pdflatex availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "634d062e-30da-4163-a729-5a5e057346a8",
  "isSidechain": false,
  "requestId": "req_011CbEND5GoFRnS8Hpr8LuDW",
  "type": "assistant",
  "uuid": "ecbd0e09-104a-4d4e-9b0e-f82812a50cc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ivWUQtfwMTtHxEq2hK84N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18701,
      "cache_read_input_tokens": 23265,
      "output_tokens": 602,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18701,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 602,
          "cache_read_input_tokens": 23265,
          "cache_creation_input_tokens": 18701,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18701
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

_source line 17 · 2026-05-20T19:23:39.340Z_

<details><summary>↩ Tool result · `toolu_01FaKwkWih6BJxx476Gs6vZJ`</summary>

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
  "parentUuid": "ecbd0e09-104a-4d4e-9b0e-f82812a50cc0",
  "isSidechain": false,
  "promptId": "907ecca9-b4a5-4dd2-af0b-6dcee3e5aad0",
  "type": "user",
  "uuid": "6537f3b0-2819-43cb-9275-d47062d89d73",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md\n/usr/bin/pdflatex",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "ecbd0e09-104a-4d4e-9b0e-f82812a50cc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-20T19:23:41.967Z_

Writing the full LaTeX paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6537f3b0-2819-43cb-9275-d47062d89d73",
  "isSidechain": false,
  "requestId": "req_011CbENE7mPhvqAUrDH3FB4L",
  "type": "assistant",
  "uuid": "2fff56ec-057b-417b-9200-608429a299f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JrQgYCfpKV1pMAcp7h5QVj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 641,
      "cache_read_input_tokens": 41966,
      "output_tokens": 12041,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 641,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12041,
          "cache_read_input_tokens": 41966,
          "cache_creation_input_tokens": 641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 641
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

_source line 19 · 2026-05-20T19:26:59.484Z_

<details open><summary>🔧 Tool call — Write · `toolu_01HwuSAwDfWUf9QGnXZtuBoW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{microtype}\n\\usepackage{array}\n\n\\newcommand{\\caclr}{\\textsc{CaCLR}}\n\\newcommand{\\ece}{\\text{ECE}}\n\\newcommand{\\auroc}{\\text{AUROC}}\n\n\\title{Shifting the Cross-Lingual Calibration Pareto Frontier:\\\\Probe-Based Calibration Transfer via CaCLR}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nNon-English languages suffer substantially worse calibration in multilingual LLMs, yet existing probe-based calibration methods operate exclusively in English.\nWe present the first systematic study of cross-lingual correctness probe transfer for calibration across 20 languages and three architectures (Qwen3-235B-A22B, Llama~4~Scout, Gemma~4~31B Dense).\nWe discover a \\emph{depth-transferability Pareto frontier}: deeper layers yield better English calibration but degrade cross-lingual zero-shot transfer, with the optimal transfer depth converging to $\\sim$58--60\\% of model depth across architectures.\nWe decompose correctness probe signal into a \\emph{difficulty-shared} component (68\\% of variance, language-agnostic, transfers at all depths) and a \\emph{capability-specific} component (32\\%, language-dependent, drives 87\\% of transfer degradation).\nWe propose \\caclr{} (\\textbf{Ca}libration-aware \\textbf{C}ross-\\textbf{L}ingual \\textbf{R}egularization), a training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without target-language labels.\n\\caclr{} shifts the Pareto frontier outward: averaged across architectures, it improves non-English AUROC by 5.2pp over zero-shot transfer and reduces ECE by $\\sim$40\\% relative to temperature scaling, with zero target-language correctness labels.\nWe further show that correctness--confidence orthogonality (cosine $<0.1$) persists across all 20 languages in both architectures, establishing output-based calibration as structurally limited regardless of language.\nResults generalize to 52 languages and two additional benchmarks (Belebele, MMLU-ProX).\n\\end{abstract}\n\n%------------------------------------------------------------------\n\\section{Introduction}\n\\label{sec:intro}\n%------------------------------------------------------------------\n\nCalibration---the alignment between a model's expressed confidence and its actual accuracy---is critical for safe deployment of large language models (LLMs). While recent work has made substantial progress on English calibration through internal representation probing \\cite{burns2023discovering,marks2024geometry,miao2026coral}, non-English languages remain poorly served: they suffer up to 5$\\times$ worse expected calibration error (ECE) under standard output-based methods.\n\nThis gap is not merely quantitative. Miao \\& Ungar (2026) demonstrated that the correctness direction in LLM activation space is \\emph{orthogonal} to the verbalized confidence direction, implying that output-based calibration methods are structurally limited. However, their analysis---and indeed all probe-based calibration work---is restricted to English. Whether this entire research line extends to multilingual settings is an open question with field-level implications.\n\nWe address this question systematically. Our investigation reveals four findings that form an unbroken causal chain:\n\n\\paragraph{Claim 1: Pareto Frontier (Discovery).}\nCross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth converges to $\\sim$58--60\\% of model depth across three architectures (Qwen3-235B-A22B, Llama~4~Scout, Gemma~4~31B Dense), with Spearman rank correlations between depth and transfer degradation of $\\rho=0.82$--$0.88$ ($p<0.001$).\n\n\\paragraph{Claim 2: Decomposition (Analysis).}\nCross-lingual transfer decomposes into a \\emph{difficulty-shared} component (68\\% of correctness variance; language-agnostic; transfers at all depths) and a \\emph{capability-specific} component (32\\%; language-dependent; accounts for 87\\% of transfer degradation). This decomposition is prescriptive: it predicts with 81\\% accuracy when alignment intervention is needed.\n\n\\paragraph{Claim 3: CaCLR (Method).}\nWe propose \\caclr{}, a probe training objective ($\\mathcal{L}_\\text{BCE} + \\alpha \\cdot \\mathcal{L}_\\text{SB-ECE} + \\beta \\cdot \\mathcal{L}_\\text{consistency}$) that shifts the Pareto frontier outward by jointly optimizing calibration and cross-lingual invariance. Averaged across both architectures, \\caclr{} improves non-English AUROC by 5.2pp over zero-shot transfer and reduces ECE by $\\sim$40\\% relative to temperature scaling, requiring zero target-language correctness labels.\n\n\\paragraph{Claim 4: Cross-Lingual Orthogonality (Mechanistic).}\nThe correctness--confidence orthogonality persists across all 20 languages (mean cosine similarity = 0.052, all $<$ 0.1), with a resource-tier gradient ($\\rho=-0.68$): better-resourced languages show stronger orthogonality. This establishes output-based calibration as fundamentally limited regardless of language.\n\nTogether, these claims position \\caclr{} as the first method to provide effective probe-based cross-lingual calibration without target-language labels, shifting the Pareto frontier that constrains all prior approaches.\n\n%------------------------------------------------------------------\n\\section{Related Work}\n\\label{sec:related}\n%------------------------------------------------------------------\n\n\\paragraph{Probe-Based Calibration.}\nBurns et al.\\ (2023) and Marks et al.\\ (2024) showed that linear probes on intermediate activations can recover correctness signals. Miao et al.\\ (2026a; CORAL) demonstrated cross-task transfer of such probes. Miao \\& Ungar (2026b) established the orthogonality of correctness and verbalized confidence directions. All of this work is English-only.\n\n\\paragraph{Cross-Lingual Representation Transfer.}\nXiao et al.\\ (ACL 2025) transferred \\emph{knowledge-boundary} probes (input-level answerability, not output-dependent correctness) across 8 languages, measuring probing accuracy rather than calibration. Civelli et al.\\ transferred difficulty probes cross-lingually, finding language-agnostic difficulty encoding---a result we leverage as a control in our decomposition (Claim~2).\n\n\\paragraph{Multilingual Calibration.}\nLACE (Zhou et al.) uses per-language layer ensembles but requires target-language labels. MKA employs multi-key attention at 5$\\times$ inference cost. Temperature scaling is the standard output-based baseline. None addresses representation-level cross-lingual calibration transfer.\n\n%------------------------------------------------------------------\n\\section{Method}\n\\label{sec:method}\n%------------------------------------------------------------------\n\n\\subsection{Correctness Probing and Transfer}\n\\label{sec:probing}\n\nGiven a multilingual LLM with $L$ layers, we extract activations $\\mathbf{h}_l^{(i)}$ at layer $l$ for input $i$. A logistic regression probe $f_l(\\mathbf{h}) = \\sigma(\\mathbf{w}_l^\\top \\mathbf{h} + b_l)$ is trained on English correctness labels (binary: correct/incorrect on GlobalMMLU). We evaluate five cross-lingual transfer conditions:\n\n\\begin{enumerate}\n\\item \\textbf{Zero-shot}: Apply the English-trained probe directly to non-English activations.\n\\item \\textbf{Mean-shift}: Subtract the English activation mean and add the target-language mean before applying the probe.\n\\item \\textbf{Linear projection}: Learn a linear map $\\mathbf{A}$ between English and target-language activation distributions from parallel data.\n\\item \\textbf{Few-shot} (25/100): Fine-tune the probe with 25 or 100 target-language labeled examples.\n\\item \\textbf{CaCLR}: Our proposed method (Section~\\ref{sec:caclr}).\n\\end{enumerate}\n\n\\subsection{Pareto Frontier Analysis}\n\\label{sec:pareto}\n\nFor each probed layer $l$, we measure English probe AUROC and mean cross-lingual transfer AUROC across 19 non-English languages. Plotting these defines a \\emph{depth-transferability Pareto frontier}: the set of layers where no other layer simultaneously achieves higher English and higher transfer performance. We characterize this frontier across multiple architectures to assess universality.\n\n\\subsection{Difficulty--Capability Decomposition}\n\\label{sec:decomp}\n\nTo explain \\emph{why} transfer degrades at deeper layers, we decompose the correctness signal. Using IRT (Item Response Theory) difficulty parameters as supervision, we train Ridge regression probes to extract a \\emph{difficulty direction} from activations. We project out this direction and retrain correctness probes on the residual activations. The residual captures \\emph{capability-specific} signal---language-dependent competence differences that drive transfer degradation.\n\n\\subsection{CaCLR: Calibration-Aware Cross-Lingual Regularization}\n\\label{sec:caclr}\n\n\\caclr{} optimizes a multi-objective loss:\n\\begin{equation}\n\\mathcal{L}_\\text{CaCLR} = \\mathcal{L}_\\text{BCE} + \\alpha \\cdot \\mathcal{L}_\\text{SB-ECE} + \\beta \\cdot \\mathcal{L}_\\text{consistency}\n\\label{eq:caclr}\n\\end{equation}\n\n\\noindent where:\n\\begin{itemize}\n\\item $\\mathcal{L}_\\text{BCE}$ is binary cross-entropy on English correctness labels.\n\\item $\\mathcal{L}_\\text{SB-ECE}$ is a soft-binned ECE loss that directly penalizes calibration error during training (as opposed to post-hoc temperature scaling).\n\\item $\\mathcal{L}_\\text{consistency}$ penalizes divergence between probe outputs on English and non-English parallel activations, forcing the probe to learn language-invariant features without requiring target-language correctness labels.\n\\end{itemize}\n\nThe key insight is that $\\mathcal{L}_\\text{consistency}$ shapes the probe during training to exploit language-invariant features, which is strictly more powerful than post-hoc alignment (mean-shift or linear projection) that corrects distributional mismatch after the probe has already been fit. Hyperparameters $\\alpha$ and $\\beta$ are tuned on a validation set; optimal values are $\\alpha=0.15$ and $\\beta=0.08$.\n\n\\subsection{Orthogonality Analysis}\n\\label{sec:ortho}\n\nFollowing Miao \\& Ungar (2026), we extract the \\emph{verbalized confidence direction} by prompting models for explicit confidence scores and regressing activations on these scores. We compute cosine similarity between the correctness direction (from probes) and the confidence direction across all 20 languages to test whether the orthogonality finding generalizes beyond English.\n\n%------------------------------------------------------------------\n\\section{Experimental Setup}\n\\label{sec:setup}\n%------------------------------------------------------------------\n\n\\paragraph{Models.} We evaluate three architectures: \\textbf{Qwen3-235B-A22B} (94 layers, MoE, $\\sim$22B active parameters), \\textbf{Llama~4~Scout} (48 layers, MoE, $\\sim$17B active, INT8 quantization), and \\textbf{Gemma~4~31B Dense} (60 layers, dense). Activations are extracted at every 4th layer.\n\n\\paragraph{Benchmarks.} Primary evaluation uses \\textbf{GlobalMMLU} (20 languages covering high-, mid-, and low-resource tiers). Generalization is tested on \\textbf{Belebele} (reading comprehension) and \\textbf{MMLU-ProX} (harder MCQA).\n\n\\paragraph{Languages.} Core set: en, zh, de, fr, es, ja, ru, pt, it, ar, hi, ko, vi, th, bn, tr, nl, sw, yo, ig. Extended set: 52 languages covering Austronesian, Dravidian, Niger-Congo~B, Uralic, and Kartvelian families.\n\n\\paragraph{Probes.} Logistic regression (primary) and 2-layer MLP (comparison). Trained on English correctness labels from GlobalMMLU.\n\n\\paragraph{Metrics.} AUROC for discrimination, ECE for calibration quality (lower is better). ECE reduction is reported relative to temperature scaling (optimized $T$; $T=4.87$ for Qwen3, $T=5.34$ for Llama~4).\n\n%------------------------------------------------------------------\n\\section{Results}\n\\label{sec:results}\n%------------------------------------------------------------------\n\n\\subsection{Pareto Frontier Discovery (Claim 1)}\n\\label{sec:res_pareto}\n\n\\paragraph{Qwen3-235B-A22B.}\nTable~\\ref{tab:pareto_qwen3} presents the full depth profile. English AUROC peaks at layer 72 (0.843) while best cross-lingual transfer occurs at layer 56 (0.762 mean across 19 languages). Six layers (L40--L60) form the Pareto frontier, with a Spearman rank correlation of $\\rho=0.88$ between depth and transfer degradation. The 16-layer gap between best-English and best-transfer layers confirms that the depth--transferability tradeoff is substantial at scale.\n\nThe resource-tier gradient is consistent: high-resource languages achieve 0.791 mean AUROC at the best-transfer layer, mid-resource 0.754, and low-resource 0.683. All low-resource languages (sw, yo, ig) exceed 0.65 AUROC.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Qwen3-235B Pareto Frontier: English AUROC vs.\\ zero-shot transfer AUROC by layer. Pareto-optimal layers are marked ($\\bullet$).}\n\\label{tab:pareto_qwen3}\n\\begin{tabular}{rrrrrr}\n\\toprule\nLayer & Depth\\% & EN & ZS-19 & Drop & Pareto \\\\\n\\midrule\n4 & 4 & .621 & .608 & 1.3 & \\\\\n8 & 9 & .648 & .637 & 1.1 & \\\\\n12 & 13 & .689 & .671 & 1.8 & \\\\\n16 & 17 & .712 & .698 & 1.4 & \\\\\n20 & 21 & .738 & .724 & 1.4 & \\\\\n24 & 26 & .756 & .742 & 1.4 & \\\\\n28 & 30 & .771 & .755 & 1.6 & \\\\\n32 & 34 & .784 & .764 & 2.0 & \\\\\n36 & 38 & .795 & .771 & 2.4 & \\\\\n40 & 43 & .803 & .776 & 2.7 & $\\bullet$ \\\\\n44 & 47 & .810 & .774 & 3.6 & $\\bullet$ \\\\\n48 & 51 & .816 & .770 & 4.6 & $\\bullet$ \\\\\n52 & 55 & .822 & .765 & 5.7 & $\\bullet$ \\\\\n56 & 60 & .827 & .762 & 6.5 & $\\bullet$ \\\\\n60 & 64 & .831 & .753 & 7.8 & $\\bullet$ \\\\\n64 & 68 & .835 & .741 & 9.4 & \\\\\n68 & 72 & .839 & .728 & 11.1 & \\\\\n72 & 77 & .843 & .712 & 13.1 & \\\\\n76 & 81 & .841 & .694 & 14.7 & \\\\\n80 & 85 & .838 & .671 & 16.7 & \\\\\n84 & 89 & .832 & .643 & 18.9 & \\\\\n88 & 94 & .819 & .611 & 20.8 & \\\\\n92 & 98 & .791 & .574 & 21.7 & \\\\\n94 & 100 & .762 & .541 & 22.1 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Transfer Conditions at Best-Transfer Layer.}\nTable~\\ref{tab:transfer_conditions} compares all five transfer conditions at layer 56. Mean-shift \\emph{degrades} performance ($-3.1$\\% ECE reduction vs.\\ temperature scaling), confirming that correctness directions require rotation, not translation. Linear projection provides moderate improvement (16.3\\% ECE reduction). Few-shot transfer with 100 labeled examples achieves 19.4\\% ECE reduction. \\caclr{} dominates all conditions: 40.8\\% ECE reduction with AUROC of 0.814, requiring no target-language labels.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Transfer condition comparison at best-transfer layer (L56, Qwen3-235B). ECE reduction is relative to temperature scaling.}\n\\label{tab:transfer_conditions}\n\\begin{tabular}{lccc}\n\\toprule\nCondition & AUROC & ECE & ECE Red.\\% \\\\\n\\midrule\nZero-shot & .762 & .098 & 0.0 \\\\\nMean-shift & .758 & .101 & $-3.1$ \\\\\nLinear proj. & .781 & .082 & 16.3 \\\\\nFew-shot (25) & .748 & .089 & 9.2 \\\\\nFew-shot (100) & .771 & .079 & 19.4 \\\\\n\\caclr{} & \\textbf{.814} & \\textbf{.058} & \\textbf{40.8} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Llama 4 Scout.}\nTable~\\ref{tab:pareto_llama4} shows the Pareto frontier for Llama~4~Scout (48 layers, INT8). English AUROC peaks at layer 36 (0.821); best transfer is at layer 28 (0.741). Four layers (L20--L32) form the frontier, with $\\rho=0.82$. The best-transfer depth is 58\\%, remarkably close to Qwen3's 60\\%.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Llama~4~Scout Pareto Frontier. Pareto-optimal layers marked ($\\bullet$).}\n\\label{tab:pareto_llama4}\n\\begin{tabular}{rrrrrr}\n\\toprule\nLayer & Depth\\% & EN & ZS-19 & Drop & Pareto \\\\\n\\midrule\n4 & 8 & .634 & .624 & 1.0 & \\\\\n8 & 17 & .672 & .659 & 1.3 & \\\\\n12 & 25 & .714 & .699 & 1.5 & \\\\\n16 & 33 & .745 & .729 & 1.6 & \\\\\n20 & 42 & .768 & .748 & 2.0 & $\\bullet$ \\\\\n24 & 50 & .786 & .745 & 4.1 & $\\bullet$ \\\\\n28 & 58 & .798 & .741 & 5.7 & $\\bullet$ \\\\\n32 & 67 & .810 & .732 & 7.8 & $\\bullet$ \\\\\n36 & 75 & .821 & .714 & 10.7 & \\\\\n40 & 83 & .818 & .689 & 12.9 & \\\\\n44 & 92 & .804 & .651 & 15.3 & \\\\\n48 & 100 & .771 & .608 & 16.3 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-Architecture Agreement.}\nTable~\\ref{tab:cross_arch} quantifies cross-architecture agreement. Best-transfer depth, Pareto zone, rank correlation, and frontier shape all agree within tight tolerances across the two MoE architectures. This establishes the depth-transferability tradeoff as an architecture-general property of transformer depth.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture Pareto frontier agreement.}\n\\label{tab:cross_arch}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Qwen3 & Llama4 & Agreement \\\\\n\\midrule\nBest EN depth\\% & 77 & 75 & within 2pp \\\\\nBest transfer depth\\% & 60 & 58 & within 2pp \\\\\nPareto zone\\% & 43--64 & 42--67 & overlapping \\\\\nRank corr.\\ $\\rho$ & 0.88 & 0.82 & both $>$0.75 \\\\\nFrontier shape & convex & convex & consistent \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{Difficulty--Capability Decomposition (Claim 2)}\n\\label{sec:res_decomp}\n%------------------------------------------------------------------\n\nTable~\\ref{tab:decomp} presents the decomposition results. IRT difficulty probes achieve $R^2=0.72$, explaining 68.4\\% of correctness variance. This \\emph{difficulty-shared} component transfers near-perfectly across languages (only 1.1pp drop from English, accounting for 13\\% of total transfer degradation). The \\emph{capability-specific} residual (31.6\\% of variance) drives nearly all transfer degradation: 14.2pp drop, accounting for 87\\% of total degradation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Decomposition: difficulty-shared vs.\\ capability-specific components.}\n\\label{tab:decomp}\n\\begin{tabular}{lcccc}\n\\toprule\nComponent & Var\\% & Transfer & Drop & Share\\% \\\\\n\\midrule\nFull correctness & 100 & .752 & 8.1 & 100 \\\\\nDifficulty (shared) & 68.4 & .738 & 1.1 & 13 \\\\\nCapability (specific) & 31.6 & .614 & 14.2 & 87 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe depth interaction is the mechanistic key (Table~\\ref{tab:decomp_depth}). Capability-specific transfer degradation accelerates with depth: 0.8pp at shallow layers ($<$30\\%), 3.4pp at mid-depth (30--60\\%), and 9.7pp at deep layers (60--90\\%). The ratio of capability to difficulty degradation grows from 2.7$\\times$ to 6.1$\\times$. This explains the Pareto frontier: deeper layers encode stronger capability-specific signals that improve English calibration but are language-dependent and thus impede transfer.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Capability-specific transfer degradation by depth band.}\n\\label{tab:decomp_depth}\n\\begin{tabular}{lccr}\n\\toprule\nDepth Band & Diff.\\ Drop & Cap.\\ Drop & Ratio \\\\\n\\midrule\n0--30\\% & 0.3pp & 0.8pp & 2.7$\\times$ \\\\\n30--60\\% & 0.8pp & 3.4pp & 4.3$\\times$ \\\\\n60--90\\% & 1.6pp & 9.7pp & 6.1$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe decomposition achieves 81\\% prescriptive accuracy: when difficulty explains most of a language-layer combination's correctness variance, zero-shot transfer suffices; when the capability residual is large, \\caclr{} is needed.\n\n%------------------------------------------------------------------\n\\subsection{CaCLR Evaluation (Claim 3)}\n\\label{sec:res_caclr}\n%------------------------------------------------------------------\n\n\\paragraph{Full Comparison.}\nTable~\\ref{tab:caclr_full} compares \\caclr{} against all baselines, averaged across both architectures and 19 non-English languages. \\caclr{} achieves the highest AUROC (0.804) and lowest ECE (0.061) while requiring no target-language labels. It outperforms linear projection by 3.4pp AUROC and few-shot (100 labeled examples) by 4.2pp AUROC. The parameter overhead is minimal ($\\sim$1\\% additional probe parameters).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{\\caclr{} vs.\\ baselines (averaged across both architectures).}\n\\label{tab:caclr_full}\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & AUROC & ECE & Labels? & Overhead \\\\\n\\midrule\nZero-shot & .752 & .098 & no & 0 \\\\\nMean-shift & .747 & .102 & no & 0 \\\\\nLinear proj. & .770 & .082 & no & $d{\\times}d$ \\\\\nFew-shot (25) & .738 & .089 & yes (25) & 0 \\\\\nFew-shot (100) & .762 & .079 & yes (100) & 0 \\\\\n\\caclr{} & \\textbf{.804} & \\textbf{.061} & \\textbf{no} & $\\sim$1\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Ablation.}\nTable~\\ref{tab:ablation} shows the contribution of each \\caclr{} loss component. $\\mathcal{L}_\\text{consistency}$ provides the bulk of AUROC improvement (+4.1pp alone), while $\\mathcal{L}_\\text{SB\\text{-}ECE}$ contributes calibration refinement (ECE drops from 0.078 to 0.061 when added). The full objective achieves synergistic gains: 0.804 AUROC and 0.061 ECE, better than either auxiliary term alone.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Ablation of \\caclr{} loss components.}\n\\label{tab:ablation}\n\\begin{tabular}{lccc}\n\\toprule\nConfiguration & AUROC & ECE & $\\Delta$AUROC \\\\\n\\midrule\n$\\mathcal{L}_\\text{BCE}$ only & .752 & .098 & $-5.2$ \\\\\n$+ \\mathcal{L}_\\text{SB-ECE}$ & .768 & .072 & $-3.6$ \\\\\n$+ \\mathcal{L}_\\text{consistency}$ & .793 & .078 & $-1.1$ \\\\\nFull \\caclr{} & \\textbf{.804} & \\textbf{.061} & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Pareto Frontier Shift.}\nTable~\\ref{tab:pareto_shift} demonstrates the headline result: \\caclr{} shifts the Pareto frontier outward on Qwen3-235B. At layer 64, zero-shot transfer achieves 0.741 AUROC; \\caclr{} achieves 0.814---a 7.3pp improvement. The practical implication: \\caclr{} enables operating at deeper, better-calibrated layers without sacrificing cross-lingual transfer. The shifted Pareto frontier extends from L48 to L68, 2 layers deeper than the original frontier (L40--L60).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{\\caclr{} Pareto frontier shift (Qwen3-235B). Shifted Pareto layers marked ($\\bullet$).}\n\\label{tab:pareto_shift}\n\\begin{tabular}{rcccc}\n\\toprule\nLayer & ZS & \\caclr{} & $\\Delta$pp & Shifted \\\\\n\\midrule\n40 & .776 & .798 & 2.2 & \\\\\n44 & .774 & .800 & 2.6 & \\\\\n48 & .770 & .803 & 3.3 & $\\bullet$ \\\\\n52 & .765 & .806 & 4.1 & $\\bullet$ \\\\\n56 & .762 & .810 & 4.8 & $\\bullet$ \\\\\n60 & .753 & .814 & 6.1 & $\\bullet$ \\\\\n64 & .741 & .814 & 7.3 & $\\bullet$ \\\\\n68 & .728 & .808 & 8.0 & $\\bullet$ \\\\\n72 & .712 & .796 & 8.4 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe improvement pass rate across model--language pairs is 92\\% (35/38). The 3 non-improving pairs are high-resource languages on Llama~4~Scout where zero-shot transfer is already excellent and the consistency loss has minimal signal to exploit.\n\n\\paragraph{Low-Resource Performance.}\n\\caclr{} is especially effective for low-resource languages. On Qwen3: Swahili 0.731, Yoruba 0.709, Igbo 0.718 (vs.\\ zero-shot: 0.695, 0.672, 0.681). On Llama~4: Swahili 0.712, Yoruba 0.681, Igbo 0.698. All low-resource languages pass the 0.60 AUROC threshold for usable calibration.\n\n%------------------------------------------------------------------\n\\subsection{Cross-Lingual Orthogonality (Claim 4)}\n\\label{sec:res_ortho}\n%------------------------------------------------------------------\n\nTable~\\ref{tab:ortho} presents the correctness--confidence cosine similarity across all 20 languages and both architectures. The mean cosine is 0.052 (range: 0.018--0.094), well within the near-orthogonal regime ($<0.1$). Across all 40 language--architecture pairs, 39/40 fall below 0.1 (Yoruba on Llama~4 reaches 0.099).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Correctness--confidence cosine similarity by language. All values $<0.1$.}\n\\label{tab:ortho}\n\\begin{tabular}{llccc}\n\\toprule\nLanguage & Tier & Qwen3 & Llama4 & Mean \\\\\n\\midrule\nen & high & .031 & .037 & .034 \\\\\nzh & high & .035 & .041 & .038 \\\\\nde & high & .033 & .039 & .036 \\\\\nfr & high & .036 & .042 & .039 \\\\\nes & high & .038 & .044 & .041 \\\\\nja & high & .041 & .047 & .044 \\\\\nru & high & .040 & .046 & .043 \\\\\npt & high & .037 & .043 & .040 \\\\\nit & high & .039 & .045 & .042 \\\\\nnl & high & .034 & .040 & .037 \\\\\n\\midrule\nar & mid & .047 & .055 & .051 \\\\\nhi & mid & .051 & .059 & .055 \\\\\nko & mid & .045 & .053 & .049 \\\\\nvi & mid & .054 & .062 & .058 \\\\\nth & mid & .057 & .065 & .061 \\\\\nbn & mid & .052 & .060 & .056 \\\\\ntr & mid & .048 & .056 & .052 \\\\\n\\midrule\nsw & low & .073 & .083 & .078 \\\\\nyo & low & .089 & .099 & .094 \\\\\nig & low & .077 & .087 & .082 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe resource-tier gradient is notable: high-resource languages have mean cosine 0.041, mid-resource 0.054, and low-resource 0.074 (Spearman $\\rho=-0.68$ between resource tier and cosine). This suggests that output-based calibration methods are not just structurally limited but are \\emph{more} limited for well-resourced languages where the orthogonality is strongest. The cross-architecture consistency (Qwen3: 0.048, Llama~4: 0.057) confirms this is not architecture-specific (Table~\\ref{tab:ortho_summary}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Orthogonality summary statistics.}\n\\label{tab:ortho_summary}\n\\begin{tabular}{lccc}\n\\toprule\nStatistic & Qwen3 & Llama4 & Both \\\\\n\\midrule\nMean & 0.048 & 0.057 & 0.052 \\\\\nStd & 0.015 & 0.017 & 0.016 \\\\\nMax & 0.089 & 0.099 & 0.094 \\\\\nMin & 0.031 & 0.037 & 0.018 \\\\\nAll $<0.1$ & 20/20 & 19/20 & 39/40 \\\\\nTier corr.\\ $\\rho$ & $-0.71$ & $-0.65$ & $-0.68$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{Probe Complexity Analysis}\n\\label{sec:res_probe}\n%------------------------------------------------------------------\n\nTable~\\ref{tab:probe_complexity} compares logistic regression vs.\\ 2-layer MLP probes. MLPs gain 1.3pp English AUROC but lose 4.3pp in cross-lingual transfer. The transfer advantage of linear probes grows with depth: 2.1pp at shallow layers vs.\\ 6.8pp at deep layers. This confirms that deep-layer transfer degradation is driven by nonlinear, language-specific features that MLPs exploit but linear probes ignore. Linear probes are thus the correct choice for cross-lingual calibration transfer.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Probe complexity comparison (Qwen3-235B).}\n\\label{tab:probe_complexity}\n\\begin{tabular}{lcccc}\n\\toprule\nProbe & EN Best & ZS-19 & Drop & ECE \\\\\n\\midrule\nLogistic regression & .843 & .762 & 8.1pp & .054 \\\\\n2-layer MLP & .856 & .733 & 12.4pp & .068 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{Cross-Benchmark Generalization}\n\\label{sec:res_benchmark}\n%------------------------------------------------------------------\n\nTable~\\ref{tab:cross_bench} shows that \\caclr{} generalizes cleanly across benchmarks. The improvement magnitude is remarkably stable: 5.1--5.2pp AUROC gain and 33--40\\% ECE reduction across GlobalMMLU, Belebele (reading comprehension), and MMLU-ProX (harder MCQA). The cross-benchmark coefficient of variation for \\caclr{} improvement is 0.08, indicating the method addresses a fundamental representation alignment issue rather than overfitting to benchmark-specific patterns.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-benchmark generalization of \\caclr{}.}\n\\label{tab:cross_bench}\n\\begin{tabular}{lcccc}\n\\toprule\nBenchmark & ZS & \\caclr{} & $\\Delta$pp & ECE Red.\\% \\\\\n\\midrule\nGlobalMMLU & .752 & .804 & 5.2 & 39.7 \\\\\nBelebele & .738 & .789 & 5.1 & 36.2 \\\\\nMMLU-ProX & .722 & .774 & 5.2 & 33.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{Three-Architecture Validation}\n\\label{sec:res_three_arch}\n%------------------------------------------------------------------\n\nTable~\\ref{tab:three_arch} summarizes results across all three architectures, including Gemma~4~31B Dense. The best-transfer depth converges to 58--60\\% across dense and MoE architectures with 48--94 layers. \\caclr{} provides consistent 2.9--3.3pp improvement. The Pareto rank correlation is 0.82--0.88 in all cases. Dense vs.\\ MoE architecture makes minimal difference---the phenomenon is a property of transformer depth, not routing architecture.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Three-architecture summary. Transfer depth\\% = best cross-lingual transfer layer as percentage of total depth.}\n\\label{tab:three_arch}\n\\begin{tabular}{lcccccc}\n\\toprule\nModel & Type & $L$ & EN & ZS-19 & Depth\\% & $\\rho$ \\\\\n\\midrule\nQwen3-235B & MoE & 94 & .843 & .762 & 60 & .88 \\\\\nLlama 4 Scout & MoE & 48 & .821 & .741 & 58 & .82 \\\\\nGemma 4 31B & Dense & 60 & .812 & .734 & 60 & .86 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{Extended Language Coverage}\n\\label{sec:res_extended}\n%------------------------------------------------------------------\n\nTable~\\ref{tab:extended_langs} summarizes the extension to 52 languages. The resource-tier gradient is smooth: \\caclr{} gain increases from 3.0pp (high-resource) to 5.6pp (very-low-resource), confirming that the consistency loss provides most value where representation misalignment is worst. Zero-shot \\caclr{} transfer achieves $>$0.60 AUROC for 48/51 non-English languages, establishing practical usability across the vast majority of languages without any target-language labels.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Extended coverage (52 languages) by resource tier.}\n\\label{tab:extended_langs}\n\\begin{tabular}{lccccc}\n\\toprule\nTier & $n$ & ZS & \\caclr{} & $\\Delta$pp & $>$0.60 \\\\\n\\midrule\nHigh & 12 & .782 & .812 & 3.0 & 100\\% \\\\\nMid & 25 & .738 & .784 & 4.6 & 100\\% \\\\\nLow & 10 & .661 & .712 & 5.1 & 90\\% \\\\\nVery low & 4 & .582 & .638 & 5.6 & 50\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{INT8 Quantization Validation}\n\\label{sec:res_int8}\n%------------------------------------------------------------------\n\nTable~\\ref{tab:int8} validates that INT8 weight quantization (used for Llama~4~Scout) introduces negligible distortion. The maximum AUROC difference is 0.3pp, and the rank correlation between INT8 and FP16 layer rankings is 0.997. The Pareto frontier shape and ordering are perfectly preserved, confirming that our quantized results are reliable.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{INT8 vs.\\ FP16 validation (Llama~4~Scout, 5\\% subset).}\n\\label{tab:int8}\n\\begin{tabular}{rcccccc}\n\\toprule\nLayer & FP16 & INT8 & $\\Delta$ & FP16-ZS & INT8-ZS & $\\Delta$-ZS \\\\\n\\midrule\n8 & .674 & .672 & .2 & .661 & .658 & .3 \\\\\n16 & .747 & .745 & .2 & .731 & .728 & .3 \\\\\n24 & .788 & .786 & .2 & .747 & .744 & .3 \\\\\n32 & .812 & .810 & .2 & .734 & .731 & .3 \\\\\n40 & .820 & .817 & .3 & .691 & .687 & .4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\section{Discussion}\n\\label{sec:discussion}\n%------------------------------------------------------------------\n\n\\paragraph{Why CaCLR Works.}\nThe decomposition analysis (Section~\\ref{sec:res_decomp}) provides a mechanistic explanation. The consistency loss ($\\mathcal{L}_\\text{consistency}$) specifically targets the capability-specific component---the 32\\% of correctness variance that is language-dependent and drives 87\\% of transfer degradation. By forcing alignment of probe outputs across languages during training, \\caclr{} learns to extract language-invariant correctness features. This is strictly more powerful than post-hoc alignment (linear projection corrects first-order distributional mismatch but not nonlinear feature interactions).\n\n\\paragraph{Why Output-Based Methods Cannot Suffice.}\nThe orthogonality results (Section~\\ref{sec:res_ortho}) establish a structural limitation. With correctness and verbalized confidence directions nearly orthogonal across all 20 languages (mean cosine = 0.052), output-based methods---which operate on the confidence direction---cannot access correctness information regardless of language. The resource-tier gradient (stronger orthogonality for high-resource languages) further implies that improved multilingual training actually \\emph{widens} this structural gap.\n\n\\paragraph{Limitations.}\nOur evaluation is restricted to MCQA benchmarks where correctness is cleanly defined. Extension to open-ended generation requires different correctness labeling strategies. The consistency loss requires parallel or comparable cross-lingual activations, which limits applicability to settings where such data exists. We evaluate only logistic regression probes; nonlinear probes may yield different tradeoff curves.\n\n%------------------------------------------------------------------\n\\section{Conclusion}\n\\label{sec:conclusion}\n%------------------------------------------------------------------\n\nWe presented the first systematic study of cross-lingual probe-based calibration, testing whether the emerging research line on representation-level calibration extends beyond English. Our four findings form a causal chain: (1)~a depth-transferability Pareto frontier constrains all probe-based calibration transfer, converging to $\\sim$60\\% depth across three architectures; (2)~this frontier arises because capability-specific (not difficulty-shared) signals drive transfer degradation, especially at depth; (3)~\\caclr{} shifts this frontier outward, achieving $\\sim$40\\% ECE reduction over temperature scaling with zero target-language labels; and (4)~correctness--confidence orthogonality persists across all 20 languages, establishing output-based calibration as structurally limited regardless of language. Results extend to 52 languages and three benchmarks, confirming the generality of both the problem and our proposed solution.\n\n%------------------------------------------------------------------\n% References\n%------------------------------------------------------------------\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[\\protect\\citeauthoryear{Burns et al.}{2023}]{burns2023discovering}\nCollin Burns, Haotian Ye, Dan Klein, and Jacob Steinhardt.\n\\newblock Discovering latent knowledge in language models without supervision.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem[\\protect\\citeauthoryear{Marks et al.}{2024}]{marks2024geometry}\nSamuel Marks, Max Tegmark, et al.\n\\newblock The geometry of truth: Emergent linear structure in large language model representations of true/false datasets.\n\\newblock In \\emph{COLM}, 2024.\n\n\\bibitem[\\protect\\citeauthoryear{Miao et al.}{2026a}]{miao2026coral}\nShuo Miao et al.\n\\newblock {CORAL}: Cross-task correctness probes for LLM calibration.\n\\newblock 2026.\n\n\\bibitem[\\protect\\citeauthoryear{Miao and Ungar}{2026b}]{miao2026ortho}\nShuo Miao and Lyle Ungar.\n\\newblock Orthogonality of correctness and confidence directions in LLM representations.\n\\newblock 2026.\n\n\\bibitem[\\protect\\citeauthoryear{Xiao et al.}{2025}]{xiao2025knowledge}\nZhihao Xiao et al.\n\\newblock Cross-lingual knowledge boundary probe transfer.\n\\newblock In \\emph{ACL}, 2025.\n\n\\bibitem[\\protect\\citeauthoryear{Civelli et al.}{2025}]{civelli2025difficulty}\nAndrea Civelli et al.\n\\newblock Cross-lingual difficulty probe transfer in multilingual LLMs.\n\\newblock 2025.\n\n\\bibitem[\\protect\\citeauthoryear{Zhou et al.}{2024}]{zhou2024lace}\nXin Zhou et al.\n\\newblock {LACE}: Layer-adaptive calibration ensembles for multilingual LLMs.\n\\newblock 2024.\n\n\\bibitem[\\protect\\citeauthoryear{Gao et al.}{2024}]{gao2024quantization}\nLeo Gao et al.\n\\newblock Quantization effects on probing and representation analysis.\n\\newblock 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fff56ec-057b-417b-9200-608429a299f8",
  "isSidechain": false,
  "requestId": "req_011CbENE7mPhvqAUrDH3FB4L",
  "type": "assistant",
  "uuid": "1280f160-b2b0-4225-9b68-bf58250319cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JrQgYCfpKV1pMAcp7h5QVj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 641,
      "cache_read_input_tokens": 41966,
      "output_tokens": 12041,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 641,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12041,
          "cache_read_input_tokens": 41966,
          "cache_creation_input_tokens": 641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 641
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

_source line 20 · 2026-05-20T19:26:59.512Z_

<details><summary>↩ Tool result · `toolu_01HwuSAwDfWUf9QGnXZtuBoW`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1280f160-b2b0-4225-9b68-bf58250319cf",
  "isSidechain": false,
  "promptId": "907ecca9-b4a5-4dd2-af0b-6dcee3e5aad0",
  "type": "user",
  "uuid": "44815b61-43bc-4d3b-95df-2929123b3fe5",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{microtype}\n\\usepackage{array}\n\n\\newcommand{\\caclr}{\\textsc{CaCLR}}\n\\newcommand{\\ece}{\\text{ECE}}\n\\newcommand{\\auroc}{\\text{AUROC}}\n\n\\title{Shifting the Cross-Lingual Calibration Pareto Frontier:\\\\Probe-Based Calibration Transfer via CaCLR}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nNon-English languages suffer substantially worse calibration in multilingual LLMs, yet existing probe-based calibration methods operate exclusively in English.\nWe present the first systematic study of cross-lingual correctness probe transfer for calibration across 20 languages and three architectures (Qwen3-235B-A22B, Llama~4~Scout, Gemma~4~31B Dense).\nWe discover a \\emph{depth-transferability Pareto frontier}: deeper layers yield better English calibration but degrade cross-lingual zero-shot transfer, with the optimal transfer depth converging to $\\sim$58--60\\% of model depth across architectures.\nWe decompose correctness probe signal into a \\emph{difficulty-shared} component (68\\% of variance, language-agnostic, transfers at all depths) and a \\emph{capability-specific} component (32\\%, language-dependent, drives 87\\% of transfer degradation).\nWe propose \\caclr{} (\\textbf{Ca}libration-aware \\textbf{C}ross-\\textbf{L}ingual \\textbf{R}egularization), a training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without target-language labels.\n\\caclr{} shifts the Pareto frontier outward: averaged across architectures, it improves non-English AUROC by 5.2pp over zero-shot transfer and reduces ECE by $\\sim$40\\% relative to temperature scaling, with zero target-language correctness labels.\nWe further show that correctness--confidence orthogonality (cosine $<0.1$) persists across all 20 languages in both architectures, establishing output-based calibration as structurally limited regardless of language.\nResults generalize to 52 languages and two additional benchmarks (Belebele, MMLU-ProX).\n\\end{abstract}\n\n%------------------------------------------------------------------\n\\section{Introduction}\n\\label{sec:intro}\n%------------------------------------------------------------------\n\nCalibration---the alignment between a model's expressed confidence and its actual accuracy---is critical for safe deployment of large language models (LLMs). While recent work has made substantial progress on English calibration through internal representation probing \\cite{burns2023discovering,marks2024geometry,miao2026coral}, non-English languages remain poorly served: they suffer up to 5$\\times$ worse expected calibration error (ECE) under standard output-based methods.\n\nThis gap is not merely quantitative. Miao \\& Ungar (2026) demonstrated that the correctness direction in LLM activation space is \\emph{orthogonal} to the verbalized confidence direction, implying that output-based calibration methods are structurally limited. However, their analysis---and indeed all probe-based calibration work---is restricted to English. Whether this entire research line extends to multilingual settings is an open question with field-level implications.\n\nWe address this question systematically. Our investigation reveals four findings that form an unbroken causal chain:\n\n\\paragraph{Claim 1: Pareto Frontier (Discovery).}\nCross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth converges to $\\sim$58--60\\% of model depth across three architectures (Qwen3-235B-A22B, Llama~4~Scout, Gemma~4~31B Dense), with Spearman rank correlations between depth and transfer degradation of $\\rho=0.82$--$0.88$ ($p<0.001$).\n\n\\paragraph{Claim 2: Decomposition (Analysis).}\nCross-lingual transfer decomposes into a \\emph{difficulty-shared} component (68\\% of correctness variance; language-agnostic; transfers at all depths) and a \\emph{capability-specific} component (32\\%; language-dependent; accounts for 87\\% of transfer degradation). This decomposition is prescriptive: it predicts with 81\\% accuracy when alignment intervention is needed.\n\n\\paragraph{Claim 3: CaCLR (Method).}\nWe propose \\caclr{}, a probe training objective ($\\mathcal{L}_\\text{BCE} + \\alpha \\cdot \\mathcal{L}_\\text{SB-ECE} + \\beta \\cdot \\mathcal{L}_\\text{consistency}$) that shifts the Pareto frontier outward by jointly optimizing calibration and cross-lingual invariance. Averaged across both architectures, \\caclr{} improves non-English AUROC by 5.2pp over zero-shot transfer and reduces ECE by $\\sim$40\\% relative to temperature scaling, requiring zero target-language correctness labels.\n\n\\paragraph{Claim 4: Cross-Lingual Orthogonality (Mechanistic).}\nThe correctness--confidence orthogonality persists across all 20 languages (mean cosine similarity = 0.052, all $<$ 0.1), with a resource-tier gradient ($\\rho=-0.68$): better-resourced languages show stronger orthogonality. This establishes output-based calibration as fundamentally limited regardless of language.\n\nTogether, these claims position \\caclr{} as the first method to provide effective probe-based cross-lingual calibration without target-language labels, shifting the Pareto frontier that constrains all prior approaches.\n\n%------------------------------------------------------------------\n\\section{Related Work}\n\\label{sec:related}\n%------------------------------------------------------------------\n\n\\paragraph{Probe-Based Calibration.}\nBurns et al.\\ (2023) and Marks et al.\\ (2024) showed that linear probes on intermediate activations can recover correctness signals. Miao et al.\\ (2026a; CORAL) demonstrated cross-task transfer of such probes. Miao \\& Ungar (2026b) established the orthogonality of correctness and verbalized confidence directions. All of this work is English-only.\n\n\\paragraph{Cross-Lingual Representation Transfer.}\nXiao et al.\\ (ACL 2025) transferred \\emph{knowledge-boundary} probes (input-level answerability, not output-dependent correctness) across 8 languages, measuring probing accuracy rather than calibration. Civelli et al.\\ transferred difficulty probes cross-lingually, finding language-agnostic difficulty encoding---a result we leverage as a control in our decomposition (Claim~2).\n\n\\paragraph{Multilingual Calibration.}\nLACE (Zhou et al.) uses per-language layer ensembles but requires target-language labels. MKA employs multi-key attention at 5$\\times$ inference cost. Temperature scaling is the standard output-based baseline. None addresses representation-level cross-lingual calibration transfer.\n\n%------------------------------------------------------------------\n\\section{Method}\n\\label{sec:method}\n%------------------------------------------------------------------\n\n\\subsection{Correctness Probing and Transfer}\n\\label{sec:probing}\n\nGiven a multilingual LLM with $L$ layers, we extract activations $\\mathbf{h}_l^{(i)}$ at layer $l$ for input $i$. A logistic regression probe $f_l(\\mathbf{h}) = \\sigma(\\mathbf{w}_l^\\top \\mathbf{h} + b_l)$ is trained on English correctness labels (binary: correct/incorrect on GlobalMMLU). We evaluate five cross-lingual transfer conditions:\n\n\\begin{enumerate}\n\\item \\textbf{Zero-shot}: Apply the English-trained probe directly to non-English activations.\n\\item \\textbf{Mean-shift}: Subtract the English activation mean and add the target-language mean before applying the probe.\n\\item \\textbf{Linear projection}: Learn a linear map $\\mathbf{A}$ between English and target-language activation distributions from parallel data.\n\\item \\textbf{Few-shot} (25/100): Fine-tune the probe with 25 or 100 target-language labeled examples.\n\\item \\textbf{CaCLR}: Our proposed method (Section~\\ref{sec:caclr}).\n\\end{enumerate}\n\n\\subsection{Pareto Frontier Analysis}\n\\label{sec:pareto}\n\nFor each probed layer $l$, we measure English probe AUROC and mean cross-lingual transfer AUROC across 19 non-English languages. Plotting these defines a \\emph{depth-transferability Pareto frontier}: the set of layers where no other layer simultaneously achieves higher English and higher transfer performance. We characterize this frontier across multiple architectures to assess universality.\n\n\\subsection{Difficulty--Capability Decomposition}\n\\label{sec:decomp}\n\nTo explain \\emph{why} transfer degrades at deeper layers, we decompose the correctness signal. Using IRT (Item Response Theory) difficulty parameters as supervision, we train Ridge regression probes to extract a \\emph{difficulty direction} from activations. We project out this direction and retrain correctness probes on the residual activations. The residual captures \\emph{capability-specific} signal---language-dependent competence differences that drive transfer degradation.\n\n\\subsection{CaCLR: Calibration-Aware Cross-Lingual Regularization}\n\\label{sec:caclr}\n\n\\caclr{} optimizes a multi-objective loss:\n\\begin{equation}\n\\mathcal{L}_\\text{CaCLR} = \\mathcal{L}_\\text{BCE} + \\alpha \\cdot \\mathcal{L}_\\text{SB-ECE} + \\beta \\cdot \\mathcal{L}_\\text{consistency}\n\\label{eq:caclr}\n\\end{equation}\n\n\\noindent where:\n\\begin{itemize}\n\\item $\\mathcal{L}_\\text{BCE}$ is binary cross-entropy on English correctness labels.\n\\item $\\mathcal{L}_\\text{SB-ECE}$ is a soft-binned ECE loss that directly penalizes calibration error during training (as opposed to post-hoc temperature scaling).\n\\item $\\mathcal{L}_\\text{consistency}$ penalizes divergence between probe outputs on English and non-English parallel activations, forcing the probe to learn language-invariant features without requiring target-language correctness labels.\n\\end{itemize}\n\nThe key insight is that $\\mathcal{L}_\\text{consistency}$ shapes the probe during training to exploit language-invariant features, which is strictly more powerful than post-hoc alignment (mean-shift or linear projection) that corrects distributional mismatch after the probe has already been fit. Hyperparameters $\\alpha$ and $\\beta$ are tuned on a validation set; optimal values are $\\alpha=0.15$ and $\\beta=0.08$.\n\n\\subsection{Orthogonality Analysis}\n\\label{sec:ortho}\n\nFollowing Miao \\& Ungar (2026), we extract the \\emph{verbalized confidence direction} by prompting models for explicit confidence scores and regressing activations on these scores. We compute cosine similarity between the correctness direction (from probes) and the confidence direction across all 20 languages to test whether the orthogonality finding generalizes beyond English.\n\n%------------------------------------------------------------------\n\\section{Experimental Setup}\n\\label{sec:setup}\n%------------------------------------------------------------------\n\n\\paragraph{Models.} We evaluate three architectures: \\textbf{Qwen3-235B-A22B} (94 layers, MoE, $\\sim$22B active parameters), \\textbf{Llama~4~Scout} (48 layers, MoE, $\\sim$17B active, INT8 quantization), and \\textbf{Gemma~4~31B Dense} (60 layers, dense). Activations are extracted at every 4th layer.\n\n\\paragraph{Benchmarks.} Primary evaluation uses \\textbf{GlobalMMLU} (20 languages covering high-, mid-, and low-resource tiers). Generalization is tested on \\textbf{Belebele} (reading comprehension) and \\textbf{MMLU-ProX} (harder MCQA).\n\n\\paragraph{Languages.} Core set: en, zh, de, fr, es, ja, ru, pt, it, ar, hi, ko, vi, th, bn, tr, nl, sw, yo, ig. Extended set: 52 languages covering Austronesian, Dravidian, Niger-Congo~B, Uralic, and Kartvelian families.\n\n\\paragraph{Probes.} Logistic regression (primary) and 2-layer MLP (comparison). Trained on English correctness labels from GlobalMMLU.\n\n\\paragraph{Metrics.} AUROC for discrimination, ECE for calibration quality (lower is better). ECE reduction is reported relative to temperature scaling (optimized $T$; $T=4.87$ for Qwen3, $T=5.34$ for Llama~4).\n\n%------------------------------------------------------------------\n\\section{Results}\n\\label{sec:results}\n%------------------------------------------------------------------\n\n\\subsection{Pareto Frontier Discovery (Claim 1)}\n\\label{sec:res_pareto}\n\n\\paragraph{Qwen3-235B-A22B.}\nTable~\\ref{tab:pareto_qwen3} presents the full depth profile. English AUROC peaks at layer 72 (0.843) while best cross-lingual transfer occurs at layer 56 (0.762 mean across 19 languages). Six layers (L40--L60) form the Pareto frontier, with a Spearman rank correlation of $\\rho=0.88$ between depth and transfer degradation. The 16-layer gap between best-English and best-transfer layers confirms that the depth--transferability tradeoff is substantial at scale.\n\nThe resource-tier gradient is consistent: high-resource languages achieve 0.791 mean AUROC at the best-transfer layer, mid-resource 0.754, and low-resource 0.683. All low-resource languages (sw, yo, ig) exceed 0.65 AUROC.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Qwen3-235B Pareto Frontier: English AUROC vs.\\ zero-shot transfer AUROC by layer. Pareto-optimal layers are marked ($\\bullet$).}\n\\label{tab:pareto_qwen3}\n\\begin{tabular}{rrrrrr}\n\\toprule\nLayer & Depth\\% & EN & ZS-19 & Drop & Pareto \\\\\n\\midrule\n4 & 4 & .621 & .608 & 1.3 & \\\\\n8 & 9 & .648 & .637 & 1.1 & \\\\\n12 & 13 & .689 & .671 & 1.8 & \\\\\n16 & 17 & .712 & .698 & 1.4 & \\\\\n20 & 21 & .738 & .724 & 1.4 & \\\\\n24 & 26 & .756 & .742 & 1.4 & \\\\\n28 & 30 & .771 & .755 & 1.6 & \\\\\n32 & 34 & .784 & .764 & 2.0 & \\\\\n36 & 38 & .795 & .771 & 2.4 & \\\\\n40 & 43 & .803 & .776 & 2.7 & $\\bullet$ \\\\\n44 & 47 & .810 & .774 & 3.6 & $\\bullet$ \\\\\n48 & 51 & .816 & .770 & 4.6 & $\\bullet$ \\\\\n52 & 55 & .822 & .765 & 5.7 & $\\bullet$ \\\\\n56 & 60 & .827 & .762 & 6.5 & $\\bullet$ \\\\\n60 & 64 & .831 & .753 & 7.8 & $\\bullet$ \\\\\n64 & 68 & .835 & .741 & 9.4 & \\\\\n68 & 72 & .839 & .728 & 11.1 & \\\\\n72 & 77 & .843 & .712 & 13.1 & \\\\\n76 & 81 & .841 & .694 & 14.7 & \\\\\n80 & 85 & .838 & .671 & 16.7 & \\\\\n84 & 89 & .832 & .643 & 18.9 & \\\\\n88 & 94 & .819 & .611 & 20.8 & \\\\\n92 & 98 & .791 & .574 & 21.7 & \\\\\n94 & 100 & .762 & .541 & 22.1 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Transfer Conditions at Best-Transfer Layer.}\nTable~\\ref{tab:transfer_conditions} compares all five transfer conditions at layer 56. Mean-shift \\emph{degrades} performance ($-3.1$\\% ECE reduction vs.\\ temperature scaling), confirming that correctness directions require rotation, not translation. Linear projection provides moderate improvement (16.3\\% ECE reduction). Few-shot transfer with 100 labeled examples achieves 19.4\\% ECE reduction. \\caclr{} dominates all conditions: 40.8\\% ECE reduction with AUROC of 0.814, requiring no target-language labels.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Transfer condition comparison at best-transfer layer (L56, Qwen3-235B). ECE reduction is relative to temperature scaling.}\n\\label{tab:transfer_conditions}\n\\begin{tabular}{lccc}\n\\toprule\nCondition & AUROC & ECE & ECE Red.\\% \\\\\n\\midrule\nZero-shot & .762 & .098 & 0.0 \\\\\nMean-shift & .758 & .101 & $-3.1$ \\\\\nLinear proj. & .781 & .082 & 16.3 \\\\\nFew-shot (25) & .748 & .089 & 9.2 \\\\\nFew-shot (100) & .771 & .079 & 19.4 \\\\\n\\caclr{} & \\textbf{.814} & \\textbf{.058} & \\textbf{40.8} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Llama 4 Scout.}\nTable~\\ref{tab:pareto_llama4} shows the Pareto frontier for Llama~4~Scout (48 layers, INT8). English AUROC peaks at layer 36 (0.821); best transfer is at layer 28 (0.741). Four layers (L20--L32) form the frontier, with $\\rho=0.82$. The best-transfer depth is 58\\%, remarkably close to Qwen3's 60\\%.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Llama~4~Scout Pareto Frontier. Pareto-optimal layers marked ($\\bullet$).}\n\\label{tab:pareto_llama4}\n\\begin{tabular}{rrrrrr}\n\\toprule\nLayer & Depth\\% & EN & ZS-19 & Drop & Pareto \\\\\n\\midrule\n4 & 8 & .634 & .624 & 1.0 & \\\\\n8 & 17 & .672 & .659 & 1.3 & \\\\\n12 & 25 & .714 & .699 & 1.5 & \\\\\n16 & 33 & .745 & .729 & 1.6 & \\\\\n20 & 42 & .768 & .748 & 2.0 & $\\bullet$ \\\\\n24 & 50 & .786 & .745 & 4.1 & $\\bullet$ \\\\\n28 & 58 & .798 & .741 & 5.7 & $\\bullet$ \\\\\n32 & 67 & .810 & .732 & 7.8 & $\\bullet$ \\\\\n36 & 75 & .821 & .714 & 10.7 & \\\\\n40 & 83 & .818 & .689 & 12.9 & \\\\\n44 & 92 & .804 & .651 & 15.3 & \\\\\n48 & 100 & .771 & .608 & 16.3 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-Architecture Agreement.}\nTable~\\ref{tab:cross_arch} quantifies cross-architecture agreement. Best-transfer depth, Pareto zone, rank correlation, and frontier shape all agree within tight tolerances across the two MoE architectures. This establishes the depth-transferability tradeoff as an architecture-general property of transformer depth.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture Pareto frontier agreement.}\n\\label{tab:cross_arch}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Qwen3 & Llama4 & Agreement \\\\\n\\midrule\nBest EN depth\\% & 77 & 75 & within 2pp \\\\\nBest transfer depth\\% & 60 & 58 & within 2pp \\\\\nPareto zone\\% & 43--64 & 42--67 & overlapping \\\\\nRank corr.\\ $\\rho$ & 0.88 & 0.82 & both $>$0.75 \\\\\nFrontier shape & convex & convex & consistent \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{Difficulty--Capability Decomposition (Claim 2)}\n\\label{sec:res_decomp}\n%------------------------------------------------------------------\n\nTable~\\ref{tab:decomp} presents the decomposition results. IRT difficulty probes achieve $R^2=0.72$, explaining 68.4\\% of correctness variance. This \\emph{difficulty-shared} component transfers near-perfectly across languages (only 1.1pp drop from English, accounting for 13\\% of total transfer degradation). The \\emph{capability-specific} residual (31.6\\% of variance) drives nearly all transfer degradation: 14.2pp drop, accounting for 87\\% of total degradation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Decomposition: difficulty-shared vs.\\ capability-specific components.}\n\\label{tab:decomp}\n\\begin{tabular}{lcccc}\n\\toprule\nComponent & Var\\% & Transfer & Drop & Share\\% \\\\\n\\midrule\nFull correctness & 100 & .752 & 8.1 & 100 \\\\\nDifficulty (shared) & 68.4 & .738 & 1.1 & 13 \\\\\nCapability (specific) & 31.6 & .614 & 14.2 & 87 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe depth interaction is the mechanistic key (Table~\\ref{tab:decomp_depth}). Capability-specific transfer degradation accelerates with depth: 0.8pp at shallow layers ($<$30\\%), 3.4pp at mid-depth (30--60\\%), and 9.7pp at deep layers (60--90\\%). The ratio of capability to difficulty degradation grows from 2.7$\\times$ to 6.1$\\times$. This explains the Pareto frontier: deeper layers encode stronger capability-specific signals that improve English calibration but are language-dependent and thus impede transfer.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Capability-specific transfer degradation by depth band.}\n\\label{tab:decomp_depth}\n\\begin{tabular}{lccr}\n\\toprule\nDepth Band & Diff.\\ Drop & Cap.\\ Drop & Ratio \\\\\n\\midrule\n0--30\\% & 0.3pp & 0.8pp & 2.7$\\times$ \\\\\n30--60\\% & 0.8pp & 3.4pp & 4.3$\\times$ \\\\\n60--90\\% & 1.6pp & 9.7pp & 6.1$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe decomposition achieves 81\\% prescriptive accuracy: when difficulty explains most of a language-layer combination's correctness variance, zero-shot transfer suffices; when the capability residual is large, \\caclr{} is needed.\n\n%------------------------------------------------------------------\n\\subsection{CaCLR Evaluation (Claim 3)}\n\\label{sec:res_caclr}\n%------------------------------------------------------------------\n\n\\paragraph{Full Comparison.}\nTable~\\ref{tab:caclr_full} compares \\caclr{} against all baselines, averaged across both architectures and 19 non-English languages. \\caclr{} achieves the highest AUROC (0.804) and lowest ECE (0.061) while requiring no target-language labels. It outperforms linear projection by 3.4pp AUROC and few-shot (100 labeled examples) by 4.2pp AUROC. The parameter overhead is minimal ($\\sim$1\\% additional probe parameters).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{\\caclr{} vs.\\ baselines (averaged across both architectures).}\n\\label{tab:caclr_full}\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & AUROC & ECE & Labels? & Overhead \\\\\n\\midrule\nZero-shot & .752 & .098 & no & 0 \\\\\nMean-shift & .747 & .102 & no & 0 \\\\\nLinear proj. & .770 & .082 & no & $d{\\times}d$ \\\\\nFew-shot (25) & .738 & .089 & yes (25) & 0 \\\\\nFew-shot (100) & .762 & .079 & yes (100) & 0 \\\\\n\\caclr{} & \\textbf{.804} & \\textbf{.061} & \\textbf{no} & $\\sim$1\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Ablation.}\nTable~\\ref{tab:ablation} shows the contribution of each \\caclr{} loss component. $\\mathcal{L}_\\text{consistency}$ provides the bulk of AUROC improvement (+4.1pp alone), while $\\mathcal{L}_\\text{SB\\text{-}ECE}$ contributes calibration refinement (ECE drops from 0.078 to 0.061 when added). The full objective achieves synergistic gains: 0.804 AUROC and 0.061 ECE, better than either auxiliary term alone.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Ablation of \\caclr{} loss components.}\n\\label{tab:ablation}\n\\begin{tabular}{lccc}\n\\toprule\nConfiguration & AUROC & ECE & $\\Delta$AUROC \\\\\n\\midrule\n$\\mathcal{L}_\\text{BCE}$ only & .752 & .098 & $-5.2$ \\\\\n$+ \\mathcal{L}_\\text{SB-ECE}$ & .768 & .072 & $-3.6$ \\\\\n$+ \\mathcal{L}_\\text{consistency}$ & .793 & .078 & $-1.1$ \\\\\nFull \\caclr{} & \\textbf{.804} & \\textbf{.061} & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Pareto Frontier Shift.}\nTable~\\ref{tab:pareto_shift} demonstrates the headline result: \\caclr{} shifts the Pareto frontier outward on Qwen3-235B. At layer 64, zero-shot transfer achieves 0.741 AUROC; \\caclr{} achieves 0.814---a 7.3pp improvement. The practical implication: \\caclr{} enables operating at deeper, better-calibrated layers without sacrificing cross-lingual transfer. The shifted Pareto frontier extends from L48 to L68, 2 layers deeper than the original frontier (L40--L60).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{\\caclr{} Pareto frontier shift (Qwen3-235B). Shifted Pareto layers marked ($\\bullet$).}\n\\label{tab:pareto_shift}\n\\begin{tabular}{rcccc}\n\\toprule\nLayer & ZS & \\caclr{} & $\\Delta$pp & Shifted \\\\\n\\midrule\n40 & .776 & .798 & 2.2 & \\\\\n44 & .774 & .800 & 2.6 & \\\\\n48 & .770 & .803 & 3.3 & $\\bullet$ \\\\\n52 & .765 & .806 & 4.1 & $\\bullet$ \\\\\n56 & .762 & .810 & 4.8 & $\\bullet$ \\\\\n60 & .753 & .814 & 6.1 & $\\bullet$ \\\\\n64 & .741 & .814 & 7.3 & $\\bullet$ \\\\\n68 & .728 & .808 & 8.0 & $\\bullet$ \\\\\n72 & .712 & .796 & 8.4 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe improvement pass rate across model--language pairs is 92\\% (35/38). The 3 non-improving pairs are high-resource languages on Llama~4~Scout where zero-shot transfer is already excellent and the consistency loss has minimal signal to exploit.\n\n\\paragraph{Low-Resource Performance.}\n\\caclr{} is especially effective for low-resource languages. On Qwen3: Swahili 0.731, Yoruba 0.709, Igbo 0.718 (vs.\\ zero-shot: 0.695, 0.672, 0.681). On Llama~4: Swahili 0.712, Yoruba 0.681, Igbo 0.698. All low-resource languages pass the 0.60 AUROC threshold for usable calibration.\n\n%------------------------------------------------------------------\n\\subsection{Cross-Lingual Orthogonality (Claim 4)}\n\\label{sec:res_ortho}\n%------------------------------------------------------------------\n\nTable~\\ref{tab:ortho} presents the correctness--confidence cosine similarity across all 20 languages and both architectures. The mean cosine is 0.052 (range: 0.018--0.094), well within the near-orthogonal regime ($<0.1$). Across all 40 language--architecture pairs, 39/40 fall below 0.1 (Yoruba on Llama~4 reaches 0.099).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Correctness--confidence cosine similarity by language. All values $<0.1$.}\n\\label{tab:ortho}\n\\begin{tabular}{llccc}\n\\toprule\nLanguage & Tier & Qwen3 & Llama4 & Mean \\\\\n\\midrule\nen & high & .031 & .037 & .034 \\\\\nzh & high & .035 & .041 & .038 \\\\\nde & high & .033 & .039 & .036 \\\\\nfr & high & .036 & .042 & .039 \\\\\nes & high & .038 & .044 & .041 \\\\\nja & high & .041 & .047 & .044 \\\\\nru & high & .040 & .046 & .043 \\\\\npt & high & .037 & .043 & .040 \\\\\nit & high & .039 & .045 & .042 \\\\\nnl & high & .034 & .040 & .037 \\\\\n\\midrule\nar & mid & .047 & .055 & .051 \\\\\nhi & mid & .051 & .059 & .055 \\\\\nko & mid & .045 & .053 & .049 \\\\\nvi & mid & .054 & .062 & .058 \\\\\nth & mid & .057 & .065 & .061 \\\\\nbn & mid & .052 & .060 & .056 \\\\\ntr & mid & .048 & .056 & .052 \\\\\n\\midrule\nsw & low & .073 & .083 & .078 \\\\\nyo & low & .089 & .099 & .094 \\\\\nig & low & .077 & .087 & .082 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe resource-tier gradient is notable: high-resource languages have mean cosine 0.041, mid-resource 0.054, and low-resource 0.074 (Spearman $\\rho=-0.68$ between resource tier and cosine). This suggests that output-based calibration methods are not just structurally limited but are \\emph{more} limited for well-resourced languages where the orthogonality is strongest. The cross-architecture consistency (Qwen3: 0.048, Llama~4: 0.057) confirms this is not architecture-specific (Table~\\ref{tab:ortho_summary}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Orthogonality summary statistics.}\n\\label{tab:ortho_summary}\n\\begin{tabular}{lccc}\n\\toprule\nStatistic & Qwen3 & Llama4 & Both \\\\\n\\midrule\nMean & 0.048 & 0.057 & 0.052 \\\\\nStd & 0.015 & 0.017 & 0.016 \\\\\nMax & 0.089 & 0.099 & 0.094 \\\\\nMin & 0.031 & 0.037 & 0.018 \\\\\nAll $<0.1$ & 20/20 & 19/20 & 39/40 \\\\\nTier corr.\\ $\\rho$ & $-0.71$ & $-0.65$ & $-0.68$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{Probe Complexity Analysis}\n\\label{sec:res_probe}\n%------------------------------------------------------------------\n\nTable~\\ref{tab:probe_complexity} compares logistic regression vs.\\ 2-layer MLP probes. MLPs gain 1.3pp English AUROC but lose 4.3pp in cross-lingual transfer. The transfer advantage of linear probes grows with depth: 2.1pp at shallow layers vs.\\ 6.8pp at deep layers. This confirms that deep-layer transfer degradation is driven by nonlinear, language-specific features that MLPs exploit but linear probes ignore. Linear probes are thus the correct choice for cross-lingual calibration transfer.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Probe complexity comparison (Qwen3-235B).}\n\\label{tab:probe_complexity}\n\\begin{tabular}{lcccc}\n\\toprule\nProbe & EN Best & ZS-19 & Drop & ECE \\\\\n\\midrule\nLogistic regression & .843 & .762 & 8.1pp & .054 \\\\\n2-layer MLP & .856 & .733 & 12.4pp & .068 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{Cross-Benchmark Generalization}\n\\label{sec:res_benchmark}\n%------------------------------------------------------------------\n\nTable~\\ref{tab:cross_bench} shows that \\caclr{} generalizes cleanly across benchmarks. The improvement magnitude is remarkably stable: 5.1--5.2pp AUROC gain and 33--40\\% ECE reduction across GlobalMMLU, Belebele (reading comprehension), and MMLU-ProX (harder MCQA). The cross-benchmark coefficient of variation for \\caclr{} improvement is 0.08, indicating the method addresses a fundamental representation alignment issue rather than overfitting to benchmark-specific patterns.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-benchmark generalization of \\caclr{}.}\n\\label{tab:cross_bench}\n\\begin{tabular}{lcccc}\n\\toprule\nBenchmark & ZS & \\caclr{} & $\\Delta$pp & ECE Red.\\% \\\\\n\\midrule\nGlobalMMLU & .752 & .804 & 5.2 & 39.7 \\\\\nBelebele & .738 & .789 & 5.1 & 36.2 \\\\\nMMLU-ProX & .722 & .774 & 5.2 & 33.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{Three-Architecture Validation}\n\\label{sec:res_three_arch}\n%------------------------------------------------------------------\n\nTable~\\ref{tab:three_arch} summarizes results across all three architectures, including Gemma~4~31B Dense. The best-transfer depth converges to 58--60\\% across dense and MoE architectures with 48--94 layers. \\caclr{} provides consistent 2.9--3.3pp improvement. The Pareto rank correlation is 0.82--0.88 in all cases. Dense vs.\\ MoE architecture makes minimal difference---the phenomenon is a property of transformer depth, not routing architecture.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Three-architecture summary. Transfer depth\\% = best cross-lingual transfer layer as percentage of total depth.}\n\\label{tab:three_arch}\n\\begin{tabular}{lcccccc}\n\\toprule\nModel & Type & $L$ & EN & ZS-19 & Depth\\% & $\\rho$ \\\\\n\\midrule\nQwen3-235B & MoE & 94 & .843 & .762 & 60 & .88 \\\\\nLlama 4 Scout & MoE & 48 & .821 & .741 & 58 & .82 \\\\\nGemma 4 31B & Dense & 60 & .812 & .734 & 60 & .86 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{Extended Language Coverage}\n\\label{sec:res_extended}\n%------------------------------------------------------------------\n\nTable~\\ref{tab:extended_langs} summarizes the extension to 52 languages. The resource-tier gradient is smooth: \\caclr{} gain increases from 3.0pp (high-resource) to 5.6pp (very-low-resource), confirming that the consistency loss provides most value where representation misalignment is worst. Zero-shot \\caclr{} transfer achieves $>$0.60 AUROC for 48/51 non-English languages, establishing practical usability across the vast majority of languages without any target-language labels.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Extended coverage (52 languages) by resource tier.}\n\\label{tab:extended_langs}\n\\begin{tabular}{lccccc}\n\\toprule\nTier & $n$ & ZS & \\caclr{} & $\\Delta$pp & $>$0.60 \\\\\n\\midrule\nHigh & 12 & .782 & .812 & 3.0 & 100\\% \\\\\nMid & 25 & .738 & .784 & 4.6 & 100\\% \\\\\nLow & 10 & .661 & .712 & 5.1 & 90\\% \\\\\nVery low & 4 & .582 & .638 & 5.6 & 50\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{INT8 Quantization Validation}\n\\label{sec:res_int8}\n%------------------------------------------------------------------\n\nTable~\\ref{tab:int8} validates that INT8 weight quantization (used for Llama~4~Scout) introduces negligible distortion. The maximum AUROC difference is 0.3pp, and the rank correlation between INT8 and FP16 layer rankings is 0.997. The Pareto frontier shape and ordering are perfectly preserved, confirming that our quantized results are reliable.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{INT8 vs.\\ FP16 validation (Llama~4~Scout, 5\\% subset).}\n\\label{tab:int8}\n\\begin{tabular}{rcccccc}\n\\toprule\nLayer & FP16 & INT8 & $\\Delta$ & FP16-ZS & INT8-ZS & $\\Delta$-ZS \\\\\n\\midrule\n8 & .674 & .672 & .2 & .661 & .658 & .3 \\\\\n16 & .747 & .745 & .2 & .731 & .728 & .3 \\\\\n24 & .788 & .786 & .2 & .747 & .744 & .3 \\\\\n32 & .812 & .810 & .2 & .734 & .731 & .3 \\\\\n40 & .820 & .817 & .3 & .691 & .687 & .4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\section{Discussion}\n\\label{sec:discussion}\n%------------------------------------------------------------------\n\n\\paragraph{Why CaCLR Works.}\nThe decomposition analysis (Section~\\ref{sec:res_decomp}) provides a mechanistic explanation. The consistency loss ($\\mathcal{L}_\\text{consistency}$) specifically targets the capability-specific component---the 32\\% of correctness variance that is language-dependent and drives 87\\% of transfer degradation. By forcing alignment of probe outputs across languages during training, \\caclr{} learns to extract language-invariant correctness features. This is strictly more powerful than post-hoc alignment (linear projection corrects first-order distributional mismatch but not nonlinear feature interactions).\n\n\\paragraph{Why Output-Based Methods Cannot Suffice.}\nThe orthogonality results (Section~\\ref{sec:res_ortho}) establish a structural limitation. With correctness and verbalized confidence directions nearly orthogonal across all 20 languages (mean cosine = 0.052), output-based methods---which operate on the confidence direction---cannot access correctness information regardless of language. The resource-tier gradient (stronger orthogonality for high-resource languages) further implies that improved multilingual training actually \\emph{widens} this structural gap.\n\n\\paragraph{Limitations.}\nOur evaluation is restricted to MCQA benchmarks where correctness is cleanly defined. Extension to open-ended generation requires different correctness labeling strategies. The consistency loss requires parallel or comparable cross-lingual activations, which limits applicability to settings where such data exists. We evaluate only logistic regression probes; nonlinear probes may yield different tradeoff curves.\n\n%------------------------------------------------------------------\n\\section{Conclusion}\n\\label{sec:conclusion}\n%------------------------------------------------------------------\n\nWe presented the first systematic study of cross-lingual probe-based calibration, testing whether the emerging research line on representation-level calibration extends beyond English. Our four findings form a causal chain: (1)~a depth-transferability Pareto frontier constrains all probe-based calibration transfer, converging to $\\sim$60\\% depth across three architectures; (2)~this frontier arises because capability-specific (not difficulty-shared) signals drive transfer degradation, especially at depth; (3)~\\caclr{} shifts this frontier outward, achieving $\\sim$40\\% ECE reduction over temperature scaling with zero target-language labels; and (4)~correctness--confidence orthogonality persists across all 20 languages, establishing output-based calibration as structurally limited regardless of language. Results extend to 52 languages and three benchmarks, confirming the generality of both the problem and our proposed solution.\n\n%------------------------------------------------------------------\n% References\n%------------------------------------------------------------------\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[\\protect\\citeauthoryear{Burns et al.}{2023}]{burns2023discovering}\nCollin Burns, Haotian Ye, Dan Klein, and Jacob Steinhardt.\n\\newblock Discovering latent knowledge in language models without supervision.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem[\\protect\\citeauthoryear{Marks et al.}{2024}]{marks2024geometry}\nSamuel Marks, Max Tegmark, et al.\n\\newblock The geometry of truth: Emergent linear structure in large language model representations of true/false datasets.\n\\newblock In \\emph{COLM}, 2024.\n\n\\bibitem[\\protect\\citeauthoryear{Miao et al.}{2026a}]{miao2026coral}\nShuo Miao et al.\n\\newblock {CORAL}: Cross-task correctness probes for LLM calibration.\n\\newblock 2026.\n\n\\bibitem[\\protect\\citeauthoryear{Miao and Ungar}{2026b}]{miao2026ortho}\nShuo Miao and Lyle Ungar.\n\\newblock Orthogonality of correctness and confidence directions in LLM representations.\n\\newblock 2026.\n\n\\bibitem[\\protect\\citeauthoryear{Xiao et al.}{2025}]{xiao2025knowledge}\nZhihao Xiao et al.\n\\newblock Cross-lingual knowledge boundary probe transfer.\n\\newblock In \\emph{ACL}, 2025.\n\n\\bibitem[\\protect\\citeauthoryear{Civelli et al.}{2025}]{civelli2025difficulty}\nAndrea Civelli et al.\n\\newblock Cross-lingual difficulty probe transfer in multilingual LLMs.\n\\newblock 2025.\n\n\\bibitem[\\protect\\citeauthoryear{Zhou et al.}{2024}]{zhou2024lace}\nXin Zhou et al.\n\\newblock {LACE}: Layer-adaptive calibration ensembles for multilingual LLMs.\n\\newblock 2024.\n\n\\bibitem[\\protect\\citeauthoryear{Gao et al.}{2024}]{gao2024quantization}\nLeo Gao et al.\n\\newblock Quantization effects on probing and representation analysis.\n\\newblock 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "1280f160-b2b0-4225-9b68-bf58250319cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T185641 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direct…",
  "leafUuid": "44815b61-43bc-4d3b-95df-2929123b3fe5",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete research paper for dream session",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75"
}
```

---

### Tool call

_source line 23 · 2026-05-20T19:27:02.825Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RUyJngGhmBRuERznQstxuT`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44815b61-43bc-4d3b-95df-2929123b3fe5",
  "isSidechain": false,
  "requestId": "req_011CbENUsanFrmWSnp4swpyT",
  "type": "assistant",
  "uuid": "17168052-f076-4a76-a1c8-2047e7dcae59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VxgFWznbTuTnQHLZspauas",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12108,
      "cache_read_input_tokens": 42607,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12108,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 42607,
          "cache_creation_input_tokens": 12108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12108
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

_source line 24 · 2026-05-20T19:27:03.024Z_

<details><summary>↩ Tool result · reported error · `toolu_01RUyJngGhmBRuERznQstxuT`</summary>

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
  "parentUuid": "17168052-f076-4a76-a1c8-2047e7dcae59",
  "isSidechain": false,
  "promptId": "907ecca9-b4a5-4dd2-af0b-6dcee3e5aad0",
  "type": "user",
  "uuid": "cd809711-1202-4de7-a63e-84d4eebdec79",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "17168052-f076-4a76-a1c8-2047e7dcae59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-20T19:27:05.842Z_

<details><summary>Logged reasoning block</summary>

```text
The acl.sty is not available. Let me switch to a standard article class instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd809711-1202-4de7-a63e-84d4eebdec79",
  "isSidechain": false,
  "requestId": "req_011CbENV8bRLquxf5cjLSuTQ",
  "type": "assistant",
  "uuid": "7532b0f5-51fb-4d21-a899-cd8da5966d70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AhyzwhPJwaq2DvuVKaUhbW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 464,
      "cache_read_input_tokens": 54715,
      "output_tokens": 461,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 464,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 461,
          "cache_read_input_tokens": 54715,
          "cache_creation_input_tokens": 464,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 464
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

_source line 26 · 2026-05-20T19:27:05.843Z_

ACL style not available. Switching to standard article class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7532b0f5-51fb-4d21-a899-cd8da5966d70",
  "isSidechain": false,
  "requestId": "req_011CbENV8bRLquxf5cjLSuTQ",
  "type": "assistant",
  "uuid": "f9c0bdb7-cd50-433c-812f-ebdcc7cf9c91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AhyzwhPJwaq2DvuVKaUhbW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 464,
      "cache_read_input_tokens": 54715,
      "output_tokens": 461,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 464,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 461,
          "cache_read_input_tokens": 54715,
          "cache_creation_input_tokens": 464,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 464
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

_source line 27 · 2026-05-20T19:27:09.370Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01BBFKwuAHmEsBv2XsKvi5k2`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{microtype}\n\\usepackage{array}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{hyperref}\n\\usepackage{microtype}\n\\usepackage{array}\n\\usepackage{natbib}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9c0bdb7-cd50-433c-812f-ebdcc7cf9c91",
  "isSidechain": false,
  "requestId": "req_011CbENV8bRLquxf5cjLSuTQ",
  "type": "assistant",
  "uuid": "21244278-b65d-48fb-8e56-f24f5ed69f90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AhyzwhPJwaq2DvuVKaUhbW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 464,
      "cache_read_input_tokens": 54715,
      "output_tokens": 461,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 464,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 461,
          "cache_read_input_tokens": 54715,
          "cache_creation_input_tokens": 464,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 464
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

_source line 28 · 2026-05-20T19:27:09.393Z_

<details><summary>↩ Tool result · `toolu_01BBFKwuAHmEsBv2XsKvi5k2`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21244278-b65d-48fb-8e56-f24f5ed69f90",
  "isSidechain": false,
  "promptId": "907ecca9-b4a5-4dd2-af0b-6dcee3e5aad0",
  "type": "user",
  "uuid": "e08f8cd0-1954-4c35-9951-19e37e357200",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{microtype}\n\\usepackage{array}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{hyperref}\n\\usepackage{microtype}\n\\usepackage{array}\n\\usepackage{natbib}",
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
        "oldStart": 9,
        "oldLines": 8,
        "newStart": 9,
        "newLines": 10,
        "lines": [
          " \\usepackage{multirow}",
          " \\usepackage{xcolor}",
          " \\usepackage{url}",
          "+\\usepackage{hyperref}",
          " \\usepackage{microtype}",
          " \\usepackage{array}",
          "+\\usepackage{natbib}",
          " ",
          " \\newcommand{\\caclr}{\\textsc{CaCLR}}",
          " \\newcommand{\\ece}{\\text{ECE}}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "21244278-b65d-48fb-8e56-f24f5ed69f90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-20T19:27:09.424Z_

```json
{
  "parentUuid": "e08f8cd0-1954-4c35-9951-19e37e357200",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "d856221e-7850-41ca-98d7-6d3ab50b69c0",
  "timestamp": "2026-05-20T19:27:09.424Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-20T19:27:12.767Z_

<details open><summary>🔧 Tool call — Edit · `toolu_011XfsaQMojggaazcM8Wqf7J`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.tex",
  "old_string": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
  "new_string": "%\\bibliography{references}\n%\\bibliographystyle{acl_natbib}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d856221e-7850-41ca-98d7-6d3ab50b69c0",
  "isSidechain": false,
  "requestId": "req_011CbENVbzwMPGzMqGcLiFSa",
  "type": "assistant",
  "uuid": "f232e65d-bf3c-47a8-abbe-9e15aab57473",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnJBUb5Q1377b9wxz9Tofz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 55179,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 652,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 176,
          "cache_read_input_tokens": 55179,
          "cache_creation_input_tokens": 652,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 652
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

_source line 31 · 2026-05-20T19:27:12.778Z_

<details><summary>↩ Tool result · `toolu_011XfsaQMojggaazcM8Wqf7J`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f232e65d-bf3c-47a8-abbe-9e15aab57473",
  "isSidechain": false,
  "promptId": "907ecca9-b4a5-4dd2-af0b-6dcee3e5aad0",
  "type": "user",
  "uuid": "069860e3-50e2-4704-9548-48fbad977db9",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.tex",
    "oldString": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
    "newString": "%\\bibliography{references}\n%\\bibliographystyle{acl_natbib}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 586,
        "oldLines": 8,
        "newStart": 586,
        "newLines": 8,
        "lines": [
          " %------------------------------------------------------------------",
          " % References",
          " %------------------------------------------------------------------",
          "-\\bibliography{references}",
          "-\\bibliographystyle{acl_natbib}",
          "+%\\bibliography{references}",
          "+%\\bibliographystyle{acl_natbib}",
          " ",
          " \\begin{thebibliography}{20}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "f232e65d-bf3c-47a8-abbe-9e15aab57473",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T19:27:16.093Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WdNvKZCetyLZ2pL6Qi2qA8`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "069860e3-50e2-4704-9548-48fbad977db9",
  "isSidechain": false,
  "requestId": "req_011CbENVrWowpB6B3bVmctqT",
  "type": "assistant",
  "uuid": "94ef7531-4061-428d-bfd3-b2aaaf1bb06e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8LtPUM45m2whjNU6az1ci",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 263,
      "cache_read_input_tokens": 55831,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 263,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 55831,
          "cache_creation_input_tokens": 263,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 263
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

_source line 33 · 2026-05-20T19:27:17.490Z_

<details><summary>↩ Tool result · `toolu_01WdNvKZCetyLZ2pL6Qi2qA8`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)
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
(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty
(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def
(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty
(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.sty
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype-pdftex.def)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-ptm.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-cmr.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msa.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msb.cfg)

Package natbib Warning: Citation `burns2023discovering' on page 1 undefined on 
input line 44.


Package natbib Warning: Citation `marks2024geometry' on page 1 undefined on inp
ut line 44.


Package natbib Warning: Citation `miao2026coral' on page 1 undefined on input l
ine 44.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]

LaTeX Warning: Reference `sec:caclr' on page 2 undefined on input line 93.

[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [3]

LaTeX Warning: Reference `tab:pareto_qwen3' on page 4 undefined on input line 1
53.


LaTeX Warning: Reference `tab:transfer_conditions' on page 4 undefined on input
 line 195.

[4]

LaTeX Warning: Reference `tab:pareto_llama4' on page 5 undefined on input line 
217.


LaTeX Warning: Reference `tab:cross_arch' on page 5 undefined on input line 245
.


LaTeX Warning: Reference `tab:decomp' on page 5 undefined on input line 270.


LaTeX Warning: Reference `tab:decomp_depth' on page 5 undefined on input line 2
88.

[5]

LaTeX Warning: Reference `tab:caclr_full' on page 6 undefined on input line 314
.


LaTeX Warning: Reference `tab:ablation' on page 6 undefined on input line 336.


LaTeX Warning: Reference `tab:pareto_shift' on page 6 undefined on input line 3
56.


LaTeX Warning: Reference `tab:ortho' on page 6 undefined on input line 390.

[6]

LaTeX Warning: Reference `tab:ortho_summary' on page 7 undefined on input line 
427.


LaTeX Warning: Reference `tab:probe_complexity' on page 7 undefined on input li
ne 453.


LaTeX Warning: Reference `tab:cross_bench' on page 7 undefined on input line 47
5.


LaTeX Warning: Reference `tab:three_arch' on page 7 undefined on input line 498
.


LaTeX Warning: Reference `tab:extended_langs' on page 7 undefined on input line
 521.

[7]

LaTeX Warning: Reference `tab:int8' on page 8 undefined on input line 545.


LaTeX Warning: Reference `sec:res_decomp' on page 8 undefined on input line 571
.


LaTeX Warning: Reference `sec:res_ortho' on page 8 undefined on input line 574.


[8] [9]

Package natbib Warning: There were undefined citations.

[10] [11] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur
w/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 148204 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)
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
(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty
(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def
(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty
(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.sty
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype-pdftex.def)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-ptm.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-cmr.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msa.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msb.cfg) [1{/var/lib/texm
f/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/d
vips/base/8r.enc}] [2]
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [3] [4] [5] [6]
[7] [8] [9] [10] [11] (./paper.aux) )&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 150085 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94ef7531-4061-428d-bfd3-b2aaaf1bb06e",
  "isSidechain": false,
  "promptId": "907ecca9-b4a5-4dd2-af0b-6dcee3e5aad0",
  "type": "user",
  "uuid": "1a2ebb41-3c7e-4416-98c6-04c6dcd6bf72",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.sty\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype-pdftex.def)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-ptm.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-cmr.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msa.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msb.cfg)\n\nPackage natbib Warning: Citation `burns2023discovering' on page 1 undefined on \ninput line 44.\n\n\nPackage natbib Warning: Citation `marks2024geometry' on page 1 undefined on inp\nut line 44.\n\n\nPackage natbib Warning: Citation `miao2026coral' on page 1 undefined on input l\nine 44.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n\nLaTeX Warning: Reference `sec:caclr' on page 2 undefined on input line 93.\n\n[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [3]\n\nLaTeX Warning: Reference `tab:pareto_qwen3' on page 4 undefined on input line 1\n53.\n\n\nLaTeX Warning: Reference `tab:transfer_conditions' on page 4 undefined on input\n line 195.\n\n[4]\n\nLaTeX Warning: Reference `tab:pareto_llama4' on page 5 undefined on input line \n217.\n\n\nLaTeX Warning: Reference `tab:cross_arch' on page 5 undefined on input line 245\n.\n\n\nLaTeX Warning: Reference `tab:decomp' on page 5 undefined on input line 270.\n\n\nLaTeX Warning: Reference `tab:decomp_depth' on page 5 undefined on input line 2\n88.\n\n[5]\n\nLaTeX Warning: Reference `tab:caclr_full' on page 6 undefined on input line 314\n.\n\n\nLaTeX Warning: Reference `tab:ablation' on page 6 undefined on input line 336.\n\n\nLaTeX Warning: Reference `tab:pareto_shift' on page 6 undefined on input line 3\n56.\n\n\nLaTeX Warning: Reference `tab:ortho' on page 6 undefined on input line 390.\n\n[6]\n\nLaTeX Warning: Reference `tab:ortho_summary' on page 7 undefined on input line \n427.\n\n\nLaTeX Warning: Reference `tab:probe_complexity' on page 7 undefined on input li\nne 453.\n\n\nLaTeX Warning: Reference `tab:cross_bench' on page 7 undefined on input line 47\n5.\n\n\nLaTeX Warning: Reference `tab:three_arch' on page 7 undefined on input line 498\n.\n\n\nLaTeX Warning: Reference `tab:extended_langs' on page 7 undefined on input line\n 521.\n\n[7]\n\nLaTeX Warning: Reference `tab:int8' on page 8 undefined on input line 545.\n\n\nLaTeX Warning: Reference `sec:res_decomp' on page 8 undefined on input line 571\n.\n\n\nLaTeX Warning: Reference `sec:res_ortho' on page 8 undefined on input line 574.\n\n\n[8] [9]\n\nPackage natbib Warning: There were undefined citations.\n\n[10] [11] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur\nw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 148204 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.sty\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype-pdftex.def)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-ptm.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-cmr.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msa.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msb.cfg) [1{/var/lib/texm\nf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/d\nvips/base/8r.enc}] [2]\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [3] [4] [5] [6]\n[7] [8] [9] [10] [11] (./paper.aux) )&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\nonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 150085 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "94ef7531-4061-428d-bfd3-b2aaaf1bb06e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T185641 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direct…",
  "leafUuid": "1a2ebb41-3c7e-4416-98c6-04c6dcd6bf72",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete research paper for dream session",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75"
}
```

---

### Assistant

_source line 36 · 2026-05-20T19:27:24.683Z_

PDF 编译成功，11 页，150KB。输出位于 `best/paper.tex` → `best/paper.pdf`。

论文覆盖了 `experiment_data.json` 中全部 8 个实验（Tables 1–15 + Table S1），按 4-claim 因果链组织：Pareto Frontier 发现 → Difficulty-Capability 分解 → CaCLR 方法 → 正交性机制解释，外加 probe complexity、cross-benchmark、three-architecture、extended language、INT8 validation 各有独立小节和表格。所有数字均取自 JSON 数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a2ebb41-3c7e-4416-98c6-04c6dcd6bf72",
  "isSidechain": false,
  "requestId": "req_011CbENWCS8CwWusfUhjawC1",
  "type": "assistant",
  "uuid": "ae95e163-89a1-4561-bbad-cdcbad6f5870",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJ6svfv8dLzVyLt1o8a6Hb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6227,
      "cache_read_input_tokens": 56094,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 56094,
          "cache_creation_input_tokens": 6227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6227
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

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T185641 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direct…",
  "leafUuid": "ae95e163-89a1-4561-bbad-cdcbad6f5870",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete research paper for dream session",
  "sessionId": "30326c6e-1574-480d-ae02-912541994f75"
}
```

---
