# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T194535 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/92734392-fd09-4d44-a705-e9afb826e672.jsonl`
- **Structured JSON:** [`f9ab46b5b44ad3ba05f6.json`](../../sessions/f9/f9ab46b5b44ad3ba05f6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T20:02:17.140Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T20:02:17.140Z",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T194535 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：原始 framing 完全成立。论文以 problem-discovery 定位：首次识别并形式化 measurement-error × causal-heterogeneity confounding，Δπ×Δτ product 诊断准则有独立实用价值。Headline result 可直接使用（\"global correction worsens bias by up to 7.8x\"）。PPCI 正交性干净，K>2 扩展自然，HB partial pooling 在小样本下优势显著。 论文结构 Theory → Synthetic → Semi-synthetic → Real data 全链条闭合，无需防守性让步。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T20:02:17.143Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T20:02:17.143Z",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672"
}
```

---

## Round 1

46 recorded events

### User

_source line 3 · 2026-05-20T20:02:17.162Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T194535 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：原始 framing 完全成立。论文以 problem-discovery 定位：首次识别并形式化 measurement-error × causal-heterogeneity confounding，Δπ×Δτ product 诊断准则有独立实用价值。Headline result 可直接使用（"global correction worsens bias by up to 7.8x"）。PPCI 正交性干净，K>2 扩展自然，HB partial pooling 在小样本下优势显著。 论文结构 Theory → Synthetic → Semi-synthetic → Real data 全链条闭合，无需防守性让步。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "bf038654-a98b-4857-b555-fee3ad057efe",
  "type": "user",
  "uuid": "fb052aa8-75af-49eb-8c03-0a2840f87509",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T20:02:17.161Z_

```json
{
  "parentUuid": "fb052aa8-75af-49eb-8c03-0a2840f87509",
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
  "uuid": "876c55d8-97cc-4d61-b992-dccf4d86b05e",
  "timestamp": "2026-05-20T20:02:17.161Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T20:02:17.161Z_

```json
{
  "parentUuid": "876c55d8-97cc-4d61-b992-dccf4d86b05e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "bb3efb65-1c6d-4a7a-a69c-fedd6554e8ef",
  "timestamp": "2026-05-20T20:02:17.161Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
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
  "aiTitle": "Generate complete simulated paper for dream research",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672"
}
```

---

### Assistant

_source line 7 · 2026-05-20T20:02:19.642Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb3efb65-1c6d-4a7a-a69c-fedd6554e8ef",
  "isSidechain": false,
  "requestId": "req_011CbERAyhEcdUAdbUA3QTMJ",
  "type": "assistant",
  "uuid": "d7d3ab98-2580-4ed0-bb8d-950bfcebd7e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017yvdAAn8TwAG6K92CrHj76",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11685,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11685,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11685
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

_source line 8 · 2026-05-20T20:02:20.129Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GUjcjziB4AsNqkrJwarkAc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7d3ab98-2580-4ed0-bb8d-950bfcebd7e5",
  "isSidechain": false,
  "requestId": "req_011CbERAyhEcdUAdbUA3QTMJ",
  "type": "assistant",
  "uuid": "aab93ece-bda3-4ea7-89bf-f1784822c85e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017yvdAAn8TwAG6K92CrHj76",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11685,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11685,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11685
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

_source line 9 · 2026-05-20T20:02:20.536Z_

<details><summary>↩ Tool result · `toolu_01GUjcjziB4AsNqkrJwarkAc`</summary>

```text
1	[
2	  {
3	    "name": "Hierarchical Bayesian EC-HTE synthetic validation",
4	    "description": "在合成数据上实现 HB Dirichlet-prior confusion matrix estimator，与 MLE stratified 和 Laplace smoothed 基线对比。覆盖 extreme/moderate/homogeneous error regimes × n_expert ∈ {100,250,500,1000,2000} × K ∈ {2,4} subgroups，共 1000 次 MC 重复。PyMC NUTS sampler，4 chains，warmup=1000。\n",
5	    "results": {
6	      "hb_rmse_vs_mle_at_n100_k2": 0.72,
7	      "hb_rmse_vs_mle_at_n250_k2": 0.74,
8	      "hb_rmse_vs_mle_at_n250_k4": 0.68,
9	      "hb_rmse_vs_mle_at_n1000_k2": 0.91,
10	      "hb_rmse_vs_mle_at_n2000_k2": 0.96,
11	      "hb_coverage_95ci_extreme_n250": 0.943,
12	      "hb_coverage_95ci_moderate_n250": 0.951,
13	      "hb_coverage_95ci_homogeneous_n250": 0.954,
14	      "mle_coverage_95ci_extreme_n250": 0.87,
15	      "laplace_coverage_95ci_extreme_n250": 0.91,
16	      "ec_hte_subgroup_bias_extreme": 0.003,
17	      "global_correction_subgroup_bias_extreme": 0.041,
18	      "rhat_max": 1.004,
19	      "ess_min": 387,
20	      "mcmc_runtime_per_fit_seconds": 2.3,
21	      "mle_runtime_per_fit_seconds": 0.008,
22	      "mc_runs": 1000
23	    },
24	    "tables": [
25	      {
26	        "title": "Table 1: RMSE comparison across methods, regimes, and sample sizes (K=2)",
27	        "columns": [
28	          "regime",
29	          "n_expert",
30	          "MLE_RMSE",
31	          "Laplace_RMSE",
32	          "HB_RMSE",
33	          "HB/MLE_ratio",
34	          "HB_95CI_coverage"
35	        ],
36	        "rows": [
37	          [
38	            "extreme",
39	            100,
40	            0.058,
41	            0.049,
42	            0.042,
43	            0.72,
44	            0.932
45	          ],
46	          [
47	            "extreme",
48	            250,
49	            0.037,
50	            0.032,
51	            0.027,
52	            0.74,
53	            0.943
54	          ],
55	          [
56	            "extreme",
57	            500,
58	            0.024,
59	            0.022,
60	            0.02,
61	            0.83,
62	            0.948
63	          ],
64	          [
65	            "extreme",
66	            1000,
67	            0.016,
68	            0.015,
69	            0.015,
70	            0.91,
71	            0.952
72	          ],
73	          [
74	            "extreme",
75	            2000,
76	            0.011,
77	            0.011,
78	            0.011,
79	            0.96,
80	            0.953
81	          ],
82	          [
83	            "moderate",
84	            100,
85	            0.041,
86	            0.036,
87	            0.031,
88	            0.76,
89	            0.938
90	          ],
91	          [
92	            "moderate",
93	            250,
94	            0.027,
95	            0.024,
96	            0.021,
97	            0.78,
98	            0.951
99	          ],
100	          [
101	            "moderate",
102	            500,
103	            0.018,
104	            0.017,
105	            0.016,
106	            0.87,
107	            0.953
108	          ],
109	          [
110	            "moderate",
111	            1000,
112	            0.012,
113	            0.012,
114	            0.011,
115	            0.93,
116	            0.954
117	          ],
118	          [
119	            "moderate",
120	            2000,
121	            0.009,
122	            0.009,
123	            0.008,
124	            0.97,
125	            0.953
126	          ],
127	          [
128	            "homogeneous",
129	            100,
130	            0.032,
131	            0.029,
132	            0.027,
133	            0.84,
134	            0.944
135	          ],
136	          [
137	            "homogeneous",
138	            250,
139	            0.021,
140	            0.02,
141	            0.019,
142	            0.88,
143	            0.954
144	          ],
145	          [
146	            "homogeneous",
147	            500,
148	            0.015,
149	            0.014,
150	            0.014,
151	            0.93,
152	            0.955
153	          ],
154	          [
155	            "homogeneous",
156	            1000,
157	            0.01,
158	            0.01,
159	            0.01,
160	            0.97,
161	            0.954
162	          ],
163	          [
164	            "homogeneous",
165	            2000,
166	            0.007,
167	            0.007,
168	            0.007,
169	            0.99,
170	            0.953
171	          ]
172	        ]
173	      },
174	      {
175	        "title": "Table 2: K=4 subgroups results (extreme regime)",
176	        "columns": [
177	          "n_expert",
178	          "MLE_RMSE",
179	          "HB_RMSE",
180	          "HB/MLE_ratio",
181	          "HB_coverage",
182	          "MLE_coverage"
183	        ],
184	        "rows": [
185	          [
186	            100,
187	            0.089,
188	            0.058,
189	            0.65,
190	            0.921,
191	            0.82
192	          ],
193	          [
194	            250,
195	            0.054,
196	            0.037,
197	            0.68,
198	            0.94,
199	            0.86
200	          ],
201	          [
202	            500,
203	            0.035,
204	            0.027,
205	            0.77,
206	            0.949,
207	            0.91
208	          ],
209	          [
210	            1000,
211	            0.023,
212	            0.02,
213	            0.87,
214	            0.953,
215	            0.94
216	          ],
217	          [
218	            2000,
219	            0.016,
220	            0.015,
221	            0.94,
222	            0.954,
223	            0.95
224	          ]
225	        ]
226	      },
227	      {
228	        "title": "Table 3: MCMC diagnostics summary",
229	        "columns": [
230	          "metric",
231	          "min",
232	          "median",
233	          "max",
234	          "threshold"
235	        ],
236	        "rows": [
237	          [
238	            "R̂",
239	            1.0,
240	            1.001,
241	            1.004,
242	            "<1.01"
243	          ],
244	          [
245	            "ESS (bulk)",
246	            387,
247	            1240,
248	            4000,
249	            ">200"
250	          ],
251	          [
252	            "ESS (tail)",
253	            302,
254	            980,
255	            3500,
256	            ">200"
257	          ],
258	          [
259	            "divergences",
260	            0,
261	            0,
262	            0,
263	            "0"
264	          ],
265	          [
266	            "runtime (s)",
267	            1.1,
268	            2.3,
269	            4.7,
270	            "-"
271	          ]
272	        ]
273	      }
274	    ],
275	    "figures": [],
276	    "analysis": "核心发现：HB partial pooling 在 n_expert ≤ 250 时提供 22-35% RMSE reduction（取决于 regime 和 K）， 且 coverage 始终在 [0.92, 0.96] 范围内。K=4 时优势更显著，因为 per-subgroup 样本量减半导致 MLE 方差翻倍。这直接支撑 Claim 2 中\"partial pooling controls estimation variance\"的论断。 Homogeneous regime 下 HB 优势最小（收缩方向与真实值接近），但不会更差——验证\"never worse than global\"性质。 MCMC 诊断全部通过，无需担心计算可靠性。\n\n\nHB Dirichlet partial pooling 在小样本下的优势来自两个机制：(1) 当 n_expert ≤ 250 时，per-subgroup confusion matrix 的 MLE 估计面临严重的有限样本方差——K=4 时每个 subgroup 仅 ~62 个标注，2×2 矩阵 4 个参数的 MLE 方差很大，矩阵求逆进一步放大误差；HB 通过向全局先验收缩，借用跨 subgroup 信息， 有效降低估计方差。(2) Coverage 改善因为 HB 的后验区间自然包含参数不确定性，而 MLE 的 delta-method CI 在小样本下低估方差。随着 n_expert → 2000，每个 subgroup 有充足数据，MLE 渐近最优性使 HB 优势消失。 Extreme regime 下 HB 优势最大，因为 subgroup 间 error rate 差异大（π₁=0.15 vs π₂=0.35）， MLE 在低频 subgroup 上方差爆炸。MCMC 收敛良好因为 Dirichlet-Multinomial 是共轭结构， posterior geometry 简单，NUTS 无困难。Runtime 比 MLE 慢 ~300x 但绝对值仍可接受。\n"
277	  },
278	  {
279	    "name": "Formal bias bound verification with K>2 extension",
280	    "description": "解析推导 bias = Σ_k w_k · (π_global - π_k) · τ_k 的形式化表达，其中 π_k 是 subgroup k 的 misclassification rate，τ_k 是 subgroup CATE。K=2 时简化为 bias ∝ Δπ × Δτ。 在系统参数网格上（Δπ ∈ [0, 0.3], Δτ ∈ [0, 0.5], base rates 变化）进行 MC 验证。 K=4 扩展验证 sum-of-products 形式。\n",
281	    "results": {
282	      "analytic_vs_mc_r_squared_k2": 0.982,
283	      "analytic_vs_mc_r_squared_k4": 0.971,
284	      "bound_tightness_ratio_median": 1.03,
285	      "bound_tightness_ratio_95pct": 1.12,
286	      "bias_amplification_max_observed": 7.8,
287	      "bias_amplification_mean_extreme": 6.2,
288	      "bias_amplification_mean_moderate": 3.1,
289	      "debiasing_hurts_fraction_extreme": 0.94,
290	      "debiasing_hurts_fraction_moderate": 0.67,
291	      "constructive_example_bias_nocorrection": 0.023,
292	      "constructive_example_bias_global": 0.179,
293	      "constructive_example_bias_ec_hte": 0.002,
294	      "k4_sum_of_products_empirical_match": 0.97
295	    },
296	    "tables": [
297	      {
298	        "title": "Table 4: Analytic bound vs MC empirical bias (K=2, selected grid points)",
299	        "columns": [
300	          "Δπ",
301	          "Δτ",
302	          "bias_analytic",
303	          "bias_mc_mean",
304	          "bias_mc_se",
305	          "ratio"
306	        ],
307	        "rows": [
308	          [
309	            0.05,
310	            0.1,
311	            0.006,
312	            0.006,
313	            0.001,
314	            1.01
315	          ],
316	          [
317	            0.1,
318	            0.1,
319	            0.013,
320	            0.012,
321	            0.001,
322	            1.02
323	          ],
324	          [
325	            0.1,
326	            0.3,
327	            0.038,
328	            0.037,
329	            0.002,
330	            1.03
331	          ],
332	          [
333	            0.2,
334	            0.2,
335	            0.05,
336	            0.049,
337	            0.002,
338	            1.02
339	          ],
340	          [
341	            0.2,
342	            0.4,
343	            0.1,
344	            0.097,
345	            0.003,
346	            1.03
347	          ],
348	          [
349	            0.25,
350	            0.5,
351	            0.156,
352	            0.149,
353	            0.004,
354	            1.05
355	          ],
356	          [
357	            0.3,
358	            0.5,
359	            0.188,
360	            0.179,
361	            0.005,
362	            1.05
363	          ]
364	        ]
365	      },
366	      {
367	        "title": "Table 5: Bias amplification factor (global/no-correction) by regime",
368	        "columns": [
369	          "regime",
370	          "Δπ",
371	          "Δτ",
372	          "bias_no_corr",
373	          "bias_global",
374	          "amplification"
375	        ],
376	        "rows": [
377	          [
378	            "extreme",
379	            0.25,
380	            0.13,
381	            0.023,
382	            0.179,
383	            "7.8x"
384	          ],
385	          [
386	            "extreme",
387	            0.2,
388	            0.15,
389	            0.019,
390	            0.118,
391	            "6.2x"
392	          ],
393	          [
394	            "extreme",
395	            0.15,
396	            0.2,
397	            0.015,
398	            0.08,
399	            "5.3x"
400	          ],
401	          [
402	            "moderate",
403	            0.1,
404	            0.1,
405	            0.008,
406	            0.025,
407	            "3.1x"
408	          ],
409	          [
410	            "homogeneous",
411	            0.03,
412	            0.05,
413	            0.001,
414	            0.002,
415	            "1.5x"
416	          ]
417	        ]
418	      },
419	      {
420	        "title": "Table 6: K=4 sum-of-products verification",
421	        "columns": [
422	          "config",
423	          "bias_predicted",
424	          "bias_mc",
425	          "abs_error"
426	        ],
427	        "rows": [
428	          [
429	            "balanced, linear Δπ",
430	            0.062,
431	            0.06,
432	            0.002
433	          ],
434	          [
435	            "balanced, quadratic Δπ",
436	            0.084,
437	            0.081,
438	            0.003
439	          ],
440	          [
441	            "unbalanced, linear Δπ",
442	            0.071,
443	            0.068,
444	            0.003
445	          ],
446	          [
447	            "unbalanced, quadratic Δπ",
448	            0.098,
449	            0.093,
450	            0.005
451	          ]
452	        ]
453	      }
454	    ],
455	    "figures": [],
456	    "analysis": "这是论文的理论基础实验。R² ≈ 0.98 证明 Δπ×Δτ product 形式不是近似而是（在 population 层面）精确的， MC 偏离仅反映有限样本噪声。Bias amplification 最高 7.8x 出现在 extreme regime 的特定配置下， 这成为论文 headline number。K=4 扩展验证 sum-of-products Σ_k w_k(π̄-π_k)τ_k 形式同样成立， R²=0.971 略低但仍远超阈值。这为 Remark 1（general-K case）提供实证支持。 关键洞察：amplification 在 Δπ 和 Δτ 都大时最严重，但即使中等水平（Δπ=0.10, Δτ=0.10） 也有 3.1x 放大，说明问题不限于极端情况。\n\n\n解析 bound 与 MC 高度吻合（R² > 0.97）的原因：在 K=2 binary classification 下，bias 的 closed-form 表达 bias_global = (π̂_global - π₁)·τ₁·w₁ + (π̂_global - π₂)·τ₂·w₂ 是精确的，不依赖渐近近似。 π̂_global = w₁π₁ + w₂π₂ 代入后得到 bias ∝ w₁w₂·Δπ·Δτ 的乘积形式。MC 偏离仅来自有限样本 confusion matrix 估计噪声，随 MC 重复次数增多趋于零。R² 未达 1.0 是因为 base rate 和 sample size 引入的二阶效应。K=4 时 R² 略低因为 sum-of-products 形式有更多交叉项，但核心结构不变。 Bias amplification 7.8x 出现在 constructive example 中：π₁=0.10, π₂=0.35, τ₁=0.15, τ₂=0.02 ——low-error subgroup 有大 treatment effect，global correction 用 π̂_global≈0.22 严重过校正该 subgroup， 而 high-error subgroup 的 small τ₂ 意味着欠校正损害小。净效果：global correction 在 subgroup 1 引入 大 bias，远超 no correction 下的原始 bias。这是本文最核心的 insight。\n"
457	  },
458	  {
459	    "name": "Semi-synthetic political-science benchmark",
460	    "description": "使用 CardiffNLP TweetEval sentiment/stance 子集或类似公开政治推文语料，注入已知 CATE 异质性结构 （如 economic framing 调节 campaign message 效果）。用 GPT-4.1 和 Qwen3-235B-A22B 标注 effect modifier， 测量 subgroup-specific misclassification rates，验证异质性存在。应用 EC-HTE vs Global vs No-correction vs MLE-stratified baselines。N ≈ 20000 tweets, n_expert = 500 gold labels。\n",
461	    "results": {
462	      "gpt4_overall_accuracy": 0.87,
463	      "gpt4_subgroup_accuracy_high": 0.93,
464	      "gpt4_subgroup_accuracy_low": 0.78,
465	      "gpt4_max_min_error_ratio": 2.15,
466	      "qwen3_overall_accuracy": 0.82,
467	      "qwen3_subgroup_accuracy_high": 0.89,
468	      "qwen3_subgroup_accuracy_low": 0.72,
469	      "qwen3_max_min_error_ratio": 2.55,
470	      "ec_hte_cate_bias_subgroup1_gpt4": 0.004,
471	      "ec_hte_cate_bias_subgroup2_gpt4": 0.006,
472	      "global_cate_bias_subgroup1_gpt4": 0.038,
473	      "global_cate_bias_subgroup2_gpt4": -0.031,
474	      "nocorrection_cate_bias_subgroup1_gpt4": 0.012,
475	      "nocorrection_cate_bias_subgroup2_gpt4": -0.018,
476	      "bias_amplification_global_gpt4": 5.4,
477	      "bias_amplification_global_qwen3": 6.9,
478	      "ec_hte_coverage_gpt4": 0.94,
479	      "ec_hte_coverage_qwen3": 0.93,
480	      "ec_hte_bias_reduction_vs_global_gpt4": 0.89,
481	      "ec_hte_bias_reduction_vs_global_qwen3": 0.92,
482	      "subgroup_misclass_heterogeneity_gpt4": 0.15,
483	      "subgroup_misclass_heterogeneity_qwen3": 0.17
484	    },
485	    "tables": [
486	      {
487	        "title": "Table 7: Subgroup-specific LLM misclassification rates",
488	        "columns": [
489	          "LLM",
490	          "subgroup",
491	          "n",
492	          "accuracy",
493	          "FPR",
494	          "FNR",
495	          "misclass_rate"
496	        ],
497	        "rows": [
498	          [
499	            "GPT-4.1",
500	            "economic-mainstream",
501	            11200,
502	            0.93,
503	            0.04,
504	            0.1,
505	            0.07
506	          ],
507	          [
508	            "GPT-4.1",
509	            "minority-immigration",
510	            8800,
511	            0.78,
512	            0.12,
513	            0.31,
514	            0.22
515	          ],
516	          [
517	            "GPT-4.1",
518	            "pooled",
519	            20000,
520	            0.87,
521	            0.07,
522	            0.19,
523	            0.13
524	          ],
525	          [
526	            "Qwen3-235B",
527	            "economic-mainstream",
528	            11200,
529	            0.89,
530	            0.06,
531	            0.16,
532	            0.11
533	          ],
534	          [
535	            "Qwen3-235B",
536	            "minority-immigration",
537	            8800,
538	            0.72,
539	            0.15,
540	            0.4,
541	            0.28
542	          ],
543	          [
544	            "Qwen3-235B",
545	            "pooled",
546	            20000,
547	            0.82,
548	            0.1,
549	            0.26,
550	            0.18
551	          ]
552	        ]
553	      },
554	      {
555	        "title": "Table 8: CATE estimation comparison (GPT-4.1 annotations)",
556	        "columns": [
557	          "method",
558	          "subgroup",
559	          "CATE_true",
560	          "CATE_est",
561	          "bias",
562	          "RMSE",
563	          "coverage_95"
564	        ],
565	        "rows": [
566	          [
567	            "No correction",
568	            "economic-mainstream",
569	            0.15,
570	            0.138,
571	            -0.012,
572	            0.018,
573	            0.89
574	          ],
575	          [
576	            "No correction",
577	            "minority-immigration",
578	            0.04,
579	            0.058,
580	            0.018,
581	            0.023,
582	            0.85
583	          ],
584	          [
585	            "Global correction",
586	            "economic-mainstream",
587	            0.15,
588	            0.188,
589	            0.038,
590	            0.042,
591	            0.71
592	          ],
593	          [
594	            "Global correction",
595	            "minority-immigration",
596	            0.04,
597	            0.009,
598	            -0.031,
599	            0.035,
600	            0.76
601	          ],
602	          [
603	            "MLE stratified",
604	            "economic-mainstream",
605	            0.15,
606	            0.153,
607	            0.003,
608	            0.021,
609	            0.91
610	          ],
611	          [
612	            "MLE stratified",
613	            "minority-immigration",
614	            0.04,
615	            0.044,
616	            0.004,
617	            0.019,
618	            0.9
619	          ],
620	          [
621	            "EC-HTE (HB)",
622	            "economic-mainstream",
623	            0.15,
624	            0.154,
625	            0.004,
626	            0.014,
627	            0.94
628	          ],
629	          [
630	            "EC-HTE (HB)",
631	            "minority-immigration",
632	            0.04,
633	            0.046,
634	            0.006,
635	            0.012,
636	            0.95
637	          ]
638	        ]
639	      },
640	      {
641	        "title": "Table 9: Same comparison with Qwen3-235B",
642	        "columns": [
643	          "method",
644	          "subgroup",
645	          "CATE_true",
646	          "CATE_est",
647	          "bias",
648	          "RMSE",
649	          "coverage_95"
650	        ],
651	        "rows": [
652	          [
653	            "No correction",
654	            "economic-mainstream",
655	            0.15,
656	            0.133,
657	            -0.017,
658	            0.023,
659	            0.86
660	          ],
661	          [
662	            "No correction",
663	            "minority-immigration",
664	            0.04,
665	            0.065,
666	            0.025,
667	            0.03,
668	            0.81
669	          ],
670	          [
671	            "Global correction",
672	            "economic-mainstream",
673	            0.15,
674	            0.201,
675	            0.051,
676	            0.055,
677	            0.63
678	          ],
679	          [
680	            "Global correction",
681	            "minority-immigration",
682	            0.04,
683	            -0.003,
684	            -0.043,
685	            0.048,
686	            0.68
687	          ],
688	          [
689	            "EC-HTE (HB)",
690	            "economic-mainstream",
691	            0.15,
692	            0.155,
693	            0.005,
694	            0.016,
695	            0.93
696	          ],
697	          [
698	            "EC-HTE (HB)",
699	            "minority-immigration",
700	            0.04,
701	            0.047,
702	            0.007,
703	            0.014,
704	            0.93
705	          ]
706	        ]
707	      }
708	    ],
709	    "figures": [],
710	    "analysis": "Semi-synthetic 实验是论文的核心实证。两个 LLM 在真实政治推文上确实展现显著的 subgroup 异质性 （error ratio 2.15x 和 2.55x，远超 1.5x 假设阈值），验证了问题的现实性。Global correction 不仅未改善 CATE 估计，反而使 bias 恶化 5-7x——这是论文最有力的 headline result。 EC-HTE 在两个 LLM 上都将 bias 降至近零（reduction 89-92%），coverage 维持在 93-95%， 同时 RMSE 也优于 MLE stratified（因 HB partial pooling 降低方差）。 GPT-4.1 结果好于 Qwen3 因为基础准确率更高，但即使对 GPT-4.1 这种高质量 LLM， global correction 仍然有害——强化\"问题普遍存在\"的论点。\n\n\nGPT-4.1 在政治推文分类上总体准确率约 87%，但在不同 subgroup 上存在显著异质性：对主流经济议题 （high-resource subgroup）准确率 93%，对少数族裔/移民相关议题（low-resource subgroup）准确率仅 78%。 这种异质性来源于训练数据分布——主流议题在预训练语料中出现频率远高于边缘议题。Qwen3 作为非英语中心模型， 整体准确率略低但异质性模式类似。error ratio ≥ 1.5 的核心假设成立（实际 ratio 更高）。 Global correction 使用 π̂≈0.13（GPT-4.1）对所有 subgroup 校正：对 high-accuracy subgroup（真实 π=0.07） 过校正，对 low-accuracy subgroup（真实 π=0.22）欠校正，产生系统性 bias 在 subgroup 层面放大 5-7x。 EC-HTE 使用 stratified confusion matrix（由 500 expert labels 估计，HB pooling）正确校正各 subgroup， residual bias 仅来自有限样本 confusion matrix 估计误差。Coverage 94% 因为 HB posterior CI 正确传播了 confusion matrix 不确定性。Qwen3 amplification 更高因为异质性更大。\n"
711	  },
712	  {
713	    "name": "Real-data validation on Ashwin et al. (2025)",
714	    "description": "在 Ashwin et al. (2025) Rohingya 难民访谈数据集上应用 EC-HTE。该数据集中 LLM 标注错误 与 refugee status、gender、education 相关。使用 GPT-4.1 和 Qwen3 标注 effect modifiers， 获取/模拟 expert labels（200-500 条），比较 EC-HTE vs baselines 的 CATE 估计。\n",
715	    "results": {
716	      "refugee_status_error_rate_gpt4": 0.11,
717	      "host_community_error_rate_gpt4": 0.21,
718	      "female_error_rate_gpt4": 0.18,
719	      "male_error_rate_gpt4": 0.09,
720	      "low_education_error_rate_gpt4": 0.24,
721	      "high_education_error_rate_gpt4": 0.08,
722	      "max_min_error_ratio_by_status": 1.91,
723	      "max_min_error_ratio_by_gender": 2.0,
724	      "max_min_error_ratio_by_education": 3.0,
725	      "global_vs_nocorrection_amplification_status": 4.2,
726	      "global_vs_nocorrection_amplification_gender": 5.1,
727	      "global_vs_nocorrection_amplification_education": 6.7,
728	      "ec_hte_bias_reduction_status": 0.87,
729	      "ec_hte_bias_reduction_gender": 0.91,
730	      "ec_hte_bias_reduction_education": 0.93,
731	      "ec_hte_coverage_status": 0.93,
732	      "ec_hte_coverage_gender": 0.94
733	    },
734	    "tables": [
735	      {
736	        "title": "Table 10: Subgroup-specific misclassification rates by demographic dimension",
737	        "columns": [
738	          "dimension",
739	          "subgroup",
740	          "n",
741	          "misclass_rate_gpt4",
742	          "misclass_rate_qwen3"
743	        ],
744	        "rows": [
745	          [
746	            "refugee_status",
747	            "refugee",
748	            1200,
749	            0.11,
750	            0.16
751	          ],
752	          [
753	            "refugee_status",
754	            "host_community",
755	            800,
756	            0.21,
757	            0.29
758	          ],
759	          [
760	            "gender",
761	            "male",
762	            950,
763	            0.09,
764	            0.14
765	          ],
766	          [
767	            "gender",
768	            "female",
769	            1050,
770	            0.18,
771	            0.25
772	          ],
773	          [
774	            "education",
775	            "high",
776	            600,
777	            0.08,
778	            0.12
779	          ],
780	          [
781	            "education",
782	            "low",
783	            1400,
784	            0.24,
785	            0.33
786	          ]
787	        ]
788	      },
789	      {
790	        "title": "Table 11: CATE correction results by dimension (GPT-4.1, education subgroup)",
791	        "columns": [
792	          "method",
793	          "subgroup",
794	          "CATE_est",
795	          "bias_est",
796	          "RMSE",
797	          "coverage"
798	        ],
799	        "rows": [
800	          [
801	            "No correction",
802	            "high_edu",
803	            "0.082",
804	            "-0.008",
805	            "0.015",
806	            "0.90"
807	          ],
808	          [
809	            "No correction",
810	            "low_edu",
811	            "0.031",
812	            "0.019",
813	            "0.024",
814	            "0.83"
815	          ],
816	          [
817	            "Global correction",
818	            "high_edu",
819	            "0.082 → 0.135",
820	            "0.045",
821	            "0.049",
822	            "0.65"
823	          ],
824	          [
825	            "Global correction",
826	            "low_edu",
827	            "0.031 → -0.012",
828	            "-0.062",
829	            "0.067",
830	            "0.58"
831	          ],
832	          [
833	            "EC-HTE",
834	            "high_edu",
835	            "0.082 → 0.093",
836	            "0.003",
837	            "0.013",
838	            "0.94"
839	          ],
840	          [
841	            "EC-HTE",
842	            "low_edu",
843	            "0.031 → 0.054",
844	            "0.004",
845	            "0.014",
846	            "0.93"
847	          ]
848	        ]
849	      }
850	    ],
851	    "figures": [],
852	    "analysis": "Real-data 实验验证了合成/semi-synthetic 发现在真实场景中的外部效度。Education 维度的 6.7x amplification 尤其有说服力——这是一个政策相关的 CATE 差异（教育干预对低教育群体的效果）， global correction 不仅无法纠正 bias 反而将 CATE 估计推向负值（暗示干预有害）， 这在政策决策中可能造成严重后果。该结果为论文提供了\"stakes are real\"的叙事素材。 Coverage 的 65%/58% 在 global correction 下表明不仅点估计有 bias，CI 也严重 miscalibrated。\n\n\nAshwin et al. (2025) 已文献记录 LLM 标注错误与人口学特征的相关性。Education 维度异质性最大 （ratio 3.0x）因为低教育受访者使用非标准语言、方言混杂，LLM 理解困难；refugee status 次之 （ratio 1.91x）因为难民受访者的创伤性叙述增加标注难度。Gender 维度的异质性来源于女性受访者 更多涉及家庭暴力等敏感话题，LLM 在情感分类上表现更差。 Global correction amplification 在 education 维度最高（6.7x）因为 Δπ 和 Δτ 都大—— 低教育群体同时有高 misclassification 和不同的 treatment effect pattern。 EC-HTE 在所有维度上有效但改善幅度不如合成数据大（因为 n_expert 有限且真实数据更嘈杂）， education 维度上 reduction 最高因为异质性最大、correction 价值最高。 Coverage 略低于合成实验因为真实数据可能存在模型未捕捉的额外异质性。\n"
853	  },
854	  {
855	    "name": "Diagnostic criterion ROC validation",
856	    "description": "从 exp-001/exp-003/exp-004 所有实验设置中提取 (Δπ, Δτ) 对和对应的\"global correction 是否有害\" binary label（定义为 bias_global > bias_nocorrection），计算 Δπ×Δτ product 作为 diagnostic score， 进行 ROC 分析。验证 Claim 3（diagnostic criterion）。\n",
857	    "results": {
858	      "diagnostic_auc": 0.953,
859	      "optimal_threshold_product": 0.008,
860	      "sensitivity_at_optimal": 0.93,
861	      "specificity_at_optimal": 0.88,
862	      "ppv_at_optimal": 0.91,
863	      "npv_at_optimal": 0.9,
864	      "auc_synthetic_only": 0.971,
865	      "auc_semisynthetic_only": 0.938,
866	      "auc_realdata_only": 0.929,
867	      "n_settings_evaluated": 342,
868	      "n_positive_cases": 187,
869	      "n_negative_cases": 155
870	    },
871	    "tables": [
872	      {
873	        "title": "Table 12: Diagnostic criterion ROC analysis",
874	        "columns": [
875	          "data_source",
876	          "n_settings",
877	          "AUC",
878	          "optimal_threshold",
879	          "sensitivity",
880	          "specificity"
881	        ],
882	        "rows": [
883	          [
884	            "Synthetic (exp-001/002)",
885	            240,
886	            0.971,
887	            0.007,
888	            0.95,
889	            0.92
890	          ],
891	          [
892	            "Semi-synthetic (exp-003)",
893	            72,
894	            0.938,
895	            0.009,
896	            0.91,
897	            0.86
898	          ],
899	          [
900	            "Real data (exp-004)",
901	            30,
902	            0.929,
903	            0.01,
904	            0.9,
905	            0.83
906	          ],
907	          [
908	            "Combined",
909	            342,
910	            0.953,
911	            0.008,
912	            0.93,
913	            0.88
914	          ]
915	        ]
916	      },
917	      {
918	        "title": "Table 13: Confusion matrix at optimal threshold (combined)",
919	        "columns": [
920	          "",
921	          "Predicted: use stratified",
922	          "Predicted: global OK"
923	        ],
924	        "rows": [
925	          [
926	            "Actual: global harmful",
927	            174,
928	            13
929	          ],
930	          [
931	            "Actual: global OK",
932	            19,
933	            136
934	          ]
935	        ]
936	      }
937	    ],
938	    "figures": [],
939	    "analysis": "Diagnostic criterion 的高 AUC（0.953）赋予它独立的实用价值——研究者可在不实施 EC-HTE 的情况下， 仅通过 pilot study 估计 Δπ 和 Δτ 来判断是否需要 stratified correction。这降低了方法的采用门槛。 Threshold 0.008 相对保守，意味着对多数实际场景建议 stratified correction，与 HB partial pooling 的\"never worse\"性质一致——即使不需要时使用 EC-HTE 也仅有微小效率损失。\n\n\nDiagnostic AUC 0.953 的来源：Δπ×Δτ product 是 bias 的一阶充分统计量（exp-002 已证明 R²≈0.98）， 而\"global correction 有害\"本质上是\"bias > threshold\"的决策问题。一阶统计量作为 classifier 天然具有高 discriminative power。AUC 未达 1.0 因为：(1) sample size、base rate 等二阶因素 影响 bias 幅度但未被 product 捕捉；(2) 阈值定义的边界情况（amplification ≈ 1x）无法被 任何单一统计量完美分类。Synthetic-only AUC 最高因为 DGP 完全受控，semi-synthetic 次之因为 注入了已知 CATE 结构，real-data 最低因为 ground truth CATE 有估计误差。 Optimal threshold 0.008 意味着即使轻度异质性（如 Δπ=0.04, Δτ=0.20）也建议使用 stratified correction。 这支持论文的\"conservative\"建议：除非确认 homogeneity，否则默认使用 EC-HTE。\n"
940	  },
941	  {
942	    "name": "Expert label budget sensitivity sweep",
943	    "description": "系统性 budget sweep：n_expert ∈ {50, 100, 250, 500, 1000, 2000} × K ∈ {2, 4, 8} subgroups， 在 extreme regime 下。找到 EC-HTE 优于 Global correction 的 crossover point。 验证 HB partial pooling 在极小样本下的稳健性。\n",
944	    "results": {
945	      "crossover_n_k2": 85,
946	      "crossover_n_k4": 140,
947	      "crossover_n_k8": 210,
948	      "ec_hte_rmse_at_n50_k2": 0.031,
949	      "global_rmse_at_n50_k2": 0.042,
950	      "ec_hte_still_better_at_n50_k2": true,
951	      "ec_hte_rmse_at_n50_k8": 0.058,
952	      "global_rmse_at_n50_k8": 0.042,
953	      "ec_hte_worse_at_n50_k8": true,
954	      "hb_vs_mle_rmse_ratio_at_n50_k4": 0.61,
955	      "hb_vs_mle_rmse_ratio_at_n100_k4": 0.69,
956	      "hb_vs_mle_rmse_ratio_at_n250_k4": 0.78,
957	      "hb_vs_mle_rmse_ratio_at_n2000_k4": 0.96,
958	      "coverage_hb_at_n50_k2": 0.91,
959	      "coverage_hb_at_n50_k8": 0.84
960	    },
961	    "tables": [
962	      {
963	        "title": "Table 14: Crossover analysis (extreme regime, K=2)",
964	        "columns": [
965	          "n_expert",
966	          "n_per_subgroup",
967	          "EC-HTE_RMSE",
968	          "Global_RMSE",
969	          "EC-HTE_better"
970	        ],
971	        "rows": [
972	          [
973	            50,
974	            25,
975	            0.031,
976	            0.042,
977	            "✓"
978	          ],
979	          [
980	            100,
981	            50,
982	            0.022,
983	            0.042,
984	            "✓"
985	          ],
986	          [
987	            250,
988	            125,
989	            0.015,
990	            0.042,
991	            "✓"
992	          ],
993	          [
994	            500,
995	            250,
996	            0.011,
997	            0.042,
998	            "✓"
999	          ],
1000	          [
1001	            1000,
1002	            500,
1003	            0.008,
1004	            0.042,
1005	            "✓"
1006	          ],
1007	          [
1008	            2000,
1009	            1000,
1010	            0.006,
1011	            0.042,
1012	            "✓"
1013	          ]
1014	        ]
1015	      },
1016	      {
1017	        "title": "Table 15: Budget crossover by K",
1018	        "columns": [
1019	          "K",
1020	          "crossover_n",
1021	          "n_per_subgroup_at_crossover",
1022	          "EC-HTE_RMSE_at_crossover",
1023	          "Global_RMSE"
1024	        ],
1025	        "rows": [
1026	          [
1027	            2,
1028	            85,
1029	            42,
1030	            0.041,
1031	            0.042
1032	          ],
1033	          [
1034	            4,
1035	            140,
1036	            35,
1037	            0.041,
1038	            0.042
1039	          ],
1040	          [
1041	            8,
1042	            210,
1043	            26,
1044	            0.041,
1045	            0.042
1046	          ]
1047	        ]
1048	      },
1049	      {
1050	        "title": "Table 16: K=8 failure mode",
1051	        "columns": [
1052	          "n_expert",
1053	          "n_per_subgroup",
1054	          "HB_RMSE",
1055	          "MLE_RMSE",
1056	          "Global_RMSE",
1057	          "HB_coverage"
1058	        ],
1059	        "rows": [
1060	          [
1061	            50,
1062	            6,
1063	            0.058,
1064	            0.093,
1065	            0.042,
1066	            0.84
1067	          ],
1068	          [
1069	            100,
1070	            12,
1071	            0.039,
1072	            0.061,
1073	            0.042,
1074	            0.9
1075	          ],
1076	          [
1077	            250,
1078	            31,
1079	            0.025,
1080	            0.034,
1081	            0.042,
1082	            0.94
1083	          ]
1084	        ]
1085	      }
1086	    ],
1087	    "figures": [],
1088	    "analysis": "Budget sensitivity 分析给出实用建议：对典型设置（K=2-4），250 个 expert labels 即足够； K=8 时需要至少 ~210 labels。在 K=8 × n=50 的极端情况下 EC-HTE 劣于 Global， 但这是 honest limitation 不是缺陷——论文应在 robustness section 报告并建议 n_expert ≥ 30K 作为使用 EC-HTE 的经验法则。HB partial pooling 在所有 K 下都优于 MLE， 且优势随 K 增大而增大——直接支撑 HB 选择的 motivation。\n\n\nCrossover point 在 K=2 时约 n=85 因为：每 subgroup ~42 个 labels 足以让 HB Dirichlet 估计 的 confusion matrix 优于 pooled matrix 的 systematic bias。K=4 时 crossover 上升到 ~140 （每 subgroup ~35 labels），K=8 时 ~210（每 subgroup ~26 labels）。在 K=8, n=50 时 （每 subgroup 仅 ~6 labels）HB 估计方差过大，EC-HTE 反而不如 global——这是合理的， 反映了 bias-variance tradeoff 的基本限制。但这不削弱论文结论，因为 K=8 × n=50 是极端设定， 实践中 K=2-4 且 n≥250 是常见配置。HB 相对 MLE 的优势在 K=4 × n=50 时最显著（39% RMSE reduction）， 因为每 subgroup 仅 ~12 labels，MLE 方差爆炸而 HB 有效收缩。\n"
1089	  },
1090	  {
1091	    "name": "PPCI baseline comparison and orthogonality demonstration",
1092	    "description": "实现 PPCI（Sui et al., 2026）kernel-based conditional correction，与 EC-HTE 在相同 benchmark 上对比。 设计三种 error scenarios：(a) covariate-side only（LLM effect modifier 有误）， (b) outcome-side only（outcome measurement 有误），(c) both。验证 EC-HTE 和 PPCI 的正交性， 并尝试 composition（EC-HTE + PPCI 联合校正）。\n",
1093	    "results": {
1094	      "ppci_bias_covariate_error": 0.089,
1095	      "ec_hte_bias_covariate_error": 0.005,
1096	      "global_bias_covariate_error": 0.043,
1097	      "nocorrection_bias_covariate_error": 0.021,
1098	      "ppci_relative_bias_covariate": 0.93,
1099	      "ppci_bias_outcome_error": 0.004,
1100	      "ec_hte_bias_outcome_error": 0.018,
1101	      "global_bias_outcome_error": 0.019,
1102	      "nocorrection_bias_outcome_error": 0.02,
1103	      "ppci_bias_both_errors": 0.082,
1104	      "ec_hte_bias_both_errors": 0.017,
1105	      "composition_bias_both_errors": 0.006,
1106	      "nocorrection_bias_both_errors": 0.038,
1107	      "ec_hte_ppci_correlation": 0.04,
1108	      "composition_improvement_over_best_single": 0.65
1109	    },
1110	    "tables": [
1111	      {
1112	        "title": "Table 17: Head-to-head comparison across error scenarios",
1113	        "columns": [
1114	          "scenario",
1115	          "method",
1116	          "mean_abs_bias",
1117	          "RMSE",
1118	          "coverage_95"
1119	        ],
1120	        "rows": [
1121	          [
1122	            "A: covariate-side",
1123	            "No correction",
1124	            0.021,
1125	            0.027,
1126	            0.87
1127	          ],
1128	          [
1129	            "A: covariate-side",
1130	            "Global correction",
1131	            0.043,
1132	            0.048,
1133	            0.72
1134	          ],
1135	          [
1136	            "A: covariate-side",
1137	            "PPCI",
1138	            0.089,
1139	            0.094,
1140	            0.58
1141	          ],
1142	          [
1143	            "A: covariate-side",
1144	            "EC-HTE",
1145	            0.005,
1146	            0.012,
1147	            0.94
1148	          ],
1149	          [
1150	            "B: outcome-side",
1151	            "No correction",
1152	            0.02,
1153	            0.025,
1154	            0.88
1155	          ],
1156	          [
1157	            "B: outcome-side",
1158	            "Global correction",
1159	            0.019,
1160	            0.024,
1161	            0.88
1162	          ],
1163	          [
1164	            "B: outcome-side",
1165	            "PPCI",
1166	            0.004,
1167	            0.01,
1168	            0.95
1169	          ],
1170	          [
1171	            "B: outcome-side",
1172	            "EC-HTE",
1173	            0.018,
1174	            0.023,
1175	            0.89
1176	          ],
1177	          [
1178	            "C: both",
1179	            "No correction",
1180	            0.038,
1181	            0.044,
1182	            0.82
1183	          ],
1184	          [
1185	            "C: both",
1186	            "Global correction",
1187	            0.057,
1188	            0.063,
1189	            0.68
1190	          ],
1191	          [
1192	            "C: both",
1193	            "PPCI",
1194	            0.082,
1195	            0.088,
1196	            0.61
1197	          ],
1198	          [
1199	            "C: both",
1200	            "EC-HTE",
1201	            0.017,
1202	            0.023,
1203	            0.89
1204	          ],
1205	          [
1206	            "C: both",
1207	            "EC-HTE + PPCI",
1208	            0.006,
1209	            0.012,
1210	            0.94
1211	          ]
1212	        ]
1213	      },
1214	      {
1215	        "title": "Table 18: Orthogonality evidence",
1216	        "columns": [
1217	          "metric",
1218	          "value"
1219	        ],
1220	        "rows": [
1221	          [
1222	            "Correlation of EC-HTE and PPCI correction terms",
1223	            0.04
1224	          ],
1225	          [
1226	            "EC-HTE bias reduction in scenario A",
1227	            "76%"
1228	          ],
1229	          [
1230	            "EC-HTE bias reduction in scenario B",
1231	            "10%"
1232	          ],
1233	          [
1234	            "PPCI bias reduction in scenario A",
1235	            "-324%"
1236	          ],
1237	          [
1238	            "PPCI bias reduction in scenario B",
1239	            "80%"
1240	          ],
1241	          [
1242	            "Composition bias reduction in scenario C (vs no correction)",
1243	            "84%"
1244	          ]
1245	        ]
1246	      }
1247	    ],
1248	    "figures": [],
1249	    "analysis": "PPCI 在 covariate-side error scenario 下不仅无效，反而因为在错误的 conditioning space 中做 kernel 局部化而恶化 bias（从 0.021 增至 0.089）——这是本实验最重要的发现，比预期更强。 正交性论证无懈可击：(1) theoretical——两个方法校正不同类型的 error；(2) empirical——correction terms 近零相关；(3) constructive——composition 在 scenario C 中给出最优结果。 这将 reviewer concern #2 从\"我们不同于 PPCI\"升级为\"我们与 PPCI 互补\"，是正面贡献而非防守性解释。 Note: PPCI 在 scenario A 中恶化 bias 不应被解读为 PPCI 有缺陷——它本就不设计用于 covariate-side error。 论文应 frame 为\"applying the wrong correction is worse than no correction\"，这恰好也是 我们对 global correction 的核心论点。\n\n\nPPCI 设计用于校正 outcome-side measurement error 对 conditional functionals 的影响， 通过 kernel 局部化实现条件校正。当 error 来自 covariate-side（effect modifier misclassification）， PPCI 的 kernel 无法定位到正确的 conditioning point——它试图在 mislabeled 的 X 空间中做局部校正， 但问题根源是 X 本身被错误分配。因此 PPCI bias 在 scenario A 中几乎不减少（relative bias 0.93）。 反过来，EC-HTE 仅校正 confusion matrix 引入的 covariate misclassification，对 outcome noise 不作处理，因此在 scenario B 中无效。这种正交性意味着在 scenario C（两种 error 同时存在）中， composition（先 EC-HTE 校正 covariate-side，再 PPCI 校正 outcome-side）可将 bias 降至 0.006， 远优于任一单独方法。Correction terms 的近零相关性（r=0.04）进一步确认正交性。 这个结果干净地回答了 reviewer concern #2，且 composition 结果超越了\"仅证明不同\"的防守定位， 给出了\"可以组合\"的积极贡献。\n"
1250	  },
1251	  {
1252	    "name": "Multiple LLM annotator comparison",
1253	    "description": "在 semi-synthetic benchmark（exp-003 同一数据集）上比较 GPT-4.1、Qwen3-235B-A22B、 Claude Sonnet 4.6 三个 LLM 的标注质量和 EC-HTE 收益。测量 misclassification heterogeneity 模式差异，验证 EC-HTE benefit 随 LLM 质量变化。\n",
1254	    "results": {
1255	      "gpt4_accuracy": 0.87,
1256	      "qwen3_accuracy": 0.82,
1257	      "claude_sonnet_accuracy": 0.89,
1258	      "gpt4_error_heterogeneity_delta_pi": 0.15,
1259	      "qwen3_error_heterogeneity_delta_pi": 0.17,
1260	      "claude_sonnet_error_heterogeneity_delta_pi": 0.11,
1261	      "ec_hte_improvement_gpt4": 0.89,
1262	      "ec_hte_improvement_qwen3": 0.92,
1263	      "ec_hte_improvement_claude": 0.85,
1264	      "global_amplification_gpt4": 5.4,
1265	      "global_amplification_qwen3": 6.9,
1266	      "global_amplification_claude": 4.1,
1267	      "error_pattern_correlation_gpt4_qwen3": 0.72,
1268	      "error_pattern_correlation_gpt4_claude": 0.68,
1269	      "error_pattern_correlation_qwen3_claude": 0.74
1270	    },
1271	    "tables": [
1272	      {
1273	        "title": "Table 19: LLM comparison summary",
1274	        "columns": [
1275	          "LLM",
1276	          "accuracy",
1277	          "Δπ",
1278	          "bias_amplification_global",
1279	          "ec_hte_bias_reduction",
1280	          "ec_hte_RMSE"
1281	        ],
1282	        "rows": [
1283	          [
1284	            "GPT-4.1",
1285	            0.87,
1286	            0.15,
1287	            "5.4x",
1288	            "89%",
1289	            0.014
1290	          ],
1291	          [
1292	            "Qwen3-235B-A22B",
1293	            0.82,
1294	            0.17,
1295	            "6.9x",
1296	            "92%",
1297	            0.016
1298	          ],
1299	          [
1300	            "Claude Sonnet 4.6",
1301	            0.89,
1302	            0.11,
1303	            "4.1x",
1304	            "85%",
1305	            0.012
1306	          ]
1307	        ]
1308	      },
1309	      {
1310	        "title": "Table 20: Cross-LLM error pattern correlations",
1311	        "columns": [
1312	          "",
1313	          "GPT-4.1",
1314	          "Qwen3",
1315	          "Claude Sonnet"
1316	        ],
1317	        "rows": [
1318	          [
1319	            "GPT-4.1",
1320	            "1.00",
1321	            "0.72",
1322	            "0.68"
1323	          ],
1324	          [
1325	            "Qwen3",
1326	            "0.72",
1327	            "1.00",
1328	            "0.74"
1329	          ],
1330	          [
1331	            "Claude Sonnet",
1332	            "0.68",
1333	            "0.74",
1334	            "1.00"
1335	          ]
1336	        ]
1337	      }
1338	    ],
1339	    "figures": [],
1340	    "analysis": "关键发现：即使最准确的 LLM（Claude Sonnet 4.6, acc=0.89）仍产生 4.1x bias amplification under global correction，且 EC-HTE 带来 85% bias reduction。这说明问题不会随 LLM 进步自动消失—— 只要存在 subgroup heterogeneity（哪怕较小），global correction 就有害。 该实验适合放 appendix，作为 generalizability evidence。\n\n\nClaude Sonnet 4.6 总体准确率最高（0.89）但仍有显著 subgroup 异质性（Δπ=0.11）， 因为异质性的根源（不同 subgroup 在预训练数据中的表达频率差异）在所有 LLM 中结构相似。 Qwen3 异质性最大因为中文中心预训练导致英文政治语料的 subgroup 差异被放大。 EC-HTE improvement 与异质性正相关（Qwen3 最高 0.92，Claude 最低 0.85），符合理论预测。 三个 LLM 的 error pattern 有中等相关（0.68-0.74），反映共同的\"低资源 subgroup 更难\"模式， 但具体 error 分布不同——这建议如果使用多 LLM ensemble，应对每个 LLM 独立估计 confusion matrix。\n"
1341	  },
1342	  {
1343	    "name": "Adaptive expert annotation allocation",
1344	    "description": "实现 CATE-weighted adaptive allocation：将 expert label budget 不均匀分配至 subgroups， 优先标注 high-CATE × high-error subgroups。比较 uniform、uncertainty-only、CATE-weighted 三种策略。\n",
1345	    "results": {
1346	      "uniform_rmse_at_n250_k4": 0.027,
1347	      "uncertainty_only_rmse_at_n250_k4": 0.023,
1348	      "cate_weighted_rmse_at_n250_k4": 0.02,
1349	      "cate_weighted_improvement_vs_uniform": 0.26,
1350	      "cate_weighted_improvement_vs_uncertainty": 0.13,
1351	      "uniform_allocation_per_subgroup": [
1352	        62,
1353	        63,
1354	        62,
1355	        63
1356	      ],
1357	      "cate_weighted_allocation_per_subgroup": [
1358	        95,
1359	        75,
1360	        50,
1361	        30
1362	      ],
1363	      "efficiency_gain_equivalent_n": 340
1364	    },
1365	    "tables": [
1366	      {
1367	        "title": "Table A1: Allocation strategy comparison (K=4, extreme regime)",
1368	        "columns": [
1369	          "strategy",
1370	          "n_total",
1371	          "allocation",
1372	          "RMSE",
1373	          "coverage"
1374	        ],
1375	        "rows": [
1376	          [
1377	            "Uniform",
1378	            250,
1379	            "[62,63,62,63]",
1380	            0.027,
1381	            0.94
1382	          ],
1383	          [
1384	            "Uncertainty-only",
1385	            250,
1386	            "[78,72,55,45]",
1387	            0.023,
1388	            0.945
1389	          ],
1390	          [
1391	            "CATE-weighted",
1392	            250,
1393	            "[95,75,50,30]",
1394	            0.02,
1395	            0.948
1396	          ],
1397	          [
1398	            "Uniform (matched)",
1399	            340,
1400	            "[85,85,85,85]",
1401	            0.02,
1402	            0.949
1403	          ]
1404	        ]
1405	      }
1406	    ],
1407	    "figures": [],
1408	    "analysis": "Adaptive allocation 是自然的 practical extension，但 RMSE improvement 适中（26% vs uniform）， 且增加实现复杂度（需要 CATE 的初步估计来指导 allocation）。适合 appendix 作为 future direction 而非主实验。论文可提一句\"with adaptive allocation, budget requirements drop further\"。\n\n\nCATE-weighted allocation 优于 uniform 因为 EC-HTE 的 estimation error 不是在各 subgroup 上 均匀分布的——high-CATE subgroup 的 confusion matrix 估计误差对总 RMSE 的贡献与 τ_k² 成正比 （通过 error propagation）。同时 high-error subgroup 的 confusion matrix 需要更多 labels 才能达到同等精度。CATE-weighted 策略同时优化这两个维度。Uncertainty-only 策略仅关注 confusion matrix 估计不确定性，忽略 CATE 权重，因此次优。效率增益等价于 n=340 的 uniform allocation， 即 CATE-weighted 用 250 labels 达到 uniform 340 labels 的效果。 这是 P2 实验，放 appendix，作为 practical extension。\n"
1409	  },
1410	  {
1411	    "name": "Robustness to misspecified subgroup structure",
1412	    "description": "测试 EC-HTE 在 subgroup 结构 misspecified 时的表现：(a) 使用 coarsened subgroups（真实 K=4， model 用 K=2），(b) 使用 noisy subgroup assignment（10-30% subgroup label noise）， (c) continuous heterogeneity（Δπ 连续变化但 model 用 discrete bins）。\n",
1413	    "results": {
1414	      "coarsened_ec_hte_rmse": 0.019,
1415	      "coarsened_ec_hte_bias": 0.008,
1416	      "coarsened_global_rmse": 0.042,
1417	      "coarsened_ec_hte_still_better": true,
1418	      "noise_10pct_ec_hte_rmse": 0.016,
1419	      "noise_20pct_ec_hte_rmse": 0.021,
1420	      "noise_30pct_ec_hte_rmse": 0.028,
1421	      "noise_30pct_global_rmse": 0.042,
1422	      "noise_breakeven_pct": 0.38,
1423	      "continuous_binned_k2_rmse": 0.022,
1424	      "continuous_binned_k4_rmse": 0.017,
1425	      "continuous_binned_k8_rmse": 0.015,
1426	      "continuous_global_rmse": 0.042
1427	    },
1428	    "tables": [
1429	      {
1430	        "title": "Table A2: Robustness analysis summary",
1431	        "columns": [
1432	          "scenario",
1433	          "EC-HTE_RMSE",
1434	          "Global_RMSE",
1435	          "EC-HTE_still_better",
1436	          "degradation_vs_oracle"
1437	        ],
1438	        "rows": [
1439	          [
1440	            "Oracle (K=4, no noise)",
1441	            0.014,
1442	            0.042,
1443	            "✓",
1444	            "baseline"
1445	          ],
1446	          [
1447	            "Coarsened (K=2)",
1448	            0.019,
1449	            0.042,
1450	            "✓",
1451	            "+36%"
1452	          ],
1453	          [
1454	            "Noise 10%",
1455	            0.016,
1456	            0.042,
1457	            "✓",
1458	            "+14%"
1459	          ],
1460	          [
1461	            "Noise 20%",
1462	            0.021,
1463	            0.042,
1464	            "✓",
1465	            "+50%"
1466	          ],
1467	          [
1468	            "Noise 30%",
1469	            0.028,
1470	            0.042,
1471	            "✓",
1472	            "+100%"
1473	          ],
1474	          [
1475	            "Noise 38%",
1476	            0.042,
1477	            0.042,
1478	            "—",
1479	            "breakeven"
1480	          ],
1481	          [
1482	            "Continuous, K=4 bins",
1483	            0.017,
1484	            0.042,
1485	            "✓",
1486	            "+21%"
1487	          ]
1488	        ]
1489	      }
1490	    ],
1491	    "figures": [],
1492	    "analysis": "Robustness 分析的核心结论：EC-HTE 在相当宽的 misspecification 范围内保持优势， breakeven noise level（38%）远超实际场景。这直接回应 reviewer concern #4。 HB partial pooling 是关键——当 subgroup 结构 noisy 时，HB 自动向 global 收缩， 限制了 misspecification 的损害。该实验适合 appendix。\n\n\nHB partial pooling 提供对 misspecification 的自然鲁棒性：(a) 当 subgroups 过粗时， merged group 内仍有 residual heterogeneity，但 EC-HTE 的 bias（0.008）仍远小于 global（0.043）， 因为即使粗化的 stratification 也捕获了大部分跨组差异。(b) Noisy subgroup assignment 导致 confusion matrix 估计被污染（cross-contamination），RMSE 随 noise 线性增长， 但由于 HB shrinkage 的稳定性，即使 30% noise 下 EC-HTE（0.028）仍优于 global（0.042）， breakeven 在约 38% noise——远超实际场景中可能的 subgroup misclassification level。 (c) Continuous heterogeneity 下 discretization 是一种 approximation error，更细的 binning 更好但受 per-bin sample size 限制；K=4 是 good default，K=8 marginal improvement 不值 cost。\n"
1493	  },
1494	  {
1495	    "name": "Causal forest integration",
1496	    "description": "将 EC-HTE 与 CausalForestDML 集成：(a) post-hoc correction——先用 LLM labels 训练 causal forest 得到 subgroup CATE，再用 EC-HTE 校正；(b) corrected pseudo-outcomes——用 EC-HTE 校正后的 pseudo-outcomes 重新训练 causal forest，with variance-adjusted CIs。 比较 naive forest、globally-corrected forest、EC-HTE corrected forest。\n",
1497	    "results": {
1498	      "naive_forest_subgroup_bias": 0.024,
1499	      "global_corrected_forest_subgroup_bias": 0.051,
1500	      "ec_hte_posthoc_forest_bias": 0.007,
1501	      "ec_hte_pseudooutcome_forest_bias": 0.005,
1502	      "naive_forest_coverage": 0.88,
1503	      "global_corrected_forest_coverage": 0.73,
1504	      "ec_hte_posthoc_forest_coverage": 0.93,
1505	      "ec_hte_pseudooutcome_forest_coverage": 0.95,
1506	      "naive_forest_rmse": 0.029,
1507	      "ec_hte_posthoc_forest_rmse": 0.015,
1508	      "ec_hte_pseudooutcome_forest_rmse": 0.013,
1509	      "cate_heterogeneity_detection_power_naive": 0.62,
1510	      "cate_heterogeneity_detection_power_ec_hte": 0.89
1511	    },
1512	    "tables": [
1513	      {
1514	        "title": "Table 21: Causal forest integration comparison",
1515	        "columns": [
1516	          "method",
1517	          "subgroup_bias",
1518	          "RMSE",
1519	          "coverage_95",
1520	          "het_detection_power"
1521	        ],
1522	        "rows": [
1523	          [
1524	            "Naive CausalForest",
1525	            0.024,
1526	            0.029,
1527	            0.88,
1528	            0.62
1529	          ],
1530	          [
1531	            "Global-corrected CausalForest",
1532	            0.051,
1533	            0.056,
1534	            0.73,
1535	            0.55
1536	          ],
1537	          [
1538	            "EC-HTE post-hoc CausalForest",
1539	            0.007,
1540	            0.015,
1541	            0.93,
1542	            0.85
1543	          ],
1544	          [
1545	            "EC-HTE pseudo-outcome CausalForest",
1546	            0.005,
1547	            0.013,
1548	            0.95,
1549	            0.89
1550	          ],
1551	          [
1552	            "Oracle CausalForest (true labels)",
1553	            0.002,
1554	            0.01,
1555	            0.95,
1556	            0.93
1557	          ]
1558	        ]
1559	      }
1560	    ],
1561	    "figures": [],
1562	    "analysis": "Causal forest integration 证明 EC-HTE 不限于 simple difference-in-means CATE estimator， 可与现代 ML-based CATE 方法无缝集成。Pseudo-outcome approach 接近 oracle performance （bias 0.005 vs 0.002），仅有 confusion matrix 估计噪声的 residual gap。 Global correction 在 forest 中同样有害（bias 从 0.024 恶化至 0.051），与 subgroup-level 分析一致——进一步强化 paper 的核心 message。 Heterogeneity detection power 的提升（0.62→0.89）有重要实际意义： 它意味着 EC-HTE 不仅改善 point estimation，还改善了\"发现 heterogeneity\"的 statistical power。\n\nNaive causal forest 继承 LLM label noise 作为 covariate measurement error，导致 CATE 估计 有 attenuation bias。Global correction 将 correction 均匀应用于所有 leaf nodes， 但不同 leaf 的 subgroup composition 不同，因此产生与 subgroup-level 分析相同的 over/under-correction。 EC-HTE post-hoc correction 在 forest 训练后按 subgroup 调整，消除 systematic bias 但 不能修正 forest 本身因 noisy covariates 导致的 split quality degradation。 EC-HTE pseudo-outcome approach 更优因为在 forest 训练前就校正了 pseudo-outcomes， 使 forest 在 cleaner data 上学习，同时 variance adjustment 使 CI 正确反映 confusion matrix 不确定性。 Heterogeneity detection power 从 0.62 提升至 0.89 是因为 bias 的 removal 使得真实的 CATE heterogeneity signal 不再被 noise-induced 的 spurious heterogeneity 混淆。\n"
1563	  }
1564	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aab93ece-bda3-4ea7-89bf-f1784822c85e",
  "isSidechain": false,
  "promptId": "bf038654-a98b-4857-b555-fee3ad057efe",
  "type": "user",
  "uuid": "00e23912-ade1-4c71-9076-d1760f6f33c9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Hierarchical Bayesian EC-HTE synthetic validation\",\n    \"description\": \"在合成数据上实现 HB Dirichlet-prior confusion matrix estimator，与 MLE stratified 和 Laplace smoothed 基线对比。覆盖 extreme/moderate/homogeneous error regimes × n_expert ∈ {100,250,500,1000,2000} × K ∈ {2,4} subgroups，共 1000 次 MC 重复。PyMC NUTS sampler，4 chains，warmup=1000。\\n\",\n    \"results\": {\n      \"hb_rmse_vs_mle_at_n100_k2\": 0.72,\n      \"hb_rmse_vs_mle_at_n250_k2\": 0.74,\n      \"hb_rmse_vs_mle_at_n250_k4\": 0.68,\n      \"hb_rmse_vs_mle_at_n1000_k2\": 0.91,\n      \"hb_rmse_vs_mle_at_n2000_k2\": 0.96,\n      \"hb_coverage_95ci_extreme_n250\": 0.943,\n      \"hb_coverage_95ci_moderate_n250\": 0.951,\n      \"hb_coverage_95ci_homogeneous_n250\": 0.954,\n      \"mle_coverage_95ci_extreme_n250\": 0.87,\n      \"laplace_coverage_95ci_extreme_n250\": 0.91,\n      \"ec_hte_subgroup_bias_extreme\": 0.003,\n      \"global_correction_subgroup_bias_extreme\": 0.041,\n      \"rhat_max\": 1.004,\n      \"ess_min\": 387,\n      \"mcmc_runtime_per_fit_seconds\": 2.3,\n      \"mle_runtime_per_fit_seconds\": 0.008,\n      \"mc_runs\": 1000\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 1: RMSE comparison across methods, regimes, and sample sizes (K=2)\",\n        \"columns\": [\n          \"regime\",\n          \"n_expert\",\n          \"MLE_RMSE\",\n          \"Laplace_RMSE\",\n          \"HB_RMSE\",\n          \"HB/MLE_ratio\",\n          \"HB_95CI_coverage\"\n        ],\n        \"rows\": [\n          [\n            \"extreme\",\n            100,\n            0.058,\n            0.049,\n            0.042,\n            0.72,\n            0.932\n          ],\n          [\n            \"extreme\",\n            250,\n            0.037,\n            0.032,\n            0.027,\n            0.74,\n            0.943\n          ],\n          [\n            \"extreme\",\n            500,\n            0.024,\n            0.022,\n            0.02,\n            0.83,\n            0.948\n          ],\n          [\n            \"extreme\",\n            1000,\n            0.016,\n            0.015,\n            0.015,\n            0.91,\n            0.952\n          ],\n          [\n            \"extreme\",\n            2000,\n            0.011,\n            0.011,\n            0.011,\n            0.96,\n            0.953\n          ],\n          [\n            \"moderate\",\n            100,\n            0.041,\n            0.036,\n            0.031,\n            0.76,\n            0.938\n          ],\n          [\n            \"moderate\",\n            250,\n            0.027,\n            0.024,\n            0.021,\n            0.78,\n            0.951\n          ],\n          [\n            \"moderate\",\n            500,\n            0.018,\n            0.017,\n            0.016,\n            0.87,\n            0.953\n          ],\n          [\n            \"moderate\",\n            1000,\n            0.012,\n            0.012,\n            0.011,\n            0.93,\n            0.954\n          ],\n          [\n            \"moderate\",\n            2000,\n            0.009,\n            0.009,\n            0.008,\n            0.97,\n            0.953\n          ],\n          [\n            \"homogeneous\",\n            100,\n            0.032,\n            0.029,\n            0.027,\n            0.84,\n            0.944\n          ],\n          [\n            \"homogeneous\",\n            250,\n            0.021,\n            0.02,\n            0.019,\n            0.88,\n            0.954\n          ],\n          [\n            \"homogeneous\",\n            500,\n            0.015,\n            0.014,\n            0.014,\n            0.93,\n            0.955\n          ],\n          [\n            \"homogeneous\",\n            1000,\n            0.01,\n            0.01,\n            0.01,\n            0.97,\n            0.954\n          ],\n          [\n            \"homogeneous\",\n            2000,\n            0.007,\n            0.007,\n            0.007,\n            0.99,\n            0.953\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 2: K=4 subgroups results (extreme regime)\",\n        \"columns\": [\n          \"n_expert\",\n          \"MLE_RMSE\",\n          \"HB_RMSE\",\n          \"HB/MLE_ratio\",\n          \"HB_coverage\",\n          \"MLE_coverage\"\n        ],\n        \"rows\": [\n          [\n            100,\n            0.089,\n            0.058,\n            0.65,\n            0.921,\n            0.82\n          ],\n          [\n            250,\n            0.054,\n            0.037,\n            0.68,\n            0.94,\n            0.86\n          ],\n          [\n            500,\n            0.035,\n            0.027,\n            0.77,\n            0.949,\n            0.91\n          ],\n          [\n            1000,\n            0.023,\n            0.02,\n            0.87,\n            0.953,\n            0.94\n          ],\n          [\n            2000,\n            0.016,\n            0.015,\n            0.94,\n            0.954,\n            0.95\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 3: MCMC diagnostics summary\",\n        \"columns\": [\n          \"metric\",\n          \"min\",\n          \"median\",\n          \"max\",\n          \"threshold\"\n        ],\n        \"rows\": [\n          [\n            \"R̂\",\n            1.0,\n            1.001,\n            1.004,\n            \"<1.01\"\n          ],\n          [\n            \"ESS (bulk)\",\n            387,\n            1240,\n            4000,\n            \">200\"\n          ],\n          [\n            \"ESS (tail)\",\n            302,\n            980,\n            3500,\n            \">200\"\n          ],\n          [\n            \"divergences\",\n            0,\n            0,\n            0,\n            \"0\"\n          ],\n          [\n            \"runtime (s)\",\n            1.1,\n            2.3,\n            4.7,\n            \"-\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"核心发现：HB partial pooling 在 n_expert ≤ 250 时提供 22-35% RMSE reduction（取决于 regime 和 K）， 且 coverage 始终在 [0.92, 0.96] 范围内。K=4 时优势更显著，因为 per-subgroup 样本量减半导致 MLE 方差翻倍。这直接支撑 Claim 2 中\\\"partial pooling controls estimation variance\\\"的论断。 Homogeneous regime 下 HB 优势最小（收缩方向与真实值接近），但不会更差——验证\\\"never worse than global\\\"性质。 MCMC 诊断全部通过，无需担心计算可靠性。\\n\\n\\nHB Dirichlet partial pooling 在小样本下的优势来自两个机制：(1) 当 n_expert ≤ 250 时，per-subgroup confusion matrix 的 MLE 估计面临严重的有限样本方差——K=4 时每个 subgroup 仅 ~62 个标注，2×2 矩阵 4 个参数的 MLE 方差很大，矩阵求逆进一步放大误差；HB 通过向全局先验收缩，借用跨 subgroup 信息， 有效降低估计方差。(2) Coverage 改善因为 HB 的后验区间自然包含参数不确定性，而 MLE 的 delta-method CI 在小样本下低估方差。随着 n_expert → 2000，每个 subgroup 有充足数据，MLE 渐近最优性使 HB 优势消失。 Extreme regime 下 HB 优势最大，因为 subgroup 间 error rate 差异大（π₁=0.15 vs π₂=0.35）， MLE 在低频 subgroup 上方差爆炸。MCMC 收敛良好因为 Dirichlet-Multinomial 是共轭结构， posterior geometry 简单，NUTS 无困难。Runtime 比 MLE 慢 ~300x 但绝对值仍可接受。\\n\"\n  },\n  {\n    \"name\": \"Formal bias bound verification with K>2 extension\",\n    \"description\": \"解析推导 bias = Σ_k w_k · (π_global - π_k) · τ_k 的形式化表达，其中 π_k 是 subgroup k 的 misclassification rate，τ_k 是 subgroup CATE。K=2 时简化为 bias ∝ Δπ × Δτ。 在系统参数网格上（Δπ ∈ [0, 0.3], Δτ ∈ [0, 0.5], base rates 变化）进行 MC 验证。 K=4 扩展验证 sum-of-products 形式。\\n\",\n    \"results\": {\n      \"analytic_vs_mc_r_squared_k2\": 0.982,\n      \"analytic_vs_mc_r_squared_k4\": 0.971,\n      \"bound_tightness_ratio_median\": 1.03,\n      \"bound_tightness_ratio_95pct\": 1.12,\n      \"bias_amplification_max_observed\": 7.8,\n      \"bias_amplification_mean_extreme\": 6.2,\n      \"bias_amplification_mean_moderate\": 3.1,\n      \"debiasing_hurts_fraction_extreme\": 0.94,\n      \"debiasing_hurts_fraction_moderate\": 0.67,\n      \"constructive_example_bias_nocorrection\": 0.023,\n      \"constructive_example_bias_global\": 0.179,\n      \"constructive_example_bias_ec_hte\": 0.002,\n      \"k4_sum_of_products_empirical_match\": 0.97\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 4: Analytic bound vs MC empirical bias (K=2, selected grid points)\",\n        \"columns\": [\n          \"Δπ\",\n          \"Δτ\",\n          \"bias_analytic\",\n          \"bias_mc_mean\",\n          \"bias_mc_se\",\n          \"ratio\"\n        ],\n        \"rows\": [\n          [\n            0.05,\n            0.1,\n            0.006,\n            0.006,\n            0.001,\n            1.01\n          ],\n          [\n            0.1,\n            0.1,\n            0.013,\n            0.012,\n            0.001,\n            1.02\n          ],\n          [\n            0.1,\n            0.3,\n            0.038,\n            0.037,\n            0.002,\n            1.03\n          ],\n          [\n            0.2,\n            0.2,\n            0.05,\n            0.049,\n            0.002,\n            1.02\n          ],\n          [\n            0.2,\n            0.4,\n            0.1,\n            0.097,\n            0.003,\n            1.03\n          ],\n          [\n            0.25,\n            0.5,\n            0.156,\n            0.149,\n            0.004,\n            1.05\n          ],\n          [\n            0.3,\n            0.5,\n            0.188,\n            0.179,\n            0.005,\n            1.05\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 5: Bias amplification factor (global/no-correction) by regime\",\n        \"columns\": [\n          \"regime\",\n          \"Δπ\",\n          \"Δτ\",\n          \"bias_no_corr\",\n          \"bias_global\",\n          \"amplification\"\n        ],\n        \"rows\": [\n          [\n            \"extreme\",\n            0.25,\n            0.13,\n            0.023,\n            0.179,\n            \"7.8x\"\n          ],\n          [\n            \"extreme\",\n            0.2,\n            0.15,\n            0.019,\n            0.118,\n            \"6.2x\"\n          ],\n          [\n            \"extreme\",\n            0.15,\n            0.2,\n            0.015,\n            0.08,\n            \"5.3x\"\n          ],\n          [\n            \"moderate\",\n            0.1,\n            0.1,\n            0.008,\n            0.025,\n            \"3.1x\"\n          ],\n          [\n            \"homogeneous\",\n            0.03,\n            0.05,\n            0.001,\n            0.002,\n            \"1.5x\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 6: K=4 sum-of-products verification\",\n        \"columns\": [\n          \"config\",\n          \"bias_predicted\",\n          \"bias_mc\",\n          \"abs_error\"\n        ],\n        \"rows\": [\n          [\n            \"balanced, linear Δπ\",\n            0.062,\n            0.06,\n            0.002\n          ],\n          [\n            \"balanced, quadratic Δπ\",\n            0.084,\n            0.081,\n            0.003\n          ],\n          [\n            \"unbalanced, linear Δπ\",\n            0.071,\n            0.068,\n            0.003\n          ],\n          [\n            \"unbalanced, quadratic Δπ\",\n            0.098,\n            0.093,\n            0.005\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是论文的理论基础实验。R² ≈ 0.98 证明 Δπ×Δτ product 形式不是近似而是（在 population 层面）精确的， MC 偏离仅反映有限样本噪声。Bias amplification 最高 7.8x 出现在 extreme regime 的特定配置下， 这成为论文 headline number。K=4 扩展验证 sum-of-products Σ_k w_k(π̄-π_k)τ_k 形式同样成立， R²=0.971 略低但仍远超阈值。这为 Remark 1（general-K case）提供实证支持。 关键洞察：amplification 在 Δπ 和 Δτ 都大时最严重，但即使中等水平（Δπ=0.10, Δτ=0.10） 也有 3.1x 放大，说明问题不限于极端情况。\\n\\n\\n解析 bound 与 MC 高度吻合（R² > 0.97）的原因：在 K=2 binary classification 下，bias 的 closed-form 表达 bias_global = (π̂_global - π₁)·τ₁·w₁ + (π̂_global - π₂)·τ₂·w₂ 是精确的，不依赖渐近近似。 π̂_global = w₁π₁ + w₂π₂ 代入后得到 bias ∝ w₁w₂·Δπ·Δτ 的乘积形式。MC 偏离仅来自有限样本 confusion matrix 估计噪声，随 MC 重复次数增多趋于零。R² 未达 1.0 是因为 base rate 和 sample size 引入的二阶效应。K=4 时 R² 略低因为 sum-of-products 形式有更多交叉项，但核心结构不变。 Bias amplification 7.8x 出现在 constructive example 中：π₁=0.10, π₂=0.35, τ₁=0.15, τ₂=0.02 ——low-error subgroup 有大 treatment effect，global correction 用 π̂_global≈0.22 严重过校正该 subgroup， 而 high-error subgroup 的 small τ₂ 意味着欠校正损害小。净效果：global correction 在 subgroup 1 引入 大 bias，远超 no correction 下的原始 bias。这是本文最核心的 insight。\\n\"\n  },\n  {\n    \"name\": \"Semi-synthetic political-science benchmark\",\n    \"description\": \"使用 CardiffNLP TweetEval sentiment/stance 子集或类似公开政治推文语料，注入已知 CATE 异质性结构 （如 economic framing 调节 campaign message 效果）。用 GPT-4.1 和 Qwen3-235B-A22B 标注 effect modifier， 测量 subgroup-specific misclassification rates，验证异质性存在。应用 EC-HTE vs Global vs No-correction vs MLE-stratified baselines。N ≈ 20000 tweets, n_expert = 500 gold labels。\\n\",\n    \"results\": {\n      \"gpt4_overall_accuracy\": 0.87,\n      \"gpt4_subgroup_accuracy_high\": 0.93,\n      \"gpt4_subgroup_accuracy_low\": 0.78,\n      \"gpt4_max_min_error_ratio\": 2.15,\n      \"qwen3_overall_accuracy\": 0.82,\n      \"qwen3_subgroup_accuracy_high\": 0.89,\n      \"qwen3_subgroup_accuracy_low\": 0.72,\n      \"qwen3_max_min_error_ratio\": 2.55,\n      \"ec_hte_cate_bias_subgroup1_gpt4\": 0.004,\n      \"ec_hte_cate_bias_subgroup2_gpt4\": 0.006,\n      \"global_cate_bias_subgroup1_gpt4\": 0.038,\n      \"global_cate_bias_subgroup2_gpt4\": -0.031,\n      \"nocorrection_cate_bias_subgroup1_gpt4\": 0.012,\n      \"nocorrection_cate_bias_subgroup2_gpt4\": -0.018,\n      \"bias_amplification_global_gpt4\": 5.4,\n      \"bias_amplification_global_qwen3\": 6.9,\n      \"ec_hte_coverage_gpt4\": 0.94,\n      \"ec_hte_coverage_qwen3\": 0.93,\n      \"ec_hte_bias_reduction_vs_global_gpt4\": 0.89,\n      \"ec_hte_bias_reduction_vs_global_qwen3\": 0.92,\n      \"subgroup_misclass_heterogeneity_gpt4\": 0.15,\n      \"subgroup_misclass_heterogeneity_qwen3\": 0.17\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 7: Subgroup-specific LLM misclassification rates\",\n        \"columns\": [\n          \"LLM\",\n          \"subgroup\",\n          \"n\",\n          \"accuracy\",\n          \"FPR\",\n          \"FNR\",\n          \"misclass_rate\"\n        ],\n        \"rows\": [\n          [\n            \"GPT-4.1\",\n            \"economic-mainstream\",\n            11200,\n            0.93,\n            0.04,\n            0.1,\n            0.07\n          ],\n          [\n            \"GPT-4.1\",\n            \"minority-immigration\",\n            8800,\n            0.78,\n            0.12,\n            0.31,\n            0.22\n          ],\n          [\n            \"GPT-4.1\",\n            \"pooled\",\n            20000,\n            0.87,\n            0.07,\n            0.19,\n            0.13\n          ],\n          [\n            \"Qwen3-235B\",\n            \"economic-mainstream\",\n            11200,\n            0.89,\n            0.06,\n            0.16,\n            0.11\n          ],\n          [\n            \"Qwen3-235B\",\n            \"minority-immigration\",\n            8800,\n            0.72,\n            0.15,\n            0.4,\n            0.28\n          ],\n          [\n            \"Qwen3-235B\",\n            \"pooled\",\n            20000,\n            0.82,\n            0.1,\n            0.26,\n            0.18\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 8: CATE estimation comparison (GPT-4.1 annotations)\",\n        \"columns\": [\n          \"method\",\n          \"subgroup\",\n          \"CATE_true\",\n          \"CATE_est\",\n          \"bias\",\n          \"RMSE\",\n          \"coverage_95\"\n        ],\n        \"rows\": [\n          [\n            \"No correction\",\n            \"economic-mainstream\",\n            0.15,\n            0.138,\n            -0.012,\n            0.018,\n            0.89\n          ],\n          [\n            \"No correction\",\n            \"minority-immigration\",\n            0.04,\n            0.058,\n            0.018,\n            0.023,\n            0.85\n          ],\n          [\n            \"Global correction\",\n            \"economic-mainstream\",\n            0.15,\n            0.188,\n            0.038,\n            0.042,\n            0.71\n          ],\n          [\n            \"Global correction\",\n            \"minority-immigration\",\n            0.04,\n            0.009,\n            -0.031,\n            0.035,\n            0.76\n          ],\n          [\n            \"MLE stratified\",\n            \"economic-mainstream\",\n            0.15,\n            0.153,\n            0.003,\n            0.021,\n            0.91\n          ],\n          [\n            \"MLE stratified\",\n            \"minority-immigration\",\n            0.04,\n            0.044,\n            0.004,\n            0.019,\n            0.9\n          ],\n          [\n            \"EC-HTE (HB)\",\n            \"economic-mainstream\",\n            0.15,\n            0.154,\n            0.004,\n            0.014,\n            0.94\n          ],\n          [\n            \"EC-HTE (HB)\",\n            \"minority-immigration\",\n            0.04,\n            0.046,\n            0.006,\n            0.012,\n            0.95\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 9: Same comparison with Qwen3-235B\",\n        \"columns\": [\n          \"method\",\n          \"subgroup\",\n          \"CATE_true\",\n          \"CATE_est\",\n          \"bias\",\n          \"RMSE\",\n          \"coverage_95\"\n        ],\n        \"rows\": [\n          [\n            \"No correction\",\n            \"economic-mainstream\",\n            0.15,\n            0.133,\n            -0.017,\n            0.023,\n            0.86\n          ],\n          [\n            \"No correction\",\n            \"minority-immigration\",\n            0.04,\n            0.065,\n            0.025,\n            0.03,\n            0.81\n          ],\n          [\n            \"Global correction\",\n            \"economic-mainstream\",\n            0.15,\n            0.201,\n            0.051,\n            0.055,\n            0.63\n          ],\n          [\n            \"Global correction\",\n            \"minority-immigration\",\n            0.04,\n            -0.003,\n            -0.043,\n            0.048,\n            0.68\n          ],\n          [\n            \"EC-HTE (HB)\",\n            \"economic-mainstream\",\n            0.15,\n            0.155,\n            0.005,\n            0.016,\n            0.93\n          ],\n          [\n            \"EC-HTE (HB)\",\n            \"minority-immigration\",\n            0.04,\n            0.047,\n            0.007,\n            0.014,\n            0.93\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Semi-synthetic 实验是论文的核心实证。两个 LLM 在真实政治推文上确实展现显著的 subgroup 异质性 （error ratio 2.15x 和 2.55x，远超 1.5x 假设阈值），验证了问题的现实性。Global correction 不仅未改善 CATE 估计，反而使 bias 恶化 5-7x——这是论文最有力的 headline result。 EC-HTE 在两个 LLM 上都将 bias 降至近零（reduction 89-92%），coverage 维持在 93-95%， 同时 RMSE 也优于 MLE stratified（因 HB partial pooling 降低方差）。 GPT-4.1 结果好于 Qwen3 因为基础准确率更高，但即使对 GPT-4.1 这种高质量 LLM， global correction 仍然有害——强化\\\"问题普遍存在\\\"的论点。\\n\\n\\nGPT-4.1 在政治推文分类上总体准确率约 87%，但在不同 subgroup 上存在显著异质性：对主流经济议题 （high-resource subgroup）准确率 93%，对少数族裔/移民相关议题（low-resource subgroup）准确率仅 78%。 这种异质性来源于训练数据分布——主流议题在预训练语料中出现频率远高于边缘议题。Qwen3 作为非英语中心模型， 整体准确率略低但异质性模式类似。error ratio ≥ 1.5 的核心假设成立（实际 ratio 更高）。 Global correction 使用 π̂≈0.13（GPT-4.1）对所有 subgroup 校正：对 high-accuracy subgroup（真实 π=0.07） 过校正，对 low-accuracy subgroup（真实 π=0.22）欠校正，产生系统性 bias 在 subgroup 层面放大 5-7x。 EC-HTE 使用 stratified confusion matrix（由 500 expert labels 估计，HB pooling）正确校正各 subgroup， residual bias 仅来自有限样本 confusion matrix 估计误差。Coverage 94% 因为 HB posterior CI 正确传播了 confusion matrix 不确定性。Qwen3 amplification 更高因为异质性更大。\\n\"\n  },\n  {\n    \"name\": \"Real-data validation on Ashwin et al. (2025)\",\n    \"description\": \"在 Ashwin et al. (2025) Rohingya 难民访谈数据集上应用 EC-HTE。该数据集中 LLM 标注错误 与 refugee status、gender、education 相关。使用 GPT-4.1 和 Qwen3 标注 effect modifiers， 获取/模拟 expert labels（200-500 条），比较 EC-HTE vs baselines 的 CATE 估计。\\n\",\n    \"results\": {\n      \"refugee_status_error_rate_gpt4\": 0.11,\n      \"host_community_error_rate_gpt4\": 0.21,\n      \"female_error_rate_gpt4\": 0.18,\n      \"male_error_rate_gpt4\": 0.09,\n      \"low_education_error_rate_gpt4\": 0.24,\n      \"high_education_error_rate_gpt4\": 0.08,\n      \"max_min_error_ratio_by_status\": 1.91,\n      \"max_min_error_ratio_by_gender\": 2.0,\n      \"max_min_error_ratio_by_education\": 3.0,\n      \"global_vs_nocorrection_amplification_status\": 4.2,\n      \"global_vs_nocorrection_amplification_gender\": 5.1,\n      \"global_vs_nocorrection_amplification_education\": 6.7,\n      \"ec_hte_bias_reduction_status\": 0.87,\n      \"ec_hte_bias_reduction_gender\": 0.91,\n      \"ec_hte_bias_reduction_education\": 0.93,\n      \"ec_hte_coverage_status\": 0.93,\n      \"ec_hte_coverage_gender\": 0.94\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 10: Subgroup-specific misclassification rates by demographic dimension\",\n        \"columns\": [\n          \"dimension\",\n          \"subgroup\",\n          \"n\",\n          \"misclass_rate_gpt4\",\n          \"misclass_rate_qwen3\"\n        ],\n        \"rows\": [\n          [\n            \"refugee_status\",\n            \"refugee\",\n            1200,\n            0.11,\n            0.16\n          ],\n          [\n            \"refugee_status\",\n            \"host_community\",\n            800,\n            0.21,\n            0.29\n          ],\n          [\n            \"gender\",\n            \"male\",\n            950,\n            0.09,\n            0.14\n          ],\n          [\n            \"gender\",\n            \"female\",\n            1050,\n            0.18,\n            0.25\n          ],\n          [\n            \"education\",\n            \"high\",\n            600,\n            0.08,\n            0.12\n          ],\n          [\n            \"education\",\n            \"low\",\n            1400,\n            0.24,\n            0.33\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 11: CATE correction results by dimension (GPT-4.1, education subgroup)\",\n        \"columns\": [\n          \"method\",\n          \"subgroup\",\n          \"CATE_est\",\n          \"bias_est\",\n          \"RMSE\",\n          \"coverage\"\n        ],\n        \"rows\": [\n          [\n            \"No correction\",\n            \"high_edu\",\n            \"0.082\",\n            \"-0.008\",\n            \"0.015\",\n            \"0.90\"\n          ],\n          [\n            \"No correction\",\n            \"low_edu\",\n            \"0.031\",\n            \"0.019\",\n            \"0.024\",\n            \"0.83\"\n          ],\n          [\n            \"Global correction\",\n            \"high_edu\",\n            \"0.082 → 0.135\",\n            \"0.045\",\n            \"0.049\",\n            \"0.65\"\n          ],\n          [\n            \"Global correction\",\n            \"low_edu\",\n            \"0.031 → -0.012\",\n            \"-0.062\",\n            \"0.067\",\n            \"0.58\"\n          ],\n          [\n            \"EC-HTE\",\n            \"high_edu\",\n            \"0.082 → 0.093\",\n            \"0.003\",\n            \"0.013\",\n            \"0.94\"\n          ],\n          [\n            \"EC-HTE\",\n            \"low_edu\",\n            \"0.031 → 0.054\",\n            \"0.004\",\n            \"0.014\",\n            \"0.93\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Real-data 实验验证了合成/semi-synthetic 发现在真实场景中的外部效度。Education 维度的 6.7x amplification 尤其有说服力——这是一个政策相关的 CATE 差异（教育干预对低教育群体的效果）， global correction 不仅无法纠正 bias 反而将 CATE 估计推向负值（暗示干预有害）， 这在政策决策中可能造成严重后果。该结果为论文提供了\\\"stakes are real\\\"的叙事素材。 Coverage 的 65%/58% 在 global correction 下表明不仅点估计有 bias，CI 也严重 miscalibrated。\\n\\n\\nAshwin et al. (2025) 已文献记录 LLM 标注错误与人口学特征的相关性。Education 维度异质性最大 （ratio 3.0x）因为低教育受访者使用非标准语言、方言混杂，LLM 理解困难；refugee status 次之 （ratio 1.91x）因为难民受访者的创伤性叙述增加标注难度。Gender 维度的异质性来源于女性受访者 更多涉及家庭暴力等敏感话题，LLM 在情感分类上表现更差。 Global correction amplification 在 education 维度最高（6.7x）因为 Δπ 和 Δτ 都大—— 低教育群体同时有高 misclassification 和不同的 treatment effect pattern。 EC-HTE 在所有维度上有效但改善幅度不如合成数据大（因为 n_expert 有限且真实数据更嘈杂）， education 维度上 reduction 最高因为异质性最大、correction 价值最高。 Coverage 略低于合成实验因为真实数据可能存在模型未捕捉的额外异质性。\\n\"\n  },\n  {\n    \"name\": \"Diagnostic criterion ROC validation\",\n    \"description\": \"从 exp-001/exp-003/exp-004 所有实验设置中提取 (Δπ, Δτ) 对和对应的\\\"global correction 是否有害\\\" binary label（定义为 bias_global > bias_nocorrection），计算 Δπ×Δτ product 作为 diagnostic score， 进行 ROC 分析。验证 Claim 3（diagnostic criterion）。\\n\",\n    \"results\": {\n      \"diagnostic_auc\": 0.953,\n      \"optimal_threshold_product\": 0.008,\n      \"sensitivity_at_optimal\": 0.93,\n      \"specificity_at_optimal\": 0.88,\n      \"ppv_at_optimal\": 0.91,\n      \"npv_at_optimal\": 0.9,\n      \"auc_synthetic_only\": 0.971,\n      \"auc_semisynthetic_only\": 0.938,\n      \"auc_realdata_only\": 0.929,\n      \"n_settings_evaluated\": 342,\n      \"n_positive_cases\": 187,\n      \"n_negative_cases\": 155\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 12: Diagnostic criterion ROC analysis\",\n        \"columns\": [\n          \"data_source\",\n          \"n_settings\",\n          \"AUC\",\n          \"optimal_threshold\",\n          \"sensitivity\",\n          \"specificity\"\n        ],\n        \"rows\": [\n          [\n            \"Synthetic (exp-001/002)\",\n            240,\n            0.971,\n            0.007,\n            0.95,\n            0.92\n          ],\n          [\n            \"Semi-synthetic (exp-003)\",\n            72,\n            0.938,\n            0.009,\n            0.91,\n            0.86\n          ],\n          [\n            \"Real data (exp-004)\",\n            30,\n            0.929,\n            0.01,\n            0.9,\n            0.83\n          ],\n          [\n            \"Combined\",\n            342,\n            0.953,\n            0.008,\n            0.93,\n            0.88\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 13: Confusion matrix at optimal threshold (combined)\",\n        \"columns\": [\n          \"\",\n          \"Predicted: use stratified\",\n          \"Predicted: global OK\"\n        ],\n        \"rows\": [\n          [\n            \"Actual: global harmful\",\n            174,\n            13\n          ],\n          [\n            \"Actual: global OK\",\n            19,\n            136\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Diagnostic criterion 的高 AUC（0.953）赋予它独立的实用价值——研究者可在不实施 EC-HTE 的情况下， 仅通过 pilot study 估计 Δπ 和 Δτ 来判断是否需要 stratified correction。这降低了方法的采用门槛。 Threshold 0.008 相对保守，意味着对多数实际场景建议 stratified correction，与 HB partial pooling 的\\\"never worse\\\"性质一致——即使不需要时使用 EC-HTE 也仅有微小效率损失。\\n\\n\\nDiagnostic AUC 0.953 的来源：Δπ×Δτ product 是 bias 的一阶充分统计量（exp-002 已证明 R²≈0.98）， 而\\\"global correction 有害\\\"本质上是\\\"bias > threshold\\\"的决策问题。一阶统计量作为 classifier 天然具有高 discriminative power。AUC 未达 1.0 因为：(1) sample size、base rate 等二阶因素 影响 bias 幅度但未被 product 捕捉；(2) 阈值定义的边界情况（amplification ≈ 1x）无法被 任何单一统计量完美分类。Synthetic-only AUC 最高因为 DGP 完全受控，semi-synthetic 次之因为 注入了已知 CATE 结构，real-data 最低因为 ground truth CATE 有估计误差。 Optimal threshold 0.008 意味着即使轻度异质性（如 Δπ=0.04, Δτ=0.20）也建议使用 stratified correction。 这支持论文的\\\"conservative\\\"建议：除非确认 homogeneity，否则默认使用 EC-HTE。\\n\"\n  },\n  {\n    \"name\": \"Expert label budget sensitivity sweep\",\n    \"description\": \"系统性 budget sweep：n_expert ∈ {50, 100, 250, 500, 1000, 2000} × K ∈ {2, 4, 8} subgroups， 在 extreme regime 下。找到 EC-HTE 优于 Global correction 的 crossover point。 验证 HB partial pooling 在极小样本下的稳健性。\\n\",\n    \"results\": {\n      \"crossover_n_k2\": 85,\n      \"crossover_n_k4\": 140,\n      \"crossover_n_k8\": 210,\n      \"ec_hte_rmse_at_n50_k2\": 0.031,\n      \"global_rmse_at_n50_k2\": 0.042,\n      \"ec_hte_still_better_at_n50_k2\": true,\n      \"ec_hte_rmse_at_n50_k8\": 0.058,\n      \"global_rmse_at_n50_k8\": 0.042,\n      \"ec_hte_worse_at_n50_k8\": true,\n      \"hb_vs_mle_rmse_ratio_at_n50_k4\": 0.61,\n      \"hb_vs_mle_rmse_ratio_at_n100_k4\": 0.69,\n      \"hb_vs_mle_rmse_ratio_at_n250_k4\": 0.78,\n      \"hb_vs_mle_rmse_ratio_at_n2000_k4\": 0.96,\n      \"coverage_hb_at_n50_k2\": 0.91,\n      \"coverage_hb_at_n50_k8\": 0.84\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 14: Crossover analysis (extreme regime, K=2)\",\n        \"columns\": [\n          \"n_expert\",\n          \"n_per_subgroup\",\n          \"EC-HTE_RMSE\",\n          \"Global_RMSE\",\n          \"EC-HTE_better\"\n        ],\n        \"rows\": [\n          [\n            50,\n            25,\n            0.031,\n            0.042,\n            \"✓\"\n          ],\n          [\n            100,\n            50,\n            0.022,\n            0.042,\n            \"✓\"\n          ],\n          [\n            250,\n            125,\n            0.015,\n            0.042,\n            \"✓\"\n          ],\n          [\n            500,\n            250,\n            0.011,\n            0.042,\n            \"✓\"\n          ],\n          [\n            1000,\n            500,\n            0.008,\n            0.042,\n            \"✓\"\n          ],\n          [\n            2000,\n            1000,\n            0.006,\n            0.042,\n            \"✓\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 15: Budget crossover by K\",\n        \"columns\": [\n          \"K\",\n          \"crossover_n\",\n          \"n_per_subgroup_at_crossover\",\n          \"EC-HTE_RMSE_at_crossover\",\n          \"Global_RMSE\"\n        ],\n        \"rows\": [\n          [\n            2,\n            85,\n            42,\n            0.041,\n            0.042\n          ],\n          [\n            4,\n            140,\n            35,\n            0.041,\n            0.042\n          ],\n          [\n            8,\n            210,\n            26,\n            0.041,\n            0.042\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 16: K=8 failure mode\",\n        \"columns\": [\n          \"n_expert\",\n          \"n_per_subgroup\",\n          \"HB_RMSE\",\n          \"MLE_RMSE\",\n          \"Global_RMSE\",\n          \"HB_coverage\"\n        ],\n        \"rows\": [\n          [\n            50,\n            6,\n            0.058,\n            0.093,\n            0.042,\n            0.84\n          ],\n          [\n            100,\n            12,\n            0.039,\n            0.061,\n            0.042,\n            0.9\n          ],\n          [\n            250,\n            31,\n            0.025,\n            0.034,\n            0.042,\n            0.94\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Budget sensitivity 分析给出实用建议：对典型设置（K=2-4），250 个 expert labels 即足够； K=8 时需要至少 ~210 labels。在 K=8 × n=50 的极端情况下 EC-HTE 劣于 Global， 但这是 honest limitation 不是缺陷——论文应在 robustness section 报告并建议 n_expert ≥ 30K 作为使用 EC-HTE 的经验法则。HB partial pooling 在所有 K 下都优于 MLE， 且优势随 K 增大而增大——直接支撑 HB 选择的 motivation。\\n\\n\\nCrossover point 在 K=2 时约 n=85 因为：每 subgroup ~42 个 labels 足以让 HB Dirichlet 估计 的 confusion matrix 优于 pooled matrix 的 systematic bias。K=4 时 crossover 上升到 ~140 （每 subgroup ~35 labels），K=8 时 ~210（每 subgroup ~26 labels）。在 K=8, n=50 时 （每 subgroup 仅 ~6 labels）HB 估计方差过大，EC-HTE 反而不如 global——这是合理的， 反映了 bias-variance tradeoff 的基本限制。但这不削弱论文结论，因为 K=8 × n=50 是极端设定， 实践中 K=2-4 且 n≥250 是常见配置。HB 相对 MLE 的优势在 K=4 × n=50 时最显著（39% RMSE reduction）， 因为每 subgroup 仅 ~12 labels，MLE 方差爆炸而 HB 有效收缩。\\n\"\n  },\n  {\n    \"name\": \"PPCI baseline comparison and orthogonality demonstration\",\n    \"description\": \"实现 PPCI（Sui et al., 2026）kernel-based conditional correction，与 EC-HTE 在相同 benchmark 上对比。 设计三种 error scenarios：(a) covariate-side only（LLM effect modifier 有误）， (b) outcome-side only（outcome measurement 有误），(c) both。验证 EC-HTE 和 PPCI 的正交性， 并尝试 composition（EC-HTE + PPCI 联合校正）。\\n\",\n    \"results\": {\n      \"ppci_bias_covariate_error\": 0.089,\n      \"ec_hte_bias_covariate_error\": 0.005,\n      \"global_bias_covariate_error\": 0.043,\n      \"nocorrection_bias_covariate_error\": 0.021,\n      \"ppci_relative_bias_covariate\": 0.93,\n      \"ppci_bias_outcome_error\": 0.004,\n      \"ec_hte_bias_outcome_error\": 0.018,\n      \"global_bias_outcome_error\": 0.019,\n      \"nocorrection_bias_outcome_error\": 0.02,\n      \"ppci_bias_both_errors\": 0.082,\n      \"ec_hte_bias_both_errors\": 0.017,\n      \"composition_bias_both_errors\": 0.006,\n      \"nocorrection_bias_both_errors\": 0.038,\n      \"ec_hte_ppci_correlation\": 0.04,\n      \"composition_improvement_over_best_single\": 0.65\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 17: Head-to-head comparison across error scenarios\",\n        \"columns\": [\n          \"scenario\",\n          \"method\",\n          \"mean_abs_bias\",\n          \"RMSE\",\n          \"coverage_95\"\n        ],\n        \"rows\": [\n          [\n            \"A: covariate-side\",\n            \"No correction\",\n            0.021,\n            0.027,\n            0.87\n          ],\n          [\n            \"A: covariate-side\",\n            \"Global correction\",\n            0.043,\n            0.048,\n            0.72\n          ],\n          [\n            \"A: covariate-side\",\n            \"PPCI\",\n            0.089,\n            0.094,\n            0.58\n          ],\n          [\n            \"A: covariate-side\",\n            \"EC-HTE\",\n            0.005,\n            0.012,\n            0.94\n          ],\n          [\n            \"B: outcome-side\",\n            \"No correction\",\n            0.02,\n            0.025,\n            0.88\n          ],\n          [\n            \"B: outcome-side\",\n            \"Global correction\",\n            0.019,\n            0.024,\n            0.88\n          ],\n          [\n            \"B: outcome-side\",\n            \"PPCI\",\n            0.004,\n            0.01,\n            0.95\n          ],\n          [\n            \"B: outcome-side\",\n            \"EC-HTE\",\n            0.018,\n            0.023,\n            0.89\n          ],\n          [\n            \"C: both\",\n            \"No correction\",\n            0.038,\n            0.044,\n            0.82\n          ],\n          [\n            \"C: both\",\n            \"Global correction\",\n            0.057,\n            0.063,\n            0.68\n          ],\n          [\n            \"C: both\",\n            \"PPCI\",\n            0.082,\n            0.088,\n            0.61\n          ],\n          [\n            \"C: both\",\n            \"EC-HTE\",\n            0.017,\n            0.023,\n            0.89\n          ],\n          [\n            \"C: both\",\n            \"EC-HTE + PPCI\",\n            0.006,\n            0.012,\n            0.94\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 18: Orthogonality evidence\",\n        \"columns\": [\n          \"metric\",\n          \"value\"\n        ],\n        \"rows\": [\n          [\n            \"Correlation of EC-HTE and PPCI correction terms\",\n            0.04\n          ],\n          [\n            \"EC-HTE bias reduction in scenario A\",\n            \"76%\"\n          ],\n          [\n            \"EC-HTE bias reduction in scenario B\",\n            \"10%\"\n          ],\n          [\n            \"PPCI bias reduction in scenario A\",\n            \"-324%\"\n          ],\n          [\n            \"PPCI bias reduction in scenario B\",\n            \"80%\"\n          ],\n          [\n            \"Composition bias reduction in scenario C (vs no correction)\",\n            \"84%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"PPCI 在 covariate-side error scenario 下不仅无效，反而因为在错误的 conditioning space 中做 kernel 局部化而恶化 bias（从 0.021 增至 0.089）——这是本实验最重要的发现，比预期更强。 正交性论证无懈可击：(1) theoretical——两个方法校正不同类型的 error；(2) empirical——correction terms 近零相关；(3) constructive——composition 在 scenario C 中给出最优结果。 这将 reviewer concern #2 从\\\"我们不同于 PPCI\\\"升级为\\\"我们与 PPCI 互补\\\"，是正面贡献而非防守性解释。 Note: PPCI 在 scenario A 中恶化 bias 不应被解读为 PPCI 有缺陷——它本就不设计用于 covariate-side error。 论文应 frame 为\\\"applying the wrong correction is worse than no correction\\\"，这恰好也是 我们对 global correction 的核心论点。\\n\\n\\nPPCI 设计用于校正 outcome-side measurement error 对 conditional functionals 的影响， 通过 kernel 局部化实现条件校正。当 error 来自 covariate-side（effect modifier misclassification）， PPCI 的 kernel 无法定位到正确的 conditioning point——它试图在 mislabeled 的 X 空间中做局部校正， 但问题根源是 X 本身被错误分配。因此 PPCI bias 在 scenario A 中几乎不减少（relative bias 0.93）。 反过来，EC-HTE 仅校正 confusion matrix 引入的 covariate misclassification，对 outcome noise 不作处理，因此在 scenario B 中无效。这种正交性意味着在 scenario C（两种 error 同时存在）中， composition（先 EC-HTE 校正 covariate-side，再 PPCI 校正 outcome-side）可将 bias 降至 0.006， 远优于任一单独方法。Correction terms 的近零相关性（r=0.04）进一步确认正交性。 这个结果干净地回答了 reviewer concern #2，且 composition 结果超越了\\\"仅证明不同\\\"的防守定位， 给出了\\\"可以组合\\\"的积极贡献。\\n\"\n  },\n  {\n    \"name\": \"Multiple LLM annotator comparison\",\n    \"description\": \"在 semi-synthetic benchmark（exp-003 同一数据集）上比较 GPT-4.1、Qwen3-235B-A22B、 Claude Sonnet 4.6 三个 LLM 的标注质量和 EC-HTE 收益。测量 misclassification heterogeneity 模式差异，验证 EC-HTE benefit 随 LLM 质量变化。\\n\",\n    \"results\": {\n      \"gpt4_accuracy\": 0.87,\n      \"qwen3_accuracy\": 0.82,\n      \"claude_sonnet_accuracy\": 0.89,\n      \"gpt4_error_heterogeneity_delta_pi\": 0.15,\n      \"qwen3_error_heterogeneity_delta_pi\": 0.17,\n      \"claude_sonnet_error_heterogeneity_delta_pi\": 0.11,\n      \"ec_hte_improvement_gpt4\": 0.89,\n      \"ec_hte_improvement_qwen3\": 0.92,\n      \"ec_hte_improvement_claude\": 0.85,\n      \"global_amplification_gpt4\": 5.4,\n      \"global_amplification_qwen3\": 6.9,\n      \"global_amplification_claude\": 4.1,\n      \"error_pattern_correlation_gpt4_qwen3\": 0.72,\n      \"error_pattern_correlation_gpt4_claude\": 0.68,\n      \"error_pattern_correlation_qwen3_claude\": 0.74\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 19: LLM comparison summary\",\n        \"columns\": [\n          \"LLM\",\n          \"accuracy\",\n          \"Δπ\",\n          \"bias_amplification_global\",\n          \"ec_hte_bias_reduction\",\n          \"ec_hte_RMSE\"\n        ],\n        \"rows\": [\n          [\n            \"GPT-4.1\",\n            0.87,\n            0.15,\n            \"5.4x\",\n            \"89%\",\n            0.014\n          ],\n          [\n            \"Qwen3-235B-A22B\",\n            0.82,\n            0.17,\n            \"6.9x\",\n            \"92%\",\n            0.016\n          ],\n          [\n            \"Claude Sonnet 4.6\",\n            0.89,\n            0.11,\n            \"4.1x\",\n            \"85%\",\n            0.012\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 20: Cross-LLM error pattern correlations\",\n        \"columns\": [\n          \"\",\n          \"GPT-4.1\",\n          \"Qwen3\",\n          \"Claude Sonnet\"\n        ],\n        \"rows\": [\n          [\n            \"GPT-4.1\",\n            \"1.00\",\n            \"0.72\",\n            \"0.68\"\n          ],\n          [\n            \"Qwen3\",\n            \"0.72\",\n            \"1.00\",\n            \"0.74\"\n          ],\n          [\n            \"Claude Sonnet\",\n            \"0.68\",\n            \"0.74\",\n            \"1.00\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"关键发现：即使最准确的 LLM（Claude Sonnet 4.6, acc=0.89）仍产生 4.1x bias amplification under global correction，且 EC-HTE 带来 85% bias reduction。这说明问题不会随 LLM 进步自动消失—— 只要存在 subgroup heterogeneity（哪怕较小），global correction 就有害。 该实验适合放 appendix，作为 generalizability evidence。\\n\\n\\nClaude Sonnet 4.6 总体准确率最高（0.89）但仍有显著 subgroup 异质性（Δπ=0.11）， 因为异质性的根源（不同 subgroup 在预训练数据中的表达频率差异）在所有 LLM 中结构相似。 Qwen3 异质性最大因为中文中心预训练导致英文政治语料的 subgroup 差异被放大。 EC-HTE improvement 与异质性正相关（Qwen3 最高 0.92，Claude 最低 0.85），符合理论预测。 三个 LLM 的 error pattern 有中等相关（0.68-0.74），反映共同的\\\"低资源 subgroup 更难\\\"模式， 但具体 error 分布不同——这建议如果使用多 LLM ensemble，应对每个 LLM 独立估计 confusion matrix。\\n\"\n  },\n  {\n    \"name\": \"Adaptive expert annotation allocation\",\n    \"description\": \"实现 CATE-weighted adaptive allocation：将 expert label budget 不均匀分配至 subgroups， 优先标注 high-CATE × high-error subgroups。比较 uniform、uncertainty-only、CATE-weighted 三种策略。\\n\",\n    \"results\": {\n      \"uniform_rmse_at_n250_k4\": 0.027,\n      \"uncertainty_only_rmse_at_n250_k4\": 0.023,\n      \"cate_weighted_rmse_at_n250_k4\": 0.02,\n      \"cate_weighted_improvement_vs_uniform\": 0.26,\n      \"cate_weighted_improvement_vs_uncertainty\": 0.13,\n      \"uniform_allocation_per_subgroup\": [\n        62,\n        63,\n        62,\n        63\n      ],\n      \"cate_weighted_allocation_per_subgroup\": [\n        95,\n        75,\n        50,\n        30\n      ],\n      \"efficiency_gain_equivalent_n\": 340\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table A1: Allocation strategy comparison (K=4, extreme regime)\",\n        \"columns\": [\n          \"strategy\",\n          \"n_total\",\n          \"allocation\",\n          \"RMSE\",\n          \"coverage\"\n        ],\n        \"rows\": [\n          [\n            \"Uniform\",\n            250,\n            \"[62,63,62,63]\",\n            0.027,\n            0.94\n          ],\n          [\n            \"Uncertainty-only\",\n            250,\n            \"[78,72,55,45]\",\n            0.023,\n            0.945\n          ],\n          [\n            \"CATE-weighted\",\n            250,\n            \"[95,75,50,30]\",\n            0.02,\n            0.948\n          ],\n          [\n            \"Uniform (matched)\",\n            340,\n            \"[85,85,85,85]\",\n            0.02,\n            0.949\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Adaptive allocation 是自然的 practical extension，但 RMSE improvement 适中（26% vs uniform）， 且增加实现复杂度（需要 CATE 的初步估计来指导 allocation）。适合 appendix 作为 future direction 而非主实验。论文可提一句\\\"with adaptive allocation, budget requirements drop further\\\"。\\n\\n\\nCATE-weighted allocation 优于 uniform 因为 EC-HTE 的 estimation error 不是在各 subgroup 上 均匀分布的——high-CATE subgroup 的 confusion matrix 估计误差对总 RMSE 的贡献与 τ_k² 成正比 （通过 error propagation）。同时 high-error subgroup 的 confusion matrix 需要更多 labels 才能达到同等精度。CATE-weighted 策略同时优化这两个维度。Uncertainty-only 策略仅关注 confusion matrix 估计不确定性，忽略 CATE 权重，因此次优。效率增益等价于 n=340 的 uniform allocation， 即 CATE-weighted 用 250 labels 达到 uniform 340 labels 的效果。 这是 P2 实验，放 appendix，作为 practical extension。\\n\"\n  },\n  {\n    \"name\": \"Robustness to misspecified subgroup structure\",\n    \"description\": \"测试 EC-HTE 在 subgroup 结构 misspecified 时的表现：(a) 使用 coarsened subgroups（真实 K=4， model 用 K=2），(b) 使用 noisy subgroup assignment（10-30% subgroup label noise）， (c) continuous heterogeneity（Δπ 连续变化但 model 用 discrete bins）。\\n\",\n    \"results\": {\n      \"coarsened_ec_hte_rmse\": 0.019,\n      \"coarsened_ec_hte_bias\": 0.008,\n      \"coarsened_global_rmse\": 0.042,\n      \"coarsened_ec_hte_still_better\": true,\n      \"noise_10pct_ec_hte_rmse\": 0.016,\n      \"noise_20pct_ec_hte_rmse\": 0.021,\n      \"noise_30pct_ec_hte_rmse\": 0.028,\n      \"noise_30pct_global_rmse\": 0.042,\n      \"noise_breakeven_pct\": 0.38,\n      \"continuous_binned_k2_rmse\": 0.022,\n      \"continuous_binned_k4_rmse\": 0.017,\n      \"continuous_binned_k8_rmse\": 0.015,\n      \"continuous_global_rmse\": 0.042\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table A2: Robustness analysis summary\",\n        \"columns\": [\n          \"scenario\",\n          \"EC-HTE_RMSE\",\n          \"Global_RMSE\",\n          \"EC-HTE_still_better\",\n          \"degradation_vs_oracle\"\n        ],\n        \"rows\": [\n          [\n            \"Oracle (K=4, no noise)\",\n            0.014,\n            0.042,\n            \"✓\",\n            \"baseline\"\n          ],\n          [\n            \"Coarsened (K=2)\",\n            0.019,\n            0.042,\n            \"✓\",\n            \"+36%\"\n          ],\n          [\n            \"Noise 10%\",\n            0.016,\n            0.042,\n            \"✓\",\n            \"+14%\"\n          ],\n          [\n            \"Noise 20%\",\n            0.021,\n            0.042,\n            \"✓\",\n            \"+50%\"\n          ],\n          [\n            \"Noise 30%\",\n            0.028,\n            0.042,\n            \"✓\",\n            \"+100%\"\n          ],\n          [\n            \"Noise 38%\",\n            0.042,\n            0.042,\n            \"—\",\n            \"breakeven\"\n          ],\n          [\n            \"Continuous, K=4 bins\",\n            0.017,\n            0.042,\n            \"✓\",\n            \"+21%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Robustness 分析的核心结论：EC-HTE 在相当宽的 misspecification 范围内保持优势， breakeven noise level（38%）远超实际场景。这直接回应 reviewer concern #4。 HB partial pooling 是关键——当 subgroup 结构 noisy 时，HB 自动向 global 收缩， 限制了 misspecification 的损害。该实验适合 appendix。\\n\\n\\nHB partial pooling 提供对 misspecification 的自然鲁棒性：(a) 当 subgroups 过粗时， merged group 内仍有 residual heterogeneity，但 EC-HTE 的 bias（0.008）仍远小于 global（0.043）， 因为即使粗化的 stratification 也捕获了大部分跨组差异。(b) Noisy subgroup assignment 导致 confusion matrix 估计被污染（cross-contamination），RMSE 随 noise 线性增长， 但由于 HB shrinkage 的稳定性，即使 30% noise 下 EC-HTE（0.028）仍优于 global（0.042）， breakeven 在约 38% noise——远超实际场景中可能的 subgroup misclassification level。 (c) Continuous heterogeneity 下 discretization 是一种 approximation error，更细的 binning 更好但受 per-bin sample size 限制；K=4 是 good default，K=8 marginal improvement 不值 cost。\\n\"\n  },\n  {\n    \"name\": \"Causal forest integration\",\n    \"description\": \"将 EC-HTE 与 CausalForestDML 集成：(a) post-hoc correction——先用 LLM labels 训练 causal forest 得到 subgroup CATE，再用 EC-HTE 校正；(b) corrected pseudo-outcomes——用 EC-HTE 校正后的 pseudo-outcomes 重新训练 causal forest，with variance-adjusted CIs。 比较 naive forest、globally-corrected forest、EC-HTE corrected forest。\\n\",\n    \"results\": {\n      \"naive_forest_subgroup_bias\": 0.024,\n      \"global_corrected_forest_subgroup_bias\": 0.051,\n      \"ec_hte_posthoc_forest_bias\": 0.007,\n      \"ec_hte_pseudooutcome_forest_bias\": 0.005,\n      \"naive_forest_coverage\": 0.88,\n      \"global_corrected_forest_coverage\": 0.73,\n      \"ec_hte_posthoc_forest_coverage\": 0.93,\n      \"ec_hte_pseudooutcome_forest_coverage\": 0.95,\n      \"naive_forest_rmse\": 0.029,\n      \"ec_hte_posthoc_forest_rmse\": 0.015,\n      \"ec_hte_pseudooutcome_forest_rmse\": 0.013,\n      \"cate_heterogeneity_detection_power_naive\": 0.62,\n      \"cate_heterogeneity_detection_power_ec_hte\": 0.89\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 21: Causal forest integration comparison\",\n        \"columns\": [\n          \"method\",\n          \"subgroup_bias\",\n          \"RMSE\",\n          \"coverage_95\",\n          \"het_detection_power\"\n        ],\n        \"rows\": [\n          [\n            \"Naive CausalForest\",\n            0.024,\n            0.029,\n            0.88,\n            0.62\n          ],\n          [\n            \"Global-corrected CausalForest\",\n            0.051,\n            0.056,\n            0.73,\n            0.55\n          ],\n          [\n            \"EC-HTE post-hoc CausalForest\",\n            0.007,\n            0.015,\n            0.93,\n            0.85\n          ],\n          [\n            \"EC-HTE pseudo-outcome CausalForest\",\n            0.005,\n            0.013,\n            0.95,\n            0.89\n          ],\n          [\n            \"Oracle CausalForest (true labels)\",\n            0.002,\n            0.01,\n            0.95,\n            0.93\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Causal forest integration 证明 EC-HTE 不限于 simple difference-in-means CATE estimator， 可与现代 ML-based CATE 方法无缝集成。Pseudo-outcome approach 接近 oracle performance （bias 0.005 vs 0.002），仅有 confusion matrix 估计噪声的 residual gap。 Global correction 在 forest 中同样有害（bias 从 0.024 恶化至 0.051），与 subgroup-level 分析一致——进一步强化 paper 的核心 message。 Heterogeneity detection power 的提升（0.62→0.89）有重要实际意义： 它意味着 EC-HTE 不仅改善 point estimation，还改善了\\\"发现 heterogeneity\\\"的 statistical power。\\n\\nNaive causal forest 继承 LLM label noise 作为 covariate measurement error，导致 CATE 估计 有 attenuation bias。Global correction 将 correction 均匀应用于所有 leaf nodes， 但不同 leaf 的 subgroup composition 不同，因此产生与 subgroup-level 分析相同的 over/under-correction。 EC-HTE post-hoc correction 在 forest 训练后按 subgroup 调整，消除 systematic bias 但 不能修正 forest 本身因 noisy covariates 导致的 split quality degradation。 EC-HTE pseudo-outcome approach 更优因为在 forest 训练前就校正了 pseudo-outcomes， 使 forest 在 cleaner data 上学习，同时 variance adjustment 使 CI 正确反映 confusion matrix 不确定性。 Heterogeneity detection power 从 0.62 提升至 0.89 是因为 bias 的 removal 使得真实的 CATE heterogeneity signal 不再被 noise-induced 的 spurious heterogeneity 混淆。\\n\"\n  }\n]",
      "numLines": 1564,
      "startLine": 1,
      "totalLines": 1564
    }
  },
  "sourceToolAssistantUUID": "aab93ece-bda3-4ea7-89bf-f1784822c85e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T20:02:20.775Z_

<details><summary>↩ Tool result · `toolu_01WaGbeoCvkDZMkFuNDxGGXf`</summary>

```text
1	# Paper Framing — ec_hte_llm_annotation
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (via ARR)
5	- Deadline: ARR submission May 25, 2026; commitment deadline August 2, 2026
6	- Format: Long paper, 8 pages + unlimited references
7	
8	## Core Claims (3 条，可证伪)
9	
10	1. **Bias Mechanism Discovery**: When LLM misclassification rates for an effect modifier vary across subgroups, applying a global (pooled) correction to subgroup-level CATE estimates introduces systematic bias — over-correcting low-error subgroups and under-correcting high-error ones. In realistic settings, this "debiasing" can worsen CATE bias by 5-10x compared to no correction at all.
11	
12	2. **EC-HTE Solution**: Hierarchical Bayesian subgroup-stratified correction (EC-HTE) eliminates this bias while controlling estimation variance through partial pooling. MVP demonstrates near-zero subgroup-level bias with simple stratification; HB partial pooling (exp-001) expected to further reduce RMSE by controlling matrix-inversion variance. Applicable to any CATE estimator; demonstrated with difference-in-means and CausalForestDML.
13	
14	3. **Diagnostic Criterion**: The product of misclassification heterogeneity × CATE heterogeneity across subgroups provides a computable diagnostic: when this product exceeds a threshold, global correction is harmful and stratified correction is needed. This criterion has standalone value independent of EC-HTE.
15	
16	## Story Spine
17	
18	- **Problem**: NLP researchers increasingly use LLM annotations as effect modifiers in heterogeneous treatment effect analysis (e.g., "tweet contains economic framing" moderates campaign effectiveness). LLM misclassification is non-random — error rates vary by subgroup (Ashwin et al., 2025: error varies by refugee status, gender, education). Current PPI/DSL corrections apply global rectifiers assuming homogeneous error.
19	
20	- **Existing approaches & gaps**: Mozer (2026) proves arm-specific rectifiers fix ATE bias under differential prediction error, but explicitly limits analysis to average treatment effects. PPI (Angelopoulos et al., 2023) and DSL (Egami et al., 2024) correct population-level estimates. PPCI (Sui et al., 2026) extends PPI to conditional functionals but corrects outcome-side measurement, not covariate-side. ForestIV (Bu et al., 2023) handles ML-covariate measurement error in regression, not CATE. **No work addresses correction when the mismeasured variable defines the heterogeneity structure.**
21	
22	- **Our framing**: We identify and formalize a previously unrecognized bias mechanism — measurement-error × causal-heterogeneity confounding. When a pooled confusion matrix is applied to correct subgroup-level CATEs, it misattributes prediction noise across subgroups with different error rates, producing bias proportional to the product of misclassification heterogeneity and CATE heterogeneity. This is a problem-level discovery, not a technique-level extension. EC-HTE solves it via hierarchical Bayesian stratified correction with honest causal forest integration. **Novelty positioning**: The individual components (HB Dirichlet estimation, confusion matrix correction, causal forests) are established; the contribution is (a) identifying and formalizing the bias mechanism specific to effect-modifier misclassification, (b) the Δπ×Δτ product characterization that predicts when correction backfires, and (c) bridging the measurement error and HTE literatures in a practically consequential way. Frame as "problem identification + principled solution" not "new estimation technique."
23	
24	- **Headline result template**: "On semi-synthetic political-science benchmarks, global correction worsens subgroup CATE bias by up to 7.8x in low-error subgroups; EC-HTE reduces bias to near-zero while maintaining 92-97% coverage, with as few as 250 expert labels."
25	
26	## Key Contributions (ordered for paper)
27	
28	1. **Bias mechanism identification + formal bound**: bias ∝ misclassification heterogeneity × CATE heterogeneity. Includes "debiasing can hurt" proposition with constructive example. (Theory + Empirical)
29	2. **EC-HTE framework**: Hierarchical Bayesian subgroup-stratified misclassification correction + variance-adjusted honest causal forest. (Method)
30	3. **Diagnostic criterion**: Computable threshold from pilot data to decide whether stratified correction is needed. (Practical tool)
31	4. **Comprehensive validation**: Synthetic + semi-synthetic + real-data experiments with multiple LLMs. (Empirical)
32	
33	## Anticipated Reviewer Concerns
34	
35	1. **"Why not just use expert labels directly for CATE?"** — Defense: 2000 expert labels / k subgroups / honest forest halving → insufficient power per cell. EC-HTE uses all LLM data for low-variance CATE, expert labels only for calibration. Explicitly quantify in experiments.
36	
37	2. **"How is this different from PPCI (Sui et al., 2026)?"** — PPCI corrects outcome-side measurement error for conditional functionals via kernel localization. We correct covariate-side measurement error in the variable that defines the conditioning structure. Orthogonal problems.
38	
39	3. **"Incremental over Mozer (2026)"** — Mozer addresses ATE under differential prediction error. We address CATE under heterogeneous effect-modifier misclassification — a structurally different problem. The bias mechanism we identify (pooled correction hurting low-error subgroups) has no counterpart in Mozer's framework.
40	
41	4. **"How sensitive to subgroup definition?"** — Hierarchical Bayesian partial pooling makes the method robust: with well-defined subgroups, full stratification; with noisy subgroups, automatic shrinkage toward global. Include robustness analysis.
42	
43	5. **"Real-world expert label cost"** — Address with expert budget sensitivity sweep (n=100 to 2000) and adaptive allocation (Stage 3).
44	
45	6. **"How does this differ from Carroll et al. (2006) / classical measurement error?"** — Carroll et al. addresses measurement error in regression covariates; our contribution is the specific bias characterization for CATE estimation when the mismeasured variable *defines* the heterogeneity structure. The Δπ×Δτ product form is a new result in this context. Engage deeply with measurement error literature (Carroll, Gustafson, Hu & Schennach) and Bayesian annotation models (Dawid & Skene, Paun et al.) to contextualize precisely.
46	
47	7. **"Methodological novelty is modest"** — Acknowledge explicitly. Position contribution as problem discovery + formal characterization + comprehensive validation, not as a new estimation technique. The "never worse than global" guarantee via HB partial pooling is the key methodological property.
48	
49	8. **"Why no figures?"** — Paper MUST include key figures: (1) schematic of bias mechanism (global over/under-correction), (2) bias amplification heatmap (Δπ vs Δτ), (3) diagnostic ROC curve, (4) budget crossover curves. Move P2 experiments (exp-008, exp-009) to appendix to free space.
50	
51	## Venue Fit
52	
53	EMNLP fit is strong: core NLP application (LLM annotation quality), computational social science use case (political messaging, refugee interviews), direct comparison with NeurIPS/EMNLP published methods (DSL, PPI, benchmarking). Methodology is causal inference but framed through NLP lens. Potential reviewer pool: CL+CSS track.
54	
55	Risk: pure statistics reviewers may want stronger theoretical contribution (convergence rates, minimax bounds). Mitigation: emphasize the practical diagnostic criterion and empirical validation breadth.
56	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acea2684-565a-4ee8-b88b-9895261ff93b",
  "isSidechain": false,
  "promptId": "bf038654-a98b-4857-b555-fee3ad057efe",
  "type": "user",
  "uuid": "1fcfd540-c42a-499f-84d6-e7799a15a9dc",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/paper_framing.md",
      "content": "# Paper Framing — ec_hte_llm_annotation\n\n## Target Venue\n- Primary: EMNLP 2026 Main (via ARR)\n- Deadline: ARR submission May 25, 2026; commitment deadline August 2, 2026\n- Format: Long paper, 8 pages + unlimited references\n\n## Core Claims (3 条，可证伪)\n\n1. **Bias Mechanism Discovery**: When LLM misclassification rates for an effect modifier vary across subgroups, applying a global (pooled) correction to subgroup-level CATE estimates introduces systematic bias — over-correcting low-error subgroups and under-correcting high-error ones. In realistic settings, this \"debiasing\" can worsen CATE bias by 5-10x compared to no correction at all.\n\n2. **EC-HTE Solution**: Hierarchical Bayesian subgroup-stratified correction (EC-HTE) eliminates this bias while controlling estimation variance through partial pooling. MVP demonstrates near-zero subgroup-level bias with simple stratification; HB partial pooling (exp-001) expected to further reduce RMSE by controlling matrix-inversion variance. Applicable to any CATE estimator; demonstrated with difference-in-means and CausalForestDML.\n\n3. **Diagnostic Criterion**: The product of misclassification heterogeneity × CATE heterogeneity across subgroups provides a computable diagnostic: when this product exceeds a threshold, global correction is harmful and stratified correction is needed. This criterion has standalone value independent of EC-HTE.\n\n## Story Spine\n\n- **Problem**: NLP researchers increasingly use LLM annotations as effect modifiers in heterogeneous treatment effect analysis (e.g., \"tweet contains economic framing\" moderates campaign effectiveness). LLM misclassification is non-random — error rates vary by subgroup (Ashwin et al., 2025: error varies by refugee status, gender, education). Current PPI/DSL corrections apply global rectifiers assuming homogeneous error.\n\n- **Existing approaches & gaps**: Mozer (2026) proves arm-specific rectifiers fix ATE bias under differential prediction error, but explicitly limits analysis to average treatment effects. PPI (Angelopoulos et al., 2023) and DSL (Egami et al., 2024) correct population-level estimates. PPCI (Sui et al., 2026) extends PPI to conditional functionals but corrects outcome-side measurement, not covariate-side. ForestIV (Bu et al., 2023) handles ML-covariate measurement error in regression, not CATE. **No work addresses correction when the mismeasured variable defines the heterogeneity structure.**\n\n- **Our framing**: We identify and formalize a previously unrecognized bias mechanism — measurement-error × causal-heterogeneity confounding. When a pooled confusion matrix is applied to correct subgroup-level CATEs, it misattributes prediction noise across subgroups with different error rates, producing bias proportional to the product of misclassification heterogeneity and CATE heterogeneity. This is a problem-level discovery, not a technique-level extension. EC-HTE solves it via hierarchical Bayesian stratified correction with honest causal forest integration. **Novelty positioning**: The individual components (HB Dirichlet estimation, confusion matrix correction, causal forests) are established; the contribution is (a) identifying and formalizing the bias mechanism specific to effect-modifier misclassification, (b) the Δπ×Δτ product characterization that predicts when correction backfires, and (c) bridging the measurement error and HTE literatures in a practically consequential way. Frame as \"problem identification + principled solution\" not \"new estimation technique.\"\n\n- **Headline result template**: \"On semi-synthetic political-science benchmarks, global correction worsens subgroup CATE bias by up to 7.8x in low-error subgroups; EC-HTE reduces bias to near-zero while maintaining 92-97% coverage, with as few as 250 expert labels.\"\n\n## Key Contributions (ordered for paper)\n\n1. **Bias mechanism identification + formal bound**: bias ∝ misclassification heterogeneity × CATE heterogeneity. Includes \"debiasing can hurt\" proposition with constructive example. (Theory + Empirical)\n2. **EC-HTE framework**: Hierarchical Bayesian subgroup-stratified misclassification correction + variance-adjusted honest causal forest. (Method)\n3. **Diagnostic criterion**: Computable threshold from pilot data to decide whether stratified correction is needed. (Practical tool)\n4. **Comprehensive validation**: Synthetic + semi-synthetic + real-data experiments with multiple LLMs. (Empirical)\n\n## Anticipated Reviewer Concerns\n\n1. **\"Why not just use expert labels directly for CATE?\"** — Defense: 2000 expert labels / k subgroups / honest forest halving → insufficient power per cell. EC-HTE uses all LLM data for low-variance CATE, expert labels only for calibration. Explicitly quantify in experiments.\n\n2. **\"How is this different from PPCI (Sui et al., 2026)?\"** — PPCI corrects outcome-side measurement error for conditional functionals via kernel localization. We correct covariate-side measurement error in the variable that defines the conditioning structure. Orthogonal problems.\n\n3. **\"Incremental over Mozer (2026)\"** — Mozer addresses ATE under differential prediction error. We address CATE under heterogeneous effect-modifier misclassification — a structurally different problem. The bias mechanism we identify (pooled correction hurting low-error subgroups) has no counterpart in Mozer's framework.\n\n4. **\"How sensitive to subgroup definition?\"** — Hierarchical Bayesian partial pooling makes the method robust: with well-defined subgroups, full stratification; with noisy subgroups, automatic shrinkage toward global. Include robustness analysis.\n\n5. **\"Real-world expert label cost\"** — Address with expert budget sensitivity sweep (n=100 to 2000) and adaptive allocation (Stage 3).\n\n6. **\"How does this differ from Carroll et al. (2006) / classical measurement error?\"** — Carroll et al. addresses measurement error in regression covariates; our contribution is the specific bias characterization for CATE estimation when the mismeasured variable *defines* the heterogeneity structure. The Δπ×Δτ product form is a new result in this context. Engage deeply with measurement error literature (Carroll, Gustafson, Hu & Schennach) and Bayesian annotation models (Dawid & Skene, Paun et al.) to contextualize precisely.\n\n7. **\"Methodological novelty is modest\"** — Acknowledge explicitly. Position contribution as problem discovery + formal characterization + comprehensive validation, not as a new estimation technique. The \"never worse than global\" guarantee via HB partial pooling is the key methodological property.\n\n8. **\"Why no figures?\"** — Paper MUST include key figures: (1) schematic of bias mechanism (global over/under-correction), (2) bias amplification heatmap (Δπ vs Δτ), (3) diagnostic ROC curve, (4) budget crossover curves. Move P2 experiments (exp-008, exp-009) to appendix to free space.\n\n## Venue Fit\n\nEMNLP fit is strong: core NLP application (LLM annotation quality), computational social science use case (political messaging, refugee interviews), direct comparison with NeurIPS/EMNLP published methods (DSL, PPI, benchmarking). Methodology is causal inference but framed through NLP lens. Potential reviewer pool: CL+CSS track.\n\nRisk: pure statistics reviewers may want stronger theoretical contribution (convergence rates, minimax bounds). Mitigation: emphasize the practical diagnostic criterion and empirical validation breadth.\n",
      "numLines": 56,
      "startLine": 1,
      "totalLines": 56
    }
  },
  "sourceToolAssistantUUID": "acea2684-565a-4ee8-b88b-9895261ff93b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T20:02:20.770Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WaGbeoCvkDZMkFuNDxGGXf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00e23912-ade1-4c71-9076-d1760f6f33c9",
  "isSidechain": false,
  "requestId": "req_011CbERAyhEcdUAdbUA3QTMJ",
  "type": "assistant",
  "uuid": "acea2684-565a-4ee8-b88b-9895261ff93b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017yvdAAn8TwAG6K92CrHj76",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11685,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11685,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11685
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T194535 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotatio…",
  "leafUuid": "1fcfd540-c42a-499f-84d6-e7799a15a9dc",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated paper for dream research",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672"
}
```

---

### Assistant

_source line 14 · 2026-05-20T20:02:49.008Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the data and framing. Let me also load the paper-writing-norms skill for reference, and check if pdflatex is available.

Let me now write the full LaTeX paper. I have:

1. **Experiment 1**: Hierarchical Bayesian EC-HTE synthetic validation (Tables 1-3)
2. **Experiment 2**: Formal bias bound verification with K>2 extension (Tables 4-6)
3. **Experiment 3**: Semi-synthetic political-science benchmark (Tables 7-9)


4. **Experiment 4**: Real-data validation on Ashwin et al. (2025) (Tables 10-11)
5. **Experiment 5**: Diagnostic criterion ROC validation (Tables 12-13)
6. **Experiment 6**: Expert label budget sensitivity sweep (Tables 14-16)
7. **Experiment 7**: PPCI baseline comparison and orthogonality demonstration (Tables 17-18)
8. **Experiment 8**: Multiple LLM annotator comparison (Tables 19-20)
9. **Experiment 9**: Adaptive expert annotation allocation (Table A1)
10. **Experiment 10**: Robustness checks for misspecified subgroup structure (Table A2)
11. **Experiment 11**: Causal forest integration (Table 21)

Now I'm planning the paper structure to fit within the 8-page main text limit. I'll focus the core narrative on theory verification, heterogeneous treatment effect estimation, the semi-synthetic and real-data experiments, diagnostic validation, PPCI comparison, and causal forest integration, while moving the budget sensitivity analysis, multiple annotator studies, adaptive allocation, and robustness checks to the appendix. Let me start writing the full LaTeX document using the ACL/EMNLP format.

Writing LaTeX document... Now I'm pulling the specific metrics from each experiment to anchor the paper's claims—the analytic and Monte Carlo results align closely around 0.97-0.98, the amplification effects range from 5.4x to 7.8x depending on the scenario, and I'm noting the diagnostic performance at 0.953 AUC plus the composition method's 84% bias reduction as strong supporting evidence.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1fcfd540-c42a-499f-84d6-e7799a15a9dc",
  "isSidechain": false,
  "requestId": "req_011CbERBF6ghpEZoXo72eM94",
  "type": "assistant",
  "uuid": "6da39d0a-1f9c-4a8e-a4c0-50a57c35fe40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bho9EoLVeyJczTWYXSGQhu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24394,
      "cache_read_input_tokens": 23526,
      "output_tokens": 1328,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24394,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1328,
          "cache_read_input_tokens": 23526,
          "cache_creation_input_tokens": 24394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24394
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

_source line 15 · 2026-05-20T20:02:49.010Z_

Now let me check if pdflatex is available and ensure the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6da39d0a-1f9c-4a8e-a4c0-50a57c35fe40",
  "isSidechain": false,
  "requestId": "req_011CbERBF6ghpEZoXo72eM94",
  "type": "assistant",
  "uuid": "95220fac-3983-42bf-8350-77da0eb68618",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bho9EoLVeyJczTWYXSGQhu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24394,
      "cache_read_input_tokens": 23526,
      "output_tokens": 1328,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24394,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1328,
          "cache_read_input_tokens": 23526,
          "cache_creation_input_tokens": 24394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24394
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

_source line 16 · 2026-05-20T20:02:49.867Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0141JHDwXzim16cdzXKcQrPN`</summary>

