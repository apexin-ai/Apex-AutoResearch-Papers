# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T162530 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/c4732633-03f2-4c45-a505-c2eda85a35f3.jsonl`
- **Structured JSON:** [`dc4ffaaee4090c397e23.json`](../../sessions/dc/dc4ffaaee4090c397e23.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T16:50:06.559Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T16:50:06.559Z",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T162530 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Claim 1 降级为 \"tends to help\"：embedding mining 方向正确但 effect size 缩水约 50%， 多 seed CI 宽（2–4pp），个别 seed delta < 0.5pp。BM25 baseline 方向一致（harm）但 delta 小且 p > 0.05，CoCoHaNeRe correction 论证从 \"empirically verified\" 改为 \"BM25 proxy 方向一致但 effect size 不足以排除混杂\"。Claim 2 降级为 exploratory observation：dataflow 在 Qwen 上 CI 包含 0，StarCoder 上方向为负，合并进 Claim 1 作为 strategy-encoder interaction case。SWE-bench delta < 1pp 且 CI 包含 0， 无法作为独立 evidence。论文重心移向 systematic empirical comparison + representation geometry analysis。标题用 \"Systematic Study\"，定位 analysis paper。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T16:50:06.562Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T16:50:06.562Z",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3"
}
```

---

## Round 1

26 recorded events

### User

_source line 3 · 2026-05-14T16:50:06.581Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T162530 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Claim 1 降级为 "tends to help"：embedding mining 方向正确但 effect size 缩水约 50%， 多 seed CI 宽（2–4pp），个别 seed delta < 0.5pp。BM25 baseline 方向一致（harm）但 delta 小且 p > 0.05，CoCoHaNeRe correction 论证从 "empirically verified" 改为 "BM25 proxy 方向一致但 effect size 不足以排除混杂"。Claim 2 降级为 exploratory observation：dataflow 在 Qwen 上 CI 包含 0，StarCoder 上方向为负，合并进 Claim 1 作为 strategy-encoder interaction case。SWE-bench delta < 1pp 且 CI 包含 0， 无法作为独立 evidence。论文重心移向 systematic empirical comparison + representation geometry analysis。标题用 "Systematic Study"，定位 analysis paper。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "2a7bf294-76bc-4051-b2db-b0a0f92c173c",
  "type": "user",
  "uuid": "515d6682-9486-4130-951a-4f68efe927e3",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T16:50:06.580Z_

```json
{
  "parentUuid": "515d6682-9486-4130-951a-4f68efe927e3",
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
  "uuid": "a5554e3e-9076-453e-be2a-9c096ba88789",
  "timestamp": "2026-05-14T16:50:06.580Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T16:50:06.580Z_

```json
{
  "parentUuid": "a5554e3e-9076-453e-be2a-9c096ba88789",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "525e3666-079b-4a9c-9cff-2522d956e95a",
  "timestamp": "2026-05-14T16:50:06.580Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3",
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
  "aiTitle": "Generate median-tier simulation paper for dream ID",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3"
}
```

---

### Assistant

_source line 7 · 2026-05-14T16:50:09.240Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "525e3666-079b-4a9c-9cff-2522d956e95a",
  "isSidechain": false,
  "requestId": "req_011Cb2ofWeNUYEe5HCgQsBT9",
  "type": "assistant",
  "uuid": "6ab3914a-2799-4e25-bc32-f7abd0bbfdc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015b3nq3953o24UVSY7ovJn5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11286,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11286,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11286,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11286
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

_source line 8 · 2026-05-14T16:50:09.748Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HUy3iFfsf2ZfuA6M9Lq5BC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ab3914a-2799-4e25-bc32-f7abd0bbfdc9",
  "isSidechain": false,
  "requestId": "req_011Cb2ofWeNUYEe5HCgQsBT9",
  "type": "assistant",
  "uuid": "e4329bda-6761-4241-9c85-e37f00d71347",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015b3nq3953o24UVSY7ovJn5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11286,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11286,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11286,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11286
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

_source line 9 · 2026-05-14T16:50:10.127Z_

<details><summary>↩ Tool result · `toolu_01HUy3iFfsf2ZfuA6M9Lq5BC`</summary>

```text
1	[
2	  {
3	    "name": "SWE-bench Lite End-to-End Evaluation",
4	    "description": "3 strategies × best checkpoint (Qwen), Qwen3.6-27B agent, 300 SWE-bench Lite instances",
5	    "results": {
6	      "random_resolve_rate_pct": 23.0,
7	      "random_resolved_count": 69,
8	      "embedding_resolve_rate_pct": 23.7,
9	      "embedding_resolved_count": 71,
10	      "dataflow_resolve_rate_pct": 23.3,
11	      "dataflow_resolved_count": 70,
12	      "emb_minus_random_delta_pp": 0.7,
13	      "df_minus_random_delta_pp": 0.3,
14	      "total_instances": 300,
15	      "retrieval_R1_on_swebench_random": 0.41,
16	      "retrieval_R1_on_swebench_embedding": 0.42,
17	      "retrieval_R1_on_swebench_dataflow": 0.41
18	    },
19	    "tables": [
20	      {
21	        "name": "Table: SWE-bench Lite Resolve Rate by Strategy",
22	        "columns": [
23	          "Strategy",
24	          "Resolved",
25	          "Total",
26	          "Rate (%)",
27	          "Δ vs Random (pp)"
28	        ],
29	        "rows": [
30	          [
31	            "random",
32	            69,
33	            300,
34	            23.0,
35	            "—"
36	          ],
37	          [
38	            "embedding",
39	            71,
40	            300,
41	            23.7,
42	            "+0.7"
43	          ],
44	          [
45	            "dataflow",
46	            70,
47	            300,
48	            23.3,
49	            "+0.3"
50	          ]
51	        ]
52	      },
53	      {
54	        "name": "Table: Retrieval-Stage R@1 on SWE-bench Repos",
55	        "columns": [
56	          "Strategy",
57	          "R@1",
58	          "R@5"
59	        ],
60	        "rows": [
61	          [
62	            "random",
63	            0.41,
64	            0.78
65	          ],
66	          [
67	            "embedding",
68	            0.42,
69	            0.79
70	          ],
71	          [
72	            "dataflow",
73	            0.41,
74	            0.78
75	          ]
76	        ]
77	      }
78	    ],
79	    "figures": [],
80	    "analysis": "SWE-bench delta 不足以支撑独立 claim。resolve rate 差异 < 1pp，在 N=300 上无统计 显著性（见 plan_016）。Retrieval-stage R@1 差异同样微小（~1pp），说明 SWE-smith 到 SWE-bench 的 domain gap 进一步压平了 strategy 差异。论文中应作为 \"sanity check\" 而非 primary evidence 呈现：确认 negative mining 策略不 harm downstream performance， 但不能 claim 显著 improvement。需在 limitation 中讨论 300 instances 的 power 不足问题。\n\n\nSWE-bench Lite 的 resolve rate 由 agent 生成能力主导，retrieval 只是 pipeline 的第一步。median 档下 retrieval R@1 delta 仅 ~1pp，传导到 end-to-end 后进一步 衰减：即使 retrieval 多找对 1-2 个 file，agent 是否能利用这个 file 生成正确 patch 是独立的噪声源。300 instances 上 2 个 count 的差异对应 ~0.7pp，远不够 statistical significance。此外 SWE-bench 的 repo 分布与 SWE-smith training 分布有 domain shift， 进一步压缩了 retrieval improvement 的传导效率。\n"
81	  },
82	  {
83	    "name": "RepoBench-R Cross-File Retrieval Evaluation",
84	    "description": "3 strategies × 3 seeds × 2 encoders, RepoBench-R test_easy (8K, pool~6) + test_hard (8K, pool~18), with 95% CIs",
85	    "results": {
86	      "qwen_test_easy": {
87	        "random_R1_mean": 0.682,
88	        "embedding_R1_mean": 0.688,
89	        "dataflow_R1_mean": 0.685,
90	        "emb_minus_random_pp": 0.6,
91	        "emb_minus_random_CI": [
92	          -0.2,
93	          1.4
94	        ]
95	      },
96	      "qwen_test_hard": {
97	        "random_R1_mean": 0.394,
98	        "embedding_R1_mean": 0.404,
99	        "dataflow_R1_mean": 0.398,
100	        "emb_minus_random_pp": 1.0,
101	        "emb_minus_random_CI": [
102	          -0.1,
103	          2.1
104	        ]
105	      },
106	      "starcoder_test_easy": {
107	        "random_R1_mean": 0.621,
108	        "embedding_R1_mean": 0.626,
109	        "dataflow_R1_mean": 0.618,
110	        "emb_minus_random_pp": 0.5,
111	        "emb_minus_random_CI": [
112	          -0.3,
113	          1.3
114	        ]
115	      },
116	      "starcoder_test_hard": {
117	        "random_R1_mean": 0.338,
118	        "embedding_R1_mean": 0.346,
119	        "dataflow_R1_mean": 0.333,
120	        "emb_minus_random_pp": 0.8,
121	        "emb_minus_random_CI": [
122	          -0.4,
123	          2.0
124	        ]
125	      },
126	      "overall_delta_pp_range": [
127	        0.0,
128	        1.5
129	      ]
130	    },
131	    "tables": [
132	      {
133	        "name": "Table: RepoBench-R R@1 by Strategy × Encoder × Difficulty",
134	        "columns": [
135	          "Encoder",
136	          "Split",
137	          "Random",
138	          "Embedding",
139	          "Dataflow",
140	          "Emb Δ (pp)",
141	          "DF Δ (pp)"
142	        ],
143	        "rows": [
144	          [
145	            "Qwen",
146	            "easy",
147	            "68.2 ± 0.7",
148	            "68.8 ± 0.8",
149	            "68.5 ± 0.9",
150	            "+0.6",
151	            "+0.3"
152	          ],
153	          [
154	            "Qwen",
155	            "hard",
156	            "39.4 ± 1.0",
157	            "40.4 ± 1.1",
158	            "39.8 ± 1.2",
159	            "+1.0",
160	            "+0.4"
161	          ],
162	          [
163	            "StarCoder",
164	            "easy",
165	            "62.1 ± 0.6",
166	            "62.6 ± 0.7",
167	            "61.8 ± 0.8",
168	            "+0.5",
169	            "−0.3"
170	          ],
171	          [
172	            "StarCoder",
173	            "hard",
174	            "33.8 ± 0.9",
175	            "34.6 ± 1.0",
176	            "33.3 ± 1.1",
177	            "+0.8",
178	            "−0.5"
179	          ]
180	        ]
181	      }
182	    ],
183	    "figures": [],
184	    "analysis": "RepoBench-R 提供了 second benchmark 覆盖，方向一致（embedding ≥ random > dataflow on StarCoder），但 effect size 不足以独立支撑 claim。test_hard 上的 delta 稍大， 说明 pool size 对 strategy 效果有调节作用（与 plan_019 呼应）。论文中报告为 \"directional consistency across benchmarks\" 而非 \"significant improvement on second benchmark\"。CIs 需在 Table 中完整展示以示 transparency。\n\n\nRepoBench-R 的 test_easy pool 仅 ~6 candidates，所有策略接近 ceiling，strategy 差异被压缩到 < 1pp。test_hard pool ~18 提供更多区分空间，delta 稍大（~1pp）但仍在 CI 包含 0 的边缘。RepoBench-R 与 SWE-smith 的 task 定义不同（cross-file completion vs bug-fix retrieval），domain shift 进一步削弱了 training-time strategy 差异的 传导。8K instances 的大样本量使 per-strategy CI 较窄（~1.5pp width），但 delta 的 CI 仍 ~2pp width，因为 strategy 间的 paired variance 较大。Dataflow 在 StarCoder 上一致为负（-0.5pp），符合 pilot 发现的 encoder-strategy interaction pattern。\n"
185	  },
186	  {
187	    "name": "Stratified Retrieval Analysis (5 Strata)",
188	    "description": "分层分析：repo size / pool size / query-pos similarity / structural data availability / neg_difficulty quartile",
189	    "results": {
190	      "stratum_1_repo_size": {
191	        "small_lt50_emb_delta_pp": 1.8,
192	        "medium_50_200_emb_delta_pp": 1.2,
193	        "large_200_500_emb_delta_pp": 0.6,
194	        "xlarge_500plus_emb_delta_pp": 0.4
195	      },
196	      "stratum_2_pool_size": {
197	        "pool_lt10_emb_delta_pp": 0.3,
198	        "pool_10_50_emb_delta_pp": 1.1,
199	        "pool_50plus_emb_delta_pp": 0.7
200	      },
201	      "stratum_3_query_pos_sim": {
202	        "high_sim_gt098_emb_delta_pp": 0.5,
203	        "medium_sim_090_098_emb_delta_pp": 1.3,
204	        "low_sim_lt090_emb_delta_pp": 1.0
205	      },
206	      "stratum_4_structural_availability": {
207	        "with_dataflow_34pct": {
208	          "random_R1": 0.538,
209	          "embedding_R1": 0.548,
210	          "dataflow_R1": 0.544,
211	          "df_minus_random_pp": 0.6,
212	          "emb_minus_random_pp": 1.0
213	        },
214	        "fallback_66pct": {
215	          "random_R1": 0.526,
216	          "embedding_R1": 0.536,
217	          "dataflow_R1": 0.527,
218	          "df_minus_random_pp": 0.1,
219	          "emb_minus_random_pp": 1.0
220	        }
221	      },
222	      "stratum_5_neg_difficulty_quartile": {
223	        "Q1_easiest": {
224	          "emb_delta_pp": 0.3,
225	          "df_delta_pp": -0.2
226	        },
227	        "Q2": {
228	          "emb_delta_pp": 0.8,
229	          "df_delta_pp": 0.1
230	        },
231	        "Q3": {
232	          "emb_delta_pp": 1.4,
233	          "df_delta_pp": 0.5
234	        },
235	        "Q4_hardest": {
236	          "emb_delta_pp": 1.6,
237	          "df_delta_pp": 1.2
238	        }
239	      }
240	    },
241	    "tables": [
242	      {
243	        "name": "Table: Embedding Delta by Repo Size Stratum (Qwen)",
244	        "columns": [
245	          "Stratum",
246	          "N instances",
247	          "Random R@1",
248	          "Emb R@1",
249	          "Δ (pp)",
250	          "95% CI"
251	        ],
252	        "rows": [
253	          [
254	            "small (<50)",
255	            500,
256	            0.571,
257	            0.589,
258	            "+1.8",
259	            "[-0.5, 4.1]"
260	          ],
261	          [
262	            "medium (50-200)",
263	            4096,
264	            0.542,
265	            0.554,
266	            "+1.2",
267	            "[0.0, 2.4]"
268	          ],
269	          [
270	            "large (200-500)",
271	            13628,
272	            0.531,
273	            0.537,
274	            "+0.6",
275	            "[-0.3, 1.5]"
276	          ],
277	          [
278	            "xlarge (500+)",
279	            25949,
280	            0.524,
281	            0.528,
282	            "+0.4",
283	            "[-0.5, 1.3]"
284	          ]
285	        ]
286	      },
287	      {
288	        "name": "Table: Strategy Delta by Structural Data Availability (Qwen)",
289	        "columns": [
290	          "Stratum",
291	          "N",
292	          "Random R@1",
293	          "Emb R@1",
294	          "DF R@1",
295	          "Emb Δ",
296	          "DF Δ"
297	        ],
298	        "rows": [
299	          [
300	            "with dataflow (34%)",
301	            "~15K",
302	            0.538,
303	            0.548,
304	            0.544,
305	            "+1.0",
306	            "+0.6"
307	          ],
308	          [
309	            "fallback (66%)",
310	            "~29K",
311	            0.526,
312	            0.536,
313	            0.527,
314	            "+1.0",
315	            "+0.1"
316	          ]
317	        ]
318	      },
319	      {
320	        "name": "Table: Strategy Delta by Neg Difficulty Quartile (Qwen)",
321	        "columns": [
322	          "Quartile",
323	          "Margin range",
324	          "Emb Δ (pp)",
325	          "DF Δ (pp)"
326	        ],
327	        "rows": [
328	          [
329	            "Q1 (easiest)",
330	            "> 0.15",
331	            "+0.3",
332	            "−0.2"
333	          ],
334	          [
335	            "Q2",
336	            "0.08–0.15",
337	            "+0.8",
338	            "+0.1"
339	          ],
340	          [
341	            "Q3",
342	            "0.02–0.08",
343	            "+1.4",
344	            "+0.5"
345	          ],
346	          [
347	            "Q4 (hardest)",
348	            "< 0.02",
349	            "+1.6",
350	            "+1.2"
351	          ]
352	        ]
353	      }
354	    ],
355	    "figures": [],
356	    "analysis": "分层分析揭示了 effect size heterogeneity：embedding mining 在 small repo / high difficulty / medium similarity 条件下效果最好，但这些条件在实际分布中占比小。 Structural availability 分层确认了 dataflow 的 conditional benefit 完全来自有 structural data 的 34%（delta +0.6pp），fallback 的 66% 贡献为零。这解释了为什么 overall dataflow delta 被 dilute 到接近 0。Neg difficulty quartile 分析提供了 最清晰的 mechanistic story：当 negatives 足够 hard（Q4），both strategies help； 当 negatives 太 easy（Q1），neither helps much。这支持 representation geometry explanation 但 effect size 不足以作为独立 claim。\n\n\nRepo size 分层：小 repo 的 pool 小、diversity 低，embedding mining 更容易找到有意义 的 hard negatives，所以 delta 最大。大 repo 中 pool 大但 noise 也大（更多 unrelated files），embedding mining 优势被稀释。Pool size 分层与 repo size 部分共线但不完全： pool < 10 时 all strategies 接近 ceiling 所以 delta 小；pool 10-50 是 sweet spot； pool 50+ 时 noise 增加。Query-pos similarity 分层：high sim (> 0.98，Qwen 主导) 表明 representation 已饱和，embedding negatives 不够 hard，delta 小；medium sim 区间 embedding mining 最 effective。Structural availability 分层：34% 有 dataflow 数据的 instances 上 dataflow strategy 有 +0.6pp 优势（真正用到了 structural signal）， 但 66% fallback instances 上 dataflow ≈ random（因为 fallback 到 random sampling）， 整体被 dilute。Neg difficulty quartile：Q4（最难 negatives）时 embedding 和 dataflow 都 help 最多，因为这些 cases 正是模型最 confuse 的地方，harder negatives 提供最大 gradient signal。但 Q1-Q2 占比大，dilute 了整体 effect。\n"
357	  },
358	  {
359	    "name": "Call-Graph Hop-Count Ablation",
360	    "description": "1-hop vs 2-hop vs 3-hop call-graph bounding for dataflow negative selection",
361	    "results": {
362	      "qwen_1hop_df_R1": 0.53,
363	      "qwen_2hop_df_R1": 0.532,
364	      "qwen_3hop_df_R1": 0.529,
365	      "starcoder_1hop_df_R1": 0.434,
366	      "starcoder_2hop_df_R1": 0.437,
367	      "starcoder_3hop_df_R1": 0.436,
368	      "qwen_2hop_minus_1hop_pp": 0.2,
369	      "qwen_2hop_minus_3hop_pp": 0.3,
370	      "eligible_negatives_per_query": {
371	        "hop_1": 3.2,
372	        "hop_2": 8.7,
373	        "hop_3": 14.1
374	      },
375	      "fallback_to_random_pct": {
376	        "hop_1": 42,
377	        "hop_2": 28,
378	        "hop_3": 18
379	      }
380	    },
381	    "tables": [
382	      {
383	        "name": "Table: Dataflow R@1 by Hop Count",
384	        "columns": [
385	          "Encoder",
386	          "1-hop",
387	          "2-hop",
388	          "3-hop",
389	          "Best"
390	        ],
391	        "rows": [
392	          [
393	            "Qwen",
394	            0.53,
395	            0.532,
396	            0.529,
397	            "2-hop"
398	          ],
399	          [
400	            "StarCoder",
401	            0.434,
402	            0.437,
403	            0.436,
404	            "2-hop"
405	          ]
406	        ]
407	      },
408	      {
409	        "name": "Table: Negative Pool Statistics by Hop Count",
410	        "columns": [
411	          "Hops",
412	          "Mean eligible neg/query",
413	          "Fallback-to-random %"
414	        ],
415	        "rows": [
416	          [
417	            1,
418	            3.2,
419	            "42%"
420	          ],
421	          [
422	            2,
423	            8.7,
424	            "28%"
425	          ],
426	          [
427	            3,
428	            14.1,
429	            "18%"
430	          ]
431	        ]
432	      }
433	    ],
434	    "figures": [],
435	    "analysis": "2-hop 作为默认设置是合理的，但 ablation signal 太弱（< 0.5pp）无法 claim hop count 是 critical design choice。放入 appendix 作为 hyperparameter justification 即可。 更重要的 takeaway 是 1-hop 的 high fallback rate（42%），说明 inter-procedural dataflow 的 coverage 本身就有限——这与 plan_005 structural availability 分层的 34% 数字一致。\n\n\n1-hop 限制太严格：平均每 query 只有 3.2 个 eligible dataflow-disconnected negatives， 42% 的 queries 不得不 fallback 到 random，稀释了 structural signal。2-hop 是 precision-recall sweet spot：8.7 eligible negatives 足够采样，fallback 率降到 28%。 3-hop 进一步扩大 candidate pool 但引入 semantically distant files（3-hop 以外的 files 很可能本来就和 query 无关），负 signal 质量下降，反而略差于 2-hop。但三者 差异均 < 0.5pp，在 noise range 内，不构成 strong ablation signal。这也反映了 median 档下 dataflow strategy 本身 effect size 就小，hop-count 作为 second-order effect 自然更小。\n"
436	  },
437	  {
438	    "name": "Training Data Size Scaling",
439	    "description": "1K vs 3K vs 5K training instances × 3 strategies, Qwen encoder",
440	    "results": {
441	      "qwen_1K": {
442	        "random_R1": 0.498,
443	        "embedding_R1": 0.501,
444	        "dataflow_R1": 0.495,
445	        "emb_delta_pp": 0.3
446	      },
447	      "qwen_3K": {
448	        "random_R1": 0.519,
449	        "embedding_R1": 0.528,
450	        "dataflow_R1": 0.521,
451	        "emb_delta_pp": 0.9
452	      },
453	      "qwen_5K": {
454	        "random_R1": 0.53,
455	        "embedding_R1": 0.54,
456	        "dataflow_R1": 0.532,
457	        "emb_delta_pp": 1.0
458	      },
459	      "scaling_slope_R1_per_1K": 0.008
460	    },
461	    "tables": [
462	      {
463	        "name": "Table: R@1 by Data Size × Strategy (Qwen)",
464	        "columns": [
465	          "Size",
466	          "Random",
467	          "Embedding",
468	          "Dataflow",
469	          "Emb Δ (pp)"
470	        ],
471	        "rows": [
472	          [
473	            "1K",
474	            0.498,
475	            0.501,
476	            0.495,
477	            "+0.3"
478	          ],
479	          [
480	            "3K",
481	            0.519,
482	            0.528,
483	            0.521,
484	            "+0.9"
485	          ],
486	          [
487	            "5K (full)",
488	            0.53,
489	            0.54,
490	            0.532,
491	            "+1.0"
492	          ]
493	        ]
494	      }
495	    ],
496	    "figures": [],
497	    "analysis": "Data scaling 是 positive signal：说明 embedding mining 的 benefit 不是 overfitting artifact（否则小数据时 delta 应更大）。但 sub-linear scaling 和 5K 时仍只有 +1.0pp 的 delta 说明 pretrained representation quality 是 bottleneck，更多 data 不会 dramatically 改变 strategy ranking。适合放入 appendix，支撑 \"mining benefit is real but modest\" 的 narrative。\n\n\n1K instances 时所有策略都 underfit：training data 不足以让 contrastive loss 充分 学习，absolute R@1 低（~0.50）。Embedding mining 在 1K 时优势最小（+0.3pp）， 因为 1K instances 中 embedding-distance 的 top-k negatives 覆盖了 corpus 的较小 subset，mining quality 受限于 candidate pool diversity。3K 到 5K 的 scaling 呈 sub-linear 增长（+1.1pp absolute from 3K→5K vs +2.1pp from 1K→3K），说明 returns diminishing。Strategy delta 的 scaling 也 sub-linear：embedding 优势在 3K 时已接近 5K 水平。这表明 effect size 的上限由 pretrained representation quality 决定，不会随 data 无限增大。\n"
498	  },
499	  {
500	    "name": "Fusion Head Ablation",
501	    "description": "Embedding-only vs structural-features-only vs combined scoring head",
502	    "results": {
503	      "qwen_embedding_only_R1": 0.539,
504	      "qwen_structural_only_R1": 0.412,
505	      "qwen_combined_R1": 0.541,
506	      "starcoder_embedding_only_R1": 0.449,
507	      "starcoder_structural_only_R1": 0.378,
508	      "starcoder_combined_R1": 0.451,
509	      "combined_minus_embedding_only_pp": 0.2
510	    },
511	    "tables": [
512	      {
513	        "name": "Table: Fusion Head Ablation R@1",
514	        "columns": [
515	          "Encoder",
516	          "Emb-only",
517	          "Struct-only",
518	          "Combined",
519	          "Combined−Emb (pp)"
520	        ],
521	        "rows": [
522	          [
523	            "Qwen",
524	            0.539,
525	            0.412,
526	            0.541,
527	            "+0.2"
528	          ],
529	          [
530	            "StarCoder",
531	            0.449,
532	            0.378,
533	            0.451,
534	            "+0.2"
535	          ]
536	        ]
537	      }
538	    ],
539	    "figures": [],
540	    "analysis": "确认 StructFuse 的 value 在 training-time negative selection 而非 inference-time feature fusion。Combined head 的 marginal gain 可能不值得 inference-time 的 CodeQL dependency。论文中作为 appendix ablation，支撑 \"negative selection is the key mechanism\" 的 argument。\n\n\nStructural-features-only（仅用 dataflow connectivity、call-graph distance 等 discrete features）大幅落后，因为 binary/categorical structural features 的 信息量远不及 dense embedding。Combined head 相比 embedding-only 仅 +0.2pp， 因为在 median 档下 structural signal 本身就弱（plan_005 已示），fusion 无法 从弱 signal 中 extract 出更多 information。这说明 structural information 的 value 主要体现在 negative selection（training time）而非 scoring（inference time）。\n"
541	  },
542	  {
543	    "name": "Dataflow-Distance Weighted vs Binary Negatives",
544	    "description": "Weighted sampling by dataflow distance vs binary connected/disconnected",
545	    "results": {
546	      "qwen_binary_df_R1": 0.532,
547	      "qwen_weighted_df_R1": 0.535,
548	      "starcoder_binary_df_R1": 0.437,
549	      "starcoder_weighted_df_R1": 0.439,
550	      "weighted_minus_binary_pp": 0.3,
551	      "weighted_minus_binary_CI": [
552	        -0.8,
553	        1.4
554	      ]
555	    },
556	    "tables": [
557	      {
558	        "name": "Table: Binary vs Weighted Dataflow Negatives",
559	        "columns": [
560	          "Encoder",
561	          "Binary DF R@1",
562	          "Weighted DF R@1",
563	          "Δ (pp)"
564	        ],
565	        "rows": [
566	          [
567	            "Qwen",
568	            0.532,
569	            0.535,
570	            "+0.3"
571	          ],
572	          [
573	            "StarCoder",
574	            0.437,
575	            0.439,
576	            "+0.2"
577	          ]
578	        ]
579	      }
580	    ],
581	    "figures": [],
582	    "analysis": "Effect 太小，不值得增加 pipeline complexity。Binary 作为默认 simple choice 是合理的。 放入 appendix 一句话即可。\n\n\nDistance-weighted sampling 理论上应该更好：给距离更远（更 disconnected）的 negatives 更高采样概率，提供更 clean 的 structural signal。但在 median 档下 dataflow strategy 本身 effect size 就小，在此基础上的 second-order refinement 自然更小（+0.3pp），CI 宽且包含 0。实际上 binary 和 weighted 的差异主要来自 少数 outlier queries（dataflow distance 分布高度 skewed），大多数 queries 的 negatives 在两种 scheme 下 overlap 很大。\n"
583	  },
584	  {
585	    "name": "SWE-bench Failure Analysis",
586	    "description": "50 SweRank/BM25 failures, categorize by whether dataflow helps",
587	    "results": {
588	      "total_failures_analyzed": 50,
589	      "category_structural_gap": 14,
590	      "category_lexical_gap": 18,
591	      "category_multi_file_dependency": 8,
592	      "category_other": 10,
593	      "df_helps_in_structural_gap_pct": 57,
594	      "df_helps_overall_pct": 28,
595	      "emb_helps_overall_pct": 36
596	    },
597	    "tables": [
598	      {
599	        "name": "Table: Failure Category Distribution",
600	        "columns": [
601	          "Category",
602	          "Count",
603	          "%",
604	          "DF helps",
605	          "Emb helps"
606	        ],
607	        "rows": [
608	          [
609	            "Structural gap",
610	            14,
611	            "28%",
612	            "8 (57%)",
613	            "5 (36%)"
614	          ],
615	          [
616	            "Lexical gap",
617	            18,
618	            "36%",
619	            "3 (17%)",
620	            "6 (33%)"
621	          ],
622	          [
623	            "Multi-file dependency",
624	            8,
625	            "16%",
626	            "4 (50%)",
627	            "5 (63%)"
628	          ],
629	          [
630	            "Other",
631	            10,
632	            "20%",
633	            "1 (10%)",
634	            "2 (20%)"
635	          ]
636	        ]
637	      }
638	    ],
639	    "figures": [],
640	    "analysis": "Failure analysis 提供了 qualitative evidence 支撑 \"structural signal helps in specific conditions\" 的 narrative，但也暴露了 ceiling：真正 structural gap 的 cases 只占 28%，coverage 限制了其中一半。适合放入 Section 5 的 analysis 段落， 不足以 support independent claim。\n\n\n50 个 failure cases 中，仅 14 个（28%）属于 structural gap（即 gold file 与 query 有 dataflow 关系但无 lexical similarity）。在这 14 个中，dataflow strategy 成功 retrieve 了 8 个（57%），但剩余 6 个仍然 fail 因为 structural data 不覆盖（34% coverage limitation）。最大的 failure category 是 lexical gap（36%，query 描述 与 target file 用语完全不同），这两种 strategy 都无法解决。这解释了为什么 overall effect size 小：真正 benefit from structural signal 的 cases 只占 ~28%，且其中 仍有近半 coverage 不足。\n"
641	  },
642	  {
643	    "name": "Qualitative Case Studies",
644	    "description": "5-10 cases where structural negatives changed retrieval outcome",
645	    "results": {
646	      "total_cases_selected": 7,
647	      "cases_df_uniquely_helps": 3,
648	      "cases_emb_uniquely_helps": 2,
649	      "cases_both_help": 2,
650	      "avg_gold_rank_improvement_df": 4.2,
651	      "avg_gold_rank_improvement_emb": 2.8
652	    },
653	    "tables": [
654	      {
655	        "name": "Table: Selected Qualitative Cases",
656	        "columns": [
657	          "Case",
658	          "Repo",
659	          "Issue type",
660	          "Random rank",
661	          "Emb rank",
662	          "DF rank",
663	          "Key observation"
664	        ],
665	        "rows": [
666	          [
667	            1,
668	            "repo_A",
669	            "missing import",
670	            12,
671	            8,
672	            2,
673	            "DF finds cross-module callee"
674	          ],
675	          [
676	            2,
677	            "repo_B",
678	            "API mismatch",
679	            9,
680	            3,
681	            4,
682	            "Emb finds similar naming"
683	          ],
684	          [
685	            3,
686	            "repo_C",
687	            "config propagation",
688	            15,
689	            11,
690	            1,
691	            "DF traces config flow"
692	          ],
693	          [
694	            4,
695	            "repo_D",
696	            "type error",
697	            6,
698	            2,
699	            3,
700	            "Both find related types"
701	          ],
702	          [
703	            5,
704	            "repo_E",
705	            "null pointer",
706	            11,
707	            7,
708	            3,
709	            "DF finds data source"
710	          ],
711	          [
712	            6,
713	            "repo_F",
714	            "method override",
715	            4,
716	            1,
717	            5,
718	            "Emb captures signature sim"
719	          ],
720	          [
721	            7,
722	            "repo_G",
723	            "circular dep",
724	            14,
725	            10,
726	            2,
727	            "DF traces dependency cycle"
728	          ]
729	        ]
730	      }
731	    ],
732	    "figures": [],
733	    "analysis": "Qualitative examples 是论文的 illustration 而非 evidence。选择具有 pedagogical value 的 cases 来解释 mechanism。在 median 档下，需要 caveat \"these are selected to illustrate the mechanism; overall effect size is modest (Table X)\"。\n\n\nCherry-picking 7 个 illustrative cases。3 个 cases 中 dataflow strategy 将 gold file 从 rank 8-15 提升到 rank 1-3（大幅改善），这些 cases 的共同特征是 gold file 与 query 有 call-chain dependency 但无 keyword overlap。2 个 cases 中 embedding strategy 独特帮助（gold file 与 query 有 similar variable naming 但 random negatives 中缺少 near-miss distractors）。但 cherry-picked cases 不代表 overall distribution（见 plan_011 的 28% structural gap rate）。\n"
734	  },
735	  {
736	    "name": "Temperature Ablation",
737	    "description": "τ ∈ {0.05, 0.1, 0.2} × 3 strategies × 2 encoders",
738	    "results": {
739	      "qwen": {
740	        "tau_005": {
741	          "random_R1": 0.53,
742	          "embedding_R1": 0.54,
743	          "dataflow_R1": 0.532,
744	          "emb_delta_pp": 1.0
745	        },
746	        "tau_010": {
747	          "random_R1": 0.537,
748	          "embedding_R1": 0.545,
749	          "dataflow_R1": 0.537,
750	          "emb_delta_pp": 0.8
751	        },
752	        "tau_020": {
753	          "random_R1": 0.521,
754	          "embedding_R1": 0.526,
755	          "dataflow_R1": 0.52,
756	          "emb_delta_pp": 0.5
757	        }
758	      },
759	      "starcoder": {
760	        "tau_005": {
761	          "random_R1": 0.443,
762	          "embedding_R1": 0.45,
763	          "dataflow_R1": 0.437,
764	          "emb_delta_pp": 0.7
765	        },
766	        "tau_010": {
767	          "random_R1": 0.451,
768	          "embedding_R1": 0.457,
769	          "dataflow_R1": 0.446,
770	          "emb_delta_pp": 0.6
771	        },
772	        "tau_020": {
773	          "random_R1": 0.435,
774	          "embedding_R1": 0.438,
775	          "dataflow_R1": 0.43,
776	          "emb_delta_pp": 0.3
777	        }
778	      },
779	      "optimal_tau": 0.1,
780	      "strategy_ranking_preserved_across_tau": true,
781	      "delta_shrinks_at_high_tau": true
782	    },
783	    "tables": [
784	      {
785	        "name": "Table: R@1 by Temperature × Strategy (Qwen)",
786	        "columns": [
787	          "τ",
788	          "Random",
789	          "Embedding",
790	          "Dataflow",
791	          "Emb Δ (pp)",
792	          "Best strat"
793	        ],
794	        "rows": [
795	          [
796	            0.05,
797	            0.53,
798	            0.54,
799	            0.532,
800	            "+1.0",
801	            "embedding"
802	          ],
803	          [
804	            0.1,
805	            0.537,
806	            0.545,
807	            0.537,
808	            "+0.8",
809	            "embedding"
810	          ],
811	          [
812	            0.2,
813	            0.521,
814	            0.526,
815	            0.52,
816	            "+0.5",
817	            "embedding"
818	          ]
819	        ]
820	      },
821	      {
822	        "name": "Table: R@1 by Temperature × Strategy (StarCoder)",
823	        "columns": [
824	          "τ",
825	          "Random",
826	          "Embedding",
827	          "Dataflow",
828	          "Emb Δ (pp)",
829	          "Best strat"
830	        ],
831	        "rows": [
832	          [
833	            0.05,
834	            0.443,
835	            0.45,
836	            0.437,
837	            "+0.7",
838	            "embedding"
839	          ],
840	          [
841	            0.1,
842	            0.451,
843	            0.457,
844	            0.446,
845	            "+0.6",
846	            "embedding"
847	          ],
848	          [
849	            0.2,
850	            0.435,
851	            0.438,
852	            0.43,
853	            "+0.3",
854	            "embedding"
855	          ]
856	        ]
857	      }
858	    ],
859	    "figures": [],
860	    "analysis": "Temperature ablation 提供两个 key findings：(1) strategy ranking 在 τ 范围内 preserved（robustness check passed），(2) optimal τ 可能是 0.1 而非 0.05，但在 optimal τ 下 embedding delta 只有 0.6-0.8pp。这要求论文报告 best-τ 结果时 acknowledge effect size 进一步缩小。建议报告 τ=0.05 作为 primary（与 prior work 对齐）加 τ sensitivity 在 appendix。如果 reviewer 质疑 regime-specificity， 可以 argue ranking preserved 但 concede magnitude is τ-dependent。\n\n\nτ=0.05（当前默认）可能过低：contrastive loss 的 gradient 过于 sharp，模型对 hard negatives 过度 sensitive，导致 overfitting（plan_002 中 step 500 后即 overfit）。 τ=0.1 在 median 档下反而略好：gradient 更 smooth，模型更 robust，absolute R@1 比 τ=0.05 高 ~0.7pp（Qwen）和 ~0.8pp（StarCoder）。但 strategy delta 在 τ=0.1 时略小（0.8pp vs 1.0pp Qwen），因为 smoother gradient 也 smooth 掉了 hard negative 的 extra signal。τ=0.2 过高：loss landscape 太 flat，training signal 不足， all strategies 退化。关键发现：strategy ranking（embedding > random ≥ dataflow） 在所有 τ 下保持一致，说明 finding 不是 regime-specific。但 delta 随 τ 增大而 缩小，表明在 optimal τ 下 effect size 可能更小。这是 median 档的典型 pattern： finding 方向 robust 但 magnitude 依赖 hyperparameter。\n"
861	  },
862	  {
863	    "name": "Dynamic vs Static Embedding Mining",
864	    "description": "Dynamic re-mine embedding negatives per epoch vs static (mine once from pretrained), Qwen encoder",
865	    "results": {
866	      "qwen_static_emb_R1": 0.54,
867	      "qwen_dynamic_emb_R1": 0.544,
868	      "dynamic_minus_static_pp": 0.4,
869	      "dynamic_minus_static_CI": [
870	        -0.8,
871	        1.6
872	      ],
873	      "training_time_ratio_dynamic_vs_static": 2.3
874	    },
875	    "tables": [
876	      {
877	        "name": "Table: Static vs Dynamic Embedding Mining (Qwen)",
878	        "columns": [
879	          "Mining",
880	          "R@1",
881	          "Δ vs static (pp)",
882	          "Train time (h)",
883	          "CI"
884	        ],
885	        "rows": [
886	          [
887	            "static",
888	            0.54,
889	            "—",
890	            7.5,
891	            "—"
892	          ],
893	          [
894	            "dynamic",
895	            0.544,
896	            "+0.4",
897	            17.3,
898	            "[-0.8, 1.6]"
899	          ]
900	        ]
901	      }
902	    ],
903	    "figures": [],
904	    "analysis": "Dynamic mining 是 expensive 的 marginal improvement。论文中一句话 dismiss this confound：\"We additionally tested dynamic re-mining (per-epoch) and found no significant improvement over static mining (Δ=+0.4pp, p=0.38), likely because the encoder changes minimally over 2-3 epochs.\"\n\n\nDynamic mining 每个 epoch 用 current encoder 重新计算 embeddings 并 re-mine negatives，理论上 negatives 始终 adaptive to current model state。但在 median 档下 static mining 本身 effect size 就小（+1.0pp），dynamic 的 incremental gain 仅 +0.4pp，因为 (1) training 只跑 2-3 epochs，encoder 变化不大，re-mining 的 negatives 与 static 的 overlap 很大（estimated > 80% overlap），(2) dynamic mining 需要 per-epoch full-corpus encoding，training time 翻 2.3x，cost-benefit 不划算。CI 包含 0，说明 gain 不 significant。这个结果也部分缓解了 \"static mining confound\" 的 reviewer concern：dynamic 没有 dramatically 改变 picture。\n"
905	  },
906	  {
907	    "name": "Bootstrap CI for SWE-bench Resolve Rate",
908	    "description": "95% bootstrap confidence intervals for all strategy comparisons on SWE-bench Lite",
909	    "results": {
910	      "n_bootstrap_samples": 10000,
911	      "random_resolve_rate_pct": 23.0,
912	      "random_CI": [
913	        18.3,
914	        27.7
915	      ],
916	      "embedding_resolve_rate_pct": 23.7,
917	      "embedding_CI": [
918	        18.7,
919	        28.3
920	      ],
921	      "dataflow_resolve_rate_pct": 23.3,
922	      "dataflow_CI": [
923	        18.3,
924	        28.0
925	      ],
926	      "emb_minus_random_delta_pp": 0.7,
927	      "emb_minus_random_CI": [
928	        -3.2,
929	        4.5
930	      ],
931	      "emb_minus_random_p_value": 0.62,
932	      "df_minus_random_delta_pp": 0.3,
933	      "df_minus_random_CI": [
934	        -3.8,
935	        4.4
936	      ],
937	      "df_minus_random_p_value": 0.78,
938	      "any_comparison_significant": false
939	    },
940	    "tables": [
941	      {
942	        "name": "Table: SWE-bench Bootstrap CIs",
943	        "columns": [
944	          "Comparison",
945	          "Δ (pp)",
946	          "95% CI",
947	          "p-value",
948	          "Significant?"
949	        ],
950	        "rows": [
951	          [
952	            "emb − random",
953	            "+0.7",
954	            "[-3.2, 4.5]",
955	            0.62,
956	            "No"
957	          ],
958	          [
959	            "df − random",
960	            "+0.3",
961	            "[-3.8, 4.4]",
962	            0.78,
963	            "No"
964	          ],
965	          [
966	            "emb − df",
967	            "+0.3",
968	            "[-3.5, 4.2]",
969	            0.73,
970	            "No"
971	          ]
972	        ]
973	      }
974	    ],
975	    "figures": [],
976	    "analysis": "SWE-bench CIs 确认 end-to-end evaluation 对 retrieval strategy 的 sensitivity 不足。这不是 negative result 而是 power limitation。论文中必须 transparently 报告 \"SWE-bench evaluation confirms no strategy harms downstream performance, but the benchmark is underpowered to detect the retrieval-stage deltas we observe (< 1pp)\"。Power analysis figure 可放入 appendix 支撑此 argument。\n\n\nN=300 binary outcomes（resolve/not-resolve）的 bootstrap CI 很宽：individual strategy 的 CI width ~9.5pp，paired delta 的 CI width ~7.7pp。这是因为 binary outcome 的 variance 最大（Bernoulli variance = p(1-p) ≈ 0.18），300 instances 给出的 standard error ≈ sqrt(0.18/300) ≈ 0.024 = 2.4pp，95% CI ≈ ±4.7pp。 在 delta < 1pp 的情况下，不可能 achieve significance。这是 fundamental power limitation，不是方法问题。Even with 3000 instances (full SWE-bench)，delta 0.7pp 仍需要 N > 15000 才能 detect with 80% power。\n"
977	  },
978	  {
979	    "name": "Inference-Time Graph Method Literature Comparison",
980	    "description": "Analysis-only comparison with CodexGraph, LocAgent, RANGER etc. (no experiment)",
981	    "results": {
982	      "papers_compared": 8,
983	      "key_distinction": "training-time mining vs inference-time navigation",
984	      "complementary_not_competing": true,
985	      "overlap_with_our_approach": "minimal — they inject structure at inference, we use structure for training data curation"
986	    },
987	    "tables": [
988	      {
989	        "name": "Table: Comparison with Inference-Time Graph Methods",
990	        "columns": [
991	          "Method",
992	          "Graph type",
993	          "When used",
994	          "Scope",
995	          "Complementary?"
996	        ],
997	        "rows": [
998	          [
999	            "CodexGraph",
1000	            "Repository graph",
1001	            "Inference",
1002	            "Navigation",
1003	            "Yes"
1004	          ],
1005	          [
1006	            "LocAgent",
1007	            "Code structure",
1008	            "Inference",
1009	            "Localization",
1010	            "Yes"
1011	          ],
1012	          [
1013	            "RANGER",
1014	            "AST + deps",
1015	            "Inference",
1016	            "Ranking",
1017	            "Yes"
1018	          ],
1019	          [
1020	            "StructFuse (ours)",
1021	            "Dataflow",
1022	            "Training",
1023	            "Neg mining",
1024	            "—"
1025	          ]
1026	        ]
1027	      }
1028	    ],
1029	    "figures": [],
1030	    "analysis": "Discussion section 需要明确 position StructFuse 为 complementary approach，not competing with inference-time methods。这也为 future work 提供了 natural extension： combine StructFuse-trained retriever with inference-time graph navigation。 Median 档下这是 speculative future work 而非 verified claim。\n\n\n8 篇 inference-time graph 方法（CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG）都在 inference 时构建或查询 code graph。与 StructFuse 的区别是 fundamental：我们在 training time 用 graph 选 negatives，他们在 inference time 用 graph navigate。二者理论上 complementary（可以用 StructFuse 训练的 retriever 作为这些 inference-time methods 的 backbone）。但 median 档下我们 没有实验验证 complementarity，只能 argue in principle。这个 literature gap 在 前几轮 review 中被 flagged（best-R2-W5），written comparison 应该足够 address。\n"
1031	  },
1032	  {
1033	    "name": "BM25 Hard Negative Baseline",
1034	    "description": "BM25-based hard negatives as 4th strategy, 1 seed × 2 encoders, compare with random/embedding/dataflow",
1035	    "results": {
1036	      "qwen_bm25_R1": 0.521,
1037	      "qwen_random_R1": 0.53,
1038	      "qwen_embedding_R1": 0.54,
1039	      "qwen_bm25_minus_random_pp": -0.9,
1040	      "qwen_bm25_minus_random_CI": [
1041	        -2.8,
1042	        1.0
1043	      ],
1044	      "qwen_bm25_minus_random_p_value": 0.12,
1045	      "starcoder_bm25_R1": 0.436,
1046	      "starcoder_random_R1": 0.443,
1047	      "starcoder_embedding_R1": 0.45,
1048	      "starcoder_bm25_minus_random_pp": -0.7,
1049	      "starcoder_bm25_minus_random_CI": [
1050	        -2.5,
1051	        1.1
1052	      ],
1053	      "starcoder_bm25_minus_random_p_value": 0.18,
1054	      "bm25_rank": "worst among 4 strategies",
1055	      "bm25_vs_embedding_delta_pp_qwen": -1.9,
1056	      "bm25_vs_embedding_delta_pp_starcoder": -1.4
1057	    },
1058	    "tables": [
1059	      {
1060	        "name": "Table: 4-Strategy Comparison R@1",
1061	        "columns": [
1062	          "Strategy",
1063	          "Qwen R@1",
1064	          "StarCoder R@1",
1065	          "Qwen Δ vs Random",
1066	          "StarCoder Δ vs Random"
1067	        ],
1068	        "rows": [
1069	          [
1070	            "random",
1071	            0.53,
1072	            0.443,
1073	            "—",
1074	            "—"
1075	          ],
1076	          [
1077	            "embedding",
1078	            0.54,
1079	            0.45,
1080	            "+1.0",
1081	            "+0.7"
1082	          ],
1083	          [
1084	            "dataflow",
1085	            0.532,
1086	            0.437,
1087	            "+0.2",
1088	            "−0.6"
1089	          ],
1090	          [
1091	            "BM25",
1092	            0.521,
1093	            0.436,
1094	            "−0.9",
1095	            "−0.7"
1096	          ]
1097	        ]
1098	      },
1099	      {
1100	        "name": "Table: BM25 vs Embedding Delta (the CoCoHaNeRe gap)",
1101	        "columns": [
1102	          "Encoder",
1103	          "BM25 R@1",
1104	          "Emb R@1",
1105	          "Δ (pp)",
1106	          "CoCoHaNeRe reported",
1107	          "Our explanation"
1108	        ],
1109	        "rows": [
1110	          [
1111	            "Qwen",
1112	            0.521,
1113	            0.54,
1114	            "−1.9",
1115	            "−27",
1116	            "Different mining protocol, pool size, pipeline robustness"
1117	          ],
1118	          [
1119	            "StarCoder",
1120	            0.436,
1121	            0.45,
1122	            "−1.4",
1123	            "n/a",
1124	            "Consistent direction, smaller magnitude"
1125	          ]
1126	        ]
1127	      }
1128	    ],
1129	    "figures": [],
1130	    "analysis": "BM25 baseline 是 median 档下最重要的新增实验。它 partially 但不 fully closes the CoCoHaNeRe correction argument。方向一致（BM25 harm, embedding help）支撑了 \"proxy conflation\" 的 narrative，但 delta 太小（-0.9pp vs -27pp）且 p > 0.05 意味着 argument 需要 soften。论文叙事从 \"we prove CoCoHaNeRe was wrong\" 调整为 \"we observe that BM25-proxy negatives trend toward harm while true embedding negatives trend toward benefit, consistent with the hypothesis that CoCoHaNeRe's reported -27pp harm was amplified by proxy conflation and other uncontrolled factors\"。这是 median 档 framing 的核心转变。Need related work 深度对比 （ANCE, curriculum mining, DPR hard negatives）来 contextualize 为什么 effect size 在 code domain 普遍 modest。\n\n\nBM25 negatives 是 lexical-similarity top-k，与 true embedding distance negatives 的 selection 方式 fundamentally 不同。BM25 top-k 主要 capture keyword overlap （function names, import statements），这些 \"negatives\" 中很多实际上是 semantically related（可能包含 false negatives / actual positives mislabeled as negatives）， 导致 noisy training signal。在 median 档下，BM25 harm 方向正确（-0.9pp Qwen, -0.7pp StarCoder），但 delta 小于 CoCoHaNeRe 报告的 -27pp。原因：(1) 我们的 training pipeline 更 robust（proper temperature, early stopping），(2) pool=50 限制了 BM25 negatives 的 \"hardness\"（不像 CoCoHaNeRe 的 full-corpus mining）。 p > 0.05 说明 harm 不 significant，but direction is consistent。这 partially closes the correction argument：可以 say \"BM25-proxy negatives harm in the direction CoCoHaNeRe reports, but the magnitude in our controlled setup is much smaller, suggesting their -27pp included other confounds beyond negative source\"。 不能 fully close（p > 0.05），只能 partially support。\n"
1131	  },
1132	  {
1133	    "name": "Pool Size Sensitivity Analysis",
1134	    "description": "Strategy ranking stability at pool={50, 100, 200, 500} on SWE-smith validation",
1135	    "results": {
1136	      "qwen": {
1137	        "pool_50": {
1138	          "random_R1": 0.53,
1139	          "embedding_R1": 0.54,
1140	          "dataflow_R1": 0.532,
1141	          "ranking": "emb > df > rand"
1142	        },
1143	        "pool_100": {
1144	          "random_R1": 0.412,
1145	          "embedding_R1": 0.421,
1146	          "dataflow_R1": 0.413,
1147	          "ranking": "emb > df ≈ rand"
1148	        },
1149	        "pool_200": {
1150	          "random_R1": 0.328,
1151	          "embedding_R1": 0.335,
1152	          "dataflow_R1": 0.33,
1153	          "ranking": "emb > df ≈ rand"
1154	        },
1155	        "pool_500": {
1156	          "random_R1": 0.241,
1157	          "embedding_R1": 0.246,
1158	          "dataflow_R1": 0.244,
1159	          "ranking": "emb ≈ df ≈ rand"
1160	        }
1161	      },
1162	      "starcoder": {
1163	        "pool_50": {
1164	          "random_R1": 0.443,
1165	          "embedding_R1": 0.45,
1166	          "dataflow_R1": 0.437,
1167	          "ranking": "emb > rand > df"
1168	        },
1169	        "pool_100": {
1170	          "random_R1": 0.339,
1171	          "embedding_R1": 0.345,
1172	          "dataflow_R1": 0.334,
1173	          "ranking": "emb > rand > df"
1174	        },
1175	        "pool_200": {
1176	          "random_R1": 0.268,
1177	          "embedding_R1": 0.272,
1178	          "dataflow_R1": 0.271,
1179	          "ranking": "emb ≈ df ≈ rand"
1180	        },
1181	        "pool_500": {
1182	          "random_R1": 0.194,
1183	          "embedding_R1": 0.196,
1184	          "dataflow_R1": 0.197,
1185	          "ranking": "df ≈ emb ≈ rand"
1186	        }
1187	      },
1188	      "pool_ranking_stable_pct": 62.5,
1189	      "ranking_crossover_threshold": "pool ≥ 200",
1190	      "absolute_R1_decline_per_10x_pool": 0.18
1191	    },
1192	    "tables": [
1193	      {
1194	        "name": "Table: R@1 by Pool Size × Strategy (Qwen)",
1195	        "columns": [
1196	          "Pool",
1197	          "Random",
1198	          "Embedding",
1199	          "Dataflow",
1200	          "Emb Δ (pp)",
1201	          "Ranking stable?"
1202	        ],
1203	        "rows": [
1204	          [
1205	            50,
1206	            0.53,
1207	            0.54,
1208	            0.532,
1209	            "+1.0",
1210	            "✓"
1211	          ],
1212	          [
1213	            100,
1214	            0.412,
1215	            0.421,
1216	            0.413,
1217	            "+0.9",
1218	            "✓"
1219	          ],
1220	          [
1221	            200,
1222	            0.328,
1223	            0.335,
1224	            0.33,
1225	            "+0.7",
1226	            "✓"
1227	          ],
1228	          [
1229	            500,
1230	            0.241,
1231	            0.246,
1232	            0.244,
1233	            "+0.5",
1234	            "✓"
1235	          ]
1236	        ]
1237	      },
1238	      {
1239	        "name": "Table: R@1 by Pool Size × Strategy (StarCoder)",
1240	        "columns": [
1241	          "Pool",
1242	          "Random",
1243	          "Embedding",
1244	          "Dataflow",
1245	          "Emb Δ (pp)",
1246	          "Ranking stable?"
1247	        ],
1248	        "rows": [
1249	          [
1250	            50,
1251	            0.443,
1252	            0.45,
1253	            0.437,
1254	            "+0.7",
1255	            "✓"
1256	          ],
1257	          [
1258	            100,
1259	            0.339,
1260	            0.345,
1261	            0.334,
1262	            "+0.6",
1263	            "✓"
1264	          ],
1265	          [
1266	            200,
1267	            0.268,
1268	            0.272,
1269	            0.271,
1270	            "+0.4",
1271	            "~"
1272	          ],
1273	          [
1274	            500,
1275	            0.194,
1276	            0.196,
1277	            0.197,
1278	            "+0.2",
1279	            "✗"
1280	          ]
1281	        ]
1282	      }
1283	    ],
1284	    "figures": [],
1285	    "analysis": "Pool size sensitivity 是 median 档下最重要的 external validity check。结果显示 embedding mining 优势 real 但 diminishing with pool size。论文需要 honestly discuss：(1) pool=50 是 validation setup，real-world repo pool 通常 200-1000+， (2) at realistic pool sizes the advantage shrinks to ~0.5pp。这强化了 \"systematic study\" 而非 \"strong method contribution\" 的 positioning。建议在 main paper 中报告 pool=50 和 pool=200 的双 benchmark，并在 limitation 中讨论 pool=500 的 convergence。\n\nPool size 增大时所有 strategies 的 absolute R@1 大幅下降（从 pool=50 的 ~53% 到 pool=500 的 ~24%），因为 retrieval 的 baseline difficulty 增加。Strategy delta 也随 pool 增大而压缩：pool=50 时 embedding delta=+1.0pp，pool=500 时仅 +0.5pp。 原因是大 pool 中 distractors 更 diverse，training-time 的 hard negative strategy 只 prepare 了模型应对特定 difficulty 分布，但 pool=500 时 test-time 的 difficulty distribution 超出了 training-time 的 coverage。在 pool ≥ 200 时偶有 ranking 交叉（StarCoder pool=500 时 dataflow 反超 embedding by 0.1pp），但差异在 noise range 内。Overall ranking stability 62.5%（8 个 encoder×pool 组合中 5 个保持 embedding > rest），低于 best 档的 >80% 但高于 worst 档的 <50%。这说明 finding \"directionally holds but weakens\" at larger pools，需在论文中 caveat。\n"
1286	  }
1287	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4329bda-6761-4241-9c85-e37f00d71347",
  "isSidechain": false,
  "promptId": "2a7bf294-76bc-4051-b2db-b0a0f92c173c",
  "type": "user",
  "uuid": "58373308-991b-4f3c-b0ec-bf8060e72a31",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"SWE-bench Lite End-to-End Evaluation\",\n    \"description\": \"3 strategies × best checkpoint (Qwen), Qwen3.6-27B agent, 300 SWE-bench Lite instances\",\n    \"results\": {\n      \"random_resolve_rate_pct\": 23.0,\n      \"random_resolved_count\": 69,\n      \"embedding_resolve_rate_pct\": 23.7,\n      \"embedding_resolved_count\": 71,\n      \"dataflow_resolve_rate_pct\": 23.3,\n      \"dataflow_resolved_count\": 70,\n      \"emb_minus_random_delta_pp\": 0.7,\n      \"df_minus_random_delta_pp\": 0.3,\n      \"total_instances\": 300,\n      \"retrieval_R1_on_swebench_random\": 0.41,\n      \"retrieval_R1_on_swebench_embedding\": 0.42,\n      \"retrieval_R1_on_swebench_dataflow\": 0.41\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: SWE-bench Lite Resolve Rate by Strategy\",\n        \"columns\": [\n          \"Strategy\",\n          \"Resolved\",\n          \"Total\",\n          \"Rate (%)\",\n          \"Δ vs Random (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"random\",\n            69,\n            300,\n            23.0,\n            \"—\"\n          ],\n          [\n            \"embedding\",\n            71,\n            300,\n            23.7,\n            \"+0.7\"\n          ],\n          [\n            \"dataflow\",\n            70,\n            300,\n            23.3,\n            \"+0.3\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Retrieval-Stage R@1 on SWE-bench Repos\",\n        \"columns\": [\n          \"Strategy\",\n          \"R@1\",\n          \"R@5\"\n        ],\n        \"rows\": [\n          [\n            \"random\",\n            0.41,\n            0.78\n          ],\n          [\n            \"embedding\",\n            0.42,\n            0.79\n          ],\n          [\n            \"dataflow\",\n            0.41,\n            0.78\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SWE-bench delta 不足以支撑独立 claim。resolve rate 差异 < 1pp，在 N=300 上无统计 显著性（见 plan_016）。Retrieval-stage R@1 差异同样微小（~1pp），说明 SWE-smith 到 SWE-bench 的 domain gap 进一步压平了 strategy 差异。论文中应作为 \\\"sanity check\\\" 而非 primary evidence 呈现：确认 negative mining 策略不 harm downstream performance， 但不能 claim 显著 improvement。需在 limitation 中讨论 300 instances 的 power 不足问题。\\n\\n\\nSWE-bench Lite 的 resolve rate 由 agent 生成能力主导，retrieval 只是 pipeline 的第一步。median 档下 retrieval R@1 delta 仅 ~1pp，传导到 end-to-end 后进一步 衰减：即使 retrieval 多找对 1-2 个 file，agent 是否能利用这个 file 生成正确 patch 是独立的噪声源。300 instances 上 2 个 count 的差异对应 ~0.7pp，远不够 statistical significance。此外 SWE-bench 的 repo 分布与 SWE-smith training 分布有 domain shift， 进一步压缩了 retrieval improvement 的传导效率。\\n\"\n  },\n  {\n    \"name\": \"RepoBench-R Cross-File Retrieval Evaluation\",\n    \"description\": \"3 strategies × 3 seeds × 2 encoders, RepoBench-R test_easy (8K, pool~6) + test_hard (8K, pool~18), with 95% CIs\",\n    \"results\": {\n      \"qwen_test_easy\": {\n        \"random_R1_mean\": 0.682,\n        \"embedding_R1_mean\": 0.688,\n        \"dataflow_R1_mean\": 0.685,\n        \"emb_minus_random_pp\": 0.6,\n        \"emb_minus_random_CI\": [\n          -0.2,\n          1.4\n        ]\n      },\n      \"qwen_test_hard\": {\n        \"random_R1_mean\": 0.394,\n        \"embedding_R1_mean\": 0.404,\n        \"dataflow_R1_mean\": 0.398,\n        \"emb_minus_random_pp\": 1.0,\n        \"emb_minus_random_CI\": [\n          -0.1,\n          2.1\n        ]\n      },\n      \"starcoder_test_easy\": {\n        \"random_R1_mean\": 0.621,\n        \"embedding_R1_mean\": 0.626,\n        \"dataflow_R1_mean\": 0.618,\n        \"emb_minus_random_pp\": 0.5,\n        \"emb_minus_random_CI\": [\n          -0.3,\n          1.3\n        ]\n      },\n      \"starcoder_test_hard\": {\n        \"random_R1_mean\": 0.338,\n        \"embedding_R1_mean\": 0.346,\n        \"dataflow_R1_mean\": 0.333,\n        \"emb_minus_random_pp\": 0.8,\n        \"emb_minus_random_CI\": [\n          -0.4,\n          2.0\n        ]\n      },\n      \"overall_delta_pp_range\": [\n        0.0,\n        1.5\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: RepoBench-R R@1 by Strategy × Encoder × Difficulty\",\n        \"columns\": [\n          \"Encoder\",\n          \"Split\",\n          \"Random\",\n          \"Embedding\",\n          \"Dataflow\",\n          \"Emb Δ (pp)\",\n          \"DF Δ (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen\",\n            \"easy\",\n            \"68.2 ± 0.7\",\n            \"68.8 ± 0.8\",\n            \"68.5 ± 0.9\",\n            \"+0.6\",\n            \"+0.3\"\n          ],\n          [\n            \"Qwen\",\n            \"hard\",\n            \"39.4 ± 1.0\",\n            \"40.4 ± 1.1\",\n            \"39.8 ± 1.2\",\n            \"+1.0\",\n            \"+0.4\"\n          ],\n          [\n            \"StarCoder\",\n            \"easy\",\n            \"62.1 ± 0.6\",\n            \"62.6 ± 0.7\",\n            \"61.8 ± 0.8\",\n            \"+0.5\",\n            \"−0.3\"\n          ],\n          [\n            \"StarCoder\",\n            \"hard\",\n            \"33.8 ± 0.9\",\n            \"34.6 ± 1.0\",\n            \"33.3 ± 1.1\",\n            \"+0.8\",\n            \"−0.5\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"RepoBench-R 提供了 second benchmark 覆盖，方向一致（embedding ≥ random > dataflow on StarCoder），但 effect size 不足以独立支撑 claim。test_hard 上的 delta 稍大， 说明 pool size 对 strategy 效果有调节作用（与 plan_019 呼应）。论文中报告为 \\\"directional consistency across benchmarks\\\" 而非 \\\"significant improvement on second benchmark\\\"。CIs 需在 Table 中完整展示以示 transparency。\\n\\n\\nRepoBench-R 的 test_easy pool 仅 ~6 candidates，所有策略接近 ceiling，strategy 差异被压缩到 < 1pp。test_hard pool ~18 提供更多区分空间，delta 稍大（~1pp）但仍在 CI 包含 0 的边缘。RepoBench-R 与 SWE-smith 的 task 定义不同（cross-file completion vs bug-fix retrieval），domain shift 进一步削弱了 training-time strategy 差异的 传导。8K instances 的大样本量使 per-strategy CI 较窄（~1.5pp width），但 delta 的 CI 仍 ~2pp width，因为 strategy 间的 paired variance 较大。Dataflow 在 StarCoder 上一致为负（-0.5pp），符合 pilot 发现的 encoder-strategy interaction pattern。\\n\"\n  },\n  {\n    \"name\": \"Stratified Retrieval Analysis (5 Strata)\",\n    \"description\": \"分层分析：repo size / pool size / query-pos similarity / structural data availability / neg_difficulty quartile\",\n    \"results\": {\n      \"stratum_1_repo_size\": {\n        \"small_lt50_emb_delta_pp\": 1.8,\n        \"medium_50_200_emb_delta_pp\": 1.2,\n        \"large_200_500_emb_delta_pp\": 0.6,\n        \"xlarge_500plus_emb_delta_pp\": 0.4\n      },\n      \"stratum_2_pool_size\": {\n        \"pool_lt10_emb_delta_pp\": 0.3,\n        \"pool_10_50_emb_delta_pp\": 1.1,\n        \"pool_50plus_emb_delta_pp\": 0.7\n      },\n      \"stratum_3_query_pos_sim\": {\n        \"high_sim_gt098_emb_delta_pp\": 0.5,\n        \"medium_sim_090_098_emb_delta_pp\": 1.3,\n        \"low_sim_lt090_emb_delta_pp\": 1.0\n      },\n      \"stratum_4_structural_availability\": {\n        \"with_dataflow_34pct\": {\n          \"random_R1\": 0.538,\n          \"embedding_R1\": 0.548,\n          \"dataflow_R1\": 0.544,\n          \"df_minus_random_pp\": 0.6,\n          \"emb_minus_random_pp\": 1.0\n        },\n        \"fallback_66pct\": {\n          \"random_R1\": 0.526,\n          \"embedding_R1\": 0.536,\n          \"dataflow_R1\": 0.527,\n          \"df_minus_random_pp\": 0.1,\n          \"emb_minus_random_pp\": 1.0\n        }\n      },\n      \"stratum_5_neg_difficulty_quartile\": {\n        \"Q1_easiest\": {\n          \"emb_delta_pp\": 0.3,\n          \"df_delta_pp\": -0.2\n        },\n        \"Q2\": {\n          \"emb_delta_pp\": 0.8,\n          \"df_delta_pp\": 0.1\n        },\n        \"Q3\": {\n          \"emb_delta_pp\": 1.4,\n          \"df_delta_pp\": 0.5\n        },\n        \"Q4_hardest\": {\n          \"emb_delta_pp\": 1.6,\n          \"df_delta_pp\": 1.2\n        }\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Embedding Delta by Repo Size Stratum (Qwen)\",\n        \"columns\": [\n          \"Stratum\",\n          \"N instances\",\n          \"Random R@1\",\n          \"Emb R@1\",\n          \"Δ (pp)\",\n          \"95% CI\"\n        ],\n        \"rows\": [\n          [\n            \"small (<50)\",\n            500,\n            0.571,\n            0.589,\n            \"+1.8\",\n            \"[-0.5, 4.1]\"\n          ],\n          [\n            \"medium (50-200)\",\n            4096,\n            0.542,\n            0.554,\n            \"+1.2\",\n            \"[0.0, 2.4]\"\n          ],\n          [\n            \"large (200-500)\",\n            13628,\n            0.531,\n            0.537,\n            \"+0.6\",\n            \"[-0.3, 1.5]\"\n          ],\n          [\n            \"xlarge (500+)\",\n            25949,\n            0.524,\n            0.528,\n            \"+0.4\",\n            \"[-0.5, 1.3]\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Strategy Delta by Structural Data Availability (Qwen)\",\n        \"columns\": [\n          \"Stratum\",\n          \"N\",\n          \"Random R@1\",\n          \"Emb R@1\",\n          \"DF R@1\",\n          \"Emb Δ\",\n          \"DF Δ\"\n        ],\n        \"rows\": [\n          [\n            \"with dataflow (34%)\",\n            \"~15K\",\n            0.538,\n            0.548,\n            0.544,\n            \"+1.0\",\n            \"+0.6\"\n          ],\n          [\n            \"fallback (66%)\",\n            \"~29K\",\n            0.526,\n            0.536,\n            0.527,\n            \"+1.0\",\n            \"+0.1\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Strategy Delta by Neg Difficulty Quartile (Qwen)\",\n        \"columns\": [\n          \"Quartile\",\n          \"Margin range\",\n          \"Emb Δ (pp)\",\n          \"DF Δ (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"Q1 (easiest)\",\n            \"> 0.15\",\n            \"+0.3\",\n            \"−0.2\"\n          ],\n          [\n            \"Q2\",\n            \"0.08–0.15\",\n            \"+0.8\",\n            \"+0.1\"\n          ],\n          [\n            \"Q3\",\n            \"0.02–0.08\",\n            \"+1.4\",\n            \"+0.5\"\n          ],\n          [\n            \"Q4 (hardest)\",\n            \"< 0.02\",\n            \"+1.6\",\n            \"+1.2\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"分层分析揭示了 effect size heterogeneity：embedding mining 在 small repo / high difficulty / medium similarity 条件下效果最好，但这些条件在实际分布中占比小。 Structural availability 分层确认了 dataflow 的 conditional benefit 完全来自有 structural data 的 34%（delta +0.6pp），fallback 的 66% 贡献为零。这解释了为什么 overall dataflow delta 被 dilute 到接近 0。Neg difficulty quartile 分析提供了 最清晰的 mechanistic story：当 negatives 足够 hard（Q4），both strategies help； 当 negatives 太 easy（Q1），neither helps much。这支持 representation geometry explanation 但 effect size 不足以作为独立 claim。\\n\\n\\nRepo size 分层：小 repo 的 pool 小、diversity 低，embedding mining 更容易找到有意义 的 hard negatives，所以 delta 最大。大 repo 中 pool 大但 noise 也大（更多 unrelated files），embedding mining 优势被稀释。Pool size 分层与 repo size 部分共线但不完全： pool < 10 时 all strategies 接近 ceiling 所以 delta 小；pool 10-50 是 sweet spot； pool 50+ 时 noise 增加。Query-pos similarity 分层：high sim (> 0.98，Qwen 主导) 表明 representation 已饱和，embedding negatives 不够 hard，delta 小；medium sim 区间 embedding mining 最 effective。Structural availability 分层：34% 有 dataflow 数据的 instances 上 dataflow strategy 有 +0.6pp 优势（真正用到了 structural signal）， 但 66% fallback instances 上 dataflow ≈ random（因为 fallback 到 random sampling）， 整体被 dilute。Neg difficulty quartile：Q4（最难 negatives）时 embedding 和 dataflow 都 help 最多，因为这些 cases 正是模型最 confuse 的地方，harder negatives 提供最大 gradient signal。但 Q1-Q2 占比大，dilute 了整体 effect。\\n\"\n  },\n  {\n    \"name\": \"Call-Graph Hop-Count Ablation\",\n    \"description\": \"1-hop vs 2-hop vs 3-hop call-graph bounding for dataflow negative selection\",\n    \"results\": {\n      \"qwen_1hop_df_R1\": 0.53,\n      \"qwen_2hop_df_R1\": 0.532,\n      \"qwen_3hop_df_R1\": 0.529,\n      \"starcoder_1hop_df_R1\": 0.434,\n      \"starcoder_2hop_df_R1\": 0.437,\n      \"starcoder_3hop_df_R1\": 0.436,\n      \"qwen_2hop_minus_1hop_pp\": 0.2,\n      \"qwen_2hop_minus_3hop_pp\": 0.3,\n      \"eligible_negatives_per_query\": {\n        \"hop_1\": 3.2,\n        \"hop_2\": 8.7,\n        \"hop_3\": 14.1\n      },\n      \"fallback_to_random_pct\": {\n        \"hop_1\": 42,\n        \"hop_2\": 28,\n        \"hop_3\": 18\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Dataflow R@1 by Hop Count\",\n        \"columns\": [\n          \"Encoder\",\n          \"1-hop\",\n          \"2-hop\",\n          \"3-hop\",\n          \"Best\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen\",\n            0.53,\n            0.532,\n            0.529,\n            \"2-hop\"\n          ],\n          [\n            \"StarCoder\",\n            0.434,\n            0.437,\n            0.436,\n            \"2-hop\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Negative Pool Statistics by Hop Count\",\n        \"columns\": [\n          \"Hops\",\n          \"Mean eligible neg/query\",\n          \"Fallback-to-random %\"\n        ],\n        \"rows\": [\n          [\n            1,\n            3.2,\n            \"42%\"\n          ],\n          [\n            2,\n            8.7,\n            \"28%\"\n          ],\n          [\n            3,\n            14.1,\n            \"18%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"2-hop 作为默认设置是合理的，但 ablation signal 太弱（< 0.5pp）无法 claim hop count 是 critical design choice。放入 appendix 作为 hyperparameter justification 即可。 更重要的 takeaway 是 1-hop 的 high fallback rate（42%），说明 inter-procedural dataflow 的 coverage 本身就有限——这与 plan_005 structural availability 分层的 34% 数字一致。\\n\\n\\n1-hop 限制太严格：平均每 query 只有 3.2 个 eligible dataflow-disconnected negatives， 42% 的 queries 不得不 fallback 到 random，稀释了 structural signal。2-hop 是 precision-recall sweet spot：8.7 eligible negatives 足够采样，fallback 率降到 28%。 3-hop 进一步扩大 candidate pool 但引入 semantically distant files（3-hop 以外的 files 很可能本来就和 query 无关），负 signal 质量下降，反而略差于 2-hop。但三者 差异均 < 0.5pp，在 noise range 内，不构成 strong ablation signal。这也反映了 median 档下 dataflow strategy 本身 effect size 就小，hop-count 作为 second-order effect 自然更小。\\n\"\n  },\n  {\n    \"name\": \"Training Data Size Scaling\",\n    \"description\": \"1K vs 3K vs 5K training instances × 3 strategies, Qwen encoder\",\n    \"results\": {\n      \"qwen_1K\": {\n        \"random_R1\": 0.498,\n        \"embedding_R1\": 0.501,\n        \"dataflow_R1\": 0.495,\n        \"emb_delta_pp\": 0.3\n      },\n      \"qwen_3K\": {\n        \"random_R1\": 0.519,\n        \"embedding_R1\": 0.528,\n        \"dataflow_R1\": 0.521,\n        \"emb_delta_pp\": 0.9\n      },\n      \"qwen_5K\": {\n        \"random_R1\": 0.53,\n        \"embedding_R1\": 0.54,\n        \"dataflow_R1\": 0.532,\n        \"emb_delta_pp\": 1.0\n      },\n      \"scaling_slope_R1_per_1K\": 0.008\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: R@1 by Data Size × Strategy (Qwen)\",\n        \"columns\": [\n          \"Size\",\n          \"Random\",\n          \"Embedding\",\n          \"Dataflow\",\n          \"Emb Δ (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"1K\",\n            0.498,\n            0.501,\n            0.495,\n            \"+0.3\"\n          ],\n          [\n            \"3K\",\n            0.519,\n            0.528,\n            0.521,\n            \"+0.9\"\n          ],\n          [\n            \"5K (full)\",\n            0.53,\n            0.54,\n            0.532,\n            \"+1.0\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Data scaling 是 positive signal：说明 embedding mining 的 benefit 不是 overfitting artifact（否则小数据时 delta 应更大）。但 sub-linear scaling 和 5K 时仍只有 +1.0pp 的 delta 说明 pretrained representation quality 是 bottleneck，更多 data 不会 dramatically 改变 strategy ranking。适合放入 appendix，支撑 \\\"mining benefit is real but modest\\\" 的 narrative。\\n\\n\\n1K instances 时所有策略都 underfit：training data 不足以让 contrastive loss 充分 学习，absolute R@1 低（~0.50）。Embedding mining 在 1K 时优势最小（+0.3pp）， 因为 1K instances 中 embedding-distance 的 top-k negatives 覆盖了 corpus 的较小 subset，mining quality 受限于 candidate pool diversity。3K 到 5K 的 scaling 呈 sub-linear 增长（+1.1pp absolute from 3K→5K vs +2.1pp from 1K→3K），说明 returns diminishing。Strategy delta 的 scaling 也 sub-linear：embedding 优势在 3K 时已接近 5K 水平。这表明 effect size 的上限由 pretrained representation quality 决定，不会随 data 无限增大。\\n\"\n  },\n  {\n    \"name\": \"Fusion Head Ablation\",\n    \"description\": \"Embedding-only vs structural-features-only vs combined scoring head\",\n    \"results\": {\n      \"qwen_embedding_only_R1\": 0.539,\n      \"qwen_structural_only_R1\": 0.412,\n      \"qwen_combined_R1\": 0.541,\n      \"starcoder_embedding_only_R1\": 0.449,\n      \"starcoder_structural_only_R1\": 0.378,\n      \"starcoder_combined_R1\": 0.451,\n      \"combined_minus_embedding_only_pp\": 0.2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Fusion Head Ablation R@1\",\n        \"columns\": [\n          \"Encoder\",\n          \"Emb-only\",\n          \"Struct-only\",\n          \"Combined\",\n          \"Combined−Emb (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen\",\n            0.539,\n            0.412,\n            0.541,\n            \"+0.2\"\n          ],\n          [\n            \"StarCoder\",\n            0.449,\n            0.378,\n            0.451,\n            \"+0.2\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"确认 StructFuse 的 value 在 training-time negative selection 而非 inference-time feature fusion。Combined head 的 marginal gain 可能不值得 inference-time 的 CodeQL dependency。论文中作为 appendix ablation，支撑 \\\"negative selection is the key mechanism\\\" 的 argument。\\n\\n\\nStructural-features-only（仅用 dataflow connectivity、call-graph distance 等 discrete features）大幅落后，因为 binary/categorical structural features 的 信息量远不及 dense embedding。Combined head 相比 embedding-only 仅 +0.2pp， 因为在 median 档下 structural signal 本身就弱（plan_005 已示），fusion 无法 从弱 signal 中 extract 出更多 information。这说明 structural information 的 value 主要体现在 negative selection（training time）而非 scoring（inference time）。\\n\"\n  },\n  {\n    \"name\": \"Dataflow-Distance Weighted vs Binary Negatives\",\n    \"description\": \"Weighted sampling by dataflow distance vs binary connected/disconnected\",\n    \"results\": {\n      \"qwen_binary_df_R1\": 0.532,\n      \"qwen_weighted_df_R1\": 0.535,\n      \"starcoder_binary_df_R1\": 0.437,\n      \"starcoder_weighted_df_R1\": 0.439,\n      \"weighted_minus_binary_pp\": 0.3,\n      \"weighted_minus_binary_CI\": [\n        -0.8,\n        1.4\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Binary vs Weighted Dataflow Negatives\",\n        \"columns\": [\n          \"Encoder\",\n          \"Binary DF R@1\",\n          \"Weighted DF R@1\",\n          \"Δ (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen\",\n            0.532,\n            0.535,\n            \"+0.3\"\n          ],\n          [\n            \"StarCoder\",\n            0.437,\n            0.439,\n            \"+0.2\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Effect 太小，不值得增加 pipeline complexity。Binary 作为默认 simple choice 是合理的。 放入 appendix 一句话即可。\\n\\n\\nDistance-weighted sampling 理论上应该更好：给距离更远（更 disconnected）的 negatives 更高采样概率，提供更 clean 的 structural signal。但在 median 档下 dataflow strategy 本身 effect size 就小，在此基础上的 second-order refinement 自然更小（+0.3pp），CI 宽且包含 0。实际上 binary 和 weighted 的差异主要来自 少数 outlier queries（dataflow distance 分布高度 skewed），大多数 queries 的 negatives 在两种 scheme 下 overlap 很大。\\n\"\n  },\n  {\n    \"name\": \"SWE-bench Failure Analysis\",\n    \"description\": \"50 SweRank/BM25 failures, categorize by whether dataflow helps\",\n    \"results\": {\n      \"total_failures_analyzed\": 50,\n      \"category_structural_gap\": 14,\n      \"category_lexical_gap\": 18,\n      \"category_multi_file_dependency\": 8,\n      \"category_other\": 10,\n      \"df_helps_in_structural_gap_pct\": 57,\n      \"df_helps_overall_pct\": 28,\n      \"emb_helps_overall_pct\": 36\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Failure Category Distribution\",\n        \"columns\": [\n          \"Category\",\n          \"Count\",\n          \"%\",\n          \"DF helps\",\n          \"Emb helps\"\n        ],\n        \"rows\": [\n          [\n            \"Structural gap\",\n            14,\n            \"28%\",\n            \"8 (57%)\",\n            \"5 (36%)\"\n          ],\n          [\n            \"Lexical gap\",\n            18,\n            \"36%\",\n            \"3 (17%)\",\n            \"6 (33%)\"\n          ],\n          [\n            \"Multi-file dependency\",\n            8,\n            \"16%\",\n            \"4 (50%)\",\n            \"5 (63%)\"\n          ],\n          [\n            \"Other\",\n            10,\n            \"20%\",\n            \"1 (10%)\",\n            \"2 (20%)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Failure analysis 提供了 qualitative evidence 支撑 \\\"structural signal helps in specific conditions\\\" 的 narrative，但也暴露了 ceiling：真正 structural gap 的 cases 只占 28%，coverage 限制了其中一半。适合放入 Section 5 的 analysis 段落， 不足以 support independent claim。\\n\\n\\n50 个 failure cases 中，仅 14 个（28%）属于 structural gap（即 gold file 与 query 有 dataflow 关系但无 lexical similarity）。在这 14 个中，dataflow strategy 成功 retrieve 了 8 个（57%），但剩余 6 个仍然 fail 因为 structural data 不覆盖（34% coverage limitation）。最大的 failure category 是 lexical gap（36%，query 描述 与 target file 用语完全不同），这两种 strategy 都无法解决。这解释了为什么 overall effect size 小：真正 benefit from structural signal 的 cases 只占 ~28%，且其中 仍有近半 coverage 不足。\\n\"\n  },\n  {\n    \"name\": \"Qualitative Case Studies\",\n    \"description\": \"5-10 cases where structural negatives changed retrieval outcome\",\n    \"results\": {\n      \"total_cases_selected\": 7,\n      \"cases_df_uniquely_helps\": 3,\n      \"cases_emb_uniquely_helps\": 2,\n      \"cases_both_help\": 2,\n      \"avg_gold_rank_improvement_df\": 4.2,\n      \"avg_gold_rank_improvement_emb\": 2.8\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Selected Qualitative Cases\",\n        \"columns\": [\n          \"Case\",\n          \"Repo\",\n          \"Issue type\",\n          \"Random rank\",\n          \"Emb rank\",\n          \"DF rank\",\n          \"Key observation\"\n        ],\n        \"rows\": [\n          [\n            1,\n            \"repo_A\",\n            \"missing import\",\n            12,\n            8,\n            2,\n            \"DF finds cross-module callee\"\n          ],\n          [\n            2,\n            \"repo_B\",\n            \"API mismatch\",\n            9,\n            3,\n            4,\n            \"Emb finds similar naming\"\n          ],\n          [\n            3,\n            \"repo_C\",\n            \"config propagation\",\n            15,\n            11,\n            1,\n            \"DF traces config flow\"\n          ],\n          [\n            4,\n            \"repo_D\",\n            \"type error\",\n            6,\n            2,\n            3,\n            \"Both find related types\"\n          ],\n          [\n            5,\n            \"repo_E\",\n            \"null pointer\",\n            11,\n            7,\n            3,\n            \"DF finds data source\"\n          ],\n          [\n            6,\n            \"repo_F\",\n            \"method override\",\n            4,\n            1,\n            5,\n            \"Emb captures signature sim\"\n          ],\n          [\n            7,\n            \"repo_G\",\n            \"circular dep\",\n            14,\n            10,\n            2,\n            \"DF traces dependency cycle\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Qualitative examples 是论文的 illustration 而非 evidence。选择具有 pedagogical value 的 cases 来解释 mechanism。在 median 档下，需要 caveat \\\"these are selected to illustrate the mechanism; overall effect size is modest (Table X)\\\"。\\n\\n\\nCherry-picking 7 个 illustrative cases。3 个 cases 中 dataflow strategy 将 gold file 从 rank 8-15 提升到 rank 1-3（大幅改善），这些 cases 的共同特征是 gold file 与 query 有 call-chain dependency 但无 keyword overlap。2 个 cases 中 embedding strategy 独特帮助（gold file 与 query 有 similar variable naming 但 random negatives 中缺少 near-miss distractors）。但 cherry-picked cases 不代表 overall distribution（见 plan_011 的 28% structural gap rate）。\\n\"\n  },\n  {\n    \"name\": \"Temperature Ablation\",\n    \"description\": \"τ ∈ {0.05, 0.1, 0.2} × 3 strategies × 2 encoders\",\n    \"results\": {\n      \"qwen\": {\n        \"tau_005\": {\n          \"random_R1\": 0.53,\n          \"embedding_R1\": 0.54,\n          \"dataflow_R1\": 0.532,\n          \"emb_delta_pp\": 1.0\n        },\n        \"tau_010\": {\n          \"random_R1\": 0.537,\n          \"embedding_R1\": 0.545,\n          \"dataflow_R1\": 0.537,\n          \"emb_delta_pp\": 0.8\n        },\n        \"tau_020\": {\n          \"random_R1\": 0.521,\n          \"embedding_R1\": 0.526,\n          \"dataflow_R1\": 0.52,\n          \"emb_delta_pp\": 0.5\n        }\n      },\n      \"starcoder\": {\n        \"tau_005\": {\n          \"random_R1\": 0.443,\n          \"embedding_R1\": 0.45,\n          \"dataflow_R1\": 0.437,\n          \"emb_delta_pp\": 0.7\n        },\n        \"tau_010\": {\n          \"random_R1\": 0.451,\n          \"embedding_R1\": 0.457,\n          \"dataflow_R1\": 0.446,\n          \"emb_delta_pp\": 0.6\n        },\n        \"tau_020\": {\n          \"random_R1\": 0.435,\n          \"embedding_R1\": 0.438,\n          \"dataflow_R1\": 0.43,\n          \"emb_delta_pp\": 0.3\n        }\n      },\n      \"optimal_tau\": 0.1,\n      \"strategy_ranking_preserved_across_tau\": true,\n      \"delta_shrinks_at_high_tau\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: R@1 by Temperature × Strategy (Qwen)\",\n        \"columns\": [\n          \"τ\",\n          \"Random\",\n          \"Embedding\",\n          \"Dataflow\",\n          \"Emb Δ (pp)\",\n          \"Best strat\"\n        ],\n        \"rows\": [\n          [\n            0.05,\n            0.53,\n            0.54,\n            0.532,\n            \"+1.0\",\n            \"embedding\"\n          ],\n          [\n            0.1,\n            0.537,\n            0.545,\n            0.537,\n            \"+0.8\",\n            \"embedding\"\n          ],\n          [\n            0.2,\n            0.521,\n            0.526,\n            0.52,\n            \"+0.5\",\n            \"embedding\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: R@1 by Temperature × Strategy (StarCoder)\",\n        \"columns\": [\n          \"τ\",\n          \"Random\",\n          \"Embedding\",\n          \"Dataflow\",\n          \"Emb Δ (pp)\",\n          \"Best strat\"\n        ],\n        \"rows\": [\n          [\n            0.05,\n            0.443,\n            0.45,\n            0.437,\n            \"+0.7\",\n            \"embedding\"\n          ],\n          [\n            0.1,\n            0.451,\n            0.457,\n            0.446,\n            \"+0.6\",\n            \"embedding\"\n          ],\n          [\n            0.2,\n            0.435,\n            0.438,\n            0.43,\n            \"+0.3\",\n            \"embedding\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Temperature ablation 提供两个 key findings：(1) strategy ranking 在 τ 范围内 preserved（robustness check passed），(2) optimal τ 可能是 0.1 而非 0.05，但在 optimal τ 下 embedding delta 只有 0.6-0.8pp。这要求论文报告 best-τ 结果时 acknowledge effect size 进一步缩小。建议报告 τ=0.05 作为 primary（与 prior work 对齐）加 τ sensitivity 在 appendix。如果 reviewer 质疑 regime-specificity， 可以 argue ranking preserved 但 concede magnitude is τ-dependent。\\n\\n\\nτ=0.05（当前默认）可能过低：contrastive loss 的 gradient 过于 sharp，模型对 hard negatives 过度 sensitive，导致 overfitting（plan_002 中 step 500 后即 overfit）。 τ=0.1 在 median 档下反而略好：gradient 更 smooth，模型更 robust，absolute R@1 比 τ=0.05 高 ~0.7pp（Qwen）和 ~0.8pp（StarCoder）。但 strategy delta 在 τ=0.1 时略小（0.8pp vs 1.0pp Qwen），因为 smoother gradient 也 smooth 掉了 hard negative 的 extra signal。τ=0.2 过高：loss landscape 太 flat，training signal 不足， all strategies 退化。关键发现：strategy ranking（embedding > random ≥ dataflow） 在所有 τ 下保持一致，说明 finding 不是 regime-specific。但 delta 随 τ 增大而 缩小，表明在 optimal τ 下 effect size 可能更小。这是 median 档的典型 pattern： finding 方向 robust 但 magnitude 依赖 hyperparameter。\\n\"\n  },\n  {\n    \"name\": \"Dynamic vs Static Embedding Mining\",\n    \"description\": \"Dynamic re-mine embedding negatives per epoch vs static (mine once from pretrained), Qwen encoder\",\n    \"results\": {\n      \"qwen_static_emb_R1\": 0.54,\n      \"qwen_dynamic_emb_R1\": 0.544,\n      \"dynamic_minus_static_pp\": 0.4,\n      \"dynamic_minus_static_CI\": [\n        -0.8,\n        1.6\n      ],\n      \"training_time_ratio_dynamic_vs_static\": 2.3\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Static vs Dynamic Embedding Mining (Qwen)\",\n        \"columns\": [\n          \"Mining\",\n          \"R@1\",\n          \"Δ vs static (pp)\",\n          \"Train time (h)\",\n          \"CI\"\n        ],\n        \"rows\": [\n          [\n            \"static\",\n            0.54,\n            \"—\",\n            7.5,\n            \"—\"\n          ],\n          [\n            \"dynamic\",\n            0.544,\n            \"+0.4\",\n            17.3,\n            \"[-0.8, 1.6]\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Dynamic mining 是 expensive 的 marginal improvement。论文中一句话 dismiss this confound：\\\"We additionally tested dynamic re-mining (per-epoch) and found no significant improvement over static mining (Δ=+0.4pp, p=0.38), likely because the encoder changes minimally over 2-3 epochs.\\\"\\n\\n\\nDynamic mining 每个 epoch 用 current encoder 重新计算 embeddings 并 re-mine negatives，理论上 negatives 始终 adaptive to current model state。但在 median 档下 static mining 本身 effect size 就小（+1.0pp），dynamic 的 incremental gain 仅 +0.4pp，因为 (1) training 只跑 2-3 epochs，encoder 变化不大，re-mining 的 negatives 与 static 的 overlap 很大（estimated > 80% overlap），(2) dynamic mining 需要 per-epoch full-corpus encoding，training time 翻 2.3x，cost-benefit 不划算。CI 包含 0，说明 gain 不 significant。这个结果也部分缓解了 \\\"static mining confound\\\" 的 reviewer concern：dynamic 没有 dramatically 改变 picture。\\n\"\n  },\n  {\n    \"name\": \"Bootstrap CI for SWE-bench Resolve Rate\",\n    \"description\": \"95% bootstrap confidence intervals for all strategy comparisons on SWE-bench Lite\",\n    \"results\": {\n      \"n_bootstrap_samples\": 10000,\n      \"random_resolve_rate_pct\": 23.0,\n      \"random_CI\": [\n        18.3,\n        27.7\n      ],\n      \"embedding_resolve_rate_pct\": 23.7,\n      \"embedding_CI\": [\n        18.7,\n        28.3\n      ],\n      \"dataflow_resolve_rate_pct\": 23.3,\n      \"dataflow_CI\": [\n        18.3,\n        28.0\n      ],\n      \"emb_minus_random_delta_pp\": 0.7,\n      \"emb_minus_random_CI\": [\n        -3.2,\n        4.5\n      ],\n      \"emb_minus_random_p_value\": 0.62,\n      \"df_minus_random_delta_pp\": 0.3,\n      \"df_minus_random_CI\": [\n        -3.8,\n        4.4\n      ],\n      \"df_minus_random_p_value\": 0.78,\n      \"any_comparison_significant\": false\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: SWE-bench Bootstrap CIs\",\n        \"columns\": [\n          \"Comparison\",\n          \"Δ (pp)\",\n          \"95% CI\",\n          \"p-value\",\n          \"Significant?\"\n        ],\n        \"rows\": [\n          [\n            \"emb − random\",\n            \"+0.7\",\n            \"[-3.2, 4.5]\",\n            0.62,\n            \"No\"\n          ],\n          [\n            \"df − random\",\n            \"+0.3\",\n            \"[-3.8, 4.4]\",\n            0.78,\n            \"No\"\n          ],\n          [\n            \"emb − df\",\n            \"+0.3\",\n            \"[-3.5, 4.2]\",\n            0.73,\n            \"No\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SWE-bench CIs 确认 end-to-end evaluation 对 retrieval strategy 的 sensitivity 不足。这不是 negative result 而是 power limitation。论文中必须 transparently 报告 \\\"SWE-bench evaluation confirms no strategy harms downstream performance, but the benchmark is underpowered to detect the retrieval-stage deltas we observe (< 1pp)\\\"。Power analysis figure 可放入 appendix 支撑此 argument。\\n\\n\\nN=300 binary outcomes（resolve/not-resolve）的 bootstrap CI 很宽：individual strategy 的 CI width ~9.5pp，paired delta 的 CI width ~7.7pp。这是因为 binary outcome 的 variance 最大（Bernoulli variance = p(1-p) ≈ 0.18），300 instances 给出的 standard error ≈ sqrt(0.18/300) ≈ 0.024 = 2.4pp，95% CI ≈ ±4.7pp。 在 delta < 1pp 的情况下，不可能 achieve significance。这是 fundamental power limitation，不是方法问题。Even with 3000 instances (full SWE-bench)，delta 0.7pp 仍需要 N > 15000 才能 detect with 80% power。\\n\"\n  },\n  {\n    \"name\": \"Inference-Time Graph Method Literature Comparison\",\n    \"description\": \"Analysis-only comparison with CodexGraph, LocAgent, RANGER etc. (no experiment)\",\n    \"results\": {\n      \"papers_compared\": 8,\n      \"key_distinction\": \"training-time mining vs inference-time navigation\",\n      \"complementary_not_competing\": true,\n      \"overlap_with_our_approach\": \"minimal — they inject structure at inference, we use structure for training data curation\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Comparison with Inference-Time Graph Methods\",\n        \"columns\": [\n          \"Method\",\n          \"Graph type\",\n          \"When used\",\n          \"Scope\",\n          \"Complementary?\"\n        ],\n        \"rows\": [\n          [\n            \"CodexGraph\",\n            \"Repository graph\",\n            \"Inference\",\n            \"Navigation\",\n            \"Yes\"\n          ],\n          [\n            \"LocAgent\",\n            \"Code structure\",\n            \"Inference\",\n            \"Localization\",\n            \"Yes\"\n          ],\n          [\n            \"RANGER\",\n            \"AST + deps\",\n            \"Inference\",\n            \"Ranking\",\n            \"Yes\"\n          ],\n          [\n            \"StructFuse (ours)\",\n            \"Dataflow\",\n            \"Training\",\n            \"Neg mining\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Discussion section 需要明确 position StructFuse 为 complementary approach，not competing with inference-time methods。这也为 future work 提供了 natural extension： combine StructFuse-trained retriever with inference-time graph navigation。 Median 档下这是 speculative future work 而非 verified claim。\\n\\n\\n8 篇 inference-time graph 方法（CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG）都在 inference 时构建或查询 code graph。与 StructFuse 的区别是 fundamental：我们在 training time 用 graph 选 negatives，他们在 inference time 用 graph navigate。二者理论上 complementary（可以用 StructFuse 训练的 retriever 作为这些 inference-time methods 的 backbone）。但 median 档下我们 没有实验验证 complementarity，只能 argue in principle。这个 literature gap 在 前几轮 review 中被 flagged（best-R2-W5），written comparison 应该足够 address。\\n\"\n  },\n  {\n    \"name\": \"BM25 Hard Negative Baseline\",\n    \"description\": \"BM25-based hard negatives as 4th strategy, 1 seed × 2 encoders, compare with random/embedding/dataflow\",\n    \"results\": {\n      \"qwen_bm25_R1\": 0.521,\n      \"qwen_random_R1\": 0.53,\n      \"qwen_embedding_R1\": 0.54,\n      \"qwen_bm25_minus_random_pp\": -0.9,\n      \"qwen_bm25_minus_random_CI\": [\n        -2.8,\n        1.0\n      ],\n      \"qwen_bm25_minus_random_p_value\": 0.12,\n      \"starcoder_bm25_R1\": 0.436,\n      \"starcoder_random_R1\": 0.443,\n      \"starcoder_embedding_R1\": 0.45,\n      \"starcoder_bm25_minus_random_pp\": -0.7,\n      \"starcoder_bm25_minus_random_CI\": [\n        -2.5,\n        1.1\n      ],\n      \"starcoder_bm25_minus_random_p_value\": 0.18,\n      \"bm25_rank\": \"worst among 4 strategies\",\n      \"bm25_vs_embedding_delta_pp_qwen\": -1.9,\n      \"bm25_vs_embedding_delta_pp_starcoder\": -1.4\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: 4-Strategy Comparison R@1\",\n        \"columns\": [\n          \"Strategy\",\n          \"Qwen R@1\",\n          \"StarCoder R@1\",\n          \"Qwen Δ vs Random\",\n          \"StarCoder Δ vs Random\"\n        ],\n        \"rows\": [\n          [\n            \"random\",\n            0.53,\n            0.443,\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"embedding\",\n            0.54,\n            0.45,\n            \"+1.0\",\n            \"+0.7\"\n          ],\n          [\n            \"dataflow\",\n            0.532,\n            0.437,\n            \"+0.2\",\n            \"−0.6\"\n          ],\n          [\n            \"BM25\",\n            0.521,\n            0.436,\n            \"−0.9\",\n            \"−0.7\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: BM25 vs Embedding Delta (the CoCoHaNeRe gap)\",\n        \"columns\": [\n          \"Encoder\",\n          \"BM25 R@1\",\n          \"Emb R@1\",\n          \"Δ (pp)\",\n          \"CoCoHaNeRe reported\",\n          \"Our explanation\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen\",\n            0.521,\n            0.54,\n            \"−1.9\",\n            \"−27\",\n            \"Different mining protocol, pool size, pipeline robustness\"\n          ],\n          [\n            \"StarCoder\",\n            0.436,\n            0.45,\n            \"−1.4\",\n            \"n/a\",\n            \"Consistent direction, smaller magnitude\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"BM25 baseline 是 median 档下最重要的新增实验。它 partially 但不 fully closes the CoCoHaNeRe correction argument。方向一致（BM25 harm, embedding help）支撑了 \\\"proxy conflation\\\" 的 narrative，但 delta 太小（-0.9pp vs -27pp）且 p > 0.05 意味着 argument 需要 soften。论文叙事从 \\\"we prove CoCoHaNeRe was wrong\\\" 调整为 \\\"we observe that BM25-proxy negatives trend toward harm while true embedding negatives trend toward benefit, consistent with the hypothesis that CoCoHaNeRe's reported -27pp harm was amplified by proxy conflation and other uncontrolled factors\\\"。这是 median 档 framing 的核心转变。Need related work 深度对比 （ANCE, curriculum mining, DPR hard negatives）来 contextualize 为什么 effect size 在 code domain 普遍 modest。\\n\\n\\nBM25 negatives 是 lexical-similarity top-k，与 true embedding distance negatives 的 selection 方式 fundamentally 不同。BM25 top-k 主要 capture keyword overlap （function names, import statements），这些 \\\"negatives\\\" 中很多实际上是 semantically related（可能包含 false negatives / actual positives mislabeled as negatives）， 导致 noisy training signal。在 median 档下，BM25 harm 方向正确（-0.9pp Qwen, -0.7pp StarCoder），但 delta 小于 CoCoHaNeRe 报告的 -27pp。原因：(1) 我们的 training pipeline 更 robust（proper temperature, early stopping），(2) pool=50 限制了 BM25 negatives 的 \\\"hardness\\\"（不像 CoCoHaNeRe 的 full-corpus mining）。 p > 0.05 说明 harm 不 significant，but direction is consistent。这 partially closes the correction argument：可以 say \\\"BM25-proxy negatives harm in the direction CoCoHaNeRe reports, but the magnitude in our controlled setup is much smaller, suggesting their -27pp included other confounds beyond negative source\\\"。 不能 fully close（p > 0.05），只能 partially support。\\n\"\n  },\n  {\n    \"name\": \"Pool Size Sensitivity Analysis\",\n    \"description\": \"Strategy ranking stability at pool={50, 100, 200, 500} on SWE-smith validation\",\n    \"results\": {\n      \"qwen\": {\n        \"pool_50\": {\n          \"random_R1\": 0.53,\n          \"embedding_R1\": 0.54,\n          \"dataflow_R1\": 0.532,\n          \"ranking\": \"emb > df > rand\"\n        },\n        \"pool_100\": {\n          \"random_R1\": 0.412,\n          \"embedding_R1\": 0.421,\n          \"dataflow_R1\": 0.413,\n          \"ranking\": \"emb > df ≈ rand\"\n        },\n        \"pool_200\": {\n          \"random_R1\": 0.328,\n          \"embedding_R1\": 0.335,\n          \"dataflow_R1\": 0.33,\n          \"ranking\": \"emb > df ≈ rand\"\n        },\n        \"pool_500\": {\n          \"random_R1\": 0.241,\n          \"embedding_R1\": 0.246,\n          \"dataflow_R1\": 0.244,\n          \"ranking\": \"emb ≈ df ≈ rand\"\n        }\n      },\n      \"starcoder\": {\n        \"pool_50\": {\n          \"random_R1\": 0.443,\n          \"embedding_R1\": 0.45,\n          \"dataflow_R1\": 0.437,\n          \"ranking\": \"emb > rand > df\"\n        },\n        \"pool_100\": {\n          \"random_R1\": 0.339,\n          \"embedding_R1\": 0.345,\n          \"dataflow_R1\": 0.334,\n          \"ranking\": \"emb > rand > df\"\n        },\n        \"pool_200\": {\n          \"random_R1\": 0.268,\n          \"embedding_R1\": 0.272,\n          \"dataflow_R1\": 0.271,\n          \"ranking\": \"emb ≈ df ≈ rand\"\n        },\n        \"pool_500\": {\n          \"random_R1\": 0.194,\n          \"embedding_R1\": 0.196,\n          \"dataflow_R1\": 0.197,\n          \"ranking\": \"df ≈ emb ≈ rand\"\n        }\n      },\n      \"pool_ranking_stable_pct\": 62.5,\n      \"ranking_crossover_threshold\": \"pool ≥ 200\",\n      \"absolute_R1_decline_per_10x_pool\": 0.18\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: R@1 by Pool Size × Strategy (Qwen)\",\n        \"columns\": [\n          \"Pool\",\n          \"Random\",\n          \"Embedding\",\n          \"Dataflow\",\n          \"Emb Δ (pp)\",\n          \"Ranking stable?\"\n        ],\n        \"rows\": [\n          [\n            50,\n            0.53,\n            0.54,\n            0.532,\n            \"+1.0\",\n            \"✓\"\n          ],\n          [\n            100,\n            0.412,\n            0.421,\n            0.413,\n            \"+0.9\",\n            \"✓\"\n          ],\n          [\n            200,\n            0.328,\n            0.335,\n            0.33,\n            \"+0.7\",\n            \"✓\"\n          ],\n          [\n            500,\n            0.241,\n            0.246,\n            0.244,\n            \"+0.5\",\n            \"✓\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: R@1 by Pool Size × Strategy (StarCoder)\",\n        \"columns\": [\n          \"Pool\",\n          \"Random\",\n          \"Embedding\",\n          \"Dataflow\",\n          \"Emb Δ (pp)\",\n          \"Ranking stable?\"\n        ],\n        \"rows\": [\n          [\n            50,\n            0.443,\n            0.45,\n            0.437,\n            \"+0.7\",\n            \"✓\"\n          ],\n          [\n            100,\n            0.339,\n            0.345,\n            0.334,\n            \"+0.6\",\n            \"✓\"\n          ],\n          [\n            200,\n            0.268,\n            0.272,\n            0.271,\n            \"+0.4\",\n            \"~\"\n          ],\n          [\n            500,\n            0.194,\n            0.196,\n            0.197,\n            \"+0.2\",\n            \"✗\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Pool size sensitivity 是 median 档下最重要的 external validity check。结果显示 embedding mining 优势 real 但 diminishing with pool size。论文需要 honestly discuss：(1) pool=50 是 validation setup，real-world repo pool 通常 200-1000+， (2) at realistic pool sizes the advantage shrinks to ~0.5pp。这强化了 \\\"systematic study\\\" 而非 \\\"strong method contribution\\\" 的 positioning。建议在 main paper 中报告 pool=50 和 pool=200 的双 benchmark，并在 limitation 中讨论 pool=500 的 convergence。\\n\\nPool size 增大时所有 strategies 的 absolute R@1 大幅下降（从 pool=50 的 ~53% 到 pool=500 的 ~24%），因为 retrieval 的 baseline difficulty 增加。Strategy delta 也随 pool 增大而压缩：pool=50 时 embedding delta=+1.0pp，pool=500 时仅 +0.5pp。 原因是大 pool 中 distractors 更 diverse，training-time 的 hard negative strategy 只 prepare 了模型应对特定 difficulty 分布，但 pool=500 时 test-time 的 difficulty distribution 超出了 training-time 的 coverage。在 pool ≥ 200 时偶有 ranking 交叉（StarCoder pool=500 时 dataflow 反超 embedding by 0.1pp），但差异在 noise range 内。Overall ranking stability 62.5%（8 个 encoder×pool 组合中 5 个保持 embedding > rest），低于 best 档的 >80% 但高于 worst 档的 <50%。这说明 finding \\\"directionally holds but weakens\\\" at larger pools，需在论文中 caveat。\\n\"\n  }\n]",
      "numLines": 1287,
      "startLine": 1,
      "totalLines": 1287
    }
  },
  "sourceToolAssistantUUID": "e4329bda-6761-4241-9c85-e37f00d71347",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T16:50:10.425Z_

<details><summary>↩ Tool result · `toolu_01M4HckXTffqxy6heAUfjWKp`</summary>

```text
1	# Paper Framing — StructFuse
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main
5	- Deadline: ARR May 25, 2026
6	
7	## Core Claims (3)
8	
9	1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported "harm" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B).
10	
11	2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.
12	
13	3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]
14	
15	## Story Spine
16	
17	- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.
18	
19	- **Existing approaches & gaps**:
20	  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies
21	  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal
22	  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only
23	  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance
24	  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works
25	
26	- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.
27	
28	- **Headline result template**: "True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis."
29	
30	## Core Insight
31	
32	The effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.
33	
34	## Dual-Pillar Motivation
35	
36	1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.
37	2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.
38	
39	## Formal Definition
40	
41	Given retrieval domain D, structural graph G, similarity function s, query q:
42	**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)
43	
44	The structural graph is externally fixed and does not update with the encoder (drift-immune).
45	
46	## Title Options
47	
48	- Primary: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
49	- Alternative: "StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval"
50	- Backup: "Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally"
51	
52	## Venue Fit
53	
54	1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. "Do Language Models..." papers). Contribution is understanding, not just a new method.
55	2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.
56	3. **Against "incremental" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.
57	
58	## Anticipated Reviewer Concerns
59	
60	| Concern | Response | Evidence |
61	|---------|----------|----------|
62	| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |
63	| BM25 vs true embedding negatives? | Run BM25 negatives to empirically verify CoCoHaNeRe used BM25-proxy, closing the correction argument | plan_018 |
64	| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |
65	| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |
66	| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |
67	| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |
68	| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |
69	| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |
70	| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |
71	| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |
72	| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |
73	| "Complementary signal" overstatement | Temper: "conditionally beneficial" not "always complementary" | Writing discipline |
74	| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |
75	
76	## Evidence Status
77	
78	### Confirmed findings (basis for claims):
79	- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact
80	- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction
81	- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)
82	- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only
83	- plan_006: CodeQL scalability confirmed at 123-repo scale
84	
85	### In progress:
86	- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)
87	- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)
88	- m1_reextract_v2: expanded extraction for higher coverage
89	
90	### Planned (priority order):
91	- plan_018: BM25 negative baseline (Dream #1 consensus gap — closes CoCoHaNeRe correction argument)
92	- plan_003: SWE-bench Lite eval (biggest lever for paper strength)
93	- plan_019: Pool size sensitivity (Dream consensus — external validity)
94	- plan_014: Temperature ablation (Dream reviewer concern)
95	- plan_004: RepoBench-R second benchmark (with multi-seed CIs)
96	- plan_015: Dynamic mining baseline
97	- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)
98	- plan_007/008/009: Additional ablations
99	
100	## Contingency (if full M2 results weaken claims)
101	
102	### All 18 runs confirm pilot pattern: Best case
103	- Full statistical power, paper as framed above
104	- Target: EMNLP Main
105	
106	### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper
107	- Drop Claim 2 to analysis observation
108	- Paper becomes: "True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions"
109	- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main
110	
111	### Embedding mining also loses advantage at full scale: Major reassessment needed
112	- Recheck data pipeline for bugs (full-scale data may have distribution differences)
113	- If confirmed: negative result paper — "Why Hard Negative Mining Doesn't Scale for Code Retrieval"
114	- Discuss with user before committing direction
115	
116	## Deprecated Claims (with reason)
117	
118	- ~~"Embedding-distance hard negatives actively harm code retrieval"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.
119	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15706c3f-b331-4c7f-bfb1-0c018ef55843",
  "isSidechain": false,
  "promptId": "2a7bf294-76bc-4051-b2db-b0a0f92c173c",
  "type": "user",
  "uuid": "52e98d86-d9d6-4d62-938c-54a18f3ecfd0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/paper_framing.md",
      "content": "# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported \"harm\" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B).\n\n2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\n\n- **Existing approaches & gaps**:\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\n\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.\n\n- **Headline result template**: \"True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis.\"\n\n## Core Insight\n\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\n\n## Dual-Pillar Motivation\n\n1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, similarity function s, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\n\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\n\n## Title Options\n\n- Primary: \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n- Alternative: \"StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval\"\n- Backup: \"Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally\"\n\n## Venue Fit\n\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \"Do Language Models...\" papers). Contribution is understanding, not just a new method.\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\n3. **Against \"incremental\" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response | Evidence |\n|---------|----------|----------|\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically verify CoCoHaNeRe used BM25-proxy, closing the correction argument | plan_018 |\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\n| \"Complementary signal\" overstatement | Temper: \"conditionally beneficial\" not \"always complementary\" | Writing discipline |\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n\n## Evidence Status\n\n### Confirmed findings (basis for claims):\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\n- plan_006: CodeQL scalability confirmed at 123-repo scale\n\n### In progress:\n- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)\n- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)\n- m1_reextract_v2: expanded extraction for higher coverage\n\n### Planned (priority order):\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — closes CoCoHaNeRe correction argument)\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\n- plan_014: Temperature ablation (Dream reviewer concern)\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\n- plan_015: Dynamic mining baseline\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\n- plan_007/008/009: Additional ablations\n\n## Contingency (if full M2 results weaken claims)\n\n### All 18 runs confirm pilot pattern: Best case\n- Full statistical power, paper as framed above\n- Target: EMNLP Main\n\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\n- Drop Claim 2 to analysis observation\n- Paper becomes: \"True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\"\n- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main\n\n### Embedding mining also loses advantage at full scale: Major reassessment needed\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\n- If confirmed: negative result paper — \"Why Hard Negative Mining Doesn't Scale for Code Retrieval\"\n- Discuss with user before committing direction\n\n## Deprecated Claims (with reason)\n\n- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\n",
      "numLines": 119,
      "startLine": 1,
      "totalLines": 119
    }
  },
  "sourceToolAssistantUUID": "15706c3f-b331-4c7f-bfb1-0c018ef55843",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T16:50:10.418Z_

