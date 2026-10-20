# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T150348 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/d2d6bb49-1e92-4164-91cd-dedff7777a4f.jsonl`
- **Structured JSON:** [`d7ffd7d987905df6dbce.json`](../../sessions/d7/d7ffd7d987905df6dbce.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T15:54:36.756Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T15:54:36.756Z",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T150348 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：切换到 Framing A：checkpoint selection criterion dominates mining strategy。\n主贡献重排：(1) 发现 checkpoint 选择标准对 reported performance 的影响（+10-16pp）远大于 mining strategy 差异（<1pp），\n揭示领域内 evaluation methodology 系统性问题；(2) 在此框架下，embedding mining 作为 controlled experiment 的一个 condition，\n在 Qwen 上有 marginal positive signal，但非 universal；(3) representation geometry 分析解释 why effect is encoder-dependent。\nBM25 neutral → 不能 claim CoCoHaNeRe 的 BM25 proxy 有害，改为 \"mining strategy choice matters less than evaluation methodology\"。\nStatistical framing：承认 3 seeds underpowered for <1pp effects，用 effect size + CI 报告而非 p-value。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T15:54:36.760Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T15:54:36.760Z",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f"
}
```

---

## Round 1

24 recorded events

### User

_source line 3 · 2026-05-16T15:54:36.783Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T150348 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：切换到 Framing A：checkpoint selection criterion dominates mining strategy。
主贡献重排：(1) 发现 checkpoint 选择标准对 reported performance 的影响（+10-16pp）远大于 mining strategy 差异（<1pp），
揭示领域内 evaluation methodology 系统性问题；(2) 在此框架下，embedding mining 作为 controlled experiment 的一个 condition，
在 Qwen 上有 marginal positive signal，但非 universal；(3) representation geometry 分析解释 why effect is encoder-dependent。
BM25 neutral → 不能 claim CoCoHaNeRe 的 BM25 proxy 有害，改为 "mining strategy choice matters less than evaluation methodology"。
Statistical framing：承认 3 seeds underpowered for <1pp effects，用 effect size + CI 报告而非 p-value。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "5b28b695-1a7e-43c8-ba53-d4ac70188a5b",
  "type": "user",
  "uuid": "6843d813-0c38-4329-93c1-a371b86fc780",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T15:54:36.782Z_

```json
{
  "parentUuid": "6843d813-0c38-4329-93c1-a371b86fc780",
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
  "uuid": "99772a08-5fd8-449f-8d34-a16a4a017d61",
  "timestamp": "2026-05-16T15:54:36.782Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T15:54:36.782Z_

```json
{
  "parentUuid": "99772a08-5fd8-449f-8d34-a16a4a017d61",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ba48cc3f-224f-4d2c-a60f-b870be207224",
  "timestamp": "2026-05-16T15:54:36.782Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f",
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
  "aiTitle": "Generate simulated research paper for dream session",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f"
}
```

---

### Assistant

_source line 7 · 2026-05-16T15:54:39.796Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the experiment data and paper framing files to understand what I need to write.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba48cc3f-224f-4d2c-a60f-b870be207224",
  "isSidechain": false,
  "requestId": "req_011Cb6X3tbsAc5UvtLPMhr2v",
  "type": "assistant",
  "uuid": "76f6b36a-847e-4561-9f5b-4bb885806c66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S4ceRsLuSu9RX8WKirUD3W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11258,
      "cache_read_input_tokens": 11841,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11258,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 225,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11258
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

_source line 8 · 2026-05-16T15:54:40.276Z_

<details open><summary>🔧 Tool call — Read · `toolu_0121u4xnqR8YM2aX9WqPibmB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76f6b36a-847e-4561-9f5b-4bb885806c66",
  "isSidechain": false,
  "requestId": "req_011Cb6X3tbsAc5UvtLPMhr2v",
  "type": "assistant",
  "uuid": "c37ac532-cf28-4556-a9e5-e885508d0029",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S4ceRsLuSu9RX8WKirUD3W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11258,
      "cache_read_input_tokens": 11841,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11258,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 225,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11258
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

_source line 9 · 2026-05-16T15:54:40.586Z_

<details><summary>↩ Tool result · `toolu_0121u4xnqR8YM2aX9WqPibmB`</summary>

```text
1	[
2	  {
3	    "name": "M2 Full Qwen 完整 9-run 最终结果",
4	    "description": "3 strategies × 3 seeds × Qwen2.5-Coder-3B 全量训练收敛后完整对比",
5	    "results": {
6	      "random_s42_R@1": 0.5527,
7	      "random_s43_R@1": 0.5554,
8	      "random_s44_R@1": 0.6009,
9	      "random_mean_R@1": 0.5697,
10	      "random_std_pp": 2.74,
11	      "embed_s42_R@1": 0.5613,
12	      "embed_s43_R@1": 0.5655,
13	      "embed_s44_R@1": 0.5942,
14	      "embed_mean_R@1": 0.5737,
15	      "embed_std_pp": 1.81,
16	      "dataflow_s42_R@1": 0.551,
17	      "dataflow_s43_R@1": 0.5564,
18	      "dataflow_s44_R@1": 0.572,
19	      "dataflow_mean_R@1": 0.5598,
20	      "dataflow_std_pp": 1.1,
21	      "embed_vs_random_mean_delta_pp": 0.4,
22	      "dataflow_vs_random_mean_delta_pp": -0.99,
23	      "embed_vs_random_95CI_pp": [
24	        -0.8,
25	        1.6
26	      ],
27	      "dataflow_vs_random_95CI_pp": [
28	        -2.2,
29	        0.2
30	      ],
31	      "cross_seed_std_random_pp": 2.74,
32	      "bootstrap_95ci_embed_excludes_zero": false
33	    },
34	    "tables": [
35	      {
36	        "name": "Table 1: Qwen2.5-Coder-3B R@1 (pool=8, best_by_R@1 checkpoint)",
37	        "columns": [
38	          "Strategy",
39	          "s42",
40	          "s43",
41	          "s44",
42	          "Mean",
43	          "Std",
44	          "Δ vs Random"
45	        ],
46	        "rows": [
47	          [
48	            "Random",
49	            0.5527,
50	            0.5554,
51	            0.6009,
52	            0.5697,
53	            0.0274,
54	            "—"
55	          ],
56	          [
57	            "Embedding",
58	            0.5613,
59	            0.5655,
60	            0.5942,
61	            0.5737,
62	            0.0181,
63	            "+0.40pp"
64	          ],
65	          [
66	            "Dataflow",
67	            0.551,
68	            0.5564,
69	            0.572,
70	            0.5598,
71	            0.011,
72	            "-0.99pp"
73	          ]
74	        ]
75	      }
76	    ],
77	    "figures": [],
78	    "analysis": "Embed 在 2/3 seeds 上有正 delta（s42: +0.86pp, s43: +1.01pp），但 s44 为 -0.67pp。\nMean delta +0.40pp 是 real signal 但 95% CI [-0.8, 1.6] 包含零。\nDataflow 整体不如 random，因为 66% 的 instance 实际拿到的是 random fallback negatives。\nCross-seed variance (2.74pp for random) >> strategy effect (0.4pp)，这是 paper pivot 到\nmethodology framing 的关键数据支撑。\n\n\ns44 random 异常高（0.6009 vs s42/s43 ~0.554）导致 random mean 被拉高，embed_s44 也高但不及 random_s44，\n使得 paired delta 在 s44 上为负（-0.67pp）。s42 和 s43 embed 各高 +0.86pp 和 +1.01pp。\n三个 seed 的 delta 方差大（std≈0.9pp），3 sample 的 95% CI 宽度约 2.4pp，下界包含零。\n这是 median 档核心特征：effect exists but underpowered detection。\nDataflow 因缺少结构数据的 instance（66% fallback to random）稀释了效果，mean slightly below random。\n"
79	  },
80	  {
81	    "name": "M2 Full StarCoder 完整 9-run 最终结果",
82	    "description": "3 strategies × 3 seeds × StarCoder2-3B 全量训练",
83	    "results": {
84	      "random_s42_R@1": 0.4604,
85	      "random_s43_R@1": 0.4859,
86	      "random_s44_R@1": 0.4897,
87	      "random_mean_R@1": 0.4787,
88	      "random_std_pp": 1.62,
89	      "embed_s42_R@1": 0.4567,
90	      "embed_s43_R@1": 0.487,
91	      "embed_s44_R@1": 0.4905,
92	      "embed_mean_R@1": 0.4781,
93	      "embed_std_pp": 1.85,
94	      "dataflow_s42_R@1": 0.449,
95	      "dataflow_s43_R@1": 0.478,
96	      "dataflow_s44_R@1": 0.483,
97	      "dataflow_mean_R@1": 0.47,
98	      "dataflow_std_pp": 1.88,
99	      "embed_vs_random_mean_delta_pp": -0.06,
100	      "dataflow_vs_random_mean_delta_pp": -0.87,
101	      "embed_vs_random_95CI_pp": [
102	        -1.4,
103	        1.3
104	      ],
105	      "bootstrap_95ci_embed_excludes_zero": false
106	    },
107	    "tables": [
108	      {
109	        "name": "Table 2: StarCoder2-3B R@1 (pool=8, best_by_R@1 checkpoint)",
110	        "columns": [
111	          "Strategy",
112	          "s42",
113	          "s43",
114	          "s44",
115	          "Mean",
116	          "Std",
117	          "Δ vs Random"
118	        ],
119	        "rows": [
120	          [
121	            "Random",
122	            0.4604,
123	            0.4859,
124	            0.4897,
125	            0.4787,
126	            0.0162,
127	            "—"
128	          ],
129	          [
130	            "Embedding",
131	            0.4567,
132	            0.487,
133	            0.4905,
134	            0.4781,
135	            0.0185,
136	            "-0.06pp"
137	          ],
138	          [
139	            "Dataflow",
140	            0.449,
141	            0.478,
142	            0.483,
143	            0.47,
144	            0.0188,
145	            "-0.87pp"
146	          ]
147	        ]
148	      }
149	    ],
150	    "figures": [],
151	    "analysis": "StarCoder 确认 embedding mining 无效。与 Qwen 的差异来自 representation geometry：\npos_sim=0.80 意味着 random negatives 已有足够 margin（0.194），embedding mining 的额外\ndifficulty 不产生 learning signal gain。这支持 \"effect is encoder-specific\" 论断。\n\n\nStarCoder embed_s42 已确认为负（0.4567 vs random 0.4604 = -0.37pp）。\ns43/s44 embed 会 track random closely（StarCoder 有 healthy geometry，pos_sim≈0.80，\nmargin 本身充足，embedding mining 提供的额外 difficulty gradient 不如 Qwen 有效）。\nMean delta 落在 -0.2 to +0.3pp 中间偏负。Dataflow 更弱因为 StarCoder embedding space\n对 structural signal 的敏感度更低（margin 本身大，dataflow negatives 没有提供足够的 incremental difficulty）。\n"
152	  },
153	  {
154	    "name": "BM25 Negative Baseline 训练",
155	    "description": "BM25-based hard negatives 作为第 4 策略，3 seeds × 2 encoders 训练对比",
156	    "results": {
157	      "qwen_bm25_s42_R@1": 0.554,
158	      "qwen_bm25_s43_R@1": 0.558,
159	      "qwen_bm25_s44_R@1": 0.598,
160	      "qwen_bm25_mean_R@1": 0.57,
161	      "qwen_bm25_vs_random_delta_pp": 0.03,
162	      "starcoder_bm25_s42_R@1": 0.458,
163	      "starcoder_bm25_s43_R@1": 0.483,
164	      "starcoder_bm25_s44_R@1": 0.487,
165	      "starcoder_bm25_mean_R@1": 0.476,
166	      "starcoder_bm25_vs_random_delta_pp": -0.27,
167	      "bm25_vs_random_pooled_delta_pp": [
168	        -0.5,
169	        0.5
170	      ],
171	      "bm25_vs_embedding_qwen_delta_pp": -0.37
172	    },
173	    "tables": [
174	      {
175	        "name": "Table 3: BM25 vs Other Strategies (R@1 pool=8)",
176	        "columns": [
177	          "Encoder",
178	          "Random",
179	          "BM25",
180	          "Embedding",
181	          "Dataflow"
182	        ],
183	        "rows": [
184	          [
185	            "Qwen",
186	            0.5697,
187	            0.57,
188	            0.5737,
189	            0.5598
190	          ],
191	          [
192	            "StarCoder",
193	            0.4787,
194	            0.476,
195	            0.4781,
196	            0.47
197	          ]
198	        ]
199	      }
200	    ],
201	    "figures": [],
202	    "analysis": "BM25 ≈ random 否定了原始 narrative（CoCoHaNeRe BM25 proxy harmful）。\nPaper 必须 pivot：不是 \"BM25 harms\" 而是 \"all strategies ≈ equivalent when checkpoint criterion dominates\"。\n这实际上 strengthens Framing A——如果连最 effortful 的 mining 都只有 <1pp 差异，\n那 checkpoint selection criterion (+10-16pp) 才是真正需要关注的 methodology gap。\n\n\nBM25 negatives 与 random 几乎无差异。原因：BM25 top-k 与 embedding top-k 有 87.1% overlap\n（已从 phase1 overlap analysis 确认），但 BM25 ranking ≠ embedding ranking，\n实际选中的 top-7 在 medium/large repo 上 Jaccard 仅 0.30-0.38。\nBM25 选出的 negatives 在 lexical space 中是 hard 的，但不一定在 encoder embedding space 中是 hard 的。\n对于 Qwen（saturated space），BM25 negatives 的 effective difficulty 介于 random 和 embedding 之间，\n但因为 Qwen space 几乎所有 pairs 都高相似度，BM25 的 lexical-hard 不等于 embedding-hard。\n对于 StarCoder（healthy space），BM25 和 random 都落在 \"sufficient margin\" 区间，无差异。\n关键结论：不能 claim CoCoHaNeRe 的 BM25 方法有害。Narrative pivot to \"strategy choice < methodology\"。\n"
203	  },
204	  {
205	    "name": "Pool Size Sensitivity Analysis",
206	    "description": "在 pool={8, 50, 100, 200, 500} 上评估策略排序稳定性",
207	    "results": {
208	      "qwen_embed_pool_8_R@1": 0.5737,
209	      "qwen_embed_pool_50_R@1": 0.432,
210	      "qwen_embed_pool_100_R@1": 0.365,
211	      "qwen_embed_pool_200_R@1": 0.288,
212	      "qwen_embed_pool_500_R@1": 0.195,
213	      "qwen_random_pool_8_R@1": 0.5697,
214	      "qwen_random_pool_50_R@1": 0.428,
215	      "qwen_random_pool_100_R@1": 0.361,
216	      "qwen_random_pool_200_R@1": 0.284,
217	      "qwen_random_pool_500_R@1": 0.191,
218	      "embed_vs_random_delta_pool_8_pp": 0.4,
219	      "embed_vs_random_delta_pool_50_pp": 0.4,
220	      "embed_vs_random_delta_pool_100_pp": 0.4,
221	      "embed_vs_random_delta_pool_200_pp": 0.4,
222	      "embed_vs_random_delta_pool_500_pp": 0.4,
223	      "criterion_effect_pool8_vs_pool50_pp": 14.2,
224	      "criterion_effect_pool8_vs_pool100_pp": 20.9,
225	      "strategy_ranking_preserved_across_pools": true
226	    },
227	    "tables": [
228	      {
229	        "name": "Table 4: R@1 by Pool Size (Qwen, embedding strategy, mean across seeds)",
230	        "columns": [
231	          "Pool",
232	          "R@1",
233	          "Δ vs pool=8"
234	        ],
235	        "rows": [
236	          [
237	            8,
238	            0.5737,
239	            "—"
240	          ],
241	          [
242	            50,
243	            0.432,
244	            "-14.2pp"
245	          ],
246	          [
247	            100,
248	            0.365,
249	            "-20.9pp"
250	          ],
251	          [
252	            200,
253	            0.288,
254	            "-28.6pp"
255	          ],
256	          [
257	            500,
258	            0.195,
259	            "-37.9pp"
260	          ]
261	        ]
262	      },
263	      {
264	        "name": "Table 5: Strategy Δ Stability Across Pool Sizes",
265	        "columns": [
266	          "Pool",
267	          "Embed-Random Δ",
268	          "Dataflow-Random Δ",
269	          "BM25-Random Δ"
270	        ],
271	        "rows": [
272	          [
273	            8,
274	            "+0.40pp",
275	            "-0.99pp",
276	            "+0.03pp"
277	          ],
278	          [
279	            50,
280	            "+0.38pp",
281	            "-1.05pp",
282	            "+0.05pp"
283	          ],
284	          [
285	            100,
286	            "+0.42pp",
287	            "-0.92pp",
288	            "-0.02pp"
289	          ],
290	          [
291	            200,
292	            "+0.39pp",
293	            "-1.01pp",
294	            "+0.08pp"
295	          ],
296	          [
297	            500,
298	            "+0.41pp",
299	            "-0.98pp",
300	            "+0.01pp"
301	          ]
302	        ]
303	      }
304	    ],
305	    "figures": [],
306	    "analysis": "Strategy ranking 在所有 pool size 下保持一致（embed > random > dataflow），但 delta < 1pp。\n绝对 R@1 随 pool 增大下降 ~14pp (pool 8→50)，这就是 \"criterion effect\" 的来源：\n如果用 pool=8 validation 选择 checkpoint，切换到 pool=50 test 时报告值 drop 10-16pp。\n更重要的是，pool=8 上的 \"best checkpoint\" 不一定是 pool=50 上的 best——\n不同 checkpoint 在不同 pool size 下的 ranking 会 shuffle。\n这是 paper 的核心方法论贡献，远比 <1pp 的 strategy delta 有实际意义。\n\n\nPool size 增大时 absolute R@1 急剧下降（从 pool=8 的 ~0.57 到 pool=50 的 ~0.43，drop 14pp），\n因为正确答案在更大 candidate pool 中更难排到第一。\n但 strategy delta 保持稳定（~0.4pp），因为 mining strategy 影响的是 encoder 的 relative ranking ability，\n与 pool size 无关。\n这是 paper 最强的 methodology insight：pool=8 validation 产生的 absolute R@1 数字\n在 pool=50 test 上 drop 10-16pp。如果研究者用 pool=8 选 checkpoint 再在 pool=50 报告，\n选中的 checkpoint 不一定是 pool=50 上最优的——这个 criterion mismatch 的 effect 远大于 strategy difference。\n具体而言：同一 checkpoint 在 pool=8 上 R@1=0.57 但在 pool=50 上只有 0.43，\n而另一个 checkpoint 可能 pool=8 上 R@1=0.55（被 criterion reject）但 pool=50 上 R@1=0.45（实际更好）。\n这个 +10-16pp criterion effect 就是 pool-size-driven checkpoint selection mismatch。\n"
307	  },
308	  {
309	    "name": "Checkpoint Selection Criterion Effect Analysis",
310	    "description": "直接量化：不同 checkpoint 选择标准对 reported R@1 的影响",
311	    "results": {
312	      "qwen_random_s42_best_by_valloss_R@1_pool50": 0.415,
313	      "qwen_random_s42_best_by_R@1_pool8_R@1_pool50": 0.428,
314	      "qwen_random_s42_best_by_R@1_pool50_R@1_pool50": 0.442,
315	      "criterion_gap_valloss_vs_R@1pool50_pp": 2.7,
316	      "criterion_gap_R@1pool8_vs_R@1pool50_pp": 1.4,
317	      "best_seed_best_criterion_R@1_pool50": 0.458,
318	      "worst_seed_worst_criterion_R@1_pool50": 0.398,
319	      "total_methodology_range_pp": 6.0,
320	      "strategy_effect_max_pp": 0.4,
321	      "methodology_vs_strategy_ratio": 15.0
322	    },
323	    "tables": [
324	      {
325	        "name": "Table 6: Methodology Confound Decomposition",
326	        "columns": [
327	          "Source",
328	          "Effect Size (pp)",
329	          "Controllable"
330	        ],
331	        "rows": [
332	          [
333	            "Pool size (8→50)",
334	            "14.2",
335	            "Yes — report on realistic pool"
336	          ],
337	          [
338	            "Checkpoint criterion (val_loss vs R@1)",
339	            "2.7",
340	            "Yes — use target metric"
341	          ],
342	          [
343	            "Seed variance",
344	            "2.7",
345	            "Partially — report mean±std"
346	          ],
347	          [
348	            "Mining strategy",
349	            "0.4",
350	            "Choice variable"
351	          ],
352	          [
353	            "Total methodology range",
354	            "10-16",
355	            "—"
356	          ]
357	        ]
358	      }
359	    ],
360	    "figures": [],
361	    "analysis": "这是 median 档 paper 的核心贡献。从 \"mining strategy matters\" 转向\n\"evaluation methodology dominates, mining strategy is noise\"。\n具体分解：pool size effect(14pp) > seed variance(2.7pp) > criterion(2.7pp) >> strategy(0.4pp)。\nPaper 的 prescriptive contribution：(1) 永远报告 pool=50+ 的 R@1；\n(2) 用目标 metric 选 checkpoint 而非 val_loss；(3) 报告 mean±CI 跨 seeds。\n\n\n在 pool=50 evaluation 上，checkpoint criterion 差异可达 2-3pp per run。\n跨 seed 时（best seed + best criterion vs worst seed + worst criterion），总 methodology range 达 6pp。\n如果进一步考虑 pool=8 training validation 与 pool=50 test 的 mismatch（14pp absolute drop），\n以及不同 epoch 的 checkpoint 在 pool=50 上的排序变化（best pool=8 ≠ best pool=50），\n整个 \"methodology confound\" 量级为 10-16pp（包含 pool effect + criterion selection + seed variance）。\n相比之下，strategy effect 最大 0.4pp。ratio = 15-40x。\n这就是 paper 最强贡献：researchers 应该先解决 methodology（pool size, criterion, seed aggregation），\n再讨论 mining strategy。\n"
362	  },
363	  {
364	    "name": "RepoBench-R Cross-file Retrieval Evaluation",
365	    "description": "RepoBench-R test_easy/test_hard 上 3 strategies × 3 seeds 评估",
366	    "results": {
367	      "qwen_random_easy_R@1_mean": 0.682,
368	      "qwen_embed_easy_R@1_mean": 0.687,
369	      "qwen_dataflow_easy_R@1_mean": 0.679,
370	      "embed_vs_random_easy_delta_pp": 0.5,
371	      "embed_vs_random_easy_95CI_pp": [
372	        -0.3,
373	        1.3
374	      ],
375	      "qwen_random_hard_R@1_mean": 0.415,
376	      "qwen_embed_hard_R@1_mean": 0.419,
377	      "qwen_dataflow_hard_R@1_mean": 0.411,
378	      "embed_vs_random_hard_delta_pp": 0.4,
379	      "embed_vs_random_hard_95CI_pp": [
380	        -0.5,
381	        1.3
382	      ],
383	      "starcoder_random_hard_R@1_mean": 0.358,
384	      "starcoder_embed_hard_R@1_mean": 0.357,
385	      "starcoder_embed_vs_random_hard_delta_pp": -0.1,
386	      "ci_overlap_easy": true,
387	      "ci_overlap_hard": true
388	    },
389	    "tables": [
390	      {
391	        "name": "Table 7: RepoBench-R Results (mean R@1 ± 95% CI)",
392	        "columns": [
393	          "Encoder",
394	          "Split",
395	          "Random",
396	          "Embedding",
397	          "Δ (CI)"
398	        ],
399	        "rows": [
400	          [
401	            "Qwen",
402	            "easy",
403	            "0.682",
404	            "0.687",
405	            "+0.5pp (-0.3, 1.3)"
406	          ],
407	          [
408	            "Qwen",
409	            "hard",
410	            "0.415",
411	            "0.419",
412	            "+0.4pp (-0.5, 1.3)"
413	          ],
414	          [
415	            "StarCoder",
416	            "easy",
417	            "0.612",
418	            "0.611",
419	            "-0.1pp (-0.9, 0.7)"
420	          ],
421	          [
422	            "StarCoder",
423	            "hard",
424	            "0.358",
425	            "0.357",
426	            "-0.1pp (-1.0, 0.8)"
427	          ]
428	        ]
429	      }
430	    ],
431	    "figures": [],
432	    "analysis": "RepoBench-R 作为 supplementary validation 支持 directional claim 但不提供 statistical significance。\n在 median 档的 methodology-first framing 下，这反而 reinforces 主论点：\n<1pp effects 即使 directionally consistent 也无法在 standard evaluation 中 reliably detect。\n\n\nRepoBench-R 是 cross-file retrieval task，与 SWE-smith 相比 domain shift 较小\n（同为 code retrieval 而非 repair），所以模型 transfer 好于 SWE-bench（OOD failure）。\nDirection 一致（Qwen embed > random）但效果量与 SWE-smith 内部评估一致（~0.4-0.5pp），\n95% CI 因为 bootstrap over 8K instances 虽然窄一些但仍包含零\n（因为 per-instance variance 大，且效果量太小）。\nStarCoder 同样 null，与 SWE-smith 结果一致。\nRepoBench-R 的主要价值是 \"directional consistency\" 而非 \"statistical confirmation\"。\n"
433	  },
434	  {
435	    "name": "Temperature Ablation Reduced",
436	    "description": "τ ∈ {0.05, 0.2} × random+embedding × Qwen × seed 42",
437	    "results": {
438	      "tau005_random_R@1": 0.535,
439	      "tau005_embed_R@1": 0.541,
440	      "tau005_embed_vs_random_pp": 0.6,
441	      "tau010_random_R@1": 0.5527,
442	      "tau010_embed_R@1": 0.5613,
443	      "tau010_embed_vs_random_pp": 0.86,
444	      "tau020_random_R@1": 0.568,
445	      "tau020_embed_R@1": 0.57,
446	      "tau020_embed_vs_random_pp": 0.2,
447	      "strategy_ranking_preserved": true,
448	      "delta_magnitude_varies": true,
449	      "tau005_vs_tau010_absolute_gap_pp": 1.77,
450	      "tau020_vs_tau010_absolute_gap_pp": 1.53
451	    },
452	    "tables": [
453	      {
454	        "name": "Table 8: Temperature × Strategy Interaction (Qwen, s42)",
455	        "columns": [
456	          "τ",
457	          "Random R@1",
458	          "Embed R@1",
459	          "Δ (pp)"
460	        ],
461	        "rows": [
462	          [
463	            0.05,
464	            0.535,
465	            0.541,
466	            "+0.60"
467	          ],
468	          [
469	            0.1,
470	            0.5527,
471	            0.5613,
472	            "+0.86"
473	          ],
474	          [
475	            0.2,
476	            0.568,
477	            0.57,
478	            "+0.20"
479	          ]
480	        ]
481	      }
482	    ],
483	    "figures": [],
484	    "analysis": "Embed advantage 在所有 τ 下存在但 magnitude 随 τ 变化。这 rules out \"effect is τ=0.1 artifact\"。\n同时也展示了 τ 是另一个 methodology confound（2pp range），再次支持 criterion-dominates framing。\n\n\nτ=0.05 使 loss landscape 更 sharp，对 hard negatives 更 sensitive——理论上应放大 mining effect。\n实际上 τ=0.05 更容易 overfit（已在 pilot 中观察到），absolute R@1 略低于 τ=0.10。\n但 embed-random delta 在 τ=0.05 下 slightly larger（0.6pp vs 0.86pp... 实际上更小）。\nτ=0.20 使 contrastive loss 更 smooth，random 和 embed 差异缩小（0.2pp），\n因为 softer temperature 减少了 hard negative 的 informative gradient signal。\n关键结论：strategy ranking 在所有 τ 下保持（embed ≥ random），但 effect magnitude 与 τ 相关。\n这意味着 mining effect 不是 regime-specific artifact，但其 practical significance 受 τ 调制。\n对 methodology framing：τ 选择（absolute R@1 vary ~2pp across τ）也是一个 methodology confound，\n量级仍 > strategy effect（0.2-0.9pp）。\n"
485	  },
486	  {
487	    "name": "Dynamic Embedding Mining Baseline",
488	    "description": "每 epoch 重新 mine embedding negatives vs 只用 pretrained（static）",
489	    "results": {
490	      "qwen_static_embed_R@1": 0.5613,
491	      "qwen_dynamic_embed_R@1": 0.564,
492	      "dynamic_vs_static_delta_pp": 0.27,
493	      "starcoder_static_embed_R@1": 0.4567,
494	      "starcoder_dynamic_embed_R@1": 0.459,
495	      "dynamic_vs_static_sc_delta_pp": 0.23,
496	      "dynamic_overhead_factor": 3.2
497	    },
498	    "tables": [
499	      {
500	        "name": "Table 9: Static vs Dynamic Mining",
501	        "columns": [
502	          "Encoder",
503	          "Static",
504	          "Dynamic",
505	          "Δ (pp)",
506	          "Time multiplier"
507	        ],
508	        "rows": [
509	          [
510	            "Qwen",
511	            0.5613,
512	            0.564,
513	            "+0.27",
514	            "3.2x"
515	          ],
516	          [
517	            "StarCoder",
518	            0.4567,
519	            0.459,
520	            "+0.23",
521	            "3.2x"
522	          ]
523	        ]
524	      }
525	    ],
526	    "figures": [],
527	    "analysis": "Dynamic mining 仅提供 ~0.25pp marginal gain over static，且 computational cost 3.2x。\nThis validates that static mining is a fair comparison point（reviewer concern addressed）。\nAlso supports narrative：even \"better\" mining only adds 0.25pp → methodology still dominates。\n\n\nDynamic mining 理论上应 better 因为 negatives adapt to evolving encoder。\n但实际提升微小（~0.2-0.3pp）因为：(1) LoRA 只 fine-tune adapter，base embedding 变化小；\n(2) 3 epochs 太短，encoder drift 有限；(3) Qwen saturated space 意味着 re-mining 后\ntop-k negatives 几乎不变（cos sim 都在 0.96+ 区间，ranking 高度稳定）。\n训练时间 3.2x（每 epoch 需要重新 encode 全 corpus + mine），ROI 极低。\n结论：static mining 是合理 baseline，dynamic 不是 confound。\n"
528	  },
529	  {
530	    "name": "UniXcoder Multi-seed Validation",
531	    "description": "UniXcoder-base 125M 上 3 strategies × 3 seeds 统计验证",
532	    "results": {
533	      "unixcoder_random_s42_R@1": 0.5534,
534	      "unixcoder_embed_s42_R@1": 0.5497,
535	      "unixcoder_dataflow_s42_R@1": 0.551,
536	      "unixcoder_random_s43_R@1": 0.577,
537	      "unixcoder_embed_s43_R@1": 0.574,
538	      "unixcoder_dataflow_s43_R@1": 0.5755,
539	      "unixcoder_random_s44_R@1": 0.562,
540	      "unixcoder_embed_s44_R@1": 0.559,
541	      "unixcoder_dataflow_s44_R@1": 0.56,
542	      "unixcoder_random_mean_R@1": 0.5641,
543	      "unixcoder_embed_mean_R@1": 0.5609,
544	      "unixcoder_dataflow_mean_R@1": 0.5622,
545	      "embed_vs_random_mean_pp": -0.32,
546	      "dataflow_vs_random_mean_pp": -0.19,
547	      "all_within_noise": true,
548	      "max_span_across_strategies_pp": 0.37
549	    },
550	    "tables": [
551	      {
552	        "name": "Table 10: UniXcoder-base Results (complete null)",
553	        "columns": [
554	          "Seed",
555	          "Random",
556	          "Embed",
557	          "Dataflow",
558	          "Max Span"
559	        ],
560	        "rows": [
561	          [
562	            42,
563	            0.5534,
564	            0.5497,
565	            0.551,
566	            "0.37pp"
567	          ],
568	          [
569	            43,
570	            0.577,
571	            0.574,
572	            0.5755,
573	            "0.30pp"
574	          ],
575	          [
576	            44,
577	            0.562,
578	            0.559,
579	            0.56,
580	            "0.30pp"
581	          ],
582	          [
583	            "Mean",
584	            0.5641,
585	            0.5609,
586	            0.5622,
587	            "0.32pp"
588	          ]
589	        ]
590	      }
591	    ],
592	    "figures": [],
593	    "analysis": "UniXcoder null + StarCoder weak = 'effect is encoder-specific, not universal'。\n在 methodology-first framing 下，这反而 strengthens 论文：即使最 favorable 的条件\n（Qwen saturated geometry）也只有 <1pp effect，其他 architecture 完全 null。\nMining strategy choice 在 typical evaluation 中完全不 matter。\n\n\nUniXcoder s42 已确认 null result（0.37pp span across all strategies）。\nMulti-seed 会重复这个 pattern：UniXcoder 作为 encoder-only 125M model，\n其 representation 是 mean-pooled 而非 last-token，embedding space 结构与 decoder-only 不同。\nMining strategy 对 encoder-only architecture 完全无效的原因：\n(1) 125M params 的 adapter 容量有限，hard negatives 的额外 gradient 无法被 absorbed；\n(2) encoder-only mean-pooling 产生的 similarity distribution 不同于 decoder last-token，\nmining 不 align with the model's actual difficulty gradient。\n这个 null result 在 paper 中不再是 limitation 而是 positive evidence：\n\"effect is encoder-specific, confirming geometry hypothesis\"。\n"
594	  },
595	  {
596	    "name": "Stratified Analysis by Structural Data Availability",
597	    "description": "5 strata 分析：repo size, pool size, query-pos similarity, structural data availability, neg_difficulty quartile",
598	    "results": {
599	      "rich_dataflow_embed_vs_random_delta_pp": 0.55,
600	      "fallback_embed_vs_random_delta_pp": 0.3,
601	      "rich_dataflow_99pct_in_large_repos": true,
602	      "cannot_isolate_dataflow_from_repo_size": true,
603	      "small_pool_lt20_delta_pp": 0.6,
604	      "large_pool_gt100_delta_pp": 0.35,
605	      "q1_low_difficulty_delta_pp": 0.15,
606	      "q4_high_difficulty_delta_pp": 0.7,
607	      "difficulty_gradient_predicts_benefit": true,
608	      "but_all_effects_within_ci_noise": true
609	    },
610	    "tables": [
611	      {
612	        "name": "Table 11: Stratified embed-random Δ (Qwen, all seeds pooled)",
613	        "columns": [
614	          "Stratum",
615	          "N",
616	          "Δ (pp)",
617	          "95% CI"
618	        ],
619	        "rows": [
620	          [
621	            "Rich dataflow (34%)",
622	            "~4800",
623	            "+0.55",
624	            "(-0.4, 1.5)"
625	          ],
626	          [
627	            "Fallback (66%)",
628	            "~9300",
629	            "+0.30",
630	            "(-0.5, 1.1)"
631	          ],
632	          [
633	            "Small repo (<50 files)",
634	            "~500",
635	            "+0.80",
636	            "(-1.5, 3.1)"
637	          ],
638	          [
639	            "Large repo (200+ files)",
640	            "~8600",
641	            "+0.35",
642	            "(-0.5, 1.2)"
643	          ],
644	          [
645	            "neg_difficulty Q1 (easy)",
646	            "~3500",
647	            "+0.15",
648	            "(-0.8, 1.1)"
649	          ],
650	          [
651	            "neg_difficulty Q4 (hard)",
652	            "~3500",
653	            "+0.70",
654	            "(-0.3, 1.7)"
655	          ]
656	        ]
657	      }
658	    ],
659	    "figures": [],
660	    "analysis": "Stratified analysis 提供 mechanistic depth 但无 statistical power。\n在 median 档 framing 中作为 \"exploratory evidence for geometry hypothesis\"。\n关键 insight：confound between repo_size 和 dataflow_richness 意味着\n不能单独 attribute benefit to structural information。\n\n\nStratified analysis 会显示 directional patterns：\n(1) Rich-dataflow instances（34%）show slightly larger embed benefit because these instances \n    tend to be in complex repos where random negatives are worse-quality；\n(2) 但 99.3% rich-dataflow 在 large/xlarge repos，无法解耦 dataflow richness 和 repo complexity；\n(3) neg_difficulty quartile 最有解释力：high-difficulty negatives（Q4）对应更大的 embed benefit，\n    因为 embed mining 选出的 negatives 比 random 更接近 difficulty optimal zone；\n(4) 所有 strata 的 effect 都在 noise floor 内（CI 包含 zero）。\n这支持 geometry hypothesis 但不能作为 statistical evidence。\n"
661	  },
662	  {
663	    "name": "1-hop vs 2-hop vs 3-hop Call-graph Bounding",
664	    "description": "CodeQL 提取时 data-flow scope 对 connected set 大小和 downstream training 的影响",
665	    "results": {
666	      "hop1_connected_mean_files": 3.2,
667	      "hop2_connected_mean_files": 8.7,
668	      "hop3_connected_mean_files": 18.4,
669	      "hop1_Z_pct": 0.52,
670	      "hop2_Z_pct": 0.78,
671	      "hop3_Z_pct": 0.89,
672	      "hop1_dataflow_R@1": 0.548,
673	      "hop2_dataflow_R@1": 0.551,
674	      "hop3_dataflow_R@1": 0.549,
675	      "hop_effect_range_pp": 0.3
676	    },
677	    "tables": [
678	      {
679	        "name": "Table 12: Hop Depth Ablation",
680	        "columns": [
681	          "Hops",
682	          "Mean connected files",
683	          "Z%",
684	          "Dataflow R@1"
685	        ],
686	        "rows": [
687	          [
688	            1,
689	            3.2,
690	            "52%",
691	            0.548
692	          ],
693	          [
694	            2,
695	            8.7,
696	            "78%",
697	            0.551
698	          ],
699	          [
700	            3,
701	            18.4,
702	            "89%",
703	            0.549
704	          ]
705	        ]
706	      }
707	    ],
708	    "figures": [],
709	    "analysis": "2-hop 是合理 default（coverage/noise trade-off），但 choice of hop depth\n对 downstream training 几乎无影响。又一个 methodology variant (hop depth) \nwhose effect << criterion effect。\n\n\n增加 hop 数扩大 connected set（从 3.2 到 18.4 mean files），增加 Z%，\n但 downstream training 差异极小（0.3pp range）。原因：\n(1) Dataflow strategy 本身效果已经 ≈ random（median 档 dataflow-random ≈ -1pp），\n    所以 connected set 的精确度差异被掩盖；\n(2) 更多 hops 包含更多 spurious connections（transitive dependencies 不等于 semantic relatedness），\n    noise 抵消了 coverage gain；\n(3) 在 2-hop（当前设置）下 Z%=78% 已经 adequate——大部分 true positives 已被 captured。\n"
710	  },
711	  {
712	    "name": "Training Data Size Scaling",
713	    "description": "1K vs 3K vs 5K vs 11K+ instances 的 scaling 行为",
714	    "results": {
715	      "size_1K_R@1": 0.505,
716	      "size_3K_R@1": 0.531,
717	      "size_5K_R@1": 0.543,
718	      "size_11K_R@1": 0.5527,
719	      "size_1K_embed_delta_pp": 1.2,
720	      "size_3K_embed_delta_pp": 0.8,
721	      "size_5K_embed_delta_pp": 0.55,
722	      "size_11K_embed_delta_pp": 0.86,
723	      "random_scaling_log_slope": 0.023,
724	      "effect_diminishes_with_data": true
725	    },
726	    "tables": [
727	      {
728	        "name": "Table 13: Data Size Scaling",
729	        "columns": [
730	          "Size",
731	          "Random R@1",
732	          "Embed R@1",
733	          "Δ (pp)"
734	        ],
735	        "rows": [
736	          [
737	            "1K",
738	            0.505,
739	            0.517,
740	            "+1.20"
741	          ],
742	          [
743	            "3K",
744	            0.531,
745	            0.539,
746	            "+0.80"
747	          ],
748	          [
749	            "5K",
750	            0.543,
751	            0.548,
752	            "+0.55"
753	          ],
754	          [
755	            "11K",
756	            0.553,
757	            0.561,
758	            "+0.86"
759	          ]
760	        ]
761	      }
762	    ],
763	    "figures": [],
764	    "analysis": "Data size effect (5pp) >> strategy effect (<1pp)。Mining advantage diminishes with more data，\nsuggesting that at even larger scale the effect may vanish entirely。\n11K 的 delta 略回弹（0.86 > 0.55 at 5K）可能是 noise 或 composition effect（\n更多 instances 中包含更多 hard cases where mining helps）。\n\n\n更多数据提升 absolute performance（log-linear scaling），但同时 diminishes mining advantage。\n原因：larger random corpus 本身 covers 更多 hard negatives by chance，\nreducing the marginal value of targeted mining。\nAt 1K，random sampling 的 coverage 差，mining 的相对优势大（+1.2pp）；\nat 11K，random 已经 sample 了 enough hard examples that mining only adds +0.86pp。\n这解释了为何 full-scale effect < pilot effect（pilot 用较小数据集）。\n在 methodology framing 中：data size（5pp range from 1K→11K）是又一个 >> strategy effect 的 factor。\n"
765	  },
766	  {
767	    "name": "Bootstrap 95% CI for All Claims",
768	    "description": "对 SWE-smith validation 上的 strategy comparisons 做 bootstrap CI（SWE-bench 已放弃）",
769	    "results": {
770	      "qwen_embed_vs_random_bootstrap_mean_pp": 0.4,
771	      "qwen_embed_vs_random_bootstrap_95CI_pp": [
772	        -0.82,
773	        1.62
774	      ],
775	      "qwen_embed_vs_random_p_value": 0.26,
776	      "ci_excludes_zero": false,
777	      "qwen_dataflow_vs_random_bootstrap_mean_pp": -0.99,
778	      "qwen_dataflow_vs_random_bootstrap_95CI_pp": [
779	        -2.45,
780	        0.47
781	      ],
782	      "starcoder_embed_vs_random_bootstrap_mean_pp": -0.06,
783	      "starcoder_embed_vs_random_bootstrap_95CI_pp": [
784	        -1.52,
785	        1.4
786	      ],
787	      "bm25_vs_random_bootstrap_mean_pp": -0.12,
788	      "bm25_vs_random_bootstrap_95CI_pp": [
789	        -1.2,
790	        0.96
791	      ],
792	      "qwen_embed_cohens_d": 0.18,
793	      "starcoder_embed_cohens_d": 0.03,
794	      "power_analysis_required_seeds_for_05pp": 12
795	    },
796	    "tables": [
797	      {
798	        "name": "Table 14: Statistical Summary (all comparisons)",
799	        "columns": [
800	          "Comparison",
801	          "Mean Δ (pp)",
802	          "95% CI",
803	          "Cohen's d",
804	          "p-value"
805	        ],
806	        "rows": [
807	          [
808	            "Qwen Embed-Random",
809	            "+0.40",
810	            "(-0.82, 1.62)",
811	            "0.18",
812	            "0.26"
813	          ],
814	          [
815	            "Qwen Dataflow-Random",
816	            "-0.99",
817	            "(-2.45, 0.47)",
818	            "0.42",
819	            "0.12"
820	          ],
821	          [
822	            "StarCoder Embed-Random",
823	            "-0.06",
824	            "(-1.52, 1.40)",
825	            "0.03",
826	            "0.94"
827	          ],
828	          [
829	            "BM25-Random (pooled)",
830	            "-0.12",
831	            "(-1.20, 0.96)",
832	            "0.05",
833	            "0.82"
834	          ]
835	        ]
836	      }
837	    ],
838	    "figures": [],
839	    "analysis": "所有 CI 都包含零。这不意味着 effect 不存在，而是 3 seeds 对 <1pp effects 统计力度不足。\nPaper 的 honest framing：report effect sizes + CIs，承认 underpowered，\nargue that the FINDING is \"methodology matters more\" not \"mining helps\"。\n\n\nWith only 3 seeds per condition, 95% CI is approximately mean ± t(0.025, df=2) × SE。\nFor cross_seed_std = 2.7pp and n=3：SE = 2.7/√3 = 1.56pp, t(0.025,2)=4.3 → CI = ±6.7pp... \n这太宽了。实际上 bootstrap CI 用的是 paired delta（each seed 的 embed - random），\npaired delta std 更小（~1.0pp因为 seeds co-vary）。\nPaired delta: s42=+0.86, s43=+1.01, s44=-0.67 → mean=0.40, std=0.93, SE=0.54。\n95% CI (bootstrap percentile) ≈ [-0.82, 1.62]，包含零。\nCohen's d = 0.40/2.2 = 0.18（small effect）。\nPower analysis：要 detect 0.5pp effect with 80% power at α=0.05，需要 ~12 seeds。\n3 seeds 的 statistical power 对 <1pp effect 约为 15-20%，underpowered。\n"
840	  },
841	  {
842	    "name": "Fusion Head Ablation",
843	    "description": "embedding-only vs structural-features-only vs combined retrieval",
844	    "results": {
845	      "embedding_only_R@1": 0.5613,
846	      "structural_only_R@1": 0.32,
847	      "combined_R@1": 0.565,
848	      "combined_vs_embed_delta_pp": 0.37
849	    },
850	    "tables": [
851	      {
852	        "name": "Table 15: Fusion Head Ablation",
853	        "columns": [
854	          "Method",
855	          "R@1",
856	          "Coverage"
857	        ],
858	        "rows": [
859	          [
860	            "Embedding only",
861	            0.5613,
862	            "100%"
863	          ],
864	          [
865	            "Structural only",
866	            0.32,
867	            "34% effective"
868	          ],
869	          [
870	            "Combined",
871	            0.565,
872	            "100%"
873	          ]
874	        ]
875	      }
876	    ],
877	    "figures": [],
878	    "analysis": "Structural signal alone insufficient due to coverage gap。\nCombined 仅 marginal gain，reinforcing that embedding-based retrieval\ncaptures most of what structural information provides。\n\n\nStructural features alone（graph-based without neural embedding）表现差\n因为 coverage 只有 34%（66% instances 无 structural data → random guess）。\nCombined（embedding + structural re-rank）marginal gain over embedding-only（+0.37pp）\n因为 structural signal 只在 34% instances 上有效，且其信号与 embedding 高度相关\n（connected files 通常也是 embedding-similar files，overlap 87%）。\n这进一步支持 \"mining strategy 差异小\" 的 narrative。\n"
879	  },
880	  {
881	    "name": "Dataflow-distance Weighted Negatives",
882	    "description": "按 dataflow distance 连续加权 vs 二值 connected/disconnected",
883	    "results": {
884	      "binary_dataflow_R@1": 0.551,
885	      "weighted_dataflow_R@1": 0.553,
886	      "weighted_vs_binary_delta_pp": 0.2
887	    },
888	    "tables": [],
889	    "figures": [],
890	    "analysis": "Minimal improvement over binary。Further confirms that structural signal\nis coarse-grained (connected vs not) rather than fine-grained (distance-weighted).\n\n\nConnected/disconnected 二值划分已经 capture 了 structural signal 的主要信息量。\n连续权重（distance = 1 vs 2 vs 3 hops）只提供 marginal refinement（+0.2pp），\n因为 (1) distance distribution 本身 noisy（CodeQL 的 hop count 不是 clean metric），\n(2) 二值判断（is_connected）在 linear proxy 中已是 top feature (+2.82 coefficient），\ngraded distance 的 incremental information content 有限。\n"
891	  },
892	  {
893	    "name": "Failure Analysis on SWE-bench Failures",
894	    "description": "50 BM25 baseline failures 分类分析",
895	    "results": {
896	      "total_analyzed": 50,
897	      "category_cross_repo_import": 12,
898	      "category_test_only_change": 15,
899	      "category_distant_dependency": 8,
900	      "category_config_files": 7,
901	      "category_other": 8,
902	      "dataflow_could_help_pct": 16,
903	      "dataflow_irrelevant_pct": 72,
904	      "dataflow_would_hurt_pct": 12
905	    },
906	    "tables": [
907	      {
908	        "name": "Table 16: Failure Case Taxonomy",
909	        "columns": [
910	          "Category",
911	          "Count",
912	          "Dataflow relevance"
913	        ],
914	        "rows": [
915	          [
916	            "Test-only changes",
917	            15,
918	            "Irrelevant"
919	          ],
920	          [
921	            "Cross-repo import",
922	            12,
923	            "Irrelevant"
924	          ],
925	          [
926	            "Distant dependency",
927	            8,
928	            "Could help"
929	          ],
930	          [
931	            "Config/build files",
932	            7,
933	            "Irrelevant"
934	          ],
935	          [
936	            "Other",
937	            8,
938	            "Mixed"
939	          ]
940	        ]
941	      }
942	    ],
943	    "figures": [],
944	    "analysis": "SWE-bench failure is OOD generalization problem, not mining strategy problem。\nConfirms paper should not mention SWE-bench。RepoBench-R is better external validation。\n\n\nSWE-bench 的 R@1=0.04 failure 主要来自 OOD 问题（不同 repo 分布），\n而非 mining strategy 不足。分析 50 个 BM25 failure case：\n大多数是 test file changes（30%）和 cross-repo import patterns（24%）——\n这些情况下 dataflow mining 无法帮助，因为 (1) test files 通常不在 dataflow graph 中，\n(2) SWE-bench 的 repo 不在训练集中。\n只有 ~16% cases 理论上 dataflow 可以帮助（distant dependency chains）。\n这 reinforces director decision to drop SWE-bench from paper。\n"
945	  },
946	  {
947	    "name": "Qualitative Retrieval Examples",
948	    "description": "5-10 cases where embedding mining changed retrieval outcome vs random",
949	    "results": {
950	      "total_diff_cases_found": 23,
951	      "selected_for_paper": 5,
952	      "pattern_A_embed_promotes_import_chain": 2,
953	      "pattern_B_embed_demotes_unrelated_similar": 2,
954	      "pattern_C_marginal_reranking": 1,
955	      "avg_rank_change_in_selected": 3.2
956	    },
957	    "tables": [],
958	    "figures": [],
959	    "analysis": "Qualitative examples 提供 intuition 但数量少（only 1.6% instances affected）。\n在 paper 中作为 \"illustrative\" 而非 \"representative\"。\n\n\n由于 overall delta 只有 ~0.4pp (pool=8)，找到 embed mining 改变 R@1 outcome 的\ncases 需要 search relatively large eval set。在 ~1400 instances 中，\n约 23 cases 的 top-1 因 strategy 不同而变化（1.6% cases）。\n选出的 5 cases 展示 3 个 pattern：\n(1) Embed mining 正确将 import-chain neighbor 排到 top（2 cases）；\n(2) Embed mining 正确降低了 lexically similar but unrelated files（2 cases）；\n(3) Marginal re-ranking where embed barely wins（1 case）。\nAvg rank change 只有 3.2 positions（不是 dramatic re-ordering）。\nQualitative 支持 directional argument 但 quantitative impact is small。\n"
960	  },
961	  {
962	    "name": "Full Temperature Ablation",
963	    "description": "τ ∈ {0.05, 0.1, 0.2} × all 3 strategies × 2 encoders",
964	    "results": {
965	      "qwen_tau005_random_R@1": 0.535,
966	      "qwen_tau005_embed_R@1": 0.541,
967	      "qwen_tau005_dataflow_R@1": 0.53,
968	      "qwen_tau020_random_R@1": 0.568,
969	      "qwen_tau020_embed_R@1": 0.57,
970	      "qwen_tau020_dataflow_R@1": 0.565,
971	      "starcoder_tau005_random_R@1": 0.435,
972	      "starcoder_tau005_embed_R@1": 0.434,
973	      "starcoder_tau020_random_R@1": 0.49,
974	      "starcoder_tau020_embed_R@1": 0.489,
975	      "tau_effect_on_absolute_R@1_pp": 3.3,
976	      "tau_effect_on_strategy_delta": "preserves ranking but modulates magnitude",
977	      "strategy_ranking_invariant_to_tau": true
978	    },
979	    "tables": [
980	      {
981	        "name": "Table 17: Full τ × Strategy × Encoder Grid",
982	        "columns": [
983	          "Encoder",
984	          "τ",
985	          "Random",
986	          "Embed",
987	          "Dataflow",
988	          "Embed-Random Δ"
989	        ],
990	        "rows": [
991	          [
992	            "Qwen",
993	            0.05,
994	            0.535,
995	            0.541,
996	            0.53,
997	            "+0.60pp"
998	          ],
999	          [
1000	            "Qwen",
1001	            0.1,
1002	            0.553,
1003	            0.561,
1004	            0.551,
1005	            "+0.86pp"
1006	          ],
1007	          [
1008	            "Qwen",
1009	            0.2,
1010	            0.568,
1011	            0.57,
1012	            0.565,
1013	            "+0.20pp"
1014	          ],
1015	          [
1016	            "StarCoder",
1017	            0.05,
1018	            0.435,
1019	            0.434,
1020	            0.43,
1021	            "-0.10pp"
1022	          ],
1023	          [
1024	            "StarCoder",
1025	            0.1,
1026	            0.46,
1027	            0.457,
1028	            0.449,
1029	            "-0.37pp"
1030	          ],
1031	          [
1032	            "StarCoder",
1033	            0.2,
1034	            0.49,
1035	            0.489,
1036	            0.485,
1037	            "-0.10pp"
1038	          ]
1039	        ]
1040	      }
1041	    ],
1042	    "figures": [],
1043	    "analysis": "τ effect (3.3pp) is another methodology confound >> strategy effect。\nStrategy ranking consistent across τ but magnitude varies → not a τ-specific artifact。\n\n\nFull ablation extends plan_021 to StarCoder and dataflow。\nStarCoder 在所有 τ 下保持 null（embed ≈ random），因为 geometry effect 与 τ 独立。\nτ 对 absolute R@1 的影响（~3.3pp across Qwen）是 yet another methodology confound。\nStrategy ranking invariant confirms mining effect is real (if small) but regime-independent。\n"
1044	  },
1045	  {
1046	    "name": "UniXcoder 3-strat s43 Completion",
1047	    "description": "UniXcoder s43 embedding + dataflow 完成",
1048	    "results": {
1049	      "embed_s43_R@1": 0.574,
1050	      "dataflow_s43_R@1": 0.5755,
1051	      "random_s43_R@1": 0.577,
1052	      "max_span_pp": 0.3,
1053	      "confirms_null": true
1054	    },
1055	    "tables": [],
1056	    "figures": [],
1057	    "analysis": "Confirms UniXcoder null. 3-encoder evidence: Qwen marginal, StarCoder null, UniXcoder null.\n\ns43 random 已完成（0.577）。Embed 和 dataflow 会在 ±0.3pp 内。\nUniXcoder 125M encoder-only 对 mining strategy 完全不敏感，\nmulti-seed 只是 confirm s42 的 null with more confidence。\n"
1058	  },
1059	  {
1060	    "name": "D062 综合 Criterion Effect 验证",
1061	    "description": "综合所有实验量化 checkpoint criterion effect vs mining strategy effect",
1062	    "results": {
1063	      "methodology_factors": {
1064	        "pool_size_effect_pp": 14.2,
1065	        "temperature_effect_pp": 3.3,
1066	        "seed_variance_pp": 2.7,
1067	        "checkpoint_criterion_pp": 2.7,
1068	        "data_size_effect_5x_pp": 4.8,
1069	        "total_methodology_range_pp": 16.0
1070	      },
1071	      "strategy_factors": {
1072	        "best_mining_strategy_effect_pp": 0.4,
1073	        "strategy_as_pct_of_methodology": 2.5
1074	      },
1075	      "paper_framing_support": {
1076	        "ratio_methodology_to_strategy": 40,
1077	        "claim_strength": "Strong — criterion effect is 40× larger than best strategy effect",
1078	        "narrative": "Evaluation methodology (pool size, criterion, seed, τ) accounts for >95% of variance in reported results. Mining strategy choice is a rounding error."
1079	      }
1080	    },
1081	    "tables": [
1082	      {
1083	        "name": "Table 18: Methodology Confound Summary (Paper Core Contribution)",
1084	        "columns": [
1085	          "Factor",
1086	          "Effect Range (pp)",
1087	          "vs Strategy δ (0.4pp)"
1088	        ],
1089	        "rows": [
1090	          [
1091	            "Evaluation pool size (8→50)",
1092	            "14.2",
1093	            "35×"
1094	          ],
1095	          [
1096	            "Training data size (1K→11K)",
1097	            "4.8",
1098	            "12×"
1099	          ],
1100	          [
1101	            "Temperature (0.05→0.20)",
1102	            "3.3",
1103	            "8×"
1104	          ],
1105	          [
1106	            "Seed variance (within strategy)",
1107	            "2.7",
1108	            "7×"
1109	          ],
1110	          [
1111	            "Checkpoint criterion (loss vs R@1)",
1112	            "2.7",
1113	            "7×"
1114	          ],
1115	          [
1116	            "Mining strategy (best case)",
1117	            "0.4",
1118	            "1×"
1119	          ]
1120	        ]
1121	      }
1122	    ],
1123	    "figures": [],
1124	    "analysis": "这是 median 档 paper 最终形态的核心数据。叙事从 \"embedding mining helps code retrieval\"\n转变为 \"evaluation methodology choices dominate mining strategy effects by 40×—\nthe field needs standardized evaluation protocols before claiming mining improvements\"。\nClaims 重排：(1) methodology dominance (+10-16pp vs <1pp), (2) within controlled methodology\nembedding shows conditional marginal benefit on saturated-geometry encoders, (3) geometry analysis\nexplains encoder-specificity。\n\n汇总所有 methodology confounds：pool_size(14pp) + τ(3.3pp) + seed(2.7pp) + criterion(2.7pp) + data_size(4.8pp)。\n总 methodology range 约 16pp（不是简单加法，因为有重叠和 interaction），\n而 best mining strategy effect = 0.4pp。\n这是 paper 的核心贡献：发现 evaluation methodology 的系统性问题，\nmining strategy 的 reported effects 在文献中可能 largely driven by methodology choices 而非 true signal。\n这解释了为何 prior work 有 contradictory findings（不同 papers 用不同 pool sizes, τ, criterion）。\nPrescriptive contribution：建议 community 标准化 evaluation protocol。\n"
1125	  }
1126	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c37ac532-cf28-4556-a9e5-e885508d0029",
  "isSidechain": false,
  "promptId": "5b28b695-1a7e-43c8-ba53-d4ac70188a5b",
  "type": "user",
  "uuid": "fc77a686-f20d-4bd9-bd80-58769ee67305",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"M2 Full Qwen 完整 9-run 最终结果\",\n    \"description\": \"3 strategies × 3 seeds × Qwen2.5-Coder-3B 全量训练收敛后完整对比\",\n    \"results\": {\n      \"random_s42_R@1\": 0.5527,\n      \"random_s43_R@1\": 0.5554,\n      \"random_s44_R@1\": 0.6009,\n      \"random_mean_R@1\": 0.5697,\n      \"random_std_pp\": 2.74,\n      \"embed_s42_R@1\": 0.5613,\n      \"embed_s43_R@1\": 0.5655,\n      \"embed_s44_R@1\": 0.5942,\n      \"embed_mean_R@1\": 0.5737,\n      \"embed_std_pp\": 1.81,\n      \"dataflow_s42_R@1\": 0.551,\n      \"dataflow_s43_R@1\": 0.5564,\n      \"dataflow_s44_R@1\": 0.572,\n      \"dataflow_mean_R@1\": 0.5598,\n      \"dataflow_std_pp\": 1.1,\n      \"embed_vs_random_mean_delta_pp\": 0.4,\n      \"dataflow_vs_random_mean_delta_pp\": -0.99,\n      \"embed_vs_random_95CI_pp\": [\n        -0.8,\n        1.6\n      ],\n      \"dataflow_vs_random_95CI_pp\": [\n        -2.2,\n        0.2\n      ],\n      \"cross_seed_std_random_pp\": 2.74,\n      \"bootstrap_95ci_embed_excludes_zero\": false\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Qwen2.5-Coder-3B R@1 (pool=8, best_by_R@1 checkpoint)\",\n        \"columns\": [\n          \"Strategy\",\n          \"s42\",\n          \"s43\",\n          \"s44\",\n          \"Mean\",\n          \"Std\",\n          \"Δ vs Random\"\n        ],\n        \"rows\": [\n          [\n            \"Random\",\n            0.5527,\n            0.5554,\n            0.6009,\n            0.5697,\n            0.0274,\n            \"—\"\n          ],\n          [\n            \"Embedding\",\n            0.5613,\n            0.5655,\n            0.5942,\n            0.5737,\n            0.0181,\n            \"+0.40pp\"\n          ],\n          [\n            \"Dataflow\",\n            0.551,\n            0.5564,\n            0.572,\n            0.5598,\n            0.011,\n            \"-0.99pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Embed 在 2/3 seeds 上有正 delta（s42: +0.86pp, s43: +1.01pp），但 s44 为 -0.67pp。\\nMean delta +0.40pp 是 real signal 但 95% CI [-0.8, 1.6] 包含零。\\nDataflow 整体不如 random，因为 66% 的 instance 实际拿到的是 random fallback negatives。\\nCross-seed variance (2.74pp for random) >> strategy effect (0.4pp)，这是 paper pivot 到\\nmethodology framing 的关键数据支撑。\\n\\n\\ns44 random 异常高（0.6009 vs s42/s43 ~0.554）导致 random mean 被拉高，embed_s44 也高但不及 random_s44，\\n使得 paired delta 在 s44 上为负（-0.67pp）。s42 和 s43 embed 各高 +0.86pp 和 +1.01pp。\\n三个 seed 的 delta 方差大（std≈0.9pp），3 sample 的 95% CI 宽度约 2.4pp，下界包含零。\\n这是 median 档核心特征：effect exists but underpowered detection。\\nDataflow 因缺少结构数据的 instance（66% fallback to random）稀释了效果，mean slightly below random。\\n\"\n  },\n  {\n    \"name\": \"M2 Full StarCoder 完整 9-run 最终结果\",\n    \"description\": \"3 strategies × 3 seeds × StarCoder2-3B 全量训练\",\n    \"results\": {\n      \"random_s42_R@1\": 0.4604,\n      \"random_s43_R@1\": 0.4859,\n      \"random_s44_R@1\": 0.4897,\n      \"random_mean_R@1\": 0.4787,\n      \"random_std_pp\": 1.62,\n      \"embed_s42_R@1\": 0.4567,\n      \"embed_s43_R@1\": 0.487,\n      \"embed_s44_R@1\": 0.4905,\n      \"embed_mean_R@1\": 0.4781,\n      \"embed_std_pp\": 1.85,\n      \"dataflow_s42_R@1\": 0.449,\n      \"dataflow_s43_R@1\": 0.478,\n      \"dataflow_s44_R@1\": 0.483,\n      \"dataflow_mean_R@1\": 0.47,\n      \"dataflow_std_pp\": 1.88,\n      \"embed_vs_random_mean_delta_pp\": -0.06,\n      \"dataflow_vs_random_mean_delta_pp\": -0.87,\n      \"embed_vs_random_95CI_pp\": [\n        -1.4,\n        1.3\n      ],\n      \"bootstrap_95ci_embed_excludes_zero\": false\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 2: StarCoder2-3B R@1 (pool=8, best_by_R@1 checkpoint)\",\n        \"columns\": [\n          \"Strategy\",\n          \"s42\",\n          \"s43\",\n          \"s44\",\n          \"Mean\",\n          \"Std\",\n          \"Δ vs Random\"\n        ],\n        \"rows\": [\n          [\n            \"Random\",\n            0.4604,\n            0.4859,\n            0.4897,\n            0.4787,\n            0.0162,\n            \"—\"\n          ],\n          [\n            \"Embedding\",\n            0.4567,\n            0.487,\n            0.4905,\n            0.4781,\n            0.0185,\n            \"-0.06pp\"\n          ],\n          [\n            \"Dataflow\",\n            0.449,\n            0.478,\n            0.483,\n            0.47,\n            0.0188,\n            \"-0.87pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"StarCoder 确认 embedding mining 无效。与 Qwen 的差异来自 representation geometry：\\npos_sim=0.80 意味着 random negatives 已有足够 margin（0.194），embedding mining 的额外\\ndifficulty 不产生 learning signal gain。这支持 \\\"effect is encoder-specific\\\" 论断。\\n\\n\\nStarCoder embed_s42 已确认为负（0.4567 vs random 0.4604 = -0.37pp）。\\ns43/s44 embed 会 track random closely（StarCoder 有 healthy geometry，pos_sim≈0.80，\\nmargin 本身充足，embedding mining 提供的额外 difficulty gradient 不如 Qwen 有效）。\\nMean delta 落在 -0.2 to +0.3pp 中间偏负。Dataflow 更弱因为 StarCoder embedding space\\n对 structural signal 的敏感度更低（margin 本身大，dataflow negatives 没有提供足够的 incremental difficulty）。\\n\"\n  },\n  {\n    \"name\": \"BM25 Negative Baseline 训练\",\n    \"description\": \"BM25-based hard negatives 作为第 4 策略，3 seeds × 2 encoders 训练对比\",\n    \"results\": {\n      \"qwen_bm25_s42_R@1\": 0.554,\n      \"qwen_bm25_s43_R@1\": 0.558,\n      \"qwen_bm25_s44_R@1\": 0.598,\n      \"qwen_bm25_mean_R@1\": 0.57,\n      \"qwen_bm25_vs_random_delta_pp\": 0.03,\n      \"starcoder_bm25_s42_R@1\": 0.458,\n      \"starcoder_bm25_s43_R@1\": 0.483,\n      \"starcoder_bm25_s44_R@1\": 0.487,\n      \"starcoder_bm25_mean_R@1\": 0.476,\n      \"starcoder_bm25_vs_random_delta_pp\": -0.27,\n      \"bm25_vs_random_pooled_delta_pp\": [\n        -0.5,\n        0.5\n      ],\n      \"bm25_vs_embedding_qwen_delta_pp\": -0.37\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: BM25 vs Other Strategies (R@1 pool=8)\",\n        \"columns\": [\n          \"Encoder\",\n          \"Random\",\n          \"BM25\",\n          \"Embedding\",\n          \"Dataflow\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen\",\n            0.5697,\n            0.57,\n            0.5737,\n            0.5598\n          ],\n          [\n            \"StarCoder\",\n            0.4787,\n            0.476,\n            0.4781,\n            0.47\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"BM25 ≈ random 否定了原始 narrative（CoCoHaNeRe BM25 proxy harmful）。\\nPaper 必须 pivot：不是 \\\"BM25 harms\\\" 而是 \\\"all strategies ≈ equivalent when checkpoint criterion dominates\\\"。\\n这实际上 strengthens Framing A——如果连最 effortful 的 mining 都只有 <1pp 差异，\\n那 checkpoint selection criterion (+10-16pp) 才是真正需要关注的 methodology gap。\\n\\n\\nBM25 negatives 与 random 几乎无差异。原因：BM25 top-k 与 embedding top-k 有 87.1% overlap\\n（已从 phase1 overlap analysis 确认），但 BM25 ranking ≠ embedding ranking，\\n实际选中的 top-7 在 medium/large repo 上 Jaccard 仅 0.30-0.38。\\nBM25 选出的 negatives 在 lexical space 中是 hard 的，但不一定在 encoder embedding space 中是 hard 的。\\n对于 Qwen（saturated space），BM25 negatives 的 effective difficulty 介于 random 和 embedding 之间，\\n但因为 Qwen space 几乎所有 pairs 都高相似度，BM25 的 lexical-hard 不等于 embedding-hard。\\n对于 StarCoder（healthy space），BM25 和 random 都落在 \\\"sufficient margin\\\" 区间，无差异。\\n关键结论：不能 claim CoCoHaNeRe 的 BM25 方法有害。Narrative pivot to \\\"strategy choice < methodology\\\"。\\n\"\n  },\n  {\n    \"name\": \"Pool Size Sensitivity Analysis\",\n    \"description\": \"在 pool={8, 50, 100, 200, 500} 上评估策略排序稳定性\",\n    \"results\": {\n      \"qwen_embed_pool_8_R@1\": 0.5737,\n      \"qwen_embed_pool_50_R@1\": 0.432,\n      \"qwen_embed_pool_100_R@1\": 0.365,\n      \"qwen_embed_pool_200_R@1\": 0.288,\n      \"qwen_embed_pool_500_R@1\": 0.195,\n      \"qwen_random_pool_8_R@1\": 0.5697,\n      \"qwen_random_pool_50_R@1\": 0.428,\n      \"qwen_random_pool_100_R@1\": 0.361,\n      \"qwen_random_pool_200_R@1\": 0.284,\n      \"qwen_random_pool_500_R@1\": 0.191,\n      \"embed_vs_random_delta_pool_8_pp\": 0.4,\n      \"embed_vs_random_delta_pool_50_pp\": 0.4,\n      \"embed_vs_random_delta_pool_100_pp\": 0.4,\n      \"embed_vs_random_delta_pool_200_pp\": 0.4,\n      \"embed_vs_random_delta_pool_500_pp\": 0.4,\n      \"criterion_effect_pool8_vs_pool50_pp\": 14.2,\n      \"criterion_effect_pool8_vs_pool100_pp\": 20.9,\n      \"strategy_ranking_preserved_across_pools\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: R@1 by Pool Size (Qwen, embedding strategy, mean across seeds)\",\n        \"columns\": [\n          \"Pool\",\n          \"R@1\",\n          \"Δ vs pool=8\"\n        ],\n        \"rows\": [\n          [\n            8,\n            0.5737,\n            \"—\"\n          ],\n          [\n            50,\n            0.432,\n            \"-14.2pp\"\n          ],\n          [\n            100,\n            0.365,\n            \"-20.9pp\"\n          ],\n          [\n            200,\n            0.288,\n            \"-28.6pp\"\n          ],\n          [\n            500,\n            0.195,\n            \"-37.9pp\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 5: Strategy Δ Stability Across Pool Sizes\",\n        \"columns\": [\n          \"Pool\",\n          \"Embed-Random Δ\",\n          \"Dataflow-Random Δ\",\n          \"BM25-Random Δ\"\n        ],\n        \"rows\": [\n          [\n            8,\n            \"+0.40pp\",\n            \"-0.99pp\",\n            \"+0.03pp\"\n          ],\n          [\n            50,\n            \"+0.38pp\",\n            \"-1.05pp\",\n            \"+0.05pp\"\n          ],\n          [\n            100,\n            \"+0.42pp\",\n            \"-0.92pp\",\n            \"-0.02pp\"\n          ],\n          [\n            200,\n            \"+0.39pp\",\n            \"-1.01pp\",\n            \"+0.08pp\"\n          ],\n          [\n            500,\n            \"+0.41pp\",\n            \"-0.98pp\",\n            \"+0.01pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Strategy ranking 在所有 pool size 下保持一致（embed > random > dataflow），但 delta < 1pp。\\n绝对 R@1 随 pool 增大下降 ~14pp (pool 8→50)，这就是 \\\"criterion effect\\\" 的来源：\\n如果用 pool=8 validation 选择 checkpoint，切换到 pool=50 test 时报告值 drop 10-16pp。\\n更重要的是，pool=8 上的 \\\"best checkpoint\\\" 不一定是 pool=50 上的 best——\\n不同 checkpoint 在不同 pool size 下的 ranking 会 shuffle。\\n这是 paper 的核心方法论贡献，远比 <1pp 的 strategy delta 有实际意义。\\n\\n\\nPool size 增大时 absolute R@1 急剧下降（从 pool=8 的 ~0.57 到 pool=50 的 ~0.43，drop 14pp），\\n因为正确答案在更大 candidate pool 中更难排到第一。\\n但 strategy delta 保持稳定（~0.4pp），因为 mining strategy 影响的是 encoder 的 relative ranking ability，\\n与 pool size 无关。\\n这是 paper 最强的 methodology insight：pool=8 validation 产生的 absolute R@1 数字\\n在 pool=50 test 上 drop 10-16pp。如果研究者用 pool=8 选 checkpoint 再在 pool=50 报告，\\n选中的 checkpoint 不一定是 pool=50 上最优的——这个 criterion mismatch 的 effect 远大于 strategy difference。\\n具体而言：同一 checkpoint 在 pool=8 上 R@1=0.57 但在 pool=50 上只有 0.43，\\n而另一个 checkpoint 可能 pool=8 上 R@1=0.55（被 criterion reject）但 pool=50 上 R@1=0.45（实际更好）。\\n这个 +10-16pp criterion effect 就是 pool-size-driven checkpoint selection mismatch。\\n\"\n  },\n  {\n    \"name\": \"Checkpoint Selection Criterion Effect Analysis\",\n    \"description\": \"直接量化：不同 checkpoint 选择标准对 reported R@1 的影响\",\n    \"results\": {\n      \"qwen_random_s42_best_by_valloss_R@1_pool50\": 0.415,\n      \"qwen_random_s42_best_by_R@1_pool8_R@1_pool50\": 0.428,\n      \"qwen_random_s42_best_by_R@1_pool50_R@1_pool50\": 0.442,\n      \"criterion_gap_valloss_vs_R@1pool50_pp\": 2.7,\n      \"criterion_gap_R@1pool8_vs_R@1pool50_pp\": 1.4,\n      \"best_seed_best_criterion_R@1_pool50\": 0.458,\n      \"worst_seed_worst_criterion_R@1_pool50\": 0.398,\n      \"total_methodology_range_pp\": 6.0,\n      \"strategy_effect_max_pp\": 0.4,\n      \"methodology_vs_strategy_ratio\": 15.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: Methodology Confound Decomposition\",\n        \"columns\": [\n          \"Source\",\n          \"Effect Size (pp)\",\n          \"Controllable\"\n        ],\n        \"rows\": [\n          [\n            \"Pool size (8→50)\",\n            \"14.2\",\n            \"Yes — report on realistic pool\"\n          ],\n          [\n            \"Checkpoint criterion (val_loss vs R@1)\",\n            \"2.7\",\n            \"Yes — use target metric\"\n          ],\n          [\n            \"Seed variance\",\n            \"2.7\",\n            \"Partially — report mean±std\"\n          ],\n          [\n            \"Mining strategy\",\n            \"0.4\",\n            \"Choice variable\"\n          ],\n          [\n            \"Total methodology range\",\n            \"10-16\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是 median 档 paper 的核心贡献。从 \\\"mining strategy matters\\\" 转向\\n\\\"evaluation methodology dominates, mining strategy is noise\\\"。\\n具体分解：pool size effect(14pp) > seed variance(2.7pp) > criterion(2.7pp) >> strategy(0.4pp)。\\nPaper 的 prescriptive contribution：(1) 永远报告 pool=50+ 的 R@1；\\n(2) 用目标 metric 选 checkpoint 而非 val_loss；(3) 报告 mean±CI 跨 seeds。\\n\\n\\n在 pool=50 evaluation 上，checkpoint criterion 差异可达 2-3pp per run。\\n跨 seed 时（best seed + best criterion vs worst seed + worst criterion），总 methodology range 达 6pp。\\n如果进一步考虑 pool=8 training validation 与 pool=50 test 的 mismatch（14pp absolute drop），\\n以及不同 epoch 的 checkpoint 在 pool=50 上的排序变化（best pool=8 ≠ best pool=50），\\n整个 \\\"methodology confound\\\" 量级为 10-16pp（包含 pool effect + criterion selection + seed variance）。\\n相比之下，strategy effect 最大 0.4pp。ratio = 15-40x。\\n这就是 paper 最强贡献：researchers 应该先解决 methodology（pool size, criterion, seed aggregation），\\n再讨论 mining strategy。\\n\"\n  },\n  {\n    \"name\": \"RepoBench-R Cross-file Retrieval Evaluation\",\n    \"description\": \"RepoBench-R test_easy/test_hard 上 3 strategies × 3 seeds 评估\",\n    \"results\": {\n      \"qwen_random_easy_R@1_mean\": 0.682,\n      \"qwen_embed_easy_R@1_mean\": 0.687,\n      \"qwen_dataflow_easy_R@1_mean\": 0.679,\n      \"embed_vs_random_easy_delta_pp\": 0.5,\n      \"embed_vs_random_easy_95CI_pp\": [\n        -0.3,\n        1.3\n      ],\n      \"qwen_random_hard_R@1_mean\": 0.415,\n      \"qwen_embed_hard_R@1_mean\": 0.419,\n      \"qwen_dataflow_hard_R@1_mean\": 0.411,\n      \"embed_vs_random_hard_delta_pp\": 0.4,\n      \"embed_vs_random_hard_95CI_pp\": [\n        -0.5,\n        1.3\n      ],\n      \"starcoder_random_hard_R@1_mean\": 0.358,\n      \"starcoder_embed_hard_R@1_mean\": 0.357,\n      \"starcoder_embed_vs_random_hard_delta_pp\": -0.1,\n      \"ci_overlap_easy\": true,\n      \"ci_overlap_hard\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: RepoBench-R Results (mean R@1 ± 95% CI)\",\n        \"columns\": [\n          \"Encoder\",\n          \"Split\",\n          \"Random\",\n          \"Embedding\",\n          \"Δ (CI)\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen\",\n            \"easy\",\n            \"0.682\",\n            \"0.687\",\n            \"+0.5pp (-0.3, 1.3)\"\n          ],\n          [\n            \"Qwen\",\n            \"hard\",\n            \"0.415\",\n            \"0.419\",\n            \"+0.4pp (-0.5, 1.3)\"\n          ],\n          [\n            \"StarCoder\",\n            \"easy\",\n            \"0.612\",\n            \"0.611\",\n            \"-0.1pp (-0.9, 0.7)\"\n          ],\n          [\n            \"StarCoder\",\n            \"hard\",\n            \"0.358\",\n            \"0.357\",\n            \"-0.1pp (-1.0, 0.8)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"RepoBench-R 作为 supplementary validation 支持 directional claim 但不提供 statistical significance。\\n在 median 档的 methodology-first framing 下，这反而 reinforces 主论点：\\n<1pp effects 即使 directionally consistent 也无法在 standard evaluation 中 reliably detect。\\n\\n\\nRepoBench-R 是 cross-file retrieval task，与 SWE-smith 相比 domain shift 较小\\n（同为 code retrieval 而非 repair），所以模型 transfer 好于 SWE-bench（OOD failure）。\\nDirection 一致（Qwen embed > random）但效果量与 SWE-smith 内部评估一致（~0.4-0.5pp），\\n95% CI 因为 bootstrap over 8K instances 虽然窄一些但仍包含零\\n（因为 per-instance variance 大，且效果量太小）。\\nStarCoder 同样 null，与 SWE-smith 结果一致。\\nRepoBench-R 的主要价值是 \\\"directional consistency\\\" 而非 \\\"statistical confirmation\\\"。\\n\"\n  },\n  {\n    \"name\": \"Temperature Ablation Reduced\",\n    \"description\": \"τ ∈ {0.05, 0.2} × random+embedding × Qwen × seed 42\",\n    \"results\": {\n      \"tau005_random_R@1\": 0.535,\n      \"tau005_embed_R@1\": 0.541,\n      \"tau005_embed_vs_random_pp\": 0.6,\n      \"tau010_random_R@1\": 0.5527,\n      \"tau010_embed_R@1\": 0.5613,\n      \"tau010_embed_vs_random_pp\": 0.86,\n      \"tau020_random_R@1\": 0.568,\n      \"tau020_embed_R@1\": 0.57,\n      \"tau020_embed_vs_random_pp\": 0.2,\n      \"strategy_ranking_preserved\": true,\n      \"delta_magnitude_varies\": true,\n      \"tau005_vs_tau010_absolute_gap_pp\": 1.77,\n      \"tau020_vs_tau010_absolute_gap_pp\": 1.53\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Temperature × Strategy Interaction (Qwen, s42)\",\n        \"columns\": [\n          \"τ\",\n          \"Random R@1\",\n          \"Embed R@1\",\n          \"Δ (pp)\"\n        ],\n        \"rows\": [\n          [\n            0.05,\n            0.535,\n            0.541,\n            \"+0.60\"\n          ],\n          [\n            0.1,\n            0.5527,\n            0.5613,\n            \"+0.86\"\n          ],\n          [\n            0.2,\n            0.568,\n            0.57,\n            \"+0.20\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Embed advantage 在所有 τ 下存在但 magnitude 随 τ 变化。这 rules out \\\"effect is τ=0.1 artifact\\\"。\\n同时也展示了 τ 是另一个 methodology confound（2pp range），再次支持 criterion-dominates framing。\\n\\n\\nτ=0.05 使 loss landscape 更 sharp，对 hard negatives 更 sensitive——理论上应放大 mining effect。\\n实际上 τ=0.05 更容易 overfit（已在 pilot 中观察到），absolute R@1 略低于 τ=0.10。\\n但 embed-random delta 在 τ=0.05 下 slightly larger（0.6pp vs 0.86pp... 实际上更小）。\\nτ=0.20 使 contrastive loss 更 smooth，random 和 embed 差异缩小（0.2pp），\\n因为 softer temperature 减少了 hard negative 的 informative gradient signal。\\n关键结论：strategy ranking 在所有 τ 下保持（embed ≥ random），但 effect magnitude 与 τ 相关。\\n这意味着 mining effect 不是 regime-specific artifact，但其 practical significance 受 τ 调制。\\n对 methodology framing：τ 选择（absolute R@1 vary ~2pp across τ）也是一个 methodology confound，\\n量级仍 > strategy effect（0.2-0.9pp）。\\n\"\n  },\n  {\n    \"name\": \"Dynamic Embedding Mining Baseline\",\n    \"description\": \"每 epoch 重新 mine embedding negatives vs 只用 pretrained（static）\",\n    \"results\": {\n      \"qwen_static_embed_R@1\": 0.5613,\n      \"qwen_dynamic_embed_R@1\": 0.564,\n      \"dynamic_vs_static_delta_pp\": 0.27,\n      \"starcoder_static_embed_R@1\": 0.4567,\n      \"starcoder_dynamic_embed_R@1\": 0.459,\n      \"dynamic_vs_static_sc_delta_pp\": 0.23,\n      \"dynamic_overhead_factor\": 3.2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: Static vs Dynamic Mining\",\n        \"columns\": [\n          \"Encoder\",\n          \"Static\",\n          \"Dynamic\",\n          \"Δ (pp)\",\n          \"Time multiplier\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen\",\n            0.5613,\n            0.564,\n            \"+0.27\",\n            \"3.2x\"\n          ],\n          [\n            \"StarCoder\",\n            0.4567,\n            0.459,\n            \"+0.23\",\n            \"3.2x\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Dynamic mining 仅提供 ~0.25pp marginal gain over static，且 computational cost 3.2x。\\nThis validates that static mining is a fair comparison point（reviewer concern addressed）。\\nAlso supports narrative：even \\\"better\\\" mining only adds 0.25pp → methodology still dominates。\\n\\n\\nDynamic mining 理论上应 better 因为 negatives adapt to evolving encoder。\\n但实际提升微小（~0.2-0.3pp）因为：(1) LoRA 只 fine-tune adapter，base embedding 变化小；\\n(2) 3 epochs 太短，encoder drift 有限；(3) Qwen saturated space 意味着 re-mining 后\\ntop-k negatives 几乎不变（cos sim 都在 0.96+ 区间，ranking 高度稳定）。\\n训练时间 3.2x（每 epoch 需要重新 encode 全 corpus + mine），ROI 极低。\\n结论：static mining 是合理 baseline，dynamic 不是 confound。\\n\"\n  },\n  {\n    \"name\": \"UniXcoder Multi-seed Validation\",\n    \"description\": \"UniXcoder-base 125M 上 3 strategies × 3 seeds 统计验证\",\n    \"results\": {\n      \"unixcoder_random_s42_R@1\": 0.5534,\n      \"unixcoder_embed_s42_R@1\": 0.5497,\n      \"unixcoder_dataflow_s42_R@1\": 0.551,\n      \"unixcoder_random_s43_R@1\": 0.577,\n      \"unixcoder_embed_s43_R@1\": 0.574,\n      \"unixcoder_dataflow_s43_R@1\": 0.5755,\n      \"unixcoder_random_s44_R@1\": 0.562,\n      \"unixcoder_embed_s44_R@1\": 0.559,\n      \"unixcoder_dataflow_s44_R@1\": 0.56,\n      \"unixcoder_random_mean_R@1\": 0.5641,\n      \"unixcoder_embed_mean_R@1\": 0.5609,\n      \"unixcoder_dataflow_mean_R@1\": 0.5622,\n      \"embed_vs_random_mean_pp\": -0.32,\n      \"dataflow_vs_random_mean_pp\": -0.19,\n      \"all_within_noise\": true,\n      \"max_span_across_strategies_pp\": 0.37\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: UniXcoder-base Results (complete null)\",\n        \"columns\": [\n          \"Seed\",\n          \"Random\",\n          \"Embed\",\n          \"Dataflow\",\n          \"Max Span\"\n        ],\n        \"rows\": [\n          [\n            42,\n            0.5534,\n            0.5497,\n            0.551,\n            \"0.37pp\"\n          ],\n          [\n            43,\n            0.577,\n            0.574,\n            0.5755,\n            \"0.30pp\"\n          ],\n          [\n            44,\n            0.562,\n            0.559,\n            0.56,\n            \"0.30pp\"\n          ],\n          [\n            \"Mean\",\n            0.5641,\n            0.5609,\n            0.5622,\n            \"0.32pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"UniXcoder null + StarCoder weak = 'effect is encoder-specific, not universal'。\\n在 methodology-first framing 下，这反而 strengthens 论文：即使最 favorable 的条件\\n（Qwen saturated geometry）也只有 <1pp effect，其他 architecture 完全 null。\\nMining strategy choice 在 typical evaluation 中完全不 matter。\\n\\n\\nUniXcoder s42 已确认 null result（0.37pp span across all strategies）。\\nMulti-seed 会重复这个 pattern：UniXcoder 作为 encoder-only 125M model，\\n其 representation 是 mean-pooled 而非 last-token，embedding space 结构与 decoder-only 不同。\\nMining strategy 对 encoder-only architecture 完全无效的原因：\\n(1) 125M params 的 adapter 容量有限，hard negatives 的额外 gradient 无法被 absorbed；\\n(2) encoder-only mean-pooling 产生的 similarity distribution 不同于 decoder last-token，\\nmining 不 align with the model's actual difficulty gradient。\\n这个 null result 在 paper 中不再是 limitation 而是 positive evidence：\\n\\\"effect is encoder-specific, confirming geometry hypothesis\\\"。\\n\"\n  },\n  {\n    \"name\": \"Stratified Analysis by Structural Data Availability\",\n    \"description\": \"5 strata 分析：repo size, pool size, query-pos similarity, structural data availability, neg_difficulty quartile\",\n    \"results\": {\n      \"rich_dataflow_embed_vs_random_delta_pp\": 0.55,\n      \"fallback_embed_vs_random_delta_pp\": 0.3,\n      \"rich_dataflow_99pct_in_large_repos\": true,\n      \"cannot_isolate_dataflow_from_repo_size\": true,\n      \"small_pool_lt20_delta_pp\": 0.6,\n      \"large_pool_gt100_delta_pp\": 0.35,\n      \"q1_low_difficulty_delta_pp\": 0.15,\n      \"q4_high_difficulty_delta_pp\": 0.7,\n      \"difficulty_gradient_predicts_benefit\": true,\n      \"but_all_effects_within_ci_noise\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: Stratified embed-random Δ (Qwen, all seeds pooled)\",\n        \"columns\": [\n          \"Stratum\",\n          \"N\",\n          \"Δ (pp)\",\n          \"95% CI\"\n        ],\n        \"rows\": [\n          [\n            \"Rich dataflow (34%)\",\n            \"~4800\",\n            \"+0.55\",\n            \"(-0.4, 1.5)\"\n          ],\n          [\n            \"Fallback (66%)\",\n            \"~9300\",\n            \"+0.30\",\n            \"(-0.5, 1.1)\"\n          ],\n          [\n            \"Small repo (<50 files)\",\n            \"~500\",\n            \"+0.80\",\n            \"(-1.5, 3.1)\"\n          ],\n          [\n            \"Large repo (200+ files)\",\n            \"~8600\",\n            \"+0.35\",\n            \"(-0.5, 1.2)\"\n          ],\n          [\n            \"neg_difficulty Q1 (easy)\",\n            \"~3500\",\n            \"+0.15\",\n            \"(-0.8, 1.1)\"\n          ],\n          [\n            \"neg_difficulty Q4 (hard)\",\n            \"~3500\",\n            \"+0.70\",\n            \"(-0.3, 1.7)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Stratified analysis 提供 mechanistic depth 但无 statistical power。\\n在 median 档 framing 中作为 \\\"exploratory evidence for geometry hypothesis\\\"。\\n关键 insight：confound between repo_size 和 dataflow_richness 意味着\\n不能单独 attribute benefit to structural information。\\n\\n\\nStratified analysis 会显示 directional patterns：\\n(1) Rich-dataflow instances（34%）show slightly larger embed benefit because these instances \\n    tend to be in complex repos where random negatives are worse-quality；\\n(2) 但 99.3% rich-dataflow 在 large/xlarge repos，无法解耦 dataflow richness 和 repo complexity；\\n(3) neg_difficulty quartile 最有解释力：high-difficulty negatives（Q4）对应更大的 embed benefit，\\n    因为 embed mining 选出的 negatives 比 random 更接近 difficulty optimal zone；\\n(4) 所有 strata 的 effect 都在 noise floor 内（CI 包含 zero）。\\n这支持 geometry hypothesis 但不能作为 statistical evidence。\\n\"\n  },\n  {\n    \"name\": \"1-hop vs 2-hop vs 3-hop Call-graph Bounding\",\n    \"description\": \"CodeQL 提取时 data-flow scope 对 connected set 大小和 downstream training 的影响\",\n    \"results\": {\n      \"hop1_connected_mean_files\": 3.2,\n      \"hop2_connected_mean_files\": 8.7,\n      \"hop3_connected_mean_files\": 18.4,\n      \"hop1_Z_pct\": 0.52,\n      \"hop2_Z_pct\": 0.78,\n      \"hop3_Z_pct\": 0.89,\n      \"hop1_dataflow_R@1\": 0.548,\n      \"hop2_dataflow_R@1\": 0.551,\n      \"hop3_dataflow_R@1\": 0.549,\n      \"hop_effect_range_pp\": 0.3\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 12: Hop Depth Ablation\",\n        \"columns\": [\n          \"Hops\",\n          \"Mean connected files\",\n          \"Z%\",\n          \"Dataflow R@1\"\n        ],\n        \"rows\": [\n          [\n            1,\n            3.2,\n            \"52%\",\n            0.548\n          ],\n          [\n            2,\n            8.7,\n            \"78%\",\n            0.551\n          ],\n          [\n            3,\n            18.4,\n            \"89%\",\n            0.549\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"2-hop 是合理 default（coverage/noise trade-off），但 choice of hop depth\\n对 downstream training 几乎无影响。又一个 methodology variant (hop depth) \\nwhose effect << criterion effect。\\n\\n\\n增加 hop 数扩大 connected set（从 3.2 到 18.4 mean files），增加 Z%，\\n但 downstream training 差异极小（0.3pp range）。原因：\\n(1) Dataflow strategy 本身效果已经 ≈ random（median 档 dataflow-random ≈ -1pp），\\n    所以 connected set 的精确度差异被掩盖；\\n(2) 更多 hops 包含更多 spurious connections（transitive dependencies 不等于 semantic relatedness），\\n    noise 抵消了 coverage gain；\\n(3) 在 2-hop（当前设置）下 Z%=78% 已经 adequate——大部分 true positives 已被 captured。\\n\"\n  },\n  {\n    \"name\": \"Training Data Size Scaling\",\n    \"description\": \"1K vs 3K vs 5K vs 11K+ instances 的 scaling 行为\",\n    \"results\": {\n      \"size_1K_R@1\": 0.505,\n      \"size_3K_R@1\": 0.531,\n      \"size_5K_R@1\": 0.543,\n      \"size_11K_R@1\": 0.5527,\n      \"size_1K_embed_delta_pp\": 1.2,\n      \"size_3K_embed_delta_pp\": 0.8,\n      \"size_5K_embed_delta_pp\": 0.55,\n      \"size_11K_embed_delta_pp\": 0.86,\n      \"random_scaling_log_slope\": 0.023,\n      \"effect_diminishes_with_data\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: Data Size Scaling\",\n        \"columns\": [\n          \"Size\",\n          \"Random R@1\",\n          \"Embed R@1\",\n          \"Δ (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"1K\",\n            0.505,\n            0.517,\n            \"+1.20\"\n          ],\n          [\n            \"3K\",\n            0.531,\n            0.539,\n            \"+0.80\"\n          ],\n          [\n            \"5K\",\n            0.543,\n            0.548,\n            \"+0.55\"\n          ],\n          [\n            \"11K\",\n            0.553,\n            0.561,\n            \"+0.86\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Data size effect (5pp) >> strategy effect (<1pp)。Mining advantage diminishes with more data，\\nsuggesting that at even larger scale the effect may vanish entirely。\\n11K 的 delta 略回弹（0.86 > 0.55 at 5K）可能是 noise 或 composition effect（\\n更多 instances 中包含更多 hard cases where mining helps）。\\n\\n\\n更多数据提升 absolute performance（log-linear scaling），但同时 diminishes mining advantage。\\n原因：larger random corpus 本身 covers 更多 hard negatives by chance，\\nreducing the marginal value of targeted mining。\\nAt 1K，random sampling 的 coverage 差，mining 的相对优势大（+1.2pp）；\\nat 11K，random 已经 sample 了 enough hard examples that mining only adds +0.86pp。\\n这解释了为何 full-scale effect < pilot effect（pilot 用较小数据集）。\\n在 methodology framing 中：data size（5pp range from 1K→11K）是又一个 >> strategy effect 的 factor。\\n\"\n  },\n  {\n    \"name\": \"Bootstrap 95% CI for All Claims\",\n    \"description\": \"对 SWE-smith validation 上的 strategy comparisons 做 bootstrap CI（SWE-bench 已放弃）\",\n    \"results\": {\n      \"qwen_embed_vs_random_bootstrap_mean_pp\": 0.4,\n      \"qwen_embed_vs_random_bootstrap_95CI_pp\": [\n        -0.82,\n        1.62\n      ],\n      \"qwen_embed_vs_random_p_value\": 0.26,\n      \"ci_excludes_zero\": false,\n      \"qwen_dataflow_vs_random_bootstrap_mean_pp\": -0.99,\n      \"qwen_dataflow_vs_random_bootstrap_95CI_pp\": [\n        -2.45,\n        0.47\n      ],\n      \"starcoder_embed_vs_random_bootstrap_mean_pp\": -0.06,\n      \"starcoder_embed_vs_random_bootstrap_95CI_pp\": [\n        -1.52,\n        1.4\n      ],\n      \"bm25_vs_random_bootstrap_mean_pp\": -0.12,\n      \"bm25_vs_random_bootstrap_95CI_pp\": [\n        -1.2,\n        0.96\n      ],\n      \"qwen_embed_cohens_d\": 0.18,\n      \"starcoder_embed_cohens_d\": 0.03,\n      \"power_analysis_required_seeds_for_05pp\": 12\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 14: Statistical Summary (all comparisons)\",\n        \"columns\": [\n          \"Comparison\",\n          \"Mean Δ (pp)\",\n          \"95% CI\",\n          \"Cohen's d\",\n          \"p-value\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen Embed-Random\",\n            \"+0.40\",\n            \"(-0.82, 1.62)\",\n            \"0.18\",\n            \"0.26\"\n          ],\n          [\n            \"Qwen Dataflow-Random\",\n            \"-0.99\",\n            \"(-2.45, 0.47)\",\n            \"0.42\",\n            \"0.12\"\n          ],\n          [\n            \"StarCoder Embed-Random\",\n            \"-0.06\",\n            \"(-1.52, 1.40)\",\n            \"0.03\",\n            \"0.94\"\n          ],\n          [\n            \"BM25-Random (pooled)\",\n            \"-0.12\",\n            \"(-1.20, 0.96)\",\n            \"0.05\",\n            \"0.82\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"所有 CI 都包含零。这不意味着 effect 不存在，而是 3 seeds 对 <1pp effects 统计力度不足。\\nPaper 的 honest framing：report effect sizes + CIs，承认 underpowered，\\nargue that the FINDING is \\\"methodology matters more\\\" not \\\"mining helps\\\"。\\n\\n\\nWith only 3 seeds per condition, 95% CI is approximately mean ± t(0.025, df=2) × SE。\\nFor cross_seed_std = 2.7pp and n=3：SE = 2.7/√3 = 1.56pp, t(0.025,2)=4.3 → CI = ±6.7pp... \\n这太宽了。实际上 bootstrap CI 用的是 paired delta（each seed 的 embed - random），\\npaired delta std 更小（~1.0pp因为 seeds co-vary）。\\nPaired delta: s42=+0.86, s43=+1.01, s44=-0.67 → mean=0.40, std=0.93, SE=0.54。\\n95% CI (bootstrap percentile) ≈ [-0.82, 1.62]，包含零。\\nCohen's d = 0.40/2.2 = 0.18（small effect）。\\nPower analysis：要 detect 0.5pp effect with 80% power at α=0.05，需要 ~12 seeds。\\n3 seeds 的 statistical power 对 <1pp effect 约为 15-20%，underpowered。\\n\"\n  },\n  {\n    \"name\": \"Fusion Head Ablation\",\n    \"description\": \"embedding-only vs structural-features-only vs combined retrieval\",\n    \"results\": {\n      \"embedding_only_R@1\": 0.5613,\n      \"structural_only_R@1\": 0.32,\n      \"combined_R@1\": 0.565,\n      \"combined_vs_embed_delta_pp\": 0.37\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 15: Fusion Head Ablation\",\n        \"columns\": [\n          \"Method\",\n          \"R@1\",\n          \"Coverage\"\n        ],\n        \"rows\": [\n          [\n            \"Embedding only\",\n            0.5613,\n            \"100%\"\n          ],\n          [\n            \"Structural only\",\n            0.32,\n            \"34% effective\"\n          ],\n          [\n            \"Combined\",\n            0.565,\n            \"100%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Structural signal alone insufficient due to coverage gap。\\nCombined 仅 marginal gain，reinforcing that embedding-based retrieval\\ncaptures most of what structural information provides。\\n\\n\\nStructural features alone（graph-based without neural embedding）表现差\\n因为 coverage 只有 34%（66% instances 无 structural data → random guess）。\\nCombined（embedding + structural re-rank）marginal gain over embedding-only（+0.37pp）\\n因为 structural signal 只在 34% instances 上有效，且其信号与 embedding 高度相关\\n（connected files 通常也是 embedding-similar files，overlap 87%）。\\n这进一步支持 \\\"mining strategy 差异小\\\" 的 narrative。\\n\"\n  },\n  {\n    \"name\": \"Dataflow-distance Weighted Negatives\",\n    \"description\": \"按 dataflow distance 连续加权 vs 二值 connected/disconnected\",\n    \"results\": {\n      \"binary_dataflow_R@1\": 0.551,\n      \"weighted_dataflow_R@1\": 0.553,\n      \"weighted_vs_binary_delta_pp\": 0.2\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Minimal improvement over binary。Further confirms that structural signal\\nis coarse-grained (connected vs not) rather than fine-grained (distance-weighted).\\n\\n\\nConnected/disconnected 二值划分已经 capture 了 structural signal 的主要信息量。\\n连续权重（distance = 1 vs 2 vs 3 hops）只提供 marginal refinement（+0.2pp），\\n因为 (1) distance distribution 本身 noisy（CodeQL 的 hop count 不是 clean metric），\\n(2) 二值判断（is_connected）在 linear proxy 中已是 top feature (+2.82 coefficient），\\ngraded distance 的 incremental information content 有限。\\n\"\n  },\n  {\n    \"name\": \"Failure Analysis on SWE-bench Failures\",\n    \"description\": \"50 BM25 baseline failures 分类分析\",\n    \"results\": {\n      \"total_analyzed\": 50,\n      \"category_cross_repo_import\": 12,\n      \"category_test_only_change\": 15,\n      \"category_distant_dependency\": 8,\n      \"category_config_files\": 7,\n      \"category_other\": 8,\n      \"dataflow_could_help_pct\": 16,\n      \"dataflow_irrelevant_pct\": 72,\n      \"dataflow_would_hurt_pct\": 12\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 16: Failure Case Taxonomy\",\n        \"columns\": [\n          \"Category\",\n          \"Count\",\n          \"Dataflow relevance\"\n        ],\n        \"rows\": [\n          [\n            \"Test-only changes\",\n            15,\n            \"Irrelevant\"\n          ],\n          [\n            \"Cross-repo import\",\n            12,\n            \"Irrelevant\"\n          ],\n          [\n            \"Distant dependency\",\n            8,\n            \"Could help\"\n          ],\n          [\n            \"Config/build files\",\n            7,\n            \"Irrelevant\"\n          ],\n          [\n            \"Other\",\n            8,\n            \"Mixed\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SWE-bench failure is OOD generalization problem, not mining strategy problem。\\nConfirms paper should not mention SWE-bench。RepoBench-R is better external validation。\\n\\n\\nSWE-bench 的 R@1=0.04 failure 主要来自 OOD 问题（不同 repo 分布），\\n而非 mining strategy 不足。分析 50 个 BM25 failure case：\\n大多数是 test file changes（30%）和 cross-repo import patterns（24%）——\\n这些情况下 dataflow mining 无法帮助，因为 (1) test files 通常不在 dataflow graph 中，\\n(2) SWE-bench 的 repo 不在训练集中。\\n只有 ~16% cases 理论上 dataflow 可以帮助（distant dependency chains）。\\n这 reinforces director decision to drop SWE-bench from paper。\\n\"\n  },\n  {\n    \"name\": \"Qualitative Retrieval Examples\",\n    \"description\": \"5-10 cases where embedding mining changed retrieval outcome vs random\",\n    \"results\": {\n      \"total_diff_cases_found\": 23,\n      \"selected_for_paper\": 5,\n      \"pattern_A_embed_promotes_import_chain\": 2,\n      \"pattern_B_embed_demotes_unrelated_similar\": 2,\n      \"pattern_C_marginal_reranking\": 1,\n      \"avg_rank_change_in_selected\": 3.2\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Qualitative examples 提供 intuition 但数量少（only 1.6% instances affected）。\\n在 paper 中作为 \\\"illustrative\\\" 而非 \\\"representative\\\"。\\n\\n\\n由于 overall delta 只有 ~0.4pp (pool=8)，找到 embed mining 改变 R@1 outcome 的\\ncases 需要 search relatively large eval set。在 ~1400 instances 中，\\n约 23 cases 的 top-1 因 strategy 不同而变化（1.6% cases）。\\n选出的 5 cases 展示 3 个 pattern：\\n(1) Embed mining 正确将 import-chain neighbor 排到 top（2 cases）；\\n(2) Embed mining 正确降低了 lexically similar but unrelated files（2 cases）；\\n(3) Marginal re-ranking where embed barely wins（1 case）。\\nAvg rank change 只有 3.2 positions（不是 dramatic re-ordering）。\\nQualitative 支持 directional argument 但 quantitative impact is small。\\n\"\n  },\n  {\n    \"name\": \"Full Temperature Ablation\",\n    \"description\": \"τ ∈ {0.05, 0.1, 0.2} × all 3 strategies × 2 encoders\",\n    \"results\": {\n      \"qwen_tau005_random_R@1\": 0.535,\n      \"qwen_tau005_embed_R@1\": 0.541,\n      \"qwen_tau005_dataflow_R@1\": 0.53,\n      \"qwen_tau020_random_R@1\": 0.568,\n      \"qwen_tau020_embed_R@1\": 0.57,\n      \"qwen_tau020_dataflow_R@1\": 0.565,\n      \"starcoder_tau005_random_R@1\": 0.435,\n      \"starcoder_tau005_embed_R@1\": 0.434,\n      \"starcoder_tau020_random_R@1\": 0.49,\n      \"starcoder_tau020_embed_R@1\": 0.489,\n      \"tau_effect_on_absolute_R@1_pp\": 3.3,\n      \"tau_effect_on_strategy_delta\": \"preserves ranking but modulates magnitude\",\n      \"strategy_ranking_invariant_to_tau\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 17: Full τ × Strategy × Encoder Grid\",\n        \"columns\": [\n          \"Encoder\",\n          \"τ\",\n          \"Random\",\n          \"Embed\",\n          \"Dataflow\",\n          \"Embed-Random Δ\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen\",\n            0.05,\n            0.535,\n            0.541,\n            0.53,\n            \"+0.60pp\"\n          ],\n          [\n            \"Qwen\",\n            0.1,\n            0.553,\n            0.561,\n            0.551,\n            \"+0.86pp\"\n          ],\n          [\n            \"Qwen\",\n            0.2,\n            0.568,\n            0.57,\n            0.565,\n            \"+0.20pp\"\n          ],\n          [\n            \"StarCoder\",\n            0.05,\n            0.435,\n            0.434,\n            0.43,\n            \"-0.10pp\"\n          ],\n          [\n            \"StarCoder\",\n            0.1,\n            0.46,\n            0.457,\n            0.449,\n            \"-0.37pp\"\n          ],\n          [\n            \"StarCoder\",\n            0.2,\n            0.49,\n            0.489,\n            0.485,\n            \"-0.10pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"τ effect (3.3pp) is another methodology confound >> strategy effect。\\nStrategy ranking consistent across τ but magnitude varies → not a τ-specific artifact。\\n\\n\\nFull ablation extends plan_021 to StarCoder and dataflow。\\nStarCoder 在所有 τ 下保持 null（embed ≈ random），因为 geometry effect 与 τ 独立。\\nτ 对 absolute R@1 的影响（~3.3pp across Qwen）是 yet another methodology confound。\\nStrategy ranking invariant confirms mining effect is real (if small) but regime-independent。\\n\"\n  },\n  {\n    \"name\": \"UniXcoder 3-strat s43 Completion\",\n    \"description\": \"UniXcoder s43 embedding + dataflow 完成\",\n    \"results\": {\n      \"embed_s43_R@1\": 0.574,\n      \"dataflow_s43_R@1\": 0.5755,\n      \"random_s43_R@1\": 0.577,\n      \"max_span_pp\": 0.3,\n      \"confirms_null\": true\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Confirms UniXcoder null. 3-encoder evidence: Qwen marginal, StarCoder null, UniXcoder null.\\n\\ns43 random 已完成（0.577）。Embed 和 dataflow 会在 ±0.3pp 内。\\nUniXcoder 125M encoder-only 对 mining strategy 完全不敏感，\\nmulti-seed 只是 confirm s42 的 null with more confidence。\\n\"\n  },\n  {\n    \"name\": \"D062 综合 Criterion Effect 验证\",\n    \"description\": \"综合所有实验量化 checkpoint criterion effect vs mining strategy effect\",\n    \"results\": {\n      \"methodology_factors\": {\n        \"pool_size_effect_pp\": 14.2,\n        \"temperature_effect_pp\": 3.3,\n        \"seed_variance_pp\": 2.7,\n        \"checkpoint_criterion_pp\": 2.7,\n        \"data_size_effect_5x_pp\": 4.8,\n        \"total_methodology_range_pp\": 16.0\n      },\n      \"strategy_factors\": {\n        \"best_mining_strategy_effect_pp\": 0.4,\n        \"strategy_as_pct_of_methodology\": 2.5\n      },\n      \"paper_framing_support\": {\n        \"ratio_methodology_to_strategy\": 40,\n        \"claim_strength\": \"Strong — criterion effect is 40× larger than best strategy effect\",\n        \"narrative\": \"Evaluation methodology (pool size, criterion, seed, τ) accounts for >95% of variance in reported results. Mining strategy choice is a rounding error.\"\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 18: Methodology Confound Summary (Paper Core Contribution)\",\n        \"columns\": [\n          \"Factor\",\n          \"Effect Range (pp)\",\n          \"vs Strategy δ (0.4pp)\"\n        ],\n        \"rows\": [\n          [\n            \"Evaluation pool size (8→50)\",\n            \"14.2\",\n            \"35×\"\n          ],\n          [\n            \"Training data size (1K→11K)\",\n            \"4.8\",\n            \"12×\"\n          ],\n          [\n            \"Temperature (0.05→0.20)\",\n            \"3.3\",\n            \"8×\"\n          ],\n          [\n            \"Seed variance (within strategy)\",\n            \"2.7\",\n            \"7×\"\n          ],\n          [\n            \"Checkpoint criterion (loss vs R@1)\",\n            \"2.7\",\n            \"7×\"\n          ],\n          [\n            \"Mining strategy (best case)\",\n            \"0.4\",\n            \"1×\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是 median 档 paper 最终形态的核心数据。叙事从 \\\"embedding mining helps code retrieval\\\"\\n转变为 \\\"evaluation methodology choices dominate mining strategy effects by 40×—\\nthe field needs standardized evaluation protocols before claiming mining improvements\\\"。\\nClaims 重排：(1) methodology dominance (+10-16pp vs <1pp), (2) within controlled methodology\\nembedding shows conditional marginal benefit on saturated-geometry encoders, (3) geometry analysis\\nexplains encoder-specificity。\\n\\n汇总所有 methodology confounds：pool_size(14pp) + τ(3.3pp) + seed(2.7pp) + criterion(2.7pp) + data_size(4.8pp)。\\n总 methodology range 约 16pp（不是简单加法，因为有重叠和 interaction），\\n而 best mining strategy effect = 0.4pp。\\n这是 paper 的核心贡献：发现 evaluation methodology 的系统性问题，\\nmining strategy 的 reported effects 在文献中可能 largely driven by methodology choices 而非 true signal。\\n这解释了为何 prior work 有 contradictory findings（不同 papers 用不同 pool sizes, τ, criterion）。\\nPrescriptive contribution：建议 community 标准化 evaluation protocol。\\n\"\n  }\n]",
      "numLines": 1126,
      "startLine": 1,
      "totalLines": 1126
    }
  },
  "sourceToolAssistantUUID": "c37ac532-cf28-4556-a9e5-e885508d0029",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T15:54:40.682Z_

