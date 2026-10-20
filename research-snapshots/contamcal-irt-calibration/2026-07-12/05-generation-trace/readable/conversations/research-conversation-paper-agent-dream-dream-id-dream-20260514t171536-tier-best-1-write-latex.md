# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T171536 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/5f0cff07-cb6a-487f-be6b-6af3047fe23a.jsonl`
- **Structured JSON:** [`41f7c1dfbcc227bf3220.json`](../../sessions/41/41f7c1dfbcc227bf3220.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T18:03:37.032Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T18:03:37.032Z",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T171536 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Original framing 完全成立，三条 Claims 无需降级。 Headline: \"ContamCal recovers true benchmark performance within 1.8pp MAE (bootstrap 95% CI: [1.2, 2.4]) with 94% credible interval coverage, while naive scores overestimate by up to 58pp under full contamination (3B GSM8K).\" C2 story: scale-dependent signal effectiveness validated —— S1 Embedding 跨尺度稳健 (AUC>0.95), S2 Min-K++ 和 S4 Self-Critique 在 0.5B 失效 (AUC≈0.47) 但在 1.5B+ 恢复 (AUC>0.70)。Min-K++ 方向性反转 (Cohen's d -1.2 to -2.7 at d100) 作为独立 cautionary finding。RRF 在 1.5B+ 实现真正 多信号融合（非 S1 单信号主导）。C3: 测量误差模型将 coverage 从 ~82% 提升至 94%，Fisher Information 推导确认 AUC≥0.55 为结构可辨识边界， AUC≥0.70 为实用边界。Paper structure 按 paper_framing.md 原样执行。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T18:03:37.037Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T18:03:37.037Z",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a"
}
```

---

## Round 1

37 recorded events

### User

_source line 3 · 2026-05-14T18:03:37.068Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T171536 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Original framing 完全成立，三条 Claims 无需降级。 Headline: "ContamCal recovers true benchmark performance within 1.8pp MAE (bootstrap 95% CI: [1.2, 2.4]) with 94% credible interval coverage, while naive scores overestimate by up to 58pp under full contamination (3B GSM8K)." C2 story: scale-dependent signal effectiveness validated —— S1 Embedding 跨尺度稳健 (AUC>0.95), S2 Min-K++ 和 S4 Self-Critique 在 0.5B 失效 (AUC≈0.47) 但在 1.5B+ 恢复 (AUC>0.70)。Min-K++ 方向性反转 (Cohen's d -1.2 to -2.7 at d100) 作为独立 cautionary finding。RRF 在 1.5B+ 实现真正 多信号融合（非 S1 单信号主导）。C3: 测量误差模型将 coverage 从 ~82% 提升至 94%，Fisher Information 推导确认 AUC≥0.55 为结构可辨识边界， AUC≥0.70 为实用边界。Paper structure 按 paper_framing.md 原样执行。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "14a905e9-cf62-4ad0-acbf-909375bdc04c",
  "type": "user",
  "uuid": "ffe3d183-d09d-4db7-8aad-c2f10b56ea2d",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T18:03:37.066Z_

```json
{
  "parentUuid": "ffe3d183-d09d-4db7-8aad-c2f10b56ea2d",
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
  "uuid": "4fb8086d-4c2c-4b6c-be0f-130038e60427",
  "timestamp": "2026-05-14T18:03:37.066Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T18:03:37.067Z_

```json
{
  "parentUuid": "4fb8086d-4c2c-4b6c-be0f-130038e60427",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7427c3fd-4737-4a0e-8d16-27d1edd90844",
  "timestamp": "2026-05-14T18:03:37.067Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
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
  "aiTitle": "Generate complete ContamCal IRT calibration paper",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a"
}
```

---

### Assistant

_source line 7 · 2026-05-14T18:03:43.276Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7427c3fd-4737-4a0e-8d16-27d1edd90844",
  "isSidechain": false,
  "requestId": "req_011Cb2uGdWfw3LyssFzwU2EA",
  "type": "assistant",
  "uuid": "29117a32-1dc6-43a6-b268-eff8c6c0ff24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Sfxtn43qsTRQ23FBUgjHp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11431,
      "cache_read_input_tokens": 11841,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11431
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

_source line 8 · 2026-05-14T18:03:44.254Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A8rUsEFqQWEvjqADdePveR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29117a32-1dc6-43a6-b268-eff8c6c0ff24",
  "isSidechain": false,
  "requestId": "req_011Cb2uGdWfw3LyssFzwU2EA",
  "type": "assistant",
  "uuid": "d52922b7-a435-4fc0-a7c3-7dda515a9f34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Sfxtn43qsTRQ23FBUgjHp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11431,
      "cache_read_input_tokens": 11841,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11431
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

_source line 9 · 2026-05-14T18:03:44.545Z_

<details><summary>↩ Tool result · `toolu_01A8rUsEFqQWEvjqADdePveR`</summary>

```text
1	[
2	  {
3	    "name": "stage1_signal_pipeline",
4	    "description": "在 exp-001 所有模型上计算 4 路检测信号。0.5B 数据已由 exp_002_signals_05B 完成，此处预测 1.5B/3B 扩展结果。核心期望：S2(Min-K++) 和 S4(Self-Critique) 在 1.5B+ 恢复辨别力。\n",
5	    "results": {
6	      "S1_d005_auc_05B_mean": 0.979,
7	      "S2_d005_auc_05B_mean": 0.465,
8	      "S4_d005_auc_05B_mean": 0.481,
9	      "S1_d005_auc_15B_mmlu": 0.961,
10	      "S1_d005_auc_15B_gsm8k": 0.985,
11	      "S1_d005_auc_15B_arc": 0.99,
12	      "S2_d005_auc_15B_mmlu": 0.718,
13	      "S2_d005_auc_15B_gsm8k": 0.762,
14	      "S2_d005_auc_15B_arc": 0.741,
15	      "S3_d005_auc_15B_mmlu": 0.795,
16	      "S3_d005_auc_15B_gsm8k": 0.832,
17	      "S3_d005_auc_15B_arc": 0.814,
18	      "S4_d005_auc_15B_mmlu": 0.692,
19	      "S4_d005_auc_15B_gsm8k": 0.731,
20	      "S4_d005_auc_15B_arc": 0.712,
21	      "S1_d005_auc_3B_mmlu": 0.948,
22	      "S1_d005_auc_3B_gsm8k": 0.982,
23	      "S1_d005_auc_3B_arc": 0.991,
24	      "S2_d005_auc_3B_mmlu": 0.798,
25	      "S2_d005_auc_3B_gsm8k": 0.842,
26	      "S2_d005_auc_3B_arc": 0.816,
27	      "S3_d005_auc_3B_mmlu": 0.836,
28	      "S3_d005_auc_3B_gsm8k": 0.873,
29	      "S3_d005_auc_3B_arc": 0.855,
30	      "S4_d005_auc_3B_mmlu": 0.751,
31	      "S4_d005_auc_3B_gsm8k": 0.792,
32	      "S4_d005_auc_3B_arc": 0.775,
33	      "S2_d100_cohens_d_15B_mean": -1.52,
34	      "S2_d100_cohens_d_3B_mean": -1.14,
35	      "S1_d100_cohens_d_15B_mean": 3.85,
36	      "S1_d100_cohens_d_3B_mean": 4.02
37	    },
38	    "tables": [
39	      {
40	        "name": "Signal × Scale × Benchmark AUC at d005",
41	        "headers": [
42	          "Signal",
43	          "Benchmark",
44	          "0.5B",
45	          "1.5B",
46	          "3B"
47	        ],
48	        "rows": [
49	          [
50	            "S1 Embedding",
51	            "MMLU",
52	            0.953,
53	            0.961,
54	            0.948
55	          ],
56	          [
57	            "S1 Embedding",
58	            "GSM8K",
59	            0.988,
60	            0.985,
61	            0.982
62	          ],
63	          [
64	            "S1 Embedding",
65	            "ARC-C",
66	            0.995,
67	            0.99,
68	            0.991
69	          ],
70	          [
71	            "S2 Min-K++",
72	            "MMLU",
73	            0.466,
74	            0.718,
75	            0.798
76	          ],
77	          [
78	            "S2 Min-K++",
79	            "GSM8K",
80	            0.465,
81	            0.762,
82	            0.842
83	          ],
84	          [
85	            "S2 Min-K++",
86	            "ARC-C",
87	            0.466,
88	            0.741,
89	            0.816
90	          ],
91	          [
92	            "S3 ConStat",
93	            "MMLU",
94	            "~0.55",
95	            0.795,
96	            0.836
97	          ],
98	          [
99	            "S3 ConStat",
100	            "GSM8K",
101	            "~0.53",
102	            0.832,
103	            0.873
104	          ],
105	          [
106	            "S3 ConStat",
107	            "ARC-C",
108	            "~0.52",
109	            0.814,
110	            0.855
111	          ],
112	          [
113	            "S4 Self-Critique",
114	            "MMLU",
115	            0.517,
116	            0.692,
117	            0.751
118	          ],
119	          [
120	            "S4 Self-Critique",
121	            "GSM8K",
122	            0.495,
123	            0.731,
124	            0.792
125	          ],
126	          [
127	            "S4 Self-Critique",
128	            "ARC-C",
129	            0.433,
130	            0.712,
131	            0.775
132	          ]
133	        ]
134	      },
135	      {
136	        "name": "Min-K++ d100 Cross-Model Cohen's d (方向性反转)",
137	        "headers": [
138	          "Benchmark",
139	          "0.5B",
140	          "1.5B",
141	          "3B"
142	        ],
143	        "rows": [
144	          [
145	            "MMLU",
146	            -1.22,
147	            -1.08,
148	            -0.85
149	          ],
150	          [
151	            "GSM8K",
152	            -2.67,
153	            -1.78,
154	            -1.31
155	          ],
156	          [
157	            "ARC-C",
158	            -2.05,
159	            -1.71,
160	            -1.26
161	          ]
162	        ]
163	      }
164	    ],
165	    "figures": [],
166	    "analysis": "Scale-dependent signal effectiveness 的核心证据。0.5B→1.5B 跨越了 Min-K++ 有效性的 capacity threshold（AUC 从 0.47 跃至 0.74）， 0.5B→3B 更进一步（0.47→0.82）。Self-Critique 在 1.5B 恢复到 0.71 刚好过 0.70 threshold。S1 Embedding 跨尺度稳定在 0.95+ ——不受尺度影响因为它是 training-data-independent 的语义相似度信号。 这为 C2 \"method-specific, scale-dependent\" framing 提供直接证据。\n\n\nS2 (Min-K++) 在 1.5B+ 恢复的核心机制：更大模型有更强的 token-level memorization capacity（LoRA adapter 从 34MB/0.5B → 71MB/1.5B → 115MB/3B）， paraphrase 训练数据在模型中留下更可检测的 token probability 指纹。 0.5B 容量有限，LoRA 微调不足以产生可区分的 memorization 信号。 S4 (Self-Critique) 恢复的机制：Self-Critique 本质是生成任务，要求模型 对自身知识来源进行元认知。0.5B 生成质量太差（自我评估近似随机噪声）， 1.5B+ 可产生足够连贯的自我评估，contaminated items 呈现特征性低熵模式。 S3 (ConStat) 在 1.5B+ 表现更好因为更强模型对 memorized original items vs unseen paraphrases 产生更大的 performance gap。S2 d100 反转持续但 幅度减弱（-1.52 at 1.5B vs -1.98 at 0.5B），因为更大模型的 perplexity distribution 更稳定，全量污染导致的分布偏移相对减小。\n"
167	  },
168	  {
169	    "name": "rrf_aggregation_ablation",
170	    "description": "4 信号 RRF 融合及消融实验。测试单信号 vs RRF 在不同尺度下的表现， 验证 RRF 在 1.5B+ 实现真正多信号融合。\n",
171	    "results": {
172	      "rrf_4signal_auc_05B": 0.962,
173	      "rrf_4signal_auc_15B": 0.924,
174	      "rrf_4signal_auc_3B": 0.943,
175	      "single_S1_auc_05B": 0.979,
176	      "single_S1_auc_15B": 0.972,
177	      "single_S1_auc_3B": 0.964,
178	      "single_S2_auc_05B": 0.465,
179	      "single_S2_auc_15B": 0.74,
180	      "single_S2_auc_3B": 0.819,
181	      "single_S3_auc_05B": 0.533,
182	      "single_S3_auc_15B": 0.814,
183	      "single_S3_auc_3B": 0.855,
184	      "single_S4_auc_05B": 0.481,
185	      "single_S4_auc_15B": 0.712,
186	      "single_S4_auc_3B": 0.773,
187	      "equal_weight_rank_avg_auc_15B": 0.908,
188	      "calibrated_weighted_rrf_auc_15B": 0.931,
189	      "rrf_2signal_auc_05B": 0.508,
190	      "rrf_2signal_auc_15B": 0.782,
191	      "rrf_2signal_auc_3B": 0.831,
192	      "fp_injection_5pct_auc_drop": 0.008,
193	      "fp_injection_10pct_auc_drop": 0.014,
194	      "fp_injection_15pct_auc_drop": 0.023,
195	      "rrf_05B_S1_weight_share": 0.89,
196	      "rrf_15B_S1_weight_share": 0.38,
197	      "rrf_3B_S1_weight_share": 0.31
198	    },
199	    "tables": [
200	      {
201	        "name": "RRF vs Single-Signal AUC (d005, benchmark-averaged)",
202	        "headers": [
203	          "Method",
204	          "0.5B",
205	          "1.5B",
206	          "3B"
207	        ],
208	        "rows": [
209	          [
210	            "RRF 4-signal",
211	            0.962,
212	            0.924,
213	            0.943
214	          ],
215	          [
216	            "S1 only",
217	            0.979,
218	            0.972,
219	            0.964
220	          ],
221	          [
222	            "S2 only",
223	            0.465,
224	            0.74,
225	            0.819
226	          ],
227	          [
228	            "S3 only",
229	            0.533,
230	            0.814,
231	            0.855
232	          ],
233	          [
234	            "S4 only",
235	            0.481,
236	            0.712,
237	            0.773
238	          ],
239	          [
240	            "RRF 2-signal (closed)",
241	            0.508,
242	            0.782,
243	            0.831
244	          ],
245	          [
246	            "Equal-weight rank avg",
247	            "—",
248	            0.908,
249	            "—"
250	          ],
251	          [
252	            "Calibrated weighted RRF",
253	            "—",
254	            0.931,
255	            "—"
256	          ]
257	        ]
258	      }
259	    ],
260	    "figures": [],
261	    "analysis": "RRF 在 0.5B 退化为 S1-dominated（weight share 89%）是预期的、正确的行为。 论文应 honestly 报告这一 degradation 并强调：(1) RRF 的价值在 1.5B+ 显现， 实现真正多信号融合; (2) 即使在 0.5B，RRF 的 graceful degradation 优于 hard failure; (3) FP robustness 证明 RRF 是比 learned aggregation 更稳健 的选择（meta-circularity argument 成立）。calibrated weighted RRF 微弱优势 不足以 justify 引入 training 依赖。\n\n\n0.5B RRF (0.962) 低于单独 S1 (0.979)，因为 S2/S4 近似随机噪声拉低 融合质量——RRF 的 rank fusion 无法区分有效和无效信号。这是 honest characterization of degraded regime。0.5B 的 S1 weight share 达 89% 说明 RRF 退化为近似单信号模式。1.5B RRF (0.924) 虽然低于单独 S1 (0.972)，但高于任何非 S1 单信号，且通过 precision 提升（false positive reduction）在 IRT 下游产生更好的 exposure estimates。3B RRF (0.943) 接近 S1 水平同时整合其他信号的互补信息。calibrated weighted RRF (0.931 at 1.5B) 比标准 RRF (0.924) 略优但差距不大——验证了 RRF 作为 training-free 方案的合理性。FP injection 鲁棒性好（15% FP 仅 降 2.3% AUC），因为 RRF 的 rank-based aggregation 天然抗异常值。\n"
262	  },
263	  {
264	    "name": "simulation_identifiability_sweep_v2",
265	    "description": "完成 120-condition simulation sweep。已有 48/120 条完成 （AUC=0.55 全部完成，AUC=0.80 部分）。预测全部完成后的结果。\n",
266	    "results": {
267	      "auc055_n20_gamma_bias": 0.02,
268	      "auc055_n20_gamma_rmse": 0.04,
269	      "auc055_n20_ci95_width_pp": 13.3,
270	      "auc055_n20_ci95_coverage": 0.8,
271	      "auc055_n50_gamma_bias": 0.015,
272	      "auc055_n50_gamma_rmse": 0.026,
273	      "auc055_n50_ci95_width_pp": 8.7,
274	      "auc055_n50_ci95_coverage": 0.9,
275	      "auc055_n100_gamma_bias": -0.003,
276	      "auc055_n100_gamma_rmse": 0.004,
277	      "auc055_n100_ci95_width_pp": 6.5,
278	      "auc055_n100_ci95_coverage": 1.0,
279	      "auc065_n20_gamma_bias": 0.016,
280	      "auc065_n20_gamma_rmse": 0.035,
281	      "auc065_n20_ci95_width_pp": 11.8,
282	      "auc065_n20_ci95_coverage": 0.85,
283	      "auc065_n50_gamma_bias": 0.01,
284	      "auc065_n50_gamma_rmse": 0.02,
285	      "auc065_n50_ci95_width_pp": 7.6,
286	      "auc065_n50_ci95_coverage": 0.93,
287	      "auc065_n100_gamma_bias": -0.004,
288	      "auc065_n100_gamma_rmse": 0.008,
289	      "auc065_n100_ci95_width_pp": 5.8,
290	      "auc065_n100_ci95_coverage": 0.97,
291	      "auc070_n50_gamma_bias": 0.008,
292	      "auc070_n50_gamma_rmse": 0.018,
293	      "auc070_n50_ci95_width_pp": 7.0,
294	      "auc070_n50_ci95_coverage": 0.95,
295	      "auc070_n100_gamma_bias": -0.002,
296	      "auc070_n100_gamma_rmse": 0.006,
297	      "auc070_n100_ci95_width_pp": 5.3,
298	      "auc070_n100_ci95_coverage": 0.98,
299	      "auc080_n50_gamma_bias": 0.006,
300	      "auc080_n50_gamma_rmse": 0.014,
301	      "auc080_n50_ci95_width_pp": 6.2,
302	      "auc080_n50_ci95_coverage": 0.96,
303	      "auc080_n100_gamma_bias": 0.003,
304	      "auc080_n100_gamma_rmse": 0.005,
305	      "auc080_n100_ci95_width_pp": 4.8,
306	      "auc080_n100_ci95_coverage": 0.98,
307	      "auc090_n50_gamma_bias": 0.004,
308	      "auc090_n50_gamma_rmse": 0.01,
309	      "auc090_n50_ci95_width_pp": 5.4,
310	      "auc090_n50_ci95_coverage": 0.97,
311	      "auc090_n100_gamma_bias": 0.002,
312	      "auc090_n100_gamma_rmse": 0.004,
313	      "auc090_n100_ci95_width_pp": 4.2,
314	      "auc090_n100_ci95_coverage": 0.99,
315	      "prior_sd05_ci_narrowing_pct": 18,
316	      "prior_sd20_ci_widening_pct": 28,
317	      "continuous_vs_binary_ci_ratio": 0.92,
318	      "fisher_info_auc_threshold_structural": 0.52,
319	      "fisher_info_auc_threshold_practical": 0.7,
320	      "growing_pains_n20_ci_narrowing_pct": 22,
321	      "total_divergences": 0,
322	      "max_rhat_across_all": 1.012,
323	      "median_fit_time_sec": 1150
324	    },
325	    "tables": [
326	      {
327	        "name": "γ Recovery: AUC × N_models Grid (γ_true=0.5)",
328	        "headers": [
329	          "AUC",
330	          "N",
331	          "Bias",
332	          "RMSE",
333	          "CI95 Width (pp)",
334	          "Coverage 95%",
335	          "θ Corr"
336	        ],
337	        "rows": [
338	          [
339	            0.55,
340	            20,
341	            "+0.020",
342	            0.04,
343	            13.3,
344	            "80%",
345	            0.958
346	          ],
347	          [
348	            0.55,
349	            50,
350	            "+0.015",
351	            0.026,
352	            8.7,
353	            "90%",
354	            0.947
355	          ],
356	          [
357	            0.55,
358	            100,
359	            "−0.003",
360	            0.004,
361	            6.5,
362	            "100%",
363	            0.95
364	          ],
365	          [
366	            0.65,
367	            20,
368	            "+0.016",
369	            0.035,
370	            11.8,
371	            "85%",
372	            0.955
373	          ],
374	          [
375	            0.65,
376	            50,
377	            "+0.010",
378	            0.02,
379	            7.6,
380	            "93%",
381	            0.952
382	          ],
383	          [
384	            0.65,
385	            100,
386	            "−0.004",
387	            0.008,
388	            5.8,
389	            "97%",
390	            0.956
391	          ],
392	          [
393	            0.7,
394	            50,
395	            "+0.008",
396	            0.018,
397	            7.0,
398	            "95%",
399	            0.958
400	          ],
401	          [
402	            0.7,
403	            100,
404	            "−0.002",
405	            0.006,
406	            5.3,
407	            "98%",
408	            0.961
409	          ],
410	          [
411	            0.8,
412	            50,
413	            "+0.006",
414	            0.014,
415	            6.2,
416	            "96%",
417	            0.96
418	          ],
419	          [
420	            0.8,
421	            100,
422	            "+0.003",
423	            0.005,
424	            4.8,
425	            "98%",
426	            0.965
427	          ],
428	          [
429	            0.9,
430	            50,
431	            "+0.004",
432	            0.01,
433	            5.4,
434	            "97%",
435	            0.964
436	          ],
437	          [
438	            0.9,
439	            100,
440	            "+0.002",
441	            0.004,
442	            4.2,
443	            "99%",
444	            0.968
445	          ]
446	        ]
447	      }
448	    ],
449	    "figures": [],
450	    "analysis": "AUC≥0.70 at N≥50 为 practical identifiability sweet spot（CI<7pp, coverage≥95%）。这正好对应 best tier 的 S2 AUC at 1.5B (~0.74)， 意味着 1.5B 模型的 Min-K++ 信号刚好越过 practical threshold。 AUC=0.55 仍可识别（CI<9pp at N≥50）但 coverage 仅 90%——需要 measurement error model 补偿。Fisher Information 推导提供理论根基， 解决 reviewer concern #1。\n\n\nAUC=0.80 N=50 的 CI width (6.2pp) 相比初步 1-seed 的 16.2pp 大幅下降—— 初始异常值被 seed 平均消除（1-seed 结果是极端离群值，10-seed 平均 回归到与趋势一致的水平）。CI width 随 AUC 单调递减（从 0.55 的 8.7pp 到 0.90 的 5.4pp at N=50）符合 Fisher Information 预测：I(γ) 随 AUC 增大，posterior uncertainty 随之收缩。CI width 随 N 按 ~1/√N 缩放 （实测比率 N20/N100 = 2.04 at AUC=0.55，理论 2.24）。 coverage 在 N=20 时低于 nominal (80-85%) 因为少量 examinee 导致 posterior 过于集中——这是已知的 small-N IRT limitation。N≥50 时 coverage 达 90%+，N=100 时接近 nominal。Fisher Information 推导 给出 structural identifiability 下界 AUC≈0.52（I(γ)>0 的理论保证）， practical threshold AUC≈0.70 定义为 \"CI95 width < 10pp at N=50\"。 连续 exposure 比 binary 产生 ~8% 更窄的 CI，因为连续值提供更多 信息。Growing Pains pre-estimation 在 N=20 缩窄 CI ~22%，因为 借用外部数据的 item parameter 估计减少了参数不确定性。\n"
451	  },
452	  {
453	    "name": "noise_propagation_analysis_v3",
454	    "description": "测量误差模型将 Stage 1 信号不确定性传播至 IRT posterior。当前 v3 在 σ_e=0.1 条件下 ME 与 simple 模型差异不显著（γ 偏差问题待修复）。 Best tier 预测在更高 σ_e 条件下 ME 模型展现明确优势。\n",
455	    "results": {
456	      "sigma01_me_gamma_bias": 0.02,
457	      "sigma01_me_gamma_rmse": 0.04,
458	      "sigma01_me_ci95_coverage": 0.95,
459	      "sigma01_me_ci_width_pp": 5.2,
460	      "sigma01_simple_gamma_bias": 0.03,
461	      "sigma01_simple_ci95_coverage": 0.91,
462	      "sigma01_simple_ci_width_pp": 4.8,
463	      "sigma03_me_gamma_bias": 0.04,
464	      "sigma03_me_gamma_rmse": 0.07,
465	      "sigma03_me_ci95_coverage": 0.93,
466	      "sigma03_me_ci_width_pp": 7.8,
467	      "sigma03_simple_gamma_bias": 0.09,
468	      "sigma03_simple_ci95_coverage": 0.78,
469	      "sigma03_simple_ci_width_pp": 5.1,
470	      "sigma05_me_gamma_bias": 0.06,
471	      "sigma05_me_gamma_rmse": 0.11,
472	      "sigma05_me_ci95_coverage": 0.91,
473	      "sigma05_me_ci_width_pp": 11.4,
474	      "sigma05_simple_gamma_bias": 0.18,
475	      "sigma05_simple_ci95_coverage": 0.65,
476	      "sigma05_simple_ci_width_pp": 5.3,
477	      "noise_1x_ci_widening_pct": 28,
478	      "noise_15x_ci_widening_pct": 52,
479	      "noise_2x_ci_widening_pct": 83,
480	      "coverage_gap_simple_vs_nominal": 0.13,
481	      "coverage_gap_me_vs_nominal": 0.01
482	    },
483	    "tables": [
484	      {
485	        "name": "ME vs Simple Model Coverage (95% nominal)",
486	        "headers": [
487	          "σ_e",
488	          "ME Coverage",
489	          "ME CI Width (pp)",
490	          "Simple Coverage",
491	          "Simple CI Width (pp)"
492	        ],
493	        "rows": [
494	          [
495	            0.1,
496	            "95%",
497	            5.2,
498	            "91%",
499	            4.8
500	          ],
501	          [
502	            0.3,
503	            "93%",
504	            7.8,
505	            "78%",
506	            5.1
507	          ],
508	          [
509	            0.5,
510	            "91%",
511	            11.4,
512	            "65%",
513	            5.3
514	          ]
515	        ]
516	      },
517	      {
518	        "name": "Post-hoc Noise Injection CI Widening",
519	        "headers": [
520	          "Noise Level",
521	          "γ CI Widening",
522	          "θ CI Widening",
523	          "Coverage Change"
524	        ],
525	        "rows": [
526	          [
527	            "1.0×",
528	            "+28%",
529	            "+15%",
530	            "−3pp"
531	          ],
532	          [
533	            "1.5×",
534	            "+52%",
535	            "+31%",
536	            "−8pp"
537	          ],
538	          [
539	            "2.0×",
540	            "+83%",
541	            "+48%",
542	            "−15pp"
543	          ]
544	        ]
545	      }
546	    ],
547	    "figures": [],
548	    "analysis": "ME 模型是 C3 claims 的关键基础设施。在真实场景中 σ_e ≈ 0.15-0.30 （基于 exp-002 signal pipeline 的 FP/FN rates），ME 模型将 coverage 从 ~78-91% 提升至 93-95%。这解决了 exp-004 simulation sweep 中 发现的 coverage gap（尤其在 low-AUC/small-N regime）。CI width 增加是必要代价——更宽的 CI 反映了 genuine epistemic uncertainty。 论文中框架为：\"Models with high-AUC signals get tighter CIs; those with degraded signals get appropriately wider CIs.\"\n\n\n当前 v3 结果中 γ 偏差问题（seed 42: 0.793 vs true 0.5, seed 43: 0.402） 源于模型中 latent τ prior 与真实 exposure 分布不匹配——在 best tier， 这通过 prior calibration (使用 exp-001 ground-truth FP/FN rates 估计 σ_e) 和增加 seeds (20+ seeds 平均) 得到解决。σ_e=0.1 时 ME vs simple 差异小（覆盖 95% vs 91%），因为低噪声下 point-estimate exposure 已足够好。σ_e=0.3 时差异显著（93% vs 78%），因为 simple 模型将噪声 错误归因为真实 exposure variation，导致 γ 被高估且 CI 过窄。ME 模型 通过显式建模 noise 产生更宽但更诚实的 CI。σ_e=0.5 时 ME 覆盖仍有 91%（略低于 nominal），因为高噪声下即使 ME 模型也难以完全分离 signal 和 noise。simple 模型在 σ_e=0.5 时严重失效（65% coverage）。 Post-hoc noise injection的 CI widening 与 σ_e 水平呈超线性关系。\n"
549	  },
550	  {
551	    "name": "irt_calibration_and_baselines",
552	    "description": "核心实验。4PL+γ IRT per-benchmark fitting on 3 scales × 5 dosages × 3 seeds = 45 model instances per benchmark。与 7 baselines 对比 5 metrics。best tier: 全面优于所有 baselines。\n",
553	    "results": {
554	      "ours_mae_pp": 1.8,
555	      "ours_mae_bootstrap_lo": 1.2,
556	      "ours_mae_bootstrap_hi": 2.4,
557	      "ours_ci95_coverage": 0.94,
558	      "ours_ci80_coverage": 0.83,
559	      "ours_ci50_coverage": 0.52,
560	      "ours_ci_width_avg_pp": 4.2,
561	      "ours_kendall_tau": 0.96,
562	      "ours_dose_response_monotonicity": 0.95,
563	      "b0_raw_mae_pp": 8.2,
564	      "b0_raw_kendall_tau": 0.87,
565	      "b1_remove_mae_pp": 4.6,
566	      "b1_remove_kendall_tau": 0.91,
567	      "b2_single_2pl_mae_pp": 2.9,
568	      "b2_single_2pl_ci95_coverage": 0.81,
569	      "b2_single_2pl_ci_width_pp": 5.6,
570	      "b2_single_2pl_kendall_tau": 0.94,
571	      "b3_vanilla_4pl_mae_pp": 6.5,
572	      "b3_vanilla_4pl_ci95_coverage": 0.58,
573	      "b3_vanilla_4pl_ci_width_pp": 3.2,
574	      "b3_vanilla_4pl_kendall_tau": 0.89,
575	      "b4_linear_mae_pp": 3.2,
576	      "b4_linear_ci95_coverage": 0.76,
577	      "b4_linear_ci_width_pp": 6.8,
578	      "b4_linear_kendall_tau": 0.93,
579	      "b5_emperor_mae_pp": 5.8,
580	      "b5_emperor_kendall_tau": 0.89,
581	      "b6_dcr_mae_pp": 3.9,
582	      "b6_dcr_kendall_tau": 0.92,
583	      "ours_mmlu_mae_pp": 1.1,
584	      "b0_raw_mmlu_mae_pp": 4.3,
585	      "b6_dcr_mmlu_mae_pp": 2.5,
586	      "ours_gsm8k_mae_pp": 2.8,
587	      "b0_raw_gsm8k_mae_pp": 14.6,
588	      "b6_dcr_gsm8k_mae_pp": 6.2,
589	      "ours_arc_mae_pp": 1.2,
590	      "b0_raw_arc_mae_pp": 4.8,
591	      "b6_dcr_arc_mae_pp": 2.8,
592	      "ours_05B_mae_pp": 2.3,
593	      "ours_15B_mae_pp": 1.4,
594	      "ours_3B_mae_pp": 1.6,
595	      "gamma_mmlu_mean": 0.22,
596	      "gamma_mmlu_ci": [
597	        0.08,
598	        0.38
599	      ],
600	      "gamma_gsm8k_mean": 0.85,
601	      "gamma_gsm8k_ci": [
602	        0.62,
603	        1.12
604	      ],
605	      "gamma_arc_mean": 0.18,
606	      "gamma_arc_ci": [
607	        0.04,
608	        0.34
609	      ],
610	      "gamma_heterogeneity_chi2_p": 0.002,
611	      "joint_gamma_global": 0.41,
612	      "joint_gamma_mae_pp": 2.6,
613	      "residual_correlation_mean": 0.032,
614	      "residual_correlation_max": 0.085,
615	      "mcmc_divergences": 0,
616	      "mcmc_max_rhat": 1.008,
617	      "mcmc_min_ess": 850,
618	      "mcmc_fit_time_per_benchmark_min": 45
619	    },
620	    "tables": [
621	      {
622	        "name": "Main Results: 8 Methods × 5 Metrics",
623	        "headers": [
624	          "Method",
625	          "MAE (pp)↓",
626	          "95% Coverage↑",
627	          "CI Width (pp)↓",
628	          "Kendall τ↑",
629	          "Monotonicity"
630	        ],
631	        "rows": [
632	          [
633	            "4PL+γ ME (ours)",
634	            "1.8 [1.2,2.4]",
635	            "94%",
636	            4.2,
637	            0.96,
638	            0.95
639	          ],
640	          [
641	            "B0: Raw",
642	            8.2,
643	            "—",
644	            "—",
645	            0.87,
646	            "—"
647	          ],
648	          [
649	            "B1: Remove-rescore",
650	            4.6,
651	            "—",
652	            "—",
653	            0.91,
654	            "—"
655	          ],
656	          [
657	            "B2: 2PL+γ (S1 only)",
658	            2.9,
659	            "81%",
660	            5.6,
661	            0.94,
662	            0.9
663	          ],
664	          [
665	            "B3: Vanilla 4PL",
666	            6.5,
667	            "58%",
668	            3.2,
669	            0.89,
670	            "—"
671	          ],
672	          [
673	            "B4: Linear reg + boot",
674	            3.2,
675	            "76%",
676	            6.8,
677	            0.93,
678	            0.85
679	          ],
680	          [
681	            "B5: Emperor mitigation",
682	            5.8,
683	            "—",
684	            "—",
685	            0.89,
686	            "—"
687	          ],
688	          [
689	            "B6: DCR fuzzy",
690	            3.9,
691	            "—",
692	            "—",
693	            0.92,
694	            0.8
695	          ]
696	        ]
697	      },
698	      {
699	        "name": "Per-Benchmark MAE (pp): Our Method vs Key Baselines",
700	        "headers": [
701	          "Benchmark",
702	          "4PL+γ ME",
703	          "B0 Raw",
704	          "B2 2PL+γ",
705	          "B4 Linear",
706	          "B6 DCR"
707	        ],
708	        "rows": [
709	          [
710	            "MMLU",
711	            1.1,
712	            4.3,
713	            1.8,
714	            2.1,
715	            2.5
716	          ],
717	          [
718	            "GSM8K",
719	            2.8,
720	            14.6,
721	            4.2,
722	            5.1,
723	            6.2
724	          ],
725	          [
726	            "ARC-C",
727	            1.2,
728	            4.8,
729	            2.0,
730	            2.2,
731	            2.8
732	          ],
733	          [
734	            "Average",
735	            1.8,
736	            8.2,
737	            2.9,
738	            3.2,
739	            3.9
740	          ]
741	        ]
742	      },
743	      {
744	        "name": "Per-Benchmark γ_k Estimates",
745	        "headers": [
746	          "Benchmark",
747	          "γ_k mean",
748	          "95% CI",
749	          "Interpretation"
750	        ],
751	        "rows": [
752	          [
753	            "MMLU",
754	            0.22,
755	            "[0.08, 0.38]",
756	            "MC memorization 产生中等 inflation"
757	          ],
758	          [
759	            "GSM8K",
760	            0.85,
761	            "[0.62, 1.12]",
762	            "生成式任务极易被 answer memorization 加速"
763	          ],
764	          [
765	            "ARC-C",
766	            0.18,
767	            "[0.04, 0.34]",
768	            "MC 格式但 science reasoning 部分抗 memorization"
769	          ]
770	        ]
771	      },
772	      {
773	        "name": "Dose-Response: 3B GSM8K (最戏剧性案例)",
774	        "headers": [
775	          "Dosage",
776	          "Observed",
777	          "Calibrated (ours)",
778	          "True (d000)",
779	          "Residual"
780	        ],
781	        "rows": [
782	          [
783	            "d000 (0%)",
784	            "12.0%",
785	            "—",
786	            "12.0%",
787	            "—"
788	          ],
789	          [
790	            "d005 (5%)",
791	            "20.8%",
792	            "13.2%",
793	            "12.0%",
794	            "+1.2pp"
795	          ],
796	          [
797	            "d025 (25%)",
798	            "~35.4%",
799	            "14.5%",
800	            "12.0%",
801	            "+2.5pp"
802	          ],
803	          [
804	            "d050 (50%)",
805	            "~51.8%",
806	            "15.1%",
807	            "12.0%",
808	            "+3.1pp"
809	          ],
810	          [
811	            "d100 (100%)",
812	            "69.7%",
813	            "16.2%",
814	            "12.0%",
815	            "+4.2pp"
816	          ]
817	        ]
818	      }
819	    ],
820	    "figures": [],
821	    "analysis": "这是论文的 Table 1。核心叙事：(1) ContamCal MAE 1.8pp 显著优于最佳 baseline DCR 的 3.9pp (bootstrap p<0.01)；(2) 唯一提供 near-nominal coverage 的方法（94% vs baselines 的 58-81%）；(3) γ_k heterogeneity 证明 per-benchmark fitting 的必要性——GSM8K γ=0.85 vs MMLU γ=0.22 差异 4 倍，joint model 会 overfit MMLU 同时 underfit GSM8K； (4) 3B GSM8K dose-response 是最佳可视化案例（57pp inflation 被矫正 至 ~4pp residual）。0.5B 的 higher MAE (2.3pp) 和 wider CI 不是缺陷 而是 honest UQ——信号差的模型得到更宽的 CI，这恰好是 C3 的核心主张。\n\n\nMAE 1.8pp (CI [1.2, 2.4]) 的分解： MMLU (1.1pp) 最低因为污染效应小（0.5B 的 forgetting 被 θ 下降吸收， 1.5B/3B 的 inflation 仅 0.5-1.8pp 容易矫正）。 GSM8K (2.8pp) 最高因为 3B 的 57pp inflation 要求巨大矫正——即使 IRT 模型准确估计 γ=0.85，exposure-score 中的噪声在乘以 γ 后放大为 ~3pp residual。ARC (1.2pp) 居中。 0.5B MAE (2.3pp) 高于 1.5B/3B 因为：(1) 0.5B 信号质量差（仅 S1 有效，exposure 估计噪声大）；(2) catastrophic forgetting 使 θ 和 γ 效应交织。ME 模型在 0.5B 条件下产生更宽 CI 以补偿。 γ_k heterogeneity (p=0.002) 证明 per-benchmark fitting 优于 joint fitting——GSM8K 的 γ=0.85 远高于 MMLU/ARC 的 0.18-0.22， 反映 MC 格式对 memorization 的易感性差异。 joint model (shared γ=0.41) MAE 2.6pp > per-benchmark 1.8pp, 确认 heterogeneity matters。 Baselines 排序：DCR (3.9) > Linear (3.2) > Single-2PL+γ (2.9) > ours (1.8)。 DCR 的 6.2pp GSM8K MAE 暴露了它对 large inflation 的处理弱点。 Vanilla 4PL (6.5pp) 接近 Raw (8.2pp) 因为没有 contamination modeling 的 IRT 将 inflation 错误吸收进 θ。Emperor (5.8pp) 确认 mitigation 策略不足以消除 contamination effect。 Coverage 0.94 接近 nominal 0.95（ME model 功劳），而 Simple model (B2, B3) 覆盖仅 58-81%——vanilla 4PL 的 58% 说明不建模 contamination 的 IRT 产出过窄、错误的 CI。 Kendall τ=0.96 说明 calibrated ranking 高度保真。\n"
822	  },
823	  {
824	    "name": "scale_bridging_7b",
825	    "description": "Qwen2.5-7B LoRA SFT at 5 dosage levels (d000-d100)。验证 calibration 在更大模型上成立。需 multi-GPU (1×H100 per run)。\n",
826	    "results": {
827	      "d000_mmlu": 0.718,
828	      "d000_gsm8k": 0.792,
829	      "d000_arc": 0.878,
830	      "d000_humaneval": 0.415,
831	      "d005_mmlu_inflation_pp": 0.8,
832	      "d005_gsm8k_inflation_pp": 1.2,
833	      "d025_mmlu_inflation_pp": 2.5,
834	      "d025_gsm8k_inflation_pp": 5.8,
835	      "d100_mmlu_inflation_pp": 4.1,
836	      "d100_gsm8k_inflation_pp": 12.5,
837	      "d100_arc_inflation_pp": 2.8,
838	      "S1_d005_auc_7B_mean": 0.954,
839	      "S2_d005_auc_7B_mean": 0.871,
840	      "S4_d005_auc_7B_mean": 0.812,
841	      "calibration_mae_pp_7B": 1.4,
842	      "ci95_coverage_7B": 0.95,
843	      "kendall_tau_7B": 0.97
844	    },
845	    "tables": [
846	      {
847	        "name": "7B Dose-Response",
848	        "headers": [
849	          "Dosage",
850	          "MMLU",
851	          "GSM8K",
852	          "ARC-C"
853	        ],
854	        "rows": [
855	          [
856	            "d000",
857	            "71.8%",
858	            "79.2%",
859	            "87.8%"
860	          ],
861	          [
862	            "d005",
863	            "72.6%",
864	            "80.4%",
865	            "88.1%"
866	          ],
867	          [
868	            "d025",
869	            "74.3%",
870	            "85.0%",
871	            "89.2%"
872	          ],
873	          [
874	            "d100",
875	            "75.9%",
876	            "91.7%",
877	            "90.6%"
878	          ]
879	        ]
880	      },
881	      {
882	        "name": "7B Signal AUC at d005",
883	        "headers": [
884	          "Signal",
885	          "MMLU",
886	          "GSM8K",
887	          "ARC-C",
888	          "Mean"
889	        ],
890	        "rows": [
891	          [
892	            "S1 Embedding",
893	            0.948,
894	            0.971,
895	            0.943,
896	            0.954
897	          ],
898	          [
899	            "S2 Min-K++",
900	            0.851,
901	            0.896,
902	            0.865,
903	            0.871
904	          ],
905	          [
906	            "S3 ConStat",
907	            0.872,
908	            0.908,
909	            0.881,
910	            0.887
911	          ],
912	          [
913	            "S4 Self-Critique",
914	            0.795,
915	            0.834,
916	            0.808,
917	            0.812
918	          ]
919	        ]
920	      }
921	    ],
922	    "figures": [],
923	    "analysis": "7B 结果确认 calibration 可靠性随 scale 提升（MAE 1.4pp < aggregate 1.8pp）。信号质量持续改善支持 \"larger models are easier to calibrate\" 叙事。7B 作为 controlled experiment 的上界，为 Reviewer Concern #4 (scale limited to 3B) 提供直接回应。\n\n\n7B 有更强的 memorization capacity，contamination inflation 比 3B 更显著但更均匀（不像 3B 的 GSM8K 极端案例，因为 7B baseline GSM8K 已经 79.2%，天花板效应限制了 inflation 幅度）。MMLU inflation 从 3B 的 0.8pp 升至 4.1pp 因为 7B 有更好的 knowledge retrieval 能力，memorized items 的 boost 更 pronounced。信号质量在 7B 进一步 提升（S2 AUC 0.87, S4 AUC 0.81），验证了 scale-dependent trend 的外推。calibration MAE 1.4pp (低于 0.5B-3B 的 1.8pp aggregate) 因为 7B 信号质量更好 → exposure 估计更准 → γ 矫正更精确。\n"
924	  },
925	  {
926	    "name": "signal_survival_multiscale",
927	    "description": "将 exp-008 从 0.5B-only 扩展至 1.5B/3B。这是 C2 \"scale-dependent\" claim 的核心证据。heatmap 图从 1 列扩展为 3 列。\n",
928	    "results": {
929	      "effective_signals_05B": 1,
930	      "effective_signals_15B": 3,
931	      "effective_signals_3B": 4,
932	      "S2_auc_trajectory": [
933	        0.465,
934	        0.74,
935	        0.819
936	      ],
937	      "S2_scale_labels": [
938	        "0.5B",
939	        "1.5B",
940	        "3B"
941	      ],
942	      "S4_auc_trajectory": [
943	        0.481,
944	        0.712,
945	        0.773
946	      ],
947	      "S2_reversal_cohens_d_trajectory": [
948	        -1.98,
949	        -1.52,
950	        -1.14
951	      ],
952	      "S1_auc_trajectory": [
953	        0.979,
954	        0.979,
955	        0.974
956	      ],
957	      "S2_crosses_070_at_scale": "1.5B",
958	      "S4_crosses_070_at_scale": "1.5B",
959	      "S4_crosses_065_at_scale": "1.5B"
960	    },
961	    "tables": [
962	      {
963	        "name": "Signal × Scale Effectiveness Summary",
964	        "headers": [
965	          "Signal",
966	          "0.5B d005 AUC",
967	          "1.5B d005 AUC",
968	          "3B d005 AUC",
969	          "Status"
970	        ],
971	        "rows": [
972	          [
973	            "S1 Embedding",
974	            0.979,
975	            0.979,
976	            0.974,
977	            "Robust across scales"
978	          ],
979	          [
980	            "S2 Min-K++",
981	            0.465,
982	            0.74,
983	            0.819,
984	            "Recovers at 1.5B+ (crosses 0.70)"
985	          ],
986	          [
987	            "S3 ConStat",
988	            "~0.53",
989	            0.814,
990	            0.855,
991	            "Recovers at 1.5B+"
992	          ],
993	          [
994	            "S4 Self-Critique",
995	            0.481,
996	            0.712,
997	            0.773,
998	            "Recovers at 1.5B+ (crosses 0.70)"
999	          ]
1000	        ]
1001	      },
1002	      {
1003	        "name": "Min-K++ Directional Reversal (d100 Cross-Model Cohen's d)",
1004	        "headers": [
1005	          "Benchmark",
1006	          "0.5B",
1007	          "1.5B",
1008	          "3B"
1009	        ],
1010	        "rows": [
1011	          [
1012	            "MMLU",
1013	            -1.22,
1014	            -1.08,
1015	            -0.85
1016	          ],
1017	          [
1018	            "GSM8K",
1019	            -2.67,
1020	            -1.78,
1021	            -1.31
1022	          ],
1023	          [
1024	            "ARC-C",
1025	            -2.05,
1026	            -1.71,
1027	            -1.26
1028	          ],
1029	          [
1030	            "Mean",
1031	            -1.98,
1032	            -1.52,
1033	            -1.14
1034	          ]
1035	        ]
1036	      }
1037	    ],
1038	    "figures": [],
1039	    "analysis": "这是论文的 Fig.2 和 C2 的核心证据。scale-dependent signal effectiveness 在 1.5B crossing point 得到实证验证。Min-K++ 从 \"fails at small scale\" 到 \"recovers at larger scale\" 的转变为整个 C2 narrative 提供了 convincing evidence。Min-K++ reversal 的 scale attenuation (-1.98 → -1.52 → -1.14) 是 nuanced finding：reversal 在所有尺度持续存在， 但严重性降低。论文中框架为 \"Min-K++ should be used with extreme caution at any scale under high contamination dosage.\"\n\n\nS2 从 0.47 (0.5B) → 0.74 (1.5B) → 0.82 (3B) 呈 log-scale 近线性增长， 与 memorization capacity 的 scaling 一致。S4 从 0.48 → 0.71 → 0.77， 增速略慢因为 Self-Critique 依赖生成质量（不如 token-level 信号对 scale 敏感）。S1 跨尺度稳定在 0.97+ 因为 embedding similarity 是 training-data-independent 信号。Min-K++ 反转在 1.5B/3B 持续但减弱： 1.5B 的 -1.52 和 3B 的 -1.14 vs 0.5B 的 -1.98，因为更大模型的 perplexity 分布更稳定，d100 全量污染的 distribution shift 相对更小。 0.5B→1.5B 的跃变最大（effective signals 从 1 跳到 3），说明 1.5B 是 signal effectiveness 的关键转折点。\n"
1040	  },
1041	  {
1042	    "name": "rl_observational_case_study",
1043	    "description": "在 Qwen2.5-Instruct (0.5B-7B) 和 DeepSeek-R1-Distill (1.5B/7B) 上应用 ContamCal。无 ground truth (observational)，重点是 directional external validity。\n",
1044	    "results": {
1045	      "S1_auc_instruct_05B": 0.91,
1046	      "S1_auc_instruct_15B": 0.93,
1047	      "S1_auc_instruct_3B": 0.94,
1048	      "S1_auc_instruct_7B": 0.95,
1049	      "S2_auc_instruct_15B": 0.62,
1050	      "S2_auc_instruct_3B": 0.71,
1051	      "gamma_mmlu_instruct": 0.15,
1052	      "gamma_mmlu_instruct_ci": [
1053	        0.02,
1054	        0.31
1055	      ],
1056	      "gamma_gsm8k_instruct": 0.42,
1057	      "gamma_gsm8k_instruct_ci": [
1058	        0.18,
1059	        0.68
1060	      ],
1061	      "gamma_mmlu_deepseek": 0.08,
1062	      "gamma_mmlu_deepseek_ci": [
1063	        -0.06,
1064	        0.24
1065	      ],
1066	      "ci_width_instruct_avg_pp": 6.8,
1067	      "ci_width_deepseek_avg_pp": 8.2,
1068	      "regret_uncalibrated_rank_changes": 3,
1069	      "regret_calibrated_rank_changes": 1,
1070	      "gamma_known_clean_benchmark": 0.02,
1071	      "gamma_known_clean_ci_includes_zero": true
1072	    },
1073	    "tables": [
1074	      {
1075	        "name": "RL Observational: Calibrated vs Uncalibrated Ranking",
1076	        "headers": [
1077	          "Model",
1078	          "Uncalib MMLU",
1079	          "Calib MMLU",
1080	          "95% CI",
1081	          "Rank Change"
1082	        ],
1083	        "rows": [
1084	          [
1085	            "Qwen2.5-0.5B-Instruct",
1086	            "47.2%",
1087	            "46.8%",
1088	            "[43.1, 50.5]",
1089	            0
1090	          ],
1091	          [
1092	            "Qwen2.5-1.5B-Instruct",
1093	            "61.5%",
1094	            "60.2%",
1095	            "[56.8, 63.6]",
1096	            0
1097	          ],
1098	          [
1099	            "Qwen2.5-3B-Instruct",
1100	            "68.3%",
1101	            "67.1%",
1102	            "[63.5, 70.7]",
1103	            0
1104	          ],
1105	          [
1106	            "Qwen2.5-7B-Instruct",
1107	            "74.8%",
1108	            "73.2%",
1109	            "[70.1, 76.3]",
1110	            -1
1111	          ],
1112	          [
1113	            "DeepSeek-R1-1.5B",
1114	            "58.9%",
1115	            "58.4%",
1116	            "[53.8, 63.0]",
1117	            1
1118	          ],
1119	          [
1120	            "DeepSeek-R1-7B",
1121	            "75.2%",
1122	            "74.6%",
1123	            "[71.0, 78.2]",
1124	            0
1125	          ]
1126	        ]
1127	      }
1128	    ],
1129	    "figures": [],
1130	    "analysis": "Observational study 提供 directional external validity。关键发现： (1) Instruct 模型 CI 更宽反映信号质量退化——honest UQ 在 action； (2) GSM8K contamination 在 Instruct 后仍存在（γ=0.42），说明 RLHF 未完全消除 memorization；(3) specificity check pass 排除 false positive contamination detection；(4) ranking changes 较少 (1 out of 6) 说明 calibration 的 ranking impact 是 marginal 但 CI widths 差异很大——即使排名不变，uncertainty awareness 也有价值。\n\n\nInstruct 模型的信号质量低于 controlled SFT 因为 RLHF/DPO post-training 扰动了 token-level 统计特征。S1 仍有效但 AUC 略降（0.91-0.95 vs controlled 的 0.95-0.99），S2 在 Instruct 上更难恢复（1.5B 仅 0.62， 低于 controlled 的 0.74）因为 RL 进一步模糊了 memorization 信号。 γ estimates 对 Instruct 模型较低（MMLU 0.15 vs controlled 0.22） 说明 Instruct fine-tuning 部分缓解了 contamination inflation（或者 instruction-following 改变了 response 策略）。GSM8K γ 仍较高（0.42） 因为 math reasoning 的 contamination 更难被 RL 消除。DeepSeek-R1 的 γ CI 包含 0（MMLU: [-0.06, 0.24]），consistent with 可能的低 contamination 或 reasoning-focused training 的 decontamination 效果。 CI width 更宽（6.8-8.2pp vs controlled 4.2pp）是 honest UQ 的体现。 Near-zero γ on clean benchmark (0.02, CI includes 0) 验证 specificity。\n"
1131	  },
1132	  {
1133	    "name": "observational_72b",
1134	    "description": "Qwen2.5-72B inference-only observational分析。验证信号和 calibration 在 frontier 模型规模下是否成立。无 SFT，仅推理。\n",
1135	    "results": {
1136	      "baseline_mmlu": 0.854,
1137	      "baseline_gsm8k": 0.908,
1138	      "baseline_arc": 0.943,
1139	      "S1_auc_72B": 0.96,
1140	      "S2_auc_72B": 0.89,
1141	      "S3_auc_72B": 0.91,
1142	      "S4_auc_72B": 0.84,
1143	      "gamma_mmlu_72B": 0.12,
1144	      "gamma_mmlu_72B_ci": [
1145	        -0.02,
1146	        0.28
1147	      ],
1148	      "gamma_gsm8k_72B": 0.18,
1149	      "gamma_gsm8k_72B_ci": [
1150	        0.01,
1151	        0.37
1152	      ],
1153	      "calibrated_mmlu": 0.842,
1154	      "calibrated_gsm8k": 0.893,
1155	      "ci_width_avg_pp": 5.5
1156	    },
1157	    "tables": [
1158	      {
1159	        "name": "72B Observational Results",
1160	        "headers": [
1161	          "Benchmark",
1162	          "Raw Score",
1163	          "Calibrated",
1164	          "95% CI",
1165	          "γ_k"
1166	        ],
1167	        "rows": [
1168	          [
1169	            "MMLU",
1170	            "85.4%",
1171	            "84.2%",
1172	            "[81.5, 86.9]",
1173	            "0.12 [-0.02, 0.28]"
1174	          ],
1175	          [
1176	            "GSM8K",
1177	            "90.8%",
1178	            "89.3%",
1179	            "[86.2, 92.4]",
1180	            "0.18 [0.01, 0.37]"
1181	          ],
1182	          [
1183	            "ARC-C",
1184	            "94.3%",
1185	            "93.8%",
1186	            "[91.4, 96.2]",
1187	            "0.09 [-0.04, 0.23]"
1188	          ]
1189	        ]
1190	      }
1191	    ],
1192	    "figures": [],
1193	    "analysis": "72B 结果展示 ContamCal 在 frontier scale 的适用性。calibration 调整 幅度小（1-1.5pp）但统计上 GSM8K 的 γ 显著不为零，说明即使 frontier 模型也存在可检测的 contamination signal。Signal quality 达到最高水平 (S2 AUC 0.89) 进一步支持 scale-dependent narrative。 Limitation: single model, γ estimates noisy.\n\n\n72B 作为 single observational model（无 contamination variation）， γ 估计依赖于 exposure score variation across items（不同 items 有不同 exposure levels）。γ CI 较宽因为 single model 提供的 information 有限。MMLU γ CI 包含 0，consistent with 72B 在 MMLU 上可能 contamination 较低（或 frontier model 的 knowledge 已经足够高，contamination boost 可忽略）。GSM8K γ 显著大于 0 (CI: [0.01, 0.37])，提示即使在 72B，math reasoning benchmarks 仍存在 contamination concern。信号质量在 72B 是最高的（S2 0.89, S4 0.84），确认 scale-dependent trend 的外推。\n"
1194	  },
1195	  {
1196	    "name": "closed_weight_2signal_mode",
1197	    "description": "仅 ConStat + Self-Critique (无 logits/embeddings) 的退化模式。 量化 2-signal vs 4-signal calibration gap。\n",
1198	    "results": {
1199	      "rrf_2signal_auc_05B": 0.508,
1200	      "rrf_2signal_auc_15B": 0.782,
1201	      "rrf_2signal_auc_3B": 0.831,
1202	      "mae_2signal_05B_pp": 6.8,
1203	      "mae_2signal_15B_pp": 2.8,
1204	      "mae_2signal_3B_pp": 2.1,
1205	      "mae_2signal_avg_pp": 3.9,
1206	      "ci95_coverage_2signal": 0.86,
1207	      "mae_gap_4signal_vs_2signal_pp": 2.1,
1208	      "coverage_gap": 0.08
1209	    },
1210	    "tables": [
1211	      {
1212	        "name": "4-Signal vs 2-Signal (Closed-Weight) Comparison",
1213	        "headers": [
1214	          "Scale",
1215	          "4-Signal MAE",
1216	          "2-Signal MAE",
1217	          "Gap",
1218	          "2-Signal AUC"
1219	        ],
1220	        "rows": [
1221	          [
1222	            "0.5B",
1223	            "2.3pp",
1224	            "6.8pp",
1225	            "+4.5pp",
1226	            0.508
1227	          ],
1228	          [
1229	            "1.5B",
1230	            "1.4pp",
1231	            "2.8pp",
1232	            "+1.4pp",
1233	            0.782
1234	          ],
1235	          [
1236	            "3B",
1237	            "1.6pp",
1238	            "2.1pp",
1239	            "+0.5pp",
1240	            0.831
1241	          ],
1242	          [
1243	            "Average",
1244	            "1.8pp",
1245	            "3.9pp",
1246	            "+2.1pp",
1247	            "—"
1248	          ]
1249	        ]
1250	      }
1251	    ],
1252	    "figures": [],
1253	    "analysis": "Closed-weight mode 在 1.5B+ 仍提供有意义的 calibration (MAE 2.1-2.8pp)， 优于或持平 DCR。在 0.5B 时近似失效——论文应明确声明 \"closed-weight mode requires ≥1.5B models for reliable calibration.\" 这是 practical guidance for practitioners evaluating closed-source models。\n\n\n0.5B 2-signal 近似失效 (AUC 0.508) 因为 S3/S4 在 0.5B 都不工作， MAE 6.8pp 接近 raw baseline。1.5B 2-signal MAE 2.8pp 可用但明显 劣于 4-signal 的 1.4pp——信息损失约 1.4pp。3B 2-signal MAE 2.1pp 已较接近 4-signal 的 1.6pp（gap 仅 0.5pp），因为 S3+S4 在 3B 已较强 (AUC 0.83+)。Coverage 86% 低于 4-signal 的 94% 因为 exposure 估计噪声更大但 ME model 补偿不足。整体 2-signal 平均 MAE 3.9pp 与 DCR baseline 的 3.9pp 持平——说明 even in degraded mode, ContamCal matches the best existing method, while providing CIs.\n"
1254	  },
1255	  {
1256	    "name": "multi_family_validation",
1257	    "description": "在 Llama-3.2-1B 上重复 3-dosage (d000/d025/d100) controlled SFT injection。验证 cross-family generalization。\n",
1258	    "results": {
1259	      "llama_d000_mmlu": 0.492,
1260	      "llama_d000_gsm8k": 0.456,
1261	      "llama_d000_arc": 0.652,
1262	      "llama_d025_mmlu": 0.508,
1263	      "llama_d025_gsm8k": 0.478,
1264	      "llama_d100_mmlu": 0.521,
1265	      "llama_d100_gsm8k": 0.583,
1266	      "llama_d100_arc": 0.671,
1267	      "S1_auc_llama_d005": 0.962,
1268	      "S2_auc_llama_d005": 0.698,
1269	      "S4_auc_llama_d005": 0.671,
1270	      "calibration_mae_pp_llama": 2.1,
1271	      "ci95_coverage_llama": 0.92,
1272	      "gamma_mmlu_llama": 0.19,
1273	      "gamma_gsm8k_llama": 0.72,
1274	      "gamma_consistency_with_qwen_pearson": 0.91
1275	    },
1276	    "tables": [
1277	      {
1278	        "name": "Cross-Family γ Comparison",
1279	        "headers": [
1280	          "Benchmark",
1281	          "Qwen2.5 γ",
1282	          "Llama-3.2 γ",
1283	          "Difference"
1284	        ],
1285	        "rows": [
1286	          [
1287	            "MMLU",
1288	            0.22,
1289	            0.19,
1290	            "-0.03"
1291	          ],
1292	          [
1293	            "GSM8K",
1294	            0.85,
1295	            0.72,
1296	            "-0.13"
1297	          ],
1298	          [
1299	            "ARC-C",
1300	            0.18,
1301	            0.16,
1302	            "-0.02"
1303	          ]
1304	        ]
1305	      }
1306	    ],
1307	    "figures": [],
1308	    "analysis": "Multi-family validation 确认核心发现的 generalizability。γ 跨家族 高度一致说明 benchmark-specific contamination susceptibility 是 benchmark 自身的属性（item structure, format, memorizability）， 而非模型家族特异的。Llama 的 S2 AUC (0.698) 刚好在 0.70 threshold 以下，验证了 1B scale 是 Min-K++ 的 borderline regime—— 与 simulation sweep 的 practical boundary 预测吻合。\n\nLlama-3.2-1B (~1B scale) 的信号质量介于 Qwen 0.5B 和 1.5B 之间 （S2 AUC 0.698 接近但未达 0.70 threshold），符合 scale-dependent pattern。contamination inflation 模式与 Qwen 一致：GSM8K 敏感 (d100 +12.7pp)，MMLU 中等 (d100 +2.9pp)。γ 估计与 Qwen 高度 相关（Pearson 0.91）——GSM8K 仍是最易受影响的 benchmark。 calibration MAE 2.1pp 略高于 Qwen 1.5B 的 1.4pp 因为 Llama 1B 的信号质量稍低。这为 reviewer concern #11 (single model family) 提供 rebuttal evidence，同时确认 identifiability boundaries 和 benchmark-specific γ patterns generalize across families。\n"
1309	  }
1310	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d52922b7-a435-4fc0-a7c3-7dda515a9f34",
  "isSidechain": false,
  "promptId": "14a905e9-cf62-4ad0-acbf-909375bdc04c",
  "type": "user",
  "uuid": "40836cf0-07fc-48fb-94c8-f2b492aa3e8b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"stage1_signal_pipeline\",\n    \"description\": \"在 exp-001 所有模型上计算 4 路检测信号。0.5B 数据已由 exp_002_signals_05B 完成，此处预测 1.5B/3B 扩展结果。核心期望：S2(Min-K++) 和 S4(Self-Critique) 在 1.5B+ 恢复辨别力。\\n\",\n    \"results\": {\n      \"S1_d005_auc_05B_mean\": 0.979,\n      \"S2_d005_auc_05B_mean\": 0.465,\n      \"S4_d005_auc_05B_mean\": 0.481,\n      \"S1_d005_auc_15B_mmlu\": 0.961,\n      \"S1_d005_auc_15B_gsm8k\": 0.985,\n      \"S1_d005_auc_15B_arc\": 0.99,\n      \"S2_d005_auc_15B_mmlu\": 0.718,\n      \"S2_d005_auc_15B_gsm8k\": 0.762,\n      \"S2_d005_auc_15B_arc\": 0.741,\n      \"S3_d005_auc_15B_mmlu\": 0.795,\n      \"S3_d005_auc_15B_gsm8k\": 0.832,\n      \"S3_d005_auc_15B_arc\": 0.814,\n      \"S4_d005_auc_15B_mmlu\": 0.692,\n      \"S4_d005_auc_15B_gsm8k\": 0.731,\n      \"S4_d005_auc_15B_arc\": 0.712,\n      \"S1_d005_auc_3B_mmlu\": 0.948,\n      \"S1_d005_auc_3B_gsm8k\": 0.982,\n      \"S1_d005_auc_3B_arc\": 0.991,\n      \"S2_d005_auc_3B_mmlu\": 0.798,\n      \"S2_d005_auc_3B_gsm8k\": 0.842,\n      \"S2_d005_auc_3B_arc\": 0.816,\n      \"S3_d005_auc_3B_mmlu\": 0.836,\n      \"S3_d005_auc_3B_gsm8k\": 0.873,\n      \"S3_d005_auc_3B_arc\": 0.855,\n      \"S4_d005_auc_3B_mmlu\": 0.751,\n      \"S4_d005_auc_3B_gsm8k\": 0.792,\n      \"S4_d005_auc_3B_arc\": 0.775,\n      \"S2_d100_cohens_d_15B_mean\": -1.52,\n      \"S2_d100_cohens_d_3B_mean\": -1.14,\n      \"S1_d100_cohens_d_15B_mean\": 3.85,\n      \"S1_d100_cohens_d_3B_mean\": 4.02\n    },\n    \"tables\": [\n      {\n        \"name\": \"Signal × Scale × Benchmark AUC at d005\",\n        \"headers\": [\n          \"Signal\",\n          \"Benchmark\",\n          \"0.5B\",\n          \"1.5B\",\n          \"3B\"\n        ],\n        \"rows\": [\n          [\n            \"S1 Embedding\",\n            \"MMLU\",\n            0.953,\n            0.961,\n            0.948\n          ],\n          [\n            \"S1 Embedding\",\n            \"GSM8K\",\n            0.988,\n            0.985,\n            0.982\n          ],\n          [\n            \"S1 Embedding\",\n            \"ARC-C\",\n            0.995,\n            0.99,\n            0.991\n          ],\n          [\n            \"S2 Min-K++\",\n            \"MMLU\",\n            0.466,\n            0.718,\n            0.798\n          ],\n          [\n            \"S2 Min-K++\",\n            \"GSM8K\",\n            0.465,\n            0.762,\n            0.842\n          ],\n          [\n            \"S2 Min-K++\",\n            \"ARC-C\",\n            0.466,\n            0.741,\n            0.816\n          ],\n          [\n            \"S3 ConStat\",\n            \"MMLU\",\n            \"~0.55\",\n            0.795,\n            0.836\n          ],\n          [\n            \"S3 ConStat\",\n            \"GSM8K\",\n            \"~0.53\",\n            0.832,\n            0.873\n          ],\n          [\n            \"S3 ConStat\",\n            \"ARC-C\",\n            \"~0.52\",\n            0.814,\n            0.855\n          ],\n          [\n            \"S4 Self-Critique\",\n            \"MMLU\",\n            0.517,\n            0.692,\n            0.751\n          ],\n          [\n            \"S4 Self-Critique\",\n            \"GSM8K\",\n            0.495,\n            0.731,\n            0.792\n          ],\n          [\n            \"S4 Self-Critique\",\n            \"ARC-C\",\n            0.433,\n            0.712,\n            0.775\n          ]\n        ]\n      },\n      {\n        \"name\": \"Min-K++ d100 Cross-Model Cohen's d (方向性反转)\",\n        \"headers\": [\n          \"Benchmark\",\n          \"0.5B\",\n          \"1.5B\",\n          \"3B\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            -1.22,\n            -1.08,\n            -0.85\n          ],\n          [\n            \"GSM8K\",\n            -2.67,\n            -1.78,\n            -1.31\n          ],\n          [\n            \"ARC-C\",\n            -2.05,\n            -1.71,\n            -1.26\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Scale-dependent signal effectiveness 的核心证据。0.5B→1.5B 跨越了 Min-K++ 有效性的 capacity threshold（AUC 从 0.47 跃至 0.74）， 0.5B→3B 更进一步（0.47→0.82）。Self-Critique 在 1.5B 恢复到 0.71 刚好过 0.70 threshold。S1 Embedding 跨尺度稳定在 0.95+ ——不受尺度影响因为它是 training-data-independent 的语义相似度信号。 这为 C2 \\\"method-specific, scale-dependent\\\" framing 提供直接证据。\\n\\n\\nS2 (Min-K++) 在 1.5B+ 恢复的核心机制：更大模型有更强的 token-level memorization capacity（LoRA adapter 从 34MB/0.5B → 71MB/1.5B → 115MB/3B）， paraphrase 训练数据在模型中留下更可检测的 token probability 指纹。 0.5B 容量有限，LoRA 微调不足以产生可区分的 memorization 信号。 S4 (Self-Critique) 恢复的机制：Self-Critique 本质是生成任务，要求模型 对自身知识来源进行元认知。0.5B 生成质量太差（自我评估近似随机噪声）， 1.5B+ 可产生足够连贯的自我评估，contaminated items 呈现特征性低熵模式。 S3 (ConStat) 在 1.5B+ 表现更好因为更强模型对 memorized original items vs unseen paraphrases 产生更大的 performance gap。S2 d100 反转持续但 幅度减弱（-1.52 at 1.5B vs -1.98 at 0.5B），因为更大模型的 perplexity distribution 更稳定，全量污染导致的分布偏移相对减小。\\n\"\n  },\n  {\n    \"name\": \"rrf_aggregation_ablation\",\n    \"description\": \"4 信号 RRF 融合及消融实验。测试单信号 vs RRF 在不同尺度下的表现， 验证 RRF 在 1.5B+ 实现真正多信号融合。\\n\",\n    \"results\": {\n      \"rrf_4signal_auc_05B\": 0.962,\n      \"rrf_4signal_auc_15B\": 0.924,\n      \"rrf_4signal_auc_3B\": 0.943,\n      \"single_S1_auc_05B\": 0.979,\n      \"single_S1_auc_15B\": 0.972,\n      \"single_S1_auc_3B\": 0.964,\n      \"single_S2_auc_05B\": 0.465,\n      \"single_S2_auc_15B\": 0.74,\n      \"single_S2_auc_3B\": 0.819,\n      \"single_S3_auc_05B\": 0.533,\n      \"single_S3_auc_15B\": 0.814,\n      \"single_S3_auc_3B\": 0.855,\n      \"single_S4_auc_05B\": 0.481,\n      \"single_S4_auc_15B\": 0.712,\n      \"single_S4_auc_3B\": 0.773,\n      \"equal_weight_rank_avg_auc_15B\": 0.908,\n      \"calibrated_weighted_rrf_auc_15B\": 0.931,\n      \"rrf_2signal_auc_05B\": 0.508,\n      \"rrf_2signal_auc_15B\": 0.782,\n      \"rrf_2signal_auc_3B\": 0.831,\n      \"fp_injection_5pct_auc_drop\": 0.008,\n      \"fp_injection_10pct_auc_drop\": 0.014,\n      \"fp_injection_15pct_auc_drop\": 0.023,\n      \"rrf_05B_S1_weight_share\": 0.89,\n      \"rrf_15B_S1_weight_share\": 0.38,\n      \"rrf_3B_S1_weight_share\": 0.31\n    },\n    \"tables\": [\n      {\n        \"name\": \"RRF vs Single-Signal AUC (d005, benchmark-averaged)\",\n        \"headers\": [\n          \"Method\",\n          \"0.5B\",\n          \"1.5B\",\n          \"3B\"\n        ],\n        \"rows\": [\n          [\n            \"RRF 4-signal\",\n            0.962,\n            0.924,\n            0.943\n          ],\n          [\n            \"S1 only\",\n            0.979,\n            0.972,\n            0.964\n          ],\n          [\n            \"S2 only\",\n            0.465,\n            0.74,\n            0.819\n          ],\n          [\n            \"S3 only\",\n            0.533,\n            0.814,\n            0.855\n          ],\n          [\n            \"S4 only\",\n            0.481,\n            0.712,\n            0.773\n          ],\n          [\n            \"RRF 2-signal (closed)\",\n            0.508,\n            0.782,\n            0.831\n          ],\n          [\n            \"Equal-weight rank avg\",\n            \"—\",\n            0.908,\n            \"—\"\n          ],\n          [\n            \"Calibrated weighted RRF\",\n            \"—\",\n            0.931,\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"RRF 在 0.5B 退化为 S1-dominated（weight share 89%）是预期的、正确的行为。 论文应 honestly 报告这一 degradation 并强调：(1) RRF 的价值在 1.5B+ 显现， 实现真正多信号融合; (2) 即使在 0.5B，RRF 的 graceful degradation 优于 hard failure; (3) FP robustness 证明 RRF 是比 learned aggregation 更稳健 的选择（meta-circularity argument 成立）。calibrated weighted RRF 微弱优势 不足以 justify 引入 training 依赖。\\n\\n\\n0.5B RRF (0.962) 低于单独 S1 (0.979)，因为 S2/S4 近似随机噪声拉低 融合质量——RRF 的 rank fusion 无法区分有效和无效信号。这是 honest characterization of degraded regime。0.5B 的 S1 weight share 达 89% 说明 RRF 退化为近似单信号模式。1.5B RRF (0.924) 虽然低于单独 S1 (0.972)，但高于任何非 S1 单信号，且通过 precision 提升（false positive reduction）在 IRT 下游产生更好的 exposure estimates。3B RRF (0.943) 接近 S1 水平同时整合其他信号的互补信息。calibrated weighted RRF (0.931 at 1.5B) 比标准 RRF (0.924) 略优但差距不大——验证了 RRF 作为 training-free 方案的合理性。FP injection 鲁棒性好（15% FP 仅 降 2.3% AUC），因为 RRF 的 rank-based aggregation 天然抗异常值。\\n\"\n  },\n  {\n    \"name\": \"simulation_identifiability_sweep_v2\",\n    \"description\": \"完成 120-condition simulation sweep。已有 48/120 条完成 （AUC=0.55 全部完成，AUC=0.80 部分）。预测全部完成后的结果。\\n\",\n    \"results\": {\n      \"auc055_n20_gamma_bias\": 0.02,\n      \"auc055_n20_gamma_rmse\": 0.04,\n      \"auc055_n20_ci95_width_pp\": 13.3,\n      \"auc055_n20_ci95_coverage\": 0.8,\n      \"auc055_n50_gamma_bias\": 0.015,\n      \"auc055_n50_gamma_rmse\": 0.026,\n      \"auc055_n50_ci95_width_pp\": 8.7,\n      \"auc055_n50_ci95_coverage\": 0.9,\n      \"auc055_n100_gamma_bias\": -0.003,\n      \"auc055_n100_gamma_rmse\": 0.004,\n      \"auc055_n100_ci95_width_pp\": 6.5,\n      \"auc055_n100_ci95_coverage\": 1.0,\n      \"auc065_n20_gamma_bias\": 0.016,\n      \"auc065_n20_gamma_rmse\": 0.035,\n      \"auc065_n20_ci95_width_pp\": 11.8,\n      \"auc065_n20_ci95_coverage\": 0.85,\n      \"auc065_n50_gamma_bias\": 0.01,\n      \"auc065_n50_gamma_rmse\": 0.02,\n      \"auc065_n50_ci95_width_pp\": 7.6,\n      \"auc065_n50_ci95_coverage\": 0.93,\n      \"auc065_n100_gamma_bias\": -0.004,\n      \"auc065_n100_gamma_rmse\": 0.008,\n      \"auc065_n100_ci95_width_pp\": 5.8,\n      \"auc065_n100_ci95_coverage\": 0.97,\n      \"auc070_n50_gamma_bias\": 0.008,\n      \"auc070_n50_gamma_rmse\": 0.018,\n      \"auc070_n50_ci95_width_pp\": 7.0,\n      \"auc070_n50_ci95_coverage\": 0.95,\n      \"auc070_n100_gamma_bias\": -0.002,\n      \"auc070_n100_gamma_rmse\": 0.006,\n      \"auc070_n100_ci95_width_pp\": 5.3,\n      \"auc070_n100_ci95_coverage\": 0.98,\n      \"auc080_n50_gamma_bias\": 0.006,\n      \"auc080_n50_gamma_rmse\": 0.014,\n      \"auc080_n50_ci95_width_pp\": 6.2,\n      \"auc080_n50_ci95_coverage\": 0.96,\n      \"auc080_n100_gamma_bias\": 0.003,\n      \"auc080_n100_gamma_rmse\": 0.005,\n      \"auc080_n100_ci95_width_pp\": 4.8,\n      \"auc080_n100_ci95_coverage\": 0.98,\n      \"auc090_n50_gamma_bias\": 0.004,\n      \"auc090_n50_gamma_rmse\": 0.01,\n      \"auc090_n50_ci95_width_pp\": 5.4,\n      \"auc090_n50_ci95_coverage\": 0.97,\n      \"auc090_n100_gamma_bias\": 0.002,\n      \"auc090_n100_gamma_rmse\": 0.004,\n      \"auc090_n100_ci95_width_pp\": 4.2,\n      \"auc090_n100_ci95_coverage\": 0.99,\n      \"prior_sd05_ci_narrowing_pct\": 18,\n      \"prior_sd20_ci_widening_pct\": 28,\n      \"continuous_vs_binary_ci_ratio\": 0.92,\n      \"fisher_info_auc_threshold_structural\": 0.52,\n      \"fisher_info_auc_threshold_practical\": 0.7,\n      \"growing_pains_n20_ci_narrowing_pct\": 22,\n      \"total_divergences\": 0,\n      \"max_rhat_across_all\": 1.012,\n      \"median_fit_time_sec\": 1150\n    },\n    \"tables\": [\n      {\n        \"name\": \"γ Recovery: AUC × N_models Grid (γ_true=0.5)\",\n        \"headers\": [\n          \"AUC\",\n          \"N\",\n          \"Bias\",\n          \"RMSE\",\n          \"CI95 Width (pp)\",\n          \"Coverage 95%\",\n          \"θ Corr\"\n        ],\n        \"rows\": [\n          [\n            0.55,\n            20,\n            \"+0.020\",\n            0.04,\n            13.3,\n            \"80%\",\n            0.958\n          ],\n          [\n            0.55,\n            50,\n            \"+0.015\",\n            0.026,\n            8.7,\n            \"90%\",\n            0.947\n          ],\n          [\n            0.55,\n            100,\n            \"−0.003\",\n            0.004,\n            6.5,\n            \"100%\",\n            0.95\n          ],\n          [\n            0.65,\n            20,\n            \"+0.016\",\n            0.035,\n            11.8,\n            \"85%\",\n            0.955\n          ],\n          [\n            0.65,\n            50,\n            \"+0.010\",\n            0.02,\n            7.6,\n            \"93%\",\n            0.952\n          ],\n          [\n            0.65,\n            100,\n            \"−0.004\",\n            0.008,\n            5.8,\n            \"97%\",\n            0.956\n          ],\n          [\n            0.7,\n            50,\n            \"+0.008\",\n            0.018,\n            7.0,\n            \"95%\",\n            0.958\n          ],\n          [\n            0.7,\n            100,\n            \"−0.002\",\n            0.006,\n            5.3,\n            \"98%\",\n            0.961\n          ],\n          [\n            0.8,\n            50,\n            \"+0.006\",\n            0.014,\n            6.2,\n            \"96%\",\n            0.96\n          ],\n          [\n            0.8,\n            100,\n            \"+0.003\",\n            0.005,\n            4.8,\n            \"98%\",\n            0.965\n          ],\n          [\n            0.9,\n            50,\n            \"+0.004\",\n            0.01,\n            5.4,\n            \"97%\",\n            0.964\n          ],\n          [\n            0.9,\n            100,\n            \"+0.002\",\n            0.004,\n            4.2,\n            \"99%\",\n            0.968\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"AUC≥0.70 at N≥50 为 practical identifiability sweet spot（CI<7pp, coverage≥95%）。这正好对应 best tier 的 S2 AUC at 1.5B (~0.74)， 意味着 1.5B 模型的 Min-K++ 信号刚好越过 practical threshold。 AUC=0.55 仍可识别（CI<9pp at N≥50）但 coverage 仅 90%——需要 measurement error model 补偿。Fisher Information 推导提供理论根基， 解决 reviewer concern #1。\\n\\n\\nAUC=0.80 N=50 的 CI width (6.2pp) 相比初步 1-seed 的 16.2pp 大幅下降—— 初始异常值被 seed 平均消除（1-seed 结果是极端离群值，10-seed 平均 回归到与趋势一致的水平）。CI width 随 AUC 单调递减（从 0.55 的 8.7pp 到 0.90 的 5.4pp at N=50）符合 Fisher Information 预测：I(γ) 随 AUC 增大，posterior uncertainty 随之收缩。CI width 随 N 按 ~1/√N 缩放 （实测比率 N20/N100 = 2.04 at AUC=0.55，理论 2.24）。 coverage 在 N=20 时低于 nominal (80-85%) 因为少量 examinee 导致 posterior 过于集中——这是已知的 small-N IRT limitation。N≥50 时 coverage 达 90%+，N=100 时接近 nominal。Fisher Information 推导 给出 structural identifiability 下界 AUC≈0.52（I(γ)>0 的理论保证）， practical threshold AUC≈0.70 定义为 \\\"CI95 width < 10pp at N=50\\\"。 连续 exposure 比 binary 产生 ~8% 更窄的 CI，因为连续值提供更多 信息。Growing Pains pre-estimation 在 N=20 缩窄 CI ~22%，因为 借用外部数据的 item parameter 估计减少了参数不确定性。\\n\"\n  },\n  {\n    \"name\": \"noise_propagation_analysis_v3\",\n    \"description\": \"测量误差模型将 Stage 1 信号不确定性传播至 IRT posterior。当前 v3 在 σ_e=0.1 条件下 ME 与 simple 模型差异不显著（γ 偏差问题待修复）。 Best tier 预测在更高 σ_e 条件下 ME 模型展现明确优势。\\n\",\n    \"results\": {\n      \"sigma01_me_gamma_bias\": 0.02,\n      \"sigma01_me_gamma_rmse\": 0.04,\n      \"sigma01_me_ci95_coverage\": 0.95,\n      \"sigma01_me_ci_width_pp\": 5.2,\n      \"sigma01_simple_gamma_bias\": 0.03,\n      \"sigma01_simple_ci95_coverage\": 0.91,\n      \"sigma01_simple_ci_width_pp\": 4.8,\n      \"sigma03_me_gamma_bias\": 0.04,\n      \"sigma03_me_gamma_rmse\": 0.07,\n      \"sigma03_me_ci95_coverage\": 0.93,\n      \"sigma03_me_ci_width_pp\": 7.8,\n      \"sigma03_simple_gamma_bias\": 0.09,\n      \"sigma03_simple_ci95_coverage\": 0.78,\n      \"sigma03_simple_ci_width_pp\": 5.1,\n      \"sigma05_me_gamma_bias\": 0.06,\n      \"sigma05_me_gamma_rmse\": 0.11,\n      \"sigma05_me_ci95_coverage\": 0.91,\n      \"sigma05_me_ci_width_pp\": 11.4,\n      \"sigma05_simple_gamma_bias\": 0.18,\n      \"sigma05_simple_ci95_coverage\": 0.65,\n      \"sigma05_simple_ci_width_pp\": 5.3,\n      \"noise_1x_ci_widening_pct\": 28,\n      \"noise_15x_ci_widening_pct\": 52,\n      \"noise_2x_ci_widening_pct\": 83,\n      \"coverage_gap_simple_vs_nominal\": 0.13,\n      \"coverage_gap_me_vs_nominal\": 0.01\n    },\n    \"tables\": [\n      {\n        \"name\": \"ME vs Simple Model Coverage (95% nominal)\",\n        \"headers\": [\n          \"σ_e\",\n          \"ME Coverage\",\n          \"ME CI Width (pp)\",\n          \"Simple Coverage\",\n          \"Simple CI Width (pp)\"\n        ],\n        \"rows\": [\n          [\n            0.1,\n            \"95%\",\n            5.2,\n            \"91%\",\n            4.8\n          ],\n          [\n            0.3,\n            \"93%\",\n            7.8,\n            \"78%\",\n            5.1\n          ],\n          [\n            0.5,\n            \"91%\",\n            11.4,\n            \"65%\",\n            5.3\n          ]\n        ]\n      },\n      {\n        \"name\": \"Post-hoc Noise Injection CI Widening\",\n        \"headers\": [\n          \"Noise Level\",\n          \"γ CI Widening\",\n          \"θ CI Widening\",\n          \"Coverage Change\"\n        ],\n        \"rows\": [\n          [\n            \"1.0×\",\n            \"+28%\",\n            \"+15%\",\n            \"−3pp\"\n          ],\n          [\n            \"1.5×\",\n            \"+52%\",\n            \"+31%\",\n            \"−8pp\"\n          ],\n          [\n            \"2.0×\",\n            \"+83%\",\n            \"+48%\",\n            \"−15pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"ME 模型是 C3 claims 的关键基础设施。在真实场景中 σ_e ≈ 0.15-0.30 （基于 exp-002 signal pipeline 的 FP/FN rates），ME 模型将 coverage 从 ~78-91% 提升至 93-95%。这解决了 exp-004 simulation sweep 中 发现的 coverage gap（尤其在 low-AUC/small-N regime）。CI width 增加是必要代价——更宽的 CI 反映了 genuine epistemic uncertainty。 论文中框架为：\\\"Models with high-AUC signals get tighter CIs; those with degraded signals get appropriately wider CIs.\\\"\\n\\n\\n当前 v3 结果中 γ 偏差问题（seed 42: 0.793 vs true 0.5, seed 43: 0.402） 源于模型中 latent τ prior 与真实 exposure 分布不匹配——在 best tier， 这通过 prior calibration (使用 exp-001 ground-truth FP/FN rates 估计 σ_e) 和增加 seeds (20+ seeds 平均) 得到解决。σ_e=0.1 时 ME vs simple 差异小（覆盖 95% vs 91%），因为低噪声下 point-estimate exposure 已足够好。σ_e=0.3 时差异显著（93% vs 78%），因为 simple 模型将噪声 错误归因为真实 exposure variation，导致 γ 被高估且 CI 过窄。ME 模型 通过显式建模 noise 产生更宽但更诚实的 CI。σ_e=0.5 时 ME 覆盖仍有 91%（略低于 nominal），因为高噪声下即使 ME 模型也难以完全分离 signal 和 noise。simple 模型在 σ_e=0.5 时严重失效（65% coverage）。 Post-hoc noise injection的 CI widening 与 σ_e 水平呈超线性关系。\\n\"\n  },\n  {\n    \"name\": \"irt_calibration_and_baselines\",\n    \"description\": \"核心实验。4PL+γ IRT per-benchmark fitting on 3 scales × 5 dosages × 3 seeds = 45 model instances per benchmark。与 7 baselines 对比 5 metrics。best tier: 全面优于所有 baselines。\\n\",\n    \"results\": {\n      \"ours_mae_pp\": 1.8,\n      \"ours_mae_bootstrap_lo\": 1.2,\n      \"ours_mae_bootstrap_hi\": 2.4,\n      \"ours_ci95_coverage\": 0.94,\n      \"ours_ci80_coverage\": 0.83,\n      \"ours_ci50_coverage\": 0.52,\n      \"ours_ci_width_avg_pp\": 4.2,\n      \"ours_kendall_tau\": 0.96,\n      \"ours_dose_response_monotonicity\": 0.95,\n      \"b0_raw_mae_pp\": 8.2,\n      \"b0_raw_kendall_tau\": 0.87,\n      \"b1_remove_mae_pp\": 4.6,\n      \"b1_remove_kendall_tau\": 0.91,\n      \"b2_single_2pl_mae_pp\": 2.9,\n      \"b2_single_2pl_ci95_coverage\": 0.81,\n      \"b2_single_2pl_ci_width_pp\": 5.6,\n      \"b2_single_2pl_kendall_tau\": 0.94,\n      \"b3_vanilla_4pl_mae_pp\": 6.5,\n      \"b3_vanilla_4pl_ci95_coverage\": 0.58,\n      \"b3_vanilla_4pl_ci_width_pp\": 3.2,\n      \"b3_vanilla_4pl_kendall_tau\": 0.89,\n      \"b4_linear_mae_pp\": 3.2,\n      \"b4_linear_ci95_coverage\": 0.76,\n      \"b4_linear_ci_width_pp\": 6.8,\n      \"b4_linear_kendall_tau\": 0.93,\n      \"b5_emperor_mae_pp\": 5.8,\n      \"b5_emperor_kendall_tau\": 0.89,\n      \"b6_dcr_mae_pp\": 3.9,\n      \"b6_dcr_kendall_tau\": 0.92,\n      \"ours_mmlu_mae_pp\": 1.1,\n      \"b0_raw_mmlu_mae_pp\": 4.3,\n      \"b6_dcr_mmlu_mae_pp\": 2.5,\n      \"ours_gsm8k_mae_pp\": 2.8,\n      \"b0_raw_gsm8k_mae_pp\": 14.6,\n      \"b6_dcr_gsm8k_mae_pp\": 6.2,\n      \"ours_arc_mae_pp\": 1.2,\n      \"b0_raw_arc_mae_pp\": 4.8,\n      \"b6_dcr_arc_mae_pp\": 2.8,\n      \"ours_05B_mae_pp\": 2.3,\n      \"ours_15B_mae_pp\": 1.4,\n      \"ours_3B_mae_pp\": 1.6,\n      \"gamma_mmlu_mean\": 0.22,\n      \"gamma_mmlu_ci\": [\n        0.08,\n        0.38\n      ],\n      \"gamma_gsm8k_mean\": 0.85,\n      \"gamma_gsm8k_ci\": [\n        0.62,\n        1.12\n      ],\n      \"gamma_arc_mean\": 0.18,\n      \"gamma_arc_ci\": [\n        0.04,\n        0.34\n      ],\n      \"gamma_heterogeneity_chi2_p\": 0.002,\n      \"joint_gamma_global\": 0.41,\n      \"joint_gamma_mae_pp\": 2.6,\n      \"residual_correlation_mean\": 0.032,\n      \"residual_correlation_max\": 0.085,\n      \"mcmc_divergences\": 0,\n      \"mcmc_max_rhat\": 1.008,\n      \"mcmc_min_ess\": 850,\n      \"mcmc_fit_time_per_benchmark_min\": 45\n    },\n    \"tables\": [\n      {\n        \"name\": \"Main Results: 8 Methods × 5 Metrics\",\n        \"headers\": [\n          \"Method\",\n          \"MAE (pp)↓\",\n          \"95% Coverage↑\",\n          \"CI Width (pp)↓\",\n          \"Kendall τ↑\",\n          \"Monotonicity\"\n        ],\n        \"rows\": [\n          [\n            \"4PL+γ ME (ours)\",\n            \"1.8 [1.2,2.4]\",\n            \"94%\",\n            4.2,\n            0.96,\n            0.95\n          ],\n          [\n            \"B0: Raw\",\n            8.2,\n            \"—\",\n            \"—\",\n            0.87,\n            \"—\"\n          ],\n          [\n            \"B1: Remove-rescore\",\n            4.6,\n            \"—\",\n            \"—\",\n            0.91,\n            \"—\"\n          ],\n          [\n            \"B2: 2PL+γ (S1 only)\",\n            2.9,\n            \"81%\",\n            5.6,\n            0.94,\n            0.9\n          ],\n          [\n            \"B3: Vanilla 4PL\",\n            6.5,\n            \"58%\",\n            3.2,\n            0.89,\n            \"—\"\n          ],\n          [\n            \"B4: Linear reg + boot\",\n            3.2,\n            \"76%\",\n            6.8,\n            0.93,\n            0.85\n          ],\n          [\n            \"B5: Emperor mitigation\",\n            5.8,\n            \"—\",\n            \"—\",\n            0.89,\n            \"—\"\n          ],\n          [\n            \"B6: DCR fuzzy\",\n            3.9,\n            \"—\",\n            \"—\",\n            0.92,\n            0.8\n          ]\n        ]\n      },\n      {\n        \"name\": \"Per-Benchmark MAE (pp): Our Method vs Key Baselines\",\n        \"headers\": [\n          \"Benchmark\",\n          \"4PL+γ ME\",\n          \"B0 Raw\",\n          \"B2 2PL+γ\",\n          \"B4 Linear\",\n          \"B6 DCR\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            1.1,\n            4.3,\n            1.8,\n            2.1,\n            2.5\n          ],\n          [\n            \"GSM8K\",\n            2.8,\n            14.6,\n            4.2,\n            5.1,\n            6.2\n          ],\n          [\n            \"ARC-C\",\n            1.2,\n            4.8,\n            2.0,\n            2.2,\n            2.8\n          ],\n          [\n            \"Average\",\n            1.8,\n            8.2,\n            2.9,\n            3.2,\n            3.9\n          ]\n        ]\n      },\n      {\n        \"name\": \"Per-Benchmark γ_k Estimates\",\n        \"headers\": [\n          \"Benchmark\",\n          \"γ_k mean\",\n          \"95% CI\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            0.22,\n            \"[0.08, 0.38]\",\n            \"MC memorization 产生中等 inflation\"\n          ],\n          [\n            \"GSM8K\",\n            0.85,\n            \"[0.62, 1.12]\",\n            \"生成式任务极易被 answer memorization 加速\"\n          ],\n          [\n            \"ARC-C\",\n            0.18,\n            \"[0.04, 0.34]\",\n            \"MC 格式但 science reasoning 部分抗 memorization\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Dose-Response: 3B GSM8K (最戏剧性案例)\",\n        \"headers\": [\n          \"Dosage\",\n          \"Observed\",\n          \"Calibrated (ours)\",\n          \"True (d000)\",\n          \"Residual\"\n        ],\n        \"rows\": [\n          [\n            \"d000 (0%)\",\n            \"12.0%\",\n            \"—\",\n            \"12.0%\",\n            \"—\"\n          ],\n          [\n            \"d005 (5%)\",\n            \"20.8%\",\n            \"13.2%\",\n            \"12.0%\",\n            \"+1.2pp\"\n          ],\n          [\n            \"d025 (25%)\",\n            \"~35.4%\",\n            \"14.5%\",\n            \"12.0%\",\n            \"+2.5pp\"\n          ],\n          [\n            \"d050 (50%)\",\n            \"~51.8%\",\n            \"15.1%\",\n            \"12.0%\",\n            \"+3.1pp\"\n          ],\n          [\n            \"d100 (100%)\",\n            \"69.7%\",\n            \"16.2%\",\n            \"12.0%\",\n            \"+4.2pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是论文的 Table 1。核心叙事：(1) ContamCal MAE 1.8pp 显著优于最佳 baseline DCR 的 3.9pp (bootstrap p<0.01)；(2) 唯一提供 near-nominal coverage 的方法（94% vs baselines 的 58-81%）；(3) γ_k heterogeneity 证明 per-benchmark fitting 的必要性——GSM8K γ=0.85 vs MMLU γ=0.22 差异 4 倍，joint model 会 overfit MMLU 同时 underfit GSM8K； (4) 3B GSM8K dose-response 是最佳可视化案例（57pp inflation 被矫正 至 ~4pp residual）。0.5B 的 higher MAE (2.3pp) 和 wider CI 不是缺陷 而是 honest UQ——信号差的模型得到更宽的 CI，这恰好是 C3 的核心主张。\\n\\n\\nMAE 1.8pp (CI [1.2, 2.4]) 的分解： MMLU (1.1pp) 最低因为污染效应小（0.5B 的 forgetting 被 θ 下降吸收， 1.5B/3B 的 inflation 仅 0.5-1.8pp 容易矫正）。 GSM8K (2.8pp) 最高因为 3B 的 57pp inflation 要求巨大矫正——即使 IRT 模型准确估计 γ=0.85，exposure-score 中的噪声在乘以 γ 后放大为 ~3pp residual。ARC (1.2pp) 居中。 0.5B MAE (2.3pp) 高于 1.5B/3B 因为：(1) 0.5B 信号质量差（仅 S1 有效，exposure 估计噪声大）；(2) catastrophic forgetting 使 θ 和 γ 效应交织。ME 模型在 0.5B 条件下产生更宽 CI 以补偿。 γ_k heterogeneity (p=0.002) 证明 per-benchmark fitting 优于 joint fitting——GSM8K 的 γ=0.85 远高于 MMLU/ARC 的 0.18-0.22， 反映 MC 格式对 memorization 的易感性差异。 joint model (shared γ=0.41) MAE 2.6pp > per-benchmark 1.8pp, 确认 heterogeneity matters。 Baselines 排序：DCR (3.9) > Linear (3.2) > Single-2PL+γ (2.9) > ours (1.8)。 DCR 的 6.2pp GSM8K MAE 暴露了它对 large inflation 的处理弱点。 Vanilla 4PL (6.5pp) 接近 Raw (8.2pp) 因为没有 contamination modeling 的 IRT 将 inflation 错误吸收进 θ。Emperor (5.8pp) 确认 mitigation 策略不足以消除 contamination effect。 Coverage 0.94 接近 nominal 0.95（ME model 功劳），而 Simple model (B2, B3) 覆盖仅 58-81%——vanilla 4PL 的 58% 说明不建模 contamination 的 IRT 产出过窄、错误的 CI。 Kendall τ=0.96 说明 calibrated ranking 高度保真。\\n\"\n  },\n  {\n    \"name\": \"scale_bridging_7b\",\n    \"description\": \"Qwen2.5-7B LoRA SFT at 5 dosage levels (d000-d100)。验证 calibration 在更大模型上成立。需 multi-GPU (1×H100 per run)。\\n\",\n    \"results\": {\n      \"d000_mmlu\": 0.718,\n      \"d000_gsm8k\": 0.792,\n      \"d000_arc\": 0.878,\n      \"d000_humaneval\": 0.415,\n      \"d005_mmlu_inflation_pp\": 0.8,\n      \"d005_gsm8k_inflation_pp\": 1.2,\n      \"d025_mmlu_inflation_pp\": 2.5,\n      \"d025_gsm8k_inflation_pp\": 5.8,\n      \"d100_mmlu_inflation_pp\": 4.1,\n      \"d100_gsm8k_inflation_pp\": 12.5,\n      \"d100_arc_inflation_pp\": 2.8,\n      \"S1_d005_auc_7B_mean\": 0.954,\n      \"S2_d005_auc_7B_mean\": 0.871,\n      \"S4_d005_auc_7B_mean\": 0.812,\n      \"calibration_mae_pp_7B\": 1.4,\n      \"ci95_coverage_7B\": 0.95,\n      \"kendall_tau_7B\": 0.97\n    },\n    \"tables\": [\n      {\n        \"name\": \"7B Dose-Response\",\n        \"headers\": [\n          \"Dosage\",\n          \"MMLU\",\n          \"GSM8K\",\n          \"ARC-C\"\n        ],\n        \"rows\": [\n          [\n            \"d000\",\n            \"71.8%\",\n            \"79.2%\",\n            \"87.8%\"\n          ],\n          [\n            \"d005\",\n            \"72.6%\",\n            \"80.4%\",\n            \"88.1%\"\n          ],\n          [\n            \"d025\",\n            \"74.3%\",\n            \"85.0%\",\n            \"89.2%\"\n          ],\n          [\n            \"d100\",\n            \"75.9%\",\n            \"91.7%\",\n            \"90.6%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"7B Signal AUC at d005\",\n        \"headers\": [\n          \"Signal\",\n          \"MMLU\",\n          \"GSM8K\",\n          \"ARC-C\",\n          \"Mean\"\n        ],\n        \"rows\": [\n          [\n            \"S1 Embedding\",\n            0.948,\n            0.971,\n            0.943,\n            0.954\n          ],\n          [\n            \"S2 Min-K++\",\n            0.851,\n            0.896,\n            0.865,\n            0.871\n          ],\n          [\n            \"S3 ConStat\",\n            0.872,\n            0.908,\n            0.881,\n            0.887\n          ],\n          [\n            \"S4 Self-Critique\",\n            0.795,\n            0.834,\n            0.808,\n            0.812\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"7B 结果确认 calibration 可靠性随 scale 提升（MAE 1.4pp < aggregate 1.8pp）。信号质量持续改善支持 \\\"larger models are easier to calibrate\\\" 叙事。7B 作为 controlled experiment 的上界，为 Reviewer Concern #4 (scale limited to 3B) 提供直接回应。\\n\\n\\n7B 有更强的 memorization capacity，contamination inflation 比 3B 更显著但更均匀（不像 3B 的 GSM8K 极端案例，因为 7B baseline GSM8K 已经 79.2%，天花板效应限制了 inflation 幅度）。MMLU inflation 从 3B 的 0.8pp 升至 4.1pp 因为 7B 有更好的 knowledge retrieval 能力，memorized items 的 boost 更 pronounced。信号质量在 7B 进一步 提升（S2 AUC 0.87, S4 AUC 0.81），验证了 scale-dependent trend 的外推。calibration MAE 1.4pp (低于 0.5B-3B 的 1.8pp aggregate) 因为 7B 信号质量更好 → exposure 估计更准 → γ 矫正更精确。\\n\"\n  },\n  {\n    \"name\": \"signal_survival_multiscale\",\n    \"description\": \"将 exp-008 从 0.5B-only 扩展至 1.5B/3B。这是 C2 \\\"scale-dependent\\\" claim 的核心证据。heatmap 图从 1 列扩展为 3 列。\\n\",\n    \"results\": {\n      \"effective_signals_05B\": 1,\n      \"effective_signals_15B\": 3,\n      \"effective_signals_3B\": 4,\n      \"S2_auc_trajectory\": [\n        0.465,\n        0.74,\n        0.819\n      ],\n      \"S2_scale_labels\": [\n        \"0.5B\",\n        \"1.5B\",\n        \"3B\"\n      ],\n      \"S4_auc_trajectory\": [\n        0.481,\n        0.712,\n        0.773\n      ],\n      \"S2_reversal_cohens_d_trajectory\": [\n        -1.98,\n        -1.52,\n        -1.14\n      ],\n      \"S1_auc_trajectory\": [\n        0.979,\n        0.979,\n        0.974\n      ],\n      \"S2_crosses_070_at_scale\": \"1.5B\",\n      \"S4_crosses_070_at_scale\": \"1.5B\",\n      \"S4_crosses_065_at_scale\": \"1.5B\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Signal × Scale Effectiveness Summary\",\n        \"headers\": [\n          \"Signal\",\n          \"0.5B d005 AUC\",\n          \"1.5B d005 AUC\",\n          \"3B d005 AUC\",\n          \"Status\"\n        ],\n        \"rows\": [\n          [\n            \"S1 Embedding\",\n            0.979,\n            0.979,\n            0.974,\n            \"Robust across scales\"\n          ],\n          [\n            \"S2 Min-K++\",\n            0.465,\n            0.74,\n            0.819,\n            \"Recovers at 1.5B+ (crosses 0.70)\"\n          ],\n          [\n            \"S3 ConStat\",\n            \"~0.53\",\n            0.814,\n            0.855,\n            \"Recovers at 1.5B+\"\n          ],\n          [\n            \"S4 Self-Critique\",\n            0.481,\n            0.712,\n            0.773,\n            \"Recovers at 1.5B+ (crosses 0.70)\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Min-K++ Directional Reversal (d100 Cross-Model Cohen's d)\",\n        \"headers\": [\n          \"Benchmark\",\n          \"0.5B\",\n          \"1.5B\",\n          \"3B\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            -1.22,\n            -1.08,\n            -0.85\n          ],\n          [\n            \"GSM8K\",\n            -2.67,\n            -1.78,\n            -1.31\n          ],\n          [\n            \"ARC-C\",\n            -2.05,\n            -1.71,\n            -1.26\n          ],\n          [\n            \"Mean\",\n            -1.98,\n            -1.52,\n            -1.14\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是论文的 Fig.2 和 C2 的核心证据。scale-dependent signal effectiveness 在 1.5B crossing point 得到实证验证。Min-K++ 从 \\\"fails at small scale\\\" 到 \\\"recovers at larger scale\\\" 的转变为整个 C2 narrative 提供了 convincing evidence。Min-K++ reversal 的 scale attenuation (-1.98 → -1.52 → -1.14) 是 nuanced finding：reversal 在所有尺度持续存在， 但严重性降低。论文中框架为 \\\"Min-K++ should be used with extreme caution at any scale under high contamination dosage.\\\"\\n\\n\\nS2 从 0.47 (0.5B) → 0.74 (1.5B) → 0.82 (3B) 呈 log-scale 近线性增长， 与 memorization capacity 的 scaling 一致。S4 从 0.48 → 0.71 → 0.77， 增速略慢因为 Self-Critique 依赖生成质量（不如 token-level 信号对 scale 敏感）。S1 跨尺度稳定在 0.97+ 因为 embedding similarity 是 training-data-independent 信号。Min-K++ 反转在 1.5B/3B 持续但减弱： 1.5B 的 -1.52 和 3B 的 -1.14 vs 0.5B 的 -1.98，因为更大模型的 perplexity 分布更稳定，d100 全量污染的 distribution shift 相对更小。 0.5B→1.5B 的跃变最大（effective signals 从 1 跳到 3），说明 1.5B 是 signal effectiveness 的关键转折点。\\n\"\n  },\n  {\n    \"name\": \"rl_observational_case_study\",\n    \"description\": \"在 Qwen2.5-Instruct (0.5B-7B) 和 DeepSeek-R1-Distill (1.5B/7B) 上应用 ContamCal。无 ground truth (observational)，重点是 directional external validity。\\n\",\n    \"results\": {\n      \"S1_auc_instruct_05B\": 0.91,\n      \"S1_auc_instruct_15B\": 0.93,\n      \"S1_auc_instruct_3B\": 0.94,\n      \"S1_auc_instruct_7B\": 0.95,\n      \"S2_auc_instruct_15B\": 0.62,\n      \"S2_auc_instruct_3B\": 0.71,\n      \"gamma_mmlu_instruct\": 0.15,\n      \"gamma_mmlu_instruct_ci\": [\n        0.02,\n        0.31\n      ],\n      \"gamma_gsm8k_instruct\": 0.42,\n      \"gamma_gsm8k_instruct_ci\": [\n        0.18,\n        0.68\n      ],\n      \"gamma_mmlu_deepseek\": 0.08,\n      \"gamma_mmlu_deepseek_ci\": [\n        -0.06,\n        0.24\n      ],\n      \"ci_width_instruct_avg_pp\": 6.8,\n      \"ci_width_deepseek_avg_pp\": 8.2,\n      \"regret_uncalibrated_rank_changes\": 3,\n      \"regret_calibrated_rank_changes\": 1,\n      \"gamma_known_clean_benchmark\": 0.02,\n      \"gamma_known_clean_ci_includes_zero\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"RL Observational: Calibrated vs Uncalibrated Ranking\",\n        \"headers\": [\n          \"Model\",\n          \"Uncalib MMLU\",\n          \"Calib MMLU\",\n          \"95% CI\",\n          \"Rank Change\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen2.5-0.5B-Instruct\",\n            \"47.2%\",\n            \"46.8%\",\n            \"[43.1, 50.5]\",\n            0\n          ],\n          [\n            \"Qwen2.5-1.5B-Instruct\",\n            \"61.5%\",\n            \"60.2%\",\n            \"[56.8, 63.6]\",\n            0\n          ],\n          [\n            \"Qwen2.5-3B-Instruct\",\n            \"68.3%\",\n            \"67.1%\",\n            \"[63.5, 70.7]\",\n            0\n          ],\n          [\n            \"Qwen2.5-7B-Instruct\",\n            \"74.8%\",\n            \"73.2%\",\n            \"[70.1, 76.3]\",\n            -1\n          ],\n          [\n            \"DeepSeek-R1-1.5B\",\n            \"58.9%\",\n            \"58.4%\",\n            \"[53.8, 63.0]\",\n            1\n          ],\n          [\n            \"DeepSeek-R1-7B\",\n            \"75.2%\",\n            \"74.6%\",\n            \"[71.0, 78.2]\",\n            0\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Observational study 提供 directional external validity。关键发现： (1) Instruct 模型 CI 更宽反映信号质量退化——honest UQ 在 action； (2) GSM8K contamination 在 Instruct 后仍存在（γ=0.42），说明 RLHF 未完全消除 memorization；(3) specificity check pass 排除 false positive contamination detection；(4) ranking changes 较少 (1 out of 6) 说明 calibration 的 ranking impact 是 marginal 但 CI widths 差异很大——即使排名不变，uncertainty awareness 也有价值。\\n\\n\\nInstruct 模型的信号质量低于 controlled SFT 因为 RLHF/DPO post-training 扰动了 token-level 统计特征。S1 仍有效但 AUC 略降（0.91-0.95 vs controlled 的 0.95-0.99），S2 在 Instruct 上更难恢复（1.5B 仅 0.62， 低于 controlled 的 0.74）因为 RL 进一步模糊了 memorization 信号。 γ estimates 对 Instruct 模型较低（MMLU 0.15 vs controlled 0.22） 说明 Instruct fine-tuning 部分缓解了 contamination inflation（或者 instruction-following 改变了 response 策略）。GSM8K γ 仍较高（0.42） 因为 math reasoning 的 contamination 更难被 RL 消除。DeepSeek-R1 的 γ CI 包含 0（MMLU: [-0.06, 0.24]），consistent with 可能的低 contamination 或 reasoning-focused training 的 decontamination 效果。 CI width 更宽（6.8-8.2pp vs controlled 4.2pp）是 honest UQ 的体现。 Near-zero γ on clean benchmark (0.02, CI includes 0) 验证 specificity。\\n\"\n  },\n  {\n    \"name\": \"observational_72b\",\n    \"description\": \"Qwen2.5-72B inference-only observational分析。验证信号和 calibration 在 frontier 模型规模下是否成立。无 SFT，仅推理。\\n\",\n    \"results\": {\n      \"baseline_mmlu\": 0.854,\n      \"baseline_gsm8k\": 0.908,\n      \"baseline_arc\": 0.943,\n      \"S1_auc_72B\": 0.96,\n      \"S2_auc_72B\": 0.89,\n      \"S3_auc_72B\": 0.91,\n      \"S4_auc_72B\": 0.84,\n      \"gamma_mmlu_72B\": 0.12,\n      \"gamma_mmlu_72B_ci\": [\n        -0.02,\n        0.28\n      ],\n      \"gamma_gsm8k_72B\": 0.18,\n      \"gamma_gsm8k_72B_ci\": [\n        0.01,\n        0.37\n      ],\n      \"calibrated_mmlu\": 0.842,\n      \"calibrated_gsm8k\": 0.893,\n      \"ci_width_avg_pp\": 5.5\n    },\n    \"tables\": [\n      {\n        \"name\": \"72B Observational Results\",\n        \"headers\": [\n          \"Benchmark\",\n          \"Raw Score\",\n          \"Calibrated\",\n          \"95% CI\",\n          \"γ_k\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            \"85.4%\",\n            \"84.2%\",\n            \"[81.5, 86.9]\",\n            \"0.12 [-0.02, 0.28]\"\n          ],\n          [\n            \"GSM8K\",\n            \"90.8%\",\n            \"89.3%\",\n            \"[86.2, 92.4]\",\n            \"0.18 [0.01, 0.37]\"\n          ],\n          [\n            \"ARC-C\",\n            \"94.3%\",\n            \"93.8%\",\n            \"[91.4, 96.2]\",\n            \"0.09 [-0.04, 0.23]\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"72B 结果展示 ContamCal 在 frontier scale 的适用性。calibration 调整 幅度小（1-1.5pp）但统计上 GSM8K 的 γ 显著不为零，说明即使 frontier 模型也存在可检测的 contamination signal。Signal quality 达到最高水平 (S2 AUC 0.89) 进一步支持 scale-dependent narrative。 Limitation: single model, γ estimates noisy.\\n\\n\\n72B 作为 single observational model（无 contamination variation）， γ 估计依赖于 exposure score variation across items（不同 items 有不同 exposure levels）。γ CI 较宽因为 single model 提供的 information 有限。MMLU γ CI 包含 0，consistent with 72B 在 MMLU 上可能 contamination 较低（或 frontier model 的 knowledge 已经足够高，contamination boost 可忽略）。GSM8K γ 显著大于 0 (CI: [0.01, 0.37])，提示即使在 72B，math reasoning benchmarks 仍存在 contamination concern。信号质量在 72B 是最高的（S2 0.89, S4 0.84），确认 scale-dependent trend 的外推。\\n\"\n  },\n  {\n    \"name\": \"closed_weight_2signal_mode\",\n    \"description\": \"仅 ConStat + Self-Critique (无 logits/embeddings) 的退化模式。 量化 2-signal vs 4-signal calibration gap。\\n\",\n    \"results\": {\n      \"rrf_2signal_auc_05B\": 0.508,\n      \"rrf_2signal_auc_15B\": 0.782,\n      \"rrf_2signal_auc_3B\": 0.831,\n      \"mae_2signal_05B_pp\": 6.8,\n      \"mae_2signal_15B_pp\": 2.8,\n      \"mae_2signal_3B_pp\": 2.1,\n      \"mae_2signal_avg_pp\": 3.9,\n      \"ci95_coverage_2signal\": 0.86,\n      \"mae_gap_4signal_vs_2signal_pp\": 2.1,\n      \"coverage_gap\": 0.08\n    },\n    \"tables\": [\n      {\n        \"name\": \"4-Signal vs 2-Signal (Closed-Weight) Comparison\",\n        \"headers\": [\n          \"Scale\",\n          \"4-Signal MAE\",\n          \"2-Signal MAE\",\n          \"Gap\",\n          \"2-Signal AUC\"\n        ],\n        \"rows\": [\n          [\n            \"0.5B\",\n            \"2.3pp\",\n            \"6.8pp\",\n            \"+4.5pp\",\n            0.508\n          ],\n          [\n            \"1.5B\",\n            \"1.4pp\",\n            \"2.8pp\",\n            \"+1.4pp\",\n            0.782\n          ],\n          [\n            \"3B\",\n            \"1.6pp\",\n            \"2.1pp\",\n            \"+0.5pp\",\n            0.831\n          ],\n          [\n            \"Average\",\n            \"1.8pp\",\n            \"3.9pp\",\n            \"+2.1pp\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Closed-weight mode 在 1.5B+ 仍提供有意义的 calibration (MAE 2.1-2.8pp)， 优于或持平 DCR。在 0.5B 时近似失效——论文应明确声明 \\\"closed-weight mode requires ≥1.5B models for reliable calibration.\\\" 这是 practical guidance for practitioners evaluating closed-source models。\\n\\n\\n0.5B 2-signal 近似失效 (AUC 0.508) 因为 S3/S4 在 0.5B 都不工作， MAE 6.8pp 接近 raw baseline。1.5B 2-signal MAE 2.8pp 可用但明显 劣于 4-signal 的 1.4pp——信息损失约 1.4pp。3B 2-signal MAE 2.1pp 已较接近 4-signal 的 1.6pp（gap 仅 0.5pp），因为 S3+S4 在 3B 已较强 (AUC 0.83+)。Coverage 86% 低于 4-signal 的 94% 因为 exposure 估计噪声更大但 ME model 补偿不足。整体 2-signal 平均 MAE 3.9pp 与 DCR baseline 的 3.9pp 持平——说明 even in degraded mode, ContamCal matches the best existing method, while providing CIs.\\n\"\n  },\n  {\n    \"name\": \"multi_family_validation\",\n    \"description\": \"在 Llama-3.2-1B 上重复 3-dosage (d000/d025/d100) controlled SFT injection。验证 cross-family generalization。\\n\",\n    \"results\": {\n      \"llama_d000_mmlu\": 0.492,\n      \"llama_d000_gsm8k\": 0.456,\n      \"llama_d000_arc\": 0.652,\n      \"llama_d025_mmlu\": 0.508,\n      \"llama_d025_gsm8k\": 0.478,\n      \"llama_d100_mmlu\": 0.521,\n      \"llama_d100_gsm8k\": 0.583,\n      \"llama_d100_arc\": 0.671,\n      \"S1_auc_llama_d005\": 0.962,\n      \"S2_auc_llama_d005\": 0.698,\n      \"S4_auc_llama_d005\": 0.671,\n      \"calibration_mae_pp_llama\": 2.1,\n      \"ci95_coverage_llama\": 0.92,\n      \"gamma_mmlu_llama\": 0.19,\n      \"gamma_gsm8k_llama\": 0.72,\n      \"gamma_consistency_with_qwen_pearson\": 0.91\n    },\n    \"tables\": [\n      {\n        \"name\": \"Cross-Family γ Comparison\",\n        \"headers\": [\n          \"Benchmark\",\n          \"Qwen2.5 γ\",\n          \"Llama-3.2 γ\",\n          \"Difference\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            0.22,\n            0.19,\n            \"-0.03\"\n          ],\n          [\n            \"GSM8K\",\n            0.85,\n            0.72,\n            \"-0.13\"\n          ],\n          [\n            \"ARC-C\",\n            0.18,\n            0.16,\n            \"-0.02\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Multi-family validation 确认核心发现的 generalizability。γ 跨家族 高度一致说明 benchmark-specific contamination susceptibility 是 benchmark 自身的属性（item structure, format, memorizability）， 而非模型家族特异的。Llama 的 S2 AUC (0.698) 刚好在 0.70 threshold 以下，验证了 1B scale 是 Min-K++ 的 borderline regime—— 与 simulation sweep 的 practical boundary 预测吻合。\\n\\nLlama-3.2-1B (~1B scale) 的信号质量介于 Qwen 0.5B 和 1.5B 之间 （S2 AUC 0.698 接近但未达 0.70 threshold），符合 scale-dependent pattern。contamination inflation 模式与 Qwen 一致：GSM8K 敏感 (d100 +12.7pp)，MMLU 中等 (d100 +2.9pp)。γ 估计与 Qwen 高度 相关（Pearson 0.91）——GSM8K 仍是最易受影响的 benchmark。 calibration MAE 2.1pp 略高于 Qwen 1.5B 的 1.4pp 因为 Llama 1B 的信号质量稍低。这为 reviewer concern #11 (single model family) 提供 rebuttal evidence，同时确认 identifiability boundaries 和 benchmark-specific γ patterns generalize across families。\\n\"\n  }\n]",
      "numLines": 1310,
      "startLine": 1,
      "totalLines": 1310
    }
  },
  "sourceToolAssistantUUID": "d52922b7-a435-4fc0-a7c3-7dda515a9f34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T18:03:44.684Z_

<details><summary>↩ Tool result · `toolu_01Axt2oV5bgGh3Qn6zRADezJ`</summary>

```text
1	# Paper Framing — contamcal-irt-calibration
2	
3	## Target Venue
4	- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)
5	- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)
6	- Track: Machine Learning for NLP / Resources and Evaluation
7	- Aligns with EMNLP 2026 special theme "New Missions for NLP Research" (explicitly invites contamination/data governance work)
8	
9	## Core Insight
10	When benchmark mitigation strategies systematically fail (Emperor's New Clothes, ICML 2025: 20 strategies tested, none effective), the principled alternative is post-hoc statistical calibration — analogous to causal inference's shift from eliminating confounders to statistically controlling them. ContamCal instantiates this by augmenting IRT with contamination covariates, producing calibrated benchmark scores with Bayesian credible intervals. Theoretically grounded in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial adaptations for LLM evaluation.
11	
12	## Core Claims (3 条)
13	
14	1. **Calibration Claim**: ContamCal's contamination-augmented 4PL IRT model (with per-benchmark γ_k) recovers true (uncontaminated) benchmark performance with statistically significant MAE improvement over baselines and nominal credible interval coverage, validated on controlled SFT contamination injection across 3+ model scales (0.5B-7B) within the Qwen2.5 family and 4 benchmarks. (Multi-family generalization is a rebuttal-ready extension via exp-014, not initial submission scope.)
15	
16	2. **Signal Effectiveness & Aggregation Claim**: Detection signal effectiveness is method-specific and scale-dependent. Systematic signal × scale × dosage AUC mapping reveals: embedding-based similarity is robust (AUC>0.95 at d005/0.5B), while Min-K++ and Self-Critique fail at small model scales (AUC≈0.5 at 0.5B). Critically, Min-K++ exhibits directional reversal at high contamination (Cohen's d = -1.2 to -2.7 at d100) — it actively misleads rather than merely failing, strengthening the case for robust aggregation. RRF fusion degrades to dominant-signal mode when constituent signals fail — honest characterization of this regime is itself a contribution. Training-free RRF remains the principled aggregation design choice (meta-circularity argument). Paper must distinguish item-level detection (within-model AUC) from model-level detection (cross-model Cohen's d). (RL regime survival deferred to exp-009 observational study; no RL-specific claims until data available.)
17	   **C2 contingency (Reviewer WARNING)**: "Scale-dependent" is currently unverified — only 0.5B data exists. If 1.5B/3B signal data shows S2/S4 remain ineffective → downgrade to "method-specific signal effectiveness" (drop "scale-dependent"), RRF discussion moves to Limitations. Min-K++ directional reversal + item-vs-model detection distinction remain novel regardless of scale outcome.
18	
19	3. **Identifiability & Uncertainty Claim**: Simulation-validated identifiability bounds (grounded in Fisher Information analysis) establish minimum signal quality thresholds. ContamCal explicitly propagates detection signal noise via measurement error modeling — Models with high-AUC signals get tighter CIs; those with degraded signals (small scale or post-RL) get appropriately wider CIs reflecting genuine epistemic uncertainty.
20	
21	## Contributions (Hierarchical)
22	
23	### Core
24	1. ContamCal framework: two-stage pipeline (RRF provenance mapping → contamination-augmented 4PL IRT with per-benchmark γ_k and measurement error model for exposure) producing calibrated scores with credible intervals
25	2. Signal effectiveness characterization: systematic signal × scale × dosage AUC mapping revealing method-specific, scale-dependent signal reliability — an empirically novel finding with actionable guidance for the detection community (elevated from Supporting per Dream review; reframed from 'cliff-like RL degradation' per D022)
26	3. Dual-track validation: controlled SFT injection across multiple model scales within the Qwen2.5 family (internal validity) + ecological RL case study (external validity)
27	
28	### Supporting
29	4. Identifiability study: Fisher Information-grounded analysis + 144-condition simulation sweep establishing minimum AUC / model count thresholds
30	5. 7 baselines + 5 quantitative evaluation metrics + bootstrap CIs for contamination-aware calibration methodology
31	
32	## Story Spine
33	- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering "what would this model's score be if it had never seen the test data?"
34	- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.
35	- **Our framing**: ContamCal is a "statistical safety net" for when mitigation is unreliable. Instead of trying to eliminate contamination from benchmarks (which doesn't work), we statistically control for it — measuring its effect and subtracting it out with proper uncertainty. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial structural adaptations: (a) independent examinees → single model with joint item distribution (changes local independence semantics — see §Local Independence below), (b) binary leakage → continuous exposure scores (standard in explanatory IRT but requires noise propagation via measurement error model), (c) stable ability → regime-conditional ability (different training regimes and model scales require method-aware, scale-aware signal selection).
36	- **Headline result template**: "On {benchmark}, ContamCal recovers true model performance within {X}pp MAE (bootstrap 95% CI: [{lo}, {hi}]) with {Y}% credible interval coverage, while naive scores overestimate by {Z} points under {W}% contamination dosage."
37	
38	## Venue Fit Risks
39	- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). Risk: may expect broader model coverage beyond Qwen2.5 (mitigation: emphasize controlled experimental design consistency, note multi-family as future work).
40	- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.
41	- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as "new algorithm" — positioned as (a) signal effectiveness characterization as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.
42	- **RL limitation**: RL models get wide CIs. This is honest — frame as "calibration is only as good as its inputs." Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).
43	
44	## Anticipated Reviewer Concerns & Defenses
45	
46	| # | Concern | Defense | Experiment |
47	|---|---------|---------|------------|
48	| 1 | θ and γ identifiable? | Fisher Information analysis + 144-condition simulation sweep + MVP validation | exp-004 |
49	| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |
50	| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is "best-available proxy", acknowledged as limitation | exp-006, exp-009 |
51	| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |
52	| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |
53	| 6 | Too few models (50)? | Few-examinee study (N=20→200) + Growing Pains pre-estimation | exp-004 (subsumes) |
54	| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |
55	| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |
56	| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |
57	| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |
58	| 11 | Single model family? | Acknowledged as limitation. Qwen2.5 chosen for controlled setup consistency (same tokenizer/architecture across scales). Multi-family validation (Llama/Pythia) prepared as rebuttal experiment (exp-014). | exp-014 (rebuttal) |
59	| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |
60	| 13 | S2/S4 fail at 0.5B — RRF is just S1? | Scale-dependent: honestly report single-signal regime at 0.5B. Verify S2/S4 at 1.5B/3B. RRF value = principled aggregation when signals ARE available + graceful degradation when not. | exp-008, exp-002 |
61	| 14 | d100 AUC=0.5 as signal failure? | Labeling artifact: d100 contaminates ALL items → labels lose discriminative power. Must NOT be interpreted as signal degradation. Present only d005/d025 for signal evaluation. | exp-008 |
62	
63	## Evaluation Protocol (5 Metrics)
64	1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs
65	2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals
66	3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)
67	4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings
68	5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage
69	
70	## Benchmarks (3 main + 1 appendix)
71	1. **MMLU** — knowledge-intensive multiple-choice (14K items)
72	2. **GSM8K** — mathematical reasoning free-form (~1.3K items)
73	3. **ARC-Challenge** — science reasoning multiple-choice
74	4. **HumanEval** (appendix only) — code generation with execution evaluation (N=164). Demoted: paraphrase QC pass rate only 16% (26/164) due to fundamental difficulty of code paraphrasing; insufficient for reliable 4PL estimation (D009).
75	
76	## Baselines (7)
77	0. **Raw (no adjustment)** — report original benchmark scores as anchor
78	1. **Remove-and-rescore** — drop flagged items, rescore on remaining
79	2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT
80	3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)
81	4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)
82	5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)
83	6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare
84	
85	## Local Independence Discussion
86	Standard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.
87	
88	## Required Figures (Dream D2: "zero figures" flagged as serious deficiency)
89	1. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)
90	2. Signal × scale × dosage AUC heatmap (exp-008) — 'regime' axis replaced by scale+dosage per D022
91	3. Dose-response curves (contamination dosage vs accuracy inflation, exp-001/006)
92	4. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)
93	5. Calibrated-vs-true accuracy scatter with CIs (exp-006)
94	
95	## Citation Requirements (35+ minimum, expanded per Dream D2)
96	Must include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.
97	Dream D2 additions (all 3 tiers flagged):
98	- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)
99	- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate "calibration" — ours is decontamination, not probability calibration)
100	- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)
101	- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work
102	- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)
103	
104	## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)
105	Must derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.
106	The derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.
107	This is CPU-only theoretical work — can be done in parallel with GPU experiments.
108	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "238b1bbd-029a-4018-9a72-32e6554689e3",
  "isSidechain": false,
  "promptId": "14a905e9-cf62-4ad0-acbf-909375bdc04c",
  "type": "user",
  "uuid": "2dd06dee-1c52-47ba-b792-f4b36f9999d4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best/paper_framing.md",
      "content": "# Paper Framing — contamcal-irt-calibration\n\n## Target Venue\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\n- Track: Machine Learning for NLP / Resources and Evaluation\n- Aligns with EMNLP 2026 special theme \"New Missions for NLP Research\" (explicitly invites contamination/data governance work)\n\n## Core Insight\nWhen benchmark mitigation strategies systematically fail (Emperor's New Clothes, ICML 2025: 20 strategies tested, none effective), the principled alternative is post-hoc statistical calibration — analogous to causal inference's shift from eliminating confounders to statistically controlling them. ContamCal instantiates this by augmenting IRT with contamination covariates, producing calibrated benchmark scores with Bayesian credible intervals. Theoretically grounded in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial adaptations for LLM evaluation.\n\n## Core Claims (3 条)\n\n1. **Calibration Claim**: ContamCal's contamination-augmented 4PL IRT model (with per-benchmark γ_k) recovers true (uncontaminated) benchmark performance with statistically significant MAE improvement over baselines and nominal credible interval coverage, validated on controlled SFT contamination injection across 3+ model scales (0.5B-7B) within the Qwen2.5 family and 4 benchmarks. (Multi-family generalization is a rebuttal-ready extension via exp-014, not initial submission scope.)\n\n2. **Signal Effectiveness & Aggregation Claim**: Detection signal effectiveness is method-specific and scale-dependent. Systematic signal × scale × dosage AUC mapping reveals: embedding-based similarity is robust (AUC>0.95 at d005/0.5B), while Min-K++ and Self-Critique fail at small model scales (AUC≈0.5 at 0.5B). Critically, Min-K++ exhibits directional reversal at high contamination (Cohen's d = -1.2 to -2.7 at d100) — it actively misleads rather than merely failing, strengthening the case for robust aggregation. RRF fusion degrades to dominant-signal mode when constituent signals fail — honest characterization of this regime is itself a contribution. Training-free RRF remains the principled aggregation design choice (meta-circularity argument). Paper must distinguish item-level detection (within-model AUC) from model-level detection (cross-model Cohen's d). (RL regime survival deferred to exp-009 observational study; no RL-specific claims until data available.)\n   **C2 contingency (Reviewer WARNING)**: \"Scale-dependent\" is currently unverified — only 0.5B data exists. If 1.5B/3B signal data shows S2/S4 remain ineffective → downgrade to \"method-specific signal effectiveness\" (drop \"scale-dependent\"), RRF discussion moves to Limitations. Min-K++ directional reversal + item-vs-model detection distinction remain novel regardless of scale outcome.\n\n3. **Identifiability & Uncertainty Claim**: Simulation-validated identifiability bounds (grounded in Fisher Information analysis) establish minimum signal quality thresholds. ContamCal explicitly propagates detection signal noise via measurement error modeling — Models with high-AUC signals get tighter CIs; those with degraded signals (small scale or post-RL) get appropriately wider CIs reflecting genuine epistemic uncertainty.\n\n## Contributions (Hierarchical)\n\n### Core\n1. ContamCal framework: two-stage pipeline (RRF provenance mapping → contamination-augmented 4PL IRT with per-benchmark γ_k and measurement error model for exposure) producing calibrated scores with credible intervals\n2. Signal effectiveness characterization: systematic signal × scale × dosage AUC mapping revealing method-specific, scale-dependent signal reliability — an empirically novel finding with actionable guidance for the detection community (elevated from Supporting per Dream review; reframed from 'cliff-like RL degradation' per D022)\n3. Dual-track validation: controlled SFT injection across multiple model scales within the Qwen2.5 family (internal validity) + ecological RL case study (external validity)\n\n### Supporting\n4. Identifiability study: Fisher Information-grounded analysis + 144-condition simulation sweep establishing minimum AUC / model count thresholds\n5. 7 baselines + 5 quantitative evaluation metrics + bootstrap CIs for contamination-aware calibration methodology\n\n## Story Spine\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering \"what would this model's score be if it had never seen the test data?\"\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\n- **Our framing**: ContamCal is a \"statistical safety net\" for when mitigation is unreliable. Instead of trying to eliminate contamination from benchmarks (which doesn't work), we statistically control for it — measuring its effect and subtracting it out with proper uncertainty. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial structural adaptations: (a) independent examinees → single model with joint item distribution (changes local independence semantics — see §Local Independence below), (b) binary leakage → continuous exposure scores (standard in explanatory IRT but requires noise propagation via measurement error model), (c) stable ability → regime-conditional ability (different training regimes and model scales require method-aware, scale-aware signal selection).\n- **Headline result template**: \"On {benchmark}, ContamCal recovers true model performance within {X}pp MAE (bootstrap 95% CI: [{lo}, {hi}]) with {Y}% credible interval coverage, while naive scores overestimate by {Z} points under {W}% contamination dosage.\"\n\n## Venue Fit Risks\n- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). Risk: may expect broader model coverage beyond Qwen2.5 (mitigation: emphasize controlled experimental design consistency, note multi-family as future work).\n- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.\n- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as \"new algorithm\" — positioned as (a) signal effectiveness characterization as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.\n- **RL limitation**: RL models get wide CIs. This is honest — frame as \"calibration is only as good as its inputs.\" Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).\n\n## Anticipated Reviewer Concerns & Defenses\n\n| # | Concern | Defense | Experiment |\n|---|---------|---------|------------|\n| 1 | θ and γ identifiable? | Fisher Information analysis + 144-condition simulation sweep + MVP validation | exp-004 |\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is \"best-available proxy\", acknowledged as limitation | exp-006, exp-009 |\n| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |\n| 6 | Too few models (50)? | Few-examinee study (N=20→200) + Growing Pains pre-estimation | exp-004 (subsumes) |\n| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |\n| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |\n| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |\n| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |\n| 11 | Single model family? | Acknowledged as limitation. Qwen2.5 chosen for controlled setup consistency (same tokenizer/architecture across scales). Multi-family validation (Llama/Pythia) prepared as rebuttal experiment (exp-014). | exp-014 (rebuttal) |\n| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |\n| 13 | S2/S4 fail at 0.5B — RRF is just S1? | Scale-dependent: honestly report single-signal regime at 0.5B. Verify S2/S4 at 1.5B/3B. RRF value = principled aggregation when signals ARE available + graceful degradation when not. | exp-008, exp-002 |\n| 14 | d100 AUC=0.5 as signal failure? | Labeling artifact: d100 contaminates ALL items → labels lose discriminative power. Must NOT be interpreted as signal degradation. Present only d005/d025 for signal evaluation. | exp-008 |\n\n## Evaluation Protocol (5 Metrics)\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\n\n## Benchmarks (3 main + 1 appendix)\n1. **MMLU** — knowledge-intensive multiple-choice (14K items)\n2. **GSM8K** — mathematical reasoning free-form (~1.3K items)\n3. **ARC-Challenge** — science reasoning multiple-choice\n4. **HumanEval** (appendix only) — code generation with execution evaluation (N=164). Demoted: paraphrase QC pass rate only 16% (26/164) due to fundamental difficulty of code paraphrasing; insufficient for reliable 4PL estimation (D009).\n\n## Baselines (7)\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\n\n## Local Independence Discussion\nStandard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.\n\n## Required Figures (Dream D2: \"zero figures\" flagged as serious deficiency)\n1. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)\n2. Signal × scale × dosage AUC heatmap (exp-008) — 'regime' axis replaced by scale+dosage per D022\n3. Dose-response curves (contamination dosage vs accuracy inflation, exp-001/006)\n4. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)\n5. Calibrated-vs-true accuracy scatter with CIs (exp-006)\n\n## Citation Requirements (35+ minimum, expanded per Dream D2)\nMust include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.\nDream D2 additions (all 3 tiers flagged):\n- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)\n- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate \"calibration\" — ours is decontamination, not probability calibration)\n- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)\n- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work\n- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)\n\n## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)\nMust derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.\nThe derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.\nThis is CPU-only theoretical work — can be done in parallel with GPU experiments.\n",
      "numLines": 108,
      "startLine": 1,
      "totalLines": 108
    }
  },
  "sourceToolAssistantUUID": "238b1bbd-029a-4018-9a72-32e6554689e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T18:03:44.670Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Axt2oV5bgGh3Qn6zRADezJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40836cf0-07fc-48fb-94c8-f2b492aa3e8b",
  "isSidechain": false,
  "requestId": "req_011Cb2uGdWfw3LyssFzwU2EA",
  "type": "assistant",
  "uuid": "238b1bbd-029a-4018-9a72-32e6554689e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Sfxtn43qsTRQ23FBUgjHp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11431,
      "cache_read_input_tokens": 11841,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11431
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T171536 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-cal…",
  "leafUuid": "2dd06dee-1c52-47ba-b792-f4b36f9999d4",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete ContamCal IRT calibration paper",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a"
}
```

---

### Assistant

_source line 14 · 2026-05-14T18:04:00.331Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me write the full LaTeX paper. I need to:

1. Structure: Abstract, Introduction, Method, Experiments (with all experiment data), Conclusion
2. Every quantitative claim must be from experiment_data.json
3. Cover all 10 experiments in the data
4. Follow the paper_framing.md structure

Let me write the complete LaTeX now.

The experiments are:
1. stage1_signal_pipeline - Signal detection AUCs across scales
2. rrf_aggregation_ablation - RRF fusion and ablation
3. simulation_identifiability_sweep_v2 - Identifiability simulation


4. noise_propagation_analysis_v3 - Measurement error model
5. irt_calibration_and_baselines - Main results (Table 1)
6. scale_bridging_7b - 7B scale validation
7. signal_survival_multiscale - Signal × scale effectiveness
8. rl_observational_case_study - Observational RL case study
9. observational_72b - 72B observational
10. closed_weight_2signal_mode - Closed-weight degraded mode
11. multi_family_validation - Llama cross-family validation

Now I'm ready to compose the paper with all these experiments integrated into the narrative.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dd06dee-1c52-47ba-b792-f4b36f9999d4",
  "isSidechain": false,
  "requestId": "req_011Cb2uHCZXJgb4zAmzAoAhR",
  "type": "assistant",
  "uuid": "915f2d3f-289b-4612-819d-f0f52c658ebb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AeKe9BonRJvGZYDp5vZL7U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25772,
      "cache_read_input_tokens": 23272,
      "output_tokens": 448,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25772,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 448,
          "cache_read_input_tokens": 23272,
          "cache_creation_input_tokens": 25772,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25772
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

_source line 15 · 2026-05-14T18:04:00.365Z_

Now let me ensure the output directory exists and write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "915f2d3f-289b-4612-819d-f0f52c658ebb",
  "isSidechain": false,
  "requestId": "req_011Cb2uHCZXJgb4zAmzAoAhR",
  "type": "assistant",
  "uuid": "c0c15379-ab3c-4f99-a933-17f678f08408",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AeKe9BonRJvGZYDp5vZL7U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25772,
      "cache_read_input_tokens": 23272,
      "output_tokens": 448,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25772,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 448,
          "cache_read_input_tokens": 23272,
          "cache_creation_input_tokens": 25772,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25772
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

_source line 16 · 2026-05-14T18:04:01.068Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HLaLVfYzUcSsi1W3vAHm44`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best/",
  "description": "List output directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0c15379-ab3c-4f99-a933-17f678f08408",
  "isSidechain": false,
  "requestId": "req_011Cb2uHCZXJgb4zAmzAoAhR",
  "type": "assistant",
  "uuid": "fb958d43-b5cf-4eb3-83fb-cc8718f40d10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AeKe9BonRJvGZYDp5vZL7U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25772,
      "cache_read_input_tokens": 23272,
      "output_tokens": 448,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25772,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 448,
          "cache_read_input_tokens": 23272,
          "cache_creation_input_tokens": 25772,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25772
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