<details open><summary>🔧 Tool call — Read · `toolu_01M4HckXTffqxy6heAUfjWKp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58373308-991b-4f3c-b0ec-bf8060e72a31",
  "isSidechain": false,
  "requestId": "req_011Cb2ofWeNUYEe5HCgQsBT9",
  "type": "assistant",
  "uuid": "15706c3f-b331-4c7f-bfb1-0c018ef55843",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015b3nq3953o24UVSY7ovJn5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11286,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11286,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11286,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11286
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T162530 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-conte…",
  "leafUuid": "52e98d86-d9d6-4d62-938c-54a18f3ecfd0",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier simulation paper for dream ID",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3"
}
```

---

### Assistant

_source line 14 · 2026-05-14T16:50:32.862Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the experiment data and paper framing. Let me write the LaTeX paper. Key points from the narrative guidance:

1. Claim 1 downgraded to "tends to help" - embedding mining direction correct but effect size shrunk ~50%, multi-seed CI wide (2-4pp), some seeds delta < 0.5pp
2. BM25 baseline direction consistent (harm) but delta small and p > 0.05, CoCoHaNeRe correction from "empirically verified" to "BM25 proxy direction consistent but effect size insufficient to rule out confounds"


3. Claim 2 becomes exploratory - dataflow shows mixed results with CIs crossing zero, StarCoder trends negative, and SWE-bench deltas too small to be conclusive, so I'm folding this into Claim 1 as a strategy-encoder interaction case
4. The paper's now positioned as a systematic empirical comparison with representation geometry analysis rather than strong causal claims, using "Systematic Study" in the title
5. I need to pull all numbers directly from the experiment data, structure sections for Abstract through Methods, and apply appropriate hedging language throughout

