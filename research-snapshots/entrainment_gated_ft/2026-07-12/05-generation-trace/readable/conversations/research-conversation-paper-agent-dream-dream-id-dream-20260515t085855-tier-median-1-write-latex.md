# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T085855 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/2c174715-22f6-4523-8f31-a43aaee0d5be.jsonl`
- **Structured JSON:** [`e3644c10c265bf8067df.json`](../../sessions/e3/e3644c10c265bf8067df.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T09:50:24.395Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T09:50:24.395Z",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T085855 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Claim 3 保持 \"empirical decision rule\"（不升级）。14B 作为 boundary case  单独一段讨论：threshold 是 soft boundary 而非 hard cutoff。 Decision rule 5/6（14B 是 type-II error），承认 rule 是 directional heuristic， Limitation 明确写 \"N=1 confirmed Spread; boundary behavior is continuous, not binary.\" 三档标签仍可用但 threshold 软化（\"approximately 0.50\" → \"in the range 0.45-0.55\"）。 Gemma-2 段落微调 BOS-fixed 数字但叙事不变。 W9 super-additive 降为 empirical observation（图+描述性文字），不写 formal proposition。 Contribution 重心从 \"diagnostic\" 向 \"constraint as universal fix\" 倾斜。 仍可投 EMNLP Main。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T09:50:24.399Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T09:50:24.399Z",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be"
}
```

---

## Round 1

37 recorded events

### User

_source line 3 · 2026-05-15T09:50:24.430Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T085855 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Claim 3 保持 "empirical decision rule"（不升级）。14B 作为 boundary case  单独一段讨论：threshold 是 soft boundary 而非 hard cutoff。 Decision rule 5/6（14B 是 type-II error），承认 rule 是 directional heuristic， Limitation 明确写 "N=1 confirmed Spread; boundary behavior is continuous, not binary." 三档标签仍可用但 threshold 软化（"approximately 0.50" → "in the range 0.45-0.55"）。 Gemma-2 段落微调 BOS-fixed 数字但叙事不变。 W9 super-additive 降为 empirical observation（图+描述性文字），不写 formal proposition。 Contribution 重心从 "diagnostic" 向 "constraint as universal fix" 倾斜。 仍可投 EMNLP Main。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "9b38a89f-3817-47d6-8645-8990dd1a76c4",
  "type": "user",
  "uuid": "52d9c6cf-d24c-4e36-8747-0d692f07c46e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T09:50:24.430Z_

```json
{
  "parentUuid": "52d9c6cf-d24c-4e36-8747-0d692f07c46e",
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
  "uuid": "a3b777ed-a10f-4d66-b985-820ad5a07531",
  "timestamp": "2026-05-15T09:50:24.430Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T09:50:24.430Z_

```json
{
  "parentUuid": "a3b777ed-a10f-4d66-b985-820ad5a07531",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4cc5217b-b193-4e10-9f8c-e0f93976c775",
  "timestamp": "2026-05-15T09:50:24.430Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier research paper simulation",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be"
}
```

---

### Assistant

_source line 7 · 2026-05-15T09:50:26.866Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cc5217b-b193-4e10-9f8c-e0f93976c775",
  "isSidechain": false,
  "requestId": "req_011Cb49U9JkhFt49GKTd8C4a",
  "type": "assistant",
  "uuid": "59fbc433-ff29-418a-acb1-4021fb53667d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013BStfiLqVA6jviVLt26mNz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12160,
      "cache_read_input_tokens": 11841,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12160,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 200,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12160,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12160
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

_source line 8 · 2026-05-15T09:50:27.353Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XZaNHzaYmNL49jWvx3HjMv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59fbc433-ff29-418a-acb1-4021fb53667d",
  "isSidechain": false,
  "requestId": "req_011Cb49U9JkhFt49GKTd8C4a",
  "type": "assistant",
  "uuid": "14a7591d-09a2-4b99-821c-c3dc06f9e9ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013BStfiLqVA6jviVLt26mNz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12160,
      "cache_read_input_tokens": 11841,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12160,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 200,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12160,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12160
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

_source line 9 · 2026-05-15T09:50:27.655Z_

<details><summary>↩ Tool result · `toolu_01XZaNHzaYmNL49jWvx3HjMv`</summary>

```text
1	[
2	  {
3	    "name": "Qwen2.5-14B hires 2-bit-only profiling",
4	    "description": "High-resolution profiling (64 seq × 2048 tok) on Qwen2.5-14B (48L × 8KV = 384 heads, GQA 5:1). Measure per-head 2-bit distortion delta, compute concentration and t₁/t₅. Tests whether Qwen-7B's Spread pattern generalizes within family at larger scale.\n",
5	    "results": {
6	      "calibration_baseline_ppl": 5.8432,
7	      "test_baseline_bf16_ppl": 6.5,
8	      "total_kv_heads": 384,
9	      "top5pct_n_heads": 19,
10	      "top5_concentration": 0.47,
11	      "t1_t5": 0.72,
12	      "delta_2bit_cv": 3.85,
13	      "l0_dominance_ratio": 0.38,
14	      "top1_head": "L0H0",
15	      "top1_delta_2bit": 3.21,
16	      "top2_head": "L0H3",
17	      "top2_delta_2bit": 2.78,
18	      "top3_head": "L0H5",
19	      "top3_delta_2bit": 2.14,
20	      "top4_head": "L8H2",
21	      "top4_delta_2bit": 1.82,
22	      "top5_head": "L0H1",
23	      "top5_delta_2bit": 1.53,
24	      "l0_heads_in_top19": 5,
25	      "positive_delta_heads": 378,
26	      "distribution_shape": "diluted_spread",
27	      "profiling_time_hours": 3.5
28	    },
29	    "tables": [
30	      {
31	        "title": "Qwen2.5-14B top-10 sensitive heads (hires 2-bit delta)",
32	        "columns": [
33	          "head",
34	          "delta_2bit"
35	        ],
36	        "rows": [
37	          [
38	            "L0H0",
39	            3.21
40	          ],
41	          [
42	            "L0H3",
43	            2.78
44	          ],
45	          [
46	            "L0H5",
47	            2.14
48	          ],
49	          [
50	            "L8H2",
51	            1.82
52	          ],
53	          [
54	            "L0H1",
55	            1.53
56	          ],
57	          [
58	            "L12H6",
59	            1.31
60	          ],
61	          [
62	            "L0H7",
63	            1.18
64	          ],
65	          [
66	            "L5H4",
67	            0.98
68	          ],
69	          [
70	            "L15H1",
71	            0.87
72	          ],
73	          [
74	            "L0H2",
75	            0.82
76	          ]
77	        ]
78	      }
79	    ],
80	    "figures": [],
81	    "analysis": "关键发现：concentration 0.47 和 t₁/t₅ 0.72 都恰好 miss joint condition （conc < 0.50 AND t₁/t₅ > 0.70）。这不是 Spread 也不是 Flat—— 是 \"diluted spread\"，joint condition 边界上的 continuous behavior。 14B 的 GQA 5:1（vs 7B 的 7:1）可能是稀释的结构性因素之一： 每层 8 个 KV heads 比 4 个更均匀，L0 cluster 效应被分散。\n\n\nQwen2.5-14B 同属 Qwen2.5 家族，L0 敏感 cluster 的 architectural pattern 大概率保留。 但 14B 有 384 个 KV head（vs 7B 的 112），top-5% 从 ~6 heads 扩至 19 heads。 L0 的 8 个 head 中 ~5 个出现在 top-19，但 L0 只占 top-19 的 26%（5/19）， 其余 14 头散布在中层（L5-L15），导致 concentration 从 7B 的 0.61 下降至 0.47—— 恰好落在 0.50 threshold 以下。 同时，L0 内部虽有多头敏感，但最强头（L0H0, delta=3.21）相对 top-5 heads 的占比上升 （t₁/t₅=0.72 vs 7B 的 0.57），因为中层 heads 稀释了 top-5 中非 L0 头的贡献。 整体呈现 \"diluted spread\"：L0 cluster 存在但在全局分布中被稀释。 CV=3.85 高于 flat 模型（Mistral 1.31, Gemma-2 1.28）但低于 7B 的数值， 进一步佐证 heterogeneity 介于 Spread 和 Flat 之间。\n"
82	  },
83	  {
84	    "name": "Qwen2.5-14B constrained MCKP eval + k ablation",
85	    "description": "Constrained MCKP on Qwen2.5-14B at budget=0.25 (4× compression)。 Sweep k ∈ {0,4,8,12,16,20,24,32,48} 寻找 optimal max_2bit。 Verify greedy = MCKP at optimal k (solver equivalence).\n",
86	    "results": {
87	      "baseline_bf16_ppl": 6.5,
88	      "uniform_4bit_ppl": 7.8,
89	      "uniform_baseline_ratio": 1.2,
90	      "constrained_mckp_ppl": 7.18,
91	      "mckp_improvement_over_uniform_pct": 7.9,
92	      "greedy_constrained_ppl": 7.18,
93	      "greedy_mckp_delta": 0.0,
94	      "optimal_k": 12,
95	      "gap_recovery_pct": 47.7,
96	      "bit_distribution": {
97	        "2": 12,
98	        "4": 366,
99	        "8": 6
100	      },
101	      "memory_ratio": 0.25,
102	      "k_ablation": {
103	        "k0": 7.8,
104	        "k4": 7.52,
105	        "k8": 7.28,
106	        "k12": 7.18,
107	        "k16": 7.21,
108	        "k20": 7.28,
109	        "k24": 7.38,
110	        "k32": 7.65,
111	        "k48": 8.42
112	      }
113	    },
114	    "tables": [
115	      {
116	        "title": "Qwen2.5-14B k ablation (384 KV heads, budget=0.25)",
117	        "columns": [
118	          "k (max_2bit)",
119	          "PPL",
120	          "note"
121	        ],
122	        "rows": [
123	          [
124	            0,
125	            7.8,
126	            "= uniform 4-bit"
127	          ],
128	          [
129	            4,
130	            7.52,
131	            ""
132	          ],
133	          [
134	            8,
135	            7.28,
136	            ""
137	          ],
138	          [
139	            12,
140	            7.18,
141	            "optimal ✓"
142	          ],
143	          [
144	            16,
145	            7.21,
146	            ""
147	          ],
148	          [
149	            20,
150	            7.28,
151	            ""
152	          ],
153	          [
154	            24,
155	            7.38,
156	            ""
157	          ],
158	          [
159	            32,
160	            7.65,
161	            "compounding visible"
162	          ],
163	          [
164	            48,
165	            8.42,
166	            "compounding dominant"
167	          ]
168	        ]
169	      },
170	      {
171	        "title": "Qwen2.5-14B allocation comparison",
172	        "columns": [
173	          "method",
174	          "PPL",
175	          "vs uniform"
176	        ],
177	        "rows": [
178	          [
179	            "Baseline bf16",
180	            6.5,
181	            "—"
182	          ],
183	          [
184	            "Uniform 4-bit",
185	            7.8,
186	            "—"
187	          ],
188	          [
189	            "MCKP constrained k=12",
190	            7.18,
191	            "+7.9%"
192	          ],
193	          [
194	            "Greedy constrained k=12",
195	            7.18,
196	            "Δ=0.0000 vs MCKP"
197	          ]
198	        ]
199	      }
200	    ],
201	    "figures": [],
202	    "analysis": "7.9% 改善远超 noise range（Gemma-2 -0.35%, Mistral -0.48%）， 是 genuine positive signal。但也远低于 7B 的 27.3%—— 这正是 median tier 的核心预期：borderline positive，不足以升级 N=1 Spread claim。 k=12 到 k=20 接近 plateau（PPL Δ < 0.10），说明 sensitivity 分布比 7B 更平滑。 论文中 14B 应呈现为 \"the benefit of non-uniform allocation degrades gracefully as concentration decreases, confirming the diagnostic as a continuous predictor rather than a binary classifier.\"\n\n\nUniform 4-bit degradation ratio 1.20×——低于 7B 的 1.575× 但显著高于 Flat 模型的 1.01-1.05×。 原因：14B 的 L0 cluster 虽然被稀释（concentration 0.47 vs 0.61）， 但仍包含 ~5 个高敏感头，被迫 4-bit 时产生可观的 degradation。 MCKP 将 top-12 敏感头从 4-bit 降至 2-bit 并将 6 个最敏感头升至 8-bit， 利用这部分 heterogeneity 获得 7.9% 改善——有意义但远低于 7B 的 27.3%。 k-PPL curve 呈浅 U 型：minimum 在 k=12（≈top-5% 的 63%）， compounding onset 在 k>32 后缓慢上升。U 型深度 (7.80-7.18=0.62) 远小于 7B 的 (15.45-10.91=4.54)， 反映可利用的 sensitivity budget 更少。 Solver equivalence 仍然成立（greedy = MCKP，Δ=0.0000）， constraint 是 primary intervention 的 claim 在 14B 上同样成立。 Recovery 47.7% 低于 7B 的 80.8%，与 concentration 的衰减定量一致。\n"
203	  },
204	  {
205	    "name": "Qwen2.5-14B unconstrained solver eval",
206	    "description": "Run unconstrained greedy and MCKP on Qwen2.5-14B. Measure compounding degradation, 2-bit head count, and ratio vs baseline.\n",
207	    "results": {
208	      "baseline_bf16_ppl": 6.5,
209	      "uniform_4bit_ppl": 7.8,
210	      "greedy_unconstrained_ppl": 10.15,
211	      "mckp_unconstrained_ppl": 10.35,
212	      "greedy_ratio_vs_baseline": 1.562,
213	      "mckp_ratio_vs_baseline": 1.592,
214	      "n_2bit_greedy": 58,
215	      "n_2bit_mckp": 62,
216	      "pct_2bit_greedy": 15.1,
217	      "pct_2bit_mckp": 16.1,
218	      "greedy_bit_distribution": {
219	        "2": 58,
220	        "4": 318,
221	        "8": 6,
222	        "16": 2
223	      },
224	      "constrained_improvement_vs_unconstrained_pct": 29.3
225	    },
226	    "tables": [
227	      {
228	        "title": "Qwen2.5-14B unconstrained vs constrained comparison",
229	        "columns": [
230	          "method",
231	          "PPL",
232	          "×baseline",
233	          "2-bit heads (%)"
234	        ],
235	        "rows": [
236	          [
237	            "Baseline bf16",
238	            6.5,
239	            "1.00×",
240	            "—"
241	          ],
242	          [
243	            "Uniform 4-bit",
244	            7.8,
245	            "1.20×",
246	            "0 (0%)"
247	          ],
248	          [
249	            "Greedy unconstrained",
250	            10.15,
251	            "1.56×",
252	            "58 (15.1%)"
253	          ],
254	          [
255	            "MCKP unconstrained",
256	            10.35,
257	            "1.59×",
258	            "62 (16.1%)"
259	          ],
260	          [
261	            "Greedy constrained k=12",
262	            7.18,
263	            "1.10×",
264	            "12 (3.1%)"
265	          ],
266	          [
267	            "MCKP constrained k=12",
268	            7.18,
269	            "1.10×",
270	            "12 (3.1%)"
271	          ]
272	        ]
273	      }
274	    ],
275	    "figures": [],
276	    "analysis": "14B 的 1.56× 填补三档分类的关键空白： 现有 \"moderate\" 只有 Gemma-2（1.47×），14B 提供第二个数据点（1.56×）， 使 catastrophic（3.31×）- moderate（1.47-1.56×）- mild（1.07-1.08×）更 robust。 论文叙事：14B 和 Gemma-2 的 moderate degradation 虽然成因不同 （14B = diluted spread compounding, Gemma-2 = flat over-allocation）， 但 constraint 在两者上都有效——strengthens \"universal fix\" 的 claim。 注意 greedy ≠ MCKP（10.15 vs 10.35），unconstrained 时 solver choice matters； 但 constrained 后 greedy = MCKP（Δ=0.0000）。这与 7B 的模式完全一致。\n\n\nConcentration 0.47 使 unconstrained 表现落在 Qwen-7B 的 catastrophic（3.31×） 和 Spike/Flat 的 mild（1.07-1.08×）之间。 Solver 仍然 over-allocate 2-bit：profiler 对大部分中间层 heads 给出相似的低 delta， solver 将 ~58 头（15.1%）降为 2-bit——比 Gemma-2 的 31.5% 少 （14B 有更多 \"中等但非零\" 差异供 solver 利用），但比 Yi 的 11.5% 多。 58 个 2-bit heads 的 compounding effect 产生 ~1.56× degradation——moderate 级别， 与 Gemma-2（1.47×）处于同一档。 Constraint 将 PPL 从 10.15 降至 7.18（改善 29.3%）， 证明 constraint 在 moderate degradation 区间也有显著价值—— 不只是 catastrophic 场景（7B）的 \"急救\"，也是 moderate 场景的 \"优化\"。\n"
277	  },
278	  {
279	    "name": "Qwen2.5-14B downstream task eval",
280	    "description": "Downstream evaluation (ARC-C, HellaSwag, PIQA, WinoGrande) on Qwen2.5-14B, 0-shot, at 4× compression. Validates whether 7.9% PPL improvement translates to downstream.\n",
281	    "results": {
282	      "baseline_avg": 0.721,
283	      "uniform_avg": 0.709,
284	      "mckp_avg": 0.716,
285	      "mckp_vs_uniform_avg_pp": 0.7,
286	      "recovery_pct": 58.3,
287	      "per_task": {
288	        "arc_challenge": {
289	          "baseline": 0.565,
290	          "uniform": 0.548,
291	          "mckp": 0.557,
292	          "delta_pp": 0.9
293	        },
294	        "hellaswag": {
295	          "baseline": 0.8,
296	          "uniform": 0.785,
297	          "mckp": 0.793,
298	          "delta_pp": 0.8
299	        },
300	        "piqa": {
301	          "baseline": 0.805,
302	          "uniform": 0.798,
303	          "mckp": 0.802,
304	          "delta_pp": 0.4
305	        },
306	        "winogrande": {
307	          "baseline": 0.715,
308	          "uniform": 0.705,
309	          "mckp": 0.712,
310	          "delta_pp": 0.7
311	        }
312	      }
313	    },
314	    "tables": [
315	      {
316	        "title": "Qwen2.5-14B downstream task results (0-shot, 4× compression)",
317	        "columns": [
318	          "Task",
319	          "BF16 Baseline",
320	          "Uniform 4-bit",
321	          "MCKP k=12",
322	          "Δ (pp)"
323	        ],
324	        "rows": [
325	          [
326	            "ARC-Challenge",
327	            0.565,
328	            0.548,
329	            0.557,
330	            "+0.9"
331	          ],
332	          [
333	            "HellaSwag",
334	            0.8,
335	            0.785,
336	            0.793,
337	            "+0.8"
338	          ],
339	          [
340	            "PIQA",
341	            0.805,
342	            0.798,
343	            0.802,
344	            "+0.4"
345	          ],
346	          [
347	            "WinoGrande",
348	            0.715,
349	            0.705,
350	            0.712,
351	            "+0.7"
352	          ],
353	          [
354	            "Average",
355	            0.721,
356	            0.709,
357	            0.716,
358	            "+0.7"
359	          ]
360	        ]
361	      }
362	    ],
363	    "figures": [],
364	    "analysis": "14B downstream 支持 \"diagnostic correctly predicts downstream\" 的 claim： borderline PPL → borderline downstream。关键对比： - 7B (Spread, conc=0.61): avg +2.6pp, all positive, 72.8% recovery - 14B (diluted spread, 0.47): avg +0.7pp, all positive, 58.3% recovery   - Yi/Llama/Mistral (Spike/Flat): avg -0.48 to -0.99pp, mixed signs 14B 的 \"all positive but modest\" 精确落在 Spread 和 non-Spread 之间， 与 concentration gradient 叙事完全吻合。 但必须在论文中标注：\"without multi-seed confidence intervals,  the per-task deltas (+0.4 to +0.9pp) are within typical single-run noise.\"\n\n\nPPL 7.9% 改善在 downstream 上转化为平均 +0.7pp。 Qwen-7B 的 scaling 参考：27.3% PPL → +2.6pp downstream（ratio ~0.095pp/1% PPL）。 14B 的 7.9% PPL → 预期 ~0.75pp，实际约 +0.7pp，高度一致。 所有 4 个 task 都是正 delta（+0.4 到 +0.9pp），这与 7B 的全正模式一致， 但幅度约为 7B 的 1/3——与 concentration 衰减的预期匹配。 ARC-C 和 HellaSwag 受益最大（reasoning-heavy tasks 对 KV cache 质量更敏感）， PIQA 最小（较简单的 commonsense，对 subtle cache 差异不敏感）。 关键问题：+0.7pp 均值没有 multi-seed CI，单 run noise ~±0.5pp， 所以 \"positive signal\" 有 significance 风险。 论文措辞应 hedge：\"shows modest but consistent positive delta across all four tasks.\"\n"
365	  },
366	  {
367	    "name": "Gemma-2-9B constrained MCKP with BOS fix",
368	    "description": "Re-evaluate constrained MCKP on Gemma-2-9B using corrected BOS-prepend  sliding-window evaluation (stride=512, max_length=2048)。 Replaces old numbers (baseline=8.9, mckp=9.05) that were affected by BOS bug.\n",
369	    "results": {
370	      "baseline_bf16_ppl": 6.0306,
371	      "uniform_4bit_ppl": 6.1683,
372	      "constrained_mckp_ppl": 6.19,
373	      "mckp_vs_uniform_pct": -0.35,
374	      "best_k": 8,
375	      "bit_distribution": {
376	        "2": 8,
377	        "4": 324,
378	        "8": 4
379	      },
380	      "memory_ratio": 0.25,
381	      "unconstrained_greedy_ppl": 8.85,
382	      "unconstrained_ratio": 1.467,
383	      "k_ablation": {
384	        "k0": 6.17,
385	        "k4": 6.17,
386	        "k8": 6.19,
387	        "k12": 6.22,
388	        "k16": 6.25,
389	        "k24": 6.31
390	      }
391	    },
392	    "tables": [
393	      {
394	        "title": "Gemma-2-9B BOS-fixed results summary",
395	        "columns": [
396	          "method",
397	          "PPL",
398	          "note"
399	        ],
400	        "rows": [
401	          [
402	            "Baseline bf16",
403	            6.03,
404	            "BOS-fixed ✓"
405	          ],
406	          [
407	            "Uniform 4-bit",
408	            6.17,
409	            "BOS-fixed ✓"
410	          ],
411	          [
412	            "MCKP constrained k=8",
413	            6.19,
414	            "-0.35% vs uniform"
415	          ],
416	          [
417	            "Greedy unconstrained",
418	            8.85,
419	            "1.47× baseline (from w2_v2)"
420	          ],
421	          [
422	            "Old baseline (BOS bug)",
423	            8.9,
424	            "deprecated"
425	          ],
426	          [
427	            "Old MCKP (BOS bug)",
428	            9.05,
429	            "deprecated"
430	          ]
431	        ]
432	      },
433	      {
434	        "title": "Gemma-2-9B k ablation (BOS-fixed, 336 heads)",
435	        "columns": [
436	          "k",
437	          "PPL",
438	          "note"
439	        ],
440	        "rows": [
441	          [
442	            0,
443	            6.17,
444	            "= uniform"
445	          ],
446	          [
447	            4,
448	            6.17,
449	            "≈ uniform"
450	          ],
451	          [
452	            8,
453	            6.19,
454	            "best k (marginal)"
455	          ],
456	          [
457	            12,
458	            6.22,
459	            ""
460	          ],
461	          [
462	            16,
463	            6.25,
464	            ""
465	          ],
466	          [
467	            24,
468	            6.31,
469	            "monotonic increase"
470	          ]
471	        ]
472	      }
473	    ],
474	    "figures": [],
475	    "analysis": "BOS fix 后 Gemma-2 constrained 结果确认论文两个关键叙事： (1) Flat distribution → MCKP 无益（-0.35% ≈ noise） (2) Constraint 仍有 universal value：unconstrained 1.47× → constrained ≈ uniform，\n    prevents 106→8 heads at 2-bit 的 over-allocation。\n论文需更新的数字：Table 2 的 Gemma-2 行从 (8.9/9.03/9.05) 改为 (6.03/6.17/6.19)。 Cross-architecture table 的 constrained vs uniform 从 \"-0.3%\" 改为 \"-0.35%\"（几乎不变）。 下游指标不需要重测（W3 的下游 eval 用的是独立 pipeline，不受 BOS 影响）。\n\n\nGemma-2 的 flat 分布（concentration 0.23, CV 1.28）意味着 profiler  几乎无法区分 heads。MCKP 选出的 8 个 2-bit 头实质上是 \"noise-driven\"—— sensitivity delta 差异太小，任何选择都无法带来有意义的优化。 PPL 6.19 vs uniform 6.17（-0.35%）完全在 noise 范围内。 k-PPL 近似单调递增（像 Mistral），因为每增加一个 2-bit head 都是 \"equal damage\"。 BOS fix 大幅改变 absolute PPL（8.9→6.03）但不改变 relative conclusions。 unconstrained ratio 1.47× 已在 w2_unconstrained_v2 中确认（BOS-fixed 数据）， 不需要修改。 此实验主要价值：提供 BOS-fixed constrained baseline 替换论文旧数字。 三档分类中的 \"moderate\" 标签不变，因为 1.47× 是 unconstrained 的数字（已有）。\n"
476	  },
477	  {
478	    "name": "Decision rule revalidation with 6 models",
479	    "description": "Revalidate joint diagnostic (concentration ≳0.50 AND t₁/t₅ ≲0.70) with Qwen2.5-14B as sixth model. Assess accuracy and boundary behavior.\n",
480	    "results": {
481	      "rule_accuracy_hard": "5/6",
482	      "rule_accuracy_non_borderline": "5/5",
483	      "n_borderline_cases": 1,
484	      "borderline_model": "Qwen2.5-14B",
485	      "borderline_conc": 0.47,
486	      "borderline_t1t5": 0.72,
487	      "borderline_actual_improvement_pct": 7.9,
488	      "rule_prediction_for_14b": "non-beneficial",
489	      "error_type": "type-II (false negative)",
490	      "softened_threshold_conc": "0.45-0.55",
491	      "softened_threshold_t1t5": "0.65-0.75"
492	    },
493	    "tables": [
494	      {
495	        "title": "Joint diagnostic evaluation across 6 architectures",
496	        "columns": [
497	          "Model",
498	          "GQA",
499	          "Conc.",
500	          "t₁/t₅",
501	          "Shape",
502	          "MCKP Δ",
503	          "Rule prediction",
504	          "Correct?"
505	        ],
506	        "rows": [
507	          [
508	            "Qwen2.5-7B",
509	            "7:1",
510	            0.61,
511	            0.57,
512	            "Spread",
513	            "+27.3%",
514	            "beneficial",
515	            "✅"
516	          ],
517	          [
518	            "Yi-1.5-9B",
519	            "8:1",
520	            0.71,
521	            0.9,
522	            "Spike",
523	            "≈0%",
524	            "non-beneficial",
525	            "✅"
526	          ],
527	          [
528	            "Llama-3.1-8B",
529	            "4:1",
530	            0.57,
531	            0.71,
532	            "Spike (border)",
533	            "+0.2%",
534	            "non-beneficial",
535	            "✅"
536	          ],
537	          [
538	            "Mistral-7B",
539	            "4:1",
540	            0.22,
541	            0.18,
542	            "Flat",
543	            "-0.4%",
544	            "non-beneficial",
545	            "✅"
546	          ],
547	          [
548	            "Gemma-2-9B",
549	            "2:1",
550	            0.23,
551	            0.38,
552	            "Flat",
553	            "-0.35%",
554	            "non-beneficial",
555	            "✅"
556	          ],
557	          [
558	            "Qwen2.5-14B",
559	            "5:1",
560	            0.47,
561	            0.72,
562	            "Diluted Spread",
563	            "+7.9%",
564	            "non-beneficial",
565	            "❌ (boundary)"
566	          ]
567	        ]
568	      }
569	    ],
570	    "figures": [],
571	    "analysis": "论文措辞建议（median tier）： - 不说 \"5/6 accuracy\"——框架为：\n  \"The rule correctly classifies all five non-borderline architectures.\n  Qwen2.5-14B falls in the boundary zone (concentration=0.47, t₁/t₅=0.72)\n  with a modest 7.9% benefit, illustrating that the diagnostic thresholds\n  represent soft boundaries rather than hard cutoffs.\"\n- Threshold 从 \"≳0.50\" 软化为 \"in the range 0.45-0.55\" - Claim 3 不升级——仍是 \"empirical decision rule\" - Limitation: \"validated on 6 architectures with N=1 confirmed Spread (Qwen2.5-7B);\n  the boundary case (14B) provides directional evidence that benefit degrades\n  continuously with concentration.\"\nConcentration-benefit gradient 的 6 个数据点： 0.22 → -0.4%, 0.23 → -0.35%, 0.47 → +7.9%, 0.57 → +0.2%, 0.61 → +27.3%, 0.71 → ≈0%。 非单调（Yi-1.5 的 0.71 / 0% 打破单调）正是 t₁/t₅ 作为 second dimension 的 justification。\n\n\n14B 的 concentration 0.47（<0.50）和 t₁/t₅ 0.72（>0.70）使其在 hard threshold 下 被分类为 non-beneficial，但实际 7.9% 改善是 genuine positive。 Type-II error（false negative）——rule 过于保守。 但 14B 恰好落在两个 threshold 的边界（0.47 vs 0.50, 0.72 vs 0.70，各差 0.03 和 0.02）， 说明 threshold 是 soft boundary 而非 hard cutoff。 这实际上 STRENGTHENS 而非 weakens 论文叙事： (a) 5/5 non-borderline accuracy 完美——rule 对 \"clear cases\" 100% 正确 (b) Boundary case 的 7.9% 改善介于 Spread（27%）和 non-Spread（≤0.2%）之间——\n    continuous behavior 符合 physical intuition\n(c) 承认 soft boundary 比 claim hard cutoff 更 scientifically honest → reviewer credibility Decision rule 的 practical value 不减：practitioners 用 rule 筛选 \"是否值得投入 MCKP\"， boundary case 的 7.9% 改善虽然 positive 但可能不 justify profiling cost（7B 级别才值得）。\n"
572	  },
573	  {
574	    "name": "W9 compounding super-additivity formalization",
575	    "description": "不需要新实验——基于 w9_compounding_v2 已有数据， 将 super-additive compounding trend 形式化为 empirical observation（非 proposition）。 评估 variance 和 formalization 适当程度。\n",
576	    "results": {
577	      "k64_topk_ppl": 22.946,
578	      "k64_randomk_ppl": 55.94,
579	      "k64_randomk_std": 9.73,
580	      "k64_randomk_topk_ratio": 2.44,
581	      "k32_randomk_topk_ratio": 1.58,
582	      "k16_randomk_topk_ratio": 1.24,
583	      "k8_randomk_topk_ratio": 1.1,
584	      "ratio_trend": "monotonically increasing from 1.01 (k=1) to 2.44 (k=64)",
585	      "variance_assessment": "high — k64 randomk std=9.73 (17.4% CV)",
586	      "formalization_level": "observation (figure + descriptive text)"
587	    },
588	    "tables": [
589	      {
590	        "title": "Compounding super-additivity: random-k vs top-k (Qwen2.5-7B)",
591	        "columns": [
592	          "k",
593	          "top-k PPL",
594	          "random-k PPL (mean±std)",
595	          "ratio (random/top)"
596	        ],
597	        "rows": [
598	          [
599	            1,
600	            9.826,
601	            "9.887±0.05",
602	            1.01
603	          ],
604	          [
605	            4,
606	            9.849,
607	            "10.06±0.06",
608	            1.02
609	          ],
610	          [
611	            8,
612	            10.042,
613	            "11.07±0.69",
614	            1.1
615	          ],
616	          [
617	            16,
618	            10.42,
619	            "12.91±0.40",
620	            1.24
621	          ],
622	          [
623	            32,
624	            11.604,
625	            "18.33±2.53",
626	            1.58
627	          ],
628	          [
629	            64,
630	            22.946,
631	            "55.94±9.73",
632	            2.44
633	          ]
634	        ]
635	      }
636	    ],
637	    "figures": [],
638	    "analysis": "论文措辞建议： \"We observe that assigning randomly-selected heads to 2-bit produces disproportionately worse perplexity than assigning the highest-sensitivity heads, and this gap widens monotonically with the number of 2-bit heads (Figure X). At k=64, random selection yields 2.44× the degradation of sensitivity-ranked selection. This super-additive behavior motivates the cardinality constraint: by limiting the number of extreme-quantization assignments, the constraint prevents compounding from low-sensitivity heads that individually appear harmless but collectively degrade quality.\" 不写 \"Observation 1:\" 或 \"Finding:\" 的 formal header—— integrate into Analysis 段落的 descriptive text 中。\n\n\nW9 数据展示明确的 super-additive trend：随 k 增大， random-k 的 PPL 增长快于 top-k，randomk/topk ratio 单调递增 （1.01 → 1.10 → 1.24 → 1.58 → 2.44）。 但以下因素阻止 formal proposition： (a) 仅在 Qwen-7B 一个模型上测试——n=1 不足以 generalize (b) k=64 的 randomk std=9.73（PPL range ~46-66），variance 极大 (c) ratio 的增长 pattern（k=32: 1.58 → k=64: 2.44 跳跃大）\n    可能部分来自 evaluation saturation（极高 PPL 区间 noise 大）\nMedian tier 的 ratio range [1.5, 2.5] 包含实际的 2.44—— 但 2.44 接近上界且 high variance，说明 point estimate 不可靠。 论文处理：Analysis 章节放 Figure + 2-3 句描述， 不给 Proposition 编号，不写 formal bound。 如 reviewer 追问，指向 \"future work: cross-architecture compounding characterization.\"\n"
639	  },
640	  {
641	    "name": "Qwen2.5-14B paper narrative integration",
642	    "description": "将 14B 全部结果整合进论文叙事。 14B 作为 \"boundary case study\" 在 Analysis section 单独一段。 更新 cross-architecture table 和 decision rule discussion。\n",
643	    "results": {
644	      "cross_architecture_table_new_row": {
645	        "model": "Qwen2.5-14B",
646	        "gqa": "5:1",
647	        "kv_heads": 384,
648	        "concentration": 0.47,
649	        "unconstrained_ratio": "1.56×",
650	        "constrained_vs_uniform": "+7.9% (7.18 vs 7.80)",
651	        "shape": "Diluted Spread",
652	        "verdict": "⚠️ Boundary positive"
653	      },
654	      "three_tier_classification": {
655	        "catastrophic": [
656	          "Qwen2.5-7B (3.31×)"
657	        ],
658	        "moderate": [
659	          "Gemma-2-9B (1.47×)",
660	          "Qwen2.5-14B (1.56×)"
661	        ],
662	        "mild": [
663	          "Yi-1.5-9B (1.08×)",
664	          "Llama-3.1-8B (1.07×)",
665	          "Mistral-7B (1.08×)"
666	        ]
667	      },
668	      "claim_updates": {
669	        "claim1": "STRENGTHENED — third distribution shape (diluted spread) adds taxonomic depth",
670	        "claim2": "STRENGTHENED — constraint effective on moderate cases, not just catastrophic",
671	        "claim3": "MAINTAINED — empirical decision rule, 5/5 non-borderline correct, boundary discussed"
672	      },
673	      "contribution_reweight": {
674	        "primary": "Cardinality constraint as universal fix (all 6 models benefit from constraint)",
675	        "secondary": "Concentration-based diagnostic (5/5 non-borderline, boundary continuous)",
676	        "tertiary": "Boundary behavior analysis (14B as case study for soft thresholds)"
677	      },
678	      "limitation_additions": [
679	        "N=1 confirmed Spread; boundary behavior continuous, not binary",
680	        "14B downstream improvement (+0.7pp avg) lacks multi-seed CI",
681	        "GQA 5:1 (14B) is untested in prior work — dilution mechanism is hypothesis"
682	      ]
683	    },
684	    "tables": [
685	      {
686	        "title": "Updated cross-architecture evidence summary (6 models)",
687	        "columns": [
688	          "Model",
689	          "GQA",
690	          "KV Heads",
691	          "Conc.",
692	          "Uncons. ×base",
693	          "Constrained Δ",
694	          "Shape",
695	          "Verdict"
696	        ],
697	        "rows": [
698	          [
699	            "Qwen2.5-7B",
700	            "7:1",
701	            112,
702	            0.61,
703	            "3.31×",
704	            "+27.3%",
705	            "Spread",
706	            "✅ Strong positive"
707	          ],
708	          [
709	            "Qwen2.5-14B",
710	            "5:1",
711	            384,
712	            0.47,
713	            "1.56×",
714	            "+7.9%",
715	            "Diluted Spread",
716	            "⚠️ Boundary positive"
717	          ],
718	          [
719	            "Yi-1.5-9B",
720	            "8:1",
721	            192,
722	            0.71,
723	            "1.08×",
724	            "≈0%",
725	            "Spike",
726	            "❌ GQA counterexample"
727	          ],
728	          [
729	            "Llama-3.1-8B",
730	            "4:1",
731	            256,
732	            0.57,
733	            "1.07×",
734	            "+0.2%",
735	            "Spike (border)",
736	            "≈ Marginal"
737	          ],
738	          [
739	            "Mistral-7B",
740	            "4:1",
741	            256,
742	            0.22,
743	            "1.08×",
744	            "-0.4%",
745	            "Flat",
746	            "❌ Negative"
747	          ],
748	          [
749	            "Gemma-2-9B",
750	            "2:1",
751	            336,
752	            0.23,
753	            "1.47×",
754	            "-0.35%",
755	            "Flat",
756	            "❌ Strongest negative"
757	          ]
758	        ]
759	      }
760	    ],
761	    "figures": [],
762	    "analysis": "Median tier 总评： 论文 contribution 三层递进成立： L1 — Constraint works everywhere（6/6 models）: undeniable, pure engineering value。 L2 — Diagnostic separates clear cases（5/5 non-borderline）: useful practical rule。 L3 — Boundary behavior is continuous（14B case study）: adds analytical depth。 如果 reviewer 接受 L1 和 L2，论文就能过。L3 是 bonus depth。 与 optimistic tier 的关键差距：无法升级到 \"diagnostic framework\"（N=1 Spread 不变）。 与 pessimistic tier 的关键差距：14B 的 positive signal 虽 modest 但 consistent across tasks， 不至于 invalidate diagnostic——最坏情况是 soft boundary，不是 wrong boundary。\n\n14B 在 median tier 下不能升级 claim（N 仍为 1）但增加了三个维度的 depth： (1) Concentration-benefit gradient：6 个数据点比 5 个更密，\n    尤其 0.47 填补了 0.23 (Flat) 和 0.61 (Spread) 之间的空白。\n    Gradient 叙事：\"benefit varies continuously with concentration\"\n    现在有 6 个 data points 而非 5 个。\n(2) 三档分类 \"moderate\" 从 n=1（Gemma-2 only）变为 n=2（+14B），\n    且两者成因不同——增加了分类的 robustness 和解释力。\n(3) Decision rule 的 \"soft boundary\" 讨论是 14B 独特贡献，\n    5 个模型看不出来——必须有一个 boundary case 才能展示 continuity。\n整体 EMNLP Main 可投性评估（median tier）： - 最可能的 reviewer 攻击点从 \"N=1 Spread\" 转向 \"boundary needs formal treatment\" - 后者更容易 defend：can point to continuous gradient + acknowledged as future work - Contribution 重心调整到 constraint universality 后，\n  即使 diagnostic 被 reviewer 质疑为 \"n=6 too small\"，\n  constraint 贡献独立于样本量。\n"
763	  }
764	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14a7591d-09a2-4b99-821c-c3dc06f9e9ca",
  "isSidechain": false,
  "promptId": "9b38a89f-3817-47d6-8645-8990dd1a76c4",
  "type": "user",
  "uuid": "90802346-b088-40c2-81b1-2ff18ab64469",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Qwen2.5-14B hires 2-bit-only profiling\",\n    \"description\": \"High-resolution profiling (64 seq × 2048 tok) on Qwen2.5-14B (48L × 8KV = 384 heads, GQA 5:1). Measure per-head 2-bit distortion delta, compute concentration and t₁/t₅. Tests whether Qwen-7B's Spread pattern generalizes within family at larger scale.\\n\",\n    \"results\": {\n      \"calibration_baseline_ppl\": 5.8432,\n      \"test_baseline_bf16_ppl\": 6.5,\n      \"total_kv_heads\": 384,\n      \"top5pct_n_heads\": 19,\n      \"top5_concentration\": 0.47,\n      \"t1_t5\": 0.72,\n      \"delta_2bit_cv\": 3.85,\n      \"l0_dominance_ratio\": 0.38,\n      \"top1_head\": \"L0H0\",\n      \"top1_delta_2bit\": 3.21,\n      \"top2_head\": \"L0H3\",\n      \"top2_delta_2bit\": 2.78,\n      \"top3_head\": \"L0H5\",\n      \"top3_delta_2bit\": 2.14,\n      \"top4_head\": \"L8H2\",\n      \"top4_delta_2bit\": 1.82,\n      \"top5_head\": \"L0H1\",\n      \"top5_delta_2bit\": 1.53,\n      \"l0_heads_in_top19\": 5,\n      \"positive_delta_heads\": 378,\n      \"distribution_shape\": \"diluted_spread\",\n      \"profiling_time_hours\": 3.5\n    },\n    \"tables\": [\n      {\n        \"title\": \"Qwen2.5-14B top-10 sensitive heads (hires 2-bit delta)\",\n        \"columns\": [\n          \"head\",\n          \"delta_2bit\"\n        ],\n        \"rows\": [\n          [\n            \"L0H0\",\n            3.21\n          ],\n          [\n            \"L0H3\",\n            2.78\n          ],\n          [\n            \"L0H5\",\n            2.14\n          ],\n          [\n            \"L8H2\",\n            1.82\n          ],\n          [\n            \"L0H1\",\n            1.53\n          ],\n          [\n            \"L12H6\",\n            1.31\n          ],\n          [\n            \"L0H7\",\n            1.18\n          ],\n          [\n            \"L5H4\",\n            0.98\n          ],\n          [\n            \"L15H1\",\n            0.87\n          ],\n          [\n            \"L0H2\",\n            0.82\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"关键发现：concentration 0.47 和 t₁/t₅ 0.72 都恰好 miss joint condition （conc < 0.50 AND t₁/t₅ > 0.70）。这不是 Spread 也不是 Flat—— 是 \\\"diluted spread\\\"，joint condition 边界上的 continuous behavior。 14B 的 GQA 5:1（vs 7B 的 7:1）可能是稀释的结构性因素之一： 每层 8 个 KV heads 比 4 个更均匀，L0 cluster 效应被分散。\\n\\n\\nQwen2.5-14B 同属 Qwen2.5 家族，L0 敏感 cluster 的 architectural pattern 大概率保留。 但 14B 有 384 个 KV head（vs 7B 的 112），top-5% 从 ~6 heads 扩至 19 heads。 L0 的 8 个 head 中 ~5 个出现在 top-19，但 L0 只占 top-19 的 26%（5/19）， 其余 14 头散布在中层（L5-L15），导致 concentration 从 7B 的 0.61 下降至 0.47—— 恰好落在 0.50 threshold 以下。 同时，L0 内部虽有多头敏感，但最强头（L0H0, delta=3.21）相对 top-5 heads 的占比上升 （t₁/t₅=0.72 vs 7B 的 0.57），因为中层 heads 稀释了 top-5 中非 L0 头的贡献。 整体呈现 \\\"diluted spread\\\"：L0 cluster 存在但在全局分布中被稀释。 CV=3.85 高于 flat 模型（Mistral 1.31, Gemma-2 1.28）但低于 7B 的数值， 进一步佐证 heterogeneity 介于 Spread 和 Flat 之间。\\n\"\n  },\n  {\n    \"name\": \"Qwen2.5-14B constrained MCKP eval + k ablation\",\n    \"description\": \"Constrained MCKP on Qwen2.5-14B at budget=0.25 (4× compression)。 Sweep k ∈ {0,4,8,12,16,20,24,32,48} 寻找 optimal max_2bit。 Verify greedy = MCKP at optimal k (solver equivalence).\\n\",\n    \"results\": {\n      \"baseline_bf16_ppl\": 6.5,\n      \"uniform_4bit_ppl\": 7.8,\n      \"uniform_baseline_ratio\": 1.2,\n      \"constrained_mckp_ppl\": 7.18,\n      \"mckp_improvement_over_uniform_pct\": 7.9,\n      \"greedy_constrained_ppl\": 7.18,\n      \"greedy_mckp_delta\": 0.0,\n      \"optimal_k\": 12,\n      \"gap_recovery_pct\": 47.7,\n      \"bit_distribution\": {\n        \"2\": 12,\n        \"4\": 366,\n        \"8\": 6\n      },\n      \"memory_ratio\": 0.25,\n      \"k_ablation\": {\n        \"k0\": 7.8,\n        \"k4\": 7.52,\n        \"k8\": 7.28,\n        \"k12\": 7.18,\n        \"k16\": 7.21,\n        \"k20\": 7.28,\n        \"k24\": 7.38,\n        \"k32\": 7.65,\n        \"k48\": 8.42\n      }\n    },\n    \"tables\": [\n      {\n        \"title\": \"Qwen2.5-14B k ablation (384 KV heads, budget=0.25)\",\n        \"columns\": [\n          \"k (max_2bit)\",\n          \"PPL\",\n          \"note\"\n        ],\n        \"rows\": [\n          [\n            0,\n            7.8,\n            \"= uniform 4-bit\"\n          ],\n          [\n            4,\n            7.52,\n            \"\"\n          ],\n          [\n            8,\n            7.28,\n            \"\"\n          ],\n          [\n            12,\n            7.18,\n            \"optimal ✓\"\n          ],\n          [\n            16,\n            7.21,\n            \"\"\n          ],\n          [\n            20,\n            7.28,\n            \"\"\n          ],\n          [\n            24,\n            7.38,\n            \"\"\n          ],\n          [\n            32,\n            7.65,\n            \"compounding visible\"\n          ],\n          [\n            48,\n            8.42,\n            \"compounding dominant\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Qwen2.5-14B allocation comparison\",\n        \"columns\": [\n          \"method\",\n          \"PPL\",\n          \"vs uniform\"\n        ],\n        \"rows\": [\n          [\n            \"Baseline bf16\",\n            6.5,\n            \"—\"\n          ],\n          [\n            \"Uniform 4-bit\",\n            7.8,\n            \"—\"\n          ],\n          [\n            \"MCKP constrained k=12\",\n            7.18,\n            \"+7.9%\"\n          ],\n          [\n            \"Greedy constrained k=12\",\n            7.18,\n            \"Δ=0.0000 vs MCKP\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"7.9% 改善远超 noise range（Gemma-2 -0.35%, Mistral -0.48%）， 是 genuine positive signal。但也远低于 7B 的 27.3%—— 这正是 median tier 的核心预期：borderline positive，不足以升级 N=1 Spread claim。 k=12 到 k=20 接近 plateau（PPL Δ < 0.10），说明 sensitivity 分布比 7B 更平滑。 论文中 14B 应呈现为 \\\"the benefit of non-uniform allocation degrades gracefully as concentration decreases, confirming the diagnostic as a continuous predictor rather than a binary classifier.\\\"\\n\\n\\nUniform 4-bit degradation ratio 1.20×——低于 7B 的 1.575× 但显著高于 Flat 模型的 1.01-1.05×。 原因：14B 的 L0 cluster 虽然被稀释（concentration 0.47 vs 0.61）， 但仍包含 ~5 个高敏感头，被迫 4-bit 时产生可观的 degradation。 MCKP 将 top-12 敏感头从 4-bit 降至 2-bit 并将 6 个最敏感头升至 8-bit， 利用这部分 heterogeneity 获得 7.9% 改善——有意义但远低于 7B 的 27.3%。 k-PPL curve 呈浅 U 型：minimum 在 k=12（≈top-5% 的 63%）， compounding onset 在 k>32 后缓慢上升。U 型深度 (7.80-7.18=0.62) 远小于 7B 的 (15.45-10.91=4.54)， 反映可利用的 sensitivity budget 更少。 Solver equivalence 仍然成立（greedy = MCKP，Δ=0.0000）， constraint 是 primary intervention 的 claim 在 14B 上同样成立。 Recovery 47.7% 低于 7B 的 80.8%，与 concentration 的衰减定量一致。\\n\"\n  },\n  {\n    \"name\": \"Qwen2.5-14B unconstrained solver eval\",\n    \"description\": \"Run unconstrained greedy and MCKP on Qwen2.5-14B. Measure compounding degradation, 2-bit head count, and ratio vs baseline.\\n\",\n    \"results\": {\n      \"baseline_bf16_ppl\": 6.5,\n      \"uniform_4bit_ppl\": 7.8,\n      \"greedy_unconstrained_ppl\": 10.15,\n      \"mckp_unconstrained_ppl\": 10.35,\n      \"greedy_ratio_vs_baseline\": 1.562,\n      \"mckp_ratio_vs_baseline\": 1.592,\n      \"n_2bit_greedy\": 58,\n      \"n_2bit_mckp\": 62,\n      \"pct_2bit_greedy\": 15.1,\n      \"pct_2bit_mckp\": 16.1,\n      \"greedy_bit_distribution\": {\n        \"2\": 58,\n        \"4\": 318,\n        \"8\": 6,\n        \"16\": 2\n      },\n      \"constrained_improvement_vs_unconstrained_pct\": 29.3\n    },\n    \"tables\": [\n      {\n        \"title\": \"Qwen2.5-14B unconstrained vs constrained comparison\",\n        \"columns\": [\n          \"method\",\n          \"PPL\",\n          \"×baseline\",\n          \"2-bit heads (%)\"\n        ],\n        \"rows\": [\n          [\n            \"Baseline bf16\",\n            6.5,\n            \"1.00×\",\n            \"—\"\n          ],\n          [\n            \"Uniform 4-bit\",\n            7.8,\n            \"1.20×\",\n            \"0 (0%)\"\n          ],\n          [\n            \"Greedy unconstrained\",\n            10.15,\n            \"1.56×\",\n            \"58 (15.1%)\"\n          ],\n          [\n            \"MCKP unconstrained\",\n            10.35,\n            \"1.59×\",\n            \"62 (16.1%)\"\n          ],\n          [\n            \"Greedy constrained k=12\",\n            7.18,\n            \"1.10×\",\n            \"12 (3.1%)\"\n          ],\n          [\n            \"MCKP constrained k=12\",\n            7.18,\n            \"1.10×\",\n            \"12 (3.1%)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"14B 的 1.56× 填补三档分类的关键空白： 现有 \\\"moderate\\\" 只有 Gemma-2（1.47×），14B 提供第二个数据点（1.56×）， 使 catastrophic（3.31×）- moderate（1.47-1.56×）- mild（1.07-1.08×）更 robust。 论文叙事：14B 和 Gemma-2 的 moderate degradation 虽然成因不同 （14B = diluted spread compounding, Gemma-2 = flat over-allocation）， 但 constraint 在两者上都有效——strengthens \\\"universal fix\\\" 的 claim。 注意 greedy ≠ MCKP（10.15 vs 10.35），unconstrained 时 solver choice matters； 但 constrained 后 greedy = MCKP（Δ=0.0000）。这与 7B 的模式完全一致。\\n\\n\\nConcentration 0.47 使 unconstrained 表现落在 Qwen-7B 的 catastrophic（3.31×） 和 Spike/Flat 的 mild（1.07-1.08×）之间。 Solver 仍然 over-allocate 2-bit：profiler 对大部分中间层 heads 给出相似的低 delta， solver 将 ~58 头（15.1%）降为 2-bit——比 Gemma-2 的 31.5% 少 （14B 有更多 \\\"中等但非零\\\" 差异供 solver 利用），但比 Yi 的 11.5% 多。 58 个 2-bit heads 的 compounding effect 产生 ~1.56× degradation——moderate 级别， 与 Gemma-2（1.47×）处于同一档。 Constraint 将 PPL 从 10.15 降至 7.18（改善 29.3%）， 证明 constraint 在 moderate degradation 区间也有显著价值—— 不只是 catastrophic 场景（7B）的 \\\"急救\\\"，也是 moderate 场景的 \\\"优化\\\"。\\n\"\n  },\n  {\n    \"name\": \"Qwen2.5-14B downstream task eval\",\n    \"description\": \"Downstream evaluation (ARC-C, HellaSwag, PIQA, WinoGrande) on Qwen2.5-14B, 0-shot, at 4× compression. Validates whether 7.9% PPL improvement translates to downstream.\\n\",\n    \"results\": {\n      \"baseline_avg\": 0.721,\n      \"uniform_avg\": 0.709,\n      \"mckp_avg\": 0.716,\n      \"mckp_vs_uniform_avg_pp\": 0.7,\n      \"recovery_pct\": 58.3,\n      \"per_task\": {\n        \"arc_challenge\": {\n          \"baseline\": 0.565,\n          \"uniform\": 0.548,\n          \"mckp\": 0.557,\n          \"delta_pp\": 0.9\n        },\n        \"hellaswag\": {\n          \"baseline\": 0.8,\n          \"uniform\": 0.785,\n          \"mckp\": 0.793,\n          \"delta_pp\": 0.8\n        },\n        \"piqa\": {\n          \"baseline\": 0.805,\n          \"uniform\": 0.798,\n          \"mckp\": 0.802,\n          \"delta_pp\": 0.4\n        },\n        \"winogrande\": {\n          \"baseline\": 0.715,\n          \"uniform\": 0.705,\n          \"mckp\": 0.712,\n          \"delta_pp\": 0.7\n        }\n      }\n    },\n    \"tables\": [\n      {\n        \"title\": \"Qwen2.5-14B downstream task results (0-shot, 4× compression)\",\n        \"columns\": [\n          \"Task\",\n          \"BF16 Baseline\",\n          \"Uniform 4-bit\",\n          \"MCKP k=12\",\n          \"Δ (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"ARC-Challenge\",\n            0.565,\n            0.548,\n            0.557,\n            \"+0.9\"\n          ],\n          [\n            \"HellaSwag\",\n            0.8,\n            0.785,\n            0.793,\n            \"+0.8\"\n          ],\n          [\n            \"PIQA\",\n            0.805,\n            0.798,\n            0.802,\n            \"+0.4\"\n          ],\n          [\n            \"WinoGrande\",\n            0.715,\n            0.705,\n            0.712,\n            \"+0.7\"\n          ],\n          [\n            \"Average\",\n            0.721,\n            0.709,\n            0.716,\n            \"+0.7\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"14B downstream 支持 \\\"diagnostic correctly predicts downstream\\\" 的 claim： borderline PPL → borderline downstream。关键对比： - 7B (Spread, conc=0.61): avg +2.6pp, all positive, 72.8% recovery - 14B (diluted spread, 0.47): avg +0.7pp, all positive, 58.3% recovery   - Yi/Llama/Mistral (Spike/Flat): avg -0.48 to -0.99pp, mixed signs 14B 的 \\\"all positive but modest\\\" 精确落在 Spread 和 non-Spread 之间， 与 concentration gradient 叙事完全吻合。 但必须在论文中标注：\\\"without multi-seed confidence intervals,  the per-task deltas (+0.4 to +0.9pp) are within typical single-run noise.\\\"\\n\\n\\nPPL 7.9% 改善在 downstream 上转化为平均 +0.7pp。 Qwen-7B 的 scaling 参考：27.3% PPL → +2.6pp downstream（ratio ~0.095pp/1% PPL）。 14B 的 7.9% PPL → 预期 ~0.75pp，实际约 +0.7pp，高度一致。 所有 4 个 task 都是正 delta（+0.4 到 +0.9pp），这与 7B 的全正模式一致， 但幅度约为 7B 的 1/3——与 concentration 衰减的预期匹配。 ARC-C 和 HellaSwag 受益最大（reasoning-heavy tasks 对 KV cache 质量更敏感）， PIQA 最小（较简单的 commonsense，对 subtle cache 差异不敏感）。 关键问题：+0.7pp 均值没有 multi-seed CI，单 run noise ~±0.5pp， 所以 \\\"positive signal\\\" 有 significance 风险。 论文措辞应 hedge：\\\"shows modest but consistent positive delta across all four tasks.\\\"\\n\"\n  },\n  {\n    \"name\": \"Gemma-2-9B constrained MCKP with BOS fix\",\n    \"description\": \"Re-evaluate constrained MCKP on Gemma-2-9B using corrected BOS-prepend  sliding-window evaluation (stride=512, max_length=2048)。 Replaces old numbers (baseline=8.9, mckp=9.05) that were affected by BOS bug.\\n\",\n    \"results\": {\n      \"baseline_bf16_ppl\": 6.0306,\n      \"uniform_4bit_ppl\": 6.1683,\n      \"constrained_mckp_ppl\": 6.19,\n      \"mckp_vs_uniform_pct\": -0.35,\n      \"best_k\": 8,\n      \"bit_distribution\": {\n        \"2\": 8,\n        \"4\": 324,\n        \"8\": 4\n      },\n      \"memory_ratio\": 0.25,\n      \"unconstrained_greedy_ppl\": 8.85,\n      \"unconstrained_ratio\": 1.467,\n      \"k_ablation\": {\n        \"k0\": 6.17,\n        \"k4\": 6.17,\n        \"k8\": 6.19,\n        \"k12\": 6.22,\n        \"k16\": 6.25,\n        \"k24\": 6.31\n      }\n    },\n    \"tables\": [\n      {\n        \"title\": \"Gemma-2-9B BOS-fixed results summary\",\n        \"columns\": [\n          \"method\",\n          \"PPL\",\n          \"note\"\n        ],\n        \"rows\": [\n          [\n            \"Baseline bf16\",\n            6.03,\n            \"BOS-fixed ✓\"\n          ],\n          [\n            \"Uniform 4-bit\",\n            6.17,\n            \"BOS-fixed ✓\"\n          ],\n          [\n            \"MCKP constrained k=8\",\n            6.19,\n            \"-0.35% vs uniform\"\n          ],\n          [\n            \"Greedy unconstrained\",\n            8.85,\n            \"1.47× baseline (from w2_v2)\"\n          ],\n          [\n            \"Old baseline (BOS bug)\",\n            8.9,\n            \"deprecated\"\n          ],\n          [\n            \"Old MCKP (BOS bug)\",\n            9.05,\n            \"deprecated\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Gemma-2-9B k ablation (BOS-fixed, 336 heads)\",\n        \"columns\": [\n          \"k\",\n          \"PPL\",\n          \"note\"\n        ],\n        \"rows\": [\n          [\n            0,\n            6.17,\n            \"= uniform\"\n          ],\n          [\n            4,\n            6.17,\n            \"≈ uniform\"\n          ],\n          [\n            8,\n            6.19,\n            \"best k (marginal)\"\n          ],\n          [\n            12,\n            6.22,\n            \"\"\n          ],\n          [\n            16,\n            6.25,\n            \"\"\n          ],\n          [\n            24,\n            6.31,\n            \"monotonic increase\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"BOS fix 后 Gemma-2 constrained 结果确认论文两个关键叙事： (1) Flat distribution → MCKP 无益（-0.35% ≈ noise） (2) Constraint 仍有 universal value：unconstrained 1.47× → constrained ≈ uniform，\\n    prevents 106→8 heads at 2-bit 的 over-allocation。\\n论文需更新的数字：Table 2 的 Gemma-2 行从 (8.9/9.03/9.05) 改为 (6.03/6.17/6.19)。 Cross-architecture table 的 constrained vs uniform 从 \\\"-0.3%\\\" 改为 \\\"-0.35%\\\"（几乎不变）。 下游指标不需要重测（W3 的下游 eval 用的是独立 pipeline，不受 BOS 影响）。\\n\\n\\nGemma-2 的 flat 分布（concentration 0.23, CV 1.28）意味着 profiler  几乎无法区分 heads。MCKP 选出的 8 个 2-bit 头实质上是 \\\"noise-driven\\\"—— sensitivity delta 差异太小，任何选择都无法带来有意义的优化。 PPL 6.19 vs uniform 6.17（-0.35%）完全在 noise 范围内。 k-PPL 近似单调递增（像 Mistral），因为每增加一个 2-bit head 都是 \\\"equal damage\\\"。 BOS fix 大幅改变 absolute PPL（8.9→6.03）但不改变 relative conclusions。 unconstrained ratio 1.47× 已在 w2_unconstrained_v2 中确认（BOS-fixed 数据）， 不需要修改。 此实验主要价值：提供 BOS-fixed constrained baseline 替换论文旧数字。 三档分类中的 \\\"moderate\\\" 标签不变，因为 1.47× 是 unconstrained 的数字（已有）。\\n\"\n  },\n  {\n    \"name\": \"Decision rule revalidation with 6 models\",\n    \"description\": \"Revalidate joint diagnostic (concentration ≳0.50 AND t₁/t₅ ≲0.70) with Qwen2.5-14B as sixth model. Assess accuracy and boundary behavior.\\n\",\n    \"results\": {\n      \"rule_accuracy_hard\": \"5/6\",\n      \"rule_accuracy_non_borderline\": \"5/5\",\n      \"n_borderline_cases\": 1,\n      \"borderline_model\": \"Qwen2.5-14B\",\n      \"borderline_conc\": 0.47,\n      \"borderline_t1t5\": 0.72,\n      \"borderline_actual_improvement_pct\": 7.9,\n      \"rule_prediction_for_14b\": \"non-beneficial\",\n      \"error_type\": \"type-II (false negative)\",\n      \"softened_threshold_conc\": \"0.45-0.55\",\n      \"softened_threshold_t1t5\": \"0.65-0.75\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Joint diagnostic evaluation across 6 architectures\",\n        \"columns\": [\n          \"Model\",\n          \"GQA\",\n          \"Conc.\",\n          \"t₁/t₅\",\n          \"Shape\",\n          \"MCKP Δ\",\n          \"Rule prediction\",\n          \"Correct?\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen2.5-7B\",\n            \"7:1\",\n            0.61,\n            0.57,\n            \"Spread\",\n            \"+27.3%\",\n            \"beneficial\",\n            \"✅\"\n          ],\n          [\n            \"Yi-1.5-9B\",\n            \"8:1\",\n            0.71,\n            0.9,\n            \"Spike\",\n            \"≈0%\",\n            \"non-beneficial\",\n            \"✅\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            \"4:1\",\n            0.57,\n            0.71,\n            \"Spike (border)\",\n            \"+0.2%\",\n            \"non-beneficial\",\n            \"✅\"\n          ],\n          [\n            \"Mistral-7B\",\n            \"4:1\",\n            0.22,\n            0.18,\n            \"Flat\",\n            \"-0.4%\",\n            \"non-beneficial\",\n            \"✅\"\n          ],\n          [\n            \"Gemma-2-9B\",\n            \"2:1\",\n            0.23,\n            0.38,\n            \"Flat\",\n            \"-0.35%\",\n            \"non-beneficial\",\n            \"✅\"\n          ],\n          [\n            \"Qwen2.5-14B\",\n            \"5:1\",\n            0.47,\n            0.72,\n            \"Diluted Spread\",\n            \"+7.9%\",\n            \"non-beneficial\",\n            \"❌ (boundary)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"论文措辞建议（median tier）： - 不说 \\\"5/6 accuracy\\\"——框架为：\\n  \\\"The rule correctly classifies all five non-borderline architectures.\\n  Qwen2.5-14B falls in the boundary zone (concentration=0.47, t₁/t₅=0.72)\\n  with a modest 7.9% benefit, illustrating that the diagnostic thresholds\\n  represent soft boundaries rather than hard cutoffs.\\\"\\n- Threshold 从 \\\"≳0.50\\\" 软化为 \\\"in the range 0.45-0.55\\\" - Claim 3 不升级——仍是 \\\"empirical decision rule\\\" - Limitation: \\\"validated on 6 architectures with N=1 confirmed Spread (Qwen2.5-7B);\\n  the boundary case (14B) provides directional evidence that benefit degrades\\n  continuously with concentration.\\\"\\nConcentration-benefit gradient 的 6 个数据点： 0.22 → -0.4%, 0.23 → -0.35%, 0.47 → +7.9%, 0.57 → +0.2%, 0.61 → +27.3%, 0.71 → ≈0%。 非单调（Yi-1.5 的 0.71 / 0% 打破单调）正是 t₁/t₅ 作为 second dimension 的 justification。\\n\\n\\n14B 的 concentration 0.47（<0.50）和 t₁/t₅ 0.72（>0.70）使其在 hard threshold 下 被分类为 non-beneficial，但实际 7.9% 改善是 genuine positive。 Type-II error（false negative）——rule 过于保守。 但 14B 恰好落在两个 threshold 的边界（0.47 vs 0.50, 0.72 vs 0.70，各差 0.03 和 0.02）， 说明 threshold 是 soft boundary 而非 hard cutoff。 这实际上 STRENGTHENS 而非 weakens 论文叙事： (a) 5/5 non-borderline accuracy 完美——rule 对 \\\"clear cases\\\" 100% 正确 (b) Boundary case 的 7.9% 改善介于 Spread（27%）和 non-Spread（≤0.2%）之间——\\n    continuous behavior 符合 physical intuition\\n(c) 承认 soft boundary 比 claim hard cutoff 更 scientifically honest → reviewer credibility Decision rule 的 practical value 不减：practitioners 用 rule 筛选 \\\"是否值得投入 MCKP\\\"， boundary case 的 7.9% 改善虽然 positive 但可能不 justify profiling cost（7B 级别才值得）。\\n\"\n  },\n  {\n    \"name\": \"W9 compounding super-additivity formalization\",\n    \"description\": \"不需要新实验——基于 w9_compounding_v2 已有数据， 将 super-additive compounding trend 形式化为 empirical observation（非 proposition）。 评估 variance 和 formalization 适当程度。\\n\",\n    \"results\": {\n      \"k64_topk_ppl\": 22.946,\n      \"k64_randomk_ppl\": 55.94,\n      \"k64_randomk_std\": 9.73,\n      \"k64_randomk_topk_ratio\": 2.44,\n      \"k32_randomk_topk_ratio\": 1.58,\n      \"k16_randomk_topk_ratio\": 1.24,\n      \"k8_randomk_topk_ratio\": 1.1,\n      \"ratio_trend\": \"monotonically increasing from 1.01 (k=1) to 2.44 (k=64)\",\n      \"variance_assessment\": \"high — k64 randomk std=9.73 (17.4% CV)\",\n      \"formalization_level\": \"observation (figure + descriptive text)\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Compounding super-additivity: random-k vs top-k (Qwen2.5-7B)\",\n        \"columns\": [\n          \"k\",\n          \"top-k PPL\",\n          \"random-k PPL (mean±std)\",\n          \"ratio (random/top)\"\n        ],\n        \"rows\": [\n          [\n            1,\n            9.826,\n            \"9.887±0.05\",\n            1.01\n          ],\n          [\n            4,\n            9.849,\n            \"10.06±0.06\",\n            1.02\n          ],\n          [\n            8,\n            10.042,\n            \"11.07±0.69\",\n            1.1\n          ],\n          [\n            16,\n            10.42,\n            \"12.91±0.40\",\n            1.24\n          ],\n          [\n            32,\n            11.604,\n            \"18.33±2.53\",\n            1.58\n          ],\n          [\n            64,\n            22.946,\n            \"55.94±9.73\",\n            2.44\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"论文措辞建议： \\\"We observe that assigning randomly-selected heads to 2-bit produces disproportionately worse perplexity than assigning the highest-sensitivity heads, and this gap widens monotonically with the number of 2-bit heads (Figure X). At k=64, random selection yields 2.44× the degradation of sensitivity-ranked selection. This super-additive behavior motivates the cardinality constraint: by limiting the number of extreme-quantization assignments, the constraint prevents compounding from low-sensitivity heads that individually appear harmless but collectively degrade quality.\\\" 不写 \\\"Observation 1:\\\" 或 \\\"Finding:\\\" 的 formal header—— integrate into Analysis 段落的 descriptive text 中。\\n\\n\\nW9 数据展示明确的 super-additive trend：随 k 增大， random-k 的 PPL 增长快于 top-k，randomk/topk ratio 单调递增 （1.01 → 1.10 → 1.24 → 1.58 → 2.44）。 但以下因素阻止 formal proposition： (a) 仅在 Qwen-7B 一个模型上测试——n=1 不足以 generalize (b) k=64 的 randomk std=9.73（PPL range ~46-66），variance 极大 (c) ratio 的增长 pattern（k=32: 1.58 → k=64: 2.44 跳跃大）\\n    可能部分来自 evaluation saturation（极高 PPL 区间 noise 大）\\nMedian tier 的 ratio range [1.5, 2.5] 包含实际的 2.44—— 但 2.44 接近上界且 high variance，说明 point estimate 不可靠。 论文处理：Analysis 章节放 Figure + 2-3 句描述， 不给 Proposition 编号，不写 formal bound。 如 reviewer 追问，指向 \\\"future work: cross-architecture compounding characterization.\\\"\\n\"\n  },\n  {\n    \"name\": \"Qwen2.5-14B paper narrative integration\",\n    \"description\": \"将 14B 全部结果整合进论文叙事。 14B 作为 \\\"boundary case study\\\" 在 Analysis section 单独一段。 更新 cross-architecture table 和 decision rule discussion。\\n\",\n    \"results\": {\n      \"cross_architecture_table_new_row\": {\n        \"model\": \"Qwen2.5-14B\",\n        \"gqa\": \"5:1\",\n        \"kv_heads\": 384,\n        \"concentration\": 0.47,\n        \"unconstrained_ratio\": \"1.56×\",\n        \"constrained_vs_uniform\": \"+7.9% (7.18 vs 7.80)\",\n        \"shape\": \"Diluted Spread\",\n        \"verdict\": \"⚠️ Boundary positive\"\n      },\n      \"three_tier_classification\": {\n        \"catastrophic\": [\n          \"Qwen2.5-7B (3.31×)\"\n        ],\n        \"moderate\": [\n          \"Gemma-2-9B (1.47×)\",\n          \"Qwen2.5-14B (1.56×)\"\n        ],\n        \"mild\": [\n          \"Yi-1.5-9B (1.08×)\",\n          \"Llama-3.1-8B (1.07×)\",\n          \"Mistral-7B (1.08×)\"\n        ]\n      },\n      \"claim_updates\": {\n        \"claim1\": \"STRENGTHENED — third distribution shape (diluted spread) adds taxonomic depth\",\n        \"claim2\": \"STRENGTHENED — constraint effective on moderate cases, not just catastrophic\",\n        \"claim3\": \"MAINTAINED — empirical decision rule, 5/5 non-borderline correct, boundary discussed\"\n      },\n      \"contribution_reweight\": {\n        \"primary\": \"Cardinality constraint as universal fix (all 6 models benefit from constraint)\",\n        \"secondary\": \"Concentration-based diagnostic (5/5 non-borderline, boundary continuous)\",\n        \"tertiary\": \"Boundary behavior analysis (14B as case study for soft thresholds)\"\n      },\n      \"limitation_additions\": [\n        \"N=1 confirmed Spread; boundary behavior continuous, not binary\",\n        \"14B downstream improvement (+0.7pp avg) lacks multi-seed CI\",\n        \"GQA 5:1 (14B) is untested in prior work — dilution mechanism is hypothesis\"\n      ]\n    },\n    \"tables\": [\n      {\n        \"title\": \"Updated cross-architecture evidence summary (6 models)\",\n        \"columns\": [\n          \"Model\",\n          \"GQA\",\n          \"KV Heads\",\n          \"Conc.\",\n          \"Uncons. ×base\",\n          \"Constrained Δ\",\n          \"Shape\",\n          \"Verdict\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen2.5-7B\",\n            \"7:1\",\n            112,\n            0.61,\n            \"3.31×\",\n            \"+27.3%\",\n            \"Spread\",\n            \"✅ Strong positive\"\n          ],\n          [\n            \"Qwen2.5-14B\",\n            \"5:1\",\n            384,\n            0.47,\n            \"1.56×\",\n            \"+7.9%\",\n            \"Diluted Spread\",\n            \"⚠️ Boundary positive\"\n          ],\n          [\n            \"Yi-1.5-9B\",\n            \"8:1\",\n            192,\n            0.71,\n            \"1.08×\",\n            \"≈0%\",\n            \"Spike\",\n            \"❌ GQA counterexample\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            \"4:1\",\n            256,\n            0.57,\n            \"1.07×\",\n            \"+0.2%\",\n            \"Spike (border)\",\n            \"≈ Marginal\"\n          ],\n          [\n            \"Mistral-7B\",\n            \"4:1\",\n            256,\n            0.22,\n            \"1.08×\",\n            \"-0.4%\",\n            \"Flat\",\n            \"❌ Negative\"\n          ],\n          [\n            \"Gemma-2-9B\",\n            \"2:1\",\n            336,\n            0.23,\n            \"1.47×\",\n            \"-0.35%\",\n            \"Flat\",\n            \"❌ Strongest negative\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median tier 总评： 论文 contribution 三层递进成立： L1 — Constraint works everywhere（6/6 models）: undeniable, pure engineering value。 L2 — Diagnostic separates clear cases（5/5 non-borderline）: useful practical rule。 L3 — Boundary behavior is continuous（14B case study）: adds analytical depth。 如果 reviewer 接受 L1 和 L2，论文就能过。L3 是 bonus depth。 与 optimistic tier 的关键差距：无法升级到 \\\"diagnostic framework\\\"（N=1 Spread 不变）。 与 pessimistic tier 的关键差距：14B 的 positive signal 虽 modest 但 consistent across tasks， 不至于 invalidate diagnostic——最坏情况是 soft boundary，不是 wrong boundary。\\n\\n14B 在 median tier 下不能升级 claim（N 仍为 1）但增加了三个维度的 depth： (1) Concentration-benefit gradient：6 个数据点比 5 个更密，\\n    尤其 0.47 填补了 0.23 (Flat) 和 0.61 (Spread) 之间的空白。\\n    Gradient 叙事：\\\"benefit varies continuously with concentration\\\"\\n    现在有 6 个 data points 而非 5 个。\\n(2) 三档分类 \\\"moderate\\\" 从 n=1（Gemma-2 only）变为 n=2（+14B），\\n    且两者成因不同——增加了分类的 robustness 和解释力。\\n(3) Decision rule 的 \\\"soft boundary\\\" 讨论是 14B 独特贡献，\\n    5 个模型看不出来——必须有一个 boundary case 才能展示 continuity。\\n整体 EMNLP Main 可投性评估（median tier）： - 最可能的 reviewer 攻击点从 \\\"N=1 Spread\\\" 转向 \\\"boundary needs formal treatment\\\" - 后者更容易 defend：can point to continuous gradient + acknowledged as future work - Contribution 重心调整到 constraint universality 后，\\n  即使 diagnostic 被 reviewer 质疑为 \\\"n=6 too small\\\"，\\n  constraint 贡献独立于样本量。\\n\"\n  }\n]",
      "numLines": 764,
      "startLine": 1,
      "totalLines": 764
    }
  },
  "sourceToolAssistantUUID": "14a7591d-09a2-4b99-821c-c3dc06f9e9ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T09:50:27.996Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NoJmyS1wDkHsD1FTDvjNux`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90802346-b088-40c2-81b1-2ff18ab64469",
  "isSidechain": false,
  "requestId": "req_011Cb49U9JkhFt49GKTd8C4a",
  "type": "assistant",
  "uuid": "f658e9aa-fa5c-496b-9d5f-0d1918ee604f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013BStfiLqVA6jviVLt26mNz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12160,
      "cache_read_input_tokens": 11841,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12160,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 200,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12160,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12160
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

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T085855 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts…",
  "leafUuid": "f658e9aa-fa5c-496b-9d5f-0d1918ee604f",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier research paper simulation",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be"
}
```

---

### Tool result

_source line 13 · 2026-05-15T09:50:28.258Z_

<details><summary>↩ Tool result · `toolu_01NoJmyS1wDkHsD1FTDvjNux`</summary>

```text
1	# Paper Framing — ratekv
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR submission)
5	- Deadline: ARR May 25, 2026 (11 days from today 2026-05-14)
6	- Track: Efficient Methods for NLP
7	
8	## bf16 Consistency Resolution (2026-05-14)
9	
10	**已解决**：qwen_bf16_reeval 确认 bf16 ≈ fp16（baseline delta=0.0006, uniform delta=0.005）。compounding_sweep bf16 rerun 不需要。
11	
12	**eval pipeline 一致性**：exp_e 使用了不同的 eval 参数（baseline=8.82, MCKP=9.57），与主 pipeline（baseline=9.81）不一致。hires_mckp_reeval 用统一 pipeline 重测：MCKP hires bf16=10.9131。**论文使用统一 pipeline 数字**。
13	
14	| 指标 | 统一 pipeline (bf16) | exp_e pipeline (bf16) | fp16 (旧) |
15	|------|---------------------|----------------------|-----------|
16	| Baseline | **9.8106** | 8.819 | 9.81 |
17	| Uniform 4-bit | **15.4454** | — | 15.45 |
18	| MCKP hires (max_2bit=8) | **10.9131** | 9.569 | — |
19	| MCKP lowres (max_2bit=8) | ~11.23 | 11.345 | 11.23 |
20	
21	## Core Insight
22	
23	Per-head KV cache quantization sensitivity varies dramatically across architectures, and the effectiveness of non-uniform mixed-precision allocation is fundamentally determined by the degree of this heterogeneity. We provide both the analysis framework — characterizing when non-uniform quantization helps via per-head sensitivity concentration metrics — and a surprisingly simple method fix: a cardinality constraint (≤k heads at 2-bit) that prevents compounding effects from profiler non-additivity and reduces the search space sufficiently that solver choice becomes irrelevant (greedy and MCKP produce identical allocations).
24	
25	## Core Claims (3 条)
26	
27	1. **Head sensitivity heterogeneity is architecture-dependent and determined by sensitivity *distribution shape*, not GQA ratio or concentration alone**: Per-KV-head quantization sensitivity is extremely non-uniform within models, but whether MCKP can exploit this heterogeneity depends on the *shape* of the sensitivity distribution, not just its magnitude. Critical counterexample: Yi-1.5-9B (GQA 8:1, concentration 0.71 — the *highest* in our lineup) provides *no benefit* from MCKP (7.22 vs 7.22 uniform), while Qwen2.5-7B (GQA 7:1, concentration 0.61) succeeds (+27.3%). The difference is distribution shape: Qwen has a *cluster* of sensitive heads (Layer 0, 4 heads with cross-bitwidth gradients — "spread" pattern, t₁/t₅=0.57), while Yi-1.5 has a single extreme outlier (L4H3, delta=13.12, t₁/t₅=0.90 — "spike" pattern) with sensitivity at only one bitwidth. A joint diagnostic — concentration ≳0.50 AND t₁/t₅ ≲0.70 — correctly separates the beneficial case (Qwen) from all four non-beneficial cases across five architectures. Three shape categories emerge:
28	   - **Spread** (Qwen): high concentration + low t₁/t₅ → multiple heads with cross-bitwidth gradients → MCKP effective
29	   - **Spike** (Yi-1.5, Llama): high t₁/t₅ → single outlier dominates → MCKP ineffective
30	   - **Flat** (Mistral, Gemma-2): low concentration → near-uniform sensitivity → MCKP ineffective (t₁/t₅ irrelevant when concentration < 0.50)
31	
32	2. **Cardinality constraint is the primary intervention; unconstrained catastrophe is Spread-specific**: On non-consecutive discrete bit-widths {2,4,8,16}, unconstrained allocation produces **catastrophic** results on Spread-heterogeneity architectures (Qwen: greedy 32.45, MCKP 36.92 vs uniform 15.45 = 3.31× baseline) because per-head independent profiling distortions compound non-additively when many heads are simultaneously assigned extreme quantization. On non-Spread architectures, unconstrained allocation causes **mild-to-moderate degradation** (Yi 1.08×, Llama 1.07×, Mistral 1.08×, Gemma-2 1.47×) but still underperforms uniform 4-bit in all cases — the solver over-allocates 2-bit heads even when individual distortions appear small. A cardinality constraint (max_2bit≤k) is a simple and sufficient condition: it prevents compounding on Spread models, avoids 2-bit over-allocation on non-Spread models, AND reduces the feasible set to where solver choice is irrelevant — constrained greedy and constrained MCKP produce identical bit allocations and PPL (Δ=0.0000, both 11.2312). **Practical implication**: the concentration diagnostic determines whether to invest in MCKP + constraint (Spread models) or simply use uniform 4-bit (non-Spread models — saves solver computation with no quality loss). The profiling benefit beyond the constraint (hires vs lowres) is architecture-dependent: substantial on Spread models (Qwen), marginal on others. The optimal k is determinable via small-scale compounding effect test (plan_004).
33	
34	**Claim 2 three-pillar support** (Reviewer Q4, new narrative STRENGTHENS Claim 2):
35	1. Spread models: constraint prevents catastrophe (Qwen 32.45→11.23)
36	2. Flat models: constraint prevents moderate over-allocation (Gemma-2 8.85→~6.17, 106→8 heads at 2-bit)
37	3. All models: constraint makes solver choice irrelevant (greedy=MCKP, Δ=0.0000)
38	This answers "when" and "why", not just "what" — stronger than original "universal catastrophe" narrative.
39	
40	3. **A joint empirical decision rule correctly separates beneficial from non-beneficial architectures**: Constrained allocation achieves 27.3% PPL improvement on Qwen (spread pattern: concentration 0.61, t₁/t₅=0.57), while providing no benefit on Yi-1.5 (spike: 0.71, t₁/t₅=0.90, ≈0%), Llama (spike: 0.34, t₁/t₅=0.71, +0.2%), Mistral (flat: 0.22, t₁/t₅=0.18, -0.4%), and Gemma-2 (flat: 0.23, t₁/t₅=0.38, -0.3%). The joint condition — concentration ≳0.50 AND t₁/t₅ ≲0.70 — correctly separates the beneficial case from all four non-beneficial cases across five architectures (5/5 accuracy). Concentration alone fails: Yi-1.5 (0.71) exceeds Qwen (0.61) yet gains nothing, because its spike pattern (single outlier, no cross-bitwidth gradient) cannot be exploited. Under aggressive compression (≥5×), constrained allocation prevents catastrophic collapse even on non-beneficial architectures (Llama 5.3×: constrained PPL 57.60 vs uniform 2-bit 2644). This provides practitioners an empirical decision rule for when to invest in mixed-precision KV cache quantization. **Claim strength note (Reviewer-verified)**: N=1 Spread → position as "empirical decision rule", NOT "diagnostic framework". If Qwen2.5-14B also confirms Spread → upgrade to "empirical diagnostic" (N=2).
41	
42	## Story Spine
43	
44	- **Problem**: KV cache quantization typically applies uniform bit-width across all heads. Per-head mixed-precision allocation promises better quality-compression tradeoffs, but two fundamental questions remain unanswered: (1) *when* does non-uniform allocation actually help — i.e., under what architectural and compression conditions does the added complexity pay off? (2) *how* to make existing allocation algorithms (greedy, MCKP) work correctly on hardware-aligned discrete bit-widths {2,4,8,16} where they currently fail catastrophically?
45	
46	- **Existing approaches & gaps**: RateQuant (May 2026) provides R-D optimal per-head allocation via continuous closed-form (Theorem 2) and discrete greedy (Algorithm 1, optimal on consecutive integers {2,...,6} per Proposition 6). However, on hardware-aligned non-consecutive sets {2,4,8,16}, RateQuant's greedy produces PPL 32.45 (vs optimal ~11.23) — the polymatroid structure that guarantees greedy optimality breaks. Moreover, unconstrained MCKP fares even worse (PPL 36.92) due to compounding effects from profiler non-additivity. Critically, neither RateQuant nor ARKV addresses *when* non-uniform allocation is beneficial.
47	
48	- **Our framing**: We present a systematic study of per-head KV cache quantization sensitivity across architectures and identify a surprisingly simple fix for the failure of existing algorithms on hardware-aligned bit-widths: a cardinality constraint limiting the number of heads assigned to extreme quantization levels. This single intervention (a) prevents compounding effects, (b) reduces the search space to where solver choice is irrelevant — greedy and MCKP produce identical optimal allocations, and (c) can be parameterized via a small-scale compounding test. Beyond the method, we establish that the benefit of non-uniform allocation is architecture-dependent and quantifiable via an empirical decision rule (concentration + distribution shape), providing practitioners a two-metric check for when mixed-precision is worthwhile.
49	
50	- **Headline result template**: "We show that the benefit of non-uniform per-head KV cache quantization is concentration-dependent: on spread-heterogeneity architectures (Qwen, concentration 0.61), unconstrained solvers fail catastrophically (PPL 32-37 vs uniform 15.45), while a cardinality constraint (≤k heads at 2-bit) achieves 27.3% PPL improvement with identical results from greedy and MCKP (Δ=0.0000). On non-spread architectures (4 models, 1.07-1.47× baseline), unconstrained solvers cause only mild degradation, and constrained MCKP offers no benefit over uniform 4-bit at either PPL or downstream task level (<1pp avg). An empirical decision rule (concentration ≳0.50 AND t₁/t₅ ≲0.70) correctly separates the beneficial case from all four non-beneficial cases (5/5 accuracy) at both PPL and downstream task level, providing practitioners a two-metric check to determine whether mixed-precision KV cache quantization is worthwhile — or whether uniform quantization suffices."
51	
52	## "When Does Non-Uniform Allocation Help?" — Analysis Chapter
53	
54	Five case studies representing the full spectrum of heterogeneity:
55	
56	| Case | Model | GQA | Top-5% Conc. | Constrained vs Uniform (4×) | Role in Paper |
57	|------|-------|-----|--------------|------------------------------|---------------|
58	| **Strong positive** | Qwen2.5-7B | 7:1 | 0.59-0.66 | **+27.3% (11.23 vs 15.45)** | Primary showcase; "spread" pattern (L0 cluster, 4 heads, 26× dominance) |
59	| **GQA counterexample** | Yi-1.5-9B | 8:1 | 0.71 (hires) | ≈0% (7.22 vs 7.22) | Highest GQA but no benefit; "spike" pattern (L4H3 single outlier, 34% of total delta) |
60	| **Marginal** | Llama-3.1-8B | 4:1 | 0.34-0.59 | +0.2% (8.45 vs 8.47) | Boundary condition; constraint never binds (natural k=2) |
61	| **Negative** | Mistral-7B-v0.3 | 4:1 | 0.22 (hires) | -0.4% (7.16 vs 7.13) | Profiler zero-signal; monotonic k-PPL curve |
62	| **Strongest negative** | Gemma-2-9B | 2:1 | 0.23 (hires) | -0.3% (9.05 vs 9.03) | Low-end anchor; most uniform sensitivity (CV=1.28, t₁/t₅=0.38) |
63	
64	**Spike vs Spread insight**: Yi-1.5 vs Qwen illustrates why GQA ratio alone is insufficient. Both have high GQA (8:1 vs 7:1), but Qwen's L0 *cluster* of sensitive heads creates optimization opportunities for MCKP, while Yi-1.5's single extreme outlier (L4H3) cannot be exploited — the solver assigns 8-bit to that one head but has no other heads to differentiate. Distribution shape matters more than the existence of outliers.
65	
66	**Compression amplifies benefit**: Even on low-heterogeneity Llama, aggressive 5.3× compression yields constrained PPL=57.60 vs uniform 2-bit=2643.77 (45× better).
67	
68	**Joint diagnostic** (n=5, 5/5 correct): concentration ≳0.50 AND t₁/t₅ ≲0.70 → non-uniform allocation recommended (spread pattern). Either condition violated → uniform suffices at moderate compression; non-uniform still valuable at aggressive compression. Yi-1.5 (concentration 0.71 but t₁/t₅=0.90 — spike) and Qwen (0.61, t₁/t₅=0.57 — spread) illustrate why concentration alone is insufficient.
69	
70	## Solver Equivalence Evidence (plan_016, CONFIRMED ✅)
71	
72	| Method | PPL | Bit Distribution | Budget |
73	|--------|-----|-------------------|--------|
74	| Greedy unconstrained | 32.45 | {2:68, 4:30, 8:4, 16:10} | 0.25 |
75	| MCKP unconstrained | 36.92 | — | 0.25 |
76	| **Greedy + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |
77	| **MCKP + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |
78	| Uniform 4-bit | 15.4454 | all 4-bit | 0.25 |
79	
80	Key takeaway: The constraint is the primary intervention — without it, both solvers fail; with it, solver choice is irrelevant (Δ=0.0000). This powerfully demonstrates the constraint is THE contribution.
81	
82	## Cross-Architecture Evidence Summary
83	
84	| Model | GQA | KV Heads | Top-5% Conc. | Unconstrained ×baseline (W2 v2) | Constrained vs Uniform (4×) | Distribution Shape | Conclusion |
85	|-------|-----|----------|--------------|--------------------------------|------------------------------|-------------------|------------|
86	| Qwen2.5-7B | 7:1 | 112 | **0.61** | **3.31× (32.45)** ☠️ | **+27.3% (11.23 vs 15.45)** | Spread (L0 cluster, 4 heads) | ✅ Strong benefit |
87	| Yi-1.5-9B | 8:1 | 192 | **0.71** (hires) | 1.08× (7.56) | **≈0% (7.22 vs 7.22)** | Spike (L4H3 single outlier) | ❌ GQA counterexample |
88	| Llama-3.1-8B | 4:1 | 256 | 0.57 (hires) | 1.07× (8.63) | **+0.2% (8.45 vs 8.47)** | Spike (borderline t₁/t₅=0.71) | ≈ Marginal |
89	| Mistral-7B-v0.3 | 4:1 | 256 | **0.22** (hires) | 1.08× (7.57) | **-0.4% (7.16 vs 7.13)** | Flat (profiler zero-signal) | ❌ Negative |
90	| Gemma-2-9B | 2:1 | 336 | **0.23** (hires) | 1.47× (8.85) | **-0.3% (9.05 vs 9.03)** | Flat (CV=1.28, t₁/t₅=0.38) | ❌ Strongest negative |
91	
92	**Unconstrained pattern** (W2 v2, all WikiText-2 test eval, gradient narrative): Unconstrained degradation follows a **concentration-dependent gradient**, not a binary catastrophe/benign split:
93	- **Spread** (Qwen, conc=0.61): **3.31×** catastrophic — L0 cluster creates massive compounding
94	- **Flat-high-2bit** (Gemma-2, conc=0.23): **1.47×** moderate — solver assigns 106/336=31.5% heads to 2-bit because distortions are indistinguishable (CV=1.28), cumulative effect significant despite small per-head delta
95	- **Spike/Flat-low-2bit** (Yi 1.08×, Llama 1.07×, Mistral 1.08×): mild — solver selects few 2-bit heads (Yi 11.5%, Llama 4.7%, Mistral 16.4%)
96	- In ALL cases unconstrained ≤ uniform 4-bit — solver consistently over-allocates 2-bit heads
97	
98	**Gemma-2 1.47× must be discussed in paper** (Reviewer mandate, severity: warning):
99	
100	Three-tier labeling (NOT binary catastrophe/benign):
101	- **Catastrophic** (3.31×): Spread model (Qwen) — L0 cluster compounding
102	- **Moderate** (1.47×): Flat-high-2bit (Gemma-2) — solver over-allocation from indistinguishable distortions
103	- **Mild** (1.07-1.08×): Spike/Flat-low-2bit (Yi, Llama, Mistral)
104	
105	Reviewer-suggested paragraph for paper (1 段, 3-4 句):
106	"Gemma-2-9B exhibits a moderate 1.47× degradation under unconstrained allocation, higher than the 1.07–1.08× observed in other non-Spread models. This stems from its flat sensitivity distribution (concentration 0.23, CV 1.28): the solver cannot meaningfully differentiate heads, leading to 31.5% of heads assigned to 2-bit (vs 4.7–16.4% in other models). While not catastrophic, this over-allocation still motivates the cardinality constraint even on flat-distribution architectures. The constraint reduces 2-bit heads from 106 to 8, yielding PPL within 0.3% of uniform — confirming that the constraint universally prevents solver over-allocation regardless of distribution shape."
107	
108	This **strengthens** the paper: (1) honesty → credibility, (2) constraint has universal value (not just Spread), (3) explains solver degradation mechanism under low signal → added insight depth.
109	
110	⚠️ **Data file note**: `artifacts/w2_unconstrained_v2_results.json` still has old Gemma-2 BOS bug data (baseline=711.6). Fix in `artifacts/w2_gemma2_bos_fix_results.json`. Agent tasked to merge.
111	
112	**Key pattern**: Constrained allocation benefit depends on the joint condition (concentration ≳0.50 AND t₁/t₅ ≲0.70, 5/5 correct), NOT GQA ratio or concentration alone. Yi-1.5 (GQA 8:1, concentration 0.71 — highest — yet no benefit) vs Qwen (GQA 7:1, concentration 0.61, +27.3%) demonstrates that neither GQA nor concentration alone is a reliable proxy. The critical factor is sensitivity *distribution shape*: spread (multiple heads with cross-bitwidth gradients) enables MCKP, while spike (single outlier) or flat (uniform sensitivity) does not.
113	
114	**Aggressive compression** (Llama): At 5.3× compression, constrained PPL=57.60 vs uniform 2-bit=2643.77 — prevents catastrophic collapse even on low-heterogeneity architectures.
115	
116	### Mistral k Ablation (256 KV heads, budget=0.25)
117	
118	PPL monotonically increases with k — every additional 2-bit head hurts. Even best k=4 (PPL 7.1648) is worse than uniform (7.131).
119	
120	| k | PPL | 2-bit | 4-bit | 8-bit | 16-bit | mem |
121	|---|-----|-------|-------|-------|--------|-----|
122	| 4 | **7.1648** | 4 | 252 | 0 | 0 | 0.248 |
123	| 8 | 7.1997 | 8 | 247 | 0 | 1 | 0.249 |
124	| 12 | 7.2448 | 12 | 242 | 0 | 2 | 0.250 |
125	| 16 | 7.3106 | 16 | 238 | 0 | 2 | 0.248 |
126	| 18 | 7.3231 | 18 | 235 | 0 | 3 | 0.250 |
127	| uniform 4-bit | 7.131 | 0 | 256 | 0 | 0 | 0.250 |
128	
129	Contrast with Qwen (U-shaped, optimal k=8) and Llama (flat, natural k=2). Mistral's monotonic pattern confirms profiler zero-signal: no head benefits from 2-bit downgrade.
130	
131	### Llama k Ablation (256 KV heads, budget=0.25)
132	
133	All k values produce identical PPL=8.4498. MCKP naturally selects only 2 heads for 2-bit — constraint never binds. Marginal +0.2% over uniform (8.4498 vs 8.469).
134	
135	### Downstream Eval — Cross-Architecture (W3, 0-shot, 5 tasks)
136	
137	**Qwen2.5-7B (Spread) — MCKP benefits translate to downstream** ✅
138	
139	| Task | Uniform 4-bit | MCKP hires | Δ | BF16 Baseline |
140	|------|---------------|------------|---|---------------|
141	| ARC-C | 0.4812 | 0.5137 | **+3.16pp** | 0.5290 |
142	| HellaSwag | 0.7284 | 0.7684 | **+4.00pp** | 0.7833 |
143	| PIQA | 0.7661 | 0.7786 | **+1.25pp** | 0.7932 |
144	| WinoGrande | 0.6622 | 0.6819 | **+1.97pp** | 0.6898 |
145	| **Avg recovery** | — | — | **72.8%** | — |
146	
147	**Yi-1.5-9B (Spike) — No MCKP benefit, consistent with PPL** (W3)
148	
149	| Task | Uniform 4-bit | MCKP (k=8) | Δ |
150	|------|---------------|------------|---|
151	| arc_easy | 0.7946 | 0.7854 | -0.92pp |
152	| arc_challenge | 0.5205 | 0.4881 | **-3.24pp** |
153	| hellaswag | 0.5857 | 0.5797 | -0.60pp |
154	| piqa | 0.7927 | 0.7894 | -0.33pp |
155	| winogrande | 0.7174 | 0.7301 | +1.27pp |
156	| **Average** | **0.6822** | **0.6745** | **-0.77pp** |
157	
158	**Llama-3.1-8B (Spike) — No MCKP benefit, consistent with PPL** (W3)
159	
160	| Task | Uniform 4-bit | MCKP (k=8) | Δ |
161	|------|---------------|------------|---|
162	| arc_easy | 0.8173 | 0.8039 | -1.34pp |
163	| arc_challenge | 0.5256 | 0.4991 | **-2.65pp** |
164	| hellaswag | 0.6026 | 0.6012 | -0.14pp |
165	| piqa | 0.7867 | 0.7802 | -0.65pp |
166	| winogrande | 0.7253 | 0.7238 | -0.15pp |
167	| **Average** | **0.6915** | **0.6816** | **-0.99pp** |
168	
169	**Mistral-7B-v0.3 (Flat) — No MCKP benefit, consistent with PPL** (W3)
170	
171	| Task | Uniform 4-bit | MCKP (k=4) | Δ |
172	|------|---------------|------------|---|
173	| arc_easy | — | — | — |
174	| arc_challenge | — | — | — |
175	| hellaswag | — | — | — |
176	| piqa | — | — | — |
177	| winogrande | — | — | — |
178	| **Average** | **0.6894** | **0.6846** | **-0.48pp** |
179	
180	**Gemma-2-9B (Flat) — Negligible MCKP effect, noise range** (W3)
181	
182	| Task | Uniform 4-bit | MCKP | Δ |
183	|------|---------------|------|---|
184	| **Average** | **0.7251** | **0.7265** | **+0.14pp** (noise) |
185	
186	**Downstream summary (Reviewer-verified framing)**:
187	- Diagnostic correctly predicts both PPL and downstream outcomes across **all 5 tested models**
188	- Spread (Qwen): consistent downstream gains (+1.25 to +4.00pp)
189	- Non-Spread (4 models): MCKP shows **minor systematic degradation** vs uniform (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp noise)
190	- **Llama signal**: 0/5 tasks where MCKP ≥ uniform — degradation is systematic, not task-specific noise
191	- arc_challenge shows largest per-task effect (Yi -3.24pp, Llama -2.65pp)
192	- **Paper must**: (a) report full per-task tables, not just averages, (b) use "shows minor degradation" NOT "preserves accuracy" — the latter has spin, (c) note arc_challenge as worst-case explicitly
193	- **Limitation**: no multi-seed CI for downstream — 0-shot arc_challenge -3.24pp could be questioned for significance
194	- **arc_challenge 系统性信号** (Reviewer 观察): arc_challenge 退化跨模型一致（Yi -3.24pp, Llama -2.65pp, Mistral -1.19pp, Gemma-2 -0.17pp），不是随机噪声。论文应主动讨论："ARC-Challenge shows the largest per-task sensitivity to allocation strategy, consistent with its reliance on multi-step reasoning where subtle KV cache errors accumulate."
195	- **呈现方式**: 主表放完整 per-task 数据，文字用均值+range 概括。建议措辞："Across four non-Spread architectures, constrained MCKP shows minor average degradation vs uniform 4-bit (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp). Per-task variation ranges from +1.27pp (Yi, WinoGrande) to -3.24pp (Yi, ARC-Challenge)."
196	
197	## Allocation Baseline Evidence (plan_015, mckp_reeval)
198	
199	All numbers from unified bf16 eval pipeline, budget=0.25.
200	
201	| Model | Baseline | Uniform 4-bit | MCKP | L0-random (mean±std) | L0-random (median) | Naive Positional | MCKP improvement |
202	|-------|----------|---------------|------|----------------------|---------------------|------------------|------------------|
203	| Qwen2.5-7B (k=8) | 9.8106 | 15.4454 | 10.9131 | 11.691±0.422 | **11.515** | 12.230 | 27.3% vs uniform (standard); 29.4% (hires, §5.4) |
204	| Llama-3.1-8B (k=2) | 8.0918 | 8.469 | 8.4498 | 10.479±1.033 | **10.038** | 9.941 | +0.2% vs uniform |
205	| Mistral-7B-v0.3 (k=4) | 7.035 | 7.131 | 7.1648 | 7.560±0.087 | **7.586** | 7.481 | -0.4% vs uniform |
206	
207	**Outlier note**: seed_4 inflates mean on Qwen (12.51) and Llama (12.44). Median is more robust: Qwen median 11.515 vs mean 11.691 (−0.176); Llama median 10.038 vs mean 10.479 (−0.441). Mistral has no outlier (median ≈ mean). Paper should report both mean±std and median.
208	
209	**MCKP vs L0-random (median)**: Qwen 10.91 vs 11.52 (−5.2%); Llama 8.45 vs 10.04 (−15.8%); Mistral 7.16 vs 7.59 (−5.7%). MCKP consistently outperforms random L0-constrained allocation across all architectures.
210	
211	## Differentiation from RateQuant
212	
213	| Aspect | RateQuant | Ours |
214	|--------|-----------|------|
215	| Bit-width selection | Greedy on consecutive integers {2,...,6} (Prop. 6 optimal) + continuous closed-form (Thm. 2) | Cardinality-constrained allocation on hardware-aligned {2,4,8,16}-bit |
216	| Distortion model | Additive, parametric D(b)=α·β^{-b} | Additive + cardinality regularization for non-additivity |
217	| Compounding effects | Acknowledged (Appendix M) but unaddressed | **Core contribution**: cardinality constraint prevents compounding; first quantitative evidence |
218	| Action space | Consecutive integers (polymatroid → greedy optimal) | Non-consecutive hardware-aligned (polymatroid breaks → constraint needed, solver doesn't matter) |
219	| Solver requirement | Greedy (provably optimal in their setting) | **Any solver** — constrained greedy = constrained MCKP (Δ=0.0000 PPL) |
220	| K/V allocation | Asymmetric K/V budget (e.g. K=2.85, V=2.15) | MCKP/greedy treats K/V heads as independent items (natural extension) |
221	| **Applicability analysis** | **Not addressed — assumes non-uniform always helps** | **Systematic study of when non-uniform allocation is beneficial (new contribution)** |
222	
223	## Venue Fit Risks
224	
225	- **"The constraint is just a heuristic, not a real contribution"**: Strongest reviewer attack under new framing. Defense: (a) principled motivation from compounding effect non-additivity with first quantitative evidence, (b) constraint parameterization via systematic compounding test, (c) the finding that constraint alone makes solver choice irrelevant is a surprising and practically useful result — practitioners need only add one parameter to existing pipelines.
226	- **Incrementality over RateQuant**: Defense: (a) RateQuant's greedy is suboptimal unconstrained on {2,4,8,16} (PPL 32.45), (b) our constraint fixes RateQuant's greedy to match MCKP — we're improving their method, not replacing it, (c) applicability analysis is entirely new.
227	- **Method only strong on one architecture (Qwen)**: 5 models tested, only Qwen shows clear benefit. Mitigate: (a) analysis contribution framing — characterizing boundary conditions is more useful than universal positive, (b) honest negative/marginal results (Yi-1.5, Gemma-2, Mistral, Llama) strengthen credibility, (c) unlike prior work that assumes non-uniform always helps, we provide the first systematic study of *when it fails*, (d) Yi-1.5 (GQA 8:1, FAIL) is particularly powerful — it disproves the naive "higher GQA = more benefit" hypothesis and shows our diagnostic is needed.
228	- **GQA ratio is not a reliable proxy**: Yi-1.5 (GQA 8:1) directly contradicts a GQA-based prediction. Do NOT present GQA ratio as a predictor — present it as one contributing factor. The reliable predictor is Top-5% concentration (0.50 threshold, 5/5 correct). The "spike vs spread" analysis explains WHY same-GQA models differ.
229	- **Statistical power**: n=5 models is directional evidence, not statistical claim. Do NOT claim "significant correlation" — use "consistent pattern across 5 architectures" or "5/5 correctly classified by the 0.50 threshold."
230	- **No eviction arm**: Mention as negative finding; framework extends naturally to eviction.
231	
232	## Anticipated Reviewer Concerns
233	
234	1. **"The cardinality constraint is trivial — just cap the extreme allocations"** → (a) Trivial in retrospect, but without it both greedy (PPL 32.45) and MCKP (PPL 36.92) fail catastrophically — the failure mode is non-obvious, (b) principled motivation from compounding effect characterization (plan_004), (c) optimal k selection via systematic small-scale test, (d) the finding that this single intervention eliminates solver complexity is surprising and practically valuable.
235	2. **"This is just RateQuant with a constraint added"** → (a) We agree — and that's the point: RateQuant's greedy + our constraint achieves identical results to MCKP + constraint, (b) the constraint addresses a real gap: compounding effects on {2,4,8,16} that RateQuant acknowledges but doesn't solve, (c) applicability analysis is new.
236	3. **"The method only works on Qwen — isn't this a Qwen paper?"** → We systematically test 4-5 architectures spanning GQA 2:1 to 8:1 and honestly report negative results (Gemma-2, Mistral). The analysis contribution — characterizing *boundary conditions* of non-uniform quantization — generalizes beyond any single model and is more useful than a universally positive but misleading claim.
237	4. **"How does this work at different compression ratios?"** → Budget sweep across 2×, 4×, 8× (plan_005). Aggressive compression on Llama shows benefit amplifies even on low-heterogeneity models.
238	5. **"n=3/4/5 models is not enough for the heterogeneity claim"** → Acknowledged as limitation. We present directional evidence across 4-5 architectures spanning GQA 2:1 to 8:1, with a monotonic trend between GQA ratio, heterogeneity, and MCKP benefit. The Top-5% concentration diagnostic is a testable hypothesis, not a statistical claim.
239	6. **"RateQuant does K/V asymmetric allocation, do you?"** → Framework naturally treats K and V heads as independent items; plan_014 tests K/V separation.
240	7. **"Where are the downstream task results?"** → ✅ DONE (plan_012 + W3, all 5 models): Qwen (Spread): +1.25 to +4.00pp across 4 tasks, 72.8% avg recovery. Yi-1.5 (Spike): avg -0.77pp. Llama (Spike): avg -0.99pp (0/5 tasks positive — systematic). Mistral (Flat): avg -0.48pp. Gemma-2 (Flat): avg +0.14pp (noise). **Diagnostic predicts both PPL and downstream correctly across all 5 architectures**. Must report full per-task tables; use "shows minor degradation" not "preserves accuracy".
241	8. **"The profiler distortion=0.0 on Mistral suggests the profiling method is broken"** → Profiler correctly reports near-zero sensitivity differences. Some architectures genuinely have homogeneous head sensitivity, making non-uniform allocation futile.
242	9. **"If solver doesn't matter, why present MCKP at all?"** → (a) MCKP provides the formal framework for the constrained allocation problem — it's the lens through which we analyze the problem even if greedy solves it equally well, (b) presenting both solvers with identical results IS the evidence that the constraint is what matters, (c) for future extensions (more bit-widths, per-layer budgets), MCKP may regain advantage — we keep it as general framework.
243	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f658e9aa-fa5c-496b-9d5f-0d1918ee604f",
  "isSidechain": false,
  "promptId": "9b38a89f-3817-47d6-8645-8990dd1a76c4",
  "type": "user",
  "uuid": "fc479da0-5863-4a4b-9d40-327ecafdd202",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median/paper_framing.md",
      "content": "# Paper Framing — ratekv\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Deadline: ARR May 25, 2026 (11 days from today 2026-05-14)\n- Track: Efficient Methods for NLP\n\n## bf16 Consistency Resolution (2026-05-14)\n\n**已解决**：qwen_bf16_reeval 确认 bf16 ≈ fp16（baseline delta=0.0006, uniform delta=0.005）。compounding_sweep bf16 rerun 不需要。\n\n**eval pipeline 一致性**：exp_e 使用了不同的 eval 参数（baseline=8.82, MCKP=9.57），与主 pipeline（baseline=9.81）不一致。hires_mckp_reeval 用统一 pipeline 重测：MCKP hires bf16=10.9131。**论文使用统一 pipeline 数字**。\n\n| 指标 | 统一 pipeline (bf16) | exp_e pipeline (bf16) | fp16 (旧) |\n|------|---------------------|----------------------|-----------|\n| Baseline | **9.8106** | 8.819 | 9.81 |\n| Uniform 4-bit | **15.4454** | — | 15.45 |\n| MCKP hires (max_2bit=8) | **10.9131** | 9.569 | — |\n| MCKP lowres (max_2bit=8) | ~11.23 | 11.345 | 11.23 |\n\n## Core Insight\n\nPer-head KV cache quantization sensitivity varies dramatically across architectures, and the effectiveness of non-uniform mixed-precision allocation is fundamentally determined by the degree of this heterogeneity. We provide both the analysis framework — characterizing when non-uniform quantization helps via per-head sensitivity concentration metrics — and a surprisingly simple method fix: a cardinality constraint (≤k heads at 2-bit) that prevents compounding effects from profiler non-additivity and reduces the search space sufficiently that solver choice becomes irrelevant (greedy and MCKP produce identical allocations).\n\n## Core Claims (3 条)\n\n1. **Head sensitivity heterogeneity is architecture-dependent and determined by sensitivity *distribution shape*, not GQA ratio or concentration alone**: Per-KV-head quantization sensitivity is extremely non-uniform within models, but whether MCKP can exploit this heterogeneity depends on the *shape* of the sensitivity distribution, not just its magnitude. Critical counterexample: Yi-1.5-9B (GQA 8:1, concentration 0.71 — the *highest* in our lineup) provides *no benefit* from MCKP (7.22 vs 7.22 uniform), while Qwen2.5-7B (GQA 7:1, concentration 0.61) succeeds (+27.3%). The difference is distribution shape: Qwen has a *cluster* of sensitive heads (Layer 0, 4 heads with cross-bitwidth gradients — \"spread\" pattern, t₁/t₅=0.57), while Yi-1.5 has a single extreme outlier (L4H3, delta=13.12, t₁/t₅=0.90 — \"spike\" pattern) with sensitivity at only one bitwidth. A joint diagnostic — concentration ≳0.50 AND t₁/t₅ ≲0.70 — correctly separates the beneficial case (Qwen) from all four non-beneficial cases across five architectures. Three shape categories emerge:\n   - **Spread** (Qwen): high concentration + low t₁/t₅ → multiple heads with cross-bitwidth gradients → MCKP effective\n   - **Spike** (Yi-1.5, Llama): high t₁/t₅ → single outlier dominates → MCKP ineffective\n   - **Flat** (Mistral, Gemma-2): low concentration → near-uniform sensitivity → MCKP ineffective (t₁/t₅ irrelevant when concentration < 0.50)\n\n2. **Cardinality constraint is the primary intervention; unconstrained catastrophe is Spread-specific**: On non-consecutive discrete bit-widths {2,4,8,16}, unconstrained allocation produces **catastrophic** results on Spread-heterogeneity architectures (Qwen: greedy 32.45, MCKP 36.92 vs uniform 15.45 = 3.31× baseline) because per-head independent profiling distortions compound non-additively when many heads are simultaneously assigned extreme quantization. On non-Spread architectures, unconstrained allocation causes **mild-to-moderate degradation** (Yi 1.08×, Llama 1.07×, Mistral 1.08×, Gemma-2 1.47×) but still underperforms uniform 4-bit in all cases — the solver over-allocates 2-bit heads even when individual distortions appear small. A cardinality constraint (max_2bit≤k) is a simple and sufficient condition: it prevents compounding on Spread models, avoids 2-bit over-allocation on non-Spread models, AND reduces the feasible set to where solver choice is irrelevant — constrained greedy and constrained MCKP produce identical bit allocations and PPL (Δ=0.0000, both 11.2312). **Practical implication**: the concentration diagnostic determines whether to invest in MCKP + constraint (Spread models) or simply use uniform 4-bit (non-Spread models — saves solver computation with no quality loss). The profiling benefit beyond the constraint (hires vs lowres) is architecture-dependent: substantial on Spread models (Qwen), marginal on others. The optimal k is determinable via small-scale compounding effect test (plan_004).\n\n**Claim 2 three-pillar support** (Reviewer Q4, new narrative STRENGTHENS Claim 2):\n1. Spread models: constraint prevents catastrophe (Qwen 32.45→11.23)\n2. Flat models: constraint prevents moderate over-allocation (Gemma-2 8.85→~6.17, 106→8 heads at 2-bit)\n3. All models: constraint makes solver choice irrelevant (greedy=MCKP, Δ=0.0000)\nThis answers \"when\" and \"why\", not just \"what\" — stronger than original \"universal catastrophe\" narrative.\n\n3. **A joint empirical decision rule correctly separates beneficial from non-beneficial architectures**: Constrained allocation achieves 27.3% PPL improvement on Qwen (spread pattern: concentration 0.61, t₁/t₅=0.57), while providing no benefit on Yi-1.5 (spike: 0.71, t₁/t₅=0.90, ≈0%), Llama (spike: 0.34, t₁/t₅=0.71, +0.2%), Mistral (flat: 0.22, t₁/t₅=0.18, -0.4%), and Gemma-2 (flat: 0.23, t₁/t₅=0.38, -0.3%). The joint condition — concentration ≳0.50 AND t₁/t₅ ≲0.70 — correctly separates the beneficial case from all four non-beneficial cases across five architectures (5/5 accuracy). Concentration alone fails: Yi-1.5 (0.71) exceeds Qwen (0.61) yet gains nothing, because its spike pattern (single outlier, no cross-bitwidth gradient) cannot be exploited. Under aggressive compression (≥5×), constrained allocation prevents catastrophic collapse even on non-beneficial architectures (Llama 5.3×: constrained PPL 57.60 vs uniform 2-bit 2644). This provides practitioners an empirical decision rule for when to invest in mixed-precision KV cache quantization. **Claim strength note (Reviewer-verified)**: N=1 Spread → position as \"empirical decision rule\", NOT \"diagnostic framework\". If Qwen2.5-14B also confirms Spread → upgrade to \"empirical diagnostic\" (N=2).\n\n## Story Spine\n\n- **Problem**: KV cache quantization typically applies uniform bit-width across all heads. Per-head mixed-precision allocation promises better quality-compression tradeoffs, but two fundamental questions remain unanswered: (1) *when* does non-uniform allocation actually help — i.e., under what architectural and compression conditions does the added complexity pay off? (2) *how* to make existing allocation algorithms (greedy, MCKP) work correctly on hardware-aligned discrete bit-widths {2,4,8,16} where they currently fail catastrophically?\n\n- **Existing approaches & gaps**: RateQuant (May 2026) provides R-D optimal per-head allocation via continuous closed-form (Theorem 2) and discrete greedy (Algorithm 1, optimal on consecutive integers {2,...,6} per Proposition 6). However, on hardware-aligned non-consecutive sets {2,4,8,16}, RateQuant's greedy produces PPL 32.45 (vs optimal ~11.23) — the polymatroid structure that guarantees greedy optimality breaks. Moreover, unconstrained MCKP fares even worse (PPL 36.92) due to compounding effects from profiler non-additivity. Critically, neither RateQuant nor ARKV addresses *when* non-uniform allocation is beneficial.\n\n- **Our framing**: We present a systematic study of per-head KV cache quantization sensitivity across architectures and identify a surprisingly simple fix for the failure of existing algorithms on hardware-aligned bit-widths: a cardinality constraint limiting the number of heads assigned to extreme quantization levels. This single intervention (a) prevents compounding effects, (b) reduces the search space to where solver choice is irrelevant — greedy and MCKP produce identical optimal allocations, and (c) can be parameterized via a small-scale compounding test. Beyond the method, we establish that the benefit of non-uniform allocation is architecture-dependent and quantifiable via an empirical decision rule (concentration + distribution shape), providing practitioners a two-metric check for when mixed-precision is worthwhile.\n\n- **Headline result template**: \"We show that the benefit of non-uniform per-head KV cache quantization is concentration-dependent: on spread-heterogeneity architectures (Qwen, concentration 0.61), unconstrained solvers fail catastrophically (PPL 32-37 vs uniform 15.45), while a cardinality constraint (≤k heads at 2-bit) achieves 27.3% PPL improvement with identical results from greedy and MCKP (Δ=0.0000). On non-spread architectures (4 models, 1.07-1.47× baseline), unconstrained solvers cause only mild degradation, and constrained MCKP offers no benefit over uniform 4-bit at either PPL or downstream task level (<1pp avg). An empirical decision rule (concentration ≳0.50 AND t₁/t₅ ≲0.70) correctly separates the beneficial case from all four non-beneficial cases (5/5 accuracy) at both PPL and downstream task level, providing practitioners a two-metric check to determine whether mixed-precision KV cache quantization is worthwhile — or whether uniform quantization suffices.\"\n\n## \"When Does Non-Uniform Allocation Help?\" — Analysis Chapter\n\nFive case studies representing the full spectrum of heterogeneity:\n\n| Case | Model | GQA | Top-5% Conc. | Constrained vs Uniform (4×) | Role in Paper |\n|------|-------|-----|--------------|------------------------------|---------------|\n| **Strong positive** | Qwen2.5-7B | 7:1 | 0.59-0.66 | **+27.3% (11.23 vs 15.45)** | Primary showcase; \"spread\" pattern (L0 cluster, 4 heads, 26× dominance) |\n| **GQA counterexample** | Yi-1.5-9B | 8:1 | 0.71 (hires) | ≈0% (7.22 vs 7.22) | Highest GQA but no benefit; \"spike\" pattern (L4H3 single outlier, 34% of total delta) |\n| **Marginal** | Llama-3.1-8B | 4:1 | 0.34-0.59 | +0.2% (8.45 vs 8.47) | Boundary condition; constraint never binds (natural k=2) |\n| **Negative** | Mistral-7B-v0.3 | 4:1 | 0.22 (hires) | -0.4% (7.16 vs 7.13) | Profiler zero-signal; monotonic k-PPL curve |\n| **Strongest negative** | Gemma-2-9B | 2:1 | 0.23 (hires) | -0.3% (9.05 vs 9.03) | Low-end anchor; most uniform sensitivity (CV=1.28, t₁/t₅=0.38) |\n\n**Spike vs Spread insight**: Yi-1.5 vs Qwen illustrates why GQA ratio alone is insufficient. Both have high GQA (8:1 vs 7:1), but Qwen's L0 *cluster* of sensitive heads creates optimization opportunities for MCKP, while Yi-1.5's single extreme outlier (L4H3) cannot be exploited — the solver assigns 8-bit to that one head but has no other heads to differentiate. Distribution shape matters more than the existence of outliers.\n\n**Compression amplifies benefit**: Even on low-heterogeneity Llama, aggressive 5.3× compression yields constrained PPL=57.60 vs uniform 2-bit=2643.77 (45× better).\n\n**Joint diagnostic** (n=5, 5/5 correct): concentration ≳0.50 AND t₁/t₅ ≲0.70 → non-uniform allocation recommended (spread pattern). Either condition violated → uniform suffices at moderate compression; non-uniform still valuable at aggressive compression. Yi-1.5 (concentration 0.71 but t₁/t₅=0.90 — spike) and Qwen (0.61, t₁/t₅=0.57 — spread) illustrate why concentration alone is insufficient.\n\n## Solver Equivalence Evidence (plan_016, CONFIRMED ✅)\n\n| Method | PPL | Bit Distribution | Budget |\n|--------|-----|-------------------|--------|\n| Greedy unconstrained | 32.45 | {2:68, 4:30, 8:4, 16:10} | 0.25 |\n| MCKP unconstrained | 36.92 | — | 0.25 |\n| **Greedy + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |\n| **MCKP + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |\n| Uniform 4-bit | 15.4454 | all 4-bit | 0.25 |\n\nKey takeaway: The constraint is the primary intervention — without it, both solvers fail; with it, solver choice is irrelevant (Δ=0.0000). This powerfully demonstrates the constraint is THE contribution.\n\n## Cross-Architecture Evidence Summary\n\n| Model | GQA | KV Heads | Top-5% Conc. | Unconstrained ×baseline (W2 v2) | Constrained vs Uniform (4×) | Distribution Shape | Conclusion |\n|-------|-----|----------|--------------|--------------------------------|------------------------------|-------------------|------------|\n| Qwen2.5-7B | 7:1 | 112 | **0.61** | **3.31× (32.45)** ☠️ | **+27.3% (11.23 vs 15.45)** | Spread (L0 cluster, 4 heads) | ✅ Strong benefit |\n| Yi-1.5-9B | 8:1 | 192 | **0.71** (hires) | 1.08× (7.56) | **≈0% (7.22 vs 7.22)** | Spike (L4H3 single outlier) | ❌ GQA counterexample |\n| Llama-3.1-8B | 4:1 | 256 | 0.57 (hires) | 1.07× (8.63) | **+0.2% (8.45 vs 8.47)** | Spike (borderline t₁/t₅=0.71) | ≈ Marginal |\n| Mistral-7B-v0.3 | 4:1 | 256 | **0.22** (hires) | 1.08× (7.57) | **-0.4% (7.16 vs 7.13)** | Flat (profiler zero-signal) | ❌ Negative |\n| Gemma-2-9B | 2:1 | 336 | **0.23** (hires) | 1.47× (8.85) | **-0.3% (9.05 vs 9.03)** | Flat (CV=1.28, t₁/t₅=0.38) | ❌ Strongest negative |\n\n**Unconstrained pattern** (W2 v2, all WikiText-2 test eval, gradient narrative): Unconstrained degradation follows a **concentration-dependent gradient**, not a binary catastrophe/benign split:\n- **Spread** (Qwen, conc=0.61): **3.31×** catastrophic — L0 cluster creates massive compounding\n- **Flat-high-2bit** (Gemma-2, conc=0.23): **1.47×** moderate — solver assigns 106/336=31.5% heads to 2-bit because distortions are indistinguishable (CV=1.28), cumulative effect significant despite small per-head delta\n- **Spike/Flat-low-2bit** (Yi 1.08×, Llama 1.07×, Mistral 1.08×): mild — solver selects few 2-bit heads (Yi 11.5%, Llama 4.7%, Mistral 16.4%)\n- In ALL cases unconstrained ≤ uniform 4-bit — solver consistently over-allocates 2-bit heads\n\n**Gemma-2 1.47× must be discussed in paper** (Reviewer mandate, severity: warning):\n\nThree-tier labeling (NOT binary catastrophe/benign):\n- **Catastrophic** (3.31×): Spread model (Qwen) — L0 cluster compounding\n- **Moderate** (1.47×): Flat-high-2bit (Gemma-2) — solver over-allocation from indistinguishable distortions\n- **Mild** (1.07-1.08×): Spike/Flat-low-2bit (Yi, Llama, Mistral)\n\nReviewer-suggested paragraph for paper (1 段, 3-4 句):\n\"Gemma-2-9B exhibits a moderate 1.47× degradation under unconstrained allocation, higher than the 1.07–1.08× observed in other non-Spread models. This stems from its flat sensitivity distribution (concentration 0.23, CV 1.28): the solver cannot meaningfully differentiate heads, leading to 31.5% of heads assigned to 2-bit (vs 4.7–16.4% in other models). While not catastrophic, this over-allocation still motivates the cardinality constraint even on flat-distribution architectures. The constraint reduces 2-bit heads from 106 to 8, yielding PPL within 0.3% of uniform — confirming that the constraint universally prevents solver over-allocation regardless of distribution shape.\"\n\nThis **strengthens** the paper: (1) honesty → credibility, (2) constraint has universal value (not just Spread), (3) explains solver degradation mechanism under low signal → added insight depth.\n\n⚠️ **Data file note**: `artifacts/w2_unconstrained_v2_results.json` still has old Gemma-2 BOS bug data (baseline=711.6). Fix in `artifacts/w2_gemma2_bos_fix_results.json`. Agent tasked to merge.\n\n**Key pattern**: Constrained allocation benefit depends on the joint condition (concentration ≳0.50 AND t₁/t₅ ≲0.70, 5/5 correct), NOT GQA ratio or concentration alone. Yi-1.5 (GQA 8:1, concentration 0.71 — highest — yet no benefit) vs Qwen (GQA 7:1, concentration 0.61, +27.3%) demonstrates that neither GQA nor concentration alone is a reliable proxy. The critical factor is sensitivity *distribution shape*: spread (multiple heads with cross-bitwidth gradients) enables MCKP, while spike (single outlier) or flat (uniform sensitivity) does not.\n\n**Aggressive compression** (Llama): At 5.3× compression, constrained PPL=57.60 vs uniform 2-bit=2643.77 — prevents catastrophic collapse even on low-heterogeneity architectures.\n\n### Mistral k Ablation (256 KV heads, budget=0.25)\n\nPPL monotonically increases with k — every additional 2-bit head hurts. Even best k=4 (PPL 7.1648) is worse than uniform (7.131).\n\n| k | PPL | 2-bit | 4-bit | 8-bit | 16-bit | mem |\n|---|-----|-------|-------|-------|--------|-----|\n| 4 | **7.1648** | 4 | 252 | 0 | 0 | 0.248 |\n| 8 | 7.1997 | 8 | 247 | 0 | 1 | 0.249 |\n| 12 | 7.2448 | 12 | 242 | 0 | 2 | 0.250 |\n| 16 | 7.3106 | 16 | 238 | 0 | 2 | 0.248 |\n| 18 | 7.3231 | 18 | 235 | 0 | 3 | 0.250 |\n| uniform 4-bit | 7.131 | 0 | 256 | 0 | 0 | 0.250 |\n\nContrast with Qwen (U-shaped, optimal k=8) and Llama (flat, natural k=2). Mistral's monotonic pattern confirms profiler zero-signal: no head benefits from 2-bit downgrade.\n\n### Llama k Ablation (256 KV heads, budget=0.25)\n\nAll k values produce identical PPL=8.4498. MCKP naturally selects only 2 heads for 2-bit — constraint never binds. Marginal +0.2% over uniform (8.4498 vs 8.469).\n\n### Downstream Eval — Cross-Architecture (W3, 0-shot, 5 tasks)\n\n**Qwen2.5-7B (Spread) — MCKP benefits translate to downstream** ✅\n\n| Task | Uniform 4-bit | MCKP hires | Δ | BF16 Baseline |\n|------|---------------|------------|---|---------------|\n| ARC-C | 0.4812 | 0.5137 | **+3.16pp** | 0.5290 |\n| HellaSwag | 0.7284 | 0.7684 | **+4.00pp** | 0.7833 |\n| PIQA | 0.7661 | 0.7786 | **+1.25pp** | 0.7932 |\n| WinoGrande | 0.6622 | 0.6819 | **+1.97pp** | 0.6898 |\n| **Avg recovery** | — | — | **72.8%** | — |\n\n**Yi-1.5-9B (Spike) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=8) | Δ |\n|------|---------------|------------|---|\n| arc_easy | 0.7946 | 0.7854 | -0.92pp |\n| arc_challenge | 0.5205 | 0.4881 | **-3.24pp** |\n| hellaswag | 0.5857 | 0.5797 | -0.60pp |\n| piqa | 0.7927 | 0.7894 | -0.33pp |\n| winogrande | 0.7174 | 0.7301 | +1.27pp |\n| **Average** | **0.6822** | **0.6745** | **-0.77pp** |\n\n**Llama-3.1-8B (Spike) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=8) | Δ |\n|------|---------------|------------|---|\n| arc_easy | 0.8173 | 0.8039 | -1.34pp |\n| arc_challenge | 0.5256 | 0.4991 | **-2.65pp** |\n| hellaswag | 0.6026 | 0.6012 | -0.14pp |\n| piqa | 0.7867 | 0.7802 | -0.65pp |\n| winogrande | 0.7253 | 0.7238 | -0.15pp |\n| **Average** | **0.6915** | **0.6816** | **-0.99pp** |\n\n**Mistral-7B-v0.3 (Flat) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=4) | Δ |\n|------|---------------|------------|---|\n| arc_easy | — | — | — |\n| arc_challenge | — | — | — |\n| hellaswag | — | — | — |\n| piqa | — | — | — |\n| winogrande | — | — | — |\n| **Average** | **0.6894** | **0.6846** | **-0.48pp** |\n\n**Gemma-2-9B (Flat) — Negligible MCKP effect, noise range** (W3)\n\n| Task | Uniform 4-bit | MCKP | Δ |\n|------|---------------|------|---|\n| **Average** | **0.7251** | **0.7265** | **+0.14pp** (noise) |\n\n**Downstream summary (Reviewer-verified framing)**:\n- Diagnostic correctly predicts both PPL and downstream outcomes across **all 5 tested models**\n- Spread (Qwen): consistent downstream gains (+1.25 to +4.00pp)\n- Non-Spread (4 models): MCKP shows **minor systematic degradation** vs uniform (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp noise)\n- **Llama signal**: 0/5 tasks where MCKP ≥ uniform — degradation is systematic, not task-specific noise\n- arc_challenge shows largest per-task effect (Yi -3.24pp, Llama -2.65pp)\n- **Paper must**: (a) report full per-task tables, not just averages, (b) use \"shows minor degradation\" NOT \"preserves accuracy\" — the latter has spin, (c) note arc_challenge as worst-case explicitly\n- **Limitation**: no multi-seed CI for downstream — 0-shot arc_challenge -3.24pp could be questioned for significance\n- **arc_challenge 系统性信号** (Reviewer 观察): arc_challenge 退化跨模型一致（Yi -3.24pp, Llama -2.65pp, Mistral -1.19pp, Gemma-2 -0.17pp），不是随机噪声。论文应主动讨论：\"ARC-Challenge shows the largest per-task sensitivity to allocation strategy, consistent with its reliance on multi-step reasoning where subtle KV cache errors accumulate.\"\n- **呈现方式**: 主表放完整 per-task 数据，文字用均值+range 概括。建议措辞：\"Across four non-Spread architectures, constrained MCKP shows minor average degradation vs uniform 4-bit (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp). Per-task variation ranges from +1.27pp (Yi, WinoGrande) to -3.24pp (Yi, ARC-Challenge).\"\n\n## Allocation Baseline Evidence (plan_015, mckp_reeval)\n\nAll numbers from unified bf16 eval pipeline, budget=0.25.\n\n| Model | Baseline | Uniform 4-bit | MCKP | L0-random (mean±std) | L0-random (median) | Naive Positional | MCKP improvement |\n|-------|----------|---------------|------|----------------------|---------------------|------------------|------------------|\n| Qwen2.5-7B (k=8) | 9.8106 | 15.4454 | 10.9131 | 11.691±0.422 | **11.515** | 12.230 | 27.3% vs uniform (standard); 29.4% (hires, §5.4) |\n| Llama-3.1-8B (k=2) | 8.0918 | 8.469 | 8.4498 | 10.479±1.033 | **10.038** | 9.941 | +0.2% vs uniform |\n| Mistral-7B-v0.3 (k=4) | 7.035 | 7.131 | 7.1648 | 7.560±0.087 | **7.586** | 7.481 | -0.4% vs uniform |\n\n**Outlier note**: seed_4 inflates mean on Qwen (12.51) and Llama (12.44). Median is more robust: Qwen median 11.515 vs mean 11.691 (−0.176); Llama median 10.038 vs mean 10.479 (−0.441). Mistral has no outlier (median ≈ mean). Paper should report both mean±std and median.\n\n**MCKP vs L0-random (median)**: Qwen 10.91 vs 11.52 (−5.2%); Llama 8.45 vs 10.04 (−15.8%); Mistral 7.16 vs 7.59 (−5.7%). MCKP consistently outperforms random L0-constrained allocation across all architectures.\n\n## Differentiation from RateQuant\n\n| Aspect | RateQuant | Ours |\n|--------|-----------|------|\n| Bit-width selection | Greedy on consecutive integers {2,...,6} (Prop. 6 optimal) + continuous closed-form (Thm. 2) | Cardinality-constrained allocation on hardware-aligned {2,4,8,16}-bit |\n| Distortion model | Additive, parametric D(b)=α·β^{-b} | Additive + cardinality regularization for non-additivity |\n| Compounding effects | Acknowledged (Appendix M) but unaddressed | **Core contribution**: cardinality constraint prevents compounding; first quantitative evidence |\n| Action space | Consecutive integers (polymatroid → greedy optimal) | Non-consecutive hardware-aligned (polymatroid breaks → constraint needed, solver doesn't matter) |\n| Solver requirement | Greedy (provably optimal in their setting) | **Any solver** — constrained greedy = constrained MCKP (Δ=0.0000 PPL) |\n| K/V allocation | Asymmetric K/V budget (e.g. K=2.85, V=2.15) | MCKP/greedy treats K/V heads as independent items (natural extension) |\n| **Applicability analysis** | **Not addressed — assumes non-uniform always helps** | **Systematic study of when non-uniform allocation is beneficial (new contribution)** |\n\n## Venue Fit Risks\n\n- **\"The constraint is just a heuristic, not a real contribution\"**: Strongest reviewer attack under new framing. Defense: (a) principled motivation from compounding effect non-additivity with first quantitative evidence, (b) constraint parameterization via systematic compounding test, (c) the finding that constraint alone makes solver choice irrelevant is a surprising and practically useful result — practitioners need only add one parameter to existing pipelines.\n- **Incrementality over RateQuant**: Defense: (a) RateQuant's greedy is suboptimal unconstrained on {2,4,8,16} (PPL 32.45), (b) our constraint fixes RateQuant's greedy to match MCKP — we're improving their method, not replacing it, (c) applicability analysis is entirely new.\n- **Method only strong on one architecture (Qwen)**: 5 models tested, only Qwen shows clear benefit. Mitigate: (a) analysis contribution framing — characterizing boundary conditions is more useful than universal positive, (b) honest negative/marginal results (Yi-1.5, Gemma-2, Mistral, Llama) strengthen credibility, (c) unlike prior work that assumes non-uniform always helps, we provide the first systematic study of *when it fails*, (d) Yi-1.5 (GQA 8:1, FAIL) is particularly powerful — it disproves the naive \"higher GQA = more benefit\" hypothesis and shows our diagnostic is needed.\n- **GQA ratio is not a reliable proxy**: Yi-1.5 (GQA 8:1) directly contradicts a GQA-based prediction. Do NOT present GQA ratio as a predictor — present it as one contributing factor. The reliable predictor is Top-5% concentration (0.50 threshold, 5/5 correct). The \"spike vs spread\" analysis explains WHY same-GQA models differ.\n- **Statistical power**: n=5 models is directional evidence, not statistical claim. Do NOT claim \"significant correlation\" — use \"consistent pattern across 5 architectures\" or \"5/5 correctly classified by the 0.50 threshold.\"\n- **No eviction arm**: Mention as negative finding; framework extends naturally to eviction.\n\n## Anticipated Reviewer Concerns\n\n1. **\"The cardinality constraint is trivial — just cap the extreme allocations\"** → (a) Trivial in retrospect, but without it both greedy (PPL 32.45) and MCKP (PPL 36.92) fail catastrophically — the failure mode is non-obvious, (b) principled motivation from compounding effect characterization (plan_004), (c) optimal k selection via systematic small-scale test, (d) the finding that this single intervention eliminates solver complexity is surprising and practically valuable.\n2. **\"This is just RateQuant with a constraint added\"** → (a) We agree — and that's the point: RateQuant's greedy + our constraint achieves identical results to MCKP + constraint, (b) the constraint addresses a real gap: compounding effects on {2,4,8,16} that RateQuant acknowledges but doesn't solve, (c) applicability analysis is new.\n3. **\"The method only works on Qwen — isn't this a Qwen paper?\"** → We systematically test 4-5 architectures spanning GQA 2:1 to 8:1 and honestly report negative results (Gemma-2, Mistral). The analysis contribution — characterizing *boundary conditions* of non-uniform quantization — generalizes beyond any single model and is more useful than a universally positive but misleading claim.\n4. **\"How does this work at different compression ratios?\"** → Budget sweep across 2×, 4×, 8× (plan_005). Aggressive compression on Llama shows benefit amplifies even on low-heterogeneity models.\n5. **\"n=3/4/5 models is not enough for the heterogeneity claim\"** → Acknowledged as limitation. We present directional evidence across 4-5 architectures spanning GQA 2:1 to 8:1, with a monotonic trend between GQA ratio, heterogeneity, and MCKP benefit. The Top-5% concentration diagnostic is a testable hypothesis, not a statistical claim.\n6. **\"RateQuant does K/V asymmetric allocation, do you?\"** → Framework naturally treats K and V heads as independent items; plan_014 tests K/V separation.\n7. **\"Where are the downstream task results?\"** → ✅ DONE (plan_012 + W3, all 5 models): Qwen (Spread): +1.25 to +4.00pp across 4 tasks, 72.8% avg recovery. Yi-1.5 (Spike): avg -0.77pp. Llama (Spike): avg -0.99pp (0/5 tasks positive — systematic). Mistral (Flat): avg -0.48pp. Gemma-2 (Flat): avg +0.14pp (noise). **Diagnostic predicts both PPL and downstream correctly across all 5 architectures**. Must report full per-task tables; use \"shows minor degradation\" not \"preserves accuracy\".\n8. **\"The profiler distortion=0.0 on Mistral suggests the profiling method is broken\"** → Profiler correctly reports near-zero sensitivity differences. Some architectures genuinely have homogeneous head sensitivity, making non-uniform allocation futile.\n9. **\"If solver doesn't matter, why present MCKP at all?\"** → (a) MCKP provides the formal framework for the constrained allocation problem — it's the lens through which we analyze the problem even if greedy solves it equally well, (b) presenting both solvers with identical results IS the evidence that the constraint is what matters, (c) for future extensions (more bit-widths, per-layer budgets), MCKP may regain advantage — we keep it as general framework.\n",
      "numLines": 243,
      "startLine": 1,
      "totalLines": 243
    }
  },
  "sourceToolAssistantUUID": "f658e9aa-fa5c-496b-9d5f-0d1918ee604f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T085855 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts…",
  "leafUuid": "fc479da0-5863-4a4b-9d40-327ecafdd202",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier research paper simulation",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be"
}
```

---

### Assistant

_source line 16 · 2026-05-15T09:50:31.778Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me write the complete LaTeX paper. Let me first make sure the output directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc479da0-5863-4a4b-9d40-327ecafdd202",
  "isSidechain": false,
  "requestId": "req_011Cb49URbHkcE1EE4LCjcNn",
  "type": "assistant",
  "uuid": "e8de729f-3fe1-4434-96c5-318f76a631e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqCMYitpeKho7xUae9k3RP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23018,
      "cache_read_input_tokens": 24001,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23018,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 24001,
          "cache_creation_input_tokens": 23018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23018
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

_source line 17 · 2026-05-15T09:50:32.432Z_

Let me verify the output directory exists and then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8de729f-3fe1-4434-96c5-318f76a631e8",
  "isSidechain": false,
  "requestId": "req_011Cb49URbHkcE1EE4LCjcNn",
  "type": "assistant",
  "uuid": "60e27a52-2ebf-460d-9b46-b291322ee899",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqCMYitpeKho7xUae9k3RP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23018,
      "cache_read_input_tokens": 24001,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23018,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 24001,
          "cache_creation_input_tokens": 23018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23018
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

_source line 18 · 2026-05-15T09:50:34.514Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015crBijMnB1hKCf21uqKNYy`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median/",
  "description": "List median directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60e27a52-2ebf-460d-9b46-b291322ee899",
  "isSidechain": false,
  "requestId": "req_011Cb49URbHkcE1EE4LCjcNn",
  "type": "assistant",
  "uuid": "d3a0609c-efeb-4b59-9947-2e9f8838a496",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqCMYitpeKho7xUae9k3RP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23018,
      "cache_read_input_tokens": 24001,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23018,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 24001,
          "cache_creation_input_tokens": 23018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23018
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

