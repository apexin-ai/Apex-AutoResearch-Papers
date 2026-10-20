# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260513T081019 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/dbc865db-dd7a-482c-ac48-3666a2c55ae3.jsonl`
- **Structured JSON:** [`fc5cba67230f466404ac.json`](../../sessions/fc/fc5cba67230f466404ac.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-13T08:33:54.855Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-13T08:33:54.855Z",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260513T081019 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/experiment_data.json`（先 Read 此文件）\n- Venue：EMNLP 2026 ARR\n- Narrative guidance：原始 framing 完全可用。标题保留 \"Alignment Gap\" + \"Accelerates Collapse\"。\nplan_001 提供锚定数据：C1 用 selection ratio 单调下降曲线 (1.04→0.52) 做主图；\nC3 用 RGDS vs uncurated 的 PPL/rare 分叉做第二主图；\nC2-weak 通过 external_only 对照自然呈现 (ratio >1.2, PPL 优于 uncurated, rare ≈ uncurated)。\nplan_004/005 提供 3-seed 统计，CI 不跨零，挡住 R3 (N=1) 攻击。\nplan_006/007 提供 GPT2-medium 结果，挡住 R1 (scale) 攻击。\nplan_008 re-anchoring 作为 §6 缓解实验，rare 改善 ~33%，升级为 \"found + partial fix\"。\nplan_009 OpenWebText 挡住 R2 (dataset 单一性) 攻击。\n可投 main conference 8 页，审稿人主攻面缩小到 scale（仍在 GPT2 家族内）和缓解方案的简单性。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-13T08:33:54.858Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-13T08:33:54.858Z",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3"
}
```

---

## Round 1

43 recorded events

### User

_source line 3 · 2026-05-13T08:33:54.878Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260513T081019 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/experiment_data.json`（先 Read 此文件）
- Venue：EMNLP 2026 ARR
- Narrative guidance：原始 framing 完全可用。标题保留 "Alignment Gap" + "Accelerates Collapse"。
plan_001 提供锚定数据：C1 用 selection ratio 单调下降曲线 (1.04→0.52) 做主图；
C3 用 RGDS vs uncurated 的 PPL/rare 分叉做第二主图；
C2-weak 通过 external_only 对照自然呈现 (ratio >1.2, PPL 优于 uncurated, rare ≈ uncurated)。
plan_004/005 提供 3-seed 统计，CI 不跨零，挡住 R3 (N=1) 攻击。
plan_006/007 提供 GPT2-medium 结果，挡住 R1 (scale) 攻击。
plan_008 re-anchoring 作为 §6 缓解实验，rare 改善 ~33%，升级为 "found + partial fix"。
plan_009 OpenWebText 挡住 R2 (dataset 单一性) 攻击。
可投 main conference 8 页，审稿人主攻面缩小到 scale（仍在 GPT2 家族内）和缓解方案的简单性。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ad861b3f-869b-46c3-a458-a9928fad5b05",
  "type": "user",
  "uuid": "378dd44f-0d54-48a4-a818-a288edf927d4",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-13T08:33:54.877Z_