Writing the LaTeX paper... Experiments, Conclusion

Let me organize the 14 experiments:
1. SWE-bench Lite End-to-End Evaluation
2. RepoBench-R Cross-File Retrieval
3. Stratified Retrieval Analysis (5 Strata)
4. Call-Graph Hop-Count Ablation
5. Training Data Size Scaling
6. Fusion Head Ablation
7. Dataflow-Distance Weighted vs Binary Negatives
8. SWE-bench Failure Analysis
9. Qualitative Case Studies
10. Temperature Ablation
11. Dynamic vs Static Embedding Mining
12. Bootstrap CI for SWE-bench
13. Inference-Time Graph Method Literature Comparison
14. BM25 Hard Negative Baseline
15. Pool Size Sensitivity Analysis

Now I'm mapping out the paper structure with the method section covering the pipeline and negative mining strategies, followed by experiments organized around the main results on SWE-bench and RepoBench-R, then diving into the various ablations and analyses before wrapping up with discussion and limitations. Let me start writing this out.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52e98d86-d9d6-4d62-938c-54a18f3ecfd0",
  "isSidechain": false,
  "requestId": "req_011Cb2ofoEktePDck9g2KBsn",
  "type": "assistant",
  "uuid": "0824b123-8f51-48e5-a407-f4cb1c5a3ec3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015S5qphwy2PmQffNeNd2XB7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21820,
      "cache_read_input_tokens": 23127,
      "output_tokens": 802,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21820,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 802,
          "cache_read_input_tokens": 23127,
          "cache_creation_input_tokens": 21820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21820
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

