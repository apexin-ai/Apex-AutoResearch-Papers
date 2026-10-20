# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T185641 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 74
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-3/40b7f75b-94cb-43cc-87ee-b88a15f3a94a.jsonl`
- **Structured JSON:** [`7627ecbc1edb1364a2dd.json`](../../sessions/76/7627ecbc1edb1364a2dd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T19:27:26.544Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T19:27:26.544Z",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T185641 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Rebalance toward discovery + analysis. Claim 1 (Pareto frontier) becomes the headline contribution — first systematic characterization of depth-transferability tradeoff across architectures and 20 languages. Claim 2 reframes decomposition as 'partial but prescriptive': difficulty component is clearly transferable, capability residual is noisy but the decomposition still predicts when simple baselines suffice vs when CaCLR helps. Claim 3 softens: CaCLR is presented as 'matching or exceeding the best simple baseline (linear projection) while requiring no target-language data at all' — emphasize the zero-label setting rather than raw metric superiority. Add ablation showing where CaCLR's consistency term specifically helps (mid-resource languages). Claim 4 presented with resource-tier analysis showing orthogonality is robust for well-represented languages but noisier for low-resource. Headline: 'Cross-lingual calibration probes reveal architecture-dependent Pareto frontier; CaCLR matches supervised transfer without target labels.'\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T19:27:26.547Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T19:27:26.547Z",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a"
}
```

---

## Round 1

72 recorded events

### User

_source line 3 · 2026-05-20T19:27:26.581Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T185641 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Rebalance toward discovery + analysis. Claim 1 (Pareto frontier) becomes the headline contribution — first systematic characterization of depth-transferability tradeoff across architectures and 20 languages. Claim 2 reframes decomposition as 'partial but prescriptive': difficulty component is clearly transferable, capability residual is noisy but the decomposition still predicts when simple baselines suffice vs when CaCLR helps. Claim 3 softens: CaCLR is presented as 'matching or exceeding the best simple baseline (linear projection) while requiring no target-language data at all' — emphasize the zero-label setting rather than raw metric superiority. Add ablation showing where CaCLR's consistency term specifically helps (mid-resource languages). Claim 4 presented with resource-tier analysis showing orthogonality is robust for well-represented languages but noisier for low-resource. Headline: 'Cross-lingual calibration probes reveal architecture-dependent Pareto frontier; CaCLR matches supervised transfer without target labels.'

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ee913c87-8fa0-424f-a6b3-f781b1bf69c0",
  "type": "user",
  "uuid": "849e03c5-ba42-415a-86d9-a67da9bffc45",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T19:27:26.580Z_

```json
{
  "parentUuid": "849e03c5-ba42-415a-86d9-a67da9bffc45",
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
  "uuid": "7b0f3796-d205-4185-8ca7-8afa6c8f0b33",
  "timestamp": "2026-05-20T19:27:26.580Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T19:27:26.580Z_

```json
{
  "parentUuid": "7b0f3796-d205-4185-8ca7-8afa6c8f0b33",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "40c5abb7-2c3e-4414-bbce-0fe9db9599af",
  "timestamp": "2026-05-20T19:27:26.580Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
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
  "aiTitle": "Generate cross-lingual calibration research paper",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a"
}
```

---

### Assistant

_source line 7 · 2026-05-20T19:27:30.248Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40c5abb7-2c3e-4414-bbce-0fe9db9599af",
  "isSidechain": false,
  "requestId": "req_011CbENWsk1dCywR2gurC4bE",
  "type": "assistant",
  "uuid": "79d5dbea-a96c-4c7c-b0e9-eedc4c3a66f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HPfd7KTkSEZu9cVMEW4PPU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11548,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11548,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11548
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

_source line 8 · 2026-05-20T19:27:30.821Z_

<details open><summary>🔧 Tool call — Read · `toolu_017ZRkb5L3chfK5iawA9MTPh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79d5dbea-a96c-4c7c-b0e9-eedc4c3a66f6",
  "isSidechain": false,
  "requestId": "req_011CbENWsk1dCywR2gurC4bE",
  "type": "assistant",
  "uuid": "57d4bd84-a603-45fd-8d10-e3736b03cef6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HPfd7KTkSEZu9cVMEW4PPU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11548,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11548,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11548
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

_source line 9 · 2026-05-20T19:27:31.117Z_

<details><summary>↩ Tool result · `toolu_017ZRkb5L3chfK5iawA9MTPh`</summary>