_source line 19 · 2026-05-15T09:50:34.846Z_

<details><summary>↩ Tool result · `toolu_015crBijMnB1hKCf21uqKNYy`</summary>

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
  "parentUuid": "d3a0609c-efeb-4b59-9947-2e9f8838a496",
  "isSidechain": false,
  "promptId": "9b38a89f-3817-47d6-8645-8990dd1a76c4",
  "type": "user",
  "uuid": "353019cd-7a46-46f4-9782-4f6a865241ce",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d3a0609c-efeb-4b59-9947-2e9f8838a496",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-15T09:50:52.476Z_

<details><summary>Logged reasoning block</summary>

```text
Good, the directory exists. Now I need to write a complete LaTeX paper. Let me organize the content based on the experiment data and narrative guidance:

**Experiments in experiment_data.json:**
1. Qwen2.5-14B hires 2-bit-only profiling
2. Qwen2.5-14B constrained MCKP eval + k ablation
3. Qwen2.5-14B unconstrained solver eval
4. Qwen2.5-14B downstream task eval
5. Gemma-2-9B constrained MCKP with BOS fix


6. Decision rule revalidation across 6 models
7. W9 compounding super-additivity formalization
8. Qwen2.5-14B paper narrative integration

For the narrative, I need to frame Claim 3 as an empirical decision rule without overstating it, position the 14B model as a soft boundary case rather than a hard threshold, acknowledge that the decision rule is directional and the 14B shows type-II error behavior, and note in limitations that we have N=1 confirmation for Spread with continuous rather than binary boundary behavior, keeping the three-tier labels but softening the threshold language.

I'll update Gemma-2 numbers for BOS-fixed results while keeping the narrative intact, downgrade W9 super-additivity to an empirical observation shown in a figure with descriptive text rather than a formal proposition, and reframe the contribution weight from diagnostic toward constraint as a universal fix. The paper should still be competitive for EMNLP Main.

Now I'm structuring the paper with sections for abstract, introduction, method covering profiling and MCKP formulation with cardinality constraints and diagnostics, and experiments organized by profiling across architectures, constrained MCKP with k ablation, unconstrained versus constrained comparison, and downstream evaluation.

Writing LaTeX document...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "353019cd-7a46-46f4-9782-4f6a865241ce",
  "isSidechain": false,
  "requestId": "req_011Cb49UupurLYCnpfsxSv6G",
  "type": "assistant",
  "uuid": "8846ba80-63d2-43ed-82fa-55f2b19a2c94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrAeCoatKNUwJwvZDP9FwR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 203,
      "cache_read_input_tokens": 47019,
      "output_tokens": 10633,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 203,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10633,
          "cache_read_input_tokens": 47019,
          "cache_creation_input_tokens": 203,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 203
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

### Assistant

_source line 21 · 2026-05-15T09:50:52.481Z_

Now I'll write the complete LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8846ba80-63d2-43ed-82fa-55f2b19a2c94",
  "isSidechain": false,
  "requestId": "req_011Cb49UupurLYCnpfsxSv6G",
  "type": "assistant",
  "uuid": "baac8457-dca7-40bb-a383-9089ff24cf16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrAeCoatKNUwJwvZDP9FwR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 203,
      "cache_read_input_tokens": 47019,
      "output_tokens": 10633,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 203,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10633,
          "cache_read_input_tokens": 47019,
          "cache_creation_input_tokens": 203,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 203
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

_source line 22 · 2026-05-15T09:53:56.166Z_

<details open><summary>🔧 Tool call — Write · `toolu_01RpPgiA3Mm3Vs9YzW3YR1eN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{microtype}\n\n\\newcommand{\\topkconc}{\\ensuremath{c_5}}\n\\newcommand{\\tratio}{\\ensuremath{t_1/t_5}}\n\n\\title{When Does Non-Uniform KV Cache Quantization Help?\\\\\nCardinality Constraints, Sensitivity Diagnostics,\\\\and a Six-Architecture Study}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%%  ABSTRACT\n%% ============================================================\n\\begin{abstract}\nPer-head mixed-precision KV cache quantization promises better quality--compression tradeoffs than uniform quantization, but two fundamental questions remain open: \\emph{when} does non-uniform allocation actually help, and \\emph{how} should existing solvers (greedy, MCKP) be adapted to hardware-aligned non-consecutive bit-widths \\{2,4,8,16\\}?\nWe present a systematic study across six transformer architectures (Qwen2.5-7B/14B, Yi-1.5-9B, Llama-3.1-8B, Mistral-7B, Gemma-2-9B) spanning GQA ratios from 2:1 to 8:1.\nOur main finding is that a cardinality constraint---limiting the number of heads assigned to extreme (2-bit) quantization---is a simple, sufficient, and universal intervention: it prevents compounding degradation on all tested architectures, reduces the solver search space so that greedy and MCKP produce identical allocations ($\\Delta=0.0000$ PPL), and yields up to 27.3\\% PPL improvement over uniform 4-bit on architectures with favorable sensitivity distributions.\nWe further propose an empirical decision rule based on two profiling metrics (top-5\\% concentration $\\gtrsim 0.50$ and $t_1/t_5 \\lesssim 0.70$) that correctly classifies all five non-borderline architectures as beneficial or non-beneficial.\nThe sixth architecture (Qwen2.5-14B) falls on the decision boundary, exhibiting a modest 7.9\\% benefit that illustrates the threshold as a soft boundary rather than a hard cutoff.\nThese results provide practitioners with both a universal method fix and a two-metric check for when mixed-precision KV cache quantization is worthwhile.\n\\end{abstract}\n\n%% ============================================================\n%%  1  INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nKV cache quantization is a standard approach for reducing memory footprint during autoregressive inference in large language models.\nMost deployed systems apply a \\emph{uniform} bit-width---typically 4-bit---to all attention heads.\nPer-head \\emph{mixed-precision} allocation, where each head receives a bit-width proportional to its quantization sensitivity, offers a principled route to better quality--compression tradeoffs.\nAlgorithms such as the greedy R-D solver of RateQuant and integer-programming formulations (MCKP) provide optimal or near-optimal allocations under additive distortion models.\n\nHowever, when the target bit-widths are the hardware-aligned non-consecutive set \\{2, 4, 8, 16\\}, two problems emerge.\nFirst, \\emph{unconstrained} solvers fail catastrophically on certain architectures: on Qwen2.5-7B, both greedy (PPL 32.45) and MCKP (PPL 36.92) produce allocations far worse than uniform 4-bit (PPL 15.45).\nThis 3.31$\\times$ degradation stems from compounding effects---per-head profiling distortions are non-additive when many heads are simultaneously assigned extreme quantization, and solvers cannot account for this.\nSecond, \\emph{when} non-uniform allocation helps is unknown: is the benefit universal, or architecture-dependent?\n\nWe address both questions through a six-architecture study.\nOur contributions, ordered by generality:\n\n\\begin{enumerate}\n    \\item \\textbf{Cardinality constraint as universal fix.}\n    A single constraint---$\\max\\_2\\text{bit} \\le k$---prevents compounding degradation on all six architectures, makes solver choice irrelevant (constrained greedy $=$ constrained MCKP), and yields 27.3\\% PPL improvement on the most favorable architecture.\n    The constraint is effective on catastrophic (Qwen-7B, 3.31$\\times$), moderate (Gemma-2, 1.47$\\times$; Qwen-14B, 1.56$\\times$), and mild (Yi, Llama, Mistral, 1.07--1.08$\\times$) degradation regimes alike.\n\n    \\item \\textbf{Sensitivity distribution taxonomy.}\n    Head sensitivity distributions fall into three shapes---Spread (cluster of sensitive heads), Spike (single outlier), and Flat (near-uniform)---that predict whether MCKP can exploit heterogeneity.\n    Neither GQA ratio nor concentration alone is sufficient: Yi-1.5-9B (GQA 8:1, concentration 0.71) gains nothing, while Qwen2.5-7B (GQA 7:1, concentration 0.61) gains 27.3\\%.\n\n    \\item \\textbf{Empirical decision rule.}\n    A joint condition (concentration in the range 0.45--0.55 AND $\\tratio \\lesssim 0.70$) correctly classifies all five non-borderline architectures.\n    We present this as a directional heuristic, not a hard cutoff, and discuss the boundary case (Qwen2.5-14B, concentration 0.47, $\\tratio = 0.72$) that yields a modest but genuine 7.9\\% benefit.\n\\end{enumerate}\n\n%% ============================================================\n%%  2  METHOD\n%% ============================================================\n\\section{Method}\n\n\\subsection{Per-Head Sensitivity Profiling}\n\nFor each KV head $h$ in a model with $H$ total KV heads, we measure the 2-bit distortion delta $\\delta_h$: the perplexity increase when head $h$ alone is quantized from the baseline precision to 2-bit, holding all other heads at 4-bit.\nWe use a high-resolution protocol (64 calibration sequences $\\times$ 2048 tokens) to obtain stable per-head estimates.\n\nTwo summary statistics characterize the sensitivity distribution:\n\\begin{itemize}\n    \\item \\textbf{Top-5\\% concentration} (\\topkconc): the fraction of total sensitivity mass held by the top 5\\% of heads.\n    High \\topkconc{} indicates a few heads dominate.\n    \\item \\textbf{Top-1 / Top-5 ratio} (\\tratio): the sensitivity of the single most sensitive head divided by the 5th most sensitive.\n    High \\tratio{} indicates a single outlier (spike); low \\tratio{} indicates a cluster (spread).\n\\end{itemize}\n\n\\subsection{Mixed-Precision Allocation via MCKP}\n\nGiven a memory budget $B$ (as a fraction of full-precision KV cache size), we allocate each head to a bit-width from $\\mathcal{B} = \\{2, 4, 8, 16\\}$ to minimize total perplexity.\nThis is a Multiple-Choice Knapsack Problem (MCKP): each head is an ``item group'' with four choices (one per bit-width), and the knapsack capacity is $B$.\nWe solve both the MCKP formulation and a greedy approximation.\n\n\\subsection{Cardinality Constraint}\n\nWe augment the allocation problem with a cardinality constraint: at most $k$ heads may be assigned 2-bit precision.\nThis prevents compounding degradation from non-additive profiling errors.\nThe optimal $k$ can be determined via a small-scale ablation: sweep $k \\in \\{0, 4, 8, \\ldots\\}$ and select the $k$ minimizing validation PPL.\n\nUnder this constraint, the feasible set shrinks sufficiently that greedy and MCKP produce identical bit allocations on all tested models ($\\Delta_{\\text{PPL}} = 0.0000$).\n\n\\subsection{Empirical Decision Rule}\n\nWe propose a two-metric decision rule for practitioners:\n\\begin{quote}\n    If \\topkconc{} is approximately $\\ge 0.50$ \\textbf{and} \\tratio{} is approximately $\\le 0.70$, invest in profiling + constrained MCKP.\n    Otherwise, uniform 4-bit quantization suffices at moderate compression.\n\\end{quote}\nThis is an empirical heuristic validated on six architectures.\nThe thresholds represent soft boundaries: models near the boundary (concentration in the range 0.45--0.55) may see modest but real benefits.\n\n%% ============================================================\n%%  3  EXPERIMENTS\n%% ============================================================\n\\section{Experiments}\n\nAll experiments use WikiText-2 for calibration and test evaluation unless otherwise noted.\nCompression target is 4$\\times$ (budget = 0.25) unless stated.\nDownstream evaluations use 0-shot accuracy on ARC-Challenge, HellaSwag, PIQA, and WinoGrande.\n\n\\subsection{Sensitivity Profiling: Qwen2.5-14B}\n\\label{sec:profiling_14b}\n\nTable~\\ref{tab:14b_topheads} shows the top-10 sensitive heads of Qwen2.5-14B (48 layers $\\times$ 8 KV heads = 384 total, GQA 5:1).\nTop-5\\% concentration is 0.47 and $\\tratio = 0.72$, both near the decision boundary.\nLayer~0 contributes 5 of the top 19 heads (26\\%), indicating a diluted version of Qwen-7B's Layer-0 cluster.\nWe term this pattern \\emph{diluted spread}: the architectural signature of sensitivity clustering is present but attenuated by the larger head count.\n\n\\begin{table}[t]\n\\centering\n\\caption{Qwen2.5-14B: top-10 sensitive KV heads by 2-bit distortion delta (hires profiling, 64 seq $\\times$ 2048 tok).}\n\\label{tab:14b_topheads}\n\\begin{tabular}{lc}\n\\toprule\nHead & $\\delta_{\\text{2bit}}$ \\\\\n\\midrule\nL0H0  & 3.21 \\\\\nL0H3  & 2.78 \\\\\nL0H5  & 2.14 \\\\\nL8H2  & 1.82 \\\\\nL0H1  & 1.53 \\\\\nL12H6 & 1.31 \\\\\nL0H7  & 1.18 \\\\\nL5H4  & 0.98 \\\\\nL15H1 & 0.87 \\\\\nL0H2  & 0.82 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe coefficient of variation (CV = 3.85) is higher than flat-distribution models (Mistral 1.31, Gemma-2 1.28) but lower than Qwen-7B, confirming that heterogeneity is intermediate.\nThe GQA ratio of 5:1 (vs.\\ 7:1 for the 7B model) yields 8 KV heads per layer rather than 4, which may contribute to the dilution of the Layer-0 cluster effect.\n\n\\subsection{Constrained Allocation and $k$ Ablation: Qwen2.5-14B}\n\\label{sec:constrained_14b}\n\nTable~\\ref{tab:14b_k_ablation} shows the $k$-ablation sweep.\nThe optimal constraint is $k = 12$, yielding PPL 7.18 versus 7.80 for uniform 4-bit---a 7.9\\% improvement.\nThe U-shaped PPL curve is shallow: from $k = 8$ to $k = 20$, PPL varies by less than 0.10, reflecting the smoother sensitivity distribution compared to Qwen-7B.\nBeyond $k = 32$, compounding effects become visible.\n\n\\begin{table}[t]\n\\centering\n\\caption{Qwen2.5-14B: $k$-ablation at budget = 0.25 (384 KV heads).}\n\\label{tab:14b_k_ablation}\n\\begin{tabular}{rll}\n\\toprule\n$k$ (max 2-bit) & PPL & Note \\\\\n\\midrule\n0  & 7.80 & = uniform 4-bit \\\\\n4  & 7.52 & \\\\\n8  & 7.28 & \\\\\n12 & \\textbf{7.18} & optimal \\\\\n16 & 7.21 & \\\\\n20 & 7.28 & \\\\\n24 & 7.38 & \\\\\n32 & 7.65 & compounding visible \\\\\n48 & 8.42 & compounding dominant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nConstrained greedy and constrained MCKP produce identical results at $k = 12$ ($\\Delta = 0.0000$), confirming that solver equivalence under cardinality constraint holds on this architecture as well (Table~\\ref{tab:14b_allocation}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Qwen2.5-14B: allocation comparison at budget = 0.25.}\n\\label{tab:14b_allocation}\n\\begin{tabular}{lcl}\n\\toprule\nMethod & PPL & Note \\\\\n\\midrule\nBaseline BF16        & 6.50 & --- \\\\\nUniform 4-bit        & 7.80 & --- \\\\\nMCKP constrained $k{=}12$  & \\textbf{7.18} & +7.9\\% vs uniform \\\\\nGreedy constrained $k{=}12$ & \\textbf{7.18} & $\\Delta = 0.0000$ vs MCKP \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 7.9\\% improvement far exceeds the noise range observed on flat-distribution models (Gemma-2: $-0.35\\%$, Mistral: $-0.48\\%$), indicating a genuine positive signal.\nHowever, it is substantially below Qwen-7B's 27.3\\%, consistent with the lower concentration.\nThe gap recovery is 47.7\\% (vs.\\ 80.8\\% for the 7B model).\n\n\\subsection{Unconstrained vs.\\ Constrained: Qwen2.5-14B}\n\\label{sec:unconstrained_14b}\n\nTable~\\ref{tab:14b_unconstrained} compares unconstrained and constrained allocation.\nUnconstrained greedy produces 1.56$\\times$ baseline degradation, placing 14B in the \\emph{moderate} tier alongside Gemma-2 (1.47$\\times$), between the catastrophic regime (Qwen-7B, 3.31$\\times$) and the mild regime (Yi/Llama/Mistral, 1.07--1.08$\\times$).\n\n\\begin{table}[t]\n\\centering\n\\caption{Qwen2.5-14B: unconstrained vs.\\ constrained comparison.}\n\\label{tab:14b_unconstrained}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & PPL & $\\times$ baseline & 2-bit heads (\\%) \\\\\n\\midrule\nBaseline BF16              & 6.50  & 1.00$\\times$ & --- \\\\\nUniform 4-bit              & 7.80  & 1.20$\\times$ & 0 (0\\%) \\\\\nGreedy unconstrained       & 10.15 & 1.56$\\times$ & 58 (15.1\\%) \\\\\nMCKP unconstrained         & 10.35 & 1.59$\\times$ & 62 (16.1\\%) \\\\\nGreedy constrained $k{=}12$  & \\textbf{7.18}  & 1.10$\\times$ & 12 (3.1\\%) \\\\\nMCKP constrained $k{=}12$    & \\textbf{7.18}  & 1.10$\\times$ & 12 (3.1\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe constraint reduces PPL from 10.15 to 7.18 (29.3\\% improvement), confirming that the cardinality constraint is effective not only on catastrophic cases (Qwen-7B) but also on moderate degradation regimes.\nUnder unconstrained allocation, solver choice matters (greedy 10.15 vs.\\ MCKP 10.35); under the constraint, it does not ($\\Delta = 0.0000$).\nThis pattern is consistent across all tested architectures.\n\n\\subsection{Gemma-2-9B: BOS-Fixed Constrained Evaluation}\n\\label{sec:gemma2}\n\nWe re-evaluated Gemma-2-9B using corrected BOS-prepend sliding-window evaluation (stride = 512, max\\_length = 2048), replacing earlier results affected by a BOS handling bug.\nTable~\\ref{tab:gemma2_bos} reports updated numbers.\n\n\\begin{table}[t]\n\\centering\n\\caption{Gemma-2-9B: BOS-fixed results (336 KV heads, budget = 0.25).}\n\\label{tab:gemma2_bos}\n\\begin{tabular}{lcl}\n\\toprule\nMethod & PPL & Note \\\\\n\\midrule\nBaseline BF16            & 6.03 & BOS-fixed \\\\\nUniform 4-bit            & 6.17 & BOS-fixed \\\\\nMCKP constrained $k{=}8$  & 6.19 & $-0.35\\%$ vs uniform \\\\\nGreedy unconstrained     & 8.85 & 1.47$\\times$ baseline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Gemma-2-9B: $k$-ablation (BOS-fixed, 336 heads).}\n\\label{tab:gemma2_k}\n\\begin{tabular}{rcl}\n\\toprule\n$k$ & PPL & Note \\\\\n\\midrule\n0  & 6.17 & = uniform \\\\\n4  & 6.17 & $\\approx$ uniform \\\\\n8  & 6.19 & best $k$ (marginal) \\\\\n12 & 6.22 & \\\\\n16 & 6.25 & \\\\\n24 & 6.31 & monotonic increase \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe BOS fix substantially changes absolute PPL (8.9 $\\to$ 6.03 for baseline) but does not change relative conclusions.\nThe flat sensitivity distribution (concentration 0.23, CV 1.28) means the profiler cannot meaningfully differentiate heads; any non-uniform allocation is noise-driven.\nThe $k$--PPL curve is approximately monotonically increasing, similar to Mistral---every additional 2-bit head adds equal damage.\nThe constraint's value on Gemma-2 is not in enabling MCKP optimization but in \\emph{preventing over-allocation}: unconstrained solvers assign 106 of 336 heads (31.5\\%) to 2-bit, producing the 1.47$\\times$ moderate degradation; the constraint caps this at 8 heads, bringing PPL within 0.35\\% of uniform.\n\n\\subsection{Decision Rule Validation Across Six Architectures}\n\\label{sec:decision_rule}\n\nTable~\\ref{tab:decision_rule} evaluates the joint diagnostic ($\\topkconc \\gtrsim 0.50$ AND $\\tratio \\lesssim 0.70$) on all six architectures.\n\n\\begin{table}[t]\n\\centering\n\\caption{Joint diagnostic evaluation across six architectures. Conc.\\ = top-5\\% concentration.}\n\\label{tab:decision_rule}\n\\small\n\\begin{tabular}{lccccccl}\n\\toprule\nModel & GQA & Conc. & $\\tratio$ & Shape & MCKP $\\Delta$ & Rule pred. & Correct? \\\\\n\\midrule\nQwen2.5-7B  & 7:1 & 0.61 & 0.57 & Spread         & +27.3\\%      & beneficial     & \\checkmark \\\\\nYi-1.5-9B   & 8:1 & 0.71 & 0.90 & Spike          & $\\approx$0\\% & non-benef.     & \\checkmark \\\\\nLlama-3.1-8B & 4:1 & 0.57 & 0.71 & Spike (border) & +0.2\\%       & non-benef.     & \\checkmark \\\\\nMistral-7B  & 4:1 & 0.22 & 0.18 & Flat           & $-$0.4\\%     & non-benef.     & \\checkmark \\\\\nGemma-2-9B  & 2:1 & 0.23 & 0.38 & Flat           & $-$0.35\\%    & non-benef.     & \\checkmark \\\\\nQwen2.5-14B & 5:1 & 0.47 & 0.72 & Diluted Spread & +7.9\\%       & non-benef.     & $\\times$ (boundary) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe rule correctly classifies all five non-borderline architectures.\nQwen2.5-14B (concentration 0.47, $\\tratio = 0.72$) falls in the boundary zone, narrowly missing both thresholds (by 0.03 and 0.02 respectively).\nIts 7.9\\% benefit constitutes a type-II error (false negative) under hard thresholds.\nThis illustrates that the diagnostic thresholds represent soft boundaries rather than hard cutoffs---the benefit degrades continuously with concentration rather than vanishing at a sharp threshold.\n\n\\paragraph{14B as boundary case.}\nThe boundary behavior of Qwen2.5-14B deserves separate discussion.\nIts 7.9\\% constrained improvement lies between the strong positive (Qwen-7B, 27.3\\%) and the non-beneficial models ($\\le 0.2\\%$), precisely where a continuous concentration--benefit relationship predicts.\nThe diluted spread pattern---a structural sensitivity cluster in Layer~0 that is attenuated by having 8 rather than 4 KV heads per layer---represents a third distribution shape beyond the original Spread and Spike/Flat categories.\nWe interpret the decision rule as a \\emph{directional heuristic}: models clearly above both thresholds benefit strongly, models clearly below do not, and models near the boundary may see modest gains whose practical value depends on deployment constraints.\nThe rule achieves 5/6 accuracy (5/5 on non-borderline cases), with the single boundary error being conservative (type-II: missing a modest positive) rather than aggressive (type-I: incorrectly recommending costly profiling).\n\n\\subsection{Cross-Architecture Summary}\n\\label{sec:cross_arch}\n\nTable~\\ref{tab:cross_arch} presents the complete evidence across all six architectures.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Cross-architecture evidence summary (6 models). Constrained $\\Delta$ is PPL improvement of constrained MCKP vs.\\ uniform 4-bit at budget = 0.25.}\n\\label{tab:cross_arch}\n\\small\n\\begin{tabular}{lccccccl}\n\\toprule\nModel & GQA & KV Heads & Conc. & Uncons.\\ $\\times$base & Constrained $\\Delta$ & Shape & Verdict \\\\\n\\midrule\nQwen2.5-7B   & 7:1 & 112 & 0.61 & 3.31$\\times$ & +27.3\\% & Spread         & Strong positive \\\\\nQwen2.5-14B  & 5:1 & 384 & 0.47 & 1.56$\\times$ & +7.9\\%  & Diluted Spread & Boundary positive \\\\\nGemma-2-9B   & 2:1 & 336 & 0.23 & 1.47$\\times$ & $-$0.35\\% & Flat         & Negative \\\\\nYi-1.5-9B    & 8:1 & 192 & 0.71 & 1.08$\\times$ & $\\approx$0\\% & Spike     & GQA counterexample \\\\\nLlama-3.1-8B & 4:1 & 256 & 0.57 & 1.07$\\times$ & +0.2\\%  & Spike (border) & Marginal \\\\\nMistral-7B   & 4:1 & 256 & 0.22 & 1.08$\\times$ & $-$0.4\\% & Flat          & Negative \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Three-tier unconstrained degradation.}\nUnconstrained allocation degradation follows a concentration-dependent gradient organized into three tiers:\n\\begin{itemize}\n    \\item \\textbf{Catastrophic} ($>$2$\\times$): Qwen-7B (3.31$\\times$)---Spread pattern with strong Layer-0 compounding.\n    \\item \\textbf{Moderate} (1.4--1.6$\\times$): Gemma-2 (1.47$\\times$) and Qwen-14B (1.56$\\times$)---solver over-allocation from either indistinguishable distortions (flat) or diluted sensitivity clusters.\n    \\item \\textbf{Mild} (1.07--1.08$\\times$): Yi, Llama, Mistral---solvers assign few heads to 2-bit.\n\\end{itemize}\nNotably, Gemma-2 and Qwen-14B reach moderate degradation through different mechanisms (flat over-allocation vs.\\ diluted spread compounding), yet the cardinality constraint is effective on both.\nThis strengthens the ``universal fix'' characterization.\n\n\\subsection{Downstream Task Evaluation: Qwen2.5-14B}\n\\label{sec:downstream_14b}\n\nTable~\\ref{tab:14b_downstream} shows 0-shot downstream results on Qwen2.5-14B at 4$\\times$ compression.\n\n\\begin{table}[t]\n\\centering\n\\caption{Qwen2.5-14B downstream task results (0-shot, 4$\\times$ compression).}\n\\label{tab:14b_downstream}\n\\begin{tabular}{lcccc}\n\\toprule\nTask & BF16 & Uniform 4-bit & MCKP $k{=}12$ & $\\Delta$ (pp) \\\\\n\\midrule\nARC-Challenge & 0.565 & 0.548 & 0.557 & +0.9 \\\\\nHellaSwag     & 0.800 & 0.785 & 0.793 & +0.8 \\\\\nPIQA          & 0.805 & 0.798 & 0.802 & +0.4 \\\\\nWinoGrande    & 0.715 & 0.705 & 0.712 & +0.7 \\\\\n\\midrule\nAverage       & 0.721 & 0.709 & 0.716 & +0.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll four tasks show positive deltas (+0.4 to +0.9 percentage points), with 58.3\\% average gap recovery.\nThis is consistent with the PPL improvement: Qwen-7B's 27.3\\% PPL gain translates to +2.6pp average downstream, while 14B's 7.9\\% PPL gain translates to +0.7pp---roughly proportional.\nHowever, without multi-seed confidence intervals, the per-task deltas (+0.4 to +0.9pp) are within typical single-run noise.\nWe describe the signal as \\emph{modest but consistent across all four tasks}.\n\n\\paragraph{Cross-architecture downstream comparison.}\nAcross prior experiments on five architectures, the diagnostic correctly predicts downstream outcomes:\nQwen-7B (Spread) shows +1.25 to +4.00pp gains across four tasks (72.8\\% recovery);\nYi-1.5 (Spike) shows $-0.77$pp average;\nLlama (Spike) shows $-0.99$pp average with 0/5 tasks positive---systematic degradation;\nMistral (Flat) shows $-0.48$pp average;\nGemma-2 (Flat) shows $+0.14$pp average (noise range).\nARC-Challenge exhibits the largest per-task sensitivity to allocation strategy across all models (Yi $-3.24$pp, Llama $-2.65$pp), consistent with its reliance on multi-step reasoning where subtle KV cache errors accumulate.\n\n\\subsection{Compounding Super-Additivity}\n\\label{sec:compounding}\n\nWe examine the compounding effect by comparing random-$k$ versus top-$k$ 2-bit head selection on Qwen2.5-7B (Table~\\ref{tab:compounding}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Compounding super-additivity: random-$k$ vs.\\ top-$k$ 2-bit assignment on Qwen2.5-7B.}\n\\label{tab:compounding}\n\\begin{tabular}{rccr}\n\\toprule\n$k$ & top-$k$ PPL & random-$k$ PPL (mean$\\pm$std) & Ratio \\\\\n\\midrule\n1  & 9.826  & 9.887$\\pm$0.05  & 1.01 \\\\\n4  & 9.849  & 10.06$\\pm$0.06  & 1.02 \\\\\n8  & 10.042 & 11.07$\\pm$0.69  & 1.10 \\\\\n16 & 10.42  & 12.91$\\pm$0.40  & 1.24 \\\\\n32 & 11.604 & 18.33$\\pm$2.53  & 1.58 \\\\\n64 & 22.946 & 55.94$\\pm$9.73  & 2.44 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAssigning randomly-selected heads to 2-bit produces disproportionately worse perplexity than assigning the highest-sensitivity heads, and this gap widens monotonically with the number of 2-bit heads.\nAt $k = 64$, random selection yields 2.44$\\times$ the degradation of sensitivity-ranked selection.\nThe variance of the random baseline also grows substantially (std from 0.05 at $k{=}1$ to 9.73 at $k{=}64$), reflecting the increasing influence of which specific heads are forced to extreme quantization.\nThis super-additive behavior motivates the cardinality constraint: by limiting the number of extreme-quantization assignments, the constraint prevents compounding from low-sensitivity heads that individually appear harmless but collectively degrade quality.\nWe present this as an empirical observation on a single architecture rather than a formal proposition, and note that cross-architecture characterization of compounding behavior is an open direction.\n\n\\subsection{Solver Equivalence Under Constraint}\n\nA consistent finding across all six architectures is that the cardinality constraint eliminates solver dependence.\nTable~\\ref{tab:solver_equiv} summarizes the unconstrained and constrained solver comparison for the primary showcase (Qwen-7B) and the boundary case (Qwen-14B).\n\n\\begin{table}[t]\n\\centering\n\\caption{Solver equivalence: greedy vs.\\ MCKP, unconstrained vs.\\ constrained.}\n\\label{tab:solver_equiv}\n\\begin{tabular}{llcc}\n\\toprule\nModel & Setting & Greedy PPL & MCKP PPL \\\\\n\\midrule\n\\multirow{2}{*}{Qwen-7B}  & Unconstrained    & 32.45 & 36.92 \\\\\n                            & Constrained $k{=}8$ & 11.23 & 11.23 \\\\\n\\midrule\n\\multirow{2}{*}{Qwen-14B} & Unconstrained    & 10.15 & 10.35 \\\\\n                            & Constrained $k{=}12$ & 7.18  & 7.18 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWithout the constraint, solver choice matters (PPL differences of 4.47 and 0.20 respectively).\nWith the constraint, solver choice is irrelevant ($\\Delta = 0.0000$ in both cases).\nThis pattern holds across all tested architectures, demonstrating that the constraint is the primary intervention---it simultaneously prevents compounding, enables solver interchangeability, and produces the best allocations.\n\n%% ============================================================\n%%  4  ANALYSIS\n%% ============================================================\n\\section{Analysis}\n\n\\paragraph{Contribution of constraint vs.\\ diagnostic.}\nOur results support a clear hierarchy: the cardinality constraint is effective on \\emph{all} tested architectures (6/6), while the benefit of sensitivity-aware allocation beyond the constraint is architecture-dependent.\nOn Spread models (Qwen-7B), constrained MCKP achieves 27.3\\% PPL improvement.\nOn diluted-Spread models (Qwen-14B), the benefit is a modest 7.9\\%.\nOn non-Spread models (4/6), uniform 4-bit with the constraint is optimal or near-optimal.\nThe diagnostic tells practitioners \\emph{when} to invest in profiling and non-uniform allocation; the constraint provides \\emph{universal insurance} against solver over-allocation.\n\n\\paragraph{The role of GQA ratio.}\nYi-1.5-9B (GQA 8:1) has the highest GQA ratio and concentration (0.71) in our study but gains nothing from MCKP ($\\approx$0\\%).\nThis definitively refutes the naive hypothesis that higher GQA ratios lead to greater MCKP benefit.\nThe critical factor is the \\emph{shape} of the sensitivity distribution: Yi-1.5's sensitivity is concentrated in a single extreme outlier (L4H3, $\\delta = 13.12$, $\\tratio = 0.90$---spike pattern) that the solver can handle with a single 8-bit upgrade, leaving no room for multi-head optimization.\nQwen-7B's sensitivity is distributed across a cluster of four heads in Layer~0 ($\\tratio = 0.57$---spread pattern) that creates a richer optimization landscape.\n\n\\paragraph{Concentration--benefit gradient.}\nThe six data points trace a non-trivial gradient:\nconcentration 0.22 $\\to$ $-$0.4\\% (Mistral),\n0.23 $\\to$ $-$0.35\\% (Gemma-2),\n0.47 $\\to$ +7.9\\% (Qwen-14B),\n0.57 $\\to$ +0.2\\% (Llama),\n0.61 $\\to$ +27.3\\% (Qwen-7B),\n0.71 $\\to$ $\\approx$0\\% (Yi-1.5).\nThe non-monotonicity (Yi-1.5 at 0.71 provides 0\\% despite high concentration) demonstrates precisely why $\\tratio$ is needed as a second dimension: concentration captures \\emph{how much} sensitivity is concentrated, while $\\tratio$ captures \\emph{how it is concentrated} (cluster vs.\\ single outlier).\n\n\\paragraph{Universality of the cardinality constraint.}\nThe constraint prevents degradation through different mechanisms depending on the architecture:\non Spread models, it caps the number of heads entering the compounding regime;\non Flat models (e.g., Gemma-2), it prevents solvers from assigning many heads to 2-bit when per-head distortions are indistinguishable (106 $\\to$ 8 heads);\non Spike models, the constraint is non-binding (solvers naturally assign few heads to 2-bit).\nIn all cases, the effect is beneficial or neutral, never harmful.\n\n%% ============================================================\n%%  5  CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe presented a systematic study of per-head KV cache quantization sensitivity across six transformer architectures.\nOur central finding is that a cardinality constraint on 2-bit head assignments is a simple, universal intervention that prevents compounding degradation, makes solver choice irrelevant, and yields up to 27.3\\% PPL improvement on favorable architectures.\n\nAn empirical decision rule based on top-5\\% concentration (approximately $\\ge 0.50$) and top-1/top-5 ratio (approximately $\\le 0.70$) correctly classifies all five non-borderline architectures.\nThe sixth architecture (Qwen2.5-14B) falls on the decision boundary with a modest 7.9\\% benefit, demonstrating that the thresholds are soft boundaries and that benefit degrades continuously with concentration.\nWe position this rule as a directional heuristic for practitioners, not a definitive diagnostic framework.\n\n\\paragraph{Limitations.}\nOur study has several limitations.\n(1) Only one architecture (Qwen2.5-7B) is a confirmed Spread case with strong MCKP benefit; boundary behavior (14B) provides directional evidence that benefit degrades continuously, but $N = 1$ confirmed Spread limits the generalizability of the strong-benefit claim.\n(2) The 14B downstream improvement (+0.7pp average) lacks multi-seed confidence intervals.\n(3) The compounding super-additivity observation (Section~\\ref{sec:compounding}) is characterized on a single model.\n(4) The dilution mechanism linking GQA 5:1 to the diluted spread pattern is a hypothesis supported by one comparison (7B vs.\\ 14B within Qwen2.5) but not validated across model families.\n(5) We do not evaluate KV cache eviction policies, though our profiling framework extends naturally to that setting.\n\n\\paragraph{Future work.}\nCross-architecture compounding characterization, per-layer budget allocation, and integration with KV cache eviction methods are natural extensions.\nValidating the decision rule on additional Spread architectures (if they exist) would strengthen the diagnostic from an empirical heuristic to a more robust framework.\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "baac8457-dca7-40bb-a383-9089ff24cf16",
  "isSidechain": false,
  "requestId": "req_011Cb49UupurLYCnpfsxSv6G",
  "type": "assistant",
  "uuid": "c22e1e58-80a2-4a0d-8bb7-04b773101f73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrAeCoatKNUwJwvZDP9FwR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 203,
      "cache_read_input_tokens": 47019,
      "output_tokens": 10633,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 203,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10633,
          "cache_read_input_tokens": 47019,
          "cache_creation_input_tokens": 203,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 203
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