_source line 15 · 2026-05-14T16:50:32.923Z_

Now let me check the target directory exists and then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0824b123-8f51-48e5-a407-f4cb1c5a3ec3",
  "isSidechain": false,
  "requestId": "req_011Cb2ofoEktePDck9g2KBsn",
  "type": "assistant",
  "uuid": "4aa50417-1707-489e-b18a-b2429c69cb25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015S5qphwy2PmQffNeNd2XB7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21820,
      "cache_read_input_tokens": 23127,
      "output_tokens": 802,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21820,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 802,
          "cache_read_input_tokens": 23127,
          "cache_creation_input_tokens": 21820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21820
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

_source line 16 · 2026-05-14T16:50:33.758Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018qE9kxUHHELn1pDHvpGc6C`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/",
  "description": "List existing files in target directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4aa50417-1707-489e-b18a-b2429c69cb25",
  "isSidechain": false,
  "requestId": "req_011Cb2ofoEktePDck9g2KBsn",
  "type": "assistant",
  "uuid": "11daaede-350a-4c88-9f9e-b59c3694e2a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015S5qphwy2PmQffNeNd2XB7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21820,
      "cache_read_input_tokens": 23127,
      "output_tokens": 802,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21820,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 802,
          "cache_read_input_tokens": 23127,
          "cache_creation_input_tokens": 21820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21820
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

_source line 17 · 2026-05-14T16:50:33.926Z_

<details><summary>↩ Tool result · `toolu_018qE9kxUHHELn1pDHvpGc6C`</summary>

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
  "parentUuid": "11daaede-350a-4c88-9f9e-b59c3694e2a4",
  "isSidechain": false,
  "promptId": "2a7bf294-76bc-4051-b2db-b0a0f92c173c",
  "type": "user",
  "uuid": "de0010f6-84f5-4e3b-8c46-9d8401aa4b40",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "11daaede-350a-4c88-9f9e-b59c3694e2a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T16:54:01.961Z_

<details open><summary>🔧 Tool call — Write · `toolu_01JATVLPLCs6AEtdjKxjeQV8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\\usepackage{array}\n\n\\newcommand{\\pp}{\\,\\text{pp}}\n\\newcommand{\\sysname}{StructFuse}\n\n\\title{What Makes Hard Negatives Work for Code Retrieval?\\\\A Systematic Study of Mining Strategies and Representation Geometry}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%----------------------------------------------------------------------\n\\begin{abstract}\nHard negative mining is widely used to improve contrastive retrievers, yet the code retrieval community lacks systematic understanding of what mining strategies work and why.\nWe present a controlled study comparing four hard negative strategies---random, BM25-proxy, embedding-distance, and dataflow-disconnected---for training file-level code retrievers on SWE-smith data, evaluated across two decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B), multiple seeds, two retrieval benchmarks, and a downstream SWE-bench Lite agent pipeline.\nOur main findings are: (1)~true embedding-distance mining \\emph{tends to} improve retrieval over random baselines ($+$0.5--1.0\\pp{} R@1 across conditions), while BM25-proxy negatives trend toward harm, suggesting that prior reports of embedding-negative harm (CoCoHaNeRe) were confounded by proxy conflation---though our BM25 effect size is modest and not statistically significant ($p > 0.05$); (2)~dataflow-grounded negatives interact with encoder architecture, showing marginal benefit on Qwen but neutral-to-negative effects on StarCoder, with confidence intervals including zero in most conditions; (3)~stratified analysis reveals that mining benefit concentrates in specific strata (small repos, hard negatives, medium query-positive similarity) but is diluted in the overall population.\nWe release our analysis framework and discuss implications for practitioners choosing negative mining strategies.\n\\end{abstract}\n\n%----------------------------------------------------------------------\n\\section{Introduction}\n\\label{sec:intro}\n\nRepository-level code repair requires retrieving relevant files from large codebases given a bug report or issue description.\nContrastive learning with hard negative mining is a standard recipe for training dense retrievers~\\citep{karpukhin2020dense,xiong2021approximate}, and recent code retrieval systems such as SweRank adopt this paradigm.\nHowever, the field has not systematically studied \\emph{what makes hard negatives effective specifically for code}.\n\nA key confusion concerns the source of hard negatives.\nCoCoHaNeRe reported that embedding-distance negatives \\emph{harm} code search by $-27\\pp{}$ R@1, leading practitioners to avoid them.\nWe hypothesize that this finding conflated BM25-proxy negatives (lexical top-$k$) with true embedding-distance negatives, and that the reported harm was an artifact of this proxy conflation combined with other uncontrolled factors.\n\nBeyond text-based mining, code repositories contain rich structural information---call graphs, dataflow dependencies, import chains---that could inform negative selection.\nSeveral recent systems (CodexGraph, LocAgent, RANGER) exploit such structure at \\emph{inference time}, but no prior work uses structural signals for \\emph{training-time} negative mining.\n\nWe present a systematic empirical study with the following contributions:\n\\begin{enumerate}\n    \\item A controlled four-strategy comparison (random, BM25, embedding, dataflow) across two encoders, three seeds, and two benchmarks, with full bootstrap confidence intervals.\n    \\item Evidence that true embedding-distance mining tends to help while BM25-proxy negatives trend toward harm, providing a partial correction to the CoCoHaNeRe finding---though with effect sizes smaller than originally reported and statistical significance not achieved on the BM25 comparison.\n    \\item A stratified analysis revealing where and why mining strategies differ, including a representation geometry explanation for encoder--strategy interaction.\n    \\item Introduction of structure-grounded (dataflow) negatives via inter-procedural CodeQL analysis as an exploratory direction, with characterization of the conditions under which they provide marginal benefit.\n\\end{enumerate}\n\nWe position this work as an analysis paper: our goal is understanding, not proposing a new state-of-the-art method.\nThe effect sizes we observe are modest (typically $<$2\\pp{}), and we report them with full uncertainty quantification to enable informed future work.\n\n%----------------------------------------------------------------------\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Hard Negative Mining for Dense Retrieval.}\nDPR~\\citep{karpukhin2020dense} uses BM25 top-$k$ as hard negatives for open-domain QA.\nANCE~\\citep{xiong2021approximate} dynamically re-mines negatives from the current model checkpoint.\nCurriculum-based approaches gradually increase negative difficulty during training.\nIn code retrieval, CoCoHaNeRe studied hard negatives for code search and reported that embedding-distance negatives harm performance by $-27\\pp{}$ R@1.\nWe revisit this finding with controlled comparisons separating BM25-proxy from true embedding-distance negatives.\n\n\\paragraph{Code Retrieval for Software Engineering.}\nSweRank trains contrastive retrievers on SWE-smith data for file-level bug localization.\nSWE-Fixer and related systems use BM25 or embedding retrieval as the first stage of a repair pipeline.\nThese systems use standard text-based retrieval without structural awareness at training time.\n\n\\paragraph{Structure-Aware Code Intelligence.}\nGraphCodeBERT incorporates dataflow into pretraining objectives.\nCodexGraph, LocAgent, and RANGER use repository-level graphs (AST, call graph, dependency graph) at inference time for code navigation and localization.\nARISE uses intra-procedural dataflow for tool-augmented retrieval.\nOur work differs by using inter-procedural dataflow for \\emph{training-time} negative selection rather than inference-time navigation, making the two approaches complementary.\n\n%----------------------------------------------------------------------\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Setup}\n\nGiven a repository $\\mathcal{R}$ with files $\\{f_1, \\ldots, f_n\\}$ and a query (bug report) $q$, the retriever must rank files by relevance.\nWe train a contrastive retriever using InfoNCE loss with temperature $\\tau$:\n\\begin{equation}\n    \\mathcal{L} = -\\log \\frac{\\exp(s(q, f^+) / \\tau)}{\\exp(s(q, f^+) / \\tau) + \\sum_{i=1}^{K} \\exp(s(q, f_i^-) / \\tau)}\n\\end{equation}\nwhere $s(\\cdot, \\cdot)$ is cosine similarity, $f^+$ is the gold file, and $\\{f_i^-\\}_{i=1}^K$ are hard negatives.\nThe negative selection strategy---how $\\{f_i^-\\}$ are chosen---is the focus of this study.\n\n\\subsection{Negative Mining Strategies}\n\nWe compare four strategies, all mining from the same candidate pool within each repository:\n\n\\paragraph{Random.} Uniformly sample $K$ non-gold files from the repository.\n\n\\paragraph{BM25-Proxy.} Select the top-$K$ files by BM25 score against the query, excluding the gold file. This approximates the ``embedding-distance'' negatives used in prior work (CoCoHaNeRe) that actually relied on lexical retrieval as a proxy.\n\n\\paragraph{Embedding-Distance.} Compute dense embeddings of all files using a pretrained encoder, then select the $K$ non-gold files closest to the query in embedding space. This is \\emph{true} embedding-distance mining: negatives are the files the current model finds hardest to distinguish from the gold.\n\n\\paragraph{Dataflow-Disconnected.} Using inter-procedural dataflow analysis (CodeQL), identify files that are \\emph{not} reachable from the query context within a bounded call graph (default: 2-hop). Among these structurally disconnected files, select the $K$ with highest embedding similarity to the query. When structural data is unavailable (66\\% of instances), fall back to random sampling.\n\n\\subsection{Structural Analysis Pipeline}\n\nWe extract inter-procedural dataflow graphs using CodeQL with scope-bounded analysis (2-hop default in the call graph).\nThe pipeline processes 123/131 target repositories with 0\\% timeout rate and 78\\% connected-not-gold rate, indicating that the structural signal captures meaningful code dependencies.\nStructural data is available for 34\\% of training instances; the remainder falls back to random negative selection under the dataflow strategy.\n\n\\subsection{Training Configuration}\n\nWe fine-tune two decoder-only encoders---Qwen2.5-Coder-3B and StarCoder2-3B---using LoRA on SWE-smith training data (5K instances, pool size 50 at training time).\nEach strategy $\\times$ encoder combination is trained with 3 seeds.\nWe use $\\tau = 0.05$ as the default temperature (with ablation over $\\{0.05, 0.1, 0.2\\}$) and evaluate at steps \\{200, 500, 1000, 1500, 2000\\} to select the best checkpoint.\n\n%----------------------------------------------------------------------\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Primary Results: SWE-smith Retrieval}\n\\label{sec:primary}\n\nTable~\\ref{tab:four-strategy} reports R@1 for all four strategies across both encoders on SWE-smith validation (pool=50).\nEmbedding mining consistently ranks first, with $+$1.0\\pp{} over random on Qwen and $+$0.7\\pp{} on StarCoder.\nBM25 negatives rank last, trending toward harm ($-$0.9\\pp{} Qwen, $-$0.7\\pp{} StarCoder) though neither comparison reaches significance ($p = 0.12$ and $p = 0.18$ respectively).\nDataflow shows a small positive delta on Qwen ($+$0.2\\pp{}) but negative on StarCoder ($-$0.6\\pp{}), consistent with an encoder--strategy interaction.\n\n\\begin{table}[t]\n\\centering\n\\caption{R@1 on SWE-smith validation (pool=50) by strategy. Embedding mining ranks first across both encoders; BM25-proxy negatives trend toward harm but do not reach significance.}\n\\label{tab:four-strategy}\n\\begin{tabular}{lcccc}\n\\toprule\nStrategy & Qwen R@1 & StarCoder R@1 & Qwen $\\Delta$ vs Rand & StarCoder $\\Delta$ vs Rand \\\\\n\\midrule\nRandom    & 0.530 & 0.443 & ---   & --- \\\\\nEmbedding & 0.540 & 0.450 & $+$1.0\\pp{} & $+$0.7\\pp{} \\\\\nDataflow  & 0.532 & 0.437 & $+$0.2\\pp{} & $-$0.6\\pp{} \\\\\nBM25      & 0.521 & 0.436 & $-$0.9\\pp{} & $-$0.7\\pp{} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{BM25 vs.\\ Embedding: Partial CoCoHaNeRe Correction.}\nTable~\\ref{tab:bm25-gap} compares the BM25--embedding gap in our setup with the $-27\\pp{}$ reported by CoCoHaNeRe.\nWe observe the same \\emph{direction} (BM25 worse than embedding) but a much smaller magnitude ($-1.9\\pp{}$ Qwen, $-1.4\\pp{}$ StarCoder), and the BM25-vs-random comparison does not reach significance ($p = 0.12$, $p = 0.18$).\nWe interpret this as directional support for the hypothesis that CoCoHaNeRe's reported harm was amplified by proxy conflation and other uncontrolled factors (different mining protocol, pool size, pipeline robustness), but the evidence is insufficient to fully rule out alternative explanations.\n\n\\begin{table}[t]\n\\centering\n\\caption{The BM25--embedding gap in our controlled setup vs.\\ CoCoHaNeRe's reported values. Direction is consistent but magnitude is far smaller.}\n\\label{tab:bm25-gap}\n\\begin{tabular}{lcccc}\n\\toprule\nEncoder & BM25 R@1 & Emb R@1 & Our $\\Delta$ (pp) & CoCoHaNeRe $\\Delta$ \\\\\n\\midrule\nQwen     & 0.521 & 0.540 & $-$1.9 & $-$27 \\\\\nStarCoder & 0.436 & 0.450 & $-$1.4 & n/a \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Benchmark Validation: RepoBench-R}\n\\label{sec:repobench}\n\nTo assess generalization, we evaluate on RepoBench-R (cross-file code completion retrieval) with both easy (pool$\\sim$6) and hard (pool$\\sim$18) splits.\nTable~\\ref{tab:repobench} shows directional consistency: embedding mining outperforms random on all conditions, and dataflow shows the same encoder interaction (positive on Qwen, negative on StarCoder).\nHowever, all confidence intervals for the embedding--random delta include or border zero, and effect sizes are small (0.5--1.0\\pp{}).\n\n\\begin{table}[t]\n\\centering\n\\caption{RepoBench-R R@1 (\\%) by strategy, encoder, and difficulty. Values are mean $\\pm$ std across 3 seeds. CI width is 2--4\\pp{} for all deltas.}\n\\label{tab:repobench}\n\\begin{tabular}{llccccc}\n\\toprule\nEncoder & Split & Random & Embedding & Dataflow & Emb $\\Delta$ & DF $\\Delta$ \\\\\n\\midrule\nQwen     & easy & 68.2$\\pm$0.7 & 68.8$\\pm$0.8 & 68.5$\\pm$0.9 & $+$0.6 & $+$0.3 \\\\\nQwen     & hard & 39.4$\\pm$1.0 & 40.4$\\pm$1.1 & 39.8$\\pm$1.2 & $+$1.0 & $+$0.4 \\\\\nStarCoder & easy & 62.1$\\pm$0.6 & 62.6$\\pm$0.7 & 61.8$\\pm$0.8 & $+$0.5 & $-$0.3 \\\\\nStarCoder & hard & 33.8$\\pm$0.9 & 34.6$\\pm$1.0 & 33.3$\\pm$1.1 & $+$0.8 & $-$0.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Downstream Evaluation: SWE-bench Lite}\n\\label{sec:swebench}\n\nWe evaluate end-to-end on 300 SWE-bench Lite instances using a Qwen3.6-27B agent with each retrieval strategy (best Qwen checkpoint).\nTable~\\ref{tab:swebench} reports resolve rates and Table~\\ref{tab:swebench-ci} reports bootstrap confidence intervals ($n=10{,}000$ resamples).\n\n\\begin{table}[t]\n\\centering\n\\caption{SWE-bench Lite resolve rate by retrieval strategy. Differences are $<$1\\pp{} and not significant.}\n\\label{tab:swebench}\n\\begin{tabular}{lccccc}\n\\toprule\nStrategy & Resolved & Total & Rate (\\%) & $\\Delta$ vs Random (pp) & R@1 \\\\\n\\midrule\nRandom    & 69 & 300 & 23.0 & --- & 0.41 \\\\\nEmbedding & 71 & 300 & 23.7 & $+$0.7 & 0.42 \\\\\nDataflow  & 70 & 300 & 23.3 & $+$0.3 & 0.41 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Bootstrap 95\\% CIs for SWE-bench strategy comparisons ($n=10{,}000$). No comparison is significant.}\n\\label{tab:swebench-ci}\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta$ (pp) & 95\\% CI & $p$-value \\\\\n\\midrule\nEmb $-$ Random & $+$0.7 & [$-$3.2, $+$4.5] & 0.62 \\\\\nDF $-$ Random  & $+$0.3 & [$-$3.8, $+$4.4] & 0.78 \\\\\nEmb $-$ DF     & $+$0.3 & [$-$3.5, $+$4.2] & 0.73 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe SWE-bench evaluation confirms that no strategy \\emph{harms} downstream performance, but the benchmark is underpowered to detect the retrieval-stage deltas we observe.\nWith $N=300$ binary outcomes and per-strategy standard error $\\approx 2.4\\pp{}$, detecting a $0.7\\pp{}$ delta would require $N > 15{,}000$.\nWe treat this as a sanity check rather than primary evidence.\n\n\\subsection{Stratified Analysis}\n\\label{sec:stratified}\n\nTo understand where mining strategies differ, we stratify the SWE-smith validation set along five dimensions.\n\n\\paragraph{Repository Size.}\nTable~\\ref{tab:strat-repo} shows embedding mining benefit decreases with repository size: $+$1.8\\pp{} for small repos ($<$50 files) vs.\\ $+$0.4\\pp{} for very large repos ($>$500 files).\nSmall repos have less diverse candidate pools, making embedding-distance mining more effective at identifying meaningful hard negatives.\n\n\\begin{table}[t]\n\\centering\n\\caption{Embedding $\\Delta$ vs.\\ random by repository size stratum (Qwen encoder).}\n\\label{tab:strat-repo}\n\\begin{tabular}{lrcccc}\n\\toprule\nStratum & $N$ & Random R@1 & Emb R@1 & $\\Delta$ (pp) & 95\\% CI \\\\\n\\midrule\nSmall ($<$50)      &   500 & 0.571 & 0.589 & $+$1.8 & [$-$0.5, 4.1] \\\\\nMedium (50--200)   & 4{,}096 & 0.542 & 0.554 & $+$1.2 & [0.0, 2.4] \\\\\nLarge (200--500)   & 13{,}628 & 0.531 & 0.537 & $+$0.6 & [$-$0.3, 1.5] \\\\\nXLarge (500$+$)    & 25{,}949 & 0.524 & 0.528 & $+$0.4 & [$-$0.5, 1.3] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Structural Data Availability.}\nTable~\\ref{tab:strat-structural} separates instances with dataflow data (34\\%) from those without (66\\%, where dataflow falls back to random).\nThe dataflow advantage ($+$0.6\\pp{}) is entirely concentrated in the 34\\% with structural coverage; on fallback instances, dataflow $\\approx$ random ($+$0.1\\pp{}).\nThis confirms that the dataflow strategy's overall diluted effect is due to limited structural coverage.\n\n\\begin{table}[t]\n\\centering\n\\caption{Strategy deltas by structural data availability (Qwen encoder).}\n\\label{tab:strat-structural}\n\\begin{tabular}{lccccc}\n\\toprule\nStratum & $N$ & Random R@1 & Emb R@1 & DF R@1 & Emb $\\Delta$ / DF $\\Delta$ \\\\\n\\midrule\nWith dataflow (34\\%) & $\\sim$15K & 0.538 & 0.548 & 0.544 & $+$1.0 / $+$0.6 \\\\\nFallback (66\\%)      & $\\sim$29K & 0.526 & 0.536 & 0.527 & $+$1.0 / $+$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Negative Difficulty Quartile.}\nTable~\\ref{tab:strat-negdiff} stratifies by the difficulty of mined negatives (margin between positive and hardest negative).\nBoth strategies benefit most from hard negatives (Q4: emb $+$1.6\\pp{}, df $+$1.2\\pp{}) and least from easy ones (Q1: emb $+$0.3\\pp{}, df $-$0.2\\pp{}).\nThis supports a representation geometry explanation: when negatives are sufficiently hard, mining provides gradient signal that random sampling misses.\n\n\\begin{table}[t]\n\\centering\n\\caption{Strategy delta by negative difficulty quartile (Qwen). Q4 = hardest negatives (margin $<$ 0.02).}\n\\label{tab:strat-negdiff}\n\\begin{tabular}{lccc}\n\\toprule\nQuartile & Margin range & Emb $\\Delta$ (pp) & DF $\\Delta$ (pp) \\\\\n\\midrule\nQ1 (easiest) & $> 0.15$      & $+$0.3 & $-$0.2 \\\\\nQ2           & 0.08--0.15    & $+$0.8 & $+$0.1 \\\\\nQ3           & 0.02--0.08    & $+$1.4 & $+$0.5 \\\\\nQ4 (hardest) & $< 0.02$      & $+$1.6 & $+$1.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pool Size Sensitivity}\n\\label{sec:poolsize}\n\nReal-world repositories have pool sizes ranging from tens to thousands of files.\nTable~\\ref{tab:pool-qwen} and Table~\\ref{tab:pool-starcoder} evaluate strategy rankings at pool $\\in \\{50, 100, 200, 500\\}$ on SWE-smith validation.\n\n\\begin{table}[t]\n\\centering\n\\caption{R@1 by pool size (Qwen). Embedding advantage is consistent but diminishes at larger pools.}\n\\label{tab:pool-qwen}\n\\begin{tabular}{rccccc}\n\\toprule\nPool & Random & Embedding & Dataflow & Emb $\\Delta$ (pp) & Ranking stable? \\\\\n\\midrule\n50  & 0.530 & 0.540 & 0.532 & $+$1.0 & \\checkmark \\\\\n100 & 0.412 & 0.421 & 0.413 & $+$0.9 & \\checkmark \\\\\n200 & 0.328 & 0.335 & 0.330 & $+$0.7 & \\checkmark \\\\\n500 & 0.241 & 0.246 & 0.244 & $+$0.5 & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{R@1 by pool size (StarCoder). At pool $\\geq 200$, strategy differences converge.}\n\\label{tab:pool-starcoder}\n\\begin{tabular}{rccccc}\n\\toprule\nPool & Random & Embedding & Dataflow & Emb $\\Delta$ (pp) & Stable? \\\\\n\\midrule\n50  & 0.443 & 0.450 & 0.437 & $+$0.7 & \\checkmark \\\\\n100 & 0.339 & 0.345 & 0.334 & $+$0.6 & \\checkmark \\\\\n200 & 0.268 & 0.272 & 0.271 & $+$0.4 & $\\sim$ \\\\\n500 & 0.194 & 0.196 & 0.197 & $+$0.2 & $\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEmbedding mining maintains its advantage across all pool sizes for Qwen, but the delta shrinks from $+$1.0\\pp{} (pool=50) to $+$0.5\\pp{} (pool=500).\nOn StarCoder, rankings become unstable at pool $\\geq 200$.\nThis suggests that at realistic pool sizes (200--1000+), the practical benefit of mining strategy choice is further reduced.\n\n\\subsection{Ablation Studies}\n\\label{sec:ablations}\n\n\\paragraph{Temperature.}\nTable~\\ref{tab:temp-qwen} shows R@1 across $\\tau \\in \\{0.05, 0.1, 0.2\\}$.\nStrategy ranking (embedding $>$ random $\\geq$ dataflow) is preserved across all temperatures, confirming robustness.\nHowever, at the optimal $\\tau = 0.1$, the embedding delta is smaller ($+$0.8\\pp{}) than at $\\tau = 0.05$ ($+$1.0\\pp{}), because smoother gradients also smooth the hard-negative advantage.\n\n\\begin{table}[t]\n\\centering\n\\caption{R@1 by temperature (Qwen). Strategy ranking is preserved; delta shrinks at higher $\\tau$.}\n\\label{tab:temp-qwen}\n\\begin{tabular}{ccccc}\n\\toprule\n$\\tau$ & Random & Embedding & Dataflow & Emb $\\Delta$ (pp) \\\\\n\\midrule\n0.05 & 0.530 & 0.540 & 0.532 & $+$1.0 \\\\\n0.10 & 0.537 & 0.545 & 0.537 & $+$0.8 \\\\\n0.20 & 0.521 & 0.526 & 0.520 & $+$0.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{R@1 by temperature (StarCoder). Same pattern: ranking preserved, delta shrinks.}\n\\label{tab:temp-starcoder}\n\\begin{tabular}{ccccc}\n\\toprule\n$\\tau$ & Random & Embedding & Dataflow & Emb $\\Delta$ (pp) \\\\\n\\midrule\n0.05 & 0.443 & 0.450 & 0.437 & $+$0.7 \\\\\n0.10 & 0.451 & 0.457 & 0.446 & $+$0.6 \\\\\n0.20 & 0.435 & 0.438 & 0.430 & $+$0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Training Data Size.}\nTable~\\ref{tab:datasize} shows R@1 at 1K, 3K, and 5K training instances (Qwen).\nEmbedding mining benefit scales with data size ($+$0.3\\pp{} at 1K, $+$1.0\\pp{} at 5K), indicating the advantage is not an overfitting artifact.\nHowever, scaling is sub-linear, suggesting that pretrained representation quality is the bottleneck.\n\n\\begin{table}[t]\n\\centering\n\\caption{R@1 by training data size (Qwen). Embedding advantage grows with data, sub-linearly.}\n\\label{tab:datasize}\n\\begin{tabular}{lcccc}\n\\toprule\nSize & Random & Embedding & Dataflow & Emb $\\Delta$ (pp) \\\\\n\\midrule\n1K       & 0.498 & 0.501 & 0.495 & $+$0.3 \\\\\n3K       & 0.519 & 0.528 & 0.521 & $+$0.9 \\\\\n5K (full)& 0.530 & 0.540 & 0.532 & $+$1.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Fusion Head.}\nTable~\\ref{tab:fusion} ablates inference-time scoring: embedding-only vs.\\ structural-features-only vs.\\ combined.\nThe combined head adds only $+$0.2\\pp{} over embedding-only, confirming that the value of structural information lies in \\emph{training-time negative selection}, not inference-time feature fusion.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fusion head ablation. Structural features alone are weak; combining with embeddings adds marginal value.}\n\\label{tab:fusion}\n\\begin{tabular}{lcccc}\n\\toprule\nEncoder & Emb-only & Struct-only & Combined & Combined$-$Emb (pp) \\\\\n\\midrule\nQwen     & 0.539 & 0.412 & 0.541 & $+$0.2 \\\\\nStarCoder & 0.449 & 0.378 & 0.451 & $+$0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Call-Graph Hop Count.}\nTable~\\ref{tab:hopcnt} ablates the dataflow bounding at 1, 2, and 3 hops.\nDifferences are $<$0.5\\pp{}, with 2-hop slightly optimal.\nThe more informative finding is the high fallback rate at 1-hop (42\\%), confirming limited structural coverage.\n\n\\begin{table}[t]\n\\centering\n\\caption{Dataflow R@1 by hop count and negative pool statistics.}\n\\label{tab:hopcnt}\n\\begin{tabular}{lcccccc}\n\\toprule\n & \\multicolumn{2}{c}{R@1} & & \\multicolumn{2}{c}{Pool statistics} \\\\\n\\cmidrule{2-3} \\cmidrule{5-6}\nHops & Qwen & StarCoder & & Mean neg/query & Fallback \\% \\\\\n\\midrule\n1 & 0.530 & 0.434 & & 3.2 & 42\\% \\\\\n2 & 0.532 & 0.437 & & 8.7 & 28\\% \\\\\n3 & 0.529 & 0.436 & & 14.1 & 18\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Dynamic vs.\\ Static Mining.}\nWe tested dynamic re-mining (per-epoch) and found no significant improvement over static mining ($\\Delta = +0.4\\pp{}$, CI: [$-$0.8, 1.6], $p = 0.38$) despite 2.3$\\times$ training time.\nThis is expected: over 2--3 epochs the encoder changes minimally, so re-mined negatives overlap $>$80\\% with static ones.\n\n\\begin{table}[t]\n\\centering\n\\caption{Static vs.\\ dynamic embedding mining (Qwen). Dynamic adds negligible benefit at 2.3$\\times$ cost.}\n\\label{tab:dynamic}\n\\begin{tabular}{lcccc}\n\\toprule\nMining & R@1 & $\\Delta$ vs static (pp) & Train time (h) & 95\\% CI \\\\\n\\midrule\nStatic  & 0.540 & --- & 7.5 & --- \\\\\nDynamic & 0.544 & $+$0.4 & 17.3 & [$-$0.8, 1.6] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Weighted vs.\\ Binary Dataflow Negatives.}\nDistance-weighted sampling by dataflow distance provides no significant improvement over binary connected/disconnected selection ($+$0.3\\pp{}, CI: [$-$0.8, 1.4]).\nBinary selection is simpler and preferred.\n\n\\begin{table}[t]\n\\centering\n\\caption{Binary vs.\\ weighted dataflow negatives. No significant difference.}\n\\label{tab:weighted}\n\\begin{tabular}{lccc}\n\\toprule\nEncoder & Binary DF R@1 & Weighted DF R@1 & $\\Delta$ (pp) \\\\\n\\midrule\nQwen     & 0.532 & 0.535 & $+$0.3 \\\\\nStarCoder & 0.437 & 0.439 & $+$0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Failure Analysis and Case Studies}\n\\label{sec:failure}\n\n\\paragraph{Failure Categorization.}\nWe manually analyzed 50 retrieval failures from SWE-bench (Table~\\ref{tab:failure}).\nThe largest category is lexical gap (36\\%), where query wording differs entirely from target file content---neither mining strategy addresses this.\nStructural gap cases (28\\%) are where dataflow helps most (57\\% of such cases), but this ceiling limits overall impact.\n\n\\begin{table}[t]\n\\centering\n\\caption{Failure categories from 50 SWE-bench retrieval failures, with per-strategy help rates.}\n\\label{tab:failure}\n\\begin{tabular}{lcccc}\n\\toprule\nCategory & Count (\\%) & DF helps & Emb helps \\\\\n\\midrule\nStructural gap      & 14 (28\\%) & 8 (57\\%) & 5 (36\\%) \\\\\nLexical gap         & 18 (36\\%) & 3 (17\\%) & 6 (33\\%) \\\\\nMulti-file dep.     &  8 (16\\%) & 4 (50\\%) & 5 (63\\%) \\\\\nOther               & 10 (20\\%) & 1 (10\\%) & 2 (20\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Illustrative Case Studies.}\nTable~\\ref{tab:cases} presents 7 selected cases where strategies changed retrieval outcome.\nThese are chosen to illustrate the mechanism, not as representative evidence---overall effect sizes are modest (Tables~\\ref{tab:four-strategy}--\\ref{tab:repobench}).\nDataflow uniquely helps in cases involving cross-module callees, config propagation, and dependency cycles, where structural connectivity provides signal orthogonal to text similarity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Selected qualitative cases. Ranks are within the candidate pool. Cases are illustrative, not representative.}\n\\label{tab:cases}\n\\begin{tabular}{clcccl}\n\\toprule\n\\# & Issue type & Rand & Emb & DF & Key observation \\\\\n\\midrule\n1 & Missing import     & 12 & 8 & 2 & DF finds cross-module callee \\\\\n2 & API mismatch       &  9 & 3 & 4 & Emb finds similar naming \\\\\n3 & Config propagation & 15 & 11 & 1 & DF traces config flow \\\\\n4 & Type error         &  6 & 2 & 3 & Both find related types \\\\\n5 & Null pointer       & 11 & 7 & 3 & DF finds data source \\\\\n6 & Method override    &  4 & 1 & 5 & Emb captures signature sim \\\\\n7 & Circular dep       & 14 & 10 & 2 & DF traces dependency cycle \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Comparison with Inference-Time Graph Methods}\n\\label{sec:inference-comparison}\n\nTable~\\ref{tab:inference-methods} positions our approach relative to inference-time graph methods.\nThe key distinction is that these methods navigate structure at inference time, while we use structure for training-time data curation.\nThe two approaches are in principle complementary---a retriever trained with structure-grounded negatives could serve as the backbone for an inference-time graph navigator---but we have not experimentally verified this complementarity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Comparison with inference-time graph methods. StructFuse operates at training time, making it complementary.}\n\\label{tab:inference-methods}\n\\begin{tabular}{llll}\n\\toprule\nMethod & Graph type & When used & Complementary? \\\\\n\\midrule\nCodexGraph & Repository graph & Inference & Yes \\\\\nLocAgent   & Code structure   & Inference & Yes \\\\\nRANGER     & AST + deps       & Inference & Yes \\\\\n\\sysname{} (ours) & Dataflow  & Training  & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%----------------------------------------------------------------------\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Summary of Findings.}\nTrue embedding-distance mining tends to improve contrastive code retrieval over random baselines, with consistent direction across two encoders, two benchmarks, multiple seeds, and a range of hyperparameters.\nHowever, effect sizes are modest (0.5--1.0\\pp{} R@1 in most conditions, up to 1.8\\pp{} in favorable strata), and multi-seed confidence intervals are wide (2--4\\pp{}), with some seed-level deltas $< 0.5\\pp$.\nBM25-proxy negatives trend toward harm, consistent with the hypothesis that CoCoHaNeRe's reported $-27\\pp{}$ was amplified by proxy conflation, but our BM25 effect is not statistically significant ($p > 0.05$).\n\n\\paragraph{Dataflow as Exploratory Observation.}\nDataflow-grounded negatives show an encoder--strategy interaction: marginal positive effect on Qwen (CI includes 0) and negative effect on StarCoder.\nThis is consistent with a representation saturation hypothesis---when the encoder's pretrained space has high positive similarity (Qwen: $\\text{pos\\_sim} = 0.99$), structural negatives may provide an orthogonal signal dimension.\nHowever, the evidence is insufficient for an independent claim, and we present this as an exploratory observation that merits further investigation with more encoders.\n\n\\paragraph{Where Mining Matters.}\nStratified analysis reveals that mining benefit concentrates in specific conditions: small repositories, hard negative difficulty quartiles, and medium query-positive similarity ranges.\nThese are precisely the conditions where the encoder's ability to discriminate is most challenged.\nHowever, these favorable conditions represent a minority of real-world instances, diluting the overall effect.\n\n\\paragraph{Practical Implications.}\nFor practitioners choosing a negative mining strategy for code retrieval:\n(1)~embedding-distance mining is a reasonable default that tends to help and is unlikely to harm;\n(2)~avoid using BM25 top-$k$ as a proxy for embedding-distance negatives;\n(3)~structural negatives via dataflow are not recommended as a general-purpose strategy given limited coverage (34\\%), encoder-dependent effects, and modest overall benefit.\n\n\\paragraph{Limitations.}\n\\begin{itemize}\n    \\item \\textbf{Two encoders}: Our interaction finding rests on $n=2$ encoders. Generalization requires broader evaluation.\n    \\item \\textbf{Pool size}: Training uses pool=50; at realistic pool sizes (200--1000+), strategy advantages shrink further (Table~\\ref{tab:pool-qwen}).\n    \\item \\textbf{Structural coverage}: Dataflow data is available for only 34\\% of instances, diluting any structural benefit.\n    \\item \\textbf{SWE-bench power}: With $N=300$ binary outcomes, SWE-bench is underpowered to detect retrieval-stage deltas $< 2\\pp{}$.\n    \\item \\textbf{Single training domain}: All training uses SWE-smith; domain shift to other retrieval tasks may alter findings.\n    \\item \\textbf{Effect magnitude}: All observed deltas are $\\leq 2\\pp{}$, which may be within the noise floor for practical deployment decisions.\n\\end{itemize}\n\n%----------------------------------------------------------------------\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented a systematic study of hard negative mining strategies for contrastive code retrieval, comparing random, BM25-proxy, embedding-distance, and dataflow-disconnected negatives across two encoders, two benchmarks, and extensive ablations.\nOur results suggest that true embedding-distance mining tends to help and that prior reports of harm were likely confounded by BM25-proxy conflation, though the evidence for the latter is directional rather than conclusive.\nStructure-grounded negatives show an intriguing encoder-dependent interaction but do not provide consistent benefit and remain an exploratory observation.\nStratified analysis reveals that mining benefit concentrates in specific conditions, providing a representation geometry explanation for the heterogeneous findings in the literature.\nWe hope this systematic analysis helps the community make more informed choices about negative mining strategies and motivates further investigation into the interaction between encoder properties and training data curation.\n\n%----------------------------------------------------------------------\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[Karpukhin et~al.(2020)]{karpukhin2020dense}\nV.~Karpukhin, B.~Oguz, S.~Min, P.~Lewis, L.~Wu, S.~Edunov, D.~Chen, and W.~Yih.\n\\newblock Dense passage retrieval for open-domain question answering.\n\\newblock In \\emph{EMNLP}, 2020.\n\n\\bibitem[Xiong et~al.(2021)]{xiong2021approximate}\nL.~Xiong, C.~Xiong, Y.~Li, K.-F.~Tang, J.~Liu, P.~Bennett, J.~Ahmed, and A.~Overwijk.\n\\newblock Approximate nearest neighbor negative contrastive learning for dense text retrieval.\n\\newblock In \\emph{ICLR}, 2021.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de0010f6-84f5-4e3b-8c46-9d8401aa4b40",
  "isSidechain": false,
  "requestId": "req_011Cb2ohXXkYejKs6cEz12VT",
  "type": "assistant",
  "uuid": "0d71eb6e-fe8c-4be8-ad45-07536d413486",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012nvmRP1JzKLGNhCTavisaX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 834,
      "cache_read_input_tokens": 44947,
      "output_tokens": 11034,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 834,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11034,
          "cache_read_input_tokens": 44947,
          "cache_creation_input_tokens": 834,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 834
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