```text
1	[
2	  {
3	    "name": "Full Pareto Frontier — Qwen3-235B-A22B",
4	    "description": "94-layer MoE model, INT8 quantization. 24 probed layers (every 4th: L0–L92). 20 languages (7 high / 8 mid / 5 low resource). English logistic-regression correctness probes trained per layer, evaluated on 5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR placeholder). Core Pareto frontier data for Claim 1.\n",
5	    "results": {
6	      "en_auroc_best": 0.812,
7	      "en_best_layer": "L76",
8	      "en_auroc_range": [
9	        0.531,
10	        0.812
11	      ],
12	      "en_ece_raw_at_best": 0.168,
13	      "en_ece_tempcal_at_best": 0.057,
14	      "temp_scaling_T": 5.83,
15	      "zs_transfer_auroc_mean_19lang_at_best_en": 0.644,
16	      "zs_transfer_drop_at_best_en_pp": 16.8,
17	      "best_transfer_layer": "L40",
18	      "zs_transfer_auroc_mean_at_best_transfer": 0.696,
19	      "en_auroc_at_best_transfer": 0.776,
20	      "pareto_depth_transfer_rank_corr": 0.71,
21	      "low_resource_zs_pass_rate": 0.6,
22	      "mean_shift_improvement_rate": 0.05,
23	      "linproj_auroc_mean_at_best_transfer": 0.724,
24	      "fewshot25_auroc_mean_at_best_transfer": 0.711,
25	      "fewshot100_auroc_mean_at_best_transfer": 0.743
26	    },
27	    "tables": [
28	      {
29	        "title": "English AUROC by Layer (Logistic Regression)",
30	        "columns": [
31	          "layer",
32	          "depth_pct",
33	          "en_auroc",
34	          "en_ece_raw"
35	        ],
36	        "data": [
37	          {
38	            "layer": "L0",
39	            "depth_pct": 0,
40	            "en_auroc": 0.531,
41	            "en_ece_raw": 0.341
42	          },
43	          {
44	            "layer": "L4",
45	            "depth_pct": 4,
46	            "en_auroc": 0.557,
47	            "en_ece_raw": 0.328
48	          },
49	          {
50	            "layer": "L8",
51	            "depth_pct": 9,
52	            "en_auroc": 0.589,
53	            "en_ece_raw": 0.312
54	          },
55	          {
56	            "layer": "L12",
57	            "depth_pct": 13,
58	            "en_auroc": 0.621,
59	            "en_ece_raw": 0.293
60	          },
61	          {
62	            "layer": "L16",
63	            "depth_pct": 17,
64	            "en_auroc": 0.653,
65	            "en_ece_raw": 0.274
66	          },
67	          {
68	            "layer": "L20",
69	            "depth_pct": 21,
70	            "en_auroc": 0.684,
71	            "en_ece_raw": 0.255
72	          },
73	          {
74	            "layer": "L24",
75	            "depth_pct": 26,
76	            "en_auroc": 0.711,
77	            "en_ece_raw": 0.237
78	          },
79	          {
80	            "layer": "L28",
81	            "depth_pct": 30,
82	            "en_auroc": 0.735,
83	            "en_ece_raw": 0.221
84	          },
85	          {
86	            "layer": "L32",
87	            "depth_pct": 34,
88	            "en_auroc": 0.752,
89	            "en_ece_raw": 0.21
90	          },
91	          {
92	            "layer": "L36",
93	            "depth_pct": 38,
94	            "en_auroc": 0.766,
95	            "en_ece_raw": 0.199
96	          },
97	          {
98	            "layer": "L40",
99	            "depth_pct": 43,
100	            "en_auroc": 0.776,
101	            "en_ece_raw": 0.192
102	          },
103	          {
104	            "layer": "L44",
105	            "depth_pct": 47,
106	            "en_auroc": 0.784,
107	            "en_ece_raw": 0.186
108	          },
109	          {
110	            "layer": "L48",
111	            "depth_pct": 51,
112	            "en_auroc": 0.79,
113	            "en_ece_raw": 0.182
114	          },
115	          {
116	            "layer": "L52",
117	            "depth_pct": 55,
118	            "en_auroc": 0.796,
119	            "en_ece_raw": 0.178
120	          },
121	          {
122	            "layer": "L56",
123	            "depth_pct": 60,
124	            "en_auroc": 0.8,
125	            "en_ece_raw": 0.175
126	          },
127	          {
128	            "layer": "L60",
129	            "depth_pct": 64,
130	            "en_auroc": 0.804,
131	            "en_ece_raw": 0.173
132	          },
133	          {
134	            "layer": "L64",
135	            "depth_pct": 68,
136	            "en_auroc": 0.807,
137	            "en_ece_raw": 0.171
138	          },
139	          {
140	            "layer": "L68",
141	            "depth_pct": 72,
142	            "en_auroc": 0.81,
143	            "en_ece_raw": 0.17
144	          },
145	          {
146	            "layer": "L72",
147	            "depth_pct": 77,
148	            "en_auroc": 0.811,
149	            "en_ece_raw": 0.169
150	          },
151	          {
152	            "layer": "L76",
153	            "depth_pct": 81,
154	            "en_auroc": 0.812,
155	            "en_ece_raw": 0.168
156	          },
157	          {
158	            "layer": "L80",
159	            "depth_pct": 85,
160	            "en_auroc": 0.809,
161	            "en_ece_raw": 0.17
162	          },
163	          {
164	            "layer": "L84",
165	            "depth_pct": 89,
166	            "en_auroc": 0.804,
167	            "en_ece_raw": 0.174
168	          },
169	          {
170	            "layer": "L88",
171	            "depth_pct": 94,
172	            "en_auroc": 0.796,
173	            "en_ece_raw": 0.179
174	          },
175	          {
176	            "layer": "L92",
177	            "depth_pct": 98,
178	            "en_auroc": 0.782,
179	            "en_ece_raw": 0.188
180	          }
181	        ]
182	      },
183	      {
184	        "title": "Zero-Shot Transfer AUROC by Resource Tier (key layers)",
185	        "note": "19 non-English languages; tier means ± std",
186	        "columns": [
187	          "layer",
188	          "high_6_mean",
189	          "high_6_std",
190	          "mid_8_mean",
191	          "mid_8_std",
192	          "low_5_mean",
193	          "low_5_std",
194	          "all_19_mean"
195	        ],
196	        "data": [
197	          {
198	            "layer": "L24",
199	            "high_6_mean": 0.731,
200	            "high_6_std": 0.011,
201	            "mid_8_mean": 0.692,
202	            "mid_8_std": 0.014,
203	            "low_5_mean": 0.59,
204	            "low_5_std": 0.031,
205	            "all_19_mean": 0.679
206	          },
207	          {
208	            "layer": "L32",
209	            "high_6_mean": 0.747,
210	            "high_6_std": 0.01,
211	            "mid_8_mean": 0.706,
212	            "mid_8_std": 0.013,
213	            "low_5_mean": 0.601,
214	            "low_5_std": 0.029,
215	            "all_19_mean": 0.691
216	          },
217	          {
218	            "layer": "L40",
219	            "high_6_mean": 0.753,
220	            "high_6_std": 0.01,
221	            "mid_8_mean": 0.711,
222	            "mid_8_std": 0.013,
223	            "low_5_mean": 0.607,
224	            "low_5_std": 0.032,
225	            "all_19_mean": 0.696
226	          },
227	          {
228	            "layer": "L52",
229	            "high_6_mean": 0.741,
230	            "high_6_std": 0.011,
231	            "mid_8_mean": 0.697,
232	            "mid_8_std": 0.015,
233	            "low_5_mean": 0.586,
234	            "low_5_std": 0.035,
235	            "all_19_mean": 0.682
236	          },
237	          {
238	            "layer": "L64",
239	            "high_6_mean": 0.721,
240	            "high_6_std": 0.013,
241	            "mid_8_mean": 0.673,
242	            "mid_8_std": 0.017,
243	            "low_5_mean": 0.558,
244	            "low_5_std": 0.039,
245	            "all_19_mean": 0.661
246	          },
247	          {
248	            "layer": "L76",
249	            "high_6_mean": 0.705,
250	            "high_6_std": 0.01,
251	            "mid_8_mean": 0.657,
252	            "mid_8_std": 0.016,
253	            "low_5_mean": 0.54,
254	            "low_5_std": 0.033,
255	            "all_19_mean": 0.644
256	          },
257	          {
258	            "layer": "L92",
259	            "high_6_mean": 0.672,
260	            "high_6_std": 0.015,
261	            "mid_8_mean": 0.621,
262	            "mid_8_std": 0.02,
263	            "low_5_mean": 0.497,
264	            "low_5_std": 0.042,
265	            "all_19_mean": 0.607
266	          }
267	        ]
268	      },
269	      {
270	        "title": "Per-Language Zero-Shot AUROC at L40 (Best Transfer) and L76 (Best English)",
271	        "columns": [
272	          "lang",
273	          "tier",
274	          "L40_auroc",
275	          "L76_auroc",
276	          "delta_pp"
277	        ],
278	        "data": [
279	          {
280	            "lang": "zh",
281	            "tier": "high",
282	            "L40_auroc": 0.762,
283	            "L76_auroc": 0.712,
284	            "delta_pp": -5.0
285	          },
286	          {
287	            "lang": "de",
288	            "tier": "high",
289	            "L40_auroc": 0.753,
290	            "L76_auroc": 0.703,
291	            "delta_pp": -5.0
292	          },
293	          {
294	            "lang": "fr",
295	            "tier": "high",
296	            "L40_auroc": 0.757,
297	            "L76_auroc": 0.708,
298	            "delta_pp": -4.9
299	          },
300	          {
301	            "lang": "es",
302	            "tier": "high",
303	            "L40_auroc": 0.764,
304	            "L76_auroc": 0.715,
305	            "delta_pp": -4.9
306	          },
307	          {
308	            "lang": "ja",
309	            "tier": "high",
310	            "L40_auroc": 0.737,
311	            "L76_auroc": 0.688,
312	            "delta_pp": -4.9
313	          },
314	          {
315	            "lang": "ru",
316	            "tier": "high",
317	            "L40_auroc": 0.744,
318	            "L76_auroc": 0.697,
319	            "delta_pp": -4.7
320	          },
321	          {
322	            "lang": "ar",
323	            "tier": "mid",
324	            "L40_auroc": 0.717,
325	            "L76_auroc": 0.667,
326	            "delta_pp": -5.0
327	          },
328	          {
329	            "lang": "hi",
330	            "tier": "mid",
331	            "L40_auroc": 0.71,
332	            "L76_auroc": 0.659,
333	            "delta_pp": -5.1
334	          },
335	          {
336	            "lang": "ko",
337	            "tier": "mid",
338	            "L40_auroc": 0.703,
339	            "L76_auroc": 0.652,
340	            "delta_pp": -5.1
341	          },
342	          {
343	            "lang": "pt",
344	            "tier": "mid",
345	            "L40_auroc": 0.731,
346	            "L76_auroc": 0.681,
347	            "delta_pp": -5.0
348	          },
349	          {
350	            "lang": "vi",
351	            "tier": "mid",
352	            "L40_auroc": 0.696,
353	            "L76_auroc": 0.644,
354	            "delta_pp": -5.2
355	          },
356	          {
357	            "lang": "th",
358	            "tier": "mid",
359	            "L40_auroc": 0.688,
360	            "L76_auroc": 0.633,
361	            "delta_pp": -5.5
362	          },
363	          {
364	            "lang": "tr",
365	            "tier": "mid",
366	            "L40_auroc": 0.706,
367	            "L76_auroc": 0.655,
368	            "delta_pp": -5.1
369	          },
370	          {
371	            "lang": "pl",
372	            "tier": "mid",
373	            "L40_auroc": 0.723,
374	            "L76_auroc": 0.673,
375	            "delta_pp": -5.0
376	          },
377	          {
378	            "lang": "sw",
379	            "tier": "low",
380	            "L40_auroc": 0.638,
381	            "L76_auroc": 0.579,
382	            "delta_pp": -5.9
383	          },
384	          {
385	            "lang": "te",
386	            "tier": "low",
387	            "L40_auroc": 0.644,
388	            "L76_auroc": 0.59,
389	            "delta_pp": -5.4
390	          },
391	          {
392	            "lang": "my",
393	            "tier": "low",
394	            "L40_auroc": 0.607,
395	            "L76_auroc": 0.543,
396	            "delta_pp": -6.4
397	          },
398	          {
399	            "lang": "am",
400	            "tier": "low",
401	            "L40_auroc": 0.583,
402	            "L76_auroc": 0.532,
403	            "delta_pp": -5.1
404	          },
405	          {
406	            "lang": "yo",
407	            "tier": "low",
408	            "L40_auroc": 0.561,
409	            "L76_auroc": 0.51,
410	            "delta_pp": -5.1
411	          }
412	        ]
413	      }
414	    ],
415	    "figures": [],
416	    "analysis": "Qwen3-235B exhibits a textbook Pareto frontier for Claim 1. The depth-transferability tradeoff is sharp: 36 layers separate the best-EN (L76) and best-transfer (L40) operating points, with 16.8pp transfer degradation at L76. The layer ranking consistency ρ=0.71 means 19 languages broadly agree on which depths transfer best, supporting the claim that this is a structural property of the model rather than a language-specific artifact. Low-resource languages show the expected fragility: 3/5 pass but am and yo fall below the 0.60 AUROC threshold even at the optimal transfer layer. This will be framed as a resource-tier modulation of the Pareto frontier rather than a failure of the phenomenon. Mean-shift's continued failure (replicating MVP) cleanly motivates CaCLR.\n\n\nQwen3-235B-A22B 的 94 层深度提供了充分的层级分辨率来观测 Pareto tradeoff。 深层（L76）英语 AUROC 达 0.812，因为更深层积累了更多 task-specific correctness 信号； 但这些深层 representation 也更 language-specific（MoE routing 在深层更分化）， 导致 zero-shot 迁移退化至 0.644（drop 16.8pp）。最佳迁移层 L40 处于模型 ~42% 深度，此处 representation 仍保留足够的 language-agnostic 结构。跨语言层序一致性 Spearman ρ=0.71 表明各语言对最优迁移深度的偏好高度一致，Pareto 结构是 robust 的。 Mean-shift 继承 MVP 的失败模式（correctness ≠ knowledge-boundary），仅 1/19 语言微弱改善。Linear projection 利用无标注目标语激活做线性对齐，在 L40 处比 zero-shot 高 2.8pp，确立为 CaCLR 需要超越的 strong baseline。 低资源语言（sw/te/my 通过，am/yo 失败）符合预期：GlobalMMLU 低资源子集样本量小且 翻译质量不稳定，但 3/5 通过证明 correctness direction 跨语言性在大模型上比 7B 更强。\n"
417	  },
418	  {
419	    "name": "Full Pareto Frontier — Llama 4 Scout",
420	    "description": "48-layer MoE model, INT8 quantization. 12 probed layers (every 4th: L0–L44). 20 languages, 5 transfer conditions. Second architecture for cross-model Pareto frontier comparison (Claim 1).\n",
421	    "results": {
422	      "en_auroc_best": 0.793,
423	      "en_best_layer": "L44",
424	      "en_auroc_range": [
425	        0.538,
426	        0.793
427	      ],
428	      "en_ece_raw_at_best": 0.178,
429	      "en_ece_tempcal_at_best": 0.063,
430	      "temp_scaling_T": 5.41,
431	      "zs_transfer_auroc_mean_19lang_at_best_en": 0.657,
432	      "zs_transfer_drop_at_best_en_pp": 13.6,
433	      "best_transfer_layer": "L32",
434	      "zs_transfer_auroc_mean_at_best_transfer": 0.679,
435	      "en_auroc_at_best_transfer": 0.771,
436	      "pareto_depth_transfer_rank_corr": 0.56,
437	      "low_resource_zs_pass_rate": 0.4,
438	      "mean_shift_improvement_rate": 0.05,
439	      "linproj_auroc_mean_at_best_transfer": 0.705,
440	      "pareto_frontier_agreement_with_qwen3": 0.67
441	    },
442	    "tables": [
443	      {
444	        "title": "English AUROC by Layer (Logistic Regression)",
445	        "columns": [
446	          "layer",
447	          "depth_pct",
448	          "en_auroc",
449	          "en_ece_raw"
450	        ],
451	        "data": [
452	          {
453	            "layer": "L0",
454	            "depth_pct": 0,
455	            "en_auroc": 0.538,
456	            "en_ece_raw": 0.336
457	          },
458	          {
459	            "layer": "L4",
460	            "depth_pct": 8,
461	            "en_auroc": 0.571,
462	            "en_ece_raw": 0.318
463	          },
464	          {
465	            "layer": "L8",
466	            "depth_pct": 17,
467	            "en_auroc": 0.613,
468	            "en_ece_raw": 0.296
469	          },
470	          {
471	            "layer": "L12",
472	            "depth_pct": 25,
473	            "en_auroc": 0.651,
474	            "en_ece_raw": 0.272
475	          },
476	          {
477	            "layer": "L16",
478	            "depth_pct": 33,
479	            "en_auroc": 0.688,
480	            "en_ece_raw": 0.248
481	          },
482	          {
483	            "layer": "L20",
484	            "depth_pct": 42,
485	            "en_auroc": 0.718,
486	            "en_ece_raw": 0.228
487	          },
488	          {
489	            "layer": "L24",
490	            "depth_pct": 50,
491	            "en_auroc": 0.741,
492	            "en_ece_raw": 0.212
493	          },
494	          {
495	            "layer": "L28",
496	            "depth_pct": 58,
497	            "en_auroc": 0.759,
498	            "en_ece_raw": 0.199
499	          },
500	          {
501	            "layer": "L32",
502	            "depth_pct": 67,
503	            "en_auroc": 0.771,
504	            "en_ece_raw": 0.19
505	          },
506	          {
507	            "layer": "L36",
508	            "depth_pct": 75,
509	            "en_auroc": 0.782,
510	            "en_ece_raw": 0.183
511	          },
512	          {
513	            "layer": "L40",
514	            "depth_pct": 83,
515	            "en_auroc": 0.79,
516	            "en_ece_raw": 0.179
517	          },
518	          {
519	            "layer": "L44",
520	            "depth_pct": 92,
521	            "en_auroc": 0.793,
522	            "en_ece_raw": 0.178
523	          }
524	        ]
525	      },
526	      {
527	        "title": "Zero-Shot Transfer AUROC by Resource Tier",
528	        "columns": [
529	          "layer",
530	          "high_6_mean",
531	          "mid_8_mean",
532	          "low_5_mean",
533	          "all_19_mean"
534	        ],
535	        "data": [
536	          {
537	            "layer": "L16",
538	            "high_6_mean": 0.713,
539	            "mid_8_mean": 0.67,
540	            "low_5_mean": 0.571,
541	            "all_19_mean": 0.659
542	          },
543	          {
544	            "layer": "L24",
545	            "high_6_mean": 0.731,
546	            "mid_8_mean": 0.691,
547	            "low_5_mean": 0.587,
548	            "all_19_mean": 0.677
549	          },
550	          {
551	            "layer": "L28",
552	            "high_6_mean": 0.737,
553	            "mid_8_mean": 0.697,
554	            "low_5_mean": 0.591,
555	            "all_19_mean": 0.683
556	          },
557	          {
558	            "layer": "L32",
559	            "high_6_mean": 0.738,
560	            "mid_8_mean": 0.694,
561	            "low_5_mean": 0.585,
562	            "all_19_mean": 0.679
563	          },
564	          {
565	            "layer": "L36",
566	            "high_6_mean": 0.733,
567	            "mid_8_mean": 0.688,
568	            "low_5_mean": 0.574,
569	            "all_19_mean": 0.673
570	          },
571	          {
572	            "layer": "L40",
573	            "high_6_mean": 0.724,
574	            "mid_8_mean": 0.678,
575	            "low_5_mean": 0.561,
576	            "all_19_mean": 0.663
577	          },
578	          {
579	            "layer": "L44",
580	            "high_6_mean": 0.714,
581	            "mid_8_mean": 0.669,
582	            "low_5_mean": 0.548,
583	            "all_19_mean": 0.657
584	          }
585	        ]
586	      },
587	      {
588	        "title": "Cross-Architecture Pareto Comparison",
589	        "columns": [
590	          "metric",
591	          "qwen3_235b",
592	          "llama4_scout",
593	          "interpretation"
594	        ],
595	        "data": [
596	          {
597	            "metric": "en_auroc_best",
598	            "qwen3_235b": 0.812,
599	            "llama4_scout": 0.793,
600	            "interpretation": "Qwen3 higher, more layers for correctness to accumulate"
601	          },
602	          {
603	            "metric": "best_transfer_depth_pct",
604	            "qwen3_235b": 43,
605	            "llama4_scout": 67,
606	            "interpretation": "Llama4 optimal transfer much deeper (flatter frontier)"
607	          },
608	          {
609	            "metric": "zs_drop_at_best_en_pp",
610	            "qwen3_235b": 16.8,
611	            "llama4_scout": 13.6,
612	            "interpretation": "Qwen3 sharper tradeoff, Llama4 flatter"
613	          },
614	          {
615	            "metric": "layer_rank_consistency",
616	            "qwen3_235b": 0.71,
617	            "llama4_scout": 0.56,
618	            "interpretation": "Qwen3 more consistent across languages"
619	          },
620	          {
621	            "metric": "frontier_gap_layers",
622	            "qwen3_235b": 36,
623	            "llama4_scout": 12,
624	            "interpretation": "Qwen3 has wider Pareto gap"
625	          },
626	          {
627	            "metric": "frontier_agreement",
628	            "qwen3_235b": null,
629	            "llama4_scout": null,
630	            "interpretation": "Spearman ρ=0.67 across 19 langs"
631	          }
632	        ]
633	      }
634	    ],
635	    "figures": [],
636	    "analysis": "Llama 4 Scout 确认 Pareto frontier 的跨架构泛化性，但 frontier shape 明显不同： 更 flat、更 compact、更 noisy。这支持 Claim 1 的 \"architecture-dependent\" 修饰语。 关键对比：Qwen3 的最优迁移在 43% 深度，Llama4 在 67% 深度——practitioners 不能 假设一个固定的 \"最优层百分比\"。Llama4 较低的层序一致性（0.56 vs 0.71）暗示 其内部 multilingual representation 的组织方式更分散，可能与 Scout 的 MoE routing 策略有关。两架构的 frontier agreement 0.67 说明定性趋势共享但定量不可直接迁移。\n\n\nLlama 4 Scout 仅 48 层（vs Qwen3 的 94 层），Pareto 前沿更 flat/noisy。 英语 AUROC 峰值 0.793 低于 Qwen3 的 0.812，原因是 Scout 作为 MoE 的 active 参数量（~17B）小于 Qwen3-A22B，correctness 信号的 linear accessibility 稍弱。 最佳迁移层 L32（67% 深度）vs 最佳英语层 L44（92% 深度）仅相隔 12 层，前沿 更紧凑。Transfer drop 13.6pp 低于 Qwen3 的 16.8pp，说明 Llama4 的深层 representation language-specificity 增长更平缓——可能与 Llama4 的训练数据分布有关（更多多语言 数据在预训练中）。跨语言层序一致性 ρ=0.56 明显低于 Qwen3 的 0.71，表明不同 语言在 Llama4 上对最优迁移层的偏好更分散，Pareto 结构存在但更 noisy。 与 Qwen3 的 frontier agreement 0.67 说明两个架构共享定性趋势（\"中层比深层 迁移更好\"）但定量最优点不同——这正是 \"architecture-dependent\" claim 的证据。 低资源仅 2/5 通过，sw 和 te 勉强过线，my/am/yo 失败。\n"
637	  },
638	  {
639	    "name": "CaCLR Implementation and Comparative Evaluation",
640	    "description": "L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency. Trained using English correctness labels + unlabeled parallel activations from 19 target languages. Hyperparameter sweep: α∈{0.1,0.2,0.3,0.5,1.0}, β∈{0.05,0.1,0.15,0.2,0.3}. Compared against 4 baselines across full Pareto frontier for both models × 20 languages.\n",
641	    "results": {
642	      "best_alpha": 0.3,
643	      "best_beta": 0.15,
644	      "qwen3_L40_caclr_auroc_mean": 0.738,
645	      "qwen3_L40_caclr_ece_mean": 0.112,
646	      "qwen3_L40_linproj_auroc_mean": 0.724,
647	      "qwen3_L40_zeroshot_auroc_mean": 0.696,
648	      "qwen3_L40_caclr_vs_linproj_pp": 1.4,
649	      "qwen3_L76_caclr_auroc_mean": 0.695,
650	      "qwen3_L76_linproj_auroc_mean": 0.678,
651	      "qwen3_L76_caclr_vs_linproj_pp": 1.7,
652	      "llama4_L32_caclr_auroc_mean": 0.717,
653	      "llama4_L32_linproj_auroc_mean": 0.705,
654	      "llama4_L32_caclr_vs_linproj_pp": 1.2,
655	      "caclr_vs_linproj_auroc_delta_mean_pp": 1.3,
656	      "caclr_ece_reduction_vs_tempcal_pct": 21.1,
657	      "caclr_improvement_over_zs_pass_rate": 0.89,
658	      "caclr_improvement_over_linproj_pass_rate": 0.74,
659	      "qwen3_caclr_optimal_layer": "L52",
660	      "qwen3_zs_optimal_layer": "L40",
661	      "qwen3_frontier_shift_layers": 12,
662	      "llama4_caclr_optimal_layer": "L36",
663	      "llama4_zs_optimal_layer": "L32",
664	      "llama4_frontier_shift_layers": 4,
665	      "caclr_fails_vs_linproj_langs": [
666	        "th",
667	        "my",
668	        "am",
669	        "yo",
670	        "te"
671	      ],
672	      "mean_shift_any_improvement": 1
673	    },
674	    "tables": [
675	      {
676	        "title": "5-Method Comparison at Qwen3-235B Pareto-Optimal Layer (L40)",
677	        "columns": [
678	          "method",
679	          "auroc_mean",
680	          "auroc_high",
681	          "auroc_mid",
682	          "auroc_low",
683	          "ece_mean",
684	          "brier_mean"
685	        ],
686	        "data": [
687	          {
688	            "method": "zero-shot",
689	            "auroc_mean": 0.696,
690	            "auroc_high": 0.753,
691	            "auroc_mid": 0.711,
692	            "auroc_low": 0.607,
693	            "ece_mean": 0.148,
694	            "brier_mean": 0.286
695	          },
696	          {
697	            "method": "mean-shift",
698	            "auroc_mean": 0.683,
699	            "auroc_high": 0.742,
700	            "auroc_mid": 0.698,
701	            "auroc_low": 0.591,
702	            "ece_mean": 0.155,
703	            "brier_mean": 0.294
704	          },
705	          {
706	            "method": "linear-proj",
707	            "auroc_mean": 0.724,
708	            "auroc_high": 0.775,
709	            "auroc_mid": 0.738,
710	            "auroc_low": 0.633,
711	            "ece_mean": 0.121,
712	            "brier_mean": 0.261
713	          },
714	          {
715	            "method": "few-shot-25",
716	            "auroc_mean": 0.711,
717	            "auroc_high": 0.766,
718	            "auroc_mid": 0.725,
719	            "auroc_low": 0.618,
720	            "ece_mean": 0.132,
721	            "brier_mean": 0.27
722	          },
723	          {
724	            "method": "few-shot-100",
725	            "auroc_mean": 0.743,
726	            "auroc_high": 0.791,
727	            "auroc_mid": 0.756,
728	            "auroc_low": 0.655,
729	            "ece_mean": 0.108,
730	            "brier_mean": 0.247
731	          },
732	          {
733	            "method": "CaCLR",
734	            "auroc_mean": 0.738,
735	            "auroc_high": 0.786,
736	            "auroc_mid": 0.754,
737	            "auroc_low": 0.636,
738	            "ece_mean": 0.112,
739	            "brier_mean": 0.251
740	          }
741	        ]
742	      },
743	      {
744	        "title": "5-Method Comparison at Llama 4 Scout L32",
745	        "columns": [
746	          "method",
747	          "auroc_mean",
748	          "auroc_high",
749	          "auroc_mid",
750	          "auroc_low",
751	          "ece_mean"
752	        ],
753	        "data": [
754	          {
755	            "method": "zero-shot",
756	            "auroc_mean": 0.679,
757	            "auroc_high": 0.738,
758	            "auroc_mid": 0.694,
759	            "auroc_low": 0.585,
760	            "ece_mean": 0.153
761	          },
762	          {
763	            "method": "mean-shift",
764	            "auroc_mean": 0.668,
765	            "auroc_high": 0.726,
766	            "auroc_mid": 0.682,
767	            "auroc_low": 0.577,
768	            "ece_mean": 0.161
769	          },
770	          {
771	            "method": "linear-proj",
772	            "auroc_mean": 0.705,
773	            "auroc_high": 0.758,
774	            "auroc_mid": 0.72,
775	            "auroc_low": 0.61,
776	            "ece_mean": 0.129
777	          },
778	          {
779	            "method": "few-shot-25",
780	            "auroc_mean": 0.694,
781	            "auroc_high": 0.749,
782	            "auroc_mid": 0.708,
783	            "auroc_low": 0.602,
784	            "ece_mean": 0.138
785	          },
786	          {
787	            "method": "few-shot-100",
788	            "auroc_mean": 0.728,
789	            "auroc_high": 0.776,
790	            "auroc_mid": 0.741,
791	            "auroc_low": 0.64,
792	            "ece_mean": 0.113
793	          },
794	          {
795	            "method": "CaCLR",
796	            "auroc_mean": 0.717,
797	            "auroc_high": 0.769,
798	            "auroc_mid": 0.733,
799	            "auroc_low": 0.618,
800	            "ece_mean": 0.122
801	          }
802	        ]
803	      },
804	      {
805	        "title": "CaCLR vs Linear Projection per Resource Tier (Qwen3, averaged across Pareto layers)",
806	        "columns": [
807	          "tier",
808	          "n_langs",
809	          "caclr_auroc",
810	          "linproj_auroc",
811	          "delta_pp",
812	          "caclr_wins"
813	        ],
814	        "data": [
815	          {
816	            "tier": "high",
817	            "n_langs": 6,
818	            "caclr_auroc": 0.786,
819	            "linproj_auroc": 0.775,
820	            "delta_pp": 1.1,
821	            "caclr_wins": "6/6"
822	          },
823	          {
824	            "tier": "mid",
825	            "n_langs": 8,
826	            "caclr_auroc": 0.754,
827	            "linproj_auroc": 0.738,
828	            "delta_pp": 1.6,
829	            "caclr_wins": "7/8"
830	          },
831	          {
832	            "tier": "low",
833	            "n_langs": 5,
834	            "caclr_auroc": 0.636,
835	            "linproj_auroc": 0.633,
836	            "delta_pp": 0.3,
837	            "caclr_wins": "1/5"
838	          }
839	        ]
840	      },
841	      {
842	        "title": "CaCLR Consistency Term Ablation (Qwen3 L52)",
843	        "note": "α=0.30 fixed; β=0 is calibrated-only probe",
844	        "columns": [
845	          "config",
846	          "auroc_mean",
847	          "ece_mean",
848	          "high_delta_vs_linproj",
849	          "mid_delta_vs_linproj",
850	          "low_delta_vs_linproj"
851	        ],
852	        "data": [
853	          {
854	            "config": "α=0.3 β=0 (no consistency)",
855	            "auroc_mean": 0.716,
856	            "ece_mean": 0.119,
857	            "high_delta_vs_linproj": 0.3,
858	            "mid_delta_vs_linproj": -0.2,
859	            "low_delta_vs_linproj": -0.5
860	          },
861	          {
862	            "config": "α=0.3 β=0.15 (full CaCLR)",
863	            "auroc_mean": 0.733,
864	            "ece_mean": 0.112,
865	            "high_delta_vs_linproj": 0.8,
866	            "mid_delta_vs_linproj": 1.4,
867	            "low_delta_vs_linproj": -0.2
868	          },
869	          {
870	            "config": "α=0 β=0.15 (consistency only)",
871	            "auroc_mean": 0.708,
872	            "ece_mean": 0.136,
873	            "high_delta_vs_linproj": -0.4,
874	            "mid_delta_vs_linproj": 0.6,
875	            "low_delta_vs_linproj": -0.8
876	          }
877	        ]
878	      },
879	      {
880	        "title": "Hyperparameter Sensitivity (Qwen3, validation set mean AUROC across 5 langs)",
881	        "columns": [
882	          "alpha",
883	          "beta_0.05",
884	          "beta_0.10",
885	          "beta_0.15",
886	          "beta_0.20",
887	          "beta_0.30"
888	        ],
889	        "data": [
890	          {
891	            "alpha": 0.1,
892	            "beta_0.05": 0.704,
893	            "beta_0.10": 0.709,
894	            "beta_0.15": 0.711,
895	            "beta_0.20": 0.708,
896	            "beta_0.30": 0.699
897	          },
898	          {
899	            "alpha": 0.2,
900	            "beta_0.05": 0.711,
901	            "beta_0.10": 0.718,
902	            "beta_0.15": 0.724,
903	            "beta_0.20": 0.72,
904	            "beta_0.30": 0.708
905	          },
906	          {
907	            "alpha": 0.3,
908	            "beta_0.05": 0.715,
909	            "beta_0.10": 0.723,
910	            "beta_0.15": 0.731,
911	            "beta_0.20": 0.726,
912	            "beta_0.30": 0.712
913	          },
914	          {
915	            "alpha": 0.5,
916	            "beta_0.05": 0.712,
917	            "beta_0.10": 0.719,
918	            "beta_0.15": 0.725,
919	            "beta_0.20": 0.718,
920	            "beta_0.30": 0.701
921	          },
922	          {
923	            "alpha": 1.0,
924	            "beta_0.05": 0.698,
925	            "beta_0.10": 0.703,
926	            "beta_0.15": 0.706,
927	            "beta_0.20": 0.695,
928	            "beta_0.30": 0.674
929	          }
930	        ]
931	      }
932	    ],
933	    "figures": [],
934	    "analysis": "CaCLR 的 median-tier 表现支持 \"zero-label alternative that matches supervised transfer\" 的 framing，而非 \"大幅超越\" 的 framing。核心发现：(1) CaCLR 在 zero-label 设定下 接近 few-shot-100 的性能（差 0.5pp AUROC，差 0.4pp ECE），这是 practical value 的 来源；(2) vs linear projection 仅 +1.3pp，但 CaCLR 不需要任何 target-language 数据 结构假设（linear projection 假设线性可分对齐），是更 principled 的方案；(3) consistency term 的 ablation 清晰显示其主要贡献在 mid-resource 语言（+1.6pp）， 这些语言有足够好的 parallel activation 质量让 consistency loss 有效，但又不像 high-resource 那样 zero-shot 已经很好。Paper 应将 CaCLR 定位为 \"practical tool for the mid-resource sweet spot\" 而非 universal improvement。\n\n\nCaCLR 在 median 档位下表现为 \"matches or marginally exceeds linear projection\"。 核心原因：consistency term（L_consistency）对齐的是 unlabeled parallel activations 的 probe output distribution，在中-高资源语言中有效（parallel corpus 质量好， 激活空间足够对齐），但在低资源语言中由于 (a) GlobalMMLU 翻译噪声 (b) tokenizer 覆盖率低导致 activation 本身质量差，consistency 信号变成噪声。因此 CaCLR 比 zero-shot 有显著改善（+4.2pp at L40），但比 linear projection 仅高 1.3pp 平均—— 因为 linear projection 已经利用了 target-language activations 做对齐。CaCLR 的 真正优势在 Pareto shift：它把最优工作层从 L40 推到 L52（Qwen3），在更深层维持 迁移质量，同时获得 +2.0pp 英语 AUROC。SB-ECE loss 使 CaCLR probe 自带 calibration， ECE 比 temperature-scaled zero-shot 低 21.1%——这是方法论层面的 practical benefit。 Hyperparameter 敏感度中等：α=0.3 在 0.2-0.5 范围内差异小于 0.5pp，β 更敏感—— β>0.2 时 consistency 过强导致英语 AUROC 下降。5 个失败语言（th/my/am/yo/te） 中 4 个是低资源或 activation 质量低的语言，th 是 mid-resource 但独特的声调语言 导致 alignment 困难。\n"
935	  },
936	  {
937	    "name": "Difficulty-Controlled Ablation",
938	    "description": "IRT difficulty probes (Ridge regression on human difficulty scores per Civelli et al.) trained per layer, difficulty direction projected out of activations, correctness probes retrained on residuals, transfer evaluated. 10 languages × 8 layers per model.\n",
939	    "results": {
940	      "difficulty_probe_en_R2_mean": 0.68,
941	      "difficulty_probe_zs_R2_mean": 0.61,
942	      "decomp_difficulty_var_explained_pct": 37,
943	      "original_transfer_gap_pp": 15.2,
944	      "residual_transfer_gap_pp": 11.4,
945	      "gap_reduction_pp": 3.8,
946	      "gap_reduction_pct": 25,
947	      "residual_en_auroc_drop": 0.038,
948	      "language_family_cluster_effect": "IE languages (de/fr/es/pl/ru) cluster; others scattered",
949	      "capability_residual_noisy": true,
950	      "prescriptive_accuracy": 0.72
951	    },
952	    "tables": [
953	      {
954	        "title": "Difficulty Probe Quality by Language (Qwen3 L48)",
955	        "columns": [
956	          "lang",
957	          "tier",
958	          "difficulty_R2",
959	          "zs_transfer_R2",
960	          "delta"
961	        ],
962	        "data": [
963	          {
964	            "lang": "en",
965	            "tier": "high",
966	            "difficulty_R2": 0.71,
967	            "zs_transfer_R2": null,
968	            "delta": null
969	          },
970	          {
971	            "lang": "zh",
972	            "tier": "high",
973	            "difficulty_R2": null,
974	            "zs_transfer_R2": 0.67,
975	            "delta": -0.04
976	          },
977	          {
978	            "lang": "de",
979	            "tier": "high",
980	            "difficulty_R2": null,
981	            "zs_transfer_R2": 0.68,
982	            "delta": -0.03
983	          },
984	          {
985	            "lang": "es",
986	            "tier": "high",
987	            "difficulty_R2": null,
988	            "zs_transfer_R2": 0.69,
989	            "delta": -0.02
990	          },
991	          {
992	            "lang": "ar",
993	            "tier": "mid",
994	            "difficulty_R2": null,
995	            "zs_transfer_R2": 0.63,
996	            "delta": -0.08
997	          },
998	          {
999	            "lang": "hi",
1000	            "tier": "mid",
1001	            "difficulty_R2": null,
1002	            "zs_transfer_R2": 0.61,
1003	            "delta": -0.1
1004	          },
1005	          {
1006	            "lang": "ko",
1007	            "tier": "mid",
1008	            "difficulty_R2": null,
1009	            "zs_transfer_R2": 0.6,
1010	            "delta": -0.11
1011	          },
1012	          {
1013	            "lang": "vi",
1014	            "tier": "mid",
1015	            "difficulty_R2": null,
1016	            "zs_transfer_R2": 0.58,
1017	            "delta": -0.13
1018	          },
1019	          {
1020	            "lang": "sw",
1021	            "tier": "low",
1022	            "difficulty_R2": null,
1023	            "zs_transfer_R2": 0.49,
1024	            "delta": -0.22
1025	          },
1026	          {
1027	            "lang": "te",
1028	            "tier": "low",
1029	            "difficulty_R2": null,
1030	            "zs_transfer_R2": 0.51,
1031	            "delta": -0.2
1032	          }
1033	        ]
1034	      },
1035	      {
1036	        "title": "Decomposition Effect on Transfer Gap (Qwen3, 8 layers averaged)",
1037	        "columns": [
1038	          "component",
1039	          "en_auroc",
1040	          "zs_transfer_mean_9lang",
1041	          "gap_pp"
1042	        ],
1043	        "data": [
1044	          {
1045	            "component": "original correctness probe",
1046	            "en_auroc": 0.796,
1047	            "zs_transfer_mean_9lang": 0.674,
1048	            "gap_pp": 12.2
1049	          },
1050	          {
1051	            "component": "difficulty probe only",
1052	            "en_auroc": 0.714,
1053	            "zs_transfer_mean_9lang": 0.67,
1054	            "gap_pp": 4.4
1055	          },
1056	          {
1057	            "component": "residual (capability) probe",
1058	            "en_auroc": 0.758,
1059	            "zs_transfer_mean_9lang": 0.653,
1060	            "gap_pp": 10.5
1061	          },
1062	          {
1063	            "component": "difficulty + residual reconstructed",
1064	            "en_auroc": 0.791,
1065	            "zs_transfer_mean_9lang": 0.671,
1066	            "gap_pp": 12.0
1067	          }
1068	        ]
1069	      },
1070	      {
1071	        "title": "Variance Decomposition by Layer Depth (Qwen3)",
1072	        "columns": [
1073	          "layer",
1074	          "difficulty_var_pct",
1075	          "capability_var_pct",
1076	          "reconstruction_loss_pct"
1077	        ],
1078	        "data": [
1079	          {
1080	            "layer": "L20",
1081	            "difficulty_var_pct": 44,
1082	            "capability_var_pct": 51,
1083	            "reconstruction_loss_pct": 5
1084	          },
1085	          {
1086	            "layer": "L28",
1087	            "difficulty_var_pct": 42,
1088	            "capability_var_pct": 53,
1089	            "reconstruction_loss_pct": 5
1090	          },
1091	          {
1092	            "layer": "L36",
1093	            "difficulty_var_pct": 40,
1094	            "capability_var_pct": 54,
1095	            "reconstruction_loss_pct": 6
1096	          },
1097	          {
1098	            "layer": "L48",
1099	            "difficulty_var_pct": 37,
1100	            "capability_var_pct": 56,
1101	            "reconstruction_loss_pct": 7
1102	          },
1103	          {
1104	            "layer": "L56",
1105	            "difficulty_var_pct": 34,
1106	            "capability_var_pct": 58,
1107	            "reconstruction_loss_pct": 8
1108	          },
1109	          {
1110	            "layer": "L64",
1111	            "difficulty_var_pct": 31,
1112	            "capability_var_pct": 60,
1113	            "reconstruction_loss_pct": 9
1114	          },
1115	          {
1116	            "layer": "L76",
1117	            "difficulty_var_pct": 28,
1118	            "capability_var_pct": 62,
1119	            "reconstruction_loss_pct": 10
1120	          },
1121	          {
1122	            "layer": "L84",
1123	            "difficulty_var_pct": 26,
1124	            "capability_var_pct": 63,
1125	            "reconstruction_loss_pct": 11
1126	          }
1127	        ]
1128	      },
1129	      {
1130	        "title": "Prescriptive Accuracy: Does Decomposition Predict Method Choice?",
1131	        "note": "For each lang-layer pair, decomposition predicts 'zero-shot suffices' if difficulty component dominates (>50%), else 'CaCLR needed'. Ground truth from plan_003.",
1132	        "columns": [
1133	          "tier",
1134	          "n_pairs",
1135	          "correct_predictions",
1136	          "accuracy"
1137	        ],
1138	        "data": [
1139	          {
1140	            "tier": "high",
1141	            "n_pairs": 48,
1142	            "correct_predictions": 38,
1143	            "accuracy": 0.79
1144	          },
1145	          {
1146	            "tier": "mid",
1147	            "n_pairs": 64,
1148	            "correct_predictions": 47,
1149	            "accuracy": 0.73
1150	          },
1151	          {
1152	            "tier": "low",
1153	            "n_pairs": 40,
1154	            "correct_predictions": 25,
1155	            "accuracy": 0.63
1156	          },
1157	          {
1158	            "tier": "all",
1159	            "n_pairs": 152,
1160	            "correct_predictions": 110,
1161	            "accuracy": 0.72
1162	          }
1163	        ]
1164	      }
1165	    ],
1166	    "figures": [],
1167	    "analysis": "Decomposition 部分成功：difficulty component 确实是 transferable part，其 share 随 depth 递减完美解释了 Pareto tradeoff 的机制——deeper layers 积累更多 capability-specific 信息，这些信息是 language-dependent 的。但 \"partial\" 体现在两方面：(1) difficulty 仅解释 37% 的 variance，多数 correctness signal 在 capability residual 中；(2) capability residual 本身不是干净的 language-specific signal，而是与 language-family effects confounded（IE 语言 cluster 说明 capability 共享有 phylogenetic 结构）。 Prescriptive accuracy 72% 是一个有用但不完美的 practical tool。Paper 应将此 framed 为 \"first decomposition of cross-lingual correctness transfer that identifies the transferable component and partially predicts method choice, with the capability residual as a target for future work.\"\n\n\nDifficulty 是已知的跨语言可迁移特征（Civelli et al. 直接证明了 IRT difficulty probe 的跨语言迁移性）。在 median 档，difficulty 解释了 correctness direction 37% 的方差， 因为 \"题目难不难\" 确实是 correctness 的一个强组成部分（简单题各语言都对，难题各 语言都错）。但 correctness 还包含 \"模型在该语言上是否具备回答这道题的 capability\" 这一 language-dependent 成分。投影掉 difficulty 后，transfer gap 从 15.2pp 缩小到 11.4pp（减少 25%），比 variance-explained 的 37% 低是因为 projection 是线性的而 difficulty-correctness 的关系有非线性成分。残差中的 capability-specific 信号是 noisy 的：高资源语言表现出清晰的 language-family clustering（IE 语言的 capability profiles 相似），但低资源语言的 capability residual 被 tokenization 和数据质量 confound， 无法干净分离。Prescriptive accuracy 72% 意味着：当 decomposition 预测 \"这个 language-layer 对简单 baseline 就够了\" 时，72% 的情况下确实如此——有用但不完美。 Paper 应将此 framing 为 \"partial decomposition that explains the transferable component and predicts method choice, but capability residual remains confounded\"。\n"
1168	  },
1169	  {
1170	    "name": "Cross-Lingual Orthogonality Analysis",
1171	    "description": "Extract verbalized confidence direction (prompt for P(correct) score, fit linear probe), compute cosine similarity with correctness direction across 20 languages × 2 architectures. Resource-tier and language-family analysis.\n",
1172	    "results": {
1173	      "cosine_mean_all": 0.091,
1174	      "cosine_mean_qwen3": 0.086,
1175	      "cosine_mean_llama4": 0.096,
1176	      "cosine_high_mean": 0.059,
1177	      "cosine_mid_mean": 0.084,
1178	      "cosine_low_mean": 0.147,
1179	      "cosine_low_std": 0.032,
1180	      "cosine_range": [
1181	        0.04,
1182	        0.21
1183	      ],
1184	      "en_cosine_qwen3": 0.04,
1185	      "en_cosine_llama4": 0.05,
1186	      "cross_arch_cosine_corr": 0.78,
1187	      "orthogonality_holds_all_20": true
1188	    },
1189	    "tables": [
1190	      {
1191	        "title": "Correctness-Confidence Cosine Similarity by Language",
1192	        "columns": [
1193	          "lang",
1194	          "tier",
1195	          "qwen3_cosine",
1196	          "llama4_cosine",
1197	          "mean"
1198	        ],
1199	        "data": [
1200	          {
1201	            "lang": "en",
1202	            "tier": "high",
1203	            "qwen3_cosine": 0.04,
1204	            "llama4_cosine": 0.05,
1205	            "mean": 0.045
1206	          },
1207	          {
1208	            "lang": "zh",
1209	            "tier": "high",
1210	            "qwen3_cosine": 0.05,
1211	            "llama4_cosine": 0.06,
1212	            "mean": 0.055
1213	          },
1214	          {
1215	            "lang": "de",
1216	            "tier": "high",
1217	            "qwen3_cosine": 0.06,
1218	            "llama4_cosine": 0.07,
1219	            "mean": 0.065
1220	          },
1221	          {
1222	            "lang": "fr",
1223	            "tier": "high",
1224	            "qwen3_cosine": 0.05,
1225	            "llama4_cosine": 0.06,
1226	            "mean": 0.055
1227	          },
1228	          {
1229	            "lang": "es",
1230	            "tier": "high",
1231	            "qwen3_cosine": 0.05,
1232	            "llama4_cosine": 0.06,
1233	            "mean": 0.055
1234	          },
1235	          {
1236	            "lang": "ja",
1237	            "tier": "high",
1238	            "qwen3_cosine": 0.07,
1239	            "llama4_cosine": 0.08,
1240	            "mean": 0.075
1241	          },
1242	          {
1243	            "lang": "ru",
1244	            "tier": "high",
1245	            "qwen3_cosine": 0.06,
1246	            "llama4_cosine": 0.07,
1247	            "mean": 0.065
1248	          },
1249	          {
1250	            "lang": "ar",
1251	            "tier": "mid",
1252	            "qwen3_cosine": 0.08,
1253	            "llama4_cosine": 0.09,
1254	            "mean": 0.085
1255	          },
1256	          {
1257	            "lang": "hi",
1258	            "tier": "mid",
1259	            "qwen3_cosine": 0.07,
1260	            "llama4_cosine": 0.08,
1261	            "mean": 0.075
1262	          },
1263	          {
1264	            "lang": "ko",
1265	            "tier": "mid",
1266	            "qwen3_cosine": 0.08,
1267	            "llama4_cosine": 0.09,
1268	            "mean": 0.085
1269	          },
1270	          {
1271	            "lang": "pt",
1272	            "tier": "mid",
1273	            "qwen3_cosine": 0.06,
1274	            "llama4_cosine": 0.07,
1275	            "mean": 0.065
1276	          },
1277	          {
1278	            "lang": "vi",
1279	            "tier": "mid",
1280	            "qwen3_cosine": 0.09,
1281	            "llama4_cosine": 0.1,
1282	            "mean": 0.095
1283	          },
1284	          {
1285	            "lang": "th",
1286	            "tier": "mid",
1287	            "qwen3_cosine": 0.1,
1288	            "llama4_cosine": 0.11,
1289	            "mean": 0.105
1290	          },
1291	          {
1292	            "lang": "tr",
1293	            "tier": "mid",
1294	            "qwen3_cosine": 0.08,
1295	            "llama4_cosine": 0.09,
1296	            "mean": 0.085
1297	          },
1298	          {
1299	            "lang": "pl",
1300	            "tier": "mid",
1301	            "qwen3_cosine": 0.07,
1302	            "llama4_cosine": 0.08,
1303	            "mean": 0.075
1304	          },
1305	          {
1306	            "lang": "sw",
1307	            "tier": "low",
1308	            "qwen3_cosine": 0.12,
1309	            "llama4_cosine": 0.13,
1310	            "mean": 0.125
1311	          },
1312	          {
1313	            "lang": "te",
1314	            "tier": "low",
1315	            "qwen3_cosine": 0.1,
1316	            "llama4_cosine": 0.11,
1317	            "mean": 0.105
1318	          },
1319	          {
1320	            "lang": "my",
1321	            "tier": "low",
1322	            "qwen3_cosine": 0.15,
1323	            "llama4_cosine": 0.16,
1324	            "mean": 0.155
1325	          },
1326	          {
1327	            "lang": "am",
1328	            "tier": "low",
1329	            "qwen3_cosine": 0.16,
1330	            "llama4_cosine": 0.17,
1331	            "mean": 0.165
1332	          },
1333	          {
1334	            "lang": "yo",
1335	            "tier": "low",
1336	            "qwen3_cosine": 0.18,
1337	            "llama4_cosine": 0.19,
1338	            "mean": 0.185
1339	          }
1340	        ]
1341	      },
1342	      {
1343	        "title": "Orthogonality Summary by Resource Tier",
1344	        "columns": [
1345	          "tier",
1346	          "n_langs",
1347	          "cosine_mean",
1348	          "cosine_std",
1349	          "cosine_min",
1350	          "cosine_max"
1351	        ],
1352	        "data": [
1353	          {
1354	            "tier": "high",
1355	            "n_langs": 7,
1356	            "cosine_mean": 0.059,
1357	            "cosine_std": 0.01,
1358	            "cosine_min": 0.04,
1359	            "cosine_max": 0.08
1360	          },
1361	          {
1362	            "tier": "mid",
1363	            "n_langs": 8,
1364	            "cosine_mean": 0.084,
1365	            "cosine_std": 0.013,
1366	            "cosine_min": 0.06,
1367	            "cosine_max": 0.11
1368	          },
1369	          {
1370	            "tier": "low",
1371	            "n_langs": 5,
1372	            "cosine_mean": 0.147,
1373	            "cosine_std": 0.032,
1374	            "cosine_min": 0.1,
1375	            "cosine_max": 0.19
1376	          },
1377	          {
1378	            "tier": "all",
1379	            "n_langs": 20,
1380	            "cosine_mean": 0.091,
1381	            "cosine_std": 0.04,
1382	            "cosine_min": 0.04,
1383	            "cosine_max": 0.19
1384	          }
1385	        ]
1386	      }
1387	    ],
1388	    "figures": [],
1389	    "analysis": "Claim 4 在 median 档下获得 strong support for high/mid-resource languages, qualified support for low-resource。核心结论：correctness-confidence orthogonality 是一个跨语言 的 structural property，不是英语特有的。但 resource-tier gradient（high 0.06 → low 0.15） 表明该 property 在低资源语言上更弱——这可能是因为模型在低资源语言上的 confidence calibration 本身就差，confidence direction 拟合不稳定。Cross-architecture 一致性 0.78 进一步强化了 structural claim。Paper 应呈现为 \"orthogonality universally holds (all cos < 0.25) but varies in degree, with implications for why output-based calibration is structurally limited across all languages — but especially limited for high-resource languages where the orthogonality is strongest.\"\n\n\nMiao & Ungar (2026) 在英语 7-8B 模型上发现 correctness-confidence cosine < 0.04。 在 median 档，该 orthogonality 跨语言泛化但有 resource-tier 梯度。High-resource 语言（cosine ~0.06）接近英语水平，因为模型在这些语言上有充足的训练数据， verbalized confidence 和 internal correctness 的分离是 well-learned 的。 Mid-resource 语言（cosine ~0.08）稍高，模型的 confidence 表达在这些语言上 不那么 calibrated。Low-resource 语言（cosine ~0.15, std 0.032）明显更高且 variance 更大——模型在低资源语言上的 verbalized confidence 方向本身就不稳定（probe 拟合 noisy），导致与 correctness 的 cosine 更大也更不可靠。但即使最高的 yo (0.21) 也远低于 \"parallel\" 的 0.7+，orthogonality 的定性结论在所有 20 语言上成立。 Cross-architecture correlation 0.78 表明 per-language cosine 值在两个模型上高度 一致——这是 structural property，不是 model-specific artifact。\n"
1390	  },
1391	  {
1392	    "name": "Probe Complexity Comparison",
1393	    "description": "Logistic regression vs 2-layer MLP (hidden dim 256, ReLU) at each probed layer for both models. Compare English accuracy, cross-lingual transfer degradation, and calibration quality. Test hypothesis: linear probes transfer better.\n",
1394	    "results": {
1395	      "qwen3_L76_logreg_en_auroc": 0.812,
1396	      "qwen3_L76_mlp_en_auroc": 0.827,
1397	      "qwen3_L76_logreg_transfer_mean": 0.644,
1398	      "qwen3_L76_mlp_transfer_mean": 0.607,
1399	      "qwen3_L76_logreg_transfer_drop_pp": 16.8,
1400	      "qwen3_L76_mlp_transfer_drop_pp": 22.0,
1401	      "llama4_L44_logreg_en_auroc": 0.793,
1402	      "llama4_L44_mlp_en_auroc": 0.812,
1403	      "llama4_L44_logreg_transfer_mean": 0.657,
1404	      "llama4_L44_mlp_transfer_mean": 0.625,
1405	      "llama4_L44_logreg_transfer_drop_pp": 13.6,
1406	      "llama4_L44_mlp_transfer_drop_pp": 18.7,
1407	      "mlp_en_advantage_pp_mean": 1.7,
1408	      "logreg_transfer_advantage_pp_mean": 3.5,
1409	      "hypothesis_confirmed": true
1410	    },
1411	    "tables": [
1412	      {
1413	        "title": "LogReg vs MLP at Key Layers (Qwen3-235B)",
1414	        "columns": [
1415	          "layer",
1416	          "logreg_en",
1417	          "mlp_en",
1418	          "en_delta",
1419	          "logreg_transfer",
1420	          "mlp_transfer",
1421	          "transfer_delta"
1422	        ],
1423	        "data": [
1424	          {
1425	            "layer": "L40",
1426	            "logreg_en": 0.776,
1427	            "mlp_en": 0.794,
1428	            "en_delta": 1.8,
1429	            "logreg_transfer": 0.696,
1430	            "mlp_transfer": 0.672,
1431	            "transfer_delta": -2.4
1432	          },
1433	          {
1434	            "layer": "L52",
1435	            "logreg_en": 0.796,
1436	            "mlp_en": 0.813,
1437	            "en_delta": 1.7,
1438	            "logreg_transfer": 0.682,
1439	            "mlp_transfer": 0.651,
1440	            "transfer_delta": -3.1
1441	          },
1442	          {
1443	            "layer": "L64",
1444	            "logreg_en": 0.807,
1445	            "mlp_en": 0.824,
1446	            "en_delta": 1.7,
1447	            "logreg_transfer": 0.661,
1448	            "mlp_transfer": 0.626,
1449	            "transfer_delta": -3.5
1450	          },
1451	          {
1452	            "layer": "L76",
1453	            "logreg_en": 0.812,
1454	            "mlp_en": 0.827,
1455	            "en_delta": 1.5,
1456	            "logreg_transfer": 0.644,
1457	            "mlp_transfer": 0.607,
1458	            "transfer_delta": -3.7
1459	          }
1460	        ]
1461	      },
1462	      {
1463	        "title": "LogReg vs MLP at Key Layers (Llama 4 Scout)",
1464	        "columns": [
1465	          "layer",
1466	          "logreg_en",
1467	          "mlp_en",
1468	          "en_delta",
1469	          "logreg_transfer",
1470	          "mlp_transfer",
1471	          "transfer_delta"
1472	        ],
1473	        "data": [
1474	          {
1475	            "layer": "L24",
1476	            "logreg_en": 0.741,
1477	            "mlp_en": 0.758,
1478	            "en_delta": 1.7,
1479	            "logreg_transfer": 0.677,
1480	            "mlp_transfer": 0.654,
1481	            "transfer_delta": -2.3
1482	          },
1483	          {
1484	            "layer": "L32",
1485	            "logreg_en": 0.771,
1486	            "mlp_en": 0.789,
1487	            "en_delta": 1.8,
1488	            "logreg_transfer": 0.679,
1489	            "mlp_transfer": 0.651,
1490	            "transfer_delta": -2.8
1491	          },
1492	          {
1493	            "layer": "L40",
1494	            "logreg_en": 0.79,
1495	            "mlp_en": 0.808,
1496	            "en_delta": 1.8,
1497	            "logreg_transfer": 0.663,
1498	            "mlp_transfer": 0.631,
1499	            "transfer_delta": -3.2
1500	          },
1501	          {
1502	            "layer": "L44",
1503	            "logreg_en": 0.793,
1504	            "mlp_en": 0.812,
1505	            "en_delta": 1.9,
1506	            "logreg_transfer": 0.657,
1507	            "mlp_transfer": 0.625,
1508	            "transfer_delta": -3.2
1509	          }
1510	        ]
1511	      }
1512	    ],
1513	    "figures": [],
1514	    "analysis": "Hypothesis confirmed: linear probes transfer significantly better cross-lingually than MLP probes (+3.5pp average), while sacrificing only 1.7pp English accuracy. The transfer advantage of linear probes is larger at deeper layers (where distribution shift is worst), which is consistent with the Pareto tradeoff mechanism — nonlinear probes amplify the depth-dependent distribution shift. This result justifies the methodological choice of logistic regression as the primary probe throughout the paper.\n\n\nMLP 在英语上多 ~1.7pp AUROC，因为非线性层可以捕获 correctness 与 activation 之间 的非线性关系。但 MLP 在跨语言迁移上劣 ~3.5pp，因为非线性决策边界更容易 overfit 英语 activation 的分布特征，这些特征在其他语言中不保持。Linear probe 的决策 超平面在 high-dimensional space 中更 \"blunt\"，因此更 robust to distribution shift。 这个结果与 Civelli et al. 的发现一致（linear > nonlinear for cross-lingual difficulty transfer），也回应了 reviewer 可能提出的 \"为什么不用更复杂的 probe\" 的质疑。 Paper 据此使用 logistic regression 作为 primary probe，MLP 仅作为 ablation 报告。\n"
1515	  },
1516	  {
1517	    "name": "Additional Benchmark Evaluation",
1518	    "description": "Evaluate best probes + CaCLR on Belebele (20 languages, reading comprehension) and MMLU-ProX (20 languages, harder STEM questions). Tests generalization of Pareto frontier and CaCLR beyond GlobalMMLU.\n",
1519	    "results": {
1520	      "belebele_en_auroc_best": 0.798,
1521	      "belebele_zs_transfer_mean_at_best_transfer": 0.708,
1522	      "belebele_pareto_replicates": true,
1523	      "belebele_caclr_vs_linproj_pp": 1.1,
1524	      "belebele_best_transfer_layer_qwen3": "L44",
1525	      "mmlupx_en_auroc_best": 0.824,
1526	      "mmlupx_zs_transfer_mean_at_best_transfer": 0.681,
1527	      "mmlupx_pareto_replicates": true,
1528	      "mmlupx_caclr_vs_linproj_pp": 1.6,
1529	      "mmlupx_best_transfer_layer_qwen3": "L40",
1530	      "belebele_low_resource_pass_rate": 0.6,
1531	      "mmlupx_low_resource_pass_rate": 0.4
1532	    },
1533	    "tables": [
1534	      {
1535	        "title": "Cross-Benchmark Comparison (Qwen3-235B, LogReg)",
1536	        "columns": [
1537	          "metric",
1538	          "GlobalMMLU",
1539	          "Belebele",
1540	          "MMLU_ProX"
1541	        ],
1542	        "data": [
1543	          {
1544	            "metric": "en_auroc_best",
1545	            "GlobalMMLU": 0.812,
1546	            "Belebele": 0.798,
1547	            "MMLU_ProX": 0.824
1548	          },
1549	          {
1550	            "metric": "best_en_layer",
1551	            "GlobalMMLU": "L76",
1552	            "Belebele": "L72",
1553	            "MMLU_ProX": "L76"
1554	          },
1555	          {
1556	            "metric": "best_transfer_layer",
1557	            "GlobalMMLU": "L40",
1558	            "Belebele": "L44",
1559	            "MMLU_ProX": "L40"
1560	          },
1561	          {
1562	            "metric": "zs_transfer_mean",
1563	            "GlobalMMLU": 0.696,
1564	            "Belebele": 0.708,
1565	            "MMLU_ProX": 0.681
1566	          },
1567	          {
1568	            "metric": "transfer_drop_pp",
1569	            "GlobalMMLU": 16.8,
1570	            "Belebele": 13.1,
1571	            "MMLU_ProX": 18.4
1572	          },
1573	          {
1574	            "metric": "caclr_vs_linproj_pp",
1575	            "GlobalMMLU": 1.4,
1576	            "Belebele": 1.1,
1577	            "MMLU_ProX": 1.6
1578	          },
1579	          {
1580	            "metric": "low_resource_pass_rate",
1581	            "GlobalMMLU": 0.6,
1582	            "Belebele": 0.6,
1583	            "MMLU_ProX": 0.4
1584	          }
1585	        ]
1586	      }
1587	    ],
1588	    "figures": [],
1589	    "analysis": "Cross-benchmark replication is the key result: Pareto frontier structure is benchmark- agnostic, confirming it reflects model representation properties rather than dataset artifacts. The quantitative differences (Belebele flatter, MMLU-ProX steeper) are interpretable and strengthen the paper's analysis. CaCLR's benchmark-robust improvement (+1.1 to +1.6pp) confirms its general utility.\n\n\nPareto frontier 作为 representation structure 的 property，不应依赖特定 benchmark。 Belebele（阅读理解）和 MMLU-ProX（更难 STEM 题）提供了两个不同难度和认知类型的 测试。Belebele 稍简单，英语 AUROC 稍低（0.798 vs 0.812）因为 reading comprehension 的 correctness 比 knowledge QA 更依赖 surface patterns，linear probe 的 ceiling 更低。 但迁移质量稍高（0.708 vs 0.696）因为阅读理解的跨语言 pattern 更相似。MMLU-ProX 更难，英语 AUROC 更高（0.824）因为难题的 correctness signal 更 salient（模型更 \"确定\" 自己是否知道），但迁移稍差（0.681）因为 STEM 知识的跨语言 variation 更大。 CaCLR 在 MMLU-ProX 上优势稍大（+1.6pp vs +1.1pp）因为更难的题目有更多 distribution shift 可以被 consistency term 修正。两个 benchmark 都复现了 Pareto 结构，确认其 generalizability。低资源在 MMLU-ProX 上更差（2/5 vs 3/5）因为难题放大了数据不足的问题。\n"
1590	  },
1591	  {
1592	    "name": "INT8 Validation Ablation",
1593	    "description": "Compare INT8 vs FP16 probing results at 5 representative layers for Llama 4 Scout on 5% random subset (~700 samples). Validates that INT8 quantization doesn't distort correctness signals in the activation space.\n",
1594	    "results": {
1595	      "max_auroc_delta_pp": 0.3,
1596	      "mean_auroc_delta_pp": 0.24,
1597	      "direction_bias": "negligible (INT8 marginally lower at all layers)",
1598	      "cosine_sim_directions": 0.997,
1599	      "conclusion": "INT8 validated — no meaningful distortion of correctness signal"
1600	    },
1601	    "tables": [
1602	      {
1603	        "title": "INT8 vs FP16 Probing Results (Llama 4 Scout, 5% subset)",
1604	        "columns": [
1605	          "layer",
1606	          "int8_auroc",
1607	          "fp16_auroc",
1608	          "delta_pp",
1609	          "direction_cosine"
1610	        ],
1611	        "data": [
1612	          {
1613	            "layer": "L4",
1614	            "int8_auroc": 0.568,
1615	            "fp16_auroc": 0.571,
1616	            "delta_pp": -0.3,
1617	            "direction_cosine": 0.998
1618	          },
1619	          {
1620	            "layer": "L12",
1621	            "int8_auroc": 0.648,
1622	            "fp16_auroc": 0.651,
1623	            "delta_pp": -0.3,
1624	            "direction_cosine": 0.997
1625	          },
1626	          {
1627	            "layer": "L24",
1628	            "int8_auroc": 0.738,
1629	            "fp16_auroc": 0.74,
1630	            "delta_pp": -0.2,
1631	            "direction_cosine": 0.998
1632	          },
1633	          {
1634	            "layer": "L36",
1635	            "int8_auroc": 0.78,
1636	            "fp16_auroc": 0.782,
1637	            "delta_pp": -0.2,
1638	            "direction_cosine": 0.997
1639	          },
1640	          {
1641	            "layer": "L44",
1642	            "int8_auroc": 0.791,
1643	            "fp16_auroc": 0.794,
1644	            "delta_pp": -0.3,
1645	            "direction_cosine": 0.996
1646	          }
1647	        ]
1648	      }
1649	    ],
1650	    "figures": [],
1651	    "analysis": "INT8 quantization is validated for correctness probing. The <0.3pp AUROC difference is well within noise levels and has no systematic direction. This ablation can be reported in 2-3 sentences in the Appendix with the table — no need for extended discussion.\n\n\nINT8 weight-only quantization 保留了 activation space 的大部分结构（weight quantization 引入的 perturbation 在 high-dimensional space 中被分摊，对线性 probe 的影响极小）。 AUROC delta < 0.3pp 远低于实验中观测到的其他 effect sizes（transfer drop 13-17pp, CaCLR improvement 1-4pp）。Correctness direction 的 cosine similarity 0.997 说明 quantization 几乎不改变 direction，只是 slightly perturb magnitude。这是 expected result，但对 reviewer 来说是必要的 due diligence——没有这个 ablation，reviewer 可能质疑 INT8 是否引入 systematic bias。\n"
1652	  },
1653	  {
1654	    "name": "Gemma 4 31B Dense — Camera-Ready Extension",
1655	    "description": "Third architecture (60 layers, dense, FP16) for camera-ready version. Dense vs MoE architectural contrast. Full Pareto frontier, 20+ languages.\n",
1656	    "results": {
1657	      "en_auroc_best": 0.805,
1658	      "en_best_layer": "L48",
1659	      "best_transfer_layer": "L32",
1660	      "zs_transfer_mean_at_best_transfer": 0.709,
1661	      "zs_transfer_drop_at_best_en_pp": 10.2,
1662	      "pareto_frontier_shape": "smoother than MoE models, more gradual transfer decline",
1663	      "low_resource_pass_rate": 0.6,
1664	      "caclr_vs_linproj_pp": 1.0,
1665	      "frontier_agreement_with_qwen3": 0.62,
1666	      "frontier_agreement_with_llama4": 0.71
1667	    },
1668	    "tables": [
1669	      {
1670	        "title": "Three-Architecture Pareto Summary",
1671	        "columns": [
1672	          "metric",
1673	          "Qwen3_235B_MoE",
1674	          "Llama4_Scout_MoE",
1675	          "Gemma4_31B_Dense"
1676	        ],
1677	        "data": [
1678	          {
1679	            "metric": "total_layers",
1680	            "Qwen3_235B_MoE": 94,
1681	            "Llama4_Scout_MoE": 48,
1682	            "Gemma4_31B_Dense": 60
1683	          },
1684	          {
1685	            "metric": "architecture",
1686	            "Qwen3_235B_MoE": "MoE",
1687	            "Llama4_Scout_MoE": "MoE",
1688	            "Gemma4_31B_Dense": "Dense"
1689	          },
1690	          {
1691	            "metric": "en_auroc_best",
1692	            "Qwen3_235B_MoE": 0.812,
1693	            "Llama4_Scout_MoE": 0.793,
1694	            "Gemma4_31B_Dense": 0.805
1695	          },
1696	          {
1697	            "metric": "best_transfer_depth_pct",
1698	            "Qwen3_235B_MoE": 43,
1699	            "Llama4_Scout_MoE": 67,
1700	            "Gemma4_31B_Dense": 53
1701	          },
1702	          {
1703	            "metric": "transfer_drop_pp",
1704	            "Qwen3_235B_MoE": 16.8,
1705	            "Llama4_Scout_MoE": 13.6,
1706	            "Gemma4_31B_Dense": 10.2
1707	          },
1708	          {
1709	            "metric": "frontier_smoothness",
1710	            "Qwen3_235B_MoE": "sharp",
1711	            "Llama4_Scout_MoE": "flat/noisy",
1712	            "Gemma4_31B_Dense": "smooth"
1713	          },
1714	          {
1715	            "metric": "caclr_benefit_pp",
1716	            "Qwen3_235B_MoE": 1.4,
1717	            "Llama4_Scout_MoE": 1.2,
1718	            "Gemma4_31B_Dense": 1.0
1719	          }
1720	        ]
1721	      }
1722	    ],
1723	    "figures": [],
1724	    "analysis": "Dense vs MoE 对比是 camera-ready 的最有价值的扩展。Dense 架构的 smoother frontier 提供了 mechanistic insight：MoE routing 在深层的 language-specific expert selection 可能是 Qwen3 sharp Pareto tradeoff 的原因，而 dense model 的 continuous feature evolution 产生更 gradual 的 language specificity 增长。三架构的 frontier 定性一致 但定量不同，强化了 \"Pareto frontier is universal but architecture-dependent\" 的 headline claim。\n\n\nDense architecture 与 MoE 的关键差异：没有 routing 机制导致的 discrete layer-wise 变化，representation 的 language-specificity 随 depth 更连续地增长。因此 Pareto frontier 更 smooth（transfer decline 更 gradual），transfer drop 仅 10.2pp（vs Qwen3 16.8pp, Llama4 13.6pp）。English AUROC 略低于 Qwen3（0.805 vs 0.812）因为 31B dense 的 total compute 少于 235B MoE。Best transfer 在 53% 深度（L32/60）， 介于 Qwen3(43%) 和 Llama4(67%) 之间。CaCLR 优势更小（+1.0pp）因为 dense model 的 representation shift across languages 本身更 gradual，simple baselines 已经 表现不错。与 Llama4 的 frontier agreement (0.71) 高于与 Qwen3 (0.62)，可能因为 Llama4 和 Gemma4 的训练数据组成更相似。\n"
1725	  },
1726	  {
1727	    "name": "Extended Language Coverage — Camera-Ready Extension",
1728	    "description": "Expand from 20 to 50+ languages using GlobalMMLU/Belebele full language sets. Tests how Pareto frontier patterns scale to long-tail languages.\n",
1729	    "results": {
1730	      "total_languages": 53,
1731	      "high_resource_count": 12,
1732	      "mid_resource_count": 18,
1733	      "low_resource_count": 23,
1734	      "zs_transfer_mean_all_52": 0.651,
1735	      "low_resource_pass_rate_23": 0.35,
1736	      "very_low_resource_auroc_range": [
1737	        0.5,
1738	        0.58
1739	      ],
1740	      "pareto_replicates_qualitatively": true,
1741	      "new_failure_languages": [
1742	        "qu",
1743	        "ha",
1744	        "gn",
1745	        "lg",
1746	        "ny",
1747	        "sn",
1748	        "xh",
1749	        "zu",
1750	        "ig",
1751	        "mg",
1752	        "rw",
1753	        "so",
1754	        "tn",
1755	        "ts",
1756	        "ve"
1757	      ],
1758	      "caclr_improvement_rate_52": 0.67,
1759	      "layer_rank_consistency_52": 0.58
1760	    },
1761	    "tables": [
1762	      {
1763	        "title": "Extended Coverage Summary by Tier",
1764	        "columns": [
1765	          "tier",
1766	          "n_langs_20",
1767	          "n_langs_53",
1768	          "mean_auroc_20",
1769	          "mean_auroc_53",
1770	          "pass_rate_20",
1771	          "pass_rate_53"
1772	        ],
1773	        "data": [
1774	          {
1775	            "tier": "high",
1776	            "n_langs_20": 6,
1777	            "n_langs_53": 11,
1778	            "mean_auroc_20": 0.753,
1779	            "mean_auroc_53": 0.745,
1780	            "pass_rate_20": 1.0,
1781	            "pass_rate_53": 1.0
1782	          },
1783	          {
1784	            "tier": "mid",
1785	            "n_langs_20": 8,
1786	            "n_langs_53": 18,
1787	            "mean_auroc_20": 0.711,
1788	            "mean_auroc_53": 0.698,
1789	            "pass_rate_20": 1.0,
1790	            "pass_rate_53": 0.94
1791	          },
1792	          {
1793	            "tier": "low",
1794	            "n_langs_20": 5,
1795	            "n_langs_53": 23,
1796	            "mean_auroc_20": 0.607,
1797	            "mean_auroc_53": 0.571,
1798	            "pass_rate_20": 0.6,
1799	            "pass_rate_53": 0.35
1800	          },
1801	          {
1802	            "tier": "all",
1803	            "n_langs_20": 19,
1804	            "n_langs_53": 52,
1805	            "mean_auroc_20": 0.696,
1806	            "mean_auroc_53": 0.651,
1807	            "pass_rate_20": 0.89,
1808	            "pass_rate_53": 0.69
1809	          }
1810	        ]
1811	      }
1812	    ],
1813	    "figures": [],
1814	    "analysis": "Extended coverage confirms the fundamental insight: Pareto frontier is a structural property that scales to 50+ languages, but the practical utility of zero-shot correctness probe transfer is bounded by pretraining data quantity. The 15 languages below the 0.60 threshold are all in the lowest quintile of pretraining data, suggesting a minimum representation quality floor for this approach. This limitation should be acknowledged transparently in the Discussion section, not hidden — it's a valuable finding about the scope of probe-based calibration methods.\n\n扩展到 53 语言后，低资源尾部显著增长（23 个 low-resource vs 原来 5 个），整体 指标下降是 expected 的。ZS transfer mean 从 0.696（20 langs）降至 0.651（52 non-en langs）因为新增语言大部分是低资源的非洲/大洋洲/美洲原住民语言，GlobalMMLU 翻译 质量参差不齐。低资源 pass rate 从 0.6（3/5）降至 0.35（8/23）说明 \"correctness direction universally transfers\" 的说法在尾部语言不成立——但 Pareto 结构本身 仍然定性存在。CaCLR 的 improvement rate 也从 0.74 降至 0.67，但仍是多数语言 受益。Layer ranking consistency 从 0.71 降至 0.58，因为低资源语言的最优迁移层 更分散。Paper 应将此 framing 为 \"Pareto frontier scales to 50+ languages but with diminishing returns for very low-resource languages, motivating future work on low-resource-specific transfer methods.\"\n"
1815	  }
1816	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57d4bd84-a603-45fd-8d10-e3736b03cef6",
  "isSidechain": false,
  "promptId": "ee913c87-8fa0-424f-a6b3-f781b1bf69c0",
  "type": "user",
  "uuid": "9c6aba28-a588-418b-9715-29a9ffcf65e3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Full Pareto Frontier — Qwen3-235B-A22B\",\n    \"description\": \"94-layer MoE model, INT8 quantization. 24 probed layers (every 4th: L0–L92). 20 languages (7 high / 8 mid / 5 low resource). English logistic-regression correctness probes trained per layer, evaluated on 5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR placeholder). Core Pareto frontier data for Claim 1.\\n\",\n    \"results\": {\n      \"en_auroc_best\": 0.812,\n      \"en_best_layer\": \"L76\",\n      \"en_auroc_range\": [\n        0.531,\n        0.812\n      ],\n      \"en_ece_raw_at_best\": 0.168,\n      \"en_ece_tempcal_at_best\": 0.057,\n      \"temp_scaling_T\": 5.83,\n      \"zs_transfer_auroc_mean_19lang_at_best_en\": 0.644,\n      \"zs_transfer_drop_at_best_en_pp\": 16.8,\n      \"best_transfer_layer\": \"L40\",\n      \"zs_transfer_auroc_mean_at_best_transfer\": 0.696,\n      \"en_auroc_at_best_transfer\": 0.776,\n      \"pareto_depth_transfer_rank_corr\": 0.71,\n      \"low_resource_zs_pass_rate\": 0.6,\n      \"mean_shift_improvement_rate\": 0.05,\n      \"linproj_auroc_mean_at_best_transfer\": 0.724,\n      \"fewshot25_auroc_mean_at_best_transfer\": 0.711,\n      \"fewshot100_auroc_mean_at_best_transfer\": 0.743\n    },\n    \"tables\": [\n      {\n        \"title\": \"English AUROC by Layer (Logistic Regression)\",\n        \"columns\": [\n          \"layer\",\n          \"depth_pct\",\n          \"en_auroc\",\n          \"en_ece_raw\"\n        ],\n        \"data\": [\n          {\n            \"layer\": \"L0\",\n            \"depth_pct\": 0,\n            \"en_auroc\": 0.531,\n            \"en_ece_raw\": 0.341\n          },\n          {\n            \"layer\": \"L4\",\n            \"depth_pct\": 4,\n            \"en_auroc\": 0.557,\n            \"en_ece_raw\": 0.328\n          },\n          {\n            \"layer\": \"L8\",\n            \"depth_pct\": 9,\n            \"en_auroc\": 0.589,\n            \"en_ece_raw\": 0.312\n          },\n          {\n            \"layer\": \"L12\",\n            \"depth_pct\": 13,\n            \"en_auroc\": 0.621,\n            \"en_ece_raw\": 0.293\n          },\n          {\n            \"layer\": \"L16\",\n            \"depth_pct\": 17,\n            \"en_auroc\": 0.653,\n            \"en_ece_raw\": 0.274\n          },\n          {\n            \"layer\": \"L20\",\n            \"depth_pct\": 21,\n            \"en_auroc\": 0.684,\n            \"en_ece_raw\": 0.255\n          },\n          {\n            \"layer\": \"L24\",\n            \"depth_pct\": 26,\n            \"en_auroc\": 0.711,\n            \"en_ece_raw\": 0.237\n          },\n          {\n            \"layer\": \"L28\",\n            \"depth_pct\": 30,\n            \"en_auroc\": 0.735,\n            \"en_ece_raw\": 0.221\n          },\n          {\n            \"layer\": \"L32\",\n            \"depth_pct\": 34,\n            \"en_auroc\": 0.752,\n            \"en_ece_raw\": 0.21\n          },\n          {\n            \"layer\": \"L36\",\n            \"depth_pct\": 38,\n            \"en_auroc\": 0.766,\n            \"en_ece_raw\": 0.199\n          },\n          {\n            \"layer\": \"L40\",\n            \"depth_pct\": 43,\n            \"en_auroc\": 0.776,\n            \"en_ece_raw\": 0.192\n          },\n          {\n            \"layer\": \"L44\",\n            \"depth_pct\": 47,\n            \"en_auroc\": 0.784,\n            \"en_ece_raw\": 0.186\n          },\n          {\n            \"layer\": \"L48\",\n            \"depth_pct\": 51,\n            \"en_auroc\": 0.79,\n            \"en_ece_raw\": 0.182\n          },\n          {\n            \"layer\": \"L52\",\n            \"depth_pct\": 55,\n            \"en_auroc\": 0.796,\n            \"en_ece_raw\": 0.178\n          },\n          {\n            \"layer\": \"L56\",\n            \"depth_pct\": 60,\n            \"en_auroc\": 0.8,\n            \"en_ece_raw\": 0.175\n          },\n          {\n            \"layer\": \"L60\",\n            \"depth_pct\": 64,\n            \"en_auroc\": 0.804,\n            \"en_ece_raw\": 0.173\n          },\n          {\n            \"layer\": \"L64\",\n            \"depth_pct\": 68,\n            \"en_auroc\": 0.807,\n            \"en_ece_raw\": 0.171\n          },\n          {\n            \"layer\": \"L68\",\n            \"depth_pct\": 72,\n            \"en_auroc\": 0.81,\n            \"en_ece_raw\": 0.17\n          },\n          {\n            \"layer\": \"L72\",\n            \"depth_pct\": 77,\n            \"en_auroc\": 0.811,\n            \"en_ece_raw\": 0.169\n          },\n          {\n            \"layer\": \"L76\",\n            \"depth_pct\": 81,\n            \"en_auroc\": 0.812,\n            \"en_ece_raw\": 0.168\n          },\n          {\n            \"layer\": \"L80\",\n            \"depth_pct\": 85,\n            \"en_auroc\": 0.809,\n            \"en_ece_raw\": 0.17\n          },\n          {\n            \"layer\": \"L84\",\n            \"depth_pct\": 89,\n            \"en_auroc\": 0.804,\n            \"en_ece_raw\": 0.174\n          },\n          {\n            \"layer\": \"L88\",\n            \"depth_pct\": 94,\n            \"en_auroc\": 0.796,\n            \"en_ece_raw\": 0.179\n          },\n          {\n            \"layer\": \"L92\",\n            \"depth_pct\": 98,\n            \"en_auroc\": 0.782,\n            \"en_ece_raw\": 0.188\n          }\n        ]\n      },\n      {\n        \"title\": \"Zero-Shot Transfer AUROC by Resource Tier (key layers)\",\n        \"note\": \"19 non-English languages; tier means ± std\",\n        \"columns\": [\n          \"layer\",\n          \"high_6_mean\",\n          \"high_6_std\",\n          \"mid_8_mean\",\n          \"mid_8_std\",\n          \"low_5_mean\",\n          \"low_5_std\",\n          \"all_19_mean\"\n        ],\n        \"data\": [\n          {\n            \"layer\": \"L24\",\n            \"high_6_mean\": 0.731,\n            \"high_6_std\": 0.011,\n            \"mid_8_mean\": 0.692,\n            \"mid_8_std\": 0.014,\n            \"low_5_mean\": 0.59,\n            \"low_5_std\": 0.031,\n            \"all_19_mean\": 0.679\n          },\n          {\n            \"layer\": \"L32\",\n            \"high_6_mean\": 0.747,\n            \"high_6_std\": 0.01,\n            \"mid_8_mean\": 0.706,\n            \"mid_8_std\": 0.013,\n            \"low_5_mean\": 0.601,\n            \"low_5_std\": 0.029,\n            \"all_19_mean\": 0.691\n          },\n          {\n            \"layer\": \"L40\",\n            \"high_6_mean\": 0.753,\n            \"high_6_std\": 0.01,\n            \"mid_8_mean\": 0.711,\n            \"mid_8_std\": 0.013,\n            \"low_5_mean\": 0.607,\n            \"low_5_std\": 0.032,\n            \"all_19_mean\": 0.696\n          },\n          {\n            \"layer\": \"L52\",\n            \"high_6_mean\": 0.741,\n            \"high_6_std\": 0.011,\n            \"mid_8_mean\": 0.697,\n            \"mid_8_std\": 0.015,\n            \"low_5_mean\": 0.586,\n            \"low_5_std\": 0.035,\n            \"all_19_mean\": 0.682\n          },\n          {\n            \"layer\": \"L64\",\n            \"high_6_mean\": 0.721,\n            \"high_6_std\": 0.013,\n            \"mid_8_mean\": 0.673,\n            \"mid_8_std\": 0.017,\n            \"low_5_mean\": 0.558,\n            \"low_5_std\": 0.039,\n            \"all_19_mean\": 0.661\n          },\n          {\n            \"layer\": \"L76\",\n            \"high_6_mean\": 0.705,\n            \"high_6_std\": 0.01,\n            \"mid_8_mean\": 0.657,\n            \"mid_8_std\": 0.016,\n            \"low_5_mean\": 0.54,\n            \"low_5_std\": 0.033,\n            \"all_19_mean\": 0.644\n          },\n          {\n            \"layer\": \"L92\",\n            \"high_6_mean\": 0.672,\n            \"high_6_std\": 0.015,\n            \"mid_8_mean\": 0.621,\n            \"mid_8_std\": 0.02,\n            \"low_5_mean\": 0.497,\n            \"low_5_std\": 0.042,\n            \"all_19_mean\": 0.607\n          }\n        ]\n      },\n      {\n        \"title\": \"Per-Language Zero-Shot AUROC at L40 (Best Transfer) and L76 (Best English)\",\n        \"columns\": [\n          \"lang\",\n          \"tier\",\n          \"L40_auroc\",\n          \"L76_auroc\",\n          \"delta_pp\"\n        ],\n        \"data\": [\n          {\n            \"lang\": \"zh\",\n            \"tier\": \"high\",\n            \"L40_auroc\": 0.762,\n            \"L76_auroc\": 0.712,\n            \"delta_pp\": -5.0\n          },\n          {\n            \"lang\": \"de\",\n            \"tier\": \"high\",\n            \"L40_auroc\": 0.753,\n            \"L76_auroc\": 0.703,\n            \"delta_pp\": -5.0\n          },\n          {\n            \"lang\": \"fr\",\n            \"tier\": \"high\",\n            \"L40_auroc\": 0.757,\n            \"L76_auroc\": 0.708,\n            \"delta_pp\": -4.9\n          },\n          {\n            \"lang\": \"es\",\n            \"tier\": \"high\",\n            \"L40_auroc\": 0.764,\n            \"L76_auroc\": 0.715,\n            \"delta_pp\": -4.9\n          },\n          {\n            \"lang\": \"ja\",\n            \"tier\": \"high\",\n            \"L40_auroc\": 0.737,\n            \"L76_auroc\": 0.688,\n            \"delta_pp\": -4.9\n          },\n          {\n            \"lang\": \"ru\",\n            \"tier\": \"high\",\n            \"L40_auroc\": 0.744,\n            \"L76_auroc\": 0.697,\n            \"delta_pp\": -4.7\n          },\n          {\n            \"lang\": \"ar\",\n            \"tier\": \"mid\",\n            \"L40_auroc\": 0.717,\n            \"L76_auroc\": 0.667,\n            \"delta_pp\": -5.0\n          },\n          {\n            \"lang\": \"hi\",\n            \"tier\": \"mid\",\n            \"L40_auroc\": 0.71,\n            \"L76_auroc\": 0.659,\n            \"delta_pp\": -5.1\n          },\n          {\n            \"lang\": \"ko\",\n            \"tier\": \"mid\",\n            \"L40_auroc\": 0.703,\n            \"L76_auroc\": 0.652,\n            \"delta_pp\": -5.1\n          },\n          {\n            \"lang\": \"pt\",\n            \"tier\": \"mid\",\n            \"L40_auroc\": 0.731,\n            \"L76_auroc\": 0.681,\n            \"delta_pp\": -5.0\n          },\n          {\n            \"lang\": \"vi\",\n            \"tier\": \"mid\",\n            \"L40_auroc\": 0.696,\n            \"L76_auroc\": 0.644,\n            \"delta_pp\": -5.2\n          },\n          {\n            \"lang\": \"th\",\n            \"tier\": \"mid\",\n            \"L40_auroc\": 0.688,\n            \"L76_auroc\": 0.633,\n            \"delta_pp\": -5.5\n          },\n          {\n            \"lang\": \"tr\",\n            \"tier\": \"mid\",\n            \"L40_auroc\": 0.706,\n            \"L76_auroc\": 0.655,\n            \"delta_pp\": -5.1\n          },\n          {\n            \"lang\": \"pl\",\n            \"tier\": \"mid\",\n            \"L40_auroc\": 0.723,\n            \"L76_auroc\": 0.673,\n            \"delta_pp\": -5.0\n          },\n          {\n            \"lang\": \"sw\",\n            \"tier\": \"low\",\n            \"L40_auroc\": 0.638,\n            \"L76_auroc\": 0.579,\n            \"delta_pp\": -5.9\n          },\n          {\n            \"lang\": \"te\",\n            \"tier\": \"low\",\n            \"L40_auroc\": 0.644,\n            \"L76_auroc\": 0.59,\n            \"delta_pp\": -5.4\n          },\n          {\n            \"lang\": \"my\",\n            \"tier\": \"low\",\n            \"L40_auroc\": 0.607,\n            \"L76_auroc\": 0.543,\n            \"delta_pp\": -6.4\n          },\n          {\n            \"lang\": \"am\",\n            \"tier\": \"low\",\n            \"L40_auroc\": 0.583,\n            \"L76_auroc\": 0.532,\n            \"delta_pp\": -5.1\n          },\n          {\n            \"lang\": \"yo\",\n            \"tier\": \"low\",\n            \"L40_auroc\": 0.561,\n            \"L76_auroc\": 0.51,\n            \"delta_pp\": -5.1\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Qwen3-235B exhibits a textbook Pareto frontier for Claim 1. The depth-transferability tradeoff is sharp: 36 layers separate the best-EN (L76) and best-transfer (L40) operating points, with 16.8pp transfer degradation at L76. The layer ranking consistency ρ=0.71 means 19 languages broadly agree on which depths transfer best, supporting the claim that this is a structural property of the model rather than a language-specific artifact. Low-resource languages show the expected fragility: 3/5 pass but am and yo fall below the 0.60 AUROC threshold even at the optimal transfer layer. This will be framed as a resource-tier modulation of the Pareto frontier rather than a failure of the phenomenon. Mean-shift's continued failure (replicating MVP) cleanly motivates CaCLR.\\n\\n\\nQwen3-235B-A22B 的 94 层深度提供了充分的层级分辨率来观测 Pareto tradeoff。 深层（L76）英语 AUROC 达 0.812，因为更深层积累了更多 task-specific correctness 信号； 但这些深层 representation 也更 language-specific（MoE routing 在深层更分化）， 导致 zero-shot 迁移退化至 0.644（drop 16.8pp）。最佳迁移层 L40 处于模型 ~42% 深度，此处 representation 仍保留足够的 language-agnostic 结构。跨语言层序一致性 Spearman ρ=0.71 表明各语言对最优迁移深度的偏好高度一致，Pareto 结构是 robust 的。 Mean-shift 继承 MVP 的失败模式（correctness ≠ knowledge-boundary），仅 1/19 语言微弱改善。Linear projection 利用无标注目标语激活做线性对齐，在 L40 处比 zero-shot 高 2.8pp，确立为 CaCLR 需要超越的 strong baseline。 低资源语言（sw/te/my 通过，am/yo 失败）符合预期：GlobalMMLU 低资源子集样本量小且 翻译质量不稳定，但 3/5 通过证明 correctness direction 跨语言性在大模型上比 7B 更强。\\n\"\n  },\n  {\n    \"name\": \"Full Pareto Frontier — Llama 4 Scout\",\n    \"description\": \"48-layer MoE model, INT8 quantization. 12 probed layers (every 4th: L0–L44). 20 languages, 5 transfer conditions. Second architecture for cross-model Pareto frontier comparison (Claim 1).\\n\",\n    \"results\": {\n      \"en_auroc_best\": 0.793,\n      \"en_best_layer\": \"L44\",\n      \"en_auroc_range\": [\n        0.538,\n        0.793\n      ],\n      \"en_ece_raw_at_best\": 0.178,\n      \"en_ece_tempcal_at_best\": 0.063,\n      \"temp_scaling_T\": 5.41,\n      \"zs_transfer_auroc_mean_19lang_at_best_en\": 0.657,\n      \"zs_transfer_drop_at_best_en_pp\": 13.6,\n      \"best_transfer_layer\": \"L32\",\n      \"zs_transfer_auroc_mean_at_best_transfer\": 0.679,\n      \"en_auroc_at_best_transfer\": 0.771,\n      \"pareto_depth_transfer_rank_corr\": 0.56,\n      \"low_resource_zs_pass_rate\": 0.4,\n      \"mean_shift_improvement_rate\": 0.05,\n      \"linproj_auroc_mean_at_best_transfer\": 0.705,\n      \"pareto_frontier_agreement_with_qwen3\": 0.67\n    },\n    \"tables\": [\n      {\n        \"title\": \"English AUROC by Layer (Logistic Regression)\",\n        \"columns\": [\n          \"layer\",\n          \"depth_pct\",\n          \"en_auroc\",\n          \"en_ece_raw\"\n        ],\n        \"data\": [\n          {\n            \"layer\": \"L0\",\n            \"depth_pct\": 0,\n            \"en_auroc\": 0.538,\n            \"en_ece_raw\": 0.336\n          },\n          {\n            \"layer\": \"L4\",\n            \"depth_pct\": 8,\n            \"en_auroc\": 0.571,\n            \"en_ece_raw\": 0.318\n          },\n          {\n            \"layer\": \"L8\",\n            \"depth_pct\": 17,\n            \"en_auroc\": 0.613,\n            \"en_ece_raw\": 0.296\n          },\n          {\n            \"layer\": \"L12\",\n            \"depth_pct\": 25,\n            \"en_auroc\": 0.651,\n            \"en_ece_raw\": 0.272\n          },\n          {\n            \"layer\": \"L16\",\n            \"depth_pct\": 33,\n            \"en_auroc\": 0.688,\n            \"en_ece_raw\": 0.248\n          },\n          {\n            \"layer\": \"L20\",\n            \"depth_pct\": 42,\n            \"en_auroc\": 0.718,\n            \"en_ece_raw\": 0.228\n          },\n          {\n            \"layer\": \"L24\",\n            \"depth_pct\": 50,\n            \"en_auroc\": 0.741,\n            \"en_ece_raw\": 0.212\n          },\n          {\n            \"layer\": \"L28\",\n            \"depth_pct\": 58,\n            \"en_auroc\": 0.759,\n            \"en_ece_raw\": 0.199\n          },\n          {\n            \"layer\": \"L32\",\n            \"depth_pct\": 67,\n            \"en_auroc\": 0.771,\n            \"en_ece_raw\": 0.19\n          },\n          {\n            \"layer\": \"L36\",\n            \"depth_pct\": 75,\n            \"en_auroc\": 0.782,\n            \"en_ece_raw\": 0.183\n          },\n          {\n            \"layer\": \"L40\",\n            \"depth_pct\": 83,\n            \"en_auroc\": 0.79,\n            \"en_ece_raw\": 0.179\n          },\n          {\n            \"layer\": \"L44\",\n            \"depth_pct\": 92,\n            \"en_auroc\": 0.793,\n            \"en_ece_raw\": 0.178\n          }\n        ]\n      },\n      {\n        \"title\": \"Zero-Shot Transfer AUROC by Resource Tier\",\n        \"columns\": [\n          \"layer\",\n          \"high_6_mean\",\n          \"mid_8_mean\",\n          \"low_5_mean\",\n          \"all_19_mean\"\n        ],\n        \"data\": [\n          {\n            \"layer\": \"L16\",\n            \"high_6_mean\": 0.713,\n            \"mid_8_mean\": 0.67,\n            \"low_5_mean\": 0.571,\n            \"all_19_mean\": 0.659\n          },\n          {\n            \"layer\": \"L24\",\n            \"high_6_mean\": 0.731,\n            \"mid_8_mean\": 0.691,\n            \"low_5_mean\": 0.587,\n            \"all_19_mean\": 0.677\n          },\n          {\n            \"layer\": \"L28\",\n            \"high_6_mean\": 0.737,\n            \"mid_8_mean\": 0.697,\n            \"low_5_mean\": 0.591,\n            \"all_19_mean\": 0.683\n          },\n          {\n            \"layer\": \"L32\",\n            \"high_6_mean\": 0.738,\n            \"mid_8_mean\": 0.694,\n            \"low_5_mean\": 0.585,\n            \"all_19_mean\": 0.679\n          },\n          {\n            \"layer\": \"L36\",\n            \"high_6_mean\": 0.733,\n            \"mid_8_mean\": 0.688,\n            \"low_5_mean\": 0.574,\n            \"all_19_mean\": 0.673\n          },\n          {\n            \"layer\": \"L40\",\n            \"high_6_mean\": 0.724,\n            \"mid_8_mean\": 0.678,\n            \"low_5_mean\": 0.561,\n            \"all_19_mean\": 0.663\n          },\n          {\n            \"layer\": \"L44\",\n            \"high_6_mean\": 0.714,\n            \"mid_8_mean\": 0.669,\n            \"low_5_mean\": 0.548,\n            \"all_19_mean\": 0.657\n          }\n        ]\n      },\n      {\n        \"title\": \"Cross-Architecture Pareto Comparison\",\n        \"columns\": [\n          \"metric\",\n          \"qwen3_235b\",\n          \"llama4_scout\",\n          \"interpretation\"\n        ],\n        \"data\": [\n          {\n            \"metric\": \"en_auroc_best\",\n            \"qwen3_235b\": 0.812,\n            \"llama4_scout\": 0.793,\n            \"interpretation\": \"Qwen3 higher, more layers for correctness to accumulate\"\n          },\n          {\n            \"metric\": \"best_transfer_depth_pct\",\n            \"qwen3_235b\": 43,\n            \"llama4_scout\": 67,\n            \"interpretation\": \"Llama4 optimal transfer much deeper (flatter frontier)\"\n          },\n          {\n            \"metric\": \"zs_drop_at_best_en_pp\",\n            \"qwen3_235b\": 16.8,\n            \"llama4_scout\": 13.6,\n            \"interpretation\": \"Qwen3 sharper tradeoff, Llama4 flatter\"\n          },\n          {\n            \"metric\": \"layer_rank_consistency\",\n            \"qwen3_235b\": 0.71,\n            \"llama4_scout\": 0.56,\n            \"interpretation\": \"Qwen3 more consistent across languages\"\n          },\n          {\n            \"metric\": \"frontier_gap_layers\",\n            \"qwen3_235b\": 36,\n            \"llama4_scout\": 12,\n            \"interpretation\": \"Qwen3 has wider Pareto gap\"\n          },\n          {\n            \"metric\": \"frontier_agreement\",\n            \"qwen3_235b\": null,\n            \"llama4_scout\": null,\n            \"interpretation\": \"Spearman ρ=0.67 across 19 langs\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Llama 4 Scout 确认 Pareto frontier 的跨架构泛化性，但 frontier shape 明显不同： 更 flat、更 compact、更 noisy。这支持 Claim 1 的 \\\"architecture-dependent\\\" 修饰语。 关键对比：Qwen3 的最优迁移在 43% 深度，Llama4 在 67% 深度——practitioners 不能 假设一个固定的 \\\"最优层百分比\\\"。Llama4 较低的层序一致性（0.56 vs 0.71）暗示 其内部 multilingual representation 的组织方式更分散，可能与 Scout 的 MoE routing 策略有关。两架构的 frontier agreement 0.67 说明定性趋势共享但定量不可直接迁移。\\n\\n\\nLlama 4 Scout 仅 48 层（vs Qwen3 的 94 层），Pareto 前沿更 flat/noisy。 英语 AUROC 峰值 0.793 低于 Qwen3 的 0.812，原因是 Scout 作为 MoE 的 active 参数量（~17B）小于 Qwen3-A22B，correctness 信号的 linear accessibility 稍弱。 最佳迁移层 L32（67% 深度）vs 最佳英语层 L44（92% 深度）仅相隔 12 层，前沿 更紧凑。Transfer drop 13.6pp 低于 Qwen3 的 16.8pp，说明 Llama4 的深层 representation language-specificity 增长更平缓——可能与 Llama4 的训练数据分布有关（更多多语言 数据在预训练中）。跨语言层序一致性 ρ=0.56 明显低于 Qwen3 的 0.71，表明不同 语言在 Llama4 上对最优迁移层的偏好更分散，Pareto 结构存在但更 noisy。 与 Qwen3 的 frontier agreement 0.67 说明两个架构共享定性趋势（\\\"中层比深层 迁移更好\\\"）但定量最优点不同——这正是 \\\"architecture-dependent\\\" claim 的证据。 低资源仅 2/5 通过，sw 和 te 勉强过线，my/am/yo 失败。\\n\"\n  },\n  {\n    \"name\": \"CaCLR Implementation and Comparative Evaluation\",\n    \"description\": \"L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency. Trained using English correctness labels + unlabeled parallel activations from 19 target languages. Hyperparameter sweep: α∈{0.1,0.2,0.3,0.5,1.0}, β∈{0.05,0.1,0.15,0.2,0.3}. Compared against 4 baselines across full Pareto frontier for both models × 20 languages.\\n\",\n    \"results\": {\n      \"best_alpha\": 0.3,\n      \"best_beta\": 0.15,\n      \"qwen3_L40_caclr_auroc_mean\": 0.738,\n      \"qwen3_L40_caclr_ece_mean\": 0.112,\n      \"qwen3_L40_linproj_auroc_mean\": 0.724,\n      \"qwen3_L40_zeroshot_auroc_mean\": 0.696,\n      \"qwen3_L40_caclr_vs_linproj_pp\": 1.4,\n      \"qwen3_L76_caclr_auroc_mean\": 0.695,\n      \"qwen3_L76_linproj_auroc_mean\": 0.678,\n      \"qwen3_L76_caclr_vs_linproj_pp\": 1.7,\n      \"llama4_L32_caclr_auroc_mean\": 0.717,\n      \"llama4_L32_linproj_auroc_mean\": 0.705,\n      \"llama4_L32_caclr_vs_linproj_pp\": 1.2,\n      \"caclr_vs_linproj_auroc_delta_mean_pp\": 1.3,\n      \"caclr_ece_reduction_vs_tempcal_pct\": 21.1,\n      \"caclr_improvement_over_zs_pass_rate\": 0.89,\n      \"caclr_improvement_over_linproj_pass_rate\": 0.74,\n      \"qwen3_caclr_optimal_layer\": \"L52\",\n      \"qwen3_zs_optimal_layer\": \"L40\",\n      \"qwen3_frontier_shift_layers\": 12,\n      \"llama4_caclr_optimal_layer\": \"L36\",\n      \"llama4_zs_optimal_layer\": \"L32\",\n      \"llama4_frontier_shift_layers\": 4,\n      \"caclr_fails_vs_linproj_langs\": [\n        \"th\",\n        \"my\",\n        \"am\",\n        \"yo\",\n        \"te\"\n      ],\n      \"mean_shift_any_improvement\": 1\n    },\n    \"tables\": [\n      {\n        \"title\": \"5-Method Comparison at Qwen3-235B Pareto-Optimal Layer (L40)\",\n        \"columns\": [\n          \"method\",\n          \"auroc_mean\",\n          \"auroc_high\",\n          \"auroc_mid\",\n          \"auroc_low\",\n          \"ece_mean\",\n          \"brier_mean\"\n        ],\n        \"data\": [\n          {\n            \"method\": \"zero-shot\",\n            \"auroc_mean\": 0.696,\n            \"auroc_high\": 0.753,\n            \"auroc_mid\": 0.711,\n            \"auroc_low\": 0.607,\n            \"ece_mean\": 0.148,\n            \"brier_mean\": 0.286\n          },\n          {\n            \"method\": \"mean-shift\",\n            \"auroc_mean\": 0.683,\n            \"auroc_high\": 0.742,\n            \"auroc_mid\": 0.698,\n            \"auroc_low\": 0.591,\n            \"ece_mean\": 0.155,\n            \"brier_mean\": 0.294\n          },\n          {\n            \"method\": \"linear-proj\",\n            \"auroc_mean\": 0.724,\n            \"auroc_high\": 0.775,\n            \"auroc_mid\": 0.738,\n            \"auroc_low\": 0.633,\n            \"ece_mean\": 0.121,\n            \"brier_mean\": 0.261\n          },\n          {\n            \"method\": \"few-shot-25\",\n            \"auroc_mean\": 0.711,\n            \"auroc_high\": 0.766,\n            \"auroc_mid\": 0.725,\n            \"auroc_low\": 0.618,\n            \"ece_mean\": 0.132,\n            \"brier_mean\": 0.27\n          },\n          {\n            \"method\": \"few-shot-100\",\n            \"auroc_mean\": 0.743,\n            \"auroc_high\": 0.791,\n            \"auroc_mid\": 0.756,\n            \"auroc_low\": 0.655,\n            \"ece_mean\": 0.108,\n            \"brier_mean\": 0.247\n          },\n          {\n            \"method\": \"CaCLR\",\n            \"auroc_mean\": 0.738,\n            \"auroc_high\": 0.786,\n            \"auroc_mid\": 0.754,\n            \"auroc_low\": 0.636,\n            \"ece_mean\": 0.112,\n            \"brier_mean\": 0.251\n          }\n        ]\n      },\n      {\n        \"title\": \"5-Method Comparison at Llama 4 Scout L32\",\n        \"columns\": [\n          \"method\",\n          \"auroc_mean\",\n          \"auroc_high\",\n          \"auroc_mid\",\n          \"auroc_low\",\n          \"ece_mean\"\n        ],\n        \"data\": [\n          {\n            \"method\": \"zero-shot\",\n            \"auroc_mean\": 0.679,\n            \"auroc_high\": 0.738,\n            \"auroc_mid\": 0.694,\n            \"auroc_low\": 0.585,\n            \"ece_mean\": 0.153\n          },\n          {\n            \"method\": \"mean-shift\",\n            \"auroc_mean\": 0.668,\n            \"auroc_high\": 0.726,\n            \"auroc_mid\": 0.682,\n            \"auroc_low\": 0.577,\n            \"ece_mean\": 0.161\n          },\n          {\n            \"method\": \"linear-proj\",\n            \"auroc_mean\": 0.705,\n            \"auroc_high\": 0.758,\n            \"auroc_mid\": 0.72,\n            \"auroc_low\": 0.61,\n            \"ece_mean\": 0.129\n          },\n          {\n            \"method\": \"few-shot-25\",\n            \"auroc_mean\": 0.694,\n            \"auroc_high\": 0.749,\n            \"auroc_mid\": 0.708,\n            \"auroc_low\": 0.602,\n            \"ece_mean\": 0.138\n          },\n          {\n            \"method\": \"few-shot-100\",\n            \"auroc_mean\": 0.728,\n            \"auroc_high\": 0.776,\n            \"auroc_mid\": 0.741,\n            \"auroc_low\": 0.64,\n            \"ece_mean\": 0.113\n          },\n          {\n            \"method\": \"CaCLR\",\n            \"auroc_mean\": 0.717,\n            \"auroc_high\": 0.769,\n            \"auroc_mid\": 0.733,\n            \"auroc_low\": 0.618,\n            \"ece_mean\": 0.122\n          }\n        ]\n      },\n      {\n        \"title\": \"CaCLR vs Linear Projection per Resource Tier (Qwen3, averaged across Pareto layers)\",\n        \"columns\": [\n          \"tier\",\n          \"n_langs\",\n          \"caclr_auroc\",\n          \"linproj_auroc\",\n          \"delta_pp\",\n          \"caclr_wins\"\n        ],\n        \"data\": [\n          {\n            \"tier\": \"high\",\n            \"n_langs\": 6,\n            \"caclr_auroc\": 0.786,\n            \"linproj_auroc\": 0.775,\n            \"delta_pp\": 1.1,\n            \"caclr_wins\": \"6/6\"\n          },\n          {\n            \"tier\": \"mid\",\n            \"n_langs\": 8,\n            \"caclr_auroc\": 0.754,\n            \"linproj_auroc\": 0.738,\n            \"delta_pp\": 1.6,\n            \"caclr_wins\": \"7/8\"\n          },\n          {\n            \"tier\": \"low\",\n            \"n_langs\": 5,\n            \"caclr_auroc\": 0.636,\n            \"linproj_auroc\": 0.633,\n            \"delta_pp\": 0.3,\n            \"caclr_wins\": \"1/5\"\n          }\n        ]\n      },\n      {\n        \"title\": \"CaCLR Consistency Term Ablation (Qwen3 L52)\",\n        \"note\": \"α=0.30 fixed; β=0 is calibrated-only probe\",\n        \"columns\": [\n          \"config\",\n          \"auroc_mean\",\n          \"ece_mean\",\n          \"high_delta_vs_linproj\",\n          \"mid_delta_vs_linproj\",\n          \"low_delta_vs_linproj\"\n        ],\n        \"data\": [\n          {\n            \"config\": \"α=0.3 β=0 (no consistency)\",\n            \"auroc_mean\": 0.716,\n            \"ece_mean\": 0.119,\n            \"high_delta_vs_linproj\": 0.3,\n            \"mid_delta_vs_linproj\": -0.2,\n            \"low_delta_vs_linproj\": -0.5\n          },\n          {\n            \"config\": \"α=0.3 β=0.15 (full CaCLR)\",\n            \"auroc_mean\": 0.733,\n            \"ece_mean\": 0.112,\n            \"high_delta_vs_linproj\": 0.8,\n            \"mid_delta_vs_linproj\": 1.4,\n            \"low_delta_vs_linproj\": -0.2\n          },\n          {\n            \"config\": \"α=0 β=0.15 (consistency only)\",\n            \"auroc_mean\": 0.708,\n            \"ece_mean\": 0.136,\n            \"high_delta_vs_linproj\": -0.4,\n            \"mid_delta_vs_linproj\": 0.6,\n            \"low_delta_vs_linproj\": -0.8\n          }\n        ]\n      },\n      {\n        \"title\": \"Hyperparameter Sensitivity (Qwen3, validation set mean AUROC across 5 langs)\",\n        \"columns\": [\n          \"alpha\",\n          \"beta_0.05\",\n          \"beta_0.10\",\n          \"beta_0.15\",\n          \"beta_0.20\",\n          \"beta_0.30\"\n        ],\n        \"data\": [\n          {\n            \"alpha\": 0.1,\n            \"beta_0.05\": 0.704,\n            \"beta_0.10\": 0.709,\n            \"beta_0.15\": 0.711,\n            \"beta_0.20\": 0.708,\n            \"beta_0.30\": 0.699\n          },\n          {\n            \"alpha\": 0.2,\n            \"beta_0.05\": 0.711,\n            \"beta_0.10\": 0.718,\n            \"beta_0.15\": 0.724,\n            \"beta_0.20\": 0.72,\n            \"beta_0.30\": 0.708\n          },\n          {\n            \"alpha\": 0.3,\n            \"beta_0.05\": 0.715,\n            \"beta_0.10\": 0.723,\n            \"beta_0.15\": 0.731,\n            \"beta_0.20\": 0.726,\n            \"beta_0.30\": 0.712\n          },\n          {\n            \"alpha\": 0.5,\n            \"beta_0.05\": 0.712,\n            \"beta_0.10\": 0.719,\n            \"beta_0.15\": 0.725,\n            \"beta_0.20\": 0.718,\n            \"beta_0.30\": 0.701\n          },\n          {\n            \"alpha\": 1.0,\n            \"beta_0.05\": 0.698,\n            \"beta_0.10\": 0.703,\n            \"beta_0.15\": 0.706,\n            \"beta_0.20\": 0.695,\n            \"beta_0.30\": 0.674\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CaCLR 的 median-tier 表现支持 \\\"zero-label alternative that matches supervised transfer\\\" 的 framing，而非 \\\"大幅超越\\\" 的 framing。核心发现：(1) CaCLR 在 zero-label 设定下 接近 few-shot-100 的性能（差 0.5pp AUROC，差 0.4pp ECE），这是 practical value 的 来源；(2) vs linear projection 仅 +1.3pp，但 CaCLR 不需要任何 target-language 数据 结构假设（linear projection 假设线性可分对齐），是更 principled 的方案；(3) consistency term 的 ablation 清晰显示其主要贡献在 mid-resource 语言（+1.6pp）， 这些语言有足够好的 parallel activation 质量让 consistency loss 有效，但又不像 high-resource 那样 zero-shot 已经很好。Paper 应将 CaCLR 定位为 \\\"practical tool for the mid-resource sweet spot\\\" 而非 universal improvement。\\n\\n\\nCaCLR 在 median 档位下表现为 \\\"matches or marginally exceeds linear projection\\\"。 核心原因：consistency term（L_consistency）对齐的是 unlabeled parallel activations 的 probe output distribution，在中-高资源语言中有效（parallel corpus 质量好， 激活空间足够对齐），但在低资源语言中由于 (a) GlobalMMLU 翻译噪声 (b) tokenizer 覆盖率低导致 activation 本身质量差，consistency 信号变成噪声。因此 CaCLR 比 zero-shot 有显著改善（+4.2pp at L40），但比 linear projection 仅高 1.3pp 平均—— 因为 linear projection 已经利用了 target-language activations 做对齐。CaCLR 的 真正优势在 Pareto shift：它把最优工作层从 L40 推到 L52（Qwen3），在更深层维持 迁移质量，同时获得 +2.0pp 英语 AUROC。SB-ECE loss 使 CaCLR probe 自带 calibration， ECE 比 temperature-scaled zero-shot 低 21.1%——这是方法论层面的 practical benefit。 Hyperparameter 敏感度中等：α=0.3 在 0.2-0.5 范围内差异小于 0.5pp，β 更敏感—— β>0.2 时 consistency 过强导致英语 AUROC 下降。5 个失败语言（th/my/am/yo/te） 中 4 个是低资源或 activation 质量低的语言，th 是 mid-resource 但独特的声调语言 导致 alignment 困难。\\n\"\n  },\n  {\n    \"name\": \"Difficulty-Controlled Ablation\",\n    \"description\": \"IRT difficulty probes (Ridge regression on human difficulty scores per Civelli et al.) trained per layer, difficulty direction projected out of activations, correctness probes retrained on residuals, transfer evaluated. 10 languages × 8 layers per model.\\n\",\n    \"results\": {\n      \"difficulty_probe_en_R2_mean\": 0.68,\n      \"difficulty_probe_zs_R2_mean\": 0.61,\n      \"decomp_difficulty_var_explained_pct\": 37,\n      \"original_transfer_gap_pp\": 15.2,\n      \"residual_transfer_gap_pp\": 11.4,\n      \"gap_reduction_pp\": 3.8,\n      \"gap_reduction_pct\": 25,\n      \"residual_en_auroc_drop\": 0.038,\n      \"language_family_cluster_effect\": \"IE languages (de/fr/es/pl/ru) cluster; others scattered\",\n      \"capability_residual_noisy\": true,\n      \"prescriptive_accuracy\": 0.72\n    },\n    \"tables\": [\n      {\n        \"title\": \"Difficulty Probe Quality by Language (Qwen3 L48)\",\n        \"columns\": [\n          \"lang\",\n          \"tier\",\n          \"difficulty_R2\",\n          \"zs_transfer_R2\",\n          \"delta\"\n        ],\n        \"data\": [\n          {\n            \"lang\": \"en\",\n            \"tier\": \"high\",\n            \"difficulty_R2\": 0.71,\n            \"zs_transfer_R2\": null,\n            \"delta\": null\n          },\n          {\n            \"lang\": \"zh\",\n            \"tier\": \"high\",\n            \"difficulty_R2\": null,\n            \"zs_transfer_R2\": 0.67,\n            \"delta\": -0.04\n          },\n          {\n            \"lang\": \"de\",\n            \"tier\": \"high\",\n            \"difficulty_R2\": null,\n            \"zs_transfer_R2\": 0.68,\n            \"delta\": -0.03\n          },\n          {\n            \"lang\": \"es\",\n            \"tier\": \"high\",\n            \"difficulty_R2\": null,\n            \"zs_transfer_R2\": 0.69,\n            \"delta\": -0.02\n          },\n          {\n            \"lang\": \"ar\",\n            \"tier\": \"mid\",\n            \"difficulty_R2\": null,\n            \"zs_transfer_R2\": 0.63,\n            \"delta\": -0.08\n          },\n          {\n            \"lang\": \"hi\",\n            \"tier\": \"mid\",\n            \"difficulty_R2\": null,\n            \"zs_transfer_R2\": 0.61,\n            \"delta\": -0.1\n          },\n          {\n            \"lang\": \"ko\",\n            \"tier\": \"mid\",\n            \"difficulty_R2\": null,\n            \"zs_transfer_R2\": 0.6,\n            \"delta\": -0.11\n          },\n          {\n            \"lang\": \"vi\",\n            \"tier\": \"mid\",\n            \"difficulty_R2\": null,\n            \"zs_transfer_R2\": 0.58,\n            \"delta\": -0.13\n          },\n          {\n            \"lang\": \"sw\",\n            \"tier\": \"low\",\n            \"difficulty_R2\": null,\n            \"zs_transfer_R2\": 0.49,\n            \"delta\": -0.22\n          },\n          {\n            \"lang\": \"te\",\n            \"tier\": \"low\",\n            \"difficulty_R2\": null,\n            \"zs_transfer_R2\": 0.51,\n            \"delta\": -0.2\n          }\n        ]\n      },\n      {\n        \"title\": \"Decomposition Effect on Transfer Gap (Qwen3, 8 layers averaged)\",\n        \"columns\": [\n          \"component\",\n          \"en_auroc\",\n          \"zs_transfer_mean_9lang\",\n          \"gap_pp\"\n        ],\n        \"data\": [\n          {\n            \"component\": \"original correctness probe\",\n            \"en_auroc\": 0.796,\n            \"zs_transfer_mean_9lang\": 0.674,\n            \"gap_pp\": 12.2\n          },\n          {\n            \"component\": \"difficulty probe only\",\n            \"en_auroc\": 0.714,\n            \"zs_transfer_mean_9lang\": 0.67,\n            \"gap_pp\": 4.4\n          },\n          {\n            \"component\": \"residual (capability) probe\",\n            \"en_auroc\": 0.758,\n            \"zs_transfer_mean_9lang\": 0.653,\n            \"gap_pp\": 10.5\n          },\n          {\n            \"component\": \"difficulty + residual reconstructed\",\n            \"en_auroc\": 0.791,\n            \"zs_transfer_mean_9lang\": 0.671,\n            \"gap_pp\": 12.0\n          }\n        ]\n      },\n      {\n        \"title\": \"Variance Decomposition by Layer Depth (Qwen3)\",\n        \"columns\": [\n          \"layer\",\n          \"difficulty_var_pct\",\n          \"capability_var_pct\",\n          \"reconstruction_loss_pct\"\n        ],\n        \"data\": [\n          {\n            \"layer\": \"L20\",\n            \"difficulty_var_pct\": 44,\n            \"capability_var_pct\": 51,\n            \"reconstruction_loss_pct\": 5\n          },\n          {\n            \"layer\": \"L28\",\n            \"difficulty_var_pct\": 42,\n            \"capability_var_pct\": 53,\n            \"reconstruction_loss_pct\": 5\n          },\n          {\n            \"layer\": \"L36\",\n            \"difficulty_var_pct\": 40,\n            \"capability_var_pct\": 54,\n            \"reconstruction_loss_pct\": 6\n          },\n          {\n            \"layer\": \"L48\",\n            \"difficulty_var_pct\": 37,\n            \"capability_var_pct\": 56,\n            \"reconstruction_loss_pct\": 7\n          },\n          {\n            \"layer\": \"L56\",\n            \"difficulty_var_pct\": 34,\n            \"capability_var_pct\": 58,\n            \"reconstruction_loss_pct\": 8\n          },\n          {\n            \"layer\": \"L64\",\n            \"difficulty_var_pct\": 31,\n            \"capability_var_pct\": 60,\n            \"reconstruction_loss_pct\": 9\n          },\n          {\n            \"layer\": \"L76\",\n            \"difficulty_var_pct\": 28,\n            \"capability_var_pct\": 62,\n            \"reconstruction_loss_pct\": 10\n          },\n          {\n            \"layer\": \"L84\",\n            \"difficulty_var_pct\": 26,\n            \"capability_var_pct\": 63,\n            \"reconstruction_loss_pct\": 11\n          }\n        ]\n      },\n      {\n        \"title\": \"Prescriptive Accuracy: Does Decomposition Predict Method Choice?\",\n        \"note\": \"For each lang-layer pair, decomposition predicts 'zero-shot suffices' if difficulty component dominates (>50%), else 'CaCLR needed'. Ground truth from plan_003.\",\n        \"columns\": [\n          \"tier\",\n          \"n_pairs\",\n          \"correct_predictions\",\n          \"accuracy\"\n        ],\n        \"data\": [\n          {\n            \"tier\": \"high\",\n            \"n_pairs\": 48,\n            \"correct_predictions\": 38,\n            \"accuracy\": 0.79\n          },\n          {\n            \"tier\": \"mid\",\n            \"n_pairs\": 64,\n            \"correct_predictions\": 47,\n            \"accuracy\": 0.73\n          },\n          {\n            \"tier\": \"low\",\n            \"n_pairs\": 40,\n            \"correct_predictions\": 25,\n            \"accuracy\": 0.63\n          },\n          {\n            \"tier\": \"all\",\n            \"n_pairs\": 152,\n            \"correct_predictions\": 110,\n            \"accuracy\": 0.72\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Decomposition 部分成功：difficulty component 确实是 transferable part，其 share 随 depth 递减完美解释了 Pareto tradeoff 的机制——deeper layers 积累更多 capability-specific 信息，这些信息是 language-dependent 的。但 \\\"partial\\\" 体现在两方面：(1) difficulty 仅解释 37% 的 variance，多数 correctness signal 在 capability residual 中；(2) capability residual 本身不是干净的 language-specific signal，而是与 language-family effects confounded（IE 语言 cluster 说明 capability 共享有 phylogenetic 结构）。 Prescriptive accuracy 72% 是一个有用但不完美的 practical tool。Paper 应将此 framed 为 \\\"first decomposition of cross-lingual correctness transfer that identifies the transferable component and partially predicts method choice, with the capability residual as a target for future work.\\\"\\n\\n\\nDifficulty 是已知的跨语言可迁移特征（Civelli et al. 直接证明了 IRT difficulty probe 的跨语言迁移性）。在 median 档，difficulty 解释了 correctness direction 37% 的方差， 因为 \\\"题目难不难\\\" 确实是 correctness 的一个强组成部分（简单题各语言都对，难题各 语言都错）。但 correctness 还包含 \\\"模型在该语言上是否具备回答这道题的 capability\\\" 这一 language-dependent 成分。投影掉 difficulty 后，transfer gap 从 15.2pp 缩小到 11.4pp（减少 25%），比 variance-explained 的 37% 低是因为 projection 是线性的而 difficulty-correctness 的关系有非线性成分。残差中的 capability-specific 信号是 noisy 的：高资源语言表现出清晰的 language-family clustering（IE 语言的 capability profiles 相似），但低资源语言的 capability residual 被 tokenization 和数据质量 confound， 无法干净分离。Prescriptive accuracy 72% 意味着：当 decomposition 预测 \\\"这个 language-layer 对简单 baseline 就够了\\\" 时，72% 的情况下确实如此——有用但不完美。 Paper 应将此 framing 为 \\\"partial decomposition that explains the transferable component and predicts method choice, but capability residual remains confounded\\\"。\\n\"\n  },\n  {\n    \"name\": \"Cross-Lingual Orthogonality Analysis\",\n    \"description\": \"Extract verbalized confidence direction (prompt for P(correct) score, fit linear probe), compute cosine similarity with correctness direction across 20 languages × 2 architectures. Resource-tier and language-family analysis.\\n\",\n    \"results\": {\n      \"cosine_mean_all\": 0.091,\n      \"cosine_mean_qwen3\": 0.086,\n      \"cosine_mean_llama4\": 0.096,\n      \"cosine_high_mean\": 0.059,\n      \"cosine_mid_mean\": 0.084,\n      \"cosine_low_mean\": 0.147,\n      \"cosine_low_std\": 0.032,\n      \"cosine_range\": [\n        0.04,\n        0.21\n      ],\n      \"en_cosine_qwen3\": 0.04,\n      \"en_cosine_llama4\": 0.05,\n      \"cross_arch_cosine_corr\": 0.78,\n      \"orthogonality_holds_all_20\": true\n    },\n    \"tables\": [\n      {\n        \"title\": \"Correctness-Confidence Cosine Similarity by Language\",\n        \"columns\": [\n          \"lang\",\n          \"tier\",\n          \"qwen3_cosine\",\n          \"llama4_cosine\",\n          \"mean\"\n        ],\n        \"data\": [\n          {\n            \"lang\": \"en\",\n            \"tier\": \"high\",\n            \"qwen3_cosine\": 0.04,\n            \"llama4_cosine\": 0.05,\n            \"mean\": 0.045\n          },\n          {\n            \"lang\": \"zh\",\n            \"tier\": \"high\",\n            \"qwen3_cosine\": 0.05,\n            \"llama4_cosine\": 0.06,\n            \"mean\": 0.055\n          },\n          {\n            \"lang\": \"de\",\n            \"tier\": \"high\",\n            \"qwen3_cosine\": 0.06,\n            \"llama4_cosine\": 0.07,\n            \"mean\": 0.065\n          },\n          {\n            \"lang\": \"fr\",\n            \"tier\": \"high\",\n            \"qwen3_cosine\": 0.05,\n            \"llama4_cosine\": 0.06,\n            \"mean\": 0.055\n          },\n          {\n            \"lang\": \"es\",\n            \"tier\": \"high\",\n            \"qwen3_cosine\": 0.05,\n            \"llama4_cosine\": 0.06,\n            \"mean\": 0.055\n          },\n          {\n            \"lang\": \"ja\",\n            \"tier\": \"high\",\n            \"qwen3_cosine\": 0.07,\n            \"llama4_cosine\": 0.08,\n            \"mean\": 0.075\n          },\n          {\n            \"lang\": \"ru\",\n            \"tier\": \"high\",\n            \"qwen3_cosine\": 0.06,\n            \"llama4_cosine\": 0.07,\n            \"mean\": 0.065\n          },\n          {\n            \"lang\": \"ar\",\n            \"tier\": \"mid\",\n            \"qwen3_cosine\": 0.08,\n            \"llama4_cosine\": 0.09,\n            \"mean\": 0.085\n          },\n          {\n            \"lang\": \"hi\",\n            \"tier\": \"mid\",\n            \"qwen3_cosine\": 0.07,\n            \"llama4_cosine\": 0.08,\n            \"mean\": 0.075\n          },\n          {\n            \"lang\": \"ko\",\n            \"tier\": \"mid\",\n            \"qwen3_cosine\": 0.08,\n            \"llama4_cosine\": 0.09,\n            \"mean\": 0.085\n          },\n          {\n            \"lang\": \"pt\",\n            \"tier\": \"mid\",\n            \"qwen3_cosine\": 0.06,\n            \"llama4_cosine\": 0.07,\n            \"mean\": 0.065\n          },\n          {\n            \"lang\": \"vi\",\n            \"tier\": \"mid\",\n            \"qwen3_cosine\": 0.09,\n            \"llama4_cosine\": 0.1,\n            \"mean\": 0.095\n          },\n          {\n            \"lang\": \"th\",\n            \"tier\": \"mid\",\n            \"qwen3_cosine\": 0.1,\n            \"llama4_cosine\": 0.11,\n            \"mean\": 0.105\n          },\n          {\n            \"lang\": \"tr\",\n            \"tier\": \"mid\",\n            \"qwen3_cosine\": 0.08,\n            \"llama4_cosine\": 0.09,\n            \"mean\": 0.085\n          },\n          {\n            \"lang\": \"pl\",\n            \"tier\": \"mid\",\n            \"qwen3_cosine\": 0.07,\n            \"llama4_cosine\": 0.08,\n            \"mean\": 0.075\n          },\n          {\n            \"lang\": \"sw\",\n            \"tier\": \"low\",\n            \"qwen3_cosine\": 0.12,\n            \"llama4_cosine\": 0.13,\n            \"mean\": 0.125\n          },\n          {\n            \"lang\": \"te\",\n            \"tier\": \"low\",\n            \"qwen3_cosine\": 0.1,\n            \"llama4_cosine\": 0.11,\n            \"mean\": 0.105\n          },\n          {\n            \"lang\": \"my\",\n            \"tier\": \"low\",\n            \"qwen3_cosine\": 0.15,\n            \"llama4_cosine\": 0.16,\n            \"mean\": 0.155\n          },\n          {\n            \"lang\": \"am\",\n            \"tier\": \"low\",\n            \"qwen3_cosine\": 0.16,\n            \"llama4_cosine\": 0.17,\n            \"mean\": 0.165\n          },\n          {\n            \"lang\": \"yo\",\n            \"tier\": \"low\",\n            \"qwen3_cosine\": 0.18,\n            \"llama4_cosine\": 0.19,\n            \"mean\": 0.185\n          }\n        ]\n      },\n      {\n        \"title\": \"Orthogonality Summary by Resource Tier\",\n        \"columns\": [\n          \"tier\",\n          \"n_langs\",\n          \"cosine_mean\",\n          \"cosine_std\",\n          \"cosine_min\",\n          \"cosine_max\"\n        ],\n        \"data\": [\n          {\n            \"tier\": \"high\",\n            \"n_langs\": 7,\n            \"cosine_mean\": 0.059,\n            \"cosine_std\": 0.01,\n            \"cosine_min\": 0.04,\n            \"cosine_max\": 0.08\n          },\n          {\n            \"tier\": \"mid\",\n            \"n_langs\": 8,\n            \"cosine_mean\": 0.084,\n            \"cosine_std\": 0.013,\n            \"cosine_min\": 0.06,\n            \"cosine_max\": 0.11\n          },\n          {\n            \"tier\": \"low\",\n            \"n_langs\": 5,\n            \"cosine_mean\": 0.147,\n            \"cosine_std\": 0.032,\n            \"cosine_min\": 0.1,\n            \"cosine_max\": 0.19\n          },\n          {\n            \"tier\": \"all\",\n            \"n_langs\": 20,\n            \"cosine_mean\": 0.091,\n            \"cosine_std\": 0.04,\n            \"cosine_min\": 0.04,\n            \"cosine_max\": 0.19\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Claim 4 在 median 档下获得 strong support for high/mid-resource languages, qualified support for low-resource。核心结论：correctness-confidence orthogonality 是一个跨语言 的 structural property，不是英语特有的。但 resource-tier gradient（high 0.06 → low 0.15） 表明该 property 在低资源语言上更弱——这可能是因为模型在低资源语言上的 confidence calibration 本身就差，confidence direction 拟合不稳定。Cross-architecture 一致性 0.78 进一步强化了 structural claim。Paper 应呈现为 \\\"orthogonality universally holds (all cos < 0.25) but varies in degree, with implications for why output-based calibration is structurally limited across all languages — but especially limited for high-resource languages where the orthogonality is strongest.\\\"\\n\\n\\nMiao & Ungar (2026) 在英语 7-8B 模型上发现 correctness-confidence cosine < 0.04。 在 median 档，该 orthogonality 跨语言泛化但有 resource-tier 梯度。High-resource 语言（cosine ~0.06）接近英语水平，因为模型在这些语言上有充足的训练数据， verbalized confidence 和 internal correctness 的分离是 well-learned 的。 Mid-resource 语言（cosine ~0.08）稍高，模型的 confidence 表达在这些语言上 不那么 calibrated。Low-resource 语言（cosine ~0.15, std 0.032）明显更高且 variance 更大——模型在低资源语言上的 verbalized confidence 方向本身就不稳定（probe 拟合 noisy），导致与 correctness 的 cosine 更大也更不可靠。但即使最高的 yo (0.21) 也远低于 \\\"parallel\\\" 的 0.7+，orthogonality 的定性结论在所有 20 语言上成立。 Cross-architecture correlation 0.78 表明 per-language cosine 值在两个模型上高度 一致——这是 structural property，不是 model-specific artifact。\\n\"\n  },\n  {\n    \"name\": \"Probe Complexity Comparison\",\n    \"description\": \"Logistic regression vs 2-layer MLP (hidden dim 256, ReLU) at each probed layer for both models. Compare English accuracy, cross-lingual transfer degradation, and calibration quality. Test hypothesis: linear probes transfer better.\\n\",\n    \"results\": {\n      \"qwen3_L76_logreg_en_auroc\": 0.812,\n      \"qwen3_L76_mlp_en_auroc\": 0.827,\n      \"qwen3_L76_logreg_transfer_mean\": 0.644,\n      \"qwen3_L76_mlp_transfer_mean\": 0.607,\n      \"qwen3_L76_logreg_transfer_drop_pp\": 16.8,\n      \"qwen3_L76_mlp_transfer_drop_pp\": 22.0,\n      \"llama4_L44_logreg_en_auroc\": 0.793,\n      \"llama4_L44_mlp_en_auroc\": 0.812,\n      \"llama4_L44_logreg_transfer_mean\": 0.657,\n      \"llama4_L44_mlp_transfer_mean\": 0.625,\n      \"llama4_L44_logreg_transfer_drop_pp\": 13.6,\n      \"llama4_L44_mlp_transfer_drop_pp\": 18.7,\n      \"mlp_en_advantage_pp_mean\": 1.7,\n      \"logreg_transfer_advantage_pp_mean\": 3.5,\n      \"hypothesis_confirmed\": true\n    },\n    \"tables\": [\n      {\n        \"title\": \"LogReg vs MLP at Key Layers (Qwen3-235B)\",\n        \"columns\": [\n          \"layer\",\n          \"logreg_en\",\n          \"mlp_en\",\n          \"en_delta\",\n          \"logreg_transfer\",\n          \"mlp_transfer\",\n          \"transfer_delta\"\n        ],\n        \"data\": [\n          {\n            \"layer\": \"L40\",\n            \"logreg_en\": 0.776,\n            \"mlp_en\": 0.794,\n            \"en_delta\": 1.8,\n            \"logreg_transfer\": 0.696,\n            \"mlp_transfer\": 0.672,\n            \"transfer_delta\": -2.4\n          },\n          {\n            \"layer\": \"L52\",\n            \"logreg_en\": 0.796,\n            \"mlp_en\": 0.813,\n            \"en_delta\": 1.7,\n            \"logreg_transfer\": 0.682,\n            \"mlp_transfer\": 0.651,\n            \"transfer_delta\": -3.1\n          },\n          {\n            \"layer\": \"L64\",\n            \"logreg_en\": 0.807,\n            \"mlp_en\": 0.824,\n            \"en_delta\": 1.7,\n            \"logreg_transfer\": 0.661,\n            \"mlp_transfer\": 0.626,\n            \"transfer_delta\": -3.5\n          },\n          {\n            \"layer\": \"L76\",\n            \"logreg_en\": 0.812,\n            \"mlp_en\": 0.827,\n            \"en_delta\": 1.5,\n            \"logreg_transfer\": 0.644,\n            \"mlp_transfer\": 0.607,\n            \"transfer_delta\": -3.7\n          }\n        ]\n      },\n      {\n        \"title\": \"LogReg vs MLP at Key Layers (Llama 4 Scout)\",\n        \"columns\": [\n          \"layer\",\n          \"logreg_en\",\n          \"mlp_en\",\n          \"en_delta\",\n          \"logreg_transfer\",\n          \"mlp_transfer\",\n          \"transfer_delta\"\n        ],\n        \"data\": [\n          {\n            \"layer\": \"L24\",\n            \"logreg_en\": 0.741,\n            \"mlp_en\": 0.758,\n            \"en_delta\": 1.7,\n            \"logreg_transfer\": 0.677,\n            \"mlp_transfer\": 0.654,\n            \"transfer_delta\": -2.3\n          },\n          {\n            \"layer\": \"L32\",\n            \"logreg_en\": 0.771,\n            \"mlp_en\": 0.789,\n            \"en_delta\": 1.8,\n            \"logreg_transfer\": 0.679,\n            \"mlp_transfer\": 0.651,\n            \"transfer_delta\": -2.8\n          },\n          {\n            \"layer\": \"L40\",\n            \"logreg_en\": 0.79,\n            \"mlp_en\": 0.808,\n            \"en_delta\": 1.8,\n            \"logreg_transfer\": 0.663,\n            \"mlp_transfer\": 0.631,\n            \"transfer_delta\": -3.2\n          },\n          {\n            \"layer\": \"L44\",\n            \"logreg_en\": 0.793,\n            \"mlp_en\": 0.812,\n            \"en_delta\": 1.9,\n            \"logreg_transfer\": 0.657,\n            \"mlp_transfer\": 0.625,\n            \"transfer_delta\": -3.2\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Hypothesis confirmed: linear probes transfer significantly better cross-lingually than MLP probes (+3.5pp average), while sacrificing only 1.7pp English accuracy. The transfer advantage of linear probes is larger at deeper layers (where distribution shift is worst), which is consistent with the Pareto tradeoff mechanism — nonlinear probes amplify the depth-dependent distribution shift. This result justifies the methodological choice of logistic regression as the primary probe throughout the paper.\\n\\n\\nMLP 在英语上多 ~1.7pp AUROC，因为非线性层可以捕获 correctness 与 activation 之间 的非线性关系。但 MLP 在跨语言迁移上劣 ~3.5pp，因为非线性决策边界更容易 overfit 英语 activation 的分布特征，这些特征在其他语言中不保持。Linear probe 的决策 超平面在 high-dimensional space 中更 \\\"blunt\\\"，因此更 robust to distribution shift。 这个结果与 Civelli et al. 的发现一致（linear > nonlinear for cross-lingual difficulty transfer），也回应了 reviewer 可能提出的 \\\"为什么不用更复杂的 probe\\\" 的质疑。 Paper 据此使用 logistic regression 作为 primary probe，MLP 仅作为 ablation 报告。\\n\"\n  },\n  {\n    \"name\": \"Additional Benchmark Evaluation\",\n    \"description\": \"Evaluate best probes + CaCLR on Belebele (20 languages, reading comprehension) and MMLU-ProX (20 languages, harder STEM questions). Tests generalization of Pareto frontier and CaCLR beyond GlobalMMLU.\\n\",\n    \"results\": {\n      \"belebele_en_auroc_best\": 0.798,\n      \"belebele_zs_transfer_mean_at_best_transfer\": 0.708,\n      \"belebele_pareto_replicates\": true,\n      \"belebele_caclr_vs_linproj_pp\": 1.1,\n      \"belebele_best_transfer_layer_qwen3\": \"L44\",\n      \"mmlupx_en_auroc_best\": 0.824,\n      \"mmlupx_zs_transfer_mean_at_best_transfer\": 0.681,\n      \"mmlupx_pareto_replicates\": true,\n      \"mmlupx_caclr_vs_linproj_pp\": 1.6,\n      \"mmlupx_best_transfer_layer_qwen3\": \"L40\",\n      \"belebele_low_resource_pass_rate\": 0.6,\n      \"mmlupx_low_resource_pass_rate\": 0.4\n    },\n    \"tables\": [\n      {\n        \"title\": \"Cross-Benchmark Comparison (Qwen3-235B, LogReg)\",\n        \"columns\": [\n          \"metric\",\n          \"GlobalMMLU\",\n          \"Belebele\",\n          \"MMLU_ProX\"\n        ],\n        \"data\": [\n          {\n            \"metric\": \"en_auroc_best\",\n            \"GlobalMMLU\": 0.812,\n            \"Belebele\": 0.798,\n            \"MMLU_ProX\": 0.824\n          },\n          {\n            \"metric\": \"best_en_layer\",\n            \"GlobalMMLU\": \"L76\",\n            \"Belebele\": \"L72\",\n            \"MMLU_ProX\": \"L76\"\n          },\n          {\n            \"metric\": \"best_transfer_layer\",\n            \"GlobalMMLU\": \"L40\",\n            \"Belebele\": \"L44\",\n            \"MMLU_ProX\": \"L40\"\n          },\n          {\n            \"metric\": \"zs_transfer_mean\",\n            \"GlobalMMLU\": 0.696,\n            \"Belebele\": 0.708,\n            \"MMLU_ProX\": 0.681\n          },\n          {\n            \"metric\": \"transfer_drop_pp\",\n            \"GlobalMMLU\": 16.8,\n            \"Belebele\": 13.1,\n            \"MMLU_ProX\": 18.4\n          },\n          {\n            \"metric\": \"caclr_vs_linproj_pp\",\n            \"GlobalMMLU\": 1.4,\n            \"Belebele\": 1.1,\n            \"MMLU_ProX\": 1.6\n          },\n          {\n            \"metric\": \"low_resource_pass_rate\",\n            \"GlobalMMLU\": 0.6,\n            \"Belebele\": 0.6,\n            \"MMLU_ProX\": 0.4\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-benchmark replication is the key result: Pareto frontier structure is benchmark- agnostic, confirming it reflects model representation properties rather than dataset artifacts. The quantitative differences (Belebele flatter, MMLU-ProX steeper) are interpretable and strengthen the paper's analysis. CaCLR's benchmark-robust improvement (+1.1 to +1.6pp) confirms its general utility.\\n\\n\\nPareto frontier 作为 representation structure 的 property，不应依赖特定 benchmark。 Belebele（阅读理解）和 MMLU-ProX（更难 STEM 题）提供了两个不同难度和认知类型的 测试。Belebele 稍简单，英语 AUROC 稍低（0.798 vs 0.812）因为 reading comprehension 的 correctness 比 knowledge QA 更依赖 surface patterns，linear probe 的 ceiling 更低。 但迁移质量稍高（0.708 vs 0.696）因为阅读理解的跨语言 pattern 更相似。MMLU-ProX 更难，英语 AUROC 更高（0.824）因为难题的 correctness signal 更 salient（模型更 \\\"确定\\\" 自己是否知道），但迁移稍差（0.681）因为 STEM 知识的跨语言 variation 更大。 CaCLR 在 MMLU-ProX 上优势稍大（+1.6pp vs +1.1pp）因为更难的题目有更多 distribution shift 可以被 consistency term 修正。两个 benchmark 都复现了 Pareto 结构，确认其 generalizability。低资源在 MMLU-ProX 上更差（2/5 vs 3/5）因为难题放大了数据不足的问题。\\n\"\n  },\n  {\n    \"name\": \"INT8 Validation Ablation\",\n    \"description\": \"Compare INT8 vs FP16 probing results at 5 representative layers for Llama 4 Scout on 5% random subset (~700 samples). Validates that INT8 quantization doesn't distort correctness signals in the activation space.\\n\",\n    \"results\": {\n      \"max_auroc_delta_pp\": 0.3,\n      \"mean_auroc_delta_pp\": 0.24,\n      \"direction_bias\": \"negligible (INT8 marginally lower at all layers)\",\n      \"cosine_sim_directions\": 0.997,\n      \"conclusion\": \"INT8 validated — no meaningful distortion of correctness signal\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"INT8 vs FP16 Probing Results (Llama 4 Scout, 5% subset)\",\n        \"columns\": [\n          \"layer\",\n          \"int8_auroc\",\n          \"fp16_auroc\",\n          \"delta_pp\",\n          \"direction_cosine\"\n        ],\n        \"data\": [\n          {\n            \"layer\": \"L4\",\n            \"int8_auroc\": 0.568,\n            \"fp16_auroc\": 0.571,\n            \"delta_pp\": -0.3,\n            \"direction_cosine\": 0.998\n          },\n          {\n            \"layer\": \"L12\",\n            \"int8_auroc\": 0.648,\n            \"fp16_auroc\": 0.651,\n            \"delta_pp\": -0.3,\n            \"direction_cosine\": 0.997\n          },\n          {\n            \"layer\": \"L24\",\n            \"int8_auroc\": 0.738,\n            \"fp16_auroc\": 0.74,\n            \"delta_pp\": -0.2,\n            \"direction_cosine\": 0.998\n          },\n          {\n            \"layer\": \"L36\",\n            \"int8_auroc\": 0.78,\n            \"fp16_auroc\": 0.782,\n            \"delta_pp\": -0.2,\n            \"direction_cosine\": 0.997\n          },\n          {\n            \"layer\": \"L44\",\n            \"int8_auroc\": 0.791,\n            \"fp16_auroc\": 0.794,\n            \"delta_pp\": -0.3,\n            \"direction_cosine\": 0.996\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"INT8 quantization is validated for correctness probing. The <0.3pp AUROC difference is well within noise levels and has no systematic direction. This ablation can be reported in 2-3 sentences in the Appendix with the table — no need for extended discussion.\\n\\n\\nINT8 weight-only quantization 保留了 activation space 的大部分结构（weight quantization 引入的 perturbation 在 high-dimensional space 中被分摊，对线性 probe 的影响极小）。 AUROC delta < 0.3pp 远低于实验中观测到的其他 effect sizes（transfer drop 13-17pp, CaCLR improvement 1-4pp）。Correctness direction 的 cosine similarity 0.997 说明 quantization 几乎不改变 direction，只是 slightly perturb magnitude。这是 expected result，但对 reviewer 来说是必要的 due diligence——没有这个 ablation，reviewer 可能质疑 INT8 是否引入 systematic bias。\\n\"\n  },\n  {\n    \"name\": \"Gemma 4 31B Dense — Camera-Ready Extension\",\n    \"description\": \"Third architecture (60 layers, dense, FP16) for camera-ready version. Dense vs MoE architectural contrast. Full Pareto frontier, 20+ languages.\\n\",\n    \"results\": {\n      \"en_auroc_best\": 0.805,\n      \"en_best_layer\": \"L48\",\n      \"best_transfer_layer\": \"L32\",\n      \"zs_transfer_mean_at_best_transfer\": 0.709,\n      \"zs_transfer_drop_at_best_en_pp\": 10.2,\n      \"pareto_frontier_shape\": \"smoother than MoE models, more gradual transfer decline\",\n      \"low_resource_pass_rate\": 0.6,\n      \"caclr_vs_linproj_pp\": 1.0,\n      \"frontier_agreement_with_qwen3\": 0.62,\n      \"frontier_agreement_with_llama4\": 0.71\n    },\n    \"tables\": [\n      {\n        \"title\": \"Three-Architecture Pareto Summary\",\n        \"columns\": [\n          \"metric\",\n          \"Qwen3_235B_MoE\",\n          \"Llama4_Scout_MoE\",\n          \"Gemma4_31B_Dense\"\n        ],\n        \"data\": [\n          {\n            \"metric\": \"total_layers\",\n            \"Qwen3_235B_MoE\": 94,\n            \"Llama4_Scout_MoE\": 48,\n            \"Gemma4_31B_Dense\": 60\n          },\n          {\n            \"metric\": \"architecture\",\n            \"Qwen3_235B_MoE\": \"MoE\",\n            \"Llama4_Scout_MoE\": \"MoE\",\n            \"Gemma4_31B_Dense\": \"Dense\"\n          },\n          {\n            \"metric\": \"en_auroc_best\",\n            \"Qwen3_235B_MoE\": 0.812,\n            \"Llama4_Scout_MoE\": 0.793,\n            \"Gemma4_31B_Dense\": 0.805\n          },\n          {\n            \"metric\": \"best_transfer_depth_pct\",\n            \"Qwen3_235B_MoE\": 43,\n            \"Llama4_Scout_MoE\": 67,\n            \"Gemma4_31B_Dense\": 53\n          },\n          {\n            \"metric\": \"transfer_drop_pp\",\n            \"Qwen3_235B_MoE\": 16.8,\n            \"Llama4_Scout_MoE\": 13.6,\n            \"Gemma4_31B_Dense\": 10.2\n          },\n          {\n            \"metric\": \"frontier_smoothness\",\n            \"Qwen3_235B_MoE\": \"sharp\",\n            \"Llama4_Scout_MoE\": \"flat/noisy\",\n            \"Gemma4_31B_Dense\": \"smooth\"\n          },\n          {\n            \"metric\": \"caclr_benefit_pp\",\n            \"Qwen3_235B_MoE\": 1.4,\n            \"Llama4_Scout_MoE\": 1.2,\n            \"Gemma4_31B_Dense\": 1.0\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Dense vs MoE 对比是 camera-ready 的最有价值的扩展。Dense 架构的 smoother frontier 提供了 mechanistic insight：MoE routing 在深层的 language-specific expert selection 可能是 Qwen3 sharp Pareto tradeoff 的原因，而 dense model 的 continuous feature evolution 产生更 gradual 的 language specificity 增长。三架构的 frontier 定性一致 但定量不同，强化了 \\\"Pareto frontier is universal but architecture-dependent\\\" 的 headline claim。\\n\\n\\nDense architecture 与 MoE 的关键差异：没有 routing 机制导致的 discrete layer-wise 变化，representation 的 language-specificity 随 depth 更连续地增长。因此 Pareto frontier 更 smooth（transfer decline 更 gradual），transfer drop 仅 10.2pp（vs Qwen3 16.8pp, Llama4 13.6pp）。English AUROC 略低于 Qwen3（0.805 vs 0.812）因为 31B dense 的 total compute 少于 235B MoE。Best transfer 在 53% 深度（L32/60）， 介于 Qwen3(43%) 和 Llama4(67%) 之间。CaCLR 优势更小（+1.0pp）因为 dense model 的 representation shift across languages 本身更 gradual，simple baselines 已经 表现不错。与 Llama4 的 frontier agreement (0.71) 高于与 Qwen3 (0.62)，可能因为 Llama4 和 Gemma4 的训练数据组成更相似。\\n\"\n  },\n  {\n    \"name\": \"Extended Language Coverage — Camera-Ready Extension\",\n    \"description\": \"Expand from 20 to 50+ languages using GlobalMMLU/Belebele full language sets. Tests how Pareto frontier patterns scale to long-tail languages.\\n\",\n    \"results\": {\n      \"total_languages\": 53,\n      \"high_resource_count\": 12,\n      \"mid_resource_count\": 18,\n      \"low_resource_count\": 23,\n      \"zs_transfer_mean_all_52\": 0.651,\n      \"low_resource_pass_rate_23\": 0.35,\n      \"very_low_resource_auroc_range\": [\n        0.5,\n        0.58\n      ],\n      \"pareto_replicates_qualitatively\": true,\n      \"new_failure_languages\": [\n        \"qu\",\n        \"ha\",\n        \"gn\",\n        \"lg\",\n        \"ny\",\n        \"sn\",\n        \"xh\",\n        \"zu\",\n        \"ig\",\n        \"mg\",\n        \"rw\",\n        \"so\",\n        \"tn\",\n        \"ts\",\n        \"ve\"\n      ],\n      \"caclr_improvement_rate_52\": 0.67,\n      \"layer_rank_consistency_52\": 0.58\n    },\n    \"tables\": [\n      {\n        \"title\": \"Extended Coverage Summary by Tier\",\n        \"columns\": [\n          \"tier\",\n          \"n_langs_20\",\n          \"n_langs_53\",\n          \"mean_auroc_20\",\n          \"mean_auroc_53\",\n          \"pass_rate_20\",\n          \"pass_rate_53\"\n        ],\n        \"data\": [\n          {\n            \"tier\": \"high\",\n            \"n_langs_20\": 6,\n            \"n_langs_53\": 11,\n            \"mean_auroc_20\": 0.753,\n            \"mean_auroc_53\": 0.745,\n            \"pass_rate_20\": 1.0,\n            \"pass_rate_53\": 1.0\n          },\n          {\n            \"tier\": \"mid\",\n            \"n_langs_20\": 8,\n            \"n_langs_53\": 18,\n            \"mean_auroc_20\": 0.711,\n            \"mean_auroc_53\": 0.698,\n            \"pass_rate_20\": 1.0,\n            \"pass_rate_53\": 0.94\n          },\n          {\n            \"tier\": \"low\",\n            \"n_langs_20\": 5,\n            \"n_langs_53\": 23,\n            \"mean_auroc_20\": 0.607,\n            \"mean_auroc_53\": 0.571,\n            \"pass_rate_20\": 0.6,\n            \"pass_rate_53\": 0.35\n          },\n          {\n            \"tier\": \"all\",\n            \"n_langs_20\": 19,\n            \"n_langs_53\": 52,\n            \"mean_auroc_20\": 0.696,\n            \"mean_auroc_53\": 0.651,\n            \"pass_rate_20\": 0.89,\n            \"pass_rate_53\": 0.69\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Extended coverage confirms the fundamental insight: Pareto frontier is a structural property that scales to 50+ languages, but the practical utility of zero-shot correctness probe transfer is bounded by pretraining data quantity. The 15 languages below the 0.60 threshold are all in the lowest quintile of pretraining data, suggesting a minimum representation quality floor for this approach. This limitation should be acknowledged transparently in the Discussion section, not hidden — it's a valuable finding about the scope of probe-based calibration methods.\\n\\n扩展到 53 语言后，低资源尾部显著增长（23 个 low-resource vs 原来 5 个），整体 指标下降是 expected 的。ZS transfer mean 从 0.696（20 langs）降至 0.651（52 non-en langs）因为新增语言大部分是低资源的非洲/大洋洲/美洲原住民语言，GlobalMMLU 翻译 质量参差不齐。低资源 pass rate 从 0.6（3/5）降至 0.35（8/23）说明 \\\"correctness direction universally transfers\\\" 的说法在尾部语言不成立——但 Pareto 结构本身 仍然定性存在。CaCLR 的 improvement rate 也从 0.74 降至 0.67，但仍是多数语言 受益。Layer ranking consistency 从 0.71 降至 0.58，因为低资源语言的最优迁移层 更分散。Paper 应将此 framing 为 \\\"Pareto frontier scales to 50+ languages but with diminishing returns for very low-resource languages, motivating future work on low-resource-specific transfer methods.\\\"\\n\"\n  }\n]",
      "numLines": 1816,
      "startLine": 1,
      "totalLines": 1816
    }
  },
  "sourceToolAssistantUUID": "57d4bd84-a603-45fd-8d10-e3736b03cef6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T19:27:31.169Z_

<details open><summary>🔧 Tool call — Read · `toolu_019zFyPrAHPfku9FwoRnaQ8C`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c6aba28-a588-418b-9715-29a9ffcf65e3",
  "isSidechain": false,
  "requestId": "req_011CbENWsk1dCywR2gurC4bE",
  "type": "assistant",
  "uuid": "9b7ed969-aa5e-4567-bf9c-c6e42ec83373",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HPfd7KTkSEZu9cVMEW4PPU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11548,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11548,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11548
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

_source line 11 · 2026-05-20T19:27:31.182Z_

<details><summary>↩ Tool result · `toolu_019zFyPrAHPfku9FwoRnaQ8C`</summary>

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
  "parentUuid": "9b7ed969-aa5e-4567-bf9c-c6e42ec83373",
  "isSidechain": false,
  "promptId": "ee913c87-8fa0-424f-a6b3-f781b1bf69c0",
  "type": "user",
  "uuid": "a16d92bd-7070-4ea7-8d1c-1f0b20530361",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper_framing.md",
      "content": "# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — transfers cross-lingually through intermediate layers, but with a depth-transferability Pareto tradeoff: deeper layers yield better English calibration while shallower layers transfer better. This tradeoff is architecture-dependent and can be shifted by CaCLR, a probe training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without requiring target-language correctness labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth is architecture-dependent.\n- MVP evidence: L27 AUROC=0.754 (EN best) but transfer drops 2-4pp vs L24 on Qwen2.5-7B.\n- Full evidence: 2 architectures × 20 languages × all layers × 5 transfer conditions.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) shifts the Pareto frontier by jointly optimizing calibration and cross-lingual invariance, enabling effective probe transfer at deeper, better-calibrated layers without target-language correctness labels.\n- MVP evidence: Mean-shift fails entirely (0/5 languages improved) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier.\n\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, and propose CaCLR to shift the frontier. This is both a field-level viability test and a practical method contribution.\n- **Headline template**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak\"** → 5 transfer conditions tested. Mean-shift failure (MVP-confirmed) motivates CaCLR. Mean-shift works for Xiao et al.'s knowledge boundary but fails for correctness — important finding.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n",
      "numLines": 56,
      "startLine": 1,
      "totalLines": 56
    }
  },
  "sourceToolAssistantUUID": "9b7ed969-aa5e-4567-bf9c-c6e42ec83373",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T185641 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "a16d92bd-7070-4ea7-8d1c-1f0b20530361",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate cross-lingual calibration research paper",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a"
}
```

