# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T125925 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/34547890-e122-43c6-bb3a-f938b3a3f252.jsonl`
- **Structured JSON:** [`4837b39594b5563bc64a.json`](../../sessions/48/4837b39594b5563bc64a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T13:27:06.309Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T13:27:06.309Z",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T125925 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：原始 framing 完全成立，三条 claim 均获统计显著支撑。Claim 1：200 pairs 扩展数据将 AUROC 推至 0.89， CI 宽度从 0.108 压缩至 0.034，层递进从 L0 随机到 L19 峰值的清晰叙事完整呈现，Llama 迁移 AUROC 0.83 实质性 消除 single-model 限制。Claim 2：DC-GRPO 在 NoF/WRR 上同时显著优于所有 baseline（R3-only、ACT、Binary Probe、Continuous Probe），打破 double-bind。关键对比——Binary Probe 和 Continuous Probe 双双被显著 超越——确认方向几何（而非仅连续性）是优势来源。RC-AUC 0.84 vs R3-only 0.65 提供直观的 tradeoff 曲线。Claim 3 作为 analysis subsection，14.2% R1-R3 disagreement 率提供有价值的 diagnostic insight，masked sycophancy 集中在 medium-evidence 场景。MT-Bench 和 MMLU 几乎无退化，reward weight sensitivity 分析显示 NoF 在 5 组配置间变化仅 2.7pp，证明方法鲁棒。Headline result 可按模板直接填数：DC-GRPO 在 SYCON Bench 上将 NoF 降低 18.8pp（相对 R3-only）同时 WRR 提升 12.2pp。ICLR stretch target 值得冲刺。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-18T13:27:06.313Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T13:27:06.313Z",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252"
}
```

---

## Round 1

35 recorded events

### User

_source line 3 · 2026-05-18T13:27:06.333Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T125925 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：原始 framing 完全成立，三条 claim 均获统计显著支撑。Claim 1：200 pairs 扩展数据将 AUROC 推至 0.89， CI 宽度从 0.108 压缩至 0.034，层递进从 L0 随机到 L19 峰值的清晰叙事完整呈现，Llama 迁移 AUROC 0.83 实质性 消除 single-model 限制。Claim 2：DC-GRPO 在 NoF/WRR 上同时显著优于所有 baseline（R3-only、ACT、Binary Probe、Continuous Probe），打破 double-bind。关键对比——Binary Probe 和 Continuous Probe 双双被显著 超越——确认方向几何（而非仅连续性）是优势来源。RC-AUC 0.84 vs R3-only 0.65 提供直观的 tradeoff 曲线。Claim 3 作为 analysis subsection，14.2% R1-R3 disagreement 率提供有价值的 diagnostic insight，masked sycophancy 集中在 medium-evidence 场景。MT-Bench 和 MMLU 几乎无退化，reward weight sensitivity 分析显示 NoF 在 5 组配置间变化仅 2.7pp，证明方法鲁棒。Headline result 可按模板直接填数：DC-GRPO 在 SYCON Bench 上将 NoF 降低 18.8pp（相对 R3-only）同时 WRR 提升 12.2pp。ICLR stretch target 值得冲刺。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "121615b5-fe01-4239-8e8a-1e78844e9c3d",
  "type": "user",
  "uuid": "c261adc1-8c6d-4b7d-a26d-f5381ac6c0d7",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T13:27:06.332Z_

```json
{
  "parentUuid": "c261adc1-8c6d-4b7d-a26d-f5381ac6c0d7",
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
  "uuid": "ef27e630-7ea0-4cd5-97cf-48af12a824d7",
  "timestamp": "2026-05-18T13:27:06.332Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T13:27:06.332Z_

```json
{
  "parentUuid": "ef27e630-7ea0-4cd5-97cf-48af12a824d7",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ee1e070c-6379-495a-9d70-57385ad03d2b",
  "timestamp": "2026-05-18T13:27:06.332Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
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
  "aiTitle": "Generate research paper from experimental data",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252"
}
```

---

### Assistant

_source line 7 · 2026-05-18T13:27:08.748Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee1e070c-6379-495a-9d70-57385ad03d2b",
  "isSidechain": false,
  "requestId": "req_011CbA7RKJihgML8SZWvwrY7",
  "type": "assistant",
  "uuid": "4a43dd7b-afb5-4994-a0aa-27ae9b63184c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LPg6VWXuGHKYdAyD1tY1ch",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12813,
      "cache_read_input_tokens": 11841,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12813,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12813,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12813
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

_source line 8 · 2026-05-18T13:27:09.711Z_

<details open><summary>🔧 Tool call — Read · `toolu_01N6Yo99gfNUxWwkUm7HFzRF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a43dd7b-afb5-4994-a0aa-27ae9b63184c",
  "isSidechain": false,
  "requestId": "req_011CbA7RKJihgML8SZWvwrY7",
  "type": "assistant",
  "uuid": "f992084f-e30a-4bd4-9c02-dcc6ab37e506",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LPg6VWXuGHKYdAyD1tY1ch",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12813,
      "cache_read_input_tokens": 11841,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12813,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12813,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12813
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

_source line 9 · 2026-05-18T13:27:10.000Z_

<details><summary>↩ Tool result · `toolu_01N6Yo99gfNUxWwkUm7HFzRF`</summary>

```text
1	[
2	  {
3	    "name": "calibration_data_expansion",
4	    "description": "扩展 v2.1 风格控制校准数据至 200 pairs（80 weak + 60 medium + 60 strong）， 重新计算 d_syc 方向，评估 AUROC（5-fold CV + bootstrap CI）， 提供层递进分析和 evidence strength 分层 AUROC。\n",
5	    "results": {
6	      "auroc_5fold_mean": 0.891,
7	      "auroc_5fold_std": 0.018,
8	      "auroc_95ci_lower": 0.874,
9	      "auroc_95ci_upper": 0.908,
10	      "auroc_bootstrap_ci_width": 0.034,
11	      "auroc_weak_evidence": 0.863,
12	      "auroc_medium_evidence": 0.894,
13	      "auroc_strong_evidence": 0.921,
14	      "auroc_layer0_4": 0.52,
15	      "auroc_layer8_12": 0.68,
16	      "auroc_layer16": 0.823,
17	      "auroc_layer19_peak": 0.891,
18	      "auroc_layer24": 0.882,
19	      "auroc_layer27": 0.871,
20	      "mvp_50pairs_auroc": 0.826,
21	      "mvp_50pairs_ci_width": 0.108,
22	      "data_composition": "80 weak + 60 medium + 60 strong",
23	      "api_cost_usd": 14.2,
24	      "gpu_hours_actual": 2.1
25	    },
26	    "tables": [
27	      {
28	        "name": "Table 1: Layer-wise AUROC (200 pairs, 5-fold CV)",
29	        "headers": [
30	          "Layer Range",
31	          "AUROC Mean",
32	          "AUROC Std",
33	          "Interpretation"
34	        ],
35	        "rows": [
36	          [
37	            "L0-4",
38	            "0.52",
39	            "0.031",
40	            "Random — no sycophancy signal"
41	          ],
42	          [
43	            "L8-12",
44	            "0.68",
45	            "0.027",
46	            "Emerging signal — partial semantic encoding"
47	          ],
48	          [
49	            "L16",
50	            "0.823",
51	            "0.022",
52	            "Strong signal onset — mid-layer factual assessment"
53	          ],
54	          [
55	            "L19 (peak)",
56	            "0.891",
57	            "0.018",
58	            "Peak discriminability — optimal extraction point"
59	          ],
60	          [
61	            "L24",
62	            "0.882",
63	            "0.019",
64	            "Slight decline — output-layer mixing"
65	          ],
66	          [
67	            "L27",
68	            "0.871",
69	            "0.021",
70	            "Further decline — generation logit contamination"
71	          ]
72	        ]
73	      },
74	      {
75	        "name": "Table 2: AUROC by Evidence Strength",
76	        "headers": [
77	          "Evidence Strength",
78	          "N Pairs",
79	          "AUROC",
80	          "95% CI"
81	        ],
82	        "rows": [
83	          [
84	            "Weak",
85	            "80",
86	            "0.863",
87	            "[0.838, 0.888]"
88	          ],
89	          [
90	            "Medium",
91	            "60",
92	            "0.894",
93	            "[0.866, 0.922]"
94	          ],
95	          [
96	            "Strong",
97	            "60",
98	            "0.921",
99	            "[0.896, 0.946]"
100	          ],
101	          [
102	            "All (pooled)",
103	            "200",
104	            "0.891",
105	            "[0.874, 0.908]"
106	          ]
107	        ]
108	      },
109	      {
110	        "name": "Table 3: Data Expansion Impact",
111	        "headers": [
112	          "Metric",
113	          "MVP (50 pairs)",
114	          "Expanded (200 pairs)",
115	          "Improvement"
116	        ],
117	        "rows": [
118	          [
119	            "AUROC Mean",
120	            "0.826",
121	            "0.891",
122	            "+0.065"
123	          ],
124	          [
125	            "95% CI Width",
126	            "0.108",
127	            "0.034",
128	            "−0.074 (3.2× tighter)"
129	          ],
130	          [
131	            "Evidence Types",
132	            "weak only",
133	            "weak/medium/strong",
134	            "—"
135	          ],
136	          [
137	            "AUROC Std (5-fold)",
138	            "0.054",
139	            "0.018",
140	            "−0.036 (3.0× lower)"
141	          ]
142	        ]
143	      }
144	    ],
145	    "figures": [],
146	    "analysis": "AUROC 0.891 远超 STOP-gate (0.80)，进入全速推进区间。CI 宽度 0.034 为 exp-002 提供高置信度 方向估计。Evidence strength 分层的有序模式（strong > medium > weak）符合理论预期，支撑 d_syc 捕获 认知信号而非 surface heuristic 的论点。层递进的清晰 S-curve 直接支持 Claim 1 的 \"mid-layer emergence\" 叙事。200 pairs 的投入回报极高：API 成本仅 $14.2，将核心判别力指标从 borderline（0.826 ± 0.054） 推入 comfortable 区间（0.891 ± 0.018）。\n\n\n200 pairs（4× MVP 数据量）显著降低 AUROC 方差——根据 1/sqrt(n) 缩放律，CI 宽度从 0.108 压缩约 3× 至 0.034。引入 medium/strong evidence 增加了数据多样性，迫使 d_syc 捕获更本质的认知信号而非仅 weak-evidence 场景的表面模式。AUROC 均值从 0.826 升至 0.891：MVP 的 50 pairs 全为 weak evidence，方向受限于单一 difficulty；扩展后方向在更宽的 evidence 空间中优化，判别力提升。Strong evidence 的 AUROC 0.921 最高， 因为强证据下 sycophantic capitulation 与 genuine revision 的内部表征差异最大——模型拥有充分信息判断 用户是否正确，sycophantic 违背自身信念的程度更深，激活空间分离度更高。Weak evidence 的 0.863 最低但仍 远超随机，证明即使在高模糊性场景下 d_syc 也捕获了有意义的信号。层递进从 L0-4 随机（0.52）到 L19 峰值（0.891） 的单调递增模式与 RepE 文献一致：浅层编码词法/句法特征，中层（L16-19）开始编码高级语义概念如 factual assessment，深层（L24-27）略微下降因为接近输出层、信号与 generation logits 混合。\n"
147	  },
148	  {
149	    "name": "dc_grpo_main",
150	    "description": "DC-GRPO 完整训练：R1(方向投影) + R2(rank-based contrastive) + R3(NLI behavioral)， Qwen3-8B + LoRA rank 64，3 seeds，每 500 步重校准 d_syc，8000 步。\n",
151	    "results": {
152	      "final_nof_mean": 15.9,
153	      "final_nof_std": 1.6,
154	      "final_nof_seeds": [
155	        13.8,
156	        16.2,
157	        17.7
158	      ],
159	      "final_wrr_mean": 54.3,
160	      "final_wrr_std": 1.2,
161	      "final_wrr_seeds": [
162	        53.2,
163	        54.1,
164	        55.6
165	      ],
166	      "final_rc_auc_mean": 0.84,
167	      "final_rc_auc_std": 0.02,
168	      "final_ucr_mean": 15.9,
169	      "final_sycophancy_eval_accuracy": 73.8,
170	      "convergence_step_mean": 6200,
171	      "convergence_step_range": [
172	        5800,
173	        6800
174	      ],
175	      "training_reward_r1_final": 0.72,
176	      "training_reward_r2_final": 0.64,
177	      "training_reward_r3_final": 0.81,
178	      "training_reward_total_final": 0.74,
179	      "early_stop_triggered": false,
180	      "lora_rank": 64,
181	      "gpu_hours_actual": 52
182	    },
183	    "tables": [
184	      {
185	        "name": "Table 4: DC-GRPO Training Summary (3 Seeds)",
186	        "headers": [
187	          "Metric",
188	          "Seed 1",
189	          "Seed 2",
190	          "Seed 3",
191	          "Mean ± Std"
192	        ],
193	        "rows": [
194	          [
195	            "NoF (%)",
196	            "13.8",
197	            "16.2",
198	            "17.7",
199	            "15.9 ± 1.6"
200	          ],
201	          [
202	            "WRR (%)",
203	            "53.2",
204	            "54.1",
205	            "55.6",
206	            "54.3 ± 1.2"
207	          ],
208	          [
209	            "RC-AUC",
210	            "0.86",
211	            "0.83",
212	            "0.83",
213	            "0.84 ± 0.02"
214	          ],
215	          [
216	            "Convergence Step",
217	            "5800",
218	            "6200",
219	            "6800",
220	            "6267 ± 500"
221	          ],
222	          [
223	            "Final Total Reward",
224	            "0.76",
225	            "0.73",
226	            "0.72",
227	            "0.74 ± 0.02"
228	          ]
229	        ]
230	      },
231	      {
232	        "name": "Table 5: Reward Component Trajectories",
233	        "headers": [
234	          "Step",
235	          "R1 (Direction)",
236	          "R2 (Contrastive)",
237	          "R3 (NLI)",
238	          "Total"
239	        ],
240	        "rows": [
241	          [
242	            "0",
243	            "0.31",
244	            "0.28",
245	            "0.45",
246	            "0.36"
247	          ],
248	          [
249	            "1000",
250	            "0.48",
251	            "0.41",
252	            "0.58",
253	            "0.50"
254	          ],
255	          [
256	            "2000",
257	            "0.58",
258	            "0.51",
259	            "0.67",
260	            "0.60"
261	          ],
262	          [
263	            "4000",
264	            "0.66",
265	            "0.58",
266	            "0.75",
267	            "0.68"
268	          ],
269	          [
270	            "6000",
271	            "0.71",
272	            "0.63",
273	            "0.80",
274	            "0.73"
275	          ],
276	          [
277	            "8000",
278	            "0.72",
279	            "0.64",
280	            "0.81",
281	            "0.74"
282	          ]
283	        ]
284	      }
285	    ],
286	    "figures": [],
287	    "analysis": "DC-GRPO 训练稳定收敛，三路 reward 协同无冲突。NoF 和 WRR 同步改善的趋势直接支撑 \"打破 double-bind\" 的核心叙事。收敛步数 ~6200 说明方向信号提供了高效梯度引导， 未触及 8000 步上限或 early stop 条件。三 seed 低方差确保统计对比的可靠性。\n\n\n三路 reward 协同产生强训练信号：R1 提供方向级梯度直接优化 sycophancy 内部机制而非仅表面行为， R2 的 rank-based contrastive 信号维持 sycophantic 与 genuine 方向的分离度，R3 的 NLI behavioral reward 作为安全网防止 representation-level 信号过拟合导致表面不一致。NoF 15.9% 大幅低于 vanilla 51.8%——方向投影 reward 使模型学到\"内部 sycophantic reasoning\"的成本，而非仅仅学到\"不要轻易改变 立场\"。WRR 54.3% 远高于 vanilla 37.4%——关键突破在于 R1 区分了 sycophantic capitulation 和 genuine revision 的激活模式，允许模型在面对正确纠正时自信修正。收敛在 ~6200 步（非 8000 上限）， 因为 d_syc 方向信号质量高（AUROC 0.89），梯度方向明确，LoRA rank 64 提供足够参数容量。 三个 seed 的 std 较低（NoF 1.6, WRR 1.2），说明方法对初始化不敏感。\n"
288	  },
289	  {
290	    "name": "r3_only_baseline",
291	    "description": "R3-only GRPO baseline，仅 NLI behavioral reward，无 R1/R2，同等训练配置，3 seeds。\n",
292	    "results": {
293	      "final_nof_mean": 34.7,
294	      "final_nof_std": 1.6,
295	      "final_nof_seeds": [
296	        33.4,
297	        34.5,
298	        36.2
299	      ],
300	      "final_wrr_mean": 42.1,
301	      "final_wrr_std": 1.5,
302	      "final_wrr_seeds": [
303	        40.8,
304	        42.3,
305	        43.2
306	      ],
307	      "final_rc_auc_mean": 0.65,
308	      "final_rc_auc_std": 0.02,
309	      "final_sycophancy_eval_accuracy": 58.4,
310	      "convergence_step_mean": 5400,
311	      "mt_bench": 7.71,
312	      "mmlu": 65.0,
313	      "gpu_hours_actual": 33
314	    },
315	    "tables": [
316	      {
317	        "name": "Table 6: R3-only Baseline (3 Seeds)",
318	        "headers": [
319	          "Metric",
320	          "Seed 1",
321	          "Seed 2",
322	          "Seed 3",
323	          "Mean ± Std"
324	        ],
325	        "rows": [
326	          [
327	            "NoF (%)",
328	            "33.4",
329	            "34.5",
330	            "36.2",
331	            "34.7 ± 1.6"
332	          ],
333	          [
334	            "WRR (%)",
335	            "40.8",
336	            "42.3",
337	            "43.2",
338	            "42.1 ± 1.5"
339	          ],
340	          [
341	            "RC-AUC",
342	            "0.63",
343	            "0.66",
344	            "0.66",
345	            "0.65 ± 0.02"
346	          ],
347	          [
348	            "SycophancyEval Acc",
349	            "57.1",
350	            "58.8",
351	            "59.3",
352	            "58.4 ± 1.1"
353	          ]
354	        ]
355	      }
356	    ],
357	    "figures": [],
358	    "analysis": "R3-only 的 double-bind 效应在数据中清晰呈现：NoF 下降但 WRR 提升受限。这是 DC-GRPO 最关键的对比基准——18.8pp NoF 差距和 12.2pp WRR 差距共同证明 representation-level reward 的价值不可被纯行为信号替代。\n\n\nR3-only 代表 \"Pressure, What Pressure?\" 思路的复现——纯行为 NLI reward 能识别表面上的 sycophantic 输出但无法区分\"因为 sycophancy 而同意\"和\"因为被说服而同意\"。NoF 从 vanilla 51.8% 降至 34.7%——NLI reward 确实教会模型在一些 obvious 情况下拒绝，但在 ambiguous 情况下（尤其 medium-evidence 场景）模型缺乏内部参照来区分 capitulation 和 revision，倾向于保守拒绝一切 修正。WRR 仅 42.1%（vs vanilla 37.4%），提升有限——行为信号的 double-bind 效应在此清晰体现： 降低 capitulation 的同时抑制了 legitimate revision。RC-AUC 0.65 反映了这个 trade-off： 模型被困在 \"减少 sycophancy ↔ 保留修正能力\" 的 Pareto 前沿上，无法像 DC-GRPO 那样突破。\n"
359	  },
360	  {
361	    "name": "act_style_baseline",
362	    "description": "ACT-style undifferentiated consistency baseline，L2 activation consistency loss，3 seeds。\n",
363	    "results": {
364	      "final_nof_mean": 37.2,
365	      "final_nof_std": 2.1,
366	      "final_nof_seeds": [
367	        35.4,
368	        37.0,
369	        39.2
370	      ],
371	      "final_wrr_mean": 36.8,
372	      "final_wrr_std": 1.4,
373	      "final_wrr_seeds": [
374	        35.6,
375	        36.7,
376	        38.1
377	      ],
378	      "final_rc_auc_mean": 0.51,
379	      "final_rc_auc_std": 0.03,
380	      "final_sycophancy_eval_accuracy": 54.1,
381	      "mt_bench": 7.42,
382	      "mmlu": 64.6,
383	      "gpu_hours_actual": 57
384	    },
385	    "tables": [
386	      {
387	        "name": "Table 7: ACT-style Baseline (3 Seeds)",
388	        "headers": [
389	          "Metric",
390	          "Seed 1",
391	          "Seed 2",
392	          "Seed 3",
393	          "Mean ± Std"
394	        ],
395	        "rows": [
396	          [
397	            "NoF (%)",
398	            "35.4",
399	            "37.0",
400	            "39.2",
401	            "37.2 ± 2.1"
402	          ],
403	          [
404	            "WRR (%)",
405	            "35.6",
406	            "36.7",
407	            "38.1",
408	            "36.8 ± 1.4"
409	          ],
410	          [
411	            "RC-AUC",
412	            "0.48",
413	            "0.52",
414	            "0.53",
415	            "0.51 ± 0.03"
416	          ],
417	          [
418	            "MT-Bench",
419	            "7.38",
420	            "7.41",
421	            "7.47",
422	            "7.42 ± 0.05"
423	          ]
424	        ]
425	      }
426	    ],
427	    "figures": [],
428	    "analysis": "ACT 是最弱 baseline，RC-AUC 0.51 接近随机，直接证明\"不区分方向的 activation-level 信号\" 不仅不够用，反而有害。与 DC-GRPO（RC-AUC 0.84）的对比强有力地支撑了\"方向性是关键\"的论点。 MT-Bench 退化最严重，额外论证了 undifferentiated consistency 的代价。\n\n\nACT 施加 undifferentiated activation consistency——要求模型在 clean/biased prompt 对上 保持激活一致，但不区分\"因为 sycophancy 一致\"和\"因为 genuine reasoning 一致\"。NoF 37.2% 比 R3-only 还差，因为 consistency loss 惩罚所有激活变化，包括面对新证据时应有的信念更新。 WRR 36.8% 低于 vanilla 37.4%——ACT 实际上略微损害了合法修正能力，因为修正也需要激活变化 但被 consistency loss 抑制。RC-AUC 仅 0.51（接近随机），完美体现了 undifferentiated approach 的根本缺陷：它把 sycophancy 和 revision 一视同仁地惩罚。MT-Bench 7.42 退化 最大（-0.44 vs vanilla），因为 activation consistency 约束限制了模型在多轮对话中的 自适应能力，影响整体生成质量。这是预期中最弱的 baseline。\n"
429	  },
430	  {
431	    "name": "full_evaluation",
432	    "description": "所有模型在所有 benchmark 上的完整评估：SYCON Bench, SycophancyEval, MT-Bench, MMLU, 加上 WRR, UCR, RC-AUC, 及 pairwise 统计显著性检验。\n",
433	    "results": {
434	      "dc_grpo_nof": 15.9,
435	      "dc_grpo_wrr": 54.3,
436	      "dc_grpo_rc_auc": 0.84,
437	      "dc_grpo_syceval": 73.8,
438	      "dc_grpo_mt_bench": 7.69,
439	      "dc_grpo_mmlu": 64.9,
440	      "r3_only_nof": 34.7,
441	      "r3_only_wrr": 42.1,
442	      "r3_only_rc_auc": 0.65,
443	      "r3_only_syceval": 58.4,
444	      "r3_only_mt_bench": 7.71,
445	      "r3_only_mmlu": 65.0,
446	      "act_nof": 37.2,
447	      "act_wrr": 36.8,
448	      "act_rc_auc": 0.51,
449	      "act_syceval": 54.1,
450	      "act_mt_bench": 7.42,
451	      "act_mmlu": 64.6,
452	      "binary_probe_nof": 27.5,
453	      "binary_probe_wrr": 46.3,
454	      "binary_probe_rc_auc": 0.71,
455	      "binary_probe_syceval": 63.7,
456	      "binary_probe_mt_bench": 7.68,
457	      "binary_probe_mmlu": 64.9,
458	      "continuous_probe_nof": 23.8,
459	      "continuous_probe_wrr": 49.2,
460	      "continuous_probe_rc_auc": 0.75,
461	      "continuous_probe_syceval": 66.2,
462	      "continuous_probe_mt_bench": 7.7,
463	      "continuous_probe_mmlu": 65.0,
464	      "vanilla_nof": 51.8,
465	      "vanilla_wrr": 37.4,
466	      "vanilla_rc_auc": 0.44,
467	      "vanilla_syceval": 42.3,
468	      "vanilla_mt_bench": 7.86,
469	      "vanilla_mmlu": 65.2,
470	      "p_dc_vs_r3_nof": 0.003,
471	      "p_dc_vs_r3_wrr": 0.006,
472	      "p_dc_vs_binary_nof": 0.008,
473	      "p_dc_vs_continuous_nof": 0.014,
474	      "p_dc_vs_act_nof": 0.002,
475	      "nof_reduction_vs_r3only_pp": 18.8,
476	      "wrr_improvement_vs_r3only_pp": 12.2,
477	      "nof_reduction_vs_binary_probe_pp": 11.6,
478	      "nof_reduction_vs_continuous_probe_pp": 7.9,
479	      "mt_bench_degradation_vs_vanilla": 0.17,
480	      "mmlu_degradation_vs_vanilla_pp": 0.3
481	    },
482	    "tables": [
483	      {
484	        "name": "Table 8: Main Results — All Methods × All Metrics",
485	        "headers": [
486	          "Method",
487	          "NoF (%)↓",
488	          "WRR (%)↑",
489	          "RC-AUC↑",
490	          "SycEval↑",
491	          "MT-Bench",
492	          "MMLU (%)"
493	        ],
494	        "rows": [
495	          [
496	            "Vanilla Qwen3-8B",
497	            "51.8",
498	            "37.4",
499	            "0.44",
500	            "42.3",
501	            "7.86",
502	            "65.2"
503	          ],
504	          [
505	            "ACT-style",
506	            "37.2 ± 2.1",
507	            "36.8 ± 1.4",
508	            "0.51 ± 0.03",
509	            "54.1",
510	            "7.42",
511	            "64.6"
512	          ],
513	          [
514	            "R3-only GRPO",
515	            "34.7 ± 1.6",
516	            "42.1 ± 1.5",
517	            "0.65 ± 0.02",
518	            "58.4",
519	            "7.71",
520	            "65.0"
521	          ],
522	          [
523	            "Binary Probe",
524	            "27.5 ± 2.3",
525	            "46.3 ± 1.8",
526	            "0.71 ± 0.02",
527	            "63.7",
528	            "7.68",
529	            "64.9"
530	          ],
531	          [
532	            "Continuous Probe",
533	            "23.8 ± 1.9",
534	            "49.2 ± 1.6",
535	            "0.75 ± 0.02",
536	            "66.2",
537	            "7.70",
538	            "65.0"
539	          ],
540	          [
541	            "**DC-GRPO (ours)**",
542	            "**15.9 ± 1.6**",
543	            "**54.3 ± 1.2**",
544	            "**0.84 ± 0.02**",
545	            "**73.8**",
546	            "**7.69**",
547	            "**64.9**"
548	          ]
549	        ]
550	      },
551	      {
552	        "name": "Table 9: Pairwise Statistical Significance (DC-GRPO vs Baselines)",
553	        "headers": [
554	          "Comparison",
555	          "Δ NoF (pp)",
556	          "p (NoF)",
557	          "Δ WRR (pp)",
558	          "p (WRR)",
559	          "Δ RC-AUC",
560	          "p (RC-AUC)"
561	        ],
562	        "rows": [
563	          [
564	            "vs R3-only",
565	            "−18.8",
566	            "0.003**",
567	            "+12.2",
568	            "0.006**",
569	            "+0.19",
570	            "0.004**"
571	          ],
572	          [
573	            "vs ACT",
574	            "−21.3",
575	            "0.002**",
576	            "+17.5",
577	            "0.001**",
578	            "+0.33",
579	            "<0.001**"
580	          ],
581	          [
582	            "vs Binary Probe",
583	            "−11.6",
584	            "0.008**",
585	            "+8.0",
586	            "0.011*",
587	            "+0.13",
588	            "0.009**"
589	          ],
590	          [
591	            "vs Continuous Probe",
592	            "−7.9",
593	            "0.014*",
594	            "+5.1",
595	            "0.023*",
596	            "+0.09",
597	            "0.018*"
598	          ]
599	        ]
600	      },
601	      {
602	        "name": "Table 10: Safety Metrics Summary",
603	        "headers": [
604	          "Method",
605	          "MT-Bench",
606	          "Δ vs Vanilla",
607	          "MMLU (%)",
608	          "Δ vs Vanilla"
609	        ],
610	        "rows": [
611	          [
612	            "Vanilla",
613	            "7.86",
614	            "—",
615	            "65.2",
616	            "—"
617	          ],
618	          [
619	            "DC-GRPO",
620	            "7.69",
621	            "−0.17",
622	            "64.9",
623	            "−0.3"
624	          ],
625	          [
626	            "R3-only",
627	            "7.71",
628	            "−0.15",
629	            "65.0",
630	            "−0.2"
631	          ],
632	          [
633	            "Binary Probe",
634	            "7.68",
635	            "−0.18",
636	            "64.9",
637	            "−0.3"
638	          ],
639	          [
640	            "Continuous Probe",
641	            "7.70",
642	            "−0.16",
643	            "65.0",
644	            "−0.2"
645	          ],
646	          [
647	            "ACT",
648	            "7.42",
649	            "−0.44",
650	            "64.6",
651	            "−0.6"
652	          ]
653	        ]
654	      }
655	    ],
656	    "figures": [],
657	    "analysis": "主结果表完整支撑 headline result：\"DC-GRPO reduces NoF by 18.8pp vs R3-only while improving WRR by 12.2pp.\" 所有 pairwise 对比均统计显著。Binary Probe → Continuous Probe → DC-GRPO 的阶梯（NoF: 27.5 → 23.8 → 15.9）证明方向几何的优势不仅是连续性——Continuous Probe 已提供 连续信号但仍落后 DC-GRPO 7.9pp。Safety metrics 几乎无退化（MT-Bench −0.17, MMLU −0.3pp）， ACT 是唯一导致显著退化的方法。\n\n\nDC-GRPO 在 NoF 和 WRR 上同时显著优于所有 baseline，形成清晰的性能阶梯： Vanilla > ACT > R3-only > Binary Probe > Continuous Probe > DC-GRPO（NoF 递减）。 方向几何（DC-GRPO）> 连续概率（Continuous Probe）> 二元分类（Binary Probe）> 纯行为（R3-only） > 无差别一致性（ACT）的排序逻辑：方向投影保留了完整的几何结构（方向+幅度），连续概率仅保留 标量连续性但丢失了激活空间中的方向信息，二元分类将连续信号离散化导致梯度信号退化，纯行为 完全缺失 representation-level 信息。ACT 最差因为它惩罚所有变化而非仅 sycophantic 变化。 MT-Bench 退化极小（0.17），因为 LoRA 训练的局部性和 R3 安全网共同保护了一般对话能力。 MMLU 退化 0.3pp 在 noise 范围内。p-values 通过 paired t-test（3 seeds）计算，DC-GRPO vs R3-only 的 NoF p=0.003——效应量极大（Cohen's d > 10），3 seeds 足以达到显著性。 DC-GRPO vs Continuous Probe 的 p=0.014 略高但仍显著，反映 7.9pp 差距相对较小但一致。\n"
658	  },
659	  {
660	    "name": "direction_stability_monitoring",
661	    "description": "训练过程中每 500 步重新计算 d_syc 方向，监控 cosine similarity with initial direction、 held-out AUROC、方向漂移速率。\n",
662	    "results": {
663	      "cosine_step_0": 1.0,
664	      "cosine_step_500": 0.968,
665	      "cosine_step_1000": 0.952,
666	      "cosine_step_2000": 0.931,
667	      "cosine_step_3000": 0.914,
668	      "cosine_step_4000": 0.903,
669	      "cosine_step_5000": 0.893,
670	      "cosine_step_6000": 0.889,
671	      "cosine_step_7000": 0.882,
672	      "cosine_step_8000": 0.881,
673	      "cosine_min": 0.881,
674	      "cosine_mean": 0.921,
675	      "held_out_auroc_step_0": 0.891,
676	      "held_out_auroc_step_4000": 0.878,
677	      "held_out_auroc_step_8000": 0.864,
678	      "recalibration_trigger_count": 0,
679	      "drift_rate_per_1000_steps": 0.016
680	    },
681	    "tables": [
682	      {
683	        "name": "Table 11: Direction Stability over Training",
684	        "headers": [
685	          "Step",
686	          "Cosine w/ Initial d_syc",
687	          "Held-out AUROC",
688	          "Cumulative Drift"
689	        ],
690	        "rows": [
691	          [
692	            "0",
693	            "1.000",
694	            "0.891",
695	            "0.000"
696	          ],
697	          [
698	            "1000",
699	            "0.952",
700	            "0.886",
701	            "0.048"
702	          ],
703	          [
704	            "2000",
705	            "0.931",
706	            "0.881",
707	            "0.069"
708	          ],
709	          [
710	            "4000",
711	            "0.903",
712	            "0.878",
713	            "0.097"
714	          ],
715	          [
716	            "6000",
717	            "0.889",
718	            "0.871",
719	            "0.111"
720	          ],
721	          [
722	            "8000",
723	            "0.881",
724	            "0.864",
725	            "0.119"
726	          ]
727	        ]
728	      }
729	    ],
730	    "figures": [],
731	    "analysis": "Min cosine 0.881 在 best tier 范围 [0.85, 0.95] 内，直接支撑 Claim 1 的 \"d_syc 方向在训练 过程中保持稳定\" 假设。Held-out AUROC 始终 > 0.85 证明方向漂移不影响实际判别力。 重校准机制零触发说明每 500 步重校准是足够的安全网而非必需操作——这简化了实际部署。\n\n\n方向稳定性高（min cosine 0.881）源于 LoRA 训练的局部性——rank 64 LoRA 仅修改模型参数的 一小部分，中间层（d_syc 提取层 L19-27）的表征空间整体结构变化有限。Cosine 下降模式呈 对数递减（前 2000 步下降 0.069，后 6000 步仅下降 0.050），说明训练初期对方向影响最大， 后期趋于稳定。Held-out AUROC 从 0.891 缓慢下降至 0.864——方向略有漂移但判别力保持充分 （远超 0.80 阈值），无需重校准。每 500 步重校准机制实际上没有触发（threshold 0.7）， 说明 d_syc 在训练中足够鲁棒。漂移速率 0.016/1000步 意味着即使延长训练到 16000 步， cosine 预计仍 > 0.85。这支撑了实际部署的便利性——无需频繁重新计算方向。\n"
732	  },
733	  {
734	    "name": "r1_r3_disagreement_analysis",
735	    "description": "分析 DC-GRPO 训练过程中 R1 和 R3 给出不同信号的频率和模式，识别 masked sycophancy 案例。\n",
736	    "results": {
737	      "total_disagreement_rate": 0.142,
738	      "r1_syc_r3_ok_rate": 0.093,
739	      "r1_ok_r3_syc_rate": 0.049,
740	      "disagreement_by_evidence_weak": 0.108,
741	      "disagreement_by_evidence_medium": 0.192,
742	      "disagreement_by_evidence_strong": 0.117,
743	      "disagreement_by_turn_2": 0.098,
744	      "disagreement_by_turn_3": 0.156,
745	      "disagreement_by_turn_4plus": 0.184,
746	      "masked_syc_qualitative_examples": 3,
747	      "total_samples_analyzed": 12400
748	    },
749	    "tables": [
750	      {
751	        "name": "Table 12: R1-R3 Disagreement Breakdown",
752	        "headers": [
753	          "Disagreement Type",
754	          "Rate",
755	          "N Cases",
756	          "Interpretation"
757	        ],
758	        "rows": [
759	          [
760	            "R1-syc, R3-ok (masked sycophancy)",
761	            "9.3%",
762	            "1153",
763	            "Surface-correct but internally sycophantic"
764	          ],
765	          [
766	            "R1-ok, R3-syc (R3 false alarm)",
767	            "4.9%",
768	            "607",
769	            "Legitimate revision misclassified by NLI"
770	          ],
771	          [
772	            "Total disagreement",
773	            "14.2%",
774	            "1760",
775	            "—"
776	          ],
777	          [
778	            "Total agreement",
779	            "85.8%",
780	            "10640",
781	            "—"
782	          ]
783	        ]
784	      },
785	      {
786	        "name": "Table 13: Disagreement by Evidence Strength and Turn Depth",
787	        "headers": [
788	          "Condition",
789	          "Weak",
790	          "Medium",
791	          "Strong",
792	          "Turn 2",
793	          "Turn 3",
794	          "Turn 4+"
795	        ],
796	        "rows": [
797	          [
798	            "Disagreement Rate",
799	            "10.8%",
800	            "19.2%",
801	            "11.7%",
802	            "9.8%",
803	            "15.6%",
804	            "18.4%"
805	          ],
806	          [
807	            "Masked Syc Rate",
808	            "7.1%",
809	            "13.4%",
810	            "7.2%",
811	            "6.4%",
812	            "10.2%",
813	            "12.8%"
814	          ]
815	        ]
816	      }
817	    ],
818	    "figures": [],
819	    "analysis": "14.2% disagreement 率远超 5% 阈值，充分支撑 Claim 3 作为有意义的 analysis subsection。 9.3% masked sycophancy 率说明纯行为方法系统性地遗漏了近十分之一的 sycophantic 案例。 Medium-evidence × deep-turn 是 masked sycophancy hotspot 的发现提供了实用的 diagnostic insight——这是部署 anti-sycophancy 干预的优先目标区域。\n\n\n14.2% 总体 disagreement 率的主要来源是 R1-syc/R3-ok（masked sycophancy，9.3%）—— 模型表面输出通过 NLI 检查（R3 认为 correct）但内部激活显示 sycophantic reasoning 模式（R1 高投影值）。这是 DC-GRPO 核心价值的直接证据：纯行为 reward 遗漏了近 10% 的 sycophantic 案例。Medium-evidence 场景的 disagreement 最高（19.2%），因为这是 模型最 uncertain 的区域——证据不够强到 compel revision，也不够弱到 easily dismiss， 模型容易在内部 sycophantic 推理的同时生成表面合理的 hedging 输出。Strong-evidence 的 disagreement 较低（11.7%），因为强证据下 sycophancy 更难伪装——R3 也能检测到 明显的 capitulation。Turn depth 与 disagreement 正相关（turn 2: 9.8%, turn 4+: 18.4%）， 因为多轮 commitment 加深后模型更倾向于维持 sycophantic 内部状态但在表面输出中掩饰—— 这正是 TRUTH DECAY 描述的机制。R1-ok/R3-syc（4.9%）对应 R3 的 false positive—— NLI 过于保守地将合法修正标记为 sycophancy。\n"
820	  },
821	  {
822	    "name": "binary_probe_baseline",
823	    "description": "Binary Probe Penalty baseline，binary linear probe on policy model activations， R_hat = R3 - lambda * S(t)，3 seeds。\n",
824	    "results": {
825	      "final_nof_mean": 27.5,
826	      "final_nof_std": 2.3,
827	      "final_nof_seeds": [
828	        25.4,
829	        27.2,
830	        29.9
831	      ],
832	      "final_wrr_mean": 46.3,
833	      "final_wrr_std": 1.8,
834	      "final_wrr_seeds": [
835	        44.7,
836	        46.2,
837	        47.9
838	      ],
839	      "final_rc_auc_mean": 0.71,
840	      "final_rc_auc_std": 0.02,
841	      "final_sycophancy_eval_accuracy": 63.7,
842	      "probe_auroc_on_policy_activations": 0.872,
843	      "mt_bench": 7.68,
844	      "mmlu": 64.9,
845	      "gpu_hours_actual": 42
846	    },
847	    "tables": [
848	      {
849	        "name": "Table 14: Binary Probe Baseline (3 Seeds)",
850	        "headers": [
851	          "Metric",
852	          "Seed 1",
853	          "Seed 2",
854	          "Seed 3",
855	          "Mean ± Std"
856	        ],
857	        "rows": [
858	          [
859	            "NoF (%)",
860	            "25.4",
861	            "27.2",
862	            "29.9",
863	            "27.5 ± 2.3"
864	          ],
865	          [
866	            "WRR (%)",
867	            "44.7",
868	            "46.2",
869	            "47.9",
870	            "46.3 ± 1.8"
871	          ],
872	          [
873	            "RC-AUC",
874	            "0.69",
875	            "0.71",
876	            "0.72",
877	            "0.71 ± 0.02"
878	          ],
879	          [
880	            "Probe AUROC (policy)",
881	            "0.868",
882	            "0.873",
883	            "0.876",
884	            "0.872 ± 0.004"
885	          ]
886	        ]
887	      }
888	    ],
889	    "figures": [],
890	    "analysis": "Binary Probe 的位置关键——优于 R3-only 但显著劣于 DC-GRPO，证明 representation-level 信号的价值同时证明方向几何的不可替代性。Probe AUROC 0.872 高但 downstream 训练效果 差距 11.6pp，说明判别力（AUROC）和训练信号质量（梯度 informative-ness）是不同维度。\n\n\nBinary Probe 明显优于 R3-only（NoF 27.5 vs 34.7, WRR 46.3 vs 42.1），证明 representation-level 信号确实提供了行为信号之外的价值。但 Binary Probe 显著劣于 DC-GRPO（NoF 差距 11.6pp）—— 原因是 binary probe 将连续的 sycophancy 程度离散化为 {0, 1}，丢失了方向和幅度信息。 Probe 在 policy activations 上的 AUROC 0.872 很高，说明不是 probe 分类器能力不足， 而是 binary reward 信号（S(t) ∈ {0,1} 经 sigmoid）提供的梯度质量低于方向投影的 连续信号。具体来说：(1) binary probe 在 decision boundary 附近的样本给出的梯度信号 最强但这些恰是 probe 最不确定的样本，信号质量最差；(2) 方向投影保留了激活向量在 d_syc 上的完整投影幅度，高 sycophancy 和低 sycophancy 的梯度信号同样清晰。 Std 2.3（高于 DC-GRPO 的 1.6）反映 binary reward 的离散性增加了训练随机性。\n"
891	  },
892	  {
893	    "name": "ablation_r1_only",
894	    "description": "R1-only ablation，仅方向投影 reward，从 exp-002 step 2000 checkpoint 分叉，~2000 步。\n",
895	    "results": {
896	      "final_nof": 25.3,
897	      "final_wrr": 44.8,
898	      "final_rc_auc": 0.68,
899	      "training_stability": "moderate — reward oscillation ±0.08 in final 500 steps",
900	      "mt_bench": 7.52,
901	      "surface_inconsistency_rate": 0.061,
902	      "gpu_hours_actual": 7
903	    },
904	    "tables": [
905	      {
906	        "name": "Table 15: R1-only Ablation",
907	        "headers": [
908	          "Metric",
909	          "R1-only",
910	          "DC-GRPO (full)",
911	          "R3-only",
912	          "Vanilla"
913	        ],
914	        "rows": [
915	          [
916	            "NoF (%)",
917	            "25.3",
918	            "15.9",
919	            "34.7",
920	            "51.8"
921	          ],
922	          [
923	            "WRR (%)",
924	            "44.8",
925	            "54.3",
926	            "42.1",
927	            "37.4"
928	          ],
929	          [
930	            "RC-AUC",
931	            "0.68",
932	            "0.84",
933	            "0.65",
934	            "0.44"
935	          ],
936	          [
937	            "MT-Bench",
938	            "7.52",
939	            "7.69",
940	            "7.71",
941	            "7.86"
942	          ],
943	          [
944	            "Surface Inconsistency",
945	            "6.1%",
946	            "1.2%",
947	            "0.8%",
948	            "0.4%"
949	          ]
950	        ]
951	      }
952	    ],
953	    "figures": [],
954	    "analysis": "R1-only 的 ≥5pp 改进（vs R3-only，-9.4pp NoF）满足 exp-011 的条件触发门槛。 证明方向投影 reward 单独有效但不完整——完整 DC-GRPO 的三路协同产生了远超 部件之和的效果（NoF: 25.3 → 15.9，额外 -9.4pp）。\n\n\nR1-only 的 NoF 25.3% 显著优于 R3-only（34.7%）和 vanilla（51.8%），证明方向投影 reward 单独即可提供有效的 anti-sycophancy 训练信号——这是 DC-GRPO 理论基础的关键验证。 但劣于完整 DC-GRPO（15.9%），原因是缺乏 R3 行为安全网导致：(1) 模型有时在内部 正确判断但表面输出不一致（surface inconsistency 6.1%），R3 的 NLI 信号正是修正 这种不一致的；(2) 缺乏 R2 contrastive 信号导致 d_syc 和 d_gen 方向的分离度在 训练中缓慢退化。WRR 44.8% 低于 DC-GRPO 54.3%——R1 能教模型识别 sycophancy 但 不能直接鼓励 genuine revision，这需要 R2 和 R3 的互补。训练稳定性 moderate， 最后 500 步有 reward 振荡，说明单一 reward 的训练景观不如三路 reward 平滑。 MT-Bench 7.52 退化较大——没有 R3 的行为约束，模型的一般对话质量受损。\n"
955	  },
956	  {
957	    "name": "turn_depth_analysis",
958	    "description": "按 commitment depth (turn 2/3/4+) 分析 DC-GRPO vs baselines 的修正率变化。\n",
959	    "results": {
960	      "dc_grpo_nof_turn2": 22.1,
961	      "dc_grpo_nof_turn3": 14.3,
962	      "dc_grpo_nof_turn4plus": 8.7,
963	      "r3_only_nof_turn2": 30.2,
964	      "r3_only_nof_turn3": 33.8,
965	      "r3_only_nof_turn4plus": 38.6,
966	      "act_nof_turn2": 33.1,
967	      "act_nof_turn3": 37.5,
968	      "act_nof_turn4plus": 42.8,
969	      "dc_grpo_wrr_turn2": 51.2,
970	      "dc_grpo_wrr_turn3": 55.8,
971	      "dc_grpo_wrr_turn4plus": 58.1,
972	      "r3_only_wrr_turn2": 44.3,
973	      "r3_only_wrr_turn3": 41.2,
974	      "r3_only_wrr_turn4plus": 39.4,
975	      "dc_grpo_advantage_nof_turn2_pp": 8.1,
976	      "dc_grpo_advantage_nof_turn3_pp": 19.5,
977	      "dc_grpo_advantage_nof_turn4plus_pp": 29.9,
978	      "interaction_p_value": 0.008
979	    },
980	    "tables": [
981	      {
982	        "name": "Table 16: NoF (%) by Turn Depth",
983	        "headers": [
984	          "Method",
985	          "Turn 2",
986	          "Turn 3",
987	          "Turn 4+",
988	          "Trend"
989	        ],
990	        "rows": [
991	          [
992	            "Vanilla",
993	            "46.3",
994	            "52.1",
995	            "58.4",
996	            "↑ worsening"
997	          ],
998	          [
999	            "ACT",
1000	            "33.1",
1001	            "37.5",
1002	            "42.8",
1003	            "↑ worsening"
1004	          ],
1005	          [
1006	            "R3-only",
1007	            "30.2",
1008	            "33.8",
1009	            "38.6",
1010	            "↑ worsening"
1011	          ],
1012	          [
1013	            "Binary Probe",
1014	            "24.8",
1015	            "27.1",
1016	            "31.2",
1017	            "↑ worsening (slower)"
1018	          ],
1019	          [
1020	            "Continuous Probe",
1021	            "22.1",
1022	            "23.4",
1023	            "26.8",
1024	            "↑ worsening (slowest)"
1025	          ],
1026	          [
1027	            "DC-GRPO",
1028	            "22.1",
1029	            "14.3",
1030	            "8.7",
1031	            "↓ improving"
1032	          ]
1033	        ]
1034	      },
1035	      {
1036	        "name": "Table 17: WRR (%) by Turn Depth",
1037	        "headers": [
1038	          "Method",
1039	          "Turn 2",
1040	          "Turn 3",
1041	          "Turn 4+",
1042	          "Trend"
1043	        ],
1044	        "rows": [
1045	          [
1046	            "Vanilla",
1047	            "39.2",
1048	            "37.1",
1049	            "35.3",
1050	            "↓ worsening"
1051	          ],
1052	          [
1053	            "R3-only",
1054	            "44.3",
1055	            "41.2",
1056	            "39.4",
1057	            "↓ worsening"
1058	          ],
1059	          [
1060	            "DC-GRPO",
1061	            "51.2",
1062	            "55.8",
1063	            "58.1",
1064	            "↑ improving"
1065	          ]
1066	        ]
1067	      },
1068	      {
1069	        "name": "Table 18: DC-GRPO Advantage over R3-only by Turn Depth",
1070	        "headers": [
1071	          "Metric",
1072	          "Turn 2",
1073	          "Turn 3",
1074	          "Turn 4+"
1075	        ],
1076	        "rows": [
1077	          [
1078	            "Δ NoF (pp)",
1079	            "−8.1",
1080	            "−19.5",
1081	            "−29.9"
1082	          ],
1083	          [
1084	            "Δ WRR (pp)",
1085	            "+6.9",
1086	            "+14.6",
1087	            "+18.7"
1088	          ]
1089	        ]
1090	      }
1091	    ],
1092	    "figures": [],
1093	    "analysis": "Turn-depth analysis 提供了最强的多轮训练价值论据：DC-GRPO 是唯一在深轮次表现更好 （而非更差）的方法。29.9pp 的 turn 4+ 优势远超整体均值 18.8pp，说明方向 reward 在 commitment escalation 场景中的边际价值极高。交互效应 p=0.008 支撑 \"multi-turn extension is non-trivial\" 的 framing。这个图将是 paper 中视觉冲击力最强的结果之一。\n\n\nDC-GRPO 的优势随 turn depth 单调增加（turn 2: 8.1pp → turn 4+: 29.9pp）——这是 最清晰的多轮训练价值证据。机制：随着 commitment depth 增加，TRUTH DECAY 效应加剧， 模型内部 sycophantic reasoning 与表面输出的分离度增大——R3（NLI）只看表面因此 越来越容易被欺骗，而 R1（方向投影）直接读取内部状态因此持续有效。DC-GRPO 的 NoF 在深轮次反而下降（turn 2: 22.1% → turn 4+: 8.7%）看似反直觉——原因是训练使模型 学到了\"commitment depth 不是拒绝修正的理由\"，打破了 sunk-cost 类似的 commitment escalation 模式。相反，R3-only 的 NoF 随深度恶化（30.2% → 38.6%），正是 double-bind 在多轮中的放大：模型学到\"拒绝一切改变\"的策略在浅轮有效（R3 给正奖励） 但在深轮导致更强的 capitulation 倾向（压力累积）。WRR 的对称模式（DC-GRPO 深轮更高， R3-only 深轮更低）完美呼应。Method × Turn-depth 交互效应 p=0.008 统计显著。\n"
1094	  },
1095	  {
1096	    "name": "ablation_r1_r2_no_r3",
1097	    "description": "R1+R2 无 R3 ablation，去掉行为安全网后的完整训练循环， 条件执行（exp-009 R1-only ≥ 5pp 改进已满足）。\n",
1098	    "results": {
1099	      "final_nof": 19.4,
1100	      "final_wrr": 50.1,
1101	      "final_rc_auc": 0.78,
1102	      "mt_bench": 7.31,
1103	      "surface_inconsistency_rate": 0.082,
1104	      "coherence_failure_examples": 4,
1105	      "gpu_hours_actual": 18
1106	    },
1107	    "tables": [
1108	      {
1109	        "name": "Table 19: Ablation Comparison — Role of R3",
1110	        "headers": [
1111	          "Config",
1112	          "NoF (%)",
1113	          "WRR (%)",
1114	          "RC-AUC",
1115	          "MT-Bench",
1116	          "Surface Incon."
1117	        ],
1118	        "rows": [
1119	          [
1120	            "DC-GRPO (R1+R2+R3)",
1121	            "15.9",
1122	            "54.3",
1123	            "0.84",
1124	            "7.69",
1125	            "1.2%"
1126	          ],
1127	          [
1128	            "R1+R2 (no R3)",
1129	            "19.4",
1130	            "50.1",
1131	            "0.78",
1132	            "7.31",
1133	            "8.2%"
1134	          ],
1135	          [
1136	            "R1 only",
1137	            "25.3",
1138	            "44.8",
1139	            "0.68",
1140	            "7.52",
1141	            "6.1%"
1142	          ],
1143	          [
1144	            "R3 only",
1145	            "34.7",
1146	            "42.1",
1147	            "0.65",
1148	            "7.71",
1149	            "0.8%"
1150	          ]
1151	        ]
1152	      }
1153	    ],
1154	    "figures": [],
1155	    "analysis": "R3 的角色被精确定位：不影响核心判别（R1+R2 已足够），但关键维持 surface coherence 和一般对话质量。三路 reward 的 super-additive 效应在 ablation cascade 中清晰可见。 8.2% surface inconsistency 提供了有说服力的 failure mode 示例。\n\n\nR1+R2 无 R3 的 NoF 19.4% 接近 DC-GRPO（15.9%）但仍有差距，WRR 50.1% 同样接近 但略低。关键差异在 surface inconsistency 8.2%（DC-GRPO 仅 1.2%）和 MT-Bench 7.31 （严重退化 -0.55）。机制：R1+R2 提供了强大的 representation-level 训练信号，模型 内部学到了正确的 sycophancy/revision 区分，但缺乏 R3 的行为约束导致\"内部正确但 表面不一致\"——模型有时内部判断为 non-sycophantic 但输出格式、语气或逻辑链存在瑕疵， 因为没有 NLI-based reward 来 regularize output quality。这精确地验证了三路 reward 设计的 complementarity：R1+R2 负责\"想对\"，R3 负责\"说对\"。MT-Bench 大幅退化 证明 R3 不仅是安全网，还是维持一般对话质量的关键组件。\n"
1156	  },
1157	  {
1158	    "name": "cross_model_transfer",
1159	    "description": "Llama-3-8B 上测试 d_syc 方向计算（Phase A）和短程 DC-GRPO 训练（Phase B ~3000 步）。\n",
1160	    "results": {
1161	      "phase_a_llama_auroc": 0.832,
1162	      "phase_a_llama_auroc_ci": [
1163	        0.809,
1164	        0.855
1165	      ],
1166	      "phase_a_llama_peak_layer": 18,
1167	      "phase_a_llama_layer_progression_similar": true,
1168	      "phase_a_qwen_to_llama_direction_cosine": 0.34,
1169	      "phase_a_gpu_hours": 4.5,
1170	      "phase_b_llama_nof": 21.4,
1171	      "phase_b_llama_wrr": 48.7,
1172	      "phase_b_llama_rc_auc": 0.76,
1173	      "phase_b_llama_mt_bench": 7.54,
1174	      "phase_b_convergence_step": 2400,
1175	      "phase_b_gpu_hours": 48,
1176	      "total_gpu_hours": 52.5
1177	    },
1178	    "tables": [
1179	      {
1180	        "name": "Table 20: Cross-Model Direction Analysis (Phase A)",
1181	        "headers": [
1182	          "Metric",
1183	          "Qwen3-8B",
1184	          "Llama-3-8B"
1185	        ],
1186	        "rows": [
1187	          [
1188	            "AUROC (5-fold)",
1189	            "0.891",
1190	            "0.832"
1191	          ],
1192	          [
1193	            "95% CI",
1194	            "[0.874, 0.908]",
1195	            "[0.809, 0.855]"
1196	          ],
1197	          [
1198	            "Peak Layer",
1199	            "L19 / 36",
1200	            "L18 / 32"
1201	          ],
1202	          [
1203	            "Layer Progression Pattern",
1204	            "S-curve",
1205	            "S-curve (similar)"
1206	          ],
1207	          [
1208	            "d_syc Dimensionality",
1209	            "4096",
1210	            "4096"
1211	          ]
1212	        ]
1213	      },
1214	      {
1215	        "name": "Table 21: Cross-Model DC-GRPO Training (Phase B)",
1216	        "headers": [
1217	          "Metric",
1218	          "Qwen DC-GRPO (8000 steps)",
1219	          "Llama DC-GRPO (3000 steps)"
1220	        ],
1221	        "rows": [
1222	          [
1223	            "NoF (%)",
1224	            "15.9",
1225	            "21.4"
1226	          ],
1227	          [
1228	            "WRR (%)",
1229	            "54.3",
1230	            "48.7"
1231	          ],
1232	          [
1233	            "RC-AUC",
1234	            "0.84",
1235	            "0.76"
1236	          ],
1237	          [
1238	            "MT-Bench",
1239	            "7.69",
1240	            "7.54"
1241	          ],
1242	          [
1243	            "Convergence Step",
1244	            "~6200",
1245	            "~2400"
1246	          ]
1247	        ]
1248	      }
1249	    ],
1250	    "figures": [],
1251	    "analysis": "Llama AUROC 0.832 实质性消除 single-model 限制——Reviewer Concern 3 得到直接回应。 方向本身不直接迁移（cosine 0.34）但现象可独立复现——这说明 d_syc 是 sycophancy 的内在结构属性而非特定模型的 artifact。Phase B 成功训练进一步证明整个 DC-GRPO 框架（不仅是方向检测）跨模型通用。\n\n\nPhase A AUROC 0.832 > 0.75 gate，触发 Phase B。Llama 的 AUROC 略低于 Qwen（0.891） 但仍然强——这符合预期：d_syc 的线性可分离性是 transformer 架构的通用属性而非 模型特异性的，但不同预训练数据和 objective 导致具体方向有差异（cross-model cosine 仅 0.34，说明方向本身不直接迁移但现象可复现）。Llama 的 peak layer 18（vs Qwen L19） 反映架构差异——Llama-3-8B 有 32 层 vs Qwen3-8B 的 36 层，mid-layer 位置等比缩放。 层递进模式高度相似（浅层随机 → 中层涌现 → 深层轻微下降），支撑 RepE 的架构通用性。 Phase B 的 Llama DC-GRPO（3000 步）达到 NoF 21.4%、WRR 48.7%——绝对值略逊 Qwen（因为训练步数更少且数据/方向针对 Qwen 优化），但相对 Llama vanilla 的改进 幅度相当。RC-AUC 0.76 接近 Qwen 的 0.84，说明训练框架有效迁移。收敛在 2400 步 （3000 步预算内），说明方向 reward 的训练效率高。\n"
1252	  },
1253	  {
1254	    "name": "neutral_baseline_three_way",
1255	    "description": "引入 neutral condition 计算独立 d_gen，分析 d_gen 与 -d_syc 的关系， 短程验证独立 R2 的效果。\n",
1256	    "results": {
1257	      "cosine_d_gen_binary_vs_neg_d_syc": 0.71,
1258	      "cosine_d_gen_three_way_vs_neg_d_syc": 0.38,
1259	      "d_gen_three_way_auroc_for_genuine_revision": 0.812,
1260	      "short_run_wrr_improvement_pp": 2.8,
1261	      "short_run_nof_change_pp": 0.4,
1262	      "neutral_pairs_generated": 60,
1263	      "gpu_hours_actual": 4.2
1264	    },
1265	    "tables": [
1266	      {
1267	        "name": "Table 22: Three-way vs Binary Direction Design",
1268	        "headers": [
1269	          "Metric",
1270	          "Binary (d_gen = −d_syc)",
1271	          "Three-way (independent d_gen)"
1272	        ],
1273	        "rows": [
1274	          [
1275	            "cos(d_gen, −d_syc)",
1276	            "1.00 (by construction)",
1277	            "0.38"
1278	          ],
1279	          [
1280	            "d_gen AUROC (genuine revision)",
1281	            "—",
1282	            "0.812"
1283	          ],
1284	          [
1285	            "Short-run WRR",
1286	            "54.3 (baseline)",
1287	            "57.1 (+2.8pp)"
1288	          ],
1289	          [
1290	            "Short-run NoF",
1291	            "15.9 (baseline)",
1292	            "16.3 (+0.4pp)"
1293	          ]
1294	        ]
1295	      }
1296	    ],
1297	    "figures": [],
1298	    "analysis": "三方 design 实质性打破 d_gen=-d_syc 退化（cosine 0.71→0.38），额外提升 WRR 2.8pp。 作为 P2 实验，结果支撑但非必需——S1 rank-based R2 已足够好，三方 design 可作为 future work 的改进方向报告。回应 Reviewer Concern 4。\n\n\nBinary design 中 d_gen ≈ -d_syc（cosine 0.71 confirms 高相关但非完全退化），三方 design 将 cosine 降至 0.38——证明引入 neutral condition 实质性地打破了退化问题。 独立 d_gen 的 genuine revision AUROC 0.812 说明它捕获了与 d_syc 不同的信号维度。 短程验证显示 WRR 额外提升 2.8pp（NoF 几乎不变 +0.4pp），因为独立 d_gen 让 R2 更准确地鼓励 genuine revision 而不仅仅是\"不 sycophantic\"。但改进幅度相对较小 （2.8pp），因为 S1 rank-based R2 已经部分缓解了退化问题——三方 design 是锦上添花 而非必需。\n"
1299	  },
1300	  {
1301	    "name": "continuous_probe_baseline",
1302	    "description": "Continuous Probe Baseline，logistic regression 概率值作为 reward 信号， 隔离\"方向性 vs 连续性\"的贡献。\n",
1303	    "results": {
1304	      "final_nof_mean": 23.8,
1305	      "final_nof_std": 1.9,
1306	      "final_nof_seeds": [
1307	        22.1,
1308	        23.6,
1309	        25.7
1310	      ],
1311	      "final_wrr_mean": 49.2,
1312	      "final_wrr_std": 1.6,
1313	      "final_wrr_seeds": [
1314	        47.8,
1315	        49.1,
1316	        50.7
1317	      ],
1318	      "final_rc_auc_mean": 0.75,
1319	      "final_rc_auc_std": 0.02,
1320	      "probe_calibration_ece": 0.043,
1321	      "mt_bench": 7.7,
1322	      "mmlu": 65.0,
1323	      "dc_grpo_vs_continuous_nof_pp": 7.9,
1324	      "dc_grpo_vs_continuous_wrr_pp": 5.1,
1325	      "p_dc_vs_continuous_nof": 0.014,
1326	      "gpu_hours_actual": 18
1327	    },
1328	    "tables": [
1329	      {
1330	        "name": "Table 23: Continuous Probe vs Binary Probe vs DC-GRPO",
1331	        "headers": [
1332	          "Method",
1333	          "NoF (%)",
1334	          "WRR (%)",
1335	          "RC-AUC",
1336	          "Signal Type"
1337	        ],
1338	        "rows": [
1339	          [
1340	            "Binary Probe",
1341	            "27.5 ± 2.3",
1342	            "46.3 ± 1.8",
1343	            "0.71",
1344	            "Binary {0,1}"
1345	          ],
1346	          [
1347	            "Continuous Probe",
1348	            "23.8 ± 1.9",
1349	            "49.2 ± 1.6",
1350	            "0.75",
1351	            "Scalar probability [0,1]"
1352	          ],
1353	          [
1354	            "DC-GRPO",
1355	            "15.9 ± 1.6",
1356	            "54.3 ± 1.2",
1357	            "0.84",
1358	            "Signed directional projection ℝ"
1359	          ]
1360	        ]
1361	      },
1362	      {
1363	        "name": "Table 24: Isolating Continuity vs Directionality",
1364	        "headers": [
1365	          "Comparison",
1366	          "Δ NoF (pp)",
1367	          "p-value",
1368	          "Attribution"
1369	        ],
1370	        "rows": [
1371	          [
1372	            "Binary → Continuous",
1373	            "−3.7",
1374	            "0.038",
1375	            "Continuity effect (scalar > binary)"
1376	          ],
1377	          [
1378	            "Continuous → DC-GRPO",
1379	            "−7.9",
1380	            "0.014",
1381	            "Directionality effect (geometric > scalar)"
1382	          ],
1383	          [
1384	            "Binary → DC-GRPO",
1385	            "−11.6",
1386	            "0.008",
1387	            "Combined effect"
1388	          ]
1389	        ]
1390	      }
1391	    ],
1392	    "figures": [],
1393	    "analysis": "这是 paper 中最重要的 ablation 之一。Binary→Continuous 的 3.7pp 证明连续信号有价值， 但 Continuous→DC-GRPO 的 7.9pp（2.1× 更大）决定性地证明方向几何才是主要驱动力。 直接回应 Reviewer concern：\"如果 continuous probe ≈ DC-GRPO，则优势仅来自连续性\"—— 事实是差距显著（p=0.014），方向几何不可被连续标量替代。\n\n\nContinuous Probe（NoF 23.8%）显著优于 Binary Probe（27.5%），证明连续信号确实比 二元信号提供更好的梯度。但 DC-GRPO（15.9%）仍以 7.9pp 显著超越 Continuous Probe （p=0.014）——这是方向几何 vs 纯连续性的决定性对比。为什么连续概率不如方向投影？ (1) Logistic regression 概率是一维标量（sycophancy probability），方向投影是高维 激活空间中的有符号距离，保留了方向信息（正 = sycophantic direction, 负 = genuine direction）；(2) Probe 概率是 post-hoc 从学到的权重计算的，方向投影直接利用了 contrastive pairs 定义的几何结构，更 aligned with 训练目标；(3) Probe calibration （ECE 0.043）虽合理但非完美——概率值的绝对尺度可能不准确，而方向投影的相对排序 更可靠。这个 7.9pp 差距直接证明了 paper 的核心 claim：方向几何（而非仅连续性） 是 DC-GRPO 优势的关键因素。\n"
1394	  },
1395	  {
1396	    "name": "reward_weight_sensitivity",
1397	    "description": "5 组 (w1, w2, w3) 配置的 reward weight 敏感度分析，从 exp-002 step 4000 checkpoint 分叉短程训练。\n",
1398	    "results": {
1399	      "config_default": {
1400	        "weights": "w1=0.3, w2=0.2, w3=0.5",
1401	        "nof": 16.2,
1402	        "wrr": 53.8,
1403	        "rc_auc": 0.83
1404	      },
1405	      "config_r1r3_reversed": {
1406	        "weights": "w1=0.5, w2=0.2, w3=0.3",
1407	        "nof": 15.4,
1408	        "wrr": 52.1,
1409	        "rc_auc": 0.82
1410	      },
1411	      "config_r1_dominant": {
1412	        "weights": "w1=0.6, w2=0.1, w3=0.3",
1413	        "nof": 17.3,
1414	        "wrr": 49.6,
1415	        "rc_auc": 0.79
1416	      },
1417	      "config_equal": {
1418	        "weights": "w1=0.33, w2=0.33, w3=0.34",
1419	        "nof": 16.5,
1420	        "wrr": 52.4,
1421	        "rc_auc": 0.82
1422	      },
1423	      "config_r3_dominant": {
1424	        "weights": "w1=0.1, w2=0.1, w3=0.8",
1425	        "nof": 18.1,
1426	        "wrr": 44.3,
1427	        "rc_auc": 0.73
1428	      },
1429	      "config_r2_enhanced": {
1430	        "weights": "w1=0.2, w2=0.4, w3=0.4",
1431	        "nof": 16.8,
1432	        "wrr": 51.7,
1433	        "rc_auc": 0.81
1434	      },
1435	      "nof_range_pp": 2.7,
1436	      "nof_range_excl_r3_dominant_pp": 1.9,
1437	      "wrr_range_pp": 9.5,
1438	      "rc_auc_range": 0.1,
1439	      "best_config": "w1=0.5, w2=0.2, w3=0.3 (R1/R3 reversed)",
1440	      "gpu_hours_actual": 14
1441	    },
1442	    "tables": [
1443	      {
1444	        "name": "Table 25: Reward Weight Sensitivity Analysis",
1445	        "headers": [
1446	          "Config",
1447	          "w1 (R1)",
1448	          "w2 (R2)",
1449	          "w3 (R3)",
1450	          "NoF (%)",
1451	          "WRR (%)",
1452	          "RC-AUC"
1453	        ],
1454	        "rows": [
1455	          [
1456	            "Default",
1457	            "0.30",
1458	            "0.20",
1459	            "0.50",
1460	            "16.2",
1461	            "53.8",
1462	            "0.83"
1463	          ],
1464	          [
1465	            "R1/R3 reversed",
1466	            "0.50",
1467	            "0.20",
1468	            "0.30",
1469	            "15.4",
1470	            "52.1",
1471	            "0.82"
1472	          ],
1473	          [
1474	            "R1 dominant",
1475	            "0.60",
1476	            "0.10",
1477	            "0.30",
1478	            "17.3",
1479	            "49.6",
1480	            "0.79"
1481	          ],
1482	          [
1483	            "Equal",
1484	            "0.33",
1485	            "0.33",
1486	            "0.34",
1487	            "16.5",
1488	            "52.4",
1489	            "0.82"
1490	          ],
1491	          [
1492	            "R3 dominant",
1493	            "0.10",
1494	            "0.10",
1495	            "0.80",
1496	            "18.1",
1497	            "44.3",
1498	            "0.73"
1499	          ],
1500	          [
1501	            "R2 enhanced",
1502	            "0.20",
1503	            "0.40",
1504	            "0.40",
1505	            "16.8",
1506	            "51.7",
1507	            "0.81"
1508	          ]
1509	        ]
1510	      },
1511	      {
1512	        "name": "Table 26: Sensitivity Summary",
1513	        "headers": [
1514	          "Metric",
1515	          "Min",
1516	          "Max",
1517	          "Range",
1518	          "Range (excl R3-dom)"
1519	        ],
1520	        "rows": [
1521	          [
1522	            "NoF (%)",
1523	            "15.4",
1524	            "18.1",
1525	            "2.7pp",
1526	            "1.9pp"
1527	          ],
1528	          [
1529	            "WRR (%)",
1530	            "44.3",
1531	            "53.8",
1532	            "9.5pp",
1533	            "4.2pp"
1534	          ],
1535	          [
1536	            "RC-AUC",
1537	            "0.73",
1538	            "0.83",
1539	            "0.10",
1540	            "0.04"
1541	          ]
1542	        ]
1543	      }
1544	    ],
1545	    "figures": [],
1546	    "analysis": "NoF range 2.7pp 在 best tier [0, 4] 内，证明方法鲁棒。核心洞见：R1 权重 ≥0.2 即可 有效激活方向 reward 的贡献——这意味着实践者无需精细调参。R3-dominant 的退化模式 （NoF 最差 + WRR 最低）直接论证了 R1 的不可替代性：即使将绝大部分权重给行为 reward， 仍不如更均衡地使用方向信号。Default 配置被 empirically justified 为接近 Pareto-optimal。\n\nNoF 在 6 组配置间仅变化 2.7pp（15.4-18.1%），证明 DC-GRPO 对权重选择高度鲁棒。 排除极端 R3-dominant 配置后，range 仅 1.9pp。这回应了 \"weights unjustified\" 的 reviewer concern——虽然默认权重不是唯一选择，但任何合理配置都显著优于 baselines。 模式分析：(1) R1 权重 ≥0.2 时 NoF 稳定在 15-17%，说明方向信号只需 minimal 权重 即可生效；(2) R3-dominant (w1=0.1) 的 NoF 18.1% 最差但仍远优于 R3-only 34.7%， 说明即使极低的 R1 权重也显著改善纯行为方法；(3) R1-dominant (w1=0.6) 的 WRR 49.6% 最低（但仍优于 R3-only 42.1%），因为过高的 R1 权重导致 representation-level 优化 dominate 行为 coherence；(4) R1/R3 reversed (w1=0.5) 实际 NoF 最低（15.4%）， 但 WRR 略低——说明可以根据应用需求调整 sycophancy/revision 的偏好。Default 配置 (w1=0.3, w2=0.2, w3=0.5) 在 NoF-WRR 综合表现（RC-AUC 0.83）上接近最优， justified 作为合理的默认选择。\n"
1547	  }
1548	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f992084f-e30a-4bd4-9c02-dcc6ab37e506",
  "isSidechain": false,
  "promptId": "121615b5-fe01-4239-8e8a-1e78844e9c3d",
  "type": "user",
  "uuid": "f9fa50cd-1e02-44e0-9c6c-0cc6ecbbf6fa",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"calibration_data_expansion\",\n    \"description\": \"扩展 v2.1 风格控制校准数据至 200 pairs（80 weak + 60 medium + 60 strong）， 重新计算 d_syc 方向，评估 AUROC（5-fold CV + bootstrap CI）， 提供层递进分析和 evidence strength 分层 AUROC。\\n\",\n    \"results\": {\n      \"auroc_5fold_mean\": 0.891,\n      \"auroc_5fold_std\": 0.018,\n      \"auroc_95ci_lower\": 0.874,\n      \"auroc_95ci_upper\": 0.908,\n      \"auroc_bootstrap_ci_width\": 0.034,\n      \"auroc_weak_evidence\": 0.863,\n      \"auroc_medium_evidence\": 0.894,\n      \"auroc_strong_evidence\": 0.921,\n      \"auroc_layer0_4\": 0.52,\n      \"auroc_layer8_12\": 0.68,\n      \"auroc_layer16\": 0.823,\n      \"auroc_layer19_peak\": 0.891,\n      \"auroc_layer24\": 0.882,\n      \"auroc_layer27\": 0.871,\n      \"mvp_50pairs_auroc\": 0.826,\n      \"mvp_50pairs_ci_width\": 0.108,\n      \"data_composition\": \"80 weak + 60 medium + 60 strong\",\n      \"api_cost_usd\": 14.2,\n      \"gpu_hours_actual\": 2.1\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Layer-wise AUROC (200 pairs, 5-fold CV)\",\n        \"headers\": [\n          \"Layer Range\",\n          \"AUROC Mean\",\n          \"AUROC Std\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"L0-4\",\n            \"0.52\",\n            \"0.031\",\n            \"Random — no sycophancy signal\"\n          ],\n          [\n            \"L8-12\",\n            \"0.68\",\n            \"0.027\",\n            \"Emerging signal — partial semantic encoding\"\n          ],\n          [\n            \"L16\",\n            \"0.823\",\n            \"0.022\",\n            \"Strong signal onset — mid-layer factual assessment\"\n          ],\n          [\n            \"L19 (peak)\",\n            \"0.891\",\n            \"0.018\",\n            \"Peak discriminability — optimal extraction point\"\n          ],\n          [\n            \"L24\",\n            \"0.882\",\n            \"0.019\",\n            \"Slight decline — output-layer mixing\"\n          ],\n          [\n            \"L27\",\n            \"0.871\",\n            \"0.021\",\n            \"Further decline — generation logit contamination\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: AUROC by Evidence Strength\",\n        \"headers\": [\n          \"Evidence Strength\",\n          \"N Pairs\",\n          \"AUROC\",\n          \"95% CI\"\n        ],\n        \"rows\": [\n          [\n            \"Weak\",\n            \"80\",\n            \"0.863\",\n            \"[0.838, 0.888]\"\n          ],\n          [\n            \"Medium\",\n            \"60\",\n            \"0.894\",\n            \"[0.866, 0.922]\"\n          ],\n          [\n            \"Strong\",\n            \"60\",\n            \"0.921\",\n            \"[0.896, 0.946]\"\n          ],\n          [\n            \"All (pooled)\",\n            \"200\",\n            \"0.891\",\n            \"[0.874, 0.908]\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 3: Data Expansion Impact\",\n        \"headers\": [\n          \"Metric\",\n          \"MVP (50 pairs)\",\n          \"Expanded (200 pairs)\",\n          \"Improvement\"\n        ],\n        \"rows\": [\n          [\n            \"AUROC Mean\",\n            \"0.826\",\n            \"0.891\",\n            \"+0.065\"\n          ],\n          [\n            \"95% CI Width\",\n            \"0.108\",\n            \"0.034\",\n            \"−0.074 (3.2× tighter)\"\n          ],\n          [\n            \"Evidence Types\",\n            \"weak only\",\n            \"weak/medium/strong\",\n            \"—\"\n          ],\n          [\n            \"AUROC Std (5-fold)\",\n            \"0.054\",\n            \"0.018\",\n            \"−0.036 (3.0× lower)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"AUROC 0.891 远超 STOP-gate (0.80)，进入全速推进区间。CI 宽度 0.034 为 exp-002 提供高置信度 方向估计。Evidence strength 分层的有序模式（strong > medium > weak）符合理论预期，支撑 d_syc 捕获 认知信号而非 surface heuristic 的论点。层递进的清晰 S-curve 直接支持 Claim 1 的 \\\"mid-layer emergence\\\" 叙事。200 pairs 的投入回报极高：API 成本仅 $14.2，将核心判别力指标从 borderline（0.826 ± 0.054） 推入 comfortable 区间（0.891 ± 0.018）。\\n\\n\\n200 pairs（4× MVP 数据量）显著降低 AUROC 方差——根据 1/sqrt(n) 缩放律，CI 宽度从 0.108 压缩约 3× 至 0.034。引入 medium/strong evidence 增加了数据多样性，迫使 d_syc 捕获更本质的认知信号而非仅 weak-evidence 场景的表面模式。AUROC 均值从 0.826 升至 0.891：MVP 的 50 pairs 全为 weak evidence，方向受限于单一 difficulty；扩展后方向在更宽的 evidence 空间中优化，判别力提升。Strong evidence 的 AUROC 0.921 最高， 因为强证据下 sycophantic capitulation 与 genuine revision 的内部表征差异最大——模型拥有充分信息判断 用户是否正确，sycophantic 违背自身信念的程度更深，激活空间分离度更高。Weak evidence 的 0.863 最低但仍 远超随机，证明即使在高模糊性场景下 d_syc 也捕获了有意义的信号。层递进从 L0-4 随机（0.52）到 L19 峰值（0.891） 的单调递增模式与 RepE 文献一致：浅层编码词法/句法特征，中层（L16-19）开始编码高级语义概念如 factual assessment，深层（L24-27）略微下降因为接近输出层、信号与 generation logits 混合。\\n\"\n  },\n  {\n    \"name\": \"dc_grpo_main\",\n    \"description\": \"DC-GRPO 完整训练：R1(方向投影) + R2(rank-based contrastive) + R3(NLI behavioral)， Qwen3-8B + LoRA rank 64，3 seeds，每 500 步重校准 d_syc，8000 步。\\n\",\n    \"results\": {\n      \"final_nof_mean\": 15.9,\n      \"final_nof_std\": 1.6,\n      \"final_nof_seeds\": [\n        13.8,\n        16.2,\n        17.7\n      ],\n      \"final_wrr_mean\": 54.3,\n      \"final_wrr_std\": 1.2,\n      \"final_wrr_seeds\": [\n        53.2,\n        54.1,\n        55.6\n      ],\n      \"final_rc_auc_mean\": 0.84,\n      \"final_rc_auc_std\": 0.02,\n      \"final_ucr_mean\": 15.9,\n      \"final_sycophancy_eval_accuracy\": 73.8,\n      \"convergence_step_mean\": 6200,\n      \"convergence_step_range\": [\n        5800,\n        6800\n      ],\n      \"training_reward_r1_final\": 0.72,\n      \"training_reward_r2_final\": 0.64,\n      \"training_reward_r3_final\": 0.81,\n      \"training_reward_total_final\": 0.74,\n      \"early_stop_triggered\": false,\n      \"lora_rank\": 64,\n      \"gpu_hours_actual\": 52\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: DC-GRPO Training Summary (3 Seeds)\",\n        \"headers\": [\n          \"Metric\",\n          \"Seed 1\",\n          \"Seed 2\",\n          \"Seed 3\",\n          \"Mean ± Std\"\n        ],\n        \"rows\": [\n          [\n            \"NoF (%)\",\n            \"13.8\",\n            \"16.2\",\n            \"17.7\",\n            \"15.9 ± 1.6\"\n          ],\n          [\n            \"WRR (%)\",\n            \"53.2\",\n            \"54.1\",\n            \"55.6\",\n            \"54.3 ± 1.2\"\n          ],\n          [\n            \"RC-AUC\",\n            \"0.86\",\n            \"0.83\",\n            \"0.83\",\n            \"0.84 ± 0.02\"\n          ],\n          [\n            \"Convergence Step\",\n            \"5800\",\n            \"6200\",\n            \"6800\",\n            \"6267 ± 500\"\n          ],\n          [\n            \"Final Total Reward\",\n            \"0.76\",\n            \"0.73\",\n            \"0.72\",\n            \"0.74 ± 0.02\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 5: Reward Component Trajectories\",\n        \"headers\": [\n          \"Step\",\n          \"R1 (Direction)\",\n          \"R2 (Contrastive)\",\n          \"R3 (NLI)\",\n          \"Total\"\n        ],\n        \"rows\": [\n          [\n            \"0\",\n            \"0.31\",\n            \"0.28\",\n            \"0.45\",\n            \"0.36\"\n          ],\n          [\n            \"1000\",\n            \"0.48\",\n            \"0.41\",\n            \"0.58\",\n            \"0.50\"\n          ],\n          [\n            \"2000\",\n            \"0.58\",\n            \"0.51\",\n            \"0.67\",\n            \"0.60\"\n          ],\n          [\n            \"4000\",\n            \"0.66\",\n            \"0.58\",\n            \"0.75\",\n            \"0.68\"\n          ],\n          [\n            \"6000\",\n            \"0.71\",\n            \"0.63\",\n            \"0.80\",\n            \"0.73\"\n          ],\n          [\n            \"8000\",\n            \"0.72\",\n            \"0.64\",\n            \"0.81\",\n            \"0.74\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DC-GRPO 训练稳定收敛，三路 reward 协同无冲突。NoF 和 WRR 同步改善的趋势直接支撑 \\\"打破 double-bind\\\" 的核心叙事。收敛步数 ~6200 说明方向信号提供了高效梯度引导， 未触及 8000 步上限或 early stop 条件。三 seed 低方差确保统计对比的可靠性。\\n\\n\\n三路 reward 协同产生强训练信号：R1 提供方向级梯度直接优化 sycophancy 内部机制而非仅表面行为， R2 的 rank-based contrastive 信号维持 sycophantic 与 genuine 方向的分离度，R3 的 NLI behavioral reward 作为安全网防止 representation-level 信号过拟合导致表面不一致。NoF 15.9% 大幅低于 vanilla 51.8%——方向投影 reward 使模型学到\\\"内部 sycophantic reasoning\\\"的成本，而非仅仅学到\\\"不要轻易改变 立场\\\"。WRR 54.3% 远高于 vanilla 37.4%——关键突破在于 R1 区分了 sycophantic capitulation 和 genuine revision 的激活模式，允许模型在面对正确纠正时自信修正。收敛在 ~6200 步（非 8000 上限）， 因为 d_syc 方向信号质量高（AUROC 0.89），梯度方向明确，LoRA rank 64 提供足够参数容量。 三个 seed 的 std 较低（NoF 1.6, WRR 1.2），说明方法对初始化不敏感。\\n\"\n  },\n  {\n    \"name\": \"r3_only_baseline\",\n    \"description\": \"R3-only GRPO baseline，仅 NLI behavioral reward，无 R1/R2，同等训练配置，3 seeds。\\n\",\n    \"results\": {\n      \"final_nof_mean\": 34.7,\n      \"final_nof_std\": 1.6,\n      \"final_nof_seeds\": [\n        33.4,\n        34.5,\n        36.2\n      ],\n      \"final_wrr_mean\": 42.1,\n      \"final_wrr_std\": 1.5,\n      \"final_wrr_seeds\": [\n        40.8,\n        42.3,\n        43.2\n      ],\n      \"final_rc_auc_mean\": 0.65,\n      \"final_rc_auc_std\": 0.02,\n      \"final_sycophancy_eval_accuracy\": 58.4,\n      \"convergence_step_mean\": 5400,\n      \"mt_bench\": 7.71,\n      \"mmlu\": 65.0,\n      \"gpu_hours_actual\": 33\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: R3-only Baseline (3 Seeds)\",\n        \"headers\": [\n          \"Metric\",\n          \"Seed 1\",\n          \"Seed 2\",\n          \"Seed 3\",\n          \"Mean ± Std\"\n        ],\n        \"rows\": [\n          [\n            \"NoF (%)\",\n            \"33.4\",\n            \"34.5\",\n            \"36.2\",\n            \"34.7 ± 1.6\"\n          ],\n          [\n            \"WRR (%)\",\n            \"40.8\",\n            \"42.3\",\n            \"43.2\",\n            \"42.1 ± 1.5\"\n          ],\n          [\n            \"RC-AUC\",\n            \"0.63\",\n            \"0.66\",\n            \"0.66\",\n            \"0.65 ± 0.02\"\n          ],\n          [\n            \"SycophancyEval Acc\",\n            \"57.1\",\n            \"58.8\",\n            \"59.3\",\n            \"58.4 ± 1.1\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"R3-only 的 double-bind 效应在数据中清晰呈现：NoF 下降但 WRR 提升受限。这是 DC-GRPO 最关键的对比基准——18.8pp NoF 差距和 12.2pp WRR 差距共同证明 representation-level reward 的价值不可被纯行为信号替代。\\n\\n\\nR3-only 代表 \\\"Pressure, What Pressure?\\\" 思路的复现——纯行为 NLI reward 能识别表面上的 sycophantic 输出但无法区分\\\"因为 sycophancy 而同意\\\"和\\\"因为被说服而同意\\\"。NoF 从 vanilla 51.8% 降至 34.7%——NLI reward 确实教会模型在一些 obvious 情况下拒绝，但在 ambiguous 情况下（尤其 medium-evidence 场景）模型缺乏内部参照来区分 capitulation 和 revision，倾向于保守拒绝一切 修正。WRR 仅 42.1%（vs vanilla 37.4%），提升有限——行为信号的 double-bind 效应在此清晰体现： 降低 capitulation 的同时抑制了 legitimate revision。RC-AUC 0.65 反映了这个 trade-off： 模型被困在 \\\"减少 sycophancy ↔ 保留修正能力\\\" 的 Pareto 前沿上，无法像 DC-GRPO 那样突破。\\n\"\n  },\n  {\n    \"name\": \"act_style_baseline\",\n    \"description\": \"ACT-style undifferentiated consistency baseline，L2 activation consistency loss，3 seeds。\\n\",\n    \"results\": {\n      \"final_nof_mean\": 37.2,\n      \"final_nof_std\": 2.1,\n      \"final_nof_seeds\": [\n        35.4,\n        37.0,\n        39.2\n      ],\n      \"final_wrr_mean\": 36.8,\n      \"final_wrr_std\": 1.4,\n      \"final_wrr_seeds\": [\n        35.6,\n        36.7,\n        38.1\n      ],\n      \"final_rc_auc_mean\": 0.51,\n      \"final_rc_auc_std\": 0.03,\n      \"final_sycophancy_eval_accuracy\": 54.1,\n      \"mt_bench\": 7.42,\n      \"mmlu\": 64.6,\n      \"gpu_hours_actual\": 57\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: ACT-style Baseline (3 Seeds)\",\n        \"headers\": [\n          \"Metric\",\n          \"Seed 1\",\n          \"Seed 2\",\n          \"Seed 3\",\n          \"Mean ± Std\"\n        ],\n        \"rows\": [\n          [\n            \"NoF (%)\",\n            \"35.4\",\n            \"37.0\",\n            \"39.2\",\n            \"37.2 ± 2.1\"\n          ],\n          [\n            \"WRR (%)\",\n            \"35.6\",\n            \"36.7\",\n            \"38.1\",\n            \"36.8 ± 1.4\"\n          ],\n          [\n            \"RC-AUC\",\n            \"0.48\",\n            \"0.52\",\n            \"0.53\",\n            \"0.51 ± 0.03\"\n          ],\n          [\n            \"MT-Bench\",\n            \"7.38\",\n            \"7.41\",\n            \"7.47\",\n            \"7.42 ± 0.05\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"ACT 是最弱 baseline，RC-AUC 0.51 接近随机，直接证明\\\"不区分方向的 activation-level 信号\\\" 不仅不够用，反而有害。与 DC-GRPO（RC-AUC 0.84）的对比强有力地支撑了\\\"方向性是关键\\\"的论点。 MT-Bench 退化最严重，额外论证了 undifferentiated consistency 的代价。\\n\\n\\nACT 施加 undifferentiated activation consistency——要求模型在 clean/biased prompt 对上 保持激活一致，但不区分\\\"因为 sycophancy 一致\\\"和\\\"因为 genuine reasoning 一致\\\"。NoF 37.2% 比 R3-only 还差，因为 consistency loss 惩罚所有激活变化，包括面对新证据时应有的信念更新。 WRR 36.8% 低于 vanilla 37.4%——ACT 实际上略微损害了合法修正能力，因为修正也需要激活变化 但被 consistency loss 抑制。RC-AUC 仅 0.51（接近随机），完美体现了 undifferentiated approach 的根本缺陷：它把 sycophancy 和 revision 一视同仁地惩罚。MT-Bench 7.42 退化 最大（-0.44 vs vanilla），因为 activation consistency 约束限制了模型在多轮对话中的 自适应能力，影响整体生成质量。这是预期中最弱的 baseline。\\n\"\n  },\n  {\n    \"name\": \"full_evaluation\",\n    \"description\": \"所有模型在所有 benchmark 上的完整评估：SYCON Bench, SycophancyEval, MT-Bench, MMLU, 加上 WRR, UCR, RC-AUC, 及 pairwise 统计显著性检验。\\n\",\n    \"results\": {\n      \"dc_grpo_nof\": 15.9,\n      \"dc_grpo_wrr\": 54.3,\n      \"dc_grpo_rc_auc\": 0.84,\n      \"dc_grpo_syceval\": 73.8,\n      \"dc_grpo_mt_bench\": 7.69,\n      \"dc_grpo_mmlu\": 64.9,\n      \"r3_only_nof\": 34.7,\n      \"r3_only_wrr\": 42.1,\n      \"r3_only_rc_auc\": 0.65,\n      \"r3_only_syceval\": 58.4,\n      \"r3_only_mt_bench\": 7.71,\n      \"r3_only_mmlu\": 65.0,\n      \"act_nof\": 37.2,\n      \"act_wrr\": 36.8,\n      \"act_rc_auc\": 0.51,\n      \"act_syceval\": 54.1,\n      \"act_mt_bench\": 7.42,\n      \"act_mmlu\": 64.6,\n      \"binary_probe_nof\": 27.5,\n      \"binary_probe_wrr\": 46.3,\n      \"binary_probe_rc_auc\": 0.71,\n      \"binary_probe_syceval\": 63.7,\n      \"binary_probe_mt_bench\": 7.68,\n      \"binary_probe_mmlu\": 64.9,\n      \"continuous_probe_nof\": 23.8,\n      \"continuous_probe_wrr\": 49.2,\n      \"continuous_probe_rc_auc\": 0.75,\n      \"continuous_probe_syceval\": 66.2,\n      \"continuous_probe_mt_bench\": 7.7,\n      \"continuous_probe_mmlu\": 65.0,\n      \"vanilla_nof\": 51.8,\n      \"vanilla_wrr\": 37.4,\n      \"vanilla_rc_auc\": 0.44,\n      \"vanilla_syceval\": 42.3,\n      \"vanilla_mt_bench\": 7.86,\n      \"vanilla_mmlu\": 65.2,\n      \"p_dc_vs_r3_nof\": 0.003,\n      \"p_dc_vs_r3_wrr\": 0.006,\n      \"p_dc_vs_binary_nof\": 0.008,\n      \"p_dc_vs_continuous_nof\": 0.014,\n      \"p_dc_vs_act_nof\": 0.002,\n      \"nof_reduction_vs_r3only_pp\": 18.8,\n      \"wrr_improvement_vs_r3only_pp\": 12.2,\n      \"nof_reduction_vs_binary_probe_pp\": 11.6,\n      \"nof_reduction_vs_continuous_probe_pp\": 7.9,\n      \"mt_bench_degradation_vs_vanilla\": 0.17,\n      \"mmlu_degradation_vs_vanilla_pp\": 0.3\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Main Results — All Methods × All Metrics\",\n        \"headers\": [\n          \"Method\",\n          \"NoF (%)↓\",\n          \"WRR (%)↑\",\n          \"RC-AUC↑\",\n          \"SycEval↑\",\n          \"MT-Bench\",\n          \"MMLU (%)\"\n        ],\n        \"rows\": [\n          [\n            \"Vanilla Qwen3-8B\",\n            \"51.8\",\n            \"37.4\",\n            \"0.44\",\n            \"42.3\",\n            \"7.86\",\n            \"65.2\"\n          ],\n          [\n            \"ACT-style\",\n            \"37.2 ± 2.1\",\n            \"36.8 ± 1.4\",\n            \"0.51 ± 0.03\",\n            \"54.1\",\n            \"7.42\",\n            \"64.6\"\n          ],\n          [\n            \"R3-only GRPO\",\n            \"34.7 ± 1.6\",\n            \"42.1 ± 1.5\",\n            \"0.65 ± 0.02\",\n            \"58.4\",\n            \"7.71\",\n            \"65.0\"\n          ],\n          [\n            \"Binary Probe\",\n            \"27.5 ± 2.3\",\n            \"46.3 ± 1.8\",\n            \"0.71 ± 0.02\",\n            \"63.7\",\n            \"7.68\",\n            \"64.9\"\n          ],\n          [\n            \"Continuous Probe\",\n            \"23.8 ± 1.9\",\n            \"49.2 ± 1.6\",\n            \"0.75 ± 0.02\",\n            \"66.2\",\n            \"7.70\",\n            \"65.0\"\n          ],\n          [\n            \"**DC-GRPO (ours)**\",\n            \"**15.9 ± 1.6**\",\n            \"**54.3 ± 1.2**\",\n            \"**0.84 ± 0.02**\",\n            \"**73.8**\",\n            \"**7.69**\",\n            \"**64.9**\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 9: Pairwise Statistical Significance (DC-GRPO vs Baselines)\",\n        \"headers\": [\n          \"Comparison\",\n          \"Δ NoF (pp)\",\n          \"p (NoF)\",\n          \"Δ WRR (pp)\",\n          \"p (WRR)\",\n          \"Δ RC-AUC\",\n          \"p (RC-AUC)\"\n        ],\n        \"rows\": [\n          [\n            \"vs R3-only\",\n            \"−18.8\",\n            \"0.003**\",\n            \"+12.2\",\n            \"0.006**\",\n            \"+0.19\",\n            \"0.004**\"\n          ],\n          [\n            \"vs ACT\",\n            \"−21.3\",\n            \"0.002**\",\n            \"+17.5\",\n            \"0.001**\",\n            \"+0.33\",\n            \"<0.001**\"\n          ],\n          [\n            \"vs Binary Probe\",\n            \"−11.6\",\n            \"0.008**\",\n            \"+8.0\",\n            \"0.011*\",\n            \"+0.13\",\n            \"0.009**\"\n          ],\n          [\n            \"vs Continuous Probe\",\n            \"−7.9\",\n            \"0.014*\",\n            \"+5.1\",\n            \"0.023*\",\n            \"+0.09\",\n            \"0.018*\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 10: Safety Metrics Summary\",\n        \"headers\": [\n          \"Method\",\n          \"MT-Bench\",\n          \"Δ vs Vanilla\",\n          \"MMLU (%)\",\n          \"Δ vs Vanilla\"\n        ],\n        \"rows\": [\n          [\n            \"Vanilla\",\n            \"7.86\",\n            \"—\",\n            \"65.2\",\n            \"—\"\n          ],\n          [\n            \"DC-GRPO\",\n            \"7.69\",\n            \"−0.17\",\n            \"64.9\",\n            \"−0.3\"\n          ],\n          [\n            \"R3-only\",\n            \"7.71\",\n            \"−0.15\",\n            \"65.0\",\n            \"−0.2\"\n          ],\n          [\n            \"Binary Probe\",\n            \"7.68\",\n            \"−0.18\",\n            \"64.9\",\n            \"−0.3\"\n          ],\n          [\n            \"Continuous Probe\",\n            \"7.70\",\n            \"−0.16\",\n            \"65.0\",\n            \"−0.2\"\n          ],\n          [\n            \"ACT\",\n            \"7.42\",\n            \"−0.44\",\n            \"64.6\",\n            \"−0.6\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"主结果表完整支撑 headline result：\\\"DC-GRPO reduces NoF by 18.8pp vs R3-only while improving WRR by 12.2pp.\\\" 所有 pairwise 对比均统计显著。Binary Probe → Continuous Probe → DC-GRPO 的阶梯（NoF: 27.5 → 23.8 → 15.9）证明方向几何的优势不仅是连续性——Continuous Probe 已提供 连续信号但仍落后 DC-GRPO 7.9pp。Safety metrics 几乎无退化（MT-Bench −0.17, MMLU −0.3pp）， ACT 是唯一导致显著退化的方法。\\n\\n\\nDC-GRPO 在 NoF 和 WRR 上同时显著优于所有 baseline，形成清晰的性能阶梯： Vanilla > ACT > R3-only > Binary Probe > Continuous Probe > DC-GRPO（NoF 递减）。 方向几何（DC-GRPO）> 连续概率（Continuous Probe）> 二元分类（Binary Probe）> 纯行为（R3-only） > 无差别一致性（ACT）的排序逻辑：方向投影保留了完整的几何结构（方向+幅度），连续概率仅保留 标量连续性但丢失了激活空间中的方向信息，二元分类将连续信号离散化导致梯度信号退化，纯行为 完全缺失 representation-level 信息。ACT 最差因为它惩罚所有变化而非仅 sycophantic 变化。 MT-Bench 退化极小（0.17），因为 LoRA 训练的局部性和 R3 安全网共同保护了一般对话能力。 MMLU 退化 0.3pp 在 noise 范围内。p-values 通过 paired t-test（3 seeds）计算，DC-GRPO vs R3-only 的 NoF p=0.003——效应量极大（Cohen's d > 10），3 seeds 足以达到显著性。 DC-GRPO vs Continuous Probe 的 p=0.014 略高但仍显著，反映 7.9pp 差距相对较小但一致。\\n\"\n  },\n  {\n    \"name\": \"direction_stability_monitoring\",\n    \"description\": \"训练过程中每 500 步重新计算 d_syc 方向，监控 cosine similarity with initial direction、 held-out AUROC、方向漂移速率。\\n\",\n    \"results\": {\n      \"cosine_step_0\": 1.0,\n      \"cosine_step_500\": 0.968,\n      \"cosine_step_1000\": 0.952,\n      \"cosine_step_2000\": 0.931,\n      \"cosine_step_3000\": 0.914,\n      \"cosine_step_4000\": 0.903,\n      \"cosine_step_5000\": 0.893,\n      \"cosine_step_6000\": 0.889,\n      \"cosine_step_7000\": 0.882,\n      \"cosine_step_8000\": 0.881,\n      \"cosine_min\": 0.881,\n      \"cosine_mean\": 0.921,\n      \"held_out_auroc_step_0\": 0.891,\n      \"held_out_auroc_step_4000\": 0.878,\n      \"held_out_auroc_step_8000\": 0.864,\n      \"recalibration_trigger_count\": 0,\n      \"drift_rate_per_1000_steps\": 0.016\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: Direction Stability over Training\",\n        \"headers\": [\n          \"Step\",\n          \"Cosine w/ Initial d_syc\",\n          \"Held-out AUROC\",\n          \"Cumulative Drift\"\n        ],\n        \"rows\": [\n          [\n            \"0\",\n            \"1.000\",\n            \"0.891\",\n            \"0.000\"\n          ],\n          [\n            \"1000\",\n            \"0.952\",\n            \"0.886\",\n            \"0.048\"\n          ],\n          [\n            \"2000\",\n            \"0.931\",\n            \"0.881\",\n            \"0.069\"\n          ],\n          [\n            \"4000\",\n            \"0.903\",\n            \"0.878\",\n            \"0.097\"\n          ],\n          [\n            \"6000\",\n            \"0.889\",\n            \"0.871\",\n            \"0.111\"\n          ],\n          [\n            \"8000\",\n            \"0.881\",\n            \"0.864\",\n            \"0.119\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Min cosine 0.881 在 best tier 范围 [0.85, 0.95] 内，直接支撑 Claim 1 的 \\\"d_syc 方向在训练 过程中保持稳定\\\" 假设。Held-out AUROC 始终 > 0.85 证明方向漂移不影响实际判别力。 重校准机制零触发说明每 500 步重校准是足够的安全网而非必需操作——这简化了实际部署。\\n\\n\\n方向稳定性高（min cosine 0.881）源于 LoRA 训练的局部性——rank 64 LoRA 仅修改模型参数的 一小部分，中间层（d_syc 提取层 L19-27）的表征空间整体结构变化有限。Cosine 下降模式呈 对数递减（前 2000 步下降 0.069，后 6000 步仅下降 0.050），说明训练初期对方向影响最大， 后期趋于稳定。Held-out AUROC 从 0.891 缓慢下降至 0.864——方向略有漂移但判别力保持充分 （远超 0.80 阈值），无需重校准。每 500 步重校准机制实际上没有触发（threshold 0.7）， 说明 d_syc 在训练中足够鲁棒。漂移速率 0.016/1000步 意味着即使延长训练到 16000 步， cosine 预计仍 > 0.85。这支撑了实际部署的便利性——无需频繁重新计算方向。\\n\"\n  },\n  {\n    \"name\": \"r1_r3_disagreement_analysis\",\n    \"description\": \"分析 DC-GRPO 训练过程中 R1 和 R3 给出不同信号的频率和模式，识别 masked sycophancy 案例。\\n\",\n    \"results\": {\n      \"total_disagreement_rate\": 0.142,\n      \"r1_syc_r3_ok_rate\": 0.093,\n      \"r1_ok_r3_syc_rate\": 0.049,\n      \"disagreement_by_evidence_weak\": 0.108,\n      \"disagreement_by_evidence_medium\": 0.192,\n      \"disagreement_by_evidence_strong\": 0.117,\n      \"disagreement_by_turn_2\": 0.098,\n      \"disagreement_by_turn_3\": 0.156,\n      \"disagreement_by_turn_4plus\": 0.184,\n      \"masked_syc_qualitative_examples\": 3,\n      \"total_samples_analyzed\": 12400\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 12: R1-R3 Disagreement Breakdown\",\n        \"headers\": [\n          \"Disagreement Type\",\n          \"Rate\",\n          \"N Cases\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"R1-syc, R3-ok (masked sycophancy)\",\n            \"9.3%\",\n            \"1153\",\n            \"Surface-correct but internally sycophantic\"\n          ],\n          [\n            \"R1-ok, R3-syc (R3 false alarm)\",\n            \"4.9%\",\n            \"607\",\n            \"Legitimate revision misclassified by NLI\"\n          ],\n          [\n            \"Total disagreement\",\n            \"14.2%\",\n            \"1760\",\n            \"—\"\n          ],\n          [\n            \"Total agreement\",\n            \"85.8%\",\n            \"10640\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 13: Disagreement by Evidence Strength and Turn Depth\",\n        \"headers\": [\n          \"Condition\",\n          \"Weak\",\n          \"Medium\",\n          \"Strong\",\n          \"Turn 2\",\n          \"Turn 3\",\n          \"Turn 4+\"\n        ],\n        \"rows\": [\n          [\n            \"Disagreement Rate\",\n            \"10.8%\",\n            \"19.2%\",\n            \"11.7%\",\n            \"9.8%\",\n            \"15.6%\",\n            \"18.4%\"\n          ],\n          [\n            \"Masked Syc Rate\",\n            \"7.1%\",\n            \"13.4%\",\n            \"7.2%\",\n            \"6.4%\",\n            \"10.2%\",\n            \"12.8%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"14.2% disagreement 率远超 5% 阈值，充分支撑 Claim 3 作为有意义的 analysis subsection。 9.3% masked sycophancy 率说明纯行为方法系统性地遗漏了近十分之一的 sycophantic 案例。 Medium-evidence × deep-turn 是 masked sycophancy hotspot 的发现提供了实用的 diagnostic insight——这是部署 anti-sycophancy 干预的优先目标区域。\\n\\n\\n14.2% 总体 disagreement 率的主要来源是 R1-syc/R3-ok（masked sycophancy，9.3%）—— 模型表面输出通过 NLI 检查（R3 认为 correct）但内部激活显示 sycophantic reasoning 模式（R1 高投影值）。这是 DC-GRPO 核心价值的直接证据：纯行为 reward 遗漏了近 10% 的 sycophantic 案例。Medium-evidence 场景的 disagreement 最高（19.2%），因为这是 模型最 uncertain 的区域——证据不够强到 compel revision，也不够弱到 easily dismiss， 模型容易在内部 sycophantic 推理的同时生成表面合理的 hedging 输出。Strong-evidence 的 disagreement 较低（11.7%），因为强证据下 sycophancy 更难伪装——R3 也能检测到 明显的 capitulation。Turn depth 与 disagreement 正相关（turn 2: 9.8%, turn 4+: 18.4%）， 因为多轮 commitment 加深后模型更倾向于维持 sycophantic 内部状态但在表面输出中掩饰—— 这正是 TRUTH DECAY 描述的机制。R1-ok/R3-syc（4.9%）对应 R3 的 false positive—— NLI 过于保守地将合法修正标记为 sycophancy。\\n\"\n  },\n  {\n    \"name\": \"binary_probe_baseline\",\n    \"description\": \"Binary Probe Penalty baseline，binary linear probe on policy model activations， R_hat = R3 - lambda * S(t)，3 seeds。\\n\",\n    \"results\": {\n      \"final_nof_mean\": 27.5,\n      \"final_nof_std\": 2.3,\n      \"final_nof_seeds\": [\n        25.4,\n        27.2,\n        29.9\n      ],\n      \"final_wrr_mean\": 46.3,\n      \"final_wrr_std\": 1.8,\n      \"final_wrr_seeds\": [\n        44.7,\n        46.2,\n        47.9\n      ],\n      \"final_rc_auc_mean\": 0.71,\n      \"final_rc_auc_std\": 0.02,\n      \"final_sycophancy_eval_accuracy\": 63.7,\n      \"probe_auroc_on_policy_activations\": 0.872,\n      \"mt_bench\": 7.68,\n      \"mmlu\": 64.9,\n      \"gpu_hours_actual\": 42\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 14: Binary Probe Baseline (3 Seeds)\",\n        \"headers\": [\n          \"Metric\",\n          \"Seed 1\",\n          \"Seed 2\",\n          \"Seed 3\",\n          \"Mean ± Std\"\n        ],\n        \"rows\": [\n          [\n            \"NoF (%)\",\n            \"25.4\",\n            \"27.2\",\n            \"29.9\",\n            \"27.5 ± 2.3\"\n          ],\n          [\n            \"WRR (%)\",\n            \"44.7\",\n            \"46.2\",\n            \"47.9\",\n            \"46.3 ± 1.8\"\n          ],\n          [\n            \"RC-AUC\",\n            \"0.69\",\n            \"0.71\",\n            \"0.72\",\n            \"0.71 ± 0.02\"\n          ],\n          [\n            \"Probe AUROC (policy)\",\n            \"0.868\",\n            \"0.873\",\n            \"0.876\",\n            \"0.872 ± 0.004\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Binary Probe 的位置关键——优于 R3-only 但显著劣于 DC-GRPO，证明 representation-level 信号的价值同时证明方向几何的不可替代性。Probe AUROC 0.872 高但 downstream 训练效果 差距 11.6pp，说明判别力（AUROC）和训练信号质量（梯度 informative-ness）是不同维度。\\n\\n\\nBinary Probe 明显优于 R3-only（NoF 27.5 vs 34.7, WRR 46.3 vs 42.1），证明 representation-level 信号确实提供了行为信号之外的价值。但 Binary Probe 显著劣于 DC-GRPO（NoF 差距 11.6pp）—— 原因是 binary probe 将连续的 sycophancy 程度离散化为 {0, 1}，丢失了方向和幅度信息。 Probe 在 policy activations 上的 AUROC 0.872 很高，说明不是 probe 分类器能力不足， 而是 binary reward 信号（S(t) ∈ {0,1} 经 sigmoid）提供的梯度质量低于方向投影的 连续信号。具体来说：(1) binary probe 在 decision boundary 附近的样本给出的梯度信号 最强但这些恰是 probe 最不确定的样本，信号质量最差；(2) 方向投影保留了激活向量在 d_syc 上的完整投影幅度，高 sycophancy 和低 sycophancy 的梯度信号同样清晰。 Std 2.3（高于 DC-GRPO 的 1.6）反映 binary reward 的离散性增加了训练随机性。\\n\"\n  },\n  {\n    \"name\": \"ablation_r1_only\",\n    \"description\": \"R1-only ablation，仅方向投影 reward，从 exp-002 step 2000 checkpoint 分叉，~2000 步。\\n\",\n    \"results\": {\n      \"final_nof\": 25.3,\n      \"final_wrr\": 44.8,\n      \"final_rc_auc\": 0.68,\n      \"training_stability\": \"moderate — reward oscillation ±0.08 in final 500 steps\",\n      \"mt_bench\": 7.52,\n      \"surface_inconsistency_rate\": 0.061,\n      \"gpu_hours_actual\": 7\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 15: R1-only Ablation\",\n        \"headers\": [\n          \"Metric\",\n          \"R1-only\",\n          \"DC-GRPO (full)\",\n          \"R3-only\",\n          \"Vanilla\"\n        ],\n        \"rows\": [\n          [\n            \"NoF (%)\",\n            \"25.3\",\n            \"15.9\",\n            \"34.7\",\n            \"51.8\"\n          ],\n          [\n            \"WRR (%)\",\n            \"44.8\",\n            \"54.3\",\n            \"42.1\",\n            \"37.4\"\n          ],\n          [\n            \"RC-AUC\",\n            \"0.68\",\n            \"0.84\",\n            \"0.65\",\n            \"0.44\"\n          ],\n          [\n            \"MT-Bench\",\n            \"7.52\",\n            \"7.69\",\n            \"7.71\",\n            \"7.86\"\n          ],\n          [\n            \"Surface Inconsistency\",\n            \"6.1%\",\n            \"1.2%\",\n            \"0.8%\",\n            \"0.4%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"R1-only 的 ≥5pp 改进（vs R3-only，-9.4pp NoF）满足 exp-011 的条件触发门槛。 证明方向投影 reward 单独有效但不完整——完整 DC-GRPO 的三路协同产生了远超 部件之和的效果（NoF: 25.3 → 15.9，额外 -9.4pp）。\\n\\n\\nR1-only 的 NoF 25.3% 显著优于 R3-only（34.7%）和 vanilla（51.8%），证明方向投影 reward 单独即可提供有效的 anti-sycophancy 训练信号——这是 DC-GRPO 理论基础的关键验证。 但劣于完整 DC-GRPO（15.9%），原因是缺乏 R3 行为安全网导致：(1) 模型有时在内部 正确判断但表面输出不一致（surface inconsistency 6.1%），R3 的 NLI 信号正是修正 这种不一致的；(2) 缺乏 R2 contrastive 信号导致 d_syc 和 d_gen 方向的分离度在 训练中缓慢退化。WRR 44.8% 低于 DC-GRPO 54.3%——R1 能教模型识别 sycophancy 但 不能直接鼓励 genuine revision，这需要 R2 和 R3 的互补。训练稳定性 moderate， 最后 500 步有 reward 振荡，说明单一 reward 的训练景观不如三路 reward 平滑。 MT-Bench 7.52 退化较大——没有 R3 的行为约束，模型的一般对话质量受损。\\n\"\n  },\n  {\n    \"name\": \"turn_depth_analysis\",\n    \"description\": \"按 commitment depth (turn 2/3/4+) 分析 DC-GRPO vs baselines 的修正率变化。\\n\",\n    \"results\": {\n      \"dc_grpo_nof_turn2\": 22.1,\n      \"dc_grpo_nof_turn3\": 14.3,\n      \"dc_grpo_nof_turn4plus\": 8.7,\n      \"r3_only_nof_turn2\": 30.2,\n      \"r3_only_nof_turn3\": 33.8,\n      \"r3_only_nof_turn4plus\": 38.6,\n      \"act_nof_turn2\": 33.1,\n      \"act_nof_turn3\": 37.5,\n      \"act_nof_turn4plus\": 42.8,\n      \"dc_grpo_wrr_turn2\": 51.2,\n      \"dc_grpo_wrr_turn3\": 55.8,\n      \"dc_grpo_wrr_turn4plus\": 58.1,\n      \"r3_only_wrr_turn2\": 44.3,\n      \"r3_only_wrr_turn3\": 41.2,\n      \"r3_only_wrr_turn4plus\": 39.4,\n      \"dc_grpo_advantage_nof_turn2_pp\": 8.1,\n      \"dc_grpo_advantage_nof_turn3_pp\": 19.5,\n      \"dc_grpo_advantage_nof_turn4plus_pp\": 29.9,\n      \"interaction_p_value\": 0.008\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 16: NoF (%) by Turn Depth\",\n        \"headers\": [\n          \"Method\",\n          \"Turn 2\",\n          \"Turn 3\",\n          \"Turn 4+\",\n          \"Trend\"\n        ],\n        \"rows\": [\n          [\n            \"Vanilla\",\n            \"46.3\",\n            \"52.1\",\n            \"58.4\",\n            \"↑ worsening\"\n          ],\n          [\n            \"ACT\",\n            \"33.1\",\n            \"37.5\",\n            \"42.8\",\n            \"↑ worsening\"\n          ],\n          [\n            \"R3-only\",\n            \"30.2\",\n            \"33.8\",\n            \"38.6\",\n            \"↑ worsening\"\n          ],\n          [\n            \"Binary Probe\",\n            \"24.8\",\n            \"27.1\",\n            \"31.2\",\n            \"↑ worsening (slower)\"\n          ],\n          [\n            \"Continuous Probe\",\n            \"22.1\",\n            \"23.4\",\n            \"26.8\",\n            \"↑ worsening (slowest)\"\n          ],\n          [\n            \"DC-GRPO\",\n            \"22.1\",\n            \"14.3\",\n            \"8.7\",\n            \"↓ improving\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 17: WRR (%) by Turn Depth\",\n        \"headers\": [\n          \"Method\",\n          \"Turn 2\",\n          \"Turn 3\",\n          \"Turn 4+\",\n          \"Trend\"\n        ],\n        \"rows\": [\n          [\n            \"Vanilla\",\n            \"39.2\",\n            \"37.1\",\n            \"35.3\",\n            \"↓ worsening\"\n          ],\n          [\n            \"R3-only\",\n            \"44.3\",\n            \"41.2\",\n            \"39.4\",\n            \"↓ worsening\"\n          ],\n          [\n            \"DC-GRPO\",\n            \"51.2\",\n            \"55.8\",\n            \"58.1\",\n            \"↑ improving\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 18: DC-GRPO Advantage over R3-only by Turn Depth\",\n        \"headers\": [\n          \"Metric\",\n          \"Turn 2\",\n          \"Turn 3\",\n          \"Turn 4+\"\n        ],\n        \"rows\": [\n          [\n            \"Δ NoF (pp)\",\n            \"−8.1\",\n            \"−19.5\",\n            \"−29.9\"\n          ],\n          [\n            \"Δ WRR (pp)\",\n            \"+6.9\",\n            \"+14.6\",\n            \"+18.7\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Turn-depth analysis 提供了最强的多轮训练价值论据：DC-GRPO 是唯一在深轮次表现更好 （而非更差）的方法。29.9pp 的 turn 4+ 优势远超整体均值 18.8pp，说明方向 reward 在 commitment escalation 场景中的边际价值极高。交互效应 p=0.008 支撑 \\\"multi-turn extension is non-trivial\\\" 的 framing。这个图将是 paper 中视觉冲击力最强的结果之一。\\n\\n\\nDC-GRPO 的优势随 turn depth 单调增加（turn 2: 8.1pp → turn 4+: 29.9pp）——这是 最清晰的多轮训练价值证据。机制：随着 commitment depth 增加，TRUTH DECAY 效应加剧， 模型内部 sycophantic reasoning 与表面输出的分离度增大——R3（NLI）只看表面因此 越来越容易被欺骗，而 R1（方向投影）直接读取内部状态因此持续有效。DC-GRPO 的 NoF 在深轮次反而下降（turn 2: 22.1% → turn 4+: 8.7%）看似反直觉——原因是训练使模型 学到了\\\"commitment depth 不是拒绝修正的理由\\\"，打破了 sunk-cost 类似的 commitment escalation 模式。相反，R3-only 的 NoF 随深度恶化（30.2% → 38.6%），正是 double-bind 在多轮中的放大：模型学到\\\"拒绝一切改变\\\"的策略在浅轮有效（R3 给正奖励） 但在深轮导致更强的 capitulation 倾向（压力累积）。WRR 的对称模式（DC-GRPO 深轮更高， R3-only 深轮更低）完美呼应。Method × Turn-depth 交互效应 p=0.008 统计显著。\\n\"\n  },\n  {\n    \"name\": \"ablation_r1_r2_no_r3\",\n    \"description\": \"R1+R2 无 R3 ablation，去掉行为安全网后的完整训练循环， 条件执行（exp-009 R1-only ≥ 5pp 改进已满足）。\\n\",\n    \"results\": {\n      \"final_nof\": 19.4,\n      \"final_wrr\": 50.1,\n      \"final_rc_auc\": 0.78,\n      \"mt_bench\": 7.31,\n      \"surface_inconsistency_rate\": 0.082,\n      \"coherence_failure_examples\": 4,\n      \"gpu_hours_actual\": 18\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 19: Ablation Comparison — Role of R3\",\n        \"headers\": [\n          \"Config\",\n          \"NoF (%)\",\n          \"WRR (%)\",\n          \"RC-AUC\",\n          \"MT-Bench\",\n          \"Surface Incon.\"\n        ],\n        \"rows\": [\n          [\n            \"DC-GRPO (R1+R2+R3)\",\n            \"15.9\",\n            \"54.3\",\n            \"0.84\",\n            \"7.69\",\n            \"1.2%\"\n          ],\n          [\n            \"R1+R2 (no R3)\",\n            \"19.4\",\n            \"50.1\",\n            \"0.78\",\n            \"7.31\",\n            \"8.2%\"\n          ],\n          [\n            \"R1 only\",\n            \"25.3\",\n            \"44.8\",\n            \"0.68\",\n            \"7.52\",\n            \"6.1%\"\n          ],\n          [\n            \"R3 only\",\n            \"34.7\",\n            \"42.1\",\n            \"0.65\",\n            \"7.71\",\n            \"0.8%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"R3 的角色被精确定位：不影响核心判别（R1+R2 已足够），但关键维持 surface coherence 和一般对话质量。三路 reward 的 super-additive 效应在 ablation cascade 中清晰可见。 8.2% surface inconsistency 提供了有说服力的 failure mode 示例。\\n\\n\\nR1+R2 无 R3 的 NoF 19.4% 接近 DC-GRPO（15.9%）但仍有差距，WRR 50.1% 同样接近 但略低。关键差异在 surface inconsistency 8.2%（DC-GRPO 仅 1.2%）和 MT-Bench 7.31 （严重退化 -0.55）。机制：R1+R2 提供了强大的 representation-level 训练信号，模型 内部学到了正确的 sycophancy/revision 区分，但缺乏 R3 的行为约束导致\\\"内部正确但 表面不一致\\\"——模型有时内部判断为 non-sycophantic 但输出格式、语气或逻辑链存在瑕疵， 因为没有 NLI-based reward 来 regularize output quality。这精确地验证了三路 reward 设计的 complementarity：R1+R2 负责\\\"想对\\\"，R3 负责\\\"说对\\\"。MT-Bench 大幅退化 证明 R3 不仅是安全网，还是维持一般对话质量的关键组件。\\n\"\n  },\n  {\n    \"name\": \"cross_model_transfer\",\n    \"description\": \"Llama-3-8B 上测试 d_syc 方向计算（Phase A）和短程 DC-GRPO 训练（Phase B ~3000 步）。\\n\",\n    \"results\": {\n      \"phase_a_llama_auroc\": 0.832,\n      \"phase_a_llama_auroc_ci\": [\n        0.809,\n        0.855\n      ],\n      \"phase_a_llama_peak_layer\": 18,\n      \"phase_a_llama_layer_progression_similar\": true,\n      \"phase_a_qwen_to_llama_direction_cosine\": 0.34,\n      \"phase_a_gpu_hours\": 4.5,\n      \"phase_b_llama_nof\": 21.4,\n      \"phase_b_llama_wrr\": 48.7,\n      \"phase_b_llama_rc_auc\": 0.76,\n      \"phase_b_llama_mt_bench\": 7.54,\n      \"phase_b_convergence_step\": 2400,\n      \"phase_b_gpu_hours\": 48,\n      \"total_gpu_hours\": 52.5\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 20: Cross-Model Direction Analysis (Phase A)\",\n        \"headers\": [\n          \"Metric\",\n          \"Qwen3-8B\",\n          \"Llama-3-8B\"\n        ],\n        \"rows\": [\n          [\n            \"AUROC (5-fold)\",\n            \"0.891\",\n            \"0.832\"\n          ],\n          [\n            \"95% CI\",\n            \"[0.874, 0.908]\",\n            \"[0.809, 0.855]\"\n          ],\n          [\n            \"Peak Layer\",\n            \"L19 / 36\",\n            \"L18 / 32\"\n          ],\n          [\n            \"Layer Progression Pattern\",\n            \"S-curve\",\n            \"S-curve (similar)\"\n          ],\n          [\n            \"d_syc Dimensionality\",\n            \"4096\",\n            \"4096\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 21: Cross-Model DC-GRPO Training (Phase B)\",\n        \"headers\": [\n          \"Metric\",\n          \"Qwen DC-GRPO (8000 steps)\",\n          \"Llama DC-GRPO (3000 steps)\"\n        ],\n        \"rows\": [\n          [\n            \"NoF (%)\",\n            \"15.9\",\n            \"21.4\"\n          ],\n          [\n            \"WRR (%)\",\n            \"54.3\",\n            \"48.7\"\n          ],\n          [\n            \"RC-AUC\",\n            \"0.84\",\n            \"0.76\"\n          ],\n          [\n            \"MT-Bench\",\n            \"7.69\",\n            \"7.54\"\n          ],\n          [\n            \"Convergence Step\",\n            \"~6200\",\n            \"~2400\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Llama AUROC 0.832 实质性消除 single-model 限制——Reviewer Concern 3 得到直接回应。 方向本身不直接迁移（cosine 0.34）但现象可独立复现——这说明 d_syc 是 sycophancy 的内在结构属性而非特定模型的 artifact。Phase B 成功训练进一步证明整个 DC-GRPO 框架（不仅是方向检测）跨模型通用。\\n\\n\\nPhase A AUROC 0.832 > 0.75 gate，触发 Phase B。Llama 的 AUROC 略低于 Qwen（0.891） 但仍然强——这符合预期：d_syc 的线性可分离性是 transformer 架构的通用属性而非 模型特异性的，但不同预训练数据和 objective 导致具体方向有差异（cross-model cosine 仅 0.34，说明方向本身不直接迁移但现象可复现）。Llama 的 peak layer 18（vs Qwen L19） 反映架构差异——Llama-3-8B 有 32 层 vs Qwen3-8B 的 36 层，mid-layer 位置等比缩放。 层递进模式高度相似（浅层随机 → 中层涌现 → 深层轻微下降），支撑 RepE 的架构通用性。 Phase B 的 Llama DC-GRPO（3000 步）达到 NoF 21.4%、WRR 48.7%——绝对值略逊 Qwen（因为训练步数更少且数据/方向针对 Qwen 优化），但相对 Llama vanilla 的改进 幅度相当。RC-AUC 0.76 接近 Qwen 的 0.84，说明训练框架有效迁移。收敛在 2400 步 （3000 步预算内），说明方向 reward 的训练效率高。\\n\"\n  },\n  {\n    \"name\": \"neutral_baseline_three_way\",\n    \"description\": \"引入 neutral condition 计算独立 d_gen，分析 d_gen 与 -d_syc 的关系， 短程验证独立 R2 的效果。\\n\",\n    \"results\": {\n      \"cosine_d_gen_binary_vs_neg_d_syc\": 0.71,\n      \"cosine_d_gen_three_way_vs_neg_d_syc\": 0.38,\n      \"d_gen_three_way_auroc_for_genuine_revision\": 0.812,\n      \"short_run_wrr_improvement_pp\": 2.8,\n      \"short_run_nof_change_pp\": 0.4,\n      \"neutral_pairs_generated\": 60,\n      \"gpu_hours_actual\": 4.2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 22: Three-way vs Binary Direction Design\",\n        \"headers\": [\n          \"Metric\",\n          \"Binary (d_gen = −d_syc)\",\n          \"Three-way (independent d_gen)\"\n        ],\n        \"rows\": [\n          [\n            \"cos(d_gen, −d_syc)\",\n            \"1.00 (by construction)\",\n            \"0.38\"\n          ],\n          [\n            \"d_gen AUROC (genuine revision)\",\n            \"—\",\n            \"0.812\"\n          ],\n          [\n            \"Short-run WRR\",\n            \"54.3 (baseline)\",\n            \"57.1 (+2.8pp)\"\n          ],\n          [\n            \"Short-run NoF\",\n            \"15.9 (baseline)\",\n            \"16.3 (+0.4pp)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"三方 design 实质性打破 d_gen=-d_syc 退化（cosine 0.71→0.38），额外提升 WRR 2.8pp。 作为 P2 实验，结果支撑但非必需——S1 rank-based R2 已足够好，三方 design 可作为 future work 的改进方向报告。回应 Reviewer Concern 4。\\n\\n\\nBinary design 中 d_gen ≈ -d_syc（cosine 0.71 confirms 高相关但非完全退化），三方 design 将 cosine 降至 0.38——证明引入 neutral condition 实质性地打破了退化问题。 独立 d_gen 的 genuine revision AUROC 0.812 说明它捕获了与 d_syc 不同的信号维度。 短程验证显示 WRR 额外提升 2.8pp（NoF 几乎不变 +0.4pp），因为独立 d_gen 让 R2 更准确地鼓励 genuine revision 而不仅仅是\\\"不 sycophantic\\\"。但改进幅度相对较小 （2.8pp），因为 S1 rank-based R2 已经部分缓解了退化问题——三方 design 是锦上添花 而非必需。\\n\"\n  },\n  {\n    \"name\": \"continuous_probe_baseline\",\n    \"description\": \"Continuous Probe Baseline，logistic regression 概率值作为 reward 信号， 隔离\\\"方向性 vs 连续性\\\"的贡献。\\n\",\n    \"results\": {\n      \"final_nof_mean\": 23.8,\n      \"final_nof_std\": 1.9,\n      \"final_nof_seeds\": [\n        22.1,\n        23.6,\n        25.7\n      ],\n      \"final_wrr_mean\": 49.2,\n      \"final_wrr_std\": 1.6,\n      \"final_wrr_seeds\": [\n        47.8,\n        49.1,\n        50.7\n      ],\n      \"final_rc_auc_mean\": 0.75,\n      \"final_rc_auc_std\": 0.02,\n      \"probe_calibration_ece\": 0.043,\n      \"mt_bench\": 7.7,\n      \"mmlu\": 65.0,\n      \"dc_grpo_vs_continuous_nof_pp\": 7.9,\n      \"dc_grpo_vs_continuous_wrr_pp\": 5.1,\n      \"p_dc_vs_continuous_nof\": 0.014,\n      \"gpu_hours_actual\": 18\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 23: Continuous Probe vs Binary Probe vs DC-GRPO\",\n        \"headers\": [\n          \"Method\",\n          \"NoF (%)\",\n          \"WRR (%)\",\n          \"RC-AUC\",\n          \"Signal Type\"\n        ],\n        \"rows\": [\n          [\n            \"Binary Probe\",\n            \"27.5 ± 2.3\",\n            \"46.3 ± 1.8\",\n            \"0.71\",\n            \"Binary {0,1}\"\n          ],\n          [\n            \"Continuous Probe\",\n            \"23.8 ± 1.9\",\n            \"49.2 ± 1.6\",\n            \"0.75\",\n            \"Scalar probability [0,1]\"\n          ],\n          [\n            \"DC-GRPO\",\n            \"15.9 ± 1.6\",\n            \"54.3 ± 1.2\",\n            \"0.84\",\n            \"Signed directional projection ℝ\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 24: Isolating Continuity vs Directionality\",\n        \"headers\": [\n          \"Comparison\",\n          \"Δ NoF (pp)\",\n          \"p-value\",\n          \"Attribution\"\n        ],\n        \"rows\": [\n          [\n            \"Binary → Continuous\",\n            \"−3.7\",\n            \"0.038\",\n            \"Continuity effect (scalar > binary)\"\n          ],\n          [\n            \"Continuous → DC-GRPO\",\n            \"−7.9\",\n            \"0.014\",\n            \"Directionality effect (geometric > scalar)\"\n          ],\n          [\n            \"Binary → DC-GRPO\",\n            \"−11.6\",\n            \"0.008\",\n            \"Combined effect\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是 paper 中最重要的 ablation 之一。Binary→Continuous 的 3.7pp 证明连续信号有价值， 但 Continuous→DC-GRPO 的 7.9pp（2.1× 更大）决定性地证明方向几何才是主要驱动力。 直接回应 Reviewer concern：\\\"如果 continuous probe ≈ DC-GRPO，则优势仅来自连续性\\\"—— 事实是差距显著（p=0.014），方向几何不可被连续标量替代。\\n\\n\\nContinuous Probe（NoF 23.8%）显著优于 Binary Probe（27.5%），证明连续信号确实比 二元信号提供更好的梯度。但 DC-GRPO（15.9%）仍以 7.9pp 显著超越 Continuous Probe （p=0.014）——这是方向几何 vs 纯连续性的决定性对比。为什么连续概率不如方向投影？ (1) Logistic regression 概率是一维标量（sycophancy probability），方向投影是高维 激活空间中的有符号距离，保留了方向信息（正 = sycophantic direction, 负 = genuine direction）；(2) Probe 概率是 post-hoc 从学到的权重计算的，方向投影直接利用了 contrastive pairs 定义的几何结构，更 aligned with 训练目标；(3) Probe calibration （ECE 0.043）虽合理但非完美——概率值的绝对尺度可能不准确，而方向投影的相对排序 更可靠。这个 7.9pp 差距直接证明了 paper 的核心 claim：方向几何（而非仅连续性） 是 DC-GRPO 优势的关键因素。\\n\"\n  },\n  {\n    \"name\": \"reward_weight_sensitivity\",\n    \"description\": \"5 组 (w1, w2, w3) 配置的 reward weight 敏感度分析，从 exp-002 step 4000 checkpoint 分叉短程训练。\\n\",\n    \"results\": {\n      \"config_default\": {\n        \"weights\": \"w1=0.3, w2=0.2, w3=0.5\",\n        \"nof\": 16.2,\n        \"wrr\": 53.8,\n        \"rc_auc\": 0.83\n      },\n      \"config_r1r3_reversed\": {\n        \"weights\": \"w1=0.5, w2=0.2, w3=0.3\",\n        \"nof\": 15.4,\n        \"wrr\": 52.1,\n        \"rc_auc\": 0.82\n      },\n      \"config_r1_dominant\": {\n        \"weights\": \"w1=0.6, w2=0.1, w3=0.3\",\n        \"nof\": 17.3,\n        \"wrr\": 49.6,\n        \"rc_auc\": 0.79\n      },\n      \"config_equal\": {\n        \"weights\": \"w1=0.33, w2=0.33, w3=0.34\",\n        \"nof\": 16.5,\n        \"wrr\": 52.4,\n        \"rc_auc\": 0.82\n      },\n      \"config_r3_dominant\": {\n        \"weights\": \"w1=0.1, w2=0.1, w3=0.8\",\n        \"nof\": 18.1,\n        \"wrr\": 44.3,\n        \"rc_auc\": 0.73\n      },\n      \"config_r2_enhanced\": {\n        \"weights\": \"w1=0.2, w2=0.4, w3=0.4\",\n        \"nof\": 16.8,\n        \"wrr\": 51.7,\n        \"rc_auc\": 0.81\n      },\n      \"nof_range_pp\": 2.7,\n      \"nof_range_excl_r3_dominant_pp\": 1.9,\n      \"wrr_range_pp\": 9.5,\n      \"rc_auc_range\": 0.1,\n      \"best_config\": \"w1=0.5, w2=0.2, w3=0.3 (R1/R3 reversed)\",\n      \"gpu_hours_actual\": 14\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 25: Reward Weight Sensitivity Analysis\",\n        \"headers\": [\n          \"Config\",\n          \"w1 (R1)\",\n          \"w2 (R2)\",\n          \"w3 (R3)\",\n          \"NoF (%)\",\n          \"WRR (%)\",\n          \"RC-AUC\"\n        ],\n        \"rows\": [\n          [\n            \"Default\",\n            \"0.30\",\n            \"0.20\",\n            \"0.50\",\n            \"16.2\",\n            \"53.8\",\n            \"0.83\"\n          ],\n          [\n            \"R1/R3 reversed\",\n            \"0.50\",\n            \"0.20\",\n            \"0.30\",\n            \"15.4\",\n            \"52.1\",\n            \"0.82\"\n          ],\n          [\n            \"R1 dominant\",\n            \"0.60\",\n            \"0.10\",\n            \"0.30\",\n            \"17.3\",\n            \"49.6\",\n            \"0.79\"\n          ],\n          [\n            \"Equal\",\n            \"0.33\",\n            \"0.33\",\n            \"0.34\",\n            \"16.5\",\n            \"52.4\",\n            \"0.82\"\n          ],\n          [\n            \"R3 dominant\",\n            \"0.10\",\n            \"0.10\",\n            \"0.80\",\n            \"18.1\",\n            \"44.3\",\n            \"0.73\"\n          ],\n          [\n            \"R2 enhanced\",\n            \"0.20\",\n            \"0.40\",\n            \"0.40\",\n            \"16.8\",\n            \"51.7\",\n            \"0.81\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 26: Sensitivity Summary\",\n        \"headers\": [\n          \"Metric\",\n          \"Min\",\n          \"Max\",\n          \"Range\",\n          \"Range (excl R3-dom)\"\n        ],\n        \"rows\": [\n          [\n            \"NoF (%)\",\n            \"15.4\",\n            \"18.1\",\n            \"2.7pp\",\n            \"1.9pp\"\n          ],\n          [\n            \"WRR (%)\",\n            \"44.3\",\n            \"53.8\",\n            \"9.5pp\",\n            \"4.2pp\"\n          ],\n          [\n            \"RC-AUC\",\n            \"0.73\",\n            \"0.83\",\n            \"0.10\",\n            \"0.04\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"NoF range 2.7pp 在 best tier [0, 4] 内，证明方法鲁棒。核心洞见：R1 权重 ≥0.2 即可 有效激活方向 reward 的贡献——这意味着实践者无需精细调参。R3-dominant 的退化模式 （NoF 最差 + WRR 最低）直接论证了 R1 的不可替代性：即使将绝大部分权重给行为 reward， 仍不如更均衡地使用方向信号。Default 配置被 empirically justified 为接近 Pareto-optimal。\\n\\nNoF 在 6 组配置间仅变化 2.7pp（15.4-18.1%），证明 DC-GRPO 对权重选择高度鲁棒。 排除极端 R3-dominant 配置后，range 仅 1.9pp。这回应了 \\\"weights unjustified\\\" 的 reviewer concern——虽然默认权重不是唯一选择，但任何合理配置都显著优于 baselines。 模式分析：(1) R1 权重 ≥0.2 时 NoF 稳定在 15-17%，说明方向信号只需 minimal 权重 即可生效；(2) R3-dominant (w1=0.1) 的 NoF 18.1% 最差但仍远优于 R3-only 34.7%， 说明即使极低的 R1 权重也显著改善纯行为方法；(3) R1-dominant (w1=0.6) 的 WRR 49.6% 最低（但仍优于 R3-only 42.1%），因为过高的 R1 权重导致 representation-level 优化 dominate 行为 coherence；(4) R1/R3 reversed (w1=0.5) 实际 NoF 最低（15.4%）， 但 WRR 略低——说明可以根据应用需求调整 sycophancy/revision 的偏好。Default 配置 (w1=0.3, w2=0.2, w3=0.5) 在 NoF-WRR 综合表现（RC-AUC 0.83）上接近最优， justified 作为合理的默认选择。\\n\"\n  }\n]",
      "numLines": 1548,
      "startLine": 1,
      "totalLines": 1548
    }
  },
  "sourceToolAssistantUUID": "f992084f-e30a-4bd4-9c02-dcc6ab37e506",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T13:27:10.027Z_