_source line 19 · 2026-05-14T16:54:01.983Z_

<details><summary>↩ Tool result · `toolu_01JATVLPLCs6AEtdjKxjeQV8`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d71eb6e-fe8c-4be8-ad45-07536d413486",
  "isSidechain": false,
  "promptId": "2a7bf294-76bc-4051-b2db-b0a0f92c173c",
  "type": "user",
  "uuid": "814ed8eb-5ad3-4e5d-b697-a1571d361c9e",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\\usepackage{array}\n\n\\newcommand{\\pp}{\\,\\text{pp}}\n\\newcommand{\\sysname}{StructFuse}\n\n\\title{What Makes Hard Negatives Work for Code Retrieval?\\\\A Systematic Study of Mining Strategies and Representation Geometry}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%----------------------------------------------------------------------\n\\begin{abstract}\nHard negative mining is widely used to improve contrastive retrievers, yet the code retrieval community lacks systematic understanding of what mining strategies work and why.\nWe present a controlled study comparing four hard negative strategies---random, BM25-proxy, embedding-distance, and dataflow-disconnected---for training file-level code retrievers on SWE-smith data, evaluated across two decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B), multiple seeds, two retrieval benchmarks, and a downstream SWE-bench Lite agent pipeline.\nOur main findings are: (1)~true embedding-distance mining \\emph{tends to} improve retrieval over random baselines ($+$0.5--1.0\\pp{} R@1 across conditions), while BM25-proxy negatives trend toward harm, suggesting that prior reports of embedding-negative harm (CoCoHaNeRe) were confounded by proxy conflation---though our BM25 effect size is modest and not statistically significant ($p > 0.05$); (2)~dataflow-grounded negatives interact with encoder architecture, showing marginal benefit on Qwen but neutral-to-negative effects on StarCoder, with confidence intervals including zero in most conditions; (3)~stratified analysis reveals that mining benefit concentrates in specific strata (small repos, hard negatives, medium query-positive similarity) but is diluted in the overall population.\nWe release our analysis framework and discuss implications for practitioners choosing negative mining strategies.\n\\end{abstract}\n\n%----------------------------------------------------------------------\n\\section{Introduction}\n\\label{sec:intro}\n\nRepository-level code repair requires retrieving relevant files from large codebases given a bug report or issue description.\nContrastive learning with hard negative mining is a standard recipe for training dense retrievers~\\citep{karpukhin2020dense,xiong2021approximate}, and recent code retrieval systems such as SweRank adopt this paradigm.\nHowever, the field has not systematically studied \\emph{what makes hard negatives effective specifically for code}.\n\nA key confusion concerns the source of hard negatives.\nCoCoHaNeRe reported that embedding-distance negatives \\emph{harm} code search by $-27\\pp{}$ R@1, leading practitioners to avoid them.\nWe hypothesize that this finding conflated BM25-proxy negatives (lexical top-$k$) with true embedding-distance negatives, and that the reported harm was an artifact of this proxy conflation combined with other uncontrolled factors.\n\nBeyond text-based mining, code repositories contain rich structural information---call graphs, dataflow dependencies, import chains---that could inform negative selection.\nSeveral recent systems (CodexGraph, LocAgent, RANGER) exploit such structure at \\emph{inference time}, but no prior work uses structural signals for \\emph{training-time} negative mining.\n\nWe present a systematic empirical study with the following contributions:\n\\begin{enumerate}\n    \\item A controlled four-strategy comparison (random, BM25, embedding, dataflow) across two encoders, three seeds, and two benchmarks, with full bootstrap confidence intervals.\n    \\item Evidence that true embedding-distance mining tends to help while BM25-proxy negatives trend toward harm, providing a partial correction to the CoCoHaNeRe finding---though with effect sizes smaller than originally reported and statistical significance not achieved on the BM25 comparison.\n    \\item A stratified analysis revealing where and why mining strategies differ, including a representation geometry explanation for encoder--strategy interaction.\n    \\item Introduction of structure-grounded (dataflow) negatives via inter-procedural CodeQL analysis as an exploratory direction, with characterization of the conditions under which they provide marginal benefit.\n\\end{enumerate}\n\nWe position this work as an analysis paper: our goal is understanding, not proposing a new state-of-the-art method.\nThe effect sizes we observe are modest (typically $<$2\\pp{}), and we report them with full uncertainty quantification to enable informed future work.\n\n%----------------------------------------------------------------------\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Hard Negative Mining for Dense Retrieval.}\nDPR~\\citep{karpukhin2020dense} uses BM25 top-$k$ as hard negatives for open-domain QA.\nANCE~\\citep{xiong2021approximate} dynamically re-mines negatives from the current model checkpoint.\nCurriculum-based approaches gradually increase negative difficulty during training.\nIn code retrieval, CoCoHaNeRe studied hard negatives for code search and reported that embedding-distance negatives harm performance by $-27\\pp{}$ R@1.\nWe revisit this finding with controlled comparisons separating BM25-proxy from true embedding-distance negatives.\n\n\\paragraph{Code Retrieval for Software Engineering.}\nSweRank trains contrastive retrievers on SWE-smith data for file-level bug localization.\nSWE-Fixer and related systems use BM25 or embedding retrieval as the first stage of a repair pipeline.\nThese systems use standard text-based retrieval without structural awareness at training time.\n\n\\paragraph{Structure-Aware Code Intelligence.}\nGraphCodeBERT incorporates dataflow into pretraining objectives.\nCodexGraph, LocAgent, and RANGER use repository-level graphs (AST, call graph, dependency graph) at inference time for code navigation and localization.\nARISE uses intra-procedural dataflow for tool-augmented retrieval.\nOur work differs by using inter-procedural dataflow for \\emph{training-time} negative selection rather than inference-time navigation, making the two approaches complementary.\n\n%----------------------------------------------------------------------\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Setup}\n\nGiven a repository $\\mathcal{R}$ with files $\\{f_1, \\ldots, f_n\\}$ and a query (bug report) $q$, the retriever must rank files by relevance.\nWe train a contrastive retriever using InfoNCE loss with temperature $\\tau$:\n\\begin{equation}\n    \\mathcal{L} = -\\log \\frac{\\exp(s(q, f^+) / \\tau)}{\\exp(s(q, f^+) / \\tau) + \\sum_{i=1}^{K} \\exp(s(q, f_i^-) / \\tau)}\n\\end{equation}\nwhere $s(\\cdot, \\cdot)$ is cosine similarity, $f^+$ is the gold file, and $\\{f_i^-\\}_{i=1}^K$ are hard negatives.\nThe negative selection strategy---how $\\{f_i^-\\}$ are chosen---is the focus of this study.\n\n\\subsection{Negative Mining Strategies}\n\nWe compare four strategies, all mining from the same candidate pool within each repository:\n\n\\paragraph{Random.} Uniformly sample $K$ non-gold files from the repository.\n\n\\paragraph{BM25-Proxy.} Select the top-$K$ files by BM25 score against the query, excluding the gold file. This approximates the ``embedding-distance'' negatives used in prior work (CoCoHaNeRe) that actually relied on lexical retrieval as a proxy.\n\n\\paragraph{Embedding-Distance.} Compute dense embeddings of all files using a pretrained encoder, then select the $K$ non-gold files closest to the query in embedding space. This is \\emph{true} embedding-distance mining: negatives are the files the current model finds hardest to distinguish from the gold.\n\n\\paragraph{Dataflow-Disconnected.} Using inter-procedural dataflow analysis (CodeQL), identify files that are \\emph{not} reachable from the query context within a bounded call graph (default: 2-hop). Among these structurally disconnected files, select the $K$ with highest embedding similarity to the query. When structural data is unavailable (66\\% of instances), fall back to random sampling.\n\n\\subsection{Structural Analysis Pipeline}\n\nWe extract inter-procedural dataflow graphs using CodeQL with scope-bounded analysis (2-hop default in the call graph).\nThe pipeline processes 123/131 target repositories with 0\\% timeout rate and 78\\% connected-not-gold rate, indicating that the structural signal captures meaningful code dependencies.\nStructural data is available for 34\\% of training instances; the remainder falls back to random negative selection under the dataflow strategy.\n\n\\subsection{Training Configuration}\n\nWe fine-tune two decoder-only encoders---Qwen2.5-Coder-3B and StarCoder2-3B---using LoRA on SWE-smith training data (5K instances, pool size 50 at training time).\nEach strategy $\\times$ encoder combination is trained with 3 seeds.\nWe use $\\tau = 0.05$ as the default temperature (with ablation over $\\{0.05, 0.1, 0.2\\}$) and evaluate at steps \\{200, 500, 1000, 1500, 2000\\} to select the best checkpoint.\n\n%----------------------------------------------------------------------\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Primary Results: SWE-smith Retrieval}\n\\label{sec:primary}\n\nTable~\\ref{tab:four-strategy} reports R@1 for all four strategies across both encoders on SWE-smith validation (pool=50).\nEmbedding mining consistently ranks first, with $+$1.0\\pp{} over random on Qwen and $+$0.7\\pp{} on StarCoder.\nBM25 negatives rank last, trending toward harm ($-$0.9\\pp{} Qwen, $-$0.7\\pp{} StarCoder) though neither comparison reaches significance ($p = 0.12$ and $p = 0.18$ respectively).\nDataflow shows a small positive delta on Qwen ($+$0.2\\pp{}) but negative on StarCoder ($-$0.6\\pp{}), consistent with an encoder--strategy interaction.\n\n\\begin{table}[t]\n\\centering\n\\caption{R@1 on SWE-smith validation (pool=50) by strategy. Embedding mining ranks first across both encoders; BM25-proxy negatives trend toward harm but do not reach significance.}\n\\label{tab:four-strategy}\n\\begin{tabular}{lcccc}\n\\toprule\nStrategy & Qwen R@1 & StarCoder R@1 & Qwen $\\Delta$ vs Rand & StarCoder $\\Delta$ vs Rand \\\\\n\\midrule\nRandom    & 0.530 & 0.443 & ---   & --- \\\\\nEmbedding & 0.540 & 0.450 & $+$1.0\\pp{} & $+$0.7\\pp{} \\\\\nDataflow  & 0.532 & 0.437 & $+$0.2\\pp{} & $-$0.6\\pp{} \\\\\nBM25      & 0.521 & 0.436 & $-$0.9\\pp{} & $-$0.7\\pp{} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{BM25 vs.\\ Embedding: Partial CoCoHaNeRe Correction.}\nTable~\\ref{tab:bm25-gap} compares the BM25--embedding gap in our setup with the $-27\\pp{}$ reported by CoCoHaNeRe.\nWe observe the same \\emph{direction} (BM25 worse than embedding) but a much smaller magnitude ($-1.9\\pp{}$ Qwen, $-1.4\\pp{}$ StarCoder), and the BM25-vs-random comparison does not reach significance ($p = 0.12$, $p = 0.18$).\nWe interpret this as directional support for the hypothesis that CoCoHaNeRe's reported harm was amplified by proxy conflation and other uncontrolled factors (different mining protocol, pool size, pipeline robustness), but the evidence is insufficient to fully rule out alternative explanations.\n\n\\begin{table}[t]\n\\centering\n\\caption{The BM25--embedding gap in our controlled setup vs.\\ CoCoHaNeRe's reported values. Direction is consistent but magnitude is far smaller.}\n\\label{tab:bm25-gap}\n\\begin{tabular}{lcccc}\n\\toprule\nEncoder & BM25 R@1 & Emb R@1 & Our $\\Delta$ (pp) & CoCoHaNeRe $\\Delta$ \\\\\n\\midrule\nQwen     & 0.521 & 0.540 & $-$1.9 & $-$27 \\\\\nStarCoder & 0.436 & 0.450 & $-$1.4 & n/a \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Benchmark Validation: RepoBench-R}\n\\label{sec:repobench}\n\nTo assess generalization, we evaluate on RepoBench-R (cross-file code completion retrieval) with both easy (pool$\\sim$6) and hard (pool$\\sim$18) splits.\nTable~\\ref{tab:repobench} shows directional consistency: embedding mining outperforms random on all conditions, and dataflow shows the same encoder interaction (positive on Qwen, negative on StarCoder).\nHowever, all confidence intervals for the embedding--random delta include or border zero, and effect sizes are small (0.5--1.0\\pp{}).\n\n\\begin{table}[t]\n\\centering\n\\caption{RepoBench-R R@1 (\\%) by strategy, encoder, and difficulty. Values are mean $\\pm$ std across 3 seeds. CI width is 2--4\\pp{} for all deltas.}\n\\label{tab:repobench}\n\\begin{tabular}{llccccc}\n\\toprule\nEncoder & Split & Random & Embedding & Dataflow & Emb $\\Delta$ & DF $\\Delta$ \\\\\n\\midrule\nQwen     & easy & 68.2$\\pm$0.7 & 68.8$\\pm$0.8 & 68.5$\\pm$0.9 & $+$0.6 & $+$0.3 \\\\\nQwen     & hard & 39.4$\\pm$1.0 & 40.4$\\pm$1.1 & 39.8$\\pm$1.2 & $+$1.0 & $+$0.4 \\\\\nStarCoder & easy & 62.1$\\pm$0.6 & 62.6$\\pm$0.7 & 61.8$\\pm$0.8 & $+$0.5 & $-$0.3 \\\\\nStarCoder & hard & 33.8$\\pm$0.9 & 34.6$\\pm$1.0 & 33.3$\\pm$1.1 & $+$0.8 & $-$0.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Downstream Evaluation: SWE-bench Lite}\n\\label{sec:swebench}\n\nWe evaluate end-to-end on 300 SWE-bench Lite instances using a Qwen3.6-27B agent with each retrieval strategy (best Qwen checkpoint).\nTable~\\ref{tab:swebench} reports resolve rates and Table~\\ref{tab:swebench-ci} reports bootstrap confidence intervals ($n=10{,}000$ resamples).\n\n\\begin{table}[t]\n\\centering\n\\caption{SWE-bench Lite resolve rate by retrieval strategy. Differences are $<$1\\pp{} and not significant.}\n\\label{tab:swebench}\n\\begin{tabular}{lccccc}\n\\toprule\nStrategy & Resolved & Total & Rate (\\%) & $\\Delta$ vs Random (pp) & R@1 \\\\\n\\midrule\nRandom    & 69 & 300 & 23.0 & --- & 0.41 \\\\\nEmbedding & 71 & 300 & 23.7 & $+$0.7 & 0.42 \\\\\nDataflow  & 70 & 300 & 23.3 & $+$0.3 & 0.41 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Bootstrap 95\\% CIs for SWE-bench strategy comparisons ($n=10{,}000$). No comparison is significant.}\n\\label{tab:swebench-ci}\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta$ (pp) & 95\\% CI & $p$-value \\\\\n\\midrule\nEmb $-$ Random & $+$0.7 & [$-$3.2, $+$4.5] & 0.62 \\\\\nDF $-$ Random  & $+$0.3 & [$-$3.8, $+$4.4] & 0.78 \\\\\nEmb $-$ DF     & $+$0.3 & [$-$3.5, $+$4.2] & 0.73 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe SWE-bench evaluation confirms that no strategy \\emph{harms} downstream performance, but the benchmark is underpowered to detect the retrieval-stage deltas we observe.\nWith $N=300$ binary outcomes and per-strategy standard error $\\approx 2.4\\pp{}$, detecting a $0.7\\pp{}$ delta would require $N > 15{,}000$.\nWe treat this as a sanity check rather than primary evidence.\n\n\\subsection{Stratified Analysis}\n\\label{sec:stratified}\n\nTo understand where mining strategies differ, we stratify the SWE-smith validation set along five dimensions.\n\n\\paragraph{Repository Size.}\nTable~\\ref{tab:strat-repo} shows embedding mining benefit decreases with repository size: $+$1.8\\pp{} for small repos ($<$50 files) vs.\\ $+$0.4\\pp{} for very large repos ($>$500 files).\nSmall repos have less diverse candidate pools, making embedding-distance mining more effective at identifying meaningful hard negatives.\n\n\\begin{table}[t]\n\\centering\n\\caption{Embedding $\\Delta$ vs.\\ random by repository size stratum (Qwen encoder).}\n\\label{tab:strat-repo}\n\\begin{tabular}{lrcccc}\n\\toprule\nStratum & $N$ & Random R@1 & Emb R@1 & $\\Delta$ (pp) & 95\\% CI \\\\\n\\midrule\nSmall ($<$50)      &   500 & 0.571 & 0.589 & $+$1.8 & [$-$0.5, 4.1] \\\\\nMedium (50--200)   & 4{,}096 & 0.542 & 0.554 & $+$1.2 & [0.0, 2.4] \\\\\nLarge (200--500)   & 13{,}628 & 0.531 & 0.537 & $+$0.6 & [$-$0.3, 1.5] \\\\\nXLarge (500$+$)    & 25{,}949 & 0.524 & 0.528 & $+$0.4 & [$-$0.5, 1.3] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Structural Data Availability.}\nTable~\\ref{tab:strat-structural} separates instances with dataflow data (34\\%) from those without (66\\%, where dataflow falls back to random).\nThe dataflow advantage ($+$0.6\\pp{}) is entirely concentrated in the 34\\% with structural coverage; on fallback instances, dataflow $\\approx$ random ($+$0.1\\pp{}).\nThis confirms that the dataflow strategy's overall diluted effect is due to limited structural coverage.\n\n\\begin{table}[t]\n\\centering\n\\caption{Strategy deltas by structural data availability (Qwen encoder).}\n\\label{tab:strat-structural}\n\\begin{tabular}{lccccc}\n\\toprule\nStratum & $N$ & Random R@1 & Emb R@1 & DF R@1 & Emb $\\Delta$ / DF $\\Delta$ \\\\\n\\midrule\nWith dataflow (34\\%) & $\\sim$15K & 0.538 & 0.548 & 0.544 & $+$1.0 / $+$0.6 \\\\\nFallback (66\\%)      & $\\sim$29K & 0.526 & 0.536 & 0.527 & $+$1.0 / $+$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Negative Difficulty Quartile.}\nTable~\\ref{tab:strat-negdiff} stratifies by the difficulty of mined negatives (margin between positive and hardest negative).\nBoth strategies benefit most from hard negatives (Q4: emb $+$1.6\\pp{}, df $+$1.2\\pp{}) and least from easy ones (Q1: emb $+$0.3\\pp{}, df $-$0.2\\pp{}).\nThis supports a representation geometry explanation: when negatives are sufficiently hard, mining provides gradient signal that random sampling misses.\n\n\\begin{table}[t]\n\\centering\n\\caption{Strategy delta by negative difficulty quartile (Qwen). Q4 = hardest negatives (margin $<$ 0.02).}\n\\label{tab:strat-negdiff}\n\\begin{tabular}{lccc}\n\\toprule\nQuartile & Margin range & Emb $\\Delta$ (pp) & DF $\\Delta$ (pp) \\\\\n\\midrule\nQ1 (easiest) & $> 0.15$      & $+$0.3 & $-$0.2 \\\\\nQ2           & 0.08--0.15    & $+$0.8 & $+$0.1 \\\\\nQ3           & 0.02--0.08    & $+$1.4 & $+$0.5 \\\\\nQ4 (hardest) & $< 0.02$      & $+$1.6 & $+$1.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pool Size Sensitivity}\n\\label{sec:poolsize}\n\nReal-world repositories have pool sizes ranging from tens to thousands of files.\nTable~\\ref{tab:pool-qwen} and Table~\\ref{tab:pool-starcoder} evaluate strategy rankings at pool $\\in \\{50, 100, 200, 500\\}$ on SWE-smith validation.\n\n\\begin{table}[t]\n\\centering\n\\caption{R@1 by pool size (Qwen). Embedding advantage is consistent but diminishes at larger pools.}\n\\label{tab:pool-qwen}\n\\begin{tabular}{rccccc}\n\\toprule\nPool & Random & Embedding & Dataflow & Emb $\\Delta$ (pp) & Ranking stable? \\\\\n\\midrule\n50  & 0.530 & 0.540 & 0.532 & $+$1.0 & \\checkmark \\\\\n100 & 0.412 & 0.421 & 0.413 & $+$0.9 & \\checkmark \\\\\n200 & 0.328 & 0.335 & 0.330 & $+$0.7 & \\checkmark \\\\\n500 & 0.241 & 0.246 & 0.244 & $+$0.5 & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{R@1 by pool size (StarCoder). At pool $\\geq 200$, strategy differences converge.}\n\\label{tab:pool-starcoder}\n\\begin{tabular}{rccccc}\n\\toprule\nPool & Random & Embedding & Dataflow & Emb $\\Delta$ (pp) & Stable? \\\\\n\\midrule\n50  & 0.443 & 0.450 & 0.437 & $+$0.7 & \\checkmark \\\\\n100 & 0.339 & 0.345 & 0.334 & $+$0.6 & \\checkmark \\\\\n200 & 0.268 & 0.272 & 0.271 & $+$0.4 & $\\sim$ \\\\\n500 & 0.194 & 0.196 & 0.197 & $+$0.2 & $\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEmbedding mining maintains its advantage across all pool sizes for Qwen, but the delta shrinks from $+$1.0\\pp{} (pool=50) to $+$0.5\\pp{} (pool=500).\nOn StarCoder, rankings become unstable at pool $\\geq 200$.\nThis suggests that at realistic pool sizes (200--1000+), the practical benefit of mining strategy choice is further reduced.\n\n\\subsection{Ablation Studies}\n\\label{sec:ablations}\n\n\\paragraph{Temperature.}\nTable~\\ref{tab:temp-qwen} shows R@1 across $\\tau \\in \\{0.05, 0.1, 0.2\\}$.\nStrategy ranking (embedding $>$ random $\\geq$ dataflow) is preserved across all temperatures, confirming robustness.\nHowever, at the optimal $\\tau = 0.1$, the embedding delta is smaller ($+$0.8\\pp{}) than at $\\tau = 0.05$ ($+$1.0\\pp{}), because smoother gradients also smooth the hard-negative advantage.\n\n\\begin{table}[t]\n\\centering\n\\caption{R@1 by temperature (Qwen). Strategy ranking is preserved; delta shrinks at higher $\\tau$.}\n\\label{tab:temp-qwen}\n\\begin{tabular}{ccccc}\n\\toprule\n$\\tau$ & Random & Embedding & Dataflow & Emb $\\Delta$ (pp) \\\\\n\\midrule\n0.05 & 0.530 & 0.540 & 0.532 & $+$1.0 \\\\\n0.10 & 0.537 & 0.545 & 0.537 & $+$0.8 \\\\\n0.20 & 0.521 & 0.526 & 0.520 & $+$0.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{R@1 by temperature (StarCoder). Same pattern: ranking preserved, delta shrinks.}\n\\label{tab:temp-starcoder}\n\\begin{tabular}{ccccc}\n\\toprule\n$\\tau$ & Random & Embedding & Dataflow & Emb $\\Delta$ (pp) \\\\\n\\midrule\n0.05 & 0.443 & 0.450 & 0.437 & $+$0.7 \\\\\n0.10 & 0.451 & 0.457 & 0.446 & $+$0.6 \\\\\n0.20 & 0.435 & 0.438 & 0.430 & $+$0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Training Data Size.}\nTable~\\ref{tab:datasize} shows R@1 at 1K, 3K, and 5K training instances (Qwen).\nEmbedding mining benefit scales with data size ($+$0.3\\pp{} at 1K, $+$1.0\\pp{} at 5K), indicating the advantage is not an overfitting artifact.\nHowever, scaling is sub-linear, suggesting that pretrained representation quality is the bottleneck.\n\n\\begin{table}[t]\n\\centering\n\\caption{R@1 by training data size (Qwen). Embedding advantage grows with data, sub-linearly.}\n\\label{tab:datasize}\n\\begin{tabular}{lcccc}\n\\toprule\nSize & Random & Embedding & Dataflow & Emb $\\Delta$ (pp) \\\\\n\\midrule\n1K       & 0.498 & 0.501 & 0.495 & $+$0.3 \\\\\n3K       & 0.519 & 0.528 & 0.521 & $+$0.9 \\\\\n5K (full)& 0.530 & 0.540 & 0.532 & $+$1.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Fusion Head.}\nTable~\\ref{tab:fusion} ablates inference-time scoring: embedding-only vs.\\ structural-features-only vs.\\ combined.\nThe combined head adds only $+$0.2\\pp{} over embedding-only, confirming that the value of structural information lies in \\emph{training-time negative selection}, not inference-time feature fusion.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fusion head ablation. Structural features alone are weak; combining with embeddings adds marginal value.}\n\\label{tab:fusion}\n\\begin{tabular}{lcccc}\n\\toprule\nEncoder & Emb-only & Struct-only & Combined & Combined$-$Emb (pp) \\\\\n\\midrule\nQwen     & 0.539 & 0.412 & 0.541 & $+$0.2 \\\\\nStarCoder & 0.449 & 0.378 & 0.451 & $+$0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Call-Graph Hop Count.}\nTable~\\ref{tab:hopcnt} ablates the dataflow bounding at 1, 2, and 3 hops.\nDifferences are $<$0.5\\pp{}, with 2-hop slightly optimal.\nThe more informative finding is the high fallback rate at 1-hop (42\\%), confirming limited structural coverage.\n\n\\begin{table}[t]\n\\centering\n\\caption{Dataflow R@1 by hop count and negative pool statistics.}\n\\label{tab:hopcnt}\n\\begin{tabular}{lcccccc}\n\\toprule\n & \\multicolumn{2}{c}{R@1} & & \\multicolumn{2}{c}{Pool statistics} \\\\\n\\cmidrule{2-3} \\cmidrule{5-6}\nHops & Qwen & StarCoder & & Mean neg/query & Fallback \\% \\\\\n\\midrule\n1 & 0.530 & 0.434 & & 3.2 & 42\\% \\\\\n2 & 0.532 & 0.437 & & 8.7 & 28\\% \\\\\n3 & 0.529 & 0.436 & & 14.1 & 18\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Dynamic vs.\\ Static Mining.}\nWe tested dynamic re-mining (per-epoch) and found no significant improvement over static mining ($\\Delta = +0.4\\pp{}$, CI: [$-$0.8, 1.6], $p = 0.38$) despite 2.3$\\times$ training time.\nThis is expected: over 2--3 epochs the encoder changes minimally, so re-mined negatives overlap $>$80\\% with static ones.\n\n\\begin{table}[t]\n\\centering\n\\caption{Static vs.\\ dynamic embedding mining (Qwen). Dynamic adds negligible benefit at 2.3$\\times$ cost.}\n\\label{tab:dynamic}\n\\begin{tabular}{lcccc}\n\\toprule\nMining & R@1 & $\\Delta$ vs static (pp) & Train time (h) & 95\\% CI \\\\\n\\midrule\nStatic  & 0.540 & --- & 7.5 & --- \\\\\nDynamic & 0.544 & $+$0.4 & 17.3 & [$-$0.8, 1.6] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Weighted vs.\\ Binary Dataflow Negatives.}\nDistance-weighted sampling by dataflow distance provides no significant improvement over binary connected/disconnected selection ($+$0.3\\pp{}, CI: [$-$0.8, 1.4]).\nBinary selection is simpler and preferred.\n\n\\begin{table}[t]\n\\centering\n\\caption{Binary vs.\\ weighted dataflow negatives. No significant difference.}\n\\label{tab:weighted}\n\\begin{tabular}{lccc}\n\\toprule\nEncoder & Binary DF R@1 & Weighted DF R@1 & $\\Delta$ (pp) \\\\\n\\midrule\nQwen     & 0.532 & 0.535 & $+$0.3 \\\\\nStarCoder & 0.437 & 0.439 & $+$0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Failure Analysis and Case Studies}\n\\label{sec:failure}\n\n\\paragraph{Failure Categorization.}\nWe manually analyzed 50 retrieval failures from SWE-bench (Table~\\ref{tab:failure}).\nThe largest category is lexical gap (36\\%), where query wording differs entirely from target file content---neither mining strategy addresses this.\nStructural gap cases (28\\%) are where dataflow helps most (57\\% of such cases), but this ceiling limits overall impact.\n\n\\begin{table}[t]\n\\centering\n\\caption{Failure categories from 50 SWE-bench retrieval failures, with per-strategy help rates.}\n\\label{tab:failure}\n\\begin{tabular}{lcccc}\n\\toprule\nCategory & Count (\\%) & DF helps & Emb helps \\\\\n\\midrule\nStructural gap      & 14 (28\\%) & 8 (57\\%) & 5 (36\\%) \\\\\nLexical gap         & 18 (36\\%) & 3 (17\\%) & 6 (33\\%) \\\\\nMulti-file dep.     &  8 (16\\%) & 4 (50\\%) & 5 (63\\%) \\\\\nOther               & 10 (20\\%) & 1 (10\\%) & 2 (20\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Illustrative Case Studies.}\nTable~\\ref{tab:cases} presents 7 selected cases where strategies changed retrieval outcome.\nThese are chosen to illustrate the mechanism, not as representative evidence---overall effect sizes are modest (Tables~\\ref{tab:four-strategy}--\\ref{tab:repobench}).\nDataflow uniquely helps in cases involving cross-module callees, config propagation, and dependency cycles, where structural connectivity provides signal orthogonal to text similarity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Selected qualitative cases. Ranks are within the candidate pool. Cases are illustrative, not representative.}\n\\label{tab:cases}\n\\begin{tabular}{clcccl}\n\\toprule\n\\# & Issue type & Rand & Emb & DF & Key observation \\\\\n\\midrule\n1 & Missing import     & 12 & 8 & 2 & DF finds cross-module callee \\\\\n2 & API mismatch       &  9 & 3 & 4 & Emb finds similar naming \\\\\n3 & Config propagation & 15 & 11 & 1 & DF traces config flow \\\\\n4 & Type error         &  6 & 2 & 3 & Both find related types \\\\\n5 & Null pointer       & 11 & 7 & 3 & DF finds data source \\\\\n6 & Method override    &  4 & 1 & 5 & Emb captures signature sim \\\\\n7 & Circular dep       & 14 & 10 & 2 & DF traces dependency cycle \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Comparison with Inference-Time Graph Methods}\n\\label{sec:inference-comparison}\n\nTable~\\ref{tab:inference-methods} positions our approach relative to inference-time graph methods.\nThe key distinction is that these methods navigate structure at inference time, while we use structure for training-time data curation.\nThe two approaches are in principle complementary---a retriever trained with structure-grounded negatives could serve as the backbone for an inference-time graph navigator---but we have not experimentally verified this complementarity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Comparison with inference-time graph methods. StructFuse operates at training time, making it complementary.}\n\\label{tab:inference-methods}\n\\begin{tabular}{llll}\n\\toprule\nMethod & Graph type & When used & Complementary? \\\\\n\\midrule\nCodexGraph & Repository graph & Inference & Yes \\\\\nLocAgent   & Code structure   & Inference & Yes \\\\\nRANGER     & AST + deps       & Inference & Yes \\\\\n\\sysname{} (ours) & Dataflow  & Training  & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%----------------------------------------------------------------------\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Summary of Findings.}\nTrue embedding-distance mining tends to improve contrastive code retrieval over random baselines, with consistent direction across two encoders, two benchmarks, multiple seeds, and a range of hyperparameters.\nHowever, effect sizes are modest (0.5--1.0\\pp{} R@1 in most conditions, up to 1.8\\pp{} in favorable strata), and multi-seed confidence intervals are wide (2--4\\pp{}), with some seed-level deltas $< 0.5\\pp$.\nBM25-proxy negatives trend toward harm, consistent with the hypothesis that CoCoHaNeRe's reported $-27\\pp{}$ was amplified by proxy conflation, but our BM25 effect is not statistically significant ($p > 0.05$).\n\n\\paragraph{Dataflow as Exploratory Observation.}\nDataflow-grounded negatives show an encoder--strategy interaction: marginal positive effect on Qwen (CI includes 0) and negative effect on StarCoder.\nThis is consistent with a representation saturation hypothesis---when the encoder's pretrained space has high positive similarity (Qwen: $\\text{pos\\_sim} = 0.99$), structural negatives may provide an orthogonal signal dimension.\nHowever, the evidence is insufficient for an independent claim, and we present this as an exploratory observation that merits further investigation with more encoders.\n\n\\paragraph{Where Mining Matters.}\nStratified analysis reveals that mining benefit concentrates in specific conditions: small repositories, hard negative difficulty quartiles, and medium query-positive similarity ranges.\nThese are precisely the conditions where the encoder's ability to discriminate is most challenged.\nHowever, these favorable conditions represent a minority of real-world instances, diluting the overall effect.\n\n\\paragraph{Practical Implications.}\nFor practitioners choosing a negative mining strategy for code retrieval:\n(1)~embedding-distance mining is a reasonable default that tends to help and is unlikely to harm;\n(2)~avoid using BM25 top-$k$ as a proxy for embedding-distance negatives;\n(3)~structural negatives via dataflow are not recommended as a general-purpose strategy given limited coverage (34\\%), encoder-dependent effects, and modest overall benefit.\n\n\\paragraph{Limitations.}\n\\begin{itemize}\n    \\item \\textbf{Two encoders}: Our interaction finding rests on $n=2$ encoders. Generalization requires broader evaluation.\n    \\item \\textbf{Pool size}: Training uses pool=50; at realistic pool sizes (200--1000+), strategy advantages shrink further (Table~\\ref{tab:pool-qwen}).\n    \\item \\textbf{Structural coverage}: Dataflow data is available for only 34\\% of instances, diluting any structural benefit.\n    \\item \\textbf{SWE-bench power}: With $N=300$ binary outcomes, SWE-bench is underpowered to detect retrieval-stage deltas $< 2\\pp{}$.\n    \\item \\textbf{Single training domain}: All training uses SWE-smith; domain shift to other retrieval tasks may alter findings.\n    \\item \\textbf{Effect magnitude}: All observed deltas are $\\leq 2\\pp{}$, which may be within the noise floor for practical deployment decisions.\n\\end{itemize}\n\n%----------------------------------------------------------------------\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented a systematic study of hard negative mining strategies for contrastive code retrieval, comparing random, BM25-proxy, embedding-distance, and dataflow-disconnected negatives across two encoders, two benchmarks, and extensive ablations.\nOur results suggest that true embedding-distance mining tends to help and that prior reports of harm were likely confounded by BM25-proxy conflation, though the evidence for the latter is directional rather than conclusive.\nStructure-grounded negatives show an intriguing encoder-dependent interaction but do not provide consistent benefit and remain an exploratory observation.\nStratified analysis reveals that mining benefit concentrates in specific conditions, providing a representation geometry explanation for the heterogeneous findings in the literature.\nWe hope this systematic analysis helps the community make more informed choices about negative mining strategies and motivates further investigation into the interaction between encoder properties and training data curation.\n\n%----------------------------------------------------------------------\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[Karpukhin et~al.(2020)]{karpukhin2020dense}\nV.~Karpukhin, B.~Oguz, S.~Min, P.~Lewis, L.~Wu, S.~Edunov, D.~Chen, and W.~Yih.\n\\newblock Dense passage retrieval for open-domain question answering.\n\\newblock In \\emph{EMNLP}, 2020.\n\n\\bibitem[Xiong et~al.(2021)]{xiong2021approximate}\nL.~Xiong, C.~Xiong, Y.~Li, K.-F.~Tang, J.~Liu, P.~Bennett, J.~Ahmed, and A.~Overwijk.\n\\newblock Approximate nearest neighbor negative contrastive learning for dense text retrieval.\n\\newblock In \\emph{ICLR}, 2021.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "0d71eb6e-fe8c-4be8-ad45-07536d413486",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T162530 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-conte…",
  "leafUuid": "814ed8eb-5ad3-4e5d-b697-a1571d361c9e",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier simulation paper for dream ID",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3"
}
```

---

### Tool call

_source line 22 · 2026-05-14T16:54:10.249Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UJkqkPWSs2c55HaCbtZCc7`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "814ed8eb-5ad3-4e5d-b697-a1571d361c9e",
  "isSidechain": false,
  "requestId": "req_011Cb2oxs3S8cFWUc9Uo9FMZ",
  "type": "assistant",
  "uuid": "b6e064e9-241e-47db-9497-1b8f68312303",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D2xZWafs6t5F8YSp2LWXbo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11099,
      "cache_read_input_tokens": 45781,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11099,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 45781,
          "cache_creation_input_tokens": 11099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11099
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

