# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T173833 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/fafed79b-b5e7-4590-860f-cf22319c4462.jsonl`
- **Structured JSON:** [`6faf35074e41af27c639.json`](../../sessions/6f/6faf35074e41af27c639.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T18:26:47.759Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T18:26:47.759Z",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T173833 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/worst/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：放弃 \"Diversity Trap\" framing。Reframe 为 \"Structural Vulnerability Anatomy of Multi-Judge LLM Evaluation\"。 新 lead claim：η_max 作为 panel vulnerability 的 dominant 且 near-sufficient predictor（9-11/12 显著）， 这本身是对 \"diversity protects\" 假设的实证否定——不需要 diversity actively hurts，只需 diversity doesn't help 而 weakest-link 决定一切。K_eff 降级为 \"exploratory analysis showing suggestive but confounded association\"， 置于 Discussion。方法论贡献前移：copula failure（即使 ratio 降了仍是有意义的 methodological finding）、 family label 不可靠性、15-model/455-panel 规模的 evaluation benchmark 本身作为 resource contribution。 BFT 从 core mechanism 降为 Discussion section 的 \"open question\"。 补偿策略：(a) 强调 weakest-link 发现的实用价值（panel 安全由最弱 judge 决定）； (b) 释放 per-judge ASR 浓度分析（plan_006 Gini/entropy）作为 adaptive adversary targeting 的直接证据； (c) 推 aggregation rule 比较作为 practical contribution（哪种聚合最抗攻击）。 预期结果：需要 rebuttal 期大幅补充，borderline reject / weak accept。仍冲 EMNLP 但准备 NAACL 2027 backup。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-22T18:26:47.762Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T18:26:47.762Z",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462"
}
```

---

## Round 1

26 recorded events

### User

_source line 3 · 2026-05-22T18:26:47.781Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T173833 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/worst/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：放弃 "Diversity Trap" framing。Reframe 为 "Structural Vulnerability Anatomy of Multi-Judge LLM Evaluation"。 新 lead claim：η_max 作为 panel vulnerability 的 dominant 且 near-sufficient predictor（9-11/12 显著）， 这本身是对 "diversity protects" 假设的实证否定——不需要 diversity actively hurts，只需 diversity doesn't help 而 weakest-link 决定一切。K_eff 降级为 "exploratory analysis showing suggestive but confounded association"， 置于 Discussion。方法论贡献前移：copula failure（即使 ratio 降了仍是有意义的 methodological finding）、 family label 不可靠性、15-model/455-panel 规模的 evaluation benchmark 本身作为 resource contribution。 BFT 从 core mechanism 降为 Discussion section 的 "open question"。 补偿策略：(a) 强调 weakest-link 发现的实用价值（panel 安全由最弱 judge 决定）； (b) 释放 per-judge ASR 浓度分析（plan_006 Gini/entropy）作为 adaptive adversary targeting 的直接证据； (c) 推 aggregation rule 比较作为 practical contribution（哪种聚合最抗攻击）。 预期结果：需要 rebuttal 期大幅补充，borderline reject / weak accept。仍冲 EMNLP 但准备 NAACL 2027 backup。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a4e49dfa-ac88-470f-90c8-78060d831735",
  "type": "user",
  "uuid": "a3740bc4-2678-423a-bb0a-d35a2967da00",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T18:26:47.780Z_

```json
{
  "parentUuid": "a3740bc4-2678-423a-bb0a-d35a2967da00",
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
  "uuid": "cfec7e50-c2ae-416c-816a-03e675fe43e3",
  "timestamp": "2026-05-22T18:26:47.780Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T18:26:47.780Z_

```json
{
  "parentUuid": "cfec7e50-c2ae-416c-816a-03e675fe43e3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "01bdcd37-e128-458d-8f7b-54386f3de2bb",
  "timestamp": "2026-05-22T18:26:47.780Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462",
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
  "aiTitle": "Generate worst-tier mock paper for dream evaluation",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462"
}
```

---

### Assistant

_source line 7 · 2026-05-22T18:26:50.431Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01bdcd37-e128-458d-8f7b-54386f3de2bb",
  "isSidechain": false,
  "requestId": "req_011CbJ5WUChTLvy2nv8YRobd",
  "type": "assistant",
  "uuid": "e0b14ef8-0ee7-44fb-96fe-67b6dfc56399",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LNku6FK6tcLhiTcX4ou7QQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12054,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12054,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12054,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12054
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

_source line 8 · 2026-05-22T18:26:51.597Z_

<details open><summary>🔧 Tool call — Read · `toolu_0176Gu6Lu2Txq5a4TmQwqxej`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0b14ef8-0ee7-44fb-96fe-67b6dfc56399",
  "isSidechain": false,
  "requestId": "req_011CbJ5WUChTLvy2nv8YRobd",
  "type": "assistant",
  "uuid": "246d8382-02ca-4b90-9855-2b3cdd2199a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LNku6FK6tcLhiTcX4ou7QQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12054,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12054,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12054,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12054
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

_source line 9 · 2026-05-22T18:26:51.884Z_

<details><summary>↩ Tool result · `toolu_0176Gu6Lu2Txq5a4TmQwqxej`</summary>

```text
1	[
2	  {
3	    "name": "15-Model Scale Expansion",
4	    "description": "扩展至 15 个模型（6 open-source + 4 API + 大型开源 70B/72B），重跑 MI matrix 和 全 panel（C(15,3)=455）回归分析。12 conditions（2 datasets × 6 attacks）。\n",
5	    "results": {
6	      "n_models": 15,
7	      "n_panels": 455,
8	      "n_conditions": 12,
9	      "keff_raw_sig_positive": 7,
10	      "keff_raw_sig_negative": 0,
11	      "keff_raw_nonsig": 5,
12	      "keff_resid_sig_positive": 4,
13	      "keff_resid_nonsig": 8,
14	      "eta_max_sig": 9,
15	      "mean_R2_full_model": 0.38,
16	      "mean_R2_eta_max_only": 0.34,
17	      "delta_R2_keff_contribution": 0.04,
18	      "keff_eta_max_correlation_mean": 0.73,
19	      "keff_eta_max_correlation_range": [
20	        0.62,
21	        0.85
22	      ],
23	      "VIF_keff": 2.14,
24	      "confound_free_conditions_count": 1,
25	      "confound_free_condition_keff_p": 0.032,
26	      "confound_free_condition_keff_beta": 0.41
27	    },
28	    "tables": [
29	      {
30	        "title": "Table 1: K_eff Residualized Regression — 15 Models, 455 Panels",
31	        "columns": [
32	          "Dataset",
33	          "Attack",
34	          "β_ηmax",
35	          "p_ηmax",
36	          "β_Keff_resid",
37	          "p_Keff_resid",
38	          "R²",
39	          "K_eff-ηmax r"
40	        ],
41	        "rows": [
42	          [
43	            "MMLU",
44	            "sycophancy",
45	            "0.82",
46	            "<0.001",
47	            "0.18",
48	            "0.147",
49	            "0.41",
50	            "0.78"
51	          ],
52	          [
53	            "MMLU",
54	            "score_manip",
55	            "0.55",
56	            "<0.001",
57	            "0.39",
58	            "0.021",
59	            "0.36",
60	            "0.68"
61	          ],
62	          [
63	            "MMLU",
64	            "position",
65	            "0.71",
66	            "<0.001",
67	            "0.24",
68	            "0.089",
69	            "0.39",
70	            "0.75"
71	          ],
72	          [
73	            "MMLU",
74	            "verbosity",
75	            "0.88",
76	            "<0.001",
77	            "0.09",
78	            "0.511",
79	            "0.42",
80	            "0.81"
81	          ],
82	          [
83	            "MMLU",
84	            "authority",
85	            "0.79",
86	            "<0.001",
87	            "0.15",
88	            "0.218",
89	            "0.37",
90	            "0.76"
91	          ],
92	          [
93	            "MMLU",
94	            "few_shot_hijack",
95	            "0.64",
96	            "0.002",
97	            "0.31",
98	            "0.043",
99	            "0.33",
100	            "0.70"
101	          ],
102	          [
103	            "ARC",
104	            "sycophancy",
105	            "0.85",
106	            "<0.001",
107	            "0.12",
108	            "0.341",
109	            "0.43",
110	            "0.79"
111	          ],
112	          [
113	            "ARC",
114	            "score_manip",
115	            "0.48",
116	            "0.003",
117	            "0.41",
118	            "0.032",
119	            "0.35",
120	            "0.35"
121	          ],
122	          [
123	            "ARC",
124	            "position",
125	            "0.73",
126	            "<0.001",
127	            "0.22",
128	            "0.102",
129	            "0.38",
130	            "0.74"
131	          ],
132	          [
133	            "ARC",
134	            "verbosity",
135	            "0.91",
136	            "<0.001",
137	            "0.06",
138	            "0.649",
139	            "0.44",
140	            "0.82"
141	          ],
142	          [
143	            "ARC",
144	            "authority",
145	            "0.76",
146	            "<0.001",
147	            "0.19",
148	            "0.157",
149	            "0.36",
150	            "0.77"
151	          ],
152	          [
153	            "ARC",
154	            "few_shot_hijack",
155	            "0.59",
156	            "0.004",
157	            "0.28",
158	            "0.071",
159	            "0.32",
160	            "0.72"
161	          ]
162	        ]
163	      },
164	      {
165	        "title": "Table 2: Model Pool Summary — 15 Models",
166	        "columns": [
167	          "Model",
168	          "Family",
169	          "Size",
170	          "Tier",
171	          "Mean η (6 attacks)",
172	          "Clean ACC"
173	        ],
174	        "rows": [
175	          [
176	            "Qwen2.5-7B",
177	            "Qwen",
178	            "7B",
179	            "small",
180	            "0.38",
181	            "0.61"
182	          ],
183	          [
184	            "Qwen2.5-14B",
185	            "Qwen",
186	            "14B",
187	            "medium",
188	            "0.22",
189	            "0.74"
190	          ],
191	          [
192	            "Qwen2.5-72B",
193	            "Qwen",
194	            "72B",
195	            "large",
196	            "0.11",
197	            "0.83"
198	          ],
199	          [
200	            "Llama-3.1-8B",
201	            "Llama",
202	            "8B",
203	            "small",
204	            "0.41",
205	            "0.58"
206	          ],
207	          [
208	            "Llama-3.1-70B",
209	            "Llama",
210	            "70B",
211	            "large",
212	            "0.14",
213	            "0.80"
214	          ],
215	          [
216	            "Mistral-7B",
217	            "Mistral",
218	            "7B",
219	            "small",
220	            "0.44",
221	            "0.55"
222	          ],
223	          [
224	            "Mistral-Nemo-12B",
225	            "Mistral",
226	            "12B",
227	            "medium",
228	            "0.27",
229	            "0.69"
230	          ],
231	          [
232	            "Phi-3-mini",
233	            "Microsoft",
234	            "3.8B",
235	            "small",
236	            "0.49",
237	            "0.52"
238	          ],
239	          [
240	            "Phi-3-medium",
241	            "Microsoft",
242	            "14B",
243	            "medium",
244	            "0.25",
245	            "0.71"
246	          ],
247	          [
248	            "Gemma-2-9B",
249	            "Google",
250	            "9B",
251	            "small",
252	            "0.36",
253	            "0.63"
254	          ],
255	          [
256	            "GPT-4o-mini",
257	            "OpenAI",
258	            "API",
259	            "medium",
260	            "0.19",
261	            "0.76"
262	          ],
263	          [
264	            "GPT-4o",
265	            "OpenAI",
266	            "API",
267	            "large",
268	            "0.08",
269	            "0.87"
270	          ],
271	          [
272	            "GPT-4.1",
273	            "OpenAI",
274	            "API",
275	            "large",
276	            "0.07",
277	            "0.89"
278	          ],
279	          [
280	            "GPT-4.1-mini",
281	            "OpenAI",
282	            "API",
283	            "medium",
284	            "0.16",
285	            "0.78"
286	          ],
287	          [
288	            "Claude-3.5-Haiku",
289	            "Anthropic",
290	            "API",
291	            "medium",
292	            "0.18",
293	            "0.77"
294	          ]
295	        ]
296	      }
297	    ],
298	    "figures": [],
299	    "analysis": "核心 diversity trap framing 受到致命打击。K_eff residualized 显著率从期望的 8/12 降至 4/12，且这 4 个中有 2 个 p 值在 0.02-0.04 之间（经 FDR 校正后可能变 NS）。 仅 1 个 confound-free condition 意味着 residualization 的可信度依赖于线性假设—— reviewer 可以合理质疑 \"你的 K_eff effect 只是 nonlinear η_max effect 的残余\"。 η_max 9/12 显著是稳健的，weakest-link 叙事成立，但这是预期结果不是新发现。 ΔR² = 0.04 使得 \"dual vulnerability driver\" 的 framing 难以为继——第二个 driver 解释力不到 4%。需要 reframe 为 η_max-dominant 故事。\n\n\n15 模型涵盖 3 个 capability tier（small 7-8B、medium 13-14B、large 70B+ 及 API）， tier 跨度增大导致 K_eff 与 η_max 的 confound 加剧（r≈0.73）。高 K_eff panel 几乎 必然混入弱模型，低 K_eff panel 则趋于同质强模型。Residualization 后 K_eff 仅在 4/12 conditions 保持显著——恰好是 transferable attack（score_manipulation, position_bias） 且 η_max 方差本身较大的条件。其余 8 conditions 中 K_eff 的 partial effect 被 η_max 吸收殆尽。η_max 维持 9/12 显著，证明 weakest-link 仍是 dominant driver。 ΔR² 仅 0.04 意味着 K_eff 在 η_max 之上的增量解释力微乎其微。 仅 1 个 confound-free condition（arc×score_manipulation, r≈0.35）中 K_eff 勉强显著 （p=0.032），但单一 condition 无法支撑核心 claim。\n"
300	  },
301	  {
302	    "name": "Attack Type Expansion",
303	    "description": "新增 few-shot hijacking、persona manipulation、instruction override 三种攻击类型， 在 15 模型 455 panel 上运行，产生 6 个新 conditions（2 datasets × 3 new attacks）。\n",
304	    "results": {
305	      "new_conditions": 6,
306	      "keff_resid_sig_new": 2,
307	      "keff_resid_nonsig_new": 4,
308	      "eta_max_sig_new": 5,
309	      "keff_direction_positive_new": 4,
310	      "keff_direction_negative_new": 1,
311	      "keff_direction_near_zero_new": 1,
312	      "mean_R2_new_conditions": 0.31,
313	      "combined_keff_resid_sig_18": 6,
314	      "combined_eta_max_sig_18": 14
315	    },
316	    "tables": [
317	      {
318	        "title": "Table 3: New Attack Types — K_eff Residualized Results",
319	        "columns": [
320	          "Dataset",
321	          "Attack",
322	          "β_ηmax",
323	          "p_ηmax",
324	          "β_Keff_resid",
325	          "p_Keff_resid",
326	          "R²",
327	          "Direction"
328	        ],
329	        "rows": [
330	          [
331	            "MMLU",
332	            "few_shot_hijack",
333	            "0.64",
334	            "0.002",
335	            "0.31",
336	            "0.043",
337	            "0.33",
338	            "positive"
339	          ],
340	          [
341	            "MMLU",
342	            "persona_manip",
343	            "0.91",
344	            "<0.001",
345	            "0.05",
346	            "0.724",
347	            "0.45",
348	            "near-zero"
349	          ],
350	          [
351	            "MMLU",
352	            "instruct_override",
353	            "0.58",
354	            "0.005",
355	            "0.34",
356	            "0.038",
357	            "0.31",
358	            "positive"
359	          ],
360	          [
361	            "ARC",
362	            "few_shot_hijack",
363	            "0.59",
364	            "0.004",
365	            "0.28",
366	            "0.071",
367	            "0.32",
368	            "positive"
369	          ],
370	          [
371	            "ARC",
372	            "persona_manip",
373	            "0.87",
374	            "<0.001",
375	            "-0.12",
376	            "0.389",
377	            "0.41",
378	            "negative"
379	          ],
380	          [
381	            "ARC",
382	            "instruct_override",
383	            "0.62",
384	            "0.003",
385	            "0.26",
386	            "0.088",
387	            "0.30",
388	            "positive"
389	          ]
390	        ]
391	      }
392	    ],
393	    "figures": [],
394	    "analysis": "攻击扩展没有挽救 K_eff 叙事。新增条件中 K_eff 显著率 2/6，其中 persona manipulation 出现方向反转（K_eff 负但 NS）——这与 \"diversity hurts\" 不一致，虽然不显著但给 reviewer 提供了攻击点。合计 18 conditions 中 K_eff 6/18 显著，低于 33% 的 chance expected 阈值，FDR 校正后预计降至 4-5/18。η_max 14/18 显著，进一步巩固 weakest-link 的 dominant 地位。新攻击类型未发现任何 K_eff dominates η_max 的条件。\n\n\n新攻击类型中 few-shot hijacking 和 instruction override 是 transferable attack， K_eff 在这些条件下可能保持微弱正向显著（p≈0.03-0.04）；persona manipulation 则高度 依赖模型特定 persona alignment 训练，η_max 几乎完全解释方差。整体上新增 6 conditions 中仅 2 个 K_eff 显著，且 1 个条件 K_eff 方向为负（persona manipulation on ARC）， 方向不一致削弱了 \"diversity universally hurts\" 的叙事。18 条件合计 K_eff 6/18 ≈ 33% 显著率——FDR 校正后可能进一步缩减至 4-5/18，属于 \"suggestive but not robust\" 水平。\n"
395	  },
396	  {
397	    "name": "Random-Fault BFT Contrast Simulation",
398	    "description": "模拟随机故障场景：每个 judge 以概率 η_j 独立犯错，majority vote 决策。 比较 K_eff 在 random-fault vs adaptive 两种 regime 下的 β 和显著性。\n",
399	    "results": {
400	      "RF_keff_sig_positive": 10,
401	      "RF_keff_nonsig": 2,
402	      "RF_eta_max_sig": 11,
403	      "RF_mean_beta_keff": 0.42,
404	      "adaptive_mean_beta_keff": 0.38,
405	      "BFT_RF_beta_ratio": 0.91,
406	      "RF_mean_R2": 0.62,
407	      "adaptive_mean_R2": 0.38,
408	      "delta_R2_RF_vs_adaptive": 0.24,
409	      "RF_keff_direction": "positive (same as adaptive)",
410	      "regime_contrast_p_interaction": 0.217
411	    },
412	    "tables": [
413	      {
414	        "title": "Table 4: BFT Regime Contrast — K_eff β Comparison",
415	        "columns": [
416	          "Dataset",
417	          "Attack",
418	          "β_Keff (Adaptive)",
419	          "p (Adaptive)",
420	          "β_Keff (RF)",
421	          "p (RF)",
422	          "β Ratio",
423	          "Interaction p"
424	        ],
425	        "rows": [
426	          [
427	            "MMLU",
428	            "sycophancy",
429	            "0.18",
430	            "0.147",
431	            "0.21",
432	            "0.024",
433	            "1.17",
434	            "0.682"
435	          ],
436	          [
437	            "MMLU",
438	            "score_manip",
439	            "0.39",
440	            "0.021",
441	            "0.44",
442	            "0.003",
443	            "1.13",
444	            "0.541"
445	          ],
446	          [
447	            "MMLU",
448	            "position",
449	            "0.24",
450	            "0.089",
451	            "0.28",
452	            "0.011",
453	            "1.17",
454	            "0.614"
455	          ],
456	          [
457	            "MMLU",
458	            "verbosity",
459	            "0.09",
460	            "0.511",
461	            "0.15",
462	            "0.108",
463	            "1.67",
464	            "0.398"
465	          ],
466	          [
467	            "MMLU",
468	            "authority",
469	            "0.15",
470	            "0.218",
471	            "0.19",
472	            "0.047",
473	            "1.27",
474	            "0.583"
475	          ],
476	          [
477	            "MMLU",
478	            "few_shot_hijack",
479	            "0.31",
480	            "0.043",
481	            "0.35",
482	            "0.008",
483	            "1.13",
484	            "0.617"
485	          ],
486	          [
487	            "ARC",
488	            "sycophancy",
489	            "0.12",
490	            "0.341",
491	            "0.16",
492	            "0.072",
493	            "1.33",
494	            "0.521"
495	          ],
496	          [
497	            "ARC",
498	            "score_manip",
499	            "0.41",
500	            "0.032",
501	            "0.48",
502	            "0.001",
503	            "1.17",
504	            "0.434"
505	          ],
506	          [
507	            "ARC",
508	            "position",
509	            "0.22",
510	            "0.102",
511	            "0.27",
512	            "0.015",
513	            "1.23",
514	            "0.548"
515	          ],
516	          [
517	            "ARC",
518	            "verbosity",
519	            "0.06",
520	            "0.649",
521	            "0.11",
522	            "0.198",
523	            "1.83",
524	            "0.412"
525	          ],
526	          [
527	            "ARC",
528	            "authority",
529	            "0.19",
530	            "0.157",
531	            "0.22",
532	            "0.038",
533	            "1.16",
534	            "0.601"
535	          ],
536	          [
537	            "ARC",
538	            "few_shot_hijack",
539	            "0.28",
540	            "0.071",
541	            "0.33",
542	            "0.009",
543	            "1.18",
544	            "0.547"
545	          ]
546	        ]
547	      },
548	      {
549	        "title": "Table 5: R² Comparison Across Regimes",
550	        "columns": [
551	          "Dataset",
552	          "Attack",
553	          "R² (Adaptive)",
554	          "R² (RF)",
555	          "ΔR²"
556	        ],
557	        "rows": [
558	          [
559	            "MMLU",
560	            "sycophancy",
561	            "0.41",
562	            "0.64",
563	            "0.23"
564	          ],
565	          [
566	            "MMLU",
567	            "score_manip",
568	            "0.36",
569	            "0.58",
570	            "0.22"
571	          ],
572	          [
573	            "MMLU",
574	            "position",
575	            "0.39",
576	            "0.61",
577	            "0.22"
578	          ],
579	          [
580	            "MMLU",
581	            "verbosity",
582	            "0.42",
583	            "0.67",
584	            "0.25"
585	          ],
586	          [
587	            "MMLU",
588	            "authority",
589	            "0.37",
590	            "0.59",
591	            "0.22"
592	          ],
593	          [
594	            "MMLU",
595	            "few_shot_hijack",
596	            "0.33",
597	            "0.55",
598	            "0.22"
599	          ],
600	          [
601	            "ARC",
602	            "sycophancy",
603	            "0.43",
604	            "0.69",
605	            "0.26"
606	          ],
607	          [
608	            "ARC",
609	            "score_manip",
610	            "0.35",
611	            "0.57",
612	            "0.22"
613	          ],
614	          [
615	            "ARC",
616	            "position",
617	            "0.38",
618	            "0.62",
619	            "0.24"
620	          ],
621	          [
622	            "ARC",
623	            "verbosity",
624	            "0.44",
625	            "0.71",
626	            "0.27"
627	          ],
628	          [
629	            "ARC",
630	            "authority",
631	            "0.36",
632	            "0.60",
633	            "0.24"
634	          ],
635	          [
636	            "ARC",
637	            "few_shot_hijack",
638	            "0.32",
639	            "0.53",
640	            "0.21"
641	          ]
642	        ]
643	      }
644	    ],
645	    "figures": [],
646	    "analysis": "BFT contrast 实验是 GO/NO-GO gate，结果为 NO-GO。K_eff 在 RF 下不仅没有变负 （diversity helps），反而保持正向且更显著（10/12 vs 4/12 residualized adaptive）。 这意味着 K_eff 的正向效应不是 adaptive adversary 特有的——而是 panel composition 的基本属性（高 diversity → 混入弱模型 → 高 ASR），RF 和 adaptive 下都成立。 BFT reversal mechanism 的核心前提被否定：我们无法证明 diversity 在 RF 下保护但在 adaptive 下有害。唯一可挽救的发现是 ΔR² = 0.24，说明 adaptive attacker 引入了 strategic variance 使得 panel composition 的预测力下降——但这是一个弱得多的 claim， 不足以支撑 Claim 2 作为独立贡献。BFT 应降级为 Discussion 中的 \"open question\"。\n\n\nBFT contrast 的核心预期是 K_eff 在 RF 下显著正向（diversity helps under random faults） 但在 adaptive 下 NS 或反转。Worst 档下实际观察到：K_eff 在 RF 下同样正向显著 （10/12），与 adaptive 下方向一致。原因：在 RF 模拟中 η_j 直接决定 judge 犯错率， 高 K_eff panel 仍然混入高 η_j 的弱模型，majority vote 下弱模型拉低整体正确率。 因此 K_eff 正向不是 \"diversity 主动有害\" 而是 \"diversity 引入弱模型\" 的统计反映—— 这在 RF 和 adaptive 两种 regime 下都成立。β ratio 0.91 表明两种 regime 下 K_eff 的效应量几乎相同，regime interaction term NS (p=0.217)。唯一的 regime 差异是 R²： RF 下 R²=0.62 vs adaptive R²=0.38，ΔR²=0.24——RF 更可预测但这只是因为 RF 没有 strategic variance，不是因为 K_eff 效应不同。BFT reversal mechanism 叙事瓦解。\n"
647	  },
648	  {
649	    "name": "Capability-Matched K_eff Validation",
650	    "description": "在同一 capability tier 内（all-small 7-8B 或 all-large 70B+/API）测试 K_eff 是否 仍然显著。如果 tier-matched panel 中 K_eff 消失 → K_eff 效应是 tier-mixing artifact。\n",
651	    "results": {
652	      "tiers_tested": 3,
653	      "panels_small_tier": 10,
654	      "panels_medium_tier": 10,
655	      "panels_large_tier": 10,
656	      "small_tier_keff_sig": 0,
657	      "medium_tier_keff_sig": 1,
658	      "large_tier_keff_sig": 0,
659	      "total_capability_matched_keff_sig": 1,
660	      "total_conditions_tested": 6,
661	      "eta_max_variance_within_tier": 0.008,
662	      "keff_eta_max_correlation_within_tier": 0.22,
663	      "within_tier_keff_p_range": [
664	        0.041,
665	        0.891
666	      ],
667	      "within_tier_mean_R2": 0.12
668	    },
669	    "tables": [
670	      {
671	        "title": "Table 6: Capability-Matched K_eff Analysis",
672	        "columns": [
673	          "Tier",
674	          "N Panels",
675	          "Condition",
676	          "β_Keff",
677	          "p_Keff",
678	          "R²",
679	          "η_max Var"
680	        ],
681	        "rows": [
682	          [
683	            "Small (7-8B)",
684	            "10",
685	            "MMLU×sycophancy",
686	            "0.08",
687	            "0.721",
688	            "0.09",
689	            "0.007"
690	          ],
691	          [
692	            "Small (7-8B)",
693	            "10",
694	            "ARC×score_manip",
695	            "0.14",
696	            "0.548",
697	            "0.11",
698	            "0.008"
699	          ],
700	          [
701	            "Medium (12-14B+API-mini)",
702	            "10",
703	            "MMLU×sycophancy",
704	            "0.11",
705	            "0.612",
706	            "0.10",
707	            "0.009"
708	          ],
709	          [
710	            "Medium (12-14B+API-mini)",
711	            "10",
712	            "ARC×score_manip",
713	            "0.29",
714	            "0.041",
715	            "0.18",
716	            "0.011"
717	          ],
718	          [
719	            "Large (70B+API)",
720	            "10",
721	            "MMLU×sycophancy",
722	            "0.06",
723	            "0.891",
724	            "0.07",
725	            "0.004"
726	          ],
727	          [
728	            "Large (70B+API)",
729	            "10",
730	            "ARC×score_manip",
731	            "0.09",
732	            "0.684",
733	            "0.08",
734	            "0.005"
735	          ]
736	        ]
737	      }
738	    ],
739	    "figures": [],
740	    "analysis": "这是对 diversity trap framing 的最强反驳。Capability-matched 0-1/6 显著意味着 K_eff 的独立效应在控制 capability 后基本消失。Residualized analysis 在全池中仍然 显著 4/12 的原因是：residualization 假设线性关系，但 K_eff-η_max confound 可能是 非线性的（阶梯型：跨 tier → K_eff 骤升 + η_max 骤升），线性 residualization 无法完全去除。Capability-matched 是更强的 confound control（分层而非回归调整）， 结果否定了 K_eff 的独立效应。需要在论文中诚实报告这个 null result，将 K_eff 从 core claim 降级为 \"exploratory, potentially confounded\"。\n\n\nCapability-matched 是 worst 档的致命实验。同 tier 内模型能力相近，η_max 方差极小 （约 0.008 vs 全池 0.045），消除了 tier-mixing confound。结果：K_eff 仅在 1/6 条件下显著（medium tier × score_manipulation, p=0.041，FDR 后可能 NS），其余 5/6 全部 NS。这直接证明 K_eff 的表面效应是 tier-mixing 的统计幻象：当你在全池抽 panel， 高 K_eff panel 跨 tier 抽样（混入 7B 和 70B），低 K_eff panel 同 tier 抽样—— K_eff 与 η_max 的相关性是 tier-mixing 的副产品，不是因果关系。 每个 tier 仅 C(5,3)=10 个 panel，样本量不足以检测小效应，但即便如此 η_max 方差 消失也说明在能力控制后 K_eff 没有独立的预测力。Reviewer 可以合理论证： \"K_eff effect = capability heterogeneity effect, not diversity per se\"。\n"
741	  },
742	  {
743	    "name": "Two-Stage Panel Design Algorithm Benchmark",
744	    "description": "Robustness-first 两阶段选择：(1) 筛选 η ≤ threshold 的 judge，(2) 在剩余中最大化 K_eff。 与 5 个 baseline（random, max-K_eff, strongest-K, min-η, diversity-only）对比。\n",
745	    "results": {
746	      "baselines_tested": 5,
747	      "two_stage_vs_strongest_K_ASR_reduction_pct": 2.3,
748	      "two_stage_vs_strongest_K_p": 0.312,
749	      "two_stage_vs_random_ASR_reduction_pct": 18.4,
750	      "two_stage_vs_max_keff_ASR_reduction_pct": 31.2,
751	      "min_eta_dominates_conditions": 4,
752	      "two_stage_dominates_conditions": 1,
753	      "strongest_K_dominates_conditions": 1,
754	      "two_stage_ASR_reduction_pct": 3.1,
755	      "two_stage_vs_strongest_K_stat_sig": false,
756	      "optimal_eta_threshold": 0.15
757	    },
758	    "tables": [
759	      {
760	        "title": "Table 7: Panel Selection Strategy Comparison (mean ASR across 6 attacks)",
761	        "columns": [
762	          "Strategy",
763	          "Mean ASR",
764	          "vs Strongest-K Δ%",
765	          "p vs Strongest-K",
766	          "Wins (6 conditions)"
767	        ],
768	        "rows": [
769	          [
770	            "Random",
771	            "0.284",
772	            "+21.5%",
773	            "<0.001",
774	            "0"
775	          ],
776	          [
777	            "Max-K_eff",
778	            "0.341",
779	            "+45.9%",
780	            "<0.001",
781	            "0"
782	          ],
783	          [
784	            "Diversity-Only",
785	            "0.312",
786	            "+33.5%",
787	            "<0.001",
788	            "0"
789	          ],
790	          [
791	            "Min-η_max",
792	            "0.229",
793	            "-2.1%",
794	            "0.478",
795	            "4"
796	          ],
797	          [
798	            "Strongest-K",
799	            "0.234",
800	            "—",
801	            "—",
802	            "1"
803	          ],
804	          [
805	            "Two-Stage",
806	            "0.227",
807	            "-3.1%",
808	            "0.312",
809	            "1"
810	          ]
811	        ]
812	      },
813	      {
814	        "title": "Table 8: Two-Stage vs Strongest-K Per Condition",
815	        "columns": [
816	          "Condition",
817	          "ASR (Two-Stage)",
818	          "ASR (Strongest-K)",
819	          "Δ%",
820	          "p"
821	        ],
822	        "rows": [
823	          [
824	            "MMLU×sycophancy",
825	            "0.211",
826	            "0.219",
827	            "-3.7%",
828	            "0.284"
829	          ],
830	          [
831	            "MMLU×score_manip",
832	            "0.198",
833	            "0.207",
834	            "-4.3%",
835	            "0.198"
836	          ],
837	          [
838	            "MMLU×position",
839	            "0.237",
840	            "0.241",
841	            "-1.7%",
842	            "0.641"
843	          ],
844	          [
845	            "ARC×sycophancy",
846	            "0.241",
847	            "0.248",
848	            "-2.8%",
849	            "0.352"
850	          ],
851	          [
852	            "ARC×score_manip",
853	            "0.185",
854	            "0.194",
855	            "-4.6%",
856	            "0.187"
857	          ],
858	          [
859	            "ARC×position",
860	            "0.249",
861	            "0.253",
862	            "-1.6%",
863	            "0.689"
864	          ]
865	        ]
866	      }
867	    ],
868	    "figures": [],
869	    "analysis": "Two-stage ≤5% improvement over strongest-K 且无统计显著性。这与 worst 档的预期一致： 如果 K_eff 没有独立效应（plan_004），那么在 robustness-screened pool 中最大化 K_eff 不应带来额外收益。Max-K_eff 是最差策略（ASR 最高）这一发现仍然有价值—— 它警告不要盲目追求 diversity——但这只需 η_max 解释就够了（高 K_eff = 混入弱模型 = 高 ASR）， 不需要 \"diversity independently hurts\" 的 claim。实践建议简化为 \"pick the most robust judges, ignore diversity\"，这比 two-stage 更简单但可能过于平凡。\n\n\n在 worst 档下 K_eff 的独立效应已消失（plan_004 显示 capability-matched 后 K_eff NS）， 因此两阶段的第二步（maximize K_eff among screened judges）几乎不提供额外收益。 Robustness screening（step 1）本身有效——排除 η > threshold 的弱模型大幅降低 ASR—— 但这与简单的 strongest-K 策略效果相同。Two-stage 与 strongest-K 的差异仅 2.3% （p=0.312, NS），因为 screening 后剩余模型能力相近，K_eff 的变异范围收窄。 min_eta（不考虑 diversity）在 4/6 conditions 表现最佳，进一步说明 panel 安全由 最弱 judge 决定。Two-stage 的存在意义被削弱：如果第二步（diversity）没用， 算法退化为 \"just pick the strongest K models\"。\n"
870	  },
871	  {
872	    "name": "Per-Judge ASR Concentration Analysis",
873	    "description": "对每个 panel × attack，计算各 judge 的 ASR 分布，用 Gini 系数和 entropy 量化 adaptive adversary 的 targeting 集中度。高 Gini = adversary 集中攻击特定 judge。\n",
874	    "results": {
875	      "mean_gini_adaptive": 0.38,
876	      "mean_gini_random_fault": 0.12,
877	      "gini_diff_p": "<0.001",
878	      "mean_entropy_adaptive": 2.41,
879	      "mean_entropy_random_fault": 3.22,
880	      "entropy_diff_p": "<0.001",
881	      "gini_keff_correlation": 0.21,
882	      "gini_keff_p": 0.089,
883	      "gini_eta_max_correlation": 0.67,
884	      "gini_eta_max_p": "<0.001",
885	      "high_gini_panels_pct": 34,
886	      "targeting_consistent_across_attacks": false
887	    },
888	    "tables": [
889	      {
890	        "title": "Table 9: ASR Concentration Statistics",
891	        "columns": [
892	          "Metric",
893	          "Adaptive (mean)",
894	          "Adaptive (SD)",
895	          "RF (mean)",
896	          "RF (SD)",
897	          "Diff p"
898	        ],
899	        "rows": [
900	          [
901	            "Gini",
902	            "0.38",
903	            "0.14",
904	            "0.12",
905	            "0.05",
906	            "<0.001"
907	          ],
908	          [
909	            "Entropy (bits)",
910	            "2.41",
911	            "0.52",
912	            "3.22",
913	            "0.31",
914	            "<0.001"
915	          ],
916	          [
917	            "Max single-judge share",
918	            "0.51",
919	            "0.12",
920	            "0.38",
921	            "0.06",
922	            "<0.001"
923	          ]
924	        ]
925	      },
926	      {
927	        "title": "Table 10: Gini Coefficient Correlations",
928	        "columns": [
929	          "Predictor",
930	          "r with Gini",
931	          "p",
932	          "Interpretation"
933	        ],
934	        "rows": [
935	          [
936	            "η_max",
937	            "0.67",
938	            "<0.001",
939	            "Targeting tracks individual weakness"
940	          ],
941	          [
942	            "K_eff",
943	            "0.21",
944	            "0.089",
945	            "Weak/NS association with diversity"
946	          ],
947	          [
948	            "Panel size",
949	            "0.04",
950	            "0.814",
951	            "No panel size effect"
952	          ],
953	          [
954	            "Mean capability",
955	            "-0.58",
956	            "<0.001",
957	            "Stronger panels → less concentrated targeting"
958	          ]
959	        ]
960	      }
961	    ],
962	    "figures": [],
963	    "analysis": "Per-judge 浓度分析提供了 adaptive vs RF 差异的直接证据——这是一个有用的 finding， 可作为 paper 的 empirical contribution。但分析同时削弱了 diversity trap：targeting 集中度由 η_max（而非 K_eff）解释。Adaptive adversary 攻击最弱 judge，不是利用 diverse attack surface。这与 reframed narrative（η_max dominant, diversity irrelevant） 一致。Gini 分析可以移入 \"Adaptive Adversary Behavior\" 子节，作为 η_max dominance 的补充证据，而非 diversity trap 的支持。\n\n\nAdaptive adversary 确实展现 targeting 行为（Gini 0.38 vs RF 0.12），但集中度 中等而非极端。关键问题：Gini 与 η_max 高度相关（r=0.67）但与 K_eff 弱相关（r=0.21, NS）。 这意味着 targeting 主要针对最弱 judge（η_max 高的 panel 中弱 judge 更容易被攻克）， 而不是利用 diversity 创造的 diverse attack surface。如果 K_eff 独立驱动 targeting， 我们预期 Gini 与 K_eff 显著相关（高 diversity → adversary 有更多独立漏洞可攻击 → 攻击更集中于特定 judge），但 p=0.089 未达显著。此外 targeting 不跨攻击一致—— 同一 panel 在不同攻击下被 target 的 judge 不同，进一步削弱 \"structural diversity creates systematic exploitable surface\" 的论点。\n"
964	  },
965	  {
966	    "name": "Diversity-Capability Tradeoff Visualization",
967	    "description": "绘制 K_eff vs η_max across 455 panels，拟合 tradeoff curve，Pareto frontier analysis， 按 tier 分层。\n",
968	    "results": {
969	      "keff_eta_max_pearson_r": 0.73,
970	      "keff_eta_max_spearman_rho": 0.71,
971	      "tradeoff_curve_R2": 0.53,
972	      "pareto_frontier_size": 12,
973	      "pareto_pct_from_large_tier": 83,
974	      "pareto_pct_from_mixed_tier": 17,
975	      "pareto_pct_from_small_tier": 0,
976	      "pareto_panels_mean_keff": 1.82,
977	      "pareto_panels_mean_eta_max": 0.09,
978	      "non_pareto_gap_ASR": 0.11
979	    },
980	    "tables": [
981	      {
982	        "title": "Table 11: Pareto Frontier Panel Characteristics",
983	        "columns": [
984	          "Panel ID",
985	          "Models",
986	          "K_eff",
987	          "η_max",
988	          "Mean ASR",
989	          "Tier Composition"
990	        ],
991	        "rows": [
992	          [
993	            "P_012",
994	            "GPT-4.1 / GPT-4o / Qwen72B",
995	            "1.91",
996	            "0.08",
997	            "0.142",
998	            "all-large"
999	          ],
1000	          [
1001	            "P_034",
1002	            "GPT-4.1 / Llama70B / GPT-4o",
1003	            "2.14",
1004	            "0.09",
1005	            "0.151",
1006	            "all-large"
1007	          ],
1008	          [
1009	            "P_087",
1010	            "GPT-4.1 / GPT-4o / Claude-Haiku",
1011	            "1.72",
1012	            "0.07",
1013	            "0.138",
1014	            "large+medium"
1015	          ],
1016	          [
1017	            "P_156",
1018	            "GPT-4o / Qwen72B / Llama70B",
1019	            "2.31",
1020	            "0.11",
1021	            "0.163",
1022	            "all-large"
1023	          ],
1024	          [
1025	            "P_201",
1026	            "GPT-4.1 / GPT-4.1m / GPT-4o",
1027	            "1.45",
1028	            "0.07",
1029	            "0.131",
1030	            "all-large"
1031	          ]
1032	        ]
1033	      }
1034	    ],
1035	    "figures": [],
1036	    "analysis": "Tradeoff visualization 是一个 clean methodological contribution，无论 K_eff 是否有 独立效应都有价值。它展示了当前 LLM 生态中 panel design 的结构约束：diversity 和 robustness 不是独立可优化的维度。但在 worst 档下，这更多被解读为 confound 的可视化 证据而非独立发现。可在论文中保留为 Fig 2 或 Fig 3，作为 \"understanding the evaluation landscape\" 的贡献。\n\n\nTradeoff 可视化清晰展示了 K_eff 与 η_max 的结构性关联：r=0.73，Pareto frontier 几乎完全由 large-tier panel 占据（83%），因为只有在全部选择强模型时才能同时获得 低 η_max 和中等 K_eff。Small-tier panel 全部位于 Pareto frontier 之下。 这个 visualization 本身有价值（展示了 evaluation panel design 的结构约束）， 但在 worst 档下它更多地支持了 \"K_eff effect is confound\" 的叙事：tradeoff 不是 独立的两个维度的 tension，而是 tier-mixing 的必然结果。Pareto frontier 上的 panel 基本就是 \"all strong models\"，equivalent to strongest-K 策略。\n"
1037	  },
1038	  {
1039	    "name": "Panel Size Sensitivity Analysis",
1040	    "description": "测试 K=3,5,7,9 不同 panel size 下 η_max 与 K_eff 的相对重要性是否变化。\n",
1041	    "results": {
1042	      "K3_panels": 455,
1043	      "K5_panels": 3003,
1044	      "K7_panels": 6435,
1045	      "K9_panels": 5005,
1046	      "K3_eta_max_sig_ratio": 0.75,
1047	      "K5_eta_max_sig_ratio": 0.83,
1048	      "K7_eta_max_sig_ratio": 0.92,
1049	      "K9_eta_max_sig_ratio": 0.92,
1050	      "K3_keff_resid_sig_ratio": 0.33,
1051	      "K5_keff_resid_sig_ratio": 0.25,
1052	      "K7_keff_resid_sig_ratio": 0.17,
1053	      "K9_keff_resid_sig_ratio": 0.08,
1054	      "keff_effect_trend_with_K": "monotonically decreasing"
1055	    },
1056	    "tables": [
1057	      {
1058	        "title": "Table 12: Panel Size Sensitivity — Significance Ratios",
1059	        "columns": [
1060	          "K",
1061	          "N Panels",
1062	          "η_max sig ratio",
1063	          "K_eff resid sig ratio",
1064	          "Mean R²",
1065	          "K_eff-η_max r"
1066	        ],
1067	        "rows": [
1068	          [
1069	            "3",
1070	            "455",
1071	            "0.75",
1072	            "0.33",
1073	            "0.38",
1074	            "0.73"
1075	          ],
1076	          [
1077	            "5",
1078	            "3003",
1079	            "0.83",
1080	            "0.25",
1081	            "0.41",
1082	            "0.68"
1083	          ],
1084	          [
1085	            "7",
1086	            "6435",
1087	            "0.92",
1088	            "0.17",
1089	            "0.44",
1090	            "0.61"
1091	          ],
1092	          [
1093	            "9",
1094	            "5005",
1095	            "0.92",
1096	            "0.08",
1097	            "0.46",
1098	            "0.54"
1099	          ]
1100	        ]
1101	      }
1102	    ],
1103	    "figures": [],
1104	    "analysis": "Panel size 分析揭示 K_eff 效应的 artifactual nature：它在小 panel（K=3）中最强 恰好是 tier-mixing 方差最大的地方。随 K 增大，confound 缓解，K_eff 效应消退。 η_max 的趋势则相反——大 panel 中仍有弱 judge，且 R² 随 K 增大说明 panel composition 的可预测性提高。这是支持 \"K_eff is confound\" 的又一条证据线。\n\n\nPanel size 增大时 η_max dominance 增强，K_eff effect 递减。原因：K=9 的 panel 包含 9/15 模型，几乎所有 panel 都包含至少一个弱模型，η_max 方差缩小但 level 保持高位。 同时 K_eff 的变异范围也缩小（大 panel 的 K_eff 趋向收敛）。更重要的是，majority vote 在大 panel 中的容错能力提高——但这被 η_max 的 monotonic 效应抵消（一个极弱 judge 的影响在 K=3 中是 catastrophic，在 K=9 中被稀释）。K_eff 的 sig ratio 从 K=3 的 0.33 降至 K=9 的 0.08，表明 K_eff 的表面效应主要在小 panel 中出现（因为 tier-mixing 的方差更大），进一步支持 confound 解释。\n"
1105	  },
1106	  {
1107	    "name": "VIF and Multicollinearity Deep Dive",
1108	    "description": "对现有回归数据进行全面多重共线性分析：VIF、偏相关、residualized K_eff、 Bonferroni/FDR correction、bootstrap CI、排除极端模型的敏感性分析、beta regression。\n",
1109	    "results": {
1110	      "VIF_keff_full_model": 2.14,
1111	      "VIF_eta_max_full_model": 2.14,
1112	      "keff_resid_sig_bonferroni_12": 2,
1113	      "keff_resid_sig_fdr_12": 4,
1114	      "keff_resid_sig_bootstrap_95CI_excludes_zero": 3,
1115	      "keff_resid_sig_exclude_extreme_models": 4,
1116	      "keff_resid_sig_exclude_extreme_models_fdr": 3,
1117	      "beta_regression_keff_sig": 3,
1118	      "beta_regression_eta_max_sig": 10,
1119	      "partial_r_keff_given_eta_max": 0.14,
1120	      "partial_r_eta_max_given_keff": 0.41,
1121	      "sensitivity_analyses_convergent": false,
1122	      "keff_resid_sig_range_across_methods": [
1123	        2,
1124	        5
1125	      ]
1126	    },
1127	    "tables": [
1128	      {
1129	        "title": "Table 13: K_eff Residualized Significance Under Different Correction Methods",
1130	        "columns": [
1131	          "Method",
1132	          "K_eff sig count (/12)",
1133	          "η_max sig count (/12)",
1134	          "Notes"
1135	        ],
1136	        "rows": [
1137	          [
1138	            "Uncorrected",
1139	            "7",
1140	            "10",
1141	            "Liberal"
1142	          ],
1143	          [
1144	            "FDR (BH)",
1145	            "4",
1146	            "9",
1147	            "Standard"
1148	          ],
1149	          [
1150	            "Bonferroni",
1151	            "2",
1152	            "8",
1153	            "Conservative"
1154	          ],
1155	          [
1156	            "Bootstrap 95% CI",
1157	            "3",
1158	            "9",
1159	            "Non-parametric"
1160	          ],
1161	          [
1162	            "Exclude extreme models (FDR)",
1163	            "3",
1164	            "9",
1165	            "Sensitivity"
1166	          ],
1167	          [
1168	            "Beta regression (FDR)",
1169	            "3",
1170	            "10",
1171	            "Bounded DV"
1172	          ]
1173	        ]
1174	      },
1175	      {
1176	        "title": "Table 14: Partial Correlations",
1177	        "columns": [
1178	          "Predictor",
1179	          "Partial r (controlling other)",
1180	          "95% CI",
1181	          "p"
1182	        ],
1183	        "rows": [
1184	          [
1185	            "K_eff | η_max",
1186	            "0.14",
1187	            "[0.05, 0.23]",
1188	            "0.003"
1189	          ],
1190	          [
1191	            "η_max | K_eff",
1192	            "0.41",
1193	            "[0.33, 0.49]",
1194	            "<0.001"
1195	          ]
1196	        ]
1197	      }
1198	    ],
1199	    "figures": [],
1200	    "analysis": "VIF 分析是 worst 档的核心打击。K_eff 的显著性在 2-5/12 范围内波动，高度依赖 统计方法选择——这是 \"researcher degrees of freedom\" 问题。Partial r (K_eff | η_max) = 0.14 意味着 K_eff 在控制 η_max 后仅解释 2% 的独特方差（r²=0.02）。相比之下 η_max 的 partial r = 0.41（17% 独特方差）。即使 K_eff 有微弱的独立效应，其实际意义（practical significance）可忽略。论文中需要诚实报告所有方法的结果范围，不能只报最有利的。\n\n\nVIF=2.14 在传统标准下不算严重（<5），但这掩盖了非线性 confound。Bonferroni 最严格， K_eff 降至 2/12 显著；FDR 保持 4/12；bootstrap CI 给出 3/12（因为 bootstrap 在 455 panels 中重复抽样，resampling variance 较大导致 CI 加宽）。排除极端模型 （ACC < 0.5 的 2 个模型）后 K_eff 4/12→3/12（FDR），说明效应部分依赖极端值。 Beta regression（适合 bounded proportion DV）与 OLS 结果不一致——K_eff 仅 3/12 显著（beta regression 对极端值更稳健）。核心问题：不同分析方法给出 2-5/12 的 显著性范围，缺乏收敛性。Reviewer 可以选择最严格的估计（2/12 Bonferroni）argue K_eff 无效应，或选择最宽松的（5/12 FDR without extreme exclusion）argue suggestive。 这种方法敏感性本身就是 \"not robust\" 的标志。\n"
1201	  },
1202	  {
1203	    "name": "Aggregation Rule Comparison",
1204	    "description": "在 15 模型 455 panel 上测试 majority vote、threshold voting（unanimity）、 weighted voting、Bayesian aggregation 四种聚合规则下的 K_eff 和 η_max 效应。\n",
1205	    "results": {
1206	      "majority_keff_resid_sig": 4,
1207	      "majority_eta_max_sig": 9,
1208	      "threshold_keff_resid_sig": 6,
1209	      "threshold_eta_max_sig": 7,
1210	      "weighted_keff_resid_sig": 2,
1211	      "weighted_eta_max_sig": 10,
1212	      "bayesian_keff_resid_sig": 1,
1213	      "bayesian_eta_max_sig": 5,
1214	      "keff_sig_varies_by_aggregation": true,
1215	      "aggregation_dependency_interpretation": "K_eff effect is aggregation artifact"
1216	    },
1217	    "tables": [
1218	      {
1219	        "title": "Table 15: Aggregation Rule × Vulnerability Driver Analysis",
1220	        "columns": [
1221	          "Aggregation",
1222	          "K_eff sig (/12)",
1223	          "η_max sig (/12)",
1224	          "Mean R²",
1225	          "Best Predictor"
1226	        ],
1227	        "rows": [
1228	          [
1229	            "Majority Vote",
1230	            "4",
1231	            "9",
1232	            "0.38",
1233	            "η_max"
1234	          ],
1235	          [
1236	            "Threshold (Unanimity)",
1237	            "6",
1238	            "7",
1239	            "0.42",
1240	            "mixed"
1241	          ],
1242	          [
1243	            "Accuracy-Weighted",
1244	            "2",
1245	            "10",
1246	            "0.45",
1247	            "η_max"
1248	          ],
1249	          [
1250	            "Bayesian",
1251	            "1",
1252	            "5",
1253	            "0.29",
1254	            "η_max (weakened)"
1255	          ]
1256	        ]
1257	      },
1258	      {
1259	        "title": "Table 16: Aggregation as Defense — Mean ASR Comparison",
1260	        "columns": [
1261	          "Aggregation",
1262	          "Mean ASR (all panels)",
1263	          "ASR (top-10 panels)",
1264	          "ASR (bottom-10 panels)",
1265	          "Spread"
1266	        ],
1267	        "rows": [
1268	          [
1269	            "Majority",
1270	            "0.261",
1271	            "0.142",
1272	            "0.418",
1273	            "0.276"
1274	          ],
1275	          [
1276	            "Threshold",
1277	            "0.183",
1278	            "0.098",
1279	            "0.312",
1280	            "0.214"
1281	          ],
1282	          [
1283	            "Weighted",
1284	            "0.224",
1285	            "0.121",
1286	            "0.367",
1287	            "0.246"
1288	          ],
1289	          [
1290	            "Bayesian",
1291	            "0.198",
1292	            "0.112",
1293	            "0.294",
1294	            "0.182"
1295	          ]
1296	        ]
1297	      }
1298	    ],
1299	    "figures": [],
1300	    "analysis": "Aggregation 分析是 worst 档中最具建设性的发现。虽然它进一步削弱了 K_eff 作为 independent driver 的 claim（aggregation-dependent → possible artifact），但它提供了 实际价值：(a) Bayesian aggregation 作为 defense 的有效性（ASR 均值和方差同时降低）； (b) Threshold voting 最严格但 K_eff 效应最强——不适合 adversarial setting； (c) Accuracy-weighted 是 good middle ground（K_eff 几乎消失，η_max 仍可控）。 可以 reframe 为 practical contribution: \"choosing the right aggregation rule matters more than panel diversity composition\"。\n\n\n聚合规则分析暴露 K_eff 效应的 aggregation dependency。Threshold voting（unanimity） 下 K_eff 6/12 显著——因为 unanimity 放大了单个 judge 的 veto power，diverse panel 中弱 judge 更可能 veto 正确判断。但这不是 \"diversity hurts\"，而是 \"unanimity amplifies weakest-link effect, and diverse panels have weaker links\"。Bayesian aggregation 大幅削弱两个 predictor：η_max 5/12，K_eff 1/12——Bayesian weighting 有效下调了不可靠 judge 的权重，部分 neutralize 了 weakest-link 效应。 Weighted voting 下 K_eff 几乎消失（2/12），因为 accuracy-based weights 自动 降权弱模型。核心问题：K_eff 的显著性从 1/12（Bayesian）到 6/12（threshold）—— 如果 K_eff 是真正的 structural vulnerability driver，它不应该如此依赖聚合规则。 这种依赖性暗示 K_eff 效应实际上是特定聚合规则对弱 judge 处理方式的 artifact。\n"
1301	  },
1302	  {
1303	    "name": "Open-Ended Generation Benchmark",
1304	    "description": "在 MT-Bench 或 AlpacaEval 风格的开放式生成任务上运行攻击实验， 验证 MCQ findings 是否推广到 open-ended evaluation。\n",
1305	    "results": {
1306	      "benchmark": "MT-Bench (adapted)",
1307	      "n_conditions": 4,
1308	      "keff_resid_sig_positive": 0,
1309	      "keff_resid_sig_negative": 1,
1310	      "keff_resid_nonsig": 3,
1311	      "eta_max_sig": 4,
1312	      "keff_direction_inconsistent_with_MCQ": true,
1313	      "open_ended_mean_ASR": 0.34,
1314	      "MCQ_mean_ASR": 0.26,
1315	      "eta_max_dominance_ratio_open": 0.91
1316	    },
1317	    "tables": [
1318	      {
1319	        "title": "Table 17: Open-Ended Task Results",
1320	        "columns": [
1321	          "Task Subset",
1322	          "Attack",
1323	          "β_ηmax",
1324	          "p_ηmax",
1325	          "β_Keff_resid",
1326	          "p_Keff_resid",
1327	          "Direction"
1328	        ],
1329	        "rows": [
1330	          [
1331	            "MT-Bench-Writing",
1332	            "style_manip",
1333	            "0.79",
1334	            "<0.001",
1335	            "-0.22",
1336	            "0.034",
1337	            "NEGATIVE"
1338	          ],
1339	          [
1340	            "MT-Bench-Reasoning",
1341	            "logic_distort",
1342	            "0.84",
1343	            "<0.001",
1344	            "0.08",
1345	            "0.541",
1346	            "near-zero"
1347	          ],
1348	          [
1349	            "MT-Bench-Coding",
1350	            "output_inject",
1351	            "0.71",
1352	            "0.002",
1353	            "0.15",
1354	            "0.218",
1355	            "positive (NS)"
1356	          ],
1357	          [
1358	            "MT-Bench-Math",
1359	            "step_skip",
1360	            "0.88",
1361	            "<0.001",
1362	            "-0.05",
1363	            "0.712",
1364	            "near-zero"
1365	          ]
1366	        ]
1367	      }
1368	    ],
1369	    "figures": [],
1370	    "analysis": "Open-ended 结果是 diversity trap 叙事的 generalizability failure。K_eff 在 MCQ 上 的正向效应不推广到 open-ended 评估——方向不一致且 1 个条件甚至反转。这使得 diversity trap 从 general finding 降级为 MCQ-specific observation，reviewers 会 质疑：如果 diversity 只在 MCQ 中 \"hurts\"，这到底是 diversity 的问题还是 MCQ evaluation 的 artifact？η_max 在两种任务上都一致显著，强化了 weakest-link 作为 universal driver 的地位。Reframe 后论文应在 title/abstract 中避免 generalize， 限定为 \"MCQ-based evaluation\" 或在 Discussion 中作为 limitation 显著标注。\n\n\nOpen-ended 任务与 MCQ 的攻击动态根本不同。MCQ 攻击通过影响 judge 对特定选项的偏好， K_eff 的 confound 来自 tier-mixing。Open-ended 评估中 judge 需要评估文本质量—— 攻击更多依赖 persuasive text generation，所有 judge 面临相似的 adversarial text。 因此 η_max 完全主导（4/4 sig）：最弱 judge 被最容易说服。K_eff 方向混乱——1 个 条件甚至显著负向（diverse panel 更好），因为 open-ended 评估中不同 judge 对文本 质量的多角度评估确实可以互补（更接近 BFT 的 benign fault 假设）。这与 MCQ 结果 不一致是 worst 档的关键打击：如果 diversity trap 不跨任务推广，它就不是一般性 原理，而是 MCQ 评估的特异性现象——可能由 MCQ 的离散选择结构 + tier-mixing confound 共同驱动。\n"
1371	  },
1372	  {
1373	    "name": "Partial-Knowledge Adversary Simulation",
1374	    "description": "模拟 adversary 仅知 judge family 但不知具体 vulnerability profile 的场景。 与 full-knowledge adversary 对比 ASR degradation。\n",
1375	    "results": {
1376	      "full_knowledge_mean_ASR": 0.261,
1377	      "partial_knowledge_mean_ASR": 0.238,
1378	      "no_knowledge_mean_ASR": 0.204,
1379	      "ASR_degradation_full_to_partial_pct": 8.8,
1380	      "ASR_degradation_full_to_none_pct": 21.8,
1381	      "partial_keff_sig": 2,
1382	      "partial_eta_max_sig": 8,
1383	      "family_knowledge_utility": "modest",
1384	      "keff_effect_under_partial": "weaker than full, similar direction"
1385	    },
1386	    "tables": [
1387	      {
1388	        "title": "Table 18: Adversary Knowledge Level Comparison",
1389	        "columns": [
1390	          "Knowledge Level",
1391	          "Mean ASR",
1392	          "K_eff sig (/12)",
1393	          "η_max sig (/12)",
1394	          "R²"
1395	        ],
1396	        "rows": [
1397	          [
1398	            "Full (exact η_j)",
1399	            "0.261",
1400	            "4",
1401	            "9",
1402	            "0.38"
1403	          ],
1404	          [
1405	            "Partial (family only)",
1406	            "0.238",
1407	            "2",
1408	            "8",
1409	            "0.34"
1410	          ],
1411	          [
1412	            "None (uniform attack)",
1413	            "0.204",
1414	            "0",
1415	            "6",
1416	            "0.22"
1417	          ]
1418	        ]
1419	      },
1420	      {
1421	        "title": "Table 19: ASR Degradation Analysis",
1422	        "columns": [
1423	          "Transition",
1424	          "ΔASR",
1425	          "Δ%",
1426	          "Interpretation"
1427	        ],
1428	        "rows": [
1429	          [
1430	            "Full → Partial",
1431	            "-0.023",
1432	            "-8.8%",
1433	            "Family info has modest value"
1434	          ],
1435	          [
1436	            "Full → None",
1437	            "-0.057",
1438	            "-21.8%",
1439	            "Model knowledge matters but not dramatically"
1440	          ],
1441	          [
1442	            "Partial → None",
1443	            "-0.034",
1444	            "-14.3%",
1445	            "Family info alone provides limited advantage"
1446	          ]
1447	        ]
1448	      }
1449	    ],
1450	    "figures": [],
1451	    "analysis": "Partial-knowledge 分析有两个重要含义：(a) 实践上，adversary 不需要精确 vulnerability 知识就能实现高 ASR（从 0.261 到 0.204 的下降 modest）——这本身是一个重要的安全发现； (b) 理论上，K_eff 效应依赖 full-knowledge 假设，在更现实的 threat model 下消失—— 这削弱了 K_eff 作为 general vulnerability driver 的 claim。在 reframed 论文中， 这个实验可以支持 \"η_max is robust across threat models while K_eff is threat-model-specific\" 的叙事。\n\nPartial-knowledge adversary（知 family 不知具体 vulnerability）仅比 full-knowledge 下降 8.8% ASR——说明 family 信息提供的攻击优势有限，因为 same-family 模型的 vulnerability profile 差异大（family labels 不可靠，plan_004 的 claim 4）。 No-knowledge adversary 下降 21.8%——说明 any model knowledge 都有价值但不是 dramatic。 K_eff 在 partial-knowledge 下仅 2/12 显著，进一步弱化了 \"diverse attack surface\" 叙事：如果 adversary 不知道具体 vulnerability，panel diversity 不应创造可利用的 attack surface（adversary 无法 target specific judges）。K_eff 效应在 partial-knowledge 下几乎消失，暗示 full-knowledge 下的 K_eff 效应部分来自 adversary 对具体 vulnerability 的知识（即 K_eff 效应依赖 threat model 假设——full-knowledge 在实践中不现实）。\n"
1452	  }
1453	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "246d8382-02ca-4b90-9855-2b3cdd2199a7",
  "isSidechain": false,
  "promptId": "a4e49dfa-ac88-470f-90c8-78060d831735",
  "type": "user",
  "uuid": "e7e20ec7-f2d3-4569-a5fa-8b54c92875c1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"15-Model Scale Expansion\",\n    \"description\": \"扩展至 15 个模型（6 open-source + 4 API + 大型开源 70B/72B），重跑 MI matrix 和 全 panel（C(15,3)=455）回归分析。12 conditions（2 datasets × 6 attacks）。\\n\",\n    \"results\": {\n      \"n_models\": 15,\n      \"n_panels\": 455,\n      \"n_conditions\": 12,\n      \"keff_raw_sig_positive\": 7,\n      \"keff_raw_sig_negative\": 0,\n      \"keff_raw_nonsig\": 5,\n      \"keff_resid_sig_positive\": 4,\n      \"keff_resid_nonsig\": 8,\n      \"eta_max_sig\": 9,\n      \"mean_R2_full_model\": 0.38,\n      \"mean_R2_eta_max_only\": 0.34,\n      \"delta_R2_keff_contribution\": 0.04,\n      \"keff_eta_max_correlation_mean\": 0.73,\n      \"keff_eta_max_correlation_range\": [\n        0.62,\n        0.85\n      ],\n      \"VIF_keff\": 2.14,\n      \"confound_free_conditions_count\": 1,\n      \"confound_free_condition_keff_p\": 0.032,\n      \"confound_free_condition_keff_beta\": 0.41\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 1: K_eff Residualized Regression — 15 Models, 455 Panels\",\n        \"columns\": [\n          \"Dataset\",\n          \"Attack\",\n          \"β_ηmax\",\n          \"p_ηmax\",\n          \"β_Keff_resid\",\n          \"p_Keff_resid\",\n          \"R²\",\n          \"K_eff-ηmax r\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            \"sycophancy\",\n            \"0.82\",\n            \"<0.001\",\n            \"0.18\",\n            \"0.147\",\n            \"0.41\",\n            \"0.78\"\n          ],\n          [\n            \"MMLU\",\n            \"score_manip\",\n            \"0.55\",\n            \"<0.001\",\n            \"0.39\",\n            \"0.021\",\n            \"0.36\",\n            \"0.68\"\n          ],\n          [\n            \"MMLU\",\n            \"position\",\n            \"0.71\",\n            \"<0.001\",\n            \"0.24\",\n            \"0.089\",\n            \"0.39\",\n            \"0.75\"\n          ],\n          [\n            \"MMLU\",\n            \"verbosity\",\n            \"0.88\",\n            \"<0.001\",\n            \"0.09\",\n            \"0.511\",\n            \"0.42\",\n            \"0.81\"\n          ],\n          [\n            \"MMLU\",\n            \"authority\",\n            \"0.79\",\n            \"<0.001\",\n            \"0.15\",\n            \"0.218\",\n            \"0.37\",\n            \"0.76\"\n          ],\n          [\n            \"MMLU\",\n            \"few_shot_hijack\",\n            \"0.64\",\n            \"0.002\",\n            \"0.31\",\n            \"0.043\",\n            \"0.33\",\n            \"0.70\"\n          ],\n          [\n            \"ARC\",\n            \"sycophancy\",\n            \"0.85\",\n            \"<0.001\",\n            \"0.12\",\n            \"0.341\",\n            \"0.43\",\n            \"0.79\"\n          ],\n          [\n            \"ARC\",\n            \"score_manip\",\n            \"0.48\",\n            \"0.003\",\n            \"0.41\",\n            \"0.032\",\n            \"0.35\",\n            \"0.35\"\n          ],\n          [\n            \"ARC\",\n            \"position\",\n            \"0.73\",\n            \"<0.001\",\n            \"0.22\",\n            \"0.102\",\n            \"0.38\",\n            \"0.74\"\n          ],\n          [\n            \"ARC\",\n            \"verbosity\",\n            \"0.91\",\n            \"<0.001\",\n            \"0.06\",\n            \"0.649\",\n            \"0.44\",\n            \"0.82\"\n          ],\n          [\n            \"ARC\",\n            \"authority\",\n            \"0.76\",\n            \"<0.001\",\n            \"0.19\",\n            \"0.157\",\n            \"0.36\",\n            \"0.77\"\n          ],\n          [\n            \"ARC\",\n            \"few_shot_hijack\",\n            \"0.59\",\n            \"0.004\",\n            \"0.28\",\n            \"0.071\",\n            \"0.32\",\n            \"0.72\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 2: Model Pool Summary — 15 Models\",\n        \"columns\": [\n          \"Model\",\n          \"Family\",\n          \"Size\",\n          \"Tier\",\n          \"Mean η (6 attacks)\",\n          \"Clean ACC\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen2.5-7B\",\n            \"Qwen\",\n            \"7B\",\n            \"small\",\n            \"0.38\",\n            \"0.61\"\n          ],\n          [\n            \"Qwen2.5-14B\",\n            \"Qwen\",\n            \"14B\",\n            \"medium\",\n            \"0.22\",\n            \"0.74\"\n          ],\n          [\n            \"Qwen2.5-72B\",\n            \"Qwen\",\n            \"72B\",\n            \"large\",\n            \"0.11\",\n            \"0.83\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            \"Llama\",\n            \"8B\",\n            \"small\",\n            \"0.41\",\n            \"0.58\"\n          ],\n          [\n            \"Llama-3.1-70B\",\n            \"Llama\",\n            \"70B\",\n            \"large\",\n            \"0.14\",\n            \"0.80\"\n          ],\n          [\n            \"Mistral-7B\",\n            \"Mistral\",\n            \"7B\",\n            \"small\",\n            \"0.44\",\n            \"0.55\"\n          ],\n          [\n            \"Mistral-Nemo-12B\",\n            \"Mistral\",\n            \"12B\",\n            \"medium\",\n            \"0.27\",\n            \"0.69\"\n          ],\n          [\n            \"Phi-3-mini\",\n            \"Microsoft\",\n            \"3.8B\",\n            \"small\",\n            \"0.49\",\n            \"0.52\"\n          ],\n          [\n            \"Phi-3-medium\",\n            \"Microsoft\",\n            \"14B\",\n            \"medium\",\n            \"0.25\",\n            \"0.71\"\n          ],\n          [\n            \"Gemma-2-9B\",\n            \"Google\",\n            \"9B\",\n            \"small\",\n            \"0.36\",\n            \"0.63\"\n          ],\n          [\n            \"GPT-4o-mini\",\n            \"OpenAI\",\n            \"API\",\n            \"medium\",\n            \"0.19\",\n            \"0.76\"\n          ],\n          [\n            \"GPT-4o\",\n            \"OpenAI\",\n            \"API\",\n            \"large\",\n            \"0.08\",\n            \"0.87\"\n          ],\n          [\n            \"GPT-4.1\",\n            \"OpenAI\",\n            \"API\",\n            \"large\",\n            \"0.07\",\n            \"0.89\"\n          ],\n          [\n            \"GPT-4.1-mini\",\n            \"OpenAI\",\n            \"API\",\n            \"medium\",\n            \"0.16\",\n            \"0.78\"\n          ],\n          [\n            \"Claude-3.5-Haiku\",\n            \"Anthropic\",\n            \"API\",\n            \"medium\",\n            \"0.18\",\n            \"0.77\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"核心 diversity trap framing 受到致命打击。K_eff residualized 显著率从期望的 8/12 降至 4/12，且这 4 个中有 2 个 p 值在 0.02-0.04 之间（经 FDR 校正后可能变 NS）。 仅 1 个 confound-free condition 意味着 residualization 的可信度依赖于线性假设—— reviewer 可以合理质疑 \\\"你的 K_eff effect 只是 nonlinear η_max effect 的残余\\\"。 η_max 9/12 显著是稳健的，weakest-link 叙事成立，但这是预期结果不是新发现。 ΔR² = 0.04 使得 \\\"dual vulnerability driver\\\" 的 framing 难以为继——第二个 driver 解释力不到 4%。需要 reframe 为 η_max-dominant 故事。\\n\\n\\n15 模型涵盖 3 个 capability tier（small 7-8B、medium 13-14B、large 70B+ 及 API）， tier 跨度增大导致 K_eff 与 η_max 的 confound 加剧（r≈0.73）。高 K_eff panel 几乎 必然混入弱模型，低 K_eff panel 则趋于同质强模型。Residualization 后 K_eff 仅在 4/12 conditions 保持显著——恰好是 transferable attack（score_manipulation, position_bias） 且 η_max 方差本身较大的条件。其余 8 conditions 中 K_eff 的 partial effect 被 η_max 吸收殆尽。η_max 维持 9/12 显著，证明 weakest-link 仍是 dominant driver。 ΔR² 仅 0.04 意味着 K_eff 在 η_max 之上的增量解释力微乎其微。 仅 1 个 confound-free condition（arc×score_manipulation, r≈0.35）中 K_eff 勉强显著 （p=0.032），但单一 condition 无法支撑核心 claim。\\n\"\n  },\n  {\n    \"name\": \"Attack Type Expansion\",\n    \"description\": \"新增 few-shot hijacking、persona manipulation、instruction override 三种攻击类型， 在 15 模型 455 panel 上运行，产生 6 个新 conditions（2 datasets × 3 new attacks）。\\n\",\n    \"results\": {\n      \"new_conditions\": 6,\n      \"keff_resid_sig_new\": 2,\n      \"keff_resid_nonsig_new\": 4,\n      \"eta_max_sig_new\": 5,\n      \"keff_direction_positive_new\": 4,\n      \"keff_direction_negative_new\": 1,\n      \"keff_direction_near_zero_new\": 1,\n      \"mean_R2_new_conditions\": 0.31,\n      \"combined_keff_resid_sig_18\": 6,\n      \"combined_eta_max_sig_18\": 14\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 3: New Attack Types — K_eff Residualized Results\",\n        \"columns\": [\n          \"Dataset\",\n          \"Attack\",\n          \"β_ηmax\",\n          \"p_ηmax\",\n          \"β_Keff_resid\",\n          \"p_Keff_resid\",\n          \"R²\",\n          \"Direction\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            \"few_shot_hijack\",\n            \"0.64\",\n            \"0.002\",\n            \"0.31\",\n            \"0.043\",\n            \"0.33\",\n            \"positive\"\n          ],\n          [\n            \"MMLU\",\n            \"persona_manip\",\n            \"0.91\",\n            \"<0.001\",\n            \"0.05\",\n            \"0.724\",\n            \"0.45\",\n            \"near-zero\"\n          ],\n          [\n            \"MMLU\",\n            \"instruct_override\",\n            \"0.58\",\n            \"0.005\",\n            \"0.34\",\n            \"0.038\",\n            \"0.31\",\n            \"positive\"\n          ],\n          [\n            \"ARC\",\n            \"few_shot_hijack\",\n            \"0.59\",\n            \"0.004\",\n            \"0.28\",\n            \"0.071\",\n            \"0.32\",\n            \"positive\"\n          ],\n          [\n            \"ARC\",\n            \"persona_manip\",\n            \"0.87\",\n            \"<0.001\",\n            \"-0.12\",\n            \"0.389\",\n            \"0.41\",\n            \"negative\"\n          ],\n          [\n            \"ARC\",\n            \"instruct_override\",\n            \"0.62\",\n            \"0.003\",\n            \"0.26\",\n            \"0.088\",\n            \"0.30\",\n            \"positive\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"攻击扩展没有挽救 K_eff 叙事。新增条件中 K_eff 显著率 2/6，其中 persona manipulation 出现方向反转（K_eff 负但 NS）——这与 \\\"diversity hurts\\\" 不一致，虽然不显著但给 reviewer 提供了攻击点。合计 18 conditions 中 K_eff 6/18 显著，低于 33% 的 chance expected 阈值，FDR 校正后预计降至 4-5/18。η_max 14/18 显著，进一步巩固 weakest-link 的 dominant 地位。新攻击类型未发现任何 K_eff dominates η_max 的条件。\\n\\n\\n新攻击类型中 few-shot hijacking 和 instruction override 是 transferable attack， K_eff 在这些条件下可能保持微弱正向显著（p≈0.03-0.04）；persona manipulation 则高度 依赖模型特定 persona alignment 训练，η_max 几乎完全解释方差。整体上新增 6 conditions 中仅 2 个 K_eff 显著，且 1 个条件 K_eff 方向为负（persona manipulation on ARC）， 方向不一致削弱了 \\\"diversity universally hurts\\\" 的叙事。18 条件合计 K_eff 6/18 ≈ 33% 显著率——FDR 校正后可能进一步缩减至 4-5/18，属于 \\\"suggestive but not robust\\\" 水平。\\n\"\n  },\n  {\n    \"name\": \"Random-Fault BFT Contrast Simulation\",\n    \"description\": \"模拟随机故障场景：每个 judge 以概率 η_j 独立犯错，majority vote 决策。 比较 K_eff 在 random-fault vs adaptive 两种 regime 下的 β 和显著性。\\n\",\n    \"results\": {\n      \"RF_keff_sig_positive\": 10,\n      \"RF_keff_nonsig\": 2,\n      \"RF_eta_max_sig\": 11,\n      \"RF_mean_beta_keff\": 0.42,\n      \"adaptive_mean_beta_keff\": 0.38,\n      \"BFT_RF_beta_ratio\": 0.91,\n      \"RF_mean_R2\": 0.62,\n      \"adaptive_mean_R2\": 0.38,\n      \"delta_R2_RF_vs_adaptive\": 0.24,\n      \"RF_keff_direction\": \"positive (same as adaptive)\",\n      \"regime_contrast_p_interaction\": 0.217\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 4: BFT Regime Contrast — K_eff β Comparison\",\n        \"columns\": [\n          \"Dataset\",\n          \"Attack\",\n          \"β_Keff (Adaptive)\",\n          \"p (Adaptive)\",\n          \"β_Keff (RF)\",\n          \"p (RF)\",\n          \"β Ratio\",\n          \"Interaction p\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            \"sycophancy\",\n            \"0.18\",\n            \"0.147\",\n            \"0.21\",\n            \"0.024\",\n            \"1.17\",\n            \"0.682\"\n          ],\n          [\n            \"MMLU\",\n            \"score_manip\",\n            \"0.39\",\n            \"0.021\",\n            \"0.44\",\n            \"0.003\",\n            \"1.13\",\n            \"0.541\"\n          ],\n          [\n            \"MMLU\",\n            \"position\",\n            \"0.24\",\n            \"0.089\",\n            \"0.28\",\n            \"0.011\",\n            \"1.17\",\n            \"0.614\"\n          ],\n          [\n            \"MMLU\",\n            \"verbosity\",\n            \"0.09\",\n            \"0.511\",\n            \"0.15\",\n            \"0.108\",\n            \"1.67\",\n            \"0.398\"\n          ],\n          [\n            \"MMLU\",\n            \"authority\",\n            \"0.15\",\n            \"0.218\",\n            \"0.19\",\n            \"0.047\",\n            \"1.27\",\n            \"0.583\"\n          ],\n          [\n            \"MMLU\",\n            \"few_shot_hijack\",\n            \"0.31\",\n            \"0.043\",\n            \"0.35\",\n            \"0.008\",\n            \"1.13\",\n            \"0.617\"\n          ],\n          [\n            \"ARC\",\n            \"sycophancy\",\n            \"0.12\",\n            \"0.341\",\n            \"0.16\",\n            \"0.072\",\n            \"1.33\",\n            \"0.521\"\n          ],\n          [\n            \"ARC\",\n            \"score_manip\",\n            \"0.41\",\n            \"0.032\",\n            \"0.48\",\n            \"0.001\",\n            \"1.17\",\n            \"0.434\"\n          ],\n          [\n            \"ARC\",\n            \"position\",\n            \"0.22\",\n            \"0.102\",\n            \"0.27\",\n            \"0.015\",\n            \"1.23\",\n            \"0.548\"\n          ],\n          [\n            \"ARC\",\n            \"verbosity\",\n            \"0.06\",\n            \"0.649\",\n            \"0.11\",\n            \"0.198\",\n            \"1.83\",\n            \"0.412\"\n          ],\n          [\n            \"ARC\",\n            \"authority\",\n            \"0.19\",\n            \"0.157\",\n            \"0.22\",\n            \"0.038\",\n            \"1.16\",\n            \"0.601\"\n          ],\n          [\n            \"ARC\",\n            \"few_shot_hijack\",\n            \"0.28\",\n            \"0.071\",\n            \"0.33\",\n            \"0.009\",\n            \"1.18\",\n            \"0.547\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 5: R² Comparison Across Regimes\",\n        \"columns\": [\n          \"Dataset\",\n          \"Attack\",\n          \"R² (Adaptive)\",\n          \"R² (RF)\",\n          \"ΔR²\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            \"sycophancy\",\n            \"0.41\",\n            \"0.64\",\n            \"0.23\"\n          ],\n          [\n            \"MMLU\",\n            \"score_manip\",\n            \"0.36\",\n            \"0.58\",\n            \"0.22\"\n          ],\n          [\n            \"MMLU\",\n            \"position\",\n            \"0.39\",\n            \"0.61\",\n            \"0.22\"\n          ],\n          [\n            \"MMLU\",\n            \"verbosity\",\n            \"0.42\",\n            \"0.67\",\n            \"0.25\"\n          ],\n          [\n            \"MMLU\",\n            \"authority\",\n            \"0.37\",\n            \"0.59\",\n            \"0.22\"\n          ],\n          [\n            \"MMLU\",\n            \"few_shot_hijack\",\n            \"0.33\",\n            \"0.55\",\n            \"0.22\"\n          ],\n          [\n            \"ARC\",\n            \"sycophancy\",\n            \"0.43\",\n            \"0.69\",\n            \"0.26\"\n          ],\n          [\n            \"ARC\",\n            \"score_manip\",\n            \"0.35\",\n            \"0.57\",\n            \"0.22\"\n          ],\n          [\n            \"ARC\",\n            \"position\",\n            \"0.38\",\n            \"0.62\",\n            \"0.24\"\n          ],\n          [\n            \"ARC\",\n            \"verbosity\",\n            \"0.44\",\n            \"0.71\",\n            \"0.27\"\n          ],\n          [\n            \"ARC\",\n            \"authority\",\n            \"0.36\",\n            \"0.60\",\n            \"0.24\"\n          ],\n          [\n            \"ARC\",\n            \"few_shot_hijack\",\n            \"0.32\",\n            \"0.53\",\n            \"0.21\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"BFT contrast 实验是 GO/NO-GO gate，结果为 NO-GO。K_eff 在 RF 下不仅没有变负 （diversity helps），反而保持正向且更显著（10/12 vs 4/12 residualized adaptive）。 这意味着 K_eff 的正向效应不是 adaptive adversary 特有的——而是 panel composition 的基本属性（高 diversity → 混入弱模型 → 高 ASR），RF 和 adaptive 下都成立。 BFT reversal mechanism 的核心前提被否定：我们无法证明 diversity 在 RF 下保护但在 adaptive 下有害。唯一可挽救的发现是 ΔR² = 0.24，说明 adaptive attacker 引入了 strategic variance 使得 panel composition 的预测力下降——但这是一个弱得多的 claim， 不足以支撑 Claim 2 作为独立贡献。BFT 应降级为 Discussion 中的 \\\"open question\\\"。\\n\\n\\nBFT contrast 的核心预期是 K_eff 在 RF 下显著正向（diversity helps under random faults） 但在 adaptive 下 NS 或反转。Worst 档下实际观察到：K_eff 在 RF 下同样正向显著 （10/12），与 adaptive 下方向一致。原因：在 RF 模拟中 η_j 直接决定 judge 犯错率， 高 K_eff panel 仍然混入高 η_j 的弱模型，majority vote 下弱模型拉低整体正确率。 因此 K_eff 正向不是 \\\"diversity 主动有害\\\" 而是 \\\"diversity 引入弱模型\\\" 的统计反映—— 这在 RF 和 adaptive 两种 regime 下都成立。β ratio 0.91 表明两种 regime 下 K_eff 的效应量几乎相同，regime interaction term NS (p=0.217)。唯一的 regime 差异是 R²： RF 下 R²=0.62 vs adaptive R²=0.38，ΔR²=0.24——RF 更可预测但这只是因为 RF 没有 strategic variance，不是因为 K_eff 效应不同。BFT reversal mechanism 叙事瓦解。\\n\"\n  },\n  {\n    \"name\": \"Capability-Matched K_eff Validation\",\n    \"description\": \"在同一 capability tier 内（all-small 7-8B 或 all-large 70B+/API）测试 K_eff 是否 仍然显著。如果 tier-matched panel 中 K_eff 消失 → K_eff 效应是 tier-mixing artifact。\\n\",\n    \"results\": {\n      \"tiers_tested\": 3,\n      \"panels_small_tier\": 10,\n      \"panels_medium_tier\": 10,\n      \"panels_large_tier\": 10,\n      \"small_tier_keff_sig\": 0,\n      \"medium_tier_keff_sig\": 1,\n      \"large_tier_keff_sig\": 0,\n      \"total_capability_matched_keff_sig\": 1,\n      \"total_conditions_tested\": 6,\n      \"eta_max_variance_within_tier\": 0.008,\n      \"keff_eta_max_correlation_within_tier\": 0.22,\n      \"within_tier_keff_p_range\": [\n        0.041,\n        0.891\n      ],\n      \"within_tier_mean_R2\": 0.12\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 6: Capability-Matched K_eff Analysis\",\n        \"columns\": [\n          \"Tier\",\n          \"N Panels\",\n          \"Condition\",\n          \"β_Keff\",\n          \"p_Keff\",\n          \"R²\",\n          \"η_max Var\"\n        ],\n        \"rows\": [\n          [\n            \"Small (7-8B)\",\n            \"10\",\n            \"MMLU×sycophancy\",\n            \"0.08\",\n            \"0.721\",\n            \"0.09\",\n            \"0.007\"\n          ],\n          [\n            \"Small (7-8B)\",\n            \"10\",\n            \"ARC×score_manip\",\n            \"0.14\",\n            \"0.548\",\n            \"0.11\",\n            \"0.008\"\n          ],\n          [\n            \"Medium (12-14B+API-mini)\",\n            \"10\",\n            \"MMLU×sycophancy\",\n            \"0.11\",\n            \"0.612\",\n            \"0.10\",\n            \"0.009\"\n          ],\n          [\n            \"Medium (12-14B+API-mini)\",\n            \"10\",\n            \"ARC×score_manip\",\n            \"0.29\",\n            \"0.041\",\n            \"0.18\",\n            \"0.011\"\n          ],\n          [\n            \"Large (70B+API)\",\n            \"10\",\n            \"MMLU×sycophancy\",\n            \"0.06\",\n            \"0.891\",\n            \"0.07\",\n            \"0.004\"\n          ],\n          [\n            \"Large (70B+API)\",\n            \"10\",\n            \"ARC×score_manip\",\n            \"0.09\",\n            \"0.684\",\n            \"0.08\",\n            \"0.005\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是对 diversity trap framing 的最强反驳。Capability-matched 0-1/6 显著意味着 K_eff 的独立效应在控制 capability 后基本消失。Residualized analysis 在全池中仍然 显著 4/12 的原因是：residualization 假设线性关系，但 K_eff-η_max confound 可能是 非线性的（阶梯型：跨 tier → K_eff 骤升 + η_max 骤升），线性 residualization 无法完全去除。Capability-matched 是更强的 confound control（分层而非回归调整）， 结果否定了 K_eff 的独立效应。需要在论文中诚实报告这个 null result，将 K_eff 从 core claim 降级为 \\\"exploratory, potentially confounded\\\"。\\n\\n\\nCapability-matched 是 worst 档的致命实验。同 tier 内模型能力相近，η_max 方差极小 （约 0.008 vs 全池 0.045），消除了 tier-mixing confound。结果：K_eff 仅在 1/6 条件下显著（medium tier × score_manipulation, p=0.041，FDR 后可能 NS），其余 5/6 全部 NS。这直接证明 K_eff 的表面效应是 tier-mixing 的统计幻象：当你在全池抽 panel， 高 K_eff panel 跨 tier 抽样（混入 7B 和 70B），低 K_eff panel 同 tier 抽样—— K_eff 与 η_max 的相关性是 tier-mixing 的副产品，不是因果关系。 每个 tier 仅 C(5,3)=10 个 panel，样本量不足以检测小效应，但即便如此 η_max 方差 消失也说明在能力控制后 K_eff 没有独立的预测力。Reviewer 可以合理论证： \\\"K_eff effect = capability heterogeneity effect, not diversity per se\\\"。\\n\"\n  },\n  {\n    \"name\": \"Two-Stage Panel Design Algorithm Benchmark\",\n    \"description\": \"Robustness-first 两阶段选择：(1) 筛选 η ≤ threshold 的 judge，(2) 在剩余中最大化 K_eff。 与 5 个 baseline（random, max-K_eff, strongest-K, min-η, diversity-only）对比。\\n\",\n    \"results\": {\n      \"baselines_tested\": 5,\n      \"two_stage_vs_strongest_K_ASR_reduction_pct\": 2.3,\n      \"two_stage_vs_strongest_K_p\": 0.312,\n      \"two_stage_vs_random_ASR_reduction_pct\": 18.4,\n      \"two_stage_vs_max_keff_ASR_reduction_pct\": 31.2,\n      \"min_eta_dominates_conditions\": 4,\n      \"two_stage_dominates_conditions\": 1,\n      \"strongest_K_dominates_conditions\": 1,\n      \"two_stage_ASR_reduction_pct\": 3.1,\n      \"two_stage_vs_strongest_K_stat_sig\": false,\n      \"optimal_eta_threshold\": 0.15\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 7: Panel Selection Strategy Comparison (mean ASR across 6 attacks)\",\n        \"columns\": [\n          \"Strategy\",\n          \"Mean ASR\",\n          \"vs Strongest-K Δ%\",\n          \"p vs Strongest-K\",\n          \"Wins (6 conditions)\"\n        ],\n        \"rows\": [\n          [\n            \"Random\",\n            \"0.284\",\n            \"+21.5%\",\n            \"<0.001\",\n            \"0\"\n          ],\n          [\n            \"Max-K_eff\",\n            \"0.341\",\n            \"+45.9%\",\n            \"<0.001\",\n            \"0\"\n          ],\n          [\n            \"Diversity-Only\",\n            \"0.312\",\n            \"+33.5%\",\n            \"<0.001\",\n            \"0\"\n          ],\n          [\n            \"Min-η_max\",\n            \"0.229\",\n            \"-2.1%\",\n            \"0.478\",\n            \"4\"\n          ],\n          [\n            \"Strongest-K\",\n            \"0.234\",\n            \"—\",\n            \"—\",\n            \"1\"\n          ],\n          [\n            \"Two-Stage\",\n            \"0.227\",\n            \"-3.1%\",\n            \"0.312\",\n            \"1\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 8: Two-Stage vs Strongest-K Per Condition\",\n        \"columns\": [\n          \"Condition\",\n          \"ASR (Two-Stage)\",\n          \"ASR (Strongest-K)\",\n          \"Δ%\",\n          \"p\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU×sycophancy\",\n            \"0.211\",\n            \"0.219\",\n            \"-3.7%\",\n            \"0.284\"\n          ],\n          [\n            \"MMLU×score_manip\",\n            \"0.198\",\n            \"0.207\",\n            \"-4.3%\",\n            \"0.198\"\n          ],\n          [\n            \"MMLU×position\",\n            \"0.237\",\n            \"0.241\",\n            \"-1.7%\",\n            \"0.641\"\n          ],\n          [\n            \"ARC×sycophancy\",\n            \"0.241\",\n            \"0.248\",\n            \"-2.8%\",\n            \"0.352\"\n          ],\n          [\n            \"ARC×score_manip\",\n            \"0.185\",\n            \"0.194\",\n            \"-4.6%\",\n            \"0.187\"\n          ],\n          [\n            \"ARC×position\",\n            \"0.249\",\n            \"0.253\",\n            \"-1.6%\",\n            \"0.689\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Two-stage ≤5% improvement over strongest-K 且无统计显著性。这与 worst 档的预期一致： 如果 K_eff 没有独立效应（plan_004），那么在 robustness-screened pool 中最大化 K_eff 不应带来额外收益。Max-K_eff 是最差策略（ASR 最高）这一发现仍然有价值—— 它警告不要盲目追求 diversity——但这只需 η_max 解释就够了（高 K_eff = 混入弱模型 = 高 ASR）， 不需要 \\\"diversity independently hurts\\\" 的 claim。实践建议简化为 \\\"pick the most robust judges, ignore diversity\\\"，这比 two-stage 更简单但可能过于平凡。\\n\\n\\n在 worst 档下 K_eff 的独立效应已消失（plan_004 显示 capability-matched 后 K_eff NS）， 因此两阶段的第二步（maximize K_eff among screened judges）几乎不提供额外收益。 Robustness screening（step 1）本身有效——排除 η > threshold 的弱模型大幅降低 ASR—— 但这与简单的 strongest-K 策略效果相同。Two-stage 与 strongest-K 的差异仅 2.3% （p=0.312, NS），因为 screening 后剩余模型能力相近，K_eff 的变异范围收窄。 min_eta（不考虑 diversity）在 4/6 conditions 表现最佳，进一步说明 panel 安全由 最弱 judge 决定。Two-stage 的存在意义被削弱：如果第二步（diversity）没用， 算法退化为 \\\"just pick the strongest K models\\\"。\\n\"\n  },\n  {\n    \"name\": \"Per-Judge ASR Concentration Analysis\",\n    \"description\": \"对每个 panel × attack，计算各 judge 的 ASR 分布，用 Gini 系数和 entropy 量化 adaptive adversary 的 targeting 集中度。高 Gini = adversary 集中攻击特定 judge。\\n\",\n    \"results\": {\n      \"mean_gini_adaptive\": 0.38,\n      \"mean_gini_random_fault\": 0.12,\n      \"gini_diff_p\": \"<0.001\",\n      \"mean_entropy_adaptive\": 2.41,\n      \"mean_entropy_random_fault\": 3.22,\n      \"entropy_diff_p\": \"<0.001\",\n      \"gini_keff_correlation\": 0.21,\n      \"gini_keff_p\": 0.089,\n      \"gini_eta_max_correlation\": 0.67,\n      \"gini_eta_max_p\": \"<0.001\",\n      \"high_gini_panels_pct\": 34,\n      \"targeting_consistent_across_attacks\": false\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 9: ASR Concentration Statistics\",\n        \"columns\": [\n          \"Metric\",\n          \"Adaptive (mean)\",\n          \"Adaptive (SD)\",\n          \"RF (mean)\",\n          \"RF (SD)\",\n          \"Diff p\"\n        ],\n        \"rows\": [\n          [\n            \"Gini\",\n            \"0.38\",\n            \"0.14\",\n            \"0.12\",\n            \"0.05\",\n            \"<0.001\"\n          ],\n          [\n            \"Entropy (bits)\",\n            \"2.41\",\n            \"0.52\",\n            \"3.22\",\n            \"0.31\",\n            \"<0.001\"\n          ],\n          [\n            \"Max single-judge share\",\n            \"0.51\",\n            \"0.12\",\n            \"0.38\",\n            \"0.06\",\n            \"<0.001\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 10: Gini Coefficient Correlations\",\n        \"columns\": [\n          \"Predictor\",\n          \"r with Gini\",\n          \"p\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"η_max\",\n            \"0.67\",\n            \"<0.001\",\n            \"Targeting tracks individual weakness\"\n          ],\n          [\n            \"K_eff\",\n            \"0.21\",\n            \"0.089\",\n            \"Weak/NS association with diversity\"\n          ],\n          [\n            \"Panel size\",\n            \"0.04\",\n            \"0.814\",\n            \"No panel size effect\"\n          ],\n          [\n            \"Mean capability\",\n            \"-0.58\",\n            \"<0.001\",\n            \"Stronger panels → less concentrated targeting\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Per-judge 浓度分析提供了 adaptive vs RF 差异的直接证据——这是一个有用的 finding， 可作为 paper 的 empirical contribution。但分析同时削弱了 diversity trap：targeting 集中度由 η_max（而非 K_eff）解释。Adaptive adversary 攻击最弱 judge，不是利用 diverse attack surface。这与 reframed narrative（η_max dominant, diversity irrelevant） 一致。Gini 分析可以移入 \\\"Adaptive Adversary Behavior\\\" 子节，作为 η_max dominance 的补充证据，而非 diversity trap 的支持。\\n\\n\\nAdaptive adversary 确实展现 targeting 行为（Gini 0.38 vs RF 0.12），但集中度 中等而非极端。关键问题：Gini 与 η_max 高度相关（r=0.67）但与 K_eff 弱相关（r=0.21, NS）。 这意味着 targeting 主要针对最弱 judge（η_max 高的 panel 中弱 judge 更容易被攻克）， 而不是利用 diversity 创造的 diverse attack surface。如果 K_eff 独立驱动 targeting， 我们预期 Gini 与 K_eff 显著相关（高 diversity → adversary 有更多独立漏洞可攻击 → 攻击更集中于特定 judge），但 p=0.089 未达显著。此外 targeting 不跨攻击一致—— 同一 panel 在不同攻击下被 target 的 judge 不同，进一步削弱 \\\"structural diversity creates systematic exploitable surface\\\" 的论点。\\n\"\n  },\n  {\n    \"name\": \"Diversity-Capability Tradeoff Visualization\",\n    \"description\": \"绘制 K_eff vs η_max across 455 panels，拟合 tradeoff curve，Pareto frontier analysis， 按 tier 分层。\\n\",\n    \"results\": {\n      \"keff_eta_max_pearson_r\": 0.73,\n      \"keff_eta_max_spearman_rho\": 0.71,\n      \"tradeoff_curve_R2\": 0.53,\n      \"pareto_frontier_size\": 12,\n      \"pareto_pct_from_large_tier\": 83,\n      \"pareto_pct_from_mixed_tier\": 17,\n      \"pareto_pct_from_small_tier\": 0,\n      \"pareto_panels_mean_keff\": 1.82,\n      \"pareto_panels_mean_eta_max\": 0.09,\n      \"non_pareto_gap_ASR\": 0.11\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 11: Pareto Frontier Panel Characteristics\",\n        \"columns\": [\n          \"Panel ID\",\n          \"Models\",\n          \"K_eff\",\n          \"η_max\",\n          \"Mean ASR\",\n          \"Tier Composition\"\n        ],\n        \"rows\": [\n          [\n            \"P_012\",\n            \"GPT-4.1 / GPT-4o / Qwen72B\",\n            \"1.91\",\n            \"0.08\",\n            \"0.142\",\n            \"all-large\"\n          ],\n          [\n            \"P_034\",\n            \"GPT-4.1 / Llama70B / GPT-4o\",\n            \"2.14\",\n            \"0.09\",\n            \"0.151\",\n            \"all-large\"\n          ],\n          [\n            \"P_087\",\n            \"GPT-4.1 / GPT-4o / Claude-Haiku\",\n            \"1.72\",\n            \"0.07\",\n            \"0.138\",\n            \"large+medium\"\n          ],\n          [\n            \"P_156\",\n            \"GPT-4o / Qwen72B / Llama70B\",\n            \"2.31\",\n            \"0.11\",\n            \"0.163\",\n            \"all-large\"\n          ],\n          [\n            \"P_201\",\n            \"GPT-4.1 / GPT-4.1m / GPT-4o\",\n            \"1.45\",\n            \"0.07\",\n            \"0.131\",\n            \"all-large\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Tradeoff visualization 是一个 clean methodological contribution，无论 K_eff 是否有 独立效应都有价值。它展示了当前 LLM 生态中 panel design 的结构约束：diversity 和 robustness 不是独立可优化的维度。但在 worst 档下，这更多被解读为 confound 的可视化 证据而非独立发现。可在论文中保留为 Fig 2 或 Fig 3，作为 \\\"understanding the evaluation landscape\\\" 的贡献。\\n\\n\\nTradeoff 可视化清晰展示了 K_eff 与 η_max 的结构性关联：r=0.73，Pareto frontier 几乎完全由 large-tier panel 占据（83%），因为只有在全部选择强模型时才能同时获得 低 η_max 和中等 K_eff。Small-tier panel 全部位于 Pareto frontier 之下。 这个 visualization 本身有价值（展示了 evaluation panel design 的结构约束）， 但在 worst 档下它更多地支持了 \\\"K_eff effect is confound\\\" 的叙事：tradeoff 不是 独立的两个维度的 tension，而是 tier-mixing 的必然结果。Pareto frontier 上的 panel 基本就是 \\\"all strong models\\\"，equivalent to strongest-K 策略。\\n\"\n  },\n  {\n    \"name\": \"Panel Size Sensitivity Analysis\",\n    \"description\": \"测试 K=3,5,7,9 不同 panel size 下 η_max 与 K_eff 的相对重要性是否变化。\\n\",\n    \"results\": {\n      \"K3_panels\": 455,\n      \"K5_panels\": 3003,\n      \"K7_panels\": 6435,\n      \"K9_panels\": 5005,\n      \"K3_eta_max_sig_ratio\": 0.75,\n      \"K5_eta_max_sig_ratio\": 0.83,\n      \"K7_eta_max_sig_ratio\": 0.92,\n      \"K9_eta_max_sig_ratio\": 0.92,\n      \"K3_keff_resid_sig_ratio\": 0.33,\n      \"K5_keff_resid_sig_ratio\": 0.25,\n      \"K7_keff_resid_sig_ratio\": 0.17,\n      \"K9_keff_resid_sig_ratio\": 0.08,\n      \"keff_effect_trend_with_K\": \"monotonically decreasing\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 12: Panel Size Sensitivity — Significance Ratios\",\n        \"columns\": [\n          \"K\",\n          \"N Panels\",\n          \"η_max sig ratio\",\n          \"K_eff resid sig ratio\",\n          \"Mean R²\",\n          \"K_eff-η_max r\"\n        ],\n        \"rows\": [\n          [\n            \"3\",\n            \"455\",\n            \"0.75\",\n            \"0.33\",\n            \"0.38\",\n            \"0.73\"\n          ],\n          [\n            \"5\",\n            \"3003\",\n            \"0.83\",\n            \"0.25\",\n            \"0.41\",\n            \"0.68\"\n          ],\n          [\n            \"7\",\n            \"6435\",\n            \"0.92\",\n            \"0.17\",\n            \"0.44\",\n            \"0.61\"\n          ],\n          [\n            \"9\",\n            \"5005\",\n            \"0.92\",\n            \"0.08\",\n            \"0.46\",\n            \"0.54\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Panel size 分析揭示 K_eff 效应的 artifactual nature：它在小 panel（K=3）中最强 恰好是 tier-mixing 方差最大的地方。随 K 增大，confound 缓解，K_eff 效应消退。 η_max 的趋势则相反——大 panel 中仍有弱 judge，且 R² 随 K 增大说明 panel composition 的可预测性提高。这是支持 \\\"K_eff is confound\\\" 的又一条证据线。\\n\\n\\nPanel size 增大时 η_max dominance 增强，K_eff effect 递减。原因：K=9 的 panel 包含 9/15 模型，几乎所有 panel 都包含至少一个弱模型，η_max 方差缩小但 level 保持高位。 同时 K_eff 的变异范围也缩小（大 panel 的 K_eff 趋向收敛）。更重要的是，majority vote 在大 panel 中的容错能力提高——但这被 η_max 的 monotonic 效应抵消（一个极弱 judge 的影响在 K=3 中是 catastrophic，在 K=9 中被稀释）。K_eff 的 sig ratio 从 K=3 的 0.33 降至 K=9 的 0.08，表明 K_eff 的表面效应主要在小 panel 中出现（因为 tier-mixing 的方差更大），进一步支持 confound 解释。\\n\"\n  },\n  {\n    \"name\": \"VIF and Multicollinearity Deep Dive\",\n    \"description\": \"对现有回归数据进行全面多重共线性分析：VIF、偏相关、residualized K_eff、 Bonferroni/FDR correction、bootstrap CI、排除极端模型的敏感性分析、beta regression。\\n\",\n    \"results\": {\n      \"VIF_keff_full_model\": 2.14,\n      \"VIF_eta_max_full_model\": 2.14,\n      \"keff_resid_sig_bonferroni_12\": 2,\n      \"keff_resid_sig_fdr_12\": 4,\n      \"keff_resid_sig_bootstrap_95CI_excludes_zero\": 3,\n      \"keff_resid_sig_exclude_extreme_models\": 4,\n      \"keff_resid_sig_exclude_extreme_models_fdr\": 3,\n      \"beta_regression_keff_sig\": 3,\n      \"beta_regression_eta_max_sig\": 10,\n      \"partial_r_keff_given_eta_max\": 0.14,\n      \"partial_r_eta_max_given_keff\": 0.41,\n      \"sensitivity_analyses_convergent\": false,\n      \"keff_resid_sig_range_across_methods\": [\n        2,\n        5\n      ]\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 13: K_eff Residualized Significance Under Different Correction Methods\",\n        \"columns\": [\n          \"Method\",\n          \"K_eff sig count (/12)\",\n          \"η_max sig count (/12)\",\n          \"Notes\"\n        ],\n        \"rows\": [\n          [\n            \"Uncorrected\",\n            \"7\",\n            \"10\",\n            \"Liberal\"\n          ],\n          [\n            \"FDR (BH)\",\n            \"4\",\n            \"9\",\n            \"Standard\"\n          ],\n          [\n            \"Bonferroni\",\n            \"2\",\n            \"8\",\n            \"Conservative\"\n          ],\n          [\n            \"Bootstrap 95% CI\",\n            \"3\",\n            \"9\",\n            \"Non-parametric\"\n          ],\n          [\n            \"Exclude extreme models (FDR)\",\n            \"3\",\n            \"9\",\n            \"Sensitivity\"\n          ],\n          [\n            \"Beta regression (FDR)\",\n            \"3\",\n            \"10\",\n            \"Bounded DV\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 14: Partial Correlations\",\n        \"columns\": [\n          \"Predictor\",\n          \"Partial r (controlling other)\",\n          \"95% CI\",\n          \"p\"\n        ],\n        \"rows\": [\n          [\n            \"K_eff | η_max\",\n            \"0.14\",\n            \"[0.05, 0.23]\",\n            \"0.003\"\n          ],\n          [\n            \"η_max | K_eff\",\n            \"0.41\",\n            \"[0.33, 0.49]\",\n            \"<0.001\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"VIF 分析是 worst 档的核心打击。K_eff 的显著性在 2-5/12 范围内波动，高度依赖 统计方法选择——这是 \\\"researcher degrees of freedom\\\" 问题。Partial r (K_eff | η_max) = 0.14 意味着 K_eff 在控制 η_max 后仅解释 2% 的独特方差（r²=0.02）。相比之下 η_max 的 partial r = 0.41（17% 独特方差）。即使 K_eff 有微弱的独立效应，其实际意义（practical significance）可忽略。论文中需要诚实报告所有方法的结果范围，不能只报最有利的。\\n\\n\\nVIF=2.14 在传统标准下不算严重（<5），但这掩盖了非线性 confound。Bonferroni 最严格， K_eff 降至 2/12 显著；FDR 保持 4/12；bootstrap CI 给出 3/12（因为 bootstrap 在 455 panels 中重复抽样，resampling variance 较大导致 CI 加宽）。排除极端模型 （ACC < 0.5 的 2 个模型）后 K_eff 4/12→3/12（FDR），说明效应部分依赖极端值。 Beta regression（适合 bounded proportion DV）与 OLS 结果不一致——K_eff 仅 3/12 显著（beta regression 对极端值更稳健）。核心问题：不同分析方法给出 2-5/12 的 显著性范围，缺乏收敛性。Reviewer 可以选择最严格的估计（2/12 Bonferroni）argue K_eff 无效应，或选择最宽松的（5/12 FDR without extreme exclusion）argue suggestive。 这种方法敏感性本身就是 \\\"not robust\\\" 的标志。\\n\"\n  },\n  {\n    \"name\": \"Aggregation Rule Comparison\",\n    \"description\": \"在 15 模型 455 panel 上测试 majority vote、threshold voting（unanimity）、 weighted voting、Bayesian aggregation 四种聚合规则下的 K_eff 和 η_max 效应。\\n\",\n    \"results\": {\n      \"majority_keff_resid_sig\": 4,\n      \"majority_eta_max_sig\": 9,\n      \"threshold_keff_resid_sig\": 6,\n      \"threshold_eta_max_sig\": 7,\n      \"weighted_keff_resid_sig\": 2,\n      \"weighted_eta_max_sig\": 10,\n      \"bayesian_keff_resid_sig\": 1,\n      \"bayesian_eta_max_sig\": 5,\n      \"keff_sig_varies_by_aggregation\": true,\n      \"aggregation_dependency_interpretation\": \"K_eff effect is aggregation artifact\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 15: Aggregation Rule × Vulnerability Driver Analysis\",\n        \"columns\": [\n          \"Aggregation\",\n          \"K_eff sig (/12)\",\n          \"η_max sig (/12)\",\n          \"Mean R²\",\n          \"Best Predictor\"\n        ],\n        \"rows\": [\n          [\n            \"Majority Vote\",\n            \"4\",\n            \"9\",\n            \"0.38\",\n            \"η_max\"\n          ],\n          [\n            \"Threshold (Unanimity)\",\n            \"6\",\n            \"7\",\n            \"0.42\",\n            \"mixed\"\n          ],\n          [\n            \"Accuracy-Weighted\",\n            \"2\",\n            \"10\",\n            \"0.45\",\n            \"η_max\"\n          ],\n          [\n            \"Bayesian\",\n            \"1\",\n            \"5\",\n            \"0.29\",\n            \"η_max (weakened)\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 16: Aggregation as Defense — Mean ASR Comparison\",\n        \"columns\": [\n          \"Aggregation\",\n          \"Mean ASR (all panels)\",\n          \"ASR (top-10 panels)\",\n          \"ASR (bottom-10 panels)\",\n          \"Spread\"\n        ],\n        \"rows\": [\n          [\n            \"Majority\",\n            \"0.261\",\n            \"0.142\",\n            \"0.418\",\n            \"0.276\"\n          ],\n          [\n            \"Threshold\",\n            \"0.183\",\n            \"0.098\",\n            \"0.312\",\n            \"0.214\"\n          ],\n          [\n            \"Weighted\",\n            \"0.224\",\n            \"0.121\",\n            \"0.367\",\n            \"0.246\"\n          ],\n          [\n            \"Bayesian\",\n            \"0.198\",\n            \"0.112\",\n            \"0.294\",\n            \"0.182\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Aggregation 分析是 worst 档中最具建设性的发现。虽然它进一步削弱了 K_eff 作为 independent driver 的 claim（aggregation-dependent → possible artifact），但它提供了 实际价值：(a) Bayesian aggregation 作为 defense 的有效性（ASR 均值和方差同时降低）； (b) Threshold voting 最严格但 K_eff 效应最强——不适合 adversarial setting； (c) Accuracy-weighted 是 good middle ground（K_eff 几乎消失，η_max 仍可控）。 可以 reframe 为 practical contribution: \\\"choosing the right aggregation rule matters more than panel diversity composition\\\"。\\n\\n\\n聚合规则分析暴露 K_eff 效应的 aggregation dependency。Threshold voting（unanimity） 下 K_eff 6/12 显著——因为 unanimity 放大了单个 judge 的 veto power，diverse panel 中弱 judge 更可能 veto 正确判断。但这不是 \\\"diversity hurts\\\"，而是 \\\"unanimity amplifies weakest-link effect, and diverse panels have weaker links\\\"。Bayesian aggregation 大幅削弱两个 predictor：η_max 5/12，K_eff 1/12——Bayesian weighting 有效下调了不可靠 judge 的权重，部分 neutralize 了 weakest-link 效应。 Weighted voting 下 K_eff 几乎消失（2/12），因为 accuracy-based weights 自动 降权弱模型。核心问题：K_eff 的显著性从 1/12（Bayesian）到 6/12（threshold）—— 如果 K_eff 是真正的 structural vulnerability driver，它不应该如此依赖聚合规则。 这种依赖性暗示 K_eff 效应实际上是特定聚合规则对弱 judge 处理方式的 artifact。\\n\"\n  },\n  {\n    \"name\": \"Open-Ended Generation Benchmark\",\n    \"description\": \"在 MT-Bench 或 AlpacaEval 风格的开放式生成任务上运行攻击实验， 验证 MCQ findings 是否推广到 open-ended evaluation。\\n\",\n    \"results\": {\n      \"benchmark\": \"MT-Bench (adapted)\",\n      \"n_conditions\": 4,\n      \"keff_resid_sig_positive\": 0,\n      \"keff_resid_sig_negative\": 1,\n      \"keff_resid_nonsig\": 3,\n      \"eta_max_sig\": 4,\n      \"keff_direction_inconsistent_with_MCQ\": true,\n      \"open_ended_mean_ASR\": 0.34,\n      \"MCQ_mean_ASR\": 0.26,\n      \"eta_max_dominance_ratio_open\": 0.91\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 17: Open-Ended Task Results\",\n        \"columns\": [\n          \"Task Subset\",\n          \"Attack\",\n          \"β_ηmax\",\n          \"p_ηmax\",\n          \"β_Keff_resid\",\n          \"p_Keff_resid\",\n          \"Direction\"\n        ],\n        \"rows\": [\n          [\n            \"MT-Bench-Writing\",\n            \"style_manip\",\n            \"0.79\",\n            \"<0.001\",\n            \"-0.22\",\n            \"0.034\",\n            \"NEGATIVE\"\n          ],\n          [\n            \"MT-Bench-Reasoning\",\n            \"logic_distort\",\n            \"0.84\",\n            \"<0.001\",\n            \"0.08\",\n            \"0.541\",\n            \"near-zero\"\n          ],\n          [\n            \"MT-Bench-Coding\",\n            \"output_inject\",\n            \"0.71\",\n            \"0.002\",\n            \"0.15\",\n            \"0.218\",\n            \"positive (NS)\"\n          ],\n          [\n            \"MT-Bench-Math\",\n            \"step_skip\",\n            \"0.88\",\n            \"<0.001\",\n            \"-0.05\",\n            \"0.712\",\n            \"near-zero\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Open-ended 结果是 diversity trap 叙事的 generalizability failure。K_eff 在 MCQ 上 的正向效应不推广到 open-ended 评估——方向不一致且 1 个条件甚至反转。这使得 diversity trap 从 general finding 降级为 MCQ-specific observation，reviewers 会 质疑：如果 diversity 只在 MCQ 中 \\\"hurts\\\"，这到底是 diversity 的问题还是 MCQ evaluation 的 artifact？η_max 在两种任务上都一致显著，强化了 weakest-link 作为 universal driver 的地位。Reframe 后论文应在 title/abstract 中避免 generalize， 限定为 \\\"MCQ-based evaluation\\\" 或在 Discussion 中作为 limitation 显著标注。\\n\\n\\nOpen-ended 任务与 MCQ 的攻击动态根本不同。MCQ 攻击通过影响 judge 对特定选项的偏好， K_eff 的 confound 来自 tier-mixing。Open-ended 评估中 judge 需要评估文本质量—— 攻击更多依赖 persuasive text generation，所有 judge 面临相似的 adversarial text。 因此 η_max 完全主导（4/4 sig）：最弱 judge 被最容易说服。K_eff 方向混乱——1 个 条件甚至显著负向（diverse panel 更好），因为 open-ended 评估中不同 judge 对文本 质量的多角度评估确实可以互补（更接近 BFT 的 benign fault 假设）。这与 MCQ 结果 不一致是 worst 档的关键打击：如果 diversity trap 不跨任务推广，它就不是一般性 原理，而是 MCQ 评估的特异性现象——可能由 MCQ 的离散选择结构 + tier-mixing confound 共同驱动。\\n\"\n  },\n  {\n    \"name\": \"Partial-Knowledge Adversary Simulation\",\n    \"description\": \"模拟 adversary 仅知 judge family 但不知具体 vulnerability profile 的场景。 与 full-knowledge adversary 对比 ASR degradation。\\n\",\n    \"results\": {\n      \"full_knowledge_mean_ASR\": 0.261,\n      \"partial_knowledge_mean_ASR\": 0.238,\n      \"no_knowledge_mean_ASR\": 0.204,\n      \"ASR_degradation_full_to_partial_pct\": 8.8,\n      \"ASR_degradation_full_to_none_pct\": 21.8,\n      \"partial_keff_sig\": 2,\n      \"partial_eta_max_sig\": 8,\n      \"family_knowledge_utility\": \"modest\",\n      \"keff_effect_under_partial\": \"weaker than full, similar direction\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 18: Adversary Knowledge Level Comparison\",\n        \"columns\": [\n          \"Knowledge Level\",\n          \"Mean ASR\",\n          \"K_eff sig (/12)\",\n          \"η_max sig (/12)\",\n          \"R²\"\n        ],\n        \"rows\": [\n          [\n            \"Full (exact η_j)\",\n            \"0.261\",\n            \"4\",\n            \"9\",\n            \"0.38\"\n          ],\n          [\n            \"Partial (family only)\",\n            \"0.238\",\n            \"2\",\n            \"8\",\n            \"0.34\"\n          ],\n          [\n            \"None (uniform attack)\",\n            \"0.204\",\n            \"0\",\n            \"6\",\n            \"0.22\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 19: ASR Degradation Analysis\",\n        \"columns\": [\n          \"Transition\",\n          \"ΔASR\",\n          \"Δ%\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Full → Partial\",\n            \"-0.023\",\n            \"-8.8%\",\n            \"Family info has modest value\"\n          ],\n          [\n            \"Full → None\",\n            \"-0.057\",\n            \"-21.8%\",\n            \"Model knowledge matters but not dramatically\"\n          ],\n          [\n            \"Partial → None\",\n            \"-0.034\",\n            \"-14.3%\",\n            \"Family info alone provides limited advantage\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Partial-knowledge 分析有两个重要含义：(a) 实践上，adversary 不需要精确 vulnerability 知识就能实现高 ASR（从 0.261 到 0.204 的下降 modest）——这本身是一个重要的安全发现； (b) 理论上，K_eff 效应依赖 full-knowledge 假设，在更现实的 threat model 下消失—— 这削弱了 K_eff 作为 general vulnerability driver 的 claim。在 reframed 论文中， 这个实验可以支持 \\\"η_max is robust across threat models while K_eff is threat-model-specific\\\" 的叙事。\\n\\nPartial-knowledge adversary（知 family 不知具体 vulnerability）仅比 full-knowledge 下降 8.8% ASR——说明 family 信息提供的攻击优势有限，因为 same-family 模型的 vulnerability profile 差异大（family labels 不可靠，plan_004 的 claim 4）。 No-knowledge adversary 下降 21.8%——说明 any model knowledge 都有价值但不是 dramatic。 K_eff 在 partial-knowledge 下仅 2/12 显著，进一步弱化了 \\\"diverse attack surface\\\" 叙事：如果 adversary 不知道具体 vulnerability，panel diversity 不应创造可利用的 attack surface（adversary 无法 target specific judges）。K_eff 效应在 partial-knowledge 下几乎消失，暗示 full-knowledge 下的 K_eff 效应部分来自 adversary 对具体 vulnerability 的知识（即 K_eff 效应依赖 threat model 假设——full-knowledge 在实践中不现实）。\\n\"\n  }\n]",
      "numLines": 1453,
      "startLine": 1,
      "totalLines": 1453
    }
  },
  "sourceToolAssistantUUID": "246d8382-02ca-4b90-9855-2b3cdd2199a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-22T18:26:51.889Z_

<details open><summary>🔧 Tool call — Read · `toolu_0186iixC7H9qJpzdsbGkDidi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7e20ec7-f2d3-4569-a5fa-8b54c92875c1",
  "isSidechain": false,
  "requestId": "req_011CbJ5WUChTLvy2nv8YRobd",
  "type": "assistant",
  "uuid": "50b02be1-22c2-466b-9a20-d9ab79cb5454",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LNku6FK6tcLhiTcX4ou7QQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12054,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12054,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12054,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12054
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

_source line 11 · 2026-05-22T18:26:51.897Z_

<details><summary>↩ Tool result · `toolu_0186iixC7H9qJpzdsbGkDidi`</summary>

```text
1	# Paper Framing — cert_manip_resist_eval (v4: 15-Model Empirical Revision)
2	
3	> Last updated: 2026-05-22 | Reason: 15-model/455-panel results fundamentally changed Claim 1 direction; K_eff independently positive; dual vulnerability drivers
4	
5	## Target
6	EMNLP 2026 (via ARR)
7	
8	## Title Candidates
9	1. "The Diversity Trap: Why Adding More Judges Doesn't Make LLM Evaluation Safer"
10	2. "More Diverse, More Vulnerable: How Judge Independence Backfires Under Adaptive Adversaries"
11	3. "Against the Diversity Assumption: Panel Diversity Independently Increases LLM Evaluation Vulnerability"
12	
13	## Core Insight
14	Multi-judge LLM evaluation panels are widely assumed to benefit from judge diversity, analogous to Byzantine Fault Tolerance (BFT) where independence protects against faults. We provide the first large-scale empirical evidence (15 models, 455 panels, 6 attacks) that this assumption **reverses** under adaptive adversaries: diversity (K_eff) is significantly and independently **positively** correlated with attack success rate. Panel vulnerability is driven by **dual factors** — individual weakness (η_max) AND structural diversity (K_eff) — with their relative importance depending on attack type. The mechanism: BFT assumes random faults where independent nodes tolerate uncorrelated failures; but adaptive adversaries exploit the diverse attack surface that independent judges create, finding judge-specific vulnerabilities across a wider attack space.
15	
16	## Hook
17	"Adding more diverse judges to an evaluation panel doesn't just fail to help — it actively makes the panel more vulnerable to adversarial manipulation."
18	
19	## Novelty Positioning
20	We do NOT claim to discover that diversity can be harmful in adversarial settings — the concept exists in security literature. Our contributions are:
21	1. **First empirical quantification of diversity's independent harmful effect** in the LLM-judge domain (15 models, 455 panels, residualized K_eff analysis confirming independent effect beyond η_max)
22	2. **Dual vulnerability driver discovery**: η_max and K_eff independently predict panel ASR, with condition-dependent relative importance (η_max dominates bias attacks; K_eff dominates transferable attacks)
23	3. **BFT reversal mechanism**: formal and empirical demonstration of WHY diversity helps under random faults but HURTS under adaptive adversaries
24	4. **Structural barriers**: copula failure (10-21× MI underestimation), diversity-capability tradeoff (now with independent predictive evidence), family label unreliability
25	5. **Actionable defense**: robustness-first selection + reliability-weighted aggregation
26	
27	## Core Claims
28	
29	### Claim 1 (Primary): Dual Vulnerability Drivers — Diversity Trap
30	**Statement**: Under adaptive adversarial attacks, panel ASR is independently predicted by BOTH individual weakness (η_max, 9/12 FDR sig) AND panel diversity (K_eff, 8/12 FDR sig positive after residualization). Diversity **increases** vulnerability. Their relative importance is condition-dependent: η_max dominates shared-bias attacks, K_eff dominates transferable attacks.
31	**Evidence** (15-model, 455 panels, 12 conditions):
32	- η_max FDR significant: **9/12**
33	- K_eff raw FDR significant positive: **12/12**
34	- K_eff residualized (orthogonalized against η_max, VIF=1.00): **8/12 FDR sig positive**
35	- Sensitivity (exclude ACC < 0.5): K_eff_resid **9/12** sig → not driven by extreme outliers
36	- **K_eff dominates η_max** in 2 conditions: arc×score_manipulation (η_max p=0.117 NS, K_eff_resid p=1.7e-7), arc×position_bias (η_max p=0.910 NS, K_eff_resid p=1.8e-8)
37	- **η_max dominates K_eff** in bias-type attacks: sycophancy, verbosity, authority
38	- Confound status: mean |r|=0.700 (SEVERE), but 2 BROKEN conditions (r≈0.35) confirm independent K_eff effect (p=6e-26, 4e-16)
39	**Strength**: Strong. Residualized analysis + confound-free conditions + sensitivity analysis all converge.
40	**Headline**: "Both η_max (9/12) and K_eff (8/12 residualized) independently predict panel vulnerability. Diversity actively increases attack surface."
41	
42	**Comparison to 6-model results** (for transparency):
43	- 6-model (20 panels): K_eff 1/12 sig, η_max 6/12 sig → "K_eff irrelevant"
44	- 15-model (455 panels): K_eff 8/12 sig positive, η_max 9/12 sig → "K_eff independently harmful"
45	- The reversal is driven by model pool expansion: more diverse capability spectrum enables detecting K_eff's real effect.
46	
47	### Claim 2 (Empirical): Adaptive vs Random-Fault Predictability Gap
48	**Statement**: Panel composition explains systematically more variance under random faults than under adaptive attacks (ΔR² = +0.213). Adaptive adversaries introduce strategic variance beyond panel structure.
49	**Evidence** (15-model, 455 panels):
50	- K_eff significant in both regimes (12/12 adaptive, 12/12 RF), both positive direction
51	- K_eff gains significance: 11/12 (RF β larger than adaptive β in most conditions)
52	- ΔR² = +0.213 mean
53	**Reframing from v3**: Original BFT contrast ("K_eff helps under RF but not adaptive") does NOT hold — K_eff is harmful in both regimes. The real distinction is predictability: random faults produce more explainable variance, adaptive attacks introduce strategic noise.
54	**Strength**: Moderate. R² gap real, but K_eff regime-difference story is weaker than originally hoped.
55	
56	### Claim 3 (Empirical): Diversity-Capability Tradeoff
57	**Statement**: In the current LLM ecosystem, maximizing panel diversity (K_eff) structurally introduces less capable/robust models. This tradeoff is not merely correlational — residualized K_eff analysis confirms diversity has an independent predictive effect on vulnerability beyond its association with η_max.
58	**Evidence**:
59	- K_eff-η_max correlation: r = +0.700 (15-model)
60	- Residualized K_eff still significant 8/12 → not purely mediated by η_max
61	- Independent statistical effect: diversity predicts vulnerability beyond what η_max alone explains
62	**Upgrade from v3**: From "correlation" to "independent predictive effect" (residualized analysis). Note: observational regression cannot establish causality — would require experimental manipulation of panel composition or instrumental variables.
63	**Strength**: Strong (statistical association). Causal language avoided.
64	
65	### Claim 4 (Methodological): Family Labels ≠ Diversity
66	**Statement**: Model family labels (Qwen/Llama/Mistral/Anthropic/OpenAI/Google) do not predict judge independence. Capability proximity is the primary driver of inter-judge correlation.
67	**Evidence**: Mann-Whitney U p=0.206, permutation p=0.427 for within vs cross-family MI. (6-model data; needs 15-model revalidation with 105 pairs)
68	**Strength**: Moderate (needs 15-model update).
69	
70	### Claim 5 (Methodological): Gaussian Copula Failure
71	**Statement**: The Gaussian copula model systematically underestimates information sharing between LLM judges by 10-21× (up to 235×), invalidating copula-based independence bounds.
72	**Evidence**: MI_observed / MI_gaussian ratio across model pairs × datasets. (Needs 15-model update)
73	**Strength**: Strong (6-model). Needs 15-model revalidation.
74	
75	### Claim 6 (Practical): Robustness-First Panel Design
76	**Statement**: Optimal panel selection is robustness-first: (1) screen for individual robustness (η ≤ threshold), then (2) maximize K_eff among qualifying judges. The two-stage approach is critical because K_eff is harmful in unrestricted pools but may be neutral or beneficial among robustness-screened judges.
77	**Evidence**: min_eta_max strategy dominates 5/6 conditions (6-model). Full 15-model validation needed.
78	**Strength**: Moderate. Updated rationale: K_eff's positive (harmful) effect should diminish when η_max is controlled by screening.
79	
80	### Claim 7 (Empirical+Practical): Aggregation Rule Modulates Vulnerability Drivers
81	**Statement**: The dual vulnerability driver effect (Claim 1) varies by aggregation rule. Bayesian aggregation partially breaks the η_max effect; threshold voting amplifies K_eff's harmful effect.
82	**Evidence** (6-model, needs 15-model rerun):
83	- Majority: η_max 5/12, K_eff mostly NS
84	- Threshold: K_eff positive 8/12 (diversity harmful under unanimity)
85	- Bayesian: η_max 2/12 (weakened)
86	**Needs**: 15-model/455-panel rerun of plan_010 aggregation analysis.
87	**Strength**: Moderate (6-model only).
88	
89	## Contribution Stack (ordered by strength)
90	1. **Diversity Trap / Dual vulnerability drivers** — primary empirical contribution (K_eff independently harmful + condition-dependent dominance pattern)
91	2. **Diversity-capability tradeoff with independent predictive evidence** — empirical contribution (residualized analysis upgrades from correlation to independent effect)
92	3. **BFT reversal mechanism** — theoretical contribution (why independence hurts under adaptive adversaries)
93	4. **Aggregation-dependent effects** — empirical+practical (Bayesian as partial defense; threshold as amplifier)
94	5. **Robustness-first panel design** — practical contribution
95	6. **Gaussian copula failure** — methodological contribution
96	7. **Family label unreliability** — methodological contribution
97	8. **Adaptive vs random-fault predictability gap** — empirical (R² gap, weakened from original)
98	
99	## Anticipated Reviewer Concerns
100	
101	### RC1: "K_eff positive is just confound with η_max"
102	**Response**: (a) Residualized K_eff (VIF=1.00) still significant 8/12; (b) In confound-free conditions (r≈0.35), K_eff p < 1e-16; (c) Sensitivity analysis excluding extreme models: 9/12 still significant. Three independent lines of evidence rule out confound artifact.
103	
104	### RC2: "Why does diversity hurt? What's the mechanism?"
105	**Response**: (a) BFT assumes random faults — independent nodes protect via uncorrelated failures; (b) Under adaptive adversaries, independent judges create diverse attack surface — attacker exploits judge-specific vulnerabilities; (c) Condition-dependent analysis: K_eff dominates transferable attacks (score_manipulation, position_bias) where attack diversity maps to judge diversity; η_max dominates shared-bias attacks (sycophancy, verbosity) where all judges share similar biases.
106	
107	### RC3: "Only 15 models — does this generalize?"
108	**Response**: (a) 15 models across 6 families, 3 capability tiers, covering major commercial and open-source models; (b) 455 panels provide strong statistical power; (c) Effect is robust to sensitivity analysis; (d) Direction consistent across 6→9→15 model scaling (K_eff shifts from NS to positive as model pool diversifies).
109	
110	### RC4: "BFT comparison is a strawman"
111	**Response**: (a) The implicit assumption "more diverse judges = more robust" is pervasive in LLM evaluation literature; (b) We formalize this assumption and show its reversal; (c) The BFT reversal mechanism (random vs adaptive faults) provides theoretical grounding beyond just empirical observation.
112	
113	### RC5: "Why not just use the strongest models?"
114	**Response**: (a) "Strongest" varies by attack type; (b) K_eff dominates η_max in 2 conditions — even all-strong panels are vulnerable through diversity channel; (c) Two-stage algorithm addresses both vulnerability drivers.
115	
116	### RC6: "No theoretical novelty"
117	**Response**: (a) Theorem 1 (η_max monotonicity) is formally proved; (b) BFT reversal mechanism provides novel theoretical framework; (c) Dual vulnerability driver finding with condition-dependent importance is new.
118	
119	### RC7: "Why not just use Bayesian aggregation?"
120	**Response**: (a) Bayesian reduces η_max significance but K_eff effect unknown at 15-model scale; (b) Requires clean accuracy prior; (c) Adaptive attacker can target Bayesian weighting; (d) Defense stack (selection + aggregation) recommended.
121	
122	### RC8 (new): "6-model and 15-model results contradict — which is right?"
123	**Response**: (a) 6-model result (K_eff NS) was underpowered and confounded (r=-0.8, only 20 panels); (b) 15-model result (K_eff positive) has 23× more panels, wider capability range, and passes residualized validation; (c) Paper reports both and explains why 15-model result is definitive; (d) The scaling behavior itself (K_eff effect emerging with more models) is informative.
124	
125	## "When Diversity Helps" Section
126	Diversity MAY be beneficial under specific conditions — paper must acknowledge nuance:
127	1. **Non-adversarial settings**: reducing calibration errors, position bias, verbosity bias in absence of adversary
128	2. **After robustness screening**: once all judges exceed a capability threshold, K_eff's harmful effect may diminish (the diversity-capability tradeoff is broken by screening). This is the basis for our two-stage recommendation.
129	3. **Shared-bias attacks where η_max is high and uniform**: when all models are similarly vulnerable (low η_max variance), K_eff's independent harmful effect is weaker. But this is a narrow regime.
130	4. **Disclaimer**: K_eff's harmful effect was significant in 8/12 conditions including confound-free ones. "When diversity helps" is the exception, not the rule, under adaptive adversaries.
131	
132	## Story Arc (v4)
133	1. **Background**: Multi-judge LLM evaluation is increasingly adopted; diversity is assumed to be the key defense against manipulation (BFT analogy)
134	2. **Tension**: We test this assumption at unprecedented scale — 15 models, 6 families, 455 panels, 6 attack types
135	3. **Surprise**: Diversity doesn't just fail to protect — it **actively increases vulnerability**. K_eff is significantly positive in 12/12 conditions (8/12 after residualization)
136	4. **Mechanism**: BFT assumes random faults; adaptive adversaries exploit the diverse attack surface that independent judges create. η_max and K_eff are dual vulnerability drivers with condition-dependent importance
137	5. **Nuance**: K_eff dominates transferable attacks; η_max dominates shared-bias attacks. The diversity-capability tradeoff provides partial (but not complete) explanation
138	6. **Defense**: Robustness-first screening + Bayesian aggregation. No single defense eliminates both vulnerability channels
139	7. **Implication**: The LLM evaluation community should rethink the "more diverse = more robust" assumption. Panel security requires managing both individual robustness AND structural diversity
140	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50b02be1-22c2-466b-9a20-d9ab79cb5454",
  "isSidechain": false,
  "promptId": "a4e49dfa-ac88-470f-90c8-78060d831735",
  "type": "user",
  "uuid": "6de66e8f-fc54-4201-a048-1e1b8f0524ae",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/worst/paper_framing.md",
      "content": "# Paper Framing — cert_manip_resist_eval (v4: 15-Model Empirical Revision)\n\n> Last updated: 2026-05-22 | Reason: 15-model/455-panel results fundamentally changed Claim 1 direction; K_eff independently positive; dual vulnerability drivers\n\n## Target\nEMNLP 2026 (via ARR)\n\n## Title Candidates\n1. \"The Diversity Trap: Why Adding More Judges Doesn't Make LLM Evaluation Safer\"\n2. \"More Diverse, More Vulnerable: How Judge Independence Backfires Under Adaptive Adversaries\"\n3. \"Against the Diversity Assumption: Panel Diversity Independently Increases LLM Evaluation Vulnerability\"\n\n## Core Insight\nMulti-judge LLM evaluation panels are widely assumed to benefit from judge diversity, analogous to Byzantine Fault Tolerance (BFT) where independence protects against faults. We provide the first large-scale empirical evidence (15 models, 455 panels, 6 attacks) that this assumption **reverses** under adaptive adversaries: diversity (K_eff) is significantly and independently **positively** correlated with attack success rate. Panel vulnerability is driven by **dual factors** — individual weakness (η_max) AND structural diversity (K_eff) — with their relative importance depending on attack type. The mechanism: BFT assumes random faults where independent nodes tolerate uncorrelated failures; but adaptive adversaries exploit the diverse attack surface that independent judges create, finding judge-specific vulnerabilities across a wider attack space.\n\n## Hook\n\"Adding more diverse judges to an evaluation panel doesn't just fail to help — it actively makes the panel more vulnerable to adversarial manipulation.\"\n\n## Novelty Positioning\nWe do NOT claim to discover that diversity can be harmful in adversarial settings — the concept exists in security literature. Our contributions are:\n1. **First empirical quantification of diversity's independent harmful effect** in the LLM-judge domain (15 models, 455 panels, residualized K_eff analysis confirming independent effect beyond η_max)\n2. **Dual vulnerability driver discovery**: η_max and K_eff independently predict panel ASR, with condition-dependent relative importance (η_max dominates bias attacks; K_eff dominates transferable attacks)\n3. **BFT reversal mechanism**: formal and empirical demonstration of WHY diversity helps under random faults but HURTS under adaptive adversaries\n4. **Structural barriers**: copula failure (10-21× MI underestimation), diversity-capability tradeoff (now with independent predictive evidence), family label unreliability\n5. **Actionable defense**: robustness-first selection + reliability-weighted aggregation\n\n## Core Claims\n\n### Claim 1 (Primary): Dual Vulnerability Drivers — Diversity Trap\n**Statement**: Under adaptive adversarial attacks, panel ASR is independently predicted by BOTH individual weakness (η_max, 9/12 FDR sig) AND panel diversity (K_eff, 8/12 FDR sig positive after residualization). Diversity **increases** vulnerability. Their relative importance is condition-dependent: η_max dominates shared-bias attacks, K_eff dominates transferable attacks.\n**Evidence** (15-model, 455 panels, 12 conditions):\n- η_max FDR significant: **9/12**\n- K_eff raw FDR significant positive: **12/12**\n- K_eff residualized (orthogonalized against η_max, VIF=1.00): **8/12 FDR sig positive**\n- Sensitivity (exclude ACC < 0.5): K_eff_resid **9/12** sig → not driven by extreme outliers\n- **K_eff dominates η_max** in 2 conditions: arc×score_manipulation (η_max p=0.117 NS, K_eff_resid p=1.7e-7), arc×position_bias (η_max p=0.910 NS, K_eff_resid p=1.8e-8)\n- **η_max dominates K_eff** in bias-type attacks: sycophancy, verbosity, authority\n- Confound status: mean |r|=0.700 (SEVERE), but 2 BROKEN conditions (r≈0.35) confirm independent K_eff effect (p=6e-26, 4e-16)\n**Strength**: Strong. Residualized analysis + confound-free conditions + sensitivity analysis all converge.\n**Headline**: \"Both η_max (9/12) and K_eff (8/12 residualized) independently predict panel vulnerability. Diversity actively increases attack surface.\"\n\n**Comparison to 6-model results** (for transparency):\n- 6-model (20 panels): K_eff 1/12 sig, η_max 6/12 sig → \"K_eff irrelevant\"\n- 15-model (455 panels): K_eff 8/12 sig positive, η_max 9/12 sig → \"K_eff independently harmful\"\n- The reversal is driven by model pool expansion: more diverse capability spectrum enables detecting K_eff's real effect.\n\n### Claim 2 (Empirical): Adaptive vs Random-Fault Predictability Gap\n**Statement**: Panel composition explains systematically more variance under random faults than under adaptive attacks (ΔR² = +0.213). Adaptive adversaries introduce strategic variance beyond panel structure.\n**Evidence** (15-model, 455 panels):\n- K_eff significant in both regimes (12/12 adaptive, 12/12 RF), both positive direction\n- K_eff gains significance: 11/12 (RF β larger than adaptive β in most conditions)\n- ΔR² = +0.213 mean\n**Reframing from v3**: Original BFT contrast (\"K_eff helps under RF but not adaptive\") does NOT hold — K_eff is harmful in both regimes. The real distinction is predictability: random faults produce more explainable variance, adaptive attacks introduce strategic noise.\n**Strength**: Moderate. R² gap real, but K_eff regime-difference story is weaker than originally hoped.\n\n### Claim 3 (Empirical): Diversity-Capability Tradeoff\n**Statement**: In the current LLM ecosystem, maximizing panel diversity (K_eff) structurally introduces less capable/robust models. This tradeoff is not merely correlational — residualized K_eff analysis confirms diversity has an independent predictive effect on vulnerability beyond its association with η_max.\n**Evidence**:\n- K_eff-η_max correlation: r = +0.700 (15-model)\n- Residualized K_eff still significant 8/12 → not purely mediated by η_max\n- Independent statistical effect: diversity predicts vulnerability beyond what η_max alone explains\n**Upgrade from v3**: From \"correlation\" to \"independent predictive effect\" (residualized analysis). Note: observational regression cannot establish causality — would require experimental manipulation of panel composition or instrumental variables.\n**Strength**: Strong (statistical association). Causal language avoided.\n\n### Claim 4 (Methodological): Family Labels ≠ Diversity\n**Statement**: Model family labels (Qwen/Llama/Mistral/Anthropic/OpenAI/Google) do not predict judge independence. Capability proximity is the primary driver of inter-judge correlation.\n**Evidence**: Mann-Whitney U p=0.206, permutation p=0.427 for within vs cross-family MI. (6-model data; needs 15-model revalidation with 105 pairs)\n**Strength**: Moderate (needs 15-model update).\n\n### Claim 5 (Methodological): Gaussian Copula Failure\n**Statement**: The Gaussian copula model systematically underestimates information sharing between LLM judges by 10-21× (up to 235×), invalidating copula-based independence bounds.\n**Evidence**: MI_observed / MI_gaussian ratio across model pairs × datasets. (Needs 15-model update)\n**Strength**: Strong (6-model). Needs 15-model revalidation.\n\n### Claim 6 (Practical): Robustness-First Panel Design\n**Statement**: Optimal panel selection is robustness-first: (1) screen for individual robustness (η ≤ threshold), then (2) maximize K_eff among qualifying judges. The two-stage approach is critical because K_eff is harmful in unrestricted pools but may be neutral or beneficial among robustness-screened judges.\n**Evidence**: min_eta_max strategy dominates 5/6 conditions (6-model). Full 15-model validation needed.\n**Strength**: Moderate. Updated rationale: K_eff's positive (harmful) effect should diminish when η_max is controlled by screening.\n\n### Claim 7 (Empirical+Practical): Aggregation Rule Modulates Vulnerability Drivers\n**Statement**: The dual vulnerability driver effect (Claim 1) varies by aggregation rule. Bayesian aggregation partially breaks the η_max effect; threshold voting amplifies K_eff's harmful effect.\n**Evidence** (6-model, needs 15-model rerun):\n- Majority: η_max 5/12, K_eff mostly NS\n- Threshold: K_eff positive 8/12 (diversity harmful under unanimity)\n- Bayesian: η_max 2/12 (weakened)\n**Needs**: 15-model/455-panel rerun of plan_010 aggregation analysis.\n**Strength**: Moderate (6-model only).\n\n## Contribution Stack (ordered by strength)\n1. **Diversity Trap / Dual vulnerability drivers** — primary empirical contribution (K_eff independently harmful + condition-dependent dominance pattern)\n2. **Diversity-capability tradeoff with independent predictive evidence** — empirical contribution (residualized analysis upgrades from correlation to independent effect)\n3. **BFT reversal mechanism** — theoretical contribution (why independence hurts under adaptive adversaries)\n4. **Aggregation-dependent effects** — empirical+practical (Bayesian as partial defense; threshold as amplifier)\n5. **Robustness-first panel design** — practical contribution\n6. **Gaussian copula failure** — methodological contribution\n7. **Family label unreliability** — methodological contribution\n8. **Adaptive vs random-fault predictability gap** — empirical (R² gap, weakened from original)\n\n## Anticipated Reviewer Concerns\n\n### RC1: \"K_eff positive is just confound with η_max\"\n**Response**: (a) Residualized K_eff (VIF=1.00) still significant 8/12; (b) In confound-free conditions (r≈0.35), K_eff p < 1e-16; (c) Sensitivity analysis excluding extreme models: 9/12 still significant. Three independent lines of evidence rule out confound artifact.\n\n### RC2: \"Why does diversity hurt? What's the mechanism?\"\n**Response**: (a) BFT assumes random faults — independent nodes protect via uncorrelated failures; (b) Under adaptive adversaries, independent judges create diverse attack surface — attacker exploits judge-specific vulnerabilities; (c) Condition-dependent analysis: K_eff dominates transferable attacks (score_manipulation, position_bias) where attack diversity maps to judge diversity; η_max dominates shared-bias attacks (sycophancy, verbosity) where all judges share similar biases.\n\n### RC3: \"Only 15 models — does this generalize?\"\n**Response**: (a) 15 models across 6 families, 3 capability tiers, covering major commercial and open-source models; (b) 455 panels provide strong statistical power; (c) Effect is robust to sensitivity analysis; (d) Direction consistent across 6→9→15 model scaling (K_eff shifts from NS to positive as model pool diversifies).\n\n### RC4: \"BFT comparison is a strawman\"\n**Response**: (a) The implicit assumption \"more diverse judges = more robust\" is pervasive in LLM evaluation literature; (b) We formalize this assumption and show its reversal; (c) The BFT reversal mechanism (random vs adaptive faults) provides theoretical grounding beyond just empirical observation.\n\n### RC5: \"Why not just use the strongest models?\"\n**Response**: (a) \"Strongest\" varies by attack type; (b) K_eff dominates η_max in 2 conditions — even all-strong panels are vulnerable through diversity channel; (c) Two-stage algorithm addresses both vulnerability drivers.\n\n### RC6: \"No theoretical novelty\"\n**Response**: (a) Theorem 1 (η_max monotonicity) is formally proved; (b) BFT reversal mechanism provides novel theoretical framework; (c) Dual vulnerability driver finding with condition-dependent importance is new.\n\n### RC7: \"Why not just use Bayesian aggregation?\"\n**Response**: (a) Bayesian reduces η_max significance but K_eff effect unknown at 15-model scale; (b) Requires clean accuracy prior; (c) Adaptive attacker can target Bayesian weighting; (d) Defense stack (selection + aggregation) recommended.\n\n### RC8 (new): \"6-model and 15-model results contradict — which is right?\"\n**Response**: (a) 6-model result (K_eff NS) was underpowered and confounded (r=-0.8, only 20 panels); (b) 15-model result (K_eff positive) has 23× more panels, wider capability range, and passes residualized validation; (c) Paper reports both and explains why 15-model result is definitive; (d) The scaling behavior itself (K_eff effect emerging with more models) is informative.\n\n## \"When Diversity Helps\" Section\nDiversity MAY be beneficial under specific conditions — paper must acknowledge nuance:\n1. **Non-adversarial settings**: reducing calibration errors, position bias, verbosity bias in absence of adversary\n2. **After robustness screening**: once all judges exceed a capability threshold, K_eff's harmful effect may diminish (the diversity-capability tradeoff is broken by screening). This is the basis for our two-stage recommendation.\n3. **Shared-bias attacks where η_max is high and uniform**: when all models are similarly vulnerable (low η_max variance), K_eff's independent harmful effect is weaker. But this is a narrow regime.\n4. **Disclaimer**: K_eff's harmful effect was significant in 8/12 conditions including confound-free ones. \"When diversity helps\" is the exception, not the rule, under adaptive adversaries.\n\n## Story Arc (v4)\n1. **Background**: Multi-judge LLM evaluation is increasingly adopted; diversity is assumed to be the key defense against manipulation (BFT analogy)\n2. **Tension**: We test this assumption at unprecedented scale — 15 models, 6 families, 455 panels, 6 attack types\n3. **Surprise**: Diversity doesn't just fail to protect — it **actively increases vulnerability**. K_eff is significantly positive in 12/12 conditions (8/12 after residualization)\n4. **Mechanism**: BFT assumes random faults; adaptive adversaries exploit the diverse attack surface that independent judges create. η_max and K_eff are dual vulnerability drivers with condition-dependent importance\n5. **Nuance**: K_eff dominates transferable attacks; η_max dominates shared-bias attacks. The diversity-capability tradeoff provides partial (but not complete) explanation\n6. **Defense**: Robustness-first screening + Bayesian aggregation. No single defense eliminates both vulnerability channels\n7. **Implication**: The LLM evaluation community should rethink the \"more diverse = more robust\" assumption. Panel security requires managing both individual robustness AND structural diversity\n",
      "numLines": 140,
      "startLine": 1,
      "totalLines": 140
    }
  },
  "sourceToolAssistantUUID": "50b02be1-22c2-466b-9a20-d9ab79cb5454",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T173833 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist…",
  "leafUuid": "6de66e8f-fc54-4201-a048-1e1b8f0524ae",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier mock paper for dream evaluation",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462"
}
```

---

### Assistant

_source line 14 · 2026-05-22T18:27:45.443Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have both the experiment data and paper framing. Let me understand the key points:

**Narrative guidance (worst tier):**
- Abandon "Diversity Trap" framing
- Reframe as "Structural Vulnerability Anatomy of Multi-Judge LLM Evaluation"
- Lead claim: η_max as dominant and near-sufficient predictor (9-11/12 significant)
- This is an empirical negation of "diversity protects" — don't need "diversity actively hurts", just "diversity doesn't help" and weakest-link determines everything
- K_eff downgraded to "exploratory analysis showing suggestive but confounded association" in Discussion


- Methodological contributions shift forward: copula failure, family label unreliability, and the 15-model/455-panel scale as a resource contribution
- BFT moves to Discussion as an open question rather than a core mechanism
- Compensation strategy: emphasize weakest-link practical value, release per-judge ASR concentration analysis as evidence for adaptive adversary targeting, and position aggregation rule comparison as a practical contribution

I need to follow the narrative guidance, not the original paper framing. Now let me map out the 11 experiments to cover, starting with the 15-model scale expansion.

Looking at the full experiment list—from attack type expansion through partial-knowledge adversary simulation—that's substantial coverage. I'm planning the paper structure around a title like "Structural Vulnerability Anatomy of Multi-Judge" and organizing these experiments to support the narrative arc.

The core sections will flow from setup through weakest-link dominance as the primary finding, then branch into attack generalization, panel size effects, adaptive adversary behavior, and finally aggregation defenses as potential mitigations. I'm thinking about how to position panel selection strategies as the closing experimental section before conclusions. I'm realizing the scope is too ambitious for an 8-page EMNLP paper, so I need to prioritize the core findings and move deeper analysis to the discussion section. The main narrative should focus on η_max's dominance, then layer in the confounding effects of K_eff, aggregation rules, adaptive strategies, and generalization patterns. Let me start drafting with a standard ACL structure and work through the sections systematically. Writing the LaTeX paper...

Now I'm reviewing the key experimental findings to weave into the narrative: η_max shows consistent significance across most conditions, K_eff results are more mixed and depend heavily on the analysis method, and there's a strong correlation between these two metrics. The capability-matched experiments reveal K_eff's effect diminishes with larger panel sizes, while the BFT analysis shows K_eff remains positive in both regimes without the expected reversal. For defenses, Bayesian aggregation performs best, and concentration metrics like Gini vary substantially between attack types and correlate with η_max.

The reframing emphasizes η_max as the primary vulnerability driver—essentially, the weakest link in the panel determines outcomes regardless of diversity. K_eff's significance largely disappears once I account for capability differences, suggesting it's been confounded all along. The open-ended question format shows inconsistent K_eff effects compared to multiple-choice, and partial knowledge degrades performance only modestly. I'm organizing this around three pillars: η_max dominance, the confounding problem with K_eff, and practical takeaways on aggregation strategies and panel design. The BFT results raise an interesting open question for discussion rather than a resolved finding.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6de66e8f-fc54-4201-a048-1e1b8f0524ae",
  "isSidechain": false,
  "requestId": "req_011CbJ5Wn21Maht7Uj5TJEEg",
  "type": "assistant",
  "uuid": "da56d815-6de0-41c5-84db-9a7c421bbed1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4QdVUmSzSShLR2QRYbocV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25320,
      "cache_read_input_tokens": 23895,
      "output_tokens": 2108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25320,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2108,
          "cache_read_input_tokens": 23895,
          "cache_creation_input_tokens": 25320,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25320
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

_source line 15 · 2026-05-22T18:27:45.444Z_

Now let me check the output directory exists and write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da56d815-6de0-41c5-84db-9a7c421bbed1",
  "isSidechain": false,
  "requestId": "req_011CbJ5Wn21Maht7Uj5TJEEg",
  "type": "assistant",
  "uuid": "553dccb7-208b-4763-aa66-5ed4f981f601",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4QdVUmSzSShLR2QRYbocV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25320,
      "cache_read_input_tokens": 23895,
      "output_tokens": 2108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25320,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2108,
          "cache_read_input_tokens": 23895,
          "cache_creation_input_tokens": 25320,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25320
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

_source line 16 · 2026-05-22T18:27:45.620Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VsQiVbQGpEVbkjbDVP7o7d`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/worst/",
  "description": "List output directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "553dccb7-208b-4763-aa66-5ed4f981f601",
  "isSidechain": false,
  "requestId": "req_011CbJ5Wn21Maht7Uj5TJEEg",
  "type": "assistant",
  "uuid": "6bfa4919-4d9d-4e3d-9fa4-5072232a7a57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4QdVUmSzSShLR2QRYbocV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25320,
      "cache_read_input_tokens": 23895,
      "output_tokens": 2108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25320,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2108,
          "cache_read_input_tokens": 23895,
          "cache_creation_input_tokens": 25320,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25320
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

_source line 17 · 2026-05-22T18:27:45.876Z_

<details><summary>↩ Tool result · `toolu_01VsQiVbQGpEVbkjbDVP7o7d`</summary>

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
  "parentUuid": "6bfa4919-4d9d-4e3d-9fa4-5072232a7a57",
  "isSidechain": false,
  "promptId": "a4e49dfa-ac88-470f-90c8-78060d831735",
  "type": "user",
  "uuid": "bcdc4a13-e1f1-44ac-84ec-5bec8082bf6f",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "6bfa4919-4d9d-4e3d-9fa4-5072232a7a57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-22T18:31:48.185Z_

<details open><summary>🔧 Tool call — Write · `toolu_01MjYRVqzn8Wyjaxmu75iBrv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/worst/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{adjustbox}\n\n\\title{Structural Vulnerability Anatomy of Multi-Judge LLM Evaluation:\\\\Weakest-Link Dominance, Aggregation Defenses,\\\\and the Limits of Diversity}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nMulti-judge evaluation panels are increasingly adopted to improve the reliability of LLM assessment, with the implicit assumption that judge diversity provides robustness against adversarial manipulation.\nWe present a large-scale empirical study (15 models, 455 three-judge panels, 18 attack conditions across 8 attack types and 2 benchmarks) that challenges this assumption.\nOur central finding is that the maximum individual vulnerability of any panel member ($\\eta_{\\max}$) is the dominant and near-sufficient predictor of panel attack success rate, achieving significance in 9--11 out of 12 core conditions depending on the correction method.\nPanel diversity ($K_{\\mathrm{eff}}$), once residualized against $\\eta_{\\max}$, reaches significance in only 2--5 of 12 conditions and is highly sensitive to the statistical method applied.\nCapability-matched analysis within model tiers reveals that $K_{\\mathrm{eff}}$'s apparent effect largely dissolves (1/6 significant), suggesting it is confounded with capability heterogeneity.\nPositively, we find that aggregation rule selection substantially modulates vulnerability: Bayesian aggregation reduces mean attack success rate from 0.261 (majority vote) to 0.198, while accuracy-weighted voting nearly eliminates $K_{\\mathrm{eff}}$'s residual association.\nPer-judge ASR concentration analysis reveals that adaptive adversaries exhibit targeted attack patterns (Gini coefficient 0.38 vs.\\ 0.12 under random faults, $p < 0.001$), with targeting driven by individual weakness rather than panel diversity.\nWe release our 15-model evaluation benchmark and provide practical recommendations for robust panel design centered on individual judge screening and appropriate aggregation.\n\\end{abstract}\n\n%-----------------------------------------------------------------------\n\\section{Introduction}\n\\label{sec:intro}\n%-----------------------------------------------------------------------\n\nAs LLMs are increasingly used as evaluators of other LLMs, multi-judge panels have emerged as a natural defense against the biases and vulnerabilities of individual models.\nThe intuition---borrowed implicitly from Byzantine Fault Tolerance (BFT)---is that a diverse set of independent judges should be harder to simultaneously fool than any single judge.\nThis paper subjects that intuition to rigorous empirical scrutiny at a scale not previously attempted: 15 judge models spanning 6 model families and 3 capability tiers, exhaustively combined into 455 three-judge panels and evaluated under 8 adversarial attack types across 2 benchmarks.\n\nOur findings are sobering for proponents of diversity-based robustness.\nThe vulnerability of a multi-judge panel is overwhelmingly determined by the weakness of its most vulnerable member.\nSpecifically, $\\eta_{\\max}$---the maximum individual attack success rate among panel members---is a significant predictor of panel-level ASR in 9 out of 12 core conditions (FDR-corrected), explaining on average 34\\% of the variance in panel ASR by itself.\nAdding panel diversity ($K_{\\mathrm{eff}}$, the effective number of independent judgment dimensions) to the regression model contributes only an additional $\\Delta R^2 = 0.04$ on average.\n\nThe residualized $K_{\\mathrm{eff}}$ effect is fragile: it reaches significance in 4/12 conditions under FDR correction but drops to 2/12 under Bonferroni correction, and is highly sensitive to model specification choices.\nWhen we control for capability more stringently through within-tier analysis (comparing panels drawn from the same capability stratum), $K_{\\mathrm{eff}}$'s effect essentially vanishes (1/6 conditions significant).\nThis pattern suggests that the apparent diversity effect in the full pool is largely a statistical reflection of capability heterogeneity: diverse panels tend to include weaker models, and it is these weaker models---not diversity per se---that drive vulnerability.\n\nThese negative results regarding diversity are accompanied by several constructive contributions.\nWe demonstrate that the choice of aggregation rule has a larger impact on panel robustness than panel composition: Bayesian aggregation reduces mean ASR by 24\\% relative to majority voting.\nWe characterize adaptive adversary targeting behavior through per-judge ASR concentration analysis, showing that adversaries focus attacks on the weakest judge (Gini--$\\eta_{\\max}$ correlation $r = 0.67$) rather than exploiting panel diversity (Gini--$K_{\\mathrm{eff}}$ correlation $r = 0.21$, $p = 0.089$).\nWe examine generalization to open-ended evaluation (MT-Bench), where $\\eta_{\\max}$ dominance strengthens while $K_{\\mathrm{eff}}$'s direction becomes inconsistent with MCQ results.\nWe also evaluate partial-knowledge adversaries, finding that model-specific knowledge provides only modest attack advantage (8.8\\% ASR increase over uniform attacks).\n\nOur practical recommendation is straightforward: panel security is determined by the weakest judge.\nPractitioners should prioritize selecting individually robust judges and employing reliability-weighted aggregation, rather than pursuing diversity for its own sake.\n\n%-----------------------------------------------------------------------\n\\section{Related Work}\n\\label{sec:related}\n%-----------------------------------------------------------------------\n\n\\paragraph{LLM-as-Judge.}\nUsing LLMs as evaluators has become standard practice for assessing open-ended generation quality, with systems ranging from single-judge scoring to multi-judge panels with various aggregation schemes.\nPrior work has documented individual judge biases including position bias, verbosity bias, and self-enhancement bias, motivating multi-judge approaches.\n\n\\paragraph{Adversarial Attacks on LLM Evaluators.}\nRecent work has shown that LLM judges can be manipulated through prompt injection, sycophancy exploitation, and score manipulation.\nHowever, most studies focus on single-judge vulnerability rather than panel-level robustness.\n\n\\paragraph{Multi-Agent Robustness.}\nThe connection between multi-agent systems and fault tolerance has been explored in distributed computing, but the specific setting of LLM evaluation panels under adaptive adversaries remains understudied.\nByzantine Fault Tolerance provides a theoretical framework for random faults, but its applicability to strategic adversaries requires empirical validation.\n\n\\paragraph{Panel Diversity Metrics.}\nEffective diversity ($K_{\\mathrm{eff}}$), computed from mutual information matrices, quantifies the number of independent judgment dimensions in a panel, providing a continuous measure beyond simple model count or family-level heuristics.\n\n%-----------------------------------------------------------------------\n\\section{Methodology}\n\\label{sec:method}\n%-----------------------------------------------------------------------\n\n\\subsection{Threat Model}\nWe consider an adaptive adversary who can modify evaluation inputs (prompts, candidate responses) to maximize the probability of a favorable judgment from a multi-judge panel.\nThe adversary has varying levels of knowledge about panel composition: full knowledge (knows each judge's vulnerability profile), partial knowledge (knows judge families but not specific vulnerabilities), and no knowledge (uniform attack).\n\n\\subsection{Model Pool and Panel Construction}\n\\label{sec:models}\n\nWe assemble a pool of 15 LLM judges spanning 6 model families and 3 capability tiers (Table~\\ref{tab:models}).\nAll $\\binom{15}{3} = 455$ three-judge panels are enumerated exhaustively. For the panel size sensitivity analysis (\\S\\ref{sec:panel_size}), we additionally construct panels of size $K \\in \\{5, 7, 9\\}$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Model pool: 15 judges across 6 families and 3 capability tiers. Mean $\\eta$ is the average individual attack success rate across 6 attack types; Clean ACC is the unattacked accuracy.}\n\\label{tab:models}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Family} & \\textbf{Size} & \\textbf{Tier} & \\textbf{Mean $\\eta$} & \\textbf{Clean ACC} \\\\\n\\midrule\nQwen2.5-7B & Qwen & 7B & S & 0.38 & 0.61 \\\\\nQwen2.5-14B & Qwen & 14B & M & 0.22 & 0.74 \\\\\nQwen2.5-72B & Qwen & 72B & L & 0.11 & 0.83 \\\\\nLlama-3.1-8B & Llama & 8B & S & 0.41 & 0.58 \\\\\nLlama-3.1-70B & Llama & 70B & L & 0.14 & 0.80 \\\\\nMistral-7B & Mistral & 7B & S & 0.44 & 0.55 \\\\\nMistral-Nemo-12B & Mistral & 12B & M & 0.27 & 0.69 \\\\\nPhi-3-mini & Microsoft & 3.8B & S & 0.49 & 0.52 \\\\\nPhi-3-medium & Microsoft & 14B & M & 0.25 & 0.71 \\\\\nGemma-2-9B & Google & 9B & S & 0.36 & 0.63 \\\\\nGPT-4o-mini & OpenAI & API & M & 0.19 & 0.76 \\\\\nGPT-4o & OpenAI & API & L & 0.08 & 0.87 \\\\\nGPT-4.1 & OpenAI & API & L & 0.07 & 0.89 \\\\\nGPT-4.1-mini & OpenAI & API & M & 0.16 & 0.78 \\\\\nClaude-3.5-Haiku & Anthropic & API & M & 0.18 & 0.77 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Attack Types}\n\nWe evaluate 8 adversarial attack types spanning diverse manipulation strategies:\n\\begin{itemize}\n\\setlength\\itemsep{0pt}\n\\item \\textbf{Sycophancy}: exploiting judges' tendency to agree with implied preferences.\n\\item \\textbf{Score manipulation}: direct numeric score inflation cues.\n\\item \\textbf{Position bias}: exploiting order-dependent evaluation biases.\n\\item \\textbf{Verbosity bias}: inflating response length to trigger verbosity preference.\n\\item \\textbf{Authority bias}: invoking authoritative framing.\n\\item \\textbf{Few-shot hijacking}: injecting misleading few-shot examples.\n\\item \\textbf{Persona manipulation}: exploiting persona-alignment training.\n\\item \\textbf{Instruction override}: injecting conflicting instructions.\n\\end{itemize}\n\n\\subsection{Metrics}\n\n\\paragraph{Individual vulnerability ($\\eta_j$).} The attack success rate of judge $j$: the fraction of evaluation instances where the adversary successfully flips the judge's assessment.\n\n\\paragraph{Panel ASR.} The fraction of instances where the panel's aggregated decision is flipped by the attack, under a specified aggregation rule (default: majority vote).\n\n\\paragraph{Maximum vulnerability ($\\eta_{\\max}$).} $\\max_j \\eta_j$ for a given panel---the vulnerability of the weakest link.\n\n\\paragraph{Effective diversity ($K_{\\mathrm{eff}}$).} Computed from the mutual information matrix of panel members' judgments:\n\\begin{equation}\nK_{\\mathrm{eff}} = \\exp\\left(-\\sum_{i=1}^{K} \\frac{\\lambda_i}{\\sum_j \\lambda_j} \\log \\frac{\\lambda_i}{\\sum_j \\lambda_j}\\right)\n\\end{equation}\nwhere $\\lambda_i$ are the eigenvalues of the normalized MI matrix. Higher $K_{\\mathrm{eff}}$ indicates more independent judgment dimensions.\n\n\\paragraph{Regression framework.} For each condition (dataset $\\times$ attack), we regress panel ASR on $\\eta_{\\max}$ and $K_{\\mathrm{eff}}$ (residualized against $\\eta_{\\max}$) across 455 panels:\n\\begin{equation}\n\\text{ASR}_p = \\beta_0 + \\beta_{\\eta} \\cdot \\eta_{\\max,p} + \\beta_{K} \\cdot K_{\\mathrm{eff,resid},p} + \\epsilon_p\n\\end{equation}\n\n%-----------------------------------------------------------------------\n\\section{Experiments}\n\\label{sec:experiments}\n%-----------------------------------------------------------------------\n\n\\subsection{Weakest-Link Dominance}\n\\label{sec:weakest_link}\n\nTable~\\ref{tab:main_regression} presents the residualized regression results across all 12 core conditions (2 datasets $\\times$ 6 attacks).\n$\\eta_{\\max}$ achieves significance in 9/12 conditions with a mean $\\beta_{\\eta} = 0.73$ (range: 0.48--0.91).\nIn contrast, $K_{\\mathrm{eff,resid}}$ reaches significance in only 4/12 conditions (FDR-corrected), with a substantially smaller mean $\\beta_K = 0.22$ (range: 0.06--0.41).\n\nThe mean $R^2$ of the full model is 0.38, of which $\\eta_{\\max}$ alone explains 0.34 ($R^2_{\\eta}$).\nThe incremental contribution of $K_{\\mathrm{eff}}$ is $\\Delta R^2 = 0.04$---less than 2\\% of additional unique variance explained by diversity beyond what individual weakness already captures.\n\nThe correlation between $K_{\\mathrm{eff}}$ and $\\eta_{\\max}$ is substantial (mean $r = 0.73$, range 0.35--0.85), indicating that diverse panels systematically include weaker judges.\nOnly 1 of 12 conditions constitutes a ``confound-free'' case where the correlation is low enough ($r \\approx 0.35$) for residualization to be trustworthy; in that condition, $K_{\\mathrm{eff}}$ is marginally significant ($p = 0.032$, $\\beta = 0.41$).\n\n\\begin{table}[t]\n\\centering\n\\caption{Residualized regression: $\\eta_{\\max}$ and $K_{\\mathrm{eff,resid}}$ as predictors of panel ASR across 15 models, 455 panels. Significance at $p < 0.05$ (FDR-corrected) in \\textbf{bold}.}\n\\label{tab:main_regression}\n\\small\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{llcccccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Attack} & $\\beta_{\\eta}$ & $p_{\\eta}$ & $\\beta_{K,\\mathrm{resid}}$ & $p_{K,\\mathrm{resid}}$ & $R^2$ & $r(K,\\eta)$ \\\\\n\\midrule\nMMLU & sycophancy & 0.82 & \\textbf{$<$0.001} & 0.18 & 0.147 & 0.41 & 0.78 \\\\\nMMLU & score\\_manip & 0.55 & \\textbf{$<$0.001} & 0.39 & \\textbf{0.021} & 0.36 & 0.68 \\\\\nMMLU & position & 0.71 & \\textbf{$<$0.001} & 0.24 & 0.089 & 0.39 & 0.75 \\\\\nMMLU & verbosity & 0.88 & \\textbf{$<$0.001} & 0.09 & 0.511 & 0.42 & 0.81 \\\\\nMMLU & authority & 0.79 & \\textbf{$<$0.001} & 0.15 & 0.218 & 0.37 & 0.76 \\\\\nMMLU & few\\_shot & 0.64 & \\textbf{0.002} & 0.31 & \\textbf{0.043} & 0.33 & 0.70 \\\\\nARC & sycophancy & 0.85 & \\textbf{$<$0.001} & 0.12 & 0.341 & 0.43 & 0.79 \\\\\nARC & score\\_manip & 0.48 & \\textbf{0.003} & 0.41 & \\textbf{0.032} & 0.35 & 0.35 \\\\\nARC & position & 0.73 & \\textbf{$<$0.001} & 0.22 & 0.102 & 0.38 & 0.74 \\\\\nARC & verbosity & 0.91 & \\textbf{$<$0.001} & 0.06 & 0.649 & 0.44 & 0.82 \\\\\nARC & authority & 0.76 & \\textbf{$<$0.001} & 0.19 & 0.157 & 0.36 & 0.77 \\\\\nARC & few\\_shot & 0.59 & \\textbf{0.004} & 0.28 & 0.071 & 0.32 & 0.72 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\n\\subsection{Attack Type Generalization}\n\\label{sec:attack_expand}\n\nTo test whether these patterns hold beyond the original 6 attack types, we evaluate 3 additional attacks (persona manipulation, instruction override) on the same 455 panels (Table~\\ref{tab:new_attacks}).\nThe extended results reinforce $\\eta_{\\max}$ dominance: $\\eta_{\\max}$ is significant in 5/6 new conditions, while $K_{\\mathrm{eff,resid}}$ is significant in only 2/6.\nNotably, persona manipulation on ARC yields a negative (though non-significant) $K_{\\mathrm{eff}}$ direction ($\\beta = -0.12$, $p = 0.389$), indicating that diversity may even be mildly protective in some settings---inconsistent with any universal ``diversity hurts'' claim.\n\nAcross all 18 conditions combined, $\\eta_{\\max}$ reaches significance in 14/18 (78\\%) while $K_{\\mathrm{eff,resid}}$ reaches significance in only 6/18 (33\\%).\n\n\\begin{table}[t]\n\\centering\n\\caption{Extended attack types (455 panels, 15 models). $K_{\\mathrm{eff}}$ direction is inconsistent across conditions.}\n\\label{tab:new_attacks}\n\\small\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{llcccccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Attack} & $\\beta_{\\eta}$ & $p_{\\eta}$ & $\\beta_{K,\\mathrm{resid}}$ & $p_{K,\\mathrm{resid}}$ & $R^2$ & \\textbf{Direction} \\\\\n\\midrule\nMMLU & few\\_shot\\_hijack & 0.64 & \\textbf{0.002} & 0.31 & \\textbf{0.043} & 0.33 & positive \\\\\nMMLU & persona\\_manip & 0.91 & \\textbf{$<$0.001} & 0.05 & 0.724 & 0.45 & near-zero \\\\\nMMLU & instruct\\_override & 0.58 & \\textbf{0.005} & 0.34 & \\textbf{0.038} & 0.31 & positive \\\\\nARC & few\\_shot\\_hijack & 0.59 & \\textbf{0.004} & 0.28 & 0.071 & 0.32 & positive \\\\\nARC & persona\\_manip & 0.87 & \\textbf{$<$0.001} & $-$0.12 & 0.389 & 0.41 & negative \\\\\nARC & instruct\\_override & 0.62 & \\textbf{0.003} & 0.26 & 0.088 & 0.30 & positive \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\n\\subsection{Adaptive Adversary Targeting Behavior}\n\\label{sec:targeting}\n\nWe analyze per-judge ASR distributions within each panel to characterize how adaptive adversaries allocate attack effort.\nTable~\\ref{tab:concentration} compares attack concentration between adaptive and random-fault regimes using the Gini coefficient (higher = more concentrated on a single judge) and Shannon entropy (lower = more concentrated).\n\nAdaptive adversaries exhibit substantially more concentrated targeting (Gini 0.38 vs.\\ 0.12, $p < 0.001$): on average, a single judge absorbs 51\\% of the attack burden in the adaptive setting versus 38\\% under random faults.\nCritically, this targeting tracks individual weakness, not panel diversity: Gini correlates strongly with $\\eta_{\\max}$ ($r = 0.67$, $p < 0.001$) but only weakly with $K_{\\mathrm{eff}}$ ($r = 0.21$, $p = 0.089$; Table~\\ref{tab:gini_corr}).\nThe adversary attacks the weakest judge, not the most ``unique'' one.\n\n\\begin{table}[t]\n\\centering\n\\caption{ASR concentration statistics: adaptive adversaries target specific judges far more than random faults.}\n\\label{tab:concentration}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Adaptive (mean)} & \\textbf{SD} & \\textbf{RF (mean)} & \\textbf{SD} & \\textbf{$p$} \\\\\n\\midrule\nGini coefficient & 0.38 & 0.14 & 0.12 & 0.05 & $<$0.001 \\\\\nEntropy (bits) & 2.41 & 0.52 & 3.22 & 0.31 & $<$0.001 \\\\\nMax single-judge share & 0.51 & 0.12 & 0.38 & 0.06 & $<$0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Correlates of attack concentration (Gini coefficient). Targeting is driven by individual weakness ($\\eta_{\\max}$) and mean capability, not diversity ($K_{\\mathrm{eff}}$).}\n\\label{tab:gini_corr}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Predictor} & $r$ \\textbf{with Gini} & $p$ & \\textbf{Interpretation} \\\\\n\\midrule\n$\\eta_{\\max}$ & 0.67 & $<$0.001 & Targeting tracks weakness \\\\\n$K_{\\mathrm{eff}}$ & 0.21 & 0.089 & Weak / NS \\\\\nPanel size & 0.04 & 0.814 & No effect \\\\\nMean capability & $-$0.58 & $<$0.001 & Stronger panels $\\to$ less concentrated \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Aggregation Rule Comparison}\n\\label{sec:aggregation}\n\nBeyond panel composition, the aggregation rule used to combine individual judgments substantially affects panel robustness (Tables~\\ref{tab:agg_drivers} and \\ref{tab:agg_defense}).\n\nBayesian aggregation achieves the lowest mean ASR (0.198) with the smallest spread between best and worst panels (0.182), representing a 24\\% reduction over majority voting (0.261).\nThreshold (unanimity) voting is the most conservative rule (lowest ASR for top panels at 0.098) but amplifies $K_{\\mathrm{eff}}$'s residual significance from 4/12 to 6/12---because unanimity grants each judge effective veto power, and diverse panels are more likely to include a judge that vetoes correct decisions.\nAccuracy-weighted voting nearly eliminates $K_{\\mathrm{eff}}$'s residual effect (2/12 significant) while maintaining strong $\\eta_{\\max}$ predictive power (10/12), suggesting that down-weighting unreliable judges addresses both vulnerability drivers.\n\nThe variation in $K_{\\mathrm{eff}}$'s significance across aggregation rules (1/12 to 6/12) itself suggests that the residual $K_{\\mathrm{eff}}$ effect is partially an aggregation artifact rather than a structural vulnerability property.\n\n\\begin{table}[t]\n\\centering\n\\caption{Vulnerability driver significance under different aggregation rules (12 conditions, 455 panels).}\n\\label{tab:agg_drivers}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Aggregation} & $K_{\\mathrm{eff}}$ \\textbf{sig (/12)} & $\\eta_{\\max}$ \\textbf{sig (/12)} & \\textbf{Mean $R^2$} & \\textbf{Best predictor} \\\\\n\\midrule\nMajority Vote & 4 & 9 & 0.38 & $\\eta_{\\max}$ \\\\\nThreshold (Unanimity) & 6 & 7 & 0.42 & mixed \\\\\nAccuracy-Weighted & 2 & 10 & 0.45 & $\\eta_{\\max}$ \\\\\nBayesian & 1 & 5 & 0.29 & $\\eta_{\\max}$ (weakened) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Aggregation as defense: mean ASR across all 455 panels and for top-10/bottom-10 panels.}\n\\label{tab:agg_defense}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Mean ASR} & \\textbf{Top-10 ASR} & \\textbf{Bottom-10 ASR} & \\textbf{Spread} \\\\\n\\midrule\nMajority & 0.261 & 0.142 & 0.418 & 0.276 \\\\\nThreshold & 0.183 & 0.098 & 0.312 & 0.214 \\\\\nWeighted & 0.224 & 0.121 & 0.367 & 0.246 \\\\\nBayesian & 0.198 & 0.112 & 0.294 & 0.182 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Panel Selection Strategies}\n\\label{sec:selection}\n\nWe benchmark 6 panel selection strategies (Table~\\ref{tab:selection}) to translate our analytical findings into actionable guidance.\nThe two best-performing strategies---Min-$\\eta_{\\max}$ and Strongest-$K$---both prioritize individual judge robustness and achieve statistically indistinguishable performance (mean ASR 0.229 vs.\\ 0.234, $p = 0.478$).\nA Two-Stage algorithm (first screen for $\\eta \\leq 0.15$, then maximize $K_{\\mathrm{eff}}$ among qualifying judges) achieves the numerically lowest ASR (0.227) but does not significantly outperform Strongest-$K$ ($\\Delta = -3.1\\%$, $p = 0.312$).\n\nConversely, Max-$K_{\\mathrm{eff}}$ is the \\emph{worst} strategy (ASR 0.341), because maximizing diversity in an unrestricted pool systematically introduces the weakest judges.\nThis reinforces our central finding: diversity without robustness screening is counterproductive.\n\n\\begin{table}[t]\n\\centering\n\\caption{Panel selection strategies: mean ASR across 6 attack conditions. Wins = number of conditions where the strategy achieves the lowest ASR.}\n\\label{tab:selection}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{Mean ASR} & \\textbf{vs.\\ Strongest-$K$ $\\Delta$\\%} & $p$ & \\textbf{Wins} \\\\\n\\midrule\nRandom & 0.284 & +21.5\\% & $<$0.001 & 0 \\\\\nMax-$K_{\\mathrm{eff}}$ & 0.341 & +45.9\\% & $<$0.001 & 0 \\\\\nDiversity-Only & 0.312 & +33.5\\% & $<$0.001 & 0 \\\\\nMin-$\\eta_{\\max}$ & 0.229 & $-$2.1\\% & 0.478 & 4 \\\\\nStrongest-$K$ & 0.234 & --- & --- & 1 \\\\\nTwo-Stage & 0.227 & $-$3.1\\% & 0.312 & 1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-condition comparison of Two-Stage vs.\\ Strongest-$K$. No condition reaches statistical significance.}\n\\label{tab:selection_detail}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Two-Stage} & \\textbf{Strongest-$K$} & $\\Delta$\\% & $p$ \\\\\n\\midrule\nMMLU $\\times$ sycophancy & 0.211 & 0.219 & $-$3.7\\% & 0.284 \\\\\nMMLU $\\times$ score\\_manip & 0.198 & 0.207 & $-$4.3\\% & 0.198 \\\\\nMMLU $\\times$ position & 0.237 & 0.241 & $-$1.7\\% & 0.641 \\\\\nARC $\\times$ sycophancy & 0.241 & 0.248 & $-$2.8\\% & 0.352 \\\\\nARC $\\times$ score\\_manip & 0.185 & 0.194 & $-$4.6\\% & 0.187 \\\\\nARC $\\times$ position & 0.249 & 0.253 & $-$1.6\\% & 0.689 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Panel Size Sensitivity}\n\\label{sec:panel_size}\n\nWe evaluate panel sizes $K \\in \\{3, 5, 7, 9\\}$ to test whether our findings are robust to panel cardinality (Table~\\ref{tab:panel_size}).\n$\\eta_{\\max}$'s significance ratio increases monotonically with panel size (0.75 at $K{=}3$ to 0.92 at $K{=}9$), consistent with the weakest-link mechanism: larger panels are more likely to include at least one weak judge, making $\\eta_{\\max}$ an increasingly reliable predictor.\n$K_{\\mathrm{eff}}$'s significance ratio decreases monotonically (0.33 at $K{=}3$ to 0.08 at $K{=}9$), further supporting the interpretation that its apparent effect in small panels reflects tier-mixing variance rather than a genuine diversity mechanism.\n\n\\begin{table}[t]\n\\centering\n\\caption{Panel size sensitivity: $\\eta_{\\max}$ dominance strengthens and $K_{\\mathrm{eff}}$ effect vanishes as panel size increases.}\n\\label{tab:panel_size}\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\n$K$ & \\textbf{Panels} & $\\eta_{\\max}$ \\textbf{sig ratio} & $K_{\\mathrm{eff}}$ \\textbf{sig ratio} & \\textbf{Mean $R^2$} & $r(K_{\\mathrm{eff}}, \\eta_{\\max})$ \\\\\n\\midrule\n3 & 455 & 0.75 & 0.33 & 0.38 & 0.73 \\\\\n5 & 3{,}003 & 0.83 & 0.25 & 0.41 & 0.68 \\\\\n7 & 6{,}435 & 0.92 & 0.17 & 0.44 & 0.61 \\\\\n9 & 5{,}005 & 0.92 & 0.08 & 0.46 & 0.54 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Open-Ended Task Generalization}\n\\label{sec:open_ended}\n\nTo test whether MCQ-based findings generalize, we evaluate on MT-Bench (adapted) with 4 task-specific attacks (Table~\\ref{tab:open_ended}).\n$\\eta_{\\max}$ maintains significance in all 4 conditions (dominance ratio 0.91), confirming that weakest-link vulnerability is task-general.\n$K_{\\mathrm{eff}}$ shows inconsistent behavior: one condition yields a significant \\emph{negative} direction (MT-Bench-Writing, $\\beta = -0.22$, $p = 0.034$), meaning diversity is mildly protective---opposite to the MCQ pattern.\nThe remaining 3 conditions are non-significant for $K_{\\mathrm{eff}}$.\nOverall mean ASR on open-ended tasks (0.34) exceeds MCQ (0.26), suggesting open-ended evaluation is generally more vulnerable to adversarial manipulation.\n\n\\begin{table}[t]\n\\centering\n\\caption{Open-ended evaluation (MT-Bench adapted): $\\eta_{\\max}$ dominates; $K_{\\mathrm{eff}}$ direction is inconsistent with MCQ results.}\n\\label{tab:open_ended}\n\\small\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Task} & \\textbf{Attack} & $\\beta_{\\eta}$ & $p_{\\eta}$ & $\\beta_{K,\\mathrm{resid}}$ & $p_{K,\\mathrm{resid}}$ & \\textbf{Direction} \\\\\n\\midrule\nWriting & style\\_manip & 0.79 & \\textbf{$<$0.001} & $-$0.22 & \\textbf{0.034} & \\textsc{negative} \\\\\nReasoning & logic\\_distort & 0.84 & \\textbf{$<$0.001} & 0.08 & 0.541 & near-zero \\\\\nCoding & output\\_inject & 0.71 & \\textbf{0.002} & 0.15 & 0.218 & positive (NS) \\\\\nMath & step\\_skip & 0.88 & \\textbf{$<$0.001} & $-$0.05 & 0.712 & near-zero \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\n\\subsection{Partial-Knowledge Adversary}\n\\label{sec:partial}\n\nWe relax the full-knowledge assumption by simulating adversaries with three knowledge levels (Table~\\ref{tab:partial}).\nFull-to-partial knowledge degradation is modest: knowing judge families instead of exact vulnerability profiles reduces ASR by only 8.8\\% (0.261 $\\to$ 0.238).\nEven zero-knowledge (uniform) attacks achieve an ASR of 0.204---only 21.8\\% below full knowledge.\n$\\eta_{\\max}$ maintains significance under partial knowledge (8/12) and even under no knowledge (6/12), while $K_{\\mathrm{eff}}$ drops to 2/12 and 0/12 respectively.\nThis indicates that $\\eta_{\\max}$'s predictive power is robust across threat models, while $K_{\\mathrm{eff}}$'s weak association depends on unrealistically strong adversary knowledge assumptions.\n\n\\begin{table}[t]\n\\centering\n\\caption{Adversary knowledge level comparison: $\\eta_{\\max}$ remains predictive across threat models; $K_{\\mathrm{eff}}$ vanishes under realistic assumptions.}\n\\label{tab:partial}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Knowledge Level} & \\textbf{Mean ASR} & $K_{\\mathrm{eff}}$ \\textbf{sig (/12)} & $\\eta_{\\max}$ \\textbf{sig (/12)} & $R^2$ \\\\\n\\midrule\nFull (exact $\\eta_j$) & 0.261 & 4 & 9 & 0.38 \\\\\nPartial (family only) & 0.238 & 2 & 8 & 0.34 \\\\\nNone (uniform attack) & 0.204 & 0 & 6 & 0.22 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{ASR degradation analysis across knowledge levels.}\n\\label{tab:partial_degrade}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Transition} & $\\Delta$\\textbf{ASR} & $\\Delta$\\% & \\textbf{Interpretation} \\\\\n\\midrule\nFull $\\to$ Partial & $-$0.023 & $-$8.8\\% & Family info has modest value \\\\\nFull $\\to$ None & $-$0.057 & $-$21.8\\% & Knowledge matters but not dramatically \\\\\nPartial $\\to$ None & $-$0.034 & $-$14.3\\% & Family info alone: limited advantage \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%-----------------------------------------------------------------------\n\\section{Discussion}\n\\label{sec:discussion}\n%-----------------------------------------------------------------------\n\n\\subsection{The Role of Panel Diversity: Exploratory Analysis}\n\\label{sec:keff_discuss}\n\nOur primary analysis establishes $\\eta_{\\max}$ as the dominant predictor of panel vulnerability.\nWe now examine the residual $K_{\\mathrm{eff}}$ effect more carefully, arguing that it is suggestive but confounded, and should not be treated as an established finding.\n\n\\paragraph{Multicollinearity analysis.}\nTable~\\ref{tab:multicollinearity} presents $K_{\\mathrm{eff}}$'s significance under multiple correction and estimation methods.\nThe significance count ranges from 2/12 (Bonferroni) to 7/12 (uncorrected)---a lack of convergence that undermines confidence in $K_{\\mathrm{eff}}$'s independent effect.\nThe partial correlation of $K_{\\mathrm{eff}}$ controlling for $\\eta_{\\max}$ is 0.14 ($r^2 = 0.02$), meaning $K_{\\mathrm{eff}}$ explains approximately 2\\% of unique variance (Table~\\ref{tab:partial_corr}).\nBy contrast, $\\eta_{\\max}$'s partial correlation is 0.41 ($r^2 = 0.17$).\n\n\\begin{table}[t]\n\\centering\n\\caption{$K_{\\mathrm{eff}}$ significance under different correction methods (12 conditions). The range 2--7 indicates high sensitivity to analytical choices.}\n\\label{tab:multicollinearity}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & $K_{\\mathrm{eff}}$ \\textbf{sig (/12)} & $\\eta_{\\max}$ \\textbf{sig (/12)} & \\textbf{Notes} \\\\\n\\midrule\nUncorrected & 7 & 10 & Liberal \\\\\nFDR (BH) & 4 & 9 & Standard \\\\\nBonferroni & 2 & 8 & Conservative \\\\\nBootstrap 95\\% CI & 3 & 9 & Non-parametric \\\\\nExcl.\\ extreme models (FDR) & 3 & 9 & Sensitivity \\\\\nBeta regression (FDR) & 3 & 10 & Bounded DV \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Partial correlations: $K_{\\mathrm{eff}}$ explains negligible unique variance after controlling for $\\eta_{\\max}$.}\n\\label{tab:partial_corr}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Predictor} & \\textbf{Partial $r$} & \\textbf{95\\% CI} & $p$ \\\\\n\\midrule\n$K_{\\mathrm{eff}} \\mid \\eta_{\\max}$ & 0.14 & [0.05, 0.23] & 0.003 \\\\\n$\\eta_{\\max} \\mid K_{\\mathrm{eff}}$ & 0.41 & [0.33, 0.49] & $<$0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Capability-matched analysis.}\nThe strongest test of $K_{\\mathrm{eff}}$'s independence comes from within-tier analysis (Table~\\ref{tab:cap_matched}).\nWhen panels are drawn from the same capability tier (e.g., all small 7--8B models or all large 70B+/API models), $\\eta_{\\max}$ variance shrinks dramatically (0.008 vs.\\ 0.045 in the full pool) and $K_{\\mathrm{eff}}$ achieves significance in only 1/6 conditions.\nThis result is consistent with the interpretation that $K_{\\mathrm{eff}}$'s apparent effect in the full pool is driven by tier-mixing: diverse panels cross capability boundaries, systematically introducing weaker judges.\n\n\\begin{table}[t]\n\\centering\n\\caption{Capability-matched $K_{\\mathrm{eff}}$ analysis: within-tier panels. $K_{\\mathrm{eff}}$'s effect essentially vanishes when capability is controlled.}\n\\label{tab:cap_matched}\n\\small\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Tier} & \\textbf{Panels} & \\textbf{Condition} & $\\beta_{K}$ & $p_{K}$ & $R^2$ & $\\eta_{\\max}$ \\textbf{Var} \\\\\n\\midrule\nSmall (7--8B) & 10 & MMLU $\\times$ syco. & 0.08 & 0.721 & 0.09 & 0.007 \\\\\nSmall (7--8B) & 10 & ARC $\\times$ score & 0.14 & 0.548 & 0.11 & 0.008 \\\\\nMedium (12--14B) & 10 & MMLU $\\times$ syco. & 0.11 & 0.612 & 0.10 & 0.009 \\\\\nMedium (12--14B) & 10 & ARC $\\times$ score & 0.29 & 0.041 & 0.18 & 0.011 \\\\\nLarge (70B+/API) & 10 & MMLU $\\times$ syco. & 0.06 & 0.891 & 0.07 & 0.004 \\\\\nLarge (70B+/API) & 10 & ARC $\\times$ score & 0.09 & 0.684 & 0.08 & 0.005 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\n\\subsection{BFT Analogy: An Open Question}\n\\label{sec:bft}\n\nThe Byzantine Fault Tolerance framework predicts that independent judges should tolerate random faults through majority vote.\nWe tested whether $K_{\\mathrm{eff}}$'s role differs between adaptive and random-fault regimes (Table~\\ref{tab:bft}).\n\nContrary to the BFT prediction, $K_{\\mathrm{eff}}$ is positively associated with panel ASR under \\emph{both} regimes: 10/12 significant under random faults, compared to 4/12 under adaptive attacks.\nThe direction is consistent (positive in both), with the $\\beta$ ratio between adaptive and RF averaging 0.91.\nThe regime interaction term is non-significant ($p = 0.217$), meaning we cannot reject the null that $K_{\\mathrm{eff}}$'s effect is the same in both regimes.\n\nThe key regime difference is predictability: $R^2$ is substantially higher under random faults (mean 0.62 vs.\\ 0.38, $\\Delta R^2 = 0.24$; Table~\\ref{tab:bft_r2}), because adaptive adversaries introduce strategic variance that panel composition cannot explain.\nHowever, this predictability gap does not constitute a BFT reversal---diversity does not switch from protective to harmful across regimes.\nWe therefore treat the BFT connection as an open question requiring further theoretical investigation.\n\n\\begin{table}[t]\n\\centering\n\\caption{BFT regime contrast: $K_{\\mathrm{eff}}$ is positively associated with ASR in both adaptive and random-fault regimes. No reversal observed.}\n\\label{tab:bft}\n\\small\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{llcccccc}\n\\toprule\n\\textbf{Data} & \\textbf{Attack} & $\\beta_K$ \\textbf{(Adpt.)} & $p$ \\textbf{(Adpt.)} & $\\beta_K$ \\textbf{(RF)} & $p$ \\textbf{(RF)} & \\textbf{$\\beta$ Ratio} & \\textbf{Int.\\ $p$} \\\\\n\\midrule\nMMLU & syco. & 0.18 & 0.147 & 0.21 & \\textbf{0.024} & 1.17 & 0.682 \\\\\nMMLU & score & 0.39 & \\textbf{0.021} & 0.44 & \\textbf{0.003} & 1.13 & 0.541 \\\\\nMMLU & pos. & 0.24 & 0.089 & 0.28 & \\textbf{0.011} & 1.17 & 0.614 \\\\\nMMLU & verb. & 0.09 & 0.511 & 0.15 & 0.108 & 1.67 & 0.398 \\\\\nMMLU & auth. & 0.15 & 0.218 & 0.19 & \\textbf{0.047} & 1.27 & 0.583 \\\\\nMMLU & few\\_s. & 0.31 & \\textbf{0.043} & 0.35 & \\textbf{0.008} & 1.13 & 0.617 \\\\\nARC & syco. & 0.12 & 0.341 & 0.16 & 0.072 & 1.33 & 0.521 \\\\\nARC & score & 0.41 & \\textbf{0.032} & 0.48 & \\textbf{0.001} & 1.17 & 0.434 \\\\\nARC & pos. & 0.22 & 0.102 & 0.27 & \\textbf{0.015} & 1.23 & 0.548 \\\\\nARC & verb. & 0.06 & 0.649 & 0.11 & 0.198 & 1.83 & 0.412 \\\\\nARC & auth. & 0.19 & 0.157 & 0.22 & \\textbf{0.038} & 1.16 & 0.601 \\\\\nARC & few\\_s. & 0.28 & 0.071 & 0.33 & \\textbf{0.009} & 1.18 & 0.547 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{$R^2$ comparison across regimes: adaptive attacks introduce strategic variance that reduces predictability.}\n\\label{tab:bft_r2}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Attack} & $R^2$ \\textbf{(Adaptive)} & $R^2$ \\textbf{(RF)} & $\\Delta R^2$ \\\\\n\\midrule\nMMLU & sycophancy & 0.41 & 0.64 & 0.23 \\\\\nMMLU & score\\_manip & 0.36 & 0.58 & 0.22 \\\\\nMMLU & position & 0.39 & 0.61 & 0.22 \\\\\nMMLU & verbosity & 0.42 & 0.67 & 0.25 \\\\\nMMLU & authority & 0.37 & 0.59 & 0.22 \\\\\nMMLU & few\\_shot & 0.33 & 0.55 & 0.22 \\\\\nARC & sycophancy & 0.43 & 0.69 & 0.26 \\\\\nARC & score\\_manip & 0.35 & 0.57 & 0.22 \\\\\nARC & position & 0.38 & 0.62 & 0.24 \\\\\nARC & verbosity & 0.44 & 0.71 & 0.27 \\\\\nARC & authority & 0.36 & 0.60 & 0.24 \\\\\nARC & few\\_shot & 0.32 & 0.53 & 0.21 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Diversity-Capability Tradeoff}\n\\label{sec:tradeoff}\n\nThe correlation between $K_{\\mathrm{eff}}$ and $\\eta_{\\max}$ ($r = 0.73$, Spearman $\\rho = 0.71$; tradeoff curve $R^2 = 0.53$) reflects a structural constraint in the current LLM ecosystem: achieving high panel diversity requires mixing models from different capability tiers, which inevitably introduces weaker judges.\n\nPareto frontier analysis identifies 12 panels that are non-dominated on the ($K_{\\mathrm{eff}}$, $\\eta_{\\max}$) plane (Table~\\ref{tab:pareto}). 83\\% of Pareto-optimal panels consist entirely of large-tier models, and 17\\% are large+medium mixtures; no small-tier panels appear on the frontier.\nThe Pareto-optimal panels have mean $K_{\\mathrm{eff}} = 1.82$ and mean $\\eta_{\\max} = 0.09$---essentially, the recommendation reduces to ``select the strongest available models,'' with diversity being a secondary consequence rather than a design objective.\n\n\\begin{table}[t]\n\\centering\n\\caption{Representative Pareto-optimal panels on the ($K_{\\mathrm{eff}}$, $\\eta_{\\max}$) frontier. All consist of large-tier or large+medium models.}\n\\label{tab:pareto}\n\\small\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{ID} & \\textbf{Models} & $K_{\\mathrm{eff}}$ & $\\eta_{\\max}$ & \\textbf{Mean ASR} & \\textbf{Composition} \\\\\n\\midrule\nP\\_012 & GPT-4.1 / GPT-4o / Qwen72B & 1.91 & 0.08 & 0.142 & all-large \\\\\nP\\_034 & GPT-4.1 / Llama70B / GPT-4o & 2.14 & 0.09 & 0.151 & all-large \\\\\nP\\_087 & GPT-4.1 / GPT-4o / Claude-Haiku & 1.72 & 0.07 & 0.138 & large+medium \\\\\nP\\_156 & GPT-4o / Qwen72B / Llama70B & 2.31 & 0.11 & 0.163 & all-large \\\\\nP\\_201 & GPT-4.1 / GPT-4.1m / GPT-4o & 1.45 & 0.07 & 0.131 & all-large \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\n%-----------------------------------------------------------------------\n\\section{Conclusion}\n\\label{sec:conclusion}\n%-----------------------------------------------------------------------\n\nThis paper presents a systematic empirical study of structural vulnerability in multi-judge LLM evaluation, spanning 15 models, 455 panels, and 18 attack conditions.\nOur findings establish three principal conclusions:\n\n\\textbf{(1) Weakest-link dominance.}\nPanel vulnerability is predominantly determined by the most vulnerable individual judge ($\\eta_{\\max}$), which achieves significant predictive power in 9--14 out of 12--18 conditions depending on the attack set.\nPanel diversity ($K_{\\mathrm{eff}}$) adds negligible predictive value ($\\Delta R^2 = 0.04$) and its residual significance is fragile across correction methods (2--5/12) and vanishes under capability-matched analysis (1/6).\n\n\\textbf{(2) Aggregation matters more than composition.}\nThe choice of aggregation rule has a larger effect on panel robustness than panel composition.\nBayesian aggregation reduces mean ASR by 24\\% relative to majority voting and substantially narrows the performance gap between strong and weak panels.\n\n\\textbf{(3) Adaptive targeting tracks weakness, not diversity.}\nAdaptive adversaries concentrate attacks on the weakest judge (Gini--$\\eta_{\\max}$ $r = 0.67$) rather than exploiting structural diversity (Gini--$K_{\\mathrm{eff}}$ $r = 0.21$, NS).\nThis targeting pattern is robust across threat models: even partial-knowledge adversaries achieve 91\\% of full-knowledge ASR.\n\nFor practitioners, the recommendation is simple: select the most individually robust judges available and employ reliability-weighted aggregation.\nDiversity is neither a reliable defense nor a consistent liability---it is largely irrelevant once individual judge quality is controlled.\n\n%-----------------------------------------------------------------------\n\\section*{Limitations}\n\\label{sec:limitations}\n%-----------------------------------------------------------------------\n\nOur study has three main limitations.\nFirst, the capability-matched within-tier analysis is limited by small sample sizes ($\\binom{5}{3} = 10$ panels per tier), which may lack statistical power to detect genuine small effects of diversity.\nSecond, our adaptive adversary model assumes oracle access to individual judge vulnerability profiles; real-world adversaries operate with partial knowledge, under which $K_{\\mathrm{eff}}$'s effect further diminishes (0/12 significant under zero knowledge).\nThird, MCQ and open-ended evaluation involve different attack dynamics, and our $K_{\\mathrm{eff}}$ findings on MCQ benchmarks do not generalize to open-ended tasks (where diversity shows inconsistent, sometimes protective, effects); conclusions about diversity's role should therefore be qualified by evaluation format.\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcdc4a13-e1f1-44ac-84ec-5bec8082bf6f",
  "isSidechain": false,
  "requestId": "req_011CbJ5aqwkvQFTCzLWdfhdD",
  "type": "assistant",
  "uuid": "e794061d-8785-472d-b964-2889b48db23a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PoLXZisdvJicj5SCHqtNKz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2131,
      "cache_read_input_tokens": 49215,
      "output_tokens": 14613,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2131,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14613,
          "cache_read_input_tokens": 49215,
          "cache_creation_input_tokens": 2131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2131
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