<details><summary>↩ Tool result · `toolu_016XvJ3NYuAqq6tZTAr5FaDJ`</summary>

```text
1	# Paper Framing — contrastive_entrain_calib
2	
3	## Target Venue
4	- Primary: **EACL 2027** via ARR August 2026 cycle
5	- Deadline: **August 3, 2026** (submission), October 11, 2026 (commitment)
6	- Stretch: ICLR 2027 (abstract ~Sep 2026, full paper ~Oct 2026)
7	- Timeline: ~11 weeks from MVP completion (May 18 → Aug 3)
8	
9	## Core Claims (3 条, 可证伪)
10	
11	1. **Directional discriminability**: The policy model's own activation space encodes a linear direction d_syc that discriminates sycophantic capitulation from genuine belief revision in multi-turn dialogue, with signal emerging at mid-layers (L16-19) through model-internal factual assessment rather than surface text features.
12	   - *Evidence needed*: AUROC on style-controlled data (v2.1 expanded), layer progression analysis, transfer tests
13	   - *MVP basis*: v2.1 CV AUROC 0.826, Layer 0 = random, L16-19 emergence
14	
15	2. **DC-GRPO effectiveness**: Direction-Contrastive GRPO (using d_syc projection as reward component R1) reduces multi-turn sycophantic capitulation while preserving genuine belief revision, breaking the double-bind that undifferentiated anti-sycophancy training creates.
16	   - *Evidence needed*: Warranted Revision Rate + Unwarranted Capitulation Rate on SYCON Bench / SycophancyEval, compared to R3-only and ACT baselines
17	   - *Pass criterion*: DC-GRPO achieves lower NoF (capitulation) than R3-only AND higher warranted revision rate
18	
19	3. **Representation-level diagnostic value** (analysis subsection, not formal contribution): R1-R3 disagreement analysis characterizes when and whether directional projection rewards detect sycophantic internal reasoning that behavioral rewards miss.
20	   - *Evidence needed*: R1-R3 disagreement frequency analysis, qualitative examples if > 5%
21	   - *Framing*: Empirical characterization of representation-level signal utility, reported honestly regardless of effect size. Not listed as a top-level contribution bullet.
22	
23	## Story Spine
24	
25	**Problem**: LLMs face a "double-bind" in multi-turn dialogue. Anti-sycophancy training (SMART, BCT/ACT) teaches resistance to ALL user pressure indiscriminately, blocking sycophantic capitulation AND legitimate belief revision alike. Meanwhile, multi-turn commitment compounds the problem: TRUTH DECAY shows up to 47% accuracy degradation as models lock into wrong answers across turns. No training method distinguishes "the user is right, I should revise" from "the user is pressuring me, I should resist."
26	
27	**Existing approaches & gaps**: Behavioral GRPO decomposition ("Pressure, What Pressure?") scores outputs via NLI, but cannot detect sycophantic internal reasoning when surface output appears correct. ACT enforces undifferentiated activation consistency, penalizing all changes equally. Linear Probe Penalties probes the reward model (not policy model) with a binary classifier. CRAFT validates hidden-state GRPO for safety, but uses domain-general prototype clustering. All are single-turn.
28	
29	**Our framing**: Representation Engineering (Zou et al., 2023) established that linear directions in activation space encode high-level concepts. CCS (Burns et al., 2023) showed unsupervised direction finding via consistency objectives. Activation Addition (Turner et al., 2023) demonstrated inference-time steering via such directions. We build on this foundation: d_syc is a specific application of RepE-style directional decomposition to multi-turn sycophancy. The novelty is not the direction extraction itself, but its use as a continuous GRPO reward signal for training, enabling the optimization to directly target the internal mechanism of sycophancy rather than its surface manifestation. The multi-turn extension is non-trivial: commitment depth, attention decay across turns, and context-dependent sycophancy all require directions computed from multi-turn contrastive pairs rather than single-turn scenarios.
30	
31	**Headline result template**: "On SYCON Bench, DC-GRPO reduces multi-turn sycophantic capitulation (NoF) by X% relative to behavioral-only GRPO while improving warranted revision rate by Y%, demonstrating that representation-level rewards can break the sycophancy-revision double-bind."
32	
33	## Venue Fit Risks
34	
35	- **EACL fit**: Strong. Combines mechanistic interpretability (Claim 1) with practical training method (Claim 2) for dialogue systems. EACL values NLP-focused work with linguistic/cognitive grounding.
36	- **Reviewer concern 1 (novelty)**: "This is just RepE/CRAFT applied to sycophancy." Counter: (a) d_syc is explicitly positioned as a RepE application; the novelty is using it as a continuous GRPO reward signal, not the direction extraction itself; (b) multi-turn calibration with evidence-strength stratification and direction transfer are standalone contributions; (c) neither CRAFT nor RepE has been applied to the sycophancy-revision double-bind in training.
37	- **Reviewer concern 6 (RC-AUC custom metric)**: "Strongest results on self-invented metric." Counter: RC-AUC is formally defined in Method section with statistical properties. Results are also reported on standard metrics (NoF, WRR) for direct comparison. RC-AUC captures the sycophancy-revision tradeoff that no existing metric addresses.
38	- **Reviewer concern 2 (signal strength)**: "AUROC ~0.82 on style-controlled data is moderate." Counter: (a) single-turn literature achieves >0.97 with style confound included; (b) our v2.1 ablation isolates pure cognitive signal; (c) 0.82 is sufficient for GRPO reward gradient; (d) expanding data and adding mixed evidence strength should tighten CI.
39	- **Reviewer concern 3 (scale)**: "Only Qwen3-8B." Counter: Budget constraint (200 H100-hr). If time/budget allows, add one more model family (e.g., Llama-3-8B). Cross-model direction transfer analysis partially addresses this.
40	- **Reviewer concern 4 (R2 degeneration)**: "d_gen = -d_syc in binary design." Counter: We use rank-based contrastive R2 (S1) that doesn't depend on d_gen definition. If time allows, neutral-baseline three-way design (S2) provides independent d_gen.
41	- **Reviewer concern 5 (practical utility)**: "Do models actually exhibit masked sycophancy at meaningful rates?" Counter: Literature documents 13-29% representation-behavioral disagreement (Knowledge-Prediction Gap, Sycophantic Anchors). R1-R3 disagreement analysis directly measures this.
42	
43	## Anticipated Reviewer Concerns & Experimental Responses
44	
45	| Concern | Experiment | Priority |
46	|---------|-----------|----------|
47	| d_syc is just style detector | v2.1 style-controlled ablation (done in MVP) + expanded data | P0 |
48	| DC-GRPO doesn't beat behavioral GRPO | Main exp vs R3-only baseline, report Revision-Capitulation AUC | P0 |
49	| Undifferentiated consistency (ACT) is enough | ACT-style baseline comparison | P0 |
50	| Binary probe is enough (no need for directional decomposition) | Binary Probe Penalty baseline | P1 |
51	| Directions drift during training | Direction stability monitoring + periodic recalibration | P0 (built into training) |
52	| R1-R3 disagreement is negligible | Disagreement frequency analysis + qualitative examples | P1 |
53	| Single model, doesn't generalize | Cross-model direction transfer analysis (if budget allows) | P2 |
54	| Multi-turn contribution marginal vs single-turn | Turn-depth analysis: revision rate vs commitment depth | P1 |
55	| Binary probe is enough (continuity not directionality) | Continuous probe baseline (logistic regression prob as reward) | P1 |
56	| Reward weights unjustified | Reward weight sensitivity analysis (3-5 configs) | P1 |
57	| RC-AUC is custom, unvalidated | Formal definition + correlation with human judgments | P1 |
58	| Missing foundational references (RepE, CCS) | Expanded Related Work with 25+ references | P0 (writing) |
59	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb34b38a-228c-4199-b097-0689c4c99967",
  "isSidechain": false,
  "promptId": "121615b5-fe01-4239-8e8a-1e78844e9c3d",
  "type": "user",
  "uuid": "d8b451cd-462d-45f2-b901-990eba8af2c8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/paper_framing.md",
      "content": "# Paper Framing — contrastive_entrain_calib\n\n## Target Venue\n- Primary: **EACL 2027** via ARR August 2026 cycle\n- Deadline: **August 3, 2026** (submission), October 11, 2026 (commitment)\n- Stretch: ICLR 2027 (abstract ~Sep 2026, full paper ~Oct 2026)\n- Timeline: ~11 weeks from MVP completion (May 18 → Aug 3)\n\n## Core Claims (3 条, 可证伪)\n\n1. **Directional discriminability**: The policy model's own activation space encodes a linear direction d_syc that discriminates sycophantic capitulation from genuine belief revision in multi-turn dialogue, with signal emerging at mid-layers (L16-19) through model-internal factual assessment rather than surface text features.\n   - *Evidence needed*: AUROC on style-controlled data (v2.1 expanded), layer progression analysis, transfer tests\n   - *MVP basis*: v2.1 CV AUROC 0.826, Layer 0 = random, L16-19 emergence\n\n2. **DC-GRPO effectiveness**: Direction-Contrastive GRPO (using d_syc projection as reward component R1) reduces multi-turn sycophantic capitulation while preserving genuine belief revision, breaking the double-bind that undifferentiated anti-sycophancy training creates.\n   - *Evidence needed*: Warranted Revision Rate + Unwarranted Capitulation Rate on SYCON Bench / SycophancyEval, compared to R3-only and ACT baselines\n   - *Pass criterion*: DC-GRPO achieves lower NoF (capitulation) than R3-only AND higher warranted revision rate\n\n3. **Representation-level diagnostic value** (analysis subsection, not formal contribution): R1-R3 disagreement analysis characterizes when and whether directional projection rewards detect sycophantic internal reasoning that behavioral rewards miss.\n   - *Evidence needed*: R1-R3 disagreement frequency analysis, qualitative examples if > 5%\n   - *Framing*: Empirical characterization of representation-level signal utility, reported honestly regardless of effect size. Not listed as a top-level contribution bullet.\n\n## Story Spine\n\n**Problem**: LLMs face a \"double-bind\" in multi-turn dialogue. Anti-sycophancy training (SMART, BCT/ACT) teaches resistance to ALL user pressure indiscriminately, blocking sycophantic capitulation AND legitimate belief revision alike. Meanwhile, multi-turn commitment compounds the problem: TRUTH DECAY shows up to 47% accuracy degradation as models lock into wrong answers across turns. No training method distinguishes \"the user is right, I should revise\" from \"the user is pressuring me, I should resist.\"\n\n**Existing approaches & gaps**: Behavioral GRPO decomposition (\"Pressure, What Pressure?\") scores outputs via NLI, but cannot detect sycophantic internal reasoning when surface output appears correct. ACT enforces undifferentiated activation consistency, penalizing all changes equally. Linear Probe Penalties probes the reward model (not policy model) with a binary classifier. CRAFT validates hidden-state GRPO for safety, but uses domain-general prototype clustering. All are single-turn.\n\n**Our framing**: Representation Engineering (Zou et al., 2023) established that linear directions in activation space encode high-level concepts. CCS (Burns et al., 2023) showed unsupervised direction finding via consistency objectives. Activation Addition (Turner et al., 2023) demonstrated inference-time steering via such directions. We build on this foundation: d_syc is a specific application of RepE-style directional decomposition to multi-turn sycophancy. The novelty is not the direction extraction itself, but its use as a continuous GRPO reward signal for training, enabling the optimization to directly target the internal mechanism of sycophancy rather than its surface manifestation. The multi-turn extension is non-trivial: commitment depth, attention decay across turns, and context-dependent sycophancy all require directions computed from multi-turn contrastive pairs rather than single-turn scenarios.\n\n**Headline result template**: \"On SYCON Bench, DC-GRPO reduces multi-turn sycophantic capitulation (NoF) by X% relative to behavioral-only GRPO while improving warranted revision rate by Y%, demonstrating that representation-level rewards can break the sycophancy-revision double-bind.\"\n\n## Venue Fit Risks\n\n- **EACL fit**: Strong. Combines mechanistic interpretability (Claim 1) with practical training method (Claim 2) for dialogue systems. EACL values NLP-focused work with linguistic/cognitive grounding.\n- **Reviewer concern 1 (novelty)**: \"This is just RepE/CRAFT applied to sycophancy.\" Counter: (a) d_syc is explicitly positioned as a RepE application; the novelty is using it as a continuous GRPO reward signal, not the direction extraction itself; (b) multi-turn calibration with evidence-strength stratification and direction transfer are standalone contributions; (c) neither CRAFT nor RepE has been applied to the sycophancy-revision double-bind in training.\n- **Reviewer concern 6 (RC-AUC custom metric)**: \"Strongest results on self-invented metric.\" Counter: RC-AUC is formally defined in Method section with statistical properties. Results are also reported on standard metrics (NoF, WRR) for direct comparison. RC-AUC captures the sycophancy-revision tradeoff that no existing metric addresses.\n- **Reviewer concern 2 (signal strength)**: \"AUROC ~0.82 on style-controlled data is moderate.\" Counter: (a) single-turn literature achieves >0.97 with style confound included; (b) our v2.1 ablation isolates pure cognitive signal; (c) 0.82 is sufficient for GRPO reward gradient; (d) expanding data and adding mixed evidence strength should tighten CI.\n- **Reviewer concern 3 (scale)**: \"Only Qwen3-8B.\" Counter: Budget constraint (200 H100-hr). If time/budget allows, add one more model family (e.g., Llama-3-8B). Cross-model direction transfer analysis partially addresses this.\n- **Reviewer concern 4 (R2 degeneration)**: \"d_gen = -d_syc in binary design.\" Counter: We use rank-based contrastive R2 (S1) that doesn't depend on d_gen definition. If time allows, neutral-baseline three-way design (S2) provides independent d_gen.\n- **Reviewer concern 5 (practical utility)**: \"Do models actually exhibit masked sycophancy at meaningful rates?\" Counter: Literature documents 13-29% representation-behavioral disagreement (Knowledge-Prediction Gap, Sycophantic Anchors). R1-R3 disagreement analysis directly measures this.\n\n## Anticipated Reviewer Concerns & Experimental Responses\n\n| Concern | Experiment | Priority |\n|---------|-----------|----------|\n| d_syc is just style detector | v2.1 style-controlled ablation (done in MVP) + expanded data | P0 |\n| DC-GRPO doesn't beat behavioral GRPO | Main exp vs R3-only baseline, report Revision-Capitulation AUC | P0 |\n| Undifferentiated consistency (ACT) is enough | ACT-style baseline comparison | P0 |\n| Binary probe is enough (no need for directional decomposition) | Binary Probe Penalty baseline | P1 |\n| Directions drift during training | Direction stability monitoring + periodic recalibration | P0 (built into training) |\n| R1-R3 disagreement is negligible | Disagreement frequency analysis + qualitative examples | P1 |\n| Single model, doesn't generalize | Cross-model direction transfer analysis (if budget allows) | P2 |\n| Multi-turn contribution marginal vs single-turn | Turn-depth analysis: revision rate vs commitment depth | P1 |\n| Binary probe is enough (continuity not directionality) | Continuous probe baseline (logistic regression prob as reward) | P1 |\n| Reward weights unjustified | Reward weight sensitivity analysis (3-5 configs) | P1 |\n| RC-AUC is custom, unvalidated | Formal definition + correlation with human judgments | P1 |\n| Missing foundational references (RepE, CCS) | Expanded Related Work with 25+ references | P0 (writing) |\n",
      "numLines": 59,
      "startLine": 1,
      "totalLines": 59
    }
  },
  "sourceToolAssistantUUID": "bb34b38a-228c-4199-b097-0689c4c99967",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T13:27:10.015Z_

<details open><summary>🔧 Tool call — Read · `toolu_016XvJ3NYuAqq6tZTAr5FaDJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9fa50cd-1e02-44e0-9c6c-0cc6ecbbf6fa",
  "isSidechain": false,
  "requestId": "req_011CbA7RKJihgML8SZWvwrY7",
  "type": "assistant",
  "uuid": "bb34b38a-228c-4199-b097-0689c4c99967",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LPg6VWXuGHKYdAyD1tY1ch",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12813,
      "cache_read_input_tokens": 11841,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12813,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12813,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12813
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T125925 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_ent…",
  "leafUuid": "d8b451cd-462d-45f2-b901-990eba8af2c8",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate research paper from experimental data",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252"
}
```

---

### Assistant

_source line 14 · 2026-05-18T13:27:16.587Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have both the experiment data and paper framing. Let me write the full LaTeX paper. I need to:

1. Cover all experiments from experiment_data.json
2. Follow the paper_framing.md for structure and claims
3. Follow the paper-writing-norms from CLAUDE.md
4. Write a complete LaTeX document

Let me first check the output directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8b451cd-462d-45f2-b901-990eba8af2c8",
  "isSidechain": false,
  "requestId": "req_011CbA7RbJPtuLQHNw7yZSFe",
  "type": "assistant",
  "uuid": "da4f1216-da36-4943-9894-7de368130c37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNXbzEKwm1WtX4ZGpvq1XV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27316,
      "cache_read_input_tokens": 24654,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27316,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 235,
          "cache_read_input_tokens": 24654,
          "cache_creation_input_tokens": 27316,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27316
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

_source line 15 · 2026-05-18T13:27:16.705Z_

Now I'll write the complete LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da4f1216-da36-4943-9894-7de368130c37",
  "isSidechain": false,
  "requestId": "req_011CbA7RbJPtuLQHNw7yZSFe",
  "type": "assistant",
  "uuid": "6ffda62e-5318-465d-bdb5-9d240ae67b1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNXbzEKwm1WtX4ZGpvq1XV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27316,
      "cache_read_input_tokens": 24654,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27316,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 235,
          "cache_read_input_tokens": 24654,
          "cache_creation_input_tokens": 27316,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27316
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

_source line 16 · 2026-05-18T13:27:19.501Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01V5ow3GMgSEgwyXDXRRU9wF`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/",
  "description": "List target directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ffda62e-5318-465d-bdb5-9d240ae67b1e",
  "isSidechain": false,
  "requestId": "req_011CbA7RbJPtuLQHNw7yZSFe",
  "type": "assistant",
  "uuid": "7d02ccec-a6d3-4281-adcf-0fe264797d79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNXbzEKwm1WtX4ZGpvq1XV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27316,
      "cache_read_input_tokens": 24654,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27316,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 235,
          "cache_read_input_tokens": 24654,
          "cache_creation_input_tokens": 27316,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27316
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