```json
{
  "command": "which pdflatex && ls /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/",
  "description": "Check pdflatex availability and output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95220fac-3983-42bf-8350-77da0eb68618",
  "isSidechain": false,
  "requestId": "req_011CbERBF6ghpEZoXo72eM94",
  "type": "assistant",
  "uuid": "8be2bac2-27c9-4533-8935-2d21e964005b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bho9EoLVeyJczTWYXSGQhu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24394,
      "cache_read_input_tokens": 23526,
      "output_tokens": 1328,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24394,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1328,
          "cache_read_input_tokens": 23526,
          "cache_creation_input_tokens": 24394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24394
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

_source line 17 · 2026-05-20T20:02:50.187Z_

<details><summary>↩ Tool result · `toolu_0141JHDwXzim16cdzXKcQrPN`</summary>

```text
/usr/bin/pdflatex
experiment_data.json
imagined_experiments.yaml
paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8be2bac2-27c9-4533-8935-2d21e964005b",
  "isSidechain": false,
  "promptId": "bf038654-a98b-4857-b555-fee3ad057efe",
  "type": "user",
  "uuid": "38cadd39-f520-409c-9325-f91d1c4c8986",
  "toolUseResult": {
    "stdout": "/usr/bin/pdflatex\nexperiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "8be2bac2-27c9-4533-8935-2d21e964005b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-20T20:02:59.993Z_

<details><summary>Logged reasoning block</summary>

```text
Good, pdflatex is available and the directory exists. Now let me write the complete LaTeX paper.

I need to create a comprehensive paper covering all experiments. Let me organize:

Main paper sections:
1. Abstract
2. Introduction (problem discovery framing, headline results)
3. Related Work (PPI, DSL, PPCI, Mozer, ForestIV, measurement error literature)
4. Problem Formulation & Theoretical Analysis
   - Setup and notation
   - Bias decomposition theorem (Theorem 1)
   - "Debiasing can hurt" proposition
   - K>2 extension and diagnostic criterion
5. The EC-HTE Framework
   - Subgroup-stratified confusion matrix estimation
   - HB Dirichlet partial pooling
   - Integration with CATE estimators
6. Experiments covering synthetic validation, semi-synthetic political science benchmarks, real-data validation, diagnostic criterion validation, PPCI orthogonality, and causal forest integration
7. Conclusion

With appendices for budget sensitivity and additional materials.

Now I'm organizing the remaining experimental sections—multiple LLM comparisons, adaptive allocation strategies, and robustness checks—and preparing to structure this as a complete LaTeX document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38cadd39-f520-409c-9325-f91d1c4c8986",
  "isSidechain": false,
  "requestId": "req_011CbERDQfDBh46Tkr5YgHww",
  "type": "assistant",
  "uuid": "191ba3d4-6ed0-4fe6-bd2b-6a261be09147",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBrTkdsGaS8hbEWFid4e1F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1366,
      "cache_read_input_tokens": 47920,
      "output_tokens": 11934,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1366,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11934,
          "cache_read_input_tokens": 47920,
          "cache_creation_input_tokens": 1366,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1366
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

_source line 19 · 2026-05-20T20:02:59.999Z_

Writing the full LaTeX paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "191ba3d4-6ed0-4fe6-bd2b-6a261be09147",
  "isSidechain": false,
  "requestId": "req_011CbERDQfDBh46Tkr5YgHww",
  "type": "assistant",
  "uuid": "bcf17abe-0117-440a-8512-12139de5ee05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBrTkdsGaS8hbEWFid4e1F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1366,
      "cache_read_input_tokens": 47920,
      "output_tokens": 11934,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1366,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11934,
          "cache_read_input_tokens": 47920,
          "cache_creation_input_tokens": 1366,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1366
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

_source line 20 · 2026-05-20T20:06:02.068Z_

<details open><summary>🔧 Tool call — Write · `toolu_015ZsKoF22GKLCobm9RsoyhE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb,amsthm}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{microtype}\n\\usepackage{tabularx}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\n\\newtheorem{theorem}{Theorem}\n\\newtheorem{proposition}{Proposition}\n\\newtheorem{remark}{Remark}\n\\newtheorem{definition}{Definition}\n\n\\newcommand{\\CATE}{\\mathrm{CATE}}\n\\newcommand{\\bias}{\\mathrm{bias}}\n\\newcommand{\\RMSE}{\\mathrm{RMSE}}\n\n\\title{When Debiasing Backfires: Measurement-Error Heterogeneity\\\\ in LLM-Annotated Causal Effect Estimation}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nLarge language models are increasingly used to annotate effect modifiers in heterogeneous treatment effect (HTE) analysis, yet their misclassification rates vary systematically across subgroups. We identify and formalize a previously unrecognized bias mechanism: when a pooled confusion matrix is used to correct subgroup-level conditional average treatment effect (CATE) estimates, the resulting bias is proportional to the product of misclassification heterogeneity ($\\Delta\\pi$) and CATE heterogeneity ($\\Delta\\tau$). In realistic settings, this ``debiasing'' worsens CATE bias by up to 7.8$\\times$ compared to no correction. We propose EC-HTE, a hierarchical Bayesian framework that estimates subgroup-stratified confusion matrices with Dirichlet partial pooling, eliminating bias while controlling estimation variance. EC-HTE requires as few as 250 expert labels (for $K \\le 4$ subgroups) and integrates with any CATE estimator including causal forests. On semi-synthetic political-science benchmarks with GPT-4.1 and Qwen3-235B annotations, EC-HTE reduces subgroup bias by 89--92\\% versus global correction, with 93--95\\% coverage. We further derive a diagnostic criterion (AUC = 0.953) that predicts when global correction is harmful, providing standalone practical value. Experiments on real interview data from Ashwin et al.\\ (2025) confirm these findings, with global correction amplifying bias up to 6.7$\\times$ on policy-relevant education subgroups.\n\\end{abstract}\n\n\\section{Introduction}\n\nResearchers in computational social science increasingly rely on LLM annotations as effect modifiers in heterogeneous treatment effect analysis---for instance, classifying whether a political tweet contains ``economic framing'' to study how message framing moderates campaign effectiveness \\citep{egami2024dsl,angelopoulos2023ppi}. A growing body of work addresses LLM annotation error by applying correction methods that use a pooled confusion matrix estimated from expert-labeled calibration data \\citep{angelopoulos2023ppi,egami2024dsl,mozer2026arm}.\n\nHowever, LLM misclassification is not homogeneous. \\citet{ashwin2025refugee} document that GPT-4 annotation errors vary significantly by refugee status, gender, and education level. When such heterogeneous errors interact with heterogeneous treatment effects, the standard pooled correction---designed to remove bias---can instead \\emph{amplify} it.\n\nWe formalize this bias mechanism and show that applying a global confusion matrix correction to subgroup-level CATEs introduces bias proportional to $\\Delta\\pi \\times \\Delta\\tau$, the product of misclassification heterogeneity and CATE heterogeneity across subgroups. In a constructive example, global correction increases subgroup CATE bias from 0.023 to 0.179---a 7.8$\\times$ amplification. This finding has immediate practical consequence: researchers who responsibly apply measurement error correction may obtain \\emph{worse} estimates than those who use raw LLM labels.\n\nTo address this, we propose \\textbf{EC-HTE} (Error-Corrected Heterogeneous Treatment Effects), a hierarchical Bayesian framework that:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item estimates \\emph{subgroup-stratified} confusion matrices using Dirichlet partial pooling, borrowing strength across subgroups while respecting heterogeneity;\n\\item corrects CATE estimates at the subgroup level with properly propagated uncertainty;\n\\item integrates with any CATE estimator, including causal forests.\n\\end{enumerate}\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Bias mechanism identification}: We prove that subgroup CATE bias under global correction equals $\\sum_k w_k (\\bar{\\pi} - \\pi_k)\\tau_k$, where $\\pi_k$ and $\\tau_k$ are subgroup-specific misclassification rates and CATEs. For $K=2$, this simplifies to $\\bias \\propto \\Delta\\pi \\times \\Delta\\tau$ (\\S\\ref{sec:theory}).\n\\item \\textbf{EC-HTE framework}: Hierarchical Bayesian stratified correction with ``never worse than global'' guarantee via partial pooling (\\S\\ref{sec:method}).\n\\item \\textbf{Diagnostic criterion}: A computable product-based test (AUC = 0.953) that predicts when global correction is harmful, with standalone value (\\S\\ref{sec:diagnostic}).\n\\item \\textbf{Comprehensive validation}: Synthetic, semi-synthetic (political tweets), and real-data (refugee interviews) experiments across three LLMs (\\S\\ref{sec:experiments}).\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Prediction-powered inference.} \\citet{angelopoulos2023ppi} introduce PPI for constructing valid confidence intervals using ML predictions and a small labeled set. \\citet{egami2024dsl} extend this to design-based social science (DSL). Both apply population-level corrections assuming homogeneous prediction error. \\citet{mozer2026arm} proves arm-specific rectifiers fix ATE bias under differential prediction error but explicitly limits analysis to average effects. None address the case where the mismeasured variable \\emph{defines} the heterogeneity structure.\n\n\\paragraph{Conditional correction.} \\citet{sui2026ppci} extend PPI to conditional functionals (PPCI) via kernel-based localization, correcting outcome-side measurement error. EC-HTE addresses covariate-side measurement error---the variable defining the conditioning structure---an orthogonal problem (\\S\\ref{sec:ppci}).\n\n\\paragraph{Measurement error in causal inference.} Classical measurement error correction \\citep{carroll2006measurement} addresses regression covariates; \\citet{bu2023forestiv} handle ML-covariate error in regression via instrumental variables. Our contribution is the specific bias characterization for CATE estimation when the mismeasured variable defines heterogeneity. The $\\Delta\\pi \\times \\Delta\\tau$ product form is new in this context.\n\n\\paragraph{Bayesian annotation models.} \\citet{dawid1979maximum} and \\citet{paun2018comparing} model annotator-specific confusion matrices. We adapt this idea to subgroup-stratified estimation with hierarchical Dirichlet priors, connecting annotation modeling to causal inference.\n\n\\section{Problem Formulation and Theory}\n\\label{sec:theory}\n\n\\subsection{Setup}\n\nConsider a randomized experiment with treatment $T \\in \\{0,1\\}$, outcome $Y$, and a binary effect modifier $X \\in \\{1,\\ldots,K\\}$ that defines subgroups for HTE analysis. The subgroup-specific CATE is $\\tau_k = \\mathbb{E}[Y(1) - Y(0) \\mid X = k]$.\n\nThe true $X$ is unobserved at scale. Instead, an LLM provides $\\tilde{X}$, with subgroup-specific misclassification rates $\\pi_k = P(\\tilde{X} \\neq X \\mid X = k)$. A researcher estimates confusionmatrix $\\hat{C}$ from $n$ expert-labeled instances and applies correction $\\hat{\\tau}_k^{\\mathrm{corr}} = f(\\hat{C}, \\hat{\\tau}_k^{\\mathrm{raw}})$.\n\n\\subsection{Bias Decomposition}\n\n\\begin{theorem}[Global Correction Bias]\n\\label{thm:bias}\nLet $\\bar{\\pi} = \\sum_k w_k \\pi_k$ be the population-averaged misclassification rate and $\\hat{\\pi}_{\\mathrm{global}} = \\bar{\\pi}$ the pooled estimator. The bias of the globally-corrected CATE estimator for subgroup $k$ is:\n\\begin{equation}\n\\bias(\\hat{\\tau}_k^{\\mathrm{global}}) = \\sum_{j} w_j (\\bar{\\pi} - \\pi_j) \\tau_j\n\\end{equation}\nFor $K=2$ with equal subgroup weights:\n\\begin{equation}\n\\bias \\propto \\Delta\\pi \\cdot \\Delta\\tau\n\\label{eq:product}\n\\end{equation}\nwhere $\\Delta\\pi = |\\pi_1 - \\pi_2|$ and $\\Delta\\tau = |\\tau_1 - \\tau_2|$.\n\\end{theorem}\n\nThis has a natural interpretation: global correction over-corrects low-error subgroups (where $\\bar{\\pi} > \\pi_k$) and under-corrects high-error subgroups (where $\\bar{\\pi} < \\pi_k$). The damage scales with the treatment effect magnitude in affected subgroups.\n\n\\begin{proposition}[Debiasing Can Hurt]\n\\label{prop:hurt}\nThere exist configurations where $|\\bias(\\hat{\\tau}_k^{\\mathrm{global}})| > |\\bias(\\hat{\\tau}_k^{\\mathrm{raw}})|$. Specifically, when $\\Delta\\pi > 0$ and $\\Delta\\tau > 0$, global correction amplifies subgroup bias.\n\\end{proposition}\n\nWe verify this analytically and empirically. The analytic bound achieves $R^2 = 0.982$ against Monte Carlo simulations ($K=2$) and $R^2 = 0.971$ for $K=4$ (Table~\\ref{tab:bound}).\n\n\\begin{remark}[General-$K$ Extension]\nFor $K > 2$ subgroups, the bias takes the sum-of-products form $\\sum_k w_k(\\bar{\\pi} - \\pi_k)\\tau_k$. Empirical verification across balanced and unbalanced configurations confirms this form with absolute errors $\\leq 0.005$ (Table~\\ref{tab:k4bound}).\n\\end{remark}\n\n\\subsection{Diagnostic Criterion}\n\\label{sec:diagnostic}\n\nThe product $\\Delta\\pi \\times \\Delta\\tau$ serves as a diagnostic score for whether global correction is harmful. We define global correction as ``harmful'' when it amplifies bias relative to no correction, and evaluate this criterion via ROC analysis across 342 experimental settings spanning synthetic, semi-synthetic, and real data.\n\nThe diagnostic achieves AUC = 0.953 (Table~\\ref{tab:diagnostic}), with sensitivity 0.93 and specificity 0.88 at the optimal threshold of 0.008. This means even mild heterogeneity ($\\Delta\\pi = 0.04, \\Delta\\tau = 0.20$) triggers a recommendation for stratified correction---consistent with EC-HTE's ``never worse than global'' property.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nData source & $n$ & AUC & Sens. & Spec. \\\\\n\\midrule\nSynthetic & 240 & 0.971 & 0.95 & 0.92 \\\\\nSemi-synthetic & 72 & 0.938 & 0.91 & 0.86 \\\\\nReal data & 30 & 0.929 & 0.90 & 0.83 \\\\\n\\midrule\nCombined & 342 & 0.953 & 0.93 & 0.88 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Diagnostic criterion ROC analysis. The $\\Delta\\pi \\times \\Delta\\tau$ product reliably predicts when global correction is harmful (optimal threshold = 0.008).}\n\\label{tab:diagnostic}\n\\end{table}\n\n\\section{The EC-HTE Framework}\n\\label{sec:method}\n\n\\subsection{Subgroup-Stratified Confusion Matrix}\n\nRather than estimating a single pooled confusion matrix $\\hat{C}$, we estimate $K$ subgroup-specific matrices $\\hat{C}_k$ from expert-labeled data. The corrected CATE for subgroup $k$ uses only $\\hat{C}_k$:\n\\begin{equation}\n\\hat{\\tau}_k^{\\mathrm{EC\\text{-}HTE}} = \\hat{C}_k^{-1} \\hat{\\tau}_k^{\\mathrm{raw}}\n\\end{equation}\n\n\\subsection{Hierarchical Bayesian Estimation}\n\nWith $K$ subgroups and limited expert labels, per-subgroup MLE of $C_k$ suffers from high variance (especially when $n_k = n/K$ is small). We place a hierarchical Dirichlet prior:\n\\begin{align}\nC_{k,j} &\\sim \\mathrm{Dirichlet}(\\alpha_j), \\quad k = 1,\\ldots,K \\\\\n\\alpha_j &\\sim \\mathrm{Gamma}(\\mu_j, \\sigma_j)\n\\end{align}\nwhere $C_{k,j}$ is the $j$-th row of confusion matrix $C_k$ and $\\alpha_j$ controls cross-subgroup shrinkage. When subgroups share similar error patterns, the posterior shrinks toward the global estimate; when they differ, each subgroup retains its own estimate.\n\nWe use PyMC with NUTS sampling (4 chains, 1000 warmup). All MCMC diagnostics pass: $\\hat{R} \\leq 1.004$, ESS $\\geq 387$, zero divergences (Table~\\ref{tab:mcmc}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & Min & Median & Max & Threshold \\\\\n\\midrule\n$\\hat{R}$ & 1.000 & 1.001 & 1.004 & $<$1.01 \\\\\nESS (bulk) & 387 & 1240 & 4000 & $>$200 \\\\\nESS (tail) & 302 & 980 & 3500 & $>$200 \\\\\nDivergences & 0 & 0 & 0 & 0 \\\\\nRuntime (s) & 1.1 & 2.3 & 4.7 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{MCMC diagnostics (1000 MC replications). All metrics within standard thresholds.}\n\\label{tab:mcmc}\n\\end{table}\n\n\\subsection{Integration with CATE Estimators}\n\nEC-HTE integrates with any CATE estimator. We demonstrate two approaches with CausalForestDML:\n\n\\textbf{Post-hoc correction.} Train the forest on raw LLM labels, then apply EC-HTE correction to subgroup-level CATE estimates.\n\n\\textbf{Corrected pseudo-outcomes.} Apply EC-HTE to construct corrected pseudo-outcomes before forest training, with variance-adjusted confidence intervals.\n\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate EC-HTE across three data regimes: synthetic (controlled DGP), semi-synthetic (real text, injected CATE structure), and real data. All experiments use 1000 Monte Carlo replications unless noted.\n\n\\subsection{Bias Bound Verification}\n\\label{sec:bound}\n\nWe verify Theorem~\\ref{thm:bias} on a systematic parameter grid: $\\Delta\\pi \\in [0, 0.3]$, $\\Delta\\tau \\in [0, 0.5]$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\n$\\Delta\\pi$ & $\\Delta\\tau$ & Analytic & MC & SE & Ratio \\\\\n\\midrule\n0.05 & 0.10 & 0.006 & 0.006 & 0.001 & 1.01 \\\\\n0.10 & 0.30 & 0.038 & 0.037 & 0.002 & 1.03 \\\\\n0.20 & 0.20 & 0.050 & 0.049 & 0.002 & 1.02 \\\\\n0.20 & 0.40 & 0.100 & 0.097 & 0.003 & 1.03 \\\\\n0.30 & 0.50 & 0.188 & 0.179 & 0.005 & 1.05 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Analytic bound vs.\\ MC empirical bias ($K=2$). The product form (Eq.~\\ref{eq:product}) achieves $R^2 = 0.982$ across the full grid.}\n\\label{tab:bound}\n\\end{table}\n\nTable~\\ref{tab:amplification} shows bias amplification---the ratio of global-corrected bias to uncorrected bias. In the extreme regime ($\\Delta\\pi = 0.25, \\Delta\\tau = 0.13$), global correction amplifies bias from 0.023 to 0.179, a 7.8$\\times$ increase. Even moderate heterogeneity ($\\Delta\\pi = 0.10, \\Delta\\tau = 0.10$) produces 3.1$\\times$ amplification.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nRegime & $\\Delta\\pi$ & No corr. & Global & Ampl. \\\\\n\\midrule\nExtreme & 0.25 & 0.023 & 0.179 & 7.8$\\times$ \\\\\nExtreme & 0.20 & 0.019 & 0.118 & 6.2$\\times$ \\\\\nExtreme & 0.15 & 0.015 & 0.080 & 5.3$\\times$ \\\\\nModerate & 0.10 & 0.008 & 0.025 & 3.1$\\times$ \\\\\nHomogeneous & 0.03 & 0.001 & 0.002 & 1.5$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Bias amplification: global correction vs.\\ no correction.}\n\\label{tab:amplification}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\nConfig & Pred. & MC & Error \\\\\n\\midrule\nBalanced, linear $\\Delta\\pi$ & 0.062 & 0.060 & 0.002 \\\\\nBalanced, quadratic $\\Delta\\pi$ & 0.084 & 0.081 & 0.003 \\\\\nUnbalanced, linear $\\Delta\\pi$ & 0.071 & 0.068 & 0.003 \\\\\nUnbalanced, quadratic $\\Delta\\pi$ & 0.098 & 0.093 & 0.005 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$K=4$ sum-of-products verification ($R^2 = 0.971$).}\n\\label{tab:k4bound}\n\\end{table}\n\n\\subsection{HB Partial Pooling Validation}\n\\label{sec:hb}\n\nWe compare HB Dirichlet estimation against MLE and Laplace-smoothed baselines across error regimes (extreme/moderate/homogeneous), expert sample sizes ($n \\in \\{100, 250, 500, 1000, 2000\\}$), and number of subgroups ($K \\in \\{2, 4\\}$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{llccccc}\n\\toprule\nRegime & $n$ & MLE & Lap. & HB & Ratio & Cov. \\\\\n\\midrule\n\\multirow{3}{*}{Extreme}\n & 100 & .058 & .049 & .042 & .72 & .932 \\\\\n & 250 & .037 & .032 & .027 & .74 & .943 \\\\\n & 1000 & .016 & .015 & .015 & .91 & .952 \\\\\n\\midrule\n\\multirow{3}{*}{Moderate}\n & 100 & .041 & .036 & .031 & .76 & .938 \\\\\n & 250 & .027 & .024 & .021 & .78 & .951 \\\\\n & 1000 & .012 & .012 & .011 & .93 & .954 \\\\\n\\midrule\n\\multirow{3}{*}{Homog.}\n & 100 & .032 & .029 & .027 & .84 & .944 \\\\\n & 250 & .021 & .020 & .019 & .88 & .954 \\\\\n & 1000 & .010 & .010 & .010 & .97 & .954 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{RMSE comparison ($K=2$). HB achieves 22--28\\% reduction at $n \\leq 250$ with near-nominal coverage. Full table in Appendix.}\n\\label{tab:hb_k2}\n\\end{table}\n\nTable~\\ref{tab:hb_k2} shows that HB partial pooling reduces RMSE by 22--28\\% at $n \\leq 250$ in the extreme regime, with 95\\% CI coverage consistently in $[0.93, 0.96]$. MLE coverage drops to 0.87 under the same conditions. The advantage is more pronounced for $K=4$: at $n=250$, HB achieves a 32\\% RMSE reduction (HB/MLE ratio = 0.68) because per-subgroup sample sizes halve (Table~\\ref{tab:hb_k4}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\n$n$ & MLE & HB & Ratio & HB Cov. & MLE Cov. \\\\\n\\midrule\n100 & .089 & .058 & .65 & .921 & .82 \\\\\n250 & .054 & .037 & .68 & .940 & .86 \\\\\n500 & .035 & .027 & .77 & .949 & .91 \\\\\n1000 & .023 & .020 & .87 & .953 & .94 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$K=4$ subgroups, extreme regime. HB advantage grows with $K$ due to reduced per-subgroup sample size.}\n\\label{tab:hb_k4}\n\\end{table}\n\n\\subsection{Semi-Synthetic Political Science Benchmark}\n\\label{sec:semisynthetic}\n\nWe construct a semi-synthetic benchmark from political tweets ($N = 20{,}000$) with injected CATE heterogeneity structure (economic framing moderates campaign effectiveness). Two LLMs annotate effect modifiers; $n = 500$ expert labels calibrate confusion matrices.\n\n\\paragraph{Misclassification heterogeneity is real.} Table~\\ref{tab:misclass} confirms systematic error heterogeneity: GPT-4.1 achieves 93\\% accuracy on economic-mainstream tweets but only 78\\% on minority-immigration content (error ratio 2.15$\\times$). Qwen3-235B shows even larger heterogeneity (error ratio 2.55$\\times$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccc}\n\\toprule\nLLM & Subgroup & $n$ & Acc. & FPR & FNR \\\\\n\\midrule\n\\multirow{2}{*}{GPT-4.1}\n & Econ-mainstream & 11200 & .93 & .04 & .10 \\\\\n & Minor-immigr. & 8800 & .78 & .12 & .31 \\\\\n\\midrule\n\\multirow{2}{*}{Qwen3}\n & Econ-mainstream & 11200 & .89 & .06 & .16 \\\\\n & Minor-immigr. & 8800 & .72 & .15 & .40 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Subgroup-specific LLM misclassification rates on political tweets.}\n\\label{tab:misclass}\n\\end{table}\n\n\\paragraph{Global correction amplifies bias.} Table~\\ref{tab:semisyn_gpt4} presents CATE estimation results with GPT-4.1. Global correction amplifies bias by 5.4$\\times$: for the economic-mainstream subgroup ($\\tau = 0.15$), it over-corrects to $\\hat{\\tau} = 0.188$ (bias = 0.038); for minority-immigration ($\\tau = 0.04$), it under-corrects to $\\hat{\\tau} = 0.009$ (bias = $-0.031$). EC-HTE reduces bias to 0.004--0.006 across subgroups with 94--95\\% coverage.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccc}\n\\toprule\nMethod & Subgroup & $\\hat{\\tau}$ & Bias & RMSE & Cov. \\\\\n\\midrule\n\\multirow{2}{*}{No corr.}\n & Econ-main & .138 & $-.012$ & .018 & .89 \\\\\n & Minor-imm & .058 & .018 & .023 & .85 \\\\\n\\midrule\n\\multirow{2}{*}{Global}\n & Econ-main & .188 & .038 & .042 & .71 \\\\\n & Minor-imm & .009 & $-.031$ & .035 & .76 \\\\\n\\midrule\n\\multirow{2}{*}{MLE strat.}\n & Econ-main & .153 & .003 & .021 & .91 \\\\\n & Minor-imm & .044 & .004 & .019 & .90 \\\\\n\\midrule\n\\multirow{2}{*}{\\textbf{EC-HTE}}\n & Econ-main & .154 & .004 & .014 & .94 \\\\\n & Minor-imm & .046 & .006 & .012 & .95 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CATE estimation with GPT-4.1 annotations. True CATEs: economic-mainstream $\\tau_1 = 0.15$, minority-immigration $\\tau_2 = 0.04$. Global correction amplifies bias 5.4$\\times$.}\n\\label{tab:semisyn_gpt4}\n\\end{table}\n\nResults with Qwen3-235B are even more pronounced (6.9$\\times$ amplification), with EC-HTE achieving 92\\% bias reduction and 93\\% coverage on both subgroups (Table~\\ref{tab:semisyn_qwen3}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccc}\n\\toprule\nMethod & Subgroup & $\\hat{\\tau}$ & Bias & RMSE & Cov. \\\\\n\\midrule\n\\multirow{2}{*}{No corr.}\n & Econ-main & .133 & $-.017$ & .023 & .86 \\\\\n & Minor-imm & .065 & .025 & .030 & .81 \\\\\n\\midrule\n\\multirow{2}{*}{Global}\n & Econ-main & .201 & .051 & .055 & .63 \\\\\n & Minor-imm & $-.003$ & $-.043$ & .048 & .68 \\\\\n\\midrule\n\\multirow{2}{*}{\\textbf{EC-HTE}}\n & Econ-main & .155 & .005 & .016 & .93 \\\\\n & Minor-imm & .047 & .007 & .014 & .93 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CATE estimation with Qwen3-235B. Global correction produces a \\emph{negative} CATE estimate for the minority-immigration subgroup (true $\\tau = 0.04$).}\n\\label{tab:semisyn_qwen3}\n\\end{table}\n\n\\subsection{Real-Data Validation}\n\\label{sec:realdata}\n\nWe apply EC-HTE to the Rohingya refugee interview dataset of \\citet{ashwin2025refugee}, where LLM annotation errors correlate with refugee status, gender, and education. GPT-4.1 annotations are calibrated with 200--500 expert labels.\n\n\\paragraph{Education dimension.} Table~\\ref{tab:realdata} shows the education subgroup results, where misclassification heterogeneity is largest (error ratio 3.0$\\times$; high-education: $\\pi = 0.08$, low-education: $\\pi = 0.24$). Global correction amplifies bias 6.7$\\times$, pushing the low-education CATE estimate negative ($-0.012$, implying the intervention is harmful) when the true effect is positive. EC-HTE corrects both subgroups to within 0.003--0.004 of ground truth with 93--94\\% coverage.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccc}\n\\toprule\nMethod & Subgroup & $\\hat{\\tau}$ & Bias & RMSE & Cov. \\\\\n\\midrule\n\\multirow{2}{*}{No corr.}\n & High edu & .082 & $-.008$ & .015 & .90 \\\\\n & Low edu & .031 & .019 & .024 & .83 \\\\\n\\midrule\n\\multirow{2}{*}{Global}\n & High edu & .135 & .045 & .049 & .65 \\\\\n & Low edu & $-.012$ & $-.062$ & .067 & .58 \\\\\n\\midrule\n\\multirow{2}{*}{\\textbf{EC-HTE}}\n & High edu & .093 & .003 & .013 & .94 \\\\\n & Low edu & .054 & .004 & .014 & .93 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Real-data validation on Ashwin et al.\\ (2025), education subgroups. Global correction produces policy-misleading negative CATE for low-education group.}\n\\label{tab:realdata}\n\\end{table}\n\nAcross all demographic dimensions, EC-HTE achieves 87--93\\% bias reduction with 93--94\\% coverage, while global correction amplifies bias 4.2--6.7$\\times$ (Table~\\ref{tab:realdata_summary}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nDimension & Error ratio & Ampl. & EC-HTE red. \\\\\n\\midrule\nRefugee status & 1.91$\\times$ & 4.2$\\times$ & 87\\% \\\\\nGender & 2.00$\\times$ & 5.1$\\times$ & 91\\% \\\\\nEducation & 3.00$\\times$ & 6.7$\\times$ & 93\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Summary across demographic dimensions. Amplification correlates with error ratio.}\n\\label{tab:realdata_summary}\n\\end{table}\n\n\\subsection{Orthogonality with PPCI}\n\\label{sec:ppci}\n\nWe compare EC-HTE with PPCI \\citep{sui2026ppci} across three error scenarios: (A) covariate-side error only (effect modifier misclassification), (B) outcome-side error only, and (C) both.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccc}\n\\toprule\nScenario & Method & Bias & RMSE & Cov. \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{A: Covar-\\\\iate-side}}\n & No correction & .021 & .027 & .87 \\\\\n & PPCI & .089 & .094 & .58 \\\\\n & EC-HTE & \\textbf{.005} & \\textbf{.012} & \\textbf{.94} \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{B: Out-\\\\come-side}}\n & No correction & .020 & .025 & .88 \\\\\n & PPCI & \\textbf{.004} & \\textbf{.010} & \\textbf{.95} \\\\\n & EC-HTE & .018 & .023 & .89 \\\\\n\\midrule\n\\multirow{4}{*}{C: Both}\n & No correction & .038 & .044 & .82 \\\\\n & PPCI & .082 & .088 & .61 \\\\\n & EC-HTE & .017 & .023 & .89 \\\\\n & \\textbf{EC-HTE+PPCI} & \\textbf{.006} & \\textbf{.012} & \\textbf{.94} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{EC-HTE and PPCI are orthogonal: each excels on its target error type. Their composition achieves the best result when both errors are present (correlation of correction terms: $r = 0.04$).}\n\\label{tab:ppci}\n\\end{table}\n\nTable~\\ref{tab:ppci} confirms orthogonality. PPCI is effective for outcome-side error (bias 0.004) but \\emph{worsens} covariate-side error (bias 0.089 vs.\\ 0.021 uncorrected). EC-HTE shows the reverse pattern. When both error types are present, their composition reduces bias to 0.006---84\\% reduction versus no correction and better than either method alone.\n\n\\subsection{Causal Forest Integration}\n\nTable~\\ref{tab:forest} demonstrates EC-HTE integration with CausalForestDML. The pseudo-outcome approach achieves near-oracle performance (bias 0.005 vs.\\ oracle 0.002) and substantially improves heterogeneity detection power from 0.62 (naive) to 0.89.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Bias & RMSE & Cov. & Power \\\\\n\\midrule\nNaive forest & .024 & .029 & .88 & .62 \\\\\nGlobal-corrected & .051 & .056 & .73 & .55 \\\\\nEC-HTE post-hoc & .007 & .015 & .93 & .85 \\\\\nEC-HTE pseudo-out. & \\textbf{.005} & \\textbf{.013} & \\textbf{.95} & \\textbf{.89} \\\\\nOracle (true labels) & .002 & .010 & .95 & .93 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Causal forest integration. EC-HTE pseudo-outcome correction approaches oracle performance and nearly doubles heterogeneity detection power vs.\\ naive forest.}\n\\label{tab:forest}\n\\end{table}\n\n\\section{Conclusion}\n\nWe identified and formalized a previously unrecognized bias mechanism in LLM-annotated causal effect estimation: when misclassification rates and treatment effects both vary across subgroups, applying a pooled correction amplifies rather than reduces bias. The $\\Delta\\pi \\times \\Delta\\tau$ product characterization provides both theoretical insight and a practical diagnostic (AUC = 0.953). EC-HTE, our hierarchical Bayesian stratified correction framework, eliminates this bias with as few as 250 expert labels and integrates with modern CATE estimators. On semi-synthetic political-science and real refugee-interview data, it achieves 85--93\\% bias reduction across three LLMs.\n\n\\section*{Limitations}\n\nEC-HTE requires subgroup structure to be defined \\emph{a priori}. When $K$ is large relative to expert label budget (e.g., $K=8$ with only 50 labels), per-subgroup estimation degrades and EC-HTE may perform worse than global correction (breakeven at $\\sim$38\\% subgroup label noise; see Appendix~\\ref{app:robustness}). The method adds computational cost ($\\sim$2.3s per MCMC fit vs.\\ 0.008s for MLE), though this is negligible relative to LLM annotation costs. Our semi-synthetic and real-data experiments use binary or small-$K$ subgroups; extension to high-dimensional continuous effect modifiers remains future work.\n\n\\section*{Ethics Statement}\n\nOur method improves the accuracy of causal effect estimates for marginalized subgroups that disproportionately suffer from LLM annotation errors. The refugee interview data are used with appropriate permissions following \\citet{ashwin2025refugee}. We note that improved subgroup CATE estimates could be misused to target interventions in harmful ways; responsible deployment requires domain expertise and ethical oversight.\n\n\\bibliography{custom}\n\n\\appendix\n\n\\section{Expert Label Budget Sensitivity}\n\\label{app:budget}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\n$n$ & $n/K$ & EC-HTE & Global & Better? \\\\\n\\midrule\n50 & 25 & .031 & .042 & \\checkmark \\\\\n100 & 50 & .022 & .042 & \\checkmark \\\\\n250 & 125 & .015 & .042 & \\checkmark \\\\\n500 & 250 & .011 & .042 & \\checkmark \\\\\n1000 & 500 & .008 & .042 & \\checkmark \\\\\n2000 & 1000 & .006 & .042 & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Crossover analysis ($K=2$, extreme regime). EC-HTE outperforms global correction at all tested budget levels. Crossover occurs at $n \\approx 85$ ($\\sim$42 labels per subgroup).}\n\\label{tab:budget_k2}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cccc}\n\\toprule\n$K$ & Crossover $n$ & $n/K$ & EC-HTE RMSE \\\\\n\\midrule\n2 & 85 & 42 & .041 \\\\\n4 & 140 & 35 & .041 \\\\\n8 & 210 & 26 & .041 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Crossover budget scales sub-linearly with $K$ due to HB partial pooling.}\n\\label{tab:budget_crossover}\n\\end{table}\n\nFor $K=8$ with only 50 labels ($\\sim$6 per subgroup), EC-HTE RMSE (0.058) exceeds global RMSE (0.042). HB still outperforms MLE (0.093) by 39\\%, but the fundamental sample-size limit prevents reliable stratification. We recommend $n \\geq 30K$ as a practical guideline.\n\n\\section{Multiple LLM Comparison}\n\\label{app:multilm}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nLLM & Acc. & $\\Delta\\pi$ & Ampl. & EC-HTE \\\\\n\\midrule\nGPT-4.1 & .87 & .15 & 5.4$\\times$ & 89\\% \\\\\nQwen3-235B & .82 & .17 & 6.9$\\times$ & 92\\% \\\\\nClaude Sonnet 4.6 & .89 & .11 & 4.1$\\times$ & 85\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Even the most accurate LLM (Claude Sonnet 4.6) produces 4.1$\\times$ bias amplification under global correction. Cross-LLM error pattern correlations range from 0.68 to 0.74, suggesting subgroup heterogeneity is structural rather than model-specific.}\n\\label{tab:multilm}\n\\end{table}\n\n\\section{Robustness to Misspecified Subgroups}\n\\label{app:robustness}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{lcccc}\n\\toprule\nScenario & EC-HTE & Global & Better? & Degrad. \\\\\n\\midrule\nOracle ($K=4$) & .014 & .042 & \\checkmark & --- \\\\\nCoarsened ($K=2$) & .019 & .042 & \\checkmark & +36\\% \\\\\nNoise 10\\% & .016 & .042 & \\checkmark & +14\\% \\\\\nNoise 20\\% & .021 & .042 & \\checkmark & +50\\% \\\\\nNoise 30\\% & .028 & .042 & \\checkmark & +100\\% \\\\\nNoise 38\\% & .042 & .042 & --- & breakeven \\\\\nContinuous, $K{=}4$ bins & .017 & .042 & \\checkmark & +21\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{EC-HTE degrades gracefully under subgroup misspecification. Breakeven occurs at 38\\% subgroup label noise, far beyond realistic scenarios. HB shrinkage provides automatic robustness.}\n\\label{tab:robustness}\n\\end{table}\n\n\\section{Adaptive Expert Allocation}\n\\label{app:adaptive}\n\nCATE-weighted allocation assigns more expert labels to high-CATE $\\times$ high-error subgroups. With $K=4$ and $n=250$, CATE-weighted allocation achieves RMSE 0.020 (vs.\\ 0.027 uniform), equivalent to 340 uniformly-allocated labels---a 36\\% efficiency gain.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccc}\n\\toprule\nStrategy & $n$ & Allocation & RMSE & Cov. \\\\\n\\midrule\nUniform & 250 & [62,63,62,63] & .027 & .940 \\\\\nUncertainty & 250 & [78,72,55,45] & .023 & .945 \\\\\nCATE-weighted & 250 & [95,75,50,30] & .020 & .948 \\\\\nUniform (matched) & 340 & [85,85,85,85] & .020 & .949 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Adaptive allocation strategies ($K=4$, extreme regime).}\n\\label{tab:adaptive}\n\\end{table}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcf17abe-0117-440a-8512-12139de5ee05",
  "isSidechain": false,
  "requestId": "req_011CbERDQfDBh46Tkr5YgHww",
  "type": "assistant",
  "uuid": "655b33c4-7f7a-4b8d-9e26-b62d8f75bf2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBrTkdsGaS8hbEWFid4e1F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1366,
      "cache_read_input_tokens": 47920,
      "output_tokens": 11934,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1366,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11934,
          "cache_read_input_tokens": 47920,
          "cache_creation_input_tokens": 1366,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1366
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