```json
{
  "parentUuid": "378dd44f-0d54-48a4-a818-a288edf927d4",
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
  "uuid": "b318e95d-672b-492a-8847-e648c2f807a4",
  "timestamp": "2026-05-13T08:33:54.877Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-13T08:33:54.877Z_

```json
{
  "parentUuid": "b318e95d-672b-492a-8847-e648c2f807a4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1a27095a-0c6e-486a-87f2-d8c9d10aae14",
  "timestamp": "2026-05-13T08:33:54.877Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
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
  "aiTitle": "Generate EMNLP paper on alignment gap and model collapse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3"
}
```

---

### Assistant

_source line 7 · 2026-05-13T08:33:58.544Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a27095a-0c6e-486a-87f2-d8c9d10aae14",
  "isSidechain": false,
  "requestId": "req_011CazG21S4JJLvuQpJtqiMP",
  "type": "assistant",
  "uuid": "52841c35-5bf0-4f95-a692-e9289033bc83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4CnDWByufTH1u2J2Woz4i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11426,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11426
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

_source line 8 · 2026-05-13T08:33:59.087Z_

<details open><summary>🔧 Tool call — Read · `toolu_011feud5iYieHLw8Trgavm5x`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52841c35-5bf0-4f95-a692-e9289033bc83",
  "isSidechain": false,
  "requestId": "req_011CazG21S4JJLvuQpJtqiMP",
  "type": "assistant",
  "uuid": "4cf3d0dc-8505-4f4c-804e-41389f4174d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4CnDWByufTH1u2J2Woz4i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11426,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11426
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

_source line 9 · 2026-05-13T08:33:59.501Z_

<details><summary>↩ Tool result · `toolu_011feud5iYieHLw8Trgavm5x`</summary>

```text
1	[
2	  {
3	    "name": "Phase 2 三方法对比 (GPT2-125M, WikiText-103, seed=42)",
4	    "description": "Self-iterate GPT2-125M × 8 gens × 3 methods (uncurated/RGDS/external_only)。锚定全部 claims 的主实验。",
5	    "results": {
6	      "rgds": {
7	        "gen0": {
8	          "ppl": 37.2,
9	          "sel_ratio": 1.04,
10	          "rare": 0.0288,
11	          "rank_corr": -0.058,
12	          "rankme": 281.5,
13	          "knn": 0.988
14	        },
15	        "gen1": {
16	          "ppl": 42.5,
17	          "sel_ratio": 0.96,
18	          "rare": 0.0208,
19	          "rank_corr": -0.074,
20	          "rankme": 290.2,
21	          "knn": 0.988
22	        },
23	        "gen2": {
24	          "ppl": 49.8,
25	          "sel_ratio": 0.87,
26	          "rare": 0.0152,
27	          "rank_corr": -0.089,
28	          "rankme": 296.4,
29	          "knn": 0.987
30	        },
31	        "gen3": {
32	          "ppl": 56.3,
33	          "sel_ratio": 0.79,
34	          "rare": 0.0113,
35	          "rank_corr": -0.103,
36	          "rankme": 300.1,
37	          "knn": 0.988
38	        },
39	        "gen4": {
40	          "ppl": 61.7,
41	          "sel_ratio": 0.71,
42	          "rare": 0.0086,
43	          "rank_corr": -0.118,
44	          "rankme": 303.2,
45	          "knn": 0.988
46	        },
47	        "gen5": {
48	          "ppl": 66.4,
49	          "sel_ratio": 0.64,
50	          "rare": 0.0068,
51	          "rank_corr": -0.131,
52	          "rankme": 301.8,
53	          "knn": 0.988
54	        },
55	        "gen6": {
56	          "ppl": 70.1,
57	          "sel_ratio": 0.57,
58	          "rare": 0.0055,
59	          "rank_corr": -0.143,
60	          "rankme": 298.5,
61	          "knn": 0.988
62	        },
63	        "gen7": {
64	          "ppl": 72.8,
65	          "sel_ratio": 0.52,
66	          "rare": 0.0046,
67	          "rank_corr": -0.155,
68	          "rankme": 294.3,
69	          "knn": 0.988
70	        }
71	      },
72	      "uncurated": {
73	        "gen0": {
74	          "ppl": 37.1,
75	          "rare": 0.029,
76	          "rank_corr": -0.023,
77	          "rankme": 280.3,
78	          "knn": 0.988
79	        },
80	        "gen1": {
81	          "ppl": 44.9,
82	          "rare": 0.0192,
83	          "rank_corr": -0.055,
84	          "rankme": 297.8,
85	          "knn": 0.988
86	        },
87	        "gen2": {
88	          "ppl": 51.6,
89	          "rare": 0.0139,
90	          "rank_corr": -0.049,
91	          "rankme": 302.6,
92	          "knn": 0.987
93	        },
94	        "gen3": {
95	          "ppl": 57.0,
96	          "rare": 0.0116,
97	          "rank_corr": -0.044,
98	          "rankme": 303.3,
99	          "knn": 0.988
100	        },
101	        "gen4": {
102	          "ppl": 55.7,
103	          "rare": 0.0101,
104	          "rank_corr": -0.042,
105	          "rankme": 301.3,
106	          "knn": 0.988
107	        },
108	        "gen5": {
109	          "ppl": 51.7,
110	          "rare": 0.0098,
111	          "rank_corr": -0.048,
112	          "rankme": 297.4,
113	          "knn": 0.988
114	        },
115	        "gen6": {
116	          "ppl": 48.7,
117	          "rare": 0.0089,
118	          "rank_corr": -0.065,
119	          "rankme": 293.0,
120	          "knn": 0.988
121	        },
122	        "gen7": {
123	          "ppl": 48.1,
124	          "rare": 0.0087,
125	          "rank_corr": -0.087,
126	          "rankme": 289.8,
127	          "knn": 0.988
128	        }
129	      },
130	      "external_only": {
131	        "gen0": {
132	          "ppl": 36.8,
133	          "sel_ratio": 1.08,
134	          "rare": 0.0289,
135	          "rank_corr": -0.024,
136	          "rankme": 280.8,
137	          "knn": 0.988
138	        },
139	        "gen1": {
140	          "ppl": 42.2,
141	          "sel_ratio": 1.12,
142	          "rare": 0.0194,
143	          "rank_corr": -0.032,
144	          "rankme": 296.5,
145	          "knn": 0.988
146	        },
147	        "gen2": {
148	          "ppl": 47.5,
149	          "sel_ratio": 1.15,
150	          "rare": 0.0141,
151	          "rank_corr": -0.036,
152	          "rankme": 302.0,
153	          "knn": 0.987
154	        },
155	        "gen3": {
156	          "ppl": 50.8,
157	          "sel_ratio": 1.18,
158	          "rare": 0.0118,
159	          "rank_corr": -0.039,
160	          "rankme": 303.0,
161	          "knn": 0.988
162	        },
163	        "gen4": {
164	          "ppl": 50.3,
165	          "sel_ratio": 1.21,
166	          "rare": 0.0103,
167	          "rank_corr": -0.041,
168	          "rankme": 300.5,
169	          "knn": 0.988
170	        },
171	        "gen5": {
172	          "ppl": 48.2,
173	          "sel_ratio": 1.24,
174	          "rare": 0.0097,
175	          "rank_corr": -0.04,
176	          "rankme": 296.8,
177	          "knn": 0.988
178	        },
179	        "gen6": {
180	          "ppl": 46.5,
181	          "sel_ratio": 1.26,
182	          "rare": 0.0091,
183	          "rank_corr": -0.038,
184	          "rankme": 292.5,
185	          "knn": 0.988
186	        },
187	        "gen7": {
188	          "ppl": 45.8,
189	          "sel_ratio": 1.28,
190	          "rare": 0.0088,
191	          "rank_corr": -0.037,
192	          "rankme": 289.4,
193	          "knn": 0.988
194	        }
195	      },
196	      "derived": {
197	        "rgds_ppl_excess_vs_uncurated_pct": 51.4,
198	        "rgds_rare_deficit_vs_uncurated_pct": 47.1,
199	        "external_ppl_improvement_vs_uncurated_pct": -4.8,
200	        "external_rare_vs_uncurated_pct": 1.1
201	      }
202	    },
203	    "tables": [
204	      "Table 1: Gen 0-7 三方法全指标（PPL, rare, sel_ratio, rank_corr, RankMe, k-NN）",
205	      "Table 2: Gen 7 汇总 + 方法间相对差异百分比"
206	    ],
207	    "figures": [],
208	    "analysis": "C1 成立：selection ratio 单调下降 8 代，效应量大（1.04→0.52），不可归因于噪声。\nC2-weak 成立：external ratio 始终 >1.0 且上升，与 internal 形成鲜明对照。\nC3 成立：RGDS PPL +51%、rare -47% vs uncurated，完整因果链闭合。\nS1 成立：external PPL -4.8% 但 rare +1.1%，PPL 与 rare 解耦。\nS2 成立：RankMe 在崩塌过程中反而上升（280→303），k-NN 稳定，无法检测多样性衰退。\n\n\nRGDS: self-iterate 导致内部嵌入空间收缩（neural collapse 类机制）。\n随代际推进，模型嵌入的\"几何多样性\"方向逐渐对齐到高频词汇模式上，\n贪心子模选择在低维空间中选中的\"远点\"恰好是词汇贫乏的样本。\nselection ratio 从 1.04 单调降至 0.52 反映了这种对齐错位的加剧。\n训练在词汇贫乏子集上 → PPL 从 37.2 飙升到 72.8（+51%），\nrare n-gram 从 0.029 降至 0.0046（-84%），远超 uncurated 的自然崩塌幅度。\n\nuncurated: 无选择偏差，PPL 先升后降（gen3 峰值 57.0 → gen7 回落 48.1），\nrare n-gram 持续下降到 0.0087（-70%）。\nPPL 回落是因为模型逐渐\"记住\"自身分布，但词汇多样性不可逆损失。\n\nexternal_only: Contriever 冻结不受训练反馈影响，diversity 信号始终校准到原始分布。\nselection ratio 稳定上升（1.08→1.28），说明它确实在挑\"更不像已有训练集\"的样本。\nPPL 略优于 uncurated（45.8 vs 48.1，-4.8%）因为语义多样性选择提供了更有信息量的训练数据。\n但 rare n-gram（0.0088）≈ uncurated（0.0087），说明语义多样性 ≠ 词汇多样性——\nContriever 捕捉的是主题/语义距离而非低频词分布。\n"
209	  },
210	  {
211	    "name": "External_only seed=123 复现",
212	    "description": "验证 external_only selection ratio >1.0 在不同种子下的可复现性。plan_004 的子集先行实验。",
213	    "results": {
214	      "external_only": {
215	        "gen0": {
216	          "ppl": 37.0,
217	          "sel_ratio": 1.07,
218	          "rare": 0.0291
219	        },
220	        "gen4": {
221	          "ppl": 50.8,
222	          "sel_ratio": 1.19,
223	          "rare": 0.0105
224	        },
225	        "gen7": {
226	          "ppl": 46.5,
227	          "sel_ratio": 1.25,
228	          "rare": 0.009
229	        }
230	      }
231	    },
232	    "tables": [],
233	    "figures": [],
234	    "analysis": "结果合并入 plan_004 的 3-seed 统计。单独作用是在 plan_001 完成前快速确认 C2-weak 方向。\n\nContriever 冻结模型的选择函数不受训练种子影响，\n但下游训练轨迹因初始化/采样随种子变化导致 ±5% 波动。\nsel_ratio 仍 >1.0 全程，确认 C2-weak 非种子偶然。\n"
235	  },
236	  {
237	    "name": "三方法 seed=123 完整复现 (GPT2-125M, WikiText-103)",
238	    "description": "3 methods × 8 gens, seed=123。第二个种子，与 plan_001 对比验证趋势可复现。",
239	    "results": {
240	      "rgds": {
241	        "gen0": {
242	          "ppl": 37.5,
243	          "sel_ratio": 1.03,
244	          "rare": 0.0285,
245	          "rank_corr": -0.062
246	        },
247	        "gen3": {
248	          "ppl": 57.8,
249	          "sel_ratio": 0.77,
250	          "rare": 0.0108,
251	          "rank_corr": -0.108
252	        },
253	        "gen7": {
254	          "ppl": 70.5,
255	          "sel_ratio": 0.54,
256	          "rare": 0.005,
257	          "rank_corr": -0.148
258	        }
259	      },
260	      "uncurated": {
261	        "gen0": {
262	          "ppl": 37.3,
263	          "rare": 0.0287,
264	          "rank_corr": -0.025
265	        },
266	        "gen3": {
267	          "ppl": 58.2,
268	          "rare": 0.0119,
269	          "rank_corr": -0.046
270	        },
271	        "gen7": {
272	          "ppl": 49.3,
273	          "rare": 0.0091,
274	          "rank_corr": -0.082
275	        }
276	      },
277	      "external_only": {
278	        "gen0": {
279	          "ppl": 37.0,
280	          "sel_ratio": 1.07,
281	          "rare": 0.0291,
282	          "rank_corr": -0.026
283	        },
284	        "gen3": {
285	          "ppl": 51.5,
286	          "sel_ratio": 1.17,
287	          "rare": 0.0121,
288	          "rank_corr": -0.041
289	        },
290	        "gen7": {
291	          "ppl": 46.5,
292	          "sel_ratio": 1.25,
293	          "rare": 0.009,
294	          "rank_corr": -0.04
295	        }
296	      },
297	      "derived": {
298	        "rgds_ppl_excess_vs_uncurated_pct": 43.0,
299	        "rgds_rare_deficit_vs_uncurated_pct": 45.1
300	      }
301	    },
302	    "tables": [
303	      "Table 3: seed=42 vs seed=123 gen7 核心指标对比"
304	    ],
305	    "figures": [],
306	    "analysis": "趋势方向完全复现。RGDS ratio <1.0 by gen2, external ratio >1.0 全程,\nRGDS PPL >> uncurated。种子间差异远小于方法间差异。\n\n\n所有方向性趋势与 seed=42 一致：RGDS ratio 单调下降、PPL 持续上升、external ratio 稳定 >1.0。\n点估计波动 ±5-8%——seed=123 的 RGDS gen7 PPL (70.5) 略低于 seed=42 (72.8)，\nsel_ratio (0.54) 略高于 seed=42 (0.52)。这是正常的种子间方差，来源于\nmini-batch 采样和初始化差异导致的训练轨迹分散。\n关键判据：方法间差异 (RGDS 70.5 vs uncurated 49.3 = Δ21.2) 远大于种子间差异 (70.5 vs 72.8 = Δ2.3)。\n"
307	  },
308	  {
309	    "name": "三方法 seed=456 完整复现 (GPT2-125M, WikiText-103)",
310	    "description": "第三个种子。与 seed=42/123 构成 N=3 统计检验基础，计算 95% CI。",
311	    "results": {
312	      "rgds": {
313	        "gen0": {
314	          "ppl": 36.9,
315	          "sel_ratio": 1.05,
316	          "rare": 0.0292,
317	          "rank_corr": -0.055
318	        },
319	        "gen3": {
320	          "ppl": 55.1,
321	          "sel_ratio": 0.81,
322	          "rare": 0.0117,
323	          "rank_corr": -0.099
324	        },
325	        "gen7": {
326	          "ppl": 74.2,
327	          "sel_ratio": 0.49,
328	          "rare": 0.0043,
329	          "rank_corr": -0.161
330	        }
331	      },
332	      "uncurated": {
333	        "gen0": {
334	          "ppl": 36.8,
335	          "rare": 0.0291,
336	          "rank_corr": -0.021
337	        },
338	        "gen3": {
339	          "ppl": 55.8,
340	          "rare": 0.0113,
341	          "rank_corr": -0.041
342	        },
343	        "gen7": {
344	          "ppl": 47.5,
345	          "rare": 0.0085,
346	          "rank_corr": -0.091
347	        }
348	      },
349	      "external_only": {
350	        "gen0": {
351	          "ppl": 36.5,
352	          "sel_ratio": 1.09,
353	          "rare": 0.0293,
354	          "rank_corr": -0.022
355	        },
356	        "gen3": {
357	          "ppl": 50.2,
358	          "sel_ratio": 1.2,
359	          "rare": 0.0122,
360	          "rank_corr": -0.037
361	        },
362	        "gen7": {
363	          "ppl": 44.9,
364	          "sel_ratio": 1.31,
365	          "rare": 0.0086,
366	          "rank_corr": -0.034
367	        }
368	      },
369	      "derived": {
370	        "rgds_ppl_excess_vs_uncurated_pct": 56.2,
371	        "rgds_rare_deficit_vs_uncurated_pct": 49.4
372	      },
373	      "three_seed_aggregation": {
374	        "note": "聚合 seed=42 (plan_001) + seed=123 (plan_004) + seed=456 (plan_005)",
375	        "rgds_gen7_ppl": {
376	          "mean": 72.5,
377	          "std": 1.85,
378	          "ci95": [
379	            67.9,
380	            77.1
381	          ]
382	        },
383	        "rgds_gen7_sel_ratio": {
384	          "mean": 0.517,
385	          "std": 0.025,
386	          "ci95": [
387	            0.455,
388	            0.579
389	          ]
390	        },
391	        "rgds_gen7_rare": {
392	          "mean": 0.00463,
393	          "std": 0.00035,
394	          "ci95": [
395	            0.00376,
396	            0.0055
397	          ]
398	        },
399	        "rgds_gen7_rank_corr": {
400	          "mean": -0.155,
401	          "std": 0.007,
402	          "ci95": [
403	            -0.171,
404	            -0.139
405	          ]
406	        },
407	        "uncurated_gen7_ppl": {
408	          "mean": 48.3,
409	          "std": 0.91,
410	          "ci95": [
411	            46.0,
412	            50.6
413	          ]
414	        },
415	        "uncurated_gen7_rare": {
416	          "mean": 0.00877,
417	          "std": 0.0003,
418	          "ci95": [
419	            0.00802,
420	            0.00952
421	          ]
422	        },
423	        "external_gen7_ppl": {
424	          "mean": 45.7,
425	          "std": 0.8,
426	          "ci95": [
427	            43.7,
428	            47.7
429	          ]
430	        },
431	        "external_gen7_sel_ratio": {
432	          "mean": 1.28,
433	          "std": 0.03,
434	          "ci95": [
435	            1.21,
436	            1.35
437	          ]
438	        },
439	        "external_gen7_rare": {
440	          "mean": 0.0088,
441	          "std": 0.0002,
442	          "ci95": [
443	            0.0083,
444	            0.0093
445	          ]
446	        },
447	        "external_gen7_rank_corr": {
448	          "mean": -0.037,
449	          "std": 0.003,
450	          "ci95": [
451	            -0.044,
452	            -0.03
453	          ]
454	        },
455	        "key_tests": {
456	          "rgds_sel_ratio_below_1": "CI [0.455, 0.579] 不跨 1.0 ✓",
457	          "external_sel_ratio_above_1": "CI [1.21, 1.35] 不跨 1.0 ✓",
458	          "rgds_ppl_above_uncurated": "CI 无重叠 (67.9-77.1 vs 46.0-50.6) ✓",
459	          "external_rare_eq_uncurated": "CI 重叠 (0.00830-0.00930 vs 0.00802-0.00952) → 差异不显著 ✓",
460	          "cohen_d_ppl": ">3 (极大效应量)"
461	        }
462	      }
463	    },
464	    "tables": [
465	      "Table 4: 3-seed 聚合统计（mean ± std, 95% CI）全指标"
466	    ],
467	    "figures": [],
468	    "analysis": "三种子全部复现主趋势方向。CI 不跨零/不跨 1.0，满足 best 档复现要求。\n方法间差异 (Δ=24.2 PPL) 远大于种子间差异 (std=1.9)，Cohen's d >3。\n审稿人 R3 (\"N=1 seed\") 完全被挡住。\n\n\nseed=456 的 RGDS gen7 PPL 最高 (74.2)、sel_ratio 最低 (0.49)——\n代表种子间方差的上界。三种子聚合后所有 CI 不跨关键阈值：\n- sel_ratio CI [0.455, 0.579] 远低于 1.0，C1 在统计上稳固\n- RGDS PPL CI [67.9, 77.1] 与 uncurated CI [46.0, 50.6] 无重叠，C3 稳固\n- external sel_ratio CI [1.21, 1.35] 远高于 1.0，C2-weak 稳固\n- external rare ≈ uncurated rare（CI 完全重叠），S1 稳固\n\nN=3 虽少，但效应量极大（Cohen's d >3），统计功效充足。\n关键是 8 代的单调趋势不是单点测量——每个种子贡献 8 个相关但独立的观测点，\n使得趋势的统计可靠性远超点估计。\n"
469	  },
470	  {
471	    "name": "GPT2-medium 355M 三方法对比 (WikiText-103, seed=42)",
472	    "description": "在 355M 参数模型上验证 alignment gap 存在。回应审稿人 R1 'GPT2-125M 太小'。",
473	    "results": {
474	      "rgds": {
475	        "gen0": {
476	          "ppl": 31.2,
477	          "sel_ratio": 1.05,
478	          "rare": 0.0295,
479	          "rank_corr": -0.051,
480	          "rankme": 342.1,
481	          "knn": 0.989
482	        },
483	        "gen1": {
484	          "ppl": 35.8,
485	          "sel_ratio": 0.97,
486	          "rare": 0.0218,
487	          "rank_corr": -0.064,
488	          "rankme": 351.4,
489	          "knn": 0.989
490	        },
491	        "gen2": {
492	          "ppl": 41.5,
493	          "sel_ratio": 0.89,
494	          "rare": 0.0163,
495	          "rank_corr": -0.078,
496	          "rankme": 357.2,
497	          "knn": 0.989
498	        },
499	        "gen3": {
500	          "ppl": 47.2,
501	          "sel_ratio": 0.81,
502	          "rare": 0.0122,
503	          "rank_corr": -0.091,
504	          "rankme": 361.8,
505	          "knn": 0.989
506	        },
507	        "gen4": {
508	          "ppl": 52.7,
509	          "sel_ratio": 0.74,
510	          "rare": 0.0094,
511	          "rank_corr": -0.104,
512	          "rankme": 363.5,
513	          "knn": 0.989
514	        },
515	        "gen5": {
516	          "ppl": 57.1,
517	          "sel_ratio": 0.67,
518	          "rare": 0.0075,
519	          "rank_corr": -0.116,
520	          "rankme": 361.2,
521	          "knn": 0.989
522	        },
523	        "gen6": {
524	          "ppl": 60.8,
525	          "sel_ratio": 0.61,
526	          "rare": 0.0062,
527	          "rank_corr": -0.127,
528	          "rankme": 357.8,
529	          "knn": 0.989
530	        },
531	        "gen7": {
532	          "ppl": 63.5,
533	          "sel_ratio": 0.56,
534	          "rare": 0.0052,
535	          "rank_corr": -0.138,
536	          "rankme": 353.5,
537	          "knn": 0.989
538	        }
539	      },
540	      "uncurated": {
541	        "gen0": {
542	          "ppl": 30.8,
543	          "rare": 0.0293,
544	          "rank_corr": -0.019,
545	          "rankme": 340.5,
546	          "knn": 0.989
547	        },
548	        "gen1": {
549	          "ppl": 37.2,
550	          "rare": 0.0198,
551	          "rank_corr": -0.047,
552	          "rankme": 355.8,
553	          "knn": 0.989
554	        },
555	        "gen2": {
556	          "ppl": 42.8,
557	          "rare": 0.0147,
558	          "rank_corr": -0.043,
559	          "rankme": 360.4,
560	          "knn": 0.989
561	        },
562	        "gen3": {
563	          "ppl": 47.5,
564	          "rare": 0.0123,
565	          "rank_corr": -0.039,
566	          "rankme": 362.1,
567	          "knn": 0.989
568	        },
569	        "gen4": {
570	          "ppl": 46.8,
571	          "rare": 0.0108,
572	          "rank_corr": -0.037,
573	          "rankme": 359.8,
574	          "knn": 0.989
575	        },
576	        "gen5": {
577	          "ppl": 44.2,
578	          "rare": 0.0102,
579	          "rank_corr": -0.042,
580	          "rankme": 355.2,
581	          "knn": 0.989
582	        },
583	        "gen6": {
584	          "ppl": 42.5,
585	          "rare": 0.0096,
586	          "rank_corr": -0.058,
587	          "rankme": 351.0,
588	          "knn": 0.989
589	        },
590	        "gen7": {
591	          "ppl": 41.8,
592	          "rare": 0.0092,
593	          "rank_corr": -0.075,
594	          "rankme": 347.5,
595	          "knn": 0.989
596	        }
597	      },
598	      "external_only": {
599	        "gen0": {
600	          "ppl": 30.5,
601	          "sel_ratio": 1.1,
602	          "rare": 0.0294,
603	          "rank_corr": -0.02,
604	          "rankme": 341.2,
605	          "knn": 0.989
606	        },
607	        "gen1": {
608	          "ppl": 34.9,
609	          "sel_ratio": 1.14,
610	          "rare": 0.0199,
611	          "rank_corr": -0.028,
612	          "rankme": 354.5,
613	          "knn": 0.989
614	        },
615	        "gen2": {
616	          "ppl": 39.8,
617	          "sel_ratio": 1.17,
618	          "rare": 0.0148,
619	          "rank_corr": -0.032,
620	          "rankme": 359.8,
621	          "knn": 0.989
622	        },
623	        "gen3": {
624	          "ppl": 43.1,
625	          "sel_ratio": 1.2,
626	          "rare": 0.0124,
627	          "rank_corr": -0.035,
628	          "rankme": 361.5,
629	          "knn": 0.989
630	        },
631	        "gen4": {
632	          "ppl": 42.8,
633	          "sel_ratio": 1.23,
634	          "rare": 0.0109,
635	          "rank_corr": -0.037,
636	          "rankme": 358.8,
637	          "knn": 0.989
638	        },
639	        "gen5": {
640	          "ppl": 41.0,
641	          "sel_ratio": 1.26,
642	          "rare": 0.0103,
643	          "rank_corr": -0.036,
644	          "rankme": 354.5,
645	          "knn": 0.989
646	        },
647	        "gen6": {
648	          "ppl": 39.5,
649	          "sel_ratio": 1.28,
650	          "rare": 0.0097,
651	          "rank_corr": -0.035,
652	          "rankme": 350.2,
653	          "knn": 0.989
654	        },
655	        "gen7": {
656	          "ppl": 38.8,
657	          "sel_ratio": 1.3,
658	          "rare": 0.0093,
659	          "rank_corr": -0.033,
660	          "rankme": 346.8,
661	          "knn": 0.989
662	        }
663	      },
664	      "derived": {
665	        "rgds_ppl_excess_vs_uncurated_pct": 51.9,
666	        "rgds_rare_deficit_vs_uncurated_pct": 43.5,
667	        "external_ppl_improvement_vs_uncurated_pct": -7.2
668	      }
669	    },
670	    "tables": [
671	      "Table 5: GPT2-125M vs GPT2-medium gen7 对比（绝对值 + 相对差异百分比）"
672	    ],
673	    "figures": [],
674	    "analysis": "C1/C2-weak/C3 在 GPT2-medium 上全部复现，相对幅度 ±5% 内一致。\n确认 alignment gap 机制的规模不变性。\n审稿人 R1 被有效回应：gap 在 2.8× 模型上同样清晰。\n相对幅度的稳定性为\"更大模型上也可能存在\"提供了间接论据。\n\n\nGPT2-medium 基线 PPL 更低（31 vs 37），因 355M 参数提供更强的语言建模能力。\nalignment gap 相对幅度与 125M 高度一致：RGDS PPL excess 51.9%（125M: 51.4%），\nsel_ratio 终点 0.56（125M: 0.52），rare deficit 43.5%（125M: 47.1%）。\n\n机制不变性解释：alignment gap 源于嵌入空间在 self-iterate 下的几何收缩，\n这是训练动力学的内禀性质，与模型容量正交。更大模型嵌入维度更高（1024 vs 768），\n但 self-iterate 的收缩力度也相应更强（更多参数 → 更强的模式记忆 → 收缩更彻底）。\n两效应大致抵消，使相对幅度在两个规模上相似。\n\nRankMe 绝对值更高（340-363 vs 280-303）因嵌入维度更大，\n但同样在崩塌过程中上升，未检出多样性衰退——S2 在更大规模上仍然成立。\n"
675	  },
676	  {
677	    "name": "GPT2-medium 355M seed=123 复现",
678	    "description": "GPT2-medium 第二种子，确认更大模型上的趋势可复现性。",
679	    "results": {
680	      "rgds": {
681	        "gen0": {
682	          "ppl": 31.5,
683	          "sel_ratio": 1.04,
684	          "rare": 0.0292,
685	          "rank_corr": -0.054
686	        },
687	        "gen7": {
688	          "ppl": 65.1,
689	          "sel_ratio": 0.53,
690	          "rare": 0.0049,
691	          "rank_corr": -0.142
692	        }
693	      },
694	      "uncurated": {
695	        "gen0": {
696	          "ppl": 31.1,
697	          "rare": 0.029
698	        },
699	        "gen7": {
700	          "ppl": 42.5,
701	          "rare": 0.0089
702	        }
703	      },
704	      "external_only": {
705	        "gen0": {
706	          "ppl": 30.8,
707	          "sel_ratio": 1.09,
708	          "rare": 0.0293
709	        },
710	        "gen7": {
711	          "ppl": 39.5,
712	          "sel_ratio": 1.27,
713	          "rare": 0.0091
714	        }
715	      },
716	      "derived": {
717	        "rgds_ppl_excess_vs_uncurated_pct": 53.2,
718	        "two_seed_aggregation": {
719	          "rgds_gen7_ppl": {
720	            "mean": 64.3,
721	            "range": [
722	              63.5,
723	              65.1
724	            ]
725	          },
726	          "rgds_gen7_sel_ratio": {
727	            "mean": 0.545,
728	            "range": [
729	              0.53,
730	              0.56
731	            ]
732	          }
733	        }
734	      }
735	    },
736	    "tables": [
737	      "Table 5 扩展为 2-seed mean ± range"
738	    ],
739	    "figures": [],
740	    "analysis": "combined 证据：125M × 3 seeds + 355M × 2 seeds = 5 个独立验证，全部方向一致。\n这是极强的鲁棒性证据。\n\n\nseed=123 在 GPT2-medium 上复现相同趋势，点估计 ±3% 波动。\nRGDS gen7 PPL 65.1 vs seed=42 的 63.5，sel_ratio 0.53 vs 0.56——方向完全一致。\nGPT2-medium 两种子足以证明趋势可复现性（配合 125M 三种子提供交叉验证）。\n"
741	  },
742	  {
743	    "name": "Embedding re-anchoring 缓解实验 (GPT2-125M, seed=42)",
744	    "description": "每一代用预训练模型嵌入替代当前模型嵌入做多样性选择（不改训练过程，只改 selection 用的嵌入）。\n验证 alignment gap 可修复性。成功→\"found + partial fix\"。\n",
745	    "results": {
746	      "reanchored_rgds": {
747	        "gen0": {
748	          "ppl": 37.2,
749	          "sel_ratio": 1.04,
750	          "rare": 0.0288,
751	          "rank_corr": -0.058
752	        },
753	        "gen1": {
754	          "ppl": 42.0,
755	          "sel_ratio": 1.02,
756	          "rare": 0.021,
757	          "rank_corr": -0.061
758	        },
759	        "gen2": {
760	          "ppl": 48.2,
761	          "sel_ratio": 1.01,
762	          "rare": 0.0156,
763	          "rank_corr": -0.064
764	        },
765	        "gen3": {
766	          "ppl": 53.5,
767	          "sel_ratio": 0.99,
768	          "rare": 0.0124,
769	          "rank_corr": -0.067
770	        },
771	        "gen4": {
772	          "ppl": 54.1,
773	          "sel_ratio": 0.98,
774	          "rare": 0.0103,
775	          "rank_corr": -0.069
776	        },
777	        "gen5": {
778	          "ppl": 52.8,
779	          "sel_ratio": 0.97,
780	          "rare": 0.0089,
781	          "rank_corr": -0.071
782	        },
783	        "gen6": {
784	          "ppl": 51.5,
785	          "sel_ratio": 0.96,
786	          "rare": 0.0077,
787	          "rank_corr": -0.073
788	        },
789	        "gen7": {
790	          "ppl": 51.2,
791	          "sel_ratio": 0.95,
792	          "rare": 0.0061,
793	          "rank_corr": -0.075
794	        }
795	      },
796	      "comparison_at_gen7": {
797	        "vs_rgds": {
798	          "ppl_reduction_pct": 29.7,
799	          "rare_improvement_pct": 32.6,
800	          "sel_ratio_change": "0.52 → 0.95（从严重失调恢复到接近 1.0）"
801	        },
802	        "vs_uncurated": {
803	          "ppl_excess_pct": 6.4,
804	          "rare_deficit_pct": 29.9
805	        },
806	        "vs_external": {
807	          "ppl_excess_pct": 11.8,
808	          "rare_deficit_pct": 30.7
809	        }
810	      }
811	    },
812	    "tables": [
813	      "Table 6: RGDS vs Re-anchored RGDS vs Uncurated vs External gen7 四方对比"
814	    ],
815	    "figures": [],
816	    "analysis": "re-anchoring 验证了 alignment gap 的因果性：消除嵌入退化 → 选择恢复 → PPL 近乎完全恢复。\nrare n-gram +32.6% 满足 best 档 [10, 40%] 要求。\n论文从\"发现问题\"升级为\"发现问题 + 简单修复部分有效 + 定位残余问题在生成端\"。\n为 §7 future work 自然引出\"生成端干预\"方向。\n\n\nre-anchoring 用预训练嵌入做选择，切断\"模型退化→嵌入退化→选择退化→模型更退化\"的反馈环。\n\nselection ratio 稳定在 ~1.0（1.04→0.95 轻微下降），而非 RGDS 的 1.04→0.52 断崖式下降。\n轻微下降原因：即使嵌入质量好，生成数据本身在退化，候选池绝对多样性下降，\n使得预训练嵌入虽能正确排序但最优子集的 ratio 也略有缩水。\n\nPPL 大幅恢复：72.8 → 51.2（-29.7%），接近 uncurated 的 48.1（仅高 6.4%）。\n说明 RGDS 的 PPL 灾难主要来自选择偏差，而非生成退化本身。\nRe-anchoring 消除了选择偏差 → PPL 近乎完全恢复。\n\nrare n-gram 部分恢复：0.0046 → 0.0061（+32.6%），但仍低于 uncurated 0.0087（-29.9%）。\nrare n-gram 损失有两个来源：\n(1) 选择偏差——词汇贫乏样本被优先选中→被 re-anchoring 修复，贡献 ~1/3 恢复\n(2) 生成端词汇萎缩——模型逐渐丢失低频词能力→re-anchoring 无法修复\n这个解耦本身就是一个有价值的发现。\n"
817	  },
818	  {
819	    "name": "OpenWebText 子集 三方法对比 (GPT2-125M, seed=42)",
820	    "description": "在 OpenWebText 上验证 alignment gap 跨数据集泛化性。回应审稿人 R2。",
821	    "results": {
822	      "rgds": {
823	        "gen0": {
824	          "ppl": 27.5,
825	          "sel_ratio": 1.05,
826	          "rare": 0.0312,
827	          "rank_corr": -0.053
828	        },
829	        "gen1": {
830	          "ppl": 31.8,
831	          "sel_ratio": 0.97,
832	          "rare": 0.023,
833	          "rank_corr": -0.068
834	        },
835	        "gen2": {
836	          "ppl": 37.4,
837	          "sel_ratio": 0.89,
838	          "rare": 0.0172,
839	          "rank_corr": -0.082
840	        },
841	        "gen3": {
842	          "ppl": 42.8,
843	          "sel_ratio": 0.81,
844	          "rare": 0.0129,
845	          "rank_corr": -0.096
846	        },
847	        "gen4": {
848	          "ppl": 48.1,
849	          "sel_ratio": 0.73,
850	          "rare": 0.0098,
851	          "rank_corr": -0.11
852	        },
853	        "gen5": {
854	          "ppl": 52.5,
855	          "sel_ratio": 0.66,
856	          "rare": 0.0079,
857	          "rank_corr": -0.122
858	        },
859	        "gen6": {
860	          "ppl": 56.2,
861	          "sel_ratio": 0.59,
862	          "rare": 0.0065,
863	          "rank_corr": -0.133
864	        },
865	        "gen7": {
866	          "ppl": 59.1,
867	          "sel_ratio": 0.53,
868	          "rare": 0.0054,
869	          "rank_corr": -0.144
870	        }
871	      },
872	      "uncurated": {
873	        "gen0": {
874	          "ppl": 27.2,
875	          "rare": 0.031,
876	          "rank_corr": -0.02
877	        },
878	        "gen1": {
879	          "ppl": 33.5,
880	          "rare": 0.0212,
881	          "rank_corr": -0.048
882	        },
883	        "gen2": {
884	          "ppl": 39.2,
885	          "rare": 0.0158,
886	          "rank_corr": -0.044
887	        },
888	        "gen3": {
889	          "ppl": 43.8,
890	          "rare": 0.0131,
891	          "rank_corr": -0.04
892	        },
893	        "gen4": {
894	          "ppl": 43.2,
895	          "rare": 0.0115,
896	          "rank_corr": -0.038
897	        },
898	        "gen5": {
899	          "ppl": 40.8,
900	          "rare": 0.0108,
901	          "rank_corr": -0.044
902	        },
903	        "gen6": {
904	          "ppl": 39.1,
905	          "rare": 0.01,
906	          "rank_corr": -0.06
907	        },
908	        "gen7": {
909	          "ppl": 38.5,
910	          "rare": 0.0095,
911	          "rank_corr": -0.08
912	        }
913	      },
914	      "external_only": {
915	        "gen0": {
916	          "ppl": 27.0,
917	          "sel_ratio": 1.09,
918	          "rare": 0.0311,
919	          "rank_corr": -0.021
920	        },
921	        "gen1": {
922	          "ppl": 31.2,
923	          "sel_ratio": 1.13,
924	          "rare": 0.0215,
925	          "rank_corr": -0.03
926	        },
927	        "gen2": {
928	          "ppl": 36.5,
929	          "sel_ratio": 1.16,
930	          "rare": 0.016,
931	          "rank_corr": -0.034
932	        },
933	        "gen3": {
934	          "ppl": 40.2,
935	          "sel_ratio": 1.19,
936	          "rare": 0.0132,
937	          "rank_corr": -0.037
938	        },
939	        "gen4": {
940	          "ppl": 40.0,
941	          "sel_ratio": 1.22,
942	          "rare": 0.0116,
943	          "rank_corr": -0.039
944	        },
945	        "gen5": {
946	          "ppl": 38.2,
947	          "sel_ratio": 1.25,
948	          "rare": 0.0109,
949	          "rank_corr": -0.038
950	        },
951	        "gen6": {
952	          "ppl": 36.8,
953	          "sel_ratio": 1.27,
954	          "rare": 0.0101,
955	          "rank_corr": -0.036
956	        },
957	        "gen7": {
958	          "ppl": 36.1,
959	          "sel_ratio": 1.29,
960	          "rare": 0.0096,
961	          "rank_corr": -0.035
962	        }
963	      },
964	      "derived": {
965	        "rgds_ppl_excess_vs_uncurated_pct": 53.5,
966	        "rgds_rare_deficit_vs_uncurated_pct": 43.2,
967	        "external_ppl_improvement_vs_uncurated_pct": -6.2
968	      }
969	    },
970	    "tables": [
971	      "Table 7: WikiText-103 vs OpenWebText gen7 指标对比（绝对值 + 相对差异）"
972	    ],
973	    "figures": [],
974	    "analysis": "alignment gap 跨数据集完全泛化。相对幅度在 WikiText 和 OWT 上一致（±3%），\n强化\"机制是通用的\"论点。审稿人 R2 被有效回应。\ncombined 全部证据：2 datasets × 2 model sizes × 3 seeds + 1 mitigation = \n极强的现象鲁棒性 + 因果验证。投 8 页 Findings 绰绰有余。\n\nOWT 基线 PPL 更低（27 vs 37），因为 GPT2 预训练语料 WebText 与 OWT 同分布。\nOWT 基线 rare n-gram 略高（0.031 vs 0.029），因 web 文本词汇更多样化。\n\nalignment gap 相对幅度与 WikiText 高度一致：\n- sel_ratio: 1.05→0.53（WikiText: 1.04→0.52）\n- PPL excess: +53.5%（WikiText: +51.4%）\n- rare deficit: -43.2%（WikiText: -47.1%）\n- external ratio: 1.09→1.29（WikiText: 1.08→1.28）\n\n一致性的机制解释：alignment gap 是模型内部嵌入空间收缩的产物，\n与训练数据领域无关。self-iterate 反馈环的收缩动力学是训练过程的内禀性质，\n不依赖数据分布的具体形态。数据集只影响绝对 PPL 水平（通过基线语言建模难度），\n不影响 gap 的相对大小。\n"
975	  }
976	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4cf3d0dc-8505-4f4c-804e-41389f4174d6",
  "isSidechain": false,
  "promptId": "ad861b3f-869b-46c3-a458-a9928fad5b05",
  "type": "user",
  "uuid": "180e509e-675b-47c9-9b8c-b855e37547ad",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Phase 2 三方法对比 (GPT2-125M, WikiText-103, seed=42)\",\n    \"description\": \"Self-iterate GPT2-125M × 8 gens × 3 methods (uncurated/RGDS/external_only)。锚定全部 claims 的主实验。\",\n    \"results\": {\n      \"rgds\": {\n        \"gen0\": {\n          \"ppl\": 37.2,\n          \"sel_ratio\": 1.04,\n          \"rare\": 0.0288,\n          \"rank_corr\": -0.058,\n          \"rankme\": 281.5,\n          \"knn\": 0.988\n        },\n        \"gen1\": {\n          \"ppl\": 42.5,\n          \"sel_ratio\": 0.96,\n          \"rare\": 0.0208,\n          \"rank_corr\": -0.074,\n          \"rankme\": 290.2,\n          \"knn\": 0.988\n        },\n        \"gen2\": {\n          \"ppl\": 49.8,\n          \"sel_ratio\": 0.87,\n          \"rare\": 0.0152,\n          \"rank_corr\": -0.089,\n          \"rankme\": 296.4,\n          \"knn\": 0.987\n        },\n        \"gen3\": {\n          \"ppl\": 56.3,\n          \"sel_ratio\": 0.79,\n          \"rare\": 0.0113,\n          \"rank_corr\": -0.103,\n          \"rankme\": 300.1,\n          \"knn\": 0.988\n        },\n        \"gen4\": {\n          \"ppl\": 61.7,\n          \"sel_ratio\": 0.71,\n          \"rare\": 0.0086,\n          \"rank_corr\": -0.118,\n          \"rankme\": 303.2,\n          \"knn\": 0.988\n        },\n        \"gen5\": {\n          \"ppl\": 66.4,\n          \"sel_ratio\": 0.64,\n          \"rare\": 0.0068,\n          \"rank_corr\": -0.131,\n          \"rankme\": 301.8,\n          \"knn\": 0.988\n        },\n        \"gen6\": {\n          \"ppl\": 70.1,\n          \"sel_ratio\": 0.57,\n          \"rare\": 0.0055,\n          \"rank_corr\": -0.143,\n          \"rankme\": 298.5,\n          \"knn\": 0.988\n        },\n        \"gen7\": {\n          \"ppl\": 72.8,\n          \"sel_ratio\": 0.52,\n          \"rare\": 0.0046,\n          \"rank_corr\": -0.155,\n          \"rankme\": 294.3,\n          \"knn\": 0.988\n        }\n      },\n      \"uncurated\": {\n        \"gen0\": {\n          \"ppl\": 37.1,\n          \"rare\": 0.029,\n          \"rank_corr\": -0.023,\n          \"rankme\": 280.3,\n          \"knn\": 0.988\n        },\n        \"gen1\": {\n          \"ppl\": 44.9,\n          \"rare\": 0.0192,\n          \"rank_corr\": -0.055,\n          \"rankme\": 297.8,\n          \"knn\": 0.988\n        },\n        \"gen2\": {\n          \"ppl\": 51.6,\n          \"rare\": 0.0139,\n          \"rank_corr\": -0.049,\n          \"rankme\": 302.6,\n          \"knn\": 0.987\n        },\n        \"gen3\": {\n          \"ppl\": 57.0,\n          \"rare\": 0.0116,\n          \"rank_corr\": -0.044,\n          \"rankme\": 303.3,\n          \"knn\": 0.988\n        },\n        \"gen4\": {\n          \"ppl\": 55.7,\n          \"rare\": 0.0101,\n          \"rank_corr\": -0.042,\n          \"rankme\": 301.3,\n          \"knn\": 0.988\n        },\n        \"gen5\": {\n          \"ppl\": 51.7,\n          \"rare\": 0.0098,\n          \"rank_corr\": -0.048,\n          \"rankme\": 297.4,\n          \"knn\": 0.988\n        },\n        \"gen6\": {\n          \"ppl\": 48.7,\n          \"rare\": 0.0089,\n          \"rank_corr\": -0.065,\n          \"rankme\": 293.0,\n          \"knn\": 0.988\n        },\n        \"gen7\": {\n          \"ppl\": 48.1,\n          \"rare\": 0.0087,\n          \"rank_corr\": -0.087,\n          \"rankme\": 289.8,\n          \"knn\": 0.988\n        }\n      },\n      \"external_only\": {\n        \"gen0\": {\n          \"ppl\": 36.8,\n          \"sel_ratio\": 1.08,\n          \"rare\": 0.0289,\n          \"rank_corr\": -0.024,\n          \"rankme\": 280.8,\n          \"knn\": 0.988\n        },\n        \"gen1\": {\n          \"ppl\": 42.2,\n          \"sel_ratio\": 1.12,\n          \"rare\": 0.0194,\n          \"rank_corr\": -0.032,\n          \"rankme\": 296.5,\n          \"knn\": 0.988\n        },\n        \"gen2\": {\n          \"ppl\": 47.5,\n          \"sel_ratio\": 1.15,\n          \"rare\": 0.0141,\n          \"rank_corr\": -0.036,\n          \"rankme\": 302.0,\n          \"knn\": 0.987\n        },\n        \"gen3\": {\n          \"ppl\": 50.8,\n          \"sel_ratio\": 1.18,\n          \"rare\": 0.0118,\n          \"rank_corr\": -0.039,\n          \"rankme\": 303.0,\n          \"knn\": 0.988\n        },\n        \"gen4\": {\n          \"ppl\": 50.3,\n          \"sel_ratio\": 1.21,\n          \"rare\": 0.0103,\n          \"rank_corr\": -0.041,\n          \"rankme\": 300.5,\n          \"knn\": 0.988\n        },\n        \"gen5\": {\n          \"ppl\": 48.2,\n          \"sel_ratio\": 1.24,\n          \"rare\": 0.0097,\n          \"rank_corr\": -0.04,\n          \"rankme\": 296.8,\n          \"knn\": 0.988\n        },\n        \"gen6\": {\n          \"ppl\": 46.5,\n          \"sel_ratio\": 1.26,\n          \"rare\": 0.0091,\n          \"rank_corr\": -0.038,\n          \"rankme\": 292.5,\n          \"knn\": 0.988\n        },\n        \"gen7\": {\n          \"ppl\": 45.8,\n          \"sel_ratio\": 1.28,\n          \"rare\": 0.0088,\n          \"rank_corr\": -0.037,\n          \"rankme\": 289.4,\n          \"knn\": 0.988\n        }\n      },\n      \"derived\": {\n        \"rgds_ppl_excess_vs_uncurated_pct\": 51.4,\n        \"rgds_rare_deficit_vs_uncurated_pct\": 47.1,\n        \"external_ppl_improvement_vs_uncurated_pct\": -4.8,\n        \"external_rare_vs_uncurated_pct\": 1.1\n      }\n    },\n    \"tables\": [\n      \"Table 1: Gen 0-7 三方法全指标（PPL, rare, sel_ratio, rank_corr, RankMe, k-NN）\",\n      \"Table 2: Gen 7 汇总 + 方法间相对差异百分比\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"C1 成立：selection ratio 单调下降 8 代，效应量大（1.04→0.52），不可归因于噪声。\\nC2-weak 成立：external ratio 始终 >1.0 且上升，与 internal 形成鲜明对照。\\nC3 成立：RGDS PPL +51%、rare -47% vs uncurated，完整因果链闭合。\\nS1 成立：external PPL -4.8% 但 rare +1.1%，PPL 与 rare 解耦。\\nS2 成立：RankMe 在崩塌过程中反而上升（280→303），k-NN 稳定，无法检测多样性衰退。\\n\\n\\nRGDS: self-iterate 导致内部嵌入空间收缩（neural collapse 类机制）。\\n随代际推进，模型嵌入的\\\"几何多样性\\\"方向逐渐对齐到高频词汇模式上，\\n贪心子模选择在低维空间中选中的\\\"远点\\\"恰好是词汇贫乏的样本。\\nselection ratio 从 1.04 单调降至 0.52 反映了这种对齐错位的加剧。\\n训练在词汇贫乏子集上 → PPL 从 37.2 飙升到 72.8（+51%），\\nrare n-gram 从 0.029 降至 0.0046（-84%），远超 uncurated 的自然崩塌幅度。\\n\\nuncurated: 无选择偏差，PPL 先升后降（gen3 峰值 57.0 → gen7 回落 48.1），\\nrare n-gram 持续下降到 0.0087（-70%）。\\nPPL 回落是因为模型逐渐\\\"记住\\\"自身分布，但词汇多样性不可逆损失。\\n\\nexternal_only: Contriever 冻结不受训练反馈影响，diversity 信号始终校准到原始分布。\\nselection ratio 稳定上升（1.08→1.28），说明它确实在挑\\\"更不像已有训练集\\\"的样本。\\nPPL 略优于 uncurated（45.8 vs 48.1，-4.8%）因为语义多样性选择提供了更有信息量的训练数据。\\n但 rare n-gram（0.0088）≈ uncurated（0.0087），说明语义多样性 ≠ 词汇多样性——\\nContriever 捕捉的是主题/语义距离而非低频词分布。\\n\"\n  },\n  {\n    \"name\": \"External_only seed=123 复现\",\n    \"description\": \"验证 external_only selection ratio >1.0 在不同种子下的可复现性。plan_004 的子集先行实验。\",\n    \"results\": {\n      \"external_only\": {\n        \"gen0\": {\n          \"ppl\": 37.0,\n          \"sel_ratio\": 1.07,\n          \"rare\": 0.0291\n        },\n        \"gen4\": {\n          \"ppl\": 50.8,\n          \"sel_ratio\": 1.19,\n          \"rare\": 0.0105\n        },\n        \"gen7\": {\n          \"ppl\": 46.5,\n          \"sel_ratio\": 1.25,\n          \"rare\": 0.009\n        }\n      }\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"结果合并入 plan_004 的 3-seed 统计。单独作用是在 plan_001 完成前快速确认 C2-weak 方向。\\n\\nContriever 冻结模型的选择函数不受训练种子影响，\\n但下游训练轨迹因初始化/采样随种子变化导致 ±5% 波动。\\nsel_ratio 仍 >1.0 全程，确认 C2-weak 非种子偶然。\\n\"\n  },\n  {\n    \"name\": \"三方法 seed=123 完整复现 (GPT2-125M, WikiText-103)\",\n    \"description\": \"3 methods × 8 gens, seed=123。第二个种子，与 plan_001 对比验证趋势可复现。\",\n    \"results\": {\n      \"rgds\": {\n        \"gen0\": {\n          \"ppl\": 37.5,\n          \"sel_ratio\": 1.03,\n          \"rare\": 0.0285,\n          \"rank_corr\": -0.062\n        },\n        \"gen3\": {\n          \"ppl\": 57.8,\n          \"sel_ratio\": 0.77,\n          \"rare\": 0.0108,\n          \"rank_corr\": -0.108\n        },\n        \"gen7\": {\n          \"ppl\": 70.5,\n          \"sel_ratio\": 0.54,\n          \"rare\": 0.005,\n          \"rank_corr\": -0.148\n        }\n      },\n      \"uncurated\": {\n        \"gen0\": {\n          \"ppl\": 37.3,\n          \"rare\": 0.0287,\n          \"rank_corr\": -0.025\n        },\n        \"gen3\": {\n          \"ppl\": 58.2,\n          \"rare\": 0.0119,\n          \"rank_corr\": -0.046\n        },\n        \"gen7\": {\n          \"ppl\": 49.3,\n          \"rare\": 0.0091,\n          \"rank_corr\": -0.082\n        }\n      },\n      \"external_only\": {\n        \"gen0\": {\n          \"ppl\": 37.0,\n          \"sel_ratio\": 1.07,\n          \"rare\": 0.0291,\n          \"rank_corr\": -0.026\n        },\n        \"gen3\": {\n          \"ppl\": 51.5,\n          \"sel_ratio\": 1.17,\n          \"rare\": 0.0121,\n          \"rank_corr\": -0.041\n        },\n        \"gen7\": {\n          \"ppl\": 46.5,\n          \"sel_ratio\": 1.25,\n          \"rare\": 0.009,\n          \"rank_corr\": -0.04\n        }\n      },\n      \"derived\": {\n        \"rgds_ppl_excess_vs_uncurated_pct\": 43.0,\n        \"rgds_rare_deficit_vs_uncurated_pct\": 45.1\n      }\n    },\n    \"tables\": [\n      \"Table 3: seed=42 vs seed=123 gen7 核心指标对比\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"趋势方向完全复现。RGDS ratio <1.0 by gen2, external ratio >1.0 全程,\\nRGDS PPL >> uncurated。种子间差异远小于方法间差异。\\n\\n\\n所有方向性趋势与 seed=42 一致：RGDS ratio 单调下降、PPL 持续上升、external ratio 稳定 >1.0。\\n点估计波动 ±5-8%——seed=123 的 RGDS gen7 PPL (70.5) 略低于 seed=42 (72.8)，\\nsel_ratio (0.54) 略高于 seed=42 (0.52)。这是正常的种子间方差，来源于\\nmini-batch 采样和初始化差异导致的训练轨迹分散。\\n关键判据：方法间差异 (RGDS 70.5 vs uncurated 49.3 = Δ21.2) 远大于种子间差异 (70.5 vs 72.8 = Δ2.3)。\\n\"\n  },\n  {\n    \"name\": \"三方法 seed=456 完整复现 (GPT2-125M, WikiText-103)\",\n    \"description\": \"第三个种子。与 seed=42/123 构成 N=3 统计检验基础，计算 95% CI。\",\n    \"results\": {\n      \"rgds\": {\n        \"gen0\": {\n          \"ppl\": 36.9,\n          \"sel_ratio\": 1.05,\n          \"rare\": 0.0292,\n          \"rank_corr\": -0.055\n        },\n        \"gen3\": {\n          \"ppl\": 55.1,\n          \"sel_ratio\": 0.81,\n          \"rare\": 0.0117,\n          \"rank_corr\": -0.099\n        },\n        \"gen7\": {\n          \"ppl\": 74.2,\n          \"sel_ratio\": 0.49,\n          \"rare\": 0.0043,\n          \"rank_corr\": -0.161\n        }\n      },\n      \"uncurated\": {\n        \"gen0\": {\n          \"ppl\": 36.8,\n          \"rare\": 0.0291,\n          \"rank_corr\": -0.021\n        },\n        \"gen3\": {\n          \"ppl\": 55.8,\n          \"rare\": 0.0113,\n          \"rank_corr\": -0.041\n        },\n        \"gen7\": {\n          \"ppl\": 47.5,\n          \"rare\": 0.0085,\n          \"rank_corr\": -0.091\n        }\n      },\n      \"external_only\": {\n        \"gen0\": {\n          \"ppl\": 36.5,\n          \"sel_ratio\": 1.09,\n          \"rare\": 0.0293,\n          \"rank_corr\": -0.022\n        },\n        \"gen3\": {\n          \"ppl\": 50.2,\n          \"sel_ratio\": 1.2,\n          \"rare\": 0.0122,\n          \"rank_corr\": -0.037\n        },\n        \"gen7\": {\n          \"ppl\": 44.9,\n          \"sel_ratio\": 1.31,\n          \"rare\": 0.0086,\n          \"rank_corr\": -0.034\n        }\n      },\n      \"derived\": {\n        \"rgds_ppl_excess_vs_uncurated_pct\": 56.2,\n        \"rgds_rare_deficit_vs_uncurated_pct\": 49.4\n      },\n      \"three_seed_aggregation\": {\n        \"note\": \"聚合 seed=42 (plan_001) + seed=123 (plan_004) + seed=456 (plan_005)\",\n        \"rgds_gen7_ppl\": {\n          \"mean\": 72.5,\n          \"std\": 1.85,\n          \"ci95\": [\n            67.9,\n            77.1\n          ]\n        },\n        \"rgds_gen7_sel_ratio\": {\n          \"mean\": 0.517,\n          \"std\": 0.025,\n          \"ci95\": [\n            0.455,\n            0.579\n          ]\n        },\n        \"rgds_gen7_rare\": {\n          \"mean\": 0.00463,\n          \"std\": 0.00035,\n          \"ci95\": [\n            0.00376,\n            0.0055\n          ]\n        },\n        \"rgds_gen7_rank_corr\": {\n          \"mean\": -0.155,\n          \"std\": 0.007,\n          \"ci95\": [\n            -0.171,\n            -0.139\n          ]\n        },\n        \"uncurated_gen7_ppl\": {\n          \"mean\": 48.3,\n          \"std\": 0.91,\n          \"ci95\": [\n            46.0,\n            50.6\n          ]\n        },\n        \"uncurated_gen7_rare\": {\n          \"mean\": 0.00877,\n          \"std\": 0.0003,\n          \"ci95\": [\n            0.00802,\n            0.00952\n          ]\n        },\n        \"external_gen7_ppl\": {\n          \"mean\": 45.7,\n          \"std\": 0.8,\n          \"ci95\": [\n            43.7,\n            47.7\n          ]\n        },\n        \"external_gen7_sel_ratio\": {\n          \"mean\": 1.28,\n          \"std\": 0.03,\n          \"ci95\": [\n            1.21,\n            1.35\n          ]\n        },\n        \"external_gen7_rare\": {\n          \"mean\": 0.0088,\n          \"std\": 0.0002,\n          \"ci95\": [\n            0.0083,\n            0.0093\n          ]\n        },\n        \"external_gen7_rank_corr\": {\n          \"mean\": -0.037,\n          \"std\": 0.003,\n          \"ci95\": [\n            -0.044,\n            -0.03\n          ]\n        },\n        \"key_tests\": {\n          \"rgds_sel_ratio_below_1\": \"CI [0.455, 0.579] 不跨 1.0 ✓\",\n          \"external_sel_ratio_above_1\": \"CI [1.21, 1.35] 不跨 1.0 ✓\",\n          \"rgds_ppl_above_uncurated\": \"CI 无重叠 (67.9-77.1 vs 46.0-50.6) ✓\",\n          \"external_rare_eq_uncurated\": \"CI 重叠 (0.00830-0.00930 vs 0.00802-0.00952) → 差异不显著 ✓\",\n          \"cohen_d_ppl\": \">3 (极大效应量)\"\n        }\n      }\n    },\n    \"tables\": [\n      \"Table 4: 3-seed 聚合统计（mean ± std, 95% CI）全指标\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"三种子全部复现主趋势方向。CI 不跨零/不跨 1.0，满足 best 档复现要求。\\n方法间差异 (Δ=24.2 PPL) 远大于种子间差异 (std=1.9)，Cohen's d >3。\\n审稿人 R3 (\\\"N=1 seed\\\") 完全被挡住。\\n\\n\\nseed=456 的 RGDS gen7 PPL 最高 (74.2)、sel_ratio 最低 (0.49)——\\n代表种子间方差的上界。三种子聚合后所有 CI 不跨关键阈值：\\n- sel_ratio CI [0.455, 0.579] 远低于 1.0，C1 在统计上稳固\\n- RGDS PPL CI [67.9, 77.1] 与 uncurated CI [46.0, 50.6] 无重叠，C3 稳固\\n- external sel_ratio CI [1.21, 1.35] 远高于 1.0，C2-weak 稳固\\n- external rare ≈ uncurated rare（CI 完全重叠），S1 稳固\\n\\nN=3 虽少，但效应量极大（Cohen's d >3），统计功效充足。\\n关键是 8 代的单调趋势不是单点测量——每个种子贡献 8 个相关但独立的观测点，\\n使得趋势的统计可靠性远超点估计。\\n\"\n  },\n  {\n    \"name\": \"GPT2-medium 355M 三方法对比 (WikiText-103, seed=42)\",\n    \"description\": \"在 355M 参数模型上验证 alignment gap 存在。回应审稿人 R1 'GPT2-125M 太小'。\",\n    \"results\": {\n      \"rgds\": {\n        \"gen0\": {\n          \"ppl\": 31.2,\n          \"sel_ratio\": 1.05,\n          \"rare\": 0.0295,\n          \"rank_corr\": -0.051,\n          \"rankme\": 342.1,\n          \"knn\": 0.989\n        },\n        \"gen1\": {\n          \"ppl\": 35.8,\n          \"sel_ratio\": 0.97,\n          \"rare\": 0.0218,\n          \"rank_corr\": -0.064,\n          \"rankme\": 351.4,\n          \"knn\": 0.989\n        },\n        \"gen2\": {\n          \"ppl\": 41.5,\n          \"sel_ratio\": 0.89,\n          \"rare\": 0.0163,\n          \"rank_corr\": -0.078,\n          \"rankme\": 357.2,\n          \"knn\": 0.989\n        },\n        \"gen3\": {\n          \"ppl\": 47.2,\n          \"sel_ratio\": 0.81,\n          \"rare\": 0.0122,\n          \"rank_corr\": -0.091,\n          \"rankme\": 361.8,\n          \"knn\": 0.989\n        },\n        \"gen4\": {\n          \"ppl\": 52.7,\n          \"sel_ratio\": 0.74,\n          \"rare\": 0.0094,\n          \"rank_corr\": -0.104,\n          \"rankme\": 363.5,\n          \"knn\": 0.989\n        },\n        \"gen5\": {\n          \"ppl\": 57.1,\n          \"sel_ratio\": 0.67,\n          \"rare\": 0.0075,\n          \"rank_corr\": -0.116,\n          \"rankme\": 361.2,\n          \"knn\": 0.989\n        },\n        \"gen6\": {\n          \"ppl\": 60.8,\n          \"sel_ratio\": 0.61,\n          \"rare\": 0.0062,\n          \"rank_corr\": -0.127,\n          \"rankme\": 357.8,\n          \"knn\": 0.989\n        },\n        \"gen7\": {\n          \"ppl\": 63.5,\n          \"sel_ratio\": 0.56,\n          \"rare\": 0.0052,\n          \"rank_corr\": -0.138,\n          \"rankme\": 353.5,\n          \"knn\": 0.989\n        }\n      },\n      \"uncurated\": {\n        \"gen0\": {\n          \"ppl\": 30.8,\n          \"rare\": 0.0293,\n          \"rank_corr\": -0.019,\n          \"rankme\": 340.5,\n          \"knn\": 0.989\n        },\n        \"gen1\": {\n          \"ppl\": 37.2,\n          \"rare\": 0.0198,\n          \"rank_corr\": -0.047,\n          \"rankme\": 355.8,\n          \"knn\": 0.989\n        },\n        \"gen2\": {\n          \"ppl\": 42.8,\n          \"rare\": 0.0147,\n          \"rank_corr\": -0.043,\n          \"rankme\": 360.4,\n          \"knn\": 0.989\n        },\n        \"gen3\": {\n          \"ppl\": 47.5,\n          \"rare\": 0.0123,\n          \"rank_corr\": -0.039,\n          \"rankme\": 362.1,\n          \"knn\": 0.989\n        },\n        \"gen4\": {\n          \"ppl\": 46.8,\n          \"rare\": 0.0108,\n          \"rank_corr\": -0.037,\n          \"rankme\": 359.8,\n          \"knn\": 0.989\n        },\n        \"gen5\": {\n          \"ppl\": 44.2,\n          \"rare\": 0.0102,\n          \"rank_corr\": -0.042,\n          \"rankme\": 355.2,\n          \"knn\": 0.989\n        },\n        \"gen6\": {\n          \"ppl\": 42.5,\n          \"rare\": 0.0096,\n          \"rank_corr\": -0.058,\n          \"rankme\": 351.0,\n          \"knn\": 0.989\n        },\n        \"gen7\": {\n          \"ppl\": 41.8,\n          \"rare\": 0.0092,\n          \"rank_corr\": -0.075,\n          \"rankme\": 347.5,\n          \"knn\": 0.989\n        }\n      },\n      \"external_only\": {\n        \"gen0\": {\n          \"ppl\": 30.5,\n          \"sel_ratio\": 1.1,\n          \"rare\": 0.0294,\n          \"rank_corr\": -0.02,\n          \"rankme\": 341.2,\n          \"knn\": 0.989\n        },\n        \"gen1\": {\n          \"ppl\": 34.9,\n          \"sel_ratio\": 1.14,\n          \"rare\": 0.0199,\n          \"rank_corr\": -0.028,\n          \"rankme\": 354.5,\n          \"knn\": 0.989\n        },\n        \"gen2\": {\n          \"ppl\": 39.8,\n          \"sel_ratio\": 1.17,\n          \"rare\": 0.0148,\n          \"rank_corr\": -0.032,\n          \"rankme\": 359.8,\n          \"knn\": 0.989\n        },\n        \"gen3\": {\n          \"ppl\": 43.1,\n          \"sel_ratio\": 1.2,\n          \"rare\": 0.0124,\n          \"rank_corr\": -0.035,\n          \"rankme\": 361.5,\n          \"knn\": 0.989\n        },\n        \"gen4\": {\n          \"ppl\": 42.8,\n          \"sel_ratio\": 1.23,\n          \"rare\": 0.0109,\n          \"rank_corr\": -0.037,\n          \"rankme\": 358.8,\n          \"knn\": 0.989\n        },\n        \"gen5\": {\n          \"ppl\": 41.0,\n          \"sel_ratio\": 1.26,\n          \"rare\": 0.0103,\n          \"rank_corr\": -0.036,\n          \"rankme\": 354.5,\n          \"knn\": 0.989\n        },\n        \"gen6\": {\n          \"ppl\": 39.5,\n          \"sel_ratio\": 1.28,\n          \"rare\": 0.0097,\n          \"rank_corr\": -0.035,\n          \"rankme\": 350.2,\n          \"knn\": 0.989\n        },\n        \"gen7\": {\n          \"ppl\": 38.8,\n          \"sel_ratio\": 1.3,\n          \"rare\": 0.0093,\n          \"rank_corr\": -0.033,\n          \"rankme\": 346.8,\n          \"knn\": 0.989\n        }\n      },\n      \"derived\": {\n        \"rgds_ppl_excess_vs_uncurated_pct\": 51.9,\n        \"rgds_rare_deficit_vs_uncurated_pct\": 43.5,\n        \"external_ppl_improvement_vs_uncurated_pct\": -7.2\n      }\n    },\n    \"tables\": [\n      \"Table 5: GPT2-125M vs GPT2-medium gen7 对比（绝对值 + 相对差异百分比）\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"C1/C2-weak/C3 在 GPT2-medium 上全部复现，相对幅度 ±5% 内一致。\\n确认 alignment gap 机制的规模不变性。\\n审稿人 R1 被有效回应：gap 在 2.8× 模型上同样清晰。\\n相对幅度的稳定性为\\\"更大模型上也可能存在\\\"提供了间接论据。\\n\\n\\nGPT2-medium 基线 PPL 更低（31 vs 37），因 355M 参数提供更强的语言建模能力。\\nalignment gap 相对幅度与 125M 高度一致：RGDS PPL excess 51.9%（125M: 51.4%），\\nsel_ratio 终点 0.56（125M: 0.52），rare deficit 43.5%（125M: 47.1%）。\\n\\n机制不变性解释：alignment gap 源于嵌入空间在 self-iterate 下的几何收缩，\\n这是训练动力学的内禀性质，与模型容量正交。更大模型嵌入维度更高（1024 vs 768），\\n但 self-iterate 的收缩力度也相应更强（更多参数 → 更强的模式记忆 → 收缩更彻底）。\\n两效应大致抵消，使相对幅度在两个规模上相似。\\n\\nRankMe 绝对值更高（340-363 vs 280-303）因嵌入维度更大，\\n但同样在崩塌过程中上升，未检出多样性衰退——S2 在更大规模上仍然成立。\\n\"\n  },\n  {\n    \"name\": \"GPT2-medium 355M seed=123 复现\",\n    \"description\": \"GPT2-medium 第二种子，确认更大模型上的趋势可复现性。\",\n    \"results\": {\n      \"rgds\": {\n        \"gen0\": {\n          \"ppl\": 31.5,\n          \"sel_ratio\": 1.04,\n          \"rare\": 0.0292,\n          \"rank_corr\": -0.054\n        },\n        \"gen7\": {\n          \"ppl\": 65.1,\n          \"sel_ratio\": 0.53,\n          \"rare\": 0.0049,\n          \"rank_corr\": -0.142\n        }\n      },\n      \"uncurated\": {\n        \"gen0\": {\n          \"ppl\": 31.1,\n          \"rare\": 0.029\n        },\n        \"gen7\": {\n          \"ppl\": 42.5,\n          \"rare\": 0.0089\n        }\n      },\n      \"external_only\": {\n        \"gen0\": {\n          \"ppl\": 30.8,\n          \"sel_ratio\": 1.09,\n          \"rare\": 0.0293\n        },\n        \"gen7\": {\n          \"ppl\": 39.5,\n          \"sel_ratio\": 1.27,\n          \"rare\": 0.0091\n        }\n      },\n      \"derived\": {\n        \"rgds_ppl_excess_vs_uncurated_pct\": 53.2,\n        \"two_seed_aggregation\": {\n          \"rgds_gen7_ppl\": {\n            \"mean\": 64.3,\n            \"range\": [\n              63.5,\n              65.1\n            ]\n          },\n          \"rgds_gen7_sel_ratio\": {\n            \"mean\": 0.545,\n            \"range\": [\n              0.53,\n              0.56\n            ]\n          }\n        }\n      }\n    },\n    \"tables\": [\n      \"Table 5 扩展为 2-seed mean ± range\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"combined 证据：125M × 3 seeds + 355M × 2 seeds = 5 个独立验证，全部方向一致。\\n这是极强的鲁棒性证据。\\n\\n\\nseed=123 在 GPT2-medium 上复现相同趋势，点估计 ±3% 波动。\\nRGDS gen7 PPL 65.1 vs seed=42 的 63.5，sel_ratio 0.53 vs 0.56——方向完全一致。\\nGPT2-medium 两种子足以证明趋势可复现性（配合 125M 三种子提供交叉验证）。\\n\"\n  },\n  {\n    \"name\": \"Embedding re-anchoring 缓解实验 (GPT2-125M, seed=42)\",\n    \"description\": \"每一代用预训练模型嵌入替代当前模型嵌入做多样性选择（不改训练过程，只改 selection 用的嵌入）。\\n验证 alignment gap 可修复性。成功→\\\"found + partial fix\\\"。\\n\",\n    \"results\": {\n      \"reanchored_rgds\": {\n        \"gen0\": {\n          \"ppl\": 37.2,\n          \"sel_ratio\": 1.04,\n          \"rare\": 0.0288,\n          \"rank_corr\": -0.058\n        },\n        \"gen1\": {\n          \"ppl\": 42.0,\n          \"sel_ratio\": 1.02,\n          \"rare\": 0.021,\n          \"rank_corr\": -0.061\n        },\n        \"gen2\": {\n          \"ppl\": 48.2,\n          \"sel_ratio\": 1.01,\n          \"rare\": 0.0156,\n          \"rank_corr\": -0.064\n        },\n        \"gen3\": {\n          \"ppl\": 53.5,\n          \"sel_ratio\": 0.99,\n          \"rare\": 0.0124,\n          \"rank_corr\": -0.067\n        },\n        \"gen4\": {\n          \"ppl\": 54.1,\n          \"sel_ratio\": 0.98,\n          \"rare\": 0.0103,\n          \"rank_corr\": -0.069\n        },\n        \"gen5\": {\n          \"ppl\": 52.8,\n          \"sel_ratio\": 0.97,\n          \"rare\": 0.0089,\n          \"rank_corr\": -0.071\n        },\n        \"gen6\": {\n          \"ppl\": 51.5,\n          \"sel_ratio\": 0.96,\n          \"rare\": 0.0077,\n          \"rank_corr\": -0.073\n        },\n        \"gen7\": {\n          \"ppl\": 51.2,\n          \"sel_ratio\": 0.95,\n          \"rare\": 0.0061,\n          \"rank_corr\": -0.075\n        }\n      },\n      \"comparison_at_gen7\": {\n        \"vs_rgds\": {\n          \"ppl_reduction_pct\": 29.7,\n          \"rare_improvement_pct\": 32.6,\n          \"sel_ratio_change\": \"0.52 → 0.95（从严重失调恢复到接近 1.0）\"\n        },\n        \"vs_uncurated\": {\n          \"ppl_excess_pct\": 6.4,\n          \"rare_deficit_pct\": 29.9\n        },\n        \"vs_external\": {\n          \"ppl_excess_pct\": 11.8,\n          \"rare_deficit_pct\": 30.7\n        }\n      }\n    },\n    \"tables\": [\n      \"Table 6: RGDS vs Re-anchored RGDS vs Uncurated vs External gen7 四方对比\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"re-anchoring 验证了 alignment gap 的因果性：消除嵌入退化 → 选择恢复 → PPL 近乎完全恢复。\\nrare n-gram +32.6% 满足 best 档 [10, 40%] 要求。\\n论文从\\\"发现问题\\\"升级为\\\"发现问题 + 简单修复部分有效 + 定位残余问题在生成端\\\"。\\n为 §7 future work 自然引出\\\"生成端干预\\\"方向。\\n\\n\\nre-anchoring 用预训练嵌入做选择，切断\\\"模型退化→嵌入退化→选择退化→模型更退化\\\"的反馈环。\\n\\nselection ratio 稳定在 ~1.0（1.04→0.95 轻微下降），而非 RGDS 的 1.04→0.52 断崖式下降。\\n轻微下降原因：即使嵌入质量好，生成数据本身在退化，候选池绝对多样性下降，\\n使得预训练嵌入虽能正确排序但最优子集的 ratio 也略有缩水。\\n\\nPPL 大幅恢复：72.8 → 51.2（-29.7%），接近 uncurated 的 48.1（仅高 6.4%）。\\n说明 RGDS 的 PPL 灾难主要来自选择偏差，而非生成退化本身。\\nRe-anchoring 消除了选择偏差 → PPL 近乎完全恢复。\\n\\nrare n-gram 部分恢复：0.0046 → 0.0061（+32.6%），但仍低于 uncurated 0.0087（-29.9%）。\\nrare n-gram 损失有两个来源：\\n(1) 选择偏差——词汇贫乏样本被优先选中→被 re-anchoring 修复，贡献 ~1/3 恢复\\n(2) 生成端词汇萎缩——模型逐渐丢失低频词能力→re-anchoring 无法修复\\n这个解耦本身就是一个有价值的发现。\\n\"\n  },\n  {\n    \"name\": \"OpenWebText 子集 三方法对比 (GPT2-125M, seed=42)\",\n    \"description\": \"在 OpenWebText 上验证 alignment gap 跨数据集泛化性。回应审稿人 R2。\",\n    \"results\": {\n      \"rgds\": {\n        \"gen0\": {\n          \"ppl\": 27.5,\n          \"sel_ratio\": 1.05,\n          \"rare\": 0.0312,\n          \"rank_corr\": -0.053\n        },\n        \"gen1\": {\n          \"ppl\": 31.8,\n          \"sel_ratio\": 0.97,\n          \"rare\": 0.023,\n          \"rank_corr\": -0.068\n        },\n        \"gen2\": {\n          \"ppl\": 37.4,\n          \"sel_ratio\": 0.89,\n          \"rare\": 0.0172,\n          \"rank_corr\": -0.082\n        },\n        \"gen3\": {\n          \"ppl\": 42.8,\n          \"sel_ratio\": 0.81,\n          \"rare\": 0.0129,\n          \"rank_corr\": -0.096\n        },\n        \"gen4\": {\n          \"ppl\": 48.1,\n          \"sel_ratio\": 0.73,\n          \"rare\": 0.0098,\n          \"rank_corr\": -0.11\n        },\n        \"gen5\": {\n          \"ppl\": 52.5,\n          \"sel_ratio\": 0.66,\n          \"rare\": 0.0079,\n          \"rank_corr\": -0.122\n        },\n        \"gen6\": {\n          \"ppl\": 56.2,\n          \"sel_ratio\": 0.59,\n          \"rare\": 0.0065,\n          \"rank_corr\": -0.133\n        },\n        \"gen7\": {\n          \"ppl\": 59.1,\n          \"sel_ratio\": 0.53,\n          \"rare\": 0.0054,\n          \"rank_corr\": -0.144\n        }\n      },\n      \"uncurated\": {\n        \"gen0\": {\n          \"ppl\": 27.2,\n          \"rare\": 0.031,\n          \"rank_corr\": -0.02\n        },\n        \"gen1\": {\n          \"ppl\": 33.5,\n          \"rare\": 0.0212,\n          \"rank_corr\": -0.048\n        },\n        \"gen2\": {\n          \"ppl\": 39.2,\n          \"rare\": 0.0158,\n          \"rank_corr\": -0.044\n        },\n        \"gen3\": {\n          \"ppl\": 43.8,\n          \"rare\": 0.0131,\n          \"rank_corr\": -0.04\n        },\n        \"gen4\": {\n          \"ppl\": 43.2,\n          \"rare\": 0.0115,\n          \"rank_corr\": -0.038\n        },\n        \"gen5\": {\n          \"ppl\": 40.8,\n          \"rare\": 0.0108,\n          \"rank_corr\": -0.044\n        },\n        \"gen6\": {\n          \"ppl\": 39.1,\n          \"rare\": 0.01,\n          \"rank_corr\": -0.06\n        },\n        \"gen7\": {\n          \"ppl\": 38.5,\n          \"rare\": 0.0095,\n          \"rank_corr\": -0.08\n        }\n      },\n      \"external_only\": {\n        \"gen0\": {\n          \"ppl\": 27.0,\n          \"sel_ratio\": 1.09,\n          \"rare\": 0.0311,\n          \"rank_corr\": -0.021\n        },\n        \"gen1\": {\n          \"ppl\": 31.2,\n          \"sel_ratio\": 1.13,\n          \"rare\": 0.0215,\n          \"rank_corr\": -0.03\n        },\n        \"gen2\": {\n          \"ppl\": 36.5,\n          \"sel_ratio\": 1.16,\n          \"rare\": 0.016,\n          \"rank_corr\": -0.034\n        },\n        \"gen3\": {\n          \"ppl\": 40.2,\n          \"sel_ratio\": 1.19,\n          \"rare\": 0.0132,\n          \"rank_corr\": -0.037\n        },\n        \"gen4\": {\n          \"ppl\": 40.0,\n          \"sel_ratio\": 1.22,\n          \"rare\": 0.0116,\n          \"rank_corr\": -0.039\n        },\n        \"gen5\": {\n          \"ppl\": 38.2,\n          \"sel_ratio\": 1.25,\n          \"rare\": 0.0109,\n          \"rank_corr\": -0.038\n        },\n        \"gen6\": {\n          \"ppl\": 36.8,\n          \"sel_ratio\": 1.27,\n          \"rare\": 0.0101,\n          \"rank_corr\": -0.036\n        },\n        \"gen7\": {\n          \"ppl\": 36.1,\n          \"sel_ratio\": 1.29,\n          \"rare\": 0.0096,\n          \"rank_corr\": -0.035\n        }\n      },\n      \"derived\": {\n        \"rgds_ppl_excess_vs_uncurated_pct\": 53.5,\n        \"rgds_rare_deficit_vs_uncurated_pct\": 43.2,\n        \"external_ppl_improvement_vs_uncurated_pct\": -6.2\n      }\n    },\n    \"tables\": [\n      \"Table 7: WikiText-103 vs OpenWebText gen7 指标对比（绝对值 + 相对差异）\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"alignment gap 跨数据集完全泛化。相对幅度在 WikiText 和 OWT 上一致（±3%），\\n强化\\\"机制是通用的\\\"论点。审稿人 R2 被有效回应。\\ncombined 全部证据：2 datasets × 2 model sizes × 3 seeds + 1 mitigation = \\n极强的现象鲁棒性 + 因果验证。投 8 页 Findings 绰绰有余。\\n\\nOWT 基线 PPL 更低（27 vs 37），因为 GPT2 预训练语料 WebText 与 OWT 同分布。\\nOWT 基线 rare n-gram 略高（0.031 vs 0.029），因 web 文本词汇更多样化。\\n\\nalignment gap 相对幅度与 WikiText 高度一致：\\n- sel_ratio: 1.05→0.53（WikiText: 1.04→0.52）\\n- PPL excess: +53.5%（WikiText: +51.4%）\\n- rare deficit: -43.2%（WikiText: -47.1%）\\n- external ratio: 1.09→1.29（WikiText: 1.08→1.28）\\n\\n一致性的机制解释：alignment gap 是模型内部嵌入空间收缩的产物，\\n与训练数据领域无关。self-iterate 反馈环的收缩动力学是训练过程的内禀性质，\\n不依赖数据分布的具体形态。数据集只影响绝对 PPL 水平（通过基线语言建模难度），\\n不影响 gap 的相对大小。\\n\"\n  }\n]",
      "numLines": 976,
      "startLine": 1,
      "totalLines": 976
    }
  },
  "sourceToolAssistantUUID": "4cf3d0dc-8505-4f4c-804e-41389f4174d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T08:33:59.516Z_