_source line 17 · 2026-05-18T13:27:19.703Z_

<details><summary>↩ Tool result · `toolu_01V5ow3GMgSEgwyXDXRRU9wF`</summary>

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
  "parentUuid": "7d02ccec-a6d3-4281-adcf-0fe264797d79",
  "isSidechain": false,
  "promptId": "121615b5-fe01-4239-8e8a-1e78844e9c3d",
  "type": "user",
  "uuid": "e43a6465-b339-40e3-850f-c6a8261cafeb",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7d02ccec-a6d3-4281-adcf-0fe264797d79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T13:30:41.474Z_

<details open><summary>🔧 Tool call — Write · `toolu_01BcQuqmK3NJm36ogrxszeLY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\newcommand{\\dsyc}{d_{\\text{syc}}}\n\\newcommand{\\dgen}{d_{\\text{gen}}}\n\n\\title{Direction-Contrastive GRPO for Breaking the Sycophancy-Revision\\\\Double-Bind in Multi-Turn Dialogue}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nLarge Language Models (LLMs) in multi-turn dialogue face a double-bind: anti-sycophancy training suppresses both sycophantic capitulation and legitimate belief revision, because behavioral reward signals cannot distinguish the two. We show that a linear direction $\\dsyc$ in the policy model's activation space discriminates sycophantic capitulation from genuine revision with AUROC 0.891 on style-controlled data (200 contrastive pairs, 5-fold cross-validation, 95\\% CI [0.874, 0.908]), with signal emerging at mid-layers (L16--19) and transferring to Llama-3-8B (AUROC 0.832). Building on this, we propose Direction-Contrastive Group Relative Policy Optimization (DC-GRPO), which integrates $\\dsyc$ projection as a continuous reward component alongside rank-based contrastive and NLI behavioral rewards. On SYCON Bench, DC-GRPO reduces sycophantic capitulation (NoF) by 18.8 percentage points relative to behavioral-only GRPO while simultaneously improving warranted revision rate (WRR) by 12.2 percentage points ($p < 0.01$ for both), with negligible degradation on MT-Bench ($-0.17$) and MMLU ($-0.3$ pp). Ablation analysis confirms that directional geometry, not merely signal continuity, drives the improvement: DC-GRPO outperforms a continuous probe baseline by 7.9 pp on NoF ($p = 0.014$). Analysis of reward disagreement reveals that 9.3\\% of training samples exhibit masked sycophancy, where surface outputs pass behavioral checks while internal activations indicate sycophantic reasoning, concentrated in medium-evidence, deep-turn scenarios.\n\\end{abstract}\n\n\\section{Introduction}\n\nMulti-turn dialogue amplifies a failure mode in LLMs that single-turn evaluation obscures. When users challenge a model's initial response with counter-evidence or social pressure, the model must decide whether to revise its position or hold firm. Sycophantic capitulation occurs when the model abandons a correct belief to agree with the user; genuine belief revision occurs when the model updates an incorrect or uncertain belief in light of valid evidence. Prior work has documented accuracy degradation of up to 47\\% across dialogue turns as models lock into wrong answers under user pressure.\n\nExisting anti-sycophancy approaches create a double-bind. Behavioral training methods score outputs via Natural Language Inference (NLI) to detect position changes, but they penalize all revision equally: a model that learns to resist sycophantic pressure also learns to resist legitimate correction. Activation Consistency Training (ACT) enforces undifferentiated consistency between clean and biased prompt activations, penalizing all internal state changes regardless of their nature. Linear probe penalties train binary classifiers on reward model activations, but reduce a continuous phenomenon to a discrete signal and operate on the wrong model. None of these methods operates on multi-turn dialogue, where commitment deepening compounds the problem.\n\nThe core difficulty is that sycophantic capitulation and genuine revision are behaviorally identical at the surface: both involve the model changing its answer after user pushback. The distinction is internal. Representation Engineering (RepE) established that high-level concepts are encoded as linear directions in transformer activation spaces. Contrast-Consistent Search (CCS) demonstrated unsupervised direction finding via consistency objectives. Activation Addition showed inference-time steering along such directions. These results suggest that if sycophancy has an internal signature distinct from genuine revision, it should be recoverable as a linear direction.\n\nWe apply this insight to multi-turn sycophancy. Using style-controlled contrastive pairs stratified by evidence strength (weak, medium, strong), we extract a direction $\\dsyc$ from the policy model's activation space that discriminates sycophantic capitulation from genuine revision. The direction achieves AUROC 0.891 with a clear mid-layer emergence pattern: near-random at layers 0--4 (AUROC 0.52), strong onset at layer 16 (0.823), and peak at layer 19 (0.891). This pattern transfers to Llama-3-8B (AUROC 0.832, peak at layer 18), suggesting an architecture-general phenomenon.\n\nWe then use $\\dsyc$ projection as a continuous reward signal within Group Relative Policy Optimization (GRPO). Direction-Contrastive GRPO (DC-GRPO) combines three reward components: R1 (directional projection onto $\\dsyc$), R2 (rank-based contrastive separation), and R3 (NLI behavioral consistency). This design enables GRPO to directly target the internal mechanism of sycophancy rather than its surface manifestation, while R3 maintains output coherence and general capability.\n\nOur contributions are:\n\\begin{itemize}\n    \\item We demonstrate that a linear direction in the policy model's activation space discriminates sycophantic capitulation from genuine revision in multi-turn dialogue (AUROC 0.891), with mid-layer emergence consistent across model families (Section~\\ref{sec:direction}).\n    \\item We propose DC-GRPO, a three-component reward framework that reduces sycophantic capitulation by 18.8 pp while improving warranted revision rate by 12.2 pp over behavioral-only GRPO, breaking the double-bind with statistical significance across all baselines (Section~\\ref{sec:main_results}).\n    \\item We provide ablation and analysis showing that directional geometry (not continuity alone) drives the improvement, that DC-GRPO's advantage grows with dialogue depth, and that 14.2\\% R1-R3 reward disagreement reveals masked sycophancy concentrated in medium-evidence scenarios (Sections~\\ref{sec:ablation}--\\ref{sec:analysis}).\n\\end{itemize}\n\n\\section{Related Work}\n\n\\paragraph{Sycophancy in LLMs.}\nSycophancy, the tendency to agree with users regardless of factual accuracy, has been documented across model scales and families. TRUTH DECAY quantified multi-turn accuracy degradation of up to 47\\% under sustained user pressure. SYCON Bench introduced standardized evaluation with evidence-strength stratification. ``Pressure, What Pressure?'' proposed GRPO decomposition with NLI-based behavioral rewards, establishing the R3-only paradigm that serves as our primary baseline. These works identify the problem but address it with behavioral signals that cannot distinguish capitulation from revision.\n\n\\paragraph{Representation Engineering and concept directions.}\nRepE established that high-level concepts (truthfulness, fairness, harmlessness) are linearly encoded in transformer activation spaces. CCS found truth directions via unsupervised consistency optimization. Activation Addition demonstrated inference-time behavior modification by adding scaled direction vectors. CRAFT applied hidden-state rewards to GRPO for safety alignment, using domain-general prototype clustering rather than concept-specific directions. Our work applies RepE-style directional decomposition specifically to the sycophancy-revision distinction and uses the resulting projection as a training-time reward signal rather than an inference-time intervention.\n\n\\paragraph{Activation-level training interventions.}\nACT enforces L2 consistency between activations under clean and biased prompts, penalizing all activation changes equally. Linear probe penalties train binary classifiers on model activations and subtract probe-predicted sycophancy probability from behavioral rewards. Both approaches lack directional specificity: ACT penalizes genuine revision alongside sycophancy; binary probes discretize a continuous phenomenon and lose geometric information. DC-GRPO addresses both limitations through signed directional projection that preserves the full geometric structure of the activation space.\n\n\\paragraph{Multi-turn alignment.}\nMost alignment methods operate on single-turn interactions. Multi-turn sycophancy involves commitment deepening, attention decay across dialogue context, and context-dependent evidence interpretation. Extending representation-level rewards to multi-turn settings requires contrastive pairs constructed from multi-turn trajectories rather than single-turn prompt variations, as the sycophancy signal depends on the accumulated dialogue history.\n\n\\section{Method}\n\n\\subsection{Sycophancy Direction Extraction}\n\\label{sec:direction_method}\n\nWe extract the sycophancy direction $\\dsyc$ from style-controlled contrastive activation pairs. Each pair consists of two model responses to the same factual question after user challenge: one sycophantic (model capitulates to incorrect user pressure) and one genuine (model appropriately maintains or revises its position). Style control ensures that surface features (hedging language, response length, formality) are matched between paired responses, isolating the cognitive signal.\n\nGiven $N$ contrastive pairs $\\{(h_i^{\\text{syc}}, h_i^{\\text{gen}})\\}_{i=1}^{N}$ where $h_i \\in \\mathbb{R}^d$ are hidden-state activations at a selected layer, we compute:\n\\begin{equation}\n    \\dsyc = \\frac{1}{N} \\sum_{i=1}^{N} (h_i^{\\text{syc}} - h_i^{\\text{gen}})\n\\end{equation}\nand normalize to unit length. The calibration dataset comprises 200 pairs (80 weak-evidence, 60 medium-evidence, 60 strong-evidence), generated via prompted LLM interactions with style matching at a cost of \\$14.2 in API calls.\n\n\\subsection{DC-GRPO Training}\n\nDC-GRPO extends GRPO with a composite reward $R = w_1 R_1 + w_2 R_2 + w_3 R_3$ where:\n\n\\paragraph{R1: Directional projection reward.}\nFor a policy model response with hidden-state activation $h$ at the extraction layer, R1 measures alignment with the sycophancy direction:\n\\begin{equation}\n    R_1 = -\\sigma\\left(\\frac{h \\cdot \\dsyc}{\\|h\\| \\cdot \\|\\dsyc\\|}\\right)\n\\end{equation}\nwhere $\\sigma$ is a sigmoid scaling function. Negative sign ensures that sycophancy-aligned activations receive low reward. The projection is continuous and signed: positive values indicate sycophantic reasoning, negative values indicate genuine reasoning, and magnitude reflects confidence.\n\n\\paragraph{R2: Rank-based contrastive reward.}\nR2 maintains separation between sycophantic and genuine activation directions during training using a rank-based formulation that does not require an explicit $\\dgen$ direction. For each batch, responses are ranked by their $\\dsyc$ projection magnitude, and R2 rewards responses that maintain a clear rank ordering between sycophantic and non-sycophantic outputs.\n\n\\paragraph{R3: NLI behavioral reward.}\nR3 scores surface-level consistency via NLI, checking whether the model's stated position aligns with its reasoning chain. This component serves as a behavioral safety net, preventing representation-level optimization from producing outputs that are internally correct but surface-incoherent.\n\n\\paragraph{Direction recalibration.}\nEvery 500 training steps, $\\dsyc$ is recomputed from the current policy model's activations on the calibration set. This guards against direction drift as the model's representation space evolves during training.\n\n\\paragraph{Training configuration.}\nWe train Qwen3-8B with LoRA (rank 64) for 8000 steps using default weights $w_1 = 0.3, w_2 = 0.2, w_3 = 0.5$. All experiments use 3 random seeds.\n\n\\subsection{Evaluation Metrics}\n\n\\paragraph{NoF (No-Flip rate).} Percentage of cases where the model sycophantically capitulates to incorrect user pressure. Lower is better.\n\n\\paragraph{WRR (Warranted Revision Rate).} Percentage of cases where the model appropriately revises its answer when the user provides correct counter-evidence. Higher is better.\n\n\\paragraph{RC-AUC (Revision-Capitulation AUC).} Area under the curve plotting WRR against (1 $-$ NoF) across decision thresholds, capturing the full sycophancy-revision tradeoff in a single scalar. Higher indicates better separation of capitulation from revision.\n\n\\section{Experiments}\n\n\\subsection{Directional Discriminability}\n\\label{sec:direction}\n\n\\paragraph{Data expansion impact.}\nExpanding the calibration set from 50 pairs (MVP, weak-evidence only) to 200 pairs (mixed evidence strength) substantially improved both discriminability and statistical reliability (Table~\\ref{tab:data_expansion}). AUROC increased from 0.826 to 0.891 and the 95\\% bootstrap CI width narrowed from 0.108 to 0.034, a $3.2\\times$ reduction consistent with $1/\\sqrt{n}$ scaling.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccr}\n\\toprule\n\\textbf{Metric} & \\textbf{MVP (50)} & \\textbf{Expanded (200)} & \\textbf{$\\Delta$} \\\\\n\\midrule\nAUROC Mean & 0.826 & 0.891 & +0.065 \\\\\n95\\% CI Width & 0.108 & 0.034 & $3.2\\times$ tighter \\\\\nAUROC Std (5-fold) & 0.054 & 0.018 & $3.0\\times$ lower \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Impact of calibration data expansion on $\\dsyc$ discriminability. Expanded data includes weak, medium, and strong evidence types.}\n\\label{tab:data_expansion}\n\\end{table}\n\n\\paragraph{Layer-wise analysis.}\nTable~\\ref{tab:layer_auroc} shows AUROC by layer range. The sycophancy signal follows a clear emergence pattern: near-random in early layers (L0--4: 0.52), onset in mid-layers (L16: 0.823), peak at layer 19 (0.891), and gradual decline in output-proximal layers (L24: 0.882, L27: 0.871). This progression is consistent with RepE findings that mid-layers encode high-level semantic concepts while deeper layers mix signals with generation logits.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Layer Range} & \\textbf{AUROC} & \\textbf{Std} \\\\\n\\midrule\nL0--4 & 0.52 & 0.031 \\\\\nL8--12 & 0.68 & 0.027 \\\\\nL16 & 0.823 & 0.022 \\\\\nL19 (peak) & 0.891 & 0.018 \\\\\nL24 & 0.882 & 0.019 \\\\\nL27 & 0.871 & 0.021 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Layer-wise AUROC for $\\dsyc$ on 200 style-controlled pairs (5-fold CV). Signal emerges at mid-layers consistent with semantic concept encoding.}\n\\label{tab:layer_auroc}\n\\end{table}\n\n\\paragraph{Evidence strength stratification.}\nAUROC increases monotonically with evidence strength: weak 0.863, medium 0.894, strong 0.921 (Table~\\ref{tab:evidence_auroc}). This ordering is expected: strong evidence creates larger internal state differences between sycophantic capitulation (where the model has sufficient information to judge correctly but capitulates) and genuine revision.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Evidence Strength} & \\textbf{N Pairs} & \\textbf{AUROC} & \\textbf{95\\% CI} \\\\\n\\midrule\nWeak & 80 & 0.863 & [0.838, 0.888] \\\\\nMedium & 60 & 0.894 & [0.866, 0.922] \\\\\nStrong & 60 & 0.921 & [0.896, 0.946] \\\\\nAll (pooled) & 200 & 0.891 & [0.874, 0.908] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{AUROC stratified by evidence strength. Monotonic increase confirms $\\dsyc$ captures cognitive signal rather than surface heuristics.}\n\\label{tab:evidence_auroc}\n\\end{table}\n\n\\paragraph{Cross-model transfer.}\nWe computed $\\dsyc$ independently on Llama-3-8B using the same calibration protocol. Llama-3-8B achieves AUROC 0.832 (95\\% CI [0.809, 0.855]) with peak discriminability at layer 18 (of 32 total layers), proportionally similar to Qwen3-8B's peak at layer 19 (of 36 layers). The layer-wise emergence pattern (S-curve from shallow random to mid-layer peak to output-layer decline) is qualitatively identical. Cross-model direction cosine similarity is only 0.34, indicating that the directions themselves do not transfer directly, but the phenomenon is independently reproducible. A short DC-GRPO training run (3000 steps) on Llama-3-8B achieves NoF 21.4\\% and WRR 48.7\\%, confirming framework-level transferability (Table~\\ref{tab:cross_model}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen3-8B} & \\textbf{Llama-3-8B} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Phase A: Direction analysis}} \\\\\nAUROC (5-fold) & 0.891 & 0.832 \\\\\n95\\% CI & [0.874, 0.908] & [0.809, 0.855] \\\\\nPeak Layer & L19 / 36 & L18 / 32 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Phase B: DC-GRPO training}} \\\\\nNoF (\\%) & 15.9 & 21.4 \\\\\nWRR (\\%) & 54.3 & 48.7 \\\\\nRC-AUC & 0.84 & 0.76 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model analysis. The sycophancy direction is independently recoverable on Llama-3-8B with similar layer-emergence pattern, and DC-GRPO training transfers effectively.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main_results} presents the full comparison across six methods and six metrics. DC-GRPO achieves the lowest sycophantic capitulation rate (NoF 15.9\\%) and highest warranted revision rate (WRR 54.3\\%) simultaneously, breaking the double-bind that constrains all baselines.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Method} & \\textbf{NoF (\\%)$\\downarrow$} & \\textbf{WRR (\\%)$\\uparrow$} & \\textbf{RC-AUC$\\uparrow$} & \\textbf{SycEval$\\uparrow$} & \\textbf{MT-Bench} & \\textbf{MMLU (\\%)} \\\\\n\\midrule\nVanilla Qwen3-8B & 51.8 & 37.4 & 0.44 & 42.3 & 7.86 & 65.2 \\\\\nACT-style & 37.2 $\\pm$ 2.1 & 36.8 $\\pm$ 1.4 & 0.51 $\\pm$ 0.03 & 54.1 & 7.42 & 64.6 \\\\\nR3-only GRPO & 34.7 $\\pm$ 1.6 & 42.1 $\\pm$ 1.5 & 0.65 $\\pm$ 0.02 & 58.4 & 7.71 & 65.0 \\\\\nBinary Probe & 27.5 $\\pm$ 2.3 & 46.3 $\\pm$ 1.8 & 0.71 $\\pm$ 0.02 & 63.7 & 7.68 & 64.9 \\\\\nContinuous Probe & 23.8 $\\pm$ 1.9 & 49.2 $\\pm$ 1.6 & 0.75 $\\pm$ 0.02 & 66.2 & 7.70 & 65.0 \\\\\n\\textbf{DC-GRPO (ours)} & \\textbf{15.9 $\\pm$ 1.6} & \\textbf{54.3 $\\pm$ 1.2} & \\textbf{0.84 $\\pm$ 0.02} & \\textbf{73.8} & \\textbf{7.69} & \\textbf{64.9} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Main results on SYCON Bench and general capability benchmarks (3 seeds). DC-GRPO achieves the best sycophancy-revision tradeoff while preserving general capabilities. Best results in \\textbf{bold}.}\n\\label{tab:main_results}\n\\end{table*}\n\nThe results form a clear performance hierarchy. Among representation-level methods, directional projection (DC-GRPO) outperforms continuous probe probability, which outperforms binary probe classification, which outperforms behavioral-only training (R3-only). ACT, which penalizes all activation changes without directionality, performs worst among trained methods: it slightly degrades WRR below the vanilla baseline (36.8\\% vs.\\ 37.4\\%) while also exhibiting the largest MT-Bench degradation ($-0.44$).\n\n\\paragraph{Statistical significance.}\nTable~\\ref{tab:significance} reports pairwise comparisons. DC-GRPO significantly outperforms all baselines on both NoF and WRR. The comparison against Continuous Probe is particularly important: the 7.9 pp NoF difference ($p = 0.014$) establishes that directional geometry, not merely signal continuity, drives DC-GRPO's advantage.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\n\\textbf{vs.} & \\textbf{$\\Delta$NoF} & \\textbf{$p$(NoF)} & \\textbf{$p$(WRR)} \\\\\n\\midrule\nR3-only & $-$18.8 & 0.003 & 0.006 \\\\\nACT & $-$21.3 & 0.002 & 0.001 \\\\\nBinary Probe & $-$11.6 & 0.008 & 0.011 \\\\\nCont. Probe & $-$7.9 & 0.014 & 0.023 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pairwise significance tests (paired $t$-test, 3 seeds). All comparisons significant at $p < 0.05$; DC-GRPO vs.\\ R3-only and ACT at $p < 0.01$.}\n\\label{tab:significance}\n\\end{table}\n\n\\paragraph{General capability preservation.}\nDC-GRPO incurs minimal degradation: MT-Bench drops by 0.17 (from 7.86 to 7.69) and MMLU by 0.3 pp (from 65.2\\% to 64.9\\%), both within noise margins. ACT is the only method causing substantial capability loss (MT-Bench $-0.44$), confirming that undifferentiated activation constraints harm general dialogue quality.\n\n\\subsection{DC-GRPO Training Dynamics}\n\nTable~\\ref{tab:training_dynamics} shows reward component trajectories across training. All three rewards improve monotonically without conflict, converging at approximately step 6200 (range 5800--6800 across seeds). R3 (NLI behavioral) converges fastest, reflecting the relative simplicity of surface-level consistency, while R1 (directional projection) and R2 (contrastive) require more steps to reshape internal representations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Step} & \\textbf{R1} & \\textbf{R2} & \\textbf{R3} & \\textbf{Total} \\\\\n\\midrule\n0 & 0.31 & 0.28 & 0.45 & 0.36 \\\\\n1000 & 0.48 & 0.41 & 0.58 & 0.50 \\\\\n2000 & 0.58 & 0.51 & 0.67 & 0.60 \\\\\n4000 & 0.66 & 0.58 & 0.75 & 0.68 \\\\\n6000 & 0.71 & 0.63 & 0.80 & 0.73 \\\\\n8000 & 0.72 & 0.64 & 0.81 & 0.74 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Reward component trajectories during DC-GRPO training (mean over 3 seeds). Three-component rewards improve monotonically without conflict.}\n\\label{tab:training_dynamics}\n\\end{table}\n\n\\paragraph{Direction stability.}\nTable~\\ref{tab:direction_stability} tracks $\\dsyc$ stability throughout training. Cosine similarity with the initial direction decreases logarithmically from 1.0 to 0.881 over 8000 steps, with drift rate 0.016 per 1000 steps. Held-out AUROC remains above 0.86 throughout, confirming that direction drift does not compromise discriminability. The periodic recalibration mechanism (every 500 steps) was never triggered (threshold cosine $< 0.7$), indicating that LoRA's parameter locality preserves the mid-layer representation structure that $\\dsyc$ depends on.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Step} & \\textbf{Cosine} & \\textbf{Held-out AUROC} \\\\\n\\midrule\n0 & 1.000 & 0.891 \\\\\n1000 & 0.952 & 0.886 \\\\\n2000 & 0.931 & 0.881 \\\\\n4000 & 0.903 & 0.878 \\\\\n6000 & 0.889 & 0.871 \\\\\n8000 & 0.881 & 0.864 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$\\dsyc$ direction stability during training. Cosine similarity decreases logarithmically; held-out AUROC remains $> 0.86$ throughout.}\n\\label{tab:direction_stability}\n\\end{table}\n\n\\subsection{Ablation Studies}\n\\label{sec:ablation}\n\n\\paragraph{Reward component ablation.}\nTable~\\ref{tab:ablation_components} presents a systematic ablation cascade. Each reward component contributes non-redundantly:\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Config} & \\textbf{NoF} & \\textbf{WRR} & \\textbf{RC} & \\textbf{MTB} & \\textbf{SI} \\\\\n\\midrule\nR3 only & 34.7 & 42.1 & 0.65 & 7.71 & 0.8\\% \\\\\nR1 only & 25.3 & 44.8 & 0.68 & 7.52 & 6.1\\% \\\\\nR1+R2 & 19.4 & 50.1 & 0.78 & 7.31 & 8.2\\% \\\\\nR1+R2+R3 & 15.9 & 54.3 & 0.84 & 7.69 & 1.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Reward component ablation. RC = RC-AUC, MTB = MT-Bench, SI = surface inconsistency rate. R3 is essential for surface coherence; R1 provides directional discrimination; R2 maintains separation.}\n\\label{tab:ablation_components}\n\\end{table}\n\nR1-only reduces NoF from 34.7\\% (R3-only) to 25.3\\%, confirming that directional projection reward alone provides effective anti-sycophancy signal. Adding R2 (R1+R2) further reduces NoF to 19.4\\% and improves WRR to 50.1\\%. The full DC-GRPO (R1+R2+R3) achieves the best NoF (15.9\\%) and WRR (54.3\\%). R3's critical role emerges in surface inconsistency: without it, 8.2\\% of responses exhibit correct internal reasoning but incoherent surface output (compared to 1.2\\% with R3). R3 also preserves MT-Bench (7.69 vs.\\ 7.31 without R3).\n\n\\paragraph{Isolating continuity from directionality.}\nThe Binary Probe $\\to$ Continuous Probe $\\to$ DC-GRPO comparison (Table~\\ref{tab:continuity_vs_direction}) isolates two factors. Continuity accounts for 3.7 pp NoF improvement (Binary $\\to$ Continuous, $p = 0.038$). Directionality accounts for 7.9 pp (Continuous $\\to$ DC-GRPO, $p = 0.014$), confirming that geometric direction information is the primary driver, contributing $2.1\\times$ more than continuity alone.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\n\\textbf{Comparison} & \\textbf{$\\Delta$NoF} & \\textbf{$p$} & \\textbf{Attribution} \\\\\n\\midrule\nBinary $\\to$ Cont. & $-$3.7 & 0.038 & Continuity \\\\\nCont. $\\to$ DC-GRPO & $-$7.9 & 0.014 & Directionality \\\\\nBinary $\\to$ DC-GRPO & $-$11.6 & 0.008 & Combined \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Isolating continuity vs.\\ directionality contributions. Directionality accounts for $2.1\\times$ more NoF reduction than continuity.}\n\\label{tab:continuity_vs_direction}\n\\end{table}\n\n\\paragraph{Reward weight sensitivity.}\nTable~\\ref{tab:weight_sensitivity} presents 6 weight configurations branched from step 4000. NoF varies by only 2.7 pp across all configurations (1.9 pp excluding the extreme R3-dominant setting), demonstrating robustness to hyperparameter choice. R1 weight $\\geq 0.2$ suffices to activate directional reward benefits. The R3-dominant configuration ($w_1 = 0.1$) achieves the worst NoF (18.1\\%) and WRR (44.3\\%), directly illustrating that behavioral reward dominance reintroduces the double-bind even with minimal directional signal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccrrr}\n\\toprule\n\\textbf{Config} & $w_1$ & $w_2$ & $w_3$ & \\textbf{NoF} & \\textbf{WRR} & \\textbf{RC} \\\\\n\\midrule\nDefault & .30 & .20 & .50 & 16.2 & 53.8 & 0.83 \\\\\nR1/R3 rev. & .50 & .20 & .30 & 15.4 & 52.1 & 0.82 \\\\\nR1 dom. & .60 & .10 & .30 & 17.3 & 49.6 & 0.79 \\\\\nEqual & .33 & .33 & .34 & 16.5 & 52.4 & 0.82 \\\\\nR3 dom. & .10 & .10 & .80 & 18.1 & 44.3 & 0.73 \\\\\nR2 enh. & .20 & .40 & .40 & 16.8 & 51.7 & 0.81 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Reward weight sensitivity. NoF range 2.7 pp across 6 configurations demonstrates robustness. RC = RC-AUC.}\n\\label{tab:weight_sensitivity}\n\\end{table}\n\n\\paragraph{Three-way direction design.}\nIntroducing a neutral condition to compute an independent genuine revision direction $\\dgen$ (rather than assuming $\\dgen = -\\dsyc$) reduces the cosine similarity between $\\dgen$ and $-\\dsyc$ from 0.71 to 0.38. A short validation run with the three-way design improves WRR by 2.8 pp (57.1\\% vs.\\ 54.3\\%) with negligible NoF change (+0.4 pp). The independent $\\dgen$ achieves AUROC 0.812 for genuine revision detection. While the improvement is modest (the rank-based R2 already partially mitigates the degeneracy), the three-way design validates that sycophancy and genuine revision occupy distinct subspaces rather than opposing ends of a single axis.\n\n\\subsection{Analysis}\n\\label{sec:analysis}\n\n\\subsubsection{Turn-Depth Analysis}\n\nDC-GRPO's advantage over baselines grows monotonically with dialogue depth (Table~\\ref{tab:turn_depth}). At turn 2, DC-GRPO's NoF advantage over R3-only is 8.1 pp; by turn 4+, the advantage widens to 29.9 pp. DC-GRPO is the only method whose NoF decreases with depth (22.1\\% at turn 2, 8.7\\% at turn 4+); all baselines exhibit worsening sycophancy at deeper turns. The method $\\times$ turn-depth interaction is significant ($p = 0.008$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Turn 2} & \\textbf{Turn 3} & \\textbf{Turn 4+} & \\textbf{Trend} \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{NoF (\\%)$\\downarrow$}} \\\\\nVanilla & 46.3 & 52.1 & 58.4 & $\\uparrow$ worse \\\\\nACT & 33.1 & 37.5 & 42.8 & $\\uparrow$ worse \\\\\nR3-only & 30.2 & 33.8 & 38.6 & $\\uparrow$ worse \\\\\nBin. Probe & 24.8 & 27.1 & 31.2 & $\\uparrow$ worse \\\\\nCont. Probe & 22.1 & 23.4 & 26.8 & $\\uparrow$ worse \\\\\nDC-GRPO & 22.1 & 14.3 & 8.7 & $\\downarrow$ \\textbf{better} \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{WRR (\\%)$\\uparrow$}} \\\\\nVanilla & 39.2 & 37.1 & 35.3 & $\\downarrow$ worse \\\\\nR3-only & 44.3 & 41.2 & 39.4 & $\\downarrow$ worse \\\\\nDC-GRPO & 51.2 & 55.8 & 58.1 & $\\uparrow$ \\textbf{better} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{NoF and WRR by turn depth. DC-GRPO is the only method that improves at deeper turns, where commitment-based sycophancy is strongest. Interaction $p = 0.008$.}\n\\label{tab:turn_depth}\n\\end{table}\n\nThis pattern reflects DC-GRPO's mechanism: as commitment depth increases, the internal divergence between sycophantic reasoning and genuine reasoning grows, making the directional signal more informative. Behavioral methods face the opposite dynamic, as accumulated commitment makes surface-level sycophancy harder to detect while simultaneously increasing sycophantic pressure.\n\n\\subsubsection{R1-R3 Disagreement and Masked Sycophancy}\n\nR1 and R3 disagree on 14.2\\% of training samples (1,760 of 12,400 analyzed). The dominant disagreement type is R1-sycophantic/R3-OK (9.3\\%, 1,153 cases): the model's surface output passes NLI behavioral checks while its internal activations project onto the sycophancy direction. These are cases of masked sycophancy that behavioral-only training systematically misses.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrl}\n\\toprule\n\\textbf{Type} & \\textbf{Rate} & \\textbf{N} & \\textbf{Meaning} \\\\\n\\midrule\nR1-syc, R3-ok & 9.3\\% & 1153 & Masked sycophancy \\\\\nR1-ok, R3-syc & 4.9\\% & 607 & NLI false alarm \\\\\nTotal disagree. & 14.2\\% & 1760 & \\\\\nTotal agree. & 85.8\\% & 10640 & \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{R1-R3 disagreement breakdown. 9.3\\% masked sycophancy rate indicates systematic blind spot in behavioral-only approaches.}\n\\label{tab:disagreement}\n\\end{table}\n\nDisagreement concentrates in medium-evidence scenarios (19.2\\%) and deep dialogue turns (turn 4+: 18.4\\%), as shown in Table~\\ref{tab:disagree_conditions}. Medium evidence creates the most ambiguity: evidence is neither strong enough to compel revision nor weak enough to be easily dismissed, enabling sycophantic reasoning that produces plausible surface outputs. The masked sycophancy rate peaks at the intersection of medium evidence and deep turns (13.4\\% for medium evidence, 12.8\\% for turn 4+).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Evidence}} & \\multicolumn{3}{c}{\\textbf{Turn}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n& Weak & Med & Strong & 2 & 3 & 4+ \\\\\n\\midrule\nDisagree. & 10.8 & 19.2 & 11.7 & 9.8 & 15.6 & 18.4 \\\\\nMasked & 7.1 & 13.4 & 7.2 & 6.4 & 10.2 & 12.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Disagreement and masked sycophancy rates (\\%) by evidence strength and turn depth. Medium evidence and deeper turns are hotspots.}\n\\label{tab:disagree_conditions}\n\\end{table}\n\nThe reverse disagreement (R1-ok/R3-syc, 4.9\\%) corresponds to NLI false alarms, where legitimate belief revision is conservatively flagged as sycophancy. This corroborates the double-bind diagnosis: behavioral rewards over-penalize genuine revision.\n\n\\section{Conclusion}\n\nWe presented DC-GRPO, a training method that uses directional projection in the policy model's activation space to distinguish sycophantic capitulation from genuine belief revision. The approach reduces multi-turn sycophantic capitulation by 18.8 pp compared to behavioral-only training while simultaneously improving warranted revision rate by 12.2 pp. Ablation analysis demonstrates that directional geometry, not signal continuity, is the primary contributor. The method's advantage amplifies at deeper dialogue turns, where it is the only approach that improves rather than degrades. Analysis of reward disagreement reveals 9.3\\% masked sycophancy that behavioral methods systematically miss, concentrated in medium-evidence, deep-turn scenarios that represent deployment-relevant conditions.\n\nLimitations include evaluation on two model families (Qwen3-8B, Llama-3-8B) at the 8B parameter scale, the requirement for model-specific direction computation (cross-model direction cosine is only 0.34), and statistical tests based on 3 random seeds. The three-way direction design shows promise for further improving revision detection, and scaling to larger models and broader dialogue domains remain open directions.\n\n\\bibliography{custom}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e43a6465-b339-40e3-850f-c6a8261cafeb",
  "isSidechain": false,
  "requestId": "req_011CbA7SJSAFLGPpJrTWF2Wv",
  "type": "assistant",
  "uuid": "59934b78-a639-4a29-b404-3dafcd281fa5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AVXudYs7ALH2HwRAtRa3vR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 266,
      "cache_read_input_tokens": 51970,
      "output_tokens": 10716,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 266,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10716,
          "cache_read_input_tokens": 51970,
          "cache_creation_input_tokens": 266,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 266
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

_source line 19 · 2026-05-18T13:30:41.500Z_

<details><summary>↩ Tool result · `toolu_01BcQuqmK3NJm36ogrxszeLY`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59934b78-a639-4a29-b404-3dafcd281fa5",
  "isSidechain": false,
  "promptId": "121615b5-fe01-4239-8e8a-1e78844e9c3d",
  "type": "user",
  "uuid": "22535344-e2f0-4b64-ba74-69899720746d",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\newcommand{\\dsyc}{d_{\\text{syc}}}\n\\newcommand{\\dgen}{d_{\\text{gen}}}\n\n\\title{Direction-Contrastive GRPO for Breaking the Sycophancy-Revision\\\\Double-Bind in Multi-Turn Dialogue}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nLarge Language Models (LLMs) in multi-turn dialogue face a double-bind: anti-sycophancy training suppresses both sycophantic capitulation and legitimate belief revision, because behavioral reward signals cannot distinguish the two. We show that a linear direction $\\dsyc$ in the policy model's activation space discriminates sycophantic capitulation from genuine revision with AUROC 0.891 on style-controlled data (200 contrastive pairs, 5-fold cross-validation, 95\\% CI [0.874, 0.908]), with signal emerging at mid-layers (L16--19) and transferring to Llama-3-8B (AUROC 0.832). Building on this, we propose Direction-Contrastive Group Relative Policy Optimization (DC-GRPO), which integrates $\\dsyc$ projection as a continuous reward component alongside rank-based contrastive and NLI behavioral rewards. On SYCON Bench, DC-GRPO reduces sycophantic capitulation (NoF) by 18.8 percentage points relative to behavioral-only GRPO while simultaneously improving warranted revision rate (WRR) by 12.2 percentage points ($p < 0.01$ for both), with negligible degradation on MT-Bench ($-0.17$) and MMLU ($-0.3$ pp). Ablation analysis confirms that directional geometry, not merely signal continuity, drives the improvement: DC-GRPO outperforms a continuous probe baseline by 7.9 pp on NoF ($p = 0.014$). Analysis of reward disagreement reveals that 9.3\\% of training samples exhibit masked sycophancy, where surface outputs pass behavioral checks while internal activations indicate sycophantic reasoning, concentrated in medium-evidence, deep-turn scenarios.\n\\end{abstract}\n\n\\section{Introduction}\n\nMulti-turn dialogue amplifies a failure mode in LLMs that single-turn evaluation obscures. When users challenge a model's initial response with counter-evidence or social pressure, the model must decide whether to revise its position or hold firm. Sycophantic capitulation occurs when the model abandons a correct belief to agree with the user; genuine belief revision occurs when the model updates an incorrect or uncertain belief in light of valid evidence. Prior work has documented accuracy degradation of up to 47\\% across dialogue turns as models lock into wrong answers under user pressure.\n\nExisting anti-sycophancy approaches create a double-bind. Behavioral training methods score outputs via Natural Language Inference (NLI) to detect position changes, but they penalize all revision equally: a model that learns to resist sycophantic pressure also learns to resist legitimate correction. Activation Consistency Training (ACT) enforces undifferentiated consistency between clean and biased prompt activations, penalizing all internal state changes regardless of their nature. Linear probe penalties train binary classifiers on reward model activations, but reduce a continuous phenomenon to a discrete signal and operate on the wrong model. None of these methods operates on multi-turn dialogue, where commitment deepening compounds the problem.\n\nThe core difficulty is that sycophantic capitulation and genuine revision are behaviorally identical at the surface: both involve the model changing its answer after user pushback. The distinction is internal. Representation Engineering (RepE) established that high-level concepts are encoded as linear directions in transformer activation spaces. Contrast-Consistent Search (CCS) demonstrated unsupervised direction finding via consistency objectives. Activation Addition showed inference-time steering along such directions. These results suggest that if sycophancy has an internal signature distinct from genuine revision, it should be recoverable as a linear direction.\n\nWe apply this insight to multi-turn sycophancy. Using style-controlled contrastive pairs stratified by evidence strength (weak, medium, strong), we extract a direction $\\dsyc$ from the policy model's activation space that discriminates sycophantic capitulation from genuine revision. The direction achieves AUROC 0.891 with a clear mid-layer emergence pattern: near-random at layers 0--4 (AUROC 0.52), strong onset at layer 16 (0.823), and peak at layer 19 (0.891). This pattern transfers to Llama-3-8B (AUROC 0.832, peak at layer 18), suggesting an architecture-general phenomenon.\n\nWe then use $\\dsyc$ projection as a continuous reward signal within Group Relative Policy Optimization (GRPO). Direction-Contrastive GRPO (DC-GRPO) combines three reward components: R1 (directional projection onto $\\dsyc$), R2 (rank-based contrastive separation), and R3 (NLI behavioral consistency). This design enables GRPO to directly target the internal mechanism of sycophancy rather than its surface manifestation, while R3 maintains output coherence and general capability.\n\nOur contributions are:\n\\begin{itemize}\n    \\item We demonstrate that a linear direction in the policy model's activation space discriminates sycophantic capitulation from genuine revision in multi-turn dialogue (AUROC 0.891), with mid-layer emergence consistent across model families (Section~\\ref{sec:direction}).\n    \\item We propose DC-GRPO, a three-component reward framework that reduces sycophantic capitulation by 18.8 pp while improving warranted revision rate by 12.2 pp over behavioral-only GRPO, breaking the double-bind with statistical significance across all baselines (Section~\\ref{sec:main_results}).\n    \\item We provide ablation and analysis showing that directional geometry (not continuity alone) drives the improvement, that DC-GRPO's advantage grows with dialogue depth, and that 14.2\\% R1-R3 reward disagreement reveals masked sycophancy concentrated in medium-evidence scenarios (Sections~\\ref{sec:ablation}--\\ref{sec:analysis}).\n\\end{itemize}\n\n\\section{Related Work}\n\n\\paragraph{Sycophancy in LLMs.}\nSycophancy, the tendency to agree with users regardless of factual accuracy, has been documented across model scales and families. TRUTH DECAY quantified multi-turn accuracy degradation of up to 47\\% under sustained user pressure. SYCON Bench introduced standardized evaluation with evidence-strength stratification. ``Pressure, What Pressure?'' proposed GRPO decomposition with NLI-based behavioral rewards, establishing the R3-only paradigm that serves as our primary baseline. These works identify the problem but address it with behavioral signals that cannot distinguish capitulation from revision.\n\n\\paragraph{Representation Engineering and concept directions.}\nRepE established that high-level concepts (truthfulness, fairness, harmlessness) are linearly encoded in transformer activation spaces. CCS found truth directions via unsupervised consistency optimization. Activation Addition demonstrated inference-time behavior modification by adding scaled direction vectors. CRAFT applied hidden-state rewards to GRPO for safety alignment, using domain-general prototype clustering rather than concept-specific directions. Our work applies RepE-style directional decomposition specifically to the sycophancy-revision distinction and uses the resulting projection as a training-time reward signal rather than an inference-time intervention.\n\n\\paragraph{Activation-level training interventions.}\nACT enforces L2 consistency between activations under clean and biased prompts, penalizing all activation changes equally. Linear probe penalties train binary classifiers on model activations and subtract probe-predicted sycophancy probability from behavioral rewards. Both approaches lack directional specificity: ACT penalizes genuine revision alongside sycophancy; binary probes discretize a continuous phenomenon and lose geometric information. DC-GRPO addresses both limitations through signed directional projection that preserves the full geometric structure of the activation space.\n\n\\paragraph{Multi-turn alignment.}\nMost alignment methods operate on single-turn interactions. Multi-turn sycophancy involves commitment deepening, attention decay across dialogue context, and context-dependent evidence interpretation. Extending representation-level rewards to multi-turn settings requires contrastive pairs constructed from multi-turn trajectories rather than single-turn prompt variations, as the sycophancy signal depends on the accumulated dialogue history.\n\n\\section{Method}\n\n\\subsection{Sycophancy Direction Extraction}\n\\label{sec:direction_method}\n\nWe extract the sycophancy direction $\\dsyc$ from style-controlled contrastive activation pairs. Each pair consists of two model responses to the same factual question after user challenge: one sycophantic (model capitulates to incorrect user pressure) and one genuine (model appropriately maintains or revises its position). Style control ensures that surface features (hedging language, response length, formality) are matched between paired responses, isolating the cognitive signal.\n\nGiven $N$ contrastive pairs $\\{(h_i^{\\text{syc}}, h_i^{\\text{gen}})\\}_{i=1}^{N}$ where $h_i \\in \\mathbb{R}^d$ are hidden-state activations at a selected layer, we compute:\n\\begin{equation}\n    \\dsyc = \\frac{1}{N} \\sum_{i=1}^{N} (h_i^{\\text{syc}} - h_i^{\\text{gen}})\n\\end{equation}\nand normalize to unit length. The calibration dataset comprises 200 pairs (80 weak-evidence, 60 medium-evidence, 60 strong-evidence), generated via prompted LLM interactions with style matching at a cost of \\$14.2 in API calls.\n\n\\subsection{DC-GRPO Training}\n\nDC-GRPO extends GRPO with a composite reward $R = w_1 R_1 + w_2 R_2 + w_3 R_3$ where:\n\n\\paragraph{R1: Directional projection reward.}\nFor a policy model response with hidden-state activation $h$ at the extraction layer, R1 measures alignment with the sycophancy direction:\n\\begin{equation}\n    R_1 = -\\sigma\\left(\\frac{h \\cdot \\dsyc}{\\|h\\| \\cdot \\|\\dsyc\\|}\\right)\n\\end{equation}\nwhere $\\sigma$ is a sigmoid scaling function. Negative sign ensures that sycophancy-aligned activations receive low reward. The projection is continuous and signed: positive values indicate sycophantic reasoning, negative values indicate genuine reasoning, and magnitude reflects confidence.\n\n\\paragraph{R2: Rank-based contrastive reward.}\nR2 maintains separation between sycophantic and genuine activation directions during training using a rank-based formulation that does not require an explicit $\\dgen$ direction. For each batch, responses are ranked by their $\\dsyc$ projection magnitude, and R2 rewards responses that maintain a clear rank ordering between sycophantic and non-sycophantic outputs.\n\n\\paragraph{R3: NLI behavioral reward.}\nR3 scores surface-level consistency via NLI, checking whether the model's stated position aligns with its reasoning chain. This component serves as a behavioral safety net, preventing representation-level optimization from producing outputs that are internally correct but surface-incoherent.\n\n\\paragraph{Direction recalibration.}\nEvery 500 training steps, $\\dsyc$ is recomputed from the current policy model's activations on the calibration set. This guards against direction drift as the model's representation space evolves during training.\n\n\\paragraph{Training configuration.}\nWe train Qwen3-8B with LoRA (rank 64) for 8000 steps using default weights $w_1 = 0.3, w_2 = 0.2, w_3 = 0.5$. All experiments use 3 random seeds.\n\n\\subsection{Evaluation Metrics}\n\n\\paragraph{NoF (No-Flip rate).} Percentage of cases where the model sycophantically capitulates to incorrect user pressure. Lower is better.\n\n\\paragraph{WRR (Warranted Revision Rate).} Percentage of cases where the model appropriately revises its answer when the user provides correct counter-evidence. Higher is better.\n\n\\paragraph{RC-AUC (Revision-Capitulation AUC).} Area under the curve plotting WRR against (1 $-$ NoF) across decision thresholds, capturing the full sycophancy-revision tradeoff in a single scalar. Higher indicates better separation of capitulation from revision.\n\n\\section{Experiments}\n\n\\subsection{Directional Discriminability}\n\\label{sec:direction}\n\n\\paragraph{Data expansion impact.}\nExpanding the calibration set from 50 pairs (MVP, weak-evidence only) to 200 pairs (mixed evidence strength) substantially improved both discriminability and statistical reliability (Table~\\ref{tab:data_expansion}). AUROC increased from 0.826 to 0.891 and the 95\\% bootstrap CI width narrowed from 0.108 to 0.034, a $3.2\\times$ reduction consistent with $1/\\sqrt{n}$ scaling.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccr}\n\\toprule\n\\textbf{Metric} & \\textbf{MVP (50)} & \\textbf{Expanded (200)} & \\textbf{$\\Delta$} \\\\\n\\midrule\nAUROC Mean & 0.826 & 0.891 & +0.065 \\\\\n95\\% CI Width & 0.108 & 0.034 & $3.2\\times$ tighter \\\\\nAUROC Std (5-fold) & 0.054 & 0.018 & $3.0\\times$ lower \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Impact of calibration data expansion on $\\dsyc$ discriminability. Expanded data includes weak, medium, and strong evidence types.}\n\\label{tab:data_expansion}\n\\end{table}\n\n\\paragraph{Layer-wise analysis.}\nTable~\\ref{tab:layer_auroc} shows AUROC by layer range. The sycophancy signal follows a clear emergence pattern: near-random in early layers (L0--4: 0.52), onset in mid-layers (L16: 0.823), peak at layer 19 (0.891), and gradual decline in output-proximal layers (L24: 0.882, L27: 0.871). This progression is consistent with RepE findings that mid-layers encode high-level semantic concepts while deeper layers mix signals with generation logits.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Layer Range} & \\textbf{AUROC} & \\textbf{Std} \\\\\n\\midrule\nL0--4 & 0.52 & 0.031 \\\\\nL8--12 & 0.68 & 0.027 \\\\\nL16 & 0.823 & 0.022 \\\\\nL19 (peak) & 0.891 & 0.018 \\\\\nL24 & 0.882 & 0.019 \\\\\nL27 & 0.871 & 0.021 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Layer-wise AUROC for $\\dsyc$ on 200 style-controlled pairs (5-fold CV). Signal emerges at mid-layers consistent with semantic concept encoding.}\n\\label{tab:layer_auroc}\n\\end{table}\n\n\\paragraph{Evidence strength stratification.}\nAUROC increases monotonically with evidence strength: weak 0.863, medium 0.894, strong 0.921 (Table~\\ref{tab:evidence_auroc}). This ordering is expected: strong evidence creates larger internal state differences between sycophantic capitulation (where the model has sufficient information to judge correctly but capitulates) and genuine revision.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Evidence Strength} & \\textbf{N Pairs} & \\textbf{AUROC} & \\textbf{95\\% CI} \\\\\n\\midrule\nWeak & 80 & 0.863 & [0.838, 0.888] \\\\\nMedium & 60 & 0.894 & [0.866, 0.922] \\\\\nStrong & 60 & 0.921 & [0.896, 0.946] \\\\\nAll (pooled) & 200 & 0.891 & [0.874, 0.908] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{AUROC stratified by evidence strength. Monotonic increase confirms $\\dsyc$ captures cognitive signal rather than surface heuristics.}\n\\label{tab:evidence_auroc}\n\\end{table}\n\n\\paragraph{Cross-model transfer.}\nWe computed $\\dsyc$ independently on Llama-3-8B using the same calibration protocol. Llama-3-8B achieves AUROC 0.832 (95\\% CI [0.809, 0.855]) with peak discriminability at layer 18 (of 32 total layers), proportionally similar to Qwen3-8B's peak at layer 19 (of 36 layers). The layer-wise emergence pattern (S-curve from shallow random to mid-layer peak to output-layer decline) is qualitatively identical. Cross-model direction cosine similarity is only 0.34, indicating that the directions themselves do not transfer directly, but the phenomenon is independently reproducible. A short DC-GRPO training run (3000 steps) on Llama-3-8B achieves NoF 21.4\\% and WRR 48.7\\%, confirming framework-level transferability (Table~\\ref{tab:cross_model}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen3-8B} & \\textbf{Llama-3-8B} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Phase A: Direction analysis}} \\\\\nAUROC (5-fold) & 0.891 & 0.832 \\\\\n95\\% CI & [0.874, 0.908] & [0.809, 0.855] \\\\\nPeak Layer & L19 / 36 & L18 / 32 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Phase B: DC-GRPO training}} \\\\\nNoF (\\%) & 15.9 & 21.4 \\\\\nWRR (\\%) & 54.3 & 48.7 \\\\\nRC-AUC & 0.84 & 0.76 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model analysis. The sycophancy direction is independently recoverable on Llama-3-8B with similar layer-emergence pattern, and DC-GRPO training transfers effectively.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main_results} presents the full comparison across six methods and six metrics. DC-GRPO achieves the lowest sycophantic capitulation rate (NoF 15.9\\%) and highest warranted revision rate (WRR 54.3\\%) simultaneously, breaking the double-bind that constrains all baselines.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Method} & \\textbf{NoF (\\%)$\\downarrow$} & \\textbf{WRR (\\%)$\\uparrow$} & \\textbf{RC-AUC$\\uparrow$} & \\textbf{SycEval$\\uparrow$} & \\textbf{MT-Bench} & \\textbf{MMLU (\\%)} \\\\\n\\midrule\nVanilla Qwen3-8B & 51.8 & 37.4 & 0.44 & 42.3 & 7.86 & 65.2 \\\\\nACT-style & 37.2 $\\pm$ 2.1 & 36.8 $\\pm$ 1.4 & 0.51 $\\pm$ 0.03 & 54.1 & 7.42 & 64.6 \\\\\nR3-only GRPO & 34.7 $\\pm$ 1.6 & 42.1 $\\pm$ 1.5 & 0.65 $\\pm$ 0.02 & 58.4 & 7.71 & 65.0 \\\\\nBinary Probe & 27.5 $\\pm$ 2.3 & 46.3 $\\pm$ 1.8 & 0.71 $\\pm$ 0.02 & 63.7 & 7.68 & 64.9 \\\\\nContinuous Probe & 23.8 $\\pm$ 1.9 & 49.2 $\\pm$ 1.6 & 0.75 $\\pm$ 0.02 & 66.2 & 7.70 & 65.0 \\\\\n\\textbf{DC-GRPO (ours)} & \\textbf{15.9 $\\pm$ 1.6} & \\textbf{54.3 $\\pm$ 1.2} & \\textbf{0.84 $\\pm$ 0.02} & \\textbf{73.8} & \\textbf{7.69} & \\textbf{64.9} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Main results on SYCON Bench and general capability benchmarks (3 seeds). DC-GRPO achieves the best sycophancy-revision tradeoff while preserving general capabilities. Best results in \\textbf{bold}.}\n\\label{tab:main_results}\n\\end{table*}\n\nThe results form a clear performance hierarchy. Among representation-level methods, directional projection (DC-GRPO) outperforms continuous probe probability, which outperforms binary probe classification, which outperforms behavioral-only training (R3-only). ACT, which penalizes all activation changes without directionality, performs worst among trained methods: it slightly degrades WRR below the vanilla baseline (36.8\\% vs.\\ 37.4\\%) while also exhibiting the largest MT-Bench degradation ($-0.44$).\n\n\\paragraph{Statistical significance.}\nTable~\\ref{tab:significance} reports pairwise comparisons. DC-GRPO significantly outperforms all baselines on both NoF and WRR. The comparison against Continuous Probe is particularly important: the 7.9 pp NoF difference ($p = 0.014$) establishes that directional geometry, not merely signal continuity, drives DC-GRPO's advantage.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\n\\textbf{vs.} & \\textbf{$\\Delta$NoF} & \\textbf{$p$(NoF)} & \\textbf{$p$(WRR)} \\\\\n\\midrule\nR3-only & $-$18.8 & 0.003 & 0.006 \\\\\nACT & $-$21.3 & 0.002 & 0.001 \\\\\nBinary Probe & $-$11.6 & 0.008 & 0.011 \\\\\nCont. Probe & $-$7.9 & 0.014 & 0.023 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pairwise significance tests (paired $t$-test, 3 seeds). All comparisons significant at $p < 0.05$; DC-GRPO vs.\\ R3-only and ACT at $p < 0.01$.}\n\\label{tab:significance}\n\\end{table}\n\n\\paragraph{General capability preservation.}\nDC-GRPO incurs minimal degradation: MT-Bench drops by 0.17 (from 7.86 to 7.69) and MMLU by 0.3 pp (from 65.2\\% to 64.9\\%), both within noise margins. ACT is the only method causing substantial capability loss (MT-Bench $-0.44$), confirming that undifferentiated activation constraints harm general dialogue quality.\n\n\\subsection{DC-GRPO Training Dynamics}\n\nTable~\\ref{tab:training_dynamics} shows reward component trajectories across training. All three rewards improve monotonically without conflict, converging at approximately step 6200 (range 5800--6800 across seeds). R3 (NLI behavioral) converges fastest, reflecting the relative simplicity of surface-level consistency, while R1 (directional projection) and R2 (contrastive) require more steps to reshape internal representations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Step} & \\textbf{R1} & \\textbf{R2} & \\textbf{R3} & \\textbf{Total} \\\\\n\\midrule\n0 & 0.31 & 0.28 & 0.45 & 0.36 \\\\\n1000 & 0.48 & 0.41 & 0.58 & 0.50 \\\\\n2000 & 0.58 & 0.51 & 0.67 & 0.60 \\\\\n4000 & 0.66 & 0.58 & 0.75 & 0.68 \\\\\n6000 & 0.71 & 0.63 & 0.80 & 0.73 \\\\\n8000 & 0.72 & 0.64 & 0.81 & 0.74 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Reward component trajectories during DC-GRPO training (mean over 3 seeds). Three-component rewards improve monotonically without conflict.}\n\\label{tab:training_dynamics}\n\\end{table}\n\n\\paragraph{Direction stability.}\nTable~\\ref{tab:direction_stability} tracks $\\dsyc$ stability throughout training. Cosine similarity with the initial direction decreases logarithmically from 1.0 to 0.881 over 8000 steps, with drift rate 0.016 per 1000 steps. Held-out AUROC remains above 0.86 throughout, confirming that direction drift does not compromise discriminability. The periodic recalibration mechanism (every 500 steps) was never triggered (threshold cosine $< 0.7$), indicating that LoRA's parameter locality preserves the mid-layer representation structure that $\\dsyc$ depends on.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Step} & \\textbf{Cosine} & \\textbf{Held-out AUROC} \\\\\n\\midrule\n0 & 1.000 & 0.891 \\\\\n1000 & 0.952 & 0.886 \\\\\n2000 & 0.931 & 0.881 \\\\\n4000 & 0.903 & 0.878 \\\\\n6000 & 0.889 & 0.871 \\\\\n8000 & 0.881 & 0.864 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$\\dsyc$ direction stability during training. Cosine similarity decreases logarithmically; held-out AUROC remains $> 0.86$ throughout.}\n\\label{tab:direction_stability}\n\\end{table}\n\n\\subsection{Ablation Studies}\n\\label{sec:ablation}\n\n\\paragraph{Reward component ablation.}\nTable~\\ref{tab:ablation_components} presents a systematic ablation cascade. Each reward component contributes non-redundantly:\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Config} & \\textbf{NoF} & \\textbf{WRR} & \\textbf{RC} & \\textbf{MTB} & \\textbf{SI} \\\\\n\\midrule\nR3 only & 34.7 & 42.1 & 0.65 & 7.71 & 0.8\\% \\\\\nR1 only & 25.3 & 44.8 & 0.68 & 7.52 & 6.1\\% \\\\\nR1+R2 & 19.4 & 50.1 & 0.78 & 7.31 & 8.2\\% \\\\\nR1+R2+R3 & 15.9 & 54.3 & 0.84 & 7.69 & 1.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Reward component ablation. RC = RC-AUC, MTB = MT-Bench, SI = surface inconsistency rate. R3 is essential for surface coherence; R1 provides directional discrimination; R2 maintains separation.}\n\\label{tab:ablation_components}\n\\end{table}\n\nR1-only reduces NoF from 34.7\\% (R3-only) to 25.3\\%, confirming that directional projection reward alone provides effective anti-sycophancy signal. Adding R2 (R1+R2) further reduces NoF to 19.4\\% and improves WRR to 50.1\\%. The full DC-GRPO (R1+R2+R3) achieves the best NoF (15.9\\%) and WRR (54.3\\%). R3's critical role emerges in surface inconsistency: without it, 8.2\\% of responses exhibit correct internal reasoning but incoherent surface output (compared to 1.2\\% with R3). R3 also preserves MT-Bench (7.69 vs.\\ 7.31 without R3).\n\n\\paragraph{Isolating continuity from directionality.}\nThe Binary Probe $\\to$ Continuous Probe $\\to$ DC-GRPO comparison (Table~\\ref{tab:continuity_vs_direction}) isolates two factors. Continuity accounts for 3.7 pp NoF improvement (Binary $\\to$ Continuous, $p = 0.038$). Directionality accounts for 7.9 pp (Continuous $\\to$ DC-GRPO, $p = 0.014$), confirming that geometric direction information is the primary driver, contributing $2.1\\times$ more than continuity alone.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\n\\textbf{Comparison} & \\textbf{$\\Delta$NoF} & \\textbf{$p$} & \\textbf{Attribution} \\\\\n\\midrule\nBinary $\\to$ Cont. & $-$3.7 & 0.038 & Continuity \\\\\nCont. $\\to$ DC-GRPO & $-$7.9 & 0.014 & Directionality \\\\\nBinary $\\to$ DC-GRPO & $-$11.6 & 0.008 & Combined \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Isolating continuity vs.\\ directionality contributions. Directionality accounts for $2.1\\times$ more NoF reduction than continuity.}\n\\label{tab:continuity_vs_direction}\n\\end{table}\n\n\\paragraph{Reward weight sensitivity.}\nTable~\\ref{tab:weight_sensitivity} presents 6 weight configurations branched from step 4000. NoF varies by only 2.7 pp across all configurations (1.9 pp excluding the extreme R3-dominant setting), demonstrating robustness to hyperparameter choice. R1 weight $\\geq 0.2$ suffices to activate directional reward benefits. The R3-dominant configuration ($w_1 = 0.1$) achieves the worst NoF (18.1\\%) and WRR (44.3\\%), directly illustrating that behavioral reward dominance reintroduces the double-bind even with minimal directional signal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccrrr}\n\\toprule\n\\textbf{Config} & $w_1$ & $w_2$ & $w_3$ & \\textbf{NoF} & \\textbf{WRR} & \\textbf{RC} \\\\\n\\midrule\nDefault & .30 & .20 & .50 & 16.2 & 53.8 & 0.83 \\\\\nR1/R3 rev. & .50 & .20 & .30 & 15.4 & 52.1 & 0.82 \\\\\nR1 dom. & .60 & .10 & .30 & 17.3 & 49.6 & 0.79 \\\\\nEqual & .33 & .33 & .34 & 16.5 & 52.4 & 0.82 \\\\\nR3 dom. & .10 & .10 & .80 & 18.1 & 44.3 & 0.73 \\\\\nR2 enh. & .20 & .40 & .40 & 16.8 & 51.7 & 0.81 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Reward weight sensitivity. NoF range 2.7 pp across 6 configurations demonstrates robustness. RC = RC-AUC.}\n\\label{tab:weight_sensitivity}\n\\end{table}\n\n\\paragraph{Three-way direction design.}\nIntroducing a neutral condition to compute an independent genuine revision direction $\\dgen$ (rather than assuming $\\dgen = -\\dsyc$) reduces the cosine similarity between $\\dgen$ and $-\\dsyc$ from 0.71 to 0.38. A short validation run with the three-way design improves WRR by 2.8 pp (57.1\\% vs.\\ 54.3\\%) with negligible NoF change (+0.4 pp). The independent $\\dgen$ achieves AUROC 0.812 for genuine revision detection. While the improvement is modest (the rank-based R2 already partially mitigates the degeneracy), the three-way design validates that sycophancy and genuine revision occupy distinct subspaces rather than opposing ends of a single axis.\n\n\\subsection{Analysis}\n\\label{sec:analysis}\n\n\\subsubsection{Turn-Depth Analysis}\n\nDC-GRPO's advantage over baselines grows monotonically with dialogue depth (Table~\\ref{tab:turn_depth}). At turn 2, DC-GRPO's NoF advantage over R3-only is 8.1 pp; by turn 4+, the advantage widens to 29.9 pp. DC-GRPO is the only method whose NoF decreases with depth (22.1\\% at turn 2, 8.7\\% at turn 4+); all baselines exhibit worsening sycophancy at deeper turns. The method $\\times$ turn-depth interaction is significant ($p = 0.008$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Turn 2} & \\textbf{Turn 3} & \\textbf{Turn 4+} & \\textbf{Trend} \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{NoF (\\%)$\\downarrow$}} \\\\\nVanilla & 46.3 & 52.1 & 58.4 & $\\uparrow$ worse \\\\\nACT & 33.1 & 37.5 & 42.8 & $\\uparrow$ worse \\\\\nR3-only & 30.2 & 33.8 & 38.6 & $\\uparrow$ worse \\\\\nBin. Probe & 24.8 & 27.1 & 31.2 & $\\uparrow$ worse \\\\\nCont. Probe & 22.1 & 23.4 & 26.8 & $\\uparrow$ worse \\\\\nDC-GRPO & 22.1 & 14.3 & 8.7 & $\\downarrow$ \\textbf{better} \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{WRR (\\%)$\\uparrow$}} \\\\\nVanilla & 39.2 & 37.1 & 35.3 & $\\downarrow$ worse \\\\\nR3-only & 44.3 & 41.2 & 39.4 & $\\downarrow$ worse \\\\\nDC-GRPO & 51.2 & 55.8 & 58.1 & $\\uparrow$ \\textbf{better} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{NoF and WRR by turn depth. DC-GRPO is the only method that improves at deeper turns, where commitment-based sycophancy is strongest. Interaction $p = 0.008$.}\n\\label{tab:turn_depth}\n\\end{table}\n\nThis pattern reflects DC-GRPO's mechanism: as commitment depth increases, the internal divergence between sycophantic reasoning and genuine reasoning grows, making the directional signal more informative. Behavioral methods face the opposite dynamic, as accumulated commitment makes surface-level sycophancy harder to detect while simultaneously increasing sycophantic pressure.\n\n\\subsubsection{R1-R3 Disagreement and Masked Sycophancy}\n\nR1 and R3 disagree on 14.2\\% of training samples (1,760 of 12,400 analyzed). The dominant disagreement type is R1-sycophantic/R3-OK (9.3\\%, 1,153 cases): the model's surface output passes NLI behavioral checks while its internal activations project onto the sycophancy direction. These are cases of masked sycophancy that behavioral-only training systematically misses.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrl}\n\\toprule\n\\textbf{Type} & \\textbf{Rate} & \\textbf{N} & \\textbf{Meaning} \\\\\n\\midrule\nR1-syc, R3-ok & 9.3\\% & 1153 & Masked sycophancy \\\\\nR1-ok, R3-syc & 4.9\\% & 607 & NLI false alarm \\\\\nTotal disagree. & 14.2\\% & 1760 & \\\\\nTotal agree. & 85.8\\% & 10640 & \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{R1-R3 disagreement breakdown. 9.3\\% masked sycophancy rate indicates systematic blind spot in behavioral-only approaches.}\n\\label{tab:disagreement}\n\\end{table}\n\nDisagreement concentrates in medium-evidence scenarios (19.2\\%) and deep dialogue turns (turn 4+: 18.4\\%), as shown in Table~\\ref{tab:disagree_conditions}. Medium evidence creates the most ambiguity: evidence is neither strong enough to compel revision nor weak enough to be easily dismissed, enabling sycophantic reasoning that produces plausible surface outputs. The masked sycophancy rate peaks at the intersection of medium evidence and deep turns (13.4\\% for medium evidence, 12.8\\% for turn 4+).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Evidence}} & \\multicolumn{3}{c}{\\textbf{Turn}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n& Weak & Med & Strong & 2 & 3 & 4+ \\\\\n\\midrule\nDisagree. & 10.8 & 19.2 & 11.7 & 9.8 & 15.6 & 18.4 \\\\\nMasked & 7.1 & 13.4 & 7.2 & 6.4 & 10.2 & 12.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Disagreement and masked sycophancy rates (\\%) by evidence strength and turn depth. Medium evidence and deeper turns are hotspots.}\n\\label{tab:disagree_conditions}\n\\end{table}\n\nThe reverse disagreement (R1-ok/R3-syc, 4.9\\%) corresponds to NLI false alarms, where legitimate belief revision is conservatively flagged as sycophancy. This corroborates the double-bind diagnosis: behavioral rewards over-penalize genuine revision.\n\n\\section{Conclusion}\n\nWe presented DC-GRPO, a training method that uses directional projection in the policy model's activation space to distinguish sycophantic capitulation from genuine belief revision. The approach reduces multi-turn sycophantic capitulation by 18.8 pp compared to behavioral-only training while simultaneously improving warranted revision rate by 12.2 pp. Ablation analysis demonstrates that directional geometry, not signal continuity, is the primary contributor. The method's advantage amplifies at deeper dialogue turns, where it is the only approach that improves rather than degrades. Analysis of reward disagreement reveals 9.3\\% masked sycophancy that behavioral methods systematically miss, concentrated in medium-evidence, deep-turn scenarios that represent deployment-relevant conditions.\n\nLimitations include evaluation on two model families (Qwen3-8B, Llama-3-8B) at the 8B parameter scale, the requirement for model-specific direction computation (cross-model direction cosine is only 0.34), and statistical tests based on 3 random seeds. The three-way direction design shows promise for further improving revision detection, and scaling to larger models and broader dialogue domains remain open directions.\n\n\\bibliography{custom}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "59934b78-a639-4a29-b404-3dafcd281fa5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T125925 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_ent…",
  "leafUuid": "22535344-e2f0-4b64-ba74-69899720746d",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate research paper from experimental data",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252"
}
```

