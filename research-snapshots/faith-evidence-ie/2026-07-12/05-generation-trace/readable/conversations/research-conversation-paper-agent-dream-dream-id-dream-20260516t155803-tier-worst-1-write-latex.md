# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T155803 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/3f919891-e40b-48de-b5ba-d9c1d745dedc.jsonl`
- **Structured JSON:** [`65475baa896d48b7b28b.json`](../../sessions/65/65475baa896d48b7b28b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T16:21:17.935Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T16:21:17.935Z",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T155803 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T155803/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T155803/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T155803/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T155803/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：完全 reframe 为 empirical analysis paper。标题改为 \"The Cost of Faithfulness: What Happens When LLMs Must Justify Their Extractions\"。 RSFT 不再定位为推荐方案，而是 \"least harmful training strategy we found\"。 Post-hoc retrieval 追平 RSFT 变成论文正文的一部分。 去掉所有 effective/competitive 措辞，改用 reveals/exposes/characterizes。 仍投 EMNLP Main（analysis paper 传统），Findings 可接受，同时准备 AAAI 2027 fallback。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T155803/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T16:21:17.940Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T16:21:17.940Z",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc"
}
```

---

## Round 1

25 recorded events

### User

_source line 3 · 2026-05-16T16:21:17.961Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T155803 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T155803/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T155803/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T155803/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T155803/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：完全 reframe 为 empirical analysis paper。标题改为 "The Cost of Faithfulness: What Happens When LLMs Must Justify Their Extractions"。 RSFT 不再定位为推荐方案，而是 "least harmful training strategy we found"。 Post-hoc retrieval 追平 RSFT 变成论文正文的一部分。 去掉所有 effective/competitive 措辞，改用 reveals/exposes/characterizes。 仍投 EMNLP Main（analysis paper 传统），Findings 可接受，同时准备 AAAI 2027 fallback。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T155803/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e3a72ef5-4fa0-4d72-a416-3b6212473770",
  "type": "user",
  "uuid": "c8e0748d-3018-4e51-815d-6b8c4e3a624d",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T16:21:17.961Z_

```json
{
  "parentUuid": "c8e0748d-3018-4e51-815d-6b8c4e3a624d",
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
  "uuid": "583f02bd-a6c4-4689-b72b-92e5b5049bf7",
  "timestamp": "2026-05-16T16:21:17.961Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T16:21:17.961Z_

```json
{
  "parentUuid": "583f02bd-a6c4-4689-b72b-92e5b5049bf7",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "341f5cf7-ef17-46d4-b3b6-4f2cf9668251",
  "timestamp": "2026-05-16T16:21:17.961Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc",
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
  "aiTitle": "Generate empirical analysis paper on LLM faithfulness costs",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc"
}
```

---

### Assistant

_source line 7 · 2026-05-16T16:21:20.983Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the experiment data and paper framing files to understand what I need to write.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "341f5cf7-ef17-46d4-b3b6-4f2cf9668251",
  "isSidechain": false,
  "requestId": "req_011Cb6Z5vN5BteCsRsq1zXF8",
  "type": "assistant",
  "uuid": "f06670e7-2808-4320-b685-d741f44158d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015u2F7MeHNaSYR7DdxQgfjy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11191,
      "cache_read_input_tokens": 11841,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11191,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 225,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11191,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11191
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

_source line 8 · 2026-05-16T16:21:21.576Z_

<details open><summary>🔧 Tool call — Read · `toolu_019bXj8uXXGWd6eWiyCHe49u`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T155803/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f06670e7-2808-4320-b685-d741f44158d1",
  "isSidechain": false,
  "requestId": "req_011Cb6Z5vN5BteCsRsq1zXF8",
  "type": "assistant",
  "uuid": "4dadee8b-657c-468e-9dd2-fe1a6aedf66b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015u2F7MeHNaSYR7DdxQgfjy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11191,
      "cache_read_input_tokens": 11841,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11191,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 225,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11191,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11191
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

_source line 9 · 2026-05-16T16:21:21.846Z_

<details><summary>↩ Tool result · `toolu_019bXj8uXXGWd6eWiyCHe49u`</summary>

```text
1	[
2	  {
3	    "name": "Test Set Evaluation (RSFT CED best + SFT baselines)",
4	    "description": "用 RSFT CED best config (s43/s44) 和 SFT baseline/no-evidence 在 DocRED test set 上评估。 提交 CodaLab 获得官方 Ign-F1/F1，本地计算 Evi-F1 和 EDCR。\n",
5	    "results": {
6	      "test_ign_f1_rsft_ced_s43": 40.2,
7	      "test_f1_rsft_ced_s43": 41.0,
8	      "test_ign_f1_rsft_ced_s44": 39.8,
9	      "test_f1_rsft_ced_s44": 40.5,
10	      "test_evi_f1_rsft_ced_s43": 0.798,
11	      "test_evi_f1_rsft_ced_s44": 0.793,
12	      "test_edcr_rsft_ced_s43": 0.672,
13	      "test_ign_f1_sft_baseline": 35.8,
14	      "test_ign_f1_sft_no_evidence": 42.5,
15	      "test_evidence_tax_4b": -6.7,
16	      "dev_test_gap_rsft_best": -5.65,
17	      "dev_test_gap_sft_no_evidence": -4.86
18	    },
19	    "tables": [
20	      {
21	        "name": "Table: Test Set Results",
22	        "columns": [
23	          "Config",
24	          "Test Ign-F1",
25	          "Test F1",
26	          "Test Evi-F1",
27	          "Δ vs SFT",
28	          "Δ dev→test"
29	        ],
30	        "rows": [
31	          [
32	            "SFT no-evidence",
33	            "42.5",
34	            "43.8",
35	            "—",
36	            "+6.7",
37	            "-4.86"
38	          ],
39	          [
40	            "SFT baseline",
41	            "35.8",
42	            "36.5",
43	            "0.782",
44	            "—",
45	            "-4.56"
46	          ],
47	          [
48	            "RSFT CED s43",
49	            "40.2",
50	            "41.0",
51	            "0.798",
52	            "+4.4",
53	            "-5.65"
54	          ],
55	          [
56	            "RSFT CED s44",
57	            "39.8",
58	            "40.5",
59	            "0.793",
60	            "+4.0",
61	            "-5.71"
62	          ],
63	          [
64	            "RSFT flat-NLI s42",
65	            "39.5",
66	            "40.2",
67	            "0.790",
68	            "+3.7",
69	            "-4.99"
70	          ]
71	        ]
72	      }
73	    ],
74	    "figures": [],
75	    "analysis": "Test set 退化 5.65pp 是 worst 档的核心打击。这暴露了两个问题： (1) CED scoring 在 RSFT 数据筛选时对 dev gold evidence 的隐式过拟合——test set 标注者偏好不同的 evidence 句子组合； (2) Evidence generation 的代价在 test distribution 下更严重（tax 从 -7.0 扩大至 -6.7pp）。 但 RSFT 仍显著 > SFT baseline (+4.4pp)，且 evidence 质量保持（test evi_f1=0.798 vs dev 0.816，仅 -1.8pp）。 论文叙事调整：不再声称 \"RSFT 是 competitive 方案\"，改为 \"RSFT 是我们发现的 least harmful training strategy， 但 dev-test gap 警示 evidence-grounded IE 的评估需要更稳健的 held-out 设计\"。 Evidence tax 扩大成为论文的 empirical finding 之一——进一步支撑 \"cost of faithfulness\" 叙事。\n\n\nWorst 档核心假设：dev→test 退化 > 4pp。Dev best RSFT CED s43 Ign-F1=45.85，退化 5.65pp 至 40.2—— 这在 DocRED 上并非不可能。DocRED test set 由不同标注者标注且标注一致性低于 dev（Re-DocRED 论文已指出）， RSFT 通过 CED scoring 对 dev-aligned 的 gold evidence pattern 进行了隐式过拟合： CED scorer 训练于 NLI 数据但在 DocRED dev gold 上筛选 RSFT 数据，筛选偏好与 dev 标注风格高度耦合。 Test set 标注风格偏移导致 RSFT 增益大幅缩水（从 dev +5.5pp 缩至 test +4.4pp over SFT）， 而 SFT no-evidence 作为更简单的目标函数，dev→test 退化相对较小。 Evidence tax 从 dev 的 -7.9pp 扩大至 test 的 -6.7pp（SFT no-evidence 42.5 vs SFT baseline 35.8）， 暴露 evidence generation 在 test distribution 下的负担更重。 关键叙事影响：RSFT test Ign-F1 < 41.5 使 \"RSFT 显著优于 SFT\" 的必要条件仍满足（+4.4pp）， 但绝对数字太低（40.2 vs encoder SOTA >60），且 evidence tax 扩大使方法贡献可信度下降。\n"
76	  },
77	  {
78	    "name": "Re-DocRED Cross-Dataset RSFT Evaluation",
79	    "description": "在 Re-DocRED 上对当前 best RSFT config 做完整 eval。 D080 已有 SFT 结果（Ign-F1 下降 3.15pp，Evi-F1=0.817），此处预测 RSFT 在 Re-DocRED 上的表现。\n",
80	    "results": {
81	      "redocred_rsft_ced_ign_f1": 38.1,
82	      "redocred_rsft_ced_evi_f1": 0.801,
83	      "redocred_rsft_ced_edcr": 0.695,
84	      "redocred_sft_ign_f1": 36.59,
85	      "redocred_rsft_vs_sft_delta": 1.5,
86	      "redocred_rsft_vs_docred_rsft_delta": -7.75,
87	      "redocred_no_evidence_ign_f1": 41.8,
88	      "redocred_evidence_tax": -5.2
89	    },
90	    "tables": [
91	      {
92	        "name": "Table: Re-DocRED Cross-Dataset Results",
93	        "columns": [
94	          "Config",
95	          "Re-DocRED Ign-F1",
96	          "Re-DocRED Evi-F1",
97	          "Δ vs DocRED"
98	        ],
99	        "rows": [
100	          [
101	            "SFT baseline",
102	            "36.59",
103	            "0.817",
104	            "-3.15pp"
105	          ],
106	          [
107	            "SFT no-evidence",
108	            "41.8",
109	            "—",
110	            "—"
111	          ],
112	          [
113	            "RSFT CED",
114	            "38.1",
115	            "0.801",
116	            "-7.75pp vs DocRED RSFT"
117	          ],
118	          [
119	            "Evidence tax",
120	            "-5.2pp",
121	            "—",
122	            "vs DocRED -7.9pp"
123	          ]
124	        ]
125	      }
126	    ],
127	    "figures": [],
128	    "analysis": "RSFT 在 Re-DocRED 上增益大幅缩水（+1.5pp vs DocRED +5.5pp）暴露了 CED scoring 的 dataset-specificity。 但 evidence 质量跨数据集保持（evi_f1 0.801）是 positive signal——说明 evidence extraction 能力本身泛化， 问题出在 CED-filtered RSFT 训练数据对 DocRED 标注分布的过拟合。 在 worst 叙事下，这成为 \"RSFT 增益依赖于 scoring function 与 gold 分布的匹配度\" 的 empirical warning。 论文定位：Re-DocRED 结果不支撑 RSFT 作为通用方案，但支撑 evidence extraction 的跨数据集鲁棒性。\n\n\nRe-DocRED 修正了 DocRED 的大量 false negative（~55% triples 无 evidence 标注）， RSFT 的 CED scoring function 在 DocRED gold 上训练的筛选偏好在 Re-DocRED 上适配性降低。 具体而言：RSFT 在 DocRED dev 上的 +5.5pp 增益来自 CED 对 DocRED 标注风格的精准匹配， Re-DocRED 标注更完整但 evidence 分布不同，导致 RSFT 增益缩水至 +1.5pp。 更关键的是，Re-DocRED 的 evaluation 中有 55% triples 无 evidence gold—— 这些 triples 上 RSFT 生成的 evidence 无法被评估，但生成负担仍在，导致 evidence tax 显著扩大。 Evi-F1 保持在 0.801（仅在有 evidence 标注的子集上评估），与 D080 SFT 的 0.817 接近但略降。 这表明 evidence extraction 能力本身跨数据集泛化，但 RSFT 的 relation extraction 增益不泛化。\n"
129	  },
130	  {
131	    "name": "EDCR Human Annotation Validation",
132	    "description": "100 个样本人工标注，判断每个 cited evidence sentence 是否真正支持对应 relation。 计算 EDCR 与人工判断的 Spearman 相关性。\n",
133	    "results": {
134	      "n_annotated_samples": 100,
135	      "annotator_agreement_kappa": 0.52,
136	      "edcr_human_spearman_rho": 0.31,
137	      "edcr_human_spearman_p": 0.0018,
138	      "edcr_human_pearson_r": 0.27,
139	      "human_evi_precision": 0.72,
140	      "human_evi_recall": 0.58,
141	      "false_positive_evidence_rate": 0.28,
142	      "edcr_identifies_bad_cases": true,
143	      "edcr_magnitude_calibration": "poor"
144	    },
145	    "tables": [
146	      {
147	        "name": "Table: EDCR Human Validation",
148	        "columns": [
149	          "Metric",
150	          "Value",
151	          "95% CI"
152	        ],
153	        "rows": [
154	          [
155	            "Spearman ρ (EDCR vs human)",
156	            "0.31",
157	            "[0.12, 0.48]"
158	          ],
159	          [
160	            "Pearson r (EDCR vs human)",
161	            "0.27",
162	            "[0.08, 0.44]"
163	          ],
164	          [
165	            "Annotator κ",
166	            "0.52",
167	            "[0.40, 0.64]"
168	          ],
169	          [
170	            "Human evidence precision",
171	            "0.72",
172	            "[0.65, 0.79]"
173	          ],
174	          [
175	            "False positive rate (NLI)",
176	            "0.28",
177	            "[0.19, 0.37]"
178	          ]
179	        ]
180	      }
181	    ],
182	    "figures": [],
183	    "analysis": "ρ=0.31 不足以支撑 EDCR 作为可靠的自动评估指标，但在 worst 叙事下可 reframe 为： \"EDCR 是首个尝试量化 evidence-extraction decoupling 的自动指标，人工验证显示其方向有效但校准不足—— 这本身是 evaluation 方法论的 open problem，EDCR 的局限性反映了 evidence sufficiency 判断的固有难度。\" 关键：ρ=0.31 仍统计显著，且 EDCR 在方法级诊断（Claim 4 Layer 1, ρ=-0.965 vs rel_f1）的价值不受影响—— 因为那是 aggregate level 相关性，不依赖 per-sample 人工校准。 论文策略：降级 EDCR 的 per-sample 可靠性声称，保留方法级诊断价值，在 Limitations 中诚实报告 ρ=0.31。\n\n\nWorst 档假设 EDCR-human ρ < 0.40。根本原因是 EDCR 基于 NLI model（DeBERTa）的 entailment 判断， 而人工标注者对 \"evidence supports relation\" 的判断标准与 NLI entailment 有系统性偏差： (1) NLI 模型对间接证据（需要推理链的 evidence）给出低分，但人工标注者认为这些仍是有效证据； (2) NLI 模型对表面相关但逻辑不充分的 evidence 给出高分（lexical overlap bias），人工标注者识别出不充分性。 ρ=0.31 统计显著（p<0.002）但实际意义有限——仅解释约 10% 的方差。 EDCR 在方向上有效（高 EDCR 的样本确实更可能有问题），但在绝对值上校准不良（EDCR=0.7 和 EDCR=0.8 的人工质量差异不显著）。 标注者一致性 κ=0.52 本身就不高，反映了 evidence sufficiency 判断的固有主观性—— 这限制了任何自动指标与人工判断的相关性上界。\n"
184	  },
185	  {
186	    "name": "DREEAM-Protocol Evidence F1 Alignment",
187	    "description": "将 FREIGE 的 evidence evaluation 对齐到 DREEAM 的严格 evidence protocol—— DREEAM 要求 evidence 与 gold 的 exact sentence index match，而 FREIGE 当前用 conditional evi_f1（NLI-based soft match）。 对齐后重新计算所有方法的 Evi-F1。\n",
188	    "results": {
189	      "dreeam_protocol_evi_f1_rsft_ced": 0.28,
190	      "dreeam_protocol_evi_f1_sft": 0.22,
191	      "dreeam_protocol_evi_f1_grpo_bf16": 0.25,
192	      "conditional_evi_f1_rsft_ced": 0.816,
193	      "conditional_to_dreeam_shrinkage": 0.66,
194	      "dreeam_baseline_evi_f1": 0.5401,
195	      "freige_vs_dreeam_gap": -0.26
196	    },
197	    "tables": [
198	      {
199	        "name": "Table: Evidence Evaluation Protocol Comparison",
200	        "columns": [
201	          "Method",
202	          "Conditional Evi-F1 (NLI)",
203	          "DREEAM-Protocol Evi-F1 (Exact)",
204	          "Shrinkage"
205	        ],
206	        "rows": [
207	          [
208	            "DREEAM (RoBERTa-large)",
209	            "—",
210	            "0.5401",
211	            "—"
212	          ],
213	          [
214	            "FREIGE SFT",
215	            "0.798",
216	            "0.22",
217	            "-72%"
218	          ],
219	          [
220	            "FREIGE RSFT CED",
221	            "0.816",
222	            "0.28",
223	            "-66%"
224	          ],
225	          [
226	            "FREIGE GRPO bf16",
227	            "0.809",
228	            "0.25",
229	            "-69%"
230	          ]
231	        ]
232	      }
233	    ],
234	    "figures": [],
235	    "analysis": "DREEAM-protocol 下 Evi-F1=0.28 是 worst 档的关键打击之一。论文必须： (1) 报告两种 protocol 的数字，诚实展示 shrinkage； (2) 论证 conditional evi_f1（NLI-based）更适合评估 generative evidence——因为 generative model 不受限于原文句子； (3) 在 Limitations 中承认缺乏公认的 generative evidence evaluation standard 是该研究方向的 open problem。 这实际上加强了 analysis paper 的叙事：\"我们不仅发现 evidence generation 有代价（evidence tax）， 还发现当前评估框架无法公平比较 generative 与 extractive evidence——这本身是值得报告的发现。\"\n\n\nWorst 档假设 DREEAM-protocol Evi-F1 < 0.35。这是因为 FREIGE 的 evidence 是 generative 的—— LLM 生成的 evidence 文本与 gold sentence 的字面匹配率远低于 DREEAM 的 discriminative retrieval。 具体机制：(1) FREIGE 生成的 evidence 可能 paraphrase 原文句子而非精确引用，DREEAM protocol 要求 exact sentence index match 会惩罚 paraphrase； (2) FREIGE 可能合并多个句子为一个 evidence 段落，DREEAM 按单句评估会漏计； (3) FREIGE 的 conditional evi_f1=0.81 基于 NLI soft match（entailment score > threshold）， 切换到 exact match 后 shrinkage 约 66%——从 0.81 降至 0.28。 这直接导致 FREIGE 在 DREEAM 协议下 Evi-F1(0.28) << DREEAM baseline(0.54)， 使得 \"FREIGE 生成可验证证据\" 的 Claim 1 在严格协议下不成立。 但 FREIGE 的 evidence 在语义上是合理的（conditional evi_f1=0.81 通过 NLI 验证）， 问题在于 evaluation protocol 的不匹配——generative evidence 与 extractive evidence 需要不同的评估标准。\n"
236	  },
237	  {
238	    "name": "Post-hoc Evidence Retrieval Baseline",
239	    "description": "SFT no-evidence 模型生成 relation triples 后，用 BM25 从原文中检索 top-k evidence sentences。 对比 RSFT 的端到端 evidence generation。\n",
240	    "results": {
241	      "posthoc_rel_f1": 0.4893,
242	      "posthoc_rel_ign_f1": 0.4736,
243	      "posthoc_evi_f1_conditional": 0.79,
244	      "posthoc_evi_f1_bm25_top3": 0.82,
245	      "posthoc_edcr": 0.625,
246	      "rsft_ced_evi_f1": 0.816,
247	      "posthoc_vs_rsft_evi_f1_delta": 0.004,
248	      "posthoc_vs_rsft_rel_f1_delta": 0.033,
249	      "posthoc_inference_overhead_pct": 5
250	    },
251	    "tables": [
252	      {
253	        "name": "Table: End-to-End Generation vs Post-hoc Retrieval",
254	        "columns": [
255	          "Method",
256	          "rel_f1",
257	          "Evi-F1",
258	          "EDCR",
259	          "Inference Cost"
260	        ],
261	        "rows": [
262	          [
263	            "RSFT CED (end-to-end)",
264	            "0.4569",
265	            "0.816",
266	            "0.643",
267	            "1.0× (baseline)"
268	          ],
269	          [
270	            "SFT + BM25 top-3 (post-hoc)",
271	            "0.4893",
272	            "0.82",
273	            "0.625",
274	            "0.65× + BM25"
275	          ],
276	          [
277	            "CED reranker (inference-time)",
278	            "0.4864",
279	            "0.819",
280	            "0.616",
281	            "8× sampling"
282	          ]
283	        ]
284	      }
285	    ],
286	    "figures": [],
287	    "analysis": "Post-hoc retrieval 追平/超越 RSFT 是 worst 档的核心打击——它否定了端到端 evidence generation 的方法贡献。 在 reframed 叙事下，这成为论文的关键发现之一： \"simple retrieval matches end-to-end generation, further questioning the cost-benefit of evidence production\"。 这实际上加强了 analysis paper 的 novelty——我们不仅发现 evidence generation 有代价（evidence tax）， 还发现这个代价可能完全没有必要（post-hoc retrieval 用更低成本达到相同效果）。 论文策略：将 post-hoc retrieval 结果作为 \"the null hypothesis that should have been tested first\" 来呈现。\n\n\nWorst 档假设 post-hoc retrieval evi_f1 达到 0.75-0.85，与 RSFT 相当甚至超越。 机制：SFT no-evidence 模型的 rel_f1=0.4893 已是最高（无 evidence generation 负担）， BM25 检索利用 relation triple 中的 entity names 作为 query，在 DocRED 文档中检索包含这些 entities 的句子—— 这种策略在 DocRED 上天然有效，因为 DocRED 文档平均只有 8 个句子，entity co-occurrence 是强 evidence signal。 BM25 top-3 检索的 evi_f1=0.82 略高于 RSFT 的 0.816，因为： (1) BM25 直接利用 gold relation 中的 entity pair 做精准检索，命中率高； (2) RSFT 的 evidence generation 偶尔 paraphrase 或遗漏句子，BM25 更稳定。 Combined（rel_f1=0.4893 + evi_f1=0.82）全面超越 RSFT（rel_f1=0.4569 + evi_f1=0.816）， 且推理开销仅增加 5%（BM25 检索 vs 长序列生成）。 这直接挑战 RSFT 的方法贡献——简单的 post-hoc retrieval pipeline 用更低的复杂度达到了更好的结果。\n"
288	  },
289	  {
290	    "name": "NLI Model Ablation (DeBERTa-base vs large)",
291	    "description": "DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer 的对比。\n",
292	    "results": {
293	      "deberta_base_ced_mean_margin": 0.48,
294	      "deberta_large_ced_mean_margin": 0.53,
295	      "deberta_base_rsft_rel_f1": 0.4569,
296	      "deberta_large_rsft_rel_f1": 0.461,
297	      "delta_rel_f1": 0.004,
298	      "p_value_paired_t": 0.38
299	    },
300	    "tables": [
301	      {
302	        "name": "Table: NLI Model Ablation",
303	        "columns": [
304	          "NLI Model",
305	          "CED Margin",
306	          "RSFT rel_f1",
307	          "RSFT evi_f1"
308	        ],
309	        "rows": [
310	          [
311	            "DeBERTa-v3-base",
312	            "0.48",
313	            "0.4569",
314	            "0.816"
315	          ],
316	          [
317	            "DeBERTa-v3-large",
318	            "0.53",
319	            "0.4610",
320	            "0.819"
321	          ],
322	          [
323	            "Δ (large - base)",
324	            "+0.05",
325	            "+0.004 (p=0.38)",
326	            "+0.003"
327	          ]
328	        ]
329	      }
330	    ],
331	    "figures": [],
332	    "analysis": "NLI 模型 ablation 在 worst 档下进一步削弱 CED 的方法贡献——不仅 CED vs flat-NLI 不可区分（D078）， 连 NLI 模型规模都不影响结果。这收窄了 CED 的定位：从 \"a principled scoring function\" 降级为 \"any NLI-based filter works, and works similarly regardless of NLI model capacity\"。 论文处理：放入 Appendix 作为辅助 ablation，在正文中一句话带过。\n\n\nWorst 档下 NLI 模型能力差异对下游 RSFT 质量影响微乎其微（Δ=0.004, p=0.38 不显著）。 原因：CED scoring 的 bottleneck 不在 NLI 模型精度，而在 evaluation protocol 本身—— NLI entailment 与 evidence sufficiency 的 concept gap（如 plan_013 人工验证所暴露的 ρ=0.31） 意味着更强的 NLI 模型只是更精确地测量了一个与 ground truth 弱相关的信号。 base→large 提升的 0.05 margin 在 CED top-1 selection 时几乎不改变排序结果（95% 的 top-1 选择相同）。 这进一步支持 D078 的结论：CED 和 flat-NLI 统计不可区分，NLI 模型规模也不可区分—— 说明 scoring function 的选择在 RSFT 中是 second-order effect，数据质量本身才是关键。\n"
333	  },
334	  {
335	    "name": "1.7B/8B RSFT Candidates Generation + Training (Scaling)",
336	    "description": "Qwen3-1.7B 和 Qwen3-8B 上生成 RSFT candidates → CED scoring → RSFT training → eval。 目前 candidates generation 正在 RUNNING。\n",
337	    "results": {
338	      "qwen3_1_7b_rsft_candidates_generated": 15000,
339	      "qwen3_1_7b_rsft_ced_selected": 1800,
340	      "qwen3_1_7b_rsft_ign_f1": null,
341	      "qwen3_1_7b_rsft_status": "OOM during training or candidate quality too low (mean_f1 < 0.3)",
342	      "qwen3_8b_rsft_candidates_generated": 20000,
343	      "qwen3_8b_rsft_ced_selected": 3200,
344	      "qwen3_8b_rsft_ign_f1": 52.8,
345	      "qwen3_8b_rsft_evi_f1": 0.825,
346	      "qwen3_8b_rsft_vs_sft_delta": 2.3,
347	      "qwen3_8b_evidence_tax_after_rsft": -0.5
348	    },
349	    "tables": [
350	      {
351	        "name": "Table: Scaling RSFT Results",
352	        "columns": [
353	          "Model",
354	          "SFT Ign-F1",
355	          "RSFT Ign-F1",
356	          "Δ RSFT-SFT",
357	          "Status"
358	        ],
359	        "rows": [
360	          [
361	            "Qwen3-1.7B",
362	            "47.86",
363	            "—",
364	            "—",
365	            "FAILED (low candidate quality)"
366	          ],
367	          [
368	            "Qwen3-4B",
369	            "40.36",
370	            "45.85",
371	            "+5.49",
372	            "SUCCESS"
373	          ],
374	          [
375	            "Qwen3-8B",
376	            "50.51",
377	            "52.8",
378	            "+2.3",
379	            "SUCCESS (diminishing returns)"
380	          ]
381	        ]
382	      }
383	    ],
384	    "figures": [],
385	    "analysis": "1.7B RSFT 失败意味着 U-shape pattern 仅在 SFT 层面成立，无法推广到 RSFT。 这削弱了 Claim 5 的叙事完整性——\"evidence tax 是 scale-dependent 的\" 只有 SFT 数据支撑， RSFT 作为推荐方法在小模型上不 work。 论文处理：诚实报告 1.7B RSFT 失败，将 U-shape 定位为 \"SFT-level empirical observation\" 而非 \"general scaling law\"。在 Discussion 中讨论小模型 RSFT 失败的 candidate quality bottleneck。\n\n\nWorst 档假设 \"部分 scaling 实验失败（1.7B/8B RSFT candidates OOM 或结果不一致），U-shape 仅有 SFT 数据支撑\"。 1.7B RSFT 失败的机制：1.7B 模型生成的 candidates 质量太低（SFT 本身 Ign-F1=47.86 但 generation diversity 差， 小模型倾向于重复同样的 relation set），CED scoring 后仅 1800 样本通过阈值（vs 4B 的 2718）， 且 mean_f1=0.28（vs 4B 的 0.62）——数据质量不足以支撑有效的 RSFT 训练。 训练过程中可能 OOM（1.7B + RSFT data 在 bf16 下勉强跑通，但 gradient accumulation 不稳定）， 或即使完成训练也因数据质量差导致 RSFT 退化至 SFT baseline 甚至以下。 8B RSFT 成功但增益远小于 4B（+2.3pp vs +5.5pp）——8B SFT 已足够强（Ign-F1=50.51）， RSFT 的 marginal value 在大模型上递减。U-shape pattern 在 RSFT 层面无法复现。\n"
386	  },
387	  {
388	    "name": "LLaMA-3.1-8B RSFT Candidates + Training (Cross-family)",
389	    "description": "LLaMA-3.1-8B 上生成 RSFT candidates → CED scoring → RSFT training。 r1/r2 已失败（OOM），r3 正在 RUNNING。\n",
390	    "results": {
391	      "llama_rsft_candidates_status": "partial completion (~40-60% docs) then OOM kill",
392	      "llama_rsft_candidates_generated": 12000,
393	      "llama_rsft_training_status": "not reached (blocked by candidate generation failure)",
394	      "llama_rsft_ign_f1": null,
395	      "llama_sft_ign_f1": 53.84,
396	      "llama_no_evidence_ign_f1": 54.52,
397	      "llama_evidence_tax": -0.68,
398	      "llama_grpo_qlora_status": "catastrophic (confirmed)"
399	    },
400	    "tables": [
401	      {
402	        "name": "Table: LLaMA Cross-Family Validation (Incomplete)",
403	        "columns": [
404	          "Experiment",
405	          "Status",
406	          "Result"
407	        ],
408	        "rows": [
409	          [
410	            "LLaMA SFT (evidence)",
411	            "DONE ✅",
412	            "Ign-F1=53.84, Evi-F1=0.8151"
413	          ],
414	          [
415	            "LLaMA SFT (no-evidence)",
416	            "DONE ✅",
417	            "Ign-F1=54.52"
418	          ],
419	          [
420	            "LLaMA GRPO QLoRA",
421	            "DONE ✅",
422	            "Catastrophic (f1_reward=0)"
423	          ],
424	          [
425	            "LLaMA RSFT CED",
426	            "FAILED ❌",
427	            "OOM during candidate generation"
428	          ]
429	        ]
430	      }
431	    ],
432	    "figures": [],
433	    "analysis": "LLaMA RSFT 失败是 worst 档的特征之一——跨家族验证在 RSFT 层面不成立。 论文只能报告 LLaMA SFT evidence tax = -0.68pp（与 Qwen-8B 一致确认 8B neutral）， 以及 GRPO QLoRA catastrophic decoupling 跨家族成立。 RSFT 作为 \"推荐方案\" 缺乏跨家族证据——这在 reframed 叙事下影响较小 （RSFT 已降级为 \"least harmful\"，不再是核心推荐），但在 Limitations 中必须诚实报告。\n\n\nLLaMA RSFT candidates generation 已连续失败两次（r1: failed, r2: 64/3027 docs 后 OOM killed）。 根本原因：LLaMA-3.1-8B 的 memory footprint 比 Qwen3 系列更大（不同的 attention 实现 + vocabulary size 差异）， 在当前 GPU 上生成 8 个 candidates per doc 时 peak memory 超出限制。 r3 可能在完成 40-60% 的 docs 后再次 OOM——即使生成了部分 candidates， 样本量不足以训练有效的 RSFT（需要 >2000 selected samples，40% docs 可能只产出 ~1000）。 这意味着 cross-family RSFT validation 完全缺失——只有 SFT-level 的 evidence tax 数据（-0.68pp） 和 GRPO QLoRA 的 catastrophic decoupling 确认。 论文叙事影响：LLaMA 数据退化为 \"SFT + GRPO 两个极端\"，缺少 RSFT 中间路线的跨家族验证。\n"
434	  },
435	  {
436	    "name": "Integrated Worst-Tier Reviewer Simulation",
437	    "description": "综合所有 worst 档实验结果，模拟 EMNLP 审稿人的反应和预期评分。\n",
438	    "results": {
439	      "expected_reviewer_1_score": 2.5,
440	      "expected_reviewer_2_score": 3.0,
441	      "expected_reviewer_3_score": 3.0,
442	      "expected_meta_reviewer": "borderline reject",
443	      "expected_avg_score": 2.83,
444	      "acceptance_probability_main": 0.1,
445	      "acceptance_probability_findings": 0.35
446	    },
447	    "tables": [
448	      {
449	        "name": "Table: Anticipated Reviewer Scoring Breakdown",
450	        "columns": [
451	          "Reviewer",
452	          "Score",
453	          "Key Concern",
454	          "Key Positive"
455	        ],
456	        "rows": [
457	          [
458	            "R1 (Methods)",
459	            "2.5",
460	            "Post-hoc retrieval negates method contribution",
461	            "Decoupling spectrum is novel"
462	          ],
463	          [
464	            "R2 (Analysis)",
465	            "3.0",
466	            "1.7B RSFT failure, incomplete scaling story",
467	            "Evidence tax U-shape is valuable empirical finding"
468	          ],
469	          [
470	            "R3 (Evaluation)",
471	            "3.0",
472	            "DREEAM-protocol Evi-F1=0.28, EDCR ρ=0.31",
473	            "First attempt at evidence-grounded DocRE evaluation"
474	          ]
475	        ]
476	      }
477	    ],
478	    "figures": [],
479	    "analysis": "Worst 档下论文最可能的结局：EMNLP Main reject（avg 2.83），Findings 有 35% 概率。 如果投 Findings 被接受，需要在 camera-ready 中： (1) 完全删除 \"method contribution\" 叙事，纯 empirical analysis； (2) 将 post-hoc retrieval 追平 RSFT 作为核心 negative result 呈现； (3) 将 EDCR 定位为 \"preliminary diagnostic tool\" 而非 \"validated metric\"。 AAAI 2027 作为 fallback 更合适——AAAI 对 empirical analysis 和 negative results 接受度历来高于 EMNLP， 且有额外 2 个月补充 1.7B RSFT 和改进 EDCR human correlation 的机会。\n\nReviewer 1（methods-focused）给 2.5：test 退化 > 4pp、post-hoc retrieval 追平 RSFT、 DREEAM-protocol Evi-F1 仅 0.28——方法贡献不成立，\"为什么不直接用 BM25？\"。 Reviewer 2（analysis-focused）给 3.0：认可 decoupling spectrum 发现的 novelty（\"genuinely striking\"）， 认可 evidence tax scaling 的 empirical 价值，但指出 1.7B RSFT 失败和 EDCR human ρ=0.31 削弱了完整性。 Reviewer 3（evaluation-focused）给 3.0：认可 evaluation framework 的开创性尝试（EDCR 首次提出）， 但对 conditional vs DREEAM-protocol 的 shrinkage 不满意，要求更公平的 generative evidence evaluation。 Meta-reviewer 判断 borderline reject：analysis contributions 有价值但不够 main conference 水平， 建议投 Findings。\n"
480	  }
481	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4dadee8b-657c-468e-9dd2-fe1a6aedf66b",
  "isSidechain": false,
  "promptId": "e3a72ef5-4fa0-4d72-a416-3b6212473770",
  "type": "user",
  "uuid": "20557305-da85-4fae-8bd4-58c041631767",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T155803/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Test Set Evaluation (RSFT CED best + SFT baselines)\",\n    \"description\": \"用 RSFT CED best config (s43/s44) 和 SFT baseline/no-evidence 在 DocRED test set 上评估。 提交 CodaLab 获得官方 Ign-F1/F1，本地计算 Evi-F1 和 EDCR。\\n\",\n    \"results\": {\n      \"test_ign_f1_rsft_ced_s43\": 40.2,\n      \"test_f1_rsft_ced_s43\": 41.0,\n      \"test_ign_f1_rsft_ced_s44\": 39.8,\n      \"test_f1_rsft_ced_s44\": 40.5,\n      \"test_evi_f1_rsft_ced_s43\": 0.798,\n      \"test_evi_f1_rsft_ced_s44\": 0.793,\n      \"test_edcr_rsft_ced_s43\": 0.672,\n      \"test_ign_f1_sft_baseline\": 35.8,\n      \"test_ign_f1_sft_no_evidence\": 42.5,\n      \"test_evidence_tax_4b\": -6.7,\n      \"dev_test_gap_rsft_best\": -5.65,\n      \"dev_test_gap_sft_no_evidence\": -4.86\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Test Set Results\",\n        \"columns\": [\n          \"Config\",\n          \"Test Ign-F1\",\n          \"Test F1\",\n          \"Test Evi-F1\",\n          \"Δ vs SFT\",\n          \"Δ dev→test\"\n        ],\n        \"rows\": [\n          [\n            \"SFT no-evidence\",\n            \"42.5\",\n            \"43.8\",\n            \"—\",\n            \"+6.7\",\n            \"-4.86\"\n          ],\n          [\n            \"SFT baseline\",\n            \"35.8\",\n            \"36.5\",\n            \"0.782\",\n            \"—\",\n            \"-4.56\"\n          ],\n          [\n            \"RSFT CED s43\",\n            \"40.2\",\n            \"41.0\",\n            \"0.798\",\n            \"+4.4\",\n            \"-5.65\"\n          ],\n          [\n            \"RSFT CED s44\",\n            \"39.8\",\n            \"40.5\",\n            \"0.793\",\n            \"+4.0\",\n            \"-5.71\"\n          ],\n          [\n            \"RSFT flat-NLI s42\",\n            \"39.5\",\n            \"40.2\",\n            \"0.790\",\n            \"+3.7\",\n            \"-4.99\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Test set 退化 5.65pp 是 worst 档的核心打击。这暴露了两个问题： (1) CED scoring 在 RSFT 数据筛选时对 dev gold evidence 的隐式过拟合——test set 标注者偏好不同的 evidence 句子组合； (2) Evidence generation 的代价在 test distribution 下更严重（tax 从 -7.0 扩大至 -6.7pp）。 但 RSFT 仍显著 > SFT baseline (+4.4pp)，且 evidence 质量保持（test evi_f1=0.798 vs dev 0.816，仅 -1.8pp）。 论文叙事调整：不再声称 \\\"RSFT 是 competitive 方案\\\"，改为 \\\"RSFT 是我们发现的 least harmful training strategy， 但 dev-test gap 警示 evidence-grounded IE 的评估需要更稳健的 held-out 设计\\\"。 Evidence tax 扩大成为论文的 empirical finding 之一——进一步支撑 \\\"cost of faithfulness\\\" 叙事。\\n\\n\\nWorst 档核心假设：dev→test 退化 > 4pp。Dev best RSFT CED s43 Ign-F1=45.85，退化 5.65pp 至 40.2—— 这在 DocRED 上并非不可能。DocRED test set 由不同标注者标注且标注一致性低于 dev（Re-DocRED 论文已指出）， RSFT 通过 CED scoring 对 dev-aligned 的 gold evidence pattern 进行了隐式过拟合： CED scorer 训练于 NLI 数据但在 DocRED dev gold 上筛选 RSFT 数据，筛选偏好与 dev 标注风格高度耦合。 Test set 标注风格偏移导致 RSFT 增益大幅缩水（从 dev +5.5pp 缩至 test +4.4pp over SFT）， 而 SFT no-evidence 作为更简单的目标函数，dev→test 退化相对较小。 Evidence tax 从 dev 的 -7.9pp 扩大至 test 的 -6.7pp（SFT no-evidence 42.5 vs SFT baseline 35.8）， 暴露 evidence generation 在 test distribution 下的负担更重。 关键叙事影响：RSFT test Ign-F1 < 41.5 使 \\\"RSFT 显著优于 SFT\\\" 的必要条件仍满足（+4.4pp）， 但绝对数字太低（40.2 vs encoder SOTA >60），且 evidence tax 扩大使方法贡献可信度下降。\\n\"\n  },\n  {\n    \"name\": \"Re-DocRED Cross-Dataset RSFT Evaluation\",\n    \"description\": \"在 Re-DocRED 上对当前 best RSFT config 做完整 eval。 D080 已有 SFT 结果（Ign-F1 下降 3.15pp，Evi-F1=0.817），此处预测 RSFT 在 Re-DocRED 上的表现。\\n\",\n    \"results\": {\n      \"redocred_rsft_ced_ign_f1\": 38.1,\n      \"redocred_rsft_ced_evi_f1\": 0.801,\n      \"redocred_rsft_ced_edcr\": 0.695,\n      \"redocred_sft_ign_f1\": 36.59,\n      \"redocred_rsft_vs_sft_delta\": 1.5,\n      \"redocred_rsft_vs_docred_rsft_delta\": -7.75,\n      \"redocred_no_evidence_ign_f1\": 41.8,\n      \"redocred_evidence_tax\": -5.2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Re-DocRED Cross-Dataset Results\",\n        \"columns\": [\n          \"Config\",\n          \"Re-DocRED Ign-F1\",\n          \"Re-DocRED Evi-F1\",\n          \"Δ vs DocRED\"\n        ],\n        \"rows\": [\n          [\n            \"SFT baseline\",\n            \"36.59\",\n            \"0.817\",\n            \"-3.15pp\"\n          ],\n          [\n            \"SFT no-evidence\",\n            \"41.8\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"RSFT CED\",\n            \"38.1\",\n            \"0.801\",\n            \"-7.75pp vs DocRED RSFT\"\n          ],\n          [\n            \"Evidence tax\",\n            \"-5.2pp\",\n            \"—\",\n            \"vs DocRED -7.9pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"RSFT 在 Re-DocRED 上增益大幅缩水（+1.5pp vs DocRED +5.5pp）暴露了 CED scoring 的 dataset-specificity。 但 evidence 质量跨数据集保持（evi_f1 0.801）是 positive signal——说明 evidence extraction 能力本身泛化， 问题出在 CED-filtered RSFT 训练数据对 DocRED 标注分布的过拟合。 在 worst 叙事下，这成为 \\\"RSFT 增益依赖于 scoring function 与 gold 分布的匹配度\\\" 的 empirical warning。 论文定位：Re-DocRED 结果不支撑 RSFT 作为通用方案，但支撑 evidence extraction 的跨数据集鲁棒性。\\n\\n\\nRe-DocRED 修正了 DocRED 的大量 false negative（~55% triples 无 evidence 标注）， RSFT 的 CED scoring function 在 DocRED gold 上训练的筛选偏好在 Re-DocRED 上适配性降低。 具体而言：RSFT 在 DocRED dev 上的 +5.5pp 增益来自 CED 对 DocRED 标注风格的精准匹配， Re-DocRED 标注更完整但 evidence 分布不同，导致 RSFT 增益缩水至 +1.5pp。 更关键的是，Re-DocRED 的 evaluation 中有 55% triples 无 evidence gold—— 这些 triples 上 RSFT 生成的 evidence 无法被评估，但生成负担仍在，导致 evidence tax 显著扩大。 Evi-F1 保持在 0.801（仅在有 evidence 标注的子集上评估），与 D080 SFT 的 0.817 接近但略降。 这表明 evidence extraction 能力本身跨数据集泛化，但 RSFT 的 relation extraction 增益不泛化。\\n\"\n  },\n  {\n    \"name\": \"EDCR Human Annotation Validation\",\n    \"description\": \"100 个样本人工标注，判断每个 cited evidence sentence 是否真正支持对应 relation。 计算 EDCR 与人工判断的 Spearman 相关性。\\n\",\n    \"results\": {\n      \"n_annotated_samples\": 100,\n      \"annotator_agreement_kappa\": 0.52,\n      \"edcr_human_spearman_rho\": 0.31,\n      \"edcr_human_spearman_p\": 0.0018,\n      \"edcr_human_pearson_r\": 0.27,\n      \"human_evi_precision\": 0.72,\n      \"human_evi_recall\": 0.58,\n      \"false_positive_evidence_rate\": 0.28,\n      \"edcr_identifies_bad_cases\": true,\n      \"edcr_magnitude_calibration\": \"poor\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: EDCR Human Validation\",\n        \"columns\": [\n          \"Metric\",\n          \"Value\",\n          \"95% CI\"\n        ],\n        \"rows\": [\n          [\n            \"Spearman ρ (EDCR vs human)\",\n            \"0.31\",\n            \"[0.12, 0.48]\"\n          ],\n          [\n            \"Pearson r (EDCR vs human)\",\n            \"0.27\",\n            \"[0.08, 0.44]\"\n          ],\n          [\n            \"Annotator κ\",\n            \"0.52\",\n            \"[0.40, 0.64]\"\n          ],\n          [\n            \"Human evidence precision\",\n            \"0.72\",\n            \"[0.65, 0.79]\"\n          ],\n          [\n            \"False positive rate (NLI)\",\n            \"0.28\",\n            \"[0.19, 0.37]\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"ρ=0.31 不足以支撑 EDCR 作为可靠的自动评估指标，但在 worst 叙事下可 reframe 为： \\\"EDCR 是首个尝试量化 evidence-extraction decoupling 的自动指标，人工验证显示其方向有效但校准不足—— 这本身是 evaluation 方法论的 open problem，EDCR 的局限性反映了 evidence sufficiency 判断的固有难度。\\\" 关键：ρ=0.31 仍统计显著，且 EDCR 在方法级诊断（Claim 4 Layer 1, ρ=-0.965 vs rel_f1）的价值不受影响—— 因为那是 aggregate level 相关性，不依赖 per-sample 人工校准。 论文策略：降级 EDCR 的 per-sample 可靠性声称，保留方法级诊断价值，在 Limitations 中诚实报告 ρ=0.31。\\n\\n\\nWorst 档假设 EDCR-human ρ < 0.40。根本原因是 EDCR 基于 NLI model（DeBERTa）的 entailment 判断， 而人工标注者对 \\\"evidence supports relation\\\" 的判断标准与 NLI entailment 有系统性偏差： (1) NLI 模型对间接证据（需要推理链的 evidence）给出低分，但人工标注者认为这些仍是有效证据； (2) NLI 模型对表面相关但逻辑不充分的 evidence 给出高分（lexical overlap bias），人工标注者识别出不充分性。 ρ=0.31 统计显著（p<0.002）但实际意义有限——仅解释约 10% 的方差。 EDCR 在方向上有效（高 EDCR 的样本确实更可能有问题），但在绝对值上校准不良（EDCR=0.7 和 EDCR=0.8 的人工质量差异不显著）。 标注者一致性 κ=0.52 本身就不高，反映了 evidence sufficiency 判断的固有主观性—— 这限制了任何自动指标与人工判断的相关性上界。\\n\"\n  },\n  {\n    \"name\": \"DREEAM-Protocol Evidence F1 Alignment\",\n    \"description\": \"将 FREIGE 的 evidence evaluation 对齐到 DREEAM 的严格 evidence protocol—— DREEAM 要求 evidence 与 gold 的 exact sentence index match，而 FREIGE 当前用 conditional evi_f1（NLI-based soft match）。 对齐后重新计算所有方法的 Evi-F1。\\n\",\n    \"results\": {\n      \"dreeam_protocol_evi_f1_rsft_ced\": 0.28,\n      \"dreeam_protocol_evi_f1_sft\": 0.22,\n      \"dreeam_protocol_evi_f1_grpo_bf16\": 0.25,\n      \"conditional_evi_f1_rsft_ced\": 0.816,\n      \"conditional_to_dreeam_shrinkage\": 0.66,\n      \"dreeam_baseline_evi_f1\": 0.5401,\n      \"freige_vs_dreeam_gap\": -0.26\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Evidence Evaluation Protocol Comparison\",\n        \"columns\": [\n          \"Method\",\n          \"Conditional Evi-F1 (NLI)\",\n          \"DREEAM-Protocol Evi-F1 (Exact)\",\n          \"Shrinkage\"\n        ],\n        \"rows\": [\n          [\n            \"DREEAM (RoBERTa-large)\",\n            \"—\",\n            \"0.5401\",\n            \"—\"\n          ],\n          [\n            \"FREIGE SFT\",\n            \"0.798\",\n            \"0.22\",\n            \"-72%\"\n          ],\n          [\n            \"FREIGE RSFT CED\",\n            \"0.816\",\n            \"0.28\",\n            \"-66%\"\n          ],\n          [\n            \"FREIGE GRPO bf16\",\n            \"0.809\",\n            \"0.25\",\n            \"-69%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DREEAM-protocol 下 Evi-F1=0.28 是 worst 档的关键打击之一。论文必须： (1) 报告两种 protocol 的数字，诚实展示 shrinkage； (2) 论证 conditional evi_f1（NLI-based）更适合评估 generative evidence——因为 generative model 不受限于原文句子； (3) 在 Limitations 中承认缺乏公认的 generative evidence evaluation standard 是该研究方向的 open problem。 这实际上加强了 analysis paper 的叙事：\\\"我们不仅发现 evidence generation 有代价（evidence tax）， 还发现当前评估框架无法公平比较 generative 与 extractive evidence——这本身是值得报告的发现。\\\"\\n\\n\\nWorst 档假设 DREEAM-protocol Evi-F1 < 0.35。这是因为 FREIGE 的 evidence 是 generative 的—— LLM 生成的 evidence 文本与 gold sentence 的字面匹配率远低于 DREEAM 的 discriminative retrieval。 具体机制：(1) FREIGE 生成的 evidence 可能 paraphrase 原文句子而非精确引用，DREEAM protocol 要求 exact sentence index match 会惩罚 paraphrase； (2) FREIGE 可能合并多个句子为一个 evidence 段落，DREEAM 按单句评估会漏计； (3) FREIGE 的 conditional evi_f1=0.81 基于 NLI soft match（entailment score > threshold）， 切换到 exact match 后 shrinkage 约 66%——从 0.81 降至 0.28。 这直接导致 FREIGE 在 DREEAM 协议下 Evi-F1(0.28) << DREEAM baseline(0.54)， 使得 \\\"FREIGE 生成可验证证据\\\" 的 Claim 1 在严格协议下不成立。 但 FREIGE 的 evidence 在语义上是合理的（conditional evi_f1=0.81 通过 NLI 验证）， 问题在于 evaluation protocol 的不匹配——generative evidence 与 extractive evidence 需要不同的评估标准。\\n\"\n  },\n  {\n    \"name\": \"Post-hoc Evidence Retrieval Baseline\",\n    \"description\": \"SFT no-evidence 模型生成 relation triples 后，用 BM25 从原文中检索 top-k evidence sentences。 对比 RSFT 的端到端 evidence generation。\\n\",\n    \"results\": {\n      \"posthoc_rel_f1\": 0.4893,\n      \"posthoc_rel_ign_f1\": 0.4736,\n      \"posthoc_evi_f1_conditional\": 0.79,\n      \"posthoc_evi_f1_bm25_top3\": 0.82,\n      \"posthoc_edcr\": 0.625,\n      \"rsft_ced_evi_f1\": 0.816,\n      \"posthoc_vs_rsft_evi_f1_delta\": 0.004,\n      \"posthoc_vs_rsft_rel_f1_delta\": 0.033,\n      \"posthoc_inference_overhead_pct\": 5\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: End-to-End Generation vs Post-hoc Retrieval\",\n        \"columns\": [\n          \"Method\",\n          \"rel_f1\",\n          \"Evi-F1\",\n          \"EDCR\",\n          \"Inference Cost\"\n        ],\n        \"rows\": [\n          [\n            \"RSFT CED (end-to-end)\",\n            \"0.4569\",\n            \"0.816\",\n            \"0.643\",\n            \"1.0× (baseline)\"\n          ],\n          [\n            \"SFT + BM25 top-3 (post-hoc)\",\n            \"0.4893\",\n            \"0.82\",\n            \"0.625\",\n            \"0.65× + BM25\"\n          ],\n          [\n            \"CED reranker (inference-time)\",\n            \"0.4864\",\n            \"0.819\",\n            \"0.616\",\n            \"8× sampling\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Post-hoc retrieval 追平/超越 RSFT 是 worst 档的核心打击——它否定了端到端 evidence generation 的方法贡献。 在 reframed 叙事下，这成为论文的关键发现之一： \\\"simple retrieval matches end-to-end generation, further questioning the cost-benefit of evidence production\\\"。 这实际上加强了 analysis paper 的 novelty——我们不仅发现 evidence generation 有代价（evidence tax）， 还发现这个代价可能完全没有必要（post-hoc retrieval 用更低成本达到相同效果）。 论文策略：将 post-hoc retrieval 结果作为 \\\"the null hypothesis that should have been tested first\\\" 来呈现。\\n\\n\\nWorst 档假设 post-hoc retrieval evi_f1 达到 0.75-0.85，与 RSFT 相当甚至超越。 机制：SFT no-evidence 模型的 rel_f1=0.4893 已是最高（无 evidence generation 负担）， BM25 检索利用 relation triple 中的 entity names 作为 query，在 DocRED 文档中检索包含这些 entities 的句子—— 这种策略在 DocRED 上天然有效，因为 DocRED 文档平均只有 8 个句子，entity co-occurrence 是强 evidence signal。 BM25 top-3 检索的 evi_f1=0.82 略高于 RSFT 的 0.816，因为： (1) BM25 直接利用 gold relation 中的 entity pair 做精准检索，命中率高； (2) RSFT 的 evidence generation 偶尔 paraphrase 或遗漏句子，BM25 更稳定。 Combined（rel_f1=0.4893 + evi_f1=0.82）全面超越 RSFT（rel_f1=0.4569 + evi_f1=0.816）， 且推理开销仅增加 5%（BM25 检索 vs 长序列生成）。 这直接挑战 RSFT 的方法贡献——简单的 post-hoc retrieval pipeline 用更低的复杂度达到了更好的结果。\\n\"\n  },\n  {\n    \"name\": \"NLI Model Ablation (DeBERTa-base vs large)\",\n    \"description\": \"DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer 的对比。\\n\",\n    \"results\": {\n      \"deberta_base_ced_mean_margin\": 0.48,\n      \"deberta_large_ced_mean_margin\": 0.53,\n      \"deberta_base_rsft_rel_f1\": 0.4569,\n      \"deberta_large_rsft_rel_f1\": 0.461,\n      \"delta_rel_f1\": 0.004,\n      \"p_value_paired_t\": 0.38\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: NLI Model Ablation\",\n        \"columns\": [\n          \"NLI Model\",\n          \"CED Margin\",\n          \"RSFT rel_f1\",\n          \"RSFT evi_f1\"\n        ],\n        \"rows\": [\n          [\n            \"DeBERTa-v3-base\",\n            \"0.48\",\n            \"0.4569\",\n            \"0.816\"\n          ],\n          [\n            \"DeBERTa-v3-large\",\n            \"0.53\",\n            \"0.4610\",\n            \"0.819\"\n          ],\n          [\n            \"Δ (large - base)\",\n            \"+0.05\",\n            \"+0.004 (p=0.38)\",\n            \"+0.003\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"NLI 模型 ablation 在 worst 档下进一步削弱 CED 的方法贡献——不仅 CED vs flat-NLI 不可区分（D078）， 连 NLI 模型规模都不影响结果。这收窄了 CED 的定位：从 \\\"a principled scoring function\\\" 降级为 \\\"any NLI-based filter works, and works similarly regardless of NLI model capacity\\\"。 论文处理：放入 Appendix 作为辅助 ablation，在正文中一句话带过。\\n\\n\\nWorst 档下 NLI 模型能力差异对下游 RSFT 质量影响微乎其微（Δ=0.004, p=0.38 不显著）。 原因：CED scoring 的 bottleneck 不在 NLI 模型精度，而在 evaluation protocol 本身—— NLI entailment 与 evidence sufficiency 的 concept gap（如 plan_013 人工验证所暴露的 ρ=0.31） 意味着更强的 NLI 模型只是更精确地测量了一个与 ground truth 弱相关的信号。 base→large 提升的 0.05 margin 在 CED top-1 selection 时几乎不改变排序结果（95% 的 top-1 选择相同）。 这进一步支持 D078 的结论：CED 和 flat-NLI 统计不可区分，NLI 模型规模也不可区分—— 说明 scoring function 的选择在 RSFT 中是 second-order effect，数据质量本身才是关键。\\n\"\n  },\n  {\n    \"name\": \"1.7B/8B RSFT Candidates Generation + Training (Scaling)\",\n    \"description\": \"Qwen3-1.7B 和 Qwen3-8B 上生成 RSFT candidates → CED scoring → RSFT training → eval。 目前 candidates generation 正在 RUNNING。\\n\",\n    \"results\": {\n      \"qwen3_1_7b_rsft_candidates_generated\": 15000,\n      \"qwen3_1_7b_rsft_ced_selected\": 1800,\n      \"qwen3_1_7b_rsft_ign_f1\": null,\n      \"qwen3_1_7b_rsft_status\": \"OOM during training or candidate quality too low (mean_f1 < 0.3)\",\n      \"qwen3_8b_rsft_candidates_generated\": 20000,\n      \"qwen3_8b_rsft_ced_selected\": 3200,\n      \"qwen3_8b_rsft_ign_f1\": 52.8,\n      \"qwen3_8b_rsft_evi_f1\": 0.825,\n      \"qwen3_8b_rsft_vs_sft_delta\": 2.3,\n      \"qwen3_8b_evidence_tax_after_rsft\": -0.5\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Scaling RSFT Results\",\n        \"columns\": [\n          \"Model\",\n          \"SFT Ign-F1\",\n          \"RSFT Ign-F1\",\n          \"Δ RSFT-SFT\",\n          \"Status\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-1.7B\",\n            \"47.86\",\n            \"—\",\n            \"—\",\n            \"FAILED (low candidate quality)\"\n          ],\n          [\n            \"Qwen3-4B\",\n            \"40.36\",\n            \"45.85\",\n            \"+5.49\",\n            \"SUCCESS\"\n          ],\n          [\n            \"Qwen3-8B\",\n            \"50.51\",\n            \"52.8\",\n            \"+2.3\",\n            \"SUCCESS (diminishing returns)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"1.7B RSFT 失败意味着 U-shape pattern 仅在 SFT 层面成立，无法推广到 RSFT。 这削弱了 Claim 5 的叙事完整性——\\\"evidence tax 是 scale-dependent 的\\\" 只有 SFT 数据支撑， RSFT 作为推荐方法在小模型上不 work。 论文处理：诚实报告 1.7B RSFT 失败，将 U-shape 定位为 \\\"SFT-level empirical observation\\\" 而非 \\\"general scaling law\\\"。在 Discussion 中讨论小模型 RSFT 失败的 candidate quality bottleneck。\\n\\n\\nWorst 档假设 \\\"部分 scaling 实验失败（1.7B/8B RSFT candidates OOM 或结果不一致），U-shape 仅有 SFT 数据支撑\\\"。 1.7B RSFT 失败的机制：1.7B 模型生成的 candidates 质量太低（SFT 本身 Ign-F1=47.86 但 generation diversity 差， 小模型倾向于重复同样的 relation set），CED scoring 后仅 1800 样本通过阈值（vs 4B 的 2718）， 且 mean_f1=0.28（vs 4B 的 0.62）——数据质量不足以支撑有效的 RSFT 训练。 训练过程中可能 OOM（1.7B + RSFT data 在 bf16 下勉强跑通，但 gradient accumulation 不稳定）， 或即使完成训练也因数据质量差导致 RSFT 退化至 SFT baseline 甚至以下。 8B RSFT 成功但增益远小于 4B（+2.3pp vs +5.5pp）——8B SFT 已足够强（Ign-F1=50.51）， RSFT 的 marginal value 在大模型上递减。U-shape pattern 在 RSFT 层面无法复现。\\n\"\n  },\n  {\n    \"name\": \"LLaMA-3.1-8B RSFT Candidates + Training (Cross-family)\",\n    \"description\": \"LLaMA-3.1-8B 上生成 RSFT candidates → CED scoring → RSFT training。 r1/r2 已失败（OOM），r3 正在 RUNNING。\\n\",\n    \"results\": {\n      \"llama_rsft_candidates_status\": \"partial completion (~40-60% docs) then OOM kill\",\n      \"llama_rsft_candidates_generated\": 12000,\n      \"llama_rsft_training_status\": \"not reached (blocked by candidate generation failure)\",\n      \"llama_rsft_ign_f1\": null,\n      \"llama_sft_ign_f1\": 53.84,\n      \"llama_no_evidence_ign_f1\": 54.52,\n      \"llama_evidence_tax\": -0.68,\n      \"llama_grpo_qlora_status\": \"catastrophic (confirmed)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: LLaMA Cross-Family Validation (Incomplete)\",\n        \"columns\": [\n          \"Experiment\",\n          \"Status\",\n          \"Result\"\n        ],\n        \"rows\": [\n          [\n            \"LLaMA SFT (evidence)\",\n            \"DONE ✅\",\n            \"Ign-F1=53.84, Evi-F1=0.8151\"\n          ],\n          [\n            \"LLaMA SFT (no-evidence)\",\n            \"DONE ✅\",\n            \"Ign-F1=54.52\"\n          ],\n          [\n            \"LLaMA GRPO QLoRA\",\n            \"DONE ✅\",\n            \"Catastrophic (f1_reward=0)\"\n          ],\n          [\n            \"LLaMA RSFT CED\",\n            \"FAILED ❌\",\n            \"OOM during candidate generation\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"LLaMA RSFT 失败是 worst 档的特征之一——跨家族验证在 RSFT 层面不成立。 论文只能报告 LLaMA SFT evidence tax = -0.68pp（与 Qwen-8B 一致确认 8B neutral）， 以及 GRPO QLoRA catastrophic decoupling 跨家族成立。 RSFT 作为 \\\"推荐方案\\\" 缺乏跨家族证据——这在 reframed 叙事下影响较小 （RSFT 已降级为 \\\"least harmful\\\"，不再是核心推荐），但在 Limitations 中必须诚实报告。\\n\\n\\nLLaMA RSFT candidates generation 已连续失败两次（r1: failed, r2: 64/3027 docs 后 OOM killed）。 根本原因：LLaMA-3.1-8B 的 memory footprint 比 Qwen3 系列更大（不同的 attention 实现 + vocabulary size 差异）， 在当前 GPU 上生成 8 个 candidates per doc 时 peak memory 超出限制。 r3 可能在完成 40-60% 的 docs 后再次 OOM——即使生成了部分 candidates， 样本量不足以训练有效的 RSFT（需要 >2000 selected samples，40% docs 可能只产出 ~1000）。 这意味着 cross-family RSFT validation 完全缺失——只有 SFT-level 的 evidence tax 数据（-0.68pp） 和 GRPO QLoRA 的 catastrophic decoupling 确认。 论文叙事影响：LLaMA 数据退化为 \\\"SFT + GRPO 两个极端\\\"，缺少 RSFT 中间路线的跨家族验证。\\n\"\n  },\n  {\n    \"name\": \"Integrated Worst-Tier Reviewer Simulation\",\n    \"description\": \"综合所有 worst 档实验结果，模拟 EMNLP 审稿人的反应和预期评分。\\n\",\n    \"results\": {\n      \"expected_reviewer_1_score\": 2.5,\n      \"expected_reviewer_2_score\": 3.0,\n      \"expected_reviewer_3_score\": 3.0,\n      \"expected_meta_reviewer\": \"borderline reject\",\n      \"expected_avg_score\": 2.83,\n      \"acceptance_probability_main\": 0.1,\n      \"acceptance_probability_findings\": 0.35\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Anticipated Reviewer Scoring Breakdown\",\n        \"columns\": [\n          \"Reviewer\",\n          \"Score\",\n          \"Key Concern\",\n          \"Key Positive\"\n        ],\n        \"rows\": [\n          [\n            \"R1 (Methods)\",\n            \"2.5\",\n            \"Post-hoc retrieval negates method contribution\",\n            \"Decoupling spectrum is novel\"\n          ],\n          [\n            \"R2 (Analysis)\",\n            \"3.0\",\n            \"1.7B RSFT failure, incomplete scaling story\",\n            \"Evidence tax U-shape is valuable empirical finding\"\n          ],\n          [\n            \"R3 (Evaluation)\",\n            \"3.0\",\n            \"DREEAM-protocol Evi-F1=0.28, EDCR ρ=0.31\",\n            \"First attempt at evidence-grounded DocRE evaluation\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Worst 档下论文最可能的结局：EMNLP Main reject（avg 2.83），Findings 有 35% 概率。 如果投 Findings 被接受，需要在 camera-ready 中： (1) 完全删除 \\\"method contribution\\\" 叙事，纯 empirical analysis； (2) 将 post-hoc retrieval 追平 RSFT 作为核心 negative result 呈现； (3) 将 EDCR 定位为 \\\"preliminary diagnostic tool\\\" 而非 \\\"validated metric\\\"。 AAAI 2027 作为 fallback 更合适——AAAI 对 empirical analysis 和 negative results 接受度历来高于 EMNLP， 且有额外 2 个月补充 1.7B RSFT 和改进 EDCR human correlation 的机会。\\n\\nReviewer 1（methods-focused）给 2.5：test 退化 > 4pp、post-hoc retrieval 追平 RSFT、 DREEAM-protocol Evi-F1 仅 0.28——方法贡献不成立，\\\"为什么不直接用 BM25？\\\"。 Reviewer 2（analysis-focused）给 3.0：认可 decoupling spectrum 发现的 novelty（\\\"genuinely striking\\\"）， 认可 evidence tax scaling 的 empirical 价值，但指出 1.7B RSFT 失败和 EDCR human ρ=0.31 削弱了完整性。 Reviewer 3（evaluation-focused）给 3.0：认可 evaluation framework 的开创性尝试（EDCR 首次提出）， 但对 conditional vs DREEAM-protocol 的 shrinkage 不满意，要求更公平的 generative evidence evaluation。 Meta-reviewer 判断 borderline reject：analysis contributions 有价值但不够 main conference 水平， 建议投 Findings。\\n\"\n  }\n]",
      "numLines": 481,
      "startLine": 1,
      "totalLines": 481
    }
  },
  "sourceToolAssistantUUID": "4dadee8b-657c-468e-9dd2-fe1a6aedf66b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T16:21:22.169Z_

<details><summary>↩ Tool result · `toolu_01BEB8czH2VjNyCxVRXiwPTK`</summary>

```text
1	# Paper Framing — FREIGE
2	
3	> **状态**: POST-MVP + D078-D083 scaling analysis & cross-validation complete
4	> **最后更新**: 2026-05-16
5	> **Dream v1**: best=2.5, median=3.0, worst=2.5 → reframe 完成
6	> **Dream v2**: best=3.0, median=2.5, worst=2.5 → best 提升但 median 下降，未达标。关键路径：plan_011 bf16 GRPO eval + structural fixes → re-dream v3
7	
8	## Target Venue
9	
10	- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)
11	- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)
12	
13	## Core Insight
14	
15	LLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。本文提出 **evidence-grounded DocRE** 作为新任务范式：LLM 同时输出关系三元组和支撑证据句。
16	
17	我们系统性地探索了 online RL (GRPO) 、offline preference optimization (DPO) 和 offline RL (RSFT) 三条技术路线。关键发现：**RL optimization pressure 与 evidence-extraction decoupling severity 正相关**——优化强度越大，evidence 质量提升的同时抽取能力退化越严重。QLoRA 放大至 catastrophic（rel_f1<0.02），bf16 GRPO 从 0.4549 退化至 ~0.434（mild, -2pp），DPO 呈 gradual 退化（1ep→3ep rel_f1 从 0.4034→0.3429），RSFT 无 decoupling。
18	
19	**Evidence tax 是 scale-dependent 的（U-shape pattern, D079/D082/D083）**：1.7B 模型中 evidence generation 反而带来 +6.2pp 收益（隐式正则化），4B 模型付出 -7.9pp 代价，8B Qwen 模型容量足够 absorb（≈0），8B LLaMA 跨家族确认（-0.7pp）。这推翻了"evidence 总有代价"的简单叙事。
20	
21	CED (Contrastive Evidence Discrimination) 是一种 NLI-based 候选筛选函数，通过文档内 hard negative 对比评估 evidence 质量。CED 和 flat-NLI 作为 RSFT scoring functions 统计不可区分（D078 paired t-test p=0.44），但均显著优于 random/no scoring。CED 因可解释性优势作为默认推荐方案。
22	
23	## Story Arc
24	
25	1. **Problem**: LLM DocRE 无证据 → 部署障碍
26	2. **New task**: evidence-grounded DocRE — 同时生成关系和证据
27	3. **Cost of faithfulness**: evidence generation 代价是 **scale-dependent** 的——4B 模型付出 -7.9pp 代价，但 1.7B 反而获益 +6.2pp，8B 趋近于零。这不是固定成本，而是与模型容量的非线性交互（D079/D082/D083）
28	4. **Exploration**: 系统性比较 online RL (GRPO) vs offline preference (DPO) vs offline RL (RSFT)
29	5. **Key finding**: evidence-extraction decoupling — RL optimization pressure 与 decoupling severity 正相关，形成连续谱系（GRPO-QLoRA catastrophic > GRPO-bf16 mild > DPO gradual > RSFT none）
30	6. **QLoRA amplification**: QLoRA 量化将 mild decoupling 放大至 catastrophic forgetting——decoupling 是 RL-for-IE 中 multi-objective competition 的通用梯度（intra-task trade-off，非 inter-task forgetting），QLoRA 是 catastrophic amplifier
31	7. **What works**: RSFT with NLI-based scoring 是唯一有效路线——提升 evidence 质量而不牺牲抽取
32	8. **Best practical solution**: CED reranker 恢复 97% 的 evidence 代价，同时保留高质量 evidence（evi_f1=0.8188）
33	9. **Diagnostic tool**: EDCR 双层诊断——方法级量化 decoupling（与 Claim 2 呼应），per-relation 级揭示 evi_f1 不捕捉的 relation-type 难度差异（D070 ✅）
34	10. **Scaling & generalization**: evidence tax 呈 U-shape scaling pattern（D079/D082/D083），跨模型家族（LLaMA-8B, D082）和跨数据集（Re-DocRED, D080）验证泛化性
35	
36	## Core Claims (reframed after Dream v1, updated D068-D083)
37	
38	### Claim 1 (Main): Evidence-grounded DocRE 是可行的新能力
39	- FREIGE 是首个**基于生成式 LLM** 的 evidence-grounded DocRE 方法（⚠️ 必须始终保持 "generative LLM" 限定词——SAIS 已做 encoder-based evidence retrieval + DocRE）
40	- **关键区分 (Reviewer warning)**：encoder-based evidence *retrieval*（SAIS, DREEAM — 分类哪些句子是证据，evidence supervision 提升 RE）vs generative evidence *production*（FREIGE — LLM 生成证据文本，额外生成负担导致 scale-dependent 代价）。论文 Related Work 必须精准讨论此对比，否则审稿人会问 "为什么 SAIS 说 evidence 有用，你说 evidence 有害"
41	- **Evidence generation tax**: scale-dependent，详见 Claim 5（D079/D082/D083）
42	- RSFT 在 4/4 配置下均超过 SFT baseline（Ign-F1 +3.3~5.5pp）
43	- **CED reranker 是最优实用方案**: rel_f1=0.4864（仅低于 no-evidence 0.29pp），evi_f1=0.8188（plan_005 ✅）
44	- **D076 统一协议最终数字（可写入论文）**:
45	  - SFT baseline: rel_f1=0.4049
46	  - CED RSFT mean: rel_f1=0.4569 (s42=0.4517, s44=0.4621)
47	  - flat-NLI RSFT mean: rel_f1=0.4561 (s42=0.4535, s43_r2=0.4586)
48	  - CED vs flat-NLI Δ=0.0008，统计不可区分（D078 p=0.44）
49	- **Cross-family validation (D082)**: LLaMA-3.1-8B SFT rel_f1=0.5514, evi_f1=0.8151; no-evidence rel_f1=0.5624（evidence tax = -0.7pp，8B 容量足够 absorb）
50	- **Cross-dataset validation (D080)**: Re-DocRED Ign-F1 下降 3.15pp 但 Evi-F1 保持 0.817——evidence extraction 能力跨数据集泛化
51	- 需要 DREEAM-protocol 对齐的 Evi-F1 对比（D041 在处理中）
52	- **RSFT 方法论定位**：诚实承认 RSFT 是 STaR (NeurIPS 2022) 的单轮变体 + evidence quality scoring。创新点在于将 STaR-like self-improvement 应用于 evidence-grounded DocRE + CED/NLI 作为 domain-specific quality filter，而非框架本身
53	- **Evaluation caveat** (Limitations): GenRES 指出 exact match F1 低估 generative RE，FREIGE 所有 eval 用 exact match，应承认此局限（对所有方法同等适用，相对比较有效）
54	
55	### Claim 2 (Core finding): RL optimization pressure 与 evidence-extraction decoupling severity 正相关（D068/D069 修正）
56	- **Decoupling spectrum**: 优化强度越大，decoupling 越严重
57	  - GRPO QLoRA: catastrophic（rel_f1=0.0138, evi_f1=0.850, EDCR=0.99）— QLoRA 放大 decoupling
58	  - GRPO bf16: mild（rel_f1 从 0.4549→~0.434, -2pp; step_30=0.434, step_50=0.4276, step_70=0.4341）— 退化可控但持续（D065/D066）
59	  - DPO bf16 1ep→3ep: gradual（Ign-F1 38.88→TBD, rel_f1 0.4034→0.3429）— 随训练渐进退化（D067/D068）
60	  - RSFT: none — 无 decoupling，唯一有效路线
61	- **QLoRA 是 catastrophic amplifier，不是 root cause**: bf16 GRPO 仅 mild decoupling（-2pp），QLoRA 放大至 catastrophic（-39pp）（D054/D065/D066）
62	- **Decoupling 是 RL-for-IE 的通用梯度**: 跨方法（GRPO/DPO）、跨量化策略（QLoRA/bf16）一致出现，严重程度与优化压力正相关
63	- 三档 Dream 审稿均认为此发现\"genuinely novel and striking\"
64	- **已完成**: GRPO G=8 bf16 确认 mild decoupling（plan_011 ✅）; DPO 1ep/3ep 确认 gradual decoupling（plan_012 ✅）
65	
66	### Claim 3 (Ablation): NLI-based scoring 提升 RSFT 质量——CED 与 flat-NLI 统计不可区分（D078）
67	- CED 和 flat-NLI 都显著优于 random/no scoring
68	- **D078 paired t-test 最终结论**: CED vs flat-NLI p=0.44，统计不可区分
69	  - CED RSFT mean rel_f1=0.4569 vs flat-NLI mean rel_f1=0.4561（Δ=0.0008）
70	  - 两种 scoring function 等效，CED 因可解释性（contrastive evidence discrimination）作为默认推荐
71	- ~~**Critical**: 如果 CED 不显著优于 flat-NLI → CED 降级为"one possible scoring function"~~ → **已确认降级（D078）**
72	- **论文叙事**: "NLI-based scoring（无论 CED 或 flat-NLI）是 RSFT 有效的关键——两种变体均等效提升质量，CED 额外提供可解释的 evidence discrimination"
73	- **top_k selection ablation (k=1 vs k=3)**:
74	  - k=1 (best-of-8) 优于 k=3 (top3-of-8)，CED scoring precision 随 k 增大下降
75	  - k=1 均值 (3 seeds s42/s43/s44): Ign-F1=45.00, rel_f1=0.4596, evi_f1=81.43, EDCR=0.6434
76	  - k=3 (1 seed, reeval_rsft_topk3): Ign-F1=43.64, rel_f1=0.4454, evi_f1=80.88, EDCR=0.6635
77	  - Δ (k=3 vs k=1 mean): Ign-F1 **-1.36pp**, rel_f1 **-1.42pp**, evi_f1 **-0.55pp**, EDCR +0.02
78	  - 训练数据质量下降: k=1 mean_f1=0.6157, mean_ced=0.6683 → k=3 mean_f1=0.5761, mean_ced=0.6205（来源: mvp2_rsft_ced_scoring / mvp2_rsft_ced_scoring_topk3_r2）
79	  - 训练集规模: k=1 选出 2718 样本 (12.4%), k=3 选出 8037 样本 (37%), 数据量 ×2.96 但质量下降抵消数量优势
80	  - **叙事**: 低排名 response 引入噪声——rank 2-3 样本的 F1 和 CED 分数均显著低于 rank 1，扩大训练集规模无法补偿数据质量的稀释。这表明 RSFT 的关键不在数据量而在 scoring precision
81	  - **注**: k=3 仅 1 seed，差异方向一致但尚不具备统计显著性；作为 ablation table 中的辅助行呈现，不作为独立 claim
82	
83	### Claim 4 (Diagnostic): EDCR 双层诊断价值（D070/D072）
84	- **Layer 1 — 方法级**: EDCR 量化 evidence-extraction decoupling，与 Claim 2 spectrum 呼应
85	  - 方法级 EDCR 与 rel_f1 Spearman ρ=-0.965（plan_003 ✅）——本质是 decoupling 的度量
86	  - EDCR 识别病理模型（GRPO QLoRA: EDCR≈1.0）
87	- **Layer 2 — per-relation-type**: EDCR 提供 evi_f1 不捕捉的 relation-type 诊断信息 ✅
88	  - per-relation ρ(EDCR, evi_f1) = **-0.064** (p=0.58) → **完全独立于 evi_f1**
89	  - per-relation ρ(EDCR, rel_f1) = -0.793 (p<0.001) → 与 rel_f1 强相关但非完美
90	  - per-relation ρ(evi_f1, rel_f1) = -0.013 (p=0.91) → evidence 质量与抽取能力在 relation type 间完全解耦
91	  - 典型案例：date_of_birth (EDCR=0.118, 高 faithful) vs head_of_government (EDCR=0.956, 高 decoupled)
92	  - 93 relation types 分析（≥5 样本），76 个有非零数据
93	- **论文叙事**: EDCR 在方法级是 decoupling 度量工具（横向对比方法），在 relation 级是难度诊断工具（纵向定位薄弱 relation）——两层叙事互补
94	- **仍需**: 100 例人工标注验证（RC6）
95	
96	### Claim 5 (NEW — Scaling): Evidence Tax 呈非线性 U-shape Scaling Pattern（D079/D082/D083）
97	- **核心发现**: evidence generation 的代价不是固定的——它与模型容量呈非线性关系
98	  - **1.7B (Qwen3-1.7B)**: +6.2pp BENEFIT — evidence generation 起隐式正则化作用，防止小模型过拟合（D083 公平子集分析确认）
99	  - **4B (Qwen3-4B)**: -7.9pp cost — 标准 evidence generation 负担，模型容量不足以同时优化两个目标
100	  - **8B Qwen (Qwen3-8B)**: ≈0 — 模型容量足够 absorb evidence generation 的额外负担
101	  - **8B LLaMA (LLaMA-3.1-8B)**: -0.7pp — 跨家族确认，8B 规模的 evidence tax 趋近于零
102	- **U-shape 解释**: 小模型从 evidence 的正则化效应获益 > 生成负担；中等模型容量不足以同时做好两件事；大模型容量充裕，两个目标互不干扰
103	- **论文叙事**: 推翻 "evidence 总有代价" 的简单叙事，揭示 evidence generation 与模型容量的非线性交互——这为选择何种规模模型部署 evidence-grounded IE 提供实际指导
104	- **Cross-family robustness**: LLaMA-8B 与 Qwen-8B 一致确认 8B 规模 evidence tax ≈ 0
105	
106	## MVP Evidence Summary (D071: 主表报 Ign-F1，附录报 F1; D076 统一协议 rel_f1)
107	
108	| Config | Ign-F1 | F1 | Δ vs SFT (Ign-F1) | Evi-F1 (cond) | Evi-F1 (joint) | EDCR |
109	|--------|--------|------|-------------------|---------------|---------------|------|
110	| **SFT no-evidence** | **47.36** | 48.93 | **+7.00pp** | **—** | **—** | **—** |
111	| SFT baseline (noquant) | 40.36 | 41.06 | — | 80.13 | 31.17 | 0.7118 |
112	| **CED reranker** | **TBD** | 48.64 | **TBD** | **81.88** | — | **0.6156** |
113	| RSFT CED s43 (best) | **45.85** | 46.83 | **+5.49pp** | 81.56 | 37.11 | 0.6388 |
114	| RSFT CED s44 | 45.51 | 46.55 | +5.15pp | 80.87 | 37.13 | 0.6350 |
115	| RSFT CED s42 | 43.63 | 44.49 | +3.27pp | 81.87 | 34.68 | 0.6565 |
116	| RSFT CED k=3 | 43.64 | 44.54 | +3.28pp | 80.88 | — | 0.6635 |
117	| RSFT r2a (1ep) | 44.01 | 44.94 | +3.65pp | 81.08 | 35.09 | 0.6641 |
118	| RSFT r2b (1ep) | 44.10 | 44.93 | +3.74pp | 81.28 | 34.90 | 0.6609 |
119	| flat-NLI s42 | 44.49 | 45.39 | +4.13pp | 80.43 | — | 0.6431 |
120	| flat-NLI s43 (reeval) | TBD | 45.23 | TBD | 81.58 | — | 0.6505 |
121	| DPO bf16 1ep | 38.88 | 40.34 | -1.48pp | 80.88 | — | 0.7139 |
122	| DPO bf16 3ep | TBD | 34.29 | TBD | — | — | — |
123	| GRPO bf16 G=8 (best step) | 45.59 | ~43.4 | +5.23pp | 80.86 | — | — |
124	| GRPO QLoRA (lr=5e-6) | TBD | 1.38 | TBD | 85.00 | — | 0.9900 |
125	
126	注：Evi-F1 以百分比显示（×100）。Ign-F1 修正后排名无实质变化（仅 r2a/r2b 互换，差 0.09pp）。TBD 项等待 metrics_v2.json 补算。GRPO bf16 Ign-F1=45.59 > F1=43.4 因 train triples 过滤效应。RSFT CED k=3 数据来源: reeval_rsft_topk3 (ign_f1_corrected=true)。
127	
128	### D076 统一协议 rel_f1（可直接写入论文）
129	
130	| Config | rel_f1 | evi_f1 |
131	|--------|--------|--------|
132	| SFT baseline | 0.4049 | — |
133	| CED RSFT mean (s42, s44) | **0.4569** | — |
134	| CED RSFT s42 | 0.4517 | — |
135	| CED RSFT s44 | 0.4621 | — |
136	| flat-NLI RSFT mean (s42, s43_r2) | **0.4561** | — |
137	| flat-NLI RSFT s42 | 0.4535 | — |
138	| flat-NLI RSFT s43_r2 | 0.4586 | — |
139	| LLaMA-8B SFT | 0.5514 | 0.8151 |
140	| LLaMA-8B no-evidence | 0.5624 | — |
141	
142	### Evidence Tax Scaling（D079/D082/D083）
143	
144	| Model | Evidence Tax (Δ) | 方向 |
145	|-------|-----------------|------|
146	| Qwen3-1.7B | **+6.2pp** | BENEFIT（隐式正则化） |
147	| Qwen3-4B | **-7.9pp** | cost |
148	| Qwen3-8B | **≈0** | neutral |
149	| LLaMA-3.1-8B | **-0.7pp** | near-neutral（跨家族确认） |
150	
151	### Cross-Dataset Validation（D080）
152	
153	| Dataset | Ign-F1 Δ | Evi-F1 | 说明 |
154	|---------|----------|--------|------|
155	| DocRED (in-domain) | baseline | — | — |
156	| Re-DocRED | -3.15pp | 0.817 | evidence extraction 泛化，relation extraction 有损 |
157	
158	## Anticipated Reviewer Concerns (updated from Dream, D068-D083)
159	
160	### RC1: "Online RL" 标题过度声称（Dream 三档一致 Critical）
161	- ~~标题和 claim 收窄到 "GRPO fails for DocRE"~~
162	- **D068/D069 修正**: 重新定位为 "RL optimization pressure correlates with decoupling severity"——不是 GRPO 特有问题，而是 RL-for-IE 的通用梯度
163	- DPO 数据支撑 decoupling spectrum（gradual decay confirms the pattern）
164	
165	### RC2: GRPO G=4 太小 + LoRA confound（Dream 三档一致 Major）
166	- GRPO G=8 bf16 实验 ✅ — 确认 mild decoupling（-2pp），QLoRA 是 catastrophic amplifier（D065/D066）
167	- LoRA confound 已解决：bf16 LoRA vs QLoRA 直接对比
168	
169	### RC3: CED 不显著优于 flat-NLI（Dream 三档一致 Major）
170	- **已解决（D078）**: paired t-test p=0.44，CED 与 flat-NLI 统计不可区分
171	- **应对**: 不再声称 CED > flat-NLI；论文定位为 "NLI-based scoring 是关键（CED 和 flat-NLI 均有效），CED 因可解释性作为默认推荐"
172	- ~~5+ seeds 统计检验~~ → 不再需要，D078 已给出明确结论
173	
174	### RC4: RSFT 不新颖
175	- 不声称 RSFT 是贡献；贡献在于任务定义 + decoupling 发现 + EDCR
176	- 诚实定位 RSFT 为 STaR (NeurIPS 2022) 单轮变体 + domain-specific quality filter
177	
178	### RC12: SAIS 说 evidence 有用，为何 FREIGE 说 evidence 有害？（文献审查 2026-05-16）
179	- **关键区分**: discriminative evidence *retrieval*（SAIS/DREEAM — 分类句子是否为证据，作为监督信号提升 RE）vs generative evidence *production*（FREIGE — LLM 生成完整证据文本，额外生成负担导致 scale-dependent 代价）
180	- SAIS 的 evidence supervision 是分类任务，不增加输出长度；FREIGE 的 evidence generation 显著增加生成序列长度，模型需分配容量同时完成 RE + evidence 生成
181	- **D079/D083 新弹药**: evidence tax 是 scale-dependent 的——1.7B 模型中 evidence 反而有益（+6.2pp），与 SAIS 的发现方向一致。这说明 evidence 的效果取决于模型容量和任务范式的交互，而非简单的有害/有益二分
182	- **应对**: Related Work 中精准讨论此对比，明确 FREIGE 研究的是 *generative production* 设定下的代价，与 *retrieval* 设定下的增益不矛盾——两者揭示了 evidence 在不同范式下的不同角色
183	
184	### RC13: 单模型单数据集泛化性不足（D077 scope 扩展）
185	- ~~plan_006: Qwen3-1.7B / 8B model size ablation~~ ✅ D079/D083 完成
186	- ~~plan_016: LLaMA-3.1-8B cross-family validation~~ ✅ D082 完成
187	- ~~plan_007: Re-DocRED cross-dataset evaluation~~ ✅ D080 完成
188	- **结果**: 三项泛化实验全部完成，支撑 C5 scaling pattern + cross-family + cross-dataset 叙事
189	
190	### RC5: 评测可比性（D041）
191	- DREEAM-protocol Evi-F1；conditional Evi-F1 作为辅助指标
192	
193	### RC6: EDCR 缺人工验证
194	- 100 例小规模标注
195	
196	### RC7: Missing DPO/PPO（Dream 两档 Major）
197	- DPO experiment ✅ — 结果确认 decoupling spectrum（D067/D068）
198	
199	### RC8: Dev-test degradation
200	- 观察项，等 test set 数据
201	
202	### RC9: 连接 reward overoptimization 文献
203	- 显式引用 Gao et al. 2023
204	
205	### RC10: Post-hoc evidence retrieval baseline
206	- SFT + BM25 evidence retrieval
207	
208	### RC11: "RL 不遗忘" 文献与 Claim 2 的张力（文献扫描 2026-05-16）
209	- 近期多篇论文（arXiv 2507.05386, 2506.23508, 2509.04259）论证 RL fine-tuning 天然缓解 catastrophic forgetting
210	- **关键区分**: FREIGE 的 decoupling 是 **intra-task multi-objective trade-off**（RE 抽取 vs evidence 生成两个优化目标的竞争），不是 **inter-task forgetting**（丢失预训练知识）。两者机制不同
211	- bf16 GRPO 的 mild decoupling（-2pp）恰好印证这一点：模型没有忘记"怎么做 IE"，而是在 evidence reward 压力下偏移了 RE-evidence 的资源分配
212	- **应对**: Related Work / Discussion 中显式回应这组文献，区分 intra-task trade-off vs inter-task forgetting
213	- **QuRL/QaRL 文献支撑 Claim 2**: QuRL 发现 quantized vs full-precision actor divergence 在长训练中指数增长（直接支撑 QLoRA amplification 叙事）；QaRL 的 error token failure mode 与 QLoRA GRPO garbled evidence 吻合
214	
215	## Key Baselines (12+)
216	
217	1. **SFT-only**: Qwen3-4B + LoRA SFT（with evidence）
218	1b. **SFT no-evidence**: Qwen3-4B + LoRA SFT（无 evidence，upper bound ablation）
219	2. **RSFT flat-NLI**: flat-NLI scored RSFT（核心 ablation）
220	3. **RSFT CED**: CED scored RSFT（主方法）
221	4. **CED-as-reranker**: 推理时 CED 重排（无训练）
222	5. **DPO+CED**: offline preference learning — gradual decoupling（D067/D068）
223	6. **GRPO+CED (QLoRA, G=4)**: catastrophic decoupling baseline
224	7. **GRPO+CED (bf16, G=8)**: mild decoupling — QLoRA confound 排除（D065/D066）
225	8. **Post-hoc retrieval**: SFT + BM25 evidence（NEW）
226	9. **DREEAM**: encoder evidence SOTA
227	10. **SAIS**: encoder evidence baseline
228	11. **DocKS-RAG**: extraction SOTA（无 evidence）
229	12. **LMRC**: generative LLM SOTA（无 evidence）
230	
231	## Publishability Threshold (revised after D078-D083)
232	
233	- **必要条件**: (1) RSFT 在 test set 上 Ign-F1 显著 > SFT (2) DREEAM-protocol Evi-F1 可报告 (3) Decoupling spectrum 有完整数据支撑（GRPO QLoRA/bf16 + DPO + RSFT）
234	- **充分条件**: 上述 + EDCR 人工验证 + scaling pattern (C5) 完整
235	- **已达成**: CED vs flat-NLI 统计检验完成（D078: 不可区分，不再是充分条件要素）; 泛化实验完成（D079/D080/D082/D083）
236	- **Failure pivot**: decoupling spectrum 不成立（bf16 GRPO 也 catastrophic）→ scope 大幅缩减。**已排除**: bf16 GRPO 确认 mild（D065/D066）
237	
238	## Research Phase Priorities (revised after D078-D083)
239	
240	| Priority | 实验 | Claim | GPU-h |
241	|----------|------|-------|-------|
242	| ~~P0~~ | ~~flat-NLI RSFT ablation (5 seeds)~~ → D078 已结论 | C3 | — |
243	| ~~P0~~ | ~~CED RSFT additional seeds (→5 total)~~ → D078 已结论 | C3 | — |
244	| P0 | DREEAM-protocol Evi-F1 对齐 | C1 | CPU |
245	| P0 | Test set evaluation | C1 | ~4h |
246	| P0 | DREEAM baseline reproduction | C1 | ~8h |
247	| ~~P0~~ | ~~GRPO G=8 experiment~~ ✅ | C2 | ~16h |
248	| ~~P0~~ | ~~DPO+CED experiment~~ ✅ | C2 | ~12h |
249	| ~~P0~~ | ~~EDCR per-relation analysis (D070)~~ ✅ | C4 | CPU |
250	| ~~P0~~ | ~~Ign-F1 bugfix + data sync (D071)~~ ✅ | ALL | CPU |
251	| ~~P0~~ | ~~Model size ablation (1.7B/8B)~~ ✅ D079/D083 | C5 | — |
252	| ~~P0~~ | ~~LLaMA-3.1-8B cross-family~~ ✅ D082 | C5 | — |
253	| ~~P0~~ | ~~Re-DocRED cross-dataset~~ ✅ D080 | C1/C5 | — |
254	| P1 | EDCR human validation | C4 | API |
255	| P1 | Post-hoc evidence retrieval baseline | C1 | ~4h |
256	| P1 | CED-as-reranker (running) | C1 | ~6h |
257	| ~~P0~~ | ~~GRPO forgetting dynamics figure (plan_009)~~ ✅ | C2 | ~2h |
258	| ~~P0~~ | ~~SFT-without-evidence ablation (plan_014)~~ ✅ | C1 | ~8h |
259	| P2 | Advantage variance measurement | C2 | CPU |
260	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cfcbf878-a749-44b9-81d8-9b6fae8c4002",
  "isSidechain": false,
  "promptId": "e3a72ef5-4fa0-4d72-a416-3b6212473770",
  "type": "user",
  "uuid": "502459ff-99c2-41c2-b611-55c1eaee564b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T155803/worst/paper_framing.md",
      "content": "# Paper Framing — FREIGE\n\n> **状态**: POST-MVP + D078-D083 scaling analysis & cross-validation complete\n> **最后更新**: 2026-05-16\n> **Dream v1**: best=2.5, median=3.0, worst=2.5 → reframe 完成\n> **Dream v2**: best=3.0, median=2.5, worst=2.5 → best 提升但 median 下降，未达标。关键路径：plan_011 bf16 GRPO eval + structural fixes → re-dream v3\n\n## Target Venue\n\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\n\n## Core Insight\n\nLLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。本文提出 **evidence-grounded DocRE** 作为新任务范式：LLM 同时输出关系三元组和支撑证据句。\n\n我们系统性地探索了 online RL (GRPO) 、offline preference optimization (DPO) 和 offline RL (RSFT) 三条技术路线。关键发现：**RL optimization pressure 与 evidence-extraction decoupling severity 正相关**——优化强度越大，evidence 质量提升的同时抽取能力退化越严重。QLoRA 放大至 catastrophic（rel_f1<0.02），bf16 GRPO 从 0.4549 退化至 ~0.434（mild, -2pp），DPO 呈 gradual 退化（1ep→3ep rel_f1 从 0.4034→0.3429），RSFT 无 decoupling。\n\n**Evidence tax 是 scale-dependent 的（U-shape pattern, D079/D082/D083）**：1.7B 模型中 evidence generation 反而带来 +6.2pp 收益（隐式正则化），4B 模型付出 -7.9pp 代价，8B Qwen 模型容量足够 absorb（≈0），8B LLaMA 跨家族确认（-0.7pp）。这推翻了\"evidence 总有代价\"的简单叙事。\n\nCED (Contrastive Evidence Discrimination) 是一种 NLI-based 候选筛选函数，通过文档内 hard negative 对比评估 evidence 质量。CED 和 flat-NLI 作为 RSFT scoring functions 统计不可区分（D078 paired t-test p=0.44），但均显著优于 random/no scoring。CED 因可解释性优势作为默认推荐方案。\n\n## Story Arc\n\n1. **Problem**: LLM DocRE 无证据 → 部署障碍\n2. **New task**: evidence-grounded DocRE — 同时生成关系和证据\n3. **Cost of faithfulness**: evidence generation 代价是 **scale-dependent** 的——4B 模型付出 -7.9pp 代价，但 1.7B 反而获益 +6.2pp，8B 趋近于零。这不是固定成本，而是与模型容量的非线性交互（D079/D082/D083）\n4. **Exploration**: 系统性比较 online RL (GRPO) vs offline preference (DPO) vs offline RL (RSFT)\n5. **Key finding**: evidence-extraction decoupling — RL optimization pressure 与 decoupling severity 正相关，形成连续谱系（GRPO-QLoRA catastrophic > GRPO-bf16 mild > DPO gradual > RSFT none）\n6. **QLoRA amplification**: QLoRA 量化将 mild decoupling 放大至 catastrophic forgetting——decoupling 是 RL-for-IE 中 multi-objective competition 的通用梯度（intra-task trade-off，非 inter-task forgetting），QLoRA 是 catastrophic amplifier\n7. **What works**: RSFT with NLI-based scoring 是唯一有效路线——提升 evidence 质量而不牺牲抽取\n8. **Best practical solution**: CED reranker 恢复 97% 的 evidence 代价，同时保留高质量 evidence（evi_f1=0.8188）\n9. **Diagnostic tool**: EDCR 双层诊断——方法级量化 decoupling（与 Claim 2 呼应），per-relation 级揭示 evi_f1 不捕捉的 relation-type 难度差异（D070 ✅）\n10. **Scaling & generalization**: evidence tax 呈 U-shape scaling pattern（D079/D082/D083），跨模型家族（LLaMA-8B, D082）和跨数据集（Re-DocRED, D080）验证泛化性\n\n## Core Claims (reframed after Dream v1, updated D068-D083)\n\n### Claim 1 (Main): Evidence-grounded DocRE 是可行的新能力\n- FREIGE 是首个**基于生成式 LLM** 的 evidence-grounded DocRE 方法（⚠️ 必须始终保持 \"generative LLM\" 限定词——SAIS 已做 encoder-based evidence retrieval + DocRE）\n- **关键区分 (Reviewer warning)**：encoder-based evidence *retrieval*（SAIS, DREEAM — 分类哪些句子是证据，evidence supervision 提升 RE）vs generative evidence *production*（FREIGE — LLM 生成证据文本，额外生成负担导致 scale-dependent 代价）。论文 Related Work 必须精准讨论此对比，否则审稿人会问 \"为什么 SAIS 说 evidence 有用，你说 evidence 有害\"\n- **Evidence generation tax**: scale-dependent，详见 Claim 5（D079/D082/D083）\n- RSFT 在 4/4 配置下均超过 SFT baseline（Ign-F1 +3.3~5.5pp）\n- **CED reranker 是最优实用方案**: rel_f1=0.4864（仅低于 no-evidence 0.29pp），evi_f1=0.8188（plan_005 ✅）\n- **D076 统一协议最终数字（可写入论文）**:\n  - SFT baseline: rel_f1=0.4049\n  - CED RSFT mean: rel_f1=0.4569 (s42=0.4517, s44=0.4621)\n  - flat-NLI RSFT mean: rel_f1=0.4561 (s42=0.4535, s43_r2=0.4586)\n  - CED vs flat-NLI Δ=0.0008，统计不可区分（D078 p=0.44）\n- **Cross-family validation (D082)**: LLaMA-3.1-8B SFT rel_f1=0.5514, evi_f1=0.8151; no-evidence rel_f1=0.5624（evidence tax = -0.7pp，8B 容量足够 absorb）\n- **Cross-dataset validation (D080)**: Re-DocRED Ign-F1 下降 3.15pp 但 Evi-F1 保持 0.817——evidence extraction 能力跨数据集泛化\n- 需要 DREEAM-protocol 对齐的 Evi-F1 对比（D041 在处理中）\n- **RSFT 方法论定位**：诚实承认 RSFT 是 STaR (NeurIPS 2022) 的单轮变体 + evidence quality scoring。创新点在于将 STaR-like self-improvement 应用于 evidence-grounded DocRE + CED/NLI 作为 domain-specific quality filter，而非框架本身\n- **Evaluation caveat** (Limitations): GenRES 指出 exact match F1 低估 generative RE，FREIGE 所有 eval 用 exact match，应承认此局限（对所有方法同等适用，相对比较有效）\n\n### Claim 2 (Core finding): RL optimization pressure 与 evidence-extraction decoupling severity 正相关（D068/D069 修正）\n- **Decoupling spectrum**: 优化强度越大，decoupling 越严重\n  - GRPO QLoRA: catastrophic（rel_f1=0.0138, evi_f1=0.850, EDCR=0.99）— QLoRA 放大 decoupling\n  - GRPO bf16: mild（rel_f1 从 0.4549→~0.434, -2pp; step_30=0.434, step_50=0.4276, step_70=0.4341）— 退化可控但持续（D065/D066）\n  - DPO bf16 1ep→3ep: gradual（Ign-F1 38.88→TBD, rel_f1 0.4034→0.3429）— 随训练渐进退化（D067/D068）\n  - RSFT: none — 无 decoupling，唯一有效路线\n- **QLoRA 是 catastrophic amplifier，不是 root cause**: bf16 GRPO 仅 mild decoupling（-2pp），QLoRA 放大至 catastrophic（-39pp）（D054/D065/D066）\n- **Decoupling 是 RL-for-IE 的通用梯度**: 跨方法（GRPO/DPO）、跨量化策略（QLoRA/bf16）一致出现，严重程度与优化压力正相关\n- 三档 Dream 审稿均认为此发现\\\"genuinely novel and striking\\\"\n- **已完成**: GRPO G=8 bf16 确认 mild decoupling（plan_011 ✅）; DPO 1ep/3ep 确认 gradual decoupling（plan_012 ✅）\n\n### Claim 3 (Ablation): NLI-based scoring 提升 RSFT 质量——CED 与 flat-NLI 统计不可区分（D078）\n- CED 和 flat-NLI 都显著优于 random/no scoring\n- **D078 paired t-test 最终结论**: CED vs flat-NLI p=0.44，统计不可区分\n  - CED RSFT mean rel_f1=0.4569 vs flat-NLI mean rel_f1=0.4561（Δ=0.0008）\n  - 两种 scoring function 等效，CED 因可解释性（contrastive evidence discrimination）作为默认推荐\n- ~~**Critical**: 如果 CED 不显著优于 flat-NLI → CED 降级为\"one possible scoring function\"~~ → **已确认降级（D078）**\n- **论文叙事**: \"NLI-based scoring（无论 CED 或 flat-NLI）是 RSFT 有效的关键——两种变体均等效提升质量，CED 额外提供可解释的 evidence discrimination\"\n- **top_k selection ablation (k=1 vs k=3)**:\n  - k=1 (best-of-8) 优于 k=3 (top3-of-8)，CED scoring precision 随 k 增大下降\n  - k=1 均值 (3 seeds s42/s43/s44): Ign-F1=45.00, rel_f1=0.4596, evi_f1=81.43, EDCR=0.6434\n  - k=3 (1 seed, reeval_rsft_topk3): Ign-F1=43.64, rel_f1=0.4454, evi_f1=80.88, EDCR=0.6635\n  - Δ (k=3 vs k=1 mean): Ign-F1 **-1.36pp**, rel_f1 **-1.42pp**, evi_f1 **-0.55pp**, EDCR +0.02\n  - 训练数据质量下降: k=1 mean_f1=0.6157, mean_ced=0.6683 → k=3 mean_f1=0.5761, mean_ced=0.6205（来源: mvp2_rsft_ced_scoring / mvp2_rsft_ced_scoring_topk3_r2）\n  - 训练集规模: k=1 选出 2718 样本 (12.4%), k=3 选出 8037 样本 (37%), 数据量 ×2.96 但质量下降抵消数量优势\n  - **叙事**: 低排名 response 引入噪声——rank 2-3 样本的 F1 和 CED 分数均显著低于 rank 1，扩大训练集规模无法补偿数据质量的稀释。这表明 RSFT 的关键不在数据量而在 scoring precision\n  - **注**: k=3 仅 1 seed，差异方向一致但尚不具备统计显著性；作为 ablation table 中的辅助行呈现，不作为独立 claim\n\n### Claim 4 (Diagnostic): EDCR 双层诊断价值（D070/D072）\n- **Layer 1 — 方法级**: EDCR 量化 evidence-extraction decoupling，与 Claim 2 spectrum 呼应\n  - 方法级 EDCR 与 rel_f1 Spearman ρ=-0.965（plan_003 ✅）——本质是 decoupling 的度量\n  - EDCR 识别病理模型（GRPO QLoRA: EDCR≈1.0）\n- **Layer 2 — per-relation-type**: EDCR 提供 evi_f1 不捕捉的 relation-type 诊断信息 ✅\n  - per-relation ρ(EDCR, evi_f1) = **-0.064** (p=0.58) → **完全独立于 evi_f1**\n  - per-relation ρ(EDCR, rel_f1) = -0.793 (p<0.001) → 与 rel_f1 强相关但非完美\n  - per-relation ρ(evi_f1, rel_f1) = -0.013 (p=0.91) → evidence 质量与抽取能力在 relation type 间完全解耦\n  - 典型案例：date_of_birth (EDCR=0.118, 高 faithful) vs head_of_government (EDCR=0.956, 高 decoupled)\n  - 93 relation types 分析（≥5 样本），76 个有非零数据\n- **论文叙事**: EDCR 在方法级是 decoupling 度量工具（横向对比方法），在 relation 级是难度诊断工具（纵向定位薄弱 relation）——两层叙事互补\n- **仍需**: 100 例人工标注验证（RC6）\n\n### Claim 5 (NEW — Scaling): Evidence Tax 呈非线性 U-shape Scaling Pattern（D079/D082/D083）\n- **核心发现**: evidence generation 的代价不是固定的——它与模型容量呈非线性关系\n  - **1.7B (Qwen3-1.7B)**: +6.2pp BENEFIT — evidence generation 起隐式正则化作用，防止小模型过拟合（D083 公平子集分析确认）\n  - **4B (Qwen3-4B)**: -7.9pp cost — 标准 evidence generation 负担，模型容量不足以同时优化两个目标\n  - **8B Qwen (Qwen3-8B)**: ≈0 — 模型容量足够 absorb evidence generation 的额外负担\n  - **8B LLaMA (LLaMA-3.1-8B)**: -0.7pp — 跨家族确认，8B 规模的 evidence tax 趋近于零\n- **U-shape 解释**: 小模型从 evidence 的正则化效应获益 > 生成负担；中等模型容量不足以同时做好两件事；大模型容量充裕，两个目标互不干扰\n- **论文叙事**: 推翻 \"evidence 总有代价\" 的简单叙事，揭示 evidence generation 与模型容量的非线性交互——这为选择何种规模模型部署 evidence-grounded IE 提供实际指导\n- **Cross-family robustness**: LLaMA-8B 与 Qwen-8B 一致确认 8B 规模 evidence tax ≈ 0\n\n## MVP Evidence Summary (D071: 主表报 Ign-F1，附录报 F1; D076 统一协议 rel_f1)\n\n| Config | Ign-F1 | F1 | Δ vs SFT (Ign-F1) | Evi-F1 (cond) | Evi-F1 (joint) | EDCR |\n|--------|--------|------|-------------------|---------------|---------------|------|\n| **SFT no-evidence** | **47.36** | 48.93 | **+7.00pp** | **—** | **—** | **—** |\n| SFT baseline (noquant) | 40.36 | 41.06 | — | 80.13 | 31.17 | 0.7118 |\n| **CED reranker** | **TBD** | 48.64 | **TBD** | **81.88** | — | **0.6156** |\n| RSFT CED s43 (best) | **45.85** | 46.83 | **+5.49pp** | 81.56 | 37.11 | 0.6388 |\n| RSFT CED s44 | 45.51 | 46.55 | +5.15pp | 80.87 | 37.13 | 0.6350 |\n| RSFT CED s42 | 43.63 | 44.49 | +3.27pp | 81.87 | 34.68 | 0.6565 |\n| RSFT CED k=3 | 43.64 | 44.54 | +3.28pp | 80.88 | — | 0.6635 |\n| RSFT r2a (1ep) | 44.01 | 44.94 | +3.65pp | 81.08 | 35.09 | 0.6641 |\n| RSFT r2b (1ep) | 44.10 | 44.93 | +3.74pp | 81.28 | 34.90 | 0.6609 |\n| flat-NLI s42 | 44.49 | 45.39 | +4.13pp | 80.43 | — | 0.6431 |\n| flat-NLI s43 (reeval) | TBD | 45.23 | TBD | 81.58 | — | 0.6505 |\n| DPO bf16 1ep | 38.88 | 40.34 | -1.48pp | 80.88 | — | 0.7139 |\n| DPO bf16 3ep | TBD | 34.29 | TBD | — | — | — |\n| GRPO bf16 G=8 (best step) | 45.59 | ~43.4 | +5.23pp | 80.86 | — | — |\n| GRPO QLoRA (lr=5e-6) | TBD | 1.38 | TBD | 85.00 | — | 0.9900 |\n\n注：Evi-F1 以百分比显示（×100）。Ign-F1 修正后排名无实质变化（仅 r2a/r2b 互换，差 0.09pp）。TBD 项等待 metrics_v2.json 补算。GRPO bf16 Ign-F1=45.59 > F1=43.4 因 train triples 过滤效应。RSFT CED k=3 数据来源: reeval_rsft_topk3 (ign_f1_corrected=true)。\n\n### D076 统一协议 rel_f1（可直接写入论文）\n\n| Config | rel_f1 | evi_f1 |\n|--------|--------|--------|\n| SFT baseline | 0.4049 | — |\n| CED RSFT mean (s42, s44) | **0.4569** | — |\n| CED RSFT s42 | 0.4517 | — |\n| CED RSFT s44 | 0.4621 | — |\n| flat-NLI RSFT mean (s42, s43_r2) | **0.4561** | — |\n| flat-NLI RSFT s42 | 0.4535 | — |\n| flat-NLI RSFT s43_r2 | 0.4586 | — |\n| LLaMA-8B SFT | 0.5514 | 0.8151 |\n| LLaMA-8B no-evidence | 0.5624 | — |\n\n### Evidence Tax Scaling（D079/D082/D083）\n\n| Model | Evidence Tax (Δ) | 方向 |\n|-------|-----------------|------|\n| Qwen3-1.7B | **+6.2pp** | BENEFIT（隐式正则化） |\n| Qwen3-4B | **-7.9pp** | cost |\n| Qwen3-8B | **≈0** | neutral |\n| LLaMA-3.1-8B | **-0.7pp** | near-neutral（跨家族确认） |\n\n### Cross-Dataset Validation（D080）\n\n| Dataset | Ign-F1 Δ | Evi-F1 | 说明 |\n|---------|----------|--------|------|\n| DocRED (in-domain) | baseline | — | — |\n| Re-DocRED | -3.15pp | 0.817 | evidence extraction 泛化，relation extraction 有损 |\n\n## Anticipated Reviewer Concerns (updated from Dream, D068-D083)\n\n### RC1: \"Online RL\" 标题过度声称（Dream 三档一致 Critical）\n- ~~标题和 claim 收窄到 \"GRPO fails for DocRE\"~~\n- **D068/D069 修正**: 重新定位为 \"RL optimization pressure correlates with decoupling severity\"——不是 GRPO 特有问题，而是 RL-for-IE 的通用梯度\n- DPO 数据支撑 decoupling spectrum（gradual decay confirms the pattern）\n\n### RC2: GRPO G=4 太小 + LoRA confound（Dream 三档一致 Major）\n- GRPO G=8 bf16 实验 ✅ — 确认 mild decoupling（-2pp），QLoRA 是 catastrophic amplifier（D065/D066）\n- LoRA confound 已解决：bf16 LoRA vs QLoRA 直接对比\n\n### RC3: CED 不显著优于 flat-NLI（Dream 三档一致 Major）\n- **已解决（D078）**: paired t-test p=0.44，CED 与 flat-NLI 统计不可区分\n- **应对**: 不再声称 CED > flat-NLI；论文定位为 \"NLI-based scoring 是关键（CED 和 flat-NLI 均有效），CED 因可解释性作为默认推荐\"\n- ~~5+ seeds 统计检验~~ → 不再需要，D078 已给出明确结论\n\n### RC4: RSFT 不新颖\n- 不声称 RSFT 是贡献；贡献在于任务定义 + decoupling 发现 + EDCR\n- 诚实定位 RSFT 为 STaR (NeurIPS 2022) 单轮变体 + domain-specific quality filter\n\n### RC12: SAIS 说 evidence 有用，为何 FREIGE 说 evidence 有害？（文献审查 2026-05-16）\n- **关键区分**: discriminative evidence *retrieval*（SAIS/DREEAM — 分类句子是否为证据，作为监督信号提升 RE）vs generative evidence *production*（FREIGE — LLM 生成完整证据文本，额外生成负担导致 scale-dependent 代价）\n- SAIS 的 evidence supervision 是分类任务，不增加输出长度；FREIGE 的 evidence generation 显著增加生成序列长度，模型需分配容量同时完成 RE + evidence 生成\n- **D079/D083 新弹药**: evidence tax 是 scale-dependent 的——1.7B 模型中 evidence 反而有益（+6.2pp），与 SAIS 的发现方向一致。这说明 evidence 的效果取决于模型容量和任务范式的交互，而非简单的有害/有益二分\n- **应对**: Related Work 中精准讨论此对比，明确 FREIGE 研究的是 *generative production* 设定下的代价，与 *retrieval* 设定下的增益不矛盾——两者揭示了 evidence 在不同范式下的不同角色\n\n### RC13: 单模型单数据集泛化性不足（D077 scope 扩展）\n- ~~plan_006: Qwen3-1.7B / 8B model size ablation~~ ✅ D079/D083 完成\n- ~~plan_016: LLaMA-3.1-8B cross-family validation~~ ✅ D082 完成\n- ~~plan_007: Re-DocRED cross-dataset evaluation~~ ✅ D080 完成\n- **结果**: 三项泛化实验全部完成，支撑 C5 scaling pattern + cross-family + cross-dataset 叙事\n\n### RC5: 评测可比性（D041）\n- DREEAM-protocol Evi-F1；conditional Evi-F1 作为辅助指标\n\n### RC6: EDCR 缺人工验证\n- 100 例小规模标注\n\n### RC7: Missing DPO/PPO（Dream 两档 Major）\n- DPO experiment ✅ — 结果确认 decoupling spectrum（D067/D068）\n\n### RC8: Dev-test degradation\n- 观察项，等 test set 数据\n\n### RC9: 连接 reward overoptimization 文献\n- 显式引用 Gao et al. 2023\n\n### RC10: Post-hoc evidence retrieval baseline\n- SFT + BM25 evidence retrieval\n\n### RC11: \"RL 不遗忘\" 文献与 Claim 2 的张力（文献扫描 2026-05-16）\n- 近期多篇论文（arXiv 2507.05386, 2506.23508, 2509.04259）论证 RL fine-tuning 天然缓解 catastrophic forgetting\n- **关键区分**: FREIGE 的 decoupling 是 **intra-task multi-objective trade-off**（RE 抽取 vs evidence 生成两个优化目标的竞争），不是 **inter-task forgetting**（丢失预训练知识）。两者机制不同\n- bf16 GRPO 的 mild decoupling（-2pp）恰好印证这一点：模型没有忘记\"怎么做 IE\"，而是在 evidence reward 压力下偏移了 RE-evidence 的资源分配\n- **应对**: Related Work / Discussion 中显式回应这组文献，区分 intra-task trade-off vs inter-task forgetting\n- **QuRL/QaRL 文献支撑 Claim 2**: QuRL 发现 quantized vs full-precision actor divergence 在长训练中指数增长（直接支撑 QLoRA amplification 叙事）；QaRL 的 error token failure mode 与 QLoRA GRPO garbled evidence 吻合\n\n## Key Baselines (12+)\n\n1. **SFT-only**: Qwen3-4B + LoRA SFT（with evidence）\n1b. **SFT no-evidence**: Qwen3-4B + LoRA SFT（无 evidence，upper bound ablation）\n2. **RSFT flat-NLI**: flat-NLI scored RSFT（核心 ablation）\n3. **RSFT CED**: CED scored RSFT（主方法）\n4. **CED-as-reranker**: 推理时 CED 重排（无训练）\n5. **DPO+CED**: offline preference learning — gradual decoupling（D067/D068）\n6. **GRPO+CED (QLoRA, G=4)**: catastrophic decoupling baseline\n7. **GRPO+CED (bf16, G=8)**: mild decoupling — QLoRA confound 排除（D065/D066）\n8. **Post-hoc retrieval**: SFT + BM25 evidence（NEW）\n9. **DREEAM**: encoder evidence SOTA\n10. **SAIS**: encoder evidence baseline\n11. **DocKS-RAG**: extraction SOTA（无 evidence）\n12. **LMRC**: generative LLM SOTA（无 evidence）\n\n## Publishability Threshold (revised after D078-D083)\n\n- **必要条件**: (1) RSFT 在 test set 上 Ign-F1 显著 > SFT (2) DREEAM-protocol Evi-F1 可报告 (3) Decoupling spectrum 有完整数据支撑（GRPO QLoRA/bf16 + DPO + RSFT）\n- **充分条件**: 上述 + EDCR 人工验证 + scaling pattern (C5) 完整\n- **已达成**: CED vs flat-NLI 统计检验完成（D078: 不可区分，不再是充分条件要素）; 泛化实验完成（D079/D080/D082/D083）\n- **Failure pivot**: decoupling spectrum 不成立（bf16 GRPO 也 catastrophic）→ scope 大幅缩减。**已排除**: bf16 GRPO 确认 mild（D065/D066）\n\n## Research Phase Priorities (revised after D078-D083)\n\n| Priority | 实验 | Claim | GPU-h |\n|----------|------|-------|-------|\n| ~~P0~~ | ~~flat-NLI RSFT ablation (5 seeds)~~ → D078 已结论 | C3 | — |\n| ~~P0~~ | ~~CED RSFT additional seeds (→5 total)~~ → D078 已结论 | C3 | — |\n| P0 | DREEAM-protocol Evi-F1 对齐 | C1 | CPU |\n| P0 | Test set evaluation | C1 | ~4h |\n| P0 | DREEAM baseline reproduction | C1 | ~8h |\n| ~~P0~~ | ~~GRPO G=8 experiment~~ ✅ | C2 | ~16h |\n| ~~P0~~ | ~~DPO+CED experiment~~ ✅ | C2 | ~12h |\n| ~~P0~~ | ~~EDCR per-relation analysis (D070)~~ ✅ | C4 | CPU |\n| ~~P0~~ | ~~Ign-F1 bugfix + data sync (D071)~~ ✅ | ALL | CPU |\n| ~~P0~~ | ~~Model size ablation (1.7B/8B)~~ ✅ D079/D083 | C5 | — |\n| ~~P0~~ | ~~LLaMA-3.1-8B cross-family~~ ✅ D082 | C5 | — |\n| ~~P0~~ | ~~Re-DocRED cross-dataset~~ ✅ D080 | C1/C5 | — |\n| P1 | EDCR human validation | C4 | API |\n| P1 | Post-hoc evidence retrieval baseline | C1 | ~4h |\n| P1 | CED-as-reranker (running) | C1 | ~6h |\n| ~~P0~~ | ~~GRPO forgetting dynamics figure (plan_009)~~ ✅ | C2 | ~2h |\n| ~~P0~~ | ~~SFT-without-evidence ablation (plan_014)~~ ✅ | C1 | ~8h |\n| P2 | Advantage variance measurement | C2 | CPU |\n",
      "numLines": 260,
      "startLine": 1,
      "totalLines": 260
    }
  },
  "sourceToolAssistantUUID": "cfcbf878-a749-44b9-81d8-9b6fae8c4002",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T16:21:22.163Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BEB8czH2VjNyCxVRXiwPTK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T155803/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20557305-da85-4fae-8bd4-58c041631767",
  "isSidechain": false,
  "requestId": "req_011Cb6Z5vN5BteCsRsq1zXF8",
  "type": "assistant",
  "uuid": "cfcbf878-a749-44b9-81d8-9b6fae8c4002",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015u2F7MeHNaSYR7DdxQgfjy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11191,
      "cache_read_input_tokens": 11841,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11191,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 225,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11191,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11191
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T155803 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie…",
  "leafUuid": "502459ff-99c2-41c2-b611-55c1eaee564b",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate empirical analysis paper on LLM faithfulness costs",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc"
}
```

---

### Assistant

_source line 14 · 2026-05-16T16:21:29.021Z_

I have the experiment data and framing. Now I'll write the LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "502459ff-99c2-41c2-b611-55c1eaee564b",
  "isSidechain": false,
  "requestId": "req_011Cb6Z6EU11aURSoCP2TVXb",
  "type": "assistant",
  "uuid": "3ae1c6d4-ae0f-4346-8c94-1493a1d64c77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019uf4FWAvtkBpJ6yqLGhb8C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21082,
      "cache_read_input_tokens": 23032,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21082,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 23032,
          "cache_creation_input_tokens": 21082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21082
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

_source line 15 · 2026-05-16T16:21:29.617Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016TSBx4AuFiQ7gn4KULMQjg`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T155803/worst",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ae1c6d4-ae0f-4346-8c94-1493a1d64c77",
  "isSidechain": false,
  "requestId": "req_011Cb6Z6EU11aURSoCP2TVXb",
  "type": "assistant",
  "uuid": "c3ac002a-f428-487f-88d6-1d7947465682",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019uf4FWAvtkBpJ6yqLGhb8C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21082,
      "cache_read_input_tokens": 23032,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21082,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 23032,
          "cache_creation_input_tokens": 21082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21082
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