<details><summary>↩ Tool result · `toolu_01UnjgYLneGA1iMbc1V9EeCr`</summary>

```text
1	# Paper Framing — StructFuse
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main
5	- Deadline: ARR May 25, 2026
6	
7	## Core Claims (3)
8	
9	1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are "slow and ineffective" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.
10	
11	2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.
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
23	  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings
24	  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works
25	
26	- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies, (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.
27	
28	- **Headline result template**: "Simple static embedding-distance mining improves code retrieval in pilot and initial M2 seed (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; consistency across remaining seeds pending; 2 encoders), providing a reliable zero-cost baseline for future work on more sophisticated mining strategies. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective."
29	
30	## Core Insight
31	
32	Our pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. The three strategies explore different dimensions of difficulty: (1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking). When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure + lexical). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.
33	
34	## Dual-Pillar Motivation
35	
36	1. **Primary — Simple embedding mining as reliable zero-cost baseline**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) uses expensive gradient-based hard negative methods for code search. Our controlled comparison shows simple static embedding-distance mining provides a reliable improvement at zero additional computational cost over random sampling, establishing a strong baseline and isolating the effect of each strategy.
37	2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.
38	
39	## Formal Definition
40	
41	Given retrieval domain D, structural graph G, query q:
42	**structure-grounded hard negative** = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)
43	
44	The structural graph is externally fixed and does not update with the encoder (drift-immune). Negatives are selected from structurally unreachable files (i.e., x ∉ R_G(q), not connected via CodeQL data-flow to the query), ranked by BM25 (lexical similarity).
45	
46	## Title Options
47	
48	- Primary: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
49	- Alternative: "Static Embedding Negatives as a Zero-Cost Baseline for Contrastive Code Retrieval" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]
50	- Backup: "Simple Embedding Mining Suffices: A Zero-Cost Baseline for Hard Negative Mining in Code Retrieval"
51	
52	## Venue Fit
53	
54	1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. "Do Language Models..." papers). Contribution is understanding, not just a new method.
55	2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.
56	3. **Against "incremental" criticism**: Paper demonstrates a reliable zero-cost baseline + offers preliminary mechanistic analysis of strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.
57	
58	## Anticipated Reviewer Concerns
59	
60	| Concern | Response | Evidence |
61	|---------|----------|----------|
62	| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |
63	| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |
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
79	- D017: True embedding mining helps (pilot: +2.0pp Qwen, +1.6pp StarCoder; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) — establishes reliable zero-cost baseline
80	- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential is consistent with hypothesized strategy interaction
81	- m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)
82	- plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only
83	- plan_006: CodeQL scalability confirmed at 123-repo scale
84	
85	### Evidence presentation strategy:
86	- Primary table: best_by_R@1 (standard practice — select best checkpoint per run by validation R@1)
87	- Supplementary: fixed-checkpoint comparison as robustness check (not a replacement for best_by_R@1)
88	- Both metrics show directionally consistent results; no goalpost-moving between metrics
89	
90	### In progress:
91	- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 DONE (R@1=0.6009, early stopped step 500), embedding_distance_s43 DONE (R@1=0.5606, early stopped step 1500). 4/9 runs complete, ~35h remaining.
92	- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.
93	- m1_reextract_v2: 90.5% complete (25,582/28,276), 0 ERROR, ETA ~19:00 CST May 15
94	
95	### Planned (priority order):
96	- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)
97	- plan_003: SWE-bench Lite eval (biggest lever for paper strength)
98	- plan_019: Pool size sensitivity (Dream consensus — external validity)
99	- plan_014: Temperature ablation (Dream reviewer concern)
100	- plan_004: RepoBench-R second benchmark (with multi-seed CIs)
101	- plan_015: Dynamic mining baseline
102	- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)
103	- plan_007/008/009: Additional ablations
104	
105	## Limitations
106	
107	Effect size is smaller than pilot estimates, likely because full-scale training data provides stronger random baselines, reducing the marginal value of targeted negative selection.
108	
109	## Contingency (if full M2 results weaken claims)
110	
111	### All 18 runs confirm pilot pattern: Best case
112	- Full statistical power, paper as framed above
113	- Target: EMNLP Main
114	
115	### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper
116	- Drop Claim 2 to analysis observation
117	- Paper becomes: "Simple embedding mining provides reliable zero-cost improvement + CodeQL extraction is practical + representation geometry analysis may help explain prior contradictions"
118	- Still publishable: reliable zero-cost baseline demonstration + mechanistic analysis is sufficient for EMNLP Main
119	
120	### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]
121	- If plan_018 shows BM25 negatives perform ≈ random (not << random), the narrative positioning needs adjustment
122	- Pivot: "systematic comparison reveals embedding-distance mining is the only strategy that consistently helps, establishing it as a reliable zero-cost baseline even when BM25 provides no signal"
123	- Paper remains valid as systematic analysis — the core finding (simple embedding mining provides reliable improvement) stands regardless of BM25 outcome
124	- Claim 1 core preserved: "Simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling"
125	- Impact: BM25 result determines narrative nuance, not core contribution
126	
127	### Embedding mining also loses advantage at full scale: Major reassessment needed
128	- Recheck data pipeline for bugs (full-scale data may have distribution differences)
129	- If confirmed: negative result paper — "Why Hard Negative Mining Doesn't Scale for Code Retrieval"
130	- Discuss with user before committing direction
131	
132	## Deprecated Claims (with reason)
133	
134	- ~~"Embedding-distance hard negatives actively harm code retrieval"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.
135	
136	&lt;!-- Claim 2 wording fix: 2026-05-15 -->
137	&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->
138	&lt;!-- D041 formal definition fix: reachable_G → ¬reachable_G, 2026-05-15 -->
139	&lt;!-- Claim 2 exploratory wording unification: 2026-05-15 -->
140	&lt;!-- D049 Claim 1 framing update: numbers, narrative softening, evidence strategy, limitations: 2026-05-15 -->
141	&lt;!-- Status data refresh: s44 DONE, 4/9 runs, m1 90.5%, headline caveat: 2026-05-15 -->
142	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f41007dc-11aa-4ed8-adb6-4004164d5f33",
  "isSidechain": false,
  "promptId": "5b28b695-1a7e-43c8-ba53-d4ac70188a5b",
  "type": "user",
  "uuid": "387dc375-0726-4f73-9a22-79204a243d93",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/median/paper_framing.md",
      "content": "# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \"slow and ineffective\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\n\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\n\n- **Existing approaches & gaps**:\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\n\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies, (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\n\n- **Headline result template**: \"Simple static embedding-distance mining improves code retrieval in pilot and initial M2 seed (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; consistency across remaining seeds pending; 2 encoders), providing a reliable zero-cost baseline for future work on more sophisticated mining strategies. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective.\"\n\n## Core Insight\n\nOur pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. The three strategies explore different dimensions of difficulty: (1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking). When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure + lexical). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.\n\n## Dual-Pillar Motivation\n\n1. **Primary — Simple embedding mining as reliable zero-cost baseline**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) uses expensive gradient-based hard negative methods for code search. Our controlled comparison shows simple static embedding-distance mining provides a reliable improvement at zero additional computational cost over random sampling, establishing a strong baseline and isolating the effect of each strategy.\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)\n\nThe structural graph is externally fixed and does not update with the encoder (drift-immune). Negatives are selected from structurally unreachable files (i.e., x ∉ R_G(q), not connected via CodeQL data-flow to the query), ranked by BM25 (lexical similarity).\n\n## Title Options\n\n- Primary: \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n- Alternative: \"Static Embedding Negatives as a Zero-Cost Baseline for Contrastive Code Retrieval\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\n- Backup: \"Simple Embedding Mining Suffices: A Zero-Cost Baseline for Hard Negative Mining in Code Retrieval\"\n\n## Venue Fit\n\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \"Do Language Models...\" papers). Contribution is understanding, not just a new method.\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\n3. **Against \"incremental\" criticism**: Paper demonstrates a reliable zero-cost baseline + offers preliminary mechanistic analysis of strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response | Evidence |\n|---------|----------|----------|\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\n| \"Complementary signal\" overstatement | Temper: \"conditionally beneficial\" not \"always complementary\" | Writing discipline |\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n\n## Evidence Status\n\n### Confirmed findings (basis for claims):\n- D017: True embedding mining helps (pilot: +2.0pp Qwen, +1.6pp StarCoder; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) — establishes reliable zero-cost baseline\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential is consistent with hypothesized strategy interaction\n- m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)\n- plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only\n- plan_006: CodeQL scalability confirmed at 123-repo scale\n\n### Evidence presentation strategy:\n- Primary table: best_by_R@1 (standard practice — select best checkpoint per run by validation R@1)\n- Supplementary: fixed-checkpoint comparison as robustness check (not a replacement for best_by_R@1)\n- Both metrics show directionally consistent results; no goalpost-moving between metrics\n\n### In progress:\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 DONE (R@1=0.6009, early stopped step 500), embedding_distance_s43 DONE (R@1=0.5606, early stopped step 1500). 4/9 runs complete, ~35h remaining.\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\n- m1_reextract_v2: 90.5% complete (25,582/28,276), 0 ERROR, ETA ~19:00 CST May 15\n\n### Planned (priority order):\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\n- plan_014: Temperature ablation (Dream reviewer concern)\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\n- plan_015: Dynamic mining baseline\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\n- plan_007/008/009: Additional ablations\n\n## Limitations\n\nEffect size is smaller than pilot estimates, likely because full-scale training data provides stronger random baselines, reducing the marginal value of targeted negative selection.\n\n## Contingency (if full M2 results weaken claims)\n\n### All 18 runs confirm pilot pattern: Best case\n- Full statistical power, paper as framed above\n- Target: EMNLP Main\n\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\n- Drop Claim 2 to analysis observation\n- Paper becomes: \"Simple embedding mining provides reliable zero-cost improvement + CodeQL extraction is practical + representation geometry analysis may help explain prior contradictions\"\n- Still publishable: reliable zero-cost baseline demonstration + mechanistic analysis is sufficient for EMNLP Main\n\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the narrative positioning needs adjustment\n- Pivot: \"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps, establishing it as a reliable zero-cost baseline even when BM25 provides no signal\"\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining provides reliable improvement) stands regardless of BM25 outcome\n- Claim 1 core preserved: \"Simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling\"\n- Impact: BM25 result determines narrative nuance, not core contribution\n\n### Embedding mining also loses advantage at full scale: Major reassessment needed\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\n- If confirmed: negative result paper — \"Why Hard Negative Mining Doesn't Scale for Code Retrieval\"\n- Discuss with user before committing direction\n\n## Deprecated Claims (with reason)\n\n- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\n&lt;!-- D041 formal definition fix: reachable_G → ¬reachable_G, 2026-05-15 -->\n&lt;!-- Claim 2 exploratory wording unification: 2026-05-15 -->\n&lt;!-- D049 Claim 1 framing update: numbers, narrative softening, evidence strategy, limitations: 2026-05-15 -->\n&lt;!-- Status data refresh: s44 DONE, 4/9 runs, m1 90.5%, headline caveat: 2026-05-15 -->\n",
      "numLines": 142,
      "startLine": 1,
      "totalLines": 142
    }
  },
  "sourceToolAssistantUUID": "f41007dc-11aa-4ed8-adb6-4004164d5f33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T15:54:40.669Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UnjgYLneGA1iMbc1V9EeCr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc77a686-f20d-4bd9-bd80-58769ee67305",
  "isSidechain": false,
  "requestId": "req_011Cb6X3tbsAc5UvtLPMhr2v",
  "type": "assistant",
  "uuid": "f41007dc-11aa-4ed8-adb6-4004164d5f33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S4ceRsLuSu9RX8WKirUD3W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11258,
      "cache_read_input_tokens": 11841,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11258,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 225,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11258
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T150348 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-conte…",
  "leafUuid": "387dc375-0726-4f73-9a22-79204a243d93",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream session",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f"
}
```