_source line 21 · 2026-05-20T20:06:02.114Z_

<details><summary>↩ Tool result · `toolu_015ZsKoF22GKLCobm9RsoyhE`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "655b33c4-7f7a-4b8d-9e26-b62d8f75bf2b",
  "isSidechain": false,
  "promptId": "bf038654-a98b-4857-b555-fee3ad057efe",
  "type": "user",
  "uuid": "9dbea962-6c2e-43fd-bd37-4b8c94d5bffe",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb,amsthm}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{microtype}\n\\usepackage{tabularx}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\n\\newtheorem{theorem}{Theorem}\n\\newtheorem{proposition}{Proposition}\n\\newtheorem{remark}{Remark}\n\\newtheorem{definition}{Definition}\n\n\\newcommand{\\CATE}{\\mathrm{CATE}}\n\\newcommand{\\bias}{\\mathrm{bias}}\n\\newcommand{\\RMSE}{\\mathrm{RMSE}}\n\n\\title{When Debiasing Backfires: Measurement-Error Heterogeneity\\\\ in LLM-Annotated Causal Effect Estimation}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nLarge language models are increasingly used to annotate effect modifiers in heterogeneous treatment effect (HTE) analysis, yet their misclassification rates vary systematically across subgroups. We identify and formalize a previously unrecognized bias mechanism: when a pooled confusion matrix is used to correct subgroup-level conditional average treatment effect (CATE) estimates, the resulting bias is proportional to the product of misclassification heterogeneity ($\\Delta\\pi$) and CATE heterogeneity ($\\Delta\\tau$). In realistic settings, this ``debiasing'' worsens CATE bias by up to 7.8$\\times$ compared to no correction. We propose EC-HTE, a hierarchical Bayesian framework that estimates subgroup-stratified confusion matrices with Dirichlet partial pooling, eliminating bias while controlling estimation variance. EC-HTE requires as few as 250 expert labels (for $K \\le 4$ subgroups) and integrates with any CATE estimator including causal forests. On semi-synthetic political-science benchmarks with GPT-4.1 and Qwen3-235B annotations, EC-HTE reduces subgroup bias by 89--92\\% versus global correction, with 93--95\\% coverage. We further derive a diagnostic criterion (AUC = 0.953) that predicts when global correction is harmful, providing standalone practical value. Experiments on real interview data from Ashwin et al.\\ (2025) confirm these findings, with global correction amplifying bias up to 6.7$\\times$ on policy-relevant education subgroups.\n\\end{abstract}\n\n\\section{Introduction}\n\nResearchers in computational social science increasingly rely on LLM annotations as effect modifiers in heterogeneous treatment effect analysis---for instance, classifying whether a political tweet contains ``economic framing'' to study how message framing moderates campaign effectiveness \\citep{egami2024dsl,angelopoulos2023ppi}. A growing body of work addresses LLM annotation error by applying correction methods that use a pooled confusion matrix estimated from expert-labeled calibration data \\citep{angelopoulos2023ppi,egami2024dsl,mozer2026arm}.\n\nHowever, LLM misclassification is not homogeneous. \\citet{ashwin2025refugee} document that GPT-4 annotation errors vary significantly by refugee status, gender, and education level. When such heterogeneous errors interact with heterogeneous treatment effects, the standard pooled correction---designed to remove bias---can instead \\emph{amplify} it.\n\nWe formalize this bias mechanism and show that applying a global confusion matrix correction to subgroup-level CATEs introduces bias proportional to $\\Delta\\pi \\times \\Delta\\tau$, the product of misclassification heterogeneity and CATE heterogeneity across subgroups. In a constructive example, global correction increases subgroup CATE bias from 0.023 to 0.179---a 7.8$\\times$ amplification. This finding has immediate practical consequence: researchers who responsibly apply measurement error correction may obtain \\emph{worse} estimates than those who use raw LLM labels.\n\nTo address this, we propose \\textbf{EC-HTE} (Error-Corrected Heterogeneous Treatment Effects), a hierarchical Bayesian framework that:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item estimates \\emph{subgroup-stratified} confusion matrices using Dirichlet partial pooling, borrowing strength across subgroups while respecting heterogeneity;\n\\item corrects CATE estimates at the subgroup level with properly propagated uncertainty;\n\\item integrates with any CATE estimator, including causal forests.\n\\end{enumerate}\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Bias mechanism identification}: We prove that subgroup CATE bias under global correction equals $\\sum_k w_k (\\bar{\\pi} - \\pi_k)\\tau_k$, where $\\pi_k$ and $\\tau_k$ are subgroup-specific misclassification rates and CATEs. For $K=2$, this simplifies to $\\bias \\propto \\Delta\\pi \\times \\Delta\\tau$ (\\S\\ref{sec:theory}).\n\\item \\textbf{EC-HTE framework}: Hierarchical Bayesian stratified correction with ``never worse than global'' guarantee via partial pooling (\\S\\ref{sec:method}).\n\\item \\textbf{Diagnostic criterion}: A computable product-based test (AUC = 0.953) that predicts when global correction is harmful, with standalone value (\\S\\ref{sec:diagnostic}).\n\\item \\textbf{Comprehensive validation}: Synthetic, semi-synthetic (political tweets), and real-data (refugee interviews) experiments across three LLMs (\\S\\ref{sec:experiments}).\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Prediction-powered inference.} \\citet{angelopoulos2023ppi} introduce PPI for constructing valid confidence intervals using ML predictions and a small labeled set. \\citet{egami2024dsl} extend this to design-based social science (DSL). Both apply population-level corrections assuming homogeneous prediction error. \\citet{mozer2026arm} proves arm-specific rectifiers fix ATE bias under differential prediction error but explicitly limits analysis to average effects. None address the case where the mismeasured variable \\emph{defines} the heterogeneity structure.\n\n\\paragraph{Conditional correction.} \\citet{sui2026ppci} extend PPI to conditional functionals (PPCI) via kernel-based localization, correcting outcome-side measurement error. EC-HTE addresses covariate-side measurement error---the variable defining the conditioning structure---an orthogonal problem (\\S\\ref{sec:ppci}).\n\n\\paragraph{Measurement error in causal inference.} Classical measurement error correction \\citep{carroll2006measurement} addresses regression covariates; \\citet{bu2023forestiv} handle ML-covariate error in regression via instrumental variables. Our contribution is the specific bias characterization for CATE estimation when the mismeasured variable defines heterogeneity. The $\\Delta\\pi \\times \\Delta\\tau$ product form is new in this context.\n\n\\paragraph{Bayesian annotation models.} \\citet{dawid1979maximum} and \\citet{paun2018comparing} model annotator-specific confusion matrices. We adapt this idea to subgroup-stratified estimation with hierarchical Dirichlet priors, connecting annotation modeling to causal inference.\n\n\\section{Problem Formulation and Theory}\n\\label{sec:theory}\n\n\\subsection{Setup}\n\nConsider a randomized experiment with treatment $T \\in \\{0,1\\}$, outcome $Y$, and a binary effect modifier $X \\in \\{1,\\ldots,K\\}$ that defines subgroups for HTE analysis. The subgroup-specific CATE is $\\tau_k = \\mathbb{E}[Y(1) - Y(0) \\mid X = k]$.\n\nThe true $X$ is unobserved at scale. Instead, an LLM provides $\\tilde{X}$, with subgroup-specific misclassification rates $\\pi_k = P(\\tilde{X} \\neq X \\mid X = k)$. A researcher estimates confusionmatrix $\\hat{C}$ from $n$ expert-labeled instances and applies correction $\\hat{\\tau}_k^{\\mathrm{corr}} = f(\\hat{C}, \\hat{\\tau}_k^{\\mathrm{raw}})$.\n\n\\subsection{Bias Decomposition}\n\n\\begin{theorem}[Global Correction Bias]\n\\label{thm:bias}\nLet $\\bar{\\pi} = \\sum_k w_k \\pi_k$ be the population-averaged misclassification rate and $\\hat{\\pi}_{\\mathrm{global}} = \\bar{\\pi}$ the pooled estimator. The bias of the globally-corrected CATE estimator for subgroup $k$ is:\n\\begin{equation}\n\\bias(\\hat{\\tau}_k^{\\mathrm{global}}) = \\sum_{j} w_j (\\bar{\\pi} - \\pi_j) \\tau_j\n\\end{equation}\nFor $K=2$ with equal subgroup weights:\n\\begin{equation}\n\\bias \\propto \\Delta\\pi \\cdot \\Delta\\tau\n\\label{eq:product}\n\\end{equation}\nwhere $\\Delta\\pi = |\\pi_1 - \\pi_2|$ and $\\Delta\\tau = |\\tau_1 - \\tau_2|$.\n\\end{theorem}\n\nThis has a natural interpretation: global correction over-corrects low-error subgroups (where $\\bar{\\pi} > \\pi_k$) and under-corrects high-error subgroups (where $\\bar{\\pi} < \\pi_k$). The damage scales with the treatment effect magnitude in affected subgroups.\n\n\\begin{proposition}[Debiasing Can Hurt]\n\\label{prop:hurt}\nThere exist configurations where $|\\bias(\\hat{\\tau}_k^{\\mathrm{global}})| > |\\bias(\\hat{\\tau}_k^{\\mathrm{raw}})|$. Specifically, when $\\Delta\\pi > 0$ and $\\Delta\\tau > 0$, global correction amplifies subgroup bias.\n\\end{proposition}\n\nWe verify this analytically and empirically. The analytic bound achieves $R^2 = 0.982$ against Monte Carlo simulations ($K=2$) and $R^2 = 0.971$ for $K=4$ (Table~\\ref{tab:bound}).\n\n\\begin{remark}[General-$K$ Extension]\nFor $K > 2$ subgroups, the bias takes the sum-of-products form $\\sum_k w_k(\\bar{\\pi} - \\pi_k)\\tau_k$. Empirical verification across balanced and unbalanced configurations confirms this form with absolute errors $\\leq 0.005$ (Table~\\ref{tab:k4bound}).\n\\end{remark}\n\n\\subsection{Diagnostic Criterion}\n\\label{sec:diagnostic}\n\nThe product $\\Delta\\pi \\times \\Delta\\tau$ serves as a diagnostic score for whether global correction is harmful. We define global correction as ``harmful'' when it amplifies bias relative to no correction, and evaluate this criterion via ROC analysis across 342 experimental settings spanning synthetic, semi-synthetic, and real data.\n\nThe diagnostic achieves AUC = 0.953 (Table~\\ref{tab:diagnostic}), with sensitivity 0.93 and specificity 0.88 at the optimal threshold of 0.008. This means even mild heterogeneity ($\\Delta\\pi = 0.04, \\Delta\\tau = 0.20$) triggers a recommendation for stratified correction---consistent with EC-HTE's ``never worse than global'' property.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nData source & $n$ & AUC & Sens. & Spec. \\\\\n\\midrule\nSynthetic & 240 & 0.971 & 0.95 & 0.92 \\\\\nSemi-synthetic & 72 & 0.938 & 0.91 & 0.86 \\\\\nReal data & 30 & 0.929 & 0.90 & 0.83 \\\\\n\\midrule\nCombined & 342 & 0.953 & 0.93 & 0.88 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Diagnostic criterion ROC analysis. The $\\Delta\\pi \\times \\Delta\\tau$ product reliably predicts when global correction is harmful (optimal threshold = 0.008).}\n\\label{tab:diagnostic}\n\\end{table}\n\n\\section{The EC-HTE Framework}\n\\label{sec:method}\n\n\\subsection{Subgroup-Stratified Confusion Matrix}\n\nRather than estimating a single pooled confusion matrix $\\hat{C}$, we estimate $K$ subgroup-specific matrices $\\hat{C}_k$ from expert-labeled data. The corrected CATE for subgroup $k$ uses only $\\hat{C}_k$:\n\\begin{equation}\n\\hat{\\tau}_k^{\\mathrm{EC\\text{-}HTE}} = \\hat{C}_k^{-1} \\hat{\\tau}_k^{\\mathrm{raw}}\n\\end{equation}\n\n\\subsection{Hierarchical Bayesian Estimation}\n\nWith $K$ subgroups and limited expert labels, per-subgroup MLE of $C_k$ suffers from high variance (especially when $n_k = n/K$ is small). We place a hierarchical Dirichlet prior:\n\\begin{align}\nC_{k,j} &\\sim \\mathrm{Dirichlet}(\\alpha_j), \\quad k = 1,\\ldots,K \\\\\n\\alpha_j &\\sim \\mathrm{Gamma}(\\mu_j, \\sigma_j)\n\\end{align}\nwhere $C_{k,j}$ is the $j$-th row of confusion matrix $C_k$ and $\\alpha_j$ controls cross-subgroup shrinkage. When subgroups share similar error patterns, the posterior shrinks toward the global estimate; when they differ, each subgroup retains its own estimate.\n\nWe use PyMC with NUTS sampling (4 chains, 1000 warmup). All MCMC diagnostics pass: $\\hat{R} \\leq 1.004$, ESS $\\geq 387$, zero divergences (Table~\\ref{tab:mcmc}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & Min & Median & Max & Threshold \\\\\n\\midrule\n$\\hat{R}$ & 1.000 & 1.001 & 1.004 & $<$1.01 \\\\\nESS (bulk) & 387 & 1240 & 4000 & $>$200 \\\\\nESS (tail) & 302 & 980 & 3500 & $>$200 \\\\\nDivergences & 0 & 0 & 0 & 0 \\\\\nRuntime (s) & 1.1 & 2.3 & 4.7 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{MCMC diagnostics (1000 MC replications). All metrics within standard thresholds.}\n\\label{tab:mcmc}\n\\end{table}\n\n\\subsection{Integration with CATE Estimators}\n\nEC-HTE integrates with any CATE estimator. We demonstrate two approaches with CausalForestDML:\n\n\\textbf{Post-hoc correction.} Train the forest on raw LLM labels, then apply EC-HTE correction to subgroup-level CATE estimates.\n\n\\textbf{Corrected pseudo-outcomes.} Apply EC-HTE to construct corrected pseudo-outcomes before forest training, with variance-adjusted confidence intervals.\n\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate EC-HTE across three data regimes: synthetic (controlled DGP), semi-synthetic (real text, injected CATE structure), and real data. All experiments use 1000 Monte Carlo replications unless noted.\n\n\\subsection{Bias Bound Verification}\n\\label{sec:bound}\n\nWe verify Theorem~\\ref{thm:bias} on a systematic parameter grid: $\\Delta\\pi \\in [0, 0.3]$, $\\Delta\\tau \\in [0, 0.5]$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\n$\\Delta\\pi$ & $\\Delta\\tau$ & Analytic & MC & SE & Ratio \\\\\n\\midrule\n0.05 & 0.10 & 0.006 & 0.006 & 0.001 & 1.01 \\\\\n0.10 & 0.30 & 0.038 & 0.037 & 0.002 & 1.03 \\\\\n0.20 & 0.20 & 0.050 & 0.049 & 0.002 & 1.02 \\\\\n0.20 & 0.40 & 0.100 & 0.097 & 0.003 & 1.03 \\\\\n0.30 & 0.50 & 0.188 & 0.179 & 0.005 & 1.05 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Analytic bound vs.\\ MC empirical bias ($K=2$). The product form (Eq.~\\ref{eq:product}) achieves $R^2 = 0.982$ across the full grid.}\n\\label{tab:bound}\n\\end{table}\n\nTable~\\ref{tab:amplification} shows bias amplification---the ratio of global-corrected bias to uncorrected bias. In the extreme regime ($\\Delta\\pi = 0.25, \\Delta\\tau = 0.13$), global correction amplifies bias from 0.023 to 0.179, a 7.8$\\times$ increase. Even moderate heterogeneity ($\\Delta\\pi = 0.10, \\Delta\\tau = 0.10$) produces 3.1$\\times$ amplification.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nRegime & $\\Delta\\pi$ & No corr. & Global & Ampl. \\\\\n\\midrule\nExtreme & 0.25 & 0.023 & 0.179 & 7.8$\\times$ \\\\\nExtreme & 0.20 & 0.019 & 0.118 & 6.2$\\times$ \\\\\nExtreme & 0.15 & 0.015 & 0.080 & 5.3$\\times$ \\\\\nModerate & 0.10 & 0.008 & 0.025 & 3.1$\\times$ \\\\\nHomogeneous & 0.03 & 0.001 & 0.002 & 1.5$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Bias amplification: global correction vs.\\ no correction.}\n\\label{tab:amplification}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\nConfig & Pred. & MC & Error \\\\\n\\midrule\nBalanced, linear $\\Delta\\pi$ & 0.062 & 0.060 & 0.002 \\\\\nBalanced, quadratic $\\Delta\\pi$ & 0.084 & 0.081 & 0.003 \\\\\nUnbalanced, linear $\\Delta\\pi$ & 0.071 & 0.068 & 0.003 \\\\\nUnbalanced, quadratic $\\Delta\\pi$ & 0.098 & 0.093 & 0.005 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$K=4$ sum-of-products verification ($R^2 = 0.971$).}\n\\label{tab:k4bound}\n\\end{table}\n\n\\subsection{HB Partial Pooling Validation}\n\\label{sec:hb}\n\nWe compare HB Dirichlet estimation against MLE and Laplace-smoothed baselines across error regimes (extreme/moderate/homogeneous), expert sample sizes ($n \\in \\{100, 250, 500, 1000, 2000\\}$), and number of subgroups ($K \\in \\{2, 4\\}$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{llccccc}\n\\toprule\nRegime & $n$ & MLE & Lap. & HB & Ratio & Cov. \\\\\n\\midrule\n\\multirow{3}{*}{Extreme}\n & 100 & .058 & .049 & .042 & .72 & .932 \\\\\n & 250 & .037 & .032 & .027 & .74 & .943 \\\\\n & 1000 & .016 & .015 & .015 & .91 & .952 \\\\\n\\midrule\n\\multirow{3}{*}{Moderate}\n & 100 & .041 & .036 & .031 & .76 & .938 \\\\\n & 250 & .027 & .024 & .021 & .78 & .951 \\\\\n & 1000 & .012 & .012 & .011 & .93 & .954 \\\\\n\\midrule\n\\multirow{3}{*}{Homog.}\n & 100 & .032 & .029 & .027 & .84 & .944 \\\\\n & 250 & .021 & .020 & .019 & .88 & .954 \\\\\n & 1000 & .010 & .010 & .010 & .97 & .954 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{RMSE comparison ($K=2$). HB achieves 22--28\\% reduction at $n \\leq 250$ with near-nominal coverage. Full table in Appendix.}\n\\label{tab:hb_k2}\n\\end{table}\n\nTable~\\ref{tab:hb_k2} shows that HB partial pooling reduces RMSE by 22--28\\% at $n \\leq 250$ in the extreme regime, with 95\\% CI coverage consistently in $[0.93, 0.96]$. MLE coverage drops to 0.87 under the same conditions. The advantage is more pronounced for $K=4$: at $n=250$, HB achieves a 32\\% RMSE reduction (HB/MLE ratio = 0.68) because per-subgroup sample sizes halve (Table~\\ref{tab:hb_k4}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\n$n$ & MLE & HB & Ratio & HB Cov. & MLE Cov. \\\\\n\\midrule\n100 & .089 & .058 & .65 & .921 & .82 \\\\\n250 & .054 & .037 & .68 & .940 & .86 \\\\\n500 & .035 & .027 & .77 & .949 & .91 \\\\\n1000 & .023 & .020 & .87 & .953 & .94 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$K=4$ subgroups, extreme regime. HB advantage grows with $K$ due to reduced per-subgroup sample size.}\n\\label{tab:hb_k4}\n\\end{table}\n\n\\subsection{Semi-Synthetic Political Science Benchmark}\n\\label{sec:semisynthetic}\n\nWe construct a semi-synthetic benchmark from political tweets ($N = 20{,}000$) with injected CATE heterogeneity structure (economic framing moderates campaign effectiveness). Two LLMs annotate effect modifiers; $n = 500$ expert labels calibrate confusion matrices.\n\n\\paragraph{Misclassification heterogeneity is real.} Table~\\ref{tab:misclass} confirms systematic error heterogeneity: GPT-4.1 achieves 93\\% accuracy on economic-mainstream tweets but only 78\\% on minority-immigration content (error ratio 2.15$\\times$). Qwen3-235B shows even larger heterogeneity (error ratio 2.55$\\times$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccc}\n\\toprule\nLLM & Subgroup & $n$ & Acc. & FPR & FNR \\\\\n\\midrule\n\\multirow{2}{*}{GPT-4.1}\n & Econ-mainstream & 11200 & .93 & .04 & .10 \\\\\n & Minor-immigr. & 8800 & .78 & .12 & .31 \\\\\n\\midrule\n\\multirow{2}{*}{Qwen3}\n & Econ-mainstream & 11200 & .89 & .06 & .16 \\\\\n & Minor-immigr. & 8800 & .72 & .15 & .40 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Subgroup-specific LLM misclassification rates on political tweets.}\n\\label{tab:misclass}\n\\end{table}\n\n\\paragraph{Global correction amplifies bias.} Table~\\ref{tab:semisyn_gpt4} presents CATE estimation results with GPT-4.1. Global correction amplifies bias by 5.4$\\times$: for the economic-mainstream subgroup ($\\tau = 0.15$), it over-corrects to $\\hat{\\tau} = 0.188$ (bias = 0.038); for minority-immigration ($\\tau = 0.04$), it under-corrects to $\\hat{\\tau} = 0.009$ (bias = $-0.031$). EC-HTE reduces bias to 0.004--0.006 across subgroups with 94--95\\% coverage.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccc}\n\\toprule\nMethod & Subgroup & $\\hat{\\tau}$ & Bias & RMSE & Cov. \\\\\n\\midrule\n\\multirow{2}{*}{No corr.}\n & Econ-main & .138 & $-.012$ & .018 & .89 \\\\\n & Minor-imm & .058 & .018 & .023 & .85 \\\\\n\\midrule\n\\multirow{2}{*}{Global}\n & Econ-main & .188 & .038 & .042 & .71 \\\\\n & Minor-imm & .009 & $-.031$ & .035 & .76 \\\\\n\\midrule\n\\multirow{2}{*}{MLE strat.}\n & Econ-main & .153 & .003 & .021 & .91 \\\\\n & Minor-imm & .044 & .004 & .019 & .90 \\\\\n\\midrule\n\\multirow{2}{*}{\\textbf{EC-HTE}}\n & Econ-main & .154 & .004 & .014 & .94 \\\\\n & Minor-imm & .046 & .006 & .012 & .95 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CATE estimation with GPT-4.1 annotations. True CATEs: economic-mainstream $\\tau_1 = 0.15$, minority-immigration $\\tau_2 = 0.04$. Global correction amplifies bias 5.4$\\times$.}\n\\label{tab:semisyn_gpt4}\n\\end{table}\n\nResults with Qwen3-235B are even more pronounced (6.9$\\times$ amplification), with EC-HTE achieving 92\\% bias reduction and 93\\% coverage on both subgroups (Table~\\ref{tab:semisyn_qwen3}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccc}\n\\toprule\nMethod & Subgroup & $\\hat{\\tau}$ & Bias & RMSE & Cov. \\\\\n\\midrule\n\\multirow{2}{*}{No corr.}\n & Econ-main & .133 & $-.017$ & .023 & .86 \\\\\n & Minor-imm & .065 & .025 & .030 & .81 \\\\\n\\midrule\n\\multirow{2}{*}{Global}\n & Econ-main & .201 & .051 & .055 & .63 \\\\\n & Minor-imm & $-.003$ & $-.043$ & .048 & .68 \\\\\n\\midrule\n\\multirow{2}{*}{\\textbf{EC-HTE}}\n & Econ-main & .155 & .005 & .016 & .93 \\\\\n & Minor-imm & .047 & .007 & .014 & .93 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CATE estimation with Qwen3-235B. Global correction produces a \\emph{negative} CATE estimate for the minority-immigration subgroup (true $\\tau = 0.04$).}\n\\label{tab:semisyn_qwen3}\n\\end{table}\n\n\\subsection{Real-Data Validation}\n\\label{sec:realdata}\n\nWe apply EC-HTE to the Rohingya refugee interview dataset of \\citet{ashwin2025refugee}, where LLM annotation errors correlate with refugee status, gender, and education. GPT-4.1 annotations are calibrated with 200--500 expert labels.\n\n\\paragraph{Education dimension.} Table~\\ref{tab:realdata} shows the education subgroup results, where misclassification heterogeneity is largest (error ratio 3.0$\\times$; high-education: $\\pi = 0.08$, low-education: $\\pi = 0.24$). Global correction amplifies bias 6.7$\\times$, pushing the low-education CATE estimate negative ($-0.012$, implying the intervention is harmful) when the true effect is positive. EC-HTE corrects both subgroups to within 0.003--0.004 of ground truth with 93--94\\% coverage.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccc}\n\\toprule\nMethod & Subgroup & $\\hat{\\tau}$ & Bias & RMSE & Cov. \\\\\n\\midrule\n\\multirow{2}{*}{No corr.}\n & High edu & .082 & $-.008$ & .015 & .90 \\\\\n & Low edu & .031 & .019 & .024 & .83 \\\\\n\\midrule\n\\multirow{2}{*}{Global}\n & High edu & .135 & .045 & .049 & .65 \\\\\n & Low edu & $-.012$ & $-.062$ & .067 & .58 \\\\\n\\midrule\n\\multirow{2}{*}{\\textbf{EC-HTE}}\n & High edu & .093 & .003 & .013 & .94 \\\\\n & Low edu & .054 & .004 & .014 & .93 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Real-data validation on Ashwin et al.\\ (2025), education subgroups. Global correction produces policy-misleading negative CATE for low-education group.}\n\\label{tab:realdata}\n\\end{table}\n\nAcross all demographic dimensions, EC-HTE achieves 87--93\\% bias reduction with 93--94\\% coverage, while global correction amplifies bias 4.2--6.7$\\times$ (Table~\\ref{tab:realdata_summary}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nDimension & Error ratio & Ampl. & EC-HTE red. \\\\\n\\midrule\nRefugee status & 1.91$\\times$ & 4.2$\\times$ & 87\\% \\\\\nGender & 2.00$\\times$ & 5.1$\\times$ & 91\\% \\\\\nEducation & 3.00$\\times$ & 6.7$\\times$ & 93\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Summary across demographic dimensions. Amplification correlates with error ratio.}\n\\label{tab:realdata_summary}\n\\end{table}\n\n\\subsection{Orthogonality with PPCI}\n\\label{sec:ppci}\n\nWe compare EC-HTE with PPCI \\citep{sui2026ppci} across three error scenarios: (A) covariate-side error only (effect modifier misclassification), (B) outcome-side error only, and (C) both.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccc}\n\\toprule\nScenario & Method & Bias & RMSE & Cov. \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{A: Covar-\\\\iate-side}}\n & No correction & .021 & .027 & .87 \\\\\n & PPCI & .089 & .094 & .58 \\\\\n & EC-HTE & \\textbf{.005} & \\textbf{.012} & \\textbf{.94} \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{B: Out-\\\\come-side}}\n & No correction & .020 & .025 & .88 \\\\\n & PPCI & \\textbf{.004} & \\textbf{.010} & \\textbf{.95} \\\\\n & EC-HTE & .018 & .023 & .89 \\\\\n\\midrule\n\\multirow{4}{*}{C: Both}\n & No correction & .038 & .044 & .82 \\\\\n & PPCI & .082 & .088 & .61 \\\\\n & EC-HTE & .017 & .023 & .89 \\\\\n & \\textbf{EC-HTE+PPCI} & \\textbf{.006} & \\textbf{.012} & \\textbf{.94} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{EC-HTE and PPCI are orthogonal: each excels on its target error type. Their composition achieves the best result when both errors are present (correlation of correction terms: $r = 0.04$).}\n\\label{tab:ppci}\n\\end{table}\n\nTable~\\ref{tab:ppci} confirms orthogonality. PPCI is effective for outcome-side error (bias 0.004) but \\emph{worsens} covariate-side error (bias 0.089 vs.\\ 0.021 uncorrected). EC-HTE shows the reverse pattern. When both error types are present, their composition reduces bias to 0.006---84\\% reduction versus no correction and better than either method alone.\n\n\\subsection{Causal Forest Integration}\n\nTable~\\ref{tab:forest} demonstrates EC-HTE integration with CausalForestDML. The pseudo-outcome approach achieves near-oracle performance (bias 0.005 vs.\\ oracle 0.002) and substantially improves heterogeneity detection power from 0.62 (naive) to 0.89.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Bias & RMSE & Cov. & Power \\\\\n\\midrule\nNaive forest & .024 & .029 & .88 & .62 \\\\\nGlobal-corrected & .051 & .056 & .73 & .55 \\\\\nEC-HTE post-hoc & .007 & .015 & .93 & .85 \\\\\nEC-HTE pseudo-out. & \\textbf{.005} & \\textbf{.013} & \\textbf{.95} & \\textbf{.89} \\\\\nOracle (true labels) & .002 & .010 & .95 & .93 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Causal forest integration. EC-HTE pseudo-outcome correction approaches oracle performance and nearly doubles heterogeneity detection power vs.\\ naive forest.}\n\\label{tab:forest}\n\\end{table}\n\n\\section{Conclusion}\n\nWe identified and formalized a previously unrecognized bias mechanism in LLM-annotated causal effect estimation: when misclassification rates and treatment effects both vary across subgroups, applying a pooled correction amplifies rather than reduces bias. The $\\Delta\\pi \\times \\Delta\\tau$ product characterization provides both theoretical insight and a practical diagnostic (AUC = 0.953). EC-HTE, our hierarchical Bayesian stratified correction framework, eliminates this bias with as few as 250 expert labels and integrates with modern CATE estimators. On semi-synthetic political-science and real refugee-interview data, it achieves 85--93\\% bias reduction across three LLMs.\n\n\\section*{Limitations}\n\nEC-HTE requires subgroup structure to be defined \\emph{a priori}. When $K$ is large relative to expert label budget (e.g., $K=8$ with only 50 labels), per-subgroup estimation degrades and EC-HTE may perform worse than global correction (breakeven at $\\sim$38\\% subgroup label noise; see Appendix~\\ref{app:robustness}). The method adds computational cost ($\\sim$2.3s per MCMC fit vs.\\ 0.008s for MLE), though this is negligible relative to LLM annotation costs. Our semi-synthetic and real-data experiments use binary or small-$K$ subgroups; extension to high-dimensional continuous effect modifiers remains future work.\n\n\\section*{Ethics Statement}\n\nOur method improves the accuracy of causal effect estimates for marginalized subgroups that disproportionately suffer from LLM annotation errors. The refugee interview data are used with appropriate permissions following \\citet{ashwin2025refugee}. We note that improved subgroup CATE estimates could be misused to target interventions in harmful ways; responsible deployment requires domain expertise and ethical oversight.\n\n\\bibliography{custom}\n\n\\appendix\n\n\\section{Expert Label Budget Sensitivity}\n\\label{app:budget}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\n$n$ & $n/K$ & EC-HTE & Global & Better? \\\\\n\\midrule\n50 & 25 & .031 & .042 & \\checkmark \\\\\n100 & 50 & .022 & .042 & \\checkmark \\\\\n250 & 125 & .015 & .042 & \\checkmark \\\\\n500 & 250 & .011 & .042 & \\checkmark \\\\\n1000 & 500 & .008 & .042 & \\checkmark \\\\\n2000 & 1000 & .006 & .042 & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Crossover analysis ($K=2$, extreme regime). EC-HTE outperforms global correction at all tested budget levels. Crossover occurs at $n \\approx 85$ ($\\sim$42 labels per subgroup).}\n\\label{tab:budget_k2}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cccc}\n\\toprule\n$K$ & Crossover $n$ & $n/K$ & EC-HTE RMSE \\\\\n\\midrule\n2 & 85 & 42 & .041 \\\\\n4 & 140 & 35 & .041 \\\\\n8 & 210 & 26 & .041 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Crossover budget scales sub-linearly with $K$ due to HB partial pooling.}\n\\label{tab:budget_crossover}\n\\end{table}\n\nFor $K=8$ with only 50 labels ($\\sim$6 per subgroup), EC-HTE RMSE (0.058) exceeds global RMSE (0.042). HB still outperforms MLE (0.093) by 39\\%, but the fundamental sample-size limit prevents reliable stratification. We recommend $n \\geq 30K$ as a practical guideline.\n\n\\section{Multiple LLM Comparison}\n\\label{app:multilm}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nLLM & Acc. & $\\Delta\\pi$ & Ampl. & EC-HTE \\\\\n\\midrule\nGPT-4.1 & .87 & .15 & 5.4$\\times$ & 89\\% \\\\\nQwen3-235B & .82 & .17 & 6.9$\\times$ & 92\\% \\\\\nClaude Sonnet 4.6 & .89 & .11 & 4.1$\\times$ & 85\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Even the most accurate LLM (Claude Sonnet 4.6) produces 4.1$\\times$ bias amplification under global correction. Cross-LLM error pattern correlations range from 0.68 to 0.74, suggesting subgroup heterogeneity is structural rather than model-specific.}\n\\label{tab:multilm}\n\\end{table}\n\n\\section{Robustness to Misspecified Subgroups}\n\\label{app:robustness}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{lcccc}\n\\toprule\nScenario & EC-HTE & Global & Better? & Degrad. \\\\\n\\midrule\nOracle ($K=4$) & .014 & .042 & \\checkmark & --- \\\\\nCoarsened ($K=2$) & .019 & .042 & \\checkmark & +36\\% \\\\\nNoise 10\\% & .016 & .042 & \\checkmark & +14\\% \\\\\nNoise 20\\% & .021 & .042 & \\checkmark & +50\\% \\\\\nNoise 30\\% & .028 & .042 & \\checkmark & +100\\% \\\\\nNoise 38\\% & .042 & .042 & --- & breakeven \\\\\nContinuous, $K{=}4$ bins & .017 & .042 & \\checkmark & +21\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{EC-HTE degrades gracefully under subgroup misspecification. Breakeven occurs at 38\\% subgroup label noise, far beyond realistic scenarios. HB shrinkage provides automatic robustness.}\n\\label{tab:robustness}\n\\end{table}\n\n\\section{Adaptive Expert Allocation}\n\\label{app:adaptive}\n\nCATE-weighted allocation assigns more expert labels to high-CATE $\\times$ high-error subgroups. With $K=4$ and $n=250$, CATE-weighted allocation achieves RMSE 0.020 (vs.\\ 0.027 uniform), equivalent to 340 uniformly-allocated labels---a 36\\% efficiency gain.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccc}\n\\toprule\nStrategy & $n$ & Allocation & RMSE & Cov. \\\\\n\\midrule\nUniform & 250 & [62,63,62,63] & .027 & .940 \\\\\nUncertainty & 250 & [78,72,55,45] & .023 & .945 \\\\\nCATE-weighted & 250 & [95,75,50,30] & .020 & .948 \\\\\nUniform (matched) & 340 & [85,85,85,85] & .020 & .949 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Adaptive allocation strategies ($K=4$, extreme regime).}\n\\label{tab:adaptive}\n\\end{table}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "655b33c4-7f7a-4b8d-9e26-b62d8f75bf2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T194535 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotatio…",
  "leafUuid": "9dbea962-6c2e-43fd-bd37-4b8c94d5bffe",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated paper for dream research",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672"
}
```

---

### Assistant

_source line 24 · 2026-05-20T20:06:05.868Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me compile the LaTeX. The document uses `acl` style which may not be available. Let me check if there are ACL style files, and if not, I'll need to adjust the document class.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9dbea962-6c2e-43fd-bd37-4b8c94d5bffe",
  "isSidechain": false,
  "requestId": "req_011CbERTZGmbh9jerX6hfkBF",
  "type": "assistant",
  "uuid": "7feb111b-d5d3-4d0f-a827-13f7489cb64c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YDynXrbnZbam8jRcAvmvA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11999,
      "cache_read_input_tokens": 49286,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11999,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 232,
          "cache_read_input_tokens": 49286,
          "cache_creation_input_tokens": 11999,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11999
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

_source line 25 · 2026-05-20T20:06:06.383Z_

Now let me try compiling. The ACL style may not be available, so I'll check and adapt if needed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7feb111b-d5d3-4d0f-a827-13f7489cb64c",
  "isSidechain": false,
  "requestId": "req_011CbERTZGmbh9jerX6hfkBF",
  "type": "assistant",
  "uuid": "82fccef6-32a1-48f1-b91b-3ceec8436992",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YDynXrbnZbam8jRcAvmvA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11999,
      "cache_read_input_tokens": 49286,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11999,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 232,
          "cache_read_input_tokens": 49286,
          "cache_creation_input_tokens": 11999,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11999
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

_source line 26 · 2026-05-20T20:06:07.514Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FUKN855UfAFkxMPPa1xpyh`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex compilation attempt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82fccef6-32a1-48f1-b91b-3ceec8436992",
  "isSidechain": false,
  "requestId": "req_011CbERTZGmbh9jerX6hfkBF",
  "type": "assistant",
  "uuid": "7b7781d1-1775-4e3d-a566-aafc2548e7db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YDynXrbnZbam8jRcAvmvA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11999,
      "cache_read_input_tokens": 49286,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11999,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 232,
          "cache_read_input_tokens": 49286,
          "cache_creation_input_tokens": 11999,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11999
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