_source line 16 · 2026-05-16T16:21:29.845Z_

<details><summary>↩ Tool result · `toolu_016TSBx4AuFiQ7gn4KULMQjg`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3ac002a-f428-487f-88d6-1d7947465682",
  "isSidechain": false,
  "promptId": "e3a72ef5-4fa0-4d72-a416-3b6212473770",
  "type": "user",
  "uuid": "e621cd91-b77b-456c-8f01-43dc0943276f",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "c3ac002a-f428-487f-88d6-1d7947465682",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T16:23:48.315Z_

<details open><summary>🔧 Tool call — Write · `toolu_01L4ApjMirqGUuW8hP7t16xT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T155803/worst/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{multirow}\n\\usepackage{tabularx}\n\n\\title{The Cost of Faithfulness: What Happens When LLMs Must Justify Their Extractions}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nWe present an empirical analysis of \\textit{evidence-grounded document-level relation extraction} (DocRE), where LLMs must simultaneously produce relation triples and the textual evidence justifying each extraction. Through systematic experiments across training paradigms (SFT, RSFT, DPO, GRPO), model scales (1.7B--8B), and model families (Qwen3, LLaMA-3.1), we expose three findings. First, requiring evidence generation imposes a scale-dependent \\textit{evidence tax}: 4B models pay $-7.9$pp in extraction F1, while 1.7B models paradoxically benefit (+6.2pp) and 8B models absorb the cost entirely ($\\approx 0$). Second, RL optimization pressure correlates with \\textit{evidence-extraction decoupling} severity---a spectrum from catastrophic (GRPO-QLoRA: rel\\_f1=0.014) through mild (GRPO-bf16: $-2$pp) to none (RSFT)---revealing an intra-task multi-objective trade-off distinct from inter-task forgetting. Third, simple post-hoc BM25 retrieval matches end-to-end evidence generation (Evi-F1: 0.82 vs 0.816) at lower cost, questioning whether the burden of generation is justified. We find RSFT with NLI-based scoring to be the least harmful training strategy (+4.4pp over SFT on test), though a 5.65pp dev-to-test gap reveals implicit overfitting to development annotation styles. Our results characterize the fundamental tension between faithfulness and extraction performance in generative IE.\n\\end{abstract}\n\n\\section{Introduction}\n\nDocument-level relation extraction (DocRE) has advanced rapidly with encoder-based models surpassing 60 Ign-F1 on DocRED. Recent work demonstrates that generative LLMs approach competitive extraction accuracy, yet no existing method produces verifiable evidence---the textual passages that justify each extracted relation. This absence constitutes a deployment barrier: users cannot verify whether an extraction reflects genuine textual support or model hallucination.\n\nWe define \\textit{evidence-grounded DocRE} as the task of jointly generating relation triples and supporting evidence sentences. This formulation differs fundamentally from encoder-based evidence \\textit{retrieval} (SAIS, DREEAM), which classifies existing sentences as evidence without generating text. In the generative setting, evidence production adds substantial output length, forcing models to allocate capacity across two objectives: accurate extraction and faithful evidence generation.\n\nThis paper characterizes what happens when this dual objective is imposed. We do not propose evidence-grounded DocRE as a solved problem; rather, we expose the costs, failure modes, and scaling behaviors that future methods must contend with. Our contributions are empirical:\n\n\\begin{enumerate}\n\\item We reveal that the evidence tax is \\textbf{scale-dependent}, following a U-shape: beneficial at 1.7B (+6.2pp), costly at 4B ($-7.9$pp), and neutral at 8B ($\\approx 0$pp). This overturns the assumption that evidence always incurs cost.\n\\item We document an \\textbf{evidence-extraction decoupling spectrum} across RL methods, where optimization pressure correlates with decoupling severity---from catastrophic (QLoRA GRPO) to none (RSFT).\n\\item We show that \\textbf{post-hoc BM25 retrieval matches end-to-end generation} in evidence quality, questioning the necessity of integrated evidence production.\n\\item We identify RSFT with NLI-based scoring as the \\textbf{least harmful} training strategy, while exposing its fragility through a 5.65pp dev-to-test degradation and limited cross-dataset transfer.\n\\end{enumerate}\n\n\\section{Task Definition and Evaluation Framework}\n\n\\subsection{Evidence-Grounded DocRE}\n\nGiven a document $D = \\{s_1, \\ldots, s_n\\}$, the model outputs a set of tuples $(h, r, t, E)$ where $h$ is the head entity, $r$ the relation, $t$ the tail entity, and $E$ is a set of evidence sentences supporting the triple.\n\n\\subsection{Metrics}\n\nWe evaluate along three axes:\n\\begin{itemize}\n\\item \\textbf{Extraction}: Ign-F1 and F1 on DocRED (official CodaLab evaluation for test set).\n\\item \\textbf{Evidence quality}: Conditional Evi-F1 (NLI-based soft match) and DREEAM-protocol Evi-F1 (exact sentence index match).\n\\item \\textbf{Decoupling}: EDCR (Evidence-Decoupled Confidence Ratio)---an NLI-based diagnostic measuring the gap between evidence quality and extraction quality per sample.\n\\end{itemize}\n\n\\subsection{EDCR Definition}\n\nEDCR quantifies evidence-extraction decoupling at the method level (Spearman $\\rho = -0.965$ with rel\\_f1 across methods) and per-relation level (orthogonal to Evi-F1: $\\rho = -0.064$, $p=0.58$). A human validation study (Section~\\ref{sec:edcr_human}) reveals its limitations.\n\n\\section{Methods}\n\n\\subsection{Training Paradigms}\n\nAll experiments use Qwen3-4B as the primary model unless stated otherwise. We explore four training paradigms for evidence-grounded DocRE:\n\n\\paragraph{SFT Baseline.} Standard supervised fine-tuning on DocRED with gold evidence annotations. SFT with evidence yields Ign-F1=40.36; without evidence (upper bound), Ign-F1=47.36.\n\n\\paragraph{RSFT (Rejection Sampling Fine-Tuning).} A STaR-like self-improvement approach: generate 8 candidate outputs per document, score with an NLI-based function (CED or flat-NLI), select the top-1, and fine-tune on selected data. CED (Contrastive Evidence Discrimination) uses document-internal hard negatives for scoring; flat-NLI uses direct entailment scores. Both are statistically indistinguishable (paired $t$-test $p=0.44$).\n\n\\paragraph{DPO (Direct Preference Optimization).} Offline preference learning using CED-scored pairs. Exhibits gradual decoupling: rel\\_f1 degrades from 0.4034 (1 epoch) to 0.3429 (3 epochs).\n\n\\paragraph{GRPO (Group Relative Policy Optimization).} Online RL with evidence-weighted rewards. Two configurations: QLoRA (catastrophic decoupling, rel\\_f1=0.014) and bf16 (mild decoupling, $-2$pp).\n\n\\subsection{Post-hoc Evidence Retrieval}\n\nAs a null hypothesis baseline, we train an SFT model without evidence generation, then retrieve evidence post-hoc using BM25 with entity names as queries over the source document.\n\n\\section{Experiments}\n\n\\subsection{Test Set Evaluation}\n\\label{sec:test}\n\nTable~\\ref{tab:test} reports official DocRED test set results.\n\n\\begin{table}[h]\n\\centering\n\\caption{DocRED test set results. Evidence tax = gap between no-evidence and evidence-producing models.}\n\\label{tab:test}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Config} & \\textbf{Test Ign-F1} & \\textbf{Test F1} & \\textbf{Test Evi-F1} & \\textbf{$\\Delta$ vs SFT} \\\\\n\\midrule\nSFT no-evidence & 42.5 & 43.8 & --- & +6.7 \\\\\nSFT baseline & 35.8 & 36.5 & 0.782 & --- \\\\\nRSFT CED s43 & 40.2 & 41.0 & 0.798 & +4.4 \\\\\nRSFT CED s44 & 39.8 & 40.5 & 0.793 & +4.0 \\\\\nRSFT flat-NLI s42 & 39.5 & 40.2 & 0.790 & +3.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRSFT CED achieves the best evidence-producing test performance (Ign-F1=40.2), representing +4.4pp over SFT baseline. However, the dev-to-test degradation is substantial: from 45.85 (dev) to 40.2 (test), a gap of $-5.65$pp. This exceeds SFT no-evidence's gap ($-4.86$pp), exposing CED scoring's implicit overfitting to dev annotation patterns. The evidence tax on test ($-6.7$pp between no-evidence and baseline) confirms that evidence generation burden persists in held-out evaluation.\n\n\\subsection{Evidence-Extraction Decoupling Spectrum}\n\nTable~\\ref{tab:decoupling} characterizes the decoupling spectrum across training paradigms.\n\n\\begin{table}[h]\n\\centering\n\\caption{Evidence-extraction decoupling spectrum. Higher EDCR indicates greater decoupling.}\n\\label{tab:decoupling}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{rel\\_f1} & \\textbf{Evi-F1} & \\textbf{EDCR} \\\\\n\\midrule\nGRPO QLoRA & 0.014 & 0.850 & 0.990 \\\\\nGRPO bf16 (best step) & $\\sim$0.434 & 0.809 & --- \\\\\nDPO bf16 (1ep) & 0.403 & 0.809 & 0.714 \\\\\nDPO bf16 (3ep) & 0.343 & --- & --- \\\\\nRSFT CED (mean) & 0.457 & 0.816 & 0.643 \\\\\nSFT baseline & 0.405 & 0.798 & 0.712 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe spectrum reveals a monotonic relationship between optimization pressure and decoupling severity. QLoRA amplifies mild decoupling to catastrophic levels---this is not inter-task forgetting (the model retains language competence) but intra-task multi-objective competition where evidence reward pressure displaces extraction capacity.\n\n\\subsection{Post-hoc Retrieval vs End-to-End Generation}\n\\label{sec:posthoc}\n\n\\begin{table}[h]\n\\centering\n\\caption{End-to-end evidence generation vs post-hoc BM25 retrieval.}\n\\label{tab:posthoc}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{rel\\_f1} & \\textbf{Evi-F1} & \\textbf{EDCR} & \\textbf{Cost} \\\\\n\\midrule\nRSFT CED (end-to-end) & 0.457 & 0.816 & 0.643 & 1.0$\\times$ \\\\\nSFT + BM25 top-3 (post-hoc) & 0.489 & 0.82 & 0.625 & 0.65$\\times$ + BM25 \\\\\nCED reranker (inference-time) & 0.486 & 0.819 & 0.616 & 8$\\times$ sampling \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPost-hoc BM25 retrieval achieves higher rel\\_f1 (+0.033) and comparable Evi-F1 (0.82 vs 0.816) with substantially lower inference cost. This result questions the fundamental premise of end-to-end evidence generation: if a simple retrieval pipeline achieves equivalent evidence quality without imposing the evidence tax during training, the cost-benefit of integrated evidence production is negative. We present this as the null hypothesis that should have been tested first.\n\n\\subsection{Evidence Tax Scaling (U-Shape Pattern)}\n\n\\begin{table}[h]\n\\centering\n\\caption{Evidence tax across model scales. Tax = Ign-F1(no-evidence) $-$ Ign-F1(with evidence).}\n\\label{tab:scaling}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{SFT Ign-F1} & \\textbf{RSFT Ign-F1} & \\textbf{$\\Delta$ RSFT$-$SFT} & \\textbf{Status} \\\\\n\\midrule\nQwen3-1.7B & 47.86 & --- & --- & FAILED \\\\\nQwen3-4B & 40.36 & 45.85 & +5.49 & SUCCESS \\\\\nQwen3-8B & 50.51 & 52.8 & +2.3 & SUCCESS \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{SFT-level evidence tax across scales and model families.}\n\\label{tab:utax}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Model} & \\textbf{Evidence Tax} & \\textbf{Direction} \\\\\n\\midrule\nQwen3-1.7B & +6.2pp & Benefit (implicit regularization) \\\\\nQwen3-4B & $-7.9$pp & Cost \\\\\nQwen3-8B & $\\approx 0$ & Neutral \\\\\nLLaMA-3.1-8B & $-0.7$pp & Near-neutral (cross-family) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe U-shape pattern holds at the SFT level: small models benefit from evidence as implicit regularization against overfitting, mid-size models lack capacity to jointly optimize both objectives, and large models absorb the burden. However, RSFT scaling reveals diminishing returns: Qwen3-8B RSFT gains only +2.3pp (vs 4B's +5.5pp), and 1.7B RSFT fails entirely due to low candidate quality (mean\\_f1 $< 0.3$ among generated candidates). The U-shape is thus an SFT-level observation, not a general scaling law for evidence-grounded IE.\n\n\\subsection{Cross-Dataset Evaluation (Re-DocRED)}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-dataset transfer to Re-DocRED.}\n\\label{tab:redocred}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Config} & \\textbf{Re-DocRED Ign-F1} & \\textbf{Evi-F1} & \\textbf{$\\Delta$ vs DocRED} \\\\\n\\midrule\nSFT baseline & 36.59 & 0.817 & $-3.15$pp \\\\\nSFT no-evidence & 41.8 & --- & --- \\\\\nRSFT CED & 38.1 & 0.801 & $-7.75$pp vs DocRED RSFT \\\\\nEvidence tax & $-5.2$pp & --- & vs DocRED $-7.9$pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRSFT's advantage shrinks dramatically on Re-DocRED (+1.5pp over SFT, vs +5.5pp on DocRED), exposing CED scoring's dataset-specificity. The CED scorer, while trained on NLI data, implicitly overfits to DocRED's annotation distribution during RSFT data selection. Evidence extraction quality, however, transfers robustly (Evi-F1=0.801), suggesting the evidence generation capability itself generalizes while the relation extraction boost does not.\n\n\\subsection{DREEAM-Protocol Evidence Evaluation}\n\n\\begin{table}[h]\n\\centering\n\\caption{Evidence evaluation under two protocols. Conditional Evi-F1 uses NLI-based soft matching; DREEAM-protocol requires exact sentence index match.}\n\\label{tab:dreeam}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Conditional Evi-F1} & \\textbf{DREEAM Evi-F1} & \\textbf{Shrinkage} \\\\\n\\midrule\nDREEAM (RoBERTa-large) & --- & 0.540 & --- \\\\\nFREIGE SFT & 0.798 & 0.22 & $-72\\%$ \\\\\nFREIGE RSFT CED & 0.816 & 0.28 & $-66\\%$ \\\\\nFREIGE GRPO bf16 & 0.809 & 0.25 & $-69\\%$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder the strict DREEAM protocol (exact sentence index matching), all generative methods score below 0.30---far below DREEAM's extractive baseline of 0.54. The 66--72\\% shrinkage from conditional to exact evaluation reflects a fundamental protocol mismatch: generative models paraphrase, merge, and restate evidence rather than pointing to exact sentence indices. This does not invalidate the generated evidence (NLI verification confirms semantic adequacy) but reveals that no established protocol fairly evaluates generative evidence. This evaluation gap is itself a finding warranting community attention.\n\n\\subsection{EDCR Human Validation}\n\\label{sec:edcr_human}\n\n\\begin{table}[h]\n\\centering\n\\caption{EDCR correlation with human judgments of evidence sufficiency ($n=100$).}\n\\label{tab:edcr_human}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{95\\% CI} \\\\\n\\midrule\nSpearman $\\rho$ (EDCR vs human) & 0.31 & [0.12, 0.48] \\\\\nPearson $r$ (EDCR vs human) & 0.27 & [0.08, 0.44] \\\\\nAnnotator $\\kappa$ & 0.52 & [0.40, 0.64] \\\\\nHuman evidence precision & 0.72 & [0.65, 0.79] \\\\\nNLI false positive rate & 0.28 & [0.19, 0.37] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEDCR's per-sample correlation with human judgments is modest ($\\rho=0.31$, statistically significant at $p=0.0018$ but explaining only $\\sim$10\\% of variance). The annotator agreement ($\\kappa=0.52$) itself reflects the inherent subjectivity of evidence sufficiency judgments, imposing an upper bound on any automatic metric's achievable correlation. EDCR's value is directional (high-EDCR samples are more likely to have problematic evidence) rather than precisely calibrated. Its method-level diagnostic utility ($\\rho=-0.965$ with rel\\_f1 across methods) remains unaffected, as aggregate-level correlations do not depend on per-sample calibration.\n\n\\subsection{NLI Model Ablation}\n\n\\begin{table}[h]\n\\centering\n\\caption{Effect of NLI scorer capacity on RSFT outcomes.}\n\\label{tab:nli_ablation}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{NLI Model} & \\textbf{CED Margin} & \\textbf{RSFT rel\\_f1} & \\textbf{RSFT Evi-F1} \\\\\n\\midrule\nDeBERTa-v3-base & 0.48 & 0.457 & 0.816 \\\\\nDeBERTa-v3-large & 0.53 & 0.461 & 0.819 \\\\\n$\\Delta$ (large $-$ base) & +0.05 & +0.004 ($p=0.38$) & +0.003 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nScaling the NLI scorer from base to large yields no significant downstream improvement ($\\Delta$=0.004, $p=0.38$). Combined with the CED vs flat-NLI indistinguishability ($p=0.44$), this reveals that the specific scoring function is a second-order effect---any NLI-based filter suffices, and the bottleneck lies elsewhere (likely in the concept gap between NLI entailment and evidence sufficiency, as the human validation confirms).\n\n\\subsection{Cross-Family Validation (LLaMA-3.1-8B)}\n\n\\begin{table}[h]\n\\centering\n\\caption{LLaMA-3.1-8B cross-family results. RSFT failed due to OOM during candidate generation.}\n\\label{tab:llama}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Experiment} & \\textbf{Status} & \\textbf{Result} \\\\\n\\midrule\nLLaMA SFT (evidence) & Complete & Ign-F1=53.84, Evi-F1=0.815 \\\\\nLLaMA SFT (no-evidence) & Complete & Ign-F1=54.52 \\\\\nLLaMA GRPO QLoRA & Complete & Catastrophic (rel\\_f1$\\approx$0) \\\\\nLLaMA RSFT CED & Failed & OOM during candidate generation \\\\\n\\midrule\n\\multicolumn{2}{l}{Evidence tax (LLaMA-8B)} & $-0.68$pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-family validation confirms two findings: (1) 8B models absorb the evidence tax (LLaMA: $-0.68$pp, consistent with Qwen3-8B $\\approx 0$), and (2) GRPO QLoRA catastrophic decoupling generalizes across architectures. RSFT cross-family validation remains incomplete due to memory constraints during candidate generation---a limitation we report transparently.\n\n\\section{Discussion}\n\n\\paragraph{The evidence generation paradox.} Our results expose a paradox: evidence generation imposes measurable cost on mid-scale models, yet simple post-hoc retrieval achieves equivalent evidence quality without this cost. This suggests that for current model capacities, the faithful generation of evidence is a burden without proportionate benefit over retrieval-based alternatives.\n\n\\paragraph{RSFT as least harmful, not recommended.} RSFT with NLI-based scoring is the least harmful training strategy we found---it improves over SFT baseline (+4.4pp test) without introducing decoupling. But the 5.65pp dev-to-test gap, the dataset-specific nature of its gains (Re-DocRED: +1.5pp only), and the fact that post-hoc retrieval matches its evidence quality without training overhead all argue against positioning it as a solution.\n\n\\paragraph{Evaluation infrastructure gap.} The 66\\% shrinkage between conditional and DREEAM-protocol Evi-F1 reveals that no existing evaluation framework adequately handles generative evidence. The community lacks protocols that distinguish semantically valid paraphrases from incorrect evidence while remaining comparable to extractive baselines.\n\n\\paragraph{EDCR: diagnostic, not metric.} EDCR's per-sample correlation with human judgments ($\\rho=0.31$) is insufficient for use as a standalone evaluation metric. Its value is restricted to method-level diagnostics (identifying pathological training configurations) and per-relation-type difficulty profiling.\n\n\\section{Related Work}\n\n\\paragraph{Evidence in DocRE.} SAIS and DREEAM demonstrate that evidence \\textit{retrieval} (classifying which sentences support a relation) improves encoder-based RE. Crucially, this adds a classification head without increasing output length. Our work studies evidence \\textit{generation}---producing evidence text---which imposes fundamentally different costs. The apparent contradiction (SAIS: evidence helps; our work: evidence costs) resolves through this distinction, further illuminated by our U-shape finding: at 1.7B, even generative evidence helps (+6.2pp), mirroring SAIS's findings in the retrieval setting.\n\n\\paragraph{RL for NLP.} Recent work argues RL fine-tuning naturally mitigates catastrophic forgetting of pre-trained knowledge. Our decoupling phenomenon is distinct: it is not inter-task forgetting (models retain language competence) but intra-task multi-objective competition. QuRL's finding that quantized-vs-full-precision actor divergence grows exponentially directly supports our QLoRA amplification observation.\n\n\\section{Limitations}\n\n\\begin{itemize}\n\\item \\textbf{Absolute performance gap}: Our best test Ign-F1 (40.2) remains far below encoder SOTA ($>$60), limiting immediate practical impact. The analysis value is in characterizing why, not in achieving competitive results.\n\\item \\textbf{RSFT cross-family incomplete}: LLaMA RSFT failed due to memory constraints. Our RSFT conclusions rest on Qwen3 experiments only.\n\\item \\textbf{RSFT scaling}: 1.7B RSFT failed (low candidate quality); the scaling analysis of RSFT itself is limited to 4B and 8B.\n\\item \\textbf{EDCR calibration}: Per-sample $\\rho=0.31$ with human judgments. EDCR should not be used as a standalone metric for individual predictions.\n\\item \\textbf{Generative evidence evaluation}: No established protocol fairly compares generative and extractive evidence. Our conditional Evi-F1 may overestimate quality; DREEAM-protocol underestimates it.\n\\item \\textbf{Single dataset family}: All experiments use DocRED/Re-DocRED. Generalization to other document-level IE benchmarks is untested.\n\\end{itemize}\n\n\\section{Conclusion}\n\nWe present a systematic empirical analysis of what happens when LLMs must justify their extractions with evidence. The cost of faithfulness is real but nuanced: scale-dependent, training-paradigm-sensitive, and potentially unnecessary given that post-hoc retrieval achieves equivalent evidence quality. The evidence-extraction decoupling spectrum reveals that RL optimization pressure creates an intra-task trade-off unique to multi-objective IE, amplified catastrophically by quantization. RSFT emerges as the least harmful approach, though its gains are fragile across evaluation settings. These findings characterize the landscape that future evidence-grounded IE methods must navigate, and expose evaluation infrastructure gaps that the community must address before faithful IE can be reliably benchmarked.\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e621cd91-b77b-456c-8f01-43dc0943276f",
  "isSidechain": false,
  "requestId": "req_011Cb6Z6p8o88KRcMJbVZtbo",
  "type": "assistant",
  "uuid": "050dfe9e-fe30-45b6-99a5-820ff09dcea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TvKwU7zSCgqBe9X3F6YLPr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 154,
      "cache_read_input_tokens": 44114,
      "output_tokens": 6988,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 154,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6988,
          "cache_read_input_tokens": 44114,
          "cache_creation_input_tokens": 154,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 154
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

_source line 18 · 2026-05-16T16:23:48.371Z_

<details><summary>↩ Tool result · `toolu_01L4ApjMirqGUuW8hP7t16xT`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T155803/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "050dfe9e-fe30-45b6-99a5-820ff09dcea2",
  "isSidechain": false,
  "promptId": "e3a72ef5-4fa0-4d72-a416-3b6212473770",
  "type": "user",
  "uuid": "67397c7d-4f46-4b03-ab80-5b30a5dbbdc8",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T155803/worst/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{multirow}\n\\usepackage{tabularx}\n\n\\title{The Cost of Faithfulness: What Happens When LLMs Must Justify Their Extractions}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nWe present an empirical analysis of \\textit{evidence-grounded document-level relation extraction} (DocRE), where LLMs must simultaneously produce relation triples and the textual evidence justifying each extraction. Through systematic experiments across training paradigms (SFT, RSFT, DPO, GRPO), model scales (1.7B--8B), and model families (Qwen3, LLaMA-3.1), we expose three findings. First, requiring evidence generation imposes a scale-dependent \\textit{evidence tax}: 4B models pay $-7.9$pp in extraction F1, while 1.7B models paradoxically benefit (+6.2pp) and 8B models absorb the cost entirely ($\\approx 0$). Second, RL optimization pressure correlates with \\textit{evidence-extraction decoupling} severity---a spectrum from catastrophic (GRPO-QLoRA: rel\\_f1=0.014) through mild (GRPO-bf16: $-2$pp) to none (RSFT)---revealing an intra-task multi-objective trade-off distinct from inter-task forgetting. Third, simple post-hoc BM25 retrieval matches end-to-end evidence generation (Evi-F1: 0.82 vs 0.816) at lower cost, questioning whether the burden of generation is justified. We find RSFT with NLI-based scoring to be the least harmful training strategy (+4.4pp over SFT on test), though a 5.65pp dev-to-test gap reveals implicit overfitting to development annotation styles. Our results characterize the fundamental tension between faithfulness and extraction performance in generative IE.\n\\end{abstract}\n\n\\section{Introduction}\n\nDocument-level relation extraction (DocRE) has advanced rapidly with encoder-based models surpassing 60 Ign-F1 on DocRED. Recent work demonstrates that generative LLMs approach competitive extraction accuracy, yet no existing method produces verifiable evidence---the textual passages that justify each extracted relation. This absence constitutes a deployment barrier: users cannot verify whether an extraction reflects genuine textual support or model hallucination.\n\nWe define \\textit{evidence-grounded DocRE} as the task of jointly generating relation triples and supporting evidence sentences. This formulation differs fundamentally from encoder-based evidence \\textit{retrieval} (SAIS, DREEAM), which classifies existing sentences as evidence without generating text. In the generative setting, evidence production adds substantial output length, forcing models to allocate capacity across two objectives: accurate extraction and faithful evidence generation.\n\nThis paper characterizes what happens when this dual objective is imposed. We do not propose evidence-grounded DocRE as a solved problem; rather, we expose the costs, failure modes, and scaling behaviors that future methods must contend with. Our contributions are empirical:\n\n\\begin{enumerate}\n\\item We reveal that the evidence tax is \\textbf{scale-dependent}, following a U-shape: beneficial at 1.7B (+6.2pp), costly at 4B ($-7.9$pp), and neutral at 8B ($\\approx 0$pp). This overturns the assumption that evidence always incurs cost.\n\\item We document an \\textbf{evidence-extraction decoupling spectrum} across RL methods, where optimization pressure correlates with decoupling severity---from catastrophic (QLoRA GRPO) to none (RSFT).\n\\item We show that \\textbf{post-hoc BM25 retrieval matches end-to-end generation} in evidence quality, questioning the necessity of integrated evidence production.\n\\item We identify RSFT with NLI-based scoring as the \\textbf{least harmful} training strategy, while exposing its fragility through a 5.65pp dev-to-test degradation and limited cross-dataset transfer.\n\\end{enumerate}\n\n\\section{Task Definition and Evaluation Framework}\n\n\\subsection{Evidence-Grounded DocRE}\n\nGiven a document $D = \\{s_1, \\ldots, s_n\\}$, the model outputs a set of tuples $(h, r, t, E)$ where $h$ is the head entity, $r$ the relation, $t$ the tail entity, and $E$ is a set of evidence sentences supporting the triple.\n\n\\subsection{Metrics}\n\nWe evaluate along three axes:\n\\begin{itemize}\n\\item \\textbf{Extraction}: Ign-F1 and F1 on DocRED (official CodaLab evaluation for test set).\n\\item \\textbf{Evidence quality}: Conditional Evi-F1 (NLI-based soft match) and DREEAM-protocol Evi-F1 (exact sentence index match).\n\\item \\textbf{Decoupling}: EDCR (Evidence-Decoupled Confidence Ratio)---an NLI-based diagnostic measuring the gap between evidence quality and extraction quality per sample.\n\\end{itemize}\n\n\\subsection{EDCR Definition}\n\nEDCR quantifies evidence-extraction decoupling at the method level (Spearman $\\rho = -0.965$ with rel\\_f1 across methods) and per-relation level (orthogonal to Evi-F1: $\\rho = -0.064$, $p=0.58$). A human validation study (Section~\\ref{sec:edcr_human}) reveals its limitations.\n\n\\section{Methods}\n\n\\subsection{Training Paradigms}\n\nAll experiments use Qwen3-4B as the primary model unless stated otherwise. We explore four training paradigms for evidence-grounded DocRE:\n\n\\paragraph{SFT Baseline.} Standard supervised fine-tuning on DocRED with gold evidence annotations. SFT with evidence yields Ign-F1=40.36; without evidence (upper bound), Ign-F1=47.36.\n\n\\paragraph{RSFT (Rejection Sampling Fine-Tuning).} A STaR-like self-improvement approach: generate 8 candidate outputs per document, score with an NLI-based function (CED or flat-NLI), select the top-1, and fine-tune on selected data. CED (Contrastive Evidence Discrimination) uses document-internal hard negatives for scoring; flat-NLI uses direct entailment scores. Both are statistically indistinguishable (paired $t$-test $p=0.44$).\n\n\\paragraph{DPO (Direct Preference Optimization).} Offline preference learning using CED-scored pairs. Exhibits gradual decoupling: rel\\_f1 degrades from 0.4034 (1 epoch) to 0.3429 (3 epochs).\n\n\\paragraph{GRPO (Group Relative Policy Optimization).} Online RL with evidence-weighted rewards. Two configurations: QLoRA (catastrophic decoupling, rel\\_f1=0.014) and bf16 (mild decoupling, $-2$pp).\n\n\\subsection{Post-hoc Evidence Retrieval}\n\nAs a null hypothesis baseline, we train an SFT model without evidence generation, then retrieve evidence post-hoc using BM25 with entity names as queries over the source document.\n\n\\section{Experiments}\n\n\\subsection{Test Set Evaluation}\n\\label{sec:test}\n\nTable~\\ref{tab:test} reports official DocRED test set results.\n\n\\begin{table}[h]\n\\centering\n\\caption{DocRED test set results. Evidence tax = gap between no-evidence and evidence-producing models.}\n\\label{tab:test}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Config} & \\textbf{Test Ign-F1} & \\textbf{Test F1} & \\textbf{Test Evi-F1} & \\textbf{$\\Delta$ vs SFT} \\\\\n\\midrule\nSFT no-evidence & 42.5 & 43.8 & --- & +6.7 \\\\\nSFT baseline & 35.8 & 36.5 & 0.782 & --- \\\\\nRSFT CED s43 & 40.2 & 41.0 & 0.798 & +4.4 \\\\\nRSFT CED s44 & 39.8 & 40.5 & 0.793 & +4.0 \\\\\nRSFT flat-NLI s42 & 39.5 & 40.2 & 0.790 & +3.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRSFT CED achieves the best evidence-producing test performance (Ign-F1=40.2), representing +4.4pp over SFT baseline. However, the dev-to-test degradation is substantial: from 45.85 (dev) to 40.2 (test), a gap of $-5.65$pp. This exceeds SFT no-evidence's gap ($-4.86$pp), exposing CED scoring's implicit overfitting to dev annotation patterns. The evidence tax on test ($-6.7$pp between no-evidence and baseline) confirms that evidence generation burden persists in held-out evaluation.\n\n\\subsection{Evidence-Extraction Decoupling Spectrum}\n\nTable~\\ref{tab:decoupling} characterizes the decoupling spectrum across training paradigms.\n\n\\begin{table}[h]\n\\centering\n\\caption{Evidence-extraction decoupling spectrum. Higher EDCR indicates greater decoupling.}\n\\label{tab:decoupling}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{rel\\_f1} & \\textbf{Evi-F1} & \\textbf{EDCR} \\\\\n\\midrule\nGRPO QLoRA & 0.014 & 0.850 & 0.990 \\\\\nGRPO bf16 (best step) & $\\sim$0.434 & 0.809 & --- \\\\\nDPO bf16 (1ep) & 0.403 & 0.809 & 0.714 \\\\\nDPO bf16 (3ep) & 0.343 & --- & --- \\\\\nRSFT CED (mean) & 0.457 & 0.816 & 0.643 \\\\\nSFT baseline & 0.405 & 0.798 & 0.712 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe spectrum reveals a monotonic relationship between optimization pressure and decoupling severity. QLoRA amplifies mild decoupling to catastrophic levels---this is not inter-task forgetting (the model retains language competence) but intra-task multi-objective competition where evidence reward pressure displaces extraction capacity.\n\n\\subsection{Post-hoc Retrieval vs End-to-End Generation}\n\\label{sec:posthoc}\n\n\\begin{table}[h]\n\\centering\n\\caption{End-to-end evidence generation vs post-hoc BM25 retrieval.}\n\\label{tab:posthoc}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{rel\\_f1} & \\textbf{Evi-F1} & \\textbf{EDCR} & \\textbf{Cost} \\\\\n\\midrule\nRSFT CED (end-to-end) & 0.457 & 0.816 & 0.643 & 1.0$\\times$ \\\\\nSFT + BM25 top-3 (post-hoc) & 0.489 & 0.82 & 0.625 & 0.65$\\times$ + BM25 \\\\\nCED reranker (inference-time) & 0.486 & 0.819 & 0.616 & 8$\\times$ sampling \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPost-hoc BM25 retrieval achieves higher rel\\_f1 (+0.033) and comparable Evi-F1 (0.82 vs 0.816) with substantially lower inference cost. This result questions the fundamental premise of end-to-end evidence generation: if a simple retrieval pipeline achieves equivalent evidence quality without imposing the evidence tax during training, the cost-benefit of integrated evidence production is negative. We present this as the null hypothesis that should have been tested first.\n\n\\subsection{Evidence Tax Scaling (U-Shape Pattern)}\n\n\\begin{table}[h]\n\\centering\n\\caption{Evidence tax across model scales. Tax = Ign-F1(no-evidence) $-$ Ign-F1(with evidence).}\n\\label{tab:scaling}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{SFT Ign-F1} & \\textbf{RSFT Ign-F1} & \\textbf{$\\Delta$ RSFT$-$SFT} & \\textbf{Status} \\\\\n\\midrule\nQwen3-1.7B & 47.86 & --- & --- & FAILED \\\\\nQwen3-4B & 40.36 & 45.85 & +5.49 & SUCCESS \\\\\nQwen3-8B & 50.51 & 52.8 & +2.3 & SUCCESS \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{SFT-level evidence tax across scales and model families.}\n\\label{tab:utax}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Model} & \\textbf{Evidence Tax} & \\textbf{Direction} \\\\\n\\midrule\nQwen3-1.7B & +6.2pp & Benefit (implicit regularization) \\\\\nQwen3-4B & $-7.9$pp & Cost \\\\\nQwen3-8B & $\\approx 0$ & Neutral \\\\\nLLaMA-3.1-8B & $-0.7$pp & Near-neutral (cross-family) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe U-shape pattern holds at the SFT level: small models benefit from evidence as implicit regularization against overfitting, mid-size models lack capacity to jointly optimize both objectives, and large models absorb the burden. However, RSFT scaling reveals diminishing returns: Qwen3-8B RSFT gains only +2.3pp (vs 4B's +5.5pp), and 1.7B RSFT fails entirely due to low candidate quality (mean\\_f1 $< 0.3$ among generated candidates). The U-shape is thus an SFT-level observation, not a general scaling law for evidence-grounded IE.\n\n\\subsection{Cross-Dataset Evaluation (Re-DocRED)}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-dataset transfer to Re-DocRED.}\n\\label{tab:redocred}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Config} & \\textbf{Re-DocRED Ign-F1} & \\textbf{Evi-F1} & \\textbf{$\\Delta$ vs DocRED} \\\\\n\\midrule\nSFT baseline & 36.59 & 0.817 & $-3.15$pp \\\\\nSFT no-evidence & 41.8 & --- & --- \\\\\nRSFT CED & 38.1 & 0.801 & $-7.75$pp vs DocRED RSFT \\\\\nEvidence tax & $-5.2$pp & --- & vs DocRED $-7.9$pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRSFT's advantage shrinks dramatically on Re-DocRED (+1.5pp over SFT, vs +5.5pp on DocRED), exposing CED scoring's dataset-specificity. The CED scorer, while trained on NLI data, implicitly overfits to DocRED's annotation distribution during RSFT data selection. Evidence extraction quality, however, transfers robustly (Evi-F1=0.801), suggesting the evidence generation capability itself generalizes while the relation extraction boost does not.\n\n\\subsection{DREEAM-Protocol Evidence Evaluation}\n\n\\begin{table}[h]\n\\centering\n\\caption{Evidence evaluation under two protocols. Conditional Evi-F1 uses NLI-based soft matching; DREEAM-protocol requires exact sentence index match.}\n\\label{tab:dreeam}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Conditional Evi-F1} & \\textbf{DREEAM Evi-F1} & \\textbf{Shrinkage} \\\\\n\\midrule\nDREEAM (RoBERTa-large) & --- & 0.540 & --- \\\\\nFREIGE SFT & 0.798 & 0.22 & $-72\\%$ \\\\\nFREIGE RSFT CED & 0.816 & 0.28 & $-66\\%$ \\\\\nFREIGE GRPO bf16 & 0.809 & 0.25 & $-69\\%$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder the strict DREEAM protocol (exact sentence index matching), all generative methods score below 0.30---far below DREEAM's extractive baseline of 0.54. The 66--72\\% shrinkage from conditional to exact evaluation reflects a fundamental protocol mismatch: generative models paraphrase, merge, and restate evidence rather than pointing to exact sentence indices. This does not invalidate the generated evidence (NLI verification confirms semantic adequacy) but reveals that no established protocol fairly evaluates generative evidence. This evaluation gap is itself a finding warranting community attention.\n\n\\subsection{EDCR Human Validation}\n\\label{sec:edcr_human}\n\n\\begin{table}[h]\n\\centering\n\\caption{EDCR correlation with human judgments of evidence sufficiency ($n=100$).}\n\\label{tab:edcr_human}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{95\\% CI} \\\\\n\\midrule\nSpearman $\\rho$ (EDCR vs human) & 0.31 & [0.12, 0.48] \\\\\nPearson $r$ (EDCR vs human) & 0.27 & [0.08, 0.44] \\\\\nAnnotator $\\kappa$ & 0.52 & [0.40, 0.64] \\\\\nHuman evidence precision & 0.72 & [0.65, 0.79] \\\\\nNLI false positive rate & 0.28 & [0.19, 0.37] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEDCR's per-sample correlation with human judgments is modest ($\\rho=0.31$, statistically significant at $p=0.0018$ but explaining only $\\sim$10\\% of variance). The annotator agreement ($\\kappa=0.52$) itself reflects the inherent subjectivity of evidence sufficiency judgments, imposing an upper bound on any automatic metric's achievable correlation. EDCR's value is directional (high-EDCR samples are more likely to have problematic evidence) rather than precisely calibrated. Its method-level diagnostic utility ($\\rho=-0.965$ with rel\\_f1 across methods) remains unaffected, as aggregate-level correlations do not depend on per-sample calibration.\n\n\\subsection{NLI Model Ablation}\n\n\\begin{table}[h]\n\\centering\n\\caption{Effect of NLI scorer capacity on RSFT outcomes.}\n\\label{tab:nli_ablation}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{NLI Model} & \\textbf{CED Margin} & \\textbf{RSFT rel\\_f1} & \\textbf{RSFT Evi-F1} \\\\\n\\midrule\nDeBERTa-v3-base & 0.48 & 0.457 & 0.816 \\\\\nDeBERTa-v3-large & 0.53 & 0.461 & 0.819 \\\\\n$\\Delta$ (large $-$ base) & +0.05 & +0.004 ($p=0.38$) & +0.003 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nScaling the NLI scorer from base to large yields no significant downstream improvement ($\\Delta$=0.004, $p=0.38$). Combined with the CED vs flat-NLI indistinguishability ($p=0.44$), this reveals that the specific scoring function is a second-order effect---any NLI-based filter suffices, and the bottleneck lies elsewhere (likely in the concept gap between NLI entailment and evidence sufficiency, as the human validation confirms).\n\n\\subsection{Cross-Family Validation (LLaMA-3.1-8B)}\n\n\\begin{table}[h]\n\\centering\n\\caption{LLaMA-3.1-8B cross-family results. RSFT failed due to OOM during candidate generation.}\n\\label{tab:llama}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Experiment} & \\textbf{Status} & \\textbf{Result} \\\\\n\\midrule\nLLaMA SFT (evidence) & Complete & Ign-F1=53.84, Evi-F1=0.815 \\\\\nLLaMA SFT (no-evidence) & Complete & Ign-F1=54.52 \\\\\nLLaMA GRPO QLoRA & Complete & Catastrophic (rel\\_f1$\\approx$0) \\\\\nLLaMA RSFT CED & Failed & OOM during candidate generation \\\\\n\\midrule\n\\multicolumn{2}{l}{Evidence tax (LLaMA-8B)} & $-0.68$pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-family validation confirms two findings: (1) 8B models absorb the evidence tax (LLaMA: $-0.68$pp, consistent with Qwen3-8B $\\approx 0$), and (2) GRPO QLoRA catastrophic decoupling generalizes across architectures. RSFT cross-family validation remains incomplete due to memory constraints during candidate generation---a limitation we report transparently.\n\n\\section{Discussion}\n\n\\paragraph{The evidence generation paradox.} Our results expose a paradox: evidence generation imposes measurable cost on mid-scale models, yet simple post-hoc retrieval achieves equivalent evidence quality without this cost. This suggests that for current model capacities, the faithful generation of evidence is a burden without proportionate benefit over retrieval-based alternatives.\n\n\\paragraph{RSFT as least harmful, not recommended.} RSFT with NLI-based scoring is the least harmful training strategy we found---it improves over SFT baseline (+4.4pp test) without introducing decoupling. But the 5.65pp dev-to-test gap, the dataset-specific nature of its gains (Re-DocRED: +1.5pp only), and the fact that post-hoc retrieval matches its evidence quality without training overhead all argue against positioning it as a solution.\n\n\\paragraph{Evaluation infrastructure gap.} The 66\\% shrinkage between conditional and DREEAM-protocol Evi-F1 reveals that no existing evaluation framework adequately handles generative evidence. The community lacks protocols that distinguish semantically valid paraphrases from incorrect evidence while remaining comparable to extractive baselines.\n\n\\paragraph{EDCR: diagnostic, not metric.} EDCR's per-sample correlation with human judgments ($\\rho=0.31$) is insufficient for use as a standalone evaluation metric. Its value is restricted to method-level diagnostics (identifying pathological training configurations) and per-relation-type difficulty profiling.\n\n\\section{Related Work}\n\n\\paragraph{Evidence in DocRE.} SAIS and DREEAM demonstrate that evidence \\textit{retrieval} (classifying which sentences support a relation) improves encoder-based RE. Crucially, this adds a classification head without increasing output length. Our work studies evidence \\textit{generation}---producing evidence text---which imposes fundamentally different costs. The apparent contradiction (SAIS: evidence helps; our work: evidence costs) resolves through this distinction, further illuminated by our U-shape finding: at 1.7B, even generative evidence helps (+6.2pp), mirroring SAIS's findings in the retrieval setting.\n\n\\paragraph{RL for NLP.} Recent work argues RL fine-tuning naturally mitigates catastrophic forgetting of pre-trained knowledge. Our decoupling phenomenon is distinct: it is not inter-task forgetting (models retain language competence) but intra-task multi-objective competition. QuRL's finding that quantized-vs-full-precision actor divergence grows exponentially directly supports our QLoRA amplification observation.\n\n\\section{Limitations}\n\n\\begin{itemize}\n\\item \\textbf{Absolute performance gap}: Our best test Ign-F1 (40.2) remains far below encoder SOTA ($>$60), limiting immediate practical impact. The analysis value is in characterizing why, not in achieving competitive results.\n\\item \\textbf{RSFT cross-family incomplete}: LLaMA RSFT failed due to memory constraints. Our RSFT conclusions rest on Qwen3 experiments only.\n\\item \\textbf{RSFT scaling}: 1.7B RSFT failed (low candidate quality); the scaling analysis of RSFT itself is limited to 4B and 8B.\n\\item \\textbf{EDCR calibration}: Per-sample $\\rho=0.31$ with human judgments. EDCR should not be used as a standalone metric for individual predictions.\n\\item \\textbf{Generative evidence evaluation}: No established protocol fairly compares generative and extractive evidence. Our conditional Evi-F1 may overestimate quality; DREEAM-protocol underestimates it.\n\\item \\textbf{Single dataset family}: All experiments use DocRED/Re-DocRED. Generalization to other document-level IE benchmarks is untested.\n\\end{itemize}\n\n\\section{Conclusion}\n\nWe present a systematic empirical analysis of what happens when LLMs must justify their extractions with evidence. The cost of faithfulness is real but nuanced: scale-dependent, training-paradigm-sensitive, and potentially unnecessary given that post-hoc retrieval achieves equivalent evidence quality. The evidence-extraction decoupling spectrum reveals that RL optimization pressure creates an intra-task trade-off unique to multi-objective IE, amplified catastrophically by quantization. RSFT emerges as the least harmful approach, though its gains are fragile across evaluation settings. These findings characterize the landscape that future evidence-grounded IE methods must navigate, and expose evaluation infrastructure gaps that the community must address before faithful IE can be reliably benchmarked.\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "050dfe9e-fe30-45b6-99a5-820ff09dcea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T155803 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie…",
  "leafUuid": "67397c7d-4f46-4b03-ab80-5b30a5dbbdc8",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate empirical analysis paper on LLM faithfulness costs",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc"
}
```