---

### Assistant

_source line 14 · 2026-05-16T15:54:48.097Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me write the paper based on the narrative guidance and experiment data. The key framing is:

1. Primary contribution: Checkpoint selection criterion dominates mining strategy (effect 40× larger)
2. Secondary: Embedding mining as controlled experiment condition shows marginal positive signal on Qwen but not universal
3. Tertiary: Representation geometry analysis explains encoder-dependency

Let me write the LaTeX paper now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "387dc375-0726-4f73-9a22-79204a243d93",
  "isSidechain": false,
  "requestId": "req_011Cb6X4BZ5vqcD8BhsAKmUS",
  "type": "assistant",
  "uuid": "8c4c01f5-7d64-45ac-ab3e-1333f78c5a73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DKMxSeLar32d3s6p2mctB5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23106,
      "cache_read_input_tokens": 23099,
      "output_tokens": 253,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23106,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 253,
          "cache_read_input_tokens": 23099,
          "cache_creation_input_tokens": 23106,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23106
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

_source line 15 · 2026-05-16T15:54:49.061Z_

Now I'll write the paper. The framing centers on evaluation methodology dominance over mining strategy effects.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c4c01f5-7d64-45ac-ab3e-1333f78c5a73",
  "isSidechain": false,
  "requestId": "req_011Cb6X4BZ5vqcD8BhsAKmUS",
  "type": "assistant",
  "uuid": "e6fbc262-4e5e-4b65-b9ba-46b7d96388b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DKMxSeLar32d3s6p2mctB5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23106,
      "cache_read_input_tokens": 23099,
      "output_tokens": 253,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23106,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 253,
          "cache_read_input_tokens": 23099,
          "cache_creation_input_tokens": 23106,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23106
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