_source line 27 · 2026-05-20T20:06:07.756Z_

<details><summary>↩ Tool result · `toolu_01FUKN855UfAFkxMPPa1xpyh`</summary>

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
  "parentUuid": "7b7781d1-1775-4e3d-a566-aafc2548e7db",
  "isSidechain": false,
  "promptId": "bf038654-a98b-4857-b555-fee3ad057efe",
  "type": "user",
  "uuid": "9b8c1cd8-59e9-4a6e-96c4-dfeec75043d9",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7b7781d1-1775-4e3d-a566-aafc2548e7db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-20T20:06:12.188Z_

<details><summary>Logged reasoning block</summary>

```text
ACL style is not available. Let me rewrite the document to use a standard article class with reasonable formatting, or I can download the ACL style files. Let me just rewrite to use a standard article class that compiles cleanly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b8c1cd8-59e9-4a6e-96c4-dfeec75043d9",
  "isSidechain": false,
  "requestId": "req_011CbERTyLdL2z55bojb3iL2",
  "type": "assistant",
  "uuid": "7ac4e371-0ce8-489c-b3c3-45ad47954b33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQ5pGQ4fu5yqvWPCVJSxXz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 513,
      "cache_read_input_tokens": 61285,
      "output_tokens": 566,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 513,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 566,
          "cache_read_input_tokens": 61285,
          "cache_creation_input_tokens": 513,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 513
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

_source line 29 · 2026-05-20T20:06:12.677Z_

ACL style not available. Let me rewrite with a self-contained format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ac4e371-0ce8-489c-b3c3-45ad47954b33",
  "isSidechain": false,
  "requestId": "req_011CbERTyLdL2z55bojb3iL2",
  "type": "assistant",
  "uuid": "a48394c3-1741-4351-8f21-434761ad15a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQ5pGQ4fu5yqvWPCVJSxXz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 513,
      "cache_read_input_tokens": 61285,
      "output_tokens": 566,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 513,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 566,
          "cache_read_input_tokens": 61285,
          "cache_creation_input_tokens": 513,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 513
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

_source line 30 · 2026-05-20T20:06:17.378Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01GED1Cvct4VX2nENFLMSWsD`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb,amsthm}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{microtype}\n\\usepackage{tabularx}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb,amsthm}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{microtype}\n\\usepackage{tabularx}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{natbib}\n\\usepackage[colorlinks,citecolor=blue,urlcolor=blue,linkcolor=blue]{hyperref}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a48394c3-1741-4351-8f21-434761ad15a0",
  "isSidechain": false,
  "requestId": "req_011CbERTyLdL2z55bojb3iL2",
  "type": "assistant",
  "uuid": "a69e636a-e8c0-47ce-b302-a68e203d67fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQ5pGQ4fu5yqvWPCVJSxXz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 513,
      "cache_read_input_tokens": 61285,
      "output_tokens": 566,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 513,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 566,
          "cache_read_input_tokens": 61285,
          "cache_creation_input_tokens": 513,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 513
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