---

### Tool call

_source line 21 · 2026-05-16T16:23:53.033Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KwPgbEzveQLmKX5mJfqfQX`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T155803/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67397c7d-4f46-4b03-ab80-5b30a5dbbdc8",
  "isSidechain": false,
  "requestId": "req_011Cb6ZH1NzxDGDJ9HkKNyEM",
  "type": "assistant",
  "uuid": "0b68d494-a21d-48a7-9efe-998f9c52b6ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193csjRGjTBiNuDV7erdsWP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7053,
      "cache_read_input_tokens": 44268,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 44268,
          "cache_creation_input_tokens": 7053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7053
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

_source line 22 · 2026-05-16T16:23:54.634Z_

<details><summary>↩ Tool result · `toolu_01KwPgbEzveQLmKX5mJfqfQX`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
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
Overfull \hbox (1.07927pt too wide) in paragraph at lines 34--35
\OT1/cmr/m/n/10.95 op-ti-miza-tion pres-sure cor-re-lates with de-cou-pling sev
erity---from catas-trophic (QLoRA GRPO)
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

LaTeX Warning: Reference `sec:edcr_human' on page 2 undefined on input line 56.


[2]

LaTeX Warning: Reference `tab:test' on page 3 undefined on input line 81.


LaTeX Warning: Reference `tab:decoupling' on page 3 undefined on input line 104
.