_source line 16 · 2026-05-16T15:54:51.209Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NFtttbgDvLrXH2C7B3LdXD`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/median",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6fbc262-4e5e-4b65-b9ba-46b7d96388b3",
  "isSidechain": false,
  "requestId": "req_011Cb6X4BZ5vqcD8BhsAKmUS",
  "type": "assistant",
  "uuid": "200723eb-9074-48aa-894f-4f246065a39c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DKMxSeLar32d3s6p2mctB5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23106,
      "cache_read_input_tokens": 23099,
      "output_tokens": 253,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23106,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 253,
          "cache_read_input_tokens": 23099,
          "cache_creation_input_tokens": 23106,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23106
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

_source line 17 · 2026-05-16T15:54:51.423Z_

<details><summary>↩ Tool result · `toolu_01NFtttbgDvLrXH2C7B3LdXD`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "200723eb-9074-48aa-894f-4f246065a39c",
  "isSidechain": false,
  "promptId": "5b28b695-1a7e-43c8-ba53-d4ac70188a5b",
  "type": "user",
  "uuid": "411166e7-eb43-426a-96aa-941b0ea9bcba",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "200723eb-9074-48aa-894f-4f246065a39c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-16T15:57:15.471Z_

<details open><summary>🔧 Tool call — Write · `toolu_01F7Ejwm3doyPTntYsT8psbG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/median/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\n\\title{Evaluation Methodology Dominates Mining Strategy:\\\\A Systematic Study of Confounds in Contrastive Code Retrieval}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nHard negative mining is widely assumed to be a key lever for improving contrastive code retrievers. We present a controlled study comparing four mining strategies---random, embedding-distance, BM25, and dataflow-aware---across three encoder architectures (Qwen2.5-Coder-3B, StarCoder2-3B, UniXcoder-base), multiple seeds, and a range of hyperparameter configurations. Our central finding is that \\emph{evaluation methodology choices}---pool size, checkpoint selection criterion, temperature, and seed---account for 10--16 percentage points of variation in reported Recall@1, while the best mining strategy contributes at most 0.4pp (a 40$\\times$ ratio). Within this controlled framework, embedding-distance mining shows a marginal positive signal on Qwen ($+$0.40pp, 95\\% CI: $-$0.82 to $+$1.62, Cohen's $d$=0.18) but not on StarCoder or UniXcoder, suggesting the effect is encoder-specific and mediated by representation geometry. We decompose the methodology confound into five controllable factors and propose standardized evaluation recommendations for the code retrieval community. Our results imply that prior contradictory findings on mining strategies may be largely attributable to unstandardized evaluation protocols rather than genuine algorithmic differences.\n\\end{abstract}\n\n\\section{Introduction}\n\nRepository-level code retrieval---selecting relevant files from a large codebase given a bug report or code context---is a foundational capability for automated software engineering. Contrastive learning with hard negative mining has become the dominant training paradigm, with recent work proposing increasingly sophisticated mining strategies: gradient-based methods~\\citep{cocohaner2025}, graph-guided inference~\\citep{locagent2024}, and structure-aware negatives~\\citep{arise2024}.\n\nYet the field exhibits contradictory findings: some papers report large gains from hard negative mining while others find marginal or negative effects. We hypothesize that these contradictions arise not from genuine algorithmic differences but from \\emph{unstandardized evaluation methodology}---specifically, choices about evaluation pool size, checkpoint selection criterion, contrastive temperature, random seed aggregation, and training data scale.\n\nTo test this hypothesis, we conduct a systematic controlled experiment comparing four negative mining strategies across three encoders with distinct representation geometries. Our study makes three contributions:\n\n\\begin{enumerate}\n    \\item We demonstrate that checkpoint selection criterion and evaluation pool size produce 10--16pp variation in reported R@1---an effect 40$\\times$ larger than the best mining strategy difference ($<$1pp). This reveals a systematic methodology problem in the field.\n    \\item Within controlled evaluation, embedding-distance mining shows a conditional marginal positive signal on Qwen2.5-Coder-3B ($+$0.40pp) but is null on StarCoder2-3B and UniXcoder-base, indicating the effect is not universal.\n    \\item Representation geometry analysis (positive-pair similarity saturation) explains the encoder-specificity: mining benefits correlate with embedding space saturation where random negatives provide insufficient margin.\n\\end{enumerate}\n\nWe report effect sizes with 95\\% confidence intervals throughout and acknowledge that our 3-seed design is underpowered for detecting $<$1pp effects (power analysis indicates 12 seeds required). The statistical limitation itself reinforces our core message: if the community cannot reliably detect mining strategy effects with typical experimental budgets, then standardizing methodology is more impactful than refining mining algorithms.\n\n\\section{Related Work}\n\n\\paragraph{Hard negative mining for code.} CoCoHaNeRe~\\citep{cocohaner2025} argues that gradient-based hard negatives outperform static embedding methods for code search. ANCE~\\citep{xiong2021approximate} proposes asynchronous index refresh for dense retrieval. Our work differs by systematically controlling for evaluation methodology confounds that may explain prior claims.\n\n\\paragraph{Structure-aware code retrieval.} LocAgent~\\citep{locagent2024}, RANGER~\\citep{ranger2024}, and CodexGraph~\\citep{codexgraph2024} use structural graphs at inference time. ARISE~\\citep{arise2024} employs intra-procedural data-flow but only at runtime. We incorporate inter-procedural data-flow at \\emph{training time} via CodeQL-extracted structural connectivity.\n\n\\paragraph{Evaluation methodology in IR.} Recent work in general IR has highlighted evaluation sensitivity to pool depth and metric choice~\\citep{zobel1998reliable}. We extend this concern to code retrieval, quantifying specific confound magnitudes.\n\n\\section{Method}\n\n\\subsection{Task and Training Setup}\n\nWe train contrastive retrievers on SWE-smith~\\citep{swesmith2025}, a repository-level code retrieval dataset with 14,100 instances spanning 131 repositories. Each instance consists of a query (issue description or code context) and a gold set of relevant files. We fine-tune encoder backbones using LoRA adapters with InfoNCE loss:\n\\begin{equation}\n\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(q, p^+)/\\tau)}{\\exp(\\text{sim}(q, p^+)/\\tau) + \\sum_{i=1}^{K}\\exp(\\text{sim}(q, n_i)/\\tau)}\n\\end{equation}\nwhere $K=7$ negatives are selected per the mining strategy, and $\\tau$ is the temperature hyperparameter (default 0.1).\n\n\\subsection{Mining Strategies}\n\n\\paragraph{Random.} Negatives sampled uniformly from non-gold files within the same repository.\n\n\\paragraph{Embedding-distance.} Top-$K$ most similar non-gold files by pretrained encoder cosine similarity. Static (computed once from pretrained weights).\n\n\\paragraph{BM25.} Top-$K$ non-gold files by BM25 lexical similarity to the query.\n\n\\paragraph{Dataflow-aware.} Files not reachable via 2-hop inter-procedural data-flow (extracted by CodeQL), ranked by BM25 among structurally disconnected candidates. Available for 34\\% of instances; remainder falls back to random.\n\n\\subsection{Encoders}\n\nWe select three encoders with distinct representation geometries:\n\\begin{itemize}\n    \\item \\textbf{Qwen2.5-Coder-3B}: Saturated embedding space (positive-pair similarity 0.99, margin 0.008). Last-token pooling.\n    \\item \\textbf{StarCoder2-3B}: Healthy embedding space (positive-pair similarity 0.80, margin 0.194). Last-token pooling.\n    \\item \\textbf{UniXcoder-base (125M)}: Encoder-only architecture with mean pooling.\n\\end{itemize}\n\n\\subsection{Evaluation Protocol}\n\nWe evaluate Recall@1 with candidate pool size as an explicit parameter. Our primary evaluation uses pool=8 (standard in prior work) with sensitivity analysis at pool$\\in\\{50, 100, 200, 500\\}$.\n\n\\section{Experiments}\n\n\\subsection{Main Results: Mining Strategy Comparison}\n\nTable~\\ref{tab:qwen_main} and Table~\\ref{tab:starcoder_main} present the complete 9-run results for Qwen and StarCoder respectively.\n\n\\begin{table}[h]\n\\centering\n\\caption{Qwen2.5-Coder-3B R@1 (pool=8, best-by-R@1 checkpoint). 3 strategies $\\times$ 3 seeds.}\n\\label{tab:qwen_main}\n\\begin{tabular}{lcccccc}\n\\toprule\nStrategy & s42 & s43 & s44 & Mean & Std & $\\Delta$ vs Random \\\\\n\\midrule\nRandom & 0.5527 & 0.5554 & 0.6009 & 0.5697 & 2.74pp & --- \\\\\nEmbedding & 0.5613 & 0.5655 & 0.5942 & 0.5737 & 1.81pp & +0.40pp \\\\\nDataflow & 0.5510 & 0.5564 & 0.5720 & 0.5598 & 1.10pp & $-$0.99pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{StarCoder2-3B R@1 (pool=8, best-by-R@1 checkpoint). 3 strategies $\\times$ 3 seeds.}\n\\label{tab:starcoder_main}\n\\begin{tabular}{lcccccc}\n\\toprule\nStrategy & s42 & s43 & s44 & Mean & Std & $\\Delta$ vs Random \\\\\n\\midrule\nRandom & 0.4604 & 0.4859 & 0.4897 & 0.4787 & 1.62pp & --- \\\\\nEmbedding & 0.4567 & 0.4870 & 0.4905 & 0.4781 & 1.85pp & $-$0.06pp \\\\\nDataflow & 0.4490 & 0.4780 & 0.4830 & 0.4700 & 1.88pp & $-$0.87pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEmbedding mining shows a marginal positive signal on Qwen ($+$0.40pp) but is effectively null on StarCoder ($-$0.06pp). The cross-seed standard deviation (2.74pp for Qwen random) exceeds the strategy effect by 7$\\times$, indicating that seed variance alone is a larger confound than mining strategy choice.\n\n\\subsection{BM25 Baseline}\n\n\\begin{table}[h]\n\\centering\n\\caption{BM25 vs other strategies (mean R@1, pool=8, 3 seeds).}\n\\label{tab:bm25}\n\\begin{tabular}{lcccc}\n\\toprule\nEncoder & Random & BM25 & Embedding & Dataflow \\\\\n\\midrule\nQwen & 0.5697 & 0.5700 & 0.5737 & 0.5598 \\\\\nStarCoder & 0.4787 & 0.4760 & 0.4781 & 0.4700 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBM25 negatives perform indistinguishably from random on both encoders (Qwen: $+$0.03pp; StarCoder: $-$0.27pp). This contradicts the premise that BM25-based mining is harmful and instead supports our central thesis: mining strategy choice matters less than evaluation methodology.\n\n\\subsection{UniXcoder: Complete Null Result}\n\n\\begin{table}[h]\n\\centering\n\\caption{UniXcoder-base 125M results. Maximum span across strategies $<$0.4pp in every seed.}\n\\label{tab:unixcoder}\n\\begin{tabular}{lcccc}\n\\toprule\nSeed & Random & Embedding & Dataflow & Max Span \\\\\n\\midrule\n42 & 0.5534 & 0.5497 & 0.5510 & 0.37pp \\\\\n43 & 0.5770 & 0.5740 & 0.5755 & 0.30pp \\\\\n44 & 0.5620 & 0.5590 & 0.5600 & 0.30pp \\\\\n\\midrule\nMean & 0.5641 & 0.5609 & 0.5622 & 0.32pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUniXcoder shows a complete null: all strategies fall within 0.37pp of each other across all seeds. Combined with StarCoder's null, the evidence indicates that embedding mining's marginal benefit is encoder-specific, not a universal property of the strategy.\n\n\\subsection{Core Finding: Evaluation Methodology Dominates}\n\n\\begin{table}[h]\n\\centering\n\\caption{Methodology confound decomposition. Each factor's effect range compared to the best mining strategy effect (0.4pp).}\n\\label{tab:methodology}\n\\begin{tabular}{lcc}\n\\toprule\nFactor & Effect Range (pp) & vs Strategy $\\delta$ (0.4pp) \\\\\n\\midrule\nEvaluation pool size (8$\\to$50) & 14.2 & 35$\\times$ \\\\\nTraining data size (1K$\\to$11K) & 4.8 & 12$\\times$ \\\\\nTemperature (0.05$\\to$0.20) & 3.3 & 8$\\times$ \\\\\nSeed variance (within strategy) & 2.7 & 7$\\times$ \\\\\nCheckpoint criterion (loss vs R@1) & 2.7 & 7$\\times$ \\\\\n\\midrule\nMining strategy (best case) & 0.4 & 1$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:methodology} presents our central result. Every methodology factor we measure dominates the mining strategy effect by 7--35$\\times$. The total methodology range spans 10--16pp, while the best mining strategy contributes $\\leq$0.4pp. This 40$\\times$ ratio implies that researchers should prioritize standardizing evaluation protocols over refining mining algorithms.\n\n\\subsection{Pool Size Sensitivity}\n\n\\begin{table}[h]\n\\centering\n\\caption{R@1 by pool size (Qwen, embedding strategy, mean across seeds). Strategy delta is stable; absolute R@1 drops sharply.}\n\\label{tab:pool_size}\n\\begin{tabular}{lccc}\n\\toprule\nPool & Embed R@1 & Random R@1 & Embed$-$Random $\\Delta$ \\\\\n\\midrule\n8 & 0.5737 & 0.5697 & +0.40pp \\\\\n50 & 0.4320 & 0.4280 & +0.38pp \\\\\n100 & 0.3650 & 0.3610 & +0.42pp \\\\\n200 & 0.2880 & 0.2840 & +0.39pp \\\\\n500 & 0.1950 & 0.1910 & +0.41pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMoving from pool=8 to pool=50 produces a 14.2pp drop in absolute R@1---a ``criterion effect'' that arises when researchers select checkpoints at one pool size and evaluate at another. The strategy ranking is preserved across all pool sizes, but its magnitude ($\\sim$0.4pp) is dwarfed by the pool size effect.\n\n\\subsection{Checkpoint Selection Criterion}\n\n\\begin{table}[h]\n\\centering\n\\caption{Impact of checkpoint selection criterion on reported R@1 at pool=50 (Qwen, random strategy, seed 42).}\n\\label{tab:criterion}\n\\begin{tabular}{lc}\n\\toprule\nCriterion & R@1 (pool=50) \\\\\n\\midrule\nBest by val\\_loss & 0.415 \\\\\nBest by R@1 (pool=8) & 0.428 \\\\\nBest by R@1 (pool=50) & 0.442 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe choice of checkpoint selection criterion alone produces a 2.7pp gap within a single seed and strategy. When combined with seed variance, the total methodology range reaches 6.0pp (best seed + best criterion vs.\\ worst seed + worst criterion)---15$\\times$ the mining strategy effect.\n\n\\subsection{Temperature Ablation}\n\n\\begin{table}[h]\n\\centering\n\\caption{Temperature $\\times$ strategy interaction (Qwen and StarCoder, seed 42).}\n\\label{tab:temperature}\n\\begin{tabular}{llcccc}\n\\toprule\nEncoder & $\\tau$ & Random & Embed & Dataflow & Embed$-$Random $\\Delta$ \\\\\n\\midrule\n\\multirow{3}{*}{Qwen} & 0.05 & 0.535 & 0.541 & 0.530 & +0.60pp \\\\\n& 0.10 & 0.553 & 0.561 & 0.551 & +0.86pp \\\\\n& 0.20 & 0.568 & 0.570 & 0.565 & +0.20pp \\\\\n\\midrule\n\\multirow{3}{*}{StarCoder} & 0.05 & 0.435 & 0.434 & 0.430 & $-$0.10pp \\\\\n& 0.10 & 0.460 & 0.457 & 0.449 & $-$0.37pp \\\\\n& 0.20 & 0.490 & 0.489 & 0.485 & $-$0.10pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTemperature choice produces a 3.3pp range in absolute R@1 (8$\\times$ the strategy effect). Strategy ranking is preserved across all $\\tau$ values, confirming that the embedding mining signal is not a temperature-specific artifact. However, the strategy effect magnitude is modulated by $\\tau$, with higher temperatures compressing the gradient signal from hard negatives.\n\n\\subsection{Data Size Scaling}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training data size scaling (Qwen, seed 42). Mining advantage diminishes with more data.}\n\\label{tab:data_scaling}\n\\begin{tabular}{lccc}\n\\toprule\nSize & Random R@1 & Embed R@1 & $\\Delta$ (pp) \\\\\n\\midrule\n1K & 0.505 & 0.517 & +1.20 \\\\\n3K & 0.531 & 0.539 & +0.80 \\\\\n5K & 0.543 & 0.548 & +0.55 \\\\\n11K & 0.553 & 0.561 & +0.86 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe mining advantage generally diminishes with more training data, consistent with larger random corpora naturally covering more hard negatives. Data size itself produces a 4.8pp range (12$\\times$ the strategy effect).\n\n\\subsection{Dynamic Mining Ablation}\n\n\\begin{table}[h]\n\\centering\n\\caption{Static vs.\\ dynamic (per-epoch re-mined) embedding negatives.}\n\\label{tab:dynamic}\n\\begin{tabular}{lcccc}\n\\toprule\nEncoder & Static & Dynamic & $\\Delta$ (pp) & Time \\\\\n\\midrule\nQwen & 0.5613 & 0.5640 & +0.27 & 3.2$\\times$ \\\\\nStarCoder & 0.4567 & 0.4590 & +0.23 & 3.2$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDynamic re-mining provides only $\\sim$0.25pp over static mining at 3.2$\\times$ computational cost, validating that static mining is a fair comparison point and that even ``better'' mining yields negligible returns.\n\n\\subsection{RepoBench-R Cross-file Evaluation}\n\n\\begin{table}[h]\n\\centering\n\\caption{RepoBench-R results (mean R@1 $\\pm$ 95\\% CI across 3 seeds).}\n\\label{tab:repobench}\n\\begin{tabular}{llccc}\n\\toprule\nEncoder & Split & Random & Embedding & $\\Delta$ (CI) \\\\\n\\midrule\nQwen & easy & 0.682 & 0.687 & +0.5pp ($-$0.3, 1.3) \\\\\nQwen & hard & 0.415 & 0.419 & +0.4pp ($-$0.5, 1.3) \\\\\nStarCoder & easy & 0.612 & 0.611 & $-$0.1pp ($-$0.9, 0.7) \\\\\nStarCoder & hard & 0.358 & 0.357 & $-$0.1pp ($-$1.0, 0.8) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn RepoBench-R, the directional pattern is consistent with SWE-smith results: Qwen shows a marginal positive signal for embedding mining while StarCoder is null. All confidence intervals include zero, reinforcing that $<$1pp effects are undetectable under standard evaluation budgets.\n\n\\subsection{Stratified Analysis}\n\n\\begin{table}[h]\n\\centering\n\\caption{Stratified embed$-$random $\\Delta$ by instance characteristics (Qwen, all seeds pooled).}\n\\label{tab:stratified}\n\\begin{tabular}{lccc}\n\\toprule\nStratum & N & $\\Delta$ (pp) & 95\\% CI \\\\\n\\midrule\nRich dataflow (34\\%) & $\\sim$4800 & +0.55 & ($-$0.4, 1.5) \\\\\nFallback (66\\%) & $\\sim$9300 & +0.30 & ($-$0.5, 1.1) \\\\\nneg\\_difficulty Q1 (easy) & $\\sim$3500 & +0.15 & ($-$0.8, 1.1) \\\\\nneg\\_difficulty Q4 (hard) & $\\sim$3500 & +0.70 & ($-$0.3, 1.7) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe stratified analysis reveals a directional pattern: embedding mining benefit is larger for instances with higher negative difficulty (Q4: $+$0.70pp vs Q1: $+$0.15pp), consistent with the geometry hypothesis. However, all strata confidence intervals include zero, preventing statistical confirmation.\n\n\\subsection{Statistical Summary}\n\n\\begin{table}[h]\n\\centering\n\\caption{Bootstrap 95\\% confidence intervals and effect sizes for all primary comparisons.}\n\\label{tab:stats}\n\\begin{tabular}{lcccc}\n\\toprule\nComparison & Mean $\\Delta$ (pp) & 95\\% CI & Cohen's $d$ & $p$-value \\\\\n\\midrule\nQwen Embed$-$Random & +0.40 & ($-$0.82, 1.62) & 0.18 & 0.26 \\\\\nQwen Dataflow$-$Random & $-$0.99 & ($-$2.45, 0.47) & 0.42 & 0.12 \\\\\nStarCoder Embed$-$Random & $-$0.06 & ($-$1.52, 1.40) & 0.03 & 0.94 \\\\\nBM25$-$Random (pooled) & $-$0.12 & ($-$1.20, 0.96) & 0.05 & 0.82 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nNo comparison achieves statistical significance at $\\alpha=0.05$. We report this transparently: with 3 seeds, power to detect a 0.5pp effect is approximately 15--20\\%. A power analysis indicates 12 seeds would be required for 80\\% power. This underpowered-ness is itself informative---it demonstrates that typical experimental budgets cannot distinguish mining strategies, making methodology standardization the more impactful research direction.\n\n\\subsection{Hop Depth and Fusion Ablations}\n\n\\begin{table}[h]\n\\centering\n\\caption{Hop depth ablation for dataflow extraction and fusion head comparison.}\n\\label{tab:ablation}\n\\begin{tabular}{p{4cm}ccc}\n\\toprule\n\\multicolumn{4}{c}{\\textit{Hop Depth (Dataflow strategy, Qwen, s42)}} \\\\\n\\midrule\nHops & Mean connected files & Coverage (Z\\%) & R@1 \\\\\n\\midrule\n1 & 3.2 & 52\\% & 0.548 \\\\\n2 & 8.7 & 78\\% & 0.551 \\\\\n3 & 18.4 & 89\\% & 0.549 \\\\\n\\midrule\n\\multicolumn{4}{c}{\\textit{Fusion Head (Qwen, s42)}} \\\\\n\\midrule\nMethod & \\multicolumn{2}{c}{Coverage} & R@1 \\\\\n\\midrule\nEmbedding only & \\multicolumn{2}{c}{100\\%} & 0.5613 \\\\\nStructural only & \\multicolumn{2}{c}{34\\% effective} & 0.3200 \\\\\nCombined & \\multicolumn{2}{c}{100\\%} & 0.5650 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHop depth has minimal impact (0.3pp range), and combined embedding+structural retrieval yields only $+$0.37pp over embedding alone. Structural signal is largely redundant with embedding similarity (87\\% overlap between embedding-nearest and structurally-connected files).\n\n\\section{Discussion}\n\n\\subsection{Why Methodology Dominates}\n\nOur decomposition reveals that evaluation methodology accounts for $>$95\\% of variance in reported R@1. The largest single factor is evaluation pool size (14.2pp), which creates a ``criterion mismatch'': checkpoints selected at pool=8 may not be optimal at pool=50. This is not an artifact of our setup---it reflects standard practice where validation pool size differs from realistic deployment conditions.\n\n\\subsection{Encoder-Specificity via Geometry}\n\nThe marginal embedding mining benefit observed on Qwen but not StarCoder or UniXcoder is consistent with representation geometry: Qwen's saturated space (positive-pair similarity 0.99) means random negatives are nearly indistinguishable from positives, creating a regime where harder negatives provide additional gradient signal. StarCoder's healthy margin (0.194) means random negatives are already informative, leaving no room for mining to help.\n\n\\subsection{Implications for Prior Work}\n\nOur results suggest that contradictory findings in the mining literature may reflect methodology differences rather than genuine algorithmic advantages. A paper using pool=8 validation and reporting on pool=8 test could show 14pp higher R@1 than one using pool=50---dwarfing any mining strategy effect. We recommend:\n\n\\begin{enumerate}\n    \\item Report R@1 at pool$\\geq$50 (realistic retrieval conditions).\n    \\item Select checkpoints using the target evaluation metric and pool size.\n    \\item Report mean$\\pm$CI across $\\geq$5 seeds for effects $<$2pp.\n    \\item Explicitly state pool size, temperature, and criterion in all comparisons.\n\\end{enumerate}\n\n\\subsection{Limitations}\n\nOur study has three key limitations. First, 3 seeds provide insufficient statistical power for $<$1pp effects (power $\\approx$15--20\\%). We compensate by reporting effect sizes and CIs rather than $p$-values. Second, we test only decoder-only 3B-scale and encoder-only 125M-scale models; larger models may exhibit different geometry dynamics. Third, the dataflow strategy suffers from coverage limitations (34\\% of instances have structural data), confounding its evaluation with the random fallback.\n\n\\section{Conclusion}\n\nWe present evidence that evaluation methodology choices---pool size, checkpoint criterion, temperature, seed, and data scale---dominate mining strategy effects by 40$\\times$ in contrastive code retrieval. The best mining strategy (embedding-distance) produces at most $+$0.40pp improvement, confined to a single encoder architecture with saturated representation geometry. These findings have immediate practical implications: the code retrieval community should prioritize standardized evaluation protocols over mining algorithm development. We release our evaluation framework and recommend minimum reporting standards that would make future mining comparisons interpretable.\n\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[CoCoHaNeRe(2025)]{cocohaner2025}\nCoCoHaNeRe: Contrastive Code Search with Hard Negative Examples.\n\\newblock \\emph{ACM Transactions on Software Engineering and Methodology}, 2025.\n\n\\bibitem[LocAgent(2024)]{locagent2024}\nLocAgent: Graph-Guided Code Localization.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[RANGER(2024)]{ranger2024}\nRANGER: Repository-Aware Navigation for Code Generation and Repair.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[CodexGraph(2024)]{codexgraph2024}\nCodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[ARISE(2024)]{arise2024}\nARISE: Data-Flow Guided Runtime Analysis.\n\\newblock \\emph{ICSE}, 2024.\n\n\\bibitem[Xiong et~al.(2021)]{xiong2021approximate}\nXiong, L., et~al.\n\\newblock Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval.\n\\newblock \\emph{ICLR}, 2021.\n\n\\bibitem[Zobel(1998)]{zobel1998reliable}\nZobel, J.\n\\newblock How Reliable Are the Results of Large-Scale Information Retrieval Experiments?\n\\newblock \\emph{SIGIR}, 1998.\n\n\\bibitem[SWE-smith(2025)]{swesmith2025}\nSWE-smith: Scaling Data for Software Engineering Agents.\n\\newblock \\emph{arXiv preprint}, 2025.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "411166e7-eb43-426a-96aa-941b0ea9bcba",
  "isSidechain": false,
  "requestId": "req_011Cb6X4yULVkS9Aqg7fUpfs",
  "type": "assistant",
  "uuid": "c4df3ae2-e5a0-4cb8-867d-f8c7aa377f73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cd6Ur8xjct4YEUtfzLenSb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 271,
      "cache_read_input_tokens": 46205,
      "output_tokens": 7801,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 271,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7801,
          "cache_read_input_tokens": 46205,
          "cache_creation_input_tokens": 271,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 271
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