_source line 17 · 2026-05-14T18:04:01.236Z_

<details><summary>↩ Tool result · `toolu_01HLaLVfYzUcSsi1W3vAHm44`</summary>

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
  "parentUuid": "fb958d43-b5cf-4eb3-83fb-cc8718f40d10",
  "isSidechain": false,
  "promptId": "14a905e9-cf62-4ad0-acbf-909375bdc04c",
  "type": "user",
  "uuid": "ff797d39-36a4-48a4-848e-9d0a050c6980",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "fb958d43-b5cf-4eb3-83fb-cc8718f40d10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T18:08:57.379Z_

<details open><summary>🔧 Tool call — Write · `toolu_01RF9jxbbfDgnNCABHHYPDEA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{bm}\n\\usepackage{microtype}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{array}\n\n\\newcommand{\\contamcal}{\\textsc{ContamCal}}\n\\newcommand{\\pp}{\\,\\text{pp}}\n\n\\title{\\contamcal{}: Calibrating Benchmark Scores for Training Data Contamination\\\\via Contamination-Augmented Item Response Theory}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n%======================================================================\n\\begin{abstract}\n%======================================================================\nTraining data contamination inflates LLM benchmark scores, yet existing detection methods flag contamination without answering: \\emph{what would this model score if it had never seen the test data?}\nWe introduce \\contamcal{}, a two-stage framework that bridges contamination detection and score calibration.\nStage~1 computes item-level contamination exposure via four complementary detection signals---embedding similarity, Min-K++, ConStat, and LLM self-critique---aggregated through Reciprocal Rank Fusion (RRF).\nStage~2 fits a contamination-augmented 4PL Item Response Theory model with per-benchmark contamination susceptibility parameters~$\\gamma_k$ and a measurement error model that propagates signal uncertainty into Bayesian posteriors.\nOn controlled contamination injection experiments across Qwen2.5 (0.5B--7B) and Llama-3.2-1B with three benchmarks (MMLU, GSM8K, ARC-Challenge), \\contamcal{} recovers true benchmark performance within 1.8\\pp{} MAE (bootstrap 95\\% CI: [1.2, 2.4]) with 94\\% credible interval coverage, while naive scores overestimate by up to 58\\pp{} under full contamination (3B GSM8K).\nWe systematically characterize signal effectiveness as method-specific and scale-dependent: embedding similarity is robust across scales (AUC$>$0.95), whereas Min-K++ and self-critique fail at 0.5B (AUC$\\approx$0.47) but recover at 1.5B+ (AUC$>$0.70).\nFisher Information analysis establishes AUC$\\geq$0.55 as the structural identifiability boundary and AUC$\\geq$0.70 as the practical boundary for reliable calibration.\n\\end{abstract}\n\n%======================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%======================================================================\n\nBenchmark contamination---where test data leaks into training corpora---is among the most serious threats to the validity of LLM evaluation \\citep{sainz2023contamination,balloccu2024leak,li2024task}.\nEven rephrased test items can inflate accuracy by 8--15 points while evading $n$-gram decontamination \\citep{yang2023rethinking,dekoninck2024evading}.\n\\citet{xu2024benchmark} systematically tested 20 mitigation strategies and found none reliably eliminates contamination effects.\n\nThis motivates a fundamental reframing: rather than trying to eliminate contamination from benchmarks (which does not work), we propose to \\emph{statistically control for it}---measuring its effect and subtracting it out with proper uncertainty quantification.\nThis mirrors the shift in causal inference from eliminating confounders to statistically adjusting for them \\citep{rosenbaum1983central}.\n\nExisting approaches address only part of the problem.\nDetection methods---Min-K\\%++ \\citep{shi2024detecting}, ConStat \\citep{dekoninck2024constat}, and LLM self-critique \\citep{yang2023rethinking}---flag contamination but do not calibrate scores.\nIRT-based evaluation \\citep{lalor2024benchmarking,polo2024tinybenchmarks} models item difficulty psychometrically but ignores contamination.\nDCR \\citep{dong2024generalization} provides adjusted accuracy but lacks uncertainty bounds.\nHiBayES \\citep{zhuang2024hibayes} provides Bayesian model evaluation but does not account for contamination.\n\nWe introduce \\contamcal{}, which bridges detection and calibration through a two-stage pipeline grounded in the educational measurement tradition of item compromise IRT \\citep{eckerly2017detecting,sinharay2017use} and explanatory IRT \\citep{deboeck2004explanatory}.\nOur framework makes three non-trivial adaptations for LLM evaluation: (a)~independent examinees become a single model with joint item distributions, altering local independence semantics; (b)~binary leakage becomes continuous exposure scores requiring measurement error propagation; and (c)~stable ability becomes regime-conditional ability requiring scale-aware signal selection.\n\nOur contributions are:\n\\begin{enumerate}\n\\item The \\contamcal{} framework: a two-stage pipeline (RRF provenance mapping $\\to$ contamination-augmented 4PL IRT with per-benchmark $\\gamma_k$ and measurement error model) producing calibrated scores with credible intervals (\\S\\ref{sec:method}).\n\\item Systematic signal effectiveness characterization: a signal $\\times$ scale $\\times$ dosage AUC mapping revealing method-specific, scale-dependent reliability, including a cautionary finding on Min-K++ directional reversal (\\S\\ref{sec:signal_analysis}).\n\\item Dual-track validation: controlled SFT injection across 0.5B--7B within Qwen2.5 plus Llama-3.2-1B (internal validity), and ecological observational studies on Instruct and DeepSeek-R1 models up to 72B (external validity) (\\S\\ref{sec:experiments}).\n\\end{enumerate}\n\n%======================================================================\n\\section{Related Work}\n\\label{sec:related}\n%======================================================================\n\n\\paragraph{Contamination Detection.}\nSeveral methods detect training data memorization in LLMs.\nMin-K\\%++ \\citep{shi2024detecting} uses token-level probability outliers; ConStat \\citep{dekoninck2024constat} exploits performance gaps between original and paraphrased items; KDS \\citep{zhang2024kds} and CDD \\citep{li2024cdd} provide detection datasets.\n\\citet{yang2023rethinking} propose LLM self-critique for contamination detection.\nThese methods flag items but do not produce calibrated scores.\n\n\\paragraph{IRT for LLM Evaluation.}\nItem Response Theory has been applied to LLM evaluation \\citep{lalor2024benchmarking,polo2024tinybenchmarks}, dynamic benchmarks \\citep{white2024livebench}, and Bayesian model comparison \\citep{zhuang2024hibayes}.\nNone model contamination as a covariate.\nOur approach builds on explanatory IRT \\citep{deboeck2004explanatory,adams1997multidimensional} and the item compromise literature \\citep{eckerly2017detecting,sinharay2017use}.\n\n\\paragraph{Contamination Mitigation.}\nDCR \\citep{dong2024generalization} uses fuzzy inference for adjusted accuracy.\n\\citet{xu2024benchmark} demonstrate that rephrasing, option shuffling, and other mitigation strategies all fail.\nDynamic benchmarks like LiveBench \\citep{white2024livebench} sidestep the problem through continuous curation.\nOur approach is complementary: \\contamcal{} provides a statistical safety net for existing static benchmarks.\n\n\\paragraph{Calibration and Uncertainty.}\nWe distinguish our use of ``calibration'' from probability calibration \\citep{guo2017calibration,platt1999probabilistic}: we calibrate \\emph{aggregate benchmark scores} for contamination bias, not per-item prediction confidences.\nFor uncertainty quantification, conformal prediction \\citep{angelopoulos2023conformal} offers distribution-free coverage guarantees; we prefer Bayesian IRT because it naturally incorporates item-level contamination covariates and produces interpretable $\\gamma_k$ parameters.\n\n\\paragraph{Differential Item Functioning.}\nOur per-benchmark $\\gamma_k$ is conceptually related to DIF \\citep{holland1993differential,thissen1993detection,zumbo1999handbook}, where item parameters differ between exposure groups.\nHowever, DIF traditionally compares demographic subgroups of examinees; we compare contamination exposure levels of items evaluated by a single model.\n\n%======================================================================\n\\section{Method}\n\\label{sec:method}\n%======================================================================\n\n\\contamcal{} operates in two stages: (1)~item-level contamination exposure estimation via multi-signal fusion, and (2)~contamination-augmented IRT calibration.\n\n\\subsection{Stage 1: Multi-Signal Exposure Estimation}\n\\label{sec:stage1}\n\nFor each benchmark item $i$ evaluated by model $j$, we compute four detection signals:\n\n\\paragraph{S1: Embedding Similarity.}\nCosine similarity between the item embedding and its nearest neighbor in the known training corpus.\nThis training-data-independent signal is robust across model scales.\n\n\\paragraph{S2: Min-K++.}\nToken-level probability outlier detection \\citep{shi2024detecting}, computed from model $j$'s own output probabilities.\nRequires logit access (open-weight models).\n\n\\paragraph{S3: ConStat.}\nPerformance gap between the original item and semantically equivalent paraphrases \\citep{dekoninck2024constat}.\nRelies on generating multiple paraphrases per item.\n\n\\paragraph{S4: LLM Self-Critique.}\nThe model generates an explanation of its own familiarity with the item; contaminated items exhibit characteristic low-entropy self-assessment patterns.\n\n\\paragraph{Reciprocal Rank Fusion.}\nWe aggregate the four signals using RRF \\citep{cormack2009reciprocal}:\n\\begin{equation}\n\\text{RRF}(i) = \\sum_{s=1}^{4} \\frac{1}{k + r_s(i)}\n\\end{equation}\nwhere $r_s(i)$ is the rank of item $i$ under signal $s$ and $k=60$ is the standard damping constant.\nRRF is a training-free aggregation---a principled design choice avoiding meta-circularity (a learned aggregator's training data may itself be contaminated).\nThe RRF score is normalized to $[0,1]$ to yield the continuous exposure estimate $\\hat{\\tau}_i$.\n\n\\subsection{Stage 2: Contamination-Augmented 4PL IRT}\n\\label{sec:stage2}\n\n\\paragraph{Base Model.}\nWe extend the 4-parameter logistic IRT model.\nFor model $j$ responding to item $i$ on benchmark $k$:\n\\begin{equation}\nP(Y_{ij}=1 \\mid \\theta_j, \\bm{\\xi}_i, \\tau_i) = c_i + \\frac{d_i - c_i}{1 + \\exp\\!\\bigl(-a_i(\\theta_j + \\gamma_k \\tau_i - b_i)\\bigr)}\n\\label{eq:4pl}\n\\end{equation}\nwhere $\\theta_j$ is model ability, $a_i$ is item discrimination, $b_i$ is difficulty, $c_i$ is guessing, $d_i$ is the upper asymptote, $\\tau_i \\in [0,1]$ is the latent contamination exposure, and $\\gamma_k$ is the per-benchmark contamination susceptibility.\n\nThe calibrated score for model $j$ on benchmark $k$ is:\n\\begin{equation}\n\\hat{s}_{jk}^{\\text{calib}} = \\frac{1}{n_k} \\sum_{i \\in k} P(Y_{ij}=1 \\mid \\theta_j, \\bm{\\xi}_i, \\tau_i=0)\n\\end{equation}\ni.e., the expected accuracy under zero contamination exposure.\n\n\\paragraph{Measurement Error Model.}\nStage~1 produces noisy exposure estimates $\\hat{\\tau}_i$.\nWe model:\n\\begin{equation}\n\\hat{\\tau}_i = \\tau_i + \\epsilon_i, \\quad \\epsilon_i \\sim \\mathcal{N}(0, \\sigma_e^2)\n\\end{equation}\nwhere $\\sigma_e$ is estimated from the signal pipeline's false positive/negative rates.\nThis measurement error model propagates signal uncertainty into the IRT posterior, producing wider credible intervals when signals are noisy.\n\n\\paragraph{Per-Benchmark $\\gamma_k$.}\nRather than estimating a single global $\\gamma$, we fit per-benchmark $\\gamma_k$ to capture contamination susceptibility heterogeneity.\nThis is motivated by the observation that different benchmark formats (multiple-choice vs.\\ free-form) and content types (factual recall vs.\\ reasoning) exhibit markedly different vulnerability to memorization.\n\n\\paragraph{Fisher Information and Identifiability.}\nThe Fisher Information for $\\gamma_k$ in the 4PL+$\\gamma$ model is:\n\\begin{equation}\nI(\\gamma_k) = \\sum_{i \\in k} \\sum_j \\tau_i^2 \\cdot a_i^2 \\cdot P_{ij}(1-P_{ij}) \\cdot \\left(\\frac{d_i - c_i}{P_{ij} - c_i}\\right)^2 \\frac{1}{(d_i - c_i)^2}\n\\end{equation}\nWhen signal AUC is low ($\\hat{\\tau}$ is nearly uninformative), $\\tau_i$ estimates cluster near 0.5 with low variance, and $I(\\gamma_k) \\to 0$---$\\gamma_k$ becomes structurally unidentifiable.\nOur simulation study (\\S\\ref{sec:identifiability}) establishes AUC$\\geq$0.55 as the structural identifiability boundary ($I(\\gamma_k) > 0$) and AUC$\\geq$0.70 as the practical boundary (CI$_{95}$ width $<$ 10\\pp{} at $N\\geq 50$ models).\n\n\\paragraph{Local Independence.}\nStandard IRT assumes independent examinees.\nIn LLM evaluation, a single model produces all item responses, introducing correlations through shared parameters.\nWe mitigate this by fitting IRT per-benchmark (reducing correlation scope) and empirically verifying via posterior predictive checks on item-level residual correlations (mean $r = 0.032$, max $r = 0.085$; \\S\\ref{sec:main_results}).\n\n\\paragraph{Inference.}\nAll models are fit via Hamiltonian Monte Carlo (4 chains, 2000 warmup + 2000 sampling iterations).\nWe verify convergence with $\\hat{R} < 1.01$ and report zero divergences across all fits.\n\n%======================================================================\n\\section{Signal Effectiveness Analysis}\n\\label{sec:signal_analysis}\n%======================================================================\n\nBefore calibration, we systematically characterize signal reliability across model scales, contamination dosages, and benchmarks.\n\n\\subsection{Signal $\\times$ Scale AUC Mapping}\n\nTable~\\ref{tab:signal_scale_auc} reports item-level detection AUC at 5\\% contamination dosage (d005) across three model scales.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Signal detection AUC at d005 across model scales and benchmarks. S1 (Embedding) is robust across scales; S2 (Min-K++), S3 (ConStat), and S4 (Self-Critique) fail at 0.5B but recover at 1.5B+.}\n\\label{tab:signal_scale_auc}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Signal} & \\textbf{Benchmark} & \\textbf{0.5B} & \\textbf{1.5B} & \\textbf{3B} \\\\\n\\midrule\n\\multirow{3}{*}{S1 Embedding}\n & MMLU   & 0.953 & 0.961 & 0.948 \\\\\n & GSM8K  & 0.988 & 0.985 & 0.982 \\\\\n & ARC-C  & 0.995 & 0.990 & 0.991 \\\\\n\\midrule\n\\multirow{3}{*}{S2 Min-K++}\n & MMLU   & 0.466 & 0.718 & 0.798 \\\\\n & GSM8K  & 0.465 & 0.762 & 0.842 \\\\\n & ARC-C  & 0.466 & 0.741 & 0.816 \\\\\n\\midrule\n\\multirow{3}{*}{S3 ConStat}\n & MMLU   & $\\sim$0.55 & 0.795 & 0.836 \\\\\n & GSM8K  & $\\sim$0.53 & 0.832 & 0.873 \\\\\n & ARC-C  & $\\sim$0.52 & 0.814 & 0.855 \\\\\n\\midrule\n\\multirow{3}{*}{S4 Self-Critique}\n & MMLU   & 0.517 & 0.692 & 0.751 \\\\\n & GSM8K  & 0.495 & 0.731 & 0.792 \\\\\n & ARC-C  & 0.433 & 0.712 & 0.775 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nS1 (Embedding Similarity) is robust across all scales (AUC $>$ 0.95) because it relies on training-data-independent semantic similarity.\nS2 (Min-K++) and S4 (Self-Critique) are near-random at 0.5B (AUC $\\approx$ 0.47) but cross the practical threshold of 0.70 at 1.5B.\nThis scale-dependent behavior reflects underlying capacity requirements: Min-K++ depends on token-level memorization capacity (LoRA adapter sizes grow from 34MB at 0.5B to 115MB at 3B), while Self-Critique requires sufficient generation quality for metacognitive self-assessment.\n\n\\subsection{Signal Survival Across Scales}\n\nTable~\\ref{tab:signal_survival} summarizes the effective number of signals at each scale.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal effectiveness summary across scales. Effective signals (AUC $\\geq$ 0.70) increase from 1 at 0.5B to 4 at 3B.}\n\\label{tab:signal_survival}\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Signal} & \\textbf{0.5B} & \\textbf{1.5B} & \\textbf{3B} & \\textbf{Status} \\\\\n\\midrule\nS1 Embed. & 0.979 & 0.979 & 0.974 & Robust \\\\\nS2 Min-K++ & 0.465 & 0.740 & 0.819 & Recovers 1.5B+ \\\\\nS3 ConStat & $\\sim$0.53 & 0.814 & 0.855 & Recovers 1.5B+ \\\\\nS4 Self-Crit. & 0.481 & 0.712 & 0.773 & Recovers 1.5B+ \\\\\n\\midrule\n\\# Effective & 1 & 3 & 4 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 0.5B, only S1 is effective; RRF degrades to a dominant-signal mode (S1 weight share: 89\\%).\nAt 1.5B, three signals cross the 0.70 threshold, enabling genuine multi-signal fusion (S1 weight share drops to 38\\%).\nAt 3B, all four signals are effective (S1 weight share: 31\\%).\n\n\\subsection{Min-K++ Directional Reversal}\n\\label{sec:reversal}\n\nA critical cautionary finding: at high contamination dosage (d100), Min-K++ exhibits \\emph{directional reversal}---contaminated items receive \\emph{lower} scores than clean items, actively misleading rather than merely failing.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Min-K++ directional reversal at d100 (Cohen's $d$; negative = reversed direction). The reversal persists across scales but attenuates with increasing model size.}\n\\label{tab:reversal}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Benchmark} & \\textbf{0.5B} & \\textbf{1.5B} & \\textbf{3B} \\\\\n\\midrule\nMMLU  & $-$1.22 & $-$1.08 & $-$0.85 \\\\\nGSM8K & $-$2.67 & $-$1.78 & $-$1.31 \\\\\nARC-C & $-$2.05 & $-$1.71 & $-$1.26 \\\\\n\\midrule\nMean  & $-$1.98 & $-$1.52 & $-$1.14 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe reversal attenuates with scale ($-$1.98 at 0.5B $\\to$ $-$1.14 at 3B) as larger models' perplexity distributions become more stable, but persists at all tested scales.\nThis strengthens the case for robust aggregation: Min-K++ should be used with extreme caution under high contamination dosage at any scale.\n\n\\subsection{RRF Aggregation Ablation}\n\\label{sec:rrf}\n\nTable~\\ref{tab:rrf} compares RRF against single-signal baselines and alternative aggregation strategies.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Detection AUC (d005, benchmark-averaged): RRF vs.\\ single-signal and alternative aggregation methods.}\n\\label{tab:rrf}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{0.5B} & \\textbf{1.5B} & \\textbf{3B} \\\\\n\\midrule\nRRF 4-signal     & 0.962 & 0.924 & 0.943 \\\\\nS1 only          & 0.979 & 0.972 & 0.964 \\\\\nS2 only          & 0.465 & 0.740 & 0.819 \\\\\nS3 only          & 0.533 & 0.814 & 0.855 \\\\\nS4 only          & 0.481 & 0.712 & 0.773 \\\\\nRRF 2-sig (closed) & 0.508 & 0.782 & 0.831 \\\\\nEqual-wt rank avg & --- & 0.908 & --- \\\\\nCalibrated wt RRF & --- & 0.931 & --- \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{FP robustness (4-signal RRF):}} \\\\\n5\\% FP injection  & \\multicolumn{3}{c}{AUC drop: 0.008} \\\\\n10\\% FP injection & \\multicolumn{3}{c}{AUC drop: 0.014} \\\\\n15\\% FP injection & \\multicolumn{3}{c}{AUC drop: 0.023} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 0.5B, RRF (0.962) is slightly below S1-only (0.979) because near-random S2/S4 signals dilute the fusion.\nThis is an honest characterization of the degraded regime: RRF gracefully degrades rather than catastrophically failing.\nAt 1.5B+, RRF enables genuine multi-signal fusion with complementary information.\nCalibrated weighted RRF (0.931 at 1.5B) provides marginal improvement over standard RRF (0.924) but introduces a training dependency, supporting our design choice of training-free RRF.\nRRF is robust to false positive injection: 15\\% FP injection causes only a 2.3\\% AUC drop, owing to rank-based aggregation's natural outlier resistance.\n\n%======================================================================\n\\section{Experiments}\n\\label{sec:experiments}\n%======================================================================\n\n\\subsection{Experimental Setup}\n\n\\paragraph{Controlled Contamination Injection.}\nWe train Qwen2.5 models (0.5B, 1.5B, 3B) via LoRA SFT at five contamination dosages: d000 (0\\%), d005 (5\\%), d025 (25\\%), d050 (50\\%), d100 (100\\%) of benchmark items injected as paraphrased training data, with 3 random seeds each, totaling 45 model instances per benchmark.\nGround-truth clean accuracy is established from d000 models.\n\n\\paragraph{Benchmarks.}\nMMLU (14K items, multiple-choice), GSM8K ($\\sim$1.3K items, free-form math), and ARC-Challenge (science reasoning, multiple-choice).\n\n\\paragraph{Baselines.}\nWe compare against 7 methods: (B0)~Raw scores, (B1)~Remove-and-rescore, (B2)~Single-signal 2PL+$\\gamma$, (B3)~Vanilla 4PL (no contamination), (B4)~Linear regression + bootstrap CI, (B5)~Emperor mitigation strategies \\citep{xu2024benchmark}, and (B6)~DCR fuzzy inference \\citep{dong2024generalization}.\n\n\\paragraph{Metrics.}\n(1)~MAE between calibrated and true accuracy with bootstrap 95\\% CIs; (2)~credible interval coverage at 50\\%/80\\%/95\\%; (3)~average CI width; (4)~Kendall's $\\tau$ for ranking preservation; (5)~dose-response monotonicity.\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Main results: 8 methods on 5 evaluation metrics across Qwen2.5 (0.5B--3B) $\\times$ 3 benchmarks $\\times$ 5 dosages $\\times$ 3 seeds. \\contamcal{} achieves the lowest MAE and the only near-nominal coverage. ``---'' indicates the method does not produce credible intervals.}\n\\label{tab:main}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{MAE (pp)$\\downarrow$} & \\textbf{95\\% Cov.$\\uparrow$} & \\textbf{CI Width (pp)$\\downarrow$} & \\textbf{Kendall $\\tau$$\\uparrow$} & \\textbf{Mono.} \\\\\n\\midrule\n4PL+$\\gamma$ ME (ours) & \\textbf{1.8} [1.2, 2.4] & \\textbf{94\\%} & 4.2 & \\textbf{0.96} & 0.95 \\\\\nB0: Raw                & 8.2          & ---    & ---  & 0.87 & --- \\\\\nB1: Remove-rescore     & 4.6          & ---    & ---  & 0.91 & --- \\\\\nB2: 2PL+$\\gamma$ (S1)  & 2.9          & 81\\%   & 5.6  & 0.94 & 0.90 \\\\\nB3: Vanilla 4PL        & 6.5          & 58\\%   & 3.2  & 0.89 & --- \\\\\nB4: Linear + boot      & 3.2          & 76\\%   & 6.8  & 0.93 & 0.85 \\\\\nB5: Emperor mitig.     & 5.8          & ---    & ---  & 0.89 & --- \\\\\nB6: DCR fuzzy          & 3.9          & ---    & ---  & 0.92 & 0.80 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\contamcal{} achieves 1.8\\pp{} MAE with bootstrap 95\\% CI [1.2, 2.4], significantly outperforming the best baseline DCR (3.9\\pp{}).\nIt is the only method producing near-nominal 95\\% credible interval coverage (94\\%), compared to 58--81\\% for baselines that produce intervals.\nVanilla 4PL's 58\\% coverage demonstrates that IRT without contamination modeling produces dangerously narrow, miscalibrated intervals.\nOur 80\\% and 50\\% coverage rates (83\\% and 52\\%, respectively) further confirm well-calibrated uncertainty.\nKendall's $\\tau = 0.96$ indicates high-fidelity ranking preservation.\nMCMC diagnostics are clean: zero divergences, $\\hat{R}_{\\max} = 1.008$, minimum ESS $= 850$.\nResidual correlations are low (mean $r = 0.032$, max $r = 0.085$), indicating acceptable local independence.\n\n\\subsection{Per-Benchmark Analysis}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-benchmark MAE (pp) for \\contamcal{} vs.\\ key baselines.}\n\\label{tab:per_bench}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Bench.} & \\textbf{Ours} & \\textbf{B0 Raw} & \\textbf{B2 2PL} & \\textbf{B6 DCR} \\\\\n\\midrule\nMMLU  & 1.1 & 4.3  & 1.8 & 2.5 \\\\\nGSM8K & 2.8 & 14.6 & 4.2 & 6.2 \\\\\nARC-C & 1.2 & 4.8  & 2.0 & 2.8 \\\\\n\\midrule\nAvg.  & 1.8 & 8.2  & 2.9 & 3.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGSM8K shows the largest raw inflation (14.6\\pp{}) and the highest residual after calibration (2.8\\pp{}), reflecting the extreme sensitivity of free-form math benchmarks to memorization.\nMMLU (1.1\\pp{}) and ARC-C (1.2\\pp{}) are well calibrated across all dosages.\n\n\\paragraph{Per-Benchmark $\\gamma_k$ Estimates.}\nThe estimated contamination susceptibility parameters reveal striking heterogeneity:\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-benchmark $\\gamma_k$ estimates. GSM8K is ${\\sim}4\\times$ more susceptible to contamination than MMLU or ARC-C.}\n\\label{tab:gamma}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Benchmark} & $\\gamma_k$ & \\textbf{95\\% CI} \\\\\n\\midrule\nMMLU  & 0.22 & [0.08, 0.38] \\\\\nGSM8K & 0.85 & [0.62, 1.12] \\\\\nARC-C & 0.18 & [0.04, 0.34] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $\\gamma_k$ heterogeneity is statistically significant ($\\chi^2$ test, $p = 0.002$), confirming that per-benchmark fitting is essential.\nA joint model with a shared global $\\gamma = 0.41$ yields MAE of 2.6\\pp{}, worse than per-benchmark fitting (1.8\\pp{}): the global model overfits MMLU while underfitting GSM8K.\n\n\\paragraph{Per-Scale MAE.}\n\\contamcal{} achieves 2.3\\pp{} at 0.5B, 1.4\\pp{} at 1.5B, and 1.6\\pp{} at 3B.\nThe higher MAE at 0.5B reflects degraded signal quality (only S1 effective), leading to noisier exposure estimates.\nThe measurement error model compensates with wider CIs, providing honest uncertainty quantification even in this degraded regime.\n\n\\subsection{Dose-Response: 3B GSM8K}\n\\label{sec:dose_response}\n\nTable~\\ref{tab:dose_response} presents the most dramatic calibration case.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Dose-response for 3B GSM8K. Naive scores inflate by up to 57.7\\pp{}; \\contamcal{} recovers true performance within 4.2\\pp{}.}\n\\label{tab:dose_response}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Dose} & \\textbf{Obs.} & \\textbf{Calib.} & \\textbf{True} & \\textbf{Resid.} \\\\\n\\midrule\nd000 (0\\%)   & 12.0\\% & ---    & 12.0\\% & --- \\\\\nd005 (5\\%)   & 20.8\\% & 13.2\\% & 12.0\\% & +1.2\\pp{} \\\\\nd025 (25\\%)  & $\\sim$35.4\\% & 14.5\\% & 12.0\\% & +2.5\\pp{} \\\\\nd050 (50\\%)  & $\\sim$51.8\\% & 15.1\\% & 12.0\\% & +3.1\\pp{} \\\\\nd100 (100\\%) & 69.7\\% & 16.2\\% & 12.0\\% & +4.2\\pp{} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt full contamination (d100), the observed score of 69.7\\% is 57.7\\pp{} above the true score of 12.0\\%.\n\\contamcal{} reduces this to a 4.2\\pp{} residual.\nEven at moderate contamination (d025), naive scores overestimate by $\\sim$23\\pp{}, while our calibration achieves a 2.5\\pp{} residual.\n\n\\subsection{Identifiability and Simulation Study}\n\\label{sec:identifiability}\n\nWe conduct a 120-condition simulation sweep varying signal AUC ($\\in \\{0.55, 0.65, 0.70, 0.80, 0.90\\}$) and number of models ($N \\in \\{20, 50, 100\\}$) at $\\gamma_{\\text{true}} = 0.5$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$\\gamma$ recovery from the simulation sweep. AUC $\\geq 0.70$ at $N \\geq 50$ is the practical identifiability sweet spot (CI $<$ 7\\pp{}, coverage $\\geq$ 95\\%).}\n\\label{tab:identifiability}\n\\begin{tabular}{cccccc}\n\\toprule\n\\textbf{AUC} & $N$ & \\textbf{Bias} & \\textbf{RMSE} & \\textbf{CI$_{95}$ (pp)} & \\textbf{Cov.} \\\\\n\\midrule\n0.55 & 20  & +0.020 & 0.040 & 13.3 & 80\\% \\\\\n0.55 & 50  & +0.015 & 0.026 & 8.7  & 90\\% \\\\\n0.55 & 100 & $-$0.003 & 0.004 & 6.5 & 100\\% \\\\\n\\midrule\n0.65 & 20  & +0.016 & 0.035 & 11.8 & 85\\% \\\\\n0.65 & 50  & +0.010 & 0.020 & 7.6  & 93\\% \\\\\n0.65 & 100 & $-$0.004 & 0.008 & 5.8 & 97\\% \\\\\n\\midrule\n0.70 & 50  & +0.008 & 0.018 & 7.0  & 95\\% \\\\\n0.70 & 100 & $-$0.002 & 0.006 & 5.3 & 98\\% \\\\\n\\midrule\n0.80 & 50  & +0.006 & 0.014 & 6.2  & 96\\% \\\\\n0.80 & 100 & +0.003 & 0.005 & 4.8  & 98\\% \\\\\n\\midrule\n0.90 & 50  & +0.004 & 0.010 & 5.4  & 97\\% \\\\\n0.90 & 100 & +0.002 & 0.004 & 4.2  & 99\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFisher Information analysis yields AUC $\\geq 0.52$ as the structural identifiability boundary and AUC $\\geq 0.70$ as the practical boundary.\nThe latter corresponds precisely to the Min-K++ AUC at 1.5B ($\\sim$0.74), confirming that 1.5B is the minimum scale for reliable multi-signal calibration.\nCI width scales as approximately $1/\\sqrt{N}$ (empirical ratio $N_{20}/N_{100} = 2.04$ at AUC=0.55; theoretical: 2.24).\nCoverage at $N=20$ falls below nominal (80--85\\%) due to a known small-$N$ IRT limitation.\nAll fits converge with zero divergences and $\\hat{R}_{\\max} = 1.012$.\n\nAdditional findings: continuous exposure scores produce $\\sim$8\\% narrower CIs than binary indicators.\nInformative priors (SD=0.5) narrow CIs by 18\\%, while vague priors (SD=2.0) widen them by 28\\%.\n\n\\subsection{Measurement Error Model}\n\\label{sec:me_model}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Measurement error (ME) model vs.\\ simple model. At high noise ($\\sigma_e = 0.5$), the simple model's coverage collapses to 65\\%; the ME model maintains 91\\%.}\n\\label{tab:me}\n\\begin{tabular}{lcccc}\n\\toprule\n$\\sigma_e$ & \\textbf{ME Cov.} & \\textbf{ME CI (pp)} & \\textbf{Simple Cov.} & \\textbf{Simple CI (pp)} \\\\\n\\midrule\n0.1 & 95\\% & 5.2 & 91\\% & 4.8 \\\\\n0.3 & 93\\% & 7.8 & 78\\% & 5.1 \\\\\n0.5 & 91\\% & 11.4 & 65\\% & 5.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt low noise ($\\sigma_e = 0.1$), both models perform similarly.\nAt $\\sigma_e = 0.3$ (typical for real signal pipelines based on observed FP/FN rates), the ME model maintains 93\\% coverage while the simple model drops to 78\\%.\nAt $\\sigma_e = 0.5$, the simple model's coverage collapses to 65\\%---dangerously miscalibrated---while the ME model maintains 91\\%.\nThe wider CIs under the ME model reflect genuine epistemic uncertainty: models with degraded signals receive appropriately wider intervals.\n\nPost-hoc noise injection experiments confirm super-linear CI widening: $1.0\\times$ noise widens $\\gamma$ CI by 28\\%, $1.5\\times$ by 52\\%, and $2.0\\times$ by 83\\%.\n\n\\subsection{Scale Bridging: 7B Validation}\n\\label{sec:7b}\n\nTo address scale concerns, we extend controlled contamination injection to Qwen2.5-7B.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Qwen2.5-7B dose-response and signal quality.}\n\\label{tab:7b_dose}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Dosage} & \\textbf{MMLU} & \\textbf{GSM8K} & \\textbf{ARC-C} \\\\\n\\midrule\nd000 & 71.8\\% & 79.2\\% & 87.8\\% \\\\\nd005 & 72.6\\% (+0.8) & 80.4\\% (+1.2) & 88.1\\% (+0.3) \\\\\nd025 & 74.3\\% (+2.5) & 85.0\\% (+5.8) & 89.2\\% (+1.4) \\\\\nd100 & 75.9\\% (+4.1) & 91.7\\% (+12.5) & 90.6\\% (+2.8) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal AUC at 7B (d005). All four signals are effective, with continued improvement over 3B.}\n\\label{tab:7b_signal}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Signal} & \\textbf{MMLU} & \\textbf{GSM8K} & \\textbf{ARC-C} & \\textbf{Mean} \\\\\n\\midrule\nS1 Embedding & 0.948 & 0.971 & 0.943 & 0.954 \\\\\nS2 Min-K++   & 0.851 & 0.896 & 0.865 & 0.871 \\\\\nS3 ConStat   & 0.872 & 0.908 & 0.881 & 0.887 \\\\\nS4 Self-Crit.& 0.795 & 0.834 & 0.808 & 0.812 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 7B, \\contamcal{} achieves 1.4\\pp{} MAE with 95\\% coverage and Kendall's $\\tau = 0.97$---the best performance across all scales.\nSignal quality continues to improve (S2 AUC: 0.871; S4 AUC: 0.812), confirming that larger models are easier to calibrate.\n\n\\subsection{Multi-Family Validation: Llama-3.2-1B}\n\\label{sec:multi_family}\n\nTo test cross-family generalization, we repeat 3-dosage (d000/d025/d100) controlled SFT injection on Llama-3.2-1B.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-family $\\gamma$ comparison. High consistency (Pearson $r = 0.91$) suggests contamination susceptibility is a benchmark property, not model-family-specific.}\n\\label{tab:cross_family}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Bench.} & \\textbf{Qwen2.5 $\\gamma$} & \\textbf{Llama $\\gamma$} & \\textbf{Diff.} \\\\\n\\midrule\nMMLU  & 0.22 & 0.19 & $-$0.03 \\\\\nGSM8K & 0.85 & 0.72 & $-$0.13 \\\\\nARC-C & 0.18 & 0.16 & $-$0.02 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\contamcal{} achieves 2.1\\pp{} MAE with 92\\% coverage on Llama.\nThe $\\gamma$ estimates are highly consistent across families (Pearson $r = 0.91$), suggesting that contamination susceptibility is primarily a benchmark property (item structure, format, memorability) rather than a model-family artifact.\nLlama's S2 AUC (0.698) falls just below the 0.70 practical threshold at the $\\sim$1B scale, consistent with the simulation sweep predictions.\n\n\\subsection{Closed-Weight Mode}\n\\label{sec:closed_weight}\n\nFor closed-weight models lacking logit/embedding access, \\contamcal{} operates in a 2-signal mode using only S3 (ConStat) and S4 (Self-Critique).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{4-signal vs.\\ 2-signal (closed-weight) mode. At 1.5B+, 2-signal mode matches or outperforms the best existing baseline (DCR: 3.9\\pp{}).}\n\\label{tab:closed_weight}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Scale} & \\textbf{4-Sig MAE} & \\textbf{2-Sig MAE} & \\textbf{Gap} & \\textbf{2-Sig AUC} \\\\\n\\midrule\n0.5B & 2.3\\pp{} & 6.8\\pp{} & +4.5\\pp{} & 0.508 \\\\\n1.5B & 1.4\\pp{} & 2.8\\pp{} & +1.4\\pp{} & 0.782 \\\\\n3B   & 1.6\\pp{} & 2.1\\pp{} & +0.5\\pp{} & 0.831 \\\\\n\\midrule\nAvg. & 1.8\\pp{} & 3.9\\pp{} & +2.1\\pp{} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 0.5B, 2-signal mode nearly fails (6.8\\pp{} MAE) because both S3 and S4 are ineffective at this scale.\nAt 1.5B+, 2-signal mode provides meaningful calibration (2.1--2.8\\pp{} MAE), matching DCR's 3.9\\pp{} aggregate while additionally providing credible intervals (86\\% coverage).\nPractical guidance: closed-weight mode requires $\\geq$1.5B models for reliable calibration.\n\n\\subsection{Observational Case Studies}\n\\label{sec:observational}\n\n\\paragraph{RL-Trained Models.}\nWe apply \\contamcal{} to Qwen2.5-Instruct (0.5B--7B) and DeepSeek-R1-Distill (1.5B, 7B) without ground truth.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Observational calibration on RL-trained models (MMLU).}\n\\label{tab:observational}\n\\begin{tabular}{lcccr}\n\\toprule\n\\textbf{Model} & \\textbf{Raw} & \\textbf{Calib.} & \\textbf{95\\% CI} & $\\Delta$\\textbf{Rank} \\\\\n\\midrule\nQwen-0.5B-Inst & 47.2\\% & 46.8\\% & [43.1, 50.5] & 0 \\\\\nQwen-1.5B-Inst & 61.5\\% & 60.2\\% & [56.8, 63.6] & 0 \\\\\nQwen-3B-Inst   & 68.3\\% & 67.1\\% & [63.5, 70.7] & 0 \\\\\nQwen-7B-Inst   & 74.8\\% & 73.2\\% & [70.1, 76.3] & $-$1 \\\\\nDS-R1-1.5B     & 58.9\\% & 58.4\\% & [53.8, 63.0] & +1 \\\\\nDS-R1-7B       & 75.2\\% & 74.6\\% & [71.0, 78.2] & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCalibration adjustments are small (0.4--1.6\\pp{}) but CIs are notably wider (6.8\\pp{} average for Instruct, 8.2\\pp{} for DeepSeek) than in the controlled setting (4.2\\pp{})---reflecting honest uncertainty when signals degrade under RL post-training.\nGSM8K contamination persists after instruction tuning ($\\gamma = 0.42$, CI [0.18, 0.68]), suggesting RLHF does not fully eliminate memorization.\nRanking changes are minimal (1 out of 6), but the CI widths provide valuable uncertainty awareness even when rankings are preserved.\n\n\\paragraph{Specificity Check.}\nOn a known-clean benchmark, \\contamcal{} estimates $\\gamma = 0.02$ with CI including zero, confirming the method does not hallucinate contamination where none exists.\n\n\\paragraph{Frontier Scale: Qwen2.5-72B.}\nWe apply inference-only \\contamcal{} to Qwen2.5-72B.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Qwen2.5-72B observational results. Signal quality reaches its highest level; GSM8K $\\gamma$ is significantly nonzero.}\n\\label{tab:72b}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Bench.} & \\textbf{Raw} & \\textbf{Calib.} & \\textbf{95\\% CI} & $\\gamma_k$ \\\\\n\\midrule\nMMLU  & 85.4\\% & 84.2\\% & [81.5, 86.9] & 0.12 [$-$0.02, 0.28] \\\\\nGSM8K & 90.8\\% & 89.3\\% & [86.2, 92.4] & 0.18 [0.01, 0.37] \\\\\nARC-C & 94.3\\% & 93.8\\% & [91.4, 96.2] & 0.09 [$-$0.04, 0.23] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSignal quality reaches its highest levels (S2 AUC: 0.89; S4 AUC: 0.84), further supporting the scale-dependent trend.\nGSM8K's $\\gamma$ is significantly nonzero (CI [0.01, 0.37]), indicating detectable contamination even at frontier scale.\nMMLU and ARC-C $\\gamma$ CIs include zero, consistent with either low contamination or the model's genuine knowledge overshadowing memorization effects.\nCI widths average 5.5\\pp{}, reasonable for a single-model observational analysis.\n\n%======================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%======================================================================\n\n\\paragraph{Why Per-Benchmark $\\gamma_k$?}\nGSM8K ($\\gamma = 0.85$) is ${\\sim}4\\times$ more susceptible than MMLU ($\\gamma = 0.22$) or ARC-C ($\\gamma = 0.18$).\nFree-form math benchmarks are highly vulnerable because answer memorization directly accelerates generation; multiple-choice benchmarks are partially protected by forced-choice format.\nThis cross-family-consistent pattern (Qwen--Llama Pearson $r = 0.91$) suggests contamination susceptibility is an intrinsic benchmark property.\n\n\\paragraph{Honest Uncertainty Quantification.}\nA distinctive feature of \\contamcal{} is that calibration quality degrades gracefully: models with poor signals get wider CIs (0.5B: 2.3\\pp{} MAE, wider CI), while those with strong signals get tighter CIs (7B: 1.4\\pp{} MAE, tighter CI).\nThis is a feature, not a bug---the measurement error model ensures that uncertainty reflects genuine epistemic limitations.\n\n\\paragraph{Practical Deployment.}\nFull 4-signal mode requires open-weight models with logit access.\nFor closed-weight models ($\\geq$1.5B), the 2-signal mode (S3 + S4 only) achieves 2.1--2.8\\pp{} MAE, matching or exceeding existing methods while additionally providing credible intervals.\nEach per-benchmark MCMC fit requires $\\sim$45 minutes on a single GPU.\n\n%======================================================================\n\\section{Limitations}\n\\label{sec:limitations}\n%======================================================================\n\n\\begin{enumerate}\n\\item \\textbf{Model family breadth.} Controlled experiments use primarily Qwen2.5, with Llama-3.2-1B as cross-family validation. Broader family coverage (Pythia, Mistral, GPT-family) remains future work.\n\\item \\textbf{Unidimensional $\\theta$.} We use a single ability parameter per model-benchmark, which is a simplification for multifaceted benchmarks like MMLU \\citep{reckase2009multidimensional}. Multidimensional IRT is a natural extension.\n\\item \\textbf{SFT $\\neq$ real contamination.} LoRA SFT injection is a controlled proxy for real-world contamination (which may occur during pre-training, RLHF, or data mixture). Observational studies provide external validity but lack ground truth.\n\\item \\textbf{Local independence.} With a single model producing all item responses, strict local independence is violated. Our per-benchmark fitting and residual correlation analysis mitigate but do not eliminate this concern.\n\\item \\textbf{Closed-weight degradation.} The 2-signal mode fails at 0.5B and provides degraded but usable calibration at 1.5B+.\n\\item \\textbf{Computational cost.} Per-benchmark MCMC requires $\\sim$45 minutes; signal computation adds overhead for each model evaluated.\n\\end{enumerate}\n\n%======================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%======================================================================\n\nWe introduced \\contamcal{}, a framework that bridges contamination detection and score calibration via contamination-augmented 4PL IRT.\nOn controlled experiments across 0.5B--7B models and two model families, \\contamcal{} recovers true benchmark performance within 1.8\\pp{} MAE with 94\\% credible interval coverage, while providing honest uncertainty quantification that widens intervals when signals are unreliable.\nOur systematic signal characterization reveals scale-dependent effectiveness with a practical threshold at 1.5B, and identifies Min-K++ directional reversal as a cautionary finding for the detection community.\nFisher Information analysis provides theoretical grounding for identifiability bounds.\nObservational studies on RL-trained models up to 72B demonstrate directional external validity.\n\n\\contamcal{} is a statistical safety net for benchmark evaluation: it does not eliminate contamination, but it measures its effect and subtracts it out with proper uncertainty.\nFuture work includes extending to multidimensional IRT, broader model families, and integration with dynamic benchmark curation.\nData attribution methods \\citep{pruthi2020estimating,park2023trak} offer promising additional contamination signals for future integration.\n\n%======================================================================\n% References\n%======================================================================\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{50}\n\n\\bibitem[Adams et al.(1997)]{adams1997multidimensional}\nR.~Adams, M.~Wilson, and W.~Wang. 1997.\n\\newblock The multidimensional random coefficients multinomial logit model.\n\\newblock \\emph{Applied Psychological Measurement}, 21(1):1--23.\n\n\\bibitem[Angelopoulos and Bates(2023)]{angelopoulos2023conformal}\nA.~Angelopoulos and S.~Bates. 2023.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock \\emph{Foundations and Trends in Machine Learning}, 16(4):494--591.\n\n\\bibitem[Balloccu et al.(2024)]{balloccu2024leak}\nS.~Balloccu, P.~Schmidli, A.~Mott, and D.~Reiter. 2024.\n\\newblock Leak, cheat, repeat: Data contamination and evaluation malpractices in closed-source LLMs.\n\\newblock In \\emph{Proc. EACL}.\n\n\\bibitem[Cormack et al.(2009)]{cormack2009reciprocal}\nG.~V. Cormack, C.~L.~A. Clarke, and S.~B\\\"uttcher. 2009.\n\\newblock Reciprocal rank fusion outperforms condorcet and individual rank learning methods.\n\\newblock In \\emph{Proc. SIGIR}.\n\n\\bibitem[De Boeck and Wilson(2004)]{deboeck2004explanatory}\nP.~De~Boeck and M.~Wilson. 2004.\n\\newblock \\emph{Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach}.\n\\newblock Springer.\n\n\\bibitem[Dekoninck et al.(2024)]{dekoninck2024constat}\nJ.~Dekoninck, M.~Müller, M.~Fischer, and M.~Vechev. 2024.\n\\newblock ConStat: Performance-based contamination detection in large language models.\n\\newblock In \\emph{Proc. NeurIPS}.\n\n\\bibitem[Dekoninck et al.(2024b)]{dekoninck2024evading}\nJ.~Dekoninck, M.~Müller, M.~Fischer, and M.~Vechev. 2024.\n\\newblock Evading data contamination detection for language models is (too) easy.\n\\newblock \\emph{arXiv preprint arXiv:2402.02823}.\n\n\\bibitem[Dong et al.(2024)]{dong2024generalization}\nG.~Dong et al. 2024.\n\\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.\n\\newblock In \\emph{Proc. EMNLP}.\n\n\\bibitem[Eckerly(2017)]{eckerly2017detecting}\nC.~Eckerly. 2017.\n\\newblock Detecting item compromise in large-scale testing using IRT-based approaches.\n\\newblock \\emph{Journal of Educational Measurement}, 54(4):467--483.\n\n\\bibitem[Guo et al.(2017)]{guo2017calibration}\nC.~Guo, G.~Pleiss, Y.~Sun, and K.~Q. Weinberger. 2017.\n\\newblock On calibration of modern neural networks.\n\\newblock In \\emph{Proc. ICML}.\n\n\\bibitem[Holland and Wainer(1993)]{holland1993differential}\nP.~W. Holland and H.~Wainer, editors. 1993.\n\\newblock \\emph{Differential Item Functioning}.\n\\newblock Lawrence Erlbaum Associates.\n\n\\bibitem[Lalor et al.(2024)]{lalor2024benchmarking}\nJ.~P. Lalor, H.~Yang, Y.~Zhao, and D.~Rodriguez Cardenas. 2024.\n\\newblock Benchmarking large language models on psychometric testing.\n\\newblock In \\emph{Proc. AAAI}.\n\n\\bibitem[Li et al.(2024a)]{li2024task}\nY.~Li et al. 2024.\n\\newblock Task contamination: Language models may not be few-shot anymore.\n\\newblock In \\emph{Proc. AAAI}.\n\n\\bibitem[Li et al.(2024b)]{li2024cdd}\nY.~Li et al. 2024.\n\\newblock CDD: A contamination detection dataset for large language models.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Maris and Bechger(2009)]{maris2009equivalence}\nG.~Maris and T.~M. Bechger. 2009.\n\\newblock On interpreting the model parameters for the three-parameter logistic model.\n\\newblock \\emph{Measurement}, 7(2):75--88.\n\n\\bibitem[Mislevy(1986)]{mislevy1986bayes}\nR.~J. Mislevy. 1986.\n\\newblock Bayes modal estimation in item response models.\n\\newblock \\emph{Psychometrika}, 51(2):177--195.\n\n\\bibitem[Park et al.(2023)]{park2023trak}\nS.~M. Park, K.~Georgiev, A.~Ilyas, G.~Leconte, and A.~Madry. 2023.\n\\newblock TRAK: Attributing model behavior at scale.\n\\newblock In \\emph{Proc. ICML}.\n\n\\bibitem[Platt(1999)]{platt1999probabilistic}\nJ.~Platt. 1999.\n\\newblock Probabilistic outputs for support vector machines and comparisons to regularized likelihood methods.\n\\newblock \\emph{Advances in Large Margin Classifiers}, 10(3):61--74.\n\n\\bibitem[Polo et al.(2024)]{polo2024tinybenchmarks}\nF.~M. Polo et al. 2024.\n\\newblock tinyBenchmarks: Evaluating LLMs with fewer examples.\n\\newblock In \\emph{Proc. ICML}.\n\n\\bibitem[Pruthi et al.(2020)]{pruthi2020estimating}\nG.~Pruthi, F.~Liu, M.~Kale, and S.~Sundararajan. 2020.\n\\newblock Estimating training data influence by tracing gradient descent.\n\\newblock In \\emph{Proc. NeurIPS}.\n\n\\bibitem[Reckase(2009)]{reckase2009multidimensional}\nM.~D. Reckase. 2009.\n\\newblock \\emph{Multidimensional Item Response Theory}.\n\\newblock Springer.\n\n\\bibitem[Rosenbaum and Rubin(1983)]{rosenbaum1983central}\nP.~R. Rosenbaum and D.~B. Rubin. 1983.\n\\newblock The central role of the propensity score in observational studies for causal effects.\n\\newblock \\emph{Biometrika}, 70(1):41--55.\n\n\\bibitem[Sainz et al.(2023)]{sainz2023contamination}\nO.~Sainz et al. 2023.\n\\newblock NLP evaluation in trouble: On the need to measure LLM data contamination for each benchmark.\n\\newblock In \\emph{Findings of EMNLP}.\n\n\\bibitem[San~Mart\\'in et al.(2009)]{sanmartin2009}\nE.~San~Mart\\'in, J.-M. Rolin, and L.~M. Castro. 2009.\n\\newblock Identification of parametric Rasch-type models.\n\\newblock \\emph{Journal of Statistical Planning and Inference}, 139(7):2421--2433.\n\n\\bibitem[Shi et al.(2024)]{shi2024detecting}\nW.~Shi, A.~Ajith, M.~Xia, Y.~Huang, D.~Liu, T.~Blevins, D.~Chen, and L.~Zettlemoyer. 2024.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{Proc. ICLR}.\n\n\\bibitem[Sinharay(2017)]{sinharay2017use}\nS.~Sinharay. 2017.\n\\newblock Detection of item preknowledge using likelihood-ratio test and score test.\n\\newblock \\emph{Journal of Educational and Behavioral Statistics}, 42(1):46--68.\n\n\\bibitem[Talts et al.(2018)]{talts2018sbc}\nS.~Talts, M.~Betancourt, D.~Simpson, A.~Vehtari, and A.~Gelman. 2018.\n\\newblock Validating Bayesian inference algorithms with simulation-based calibration.\n\\newblock \\emph{arXiv preprint arXiv:1804.06788}.\n\n\\bibitem[Thissen et al.(1993)]{thissen1993detection}\nD.~Thissen, L.~Steinberg, and H.~Wainer. 1993.\n\\newblock Detection of differential item functioning using the parameters of item response models.\n\\newblock In \\emph{Differential Item Functioning}, pages 67--113.\n\n\\bibitem[White et al.(2024)]{white2024livebench}\nC.~White, S.~Dooley, M.~Roberts, A.~Pal, B.~Feuer, S.~Jain, R.~Shwartz-Ziv, N.~Jain, K.~Saifullah, S.~Naber, and T.~Goldstein. 2024.\n\\newblock LiveBench: A challenging, contamination-free LLM benchmark.\n\\newblock \\emph{arXiv preprint arXiv:2406.19314}.\n\n\\bibitem[Xu et al.(2024)]{xu2024benchmark}\nR.~Xu, Z.~Wang, R.~Fan, and P.~Liu. 2024.\n\\newblock Benchmark data contamination of large language models: A survey.\n\\newblock \\emph{arXiv preprint arXiv:2406.04244}.\n\n\\bibitem[Yang et al.(2023)]{yang2023rethinking}\nS.~Yang et al. 2023.\n\\newblock Rethinking benchmark and contamination for language models with rephrased samples.\n\\newblock \\emph{arXiv preprint arXiv:2311.04850}.\n\n\\bibitem[Zhang et al.(2024)]{zhang2024kds}\nY.~Zhang et al. 2024.\n\\newblock KDS: A benchmark for evaluating knowledge in large language models.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Zhuang et al.(2024)]{zhuang2024hibayes}\nY.~Zhuang et al. 2024.\n\\newblock HiBayES: A hierarchical Bayesian approach for LLM evaluation.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Zumbo(1999)]{zumbo1999handbook}\nB.~D. Zumbo. 1999.\n\\newblock \\emph{A Handbook on the Theory and Methods of Differential Item Functioning (DIF)}.\n\\newblock National Defense Headquarters, Ottawa.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff797d39-36a4-48a4-848e-9d0a050c6980",
  "isSidechain": false,
  "requestId": "req_011Cb2uJR1tqdbMifUDZpcQw",
  "type": "assistant",
  "uuid": "f6791ddd-7081-44e9-9f2f-7b6ccec67fcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3Q8LMZAtaUCHrgpYfXYqt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 478,
      "cache_read_input_tokens": 49044,
      "output_tokens": 17332,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 478,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17332,
          "cache_read_input_tokens": 49044,
          "cache_creation_input_tokens": 478,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 478
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

_source line 19 · 2026-05-14T18:08:57.508Z_

<details><summary>↩ Tool result · `toolu_01RF9jxbbfDgnNCABHHYPDEA`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6791ddd-7081-44e9-9f2f-7b6ccec67fcc",
  "isSidechain": false,
  "promptId": "14a905e9-cf62-4ad0-acbf-909375bdc04c",
  "type": "user",
  "uuid": "78898540-b4c0-4538-8886-5014c914d5f2",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{bm}\n\\usepackage{microtype}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{array}\n\n\\newcommand{\\contamcal}{\\textsc{ContamCal}}\n\\newcommand{\\pp}{\\,\\text{pp}}\n\n\\title{\\contamcal{}: Calibrating Benchmark Scores for Training Data Contamination\\\\via Contamination-Augmented Item Response Theory}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n%======================================================================\n\\begin{abstract}\n%======================================================================\nTraining data contamination inflates LLM benchmark scores, yet existing detection methods flag contamination without answering: \\emph{what would this model score if it had never seen the test data?}\nWe introduce \\contamcal{}, a two-stage framework that bridges contamination detection and score calibration.\nStage~1 computes item-level contamination exposure via four complementary detection signals---embedding similarity, Min-K++, ConStat, and LLM self-critique---aggregated through Reciprocal Rank Fusion (RRF).\nStage~2 fits a contamination-augmented 4PL Item Response Theory model with per-benchmark contamination susceptibility parameters~$\\gamma_k$ and a measurement error model that propagates signal uncertainty into Bayesian posteriors.\nOn controlled contamination injection experiments across Qwen2.5 (0.5B--7B) and Llama-3.2-1B with three benchmarks (MMLU, GSM8K, ARC-Challenge), \\contamcal{} recovers true benchmark performance within 1.8\\pp{} MAE (bootstrap 95\\% CI: [1.2, 2.4]) with 94\\% credible interval coverage, while naive scores overestimate by up to 58\\pp{} under full contamination (3B GSM8K).\nWe systematically characterize signal effectiveness as method-specific and scale-dependent: embedding similarity is robust across scales (AUC$>$0.95), whereas Min-K++ and self-critique fail at 0.5B (AUC$\\approx$0.47) but recover at 1.5B+ (AUC$>$0.70).\nFisher Information analysis establishes AUC$\\geq$0.55 as the structural identifiability boundary and AUC$\\geq$0.70 as the practical boundary for reliable calibration.\n\\end{abstract}\n\n%======================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%======================================================================\n\nBenchmark contamination---where test data leaks into training corpora---is among the most serious threats to the validity of LLM evaluation \\citep{sainz2023contamination,balloccu2024leak,li2024task}.\nEven rephrased test items can inflate accuracy by 8--15 points while evading $n$-gram decontamination \\citep{yang2023rethinking,dekoninck2024evading}.\n\\citet{xu2024benchmark} systematically tested 20 mitigation strategies and found none reliably eliminates contamination effects.\n\nThis motivates a fundamental reframing: rather than trying to eliminate contamination from benchmarks (which does not work), we propose to \\emph{statistically control for it}---measuring its effect and subtracting it out with proper uncertainty quantification.\nThis mirrors the shift in causal inference from eliminating confounders to statistically adjusting for them \\citep{rosenbaum1983central}.\n\nExisting approaches address only part of the problem.\nDetection methods---Min-K\\%++ \\citep{shi2024detecting}, ConStat \\citep{dekoninck2024constat}, and LLM self-critique \\citep{yang2023rethinking}---flag contamination but do not calibrate scores.\nIRT-based evaluation \\citep{lalor2024benchmarking,polo2024tinybenchmarks} models item difficulty psychometrically but ignores contamination.\nDCR \\citep{dong2024generalization} provides adjusted accuracy but lacks uncertainty bounds.\nHiBayES \\citep{zhuang2024hibayes} provides Bayesian model evaluation but does not account for contamination.\n\nWe introduce \\contamcal{}, which bridges detection and calibration through a two-stage pipeline grounded in the educational measurement tradition of item compromise IRT \\citep{eckerly2017detecting,sinharay2017use} and explanatory IRT \\citep{deboeck2004explanatory}.\nOur framework makes three non-trivial adaptations for LLM evaluation: (a)~independent examinees become a single model with joint item distributions, altering local independence semantics; (b)~binary leakage becomes continuous exposure scores requiring measurement error propagation; and (c)~stable ability becomes regime-conditional ability requiring scale-aware signal selection.\n\nOur contributions are:\n\\begin{enumerate}\n\\item The \\contamcal{} framework: a two-stage pipeline (RRF provenance mapping $\\to$ contamination-augmented 4PL IRT with per-benchmark $\\gamma_k$ and measurement error model) producing calibrated scores with credible intervals (\\S\\ref{sec:method}).\n\\item Systematic signal effectiveness characterization: a signal $\\times$ scale $\\times$ dosage AUC mapping revealing method-specific, scale-dependent reliability, including a cautionary finding on Min-K++ directional reversal (\\S\\ref{sec:signal_analysis}).\n\\item Dual-track validation: controlled SFT injection across 0.5B--7B within Qwen2.5 plus Llama-3.2-1B (internal validity), and ecological observational studies on Instruct and DeepSeek-R1 models up to 72B (external validity) (\\S\\ref{sec:experiments}).\n\\end{enumerate}\n\n%======================================================================\n\\section{Related Work}\n\\label{sec:related}\n%======================================================================\n\n\\paragraph{Contamination Detection.}\nSeveral methods detect training data memorization in LLMs.\nMin-K\\%++ \\citep{shi2024detecting} uses token-level probability outliers; ConStat \\citep{dekoninck2024constat} exploits performance gaps between original and paraphrased items; KDS \\citep{zhang2024kds} and CDD \\citep{li2024cdd} provide detection datasets.\n\\citet{yang2023rethinking} propose LLM self-critique for contamination detection.\nThese methods flag items but do not produce calibrated scores.\n\n\\paragraph{IRT for LLM Evaluation.}\nItem Response Theory has been applied to LLM evaluation \\citep{lalor2024benchmarking,polo2024tinybenchmarks}, dynamic benchmarks \\citep{white2024livebench}, and Bayesian model comparison \\citep{zhuang2024hibayes}.\nNone model contamination as a covariate.\nOur approach builds on explanatory IRT \\citep{deboeck2004explanatory,adams1997multidimensional} and the item compromise literature \\citep{eckerly2017detecting,sinharay2017use}.\n\n\\paragraph{Contamination Mitigation.}\nDCR \\citep{dong2024generalization} uses fuzzy inference for adjusted accuracy.\n\\citet{xu2024benchmark} demonstrate that rephrasing, option shuffling, and other mitigation strategies all fail.\nDynamic benchmarks like LiveBench \\citep{white2024livebench} sidestep the problem through continuous curation.\nOur approach is complementary: \\contamcal{} provides a statistical safety net for existing static benchmarks.\n\n\\paragraph{Calibration and Uncertainty.}\nWe distinguish our use of ``calibration'' from probability calibration \\citep{guo2017calibration,platt1999probabilistic}: we calibrate \\emph{aggregate benchmark scores} for contamination bias, not per-item prediction confidences.\nFor uncertainty quantification, conformal prediction \\citep{angelopoulos2023conformal} offers distribution-free coverage guarantees; we prefer Bayesian IRT because it naturally incorporates item-level contamination covariates and produces interpretable $\\gamma_k$ parameters.\n\n\\paragraph{Differential Item Functioning.}\nOur per-benchmark $\\gamma_k$ is conceptually related to DIF \\citep{holland1993differential,thissen1993detection,zumbo1999handbook}, where item parameters differ between exposure groups.\nHowever, DIF traditionally compares demographic subgroups of examinees; we compare contamination exposure levels of items evaluated by a single model.\n\n%======================================================================\n\\section{Method}\n\\label{sec:method}\n%======================================================================\n\n\\contamcal{} operates in two stages: (1)~item-level contamination exposure estimation via multi-signal fusion, and (2)~contamination-augmented IRT calibration.\n\n\\subsection{Stage 1: Multi-Signal Exposure Estimation}\n\\label{sec:stage1}\n\nFor each benchmark item $i$ evaluated by model $j$, we compute four detection signals:\n\n\\paragraph{S1: Embedding Similarity.}\nCosine similarity between the item embedding and its nearest neighbor in the known training corpus.\nThis training-data-independent signal is robust across model scales.\n\n\\paragraph{S2: Min-K++.}\nToken-level probability outlier detection \\citep{shi2024detecting}, computed from model $j$'s own output probabilities.\nRequires logit access (open-weight models).\n\n\\paragraph{S3: ConStat.}\nPerformance gap between the original item and semantically equivalent paraphrases \\citep{dekoninck2024constat}.\nRelies on generating multiple paraphrases per item.\n\n\\paragraph{S4: LLM Self-Critique.}\nThe model generates an explanation of its own familiarity with the item; contaminated items exhibit characteristic low-entropy self-assessment patterns.\n\n\\paragraph{Reciprocal Rank Fusion.}\nWe aggregate the four signals using RRF \\citep{cormack2009reciprocal}:\n\\begin{equation}\n\\text{RRF}(i) = \\sum_{s=1}^{4} \\frac{1}{k + r_s(i)}\n\\end{equation}\nwhere $r_s(i)$ is the rank of item $i$ under signal $s$ and $k=60$ is the standard damping constant.\nRRF is a training-free aggregation---a principled design choice avoiding meta-circularity (a learned aggregator's training data may itself be contaminated).\nThe RRF score is normalized to $[0,1]$ to yield the continuous exposure estimate $\\hat{\\tau}_i$.\n\n\\subsection{Stage 2: Contamination-Augmented 4PL IRT}\n\\label{sec:stage2}\n\n\\paragraph{Base Model.}\nWe extend the 4-parameter logistic IRT model.\nFor model $j$ responding to item $i$ on benchmark $k$:\n\\begin{equation}\nP(Y_{ij}=1 \\mid \\theta_j, \\bm{\\xi}_i, \\tau_i) = c_i + \\frac{d_i - c_i}{1 + \\exp\\!\\bigl(-a_i(\\theta_j + \\gamma_k \\tau_i - b_i)\\bigr)}\n\\label{eq:4pl}\n\\end{equation}\nwhere $\\theta_j$ is model ability, $a_i$ is item discrimination, $b_i$ is difficulty, $c_i$ is guessing, $d_i$ is the upper asymptote, $\\tau_i \\in [0,1]$ is the latent contamination exposure, and $\\gamma_k$ is the per-benchmark contamination susceptibility.\n\nThe calibrated score for model $j$ on benchmark $k$ is:\n\\begin{equation}\n\\hat{s}_{jk}^{\\text{calib}} = \\frac{1}{n_k} \\sum_{i \\in k} P(Y_{ij}=1 \\mid \\theta_j, \\bm{\\xi}_i, \\tau_i=0)\n\\end{equation}\ni.e., the expected accuracy under zero contamination exposure.\n\n\\paragraph{Measurement Error Model.}\nStage~1 produces noisy exposure estimates $\\hat{\\tau}_i$.\nWe model:\n\\begin{equation}\n\\hat{\\tau}_i = \\tau_i + \\epsilon_i, \\quad \\epsilon_i \\sim \\mathcal{N}(0, \\sigma_e^2)\n\\end{equation}\nwhere $\\sigma_e$ is estimated from the signal pipeline's false positive/negative rates.\nThis measurement error model propagates signal uncertainty into the IRT posterior, producing wider credible intervals when signals are noisy.\n\n\\paragraph{Per-Benchmark $\\gamma_k$.}\nRather than estimating a single global $\\gamma$, we fit per-benchmark $\\gamma_k$ to capture contamination susceptibility heterogeneity.\nThis is motivated by the observation that different benchmark formats (multiple-choice vs.\\ free-form) and content types (factual recall vs.\\ reasoning) exhibit markedly different vulnerability to memorization.\n\n\\paragraph{Fisher Information and Identifiability.}\nThe Fisher Information for $\\gamma_k$ in the 4PL+$\\gamma$ model is:\n\\begin{equation}\nI(\\gamma_k) = \\sum_{i \\in k} \\sum_j \\tau_i^2 \\cdot a_i^2 \\cdot P_{ij}(1-P_{ij}) \\cdot \\left(\\frac{d_i - c_i}{P_{ij} - c_i}\\right)^2 \\frac{1}{(d_i - c_i)^2}\n\\end{equation}\nWhen signal AUC is low ($\\hat{\\tau}$ is nearly uninformative), $\\tau_i$ estimates cluster near 0.5 with low variance, and $I(\\gamma_k) \\to 0$---$\\gamma_k$ becomes structurally unidentifiable.\nOur simulation study (\\S\\ref{sec:identifiability}) establishes AUC$\\geq$0.55 as the structural identifiability boundary ($I(\\gamma_k) > 0$) and AUC$\\geq$0.70 as the practical boundary (CI$_{95}$ width $<$ 10\\pp{} at $N\\geq 50$ models).\n\n\\paragraph{Local Independence.}\nStandard IRT assumes independent examinees.\nIn LLM evaluation, a single model produces all item responses, introducing correlations through shared parameters.\nWe mitigate this by fitting IRT per-benchmark (reducing correlation scope) and empirically verifying via posterior predictive checks on item-level residual correlations (mean $r = 0.032$, max $r = 0.085$; \\S\\ref{sec:main_results}).\n\n\\paragraph{Inference.}\nAll models are fit via Hamiltonian Monte Carlo (4 chains, 2000 warmup + 2000 sampling iterations).\nWe verify convergence with $\\hat{R} < 1.01$ and report zero divergences across all fits.\n\n%======================================================================\n\\section{Signal Effectiveness Analysis}\n\\label{sec:signal_analysis}\n%======================================================================\n\nBefore calibration, we systematically characterize signal reliability across model scales, contamination dosages, and benchmarks.\n\n\\subsection{Signal $\\times$ Scale AUC Mapping}\n\nTable~\\ref{tab:signal_scale_auc} reports item-level detection AUC at 5\\% contamination dosage (d005) across three model scales.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Signal detection AUC at d005 across model scales and benchmarks. S1 (Embedding) is robust across scales; S2 (Min-K++), S3 (ConStat), and S4 (Self-Critique) fail at 0.5B but recover at 1.5B+.}\n\\label{tab:signal_scale_auc}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Signal} & \\textbf{Benchmark} & \\textbf{0.5B} & \\textbf{1.5B} & \\textbf{3B} \\\\\n\\midrule\n\\multirow{3}{*}{S1 Embedding}\n & MMLU   & 0.953 & 0.961 & 0.948 \\\\\n & GSM8K  & 0.988 & 0.985 & 0.982 \\\\\n & ARC-C  & 0.995 & 0.990 & 0.991 \\\\\n\\midrule\n\\multirow{3}{*}{S2 Min-K++}\n & MMLU   & 0.466 & 0.718 & 0.798 \\\\\n & GSM8K  & 0.465 & 0.762 & 0.842 \\\\\n & ARC-C  & 0.466 & 0.741 & 0.816 \\\\\n\\midrule\n\\multirow{3}{*}{S3 ConStat}\n & MMLU   & $\\sim$0.55 & 0.795 & 0.836 \\\\\n & GSM8K  & $\\sim$0.53 & 0.832 & 0.873 \\\\\n & ARC-C  & $\\sim$0.52 & 0.814 & 0.855 \\\\\n\\midrule\n\\multirow{3}{*}{S4 Self-Critique}\n & MMLU   & 0.517 & 0.692 & 0.751 \\\\\n & GSM8K  & 0.495 & 0.731 & 0.792 \\\\\n & ARC-C  & 0.433 & 0.712 & 0.775 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nS1 (Embedding Similarity) is robust across all scales (AUC $>$ 0.95) because it relies on training-data-independent semantic similarity.\nS2 (Min-K++) and S4 (Self-Critique) are near-random at 0.5B (AUC $\\approx$ 0.47) but cross the practical threshold of 0.70 at 1.5B.\nThis scale-dependent behavior reflects underlying capacity requirements: Min-K++ depends on token-level memorization capacity (LoRA adapter sizes grow from 34MB at 0.5B to 115MB at 3B), while Self-Critique requires sufficient generation quality for metacognitive self-assessment.\n\n\\subsection{Signal Survival Across Scales}\n\nTable~\\ref{tab:signal_survival} summarizes the effective number of signals at each scale.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal effectiveness summary across scales. Effective signals (AUC $\\geq$ 0.70) increase from 1 at 0.5B to 4 at 3B.}\n\\label{tab:signal_survival}\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Signal} & \\textbf{0.5B} & \\textbf{1.5B} & \\textbf{3B} & \\textbf{Status} \\\\\n\\midrule\nS1 Embed. & 0.979 & 0.979 & 0.974 & Robust \\\\\nS2 Min-K++ & 0.465 & 0.740 & 0.819 & Recovers 1.5B+ \\\\\nS3 ConStat & $\\sim$0.53 & 0.814 & 0.855 & Recovers 1.5B+ \\\\\nS4 Self-Crit. & 0.481 & 0.712 & 0.773 & Recovers 1.5B+ \\\\\n\\midrule\n\\# Effective & 1 & 3 & 4 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 0.5B, only S1 is effective; RRF degrades to a dominant-signal mode (S1 weight share: 89\\%).\nAt 1.5B, three signals cross the 0.70 threshold, enabling genuine multi-signal fusion (S1 weight share drops to 38\\%).\nAt 3B, all four signals are effective (S1 weight share: 31\\%).\n\n\\subsection{Min-K++ Directional Reversal}\n\\label{sec:reversal}\n\nA critical cautionary finding: at high contamination dosage (d100), Min-K++ exhibits \\emph{directional reversal}---contaminated items receive \\emph{lower} scores than clean items, actively misleading rather than merely failing.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Min-K++ directional reversal at d100 (Cohen's $d$; negative = reversed direction). The reversal persists across scales but attenuates with increasing model size.}\n\\label{tab:reversal}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Benchmark} & \\textbf{0.5B} & \\textbf{1.5B} & \\textbf{3B} \\\\\n\\midrule\nMMLU  & $-$1.22 & $-$1.08 & $-$0.85 \\\\\nGSM8K & $-$2.67 & $-$1.78 & $-$1.31 \\\\\nARC-C & $-$2.05 & $-$1.71 & $-$1.26 \\\\\n\\midrule\nMean  & $-$1.98 & $-$1.52 & $-$1.14 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe reversal attenuates with scale ($-$1.98 at 0.5B $\\to$ $-$1.14 at 3B) as larger models' perplexity distributions become more stable, but persists at all tested scales.\nThis strengthens the case for robust aggregation: Min-K++ should be used with extreme caution under high contamination dosage at any scale.\n\n\\subsection{RRF Aggregation Ablation}\n\\label{sec:rrf}\n\nTable~\\ref{tab:rrf} compares RRF against single-signal baselines and alternative aggregation strategies.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Detection AUC (d005, benchmark-averaged): RRF vs.\\ single-signal and alternative aggregation methods.}\n\\label{tab:rrf}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{0.5B} & \\textbf{1.5B} & \\textbf{3B} \\\\\n\\midrule\nRRF 4-signal     & 0.962 & 0.924 & 0.943 \\\\\nS1 only          & 0.979 & 0.972 & 0.964 \\\\\nS2 only          & 0.465 & 0.740 & 0.819 \\\\\nS3 only          & 0.533 & 0.814 & 0.855 \\\\\nS4 only          & 0.481 & 0.712 & 0.773 \\\\\nRRF 2-sig (closed) & 0.508 & 0.782 & 0.831 \\\\\nEqual-wt rank avg & --- & 0.908 & --- \\\\\nCalibrated wt RRF & --- & 0.931 & --- \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{FP robustness (4-signal RRF):}} \\\\\n5\\% FP injection  & \\multicolumn{3}{c}{AUC drop: 0.008} \\\\\n10\\% FP injection & \\multicolumn{3}{c}{AUC drop: 0.014} \\\\\n15\\% FP injection & \\multicolumn{3}{c}{AUC drop: 0.023} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 0.5B, RRF (0.962) is slightly below S1-only (0.979) because near-random S2/S4 signals dilute the fusion.\nThis is an honest characterization of the degraded regime: RRF gracefully degrades rather than catastrophically failing.\nAt 1.5B+, RRF enables genuine multi-signal fusion with complementary information.\nCalibrated weighted RRF (0.931 at 1.5B) provides marginal improvement over standard RRF (0.924) but introduces a training dependency, supporting our design choice of training-free RRF.\nRRF is robust to false positive injection: 15\\% FP injection causes only a 2.3\\% AUC drop, owing to rank-based aggregation's natural outlier resistance.\n\n%======================================================================\n\\section{Experiments}\n\\label{sec:experiments}\n%======================================================================\n\n\\subsection{Experimental Setup}\n\n\\paragraph{Controlled Contamination Injection.}\nWe train Qwen2.5 models (0.5B, 1.5B, 3B) via LoRA SFT at five contamination dosages: d000 (0\\%), d005 (5\\%), d025 (25\\%), d050 (50\\%), d100 (100\\%) of benchmark items injected as paraphrased training data, with 3 random seeds each, totaling 45 model instances per benchmark.\nGround-truth clean accuracy is established from d000 models.\n\n\\paragraph{Benchmarks.}\nMMLU (14K items, multiple-choice), GSM8K ($\\sim$1.3K items, free-form math), and ARC-Challenge (science reasoning, multiple-choice).\n\n\\paragraph{Baselines.}\nWe compare against 7 methods: (B0)~Raw scores, (B1)~Remove-and-rescore, (B2)~Single-signal 2PL+$\\gamma$, (B3)~Vanilla 4PL (no contamination), (B4)~Linear regression + bootstrap CI, (B5)~Emperor mitigation strategies \\citep{xu2024benchmark}, and (B6)~DCR fuzzy inference \\citep{dong2024generalization}.\n\n\\paragraph{Metrics.}\n(1)~MAE between calibrated and true accuracy with bootstrap 95\\% CIs; (2)~credible interval coverage at 50\\%/80\\%/95\\%; (3)~average CI width; (4)~Kendall's $\\tau$ for ranking preservation; (5)~dose-response monotonicity.\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Main results: 8 methods on 5 evaluation metrics across Qwen2.5 (0.5B--3B) $\\times$ 3 benchmarks $\\times$ 5 dosages $\\times$ 3 seeds. \\contamcal{} achieves the lowest MAE and the only near-nominal coverage. ``---'' indicates the method does not produce credible intervals.}\n\\label{tab:main}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{MAE (pp)$\\downarrow$} & \\textbf{95\\% Cov.$\\uparrow$} & \\textbf{CI Width (pp)$\\downarrow$} & \\textbf{Kendall $\\tau$$\\uparrow$} & \\textbf{Mono.} \\\\\n\\midrule\n4PL+$\\gamma$ ME (ours) & \\textbf{1.8} [1.2, 2.4] & \\textbf{94\\%} & 4.2 & \\textbf{0.96} & 0.95 \\\\\nB0: Raw                & 8.2          & ---    & ---  & 0.87 & --- \\\\\nB1: Remove-rescore     & 4.6          & ---    & ---  & 0.91 & --- \\\\\nB2: 2PL+$\\gamma$ (S1)  & 2.9          & 81\\%   & 5.6  & 0.94 & 0.90 \\\\\nB3: Vanilla 4PL        & 6.5          & 58\\%   & 3.2  & 0.89 & --- \\\\\nB4: Linear + boot      & 3.2          & 76\\%   & 6.8  & 0.93 & 0.85 \\\\\nB5: Emperor mitig.     & 5.8          & ---    & ---  & 0.89 & --- \\\\\nB6: DCR fuzzy          & 3.9          & ---    & ---  & 0.92 & 0.80 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\contamcal{} achieves 1.8\\pp{} MAE with bootstrap 95\\% CI [1.2, 2.4], significantly outperforming the best baseline DCR (3.9\\pp{}).\nIt is the only method producing near-nominal 95\\% credible interval coverage (94\\%), compared to 58--81\\% for baselines that produce intervals.\nVanilla 4PL's 58\\% coverage demonstrates that IRT without contamination modeling produces dangerously narrow, miscalibrated intervals.\nOur 80\\% and 50\\% coverage rates (83\\% and 52\\%, respectively) further confirm well-calibrated uncertainty.\nKendall's $\\tau = 0.96$ indicates high-fidelity ranking preservation.\nMCMC diagnostics are clean: zero divergences, $\\hat{R}_{\\max} = 1.008$, minimum ESS $= 850$.\nResidual correlations are low (mean $r = 0.032$, max $r = 0.085$), indicating acceptable local independence.\n\n\\subsection{Per-Benchmark Analysis}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-benchmark MAE (pp) for \\contamcal{} vs.\\ key baselines.}\n\\label{tab:per_bench}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Bench.} & \\textbf{Ours} & \\textbf{B0 Raw} & \\textbf{B2 2PL} & \\textbf{B6 DCR} \\\\\n\\midrule\nMMLU  & 1.1 & 4.3  & 1.8 & 2.5 \\\\\nGSM8K & 2.8 & 14.6 & 4.2 & 6.2 \\\\\nARC-C & 1.2 & 4.8  & 2.0 & 2.8 \\\\\n\\midrule\nAvg.  & 1.8 & 8.2  & 2.9 & 3.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGSM8K shows the largest raw inflation (14.6\\pp{}) and the highest residual after calibration (2.8\\pp{}), reflecting the extreme sensitivity of free-form math benchmarks to memorization.\nMMLU (1.1\\pp{}) and ARC-C (1.2\\pp{}) are well calibrated across all dosages.\n\n\\paragraph{Per-Benchmark $\\gamma_k$ Estimates.}\nThe estimated contamination susceptibility parameters reveal striking heterogeneity:\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-benchmark $\\gamma_k$ estimates. GSM8K is ${\\sim}4\\times$ more susceptible to contamination than MMLU or ARC-C.}\n\\label{tab:gamma}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Benchmark} & $\\gamma_k$ & \\textbf{95\\% CI} \\\\\n\\midrule\nMMLU  & 0.22 & [0.08, 0.38] \\\\\nGSM8K & 0.85 & [0.62, 1.12] \\\\\nARC-C & 0.18 & [0.04, 0.34] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $\\gamma_k$ heterogeneity is statistically significant ($\\chi^2$ test, $p = 0.002$), confirming that per-benchmark fitting is essential.\nA joint model with a shared global $\\gamma = 0.41$ yields MAE of 2.6\\pp{}, worse than per-benchmark fitting (1.8\\pp{}): the global model overfits MMLU while underfitting GSM8K.\n\n\\paragraph{Per-Scale MAE.}\n\\contamcal{} achieves 2.3\\pp{} at 0.5B, 1.4\\pp{} at 1.5B, and 1.6\\pp{} at 3B.\nThe higher MAE at 0.5B reflects degraded signal quality (only S1 effective), leading to noisier exposure estimates.\nThe measurement error model compensates with wider CIs, providing honest uncertainty quantification even in this degraded regime.\n\n\\subsection{Dose-Response: 3B GSM8K}\n\\label{sec:dose_response}\n\nTable~\\ref{tab:dose_response} presents the most dramatic calibration case.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Dose-response for 3B GSM8K. Naive scores inflate by up to 57.7\\pp{}; \\contamcal{} recovers true performance within 4.2\\pp{}.}\n\\label{tab:dose_response}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Dose} & \\textbf{Obs.} & \\textbf{Calib.} & \\textbf{True} & \\textbf{Resid.} \\\\\n\\midrule\nd000 (0\\%)   & 12.0\\% & ---    & 12.0\\% & --- \\\\\nd005 (5\\%)   & 20.8\\% & 13.2\\% & 12.0\\% & +1.2\\pp{} \\\\\nd025 (25\\%)  & $\\sim$35.4\\% & 14.5\\% & 12.0\\% & +2.5\\pp{} \\\\\nd050 (50\\%)  & $\\sim$51.8\\% & 15.1\\% & 12.0\\% & +3.1\\pp{} \\\\\nd100 (100\\%) & 69.7\\% & 16.2\\% & 12.0\\% & +4.2\\pp{} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt full contamination (d100), the observed score of 69.7\\% is 57.7\\pp{} above the true score of 12.0\\%.\n\\contamcal{} reduces this to a 4.2\\pp{} residual.\nEven at moderate contamination (d025), naive scores overestimate by $\\sim$23\\pp{}, while our calibration achieves a 2.5\\pp{} residual.\n\n\\subsection{Identifiability and Simulation Study}\n\\label{sec:identifiability}\n\nWe conduct a 120-condition simulation sweep varying signal AUC ($\\in \\{0.55, 0.65, 0.70, 0.80, 0.90\\}$) and number of models ($N \\in \\{20, 50, 100\\}$) at $\\gamma_{\\text{true}} = 0.5$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$\\gamma$ recovery from the simulation sweep. AUC $\\geq 0.70$ at $N \\geq 50$ is the practical identifiability sweet spot (CI $<$ 7\\pp{}, coverage $\\geq$ 95\\%).}\n\\label{tab:identifiability}\n\\begin{tabular}{cccccc}\n\\toprule\n\\textbf{AUC} & $N$ & \\textbf{Bias} & \\textbf{RMSE} & \\textbf{CI$_{95}$ (pp)} & \\textbf{Cov.} \\\\\n\\midrule\n0.55 & 20  & +0.020 & 0.040 & 13.3 & 80\\% \\\\\n0.55 & 50  & +0.015 & 0.026 & 8.7  & 90\\% \\\\\n0.55 & 100 & $-$0.003 & 0.004 & 6.5 & 100\\% \\\\\n\\midrule\n0.65 & 20  & +0.016 & 0.035 & 11.8 & 85\\% \\\\\n0.65 & 50  & +0.010 & 0.020 & 7.6  & 93\\% \\\\\n0.65 & 100 & $-$0.004 & 0.008 & 5.8 & 97\\% \\\\\n\\midrule\n0.70 & 50  & +0.008 & 0.018 & 7.0  & 95\\% \\\\\n0.70 & 100 & $-$0.002 & 0.006 & 5.3 & 98\\% \\\\\n\\midrule\n0.80 & 50  & +0.006 & 0.014 & 6.2  & 96\\% \\\\\n0.80 & 100 & +0.003 & 0.005 & 4.8  & 98\\% \\\\\n\\midrule\n0.90 & 50  & +0.004 & 0.010 & 5.4  & 97\\% \\\\\n0.90 & 100 & +0.002 & 0.004 & 4.2  & 99\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFisher Information analysis yields AUC $\\geq 0.52$ as the structural identifiability boundary and AUC $\\geq 0.70$ as the practical boundary.\nThe latter corresponds precisely to the Min-K++ AUC at 1.5B ($\\sim$0.74), confirming that 1.5B is the minimum scale for reliable multi-signal calibration.\nCI width scales as approximately $1/\\sqrt{N}$ (empirical ratio $N_{20}/N_{100} = 2.04$ at AUC=0.55; theoretical: 2.24).\nCoverage at $N=20$ falls below nominal (80--85\\%) due to a known small-$N$ IRT limitation.\nAll fits converge with zero divergences and $\\hat{R}_{\\max} = 1.012$.\n\nAdditional findings: continuous exposure scores produce $\\sim$8\\% narrower CIs than binary indicators.\nInformative priors (SD=0.5) narrow CIs by 18\\%, while vague priors (SD=2.0) widen them by 28\\%.\n\n\\subsection{Measurement Error Model}\n\\label{sec:me_model}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Measurement error (ME) model vs.\\ simple model. At high noise ($\\sigma_e = 0.5$), the simple model's coverage collapses to 65\\%; the ME model maintains 91\\%.}\n\\label{tab:me}\n\\begin{tabular}{lcccc}\n\\toprule\n$\\sigma_e$ & \\textbf{ME Cov.} & \\textbf{ME CI (pp)} & \\textbf{Simple Cov.} & \\textbf{Simple CI (pp)} \\\\\n\\midrule\n0.1 & 95\\% & 5.2 & 91\\% & 4.8 \\\\\n0.3 & 93\\% & 7.8 & 78\\% & 5.1 \\\\\n0.5 & 91\\% & 11.4 & 65\\% & 5.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt low noise ($\\sigma_e = 0.1$), both models perform similarly.\nAt $\\sigma_e = 0.3$ (typical for real signal pipelines based on observed FP/FN rates), the ME model maintains 93\\% coverage while the simple model drops to 78\\%.\nAt $\\sigma_e = 0.5$, the simple model's coverage collapses to 65\\%---dangerously miscalibrated---while the ME model maintains 91\\%.\nThe wider CIs under the ME model reflect genuine epistemic uncertainty: models with degraded signals receive appropriately wider intervals.\n\nPost-hoc noise injection experiments confirm super-linear CI widening: $1.0\\times$ noise widens $\\gamma$ CI by 28\\%, $1.5\\times$ by 52\\%, and $2.0\\times$ by 83\\%.\n\n\\subsection{Scale Bridging: 7B Validation}\n\\label{sec:7b}\n\nTo address scale concerns, we extend controlled contamination injection to Qwen2.5-7B.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Qwen2.5-7B dose-response and signal quality.}\n\\label{tab:7b_dose}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Dosage} & \\textbf{MMLU} & \\textbf{GSM8K} & \\textbf{ARC-C} \\\\\n\\midrule\nd000 & 71.8\\% & 79.2\\% & 87.8\\% \\\\\nd005 & 72.6\\% (+0.8) & 80.4\\% (+1.2) & 88.1\\% (+0.3) \\\\\nd025 & 74.3\\% (+2.5) & 85.0\\% (+5.8) & 89.2\\% (+1.4) \\\\\nd100 & 75.9\\% (+4.1) & 91.7\\% (+12.5) & 90.6\\% (+2.8) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal AUC at 7B (d005). All four signals are effective, with continued improvement over 3B.}\n\\label{tab:7b_signal}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Signal} & \\textbf{MMLU} & \\textbf{GSM8K} & \\textbf{ARC-C} & \\textbf{Mean} \\\\\n\\midrule\nS1 Embedding & 0.948 & 0.971 & 0.943 & 0.954 \\\\\nS2 Min-K++   & 0.851 & 0.896 & 0.865 & 0.871 \\\\\nS3 ConStat   & 0.872 & 0.908 & 0.881 & 0.887 \\\\\nS4 Self-Crit.& 0.795 & 0.834 & 0.808 & 0.812 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 7B, \\contamcal{} achieves 1.4\\pp{} MAE with 95\\% coverage and Kendall's $\\tau = 0.97$---the best performance across all scales.\nSignal quality continues to improve (S2 AUC: 0.871; S4 AUC: 0.812), confirming that larger models are easier to calibrate.\n\n\\subsection{Multi-Family Validation: Llama-3.2-1B}\n\\label{sec:multi_family}\n\nTo test cross-family generalization, we repeat 3-dosage (d000/d025/d100) controlled SFT injection on Llama-3.2-1B.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-family $\\gamma$ comparison. High consistency (Pearson $r = 0.91$) suggests contamination susceptibility is a benchmark property, not model-family-specific.}\n\\label{tab:cross_family}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Bench.} & \\textbf{Qwen2.5 $\\gamma$} & \\textbf{Llama $\\gamma$} & \\textbf{Diff.} \\\\\n\\midrule\nMMLU  & 0.22 & 0.19 & $-$0.03 \\\\\nGSM8K & 0.85 & 0.72 & $-$0.13 \\\\\nARC-C & 0.18 & 0.16 & $-$0.02 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\contamcal{} achieves 2.1\\pp{} MAE with 92\\% coverage on Llama.\nThe $\\gamma$ estimates are highly consistent across families (Pearson $r = 0.91$), suggesting that contamination susceptibility is primarily a benchmark property (item structure, format, memorability) rather than a model-family artifact.\nLlama's S2 AUC (0.698) falls just below the 0.70 practical threshold at the $\\sim$1B scale, consistent with the simulation sweep predictions.\n\n\\subsection{Closed-Weight Mode}\n\\label{sec:closed_weight}\n\nFor closed-weight models lacking logit/embedding access, \\contamcal{} operates in a 2-signal mode using only S3 (ConStat) and S4 (Self-Critique).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{4-signal vs.\\ 2-signal (closed-weight) mode. At 1.5B+, 2-signal mode matches or outperforms the best existing baseline (DCR: 3.9\\pp{}).}\n\\label{tab:closed_weight}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Scale} & \\textbf{4-Sig MAE} & \\textbf{2-Sig MAE} & \\textbf{Gap} & \\textbf{2-Sig AUC} \\\\\n\\midrule\n0.5B & 2.3\\pp{} & 6.8\\pp{} & +4.5\\pp{} & 0.508 \\\\\n1.5B & 1.4\\pp{} & 2.8\\pp{} & +1.4\\pp{} & 0.782 \\\\\n3B   & 1.6\\pp{} & 2.1\\pp{} & +0.5\\pp{} & 0.831 \\\\\n\\midrule\nAvg. & 1.8\\pp{} & 3.9\\pp{} & +2.1\\pp{} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 0.5B, 2-signal mode nearly fails (6.8\\pp{} MAE) because both S3 and S4 are ineffective at this scale.\nAt 1.5B+, 2-signal mode provides meaningful calibration (2.1--2.8\\pp{} MAE), matching DCR's 3.9\\pp{} aggregate while additionally providing credible intervals (86\\% coverage).\nPractical guidance: closed-weight mode requires $\\geq$1.5B models for reliable calibration.\n\n\\subsection{Observational Case Studies}\n\\label{sec:observational}\n\n\\paragraph{RL-Trained Models.}\nWe apply \\contamcal{} to Qwen2.5-Instruct (0.5B--7B) and DeepSeek-R1-Distill (1.5B, 7B) without ground truth.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Observational calibration on RL-trained models (MMLU).}\n\\label{tab:observational}\n\\begin{tabular}{lcccr}\n\\toprule\n\\textbf{Model} & \\textbf{Raw} & \\textbf{Calib.} & \\textbf{95\\% CI} & $\\Delta$\\textbf{Rank} \\\\\n\\midrule\nQwen-0.5B-Inst & 47.2\\% & 46.8\\% & [43.1, 50.5] & 0 \\\\\nQwen-1.5B-Inst & 61.5\\% & 60.2\\% & [56.8, 63.6] & 0 \\\\\nQwen-3B-Inst   & 68.3\\% & 67.1\\% & [63.5, 70.7] & 0 \\\\\nQwen-7B-Inst   & 74.8\\% & 73.2\\% & [70.1, 76.3] & $-$1 \\\\\nDS-R1-1.5B     & 58.9\\% & 58.4\\% & [53.8, 63.0] & +1 \\\\\nDS-R1-7B       & 75.2\\% & 74.6\\% & [71.0, 78.2] & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCalibration adjustments are small (0.4--1.6\\pp{}) but CIs are notably wider (6.8\\pp{} average for Instruct, 8.2\\pp{} for DeepSeek) than in the controlled setting (4.2\\pp{})---reflecting honest uncertainty when signals degrade under RL post-training.\nGSM8K contamination persists after instruction tuning ($\\gamma = 0.42$, CI [0.18, 0.68]), suggesting RLHF does not fully eliminate memorization.\nRanking changes are minimal (1 out of 6), but the CI widths provide valuable uncertainty awareness even when rankings are preserved.\n\n\\paragraph{Specificity Check.}\nOn a known-clean benchmark, \\contamcal{} estimates $\\gamma = 0.02$ with CI including zero, confirming the method does not hallucinate contamination where none exists.\n\n\\paragraph{Frontier Scale: Qwen2.5-72B.}\nWe apply inference-only \\contamcal{} to Qwen2.5-72B.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Qwen2.5-72B observational results. Signal quality reaches its highest level; GSM8K $\\gamma$ is significantly nonzero.}\n\\label{tab:72b}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Bench.} & \\textbf{Raw} & \\textbf{Calib.} & \\textbf{95\\% CI} & $\\gamma_k$ \\\\\n\\midrule\nMMLU  & 85.4\\% & 84.2\\% & [81.5, 86.9] & 0.12 [$-$0.02, 0.28] \\\\\nGSM8K & 90.8\\% & 89.3\\% & [86.2, 92.4] & 0.18 [0.01, 0.37] \\\\\nARC-C & 94.3\\% & 93.8\\% & [91.4, 96.2] & 0.09 [$-$0.04, 0.23] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSignal quality reaches its highest levels (S2 AUC: 0.89; S4 AUC: 0.84), further supporting the scale-dependent trend.\nGSM8K's $\\gamma$ is significantly nonzero (CI [0.01, 0.37]), indicating detectable contamination even at frontier scale.\nMMLU and ARC-C $\\gamma$ CIs include zero, consistent with either low contamination or the model's genuine knowledge overshadowing memorization effects.\nCI widths average 5.5\\pp{}, reasonable for a single-model observational analysis.\n\n%======================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%======================================================================\n\n\\paragraph{Why Per-Benchmark $\\gamma_k$?}\nGSM8K ($\\gamma = 0.85$) is ${\\sim}4\\times$ more susceptible than MMLU ($\\gamma = 0.22$) or ARC-C ($\\gamma = 0.18$).\nFree-form math benchmarks are highly vulnerable because answer memorization directly accelerates generation; multiple-choice benchmarks are partially protected by forced-choice format.\nThis cross-family-consistent pattern (Qwen--Llama Pearson $r = 0.91$) suggests contamination susceptibility is an intrinsic benchmark property.\n\n\\paragraph{Honest Uncertainty Quantification.}\nA distinctive feature of \\contamcal{} is that calibration quality degrades gracefully: models with poor signals get wider CIs (0.5B: 2.3\\pp{} MAE, wider CI), while those with strong signals get tighter CIs (7B: 1.4\\pp{} MAE, tighter CI).\nThis is a feature, not a bug---the measurement error model ensures that uncertainty reflects genuine epistemic limitations.\n\n\\paragraph{Practical Deployment.}\nFull 4-signal mode requires open-weight models with logit access.\nFor closed-weight models ($\\geq$1.5B), the 2-signal mode (S3 + S4 only) achieves 2.1--2.8\\pp{} MAE, matching or exceeding existing methods while additionally providing credible intervals.\nEach per-benchmark MCMC fit requires $\\sim$45 minutes on a single GPU.\n\n%======================================================================\n\\section{Limitations}\n\\label{sec:limitations}\n%======================================================================\n\n\\begin{enumerate}\n\\item \\textbf{Model family breadth.} Controlled experiments use primarily Qwen2.5, with Llama-3.2-1B as cross-family validation. Broader family coverage (Pythia, Mistral, GPT-family) remains future work.\n\\item \\textbf{Unidimensional $\\theta$.} We use a single ability parameter per model-benchmark, which is a simplification for multifaceted benchmarks like MMLU \\citep{reckase2009multidimensional}. Multidimensional IRT is a natural extension.\n\\item \\textbf{SFT $\\neq$ real contamination.} LoRA SFT injection is a controlled proxy for real-world contamination (which may occur during pre-training, RLHF, or data mixture). Observational studies provide external validity but lack ground truth.\n\\item \\textbf{Local independence.} With a single model producing all item responses, strict local independence is violated. Our per-benchmark fitting and residual correlation analysis mitigate but do not eliminate this concern.\n\\item \\textbf{Closed-weight degradation.} The 2-signal mode fails at 0.5B and provides degraded but usable calibration at 1.5B+.\n\\item \\textbf{Computational cost.} Per-benchmark MCMC requires $\\sim$45 minutes; signal computation adds overhead for each model evaluated.\n\\end{enumerate}\n\n%======================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%======================================================================\n\nWe introduced \\contamcal{}, a framework that bridges contamination detection and score calibration via contamination-augmented 4PL IRT.\nOn controlled experiments across 0.5B--7B models and two model families, \\contamcal{} recovers true benchmark performance within 1.8\\pp{} MAE with 94\\% credible interval coverage, while providing honest uncertainty quantification that widens intervals when signals are unreliable.\nOur systematic signal characterization reveals scale-dependent effectiveness with a practical threshold at 1.5B, and identifies Min-K++ directional reversal as a cautionary finding for the detection community.\nFisher Information analysis provides theoretical grounding for identifiability bounds.\nObservational studies on RL-trained models up to 72B demonstrate directional external validity.\n\n\\contamcal{} is a statistical safety net for benchmark evaluation: it does not eliminate contamination, but it measures its effect and subtracts it out with proper uncertainty.\nFuture work includes extending to multidimensional IRT, broader model families, and integration with dynamic benchmark curation.\nData attribution methods \\citep{pruthi2020estimating,park2023trak} offer promising additional contamination signals for future integration.\n\n%======================================================================\n% References\n%======================================================================\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{50}\n\n\\bibitem[Adams et al.(1997)]{adams1997multidimensional}\nR.~Adams, M.~Wilson, and W.~Wang. 1997.\n\\newblock The multidimensional random coefficients multinomial logit model.\n\\newblock \\emph{Applied Psychological Measurement}, 21(1):1--23.\n\n\\bibitem[Angelopoulos and Bates(2023)]{angelopoulos2023conformal}\nA.~Angelopoulos and S.~Bates. 2023.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock \\emph{Foundations and Trends in Machine Learning}, 16(4):494--591.\n\n\\bibitem[Balloccu et al.(2024)]{balloccu2024leak}\nS.~Balloccu, P.~Schmidli, A.~Mott, and D.~Reiter. 2024.\n\\newblock Leak, cheat, repeat: Data contamination and evaluation malpractices in closed-source LLMs.\n\\newblock In \\emph{Proc. EACL}.\n\n\\bibitem[Cormack et al.(2009)]{cormack2009reciprocal}\nG.~V. Cormack, C.~L.~A. Clarke, and S.~B\\\"uttcher. 2009.\n\\newblock Reciprocal rank fusion outperforms condorcet and individual rank learning methods.\n\\newblock In \\emph{Proc. SIGIR}.\n\n\\bibitem[De Boeck and Wilson(2004)]{deboeck2004explanatory}\nP.~De~Boeck and M.~Wilson. 2004.\n\\newblock \\emph{Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach}.\n\\newblock Springer.\n\n\\bibitem[Dekoninck et al.(2024)]{dekoninck2024constat}\nJ.~Dekoninck, M.~Müller, M.~Fischer, and M.~Vechev. 2024.\n\\newblock ConStat: Performance-based contamination detection in large language models.\n\\newblock In \\emph{Proc. NeurIPS}.\n\n\\bibitem[Dekoninck et al.(2024b)]{dekoninck2024evading}\nJ.~Dekoninck, M.~Müller, M.~Fischer, and M.~Vechev. 2024.\n\\newblock Evading data contamination detection for language models is (too) easy.\n\\newblock \\emph{arXiv preprint arXiv:2402.02823}.\n\n\\bibitem[Dong et al.(2024)]{dong2024generalization}\nG.~Dong et al. 2024.\n\\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.\n\\newblock In \\emph{Proc. EMNLP}.\n\n\\bibitem[Eckerly(2017)]{eckerly2017detecting}\nC.~Eckerly. 2017.\n\\newblock Detecting item compromise in large-scale testing using IRT-based approaches.\n\\newblock \\emph{Journal of Educational Measurement}, 54(4):467--483.\n\n\\bibitem[Guo et al.(2017)]{guo2017calibration}\nC.~Guo, G.~Pleiss, Y.~Sun, and K.~Q. Weinberger. 2017.\n\\newblock On calibration of modern neural networks.\n\\newblock In \\emph{Proc. ICML}.\n\n\\bibitem[Holland and Wainer(1993)]{holland1993differential}\nP.~W. Holland and H.~Wainer, editors. 1993.\n\\newblock \\emph{Differential Item Functioning}.\n\\newblock Lawrence Erlbaum Associates.\n\n\\bibitem[Lalor et al.(2024)]{lalor2024benchmarking}\nJ.~P. Lalor, H.~Yang, Y.~Zhao, and D.~Rodriguez Cardenas. 2024.\n\\newblock Benchmarking large language models on psychometric testing.\n\\newblock In \\emph{Proc. AAAI}.\n\n\\bibitem[Li et al.(2024a)]{li2024task}\nY.~Li et al. 2024.\n\\newblock Task contamination: Language models may not be few-shot anymore.\n\\newblock In \\emph{Proc. AAAI}.\n\n\\bibitem[Li et al.(2024b)]{li2024cdd}\nY.~Li et al. 2024.\n\\newblock CDD: A contamination detection dataset for large language models.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Maris and Bechger(2009)]{maris2009equivalence}\nG.~Maris and T.~M. Bechger. 2009.\n\\newblock On interpreting the model parameters for the three-parameter logistic model.\n\\newblock \\emph{Measurement}, 7(2):75--88.\n\n\\bibitem[Mislevy(1986)]{mislevy1986bayes}\nR.~J. Mislevy. 1986.\n\\newblock Bayes modal estimation in item response models.\n\\newblock \\emph{Psychometrika}, 51(2):177--195.\n\n\\bibitem[Park et al.(2023)]{park2023trak}\nS.~M. Park, K.~Georgiev, A.~Ilyas, G.~Leconte, and A.~Madry. 2023.\n\\newblock TRAK: Attributing model behavior at scale.\n\\newblock In \\emph{Proc. ICML}.\n\n\\bibitem[Platt(1999)]{platt1999probabilistic}\nJ.~Platt. 1999.\n\\newblock Probabilistic outputs for support vector machines and comparisons to regularized likelihood methods.\n\\newblock \\emph{Advances in Large Margin Classifiers}, 10(3):61--74.\n\n\\bibitem[Polo et al.(2024)]{polo2024tinybenchmarks}\nF.~M. Polo et al. 2024.\n\\newblock tinyBenchmarks: Evaluating LLMs with fewer examples.\n\\newblock In \\emph{Proc. ICML}.\n\n\\bibitem[Pruthi et al.(2020)]{pruthi2020estimating}\nG.~Pruthi, F.~Liu, M.~Kale, and S.~Sundararajan. 2020.\n\\newblock Estimating training data influence by tracing gradient descent.\n\\newblock In \\emph{Proc. NeurIPS}.\n\n\\bibitem[Reckase(2009)]{reckase2009multidimensional}\nM.~D. Reckase. 2009.\n\\newblock \\emph{Multidimensional Item Response Theory}.\n\\newblock Springer.\n\n\\bibitem[Rosenbaum and Rubin(1983)]{rosenbaum1983central}\nP.~R. Rosenbaum and D.~B. Rubin. 1983.\n\\newblock The central role of the propensity score in observational studies for causal effects.\n\\newblock \\emph{Biometrika}, 70(1):41--55.\n\n\\bibitem[Sainz et al.(2023)]{sainz2023contamination}\nO.~Sainz et al. 2023.\n\\newblock NLP evaluation in trouble: On the need to measure LLM data contamination for each benchmark.\n\\newblock In \\emph{Findings of EMNLP}.\n\n\\bibitem[San~Mart\\'in et al.(2009)]{sanmartin2009}\nE.~San~Mart\\'in, J.-M. Rolin, and L.~M. Castro. 2009.\n\\newblock Identification of parametric Rasch-type models.\n\\newblock \\emph{Journal of Statistical Planning and Inference}, 139(7):2421--2433.\n\n\\bibitem[Shi et al.(2024)]{shi2024detecting}\nW.~Shi, A.~Ajith, M.~Xia, Y.~Huang, D.~Liu, T.~Blevins, D.~Chen, and L.~Zettlemoyer. 2024.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{Proc. ICLR}.\n\n\\bibitem[Sinharay(2017)]{sinharay2017use}\nS.~Sinharay. 2017.\n\\newblock Detection of item preknowledge using likelihood-ratio test and score test.\n\\newblock \\emph{Journal of Educational and Behavioral Statistics}, 42(1):46--68.\n\n\\bibitem[Talts et al.(2018)]{talts2018sbc}\nS.~Talts, M.~Betancourt, D.~Simpson, A.~Vehtari, and A.~Gelman. 2018.\n\\newblock Validating Bayesian inference algorithms with simulation-based calibration.\n\\newblock \\emph{arXiv preprint arXiv:1804.06788}.\n\n\\bibitem[Thissen et al.(1993)]{thissen1993detection}\nD.~Thissen, L.~Steinberg, and H.~Wainer. 1993.\n\\newblock Detection of differential item functioning using the parameters of item response models.\n\\newblock In \\emph{Differential Item Functioning}, pages 67--113.\n\n\\bibitem[White et al.(2024)]{white2024livebench}\nC.~White, S.~Dooley, M.~Roberts, A.~Pal, B.~Feuer, S.~Jain, R.~Shwartz-Ziv, N.~Jain, K.~Saifullah, S.~Naber, and T.~Goldstein. 2024.\n\\newblock LiveBench: A challenging, contamination-free LLM benchmark.\n\\newblock \\emph{arXiv preprint arXiv:2406.19314}.\n\n\\bibitem[Xu et al.(2024)]{xu2024benchmark}\nR.~Xu, Z.~Wang, R.~Fan, and P.~Liu. 2024.\n\\newblock Benchmark data contamination of large language models: A survey.\n\\newblock \\emph{arXiv preprint arXiv:2406.04244}.\n\n\\bibitem[Yang et al.(2023)]{yang2023rethinking}\nS.~Yang et al. 2023.\n\\newblock Rethinking benchmark and contamination for language models with rephrased samples.\n\\newblock \\emph{arXiv preprint arXiv:2311.04850}.\n\n\\bibitem[Zhang et al.(2024)]{zhang2024kds}\nY.~Zhang et al. 2024.\n\\newblock KDS: A benchmark for evaluating knowledge in large language models.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Zhuang et al.(2024)]{zhuang2024hibayes}\nY.~Zhuang et al. 2024.\n\\newblock HiBayES: A hierarchical Bayesian approach for LLM evaluation.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Zumbo(1999)]{zumbo1999handbook}\nB.~D. Zumbo. 1999.\n\\newblock \\emph{A Handbook on the Theory and Methods of Differential Item Functioning (DIF)}.\n\\newblock National Defense Headquarters, Ottawa.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "f6791ddd-7081-44e9-9f2f-7b6ccec67fcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T171536 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-cal…",
  "leafUuid": "78898540-b4c0-4538-8886-5014c914d5f2",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete ContamCal IRT calibration paper",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a"
}
```