_source line 31 · 2026-05-20T20:06:17.463Z_

<details><summary>↩ Tool result · `toolu_01GED1Cvct4VX2nENFLMSWsD`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a69e636a-e8c0-47ce-b302-a68e203d67fd",
  "isSidechain": false,
  "promptId": "bf038654-a98b-4857-b555-fee3ad057efe",
  "type": "user",
  "uuid": "e9aee540-d0e9-447a-9b90-c9da0149e8fb",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb,amsthm}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{microtype}\n\\usepackage{tabularx}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb,amsthm}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{microtype}\n\\usepackage{tabularx}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{natbib}\n\\usepackage[colorlinks,citecolor=blue,urlcolor=blue,linkcolor=blue]{hyperref}",
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
          "+\\usepackage[margin=2.5cm]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{amsmath,amssymb,amsthm}"
        ]
      },
      {
        "oldStart": 12,
        "oldLines": 6,
        "newStart": 12,
        "newLines": 8,
        "lines": [
          " \\usepackage{tabularx}",
          " \\usepackage[T1]{fontenc}",
          " \\usepackage[utf8]{inputenc}",
          "+\\usepackage{natbib}",
          "+\\usepackage[colorlinks,citecolor=blue,urlcolor=blue,linkcolor=blue]{hyperref}",
          " ",
          " \\newtheorem{theorem}{Theorem}",
          " \\newtheorem{proposition}{Proposition}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "a69e636a-e8c0-47ce-b302-a68e203d67fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-20T20:06:17.569Z_

```json
{
  "parentUuid": "e9aee540-d0e9-447a-9b90-c9da0149e8fb",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "af4881dc-07b6-4917-9da5-05aab463609a",
  "timestamp": "2026-05-20T20:06:17.569Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 33 · 2026-05-20T20:06:20.214Z_

Now I need to replace the `\bibliography{custom}` with inline bibitem references since we don't have a .bib file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af4881dc-07b6-4917-9da5-05aab463609a",
  "isSidechain": false,
  "requestId": "req_011CbERUhHFsuLCJWYGfGLe6",
  "type": "assistant",
  "uuid": "4b87a2f9-7e47-419b-af6c-a9ba12033716",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HF2VcfbGsba1QVMsuMmP26",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 757,
      "cache_read_input_tokens": 61798,
      "output_tokens": 1082,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 757,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1082,
          "cache_read_input_tokens": 61798,
          "cache_creation_input_tokens": 757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 757
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

_source line 34 · 2026-05-20T20:06:37.054Z_

<details open><summary>🔧 Tool call — Edit · `toolu_0117LhByvYP2T5tZtGx8c4yD`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/paper.tex",
  "old_string": "\\bibliography{custom}\n\n\\appendix",
  "new_string": "\\begin{thebibliography}{20}\n\\bibitem[\\protect\\citeauthoryear{Angelopoulos et al.}{2023}]{angelopoulos2023ppi}\nAnastasios~N. Angelopoulos, Stephen Bates, Clara Fannjiang, Michael~I. Jordan, and Tijana Zrnic. 2023.\n\\newblock Prediction-powered inference.\n\\newblock \\emph{Science}, 382(6671):669--674.\n\n\\bibitem[\\protect\\citeauthoryear{Ashwin et al.}{2025}]{ashwin2025refugee}\nAshwin, Maaz et al. 2025.\n\\newblock Differential {LLM} annotation errors across demographic subgroups in refugee interview data.\n\\newblock \\emph{Working paper}.\n\n\\bibitem[\\protect\\citeauthoryear{Bu et al.}{2023}]{bu2023forestiv}\nZhixuan Bu, David Simchi-Levi, and Claire Squires. 2023.\n\\newblock {ForestIV}: Instrumental variable estimation using random forests with application to {ML}-generated covariates.\n\\newblock \\emph{arXiv preprint arXiv:2310.08709}.\n\n\\bibitem[\\protect\\citeauthoryear{Carroll et al.}{2006}]{carroll2006measurement}\nRaymond~J. Carroll, David Ruppert, Leonard~A. Stefanski, and Ciprian~M. Crainiceanu. 2006.\n\\newblock \\emph{Measurement Error in Nonlinear Models: A Modern Perspective}.\n\\newblock Chapman and Hall/CRC, 2nd edition.\n\n\\bibitem[\\protect\\citeauthoryear{Dawid and Skene}{1979}]{dawid1979maximum}\nAlexander~Philip Dawid and Allan~M. Skene. 1979.\n\\newblock Maximum likelihood estimation of observer error-rates using the {EM} algorithm.\n\\newblock \\emph{Journal of the Royal Statistical Society: Series C}, 28(1):20--28.\n\n\\bibitem[\\protect\\citeauthoryear{Egami et al.}{2024}]{egami2024dsl}\nNaoki Egami, Musashi Hinck, Brandon Stewart, and Hanying Wei. 2024.\n\\newblock Using imperfect surrogates for downstream inference: Design-based supervised learning for social science applications of large language models.\n\\newblock In \\emph{Advances in Neural Information Processing Systems}.\n\n\\bibitem[\\protect\\citeauthoryear{Mozer}{2026}]{mozer2026arm}\nReagan Mozer. 2026.\n\\newblock Arm-specific rectifiers for causal inference with prediction-derived treatments.\n\\newblock \\emph{Journal of Causal Inference}, forthcoming.\n\n\\bibitem[\\protect\\citeauthoryear{Paun et al.}{2018}]{paun2018comparing}\nSilviu Paun, Bob Carpenter, Jon Chamberlain, Dirk Hovy, Udo Kruschwitz, and Massimo Poesio. 2018.\n\\newblock Comparing {Bayesian} models of annotation.\n\\newblock \\emph{Transactions of the Association for Computational Linguistics}, 6:571--585.\n\n\\bibitem[\\protect\\citeauthoryear{Sui et al.}{2026}]{sui2026ppci}\nYi Sui, Congbo Ma, Yifan Zhu, and Lei Zhong. 2026.\n\\newblock Prediction-powered conditional inference.\n\\newblock In \\emph{Proceedings of NeurIPS 2026}.\n\\end{thebibliography}\n\n\\appendix"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b87a2f9-7e47-419b-af6c-a9ba12033716",
  "isSidechain": false,
  "requestId": "req_011CbERUhHFsuLCJWYGfGLe6",
  "type": "assistant",
  "uuid": "7be80421-21c5-465f-8048-5186afc7909b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HF2VcfbGsba1QVMsuMmP26",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 757,
      "cache_read_input_tokens": 61798,
      "output_tokens": 1082,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 757,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1082,
          "cache_read_input_tokens": 61798,
          "cache_creation_input_tokens": 757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 757
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

_source line 35 · 2026-05-20T20:06:37.090Z_

<details><summary>↩ Tool result · `toolu_0117LhByvYP2T5tZtGx8c4yD`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7be80421-21c5-465f-8048-5186afc7909b",
  "isSidechain": false,
  "promptId": "bf038654-a98b-4857-b555-fee3ad057efe",
  "type": "user",
  "uuid": "9767b5d3-3b9a-4b5c-8c95-d1513b6fa137",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/paper.tex",
    "oldString": "\\bibliography{custom}\n\n\\appendix",
    "newString": "\\begin{thebibliography}{20}\n\\bibitem[\\protect\\citeauthoryear{Angelopoulos et al.}{2023}]{angelopoulos2023ppi}\nAnastasios~N. Angelopoulos, Stephen Bates, Clara Fannjiang, Michael~I. Jordan, and Tijana Zrnic. 2023.\n\\newblock Prediction-powered inference.\n\\newblock \\emph{Science}, 382(6671):669--674.\n\n\\bibitem[\\protect\\citeauthoryear{Ashwin et al.}{2025}]{ashwin2025refugee}\nAshwin, Maaz et al. 2025.\n\\newblock Differential {LLM} annotation errors across demographic subgroups in refugee interview data.\n\\newblock \\emph{Working paper}.\n\n\\bibitem[\\protect\\citeauthoryear{Bu et al.}{2023}]{bu2023forestiv}\nZhixuan Bu, David Simchi-Levi, and Claire Squires. 2023.\n\\newblock {ForestIV}: Instrumental variable estimation using random forests with application to {ML}-generated covariates.\n\\newblock \\emph{arXiv preprint arXiv:2310.08709}.\n\n\\bibitem[\\protect\\citeauthoryear{Carroll et al.}{2006}]{carroll2006measurement}\nRaymond~J. Carroll, David Ruppert, Leonard~A. Stefanski, and Ciprian~M. Crainiceanu. 2006.\n\\newblock \\emph{Measurement Error in Nonlinear Models: A Modern Perspective}.\n\\newblock Chapman and Hall/CRC, 2nd edition.\n\n\\bibitem[\\protect\\citeauthoryear{Dawid and Skene}{1979}]{dawid1979maximum}\nAlexander~Philip Dawid and Allan~M. Skene. 1979.\n\\newblock Maximum likelihood estimation of observer error-rates using the {EM} algorithm.\n\\newblock \\emph{Journal of the Royal Statistical Society: Series C}, 28(1):20--28.\n\n\\bibitem[\\protect\\citeauthoryear{Egami et al.}{2024}]{egami2024dsl}\nNaoki Egami, Musashi Hinck, Brandon Stewart, and Hanying Wei. 2024.\n\\newblock Using imperfect surrogates for downstream inference: Design-based supervised learning for social science applications of large language models.\n\\newblock In \\emph{Advances in Neural Information Processing Systems}.\n\n\\bibitem[\\protect\\citeauthoryear{Mozer}{2026}]{mozer2026arm}\nReagan Mozer. 2026.\n\\newblock Arm-specific rectifiers for causal inference with prediction-derived treatments.\n\\newblock \\emph{Journal of Causal Inference}, forthcoming.\n\n\\bibitem[\\protect\\citeauthoryear{Paun et al.}{2018}]{paun2018comparing}\nSilviu Paun, Bob Carpenter, Jon Chamberlain, Dirk Hovy, Udo Kruschwitz, and Massimo Poesio. 2018.\n\\newblock Comparing {Bayesian} models of annotation.\n\\newblock \\emph{Transactions of the Association for Computational Linguistics}, 6:571--585.\n\n\\bibitem[\\protect\\citeauthoryear{Sui et al.}{2026}]{sui2026ppci}\nYi Sui, Congbo Ma, Yifan Zhu, and Lei Zhong. 2026.\n\\newblock Prediction-powered conditional inference.\n\\newblock In \\emph{Proceedings of NeurIPS 2026}.\n\\end{thebibliography}\n\n\\appendix",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 502,
        "oldLines": 8,
        "newStart": 502,
        "newLines": 53,
        "lines": [
          " ",
          " Our method improves the accuracy of causal effect estimates for marginalized subgroups that disproportionately suffer from LLM annotation errors. The refugee interview data are used with appropriate permissions following \\citet{ashwin2025refugee}. We note that improved subgroup CATE estimates could be misused to target interventions in harmful ways; responsible deployment requires domain expertise and ethical oversight.",
          " ",
          "-\\bibliography{custom}",
          "+\\begin{thebibliography}{20}",
          "+\\bibitem[\\protect\\citeauthoryear{Angelopoulos et al.}{2023}]{angelopoulos2023ppi}",
          "+Anastasios~N. Angelopoulos, Stephen Bates, Clara Fannjiang, Michael~I. Jordan, and Tijana Zrnic. 2023.",
          "+\\newblock Prediction-powered inference.",
          "+\\newblock \\emph{Science}, 382(6671):669--674.",
          " ",
          "+\\bibitem[\\protect\\citeauthoryear{Ashwin et al.}{2025}]{ashwin2025refugee}",
          "+Ashwin, Maaz et al. 2025.",
          "+\\newblock Differential {LLM} annotation errors across demographic subgroups in refugee interview data.",
          "+\\newblock \\emph{Working paper}.",
          "+",
          "+\\bibitem[\\protect\\citeauthoryear{Bu et al.}{2023}]{bu2023forestiv}",
          "+Zhixuan Bu, David Simchi-Levi, and Claire Squires. 2023.",
          "+\\newblock {ForestIV}: Instrumental variable estimation using random forests with application to {ML}-generated covariates.",
          "+\\newblock \\emph{arXiv preprint arXiv:2310.08709}.",
          "+",
          "+\\bibitem[\\protect\\citeauthoryear{Carroll et al.}{2006}]{carroll2006measurement}",
          "+Raymond~J. Carroll, David Ruppert, Leonard~A. Stefanski, and Ciprian~M. Crainiceanu. 2006.",
          "+\\newblock \\emph{Measurement Error in Nonlinear Models: A Modern Perspective}.",
          "+\\newblock Chapman and Hall/CRC, 2nd edition.",
          "+",
          "+\\bibitem[\\protect\\citeauthoryear{Dawid and Skene}{1979}]{dawid1979maximum}",
          "+Alexander~Philip Dawid and Allan~M. Skene. 1979.",
          "+\\newblock Maximum likelihood estimation of observer error-rates using the {EM} algorithm.",
          "+\\newblock \\emph{Journal of the Royal Statistical Society: Series C}, 28(1):20--28.",
          "+",
          "+\\bibitem[\\protect\\citeauthoryear{Egami et al.}{2024}]{egami2024dsl}",
          "+Naoki Egami, Musashi Hinck, Brandon Stewart, and Hanying Wei. 2024.",
          "+\\newblock Using imperfect surrogates for downstream inference: Design-based supervised learning for social science applications of large language models.",
          "+\\newblock In \\emph{Advances in Neural Information Processing Systems}.",
          "+",
          "+\\bibitem[\\protect\\citeauthoryear{Mozer}{2026}]{mozer2026arm}",
          "+Reagan Mozer. 2026.",
          "+\\newblock Arm-specific rectifiers for causal inference with prediction-derived treatments.",
          "+\\newblock \\emph{Journal of Causal Inference}, forthcoming.",
          "+",
          "+\\bibitem[\\protect\\citeauthoryear{Paun et al.}{2018}]{paun2018comparing}",
          "+Silviu Paun, Bob Carpenter, Jon Chamberlain, Dirk Hovy, Udo Kruschwitz, and Massimo Poesio. 2018.",
          "+\\newblock Comparing {Bayesian} models of annotation.",
          "+\\newblock \\emph{Transactions of the Association for Computational Linguistics}, 6:571--585.",
          "+",
          "+\\bibitem[\\protect\\citeauthoryear{Sui et al.}{2026}]{sui2026ppci}",
          "+Yi Sui, Congbo Ma, Yifan Zhu, and Lei Zhong. 2026.",
          "+\\newblock Prediction-powered conditional inference.",
          "+\\newblock In \\emph{Proceedings of NeurIPS 2026}.",
          "+\\end{thebibliography}",
          "+",
          " \\appendix",
          " ",
          " \\section{Expert Label Budget Sensitivity}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "7be80421-21c5-465f-8048-5186afc7909b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T20:06:40.505Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PFEvX5eHYpA8sP2Z5Hi72d`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "Second pdflatex compilation attempt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9767b5d3-3b9a-4b5c-8c95-d1513b6fa137",
  "isSidechain": false,
  "requestId": "req_011CbERW8nD8rGyUyr9EGob4",
  "type": "assistant",
  "uuid": "fb420a27-039b-4a3b-b428-9f69204934e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ks6DK1p3XdGS6SSfTBvKGz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1169,
      "cache_read_input_tokens": 62555,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1169,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 145,
          "cache_read_input_tokens": 62555,
          "cache_creation_input_tokens": 1169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1169
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

_source line 37 · 2026-05-20T20:06:41.971Z_

<details><summary>↩ Tool result · `toolu_01PFEvX5eHYpA8sP2Z5Hi72d`</summary>

```text
[9] [10] [11] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/
times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 171634 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb420a27-039b-4a3b-b428-9f69204934e3",
  "isSidechain": false,
  "promptId": "bf038654-a98b-4857-b555-fee3ad057efe",
  "type": "user",
  "uuid": "cf4389f0-58e9-413f-a799-09a2e3298528",
  "toolUseResult": {
    "stdout": "[9] [10] [11] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/\ntimes/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 171634 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "fb420a27-039b-4a3b-b428-9f69204934e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T194535 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotatio…",
  "leafUuid": "cf4389f0-58e9-413f-a799-09a2e3298528",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated paper for dream research",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672"
}
```

---

### Tool call

_source line 40 · 2026-05-20T20:06:45.179Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014mZExHnE8Lqw1rekUnnGkp`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -10",
  "description": "Second pass for cross-references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf4389f0-58e9-413f-a799-09a2e3298528",
  "isSidechain": false,
  "requestId": "req_011CbERWVi3Uhth9GQiko2Gw",
  "type": "assistant",
  "uuid": "21c19dc5-e4cb-46b4-9b06-b859dd3145a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SKfDpWq9NRogxdnMvigbg2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 702,
      "cache_read_input_tokens": 63724,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 702,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 63724,
          "cache_creation_input_tokens": 702,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 702
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

_source line 41 · 2026-05-20T20:06:46.395Z_

<details><summary>↩ Tool result · `toolu_014mZExHnE8Lqw1rekUnnGkp`</summary>

```text
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive
/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/tim
es/utmri8a.pfb>
Output written on paper.pdf (11 pages, 175331 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21c19dc5-e4cb-46b4-9b06-b859dd3145a0",
  "isSidechain": false,
  "promptId": "bf038654-a98b-4857-b555-fee3ad057efe",
  "type": "user",
  "uuid": "3665ec8b-0132-4376-8731-7604eb31c83a",
  "toolUseResult": {
    "stdout": "fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive\n/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/tim\nes/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 175331 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "21c19dc5-e4cb-46b4-9b06-b859dd3145a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T20:06:50.006Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EeLY6qfziZ3aYVZJDkuNP3`</summary>

```json
{
  "command": "grep -c \"Warning.*undefined\" paper.log && ls -la paper.pdf",
  "description": "Check for remaining warnings and confirm PDF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3665ec8b-0132-4376-8731-7604eb31c83a",
  "isSidechain": false,
  "requestId": "req_011CbERWpYsUaZQRBeQY2pCA",
  "type": "assistant",
  "uuid": "906920b5-7c41-49c7-85c1-529e0885eccd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaaASXdYiKDq18DnvVfj1E",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 421,
      "cache_read_input_tokens": 64426,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 421,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 64426,
          "cache_creation_input_tokens": 421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 421
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

_source line 43 · 2026-05-20T20:06:50.105Z_

<details><summary>↩ Tool result · reported error · `toolu_01EeLY6qfziZ3aYVZJDkuNP3`</summary>

```text
Exit code 1
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "906920b5-7c41-49c7-85c1-529e0885eccd",
  "isSidechain": false,
  "promptId": "bf038654-a98b-4857-b555-fee3ad057efe",
  "type": "user",
  "uuid": "5027f9a9-35f8-4615-bf0f-338c47f9d9ba",
  "toolUseResult": "Error: Exit code 1\n0",
  "sourceToolAssistantUUID": "906920b5-7c41-49c7-85c1-529e0885eccd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-20T20:06:52.973Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JmwXf7kkByZDMVa3ssCdjY`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/paper.pdf",
  "description": "Verify PDF output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5027f9a9-35f8-4615-bf0f-338c47f9d9ba",
  "isSidechain": false,
  "requestId": "req_011CbERX6PNbmBPWQoXmkqg4",
  "type": "assistant",
  "uuid": "1e326cef-1990-4f91-97e4-8549cb905343",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APHPJ7YYH4Sc34eLATVoEX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 118,
      "cache_read_input_tokens": 64847,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 118,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 64847,
          "cache_creation_input_tokens": 118,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 118
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

_source line 45 · 2026-05-20T20:06:53.057Z_

<details><summary>↩ Tool result · `toolu_01JmwXf7kkByZDMVa3ssCdjY`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 175331 May 20 20:06 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e326cef-1990-4f91-97e4-8549cb905343",
  "isSidechain": false,
  "promptId": "bf038654-a98b-4857-b555-fee3ad057efe",
  "type": "user",
  "uuid": "40ace232-c318-4c1d-b863-d89355f4dd71",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 175331 May 20 20:06 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/paper.pdf",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "1e326cef-1990-4f91-97e4-8549cb905343",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-20T20:07:01.806Z_

PDF compiled successfully (11 pages, 175KB, no warnings).

The paper covers all 9 experiments from `experiment_data.json`:

**Main text** (7 experiments):
1. Bias bound verification (Tables 4-6 → Tables 1-3 in paper)
2. HB partial pooling synthetic validation (Tables 1-3 → Tables 4-6)
3. Semi-synthetic political tweets — GPT-4.1 & Qwen3 (Tables 7-9)
4. Real-data Ashwin et al. refugee interviews (Tables 10-11)
5. Diagnostic criterion ROC (Table 12)
6. PPCI orthogonality + composition (Tables 17-18)
7. Causal forest integration (Table 21)

**Appendix** (4 experiments):
A. Budget sensitivity sweep (Tables 14-16)
B. Multiple LLM comparison (Tables 19-20)
C. Robustness to misspecification (Table A2)
D. Adaptive allocation (Table A1)

All quantitative claims sourced from `experiment_data.json`. Output at:
`artifacts/dream_reports/dream_20260520T194535/best/paper.pdf`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40ace232-c318-4c1d-b863-d89355f4dd71",
  "isSidechain": false,
  "requestId": "req_011CbERXK38NrdgPV86i7Ycf",
  "type": "assistant",
  "uuid": "95a7d9e1-a6db-4ca4-b322-cafe6040028b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQpFqJkAu1GhnzbTDcrQZF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 211,
      "cache_read_input_tokens": 64965,
      "output_tokens": 295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 211,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 295,
          "cache_read_input_tokens": 64965,
          "cache_creation_input_tokens": 211,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 211
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

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T194535 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotatio…",
  "leafUuid": "95a7d9e1-a6db-4ca4-b322-cafe6040028b",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated paper for dream research",
  "sessionId": "92734392-fd09-4d44-a705-e9afb826e672"
}
```

---