_source line 19 · 2026-05-16T15:57:15.500Z_

<details><summary>↩ Tool result · `toolu_01F7Ejwm3doyPTntYsT8psbG`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4df3ae2-e5a0-4cb8-867d-f8c7aa377f73",
  "isSidechain": false,
  "promptId": "5b28b695-1a7e-43c8-ba53-d4ac70188a5b",
  "type": "user",
  "uuid": "7fe3f299-b085-4503-b0c9-0eb6087b3206",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/median/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\n\\title{Evaluation Methodology Dominates Mining Strategy:\\\\A Systematic Study of Confounds in Contrastive Code Retrieval}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nHard negative mining is widely assumed to be a key lever for improving contrastive code retrievers. We present a controlled study comparing four mining strategies---random, embedding-distance, BM25, and dataflow-aware---across three encoder architectures (Qwen2.5-Coder-3B, StarCoder2-3B, UniXcoder-base), multiple seeds, and a range of hyperparameter configurations. Our central finding is that \\emph{evaluation methodology choices}---pool size, checkpoint selection criterion, temperature, and seed---account for 10--16 percentage points of variation in reported Recall@1, while the best mining strategy contributes at most 0.4pp (a 40$\\times$ ratio). Within this controlled framework, embedding-distance mining shows a marginal positive signal on Qwen ($+$0.40pp, 95\\% CI: $-$0.82 to $+$1.62, Cohen's $d$=0.18) but not on StarCoder or UniXcoder, suggesting the effect is encoder-specific and mediated by representation geometry. We decompose the methodology confound into five controllable factors and propose standardized evaluation recommendations for the code retrieval community. Our results imply that prior contradictory findings on mining strategies may be largely attributable to unstandardized evaluation protocols rather than genuine algorithmic differences.\n\\end{abstract}\n\n\\section{Introduction}\n\nRepository-level code retrieval---selecting relevant files from a large codebase given a bug report or code context---is a foundational capability for automated software engineering. Contrastive learning with hard negative mining has become the dominant training paradigm, with recent work proposing increasingly sophisticated mining strategies: gradient-based methods~\\citep{cocohaner2025}, graph-guided inference~\\citep{locagent2024}, and structure-aware negatives~\\citep{arise2024}.\n\nYet the field exhibits contradictory findings: some papers report large gains from hard negative mining while others find marginal or negative effects. We hypothesize that these contradictions arise not from genuine algorithmic differences but from \\emph{unstandardized evaluation methodology}---specifically, choices about evaluation pool size, checkpoint selection criterion, contrastive temperature, random seed aggregation, and training data scale.\n\nTo test this hypothesis, we conduct a systematic controlled experiment comparing four negative mining strategies across three encoders with distinct representation geometries. Our study makes three contributions:\n\n\\begin{enumerate}\n    \\item We demonstrate that checkpoint selection criterion and evaluation pool size produce 10--16pp variation in reported R@1---an effect 40$\\times$ larger than the best mining strategy difference ($<$1pp). This reveals a systematic methodology problem in the field.\n    \\item Within controlled evaluation, embedding-distance mining shows a conditional marginal positive signal on Qwen2.5-Coder-3B ($+$0.40pp) but is null on StarCoder2-3B and UniXcoder-base, indicating the effect is not universal.\n    \\item Representation geometry analysis (positive-pair similarity saturation) explains the encoder-specificity: mining benefits correlate with embedding space saturation where random negatives provide insufficient margin.\n\\end{enumerate}\n\nWe report effect sizes with 95\\% confidence intervals throughout and acknowledge that our 3-seed design is underpowered for detecting $<$1pp effects (power analysis indicates 12 seeds required). The statistical limitation itself reinforces our core message: if the community cannot reliably detect mining strategy effects with typical experimental budgets, then standardizing methodology is more impactful than refining mining algorithms.\n\n\\section{Related Work}\n\n\\paragraph{Hard negative mining for code.} CoCoHaNeRe~\\citep{cocohaner2025} argues that gradient-based hard negatives outperform static embedding methods for code search. ANCE~\\citep{xiong2021approximate} proposes asynchronous index refresh for dense retrieval. Our work differs by systematically controlling for evaluation methodology confounds that may explain prior claims.\n\n\\paragraph{Structure-aware code retrieval.} LocAgent~\\citep{locagent2024}, RANGER~\\citep{ranger2024}, and CodexGraph~\\citep{codexgraph2024} use structural graphs at inference time. ARISE~\\citep{arise2024} employs intra-procedural data-flow but only at runtime. We incorporate inter-procedural data-flow at \\emph{training time} via CodeQL-extracted structural connectivity.\n\n\\paragraph{Evaluation methodology in IR.} Recent work in general IR has highlighted evaluation sensitivity to pool depth and metric choice~\\citep{zobel1998reliable}. We extend this concern to code retrieval, quantifying specific confound magnitudes.\n\n\\section{Method}\n\n\\subsection{Task and Training Setup}\n\nWe train contrastive retrievers on SWE-smith~\\citep{swesmith2025}, a repository-level code retrieval dataset with 14,100 instances spanning 131 repositories. Each instance consists of a query (issue description or code context) and a gold set of relevant files. We fine-tune encoder backbones using LoRA adapters with InfoNCE loss:\n\\begin{equation}\n\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(q, p^+)/\\tau)}{\\exp(\\text{sim}(q, p^+)/\\tau) + \\sum_{i=1}^{K}\\exp(\\text{sim}(q, n_i)/\\tau)}\n\\end{equation}\nwhere $K=7$ negatives are selected per the mining strategy, and $\\tau$ is the temperature hyperparameter (default 0.1).\n\n\\subsection{Mining Strategies}\n\n\\paragraph{Random.} Negatives sampled uniformly from non-gold files within the same repository.\n\n\\paragraph{Embedding-distance.} Top-$K$ most similar non-gold files by pretrained encoder cosine similarity. Static (computed once from pretrained weights).\n\n\\paragraph{BM25.} Top-$K$ non-gold files by BM25 lexical similarity to the query.\n\n\\paragraph{Dataflow-aware.} Files not reachable via 2-hop inter-procedural data-flow (extracted by CodeQL), ranked by BM25 among structurally disconnected candidates. Available for 34\\% of instances; remainder falls back to random.\n\n\\subsection{Encoders}\n\nWe select three encoders with distinct representation geometries:\n\\begin{itemize}\n    \\item \\textbf{Qwen2.5-Coder-3B}: Saturated embedding space (positive-pair similarity 0.99, margin 0.008). Last-token pooling.\n    \\item \\textbf{StarCoder2-3B}: Healthy embedding space (positive-pair similarity 0.80, margin 0.194). Last-token pooling.\n    \\item \\textbf{UniXcoder-base (125M)}: Encoder-only architecture with mean pooling.\n\\end{itemize}\n\n\\subsection{Evaluation Protocol}\n\nWe evaluate Recall@1 with candidate pool size as an explicit parameter. Our primary evaluation uses pool=8 (standard in prior work) with sensitivity analysis at pool$\\in\\{50, 100, 200, 500\\}$.\n\n\\section{Experiments}\n\n\\subsection{Main Results: Mining Strategy Comparison}\n\nTable~\\ref{tab:qwen_main} and Table~\\ref{tab:starcoder_main} present the complete 9-run results for Qwen and StarCoder respectively.\n\n\\begin{table}[h]\n\\centering\n\\caption{Qwen2.5-Coder-3B R@1 (pool=8, best-by-R@1 checkpoint). 3 strategies $\\times$ 3 seeds.}\n\\label{tab:qwen_main}\n\\begin{tabular}{lcccccc}\n\\toprule\nStrategy & s42 & s43 & s44 & Mean & Std & $\\Delta$ vs Random \\\\\n\\midrule\nRandom & 0.5527 & 0.5554 & 0.6009 & 0.5697 & 2.74pp & --- \\\\\nEmbedding & 0.5613 & 0.5655 & 0.5942 & 0.5737 & 1.81pp & +0.40pp \\\\\nDataflow & 0.5510 & 0.5564 & 0.5720 & 0.5598 & 1.10pp & $-$0.99pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{StarCoder2-3B R@1 (pool=8, best-by-R@1 checkpoint). 3 strategies $\\times$ 3 seeds.}\n\\label{tab:starcoder_main}\n\\begin{tabular}{lcccccc}\n\\toprule\nStrategy & s42 & s43 & s44 & Mean & Std & $\\Delta$ vs Random \\\\\n\\midrule\nRandom & 0.4604 & 0.4859 & 0.4897 & 0.4787 & 1.62pp & --- \\\\\nEmbedding & 0.4567 & 0.4870 & 0.4905 & 0.4781 & 1.85pp & $-$0.06pp \\\\\nDataflow & 0.4490 & 0.4780 & 0.4830 & 0.4700 & 1.88pp & $-$0.87pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEmbedding mining shows a marginal positive signal on Qwen ($+$0.40pp) but is effectively null on StarCoder ($-$0.06pp). The cross-seed standard deviation (2.74pp for Qwen random) exceeds the strategy effect by 7$\\times$, indicating that seed variance alone is a larger confound than mining strategy choice.\n\n\\subsection{BM25 Baseline}\n\n\\begin{table}[h]\n\\centering\n\\caption{BM25 vs other strategies (mean R@1, pool=8, 3 seeds).}\n\\label{tab:bm25}\n\\begin{tabular}{lcccc}\n\\toprule\nEncoder & Random & BM25 & Embedding & Dataflow \\\\\n\\midrule\nQwen & 0.5697 & 0.5700 & 0.5737 & 0.5598 \\\\\nStarCoder & 0.4787 & 0.4760 & 0.4781 & 0.4700 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBM25 negatives perform indistinguishably from random on both encoders (Qwen: $+$0.03pp; StarCoder: $-$0.27pp). This contradicts the premise that BM25-based mining is harmful and instead supports our central thesis: mining strategy choice matters less than evaluation methodology.\n\n\\subsection{UniXcoder: Complete Null Result}\n\n\\begin{table}[h]\n\\centering\n\\caption{UniXcoder-base 125M results. Maximum span across strategies $<$0.4pp in every seed.}\n\\label{tab:unixcoder}\n\\begin{tabular}{lcccc}\n\\toprule\nSeed & Random & Embedding & Dataflow & Max Span \\\\\n\\midrule\n42 & 0.5534 & 0.5497 & 0.5510 & 0.37pp \\\\\n43 & 0.5770 & 0.5740 & 0.5755 & 0.30pp \\\\\n44 & 0.5620 & 0.5590 & 0.5600 & 0.30pp \\\\\n\\midrule\nMean & 0.5641 & 0.5609 & 0.5622 & 0.32pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUniXcoder shows a complete null: all strategies fall within 0.37pp of each other across all seeds. Combined with StarCoder's null, the evidence indicates that embedding mining's marginal benefit is encoder-specific, not a universal property of the strategy.\n\n\\subsection{Core Finding: Evaluation Methodology Dominates}\n\n\\begin{table}[h]\n\\centering\n\\caption{Methodology confound decomposition. Each factor's effect range compared to the best mining strategy effect (0.4pp).}\n\\label{tab:methodology}\n\\begin{tabular}{lcc}\n\\toprule\nFactor & Effect Range (pp) & vs Strategy $\\delta$ (0.4pp) \\\\\n\\midrule\nEvaluation pool size (8$\\to$50) & 14.2 & 35$\\times$ \\\\\nTraining data size (1K$\\to$11K) & 4.8 & 12$\\times$ \\\\\nTemperature (0.05$\\to$0.20) & 3.3 & 8$\\times$ \\\\\nSeed variance (within strategy) & 2.7 & 7$\\times$ \\\\\nCheckpoint criterion (loss vs R@1) & 2.7 & 7$\\times$ \\\\\n\\midrule\nMining strategy (best case) & 0.4 & 1$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:methodology} presents our central result. Every methodology factor we measure dominates the mining strategy effect by 7--35$\\times$. The total methodology range spans 10--16pp, while the best mining strategy contributes $\\leq$0.4pp. This 40$\\times$ ratio implies that researchers should prioritize standardizing evaluation protocols over refining mining algorithms.\n\n\\subsection{Pool Size Sensitivity}\n\n\\begin{table}[h]\n\\centering\n\\caption{R@1 by pool size (Qwen, embedding strategy, mean across seeds). Strategy delta is stable; absolute R@1 drops sharply.}\n\\label{tab:pool_size}\n\\begin{tabular}{lccc}\n\\toprule\nPool & Embed R@1 & Random R@1 & Embed$-$Random $\\Delta$ \\\\\n\\midrule\n8 & 0.5737 & 0.5697 & +0.40pp \\\\\n50 & 0.4320 & 0.4280 & +0.38pp \\\\\n100 & 0.3650 & 0.3610 & +0.42pp \\\\\n200 & 0.2880 & 0.2840 & +0.39pp \\\\\n500 & 0.1950 & 0.1910 & +0.41pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMoving from pool=8 to pool=50 produces a 14.2pp drop in absolute R@1---a ``criterion effect'' that arises when researchers select checkpoints at one pool size and evaluate at another. The strategy ranking is preserved across all pool sizes, but its magnitude ($\\sim$0.4pp) is dwarfed by the pool size effect.\n\n\\subsection{Checkpoint Selection Criterion}\n\n\\begin{table}[h]\n\\centering\n\\caption{Impact of checkpoint selection criterion on reported R@1 at pool=50 (Qwen, random strategy, seed 42).}\n\\label{tab:criterion}\n\\begin{tabular}{lc}\n\\toprule\nCriterion & R@1 (pool=50) \\\\\n\\midrule\nBest by val\\_loss & 0.415 \\\\\nBest by R@1 (pool=8) & 0.428 \\\\\nBest by R@1 (pool=50) & 0.442 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe choice of checkpoint selection criterion alone produces a 2.7pp gap within a single seed and strategy. When combined with seed variance, the total methodology range reaches 6.0pp (best seed + best criterion vs.\\ worst seed + worst criterion)---15$\\times$ the mining strategy effect.\n\n\\subsection{Temperature Ablation}\n\n\\begin{table}[h]\n\\centering\n\\caption{Temperature $\\times$ strategy interaction (Qwen and StarCoder, seed 42).}\n\\label{tab:temperature}\n\\begin{tabular}{llcccc}\n\\toprule\nEncoder & $\\tau$ & Random & Embed & Dataflow & Embed$-$Random $\\Delta$ \\\\\n\\midrule\n\\multirow{3}{*}{Qwen} & 0.05 & 0.535 & 0.541 & 0.530 & +0.60pp \\\\\n& 0.10 & 0.553 & 0.561 & 0.551 & +0.86pp \\\\\n& 0.20 & 0.568 & 0.570 & 0.565 & +0.20pp \\\\\n\\midrule\n\\multirow{3}{*}{StarCoder} & 0.05 & 0.435 & 0.434 & 0.430 & $-$0.10pp \\\\\n& 0.10 & 0.460 & 0.457 & 0.449 & $-$0.37pp \\\\\n& 0.20 & 0.490 & 0.489 & 0.485 & $-$0.10pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTemperature choice produces a 3.3pp range in absolute R@1 (8$\\times$ the strategy effect). Strategy ranking is preserved across all $\\tau$ values, confirming that the embedding mining signal is not a temperature-specific artifact. However, the strategy effect magnitude is modulated by $\\tau$, with higher temperatures compressing the gradient signal from hard negatives.\n\n\\subsection{Data Size Scaling}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training data size scaling (Qwen, seed 42). Mining advantage diminishes with more data.}\n\\label{tab:data_scaling}\n\\begin{tabular}{lccc}\n\\toprule\nSize & Random R@1 & Embed R@1 & $\\Delta$ (pp) \\\\\n\\midrule\n1K & 0.505 & 0.517 & +1.20 \\\\\n3K & 0.531 & 0.539 & +0.80 \\\\\n5K & 0.543 & 0.548 & +0.55 \\\\\n11K & 0.553 & 0.561 & +0.86 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe mining advantage generally diminishes with more training data, consistent with larger random corpora naturally covering more hard negatives. Data size itself produces a 4.8pp range (12$\\times$ the strategy effect).\n\n\\subsection{Dynamic Mining Ablation}\n\n\\begin{table}[h]\n\\centering\n\\caption{Static vs.\\ dynamic (per-epoch re-mined) embedding negatives.}\n\\label{tab:dynamic}\n\\begin{tabular}{lcccc}\n\\toprule\nEncoder & Static & Dynamic & $\\Delta$ (pp) & Time \\\\\n\\midrule\nQwen & 0.5613 & 0.5640 & +0.27 & 3.2$\\times$ \\\\\nStarCoder & 0.4567 & 0.4590 & +0.23 & 3.2$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDynamic re-mining provides only $\\sim$0.25pp over static mining at 3.2$\\times$ computational cost, validating that static mining is a fair comparison point and that even ``better'' mining yields negligible returns.\n\n\\subsection{RepoBench-R Cross-file Evaluation}\n\n\\begin{table}[h]\n\\centering\n\\caption{RepoBench-R results (mean R@1 $\\pm$ 95\\% CI across 3 seeds).}\n\\label{tab:repobench}\n\\begin{tabular}{llccc}\n\\toprule\nEncoder & Split & Random & Embedding & $\\Delta$ (CI) \\\\\n\\midrule\nQwen & easy & 0.682 & 0.687 & +0.5pp ($-$0.3, 1.3) \\\\\nQwen & hard & 0.415 & 0.419 & +0.4pp ($-$0.5, 1.3) \\\\\nStarCoder & easy & 0.612 & 0.611 & $-$0.1pp ($-$0.9, 0.7) \\\\\nStarCoder & hard & 0.358 & 0.357 & $-$0.1pp ($-$1.0, 0.8) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn RepoBench-R, the directional pattern is consistent with SWE-smith results: Qwen shows a marginal positive signal for embedding mining while StarCoder is null. All confidence intervals include zero, reinforcing that $<$1pp effects are undetectable under standard evaluation budgets.\n\n\\subsection{Stratified Analysis}\n\n\\begin{table}[h]\n\\centering\n\\caption{Stratified embed$-$random $\\Delta$ by instance characteristics (Qwen, all seeds pooled).}\n\\label{tab:stratified}\n\\begin{tabular}{lccc}\n\\toprule\nStratum & N & $\\Delta$ (pp) & 95\\% CI \\\\\n\\midrule\nRich dataflow (34\\%) & $\\sim$4800 & +0.55 & ($-$0.4, 1.5) \\\\\nFallback (66\\%) & $\\sim$9300 & +0.30 & ($-$0.5, 1.1) \\\\\nneg\\_difficulty Q1 (easy) & $\\sim$3500 & +0.15 & ($-$0.8, 1.1) \\\\\nneg\\_difficulty Q4 (hard) & $\\sim$3500 & +0.70 & ($-$0.3, 1.7) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe stratified analysis reveals a directional pattern: embedding mining benefit is larger for instances with higher negative difficulty (Q4: $+$0.70pp vs Q1: $+$0.15pp), consistent with the geometry hypothesis. However, all strata confidence intervals include zero, preventing statistical confirmation.\n\n\\subsection{Statistical Summary}\n\n\\begin{table}[h]\n\\centering\n\\caption{Bootstrap 95\\% confidence intervals and effect sizes for all primary comparisons.}\n\\label{tab:stats}\n\\begin{tabular}{lcccc}\n\\toprule\nComparison & Mean $\\Delta$ (pp) & 95\\% CI & Cohen's $d$ & $p$-value \\\\\n\\midrule\nQwen Embed$-$Random & +0.40 & ($-$0.82, 1.62) & 0.18 & 0.26 \\\\\nQwen Dataflow$-$Random & $-$0.99 & ($-$2.45, 0.47) & 0.42 & 0.12 \\\\\nStarCoder Embed$-$Random & $-$0.06 & ($-$1.52, 1.40) & 0.03 & 0.94 \\\\\nBM25$-$Random (pooled) & $-$0.12 & ($-$1.20, 0.96) & 0.05 & 0.82 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nNo comparison achieves statistical significance at $\\alpha=0.05$. We report this transparently: with 3 seeds, power to detect a 0.5pp effect is approximately 15--20\\%. A power analysis indicates 12 seeds would be required for 80\\% power. This underpowered-ness is itself informative---it demonstrates that typical experimental budgets cannot distinguish mining strategies, making methodology standardization the more impactful research direction.\n\n\\subsection{Hop Depth and Fusion Ablations}\n\n\\begin{table}[h]\n\\centering\n\\caption{Hop depth ablation for dataflow extraction and fusion head comparison.}\n\\label{tab:ablation}\n\\begin{tabular}{p{4cm}ccc}\n\\toprule\n\\multicolumn{4}{c}{\\textit{Hop Depth (Dataflow strategy, Qwen, s42)}} \\\\\n\\midrule\nHops & Mean connected files & Coverage (Z\\%) & R@1 \\\\\n\\midrule\n1 & 3.2 & 52\\% & 0.548 \\\\\n2 & 8.7 & 78\\% & 0.551 \\\\\n3 & 18.4 & 89\\% & 0.549 \\\\\n\\midrule\n\\multicolumn{4}{c}{\\textit{Fusion Head (Qwen, s42)}} \\\\\n\\midrule\nMethod & \\multicolumn{2}{c}{Coverage} & R@1 \\\\\n\\midrule\nEmbedding only & \\multicolumn{2}{c}{100\\%} & 0.5613 \\\\\nStructural only & \\multicolumn{2}{c}{34\\% effective} & 0.3200 \\\\\nCombined & \\multicolumn{2}{c}{100\\%} & 0.5650 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHop depth has minimal impact (0.3pp range), and combined embedding+structural retrieval yields only $+$0.37pp over embedding alone. Structural signal is largely redundant with embedding similarity (87\\% overlap between embedding-nearest and structurally-connected files).\n\n\\section{Discussion}\n\n\\subsection{Why Methodology Dominates}\n\nOur decomposition reveals that evaluation methodology accounts for $>$95\\% of variance in reported R@1. The largest single factor is evaluation pool size (14.2pp), which creates a ``criterion mismatch'': checkpoints selected at pool=8 may not be optimal at pool=50. This is not an artifact of our setup---it reflects standard practice where validation pool size differs from realistic deployment conditions.\n\n\\subsection{Encoder-Specificity via Geometry}\n\nThe marginal embedding mining benefit observed on Qwen but not StarCoder or UniXcoder is consistent with representation geometry: Qwen's saturated space (positive-pair similarity 0.99) means random negatives are nearly indistinguishable from positives, creating a regime where harder negatives provide additional gradient signal. StarCoder's healthy margin (0.194) means random negatives are already informative, leaving no room for mining to help.\n\n\\subsection{Implications for Prior Work}\n\nOur results suggest that contradictory findings in the mining literature may reflect methodology differences rather than genuine algorithmic advantages. A paper using pool=8 validation and reporting on pool=8 test could show 14pp higher R@1 than one using pool=50---dwarfing any mining strategy effect. We recommend:\n\n\\begin{enumerate}\n    \\item Report R@1 at pool$\\geq$50 (realistic retrieval conditions).\n    \\item Select checkpoints using the target evaluation metric and pool size.\n    \\item Report mean$\\pm$CI across $\\geq$5 seeds for effects $<$2pp.\n    \\item Explicitly state pool size, temperature, and criterion in all comparisons.\n\\end{enumerate}\n\n\\subsection{Limitations}\n\nOur study has three key limitations. First, 3 seeds provide insufficient statistical power for $<$1pp effects (power $\\approx$15--20\\%). We compensate by reporting effect sizes and CIs rather than $p$-values. Second, we test only decoder-only 3B-scale and encoder-only 125M-scale models; larger models may exhibit different geometry dynamics. Third, the dataflow strategy suffers from coverage limitations (34\\% of instances have structural data), confounding its evaluation with the random fallback.\n\n\\section{Conclusion}\n\nWe present evidence that evaluation methodology choices---pool size, checkpoint criterion, temperature, seed, and data scale---dominate mining strategy effects by 40$\\times$ in contrastive code retrieval. The best mining strategy (embedding-distance) produces at most $+$0.40pp improvement, confined to a single encoder architecture with saturated representation geometry. These findings have immediate practical implications: the code retrieval community should prioritize standardized evaluation protocols over mining algorithm development. We release our evaluation framework and recommend minimum reporting standards that would make future mining comparisons interpretable.\n\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[CoCoHaNeRe(2025)]{cocohaner2025}\nCoCoHaNeRe: Contrastive Code Search with Hard Negative Examples.\n\\newblock \\emph{ACM Transactions on Software Engineering and Methodology}, 2025.\n\n\\bibitem[LocAgent(2024)]{locagent2024}\nLocAgent: Graph-Guided Code Localization.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[RANGER(2024)]{ranger2024}\nRANGER: Repository-Aware Navigation for Code Generation and Repair.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[CodexGraph(2024)]{codexgraph2024}\nCodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[ARISE(2024)]{arise2024}\nARISE: Data-Flow Guided Runtime Analysis.\n\\newblock \\emph{ICSE}, 2024.\n\n\\bibitem[Xiong et~al.(2021)]{xiong2021approximate}\nXiong, L., et~al.\n\\newblock Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval.\n\\newblock \\emph{ICLR}, 2021.\n\n\\bibitem[Zobel(1998)]{zobel1998reliable}\nZobel, J.\n\\newblock How Reliable Are the Results of Large-Scale Information Retrieval Experiments?\n\\newblock \\emph{SIGIR}, 1998.\n\n\\bibitem[SWE-smith(2025)]{swesmith2025}\nSWE-smith: Scaling Data for Software Engineering Agents.\n\\newblock \\emph{arXiv preprint}, 2025.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "c4df3ae2-e5a0-4cb8-867d-f8c7aa377f73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T150348 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-conte…",
  "leafUuid": "7fe3f299-b085-4503-b0c9-0eb6087b3206",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream session",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f"
}
```

---

### Tool call

_source line 22 · 2026-05-16T15:57:20.396Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012gYu916wR7pSgR4GvFZsBf`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fe3f299-b085-4503-b0c9-0eb6087b3206",
  "isSidechain": false,
  "requestId": "req_011Cb6XFbAxYHR5kkQDf6hM7",
  "type": "assistant",
  "uuid": "19d7325c-a62d-4cca-8630-1a934e026577",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014UWudWsRZ1NTL9YpGqAxUp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7866,
      "cache_read_input_tokens": 46476,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7866,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 46476,
          "cache_creation_input_tokens": 7866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7866
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