_source line 23 · 2026-05-15T09:53:56.184Z_

<details><summary>↩ Tool result · `toolu_01RpPgiA3Mm3Vs9YzW3YR1eN`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c22e1e58-80a2-4a0d-8bb7-04b773101f73",
  "isSidechain": false,
  "promptId": "9b38a89f-3817-47d6-8645-8990dd1a76c4",
  "type": "user",
  "uuid": "a970f38d-5442-4faf-9f0e-2bb8480c9391",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{microtype}\n\n\\newcommand{\\topkconc}{\\ensuremath{c_5}}\n\\newcommand{\\tratio}{\\ensuremath{t_1/t_5}}\n\n\\title{When Does Non-Uniform KV Cache Quantization Help?\\\\\nCardinality Constraints, Sensitivity Diagnostics,\\\\and a Six-Architecture Study}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%%  ABSTRACT\n%% ============================================================\n\\begin{abstract}\nPer-head mixed-precision KV cache quantization promises better quality--compression tradeoffs than uniform quantization, but two fundamental questions remain open: \\emph{when} does non-uniform allocation actually help, and \\emph{how} should existing solvers (greedy, MCKP) be adapted to hardware-aligned non-consecutive bit-widths \\{2,4,8,16\\}?\nWe present a systematic study across six transformer architectures (Qwen2.5-7B/14B, Yi-1.5-9B, Llama-3.1-8B, Mistral-7B, Gemma-2-9B) spanning GQA ratios from 2:1 to 8:1.\nOur main finding is that a cardinality constraint---limiting the number of heads assigned to extreme (2-bit) quantization---is a simple, sufficient, and universal intervention: it prevents compounding degradation on all tested architectures, reduces the solver search space so that greedy and MCKP produce identical allocations ($\\Delta=0.0000$ PPL), and yields up to 27.3\\% PPL improvement over uniform 4-bit on architectures with favorable sensitivity distributions.\nWe further propose an empirical decision rule based on two profiling metrics (top-5\\% concentration $\\gtrsim 0.50$ and $t_1/t_5 \\lesssim 0.70$) that correctly classifies all five non-borderline architectures as beneficial or non-beneficial.\nThe sixth architecture (Qwen2.5-14B) falls on the decision boundary, exhibiting a modest 7.9\\% benefit that illustrates the threshold as a soft boundary rather than a hard cutoff.\nThese results provide practitioners with both a universal method fix and a two-metric check for when mixed-precision KV cache quantization is worthwhile.\n\\end{abstract}\n\n%% ============================================================\n%%  1  INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nKV cache quantization is a standard approach for reducing memory footprint during autoregressive inference in large language models.\nMost deployed systems apply a \\emph{uniform} bit-width---typically 4-bit---to all attention heads.\nPer-head \\emph{mixed-precision} allocation, where each head receives a bit-width proportional to its quantization sensitivity, offers a principled route to better quality--compression tradeoffs.\nAlgorithms such as the greedy R-D solver of RateQuant and integer-programming formulations (MCKP) provide optimal or near-optimal allocations under additive distortion models.\n\nHowever, when the target bit-widths are the hardware-aligned non-consecutive set \\{2, 4, 8, 16\\}, two problems emerge.\nFirst, \\emph{unconstrained} solvers fail catastrophically on certain architectures: on Qwen2.5-7B, both greedy (PPL 32.45) and MCKP (PPL 36.92) produce allocations far worse than uniform 4-bit (PPL 15.45).\nThis 3.31$\\times$ degradation stems from compounding effects---per-head profiling distortions are non-additive when many heads are simultaneously assigned extreme quantization, and solvers cannot account for this.\nSecond, \\emph{when} non-uniform allocation helps is unknown: is the benefit universal, or architecture-dependent?\n\nWe address both questions through a six-architecture study.\nOur contributions, ordered by generality:\n\n\\begin{enumerate}\n    \\item \\textbf{Cardinality constraint as universal fix.}\n    A single constraint---$\\max\\_2\\text{bit} \\le k$---prevents compounding degradation on all six architectures, makes solver choice irrelevant (constrained greedy $=$ constrained MCKP), and yields 27.3\\% PPL improvement on the most favorable architecture.\n    The constraint is effective on catastrophic (Qwen-7B, 3.31$\\times$), moderate (Gemma-2, 1.47$\\times$; Qwen-14B, 1.56$\\times$), and mild (Yi, Llama, Mistral, 1.07--1.08$\\times$) degradation regimes alike.\n\n    \\item \\textbf{Sensitivity distribution taxonomy.}\n    Head sensitivity distributions fall into three shapes---Spread (cluster of sensitive heads), Spike (single outlier), and Flat (near-uniform)---that predict whether MCKP can exploit heterogeneity.\n    Neither GQA ratio nor concentration alone is sufficient: Yi-1.5-9B (GQA 8:1, concentration 0.71) gains nothing, while Qwen2.5-7B (GQA 7:1, concentration 0.61) gains 27.3\\%.\n\n    \\item \\textbf{Empirical decision rule.}\n    A joint condition (concentration in the range 0.45--0.55 AND $\\tratio \\lesssim 0.70$) correctly classifies all five non-borderline architectures.\n    We present this as a directional heuristic, not a hard cutoff, and discuss the boundary case (Qwen2.5-14B, concentration 0.47, $\\tratio = 0.72$) that yields a modest but genuine 7.9\\% benefit.\n\\end{enumerate}\n\n%% ============================================================\n%%  2  METHOD\n%% ============================================================\n\\section{Method}\n\n\\subsection{Per-Head Sensitivity Profiling}\n\nFor each KV head $h$ in a model with $H$ total KV heads, we measure the 2-bit distortion delta $\\delta_h$: the perplexity increase when head $h$ alone is quantized from the baseline precision to 2-bit, holding all other heads at 4-bit.\nWe use a high-resolution protocol (64 calibration sequences $\\times$ 2048 tokens) to obtain stable per-head estimates.\n\nTwo summary statistics characterize the sensitivity distribution:\n\\begin{itemize}\n    \\item \\textbf{Top-5\\% concentration} (\\topkconc): the fraction of total sensitivity mass held by the top 5\\% of heads.\n    High \\topkconc{} indicates a few heads dominate.\n    \\item \\textbf{Top-1 / Top-5 ratio} (\\tratio): the sensitivity of the single most sensitive head divided by the 5th most sensitive.\n    High \\tratio{} indicates a single outlier (spike); low \\tratio{} indicates a cluster (spread).\n\\end{itemize}\n\n\\subsection{Mixed-Precision Allocation via MCKP}\n\nGiven a memory budget $B$ (as a fraction of full-precision KV cache size), we allocate each head to a bit-width from $\\mathcal{B} = \\{2, 4, 8, 16\\}$ to minimize total perplexity.\nThis is a Multiple-Choice Knapsack Problem (MCKP): each head is an ``item group'' with four choices (one per bit-width), and the knapsack capacity is $B$.\nWe solve both the MCKP formulation and a greedy approximation.\n\n\\subsection{Cardinality Constraint}\n\nWe augment the allocation problem with a cardinality constraint: at most $k$ heads may be assigned 2-bit precision.\nThis prevents compounding degradation from non-additive profiling errors.\nThe optimal $k$ can be determined via a small-scale ablation: sweep $k \\in \\{0, 4, 8, \\ldots\\}$ and select the $k$ minimizing validation PPL.\n\nUnder this constraint, the feasible set shrinks sufficiently that greedy and MCKP produce identical bit allocations on all tested models ($\\Delta_{\\text{PPL}} = 0.0000$).\n\n\\subsection{Empirical Decision Rule}\n\nWe propose a two-metric decision rule for practitioners:\n\\begin{quote}\n    If \\topkconc{} is approximately $\\ge 0.50$ \\textbf{and} \\tratio{} is approximately $\\le 0.70$, invest in profiling + constrained MCKP.\n    Otherwise, uniform 4-bit quantization suffices at moderate compression.\n\\end{quote}\nThis is an empirical heuristic validated on six architectures.\nThe thresholds represent soft boundaries: models near the boundary (concentration in the range 0.45--0.55) may see modest but real benefits.\n\n%% ============================================================\n%%  3  EXPERIMENTS\n%% ============================================================\n\\section{Experiments}\n\nAll experiments use WikiText-2 for calibration and test evaluation unless otherwise noted.\nCompression target is 4$\\times$ (budget = 0.25) unless stated.\nDownstream evaluations use 0-shot accuracy on ARC-Challenge, HellaSwag, PIQA, and WinoGrande.\n\n\\subsection{Sensitivity Profiling: Qwen2.5-14B}\n\\label{sec:profiling_14b}\n\nTable~\\ref{tab:14b_topheads} shows the top-10 sensitive heads of Qwen2.5-14B (48 layers $\\times$ 8 KV heads = 384 total, GQA 5:1).\nTop-5\\% concentration is 0.47 and $\\tratio = 0.72$, both near the decision boundary.\nLayer~0 contributes 5 of the top 19 heads (26\\%), indicating a diluted version of Qwen-7B's Layer-0 cluster.\nWe term this pattern \\emph{diluted spread}: the architectural signature of sensitivity clustering is present but attenuated by the larger head count.\n\n\\begin{table}[t]\n\\centering\n\\caption{Qwen2.5-14B: top-10 sensitive KV heads by 2-bit distortion delta (hires profiling, 64 seq $\\times$ 2048 tok).}\n\\label{tab:14b_topheads}\n\\begin{tabular}{lc}\n\\toprule\nHead & $\\delta_{\\text{2bit}}$ \\\\\n\\midrule\nL0H0  & 3.21 \\\\\nL0H3  & 2.78 \\\\\nL0H5  & 2.14 \\\\\nL8H2  & 1.82 \\\\\nL0H1  & 1.53 \\\\\nL12H6 & 1.31 \\\\\nL0H7  & 1.18 \\\\\nL5H4  & 0.98 \\\\\nL15H1 & 0.87 \\\\\nL0H2  & 0.82 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe coefficient of variation (CV = 3.85) is higher than flat-distribution models (Mistral 1.31, Gemma-2 1.28) but lower than Qwen-7B, confirming that heterogeneity is intermediate.\nThe GQA ratio of 5:1 (vs.\\ 7:1 for the 7B model) yields 8 KV heads per layer rather than 4, which may contribute to the dilution of the Layer-0 cluster effect.\n\n\\subsection{Constrained Allocation and $k$ Ablation: Qwen2.5-14B}\n\\label{sec:constrained_14b}\n\nTable~\\ref{tab:14b_k_ablation} shows the $k$-ablation sweep.\nThe optimal constraint is $k = 12$, yielding PPL 7.18 versus 7.80 for uniform 4-bit---a 7.9\\% improvement.\nThe U-shaped PPL curve is shallow: from $k = 8$ to $k = 20$, PPL varies by less than 0.10, reflecting the smoother sensitivity distribution compared to Qwen-7B.\nBeyond $k = 32$, compounding effects become visible.\n\n\\begin{table}[t]\n\\centering\n\\caption{Qwen2.5-14B: $k$-ablation at budget = 0.25 (384 KV heads).}\n\\label{tab:14b_k_ablation}\n\\begin{tabular}{rll}\n\\toprule\n$k$ (max 2-bit) & PPL & Note \\\\\n\\midrule\n0  & 7.80 & = uniform 4-bit \\\\\n4  & 7.52 & \\\\\n8  & 7.28 & \\\\\n12 & \\textbf{7.18} & optimal \\\\\n16 & 7.21 & \\\\\n20 & 7.28 & \\\\\n24 & 7.38 & \\\\\n32 & 7.65 & compounding visible \\\\\n48 & 8.42 & compounding dominant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nConstrained greedy and constrained MCKP produce identical results at $k = 12$ ($\\Delta = 0.0000$), confirming that solver equivalence under cardinality constraint holds on this architecture as well (Table~\\ref{tab:14b_allocation}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Qwen2.5-14B: allocation comparison at budget = 0.25.}\n\\label{tab:14b_allocation}\n\\begin{tabular}{lcl}\n\\toprule\nMethod & PPL & Note \\\\\n\\midrule\nBaseline BF16        & 6.50 & --- \\\\\nUniform 4-bit        & 7.80 & --- \\\\\nMCKP constrained $k{=}12$  & \\textbf{7.18} & +7.9\\% vs uniform \\\\\nGreedy constrained $k{=}12$ & \\textbf{7.18} & $\\Delta = 0.0000$ vs MCKP \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 7.9\\% improvement far exceeds the noise range observed on flat-distribution models (Gemma-2: $-0.35\\%$, Mistral: $-0.48\\%$), indicating a genuine positive signal.\nHowever, it is substantially below Qwen-7B's 27.3\\%, consistent with the lower concentration.\nThe gap recovery is 47.7\\% (vs.\\ 80.8\\% for the 7B model).\n\n\\subsection{Unconstrained vs.\\ Constrained: Qwen2.5-14B}\n\\label{sec:unconstrained_14b}\n\nTable~\\ref{tab:14b_unconstrained} compares unconstrained and constrained allocation.\nUnconstrained greedy produces 1.56$\\times$ baseline degradation, placing 14B in the \\emph{moderate} tier alongside Gemma-2 (1.47$\\times$), between the catastrophic regime (Qwen-7B, 3.31$\\times$) and the mild regime (Yi/Llama/Mistral, 1.07--1.08$\\times$).\n\n\\begin{table}[t]\n\\centering\n\\caption{Qwen2.5-14B: unconstrained vs.\\ constrained comparison.}\n\\label{tab:14b_unconstrained}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & PPL & $\\times$ baseline & 2-bit heads (\\%) \\\\\n\\midrule\nBaseline BF16              & 6.50  & 1.00$\\times$ & --- \\\\\nUniform 4-bit              & 7.80  & 1.20$\\times$ & 0 (0\\%) \\\\\nGreedy unconstrained       & 10.15 & 1.56$\\times$ & 58 (15.1\\%) \\\\\nMCKP unconstrained         & 10.35 & 1.59$\\times$ & 62 (16.1\\%) \\\\\nGreedy constrained $k{=}12$  & \\textbf{7.18}  & 1.10$\\times$ & 12 (3.1\\%) \\\\\nMCKP constrained $k{=}12$    & \\textbf{7.18}  & 1.10$\\times$ & 12 (3.1\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe constraint reduces PPL from 10.15 to 7.18 (29.3\\% improvement), confirming that the cardinality constraint is effective not only on catastrophic cases (Qwen-7B) but also on moderate degradation regimes.\nUnder unconstrained allocation, solver choice matters (greedy 10.15 vs.\\ MCKP 10.35); under the constraint, it does not ($\\Delta = 0.0000$).\nThis pattern is consistent across all tested architectures.\n\n\\subsection{Gemma-2-9B: BOS-Fixed Constrained Evaluation}\n\\label{sec:gemma2}\n\nWe re-evaluated Gemma-2-9B using corrected BOS-prepend sliding-window evaluation (stride = 512, max\\_length = 2048), replacing earlier results affected by a BOS handling bug.\nTable~\\ref{tab:gemma2_bos} reports updated numbers.\n\n\\begin{table}[t]\n\\centering\n\\caption{Gemma-2-9B: BOS-fixed results (336 KV heads, budget = 0.25).}\n\\label{tab:gemma2_bos}\n\\begin{tabular}{lcl}\n\\toprule\nMethod & PPL & Note \\\\\n\\midrule\nBaseline BF16            & 6.03 & BOS-fixed \\\\\nUniform 4-bit            & 6.17 & BOS-fixed \\\\\nMCKP constrained $k{=}8$  & 6.19 & $-0.35\\%$ vs uniform \\\\\nGreedy unconstrained     & 8.85 & 1.47$\\times$ baseline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Gemma-2-9B: $k$-ablation (BOS-fixed, 336 heads).}\n\\label{tab:gemma2_k}\n\\begin{tabular}{rcl}\n\\toprule\n$k$ & PPL & Note \\\\\n\\midrule\n0  & 6.17 & = uniform \\\\\n4  & 6.17 & $\\approx$ uniform \\\\\n8  & 6.19 & best $k$ (marginal) \\\\\n12 & 6.22 & \\\\\n16 & 6.25 & \\\\\n24 & 6.31 & monotonic increase \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe BOS fix substantially changes absolute PPL (8.9 $\\to$ 6.03 for baseline) but does not change relative conclusions.\nThe flat sensitivity distribution (concentration 0.23, CV 1.28) means the profiler cannot meaningfully differentiate heads; any non-uniform allocation is noise-driven.\nThe $k$--PPL curve is approximately monotonically increasing, similar to Mistral---every additional 2-bit head adds equal damage.\nThe constraint's value on Gemma-2 is not in enabling MCKP optimization but in \\emph{preventing over-allocation}: unconstrained solvers assign 106 of 336 heads (31.5\\%) to 2-bit, producing the 1.47$\\times$ moderate degradation; the constraint caps this at 8 heads, bringing PPL within 0.35\\% of uniform.\n\n\\subsection{Decision Rule Validation Across Six Architectures}\n\\label{sec:decision_rule}\n\nTable~\\ref{tab:decision_rule} evaluates the joint diagnostic ($\\topkconc \\gtrsim 0.50$ AND $\\tratio \\lesssim 0.70$) on all six architectures.\n\n\\begin{table}[t]\n\\centering\n\\caption{Joint diagnostic evaluation across six architectures. Conc.\\ = top-5\\% concentration.}\n\\label{tab:decision_rule}\n\\small\n\\begin{tabular}{lccccccl}\n\\toprule\nModel & GQA & Conc. & $\\tratio$ & Shape & MCKP $\\Delta$ & Rule pred. & Correct? \\\\\n\\midrule\nQwen2.5-7B  & 7:1 & 0.61 & 0.57 & Spread         & +27.3\\%      & beneficial     & \\checkmark \\\\\nYi-1.5-9B   & 8:1 & 0.71 & 0.90 & Spike          & $\\approx$0\\% & non-benef.     & \\checkmark \\\\\nLlama-3.1-8B & 4:1 & 0.57 & 0.71 & Spike (border) & +0.2\\%       & non-benef.     & \\checkmark \\\\\nMistral-7B  & 4:1 & 0.22 & 0.18 & Flat           & $-$0.4\\%     & non-benef.     & \\checkmark \\\\\nGemma-2-9B  & 2:1 & 0.23 & 0.38 & Flat           & $-$0.35\\%    & non-benef.     & \\checkmark \\\\\nQwen2.5-14B & 5:1 & 0.47 & 0.72 & Diluted Spread & +7.9\\%       & non-benef.     & $\\times$ (boundary) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe rule correctly classifies all five non-borderline architectures.\nQwen2.5-14B (concentration 0.47, $\\tratio = 0.72$) falls in the boundary zone, narrowly missing both thresholds (by 0.03 and 0.02 respectively).\nIts 7.9\\% benefit constitutes a type-II error (false negative) under hard thresholds.\nThis illustrates that the diagnostic thresholds represent soft boundaries rather than hard cutoffs---the benefit degrades continuously with concentration rather than vanishing at a sharp threshold.\n\n\\paragraph{14B as boundary case.}\nThe boundary behavior of Qwen2.5-14B deserves separate discussion.\nIts 7.9\\% constrained improvement lies between the strong positive (Qwen-7B, 27.3\\%) and the non-beneficial models ($\\le 0.2\\%$), precisely where a continuous concentration--benefit relationship predicts.\nThe diluted spread pattern---a structural sensitivity cluster in Layer~0 that is attenuated by having 8 rather than 4 KV heads per layer---represents a third distribution shape beyond the original Spread and Spike/Flat categories.\nWe interpret the decision rule as a \\emph{directional heuristic}: models clearly above both thresholds benefit strongly, models clearly below do not, and models near the boundary may see modest gains whose practical value depends on deployment constraints.\nThe rule achieves 5/6 accuracy (5/5 on non-borderline cases), with the single boundary error being conservative (type-II: missing a modest positive) rather than aggressive (type-I: incorrectly recommending costly profiling).\n\n\\subsection{Cross-Architecture Summary}\n\\label{sec:cross_arch}\n\nTable~\\ref{tab:cross_arch} presents the complete evidence across all six architectures.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Cross-architecture evidence summary (6 models). Constrained $\\Delta$ is PPL improvement of constrained MCKP vs.\\ uniform 4-bit at budget = 0.25.}\n\\label{tab:cross_arch}\n\\small\n\\begin{tabular}{lccccccl}\n\\toprule\nModel & GQA & KV Heads & Conc. & Uncons.\\ $\\times$base & Constrained $\\Delta$ & Shape & Verdict \\\\\n\\midrule\nQwen2.5-7B   & 7:1 & 112 & 0.61 & 3.31$\\times$ & +27.3\\% & Spread         & Strong positive \\\\\nQwen2.5-14B  & 5:1 & 384 & 0.47 & 1.56$\\times$ & +7.9\\%  & Diluted Spread & Boundary positive \\\\\nGemma-2-9B   & 2:1 & 336 & 0.23 & 1.47$\\times$ & $-$0.35\\% & Flat         & Negative \\\\\nYi-1.5-9B    & 8:1 & 192 & 0.71 & 1.08$\\times$ & $\\approx$0\\% & Spike     & GQA counterexample \\\\\nLlama-3.1-8B & 4:1 & 256 & 0.57 & 1.07$\\times$ & +0.2\\%  & Spike (border) & Marginal \\\\\nMistral-7B   & 4:1 & 256 & 0.22 & 1.08$\\times$ & $-$0.4\\% & Flat          & Negative \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Three-tier unconstrained degradation.}\nUnconstrained allocation degradation follows a concentration-dependent gradient organized into three tiers:\n\\begin{itemize}\n    \\item \\textbf{Catastrophic} ($>$2$\\times$): Qwen-7B (3.31$\\times$)---Spread pattern with strong Layer-0 compounding.\n    \\item \\textbf{Moderate} (1.4--1.6$\\times$): Gemma-2 (1.47$\\times$) and Qwen-14B (1.56$\\times$)---solver over-allocation from either indistinguishable distortions (flat) or diluted sensitivity clusters.\n    \\item \\textbf{Mild} (1.07--1.08$\\times$): Yi, Llama, Mistral---solvers assign few heads to 2-bit.\n\\end{itemize}\nNotably, Gemma-2 and Qwen-14B reach moderate degradation through different mechanisms (flat over-allocation vs.\\ diluted spread compounding), yet the cardinality constraint is effective on both.\nThis strengthens the ``universal fix'' characterization.\n\n\\subsection{Downstream Task Evaluation: Qwen2.5-14B}\n\\label{sec:downstream_14b}\n\nTable~\\ref{tab:14b_downstream} shows 0-shot downstream results on Qwen2.5-14B at 4$\\times$ compression.\n\n\\begin{table}[t]\n\\centering\n\\caption{Qwen2.5-14B downstream task results (0-shot, 4$\\times$ compression).}\n\\label{tab:14b_downstream}\n\\begin{tabular}{lcccc}\n\\toprule\nTask & BF16 & Uniform 4-bit & MCKP $k{=}12$ & $\\Delta$ (pp) \\\\\n\\midrule\nARC-Challenge & 0.565 & 0.548 & 0.557 & +0.9 \\\\\nHellaSwag     & 0.800 & 0.785 & 0.793 & +0.8 \\\\\nPIQA          & 0.805 & 0.798 & 0.802 & +0.4 \\\\\nWinoGrande    & 0.715 & 0.705 & 0.712 & +0.7 \\\\\n\\midrule\nAverage       & 0.721 & 0.709 & 0.716 & +0.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll four tasks show positive deltas (+0.4 to +0.9 percentage points), with 58.3\\% average gap recovery.\nThis is consistent with the PPL improvement: Qwen-7B's 27.3\\% PPL gain translates to +2.6pp average downstream, while 14B's 7.9\\% PPL gain translates to +0.7pp---roughly proportional.\nHowever, without multi-seed confidence intervals, the per-task deltas (+0.4 to +0.9pp) are within typical single-run noise.\nWe describe the signal as \\emph{modest but consistent across all four tasks}.\n\n\\paragraph{Cross-architecture downstream comparison.}\nAcross prior experiments on five architectures, the diagnostic correctly predicts downstream outcomes:\nQwen-7B (Spread) shows +1.25 to +4.00pp gains across four tasks (72.8\\% recovery);\nYi-1.5 (Spike) shows $-0.77$pp average;\nLlama (Spike) shows $-0.99$pp average with 0/5 tasks positive---systematic degradation;\nMistral (Flat) shows $-0.48$pp average;\nGemma-2 (Flat) shows $+0.14$pp average (noise range).\nARC-Challenge exhibits the largest per-task sensitivity to allocation strategy across all models (Yi $-3.24$pp, Llama $-2.65$pp), consistent with its reliance on multi-step reasoning where subtle KV cache errors accumulate.\n\n\\subsection{Compounding Super-Additivity}\n\\label{sec:compounding}\n\nWe examine the compounding effect by comparing random-$k$ versus top-$k$ 2-bit head selection on Qwen2.5-7B (Table~\\ref{tab:compounding}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Compounding super-additivity: random-$k$ vs.\\ top-$k$ 2-bit assignment on Qwen2.5-7B.}\n\\label{tab:compounding}\n\\begin{tabular}{rccr}\n\\toprule\n$k$ & top-$k$ PPL & random-$k$ PPL (mean$\\pm$std) & Ratio \\\\\n\\midrule\n1  & 9.826  & 9.887$\\pm$0.05  & 1.01 \\\\\n4  & 9.849  & 10.06$\\pm$0.06  & 1.02 \\\\\n8  & 10.042 & 11.07$\\pm$0.69  & 1.10 \\\\\n16 & 10.42  & 12.91$\\pm$0.40  & 1.24 \\\\\n32 & 11.604 & 18.33$\\pm$2.53  & 1.58 \\\\\n64 & 22.946 & 55.94$\\pm$9.73  & 2.44 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAssigning randomly-selected heads to 2-bit produces disproportionately worse perplexity than assigning the highest-sensitivity heads, and this gap widens monotonically with the number of 2-bit heads.\nAt $k = 64$, random selection yields 2.44$\\times$ the degradation of sensitivity-ranked selection.\nThe variance of the random baseline also grows substantially (std from 0.05 at $k{=}1$ to 9.73 at $k{=}64$), reflecting the increasing influence of which specific heads are forced to extreme quantization.\nThis super-additive behavior motivates the cardinality constraint: by limiting the number of extreme-quantization assignments, the constraint prevents compounding from low-sensitivity heads that individually appear harmless but collectively degrade quality.\nWe present this as an empirical observation on a single architecture rather than a formal proposition, and note that cross-architecture characterization of compounding behavior is an open direction.\n\n\\subsection{Solver Equivalence Under Constraint}\n\nA consistent finding across all six architectures is that the cardinality constraint eliminates solver dependence.\nTable~\\ref{tab:solver_equiv} summarizes the unconstrained and constrained solver comparison for the primary showcase (Qwen-7B) and the boundary case (Qwen-14B).\n\n\\begin{table}[t]\n\\centering\n\\caption{Solver equivalence: greedy vs.\\ MCKP, unconstrained vs.\\ constrained.}\n\\label{tab:solver_equiv}\n\\begin{tabular}{llcc}\n\\toprule\nModel & Setting & Greedy PPL & MCKP PPL \\\\\n\\midrule\n\\multirow{2}{*}{Qwen-7B}  & Unconstrained    & 32.45 & 36.92 \\\\\n                            & Constrained $k{=}8$ & 11.23 & 11.23 \\\\\n\\midrule\n\\multirow{2}{*}{Qwen-14B} & Unconstrained    & 10.15 & 10.35 \\\\\n                            & Constrained $k{=}12$ & 7.18  & 7.18 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWithout the constraint, solver choice matters (PPL differences of 4.47 and 0.20 respectively).\nWith the constraint, solver choice is irrelevant ($\\Delta = 0.0000$ in both cases).\nThis pattern holds across all tested architectures, demonstrating that the constraint is the primary intervention---it simultaneously prevents compounding, enables solver interchangeability, and produces the best allocations.\n\n%% ============================================================\n%%  4  ANALYSIS\n%% ============================================================\n\\section{Analysis}\n\n\\paragraph{Contribution of constraint vs.\\ diagnostic.}\nOur results support a clear hierarchy: the cardinality constraint is effective on \\emph{all} tested architectures (6/6), while the benefit of sensitivity-aware allocation beyond the constraint is architecture-dependent.\nOn Spread models (Qwen-7B), constrained MCKP achieves 27.3\\% PPL improvement.\nOn diluted-Spread models (Qwen-14B), the benefit is a modest 7.9\\%.\nOn non-Spread models (4/6), uniform 4-bit with the constraint is optimal or near-optimal.\nThe diagnostic tells practitioners \\emph{when} to invest in profiling and non-uniform allocation; the constraint provides \\emph{universal insurance} against solver over-allocation.\n\n\\paragraph{The role of GQA ratio.}\nYi-1.5-9B (GQA 8:1) has the highest GQA ratio and concentration (0.71) in our study but gains nothing from MCKP ($\\approx$0\\%).\nThis definitively refutes the naive hypothesis that higher GQA ratios lead to greater MCKP benefit.\nThe critical factor is the \\emph{shape} of the sensitivity distribution: Yi-1.5's sensitivity is concentrated in a single extreme outlier (L4H3, $\\delta = 13.12$, $\\tratio = 0.90$---spike pattern) that the solver can handle with a single 8-bit upgrade, leaving no room for multi-head optimization.\nQwen-7B's sensitivity is distributed across a cluster of four heads in Layer~0 ($\\tratio = 0.57$---spread pattern) that creates a richer optimization landscape.\n\n\\paragraph{Concentration--benefit gradient.}\nThe six data points trace a non-trivial gradient:\nconcentration 0.22 $\\to$ $-$0.4\\% (Mistral),\n0.23 $\\to$ $-$0.35\\% (Gemma-2),\n0.47 $\\to$ +7.9\\% (Qwen-14B),\n0.57 $\\to$ +0.2\\% (Llama),\n0.61 $\\to$ +27.3\\% (Qwen-7B),\n0.71 $\\to$ $\\approx$0\\% (Yi-1.5).\nThe non-monotonicity (Yi-1.5 at 0.71 provides 0\\% despite high concentration) demonstrates precisely why $\\tratio$ is needed as a second dimension: concentration captures \\emph{how much} sensitivity is concentrated, while $\\tratio$ captures \\emph{how it is concentrated} (cluster vs.\\ single outlier).\n\n\\paragraph{Universality of the cardinality constraint.}\nThe constraint prevents degradation through different mechanisms depending on the architecture:\non Spread models, it caps the number of heads entering the compounding regime;\non Flat models (e.g., Gemma-2), it prevents solvers from assigning many heads to 2-bit when per-head distortions are indistinguishable (106 $\\to$ 8 heads);\non Spike models, the constraint is non-binding (solvers naturally assign few heads to 2-bit).\nIn all cases, the effect is beneficial or neutral, never harmful.\n\n%% ============================================================\n%%  5  CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe presented a systematic study of per-head KV cache quantization sensitivity across six transformer architectures.\nOur central finding is that a cardinality constraint on 2-bit head assignments is a simple, universal intervention that prevents compounding degradation, makes solver choice irrelevant, and yields up to 27.3\\% PPL improvement on favorable architectures.\n\nAn empirical decision rule based on top-5\\% concentration (approximately $\\ge 0.50$) and top-1/top-5 ratio (approximately $\\le 0.70$) correctly classifies all five non-borderline architectures.\nThe sixth architecture (Qwen2.5-14B) falls on the decision boundary with a modest 7.9\\% benefit, demonstrating that the thresholds are soft boundaries and that benefit degrades continuously with concentration.\nWe position this rule as a directional heuristic for practitioners, not a definitive diagnostic framework.\n\n\\paragraph{Limitations.}\nOur study has several limitations.\n(1) Only one architecture (Qwen2.5-7B) is a confirmed Spread case with strong MCKP benefit; boundary behavior (14B) provides directional evidence that benefit degrades continuously, but $N = 1$ confirmed Spread limits the generalizability of the strong-benefit claim.\n(2) The 14B downstream improvement (+0.7pp average) lacks multi-seed confidence intervals.\n(3) The compounding super-additivity observation (Section~\\ref{sec:compounding}) is characterized on a single model.\n(4) The dilution mechanism linking GQA 5:1 to the diluted spread pattern is a hypothesis supported by one comparison (7B vs.\\ 14B within Qwen2.5) but not validated across model families.\n(5) We do not evaluate KV cache eviction policies, though our profiling framework extends naturally to that setting.\n\n\\paragraph{Future work.}\nCross-architecture compounding characterization, per-layer budget allocation, and integration with KV cache eviction methods are natural extensions.\nValidating the decision rule on additional Spread architectures (if they exist) would strengthen the diagnostic from an empirical heuristic to a more robust framework.\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "c22e1e58-80a2-4a0d-8bb7-04b773101f73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T085855 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts…",
  "leafUuid": "a970f38d-5442-4faf-9f0e-2bb8480c9391",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier research paper simulation",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be"
}
```

---

### Tool call

_source line 26 · 2026-05-15T09:54:00.628Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CsE8hqmFxjDcjbbVC94cs7`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper (two passes)",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a970f38d-5442-4faf-9f0e-2bb8480c9391",
  "isSidechain": false,
  "requestId": "req_011Cb49jkfB8r27pmtDzuc8H",
  "type": "assistant",
  "uuid": "f0fadcad-c0ac-4d72-9a32-c8343e436f50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JbWBcxCC2x1Nzt83hC8yUy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10695,
      "cache_read_input_tokens": 47222,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10695,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 47222,
          "cache_creation_input_tokens": 10695,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10695
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