---

### Tool call

_source line 22 · 2026-05-14T18:09:01.479Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016d9eGW7co5iL9yYQczyhpP`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78898540-b4c0-4538-8886-5014c914d5f2",
  "isSidechain": false,
  "requestId": "req_011Cb2ugFW29oGahQ38CQryS",
  "type": "assistant",
  "uuid": "babab22f-3475-4132-9edc-c07d0e4375d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014KHtS8wKotGdJ6TtZgr1EY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17401,
      "cache_read_input_tokens": 49522,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17401,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 49522,
          "cache_creation_input_tokens": 17401,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17401
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

_source line 23 · 2026-05-14T18:09:02.079Z_

<details><summary>↩ Tool result · reported error · `toolu_016d9eGW7co5iL9yYQczyhpP`</summary>

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
  "parentUuid": "babab22f-3475-4132-9edc-c07d0e4375d4",
  "isSidechain": false,
  "promptId": "14a905e9-cf62-4ad0-acbf-909375bdc04c",
  "type": "user",
  "uuid": "810bc140-d477-4cb9-a9ea-d6502351d9ac",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "babab22f-3475-4132-9edc-c07d0e4375d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-14T18:09:05.559Z_

<details><summary>Logged reasoning block</summary>

```text
The acl.sty file is not available. Let me switch to a standard article class instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "810bc140-d477-4cb9-a9ea-d6502351d9ac",
  "isSidechain": false,
  "requestId": "req_011Cb2ugb31kn3JpAsBeBTpv",
  "type": "assistant",
  "uuid": "87f1a3eb-db1f-478d-a0b1-b34f90a41ce8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XBU8n2Muqg3iEdrceAZEyL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 468,
      "cache_read_input_tokens": 66923,
      "output_tokens": 499,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 499,
          "cache_read_input_tokens": 66923,
          "cache_creation_input_tokens": 468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 468
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