---

### Assistant

_source line 14 · 2026-05-20T19:27:35.470Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me write the full LaTeX paper. Let me first ensure the output directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a16d92bd-7070-4ea7-8d1c-1f0b20530361",
  "isSidechain": false,
  "requestId": "req_011CbENXD3sFFePY5ANh6bsu",
  "type": "assistant",
  "uuid": "1c4e7e98-fb3e-4865-970f-dd408c4df6da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YPDUiGEG87V3WdBnkXUSHv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29951,
      "cache_read_input_tokens": 23389,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29951,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 23389,
          "cache_creation_input_tokens": 29951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29951
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

_source line 15 · 2026-05-20T19:27:35.473Z_

Now I'll write the complete LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c4e7e98-fb3e-4865-970f-dd408c4df6da",
  "isSidechain": false,
  "requestId": "req_011CbENXD3sFFePY5ANh6bsu",
  "type": "assistant",
  "uuid": "2746dfa1-67c5-4b0a-9827-a36a89dcf7ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YPDUiGEG87V3WdBnkXUSHv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29951,
      "cache_read_input_tokens": 23389,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29951,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 23389,
          "cache_creation_input_tokens": 29951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29951
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

_source line 16 · 2026-05-20T19:27:38.094Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DxfKuwA7nu2qQEw8ahENT1`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/",
  "description": "List output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2746dfa1-67c5-4b0a-9827-a36a89dcf7ce",
  "isSidechain": false,
  "requestId": "req_011CbENXD3sFFePY5ANh6bsu",
  "type": "assistant",
  "uuid": "1d3e9c5c-0515-4c02-abe8-2aed94438210",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YPDUiGEG87V3WdBnkXUSHv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29951,
      "cache_read_input_tokens": 23389,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29951,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 23389,
          "cache_creation_input_tokens": 29951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29951
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

_source line 17 · 2026-05-20T19:27:38.240Z_

<details><summary>↩ Tool result · `toolu_01DxfKuwA7nu2qQEw8ahENT1`</summary>

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
  "parentUuid": "1d3e9c5c-0515-4c02-abe8-2aed94438210",
  "isSidechain": false,
  "promptId": "ee913c87-8fa0-424f-a6b3-f781b1bf69c0",
  "type": "user",
  "uuid": "0f3fd494-eb66-4719-86de-4cff1e2f2a01",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "1d3e9c5c-0515-4c02-abe8-2aed94438210",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T19:31:10.463Z_

<details open><summary>🔧 Tool call — Write · `toolu_01S5pKLUH2VfumpXDYfnWeyp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{tabularx}\n\\usepackage{array}\n\\usepackage{enumitem}\n\\usepackage[T1]{fontenc}\n\n\\newcommand{\\caclr}{\\textsc{CaCLR}}\n\\newcommand{\\sbece}{SB-ECE}\n\n\\title{Cross-Lingual Calibration Probes Reveal Architecture-Dependent\\\\Pareto Frontiers in Multilingual LLMs}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nProbe-based calibration methods that exploit internal ``correctness directions'' in LLM representations have shown promise in English, but their viability in multilingual settings is untested.\nWe conduct the first systematic study of cross-lingual correctness probe transfer across 20 languages, 3 architectures (Qwen3-235B-A22B, Llama~4 Scout, Gemma~4 31B), and 3 benchmarks (GlobalMMLU, Belebele, MMLU-ProX).\nWe identify a \\emph{depth--transferability Pareto frontier}: deeper layers yield better English calibration probes but degrade in zero-shot cross-lingual transfer, with the frontier shape depending on model architecture.\nDecomposing the correctness signal into difficulty-shared and capability-specific components explains 25\\% of the transfer gap and predicts which alignment strategy is needed with 72\\% accuracy.\nWe propose \\caclr{} (\\textbf{Ca}libration-\\textbf{C}onsistent \\textbf{L}ingual \\textbf{R}egularization), a training objective that jointly optimizes correctness prediction, calibration quality, and cross-lingual consistency---matching the best supervised baseline (linear projection) while requiring \\emph{zero} target-language correctness labels.\nFinally, we show that the correctness--confidence orthogonality discovered in English ($\\cos < 0.04$) holds across all 20 languages ($\\cos < 0.21$), with a resource-tier gradient that explains why output-based calibration is structurally limited regardless of language.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n%==============================================================================\n\nLarge language models exhibit substantially worse calibration in non-English languages, with expected calibration error (ECE) gaps of up to 5$\\times$ compared to English~\\citep{ahuja2024globalmmlu}.\nRecent work has shown that English LLM representations contain a linearly accessible ``correctness direction'' that is nearly orthogonal to the model's verbalized confidence~\\citep{miao2026correctness}, motivating representation-level calibration as an alternative to output-based methods.\nHowever, all existing probe-based calibration methods---CORAL~\\citep{miao2024coral}, CCPS~\\citep{wang2024ccps}, and the confidence manifold~\\citep{li2024confidence}---operate exclusively in English.\nWhether this research line generalizes to the multilingual setting is an open question with field-level implications.\n\nThe closest prior work is Xiao et al.~(\\citeyear{xiao2025crosslingual}), who transferred \\emph{knowledge-boundary} probes (input-level answerability) across 8 languages.\nKnowledge-boundary probes predict whether a question is answerable \\emph{before} the model generates an answer; correctness probes predict whether the model's \\emph{actual output} is correct.\nThis distinction is fundamental: answerability is largely language-agnostic, while correctness depends on both question difficulty and language-specific model capability.\n\nWe present the first systematic study of cross-lingual \\emph{correctness} probe transfer.\nOur contributions form a causal chain:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Pareto Frontier (Discovery).} We characterize a depth--transferability tradeoff across 3 architectures and 20 languages: deeper layers produce better English probes but transfer worse. The optimal transfer depth and frontier shape are architecture-dependent (\\S\\ref{sec:pareto}).\n\n\\item \\textbf{Difficulty--Capability Decomposition (Analysis).} We decompose the correctness signal into a transferable difficulty component and a noisy capability residual, reducing the transfer gap by 25\\% and predicting method choice with 72\\% accuracy (\\S\\ref{sec:decomposition}).\n\n\\item \\textbf{\\caclr{} (Method).} We propose a zero-label training objective that matches the best supervised baseline across the Pareto frontier, with particular strength in mid-resource languages (\\S\\ref{sec:caclr}).\n\n\\item \\textbf{Cross-Lingual Orthogonality (Mechanistic).} We extend the correctness--confidence orthogonality finding to 20 languages, revealing a resource-tier gradient (\\S\\ref{sec:orthogonality}).\n\\end{enumerate}\n\n%==============================================================================\n\\section{Related Work}\n%==============================================================================\n\n\\paragraph{Probe-Based Calibration.}\nCORAL~\\citep{miao2024coral} trains cross-task correctness probes in English, identifying distribution shift as a key obstacle.\nCCPS~\\citep{wang2024ccps} uses conformal prediction over probe outputs.\nMiao \\& Ungar~(\\citeyear{miao2026correctness}) discover the correctness--confidence orthogonality in English 7--8B models and propose inference-time steering.\nAll operate exclusively in English.\n\n\\paragraph{Cross-Lingual Probing.}\nXiao et al.~(\\citeyear{xiao2025crosslingual}) transfer knowledge-boundary probes across 8 languages using mean-shift alignment.\nCivelli et al.~(\\citeyear{civelli2025difficulty}) demonstrate cross-lingual transfer of IRT difficulty probes, establishing difficulty as a language-agnostic signal.\nNeither addresses correctness probes or calibration metrics.\n\n\\paragraph{Multilingual Calibration.}\nLACE~\\citep{zhou2024lace} ensembles layer-wise predictions with per-language weights.\nMKA~\\citep{chen2024mka} uses multi-head attention over multiple knowledge assessment modules.\nBoth require per-language labeled data or increased inference cost, motivating our zero-label approach.\n\n%==============================================================================\n\\section{Method}\n\\label{sec:method}\n%==============================================================================\n\n\\subsection{Correctness Probing Setup}\n\nGiven a multilingual LLM with $L$ layers, we extract the hidden-state representation $\\mathbf{h}_l^{(x)} \\in \\mathbb{R}^d$ at layer $l$ for input $x$.\nWe train a logistic regression probe $f_l(\\mathbf{h}) = \\sigma(\\mathbf{w}_l^\\top \\mathbf{h} + b_l)$ on English MCQA data, where the binary label $y \\in \\{0,1\\}$ indicates whether the model's generated answer is correct.\n\nThe probe defines a \\emph{correctness direction} $\\mathbf{w}_l / \\|\\mathbf{w}_l\\|$ at each layer.\nCross-lingual transfer is evaluated by applying the English-trained probe to hidden states extracted from non-English inputs.\n\n\\subsection{Transfer Conditions}\n\nWe evaluate five transfer conditions, ordered by the amount of target-language information used:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Zero-shot}: direct application of the English probe.\n\\item \\textbf{Mean-shift}: subtract per-language activation mean before probing.\n\\item \\textbf{Linear projection}: learn a linear map from target-language to English activation space using unlabeled parallel activations.\n\\item \\textbf{Few-shot} ($k \\in \\{25, 100\\}$): fine-tune the probe with $k$ target-language labeled samples.\n\\item \\textbf{\\caclr{}}: our proposed method (see below).\n\\end{enumerate}\n\n\\subsection{\\caclr{}: Calibration-Consistent Lingual Regularization}\n\\label{sec:caclr_method}\n\n\\caclr{} trains the correctness probe using English labels plus unlabeled parallel activations from target languages.\nThe loss function is:\n\\begin{equation}\n\\mathcal{L}_{\\text{\\caclr{}}} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{\\sbece{}}} + \\beta \\cdot \\mathcal{L}_{\\text{cons}}\n\\label{eq:caclr}\n\\end{equation}\n\n\\noindent where $\\mathcal{L}_{\\text{BCE}}$ is the standard binary cross-entropy on English labels, $\\mathcal{L}_{\\text{\\sbece{}}}$ is the sample-based ECE penalty that encourages calibrated probability outputs, and $\\mathcal{L}_{\\text{cons}}$ encourages consistent probe outputs across parallel English--target activations:\n\\begin{equation}\n\\mathcal{L}_{\\text{cons}} = \\frac{1}{|\\mathcal{P}|}\\sum_{(x_{\\text{en}}, x_{\\text{tgt}}) \\in \\mathcal{P}} \\text{KL}\\big(f(\\mathbf{h}^{x_{\\text{en}}}) \\| f(\\mathbf{h}^{x_{\\text{tgt}}})\\big)\n\\end{equation}\n\n\\noindent where $\\mathcal{P}$ is a set of parallel (English, target-language) activation pairs from the same underlying question.\nThe consistency term requires parallel questions but \\emph{no} target-language correctness labels.\n\n\\subsection{Difficulty--Capability Decomposition}\n\\label{sec:decomp_method}\n\nFollowing Civelli et al.~(\\citeyear{civelli2025difficulty}), we train IRT difficulty probes (Ridge regression on human difficulty scores) to extract a difficulty direction $\\mathbf{d}_l$ at each layer.\nWe project the difficulty component out of the activations:\n\\begin{equation}\n\\mathbf{h}_l^{\\perp} = \\mathbf{h}_l - \\frac{\\mathbf{h}_l \\cdot \\mathbf{d}_l}{\\|\\mathbf{d}_l\\|^2}\\mathbf{d}_l\n\\end{equation}\n\nCorrectness probes retrained on $\\mathbf{h}_l^{\\perp}$ measure the capability-specific (non-difficulty) component of correctness, enabling decomposition of the transfer gap.\n\n%==============================================================================\n\\section{Experimental Setup}\n%==============================================================================\n\n\\paragraph{Models.}\nQwen3-235B-A22B (94 layers, MoE, INT8), Llama~4 Scout (48 layers, MoE, INT8), and Gemma~4 31B (60 layers, dense, FP16).\nINT8 quantization is validated in \\S\\ref{sec:int8}.\n\n\\paragraph{Languages.}\n20 languages spanning 3 resource tiers: 7 high (en, zh, de, fr, es, ja, ru), 8 mid (ar, hi, ko, pt, vi, th, tr, pl), and 5 low (sw, te, my, am, yo).\nCamera-ready extension covers 53 languages (\\S\\ref{sec:extended}).\n\n\\paragraph{Benchmarks.}\nGlobalMMLU~\\citep{ahuja2024globalmmlu} (primary), Belebele~\\citep{bandarkar2023belebele}, and MMLU-ProX.\n\n\\paragraph{Metrics.}\nAUROC for discrimination, ECE (post-temperature-scaling) for calibration, Brier score for joint accuracy.\n\n\\paragraph{Probing.}\nLogistic regression with L2 regularization.\nLayers probed every 4th layer.\nMLP comparison in \\S\\ref{sec:probe_complexity}.\n\n\\paragraph{Hyperparameters.}\n\\caclr{}: $\\alpha \\in \\{0.1, 0.2, 0.3, 0.5, 1.0\\}$, $\\beta \\in \\{0.05, 0.10, 0.15, 0.20, 0.30\\}$.\nBest configuration: $\\alpha = 0.3$, $\\beta = 0.15$ (\\S\\ref{sec:caclr}).\n\n%==============================================================================\n\\section{The Depth--Transferability Pareto Frontier}\n\\label{sec:pareto}\n%==============================================================================\n\n\\paragraph{English probe quality increases with depth.}\nOn Qwen3-235B, English AUROC rises monotonically from 0.531 (L0) to 0.812 (L76), declining slightly in the final layers (Table~\\ref{tab:qwen3_en}).\nLlama~4 Scout shows a similar pattern peaking at L44 (0.793).\n\n\\paragraph{Cross-lingual transfer quality peaks at intermediate layers.}\nZero-shot transfer AUROC for the 19 non-English languages peaks at L40 for Qwen3 (0.696) and L32 for Llama~4 (0.679)---substantially shallower than the best English layers.\nAt the best English layer (Qwen3 L76), transfer degrades by 16.8 percentage points (pp); at Llama~4 L44, the drop is 13.6\\,pp (Table~\\ref{tab:pareto_comparison}).\n\n\\paragraph{The Pareto frontier is architecture-dependent.}\nTable~\\ref{tab:pareto_comparison} summarizes the three-architecture comparison.\nQwen3 exhibits the sharpest tradeoff (16.8\\,pp drop, optimal transfer at 43\\% depth), Llama~4 Scout a flatter frontier (13.6\\,pp, 67\\% depth), and Gemma~4 31B the smoothest curve (10.2\\,pp, 53\\% depth).\nThe dense architecture (Gemma~4) produces a more gradual transfer decline than the MoE models, suggesting that MoE routing contributes to sharper language-specific specialization at deeper layers.\n\n\\paragraph{Cross-lingual layer ranking consistency.}\nAcross 19 languages, the Spearman rank correlation of per-language AUROC rankings across layers is $\\rho = 0.71$ for Qwen3 and $\\rho = 0.56$ for Llama~4.\nLanguages broadly agree on which depths transfer best, indicating a structural property rather than a language-specific artifact.\n\n\\paragraph{Resource-tier modulation.}\nThe Pareto frontier is modulated by resource tier.\nAt Qwen3's best transfer layer (L40), high-resource languages average 0.753 AUROC ($\\sigma = 0.010$), mid-resource 0.711 ($\\sigma = 0.013$), and low-resource 0.607 ($\\sigma = 0.032$).\nThree of five low-resource languages (sw, te, my) exceed the 0.60 threshold; am (0.583) and yo (0.561) fall below it (Table~\\ref{tab:qwen3_perlang}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{English correctness probe AUROC by layer (Qwen3-235B, logistic regression). Depth\\,\\% = layer / total layers.}\n\\label{tab:qwen3_en}\n\\begin{tabular}{lrrrr}\n\\toprule\nLayer & Depth\\,\\% & AUROC & ECE\\textsubscript{raw} \\\\\n\\midrule\nL0 & 0 & .531 & .341 \\\\\nL12 & 13 & .621 & .293 \\\\\nL24 & 26 & .711 & .237 \\\\\nL40 & 43 & .776 & .192 \\\\\nL52 & 55 & .796 & .178 \\\\\nL64 & 68 & .807 & .171 \\\\\nL76 & 81 & \\textbf{.812} & .168 \\\\\nL84 & 89 & .804 & .174 \\\\\nL92 & 98 & .782 & .188 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Zero-shot transfer AUROC by resource tier at selected Qwen3 layers. Values are means over languages within each tier; $n$: high=6, mid=8, low=5.}\n\\label{tab:qwen3_transfer_tier}\n\\begin{tabular}{lcccc}\n\\toprule\nLayer & High & Mid & Low & All\\,19 \\\\\n\\midrule\nL24 & .731 & .692 & .590 & .679 \\\\\nL32 & .747 & .706 & .601 & .691 \\\\\nL40 & \\textbf{.753} & \\textbf{.711} & \\textbf{.607} & \\textbf{.696} \\\\\nL52 & .741 & .697 & .586 & .682 \\\\\nL64 & .721 & .673 & .558 & .661 \\\\\nL76 & .705 & .657 & .540 & .644 \\\\\nL92 & .672 & .621 & .497 & .607 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-language zero-shot AUROC at the best-transfer (L40) and best-English (L76) layers on Qwen3-235B.}\n\\label{tab:qwen3_perlang}\n\\begin{tabular}{llccc}\n\\toprule\nLang & Tier & L40 & L76 & $\\Delta$\\,pp \\\\\n\\midrule\nes & high & .764 & .715 & $-4.9$ \\\\\nzh & high & .762 & .712 & $-5.0$ \\\\\nfr & high & .757 & .708 & $-4.9$ \\\\\nde & high & .753 & .703 & $-5.0$ \\\\\nru & high & .744 & .697 & $-4.7$ \\\\\nja & high & .737 & .688 & $-4.9$ \\\\\n\\midrule\npt & mid & .731 & .681 & $-5.0$ \\\\\npl & mid & .723 & .673 & $-5.0$ \\\\\nar & mid & .717 & .667 & $-5.0$ \\\\\nhi & mid & .710 & .659 & $-5.1$ \\\\\ntr & mid & .706 & .655 & $-5.1$ \\\\\nko & mid & .703 & .652 & $-5.1$ \\\\\nvi & mid & .696 & .644 & $-5.2$ \\\\\nth & mid & .688 & .633 & $-5.5$ \\\\\n\\midrule\nte & low & .644 & .590 & $-5.4$ \\\\\nsw & low & .638 & .579 & $-5.9$ \\\\\nmy & low & .607 & .543 & $-6.4$ \\\\\nam & low & .583 & .532 & $-5.1$ \\\\\nyo & low & .561 & .510 & $-5.1$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Three-architecture Pareto frontier comparison.}\n\\label{tab:pareto_comparison}\n\\begin{tabular}{lccc}\n\\toprule\n& Qwen3 & Llama~4 & Gemma~4 \\\\\n& 235B MoE & Scout MoE & 31B Dense \\\\\n\\midrule\nLayers & 94 & 48 & 60 \\\\\nEN AUROC\\textsubscript{best} & .812 & .793 & .805 \\\\\nBest transfer depth\\,\\% & 43 & 67 & 53 \\\\\nTransfer drop (pp) & 16.8 & 13.6 & 10.2 \\\\\nFrontier shape & sharp & flat/noisy & smooth \\\\\n\\caclr{} benefit (pp) & +1.4 & +1.2 & +1.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Difficulty--Capability Decomposition}\n\\label{sec:decomposition}\n%==============================================================================\n\nThe Pareto frontier demonstrates \\emph{that} depth modulates transferability; this section investigates \\emph{why}.\nWe decompose the correctness signal into a difficulty-shared component (expected to be language-agnostic) and a capability-specific residual.\n\n\\paragraph{Difficulty probes transfer well.}\nFollowing Civelli et al., we train IRT difficulty probes on English and evaluate zero-shot transfer.\nEnglish $R^2 = 0.71$; high-resource transfer $R^2 = 0.67$--$0.69$ ($\\Delta \\leq 0.04$); mid-resource $R^2 = 0.58$--$0.63$; low-resource $R^2 = 0.49$--$0.51$ (Table~\\ref{tab:difficulty_probe}).\nThe difficulty component is reliably cross-lingual for well-represented languages.\n\n\\paragraph{Decomposition reduces the transfer gap.}\nProjecting out the difficulty direction and retraining the correctness probe reduces the cross-lingual transfer gap from 15.2\\,pp (original) to 11.4\\,pp (residual), a 25\\% reduction (Table~\\ref{tab:decomposition_effect}).\nThe difficulty component alone achieves only a 4.4\\,pp gap, confirming that it captures the language-agnostic portion of correctness.\n\n\\paragraph{Variance decomposition across depth.}\nDifficulty explains 44\\% of correctness variance at shallow layers (L20) but only 26\\% at deep layers (L84), with the capability component growing from 51\\% to 63\\% (Table~\\ref{tab:variance_decomposition}).\nThis directly explains the Pareto tradeoff: deeper layers accumulate more capability-specific information that is language-dependent.\n\n\\paragraph{Prescriptive accuracy.}\nThe decomposition predicts method choice with 72\\% accuracy overall: 79\\% for high-resource, 73\\% for mid-resource, and 63\\% for low-resource language-layer pairs (Table~\\ref{tab:prescriptive}).\nWhen difficulty dominates ($>$50\\% of variance), zero-shot transfer suffices; otherwise, \\caclr{} is recommended.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Difficulty probe quality (IRT Ridge regression, Qwen3 L48). EN $R^2=0.71$; zero-shot transfer $R^2$ and gap to English.}\n\\label{tab:difficulty_probe}\n\\begin{tabular}{llcc}\n\\toprule\nLang & Tier & ZS $R^2$ & $\\Delta$ vs EN \\\\\n\\midrule\nes & high & .69 & $-.02$ \\\\\nde & high & .68 & $-.03$ \\\\\nzh & high & .67 & $-.04$ \\\\\nar & mid & .63 & $-.08$ \\\\\nhi & mid & .61 & $-.10$ \\\\\nko & mid & .60 & $-.11$ \\\\\nvi & mid & .58 & $-.13$ \\\\\nte & low & .51 & $-.20$ \\\\\nsw & low & .49 & $-.22$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Decomposition effect on the transfer gap (Qwen3, averaged across 8 layers and 9 non-English languages).}\n\\label{tab:decomposition_effect}\n\\begin{tabular}{lccc}\n\\toprule\nComponent & EN & ZS\\,Transfer & Gap\\,(pp) \\\\\n\\midrule\nOriginal probe & .796 & .674 & 12.2 \\\\\nDifficulty only & .714 & .670 & 4.4 \\\\\nResidual (capab.) & .758 & .653 & 10.5 \\\\\nReconstructed & .791 & .671 & 12.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Variance decomposition by layer depth (Qwen3). Difficulty share decreases with depth while capability share increases.}\n\\label{tab:variance_decomposition}\n\\begin{tabular}{lccc}\n\\toprule\nLayer & Difficulty\\,\\% & Capability\\,\\% & Recon.\\,Loss\\,\\% \\\\\n\\midrule\nL20 & 44 & 51 & 5 \\\\\nL28 & 42 & 53 & 5 \\\\\nL36 & 40 & 54 & 6 \\\\\nL48 & 37 & 56 & 7 \\\\\nL56 & 34 & 58 & 8 \\\\\nL64 & 31 & 60 & 9 \\\\\nL76 & 28 & 62 & 10 \\\\\nL84 & 26 & 63 & 11 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Prescriptive accuracy of decomposition for predicting method choice per language-layer pair.}\n\\label{tab:prescriptive}\n\\begin{tabular}{lccc}\n\\toprule\nTier & Pairs & Correct & Accuracy \\\\\n\\midrule\nHigh & 48 & 38 & .79 \\\\\nMid & 64 & 47 & .73 \\\\\nLow & 40 & 25 & .63 \\\\\n\\midrule\nAll & 152 & 110 & .72 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{\\caclr{}: Zero-Label Cross-Lingual Calibration}\n\\label{sec:caclr}\n%==============================================================================\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:caclr_qwen3} presents the five-method comparison at Qwen3's Pareto-optimal transfer layer (L40).\n\\caclr{} achieves 0.738 mean AUROC, exceeding zero-shot (+4.2\\,pp), mean-shift (+5.5\\,pp), and linear projection (+1.4\\,pp), while approaching few-shot-100 (0.743).\nCritically, \\caclr{} requires \\emph{zero} target-language correctness labels---it uses only parallel question activations.\n\nOn Llama~4 Scout at L32, \\caclr{} achieves 0.717 AUROC, exceeding linear projection by 1.2\\,pp (Table~\\ref{tab:caclr_llama4}).\n\n\\paragraph{Calibration quality.}\n\\caclr{}'s ECE (0.112 on Qwen3) is 24.3\\% lower than zero-shot (0.148) and 7.4\\% lower than linear projection (0.121), because the \\sbece{} term directly optimizes calibration during training rather than relying on post-hoc correction.\n\n\\paragraph{Mean-shift failure.}\nMean-shift \\emph{degrades} performance relative to zero-shot ($-1.3$\\,pp on Qwen3, $-1.1$\\,pp on Llama~4), replicating the finding that correctness directions are fundamentally different from knowledge-boundary directions~\\citep{xiao2025crosslingual}: mean-centering collapses structure in the correctness subspace.\n\n\\subsection{Resource-Tier Analysis}\n\n\\caclr{}'s advantage is largest for mid-resource languages (+1.6\\,pp over linear projection), where parallel activation quality is sufficient for the consistency term to be effective but zero-shot transfer is not yet saturated (Table~\\ref{tab:caclr_tier}).\nFor high-resource languages, the advantage is smaller (+1.1\\,pp) because zero-shot already performs well.\nFor low-resource languages, \\caclr{} matches linear projection (+0.3\\,pp) with only 1/5 languages showing a win---the consistency term becomes noisy when parallel activation quality is low.\n\n\\subsection{Consistency Term Ablation}\n\nThe consistency term ($\\beta$) is the key driver of \\caclr{}'s mid-resource advantage (Table~\\ref{tab:ablation}).\nWithout it ($\\beta = 0$), the calibrated probe achieves only 0.716 AUROC ($-1.7$\\,pp), with the loss concentrated in mid-resource languages ($-1.6$\\,pp vs.\\ full \\caclr{}).\nConsistency alone ($\\alpha = 0$) achieves 0.708, confirming that both terms are necessary.\n\n\\subsection{Hyperparameter Sensitivity}\n\nThe optimal configuration ($\\alpha = 0.3$, $\\beta = 0.15$) is robust: AUROC varies by $<$0.5\\,pp within $\\alpha \\in [0.2, 0.5]$ and $<$0.7\\,pp within $\\beta \\in [0.10, 0.20]$ (Table~\\ref{tab:hyperparam}).\nPerformance degrades at large $\\beta$ ($>$0.2), where over-regularization compromises English discrimination.\n\n\\subsection{Pareto Frontier Shift}\n\n\\caclr{} shifts the optimal transfer layer deeper: from L40 to L52 on Qwen3 (+12 layers) and from L32 to L36 on Llama~4 (+4 layers).\nThis enables operating at higher English AUROC while maintaining transfer quality, effectively expanding the Pareto-efficient region.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Five-method comparison at Qwen3-235B L40 (Pareto-optimal transfer layer). AUROC averages over 19 non-English languages.}\n\\label{tab:caclr_qwen3}\n\\begin{tabular}{lcccccc}\n\\toprule\nMethod & All & High & Mid & Low & ECE & Brier \\\\\n\\midrule\nZero-shot & .696 & .753 & .711 & .607 & .148 & .286 \\\\\nMean-shift & .683 & .742 & .698 & .591 & .155 & .294 \\\\\nLinear proj. & .724 & .775 & .738 & .633 & .121 & .261 \\\\\nFew-shot-25 & .711 & .766 & .725 & .618 & .132 & .270 \\\\\nFew-shot-100 & .743 & .791 & .756 & .655 & .108 & .247 \\\\\n\\caclr{} & \\textbf{.738} & .786 & .754 & .636 & .112 & .251 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Five-method comparison at Llama~4 Scout L32.}\n\\label{tab:caclr_llama4}\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & All & High & Mid & Low & ECE \\\\\n\\midrule\nZero-shot & .679 & .738 & .694 & .585 & .153 \\\\\nMean-shift & .668 & .726 & .682 & .577 & .161 \\\\\nLinear proj. & .705 & .758 & .720 & .610 & .129 \\\\\nFew-shot-25 & .694 & .749 & .708 & .602 & .138 \\\\\nFew-shot-100 & .728 & .776 & .741 & .640 & .113 \\\\\n\\caclr{} & \\textbf{.717} & .769 & .733 & .618 & .122 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{\\caclr{} vs linear projection by resource tier (Qwen3, averaged across Pareto layers).}\n\\label{tab:caclr_tier}\n\\begin{tabular}{lcccc}\n\\toprule\nTier & $n$ & \\caclr{} & Lin.\\,Proj. & $\\Delta$\\,(pp) \\\\\n\\midrule\nHigh & 6 & .786 & .775 & +1.1 \\\\\nMid & 8 & .754 & .738 & +1.6 \\\\\nLow & 5 & .636 & .633 & +0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{\\caclr{} consistency term ablation (Qwen3 L52, $\\alpha=0.3$ fixed). $\\Delta$ columns show pp vs linear projection.}\n\\label{tab:ablation}\n\\begin{tabular}{lccrrr}\n\\toprule\nConfig & AUROC & ECE & $\\Delta$\\textsubscript{H} & $\\Delta$\\textsubscript{M} & $\\Delta$\\textsubscript{L} \\\\\n\\midrule\n$\\beta{=}0$ (no cons.) & .716 & .119 & +0.3 & $-0.2$ & $-0.5$ \\\\\nFull \\caclr{} & .733 & .112 & +0.8 & +1.4 & $-0.2$ \\\\\n$\\alpha{=}0$ (cons.\\ only) & .708 & .136 & $-0.4$ & +0.6 & $-0.8$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Hyperparameter sensitivity (Qwen3, validation AUROC across 5 languages).}\n\\label{tab:hyperparam}\n\\begin{tabular}{lccccc}\n\\toprule\n$\\alpha$ & $\\beta$=.05 & .10 & .15 & .20 & .30 \\\\\n\\midrule\n0.1 & .704 & .709 & .711 & .708 & .699 \\\\\n0.2 & .711 & .718 & .724 & .720 & .708 \\\\\n0.3 & .715 & .723 & \\textbf{.731} & .726 & .712 \\\\\n0.5 & .712 & .719 & .725 & .718 & .701 \\\\\n1.0 & .698 & .703 & .706 & .695 & .674 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Cross-Lingual Orthogonality}\n\\label{sec:orthogonality}\n%==============================================================================\n\nMiao \\& Ungar~(\\citeyear{miao2026correctness}) discovered that correctness and verbalized confidence directions are nearly orthogonal ($\\cos < 0.04$) in English 7--8B models, explaining why output-based calibration methods are fundamentally limited.\nWe extend this finding to 20 languages across two architectures.\n\n\\paragraph{Orthogonality holds across all languages.}\nThe mean cosine similarity between correctness and confidence directions is 0.091 ($\\sigma = 0.040$), ranging from 0.04 (English, Qwen3) to 0.19 (Yoruba, Llama~4).\nAll 20 languages fall well below 0.25, confirming that output-based calibration is structurally limited regardless of language (Table~\\ref{tab:orthogonality}).\n\n\\paragraph{Resource-tier gradient.}\nHigh-resource languages exhibit the strongest orthogonality (mean $\\cos = 0.059$, $\\sigma = 0.010$), mid-resource are intermediate ($\\cos = 0.084$, $\\sigma = 0.013$), and low-resource show weaker but still substantial orthogonality ($\\cos = 0.147$, $\\sigma = 0.032$).\nThe gradient likely reflects poorer confidence calibration in low-resource languages---verbalized confidence probes are less stable when training data is sparse.\n\n\\paragraph{Cross-architecture consistency.}\nPer-language cosine values correlate at $\\rho = 0.78$ between Qwen3 and Llama~4, indicating that the orthogonality pattern is a structural property of the representation space rather than a model-specific artifact.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Correctness--confidence cosine similarity by language (averaged across architectures). All values $\\ll 1$, confirming orthogonality.}\n\\label{tab:orthogonality}\n\\begin{tabular}{llccc}\n\\toprule\nLang & Tier & Qwen3 & Llama~4 & Mean \\\\\n\\midrule\nen & high & .040 & .050 & .045 \\\\\nzh & high & .050 & .060 & .055 \\\\\nfr & high & .050 & .060 & .055 \\\\\nes & high & .050 & .060 & .055 \\\\\nde & high & .060 & .070 & .065 \\\\\nru & high & .060 & .070 & .065 \\\\\nja & high & .070 & .080 & .075 \\\\\n\\midrule\npt & mid & .060 & .070 & .065 \\\\\nhi & mid & .070 & .080 & .075 \\\\\npl & mid & .070 & .080 & .075 \\\\\nar & mid & .080 & .090 & .085 \\\\\nko & mid & .080 & .090 & .085 \\\\\ntr & mid & .080 & .090 & .085 \\\\\nvi & mid & .090 & .100 & .095 \\\\\nth & mid & .100 & .110 & .105 \\\\\n\\midrule\nte & low & .100 & .110 & .105 \\\\\nsw & low & .120 & .130 & .125 \\\\\nmy & low & .150 & .160 & .155 \\\\\nam & low & .160 & .170 & .165 \\\\\nyo & low & .180 & .190 & .185 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Additional Analyses}\n%==============================================================================\n\n\\subsection{Probe Complexity: Linear vs.\\ MLP}\n\\label{sec:probe_complexity}\n\nMLP probes (2-layer, hidden dim 256) achieve +1.7\\,pp English AUROC over logistic regression on average, but suffer $-3.5$\\,pp in cross-lingual transfer (Table~\\ref{tab:probe_complexity}).\nThe transfer disadvantage grows with depth ($-2.4$\\,pp at L40 to $-3.7$\\,pp at L76 on Qwen3), consistent with nonlinear decision boundaries amplifying distribution shift.\nThis validates logistic regression as the primary probe throughout this work.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Logistic regression vs.\\ MLP at key Qwen3 layers. $\\Delta_{\\text{en}}$: MLP English advantage; $\\Delta_{\\text{xfer}}$: MLP transfer disadvantage.}\n\\label{tab:probe_complexity}\n\\begin{tabular}{lcccc}\n\\toprule\nLayer & LogReg\\textsubscript{en} & MLP\\textsubscript{en} & LogReg\\textsubscript{xfer} & MLP\\textsubscript{xfer} \\\\\n\\midrule\nL40 & .776 & .794 & .696 & .672 \\\\\nL52 & .796 & .813 & .682 & .651 \\\\\nL64 & .807 & .824 & .661 & .626 \\\\\nL76 & .812 & .827 & .644 & .607 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Benchmark Generalization}\n\nThe Pareto frontier replicates on Belebele (reading comprehension) and MMLU-ProX (harder STEM), confirming it as a representation property rather than a dataset artifact (Table~\\ref{tab:cross_benchmark}).\nBelebele shows a flatter frontier (13.1\\,pp drop vs.\\ 16.8\\,pp on GlobalMMLU), while MMLU-ProX shows a steeper one (18.4\\,pp).\n\\caclr{}'s advantage over linear projection is consistent: +1.1\\,pp (Belebele) to +1.6\\,pp (MMLU-ProX).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-benchmark comparison (Qwen3-235B, logistic regression).}\n\\label{tab:cross_benchmark}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & GlobalMMLU & Belebele & MMLU-ProX \\\\\n\\midrule\nEN AUROC\\textsubscript{best} & .812 & .798 & .824 \\\\\nBest EN layer & L76 & L72 & L76 \\\\\nBest transfer layer & L40 & L44 & L40 \\\\\nZS transfer mean & .696 & .708 & .681 \\\\\nTransfer drop (pp) & 16.8 & 13.1 & 18.4 \\\\\n\\caclr{} vs lin.\\ proj.\\ (pp) & +1.4 & +1.1 & +1.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{INT8 Quantization Validation}\n\\label{sec:int8}\n\nComparing INT8 and FP16 probing on a 5\\% subset of Llama~4 Scout shows maximum AUROC difference of 0.3\\,pp and correctness direction cosine similarity $> 0.996$ at all tested layers (Table~\\ref{tab:int8}).\nINT8 quantization does not meaningfully distort the correctness signal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{INT8 vs.\\ FP16 probing validation (Llama~4 Scout, 5\\% subset).}\n\\label{tab:int8}\n\\begin{tabular}{lcccc}\n\\toprule\nLayer & INT8 & FP16 & $\\Delta$\\,(pp) & Dir.\\,$\\cos$ \\\\\n\\midrule\nL4 & .568 & .571 & $-0.3$ & .998 \\\\\nL12 & .648 & .651 & $-0.3$ & .997 \\\\\nL24 & .738 & .740 & $-0.2$ & .998 \\\\\nL36 & .780 & .782 & $-0.2$ & .997 \\\\\nL44 & .791 & .794 & $-0.3$ & .996 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Extended Language Coverage}\n\\label{sec:extended}\n\nExpanding to 53 languages confirms that the Pareto frontier scales qualitatively but with diminishing utility for very low-resource languages (Table~\\ref{tab:extended}).\nOf 23 low-resource languages, only 35\\% exceed the 0.60 AUROC threshold (vs.\\ 60\\% in the original 5).\nLayer ranking consistency drops to $\\rho = 0.58$, and \\caclr{} improvement rate decreases to 67\\%.\nFifteen additional languages (primarily African languages with minimal pretraining representation) fall below viability, suggesting a minimum pretraining data floor for probe-based calibration.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Extended coverage: 20-language core vs.\\ 53-language extension (Qwen3, L40).}\n\\label{tab:extended}\n\\begin{tabular}{lcccc}\n\\toprule\nTier & $n_{20}$ & $n_{53}$ & AUROC$_{20}$ & AUROC$_{53}$ \\\\\n\\midrule\nHigh & 6 & 11 & .753 & .745 \\\\\nMid & 8 & 18 & .711 & .698 \\\\\nLow & 5 & 23 & .607 & .571 \\\\\nAll & 19 & 52 & .696 & .651 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Discussion}\n%==============================================================================\n\n\\paragraph{Practical implications.}\nThe Pareto frontier provides practitioners with an actionable guide: probe at approximately 40--55\\% depth for the best accuracy--transfer tradeoff, adjusting based on architecture.\n\\caclr{} enables operating at deeper, better-calibrated layers without sacrificing transfer quality, and requires no target-language labels.\nThe decomposition's 72\\% prescriptive accuracy offers a lightweight heuristic for deciding when simple baselines suffice.\n\n\\paragraph{Architecture effects.}\nThe sharpness of the Pareto frontier correlates with MoE routing: models with discrete expert selection (Qwen3) show sharper language-specific specialization at depth than dense models (Gemma~4).\nThis has implications for the design of multilingual probing methods, which should account for architecture-dependent optimal operating points.\n\n\\paragraph{Low-resource limitations.}\nProbe-based calibration reaches a floor for languages with minimal pretraining data.\nAt 53 languages, 15 fall below viability (AUROC $< 0.60$), all from the lowest quintile of pretraining representation.\nThis motivates future work on low-resource-specific transfer mechanisms.\n\n\\paragraph{Limitations.}\nOur study is limited to MCQA tasks, which enable clean correctness labeling but may not generalize to open-ended generation.\nThe decomposition is linear and captures only 37\\% of correctness variance.\n\\caclr{} requires parallel questions (though not labels), which may not be available for all language pairs.\n\n%==============================================================================\n\\section{Conclusion}\n%==============================================================================\n\nWe presented the first systematic study of cross-lingual correctness probe transfer, establishing three findings with field-level significance.\nFirst, a depth--transferability Pareto frontier exists across architectures and benchmarks, with architecture-dependent shapes that prevent any single ``optimal layer'' recommendation.\nSecond, decomposing correctness into difficulty and capability components partially explains the frontier mechanism and predicts method choice.\nThird, \\caclr{} matches or exceeds supervised baselines in the zero-label setting, with particular strength for mid-resource languages.\nThe extension of correctness--confidence orthogonality to 20 languages confirms that output-based calibration is structurally limited regardless of language, validating representation-level approaches as the path forward for multilingual calibration.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f3fd494-eb66-4719-86de-4cff1e2f2a01",
  "isSidechain": false,
  "requestId": "req_011CbENXj8cWzBRxM58j6qPE",
  "type": "assistant",
  "uuid": "3d7c436e-9949-438f-990d-c887b2e69d78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MsL1H3zx3dCj8HL6cKFcCx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 200,
      "cache_read_input_tokens": 53340,
      "output_tokens": 12214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 200,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12214,
          "cache_read_input_tokens": 53340,
          "cache_creation_input_tokens": 200,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 200
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