_source line 27 · 2026-05-15T09:54:01.128Z_

<details><summary>↩ Tool result · reported error · `toolu_01CsE8hqmFxjDcjbbVC94cs7`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.sty
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype-pdftex.def)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-cmr.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msa.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msb.cfg)
Overfull \hbox (0.6004pt too wide) in paragraph at lines 31--37
\T1/cmr/m/n/10 (-20) car-di-nal-ity constraint---limiting the num-ber of heads 
as-signed to ex-treme (2-bit) quantization---
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}
! pdfTeX error (font expansion): auto expansion is only possible with scalable 
fonts.
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.61 
     
!  ==> Fatal error occurred, no output PDF file produced!
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0fadcad-c0ac-4d72-9a32-c8343e436f50",
  "isSidechain": false,
  "promptId": "9b38a89f-3817-47d6-8645-8990dd1a76c4",
  "type": "user",
  "uuid": "87baf357-cbad-4dea-9828-15a76ac9987b",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.sty\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype-pdftex.def)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-cmr.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msa.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msb.cfg)\nOverfull \\hbox (0.6004pt too wide) in paragraph at lines 31--37\n\\T1/cmr/m/n/10 (-20) car-di-nal-ity constraint---limiting the num-ber of heads \nas-signed to ex-treme (2-bit) quantization---\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}\n! pdfTeX error (font expansion): auto expansion is only possible with scalable \nfonts.\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.61 \n     \n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "f0fadcad-c0ac-4d72-9a32-c8343e436f50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-15T09:54:03.953Z_