_source line 25 · 2026-05-14T18:09:06.058Z_

ACL style not available. Let me fix the document class to use standard article formatting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87f1a3eb-db1f-478d-a0b1-b34f90a41ce8",
  "isSidechain": false,
  "requestId": "req_011Cb2ugb31kn3JpAsBeBTpv",
  "type": "assistant",
  "uuid": "99203804-6ad0-4e25-a022-3889a090de4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XBU8n2Muqg3iEdrceAZEyL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 468,
      "cache_read_input_tokens": 66923,
      "output_tokens": 499,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 499,
          "cache_read_input_tokens": 66923,
          "cache_creation_input_tokens": 468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 468
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

_source line 26 · 2026-05-14T18:09:09.852Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01DkVSsejfETjFZoUBgxsnx9`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{bm}\n\\usepackage{microtype}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{array}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{bm}\n\\usepackage{microtype}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{array}\n\\usepackage{hyperref}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99203804-6ad0-4e25-a022-3889a090de4e",
  "isSidechain": false,
  "requestId": "req_011Cb2ugb31kn3JpAsBeBTpv",
  "type": "assistant",
  "uuid": "2f7544e5-f2fe-4f88-b41c-00ddb17d2528",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XBU8n2Muqg3iEdrceAZEyL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 468,
      "cache_read_input_tokens": 66923,
      "output_tokens": 499,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 499,
          "cache_read_input_tokens": 66923,
          "cache_creation_input_tokens": 468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 468
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

_source line 27 · 2026-05-14T18:09:09.989Z_

<details><summary>↩ Tool result · `toolu_01DkVSsejfETjFZoUBgxsnx9`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f7544e5-f2fe-4f88-b41c-00ddb17d2528",
  "isSidechain": false,
  "promptId": "14a905e9-cf62-4ad0-acbf-909375bdc04c",
  "type": "user",
  "uuid": "f86c06a3-12e3-4476-8ecc-93f9926c08b1",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{bm}\n\\usepackage{microtype}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{array}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{bm}\n\\usepackage{microtype}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{array}\n\\usepackage{hyperref}",
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
          " \\usepackage{amsmath,amssymb,amsfonts}"
        ]
      },
      {
        "oldStart": 12,
        "oldLines": 6,
        "newStart": 12,
        "newLines": 7,
        "lines": [
          " \\usepackage{natbib}",
          " \\usepackage{tabularx}",
          " \\usepackage{array}",
          "+\\usepackage{hyperref}",
          " ",
          " \\newcommand{\\contamcal}{\\textsc{ContamCal}}",
          " \\newcommand{\\pp}{\\,\\text{pp}}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "2f7544e5-f2fe-4f88-b41c-00ddb17d2528",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T18:09:13.840Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01A5L76wWLqWk1iCGescrKJg`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f86c06a3-12e3-4476-8ecc-93f9926c08b1",
  "isSidechain": false,
  "requestId": "req_011Cb2uhAwCqkNDMrGEWhMGr",
  "type": "assistant",
  "uuid": "b92e8f3f-c1b3-478c-88ae-9be6f7cca3b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0187KWFLzcZ6BRx6aS41W2uF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 588,
      "cache_read_input_tokens": 67391,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 588,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 67391,
          "cache_creation_input_tokens": 588,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 588
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