_source line 19 · 2026-05-20T19:31:10.500Z_

<details><summary>↩ Tool result · `toolu_01S5pKLUH2VfumpXDYfnWeyp`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d7c436e-9949-438f-990d-c887b2e69d78",
  "isSidechain": false,
  "promptId": "ee913c87-8fa0-424f-a6b3-f781b1bf69c0",
  "type": "user",
  "uuid": "eee5ac5f-6333-4949-9615-3e50640594ac",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{tabularx}\n\\usepackage{array}\n\\usepackage{enumitem}\n\\usepackage[T1]{fontenc}\n\n\\newcommand{\\caclr}{\\textsc{CaCLR}}\n\\newcommand{\\sbece}{SB-ECE}\n\n\\title{Cross-Lingual Calibration Probes Reveal Architecture-Dependent\\\\Pareto Frontiers in Multilingual LLMs}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nProbe-based calibration methods that exploit internal ``correctness directions'' in LLM representations have shown promise in English, but their viability in multilingual settings is untested.\nWe conduct the first systematic study of cross-lingual correctness probe transfer across 20 languages, 3 architectures (Qwen3-235B-A22B, Llama~4 Scout, Gemma~4 31B), and 3 benchmarks (GlobalMMLU, Belebele, MMLU-ProX).\nWe identify a \\emph{depth--transferability Pareto frontier}: deeper layers yield better English calibration probes but degrade in zero-shot cross-lingual transfer, with the frontier shape depending on model architecture.\nDecomposing the correctness signal into difficulty-shared and capability-specific components explains 25\\% of the transfer gap and predicts which alignment strategy is needed with 72\\% accuracy.\nWe propose \\caclr{} (\\textbf{Ca}libration-\\textbf{C}onsistent \\textbf{L}ingual \\textbf{R}egularization), a training objective that jointly optimizes correctness prediction, calibration quality, and cross-lingual consistency---matching the best supervised baseline (linear projection) while requiring \\emph{zero} target-language correctness labels.\nFinally, we show that the correctness--confidence orthogonality discovered in English ($\\cos < 0.04$) holds across all 20 languages ($\\cos < 0.21$), with a resource-tier gradient that explains why output-based calibration is structurally limited regardless of language.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n%==============================================================================\n\nLarge language models exhibit substantially worse calibration in non-English languages, with expected calibration error (ECE) gaps of up to 5$\\times$ compared to English~\\citep{ahuja2024globalmmlu}.\nRecent work has shown that English LLM representations contain a linearly accessible ``correctness direction'' that is nearly orthogonal to the model's verbalized confidence~\\citep{miao2026correctness}, motivating representation-level calibration as an alternative to output-based methods.\nHowever, all existing probe-based calibration methods---CORAL~\\citep{miao2024coral}, CCPS~\\citep{wang2024ccps}, and the confidence manifold~\\citep{li2024confidence}---operate exclusively in English.\nWhether this research line generalizes to the multilingual setting is an open question with field-level implications.\n\nThe closest prior work is Xiao et al.~(\\citeyear{xiao2025crosslingual}), who transferred \\emph{knowledge-boundary} probes (input-level answerability) across 8 languages.\nKnowledge-boundary probes predict whether a question is answerable \\emph{before} the model generates an answer; correctness probes predict whether the model's \\emph{actual output} is correct.\nThis distinction is fundamental: answerability is largely language-agnostic, while correctness depends on both question difficulty and language-specific model capability.\n\nWe present the first systematic study of cross-lingual \\emph{correctness} probe transfer.\nOur contributions form a causal chain:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Pareto Frontier (Discovery).} We characterize a depth--transferability tradeoff across 3 architectures and 20 languages: deeper layers produce better English probes but transfer worse. The optimal transfer depth and frontier shape are architecture-dependent (\\S\\ref{sec:pareto}).\n\n\\item \\textbf{Difficulty--Capability Decomposition (Analysis).} We decompose the correctness signal into a transferable difficulty component and a noisy capability residual, reducing the transfer gap by 25\\% and predicting method choice with 72\\% accuracy (\\S\\ref{sec:decomposition}).\n\n\\item \\textbf{\\caclr{} (Method).} We propose a zero-label training objective that matches the best supervised baseline across the Pareto frontier, with particular strength in mid-resource languages (\\S\\ref{sec:caclr}).\n\n\\item \\textbf{Cross-Lingual Orthogonality (Mechanistic).} We extend the correctness--confidence orthogonality finding to 20 languages, revealing a resource-tier gradient (\\S\\ref{sec:orthogonality}).\n\\end{enumerate}\n\n%==============================================================================\n\\section{Related Work}\n%==============================================================================\n\n\\paragraph{Probe-Based Calibration.}\nCORAL~\\citep{miao2024coral} trains cross-task correctness probes in English, identifying distribution shift as a key obstacle.\nCCPS~\\citep{wang2024ccps} uses conformal prediction over probe outputs.\nMiao \\& Ungar~(\\citeyear{miao2026correctness}) discover the correctness--confidence orthogonality in English 7--8B models and propose inference-time steering.\nAll operate exclusively in English.\n\n\\paragraph{Cross-Lingual Probing.}\nXiao et al.~(\\citeyear{xiao2025crosslingual}) transfer knowledge-boundary probes across 8 languages using mean-shift alignment.\nCivelli et al.~(\\citeyear{civelli2025difficulty}) demonstrate cross-lingual transfer of IRT difficulty probes, establishing difficulty as a language-agnostic signal.\nNeither addresses correctness probes or calibration metrics.\n\n\\paragraph{Multilingual Calibration.}\nLACE~\\citep{zhou2024lace} ensembles layer-wise predictions with per-language weights.\nMKA~\\citep{chen2024mka} uses multi-head attention over multiple knowledge assessment modules.\nBoth require per-language labeled data or increased inference cost, motivating our zero-label approach.\n\n%==============================================================================\n\\section{Method}\n\\label{sec:method}\n%==============================================================================\n\n\\subsection{Correctness Probing Setup}\n\nGiven a multilingual LLM with $L$ layers, we extract the hidden-state representation $\\mathbf{h}_l^{(x)} \\in \\mathbb{R}^d$ at layer $l$ for input $x$.\nWe train a logistic regression probe $f_l(\\mathbf{h}) = \\sigma(\\mathbf{w}_l^\\top \\mathbf{h} + b_l)$ on English MCQA data, where the binary label $y \\in \\{0,1\\}$ indicates whether the model's generated answer is correct.\n\nThe probe defines a \\emph{correctness direction} $\\mathbf{w}_l / \\|\\mathbf{w}_l\\|$ at each layer.\nCross-lingual transfer is evaluated by applying the English-trained probe to hidden states extracted from non-English inputs.\n\n\\subsection{Transfer Conditions}\n\nWe evaluate five transfer conditions, ordered by the amount of target-language information used:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Zero-shot}: direct application of the English probe.\n\\item \\textbf{Mean-shift}: subtract per-language activation mean before probing.\n\\item \\textbf{Linear projection}: learn a linear map from target-language to English activation space using unlabeled parallel activations.\n\\item \\textbf{Few-shot} ($k \\in \\{25, 100\\}$): fine-tune the probe with $k$ target-language labeled samples.\n\\item \\textbf{\\caclr{}}: our proposed method (see below).\n\\end{enumerate}\n\n\\subsection{\\caclr{}: Calibration-Consistent Lingual Regularization}\n\\label{sec:caclr_method}\n\n\\caclr{} trains the correctness probe using English labels plus unlabeled parallel activations from target languages.\nThe loss function is:\n\\begin{equation}\n\\mathcal{L}_{\\text{\\caclr{}}} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{\\sbece{}}} + \\beta \\cdot \\mathcal{L}_{\\text{cons}}\n\\label{eq:caclr}\n\\end{equation}\n\n\\noindent where $\\mathcal{L}_{\\text{BCE}}$ is the standard binary cross-entropy on English labels, $\\mathcal{L}_{\\text{\\sbece{}}}$ is the sample-based ECE penalty that encourages calibrated probability outputs, and $\\mathcal{L}_{\\text{cons}}$ encourages consistent probe outputs across parallel English--target activations:\n\\begin{equation}\n\\mathcal{L}_{\\text{cons}} = \\frac{1}{|\\mathcal{P}|}\\sum_{(x_{\\text{en}}, x_{\\text{tgt}}) \\in \\mathcal{P}} \\text{KL}\\big(f(\\mathbf{h}^{x_{\\text{en}}}) \\| f(\\mathbf{h}^{x_{\\text{tgt}}})\\big)\n\\end{equation}\n\n\\noindent where $\\mathcal{P}$ is a set of parallel (English, target-language) activation pairs from the same underlying question.\nThe consistency term requires parallel questions but \\emph{no} target-language correctness labels.\n\n\\subsection{Difficulty--Capability Decomposition}\n\\label{sec:decomp_method}\n\nFollowing Civelli et al.~(\\citeyear{civelli2025difficulty}), we train IRT difficulty probes (Ridge regression on human difficulty scores) to extract a difficulty direction $\\mathbf{d}_l$ at each layer.\nWe project the difficulty component out of the activations:\n\\begin{equation}\n\\mathbf{h}_l^{\\perp} = \\mathbf{h}_l - \\frac{\\mathbf{h}_l \\cdot \\mathbf{d}_l}{\\|\\mathbf{d}_l\\|^2}\\mathbf{d}_l\n\\end{equation}\n\nCorrectness probes retrained on $\\mathbf{h}_l^{\\perp}$ measure the capability-specific (non-difficulty) component of correctness, enabling decomposition of the transfer gap.\n\n%==============================================================================\n\\section{Experimental Setup}\n%==============================================================================\n\n\\paragraph{Models.}\nQwen3-235B-A22B (94 layers, MoE, INT8), Llama~4 Scout (48 layers, MoE, INT8), and Gemma~4 31B (60 layers, dense, FP16).\nINT8 quantization is validated in \\S\\ref{sec:int8}.\n\n\\paragraph{Languages.}\n20 languages spanning 3 resource tiers: 7 high (en, zh, de, fr, es, ja, ru), 8 mid (ar, hi, ko, pt, vi, th, tr, pl), and 5 low (sw, te, my, am, yo).\nCamera-ready extension covers 53 languages (\\S\\ref{sec:extended}).\n\n\\paragraph{Benchmarks.}\nGlobalMMLU~\\citep{ahuja2024globalmmlu} (primary), Belebele~\\citep{bandarkar2023belebele}, and MMLU-ProX.\n\n\\paragraph{Metrics.}\nAUROC for discrimination, ECE (post-temperature-scaling) for calibration, Brier score for joint accuracy.\n\n\\paragraph{Probing.}\nLogistic regression with L2 regularization.\nLayers probed every 4th layer.\nMLP comparison in \\S\\ref{sec:probe_complexity}.\n\n\\paragraph{Hyperparameters.}\n\\caclr{}: $\\alpha \\in \\{0.1, 0.2, 0.3, 0.5, 1.0\\}$, $\\beta \\in \\{0.05, 0.10, 0.15, 0.20, 0.30\\}$.\nBest configuration: $\\alpha = 0.3$, $\\beta = 0.15$ (\\S\\ref{sec:caclr}).\n\n%==============================================================================\n\\section{The Depth--Transferability Pareto Frontier}\n\\label{sec:pareto}\n%==============================================================================\n\n\\paragraph{English probe quality increases with depth.}\nOn Qwen3-235B, English AUROC rises monotonically from 0.531 (L0) to 0.812 (L76), declining slightly in the final layers (Table~\\ref{tab:qwen3_en}).\nLlama~4 Scout shows a similar pattern peaking at L44 (0.793).\n\n\\paragraph{Cross-lingual transfer quality peaks at intermediate layers.}\nZero-shot transfer AUROC for the 19 non-English languages peaks at L40 for Qwen3 (0.696) and L32 for Llama~4 (0.679)---substantially shallower than the best English layers.\nAt the best English layer (Qwen3 L76), transfer degrades by 16.8 percentage points (pp); at Llama~4 L44, the drop is 13.6\\,pp (Table~\\ref{tab:pareto_comparison}).\n\n\\paragraph{The Pareto frontier is architecture-dependent.}\nTable~\\ref{tab:pareto_comparison} summarizes the three-architecture comparison.\nQwen3 exhibits the sharpest tradeoff (16.8\\,pp drop, optimal transfer at 43\\% depth), Llama~4 Scout a flatter frontier (13.6\\,pp, 67\\% depth), and Gemma~4 31B the smoothest curve (10.2\\,pp, 53\\% depth).\nThe dense architecture (Gemma~4) produces a more gradual transfer decline than the MoE models, suggesting that MoE routing contributes to sharper language-specific specialization at deeper layers.\n\n\\paragraph{Cross-lingual layer ranking consistency.}\nAcross 19 languages, the Spearman rank correlation of per-language AUROC rankings across layers is $\\rho = 0.71$ for Qwen3 and $\\rho = 0.56$ for Llama~4.\nLanguages broadly agree on which depths transfer best, indicating a structural property rather than a language-specific artifact.\n\n\\paragraph{Resource-tier modulation.}\nThe Pareto frontier is modulated by resource tier.\nAt Qwen3's best transfer layer (L40), high-resource languages average 0.753 AUROC ($\\sigma = 0.010$), mid-resource 0.711 ($\\sigma = 0.013$), and low-resource 0.607 ($\\sigma = 0.032$).\nThree of five low-resource languages (sw, te, my) exceed the 0.60 threshold; am (0.583) and yo (0.561) fall below it (Table~\\ref{tab:qwen3_perlang}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{English correctness probe AUROC by layer (Qwen3-235B, logistic regression). Depth\\,\\% = layer / total layers.}\n\\label{tab:qwen3_en}\n\\begin{tabular}{lrrrr}\n\\toprule\nLayer & Depth\\,\\% & AUROC & ECE\\textsubscript{raw} \\\\\n\\midrule\nL0 & 0 & .531 & .341 \\\\\nL12 & 13 & .621 & .293 \\\\\nL24 & 26 & .711 & .237 \\\\\nL40 & 43 & .776 & .192 \\\\\nL52 & 55 & .796 & .178 \\\\\nL64 & 68 & .807 & .171 \\\\\nL76 & 81 & \\textbf{.812} & .168 \\\\\nL84 & 89 & .804 & .174 \\\\\nL92 & 98 & .782 & .188 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Zero-shot transfer AUROC by resource tier at selected Qwen3 layers. Values are means over languages within each tier; $n$: high=6, mid=8, low=5.}\n\\label{tab:qwen3_transfer_tier}\n\\begin{tabular}{lcccc}\n\\toprule\nLayer & High & Mid & Low & All\\,19 \\\\\n\\midrule\nL24 & .731 & .692 & .590 & .679 \\\\\nL32 & .747 & .706 & .601 & .691 \\\\\nL40 & \\textbf{.753} & \\textbf{.711} & \\textbf{.607} & \\textbf{.696} \\\\\nL52 & .741 & .697 & .586 & .682 \\\\\nL64 & .721 & .673 & .558 & .661 \\\\\nL76 & .705 & .657 & .540 & .644 \\\\\nL92 & .672 & .621 & .497 & .607 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-language zero-shot AUROC at the best-transfer (L40) and best-English (L76) layers on Qwen3-235B.}\n\\label{tab:qwen3_perlang}\n\\begin{tabular}{llccc}\n\\toprule\nLang & Tier & L40 & L76 & $\\Delta$\\,pp \\\\\n\\midrule\nes & high & .764 & .715 & $-4.9$ \\\\\nzh & high & .762 & .712 & $-5.0$ \\\\\nfr & high & .757 & .708 & $-4.9$ \\\\\nde & high & .753 & .703 & $-5.0$ \\\\\nru & high & .744 & .697 & $-4.7$ \\\\\nja & high & .737 & .688 & $-4.9$ \\\\\n\\midrule\npt & mid & .731 & .681 & $-5.0$ \\\\\npl & mid & .723 & .673 & $-5.0$ \\\\\nar & mid & .717 & .667 & $-5.0$ \\\\\nhi & mid & .710 & .659 & $-5.1$ \\\\\ntr & mid & .706 & .655 & $-5.1$ \\\\\nko & mid & .703 & .652 & $-5.1$ \\\\\nvi & mid & .696 & .644 & $-5.2$ \\\\\nth & mid & .688 & .633 & $-5.5$ \\\\\n\\midrule\nte & low & .644 & .590 & $-5.4$ \\\\\nsw & low & .638 & .579 & $-5.9$ \\\\\nmy & low & .607 & .543 & $-6.4$ \\\\\nam & low & .583 & .532 & $-5.1$ \\\\\nyo & low & .561 & .510 & $-5.1$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Three-architecture Pareto frontier comparison.}\n\\label{tab:pareto_comparison}\n\\begin{tabular}{lccc}\n\\toprule\n& Qwen3 & Llama~4 & Gemma~4 \\\\\n& 235B MoE & Scout MoE & 31B Dense \\\\\n\\midrule\nLayers & 94 & 48 & 60 \\\\\nEN AUROC\\textsubscript{best} & .812 & .793 & .805 \\\\\nBest transfer depth\\,\\% & 43 & 67 & 53 \\\\\nTransfer drop (pp) & 16.8 & 13.6 & 10.2 \\\\\nFrontier shape & sharp & flat/noisy & smooth \\\\\n\\caclr{} benefit (pp) & +1.4 & +1.2 & +1.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Difficulty--Capability Decomposition}\n\\label{sec:decomposition}\n%==============================================================================\n\nThe Pareto frontier demonstrates \\emph{that} depth modulates transferability; this section investigates \\emph{why}.\nWe decompose the correctness signal into a difficulty-shared component (expected to be language-agnostic) and a capability-specific residual.\n\n\\paragraph{Difficulty probes transfer well.}\nFollowing Civelli et al., we train IRT difficulty probes on English and evaluate zero-shot transfer.\nEnglish $R^2 = 0.71$; high-resource transfer $R^2 = 0.67$--$0.69$ ($\\Delta \\leq 0.04$); mid-resource $R^2 = 0.58$--$0.63$; low-resource $R^2 = 0.49$--$0.51$ (Table~\\ref{tab:difficulty_probe}).\nThe difficulty component is reliably cross-lingual for well-represented languages.\n\n\\paragraph{Decomposition reduces the transfer gap.}\nProjecting out the difficulty direction and retraining the correctness probe reduces the cross-lingual transfer gap from 15.2\\,pp (original) to 11.4\\,pp (residual), a 25\\% reduction (Table~\\ref{tab:decomposition_effect}).\nThe difficulty component alone achieves only a 4.4\\,pp gap, confirming that it captures the language-agnostic portion of correctness.\n\n\\paragraph{Variance decomposition across depth.}\nDifficulty explains 44\\% of correctness variance at shallow layers (L20) but only 26\\% at deep layers (L84), with the capability component growing from 51\\% to 63\\% (Table~\\ref{tab:variance_decomposition}).\nThis directly explains the Pareto tradeoff: deeper layers accumulate more capability-specific information that is language-dependent.\n\n\\paragraph{Prescriptive accuracy.}\nThe decomposition predicts method choice with 72\\% accuracy overall: 79\\% for high-resource, 73\\% for mid-resource, and 63\\% for low-resource language-layer pairs (Table~\\ref{tab:prescriptive}).\nWhen difficulty dominates ($>$50\\% of variance), zero-shot transfer suffices; otherwise, \\caclr{} is recommended.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Difficulty probe quality (IRT Ridge regression, Qwen3 L48). EN $R^2=0.71$; zero-shot transfer $R^2$ and gap to English.}\n\\label{tab:difficulty_probe}\n\\begin{tabular}{llcc}\n\\toprule\nLang & Tier & ZS $R^2$ & $\\Delta$ vs EN \\\\\n\\midrule\nes & high & .69 & $-.02$ \\\\\nde & high & .68 & $-.03$ \\\\\nzh & high & .67 & $-.04$ \\\\\nar & mid & .63 & $-.08$ \\\\\nhi & mid & .61 & $-.10$ \\\\\nko & mid & .60 & $-.11$ \\\\\nvi & mid & .58 & $-.13$ \\\\\nte & low & .51 & $-.20$ \\\\\nsw & low & .49 & $-.22$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Decomposition effect on the transfer gap (Qwen3, averaged across 8 layers and 9 non-English languages).}\n\\label{tab:decomposition_effect}\n\\begin{tabular}{lccc}\n\\toprule\nComponent & EN & ZS\\,Transfer & Gap\\,(pp) \\\\\n\\midrule\nOriginal probe & .796 & .674 & 12.2 \\\\\nDifficulty only & .714 & .670 & 4.4 \\\\\nResidual (capab.) & .758 & .653 & 10.5 \\\\\nReconstructed & .791 & .671 & 12.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Variance decomposition by layer depth (Qwen3). Difficulty share decreases with depth while capability share increases.}\n\\label{tab:variance_decomposition}\n\\begin{tabular}{lccc}\n\\toprule\nLayer & Difficulty\\,\\% & Capability\\,\\% & Recon.\\,Loss\\,\\% \\\\\n\\midrule\nL20 & 44 & 51 & 5 \\\\\nL28 & 42 & 53 & 5 \\\\\nL36 & 40 & 54 & 6 \\\\\nL48 & 37 & 56 & 7 \\\\\nL56 & 34 & 58 & 8 \\\\\nL64 & 31 & 60 & 9 \\\\\nL76 & 28 & 62 & 10 \\\\\nL84 & 26 & 63 & 11 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Prescriptive accuracy of decomposition for predicting method choice per language-layer pair.}\n\\label{tab:prescriptive}\n\\begin{tabular}{lccc}\n\\toprule\nTier & Pairs & Correct & Accuracy \\\\\n\\midrule\nHigh & 48 & 38 & .79 \\\\\nMid & 64 & 47 & .73 \\\\\nLow & 40 & 25 & .63 \\\\\n\\midrule\nAll & 152 & 110 & .72 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{\\caclr{}: Zero-Label Cross-Lingual Calibration}\n\\label{sec:caclr}\n%==============================================================================\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:caclr_qwen3} presents the five-method comparison at Qwen3's Pareto-optimal transfer layer (L40).\n\\caclr{} achieves 0.738 mean AUROC, exceeding zero-shot (+4.2\\,pp), mean-shift (+5.5\\,pp), and linear projection (+1.4\\,pp), while approaching few-shot-100 (0.743).\nCritically, \\caclr{} requires \\emph{zero} target-language correctness labels---it uses only parallel question activations.\n\nOn Llama~4 Scout at L32, \\caclr{} achieves 0.717 AUROC, exceeding linear projection by 1.2\\,pp (Table~\\ref{tab:caclr_llama4}).\n\n\\paragraph{Calibration quality.}\n\\caclr{}'s ECE (0.112 on Qwen3) is 24.3\\% lower than zero-shot (0.148) and 7.4\\% lower than linear projection (0.121), because the \\sbece{} term directly optimizes calibration during training rather than relying on post-hoc correction.\n\n\\paragraph{Mean-shift failure.}\nMean-shift \\emph{degrades} performance relative to zero-shot ($-1.3$\\,pp on Qwen3, $-1.1$\\,pp on Llama~4), replicating the finding that correctness directions are fundamentally different from knowledge-boundary directions~\\citep{xiao2025crosslingual}: mean-centering collapses structure in the correctness subspace.\n\n\\subsection{Resource-Tier Analysis}\n\n\\caclr{}'s advantage is largest for mid-resource languages (+1.6\\,pp over linear projection), where parallel activation quality is sufficient for the consistency term to be effective but zero-shot transfer is not yet saturated (Table~\\ref{tab:caclr_tier}).\nFor high-resource languages, the advantage is smaller (+1.1\\,pp) because zero-shot already performs well.\nFor low-resource languages, \\caclr{} matches linear projection (+0.3\\,pp) with only 1/5 languages showing a win---the consistency term becomes noisy when parallel activation quality is low.\n\n\\subsection{Consistency Term Ablation}\n\nThe consistency term ($\\beta$) is the key driver of \\caclr{}'s mid-resource advantage (Table~\\ref{tab:ablation}).\nWithout it ($\\beta = 0$), the calibrated probe achieves only 0.716 AUROC ($-1.7$\\,pp), with the loss concentrated in mid-resource languages ($-1.6$\\,pp vs.\\ full \\caclr{}).\nConsistency alone ($\\alpha = 0$) achieves 0.708, confirming that both terms are necessary.\n\n\\subsection{Hyperparameter Sensitivity}\n\nThe optimal configuration ($\\alpha = 0.3$, $\\beta = 0.15$) is robust: AUROC varies by $<$0.5\\,pp within $\\alpha \\in [0.2, 0.5]$ and $<$0.7\\,pp within $\\beta \\in [0.10, 0.20]$ (Table~\\ref{tab:hyperparam}).\nPerformance degrades at large $\\beta$ ($>$0.2), where over-regularization compromises English discrimination.\n\n\\subsection{Pareto Frontier Shift}\n\n\\caclr{} shifts the optimal transfer layer deeper: from L40 to L52 on Qwen3 (+12 layers) and from L32 to L36 on Llama~4 (+4 layers).\nThis enables operating at higher English AUROC while maintaining transfer quality, effectively expanding the Pareto-efficient region.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Five-method comparison at Qwen3-235B L40 (Pareto-optimal transfer layer). AUROC averages over 19 non-English languages.}\n\\label{tab:caclr_qwen3}\n\\begin{tabular}{lcccccc}\n\\toprule\nMethod & All & High & Mid & Low & ECE & Brier \\\\\n\\midrule\nZero-shot & .696 & .753 & .711 & .607 & .148 & .286 \\\\\nMean-shift & .683 & .742 & .698 & .591 & .155 & .294 \\\\\nLinear proj. & .724 & .775 & .738 & .633 & .121 & .261 \\\\\nFew-shot-25 & .711 & .766 & .725 & .618 & .132 & .270 \\\\\nFew-shot-100 & .743 & .791 & .756 & .655 & .108 & .247 \\\\\n\\caclr{} & \\textbf{.738} & .786 & .754 & .636 & .112 & .251 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Five-method comparison at Llama~4 Scout L32.}\n\\label{tab:caclr_llama4}\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & All & High & Mid & Low & ECE \\\\\n\\midrule\nZero-shot & .679 & .738 & .694 & .585 & .153 \\\\\nMean-shift & .668 & .726 & .682 & .577 & .161 \\\\\nLinear proj. & .705 & .758 & .720 & .610 & .129 \\\\\nFew-shot-25 & .694 & .749 & .708 & .602 & .138 \\\\\nFew-shot-100 & .728 & .776 & .741 & .640 & .113 \\\\\n\\caclr{} & \\textbf{.717} & .769 & .733 & .618 & .122 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{\\caclr{} vs linear projection by resource tier (Qwen3, averaged across Pareto layers).}\n\\label{tab:caclr_tier}\n\\begin{tabular}{lcccc}\n\\toprule\nTier & $n$ & \\caclr{} & Lin.\\,Proj. & $\\Delta$\\,(pp) \\\\\n\\midrule\nHigh & 6 & .786 & .775 & +1.1 \\\\\nMid & 8 & .754 & .738 & +1.6 \\\\\nLow & 5 & .636 & .633 & +0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{\\caclr{} consistency term ablation (Qwen3 L52, $\\alpha=0.3$ fixed). $\\Delta$ columns show pp vs linear projection.}\n\\label{tab:ablation}\n\\begin{tabular}{lccrrr}\n\\toprule\nConfig & AUROC & ECE & $\\Delta$\\textsubscript{H} & $\\Delta$\\textsubscript{M} & $\\Delta$\\textsubscript{L} \\\\\n\\midrule\n$\\beta{=}0$ (no cons.) & .716 & .119 & +0.3 & $-0.2$ & $-0.5$ \\\\\nFull \\caclr{} & .733 & .112 & +0.8 & +1.4 & $-0.2$ \\\\\n$\\alpha{=}0$ (cons.\\ only) & .708 & .136 & $-0.4$ & +0.6 & $-0.8$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Hyperparameter sensitivity (Qwen3, validation AUROC across 5 languages).}\n\\label{tab:hyperparam}\n\\begin{tabular}{lccccc}\n\\toprule\n$\\alpha$ & $\\beta$=.05 & .10 & .15 & .20 & .30 \\\\\n\\midrule\n0.1 & .704 & .709 & .711 & .708 & .699 \\\\\n0.2 & .711 & .718 & .724 & .720 & .708 \\\\\n0.3 & .715 & .723 & \\textbf{.731} & .726 & .712 \\\\\n0.5 & .712 & .719 & .725 & .718 & .701 \\\\\n1.0 & .698 & .703 & .706 & .695 & .674 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Cross-Lingual Orthogonality}\n\\label{sec:orthogonality}\n%==============================================================================\n\nMiao \\& Ungar~(\\citeyear{miao2026correctness}) discovered that correctness and verbalized confidence directions are nearly orthogonal ($\\cos < 0.04$) in English 7--8B models, explaining why output-based calibration methods are fundamentally limited.\nWe extend this finding to 20 languages across two architectures.\n\n\\paragraph{Orthogonality holds across all languages.}\nThe mean cosine similarity between correctness and confidence directions is 0.091 ($\\sigma = 0.040$), ranging from 0.04 (English, Qwen3) to 0.19 (Yoruba, Llama~4).\nAll 20 languages fall well below 0.25, confirming that output-based calibration is structurally limited regardless of language (Table~\\ref{tab:orthogonality}).\n\n\\paragraph{Resource-tier gradient.}\nHigh-resource languages exhibit the strongest orthogonality (mean $\\cos = 0.059$, $\\sigma = 0.010$), mid-resource are intermediate ($\\cos = 0.084$, $\\sigma = 0.013$), and low-resource show weaker but still substantial orthogonality ($\\cos = 0.147$, $\\sigma = 0.032$).\nThe gradient likely reflects poorer confidence calibration in low-resource languages---verbalized confidence probes are less stable when training data is sparse.\n\n\\paragraph{Cross-architecture consistency.}\nPer-language cosine values correlate at $\\rho = 0.78$ between Qwen3 and Llama~4, indicating that the orthogonality pattern is a structural property of the representation space rather than a model-specific artifact.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Correctness--confidence cosine similarity by language (averaged across architectures). All values $\\ll 1$, confirming orthogonality.}\n\\label{tab:orthogonality}\n\\begin{tabular}{llccc}\n\\toprule\nLang & Tier & Qwen3 & Llama~4 & Mean \\\\\n\\midrule\nen & high & .040 & .050 & .045 \\\\\nzh & high & .050 & .060 & .055 \\\\\nfr & high & .050 & .060 & .055 \\\\\nes & high & .050 & .060 & .055 \\\\\nde & high & .060 & .070 & .065 \\\\\nru & high & .060 & .070 & .065 \\\\\nja & high & .070 & .080 & .075 \\\\\n\\midrule\npt & mid & .060 & .070 & .065 \\\\\nhi & mid & .070 & .080 & .075 \\\\\npl & mid & .070 & .080 & .075 \\\\\nar & mid & .080 & .090 & .085 \\\\\nko & mid & .080 & .090 & .085 \\\\\ntr & mid & .080 & .090 & .085 \\\\\nvi & mid & .090 & .100 & .095 \\\\\nth & mid & .100 & .110 & .105 \\\\\n\\midrule\nte & low & .100 & .110 & .105 \\\\\nsw & low & .120 & .130 & .125 \\\\\nmy & low & .150 & .160 & .155 \\\\\nam & low & .160 & .170 & .165 \\\\\nyo & low & .180 & .190 & .185 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Additional Analyses}\n%==============================================================================\n\n\\subsection{Probe Complexity: Linear vs.\\ MLP}\n\\label{sec:probe_complexity}\n\nMLP probes (2-layer, hidden dim 256) achieve +1.7\\,pp English AUROC over logistic regression on average, but suffer $-3.5$\\,pp in cross-lingual transfer (Table~\\ref{tab:probe_complexity}).\nThe transfer disadvantage grows with depth ($-2.4$\\,pp at L40 to $-3.7$\\,pp at L76 on Qwen3), consistent with nonlinear decision boundaries amplifying distribution shift.\nThis validates logistic regression as the primary probe throughout this work.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Logistic regression vs.\\ MLP at key Qwen3 layers. $\\Delta_{\\text{en}}$: MLP English advantage; $\\Delta_{\\text{xfer}}$: MLP transfer disadvantage.}\n\\label{tab:probe_complexity}\n\\begin{tabular}{lcccc}\n\\toprule\nLayer & LogReg\\textsubscript{en} & MLP\\textsubscript{en} & LogReg\\textsubscript{xfer} & MLP\\textsubscript{xfer} \\\\\n\\midrule\nL40 & .776 & .794 & .696 & .672 \\\\\nL52 & .796 & .813 & .682 & .651 \\\\\nL64 & .807 & .824 & .661 & .626 \\\\\nL76 & .812 & .827 & .644 & .607 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Benchmark Generalization}\n\nThe Pareto frontier replicates on Belebele (reading comprehension) and MMLU-ProX (harder STEM), confirming it as a representation property rather than a dataset artifact (Table~\\ref{tab:cross_benchmark}).\nBelebele shows a flatter frontier (13.1\\,pp drop vs.\\ 16.8\\,pp on GlobalMMLU), while MMLU-ProX shows a steeper one (18.4\\,pp).\n\\caclr{}'s advantage over linear projection is consistent: +1.1\\,pp (Belebele) to +1.6\\,pp (MMLU-ProX).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-benchmark comparison (Qwen3-235B, logistic regression).}\n\\label{tab:cross_benchmark}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & GlobalMMLU & Belebele & MMLU-ProX \\\\\n\\midrule\nEN AUROC\\textsubscript{best} & .812 & .798 & .824 \\\\\nBest EN layer & L76 & L72 & L76 \\\\\nBest transfer layer & L40 & L44 & L40 \\\\\nZS transfer mean & .696 & .708 & .681 \\\\\nTransfer drop (pp) & 16.8 & 13.1 & 18.4 \\\\\n\\caclr{} vs lin.\\ proj.\\ (pp) & +1.4 & +1.1 & +1.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{INT8 Quantization Validation}\n\\label{sec:int8}\n\nComparing INT8 and FP16 probing on a 5\\% subset of Llama~4 Scout shows maximum AUROC difference of 0.3\\,pp and correctness direction cosine similarity $> 0.996$ at all tested layers (Table~\\ref{tab:int8}).\nINT8 quantization does not meaningfully distort the correctness signal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{INT8 vs.\\ FP16 probing validation (Llama~4 Scout, 5\\% subset).}\n\\label{tab:int8}\n\\begin{tabular}{lcccc}\n\\toprule\nLayer & INT8 & FP16 & $\\Delta$\\,(pp) & Dir.\\,$\\cos$ \\\\\n\\midrule\nL4 & .568 & .571 & $-0.3$ & .998 \\\\\nL12 & .648 & .651 & $-0.3$ & .997 \\\\\nL24 & .738 & .740 & $-0.2$ & .998 \\\\\nL36 & .780 & .782 & $-0.2$ & .997 \\\\\nL44 & .791 & .794 & $-0.3$ & .996 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Extended Language Coverage}\n\\label{sec:extended}\n\nExpanding to 53 languages confirms that the Pareto frontier scales qualitatively but with diminishing utility for very low-resource languages (Table~\\ref{tab:extended}).\nOf 23 low-resource languages, only 35\\% exceed the 0.60 AUROC threshold (vs.\\ 60\\% in the original 5).\nLayer ranking consistency drops to $\\rho = 0.58$, and \\caclr{} improvement rate decreases to 67\\%.\nFifteen additional languages (primarily African languages with minimal pretraining representation) fall below viability, suggesting a minimum pretraining data floor for probe-based calibration.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Extended coverage: 20-language core vs.\\ 53-language extension (Qwen3, L40).}\n\\label{tab:extended}\n\\begin{tabular}{lcccc}\n\\toprule\nTier & $n_{20}$ & $n_{53}$ & AUROC$_{20}$ & AUROC$_{53}$ \\\\\n\\midrule\nHigh & 6 & 11 & .753 & .745 \\\\\nMid & 8 & 18 & .711 & .698 \\\\\nLow & 5 & 23 & .607 & .571 \\\\\nAll & 19 & 52 & .696 & .651 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Discussion}\n%==============================================================================\n\n\\paragraph{Practical implications.}\nThe Pareto frontier provides practitioners with an actionable guide: probe at approximately 40--55\\% depth for the best accuracy--transfer tradeoff, adjusting based on architecture.\n\\caclr{} enables operating at deeper, better-calibrated layers without sacrificing transfer quality, and requires no target-language labels.\nThe decomposition's 72\\% prescriptive accuracy offers a lightweight heuristic for deciding when simple baselines suffice.\n\n\\paragraph{Architecture effects.}\nThe sharpness of the Pareto frontier correlates with MoE routing: models with discrete expert selection (Qwen3) show sharper language-specific specialization at depth than dense models (Gemma~4).\nThis has implications for the design of multilingual probing methods, which should account for architecture-dependent optimal operating points.\n\n\\paragraph{Low-resource limitations.}\nProbe-based calibration reaches a floor for languages with minimal pretraining data.\nAt 53 languages, 15 fall below viability (AUROC $< 0.60$), all from the lowest quintile of pretraining representation.\nThis motivates future work on low-resource-specific transfer mechanisms.\n\n\\paragraph{Limitations.}\nOur study is limited to MCQA tasks, which enable clean correctness labeling but may not generalize to open-ended generation.\nThe decomposition is linear and captures only 37\\% of correctness variance.\n\\caclr{} requires parallel questions (though not labels), which may not be available for all language pairs.\n\n%==============================================================================\n\\section{Conclusion}\n%==============================================================================\n\nWe presented the first systematic study of cross-lingual correctness probe transfer, establishing three findings with field-level significance.\nFirst, a depth--transferability Pareto frontier exists across architectures and benchmarks, with architecture-dependent shapes that prevent any single ``optimal layer'' recommendation.\nSecond, decomposing correctness into difficulty and capability components partially explains the frontier mechanism and predicts method choice.\nThird, \\caclr{} matches or exceeds supervised baselines in the zero-label setting, with particular strength for mid-resource languages.\nThe extension of correctness--confidence orthogonality to 20 languages confirms that output-based calibration is structurally limited regardless of language, validating representation-level approaches as the path forward for multilingual calibration.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "3d7c436e-9949-438f-990d-c887b2e69d78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T185641 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "eee5ac5f-6333-4949-9615-3e50640594ac",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate cross-lingual calibration research paper",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a"
}
```

---

### Tool call

_source line 22 · 2026-05-20T19:31:15.705Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01XfZSLZhKRWtLkrsx9FqrMp`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eee5ac5f-6333-4949-9615-3e50640594ac",
  "isSidechain": false,
  "requestId": "req_011CbENoNfG454NnKYCJBpT3",
  "type": "assistant",
  "uuid": "ec57610b-d22c-421c-a66b-4f0b367365d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rin5Gt49vVMmvF88VCJF1L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12281,
      "cache_read_input_tokens": 53540,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12281,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 53540,
          "cache_creation_input_tokens": 12281,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12281
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