<details><summary>Logged reasoning block</summary>

```text
Font expansion issue with microtype. Let me remove the microtype package.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87baf357-cbad-4dea-9828-15a76ac9987b",
  "isSidechain": false,
  "requestId": "req_011Cb49k7hhsXQQ7VbBCHPAo",
  "type": "assistant",
  "uuid": "021badb3-e119-4403-a4a5-102a7ca2dfa8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BN23YNx9V3WxYSqJgfhyAf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2407,
      "cache_read_input_tokens": 57917,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 196,
          "cache_read_input_tokens": 57917,
          "cache_creation_input_tokens": 2407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2407
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

_source line 29 · 2026-05-15T09:54:04.448Z_

Font expansion issue with microtype. I'll remove it and recompile.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "021badb3-e119-4403-a4a5-102a7ca2dfa8",
  "isSidechain": false,
  "requestId": "req_011Cb49k7hhsXQQ7VbBCHPAo",
  "type": "assistant",
  "uuid": "cf49c8af-f64a-4864-a548-241b7c8e5d19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BN23YNx9V3WxYSqJgfhyAf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2407,
      "cache_read_input_tokens": 57917,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 196,
          "cache_read_input_tokens": 57917,
          "cache_creation_input_tokens": 2407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2407
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

_source line 30 · 2026-05-15T09:54:05.572Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01WyqjzRxRY5PWs4NegaoRTr`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median/paper.tex",
  "old_string": "\\usepackage{microtype}",
  "new_string": "% \\usepackage{microtype}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf49c8af-f64a-4864-a548-241b7c8e5d19",
  "isSidechain": false,
  "requestId": "req_011Cb49k7hhsXQQ7VbBCHPAo",
  "type": "assistant",
  "uuid": "6e2c495d-9a04-4c84-9dc2-8b64f2ea8894",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BN23YNx9V3WxYSqJgfhyAf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2407,
      "cache_read_input_tokens": 57917,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 196,
          "cache_read_input_tokens": 57917,
          "cache_creation_input_tokens": 2407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2407
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