<details><summary>↩ Tool result · `toolu_01NqHxoi3z9PozMgTK9SLarb`</summary>

```text
1	# Paper Framing — Embedding Alignment Gap
2	
3	## Target Venue
4	EMNLP 2026 ARR (deadline: May 25, 2026) — Findings full paper (8 pages)
5	
6	## Title (working)
7	"The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training"
8	
9	## Core Insight
10	In iterative self-training (student-as-generator feedback loop), the geometric diversity of a model's internal embeddings becomes systematically misaligned with content diversity (measured by rare n-gram survival). This "alignment gap" worsens monotonically across generations, causing diversity-based data selection using internal representations to **accelerate** rather than prevent model collapse. Frozen external embeddings (e.g., Contriever) are immune to this misalignment.
11	
12	## Core Claims
13	
14	### C1: Alignment Gap Exists and Worsens Monotonically
15	- Internal embedding diversity selection ratio degrades from ~1.04 (Gen 0) to ~0.52 (Gen 7)
16	- The model increasingly selects vocabulary-poor samples when using its own representations for diversity scoring
17	- Evidence: Phase 2 RGDS selection diagnostics (GPT2-125M, WikiText-103, self-iterate)
18	
19	### C2-weak: Frozen External Embeddings Are Immune to the Gap
20	- Contriever-based selection maintains ratio >1.1 across all generations (1.14→1.28 through Gen 4)
21	- External embeddings improve model quality (PPL -6.5% vs uncurated) but do NOT improve rare n-gram survival
22	- This is a comparative claim: external embeddings "don't make the mistake" internal ones make, not a solution to vocabulary collapse
23	- The dissociation between PPL improvement and rare n-gram stagnation itself is an interesting finding
24	
25	### C3: The Gap Causes Accelerated Collapse
26	- RGDS (internal diversity selection) produces PPL 75.07 vs uncurated 50.28 (+49%) and rare n-gram 0.0051 vs 0.0090 (-43%)
27	- Complete causal chain: embedding space contracts → "geometrically diverse" = "vocabulary-poor" → selection amplifies homogeneity → accelerated collapse
28	
29	## Secondary Claims
30	
31	### S1: PPL and Rare N-gram Measure Different Collapse Dimensions
32	- External selection improves PPL (-6.5%) without improving rare n-gram survival
33	- Selection ratio >1.1 translates to PPL gains but not vocabulary diversity gains
34	- Implication: semantic diversity ≠ lexical diversity in the context of iterative distillation
35	
36	### S2: Representation Quality Metrics Don't Detect Diversity Collapse
37	- RankMe increases during collapse (280→303, +8%)
38	- k-NN probe accuracy stable (0.988 throughout)
39	- These metrics track representation structure, not content diversity — a cautionary finding for monitoring frameworks
40	
41	## Anticipated Reviewer Concerns
42	
43	### R1: "GPT2-125M is too small — does this generalize?"
44	- Response: GPT2-medium (355M) experiments planned; alignment gap mechanism (embedding space contraction under self-iterate) is architecture-general
45	- If GPT2-medium shows gap: "scales beyond toy models"
46	
47	### R2: "Only one dataset (WikiText-103)"
48	- Response: OpenWebText subset planned as P1
49	- The mechanism is data-agnostic (self-iterate collapse is well-documented across datasets)
50	
51	### R3: "N=1 seed — is this noise?"
52	- Response: 3 seeds per configuration planned; the monotonic trend over 8 generations (not a single-point measurement) reduces seed sensitivity concern
53	- seed=123 already running as replication
54	
55	### R4: "You only found a problem, not a solution"
56	- Response: (a) Embedding re-anchoring experiment planned as simple mitigation; (b) the finding itself has immediate practical value — practitioners should avoid internal-embedding-based curation during iterative training
57	- If re-anchoring works → upgrade to "found + solved"
58	
59	### R5: "What's the theoretical explanation for the gap?"
60	- Connect to neural collapse literature (Papyan et al. 2020): self-iterate reduces intra-class variability → embedding effective dimensionality drops → greedy submodular selection in low-dim space favors collapsed mode directions
61	- Not a formal proof, but a plausible mechanistic intuition with empirical support
62	
63	### R6: "External embeddings don't improve rare n-gram — how is C2 useful?"
64	- C2 is comparative: shows the gap is specific to internal embeddings under training feedback, not an inherent property of embedding-based selection
65	- PPL improvement shows external selection captures meaningful diversity (semantic level), even if not lexical level
66	- Opens future work: what selection signal DOES preserve lexical diversity?
67	
68	## Narrative Arc
69	1. **Setup**: Iterative self-training causes model collapse (established). Diversity-based data curation is a natural mitigation idea.
70	2. **Surprise**: Using the model's own representations for diversity selection makes collapse WORSE, not better.
71	3. **Explanation**: The Embedding Alignment Gap — internal representations' notion of "diverse" diverges from content diversity as training progresses.
72	4. **Contrast**: Frozen external embeddings don't suffer this misalignment (but also don't solve vocabulary collapse).
73	5. **Implication**: Embedding-based diversity selection is unreliable in iterative settings; the field needs vocabulary-aware alternatives.
74	
75	## Related Work Positioning
76	- Model collapse: Shumailov et al. (Nature 2024), Alemohammad et al. (2024), Dohmatob et al. (2024)
77	- Data selection/curation: SemDeDup (Abbas 2023), D4 (Tirumala 2023), DSIR (Xie 2023) — these use external embeddings for static (non-iterative) curation; we show iterative setting introduces new failure mode
78	- Neural collapse: Papyan et al. (2020) — theoretical grounding for why embeddings lose diversity signal
79	- Representation quality metrics: RankMe (Garrido et al. 2023) — we show RankMe doesn't detect diversity collapse
80	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1892d7ab-f8ef-4206-a2fc-558694b4d534",
  "isSidechain": false,
  "promptId": "ad861b3f-869b-46c3-a458-a9928fad5b05",
  "type": "user",
  "uuid": "4258fc09-3297-4150-8b3c-2cf9e0e9afb3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/paper_framing.md",
      "content": "# Paper Framing — Embedding Alignment Gap\n\n## Target Venue\nEMNLP 2026 ARR (deadline: May 25, 2026) — Findings full paper (8 pages)\n\n## Title (working)\n\"The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training\"\n\n## Core Insight\nIn iterative self-training (student-as-generator feedback loop), the geometric diversity of a model's internal embeddings becomes systematically misaligned with content diversity (measured by rare n-gram survival). This \"alignment gap\" worsens monotonically across generations, causing diversity-based data selection using internal representations to **accelerate** rather than prevent model collapse. Frozen external embeddings (e.g., Contriever) are immune to this misalignment.\n\n## Core Claims\n\n### C1: Alignment Gap Exists and Worsens Monotonically\n- Internal embedding diversity selection ratio degrades from ~1.04 (Gen 0) to ~0.52 (Gen 7)\n- The model increasingly selects vocabulary-poor samples when using its own representations for diversity scoring\n- Evidence: Phase 2 RGDS selection diagnostics (GPT2-125M, WikiText-103, self-iterate)\n\n### C2-weak: Frozen External Embeddings Are Immune to the Gap\n- Contriever-based selection maintains ratio >1.1 across all generations (1.14→1.28 through Gen 4)\n- External embeddings improve model quality (PPL -6.5% vs uncurated) but do NOT improve rare n-gram survival\n- This is a comparative claim: external embeddings \"don't make the mistake\" internal ones make, not a solution to vocabulary collapse\n- The dissociation between PPL improvement and rare n-gram stagnation itself is an interesting finding\n\n### C3: The Gap Causes Accelerated Collapse\n- RGDS (internal diversity selection) produces PPL 75.07 vs uncurated 50.28 (+49%) and rare n-gram 0.0051 vs 0.0090 (-43%)\n- Complete causal chain: embedding space contracts → \"geometrically diverse\" = \"vocabulary-poor\" → selection amplifies homogeneity → accelerated collapse\n\n## Secondary Claims\n\n### S1: PPL and Rare N-gram Measure Different Collapse Dimensions\n- External selection improves PPL (-6.5%) without improving rare n-gram survival\n- Selection ratio >1.1 translates to PPL gains but not vocabulary diversity gains\n- Implication: semantic diversity ≠ lexical diversity in the context of iterative distillation\n\n### S2: Representation Quality Metrics Don't Detect Diversity Collapse\n- RankMe increases during collapse (280→303, +8%)\n- k-NN probe accuracy stable (0.988 throughout)\n- These metrics track representation structure, not content diversity — a cautionary finding for monitoring frameworks\n\n## Anticipated Reviewer Concerns\n\n### R1: \"GPT2-125M is too small — does this generalize?\"\n- Response: GPT2-medium (355M) experiments planned; alignment gap mechanism (embedding space contraction under self-iterate) is architecture-general\n- If GPT2-medium shows gap: \"scales beyond toy models\"\n\n### R2: \"Only one dataset (WikiText-103)\"\n- Response: OpenWebText subset planned as P1\n- The mechanism is data-agnostic (self-iterate collapse is well-documented across datasets)\n\n### R3: \"N=1 seed — is this noise?\"\n- Response: 3 seeds per configuration planned; the monotonic trend over 8 generations (not a single-point measurement) reduces seed sensitivity concern\n- seed=123 already running as replication\n\n### R4: \"You only found a problem, not a solution\"\n- Response: (a) Embedding re-anchoring experiment planned as simple mitigation; (b) the finding itself has immediate practical value — practitioners should avoid internal-embedding-based curation during iterative training\n- If re-anchoring works → upgrade to \"found + solved\"\n\n### R5: \"What's the theoretical explanation for the gap?\"\n- Connect to neural collapse literature (Papyan et al. 2020): self-iterate reduces intra-class variability → embedding effective dimensionality drops → greedy submodular selection in low-dim space favors collapsed mode directions\n- Not a formal proof, but a plausible mechanistic intuition with empirical support\n\n### R6: \"External embeddings don't improve rare n-gram — how is C2 useful?\"\n- C2 is comparative: shows the gap is specific to internal embeddings under training feedback, not an inherent property of embedding-based selection\n- PPL improvement shows external selection captures meaningful diversity (semantic level), even if not lexical level\n- Opens future work: what selection signal DOES preserve lexical diversity?\n\n## Narrative Arc\n1. **Setup**: Iterative self-training causes model collapse (established). Diversity-based data curation is a natural mitigation idea.\n2. **Surprise**: Using the model's own representations for diversity selection makes collapse WORSE, not better.\n3. **Explanation**: The Embedding Alignment Gap — internal representations' notion of \"diverse\" diverges from content diversity as training progresses.\n4. **Contrast**: Frozen external embeddings don't suffer this misalignment (but also don't solve vocabulary collapse).\n5. **Implication**: Embedding-based diversity selection is unreliable in iterative settings; the field needs vocabulary-aware alternatives.\n\n## Related Work Positioning\n- Model collapse: Shumailov et al. (Nature 2024), Alemohammad et al. (2024), Dohmatob et al. (2024)\n- Data selection/curation: SemDeDup (Abbas 2023), D4 (Tirumala 2023), DSIR (Xie 2023) — these use external embeddings for static (non-iterative) curation; we show iterative setting introduces new failure mode\n- Neural collapse: Papyan et al. (2020) — theoretical grounding for why embeddings lose diversity signal\n- Representation quality metrics: RankMe (Garrido et al. 2023) — we show RankMe doesn't detect diversity collapse\n",
      "numLines": 80,
      "startLine": 1,
      "totalLines": 80
    }
  },
  "sourceToolAssistantUUID": "1892d7ab-f8ef-4206-a2fc-558694b4d534",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T08:33:59.506Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NqHxoi3z9PozMgTK9SLarb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "180e509e-675b-47c9-9b8c-b855e37547ad",
  "isSidechain": false,
  "requestId": "req_011CazG21S4JJLvuQpJtqiMP",
  "type": "assistant",
  "uuid": "1892d7ab-f8ef-4206-a2fc-558694b4d534",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4CnDWByufTH1u2J2Woz4i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11426,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11426
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260513T081019 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compou…",
  "leafUuid": "4258fc09-3297-4150-8b3c-2cf9e0e9afb3",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP paper on alignment gap and model collapse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3"
}
```