_source line 29 · 2026-05-14T18:09:20.711Z_

<details><summary>↩ Tool result · `toolu_01A5L76wWLqWk1iCGescrKJg`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/tools/bm.sty)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.sty
(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype-pdftex.def)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
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

Package natbib Warning: Citation `sainz2023contamination' on page 1 undefined o
n input line 44.


Package natbib Warning: Citation `balloccu2024leak' on page 1 undefined on inpu
t line 44.


Package natbib Warning: Citation `li2024task' on page 1 undefined on input line
 44.


Package natbib Warning: Citation `yang2023rethinking' on page 1 undefined on in
put line 45.


Package natbib Warning: Citation `dekoninck2024evading' on page 1 undefined on 
input line 45.


Package natbib Warning: Citation `xu2024benchmark' on page 1 undefined on input
 line 46.


Package natbib Warning: Citation `rosenbaum1983central' on page 1 undefined on 
input line 49.


Package natbib Warning: Citation `shi2024detecting' on page 1 undefined on inpu
t line 52.


Package natbib Warning: Citation `dekoninck2024constat' on page 1 undefined on 
input line 52.


Package natbib Warning: Citation `yang2023rethinking' on page 1 undefined on in
put line 52.


Package natbib Warning: Citation `lalor2024benchmarking' on page 1 undefined on
 input line 53.


Package natbib Warning: Citation `polo2024tinybenchmarks' on page 1 undefined o
n input line 53.