_source line 31 · 2026-05-15T09:54:05.584Z_

<details><summary>↩ Tool result · `toolu_01WyqjzRxRY5PWs4NegaoRTr`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e2c495d-9a04-4c84-9dc2-8b64f2ea8894",
  "isSidechain": false,
  "promptId": "9b38a89f-3817-47d6-8645-8990dd1a76c4",
  "type": "user",
  "uuid": "4fa877e5-797c-4a2b-998a-1f2c46e51ebf",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median/paper.tex",
    "oldString": "\\usepackage{microtype}",
    "newString": "% \\usepackage{microtype}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 9,
        "oldLines": 7,
        "newStart": 9,
        "newLines": 7,
        "lines": [
          " \\usepackage[margin=1in]{geometry}",
          " \\usepackage{hyperref}",
          " \\usepackage{natbib}",
          "-\\usepackage{microtype}",
          "+% \\usepackage{microtype}",
          " ",
          " \\newcommand{\\topkconc}{\\ensuremath{c_5}}",
          " \\newcommand{\\tratio}{\\ensuremath{t_1/t_5}}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "6e2c495d-9a04-4c84-9dc2-8b64f2ea8894",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-15T09:54:05.631Z_

```json
{
  "parentUuid": "4fa877e5-797c-4a2b-998a-1f2c46e51ebf",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "0ad9670c-026c-4945-a30b-c9af53bd0e5e",
  "timestamp": "2026-05-15T09:54:05.631Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 33 · 2026-05-15T09:54:08.922Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01T4bWu97h1YQSUX3195xq4f`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper (two passes, no microtype)",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ad9670c-026c-4945-a30b-c9af53bd0e5e",
  "isSidechain": false,
  "requestId": "req_011Cb49kSsNpVKRJccbqRhG4",
  "type": "assistant",
  "uuid": "42acdc01-3dd6-41a5-9290-6b6769798aba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Apyfzf96J5caL47EZTH4b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 383,
      "cache_read_input_tokens": 60324,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 383,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 60324,
          "cache_creation_input_tokens": 383,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 383
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

_source line 34 · 2026-05-15T09:54:09.811Z_

<details><summary>↩ Tool result · `toolu_01T4bWu97h1YQSUX3195xq4f`</summary>

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
nts/map/pdftex/updmap/pdftex.map}]
Overfull \hbox (9.2476pt too wide) in paragraph at lines 62--65
[]\T1/cmr/bx/n/10.95 Sensitivity dis-tri-bu-tion tax-on-omy. \T1/cmr/m/n/10.95 
Head sen-si-tiv-ity dis-tri-bu-tions fall into three shapes---
[2]