---

### Assistant

_source line 14 · 2026-05-13T08:34:03.508Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the data and framing. Let me write the full LaTeX paper. Let me first ensure the output directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4258fc09-3297-4150-8b3c-2cf9e0e9afb3",
  "isSidechain": false,
  "requestId": "req_011CazG2Ln9LJNE6jPFM1D6F",
  "type": "assistant",
  "uuid": "098a2084-3eb0-44bb-bb0f-0414a29bb659",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LxL6EwhJHMaKSapFRj2x8Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16761,
      "cache_read_input_tokens": 23267,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16761,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 23267,
          "cache_creation_input_tokens": 16761,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16761
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

_source line 15 · 2026-05-13T08:34:03.970Z_

Now I'll write the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "098a2084-3eb0-44bb-bb0f-0414a29bb659",
  "isSidechain": false,
  "requestId": "req_011CazG2Ln9LJNE6jPFM1D6F",
  "type": "assistant",
  "uuid": "1b4ec833-6098-45d7-8746-a66cf75bf6d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LxL6EwhJHMaKSapFRj2x8Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16761,
      "cache_read_input_tokens": 23267,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16761,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 23267,
          "cache_creation_input_tokens": 16761,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16761
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

_source line 16 · 2026-05-13T08:34:06.465Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NpcgEitVEHq4Xx3fVgyKwj`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/",
  "description": "Check output directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b4ec833-6098-45d7-8746-a66cf75bf6d0",
  "isSidechain": false,
  "requestId": "req_011CazG2Ln9LJNE6jPFM1D6F",
  "type": "assistant",
  "uuid": "d402b74a-4215-44f2-ba28-97637470eb2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LxL6EwhJHMaKSapFRj2x8Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16761,
      "cache_read_input_tokens": 23267,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16761,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 23267,
          "cache_creation_input_tokens": 16761,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16761
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

_source line 17 · 2026-05-13T08:34:06.613Z_

<details><summary>↩ Tool result · `toolu_01NpcgEitVEHq4Xx3fVgyKwj`</summary>

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
  "parentUuid": "d402b74a-4215-44f2-ba28-97637470eb2f",
  "isSidechain": false,
  "promptId": "ad861b3f-869b-46c3-a458-a9928fad5b05",
  "type": "user",
  "uuid": "1ccdcdb8-09b0-4f7e-b366-2db91e9ebb0f",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d402b74a-4215-44f2-ba28-97637470eb2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-13T08:36:32.417Z_

<details open><summary>🔧 Tool call — Write · `toolu_01HewNWwPUpwYTU19poRP5iM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\title{The Embedding Alignment Gap: Why Diversity-Based Data Selection\\\\Accelerates Model Collapse in Iterative Self-Training}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nDiversity-based data curation is a natural strategy to mitigate model collapse in iterative self-training, yet we show it can \\emph{accelerate} collapse when using the model's own representations.\nWe identify the \\textbf{Embedding Alignment Gap}: as a language model is iteratively trained on its own outputs, its internal embeddings' notion of ``diverse'' becomes systematically misaligned with content diversity.\nConcretely, in an 8-generation self-training loop on GPT-2 (125M and 355M), an internal-embedding diversity selector's selection ratio drops monotonically from $1.04$ to $0.52$ ($95\\%$ CI $[0.46, 0.58]$, $n{=}3$ seeds), producing $+50\\%$ perplexity and $-47\\%$ rare $n$-gram survival relative to uncurated baselines.\nA frozen external retriever (Contriever) is immune to this misalignment---its selection ratio \\emph{rises} to $1.28$ ($95\\%$ CI $[1.21, 1.35]$)---yet still fails to preserve lexical diversity, revealing that semantic diversity $\\neq$ lexical diversity.\nA simple re-anchoring fix that uses pre-trained embeddings for selection recovers $30\\%$ of the perplexity gap and $33\\%$ of rare $n$-gram loss, localizing $\\sim$two-thirds of residual vocabulary collapse to the generation side.\nOur results hold across two model scales, two datasets (WikiText-103, OpenWebText), and three random seeds.\nThese findings carry a practical warning: embedding-based diversity selection is unreliable in iterative training and may actively harm model quality.\n\\end{abstract}\n\n%=============================================\n\\section{Introduction}\n\\label{sec:intro}\n\nIterative self-training---in which a model generates data that is fed back into training---is increasingly common in language modeling pipelines involving synthetic data augmentation \\cite{shumailov2024nature}, knowledge distillation loops, and self-play.\nA well-documented failure mode of such loops is \\emph{model collapse}: progressive loss of distributional diversity as rare modes are underrepresented in generated data \\cite{shumailov2024nature,alemohammad2024selfconsuming,dohmatob2024tale}.\n\nA natural countermeasure is diversity-based data curation: selecting a maximally diverse subset from the generated pool before training.\nMethods such as SemDeDup \\cite{abbas2023semdedup}, D$^4$ \\cite{tirumala2023d4}, and facility-location submodular selection \\cite{kirchhoff2014submodular} measure diversity in embedding space and have proven effective for static dataset curation.\nThe implicit assumption is that geometric diversity in representation space is a reliable proxy for content diversity.\n\nWe show this assumption breaks down catastrophically in the iterative setting.\nAs the model trains on its own outputs across generations, its embedding space contracts in directions correlated with vocabulary diversity.\nA greedy diversity selector operating in this shrinking space systematically favors vocabulary-poor samples---precisely the opposite of the intended effect.\nWe call this progressive misalignment the \\textbf{Embedding Alignment Gap}.\n\nWe make the following contributions:\n\\begin{enumerate}\n\\item We identify and quantify the Embedding Alignment Gap: a monotonic degradation of the alignment between embedding-space diversity and content diversity across self-training generations (\\S\\ref{sec:main_results}).\n\\item We show that diversity-based selection using internal embeddings \\emph{accelerates} model collapse, producing $+50\\%$ perplexity and $-47\\%$ rare $n$-gram loss relative to uncurated training (\\S\\ref{sec:main_results}).\n\\item We demonstrate that frozen external embeddings (Contriever) are immune to the gap but do not preserve lexical diversity, establishing that semantic diversity $\\neq$ lexical diversity (\\S\\ref{sec:external}).\n\\item We propose embedding re-anchoring as a simple partial mitigation, recovering $\\sim$33\\% of rare $n$-gram loss and localizing residual collapse to the generation side (\\S\\ref{sec:mitigation}).\n\\item We validate all findings across two model scales (GPT-2 125M, 355M), two datasets (WikiText-103, OpenWebText), and three random seeds (\\S\\ref{sec:robustness}).\n\\end{enumerate}\n\n%=============================================\n\\section{Background and Related Work}\n\\label{sec:related}\n\n\\paragraph{Model collapse.}\n\\citet{shumailov2024nature} demonstrated that iteratively training on model-generated data leads to progressive loss of distributional tails.\n\\citet{alemohammad2024selfconsuming} formalized this as ``self-consuming generative models'' and showed tail collapse scales with generation count.\n\\citet{dohmatob2024tale} provided theoretical analysis connecting collapse to the spectral properties of the data distribution.\nOur work complements this line by showing that a natural mitigation (diversity selection) can paradoxically worsen collapse.\n\n\\paragraph{Data curation and selection.}\nEmbedding-based data selection has been effective for static corpus curation: SemDeDup \\cite{abbas2023semdedup} deduplicates near-neighbors in embedding space; D$^4$ \\cite{tirumala2023d4} uses prototypicality scoring; DSIR \\cite{xie2023dsir} importance-weights by distribution matching.\nThese methods assume a fixed embedding space. We show that in iterative settings, the embedding space co-evolves with the data distribution, breaking this assumption.\n\n\\paragraph{Neural collapse.}\n\\citet{papyan2020prevalence} showed that deep network representations converge to a simplex ETF structure during prolonged training.\nIn the iterative self-training setting, this collapse-like contraction of the embedding space directly reduces the signal available for diversity-based selection---providing a mechanistic explanation for the alignment gap.\n\n\\paragraph{Representation quality metrics.}\nRankMe \\cite{garrido2023rankme} measures effective dimensionality of representations; $k$-NN probes assess local structure quality.\nWe show these metrics are \\emph{insensitive} to the alignment gap: RankMe increases during collapse, and $k$-NN accuracy remains stable, making them unreliable monitors for diversity degradation.\n\n%=============================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Iterative Self-Training Loop}\n\nWe define a generation-indexed training loop. Let $M_0$ be a pre-trained language model and $\\mathcal{D}_0$ the original training corpus.\nAt each generation $t$:\n\\begin{enumerate}\n\\item \\textbf{Generate}: Sample $N$ sequences from $M_{t-1}$ to form candidate pool $\\mathcal{G}_t$.\n\\item \\textbf{Select}: Apply a selection function $S(\\mathcal{G}_t) \\to \\mathcal{D}_t$ that selects a training subset.\n\\item \\textbf{Train}: Fine-tune $M_{t-1}$ on $\\mathcal{D}_t$ to obtain $M_t$.\n\\end{enumerate}\nWe compare three selection strategies:\n\\begin{itemize}\n\\item \\textbf{Uncurated}: $S = \\text{identity}$ (no selection; standard self-training baseline).\n\\item \\textbf{RGDS} (Representation-Guided Diversity Selection): Greedy submodular facility-location selection using $M_{t-1}$'s internal embeddings to maximize geometric diversity.\n\\item \\textbf{External-only}: Same submodular objective but using frozen Contriever \\cite{izacard2022contriever} embeddings instead of $M_{t-1}$'s representations.\n\\end{itemize}\n\n\\subsection{Selection Ratio: Quantifying the Alignment Gap}\n\nWe introduce the \\emph{selection ratio} as a diagnostic metric:\n\\begin{equation}\nr_t = \\frac{\\text{avg-rare}(S(\\mathcal{G}_t))}{\\text{avg-rare}(\\mathcal{G}_t)}\n\\end{equation}\nwhere $\\text{avg-rare}(\\cdot)$ computes mean rare $n$-gram frequency over a set.\nA well-calibrated diversity selector should satisfy $r_t \\geq 1$: the selected subset should be at least as lexically diverse as the full pool.\nThe alignment gap manifests as $r_t < 1$, indicating the selector systematically favors vocabulary-poor samples.\n\n\\subsection{Evaluation Metrics}\n\n\\begin{itemize}\n\\item \\textbf{Perplexity} (PPL): Evaluated on held-out test data from the original distribution.\n\\item \\textbf{Rare $n$-gram survival}: Fraction of $n$-grams in generated text that appear $\\leq 5$ times in the original corpus, measuring lexical diversity.\n\\item \\textbf{Rank correlation}: Spearman correlation between embedding-space diversity rank and rare $n$-gram rank across samples. Increasingly negative values indicate growing misalignment.\n\\item \\textbf{RankMe} \\cite{garrido2023rankme}: Effective rank of the embedding covariance matrix.\n\\item \\textbf{$k$-NN accuracy}: Leave-one-out $k$-NN classification accuracy in embedding space.\n\\end{itemize}\n\n%=============================================\n\\section{Main Results: The Alignment Gap}\n\\label{sec:main_results}\n\n\\subsection{Experimental Setup}\n\nWe use GPT-2 125M as the base model, fine-tuned on WikiText-103.\nThe self-training loop runs for 8 generations ($t = 0, \\ldots, 7$) with all three selection strategies.\nResults are averaged over 3 random seeds (42, 123, 456) with 95\\% confidence intervals.\n\n\\subsection{Selection Ratio Degradation (C1)}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Gen} & \\textbf{RGDS} & \\textbf{External} & \\textbf{Uncurated} \\\\\n\\midrule\n0 & 1.04 & 1.08 & --- \\\\\n1 & 0.96 & 1.12 & --- \\\\\n2 & 0.87 & 1.15 & --- \\\\\n3 & 0.79 & 1.18 & --- \\\\\n4 & 0.71 & 1.21 & --- \\\\\n5 & 0.64 & 1.24 & --- \\\\\n6 & 0.57 & 1.26 & --- \\\\\n7 & 0.52 & 1.28 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Selection ratio across generations (seed=42). RGDS ratio drops monotonically below 1.0, indicating the selector increasingly favors vocabulary-poor samples. External embeddings maintain ratio $>1.0$ throughout.}\n\\label{tab:sel_ratio}\n\\end{table}\n\nTable~\\ref{tab:sel_ratio} shows the selection ratio across 8 generations.\nRGDS begins near parity ($r_0 = 1.04$) but degrades monotonically to $r_7 = 0.52$---meaning the selected subset contains only half the rare $n$-gram density of the unselected pool.\nAcross 3 seeds, the gen-7 RGDS ratio averages $0.517$ (95\\% CI $[0.455, 0.579]$), with the confidence interval entirely below 1.0.\n\nThe rank correlation between embedding diversity scores and rare $n$-gram frequency (Table~\\ref{tab:main_full}) becomes increasingly negative ($-0.058 \\to -0.155$), confirming that the embedding space's notion of ``geometrically distant'' progressively aligns with vocabulary poverty rather than vocabulary richness.\n\n\\subsection{Accelerated Collapse (C3)}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{PPL}$\\downarrow$ & \\textbf{Rare}$\\uparrow$ & \\textbf{Rank Corr.} & \\textbf{Sel. Ratio} \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Generation 0}} \\\\\nUncurated & 37.1 & 0.0290 & $-$0.023 & --- \\\\\nRGDS & 37.2 & 0.0288 & $-$0.058 & 1.04 \\\\\nExternal & 36.8 & 0.0289 & $-$0.024 & 1.08 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Generation 7 (3-seed mean $\\pm$ std)}} \\\\\nUncurated & 48.3{\\scriptsize$\\pm$0.9} & .0088{\\scriptsize$\\pm$.0003} & $-$.087 & --- \\\\\nRGDS & 72.5{\\scriptsize$\\pm$1.9} & .0046{\\scriptsize$\\pm$.0004} & $-$.155 & 0.52{\\scriptsize$\\pm$.03} \\\\\nExternal & 45.7{\\scriptsize$\\pm$0.8} & .0088{\\scriptsize$\\pm$.0002} & $-$.037 & 1.28{\\scriptsize$\\pm$.03} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Core metrics at generations 0 and 7 (GPT-2 125M, WikiText-103). RGDS worsens both PPL (+50\\% vs uncurated) and rare $n$-gram survival ($-$47\\%). 3-seed 95\\% CIs for RGDS vs uncurated PPL do not overlap: $[67.9, 77.1]$ vs $[46.0, 50.6]$, $p < 0.01$.}\n\\label{tab:main_full}\n\\end{table}\n\nTable~\\ref{tab:main_full} summarizes the core finding.\nAt generation 7, RGDS produces PPL 72.5 vs.\\ uncurated 48.3 ($+50.2\\%$) and rare $n$-gram 0.0046 vs.\\ 0.0088 ($-47.1\\%$).\nThe 95\\% confidence intervals do not overlap (PPL: $[67.9, 77.1]$ vs.\\ $[46.0, 50.6]$; Cohen's $d > 3$).\nRGDS was designed to \\emph{prevent} collapse, but the alignment gap causes it to amplify the very failure mode it targets.\n\nThe causal chain is: (1) self-training contracts the embedding space; (2) greedy diversity selection in the contracted space picks points that are ``far'' in the degenerate geometry, which happen to be vocabulary-poor; (3) training on these impoverished subsets further contracts the embedding space, closing a positive feedback loop.\n\n\\subsection{Representation Metrics Miss the Collapse (S2)}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Gen} & \\textbf{PPL} & \\textbf{Rare} & \\textbf{RankMe} & \\textbf{$k$-NN} \\\\\n\\midrule\n0 & 37.2 & 0.0288 & 281.5 & 0.988 \\\\\n3 & 56.3 & 0.0113 & 300.1 & 0.988 \\\\\n7 & 72.8 & 0.0046 & 294.3 & 0.988 \\\\\n\\midrule\n$\\Delta$ & +96\\% & $-$84\\% & +5\\% & 0.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{RankMe and $k$-NN under RGDS collapse (seed=42). Despite catastrophic PPL and rare $n$-gram degradation, RankMe \\emph{increases} and $k$-NN is stable. These metrics track geometric structure, not content diversity.}\n\\label{tab:metrics_blind}\n\\end{table}\n\nTable~\\ref{tab:metrics_blind} reveals a cautionary finding: RankMe increases from 281.5 to 294.3 ($+5\\%$) during RGDS collapse, and $k$-NN accuracy remains at 0.988.\nThese metrics measure representation geometry---effective dimensionality and local neighborhood quality---but are blind to the misalignment between that geometry and downstream content diversity.\nPractitioners relying on such metrics to monitor iterative training would detect no anomaly even as diversity collapses.\n\n%=============================================\n\\section{External Embeddings and the PPL--Diversity Dissociation}\n\\label{sec:external}\n\nExternal-only selection using frozen Contriever embeddings maintains $r_t > 1.0$ across all generations (Table~\\ref{tab:sel_ratio}), rising to $1.28$ at gen 7 (95\\% CI $[1.21, 1.35]$).\nThis confirms the alignment gap is specific to embeddings under training feedback, not an inherent limitation of embedding-based selection.\n\nHowever, external selection reveals a striking dissociation (S1): it improves PPL relative to uncurated ($45.7$ vs.\\ $48.3$, $-5.4\\%$) while producing \\emph{identical} rare $n$-gram survival ($0.0088$ vs.\\ $0.0088$; CI fully overlapping: $[0.0083, 0.0093]$ vs.\\ $[0.0080, 0.0095]$).\nContriever captures topic-level and semantic-level diversity, which helps the model maintain broader coverage of test-set phenomena (lower PPL), but this semantic diversity does not translate into preservation of rare lexical patterns.\n\nThis dissociation implies that model collapse operates on at least two independent axes: \\emph{semantic} collapse (loss of topical coverage, reflected in PPL) and \\emph{lexical} collapse (loss of rare vocabulary patterns, reflected in rare $n$-gram survival).\nExternal embedding selection partially addresses the former but not the latter.\n\n%=============================================\n\\section{Mitigation: Embedding Re-Anchoring}\n\\label{sec:mitigation}\n\nThe alignment gap arises because the selector uses embeddings from $M_{t-1}$, which has been corrupted by prior self-training.\nA minimal fix: at each generation, compute diversity scores using the \\emph{original} pre-trained model $M_0$'s embeddings instead of $M_{t-1}$'s, while still training $M_{t-1} \\to M_t$ as usual.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{PPL}$\\downarrow$ & \\textbf{Rare}$\\uparrow$ & \\textbf{Sel. Ratio} \\\\\n\\midrule\nRGDS & 72.8 & 0.0046 & 0.52 \\\\\nRe-anchored RGDS & 51.2 & 0.0061 & 0.95 \\\\\nUncurated & 48.1 & 0.0087 & --- \\\\\nExternal-only & 45.8 & 0.0088 & 1.28 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Re-anchored vs.\\ RGDS improvement}} \\\\\n & $-$29.7\\% & +32.6\\% & +0.43 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Re-anchoring results (gen 7, GPT-2 125M, seed=42). Re-anchoring largely eliminates the selection ratio degradation ($0.52 \\to 0.95$) and recovers most of the PPL gap. Rare $n$-gram recovery is partial ($+33\\%$), localizing residual loss to the generation side.}\n\\label{tab:reanchor}\n\\end{table}\n\nTable~\\ref{tab:reanchor} shows that re-anchoring restores the selection ratio from 0.52 to 0.95 (near-parity), reduces PPL from 72.8 to 51.2 ($-29.7\\%$, close to uncurated's 48.1), and recovers rare $n$-gram survival from 0.0046 to 0.0061 ($+32.6\\%$).\n\nThe asymmetry between PPL recovery (near-complete) and rare $n$-gram recovery (partial) is informative.\nIt decomposes vocabulary collapse into two sources:\n\\begin{enumerate}\n\\item \\textbf{Selection-side}: The model's corrupted embeddings select vocabulary-poor subsets. Re-anchoring eliminates this component, recovering most PPL and $\\sim$1/3 of rare $n$-gram loss.\n\\item \\textbf{Generation-side}: The model itself progressively loses the ability to produce rare vocabulary, independent of what is selected. This accounts for the remaining $\\sim$2/3 of rare $n$-gram loss ($0.0061$ vs.\\ $0.0087$).\n\\end{enumerate}\n\nThis decomposition provides actionable direction: addressing model collapse fully requires generation-side interventions (e.g., vocabulary regularization, constrained decoding, or mixing in real data) in addition to selection-side fixes.\n\n%=============================================\n\\section{Robustness}\n\\label{sec:robustness}\n\n\\subsection{Multiple Seeds}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric (Gen 7)} & \\textbf{Mean} & \\textbf{Std} & \\textbf{95\\% CI} \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{RGDS}} \\\\\nPPL & 72.5 & 1.85 & [67.9, 77.1] \\\\\nSel.\\ ratio & 0.517 & 0.025 & [0.455, 0.579] \\\\\nRare $n$-gram & 0.0046 & 0.0004 & [0.0038, 0.0055] \\\\\nRank corr. & $-$0.155 & 0.007 & [$-$0.171, $-$0.139] \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Uncurated}} \\\\\nPPL & 48.3 & 0.91 & [46.0, 50.6] \\\\\nRare $n$-gram & 0.0088 & 0.0003 & [0.0080, 0.0095] \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{External-only}} \\\\\nPPL & 45.7 & 0.80 & [43.7, 47.7] \\\\\nSel.\\ ratio & 1.280 & 0.030 & [1.210, 1.350] \\\\\nRare $n$-gram & 0.0088 & 0.0002 & [0.0083, 0.0093] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Three-seed aggregated statistics (seeds 42, 123, 456; GPT-2 125M, WikiText-103). All key contrasts hold: RGDS ratio CI below 1.0; external ratio CI above 1.0; RGDS--uncurated PPL CIs non-overlapping.}\n\\label{tab:three_seed}\n\\end{table}\n\nTable~\\ref{tab:three_seed} reports 3-seed aggregated statistics.\nMethod-level differences (RGDS PPL $72.5$ vs.\\ uncurated $48.3$, $\\Delta = 24.2$) are an order of magnitude larger than seed-level variance (std $= 1.85$), yielding Cohen's $d > 3$.\nAll critical CIs are well-separated from threshold values.\n\n\\subsection{Model Scale: GPT-2 Medium (355M)}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Model} & \\textbf{Method} & \\textbf{PPL}$\\downarrow$ & \\textbf{Rare}$\\uparrow$ & \\textbf{Ratio} \\\\\n\\midrule\n\\multirow{3}{*}{125M} & Uncurated & 48.1 & 0.0087 & --- \\\\\n & RGDS & 72.8 & 0.0046 & 0.52 \\\\\n & External & 45.8 & 0.0088 & 1.28 \\\\\n\\midrule\n\\multirow{3}{*}{355M} & Uncurated & 41.8 & 0.0092 & --- \\\\\n & RGDS & 63.5 & 0.0052 & 0.56 \\\\\n & External & 38.8 & 0.0093 & 1.30 \\\\\n\\midrule\n\\multirow{3}{*}{355M$^\\dagger$} & Uncurated & 42.5 & 0.0089 & --- \\\\\n & RGDS & 65.1 & 0.0049 & 0.53 \\\\\n & External & 39.5 & 0.0091 & 1.27 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-scale comparison at gen 7 (WikiText-103). 355M results from seed=42 and $^\\dagger$seed=123. Relative magnitudes are consistent: RGDS PPL excess $+52\\%$ (125M) vs.\\ $+52\\%$ (355M); selection ratio endpoints $0.52$ vs.\\ $0.56$.}\n\\label{tab:scale}\n\\end{table}\n\nTable~\\ref{tab:scale} shows the alignment gap replicates on GPT-2 Medium (355M parameters).\nThe relative RGDS PPL excess over uncurated is $+51.9\\%$ (355M) vs.\\ $+51.4\\%$ (125M), and selection ratio endpoints are $0.56$ (355M) vs.\\ $0.52$ (125M).\nA second seed (123) on 355M confirms the trend with PPL excess $+53.2\\%$ and ratio $0.53$.\nThe mechanism's scale invariance is expected: the embedding alignment gap arises from training dynamics (embedding space contraction under self-iteration), not from model capacity per se.\n\n\\subsection{Dataset Generalization: OpenWebText}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Method} & \\textbf{PPL}$\\downarrow$ & \\textbf{Rare}$\\uparrow$ & \\textbf{Ratio} \\\\\n\\midrule\n\\multirow{3}{*}{Wiki} & Uncurated & 48.1 & 0.0087 & --- \\\\\n & RGDS & 72.8 & 0.0046 & 0.52 \\\\\n & External & 45.8 & 0.0088 & 1.28 \\\\\n\\midrule\n\\multirow{3}{*}{OWT} & Uncurated & 38.5 & 0.0095 & --- \\\\\n & RGDS & 59.1 & 0.0054 & 0.53 \\\\\n & External & 36.1 & 0.0096 & 1.29 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-dataset comparison at gen 7 (GPT-2 125M, seed=42). OpenWebText shows lower absolute PPL (GPT-2's pre-training domain) but identical alignment gap magnitudes: RGDS PPL excess $+54\\%$, rare deficit $-43\\%$.}\n\\label{tab:dataset}\n\\end{table}\n\nTable~\\ref{tab:dataset} shows the alignment gap generalizes to OpenWebText.\nDespite substantial differences in absolute baselines (OWT PPL 38.5 vs.\\ WikiText 48.1, owing to GPT-2's pre-training on WebText), relative alignment gap magnitudes are remarkably consistent: RGDS PPL excess $+53.5\\%$ (OWT) vs.\\ $+51.4\\%$ (WikiText); selection ratio $0.53$ (OWT) vs.\\ $0.52$ (WikiText).\nThe alignment gap is a property of the self-training dynamics, not of the data domain.\n\n%=============================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why does the alignment gap arise?}\nWe connect the mechanism to neural collapse \\cite{papyan2020prevalence}: iterative self-training reduces intra-distribution variability in the embedding space.\nAs the model ``memorizes'' its own output distribution, embeddings cluster along fewer effective directions.\nGreedy facility-location selection in this lower-dimensional space picks points that maximize geometric spread along the remaining directions---which, critically, are no longer aligned with lexical diversity.\nThe rank correlation evidence (Table~\\ref{tab:main_full}: $-0.058 \\to -0.155$) directly confirms this progressive misalignment.\n\n\\paragraph{Practical implications.}\nAny iterative training pipeline using the model's own representations for data selection is potentially vulnerable.\nThis includes retrieval-augmented self-improvement, iterative distillation with embedding-based filtering, and active learning with representation-space acquisition functions.\nOur results recommend either (a) using frozen external embeddings for selection, or (b) re-anchoring to pre-trained representations at each iteration.\n\n\\paragraph{Limitations.}\nOur experiments use GPT-2 family models (125M, 355M).\nWhile the alignment gap's relative magnitude is stable across these scales, verification on models $>1$B parameters remains future work.\nThe re-anchoring mitigation is simple by design; more sophisticated generation-side interventions may recover the remaining $\\sim$2/3 of vocabulary loss.\n\n%=============================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe identified the Embedding Alignment Gap: a systematic failure mode where diversity-based data selection using a model's own representations accelerates model collapse in iterative self-training.\nThe gap manifests as a monotonic degradation of the selection ratio from $1.04$ to $0.52$ over 8 generations, causing $+50\\%$ perplexity and $-47\\%$ rare $n$-gram loss relative to uncurated baselines.\nFrozen external embeddings are immune to the gap but reveal that semantic diversity does not ensure lexical diversity.\nA simple re-anchoring fix recovers $\\sim$30\\% of the gap, localizing the majority of residual collapse to the generation side.\nThese findings are robust across model scales, datasets, and random seeds.\nThe practical takeaway is clear: in iterative training, never trust the model's own embeddings for diversity-based data curation.\n\n\\bibliography{custom}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ccdcdb8-09b0-4f7e-b366-2db91e9ebb0f",
  "isSidechain": false,
  "requestId": "req_011CazG2rzq8NAuUSd33px6o",
  "type": "assistant",
  "uuid": "7874b0f4-beca-4aa3-83c7-21e317f7c186",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ChQBzbgr399Da6fPBEwbV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 209,
      "cache_read_input_tokens": 40028,
      "output_tokens": 8121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 209,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8121,
          "cache_read_input_tokens": 40028,
          "cache_creation_input_tokens": 209,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 209
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

_source line 19 · 2026-05-13T08:36:32.454Z_

<details><summary>↩ Tool result · `toolu_01HewNWwPUpwYTU19poRP5iM`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7874b0f4-beca-4aa3-83c7-21e317f7c186",
  "isSidechain": false,
  "promptId": "ad861b3f-869b-46c3-a458-a9928fad5b05",
  "type": "user",
  "uuid": "e473c86a-6f52-4e69-9006-d54f9763f2b9",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\title{The Embedding Alignment Gap: Why Diversity-Based Data Selection\\\\Accelerates Model Collapse in Iterative Self-Training}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nDiversity-based data curation is a natural strategy to mitigate model collapse in iterative self-training, yet we show it can \\emph{accelerate} collapse when using the model's own representations.\nWe identify the \\textbf{Embedding Alignment Gap}: as a language model is iteratively trained on its own outputs, its internal embeddings' notion of ``diverse'' becomes systematically misaligned with content diversity.\nConcretely, in an 8-generation self-training loop on GPT-2 (125M and 355M), an internal-embedding diversity selector's selection ratio drops monotonically from $1.04$ to $0.52$ ($95\\%$ CI $[0.46, 0.58]$, $n{=}3$ seeds), producing $+50\\%$ perplexity and $-47\\%$ rare $n$-gram survival relative to uncurated baselines.\nA frozen external retriever (Contriever) is immune to this misalignment---its selection ratio \\emph{rises} to $1.28$ ($95\\%$ CI $[1.21, 1.35]$)---yet still fails to preserve lexical diversity, revealing that semantic diversity $\\neq$ lexical diversity.\nA simple re-anchoring fix that uses pre-trained embeddings for selection recovers $30\\%$ of the perplexity gap and $33\\%$ of rare $n$-gram loss, localizing $\\sim$two-thirds of residual vocabulary collapse to the generation side.\nOur results hold across two model scales, two datasets (WikiText-103, OpenWebText), and three random seeds.\nThese findings carry a practical warning: embedding-based diversity selection is unreliable in iterative training and may actively harm model quality.\n\\end{abstract}\n\n%=============================================\n\\section{Introduction}\n\\label{sec:intro}\n\nIterative self-training---in which a model generates data that is fed back into training---is increasingly common in language modeling pipelines involving synthetic data augmentation \\cite{shumailov2024nature}, knowledge distillation loops, and self-play.\nA well-documented failure mode of such loops is \\emph{model collapse}: progressive loss of distributional diversity as rare modes are underrepresented in generated data \\cite{shumailov2024nature,alemohammad2024selfconsuming,dohmatob2024tale}.\n\nA natural countermeasure is diversity-based data curation: selecting a maximally diverse subset from the generated pool before training.\nMethods such as SemDeDup \\cite{abbas2023semdedup}, D$^4$ \\cite{tirumala2023d4}, and facility-location submodular selection \\cite{kirchhoff2014submodular} measure diversity in embedding space and have proven effective for static dataset curation.\nThe implicit assumption is that geometric diversity in representation space is a reliable proxy for content diversity.\n\nWe show this assumption breaks down catastrophically in the iterative setting.\nAs the model trains on its own outputs across generations, its embedding space contracts in directions correlated with vocabulary diversity.\nA greedy diversity selector operating in this shrinking space systematically favors vocabulary-poor samples---precisely the opposite of the intended effect.\nWe call this progressive misalignment the \\textbf{Embedding Alignment Gap}.\n\nWe make the following contributions:\n\\begin{enumerate}\n\\item We identify and quantify the Embedding Alignment Gap: a monotonic degradation of the alignment between embedding-space diversity and content diversity across self-training generations (\\S\\ref{sec:main_results}).\n\\item We show that diversity-based selection using internal embeddings \\emph{accelerates} model collapse, producing $+50\\%$ perplexity and $-47\\%$ rare $n$-gram loss relative to uncurated training (\\S\\ref{sec:main_results}).\n\\item We demonstrate that frozen external embeddings (Contriever) are immune to the gap but do not preserve lexical diversity, establishing that semantic diversity $\\neq$ lexical diversity (\\S\\ref{sec:external}).\n\\item We propose embedding re-anchoring as a simple partial mitigation, recovering $\\sim$33\\% of rare $n$-gram loss and localizing residual collapse to the generation side (\\S\\ref{sec:mitigation}).\n\\item We validate all findings across two model scales (GPT-2 125M, 355M), two datasets (WikiText-103, OpenWebText), and three random seeds (\\S\\ref{sec:robustness}).\n\\end{enumerate}\n\n%=============================================\n\\section{Background and Related Work}\n\\label{sec:related}\n\n\\paragraph{Model collapse.}\n\\citet{shumailov2024nature} demonstrated that iteratively training on model-generated data leads to progressive loss of distributional tails.\n\\citet{alemohammad2024selfconsuming} formalized this as ``self-consuming generative models'' and showed tail collapse scales with generation count.\n\\citet{dohmatob2024tale} provided theoretical analysis connecting collapse to the spectral properties of the data distribution.\nOur work complements this line by showing that a natural mitigation (diversity selection) can paradoxically worsen collapse.\n\n\\paragraph{Data curation and selection.}\nEmbedding-based data selection has been effective for static corpus curation: SemDeDup \\cite{abbas2023semdedup} deduplicates near-neighbors in embedding space; D$^4$ \\cite{tirumala2023d4} uses prototypicality scoring; DSIR \\cite{xie2023dsir} importance-weights by distribution matching.\nThese methods assume a fixed embedding space. We show that in iterative settings, the embedding space co-evolves with the data distribution, breaking this assumption.\n\n\\paragraph{Neural collapse.}\n\\citet{papyan2020prevalence} showed that deep network representations converge to a simplex ETF structure during prolonged training.\nIn the iterative self-training setting, this collapse-like contraction of the embedding space directly reduces the signal available for diversity-based selection---providing a mechanistic explanation for the alignment gap.\n\n\\paragraph{Representation quality metrics.}\nRankMe \\cite{garrido2023rankme} measures effective dimensionality of representations; $k$-NN probes assess local structure quality.\nWe show these metrics are \\emph{insensitive} to the alignment gap: RankMe increases during collapse, and $k$-NN accuracy remains stable, making them unreliable monitors for diversity degradation.\n\n%=============================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Iterative Self-Training Loop}\n\nWe define a generation-indexed training loop. Let $M_0$ be a pre-trained language model and $\\mathcal{D}_0$ the original training corpus.\nAt each generation $t$:\n\\begin{enumerate}\n\\item \\textbf{Generate}: Sample $N$ sequences from $M_{t-1}$ to form candidate pool $\\mathcal{G}_t$.\n\\item \\textbf{Select}: Apply a selection function $S(\\mathcal{G}_t) \\to \\mathcal{D}_t$ that selects a training subset.\n\\item \\textbf{Train}: Fine-tune $M_{t-1}$ on $\\mathcal{D}_t$ to obtain $M_t$.\n\\end{enumerate}\nWe compare three selection strategies:\n\\begin{itemize}\n\\item \\textbf{Uncurated}: $S = \\text{identity}$ (no selection; standard self-training baseline).\n\\item \\textbf{RGDS} (Representation-Guided Diversity Selection): Greedy submodular facility-location selection using $M_{t-1}$'s internal embeddings to maximize geometric diversity.\n\\item \\textbf{External-only}: Same submodular objective but using frozen Contriever \\cite{izacard2022contriever} embeddings instead of $M_{t-1}$'s representations.\n\\end{itemize}\n\n\\subsection{Selection Ratio: Quantifying the Alignment Gap}\n\nWe introduce the \\emph{selection ratio} as a diagnostic metric:\n\\begin{equation}\nr_t = \\frac{\\text{avg-rare}(S(\\mathcal{G}_t))}{\\text{avg-rare}(\\mathcal{G}_t)}\n\\end{equation}\nwhere $\\text{avg-rare}(\\cdot)$ computes mean rare $n$-gram frequency over a set.\nA well-calibrated diversity selector should satisfy $r_t \\geq 1$: the selected subset should be at least as lexically diverse as the full pool.\nThe alignment gap manifests as $r_t < 1$, indicating the selector systematically favors vocabulary-poor samples.\n\n\\subsection{Evaluation Metrics}\n\n\\begin{itemize}\n\\item \\textbf{Perplexity} (PPL): Evaluated on held-out test data from the original distribution.\n\\item \\textbf{Rare $n$-gram survival}: Fraction of $n$-grams in generated text that appear $\\leq 5$ times in the original corpus, measuring lexical diversity.\n\\item \\textbf{Rank correlation}: Spearman correlation between embedding-space diversity rank and rare $n$-gram rank across samples. Increasingly negative values indicate growing misalignment.\n\\item \\textbf{RankMe} \\cite{garrido2023rankme}: Effective rank of the embedding covariance matrix.\n\\item \\textbf{$k$-NN accuracy}: Leave-one-out $k$-NN classification accuracy in embedding space.\n\\end{itemize}\n\n%=============================================\n\\section{Main Results: The Alignment Gap}\n\\label{sec:main_results}\n\n\\subsection{Experimental Setup}\n\nWe use GPT-2 125M as the base model, fine-tuned on WikiText-103.\nThe self-training loop runs for 8 generations ($t = 0, \\ldots, 7$) with all three selection strategies.\nResults are averaged over 3 random seeds (42, 123, 456) with 95\\% confidence intervals.\n\n\\subsection{Selection Ratio Degradation (C1)}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Gen} & \\textbf{RGDS} & \\textbf{External} & \\textbf{Uncurated} \\\\\n\\midrule\n0 & 1.04 & 1.08 & --- \\\\\n1 & 0.96 & 1.12 & --- \\\\\n2 & 0.87 & 1.15 & --- \\\\\n3 & 0.79 & 1.18 & --- \\\\\n4 & 0.71 & 1.21 & --- \\\\\n5 & 0.64 & 1.24 & --- \\\\\n6 & 0.57 & 1.26 & --- \\\\\n7 & 0.52 & 1.28 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Selection ratio across generations (seed=42). RGDS ratio drops monotonically below 1.0, indicating the selector increasingly favors vocabulary-poor samples. External embeddings maintain ratio $>1.0$ throughout.}\n\\label{tab:sel_ratio}\n\\end{table}\n\nTable~\\ref{tab:sel_ratio} shows the selection ratio across 8 generations.\nRGDS begins near parity ($r_0 = 1.04$) but degrades monotonically to $r_7 = 0.52$---meaning the selected subset contains only half the rare $n$-gram density of the unselected pool.\nAcross 3 seeds, the gen-7 RGDS ratio averages $0.517$ (95\\% CI $[0.455, 0.579]$), with the confidence interval entirely below 1.0.\n\nThe rank correlation between embedding diversity scores and rare $n$-gram frequency (Table~\\ref{tab:main_full}) becomes increasingly negative ($-0.058 \\to -0.155$), confirming that the embedding space's notion of ``geometrically distant'' progressively aligns with vocabulary poverty rather than vocabulary richness.\n\n\\subsection{Accelerated Collapse (C3)}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{PPL}$\\downarrow$ & \\textbf{Rare}$\\uparrow$ & \\textbf{Rank Corr.} & \\textbf{Sel. Ratio} \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Generation 0}} \\\\\nUncurated & 37.1 & 0.0290 & $-$0.023 & --- \\\\\nRGDS & 37.2 & 0.0288 & $-$0.058 & 1.04 \\\\\nExternal & 36.8 & 0.0289 & $-$0.024 & 1.08 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Generation 7 (3-seed mean $\\pm$ std)}} \\\\\nUncurated & 48.3{\\scriptsize$\\pm$0.9} & .0088{\\scriptsize$\\pm$.0003} & $-$.087 & --- \\\\\nRGDS & 72.5{\\scriptsize$\\pm$1.9} & .0046{\\scriptsize$\\pm$.0004} & $-$.155 & 0.52{\\scriptsize$\\pm$.03} \\\\\nExternal & 45.7{\\scriptsize$\\pm$0.8} & .0088{\\scriptsize$\\pm$.0002} & $-$.037 & 1.28{\\scriptsize$\\pm$.03} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Core metrics at generations 0 and 7 (GPT-2 125M, WikiText-103). RGDS worsens both PPL (+50\\% vs uncurated) and rare $n$-gram survival ($-$47\\%). 3-seed 95\\% CIs for RGDS vs uncurated PPL do not overlap: $[67.9, 77.1]$ vs $[46.0, 50.6]$, $p < 0.01$.}\n\\label{tab:main_full}\n\\end{table}\n\nTable~\\ref{tab:main_full} summarizes the core finding.\nAt generation 7, RGDS produces PPL 72.5 vs.\\ uncurated 48.3 ($+50.2\\%$) and rare $n$-gram 0.0046 vs.\\ 0.0088 ($-47.1\\%$).\nThe 95\\% confidence intervals do not overlap (PPL: $[67.9, 77.1]$ vs.\\ $[46.0, 50.6]$; Cohen's $d > 3$).\nRGDS was designed to \\emph{prevent} collapse, but the alignment gap causes it to amplify the very failure mode it targets.\n\nThe causal chain is: (1) self-training contracts the embedding space; (2) greedy diversity selection in the contracted space picks points that are ``far'' in the degenerate geometry, which happen to be vocabulary-poor; (3) training on these impoverished subsets further contracts the embedding space, closing a positive feedback loop.\n\n\\subsection{Representation Metrics Miss the Collapse (S2)}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Gen} & \\textbf{PPL} & \\textbf{Rare} & \\textbf{RankMe} & \\textbf{$k$-NN} \\\\\n\\midrule\n0 & 37.2 & 0.0288 & 281.5 & 0.988 \\\\\n3 & 56.3 & 0.0113 & 300.1 & 0.988 \\\\\n7 & 72.8 & 0.0046 & 294.3 & 0.988 \\\\\n\\midrule\n$\\Delta$ & +96\\% & $-$84\\% & +5\\% & 0.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{RankMe and $k$-NN under RGDS collapse (seed=42). Despite catastrophic PPL and rare $n$-gram degradation, RankMe \\emph{increases} and $k$-NN is stable. These metrics track geometric structure, not content diversity.}\n\\label{tab:metrics_blind}\n\\end{table}\n\nTable~\\ref{tab:metrics_blind} reveals a cautionary finding: RankMe increases from 281.5 to 294.3 ($+5\\%$) during RGDS collapse, and $k$-NN accuracy remains at 0.988.\nThese metrics measure representation geometry---effective dimensionality and local neighborhood quality---but are blind to the misalignment between that geometry and downstream content diversity.\nPractitioners relying on such metrics to monitor iterative training would detect no anomaly even as diversity collapses.\n\n%=============================================\n\\section{External Embeddings and the PPL--Diversity Dissociation}\n\\label{sec:external}\n\nExternal-only selection using frozen Contriever embeddings maintains $r_t > 1.0$ across all generations (Table~\\ref{tab:sel_ratio}), rising to $1.28$ at gen 7 (95\\% CI $[1.21, 1.35]$).\nThis confirms the alignment gap is specific to embeddings under training feedback, not an inherent limitation of embedding-based selection.\n\nHowever, external selection reveals a striking dissociation (S1): it improves PPL relative to uncurated ($45.7$ vs.\\ $48.3$, $-5.4\\%$) while producing \\emph{identical} rare $n$-gram survival ($0.0088$ vs.\\ $0.0088$; CI fully overlapping: $[0.0083, 0.0093]$ vs.\\ $[0.0080, 0.0095]$).\nContriever captures topic-level and semantic-level diversity, which helps the model maintain broader coverage of test-set phenomena (lower PPL), but this semantic diversity does not translate into preservation of rare lexical patterns.\n\nThis dissociation implies that model collapse operates on at least two independent axes: \\emph{semantic} collapse (loss of topical coverage, reflected in PPL) and \\emph{lexical} collapse (loss of rare vocabulary patterns, reflected in rare $n$-gram survival).\nExternal embedding selection partially addresses the former but not the latter.\n\n%=============================================\n\\section{Mitigation: Embedding Re-Anchoring}\n\\label{sec:mitigation}\n\nThe alignment gap arises because the selector uses embeddings from $M_{t-1}$, which has been corrupted by prior self-training.\nA minimal fix: at each generation, compute diversity scores using the \\emph{original} pre-trained model $M_0$'s embeddings instead of $M_{t-1}$'s, while still training $M_{t-1} \\to M_t$ as usual.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{PPL}$\\downarrow$ & \\textbf{Rare}$\\uparrow$ & \\textbf{Sel. Ratio} \\\\\n\\midrule\nRGDS & 72.8 & 0.0046 & 0.52 \\\\\nRe-anchored RGDS & 51.2 & 0.0061 & 0.95 \\\\\nUncurated & 48.1 & 0.0087 & --- \\\\\nExternal-only & 45.8 & 0.0088 & 1.28 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Re-anchored vs.\\ RGDS improvement}} \\\\\n & $-$29.7\\% & +32.6\\% & +0.43 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Re-anchoring results (gen 7, GPT-2 125M, seed=42). Re-anchoring largely eliminates the selection ratio degradation ($0.52 \\to 0.95$) and recovers most of the PPL gap. Rare $n$-gram recovery is partial ($+33\\%$), localizing residual loss to the generation side.}\n\\label{tab:reanchor}\n\\end{table}\n\nTable~\\ref{tab:reanchor} shows that re-anchoring restores the selection ratio from 0.52 to 0.95 (near-parity), reduces PPL from 72.8 to 51.2 ($-29.7\\%$, close to uncurated's 48.1), and recovers rare $n$-gram survival from 0.0046 to 0.0061 ($+32.6\\%$).\n\nThe asymmetry between PPL recovery (near-complete) and rare $n$-gram recovery (partial) is informative.\nIt decomposes vocabulary collapse into two sources:\n\\begin{enumerate}\n\\item \\textbf{Selection-side}: The model's corrupted embeddings select vocabulary-poor subsets. Re-anchoring eliminates this component, recovering most PPL and $\\sim$1/3 of rare $n$-gram loss.\n\\item \\textbf{Generation-side}: The model itself progressively loses the ability to produce rare vocabulary, independent of what is selected. This accounts for the remaining $\\sim$2/3 of rare $n$-gram loss ($0.0061$ vs.\\ $0.0087$).\n\\end{enumerate}\n\nThis decomposition provides actionable direction: addressing model collapse fully requires generation-side interventions (e.g., vocabulary regularization, constrained decoding, or mixing in real data) in addition to selection-side fixes.\n\n%=============================================\n\\section{Robustness}\n\\label{sec:robustness}\n\n\\subsection{Multiple Seeds}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric (Gen 7)} & \\textbf{Mean} & \\textbf{Std} & \\textbf{95\\% CI} \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{RGDS}} \\\\\nPPL & 72.5 & 1.85 & [67.9, 77.1] \\\\\nSel.\\ ratio & 0.517 & 0.025 & [0.455, 0.579] \\\\\nRare $n$-gram & 0.0046 & 0.0004 & [0.0038, 0.0055] \\\\\nRank corr. & $-$0.155 & 0.007 & [$-$0.171, $-$0.139] \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Uncurated}} \\\\\nPPL & 48.3 & 0.91 & [46.0, 50.6] \\\\\nRare $n$-gram & 0.0088 & 0.0003 & [0.0080, 0.0095] \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{External-only}} \\\\\nPPL & 45.7 & 0.80 & [43.7, 47.7] \\\\\nSel.\\ ratio & 1.280 & 0.030 & [1.210, 1.350] \\\\\nRare $n$-gram & 0.0088 & 0.0002 & [0.0083, 0.0093] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Three-seed aggregated statistics (seeds 42, 123, 456; GPT-2 125M, WikiText-103). All key contrasts hold: RGDS ratio CI below 1.0; external ratio CI above 1.0; RGDS--uncurated PPL CIs non-overlapping.}\n\\label{tab:three_seed}\n\\end{table}\n\nTable~\\ref{tab:three_seed} reports 3-seed aggregated statistics.\nMethod-level differences (RGDS PPL $72.5$ vs.\\ uncurated $48.3$, $\\Delta = 24.2$) are an order of magnitude larger than seed-level variance (std $= 1.85$), yielding Cohen's $d > 3$.\nAll critical CIs are well-separated from threshold values.\n\n\\subsection{Model Scale: GPT-2 Medium (355M)}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Model} & \\textbf{Method} & \\textbf{PPL}$\\downarrow$ & \\textbf{Rare}$\\uparrow$ & \\textbf{Ratio} \\\\\n\\midrule\n\\multirow{3}{*}{125M} & Uncurated & 48.1 & 0.0087 & --- \\\\\n & RGDS & 72.8 & 0.0046 & 0.52 \\\\\n & External & 45.8 & 0.0088 & 1.28 \\\\\n\\midrule\n\\multirow{3}{*}{355M} & Uncurated & 41.8 & 0.0092 & --- \\\\\n & RGDS & 63.5 & 0.0052 & 0.56 \\\\\n & External & 38.8 & 0.0093 & 1.30 \\\\\n\\midrule\n\\multirow{3}{*}{355M$^\\dagger$} & Uncurated & 42.5 & 0.0089 & --- \\\\\n & RGDS & 65.1 & 0.0049 & 0.53 \\\\\n & External & 39.5 & 0.0091 & 1.27 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-scale comparison at gen 7 (WikiText-103). 355M results from seed=42 and $^\\dagger$seed=123. Relative magnitudes are consistent: RGDS PPL excess $+52\\%$ (125M) vs.\\ $+52\\%$ (355M); selection ratio endpoints $0.52$ vs.\\ $0.56$.}\n\\label{tab:scale}\n\\end{table}\n\nTable~\\ref{tab:scale} shows the alignment gap replicates on GPT-2 Medium (355M parameters).\nThe relative RGDS PPL excess over uncurated is $+51.9\\%$ (355M) vs.\\ $+51.4\\%$ (125M), and selection ratio endpoints are $0.56$ (355M) vs.\\ $0.52$ (125M).\nA second seed (123) on 355M confirms the trend with PPL excess $+53.2\\%$ and ratio $0.53$.\nThe mechanism's scale invariance is expected: the embedding alignment gap arises from training dynamics (embedding space contraction under self-iteration), not from model capacity per se.\n\n\\subsection{Dataset Generalization: OpenWebText}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Method} & \\textbf{PPL}$\\downarrow$ & \\textbf{Rare}$\\uparrow$ & \\textbf{Ratio} \\\\\n\\midrule\n\\multirow{3}{*}{Wiki} & Uncurated & 48.1 & 0.0087 & --- \\\\\n & RGDS & 72.8 & 0.0046 & 0.52 \\\\\n & External & 45.8 & 0.0088 & 1.28 \\\\\n\\midrule\n\\multirow{3}{*}{OWT} & Uncurated & 38.5 & 0.0095 & --- \\\\\n & RGDS & 59.1 & 0.0054 & 0.53 \\\\\n & External & 36.1 & 0.0096 & 1.29 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-dataset comparison at gen 7 (GPT-2 125M, seed=42). OpenWebText shows lower absolute PPL (GPT-2's pre-training domain) but identical alignment gap magnitudes: RGDS PPL excess $+54\\%$, rare deficit $-43\\%$.}\n\\label{tab:dataset}\n\\end{table}\n\nTable~\\ref{tab:dataset} shows the alignment gap generalizes to OpenWebText.\nDespite substantial differences in absolute baselines (OWT PPL 38.5 vs.\\ WikiText 48.1, owing to GPT-2's pre-training on WebText), relative alignment gap magnitudes are remarkably consistent: RGDS PPL excess $+53.5\\%$ (OWT) vs.\\ $+51.4\\%$ (WikiText); selection ratio $0.53$ (OWT) vs.\\ $0.52$ (WikiText).\nThe alignment gap is a property of the self-training dynamics, not of the data domain.\n\n%=============================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why does the alignment gap arise?}\nWe connect the mechanism to neural collapse \\cite{papyan2020prevalence}: iterative self-training reduces intra-distribution variability in the embedding space.\nAs the model ``memorizes'' its own output distribution, embeddings cluster along fewer effective directions.\nGreedy facility-location selection in this lower-dimensional space picks points that maximize geometric spread along the remaining directions---which, critically, are no longer aligned with lexical diversity.\nThe rank correlation evidence (Table~\\ref{tab:main_full}: $-0.058 \\to -0.155$) directly confirms this progressive misalignment.\n\n\\paragraph{Practical implications.}\nAny iterative training pipeline using the model's own representations for data selection is potentially vulnerable.\nThis includes retrieval-augmented self-improvement, iterative distillation with embedding-based filtering, and active learning with representation-space acquisition functions.\nOur results recommend either (a) using frozen external embeddings for selection, or (b) re-anchoring to pre-trained representations at each iteration.\n\n\\paragraph{Limitations.}\nOur experiments use GPT-2 family models (125M, 355M).\nWhile the alignment gap's relative magnitude is stable across these scales, verification on models $>1$B parameters remains future work.\nThe re-anchoring mitigation is simple by design; more sophisticated generation-side interventions may recover the remaining $\\sim$2/3 of vocabulary loss.\n\n%=============================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe identified the Embedding Alignment Gap: a systematic failure mode where diversity-based data selection using a model's own representations accelerates model collapse in iterative self-training.\nThe gap manifests as a monotonic degradation of the selection ratio from $1.04$ to $0.52$ over 8 generations, causing $+50\\%$ perplexity and $-47\\%$ rare $n$-gram loss relative to uncurated baselines.\nFrozen external embeddings are immune to the gap but reveal that semantic diversity does not ensure lexical diversity.\nA simple re-anchoring fix recovers $\\sim$30\\% of the gap, localizing the majority of residual collapse to the generation side.\nThese findings are robust across model scales, datasets, and random seeds.\nThe practical takeaway is clear: in iterative training, never trust the model's own embeddings for diversity-based data curation.\n\n\\bibliography{custom}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "7874b0f4-beca-4aa3-83c7-21e317f7c186",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260513T081019 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compou…",
  "leafUuid": "e473c86a-6f52-4e69-9006-d54f9763f2b9",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP paper on alignment gap and model collapse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3"
}
```

---

### Assistant

_source line 22 · 2026-05-13T08:36:36.485Z_

Now let me compile it. Since there's no .bib file, I need to handle bibliography. Let me create a minimal bib file and compile.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e473c86a-6f52-4e69-9006-d54f9763f2b9",
  "isSidechain": false,
  "requestId": "req_011CazGDcUm3gHTu5XnMYh82",
  "type": "assistant",
  "uuid": "4d87aab1-d627-4134-8c5d-d9deeb8e9ee2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019nj2DG3CAxVfczrByonbSp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8189,
      "cache_read_input_tokens": 40237,
      "output_tokens": 1163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1163,
          "cache_read_input_tokens": 40237,
          "cache_creation_input_tokens": 8189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8189
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

_source line 23 · 2026-05-13T08:36:55.734Z_

<details open><summary>🔧 Tool call — Write · `toolu_019aFMLx3eCr8BoumwQP6LWG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/custom.bib",
  "content": "@article{shumailov2024nature,\n  title={AI models collapse when trained on recursively generated data},\n  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  journal={Nature},\n  volume={631},\n  pages={755--759},\n  year={2024}\n}\n\n@article{alemohammad2024selfconsuming,\n  title={Self-consuming generative models go {MAD}},\n  author={Alemohammad, Sina and Casco-Rodriguez, Josue and Luber, Lorenzo and Babaei, Ahmed and Letizia, Daniel and Bastani, Osbert and Calmon, Flavio},\n  journal={arXiv preprint arXiv:2307.01850},\n  year={2024}\n}\n\n@article{dohmatob2024tale,\n  title={A tale of tails: Model collapse as a change of scaling laws},\n  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  journal={arXiv preprint arXiv:2402.07043},\n  year={2024}\n}\n\n@inproceedings{abbas2023semdedup,\n  title={{SemDeDup}: Data-efficient learning at web-scale through semantic deduplication},\n  author={Abbas, Amro and Tirumala, Kushal and Simig, D{\\'a}niel and Ganguli, Surya and Morcos, Ari},\n  booktitle={Proceedings of NeurIPS},\n  year={2023}\n}\n\n@article{tirumala2023d4,\n  title={D4: Improving {LLM} pretraining via document de-duplication and diversification},\n  author={Tirumala, Kushal and Markosyan, Aram and Zettlemoyer, Luke and Aghajanyan, Armen},\n  journal={arXiv preprint arXiv:2308.12284},\n  year={2023}\n}\n\n@inproceedings{xie2023dsir,\n  title={Data selection for language models via importance resampling},\n  author={Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  booktitle={Proceedings of NeurIPS},\n  year={2023}\n}\n\n@inproceedings{kirchhoff2014submodular,\n  title={Submodularity for data selection in machine translation},\n  author={Kirchhoff, Katrin and Bilmes, Jeff},\n  booktitle={Proceedings of EMNLP},\n  year={2014}\n}\n\n@inproceedings{papyan2020prevalence,\n  title={Prevalence of neural collapse during the terminal phase of deep learning training},\n  author={Papyan, Vardan and Han, X.Y. and Donoho, David L.},\n  booktitle={Proceedings of the National Academy of Sciences},\n  volume={117},\n  pages={24652--24663},\n  year={2020}\n}\n\n@article{garrido2023rankme,\n  title={{RankMe}: Assessing the downstream performance of pretrained self-supervised representations by their rank},\n  author={Garrido, Quentin and Balestriero, Randall and Najman, Laurent and LeCun, Yann},\n  journal={arXiv preprint arXiv:2210.02885},\n  year={2023}\n}\n\n@article{izacard2022contriever,\n  title={Unsupervised dense information retrieval with contrastive learning},\n  author={Izacard, Gautier and Caron, Mathilde and Hosseini, Lucas and Riedel, Sebastian and Bojanowski, Piotr and Joulin, Armand and Grave, Edouard},\n  journal={Transactions on Machine Learning Research},\n  year={2022}\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d87aab1-d627-4134-8c5d-d9deeb8e9ee2",
  "isSidechain": false,
  "requestId": "req_011CazGDcUm3gHTu5XnMYh82",
  "type": "assistant",
  "uuid": "4f72c5aa-9acc-4815-8f0a-77567269b361",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019nj2DG3CAxVfczrByonbSp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8189,
      "cache_read_input_tokens": 40237,
      "output_tokens": 1163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1163,
          "cache_read_input_tokens": 40237,
          "cache_creation_input_tokens": 8189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8189
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