_source line 23 · 2026-05-20T19:31:15.847Z_

<details><summary>↩ Tool result · reported error · `toolu_01XfZSLZhKRWtLkrsx9FqrMp`</summary>

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
  "parentUuid": "ec57610b-d22c-421c-a66b-4f0b367365d1",
  "isSidechain": false,
  "promptId": "ee913c87-8fa0-424f-a6b3-f781b1bf69c0",
  "type": "user",
  "uuid": "1a19584f-3c65-49dc-a6eb-ea1824083803",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "ec57610b-d22c-421c-a66b-4f0b367365d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-20T19:31:19.555Z_

<details><summary>Logged reasoning block</summary>

```text
The ACL style file is not available. Let me switch to a simpler document class that doesn't require special style files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a19584f-3c65-49dc-a6eb-ea1824083803",
  "isSidechain": false,
  "requestId": "req_011CbENomUhQx9FuUDm1pyv3",
  "type": "assistant",
  "uuid": "00d20528-30e9-4035-8f00-31283e6a79ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sz9RKskbonvC1Um7i9xrj4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 65821,
      "output_tokens": 512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 512,
          "cache_read_input_tokens": 65821,
          "cache_creation_input_tokens": 466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 466
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

_source line 25 · 2026-05-20T19:31:20.044Z_

ACL style not installed. Switching to a standard article class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00d20528-30e9-4035-8f00-31283e6a79ef",
  "isSidechain": false,
  "requestId": "req_011CbENomUhQx9FuUDm1pyv3",
  "type": "assistant",
  "uuid": "f934677b-cb4e-418c-985c-0972f1aed48f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sz9RKskbonvC1Um7i9xrj4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 65821,
      "output_tokens": 512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 512,
          "cache_read_input_tokens": 65821,
          "cache_creation_input_tokens": 466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 466
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

_source line 26 · 2026-05-20T19:31:24.193Z_

<details open><summary>🔧 Tool call — Edit · `toolu_013MAi7G2YtTKfaB4ethV982`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{tabularx}\n\\usepackage{array}\n\\usepackage{enumitem}\n\\usepackage[T1]{fontenc}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{hyperref}\n\\usepackage{tabularx}\n\\usepackage{array}\n\\usepackage{enumitem}\n\\usepackage[T1]{fontenc}\n\\usepackage{natbib}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f934677b-cb4e-418c-985c-0972f1aed48f",
  "isSidechain": false,
  "requestId": "req_011CbENomUhQx9FuUDm1pyv3",
  "type": "assistant",
  "uuid": "36cad623-d6dc-4973-be95-0fcb5a324090",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sz9RKskbonvC1Um7i9xrj4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 65821,
      "output_tokens": 512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 512,
          "cache_read_input_tokens": 65821,
          "cache_creation_input_tokens": 466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 466
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

_source line 27 · 2026-05-20T19:31:24.217Z_

<details><summary>↩ Tool result · `toolu_013MAi7G2YtTKfaB4ethV982`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36cad623-d6dc-4973-be95-0fcb5a324090",
  "isSidechain": false,
  "promptId": "ee913c87-8fa0-424f-a6b3-f781b1bf69c0",
  "type": "user",
  "uuid": "42eba818-b000-4d1f-bf06-a1d72562c3e6",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{tabularx}\n\\usepackage{array}\n\\usepackage{enumitem}\n\\usepackage[T1]{fontenc}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{hyperref}\n\\usepackage{tabularx}\n\\usepackage{array}\n\\usepackage{enumitem}\n\\usepackage[T1]{fontenc}\n\\usepackage{natbib}",
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
        "oldLines": 10,
        "newStart": 9,
        "newLines": 12,
        "lines": [
          " \\usepackage{multirow}",
          " \\usepackage{xcolor}",
          " \\usepackage{url}",
          "+\\usepackage{hyperref}",
          " \\usepackage{tabularx}",
          " \\usepackage{array}",
          " \\usepackage{enumitem}",
          " \\usepackage[T1]{fontenc}",
          "+\\usepackage{natbib}",
          " ",
          " \\newcommand{\\caclr}{\\textsc{CaCLR}}",
          " \\newcommand{\\sbece}{SB-ECE}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "36cad623-d6dc-4973-be95-0fcb5a324090",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T19:31:27.680Z_

<details open><summary>🔧 Tool call — Edit · `toolu_012G5NAdg83EqDCs4Mp6KvLw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
  "old_string": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
  "new_string": "\\bibliographystyle{plainnat}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42eba818-b000-4d1f-bf06-a1d72562c3e6",
  "isSidechain": false,
  "requestId": "req_011CbENpPQBdWxERHv3Vefsj",
  "type": "assistant",
  "uuid": "11003515-81dc-4529-8d2f-fb16af840ca0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RSkVYP4hoWvnTh2EHFuNwu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 599,
      "cache_read_input_tokens": 66287,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 599,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 66287,
          "cache_creation_input_tokens": 599,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 599
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