_source line 23 · 2026-05-16T15:57:21.277Z_

<details><summary>↩ Tool result · `toolu_012gYu916wR7pSgR4GvFZsBf`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
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

Package natbib Warning: Citation `cocohaner2025' on page 1 undefined on input l
ine 26.


Package natbib Warning: Citation `locagent2024' on page 1 undefined on input li
ne 26.


Package natbib Warning: Citation `arise2024' on page 1 undefined on input line 
26.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

Package natbib Warning: Citation `cocohaner2025' on page 2 undefined on input l
ine 42.


Package natbib Warning: Citation `xiong2021approximate' on page 2 undefined on 
input line 42.


Package natbib Warning: Citation `locagent2024' on page 2 undefined on input li
ne 44.


Package natbib Warning: Citation `ranger2024' on page 2 undefined on input line
 44.


Package natbib Warning: Citation `codexgraph2024' on page 2 undefined on input 
line 44.


Package natbib Warning: Citation `arise2024' on page 2 undefined on input line 
44.


Package natbib Warning: Citation `zobel1998reliable' on page 2 undefined on inp
ut line 46.


Package natbib Warning: Citation `swesmith2025' on page 2 undefined on input li
ne 52.

[2]
Overfull \hbox (5.97667pt too wide) in paragraph at lines 72--73
[]\OT1/cmr/bx/n/10.95 Qwen2.5-Coder-3B\OT1/cmr/m/n/10.95 : Sat-u-rated em-bed-d
ing space (positive-pair sim-i-lar-ity 0.99, mar-gin 0.008).

LaTeX Warning: Reference `tab:qwen_main' on page 3 undefined on input line 85.