[3]

LaTeX Warning: `h' float specifier changed to `ht'.

[4] [5]
Overfull \hbox (7.78308pt too wide) in paragraph at lines 260--261
[]\OT1/cmr/m/n/10.95 Scaling the NLI scorer from base to large yields no sig-ni
f-i-cant down-stream im-prove-ment ($^^A$=0.004,

Overfull \hbox (4.51767pt too wide) in paragraph at lines 290--291
 []\OT1/cmr/bx/n/10.95 Evaluation in-fras-truc-ture gap.[] \OT1/cmr/m/n/10.95 T
he 66% shrink-age be-tween con-di-tional and DREEAM-protocol
[6] [7] [8] (./paper.aux)
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 tcrm1095
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input tcrm1095
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm1095.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymb.mf
 Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf
 Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [27] [29])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txgen.mf
 Ok [100] [109] [98] [99] [108])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymbol.mf
 Ok [13] [18] [21] [22] [23] [24] [25] [26] [28] [31] [32] [36] [39] [44]
[45] [46] [42] [47] [60] [61] [62] [77] [79] [87] [110] [91] [93] [94] [95]
[96] [126] [127] [128] [129] [130] [131] [132] [133] [134] [135] [136] [137]
[138] [139] [140] [141] [142] [143] [144] [145] [146] [147] [148] [149]
[150] [151] [152] [153] [154] [155] [156] [157] [158] [159] [160] [161]
[162] [163] [164] [165] [166] [167] [168] [169] [171] [172] [173] [174]
[175] [177] [176] [180] [181] [182] [183] [184] [187] [191] [214] [246])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txromod.mf
 Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrsuper.mf
 Ok [185] [178] [179] [170] [186])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrfract.mf
 Ok [188] [189] [190]) ) ) )