_source line 24 · 2026-05-13T08:36:55.764Z_

<details><summary>↩ Tool result · `toolu_019aFMLx3eCr8BoumwQP6LWG`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/custom.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f72c5aa-9acc-4815-8f0a-77567269b361",
  "isSidechain": false,
  "promptId": "ad861b3f-869b-46c3-a458-a9928fad5b05",
  "type": "user",
  "uuid": "372345dd-a2b6-4923-aebd-7af5618fb068",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/custom.bib",
    "content": "@article{shumailov2024nature,\n  title={AI models collapse when trained on recursively generated data},\n  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  journal={Nature},\n  volume={631},\n  pages={755--759},\n  year={2024}\n}\n\n@article{alemohammad2024selfconsuming,\n  title={Self-consuming generative models go {MAD}},\n  author={Alemohammad, Sina and Casco-Rodriguez, Josue and Luber, Lorenzo and Babaei, Ahmed and Letizia, Daniel and Bastani, Osbert and Calmon, Flavio},\n  journal={arXiv preprint arXiv:2307.01850},\n  year={2024}\n}\n\n@article{dohmatob2024tale,\n  title={A tale of tails: Model collapse as a change of scaling laws},\n  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  journal={arXiv preprint arXiv:2402.07043},\n  year={2024}\n}\n\n@inproceedings{abbas2023semdedup,\n  title={{SemDeDup}: Data-efficient learning at web-scale through semantic deduplication},\n  author={Abbas, Amro and Tirumala, Kushal and Simig, D{\\'a}niel and Ganguli, Surya and Morcos, Ari},\n  booktitle={Proceedings of NeurIPS},\n  year={2023}\n}\n\n@article{tirumala2023d4,\n  title={D4: Improving {LLM} pretraining via document de-duplication and diversification},\n  author={Tirumala, Kushal and Markosyan, Aram and Zettlemoyer, Luke and Aghajanyan, Armen},\n  journal={arXiv preprint arXiv:2308.12284},\n  year={2023}\n}\n\n@inproceedings{xie2023dsir,\n  title={Data selection for language models via importance resampling},\n  author={Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  booktitle={Proceedings of NeurIPS},\n  year={2023}\n}\n\n@inproceedings{kirchhoff2014submodular,\n  title={Submodularity for data selection in machine translation},\n  author={Kirchhoff, Katrin and Bilmes, Jeff},\n  booktitle={Proceedings of EMNLP},\n  year={2014}\n}\n\n@inproceedings{papyan2020prevalence,\n  title={Prevalence of neural collapse during the terminal phase of deep learning training},\n  author={Papyan, Vardan and Han, X.Y. and Donoho, David L.},\n  booktitle={Proceedings of the National Academy of Sciences},\n  volume={117},\n  pages={24652--24663},\n  year={2020}\n}\n\n@article{garrido2023rankme,\n  title={{RankMe}: Assessing the downstream performance of pretrained self-supervised representations by their rank},\n  author={Garrido, Quentin and Balestriero, Randall and Najman, Laurent and LeCun, Yann},\n  journal={arXiv preprint arXiv:2210.02885},\n  year={2023}\n}\n\n@article{izacard2022contriever,\n  title={Unsupervised dense information retrieval with contrastive learning},\n  author={Izacard, Gautier and Caron, Mathilde and Hosseini, Lucas and Riedel, Sebastian and Bojanowski, Piotr and Joulin, Armand and Grave, Edouard},\n  journal={Transactions on Machine Learning Research},\n  year={2022}\n}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "4f72c5aa-9acc-4815-8f0a-77567269b361",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-13T08:37:07.232Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Y2iZhMgfiw9KrXtr77shmS`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/emnlp2023.sty 2>/dev/null && echo \"FOUND\" || echo \"NOT_FOUND\"",
  "description": "Check if EMNLP style file exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "372345dd-a2b6-4923-aebd-7af5618fb068",
  "isSidechain": false,
  "requestId": "req_011CazGFLEWw54qbqzkWAUAb",
  "type": "assistant",
  "uuid": "fb6757a7-3e26-4a3c-af51-c68c2a22e4d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NsNMzQ5KZAnCWWRzWF1ymk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1232,
      "cache_read_input_tokens": 48426,
      "output_tokens": 155,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1232,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 155,
          "cache_read_input_tokens": 48426,
          "cache_creation_input_tokens": 1232,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1232
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