_source line 23 · 2026-05-14T16:54:11.367Z_

<details><summary>↩ Tool result · `toolu_01UJkqkPWSs2c55HaCbtZCc7`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `karpukhin2020dense' on page 1 undefined on in
put line 40.


Package natbib Warning: Citation `xiong2021approximate' on page 1 undefined on 
input line 40.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

Package natbib Warning: Citation `karpukhin2020dense' on page 2 undefined on in
put line 66.


Package natbib Warning: Citation `xiong2021approximate' on page 2 undefined on 
input line 67.

[2]

LaTeX Warning: Reference `tab:four-strategy' on page 3 undefined on input line 
128.


Overfull \hbox (2.54057pt too wide) in paragraph at lines 128--132
\T1/cmr/m/n/10.95 Table [] re-ports R@1 for all four strate-gies across both en
-coders on SWE-smith val-i-da-tion (pool=50).

LaTeX Warning: Reference `tab:bm25-gap' on page 3 undefined on input line 150.

[3]

LaTeX Warning: Reference `tab:repobench' on page 4 undefined on input line 172.



LaTeX Warning: Reference `tab:swebench' on page 4 undefined on input line 195.


LaTeX Warning: Reference `tab:swebench-ci' on page 4 undefined on input line 19
5.


LaTeX Warning: Reference `tab:strat-repo' on page 4 undefined on input line 237
.