Package natbib Warning: Citation `dong2024generalization' on page 1 undefined o
n input line 54.


Package natbib Warning: Citation `zhuang2024hibayes' on page 1 undefined on inp
ut line 55.


Package natbib Warning: Citation `eckerly2017detecting' on page 1 undefined on 
input line 57.


Package natbib Warning: Citation `sinharay2017use' on page 1 undefined on input
 line 57.


Package natbib Warning: Citation `deboeck2004explanatory' on page 1 undefined o
n input line 57.

(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)

LaTeX Warning: Reference `sec:method' on page 1 undefined on input line 62.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]

LaTeX Warning: Reference `sec:signal_analysis' on page 2 undefined on input lin
e 63.


LaTeX Warning: Reference `sec:experiments' on page 2 undefined on input line 64
.


Package natbib Warning: Citation `shi2024detecting' on page 2 undefined on inpu
t line 74.


Package natbib Warning: Citation `dekoninck2024constat' on page 2 undefined on 
input line 74.


Package natbib Warning: Citation `zhang2024kds' on page 2 undefined on input li
ne 74.


Package natbib Warning: Citation `li2024cdd' on page 2 undefined on input line 
74.


Package natbib Warning: Citation `yang2023rethinking' on page 2 undefined on in
put line 75.


Package natbib Warning: Citation `lalor2024benchmarking' on page 2 undefined on
 input line 79.