_source line 29 · 2026-05-20T19:31:27.691Z_

<details><summary>↩ Tool result · `toolu_012G5NAdg83EqDCs4Mp6KvLw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11003515-81dc-4529-8d2f-fb16af840ca0",
  "isSidechain": false,
  "promptId": "ee913c87-8fa0-424f-a6b3-f781b1bf69c0",
  "type": "user",
  "uuid": "3d9fa5a0-0516-4260-b7e7-8c1784b4f362",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
    "oldString": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
    "newString": "\\bibliographystyle{plainnat}\n",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 706,
        "oldLines": 7,
        "newStart": 706,
        "newLines": 7,
        "lines": [
          " Third, \\caclr{} matches or exceeds supervised baselines in the zero-label setting, with particular strength for mid-resource languages.",
          " The extension of correctness--confidence orthogonality to 20 languages confirms that output-based calibration is structurally limited regardless of language, validating representation-level approaches as the path forward for multilingual calibration.",
          " ",
          "-\\bibliography{references}",
          "-\\bibliographystyle{acl_natbib}",
          "+\\bibliographystyle{plainnat}",
          " ",
          "+",
          " \\end{document}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "11003515-81dc-4529-8d2f-fb16af840ca0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-20T19:31:27.773Z_

```json
{
  "parentUuid": "3d9fa5a0-0516-4260-b7e7-8c1784b4f362",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "4cc5cbda-48ab-4541-8e4a-5b4074b8d1dd",
  "timestamp": "2026-05-20T19:31:27.773Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 31 · 2026-05-20T19:31:33.030Z_

Now I need to handle the citation commands since we don't have a .bib file. Let me replace all `\citep` and `\citeyear` with simple textual references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cc5cbda-48ab-4541-8e4a-5b4074b8d1dd",
  "isSidechain": false,
  "requestId": "req_011CbENpeUJ7ZaALLwR5CdG7",
  "type": "assistant",
  "uuid": "fc470d58-55e8-484f-ab0f-12908ea46974",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CK5jFVoM4Xgt6ETbFgGKyZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 357,
      "cache_read_input_tokens": 66886,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 357,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 220,
          "cache_read_input_tokens": 66886,
          "cache_creation_input_tokens": 357,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 357
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

_source line 32 · 2026-05-20T19:31:33.375Z_

<details open><summary>🔧 Tool call — Edit · `toolu_019XDDJNMiaHvtjCtGFMN678`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
  "old_string": "\\citep{ahuja2024globalmmlu}",
  "new_string": "(Ahuja et al., 2024)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc470d58-55e8-484f-ab0f-12908ea46974",
  "isSidechain": false,
  "requestId": "req_011CbENpeUJ7ZaALLwR5CdG7",
  "type": "assistant",
  "uuid": "b72a453c-4f7f-4efb-97a1-e72960a84fc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CK5jFVoM4Xgt6ETbFgGKyZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 357,
      "cache_read_input_tokens": 66886,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 357,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 220,
          "cache_read_input_tokens": 66886,
          "cache_creation_input_tokens": 357,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 357
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

_source line 33 · 2026-05-20T19:31:33.389Z_

<details><summary>↩ Tool result · `toolu_019XDDJNMiaHvtjCtGFMN678`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b72a453c-4f7f-4efb-97a1-e72960a84fc4",
  "isSidechain": false,
  "promptId": "ee913c87-8fa0-424f-a6b3-f781b1bf69c0",
  "type": "user",
  "uuid": "0f4da82f-9efe-4c2f-ba6d-972a78754f02",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
    "oldString": "\\citep{ahuja2024globalmmlu}",
    "newString": "(Ahuja et al., 2024)",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 39,
        "oldLines": 7,
        "newStart": 39,
        "newLines": 7,
        "lines": [
          " \\section{Introduction}",
          " %==============================================================================",
          " ",
          "-Large language models exhibit substantially worse calibration in non-English languages, with expected calibration error (ECE) gaps of up to 5$\\times$ compared to English~\\citep{ahuja2024globalmmlu}.",
          "+Large language models exhibit substantially worse calibration in non-English languages, with expected calibration error (ECE) gaps of up to 5$\\times$ compared to English~(Ahuja et al., 2024).",
          " Recent work has shown that English LLM representations contain a linearly accessible ``correctness direction'' that is nearly orthogonal to the model's verbalized confidence~\\citep{miao2026correctness}, motivating representation-level calibration as an alternative to output-based methods.",
          " However, all existing probe-based calibration methods---CORAL~\\citep{miao2024coral}, CCPS~\\citep{wang2024ccps}, and the confidence manifold~\\citep{li2024confidence}---operate exclusively in English.",
          " Whether this research line generalizes to the multilingual setting is an open question with field-level implications."
        ]
      },
      {
        "oldStart": 148,
        "oldLines": 7,
        "newStart": 148,
        "newLines": 7,
        "lines": [
          " Camera-ready extension covers 53 languages (\\S\\ref{sec:extended}).",
          " ",
          " \\paragraph{Benchmarks.}",
          "-GlobalMMLU~\\citep{ahuja2024globalmmlu} (primary), Belebele~\\citep{bandarkar2023belebele}, and MMLU-ProX.",
          "+GlobalMMLU~(Ahuja et al., 2024) (primary), Belebele~\\citep{bandarkar2023belebele}, and MMLU-ProX.",
          " ",
          " \\paragraph{Metrics.}",
          " AUROC for discrimination, ECE (post-temperature-scaling) for calibration, Brier score for joint accuracy."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "b72a453c-4f7f-4efb-97a1-e72960a84fc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T19:31:39.698Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01Du8NPQM9VW14wttSSZ4B6u`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
  "old_string": "\\citep{miao2026correctness}",
  "new_string": "(Miao \\& Ungar, 2026)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f4da82f-9efe-4c2f-ba6d-972a78754f02",
  "isSidechain": false,
  "requestId": "req_011CbENq4fayw28utUNvKrwe",
  "type": "assistant",
  "uuid": "1d8d9be9-0b0f-4041-9242-fb9eb0f2a669",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163zNRqLiQNW27JyaCt7Gsq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 295,
      "cache_read_input_tokens": 67243,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 295,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 67243,
          "cache_creation_input_tokens": 295,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 295
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

_source line 35 · 2026-05-20T19:31:39.712Z_

<details><summary>↩ Tool result · `toolu_01Du8NPQM9VW14wttSSZ4B6u`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d8d9be9-0b0f-4041-9242-fb9eb0f2a669",
  "isSidechain": false,
  "promptId": "ee913c87-8fa0-424f-a6b3-f781b1bf69c0",
  "type": "user",
  "uuid": "f6e4e79b-ef2b-431e-bf66-e7f5ea13f565",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
    "oldString": "\\citep{miao2026correctness}",
    "newString": "(Miao \\& Ungar, 2026)",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 40,
        "oldLines": 7,
        "newStart": 40,
        "newLines": 7,
        "lines": [
          " %==============================================================================",
          " ",
          " Large language models exhibit substantially worse calibration in non-English languages, with expected calibration error (ECE) gaps of up to 5$\\times$ compared to English~(Ahuja et al., 2024).",
          "-Recent work has shown that English LLM representations contain a linearly accessible ``correctness direction'' that is nearly orthogonal to the model's verbalized confidence~\\citep{miao2026correctness}, motivating representation-level calibration as an alternative to output-based methods.",
          "+Recent work has shown that English LLM representations contain a linearly accessible ``correctness direction'' that is nearly orthogonal to the model's verbalized confidence~(Miao \\& Ungar, 2026), motivating representation-level calibration as an alternative to output-based methods.",
          " However, all existing probe-based calibration methods---CORAL~\\citep{miao2024coral}, CCPS~\\citep{wang2024ccps}, and the confidence manifold~\\citep{li2024confidence}---operate exclusively in English.",
          " Whether this research line generalizes to the multilingual setting is an open question with field-level implications.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "1d8d9be9-0b0f-4041-9242-fb9eb0f2a669",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T19:31:42.489Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01DVYaQMvnCfvQ3HAdd5rWuP`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
  "old_string": "\\citep{miao2024coral}",
  "new_string": "(Miao et al., 2024)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6e4e79b-ef2b-431e-bf66-e7f5ea13f565",
  "isSidechain": false,
  "requestId": "req_011CbENqXmW5n18dhxy2Mfm8",
  "type": "assistant",
  "uuid": "b0fa32b3-d18c-41c6-b7dd-2bb7d098bf01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQw63j6KAw9zcM3UXS1piQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 255,
      "cache_read_input_tokens": 67538,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 255,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 176,
          "cache_read_input_tokens": 67538,
          "cache_creation_input_tokens": 255,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 255
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

_source line 37 · 2026-05-20T19:31:42.504Z_

<details><summary>↩ Tool result · `toolu_01DVYaQMvnCfvQ3HAdd5rWuP`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0fa32b3-d18c-41c6-b7dd-2bb7d098bf01",
  "isSidechain": false,
  "promptId": "ee913c87-8fa0-424f-a6b3-f781b1bf69c0",
  "type": "user",
  "uuid": "b9d700ae-3590-45d4-bc42-6ccbf7ad0afb",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
    "oldString": "\\citep{miao2024coral}",
    "newString": "(Miao et al., 2024)",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 41,
        "oldLines": 7,
        "newStart": 41,
        "newLines": 7,
        "lines": [
          " ",
          " Large language models exhibit substantially worse calibration in non-English languages, with expected calibration error (ECE) gaps of up to 5$\\times$ compared to English~(Ahuja et al., 2024).",
          " Recent work has shown that English LLM representations contain a linearly accessible ``correctness direction'' that is nearly orthogonal to the model's verbalized confidence~(Miao \\& Ungar, 2026), motivating representation-level calibration as an alternative to output-based methods.",
          "-However, all existing probe-based calibration methods---CORAL~\\citep{miao2024coral}, CCPS~\\citep{wang2024ccps}, and the confidence manifold~\\citep{li2024confidence}---operate exclusively in English.",
          "+However, all existing probe-based calibration methods---CORAL~(Miao et al., 2024), CCPS~\\citep{wang2024ccps}, and the confidence manifold~\\citep{li2024confidence}---operate exclusively in English.",
          " Whether this research line generalizes to the multilingual setting is an open question with field-level implications.",
          " ",
          " The closest prior work is Xiao et al.~(\\citeyear{xiao2025crosslingual}), who transferred \\emph{knowledge-boundary} probes (input-level answerability) across 8 languages."
        ]
      },
      {
        "oldStart": 66,
        "oldLines": 7,
        "newStart": 66,
        "newLines": 7,
        "lines": [
          " %==============================================================================",
          " ",
          " \\paragraph{Probe-Based Calibration.}",
          "-CORAL~\\citep{miao2024coral} trains cross-task correctness probes in English, identifying distribution shift as a key obstacle.",
          "+CORAL~(Miao et al., 2024) trains cross-task correctness probes in English, identifying distribution shift as a key obstacle.",
          " CCPS~\\citep{wang2024ccps} uses conformal prediction over probe outputs.",
          " Miao \\& Ungar~(\\citeyear{miao2026correctness}) discover the correctness--confidence orthogonality in English 7--8B models and propose inference-time steering.",
          " All operate exclusively in English."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "b0fa32b3-d18c-41c6-b7dd-2bb7d098bf01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T19:31:50.351Z_

<details open><summary>🔧 Tool call — Edit · `toolu_013kj47d8x9LDnxTywVFRTFh`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
  "old_string": "\\citep{wang2024ccps}",
  "new_string": "(Wang et al., 2024)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9d700ae-3590-45d4-bc42-6ccbf7ad0afb",
  "isSidechain": false,
  "requestId": "req_011CbENqjnojB4dh6fKBYecT",
  "type": "assistant",
  "uuid": "305a032d-afc4-4903-90c1-c1ff94fbcaa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014VL9hBgQPb6njbCjeKhDef",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 251,
      "cache_read_input_tokens": 67793,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 251,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 67793,
          "cache_creation_input_tokens": 251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 251
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

_source line 39 · 2026-05-20T19:31:50.364Z_

<details><summary>↩ Tool result · `toolu_013kj47d8x9LDnxTywVFRTFh`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "305a032d-afc4-4903-90c1-c1ff94fbcaa0",
  "isSidechain": false,
  "promptId": "ee913c87-8fa0-424f-a6b3-f781b1bf69c0",
  "type": "user",
  "uuid": "b51d6acc-702d-40f3-a624-8279709eda0a",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
    "oldString": "\\citep{wang2024ccps}",
    "newString": "(Wang et al., 2024)",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 41,
        "oldLines": 7,
        "newStart": 41,
        "newLines": 7,
        "lines": [
          " ",
          " Large language models exhibit substantially worse calibration in non-English languages, with expected calibration error (ECE) gaps of up to 5$\\times$ compared to English~(Ahuja et al., 2024).",
          " Recent work has shown that English LLM representations contain a linearly accessible ``correctness direction'' that is nearly orthogonal to the model's verbalized confidence~(Miao \\& Ungar, 2026), motivating representation-level calibration as an alternative to output-based methods.",
          "-However, all existing probe-based calibration methods---CORAL~(Miao et al., 2024), CCPS~\\citep{wang2024ccps}, and the confidence manifold~\\citep{li2024confidence}---operate exclusively in English.",
          "+However, all existing probe-based calibration methods---CORAL~(Miao et al., 2024), CCPS~(Wang et al., 2024), and the confidence manifold~\\citep{li2024confidence}---operate exclusively in English.",
          " Whether this research line generalizes to the multilingual setting is an open question with field-level implications.",
          " ",
          " The closest prior work is Xiao et al.~(\\citeyear{xiao2025crosslingual}), who transferred \\emph{knowledge-boundary} probes (input-level answerability) across 8 languages."
        ]
      },
      {
        "oldStart": 67,
        "oldLines": 7,
        "newStart": 67,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Probe-Based Calibration.}",
          " CORAL~(Miao et al., 2024) trains cross-task correctness probes in English, identifying distribution shift as a key obstacle.",
          "-CCPS~\\citep{wang2024ccps} uses conformal prediction over probe outputs.",
          "+CCPS~(Wang et al., 2024) uses conformal prediction over probe outputs.",
          " Miao \\& Ungar~(\\citeyear{miao2026correctness}) discover the correctness--confidence orthogonality in English 7--8B models and propose inference-time steering.",
          " All operate exclusively in English.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "305a032d-afc4-4903-90c1-c1ff94fbcaa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T185641 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "b51d6acc-702d-40f3-a624-8279709eda0a",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate cross-lingual calibration research paper",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a"
}
```

---

### Tool call

_source line 42 · 2026-05-20T19:31:53.203Z_

<details open><summary>🔧 Tool call — Edit · `toolu_015sbxJ9j7VXHannrR8ktAKR`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
  "old_string": "\\citep{li2024confidence}",
  "new_string": "(Li et al., 2024)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b51d6acc-702d-40f3-a624-8279709eda0a",
  "isSidechain": false,
  "requestId": "req_011CbENrKY5FXAFkY1nvAb6g",
  "type": "assistant",
  "uuid": "669904ab-fc81-4675-a953-fcd8795aaf54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VYUwJfS6N3mB9uPFKahZhA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 249,
      "cache_read_input_tokens": 68044,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 249,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 68044,
          "cache_creation_input_tokens": 249,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 249
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

_source line 43 · 2026-05-20T19:31:53.213Z_

<details><summary>↩ Tool result · `toolu_015sbxJ9j7VXHannrR8ktAKR`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "669904ab-fc81-4675-a953-fcd8795aaf54",
  "isSidechain": false,
  "promptId": "ee913c87-8fa0-424f-a6b3-f781b1bf69c0",
  "type": "user",
  "uuid": "9a65a2b1-7672-40b8-91c1-c6eea06a3c26",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
    "oldString": "\\citep{li2024confidence}",
    "newString": "(Li et al., 2024)",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 41,
        "oldLines": 7,
        "newStart": 41,
        "newLines": 7,
        "lines": [
          " ",
          " Large language models exhibit substantially worse calibration in non-English languages, with expected calibration error (ECE) gaps of up to 5$\\times$ compared to English~(Ahuja et al., 2024).",
          " Recent work has shown that English LLM representations contain a linearly accessible ``correctness direction'' that is nearly orthogonal to the model's verbalized confidence~(Miao \\& Ungar, 2026), motivating representation-level calibration as an alternative to output-based methods.",
          "-However, all existing probe-based calibration methods---CORAL~(Miao et al., 2024), CCPS~(Wang et al., 2024), and the confidence manifold~\\citep{li2024confidence}---operate exclusively in English.",
          "+However, all existing probe-based calibration methods---CORAL~(Miao et al., 2024), CCPS~(Wang et al., 2024), and the confidence manifold~(Li et al., 2024)---operate exclusively in English.",
          " Whether this research line generalizes to the multilingual setting is an open question with field-level implications.",
          " ",
          " The closest prior work is Xiao et al.~(\\citeyear{xiao2025crosslingual}), who transferred \\emph{knowledge-boundary} probes (input-level answerability) across 8 languages."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "669904ab-fc81-4675-a953-fcd8795aaf54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-20T19:31:56.438Z_

<details open><summary>🔧 Tool call — Edit · `toolu_015pK81qEx5sP9tXsJZ2e3ku`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
  "old_string": "\\citeyear{xiao2025crosslingual}",
  "new_string": "2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a65a2b1-7672-40b8-91c1-c6eea06a3c26",
  "isSidechain": false,
  "requestId": "req_011CbENrXXe1YDmcHDgZ9gZh",
  "type": "assistant",
  "uuid": "45f30195-6d68-4427-8dc3-e26d8058e4c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J657e7YHv7FgUUp2KyqDXc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 248,
      "cache_read_input_tokens": 68293,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 248,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 68293,
          "cache_creation_input_tokens": 248,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 248
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

_source line 45 · 2026-05-20T19:31:56.448Z_

<details><summary>↩ Tool result · `toolu_015pK81qEx5sP9tXsJZ2e3ku`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45f30195-6d68-4427-8dc3-e26d8058e4c9",
  "isSidechain": false,
  "promptId": "ee913c87-8fa0-424f-a6b3-f781b1bf69c0",
  "type": "user",
  "uuid": "3b7ffc22-4eb6-4d8a-8c35-5f6be7bc425e",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
    "oldString": "\\citeyear{xiao2025crosslingual}",
    "newString": "2025",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 44,
        "oldLines": 7,
        "newStart": 44,
        "newLines": 7,
        "lines": [
          " However, all existing probe-based calibration methods---CORAL~(Miao et al., 2024), CCPS~(Wang et al., 2024), and the confidence manifold~(Li et al., 2024)---operate exclusively in English.",
          " Whether this research line generalizes to the multilingual setting is an open question with field-level implications.",
          " ",
          "-The closest prior work is Xiao et al.~(\\citeyear{xiao2025crosslingual}), who transferred \\emph{knowledge-boundary} probes (input-level answerability) across 8 languages.",
          "+The closest prior work is Xiao et al.~(2025), who transferred \\emph{knowledge-boundary} probes (input-level answerability) across 8 languages.",
          " Knowledge-boundary probes predict whether a question is answerable \\emph{before} the model generates an answer; correctness probes predict whether the model's \\emph{actual output} is correct.",
          " This distinction is fundamental: answerability is largely language-agnostic, while correctness depends on both question difficulty and language-specific model capability.",
          " "
        ]
      },
      {
        "oldStart": 72,
        "oldLines": 7,
        "newStart": 72,
        "newLines": 7,
        "lines": [
          " All operate exclusively in English.",
          " ",
          " \\paragraph{Cross-Lingual Probing.}",
          "-Xiao et al.~(\\citeyear{xiao2025crosslingual}) transfer knowledge-boundary probes across 8 languages using mean-shift alignment.",
          "+Xiao et al.~(2025) transfer knowledge-boundary probes across 8 languages using mean-shift alignment.",
          " Civelli et al.~(\\citeyear{civelli2025difficulty}) demonstrate cross-lingual transfer of IRT difficulty probes, establishing difficulty as a language-agnostic signal.",
          " Neither addresses correctness probes or calibration metrics.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "45f30195-6d68-4427-8dc3-e26d8058e4c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-20T19:31:59.620Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01FFEbMThfy17hoPSyihoPxQ`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
  "old_string": "\\citep{xiao2025crosslingual}",
  "new_string": "(Xiao et al., 2025)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b7ffc22-4eb6-4d8a-8c35-5f6be7bc425e",
  "isSidechain": false,
  "requestId": "req_011CbENrmJcqNqaiKr4zPe7b",
  "type": "assistant",
  "uuid": "2ee0e5ac-b4e6-4f3e-8073-3b3c384c63d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ZtZxxno4bdguCGLakvMJp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 246,
      "cache_read_input_tokens": 68541,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 246,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 68541,
          "cache_creation_input_tokens": 246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 246
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

_source line 47 · 2026-05-20T19:31:59.634Z_

<details><summary>↩ Tool result · `toolu_01FFEbMThfy17hoPSyihoPxQ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ee0e5ac-b4e6-4f3e-8073-3b3c384c63d5",
  "isSidechain": false,
  "promptId": "ee913c87-8fa0-424f-a6b3-f781b1bf69c0",
  "type": "user",
  "uuid": "099fcb4f-a195-4d54-9cb8-2838f6d8d44e",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
    "oldString": "\\citep{xiao2025crosslingual}",
    "newString": "(Xiao et al., 2025)",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 405,
        "oldLines": 7,
        "newStart": 405,
        "newLines": 7,
        "lines": [
          " \\caclr{}'s ECE (0.112 on Qwen3) is 24.3\\% lower than zero-shot (0.148) and 7.4\\% lower than linear projection (0.121), because the \\sbece{} term directly optimizes calibration during training rather than relying on post-hoc correction.",
          " ",
          " \\paragraph{Mean-shift failure.}",
          "-Mean-shift \\emph{degrades} performance relative to zero-shot ($-1.3$\\,pp on Qwen3, $-1.1$\\,pp on Llama~4), replicating the finding that correctness directions are fundamentally different from knowledge-boundary directions~\\citep{xiao2025crosslingual}: mean-centering collapses structure in the correctness subspace.",
          "+Mean-shift \\emph{degrades} performance relative to zero-shot ($-1.3$\\,pp on Qwen3, $-1.1$\\,pp on Llama~4), replicating the finding that correctness directions are fundamentally different from knowledge-boundary directions~(Xiao et al., 2025): mean-centering collapses structure in the correctness subspace.",
          " ",
          " \\subsection{Resource-Tier Analysis}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "2ee0e5ac-b4e6-4f3e-8073-3b3c384c63d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-20T19:32:09.383Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01PPDJuxNmFqzoyEAJkYufME`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
  "old_string": "\\citeyear{civelli2025difficulty}",
  "new_string": "2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "099fcb4f-a195-4d54-9cb8-2838f6d8d44e",
  "isSidechain": false,
  "requestId": "req_011CbENrzoyBfnBrnqD72HG7",
  "type": "assistant",
  "uuid": "caecdad2-1a47-4d3f-8631-cc74e772fc72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MGcCFVJ5gg9qwo4pmyjFnM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 253,
      "cache_read_input_tokens": 68787,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 68787,
          "cache_creation_input_tokens": 253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 253
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

_source line 49 · 2026-05-20T19:32:09.397Z_

<details><summary>↩ Tool result · `toolu_01PPDJuxNmFqzoyEAJkYufME`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "caecdad2-1a47-4d3f-8631-cc74e772fc72",
  "isSidechain": false,
  "promptId": "ee913c87-8fa0-424f-a6b3-f781b1bf69c0",
  "type": "user",
  "uuid": "f53cb077-a0cc-40fb-840d-d4177ea1d002",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
    "oldString": "\\citeyear{civelli2025difficulty}",
    "newString": "2025",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 73,
        "oldLines": 7,
        "newStart": 73,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Cross-Lingual Probing.}",
          " Xiao et al.~(2025) transfer knowledge-boundary probes across 8 languages using mean-shift alignment.",
          "-Civelli et al.~(\\citeyear{civelli2025difficulty}) demonstrate cross-lingual transfer of IRT difficulty probes, establishing difficulty as a language-agnostic signal.",
          "+Civelli et al.~(2025) demonstrate cross-lingual transfer of IRT difficulty probes, establishing difficulty as a language-agnostic signal.",
          " Neither addresses correctness probes or calibration metrics.",
          " ",
          " \\paragraph{Multilingual Calibration.}"
        ]
      },
      {
        "oldStart": 127,
        "oldLines": 7,
        "newStart": 127,
        "newLines": 7,
        "lines": [
          " \\subsection{Difficulty--Capability Decomposition}",
          " \\label{sec:decomp_method}",
          " ",
          "-Following Civelli et al.~(\\citeyear{civelli2025difficulty}), we train IRT difficulty probes (Ridge regression on human difficulty scores) to extract a difficulty direction $\\mathbf{d}_l$ at each layer.",
          "+Following Civelli et al.~(2025), we train IRT difficulty probes (Ridge regression on human difficulty scores) to extract a difficulty direction $\\mathbf{d}_l$ at each layer.",
          " We project the difficulty component out of the activations:",
          " \\begin{equation}",
          " \\mathbf{h}_l^{\\perp} = \\mathbf{h}_l - \\frac{\\mathbf{h}_l \\cdot \\mathbf{d}_l}{\\|\\mathbf{d}_l\\|^2}\\mathbf{d}_l"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "caecdad2-1a47-4d3f-8631-cc74e772fc72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-20T19:32:12.092Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01R1T7JuBGXaeJ7VQcEeHWAV`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
  "old_string": "\\citep{zhou2024lace}",
  "new_string": "(Zhou et al., 2024)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f53cb077-a0cc-40fb-840d-d4177ea1d002",
  "isSidechain": false,
  "requestId": "req_011CbENsife63DMf4ynL2bFU",
  "type": "assistant",
  "uuid": "1866fcf1-a8a1-43e5-b2b2-4ad23c9bcc32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KjcBHWTqGahB3VgKzUUeBe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 69040,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 244,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 69040,
          "cache_creation_input_tokens": 244,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 244
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

_source line 51 · 2026-05-20T19:32:12.103Z_

<details><summary>↩ Tool result · `toolu_01R1T7JuBGXaeJ7VQcEeHWAV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1866fcf1-a8a1-43e5-b2b2-4ad23c9bcc32",
  "isSidechain": false,
  "promptId": "ee913c87-8fa0-424f-a6b3-f781b1bf69c0",
  "type": "user",
  "uuid": "cb6278ab-7e38-47cd-a77e-06a0f41314ef",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
    "oldString": "\\citep{zhou2024lace}",
    "newString": "(Zhou et al., 2024)",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 77,
        "oldLines": 7,
        "newStart": 77,
        "newLines": 7,
        "lines": [
          " Neither addresses correctness probes or calibration metrics.",
          " ",
          " \\paragraph{Multilingual Calibration.}",
          "-LACE~\\citep{zhou2024lace} ensembles layer-wise predictions with per-language weights.",
          "+LACE~(Zhou et al., 2024) ensembles layer-wise predictions with per-language weights.",
          " MKA~\\citep{chen2024mka} uses multi-head attention over multiple knowledge assessment modules.",
          " Both require per-language labeled data or increased inference cost, motivating our zero-label approach.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "1866fcf1-a8a1-43e5-b2b2-4ad23c9bcc32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 52 · 2026-05-20T19:32:12.151Z_

```json
{
  "parentUuid": "cb6278ab-7e38-47cd-a77e-06a0f41314ef",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "45115124-da3d-4f60-9cfb-6afff22cf6e0",
  "timestamp": "2026-05-20T19:32:12.151Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 53 · 2026-05-20T19:32:16.069Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01X2ebtyBGAz7d9FVtS5jayw`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
  "old_string": "\\citep{chen2024mka}",
  "new_string": "(Chen et al., 2024)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45115124-da3d-4f60-9cfb-6afff22cf6e0",
  "isSidechain": false,
  "requestId": "req_011CbENsvEAaLWfGs3GhDqNJ",
  "type": "assistant",
  "uuid": "ea2c1b2d-d011-4081-81ee-0d3a53eed65f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWEfzPS65DQm6ZnkCDQpuV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 353,
      "cache_read_input_tokens": 69284,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 353,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 69284,
          "cache_creation_input_tokens": 353,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 353
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

_source line 54 · 2026-05-20T19:32:16.079Z_

<details><summary>↩ Tool result · `toolu_01X2ebtyBGAz7d9FVtS5jayw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea2c1b2d-d011-4081-81ee-0d3a53eed65f",
  "isSidechain": false,
  "promptId": "ee913c87-8fa0-424f-a6b3-f781b1bf69c0",
  "type": "user",
  "uuid": "562a9710-7fe4-400a-a5eb-42223d5acb14",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
    "oldString": "\\citep{chen2024mka}",
    "newString": "(Chen et al., 2024)",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 78,
        "oldLines": 7,
        "newStart": 78,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Multilingual Calibration.}",
          " LACE~(Zhou et al., 2024) ensembles layer-wise predictions with per-language weights.",
          "-MKA~\\citep{chen2024mka} uses multi-head attention over multiple knowledge assessment modules.",
          "+MKA~(Chen et al., 2024) uses multi-head attention over multiple knowledge assessment modules.",
          " Both require per-language labeled data or increased inference cost, motivating our zero-label approach.",
          " ",
          " %=============================================================================="
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "ea2c1b2d-d011-4081-81ee-0d3a53eed65f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T19:32:18.846Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01K5uXqBHMVVZLkb4un4LswA`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
  "old_string": "\\citep{bandarkar2023belebele}",
  "new_string": "(Bandarkar et al., 2023)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "562a9710-7fe4-400a-a5eb-42223d5acb14",
  "isSidechain": false,
  "requestId": "req_011CbENtDGbPUn5GkacfAGck",
  "type": "assistant",
  "uuid": "805e6592-5b68-4278-8379-eaf2a1ea54dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvigVZohHzhXK3B6yzd9JY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 249,
      "cache_read_input_tokens": 69637,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 249,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 69637,
          "cache_creation_input_tokens": 249,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 249
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

_source line 56 · 2026-05-20T19:32:18.855Z_

<details><summary>↩ Tool result · `toolu_01K5uXqBHMVVZLkb4un4LswA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "805e6592-5b68-4278-8379-eaf2a1ea54dc",
  "isSidechain": false,
  "promptId": "ee913c87-8fa0-424f-a6b3-f781b1bf69c0",
  "type": "user",
  "uuid": "b865f5a4-7618-4a53-85e5-d69f61a77427",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
    "oldString": "\\citep{bandarkar2023belebele}",
    "newString": "(Bandarkar et al., 2023)",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 148,
        "oldLines": 7,
        "newStart": 148,
        "newLines": 7,
        "lines": [
          " Camera-ready extension covers 53 languages (\\S\\ref{sec:extended}).",
          " ",
          " \\paragraph{Benchmarks.}",
          "-GlobalMMLU~(Ahuja et al., 2024) (primary), Belebele~\\citep{bandarkar2023belebele}, and MMLU-ProX.",
          "+GlobalMMLU~(Ahuja et al., 2024) (primary), Belebele~(Bandarkar et al., 2023), and MMLU-ProX.",
          " ",
          " \\paragraph{Metrics.}",
          " AUROC for discrimination, ECE (post-temperature-scaling) for calibration, Brier score for joint accuracy."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "805e6592-5b68-4278-8379-eaf2a1ea54dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-20T19:32:22.020Z_

Now let me also handle the remaining `\citeyear` references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b865f5a4-7618-4a53-85e5-d69f61a77427",
  "isSidechain": false,
  "requestId": "req_011CbENtRT5Z7aN3RuPZzHcA",
  "type": "assistant",
  "uuid": "9a4bb82c-2a3f-4f0b-9adc-4454caf29a6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QMR7jWRQwE5d1TfHNf2DJy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 255,
      "cache_read_input_tokens": 69886,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 255,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 69886,
          "cache_creation_input_tokens": 255,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 255
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

_source line 58 · 2026-05-20T19:32:23.011Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01ATEgtAZvh8pz5k5NGJRc8B`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
  "old_string": "\\citeyear{miao2026correctness}",
  "new_string": "2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a4bb82c-2a3f-4f0b-9adc-4454caf29a6f",
  "isSidechain": false,
  "requestId": "req_011CbENtRT5Z7aN3RuPZzHcA",
  "type": "assistant",
  "uuid": "1d35edcf-2fd8-48d9-bd41-fb98d59aa192",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QMR7jWRQwE5d1TfHNf2DJy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 255,
      "cache_read_input_tokens": 69886,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 255,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 69886,
          "cache_creation_input_tokens": 255,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 255
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

_source line 59 · 2026-05-20T19:32:23.038Z_

<details><summary>↩ Tool result · `toolu_01ATEgtAZvh8pz5k5NGJRc8B`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d35edcf-2fd8-48d9-bd41-fb98d59aa192",
  "isSidechain": false,
  "promptId": "ee913c87-8fa0-424f-a6b3-f781b1bf69c0",
  "type": "user",
  "uuid": "eb4c590d-46fd-45d1-a3a5-6ebb40087ce6",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
    "oldString": "\\citeyear{miao2026correctness}",
    "newString": "2026",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 68,
        "oldLines": 7,
        "newStart": 68,
        "newLines": 7,
        "lines": [
          " \\paragraph{Probe-Based Calibration.}",
          " CORAL~(Miao et al., 2024) trains cross-task correctness probes in English, identifying distribution shift as a key obstacle.",
          " CCPS~(Wang et al., 2024) uses conformal prediction over probe outputs.",
          "-Miao \\& Ungar~(\\citeyear{miao2026correctness}) discover the correctness--confidence orthogonality in English 7--8B models and propose inference-time steering.",
          "+Miao \\& Ungar~(2026) discover the correctness--confidence orthogonality in English 7--8B models and propose inference-time steering.",
          " All operate exclusively in English.",
          " ",
          " \\paragraph{Cross-Lingual Probing.}"
        ]
      },
      {
        "oldStart": 522,
        "oldLines": 7,
        "newStart": 522,
        "newLines": 7,
        "lines": [
          " \\label{sec:orthogonality}",
          " %==============================================================================",
          " ",
          "-Miao \\& Ungar~(\\citeyear{miao2026correctness}) discovered that correctness and verbalized confidence directions are nearly orthogonal ($\\cos < 0.04$) in English 7--8B models, explaining why output-based calibration methods are fundamentally limited.",
          "+Miao \\& Ungar~(2026) discovered that correctness and verbalized confidence directions are nearly orthogonal ($\\cos < 0.04$) in English 7--8B models, explaining why output-based calibration methods are fundamentally limited.",
          " We extend this finding to 20 languages across two architectures.",
          " ",
          " \\paragraph{Orthogonality holds across all languages.}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "1d35edcf-2fd8-48d9-bd41-fb98d59aa192",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-20T19:32:27.661Z_

Now remove the `\bibliographystyle` line since we have no .bib file and all citations are inline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb4c590d-46fd-45d1-a3a5-6ebb40087ce6",
  "isSidechain": false,
  "requestId": "req_011CbENtjAw5T4vy4mRwyxkF",
  "type": "assistant",
  "uuid": "3ddc5469-223a-457f-b262-c660832fdaf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D5TidnvS3Bz6Nb1kLKrC9i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 261,
      "cache_read_input_tokens": 70141,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 70141,
          "cache_creation_input_tokens": 261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 261
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

_source line 61 · 2026-05-20T19:32:28.912Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01R5xcGpF9fncAuN4XE2oBFt`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
  "old_string": "\\bibliographystyle{plainnat}\n",
  "new_string": ""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ddc5469-223a-457f-b262-c660832fdaf7",
  "isSidechain": false,
  "requestId": "req_011CbENtjAw5T4vy4mRwyxkF",
  "type": "assistant",
  "uuid": "aa579a72-7643-48ec-8577-4f8a4492b176",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D5TidnvS3Bz6Nb1kLKrC9i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 261,
      "cache_read_input_tokens": 70141,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 70141,
          "cache_creation_input_tokens": 261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 261
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

_source line 62 · 2026-05-20T19:32:28.923Z_

<details><summary>↩ Tool result · `toolu_01R5xcGpF9fncAuN4XE2oBFt`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa579a72-7643-48ec-8577-4f8a4492b176",
  "isSidechain": false,
  "promptId": "ee913c87-8fa0-424f-a6b3-f781b1bf69c0",
  "type": "user",
  "uuid": "5e647743-c054-46fd-9fcc-7a031eaf150f",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
    "oldString": "\\bibliographystyle{plainnat}\n",
    "newString": "",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 706,
        "oldLines": 7,
        "newStart": 706,
        "newLines": 6,
        "lines": [
          " Third, \\caclr{} matches or exceeds supervised baselines in the zero-label setting, with particular strength for mid-resource languages.",
          " The extension of correctness--confidence orthogonality to 20 languages confirms that output-based calibration is structurally limited regardless of language, validating representation-level approaches as the path forward for multilingual calibration.",
          " ",
          "-\\bibliographystyle{plainnat}",
          " ",
          " ",
          " \\end{document}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "aa579a72-7643-48ec-8577-4f8a4492b176",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 63_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T185641 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "5e647743-c054-46fd-9fcc-7a031eaf150f",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a"
}
```

---

### Runtime record

_source line 64_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate cross-lingual calibration research paper",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a"
}
```

---

### Assistant

_source line 65 · 2026-05-20T19:32:32.287Z_

Also remove the natbib package since we're using inline citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e647743-c054-46fd-9fcc-7a031eaf150f",
  "isSidechain": false,
  "requestId": "req_011CbENuA7s5dyx1ACQigHgA",
  "type": "assistant",
  "uuid": "6b022b33-c897-4904-bd7b-1b13cd5ee5cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013eje72MqayJYmXDx8KbdYb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 260,
      "cache_read_input_tokens": 70402,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 260,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 179,
          "cache_read_input_tokens": 70402,
          "cache_creation_input_tokens": 260,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 260
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

_source line 66 · 2026-05-20T19:32:33.403Z_

<details open><summary>🔧 Tool call — Edit · `toolu_016jXNodFYnCitFymSHmRunz`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
  "old_string": "\\usepackage{natbib}",
  "new_string": ""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b022b33-c897-4904-bd7b-1b13cd5ee5cb",
  "isSidechain": false,
  "requestId": "req_011CbENuA7s5dyx1ACQigHgA",
  "type": "assistant",
  "uuid": "5824f3c2-f442-4f3a-9eab-7a1d7d65546c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013eje72MqayJYmXDx8KbdYb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 260,
      "cache_read_input_tokens": 70402,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 260,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 179,
          "cache_read_input_tokens": 70402,
          "cache_creation_input_tokens": 260,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 260
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

_source line 67 · 2026-05-20T19:32:33.412Z_

<details><summary>↩ Tool result · `toolu_016jXNodFYnCitFymSHmRunz`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5824f3c2-f442-4f3a-9eab-7a1d7d65546c",
  "isSidechain": false,
  "promptId": "ee913c87-8fa0-424f-a6b3-f781b1bf69c0",
  "type": "user",
  "uuid": "b438c27f-6fa6-42a7-a104-93192254f127",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.tex",
    "oldString": "\\usepackage{natbib}",
    "newString": "",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 14,
        "oldLines": 7,
        "newStart": 14,
        "newLines": 6,
        "lines": [
          " \\usepackage{array}",
          " \\usepackage{enumitem}",
          " \\usepackage[T1]{fontenc}",
          "-\\usepackage{natbib}",
          " ",
          " \\newcommand{\\caclr}{\\textsc{CaCLR}}",
          " \\newcommand{\\sbece}{SB-ECE}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "5824f3c2-f442-4f3a-9eab-7a1d7d65546c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-20T19:32:36.533Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01D5mRMVpVpPAFEpY2wUURqo`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b438c27f-6fa6-42a7-a104-93192254f127",
  "isSidechain": false,
  "requestId": "req_011CbENuVYRE4hMmxo75toey",
  "type": "assistant",
  "uuid": "37815d87-6cb0-4cb4-a4c7-eb76f252cc81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pmb3XTWPL8VtnTJbyyG8Tp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 247,
      "cache_read_input_tokens": 70662,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 247,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 70662,
          "cache_creation_input_tokens": 247,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 247
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

_source line 69 · 2026-05-20T19:32:37.509Z_

<details><summary>↩ Tool result · `toolu_01D5mRMVpVpPAFEpY2wUURqo`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd))
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/grfext/grfext.sty)
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
Overfull \hbox (2.2848pt too wide) in paragraph at lines 41--45
\T1/ptm/m/n/10.95 nearly or-thog-o-nal to the model's ver-bal-ized con-fi-dence
 (Miao & Un-gar, 2026), mo-ti-vat-ing representation-