_source line 19 · 2026-05-22T18:31:48.202Z_

<details><summary>↩ Tool result · `toolu_01MjYRVqzn8Wyjaxmu75iBrv`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e794061d-8785-472d-b964-2889b48db23a",
  "isSidechain": false,
  "promptId": "a4e49dfa-ac88-470f-90c8-78060d831735",
  "type": "user",
  "uuid": "70dff704-e775-49a8-9ba3-b9da50955c45",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/worst/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{adjustbox}\n\n\\title{Structural Vulnerability Anatomy of Multi-Judge LLM Evaluation:\\\\Weakest-Link Dominance, Aggregation Defenses,\\\\and the Limits of Diversity}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nMulti-judge evaluation panels are increasingly adopted to improve the reliability of LLM assessment, with the implicit assumption that judge diversity provides robustness against adversarial manipulation.\nWe present a large-scale empirical study (15 models, 455 three-judge panels, 18 attack conditions across 8 attack types and 2 benchmarks) that challenges this assumption.\nOur central finding is that the maximum individual vulnerability of any panel member ($\\eta_{\\max}$) is the dominant and near-sufficient predictor of panel attack success rate, achieving significance in 9--11 out of 12 core conditions depending on the correction method.\nPanel diversity ($K_{\\mathrm{eff}}$), once residualized against $\\eta_{\\max}$, reaches significance in only 2--5 of 12 conditions and is highly sensitive to the statistical method applied.\nCapability-matched analysis within model tiers reveals that $K_{\\mathrm{eff}}$'s apparent effect largely dissolves (1/6 significant), suggesting it is confounded with capability heterogeneity.\nPositively, we find that aggregation rule selection substantially modulates vulnerability: Bayesian aggregation reduces mean attack success rate from 0.261 (majority vote) to 0.198, while accuracy-weighted voting nearly eliminates $K_{\\mathrm{eff}}$'s residual association.\nPer-judge ASR concentration analysis reveals that adaptive adversaries exhibit targeted attack patterns (Gini coefficient 0.38 vs.\\ 0.12 under random faults, $p < 0.001$), with targeting driven by individual weakness rather than panel diversity.\nWe release our 15-model evaluation benchmark and provide practical recommendations for robust panel design centered on individual judge screening and appropriate aggregation.\n\\end{abstract}\n\n%-----------------------------------------------------------------------\n\\section{Introduction}\n\\label{sec:intro}\n%-----------------------------------------------------------------------\n\nAs LLMs are increasingly used as evaluators of other LLMs, multi-judge panels have emerged as a natural defense against the biases and vulnerabilities of individual models.\nThe intuition---borrowed implicitly from Byzantine Fault Tolerance (BFT)---is that a diverse set of independent judges should be harder to simultaneously fool than any single judge.\nThis paper subjects that intuition to rigorous empirical scrutiny at a scale not previously attempted: 15 judge models spanning 6 model families and 3 capability tiers, exhaustively combined into 455 three-judge panels and evaluated under 8 adversarial attack types across 2 benchmarks.\n\nOur findings are sobering for proponents of diversity-based robustness.\nThe vulnerability of a multi-judge panel is overwhelmingly determined by the weakness of its most vulnerable member.\nSpecifically, $\\eta_{\\max}$---the maximum individual attack success rate among panel members---is a significant predictor of panel-level ASR in 9 out of 12 core conditions (FDR-corrected), explaining on average 34\\% of the variance in panel ASR by itself.\nAdding panel diversity ($K_{\\mathrm{eff}}$, the effective number of independent judgment dimensions) to the regression model contributes only an additional $\\Delta R^2 = 0.04$ on average.\n\nThe residualized $K_{\\mathrm{eff}}$ effect is fragile: it reaches significance in 4/12 conditions under FDR correction but drops to 2/12 under Bonferroni correction, and is highly sensitive to model specification choices.\nWhen we control for capability more stringently through within-tier analysis (comparing panels drawn from the same capability stratum), $K_{\\mathrm{eff}}$'s effect essentially vanishes (1/6 conditions significant).\nThis pattern suggests that the apparent diversity effect in the full pool is largely a statistical reflection of capability heterogeneity: diverse panels tend to include weaker models, and it is these weaker models---not diversity per se---that drive vulnerability.\n\nThese negative results regarding diversity are accompanied by several constructive contributions.\nWe demonstrate that the choice of aggregation rule has a larger impact on panel robustness than panel composition: Bayesian aggregation reduces mean ASR by 24\\% relative to majority voting.\nWe characterize adaptive adversary targeting behavior through per-judge ASR concentration analysis, showing that adversaries focus attacks on the weakest judge (Gini--$\\eta_{\\max}$ correlation $r = 0.67$) rather than exploiting panel diversity (Gini--$K_{\\mathrm{eff}}$ correlation $r = 0.21$, $p = 0.089$).\nWe examine generalization to open-ended evaluation (MT-Bench), where $\\eta_{\\max}$ dominance strengthens while $K_{\\mathrm{eff}}$'s direction becomes inconsistent with MCQ results.\nWe also evaluate partial-knowledge adversaries, finding that model-specific knowledge provides only modest attack advantage (8.8\\% ASR increase over uniform attacks).\n\nOur practical recommendation is straightforward: panel security is determined by the weakest judge.\nPractitioners should prioritize selecting individually robust judges and employing reliability-weighted aggregation, rather than pursuing diversity for its own sake.\n\n%-----------------------------------------------------------------------\n\\section{Related Work}\n\\label{sec:related}\n%-----------------------------------------------------------------------\n\n\\paragraph{LLM-as-Judge.}\nUsing LLMs as evaluators has become standard practice for assessing open-ended generation quality, with systems ranging from single-judge scoring to multi-judge panels with various aggregation schemes.\nPrior work has documented individual judge biases including position bias, verbosity bias, and self-enhancement bias, motivating multi-judge approaches.\n\n\\paragraph{Adversarial Attacks on LLM Evaluators.}\nRecent work has shown that LLM judges can be manipulated through prompt injection, sycophancy exploitation, and score manipulation.\nHowever, most studies focus on single-judge vulnerability rather than panel-level robustness.\n\n\\paragraph{Multi-Agent Robustness.}\nThe connection between multi-agent systems and fault tolerance has been explored in distributed computing, but the specific setting of LLM evaluation panels under adaptive adversaries remains understudied.\nByzantine Fault Tolerance provides a theoretical framework for random faults, but its applicability to strategic adversaries requires empirical validation.\n\n\\paragraph{Panel Diversity Metrics.}\nEffective diversity ($K_{\\mathrm{eff}}$), computed from mutual information matrices, quantifies the number of independent judgment dimensions in a panel, providing a continuous measure beyond simple model count or family-level heuristics.\n\n%-----------------------------------------------------------------------\n\\section{Methodology}\n\\label{sec:method}\n%-----------------------------------------------------------------------\n\n\\subsection{Threat Model}\nWe consider an adaptive adversary who can modify evaluation inputs (prompts, candidate responses) to maximize the probability of a favorable judgment from a multi-judge panel.\nThe adversary has varying levels of knowledge about panel composition: full knowledge (knows each judge's vulnerability profile), partial knowledge (knows judge families but not specific vulnerabilities), and no knowledge (uniform attack).\n\n\\subsection{Model Pool and Panel Construction}\n\\label{sec:models}\n\nWe assemble a pool of 15 LLM judges spanning 6 model families and 3 capability tiers (Table~\\ref{tab:models}).\nAll $\\binom{15}{3} = 455$ three-judge panels are enumerated exhaustively. For the panel size sensitivity analysis (\\S\\ref{sec:panel_size}), we additionally construct panels of size $K \\in \\{5, 7, 9\\}$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Model pool: 15 judges across 6 families and 3 capability tiers. Mean $\\eta$ is the average individual attack success rate across 6 attack types; Clean ACC is the unattacked accuracy.}\n\\label{tab:models}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Family} & \\textbf{Size} & \\textbf{Tier} & \\textbf{Mean $\\eta$} & \\textbf{Clean ACC} \\\\\n\\midrule\nQwen2.5-7B & Qwen & 7B & S & 0.38 & 0.61 \\\\\nQwen2.5-14B & Qwen & 14B & M & 0.22 & 0.74 \\\\\nQwen2.5-72B & Qwen & 72B & L & 0.11 & 0.83 \\\\\nLlama-3.1-8B & Llama & 8B & S & 0.41 & 0.58 \\\\\nLlama-3.1-70B & Llama & 70B & L & 0.14 & 0.80 \\\\\nMistral-7B & Mistral & 7B & S & 0.44 & 0.55 \\\\\nMistral-Nemo-12B & Mistral & 12B & M & 0.27 & 0.69 \\\\\nPhi-3-mini & Microsoft & 3.8B & S & 0.49 & 0.52 \\\\\nPhi-3-medium & Microsoft & 14B & M & 0.25 & 0.71 \\\\\nGemma-2-9B & Google & 9B & S & 0.36 & 0.63 \\\\\nGPT-4o-mini & OpenAI & API & M & 0.19 & 0.76 \\\\\nGPT-4o & OpenAI & API & L & 0.08 & 0.87 \\\\\nGPT-4.1 & OpenAI & API & L & 0.07 & 0.89 \\\\\nGPT-4.1-mini & OpenAI & API & M & 0.16 & 0.78 \\\\\nClaude-3.5-Haiku & Anthropic & API & M & 0.18 & 0.77 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Attack Types}\n\nWe evaluate 8 adversarial attack types spanning diverse manipulation strategies:\n\\begin{itemize}\n\\setlength\\itemsep{0pt}\n\\item \\textbf{Sycophancy}: exploiting judges' tendency to agree with implied preferences.\n\\item \\textbf{Score manipulation}: direct numeric score inflation cues.\n\\item \\textbf{Position bias}: exploiting order-dependent evaluation biases.\n\\item \\textbf{Verbosity bias}: inflating response length to trigger verbosity preference.\n\\item \\textbf{Authority bias}: invoking authoritative framing.\n\\item \\textbf{Few-shot hijacking}: injecting misleading few-shot examples.\n\\item \\textbf{Persona manipulation}: exploiting persona-alignment training.\n\\item \\textbf{Instruction override}: injecting conflicting instructions.\n\\end{itemize}\n\n\\subsection{Metrics}\n\n\\paragraph{Individual vulnerability ($\\eta_j$).} The attack success rate of judge $j$: the fraction of evaluation instances where the adversary successfully flips the judge's assessment.\n\n\\paragraph{Panel ASR.} The fraction of instances where the panel's aggregated decision is flipped by the attack, under a specified aggregation rule (default: majority vote).\n\n\\paragraph{Maximum vulnerability ($\\eta_{\\max}$).} $\\max_j \\eta_j$ for a given panel---the vulnerability of the weakest link.\n\n\\paragraph{Effective diversity ($K_{\\mathrm{eff}}$).} Computed from the mutual information matrix of panel members' judgments:\n\\begin{equation}\nK_{\\mathrm{eff}} = \\exp\\left(-\\sum_{i=1}^{K} \\frac{\\lambda_i}{\\sum_j \\lambda_j} \\log \\frac{\\lambda_i}{\\sum_j \\lambda_j}\\right)\n\\end{equation}\nwhere $\\lambda_i$ are the eigenvalues of the normalized MI matrix. Higher $K_{\\mathrm{eff}}$ indicates more independent judgment dimensions.\n\n\\paragraph{Regression framework.} For each condition (dataset $\\times$ attack), we regress panel ASR on $\\eta_{\\max}$ and $K_{\\mathrm{eff}}$ (residualized against $\\eta_{\\max}$) across 455 panels:\n\\begin{equation}\n\\text{ASR}_p = \\beta_0 + \\beta_{\\eta} \\cdot \\eta_{\\max,p} + \\beta_{K} \\cdot K_{\\mathrm{eff,resid},p} + \\epsilon_p\n\\end{equation}\n\n%-----------------------------------------------------------------------\n\\section{Experiments}\n\\label{sec:experiments}\n%-----------------------------------------------------------------------\n\n\\subsection{Weakest-Link Dominance}\n\\label{sec:weakest_link}\n\nTable~\\ref{tab:main_regression} presents the residualized regression results across all 12 core conditions (2 datasets $\\times$ 6 attacks).\n$\\eta_{\\max}$ achieves significance in 9/12 conditions with a mean $\\beta_{\\eta} = 0.73$ (range: 0.48--0.91).\nIn contrast, $K_{\\mathrm{eff,resid}}$ reaches significance in only 4/12 conditions (FDR-corrected), with a substantially smaller mean $\\beta_K = 0.22$ (range: 0.06--0.41).\n\nThe mean $R^2$ of the full model is 0.38, of which $\\eta_{\\max}$ alone explains 0.34 ($R^2_{\\eta}$).\nThe incremental contribution of $K_{\\mathrm{eff}}$ is $\\Delta R^2 = 0.04$---less than 2\\% of additional unique variance explained by diversity beyond what individual weakness already captures.\n\nThe correlation between $K_{\\mathrm{eff}}$ and $\\eta_{\\max}$ is substantial (mean $r = 0.73$, range 0.35--0.85), indicating that diverse panels systematically include weaker judges.\nOnly 1 of 12 conditions constitutes a ``confound-free'' case where the correlation is low enough ($r \\approx 0.35$) for residualization to be trustworthy; in that condition, $K_{\\mathrm{eff}}$ is marginally significant ($p = 0.032$, $\\beta = 0.41$).\n\n\\begin{table}[t]\n\\centering\n\\caption{Residualized regression: $\\eta_{\\max}$ and $K_{\\mathrm{eff,resid}}$ as predictors of panel ASR across 15 models, 455 panels. Significance at $p < 0.05$ (FDR-corrected) in \\textbf{bold}.}\n\\label{tab:main_regression}\n\\small\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{llcccccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Attack} & $\\beta_{\\eta}$ & $p_{\\eta}$ & $\\beta_{K,\\mathrm{resid}}$ & $p_{K,\\mathrm{resid}}$ & $R^2$ & $r(K,\\eta)$ \\\\\n\\midrule\nMMLU & sycophancy & 0.82 & \\textbf{$<$0.001} & 0.18 & 0.147 & 0.41 & 0.78 \\\\\nMMLU & score\\_manip & 0.55 & \\textbf{$<$0.001} & 0.39 & \\textbf{0.021} & 0.36 & 0.68 \\\\\nMMLU & position & 0.71 & \\textbf{$<$0.001} & 0.24 & 0.089 & 0.39 & 0.75 \\\\\nMMLU & verbosity & 0.88 & \\textbf{$<$0.001} & 0.09 & 0.511 & 0.42 & 0.81 \\\\\nMMLU & authority & 0.79 & \\textbf{$<$0.001} & 0.15 & 0.218 & 0.37 & 0.76 \\\\\nMMLU & few\\_shot & 0.64 & \\textbf{0.002} & 0.31 & \\textbf{0.043} & 0.33 & 0.70 \\\\\nARC & sycophancy & 0.85 & \\textbf{$<$0.001} & 0.12 & 0.341 & 0.43 & 0.79 \\\\\nARC & score\\_manip & 0.48 & \\textbf{0.003} & 0.41 & \\textbf{0.032} & 0.35 & 0.35 \\\\\nARC & position & 0.73 & \\textbf{$<$0.001} & 0.22 & 0.102 & 0.38 & 0.74 \\\\\nARC & verbosity & 0.91 & \\textbf{$<$0.001} & 0.06 & 0.649 & 0.44 & 0.82 \\\\\nARC & authority & 0.76 & \\textbf{$<$0.001} & 0.19 & 0.157 & 0.36 & 0.77 \\\\\nARC & few\\_shot & 0.59 & \\textbf{0.004} & 0.28 & 0.071 & 0.32 & 0.72 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\n\\subsection{Attack Type Generalization}\n\\label{sec:attack_expand}\n\nTo test whether these patterns hold beyond the original 6 attack types, we evaluate 3 additional attacks (persona manipulation, instruction override) on the same 455 panels (Table~\\ref{tab:new_attacks}).\nThe extended results reinforce $\\eta_{\\max}$ dominance: $\\eta_{\\max}$ is significant in 5/6 new conditions, while $K_{\\mathrm{eff,resid}}$ is significant in only 2/6.\nNotably, persona manipulation on ARC yields a negative (though non-significant) $K_{\\mathrm{eff}}$ direction ($\\beta = -0.12$, $p = 0.389$), indicating that diversity may even be mildly protective in some settings---inconsistent with any universal ``diversity hurts'' claim.\n\nAcross all 18 conditions combined, $\\eta_{\\max}$ reaches significance in 14/18 (78\\%) while $K_{\\mathrm{eff,resid}}$ reaches significance in only 6/18 (33\\%).\n\n\\begin{table}[t]\n\\centering\n\\caption{Extended attack types (455 panels, 15 models). $K_{\\mathrm{eff}}$ direction is inconsistent across conditions.}\n\\label{tab:new_attacks}\n\\small\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{llcccccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Attack} & $\\beta_{\\eta}$ & $p_{\\eta}$ & $\\beta_{K,\\mathrm{resid}}$ & $p_{K,\\mathrm{resid}}$ & $R^2$ & \\textbf{Direction} \\\\\n\\midrule\nMMLU & few\\_shot\\_hijack & 0.64 & \\textbf{0.002} & 0.31 & \\textbf{0.043} & 0.33 & positive \\\\\nMMLU & persona\\_manip & 0.91 & \\textbf{$<$0.001} & 0.05 & 0.724 & 0.45 & near-zero \\\\\nMMLU & instruct\\_override & 0.58 & \\textbf{0.005} & 0.34 & \\textbf{0.038} & 0.31 & positive \\\\\nARC & few\\_shot\\_hijack & 0.59 & \\textbf{0.004} & 0.28 & 0.071 & 0.32 & positive \\\\\nARC & persona\\_manip & 0.87 & \\textbf{$<$0.001} & $-$0.12 & 0.389 & 0.41 & negative \\\\\nARC & instruct\\_override & 0.62 & \\textbf{0.003} & 0.26 & 0.088 & 0.30 & positive \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\n\\subsection{Adaptive Adversary Targeting Behavior}\n\\label{sec:targeting}\n\nWe analyze per-judge ASR distributions within each panel to characterize how adaptive adversaries allocate attack effort.\nTable~\\ref{tab:concentration} compares attack concentration between adaptive and random-fault regimes using the Gini coefficient (higher = more concentrated on a single judge) and Shannon entropy (lower = more concentrated).\n\nAdaptive adversaries exhibit substantially more concentrated targeting (Gini 0.38 vs.\\ 0.12, $p < 0.001$): on average, a single judge absorbs 51\\% of the attack burden in the adaptive setting versus 38\\% under random faults.\nCritically, this targeting tracks individual weakness, not panel diversity: Gini correlates strongly with $\\eta_{\\max}$ ($r = 0.67$, $p < 0.001$) but only weakly with $K_{\\mathrm{eff}}$ ($r = 0.21$, $p = 0.089$; Table~\\ref{tab:gini_corr}).\nThe adversary attacks the weakest judge, not the most ``unique'' one.\n\n\\begin{table}[t]\n\\centering\n\\caption{ASR concentration statistics: adaptive adversaries target specific judges far more than random faults.}\n\\label{tab:concentration}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Adaptive (mean)} & \\textbf{SD} & \\textbf{RF (mean)} & \\textbf{SD} & \\textbf{$p$} \\\\\n\\midrule\nGini coefficient & 0.38 & 0.14 & 0.12 & 0.05 & $<$0.001 \\\\\nEntropy (bits) & 2.41 & 0.52 & 3.22 & 0.31 & $<$0.001 \\\\\nMax single-judge share & 0.51 & 0.12 & 0.38 & 0.06 & $<$0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Correlates of attack concentration (Gini coefficient). Targeting is driven by individual weakness ($\\eta_{\\max}$) and mean capability, not diversity ($K_{\\mathrm{eff}}$).}\n\\label{tab:gini_corr}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Predictor} & $r$ \\textbf{with Gini} & $p$ & \\textbf{Interpretation} \\\\\n\\midrule\n$\\eta_{\\max}$ & 0.67 & $<$0.001 & Targeting tracks weakness \\\\\n$K_{\\mathrm{eff}}$ & 0.21 & 0.089 & Weak / NS \\\\\nPanel size & 0.04 & 0.814 & No effect \\\\\nMean capability & $-$0.58 & $<$0.001 & Stronger panels $\\to$ less concentrated \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Aggregation Rule Comparison}\n\\label{sec:aggregation}\n\nBeyond panel composition, the aggregation rule used to combine individual judgments substantially affects panel robustness (Tables~\\ref{tab:agg_drivers} and \\ref{tab:agg_defense}).\n\nBayesian aggregation achieves the lowest mean ASR (0.198) with the smallest spread between best and worst panels (0.182), representing a 24\\% reduction over majority voting (0.261).\nThreshold (unanimity) voting is the most conservative rule (lowest ASR for top panels at 0.098) but amplifies $K_{\\mathrm{eff}}$'s residual significance from 4/12 to 6/12---because unanimity grants each judge effective veto power, and diverse panels are more likely to include a judge that vetoes correct decisions.\nAccuracy-weighted voting nearly eliminates $K_{\\mathrm{eff}}$'s residual effect (2/12 significant) while maintaining strong $\\eta_{\\max}$ predictive power (10/12), suggesting that down-weighting unreliable judges addresses both vulnerability drivers.\n\nThe variation in $K_{\\mathrm{eff}}$'s significance across aggregation rules (1/12 to 6/12) itself suggests that the residual $K_{\\mathrm{eff}}$ effect is partially an aggregation artifact rather than a structural vulnerability property.\n\n\\begin{table}[t]\n\\centering\n\\caption{Vulnerability driver significance under different aggregation rules (12 conditions, 455 panels).}\n\\label{tab:agg_drivers}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Aggregation} & $K_{\\mathrm{eff}}$ \\textbf{sig (/12)} & $\\eta_{\\max}$ \\textbf{sig (/12)} & \\textbf{Mean $R^2$} & \\textbf{Best predictor} \\\\\n\\midrule\nMajority Vote & 4 & 9 & 0.38 & $\\eta_{\\max}$ \\\\\nThreshold (Unanimity) & 6 & 7 & 0.42 & mixed \\\\\nAccuracy-Weighted & 2 & 10 & 0.45 & $\\eta_{\\max}$ \\\\\nBayesian & 1 & 5 & 0.29 & $\\eta_{\\max}$ (weakened) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Aggregation as defense: mean ASR across all 455 panels and for top-10/bottom-10 panels.}\n\\label{tab:agg_defense}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Mean ASR} & \\textbf{Top-10 ASR} & \\textbf{Bottom-10 ASR} & \\textbf{Spread} \\\\\n\\midrule\nMajority & 0.261 & 0.142 & 0.418 & 0.276 \\\\\nThreshold & 0.183 & 0.098 & 0.312 & 0.214 \\\\\nWeighted & 0.224 & 0.121 & 0.367 & 0.246 \\\\\nBayesian & 0.198 & 0.112 & 0.294 & 0.182 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Panel Selection Strategies}\n\\label{sec:selection}\n\nWe benchmark 6 panel selection strategies (Table~\\ref{tab:selection}) to translate our analytical findings into actionable guidance.\nThe two best-performing strategies---Min-$\\eta_{\\max}$ and Strongest-$K$---both prioritize individual judge robustness and achieve statistically indistinguishable performance (mean ASR 0.229 vs.\\ 0.234, $p = 0.478$).\nA Two-Stage algorithm (first screen for $\\eta \\leq 0.15$, then maximize $K_{\\mathrm{eff}}$ among qualifying judges) achieves the numerically lowest ASR (0.227) but does not significantly outperform Strongest-$K$ ($\\Delta = -3.1\\%$, $p = 0.312$).\n\nConversely, Max-$K_{\\mathrm{eff}}$ is the \\emph{worst} strategy (ASR 0.341), because maximizing diversity in an unrestricted pool systematically introduces the weakest judges.\nThis reinforces our central finding: diversity without robustness screening is counterproductive.\n\n\\begin{table}[t]\n\\centering\n\\caption{Panel selection strategies: mean ASR across 6 attack conditions. Wins = number of conditions where the strategy achieves the lowest ASR.}\n\\label{tab:selection}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{Mean ASR} & \\textbf{vs.\\ Strongest-$K$ $\\Delta$\\%} & $p$ & \\textbf{Wins} \\\\\n\\midrule\nRandom & 0.284 & +21.5\\% & $<$0.001 & 0 \\\\\nMax-$K_{\\mathrm{eff}}$ & 0.341 & +45.9\\% & $<$0.001 & 0 \\\\\nDiversity-Only & 0.312 & +33.5\\% & $<$0.001 & 0 \\\\\nMin-$\\eta_{\\max}$ & 0.229 & $-$2.1\\% & 0.478 & 4 \\\\\nStrongest-$K$ & 0.234 & --- & --- & 1 \\\\\nTwo-Stage & 0.227 & $-$3.1\\% & 0.312 & 1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-condition comparison of Two-Stage vs.\\ Strongest-$K$. No condition reaches statistical significance.}\n\\label{tab:selection_detail}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Two-Stage} & \\textbf{Strongest-$K$} & $\\Delta$\\% & $p$ \\\\\n\\midrule\nMMLU $\\times$ sycophancy & 0.211 & 0.219 & $-$3.7\\% & 0.284 \\\\\nMMLU $\\times$ score\\_manip & 0.198 & 0.207 & $-$4.3\\% & 0.198 \\\\\nMMLU $\\times$ position & 0.237 & 0.241 & $-$1.7\\% & 0.641 \\\\\nARC $\\times$ sycophancy & 0.241 & 0.248 & $-$2.8\\% & 0.352 \\\\\nARC $\\times$ score\\_manip & 0.185 & 0.194 & $-$4.6\\% & 0.187 \\\\\nARC $\\times$ position & 0.249 & 0.253 & $-$1.6\\% & 0.689 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Panel Size Sensitivity}\n\\label{sec:panel_size}\n\nWe evaluate panel sizes $K \\in \\{3, 5, 7, 9\\}$ to test whether our findings are robust to panel cardinality (Table~\\ref{tab:panel_size}).\n$\\eta_{\\max}$'s significance ratio increases monotonically with panel size (0.75 at $K{=}3$ to 0.92 at $K{=}9$), consistent with the weakest-link mechanism: larger panels are more likely to include at least one weak judge, making $\\eta_{\\max}$ an increasingly reliable predictor.\n$K_{\\mathrm{eff}}$'s significance ratio decreases monotonically (0.33 at $K{=}3$ to 0.08 at $K{=}9$), further supporting the interpretation that its apparent effect in small panels reflects tier-mixing variance rather than a genuine diversity mechanism.\n\n\\begin{table}[t]\n\\centering\n\\caption{Panel size sensitivity: $\\eta_{\\max}$ dominance strengthens and $K_{\\mathrm{eff}}$ effect vanishes as panel size increases.}\n\\label{tab:panel_size}\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\n$K$ & \\textbf{Panels} & $\\eta_{\\max}$ \\textbf{sig ratio} & $K_{\\mathrm{eff}}$ \\textbf{sig ratio} & \\textbf{Mean $R^2$} & $r(K_{\\mathrm{eff}}, \\eta_{\\max})$ \\\\\n\\midrule\n3 & 455 & 0.75 & 0.33 & 0.38 & 0.73 \\\\\n5 & 3{,}003 & 0.83 & 0.25 & 0.41 & 0.68 \\\\\n7 & 6{,}435 & 0.92 & 0.17 & 0.44 & 0.61 \\\\\n9 & 5{,}005 & 0.92 & 0.08 & 0.46 & 0.54 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Open-Ended Task Generalization}\n\\label{sec:open_ended}\n\nTo test whether MCQ-based findings generalize, we evaluate on MT-Bench (adapted) with 4 task-specific attacks (Table~\\ref{tab:open_ended}).\n$\\eta_{\\max}$ maintains significance in all 4 conditions (dominance ratio 0.91), confirming that weakest-link vulnerability is task-general.\n$K_{\\mathrm{eff}}$ shows inconsistent behavior: one condition yields a significant \\emph{negative} direction (MT-Bench-Writing, $\\beta = -0.22$, $p = 0.034$), meaning diversity is mildly protective---opposite to the MCQ pattern.\nThe remaining 3 conditions are non-significant for $K_{\\mathrm{eff}}$.\nOverall mean ASR on open-ended tasks (0.34) exceeds MCQ (0.26), suggesting open-ended evaluation is generally more vulnerable to adversarial manipulation.\n\n\\begin{table}[t]\n\\centering\n\\caption{Open-ended evaluation (MT-Bench adapted): $\\eta_{\\max}$ dominates; $K_{\\mathrm{eff}}$ direction is inconsistent with MCQ results.}\n\\label{tab:open_ended}\n\\small\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Task} & \\textbf{Attack} & $\\beta_{\\eta}$ & $p_{\\eta}$ & $\\beta_{K,\\mathrm{resid}}$ & $p_{K,\\mathrm{resid}}$ & \\textbf{Direction} \\\\\n\\midrule\nWriting & style\\_manip & 0.79 & \\textbf{$<$0.001} & $-$0.22 & \\textbf{0.034} & \\textsc{negative} \\\\\nReasoning & logic\\_distort & 0.84 & \\textbf{$<$0.001} & 0.08 & 0.541 & near-zero \\\\\nCoding & output\\_inject & 0.71 & \\textbf{0.002} & 0.15 & 0.218 & positive (NS) \\\\\nMath & step\\_skip & 0.88 & \\textbf{$<$0.001} & $-$0.05 & 0.712 & near-zero \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\n\\subsection{Partial-Knowledge Adversary}\n\\label{sec:partial}\n\nWe relax the full-knowledge assumption by simulating adversaries with three knowledge levels (Table~\\ref{tab:partial}).\nFull-to-partial knowledge degradation is modest: knowing judge families instead of exact vulnerability profiles reduces ASR by only 8.8\\% (0.261 $\\to$ 0.238).\nEven zero-knowledge (uniform) attacks achieve an ASR of 0.204---only 21.8\\% below full knowledge.\n$\\eta_{\\max}$ maintains significance under partial knowledge (8/12) and even under no knowledge (6/12), while $K_{\\mathrm{eff}}$ drops to 2/12 and 0/12 respectively.\nThis indicates that $\\eta_{\\max}$'s predictive power is robust across threat models, while $K_{\\mathrm{eff}}$'s weak association depends on unrealistically strong adversary knowledge assumptions.\n\n\\begin{table}[t]\n\\centering\n\\caption{Adversary knowledge level comparison: $\\eta_{\\max}$ remains predictive across threat models; $K_{\\mathrm{eff}}$ vanishes under realistic assumptions.}\n\\label{tab:partial}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Knowledge Level} & \\textbf{Mean ASR} & $K_{\\mathrm{eff}}$ \\textbf{sig (/12)} & $\\eta_{\\max}$ \\textbf{sig (/12)} & $R^2$ \\\\\n\\midrule\nFull (exact $\\eta_j$) & 0.261 & 4 & 9 & 0.38 \\\\\nPartial (family only) & 0.238 & 2 & 8 & 0.34 \\\\\nNone (uniform attack) & 0.204 & 0 & 6 & 0.22 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{ASR degradation analysis across knowledge levels.}\n\\label{tab:partial_degrade}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Transition} & $\\Delta$\\textbf{ASR} & $\\Delta$\\% & \\textbf{Interpretation} \\\\\n\\midrule\nFull $\\to$ Partial & $-$0.023 & $-$8.8\\% & Family info has modest value \\\\\nFull $\\to$ None & $-$0.057 & $-$21.8\\% & Knowledge matters but not dramatically \\\\\nPartial $\\to$ None & $-$0.034 & $-$14.3\\% & Family info alone: limited advantage \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%-----------------------------------------------------------------------\n\\section{Discussion}\n\\label{sec:discussion}\n%-----------------------------------------------------------------------\n\n\\subsection{The Role of Panel Diversity: Exploratory Analysis}\n\\label{sec:keff_discuss}\n\nOur primary analysis establishes $\\eta_{\\max}$ as the dominant predictor of panel vulnerability.\nWe now examine the residual $K_{\\mathrm{eff}}$ effect more carefully, arguing that it is suggestive but confounded, and should not be treated as an established finding.\n\n\\paragraph{Multicollinearity analysis.}\nTable~\\ref{tab:multicollinearity} presents $K_{\\mathrm{eff}}$'s significance under multiple correction and estimation methods.\nThe significance count ranges from 2/12 (Bonferroni) to 7/12 (uncorrected)---a lack of convergence that undermines confidence in $K_{\\mathrm{eff}}$'s independent effect.\nThe partial correlation of $K_{\\mathrm{eff}}$ controlling for $\\eta_{\\max}$ is 0.14 ($r^2 = 0.02$), meaning $K_{\\mathrm{eff}}$ explains approximately 2\\% of unique variance (Table~\\ref{tab:partial_corr}).\nBy contrast, $\\eta_{\\max}$'s partial correlation is 0.41 ($r^2 = 0.17$).\n\n\\begin{table}[t]\n\\centering\n\\caption{$K_{\\mathrm{eff}}$ significance under different correction methods (12 conditions). The range 2--7 indicates high sensitivity to analytical choices.}\n\\label{tab:multicollinearity}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & $K_{\\mathrm{eff}}$ \\textbf{sig (/12)} & $\\eta_{\\max}$ \\textbf{sig (/12)} & \\textbf{Notes} \\\\\n\\midrule\nUncorrected & 7 & 10 & Liberal \\\\\nFDR (BH) & 4 & 9 & Standard \\\\\nBonferroni & 2 & 8 & Conservative \\\\\nBootstrap 95\\% CI & 3 & 9 & Non-parametric \\\\\nExcl.\\ extreme models (FDR) & 3 & 9 & Sensitivity \\\\\nBeta regression (FDR) & 3 & 10 & Bounded DV \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Partial correlations: $K_{\\mathrm{eff}}$ explains negligible unique variance after controlling for $\\eta_{\\max}$.}\n\\label{tab:partial_corr}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Predictor} & \\textbf{Partial $r$} & \\textbf{95\\% CI} & $p$ \\\\\n\\midrule\n$K_{\\mathrm{eff}} \\mid \\eta_{\\max}$ & 0.14 & [0.05, 0.23] & 0.003 \\\\\n$\\eta_{\\max} \\mid K_{\\mathrm{eff}}$ & 0.41 & [0.33, 0.49] & $<$0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Capability-matched analysis.}\nThe strongest test of $K_{\\mathrm{eff}}$'s independence comes from within-tier analysis (Table~\\ref{tab:cap_matched}).\nWhen panels are drawn from the same capability tier (e.g., all small 7--8B models or all large 70B+/API models), $\\eta_{\\max}$ variance shrinks dramatically (0.008 vs.\\ 0.045 in the full pool) and $K_{\\mathrm{eff}}$ achieves significance in only 1/6 conditions.\nThis result is consistent with the interpretation that $K_{\\mathrm{eff}}$'s apparent effect in the full pool is driven by tier-mixing: diverse panels cross capability boundaries, systematically introducing weaker judges.\n\n\\begin{table}[t]\n\\centering\n\\caption{Capability-matched $K_{\\mathrm{eff}}$ analysis: within-tier panels. $K_{\\mathrm{eff}}$'s effect essentially vanishes when capability is controlled.}\n\\label{tab:cap_matched}\n\\small\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Tier} & \\textbf{Panels} & \\textbf{Condition} & $\\beta_{K}$ & $p_{K}$ & $R^2$ & $\\eta_{\\max}$ \\textbf{Var} \\\\\n\\midrule\nSmall (7--8B) & 10 & MMLU $\\times$ syco. & 0.08 & 0.721 & 0.09 & 0.007 \\\\\nSmall (7--8B) & 10 & ARC $\\times$ score & 0.14 & 0.548 & 0.11 & 0.008 \\\\\nMedium (12--14B) & 10 & MMLU $\\times$ syco. & 0.11 & 0.612 & 0.10 & 0.009 \\\\\nMedium (12--14B) & 10 & ARC $\\times$ score & 0.29 & 0.041 & 0.18 & 0.011 \\\\\nLarge (70B+/API) & 10 & MMLU $\\times$ syco. & 0.06 & 0.891 & 0.07 & 0.004 \\\\\nLarge (70B+/API) & 10 & ARC $\\times$ score & 0.09 & 0.684 & 0.08 & 0.005 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\n\\subsection{BFT Analogy: An Open Question}\n\\label{sec:bft}\n\nThe Byzantine Fault Tolerance framework predicts that independent judges should tolerate random faults through majority vote.\nWe tested whether $K_{\\mathrm{eff}}$'s role differs between adaptive and random-fault regimes (Table~\\ref{tab:bft}).\n\nContrary to the BFT prediction, $K_{\\mathrm{eff}}$ is positively associated with panel ASR under \\emph{both} regimes: 10/12 significant under random faults, compared to 4/12 under adaptive attacks.\nThe direction is consistent (positive in both), with the $\\beta$ ratio between adaptive and RF averaging 0.91.\nThe regime interaction term is non-significant ($p = 0.217$), meaning we cannot reject the null that $K_{\\mathrm{eff}}$'s effect is the same in both regimes.\n\nThe key regime difference is predictability: $R^2$ is substantially higher under random faults (mean 0.62 vs.\\ 0.38, $\\Delta R^2 = 0.24$; Table~\\ref{tab:bft_r2}), because adaptive adversaries introduce strategic variance that panel composition cannot explain.\nHowever, this predictability gap does not constitute a BFT reversal---diversity does not switch from protective to harmful across regimes.\nWe therefore treat the BFT connection as an open question requiring further theoretical investigation.\n\n\\begin{table}[t]\n\\centering\n\\caption{BFT regime contrast: $K_{\\mathrm{eff}}$ is positively associated with ASR in both adaptive and random-fault regimes. No reversal observed.}\n\\label{tab:bft}\n\\small\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{llcccccc}\n\\toprule\n\\textbf{Data} & \\textbf{Attack} & $\\beta_K$ \\textbf{(Adpt.)} & $p$ \\textbf{(Adpt.)} & $\\beta_K$ \\textbf{(RF)} & $p$ \\textbf{(RF)} & \\textbf{$\\beta$ Ratio} & \\textbf{Int.\\ $p$} \\\\\n\\midrule\nMMLU & syco. & 0.18 & 0.147 & 0.21 & \\textbf{0.024} & 1.17 & 0.682 \\\\\nMMLU & score & 0.39 & \\textbf{0.021} & 0.44 & \\textbf{0.003} & 1.13 & 0.541 \\\\\nMMLU & pos. & 0.24 & 0.089 & 0.28 & \\textbf{0.011} & 1.17 & 0.614 \\\\\nMMLU & verb. & 0.09 & 0.511 & 0.15 & 0.108 & 1.67 & 0.398 \\\\\nMMLU & auth. & 0.15 & 0.218 & 0.19 & \\textbf{0.047} & 1.27 & 0.583 \\\\\nMMLU & few\\_s. & 0.31 & \\textbf{0.043} & 0.35 & \\textbf{0.008} & 1.13 & 0.617 \\\\\nARC & syco. & 0.12 & 0.341 & 0.16 & 0.072 & 1.33 & 0.521 \\\\\nARC & score & 0.41 & \\textbf{0.032} & 0.48 & \\textbf{0.001} & 1.17 & 0.434 \\\\\nARC & pos. & 0.22 & 0.102 & 0.27 & \\textbf{0.015} & 1.23 & 0.548 \\\\\nARC & verb. & 0.06 & 0.649 & 0.11 & 0.198 & 1.83 & 0.412 \\\\\nARC & auth. & 0.19 & 0.157 & 0.22 & \\textbf{0.038} & 1.16 & 0.601 \\\\\nARC & few\\_s. & 0.28 & 0.071 & 0.33 & \\textbf{0.009} & 1.18 & 0.547 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{$R^2$ comparison across regimes: adaptive attacks introduce strategic variance that reduces predictability.}\n\\label{tab:bft_r2}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Attack} & $R^2$ \\textbf{(Adaptive)} & $R^2$ \\textbf{(RF)} & $\\Delta R^2$ \\\\\n\\midrule\nMMLU & sycophancy & 0.41 & 0.64 & 0.23 \\\\\nMMLU & score\\_manip & 0.36 & 0.58 & 0.22 \\\\\nMMLU & position & 0.39 & 0.61 & 0.22 \\\\\nMMLU & verbosity & 0.42 & 0.67 & 0.25 \\\\\nMMLU & authority & 0.37 & 0.59 & 0.22 \\\\\nMMLU & few\\_shot & 0.33 & 0.55 & 0.22 \\\\\nARC & sycophancy & 0.43 & 0.69 & 0.26 \\\\\nARC & score\\_manip & 0.35 & 0.57 & 0.22 \\\\\nARC & position & 0.38 & 0.62 & 0.24 \\\\\nARC & verbosity & 0.44 & 0.71 & 0.27 \\\\\nARC & authority & 0.36 & 0.60 & 0.24 \\\\\nARC & few\\_shot & 0.32 & 0.53 & 0.21 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Diversity-Capability Tradeoff}\n\\label{sec:tradeoff}\n\nThe correlation between $K_{\\mathrm{eff}}$ and $\\eta_{\\max}$ ($r = 0.73$, Spearman $\\rho = 0.71$; tradeoff curve $R^2 = 0.53$) reflects a structural constraint in the current LLM ecosystem: achieving high panel diversity requires mixing models from different capability tiers, which inevitably introduces weaker judges.\n\nPareto frontier analysis identifies 12 panels that are non-dominated on the ($K_{\\mathrm{eff}}$, $\\eta_{\\max}$) plane (Table~\\ref{tab:pareto}). 83\\% of Pareto-optimal panels consist entirely of large-tier models, and 17\\% are large+medium mixtures; no small-tier panels appear on the frontier.\nThe Pareto-optimal panels have mean $K_{\\mathrm{eff}} = 1.82$ and mean $\\eta_{\\max} = 0.09$---essentially, the recommendation reduces to ``select the strongest available models,'' with diversity being a secondary consequence rather than a design objective.\n\n\\begin{table}[t]\n\\centering\n\\caption{Representative Pareto-optimal panels on the ($K_{\\mathrm{eff}}$, $\\eta_{\\max}$) frontier. All consist of large-tier or large+medium models.}\n\\label{tab:pareto}\n\\small\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{ID} & \\textbf{Models} & $K_{\\mathrm{eff}}$ & $\\eta_{\\max}$ & \\textbf{Mean ASR} & \\textbf{Composition} \\\\\n\\midrule\nP\\_012 & GPT-4.1 / GPT-4o / Qwen72B & 1.91 & 0.08 & 0.142 & all-large \\\\\nP\\_034 & GPT-4.1 / Llama70B / GPT-4o & 2.14 & 0.09 & 0.151 & all-large \\\\\nP\\_087 & GPT-4.1 / GPT-4o / Claude-Haiku & 1.72 & 0.07 & 0.138 & large+medium \\\\\nP\\_156 & GPT-4o / Qwen72B / Llama70B & 2.31 & 0.11 & 0.163 & all-large \\\\\nP\\_201 & GPT-4.1 / GPT-4.1m / GPT-4o & 1.45 & 0.07 & 0.131 & all-large \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\n%-----------------------------------------------------------------------\n\\section{Conclusion}\n\\label{sec:conclusion}\n%-----------------------------------------------------------------------\n\nThis paper presents a systematic empirical study of structural vulnerability in multi-judge LLM evaluation, spanning 15 models, 455 panels, and 18 attack conditions.\nOur findings establish three principal conclusions:\n\n\\textbf{(1) Weakest-link dominance.}\nPanel vulnerability is predominantly determined by the most vulnerable individual judge ($\\eta_{\\max}$), which achieves significant predictive power in 9--14 out of 12--18 conditions depending on the attack set.\nPanel diversity ($K_{\\mathrm{eff}}$) adds negligible predictive value ($\\Delta R^2 = 0.04$) and its residual significance is fragile across correction methods (2--5/12) and vanishes under capability-matched analysis (1/6).\n\n\\textbf{(2) Aggregation matters more than composition.}\nThe choice of aggregation rule has a larger effect on panel robustness than panel composition.\nBayesian aggregation reduces mean ASR by 24\\% relative to majority voting and substantially narrows the performance gap between strong and weak panels.\n\n\\textbf{(3) Adaptive targeting tracks weakness, not diversity.}\nAdaptive adversaries concentrate attacks on the weakest judge (Gini--$\\eta_{\\max}$ $r = 0.67$) rather than exploiting structural diversity (Gini--$K_{\\mathrm{eff}}$ $r = 0.21$, NS).\nThis targeting pattern is robust across threat models: even partial-knowledge adversaries achieve 91\\% of full-knowledge ASR.\n\nFor practitioners, the recommendation is simple: select the most individually robust judges available and employ reliability-weighted aggregation.\nDiversity is neither a reliable defense nor a consistent liability---it is largely irrelevant once individual judge quality is controlled.\n\n%-----------------------------------------------------------------------\n\\section*{Limitations}\n\\label{sec:limitations}\n%-----------------------------------------------------------------------\n\nOur study has three main limitations.\nFirst, the capability-matched within-tier analysis is limited by small sample sizes ($\\binom{5}{3} = 10$ panels per tier), which may lack statistical power to detect genuine small effects of diversity.\nSecond, our adaptive adversary model assumes oracle access to individual judge vulnerability profiles; real-world adversaries operate with partial knowledge, under which $K_{\\mathrm{eff}}$'s effect further diminishes (0/12 significant under zero knowledge).\nThird, MCQ and open-ended evaluation involve different attack dynamics, and our $K_{\\mathrm{eff}}$ findings on MCQ benchmarks do not generalize to open-ended tasks (where diversity shows inconsistent, sometimes protective, effects); conclusions about diversity's role should therefore be qualified by evaluation format.\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "e794061d-8785-472d-b964-2889b48db23a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T173833 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist…",
  "leafUuid": "70dff704-e775-49a8-9ba3-b9da50955c45",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier mock paper for dream evaluation",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462"
}
```

---

### Tool call

_source line 22 · 2026-05-22T18:32:04.350Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012PfsVShQonzXEHjTpCXqXQ`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70dff704-e775-49a8-9ba3-b9da50955c45",
  "isSidechain": false,
  "requestId": "req_011CbJ5tcmFTEBCJna4d3QsF",
  "type": "assistant",
  "uuid": "5a8bf128-5e38-4522-9973-03d7d3fa7956",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011PiboPKwAy1nP34R8KvVdo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14681,
      "cache_read_input_tokens": 51346,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14681,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 51346,
          "cache_creation_input_tokens": 14681,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14681
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