Package natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o
n input line 79.


Package natbib Warning: Citation `white2024livebench' on page 2 undefined on in
put line 79.


Package natbib Warning: Citation `zhuang2024hibayes' on page 2 undefined on inp
ut line 79.


Package natbib Warning: Citation `deboeck2004explanatory' on page 2 undefined o
n input line 81.


Package natbib Warning: Citation `adams1997multidimensional' on page 2 undefine
d on input line 81.


Package natbib Warning: Citation `eckerly2017detecting' on page 2 undefined on 
input line 81.


Package natbib Warning: Citation `sinharay2017use' on page 2 undefined on input
 line 81.


Package natbib Warning: Citation `dong2024generalization' on page 2 undefined o
n input line 84.


Package natbib Warning: Citation `xu2024benchmark' on page 2 undefined on input
 line 85.


Package natbib Warning: Citation `white2024livebench' on page 2 undefined on in
put line 86.


Package natbib Warning: Citation `guo2017calibration' on page 2 undefined on in
put line 90.


Package natbib Warning: Citation `platt1999probabilistic' on page 2 undefined o
n input line 90.


Package natbib Warning: Citation `angelopoulos2023conformal' on page 2 undefine
d on input line 91.


Package natbib Warning: Citation `holland1993differential' on page 2 undefined 
on input line 94.


Package natbib Warning: Citation `thissen1993detection' on page 2 undefined on 
input line 94.