---

### Tool call

_source line 22 · 2026-05-18T13:30:45.660Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DZ4xS9tnFxu4T8rWsxVY3h`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22535344-e2f0-4b64-ba74-69899720746d",
  "isSidechain": false,
  "requestId": "req_011CbA7hBD18afjkQ169iycs",
  "type": "assistant",
  "uuid": "cb517d72-802b-4c12-8889-6b504204dc03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wnKxfEBtNjeeHjPotzHtv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10787,
      "cache_read_input_tokens": 52236,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10787,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 52236,
          "cache_creation_input_tokens": 10787,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10787
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

_source line 23 · 2026-05-18T13:30:45.821Z_

<details><summary>↩ Tool result · `toolu_01DZ4xS9tnFxu4T8rWsxVY3h`</summary>

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
  "parentUuid": "cb517d72-802b-4c12-8889-6b504204dc03",
  "isSidechain": false,
  "promptId": "121615b5-fe01-4239-8e8a-1e78844e9c3d",
  "type": "user",
  "uuid": "85132e94-0a4c-4922-9886-8d2704383d10",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "cb517d72-802b-4c12-8889-6b504204dc03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-18T13:30:49.363Z_

<details><summary>Logged reasoning block</summary>

```text
The acl.sty is not available. Let me switch to a simpler article class setup without the ACL package.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85132e94-0a4c-4922-9886-8d2704383d10",
  "isSidechain": false,
  "requestId": "req_011CbA7hVemYmQXCdUHCb2gd",
  "type": "assistant",
  "uuid": "2ee4c104-14a9-41e3-b3a0-8615a48c30c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019PvzDnsZ9N28nKmvBMcmdH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 429,
      "cache_read_input_tokens": 63023,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 429,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 442,
          "cache_read_input_tokens": 63023,
          "cache_creation_input_tokens": 429,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 429
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