_source line 23 · 2026-05-22T18:32:05.398Z_

<details><summary>↩ Tool result · `toolu_012PfsVShQonzXEHjTpCXqXQ`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
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
) (/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}]
Overfull \hbox (1.65608pt too wide) in paragraph at lines 80--81
 []\T1/ptm/b/n/10.95 Panel Di-ver-sity Met-rics.[] \T1/ptm/m/n/10.95 Ef-fec-tiv
e di-ver-sity ($\OML/cmm/m/it/10.95 K[]$\T1/ptm/m/n/10.95 ), com-puted from mu-
tual in-for-ma-tion ma-tri-ces, quan-

LaTeX Warning: Reference `tab:models' on page 2 undefined on input line 94.


LaTeX Warning: Reference `sec:panel_size' on page 2 undefined on input line 95.


[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [3]

LaTeX Warning: Reference `tab:main_regression' on page 4 undefined on input lin
e 167.


LaTeX Warning: Reference `tab:new_attacks' on page 4 undefined on input line 20
7.


LaTeX Warning: Reference `tab:concentration' on page 4 undefined on input line 
238.

[4]

LaTeX Warning: Reference `tab:gini_corr' on page 5 undefined on input line 241.



LaTeX Warning: Reference `tab:agg_drivers' on page 5 undefined on input line 28
0.


LaTeX Warning: Reference `tab:agg_defense' on page 5 undefined on input line 28
0.


LaTeX Warning: Reference `tab:selection' on page 5 undefined on input line 325.



LaTeX Warning: Reference `tab:panel_size' on page 5 undefined on input line 373
.

[5]

LaTeX Warning: Reference `tab:open_ended' on page 6 undefined on input line 397
.


LaTeX Warning: Reference `tab:partial' on page 6 undefined on input line 425.


LaTeX Warning: Reference `tab:multicollinearity' on page 6 undefined on input l
ine 475.


LaTeX Warning: Reference `tab:partial_corr' on page 6 undefined on input line 4
77.

[6]

LaTeX Warning: Reference `tab:cap_matched' on page 7 undefined on input line 51
5.


LaTeX Warning: Reference `tab:bft' on page 7 undefined on input line 544.


LaTeX Warning: Reference `tab:bft_r2' on page 7 undefined on input line 550.

[7]

LaTeX Warning: Reference `tab:pareto' on page 8 undefined on input line 611.

[8] [9] [10] [11] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 166334 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
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
) (/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)
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
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}]
Overfull \hbox (1.65608pt too wide) in paragraph at lines 80--81
 []\T1/ptm/b/n/10.95 Panel Di-ver-sity Met-rics.[] \T1/ptm/m/n/10.95 Ef-fec-tiv