LaTeX Warning: Reference `tab:14b_topheads' on page 3 undefined on input line 1
25.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 155.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 155.


LaTeX Warning: Reference `tab:14b_k_ablation' on page 3 undefined on input line
 158.


LaTeX Warning: Reference `tab:14b_allocation' on page 3 undefined on input line
 184.

[3]

LaTeX Warning: Reference `tab:14b_unconstrained' on page 4 undefined on input l
ine 209.


LaTeX Warning: Reference `tab:gemma2_bos' on page 4 undefined on input line 238
.


LaTeX Warning: Reference `tab:decision_rule' on page 4 undefined on input line 
282.

[4]

LaTeX Warning: Reference `tab:cross_arch' on page 5 undefined on input line 318
.


Overfull \hbox (85.17824pt too wide) in paragraph at lines 325--337
 [][] 
[5]

LaTeX Warning: Reference `tab:14b_downstream' on page 6 undefined on input line
 352.


LaTeX Warning: Reference `tab:compounding' on page 6 undefined on input line 38
9.

[6]

LaTeX Warning: Reference `tab:solver_equiv' on page 7 undefined on input line 4
18.

[7] [8]

LaTeX Warning: Reference `sec:compounding' on page 9 undefined on input line 49
2.

[9] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho
me/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/symbols/msam10.pfb>
Output written on paper.pdf (9 pages, 216454 bytes).
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
nts/map/pdftex/updmap/pdftex.map}]
Overfull \hbox (9.2476pt too wide) in paragraph at lines 62--65
[]\T1/cmr/bx/n/10.95 Sensitivity dis-tri-bu-tion tax-on-omy. \T1/cmr/m/n/10.95 
Head sen-si-tiv-ity dis-tri-bu-tions fall into three shapes---
[2]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 155.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 155.

[3] [4]
Overfull \hbox (85.17824pt too wide) in paragraph at lines 325--337
 [][] 
[5] [6] [7] [8] [9] (./paper.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho
me/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/symbols/msam10.pfb>
Output written on paper.pdf (9 pages, 217766 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42acdc01-3dd6-41a5-9290-6b6769798aba",
  "isSidechain": false,
  "promptId": "9b38a89f-3817-47d6-8645-8990dd1a76c4",
  "type": "user",
  "uuid": "d5e2d798-5271-443a-9852-a21b3d449c46",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}]\nOverfull \\hbox (9.2476pt too wide) in paragraph at lines 62--65\n[]\\T1/cmr/bx/n/10.95 Sensitivity dis-tri-bu-tion tax-on-omy. \\T1/cmr/m/n/10.95 \nHead sen-si-tiv-ity dis-tri-bu-tions fall into three shapes---\n[2]\n\nLaTeX Warning: Reference `tab:14b_topheads' on page 3 undefined on input line 1\n25.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 155.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 155.\n\n\nLaTeX Warning: Reference `tab:14b_k_ablation' on page 3 undefined on input line\n 158.\n\n\nLaTeX Warning: Reference `tab:14b_allocation' on page 3 undefined on input line\n 184.\n\n[3]\n\nLaTeX Warning: Reference `tab:14b_unconstrained' on page 4 undefined on input l\nine 209.\n\n\nLaTeX Warning: Reference `tab:gemma2_bos' on page 4 undefined on input line 238\n.\n\n\nLaTeX Warning: Reference `tab:decision_rule' on page 4 undefined on input line \n282.\n\n[4]\n\nLaTeX Warning: Reference `tab:cross_arch' on page 5 undefined on input line 318\n.\n\n\nOverfull \\hbox (85.17824pt too wide) in paragraph at lines 325--337\n [][] \n[5]\n\nLaTeX Warning: Reference `tab:14b_downstream' on page 6 undefined on input line\n 352.\n\n\nLaTeX Warning: Reference `tab:compounding' on page 6 undefined on input line 38\n9.\n\n[6]\n\nLaTeX Warning: Reference `tab:solver_equiv' on page 7 undefined on input line 4\n18.\n\n[7] [8]\n\nLaTeX Warning: Reference `sec:compounding' on page 9 undefined on input line 49\n2.\n\n[9] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/symbols/msam10.pfb>\nOutput written on paper.pdf (9 pages, 216454 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}]\nOverfull \\hbox (9.2476pt too wide) in paragraph at lines 62--65\n[]\\T1/cmr/bx/n/10.95 Sensitivity dis-tri-bu-tion tax-on-omy. \\T1/cmr/m/n/10.95 \nHead sen-si-tiv-ity dis-tri-bu-tions fall into three shapes---\n[2]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 155.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 155.\n\n[3] [4]\nOverfull \\hbox (85.17824pt too wide) in paragraph at lines 325--337\n [][] \n[5] [6] [7] [8] [9] (./paper.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/symbols/msam10.pfb>\nOutput written on paper.pdf (9 pages, 217766 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "42acdc01-3dd6-41a5-9290-6b6769798aba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T085855 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts…",
  "leafUuid": "d5e2d798-5271-443a-9852-a21b3d449c46",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier research paper simulation",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be"
}
```

---

### Assistant

_source line 37 · 2026-05-15T09:54:25.645Z_

编译成功，生成 9 页 PDF。

`paper.pdf` 已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median/paper.pdf`。

论文结构覆盖 experiment_data.json 中全部 8 个实验：
- **§3.1** 14B profiling（diluted spread, conc=0.47, t₁/t₅=0.72）
- **§3.2** 14B constrained MCKP + k-ablation（optimal k=12, +7.9%）
- **§3.3** 14B unconstrained vs constrained（1.56× → 1.10×, 29.3% improvement）
- **§3.4** Gemma-2 BOS-fixed（baseline 6.03, -0.35% noise）
- **§3.5** Decision rule 6-model validation（5/5 non-borderline correct, 14B as type-II boundary）
- **§3.6** Cross-architecture summary table（三档分类：catastrophic/moderate/mild）
- **§3.7** 14B downstream（+0.7pp avg, all positive, 58.3% recovery）
- **§3.8** W9 compounding super-additivity（observation only, ratio 1.01→2.44）
- **§3.9** Solver equivalence（greedy=MCKP under constraint）

Narrative guidance 要求全部落实：Claim 3 保持 empirical decision rule；14B boundary case 单独段落；threshold 软化为 0.45-0.55 range；W9 降为 empirical observation；contribution 重心在 constraint universality。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5e2d798-5271-443a-9852-a21b3d449c46",
  "isSidechain": false,
  "requestId": "req_011Cb49kkq7p7ssmugLgKTDu",
  "type": "assistant",
  "uuid": "39855fea-37cc-4b26-8c1f-a0ad92cfb439",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/median",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GeMDYymEG1tsvoCebVhGJf",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6459,
      "cache_read_input_tokens": 60707,
      "output_tokens": 457,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6459,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 457,
          "cache_read_input_tokens": 60707,
          "cache_creation_input_tokens": 6459,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6459
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

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T085855 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts…",
  "leafUuid": "39855fea-37cc-4b26-8c1f-a0ad92cfb439",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier research paper simulation",
  "sessionId": "2c174715-22f6-4523-8f31-a43aaee0d5be"
}
```

---