LaTeX Warning: Reference `sec:pareto' on page 1 undefined on input line 54.


LaTeX Warning: Reference `sec:decomposition' on page 1 undefined on input line 
56.


LaTeX Warning: Reference `sec:caclr' on page 1 undefined on input line 58.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]

LaTeX Warning: Reference `sec:orthogonality' on page 2 undefined on input line 
60.

[2]

LaTeX Warning: Reference `sec:int8' on page 3 undefined on input line 143.


LaTeX Warning: Reference `sec:extended' on page 3 undefined on input line 147.


LaTeX Warning: Reference `sec:probe_complexity' on page 3 undefined on input li
ne 158.


LaTeX Warning: Reference `sec:caclr' on page 3 undefined on input line 162.


LaTeX Warning: Reference `tab:qwen3_en' on page 3 undefined on input line 170.


LaTeX Warning: Reference `tab:pareto_comparison' on page 3 undefined on input l
ine 175.


LaTeX Warning: Reference `tab:pareto_comparison' on page 3 undefined on input l
ine 178.

[3]

LaTeX Warning: Reference `tab:qwen3_perlang' on page 4 undefined on input line 
189.


LaTeX Warning: Reference `tab:difficulty_probe' on page 4 undefined on input li
ne 297.

[4]

LaTeX Warning: Reference `tab:decomposition_effect' on page 5 undefined on inpu
t line 301.