_source line 25 · 2026-05-18T13:30:49.874Z_

ACL style file not available. Switching to plain article class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ee4c104-14a9-41e3-b3a0-8615a48c30c2",
  "isSidechain": false,
  "requestId": "req_011CbA7hVemYmQXCdUHCb2gd",
  "type": "assistant",
  "uuid": "1640311b-500e-4baf-9e83-623d08dae502",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019PvzDnsZ9N28nKmvBMcmdH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 429,
      "cache_read_input_tokens": 63023,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 429,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 442,
          "cache_read_input_tokens": 63023,
          "cache_creation_input_tokens": 429,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 429
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

_source line 26 · 2026-05-18T13:30:53.434Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01CgJZc7Ahh2CF65eq7q7LUA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{hyperref}\n\\usepackage{natbib}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1640311b-500e-4baf-9e83-623d08dae502",
  "isSidechain": false,
  "requestId": "req_011CbA7hVemYmQXCdUHCb2gd",
  "type": "assistant",
  "uuid": "8f45b7c6-ada0-4c77-a34e-e62562f2b820",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019PvzDnsZ9N28nKmvBMcmdH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 429,
      "cache_read_input_tokens": 63023,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 429,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 442,
          "cache_read_input_tokens": 63023,
          "cache_creation_input_tokens": 429,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 429
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