[4]

LaTeX Warning: Reference `tab:strat-structural' on page 5 undefined on input li
ne 257.


LaTeX Warning: Reference `tab:strat-negdiff' on page 5 undefined on input line 
276.


LaTeX Warning: Reference `tab:pool-qwen' on page 5 undefined on input line 300.



LaTeX Warning: Reference `tab:pool-starcoder' on page 5 undefined on input line
 300.


LaTeX Warning: Reference `tab:temp-qwen' on page 5 undefined on input line 342.


[5]

LaTeX Warning: Reference `tab:datasize' on page 6 undefined on input line 377.


LaTeX Warning: Reference `tab:fusion' on page 6 undefined on input line 397.


LaTeX Warning: Reference `tab:hopcnt' on page 6 undefined on input line 415.


LaTeX Warning: Reference `tab:failure' on page 6 undefined on input line 476.

[6]

LaTeX Warning: Reference `tab:cases' on page 7 undefined on input line 497.


LaTeX Warning: Reference `tab:four-strategy' on page 7 undefined on input line 
498.


LaTeX Warning: Reference `tab:repobench' on page 7 undefined on input line 498.



LaTeX Warning: Reference `tab:inference-methods' on page 7 undefined on input l
ine 523.


Overfull \hbox (2.60597pt too wide) in paragraph at lines 553--556
 []\T1/cmr/bx/n/10.95 Dataflow as Ex-ploratory Ob-ser-va-tion.[] \T1/cmr/m/n/10
.95 Dataflow-grounded neg-a-tives show an encoder--strategy
[7]

LaTeX Warning: Reference `tab:pool-qwen' on page 8 undefined on input line 571.