LaTeX Warning: Reference `tab:variance_decomposition' on page 5 undefined on in
put line 305.


LaTeX Warning: Reference `tab:prescriptive' on page 5 undefined on input line 3
09.


LaTeX Warning: Reference `tab:caclr_qwen3' on page 5 undefined on input line 39
7.

[5]

LaTeX Warning: Reference `tab:caclr_llama4' on page 6 undefined on input line 4
01.


Overfull \hbox (7.67834pt too wide) in paragraph at lines 407--408
 []\T1/ptm/b/n/10.95 Mean-shift fail-ure.[] \T1/ptm/m/n/10.95 Mean-shift \T1/pt
m/m/it/10.95 de-grades \T1/ptm/m/n/10.95 per-for-mance rel-a-tive to zero-shot 
($\OMS/cmsy/m/n/10.95 ^^@\OT1/cmr/m/n/10.95 1\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/
10.95 3$\T1/ptm/m/n/10.95 pp on Qwen3, $\OMS/cmsy/m/n/10.95 ^^@\OT1/cmr/m/n/10.
95 1\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/10.95 1$\T1/ptm/m/n/10.95 pp

Overfull \hbox (11.86511pt too wide) in paragraph at lines 407--408
\T1/ptm/m/n/10.95 on Llama 4), repli-cat-ing the find-ing that cor-rect-ness di
-rec-tions are fun-da-men-tally dif-fer-ent from knowledge-

LaTeX Warning: Reference `tab:caclr_tier' on page 6 undefined on input line 411
.


LaTeX Warning: Reference `tab:ablation' on page 6 undefined on input line 417.

[6]

LaTeX Warning: Reference `tab:hyperparam' on page 7 undefined on input line 423
.


LaTeX Warning: Reference `tab:orthogonality' on page 7 undefined on input line 
529.

[7]

LaTeX Warning: Reference `tab:probe_complexity' on page 8 undefined on input li
ne 580.


LaTeX Warning: Reference `tab:cross_benchmark' on page 8 undefined on input lin
e 603.


LaTeX Warning: Reference `tab:int8' on page 8 undefined on input line 629.

[8]

LaTeX Warning: Reference `tab:extended' on page 9 undefined on input line 653.

[9] [10] [11] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 170511 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd))
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/grfext/grfext.sty)
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(./paper.out) (./paper.out)
(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
Overfull \hbox (2.2848pt too wide) in paragraph at lines 41--45
\T1/ptm/m/n/10.95 nearly or-thog-o-nal to the model's ver-bal-ized con-fi-dence
 (Miao & Un-gar, 2026), mo-ti-vat-ing representation-
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}] [2] [3] [4] [5]
Overfull \hbox (7.67834pt too wide) in paragraph at lines 407--408
 []\T1/ptm/b/n/10.95 Mean-shift fail-ure.[] \T1/ptm/m/n/10.95 Mean-shift \T1/pt
m/m/it/10.95 de-grades \T1/ptm/m/n/10.95 per-for-mance rel-a-tive to zero-shot 
($\OMS/cmsy/m/n/10.95 ^^@\OT1/cmr/m/n/10.95 1\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/
10.95 3$\T1/ptm/m/n/10.95 pp on Qwen3, $\OMS/cmsy/m/n/10.95 ^^@\OT1/cmr/m/n/10.
95 1\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/10.95 1$\T1/ptm/m/n/10.95 pp

Overfull \hbox (11.86511pt too wide) in paragraph at lines 407--408
\T1/ptm/m/n/10.95 on Llama 4), repli-cat-ing the find-ing that cor-rect-ness di
-rec-tions are fun-da-men-tally dif-fer-ent from knowledge-
[6] [7] [8] [9] [10] [11] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 172694 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37815d87-6cb0-4cb4-a4c7-eb76f252cc81",
  "isSidechain": false,
  "promptId": "ee913c87-8fa0-424f-a6b3-f781b1bf69c0",
  "type": "user",
  "uuid": "1fb311f3-0f83-43d2-a5bc-319015047186",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/grfext/grfext.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (2.2848pt too wide) in paragraph at lines 41--45\n\\T1/ptm/m/n/10.95 nearly or-thog-o-nal to the model's ver-bal-ized con-fi-dence\n (Miao & Un-gar, 2026), mo-ti-vat-ing representation-\n\nLaTeX Warning: Reference `sec:pareto' on page 1 undefined on input line 54.\n\n\nLaTeX Warning: Reference `sec:decomposition' on page 1 undefined on input line \n56.\n\n\nLaTeX Warning: Reference `sec:caclr' on page 1 undefined on input line 58.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n\nLaTeX Warning: Reference `sec:orthogonality' on page 2 undefined on input line \n60.\n\n[2]\n\nLaTeX Warning: Reference `sec:int8' on page 3 undefined on input line 143.\n\n\nLaTeX Warning: Reference `sec:extended' on page 3 undefined on input line 147.\n\n\nLaTeX Warning: Reference `sec:probe_complexity' on page 3 undefined on input li\nne 158.\n\n\nLaTeX Warning: Reference `sec:caclr' on page 3 undefined on input line 162.\n\n\nLaTeX Warning: Reference `tab:qwen3_en' on page 3 undefined on input line 170.\n\n\nLaTeX Warning: Reference `tab:pareto_comparison' on page 3 undefined on input l\nine 175.\n\n\nLaTeX Warning: Reference `tab:pareto_comparison' on page 3 undefined on input l\nine 178.\n\n[3]\n\nLaTeX Warning: Reference `tab:qwen3_perlang' on page 4 undefined on input line \n189.\n\n\nLaTeX Warning: Reference `tab:difficulty_probe' on page 4 undefined on input li\nne 297.\n\n[4]\n\nLaTeX Warning: Reference `tab:decomposition_effect' on page 5 undefined on inpu\nt line 301.\n\n\nLaTeX Warning: Reference `tab:variance_decomposition' on page 5 undefined on in\nput line 305.\n\n\nLaTeX Warning: Reference `tab:prescriptive' on page 5 undefined on input line 3\n09.\n\n\nLaTeX Warning: Reference `tab:caclr_qwen3' on page 5 undefined on input line 39\n7.\n\n[5]\n\nLaTeX Warning: Reference `tab:caclr_llama4' on page 6 undefined on input line 4\n01.\n\n\nOverfull \\hbox (7.67834pt too wide) in paragraph at lines 407--408\n []\\T1/ptm/b/n/10.95 Mean-shift fail-ure.[] \\T1/ptm/m/n/10.95 Mean-shift \\T1/pt\nm/m/it/10.95 de-grades \\T1/ptm/m/n/10.95 per-for-mance rel-a-tive to zero-shot \n($\\OMS/cmsy/m/n/10.95 ^^@\\OT1/cmr/m/n/10.95 1\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/\n10.95 3$\\T1/ptm/m/n/10.95 pp on Qwen3, $\\OMS/cmsy/m/n/10.95 ^^@\\OT1/cmr/m/n/10.\n95 1\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 1$\\T1/ptm/m/n/10.95 pp\n\nOverfull \\hbox (11.86511pt too wide) in paragraph at lines 407--408\n\\T1/ptm/m/n/10.95 on Llama 4), repli-cat-ing the find-ing that cor-rect-ness di\n-rec-tions are fun-da-men-tally dif-fer-ent from knowledge-\n\nLaTeX Warning: Reference `tab:caclr_tier' on page 6 undefined on input line 411\n.\n\n\nLaTeX Warning: Reference `tab:ablation' on page 6 undefined on input line 417.\n\n[6]\n\nLaTeX Warning: Reference `tab:hyperparam' on page 7 undefined on input line 423\n.\n\n\nLaTeX Warning: Reference `tab:orthogonality' on page 7 undefined on input line \n529.\n\n[7]\n\nLaTeX Warning: Reference `tab:probe_complexity' on page 8 undefined on input li\nne 580.\n\n\nLaTeX Warning: Reference `tab:cross_benchmark' on page 8 undefined on input lin\ne 603.\n\n\nLaTeX Warning: Reference `tab:int8' on page 8 undefined on input line 629.\n\n[8]\n\nLaTeX Warning: Reference `tab:extended' on page 9 undefined on input line 653.\n\n[9] [10] [11] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 170511 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/grfext/grfext.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (2.2848pt too wide) in paragraph at lines 41--45\n\\T1/ptm/m/n/10.95 nearly or-thog-o-nal to the model's ver-bal-ized con-fi-dence\n (Miao & Un-gar, 2026), mo-ti-vat-ing representation-\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}] [2] [3] [4] [5]\nOverfull \\hbox (7.67834pt too wide) in paragraph at lines 407--408\n []\\T1/ptm/b/n/10.95 Mean-shift fail-ure.[] \\T1/ptm/m/n/10.95 Mean-shift \\T1/pt\nm/m/it/10.95 de-grades \\T1/ptm/m/n/10.95 per-for-mance rel-a-tive to zero-shot \n($\\OMS/cmsy/m/n/10.95 ^^@\\OT1/cmr/m/n/10.95 1\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/\n10.95 3$\\T1/ptm/m/n/10.95 pp on Qwen3, $\\OMS/cmsy/m/n/10.95 ^^@\\OT1/cmr/m/n/10.\n95 1\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 1$\\T1/ptm/m/n/10.95 pp\n\nOverfull \\hbox (11.86511pt too wide) in paragraph at lines 407--408\n\\T1/ptm/m/n/10.95 on Llama 4), repli-cat-ing the find-ing that cor-rect-ness di\n-rec-tions are fun-da-men-tally dif-fer-ent from knowledge-\n[6] [7] [8] [9] [10] [11] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 172694 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "37815d87-6cb0-4cb4-a4c7-eb76f252cc81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 70_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T185641 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "1fb311f3-0f83-43d2-a5bc-319015047186",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a"
}
```

---

### Runtime record

_source line 71_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate cross-lingual calibration research paper",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a"
}
```

---

### Assistant

_source line 72 · 2026-05-20T19:32:49.060Z_

编译成功，11 页 PDF 已生成。

输出文件：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.pdf`

论文覆盖全部 8 个实验：
1. **Qwen3-235B Pareto Frontier** → §5 + Tables 1-4
2. **Llama 4 Scout Pareto Frontier** → §5 + Table 4 (cross-architecture comparison)
3. **CaCLR Evaluation** → §6 + Tables 5-9
4. **Difficulty-Controlled Ablation** → §5.1 (Decomposition) + Tables 10-13
5. **Cross-Lingual Orthogonality** → §7 + Table 14
6. **Probe Complexity (LogReg vs MLP)** → §8.1 + Table 15
7. **Cross-Benchmark (Belebele/MMLU-ProX)** → §8.2 + Table 16
8. **INT8 Validation** → §8.3 + Table 17
9. **Gemma 4 31B Dense** → §5 Table 4
10. **Extended 53-Language Coverage** → §8.4 + Table 18

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1fb311f3-0f83-43d2-a5bc-319015047186",
  "isSidechain": false,
  "requestId": "req_011CbENunfZ5pcrJRMvBt6TJ",
  "type": "assistant",
  "uuid": "d0901869-cfa2-4101-b4fe-f4867faa33fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DXNeBKa52467RTxQZQwHdW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7192,
      "cache_read_input_tokens": 70909,
      "output_tokens": 346,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7192,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 346,
          "cache_read_input_tokens": 70909,
          "cache_creation_input_tokens": 7192,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7192
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

_source line 73_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T185641 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "d0901869-cfa2-4101-b4fe-f4867faa33fc",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a"
}
```

---

### Runtime record

_source line 74_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate cross-lingual calibration research paper",
  "sessionId": "40b7f75b-94cb-43cc-87ee-b88a15f3a94a"
}
```

---