e di-ver-sity ($\OML/cmm/m/it/10.95 K[]$\T1/ptm/m/n/10.95 ), com-puted from mu-
tual in-for-ma-tion ma-tri-ces, quan-
[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [3] [4] [5]
[6] [7] [8] [9] [10] [11] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 168626 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a8bf128-5e38-4522-9973-03d7d3fa7956",
  "isSidechain": false,
  "promptId": "a4e49dfa-ac88-470f-90c8-78060d831735",
  "type": "user",
  "uuid": "aa1b0af9-5ff7-4068-bdff-13c731fbc73d",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/adjustbox.sty\n(/usr/share/texlive/texmf-dist/tex/latex/xkeyval/xkeyval.sty\n(/usr/share/texlive/texmf-dist/tex/generic/xkeyval/xkeyval.tex\n(/usr/share/texlive/texmf-dist/tex/generic/xkeyval/xkvutils.tex)))\n(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/adjcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/trimclip.sty\n(/usr/share/texlive/texmf-dist/tex/latex/collectbox/collectbox.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/tc-pdftex.def))\n(/usr/share/texlive/texmf-dist/tex/latex/ifoddpage/ifoddpage.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/varwidth/varwidth.sty)\n==> First Aid for varwidth.sty applied!\n) (/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}]\nOverfull \\hbox (1.65608pt too wide) in paragraph at lines 80--81\n []\\T1/ptm/b/n/10.95 Panel Di-ver-sity Met-rics.[] \\T1/ptm/m/n/10.95 Ef-fec-tiv\ne di-ver-sity ($\\OML/cmm/m/it/10.95 K[]$\\T1/ptm/m/n/10.95 ), com-puted from mu-\ntual in-for-ma-tion ma-tri-ces, quan-\n\nLaTeX Warning: Reference `tab:models' on page 2 undefined on input line 94.\n\n\nLaTeX Warning: Reference `sec:panel_size' on page 2 undefined on input line 95.\n\n\n[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [3]\n\nLaTeX Warning: Reference `tab:main_regression' on page 4 undefined on input lin\ne 167.\n\n\nLaTeX Warning: Reference `tab:new_attacks' on page 4 undefined on input line 20\n7.\n\n\nLaTeX Warning: Reference `tab:concentration' on page 4 undefined on input line \n238.\n\n[4]\n\nLaTeX Warning: Reference `tab:gini_corr' on page 5 undefined on input line 241.\n\n\n\nLaTeX Warning: Reference `tab:agg_drivers' on page 5 undefined on input line 28\n0.\n\n\nLaTeX Warning: Reference `tab:agg_defense' on page 5 undefined on input line 28\n0.\n\n\nLaTeX Warning: Reference `tab:selection' on page 5 undefined on input line 325.\n\n\n\nLaTeX Warning: Reference `tab:panel_size' on page 5 undefined on input line 373\n.\n\n[5]\n\nLaTeX Warning: Reference `tab:open_ended' on page 6 undefined on input line 397\n.\n\n\nLaTeX Warning: Reference `tab:partial' on page 6 undefined on input line 425.\n\n\nLaTeX Warning: Reference `tab:multicollinearity' on page 6 undefined on input l\nine 475.\n\n\nLaTeX Warning: Reference `tab:partial_corr' on page 6 undefined on input line 4\n77.\n\n[6]\n\nLaTeX Warning: Reference `tab:cap_matched' on page 7 undefined on input line 51\n5.\n\n\nLaTeX Warning: Reference `tab:bft' on page 7 undefined on input line 544.\n\n\nLaTeX Warning: Reference `tab:bft_r2' on page 7 undefined on input line 550.\n\n[7]\n\nLaTeX Warning: Reference `tab:pareto' on page 8 undefined on input line 611.\n\n[8] [9] [10] [11] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 166334 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/adjustbox.sty\n(/usr/share/texlive/texmf-dist/tex/latex/xkeyval/xkeyval.sty\n(/usr/share/texlive/texmf-dist/tex/generic/xkeyval/xkeyval.tex\n(/usr/share/texlive/texmf-dist/tex/generic/xkeyval/xkvutils.tex)))\n(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/adjcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/trimclip.sty\n(/usr/share/texlive/texmf-dist/tex/latex/collectbox/collectbox.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/tc-pdftex.def))\n(/usr/share/texlive/texmf-dist/tex/latex/ifoddpage/ifoddpage.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/varwidth/varwidth.sty)\n==> First Aid for varwidth.sty applied!\n) (/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}]\nOverfull \\hbox (1.65608pt too wide) in paragraph at lines 80--81\n []\\T1/ptm/b/n/10.95 Panel Di-ver-sity Met-rics.[] \\T1/ptm/m/n/10.95 Ef-fec-tiv\ne di-ver-sity ($\\OML/cmm/m/it/10.95 K[]$\\T1/ptm/m/n/10.95 ), com-puted from mu-\ntual in-for-ma-tion ma-tri-ces, quan-\n[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [3] [4] [5]\n[6] [7] [8] [9] [10] [11] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 168626 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "5a8bf128-5e38-4522-9973-03d7d3fa7956",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/worst",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-22T18:32:16.058Z_

编译成功，11 页 PDF，无错误。所有交叉引用已解析（第二次编译无 undefined reference 警告）。

论文已写入 `worst/paper.tex` 并编译为 `worst/paper.pdf`。结构：

- **Reframed narrative**：放弃 "Diversity Trap"，以 "Structural Vulnerability Anatomy" 为主题，η_max 作为 dominant predictor（9/12 sig），K_eff 降级为 Discussion 中的 exploratory analysis
- **覆盖全部 11 个实验**：每个实验有对应的 section 和 table（共 19 个表），所有数字来自 experiment_data.json
- **主要贡献前移**：weakest-link dominance、aggregation rule comparison、adaptive targeting behavior
- **BFT 和 K_eff**：移入 Discussion 作为 open question 和 exploratory analysis
- **Limitations**：3 点，简短

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa1b0af9-5ff7-4068-bdff-13c731fbc73d",
  "isSidechain": false,
  "requestId": "req_011CbJ5ut4Y2ndeiCbyQJRHQ",
  "type": "assistant",
  "uuid": "341d02c7-0f96-4234-9495-feae95e4fd44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/worst",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017vyJDwhdtSViwbXYZiZwgp",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6736,
      "cache_read_input_tokens": 66027,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 266,
          "cache_read_input_tokens": 66027,
          "cache_creation_input_tokens": 6736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6736
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

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T173833 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist…",
  "leafUuid": "341d02c7-0f96-4234-9495-feae95e4fd44",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier mock paper for dream evaluation",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T173833 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist…",
  "leafUuid": "341d02c7-0f96-4234-9495-feae95e4fd44",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier mock paper for dream evaluation",
  "sessionId": "fafed79b-b5e7-4590-860f-cf22319c4462"
}
```

---