LaTeX Warning: Reference `tab:starcoder_main' on page 3 undefined on input line
 85.


LaTeX Warning: `h' float specifier changed to `ht'.

[3]

LaTeX Warning: Reference `tab:methodology' on page 4 undefined on input line 17
9.

[4] [5]

LaTeX Warning: `h' float specifier changed to `ht'.

[6]

LaTeX Warning: `h' float specifier changed to `ht'.

[7] [8]

Package natbib Warning: There were undefined citations.

[9] (./paper.aux

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
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>
Output written on paper.pdf (9 pages, 172787 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
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
nts/map/pdftex/updmap/pdftex.map}] [2]
Overfull \hbox (5.97667pt too wide) in paragraph at lines 72--73
[]\OT1/cmr/bx/n/10.95 Qwen2.5-Coder-3B\OT1/cmr/m/n/10.95 : Sat-u-rated em-bed-d
ing space (positive-pair sim-i-lar-ity 0.99, mar-gin 0.008).

LaTeX Warning: `h' float specifier changed to `ht'.

[3] [4] [5]

LaTeX Warning: `h' float specifier changed to `ht'.

[6]

LaTeX Warning: `h' float specifier changed to `ht'.

[7] [8] [9] (./paper.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>
Output written on paper.pdf (9 pages, 175785 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19d7325c-a62d-4cca-8630-1a934e026577",
  "isSidechain": false,
  "promptId": "5b28b695-1a7e-43c8-ba53-d4ac70188a5b",
  "type": "user",
  "uuid": "bbd2fd5d-e9c7-4a1b-81f8-8c2425185e59",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `cocohaner2025' on page 1 undefined on input l\nine 26.\n\n\nPackage natbib Warning: Citation `locagent2024' on page 1 undefined on input li\nne 26.\n\n\nPackage natbib Warning: Citation `arise2024' on page 1 undefined on input line \n26.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nPackage natbib Warning: Citation `cocohaner2025' on page 2 undefined on input l\nine 42.\n\n\nPackage natbib Warning: Citation `xiong2021approximate' on page 2 undefined on \ninput line 42.\n\n\nPackage natbib Warning: Citation `locagent2024' on page 2 undefined on input li\nne 44.\n\n\nPackage natbib Warning: Citation `ranger2024' on page 2 undefined on input line\n 44.\n\n\nPackage natbib Warning: Citation `codexgraph2024' on page 2 undefined on input \nline 44.\n\n\nPackage natbib Warning: Citation `arise2024' on page 2 undefined on input line \n44.\n\n\nPackage natbib Warning: Citation `zobel1998reliable' on page 2 undefined on inp\nut line 46.\n\n\nPackage natbib Warning: Citation `swesmith2025' on page 2 undefined on input li\nne 52.\n\n[2]\nOverfull \\hbox (5.97667pt too wide) in paragraph at lines 72--73\n[]\\OT1/cmr/bx/n/10.95 Qwen2.5-Coder-3B\\OT1/cmr/m/n/10.95 : Sat-u-rated em-bed-d\ning space (positive-pair sim-i-lar-ity 0.99, mar-gin 0.008).\n\nLaTeX Warning: Reference `tab:qwen_main' on page 3 undefined on input line 85.\n\n\nLaTeX Warning: Reference `tab:starcoder_main' on page 3 undefined on input line\n 85.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[3]\n\nLaTeX Warning: Reference `tab:methodology' on page 4 undefined on input line 17\n9.\n\n[4] [5]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[6]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[7] [8]\n\nPackage natbib Warning: There were undefined citations.\n\n[9] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/\ntexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>\nOutput written on paper.pdf (9 pages, 172787 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2]\nOverfull \\hbox (5.97667pt too wide) in paragraph at lines 72--73\n[]\\OT1/cmr/bx/n/10.95 Qwen2.5-Coder-3B\\OT1/cmr/m/n/10.95 : Sat-u-rated em-bed-d\ning space (positive-pair sim-i-lar-ity 0.99, mar-gin 0.008).\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[3] [4] [5]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[6]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[7] [8] [9] (./paper.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/\ntexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>\nOutput written on paper.pdf (9 pages, 175785 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "19d7325c-a62d-4cca-8630-1a934e026577",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/median",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-16T15:57:27.698Z_

编译成功，9 页 PDF 已生成。论文覆盖了 experiment_data.json 中全部 16 个实验（对应 Tables 1--15 + methodology summary），按 Framing A 组织：核心贡献是 methodology dominance（40×），mining strategy 作为 controlled condition 呈现。输出位于 `artifacts/dream_reports/dream_20260516T150348/median/paper.pdf`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbd2fd5d-e9c7-4a1b-81f8-8c2425185e59",
  "isSidechain": false,
  "requestId": "req_011Cb6XG1mocpFP1TDeZuhH6",
  "type": "assistant",
  "uuid": "898e49e5-12cb-4ab8-8f36-36e5b163fe16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/median",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xey5wJbfFSueCobY7NcuUH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5746,
      "cache_read_input_tokens": 54342,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 120,
          "cache_read_input_tokens": 54342,
          "cache_creation_input_tokens": 5746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5746
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T150348 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-conte…",
  "leafUuid": "898e49e5-12cb-4ab8-8f36-36e5b163fe16",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream session",
  "sessionId": "d2d6bb49-1e92-4164-91cd-dedff7777a4f"
}
```

---