(some charht values had to be adjusted by as much as 0.06952pt)
Font metrics written on tcrm1095.tfm.
Output written on tcrm1095.600gf (128 characters, 25592 bytes).
Transcript written on tcrm1095.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk: successfully generated.


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
type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
r17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>
Output written on paper.pdf (8 pages, 157202 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
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
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
Overfull \hbox (1.07927pt too wide) in paragraph at lines 34--35
\OT1/cmr/m/n/10.95 op-ti-miza-tion pres-sure cor-re-lates with de-cou-pling sev
erity---from catas-trophic (QLoRA GRPO)
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2] [3]

LaTeX Warning: `h' float specifier changed to `ht'.

[4] [5]
Overfull \hbox (7.78308pt too wide) in paragraph at lines 260--261
[]\OT1/cmr/m/n/10.95 Scaling the NLI scorer from base to large yields no sig-ni
f-i-cant down-stream im-prove-ment ($^^A$=0.004,

Overfull \hbox (4.51767pt too wide) in paragraph at lines 290--291
 []\OT1/cmr/bx/n/10.95 Evaluation in-fras-truc-ture gap.[] \OT1/cmr/m/n/10.95 T
he 66% shrink-age be-tween con-di-tional and DREEAM-protocol
[6] [7] [8] (./paper.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
r17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>
Output written on paper.pdf (8 pages, 158602 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b68d494-a21d-48a7-9efe-998f9c52b6ed",
  "isSidechain": false,
  "promptId": "e3a72ef5-4fa0-4d72-a416-3b6212473770",
  "type": "user",
  "uuid": "c1e33a23-3b2c-474b-9bdf-a60d86ceeac0",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (1.07927pt too wide) in paragraph at lines 34--35\n\\OT1/cmr/m/n/10.95 op-ti-miza-tion pres-sure cor-re-lates with de-cou-pling sev\nerity---from catas-trophic (QLoRA GRPO)\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nLaTeX Warning: Reference `sec:edcr_human' on page 2 undefined on input line 56.\n\n\n[2]\n\nLaTeX Warning: Reference `tab:test' on page 3 undefined on input line 81.\n\n\nLaTeX Warning: Reference `tab:decoupling' on page 3 undefined on input line 104\n.\n\n[3]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[4] [5]\nOverfull \\hbox (7.78308pt too wide) in paragraph at lines 260--261\n[]\\OT1/cmr/m/n/10.95 Scaling the NLI scorer from base to large yields no sig-ni\nf-i-cant down-stream im-prove-ment ($^^A$=0.004,\n\nOverfull \\hbox (4.51767pt too wide) in paragraph at lines 290--291\n []\\OT1/cmr/bx/n/10.95 Evaluation in-fras-truc-ture gap.[] \\OT1/cmr/m/n/10.95 T\nhe 66% shrink-age be-tween con-di-tional and DREEAM-protocol\n[6] [7] [8] (./paper.aux)\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 tcrm1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input tcrm1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymb.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [27] [29])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txgen.mf\n Ok [100] [109] [98] [99] [108])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymbol.mf\n Ok [13] [18] [21] [22] [23] [24] [25] [26] [28] [31] [32] [36] [39] [44]\n[45] [46] [42] [47] [60] [61] [62] [77] [79] [87] [110] [91] [93] [94] [95]\n[96] [126] [127] [128] [129] [130] [131] [132] [133] [134] [135] [136] [137]\n[138] [139] [140] [141] [142] [143] [144] [145] [146] [147] [148] [149]\n[150] [151] [152] [153] [154] [155] [156] [157] [158] [159] [160] [161]\n[162] [163] [164] [165] [166] [167] [168] [169] [171] [172] [173] [174]\n[175] [177] [176] [180] [181] [182] [183] [184] [187] [191] [214] [246])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txromod.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrsuper.mf\n Ok [185] [178] [179] [170] [186])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrfract.mf\n Ok [188] [189] [190]) ) ) )\n(some charht values had to be adjusted by as much as 0.06952pt)\nFont metrics written on tcrm1095.tfm.\nOutput written on tcrm1095.600gf (128 characters, 25592 bytes).\nTranscript written on tcrm1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk: successfully generated.\n\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>\nOutput written on paper.pdf (8 pages, 157202 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (1.07927pt too wide) in paragraph at lines 34--35\n\\OT1/cmr/m/n/10.95 op-ti-miza-tion pres-sure cor-re-lates with de-cou-pling sev\nerity---from catas-trophic (QLoRA GRPO)\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2] [3]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[4] [5]\nOverfull \\hbox (7.78308pt too wide) in paragraph at lines 260--261\n[]\\OT1/cmr/m/n/10.95 Scaling the NLI scorer from base to large yields no sig-ni\nf-i-cant down-stream im-prove-ment ($^^A$=0.004,\n\nOverfull \\hbox (4.51767pt too wide) in paragraph at lines 290--291\n []\\OT1/cmr/bx/n/10.95 Evaluation in-fras-truc-ture gap.[] \\OT1/cmr/m/n/10.95 T\nhe 66% shrink-age be-tween con-di-tional and DREEAM-protocol\n[6] [7] [8] (./paper.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>\nOutput written on paper.pdf (8 pages, 158602 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0b68d494-a21d-48a7-9efe-998f9c52b6ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T155803/worst",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-16T16:24:02.262Z_

编译成功，8 页 PDF 无错误。论文已写入 `paper.tex` 并编译为 `paper.pdf`，覆盖全部 8 个实验（test set evaluation、Re-DocRED cross-dataset、EDCR human validation、DREEAM-protocol alignment、post-hoc retrieval baseline、NLI model ablation、1.7B/8B scaling、LLaMA cross-family），按 narrative guidance 重新定位为 empirical analysis paper，RSFT 降级为 "least harmful"，post-hoc retrieval 追平作为正文核心发现。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1e33a23-3b2c-474b-9bdf-a60d86ceeac0",
  "isSidechain": false,
  "requestId": "req_011Cb6ZHU4rioHTh4VzcDedg",
  "type": "assistant",
  "uuid": "21687f38-b9a4-4c1c-97b8-4637074c4dd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T155803/worst",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SBLd7dGqemjgjwYC8mVa5Q",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6669,
      "cache_read_input_tokens": 51321,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6669,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 51321,
          "cache_creation_input_tokens": 6669,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6669
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

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T155803 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie…",
  "leafUuid": "21687f38-b9a4-4c1c-97b8-4637074c4dd6",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate empirical analysis paper on LLM faithfulness costs",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T155803 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie…",
  "leafUuid": "21687f38-b9a4-4c1c-97b8-4637074c4dd6",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate empirical analysis paper on LLM faithfulness costs",
  "sessionId": "3f919891-e40b-48de-b5ba-d9c1d745dedc"
}
```

---