_source line 26 · 2026-05-13T08:37:07.302Z_

<details><summary>↩ Tool result · `toolu_01Y2iZhMgfiw9KrXtr77shmS`</summary>

```text
NOT_FOUND
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb6757a7-3e26-4a3c-af51-c68c2a22e4d8",
  "isSidechain": false,
  "promptId": "ad861b3f-869b-46c3-a458-a9928fad5b05",
  "type": "user",
  "uuid": "e74df11d-6df1-4ba3-bf59-088c8c568240",
  "toolUseResult": {
    "stdout": "NOT_FOUND",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "fb6757a7-3e26-4a3c-af51-c68c2a22e4d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-13T08:37:11.055Z_

No EMNLP style file. I'll switch to a standard article class setup that compiles without external style files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e74df11d-6df1-4ba3-bf59-088c8c568240",
  "isSidechain": false,
  "requestId": "req_011CazGGBPj5jvrowsukJ7PK",
  "type": "assistant",
  "uuid": "745fa988-a6a0-4db0-86ea-74bba4d8e0a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQ5hhJUZUDyHAa9ZxaSiME",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 171,
      "cache_read_input_tokens": 49658,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 171,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 49658,
          "cache_creation_input_tokens": 171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 171
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

_source line 28 · 2026-05-13T08:37:11.745Z_

<details open><summary>🔧 Tool call — Read · `toolu_015wtNrpJnNSZwNTSMNjkdvs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/paper.tex",
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "745fa988-a6a0-4db0-86ea-74bba4d8e0a1",
  "isSidechain": false,
  "requestId": "req_011CazGGBPj5jvrowsukJ7PK",
  "type": "assistant",
  "uuid": "d94baf68-3897-41f0-8f7a-407803009757",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQ5hhJUZUDyHAa9ZxaSiME",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 171,
      "cache_read_input_tokens": 49658,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 171,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 49658,
          "cache_creation_input_tokens": 171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 171
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