Package natbib Warning: Citation `zumbo1999handbook' on page 2 undefined on inp
ut line 94.


Package natbib Warning: Citation `shi2024detecting' on page 2 undefined on inpu
t line 114.

[2]

Package natbib Warning: Citation `dekoninck2024constat' on page 3 undefined on 
input line 118.


Package natbib Warning: Citation `cormack2009reciprocal' on page 3 undefined on
 input line 125.


LaTeX Warning: Reference `sec:identifiability' on page 3 undefined on input lin
e 170.

[3]

LaTeX Warning: Reference `sec:main_results' on page 4 undefined on input line 1
75.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 188.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\times' on input line 188.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 188.


LaTeX Warning: Reference `tab:signal_scale_auc' on page 4 undefined on input li
ne 190.


LaTeX Warning: Reference `tab:signal_survival' on page 4 undefined on input lin
e 230.

[4]

LaTeX Warning: Reference `tab:rrf' on page 5 undefined on input line 284.

[5]

Package natbib Warning: Citation `xu2024benchmark' on page 6 undefined on input
 line 333.


Package natbib Warning: Citation `dong2024generalization' on page 6 undefined o
n input line 333.

[6]

LaTeX Warning: Reference `tab:dose_response' on page 7 undefined on input line 
423.

[7] [8] [9]

Package natbib Warning: Citation `reckase2009multidimensional' on page 10 undef
ined on input line 692.

[10]

Package natbib Warning: Citation `pruthi2020estimating' on page 11 undefined on
 input line 712.


Package natbib Warning: Citation `park2023trak' on page 11 undefined on input l
ine 712.

No file paper.bbl.
[11] [12]

Package natbib Warning: There were undefined citations.

[13] (./paper.aux

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
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (13 pages, 199300 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/tools/bm.sty)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.sty
(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype-pdftex.def)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
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
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-ptm.cfg) (./paper.out)
(./paper.out) (/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-cmr.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msa.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msb.cfg) [1{/var/lib/texm
f/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/d
vips/base/8r.enc}] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)
[2] [3]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 188.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\times' on input line 188.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 188.

[4] [5] [6] [7] [8] [9] [10]
No file paper.bbl.
[11] [12] [13] (./paper.aux)

LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (13 pages, 205781 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b92e8f3f-c1b3-478c-88ae-9be6f7cca3b6",
  "isSidechain": false,
  "promptId": "14a905e9-cf62-4ad0-acbf-909375bdc04c",
  "type": "user",
  "uuid": "e3e61485-6c5c-47b2-9575-b7e56f9c27b6",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/bm.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.sty\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype-pdftex.def)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-ptm.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-cmr.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msa.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msb.cfg)\n\nPackage natbib Warning: Citation `sainz2023contamination' on page 1 undefined o\nn input line 44.\n\n\nPackage natbib Warning: Citation `balloccu2024leak' on page 1 undefined on inpu\nt line 44.\n\n\nPackage natbib Warning: Citation `li2024task' on page 1 undefined on input line\n 44.\n\n\nPackage natbib Warning: Citation `yang2023rethinking' on page 1 undefined on in\nput line 45.\n\n\nPackage natbib Warning: Citation `dekoninck2024evading' on page 1 undefined on \ninput line 45.\n\n\nPackage natbib Warning: Citation `xu2024benchmark' on page 1 undefined on input\n line 46.\n\n\nPackage natbib Warning: Citation `rosenbaum1983central' on page 1 undefined on \ninput line 49.\n\n\nPackage natbib Warning: Citation `shi2024detecting' on page 1 undefined on inpu\nt line 52.\n\n\nPackage natbib Warning: Citation `dekoninck2024constat' on page 1 undefined on \ninput line 52.\n\n\nPackage natbib Warning: Citation `yang2023rethinking' on page 1 undefined on in\nput line 52.\n\n\nPackage natbib Warning: Citation `lalor2024benchmarking' on page 1 undefined on\n input line 53.\n\n\nPackage natbib Warning: Citation `polo2024tinybenchmarks' on page 1 undefined o\nn input line 53.\n\n\nPackage natbib Warning: Citation `dong2024generalization' on page 1 undefined o\nn input line 54.\n\n\nPackage natbib Warning: Citation `zhuang2024hibayes' on page 1 undefined on inp\nut line 55.\n\n\nPackage natbib Warning: Citation `eckerly2017detecting' on page 1 undefined on \ninput line 57.\n\n\nPackage natbib Warning: Citation `sinharay2017use' on page 1 undefined on input\n line 57.\n\n\nPackage natbib Warning: Citation `deboeck2004explanatory' on page 1 undefined o\nn input line 57.\n\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)\n\nLaTeX Warning: Reference `sec:method' on page 1 undefined on input line 62.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n\nLaTeX Warning: Reference `sec:signal_analysis' on page 2 undefined on input lin\ne 63.\n\n\nLaTeX Warning: Reference `sec:experiments' on page 2 undefined on input line 64\n.\n\n\nPackage natbib Warning: Citation `shi2024detecting' on page 2 undefined on inpu\nt line 74.\n\n\nPackage natbib Warning: Citation `dekoninck2024constat' on page 2 undefined on \ninput line 74.\n\n\nPackage natbib Warning: Citation `zhang2024kds' on page 2 undefined on input li\nne 74.\n\n\nPackage natbib Warning: Citation `li2024cdd' on page 2 undefined on input line \n74.\n\n\nPackage natbib Warning: Citation `yang2023rethinking' on page 2 undefined on in\nput line 75.\n\n\nPackage natbib Warning: Citation `lalor2024benchmarking' on page 2 undefined on\n input line 79.\n\n\nPackage natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o\nn input line 79.\n\n\nPackage natbib Warning: Citation `white2024livebench' on page 2 undefined on in\nput line 79.\n\n\nPackage natbib Warning: Citation `zhuang2024hibayes' on page 2 undefined on inp\nut line 79.\n\n\nPackage natbib Warning: Citation `deboeck2004explanatory' on page 2 undefined o\nn input line 81.\n\n\nPackage natbib Warning: Citation `adams1997multidimensional' on page 2 undefine\nd on input line 81.\n\n\nPackage natbib Warning: Citation `eckerly2017detecting' on page 2 undefined on \ninput line 81.\n\n\nPackage natbib Warning: Citation `sinharay2017use' on page 2 undefined on input\n line 81.\n\n\nPackage natbib Warning: Citation `dong2024generalization' on page 2 undefined o\nn input line 84.\n\n\nPackage natbib Warning: Citation `xu2024benchmark' on page 2 undefined on input\n line 85.\n\n\nPackage natbib Warning: Citation `white2024livebench' on page 2 undefined on in\nput line 86.\n\n\nPackage natbib Warning: Citation `guo2017calibration' on page 2 undefined on in\nput line 90.\n\n\nPackage natbib Warning: Citation `platt1999probabilistic' on page 2 undefined o\nn input line 90.\n\n\nPackage natbib Warning: Citation `angelopoulos2023conformal' on page 2 undefine\nd on input line 91.\n\n\nPackage natbib Warning: Citation `holland1993differential' on page 2 undefined \non input line 94.\n\n\nPackage natbib Warning: Citation `thissen1993detection' on page 2 undefined on \ninput line 94.\n\n\nPackage natbib Warning: Citation `zumbo1999handbook' on page 2 undefined on inp\nut line 94.\n\n\nPackage natbib Warning: Citation `shi2024detecting' on page 2 undefined on inpu\nt line 114.\n\n[2]\n\nPackage natbib Warning: Citation `dekoninck2024constat' on page 3 undefined on \ninput line 118.\n\n\nPackage natbib Warning: Citation `cormack2009reciprocal' on page 3 undefined on\n input line 125.\n\n\nLaTeX Warning: Reference `sec:identifiability' on page 3 undefined on input lin\ne 170.\n\n[3]\n\nLaTeX Warning: Reference `sec:main_results' on page 4 undefined on input line 1\n75.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 188.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\times' on input line 188.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 188.\n\n\nLaTeX Warning: Reference `tab:signal_scale_auc' on page 4 undefined on input li\nne 190.\n\n\nLaTeX Warning: Reference `tab:signal_survival' on page 4 undefined on input lin\ne 230.\n\n[4]\n\nLaTeX Warning: Reference `tab:rrf' on page 5 undefined on input line 284.\n\n[5]\n\nPackage natbib Warning: Citation `xu2024benchmark' on page 6 undefined on input\n line 333.\n\n\nPackage natbib Warning: Citation `dong2024generalization' on page 6 undefined o\nn input line 333.\n\n[6]\n\nLaTeX Warning: Reference `tab:dose_response' on page 7 undefined on input line \n423.\n\n[7] [8] [9]\n\nPackage natbib Warning: Citation `reckase2009multidimensional' on page 10 undef\nined on input line 692.\n\n[10]\n\nPackage natbib Warning: Citation `pruthi2020estimating' on page 11 undefined on\n input line 712.\n\n\nPackage natbib Warning: Citation `park2023trak' on page 11 undefined on input l\nine 712.\n\nNo file paper.bbl.\n[11] [12]\n\nPackage natbib Warning: There were undefined citations.\n\n[13] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts\n/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (13 pages, 199300 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/bm.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.sty\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype-pdftex.def)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-ptm.cfg) (./paper.out)\n(./paper.out) (/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-cmr.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msa.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msb.cfg) [1{/var/lib/texm\nf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/d\nvips/base/8r.enc}] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)\n[2] [3]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 188.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\times' on input line 188.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 188.\n\n[4] [5] [6] [7] [8] [9] [10]\nNo file paper.bbl.\n[11] [12] [13] (./paper.aux)\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts\n/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (13 pages, 205781 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b92e8f3f-c1b3-478c-88ae-9be6f7cca3b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-14T18:09:20.728Z_

```json
{
  "parentUuid": "e3e61485-6c5c-47b2-9575-b7e56f9c27b6",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f4d00c5b-cfbf-4938-abf8-8f51c55c317e",
  "timestamp": "2026-05-14T18:09:20.728Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T171536 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-cal…",
  "leafUuid": "f4d00c5b-cfbf-4938-abf8-8f51c55c317e",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete ContamCal IRT calibration paper",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a"
}
```

---

### Assistant

_source line 33 · 2026-05-14T18:09:24.415Z_

<details><summary>Logged reasoning block</summary>

```text
Third run needed to resolve the label change warning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4d00c5b-cfbf-4938-abf8-8f51c55c317e",
  "isSidechain": false,
  "requestId": "req_011Cb2uhxjWhs8Auxmej8d8H",
  "type": "assistant",
  "uuid": "2937a3b7-ea8e-4413-bac9-581ab9939b93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JfQ4WkmunuLfqcgfnzxgcW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7987,
      "cache_read_input_tokens": 67979,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7987,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 204,
          "cache_read_input_tokens": 67979,
          "cache_creation_input_tokens": 7987,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7987
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

_source line 34 · 2026-05-14T18:09:24.423Z_

Need one more pass to resolve the label change warning.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2937a3b7-ea8e-4413-bac9-581ab9939b93",
  "isSidechain": false,
  "requestId": "req_011Cb2uhxjWhs8Auxmej8d8H",
  "type": "assistant",
  "uuid": "0998a6da-4328-420d-afea-c3d61f12ce7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JfQ4WkmunuLfqcgfnzxgcW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7987,
      "cache_read_input_tokens": 67979,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7987,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 204,
          "cache_read_input_tokens": 67979,
          "cache_creation_input_tokens": 7987,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7987
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

_source line 35 · 2026-05-14T18:09:27.723Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01D57WjkqPcUSWabnmJimC7g`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Third LaTeX pass for stable cross-references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0998a6da-4328-420d-afea-c3d61f12ce7e",
  "isSidechain": false,
  "requestId": "req_011Cb2uhxjWhs8Auxmej8d8H",
  "type": "assistant",
  "uuid": "58d97cf5-be5c-488f-b724-4950cb6fa085",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JfQ4WkmunuLfqcgfnzxgcW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7987,
      "cache_read_input_tokens": 67979,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7987,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 204,
          "cache_read_input_tokens": 67979,
          "cache_creation_input_tokens": 7987,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7987
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

_source line 36 · 2026-05-14T18:09:31.030Z_

<details><summary>↩ Tool result · `toolu_01D57WjkqPcUSWabnmJimC7g`</summary>

```text
/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times
/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (13 pages, 205781 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58d97cf5-be5c-488f-b724-4950cb6fa085",
  "isSidechain": false,
  "promptId": "14a905e9-cf62-4ad0-acbf-909375bdc04c",
  "type": "user",
  "uuid": "961274e6-8a5f-45ef-b4d1-993fcfb04053",
  "toolUseResult": {
    "stdout": "/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\n/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (13 pages, 205781 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "58d97cf5-be5c-488f-b724-4950cb6fa085",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-14T18:09:46.268Z_

PDF 编译成功，13 页，205KB。

输出文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best/paper.pdf`

论文覆盖了 experiment_data.json 中全部 10 个实验：
- **Signal Pipeline** → Table 1 (Signal × Scale AUC) + Signal Survival summary
- **RRF Aggregation Ablation** → Table 5 (RRF vs single-signal + FP robustness)
- **Simulation Identifiability Sweep** → Table 7 (γ recovery grid, Fisher Info bounds)
- **Noise Propagation / ME Model** → Table 8 (ME vs Simple coverage)
- **IRT Calibration & Baselines** → Table 2 (main 8-method comparison), per-benchmark MAE, γ_k estimates, dose-response
- **Scale Bridging 7B** → Tables 9-10 (7B dose-response + signal AUC)
- **Multi-Family Validation** → Table 11 (cross-family γ comparison)
- **Signal Survival Multiscale** → Table 3 (effectiveness summary) + Min-K++ reversal
- **RL Observational Case Study** → Table 12 (Instruct/DeepSeek calibration + specificity check)
- **72B Observational** → Table 13
- **Closed-Weight 2-Signal** → Table 11 (4-signal vs 2-signal)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "961274e6-8a5f-45ef-b4d1-993fcfb04053",
  "isSidechain": false,
  "requestId": "req_011Cb2uiineb4cyyWE77mTNd",
  "type": "assistant",
  "uuid": "bd07d34f-7405-4192-ace3-22e5e381bf85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D9hhQMawicP4uCNZhVy2Dm",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 314,
      "cache_read_input_tokens": 75966,
      "output_tokens": 401,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 314,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 401,
          "cache_read_input_tokens": 75966,
          "cache_creation_input_tokens": 314,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 314
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T171536 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-cal…",
  "leafUuid": "bd07d34f-7405-4192-ace3-22e5e381bf85",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete ContamCal IRT calibration paper",
  "sessionId": "5f0cff07-cb6a-487f-be6b-6af3047fe23a"
}
```

---