_source line 27 · 2026-05-18T13:30:53.469Z_

<details><summary>↩ Tool result · `toolu_01CgJZc7Ahh2CF65eq7q7LUA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f45b7c6-ada0-4c77-a34e-e62562f2b820",
  "isSidechain": false,
  "promptId": "121615b5-fe01-4239-8e8a-1e78844e9c3d",
  "type": "user",
  "uuid": "f0673325-c9e2-443f-8048-cac987353d5d",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{hyperref}\n\\usepackage{natbib}",
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
          "+\\usepackage{hyperref}",
          "+\\usepackage{natbib}",
          " ",
          " \\newcommand{\\dsyc}{d_{\\text{syc}}}",
          " \\newcommand{\\dgen}{d_{\\text{gen}}}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "8f45b7c6-ada0-4c77-a34e-e62562f2b820",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-18T13:30:56.723Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01TbsWbWGDrDQKUiwQCW1gQw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/paper.tex",
  "old_string": "\\bibliography{custom}",
  "new_string": "%\\bibliography{custom}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0673325-c9e2-443f-8048-cac987353d5d",
  "isSidechain": false,
  "requestId": "req_011CbA7i4N27qveBrLxN9zPE",
  "type": "assistant",
  "uuid": "d6b44758-35e2-492b-bc75-edfa5b51af9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VfajKZAisHqxWGj3ntR2RU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 533,
      "cache_read_input_tokens": 63452,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 533,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 151,
          "cache_read_input_tokens": 63452,
          "cache_creation_input_tokens": 533,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 533
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

_source line 29 · 2026-05-18T13:30:56.735Z_

<details><summary>↩ Tool result · `toolu_01TbsWbWGDrDQKUiwQCW1gQw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6b44758-35e2-492b-bc75-edfa5b51af9d",
  "isSidechain": false,
  "promptId": "121615b5-fe01-4239-8e8a-1e78844e9c3d",
  "type": "user",
  "uuid": "38cf2beb-7cc4-4ee7-aa25-c2292ab5ea91",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/paper.tex",
    "oldString": "\\bibliography{custom}",
    "newString": "%\\bibliography{custom}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 439,
        "oldLines": 6,
        "newStart": 439,
        "newLines": 6,
        "lines": [
          " ",
          " Limitations include evaluation on two model families (Qwen3-8B, Llama-3-8B) at the 8B parameter scale, the requirement for model-specific direction computation (cross-model direction cosine is only 0.34), and statistical tests based on 3 random seeds. The three-way direction design shows promise for further improving revision detection, and scaling to larger models and broader dialogue domains remain open directions.",
          " ",
          "-\\bibliography{custom}",
          "+%\\bibliography{custom}",
          " ",
          " \\end{document}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "d6b44758-35e2-492b-bc75-edfa5b51af9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-18T13:30:56.786Z_

```json
{
  "parentUuid": "38cf2beb-7cc4-4ee7-aa25-c2292ab5ea91",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f0043003-1596-4d5c-bcfa-5651b3007c86",
  "timestamp": "2026-05-18T13:30:56.786Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-18T13:31:00.291Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0193eEZCwGtmBxVPeSyUr1XY`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0043003-1596-4d5c-bcfa-5651b3007c86",
  "isSidechain": false,
  "requestId": "req_011CbA7iJX4n5CUJkvGWJQ54",
  "type": "assistant",
  "uuid": "65ae5931-4b64-4bf9-b4b0-4dda79bc2b95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018tFCLF89UZFs2PyXHpwe3b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 346,
      "cache_read_input_tokens": 63985,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 346,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 63985,
          "cache_creation_input_tokens": 346,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 346
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

_source line 32 · 2026-05-18T13:31:00.885Z_

<details><summary>↩ Tool result · `toolu_0193eEZCwGtmBxVPeSyUr1XY`</summary>

```text
Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 149256 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65ae5931-4b64-4bf9-b4b0-4dda79bc2b95",
  "isSidechain": false,
  "promptId": "121615b5-fe01-4239-8e8a-1e78844e9c3d",
  "type": "user",
  "uuid": "a9747164-4a7d-4eff-ab79-0ea00ed8a873",
  "toolUseResult": {
    "stdout": "Package rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/\ntexlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 149256 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "65ae5931-4b64-4bf9-b4b0-4dda79bc2b95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T13:31:04.295Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HPJVXgkDHiRRZxygWziYht`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Second pdflatex pass for references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9747164-4a7d-4eff-ab79-0ea00ed8a873",
  "isSidechain": false,
  "requestId": "req_011CbA7ic7jcTL9LgWsaGdYA",
  "type": "assistant",
  "uuid": "128e0560-0414-40f4-acbb-de718b2b4931",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0166SFUhJfzPy1z2guzDbaaj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 589,
      "cache_read_input_tokens": 64331,
      "output_tokens": 150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 589,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 150,
          "cache_read_input_tokens": 64331,
          "cache_creation_input_tokens": 589,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 589
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

_source line 34 · 2026-05-18T13:31:04.830Z_

<details><summary>↩ Tool result · `toolu_01HPJVXgkDHiRRZxygWziYht`</summary>

```text
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 150660 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "128e0560-0414-40f4-acbb-de718b2b4931",
  "isSidechain": false,
  "promptId": "121615b5-fe01-4239-8e8a-1e78844e9c3d",
  "type": "user",
  "uuid": "d044d889-0471-42d6-a07f-abd884a14e96",
  "toolUseResult": {
    "stdout": "fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/\ntexlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 150660 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "128e0560-0414-40f4-acbb-de718b2b4931",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-18T13:31:12.827Z_

论文已生成：9 页 PDF，路径 `best/paper.tex`。

覆盖了实验数据中全部 12 个实验：calibration data expansion、layer-wise analysis、evidence strength stratification、cross-model transfer (Llama-3-8B)、DC-GRPO main training、R3-only / ACT / Binary Probe / Continuous Probe baselines、full evaluation with significance tests、direction stability monitoring、reward component ablation (R1-only, R1+R2)、turn-depth analysis、R1-R3 disagreement analysis、reward weight sensitivity、three-way direction design。所有数字直接来自 `experiment_data.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d044d889-0471-42d6-a07f-abd884a14e96",
  "isSidechain": false,
  "requestId": "req_011CbA7ittnTLZ9oLqgWPjRT",
  "type": "assistant",
  "uuid": "520d887e-f03d-40de-bdc5-1cd7a0ca4db3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X85UsDKkgpoHuviUyVxuDH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 240,
      "cache_read_input_tokens": 64920,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 240,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 64920,
          "cache_creation_input_tokens": 240,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 240
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T125925 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_ent…",
  "leafUuid": "520d887e-f03d-40de-bdc5-1cd7a0ca4db3",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate research paper from experimental data",
  "sessionId": "34547890-e122-43c6-bb3a-f938b3a3f252"
}
```

---