_source line 29 · 2026-05-13T08:37:11.751Z_

<details><summary>↩ Tool result · `toolu_015wtNrpJnNSZwNTSMNjkdvs`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[hyperref]{emnlp2023}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d94baf68-3897-41f0-8f7a-407803009757",
  "isSidechain": false,
  "promptId": "ad861b3f-869b-46c3-a458-a9928fad5b05",
  "type": "user",
  "uuid": "10884cc8-0d67-45dc-a717-3da7cd76d986",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/paper.tex",
      "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}",
      "numLines": 5,
      "startLine": 1,
      "totalLines": 390
    }
  },
  "sourceToolAssistantUUID": "d94baf68-3897-41f0-8f7a-407803009757",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-13T08:37:11.810Z_

```json
{
  "parentUuid": "10884cc8-0d67-45dc-a717-3da7cd76d986",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "97eaf94a-fa19-4269-a4ec-0e525ed46a0c",
  "timestamp": "2026-05-13T08:37:11.810Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-13T08:37:18.886Z_

<details open><summary>🔧 Tool call — Edit · `toolu_013WXm4dhBn7rNT8BsH2MXiH`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/paper.tex",
  "old_string": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\title{The Embedding Alignment Gap: Why Diversity-Based Data Selection\\\\Accelerates Model Collapse in Iterative Self-Training}\n\n\\author{Anonymous}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{natbib}\n\\usepackage[colorlinks,citecolor=blue,urlcolor=blue]{hyperref}\n\n\\title{The Embedding Alignment Gap: Why Diversity-Based Data Selection\\\\Accelerates Model Collapse in Iterative Self-Training}\n\n\\author{Anonymous}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97eaf94a-fa19-4269-a4ec-0e525ed46a0c",
  "isSidechain": false,
  "requestId": "req_011CazGGWe7RMsRU4BbJqZaR",
  "type": "assistant",
  "uuid": "dbdf3baa-10ed-4d69-8384-bce316b31173",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U6TsaJK7n6QHP9TuaUgrQV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 326,
      "cache_read_input_tokens": 49829,
      "output_tokens": 475,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 326,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 475,
          "cache_read_input_tokens": 49829,
          "cache_creation_input_tokens": 326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 326
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

_source line 32 · 2026-05-13T08:37:18.905Z_

<details><summary>↩ Tool result · `toolu_013WXm4dhBn7rNT8BsH2MXiH`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dbdf3baa-10ed-4d69-8384-bce316b31173",
  "isSidechain": false,
  "promptId": "ad861b3f-869b-46c3-a458-a9928fad5b05",
  "type": "user",
  "uuid": "ba2e781d-aa3f-4b4f-9d04-a316d5199204",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/paper.tex",
    "oldString": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\title{The Embedding Alignment Gap: Why Diversity-Based Data Selection\\\\Accelerates Model Collapse in Iterative Self-Training}\n\n\\author{Anonymous}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{natbib}\n\\usepackage[colorlinks,citecolor=blue,urlcolor=blue]{hyperref}\n\n\\title{The Embedding Alignment Gap: Why Diversity-Based Data Selection\\\\Accelerates Model Collapse in Iterative Self-Training}\n\n\\author{Anonymous}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          "-\\documentclass[11pt]{article}",
          "-\\usepackage[hyperref]{emnlp2023}",
          "+\\documentclass[11pt,a4paper]{article}",
          "+\\usepackage[margin=1in]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{amsmath}"
        ]
      },
      {
        "oldStart": 9,
        "oldLines": 6,
        "newStart": 9,
        "newLines": 8,
        "lines": [
          " \\usepackage{multirow}",
          " \\usepackage{xcolor}",
          " \\usepackage{subcaption}",
          "+\\usepackage{natbib}",
          "+\\usepackage[colorlinks,citecolor=blue,urlcolor=blue]{hyperref}",
          " ",
          " \\title{The Embedding Alignment Gap: Why Diversity-Based Data Selection\\\\Accelerates Model Collapse in Iterative Self-Training}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "dbdf3baa-10ed-4d69-8384-bce316b31173",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-13T08:37:25.264Z_

Now I need to update the \cite commands to natbib-compatible \citep/\citet and fix the bibliography command.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba2e781d-aa3f-4b4f-9d04-a316d5199204",
  "isSidechain": false,
  "requestId": "req_011CazGH35wezYQqdAJnSHrV",
  "type": "assistant",
  "uuid": "38af8db9-31ce-49a2-81da-c9cb0434994f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M2qdUFqiVBHKjypbJ6ZXtf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 563,
      "cache_read_input_tokens": 50155,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 563,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 50155,
          "cache_creation_input_tokens": 563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 563
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-13T08:37:26.444Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01AWg3MSc9BZmS9hsbLcgd5j`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/paper.tex",
  "old_string": "\\bibliography{custom}",
  "new_string": "\\bibliographystyle{plainnat}\n\\bibliography{custom}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38af8db9-31ce-49a2-81da-c9cb0434994f",
  "isSidechain": false,
  "requestId": "req_011CazGH35wezYQqdAJnSHrV",
  "type": "assistant",
  "uuid": "66354c22-f2ba-4aca-9ca8-7839010fd5dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M2qdUFqiVBHKjypbJ6ZXtf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 563,
      "cache_read_input_tokens": 50155,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 563,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 50155,
          "cache_creation_input_tokens": 563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 563
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-13T08:37:26.461Z_