[8]

Package natbib Warning: There were undefined citations.

[9] [10] [11] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/symbols/msam10.pfb>
Output written on paper.pdf (11 pages, 217325 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(./paper.out) (./paper.out)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}] [2] [3] [4] [5] [6]
Overfull \hbox (2.60597pt too wide) in paragraph at lines 553--556
 []\T1/cmr/bx/n/10.95 Dataflow as Ex-ploratory Ob-ser-va-tion.[] \T1/cmr/m/n/10
.95 Dataflow-grounded neg-a-tives show an encoder--strategy
[7] [8] [9] [10] [11] (./paper.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/symbols/msam10.pfb>
Output written on paper.pdf (11 pages, 219783 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6e064e9-241e-47db-9497-1b8f68312303",
  "isSidechain": false,
  "promptId": "2a7bf294-76bc-4051-b2db-b0a0f92c173c",
  "type": "user",
  "uuid": "43cb2733-4b3b-4ea8-8934-d42dff58d2ac",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `karpukhin2020dense' on page 1 undefined on in\nput line 40.\n\n\nPackage natbib Warning: Citation `xiong2021approximate' on page 1 undefined on \ninput line 40.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nPackage natbib Warning: Citation `karpukhin2020dense' on page 2 undefined on in\nput line 66.\n\n\nPackage natbib Warning: Citation `xiong2021approximate' on page 2 undefined on \ninput line 67.\n\n[2]\n\nLaTeX Warning: Reference `tab:four-strategy' on page 3 undefined on input line \n128.\n\n\nOverfull \\hbox (2.54057pt too wide) in paragraph at lines 128--132\n\\T1/cmr/m/n/10.95 Table [] re-ports R@1 for all four strate-gies across both en\n-coders on SWE-smith val-i-da-tion (pool=50).\n\nLaTeX Warning: Reference `tab:bm25-gap' on page 3 undefined on input line 150.\n\n[3]\n\nLaTeX Warning: Reference `tab:repobench' on page 4 undefined on input line 172.\n\n\n\nLaTeX Warning: Reference `tab:swebench' on page 4 undefined on input line 195.\n\n\nLaTeX Warning: Reference `tab:swebench-ci' on page 4 undefined on input line 19\n5.\n\n\nLaTeX Warning: Reference `tab:strat-repo' on page 4 undefined on input line 237\n.\n\n[4]\n\nLaTeX Warning: Reference `tab:strat-structural' on page 5 undefined on input li\nne 257.\n\n\nLaTeX Warning: Reference `tab:strat-negdiff' on page 5 undefined on input line \n276.\n\n\nLaTeX Warning: Reference `tab:pool-qwen' on page 5 undefined on input line 300.\n\n\n\nLaTeX Warning: Reference `tab:pool-starcoder' on page 5 undefined on input line\n 300.\n\n\nLaTeX Warning: Reference `tab:temp-qwen' on page 5 undefined on input line 342.\n\n\n[5]\n\nLaTeX Warning: Reference `tab:datasize' on page 6 undefined on input line 377.\n\n\nLaTeX Warning: Reference `tab:fusion' on page 6 undefined on input line 397.\n\n\nLaTeX Warning: Reference `tab:hopcnt' on page 6 undefined on input line 415.\n\n\nLaTeX Warning: Reference `tab:failure' on page 6 undefined on input line 476.\n\n[6]\n\nLaTeX Warning: Reference `tab:cases' on page 7 undefined on input line 497.\n\n\nLaTeX Warning: Reference `tab:four-strategy' on page 7 undefined on input line \n498.\n\n\nLaTeX Warning: Reference `tab:repobench' on page 7 undefined on input line 498.\n\n\n\nLaTeX Warning: Reference `tab:inference-methods' on page 7 undefined on input l\nine 523.\n\n\nOverfull \\hbox (2.60597pt too wide) in paragraph at lines 553--556\n []\\T1/cmr/bx/n/10.95 Dataflow as Ex-ploratory Ob-ser-va-tion.[] \\T1/cmr/m/n/10\n.95 Dataflow-grounded neg-a-tives show an encoder--strategy\n[7]\n\nLaTeX Warning: Reference `tab:pool-qwen' on page 8 undefined on input line 571.\n\n\n[8]\n\nPackage natbib Warning: There were undefined citations.\n\n[9] [10] [11] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/symbols/msam10.pfb>\nOutput written on paper.pdf (11 pages, 217325 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2] [3] [4] [5] [6]\nOverfull \\hbox (2.60597pt too wide) in paragraph at lines 553--556\n []\\T1/cmr/bx/n/10.95 Dataflow as Ex-ploratory Ob-ser-va-tion.[] \\T1/cmr/m/n/10\n.95 Dataflow-grounded neg-a-tives show an encoder--strategy\n[7] [8] [9] [10] [11] (./paper.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/symbols/msam10.pfb>\nOutput written on paper.pdf (11 pages, 219783 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b6e064e9-241e-47db-9497-1b8f68312303",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T162530 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-conte…",
  "leafUuid": "43cb2733-4b3b-4ea8-8934-d42dff58d2ac",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier simulation paper for dream ID",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3"
}
```

---

### Assistant

_source line 26 · 2026-05-14T16:54:17.519Z_

编译成功，生成 11 页 PDF。`paper.pdf` 已写入 `median/` 目录，覆盖全部 14 个实验的对应 table/section，所有数字来自 `experiment_data.json`，叙事按 narrative guidance 做了降级处理（Claim 1 → "tends to help"，Claim 2 → exploratory observation，SWE-bench → sanity check，CoCoHaNeRe → partial directional support）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43cb2733-4b3b-4ea8-8934-d42dff58d2ac",
  "isSidechain": false,
  "requestId": "req_011Cb2oyZAgCmDk3x6FHtrCe",
  "type": "assistant",
  "uuid": "7e9474a7-f469-4651-bbd2-a8225d728708",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0162zQToh5GKJnLGCvVPJ8UP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6850,
      "cache_read_input_tokens": 56880,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6850,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 56880,
          "cache_creation_input_tokens": 6850,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6850
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T162530 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-conte…",
  "leafUuid": "7e9474a7-f469-4651-bbd2-a8225d728708",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier simulation paper for dream ID",
  "sessionId": "c4732633-03f2-4c45-a505-c2eda85a35f3"
}
```

---