<details><summary>↩ Tool result · `toolu_01AWg3MSc9BZmS9hsbLcgd5j`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66354c22-f2ba-4aca-9ca8-7839010fd5dd",
  "isSidechain": false,
  "promptId": "ad861b3f-869b-46c3-a458-a9928fad5b05",
  "type": "user",
  "uuid": "71fc396a-b15a-4075-85e9-5731e933b149",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/paper.tex",
    "oldString": "\\bibliography{custom}",
    "newString": "\\bibliographystyle{plainnat}\n\\bibliography{custom}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 386,
        "oldLines": 6,
        "newStart": 386,
        "newLines": 7,
        "lines": [
          " These findings are robust across model scales, datasets, and random seeds.",
          " The practical takeaway is clear: in iterative training, never trust the model's own embeddings for diversity-based data curation.",
          " ",
          "+\\bibliographystyle{plainnat}",
          " \\bibliography{custom}",
          " ",
          " \\end{document}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "66354c22-f2ba-4aca-9ca8-7839010fd5dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-13T08:37:29.804Z_

Now compile with pdflatex + bibtex + pdflatex x2.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71fc396a-b15a-4075-85e9-5731e933b149",
  "isSidechain": false,
  "requestId": "req_011CazGHbNeY1mcLSyyJk8mn",
  "type": "assistant",
  "uuid": "0b845eb2-5526-4555-8de7-aa77bb8538e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017DdtuTo9j4YaUVRFKPSd2E",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 274,
      "cache_read_input_tokens": 50718,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 274,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 50718,
          "cache_creation_input_tokens": 274,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 274
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

_source line 37 · 2026-05-13T08:37:30.920Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011ZiQgSvXV59ph2ARXa6RKz`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "First pdflatex pass",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b845eb2-5526-4555-8de7-aa77bb8538e0",
  "isSidechain": false,
  "requestId": "req_011CazGHbNeY1mcLSyyJk8mn",
  "type": "assistant",
  "uuid": "c7f1b15c-1f4f-4171-a5c9-49fb0b3a94f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017DdtuTo9j4YaUVRFKPSd2E",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 274,
      "cache_read_input_tokens": 50718,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 274,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 50718,
          "cache_creation_input_tokens": 274,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 274
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

_source line 38 · 2026-05-13T08:37:31.608Z_

<details><summary>↩ Tool result · `toolu_011ZiQgSvXV59ph2ARXa6RKz`</summary>

```text
LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-
dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (8 pages, 139119 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7f1b15c-1f4f-4171-a5c9-49fb0b3a94f5",
  "isSidechain": false,
  "promptId": "ad861b3f-869b-46c3-a458-a9928fad5b05",
  "type": "user",
  "uuid": "7c6c133e-1d30-4e9f-9946-a8a20cfb6725",
  "toolUseResult": {
    "stdout": "LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-\ndist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (8 pages, 139119 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "c7f1b15c-1f4f-4171-a5c9-49fb0b3a94f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-13T08:37:35.904Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01X1ZHY7JBkShb5hBm3pfDgC`</summary>

```json
{
  "command": "bibtex paper 2>&1 | tail -10 && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5 && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "bibtex + two more pdflatex passes",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c6c133e-1d30-4e9f-9946-a8a20cfb6725",
  "isSidechain": false,
  "requestId": "req_011CazGHyHXBtxNRufxS8r8G",
  "type": "assistant",
  "uuid": "c027e5ff-5121-49fd-8efd-724af5aeccd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167oeyhp7thyVCxwqw4wR9e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 663,
      "cache_read_input_tokens": 50992,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 663,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 50992,
          "cache_creation_input_tokens": 663,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 663
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

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260513T081019 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compou…",
  "leafUuid": "c027e5ff-5121-49fd-8efd-724af5aeccd8",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP paper on alignment gap and model collapse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3"
}
```

---

### Tool result

_source line 42 · 2026-05-13T08:37:36.918Z_

<details><summary>↩ Tool result · `toolu_01X1ZHY7JBkShb5hBm3pfDgC`</summary>

```text
This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: paper.aux
The style file: plainnat.bst
Database file #1: custom.bib
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-
dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (8 pages, 146945 bytes).
Transcript written on paper.log.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-
dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (8 pages, 148647 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c027e5ff-5121-49fd-8efd-724af5aeccd8",
  "isSidechain": false,
  "promptId": "ad861b3f-869b-46c3-a458-a9928fad5b05",
  "type": "user",
  "uuid": "d95a1d3f-3254-4860-895f-7daccfd27dbf",
  "toolUseResult": {
    "stdout": "This is BibTeX, Version 0.99d (TeX Live 2025/Debian)\nThe top-level auxiliary file: paper.aux\nThe style file: plainnat.bst\nDatabase file #1: custom.bib\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-\ndist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (8 pages, 146945 bytes).\nTranscript written on paper.log.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-\ndist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (8 pages, 148647 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "c027e5ff-5121-49fd-8efd-724af5aeccd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-13T08:37:49.817Z_

编译成功，8 页 PDF 已生成。

`paper.pdf` 位于 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best/paper.pdf`（148 KB，8 页）。

论文结构：
- **Abstract**: 全部定量 claim 均引自 experiment_data.json
- **§1 Introduction**: 叙事弧——diversity selection 本意防崩塌，实则加速崩塌
- **§2 Related Work**: model collapse / data curation / neural collapse / representation metrics
- **§3 Method**: 三方法定义 + selection ratio 指标
- **§4 Main Results**: C1 (ratio 单调下降)、C3 (PPL +50%, rare -47%)、S2 (RankMe/k-NN 检测盲区)
- **§5 External Embeddings**: C2-weak + S1 (PPL-diversity 解耦)
- **§6 Mitigation**: re-anchoring，PPL -30%、rare +33%，分解 selection-side vs generation-side
- **§7 Robustness**: 3 seeds (Table 5)、GPT2-medium 355M (Table 6)、OpenWebText (Table 7)
- **§8 Conclusion**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d95a1d3f-3254-4860-895f-7daccfd27dbf",
  "isSidechain": false,
  "requestId": "req_011CazGJN2W24Uouw4JNxJQK",
  "type": "assistant",
  "uuid": "6d4a6e7e-2f5c-46ad-a083-f6ef9bf49715",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260513T081019/best",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDzqQq6H9FRjEsEz3zqd8h",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 488,
      "cache_read_input_tokens": 51655,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 488,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 365,
          "cache_read_input_tokens": 51655,
          "cache_creation_input_tokens": 488,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 488
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

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260513T081019 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/phase-gated-compou…",
  "leafUuid": "6d4a6e7e-2f5c-46ad-a083-f6ef9bf49715",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP paper on alignment gap and model collapse",
  "sessionId": "dbc865db-dd7a-482c-ac48-3666a2c55ae3"
}
```

---
